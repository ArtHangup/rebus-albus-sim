"""REBUS as stated: dose reduces prior precision, and nothing else.

The mapping is fixed in PREREGISTRATION.md and must not be changed here without a
new commit to that file. See section 2 of the prereg for why that matters.

Belief updating is precision-weighted combination of a rigid prior with accumulated
evidence, which is the two-parameter structure Rajpal et al. (2022) fit to MEG:

    log b(i)  =  gamma * u(i)  +  lambda * sum_t log p(o_t | i)

gamma is prior precision, the thing the drug lowers. lambda is sensory precision,
held constant in arm 1 and lowered with dose in arm 2.
"""

import numpy as np

K = 6           # number of competing hypotheses about the world
TRUE = 0        # the hypothesis the world actually supports
MALADAPTIVE = 1 # the conviction the agent arrives holding

GAMMA_0 = 8.0   # prior precision with no drug: odds ~2981:1 on the wrong belief
LAMBDA_0 = 1.0  # sensory precision at baseline
WINDOW = 12     # observations arriving during the acute window


def prior_logits():
    """Structural prior, peaked on the maladaptive hypothesis.

    Scaled by gamma at use time, so gamma=0 gives a uniform prior and large gamma
    gives near point mass on MALADAPTIVE.
    """
    u = np.zeros(K)
    u[MALADAPTIVE] = 1.0
    return u


def likelihood(r):
    """A[j, i] = p(observation j | context i) at reliability r."""
    a = np.full((K, K), (1.0 - r) / (K - 1))
    np.fill_diagonal(a, r)
    return a


def softmax(x):
    x = x - x.max()
    e = np.exp(x)
    return e / e.sum()


def run_trial(dose, r, rng, window=WINDOW, gamma_0=GAMMA_0,
              lambda_0=LAMBDA_0, sensory_disruption=False):
    """One agent, one window. Returns (belief_at_window_end, belief_terminal).

    During the window the prior is relaxed to gamma_0*(1-dose) and observations
    arrive. Afterwards no new evidence arrives and the prior snaps back to gamma_0,
    so whether a revised belief survives is the REBAS measurement.
    """
    a = likelihood(r)
    u = prior_logits()

    gamma_d = gamma_0 * (1.0 - dose)
    # Arm 2 only: high doses also degrade sensory processing. This is an extra
    # assumption, not part of REBUS, which is why it is a separate arm.
    lambda_d = lambda_0 * (1.0 - 0.7 * dose) if sensory_disruption else lambda_0

    log_a = np.log(a)
    cum_ll = np.zeros(K)
    for _ in range(window):
        obs = rng.choice(K, p=a[:, TRUE])
        cum_ll += log_a[obs, :]

    belief_window = softmax(gamma_d * u + lambda_d * cum_ll)
    # Evidence was encoded at whatever precision was available at the time, so
    # lambda_d stays attached to it after the prior returns.
    belief_terminal = softmax(gamma_0 * u + lambda_d * cum_ll)
    return belief_window, belief_terminal


def classify(belief):
    """Outcome categories fixed in prereg section 3."""
    m = int(np.argmax(belief))
    if m == TRUE:
        return "insight"
    if m == MALADAPTIVE:
        return "no_change"
    return "false_insight"


def baseline_conviction(gamma_0=GAMMA_0):
    """Belief in the maladaptive hypothesis before dosing, for the SEBUS contrast."""
    return softmax(gamma_0 * prior_logits())[MALADAPTIVE]
