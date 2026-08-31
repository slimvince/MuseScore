# Second-pass extract — row 2: McLeod & Rohrmeier 2024, chord tone alterations and suspensions

> **STATUS: SECOND INDEPENDENT EXTRACTION (session 2 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the independence protocol
> of `reading_pass/continuation.md` §2. **Neither `reading_pass/extracts/` nor
> `docs/research_papers/reading_pass_2026_08/` was opened for this paper before this file was
> written.** Read at its source, `https://apmcleod.github.io/pdf/chord-sus-jnmr.pdf`, in two
> separately-prompted passes.
>
> **GRADE, DECLARED AT ITS FACE: RELAYED, not at-the-object.** This environment's web-fetch tool
> answers prompted questions over a document rather than returning its text or its pages. Quoted
> wording below is the tool's relay of the paper's wording. Session-and-prompt independence, not
> read-tool independence — see the cross-check.

## Identity

Andrew McLeod & Martin Rohrmeier, "Detecting Chord Tone Alterations and Suspensions", *Journal of
New Music Research*, published 11 October 2024, doi `10.1080/09298215.2024.2412595`.

## The claim that matters most, first — because DP-D turns on it

**[FACT] Alterations and suspensions are decided POST HOC, on a chord label whose root and quality
are already fixed.** The method *"takes as input a musical score with such labels and adds chord
tone alterations such as suspensions to them"*, where the input labels already carry *"at least a
root pitch and a chord quality."* Per unit: it *"takes as input a chord label (and the notes
present in the score for the duration of that label) and output a set of pitch classes (PCs) that
should be incorporated into the label."*

**[FACT] The input label's root, quality and inversion are HELD FIXED — the method only augments
them. But the SEGMENTATION is not held fixed:** consecutive windows are merged where their pitch-class
vectors are compatible, so boundaries do move under this step.

**[FACT] The stated reason for the post-hoc shape is vocabulary size, not a claim that post-hoc is
better.** *"It is an important aspect of harmonic analysis, [but] it is infeasible to do so by
simply adding features to the labels in the vocabulary, given the multiplicative effect on
vocabulary sizes"*, and *"no chord labeling model has yet been proposed that includes an analysis
of such complex chord forms directly in their output chord labels."*

**★ [FACT of absence, established by a targeted read] THE PAPER DOES NOT COMPARE POST-HOC AGAINST
JOINT.** Asked directly, the text carries no discussion of doing chord-tone assignment jointly with
chord identification, no argument that post-hoc is preferable, and no measurement of what post-hoc
costs. **Its choice is a response to a vocabulary-explosion problem in the label space, not a
finding against joint assignment.** This is the single most load-bearing thing in the paper for
this project, and it is stated here as an absence rather than filled.

## The method, step by step

**[FACT] Three steps.** (1) A **Chord Pitches Model (CPM)** assigns every note a probability that it
is *"important" — that it is not an ornamentation and rather belongs in the chord label*. (2) Those
probabilities are pooled into windowed pitch-class probability vectors and **binarized against
thresholds**. (3) Neighbouring vectors are **iteratively merged** under compatibility rules.

**[FACT] The CPM's architecture and inputs.** A feed-forward layer, one or more **bi-directional**
LSTM layers, a feed-forward layer, and a single sigmoid output per note. Its features are: the
note's pitch class, octave, metrical level, duration and timing within the chord; the previous and
next chords' root, quality, inversion, key and diatonicity; and the current chord's quality and
context — **but not the current chord's root**. Its training target is 1 where the note's pitch
class appears in the ground-truth label and 0 otherwise.

**[FACT] Three tuned thresholds:** a default threshold *d* ∈ {0.7, 0.8, 0.9}, an add threshold
*a* ∈ {0.7, 0.8, 0.9}, and a replacement threshold *r* ∈ {0.5, 0.6, 0.7}.

**[FACT] The merge rule, relayed close to verbatim.** Two pitch-class vectors merge if identical;
or if *"each 1 in one vector corresponds to a 1 in the other"*; or if *"each vector has an 'extra'
1"* provided that extra is *"(1) … a default PC, and no extra PC in the other vector replaces it;
or (2) … a non-default PC, and no extra PC in the other vector is a replacement of it."*

**[FACT] The baseline is a rule set, not a null.** It includes the default pitch classes; detects
named alterations (diminished fifths in major triads, altered thirds in diminished triads); adds a
seventh where absent; recognises suspensions by two surface rules (a sixth without a fifth, a
fourth without a third); and then runs **the same merging procedure**. So the reported gains are
gains over a hand-written rule set with the same segmentation machinery, not over nothing.

## Measured results, as tabulated

**Corpus: 924 pieces** — the Annotated Beethoven Corpus, the Annotated Mozart Sonatas, and the
Corelli trio sonatas; 80/10/10 train/validation/test.
**Metric:** exact pitch-class-vector match per windowed segment, reported three ways — *default
accuracy* (windows whose ground-truth label contains only default pitch classes), *non-default
accuracy* (windows with at least one non-default pitch class), and overall.

**Given GROUND-TRUTH chord labels as input (Table 1):**

| Input vocabulary | Default | Non-default | Overall |
|---|---|---|---|
| Full | 96.1 | 36.7 | 89.2 |
| Triad | 84.5 | 35.3 | 78.4 |
| Major–minor | 84.0 | 28.8 | 77.2 |

**Given NOISY chord labels from a chord-labelling model (Table 3):**

| Input vocabulary | Default | Non-default | Overall |
|---|---|---|---|
| Full | 78.1 | 35.8 | 73.2 |
| Triad | 73.2 | 39.2 | 69.0 |
| Major–minor | 73.5 | 36.6 | 69.0 |

All comparisons against the baseline significant at *p* < .001.

**★ THE READING OF THOSE TWO TABLES THAT MATTERS.** The non-default column — the cases the whole
method exists for — **sits between 28.8 and 39.2 in every condition, and barely moves when the
input labels degrade from ground truth to a model's output.** The default column collapses by
roughly 18 points on the same degradation while the non-default column does not. The paper's own
gloss: *"There is clearly a difficulty in detecting non-default chord tones, which is expected
since they are the much rarer case, and there is an inherent trade-off between default and
non-default accuracy."*

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** a symbolic score, **plus a completed chord analysis** — per-span labels
carrying at least root and quality — plus the notes sounding for each label's duration. Metrical
level and local key are used as features. **This is the strongest upstream assumption in the
population so far: the method cannot run at all until something else has already decided the
chords and the spans.**

**HANDS downstream:** the same chord labels, augmented with a pitch-class set, from which a
descriptive label is generated (the paper's examples: `C4` for a fourth suspension, `C6/4` for the
cadential six-four). Boundaries may have moved by merging. **No rivals, no confidence surface** —
the binarized vector is committed.

**STATED SCOPE and limits:** Western classical harmonic analysis, with the authors noting that
alterations and extensions matter *"in much of harmonic analysis in general (e.g., in jazz)"*.
Non-default detection is acknowledged as hard and as trading off against default accuracy.
**Pedal tones: not stated anywhere** — the 2021 companion (row 1) named them as future work
alongside suspensions, and this paper does not deliver them.

**Its own definitions, such as they are:** a *chord tone* is a pitch class that should be included
in the chord label, as against ornamentation; a *non-chord tone* is ornamentation, or a note not
belonging in the label. **Neither "suspension" nor "alteration" is formally defined** — both are
used in their standard music-theory sense and shown by example.

## Bearing, flagged for the findings surface (verdicts are Task 4's, not this file's)

**DP-D is the one rival-shaped item, and this paper is the rival's best-published form.** What the
second pass establishes about it, stated flatly: the rival exists, it is measured, and it works
tolerably on the easy majority and poorly on the cases it was built for. It does **not** carry an
argument against joint assignment — its stated ground is a label-vocabulary problem, which is a
problem about the OUTPUT REPRESENTATION rather than about where in the inference the assignment
belongs. **Whether that leaves DP-D's ground untouched or partly answered is Task 4's verdict and
is not taken here.**

## What this extract does NOT establish

- The CPM's window definition (what fixes a window before merging).
- How the three thresholds were selected and on what split.
- Whether the 924-piece corpus overlaps the 742-piece internal corpus of row 1.
- The per-alteration-type breakdown, if the paper carries one.
- **Nothing here is at-the-object.** Every figure and quotation is relayed.

*Provenance: second pass of the reading pass, 2026-08-31. Read at the source URL only. No
specification derived, no document amended, no code opened, no register touched.*
