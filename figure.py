"""The poster figure: consolidation is a gate, dose is a gain, and the gate is blind.

Reads dense_grids.json (produced by dense_grids.py, a resolution-only recompute of
the quantities in consolidation_results.json). Extents are set so tick values sit at
cell centers, which fixes the panel B tick misalignment noted in RESULTS.md: that
panel previously drew three unequally spaced doses as equal-width categorical
columns on an axis that read as continuous.
"""

import json
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = pathlib.Path(__file__).parent
d = json.loads((HERE / "dense_grids.json").read_text())

DOSES = np.array(d["doses"])
CS = np.array(d["cs"])

# Cell-center alignment: N cells whose centers span [0, 1].
half_d = (DOSES[1] - DOSES[0]) / 2
half_c = (CS[1] - CS[0]) / 2
EXTENT = [-half_d, 1 + half_d, -half_c, 1 + half_c]

fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

# Panel A: persistent insight, good evidence
m = np.array(d["insight_r055"])
im = axes[0].imshow(m, origin="lower", aspect="auto", cmap="viridis",
                    vmin=0, vmax=1, extent=EXTENT)
axes[0].axhline(0.5, color="w", ls="--", lw=1.4)
axes[0].set_title("A. Lasting insight\n(informative evidence, r = 0.55)")
axes[0].set_xlabel("dose (prior precision reduction)")
axes[0].set_ylabel("consolidation strength c")
fig.colorbar(im, ax=axes[0], label="persistent insight rate")

# Panel B: persistent false insight, poor evidence, same continuous axes as A
m2 = np.array(d["false_insight_r030"])
im2 = axes[1].imshow(m2, origin="lower", aspect="auto", cmap="magma",
                     vmin=0, vmax=0.3, extent=EXTENT)
axes[1].axhline(0.5, color="w", ls="--", lw=1.4)
axes[1].set_title("B. Lasting FALSE insight\n(uninformative evidence, r = 0.30)")
axes[1].set_xlabel("dose")
axes[1].set_ylabel("consolidation strength c")
fig.colorbar(im2, ax=axes[1], label="persistent false insight rate")

# Panel C: the SEBUS test
seb = d["sebus"]
axes[2].axhline(seb["baseline"], color="k", ls=":", lw=1.4,
                label="pre-dose conviction")
for r, style in ((0.3, "-o"), (0.55, "-s"), (0.85, "-^")):
    axes[2].plot(DOSES, seb["curves"][f"{r}"], style, ms=4, markevery=4,
                 label=f"evidence r = {r}")
axes[2].set_title("C. ALBUS predicts a rise here.\nThere is none.")
axes[2].set_xlabel("dose")
axes[2].set_ylabel("conviction in the maladaptive belief")
axes[2].set_ylim(-0.05, 1.05)
axes[2].legend(fontsize=8)

fig.suptitle("Relaxing priors is not enough: consolidation gates lasting change, "
             "and the gate does not check whether the belief is true",
             fontsize=12)
fig.tight_layout()
out = HERE / "figure_main.png"
fig.savefig(out, dpi=170)
print(f"wrote {out.name}")
