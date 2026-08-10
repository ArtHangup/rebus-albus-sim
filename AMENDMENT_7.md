# Amendment 7: ALBUS's own mechanism, head to head with avoidance

Written 2026-08-10, **before writing or running any of the code below.** Prior commits:
8109e7f (mapping), 860c369, d003810, ca4622e, b9a5d47, daef447, 6d4e093 (window arm),
2b83f4f (window results).

## Why this arm exists

The strongest objection to the SEBUS results so far is scope: the preregistered dose
mapping is monotone relaxation by design, and ALBUS's own proposed mechanism is a
low-dose **gain increase** on priors. Building that in produces SEBUS by construction,
which is why it was excluded. But exclusion leaves the objection standing, and it also
leaves value on the table: if both the gain account and the avoidance account can
produce SEBUS, the useful question is no longer which theory is right but **what
measurable signature separates them.** This arm implements the gain mechanism honestly,
runs it beside the avoidance mechanism, and looks for the discriminators.

## Design

One-parameter extension of the preregistered dose mapping:

    gamma(d) = gamma_0 * (1 - d) * (1 + A * d)

- `A = 0` recovers the original REBUS mapping exactly.
- `A > 1` gives a low-dose gain peak: maximum `gamma_0 * (A+1)^2 / (4A)` at
  `d* = (A-1) / (2A)`, returning to `gamma_0` at `d = 1/... ` and to full relaxation
  (gamma 0) at `d = 1`. This is the qualitative ALBUS shape: strengthen low, relax
  high, one knob controlling how strong the low-dose regime is.
- `A` swept over {0, 1, 2, 4}. If nothing measurable changes anywhere at A = 4, extend
  once to A = 8 before concluding the gain is too weak; declared here so it is not a
  post hoc choice.

Passive model: reliabilities {0.30, 0.55}, 41 doses, 20,000 paired trials, conviction
at window end versus the pre-dose baseline.

Acting model: unchanged from the costly-test arm (gamma_0 = 3.0, r = 0.85, alpha = 8,
14 steps), A x costs {0.0, 0.3, 0.5} x 41 doses, 20,000 trials. Recorded: window-end
conviction, deep-probe usage, and the lasting outcome after arithmetic consolidation
(c = 0.8, t_c = 14), with the no-session baseline 0.8007 as the comparison.

## Predictions, written before running

27. **The construction check, stated honestly in both directions.** Under gain (A > 1)
    window-end conviction at low dose exceeds its A = 0 value everywhere; that part is
    mechanical and proves nothing. The informative part is whether conviction exceeds
    the **pre-dose baseline** (literal SEBUS). Expected: yes where evidence is weak
    (passive, r = 0.30) or where the test is also costly; **not** expected in the
    acting model with a free test, because the deep probe still runs and two or three
    uses still overwhelm the boosted prior. If literal SEBUS fails to appear even with
    the gain built in and the test free, then within this family ALBUS's strengthening
    is only strengthening relative to the relaxed counterfactual, not relative to the
    person's pre-dose belief, and the theory needs to say which one it means.

28. **The mediator separates the accounts by sign.** Under gain with a free test,
    deep-probe usage at low dose falls **below** its dose-zero value: the drug
    suppresses engagement with the diagnostic test. Under avoidance (A = 0, cost > 0),
    usage never falls below its dose-zero value and rises with dose. So the sign of
    the low-dose change in diagnostic engagement is a behavioral discriminator between
    the two SEBUS accounts, and it is the kind of thing a task battery could measure.

29. **Gain and avoidance interact, and gain alone cannot entrench.** Two parts.
    (a) With both present (A >= 2, cost 0.3), the SEBUS region is larger than under
    either alone: the gain lowers the effective cost threshold. (b) Composed with
    consolidation, gain with a **free** test does not produce lasting conviction above
    the no-session baseline at any dose (the deep evidence, once gathered, wins),
    whereas gain plus cost does. If (b) holds, then even under ALBUS's own mechanism
    lasting entrenchment still requires avoidance, and the two theories converge on
    avoidance as the load-bearing quantity, which neither states. If (b) fails, gain
    alone can lock in a strengthened belief and that is the more alarming result and
    must be reported as such.

## What would falsify the exercise

If the A = 0 and A = 4 rows are indistinguishable on every recorded quantity after
the declared extension to A = 8, the gain parameterization is too weak to carry
ALBUS's claim and the arm reports that as its result rather than tuning further.
