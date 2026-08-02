# The acting agent: four mechanisms, three failures, and where SEBUS actually lives

Arms declared in AMENDMENT_3, _4 and _5 before each was implemented. Roughly 100 million
agent-trajectories at 14 decision steps each.

## The arc

| # | Mechanism | SEBUS? | Preregistered as |
|---|---|---|---|
| 1 | Passive precision reduction | **no** | prediction 3, confirmed |
| 2 | Epistemic action, correct model | **no** | prediction 13, **failed** |
| 3 | Epistemic action, misspecified self-knowledge | **no** | prediction 18, **failed** |
| 4 | Epistemic action + a costly diagnostic test | **yes** | prediction 21, confirmed |

## Why the first three failed, and it is the same reason each time

In every one of them a genuinely diagnostic test exists and the agent's epistemic drive
prices it correctly. It runs that test 14 to 25 percent of the time, and two or three uses
carry enough evidence to overwhelm the maladaptive belief. Rigid priors do not stop it.
Misspecification about the *other* tests does not stop it. A Bayesian agent with a working
epistemic appetite finds the question that matters.

Neither failure was an inert model. The confusability structure retarded revision by a
factor of six (conviction 0.368 against 0.057 in the separable control). Misspecification
cut accuracy from 0.654 to 0.416. Both did real damage. Neither produced strengthening.

## Where SEBUS actually lives

Price the diagnostic test and it appears. Conviction at window end against a pre-dose
baseline of 0.8007, entrenchment 3.0:

| cost of the test | peak conviction | delta vs baseline | dose range showing SEBUS |
|---|---|---|---|
| 0.00 | 0.3676 | -0.4331 | none |
| 0.10 | 0.6034 | -0.1973 | none |
| 0.20 | 0.7948 | -0.0059 | none |
| **0.30** | **0.8897** | **+0.0891** | 0.00 to 0.23 |
| 0.50 | 0.9357 | +0.1351 | 0.00 to 0.42 |
| 0.80 | 0.9442 | +0.1435 | 0.00 to 0.50 |
| 1.20 | 0.9455 | +0.1448 | 0.00 to 0.50 |

There is a threshold between 0.2 and 0.3, and above it the agent ends the window **more**
convinced of the untested belief than it began.

**So SEBUS is not a precision phenomenon. It is an avoidance phenomenon.** Belief
strengthening requires that the agent was already declining to run the test that would
disconfirm it. Precision has nothing to do with it, which is why three precision-based
mechanisms could not produce it.

## The mediator, confirmed (prediction 23)

Deep-probe usage against dose. This is the claim that makes the account mechanistic:

| dose | cost 0.0 | cost 0.2 | cost 0.3 | cost 1.2 |
|---|---|---|---|---|
| 0.00 | 0.239 | 0.056 | 0.023 | 0.000 |
| 0.50 | 0.247 | 0.090 | 0.044 | 0.000 |
| 0.88 | 0.224 | 0.097 | 0.056 | 0.000 |

With no cost, usage is flat and slightly falling. With a cost, **usage rises with dose**:
relaxing the prior raises uncertainty about the distinction that matters, which raises the
epistemic value of the test, which pushes it back above the cost.

**Prior relaxation causes the agent to face a test it was avoiding.** That is a
mechanistic account of what the drug does, and neither REBUS nor ALBUS states it.

At cost 1.2 usage is 0.000 at every dose. **Above a cost ceiling the drug cannot help at
all**, because no amount of prior relaxation makes the test worth running.

## Prediction 22, half right, stated precisely

The SEBUS-to-REBUS crossover exists and **moves to higher dose as cost rises**, from 0.23
at cost 0.3 to 0.50 at cost 0.8. That is ALBUS's structure: a low-dose regime of
strengthened belief giving way to a high-dose regime of relaxation.

But the peak conviction is always at dose **zero**, so the curve within the SEBUS region is
flat-to-declining rather than rising. The drug never *adds* strengthening. It fails to
remove pre-existing strengthening until the dose is high enough. That distinction matters
and should not be smoothed over: ALBUS as usually read implies the drug actively
strengthens beliefs at low doses, and nothing here does that.

## What to claim, and what not to

**Claim:** SEBUS requires avoidance of a diagnostic test, not altered precision. Three
precision-based mechanisms fail to produce it and one avoidance-based mechanism does. The
therapeutic action of prior relaxation is to make an avoided test worth running, and above
a cost ceiling that mechanism is unavailable.

**Do not claim** that ALBUS is wrong. Claim that its prediction has no route through
precision, that it needs an avoidance term, and that the term is absent from the paper.

## Limits

- The cost is a free parameter and the threshold near 0.25 is a property of this
  epistemic-value scale, not a measured quantity. What survives is the existence of a
  threshold and a ceiling, and the direction of the mediator.
- One diagnostic test, one maladaptive belief, a static world.
- All of this is belief dynamics. Nothing here bears on phenomenal experience, and the
  poster must say so.
