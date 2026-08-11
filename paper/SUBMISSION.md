# Preprint submission package: paper 1

**STATUS 2026-08-12: REJECTED by PsyArXiv moderation.** Grounds: their expertise
policy ("we need to look at the author's expertise via past publications"; no
prior peer-reviewed record found). The manuscript itself was not evaluated.
Decision marked final; do not resubmit there. An appeal exists (see below) and is
optional. **ACTIVE PLAN: Zenodo** for the DOI (no moderation, no credential
screen, sign in with the GitHub account that already owns the repo), then a
peer-reviewed journal submission as the durable fix, since journals evaluate the
manuscript rather than the author, and one published paper dissolves this wall
permanently.

## Zenodo upload (5 minutes, your GitHub login)

1. zenodo.org, Sign in with GitHub (ArtHangup).
2. New upload. Attach paper/main.pdf.
3. Resource type: Preprint. Title, author, abstract, keywords: paste from the
   fields below. License: CC-BY 4.0. Add the repo URL under Related works
   (is supplemented by).
4. Publish. The DOI is minted instantly; it also supports versioning for later
   revisions.
5. Optional, recommended: in Zenodo's GitHub integration, flip the switch on
   rebus-albus-sim and cut a release; the frozen code gets its own DOI, and the
   poster can cite paper and code separately.
6. Record the DOI here, in SESSION_LOG.md, and add the DOI QR to the poster.

## Optional appeal to PsyArXiv (low odds; costs one email)

Per their appeals page. Draft, factual and short:

> Dear PsyArXiv moderators,
>
> I am appealing the rejection of "What the Theory Never Specifies:
> Preregistered Simulations of REBUS and ALBUS." The stated grounds were the
> absence of prior peer-reviewed publications by the author. As I understand the
> March 2026 moderation policy, the past-publication check applies to formats
> such as reviews, case studies, and opinion pieces. This submission is an
> original research article reporting preregistered computational experiments,
> with all code, declarations, and results public at
> github.com/ArtHangup/rebus-albus-sim, where the commit history orders every
> preregistered declaration before its implementing code. I would respectfully
> ask that the work be assessed as a research article on its verifiable record
> rather than under the format policy for expertise-dependent submissions. If
> the policy is intended to apply to all first-time authors regardless of
> format, I accept the decision and thank you for your time.
>
> Joshua Rogers

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
