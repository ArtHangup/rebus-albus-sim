"""Arm 3: does consolidation rescue persistence, and what does it lock in?

Declared in AMENDMENT_1.md before this file existed. Predictions 6, 7, 8 there.
"""

import json
import pathlib

import numpy as np

from model import (GAMMA_0, MALADAPTIVE, TRUE, classify, likelihood,
                   prior_logits, run_trial, softmax)

OUT = pathlib.Path(__file__).parent / "consolidation_results.json"


def original_prior(gamma_0=GAMMA_0):
    return softmax(gamma_0 * prior_logits())


def consolidate(belief_window, c, gamma_0=GAMMA_0):
    """p_after = (1-c)*p_original + c*b_window. No re-application of evidence."""
    return (1.0 - c) * original_prior(gamma_0) + c * belief_window


def cell(dose, r, c, rng, trials, gamma_0=GAMMA_0):
    counts = {"insight": 0, "no_change": 0, "false_insight": 0}
    win = {"insight": 0, "no_change": 0, "false_insight": 0}
    conv = []
    for _ in range(trials):
        bw, _ = run_trial(dose, r, rng, gamma_0=gamma_0)
        win[classify(bw)] += 1
        conv.append(bw[MALADAPTIVE])
        counts[classify(consolidate(bw, c, gamma_0))] += 1
    n = float(trials)
    return {k: v / n for k, v in counts.items()} | {
        "window_insight": win["insight"] / n,
        "window_false": win["false_insight"] / n,
        "conviction_at_window_end": float(np.mean(conv)),
    }


def main():
    rng = np.random.default_rng(11)
    TRIALS = 400
    DOSES = np.round(np.linspace(0, 1, 11), 3)
    CS = np.round(np.linspace(0, 1, 21), 3)
    results = {}

    # --- Prediction 6: is there a consolidation threshold, and is it dose-independent?
    print("=== P6: persistent insight rate, dose x consolidation, r=0.55 ===")
    print(f"{'c':>6}" + "".join(f"{f'd={d:.1f}':>9}" for d in DOSES[::2]))
    grid = {}
    for c in CS:
        row = f"{c:>6.2f}"
        for d in DOSES:
            g = cell(d, 0.55, c, rng, TRIALS)
            grid[f"{d}|{c}"] = g
            if d in DOSES[::2]:
                row += f"{g['insight']:>9.3f}"
        print(row)
    results["dose_x_consolidation_r055"] = grid

    # --- Prediction 7: does the threshold move with entrenchment?
    print("\n=== P7: consolidation threshold vs entrenchment (dose=0.8, r=0.55) ===")
    print(f"{'gamma_0':>8}{'p_orig(mal)':>13}{'c* (50% insight)':>18}")
    ent = {}
    for g0 in (4.0, 6.0, 8.0, 10.0, 12.0):
        thresh = None
        for c in CS:
            v = cell(0.8, 0.55, c, rng, 300, gamma_0=g0)["insight"]
            if v >= 0.5 and thresh is None:
                thresh = float(c)
        po = float(original_prior(g0)[MALADAPTIVE])
        ent[str(g0)] = {"p_original": po, "c_star": thresh}
        print(f"{g0:>8.1f}{po:>13.4f}{str(thresh):>18}")
    results["entrenchment"] = ent

    # --- Prediction 8: is consolidation indiscriminate?
    print("\n=== P8: persistent FALSE insight, low reliability r=0.30 ===")
    print(f"{'c':>6}{'d=0.4':>9}{'d=0.8':>9}{'d=1.0':>9}")
    ind = {}
    for c in CS[::2]:
        row = f"{c:>6.2f}"
        for d in (0.4, 0.8, 1.0):
            g = cell(d, 0.30, c, rng, TRIALS)
            ind[f"{d}|{c}"] = g
            row += f"{g['false_insight']:>9.3f}"
        print(row)
    results["false_insight_r030"] = ind

    # --- Prediction 3: does SEBUS emerge? conviction at window end vs dose.
    print("\n=== P3: SEBUS check. conviction in the maladaptive belief at window end ===")
    print(f"{'dose':>6}{'r=0.30':>10}{'r=0.55':>10}{'r=0.85':>10}")
    seb = {}
    base = float(original_prior()[MALADAPTIVE])
    print(f"{'pre':>6}{base:>10.4f}{base:>10.4f}{base:>10.4f}")
    for d in DOSES:
        row = f"{d:>6.2f}"
        for r in (0.30, 0.55, 0.85):
            v = cell(d, r, 0.0, rng, 600)["conviction_at_window_end"]
            seb[f"{d}|{r}"] = v
            row += f"{v:>10.4f}"
        print(row)
    results["sebus"] = {"baseline": base, "grid": seb}

    OUT.write_text(json.dumps(results, indent=1))
    print(f"\nwrote {OUT.name}")


if __name__ == "__main__":
    main()
