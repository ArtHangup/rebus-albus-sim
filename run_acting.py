"""Predictions 13-17. Confusable arm vs the separable control."""
import json, pathlib, time
import numpy as np
from acting import run_batch, baseline_conviction, TRUE, MALADAPTIVE

DOSES = np.round(np.linspace(0, 1, 41), 3)
GAMMAS = (1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0)
R = 0.85
TRIALS = 20_000

def cell(dose, g0, conf, rng):
    b, deep = run_batch(dose, R, rng, TRIALS, gamma_0=g0, confusable=conf)
    return {"conviction": float(b[:, MALADAPTIVE].mean()),
            "deep_rate": float(deep.mean()),
            "insight": float((np.argmax(b, axis=1) == TRUE).mean())}

rng = np.random.default_rng(4242)
t0 = time.time()
res = {"R": R, "trials": TRIALS, "doses": DOSES.tolist(), "gammas": list(GAMMAS)}

for conf, name in ((True, "confusable"), (False, "control_separable")):
    print(f"\n=== {name}: conviction in the maladaptive belief at window end ===")
    print(f"{'dose':>6}" + "".join(f"{f'g={g}':>10}" for g in GAMMAS))
    print(f"{'pre':>6}" + "".join(f"{baseline_conviction(g):>10.4f}" for g in GAMMAS))
    block = {}
    for d in DOSES:
        row = f"{d:>6.2f}"
        for g in GAMMAS:
            c = cell(d, g, conf, rng)
            block[f"{d}|{g}"] = c
            row += f"{c['conviction']:>10.4f}"
        if abs(d * 10 - round(d * 10)) < 1e-9 and round(d * 10) % 1 == 0 and d in DOSES[::4]:
            print(row)
    res[name] = block
    print(f"  ({time.time()-t0:.0f}s)")

print("\n=== P13/P14: SEBUS. peak conviction minus pre-dose baseline ===")
print(f"{'gamma_0':>8}{'baseline':>10}{'confusable':>12}{'peak@dose':>11}{'control':>10}")
summ = {}
for g in GAMMAS:
    base = baseline_conviction(g)
    cs = [res["confusable"][f"{d}|{g}"]["conviction"] for d in DOSES]
    ks = [res["control_separable"][f"{d}|{g}"]["conviction"] for d in DOSES]
    i = int(np.argmax(cs))
    summ[str(g)] = {"baseline": base, "peak": max(cs), "peak_dose": float(DOSES[i]),
                    "delta": max(cs) - base, "delta_control": max(ks) - base}
    print(f"{g:>8.1f}{base:>10.4f}{max(cs)-base:>+12.4f}{DOSES[i]:>11.2f}{max(ks)-base:>+10.4f}")
res["summary"] = summ

print("\n=== P16: deep-probe usage vs dose (confusable, gamma_0=3.0) ===")
print(f"{'dose':>6}{'deep rate':>11}{'conviction':>12}{'insight':>9}   (baseline "
      f"{baseline_conviction(3.0):.4f})")
for d in DOSES[::4]:
    c = res["confusable"][f"{d}|3.0"]
    print(f"{d:>6.2f}{c['deep_rate']:>11.3f}{c['conviction']:>12.4f}{c['insight']:>9.3f}")

pathlib.Path("acting_results.json").write_text(json.dumps(res, indent=1))
print("\nwrote acting_results.json")
