# Preregistration: REBUS as stated, and whether ALBUS emerges from it

Written 2026-07-31, **before any sweep was run.** Committed to git before `sweep.py`
produced output. Nothing below was chosen after seeing a result.

The point of this document is that whoever picks the mapping from theory to parameters can
make either theory win. So the mapping is fixed here, in advance, and derived from what
each paper actually says rather than from what produces a nice figure.

---

## 1. The two claims being tested

**REBUS** (Carhart-Harris and Friston 2019, *Pharmacol Rev* 71(3):316-344). Psychedelics
reduce the precision of high-level priors, which permits belief revision that rigid priors
would otherwise prevent.

**ALBUS** (Safron, Juliani, Reggente, Klimaj and Johnson 2025, *Neuroscience of
Consciousness* 2025(1):niae038). At low to moderate 5-HT2A agonism, beliefs are
*strengthened* (SEBUS), with REBUS-style relaxation appearing only at higher doses. The
predicted dose-response is therefore non-monotonic and opposite-signed at low doses.

**FIBUS** (McGovern, Grimmer, Doss, Hutchinson, Timmermann, Lyon, Corlett and Laukkonen
2024, *Communications Psychology*). Relaxation can install *false* beliefs, not only
correct ones. This is measured here as a distinct outcome rather than as failure.

**REBAS** (Zeifman et al. 2025, *Scientific Reports* 15:3651). Whether revised beliefs
persist after the acute window closes.

---

## 2. The mapping, fixed in advance

### Generative model

A single hidden state factor, `context`, with K = 6 mutually exclusive hypotheses about
how the world is.

- `context = 0` is **true**.
- `context = 1` is the agent's **maladaptive prior conviction**, the belief it arrives
  holding and that the world does not support.
- `context = 2..5` are **alternative hypotheses**, available but unsupported.

Observations are drawn from a categorical likelihood with reliability `r`:

    p(obs = j | context = i) = r           if i == j
                             = (1-r)/(K-1) if i != j

`r` is the **setting**: how informative the evidence arriving during the window is.
`r = 1/K` is pure noise, `r = 1` is perfectly diagnostic. The world is static; the
transition model is the identity. This is deliberate. REBUS is a claim about belief
revision, not about world dynamics.

### Belief updating

The agent's belief after t observations is the precision-weighted combination of prior and
accumulated evidence:

    log b_t(i)  =  gamma * log D(i)  +  lambda * sum_{tau <= t} log p(o_tau | i)

where `D` is peaked on `context = 1`, `gamma` is **prior precision**, and `lambda` is
**sensory precision**. This is the same two-parameter structure Rajpal et al. (2022,
*NeuroImage* 263:119624) fit to MEG data, which is the closest published precedent, and it
is the formulation REBUS is stated in.

### The dose mapping (this is the load-bearing choice)

**Dose reduces prior precision, monotonically, and does nothing else:**

    gamma(d) = gamma_0 * (1 - d),  d in [0, 1]

At `d = 0` the prior is fully rigid. At `d = 1` the prior is uniform and the agent follows
the evidence.

**This mapping deliberately contains no route to SEBUS.** There is no level-dependence, no
sign flip, no low-dose strengthening term. That is the whole point. ALBUS's low-dose
prediction is not built in, so if a strengthening effect appears it will have emerged from
the dynamics, and if it does not appear that is evidence that precision reduction alone
cannot produce it.

### The window

`T = 40` timesteps total. Relaxation applies for the first `W` steps, then `gamma` returns
to `gamma_0` for the remainder. Evidence accumulated during the window persists, so
whether a revised belief survives the prior snapping back is the REBAS measurement.

### Two arms

- **Arm 1, pure REBUS.** `lambda` held constant across dose. This is REBUS as literally
  stated.
- **Arm 2, sensory disruption.** `lambda` also falls with dose, reflecting the
  uncontroversial fact that high doses degrade sensory processing. This is an *additional*
  assumption not contained in REBUS, so it is run separately and reported separately
  rather than folded in.

---

## 3. Outcomes, defined before running

Classified by the agent's terminal MAP belief:

| Outcome | Terminal belief | Reading |
|---|---|---|
| **Insight** | 0 | reached the true hypothesis |
| **No change** | 1 | still holds the maladaptive conviction |
| **False insight** | 2 to 5 | revised, but onto something unsupported (the FIBUS outcome) |

Plus two continuous measures:

- **SEBUS delta**: `b(1)` at the end of the window minus `b(1)` at t = 0. ALBUS predicts
  this is **positive at low dose**. REBUS predicts it is non-positive and monotonically
  decreasing.
- **Persistence**: whether the terminal belief at `T` equals the belief at the end of the
  window `W`, which is the REBAS quantity.

---

## 4. Predictions, written before seeing any output

1. **Insight requires both.** Neither dose alone nor reliable evidence alone suffices. The
   insight region is a ridge in the dose-by-reliability plane, not a slope. **This is the
   claim that "set and setting" is a mathematical necessity rather than clinical folklore,
   and it is the poster's headline if it holds.**
2. **False insight rises with dose when reliability is low.** Flattening the prior while
   evidence is uninformative should move the agent off its conviction and onto noise.
3. **SEBUS will not emerge.** Under this mapping I expect the SEBUS delta to be
   non-positive at every dose. **Stated plainly in advance so it cannot be claimed as a
   discovery afterward:** if this holds, the finding is not that ALBUS is wrong, it is that
   ALBUS requires a mechanism beyond precision reduction, and that mechanism is not
   specified in the paper.
4. **Persistence falls as dose rises**, because a belief reached under a flat prior has to
   survive that prior returning.
5. **Arm 2 will show a genuine interior optimum**, with the best outcomes at moderate
   rather than maximal dose, because sensory degradation eventually costs more than prior
   relaxation buys.

---

## 5. What would falsify the exercise

If the insight region turns out to be a monotone slope in dose with no dependence on
reliability, then prediction 1 fails and the model is reproducing the trivial result that a
flatter prior updates faster. That would be a negative outcome worth reporting rather than
a bug, and it would mean this apparatus does not support the set-and-setting argument.

---

## 6. Known limitation, stated up front

The agent does not act. It receives evidence rather than choosing what to sample. That
matters because the most plausible route to SEBUS is **confirmation sampling**: a rigid
belief steering the agent toward evidence that supports it, with slight relaxation
increasing exploration without yet breaking the bias. That mechanism cannot appear here.

So prediction 3 should be read narrowly. It tests whether **passive** precision reduction
produces SEBUS. It does not test whether active inference with epistemic action does. That
is the named follow-up, and it is the fair test of ALBUS. Any claim about ALBUS made from
this model alone must carry that qualification.
