# EXTRACT — Pardo & Birmingham 2002, "Algorithms for Chordal Analysis" — Task B candidacy row 4, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All twenty-three printed pages (pp. 27–49) were read AT THE OBJECT: the held PDF
> staged through the bridge and read with the file tools as page images. **No relay, no web-fetch
> read, no prompted extraction.** Every quotation below was read from the page and carries its
> printed page number.
>
> **Why this paper and why first.** It is row 4 of `reading_pass/candidacy_upgrades.md`, ADMITTED
> there because *"it supplies L1's partition-point construction … and its tie-breaking residual is the
> measurement DP-C carries."* **Ruling 10 of `cowork_rulings_2026_08_31_decision_surface_sitting.md`
> made L0+L1 the first deriving subject**, and this is the load-bearing member of that subject's slice
> of Task B: the paper the L1 charter takes its own partition-point construction from.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Bryan Pardo & William P. Birmingham, "Algorithms for Chordal Analysis", *Computer Music Journal*
**26:2**, pp. 27–49, Summer 2002. © 2002 Massachusetts Institute of Technology. Artificial
Intelligence Laboratory, Electrical Engineering and Computer Science Department, The University of
Michigan.

**File:** `docs/research_papers/pardo_birmingham_2002_cmj_algorithms_chordal_analysis.pdf`.

## Claims, labeled

### The partition-point construction — L1's own territory

**★ [FACT, p. 28–29, restated p. 35]** The construction the L1 charter uses, in the paper's own
words: *"Harmonic change can only occur when at least one note begins or ends. A partition point
occurs where the set of pitches currently sounding in the music changes by the onset or offset of one
or more notes."* On p. 35: *"Harmonic change can only occur where notes begin or end. A point of
possible harmonic change is called a partition point, where the set of pitches currently sounding in
the music changes by the onset or offset of one or more notes."*

**[FACT, p. 29]** *"A segment is a contiguous interval between two partition points. A minimal
segment is the interval between two sequential partition points."* The ordered set of all partition
points for a piece is written `P_all`, its size `p` (p. 35).

**★ [FACT, p. 36]** *"The number of partition points is limited to a maximum of twice the number of
notes (one point for each note beginning and each note end)."*

**[FACT, p. 36]** The count of possible segmentations is `2^(p−2)`, the first and last partition
points being always included. Worked at the object: *"Bach's Sinfonia No. 1, a 21-measure solo
keyboard piece, has 341 partition points and thus 2^339, or roughly 10^102, segmentations."* A single
block chord where all notes begin and end together has `2^0 = 1` segmentation.

### What the labelling method is, and what it deliberately does not read

**[FACT, p. 28]** Seventy-two templates from six template classes, twelve members each (one per root
pitch class). The classes were chosen by frequency in the answer key: *"All chord qualities
accounting for at least 2% (when rounded) of the chord labels in the corpus were used."* The six, with
their stated proportions of the corpus (Table 2, p. 29): major triad 43.6%, dominant seventh 21.9%,
minor triad 19.4%, fully diminished seventh 4.4%, half-diminished seventh 3.7%, diminished triad 1.8%.

**[FACT, p. 29, Figure 3]** The segment content score is `S = P − (M + N)`: positive evidence `P` is
the summed weight of notes whose pitch class matches a template element; `N` the summed weight of
notes matching none; `M` the count of template elements matched by no note.

**★ [FACT, p. 30] The note weight is not duration.** *"the number of minimal segments a note spans
determines its weight. Note that this does not directly correlate to the absolute duration of the note
or to its notated rhythmic value. Rather, it correlates to the number of changes in the music the note
overlaps."* The authors tried duration- and velocity-based weightings: *"We tried a number of ad hoc
approaches to note weighting involving these parameters but found that the approach based on minimal
segments worked surprisingly well."*

**★ [FACT, p. 31]** *"No notion of tonal context, beat, absolute pitch height, or dynamics enters into
the calculation."* Restated in the conclusion, p. 46–47: *"metric information, key signature, harmonic
function, voice leading, and stylistic information were not used."*

**[FACT, p. 30, Figure 4]** Three tie-breaking rules, applied in order: **root weight** (choose the
template whose root pitch class has the greatest weight of notes present); **prior probability**
(choose the template with the higher corpus frequency); **dim7 resolution** (where all top templates
are fully diminished sevenths, choose the one whose root is a semitone below the root of the top
template in the following segment). The first two are context-free; **the third is contextual** and is
the only place the labelling system reads harmonic context at all (p. 35).

### Segmentation as a search, and its two algorithms

**[FACT, p. 36]** The problem is posed as a highest-reward path through a directed acyclic graph: one
vertex per partition point, one edge per possible segment, the edge's reward the segment's content
score. *"Any path from the first vertex to the last one represents a segmentation of the piece."*

**★ [FACT, p. 36] The assumption that makes it tractable, stated as an assumption.** *"For the purpose
of this analysis, we assume that individual segments may be scored without reference to their context.
The segment-labeling method described in this article has this property."* And: *"any system that
performs harmonic analysis must make assumptions to reduce the size of the search problem … The
framework we propose in this article limits context sensitivity in order to constrain the search
problem."*

**[FACT, p. 37]** Relaxation search over the DAG is guaranteed to find the highest-scoring path in
`O(E)`; edges number at most `p²/2`, and since `p ≤ 2n` the segmentation is found in `O(n²)` steps for
`n` notes.

**[FACT, pp. 39–40]** **HarmAn** is the greedy linear-time alternative: it considers exactly three
edges per partition point, giving `O(n)`. Worked at the object on the same piece: Relaxation needs
`(341²)/2 ≈ 58,000` steps; HarmAn `(341 − 2) × 3 = 668`. *"The catch is that a HarmAn search, unlike a
Relaxation search, does not explore all possible segmentations."*

## Measured results, as the paper states them

**Corpus for labelling (pp. 27, 31):** the **KP corpus** — 45 excerpts of tonal music compiled by David
Temperley from the teacher's edition of Kostka & Payne, *Tonal Harmony* (1984). The full excerpt list is
the paper's appendix, pp. 48–49 (Bach through Tchaikovsky; the excerpts are short, typically 8–20 bars).

**Grading metric (p. 31):** one point per minimal segment whose label exactly matches the answer key;
where the program returns several labels and the correct one is among them, the point is divided by the
number of guesses; segments whose answer is outside the system's vocabulary are not graded. The authors
call it *"a non-forgiving grading measure"* and say so twice.

**Table 4, p. 32 — mean label scores by tie-breaking regime (45 cases each):**

| Tie-breaking strategy | Mean % of piece with multiple labels | Mean score % | Std dev |
|---|---|---|---|
| No tie breaking | 9.45 | 84.54 | 13.00 |
| Rule 1: root weight | 4.27 | 85.65 | 11.77 |
| Rule 2: prior probability | 7.94 | 86.12 | 11.44 |
| Rule 3: dim7 resolution | 7.53 | 86.11 | 13.03 |
| Rules 1 and 3 | 2.22 | 86.97 | 10.83 |
| Rules 1 and 2 | 3.74 | 87.22 | 11.78 |
| Rules 2 and 3 | 6.03 | 87.80 | 11.28 |
| Rules 1, 2 and 3 | 1.68 | 88.66 | 10.72 |

Perfect scores rise from six excerpts (no tie breaking) to thirteen (all three rules); tie breaking
*lowered* the label score on excerpts 2, 16 and 20 (p. 32).

**★ The tie-breaking residual — the measurement DP-C carries (p. 34, restated p. 46).** *"Perfect tie
breaking can be expected to eliminate three of the error classes … for a total 26% of the errors. This
is the maximum improvement that can be expected from improved tie breaking."* Conclusion, p. 46: *"26%
of labeling errors can be eliminated with improved tie breaking between chord templates."* The three
classes are bad tiebreak, miscellaneous unresolved tie, and unresolved fully diminished tie (Figure 8,
p. 35, error counts by class: miscellaneous passing tone 23, passing tone called seventh 15,
harmonic context required 12, unresolved fully diminished tie 12, misc unresolved tie 8, disagree with
answer key 5, I–vii°6–I6 6, pedal tone 6, performance variation 5).

**Table 5, p. 43 — labelling scores by segmentation approach:**

| Proportion of KP corpus | Segmentation approach | Mean grade % | Std dev |
|---|---|---|---|
| All 45 excerpts | Use answer-key segmentation | 88.65 | 10.72 |
| All 45 excerpts | Relaxation search | 76.50 | 12.88 |
| All 45 excerpts | HarmAn search | 75.81 | 12.78 |
| Best 13 excerpts | Use answer-key segmentation | 100.00 | 0.00 |
| Best 13 excerpts | Relaxation search | 86.89 | 10.59 |
| Best 13 excerpts | HarmAn search | 86.08 | 11.13 |

**Corpus for the search-quality experiment (p. 41):** a separate corpus of **32 MIDI performances of
complete pieces** — Bach's 15 Three-Part Inventions, seven Bagatelles from Beethoven's Op. 33, and
Chopin's Nocturnes 10 through 19. Each piece was segmented 43 times (Relaxation once, HarmAn
start-to-finish once, HarmAn finish-to-start once, and HarmAn in 40 random orders).

**Figure 15, p. 42 — normalised segmentation content scores against Relaxation as 1.0:** HarmAn
forward median **98.7%**, HarmAn backward median **98.2%**, neither ever below 95%; random-order
median **90.5%**, lowest **72.2%** (Beethoven's Bagatelle No. 3).

**[FACT, p. 42] The order finding, and its own negative half.** *"Suppositions"* 1 and 2 were
supported — greedy search comes close to full search, and the order of partition-point selection
strongly influences the result. **Supposition 3 — that start-to-finish is the best order — was NOT
supported:** *"While forward search did achieve the highest median score, it was only marginally
better than backward search … Furthermore, backward search outscored forward search on many pieces."*

**Conclusion figures (p. 46):** given the correct segmentation, the labelling method *"labeled an
average of 89% of minimal segments correctly on the KP corpus"*; thirteen of 45 excerpts were labelled
perfectly; the combined system *"correctly labels roughly 77% of minimal segments in the full KP
corpus."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic stream with note onsets and offsets — MIDI, read as
delta-time events (p. 30). It assumes **nothing else**: no key signature, no metric position, no beat,
no voice membership, no spelling, no dynamics, no tonal context (p. 31, p. 46–47). Its partition points
are computed from onsets and offsets alone. For the 32-piece experiment the input is MIDI
**performances**, and the paper records the consequence as an error class of its own — *performance
variation*, where *"a timing variation in performance caused notes in the MIDI file to overlap in
different combinations than indicated in the score"* (p. 34).

**What it HANDS downstream.** A segmentation of the piece into segments, each carrying one best-matching
chord label (root pitch class and quality from the six-class vocabulary) and its numeric segment content
score; where a tie survives the three rules, **several labels for one segment**, which the grading metric
then splits. It hands on **no** tonality, no Roman numeral, no chord-tone assignment, no inversion, no
cadence and no figured bass. Labels are held to apply *"from the point where they appear until the next
label appears"* (p. 33).

**Its own STATED SCOPE and limits.**
- **Segment scoring is context-free by assumption** (p. 36, quoted above), and the authors state the
  cost of that assumption in their own conclusion (p. 47): *"While we broke the chordal analysis problem
  into two quasi-independent subtasks, it is clear that there are subtle (and not so subtle)
  interactions when segment scores are generated using the segment labeling system. Furthermore, segment
  scores generated by our current system do not fully capture the detail needed to match the answer key
  segmentation."*
- **The vocabulary is six chord classes.** Answers outside it (the paper's examples are *"German 6th"*
  and *"rest"*) are not graded rather than counted wrong (p. 31).
- **No inversion and no functional label** is produced; the KP answer key's Roman numerals were
  translated by the first author into the system's root-and-quality vocabulary (p. 31).
- **The remaining errors are attributed by the authors to what the decomposition does not admit:** the
  passing-tone class *"would probably coincide with disagreement among human analysts. This problem
  class might perhaps be resolved through a deep understanding of structural voice leading"*, and the
  *harmonic context required* class is *"An incomplete chord, which can only be uniquely identified
  through tonal function in context"* (pp. 34–35).

## ★ Findings, routed and not applied

**(1) The L1 charter's construction is CONFIRMED at its own primary, including the release half.** The
charter's change point is *"every onset and every release of an eligible note"*; the paper's partition
point is *"the onset or offset of one or more notes"*, stated twice, pp. 28–29 and p. 35. **The framework's
release-inclusive reading is the paper's own**, not an extension of it. *(The charter's separate ground for
releases — that slice identity is the sounding note set, so a unison or octave shrink is a real change —
is this project's own and is not in this paper.)*

**(2) DP-C's tie-breaking residual is VERIFIED at the object.** The framework carries *"with perfect
tie-breaking between equally-scoring labels, one published segment-then-label system would still remove
only 26% of its errors — the rest needs tonal context and voice leading its decomposition does not
admit."* Both halves check: the 26% at p. 34 and p. 46, and the gloss about tonal context and voice
leading is the authors' own attribution of the remaining classes at pp. 34–35. **No correction is owed.**

**(3) ★ AN ADDITION CANDIDATE TO DP-C's DEFENSE — an on-domain boundaries-given-versus-found gap, which
the framework's record does not currently carry.** DP-C's measured ground is presently an audio system
(68.8% given against 23.3% found) and segmental-model comparisons. **Table 5 of this paper is the same
shape on symbolic classical music and on our own kind of input:** the identical labelling method scores
**88.65%** given the analyst's segmentation and **76.50%** when a search that is *guaranteed optimal
under its own metric* must find one — and on the thirteen excerpts where the method is perfect given the
right segmentation, it falls to **86.89%**. The authors draw the inference themselves (p. 43): *"Because
the system achieves perfect labeling on these excerpts when the correct segmentation is provided, the
search methods must have generated segmentations different from those given by the answer key. Relaxation
search is guaranteed to find the best scoring segmentation given a particular scoring metric. Thus, the
only way for the search not to find the same segmentation as the answer key is for the segment scoring
mechanism to be sub-optimal for the task of finding the right segmentation."* **This is a stronger form
of DP-C's argument than the one on the record: not that a search is too weak, but that a perfect search
over a context-free segment content score still does not recover the analyst's segmentation.**
**ROUTED, NOT APPLIED** — an amendment to `FRAMEWORK.md` is the user's act on a surface, and this
commission amends nothing (§4 of the remedial commission).

**(4) A labelling discipline point, recorded because it would be easy to over-read.** The authors
suggest that *"System performance might be further improved by adding beat information to the note
weights"*, which would reduce the passing-tone and pedal-tone classes (p. 35). **That is CONJECTURE by
the authors, not a measurement**, and it may not be carried as support for L1 publishing metric strength.
L1's metric-strength ground stays where it is — Temperley 2009's Table 1, already read at the object and
corrected under Ruling 2.

**(5) The search-order finding, with what it is NOT about stated so it is not misread later.** Backward
search outscored forward search on many pieces (p. 42). **This is about the order in which a greedy
search visits partition points, not about the direction of information flow between layers.** It bears
on nothing in the framework's forward-only boundary contracts, and it is recorded here only so that a
later reader meeting the sentence does not take it for evidence about D-466.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL.** Its claims carry load in an L1 detail specification (the partition-point construction and
the note-weight alternative) and against a design point (DP-C's *before* rival, and finding 3 above,
which is an addition candidate to a chosen point's defense). **A second independent extraction is
therefore owed** under the original commission's §4 central-source rule, by one of that commission's two
routes. It has not been performed and is recorded here as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched, and finding (3) is routed to the user as an
addition candidate rather than written anywhere. It opens no code, touches no measurement tool, no
corpus, no golden and nothing under `tools/`. It writes no open-items row and allocates no
decisions-register identity. It takes no decision about the reading order of the remaining slice.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read (`CLAUDE.md` whole,
`DECISIONS.md` whole, `STATUS.md`, the derived gating answer). Read for this extract, at the files:
`cowork_reading_pass_remedial_commission_2026_08_31.md` whole, `cowork_reading_pass_commission_2026_08_30.md`
whole, `reading_pass/candidacy_upgrades.md` whole, `FRAMEWORK.md` §5 and §9 whole,
`cowork_reading_pass_findings_2026_08_31.md` §1, §2 and §3.2–§3.3. The paper itself was read at the object
as page images, pp. 27–49. No shell command was run on the repository or on any staged copy of it for
content or for listings; the container copy used for writing this file is declared. No figure of this
project's own measurement is restated (#17f, D-431); every value above is the paper's own, quoted with
its printed page.*

# EXTRACT — Temperley & Sleator 1999, "Modeling Meter and Harmony: A Preference-Rule Approach" — Task B candidacy row 7, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eighteen printed pages (pp. 10–27) were read AT THE OBJECT: the held PDF staged
> through the bridge and read with the file tools as page images. **No relay, no web-fetch read.**
> Every quotation carries its printed page.
>
> **Why this paper.** Row 7 of `reading_pass/candidacy_upgrades.md`, ADMITTED there because it
> *"decides meter and harmony together by preference rules — a rival shape for the L1/L2 division, and
> for how metric strength enters."* It is the second member of the L1 slice that **Ruling 10** made the
> phase's first needed reading.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

David Temperley & Daniel Sleator, "Modeling Meter and Harmony: A Preference-Rule Approach", *Computer
Music Journal* **23:1**, pp. 10–27, Spring 1999. © 1999 Massachusetts Institute of Technology.
Temperley — School of Music, Ohio State University; Sleator — School of Computer Science,
Carnegie-Mellon University.

**File:** `docs/research_papers/temperley_sleator_1999_cmj_meter_harmony_preference_rules.pdf`.

## Claims, labeled

### What the system is, and the shape of its division of labour

**[FACT, p. 10]** One program producing two structures at once: *"a representation showing a metrical
structure (consisting of several levels of beats) and a harmonic structure (consisting of a
partitioning of the piece into segments, each labeled with a root). (There are important reasons for
combining the metrical and harmonic systems into a single program, which we will explain.)"*

**[FACT, p. 10]** The method is a **preference-rule system**: *"Preference rules are criteria for
selecting an analysis of a piece out of many possible ones. The preferred analysis is the one which,
on balance, best satisfies the rules."* Contrasted by the authors with *procedural* systems, whose
output cannot be described as satisfying a stated criterion.

**★ [FACT, p. 11] THE INPUT CONTRACT, AND IT IS THE OPPOSITE OF OURS.** *"The input we assume is a
'note list,' giving the pitch (in integer notation, middle C = 60) and the on-time and off-time (in
milliseconds) of a series of notes. … The program requires no information beyond this: in particular,
it does not require other information commonly available in scores, such as bar lines, key signatures,
rhythmic notation, and the spellings of pitches."*

### The metrical half

**[FACT, p. 12]** Three metrical preference rules, the authors' own wording: the **event rule** —
*"prefer a structure that aligns beats with event onsets"*; the **length rule** — *"prefer a structure
that aligns strong beats with onsets of longer events"*; and (p. 14) the **regularity rule** —
*"prefer beats at each level to be maximally evenly spaced."*

**[FACT, p. 13]** "Length" is not notated duration: the authors define **registral inter-onset
interval** — the interval to the next event within nine semitones — and take an event's length as
*"the maximum of its duration and its registral IOI."*

**★ [FACT, p. 14] Quantization and meter-finding are ONE process, not two.** *"an important recent
realization of music artificial intelligence has been that quantization and meter finding are really
part of the same process."* The input is quantized to 35-msec **pips**, a value *"simply found to be
optimal through trial and error"*; beats may fall only at pip starts.

**[FACT, p. 15]** Five metrical levels prove sufficient; the tactus is level 2, with two levels above
and two below. The regularity requirement is a preference, not a well-formedness constraint, so the
system tracks tempo change: *"we cannot simply infer the metrical structure at the beginning of a
piece and extrapolate it metronomically through the rest of the piece."*

### The harmonic half

**[FACT, p. 15]** The output is **chord spans** labelled with roots **in absolute terms**: *"whereas a
Roman-numeral analysis represents each root relative to the current key, the current program simply
labels roots in absolute terms."* No key, no mode, no Roman numeral.

**[FACT, p. 16]** Four harmonic preference rules in the authors' wording: the **compatibility rule** —
*"prefer roots that result in certain pitch-root relationships"*, preferred in the order 1, 5, 3, ♭3,
♭7, ♭5, ♭9, ornamental; the **ornamental dissonance rule** — *"in labeling events as ornamental, prefer
events that are (1) closely followed by another event a half-step or whole-step away, and (2)
metrically weak"*; the **harmonic variance rule** — *"prefer roots such that roots of nearby chord spans
are close together on the line of fifths"*; and (p. 17) the **pitch-variance rule** — *"prefer spellings
for pitch events such that nearby events are close together on the line of fifths."*

**[FACT, p. 16]** Pitches are represented as **tonal pitch classes** on an infinite **line of fifths**,
not as the twelve neutral pitch classes: *"It is our view that these spelling distinctions are an
important aspect of tonal harmony, and must be represented."* Spelling is therefore **inferred by this
system**, and harmony feeds back into it: *"harmonic considerations may force a pitch spelling that
would be less preferred given the pitch-variance rule alone. In this way, harmonic considerations
'feed back' to influence pitch spelling"* (p. 17).

**★ [FACT, p. 17] THE STRONG-BEAT RULE, AND IT IS THE PAPER'S OWN REASON FOR ONE PROGRAM.**
*"**Strong-beat rule**—prefer to start chord spans on strong beats"*, immediately followed by: *"This
important rule explains the motivation for incorporating the harmonic and metrical programs into a
single program. Since harmonic analysis requires metrical information, it is useful to be able to use
the output of the metrical program as input to the harmonic program. There is a problem here, however,
as metrical analysis sometimes requires harmonic information."*

**★ [FACT, p. 17] Chord-span boundaries are restricted to a metrical grid.** *"we divide the piece into
segments based on the lowest level of the metrical structure (usually on the order of 100–300 msec),
and stipulate that chord-span boundaries can only occur at these segment boundaries."* The root space
is bounded arbitrarily: *"we arbitrarily limit it to a range of 48 roots on the line of fifths."*

### The search

**[FACT, pp. 18–19]** Dynamic programming over a table whose columns are segments and whose rows are
candidate roots; the best-so-far analysis ending in each root is carried forward. The authors name the
consequence and treat it as a virtue: *"In this way, the system naturally handles the 'garden-path'
effect: the phenomenon of revising one's initial interpretation of a segment based on what follows."*

**★ [FACT, p. 19] The exact table is intractable and is PRUNED.** *"To incorporate the harmonic variance
rule and the pitch-variance rule … we end up with a four-dimensional table … In practice, the computation
described above is intractable, because the four-dimensional table gets too large. We handle this by
pruning the table for a given segment immediately after the table for that segment is constructed. We
simply keep only those elements that are within some constant of the highest score in the table. We have
found a value for this constant that maintains a reasonable speed for the system without compromising
accuracy."* **The claim that accuracy is not compromised is stated, not measured** — see the next
section.

### ★ The circularity — the [FACT] the framework's L0 section cites, verified at the object

**[FACT, p. 25]** *"Making use of the harmonic analysis is another approach to improving the performance
of the metrical program on the higher levels. … The idea, then, is to let the harmonic analysis influence
the metrical analysis by favoring strong beats at changes of harmony. **This presents a serious
chicken-and-egg problem, however, since meter is crucial as input to harmony. One solution would be to
compute everything at once, optimizing over both the metrical and harmonic rules, but we have not yet
found an efficient way of doing this.** Another solution, which we are currently exploring, is to first
run the piece through the harmonic program, generating a provisional harmonic analysis, then run the
output of that through the meter program, which is now modified to prefer strong beats at points of
harmonic change, and finally run this output through the harmonic program again to generate the final
harmonic analysis."*

## Measured results, as the paper states them

**★ THERE ARE NONE. This is the single most consequential fact in the paper for our purposes, and it is
stated as an absence rather than inferred.** The paper reports **no corpus, no metric and no accuracy
value anywhere in its eighteen pages.** Its evidence is four worked examples shown as output listings and
discussed in prose: Bach's Cello Suite No. 3 Courante (Figures 6–7), Beethoven's Op. 13 II (Figures 8–9),
Schubert's *Moment Musical* No. 6 (Figure 10) and Schumann's Op. 15 No. 2 (Figure 11). The scope of
testing is given only as *"We have tested the program on a number of pieces and sections of pieces …
Most are pieces from the common-practice (Bach to Brahms) era, mainly piano pieces; there are also a
number of unaccompanied melodies"* (p. 19).

**The parameters are hand-set.** [FACT, p. 20] *"Both the metrical and harmonic programs involve a
number of parameters. The weight of each preference rule relative to the others must be specified. Many
rules also involve internal parameters … We have simply adjusted these parameters on a trial-and-error
basis. After many tests and adjustments, we have found a set of values that seems to produce generally
good results."*

**The authors' own catalogue of failures, from the worked examples** [FACT, pp. 22–25]: no knowledge of
**pedals**, so a chord over a pedal is misread (measures 7 and 15 of the Schubert); no knowledge of
**voice leading**, which *"results in a fair number of spelling mistakes"* and misreads a German sixth as
a dominant seventh; **no anticipations or escape tones**; upper metrical levels are weak — *"The
performance on the upper levels is weaker, especially on level 4. Frequently the program correctly
identifies level 4 as duple, which it usually is, but chooses the incorrect phase"*; and the output
*"indicates only the roots of chords, without further information such as mode (major or minor),
extension (triad or seventh), and inversion."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A note list of pitch, on-time and off-time in milliseconds, and
**nothing else** — explicitly not bar lines, key signature, rhythmic notation or spelling (p. 11). It
accepts unquantized live-performance input and handles tempo fluctuation by design (pp. 14, 22).

**What it HANDS downstream.** Three things: a metrical structure of five beat levels; a partition into
chord spans each labelled with an absolute root; and a tonal-pitch-class spelling for every pitch event.
It hands on **no key, no mode, no chord quality, no extension, no inversion, no Roman numeral, no
cadence and no phrase grouping.**

**Its own STATED SCOPE and limits.** Western tonal music, particularly common-practice art music (p. 10).
Grouping structure is named as the missing piece that would fix the upper metrical levels, and the authors
report their own attempt failed: *"getting a computer to determine grouping boundaries proves to be a very
difficult problem, and our preliminary efforts have been unsuccessful"* (p. 25). The meter-harmony
circularity is unresolved in the joint form (p. 25, quoted above). No evaluation is claimed.

## ★ Findings, routed and not applied

**(1) The framework's L0 meter [FACT] VERIFIES at the object, with its wording earned.** §5, L0 carries:
*"Systems that take a piano roll must infer metrical structure, and one such system reports an unsolved
circularity between meter and harmony as a result. [FACT.]"* This is that system and that report. The
authors call it *"a serious chicken-and-egg problem"*, state they *"have not yet found an efficient way"*
of optimising jointly, and offer a three-pass workaround they were *"currently exploring"*. **"Unsolved"
is fair at the page**: what is unsolved is the joint optimisation, and the workaround is offered as an
alternative to it rather than as a solution to it. **No correction is owed.**

**(2) ★ THE RIVAL SHAPE FOR THE L1/L2 DIVISION IS UNEVALUATED, AND THAT IS A FINDING ABOUT THE RIVAL.**
The candidacy derivation admitted this row as *"a rival shape for the L1/L2 division"*. Read whole, the
rival **reports no accuracy value of any kind** — no corpus, no metric, no comparison. Its parameters are
hand-tuned by trial and error until the output looked good. **A rival with no measured performance cannot
be preferred to a chosen design point on evidence, and cannot falsify one.** This is not a criticism of a
1999 paper; it is the fact that decides what weight the rival carries in a detail specification.
*(Independently corroborated inside our own read set: Pardo & Birmingham 2002, read at the object as row 4,
say of this same system that its authors "do not give any statistical analysis of the performance of their
system when compared to an outside measure" — two primaries agreeing, one of them the rival's own.)*

**(3) A second instance of the fitting pathology already recorded once.** The findings surface records row
19 as *"a concrete instance of what principles #20 and D-096 exist to prevent"* — parameters introduced
until known-correct outputs were reproduced, with no held-out discipline. **This paper is a second instance
of the same shape**, milder in form (trial-and-error weights rather than added parameters) and identical in
kind: no split, no held-out set, no reported metric. **Recorded as a finding, routed to measurement design;
nothing is written to any surface here.**

**(4) One passage that SUPPORTS a chosen L2 clause rather than rivalling it.** The L2 charter forbids
discarding a rival *"before the whole sequence of spans has been scored"*, on the ground that a wrong
reading can be a local optimum. This system's dynamic programming produces exactly that behaviour and its
authors name it — the garden-path effect, an initial reading of a span revised by what follows (p. 19).
**A rival system's own design corroborating a chosen point is worth recording; it is support, not a
falsifier, and nothing is amended.**

**(5) A relevance to R-8, recorded because the gap is already declared.** The authors close by naming
Krumhansl's key-profile model as the well-known proposal for key and stating its weakness: *"it has no
mechanism for handling modulation"* (p. 27). **R-8 records that the tonality-profiles primary is not held
and is unfetchable**; this is a second-hand characterisation and **nothing is carried out of it** beyond
the fact that this remark exists.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL.** Its claims carry load against a design point — it is the named rival shape for the L1/L2
division, and finding (2) bears directly on how much weight that rival can carry. **A second independent
extraction is therefore owed** under the original commission's §4 central-source rule. It has not been
performed and is recorded here as owed.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md` and
`cowork_reading_pass_findings_2026_08_31.md` are untouched, and findings (2) and (3) are routed rather
than written anywhere. It opens no code, touches no measurement tool, no corpus, no golden and nothing
under `tools/`. It writes no open-items row and allocates no decisions-register identity.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. Read for this
extract, at the files: both reading-pass commissions whole, `reading_pass/candidacy_upgrades.md` whole,
`FRAMEWORK.md` §5 and §9 whole, and the findings surface's §1, §2 and §3.2–§3.3; the row-4 extract of this
same slice. The paper itself was read at the object as page images, pp. 10–27. No shell command was run on
the repository or on any staged copy of it for content or for listings; the container copy used for writing
this file is declared. Every value above is the paper's own, quoted with its printed page (#17f, D-431).*

# EXTRACT — Bigo, Feisthauer, Giraud & Levé 2018, "Relevance of Musical Features for Cadence Detection" — Task B candidacy row 37, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** All seven printed pages (pp. 355–361) read AT THE OBJECT as page images through the
> bridge. **No relay, no web-fetch read.** Every quotation carries its printed page or section.
>
> **Why this paper.** Row 37 of `reading_pass/candidacy_upgrades.md`, ADMITTED because it is *"V6's
> primary, and the method behind DP-I's split: which cues are computable before the harmony is the L1
> charter's own content."* Third member of the L1 slice **Ruling 10** made the phase's first reading.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Louis Bigo, Laurent Feisthauer, Mathieu Giraud & Florence Levé, "Relevance of Musical Features for
Cadence Detection", *Proceedings of the 19th International Society for Music Information Retrieval
Conference (ISMIR 2018)*, Paris, pp. 355–361. CRIStAL UMR 9189, CNRS, Université de Lille; MIS,
Université de Picardie Jules Verne. CC BY 4.0.

**File:** `docs/research_papers/bigo_feisthauer_giraud_leve_2018_ismir_cadence_detection_features.pdf`.

## Claims, labeled

### ★ The two exclusions that make this L1's paper

**[FACT, §1.3]** *"The proposed strategy avoids chord segmentation, which is itself a difficult MIR
problem."* And **[FACT, §2]**: *"We therefore do not start from a complete harmony analysis nor a chord
segmentation, that can be error-prone. Even when the methods finding Y(Z) and X(Z) return approximate
onsets, the computed features may be relevant."*

**★ [FACT, §2.1]** *"we do not perform tonality estimation … because of the usual difficulty of
algorithms to disambiguate adjacent tonalities in the circle of fifths."* **The features reach for
tonality only as a hypothesis anchored on the bass of the arrival chord, never as a decided key.**

### What the method is

**[FACT, abstract, §2]** **44 binary, musical, local cadential features**, computed at **each beat** of
the score, turning cadence detection into a per-beat classification task. Features describe three
onsets: **Z**, the candidate arrival beat; **Y**, the chord preceding it; and **X**, the cadence
preparation.

**[FACT, §2.3]** Y is found heuristically: *"the latest beat preceding Z for which the bass voice
includes a sounding note, limited to one measure in the past."* Beat resolution for the search depends
on the corpus — quarter note for Haydn, eighth for Bach, *"to cope with the faster harmonic rhythm"*
(Figure 3).

**[FACT, §2.4]** X is *"the latest beat before Y whose lowest sounding note has a different pitch
(modulo octave) than the lowest note of Y."*

**★ [FACT, §2.1] The feature that IS the L1 charter's third cue.** *"Z-bass-compatible-with-I (resp.
Z-bass-compatible-with-V): Both notes 4 and 7 of the tonality that would be implied by the bass of Z are
present in the four beats before Z."* A companion feature, `Z-bass-compatible-with-I-scale`, asks whether
*"The 8 previous beats exhibits the whole scale of the same implied tonality."*

**[FACT, §2.1–2.4]** The other feature families, in the paper's own groupings: chord constitution at Z
(perfect triad, sus4, highest note is the tonic or the third); **voice-leading** features
`Z-β-comes-from-α` and `Z-α-moves-to-β` (an immediate resolution of one degree to another); **rhythmic
and break** features `R-Z-strong-beat`, `R-Z-same-rhythm`, `R-Z-sustained-note`, `R-after-Z-rest-*`;
features on Y (`Y-has-7`, `Y-in-V7`, `Y-Z-bass-moves-compatible-V-I`, `Y-Z-bass-same-voice`); and on X
(`X-Y-bass-moves-2nd-min`, `-2nd-Maj`, `-4th`).

**[FACT, §3]** A linear **SVM**, with **leave-one-piece-out** cross-validation for hyper-parameters —
chosen deliberately: *"the traditional Leave-One-Out (LOO) cross-validation approach that would consist
in leaving only one beat of one piece out of the training set would result here in overfitting due to
intra-piece musical repetitions."* Classes are unbalanced (about 98% non-cadential), so cadential beats
are weighted more heavily. *k*-nearest-neighbour and decision trees *"turned out to provide comparable
or inferior results."*

## Measured results, as the paper states them

**Corpora (Table 1).** `bach-wtc-i`: 24 fugues of the Well-Tempered Clavier book I, 2 to 5 voices, 4739
beats, PAC 63 (23 final), rIAC 24, HC (5). `haydn-quartets`: 42 expositions from Haydn string quartet
movements in sonata form, 4 voices, 7173 beats, PAC 99 (21), rIAC (8), HC 70. *"Cadences are labeled at
about 2% of the beats."* Bach annotations from the authors' own earlier fugue work; Haydn annotations
from Sears and colleagues.

**Table 3 — detection on the test sets, all features:**

| Corpus | Target | beats | ref | TP | FP | FN | F₁ |
|---|---|---|---|---|---|---|---|
| haydn-quartets (21 quatuors) | PAC | 3583 | 51 | 42 | 28 | 9 | **0.69** |
| haydn-quartets | HC | 3583 | 32 | 18 | 73 | 14 | **0.29** |
| bach-wtc-i (12 fugues) | PAC | 2357 | 36 | 26 | 3 | 10 | **0.80** |
| bach-wtc-i | PAC+rIAC | 2357 | 46 | 30 | 12 | 16 | **0.68** |

**Table 4 — F₁ by feature subset** (haydn PAC / haydn HC / bach PAC / bach PAC+rIAC): all features XYZR
0.69 / 0.29 / 0.80 / 0.68; YZR 0.69 / 0.27 / 0.71 / 0.68; ZR 0.59 / 0.24 / 0.52 / 0.34; XYZ 0.72 / 0.25
/ 0.74 / 0.54.

**[FACT, §4.4]** *"The detection of PAC is good, with more than 75% PAC detected and a low false
positive rate (< 1%)."* And, recorded because it is the authors' own caution about an earlier number:
*"Note that we previously reported 82% of PAC detection in fugues with manual hand-coded rules but that
may have resulted in overfitting."*

**★ [FACT, §4.2] The stated reason the half cadence is hard — and it is the framework's own sentence.**
*"We also notably lack strong significant features for HC. Indeed, the Y-Z bass move in a HC is variable
(it is typically similar to X-Y moves in PAC)."* **[FACT, §4.4]** *"The detection of HC is difficult
(Haydn corpus), as there is not a single feature applicable to every case. Half of them are detected,
with about 2% FP."*

**[FACT, §4.4]** Of 28 PAC false positives in Haydn, *"at least 5 FP can be seen as actual cadences"* —
the annotation itself is contestable at the margin.

**[FACT, §4.4]** Rhythmic features matter most where the harmony is weakest: *"Rhythmic features (R)
bring an improvement especially for HC, in particular with R-Z-strong-beat that correctly filters out
more than half of the beats."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score with **voices** (files were voice-separated
`.krn`; *"the features proposed here could also apply to non-separated files, except for after-Z-rest-*
and Y-Z-bass-same-voice"*), **metric position** (`R-Z-strong-beat` needs to know which beats are strong
for the time signature), **a bass voice**, and **durations**. It assumes **no key**, **no chord
segmentation** and **no harmonic analysis**. Features are extracted with music21; classification with
scikit-learn.

**What it HANDS downstream.** A per-beat binary verdict — this beat is or is not the arrival point of a
cadence of the trained type (PAC, rIAC or HC) — and, in the study itself, the per-feature significance
tallies of Table 2. It hands on **no chord, no key, no segmentation and no cadence type beyond the class
trained for.**

**Its own STATED SCOPE and limits.** Two corpora, Bach fugues and Haydn quartet expositions; the
annotations *"model cadences in the light of a global analysis of the form"* while the detection is
local, which the authors state as a known mismatch: *"we have used them as a benchmark on our local
feature-based detection."* Suspensions were expected to be significant for both PAC and HC and *"do not
appear significantly in these corpora."* The conclusion names the shape of the fix: *"Cadence
preparations could for example be described by features regarding contiguous 'spans' of onsets rather
than single onsets X and Y, in order to improve the harmony relevance of the model. Research along these
lines could significantly improve HC detection."*

## ★ Findings, routed and not applied

**(1) The L1 charter's cadence-cue paragraph verifies at this primary, in three separate places.** The
charter says the cues are *"computable from the notation without knowing the tonality"* — §2.1 says the
authors do not perform tonality estimation, and §1.3/§2 say they avoid chord segmentation and harmonic
analysis. The charter says *"hand-designed local features reach F .80 on perfect authentic cadences
with, in the authors' words, no chord segmentation and no tonality estimation"* — Table 3, bach-wtc-i
PAC, F₁ **0.80**. The charter says the half cadence is weak *"because the bass motion into a half cadence
is variable"* — §4.2 in the authors' own words. **No correction is owed on any of the three.**

**(2) The framework's third cue is this paper's feature, and the precision is worth carrying into the
detail specification.** The charter's *"the sounding together of the fourth and seventh degrees of a
candidate tonality in the approach"* is `Z-bass-compatible-with-I`: degrees 4 and 7 **of the tonality
implied by the bass of the arrival chord**, present **in the four beats before it**. The phrase
*candidate tonality* is therefore not loose — it names a hypothesis anchored on a note the score gives,
which is what keeps the cue inside L1's *decides nothing* rule. **Recorded for the derivation; nothing
is amended.**

**(3) A caution the charter does not carry, and a derivation should.** The Haydn cadence annotations
this study is graded against *"model cadences in the light of a global analysis of the form"* while the
detection is local, and the authors say at least five of the twenty-eight Haydn PAC false positives
*"can be seen as actual cadences"*. **The ceiling on a local cue is partly an artefact of a
form-level ground truth** — principle #21's shape, on the cadence axis. **Routed to measurement design.**

**(4) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL** — it is the primary under a chosen design point's recorded ground and under verification
target V6. **A second independent extraction is owed** under the original commission's §4 and has not
been performed.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. The paper was read
at the object as page images, pp. 355–361. No shell command was run on the repository or on any staged
copy of it for content or for listings; the container copy used for writing this file is declared. Every
value above is the paper's own (#17f, D-431).*

# EXTRACT — Karystinaios & Widmer 2022, "Cadence Detection in Symbolic Classical Music using Graph Neural Networks" — Task B candidacy row 38, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** All eight pages read AT THE OBJECT as page images through the bridge. **No relay, no
> web-fetch read.**
>
> **Why this paper.** Row 38 of `reading_pass/candidacy_upgrades.md`, ADMITTED as *"the second half of
> V6, and a different method for the same L1/L3 split."* Fourth member of the L1 slice **Ruling 10**
> made the phase's first reading. It is read immediately after row 37 because it is that paper's direct
> comparator and reports row 37's own numbers beside its own.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Emmanouil Karystinaios & Gerhard Widmer, "Cadence Detection in Symbolic Classical Music using Graph
Neural Networks", *Proceedings of the 23rd International Society for Music Information Retrieval
Conference (ISMIR 2022)*, Bengaluru. arXiv:2208.14819v1, 31 Aug 2022. Institute of Computational
Perception, Johannes Kepler University Linz; LIT AI Lab. CC BY 4.0.

**File:** `docs/research_papers/karystinaios_widmer_2022_arxiv_cadence_detection_gnn.pdf`.

## Claims, labeled

### What the method is

**[FACT, §1, §3]** Cadence detection is posed as **imbalanced node classification on a graph**. The
score becomes a *homogeneous* graph: every note **and every rest** is a node; three kinds of undirected
edge join them — `E_on` between notes sharing an onset, `E_cons` between consecutive notes, and `E_dur`
between a longer note and notes whose onsets fall during it.

**[FACT, §3.1]** **135 features per node**, in three categories: general note-wise features (onset in
score-relative beats, duration in beats, MIDI pitch, plus **global attributes such as time signature and
key signature assigned to each note**, and interval vectors with binary chord-type indicators);
graph-aware features (the first 20 eigenvectors of the Laplacian of the adjacency matrix); and
cadence-related note features *"similar to those in [4]"* — that is, row 37's.

**★ [FACT, §3.1] The deliberate weakening of row 37's frame, and its stated purpose.** *"in contrast to
[4], we restrict these to only consider the immediate local context of a note instead of using positional
features relating to predefined past 'cadence anchor points'. In this way, we wish to demonstrate the
generality of our representation and learning approach, which will hopefully learn more long-distance
aspects automatically."* And: *"we do not use any information about events that occur on previous beats
… While these features are more restricted compared to [4] they are also more general, since we make no
assumptions and reference to 'cadence anchor points' (e.g., the occurrence of the preceding subdominant
and dominant harmony), which in [4] are identified with specialized heuristics."*

**[FACT, §5]** The model is **Stochastic GraphSMOTE**: a GraphSAGE encoder, a SMOTE layer applied in the
encoder's *latent* space to force a 1:1 class balance per batch, a decoder generating edges for the
synthetic nodes, and a GraphSAGE classifier over the generated adjacency. The total loss is cross-entropy
plus a weighted edge-reconstruction loss.

**★ [FACT, §1, §6.1] Prediction granularity is a property of the representation, not of the task.** *"our
model can provide predictions at three different scales, note-wise, onset-wise and beat-wise (the latter
two simply by aggregation)"*, whereas *"The reference model [4] can only classify at the beat level."*

## Measured results, as the paper states them

**Corpora (Table 1).** Bach Fugues — 24 pieces, 24,567 nodes, 229,107 edges, PAC 237, rIAC 78, HC 15.
Haydn String Quartets — 45 pieces, 38,661 nodes, 441,491 edges, PAC 434, rIAC 24, HC 340. Mozart String
Quartets — 31 pieces, 68,190 nodes, 762,796 edges, PAC 1,089, HC 1,930. *"Cadence nodes constitute less
than 2% of all nodes."* Scores from kern.ccarh.org, parsed with partitura.

**Table 2 — half for training, half for testing; F₁ for the positive (cadence) class:**

| Dataset | Model | F₁ Note | F₁ Onset | F₁ Beat | Prec. Beat | Recall Beat |
|---|---|---|---|---|---|---|
| Bach Fugues (PAC) | Bigo et al. | – | – | **0.80** | 0.89 | 0.72 |
| | Stochastic GraphSMOTE | 0.85 | 0.75 | 0.73 | 0.70 | 0.77 |
| | Pretrained SGSMOTE | **0.90** | **0.83** | 0.80 | 0.74 | **0.89** |
| Bach Fugues (rIAC) | Bigo et al. | – | – | 0.68 | 0.71 | 0.65 |
| | Stochastic GraphSMOTE | **0.87** | **0.75** | **0.73** | **0.75** | 0.72 |
| | Pretrained SGSMOTE | 0.87 | 0.73 | 0.71 | 0.62 | **0.82** |
| Haydn String Quartets (PAC) | Bigo et al. | – | – | **0.69** | 0.60 | **0.82** |
| | Stochastic GraphSMOTE | 0.77 | 0.56 | 0.59 | 0.47 | 0.78 |
| | Pretrained SGSMOTE | **0.81** | **0.63** | 0.64 | 0.54 | 0.78 |
| Haydn String Quartets (HC) | Bigo et al. | – | – | **0.29** | 0.19 | **0.56** |
| | Stochastic GraphSMOTE | 0.65 | 0.32 | 0.30 | 0.33 | 0.27 |
| | Pretrained SGSMOTE | **0.69** | **0.44** | **0.41** | **0.41** | 0.41 |

**★ [FACT, §6.1] The authors' own summary of that table.** *"Our model matches or slightly surpasses the
state of the art in rIAC detection on Bach fugues and on HCs in Haydn string quartets but does not reach
the reference model's F1 results in PAC detection."* Pre-training on the other dataset *"is the price we
pay for the generality of the graph representation and the consequent size (number of parameters) of the
deep network."* And the comparison of error shapes: *"In the PAC detection tasks, in particular, we
observe comparable or higher recall of our model compared to the reference, but lower precision."*

**★ [FACT, §6.1] The independent replication.** *"Generally, our results agree with [4] in implying that
half cadences (HC) seem significantly harder to identify than authentic cadences, both perfect and
imperfect."*

**Table 3 — three-class classification (no cadence / PAC / rIAC or HC), 5-fold cross-validation, macro-averaged F₁**, comparing all features against *general* (excluding the cadence-specific engineered
category): Bach Fugues general 0.602 note / 0.667 beat against all 0.653 / 0.702; Haydn general 0.542 /
0.610 against all 0.648 / 0.663; Mozart general 0.584 / 0.569 against all 0.588 / 0.606. The authors'
reading: the engineered features help, *"However, also the general-purpose category 1 and 2 features
alone support non-trivial cadence recognition and discrimination performance, which implies that the
relational graph representation in combination with a convolutional approach manages to enrich highly
local features with relevant non-local score context."*

**Table 4 — neighbour-convolution depth on Bach PAC** (F₁ note / onset / beat): none 0.833 / 0.671 /
0.667; 1-hop 0.854 / 0.707 / 0.701; **2-hop 0.869 / 0.737 / 0.732**; 3-hop 0.836 / 0.706 / 0.659. *"Best
results are achieved when using a convolution depth of 2. Increasing the receptive field beyond that
level, we observed some instabilities emerging in the learning model."*

**[FACT, §6.2] The false positives are diagnosed, not just counted.** *"many false positive predictions
resemble cadences, in terms of tonal structure or implications, and could be considered and annotated as
such, but lack some main components."* The worked case is Haydn Op. 54 No. 1 II, mm. 33–45, where a
modulating melodic and harmonic sequence ends each statement with a cadential pattern: *"A harmonic
analysis of these bars indicates a proper PAC preparation with text-book voice leading on the cadence
arrival point in every occasion. These two false positive PACs form part of a modulating melodic and
harmonic sequence; whether to classify them as cadences is a matter of higher-level musicological
considerations."* And the stated boundary of the method: *"by design cannot consider higher-level
musical considerations such as, e.g., whether PAC-like patterns that occur in sequence should count as
PACs or not."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A parsed symbolic score giving, per note and per rest, onset in
score-relative beats, duration in beats and MIDI pitch, **plus the time signature and the key signature
as global attributes attached to every node**. Notes and rests both. No chord segmentation, no harmonic
analysis, no decided tonality — **but the key signature is used as a feature**, which the L0 contract
also gives, as a weak prior and never as a fact about the tonality.

**What it HANDS downstream.** A cadence label per **note**, and by aggregation per onset and per beat —
binary in the first experiment, three-class in the second. Nothing else: no chord, no key, no
segmentation.

**Its own STATED SCOPE and limits.** Baroque and Classical cadences, three corpora, focused on PAC with
rIAC and HC *"where our annotated datasets permit"*. The Bach HC count is 15 and the Haydn rIAC count 24,
and the paper says in a footnote that it ignores *"the HC in Bach and rIAC in Haydn, because of their low
numbers."* Pre-training on a second dataset is required for the best figures. Convolution beyond 2-hop
destabilises. The method cannot reach form-level judgements, by design.

## ★ Findings, routed and not applied

**(1) ★ THE FRAMEWORK'S ".29 AND .41" PAIR IS VERIFIED, AND BOTH VALUES SIT IN THIS ONE TABLE.** The L1
charter carries: *"the half cadence reaches F .29 and .41 in those same two studies."* Table 2 of this
paper reports **0.29** for the Bigo et al. reference model on Haydn HC — the same value row 37's own
Table 3 reports — and **0.41** for this paper's own pretrained model on the same target. **Both halves of
the charter's figure verify at the object, and the two studies are now both read whole. No correction is
owed.**

**(2) The independent replication the charter's DP-I rests on is real and is stated as such.** *"our
results agree with [4] in implying that half cadences seem significantly harder to identify than
authentic cadences"* — an independent method, a different corpus, the same conclusion. **DP-I's split —
cues at L1, type at L3 — is supported by two primaries rather than one, and both are now at the object.**

**(3) ★ A finding that sharpens what the charter means by a cue, and that the derivation should carry.**
This paper deliberately **removed** row 37's anchor-point heuristics and still reached comparable results
by letting a graph supply the surrounding context. Read together, the two papers say the cue is carried
by **local musical evidence plus some view of its surroundings**, and that the surroundings can be
supplied either by hand-named anchors or learned. **For L1 that is a boundary statement, not a licence:**
the charter has L1 publish evidence at change points and decide nothing, so the surrounding-context half
belongs to the layer that sees the span. **Routed to the L1 and L2 detail specifications; nothing is
amended.**

**(4) A ceiling caution, agreeing with row 37's from the other side.** Row 37 records that at least five
of its Haydn PAC false positives *"can be seen as actual cadences"*. This paper's §6.2 says the same in
its own words and works an example: cadential patterns inside a modulating sequence, textbook-correct at
the arrival, counted as false positives because whether they are cadences *"is a matter of higher-level
musicological considerations."* **Two independent studies report that the annotation, not only the
method, bounds the measured figure.** Principle #21's shape on the cadence axis. **Routed to measurement
design.**

**(5) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL** — the second primary under V6 and under DP-I's recorded ground. **A second independent
extraction is owed** and has not been performed.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. The paper was read
at the object as page images, all eight pages. No shell command was run on the repository or on any
staged copy of it for content or for listings; the container copy used for writing this file is declared.
Every value above is the paper's own (#17f, D-431).*

# EXTRACT — Sears, Pearce, Caplin & McAdams 2018, "Simulating melodic and harmonic expectations for tonal cadences using probabilistic models" — Task B candidacy row 39, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** All twenty-four pages read AT THE OBJECT as page images through the bridge. **No
> relay, no web-fetch read.**
>
> **Why this paper, and what the read was for.** Row 39 of `reading_pass/candidacy_upgrades.md`,
> admitted **ON THE DOUBT DEFAULT**: *"A computational model of cadential arrival; whether its method
> bears on L1's cues or only on perception is not settled by the row."* **The doubt default's whole
> point is that such a question is answered by reading, not by the derivation. This read answers it.**
> Fifth and last member of the L1 slice **Ruling 10** made the phase's first reading.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

David R. W. Sears, Marcus T. Pearce, William E. Caplin & Stephen McAdams, "Simulating melodic and
harmonic expectations for tonal cadences using probabilistic models", *Journal of New Music Research*
**47:1** (2018), pp. 29–52. Published online 22 November 2017, DOI 10.1080/09298215.2017.1367010.
McGill University; Queen Mary University of London.

**File:** `docs/research_papers/sears_pearce_caplin_mcadams_2018_jnmr_cadence_expectations.pdf`.

## ★ The doubt-default question, answered

**Its method does NOT bear on L1's cues. It bears on perception, and — secondarily — on how a cadence
ground truth and a cadence measurement are read.** Three findings at the object settle it, and any one
of them would:

1. **It does not detect cadences. It consumes them.** The cadence collection is **annotated by hand**
   under Caplin's typology and supplied to the analysis; the study then measures how *predictable* the
   annotated terminal events are. There is no detection task, no classifier, no precision and no recall
   anywhere in the paper.
2. **★ Its harmonic viewpoints require a hand-annotated tonality.** [FACT, §5.2] *"to relate `cpitch`
   to a referential tonic pitch class for every event in the corpus, we manually annotated the key,
   mode, modulations and pivot boundaries for each movement."* **The scale-degree viewpoints `csd` and
   `csdc` — the ones carrying every harmonic result in the paper — are computed from a key that a human
   supplied.** A method that consumes a decided tonality cannot produce an L1 cue, L1 being the layer
   that decides nothing and runs before any tonality exists.
3. **The authors name their own object of study, in the paper's last sentence.** [FACT, §7] *"the
   schematic expectations formed by listeners for cadences and other recurrent temporal patterns amount
   to these sorts of probabilistic inferences requires an entirely different approach, one in which the
   listener, rather than the music, represents the primary object of study."*

**So the doubt resolves against L1 candidacy — and the reading was still worth its cost**, because three
of its findings bear on things the record does care about. Those are §"Findings" below.

## Claims, labeled

### What the method is

**[FACT, abstract, §1]** The model is **IDyOM** — a finite-context (*n*-gram) model that predicts the
next event in a musical stimulus by unsupervised statistical learning of sequential structure — applied
to the terminal melodic and harmonic events of **245 exemplars** of the five most common cadence
categories in the classical style.

**[FACT, §3, §5.2]** Events are represented in Conklin's **multiple viewpoints** framework. The melodic
viewpoints are chromatic pitch (`cpitch`), melodic interval (`melint`), chromatic scale degree (`csd`)
and an optimised combination (`selection`); the harmonic ones are vertical interval class combination
(`vintcc`) and chromatic scale-degree combination (`csdc`), the latter *"intended to approximate Roman
numerals"*; and `composite` is the joint probability of the melodic and harmonic models.

**[FACT, §4]** Probabilities come from maximum-likelihood *n*-gram counts smoothed by **Prediction by
Partial Match**, in the variable-order **PPM\*** variant with interpolated smoothing and Moffat's escape
method C. The reported quantity is **information content**, IC = log₂(1/p), in bits.

**[FACT, §5.3]** Only the **long-term model** (LTM+) is used: *"the STM should be irrelevant for the
present purposes, since cadences exemplify the kinds of inter-opus patterns that listeners are likely to
store in long-term memory."*

**[FACT, §5.4]** Evaluation is **10-fold cross-validation**, the corpus serving as both training and
test set.

### Its own preprocessing, recorded because it bounds what the figures mean

**[FACT, §5.1]** *"To ensure that each instrumental part would qualify as monophonic … all trills,
extended string techniques, and other ornaments were removed."* Double and triple stops were reduced to
the note events preserving the voice leading. Chord events are formed by **full expansion**, duplicating
overlapping note events at every unique onset time.

**[FACT, §5.2]** Rhythmic and metric viewpoints were **deliberately excluded**: *"the terminal events at
the moment of cadential arrival appear in strong metric positions, and few of the cadences feature
unexpected durations or inter-onset intervals at the cadential arrival, so we have excluded viewpoint
models for rhythmic or metric attributes from the present investigation."*

## Measured results, as the paper states them

**Corpus (§5.1, Tables 2–3).** 50 sonata-form expositions from Haydn's string quartets (1771–1803),
Opp. 17–76, from KernScores. 270 cadences annotated, 25 excluded (15 where the cadential bass or soprano
is absent from cello or first violin; 10 implying more than one category), leaving **245 cadences**:
PAC 122, IAC 9, deceptive 19, evaded 11, half cadence 84. Note events: violin 1 14,506; violin 2 10,653;
viola 9156; cello 8463; expanded chord events 20,290.

**Experiment 1 — are cadential terminal events more predictable than non-cadential ones?** For the first
violin, mean IC increased significantly from PAC to non-cadential contexts for `melint`, `csd` and
`selection`, but not for the baseline `cpitch` (Table 4). **For the cello the direction reversed**: mean
IC *decreased* in every model from PAC to the non-cadential levels — *"contrary to our predictions, the
terminal events in the cello from cadential contexts were actually less predictable than those from
non-cadential contexts."* For the chord viewpoints `vintcc`, `csdc` and `composite`, cadential terminal
events were more predictable than non-cadential ones, `composite` showing *"an ascending staircase"*
from PAC through tonic to non-tonic.

**★ [FACT, §6.1.3] The authors' own explanation of the cello reversal, and it is a fact about the
evidence rather than about the model.** *"since the leap in the bass by descending fifth (or ascending
fourth) in perfect authentic cadential contexts occurs less frequently than motion by smaller intervals
in any other context …, it may also be that cadential bass lines are simply less predictable than their
stepwise, non-cadential counterparts when considered in isolation. For the viewpoints that explicitly
model the interaction between the bass and the upper voices, however (e.g. `vintcc`, `csdc`, or
`composite`), IDyOM produced considerably lower IC estimates for cadential successions like 5̂–1̂ than
for non-cadential successions like 1̂–1̂, 2̂–1̂, or 7̂–1̂."*

**★ [FACT, §6.1.3] The half cadence, measured by a third method.** *"half-cadential contexts generally
failed to elicit lower mean IC estimates compared to non-cadential root-position dominants. Thus,
according to IDyOM, the terminal events from the HC level are no more (or less) predictable than any
other instance of root-position dominant harmony selected at random from the corpus."*

**Experiment 2 — do the IC estimates order the cadence categories as a typology predicts?** The
*Prospective Schemas* ordering PAC→IAC→HC→DC→EV fits better than the *1-Schema* ordering
PAC→IAC→DC→EV→HC; for `composite` the Prospective model *"accounted for roughly 55% of the variance …
which represents the largest effect demonstrated across all of the polynomial contrasts from every
viewpoint model"* (Table 6). Genuine cadence categories received lower mean IC than the cadential
deviations in every model.

**★ Experiment 3 — where the boundary evidence actually sits.** [FACT, §6.3] The two hypotheses tested
are *"(1) that the terminal event of a group is the most expected (i.e. predictable) event in the
surrounding sequence; and (2) that the next event in the sequence is comparatively unexpected (i.e.
unpredictable)"*, on the ground that *"unexpected events engender prediction errors that lead the
perceptual system to segment the event stream into discrete chunks."* Results (Table 7, Figure 6): for
the first violin, *"the mean IC estimates … increased significantly following the predicted boundary for
every cadence category in the collection"*, and for PAC, IAC, HC and DC the increase from the terminal
event to the following one was significant. For the **evaded** category the significant increase occurs
*at* rather than after the expected terminal event, which the authors give as the predicted behaviour
for a cadential deviation. The framing sentence: *"the strength of the potential boundary between two
sequential events results in part from the increase in information content (or decrease in probability)
from the first to the second event."*

**The authors' own stated limitations** [FACT, §7]: *"the rather meager sample size for three of the
five cadence categories … casts some doubt upon the generalisability of the reported findings"*; the
melodic models assume listeners expect *specific* intervals rather than small ones generally, which is
*"theoretical, rather than empirical"*; only contiguous *n*-grams were used, which *"is particularly
acute for corpus studies of tonal harmony, where the musical surface contains considerable repetition,
and many of the vertical sonorities from the notated score do not represent triads or seventh chords,
thereby obscuring the most recurrent patterns"*; and *"IDyOM benefited from human annotations of tonal
information in `csd`."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score reduced so that each instrumental part is
monophonic (ornaments and multiple stops removed); **a hand-annotated key, mode, modulation and pivot
boundary track**; and **a hand-annotated cadence collection** typed under Caplin. It assumes no
segmentation of its own and performs none.

**What it HANDS downstream.** Per-event information content in bits, per viewpoint — a scalar of
*predictedness*, not a label, not a boundary and not a decision. Nothing in its output is a fact about
the music that another layer could consume as evidence without first deciding what an IC value means.

**Its own STATED SCOPE and limits.** One composer, one genre, one form section: Haydn string-quartet
sonata-form expositions. Rhythm and meter excluded by design. The object of study is the listener.

## ★ Findings, routed and not applied

**(1) ★ A THIRD INDEPENDENT STATEMENT THAT THE HALF CADENCE IS NOT SEPARABLE BY LOCAL EVIDENCE — AND IT
COMES FROM A DIFFERENT KIND OF METHOD ENTIRELY.** Rows 37 and 38 say it in F-measure (0.29 and 0.41
against 0.80 for the perfect authentic cadence). This study says it in information content: the terminal
events of a half cadence are *"no more (or less) predictable than any other instance of root-position
dominant harmony selected at random from the corpus."* **Detection and predictability are different
measurements, and they agree.** This strengthens DP-I's recorded ground — cues at L1, type at L3 —
beyond what the charter currently cites. **Routed as an addition candidate to DP-I's defense; not
applied, an amendment being the user's act on a surface.**

**(2) ★ A PRECISION ABOUT THE "TWO INDEPENDENT STUDIES", worth carrying because a later reader will lean
on it.** The L1 charter cites rows 37 and 38 as two independent studies. **They are independent in
METHOD and not in DATA:** row 38 states it uses *"two datasets also used by Bigo et al."*, and row 37's
Haydn cadence annotations are *"from Sears and colleagues"* — that is, from **this paper's own author
group and annotation programme**. So the replication is a second method over largely the same annotated
material. **The charter's sentence is not wrong** — they are two studies and they are independent — **but
the independence does not extend to the ground truth, and a derivation that leans on the replication
should say which kind of independence it is relying on.** *(Finding (1) is not subject to this caveat in
the same way: it is a third method AND a different measurement, though on the same composer.)*
**Recorded; nothing amended.**

**(3) ★ A FINDING ABOUT BASS EVIDENCE THAT BEARS ON HOW ANY CUE IS FORMED.** In isolation, the cadential
bass leap is *less* predictable than the stepwise motion of non-cadential contexts — so a single-voice
statistical model **penalises exactly the motion that signals the cadence**, and the sign of the effect
reverses. Only viewpoints that model the interaction between bass and upper voices recover the expected
direction. **The practical statement for a detail specification: a cue defined over the bass alone can
have the wrong sign; the cue is the bass motion IN RELATION to what sounds above it.** *(Read beside row
37, which reaches the same place from the other side: its bass-move features are always relative to the
chord at the arrival, never to the bass line alone.)* **Routed to the L1 and L2 detail specifications.**

**(4) A boundary-evidence claim, routed to the phrase-boundary primitive and to L3, not to L1.**
Experiment 3's result is that a boundary's strength lies partly in the **rise** in information content
*after* the terminal event, not in the terminal event alone. **This is a claim about where boundary
evidence sits in time**, and its owner in our frame is the phrase-boundary primitive and L3's grouping,
not L1's cues. **Recorded, routed, not applied.**

**(5) A fourth instance of the ground-truth-bounds-the-figure pattern.** The authors exclude 25 of 270
annotated cadences because the annotation cannot be made to fit the analysis — 15 for a missing bass or
soprano, 10 for implying more than one category — and name the small sample for three of five categories
as a limit on generalisability. **Routed to measurement design**, beside rows 37 and 38's own versions of
the same point.

**(6) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**NOT CENTRAL for L1** — no claim of this paper carries load in an L1 detail specification, which is the
doubt-default question answered above. **Its findings (1), (3) and (4) do carry load elsewhere** — DP-I's
defense, the L2 detail specification, and the phrase-boundary primitive — so **whether a second
extraction is owed is a question for the sessions that take up those subjects, and is deliberately not
decided here.** Recorded rather than assumed either way.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity. It does not
re-open DP-I; finding (1) is an addition candidate put to the user, not an amendment.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. The paper was read
at the object as page images, all twenty-four pages. Read beside it for findings (1) and (2): this
session's own row-37 and row-38 extracts. No shell command was run on the repository or on any staged
copy of it for content or for listings; the container copy used for writing this file is declared. Every
value above is the paper's own (#17f, D-431).*
