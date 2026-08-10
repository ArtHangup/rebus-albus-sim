"""The therapeutic-window figure. Data from window.py (AMENDMENT_6)."""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d = json.loads(pathlib.Path("window_results.json").read_text())
cfg = d["config"]
base = cfg["baseline"]
DOSES = np.array(cfg["doses"]); COSTS = cfg["costs"]; TCS = cfg["tcs"]
g = lambda c, dd, tc, cc: d["grid"][f"{c}|{dd}|{tc}|{cc}"]

fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))
cm = plt.cm.viridis(np.linspace(0, .85, len(COSTS)))

# A: lasting conviction vs dose by cost, t_c = 14, c = 0.8
for c, col in zip(COSTS, cm):
    ax[0].plot(DOSES, [g(c, dd, 14, 0.8)["conviction"] for dd in DOSES],
               lw=2, color=col, label=f"cost {c}")
ax[0].axhline(base, color="k", ls=":", lw=1.5)
ax[0].text(0.02, base + .012, "no-session baseline", fontsize=8)
ax[0].fill_between([0, 1], base, 1.0, color="crimson", alpha=.07)
ax[0].text(.63, .965, "session entrenches", fontsize=8, color="crimson",
           transform=ax[0].transAxes)
ax[0].set_title("A. Lasting conviction after integration:\ndose must clear the crossover")
ax[0].set_xlabel("dose (prior precision reduction)")
ax[0].set_ylabel("lasting conviction in the untested belief")
ax[0].legend(fontsize=7, loc="lower left"); ax[0].grid(alpha=.25); ax[0].set_ylim(0, 1)

# B: within-window trajectories at dose 0.5, one curve per cost
steps = np.arange(1, cfg["steps"] + 1)
for c, col in zip(COSTS, cm):
    ax[1].plot(steps, d["traj_conviction"][f"{c}|0.5"], lw=2, color=col)
ax[1].axhline(base, color="k", ls=":", lw=1.5)
ax[1].annotate("cost 0: test runs early, conviction falls", xy=(6, .42),
               xytext=(4.6, .30), fontsize=8, arrowprops=dict(arrowstyle="->", lw=.9))
ax[1].annotate("cost 0.3: rise, then the avoided\ntest finally runs", xy=(9.5, .685),
               xytext=(8.2, .53), fontsize=8, arrowprops=dict(arrowstyle="->", lw=.9))
ax[1].annotate("cost 0.5+: the fall never comes", xy=(11, .79), xytext=(4.2, .90),
               fontsize=8, arrowprops=dict(arrowstyle="->", lw=.9))
ax[1].set_title("B. Conviction within the window (dose 0.5):\nthe worst time to integrate is the peak")
ax[1].set_xlabel("decision step"); ax[1].set_ylabel("conviction")
ax[1].grid(alpha=.25); ax[1].set_ylim(0, 1)

# C: the window map at cost 0.3, c = 0.8
m = np.array([[g(0.3, dd, tc, 0.8)["conviction"] - base for dd in DOSES]
              for tc in TCS])
half = (DOSES[1] - DOSES[0]) / 2
im = ax[2].imshow(m, origin="lower", aspect="auto", cmap="RdBu_r",
                  vmin=-0.45, vmax=0.45,
                  extent=[-half, 1 + half, 0.5, len(TCS) + 0.5])
ax[2].set_title("C. The window map (cost 0.3):\nred entrenches, blue helps")
ax[2].set_xlabel("dose"); ax[2].set_ylabel("consolidation timing $t_c$ (step)")
fig.colorbar(im, ax=ax[2], label="lasting conviction minus baseline")

fig.suptitle("The therapeutic window is three-dimensional: dose above the crossover, "
             "cost below the ceiling, integration after the avoided test has run",
             fontsize=11.5)
fig.tight_layout()
fig.savefig("figure_window.png", dpi=170)
print("wrote figure_window.png")
