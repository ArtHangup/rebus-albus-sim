"""Predictions 21-23: does pricing out the diagnostic test produce SEBUS?"""
import json, pathlib, time
import numpy as np
from acting import run_batch, baseline_conviction, TRUE, MALADAPTIVE

DOSES=np.round(np.linspace(0,1,41),3)
COSTS=(0.0,0.05,0.1,0.2,0.3,0.5,0.8,1.2)
G0, R, TRIALS = 3.0, 0.85, 20_000
rng=np.random.default_rng(31337); t0=time.time()
base=baseline_conviction(G0)

block={}
for c in COSTS:
    for d in DOSES:
        b,deep=run_batch(d,R,rng,TRIALS,gamma_0=G0,confusable=True,deep_cost=c)
        block[f"{c}|{d}"]={"conviction":float(b[:,MALADAPTIVE].mean()),
                           "deep_rate":float(deep.mean()),
                           "insight":float((np.argmax(b,axis=1)==TRUE).mean())}
print(f"swept in {time.time()-t0:.0f}s   pre-dose baseline = {base:.4f}\n")

print("=== P21/P22: conviction vs dose, by cost of the diagnostic test ===")
print("* = above pre-dose baseline (SEBUS)")
print(f"{'dose':>6}" + "".join(f"{f'c={c}':>11}" for c in COSTS))
for d in DOSES[::4]:
    row=f"{d:>6.2f}"
    for c in COSTS:
        v=block[f"{c}|{d}"]["conviction"]
        row+=f"{v:>10.4f}"+("*" if v>base else " ")
    print(row)

print("\n=== SEBUS magnitude and crossover by cost ===")
print(f"{'cost':>6}{'peak conv':>11}{'@dose':>7}{'delta':>9}{'SEBUS dose range':>20}")
summ={}
for c in COSTS:
    vs=[block[f'{c}|{d}']["conviction"] for d in DOSES]
    i=int(np.argmax(vs)); above=[d for d,v in zip(DOSES,vs) if v>base]
    rng_s=f"{min(above):.2f} to {max(above):.2f}" if above else "none"
    summ[str(c)]={"peak":max(vs),"peak_dose":float(DOSES[i]),"delta":max(vs)-base,
                  "sebus_lo":min(above) if above else None,
                  "sebus_hi":max(above) if above else None}
    print(f"{c:>6.2f}{max(vs):>11.4f}{DOSES[i]:>7.2f}{max(vs)-base:>+9.4f}{rng_s:>20}")

print("\n=== P23: deep-probe usage vs dose (the mediator) ===")
print(f"{'dose':>6}" + "".join(f"{f'c={c}':>9}" for c in COSTS))
for d in DOSES[::5]:
    print(f"{d:>6.2f}" + "".join(f"{block[f'{c}|{d}']['deep_rate']:>9.3f}" for c in COSTS))

pathlib.Path("cost_results.json").write_text(json.dumps(
    {"baseline":base,"gamma_0":G0,"doses":DOSES.tolist(),"costs":list(COSTS),
     "grid":block,"summary":summ},indent=1))
print("\nwrote cost_results.json")
