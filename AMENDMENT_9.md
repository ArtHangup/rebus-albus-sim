# Amendment 9: compounding sessions, chronicity, and the shape of treatment

Written 2026-08-10, **before writing or running any of the code below.** Prior
commits: 8109e7f through ab55a19 (hierarchy arm declared), f630ccb (hierarchy
results).

## Why this arm exists

The hierarchy arm found self-sealing within a single window: with ambiguous evidence
and strong top-down perception, the learning increment mirrors the prior back into
itself, and a 32-fold increase in learning moves conviction by 0.008. Everything so
far is single-session. The clinical questions are multi-session: does a sealed
belief deepen, persist, or slowly resolve if untreated; does going untreated longer
make treatment harder; does a course of dosed sessions need a minimum dose to
converge; and is one large session better or worse than several moderate ones. This
arm runs the capture mechanism through repeated sessions and asks which of those
answers the model gives, and, in keeping with the thesis, which of them depend on yet
another assumption nobody states.

That assumption, named now: **what happens to count mass across sessions.** If each
session's learning adds mass (Dirichlet accumulation, `N_{k+1} = N_k + E`), beliefs
mechanically rigidify with experience and chronicity is destiny. If the mean updates
at fixed mass (`N` constant, exponential forgetting), plasticity is stationary and
only capture itself can make chronicity matter. Both are defensible readings of
memory; no psychedelic theory specifies either. Both are run.

## Design

The two-level model and L-H encoding rule of AMENDMENT_8, unchanged (q = 0.8,
T = 12 observations per session, N0 = 20, starting conviction 0.8007, learning
amount E = 10 primary with {5, 20} as natural-history robustness). Sessions repeat:
each session draws fresh observations, runs inference under the trial's own current
stored prior with relaxation w = 1 - d applied during the session, then updates that
prior by the L-H rule. Each of 10,000 trials carries its own evolving prior.
Comparators: kappa = 1 (exact perception) and the L-E rule (no capture, dose-free),
both under the same protocols. r = 0.40 primary (the capture regime), r = 0.70 in
natural history only. Seed 11.

Protocols:

1. **Natural history:** dose 0 for 40 sessions. Track mean conviction and insight
   fraction per session. Recovery criterion, fixed now: the first session at which
   the insight fraction reaches 0.5, written S50, or "not reached in 40."
2. **Chronicity then treatment:** j in {0, 5, 10, 20, 40} untreated sessions, then
   dosed sessions at d in {0.2, 0.4, 0.6, 0.8, 1.0} until S50 or 40 treatment
   sessions. Outcome: course length as a function of j and d, under both mass
   variants.
3. **Protocol shape at matched exposure:** total exposure fixed at 1.0 after j = 10
   untreated sessions: (a) one session at d = 1.0, (b) two at d = 0.5, (c) five at
   d = 0.2, each followed by untreated sessions to a 20-session horizon. Outcome:
   insight fraction at horizon, both mass variants, kappa = 3, r = 0.40.

## Predictions, written before running

34. **Capture is delay, not destiny, and the delay is large.** In natural history at
    r = 0.40, recovery order is L-E fastest, kappa = 1 slower, kappa = 3 much slower:
    S50(kappa = 3) at least three times S50(kappa = 1), possibly not reached in 40.
    Mechanism expectation: erosion accelerates as conviction falls (weaker top-down
    frees encoding), so the trajectory is convex, a slow leak then a dam break. Two
    alternative outcomes are possible and are declared as such: a true plateau
    (conviction stable, insight never approached, sealing absolute) would be the
    stronger sealing result; a conviction that **climbs** across sessions would be
    compounding entrenchment, the one outcome that would finally show strengthening
    without avoidance or gain, and it gets the headline if it appears.

35. **Whether chronicity hurts is decided by the mass assumption.** Under mass
    accumulation, course length rises with j (later treatment faces heavier counts),
    with some (j, d) cells unreachable in 40 sessions: the untreatable regime of the
    consolidation arms, returning through time. Under fixed mass, course length is
    roughly flat in j. So "the longer untreated, the harder to treat," a claim with
    obvious clinical stakes, is not a prediction of the capture mechanism; it is a
    prediction of a memory assumption that has never been named, and the two variants
    bracket it.

36. **Under capture there is a dose threshold for cumulative treatment.** At
    kappa = 3, r = 0.40, there exists a dose below which repeated dosed sessions do
    not reach S50 within 40 sessions (each session's relaxation is too small to
    outpace re-sealing) and above which courses converge, with length falling in
    dose. At kappa = 1 every dose in the grid converges and length falls smoothly.
    If even d = 0.2 converges at kappa = 3, the threshold claim is dead and dose
    only buys speed; report which.

37. **Protocol shape is decided by the mass fork, not by the drug.** At matched
    total exposure: under fixed mass, the repeated-moderate protocol (c) matches or
    beats the single-high protocol (a), because each dosed session re-opens encoding
    and the gains persist between sessions. Under mass accumulation, (a) beats (c),
    because early sessions face the lightest counts. If one protocol dominates under
    both variants, the mass fork is not load-bearing here and that is reported.

## What would falsify the exercise

If the L-H and L-E trajectories are indistinguishable across all protocols (capture
has no cross-session signature at all), the arm's premise fails and that null is the
result. If protocol outcomes are insensitive to the mass variant everywhere,
prediction 35 and 37 die together and the arm reduces to prediction 34 and 36.
