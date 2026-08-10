"""Dense recompute of the figure_main panels. No new hypotheses, no new arms.

This recomputes three quantities already declared and reported (predictions 6, 8, 3;
see AMENDMENT_1.md and PREREGISTRATION.md) on a finer grid with more trials, so the
poster figure can use a genuinely continuous dose axis instead of three categorical
columns. The mechanism, mapping, and outcome definitions are byte-identical to
consolidation.py; only resolution changes. Spot checks against the published coarse
numbers are printed at the end and must agree within Monte Carlo error.

Observation draws are shared across dose and consolidation within each block, so
contrasts are paired, matching the design of robustness.py.
"""

import json
import pathlib

import numpy as np

from model import GAMMA_0, K, MALADAPTIVE, TRUE, likelihood, prior_logits, softmax

OUT = pathlib.Path(__file__).parent / "dense_grids.json"

WINDOW = 12
TRIALS = 20000
DOSES = np.round(np.linspace(0, 1, 41), 4)
CS = np.round(np.linspace(0, 1, 41), 4)


def draw_counts(r, trials, rng):
    """Multinomial observation counts per trial. cum_ll = counts @ log A."""
    a = likelihood(r)
    counts = rng.multinomial(WINDOW, a[:, TRUE], size=trials)
    return counts @ np.log(a)


def outcome_grid(cum_ll, which):
    """Rate of `which` outcome after consolidation, over the dose x c grid."""
    u = prior_logits()
    p_orig = softmax(GAMMA_0 * u)
    out = np.zeros((len(CS), len(DOSES)))
    for j, d in enumerate(DOSES):
        gamma_d = GAMMA_0 * (1.0 - d)
        logits = gamma_d * u[None, :] + cum_ll
        logits -= logits.max(axis=1, keepdims=True)
        bw = np.exp(logits)
        bw /= bw.sum(axis=1, keepdims=True)
        for i, c in enumerate(CS):
            p_after = (1.0 - c) * p_orig[None, :] + c * bw
            m = p_after.argmax(axis=1)
            if which == "insight":
                out[i, j] = (m == TRUE).mean()
            else:
                out[i, j] = (m >= 2).mean()
    return out


def sebus_curves(rng):
    """Mean conviction in the maladaptive belief at window end, per dose."""
    u = prior_logits()
    curves = {}
    for r in (0.30, 0.55, 0.85):
        cum_ll = draw_counts(r, TRIALS, rng)
        ys = []
        for d in DOSES:
            gamma_d = GAMMA_0 * (1.0 - d)
            logits = gamma_d * u[None, :] + cum_ll
            logits -= logits.max(axis=1, keepdims=True)
            bw = np.exp(logits)
            bw /= bw.sum(axis=1, keepdims=True)
            ys.append(float(bw[:, MALADAPTIVE].mean()))
        curves[f"{r}"] = ys
    return curves


def main():
    rng = np.random.default_rng(11)

    insight = outcome_grid(draw_counts(0.55, TRIALS, rng), "insight")
    false_g = outcome_grid(draw_counts(0.30, TRIALS, rng), "false_insight")
    seb = sebus_curves(rng)
    base = float(softmax(GAMMA_0 * prior_logits())[MALADAPTIVE])

    OUT.write_text(json.dumps({
        "doses": DOSES.tolist(), "cs": CS.tolist(), "trials": TRIALS,
        "insight_r055": insight.tolist(),
        "false_insight_r030": false_g.tolist(),
        "sebus": {"baseline": base, "curves": seb},
    }))
    print(f"wrote {OUT.name}")

    # Spot checks against published coarse numbers (400 to 600 trials there).
    ci = {c: i for i, c in enumerate(CS)}
    di = {d: j for j, d in enumerate(DOSES)}
    print("\nspot checks (dense vs published):")
    for c, d, pub in ((0.55, 0.0, 0.505), (0.55, 1.0, 0.895), (0.8, 0.8, 0.935)):
        print(f"  insight  c={c} d={d}: {insight[ci[c], di[d]]:.3f} vs {pub}")
    for c, d, pub in ((0.9, 1.0, 0.247), (0.7, 0.8, 0.058), (0.5, 1.0, 0.0)):
        print(f"  false    c={c} d={d}: {false_g[ci[c], di[d]]:.3f} vs {pub}")
    for d, r, pub in ((0.0, 0.55, 0.2968), (1.0, 0.30, 0.1229), (0.5, 0.55, 0.0720)):
        print(f"  sebus    d={d} r={r}: {seb[f'{r}'][di[d]]:.4f} vs {pub}")


if __name__ == "__main__":
    main()
