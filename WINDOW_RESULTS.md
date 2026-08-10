# The therapeutic window: dose, cost, and timing

Arm declared in AMENDMENT_6.md (commit 6d4e093) before the code existed. Predictions
24 to 26. Grid: 5 costs x 21 doses x 14 consolidation timings x 3 consolidation
strengths x 20,000 trials, trajectories shared across timing and strength. The
no-session baseline is the undosed prior itself: conviction 0.8007, argmax on the
maladaptive belief.

## Prediction 24, confirmed, with one refinement the prediction missed

Consolidating the window-end belief (t_c = 14, c = 0.8), the dose at which lasting
conviction first falls below the no-session baseline sits essentially at the acute
SEBUS-to-REBUS crossover measured in the costly-test arm, and it is robust to
consolidation strength:

| cost | lasting crossover | acute crossover | lasting crossover at c = 0.6 / 1.0 |
|---|---|---|---|
| 0.3 | 0.25 | 0.23 | 0.25 / 0.25 |
| 0.5 | 0.45 | 0.42 | |
| 0.8 | 0.55 | 0.50 | |
| 1.2 | 0.55 | 0.50 | |

Below the crossover the session leaves lasting conviction above baseline: the same
session that was meant to revise the belief entrenches it, because integration locks
in the shallow-sampling inflation that the dose was too low to interrupt. Above the
crossover it helps. So the acute crossover is not just an acute curiosity; it is the
lower edge of the therapeutic dose window once consolidation is added.

**The refinement: above the cost ceiling, conviction and insight come apart.** The
prediction said no dose helps at cost 1.2. That is true for insight and false for
conviction. Lasting insight at the best dose, by cost:

| cost | 0.0 | 0.3 | 0.5 | 0.8 | 1.2 |
|---|---|---|---|---|---|
| max lasting insight | 0.886 | 0.519 | 0.167 | 0.017 | 0.001 |

At cost 1.2 the deep probe never runs (usage 0.000 at every dose), so no evidence
for the true hypothesis is ever gathered and lasting insight is zero. But high dose
still drags lasting conviction below baseline (0.548 at dose 1.0), purely because
relaxation dilutes the conviction and consolidation locks the dilution in. Above the
ceiling a session can weaken the belief but cannot replace it: dissolution without
insight. This dissociation was not predicted and is reported as a post hoc
observation.

## Prediction 25, confirmed at the threshold cost, failed above it

The within-window conviction trajectory (mean over 20,000 agents):

- **Cost 0.0**: peak at step 2, then a hard monotone fall at every dose. The test is
  affordable, the agent runs it early, revision dominates the window.
- **Cost 0.3** (just above the SEBUS threshold): rise then fall at every dose, as
  predicted. Peak conviction at step 9 at dose 0, moving to step 6 as dose rises,
  confirming that t* decreases with dose: relaxation brings the avoided test
  forward.
- **Cost 0.5 and up**: the rise never turns over within the 14-step window. The
  predicted fall requires the deep probe to run, and at these costs it does not.

So the non-monotone shape and the timing threshold exist exactly in the cost band
where the drug's mechanism (making the avoided test worth running) is active, which
is coherent with the whole account: below the band the test was never avoided, above
the band it is never taken.

**The timing rule that falls out is not "integrate early."** Consolidating early
(t_c = 4) does leave conviction lower than consolidating at the mid-window peak, but
it locks in almost nothing: at cost 0.3, dose 0.5, lasting insight is 0.003
consolidating at step 4 against 0.130 at step 14. Early integration consolidates
dilution, not learning. Mid-window integration consolidates the inflation peak,
the worst option. The rule the model actually supports: **integration helps only
when it captures the state after the avoided test has run**, and the drug's role is
to make that happen earlier and more often.

## Prediction 26, confirmed

Across every cost, timing, and consolidation strength (4,200 dose-versus-zero
comparisons), the maximum excess of lasting conviction at any dose over dose zero is
negative: -0.0046. In this model the drug never adds entrenchment, lasting or acute.
Harm comes from cost and timing, not from dose. The model therefore continues to
produce ALBUS's crossover structure without ALBUS's active low-dose strengthening.

## What this adds to the poster

One sentence: **the therapeutic window is three-dimensional; dose must clear the
cost-dependent crossover, cost must sit below the ceiling, and integration must come
after the avoided test has run, and missing any one coordinate makes the same
session entrench the belief or dissolve it without replacing it.** Figure:
figure_window.png (panel C is the window map).

## Limits

- Everything inherited from the costly-test arm: the cost and c are free
  parameters, one test, one belief, a static world, belief dynamics only.
- t_c treats consolidation as a snapshot of one step. Real integration presumably
  weights the whole window; a decaying-trace variant is the obvious follow-up.
- The conviction-insight dissociation above the ceiling depends on P-A mixing
  toward a diluted belief. Under P-D (memory trace), consolidating no evidence
  would leave the original conviction intact instead. Mechanism-dependence again.

## Reproduce

```bash
.venv/bin/python window.py && .venv/bin/python figure_window.py
```
