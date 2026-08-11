# Hierarchy and learning: the fork survives, and rigidity finds a third defense

Arm declared in AMENDMENT_8.md (commit ab55a19) before the code existed. Predictions
30 to 33. Two-level model (context above events above observations), persistence
through Dirichlet-mean learning on the stored context prior, precision applied at use
time only. Grid: 4 learning rules x 21 doses x 7 learning amounts x 2 reliabilities
(x 2 top-down weights for the encoding rule), 20,000 paired trials.

## Prediction 30, confirmed

With no learning the lasting outcome is the unchanged prior at every dose, and level-2
inference reduces exactly to the flat model under the effective likelihood m(o|C).
Adding a level, by itself, rescues nothing. The snap-back result is not an artifact of
flatness.

## Prediction 31, confirmed: learning inherits the consolidation fork

Dose spread in lasting insight at learning amount E = 20:

| rule | increment computed from | spread, r = 0.40 | spread, r = 0.70 |
|---|---|---|---|
| L-P posterior-driven | window-end context posterior | 0.2141 | 0.0456 |
| L-E evidence-driven | likelihood-only posterior | **0.0000** | **0.0000** |
| L-D decay | nothing (prior decays) | **0.0000** | **0.0000** |
| L-H encoding-driven | inferred level-1 events | 0.0000 to 0.1736 | 0.1497 to 0.6587 |

The zeros are exact (paired draws), not approximate. Whether the drug matters for the
lasting outcome depends entirely on whether the learning increment contains the
dose-dependent posterior, which is the P-A / P-D / P-C fork restated in the
framework's own vocabulary. "Active inference already provides persistence through
learning" is true and changes nothing: the modeler still chooses what the increment
is computed from, and the theory still does not say.

One structural echo, noted post hoc: the consolidation gate reappears as a
pseudo-count ratio. At r = 0.70, kappa = 3, dose 0, lasting insight jumps from 0.000
at E = 20 to 0.599 at E = 40: the old count mass N0 must be outweighed before
anything crosses, which is the gate of RESULTS.md section 2 wearing Dirichlet
clothing.

## Prediction 32: (a) and (c) confirmed, (b) failed and reported dead

**(a)** The encoding rule is dose-relevant despite being evidence-driven in form
(spreads above), because relaxation changes what the level-1 inference makes of each
ambiguous observation, which changes what the learning rule counts. The hierarchy
adds a genuine second route from dose to lasting outcome: not what is concluded, but
what is encoded.

**(b) There is no emergent self-strengthening.** In no cell of the declared grid
does lasting conviction exceed its starting value 0.8007. The closest approach is
0.799. The falsifier in the amendment fires: emergent SEBUS through biased encoding
is dead in this family, and with it the last candidate route to strengthening that
is not assumed outright. Across all four arms, the standing result is now: beliefs
strengthen only through avoidance (emergent) or through gain plus avoidance
(assumed plus emergent); every other mechanism tried leaves conviction at or below
its starting point.

**What appeared instead is self-sealing, which is arguably the better result.**
Lasting conviction at dose 0, as learning amount E grows 32-fold:

| world | top-down weight | E = 2.5 | E = 10 | E = 40 | E = 80 |
|---|---|---|---|---|---|
| ambiguous (r = 0.40) | kappa = 1 | 0.765 | 0.693 | 0.585 | 0.542 |
| ambiguous (r = 0.40) | **kappa = 3** | **0.799** | **0.797** | **0.793** | **0.791** |
| clear (r = 0.70) | kappa = 3 | 0.745 | 0.635 | 0.469 | 0.403 |

With ambiguous evidence and strong top-down weighting, the conviction does not grow;
it **freezes**. A 32-fold increase in learning moves it by 0.008, and lasting insight
is 0.000 at every learning amount. The mechanism is visible in the increment: the
rigid prior explains ambiguous events as conviction-typical, the learning rule counts
those explanations as evidence, and the prior launders itself back into the counts.
Learning is not blocked; it is captured. Dose breaks the loop from the perception
side: at full relaxation the same rule, same world, and same learning amount reach
insight 0.174 (r = 0.40) and 0.659 (r = 0.70, E = 20). **(c)** confirmed: the
entrenchment-adjacent behavior shrinks with dose and with evidence clarity.

This is a third self-protection mechanism for rigid beliefs, joining the other two:
avoidance protects through action (do not run the test), capture protects through
interpretation (ambiguity is read as confirmation), gain protects through weighting
(the prior counts more). They are dissociable: capture requires no cost and no gain
term, only hierarchy, ambiguity, and top-down perception. And the drug's role
differs again: under avoidance it reprices the test; under capture it unfreezes the
encoding. Labeled post hoc: the self-sealing pattern was not among the declared
predictions, though it lives in the cells the amendment declared.

## Prediction 33, confirmed: plasticity scales, relaxation redirects

Max L1 change in the normalized learning increment across dose, r = 0.40:

| rule | direction shift |
|---|---|
| L-E evidence-driven | **0.0000** |
| L-P posterior-driven | 0.7179 |
| L-H encoding-driven (kappa = 3) | 1.3614 |

Under evidence-driven learning, a dose-dependent learning rate (the plasticity
reading of psychedelic action) can only move the belief further along a fixed line:
the destination is dose-invariant by construction. Content change requires dose to
enter through a posterior, either at the top (L-P) or in perception (L-H). So "the
drug opens a plasticity window" and "the drug relaxes priors" are empirically
different claims: one predicts bigger belief changes, the other predicts different
ones, and the literature that invokes both does not distinguish them.

## What this arm changes

The "active inference already has the answer" objection now has a quantitative reply:
the framework's own persistence mechanism inherits the fork (exact zeros against
positive spreads), the hierarchy's genuinely new contribution is an encoding route
that produces self-sealing rather than self-strengthening, and the plasticity and
relaxation readings of drug action are dissociable. Nothing about going hierarchical
made the unstated assumptions go away; it added two more (the increment source and
the dose-dependence of the learning rate).

## Limits

- One hierarchy depth, hand-set q and kappa, learning on the context prior only (not
  on the likelihoods), no action. The encoding result should be checked under
  likelihood learning, where capture might compound across sessions.
- The self-sealing plateau is a property of this increment normalization; the ordinal
  claim (kappa raises the plateau and flattens its E-dependence) is what should
  travel, not the 0.79.
- All prior limits carry over.

## Reproduce

```bash
.venv/bin/python hierarchy.py && .venv/bin/python figure_hierarchy.py
```
