import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
d=json.loads(pathlib.Path("cost_results.json").read_text())
ac=json.loads(pathlib.Path("acting_results.json").read_text())
mc=json.loads(pathlib.Path("miscal_results.json").read_text())
DO=np.array(d["doses"]); COSTS=d["costs"]; base=d["baseline"]
fig,ax=plt.subplots(1,3,figsize=(15.5,4.8))
cm=plt.cm.viridis(np.linspace(0,.9,len(COSTS)))

for c,col in zip(COSTS,cm):
    ax[0].plot(DO,[d["grid"][f"{c}|{dd}"]["conviction"] for dd in DO],lw=2,color=col,label=f"cost {c}")
ax[0].axhline(base,color="k",ls=":",lw=1.5)
ax[0].text(0.52,base+.012,"pre-dose conviction",fontsize=8)
ax[0].fill_between([0,1],base,1.0,color="crimson",alpha=.07)
ax[0].text(.03,.965,"SEBUS region",fontsize=8,color="crimson",transform=ax[0].transAxes)
ax[0].set_title("A. Belief strengthening appears only when\nthe diagnostic test is costly")
ax[0].set_xlabel("dose (prior precision reduction)"); ax[0].set_ylabel("conviction in the untested belief")
ax[0].legend(fontsize=7,ncol=2); ax[0].grid(alpha=.25); ax[0].set_ylim(0,1)

for c,col in zip(COSTS,cm):
    ax[1].plot(DO,[d["grid"][f"{c}|{dd}"]["deep_rate"] for dd in DO],lw=2,color=col)
ax[1].set_title("B. The mediator: dose makes the agent\nrun the test it was avoiding")
ax[1].set_xlabel("dose"); ax[1].set_ylabel("diagnostic-test usage rate"); ax[1].grid(alpha=.25)
ax[1].set_ylim(-0.012,0.285)
ax[1].annotate("no cost: flat, even falling",xy=(.45,.249),xytext=(.02,.267),fontsize=8,
    arrowprops=dict(arrowstyle="->",lw=.9))
ax[1].annotate("costly: rises with dose",xy=(.7,.099),xytext=(.2,.114),fontsize=8,
    arrowprops=dict(arrowstyle="->",lw=.9))

G="3.0"; b3=0.8007
ax[2].axhline(b3,color="k",ls=":",lw=1.5)
ax[2].plot(DO,[ac["confusable"][f"{dd}|{G}"]["conviction"] for dd in ac["doses"]],lw=2.2,label="2. epistemic action")
ax[2].plot(DO,[mc["miscalibrated"][f"{dd}|{G}"]["conviction"] for dd in mc["doses"]],lw=2.2,label="3. + miscalibrated")
ax[2].plot(DO,[d["grid"][f"0.5|{dd}"]["conviction"] for dd in DO],lw=2.6,color="crimson",label="4. + costly test")
ax[2].text(.55,b3+.015,"pre-dose conviction",fontsize=8)
ax[2].set_title("C. Three precision mechanisms fail.\nOnly avoidance crosses the line.")
ax[2].set_xlabel("dose"); ax[2].set_ylabel("conviction"); ax[2].legend(fontsize=8); ax[2].grid(alpha=.25); ax[2].set_ylim(0,1)
fig.suptitle("SEBUS is not a precision phenomenon. It requires that the agent was avoiding the test that would disconfirm it.",fontsize=12)
fig.tight_layout(); fig.savefig("figure_acting.png",dpi=170); print("wrote figure_acting.png")
