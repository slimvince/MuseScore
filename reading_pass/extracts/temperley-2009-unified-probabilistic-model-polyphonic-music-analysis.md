# EXTRACT — Temperley 2009, "A Unified Probabilistic Model for Polyphonic Music Analysis" — Task B candidacy row 8, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-05).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All sixteen pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints the journal's own page numbers, 3 to 18; every location below is the printed
> journal page and the paper's own section.
>
> **Why this paper and its place in L2's slice.** It is row 8 of `reading_pass/candidacy_upgrades.md`,
> ADMITTED there as *"The unified probabilistic model the hypothesis names; it is also V4's primary, but
> it is admitted for its method."* That file's own "READING PROGRESS" block records it as the one
> borderline of the L0+L1 slice: *"Row 8 supplies L1's metric-strength ground, but its METHOD is L2's
> joint model, so it stays in the L2 slice; its L1-bearing value is already read at the object and ruled
> (the V4 divergence, Ruling 2)."* `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 places it in L2's
> slice on the same ground. It is fourth in group 1 of the proposed reading order ("the joint
> tonality-and-chord decision"), after rows 27, 28 and 1. Ruling 1 of
> `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before L2's slice of
> Task B is read. This is the fourth member of that slice read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

David Temperley (Eastman School of Music, University of Rochester), "A Unified Probabilistic Model for
Polyphonic Music Analysis", *Journal of New Music Research* 2009, Vol. 38, No. 1, pp. 3–18 (DOI
10.1080/09298210902928495, © 2009 Taylor & Francis). Six sections (Introduction; The generative
process; The analytical process, with 3.1 Overview, 3.2 The stream analysis process, 3.3 Metrical and
harmonic analysis; Testing the analytical model; Transcription; Conclusions), nine figures, three
tables. Footnote 1 (p. 3) names the source code as downloadable, written in C ("melisma2").

**File:** `docs/research_papers/temperley_2009_jnmr_unified_probabilistic_polyphonic_analysis.pdf`
(1,444,387 bytes at the listing). The printed title and author match the bibliography's row exactly
(`docs/research_papers/BIBLIOGRAPHY.md` line 22).

## Claims, labeled

### What the method decides — and what it does NOT decide

**★ [FACT, p. 3, Abstract]** *"Taking a note pattern as input, the model combines three aspects of
symbolic music analysis — metrical analysis, harmonic analysis, and stream segregation — into a single
process, allowing it to capture the complex interactions between these structures. The model also
yields an estimate of the probability of the note pattern itself; this has implications for the
modelling of music transcription."*

**★ [FACT, p. 4, §1] THE HARMONIC STRUCTURE IS A SEGMENTATION LABELLED WITH ROOTS ONLY. NO TONALITY IS
DECIDED ANYWHERE IN THE MODEL.** *"A harmonic structure is a segmentation of a piece into time-spans
labelled with chords; for our purposes the labels are simply roots, though they could also carry more
specific information, e.g. chord quality (major versus minor) or relationship to the key (e.g. 'I of C
major')."* And at the end of §3.3 (p. 12): *"a natural further step would be to expand the harmonic
possibilities, e.g. using key-specific names for chords (I/C, V/F, etc.); this would yield a richer
harmonic analysis and might improve the metrical analysis as well. This has not been attempted yet,
however."* Figure 1 (p. 5) shows the output: per lowest-level metrical segment, one root letter (G or
C), the four-level metrical grid, and the notes grouped into two streams. **What is decided jointly is
meter, root-harmony and stream membership — not tonality and chord.** See finding (1) below.

**★ [FACT, p. 4, §1] The metric-strength evidence, as the text states it, with the table values
reproduced.** *"Regarding the interaction of meter and harmony, it can be seen from almost any harmonic
analysis that changes of harmony tend to occur on relatively strong beats: generally at strong tactus
beats, and very rarely below the level of the tactus."* *"If we define the tactus level as level 2, the
level immediately above as level 3, and the level below as level 1, changes of harmony occur on about
71% of level 3 beats, 22% of level 2 beats, and only 2% of level 1 beats."* Table 1 (p. 6), caption
*"Harmonic changes at beats of different metrical levels in the Kostka–Payne corpus"*, column headings
*"Metrical level (2 = tactus)"* and *"% of beats with changes of harmony"*: level 3 — 71.5; level 2 —
22.3; level 1 — 2.4. The model's grid has *"four levels, numbered 0 through 3"* (p. 6), so level 1 is
not its lowest level; Table 1 lists no level-0 row. **This reproduces at the object exactly what the V4
divergence memo and the corrected `FRAMEWORK.md` clause state; nothing new moves.**

**[FACT, p. 4, §1] The paper itself names the fixed-grid alternative and its author:** *"[Others, such
as Raphael and Stoddard (2004), have finessed the problem by limiting the possible points of harmonic
change to a high metrical level such as bars or half-bars.]"* — and states that the influence runs
both ways: *"if a strong beat indicates a high probability of a harmonic change, it is hardly surprising
that the clear presence of a harmonic change would suggest a strong beat."*

### The generative process (§2)

**★ [FACT, p. 6, eq. 4] The factorisation.** P(M, H, S, N) = P(N | M, H, S) × P(H | M) × P(S | M) × P(M).
*"Essentially, the model first generates a metrical structure; it then generates harmonic and stream
structures (these structures are dependent on the meter but independent of each other); finally, it
generates the note pattern, which is dependent on all three structural representations."* Time is
discretised into *"pips"* 50 ms apart; *"note-onsets and offsets as well as structural events (beats,
changes of harmony, and stream beginnings and endings) may only occur at pips."*

**[FACT, p. 6–7, §2] The metrical grid** has four levels; level 2 is the tactus; the first tactus
interval is drawn from a distribution favouring 600–800 ms; each subsequent one is conditional on the
previous, *"favouring a tactus level that is roughly regular, but allowing some fluctuation"*; L3 and
L2 may be duple or triple, L1 is assumed duple; the phase of L3 is chosen; *"The metrical grid is
assumed to begin and end on tactus beats."*

**★ [FACT, p. 7, §2] HARMONIC CHANGE IS RESTRICTED TO TACTUS BEATS BY CONSTRUCTION, ON TABLE 1'S
EVIDENCE, AND THE COST OF THE RESTRICTION IS ASSERTED, NOT MEASURED.** *"An important simplification
here is that harmonic changes are allowed only on tactus beats. (As shown in Table 1, it appears that
only a very small percentage of harmonic changes are on sub-tactus beats, so excluding this possibility
results in only a small loss of accuracy.) Thus the model's task is simply to choose a root for each
tactus interval."* No value is attached to *"only a small loss of accuracy"* anywhere in the paper.

**★ [FACT, p. 7, §2] The root transition model.** *"For the first tactus interval, a root is chosen out of
a uniform distribution. For each subsequent interval, the model first decides whether to continue the
previous root or to change to a new root; the probability of change is higher for L3 beats than L2
beats, reflecting the greater likelihood of chord changes on stronger beats (see Table 1). If a new
root is chosen, there is a high probability of moving to a root that is a perfect fifth above or below
the previous one, reflecting the well-known preference for root motion by fifths in Western music; all
other roots are assigned the same low probability."* Two things follow and are stated so they are not
inferred later: the change-versus-continue decision is conditioned on the metrical level of the beat —
**the meter–harmony coupling is a conditional probability in the root chain**; and the transition
vocabulary is root-interval only, with no notion of function, degree or tonality.

**[FACT, p. 7, §2] Streams** begin and end only at tactus beats (*"This constraint has no musical
justification, but is made simply to limit the space of possible streams"*), a Poisson-distributed
number of new streams per tactus beat, and *"streams in themselves are not assigned to specific pitches
or even to any pitch range."*

**[FACT, p. 7–8, §2] Note onsets by "metrical anchoring"**: the probability of an onset at a weak beat
depends on whether notes are present at the surrounding higher-level beats within the same stream
(Figure 4, Essen folksong data: unanchored .003, pre-anchored .01, post-anchored .43, both-anchored
.37); offsets are generated at subsequent tactus beats with a stochastic continue-or-end decision, and
a note ends with probability 1 where the next note in its stream begins.

**★ [FACT, p. 8, §2] The pitch emission is per note, conditioned on the current ROOT and the previous
pitch in the same stream.** *"Finally, a pitch is chosen for each note-onset generated. This is
conditional on the current harmony and the previous pitch within the stream. We create a 'proximity
profile', a normal distribution centred around the previous pitch (Temperley, 2007); a 'chord-profile'
is also generated, which favours notes that are chord-tones of the current root and also slightly
favours notes within the major and minor scales of the current root."* The two profiles are multiplied
and normalised. **The "scale" in the chord-profile is the major or minor scale built on the current
root, not the scale of any tonality** — the paper has no tonality to condition on.

**[FACT, p. 8, §2] The parameter count and how the parameters were set.** *"The program contains
exactly 50 probability distributions; all but 8 of these are binary distributions, i.e. variables with
just two values (thus requiring only one parameter value). Where possible, the variables were set using
corpus data; most of the metrical parameters were set using the Essen folksong corpus, a large corpus
of over 6000 European folk songs (Schaffrath, 1995). Other parameters were set using trial-and-error
testing on a miscellaneous corpus of classical pieces."* Whether that miscellaneous corpus is disjoint
from the Kostka–Payne test corpus is not stated (see the scope limits below).

### The analytical process (§3)

**★ [FACT, p. 9, §3.1–3.2] The search is NOT a joint decode over all three structures; the stream
structure is found FIRST, assuming a flat meter and a flat harmony, and then held fixed.** Equation 6:
P(M, H, S₁, N) ≈∝ P(M, H, S₂, N) *"as M and H are varied"*. *"Thus if one wishes to find {M, H, S}*, this
can be done by assuming any metrical and harmonic structure Mₓ and Hᵧ and finding argmax[S] P(Mₓ, Hᵧ,
S, N); by assumption, this will also be the S of {M, H, S}*."* The assumed meter is *"one in which there
is just one row of beats roughly 300 ms apart"*; *"With regard to harmony, we assume a completely 'flat'
harmonic profile so that all pitch-classes are equally likely."* The author's stated ground: *"it
appears also that the most probable stream structure for a note pattern can be inferred with reasonable
accuracy without consideration of meter and harmony … there are relatively few cases where the
inference of streams seems to require knowledge of metrical and harmonic information."* The stream
search is a dynamic programme over columns of a pseudo-beat × pitch array (§3.2, Figure 5), with two
further well-formedness constraints (no crossing, no shared square) the author acknowledges are *"not
part of the generative process"* and cost probability mass (footnote 3, p. 10).

**★ [FACT, p. 11, §3.3] Meter and harmony are then decided TOGETHER by dynamic programming over
"tactus-root combinations".** *"The first stage of the metrical/harmonic analysis process (the
identification of the harmony and levels 0, 1, and 2 of the meter) depends on the concept of a
'tactus-root combination' (TRC): the combination of a hypothetical tactus interval (two adjacent tactus
beats) and a root. The essential idea is that the probability of a certain TRC depends only on the
previous TRC, and the probability of beats and notes within the TRC depends only on the TRC. Viewed in
this way, the metrical/harmonic analysis process can be viewed as a rather complex kind of hidden
Markov model."* For each candidate tactus interval the best L1/L0 subdivision is found by exhaustive
search; pitch probability *"depends only on the current root, which we know, and the interval to the
previous pitch within the stream, which we also know."* The DP proceeds left to right over pips with
the usual traceback (p. 12; footnote 5 allows the first tactus beat a range of positions).

**★ [FACT, p. 11, §3.3] A NON-CHORD-TONE PENALTY CONDITIONED ON MELODIC RESOLUTION, ADDED OUTSIDE THE
GENERATIVE MODEL.** *"In assigning pitch probabilities, we also assign a penalty (a reduction in
probability) for any note that is not part of the harmony and is not followed by stepwise motion. This
is, once again, an ad hoc move that is not reflected in the generative process and results in some loss
of probability mass, but it seems justified by the resulting improvement in performance."* No value is
given for the improvement.

**[FACT, p. 12, §3.3] Level 3 is found in a second pass, and the harmony is re-decided with it.** *"We
also redo the harmonic analysis at this stage, considering each possible root for each tactus interval,
on the reasoning that the addition of L3 may affect the most optimal points for harmonic change."* The
L3 pass factors *"a somewhat higher probability for harmonic changes and note-onsets at L3 beats than L2
beats"* and phase scores.

### The experiments, as stated (§4)

**[FACT, p. 12–13] Corpus and measurement.** The Kostka–Payne corpus: *"a set of 46 excerpts from the
common-practice repertoire from the workbook accompanying Kostka and Payne's (1995) theory textbook,
with harmonic analysis (showing keys and Roman-numeral chord symbols) done by the authors"*, converted
to MIDI as in Temperley (2001), *"the harmonic analyses were encoded by Bryan Pardo"*; plus 19 of the
excerpts performed by *"a semi-professional pianist"*. Harmonic accuracy is *"the proportion of time in
the entire corpus that the model assigns the correct root."*

**★ [FACT, p. 12, Table 2] Metrical result.** Tactus level correct (within 10 % of the correct tactus
length): probabilistic model 37/46 (80.4 %) against Melisma 32/46 (69.6 %) on the quantised corpus;
14/19 (73.7 %) each on the performed corpus; on the other four metrical statistics the author calls the
two models *"very similar in their level of performance"* (quantised) and *"very close"* (performed).
*"Inspection of the output suggests that the probabilistic model's consideration of harmony is a
crucial factor in its superior performance."* Figure 6 shows one case.

**★ [FACT, p. 13, Table 3] Harmonic result, with the author's own statement that the comparison is not
fair in either direction.** Melisma model 80.8 % of total time correctly labelled; Pardo & Birmingham
2002 76.5 % of minimal segments correctly labelled (their model *"also identifies chord quality
(major/minor/diminished), and they required correct chord quality for a correct answer"* — Table 3's
own footnote); probabilistic model 78.7 % of total time. *"the Melisma model was given the correct
metrical structure (as indicated by the score). By contrast, the polyphonic model must infer the
metrical structure on its own, and is not always correct … Thus the Melisma model has a significant
advantage. Even so, the Melisma model performs only slightly better than the polyphonic model."*
**The stream component is not evaluated at all:** *"this is difficult to test; it is frequently unclear
in common-practice music what the 'correct' analysis would be, and no annotated corpora are
available."*

### Transcription (§5) and conclusions (§6)

**[FACT, p. 13–17, §5]** P(N) is estimated by summing over meters and harmonies at the single best
stream structure (eq. 9); Figure 7 shows the Bach minuet and three altered versions assigned lower log
probabilities (−140.0 original against −161.9, −146.4, −143.1). The transcription system — a chunked
back-and-forth between this "prior model" and a signal model via pitch × pip arrays — is *"still under
development"*; only the prior-model half is complete. Nothing of §5 bears on any charter and nothing is
carried out of it beyond this note.

**[FACT, p. 17, §6] The author's own list of what the model lacks:** *"more detailed knowledge about
harmony (knowledge of functional harmony and of stylistic progressions such as cadences), knowledge of
conventional phrase structures (the norm of 4-bar phrases), and awareness of repeated melodic patterns
or 'parallelisms'"*, with the two challenges named as integrating such knowledge into the generative
process and keeping inference tractable.

## Measured results, as the paper states them

| Result | Corpus | Metric | Value |
|---|---|---|---|
| Harmonic change by metrical level (Table 1) | Kostka–Payne | % of beats at that level with a change of harmony | L3 71.5; L2 (tactus) 22.3; L1 2.4 |
| Tactus correct (Table 2) | Kostka–Payne, quantised, 46 excerpts | count correct within 10 % of true tactus length | probabilistic 37/46 (80.4 %); Melisma 32/46 (69.6 %) |
| Tactus correct (Table 2) | Kostka–Payne, performed, 19 excerpts | same | 14/19 (73.7 %) both |
| Root accuracy (Table 3) | Kostka–Payne | % of total time correctly labelled | probabilistic 78.7; Melisma (given the correct meter) 80.8 |
| Root accuracy (Table 3) | Kostka–Payne | % of minimal segments correct, quality required | Pardo & Birmingham 2002: 76.5 |
| Stream analysis | — | — | **not evaluated** (no annotated corpus, p. 13) |
| Cost of the tactus-only restriction on harmonic change | — | — | **asserted "small", no value** (p. 7) |
| Gain from the non-chord-tone penalty | — | — | **asserted, no value** (p. 11) |

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A MIDI or piano-roll note list — on-time and off-time in
milliseconds and pitch per note (p. 4); no time signature, no bar lines, no key signature, no spelling
(pitch numbers only), no voices (streams are inferred), no dynamics. Timing may be quantised or
performed. Nothing about tonality is read in; nothing about tonality is produced.

**What it HANDS downstream.** Per lowest-level metrical segment (Figure 1): one root letter; the
four-level metrical grid; a stream number per note; and, for transcription, the probability of the
note pattern. It hands on **no tonality, no mode, no scale degree, no chord quality, no inversion or
bass, no chord-tone assignment as a published fact** (the chord-profile and the resolution penalty live
inside the emission), **no cadence, no figured bass, and no alternatives or confidences** — the single
argmax structure is chosen and traced back (§3.3), and the summed probability of eq. 9 is used only for
P(N), never published per segment.

**Its own STATED SCOPE and limits.**
- **Harmonic vocabulary:** roots only; twelve pitch-class roots; the extension to key-specific names
  *"has not been attempted yet"* (p. 12).
- **Segmentation:** harmonic change only at tactus beats, by construction (p. 7); a stream begins and
  ends only at tactus beats, by construction with *"no musical justification"* (p. 7).
- **Search:** streams first under flat meter and flat harmony (eq. 6), then meter L0–L2 and harmony
  jointly, then L3 with the harmony re-decided; the second and third stages are exact dynamic
  programmes over the state the paper defines, the first-stage decoupling is an approximation the
  author defends qualitatively (p. 9).
- **Fitting:** 50 distributions, most set from the Essen folksong corpus (monophonic folk song, not
  the test repertoire), the remainder by trial and error on *"a miscellaneous corpus of classical
  pieces"* whose relation to the test corpus is not stated (p. 8).
- **Evaluation:** one corpus of 46 excerpts (19 also performed); root-only harmonic accuracy by time;
  the stream component unevaluated; the two comparators not comparable on the author's own account
  (p. 13).
- **Repertoire:** *"intended primarily for traditional Western art music ('classical' music), but may
  be applicable to other styles as well"* (p. 3).
- **Named ad hoc moves that leave the generative model ill-defined:** the stream well-formedness
  constraints (p. 10, footnote 3) and the non-chord-tone resolution penalty (p. 11), both acknowledged
  as losing probability mass.

## What an L2 (or L1) detail specification could adopt, adapt, or must argue against

- **Adopt (as a shape, for L1's metric-strength ground — already ruled):** the change-versus-continue
  decision conditioned on the metrical level of the beat, learned from Table 1's gradient. The charter
  already rests on this (the corrected V4 clause); this read adds the paper's own mechanism for using it.
- **Adopt (as a documented precedent for DP-C's "with", read carefully):** the segmentation is decided
  jointly with the labelling — each tactus interval's continue-or-change decision is inside the same
  dynamic programme that chooses the root — and the paper reports the meter-and-harmony joint decision
  beating the meter-alone comparator on the tactus (Table 2, with the author's inspection attributing
  the gain to harmony). **But the candidate boundaries are a metrical grid, not note change points**, so
  this is at once a precedent for joint segmentation and the rival the L1 charter's change-point
  construction argues against.
- **Adapt (for DP-D and D-527's shape):** a per-note emission conditioned on the current harmony and on
  a chord-independent melodic covariate (the previous pitch in the same stream), with a further penalty
  for a non-chord tone not followed by stepwise motion — the 2009 form of "emit each tone by category
  conditioned on melodic covariates". Two cautions travel with it: the penalty is outside the generative
  model and unvalued; and "harmony" here is a bare root, so chord-tone membership is root-membership.
- **Adapt (for the L2 charter's coupling question, by contrast):** this paper is the clearest published
  case of a **first-stage decoupling defended qualitatively** — streams found under flat harmony because
  *"relatively few cases"* need it — beside a **second-stage full coupling** of meter and harmony. A
  detail specification that decouples anything can cite the argument's shape; it cannot cite a
  measurement of what the decoupling costs, because none is given.
- **Must argue against:** the tactus grid as the only admissible harmonic boundary (the L1 charter's
  change points are exhaustive; the paper's own Table 1 shows 2.4 % of level-1 beats carry a change,
  and the cost of excluding them is asserted, not measured); root-only labels with no tonality and no
  quality; pitch numbers without spelling (L0 gives spelling); the single-path output with no
  alternatives and no confidence; and stream membership inferred rather than read (the voices are in
  the file here — the same boundary as row 1's).

## ★ Findings, routed and not applied

**(1) THE PAPER DOES NOT DECIDE TONALITY AND CHORD TOGETHER; IT DECIDES METER, ROOT-HARMONY AND STREAMS
TOGETHER, AND SAYS SO. The record's characterisation of it as "L2's joint model" and its placement in
reading group 1, "the joint tonality-and-chord decision", are IMPRECISE at the object.** The
bibliography row, `candidacy_upgrades.md` row 8 (*"admitted for its method"*), the borderline note
(*"its METHOD is L2's joint model"*), the slice derivation row 8 (same words) and the reading order's
group 1 all carry or inherit the reading that this is a joint-decode paper of the Raphael & Stoddard
kind. At the object the harmonic labels are *"simply roots"* (p. 4) and the key-specific extension
*"has not been attempted yet"* (p. 12). **What this does and does not move:** the row's ADMISSION
stands — its method (joint segmentation-with-labelling on a metrical grid; a per-note emission with a
melodic covariate; a meter–harmony conditional coupling) is a live candidate or rival for L1 and L2
decisions, which is the criterion — but its group is wrong: by the reading order's own group
definitions it belongs with group 2 (*"segmentation decided with the labelling"*) and with group 5
(L1's cues, beside row 7), not with the tonality-and-chord group. **No chosen design point's ground
rests on this paper being a tonality-and-chord model** (`FRAMEWORK.md` cites it only for the metric-
strength count; alternative (f) names Raphael & Stoddard, not this paper), so **no verdict moves and no
STOP fires**. ROUTED to the user as a precision on the derivation's characterisation and on the
proposed order — *stated, not ruled* by that file's own words — and applied nowhere; the remaining
group-1 members are unaffected.

**(2) The V4 figures and their attachment REPRODUCE at the object, in two places.** Table 1 (p. 6) and
the running text (p. 4, *"about 71% of level 3 beats, 22% of level 2 beats, and only 2% of level 1
beats"*) both attach 71.5 % to the level above the tactus; the model carries a level 0 below level 1
(p. 6). The corrected `FRAMEWORK.md` clause and the STOP memo's wording are exactly what the paper says.
**Nothing new; recorded because the record said this value was read and ruled, and a whole read is the
occasion to confirm it did not depend on one table alone.** Option B of the V4 surface (a further
finding of this paper deliberately not brought into the charter) is not re-raised here; the tactus-only
restriction that finding concerns is stated above as a FACT of the paper with its unvalued cost.

**(3) DP-C — a "with" instance whose boundary set is a GRID, with the grid's cost asserted and never
measured.** The paper is evidence that deciding segmentation with labelling pays on the metrical side
(Table 2) — ENRICHES-shaped for the chosen "with" — and at the same time a rival instance for the L1
charter's boundary construction, because its candidate boundaries are tactus beats rather than note
change points, and its only defence of that is Table 1 plus the unvalued *"only a small loss of
accuracy"*. Routed to the findings surface's DP-C block and to the L1 and L2 detail specifications.

**(4) A second published precedent for the record's emission shape (D-527, DP-D), six years later than
row 1's.** Per-note emission conditioned on the current harmony and on a
chord-independent melodic covariate, plus an explicit non-chord-tone-resolution penalty — the latter
acknowledged ad hoc and unvalued. Routed to L2's detail specification as a FACT of this paper.

**(5) The fit/evaluation separation is NOT established at the object.** Some parameters were set by
trial and error on *"a miscellaneous corpus of classical pieces"* (p. 8) and the test is on the
Kostka–Payne corpus; the paper does not say whether they overlap. Under #20 the Table 2 and Table 3
values are carried with this bound attached, never as held-out figures. Routed to measurement design.

**(6) The two comparators in Table 3 are NOT comparable, by the author's own statement,** in opposite
directions (Melisma given the true meter; Pardo & Birmingham graded on quality as well as root). Any
later use of 78.7 / 80.8 / 76.5 as a ranking is unsupported at the primary. Routed to measurement
design beside (5).

**(7) No falsifier.** Nothing read contradicts any CHOSEN design point: the metric-strength ground is
confirmed at the corrected wording; the coupling of meter and harmony is a conditional in a chain, never
a veto; the grid is a rival at DP-C, not a refutation. **No STOP fires** under the remedial commission's
§5.

## Centrality

**CENTRAL, on a narrow ground.** A `[FACT]` in the L1 charter rests on this paper (ruled at V4 and
reproduced here), an L1 detail specification must argue against its grid, and an L2 detail
specification would cite its joint segmentation-with-labelling and its emission shape as precedents —
those claims would carry load. The ground is narrow because the paper's own harmonic vocabulary (roots
only, no tonality) keeps it out of the tonality-and-chord decision that gives group 1 its weight. A
second independent extraction under the original commission's §4 central-source rule is therefore
**owed**; its decisive questions are finding (1) — whether any passage of the paper decides or labels a
tonality, which this read says none does — and whether any value is attached anywhere to the cost of
the tactus-only restriction or to the resolution penalty. It has not been performed and is recorded here
as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `cowork_l2_task_b_slice_derivation_2026_09_05.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (6) are routed and written
nowhere else. It re-rules nothing about V4. It opens no code, touches no measurement tool, no corpus,
no golden and nothing under `tools/`. It writes no open-items row and allocates no decisions-register
identity. It reads no other paper and takes no decision about the order of the remaining slice; finding
(1)'s consequence for the order is the user's.

---

*Provenance: written 2026-09-05 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_fifteen.md` and performed the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived gating answer). Read for this
extract, at the files: `reading_pass/candidacy_upgrades.md` whole (row 8 at its line 70, the borderline
note at lines 207–209, the proposed order at lines 175–181); `reading_pass/l2_slice_reading_progress.md`
whole; `cowork_l2_task_b_slice_derivation_2026_09_05.md` at its row 8; `docs/research_papers/BIBLIOGRAPHY.md`
at line 22; `FRAMEWORK.md` at lines 352–373 (the metric-strength clause and its 2026-08-31 correction),
located with `Grep` on the staged copy, which found no other citation of this paper;
`cowork_reading_pass_findings_2026_08_31.md` at its V4 rows (lines 608 and 619–625);
`reading_pass/population.md` at its V4 row (line 105); `reading_pass/stop_v4_divergence_2026_08_30.md`
whole; both commissions whole; and the row 1 extract whole, for the form. The paper itself was read at
the object as page images, all sixteen pages. No shell command was run on the repository or on any staged
copy of it for content or for listings. No figure of this project's own measurement is restated (#17f,
D-431); every value above is the paper's own.*
