# EXTRACT — Ju, Margot, McKay, Dahn & Fujinaga 2020, "Automatic Figured Bass Annotation Using the New Bach Chorales Figured Bass Dataset" — Task B candidacy row 36, SECOND pass, AT THE OBJECT

> **STATUS: SECOND-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-10-15).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet: a CENTRAL source extracted in a second
> independent pass and then cross-checked against the first. Row 36 was decided CENTRAL by entry 395.
>
> **The grade.** Seven pages, printed pp. 640–646, read as page images through the bridge; the page count
> was established at the tool by an out-of-range request (it answered "PDF has 7 pages"), and all seven
> images were seen to be present, not merely the call to succeed. No relay, no web read.
>
> **The independence bound, declared and not claimed away.** Before this extraction the writing session had
> read: entry 395 §2, which states the first extract's finding (1) — the 3% / 64.5% / 85.3% figures, their
> pages, and that the sealed first-stage draft pairs two of them; entry 395 §3, which states that this side's
> reading is that L3 needs L2's published elaboration relations for the figured bass, that the paper's
> equivalence rules are the natural grading rule, that the paper's slice is cut at onsets only, and that the
> dataset's overlap with the regression corpus is unchecked; entry 404, which names the paper's subject; and
> the 2026-10-15 first-pass ruling record's item 8. **The first extract itself was not opened before this
> file was landed.** So this pass is independent of the first extract's text, and not independent of the
> four findings just named.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Yaolong Ju, Sylvain Margot, Cory McKay, Luke Dahn & Ichiro Fujinaga, "Automatic Figured Bass Annotation
Using the New Bach Chorales Figured Bass Dataset", in *Proc. of the 21st International Society for Music
Information Retrieval Conf.*, Montréal, Canada, 2020 (conference dates October 11–16, 2020), pp. 640–646.
McGill University (Ju, Margot, Fujinaga); Marianopolis College (McKay); The University of Utah (Dahn).
Licensed CC BY 4.0 (page 640).

**File:** `docs/research_papers/ju_margot_mckay_dahn_fujinaga_2020_ismir_bcfb_figured_bass.pdf`.

## Claims, labeled

### What figured bass is, as the paper uses the term

**[THEORY, §1, p. 640]** Figured bass is notation that uses numerals and other symbols to indicate the
intervals to be played above a bass note. The paper names three aspects of the figured bass annotations
(its abbreviation: FBAs) to be highlighted: (1) the Neue Bach Ausgabe edition writes raised intervals with
a backslash through the numeral and lowered ones with a forward slash; (2) an FBA followed by a
continuation line indicates that the harmony of the preceding figure is prolonged; (3) *"Multiple FBAs over
a stationary bass (e.g., 4–3 in m. 5) usually indicate a suspension being resolved."*

**[FACT, Fig. 1 caption, p. 641]** *"FBAs do not always specify all the notes to be played by the continuo
player, and usually omit some obvious figures"* — the caption's example is a "6" over B♭ where the D (a
third above) is not written but would typically be played.

**[FACT, §1, p. 640]** The authors found two earlier papers on automatic figured bass annotation, both
rule-based: Barthélemy and Bonardi, who *"treated figured bass as a harmonic reduction and devised rules to
identify and remove ornamental notes, permitting them to cluster the remaining chord tones as figures"*; and
Wead and Knopke, who *"manually designed a decision tree to determine the figured bass for a given bass
line"*. Neither, they state, has open-source code or quantitative results. They state they are not aware of
any previous machine-learning application to figured bass, nor of any digital dataset with FBAs.

### The dataset (BCFB)

**[FACT, §2, p. 641]** The Bach Chorales Figured Bass dataset holds **139** four-voice Bach chorales that
carry Bach's own figured bass, encoded in MusicXML, \*\*kern and MEI, based on the Neue Bach Ausgabe (NBA)
critical edition. The 139 were found by building a reference table of **420** chorales attributed to Bach,
indexed by BWV number and cross-referenced with the NBA, and checking which settings have original FBAs
accessible. The chorales come from larger works: cantatas, passions, motets and the Christmas Oratorio.

**[FACT, §2.2, p. 641]** **109** of the 139 were taken from existing \*\*kern encodings on KernScores,
translated automatically to MusicXML with music21 (v. 5.1.0), and edited to match the NBA (footnote 5:
adding a continuo line and/or instrumental voices, transposing, changing meter, pitch and duration of
certain notes; the textual content was not encoded). The remaining **30** were encoded by hand. MusicXML is
the master format; MuseScore 3 was the editor for both musical content and FBAs.

**[FACT, §2.3, pp. 641–642]** MusicXML → \*\*kern by musicxml2hum worked except for continuation lines;
\*\*kern → MEI by Verovio *"was perfect"*; direct MusicXML → MEI by Verovio lost accidentals, slashes and
continuation lines, so the MEI files were made from \*\*kern after the continuation lines were added to the
\*\*kern files by hand in a text editor.

**[FACT, footnotes 2 and 3, p. 641]** The Breitkopf edition contains 371 four-voice chorales; KernScores
holds 371 four-part chorales in \*\*kern.

### The data used for the experiments

**[FACT, §3.1, p. 642]** 120 of the 139 chorales were used. Excluded: 12 chorales with elaborate
instrumental interludes between phrases (listed in footnote 14); five *"barely figured"* chorales (footnote
15: BWV 16.06, 48.07, 149.07, 195.06 and 447); and BWV 8.06 and 161.06, *"because they feature irregular
textures, such as having an obbligato continuo and/or instrumental part."* *(12 + 5 + 2 = 19, and
139 − 19 = 120; the arithmetic is this extract's, and it closes.)*

### The simple rule-based labeller

**[FACT, §3.2.1, p. 642]** It labels all the intervals above the bass. The music is cut into **note onset
slices**: *"A new slice is formed whenever a new note onset occurs in any musical voice, and each slice
consists of the vertical set of notes sounding at that moment."* Worked example: pitch classes G, D and B
above a bass G give the generated FBA 8/5/3.

**[FACT, §3.2.1, p. 642]** Against Bach's original FBAs, *"the percentage of exact matches was only 3%"*.
The authors attribute this partly to Bach not labelling every interval above the bass, Baroque FBAs
being in effect abbreviations that omit obvious intervals; their example is m. 3.2.5 of Fig. 2, where A and
D sound above F♯ but only the D is figured ("6").

### The evaluation metric — the equivalence rules

**[FACT, §3.2.2, p. 642]** A metric that *"treats figures that are musically equivalent as notationally
equivalent"*, its rules *"inspired by Arnold [11]"* (F. T. Arnold, *The Art of Accompaniment from a
Thorough-bass*, 1931):

- a **3** can be omitted unless there is a 4th in the sonority, or the 3rd is the resolution of a 4–3
  suspension;
- a **5** can be omitted unless there is a 6th in the sonority, the 5th is the resolution of a 6–5
  suspension, or the 5th has an accidental;
- an **8** can be omitted unless there is a 9th in the sonority, the 8th is the resolution of a 9–8
  suspension, or the 8th has an accidental;
- a **6** can be omitted if the sonority forms a 6/4/3 or a 6/4/2 chord.

**[FACT, footnote 19, p. 642]** *"Sonority" means the set of pitch classes present in a note onset slice*,
and *"4th"* means a wrapped interval of a fourth between the bass and an upper voice, *"regardless of
whether it is labelled in the figured bass."*

**[FACT, §3.2.2, p. 643, Fig. 3]** Worked example: for a root-position dominant seventh, "7", "7/3", "7/5"
and "7/5/3" are all equivalent under the metric, so a generated figure and a ground-truth figure that are
any pairing of these count as correct.

### The improved rule-based labeller

**[FACT, §3.2.3, p. 643]** Under the metric, the simple labeller has *"an effective agreement of 64.5% with
Bach's FBAs"*; where they disagreed the generated FBAs *"tend to have more figures than those of Bach."* Two
families of rules were added by hand:

1. In each note onset slice, the figure for a note in an upper voice is omitted if both (1) the note was
   labelled in the previous slice and (2) the bass pitch class is unchanged from the previous slice.
2. On fractional beats (e.g. beat 2.5 and 3.5), ornamental notes — *"passing tones, neighbour tones,
   escape tones, and anticipations, which are all approached or departed by step"* — are looked for. If
   such a note is in an upper voice its number is removed from the figure; if it is in the bass, the slice
   is left entirely unfigured.

**[FACT, §3.2.3, p. 643]** *"After the addition of these rules, the model was able to achieve 85.3%
agreement with Bach's figures, a large improvement over the 64.5% agreement achieved with the simple method
and equivalency rules."*

**[FACT, footnote 20, p. 643]** *"The rules were proposed by observing the generated FBAs and were evaluated
against the ground truth FBAs from BCFB. We selected the rules that yielded higher accuracy."* The body text
adds that more rules were not developed partly because *"we wanted to avoid overfitting our rules"*.

### The machine-learning labellers

**[FACT, §3.3.1, p. 643]** Each FBA is converted to an **interval-class vector** of 12 elements over
*ordered* interval classes from the bass upward (0–11, footnote 21), including *"all the notes above the
bass that are sounding in the current slice"*. Where a figure does not give the exact interval (a "6" may
be major or minor), the score is consulted by heuristic post-processing; converting back, pitch spelling in
the score decides between, e.g., "♭3" and "♯2" (footnote 22 gives the "2"/"9" case: the actual note above
the bass is found and compared).

**[FACT, §3.3.2, pp. 643–644]** Three binary input vectors per slice: interval classes (12); onsets (12 —
which notes above the bass have onsets within the slice rather than being held); metrical context (3 —
downbeat, another beat, or a fractional beat). 27 per slice; the previous and following slices' vectors are
appended (zero-padded at the ends), giving 81.

**[FACT, §3.3.3, p. 644]** Two learners: a decision tree (scikit-learn `DecisionTreeClassifier`, default
settings, an optimised CART — footnote 24) and a feedforward deep neural network (three hidden layers of 300
units, Adam, binary cross-entropy, hyperparameters tuned on the validation set — footnote 25). Each outputs
a 12-element binary vector of semitones above the bass.

**[FACT, §3.3.4, p. 644]** Ten-fold cross-validation. Network: 80% training, 10% validation (also used for
early stopping, footnote 27), 10% testing. Decision tree: 90% training (the union of the network's training
and validation folds), 10% testing, matching the network's test folds.

## Measured results, as the paper states them

| Method | Corpus | Metric | Value | Where |
|---|---|---|---|---|
| Simple rule-based | BCFB, 120 chorales (see the note below the table) | exact match with Bach's FBAs | 3% | p. 642 |
| Simple rule-based | same | agreement under the equivalence metric | 64.5% | p. 643 |
| Improved rule-based | same | agreement under the equivalence metric | 85.3% | p. 643; abstract; §5 |
| Decision tree | same, ten-fold cross-validation | classification accuracy under the equivalence metric | 84.3 ± 0.5% | p. 644 |
| Deep neural network | same, ten-fold cross-validation | classification accuracy under the equivalence metric | 85.9 ± 0.6% | p. 644; abstract; §5 |

*The corpus column:* §3.1 says the 120 chorales were used *"to train and test our models"*; that the
rule-based figures are measured over the same 120 is this extract's reading — the paper does not state the
rule-based labellers' corpus separately.

**[FACT, footnote 28, p. 644]** The ± values are *"standard error across cross-validation folds."* No
uncertainty is stated for the rule-based figures.

**[FACT, abstract, p. 640]** The abstract pairs **85.3%** (rule-based) and **85.9%** (machine learning) as
the two approaches' accuracies on BCFB.

**[FACT, §5, p. 645]** *"the machine learning models did not outperform the rule-based model"*; the authors
offer *"the relatively small size of BCFB"* as a potential reason.

## Discussion of errors, as the paper states it (§4, p. 644; Fig. 4, p. 645)

**[FACT]** *"One common error made by our model was to miss figures that indicate the resolution of a
suspension, such as the 9–8 shown in Fig. 4(a), m. 8.4. This may be because the features we used did not
contain sufficient voice-leading information to detect such suspensions."* Fig. 4 is the best-performing
model on m. 8 of BWV 108.06 and mm. 2–3 of BWV 145.05.

**[FACT]** Two disagreements the authors judge *"theoretically acceptable answers"*: at m. 2.3 the model
wrote "♯" where Bach wrote nothing, and the D is sharpened in the soprano; at m. 3.2 the model wrote "♯7"
where Bach did not, possibly because Bach treated the D♯ as a passing tone or as diatonic in a Dorian tune.

**[FACT]** Bach's own variability under seemingly similar contexts: accidentals labelled once and not the
next time (m. 2.3 against m. 3.3); suspensions sometimes labelled (m. 8.4 of Fig. 4(a)) and sometimes not
(m. 1.4 of BWV 194.06); the same chord figured 6/4/2 at one place and 4/2 at another (m. 10.4 of BWV 13.06
against m. 2.1 of Fig. 4(b)). *"So, one cannot expect 100% agreement to be achievable, given such
variability. Bach, like everyone, was sometimes inconsistent with himself, which imposes an artificial
performance ceiling on our models [12]."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic four-voice score with the bass voice identified and
pitch spelling present (spelling is read back to choose between enharmonic figures, §3.3.1); metric
position at the level of downbeat / other beat / fractional beat (§3.3.2, and the improved rule's
fractional-beat test, §3.2.3); note onsets per voice, which define the slices. **It assumes no key and no
chord.** In §3 as read, neither the rule-based labellers nor the learners take a tonality or a chord label
as input. The improved rule-based labeller decides *on its own* which notes are passing, neighbour,
escape or anticipation tones, by a local stepwise-approach test on fractional beats.

**What it HANDS downstream.** One figure per note onset slice — an interval-class vector converted back to
figures with flats and sharps for lowered and raised intervals, and **no continuation lines** (footnote 12,
p. 642).

**Its own STATED SCOPE and limits.** One composer, one genre: Bach's four-voice chorales with his own
figures, 120 of 139 after exclusions. The rule set was selected against the same ground truth it is
reported on (footnote 20). The authors name a ceiling set by Bach's own inconsistency, and the dataset's
small size as a possible reason the learners did not do better. Further work they name (§5): adding
voice-leading information; improving the rule-based model, e.g. by reading the trained decision trees;
figured bass from other Bach works and other Baroque composers.

**What the authors propose it be used for (§5, p. 645) — a proposal, not a result.** Generating figured bass
first and then converting the figures to chord labels, so that a chord classifier can use what Bach's
figures encode; they place this beside existing methods that identify chords directly from the music, or
identify and remove non-chord tones first and label the chord from what remains.

## What an L3 detail specification could adopt, adapt, or must argue against

*This section is this extract's reading of how the paper meets this project's frame. Facts about the paper
are labeled FACT with their page; each consequence drawn for this project is labeled CONJECTURE, and where
it rests on a project object read in this sitting, that object is named.*

**(a) The figured bass as computed here needs no decided chord and no key.** [FACT about the paper, from
§3; the consequence is CONJECTURE.] `FRAMEWORK.md` §5 places the figured bass among the facts L3 publishes,
given a settled tonal reading. The paper shows a figured bass computed from the bass, the sounding pitches
and the meter alone, reaching 85.3% under its own metric (a figure with the bound stated at finding (2)).
So this paper gives no support to a claim that the figured bass *needs* the tonal reading; what it does
show is that the figure depends heavily on deciding which notes are elaborations (item (b)). If the L3
placement is defended, this paper points at that dependence as the ground, not at the key or the chord.

**(b) The improved labeller's gain comes with rules that decide which notes are elaborations.** [FACT: 64.5% → 85.3%,
and the second family of added rules removes passing, neighbour, escape and anticipation tones, p. 643.
Which of the two added rule families produced how much of the gain is NOT stated in the paper.] In this
project's frame, the L2 → L3 contract in `FRAMEWORK.md` §5 carries *"chord-tone assignment and elaboration
relation per note"* forward to L3, and the fact-publication corollary in `CLAUDE.md` says consumers read
and never re-derive. **So an L3 figured bass that removed elaborations by its own local stepwise rule, as
the paper does, would be re-deriving a fact L2 publishes.** That makes the paper's improved rules a method
L3 must argue against in form, while its result is evidence that the elaboration decision is what the
figured bass most depends on. [CONJECTURE, resting on the two project objects named.]

**(c) The suspension figures.** [FACT: the learners' most common named error is the missed 9–8 resolution;
the authors attribute it to missing voice-leading information, p. 644.] A figure such as 9–8 or 4–3 names
a dissonance and its resolution over a held bass — a voice-leading relation across slices, not a property of
one slice's pitch-class set. [THEORY.] Whether L2's published elaboration relation names a suspension and
its resolution, so that L3 can figure 9–8 by reading it, is **not settled by this extract**; it is a
question for the L3 detail specification against L2's published facts.

**(d) The slice is not this project's slice.** [FACT about the paper: a new slice at every note onset in any
voice, p. 642.] This project's slice begins when any note starts **or stops** (`DECISIONS.md`, terms table,
"slice"). A figure written in this paper's onset slices is therefore not one-to-one with figures over this
project's slices where a note is released without a new onset. A comparison against BCFB would need a stated
alignment. [CONJECTURE about the consequence.]

**(e) The equivalence rules are a grading convention, and grading is measurement design.** [FACT: the
rules, p. 642; `FRAMEWORK.md` §5 names the measurement of the analysis as NOT A LAYER and a later stage's
business.] Routed to measurement design, not to the L3 specification.

## Findings, routed and not applied

**(1) The three figures belong to two different labellers, and the pairing matters.** [FACT, pp. 642–643.]
3% is the *simple* labeller under *exact* match; 64.5% is the *same simple* labeller under the
*equivalence* metric; 85.3% is the *improved* labeller — with its hand-selected omission and elaboration
rules — under the equivalence metric. Any sentence pairing 3% with 85.3% as one labeller's two scores, or
reading the gap between them as notation convention alone, says more than the paper does: the 3% → 64.5%
step is the metric, and the 64.5% → 85.3% step is new rules, one family of which removes non-chord tones.
**Routed to the cross-check of the sealed first-stage draft's statement; not applied here.**

**(2) The 85.3% is not a held-out figure.** [FACT: footnote 20 — the rules were selected by their accuracy
against the same ground truth.] The learners' figures are ten-fold cross-validated with stated standard
errors; the rule-based figure is fitted and self-measured, and the paper states no uncertainty for it. Under `CLAUDE.md`
principle #20 a fitted-and-self-measured number is not established. **So the abstract's 85.3% against
85.9% is not a like-for-like comparison**, and the paper's own §5 sentence that the learners *"did not
outperform"* the rule-based model compares a selected-on-test figure with cross-validated ones. **Routed to
measurement design and to any specification sentence that cites 85.3%.**

**(3) A stated ground-truth ceiling, on this project's own repertoire.** [FACT, p. 644.] Bach is
inconsistent with himself in figuring, and the authors call the result an artificial ceiling. This bears on
`CLAUDE.md` principle #21 (ground truth is a measurement tool too) for any figured-bass measurement. No
agreement figure is given for it. **Routed to measurement design.**

**(4) A Bach-chorale ground truth that is not a Roman-numeral analysis.** BCFB is the composer's own
figures, not an analyst's labels. Whether BCFB is held in this repository, and whether its chorales overlap
the regression corpus, was **not checked** in this sitting; `DECISIONS.md` D-514 makes an overlapping
annotation set record-only without a user ruling. **Routed to the staged-score and measurement sessions.**

**(5) No falsifier.** Nothing read contradicts a chosen design point of `FRAMEWORK.md` that this sitting
read (the L3 block, DP-I). Finding (a) above narrows what the L3 placement of the figured bass can rest on;
it does not contradict that placement. **No STOP fires** under the commission's §6, as far as the design
points read reach.

## Closing — the read-back and the sweep, written after both were run

**Read back against the pages.** The finished text was compared with the seven page images. Three
corrections were made before this section was added: the measured-results table's corpus column claimed
120 chorales for the rule-based figures, which the paper does not state separately (now marked as this
extract's reading, below the table); item (a) said the L3 placement *"cannot rest"* on the figured bass
needing the tonal reading, which is wider than a paper reaching 85.3% can carry (narrowed to *"gives no
support to"*); and item (b)'s heading claimed the *"largest gain"* came from the elaboration rules while its
own body says the paper does not split the gain between its two rule families (heading narrowed).

**Swept for absolutes**, every hit of *only, never, every, all, none, no, nothing, always, complete, whole,
any, cannot* read at its line. Two more were narrowed: the coupling-facts sentence that no input anywhere
in §3 is a key or chord is now scoped to *"§3 as read"*; and *"carries no uncertainty"* became *"the paper
states no uncertainty for it"*. The section-(a)-to-(e) preamble claimed every statement there was a
conjecture, which was false of its FACT-labeled sentences, and was rewritten. The remaining hits are the
paper's own words in quotation, or are scoped at their line.

**Not done here:** the first extract was not opened; the cross-check is a later act on this landed file.

## The cross-check against the first extract (2026-10-15, after this file had landed)

The first extract (`reading_pass/extracts/` under the same file name, 22,387 bytes at the folder listing)
was opened only after this file had landed at 23,432 bytes, and was read whole.

**Agreed, value for value:** every figure both extracts transcribe — 139, 420, 109 and 30, 120 after
the 12 + 5 + 2 exclusions; 3%, 64.5% and 85.3%; 84.3 ± 0.5% and 85.9 ± 0.6% with the ± as standard error
across folds; the 12 + 12 + 3 = 27 and 81 input sizes; the 80/10/10 and 90/10 splits; the four
equivalence rules; footnote 20's rule selection; the authors' §5 proposal. The two extracts reach the
same finding on the sealed draft's pairing of 3% with 85.3% (this file's finding (1), the first's
finding (1)), on the 85.3% not being held out, on the slice being cut at onsets only, and on BCFB's
overlap with the regression corpus being unchecked — the last three of which this pass had read in
entry 395 before extracting, as its independence bound declares.

**Disagreements, each resolved at the paper:**

- **The first extract's quotation "obligato"** (its §3.1 claim). The page reads *"obbligato"* (p. 642).
  The first extract is corrected at its site, former wording kept.
- **The first extract's "decided by whether the note is an octave or more above the bass"** for footnote
  22. The footnote says *"If they are one octave apart, the generated figure will be "9", and "2"
  otherwise."* Corrected at its site, former wording kept.
- **The corpus of the rule-based figures.** The first extract's results table says "Corpus for all rows:
  BCFB, 120 of its 139 chorales (§3.1)"; this file marks that as a reading for the rule-based rows. At
  the paper: §3.1 says the 120 were used *"to train and test our models"*, and p. 643 calls the improved
  rule-based labeller *"the model"* (*"the model was able to achieve 85.3% agreement"*). So the first
  extract's reading is supported by the paper's own wording, and is still not stated in so many words.
  **Neither extract is changed for it**; this note records the support.

**Recorded, not resolvable at the paper — a difference of routing, not of fact.** The first extract
routes the equivalence rules to the L3 specification as *"the grading rule for any figured bass L3
publishes"*; this file routes them to measurement design, because `FRAMEWORK.md` §5 names the
measurement of the analysis as NOT A LAYER and a later stage's business. The first extract's own bullet
says a *measurement* of L3's figured bass would need them, so the two agree on what the rules are for and
differ only on which document carries them. Left for the L3 specification's author; no extract changed.

**Found only by this pass:** the abstract's 85.3% against 85.9% is not a like-for-like comparison
(finding (2) here); the Fig. 1 caption's statement that figures omit obvious notes; footnote 19's
definition of "4th" as a wrapped interval regardless of whether it is labelled. **Found only by the
first pass:** that what a cross-validation fold is cut by (chorale or slice), and what unit the accuracy
counts, are not stated in the pages — this pass did not look for either and does not dispute them; and
the chorales being *"largely homorhythmic"* (p. 642), which this pass's coupling facts omit.

No claim is made that the comparison was exhaustive: it ran over what both extracts carry.
