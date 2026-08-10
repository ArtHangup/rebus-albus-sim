# Amendment 6: the therapeutic window

Written 2026-08-10, **before writing or running any of the code below.** Prior commits:
8109e7f (mapping), 860c369, d003810, ca4622e, b9a5d47, daef447 (costly test declared),
ec32da4 (costly-test results).

## Why this arm exists

The costly-test arm established where SEBUS lives: above a cost threshold the agent ends
the acute window more convinced of the untested belief than it began, and prior
relaxation helps by making the avoided test worth running. The consolidation arms
established that nothing lasts without integration, and that what consolidation operates
on decides whether dose matters.

Those two results have never been composed. The acting agent's window belief has never
been consolidated, so the model has not yet answered the clinical question it is now
equipped to ask: **when does a session help, and when does it entrench the belief it was
meant to revise?** The hypothesis is that the answer is a window jointly bounded by test
cost, dose, and consolidation timing.

## Design

The acting agent of AMENDMENT_3 with the costly deep probe of AMENDMENT_5, unchanged:
same confusable probe structure, same epistemic-only action selection, same dose mapping
(initial prior relaxed to `gamma_0 * (1 - dose)`), `gamma_0 = 3.0`, `alpha = 8.0`, 14
decision steps, reliability 0.85 as in the costly-test runs. Nothing about the
within-window dynamics changes.

Two additions, both measurement-side:

1. **The belief trajectory is recorded at every step**, not only at window end.
2. **Consolidation is applied to the recorded belief at step `t_c`**, using the
   arithmetic mechanism of AMENDMENT_1 (P-A, kept for comparability with the existing
   gate results): `p_after = (1 - c) * p_orig + c * b(t_c)`, where `p_orig` is the
   undosed prior (conviction 0.8007). `t_c` is **consolidation timing**: how much of the
   session's evidence-gathering is captured by integration.

Grid, fixed in advance: costs {0.0, 0.3, 0.5, 0.8, 1.2} (spanning below threshold, at
threshold, mid, high, above ceiling), 21 doses 0 to 1, `t_c` in {1, ..., 14}, `c` in
{0.6, 0.8, 1.0} (all above the P-A gate; 0.8 is the reporting value, the others are
robustness), 20,000 trials per cost-dose cell with the trajectory shared across `t_c`
and `c`, seed 11.

Outcomes per cell: mean lasting conviction `E[p_after(1)]`, lasting insight rate
`P(argmax p_after = 0)`, and the comparison against the no-session baseline, which is
`p_orig` itself: a session **helps** where lasting conviction falls below 0.8007 and
**entrenches** where it ends above 0.8007.

## Predictions, written before running

24. **The benefit of dose is gated by the crossover.** At costs showing SEBUS (0.3 and
    up), consolidating the window-end belief (`t_c = 14`) leaves lasting conviction
    *above* the no-session baseline for doses below the SEBUS-to-REBUS crossover
    measured in the costly-test arm, and below baseline only for doses above it. The
    therapeutic window in dose is therefore approximately [crossover(cost), 1]: it
    shrinks as cost rises, and above the cost ceiling (1.2) no dose brings lasting
    conviction below baseline.

25. **Timing can flip the sign of the same session.** Under a costly test at moderate
    dose, the within-window conviction trajectory is non-monotone: it rises first,
    while cheap shallow probes eliminate irrelevant alternatives and inflate conviction
    by redistribution, and falls later, once relaxation-boosted epistemic value pushes
    the deep probe above its cost. Consequently there exists a timing threshold `t*`
    such that consolidating before `t*` entrenches the belief and consolidating after
    `t*` reduces it, and `t*` decreases with dose (higher dose brings the deep probe
    forward). Stated for the record: if the trajectory turns out monotone at every
    dose-cost cell, prediction 25 fails and the timing story is dead.

26. **Dose never adds entrenchment.** Holding cost, `c`, and `t_c` fixed, lasting
    conviction at any dose d > 0 is never meaningfully above its value at dose 0
    (tolerance: Monte Carlo error). Harm in this model comes from cost and timing, not
    from dose. This is the lasting-outcome extension of the dose-zero-peak result, and
    it is the claim on which this model departs from ALBUS as usually read: if some
    dose-cost-timing cell shows lasting conviction rising with dose, the model
    reproduces ALBUS's active low-dose strengthening after all, and that would be the
    more interesting result and must be reported as such.

## What would falsify the exercise

If consolidation timing and cost turn out not to interact (the helps-versus-entrenches
boundary is flat in `t_c` at every cost), then "the therapeutic window" reduces to the
crossover already reported and this arm adds nothing. That null is reportable and would
close the arm.
