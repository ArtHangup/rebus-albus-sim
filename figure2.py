"""Robustness figure: does the drug matter, and is there a safe window?"""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d=json.loads(pathlib.Path("robustness_results.json").read_text())
cfg=d["config"]; M=d["main"]
DOSES=np.array(cfg["doses"]); CS=np.array(cfg["cs"]); RS=cfg["reliabilities"]; P=cfg["params"]
LBL={"P-A_arithmetic":"P-A arithmetic mixture","P-B_geometric":"P-B geometric mixture",
     "P-C_attractor":"P-C attractor weakening","P-D_memory":"P-D memory trace"}
COL=dict(zip(P,["#1b6ca8","#e07b39","#2e8b57","#a3336e"]))
r_hi=min(RS,key=lambda x:abs(x-0.55)); r_lo=min(RS,key=lambda x:abs(x-0.31))
g=lambda k,r,dd,c: M[f"{k}|{r}|{dd}|{c}"]

fig,ax=plt.subplots(1,3,figsize=(15.5,4.8))

# A: dose dependence at c = 0.8. Not 1.0: at full consolidation P-A and P-B coincide
# exactly (both reduce to the window belief), so the P-A curve hides under P-B.
C_A=0.8
for k in P:
    ax[0].plot(DOSES,[g(k,r_hi,dd,C_A)[0] for dd in DOSES],lw=2.2,color=COL[k],label=LBL[k])
ax[0].set_title(f"A. Does the drug change the lasting outcome?\nOnly if consolidation acts on the belief reached (c = {C_A})")
ax[0].set_xlabel("dose (prior precision reduction)"); ax[0].set_ylabel("persistent insight rate")
ax[0].set_ylim(0.38,1.02); ax[0].legend(fontsize=8,loc="lower right"); ax[0].grid(alpha=.25)
pc=g("P-C_attractor",r_hi,0.5,C_A)[0]; pd=g("P-D_memory",r_hi,0.5,C_A)[0]
ax[0].annotate("flat: dose is causally irrelevant",xy=(0.35,pc),xytext=(0.13,pc-0.055),
    fontsize=8,arrowprops=dict(arrowstyle="->",lw=.9))
ax[0].annotate("flat again, at the worst outcome",xy=(0.38,pd),xytext=(0.02,pd-0.045),
    fontsize=8,arrowprops=dict(arrowstyle="->",lw=.9))

# B: the safe window
dose=DOSES[np.argmin(abs(DOSES-0.8))]
for k in P:
    ax[1].plot(CS,[g(k,r_hi,dose,c)[0] for c in CS],lw=2.2,color=COL[k],label=LBL[k])
    ax[1].plot(CS,[g(k,r_lo,dose,c)[2] for c in CS],lw=1.6,ls="--",color=COL[k])
ax[1].set_title("B. Solid = lasting TRUE insight\nDashed = lasting FALSE insight")
ax[1].set_xlabel("consolidation strength c"); ax[1].set_ylabel("rate"); ax[1].grid(alpha=.25)
ax[1].text(.03,.93,"false always onsets later than true\n(all 4 mechanisms, all K, all windows)",
    fontsize=8,transform=ax[1].transAxes,va="top")

# C: entrenchment
E=d["entrenchment"]; g0=sorted({float(x.split('|')[1]) for x in E})
for k in P:
    ys=[E[f"{k}|{x}"] for x in g0]
    xs=[x for x,y in zip(g0,ys) if y is not None]; yy=[y for y in ys if y is not None]
    ax[2].plot(xs,yy,"-o",ms=5,lw=2.2,color=COL[k],label=LBL[k])
    if len(yy)<len(ys):
        ax[2].scatter([x for x,y in zip(g0,ys) if y is None],[1.03]*(len(ys)-len(yy)),
            marker="x",s=55,color=COL[k])
ax[2].axhline(1.0,color="k",lw=.6,ls=":")
ax[2].text(13,1.055,"x = unreachable at any c",fontsize=8)
ax[2].set_title("C. How much integration a belief demands\nrises with how entrenched it is")
ax[2].set_xlabel("entrenchment of the original conviction (gamma_0)")
ax[2].set_ylabel("consolidation needed for 50% insight"); ax[2].set_ylim(-0.05,1.12); ax[2].grid(alpha=.25)

fig.suptitle("Four defensible readings of 'the revision sticks' disagree about whether the drug is necessary, "
             "whether integration is safe, and whether some beliefs are treatable",fontsize=11.5)
fig.tight_layout(); fig.savefig("figure_robustness.png",dpi=170)
print("wrote figure_robustness.png")
