# Amendment 8: hierarchy, learning, and whether either dissolves the fork

Written 2026-08-10, **before writing or running any of the code below.** Prior commits:
8109e7f, 860c369, d003810, ca4622e, b9a5d47, daef447, 6d4e093, 156c626 (gain arm),
8bf4906 (gain results).

## Why this arm exists

The standing objection to the consolidation results is that the model is flat and
static while REBUS is hierarchical, and that in active inference persistence does not
need a bolted-on consolidation step: it arrives through **learning**, meaning slow
updates to model parameters, while precision changes are fast state-level weightings.
On this view the four consolidation mechanisms are hand-rolled stand-ins for something
the framework already provides.

This arm builds the hierarchical model with parameter learning and asks whether the
framework's own machinery answers the question the consolidation arms raised, or
inherits it. The hypothesis, declared here: **learning is not one mechanism.** The
modeler must still choose what the learning increment is computed from, and those
choices reproduce the consolidation fork one level down. The hierarchy adds one
genuinely new route (top-down bias in what gets encoded), and that route is the most
clinically interesting thing this model family could contain, because it is the
mechanism of self-fulfilling perception.

## The model

Two levels, minimal.

- **Level 2 (context):** C in {0..5}. C = 0 true, C = 1 the maladaptive conviction.
  The stored prior is a probability vector `p2` with count mass `N0 = 20`
  (Dirichlet-mean form). Initial conviction `p2[1] = 0.8007`, matching the acting
  arm's entrenchment, so there is headroom above it.
- **Level 1 (events):** s in {0..5}. `p(s|C) = q` if s = C else `(1-q)/5`, q = 0.8.
  Context produces context-typical events, noisily.
- **Observations:** `p(o|s) = r` if o = s else `(1-r)/5`, r in {0.40, 0.70}. The
  exact marginal likelihood `m(o|C) = sum_s p(o|s) p(s|C)` is what level-2 inference
  uses; the hierarchy under exact inference reduces to the flat model with `m` as its
  effective likelihood.
- **Window:** T = 12 observations. During it, the weight on the stored log-prior is
  multiplied by (1 - d): the same relaxation mapping as always, applied at use time.
  The stored counts are untouched by dose.
- **Level-1 inference (used only by the encoding rule):** at step t,
  `prior1(s) = sum_C b_C * p(s|C)` from the current level-2 belief, and
  `posterior1(s) proportional to prior1(s)^kappa * p(o_t|s)`, kappa in {1, 3}.
  kappa = 1 is exact; kappa = 3 overweights the top-down prior, the strong-prior
  regime of Powers, Mathys and Corlett.

**Learning** adds mass E in {0, 2.5, 5, 10, 20, 40, 80} of a normalized increment
`inc` to the stored counts: `p2_new = (N0 p2 + E inc) / (N0 + E)`. The lasting
outcome IS the updated prior: lasting conviction `p2_new[1]`, lasting insight
`argmax p2_new = 0`. Four increment rules, each a defensible reading of "the agent
learns from the session":

- **L-P, posterior-driven:** `inc = b_C(T)`, the window-end context posterior.
  The analog of P-A/P-B.
- **L-E, evidence-driven:** `inc = softmax(sum_t log m(o_t|C))`, the likelihood-only
  posterior, prior excluded. The analog of P-D.
- **L-D, decay:** no increment; the stored prior decays toward uniform with
  equivalent strength `E/(N0+E)`. The analog of P-C.
- **L-H, encoding-driven:** `inc[C] proportional to sum_t posterior1(s = C)`, how
  often the agent inferred each context's typical event to have occurred. Evidence-
  driven in spirit, but the inference it counts is shaped by the top-down prior.
  This rule contains no strengthening term and is symmetric across contexts.

Grid: 4 rules x 21 doses x 7 E values x 2 r values (x 2 kappa for L-H), 20,000
trials, observation draws shared across dose, rule, E, and kappa, seed 11.

## Predictions, written before running

30. **Hierarchy alone changes nothing.** With E = 0 the lasting outcome is the
    unchanged prior at every dose: the snap-back result restated one level up, exact
    rather than statistical. And level-2 inference itself reduces to the flat model
    under `m(o|C)`, so nothing about adding a level, by itself, rescues persistence.

31. **Learning inherits the consolidation fork.** Dose spread in lasting insight is
    strictly positive under L-P, and exactly zero under L-E and L-D (paired draws
    make this exact, not approximate): the increment either contains the
    dose-dependent posterior or it does not. This is the P-A/P-D/P-C fork, renamed.
    If L-E shows a nonzero spread, that is an implementation bug or a genuine
    surprise, and the arm stops until it is diagnosed.

32. **The hierarchy's new route is encoding bias, and it self-entrenches.** Under
    L-H: (a) dose spread is strictly positive even though the rule is evidence-driven
    in form, because relaxation changes level-1 inference during the window; (b) at
    dose 0, with ambiguous observations (r = 0.40) and strong top-down weighting
    (kappa = 3), lasting conviction exceeds its starting value 0.8007: **emergent
    self-strengthening with no cost term and no gain term**, arising from the rigid
    prior explaining ambiguous events as conviction-typical and the learning rule
    then crediting the conviction; (c) the entrenchment shrinks as dose rises
    (relaxation frees encoding) and as r rises (unambiguous events resist
    reinterpretation). If no cell in the declared grid shows (b), the emergent-SEBUS
    claim is dead and is reported dead.

33. **Plasticity and relaxation are dissociable claims.** Making the learning rate
    dose-dependent (multiplier 1 + 2d, the plasticity reading of psychedelic action)
    under L-E scales how far the prior moves but cannot change the direction it
    moves in: the increment is dose-invariant by construction. Under L-P and L-H the
    direction itself changes with dose. So "the drug opens a plasticity window" and
    "the drug relaxes priors" make different predictions: magnitude change versus
    content change of the post-session belief, and neither REBUS nor the plasticity
    literature distinguishes them. Reported as the max L1 distance between the
    normalized increment at dose d and at dose 0, per rule.

## What would falsify the exercise

If L-P, L-E, and L-H turn out indistinguishable in lasting outcome across the whole
grid, then in this family the increment choice does not matter, learning genuinely
dissolves the fork rather than inheriting it, and the consolidation results of
amendments 1 to 6 lose their sting. That outcome would be reported as the headline.
