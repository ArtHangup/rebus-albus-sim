# The ratchet: avoidance loads the trap, capture locks it

Arm declared in AMENDMENT_10.md (commit ca798a0) before the code existed.
Predictions 38 to 41. The acting model's within-session mechanics unchanged;
capture-weighted stepwise learning; stored prior evolving across sessions, 10,000
trials, 40-session horizon plus treatment protocols.

## Prediction 38, confirmed where it matters: permanent entrenchment exists

Stored conviction across untreated sessions (fixed mass, start 0.8007):

| cost | kappa | s1 | s5 | s10 | s20 | s40 | recovery (S50) |
|---|---|---|---|---|---|---|---|
| 0.0 | 1 or 3 | 0.74 to 0.77 | 0.33 to 0.38 | ~0.10 | ~0.02 | 0.004 | session 4 |
| 0.3 | 1 | 0.829 | 0.844 | 0.737 | 0.424 | 0.127 | session 17 |
| 0.3 | 3 | 0.859 | 0.963 | 0.987 | 0.989 | **0.989** | **never** |
| 0.8 | 1 | 0.837 | 0.910 | 0.937 | 0.947 | **0.946** | **never** |
| 0.8 | 3 | 0.863 | 0.970 | 0.996 | 1.000 | **1.000** | **never** |

For the first time in ten amendments, belief strengthens over time and stays
strengthened. Insight at session 40 in the locked cells: 0.011 and 0.000. The
declared bar (conviction above start by 0.02 at session 40 at both kappas) is met
at cost 0.8 and fails at cost 0.3 kappa = 1, where the ratchet is transient: a
climb to 0.844, then recovery by session 17.

That transient case is the mechanism made visible, via the mediator. Deep-probe
usage across sessions at cost 0.3: kappa = 1 rises (0.024, 0.036, 0.053, 0.061)
until the test gets paid for and the belief resolves; kappa = 3 falls and stays
down (0.023, 0.017, 0.015, 0.015). The reason: with the deep test avoided, shallow
eliminations migrate stored mass onto the {0, 1} pair jointly, which rebuilds
exactly the uncertainty that makes the test worth its cost. **Avoidance alone is
self-limiting: it stores up the doubt that eventually reopens the test.** Capture
prevents that doubt from ever being credited (interpreted outcomes give the
conviction's share to the conviction), so the door never reopens. At cost 0.8 the
door was never open at any point (usage 0.000 flat, both kappas), and even exact
perception locks.

One sentence for the poster: **avoidance loads the trap; capture springs it shut;
high enough cost welds it.**

## Prediction 39: boundary confirmed and harsher than declared; the harmful half dies

Treatment courses (dosed sessions to majority insight, kappa = 3, fixed mass):

| cost | chronicity j | d = 0.2 | d = 0.6 | d = 1.0 |
|---|---|---|---|---|
| 0.3 | 5 | never | 12 | 5 |
| 0.3 | 20 | never | **never** | 5 |
| 0.8 | 5 or 20 | never | never | **never** |
| 1.2 | 5 or 20 | never | never | never |

The declared boundary (the within-session crossover) held for cost 0.3 at low
chronicity and was far too optimistic elsewhere: at cost 0.8 **no dose converges**,
against a declared prediction that 0.6 and 1.0 would. The failure mode is new and
worth naming. At cost 0.8, d = 1.0, the dosed sessions dissolve the conviction
(0.970 to 0.492 in five sessions) and then stall at 0.42 forever, with deep usage
still 0.001 and insight creeping to 0.43 without ever crossing: the test stays
priced out even at full relaxation, so no discriminating evidence ever arrives, and
the 0-versus-1 tie cannot be broken. **Dissolution without insight, previously a
single-session curiosity of the gain arm, is here the permanent terminal state of
aggressive treatment under high avoidance.** The belief is neither held nor
replaced.

The "subthreshold dosing is actively harmful" half of the prediction dies as
declared: sustained d = 0.2 ends at conviction 0.977 against 0.989 untreated at
cost 0.3, and 1.000 against 1.000 at cost 0.8. Subthreshold dosing is useless, not
harmful; there was no headroom left for "worse," because untreated natural history
under the ratchet already saturates. The window arm's harm finding applies to a
single session against a fresh baseline, not to a locked chronic state.

## Prediction 40, confirmed to the point of infinity

At cost 0.3, d = 0.6: course 12 at j = 5, **never** at j = 20, under fixed mass,
where the sessions arm had found that time heals. Chronicity under the ratchet is
real chronicity: waiting converts a treatable case into an untreatable one, and the
reversal against AMENDMENT_9 quantifies exactly what the benign-world assumption
was doing: same learning machinery, opposite conclusion, and the difference is who
chooses the evidence. Mass accumulation removes the last rescue: at j = 20 under
accumulating mass, even d = 1.0 never converges (5 sessions under fixed mass).

## Prediction 41, confirmed

At cost 0 the ratchet does not form at either kappa (recovery by session 4, faster
than the passive sessions arm because chosen probes are informative). Capture alone
cannot close the loop; avoidance is load-bearing, and capture converts a transient
trap into a permanent one.

## What this arm changes

The family now contains a complete mechanistic account of chronic belief that no
single piece produced: **entrenchment is a composition phenomenon.** Passive
distortion leaks (sessions arm), avoidance alone leaks through its own stored doubt
(this arm, kappa = 1), gain alone cannot beat a free test (gain arm). Permanence
requires avoidance plus one of: capture, high cost, or accumulated mass. And
treatment fails three distinct ways, each with a different clinical face: the dose
never opens the test (below-boundary failure), the test stays priced out at any
dose and the belief dissolves without being replaced (high-cost failure), or memory
mass outruns the course (chronicity failure). Every one of those failure modes is a
measurable prediction about behavior during treatment, and the mediator (diagnostic
engagement) is the observable that separates them.

## Limits

- The cost is still imposed rather than derived; the untreatable regimes inherit
  that free parameter. Deriving cost from expected self-model revision remains the
  named next step.
- One test, one belief, stationary world, belief dynamics only. The "dissolution
  without insight" state in particular should not be over-read clinically; it is a
  statement about this model's evidence starvation, not about any patient.
- S50 population criterion as before; per-trial heterogeneity unanalyzed.

## Reproduce

```bash
.venv/bin/python ratchet.py && .venv/bin/python figure_ratchet.py
```
