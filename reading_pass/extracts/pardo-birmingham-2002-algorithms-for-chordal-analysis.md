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
>
> **★ CORRECTED 2026-09-20 AT SIX SITES, by the sitting that wrote this paper's second extraction**
> (`reading_pass/extracts_second_pass/pardo-birmingham-2002-algorithms-for-chordal-analysis.md`, §9.3
> (a) to (f)), under the standing rule the user ruled on 2026-09-19 (handoff entry 198 §7): where the
> cross-check finds this extract departing from the page and no value, finding or verdict moves, the
> site is corrected with the former wording preserved (#12). Each site below carries a "★ CORRECTED
> 2026-09-20" note. **No value, table cell, finding or verdict was changed, and nothing of the
> record-facing half was touched.** Four further places that do touch a value, a finding or the
> verdict's ground were **NOT** corrected and stand with the user; they are listed at the second
> extract's §9.4.
>
> **★ UNDER THE USER'S RULING OF 2026-09-20 — his words: "I agree with C" — the last two sentences
> above are made stale and left standing (#12).** C was: correct items 1, 3 and 4 of the second
> extract's §9.4 at their sites, former wording preserved; leave finding (2) as written and put a
> pointer remark beneath it, so that finding (2) and the `FRAMEWORK.md` sentence it speaks about are
> changed together later, on their own surface, after the framework's passages have been read whole.
> **Done here:** Figure 8's values (in the tie-breaking-residual paragraph), the *Adapt* bullet's "on
> measured grounds", and finding (3)'s "on our own kind of input", each with an "UNDER THE USER'S
> RULING" note; and the pointer remark beneath finding (2). **Finding (2) itself, its conclusion, the
> 26%, Table 4, Table 5, the three values of finding (3) and the Centrality verdict were not changed.**
>
> **★ UNDER THE USER'S LATER RULING OF 2026-09-20 — his words: "I agree: A" — the sentence above that
> finding (2) and its conclusion were not changed is made stale and left standing (#12).** A was: narrow
> the `FRAMEWORK.md` sentence at DP-C in place to what the authors report, former wording preserved, and
> correct finding (2) to say that the 26% verifies and the gloss was wider than the authors' account.
> **Done here:** finding (2) rewritten with its former wording preserved beneath it, and a note beneath
> the scope bullet that feeds it. **Not done here:** the `FRAMEWORK.md` edit, which goes in a dispatch
> run with Claude Code and is owed. The 26%, every table and the Centrality verdict were not changed.

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
approaches to note weight involving these parameters but found that the approach based on minimal
segments worked surprisingly well."*
*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): "approaches to note weighting involving
these parameters" — p. 30 prints "note weight".)*

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

**[FACT, pp. 36–37]** The problem is posed as a highest-reward path through a directed acyclic graph: one
vertex per partition point, one edge per possible segment, the edge's reward the segment's content
score. *"Any path from the first vertex to the last one represents a segmentation of the piece."*
*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): "[FACT, p. 36]" — the section begins on
p. 36; the graph's description and the quoted sentence are on p. 37.)*

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
Temperley from Kostka & Payne, *Tonal Harmony* (1984), with an answer key *"based on the analyses in
the teacher's edition of the textbook"* (p. 27).
*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): "compiled by David Temperley from the
teacher's edition of Kostka & Payne, Tonal Harmony (1984)." — p. 27 says the excerpts were compiled
from the textbook and that the answer key is based on the teacher's edition.)*
The full excerpt list is
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
p. 35, error frequencies by class as a percentage of the total, p. 34: miscellaneous passing tone 23,
passing tone called seventh 15, harmonic context required 12, unresolved fully diminished tie 12, misc
unresolved tie 9, disagree with answer key 6, I–vii°6–I6 6, pedal tone 6, bad tiebreak 5, performance
variation 5).
*(★ CORRECTED 2026-09-20 UNDER THE USER'S RULING. FORMER WORDING, PRESERVED (#12): "error counts by
class: miscellaneous passing tone 23, passing tone called seventh 15, harmonic context required 12,
unresolved fully diminished tie 12, misc unresolved tie 8, disagree with answer key 5, I–vii°6–I6 6,
pedal tone 6, performance variation 5" — the second reader, with PDF page 9 requested again, read ten
bars, left to right 23, 5, 6, 12, 6, 5, 9, 6, 15, 12, and p. 34 calls them "Error frequencies as a
percentage of the total". The numerals are small at the size delivered; the paper's own sum supports 9:
bad tiebreak 5 + misc unresolved tie 9 + unresolved fully diminished tie 12 = 26. The 26% is
unchanged.)*

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
delta-time events (p. 30). By its own statements it does not use tonal context, beat, absolute pitch
height or dynamics (p. 31), nor metric information, key signature, harmonic function, voice leading or
stylistic information (pp. 46–47).
*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): "It assumes **nothing else**: no key
signature, no metric position, no beat, no voice membership, no spelling, no dynamics, no tonal context
(p. 31, p. 46–47)." — neither page prints voice membership or spelling, and "nothing else" passes over
what p. 28 and Figure 4 state: the template vocabulary and the prior-probability rule are taken from
the answer key of the corpus under test.)*
Its partition points
are computed from onsets and offsets alone. For the 32-piece experiment the input is MIDI
**performances** (p. 41). Among the error classes of the **KP-corpus** labelling experiment the paper
records *performance
variation*, where *"a timing variation in performance caused notes in the MIDI file to overlap in
different combinations than indicated in the score"* (p. 34).
*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): "For the 32-piece experiment the input is
MIDI **performances**, and the paper records the consequence as an error class of its own —" — the ten
error classes come from the hand examination of the 45-excerpt KP corpus (p. 33; Figure 8's caption);
an error analysis of the 32-piece experiment was met nowhere in the pages as the second reader read
them. So the class shows performed timing in at least some
KP-corpus files.)*

**What it HANDS downstream.** A segmentation of the piece into segments, each carrying one best-matching
chord label (root pitch class and quality from the six-class vocabulary) and its numeric segment content
score; where a tie survives the three rules, **several labels for one segment**, which the grading metric
then splits. It hands on **no** tonality, no Roman numeral, no chord-tone assignment, no inversion, no
cadence and no figured bass. Labels are held to apply *"from the point where they appear until the next
label appears"* (p. 44).
*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): "(p. 33)" — the quoted words are p. 44's;
p. 33 prints "Labels remain in effect from the point where they appear until the next label is
encountered.")*

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
  *(★ NOTE 2026-09-20 UNDER THE USER'S RULING "I agree: A". The bullet's heading is wider than the two
  classes it names: those two are two of the seven error classes outside the three tie classes. What
  the authors say of the other five is at finding (2) below. The bullet's wording and its two
  quotations are left as written.)*

## What an L1 or L2 detail specification could adopt, adapt, or must argue against

- **Adopt:** the partition-point construction itself, which is the L1 charter's own — and the bound it
  carries, that partition points are at most twice the number of notes, which is what makes the change-point
  set finite and enumerable.
- **Adapt:** the note weight defined as the count of minimal segments a note spans rather than its
  notated duration. This is a live alternative to duration weighting for any evidence term over a span,
  and the authors report that they tried approaches involving duration, velocity and the highest or
  lowest note and *"found that the approach based on minimal segments worked surprisingly well"*
  (p. 30); a measurement of the alternatives was not met in the pages as the second reader read them.
  *(★ This sentence's close was itself brought inside its bound at the user-ordered check of the same
  day; it had read "they print no measurement of the alternatives".)*
  *(★ CORRECTED 2026-09-20 UNDER THE USER'S RULING. FORMER WORDING, PRESERVED (#12): "and the authors
  report choosing it over duration and velocity on measured grounds." — a measurement of any
  alternative was met nowhere in the pages as the second reader read them; p. 30 adds that the choice
  fits the authors' preference for the simplest approach. The Centrality verdict below, which names
  the note-weight alternative, is not changed by this note.)*
- **Must argue against:** the context-free segment content score. The framework's L2 decides
  segmentation *with* tonality, chord and chord-tone assignment; this paper's decomposition is the
  boundary case where the segment content score reads nothing but pitch classes, and its authors' own
  conclusion is that the assumption does not hold well enough to recover the analyst's segmentation.
- **Must argue against, second:** the two-subtask split itself — label a segment, then search over
  segmentations using those labels' scores. That is DP-C's *before* rival in its cleanest published form,
  built by authors who state its limits themselves.

## ★ Findings, routed and not applied

**(1) The L1 charter's construction is CONFIRMED at its own primary, including the release half.** The
charter's change point is *"every onset and every release of an eligible note"*; the paper's partition
point is *"the onset or offset of one or more notes"*, stated twice, pp. 28–29 and p. 35. **The framework's
release-inclusive reading is the paper's own**, not an extension of it. *(The charter's separate ground for
releases — that slice identity is the sounding note set, so a unison or octave shrink is a real change —
is this project's own and is not in this paper.)*

**(2) DP-C's tie-breaking residual: the 26% is VERIFIED at the object, and the second half of the
framework's sentence is WIDER than the authors' account.** The framework carries *"with perfect
tie-breaking between equally-scoring labels, one published segment-then-label system would still remove
only 26% of its errors — the rest needs tonal context and voice leading its decomposition does not
admit."* The 26% checks at p. 34 and p. 46 (p. 46 is the first reader's locator, carried over; the
correcting sitting saw p. 34). The second half does not check as written. Seven error
classes stand outside the three tie classes (Figure 8's values, percentages of the total, small
numerals). The authors define one, *harmonic context required* (12), by *"tonal function in context"*
(p. 34). Of one, *passing tone called seventh* (15), they say it *"might perhaps be resolved through a
deep understanding of structural voice leading"* and that such passages *"would probably coincide with
disagreement among human analysts"* (p. 35). For two, *miscellaneous passing tone* (23) and *pedal
tone* (6), they suggest adding beat information to the note weights, which *"could reduce"* them,
*"although heavily syncopated music would still present a problem"* (p. 35). For one, *I–vii°6–I6* (6),
they suggest a two-pass system (pp. 34–35). One, *disagree with answer key* (6), is their belief that
the key is wrong (p. 33), and one, *performance variation* (5), is timing in the MIDI file (p. 34).
They also say, tied to no class, that *"Knowledge of adjacent chord labels might be used to adjust
chord-label weights"* (p. 35). The error study was run with the segmentation taken from the answer key
(pp. 31–32). **ROUTED: under the user's ruling of 2026-09-20 — his words: "I agree: A" — the
`FRAMEWORK.md` sentence at DP-C is to be narrowed in place to this account, former wording preserved,
by a dispatch run with Claude Code. That dispatch is owed and was not written by the sitting that made
this correction. This extract amends nothing.**

*(★ CORRECTED 2026-09-20 UNDER THE USER'S RULING "I agree: A". FORMER WORDING OF FINDING (2),
PRESERVED (#12): "**(2) DP-C's tie-breaking residual is VERIFIED at the object.** The framework carries
[the sentence quoted above]. Both halves check: the 26% at p. 34 and p. 46, and the gloss about tonal
context and voice leading is the authors' own attribution of the remaining classes at pp. 34–35. **No
correction is owed.**" The sitting that made this correction read printed pp. 31–35 again at the page
images; the account above is set against those pages and against the second extract's §9.4 item 2. The
pointer remark beneath this note was true when written and is made stale by this correction; it is
left standing.)*

*(★ POINTER REMARK, 2026-09-20, UNDER THE USER'S RULING — FINDING (2) ABOVE IS LEFT AS WRITTEN AND IS
CONTESTED. The second extraction's cross-check reads pp. 34–35 differently: the authors attribute two
of the seven classes outside the tie classes to tonal function in context or to voice leading, suggest
beat information for two more and a two-pass relabeling for one, and put two down to the answer key or
the performance. The account, with its derived sums, is at the second extract's §9.4 item 2. By the
ruling, this finding and the `FRAMEWORK.md` sentence it speaks about are to be changed together, on
their own surface, after the framework's passages have been read whole. Until then a reader should not
take "No correction is owed" as settled.)*

**(3) ★ AN ADDITION CANDIDATE TO DP-C's DEFENSE — an on-domain boundaries-given-versus-found gap, which
the framework's record does not currently carry.** DP-C's measured ground is presently an audio system
(68.8% given against 23.3% found) and segmental-model comparisons. **Table 5 of this paper is the same
shape on symbolic classical music (MIDI; see the note beneath this finding):** the identical labelling method scores
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

*(★ CORRECTED 2026-09-20 UNDER THE USER'S RULING. FORMER WORDING, PRESERVED (#12): "Table 5 of this
paper is the same shape on symbolic classical music and on our own kind of input:" — the paper's error
class "performance variation" (p. 34) shows that at least some of the 45-excerpt corpus's MIDI files
carry performed timing, and how those files were made was met nowhere in the pages as the second reader
read them. So the corpus is symbolic, and it is not shown to be notated-score input of the kind this
project reads. The three values 88.65, 76.50 and 86.89 agree with the page and are unchanged, and the
authors' inference is quoted as they print it.)*

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
