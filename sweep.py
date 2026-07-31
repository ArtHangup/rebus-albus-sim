"""Sweep dose against evidence reliability. Outcomes defined in PREREGISTRATION.md."""

import json
import pathlib
import sys

import numpy as np

from model import (LAMBDA_0, MALADAPTIVE, WINDOW, baseline_conviction, classify,
                   run_trial)

DOSES = np.round(np.linspace(0.0, 1.0, 21), 3)
RELIABILITIES = np.round(np.linspace(0.20, 0.95, 16), 3)
TRIALS = 400
OUT = pathlib.Path(__file__).parent / "sweep_results.json"


def sweep(sensory_disruption, seed=0):
    rng = np.random.default_rng(seed)
    grid = {}
    for d in DOSES:
        for r in RELIABILITIES:
            counts = {"insight": 0, "no_change": 0, "false_insight": 0}
            conviction, persisted = [], 0
            for _ in range(TRIALS):
                bw, bt = run_trial(d, r, rng,
                                   sensory_disruption=sensory_disruption)
                counts[classify(bt)] += 1
                conviction.append(bw[MALADAPTIVE])
                persisted += int(np.argmax(bw) == np.argmax(bt))
            grid[f"{d}|{r}"] = {
                "dose": float(d),
                "reliability": float(r),
                "insight": counts["insight"] / TRIALS,
                "no_change": counts["no_change"] / TRIALS,
                "false_insight": counts["false_insight"] / TRIALS,
                "conviction_at_window_end": float(np.mean(conviction)),
                "persistence": persisted / TRIALS,
            }
    return grid


def main():
    base = baseline_conviction()
    print(f"baseline conviction in the maladaptive belief: {base:.4f}")
    print(f"grid: {len(DOSES)} doses x {len(RELIABILITIES)} reliabilities "
          f"x {TRIALS} trials x 2 arms")

    results = {
        "config": {
            "doses": DOSES.tolist(),
            "reliabilities": RELIABILITIES.tolist(),
            "trials": TRIALS,
            "window": WINDOW,
            "lambda_0": LAMBDA_0,
            "baseline_conviction": base,
        },
        "arm1_pure_rebus": sweep(sensory_disruption=False, seed=1),
        "arm2_sensory_disruption": sweep(sensory_disruption=True, seed=2),
    }
    OUT.write_text(json.dumps(results, indent=1))
    print(f"wrote {OUT.name}")

    # Prediction 1: is insight a ridge in dose, or a monotone slope?
    for arm in ("arm1_pure_rebus", "arm2_sensory_disruption"):
        print(f"\n=== {arm}: insight rate by dose, at three reliabilities ===")
        print(f"{'dose':>6}" + "".join(f"{f'r={r}':>10}" for r in (0.25, 0.55, 0.95)))
        for d in DOSES[::4]:
            row = f"{d:>6.2f}"
            for r in (0.25, 0.55, 0.95):
                rr = min(RELIABILITIES, key=lambda x: abs(x - r))
                row += f"{results[arm][f'{d}|{rr}']['insight']:>10.3f}"
            print(row)


if __name__ == "__main__":
    sys.exit(main())
