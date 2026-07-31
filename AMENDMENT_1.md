# Amendment 1: adding a consolidation arm

Written 2026-07-31, **after running arms 1 and 2, before writing or running the
consolidation arm.** The original preregistration is unchanged and remains committed at
8109e7f. This document exists so the sequence is auditable.

---

## What happened

Prediction 1 said the insight region would be a ridge in the dose-by-reliability plane. It
is not. In arm 1, pure REBUS, **dose has exactly zero effect on the terminal outcome**, at
every reliability.

The reason is structural rather than numerical, and it is visible in the algebra. In arm 1
the terminal belief is

    softmax(gamma_0 * u  +  lambda * cum_ll)

and `cum_ll` depends only on reliability and the random draws. Dose enters solely through
`gamma_d`, which applies during the window and is gone afterwards. So dose cannot appear in
the terminal belief. It is not that the effect is small. It is absent by construction.

## Why this is a result and not a bug

The model is not inert. Measured at the end of the window, dose does a great deal. At
reliability 0.55, over 3,000 trials per cell:

| dose | insight during window | insight after window | conviction in the wrong belief at window end |
|---|---|---|---|
| 0.0 | 0.684 | 0.684 | 0.318 |
| 0.2 | 0.815 | 0.695 | 0.199 |
| 0.4 | 0.890 | 0.667 | 0.121 |
| 0.6 | 0.937 | 0.679 | 0.064 |
| 0.8 | 0.960 | 0.691 | 0.026 |
| 1.0 | 0.963 | 0.669 | 0.012 |

A large acute effect that completely evaporates.

So the finding is this: **if the only thing the drug does is transiently reduce the
precision of a prior that then returns to full strength, it can produce no lasting change
at all.** The acute experience is not the mechanism. Something has to make the revision
stick.

That is not a defect of the simulation. It is REBUS taken literally, and it is why REBAS
was proposed as a separate construct.

## The added arm, declared before it is written

**Arm 3, consolidation.** At the end of the window the agent's structural prior becomes a
mixture of what it held before and what it reached during the window:

    p_after = (1 - c) * p_original  +  c * b_window

with `c` in [0, 1] a **consolidation strength**, interpretable as integration. `c = 0` is
complete relapse to the prior conviction. `c = 1` is full adoption of whatever the window
produced. The terminal belief is `p_after`, with no re-application of the evidence already
reflected in `b_window`, so nothing is double counted.

`c` is swept as a third axis. It is a free parameter and is reported as one. No value of
`c` is claimed to correspond to any clinical quantity.

## Predictions for arm 3, written before running it

6. **A consolidation threshold exists**, below which no dose produces lasting change.
   Because the outcome flips when `c * b_window(true) > (1 - c) * p_original(maladaptive)`,
   and the original conviction here is 0.998, the threshold should sit somewhere near
   `c ≈ 0.5` and should be **largely independent of dose** once the window belief is
   confident.
7. **The threshold rises with the rigidity of the original conviction.** A more entrenched
   belief should demand more consolidation to displace. If this holds, it is the model's
   clearest clinical statement: integration effort must scale with entrenchment.
8. **Consolidation is indiscriminate.** It should lock in false insights at the same rate
   it locks in true ones. Under low reliability, raising `c` should raise the persistent
   false-insight rate. If so, the mechanism that makes psychedelic therapy work is the same
   mechanism that makes it risky, and the two cannot be separated by tuning `c`.

Prediction 8 is the one I most expect to be uncomfortable and most want on the poster.

## Status of the original predictions

- **Prediction 1: FAILED**, for the structural reason above. Reported as a finding.
- **Prediction 2 (false insight rises with dose at low reliability): not yet evaluated**
  at the window-end timepoint, which is now the correct place to test it.
- **Prediction 3 (SEBUS will not emerge): still to be evaluated.**
- **Prediction 4 (persistence falls as dose rises): void in arm 1**, since there is no
  persistence at all. Re-scoped to arm 3.
- **Prediction 5 (arm 2 shows an interior optimum): FAILED.** Arm 2 is monotonically
  harmful, not humped. Dose only ever costs, because sensory degradation has no benefit to
  trade against once the prior effect cannot persist.
