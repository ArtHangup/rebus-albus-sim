"""Ratchet figure. Data from ratchet.py (AMENDMENT_10)."""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d = json.loads(pathlib.Path("ratchet_results.json").read_text())
CONV0 = d["config"]["conv0"]
S = np.arange(1, d["config"]["horizon"] + 1)

fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))

# A: natural history
for cost, kap, col, lbl in ((0.0, 3.0, "#999999", "test affordable (cost 0)"),
                            (0.3, 1.0, "#6baed6", "avoidance only (cost 0.3, exact)"),
                            (0.3, 3.0, "#b2182b", "avoidance + capture (cost 0.3)"),
                            (0.8, 1.0, "#e08214", "high cost, exact perception"),
                            (0.8, 3.0, "#67001f", "high cost + capture")):
    ys = [t[0] for t in d["natural"][f"{cost}|{kap}|fixed"]]
    ax[0].plot(S, ys, lw=2.2, color=col, label=lbl)
ax[0].axhline(CONV0, color="k", ls=":", lw=1.2)
ax[0].text(40, CONV0 - .05, "starting conviction", fontsize=8, ha="right")
ax[0].set_title("A. Untreated: the first permanent entrenchment.\nAvoidance loads the trap, capture locks it")
ax[0].set_xlabel("session"); ax[0].set_ylabel("stored conviction")
ax[0].legend(fontsize=7, loc="center right"); ax[0].grid(alpha=.25)
ax[0].set_ylim(0, 1.05)

# B: the mediator escape channel
for kap, col, lbl in ((1.0, "#6baed6", "exact perception: stored doubt\nreopens the test, then resolves"),
                      (3.0, "#b2182b", "capture: doubt is never credited,\nthe door stays shut")):
    ys = [t[2] for t in d["natural"][f"0.3|{kap}|fixed"]]
    ax[1].plot(S, ys, lw=2.2, color=col, label=lbl)
ax[1].set_title("B. The escape channel (cost 0.3):\ndiagnostic engagement across sessions")
ax[1].set_xlabel("session"); ax[1].set_ylabel("deep-probe usage")
ax[1].legend(fontsize=8); ax[1].grid(alpha=.25)

# C: treatment
SS = np.arange(1, len(d["treatment"]["0.3|fixed|5|0.6"]["traj"]) + 1)
for key, col, style, lbl in (
        ("natural:0.3|3.0|fixed", "#b2182b", "-", "untreated (cost 0.3)"),
        ("treat:0.3|fixed|5|0.6", "#1b7837", "-", "d=0.6 starting session 5: cured"),
        ("treat:0.3|fixed|20|0.6", "#5aae61", "--", "d=0.6 starting session 20: never"),
        ("treat:0.3|accum|20|1.0", "#762a83", "--", "d=1.0, session 20, accumulating mass: never"),
        ("treat:0.8|fixed|5|1.0", "#555555", "-.", "cost 0.8, d=1.0: dissolves, never resolves")):
    src, k = key.split(":")
    traj = d["natural"][k] if src == "natural" else d["treatment"][k]["traj"]
    ys = [t[0] for t in traj]
    ax[2].plot(np.arange(1, len(ys) + 1), ys, style, lw=2.1, color=col, label=lbl)
ax[2].annotate("dissolution without insight:\nthe belief is neither held nor replaced",
               xy=(38, 0.425), xytext=(13, 0.13), fontsize=8,
               arrowprops=dict(arrowstyle="->", lw=.9))
ax[2].set_title("C. Treatment fails three different ways:\nlate, subthreshold, or evidence-starved")
ax[2].set_xlabel("session"); ax[2].set_ylabel("stored conviction")
ax[2].legend(fontsize=7, loc="upper right"); ax[2].grid(alpha=.25); ax[2].set_ylim(0, 1.09)

fig.suptitle("Chronic belief is a composition phenomenon: no single mechanism entrenches, "
             "avoidance plus capture does, and each treatment failure mode has an observable signature",
             fontsize=11.5)
fig.tight_layout()
fig.savefig("figure_ratchet.png", dpi=170)
print("wrote figure_ratchet.png")
