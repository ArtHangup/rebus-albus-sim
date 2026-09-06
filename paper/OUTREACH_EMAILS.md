# Direct outreach drafts: three emails, one specific question each

**STATUS: SENT by Josh 2026-09-06** (Wolff resent to max.wolff@charite.de after the MIND Foundation address bounced). Original staging note:** all three were sitting as DRAFTS in Josh's Gmail**, DOI
included, addressed to max.wolff@mind-foundation.org, asafron@gmail.com, and
rick.adams@ucl.ac.uk. Verify the Safron address before sending (it came from a
contact-lookup listing, moderate confidence; his X account @adamsafron is the
fallback). Josh reviews and sends.

Prepared 2026-09-05. Drafts only; Josh sends from josh@envitae.io. Before sending:
do the Zenodo upload so each email can carry the DOI, and swap it in where
marked. Keep each under 200 words; the specific question is the whole trick.

Addresses found:
- Rick Adams: rick.adams@ucl.ac.uk (public on his UCL profile).
- Max Wolff: MIND Foundation Berlin (Director of Research and Training) and
  HU Berlin; use the contact route on mind-foundation.org or his ResearchGate;
  no public direct address found.
- Adam Safron: Allen Discovery Center at Tufts and IACS; adamsafron.com has a
  contact route.

---

## 1. Max Wolff (the natural ally; his verbal model is what the result formalizes)

**Subject:** Your avoidance-free exposure model, implemented: it is the only
mechanism that worked

Dear Dr. Wolff,

I built a minimal Bayesian implementation of REBUS and ALBUS, preregistered in a
public git history before any code ran, and the central result is effectively a
formalization of the model in Learning to Let Go. Belief strengthening never
emerges from precision manipulations (passive relaxation, epistemic action,
miscalibrated self-knowledge all fail). It appears only when the diagnostic test
that could disconfirm the belief carries a cost the agent declines to pay, and
prior relaxation then works by raising the value of the avoided test until it
clears that cost: avoidance-free exposure, derived rather than posited, with a
cost ceiling above which no dose helps.

One question, if you have a moment: does the implementation misrepresent your
model anywhere that matters, and is there a signature of avoidance-free exposure
you would predict that I could compute? Criticism, especially where this is wrong
or already known, is exactly what I am after; one sentence pointing at the
weakest link would be genuinely valuable.

Paper and full audit trail: https://doi.org/10.5281/zenodo.22547758, github.com/ArtHangup/rebus-albus-sim

Joshua Rogers, independent researcher

---

## 2. Adam Safron (the fair-test question about ALBUS's own mechanism)

**Subject:** We implemented ALBUS's low-dose gain claim; one question about the
mapping

Dear Dr. Safron,

I implemented REBUS and ALBUS as a minimal Bayesian agent, preregistered in git
before code, including your low-dose gain mechanism as
gamma(d) = gamma0 (1 - d)(1 + Ad), which nests the REBUS mapping at A = 0.
Findings, reported with the failed predictions included: the gain alone cannot
strengthen a belief against a freely run diagnostic test at any strength tried,
and cannot produce lasting entrenchment without a test cost; with both present
there is a confirmed interior dose window of active strengthening; and the two
SEBUS accounts separate behaviorally by the sign of the low-dose change in
diagnostic engagement (gain predicts the drug suppresses checking, avoidance
predicts it never does).

The question I most need answered: is that gain mapping a fair rendering of
SEBUS's mechanism at the level ALBUS intends, and if not, which functional form
would be? I would much rather be corrected than cited. One sentence on the
weakest link would be valuable.

Paper and audit trail: https://doi.org/10.5281/zenodo.22547758, github.com/ArtHangup/rebus-albus-sim

Joshua Rogers, independent researcher

---

## 3. Rick Adams (the computational psychiatry read on the ratchet)

**Subject:** Chronic belief from avoidance plus biased encoding in a
preregistered toy model; one question

Dear Prof. Adams,

I ran a preregistered series of minimal Bayesian simulations implementing REBUS
and ALBUS (public git audit trail, failed predictions reported). The result I
would most value your judgment on: in this family, no single mechanism entrenches
a belief across sessions. Biased top-down encoding alone only delays recovery;
avoidance alone defeats itself (stored doubt eventually reprices the avoided
test); composed, they lock permanently, and treatment then fails in three
distinct ways (subthreshold dose, evidence starvation at any dose, chronicity
plus accumulated memory mass), each separable by one observable: engagement with
avoided disconfirming evidence.

My question: does this composition connect to, or duplicate, computational
psychiatry results I have missed, and would the engagement mediator be measurable
with existing task batteries? Criticism is the goal; one sentence on the weakest
link would be genuinely useful.

Paper and audit trail: https://doi.org/10.5281/zenodo.22547758, github.com/ArtHangup/rebus-albus-sim

Joshua Rogers, independent researcher
