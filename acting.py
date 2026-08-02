"""Acting agent: epistemic action selection over probes of unequal diagnosticity.

Design and predictions 13-17 declared in AMENDMENT_3.md before this file existed.

Action is selected by expected free energy, epistemic term only. There are no
preferences and no reward, so nothing biases the agent toward the maladaptive
hypothesis. Any confirmation dynamics have to come from the interaction between
epistemic value and the confusability structure.

Batched across trials: every agent in a batch runs its own trajectory, but the
epistemic values for all of them are computed in one tensor operation.
"""

import numpy as np

K = 6
TRUE = 0
MALADAPTIVE = 1


def probe_set(r, confusable=True, k=K):
    """Stack of likelihoods, shape (n_probes, 2 outcomes, k states).

    Shallow probe j tests membership in G_j. With confusable=True,
    G_0 = G_1 = {0,1}, so no shallow probe separates the true hypothesis from
    the maladaptive one. With confusable=False (the prediction-15 control),
    G_j = {j} and every hypothesis is separable.

    The last probe is the deep one: it separates 0 from 1 and says nothing
    about the rest.
    """
    rows = []
    for j in range(k):
        if confusable and j in (TRUE, MALADAPTIVE):
            members = {TRUE, MALADAPTIVE}
        else:
            members = {j}
        p_yes = np.where([s in members for s in range(k)], r, 1.0 - r)
        rows.append(np.stack([p_yes, 1.0 - p_yes]))

    deep = np.full(k, 0.5)
    deep[MALADAPTIVE] = r
    deep[TRUE] = 1.0 - r
    rows.append(np.stack([deep, 1.0 - deep]))
    return np.stack(rows)


def epistemic_values(b, probes):
    """E_o[ KL(posterior(s|o) || b) ] per trial per probe. b is (N, k)."""
    joint = probes[None, :, :, :] * b[:, None, None, :]      # (N, P, 2, k)
    p_o = joint.sum(axis=-1)                                  # (N, P, 2)
    post = joint / np.maximum(p_o[..., None], 1e-300)
    ratio = np.log(np.maximum(post, 1e-300)) - np.log(
        np.maximum(b[:, None, None, :], 1e-300))
    return (p_o * (post * ratio).sum(axis=-1)).sum(axis=-1)   # (N, P)


def run_batch(dose, r, rng, n, gamma_0=3.0, steps=14, alpha=8.0,
              confusable=True, k=K, miscalibrated=False, deep_cost=0.0):
    """Returns (final beliefs (n,k), deep-probe usage rate per trial (n,)).

    With miscalibrated=True the world stays confusable but the agent's internal
    model believes every shallow probe is fully diagnostic. Observations are
    sampled from the true world and updated through the agent's wrong model.
    """
    probes = probe_set(r, confusable=confusable, k=k)        # the world
    model = probe_set(r, confusable=not miscalibrated and confusable, k=k) \
        if miscalibrated else probes                          # what the agent believes
    n_probes = probes.shape[0]
    deep_idx = n_probes - 1

    u = np.zeros(k)
    u[MALADAPTIVE] = 1.0
    logits = gamma_0 * (1.0 - dose) * u
    b = np.exp(logits - logits.max())
    b = np.tile(b / b.sum(), (n, 1))

    deep = np.zeros(n)
    idx = np.arange(n)
    for _ in range(steps):
        ev = epistemic_values(b, model)
        ev[:, deep_idx] -= deep_cost   # pragmatic cost of the diagnostic test
        w = np.exp(alpha * (ev - ev.max(axis=1, keepdims=True)))
        w /= w.sum(axis=1, keepdims=True)
        choice = (w.cumsum(axis=1) < rng.random((n, 1))).sum(axis=1)
        choice = np.minimum(choice, n_probes - 1)
        deep += (choice == deep_idx)

        a_world = probes[choice]                              # (n, 2, k)
        a_model = model[choice]
        obs = (rng.random(n) >= a_world[:, 0, TRUE]).astype(int)   # 0 = "yes"
        b = b * a_model[idx, obs, :]
        b /= b.sum(axis=1, keepdims=True)
    return b, deep / steps


def baseline_conviction(gamma_0, k=K):
    """Pre-dose conviction: what the agent believed before anything happened."""
    return float(np.exp(gamma_0) / (np.exp(gamma_0) + (k - 1)))
