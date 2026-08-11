"""Predictions 30-33: hierarchy, learning, and whether either dissolves the fork.

Declared in AMENDMENT_8.md (commit ab55a19) before this file existed. Two-level
model; persistence through Dirichlet-mean learning on the stored level-2 prior;
precision (dose) applied at use time only and never to the stored counts.
"""

import json
import pathlib
import time

import numpy as np

OUT = pathlib.Path(__file__).parent / "hierarchy_results.json"

K = 6
TRUE = 0
MALADAPTIVE = 1
Q = 0.8
T = 12
N0 = 20.0
CONV0 = 0.8007
TRIALS = 20_000
DOSES = np.round(np.linspace(0, 1, 21), 4)
ES = (0.0, 2.5, 5.0, 10.0, 20.0, 40.0, 80.0)
RS = (0.40, 0.70)
KAPPAS = (1.0, 3.0)
RULES = ("L-P", "L-E", "L-D", "L-H")


def p_s_given_c():
    m = np.full((K, K), (1.0 - Q) / (K - 1))
    np.fill_diagonal(m, Q)
    return m  # [s, C]


def p_o_given_s(r):
    m = np.full((K, K), (1.0 - r) / (K - 1))
    np.fill_diagonal(m, r)
    return m  # [o, s]


def init_prior():
    p2 = np.full(K, (1.0 - CONV0) / (K - 1))
    p2[MALADAPTIVE] = CONV0
    return p2


def simulate(r, rng):
    """Draw the world once: events from the TRUE context, then observations."""
    psc = p_s_given_c()
    pos = p_o_given_s(r)
    s = rng.choice(K, size=(TRIALS, T), p=psc[:, TRUE])
    u = rng.random((TRIALS, T))
    o = np.where(u < r, s, rng.choice(K, size=(TRIALS, T)))
    # crude off-diagonal redraw: ensure o != s on the noise branch
    noise = u >= r
    while True:
        clash = noise & (o == s)
        if not clash.any():
            break
        o[clash] = rng.choice(K, size=int(clash.sum()))
    return o, pos, psc


def run_block(r, rng):
    o, pos, psc = simulate(r, rng)
    m_oc = pos @ psc                     # m(o|C), [o, C]
    log_m = np.log(m_oc)
    p2 = init_prior()
    log_p2 = np.log(p2)

    cum = np.cumsum(log_m[o, :], axis=1)          # (TRIALS, T, K) over C
    cum_T = cum[:, -1, :]

    # L-E increment: likelihood-only posterior, dose-free by construction
    z = cum_T - cum_T.max(axis=1, keepdims=True)
    inc_LE = np.exp(z)
    inc_LE /= inc_LE.sum(axis=1, keepdims=True)

    out = {}
    for d in DOSES:
        w = 1.0 - d
        # level-2 belief trajectory b_C,t (posterior after t observations)
        logits = w * log_p2[None, None, :] + cum          # (TRIALS, T, K)
        logits -= logits.max(axis=2, keepdims=True)
        b = np.exp(logits)
        b /= b.sum(axis=2, keepdims=True)
        inc_LP = b[:, -1, :]                              # window-end posterior

        # L-H: encoding-driven, per kappa. b at step t uses belief BEFORE o_t:
        # prior belief for step 0 is the (relaxed) stored prior.
        z0 = w * log_p2
        b_prev = np.tile(np.exp(z0 - z0.max()) / np.exp(z0 - z0.max()).sum(),
                         (TRIALS, 1))
        occ = {k: np.zeros((TRIALS, K)) for k in KAPPAS}
        for t in range(T):
            prior1 = b_prev @ psc.T                       # (TRIALS, K) over s
            for kap in KAPPAS:
                lp1 = kap * np.log(np.maximum(prior1, 1e-300)) \
                    + np.log(pos[o[:, t], :])
                lp1 -= lp1.max(axis=1, keepdims=True)
                q1 = np.exp(lp1)
                q1 /= q1.sum(axis=1, keepdims=True)
                occ[kap] += q1
            b_prev = b[:, t, :]
        for kap in KAPPAS:
            occ[kap] /= occ[kap].sum(axis=1, keepdims=True)

        for E in ES:
            frac = E / (N0 + E)
            for rule in RULES:
                if rule == "L-P":
                    inc = inc_LP
                elif rule == "L-E":
                    inc = inc_LE
                elif rule == "L-D":
                    inc = None
                else:
                    inc = None  # handled per kappa below
                keys = []
                if rule == "L-H":
                    for kap in KAPPAS:
                        keys.append((f"{rule}|{kap}", occ[kap]))
                elif rule == "L-D":
                    p2_new = (1 - frac) * p2[None, :] + frac * np.full(K, 1.0 / K)
                    out[f"{rule}|{r}|{d}|{E}"] = {
                        "conviction": float(p2_new[0, MALADAPTIVE]),
                        "insight": float(p2_new[0].argmax() == TRUE),
                    }
                    continue
                else:
                    keys.append((rule, inc))
                for key, incv in keys:
                    p2_new = (N0 * p2[None, :] + E * incv) / (N0 + E)
                    mx = p2_new.argmax(axis=1)
                    out[f"{key}|{r}|{d}|{E}"] = {
                        "conviction": float(p2_new[:, MALADAPTIVE].mean()),
                        "insight": float((mx == TRUE).mean()),
                    }

    return out


def main():
    rng = np.random.default_rng(11)
    t0 = time.time()
    grid = {}
    direction = {}
    for r in RS:
        grid.update(run_block(r, rng))
        print(f"r={r} done at {time.time()-t0:.0f}s")

    # Prediction 33 needs increments per dose; recompute compactly at E-independent
    # level for r = 0.40 (the informative regime), all rules.
    r = 0.40
    rng33 = np.random.default_rng(11)
    o, pos, psc = simulate(r, rng33)
    m_oc = pos @ psc
    log_m = np.log(m_oc)
    p2 = init_prior()
    log_p2 = np.log(p2)
    cum = np.cumsum(log_m[o, :], axis=1)
    z = cum[:, -1, :] - cum[:, -1, :].max(axis=1, keepdims=True)
    inc_LE = np.exp(z)
    inc_LE /= inc_LE.sum(axis=1, keepdims=True)
    mean_incs = {"L-P": {}, "L-E": {}, "L-H|3.0": {}}
    for d in DOSES:
        w = 1.0 - d
        logits = w * log_p2[None, None, :] + cum
        logits -= logits.max(axis=2, keepdims=True)
        b = np.exp(logits)
        b /= b.sum(axis=2, keepdims=True)
        mean_incs["L-P"][f"{d}"] = b[:, -1, :].mean(axis=0).tolist()
        mean_incs["L-E"][f"{d}"] = inc_LE.mean(axis=0).tolist()
        z0 = w * log_p2
        b_prev = np.tile(np.exp(z0 - z0.max()) / np.exp(z0 - z0.max()).sum(),
                         (TRIALS, 1))
        occ = np.zeros((TRIALS, K))
        for t in range(T):
            prior1 = b_prev @ psc.T
            lp1 = 3.0 * np.log(np.maximum(prior1, 1e-300)) + np.log(pos[o[:, t], :])
            lp1 -= lp1.max(axis=1, keepdims=True)
            q1 = np.exp(lp1)
            q1 /= q1.sum(axis=1, keepdims=True)
            occ += q1
            b_prev = b[:, t, :]
        occ /= occ.sum(axis=1, keepdims=True)
        mean_incs["L-H|3.0"][f"{d}"] = occ.mean(axis=0).tolist()
    for rule in mean_incs:
        base_v = np.array(mean_incs[rule]["0.0"])
        direction[rule] = max(float(np.abs(np.array(mean_incs[rule][f"{d}"]) -
                                           base_v).sum()) for d in DOSES)

    OUT.write_text(json.dumps({
        "config": {"doses": DOSES.tolist(), "Es": list(ES), "rs": list(RS),
                   "kappas": list(KAPPAS), "N0": N0, "conv0": CONV0, "q": Q,
                   "T": T, "trials": TRIALS},
        "grid": grid, "mean_incs": mean_incs, "direction_shift": direction}))
    print(f"wrote {OUT.name}\n")

    g = lambda k, r, d, E: grid[f"{k}|{r}|{d}|{E}"]

    print("=== P30/P31: dose spread in lasting insight (E = 20, both r) ===")
    for r in RS:
        for key in ("L-P", "L-E", "L-D", "L-H|1.0", "L-H|3.0"):
            vals = [g(key, r, d, 20.0)["insight"] for d in DOSES]
            print(f"  r={r} {key}: spread {max(vals)-min(vals):.4f} "
                  f"(d=0: {vals[0]:.3f}, d=1: {vals[-1]:.3f})")

    print(f"\n=== P32: L-H lasting conviction vs start ({CONV0}) ===")
    for r in RS:
        for kap in KAPPAS:
            for E in (10.0, 40.0, 80.0):
                vals = [(g(f"L-H|{kap}", r, d, E)["conviction"], d) for d in DOSES]
                peak, pd = max(vals)
                above = [d for v, d in vals if v > CONV0]
                rng_s = f"{min(above):.2f} to {max(above):.2f}" if above else "none"
                print(f"  r={r} kappa={kap} E={E}: peak {peak:.4f} at d={pd}, "
                      f"entrench range {rng_s}")

    print("\n=== P33: direction shift, max L1(inc_d - inc_0), r=0.40 ===")
    for rule, v in direction.items():
        print(f"  {rule}: {v:.4f}")


if __name__ == "__main__":
    main()
