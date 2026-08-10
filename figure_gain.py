"""Gain versus avoidance figure. Data from gain.py and gain_posthoc.py (AMENDMENT_7)."""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d = json.loads(pathlib.Path("gain_results.json").read_text())
ph = json.loads(pathlib.Path("gain_posthoc.json").read_text())
DOSES = np.array(d["config"]["doses"])
base = d["acting"]["baseline"]
g = lambda A, c, dd: d["acting"]["grid"][f"{A}|{c}|{dd}"]
gp = lambda A, c, dd: ph["grid"][f"{A}|{c}|{dd}"]

fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))

# A: the implemented mapping
for A, col in zip((0.0, 1.0, 2.0, 4.0), plt.cm.plasma(np.linspace(0.05, 0.75, 4))):
    ax[0].plot(DOSES, (1 - DOSES) * (1 + A * DOSES), lw=2.2, color=col,
               label=f"A = {A:g}" + ("  (REBUS mapping)" if A == 0 else ""))
ax[0].axhline(1.0, color="k", ls=":", lw=1.2)
ax[0].set_title("A. ALBUS's gain mechanism, implemented:\n$\\gamma(d)/\\gamma_0 = (1-d)(1+Ad)$")
ax[0].set_xlabel("dose"); ax[0].set_ylabel("prior precision multiplier")
ax[0].legend(fontsize=8); ax[0].grid(alpha=.25)

# B: the sign discriminator on the mediator
for A, cost, col, lbl in ((4.0, 0.0, "#7b2d8b", "gain (A=4, free test)"),
                          (0.0, 0.3, "#1b6ca8", "avoidance (A=0, cost 0.3)"),
                          (0.0, 0.0, "#888888", "neither (A=0, free test)")):
    ys = [g(A, cost, dd)["deep_rate"] - g(A, cost, 0.0)["deep_rate"] for dd in DOSES]
    ax[1].plot(DOSES, ys, lw=2.2, color=col, label=lbl)
ax[1].axhline(0, color="k", lw=.8)
ax[1].set_title("B. The discriminator: change in diagnostic\nengagement from its sober value")
ax[1].set_xlabel("dose"); ax[1].set_ylabel("deep-probe usage minus usage at dose 0")
ax[1].legend(fontsize=8, loc="upper left"); ax[1].grid(alpha=.25)
ax[1].text(.985, .04, "gain says the drug suppresses checking;\navoidance says it never does",
           fontsize=8, ha="right", transform=ax[1].transAxes)

# C: drug-added strengthening exists only with both mechanisms
ax[2].axhline(base, color="k", ls=":", lw=1.5)
ax[2].text(0.99, base + .012, "pre-dose conviction", fontsize=8, ha="right")
ax[2].fill_between([0, 1], base, 1.0, color="crimson", alpha=.07)
for A, cost, col, lbl, src in ((4.0, 0.0, "#7b2d8b", "gain alone (A=4, cost 0)", g),
                               (0.0, 0.3, "#1b6ca8", "avoidance alone (A=0, cost 0.3)", g),
                               (4.0, 0.1, "crimson", "both (A=4, cost 0.1, post hoc)", gp)):
    ax[2].plot(DOSES, [src(A, cost, dd)["conviction"] for dd in DOSES],
               lw=2.4 if cost == 0.1 else 2.0, color=col, label=lbl)
ax[2].annotate("the one regime where the drug\nADDS strengthening", xy=(0.37, 0.845),
               xytext=(0.30, 0.62), fontsize=8,
               arrowprops=dict(arrowstyle="->", lw=.9))
ax[2].set_title("C. Active strengthening requires gain\nAND avoidance together")
ax[2].set_xlabel("dose"); ax[2].set_ylabel("conviction at window end")
ax[2].legend(fontsize=8, loc="lower left"); ax[2].grid(alpha=.25); ax[2].set_ylim(0, 1)

fig.suptitle("ALBUS's own mechanism, implemented: it cannot beat a freely run test, cannot "
             "entrench without avoidance, and adds strengthening only jointly with it",
             fontsize=11.5)
fig.tight_layout()
fig.savefig("figure_gain.png", dpi=170)
print("wrote figure_gain.png")
