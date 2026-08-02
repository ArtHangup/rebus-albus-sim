import json, pathlib
import numpy as np
d = json.loads((pathlib.Path("robustness_results.json")).read_text())
cfg = d["config"]; M = d["main"]
DOSES = cfg["doses"]; CS = cfg["cs"]; RS = cfg["reliabilities"]; P = cfg["params"]
def get(kind,r,dose,c): return M[f"{kind}|{r}|{dose}|{c}"]

r_hi = min(RS, key=lambda x: abs(x-0.55)); r_lo = min(RS, key=lambda x: abs(x-0.31))
print(f"using r_hi={r_hi} (informative), r_lo={r_lo} (uninformative)\n")

print("=== P9: does dose carry through to the LASTING outcome? ===")
print("persistent insight at c=1.0 (full consolidation), r=%.3f" % r_hi)
print(f"{'dose':>6}" + "".join(f"{k.split('_')[0]:>12}" for k in P))
for dose in [DOSES[i] for i in (0,10,20,30,40)]:
    print(f"{dose:>6.2f}" + "".join(f"{get(k,r_hi,dose,1.0)[0]:>12.4f}" for k in P))
print("\nspread across dose (max-min) at c=1.0:")
for k in P:
    v=[get(k,r_hi,dose,1.0)[0] for dose in DOSES]
    print(f"  {k:>18}  {max(v)-min(v):.4f}")

print("\n=== P10: threshold in c (dose=0.8, r=%.3f) ===" % r_hi)
dose=min(DOSES,key=lambda x:abs(x-0.8))
print(f"{'c':>6}" + "".join(f"{k.split('_')[0]:>12}" for k in P))
for c in [CS[i] for i in (0,8,16,18,20,22,24,32,40)]:
    print(f"{c:>6.2f}" + "".join(f"{get(k,r_hi,dose,c)[0]:>12.4f}" for k in P))
print("\nsharpness: c range covering 5%->95% of final insight")
for k in P:
    v=np.array([get(k,r_hi,dose,c)[0] for c in CS]); lo,hi=v.min(),v.max()
    if hi-lo<0.05: print(f"  {k:>18}  flat"); continue
    idx=[i for i,x in enumerate(v) if x>=lo+0.05*(hi-lo)]
    jdx=[i for i,x in enumerate(v) if x>=lo+0.95*(hi-lo)]
    print(f"  {k:>18}  c={CS[idx[0]]:.3f} -> {CS[jdx[0]]:.3f}   width {CS[jdx[0]]-CS[idx[0]]:.3f}")

print("\n=== P11: is the gate shared between TRUE and FALSE insight? ===")
print("c at which each first appears (true>=0.05 of its max; false>=0.05 of its max)")
for k in P:
    vt=np.array([get(k,r_hi,dose,c)[0] for c in CS])
    vf=np.array([get(k,r_lo,dose,c)[2] for c in CS])
    def onset(v):
        lo,hi=v.min(),v.max()
        if hi-lo<0.02: return None
        return CS[[i for i,x in enumerate(v) if x>=lo+0.05*(hi-lo)][0]]
    ot,of_=onset(vt),onset(vf)
    print(f"  {k:>18}  true onset {str(ot):>6}   false onset {str(of_):>6}   "
          f"gap {'n/a' if None in (ot,of_) else f'{abs(ot-of_):.3f}'}")

print("\n=== P12: entrenchment shifts the threshold? (c* for 50% insight) ===")
E=d["entrenchment"]; g0s=sorted({float(x.split('|')[1]) for x in E})
print(f"{'gamma_0':>8}" + "".join(f"{k.split('_')[0]:>12}" for k in P))
for g in g0s:
    print(f"{g:>8.1f}" + "".join(f"{str(E[f'{k}|{g}']):>12}" for k in P))

print("\n=== structural robustness: does the shared gate survive K and window? ===")
S=d["structural"]
print(f"{'cell':>14}" + "".join(f"{k.split('_')[0]:>22}" for k in P))
print(f"{'':>14}" + "".join(f"{'true / false':>22}" for k in P))
for kk in sorted({x.split('|',1)[1] for x in S}, key=lambda s:(int(s.split('K=')[1].split('|')[0]), int(s.split('W=')[1]))):
    row=f"{kk:>14}"
    for k in P:
        v=S[f"{k}|{kk}"]; row+=f"{str(v['c_true50']):>10} /{str(v['c_false5']):>10}"
    print(row)
