"""Compounding-sessions figure. Data from sessions.py (AMENDMENT_9)."""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d = json.loads(pathlib.Path("sessions_results.json").read_text())
S = np.arange(1, d["config"]["horizon"] + 1)

fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))

# A: natural history, r = 0.40
styles = {"fixed": "-", "accum": "--"}
cols = {"L-E": "#e07b39", "L-H|1": "#6db56d", "L-H|3": "#2e8b57"}
lbls = {"L-E": "unbiased learning", "L-H|1": "capture, exact perception",
        "L-H|3": "capture, strong top-down"}
for key in ("L-E", "L-H|1", "L-H|3"):
    for mass in ("fixed", "accum"):
        ys = [t[1] for t in d["natural"][f"{key}|0.4|{mass}"]]
        ax[0].plot(S, ys, styles[mass], lw=2, color=cols[key],
                   label=f"{lbls[key]}, {mass} mass")
ax[0].axhline(0.5, color="k", ls=":", lw=1)
ax[0].set_title("A. Untreated natural history: the seal leaks,\nthen the dam breaks (ambiguous world)")
ax[0].set_xlabel("session"); ax[0].set_ylabel("insight fraction")
ax[0].legend(fontsize=7, loc="lower right"); ax[0].grid(alpha=.25)

# B: course length vs chronicity
for mass, kap, col, lbl in (("fixed", "3.0", "#1b6ca8", "fixed mass, capture"),
                            ("accum", "3.0", "#b2182b", "accumulating mass, capture"),
                            ("accum", "1.0", "#ef8a62", "accumulating mass, exact perception")):
    js = (0, 5, 10, 20, 40)
    ys = [d["treatment"][f"{kap}|{mass}|{j}|0.2"]["course"] for j in js]
    ax[1].plot(js, ys, "-o", ms=5, lw=2.2, color=col, label=lbl)
ax[1].annotate("the hardest window: mass has grown,\nthe belief has not yet eroded",
               xy=(5, 15), xytext=(11, 13.4), fontsize=8,
               arrowprops=dict(arrowstyle="->", lw=.9))
ax[1].set_title("B. Does waiting make treatment harder?\nThe memory assumption decides (d = 0.2)")
ax[1].set_xlabel("untreated sessions before treatment (chronicity)")
ax[1].set_ylabel("dosed sessions to majority insight")
ax[1].legend(fontsize=7); ax[1].grid(alpha=.25)

# C: protocol shape at matched exposure
names = ("a_single_1.0", "b_two_0.5", "c_five_0.2")
labels = ("one session\nat d = 1.0", "two sessions\nat d = 0.5", "five sessions\nat d = 0.2")
x = np.arange(3)
for off, mass, col in ((-0.18, "fixed", "#1b6ca8"), (0.18, "accum", "#b2182b")):
    vals = [d["shape"][f"{n}|{mass}"]["insight_end"] for n in names]
    bars = ax[2].bar(x + off, vals, width=0.34, color=col,
                     label=f"{mass} mass")
    for b, v in zip(bars, vals):
        ax[2].text(b.get_x() + b.get_width() / 2, v + .015, f"{v:.2f}",
                   ha="center", fontsize=8)
ax[2].set_xticks(x); ax[2].set_xticklabels(labels, fontsize=8)
ax[2].set_title("C. One big session or many small ones?\nAt matched exposure the model does not care")
ax[2].set_ylabel("insight fraction at 20-session horizon")
ax[2].set_ylim(0, 1.12); ax[2].legend(fontsize=8); ax[2].grid(alpha=.25, axis="y")

fig.suptitle("Across sessions the capture mechanism is a delay, not a destiny, and the clinical questions "
             "(chronicity, minimum dose, protocol shape) land on memory assumptions no theory states",
             fontsize=11.5)
fig.tight_layout()
fig.savefig("figure_sessions.png", dpi=170)
print("wrote figure_sessions.png")
