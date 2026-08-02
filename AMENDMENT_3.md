# Amendment 3: an acting agent, and the fair test of ALBUS

Written 2026-08-01, **before writing or running any of the code below.** Prior commits:
8109e7f, 860c369, 2da4644, d003810.

## Why this arm exists

Every result so far comes from an agent that receives evidence rather than choosing it.
PREREGISTRATION.md section 6 flagged that as the reason the SEBUS null must be read
narrowly, and named confirmation sampling as the mechanism that could produce belief
strengthening. This arm builds it.

## The mechanism, and why it can produce SEBUS without SEBUS being assumed

Hypotheses are not equally distinguishable from one another. Some tests separate a
hypothesis from distant rivals while leaving it confounded with its nearest neighbour.

- Six hypotheses. Hypothesis 0 is **true**. Hypothesis 1 is the **maladaptive conviction**.
  They are **mutually confusable**: no shallow test separates them.
- **Shallow probes**, one per hypothesis. Shallow probe `j` tests membership in group
  `G_j`, where `G_0 = G_1 = {0, 1}` and `G_j = {j}` for `j >= 2`. So a shallow probe can
  eliminate hypotheses 2 through 5, and can confirm that the answer lies in {0, 1}, but
  can never say which.
- **One deep probe**, which separates 0 from 1 and is uninformative about everything else.

Action is selected by expected free energy, epistemic term only, so the agent samples
wherever it expects to learn most **given its current beliefs**. Softmax over the epistemic
values with policy precision `alpha`. No preferences, no reward, nothing that could smuggle
in a bias toward the maladaptive hypothesis.

**The trap is a consequence, not an assumption.** An agent confident in hypothesis 1 has
little uncertainty about the 0-versus-1 distinction, so the deep probe looks epistemically
worthless to it. Its residual uncertainty is spread over 2 through 5, so shallow probes
look valuable. It runs them, eliminates the irrelevant alternatives, and the probability
mass they held redistributes onto {0, 1} in the ratio its prior already had. **Its
confidence in the maladaptive belief rises without that belief ever being tested.**

That is confirmation bias arising in an agent with a correct model, purely from the
interaction between epistemic action selection and an uneven confusability structure. It is
also, as far as I can tell, the mechanism ALBUS needs and does not specify.

## Predictions, written before running

13. **SEBUS will emerge.** At low dose, conviction in the maladaptive hypothesis at the end
    of the window will be **above** the pre-dose baseline. Contrast this with the
    preregistered and confirmed prediction 3, where passive precision reduction produced a
    monotone decrease at every reliability. If 13 holds, the SEBUS/REBUS disagreement is a
    disagreement about **whether the agent acts**, not about precision.
14. **The dose response will be non-monotonic**: rise, peak, then fall, with a crossover
    back below baseline at intermediate to high dose. This is ALBUS's shape, emerging.
15. **The effect requires the confusability structure.** In a control condition where every
    hypothesis is separable by some shallow probe, SEBUS should vanish and the dose response
    should be monotone decreasing, matching prediction 3. **This is the control that keeps
    the arm honest.** If SEBUS appears in the control too, the effect is something duller
    than confirmation sampling and the headline is wrong.
16. **Deep-probe usage mediates it.** The rate at which the agent selects the deep probe
    should rise with dose, and the dose at which it takes off should coincide with the
    crossover in prediction 14.
17. **The size of the SEBUS effect scales with how much prior mass sits on irrelevant
    alternatives**, because that is the mass whose elimination inflates confidence. So it
    should be large at moderate `gamma_0` and vanish as `gamma_0` grows and the baseline
    saturates near 1. `gamma_0` is swept and the whole curve reported; **no single value is
    selected after the fact.**

## What would make me discard this arm

If prediction 15 fails, meaning SEBUS appears just as strongly without the confusability
structure, then the result is an artifact of epistemic action in general rather than of
confirmation sampling, and it should not be presented as a test of ALBUS.
