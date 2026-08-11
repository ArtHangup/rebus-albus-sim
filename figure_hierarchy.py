"""Hierarchy-with-learning figure. Data from hierarchy.py (AMENDMENT_8)."""
import json, pathlib
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

d = json.loads(pathlib.Path("hierarchy_results.json").read_text())
DOSES = np.array(d["config"]["doses"])
CONV0 = d["config"]["conv0"]
g = lambda k, r, dd, E: d["grid"][f"{k}|{r}|{dd}|{E}"]

fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.8))

# A: the fork, learning edition (r = 0.70, E = 20)
curves = (("L-P", "#1b6ca8", "posterior-driven (L-P)"),
          ("L-E", "#e07b39", "evidence-driven (L-E)"),
          ("L-D", "#a3336e", "decay only (L-D)"),
          ("L-H|1.0", "#6db56d", "encoding-driven, exact perception"),
          ("L-H|3.0", "#2e8b57", "encoding-driven, strong top-down"))
for key, col, lbl in curves:
    ax[0].plot(DOSES, [g(key, 0.7, dd, 20.0)["insight"] for dd in DOSES],
               lw=2.2, color=col, label=lbl)
ax[0].set_title("A. Learning inherits the fork:\nthe increment choice decides whether dose matters")
ax[0].set_xlabel("dose (prior precision reduction)")
ax[0].set_ylabel("lasting insight rate (learned prior)")
ax[0].legend(fontsize=7, loc="center right"); ax[0].grid(alpha=.25)
ax[0].set_ylim(-0.03, 1.0)

# B: self-sealing at dose 0
ES = [e for e in d["config"]["Es"] if e > 0]
for r, kap, col, lbl in ((0.4, 3.0, "#b2182b", "ambiguous world, strong top-down"),
                         (0.4, 1.0, "#ef8a62", "ambiguous world, exact perception"),
                         (0.7, 3.0, "#67a9cf", "clear world, strong top-down"),
                         (0.7, 1.0, "#2166ac", "clear world, exact perception")):
    ax[1].plot(ES, [g(f"L-H|{kap}", r, 0.0, E)["conviction"] for E in ES],
               "-o", ms=4, lw=2, color=col, label=lbl)
ax[1].axhline(CONV0, color="k", ls=":", lw=1.4)
ax[1].text(2.6, CONV0 + .012, "starting conviction", fontsize=8)
ax[1].set_xscale("log")
ax[1].set_title("B. Self-sealing: with ambiguity and strong top-down\nperception, no amount of learning erodes the belief")
ax[1].set_xlabel("learning amount E (log scale), dose 0")
ax[1].set_ylabel("lasting conviction")
ax[1].legend(fontsize=7, loc="lower left"); ax[1].grid(alpha=.25)

# C: plasticity scales, relaxation redirects
rules = ("evidence-driven\n(L-E)", "posterior-driven\n(L-P)", "encoding-driven\n(L-H, strong top-down)")
vals = (d["direction_shift"]["L-E"], d["direction_shift"]["L-P"],
        d["direction_shift"]["L-H|3.0"])
bars = ax[2].bar(rules, vals, color=("#e07b39", "#1b6ca8", "#2e8b57"), width=0.55)
for b, v in zip(bars, vals):
    ax[2].text(b.get_x() + b.get_width() / 2, v + 0.03, f"{v:.2f}",
               ha="center", fontsize=9)
ax[2].set_title("C. Plasticity scales, relaxation redirects:\nhow much dose changes WHAT is learned")
ax[2].set_ylabel("max L1 shift of the learning target across dose")
ax[2].set_ylim(0, 1.55); ax[2].grid(alpha=.25, axis="y")
ax[2].text(.5, .78, "a dose-dependent learning rate\ncannot move the zero bar:\nunder evidence-driven learning the\ndrug changes only how far, never where",
           fontsize=8, ha="center", transform=ax[2].transAxes)

fig.suptitle("Hierarchy and learning do not dissolve the fork: the increment source decides the drug's role, "
             "and rigid beliefs gain a third defense, interpretive capture",
             fontsize=11.5)
fig.tight_layout()
fig.savefig("figure_hierarchy.png", dpi=170)
print("wrote figure_hierarchy.png")
