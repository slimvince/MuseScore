# Row 8 — SECOND INDEPENDENT EXTRACTION

**Temperley, David — "A Unified Probabilistic Model for Polyphonic Music Analysis",
*Journal of New Music Research* 38(1), 2009, pp. 3–18.**

Held at `docs/research_papers/temperley_2009_jnmr_unified_probabilistic_polyphonic_analysis.pdf`,
1,444,387 bytes at a bridge listing of `docs/research_papers/`. **Read AT THE OBJECT, as page images
with the file tools, whole — all sixteen pages.**

**★ HOW PAGES ARE CITED BELOW.** The held file has **sixteen** pages; the journal's own pagination runs
**3 to 18**. Held page 1 carries printed page 3, so **held page *n* is printed page *n* + 2**, and held
page 16 is printed page 18 — which closes exactly on the journal's stated range. **Every page citation
below is the PRINTED page number**, and the correspondence above is what converts it.

---

## §1 — What this file is, and the bound on its independence

This is the **second** of the two independent extractions the reading-pass commission's §4 requires of
a CENTRAL source: *"CENTRAL sources … are extracted in a SECOND independent pass (a fresh session, or
a cleanly separated re-read that does not consult the first extract) and the two extracts
cross-checked; disagreements are resolved at the paper or recorded as unresolved."*
(`cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, read whole at the object this
sitting.)

**The route taken is the second one — a cleanly separated re-read in a session that has not opened the
first extract.** **It was not opened before §1 through §8 of this file were written.** The cross-check
against it is a later section of this file, written after this one had landed.

**THE CONTAMINATION, DECLARED RATHER THAN CLAIMED AWAY.** What this side held about this paper before
it opened it, and from where:

- **`reading_pass/candidacy_upgrades.md` row 8**, read at that row's line to learn what row 8 IS:
  *"Temperley, JNMR 38(1) 2009, a unified probabilistic model for polyphonic music analysis"*, held,
  **ADMITTED**, with the reason *"The unified probabilistic model the hypothesis names; it is also V4's
  primary, but it is admitted for its method."* **So this side knew before reading that the record
  treats this paper as a verification target for some figure, and that its admission rests on its
  METHOD rather than on that figure. It did not know which figure, and did not look.**
- **`cowork_reading_pass_remedial_commission_2026_08_31.md` §3's starting hypothesis**, which that
  document itself calls *"the writing side's reading of the bibliography, not an established set"*,
  names *"the unified probabilistic polyphonic model, as joint-decode designs"* among the papers it
  expects the derivation to admit.
- **The hundred-and-seventieth handoff entry's §1**, which places row 8 second in the table's reading
  order after row 1 and says nothing else about it.

**None of these was used as a finding, and none is repeated below as though this reading produced
it.** What this side did NOT hold when it read: the first extract's text, the progress record's row 8
(**the progress record was not opened at all in this sitting**), the identity of the verification
target the candidacy row alludes to, `FRAMEWORK.md`'s treatment of this paper, and the findings
surface.

**★ ONE FURTHER CONTAMINATION, AND IT IS PECULIAR TO THIS SITTING.** This side read **row 1 — Raphael
& Stoddard 2003 — whole at the object, and extracted and cross-checked it, immediately before opening
this paper.** **This paper's body cites Raphael & Stoddard by name three times** — **printed pages 3, 4
and 11**, the three §5.4 quotes below — and one of those citations characterises their method. *(★
CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED (#12): "This paper cites Raphael &
Stoddard by name three times (pages 3, 6 and 11)". The middle page was wrong — the characterising
citation is on printed page 4, as §5.4 says — and "cites" is now bounded to the body, the reference
list on page 18 carrying a fourth appearance.)* **So this side came to those sentences already holding
a whole independent reading of the paper they describe.** That is not a bound on what this extract may
say about THIS paper; it is declared because §5.4 below compares the two, and a reader should know the
comparison was made by someone who had just read the other one rather than by someone meeting it here.

**The page count was established AT THE TOOL**, by a deliberately out-of-range page request, which
answered *"PDF has 16 pages"*. **Each of the sixteen page images was checked to be present and legible
at the image itself, not at the call's success line** (the standing page-image-fault cadence).

**The identity was checked before anything was extracted.** Printed page 3 carries the running head
*Journal of New Music Research, 2009, Vol. 38, No. 1, pp. 3–18*, the title *A Unified Probabilistic
Model for Polyphonic Music Analysis*, the author *David Temperley*, the affiliation *Eastman School of
Music, University of Rochester, USA*, and *DOI: 10.1080/09298210902928495 © 2009 Taylor & Francis*.
`reading_pass/candidacy_upgrades.md` row 8 names *"Temperley, JNMR 38(1) 2009"*. **They match, so no
identity finding.**

**A POINTER THE PAPER ITSELF SUPPLIES AND THIS READING DID NOT FOLLOW.** Footnote 1 on printed page 3
reads *"The source code for the implementation of the model, which is written in C, can be downloaded
at www.theory.esm.rochester.edu/temperley/melisma2."* **No web access of any kind was made in this
sitting**, so nothing is asserted about that address, and **no claim below rests on the code** — the
extract is of the paper.

---

## §2 — What the paper is, in plain words

Temperley proposes one probabilistic model that does three jobs at once on a piece of symbolic music:
it finds the beat structure, it finds where the harmony changes and what root each stretch has, and it
groups the notes into separate melodic lines. His argument for putting all three in one model is that
they depend on one another — harmony changes on strong beats, and a note's rhythmic weight depends on
which line it belongs to — so a model that does them separately cannot use what each one knows about
the others.

The model is stated as a **generative story**: first a metrical grid is produced, then a harmonic
segmentation and a set of melodic lines given that grid, then the actual notes given all three. Because
the story assigns a probability to any combination of structures and notes, the same machinery answers
a second question: how probable is this pattern of notes in the first place? That second answer is
what he wants for a transcription system, where you are choosing among the note patterns an audio
signal might contain.

The analysis then runs the story backwards to find the most probable structures for a given pattern of
notes. He is explicit that this search cannot be done exactly and that several steps are
approximations.

He tests the metrical part and the harmonic part against an earlier non-probabilistic system of his
own on a corpus of 46 annotated classical excerpts, and reports both results. The stream part he does
not test at all, and says why. The transcription system the second half of the paper describes is not
finished.

**Nothing in this section is a finding.** It is the orientation a reader needs before §3.

---

## §3 — The model, transcribed at the pages

### 3.1 What goes in and what comes out (page 4)

**Input:** *"a MIDI or 'piano-roll' representation—a list of notes indicating the on-time and off-time
(in milliseconds) and pitch of each note."*

**Three outputs**, each defined at the page:

- **Metrical structure** — *"Following a widely used convention (Lerdahl & Jackendoff, 1983), I define
  a metrical structure as a framework of levels of beats … Generally (at least in Western music), every
  second or third beat at one level is retained at the next level up; beats at each level tend to be
  roughly evenly spaced, but not exactly so, at least in human performance."*
- **Harmonic structure** — *"a segmentation of a piece into time-spans labelled with chords; **for our
  purposes the labels are simply roots**, though they could also carry more specific information, e.g.
  chord quality (major versus minor) or relationship to the key (e.g. 'I of C major')."*
- **Stream structure** — *"a grouping of the notes of a polyphonic texture into melodic lines (also
  called streams or voices)."* *"I assume that the number of active streams within a piece may
  fluctuate; thus streams are allowed to begin and end within the piece."*

**★ The harmonic output is a ROOT PER SEGMENT AND NOTHING ELSE.** No quality, no key, no Roman numeral,
no inversion, no figure. The paper says in that same sentence that the labels *could* carry more, and
returns to the point in its conclusions (§3.8 and 5.3 below).

### 3.2 The measured ground for coupling meter and harmony (page 4, Table 1 on page 6)

The paper's evidence that harmony changes on strong beats, stated first in prose and then as a table:

> *"If we define the tactus level as level 2, the level immediately above as level 3, and the level
> below as level 1, changes of harmony occur on about 71% of level 3 beats, 22% of level 2 beats
> (which are not level 3 beats), and only 2% of level 1 beats."*

**Table 1 (printed page 6), *"Harmonic changes at beats of different metrical levels in the
Kostka–Payne corpus"*:**

| Metrical level (2 = tactus) | % of beats with changes of harmony |
|---|---|
| 3 | **71.5** |
| 2 | **22.3** |
| 1 | **2.4** |

*(The prose's "about 71%", "22%" and "only 2%" agree with the table's 71.5, 22.3 and 2.4 — this side's
check. **The prose's parenthesis is load-bearing and is quoted in full above**: without *"(which are
not level 3 beats)"* the three figures would not be a partition, because in a metrical hierarchy every
level-3 beat is also a level-2 beat. See §9.4.)*

**★ THE TABLE HAS NO ROW FOR LEVEL 0, AND THE MODEL HAS ONE.** The grid is *"four levels, numbered 0
through 3"* (page 6), and Table 1 reports levels **3, 2 and 1** only. **So the evidence offered for
restricting harmonic change to tactus beats covers one of the two sub-tactus levels the restriction
excludes, and is silent about the other.** *(This gap was not in this extract's first writing; it came
from the cross-check — see §9.3.)*

The paper defines the tactus in the same passage: *"an intermediate level in the metrical hierarchy,
usually corresponding to what is informally called the 'beat'—most often the quarter-note."*

**The coupling is stated as running BOTH ways** (page 4): *"In Temperley (2001), in discussing the
metrical analysis model presented there, I noted that many of the model's errors were due solely to
its ignorance of harmonic structure … From a probabilistic viewpoint, this two-way interaction makes
sense: if a strong beat indicates a high probability of a harmonic change, it is hardly surprising
that the clear presence of a harmonic change would suggest a strong beat."*

**And the coupling to STREAM structure is argued separately** (page 4), on two grounds: that what
matters for a note's perceived length is *"the IOI of a note in relation to the next note **within the
same voice**; obviously, this assumes knowledge of stream structure"*, and that *"non-chord-tones …
tend to resolve by step; but this generally implies resolution to another note within the same voice,
which again requires the grouping of notes into voices."*

### 3.3 The generative process (page 6, Equations 2–4, Figure 2)

> `P(M, H, S|N) ∝ P(N|M, H, S) P(M, H, S) = P(M, H, S, N)`   **(2)**
> `P(N) = Σ_{M,H,S} P(M, H, S, N)`                            **(3)**
> `P(M, H, S, N) = P(N|M, H, S) × P(H|M) × P(S|M) × P(M)`     **(4)**

*"Essentially, the model first generates a metrical structure; it then generates harmonic and stream
structures (these structures are dependent on the meter but independent of each other); finally, it
generates the note pattern, which is dependent on all three structural elements."* **★ The last word is
disputed between the two extracts — see §9.4; this side reads "elements" at two separate page
requests.**

**★ So harmony and stream are conditionally independent GIVEN the meter**, and both hang off the meter.
Figure 2 (*"The structure of the generative process"*) draws exactly that, with the note pattern
split into a rhythmic pattern and a pitch pattern beneath it.

**The time base:** *"We assume a discrete timeline of points spaced 50 ms apart, known as **pips**;
note-onsets and offsets as well as structural events (beats, changes of harmony, and stream beginnings
and endings) may only occur at pips."*

### 3.4 The metrical grid (pages 6–7, Figure 3)

**Four levels, numbered 0 to 3**, *"where level 3 is the highest, i.e. sparsest, level"*; **level 2 is
the tactus.** The paper notes the relation to its predecessor: *"very similar to what was proposed for
the monophonic meter-finding model in Temperley (2007), the main difference being that the current
structure has four levels instead of three."*

The order of generation, as Figure 3 draws it and the prose describes it: decide the time signature;
generate the tactus (L2) level; add L3 beats, which *"follows automatically"* from the first two;
generate L1 beats; generate L0 beats.

**Stated details, each at the page (page 7):**

- The first tactus interval uses *"a distribution which favours intervals in the range of 600–800
  ms."*
- Subsequent tactus beats come from *"a distribution conditional on the previous tactus interval,
  favouring a tactus level that is roughly regular, but allowing some fluctuation."*
- At each tactus beat a decision is made whether to continue or to end the level — *"in effect, this
  determines the length of the piece."*
- **L1 is assumed duple**, *"given that in Western music a triple division of the sub-tactus level is
  extremely rare."*
- L1 and L0 placements *"favour a roughly equal division of the higher-level beat interval but allow
  some irregularity."*
- The 'phase' of level 3 is chosen last, and *"the metrical grid is assumed to begin and end on tactus
  beats."*

**★ Two things about this passage are recorded at §7.1 and §7.2** — one a numbering defect in Figure 3,
and one a sentence whose two levels appear to be the wrong way round.

### 3.5 The harmonic generative step (page 7)

> *"The task of the generative process here is to segment the piece into harmonic segments or
> 'chord-spans', each one labelled with a root. **An important simplification here is that harmonic
> changes are allowed only on tactus beats.** (As shown in Table 1, it appears that only a very small
> percentage of harmonic changes are on sub-tactus beats, so excluding this possibility results in only
> a small loss of accuracy.) Thus the model's task is simply to choose a root for each tactus
> interval."*

**The root process, as printed:**

- The first tactus interval's root is *"chosen out of a uniform distribution."*
- For each later interval, the model *"first decides whether to continue the previous root or to change
  to a new root; **the probability of change is higher for L3 beats than L2 beats**, reflecting the
  greater likelihood of chord changes on stronger beats (see Table 1)."*
- *"If a new root is chosen, there is a high probability of moving to a root that is a perfect fifth
  above or below the previous one, reflecting the well-known preference for root motion by fifths in
  Western music; **all other roots are assigned the same low probability.**"*

**★ So the harmonic transition model is: stay-or-change, conditioned on metrical level; and if change,
fifth-related or flat.** **No key, no functional relation and no distinction among the non-fifth roots
is met anywhere in the sixteen pages as read.** *(Counting the flat class: a change excludes the
previous root, leaving eleven candidates, of which the fifth above and the fifth below are singled
out — so **nine** roots share the one low probability. That arithmetic is this side's, over the
paper's own sentence; the paper states no count.)*

### 3.6 The stream generative step (page 7)

*"the task of the generative process is simply to generate a set of streams, each one spanning a
certain portion of the piece. **We limit the possible beginning and ending points of streams to tactus
beats.** (This constraint has no musical justification, but is made simply to limit the space of
possible streams; as we will see, it does not imply that the first or last note of a stream must be on
a tactus beat.)"*

*"At each tactus beat, for each integer n there is a possibility of generating n new streams; a
**Poisson distribution** is used here with an expected value of much less than 1. (For the initial
tactus beat, a Poisson distribution with an expected value of **2** is used.)"* At each later tactus
beat a stream either continues or ends. *"Notice that streams in themselves are not assigned to
specific pitches or even to any pitch range."*

### 3.7 The note pattern: metrical anchoring, offsets, pitch (pages 7–8, Figure 4)

**Onsets.** *"for each stream, at each pip within the stream, a choice is made as to whether to
generate a note-onset at that point. There is an extremely low, but non-zero, probability of
note-onsets occurring at non-beat pips (this allows for notes on very weak beats such as 32nd-note
beats, and for 'extrametrical' notes such as grace notes)."*

**★ Metrical anchoring, which the paper presents as its own novelty** — *"I use a novel method which I
call *metrical anchoring* [this was discussed but not implemented in Temperley (2007)]"* (page 7):

> *"the probability of a note-onset at a beat **depends** on the presence of notes at the surrounding
> higher-level beats. Consider a weak eighth-note beat with stronger beats on either side (see Figure
> 4). A note on such a beat is extremely unlikely if there is no note on either side (we call this an
> 'unanchored' note); it is only slightly more likely if there is a note only on the previous beat
> ('pre-anchored'), much more likely if there is a note on the following beat ('post-anchored'), and
> again very likely if there are notes on both beats ('both-anchored')."*

**Figure 4 (printed page 8)** — *"Four rhythmic patterns (the third rest or note in each pattern may be
of any length). The numbers to the right show the probability of a note-onset on the second (weak)
beat, given the context of the first and third beats. **Data is from the Essen Folksong
Collection.**"*

| Pattern | Probability, as printed |
|---|---|
| Unanchored | **.003** |
| Pre-anchored | **.01** |
| Post-anchored | **.43** |
| Both-anchored | **.37** |

**★ The two largest values are not in the order the prose's list leads a reader to expect** — see
§7.3.

**The top-down onset order** (page 8): note status at L2 and L3 is decided first, *"each decision …
made independent of context, with the onset probability at L3 beats slightly higher than at L2
beats"*; then L1 conditional on neighbouring L2 beats; then L0 conditional on neighbouring L1 beats.
*"(It is the presence of neighbouring notes **within the same stream** that matters here, thus
capturing the interaction with stream structure discussed earlier.)"* The paper claims a benefit:
*"it allows us to indirectly incorporate the preference for longer notes on stronger beats."*

**Offsets** (page 8). *"the offset of each note must be no later than the following note-onset within
the stream (if any)."* Beyond that: *"notes are generally notated as ending on tactus beats unless
another note-onset intervenes. Thus we generate note-offsets as follows. For each note-onset, at each
subsequent tactus beat T, we make a stochastic decision as to whether to end the note at T or to
extend it further; but if, when considering T, we find that the onset of the next note in the stream
occurs before T, the note is ended at that onset with probability 1."*

**Pitch** (page 8). *"conditional on the current harmony and the previous pitch within the stream."*
Two profiles are multiplied: a **proximity profile**, *"a normal distribution centred around the
previous pitch (Temperley, 2007)"*, and a **chord-profile**, *"which favours notes that are chord-tones
of the current root and also slightly favours notes within the major and minor scales of the current
root."* For a stream's first note the proximity profile is replaced by *"an 'initial pitch
distribution'—a normal distribution across a broad pitch range."* The product *"is normalized to sum to
1."*

### 3.8 How many parameters, and where they came from (page 8)

> *"compared to many probabilistic models, the number of parameters is extremely small. **The program
> contains exactly 50 probability distributions; all but 8 of these are binary distributions, i.e.
> variables with just two values (thus requiring only one parameter value).** Where possible, the
> variables were set using corpus data; most of the metrical parameters were set using the **Essen
> folksong corpus, a large corpus of over 6000 European folk songs** (Schaffrath, 1995). **Other
> parameters were set using trial-and-error testing on a miscellaneous corpus of classical pieces.**"*

**★ The last sentence is taken up at §7.5**, because the paper does not say what that miscellaneous
corpus was or whether it overlaps the corpus the model is then tested on.

### 3.9 The analytical process, and the declared departures from exactness (pages 9–12)

*(★ HEADING CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED (#12): "The analytical
process, and the three declared approximations". It said three where F11 names four and where 3.10
below calls Equation 9 "a FOURTH declared approximation" — a count of this side's own reading that the
file contradicted twice.)*

> `{M, H, S}* = argmax[M, H, S] P(M, H, S, N)`   **(5)**

The paper writes out the brute-force loop and rejects it: *"This procedure is not remotely tractable,
even for one component of the structure, let alone for all the components combined. In what follows I
explain various techniques that are used for overcoming this search problem. **Some of the techniques
are approximate while others are exact.**"* (page 9).

**★ APPROXIMATION 1 — STREAMS ARE FOUND FIRST, IN A SEPARATE PASS (page 9, §3.2 and Equation 6).**
The paper states both the move and its licence:

> *"it appears also that the most probable stream structure for a note pattern can be inferred with
> reasonable accuracy without consideration of meter and harmony. … Another way to put this is that,
> given arbitrary stream structures S₁ and S₂, for any N,*
> `P(M, H, S₁, N) ≈∝ P(M, H, S₂, N)`   **(6)**
> *[≈∝, means 'approximately proportional to'] as M and H are varied. Thus if one wishes to find
> {M, H, S}*, this can be done by assuming any metrical and harmonic structure M_x and H_y and finding
> argmax[S] P(M_x, H_y, S, N)."*

The neutral structures used are stated: a metrical structure *"in which there is just one row of beats
roughly 300 ms apart"* and *"a completely 'flat' harmonic profile so that all pitch-classes are equally
likely."* **Once the best S is found it is fixed and the rest of the search assumes it.** Footnote 2
adds that this procedure *"has much in common with the stream analysis model presented in Temperley
(2001), and could (roughly speaking) be regarded as a probabilistic version of that model."*

**The stream pass is itself solved by dynamic programming** (page 11): *"It can be seen that the
legality and 'goodness' of a certain transition and column analysis depend only on the preceding column
analysis. … Because of the local fashion in which probabilities are calculated, a dynamic programming
approach may be used."* **So the staging is not exactness against approximation at the level of search
machinery — both passes use dynamic programming. What is approximate is the DECOUPLING of the two.**

**★ APPROXIMATION 2 — TWO WELL-FORMEDNESS CONSTRAINTS SIT OUTSIDE THE GENERATIVE MODEL (page 10).**
*"(1) streams may never cross in pitch; (2) two streams may never occupy the same square."* The paper
then says plainly what that costs:

> *"these constraints were not part of the generative process presented earlier. In effect, it may be
> assumed that stream structures with crossing and 'colliding' streams are sometimes generated but are
> then weeded out by some kind of filtering process. **The problem with such a step is that the
> probabilistic model is now no longer well defined.** … By filtering out certain structures, we are in
> effect giving these regions a probability of zero, but other regions not being adjusted to compensate
> for this, so the resulting total probability mass is less than 1. Really we should adjust for the loss
> of mass in some way … **This does not appear to be a serious problem, however. The main goal of the
> model is simply to find the most probable structure, and some loss of probability mass does not
> interfere with this task.** It simply means that the probabilities assigned to structures are somewhat
> lower than they should be."*

**Footnote 3 carries the argument:** *"Let us assume that the 'correct' model is the one in which the
probabilities of all structures are raised by the same proportion to make up for the loss of mass just
suggested. The most probable structure will be the same one with or without this adjustment, as the
probabilities of all structures are adjusted equally."* **★ What that argument does and does not reach
is recorded at §7.6.**

**★ APPROXIMATION 3 — AN *ad hoc* PITCH PENALTY, also outside the generative process (page 11).**
*"we also assign a penalty (a reduction in probability) for any note that is not part of the harmony
and is not followed by stepwise motion. This is, once again, an **ad hoc** move that is not reflected
in the generative process and results in some loss of probability mass, but it seems justified by the
resulting improvement in performance."*

**★ AND THE PART THAT IS JOINT: METER AND HARMONY, TOGETHER, OVER 'TACTUS-ROOT COMBINATIONS' (page
11, §3.3).**

> *"The first stage of the metrical/harmonic analysis process (the identification of the harmony and
> levels 0, 1, and 2 of the meter) uses the concept of a 'tactus-root combination' (**TRC**): the
> combination of a hypothetical tactus interval (two adjacent tactus beats) and a root. The essential
> idea is that the probability of a certain TRC depends only on the previous TRC, and the probability
> of beats and notes within the TRC depends only on the TRC. **Viewed in this way, the metrical/harmonic
> analysis process can be viewed as a rather complex kind of hidden Markov model.**"*

L0 and L1 placement inside a tactus span is *"essentially done as an exhaustive search"*; the sequence
of TRCs is found by dynamic programming, *"an approach which has long been standard in metrical and
harmonic analysis models (Temperley, 1997, 2001; Cemgil et al., 2000b; **Raphael & Stoddard, 2004**)"*,
with a traceback at the end.

**Level 3 is found last, on a second pass (page 12).** *"there are just five possibilities: L3 could be
duple (with an L3 beat at the first or second L2 beat) or triple (with an L3 beat at the first, second,
or third L2 beat)."* *(Two plus three is five — this side's arithmetic against the paper's own
enumeration.)* *"We also redo the harmonic analysis at this stage … on the reasoning that the addition
of L3 may affect the most optimal points for harmonic change."*

**And one extension the paper names and then declines** (page 12): *"a natural further step would be to
expand the harmonic possibilities, e.g. using key-specific names for chords (I/C, V/F, etc.); this
would yield a richer harmonic analysis and might improve the metrical analysis as well. **This has not
been attempted yet, however.**"*

### 3.10 The transcription half (pages 13–17)

> `P(N|Signal) ∝ P(Signal|N) P(N)`   **(7)**
> `P(N) = Σ_{M,H,S} P(M, H, S, N)`   **(8)**
> `P(N) ≈ Σ_{M,H} P(M, H, S*, N)`    **(9)**

**★ Equation 9 is a FOURTH declared approximation, and it is the one that bears on `P(N)` itself:**
*"rather than summing the quantity over all stream structures, we consider only the most probable
stream structure S*, derived in the 'first-pass' stream analysis."*

**Figure 7 (printed page 14)** shows the Bach passage of Figure 1 and three altered versions, with the
log probability the model assigns to each:

| Passage | Log probability, as printed |
|---|---|
| (a) the original | **−140.0** |
| (b) a note displaced by an octave | **−161.9** |
| (c) a right-hand note shifted by one eighth-note | **−146.4** |
| (d) the second D of the melody replaced by C♯ | **−143.1** |

*"It can be seen that the model assigns higher probability to the original pattern than to any of the
variants."* The paper's own reading of each variant is given at the page: (b) *"forcing the model to
create a new stream just for that note (which incurs a low probability)"*; (c) *"placing it on a weak
eighth-note beat rather than a quarter-note beat"*; (d) *"which makes it a non-chord-tone in relation
to the apparent root of G (and one that does not resolve by step)."*

**★ This is one passage with three variants, offered as an illustration.** The paper does not present
it as a measurement and no corpus, metric or rate accompanies it.

**The transcription machinery itself** (pages 14–17): a **PP array**, *"a two-dimensional array with
pips on one axis and pitch categories on the other"*, whose cells are note-onset probabilities; the
piece divided into *"'chunks' of one second in length"*; an iterative exchange in which the prior model
produces a PP array for a chunk, the signal model returns a determinate note pattern for it, and the
prior model analyses that and predicts the next (Figure 8). Equations 10 and 11 are printed in full.
Figure 9 prints a whole PP array for one chunk of the Bach passage, pitches 30 to 90 against pip times
3000 to 3950.

**What the paper says those log probabilities amount to** (page 14): *"the probabilities assigned by
the model reflect a kind of typicality or 'grammaticality' of note patterns within the language of
common-practice music."*

**★ AND THE STATE OF THAT HALF, TWICE IN THE PAPER'S OWN WORDS (pages 15 and 17):** *"While the
transcription system described above is still under development, the 'prior model' component is
complete"*, and *"the transcription system described above is still under construction. Work is
ongoing to refine the signal model and the interaction of signal model and prior model."* The
outstanding half is named as joint work (page 14): *"In recent work in collaboration with Taylan
Cemgil, I have begun to explore a solution to this problem."*

### 3.11 What the conclusions say is missing (page 17)

> *"There are many other kinds of musical knowledge that could be incorporated into the model—for
> example, more detailed knowledge about harmony (**knowledge of functional harmony and of stylistic
> progressions such as cadences**), knowledge of conventional phrase structures (the norm of 4-bar
> phrases), and awareness of repeated melodic patterns or 'parallelisms' (which play an important role
> in meter, among other things). The challenges will be, first, to find logical ways of integrating
> these kinds of musical knowledge with the existing generative process, and second, to keep the
> computational complexity of the inference problem at a tractable level, either with exact methods
> such as dynamic programming or with reasonable approximations."*

And a priority claim, hedged at the page: *"the system sketched above **appears to be** the first
concerted attempt to bring to bear higher-level musical knowledge on the transcription process. It
remains to be seen how much benefit this knowledge will yield."*

---

## §4 — Claims, labeled

The commission's §4 requires every claim to carry FACT (stated or measured in the paper, with its
location), THEORY (established published theory), or CONJECTURE. **Nothing unlabeled below carries
load later.**

### FACT — what the paper states of itself, with its location

- **F1 (pages 3–4, 6).** **Meter, harmony and stream are one generative model**, decomposed as
  Equation 4, with harmony and stream conditionally independent given the meter.
- **F2 (page 11).** **Meter and harmony are decided TOGETHER**, as one hidden-Markov-style search over
  tactus-root combinations — 3.9's quoted sentence.
- **F3 (page 9).** **Streams are decided FIRST and SEPARATELY**, on the explicitly stated approximation
  of Equation 6, and then held fixed. **The model is therefore unified in its generative story and
  staged in its analysis.**
- **F4 (page 4).** **The harmonic label is a root and nothing else** — no quality, no key, no Roman
  numeral, no inversion.
- **F5 (page 7).** **Harmonic change is permitted only at tactus beats**, and the paper grounds that
  restriction on Table 1's 2.4% figure for level-1 beats.
- **F6 (page 8).** **Exactly 50 probability distributions, all but 8 of them binary.** Metrical
  parameters mostly from the Essen folksong corpus (*"over 6000 European folk songs"*); others *"set
  using trial-and-error testing on a miscellaneous corpus of classical pieces."*
- **F7 (page 12).** **The test corpus is the Kostka–Payne corpus**: *"a set of 46 excerpts from the
  common-practice repertoire from the workbook accompanying Kostka and Payne's (1995) theory textbook,
  with harmonic analysis (showing keys and Roman-numeral chord symbols) done by the authors … the
  harmonic analyses were encoded by Bryan Pardo."* **19 of those excerpts** were also played by *"a
  semi-professional pianist"* to give a performed version (page 13).
- **F8 (page 12, Table 2).** On metre, the probabilistic model beats the Melisma model on the tactus
  level of the quantized corpus, **37/46 against 32/46**, and the two are close elsewhere. Every value
  is in §6 below.
- **F9 (page 13, Table 3).** On harmony, the probabilistic model scores **78.7%** of total time
  correctly labelled and the Melisma model **80.8%** — **so on this measurement the unified model is
  the WORSE of the two** — and the paper states the reason: *"the Melisma model was given the correct
  metrical structure (as indicated by the score). By contrast, the polyphonic model must infer the
  metrical structure on its own, and is not always correct."*
- **F10 (page 13).** **The stream component is not tested at all**: *"As for the stream component of
  the model, this is difficult to test; it is frequently unclear in common-practice music what the
  'correct' analysis would be, and no annotated corpora are available."*
- **F11 (pages 9, 10, 11, 14).** **The paper declares departures from exactness at four places, named
  rather than counted** — the stream-first approximation (Eqn 6, page 9); the two well-formedness
  constraints that sit outside the generative model (page 10); the *ad hoc* non-chord-tone penalty
  (page 11); and the single-stream-structure estimate of `P(N)` (Eqn 9, page 14). **Of those, the
  paper states that TWO lose probability mass** — the well-formedness constraints (*"the resulting
  total probability mass is less than 1"*) and the *ad hoc* penalty (*"results in some loss of
  probability mass"*). **The other two are described as approximations without a statement about
  mass.**
- **F12 (pages 15, 17).** **The transcription system is not finished.** Only the prior model is
  complete.
- **F13 (page 12).** **Extending the harmony to key-specific chord names is named and declined**:
  *"This has not been attempted yet, however."*
- **★ F15 (pages 3, 4, 12, 17). THE MODEL DOES NOT INFER KEY — AND ITS OWN PREDECESSOR DID.** Page 3
  describes the earlier model this one builds on: *"in Temperley (2007), I presented a model which
  analyses **key** and meter in monophonic input and estimates the probabilities of monophonic note
  patterns. The current model extends this previous research by accommodating polyphonic input,
  incorporating harmonic and stream analysis, and providing a workable component for a transcription
  system."* **Key is not among the three structures the 2009 model derives**, and page 4 excludes it
  from the harmonic label in terms — the labels are *"simply roots, though they could also carry more
  specific information, e.g. chord quality (major versus minor) or **relationship to the key** (e.g.
  'I of C major')."* Page 12 names the key-specific extension and says it *"has not been attempted
  yet"*, and page 17's conclusions list *"knowledge of functional harmony"* among what is missing.
  **So the extension to polyphony was bought, on this axis, by dropping a structure the monophonic
  predecessor had.** *(That last sentence is this side's reading of the two descriptions set beside
  each other; the paper does not characterise the change as a loss.)*
- **F14 (page 12).** **The metrical scoring rule:** *"TL is considered correct if it is within 10% of
  the correct value; all other values must match exactly to be correct,"* and *"figures for TD, UD, TP,
  and UPh are only given for cases where TL is correct."*

### THEORY — established published machinery or positions the paper adopts rather than invents

- **T1.** The metrical-hierarchy definition, credited to Lerdahl & Jackendoff (1983) (page 4).
- **T2.** Dynamic programming for metrical and harmonic analysis, presented as long standard and
  credited to Temperley (1997, 2001), Cemgil et al. (2000b) and Raphael & Stoddard (2004) (page 11).
- **T3.** That note-onsets are less likely on lower metrical levels, credited to Palmer & Krumhansl
  (1990) (page 8).
- **T4.** The preference for root motion by fifths, invoked as *"the well-known preference for root
  motion by fifths in Western music"* (page 7) with no citation at that sentence.
- **T5.** Bayesian inversion for transcription, `P(N|Signal) ∝ P(Signal|N)P(N)` (pages 4 and 13).

### CONJECTURE — what the paper asserts without measuring it

- **C1 (page 3).** That unification *"holds out the promise of improving performance on each individual
  problem, in relation to what can be achieved by addressing them separately."* **Table 3 is the one
  place in the sixteen pages as read where that promise meets a harmonic measurement, and there the
  unified model comes out BELOW the separate one** (F9) — for a reason the paper gives, but the
  promise itself is not demonstrated on that axis here. *(On the metrical axis Table 2 does show the
  unified model ahead, so the promise is not refuted either; the two axes point different ways and
  the paper says so at page 13.)*
- **C2 (page 9).** Equation 6 — that stream structure can be inferred *"with reasonable accuracy
  without consideration of meter and harmony."* **Called an approximation and defended by citation to
  an argument in Temperley (2001); no measurement of the approximation's cost is given here**, and F10
  says the stream component is untested.
- **C3 (page 10).** That the lost probability mass *"does not appear to be a serious problem."*
- **C4 (page 11).** That the *ad hoc* pitch penalty *"seems justified by the resulting improvement in
  performance."* **No before-and-after figure for that penalty is given.**
- **C5 (page 12).** *"Inspection of the output suggests that the probabilistic model's consideration of
  harmony is a crucial factor in its superior performance."* Stated as an inspection, not a measured
  ablation.
- **C6 (page 13).** *"Perhaps further refinement of the parameters could yield further improvement."*
- **C7 (page 14).** That each of the three Figure-7 variants is *"in some way 'ungrammatical' … or at
  least less normative than the original."* One passage, three variants, no corpus.
- **C8 (page 17).** That the sketched system *"appears to be the first concerted attempt"* of its kind.
  Hedged at the page and not established there.

---

## §5 — Coupling facts (mandatory under the commission's §4)

### 5.1 What the method ASSUMES about its upstream

- **A piano-roll: pitch, on-time and off-time in milliseconds** (page 4). **No spelling**, no dynamics,
  no bar lines, no key signature, no time signature. Everything metrical is *inferred*, which is the
  point of the model.
- **A 50 ms discretisation.** All onsets, offsets, beats, harmonic changes and stream boundaries are
  quantized to pips (page 6), and *"note-onsets and offsets are quantized to pips … in a somewhat
  complex and context-sensitive way, to avoid certain problems such as assigning the notes of a single
  chord to different pips or creating notes of length zero"* (page 9).
- **Timing that may be human or quantized.** The paper tests both and reports them separately (F7).
- **Parameters already set.** There is no fitting stage in the analysis; the 50 distributions are set
  in advance (F6).
- **Nothing upstream supplies streams, meter or harmony.** *All three* are outputs. **This is the sharp
  contrast with the Melisma comparison of F9, where the rival was handed the correct meter.**

### 5.2 What the method HANDS downstream

- **A metrical grid of four levels**, 0 to 3, with L2 the tactus (3.4).
- **A harmonic segmentation into tactus-aligned spans, each carrying ONE ROOT** (F4, F5, F15). **A
  consumer gets no quality, no key, no numeral, no inversion, no bass, and no boundary that is not a
  tactus beat** — each of those absences stated by the paper at 3.1, 3.5 or F15 rather than inferred
  here.
- **A partition of the notes into streams**, with streams beginning and ending at tactus beats (3.6),
  non-crossing and non-colliding (3.9), **and with no evaluation attached to any of it** (F10).
- **A single committed analysis.** The search returns the argmax; **no ranked alternative structure and
  no per-segment confidence is met anywhere in the sixteen pages as read.**
- **`P(N)`, a log probability for the whole note pattern** (3.10) — which is the output the
  transcription half consumes, and which carries the four approximations of F11. Figure 7 shows it
  used comparatively across four note patterns.
- **A PP array per chunk** for a signal model to consume — but the consumer does not yet exist (F12).

### 5.3 The method's own STATED SCOPE and limits

Collected from the paper's own sentences rather than inferred:

- **Repertoire.** *"intended primarily for traditional Western art music ('classical' music), but may
  be applicable to other styles as well"* (page 3).
- **Roots only, and no key**, with functional harmony and cadences named in the conclusions as
  knowledge the model does not have (F4, F15, 3.11).
- **Harmonic change only at tactus beats** (F5).
- **Stream boundaries only at tactus beats**, a constraint the paper says *"has no musical
  justification"* (3.6).
- **L1 assumed duple** (3.4).
- **Four declared departures from exactness, TWO of them stated to lose probability mass** (F11).
  *(★ CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED (#12): "Four approximations, three
  of them losing probability mass". F11 was corrected from three to two at the read-back and this copy
  of the same fact was left behind.)*
- **The stream component untested** (F10).
- **The transcription system unfinished** (F12).
- **A 46-excerpt test corpus** (F7).

### 5.4 ★ How this paper stands to row 1, Raphael & Stoddard 2003

**Recorded because this paper cites those authors three times and because this side read their 2003
paper whole, at the object, immediately before this one** (§1's declared contamination).

- **Page 3** lists *"key induction and harmonic analysis (**Raphael & Stoddard, 2004**; Temperley,
  2004)"* among the decade's probabilistic work.
- **Page 11** names *"Raphael & Stoddard, 2004"* among the models for which dynamic programming *"has
  long been standard"*.
- **Page 4 characterises their method, and this is the load-bearing one:** *"Several models of harmonic
  analysis, such as those of Maxwell (1992) and Temperley (2001), have explicitly weighted metrical
  information in the input. [Others, such as **Raphael and Stoddard (2004)**, have **finessed** the
  problem by limiting the possible points of harmonic change to a high metrical level such as bars or
  half-bars.]"*

**★ TWO THINGS MUST BE SAID ABOUT THAT SENTENCE AND BOTH ARE BOUNDS, NOT FINDINGS.**

1. **The citation is to Raphael & Stoddard 2004, the *Computer Music Journal* article — which is row 2
   of the candidacy list, is marked PAYWALL, is NOT HELD, and has NOT been read by anyone here.**
   `docs/research_papers/BIBLIOGRAPHY.md` line 16 records it, and this paper's own reference list gives
   it as *"Raphael, C. & Stoddard, J. (2004). Functional harmonic analysis using probabilistic models.
   Computer Music Journal, 28(3), 45–52."* **So Temperley is describing a paper this project does not
   hold.** Nothing below is a claim about what that 2004 article says.
2. **What the description says IS true of the 2003 conference paper this side read whole**, which fixes
   a metrical period `q` in advance — *"say a measure (q = 1) or half measure (q = 1/2)"* — and permits
   a harmonic label only per period. **This side notes the agreement and takes no verdict on whether
   Temperley's sentence is accurate about the 2004 article, which is the document he cites.**

**Where the two designs sit relative to each other, stated only from what each paper says of itself:**

| | Raphael & Stoddard 2003 (row 1) | Temperley 2009 (row 8) |
|---|---|---|
| What is decided jointly | tonic, mode and chord degree, in one state | meter and harmony, in one state |
| What is NOT joint | meter — the period grid is given in advance | streams — found first, separately, on a declared approximation |
| Harmonic label | tonic + mode + degree (I…VII) | root only |
| Where a harmonic boundary may fall | at a fixed period boundary chosen per piece | at a tactus beat the model itself infers |
| Search | exact global maximum, explicitly no beam search | partly exact, partly approximate, by the paper's own statement |
| Parameters | 104 transition + 30 output, two groups hand-set | 50 distributions, 42 of them binary |
| Fitting | unsupervised, forward-backward, on about five movements | set in advance from the Essen corpus and by trial and error |
| Reported accuracy | **none at all** | **Tables 2 and 3** |

**No verdict is taken on which is better and none is available from these two papers**, because they
report on different tasks and one of them reports nothing.

---

## §6 — Measured results, with corpus, metric and value as the paper states them

**Unlike row 1, this paper does report measurements.** Every figure below is transcribed at its table
or its line, and no figure is restated from prose where a table carries it.

### 6.1 The corpus

**The Kostka–Payne (K-P) corpus** (page 12): *"a set of 46 excerpts from the common-practice repertoire
from the workbook accompanying Kostka and Payne's (1995) theory textbook, with harmonic analysis
(showing keys and Roman-numeral chord symbols) done by the authors. The excerpts were converted into
midifiles as described in Temperley (2001); the harmonic analyses were encoded by Bryan Pardo."*

**A second, performed version** (page 13): *"the 19 excerpts from the corpus for solo piano were also
performed by a semi-professional pianist and midifiles were generated from these."* The paper's stated
reason: *"This allows the results for both the probabilistic model and the Melisma model to be tested
using the more irregular and complex timing characteristic of human performance."*

### 6.2 Table 1 — the ground for the meter-harmony coupling (printed page 6)

Transcribed at 3.2 above: **71.5 / 22.3 / 2.4** per cent of beats at levels 3 / 2 / 1 carrying a change
of harmony, in the Kostka–Payne corpus.

### 6.3 Table 2 — metre (printed page 12)

*"The performance of the Melisma and probabilistic meter-finding models on the Kostka–Payne corpus.
TL = tactus length; TD = upper-level division (duple or triple); UD = tactus division (duple or
triple); TP = number of pickup notes (before first tactus beat); UPh = phase of upper level."*

| | Melisma model | Probabilistic model |
|---|---|---|
| **Quantized corpus (46 excerpts)** | | |
| TL | 32/46 (69.6%) | **37/46 (80.4%)** |
| TD | 32/32 (100.0%) | 37/37 (100.0%) |
| UD | 31/32 (96.9%) | 34/37 (91.9%) |
| TP | 29/32 (90.6%) | 36/37 (97.3%) |
| UPh | 27/31 (87.1%) | 30/34 (88.2%) |
| **Performed piano corpus (19 excerpts)** | | |
| TL | 14/19 (73.7%) | 14/19 (73.7%) |
| TD | 13/14 (92.9%) | 12/14 (85.7%) |
| UD | 10/14 (71.4%) | 12/14 (85.7%) |
| TP | 14/14 (100.0%) | 14/14 (100.0%) |
| UPh | 10/10 (100.0%) | 12/12 (100.0%) |

*(Every ratio in that table was recomputed by this side and every printed percentage is the correct
rounding of its own ratio. The table has five rows, two models and two corpora, so the pairs are
twenty — a count over the paper's table, not over this side's acts.)*

**★ The definitions the table's letters carry are given in the prose rather than the caption** (page
12) and are reproduced here because the caption alone does not make the table readable: `TL` = average
tactus length in milliseconds; `TD` = division of the tactus level; `UD` = division of the level above
the tactus; `TP` = number of pickup notes before the first tactus beat; `UPh` = phase of the upper
level. **★ The caption's own glosses for TD and UD are the reverse of the prose's, and that is recorded
at §7.4.**

**★ The denominators do not all follow the rule the prose states, and that is recorded at §7.7.**

**What the paper says about the table** (page 12): *"Of most interest is the fact that the
probabilistic model achieves substantially better results on the tactus level, obtaining a correct
result on 37 cases versus 32 for the Melisma model. Regarding other aspects of metrical structure, the
two models are very similar in their level of performance."* And of the performed corpus (page 13):
*"the two models are very close in performance, though the probabilistic model achieves slightly better
results on the upper level."*

### 6.4 Table 3 — harmony (printed page 13)

*"Performance of harmonic analysis models on the Kostka–Payne corpus."*

**The metric is defined in the prose rather than the caption** (page 13): *"For testing the harmonic
model, we again use the K-P corpus. In this case, we simply measure the proportion of time in the
entire corpus that the model assigns the correct root."*

| Model | Score |
|---|---|
| Melisma model (% of total time correctly labelled) | **80.8%** |
| Pardo and Birmingham 2002 (% of minimal segments correctly labelled)* | **76.5%** |
| Probabilistic model (% of total time correctly labelled) | **78.7%** |

*(The per-cent signs are printed in the table's cells, under a column headed simply "Score".)*

*The table's own footnote:* *"A 'minimal segment' is a time segment between successive onsets or
offsets. While the Melisma and probabilistic models only produce root judgments, Pardo and
Birmingham's model also identifies chord quality (major/minor/diminished), and they required correct
chord quality for a correct answer."*

**★ THE TWO THINGS THIS TABLE ESTABLISHES, AND THEY PULL IN OPPOSITE DIRECTIONS.**

1. **The unified model is 2.1 points BELOW the older separate model on harmony** — 78.7 against 80.8 —
   **and the difference is the metrical information.** The paper states the asymmetry itself: *"the
   Melisma harmonic model requires a metrical analysis as part of the input. In the current test (as
   in Temperley, 2001), the Melisma model was given the correct metrical structure (as indicated by
   the score). By contrast, the polyphonic model must infer the metrical structure on its own, and is
   not always correct, as indicated by the test results reported above. Thus the Melisma model has a
   significant advantage."*
2. **The paper's own summary of the pair** (page 13): *"On balance, the probabilistic model's metrical
   analysis is significantly better than Melisma's, and its harmonic performance is nearly as good
   despite the disadvantage of having imperfect metrical information."*

**★ WHAT THAT 2.1-POINT FIGURE IS AND IS NOT, said carefully because it is the kind of number a reader
will want to lift.** It is the gap between **one model given the correct metrical structure** and **a
different model inferring its own**, on the same corpus and the same metric. **It is not a measurement
of one model with and without given metre** — no such ablation is reported anywhere in the sixteen
pages as read — so it does not isolate the cost of inferring the metre from every other difference
between the two systems. **This side records the figure and states that bound at the same time.**

**★ AND THE THIRD ROW IS ON A DIFFERENT METRIC FROM THE OTHER TWO** — see §7.8.

### 6.5 The one worked case the paper gives for WHY the metrical result differs (printed page 13)

**Figure 6** — *"Beethoven, Rondo Op. 51 No. 1, mm. 109-11 (from the Kostka–Payne corpus), showing the
tactus analyses of the Melisma model and the probabilistic model."* The two models' tactus rows are
drawn above the score, labelled *Prob. model* and *Melisma*.

The paper's reading of it: *"The Melisma model places tactus beats one 16th-note too early, as shown;
it favours these positions because the coinciding notes are 'long' (by the Melisma model's definition).
But the probabilistic model considers harmonic information and thus favours tactus beat locations that
correspond with the changes of harmony, as is fact correct."*

**This is one measure of one excerpt, offered as an illustration of the mechanism C5 asserts.** It is
not an ablation and carries no rate.

### 6.6 Figure 4's probabilities, and Figure 7's log probabilities

Both are transcribed at 3.7 and 3.10 above. **Figure 4's four values are stated to come from the Essen
Folksong Collection**, which is the parameter-setting corpus and not the test corpus. **Figure 7's four
log probabilities are one passage and three hand-made variants of it**, and the paper offers them as
illustration.

### 6.7 What the paper does NOT report

**Named rather than counted, and each a negative over the sixteen pages as read:**

- **No measurement of the stream component**, by the paper's own statement (F10).
- **No confidence interval, no error bar and no significance test is met anywhere in the sixteen pages
  as read** — **and the paper nevertheless uses the word *significantly*** of the metrical comparison
  (page 13) and again of the Melisma model's advantage on harmony.
- **No ablation.** The *ad hoc* pitch penalty (C4), the metrical anchoring method, and the harmony
  channel whose contribution C5 calls *"crucial"* are each argued for without a with-and-without
  figure.
- **No timing or complexity figure** for the analysis.
- **No transcription result**, the system being unfinished (F12).

---

## §7 — Defects and tensions met in the pages as read

**Named rather than counted**, and each read at its own line. **Each is a statement about what is
printed in these sixteen pages; none is a statement about the record or about our own design.** *(No
claim is made that this is everything a further reader would find.)*

### 7.1 Figure 3 numbers two of its boxes the same (printed page 7)

Figure 3, *"The generative process for the metrical grid"*, has five boxes, and they are labelled
**1, 2, 3, 4, 4** — *"1. Decide time signature"*, *"2. Generate L2 (tactus) level"*, *"3. Add level L3
beats (follows automatically from 1 and 2)"*, *"4. Generate L1 beats"*, and *"4. Generate L0 beats"*.
**The last two carry the same number**, and the prose describing the same process treats them as
successive stages. **Nothing rests on it** — the arrows fix the order — but a reader citing a step by
number cannot.

### 7.2 A sentence about metrical levels reads the wrong way round (printed page 7)

> *"Next, decisions are made as to whether level 3 should be duple (**in which case every second L3
> beat is an L2 beat**) or triple, and whether L2 beat intervals should be divided duply or triply."*

**Page 6 states that level 3 is the highest, i.e. the sparsest, level, and that level 2 is the
tactus.** A sparser level cannot have two of its beats inside one beat of a denser one. **Under the
paper's own definitions the relation runs the other way: if L3 is duple, every second L2 beat is an L3
beat.**

**Three other sentences in the paper say it that way round, and one of them is on this same page:**

- **Page 7, four sentences later:** *"Finally, the 'phase' of L3 must be chosen—whether the first L2
  beat is the first, second, or third beat of a L3 beat interval."* — an L3 interval containing two or
  three L2 beats.
- **Page 11:** *"Level 3—which simply defines **every second or third level 2 beat** as strong—is then
  determined on a second pass."*
- **Page 12:** *"L3 could be duple (with an L3 beat at the first or second L2 beat) or triple (with an
  L3 beat at the first, second, or third L2 beat)."*

**So one sentence stands against three and against the paper's own definition of its levels.** *(This
side takes no verdict on what the author intended; what is established is that the quoted clause
cannot hold alongside the other four statements.)*

### 7.3 Figure 4's largest value is not the one the prose builds to (printed page 8)

The prose orders the four cases as a rising sequence: *"extremely unlikely"* (unanchored), *"only
slightly more likely"* (pre-anchored), *"much more likely"* (post-anchored), *"and again very likely"*
(both-anchored). **The figure's numbers are .003, .01, .43 and .37** — so the fourth is **lower** than
the third.

**The prose is not falsified by that**: *"again very likely"* does not assert *higher*. **But a reader
taking the four phrases as a ranking gets the top two the wrong way round**, and the paper does not
remark on the reversal or offer a reason for it. **Recorded as a reading hazard with both the prose and
the values transcribed, not as a contradiction.**

### 7.4 Table 2's caption defines two of its own letters the opposite way from the prose (printed page 12)

**The caption reads:** *"TD = upper-level division (duple or triple); UD = tactus division (duple or
triple)."*

**The prose on the same page reads:** *"TD = division of the tactus level (2 if duple, 3 if triple);
UD = division of the level above the tactus (2 if duple, 3 if triple)."*

**These are exact opposites.** Three things favour the prose:

- **The letters themselves** — **T** for tactus, **U** for upper.
- **The neighbouring `UPh`**, which prose and caption agree is the *"phase of upper level"*.
- **★ A third sentence in the prose that only works under the prose's own definition:** *"UPh = the
  phase of the upper level, i.e. whether the first tactus beat is the first (1), second (2) or third
  (3) beat of an upper-level span (**the third option is only possible if UD = 3**)."* A first tactus
  beat can be the *third* beat of an upper-level span only when **the upper level** is triple — so
  `UD` must be the upper level's division, which is what the prose says and the opposite of what the
  caption says.

**So the caption appears to have swapped the two glosses**, and a reader who reads the table by its
caption alone will read both rows inverted.

**★ Unlike the other defects recorded in this section, this one could move a value a later reader
lifts**, because TD and UD carry different numbers in three of the four columns — on the performed
corpus the Melisma model is 13/14 on one row and 10/14 on the other. **Whoever lifts a figure from
that table must decide which gloss to believe, and this extract records the conflict rather than
choosing for them** — while noting that the three points above all fall on the prose's side.

### 7.5 The tuning corpus is not named, and its relation to the test corpus is not stated (printed pages 8 and 12)

Page 8: *"Other parameters were set using **trial-and-error testing on a miscellaneous corpus of
classical pieces**."* Page 12: the model is then tested on 46 classical excerpts from the Kostka–Payne
workbook.

**The paper does not say what the miscellaneous corpus contained, how large it was, or whether it
overlaps the Kostka–Payne corpus.** The metrical parameters' source *is* named and *is* clearly
separate — the Essen folksong corpus. **The others are not.** **This side asserts no overlap and no
absence of overlap; what is established is that the paper does not settle the question**, and that a
reader who wants the reported figures to be held-out figures cannot get that from these sixteen pages.

### 7.6 What the lost-probability-mass argument covers, and what it does not (printed pages 10 and 14)

Page 10 concedes that filtering out ill-formed stream structures leaves *"total probability mass …
less than 1"*, and argues the loss is harmless: *"The main goal of the model is simply to find the most
probable structure, and some loss of probability mass does not interfere with this task."* Footnote 3
makes the argument exact: if every structure's probability is raised by **the same proportion**, *"the
most probable structure will be the same one with or without this adjustment."*

**That argument is about choosing among structures for ONE note pattern, and it is sound for that.**

**But §5 puts `P(N)` to a different use** — comparing **different note patterns** against one another,
which is what Equation 7 needs and what Figure 7 actually does with four of them. **Nothing met in the
sixteen pages as read argues that the lost mass is the same proportion across different note
patterns**, which is what would be needed to carry the footnote's argument over to that use.

**Recorded as a gap in what the paper's own argument reaches, not as an error.** The paper says at page
10 that the probabilities *"are somewhat lower than they should be"*; **it does not say by how much, or
whether by the same factor everywhere.**

### 7.7 Table 2's denominators do not all follow the rule the prose states (printed page 12)

The prose states one rule: *"figures for TD, UD, TP, and UPh are only given for cases where TL is
correct."* **On that rule every denominator in those four rows should be the TL-correct count of its
own column** — 32, 37, 14 and 14.

**Three of the four rows obey it. `UPh` does not.** Its denominators are **31, 34, 10 and 12** — and in
each column that number is exactly the **numerator of the `UD` row** immediately above it (31, 34, 10,
12). **So `UPh` is reported only for cases where the upper-level division was also correct**, which is
a narrower population than the prose describes.

**That reading is derived from the printed numbers, not stated by the paper**, and the paper gives no
reason for the narrowing. **The consequence for a reader is concrete: `UPh`'s percentages — 87.1, 88.2,
100.0 and 100.0 — are over fewer excerpts than the rows above them**, and the 100.0% figures in the
performed columns rest on ten and twelve cases out of nineteen.

### 7.8 Table 3 places three figures on one axis, two of them on a different metric from the third (printed page 13)

The rows read **80.8**, **76.5** and **78.7** under one heading, *"Score"*. But the first and third are
*"% of total time correctly labelled"* and the second is *"% of minimal segments correctly labelled"* —
**a proportion of duration against a proportion of a count of segments.**

**The paper flags one difference between the rows and not the other.** Its prose says the Pardo and
Birmingham comparison *"is not entirely fair … as Pardo and Birmingham's model also identifies chord
quality … and they required correct chord quality for a correct answer"*, and the table's footnote says
the same. **Neither mentions that the unit of measurement itself differs.** The row labels carry it,
and a reader who reads only the numbers and the prose will not meet it.

### 7.9 A word dropped (printed page 13)

*"But the probabilistic model considers harmonic information and thus favours tactus beat locations
that correspond with the changes of harmony, **as is fact correct**."* — *in* is required before
*fact*. **Nothing rests on it.**

### 7.10 The reference list checked, and found to hold

**Every author-and-year citation met in the body resolves to an entry in the reference list on printed
page 18** — named rather than counted: Cambouropoulos 2008; Cemgil et al. 2000a and 2000b; Cemgil &
Kappen 2003; Cemgil et al. 2005; Chai & Vercoe 2001; Davy 2006; de la Higuera et al. 2005; Jones et al.
2002; Kashino et al. 1998; Kirlin & Utgoff 2005; Klapuri 2004; Klapuri & Davy 2006; Kostka & Payne
1995; Lerdahl & Jackendoff 1983; Maxwell 1992; Palmer & Krumhansl 1990; Pardo & Birmingham 2002; Pearce
& Wiggins 2006; Povel & Essens 1985; Raphael 2002; Raphael & Stoddard 2004; Rosenthal 1992; Schaffrath
1995; Schellenberg 1997; Temperley 1997, 2001, 2004 and 2007. **No unresolved citation was met.**
*(This is a check that HELD, recorded because a negative result is a result. It is a statement about
the citations this side met while reading the body whole; it is not a claim that the list was walked in
the other direction.)*

**Two entries are formatted unlike the rest** — *"Cemgil, A.T., Kappen, B. & Barber, D. 2005."* and
*"Klapuri A.P. 2004."*, both without the parentheses every other entry puts round its year, the second
also without a comma after the surname. **Typography, carrying nothing.**

---

## §8 — The closing section: what the read-back and the sweep found

**This section was written as its own edit, after §1 to §7 were finished and before this file was
landed**, which is the order the hundred-and-sixty-ninth handoff entry's §3 sets. **The first extract
was still unopened when this section was written.**

### 8.1 What the read-back was

After §1 to §7 were written, **the paper was re-opened and every transcription in them was compared at
its page.** The requests made after the whole read are **named rather than counted**: **held pages 10
and 11 together** (printed 12–13, the two result tables); **held 4 to 6** (printed 6–8, Table 1,
Figures 2, 3 and 4, and the parameter count); **held 7 to 9** (printed 9–11, the approximations and
the tactus-root combination); **held 1 and 2** (printed 3–4, the abstract, the introduction and the
Raphael & Stoddard sentence); and **held 12 to 15** (printed 14–17, Figure 7, the transcription
machinery and the conclusions). *(★ CORRECTED AT THE POST-LANDING CHECK. FORMER WORDING, PRESERVED
(#12): "Four requests were made after the whole read, named rather than counted:". **It said four and
then listed five, in one sentence** — the cadence's own rule broken in the very clause that invokes
it.)*

**NO TRANSCRIBED VALUE MOVED.** Every figure in this extract was re-read at its table or its line and
stands as first written: Table 1's **71.5 / 22.3 / 2.4**; Figure 4's **.003 / .01 / .43 / .37**; the
**50** probability distributions of which **all but 8** are binary; the **over 6000** Essen folk songs;
the **46** and **19** excerpt corpora; **every one of Table 2's twenty ratios and their percentages**;
Table 3's **80.8% / 76.5% / 78.7%**; Figure 7's **−140.0 / −161.9 / −146.4 / −143.1**; the **600–800
ms** tactus range; the **50 ms** pip; the **300 ms** neutral beat row; the **one-second** chunks; and
the **four levels**, **five** L3 possibilities and Poisson expectation of **2**.

### 8.2 What the read-back ADDED, because the first writing had missed it

- **★ That the model does not infer key at all, while the monophonic predecessor it builds on did.**
  Now **F15**, and carried into 5.2 and 5.3. **This is the largest thing the first writing missed**,
  and it was missed because page 3's sentence about Temperley (2007) reads as provenance rather than
  as a statement about scope.
- **Three further corroborations for §7.2**, two of which were already in front of this side and not
  used: page 7's own phase sentence four sentences later, page 11's *"every second or third level 2
  beat"*, and page 12's enumeration of the five L3 possibilities. **The finding went from one sentence
  against a definition to one sentence against four.**
- **A third piece of evidence for §7.4**, and the decisive one: the prose's parenthesis *"the third
  option is only possible if UD = 3"*, which only works under the prose's own gloss of `UD`. **The
  finding went from "the caption and the prose conflict" to "three independent points fall on the
  prose's side."**
- **That the stream pass is itself solved by dynamic programming** (page 11), so the staging is not a
  matter of exact machinery against approximate machinery. Now at 3.9.
- **The harmonic metric's definition from the prose** — *"the proportion of time in the entire corpus
  that the model assigns the correct root"* — which the table's caption does not give. Now at 6.4.
- **Figure 6**, the one worked case the paper offers for why its metrical result differs from
  Melisma's. Now its own subsection at 6.5.
- **That Table 3's cells carry per-cent signs** under a column headed only *"Score"*. Corrected at 6.4.
- **The paper's own gloss of what its log probabilities amount to** — *"a kind of typicality or
  'grammaticality'"* — and that the unfinished transcription half is named as joint work with Taylan
  Cemgil. Now at 3.10.

### 8.3 What the read-back FALSIFIED in this extract's own writing

**★ THREE COUNTS THIS SIDE DERIVED AND GOT WRONG. All three were arithmetic over the paper rather than
transcription of it, and all three are corrected at their sites.**

1. **§3.5 read *"the ten non-fifth roots"*.** **It is nine.** A change excludes the previous root,
   leaving eleven candidates, of which the fifth above and the fifth below are singled out: 11 − 2 = 9.
   The site now carries the derivation rather than the bare number.
2. **F11 read *"Three of the four are stated to lose probability mass."*** **It is two.** The paper
   says it of the well-formedness constraints (*"total probability mass is less than 1"*) and of the
   *ad hoc* penalty (*"results in some loss of probability mass"*), and says no such thing of the
   stream-first approximation or of Equation 9. **The site now names which two and says what the other
   two are described as instead.**
3. **§6.3 read *"those fifteen ratio-and-percentage pairs"*.** **There are twenty** — five rows, two
   models, two corpora. The site now states the multiplication rather than the product.

**All three are the same error**: a number put on this side's own reading without deriving it, which is
what cadence 6 forbids in those words. **The read-back is the act that caught THESE THREE, and none of
these three reached a landed file.**

> **★ CORRECTED AT THE POST-LANDING CHECK OF 2026-09-13. FORMER WORDING, PRESERVED (#12): "The
> read-back is the act that caught them and none reached a landed file."** **Read as a general
> statement that is FALSE, and this file is where it fails.** More instances of the same error were in
> this file when it landed and were caught only at the post-landing check — among them 8.1's own
> *"Four requests"* above a list of five, 3.9's heading, and 5.3's *"three of them losing probability
> mass"*. **The sentence is true of the three items numbered above it and of nothing wider.** The full
> account is §10.

### 8.4 What the sweep for absolutes struck

Every hit was read at its own line. **Named rather than counted, with the former wording quoted so the
change is inspectable.**

- **3.9** read *"This is the single largest structural fact about the analytical side."* **Struck** — a
  superlative over this side's own judgment of the paper's parts, derived from nothing.
- **3.5** read *"So the whole harmonic transition model is …"* and then *"There is no key, no
  functional relation, and no distinction among the ten non-fifth roots."* **The "whole" is struck and
  the negative is bounded to the sixteen pages as read** (the count being separately wrong, 8.3).
- **C1** read *"The paper's own Table 3 is the one place it could test this on harmony."* **Bounded to
  the pages as read, and balanced**: Table 2 shows the unified model ahead on the metrical axis, so
  the promise is not refuted either, and the entry now says so.
- **The "what the paper does NOT report" subsection — now 6.7, renumbered when Figure 6 took 6.5 —
  read** *"No uncertainty of any kind on any figure."* **Replaced** by the named absences — confidence
  interval, error bar, significance test — each bounded to the pages as read.
- **7.4** read *"THIS IS THE ONE DEFECT HERE THAT COULD MOVE A VALUE A LATER READER LIFTS."*
  **Reworded** to place it against the other defects recorded in that section rather than as a
  superlative.
- **5.2** read *"A consumer gets no quality, no key, no numeral, no inversion, no bass, and no boundary
  that is not a tactus beat."* **Kept, but now says that each of those absences is stated by the paper
  rather than inferred here.**

**And one bound added rather than removed:** **F15**'s closing sentence now says in terms that reading
the polyphonic extension as having been bought by dropping key is **this side's reading of two
descriptions set beside each other**, and that the paper does not characterise the change as a loss.

### 8.5 What these two acts did NOT do

**They did not open the first extract** — that is the next section's work. **They did not open the
progress record, `FRAMEWORK.md`, `population.md`, the findings surface, the slice derivation, or any
other extract.** **No web access of any kind was made**, so the source-code address at §1 is unvisited
and unasserted. **No repository sweep was run for this paper** — not for its author, not for its title,
not for any of its values — **so this extract asserts nothing about what the record says of it**, and
in particular **nothing about which verification target the candidacy row means when it calls this
paper "V4's primary."** **No shell command was run**, in the container or on the device.

### 8.6 The questions this extract leaves

**None is proposed as an act; each is recorded where the next reader will meet it.**

1. **§7.4 is the one a later reader must settle before lifting a figure**: Table 2's caption and its
   prose define `TD` and `UD` as each other's opposite, and the rows carry different numbers. **Three
   points fall on the prose's side and none on the caption's**, but this extract takes no verdict and
   a reader routing either row should carry the conflict with it.
2. **§7.5 leaves the fit/evaluation relation unsettled from these pages alone**: the paper does not
   say whether the miscellaneous classical corpus it tuned parameters on overlaps the Kostka–Payne
   corpus it then reports figures on. **No overlap and no absence of overlap is asserted here.**
3. **§7.6 records a gap in the paper's own argument, not an error**: the lost-probability-mass defence
   is made for choosing among structures of one note pattern, and §5 then uses `P(N)` to compare
   different note patterns.
4. **The 2.1-point gap at 6.4 is the figure most likely to be lifted from this paper, and 6.4 states
   its bound at the same place**: it is one model given the correct metre against a different model
   inferring its own, not one model measured with and without.

---

## §9 — The cross-check against the first extract

**Written after this file had landed carrying §1 to §8, and after — and only after — the first extract
was opened for the first time.** That is step 7 of the hundred-and-sixty-ninth handoff entry's §3
procedure, and the order was kept.

The first extract is
`reading_pass/extracts/temperley-2009-unified-probabilistic-model-polyphonic-music-analysis.md`,
**31,377 bytes, read whole in one call.** It is dated 2026-09-05 and was written by the session that
booted on the hundred-and-fifteenth handoff entry. **Its file name differs from this one's** — it omits
the word *for* — which is why this file does not sit beside it under a matching name.

### 9.1 What agreed

**EVERY NUMERIC VALUE THE TWO EXTRACTS BOTH TRANSCRIBED AGREES, DIGIT FOR DIGIT.** Named rather than
counted: Table 1's **71.5 / 22.3 / 2.4**; Figure 4's **.003 / .01 / .43 / .37**; the **50**
distributions of which **all but 8** are binary; the **over 6000** Essen folk songs; **600–800 ms**;
**50 ms** pips; **300 ms**; **46** and **19** excerpts; the **within 10%** tolerance; Table 2's tactus
row — **37/46 (80.4%)** against **32/46 (69.6%)** quantized and **14/19 (73.7%)** each performed; Table
3's **80.8 / 76.5 / 78.7**; Figure 7's **−140.0 / −161.9 / −146.4 / −143.1**; the file's **1,444,387**
bytes; **sixteen** pages, printed **3–18**; and the DOI. **Not one of the disagreements below carries a
digit.**

**★ AND THE TWO READS AGREE ON THE PAPER'S CENTRAL STRUCTURAL FACT, INDEPENDENTLY.** The first
extract's finding (1) is headed *"THE PAPER DOES NOT DECIDE TONALITY AND CHORD TOGETHER; IT DECIDES
METER, ROOT-HARMONY AND STREAMS TOGETHER, AND SAYS SO."* **This side reached the same place without
sight of that**, at **F15** and at 3.1 and 3.5. **Two independent whole reads, both finding no tonality
anywhere in the model.** *(This side's F15 adds one thing the first extract does not carry: that the
monophonic predecessor the paper builds on DID analyse key, which the paper states at page 3.)*

Three further agreements worth naming:

- **Both reads met the stream-first decoupling as the analytical side's main departure from
  unification**, and both quote Equation 6 and the flat-meter, flat-harmony assumption.
- **Both reads met the two *ad hoc* moves that leave the generative model ill-defined**, and both
  record that neither carries a value for what it buys.
- **Both reads met the tuning-corpus question** — the first extract at its finding (5), this side at
  §7.5 — and **neither asserts overlap or its absence.**

### 9.2 The decisive questions the first extract left, and what happened to each

The first extract's **Centrality** section names them: *"its decisive questions are finding (1) —
whether any passage of the paper decides or labels a tonality, which this read says none does — and
whether any value is attached anywhere to the cost of the tactus-only restriction or to the resolution
penalty."*

**BOTH ARE ANSWERED, by agreement of two blind reads.**

1. **No passage of the paper decides or labels a tonality.** This side read all sixteen pages whole
   **without knowing the question had been asked** and met none; F15 and 5.3 record it, resting on the
   paper's own page-4 sentence that the labels are *"simply roots"* and on page 12's *"has not been
   attempted yet"*.
2. **No value is attached to either.** The tactus-only restriction's cost is *"only a small loss of
   accuracy"* with no figure (3.5), and the *ad hoc* penalty *"seems justified by the resulting
   improvement in performance"* with no figure (3.9, C4). **This side's 6.7 states both as negatives
   over the sixteen pages as read.**

**★ THE BOUND ON THAT, SAID PLAINLY.** Two independent whole reads met nothing is not the same as
nothing being there. **What is established is that two readers, reading the whole paper without sight
of each other, both met nothing** — which is what the doubling is for and is stronger than either read
alone.

### 9.3 What the cross-check ADDED to this extract

**One thing, and it came from the first extract's own observation rather than from a disagreement.**

**Table 1 has no row for metrical level 0**, while the model's grid has four levels numbered 0 to 3.
The first extract notes it in one clause — *"the model's grid has 'four levels, numbered 0 through 3'
(p. 6), so level 1 is not its lowest level; Table 1 lists no level-0 row"* — and this side had missed
it. **Confirmed at printed page 6 at this cross-check, and now recorded at 6.2 with what follows from
it:** the restriction of harmonic change to tactus beats excludes both sub-tactus levels, and the
evidence offered for the restriction measures one of them and is silent about the other.

**This side found nothing else in the first extract that this extract lacked on the paper's own side.**
Its findings (1), (2), (3), (5), (6) and (7) reach beyond the paper to `FRAMEWORK.md`, the candidacy
list, the slice derivation, the reading order and the findings surface — **none of which this sitting
opened** — so this side has checked none of that half and takes no position on it.

### 9.4 Where the paper goes against the FIRST extract — recorded, and that file left untouched

**Three, named rather than counted, each resolved at the paper. None moves a value; one of them moves
what a sentence establishes.**

1. **★ A LOAD-BEARING PARENTHESIS DROPPED FROM A QUOTATION.** The first extract quotes page 4 as
   *"changes of harmony occur on about 71% of level 3 beats, 22% of level 2 beats, and only 2% of level
   1 beats."* **The paper prints *"22% of level 2 beats (which are not level 3 beats)"*** — confirmed at
   page 4 at the whole read, at the read-back and again at this cross-check, three readings. **The
   parenthesis is not decoration.** In a metrical hierarchy every level-3 beat is also a level-2 beat,
   so without it the three figures read as overlapping populations rather than as a partition, and
   22.3% reads as the rate over all tactus beats instead of over the tactus beats that are not also
   upper-level beats. **No ellipsis marks the omission.** *(What it does NOT do: the table itself is
   transcribed correctly in both extracts, and the first extract's own analysis elsewhere treats the
   levels correctly — this is a defect in one quotation, not in its reading.)*
2. **A word changed inside a quotation.** The first extract quotes page 11 as *"the metrical/harmonic
   analysis process … **depends on** the concept of a 'tactus-root combination'"*. **The paper prints
   *"uses* the concept"** — read three times at three separate page requests. **Nothing turns on it**;
   the sense is the same.
3. **A word this side and the first extract read differently, resolved in this side's favour on two
   readings and recorded with its likely cause.** The first extract quotes the Equation-4 gloss as
   *"dependent on all three structural **representations**"*; **this side reads *"all three structural
   elements"*** at every request of printed page 6 it made — the whole read, the read-back's held 4–6
   and this cross-check's held 2–4, three in all. *(★ "at two separate requests of page 6" at the
   post-landing check; corrected to three.)* **The phrase *"structural representations"* does
   occur on that same page**, in the left column — *"a Bayesian transcription system really requires
   that any structural representations that affect P(N) be integrated into a single generative
   model"* — **which is a plausible source for the other reading.** **Nothing turns on it.**

**One smaller thing, recorded as a citation precision rather than a defect:** the first extract
attributes the probability-mass statement to *"footnote 3, p. 10"*. **The statement that the mass falls
below 1 is in the body of page 10**; footnote 3 carries the separate argument that a uniform adjustment
would leave the argmax unchanged. The page is right.

**THE FIRST EXTRACT WAS NOT EDITED.** This side recorded these and left that file untouched, on the
same ground the preceding sittings of this line gave for rows 27, 28 and 1: **rewriting another read's
text destroys what the doubling compares.** **Whether they are corrected at their own site is the
user's**, and item 1 is the first of these to be worth putting to him on its own account, because a
later reader lifting that quotation would carry a figure attached to the wrong population.

### 9.5 What the cross-check did NOT do

It **opened no page of the paper except printed pages 4, 5, 6 and 11**, and those only to resolve the
disagreements above and to confirm the Table 1 observation. It **read no other extract**, **did not
open the progress record**, **did not open `FRAMEWORK.md`, `population.md`, `candidacy_upgrades.md`
beyond row 8's own line, the slice derivation, the findings surface or the V4 stop memo** — all of
which the first extract's findings rest on and **none of which this side has checked**. It **ran no web
access and no shell command**. It **moved no verdict**, **flipped no row**, **routed nothing**, and
**edited no file but this one**. It **changed no transcribed value**: every figure, table, equation and
quoted measurement above stands exactly as it was first landed, and the sites it edited are **named
rather than counted** — 3.3's note on the disputed word, and two additions at 6.2, the level-0 gap and
the note on the parenthesis — with nothing removed. *(★ "the corrections it made are at three sites" at
the post-landing check; the edits were three but they fall at two locations, and the sentence counted
the one that was edited twice as two sites.)*

---

## §10 — The user-ordered fact- and source-check, run after this file had landed

**Written in the act that ran it, 2026-09-13.** The user's standing rule of 2026-09-12 extends the
pre-landing check to landed work on four axes — completeness, coherence, correctness, and misuse of
hyperbole and absolutes — and he ordered it on this sitting's writing. **This file was re-read WHOLE as
landed, at the device's own copy staged back, at 83,198 bytes.**

**Every defect it found is corrected above at its own site with the former wording preserved (#12).
Named rather than counted:**

- **★ A COUNT CONTRADICTED BY THE LIST IT INTRODUCES, IN ONE SENTENCE.** §8.1 read *"Four requests were
  made after the whole read, named rather than counted:"* and then named **five**. The clause that
  invokes the name-rather-than-count rule is the clause that broke it.
- **A heading contradicted twice by its own section.** §3.9 was headed *"the three declared
  approximations"* where F11 names four and 3.10 calls Equation 9 the fourth.
- **A fact corrected at the read-back and left uncorrected in a second place.** 5.3 still read *"Four
  approximations, three of them losing probability mass"* after F11 had been corrected from three to
  two.
- **A wrong page number, contradicted by this file's own §5.4.** §1 said this paper cites Raphael &
  Stoddard on *"pages 3, 6 and 11"*; the characterising citation is on printed page **4**, which §5.4
  quotes correctly. *"Cites"* is now bounded to the body, the reference list carrying a fourth
  appearance.
- **Two more undercounts of this side's own page requests**, at §9.4's *"two separate requests of page
  6"* (three) and at §9.5's *"three sites"* (three edits at two locations).

**★ WHAT THIS CHECK ESTABLISHES ABOUT THE SITTING, AND IT IS THE FINDING THAT MATTERS MOST.** §8.3
closed by saying the read-back caught this file's miscounts and that **"none reached a landed file"**,
and the hundred-and-seventy-first handoff entry's (x) said the same of the sitting as a whole. **Read
as a general statement that is FALSE.** Four further instances of the same tell — a number put on this
side's own reading without deriving it — **were in this file when it landed**, and its companion
extract carried four more. **§8.3 is corrected at its own site, and so is the entry.** The tell did not
stop at the read-back; the post-landing check is what caught the rest, and nothing establishes that it
caught all of them.

**One thing recorded rather than corrected:** the FACT list runs **F13, F15, F14** — F15 was inserted
before F14 when the read-back added it. **The numbers are not renumbered**, because 5.2, 5.3 and §9.1
cite F15 by name and renumbering would break those references. A reader meeting F15 before F14 is
meeting an insertion, not a gap.

**What this check did NOT do.** It fetched no page image, opened no paper, opened neither first
extract, ran no web access, swept no repository, and **edited no file but the three this sitting
wrote**. It **moved no verdict, routed nothing, flipped no row**, and **changed no transcribed value**:
every figure, table, equation and quoted measurement above stands exactly as it was first landed. It
reaches this sitting's own writing and nothing else.
