# Second extraction — Temperley 2002, "A Bayesian Approach to Key-Finding"

Row 5 of the Task B L2 slice. Written in a session that had not opened the first extract when
§0–§8 were written. The cross-check against the first extract is §9 and was written after this
file had landed.

## §0 — What was read, and the bound on this read's independence

**Read at the object:** the paper whole, all twelve pages, at
`docs/research_papers/temperley_2002_icmai_bayesian_key_finding.pdf` (85,400 bytes on disk).
The page count was established at the tool by a deliberately out-of-range request, which
answered that the document has twelve pages. Printed pagination 195–206; the twelfth page is the
reference list.

**Every page image was checked at the image**, not at the call's success line. All twelve were
present and legible.

**The independence bound, declared rather than claimed away.** This side booted on the handoff
line and read **four of its entries whole and parts of four others**. Those entries carry no
summary of this paper's contents. **What touches the paper's CONTENT is the candidacy row alone**
— one line, quoted at §1.4 below — which states a verdict and a reason; the entries touch row 5
only as a position in a reading order. That is contamination in the direction the commission's
rule cares about, and it is written down here rather than denied. **The first extract was not
opened before §9.**

*(★ CORRECTED AT THE USER-ORDERED CHECK. TWO FORMER WORDINGS, PRESERVED (#12): "four of its
entries plus parts of two older ones", **an undercount of this side's own reading** — four were
read whole and four others in part, as (vi) of this sitting's entry records; and "What this side
did read that touches row 5 at all is the candidacy row itself", which was false as stated,
because two of the entries name row 5 as next in the table order. What is true is the narrower
claim now standing: nothing but the candidacy row touches the paper's content.)*

**What was read AFTER this section was written** — the pages re-opened at the read-back and at
the cross-check — is recorded at §8.1 and §9.1, not here.

**Not read, not searched, not staged for this member:** `FRAMEWORK.md` at all, the slice
derivation, the progress record, the findings surface, `population.md`, the bibliography row for
this paper, and every other extract. **No sweep of the repository was run for this paper** — not
for its author, not for its title, not for any of its values — so **this read asserts nothing
about what the record says of it.** That half lives in the first extract.

## §1 — What the paper is

**§1.1 Identity, confirmed at page 1 and at the footer of page 1.** "A Bayesian Approach to
Key-Finding", David Temperley, Department of Music Theory, Eastman School of Music, Rochester,
New York. The footer records the volume: ICMAI 2002, LNAI 2445, pages 195–206, 2002,
Springer-Verlag Berlin Heidelberg. **Each of those items was read on page 1 itself.**

*(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "Every axis of that identity is
at the object." The word "axis" had no stated argument — axis of what list? The list a reader
would supply is the bibliography row's, and **this read did not open the bibliography row**, so
the sentence claimed a match against a list it never saw. What is true is what now stands: these
items were read on page 1.)*

**§1.2 What it sets out to do, in the paper's own framing.** The stated aim is to examine the
connection between the key-profile model of key-finding and Bayesian cognitive modelling, and to
show that the key-profile model — the author's own modified version in particular — can be
reinterpreted as a Bayesian probabilistic model with a few small modifications. The author gives
three reasons for caring: a more compelling psychological motivation for the key-profile model; a
possible broader connection between Bayesian modelling and the preference-rule approach across
several musical tasks; and a bearing on ambiguity and expectation.

**§1.3 What it is NOT.** It is not a new key-finding algorithm proposed as an improvement. The
Bayesian version it builds scores **lower** than the model it reinterprets (§5). It is a
reinterpretation paper whose own closing words call many of its ideas conjectural.

**§1.4 The candidacy row this read was given, quoted because it is the one piece of the record
this side saw before reading.** At `reading_pass/candidacy_upgrades.md`, row 5 reads: a
tonality-deciding method, and the source of V3's spelling measurement; admitted for the method,
not the figure. **This read takes no position on what V3 is** — that document was not opened —
and records only this: **the paper prints one spelling-related rate**, at §5.3 below. **Whether
that is the measurement the row means is a question for whoever opens V3**, and this read does
not answer it.

*(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "the spelling
measurement the row points at is almost certainly the value at §5.3 below". **That is a hedged
assertion about an unexamined thing** — the user's own list names that shape — sitting one clause
after a sentence saying this read takes no position on it.)*

## §2 — The method, as the paper states it

### §2.1 The key-profile model being reinterpreted

A key-profile is a twelve-valued vector, one value per pitch class, representing that pitch
class's stability or compatibility relative to a key. Profiles for other keys are obtained by
rotating the C profile by the appropriate number of steps; the paper gives C major and C# major
as its worked instance of the rotation.

The paper prints the two profiles it uses as Figure 1 on printed page 197. Transcribed here as
printed, C-relative:

| Pitch class | C major profile | C minor profile |
|---|---|---|
| C | 5.0 | 5.0 |
| C#/Db | 2.0 | 2.0 |
| D | 3.5 | 3.5 |
| D#/Eb | 2.0 | 4.5 |
| E | 4.5 | 2.0 |
| F | 4.0 | 4.0 |
| F#/Gb | 2.0 | 2.0 |
| G | 4.5 | 4.5 |
| G#/Ab | 2.0 | 3.5 |
| A | 3.5 | 2.0 |
| A#/Bb | 1.5 | 1.5 |
| B | 4.0 | 4.0 |

**These are the author's own modified values, not Krumhansl and Schmuckler's.** The paper states
that its profiles differ slightly from the original version's, which were based on experimental
data, and points at reference [14] for why the modified values were proposed. **No derivation of
these twenty-four values is given anywhere in this paper as read**, and reference [14] was not
opened here.

The paper describes the profiles as reflecting basic theoretical principles of tonal music: in
the major profile the major-scale values exceed the chromatic ones, within the scale the
tonic-triad values exceed the other diatonic ones, and the tonic is highest of all; the same is
said of the minor profile, on the assumption of the harmonic minor scale.

### §2.2 The input, and why it is a present/absent set rather than durations

The model builds an input vector for a stretch of music. In the original design this vector
carried the total duration of each pitch class. The paper reports that this weighted form gave
repeated notes too much weight, and gives Figure 2b as the case: repetitions of one note pull the
judgment toward that note's major and minor keys where a different key is the correct reading.
The paper states the same problem arises when a pitch class is duplicated across octaves.

**The fix is the flat input vector, and it is what the tested model uses.** Each pitch class
present in the segment scores 1 and each absent one scores 0. Because the values are all 1 or 0,
the correlation reduces to adding the key-profile values of the pitch classes that are present.
The paper's worked instance is Figure 2a, where the C major total is obtained by adding the C
major profile's values for C, D, E and F.

The paper reports that the flat-input approach achieved substantially better results than the
weighted-input approach of the original model. **It prints no value for that comparison** — the
figures are in reference [14], which this read did not open.

### §2.3 The segmentation the model requires, supplied from outside

The flat input vector only makes sense over a stretch, so **the model assumes a segmentation of
the piece which has to be provided in the input.** The paper states that segments of one to two
seconds work best, and that in the tests reported it used metrical units — bars, half-bars and so
on — always taking the smallest metrical level longer than one second.

**This is the paper's own hardest upstream requirement and the author names it as a weakness
twice**: in the closing paragraph of the paper's section 4, on printed page 202, where he flags
that the approach is not ideal because it requires a prior segmentation and there is little
reason to think such a segmentation is involved in human key-finding; and on printed page 203,
where he notes that a reduction-based alternative would avoid the arbitrary segmentation the
flat-input model requires.

*(★ CORRECTED AT THE READ-BACK. FORMER WORDING, PRESERVED (#12): "at §4's opening he flags…".
**The passage is at the CLOSE of that section, not its opening** — a location stated from memory
of writing rather than checked at the page.)*

### §2.4 Modulation, and the change penalty

The original key-profile model produced a single key judgment for the whole input and could not
handle modulation. Judging each segment independently is available once a segmentation exists,
but the paper rejects it as unsatisfactory on the ground that key has a kind of inertia — once in
a key, one prefers to stay unless the evidence is strong.

**So each segment is evaluated independently and a change penalty is imposed where a segment's
key differs from the previous segment's.** The penalties combine additively with the key-profile
scores.

The paper then draws the consequence that matters structurally: once the change penalty exists,
a segment's best analysis depends on what precedes it, and — if the aim is the best analysis
overall — on what follows it as well. Guaranteeing the optimum means considering every labelling
of every segment with a key, and the number of those grows exponentially with the number of
segments. **The paper states this is not feasible in practice for a computer or a human mind, and
that the implementation uses dynamic programming to find the highest-scoring analysis without
generating them all.**

### §2.5 The Bayesian re-reading

The general frame the paper sets up: a perceiver receives a surface and must recover the
structure that gave rise to it; the task is to find the structure maximising the probability of
structure given surface; by Bayes' rule and because the probability of the surface is constant
across structures, this is the structure maximising the probability of the surface given the
structure multiplied by the prior probability of the structure. The paper's illustration is
speech recognition, with a phone sequence as surface and a word sequence as structure.

Applied to key-finding, **the structure is a sequence of keys and the surface is a pattern of
notes.**

**The prior over structures.** All 24 keys are taken as equally probable for the first segment.
For every later segment there is a high probability of staying in the previous segment's key and
a lower one of switching. The paper assumes 0.8 for staying and 0.2 divided by 23 for changing to
any one other key, and states that treating all key changes as equally likely may be an
oversimplification. The structure's probability is the product of these per-segment values.

**The likelihood of the surface.** The paper supposes that in each segment the composer makes
twelve independent decisions whether to use each pitch class, and that these probabilities are
what a key-profile expresses. A segment's score is the product of the profile values for the
pitch classes present multiplied by the product of the complementary values for the pitch classes
absent, the complementary value being one minus the profile value.

**The whole-piece quantity** is the product over segments of the modulation value and the two
products above; taking logarithms turns it into a sum, which the paper notes is legitimate
because the logarithm is monotonic and only the maximising structure is wanted. After the
logarithm, a segment's score is a sum of a modulation term, the present-pitch-class terms and the
absent-pitch-class terms.

### §2.6 What the equivalence claim actually says, which is narrower than the abstract

The paper's own comparison of the two models, at printed page 202, is conditional and it names
its own exception. **The two are said to be virtually identical IF one pretends that the earlier
model's key-profile values and modulation penalties are themselves logarithms of other numbers.**
Two differences are then called superficial or cosmetic: every Bayesian score is negative,
because the values are logarithms of probabilities; and the Bayesian model adds a modulation term
for every segment rather than only for modulating ones. The paper says both could be removed by
scaling the earlier model's values differently, without changing its results.

**One difference is then called significant and is not disposed of:** the earlier model summed
key-profile values for the pitch classes present only, while the Bayesian model also adds the
absent-pitch-class terms. The paper says this may be a significant difference between the two
models, and §5.4 below records what the measurement then did with it.

**So the introduction's stronger form — that the key-profile model simply is a Bayesian
probabilistic model — is wider than what the body establishes.** The body establishes a
conditional identity with one named residual difference, and that residual is the one the
measurement later attaches the performance gap to.

## §3 — Coupling facts

### §3.1 What the method ASSUMES about its upstream

- **A segmentation of the piece, supplied in the input.** Not derived by the method. The paper's
  own choice is metrical: the smallest metrical level whose unit is longer than one second, with
  one to two seconds named as the range that works best.
- **Pitch-class content per segment as a present/absent set.** Durations and repetition counts are
  deliberately discarded by the flat input vector; the paper's stated ground is that carrying them
  measured worse.
- **Neutral pitch classes, with no spelling, in the version whose figures govern.** The paper
  develops a spelling-aware variant and then sets it aside for the tests that follow (§5.3).
- **Enough note information to decide presence within a segment** — onsets and durations — but
  nothing above the note surface. No harmony, no metre beyond the supplied segmentation, no
  reduction.

### §3.2 What it HANDS downstream

- **One key label per segment, from 24 keys** — twelve tonics times major and minor. No modes
  beyond those two. No abstention: every segment is labelled.
- **A joint labelling of the whole piece**, not a per-segment answer computed independently; the
  change penalty makes the labelling interdependent in both directions, and the reported
  implementation optimises over the whole piece by dynamic programming.
- **Modulations as a derived fact**, not a primitive: a modulation is where consecutive segments
  carry different labels. The method emits no modulation object, no boundary confidence and no
  distinction between a modulation and a tonicization — the absence of that distinction is one of
  the paper's own named error sources (§5.5).
- **A numerical score per analysis**, in the Bayesian reading a log-probability. The paper says
  ambiguity is readable off these scores: an ambiguous passage is one where two or more analyses
  are close to tied.
- **In principle, a probability of the surface itself**, by summing the joint quantity over all
  structures. The paper states this and notes the summands are exactly what must be generated
  anyway to find the best structure. **No such value is computed anywhere in the paper as read** —
  a negative over the twelve pages this read opened, which is the whole paper, and over nothing
  else.

### §3.3 Its own STATED scope and limits

- **Repertory:** common-practice tonal music. The test material is excerpts from a tonal-harmony
  teaching workbook (§5.1).
- **Key vocabulary:** major and minor only — the paper's own 24 keys. **This read met nothing in
  the twelve pages admitting a modal reading**, which is a statement about what was met and not a
  proof that no such sentence exists.
- **The segmentation requirement is a limit the author himself flags twice** (§2.3), on the ground
  that a supplied segmentation is implausible as a model of human key-finding.
- **Chromatic harmony is a named weakness.** The paper reports that the program frequently had
  trouble with chromatic harmonies such as augmented sixth chords, and says special rules for such
  cases might be desirable but had not been attempted.
- **The modulation rate is a named weakness**, in both directions (§5.5).
- **Spelling is excluded from the governing version on a modelling-perception ground, not a
  measurement one** (§5.3).
- **The author's own closing bound:** many of the paper's ideas are called conjectural, and the
  Bayesian framework is offered as a promising avenue deserving further exploration rather than as
  an established result.

## §4 — Claims, labeled

Each label is this read's, against the commission's definitions: FACT where the paper states or
measures it and the location is given; THEORY where it is established published theory the paper
draws on; CONJECTURE where the paper itself offers it as a suggestion, a possibility or an
intention. **Where the paper labels its own claim, that is noted — several of the CONJECTURE
labels below are the paper's own hedging and not this read's downgrade.**

**F-1 [FACT, p. 198].** The earlier key-profile model, run on 46 excerpts from the Kostka–Payne
workbook and compared against the analyses in the instructors' manual, labelled 751 of 896
segments correctly, a rate the paper states as 83.8%.

**F-2 [FACT, p. 198].** For that test the key-profiles were fixed before the test, but **the
change penalty was adjusted to achieve optimal performance on the test.** The paper states this
in its own parenthesis.

**F-3 [FACT, p. 202].** The Bayesian version, on the same corpus, achieved a correct rate the
paper states as 77.1% — lower than F-1.

**F-4 [FACT, p. 202].** The Bayesian version's key-profiles were generated empirically from the
Kostka–Payne corpus, and **the paper states that the corpus used for estimating parameters should
normally not be used for testing**, saying this was deemed necessary given the small amount of
data available.

**F-5 [FACT, p. 202].** For the Bayesian version too, the change penalty was the only parameter
to be set, different values were tried, and the one yielding optimal results was chosen.

**F-6 [FACT, p. 199].** A version of the model that recognised spelling distinctions reached a
level of performance the paper states as 87.4% on the Kostka–Payne corpus.

**F-7 [FACT, p. 199].** That spelling-aware version is set aside for the tests that follow, on
the stated ground that if the aim is to model perception, supplying the program with spelling
could be considered cheating, since a pitch's spelling may sometimes be inferable only by using
knowledge of the key.

**F-8 [FACT, p. 201].** Table 1 gives, per scale degree relative to the current key, the
proportion of Kostka–Payne segments in which that degree occurs, separately for major and minor
keys. The table is transcribed at §5.2.

**F-9 [FACT, p. 197].** The flat-input approach achieved substantially better results than the
weighted-input approach of the original model. **No value for that comparison was met anywhere
in the twelve pages as read**; the paper points at reference [14], which was not opened here.

**F-10 [FACT, p. 202].** The paper states it is unclear why the Bayesian model performs worse
than the earlier one, and records an intention to investigate further. **The paper does not
isolate a cause.**

**F-11 [FACT, p. 198].** The program's errors are attributed to three things: a sometimes wrong
rate of modulation, in both directions; trouble with chromatic harmonies such as augmented sixth
chords; and pitch spelling. **No per-class share of the errors is given for any of the three.**

**T-1 [THEORY, p. 199–200].** Bayes' rule, and the standard reduction that dropping the constant
probability of the surface leaves the product of likelihood and prior as the quantity to
maximise. The paper states it as established and applies it without deriving it.

**T-2 [THEORY, p. 200].** The Bayesian framing of perception as recovering a structure from a
surface, with speech recognition as the worked example, cited to reference [5].

**T-3 [THEORY, p. 196].** The key-profile model of key-finding as such, attributed to Krumhansl
and Schmuckler at reference [8], with the author's own modified version at [13] and [14].

**T-4 [THEORY, p. 204].** The preference-rule approach as a family of models applied to metrical
analysis, grouping, pitch reduction, harmonic analysis and stream segregation, cited to [10] and
[14].

**T-5 [THEORY, p. 205].** That listeners' expectations for melodic continuations correspond
closely with the original model's key-profiles, attributed to Schmuckler at reference [12]. **The
paper reports this as an existing experimental demonstration and measures nothing itself.**

**C-1 [CONJECTURE, the paper's own hedge, p. 196].** That the key-profile model, and the author's
version in particular, simply is a Bayesian probabilistic model. The paper introduces this with
"it could practically be argued that", and §2.6 above records that the body establishes a
narrower, conditional form of it.

**C-2 [CONJECTURE, the paper's own hedge, p. 204].** That preference-rule models generally can be
construed as Bayesian models. The paper says it appears that they can; no second model is carried
through in this paper.

**C-3 [CONJECTURE, p. 204].** The proposed split of preference rules into two categories — rules
bearing on the probability of a structure, and rules bearing on the probability of a surface
given a structure — with the Modulation Rule assigned to the first and the Key-Profile Rule to
the second. **§7.1 records an inconsistency in how the second category is named.**

**C-4 [CONJECTURE, p. 203].** That a more successful model might be built on the weighted-input
idea by generating the surface from a sparser reduced representation in which immediate
repetitions and perhaps octave doublings are removed. The paper immediately states the
methodological problem: the reduction would have to be derived before key-finding could take
place.

**C-5 [CONJECTURE, p. 203].** That treating key-profiles as probability functions over
independent events is unlikely to work well. The paper's ground is the flat-versus-weighted
result at F-9, which is a result about a different pair of models, carried across by argument.

**C-6 [CONJECTURE, p. 205].** That perceivers may generate a measure of the probability of the
surface itself by summing the joint scores, and that this bears on expectation. Offered as not
implausible; nothing is computed.

**C-7 [CONJECTURE, p. 203, footnote 3 at p. 205].** That the probability of a passage under the
model might reflect its tonalness. Explicitly floated as possibly interesting.

**C-8 [CONJECTURE, p. 199].** That building special rules for chromatic harmonies such as
augmented sixths might be desirable. The paper states it has not been attempted.

## §5 — Measured results, with corpus, metric and value as the paper states them

### §5.1 The one corpus, and what the ground truth is

**Corpus:** excerpts from the workbook accompanying the tonal-harmony textbook by Kostka and
Payne, references [7] and [6]. **46 excerpts, 896 segments.** The ground truth is the harmonic
analyses in the instructors' manual, done by the textbook's authors, showing keys and
modulations.

**Every number in this section comes from that one corpus.** The paper reports no second corpus,
no held-out split, no cross-validation, and **no uncertainty on any reported rate met anywhere in
the twelve pages as read** — no
spread, no significance test, no interval.

### §5.2 The empirically estimated key-profiles (Table 1, p. 201)

Proportion of segments in which each scale degree occurs, relative to the current key, collapsed
over all major keys and over all minor keys:

| Scale degree | Major keys | Minor keys |
|---|---|---|
| 1 | .748 | .712 |
| #1/b2 | .060 | .084 |
| 2 | .488 | .474 |
| #2/b3 | .082 | .618 |
| 3 | .670 | .049 |
| 4 | .460 | .460 |
| #4/b5 | .096 | .105 |
| 5 | .715 | .747 |
| #5/b6 | .104 | .404 |
| 6 | .366 | .067 |
| #6/b7 | .057 | .133 |
| 7 | .400 | .330 |

The paper reads two values out of this table in its prose and both match the table as printed:
the tonic occurs in .748 of major-key segments, and the raised fourth degree in .096 of them.

**The paper names one exception to its own stated hierarchy**: that degree 5 scores higher than
degree 1 in minor. §6.2 records what this read's own checks of the hierarchy found.

### §5.3 The three reported rates, and what separates them

| Version | Rate as printed | Key-profiles used | What was tuned on the test |
|---|---|---|---|
| Earlier key-profile model | 83.8% (751 of 896) | The hand-set values of Figure 1 | The change penalty |
| Spelling-aware variant | 87.4% | Not stated | Not stated |
| Bayesian version | 77.1% | Estimated from the test corpus itself | The change penalty |

**The count is printed for the first row only.** For the other two the paper prints a percentage
and no count, and this read derives none (§6.3).

### §5.4 What the paper says separates 83.8% from 77.1%, stated at the paper's own strength

The paper says the main difference between the two models **appears to be** that the second adds
absent-pitch-class scores to the key-profile scores. It then immediately records that the
key-profiles are also different, and that the Bayesian model's were generated directly from the
test data, so one would expect them to be optimal. It closes by saying it is unclear why this
would result in lesser performance and that the author intends to investigate further.

**So the paper does not attribute the gap to any one cause, and says so.** At least two things
move between the two rows of §5.3 — the profile values and the presence of the absent-pitch-class
terms — and the paper isolates neither.

### §5.5 The error account (p. 198–199)

Three sources, named and not quantified:

1. **Modulation rate, wrong in both directions** — the program sometimes modulated where the
   reference analysis did not, the paper offering as a possible reason that the reference treated
   the passage as a secondary harmony or tonicization instead; and sometimes failed to modulate
   where the reference did.
2. **Chromatic harmony**, augmented sixth chords named as the instance.
3. **Pitch spelling**, which is what the variant at §5.3's second row addresses.

**No share of the 145 mislabelled segments is attributed to any of the three.** The 145 is this
read's subtraction, not a number the paper prints (§6.3).

## §6 — Arithmetic this read performed on the paper's own printed values

**Everything in this section is this read's own calculation on values transcribed above. None of
it is the paper's, and where a result is a derivation rather than a transcription it is marked.**

### §6.1 The headline rate closes against its own counts

751 divided by 896 is 0.8382, which rounds to the 83.8% the paper prints. **The one rate the
paper gives a count for checks.**

### §6.2 The stated hierarchy checks at both objects, and the paper's own exception is the only one

The paper states a hierarchy — tonic highest, then the other degrees of the tonic chord, then the
other diatonic degrees, then the chromatic degrees — of Figure 1, and says it is reflected in the
Table 1 profiles as well with one odd exception, that 5 scores higher than 1 in minor.

**Checked at Figure 1.** Major: the lowest scale value (3.5) exceeds the highest chromatic value
(2.0); the lowest tonic-triad value (4.5) exceeds the highest other-diatonic value (4.0); the
tonic (5.0) is highest. Minor, on the harmonic minor scale the paper names: the same three
comparisons hold at the same values. **Figure 1 satisfies the hierarchy with no exception, in
both modes.**

**Checked at Table 1.** Major: tonic .748 is the highest value in the column; the lowest
tonic-triad value (.670 at degree 3) exceeds the highest other-diatonic value (.488 at degree 2);
the lowest diatonic value (.366 at degree 6) exceeds the highest chromatic value (.104 at
#5/b6). **The major column satisfies the hierarchy throughout.** Minor: degree 5 (.747) exceeds
the tonic (.712), which is the exception the paper names; apart from that, the lowest
tonic-triad value (.618 at b3) exceeds the highest other-diatonic value (.474 at degree 2), and
the lowest diatonic value (.330 at degree 7) exceeds the highest chromatic value (.133 at
#6/b7).

**So the paper's claim is correct at both objects and its one named exception is the only
departure this read found.** This is a positive check on a sentence that could have been loose,
and it is recorded as such.

### §6.3 Two counts the paper does not print, derived here and marked as derived

If the two remaining rates were measured over the same 896 segments — **which the paper does not
state, and which this read assumes rather than establishes** — then each percentage as printed
admits exactly one integer count:

- 77.1% corresponds to **691** of 896 (691 gives 0.7712; 690 gives 77.0% and 692 gives 77.2%).
- 87.4% corresponds to **783** of 896 (783 gives 0.8739; 782 gives 87.3% and 784 gives 87.5%).

**Both are derivations under an assumption the paper leaves open**, and neither should be carried
as a value the paper reports. 896 minus 751 gives **145** mislabelled segments for the one row
where the count is printed.

### §6.4 The gap between the two models, stated in the right unit

83.8 minus 77.1 is **6.7 percentage points**, not 6.7 per cent. The Bayesian version labels a
smaller share of segments correctly than the model it reinterprets, by that difference, on the
same corpus.

### §6.5 The two worked calculations this read met both reproduce

- **The Figure 2a key-profile total.** The C major profile values for C, D, E and F are 5.0, 3.5,
  4.5 and 4.0; their sum is 17.0, the value the paper prints. **The four values match Figure 1 as
  transcribed at §2.1**, so the worked example is internally consistent with the printed profile.
- **The four-segment structure prior.** One twenty-fourth, times 0.8, times 0.8, times 0.2
  divided by 23, gives 0.0002319, which rounds to the .000232 the paper prints.

### §6.6 Segments per excerpt

896 segments over 46 excerpts averages **19.5 segments per excerpt**. This read's division. The
paper gives no per-excerpt distribution, so nothing follows from the average about any one
excerpt's length.

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Inconsistencies and defects inside the paper

**D-1. The paper's own new distinction is named in two opposite directions, and the category
heading is the outlier.** At printed page 204 the paper proposes splitting preference rules into
two kinds: those bearing on the probability of a structure, and those bearing on the probability
of a surface given a structure. It names the second kind with a hyphenated compound that reads
surface-then-structure. It then labels the Key-Profile Rule with the compound reversed —
structure-then-surface — and later on that same page labels the Event Rule and the Length Rule
the same reversed way.

**Counted at the page rather than asserted: the category compound occurs once, and the reversed
compound occurs twice, the second occurrence covering two rules — so three rules are labelled in
the direction opposite to the category that is supposed to contain them.** All of this is on
printed page 204.

*(★ CORRECTED AT THE READ-BACK, AND THIS IS A DEGRADATION TELL OF THIS SIDE'S OWN. FORMER
WORDING, PRESERVED (#12): "the instance labels occur three times", and "on the same and the
following page". **Both were counts and locations put on this side's own reading without being
derived** — the reversed compound occurs twice, not three times, and every occurrence is on one
page, not two. The number three came from the count of RULES labelled, which is not what the
sentence said. Caught by re-opening page 204 at the read-back, before this file had landed.)*

Which of the two directions is right is decidable from the paper's own definition: the quantity
is the probability of the surface **given** the structure, which is the generative direction from
structure to surface, so **the reversed labels are coherent with the definition and the category
heading is not.** **This is a defect in the naming of one of the paper's two headline
contributions** — C-3 above — and a later reader taking the category name at face value would
have the direction backwards.

*Bound: this read checked the three compound occurrences it met on printed page 204 and did not
search the rest of the paper for further uses.*

*(★ CORRECTED AT THE USER-ORDERED CHECK. TWO FORMER WORDINGS, PRESERVED (#12): "the three
instance labels are coherent with the definition", and a bound reading "the three occurrences it
met on pages 204 and 205". **Both are sentences the read-back's own correction left stale** — it
established that the reversed compound occurs twice and that every occurrence is on one page, and
these two sentences went on carrying the superseded count and the superseded page span. This is
the same shape the previous entry of this line records: a correction that fixes its own sentence
and not its neighbours.)*

**D-2. The abstract carries the strong form of the equivalence and the body carries a weaker
one.** §2.6 sets out the difference: the body's identity is conditional on reading the earlier
model's values as logarithms, and it names one difference it does not dispose of. The
introduction's formulation that the model simply is a Bayesian model, and the abstract's that it
can be reinterpreted with a few small modifications, are both wider than what page 202
establishes.

**D-3. The abstract does not carry the direction of the measured outcome.** The reinterpreted
version measured **6.7 percentage points below** the model it reinterprets, on the same corpus
(§6.4). A reader of the abstract alone learns that a reinterpretation is available and that it
sheds light on several issues; the abstract as printed says nothing about the reinterpreted
model performing worse. **This is a defect of completeness in the abstract rather than a false
statement in it.**

**D-4. Neither reported rate is a held-out value, and the paper states both facts without
drawing the consequence.** The earlier model's change penalty was adjusted for optimal
performance on the test (F-2). The Bayesian model's change penalty was chosen the same way (F-5)
**and its key-profiles were estimated from the very corpus it was tested on** (F-4). The paper
flags the second of these against normal practice and explains why it accepted it. **What it does
not then say is what this does to the comparison between the two rates** — and the direction is
worth stating, because it cuts against the paper's own result rather than for it: the Bayesian
model's rate is the more optimistically biased of the two, and it is still the lower one.

**D-5. The one difference the paper calls significant is never isolated.** The absent-pitch-class
terms are named at page 202 as the significant difference between the two models and again as the
main difference when the measurement is reported. **At least two things change together between
the two measured rows** — those terms and the whole set of profile values — so the paper's own
measurement cannot attribute the gap to either. The paper says as much, in saying it is unclear
why, which is honest; the defect is that the comparison was run in a form that could not answer
the question the paper asks of it.

**D-6. The highest of the three reported rates is the least described.** The spelling-aware
variant's 87.4% (F-6) is given with no count and no account of how the spelling distinctions
entered the profiles. **The corpus IS named** — the same Kostka–Payne corpus — and what is not
stated is the segment count it was measured over. It is then set aside on a modelling-perception
ground (F-7) rather than a measurement one.

*(★ CORRECTED AT THE READ-BACK. TWO FORMER WORDINGS, PRESERVED (#12): "The highest number in the
paper", which was false — 896 and 751 are larger numbers in the same paper, and what was meant
was the highest RATE; and "no statement of whether it was measured over the same segments",
which was refuted by the paper's own sentence naming the corpus on printed page 199. The
remaining gap is the count, not the corpus.)*

**D-7. A comparative claim whose evidence is not in this paper.** F-9 states that flat input did
substantially better than weighted input, with no value here; the values are in reference [14].
Anything this project carries from F-9 carries that bound with it.

**D-8. A printed value in Figure 1 is missing its decimal point, in both profiles, and the trap
it sets is real.** Figure 1 prints each profile's twelve values as a label row beneath the bars.
**In both the major and the minor profile the A#/Bb entry is printed as "15"**, where every other
value in both rows carries a decimal point and where the drawn bar sits between 1 and 2 — that
is, at 1.5. This read transcribed the value as **1.5** at §2.1 on the bar height and on the
pattern of the other eleven labels, and records here that the printed label says otherwise.

*Why it is worth recording rather than silently normalised:* a later reader re-keying the profile
from the label row alone would carry **15** into a vector whose other values run from 1.5 to 5.0,
and a single value ten times the maximum would dominate every correlation the profile enters.
**The defect is typographic and the value is not in doubt** — but the transcription hazard is
exactly the kind this project's own reading pass exists to catch, and it sits in the profile
table a later reader would re-key.

*(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "the one figure a
reader is most likely to copy". **A superlative this side never derived** — no comparison across
the paper's two figures and one table was made — and it used the word *figure* in a sense this
project's Conventions reserve.)*

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

1. **The change penalty.** Its value is nowhere in the paper as read, for either model, though it
   is the one free parameter both models tune.
2. **The per-source error shares.** Three error sources are named (F-11) and none is quantified.
3. **The absent-pitch-class terms on their own.** No ablation.
4. **The profile values on their own.** No run of the Bayesian machinery on the Figure 1 values,
   or of the earlier model on the Table 1 values, which is the comparison that would separate
   D-5's two changes.
5. **The sensitivity to segmentation.** The one-to-two-second range and the smallest-metrical-
   level-above-one-second rule are stated; no sweep, no alternative segmentation, no measurement
   of what the choice costs.
6. **The modulation prior.** 0.8 for staying and 0.2 over 23 for each alternative are assumed,
   with the equal treatment of all key changes flagged by the paper as possibly an
   oversimplification. No derivation, no fit, no sensitivity.
7. **Uncertainty on any rate.** No spread, no significance test, no interval, on 46 excerpts.
8. **The probability of a surface.** Equation 9 is stated and its summands are said to be
   generated anyway; no value is computed anywhere in the paper as read.
9. **Whether the three rates share a denominator** (§6.3).

### §7.3 What is both measured and structural here

Stated at the strength the paper supports, because these are the parts a later reader could
actually carry:

- **Direction, not value: discarding repetition and duration in favour of pitch-class presence
  measured better than keeping them** (F-9), on the author's own earlier tests, reported here
  without a figure.
- **A joint labelling over the whole piece, with a cost on changing key, is tractable by dynamic
  programming** and the paper states the exhaustive alternative is not feasible. This is a
  structural claim about the search and it does not depend on any of the tuned values.
- **Ambiguity falls out of the same scores** rather than needing separate machinery: near-ties
  between analyses are what ambiguity is, in both the original and the Bayesian reading.
- **The probabilistic reinterpretation did not buy accuracy here.** Read carefully, the result is
  sharper than the paper puts it: a model whose profiles were fitted on the test set scored below
  a model whose profiles were set by hand beforehand, on that same test set (D-4). **What that
  does not establish** is that the Bayesian formulation is worse in general — the confound at D-5
  is unresolved, and one corpus of 46 excerpts with no stated uncertainty cannot carry a general
  claim in either direction.

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it did not re-open

After §0–§7 were written, the paper was re-opened at the pages carrying this extract's
transcribed values and its load-bearing claims: **printed pages 197–202 in one request, printed
page 204 in a second, and printed page 195 in a third.** Between them those pages carry Figure
1's twenty-four profile values, Table 1 whole, every reported rate and the one printed count, the
two worked calculations, the modulation prior, the equivalence passage, the rule-category
passage, and the abstract.

**Four pages were NOT re-opened at the read-back: printed 196, 203, 205 and 206.** The ground is
that **no numeric value of this extract's comes from any of them**, and it is a ground rather
than a proof. What this leaves as a real gap: several prose characterisations in §4 — C-4 and C-5
from printed 203, C-6 and C-7 from printed 205 — were written from the first whole read and
**were not re-checked at their pages.** They are the least-verified sentences in this file and a
next reader should treat them as such.

*(★ AMENDED AT THE USER-ORDERED CHECK, AND THE FORMER STATE IS PRESERVED (#12): the sentence above
was true of the read-back and **was made false afterwards by this sitting's own work.** Printed
page 203 WAS re-opened, at the cross-check, to settle the disagreement recorded at §9.3. **So
three pages stand un-re-opened — printed 196, 205 and 206 — and C-4 and C-5, which come from 203,
are no longer among the least-verified sentences; C-6 and C-7 still are.** This is cadence 8's own
case: a sentence about the sitting's own state, true when written and false while the sitting
worked on.)*

### §8.2 What the read-back and the sweep struck in this side's own writing

Named rather than counted, each corrected at its own site with the former wording preserved
(#12):

- **An identity claim whose predicate named no argument** (§1.1). It asserted that every "axis" of
  the paper's identity was at the object, where the list of axes a reader would supply is the
  bibliography row's — **a file this read never opened.**
- **A location stated from memory of writing rather than checked at the page** (§2.3): the
  segmentation caveat placed at the opening of the paper's section 4 when it stands at its close.
- **A count and a location in one sentence, neither derived** (§7.1 D-1) — see §8.3.
- **A superlative that was both underived and false** (§7.1 D-6): "the highest number in the
  paper", of a rate, in a paper containing 896 and 751 — see §8.3.
- **A claim refuted by the paper's own sentence two pages from where this side had read it**
  (§7.1 D-6): that the spelling variant's corpus was not stated. Printed page 199 names it.
- **Five absence claims stated wider than the act that produced them** — at §2.1, §3.2, §3.3, F-9
  and §5.1 — each of which said in effect *not in this paper* where what this side can support is
  *not met anywhere in the twelve pages as read*. All five now carry that bound. **This is
  cadence 7's own class.**
- **One unbounded count phrase** at §6.5, "the two worked calculations in the paper", now "the two
  this read met".

**And one candidate finding was MANUFACTURED and withdrawn before it entered the file.** This
side had drafted an observation that the paper describes a rise of 3.6 percentage points as
"slightly higher" and a fall of 6.7 points as "somewhat lower", and was going to record the pair
as an asymmetry in how it characterises movements of its own headline rate. **Checking the two
adverbs against the two magnitudes refuted it**: the milder word sits on the smaller movement and
the stronger word on the larger one, so the paper's language tracks its own numbers. The
candidate is recorded here as withdrawn rather than left unmentioned, because a defect this side
invented and then removed is evidence about this side and not about the paper.

### §8.3 The degradation tells, reported unprompted

The user's standing rule of 2026-08-15 asks this side to report its own degradation tells without
being asked. **Two of the named tells fired in this sitting's writing, and both are reported
here.**

*(★ AMENDED AT THE USER-ORDERED CHECK. **This section's account was true of what the read-back and
the sweep found, and it is no longer the whole count.** That check found a further instance of
each of the two tells named below — a second underived count at §9.3, and a second underived
superlative at §7.1 D-8 — so the tally is **two named tells, four instances**. **The two named
tells are unchanged; what was under-reported is how many times each fired.** The full account is
at §10, and this note stands here so that a reader of §8.3 alone is not left with the smaller
number.)*

**Tell A — a count put on this side's own reading without deriving it. One instance.** §7.1 D-1
stated that the reversed compound occurs "three times". **It occurs twice**; the figure three was
the number of RULES labelled, which is not what the sentence said. In the same sentence a second
claim, that the occurrences spanned two pages, was also wrong — they are all on printed page 204
— and that half is the never-work-from-memory failure rather than a count: **a location written
from the memory of writing it instead of checked at the page.** Both were caught by re-opening
page 204 at the read-back, before this file landed.

**Tell B — a superlative this side never derived. One instance.** §7.1 D-6 called the 87.4% "the
highest number in the paper". **No comparison over the paper's numbers was ever made**, and the
claim is false as stated: 896 and 751 are larger numbers in the same paper. What was meant, and
what now stands, is the highest of the three reported rates. Caught at the sweep.

**What the threshold means here, stated plainly rather than grouped away.** The rule is that when
two or more of the named tells appear, this side says so and **recommends handover at a verified
stop**. Two appeared. **That both were caught before this file landed does not lower the count** —
the previous entry in this line was corrected for exactly that grouping, filing its own tells as
ordinary defects and reporting one where three had fired.

**Where the recommendation attaches.** **The verified stop is the member boundary, and it has now
been reached** — the extract is landed and proved, the cross-check has run and is at §9, and the
closing entry carries the recommendation at its head. **The recommendation is not that work stop
mid-member** — stopping before the cross-check would have lost the twelve-page read and left the
member half-done, which is the thing a member boundary exists to prevent. **It is that the NEXT
member be taken by a fresh session.**

*(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "This sitting has not
reached a verified stop: the extract has not landed, and the cross-check against the first extract
has not run." **True when §8 was written and made false by the sitting's own next three acts** —
the landing, the cross-check and the closing entry — and it went out of date INSIDE a landed file
rather than in a draft. **Cadence 8's case, and the second instance of it in this file**, the
other being at §8.1.)*

### §8.4 The bound on this section

**This is a pass over this side's own writing, by the same side that wrote it.** It establishes
what it found and **nothing about what remains.** Two of the defects it struck — the underived
count and the underived superlative — had already survived the act of writing them and the act of
reading the paragraph they sat in, so nothing about this section's yield says the rest of the
file is clean. Four pages were not re-opened (§8.1), and the sentences resting on them are named
there.

**This section was written in the act that ran the read-back and the sweep**, not planned before
them, and no check is recorded here as run that was not run.

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

The first extract, `reading_pass/extracts/temperley-2002-a-bayesian-approach-to-key-finding.md`,
30,613 bytes, **was opened for the first time after this file had landed at 46,089 bytes** and
was then read whole. Before that point this side knew of it only that it existed, at that size
and at a matching file-name slug, from a listing of file names.

**The independence bound, stated rather than claimed away.** This read had seen row 5's candidacy
line before reading the paper, which carries a verdict and a reason (§0). It had not seen the
first extract, the progress record, the framework, the slice derivation or the findings surface.
**The correction at §2.3 — the segmentation reservation's location — was made at the read-back,
before this section opened the first extract**, which is why the agreement recorded at §9.3 is an
agreement and not a copy.

### §9.2 Every numeric value both extracts transcribed agrees, digit for digit

Checked value by value, not by impression:

- **Figure 1, the C major profile** — all twelve values.
- **Figure 1, the C minor profile** — all twelve values.
- **Table 1, the major column** — all twelve values.
- **Table 1, the minor column** — all twelve values.
- **The evaluation numbers** — 46 excerpts, 896 segments, 751 correct, 83.8%.
- **The other two rates** — 87.4% and 77.1%.
- **The modulation prior** — 0.8, 0.2 divided by 23, the initial one twenty-fourth over 24 keys,
  and the worked four-segment value .000232.
- **The held file's size** — 85,400 bytes — and the page count and printed pagination.

**Forty-eight profile values and every reported number: no disagreement anywhere.**

### §9.3 The disagreements, and the direction is not symmetrical

**One disagreement goes against the first extract, and it is a word inserted inside a quotation.**
That extract quotes the paper's flat-versus-weighted sentence with the word *for* before "the
weighted-input model". **Resolved at printed page 203: the paper does not print that word** — it
reads "better performance for the flat-input model than the weighted-input model", the comparison
carrying one *for* and not two. **No value moves**, and the sense is unchanged.

**That file is untouched**, on the standing ground that rewriting another read's text destroys
what the doubling compares. **Whether it is corrected at its own site is the user's**, and it is
the **seventh** item of that shape now standing with him — rows 27, 28, 1, 8, 26 and 30 carry the
other six.

*(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "the sixth item of that
shape". **A count put on this side's own reading without deriving it** — the previous entry's
watch line records six items standing before this member, so row 5's makes seven. **This is a
third instance of the count tell, and it is recorded at §8.3 and at §10.** It also put this file
in disagreement with this sitting's own closing entry, which says seven.)*

**Nothing in the cross-check goes against this side.** Stated exactly: no claim of this extract
was refuted by the first extract or by the pages re-opened to settle the comparison. **That is
not a claim that this file is clean** — §8.4 says what it is worth — and two of this side's own
defects had already been struck before the first extract was opened at all.

**And one thing the first extract got right that a careless reader would have silently repaired.**
The paper's own sentence reporting the Bayesian rate carries a small grammatical slip — an
article missing before "correct rate of the earlier version". **The first extract quotes it as
printed, slip included.** This read paraphrased the sentence rather than quoting it, so the
question did not arise here; it is recorded because the opposite act — tidying a printed slip
away inside a quotation — is the defect the previous member of this line found in itself.

### §9.4 What the doubling produced that neither read had alone, in both directions

**Only in this read:**

- **The rule-direction inconsistency (§7.1 D-1).** The first extract quotes the paper's instance
  label correctly and **adopts it as the name of the category in its own heading**, so it does
  not carry the paper's own contrary category wording and does not record that the two disagree.
  The inconsistency is therefore invisible in that extract — not misquoted, unnoticed.
- **The missing decimal point in Figure 1 (§7.1 D-8).** Both extracts transcribe the value as
  1.5, so both silently normalised the printed label; **this read is the one that noticed and
  said so.** The transcription hazard is recorded nowhere else this side has seen.
- **The arithmetic of §6** — the hierarchy verified at both objects, the two counts derivable from
  the unprinted rates, the gap stated as percentage points, the segments-per-excerpt average.
- **That the abstract carries no word of the measured drop (§7.1 D-3).**
- **That the lower of the two rates is also the more optimistically biased one (§7.1 D-4)** — the
  Bayesian model's profiles were fitted on its own test corpus, so its 77.1% is the more
  favourably biased of the two rates, and it still came in 6.7 points below.

**Only in the first extract, and this read takes no position on any of it:**

- **The whole record-side half.** That extract reaches `FRAMEWORK.md`'s L0 bullet and its [FACT],
  the findings surface's verification row, the bibliography row, the slice derivation's placement
  of row 5, and a repository-wide search for the paper's values; it routes each of its findings
  to a design point and argues centrality with its rival ground stated. **This side opened none
  of those objects, so on that half this is not a second opinion but silence.**
- **The paper's structural inventory** — two figures, one table, nine numbered equations, sixteen
  references, three footnotes. **This read checked all five counts against the pages and all five
  hold**, which is a positive check this read can offer on that extract rather than a finding.
- **The claim that this is the only held primary of its family**, which turns on the held set and
  was checked at no object here.
- **The verbatim quotations**, which that extract carries in far greater quantity than this one.

### §9.5 What the cross-check does NOT establish

It compared what both files carry. **A claim present in only one of them was not tested by the
comparison** — it was at most checked at the paper, and only where this read went back to the
page. Nothing here establishes that the first extract's record-side half is right, and nothing
establishes that this read's §7 findings are complete.

## §10 — The user-ordered fact- and source-check, run after this file had landed twice

The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes:
completeness, coherence, correctness, and misuse of hyperbole and absolutes. **This file was
re-read WHOLE as landed at 52,386 bytes, at the device's own copy staged back**, and what follows
is what that reading found. Every correction is made at its own site with the former wording
preserved (#12).

### §10.1 Two sentences about this sitting's own state had gone false inside a landed file

**Both are cadence 8's case, and both were true when written.**

- **§8.1's list of pages not re-opened.** It named four; printed page 203 was then re-opened at
  the cross-check, leaving three. The consequence it drew — which sentences are the least verified
  in this file — moved with it, and C-4 and C-5 are no longer among them.
- **§8.3's statement that the sitting had not reached a verified stop.** It was written before the
  landing, the cross-check and the closing entry, and all three then happened. **This is the more
  serious of the two**, because it is a statement about whether a rule's threshold condition had
  been met, standing in the section that reports that rule.

### §10.2 Two further instances of the two tells already named at §8.3

**Tell A, a count put on this side's own reading without deriving it — a SECOND instance.** §9.3
called row 5's item *"the sixth item of that shape"* standing with the user. **It is the seventh**
— the previous entry's watch line records six before this member. **The count also put this file
in disagreement with this sitting's own closing entry**, which says seven, so the defect was
visible from outside the file as well as inside it.

**Tell B, a superlative this side never derived — a SECOND instance.** §7.1 D-8 closed by saying
the transcription trap sits in *"the one figure a reader is most likely to copy"*. **No comparison
across the paper's two figures and one table was made**, and the sentence also used a word this
project's Conventions reserve for figuration.

**So the tally at this check is two named tells and FOUR instances**, against the two instances
§8.3 reported. **The under-report was of how often each tell fired, not of which tells fired** —
and it is recorded here in those terms rather than smoothed, because the previous entry of this
line was corrected for an undercount of exactly this kind and its correction records that
undercounting one's own tells is itself the class being undercounted.

### §10.3 A correction that left its neighbours stale

The read-back's correction at §7.1 D-1 established that the reversed compound occurs twice and on
one page. **Two sentences in the same finding went on carrying the superseded count and the
superseded page span** — the sentence deciding which direction is right, which still said "the
three instance labels", and the bound, which still said "pages 204 and 205". Both are corrected
now. **The shape is one the previous entry of this line records: a correction that fixes its own
sentence and not the sentences around it.**

### §10.4 Reserved vocabulary, corrected where this read introduced it

`CLAUDE.md`'s Conventions reserve the bare word *figure* for figuration and require the numerical
sense to be written as *number* or *value*. **This read had introduced that collision, and the
sites are named rather than counted:** §5.1's opening sentence, §5.5's closing clause, the
correction note at §7.1 D-1, D-4 twice, D-7, D-8, §9.2's evaluation bullet, and §9.4 twice. Each
is corrected. The §9.4 passage also used *"thumb on the scale"*, a second reserved word, and is
reworded. **Uses of *Figure 1* and *Figure 2a* as the paper's own object names are not collisions
and are left.**

*(★ This bullet was itself written with a total in it — "in seven places" — and the total was
wrong. **It is corrected before landing, and it is recorded rather than quietly fixed**, because a
miscount inside the paragraph reporting this side's miscounts is the same defect the previous
entry of this line records finding in itself: a count tell written inside the very sentence
reporting a count tell. Cadence 6 asks for the members to be named, and they now are.)*

### §10.5 Two defects of completeness and coherence

- **§0 undercounted this side's own boot reading** — four entries whole and parts of four others,
  not "parts of two older ones" — and **overstated what touched row 5**, where two of those
  entries name row 5 as next in the reading order.
- **§2.1 named reference [14] twice in adjacent sentences**, a redundancy the read-back's own edit
  introduced. One naming now stands.
- **§1.4 carried a hedged assertion about an unexamined thing** — that the candidacy row's
  spelling measurement is "almost certainly" this paper's 87.4% — one clause after saying this
  read takes no position on it. The guess is withdrawn and the question left where it belongs.
- **§3.2 carried a list item whose continuation lines had lost their indentation**, breaking the
  list. Formatting only; corrected.

### §10.6 What this check did NOT do, and what it does not establish

It re-read this file and nothing else. **It fetched no page image, re-opened no page of the paper,
did not re-open the first extract, ran no web access and swept no repository.** It changed **no
value this extract takes from the paper**: every profile value, every rate, every count, every
page location and every transcribed table stands exactly as landed.

**And it is a further pass over the same writing by the same side.** Two of the defects it found
had already survived the writing, the read-back, the sweep, two landings and a cross-check — one
of them a false statement about whether this sitting had met a rule's own threshold — **so nothing
about this check's yield says the remainder is clean.**
