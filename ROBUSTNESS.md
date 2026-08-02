# Robustness: four consolidation mechanisms

2.69 billion simulated agents. Parameterizations declared at d003810, before the code.
Main grid: 8 reliabilities x 41 doses x 41 consolidation levels x 4 mechanisms x 50,000
trials, with observation draws shared across dose so the dose contrast is paired.

---

## 1. The finding: whether the drug matters at all depends on what consolidation acts on

Prediction 9, confirmed, and more sharply than expected. Persistent insight at full
consolidation, informative evidence:

| dose | P-A arithmetic | P-B geometric | P-C attractor | P-D memory |
|---|---|---|---|---|
| 0.00 | 0.6120 | 0.6120 | 0.9634 | 0.6120 |
| 0.50 | 0.8627 | 0.8627 | 0.9634 | 0.6120 |
| 1.00 | 0.9634 | 0.9634 | 0.9634 | 0.6120 |
| **spread across all 41 doses** | **0.3514** | **0.3514** | **0.0000** | **0.0000** |

Exactly zero, not approximately. In the two mechanisms where consolidation acts on the
**belief state reached during the window**, dose changes the lasting outcome substantially.
In the two where it acts on the **attractor** or on the **encoded evidence**, dose is
causally irrelevant to what the agent ends up believing, at every dose, at every
reliability.

Note the P-C column: 0.9634 at dose zero. Under the attractor account the best available
outcome is reached **with no drug at all**, purely by weakening the old conviction.

**The therapeutic relevance of the acute experience is not a finding of REBUS. It is a
hidden assumption about what consolidation operates on, and neither REBUS nor REBAS states
it.** That is the poster's sharpest claim and it is mechanism-independent in the sense that
it is a statement *about* the space of mechanisms.

## 2. Correction to RESULTS.md section 3: the gate is not blind

RESULTS.md claimed that no setting of `c` separates true from false insight. **That was
true only of the arithmetic mixture, and it is false in general.** Onset of each outcome as
`c` rises, at dose 0.8:

| mechanism | true insight onset | false insight onset | separation |
|---|---|---|---|
| P-A arithmetic | 0.500 | 0.600 | 0.100 |
| P-B geometric | 0.375 | 0.775 | 0.400 |
| P-C attractor | 0.175 | 0.525 | 0.350 |
| P-D memory | 0.525 | never appears | total |

**There is a safe consolidation window.** In three of four mechanisms it is wide. In P-D,
poor evidence never produces a persistent false belief at any consolidation level, because
with uninformative evidence the old conviction simply wins rather than being displaced by
noise.

The invariant that *does* survive every mechanism, every hypothesis count K in {3, 6, 10,
20}, and every window length in {4, 12, 30}: **false insight always requires more
consolidation than true insight.** In every cell of the structural sweep where both are
defined, the false onset exceeds the true onset. None reversed.

So the defensible claim is not "integration is indiscriminate." It is: **integration
admits true beliefs at a lower threshold than false ones, so there exists a window in which
it helps without hurting, and the width of that window depends on a mechanism nobody has
pinned down.**

That is a better result than the one it replaces, and it is falsifiable: it says which
measurement would settle the question.

## 3. A threshold exists in all four, with very different sharpness

Prediction 10, confirmed for existence, half right on sharpness. Width of the `c` range
covering 5 to 95 percent of the final insight rate:

| mechanism | width |
|---|---|
| P-A arithmetic | 0.200 |
| P-D memory | 0.425 |
| P-B geometric | 0.450 |
| P-C attractor | 0.625 |

P-A sharpest, as predicted. P-B smoothest, **not** as predicted; P-C is. The hard step in
the original results was the sharpest case in the family, so the earlier figure oversold
how knife-edged the transition is.

## 4. Entrenchment: the untreatable regime

Prediction 12, confirmed. Consolidation needed for 50 percent lasting insight, as the
original conviction hardens:

| gamma_0 | P-A | P-B | P-C | P-D |
|---|---|---|---|---|
| 4 | 0.475 | 0.300 | 0.000 | 0.375 |
| 8 | 0.500 | 0.475 | 0.000 | 0.750 |
| 12 | 0.525 | 0.600 | 0.100 | **unreachable** |
| 16 | 0.525 | 0.700 | 0.325 | **unreachable** |
| 24 | 0.525 | 0.800 | 0.550 | **unreachable** |

P-A barely moves, which is why the original single-mechanism result looked entrenchment
insensitive. Every other mechanism moves a great deal. Under P-D, past a conviction
strength of roughly 12 **no amount of consolidation reaches 50 percent**: the belief is
untreatable within the model, because retaining a fraction of encoded evidence can never
overcome a prior that strong.

That regime does not exist under P-A. Whether it exists in reality is an empirical question
about which mechanism is right.

---

## What this does to the poster

The headline moves up a level. It is no longer "here is how REBUS behaves when you
implement it." It is:

> Implementing REBUS requires an assumption its authors never state, four defensible
> versions of that assumption exist, and they disagree about whether the drug is necessary
> at all, whether integration can be made safe, and whether some beliefs are treatable.

Every one of those disagreements is a measurable prediction rather than a philosophical
dispute.

## Honest limits

- `c` remains a free parameter with no calibration to any clinical quantity in any of the
  four mechanisms. Thresholds are ordinal claims, not numbers to quote.
- The agent still does not act, so the confirmation-sampling route to SEBUS is still
  untested. That remains the fair test of ALBUS.
- Prediction 11 as originally written was wrong, and the earlier writeup stated its
  conclusion too strongly. Corrected above rather than quietly amended.
