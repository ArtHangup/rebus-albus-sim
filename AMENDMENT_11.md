# Amendment 11: confirmatory re-run of the gain arm's post hoc cells

Written 2026-08-10, **before running any of the code below**, and pushed to the
public repository before the run, so this declaration carries a third-party
timestamp. Prior commits: 156c626 (gain arm declared), 8bf4906 (gain results,
including cells at costs 0.1 and 0.2 that were added post hoc and labeled as
such in GAIN_RESULTS.md).

## Why

The most poster-relevant single finding of the gain arm, the interior dose window
in which the drug actively adds strengthening, currently rests on post hoc cells.
Paper 2 and the poster want to cite it without the asterisk. This amendment
declares an exact confirmatory replication with a fresh seed. Nothing is tuned;
the grid and criteria are fixed here before the run.

## Design

Identical machinery to gain.py and gain_posthoc.py: acting model, gamma_0 = 3.0,
r = 0.85, alpha = 8, 14 steps, gain mapping gamma(d) = gamma_0 (1-d)(1+Ad),
arithmetic consolidation c = 0.8 at window end. Grid: A in {0, 4} x costs
{0.1, 0.2} x 41 doses x 20,000 trials. Fresh seed 20260810, chosen as today's
date and fixed here.

## Predictions

42. At A = 4, cost 0.1: a SEBUS region (window-end conviction above the pre-dose
    baseline 0.8007) exists and is **detached from dose zero**: its lower edge is
    at dose 0.10 or above, and conviction at dose 0 is below baseline. Declared
    reproduction tolerance: the region's edges lie within 0.10 of the post hoc
    values (0.17 and 0.57).
43. At A = 4, cost 0.2: the region is anchored at or near dose zero (lower edge
    at or below 0.05), reproducing the post hoc shape transition between costs.
44. At A = 0, costs 0.1 and 0.2: no SEBUS at any dose, reproducing the null.

If prediction 42 fails (no region, or a region anchored at zero, or edges off by
more than 0.10), the interior-window claim reverts to unconfirmed, is flagged in
GAIN_RESULTS.md, and is removed from paper 2 and the poster.
