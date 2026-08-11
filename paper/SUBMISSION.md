# Preprint submission package: paper 1

Prepared 2026-08-10. Everything below is ready to paste. The upload itself needs
your OSF login, so the final steps are yours; nothing here has been posted
anywhere.

## Venue: PsyArXiv (recommended)

Why: right scope (theoretical and computational psychology), no endorsement
gate, free, OSF-backed with DOI, moderation typically within a couple of days,
and it is where the REBAS and psychedelic-psychology audience looks. Alternatives
considered: bioRxiv (scoped to biology; a pure simulation paper fits awkwardly)
and arXiv q-bio.NC (needs an endorser; friction for an independent author).

## Repo status: PUBLIC as of 2026-08-10

Done: https://github.com/ArtHangup/rebus-albus-sim (69 tracked files, no
secrets, .venv excluded). The URL is in the paper's Reproducibility section and
in the availability statement below. Upload the freshly compiled main.pdf.

## Form fields, ready to paste

**Title:** What the Theory Never Specifies: Preregistered Simulations of REBUS
and ALBUS

**Author:** Joshua Rogers, independent researcher (josh@envitae.io)

**Abstract (plain text):**

REBUS holds that psychedelics reduce the precision of high-level priors,
permitting belief revision that rigid priors prevent. ALBUS replies that at low
doses beliefs are instead strengthened (SEBUS), with relaxation appearing only at
higher doses. Neither account has published equations or code. We built the
minimal Bayesian agent both theories describe, preregistered the mapping from
each paper's stated claims to model parameters (committed to a git history before
any code ran, for every arm), and swept dose against evidence quality across
billions of simulated agents. Three findings. First, REBUS as literally stated
produces no lasting change at all: dose transforms the acute state, and the
effect evaporates when precision returns to baseline. The failure is structural
rather than numerical, so something must make revision stick, and that something
is not in the theory. Second, adding a consolidation process, it acts as a gate:
below a threshold, lasting insight is exactly zero at every dose, and above it
dose scales the yield. But four defensible parameterizations of what
consolidation operates on disagree about whether the drug matters at all (under
one, the best available outcome occurs at dose zero), whether integration can be
made safe, and whether entrenched beliefs are treatable. The gate also passes
false beliefs, though in every mechanism tested false insight requires more
consolidation than true insight, so a safe integration window exists whose width
depends on which mechanism is right. Third, SEBUS never emerges from precision
mechanics: passive relaxation, epistemic action under a correct model, and
miscalibrated self-knowledge all fail to produce it. It appears only when the
diagnostic test carries a cost. Strengthening is avoidance, converging with the
clinical safety-behaviors account, and the mediating variable identifies what the
drug does: prior relaxation raises the epistemic value of an avoided test until
it is worth running. Above a cost ceiling, no dose helps. The general lesson is
methodological: implementing a theory's functional claim forces an assumption the
theory never specifies, and that assumption, not the theory, decides the result.
Every disagreement above is a measurable prediction.

**Discipline / subjects:** Psychology; Cognitive Psychology; Theory and
Philosophy of Science (secondary: Neuroscience if the form allows a second
discipline)

**Keywords:** psychedelics; REBUS; ALBUS; SEBUS; predictive processing; active
inference; belief revision; computational modeling; preregistration; safety
behaviors; exposure

**License:** CC-BY 4.0 (standard for preprints; keeps reuse simple)

**Conflicts of interest:** none. **Funding:** none; total compute cost was zero
API spend on a personal machine.

**Data and code availability statement (paste if the form has one):** All
simulation code, preregistration documents, amendments, and result files are in a
public git repository whose commit history orders every declaration before its
implementation: https://github.com/ArtHangup/rebus-albus-sim

## Upload steps (your login)

1. Sign in at osf.io, then go to the PsyArXiv submit page (preprints, add a
   preprint, choose PsyArXiv).
2. Upload `paper/main.pdf` (freshly compiled; check the title page renders).
3. Paste the fields above; set the license; confirm authorship.
4. Submit for moderation. It appears publicly after moderation, usually one to
   two days.
5. When it is live, note the DOI: the BCSP poster should carry it (and a QR code
   pointing at it) so the poster has a citable object behind it.

## After it is live

- Add the DOI to SESSION_LOG.md and to the poster materials.
- If the repo went public, confirm the URL in the PDF matches.
