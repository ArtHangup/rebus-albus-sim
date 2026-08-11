"""Predictions 38-41: the ratchet. Capture plus avoidance across sessions.

Declared in AMENDMENT_10.md (commit ca798a0) before this file existed. The acting
model's within-session mechanics are unchanged (probe_set and epistemic_values are
imported from acting.py); the stored prior evolves per trial across sessions with
the capture-weighted stepwise increment of AMENDMENT_8/9.
"""

import json
import pathlib
import time

import numpy as np

from acting import K, MALADAPTIVE, TRUE, epistemic_values, probe_set

OUT = pathlib.Path(__file__).parent / "ratchet_results.json"

R = 0.85
ALPHA = 8.0
STEPS = 14
N0 = 20.0
CONV0 = 0.8007
E = 10.0
TRIALS = 10_000
HORIZON = 40


def init_prior():
    p2 = np.full(K, (1.0 - CONV0) / (K - 1))
    p2[MALADAPTIVE] = CONV0
    return np.tile(p2, (TRIALS, 1))


def one_session(p2, d, cost, kappa, rng):
    """One acting session. Returns (increment, deep usage, window-end belief)."""
    probes = probe_set(R, confusable=True, k=K)
    n_probes = probes.shape[0]
    deep_idx = n_probes - 1
    n = p2.shape[0]
    idx = np.arange(n)

    w = 1.0 - d
    logits = w * np.log(np.maximum(p2, 1e-300))
    logits -= logits.max(axis=1, keepdims=True)
    b = np.exp(logits)
    b /= b.sum(axis=1, keepdims=True)

    occ = np.zeros((n, K))
    deep = np.zeros(n)
    for _ in range(STEPS):
        ev = epistemic_values(b, probes)
        ev[:, deep_idx] -= cost
        wts = np.exp(ALPHA * (ev - ev.max(axis=1, keepdims=True)))
        wts /= wts.sum(axis=1, keepdims=True)
        choice = (wts.cumsum(axis=1) < rng.random((n, 1))).sum(axis=1)
        choice = np.minimum(choice, n_probes - 1)
        deep += (choice == deep_idx)

        a = probes[choice]                                   # (n, 2, K)
        obs = (rng.random(n) >= a[:, 0, TRUE]).astype(int)   # 0 = "yes"
        lik = a[idx, obs, :]

        lq = kappa * np.log(np.maximum(b, 1e-300)) + np.log(np.maximum(lik, 1e-300))
        lq -= lq.max(axis=1, keepdims=True)
        q = np.exp(lq)
        q /= q.sum(axis=1, keepdims=True)
        occ += q

        b = b * lik
        b /= b.sum(axis=1, keepdims=True)

    inc = occ / occ.sum(axis=1, keepdims=True)
    return inc, deep / STEPS, b


def run_protocol(doses, cost, kappa, mass, rng):
    p2 = init_prior()
    N = N0
    traj = []
    for d in doses:
        inc, deep, _ = one_session(p2, d, cost, kappa, rng)
        p2 = (N * p2 + E * inc) / (N + E)
        if mass == "accum":
            N += E
        traj.append((float(p2[:, MALADAPTIVE].mean()),
                     float((p2.argmax(axis=1) == TRUE).mean()),
                     float(deep.mean())))
    return traj


def s50(traj):
    for i, (_, ins, _) in enumerate(traj):
        if ins >= 0.5:
            return i + 1
    return None


def main():
    rng = np.random.default_rng(11)
    t0 = time.time()
    results = {"config": {"r": R, "alpha": ALPHA, "steps": STEPS, "N0": N0,
                          "conv0": CONV0, "E": E, "trials": TRIALS,
                          "horizon": HORIZON},
               "natural": {}, "treatment": {}}

    # Protocol 1: natural history
    for cost in (0.0, 0.3, 0.8):
        for kappa in (1.0, 3.0):
            for mass in ("fixed", "accum"):
                traj = run_protocol([0.0] * HORIZON, cost, kappa, mass, rng)
                results["natural"][f"{cost}|{kappa}|{mass}"] = traj
        print(f"natural cost {cost} done at {time.time()-t0:.0f}s")

    # Protocol 2: treatment, kappa = 3
    for cost in (0.3, 0.8, 1.2):
        for j in (5, 20):
            for d in (0.2, 0.6, 1.0):
                traj = run_protocol([0.0] * j + [d] * HORIZON, cost, 3.0,
                                    "fixed", rng)
                results["treatment"][f"{cost}|fixed|{j}|{d}"] = {
                    "course": s50(traj[j:]),
                    "traj": traj,
                }
        print(f"treatment cost {cost} done at {time.time()-t0:.0f}s")
    for d in (0.2, 0.6, 1.0):
        traj = run_protocol([0.0] * 20 + [d] * HORIZON, 0.3, 3.0, "accum", rng)
        results["treatment"][f"0.3|accum|20|{d}"] = {"course": s50(traj[20:]),
                                                     "traj": traj}

    OUT.write_text(json.dumps(results))
    print(f"wrote {OUT.name}\n")

    # ---- summaries ----
    print(f"=== P38 natural history: stored conviction (start {CONV0}) ===")
    for cost in (0.0, 0.3, 0.8):
        for kappa in (1.0, 3.0):
            traj = results["natural"][f"{cost}|{kappa}|fixed"]
            marks = "  ".join(f"s{s}: {traj[s-1][0]:.3f}" for s in (1, 5, 10, 20, 40))
            print(f"  cost {cost} kappa {kappa} (fixed): {marks}  S50: {s50(traj)}")

    print("\n=== P38 mediator: deep usage across sessions (cost 0.3, fixed) ===")
    for kappa in (1.0, 3.0):
        traj = results["natural"][f"0.3|{kappa}|fixed"]
        marks = "  ".join(f"s{s}: {traj[s-1][2]:.3f}" for s in (1, 5, 10, 20, 40))
        print(f"  kappa {kappa}: {marks}")

    print("\n=== P39/P40 treatment courses (kappa 3, fixed mass) ===")
    print(f"{'cost':>6}{'j':>4}" + "".join(f"{f'd={d}':>8}" for d in (0.2, 0.6, 1.0)))
    for cost in (0.3, 0.8, 1.2):
        for j in (5, 20):
            row = f"{cost:>6}{j:>4}"
            for d in (0.2, 0.6, 1.0):
                c = results["treatment"][f"{cost}|fixed|{j}|{d}"]["course"]
                row += f"{str(c) if c else 'never':>8}"
            print(row)

    print("\n=== P39 harmful subthreshold check: conviction at horizon ===")
    for cost in (0.3, 0.8):
        nat = results["natural"][f"{cost}|3.0|fixed"][-1][0]
        tr = results["treatment"][f"{cost}|fixed|5|0.2"]["traj"][-1][0]
        print(f"  cost {cost}: untreated s40 conviction {nat:.3f}, "
              f"sustained d=0.2 (after j=5) end conviction {tr:.3f}")


if __name__ == "__main__":
    main()
