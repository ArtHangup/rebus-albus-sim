# Computational Brain and Behavior: submission package for paper 1

Prepared 2026-09-05. Portal: Springer Editorial Manager, reached from
link.springer.com/journal/42113 (How to publish / Submit). Your account, your
click; everything below is paste-ready.

## Route and cost

Submit under the SUBSCRIPTION route: no fee to publish. Decline the open access
option if offered ($3,390); openness is already covered by the public repository
and the Zenodo DOI (green self-archiving of the accepted manuscript is standard
at Springer; verify the embargo terms at acceptance).

## Known requirements

- Abstract: 150 to 250 words, no undefined abbreviations. The manuscript's
  current abstract is far over; use the 245-word version below in the submission
  form AND swap it into main.tex before generating the submission PDF.
- Standard Springer declarations apply: conflicts (none), funding (none), data
  and code availability (statement below).
- Check the current guidelines page during submission for reference style and
  any structured sections; expect to be asked for highlights or a significance
  statement.

## Submission abstract (245 words)

REBUS proposes that psychedelics reduce the precision of high-level priors,
permitting belief revision; ALBUS predicts low-dose belief strengthening
(SEBUS). Neither theory has a runnable implementation. We implemented the
minimal Bayesian agent both describe, preregistering every mapping from text to
parameters in a public git history before writing the code it governed, across
numbered predictions whose failures are reported alongside confirmations. Three
results. First, REBUS as literally stated produces no lasting change: dose
enters only through a precision that reverts, so it cannot appear in the
terminal belief. Second, adding consolidation rescues persistence but introduces
a fork: four defensible parameterizations of what consolidation operates on
disagree about whether dose affects the lasting outcome at all, whether
integration can be made safe, and whether entrenched beliefs are treatable; in
every mechanism tested, false insight requires more consolidation than true
insight, so a safe integration window exists. Third, SEBUS never emerges from
precision manipulations (passive relaxation, epistemic action under a correct
model, miscalibrated self-knowledge) and appears only when the single diagnostic
test carries a cost the agent declines to pay, converging with the clinical
safety-behaviors account of belief maintenance: prior relaxation acts by raising
the epistemic value of the avoided test until it clears its cost, and above a
cost ceiling no dose helps. Implementing a theory's functional claims forces
assumptions the theory does not specify, and those assumptions, not the
theories, decide the clinically relevant results. Each divergence is a
measurable prediction.

## Cover letter draft

Dear Editors,

I am submitting "What the Theory Never Specifies: Preregistered Simulations of
REBUS and ALBUS" for consideration as a research article.

The paper reports the first runnable implementation of REBUS and ALBUS, two
influential and mutually contradictory theories of psychedelic action that have
until now existed only in prose, a gap conceded within that literature. The
contribution is methodological in a way I believe suits this journal: every
mapping from theory text to model parameters was declared and committed to a
public git history before the code that tested it existed, failed predictions
are reported in full, and the headline finding is about the theory space itself:
implementing each theory's functional claims forces assumptions neither theory
specifies, and those assumptions decide the clinically relevant results. A
secondary finding connects the psychedelic theory literature to the clinical
safety-behaviors account of belief maintenance, with discriminating behavioral
predictions stated in one observable.

All code, preregistration documents, amendments, and results are public at
github.com/ArtHangup/rebus-albus-sim, with an archived version at https://doi.org/10.5281/zenodo.22547758.
The work received no funding, has no conflicts of interest, and is submitted
solely to this journal. I am an independent researcher; the audit trail is
constructed so that every ordering claim can be verified without reference to
my credentials.

Thank you for your consideration.

Joshua Rogers

## Suggested reviewers (methods-oriented, no conflicts)

- Quentin Huys (UCL, computational psychiatry of decision and belief)
- Michael Moutoussis (UCL, computational models of clinical belief dynamics)
- Toby Wise (King's College London, avoidance and threat learning models)
- A Society for Mathematical Psychology modeling generalist chosen from the
  editorial board at submission time.

Do NOT suggest principals of either theory (Carhart-Harris, Friston, Safron and
coauthors); expect one as a reviewer anyway and let the editor choose that.

## Declarations, paste-ready

- Conflicts of interest: The author declares no conflicts of interest.
- Funding: This work received no funding. Total compute cost was zero paid API
  usage on a personal machine.
- Data and code availability: All simulation code, preregistration documents,
  amendments, and result files are publicly available at
  github.com/ArtHangup/rebus-albus-sim (archived at https://doi.org/10.5281/zenodo.22547758). The git
  commit history orders every preregistered declaration before its implementing
  code.
- Ethics: Not applicable; the work contains no human or animal data.

## Order of operations

1. Zenodo upload first (the DOI slots into the cover letter, the availability
   statement, and the paper).
2. Swap the 245-word abstract into paper/main.tex, recompile.
3. Optional but recommended before submission: retitle Section 7 to
   "Discussion" and fold Limitations under it (IMRaD-adjacent shape); this is
   the most likely reviewer request and costs twenty minutes now.
4. Submit via Editorial Manager, subscription route, declarations above.
