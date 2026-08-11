# Amendment 10: the ratchet. Capture plus avoidance across sessions

Written 2026-08-10, **before writing or running any of the code below.** Prior
commits: 8109e7f through 3615dd2 (sessions arm declared), fcba4f9 (sessions
results).

## Why this arm exists

Every arm so far has ended the same way for entrenchment: nothing strengthens a
belief over time. The sessions arm explained why: its world keeps volunteering
disconfirming evidence, and a passive perceiver cannot refuse it, only distort it,
and distortion leaks. The acting arms identified the one mechanism that can refuse
evidence outright: avoidance. But the acting arms were single-session.

This arm composes them: an acting agent with a costly diagnostic test, whose
learning increment passes through capture-weighted interpretation, run across
repeated sessions with an evolving stored prior. The hypothesized mechanism is a
ratchet with three teeth: (1) with the deep test priced out, the chosen evidence
stream contains no information separating the true hypothesis from the conviction,
so within-session shallow sampling inflates conviction (established, ACTING_RESULTS);
(2) learning writes the inflated belief into the stored prior, so the next session
starts more convinced (the window arm's below-crossover entrenchment, now
compounding); (3) higher stored conviction means less felt uncertainty, so the deep
test looks even less worth its cost, and usage falls session over session. Each
tooth is already demonstrated in isolation. The question is whether the loop closes.

## Design

The acting model of AMENDMENT_3/5 unchanged in its within-session mechanics: six
hypotheses, shallow probes with the confusable structure (no shallow probe separates
hypothesis 0 from 1), one deep probe, epistemic action selection with softmax
alpha = 8, cost subtracted from the deep probe's value, probe reliability r = 0.85,
14 decision steps per session, relaxation w = 1 - d applied to the stored log-prior
at use time.

The learning layer follows AMENDMENT_8/9: stored prior p2 per trial, count mass
N0 = 20, starting conviction 0.8007, learning amount E = 10, both mass variants
(fixed primary, accumulating secondary). The increment is the capture-weighted
stepwise interpretation: at each step, q_t(i) proportional to
b_{t-1}(i)^kappa * p(o_t | i, a_t), summed over the session and normalized,
kappa in {1, 3}. Belief-level inference within the session remains exact, as in
AMENDMENT_8. At kappa = 3 even a deep-probe outcome can be explained away by a
strong enough prior, which is what "the test must have been wrong" means.

Protocols, 10,000 trials, seed 11:

1. **Natural history:** dose 0 for 40 sessions; costs {0.0, 0.3, 0.8}; kappa
   {1, 3}; both mass variants. Track stored conviction, insight fraction, and
   deep-probe usage per session.
2. **Treatment:** after j in {5, 20} untreated sessions at cost {0.3, 0.8, 1.2},
   dosed sessions at d in {0.2, 0.6, 1.0} up to 40, kappa = 3, fixed mass primary
   (accumulating at cost 0.3, j = 20 as the variant check). Course = sessions to
   insight fraction 0.5, or never.

## Predictions, written before running

38. **Compounding entrenchment finally appears.** At dose 0 with cost 0.3 and
    above, stored conviction climbs session over session, ending above its starting
    value by more than 0.02 at session 40 (clear of Monte Carlo error), at both
    kappa values, and insight never arrives. The mediator closes the loop: deep
    usage declines across sessions as conviction climbs. This would be the first
    strengthening-over-time in the whole family, and it requires no gain term:
    avoidance starves the evidence stream while shallow inflation plus learning
    feed the prior. If conviction instead plateaus or erodes, the ratchet does not
    close and the headline dies; report which tooth failed (inflation absent,
    learning leak, or usage not falling).

39. **The within-session crossover becomes the multi-session treatment boundary,
    and subthreshold dosing is actively harmful.** Treatment converges only at
    doses above the acting arm's SEBUS-to-REBUS crossover for that cost (0.23 at
    cost 0.3, 0.50 at cost 0.8): so d = 0.2 fails at both costs, d = 0.6 and 1.0
    succeed at cost 0.3 and 0.8, and at cost 1.2 (deep usage 0.000 at every dose)
    no dose converges: the first genuinely untreatable regime produced by dynamics
    rather than by parameter assumption. Sharper: below-crossover treatment
    sessions consolidate inflated beliefs, so sustained d = 0.2 leaves conviction
    HIGHER than no treatment at all at the same horizon. If low doses merely slow
    recovery rather than worsening, the "harmful" half dies; report which.

40. **Chronicity is real in both mass variants.** Under the ratchet, waiting makes
    treatment harder even at fixed mass (course length at j = 20 exceeds j = 5 in
    every treatable cell), reversing the sessions arm's fixed-mass finding that
    time heals. The reversal quantifies what the benign-world assumption was doing:
    same learning machinery, opposite chronicity conclusion, and the difference is
    who chooses the evidence.

41. **Avoidance is load-bearing; capture is an amplifier.** At cost 0 the ratchet
    does not form at either kappa: the deep probe runs freely, truth enters, and
    recovery completes within roughly ten sessions, as in the sessions arm. At
    cost 0.3 the climb is faster at kappa = 3 than kappa = 1. If a ratchet forms
    at cost 0 under kappa = 3, capture alone can close the loop and the claim
    inverts; report it.

## What would falsify the exercise

If prediction 38 fails at every cost and kappa, the composition adds nothing over
its parts and this arm reports that null as its result. Predictions 39 and 40 are
only meaningful if 38 holds in at least one cell; if it holds nowhere, they are
reported as vacuous rather than confirmed.
