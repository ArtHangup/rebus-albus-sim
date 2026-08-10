"""Predictions 24-26: the therapeutic window in cost, dose, and consolidation timing.

Declared in AMENDMENT_6.md (commit 6d4e093) before this file existed. The agent and
its dynamics are byte-identical to the costly-test arm (acting.py / run_cost.py); the
only additions are measurement-side: the belief trajectory is recorded at every step,
and the arithmetic consolidation of AMENDMENT_1 is applied to the belief at step t_c.
"""

import json
import pathlib
import time

import numpy as np

from acting import K, MALADAPTIVE, TRUE, baseline_conviction, epistemic_values, probe_set

OUT = pathlib.Path(__file__).parent / "window_results.json"

G0, R, ALPHA, STEPS, TRIALS = 3.0, 0.85, 8.0, 14, 20_000
COSTS = (0.0, 0.3, 0.5, 0.8, 1.2)
DOSES = np.round(np.linspace(0, 1, 21), 3)
TCS = list(range(1, STEPS + 1))
CONS = (0.6, 0.8, 1.0)


def run_batch_traj(dose, r, rng, n, gamma_0=G0, steps=STEPS, alpha=ALPHA,
                   deep_cost=0.0):
    """run_batch from acting.py with the belief recorded after every step.

    Returns beliefs of shape (steps, n, K): beliefs[t] is the state after t+1
    decisions, so t_c = t + 1 in the amendment's numbering.
    """
    probes = probe_set(r, confusable=True, k=K)
    n_probes = probes.shape[0]
    deep_idx = n_probes - 1

    u = np.zeros(K)
    u[MALADAPTIVE] = 1.0
    logits = gamma_0 * (1.0 - dose) * u
    b = np.exp(logits - logits.max())
    b = np.tile(b / b.sum(), (n, 1))

    idx = np.arange(n)
    traj = np.empty((steps, n, K))
    for t in range(steps):
        ev = epistemic_values(b, probes)
        ev[:, deep_idx] -= deep_cost
        w = np.exp(alpha * (ev - ev.max(axis=1, keepdims=True)))
        w /= w.sum(axis=1, keepdims=True)
        choice = (w.cumsum(axis=1) < rng.random((n, 1))).sum(axis=1)
        choice = np.minimum(choice, n_probes - 1)

        a = probes[choice]
        obs = (rng.random(n) >= a[:, 0, TRUE]).astype(int)
        b = b * a[idx, obs, :]
        b /= b.sum(axis=1, keepdims=True)
        traj[t] = b
    return traj


def main():
    rng = np.random.default_rng(11)
    base = baseline_conviction(G0)
    u = np.zeros(K)
    u[MALADAPTIVE] = 1.0
    logits = G0 * u
    p_orig = np.exp(logits - logits.max())
    p_orig = p_orig / p_orig.sum()

    t0 = time.time()
    results = {"config": {"gamma_0": G0, "r": R, "alpha": ALPHA, "steps": STEPS,
                          "trials": TRIALS, "costs": list(COSTS),
                          "doses": DOSES.tolist(), "tcs": TCS, "cons": list(CONS),
                          "baseline": base},
               "grid": {}, "traj_conviction": {}}

    for cost in COSTS:
        for d in DOSES:
            traj = run_batch_traj(d, R, rng, TRIALS, deep_cost=cost)
            # mean within-window conviction trajectory, for prediction 25
            results["traj_conviction"][f"{cost}|{d}"] = \
                traj[:, :, MALADAPTIVE].mean(axis=1).round(6).tolist()
            for tc in TCS:
                bw = traj[tc - 1]
                for c in CONS:
                    p_after = (1.0 - c) * p_orig[None, :] + c * bw
                    m = p_after.argmax(axis=1)
                    results["grid"][f"{cost}|{d}|{tc}|{c}"] = {
                        "conviction": float(p_after[:, MALADAPTIVE].mean()),
                        "insight": float((m == TRUE).mean()),
                    }
        print(f"cost {cost} done at {time.time()-t0:.0f}s")

    OUT.write_text(json.dumps(results))
    print(f"wrote {OUT.name}")

    # ---- Prediction 24: dose-gated benefit at t_c = 14, c = 0.8 ----
    print("\n=== P24: lasting conviction vs dose at t_c=14, c=0.8 ===")
    print("* = above the no-session baseline (session entrenches)")
    print(f"{'dose':>6}" + "".join(f"{f'cost {c}':>12}" for c in COSTS))
    for d in DOSES[::2]:
        row = f"{d:>6.2f}"
        for c in COSTS:
            v = results["grid"][f"{c}|{d}|14|0.8"]["conviction"]
            row += f"{v:>11.4f}" + ("*" if v > base else " ")
        print(row)

    # ---- Prediction 25: within-window trajectory shape ----
    print("\n=== P25: mean conviction trajectory (cost 0.5) ===")
    print(f"{'step':>5}" + "".join(f"{f'd={d}':>9}" for d in (0.0, 0.25, 0.5, 0.75, 1.0)))
    for t in range(STEPS):
        row = f"{t+1:>5d}"
        for d in (0.0, 0.25, 0.5, 0.75, 1.0):
            row += f"{results['traj_conviction'][f'0.5|{d}'][t]:>9.4f}"
        print(row)

    # ---- Prediction 26: does dose ever add lasting conviction? ----
    print("\n=== P26: max over (cost,tc,c) of conviction(d) - conviction(0) ===")
    worst = -1.0
    worst_cell = None
    for cost in COSTS:
        for tc in TCS:
            for c in CONS:
                v0 = results["grid"][f"{cost}|0.0|{tc}|{c}"]["conviction"]
                for d in DOSES[1:]:
                    v = results["grid"][f"{cost}|{d}|{tc}|{c}"]["conviction"]
                    if v - v0 > worst:
                        worst, worst_cell = v - v0, (cost, float(d), tc, c)
    print(f"max excess = {worst:+.4f} at (cost, dose, t_c, c) = {worst_cell}")


if __name__ == "__main__":
    main()
