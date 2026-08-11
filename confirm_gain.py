"""Predictions 42-44: confirmatory re-run of the gain arm's post hoc cells.

Declared in AMENDMENT_11.md (commit 27da277, pushed before this run). Fresh seed
fixed in the amendment. Machinery identical to gain_posthoc.py.
"""

import json
import pathlib

import numpy as np

from acting import MALADAPTIVE, TRUE, baseline_conviction, run_batch

OUT = pathlib.Path(__file__).parent / "confirm_gain_results.json"
DOSES = np.round(np.linspace(0, 1, 41), 4)
G0, R, TRIALS, C_CONS = 3.0, 0.85, 20_000, 0.8


def main():
    rng = np.random.default_rng(20260810)
    base = baseline_conviction(G0)
    out = {"baseline": base, "grid": {}}
    for A in (0.0, 4.0):
        for cost in (0.1, 0.2):
            for d in DOSES:
                d_eff = 1.0 - (1.0 - d) * (1.0 + A * d)
                b, _ = run_batch(d_eff, R, rng, TRIALS, gamma_0=G0,
                                 confusable=True, deep_cost=cost)
                out["grid"][f"{A}|{cost}|{d}"] = float(b[:, MALADAPTIVE].mean())
    OUT.write_text(json.dumps(out))
    print(f"wrote {OUT.name}   baseline {base:.4f}")
    for A in (0.0, 4.0):
        for cost in (0.1, 0.2):
            above = [d for d in DOSES if out["grid"][f"{A}|{cost}|{d}"] > base]
            rng_s = f"{min(above):.2f} to {max(above):.2f}" if above else "none"
            c0 = out["grid"][f"{A}|{cost}|0.0"]
            print(f"A={A} cost={cost}: SEBUS {rng_s}   conviction(d=0) {c0:.4f}")


if __name__ == "__main__":
    main()
