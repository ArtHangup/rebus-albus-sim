"""Predictions 34-37: compounding sessions, chronicity, and treatment shape.

Declared in AMENDMENT_9.md (commit 3615dd2) before this file existed. The
two-level model and L-H encoding rule of hierarchy.py, run through repeated
sessions; each trial carries its own evolving stored prior.
"""

import json
import pathlib
import time

import numpy as np

OUT = pathlib.Path(__file__).parent / "sessions_results.json"

K = 6
TRUE = 0
MALADAPTIVE = 1
Q = 0.8
T = 12
N0 = 20.0
CONV0 = 0.8007
TRIALS = 10_000
E_PRIMARY = 10.0
HORIZON = 40


def p_s_given_c():
    m = np.full((K, K), (1.0 - Q) / (K - 1))
    np.fill_diagonal(m, Q)
    return m


def p_o_given_s(r):
    m = np.full((K, K), (1.0 - r) / (K - 1))
    np.fill_diagonal(m, r)
    return m


def init_prior():
    p2 = np.full(K, (1.0 - CONV0) / (K - 1))
    p2[MALADAPTIVE] = CONV0
    return np.tile(p2, (TRIALS, 1))


def draw_obs(r, rng):
    psc = p_s_given_c()
    s = rng.choice(K, size=(TRIALS, T), p=psc[:, TRUE])
    u = rng.random((TRIALS, T))
    o = np.where(u < r, s, rng.choice(K, size=(TRIALS, T)))
    noise = u >= r
    while True:
        clash = noise & (o == s)
        if not clash.any():
            break
        o[clash] = rng.choice(K, size=int(clash.sum()))
    return o


def one_session(p2, N, d, r, kappa, rule, E, rng):
    """Run one session and return (p2_new, N_new). p2 is (TRIALS, K)."""
    psc = p_s_given_c()
    pos = p_o_given_s(r)
    m_oc = pos @ psc
    log_m = np.log(m_oc)
    o = draw_obs(r, rng)
    w = 1.0 - d
    log_p2 = np.log(np.maximum(p2, 1e-300))

    cum = np.cumsum(log_m[o, :], axis=1)              # (TRIALS, T, K)
    logits = w * log_p2[:, None, :] + cum
    logits -= logits.max(axis=2, keepdims=True)
    b = np.exp(logits)
    b /= b.sum(axis=2, keepdims=True)

    if rule == "L-E":
        z = cum[:, -1, :] - cum[:, -1, :].max(axis=1, keepdims=True)
        inc = np.exp(z)
        inc /= inc.sum(axis=1, keepdims=True)
    else:  # L-H
        z0 = w * log_p2
        z0 -= z0.max(axis=1, keepdims=True)
        b_prev = np.exp(z0)
        b_prev /= b_prev.sum(axis=1, keepdims=True)
        occ = np.zeros((TRIALS, K))
        for t in range(T):
            prior1 = b_prev @ psc.T
            lp1 = kappa * np.log(np.maximum(prior1, 1e-300)) + np.log(pos[o[:, t], :])
            lp1 -= lp1.max(axis=1, keepdims=True)
            q1 = np.exp(lp1)
            q1 /= q1.sum(axis=1, keepdims=True)
            occ += q1
            b_prev = b[:, t, :]
        inc = occ / occ.sum(axis=1, keepdims=True)

    p2_new = (N * p2 + E * inc) / (N + E)
    return p2_new


def run_protocol(doses, r, kappa, rule, mass, rng, E=E_PRIMARY):
    """doses: sequence of session doses. Returns per-session (conviction, insight)."""
    p2 = init_prior()
    N = N0
    traj = []
    for d in doses:
        p2 = one_session(p2, N, d, r, kappa, rule, E, rng)
        if mass == "accum":
            N += E
        traj.append((float(p2[:, MALADAPTIVE].mean()),
                     float((p2.argmax(axis=1) == TRUE).mean())))
    return traj, p2, N


def s50(traj):
    for i, (_, ins) in enumerate(traj):
        if ins >= 0.5:
            return i + 1
    return None


def main():
    rng = np.random.default_rng(11)
    t0 = time.time()
    results = {"config": {"trials": TRIALS, "E": E_PRIMARY, "N0": N0,
                          "conv0": CONV0, "horizon": HORIZON},
               "natural": {}, "treatment": {}, "shape": {}}

    # Protocol 1: natural history
    for r in (0.40, 0.70):
        for mass in ("fixed", "accum"):
            for key, rule, kappa in (("L-H|3", "L-H", 3.0), ("L-H|1", "L-H", 1.0),
                                     ("L-E", "L-E", 0.0)):
                traj, _, _ = run_protocol([0.0] * HORIZON, r, kappa, rule, mass, rng)
                results["natural"][f"{key}|{r}|{mass}"] = traj
        for E in (5.0, 20.0):
            traj, _, _ = run_protocol([0.0] * HORIZON, r, 3.0, "L-H", "fixed",
                                      rng, E=E)
            results["natural"][f"L-H|3|{r}|fixed|E{E}"] = traj
    print(f"natural history done at {time.time()-t0:.0f}s")

    # Protocol 2: chronicity then treatment (r = 0.40)
    for mass in ("fixed", "accum"):
        for kappa in (3.0, 1.0):
            for j in (0, 5, 10, 20, 40):
                for d in (0.2, 0.4, 0.6, 0.8, 1.0):
                    doses = [0.0] * j + [d] * HORIZON
                    traj, _, _ = run_protocol(doses, 0.40, kappa, "L-H", mass, rng)
                    course = s50(traj[j:])
                    results["treatment"][f"{kappa}|{mass}|{j}|{d}"] = {
                        "course": course,
                        "insight_end": traj[-1][1],
                        "conviction_at_treatment_start": traj[j - 1][0] if j else CONV0,
                    }
        print(f"treatment ({mass}) done at {time.time()-t0:.0f}s")

    # Protocol 3: shape at matched exposure, j = 10, kappa = 3, r = 0.40
    protos = {"a_single_1.0": [1.0] + [0.0] * 19,
              "b_two_0.5": [0.5] * 2 + [0.0] * 18,
              "c_five_0.2": [0.2] * 5 + [0.0] * 15}
    for mass in ("fixed", "accum"):
        for name, course in protos.items():
            doses = [0.0] * 10 + course
            traj, _, _ = run_protocol(doses, 0.40, 3.0, "L-H", mass, rng)
            results["shape"][f"{name}|{mass}"] = {
                "traj": traj, "insight_end": traj[-1][1],
                "conviction_end": traj[-1][0]}
    print(f"shape done at {time.time()-t0:.0f}s")

    OUT.write_text(json.dumps(results))
    print(f"wrote {OUT.name}\n")

    # ---- summaries ----
    print("=== P34 natural history, r=0.40, fixed mass: insight by session ===")
    for key in ("L-E", "L-H|1", "L-H|3"):
        traj = results["natural"][f"{key}|0.4|fixed"]
        marks = {s: traj[s - 1][1] for s in (1, 5, 10, 20, 40)}
        print(f"  {key}: " + "  ".join(f"s{s}: {v:.3f}" for s, v in marks.items())
              + f"   S50: {s50(traj)}")
    print("  conviction, L-H|3 fixed: " + "  ".join(
        f"s{s}: {results['natural']['L-H|3|0.4|fixed'][s-1][0]:.3f}"
        for s in (1, 5, 10, 20, 40)))
    print("  conviction, L-H|3 accum: " + "  ".join(
        f"s{s}: {results['natural']['L-H|3|0.4|accum'][s-1][0]:.3f}"
        for s in (1, 5, 10, 20, 40)))

    print("\n=== P35/P36 course length (sessions to S50, treatment only) ===")
    for mass in ("fixed", "accum"):
        print(f"  kappa=3, {mass} mass:")
        print(f"{'j':>6}" + "".join(f"{f'd={d}':>8}" for d in (0.2, 0.4, 0.6, 0.8, 1.0)))
        for j in (0, 5, 10, 20, 40):
            row = f"{j:>6}"
            for d in (0.2, 0.4, 0.6, 0.8, 1.0):
                c = results["treatment"][f"3.0|{mass}|{j}|{d}"]["course"]
                row += f"{str(c) if c else 'never':>8}"
            print(row)

    print("\n=== P37 protocol shape, insight at 20-session horizon ===")
    for mass in ("fixed", "accum"):
        row = f"  {mass} mass: "
        for name in ("a_single_1.0", "b_two_0.5", "c_five_0.2"):
            row += f"{name}: {results['shape'][f'{name}|{mass}']['insight_end']:.3f}  "
        print(row)


if __name__ == "__main__":
    main()
