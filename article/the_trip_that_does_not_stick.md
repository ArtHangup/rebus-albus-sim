# The Trip That Doesn't Stick

## What happened when I turned the leading theories of psychedelic therapy into running code

*Draft for pitching to a popular science outlet (Nautilus, Aeon, Scientific American
Mind register). About 1,550 words. Joshua Rogers. All claims trace to the public
repository; nothing here goes beyond what the papers say.*

---

Here is a puzzle that sits quietly under the psychedelic renaissance. Two people
take the same drug at the same dose in the same clinic. One of them walks out
changed: a belief that organized decades of their suffering, that they are
unlovable, that the world is unsafe, that nothing can be different, has somehow
loosened and stayed loose. The other feels the full force of the experience,
weeps, sees visions, touches what feels like truth, and six weeks later is exactly
who they were. A third person, and this is the unsettling one, comes back more
certain of the harmful belief than before.

The leading scientific theory of how psychedelics change minds is called REBUS,
short for relaxed beliefs under psychedelics. It says the drug turns down the
authority of your prior beliefs. The brain, on this view, is a prediction machine
that filters everything through what it already expects, and some expectations
grip so hard that no experience can loosen them. Psychedelics relax the grip.
Evidence gets a hearing it never gets sober. A rival theory, ALBUS, answers that
at low doses the drug does the opposite and makes beliefs stronger. The two
theories are elegant, influential, and in open disagreement.

They share one other feature. Neither has ever been implemented. No equations you
can run, no code, no simulation. The entire debate lives in prose, and prose is
forgiving in a way that running code is not.

So I built the machine both theories describe and ran it. Not a brain, not a mind:
the humblest possible version of the thing the theories talk about. My simulated
agent's whole mental life is six numbers, the probabilities it assigns to six
stories about its world. One story is true. One is a harmful conviction the agent
arrives holding at odds of three thousand to one. The drug does exactly one thing,
the thing REBUS says it does: it relaxes the conviction's weight for a while, and
then the weight comes back. To keep myself honest I preregistered everything in a
public code history: every modeling choice was committed before the code that
tested it existed, forty four numbered predictions in all. About a third of my
predictions died on contact with the results. The failures turned out to be the
best part.

The first thing the machine taught me is that REBUS, taken exactly at its word,
predicts that psychedelic therapy cannot work at all. The acute experience is
real: during the simulated trip, belief in the harmful story collapses and the
truth comes through. Then the window closes, the old weighting returns, and the
mathematics quietly deletes everything that happened. Not mostly. Exactly. If the
only thing the drug does is temporarily relax the grip of prior belief, then dose
cannot leave a trace, because it only ever touched a dial that reset. The trip is
real and the trip evaporates.

Something has to make revision stick, and the theory does not say what. Clinicians
have a word for the missing piece, integration, the work that happens after the
session. So I gave the machine integration: a process that consolidates some of
what the window revealed. And here the story turned. It matters enormously what,
precisely, integration operates on, and there are at least four defensible
readings. Under one, the drug's dose largely determines how much change survives.
Under another, dose is completely irrelevant, and the best outcome available comes
with no drug at all. Four readings of one unstated assumption, four different
clinical worlds, and nothing in either theory tells you which one we live in. That
is not a detail. That is the difference between psychedelic therapy being about
the drug and being about everything around the drug.

The second lesson came when I let the agent act. Real minds do not passively
receive evidence; they choose what to look at. So the agent got a set of tests it
could run on its world, and one of those tests, only one, could actually
distinguish the harmful conviction from the truth. Here is what did not work: I
could not make the agent's belief strengthen, the thing ALBUS predicts at low
doses, through any manipulation of belief weighting whatsoever. Rigid priors,
distorted self-knowledge, none of it. A believer that is willing to check its
belief, however rigid, eventually checks it and gets corrected.

Then I made the one revealing test expensive, and everything changed. When
confronting the belief carries a cost, the agent stops paying it. It keeps
gathering evidence, but only the comfortable kind, the kind that cannot settle the
question, and its conviction climbs. Belief strengthening, it turns out, is not a
weighting phenomenon in this model family. It is an avoidance phenomenon. And with
that, the drug's role snapped into focus in a way neither theory states:
relaxation raises the agent's uncertainty, which raises the value of the question
it has been refusing to ask, until asking finally becomes worth the price. In this
little world, that is what a psychedelic is for. It does not install insight. It
makes an avoided question worth asking.

If that sounds familiar, it should. Clinical psychology has known for over thirty
years that anxious beliefs survive because of safety behaviors, the small
avoidances that prevent the disconfirming test from ever being run, and that
exposure therapy works by arranging exactly that test. Researchers had even
proposed, in words, that psychedelic therapy is a kind of avoidance interruption.
I did not discover this idea, and it matters to say so plainly. What the machine
adds is what words cannot: proof that in this family nothing else works, that the
weighting story alone cannot produce what it claims, and a set of measurable
predictions, including a threshold, a ceiling (if confronting the belief is costly
enough, no dose helps at all), and a marker I will come back to.

The third lesson is the one I find hardest to stop thinking about. I ran the agent
through many sessions, letting it learn between them, and I gave its perception a
human flaw: ambiguous experiences get interpreted through current beliefs. A
neutral glance reads as contempt if you already believe you are despised. Each
mechanism alone was survivable. Biased interpretation alone only delays recovery,
because the world keeps volunteering correction. Avoidance alone actually defeats
itself, slowly: refusing the test lets doubt quietly accumulate until the question
becomes irresistible, and then the belief resolves. But together they form what I
came to call the ratchet. Avoidance starves the belief of its test. Biased
interpretation launders every ambiguous experience into fresh confirmation, so the
accumulated doubt never gets credited. Conviction climbs, session after session,
and locks. In the model, this is how a belief becomes chronic: not through any
single flaw, but through two flaws that each disable the other's natural cure.

The treatment simulations that followed had an uncomfortable clinical shape. Below
a dose threshold, treatment sessions accomplish nothing, because the avoided
question never gets asked. When avoidance is severe enough, even the maximum dose
produces something stranger: the conviction dissolves but nothing replaces it,
because no discriminating evidence ever arrives, a permanent middle state in which
the belief is neither held nor resolved. And waiting matters: in the model, a
treatable case at session five can become an untreatable one at session twenty.

Now the caveats, which deserve their own paragraph and not a footnote. This agent
is six numbers. It has no emotions, no body, no childhood, no serotonin, and
nothing here touches consciousness or what an experience feels like. The specific
numbers in these results are properties of my parameter choices, not of people.
What the simulations actually test is the theories, not the brain: the theories
are stated in exactly this mathematical vocabulary, so building the minimal system
that satisfies their own description is a fair audit of what they do and do not
say. The headline of that audit is that the most important claims, whether the
drug matters, whether integration is safe, why beliefs become chronic, are decided
by assumptions the theories never state.

But the machine's best gift is that every one of those assumptions became a
measurable question, and they converge on a single observable: how willing a
person is to engage with the evidence they have been avoiding. The two rival
accounts of belief strengthening disagree about its direction at low doses. The
model says therapy works when engagement rises and fails, in three distinguishable
ways, when it does not. That is a number a clinical study could track tomorrow,
with no simulation required.

The psychedelic renaissance is running far ahead of its theories, and the theories
themselves, it turns out, are running on unstated assumptions. Running code is one
way to find out where they live. Everything here, the code, the preregistrations,
the predictions that failed, is public, and the invitation is the same one the
model makes to its own stubborn agent: the question you have been avoiding is
usually the one worth asking.

---

*Joshua Rogers is an independent researcher. The simulations, preregistrations,
and both technical papers are at github.com/ArtHangup/rebus-albus-sim.*
