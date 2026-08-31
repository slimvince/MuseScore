# Second-pass extract — row 21: Humphrey & Bello 2015, "Four Timely Insights on Automatic Chord Estimation"

> **STATUS: SECOND EXTRACTION (session 2 of the reading pass, 2026-08-31), INDEPENDENT EXCEPT ON
> ONE DECLARED POINT.** Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the
> independence protocol of `reading_pass/continuation.md` §2.
>
> **★ THE DECLARED CONTAMINATION, RESTATED AT THIS FILE'S OWN FACE.** The continuation file
> requires this session to read `reading_pass/population.md` §3 before extracting, and that
> section's verification target **V12 states a substantive finding about this very paper** — that
> Humphrey & Bello do NOT carry the above-human-agreement claim, their systems scoring below their
> measured annotator agreement. **This session met that finding before reading this paper.** So
> this extract is independent of session 1's extract on everything EXCEPT that point, on which it
> is not independent at all. **It is recorded below as a confirmation, never as an independent
> discovery.** The route to a fully blind reading, if the user wants one, is the one the
> continuation names: hand this paper to a session that has read neither the continuation nor the
> population file.
>
> Neither `reading_pass/extracts/` nor `docs/research_papers/reading_pass_2026_08/` was opened for
> this paper before this file was written. Read at
> **`https://archives.ismir.net/ismir2015/paper/000294.pdf`** — the true archive URL, which the
> register's R-9 row does not carry (it cites 000119, a different paper).
>
> **GRADE: RELAYED, not at-the-object.** Same web-fetch bound as the other second-pass extracts.

## Identity

Eric J. Humphrey & Juan P. Bello, "Four Timely Insights on Automatic Chord Estimation",
*Proceedings of the 16th International Society for Music Information Retrieval Conference*
(ISMIR 2015), pp. 673–679.

**The identity is confirmed at the object of the fetch: paper 000294 is this paper.** R-9's
mis-filing is therefore established from both ends — session 1 established that the locally held
file named for this paper contains a different one (Chen, Su & Yang's electric-guitar paper), and
this pass establishes that 000294 is the paper the register's row should have cited.

## The V12 point — a CONFIRMATION, not an independent finding (see the banner)

**[FACT] The paper's systems score BELOW its measured human–human agreement, not above it.**
Verbatim: *"That said, the human annotators do agree a deal more that is attained by either system,
indicating that there is likely room for improvement."* **[sic] on the paper's own grammar.**

The numbers, Table 2, on the Rock Corpus's dual annotations:

| Comparison | root | tetrads |
|---|---|---|
| **Annotator against annotator** (DT–TdC) | **0.932** | **0.835** |
| kHMM against the best reference | — | 0.590 |
| DNN against the best reference | — | 0.540 |
| System against system (kHMM–DNN) | — | 0.678 |

Full annotator-agreement row as relayed: root 0.932, thirds 0.903, majmin 0.905, mirex 0.902,
triads 0.898, sevenths 0.842, tetrads 0.835, v157 0.838.

**Asked directly whether the paper anywhere claims machines already match or exceed human
agreement, the answer is: no.** **So V12's negative establishment holds at the primary.** The
above-human-agreement claim's actual primary is Koops et al.'s Utrecht technical report, as session
1's verification recorded.

## The four insights, as the paper states them

1. *"music recordings that invalidate tacit assumptions about harmony and tonality result in
   erroneous and even misleading performance"*
2. *"standard lexicons and comparison methods struggle to reflect the natural relationships between
   chords"*
3. *"conventional approaches conflate the competing goals of recognition and transcription to some
   undefined degree"*
4. *"the perception of chords in real music can be highly subjective, making the very notion of
   'ground truth' annotations tenuous"*

## Claims, labeled

**★ [FACT] INSIGHT 3 IS THE ONE THIS PROJECT SHOULD MEET FIRST, AND IT IS A DISTINCTION, NOT A
MEASUREMENT.** The paper separates two tasks that share a name. **Chord transcription** is
*"an abstract task related to functional analysis, taking into consideration high-level concepts
such as long term musical structure, repetition, segmentation or key."* **Chord recognition** is
*"quite literal, and is closely related to polyphonic pitch detection."* The defect: *"both
interpretations are easily found in the collection of reference annotations, however, conflating
these two tasks to some unknown degree"* — so a system is graded against a reference set that is a
mixture of two different tasks, in unknown proportion.

**[FACT] Insight 1 — the two named ways real recordings break the assumptions.** *Tuning:*
recordings *"not tuned to A440, with some varying by more than a quarter-tone"*, causing estimates
that differ *"by a semitone from the reference"*. *Repertoire:* some tracks *"do not truly make use
of, and are thus not well described by, chords"* — the examples named span *"rap, hip hop, reggae,
funk and disco"*. The conclusion, verbatim: *"chords may not be a valid way to describe all kinds
of music."* **Both are audio- and popular-repertoire-specific; neither transfers to notated
common-practice music without argument.**

**★ [FACT] INSIGHT 2 — FLAT ONE-OF-K CHORD CLASSES MISREPRESENT THE RELATIONSHIPS BETWEEN CHORDS.**
Verbatim: *"Chords are naturally related to each other hierarchically, and cannot always be treated
as distinct classes"*, the worked case being that *"C:maj7 and C:maj"* are not mutually exclusive
*"since the former contains the latter"*. And on the evaluation consequence: *"this quantization
process assigns all observations to a one-of-K representation effectively making all errors
equivalent. For the purposes of stable evaluation, this can have significantly negative
consequences."*

**[FACT] The proposal it makes instead — a continuous affinity vector over multiple human
references.** Verbatim: *"Synthesizing multiple human perspectives into a continuous-valued chord
affinity vector would allow for more stable evaluation by encoding the degree to which a chord label
applies to an observation."* **Proposed, not built and not measured in this paper.**

**[FACT] Insight 4's own conclusion about ground truth.** *"the subjective nature of chord
perception may render objective ground truth and evaluation untenable"*, and the open question
stated as such: *"it is an open question as to how an estimated annotation might best be compared
against more than one human reference."*

**[FACT] The dual-annotation evidence base.** The **Rock Corpus** — 200 popular rock tracks with two
independent expert transcriptions, a pianist and a guitarist. On the tetrads comparison, *"more than
a 15% discrepancy"* between the two annotators; on one track (*"I Saw Her Standing There"*),
*"no two reference annotations correspond to greater than a 65% agreement."*

**[FACT] The glass-ceiling claim.** *"system performance appears to be converging to yet another
glass ceiling"*, and *"performance appears to be tapering off, as evidenced by recent years'
results."*

**[FACT] The systems and their corpora.** Two audio systems: a **DNN** taking *"Time-frequency
patches of local contrast normalized constant-Q spectra"*, and a **kHMM** taking a *"multiband
chroma representation … computed from beat-synchronous audio analysis"*. Corpora: Isophonics
(200 Beatles and Queen songs), McGill Billboard (700+ annotations, ~1000 total), MARL/NYU (295
annotations — 195 US-Pop, 100 RWC-Pop) and the Rock Corpus (200 tracks, dual). Merged training set
**1,217 unique tracks**. Vocabulary **157 chord classes** (13 qualities × 12 roots, plus no-chord).
Evaluation through `mir_eval`'s comparison functions: root, thirds, majmin, mirex, triads, sevenths,
tetrads, v157. On ground truth at tetrads (Table 1): kHMM **0.721**, DNN **0.705**.

**[FACT] A stated evaluation caveat of its own.** The Rock Corpus evaluation acknowledges *"a
mismatch in chord vocabulary"*.

## Coupling facts (the commission's mandatory widening)

**★ THE DOMAIN BOUND IS THE COUPLING FACT HERE, AND IT IS DECISIVE FOR HOW THIS ROW MAY BE USED.**
Everything measured in this paper is **audio**, on **popular music** — Beatles, Queen, Billboard,
US-Pop, RWC-Pop, rock — with **two annotators on the one dual-annotated set**. It assumes upstream
an audio signal and a tuning reference; it hands downstream a time-aligned chord label sequence
over a 157-class flat vocabulary. **Nothing about notated common-practice music, nothing symbolic,
nothing about Roman numerals, keys or functions is measured anywhere in it.**

**This is the same off-domain class principle #21 already refuses as a ground-truth ceiling for this
project's repertoire, and the same bound V12's own record attaches to the Koops figures.** The
insights may travel as arguments; **the numbers do not travel at all.**

**Its own stated scope:** *"This work explores the behavior of these two high performing, systems as
a means of understanding obstacles and limitations in chord estimation"* **[sic]** — a diagnostic
study of two systems, not a method paper.

## Bearing, flagged for the findings surface (verdicts are Task 4's, not this file's)

- **R-9's true paper is now read at its primary from both ends** — the mis-filed local file
  identified by session 1, and 000294 confirmed as the right paper here.
- **V12 stands as session 1 recorded it:** this paper does not carry the above-human-agreement
  claim, and its own systems fall well short of its measured annotator agreement.
- **Insight 3 — the recognition/transcription conflation — is the one item here with a real claim
  on this project's attention**, because it is about what a reference annotation set *is*, not about
  audio. Whether it bears on this project's own ground truth is a question for Task 4 and is not
  answered here.
- **Insight 2's argument against flat one-of-K chord classes** is adjacent to what rows 1 and 3 do
  from the other direction — a holistic symbol vocabulary and a typed graph respectively. **Adjacent
  is not the same as agreeing, and nothing here measures the comparison.**

## What this extract does NOT establish

- The full Table 1 and Table 2 beyond the values quoted.
- Whether the Rock Corpus's two annotators worked independently or reviewed each other.
- What "v157" measures precisely as a comparison function.
- Whether the affinity-vector proposal was subsequently built by anyone.
- **Nothing here is at-the-object.** Every figure and quotation is relayed.

*Provenance: second pass of the reading pass, 2026-08-31, with the V12 contamination declared at
this file's head. Read at the archive URL only. No specification derived, no document amended, no
code opened, no register touched — including the bibliography's R-9 row, whose URL correction
belongs to the reconciliation act.*
