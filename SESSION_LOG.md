# Session log

## 2026-08-10 (Track C session)

Work this session, newest first. Poster abstract deadline is Sunday 2026-08-16.

### Later the same day: defensive edits and the gain-vs-avoidance arm

- Defensive edits after an attack review with Josh: "never states" became "never
  specifies" in the abstract and manuscript (titles included), "no route through
  precision" became "no route through precision reduction," and both files now
  carry the by-construction scope note about ALBUS's gain mechanism.
- AMENDMENT_7 (commit 156c626, declared before code): implemented ALBUS's own
  mechanism, gamma(d) = gamma_0(1-d)(1+Ad), head to head with avoidance.
  Predictions 27 to 29 all resolved, see GAIN_RESULTS.md. Headlines: gain cannot
  produce literal SEBUS against a freely run test at any strength tried; gain alone
  never entrenches after consolidation; gain amplifies avoidance (SEBUS region
  0.23 wide at A=0 cost 0.3, 0.80 wide at A=4); and in post hoc cells (cost 0.1,
  A=4, labeled) the SEBUS region detaches from dose zero, the one regime where the
  drug actively adds strengthening, requiring both mechanisms jointly. The
  mediator separates the accounts by sign: gain suppresses diagnostic engagement
  at low dose, avoidance never does.
- The "drug never adds strengthening" claim in ACTING_RESULTS.md is now known to be
  mapping-scoped; the poster abstract notes carry the qualified version. The
  manuscript (scope: amendments 1 to 5) remains accurate as written but the
  fold-in decision now covers amendments 6 and 7.
- Open question raised by the attack review, not yet acted on: the local git
  history is self-hosted preregistration; pushing the repo to a public remote
  would third-party timestamp everything from that point on. Josh's call.

### State at close

Everything committed. Deliverables all done: abstract draft 4 ready for Josh (outer
repo), three figure problems fixed, manuscript compiling under tectonic
(paper/main.tex, all bibliography entries verified by web search), and one new
preregistered arm run and written up. Open items for the next session: Josh sends the
abstract (BCSP requirements still unconfirmed; inquiry email drafted at
project/EMAIL_bcsp_poster_inquiry.md, send status unknown); the manuscript does not
yet include the AMENDMENT_6 window results (decide whether to fold them in as a
section 7 or keep the paper at amendment 5 scope); consider a decaying-trace variant
of consolidation timing (noted in WINDOW_RESULTS limits) only if it earns poster
space.

### New arm: the therapeutic window (AMENDMENT_6)

- Declared predictions 24 to 26 in AMENDMENT_6.md, committed at 6d4e093 before
  window.py existed. Composes the costly-test acting agent with P-A consolidation
  applied at a swept timing t_c; 5 costs x 21 doses x 14 timings x 3 strengths x
  20,000 trials.
- P24 confirmed: the lasting-conviction crossover sits at the acute SEBUS crossover
  (0.25 vs 0.23 at cost 0.3; 0.45 vs 0.42; 0.55 vs 0.50), robust to c. Refinement the
  prediction missed: above the cost ceiling conviction and insight dissociate; high
  dose still dilutes lasting conviction while lasting insight stays at 0.001
  (dissolution without insight). Post hoc observation, labeled as such.
- P25 confirmed at the threshold cost, failed above it: rise-then-fall trajectory
  exists at cost 0.3 (peak step 9 falling to 6 as dose rises, so t* falls with dose
  as predicted); at cost 0.5+ the fall never arrives inside the window. Timing rule:
  integration helps only when it captures the state after the avoided test has run;
  early consolidation locks in dilution, not learning (insight 0.003 at t_c=4 vs
  0.130 at t_c=14, cost 0.3, dose 0.5).
- P26 confirmed: across 4,200 dose-versus-zero cells the max excess of lasting
  conviction is negative (-0.0046). Dose never adds entrenchment.
- Writeup in WINDOW_RESULTS.md, figure in figure_window.png, noted in the poster
  abstract's Notes section.

### Manuscript

- paper/main.tex: standalone manuscript in the gwbench register (honest, no
  overclaiming, limitations, failed predictions reported). Compiles with tectonic.
  All four initially uncertain bibliography entries verified by web search (Zeifman
  Sci Rep 15:3651; Fisher Transl Psychiatry 14:394; Mago et al. Neurosci Conscious
  2026 niaf069 "Computational spirits"; Allohverdi et al. bioRxiv
  10.1101/2025.11.06.687023). Scope: through amendment 5; window arm not yet
  included.

### Figure fixes

- **figure2.py**: panel A redrawn at c = 0.8 instead of c = 1.0. At full consolidation
  P-A and P-B coincide exactly (both reduce to the window belief), so the P-A curve was
  invisible under P-B. At 0.8 they separate; both flat mechanisms (P-C at 0.952, P-D at
  0.443) are labeled.
- **figure3.py**: panel B annotations moved inside the axes (one was colliding with the
  title) and off the curves.

- **dense_grids.py / dense_grids.json**: resolution-only recompute of the three
  figure_main quantities (predictions 6, 8, 3) at 41 doses x 41 consolidation levels x
  20,000 paired trials. No new hypotheses, no new arms, mechanism byte-identical to
  consolidation.py; spot checks against the published coarse numbers printed by the
  script and all agree within Monte Carlo error. Done so panel B could carry a genuine
  continuous dose axis instead of three equal-width categorical columns (the "misaligned
  ticks" issue in RESULTS.md).
- **figure.py**: reads dense_grids.json; extents set so tick values sit at cell centers
  in both heatmap panels.

### Abstract

- POSTER_ABSTRACT.md rewritten (draft 4) in the outer Consciousness_Berkeley repo:
  REBUS/ALBUS lead, gwbench supporting, built on the settled thesis. Josh sends; BCSP
  requirements still unconfirmed (inquiry email drafted, send status unknown).
