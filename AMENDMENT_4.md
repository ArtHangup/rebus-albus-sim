# Amendment 4: miscalibrated self-knowledge

Written 2026-08-01, **after the acting-agent results, before implementing this arm.**

## What happened

Prediction 13 failed. The acting agent produced no SEBUS at any dose, at any entrenchment.
Conviction fell monotonically, peaking at dose zero and always **below** the pre-dose
baseline. Prediction 16 failed too: deep-probe usage was flat at roughly 0.21 to 0.25 and
slightly *decreasing* in dose, not rising.

The reason is a result I should have taken more seriously before building it. **A Bayesian
agent with a correct generative model does not fall into confirmation bias.** Its epistemic
value function correctly prices the deep probe according to how much 0-versus-1 uncertainty
it actually has, so it runs that probe whenever the uncertainty is real, and it revises.

The confusability structure was not inert. At dose zero it left conviction at 0.368 against
0.057 in the separable control, a factor of six. So the structure **retards** revision
substantially. It just never reverses it.

Two independent mechanisms have now failed to produce ALBUS's prediction: passive precision
reduction, and epistemic action under a correct model.

## The remaining candidate, and why it is not circular

The agent above knows which of its probes are diagnostic. Real agents do not. The clinical
content of the word "insight" is largely the discovery that evidence you found convincing
did not test what you thought it tested.

So: **the agent's internal likelihood model says the shallow probes are fully diagnostic,
when in the world probes 0 and 1 cannot separate hypotheses 0 and 1.** The world stays
confusable; only the agent's model of it changes. When the agent runs shallow probe 1 and
sees "yes", it believes it has confirmed hypothesis 1, when in fact "yes" only narrows to
{0, 1}.

This is not a preference for confirmation and nothing rewards agreeing with oneself. It is
a single, independently motivated misspecification: the agent overestimates the
diagnosticity of its own tests. Observations are sampled from the true world and updated
through the agent's incorrect model, which is the standard way misspecification is handled.

## Predictions, written before implementing

18. **SEBUS will emerge.** Conviction at window end will exceed the pre-dose baseline at
    low dose, because over-interpreted shallow evidence inflates confidence in the
    untested hypothesis.
19. **The dose response will be non-monotonic**, rising to a peak and then falling below
    baseline, which is ALBUS's shape.
20. **Miscalibration is necessary, not merely sufficient.** The calibrated confusable arm
    already run shows no SEBUS, so the contrast between the two isolates misspecification
    as the mechanism. If SEBUS also fails here, then three distinct mechanisms have failed
    and the honest conclusion is that ALBUS's prediction has no route through precision at
    all.

## If prediction 18 also fails

Report it. Three failures across passive updating, epistemic action, and misspecified
self-knowledge would be a considerably stronger result than one, and it would say something
specific: that SEBUS, if real, is not a phenomenon of belief updating under altered
precision, and must live somewhere else entirely.
