"""Predictions 27-29: ALBUS's gain mechanism head to head with avoidance.

Declared in AMENDMENT_7.md (commit 156c626) before this file existed. The gain
mapping gamma(d) = gamma_0 * (1 - d) * (1 + A d) nests the preregistered REBUS
mapping at A = 0. The acting agent is reused unchanged: run_batch computes
gamma_0 * (1 - dose), so the gain mapping is passed through an effective dose
d_eff = 1 - (1 - d)(1 + A d), which is exact, not an approximation.
"""

import json
import pathlib
import time

import numpy as np

from acting import MALADAPTIVE, TRUE, baseline_conviction, run_batch
from acting import K as K_ACT
from model import GAMMA_0, K, likelihood, prior_logits, softmax

OUT = pathlib.Path(__file__).parent / "gain_results.json"

AS = (0.0, 1.0, 2.0, 4.0)
DOSES = np.round(np.linspace(0, 1, 41), 4)
COSTS = (0.0, 0.3, 0.5)
TRIALS = 20_000
G0_ACT, R_ACT, C_CONS = 3.0, 0.85, 0.8
WINDOW_PASSIVE = 12


def gain_factor(d, A):
    return (1.0 - d) * (1.0 + A * d)


def passive_block(rng):
    """Window-end conviction vs dose per A, paired draws, r in {0.30, 0.55}."""
    u = prior_logits()
    base = float(softmax(GAMMA_0 * u)[MALADAPTIVE])
    out = {"baseline": base, "curves": {}}
    for r in (0.30, 0.55):
        a = likelihood(r)
        counts = rng.multinomial(WINDOW_PASSIVE, a[:, TRUE], size=TRIALS)
        cum = counts @ np.log(a)
        for A in AS:
            ys = []
            for d in DOSES:
                logits = GAMMA_0 * gain_factor(d, A) * u[None, :] + cum
                logits -= logits.max(axis=1, keepdims=True)
                b = np.exp(logits)
                b /= b.sum(axis=1, keepdims=True)
                ys.append(float(b[:, MALADAPTIVE].mean()))
            out["curves"][f"{r}|{A}"] = ys
    return out


def acting_block(rng):
    """Window-end conviction, deep usage, and consolidated lasting outcome."""
    base = baseline_conviction(G0_ACT)
    u = np.zeros(K_ACT)
    u[MALADAPTIVE] = 1.0
    logits = G0_ACT * u
    p_orig = np.exp(logits - logits.max())
    p_orig = p_orig / p_orig.sum()

    out = {"baseline": base, "grid": {}}
    t0 = time.time()
    for A in AS:
        for cost in COSTS:
            for d in DOSES:
                d_eff = 1.0 - gain_factor(d, A)
                b, deep = run_batch(d_eff, R_ACT, rng, TRIALS, gamma_0=G0_ACT,
                                    confusable=True, deep_cost=cost)
                p_after = (1.0 - C_CONS) * p_orig[None, :] + C_CONS * b
                m = p_after.argmax(axis=1)
                out["grid"][f"{A}|{cost}|{d}"] = {
                    "conviction": float(b[:, MALADAPTIVE].mean()),
                    "deep_rate": float(deep.mean()),
                    "lasting_conviction": float(p_after[:, MALADAPTIVE].mean()),
                    "lasting_insight": float((m == TRUE).mean()),
                }
        print(f"A={A} done at {time.time()-t0:.0f}s")
    return out


def main():
    rng = np.random.default_rng(11)
    passive = passive_block(rng)
    acting = acting_block(rng)
    OUT.write_text(json.dumps({
        "config": {"As": list(AS), "doses": DOSES.tolist(), "costs": list(COSTS),
                   "trials": TRIALS, "c_cons": C_CONS},
        "passive": passive, "acting": acting}))
    print(f"wrote {OUT.name}\n")

    g = lambda A, c, d: acting["grid"][f"{A}|{c}|{d}"]
    base_a = acting["baseline"]

    print("=== P27 passive: window-end conviction vs pre-dose baseline "
          f"({passive['baseline']:.4f}) ===")
    for r in (0.3, 0.55):
        for A in AS:
            ys = passive["curves"][f"{r}|{A}"]
            above = [d for d, y in zip(DOSES, ys) if y > passive["baseline"]]
            rng_s = f"{min(above):.2f} to {max(above):.2f}" if above else "none"
            print(f"  r={r} A={A}: peak {max(ys):.4f} at d={DOSES[int(np.argmax(ys))]:.2f}, "
                  f"SEBUS dose range {rng_s}")

    print(f"\n=== P27 acting, free test: conviction vs baseline ({base_a:.4f}) ===")
    for A in AS:
        ys = [g(A, 0.0, d)["conviction"] for d in DOSES]
        above = [d for d, y in zip(DOSES, ys) if y > base_a]
        rng_s = f"{min(above):.2f} to {max(above):.2f}" if above else "none"
        print(f"  A={A}: peak {max(ys):.4f}, SEBUS range {rng_s}")

    print("\n=== P28 mediator: deep usage, low dose vs dose zero ===")
    for A in AS:
        for cost in COSTS:
            u0 = g(A, cost, 0.0)["deep_rate"]
            low = min(g(A, cost, d)["deep_rate"] for d in DOSES if 0 < d <= 0.5)
            print(f"  A={A} cost={cost}: usage(d=0) {u0:.3f}, "
                  f"min usage in (0,0.5] {low:.3f}, dip {'YES' if low < u0 - 0.005 else 'no'}")

    print("\n=== P29a SEBUS region size (window-end conviction > baseline) ===")
    for A in (0.0, 2.0, 4.0):
        for cost in COSTS:
            above = [d for d in DOSES if g(A, cost, d)["conviction"] > base_a]
            rng_s = f"{min(above):.2f} to {max(above):.2f}" if above else "none"
            print(f"  A={A} cost={cost}: {rng_s}")

    print("\n=== P29b lasting entrenchment (lasting conviction > baseline) ===")
    for A in AS:
        for cost in COSTS:
            above = [d for d in DOSES if g(A, cost, d)["lasting_conviction"] > base_a]
            rng_s = f"{min(above):.2f} to {max(above):.2f}" if above else "none"
            print(f"  A={A} cost={cost}: {rng_s}")


if __name__ == "__main__":
    main()
