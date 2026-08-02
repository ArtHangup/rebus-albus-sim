"""Four consolidation parameterizations, declared in AMENDMENT_2.md before this file.

Vectorized: observation counts for a reliability are drawn once and reused across every
dose, c, and parameterization, so the dose contrast is paired.
"""

import json
import pathlib
import time

import numpy as np

HERE = pathlib.Path(__file__).parent
OUT = HERE / "robustness_results.json"

K_DEFAULT = 6
TRUE = 0
MALADAPTIVE = 1
GAMMA_0 = 8.0
LAMBDA_0 = 1.0
WINDOW = 12
EPS = 1e-300

DOSES = np.round(np.linspace(0.0, 1.0, 41), 4)
CS = np.round(np.linspace(0.0, 1.0, 41), 4)
RELIABILITIES = np.round(np.linspace(0.20, 0.95, 8), 4)
TRIALS = 50_000

PARAMS = ("P-A_arithmetic", "P-B_geometric", "P-C_attractor", "P-D_memory")


def softmax_rows(x):
    x = x - x.max(axis=1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=1, keepdims=True)


def draw_cum_ll(r, rng, trials, k=K_DEFAULT, window=WINDOW):
    """Accumulated log-likelihood per trial, vectorized.

    Only the COUNT of each observation type matters for the sum of log-likelihoods,
    so one multinomial draw per trial replaces the inner loop entirely.
    """
    a = np.full((k, k), (1.0 - r) / (k - 1))
    np.fill_diagonal(a, r)
    counts = rng.multinomial(window, a[:, TRUE], size=trials).astype(np.float64)
    return counts @ np.log(a), a


def window_belief(cum_ll, dose, k=K_DEFAULT, gamma_0=GAMMA_0, lambda_0=LAMBDA_0,
                  sensory_disruption=False):
    u = np.zeros(k)
    u[MALADAPTIVE] = 1.0
    gamma_d = gamma_0 * (1.0 - dose)
    lambda_d = lambda_0 * (1.0 - 0.7 * dose) if sensory_disruption else lambda_0
    return softmax_rows(gamma_d * u + lambda_d * cum_ll), lambda_d, u


def consolidate(kind, b, cum_ll, c, u, lambda_d, gamma_0=GAMMA_0):
    """The four mechanisms from AMENDMENT_2.md."""
    p_orig = softmax_rows((gamma_0 * u)[None, :])
    if kind == "P-A_arithmetic":
        return (1.0 - c) * p_orig + c * b
    if kind == "P-B_geometric":
        return softmax_rows((1.0 - c) * np.log(p_orig + EPS) + c * np.log(b + EPS))
    if kind == "P-C_attractor":
        return softmax_rows(gamma_0 * (1.0 - c) * u + lambda_d * cum_ll)
    if kind == "P-D_memory":
        return softmax_rows(gamma_0 * u + c * lambda_d * cum_ll)
    raise ValueError(kind)


def rates(p):
    m = np.argmax(p, axis=1)
    n = float(len(m))
    return (float((m == TRUE).sum() / n),
            float((m == MALADAPTIVE).sum() / n),
            float(((m != TRUE) & (m != MALADAPTIVE)).sum() / n))


def main_sweep(rng):
    out = {}
    t0 = time.time()
    for r in RELIABILITIES:
        cum_ll, _ = draw_cum_ll(r, rng, TRIALS)
        for d in DOSES:
            b, lambda_d, u = window_belief(cum_ll, d)
            for kind in PARAMS:
                for c in CS:
                    ins, noc, fal = rates(
                        consolidate(kind, b, cum_ll, c, u, lambda_d))
                    out[f"{kind}|{r}|{d}|{c}"] = [ins, noc, fal]
        print(f"  r={r:.3f} done  ({time.time()-t0:.0f}s)")
    return out


def entrenchment_sweep(rng):
    """Prediction 12: does gamma_0 move the threshold differently by mechanism?"""
    out = {}
    for g0 in (4.0, 6.0, 8.0, 10.0, 12.0, 16.0, 24.0):
        cum_ll, _ = draw_cum_ll(0.55, rng, TRIALS)
        b, lambda_d, u = window_belief(cum_ll, 0.8, gamma_0=g0)
        for kind in PARAMS:
            star = None
            for c in CS:
                ins, _, _ = rates(consolidate(kind, b, cum_ll, c, u, lambda_d,
                                              gamma_0=g0))
                if ins >= 0.5 and star is None:
                    star = float(c)
            out[f"{kind}|{g0}"] = star
    return out


def structural_sweep(rng):
    """Does the shared-threshold claim survive changing K and the window length?"""
    out = {}
    for k in (3, 6, 10, 20):
        for w in (4, 12, 30):
            cum_ll, _ = draw_cum_ll(0.55, rng, 20_000, k=k, window=w)
            b, lambda_d, u = window_belief(cum_ll, 0.8, k=k)
            cum_ll_lo, _ = draw_cum_ll(0.30, rng, 20_000, k=k, window=w)
            b_lo, ld_lo, _ = window_belief(cum_ll_lo, 0.8, k=k)
            for kind in PARAMS:
                t_true = t_false = None
                for c in CS:
                    ins, _, _ = rates(consolidate(kind, b, cum_ll, c, u, lambda_d))
                    _, _, fal = rates(
                        consolidate(kind, b_lo, cum_ll_lo, c, u, ld_lo))
                    if ins >= 0.5 and t_true is None:
                        t_true = float(c)
                    if fal >= 0.05 and t_false is None:
                        t_false = float(c)
                out[f"{kind}|K={k}|W={w}"] = {"c_true50": t_true,
                                              "c_false5": t_false}
    return out


def main():
    rng = np.random.default_rng(2026)
    print(f"main sweep: {len(RELIABILITIES)}r x {len(DOSES)}d x {len(CS)}c "
          f"x {len(PARAMS)}p x {TRIALS:,} trials")
    print(f"  = {len(RELIABILITIES)*len(DOSES)*len(CS)*len(PARAMS)*TRIALS:,} agents")
    res = {
        "config": {"doses": DOSES.tolist(), "cs": CS.tolist(),
                   "reliabilities": RELIABILITIES.tolist(), "trials": TRIALS,
                   "params": list(PARAMS), "window": WINDOW, "gamma_0": GAMMA_0},
        "main": main_sweep(rng),
    }
    print("entrenchment sweep...")
    res["entrenchment"] = entrenchment_sweep(rng)
    print("structural sweep (K and window)...")
    res["structural"] = structural_sweep(rng)
    OUT.write_text(json.dumps(res))
    print(f"wrote {OUT.name} ({OUT.stat().st_size/1e6:.1f} MB)")


if __name__ == "__main__":
    main()
