# Session log

## 2026-08-10 (Track C session)

Work this session, newest first. Poster abstract deadline is Sunday 2026-08-16.

### Preprint SUBMITTED (2026-08-10, evening)

- Paper 1 uploaded to PsyArXiv by Josh, pending moderation (typically 1 to 2
  days). The OSF affiliation concern resolved via the plain email signup.
  "Public Preregistration" answered Unavailable on the form: the git trail is
  not a registry deposit, and the paper says only what is true about it.
- WHEN LIVE: record the DOI here and in paper/SUBMISSION.md; add DOI + QR to the
  poster; consider a one-sentence registry-disclosure addition to the
  Reproducibility section in the next version. For paper 2: preregister on OSF
  Registries BEFORE running further arms, so the next form answer is Available.

### Repo is PUBLIC (2026-08-10)

- https://github.com/ArtHangup/rebus-albus-sim, pushed with full history, so all
  preregistration commits now carry third-party timestamps. Pre-publish check:
  69 tracked files, no secrets, .venv/pycache ignored, paper PDF gitignored.
- Repo URL added to the paper's Reproducibility section and SUBMISSION.md;
  recompiled. NEXT AND FINAL STEP IS JOSH'S: upload paper/main.pdf to PsyArXiv
  per paper/SUBMISSION.md, then put the DOI on the poster and in this log.

### Previous: safety-behaviors literature integrated; preprint package ready

- Verified and integrated the prior-art literature the avoidance results needed:
  Salkovskis 1991 (safety behaviors prevent disconfirmation), Foa and Kozak 1986,
  Craske et al. 2014 (exposure/inhibitory learning), Wolff et al. 2020 (verbal
  model: psychedelic relaxation enables avoidance-free exposure), Zeifman et al.
  2020 (experiential avoidance reductions track outcomes), plus computational
  psychosis (Corlett 2010, Adams 2013, Sterzer 2018). Positioning everywhere is
  "convergence, not discovery": the formal additions are necessity (three
  precision mechanisms fail), the derived drug role (repricing the avoided test),
  the ceiling, the dose-zero peak, and the mediator.
- paper/main.tex: new related-work paragraph, "Relation to the exposure account"
  in the discussion, 8 new bibitems; compiles clean. ACTING_RESULTS.md and
  RATCHET_RESULTS.md carry matching prior-art notes.
- paper/SUBMISSION.md: complete PsyArXiv handoff package (venue rationale,
  paste-ready metadata, plain-text abstract, license, steps). BLOCKED ON JOSH:
  the OSF login and upload are his; also his call whether to make the repo
  public first (gh command in the package; recommended so the preregistration
  hashes are auditable and the poster can carry the DOI).

### Previous: the ratchet arm (AMENDMENT_10, capture plus avoidance)

- Declared predictions 38 to 41 at ca798a0 before ratchet.py existed. Acting agent
  (costly deep probe) with capture-weighted learning across sessions.
- P38 CONFIRMED where it matters: the first permanent entrenchment in ten
  amendments. Cost 0.3 + capture locks conviction at 0.989 forever; cost 0.8 locks
  at both kappas (0.946 / 1.000). At cost 0.3 without capture the ratchet is
  transient (peak 0.844, recovery by session 17) because avoidance is
  self-limiting: shallow eliminations migrate stored mass onto {0,1}, rebuilding
  the doubt that reopens the test (usage rises 0.024 to 0.061). Capture starves
  that channel (usage falls to 0.015): avoidance loads the trap, capture locks it.
- P39: boundary confirmed but far harsher than the within-session crossover: at
  cost 0.8 NO dose converges: d=1.0 dissolves conviction to 0.42 then stalls
  forever with insight never crossing 0.5 (deep usage 0.001): dissolution without
  insight as a permanent terminal state. The "subthreshold dosing is harmful" half
  DIED as declared (0.977 treated vs 0.989 untreated: useless, not harmful; no
  headroom because untreated already saturates).
- P40 confirmed to infinity: cost 0.3 d=0.6 course 12 at j=5, never at j=20, at
  FIXED mass (reversing the sessions arm's time-heals). Accumulating mass removes
  the last rescue (even d=1.0 never at j=20).
- P41 confirmed: no ratchet at cost 0 (recovery by session 4 both kappas).
- Composition summary now standing: entrenchment requires avoidance plus one of
  capture, high cost, or accumulated mass; treatment fails three observable ways
  (late, subthreshold, evidence-starved), separated by the diagnostic-engagement
  mediator.
- Files: AMENDMENT_10.md, ratchet.py, ratchet_results.json, RATCHET_RESULTS.md,
  figure_ratchet.png. Named next steps: derive the cost from expected self-model
  revision; consider folding amendments 6 to 10 into the manuscript as a second
  part or a follow-on paper.

### Previous: the compounding-sessions arm (AMENDMENT_9)

- Declared predictions 34 to 37 at 3615dd2 before sessions.py existed. Multi-session
  runs of the capture mechanism, both count-mass variants, with treatment protocols.
- Mostly a graveyard of the declared predictions, reported as such, and the
  failures are the findings:
  - P34: shape confirmed (convex leak-then-break erosion), magnitude FAILED: capture
    delays recovery 1.3x to 1.8x vs exact perception (declared bar was 3x), 3x to 6x
    vs unbiased learning; S50 = 8 (fixed mass) / 23 (accum). No plateau, no climb:
    cross-session compounding does not strengthen beliefs. CORRECTION issued inside
    HIERARCHY_RESULTS.md: self-sealing is within-session freeze plus multi-session
    delay, not destiny, in a stationary world.
  - P35: core confirmed (the count-mass assumption decides whether chronicity
    hurts), both declared shapes wrong: fixed mass = chronicity helps; accum =
    non-monotone with a hardest window at j ~ 5, and the hump needs capture AND
    accumulation jointly (kappa=1 accum is monotone).
  - P36: dose threshold DEAD (declared alternative): every dose converges, dose
    buys speed only. Contrast with the avoidance cost ceiling noted.
  - P37: both shapes failed: at matched total exposure, protocol shape is
    irrelevant under both mass variants (0.996/0.993/0.986 fixed;
    0.634/0.643/0.636 accum); the mass assumption moves the level by 35 points.
- Two more unstated assumptions now carry clinical answers: count-mass dynamics and
  world stationarity. Named next arm: compose capture with avoidance (an acting
  agent with biased perception that can stop sampling the world that would heal it).
- Files: AMENDMENT_9.md, sessions.py, sessions_results.json, SESSIONS_RESULTS.md,
  figure_sessions.png.

### Later still: the hierarchy-with-learning arm (AMENDMENT_8)

- Declared predictions 30 to 33 at ab55a19 before hierarchy.py existed. Two-level
  model (context, events, observations), persistence via Dirichlet-mean learning on
  the stored context prior, four increment rules, precision at use time only.
- P30 confirmed: hierarchy alone rescues nothing; exact reduction to the flat model.
- P31 confirmed: learning inherits the consolidation fork. Dose spread positive
  under posterior-driven learning, exactly 0.0000 under evidence-driven and decay
  (paired draws). "Active inference provides persistence through learning" is true
  and changes nothing: the increment source is the same unstated fork.
- P32: (a) and (c) confirmed, (b) FAILED and reported dead: no emergent
  self-strengthening anywhere (closest 0.799 vs start 0.8007). What appeared
  instead: SELF-SEALING (post hoc, labeled): with ambiguous evidence (r=0.4) and
  strong top-down perception (kappa=3), lasting conviction is frozen at ~0.79
  across a 32-fold increase in learning and insight stays 0.000 at dose 0; dose
  unfreezes encoding. Third rigidity defense: capture (interpretation), joining
  avoidance (action) and gain (weighting).
- P33 confirmed: direction shift of the learning target across dose is exactly 0
  under evidence-driven learning, 0.72 posterior-driven, 1.36 encoding-driven:
  plasticity scales belief change, relaxation redirects it; dissociable claims.
- Files: AMENDMENT_8.md, hierarchy.py, hierarchy_results.json,
  HIERARCHY_RESULTS.md, figure_hierarchy.png.
- POSTER_ABSTRACT.md is now draft 5 (Josh/another track folded gwbench Tracks A and
  B in); left untouched this round. If the poster wants the hierarchy arm, the line
  is: "the framework's own learning mechanism inherits the fork, and hierarchical
  perception gives rigid beliefs a third defense, interpretive capture."

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
