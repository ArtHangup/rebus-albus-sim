# Amendment 5: a costly diagnostic test

Written 2026-08-01, **after the miscalibration result, before implementing this arm.**

## What happened

Prediction 18 failed. Misspecified self-knowledge did not produce SEBUS either. Only one
cell in the entire grid rose above baseline: the weakest entrenchment, at dose zero, by
0.0067, which is not a dose effect at all.

Miscalibration was not inert. It made the agent substantially worse at finding the truth
(insight 0.416 against 0.654 calibrated at gamma_0 = 3.0). It just never made it more
confident in the untested belief than it started.

**Why all three failed, diagnosed:** in every arm a genuinely diagnostic test exists and
the agent's epistemic drive finds it valuable. It runs the deep probe roughly 14 to 25
percent of the time, and two or three uses carry enough evidence against the maladaptive
hypothesis to overwhelm everything else. Rigidity does not stop it. Misspecification about
the *other* tests does not stop it.

So the missing ingredient is not about precision or calibration. **It is about whether the
agent is willing to run the test at all.**

## This arm

Give the deep probe a **cost**, subtracted from its expected free energy before action
selection. Real diagnostic tests are effortful or aversive: confronting the belief that
organises your self-model is the expensive thing, which is exactly what avoidance means
clinically.

The cost is swept from zero upward. Nothing else changes.

## Why this is not circular

"An agent that avoids the disconfirming test stays confident" would be true by
construction and worth nothing. The non-trivial question is the **interaction with dose**:
relaxing the prior raises the agent's uncertainty about the 0-versus-1 distinction, which
raises the epistemic value of the deep probe, which may push it back above the cost
threshold. If so, then **prior relaxation causes the agent to face a test it was
previously avoiding**, and that is a mechanistic account of why the drug helps that neither
REBUS nor ALBUS states.

## Predictions, written before implementing

21. **SEBUS will emerge above some cost threshold.** With the diagnostic test priced out,
    shallow probes eliminate alternatives without testing the belief, and conviction rises
    above the pre-dose baseline.
22. **The dose response will become non-monotonic**, rising then falling, with the peak
    moving to higher dose as cost rises. This is ALBUS's shape, and it would place the
    SEBUS-to-REBUS crossover at the dose where epistemic value first exceeds the cost.
23. **Deep-probe usage will rise with dose in this arm**, unlike every previous arm where
    it was flat or falling. That is the mediator, and it is the claim that makes the story
    mechanistic rather than descriptive.
