# EXTRACT — Raphael & Stoddard 2003, "Harmonic Analysis with Probabilistic Graphical Models" — Task B candidacy row 1, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All five pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints no page numbers; every location below is given as the page's position in the
> held file (p. 1 to p. 5) and the paper's own section.
>
> **Why this paper and its place in L2's slice.** It is row 1 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"A method that decides tonality and chord together over a score. Directly a
> candidate for L2's one entangled decision (§5, L2). The commission's hypothesis names it."*
> `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 places it in L2's slice: *"Decides tonality and
> chord together over a score — L2's entangled decision (the row's own words)."* It is third in group 1
> of the proposed reading order ("the joint tonality-and-chord decision"), after rows 27 and 28. Row 2
> — the same authors' 2004 journal account — is *"Paywalled and not held"* (`candidacy_upgrades.md`
> row 2) and is not read; nothing here is carried as a claim about it. Ruling 1 of
> `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before L2's slice
> of Task B is read. This is the third member of that slice read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Christopher Raphael and Josh Stoddard (Dept. of Mathematics and Statistics, Univ. of Massachusetts,
Amherst), "Harmonic Analysis with Probabilistic Graphical Models", ISMIR 2003 (the permission block
reads *"© 2003 Johns Hopkins University"*), five pages, five sections (Introduction; The Model;
Training the Model; Experiments; Extending the Model) and seven references. Keywords as printed:
*"harmonic analysis, music, probabilistic graphical model, hidden Markov model"*.

**File:** `docs/research_papers/raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf` (93,277 bytes
at the listing).

## Claims, labeled

### What the method decides, and how it decides it jointly

**★ [FACT, p. 1, Abstract]** *"A technique for harmonic analysis is presented that partitions a piece of
music into contiguous regions and labels each with the key, mode, and functional chord, e.g. tonic,
dominant, etc. The analysis is performed with a hidden Markov model and, as such, is automatically
trainable from generic MIDI files and capable of finding the globally optimal harmonic labeling."*

**★ [FACT, p. 2, §1] The joint decision is the authors' own stated point of difference:** *"Another
significant difference between our approach and all others we know is our simultaneous recognition of
chord and key. The hope here is that the more structured sequence of chord functions (e.g. tonic,
dominant etc.) will help guide the analysis when the choice of chord (e.g. c major triad, f minor triad,
etc) is ambiguous."*

**★ [FACT, p. 2, §2] The label is a TRIPLE of tonic, mode and scale degree — the chord is named relative
to the tonality, not absolutely.** Each period is labelled with an element of
L = T × M × C = {0, …, 11} × {major, minor} × {I, II, …, VII}, *"where T, M, C stand for tonic, mode,
and chord. For instance, (t, m, c) = (3, major, II) would represent the triad in the key of 2 = d major
built on the II = 2nd scale degree which contains pitches e, g, b."* Upper and lower case numerals are
not distinguished. Modes are *"the basic major and harmonic minor"*; chords in the discussion are *"the
seven basic triads"*; **inversion is not modelled** (*"We do not currently model chord inversion in
this work"*). **Secondary function is represented as a change of key, not as an applied chord:** the
progression c major, d major, g major in c major *"can be represented as (c=0, major, I), (g=7, major,
V), (g=7, major, I). Clearly our representation allows for a rich variety of secondary functionality
while avoiding murky distinctions between secondary function and actual modulation."*

**★ [FACT, p. 2, §2] The unit of decision is a FIXED metrical period, chosen in advance.** *"Our
harmonic analysis is performed on a fixed musical period, q, say a measure (q = 1) or half measure,
(q = 1/2). To this end we partition the pitches in our musical composition into a sequence of subsets
y₁, …, y_N where yₙ is the collection of pitches whose onset time, in measures, lies in the interval
[nq, (n+1)q)."* The analysis is on **pitch class only**: *"since MIDI does not use enharmonic
spellings, we do not model them."* The labels form a homogeneous Markov chain, p(xₙ₊₁ | x₁, …, xₙ) =
p(xₙ₊₁ | xₙ); the pitches of a period are an observation whose distribution depends only on that
period's label (the HMM assumptions, p. 2).

**★ [FACT, p. 3, §2.1] The transition probability is factored so that the coupling between tonality
and chord is a CONDITIONAL, never a constraint.** Equations (1)–(2): p(x' | x) = p(t', m' | t, m, c) ·
p(c' | t', m', t, m, c), simplified to p(t'−t, m' | m) times q²_c(c' | c) when the key is unchanged
(t' = t, m' = m) and q¹_c(c') otherwise. The three simplifications are stated as assumptions and
defended one by one: the key change does not depend on the current chord; it is translation-invariant
(*"as one who does not have perfect pitch and hears only relative pitch movement, this and other pitch
translation invariance assumptions seem unassailable"*); chord transitions within a key do not depend
on the key (*"the probability of moving from I to V is the same in both major and minor modes"*); and
on a key change the new chord is drawn *"at random without regard for the new or old keys"* — of which
the authors write *"We doubt this particular assumption would hold up under empirical investigation."*
The parameter count falls from (12 × 2 × 7)² = 28 224 to 12 × 2 × 2 + 7 × 7 + 7 = 104. **No chord is
excluded under any tonality; every one of the 168 labels is reachable at every period.**

**★ [FACT, p. 3, §2.1] The emission is PER PITCH, by the pitch's category relative to the label, with
the metrical position as a covariate.** Each pitch y^k of a period is assigned a category d(y^k, x) ∈
{1, …, 5}: root, third, fifth of the chord; in the scale but not the triad; otherwise. The output
probability is p(y | x, r) = ∏ₖ q_o(d(y^k, x) | r^k) / V(d(y^k, x)), where V(d) is the number of
chromatic pitches in the category (V(1) = V(2) = V(3) = 1; V(4) = 4; V(5) = 5) and r^k is the pitch's
metrical position category — *"0 if y^k occupies the start of a measure, 1 if y^k begins on the 2nd
half note of the measure, 2, if y^k lies on the 2nd or 4th quarter note positions, etc. with a final
category 3 for 'other'"* (p. 3; a later sentence on the same page writes r ∈ {0, …, 5} and counts 5 × 6
= 30 output parameters — both statements are as printed). The motivation: *"we anticipate that chord
tones are more likely to occur on rhythmically strong beats than weak ones. Rather than trying to
quantify such a notion directly, we simply allow the output distributions to depend on the known
measure positions in a manner we will learn from data."* The authors name the conditional independence
of pitches given the label as *"among the most problematic"* of their assumptions, because *"the
order in which pitches appear clearly affects one's harmonic perception."*

**[FACT, p. 3–4, §3] Training is UNSUPERVISED, by the forward-backward (Baum-Welch) algorithm on
unlabeled MIDI**, and this is stated as the reason for the probabilistic form: *"Our preference for the
HMM, and, more generally, probabilistic graphical models, is partly due to the way the model parameters
… can be trained from unlabeled examples."* The re-estimation formulae for q_o and q²_c are given
(p. 4).

**[FACT, p. 4, §4] Decoding is the GLOBAL maximum by dynamic programming**, x̂ = arg max p(x | y) =
arg max p(x, y), with the recursion written out; *"While in many applications the dynamic programming
recursion is approximated with a 'beam search', the size of our state space allows for full-fledged
dynamic programming."*

### The experiments, as stated

**[FACT, p. 4–5, §4]** Training on *"around 5 or so short movements"*, *"around 5 iterations"*,
learning q_o and q²_c; *"The remaining parameters of the transition probabilities, q_t and q¹_c, seem
to require larger training sets to be reliably estimated; we have set these parameters by hand in the
experiments here."* Three worked examples, published on the web: Haydn Piano Sonata 6 first movement,
Chopin's Raindrop Prelude Op. 28 no. 15, and the Prelude from Debussy's Suite Bergamasque — all in 4/4
*"to facilitate a uniform definition of the rhythm variables"*. Harmonic transitions were allowed only
at 2-beat boundaries in the Haydn and Chopin; *"This was relaxed to 1 beat boundaries in the Debussy
example, and results in a somewhat overanalyzed labeling."* In these experiments the dominant 7th was
added to the seven triads; *"Some basic extensions, such as fully diminished 7th chords and chords in
minor mode built on the flat seventh scale degree, are needed in these experiments; however, more exotic
additions such as augmented sixth chords, and Neapolitan chords are possible."*

**★ [FACT, p. 5, §4] NO MEASURED RESULT IS REPORTED, by the authors' own statement:** *"At this point we
do not offer any objective measure of success, such as 'error rate,' or comparison of our results. This
is due, in part, to the difficulty in defining and obtaining 'correct' harmonic analyses."* The
examples *"are representative of the more successful applications of our program … The less successful
results seem to mostly be compositions with very sparse textures."*

### The proposed extension (§5)

**★ [FACT, p. 5, §5]** *"To our mind, the most troubling modeling assumption we make is the conditional
independence of pitches … This assumption disregards the way music is usually composed of independent
parts or voices that obey an internal logic such as a preference for scales and arpeggios. Given the
often unvoiced nature of MIDI data and our current focus on piano music, we have begun with a simple
model that does not require voicing information. However, we now propose a model that regards the data
as a collection of voices where the evolution of each voice is conditionally independent of the others,
given the harmonic state."* On obtaining voices: *"Automatically partitioning MIDI data into voices is,
no doubt, a challenging problem … But it is rather simple to create an algorithm that performs
reasonably … We assume here that we begin with voiced data, either from an official or algorithmic
source."* In the proposed model each voice's pitch depends on the (key, chord) pair and on that voice's
previous pitch (Figure 5, two voices); *"Such a model, suitably trained, would understand a voice's
preference for scales within the key, arpeggios within the (key,chord) pair, and tendencies regarding
the resolution of non-chord tones."* It *"has a linear structure amenable to an analogous training
algorithm"* and is *"every bit as computationally tractable as the HMM."* **The extension is proposed;
no result of it is reported.**

## Measured results, as the paper states them

**None.** The paper reports no corpus, no metric and no value; see the quotation at §4 above. Its
evidence is three published worked examples and the authors' qualitative characterisation of them.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** MIDI with pitch and onset time and a known metre — *"any
collection of MIDI files that explicitly represent both rhythm and pitch can be used for training … the
case for most MIDI files that do not come from actual performances"* (p. 3). Pitch class only; no
spelling, no voices (the base model), no dynamics, no duration beyond onset-in-period membership, and
**a fixed period grid chosen in advance** (measure, half-measure, or a beat), so every harmonic boundary
lies on that grid. The metrical position of each onset is a covariate the model reads.

**What it HANDS downstream.** Per period, one label — tonic, mode, and chord as a scale degree
(seven triads plus, in the experiments, the dominant seventh and a few extensions) — as the single
globally optimal labelling; on the web, a MIDI file with the chords superimposed and text messages
*"giving the harmonic label as a (roman numeral, tonic, mode) triple"* at each chord change. Each pitch
is implicitly categorised as root, third, fifth, scale tone or other under the winning label, but that
categorisation is inside the emission and is not published as an output. It hands on **no** inversion
or bass, no applied-chord label (secondary function appears as a key change), no chord-tone assignment
as a published fact, no cadence, no figured bass, and **no alternatives or confidences** — the
forward-backward posteriors p(xₙ | y₁ … y_N) exist inside training (p. 4) but the output is the single
Viterbi path.

**Its own STATED SCOPE and limits.**
- **Vocabulary:** 12 tonics × {major, harmonic minor} × seven diatonic triads (168 labels); the
  experiments add the dominant seventh and *"some basic extensions"*; *"the choice of possible chords
  is somewhat arbitrary"* (p. 5).
- **Granularity:** a fixed metrical period; a finer period *"results in a somewhat overanalyzed
  labeling"* (p. 5).
- **Fitting:** unsupervised, from about five movements; two of the four parameter families hand-set.
- **Evaluation:** none, by the authors' statement.
- **Named weaknesses (§5):** conditional independence of pitches; no voice structure; sparse textures
  the weak case; the key-change-then-random-chord assumption doubted by the authors themselves (p. 3).

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (as a shape, the reference instance):** the joint (tonic, mode, degree) hidden state decoded
  as one globally optimal path — the shape the framework's alternative (f) names as *"the reference
  joint model of Raphael and Stoddard"* and the shape of D-001. **The chord axis as a scale degree
  relative to the state's own tonic and mode** is exactly D-526's form, and this paper is a published
  precedent for it, with the derived absolute chord *"(2 = d major … contains pitches e, g, b)"* read
  off from the triple.
- **Adopt (as the charter's boundary condition, exhibited):** the tonality–chord coupling as a
  conditional probability in the path — every label reachable, none vetoed.
- **Adapt (for DP-D and D-527's shape):** the per-pitch emission by category relative to the label
  (root / third / fifth / scale tone / other), conditioned on a chord-independent metrical covariate
  learned from data rather than hand-weighted. This is a per-tone category emission conditioned on a
  metric covariate — the same shape as the record's own emission design — published in 2003 with the
  authors' stated reason for the covariate.
- **Adapt (for DP-P, the fitting question):** the paper's own accounting of what an unsupervised fit
  on a small corpus could and could not learn — output and within-key chord transitions learned;
  key-change and cross-key chord parameters hand-set for want of data — and its translation-invariance
  argument for pooling key transitions by interval.
- **Adapt (a representational choice the detail specification must take a position on):** secondary
  function as a brief key change rather than an applied-chord label. The L2 charter publishes the
  chord *"as degree, quality, figure and applied target"*, so the charter has already taken the
  opposite position; this paper is the published argument for the other side (*"avoiding murky
  distinctions between secondary function and actual modulation"*), which the specification's defense
  should meet.
- **Must argue against:** the fixed metrical period as the unit of decision (L2's boundaries are a
  subset of L1's change points, not a grid — and the authors themselves report the grid's granularity
  visibly changing the labelling); pitch class without spelling (L0 gives spelling); the base model's
  independence of pitches with no voice structure (the voices are in the file here); the single-path
  output with no rivals and no confidence; and the absence of any measured result to weigh.

## ★ Findings, routed and not applied

**(1) The L0 boundary condition's [FACT] about this paper is a slight OVER-STATEMENT, and is
recorded as a wording precision, not a correction that moves anything.** `FRAMEWORK.md`'s "Voice
membership is given" bullet reads *"Raphael and Stoddard proposed extending their model with a
per-voice dependency and could not, because it would have required voice separation first. [FACT —
stated in their 'Extending the Model' section.]"* (line 1536 at this reading). At the object, §5 states
the proposal, calls voice partitioning *"a challenging problem"* while adding that *"it is rather simple
to create an algorithm that performs reasonably"*, and then **assumes voiced input** — *"We assume here
that we begin with voiced data, either from an official or algorithmic source."* The paper does not say
they *could not*; it says the extension is proposed and unreported, and that it starts from voiced
data. The bullet's conclusion — that voice-leading evidence needs a voice-separation stage on MIDI and
none here — is untouched, and the bullet is a boundary-condition statement rather than a chosen design
point's ground, so **no verdict moves and no STOP fires**. ROUTED to the user with the other routed
wording findings; `FRAMEWORK.md` is untouched.

**(2) Alternative (f)'s provenance and establishment are REPRODUCED at the object, with one bound
added.** `FRAMEWORK.md`'s alternative (f), "One undivided joint decision", names this paper as the
reference joint model and grades its establishment *"the strongest in the literature"* (line 1613). The
paper IS the joint decision in its purest published form. **But it reports no measurement at all**, by
its own statement; whatever establishment the joint form has in the literature comes from the systems
descended from it, not from this paper's own results. Recorded so a later reader does not take the
reference paper for a measured one.

**(3) DP-C — a fixed-grid "before" instance with the authors' own observation of the grid's effect.**
The system decides segmentation before the harmonic decision, on a metrical period chosen per piece,
and the authors report that moving the period from two beats to one *"results in a somewhat
overanalyzed labeling"* — an unvalued statement that the grid's granularity, not the music, changed the
analysis. ENRICHES-shaped for the chosen "with"; not a falsifier. Routed to the findings surface's DP-C
block and to L2's detail specification.

**(4) A published precedent for the record's own emission shape, not currently cited by the record
for it.** The per-pitch category emission conditioned on a chord-independent metrical covariate (§2.1)
is the shape of D-527 (each tone emitted by category, conditioned on chord-independent covariates)
and bears on DP-D. The record cites this paper for its joint decision and for its voice remark, not for
this. Routed to L2's detail specification as a FACT of this paper — a precedent, not a measurement.

**(5) The secondary-function representation is a published position the detail specification must
meet.** Stated under "Adapt" above. Routed to L2's detail specification.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point: the joint decision is
exhibited, the coupling is soft, the grid is the rival at DP-C and its author reports its cost in words.
**No STOP fires** under the remedial commission's §5.

## Centrality

**CENTRAL.** The framework names this paper as the provenance of alternative (f) and cites its §5 as a
[FACT] in an L0 boundary condition, and an L2 detail specification would adopt its scale-degree chord
axis and its per-tone category emission as precedents and argue against its fixed grid. A second
independent extraction under the original commission's §4 central-source rule is therefore **owed**; its
decisive questions are finding (1)'s wording and whether any measured value exists anywhere in the
paper. It has not been performed and is recorded here as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (5) are routed and written
nowhere else. It does not read row 2 (the 2004 journal account), which is not held. It opens no code,
touches no measurement tool, no corpus, no golden and nothing under `tools/`. It writes no open-items
row and allocates no decisions-register identity. It reads no other paper and takes no decision about
the order of the remaining slice.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_thirteen.md` and performed the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer), in the same sitting
that read row 28. Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` rows 1 and
2 and its hypothesis line, `cowork_l2_task_b_slice_derivation_2026_09_05.md` row 1,
`docs/research_papers/BIBLIOGRAPHY.md` rows for both Raphael & Stoddard papers, `FRAMEWORK.md` at the
"Voice membership is given" bullet (lines 1530–1541) and at alternative (f) (lines 1610–1621) — both
located with `Grep` on the staged copy — and `cowork_reading_pass_findings_2026_08_31.md`, which a `Grep`
for the authors' name found does not mention this paper. The paper itself was read at the object as
page images, all five pages. No shell command was run on the repository or on any staged copy of it for
content or for listings. No figure of this project's own measurement is restated (#17f, D-431); every
value above is the paper's own.*
