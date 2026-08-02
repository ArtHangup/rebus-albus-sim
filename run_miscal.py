"""Predictions 18-20: does misspecified self-knowledge produce SEBUS?"""
import json, pathlib, time
import numpy as np
from acting import run_batch, baseline_conviction, TRUE, MALADAPTIVE

DOSES = np.round(np.linspace(0, 1, 41), 3)
GAMMAS = (1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0)
R, TRIALS = 0.85, 20_000
rng = np.random.default_rng(777); t0=time.time()

prev = json.loads(pathlib.Path("acting_results.json").read_text())
res = {"R":R,"trials":TRIALS,"doses":DOSES.tolist(),"gammas":list(GAMMAS)}
block={}
for d in DOSES:
    for g in GAMMAS:
        b, deep = run_batch(d, R, rng, TRIALS, gamma_0=g, confusable=True,
                            miscalibrated=True)
        block[f"{d}|{g}"]={"conviction":float(b[:,MALADAPTIVE].mean()),
                           "deep_rate":float(deep.mean()),
                           "insight":float((np.argmax(b,axis=1)==TRUE).mean())}
res["miscalibrated"]=block
print(f"swept in {time.time()-t0:.0f}s\n")

print("=== P18/P19: conviction vs dose. * marks ABOVE pre-dose baseline (SEBUS) ===")
print(f"{'dose':>6}" + "".join(f"{f'g={g}':>11}" for g in GAMMAS))
print(f"{'pre':>6}" + "".join(f"{baseline_conviction(g):>11.4f}" for g in GAMMAS))
for d in DOSES[::4]:
    row=f"{d:>6.2f}"
    for g in GAMMAS:
        v=block[f"{d}|{g}"]["conviction"]; base=baseline_conviction(g)
        row+=f"{v:>10.4f}" + ("*" if v>base else " ")
    print(row)

print("\n=== P20: SEBUS magnitude, miscalibrated vs calibrated control ===")
print(f"{'gamma_0':>8}{'baseline':>10}{'miscal peak':>13}{'@dose':>7}"
      f"{'delta':>9}{'calibrated delta':>18}")
summ={}
for g in GAMMAS:
    base=baseline_conviction(g)
    cs=[block[f"{d}|{g}"]["conviction"] for d in DOSES]
    cal=[prev["confusable"][f"{d}|{g}"]["conviction"] for d in prev["doses"]]
    i=int(np.argmax(cs))
    summ[str(g)]={"baseline":base,"peak":max(cs),"peak_dose":float(DOSES[i]),
                  "delta":max(cs)-base,"delta_calibrated":max(cal)-base}
    print(f"{g:>8.1f}{base:>10.4f}{max(cs):>13.4f}{DOSES[i]:>7.2f}"
          f"{max(cs)-base:>+9.4f}{max(cal)-base:>+18.4f}")
res["summary"]=summ

print("\n=== crossover: highest dose still above baseline (gamma_0=3.0) ===")
base=baseline_conviction(3.0)
above=[d for d in DOSES if block[f"{d}|3.0"]["conviction"]>base]
print(f"baseline {base:.4f}; SEBUS region dose {min(above) if above else None} "
      f"to {max(above) if above else None}")
print(f"{'dose':>6}{'conviction':>12}{'deep rate':>11}{'insight':>9}")
for d in DOSES[::2]:
    c=block[f"{d}|3.0"]
    flag=" *" if c["conviction"]>base else ""
    print(f"{d:>6.2f}{c['conviction']:>12.4f}{c['deep_rate']:>11.3f}{c['insight']:>9.3f}{flag}")

pathlib.Path("miscal_results.json").write_text(json.dumps(res,indent=1))
print("\nwrote miscal_results.json")
