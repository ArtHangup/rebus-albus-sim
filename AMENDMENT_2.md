# Amendment 2: four parameterizations of consolidation

Written 2026-07-31, **before writing or running any of the code below.** Prior commits:
8109e7f (original mapping), 860c369 (consolidation arm), 2da4644 (arm 3 results).

## Why

RESULTS.md claims a consolidation threshold near 0.5 and, more importantly, that the
threshold is *shared* between true and false insight. The threshold value is obviously an
artifact of the arithmetic-mixture parameterization I happened to pick. The question is
which claims survive a change of mechanism.

So: four mechanisms, each a defensible reading of what "the revision sticks" could mean,
each declared here before implementation.

## The four

Let `u` be the one-hot on the maladaptive hypothesis, `p_orig = softmax(gamma_0 * u)` the
pre-dose conviction, `b` the belief reached at the end of the window, and `cum_ll` the
accumulated log likelihood of the evidence encountered during the window.

**P-A, arithmetic mixture** (the original, kept for comparison). Consolidation blends the
old conviction with the new belief.

    p_after = (1 - c) * p_orig  +  c * b

**P-B, geometric mixture** (log-linear pooling). The same blend performed in log space,
which is the natural operation if the two are treated as independent sources of evidence
rather than as competing hypotheses.

    log p_after  =  (1 - c) * log p_orig  +  c * log b     (then normalize)

**P-C, attractor weakening.** Consolidation does not install a new belief. It permanently
weakens the old one, and the outcome is recomputed from the evidence against the weakened
attractor.

    log p_after  =  gamma_0 * (1 - c) * u  +  lambda * cum_ll

**P-D, memory trace.** Consolidation is how much of what you *learned* you retain. The
attractor returns at full strength and competes against a fraction of the encoded evidence.

    log p_after  =  gamma_0 * u  +  c * lambda * cum_ll

P-A and P-B act on **the belief state reached during the window**. P-C and P-D act on
**the evidence, or on the attractor**, and never look at `b` at all.

## Predictions, written before running

9. **The causal relevance of the acute experience is parameterization-dependent, and this
   is the important one.** Dose enters the terminal outcome only through `b`. So P-A and
   P-B should carry a dose effect, and **P-C and P-D should show none at all in arm 1**,
   because dose never touches `cum_ll` or `gamma_0`. If this holds, then whether the acute
   experience matters for the outcome depends entirely on an assumption about what
   consolidation operates on, and **neither REBUS nor REBAS states that assumption.**
10. **A threshold in `c` exists in all four**, since all four interpolate between "old
    conviction wins" and "new information wins." Its location and sharpness should differ.
    I expect P-A sharpest and P-B smoothest.
11. **The threshold is shared between true and false insight in all four.** No mechanism
    here inspects whether the belief is correct, so none can preferentially pass true ones.
    This is the claim from RESULTS.md section 3 under test, and it is the one I most expect
    to survive.
12. **Entrenchment (`gamma_0`) should shift the threshold more in P-C and P-D than in P-A**,
    because in those two the attractor competes on the same log scale as the evidence,
    whereas in P-A it saturates near probability 1 and the threshold asymptotes to 0.5.

## Scale

Vectorized across trials, so the observation counts for a given reliability are drawn once
and reused across every dose, `c`, and parameterization. That makes the dose comparison
paired rather than independent, which removes sampling noise from the contrast that
matters.

Target: 50,000 trials per cell, 41 dose values, 41 consolidation values, 8 reliabilities,
4 parameterizations, plus separate entrenchment, hypothesis-count, and window-length
robustness sweeps. Roughly 10^9 simulated agents in total.
