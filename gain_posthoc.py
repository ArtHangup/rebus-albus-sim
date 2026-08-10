"""Post-declaration resolution addition to the amendment 7 grid.

AMENDMENT_7 declared costs {0.0, 0.3, 0.5}. Prediction 29a (gain lowers the
effective cost threshold) turned out to need cells below 0.3 to be tested
properly, so this script adds costs {0.1, 0.2} at A in {0, 4}. It is a
measurement-resolution addition to a declared analysis, run after seeing the
main grid, and is labeled as such wherever its numbers are used. Everything
else is identical to gain.py.
"""

import json
import pathlib

import numpy as np

from acting import MALADAPTIVE, TRUE, baseline_conviction, run_batch

OUT = pathlib.Path(__file__).parent / "gain_posthoc.json"
DOSES = np.round(np.linspace(0, 1, 41), 4)
G0, R, TRIALS, C_CONS = 3.0, 0.85, 20_000, 0.8


def main():
    rng = np.random.default_rng(211)
    base = baseline_conviction(G0)
    u = np.zeros(6)
    u[MALADAPTIVE] = 1.0
    logits = G0 * u
    p_orig = np.exp(logits - logits.max())
    p_orig = p_orig / p_orig.sum()

    out = {"baseline": base, "grid": {}}
    for A in (0.0, 4.0):
        for cost in (0.1, 0.2):
            for d in DOSES:
                d_eff = 1.0 - (1.0 - d) * (1.0 + A * d)
                b, deep = run_batch(d_eff, R, rng, TRIALS, gamma_0=G0,
                                    confusable=True, deep_cost=cost)
                p_after = (1.0 - C_CONS) * p_orig[None, :] + C_CONS * b
                out["grid"][f"{A}|{cost}|{d}"] = {
                    "conviction": float(b[:, MALADAPTIVE].mean()),
                    "deep_rate": float(deep.mean()),
                    "lasting_conviction": float(p_after[:, MALADAPTIVE].mean()),
                    "lasting_insight": float((p_after.argmax(axis=1) == TRUE).mean()),
                }
    OUT.write_text(json.dumps(out))
    print(f"wrote {OUT.name}")
    for A in (0.0, 4.0):
        for cost in (0.1, 0.2):
            above = [d for d in DOSES
                     if out["grid"][f"{A}|{cost}|{d}"]["conviction"] > base]
            print(f"A={A} cost={cost}: SEBUS "
                  f"{f'{min(above):.2f} to {max(above):.2f}' if above else 'none'}")


if __name__ == "__main__":
    main()
