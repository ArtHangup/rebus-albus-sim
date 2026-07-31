"""The poster figure: consolidation is a gate, dose is a gain, and the gate is blind."""

import json
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = pathlib.Path(__file__).parent
d = json.loads((HERE / "consolidation_results.json").read_text())

CS = np.round(np.linspace(0, 1, 21), 3)
DOSES = np.round(np.linspace(0, 1, 11), 3)


def grid(block, key, doses, cs):
    m = np.full((len(cs), len(doses)), np.nan)
    for i, c in enumerate(cs):
        for j, dd in enumerate(doses):
            cell = d[block].get(f"{dd}|{c}")
            if cell:
                m[i, j] = cell[key]
    return m


fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

# Panel A: persistent insight, good evidence
m = grid("dose_x_consolidation_r055", "insight", DOSES, CS)
im = axes[0].imshow(m, origin="lower", aspect="auto", cmap="viridis",
                    vmin=0, vmax=1, extent=[0, 1, 0, 1])
axes[0].axhline(0.5, color="w", ls="--", lw=1.4)
axes[0].set_title("A. Lasting insight\n(informative evidence, r = 0.55)")
axes[0].set_xlabel("dose (prior precision reduction)")
axes[0].set_ylabel("consolidation strength c")
fig.colorbar(im, ax=axes[0], label="persistent insight rate")

# Panel B: persistent false insight, poor evidence
cs2 = CS[::2]
doses2 = np.array([0.4, 0.8, 1.0])
m2 = grid("false_insight_r030", "false_insight", doses2, cs2)
im2 = axes[1].imshow(m2, origin="lower", aspect="auto", cmap="magma",
                     vmin=0, vmax=0.3,
                     extent=[0, len(doses2), 0, 1])
axes[1].axhline(0.5, color="w", ls="--", lw=1.4)
axes[1].set_xticks(np.arange(len(doses2)) + 0.5)
axes[1].set_xticklabels([f"{x:.1f}" for x in doses2])
axes[1].set_title("B. Lasting FALSE insight\n(uninformative evidence, r = 0.30)")
axes[1].set_xlabel("dose")
axes[1].set_ylabel("consolidation strength c")
fig.colorbar(im2, ax=axes[1], label="persistent false insight rate")

# Panel C: the SEBUS test
seb = d["sebus"]
axes[2].axhline(seb["baseline"], color="k", ls=":", lw=1.4,
                label="pre-dose conviction")
for r, style in ((0.30, "-o"), (0.55, "-s"), (0.85, "-^")):
    ys = [seb["grid"][f"{dd}|{r}"] for dd in DOSES]
    axes[2].plot(DOSES, ys, style, ms=4, label=f"evidence r = {r}")
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
