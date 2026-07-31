# Results

Run 2026-07-31. Mapping preregistered at 8109e7f, consolidation arm declared at 860c369,
both before the code that produced these numbers existed.

---

## 1. REBUS as literally stated produces no lasting change at all

At reliability 0.55, dose drives acute insight from 0.684 to 0.963 and collapses conviction
in the maladaptive belief from 0.318 to 0.012. Measured after the window, insight is
**flat at roughly 0.68 across every dose**.

This is structural, not numerical. If dose enters only through prior precision, and that
precision returns to baseline afterwards, dose cannot appear in the terminal belief. The
acute experience is real and it evaporates completely.

**Something must make the revision stick. That something is not in REBUS.**

## 2. Consolidation is a gate, dose is a gain

Adding a consolidation parameter `c`, where the post-window prior is
`(1-c) * original + c * window_belief`:

| c | d=0.0 | d=0.4 | d=0.8 | d=1.0 |
|---|---|---|---|---|
| 0.00 to 0.45 | **0.000** | **0.000** | **0.000** | **0.000** |
| 0.50 | 0.090 | 0.352 | 0.480 | 0.545 |
| 0.55 | 0.505 | 0.785 | 0.887 | 0.895 |
| 0.80 | 0.698 | 0.863 | 0.935 | 0.965 |
| 1.00 | 0.682 | 0.897 | 0.945 | 0.990 |

Below `c ≈ 0.5` the lasting insight rate is **exactly zero at every dose**. No amount of
prior relaxation helps. Above the threshold, dose determines how much you get.

That is the cleanest statement the model makes: **integration is necessary, dose is not
sufficient, and the two are not interchangeable.**

## 3. The gate does not check whether the belief is true

At reliability 0.30, where the evidence arriving during the window is close to
uninformative, the same threshold passes false beliefs:

| c | d=0.4 | d=0.8 | d=1.0 |
|---|---|---|---|
| ≤ 0.50 | 0.000 | 0.000 | 0.000 |
| 0.70 | 0.000 | 0.058 | 0.145 |
| 0.90 | 0.003 | 0.140 | 0.247 |

Up to a quarter of agents end up permanently holding a belief the world does not support,
and they get there through the identical mechanism that produces genuine insight, at the
identical threshold.

**The mechanism that makes this work is the mechanism that makes it dangerous, and no
setting of `c` separates them.** What separates them is the quality of the evidence
present during the window, which is the only lever in the model that discriminates true
from false. That is a derived argument for set and setting rather than an asserted one.

## 4. SEBUS does not emerge (preregistered prediction 3, confirmed)

Conviction in the maladaptive belief at window end, against a pre-dose value of 0.9983:

| dose | r=0.30 | r=0.55 | r=0.85 |
|---|---|---|---|
| 0.0 | 0.9916 | 0.2968 | 0.0000 |
| 0.5 | 0.7544 | 0.0720 | 0.0000 |
| 1.0 | 0.1229 | 0.0123 | 0.0000 |

Monotonically decreasing at every reliability. No dose at which conviction rises above
baseline. **Passive precision reduction cannot produce belief strengthening.**

Read this narrowly, as the preregistration requires. It does not show ALBUS is wrong. It
shows ALBUS needs a mechanism beyond precision reduction, and that mechanism is not
specified in the paper. The most plausible candidate is confirmation sampling, which
requires an agent that chooses what evidence to gather. That is the named follow-up and it
is the fair test.

---

## Predictions that failed

Reported because they were preregistered.

- **Prediction 1 (insight is a ridge in dose by reliability): FAILED.** There is no ridge
  because there is no persistence at all in the pure arm. The failure is what produced
  result 1.
- **Prediction 5 (arm 2 shows an interior optimum): FAILED.** Adding sensory degradation
  makes dose monotonically harmful, never humped, because there is no persisting benefit
  for the cost to trade against.
- **Prediction 7 (threshold rises with entrenchment): directionally right, magnitude
  small.** The threshold moves from 0.50 to 0.55 as the original conviction goes from
  0.916 to 1.0000. The algebra explains why it barely moves: once the original conviction
  approaches certainty the threshold asymptotes to 0.5. Do not oversell this one.

## Limitations to state on the poster

- **The agent does not act.** It receives evidence rather than choosing what to sample.
  This is the reason the SEBUS result must be read narrowly.
- **`c` is a free parameter** with no calibration to any clinical quantity. The threshold
  at 0.5 is a property of the mixture parameterization, not a measured number. What
  survives reparameterization is that a threshold *exists* and that it is shared between
  true and false insight, not its value.
- **The world is static.** Transitions are the identity, so this models belief revision
  and not a changing environment.
- One empirical result sits awkwardly with all of this: Allohverdi et al. (2025, bioRxiv)
  fit a Hierarchical Gaussian Filter to EEG and found ketamine reduced sensory precision
  while **psilocybin showed no significant effect**. That belongs on the poster.

## Reproduce

```bash
.venv/bin/python sweep.py && .venv/bin/python consolidation.py && .venv/bin/python figure.py
```

## Known cosmetic issue

Panel B of `figure_main.png` has misaligned x tick positions from the `imshow` extent.
The numbers are correct; the axis needs fixing before the poster.
