# Gain versus avoidance: implementing ALBUS's own mechanism

Arm declared in AMENDMENT_7.md (commit 156c626) before the code existed. Predictions
27 to 29. The gain mapping `gamma(d) = gamma_0 (1-d)(1+Ad)` nests the preregistered
REBUS mapping at A = 0 and gives a low-dose gain peak for A > 1 (factor 1.125 at
A = 2, 1.5625 at A = 4). Main grid: 4 gains x 3 costs x 41 doses x 20,000 trials in
the acting model, plus the passive model at r in {0.30, 0.55}. Costs {0.1, 0.2} at
A in {0, 4} were added after seeing the main grid to resolve prediction 29a properly;
those cells are from gain_posthoc.py and are labeled post hoc below.

## Prediction 27, confirmed, and the sharpest version of it

**Even with ALBUS's mechanism built in, literal SEBUS almost never happens.** With a
free diagnostic test, window-end conviction never exceeds the pre-dose baseline at
any gain and any dose: acting model peak 0.6318 at A = 4 against baseline 0.8007;
passive model at informative evidence (r = 0.55) peak 0.7048 against 0.9983. The
agent that can freely check its belief still checks it, and two or three checks beat
a 1.56x boosted prior. Literal strengthening appeared in exactly one place without
cost: the passive model with near-uninformative evidence and the strongest gain
(r = 0.30, A = 4, SEBUS from dose 0.10 to 0.65), and there the pre-dose baseline is
0.9983, so the ceiling is almost saturated before the drug arrives.

So the family now says something sharper than before: ALBUS's strengthening claim,
implemented as stated, is strengthening **relative to the relaxed counterfactual**,
not relative to the person's pre-dose belief, except where evidence is nearly absent
or the diagnostic test is avoided. The theory does not say which comparison it means,
and the two readings come apart everywhere that matters.

## Prediction 28, confirmed: the accounts separate by sign

Change in deep-probe usage from its dose-zero value, minimum over doses in (0, 0.5]:

| account | usage at d = 0 | min in (0, 0.5] | direction |
|---|---|---|---|
| gain, A = 4, cost 0 | 0.239 | 0.200 | **dips** |
| gain, A = 2, cost 0 | 0.240 | 0.230 | dips (small) |
| avoidance, A = 0, cost 0.3 | 0.024 | 0.024 | never dips, rises |
| neutral, A = 0, cost 0 | 0.239 | 0.240 | flat |

Under the gain account the drug **suppresses** engagement with the diagnostic test at
low dose (the boosted prior sees less uncertainty, so the test looks less valuable).
Under the avoidance account engagement never falls below its sober value and rises
with dose. The sign of the low-dose change in diagnostic engagement is therefore a
behavioral discriminator between the two SEBUS accounts. At model effect sizes
(0.239 against 0.200) a two-condition comparison needs on the order of two thousand
binary observations per condition; that number is a property of this parameterization
and is quoted only to show the effect is not knife-edge.

## Prediction 29, confirmed, plus the result that revises an earlier claim

**(a) Gain amplifies avoidance.** SEBUS dose range at fixed cost, acting model:

| cost | A = 0 | A = 2 | A = 4 |
|---|---|---|---|
| 0.0 | none | none | none |
| 0.3 | 0.00 to 0.23 | 0.00 to 0.65 | 0.00 to 0.80 |
| 0.5 | 0.00 to 0.42 | 0.00 to 0.78 | 0.00 to 0.85 |

And the effective cost threshold falls: at A = 0, SEBUS needs cost above 0.2; at
A = 4 it is present at cost 0.1 (post hoc cells).

**(b) Gain alone cannot entrench.** After consolidation (c = 0.8, t_c = 14), lasting
conviction exceeds the no-session baseline at **no** dose when the test is free, at
every gain up to A = 4. Every entrenchment region in the grid requires cost > 0. So
even under ALBUS's own mechanism, lasting entrenchment runs through avoidance, and
the two theories converge on avoidance as the load-bearing quantity. Neither paper
names it.

**The revision (post hoc, from the added cells): the drug can add strengthening, but
only when gain and avoidance are both present.** At A = 4, cost 0.1, the SEBUS
region is 0.17 to 0.57: it detaches from dose zero. Conviction at dose zero is 0.60,
well below baseline, and climbs **above** baseline at moderate dose. Everywhere else
in three arms of results, peak conviction sat at dose zero and the drug only failed
to remove strengthening. This is the one regime found so far in which the drug
actively strengthens the belief, which is ALBUS as usually read. It requires the
gain mechanism and a modest test cost jointly; neither produces it alone. The
statement in ACTING_RESULTS.md ("the drug never adds strengthening") is therefore
correct for the preregistered relaxation-only mapping and does not survive the gain
extension; the writeups should carry the qualified version from now on.

## What this arm changes

The objection "you never implemented ALBUS's mechanism" is now answered with results
rather than scope notes: implemented as stated, the gain mechanism cannot strengthen
a belief against a freely run test, cannot entrench anything without avoidance, and
in combination with avoidance reproduces ALBUS's active low-dose strengthening in a
narrow interior dose window. The debate between the theories reduces to two
measurable quantities: the sign of the low-dose change in diagnostic engagement
(prediction 28), and whether strengthening ever appears without avoidance
(prediction 29b).

## Limits

- The gain form is one parameterization of "low-dose gain increase"; ALBUS describes
  hierarchical level-dependence this flat model cannot express.
- The post hoc cells (costs 0.1, 0.2) were run after the main grid and are labeled;
  the interior-window result should be treated as post hoc until re-run under a
  declared grid.
- All prior limits carry over: free parameters, one test, one belief, static world,
  belief dynamics only.

## Reproduce

```bash
.venv/bin/python gain.py && .venv/bin/python gain_posthoc.py && .venv/bin/python figure_gain.py
```
