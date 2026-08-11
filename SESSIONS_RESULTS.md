# Compounding sessions: the seal leaks, and the clinic's questions land on memory assumptions

Arm declared in AMENDMENT_9.md (commit 3615dd2) before the code existed. Predictions
34 to 37. Multi-session runs of the encoding-capture mechanism: 10,000 trials each
carrying their own evolving stored prior, 40-session horizon, both count-mass
variants (fixed mass and Dirichlet accumulation), with unbiased learning (L-E) and
exact perception (kappa = 1) as comparators. Most of the declared predictions failed,
and the failures are the findings.

## Prediction 34: mechanism confirmed, magnitude failed, and a correction issued

The predicted shape was right: erosion is convex, a slow leak then a dam break. Mean
conviction under capture (kappa = 3, r = 0.40, fixed mass) across untreated sessions:
0.795 at session 1, 0.649 at 5, 0.371 at 10, 0.090 at 20. Each session's small leak
weakens the top-down grip, which frees the next session's encoding, which leaks
faster.

The predicted magnitude was wrong. Sessions to majority insight (S50), r = 0.40:

| learning | fixed mass | accumulating mass |
|---|---|---|
| unbiased (L-E) | 3 | 4 |
| capture, exact perception (kappa = 1) | 6 | 13 |
| capture, strong top-down (kappa = 3) | 8 | 23 |

The declared bar was S50(kappa = 3) at least three times S50(kappa = 1): observed
1.3x (fixed) and 1.8x (accumulating). **Failed.** Capture delays recovery by a factor
of roughly three to six relative to unbiased learning, and that is all it does in
this world. Neither declared alternative occurred: no plateau, and no climb. The
graveyard of strengthening routes gains one more grave: cross-session compounding
does not strengthen beliefs either.

> **Correction to HIERARCHY_RESULTS.md, same-day.** That file says "no amount of
> learning erodes the belief" under capture. True within one session, where the
> increment mirrors a fixed prior. Across sessions the mirrored prior is itself
> slightly eroded each time, so the freeze is not a fixed point; it is a slow leak
> with positive feedback. Self-sealing is a within-session phenomenon and a
> multi-session delay, not destiny. A correction note now sits in that file.

The delay is real and scales the right way (r = 0.70 erases it entirely: S50 of 2 to
3 everywhere; E robustness ordinal as expected). But the dramatic single-session
freeze dissolves in eight sessions in a stationary world where the truth keeps
generating evidence. Whether real chronic beliefs live in such a world is exactly
the question this result throws back at the theories, and the model cannot answer
it. What it can say: within the model family, lasting rigidity cannot come from
biased perception alone; it needs the world to stop cooperating (or the agent to
stop sampling it, which is the avoidance arm's territory, and the two have not yet
been composed).

## Prediction 35: the fork matters, but both declared shapes were wrong

Course length (dosed sessions to S50) after j untreated sessions, kappa = 3:

| j | fixed, d=0.2 | fixed, d=1.0 | accum, d=0.2 | accum, d=1.0 |
|---|---|---|---|---|
| 0 | 6 | 3 | 12 | 5 |
| 5 | 3 | 2 | **15** | **11** |
| 10 | 1 | 1 | 12 | 12 |
| 20 | 1 | 1 | 3 | 4 |
| 40 | 1 | 1 | 1 | 1 |

Declared: course length flat in j under fixed mass, rising (possibly to unreachable)
under accumulation. Observed: under fixed mass chronicity **helps** (natural erosion
does the work before treatment starts), and under accumulation the relationship is
**non-monotone**, hardest at j around 5: early on, count mass grows faster than the
belief erodes, so the worst moment to begin treatment is a few sessions in; later,
erosion has already won. The hump needs both ingredients: at kappa = 1 under
accumulation the course length falls monotonically (11, 8, 3, 1), so the hardest
window is an interaction of interpretive capture with accumulating mass. No cell was
unreachable.

The prediction's core survives its shapes: whether going untreated longer makes
treatment harder is decided by the count-mass assumption and the world's
stationarity, not by anything either psychedelic theory states. But the benign-world
caveat belongs in bold: in this world, time heals. A model in which evidence stops
arriving, or the agent stops looking, would answer differently, and neither variant
has been run.

## Prediction 36: the dose threshold is dead, as the declared alternative

Every dose converges, including d = 0.2 at kappa = 3 (course 6, 5, 4, 3, 3 across
the dose grid at j = 0, fixed mass). Dose buys speed, never possibility. The declared
alternative fires: no cumulative-treatment threshold exists in this family. The
contrast with the acting arm's cost ceiling is instructive: avoidance can price the
drug out entirely; capture cannot, because perception still lets a trickle of truth
through and trickles compound.

## Prediction 37: both declared shapes failed; what holds is exposure sufficiency

Insight fraction at the 20-session horizon, matched total exposure of 1.0 after 10
untreated sessions:

| protocol | fixed mass | accumulating mass |
|---|---|---|
| one session at d = 1.0 | 0.996 | 0.634 |
| two sessions at d = 0.5 | 0.993 | 0.643 |
| five sessions at d = 0.2 | 0.986 | 0.636 |

No protocol dominates under either variant; the declared falsifier fires for both
halves of the prediction. Within this grid, total exposure is sufficient: one large
session and several small ones land within a point of each other, while the mass
assumption moves the outcome by 35 points. The model's cleanest practical statement,
free-parameter caveats attached: protocol shape is a second-order question; what
memory does between sessions is first-order, and it is unmeasured.

## What this arm changes

Two more unstated assumptions now carry the clinically loaded answers: **count-mass
dynamics** (does experience rigidify) and **world stationarity** (does disconfirming
evidence keep arriving). Chronicity, minimum effective dose, and protocol shape all
land on those two, not on the drug mechanics either theory describes. And the
capture mechanism is downgraded honestly: a strong within-session distortion and a
multi-session delay, not a life sentence, in any world that keeps talking back.

## Limits

- The world is stationary and benign: the true context never stops generating
  evidence, sessions arrive on schedule, and nothing in the environment responds to
  the agent's state. Every "time heals" result is conditional on that.
- Capture and avoidance have not been composed; the obvious next arm is an acting
  agent with biased perception, where the agent can stop sampling the world that
  would have healed it.
- S50 is a population criterion (insight fraction 0.5); per-trial course lengths
  vary and were not analyzed.
- All prior limits carry over.

## Reproduce

```bash
.venv/bin/python sessions.py && .venv/bin/python figure_sessions.py
```
