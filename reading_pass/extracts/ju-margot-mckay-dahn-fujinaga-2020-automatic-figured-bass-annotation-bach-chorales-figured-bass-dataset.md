# EXTRACT — Ju, Margot, McKay, Dahn & Fujinaga 2020, "Automatic Figured Bass Annotation Using the New Bach Chorales Figured Bass Dataset" — Task B candidacy row 36, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-10-14).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** The PDF has 7 pages, established at the tool by a deliberately out-of-range request
> (the tool answered "PDF has 7 pages"). All seven (printed pp. 640–646) were read AT THE OBJECT as page
> images through the bridge, and the seven images were checked to be present, not only the call's
> success. **No relay, no web-fetch read.** Every quotation carries its printed page or section.
>
> **Why this paper.** Row 36 of `reading_pass/candidacy_upgrades.md`, ADMITTED because *"L3 publishes
> the figured bass and the read set contains no producer for it"*. Placed in L3's reading slice by
> handoff entry 394 §2; the one row of that slice that was unread.
>
> **Independence.** No earlier extract of this paper exists in `reading_pass/extracts/` or
> `reading_pass/extracts_second_pass/` (handoff entry 393 §2, by listing; this session's listing of
> `reading_pass/extracts/` confirms no file of this paper there). Before reading the paper this session
> had not opened `FRAMEWORK.md`; after reading it, it read `FRAMEWORK.md` at the L3 charter and at
> every line a search for "figured bass" found, in order to write the findings below.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Yaolong Ju, Sylvain Margot, Cory McKay, Luke Dahn & Ichiro Fujinaga, "Automatic Figured Bass Annotation
Using the New Bach Chorales Figured Bass Dataset", *Proceedings of the 21st International Society for
Music Information Retrieval Conference (ISMIR 2020)*, Montréal, pp. 640–646. Schulich School of Music,
McGill University; Department of Liberal and Creative Arts, Marianopolis College; School of Music, The
University of Utah. CC BY 4.0 (640).

**File:** `docs/research_papers/ju_margot_mckay_dahn_fujinaga_2020_ismir_bcfb_figured_bass.pdf`
(1,022,218 bytes at the staging result).

## Claims, labeled

### What the paper contributes, in its own list (§1, 640)

**[FACT, §1]** Four contributions: (1) the Bach Chorales Figured Bass dataset (BCFB), *"139 chorales
composed by Johann Sebastian Bach"* drawn from the cantatas, passions, motets and the Christmas
Oratorio; (2) the digitization method; (3) *"a comparative study of automatic figured bass annotations
of BCFB, using both rule-based and machine learning approaches"*; (4) applications of figured bass
annotation, *"especially in connection with converting figured bass to chord labels"*.

**[FACT, §1]** The state of the field as the authors found it: two earlier papers on automatic figured
bass, both rule-based — Barthélemy and Bonardi, who *"treated figured bass as a harmonic reduction and
devised rules to identify and remove ornamental notes, permitting them to cluster the remaining chord
tones as figures"*, and Wead and Knopke, who *"manually designed a decision tree to determine the
figured bass for a given bass line"* — with *"no open-source code and a lack of quantitative results"*.
*"we are not aware of any previous applications of machine learning to figured bass, nor of any existing
digital dataset with figured bass annotations"* (640).

### The dataset (§2, 641–642)

**[FACT, §2]** 139 four-voice chorales *"that include his own figured bass, based on the Neue Bach
Ausgabe (NBA) critical edition"*, encoded in MusicXML, \*\*kern and MEI. A reference table of all 420
chorales attributed to Bach was cross-referenced with the NBA to find the 139 (§2.1).

**[FACT, §2.2]** 109 of the 139 came from existing \*\*kern encodings in the KernScores repository,
converted to MusicXML with music21 (v. 5.1.0) and corrected to match the NBA; the remaining 30 were
entered by hand. MusicXML is the master format; editing in MuseScore 3. Changes to match the NBA
included *"adding a continuo line and/or instrumental voices; transposing; changing the meter, pitch,
and duration of certain notes; etc."* (footnote 5).

**[FACT, §2.3]** Conversion to the other formats: MusicXML to \*\*kern with *musicxml2hum*, *"except for
the continuation lines"*; \*\*kern to MEI with Verovio. Direct MusicXML-to-MEI conversion lost
accidentals, slashes and continuation lines, so continuation lines were added to the \*\*kern files by
hand before converting to MEI (641–642).

### The task and the evaluation metric (§3, 642–643)

**[FACT, §3, footnote 12]** *"The generated FBAs use flats and sharps to respectively indicate lowered
and raised intervals, and do not contain continuation lines."* (FBA is the paper's abbreviation for
figured bass annotation.)

**[FACT, §3.1]** 120 of the 139 chorales were used to train and test. Excluded: 12 chorales with
*"elaborate instrumental interludes between phrases"*, five *"that are barely figured"*, and BWV 8.06 and
BWV 161.06 *"because they feature irregular textures, such as having an obligato continuo and/or
instrumental part"* (642).

**★ [FACT, §3.2.1] The unit of analysis is the note-onset slice.** *"First, the music is segmented into
a series of note onset slices [8,9]. A new slice is formed whenever a new note onset occurs in any musical
voice, and each slice consists of the vertical set of notes sounding at that moment."* A note held from
an earlier slice belongs to the later slice's sounding set (the 3.3.2 example marks notes as "held").
The paper's *sonority* is *"the set of pitch classes present in a note onset slice"* (footnote 19).

**[FACT, §3.2.1]** The simple rule-based algorithm labels every interval above the bass. Its exact match
with Bach's figures: *"the percentage of exact matches was only 3%"* — *"partly because Bach did not
explicitly label all the intervals above the bass in his FBAs"* (642).

**[FACT, §3.2.2]** The evaluation metric treats musically equivalent figures as equivalent. The rules,
*"inspired by Arnold [11]"*:
- a "3" can be omitted *"unless there is a 4th in the sonority, or unless the 3rd is the resolution of a
  4–3 suspension"*;
- a "5" can be omitted unless there is a 6th in the sonority, the 5th resolves a 6–5 suspension, or the
  5th has an accidental;
- an "8" can be omitted unless there is a 9th in the sonority, the 8th resolves a 9–8 suspension, or the
  8th has an accidental;
- a "6" can be omitted *"if the sonority forms a "6/4/3" or a "6/4/2" chord"* (642).

**[FACT, §3.2.3]** Under that metric the simple algorithm agrees with Bach's figures at **64.5%** (643).

**[FACT, §3.2.3]** The improved rule-based algorithm adds two rules: (1) omit the figure for an
upper-voice note if *"the note is labelled in the previous slice"* and *"the pitch class of the bass in
the current slice remains the same as in the previous slice"*; (2) on fractional beats, look for
*"ornamental notes, such as passing tones, neighbour tones, escape tones, and anticipations, which are
all approached or departed by step. If such a note is in an upper voice, its corresponding number is
removed from the figure; if such a note is in the bass, the slice is left entirely unfigured"* (643).
With these, **85.3%** agreement (643).

**★ [FACT, footnote 20] The rules were chosen on the data they are graded on.** *"The rules were
proposed by observing the generated FBAs and were evaluated against the ground truth FBAs from BCFB. We
selected the rules that yielded higher accuracy."* No held-out split is stated for the rule-based
results in the pages as read. *(This bears on guiding principle #20, fit/evaluation separation: the
85.3% is a figure the rules were selected against. The machine-learning figures below are
cross-validated.)*

**[FACT, §3.2.3]** The authors stopped adding rules: *"none were readily obvious from the perspective of
music theory or performance practice, and we wanted to avoid overfitting our rules"* (643).

### The machine-learning method (§3.3, 643–644)

**[FACT, §3.3.1]** Each figure is converted to a 12-element interval-class vector *"that includes all
the notes above the bass that are sounding in the current slice"*. The interval class is ORDERED, from
the bass to the upper voice, ranging 0 to 11 (footnote 21). Where a figure does not specify the exact
interval (a "6" could be major or minor), *"we rely on the score to determine the exact interval using
heuristics-based post-processing"*; the score's pitch spelling is likewise used to convert vectors back
to figures (e.g. 3 semitones as "♭3" or "♯2"; "2" versus "9" decided by whether the note is an octave or
more above the bass, footnote 22).

**[FACT, §3.3.2]** Input per slice: three binary vectors — interval classes (12), onsets (12: which notes
above the bass have onsets in this slice rather than being held), metrical context (3: downbeat, another
beat, or a fractional beat) — 27 dimensions; with the previous and following slices concatenated
(zero-padded at the ends), 81 dimensions (644).

**[FACT, §3.3.3]** Decision trees (scikit-learn `DecisionTreeClassifier`, default settings, *"an
optimized version of CART"*, footnote 24) and a feedforward network of three hidden layers of 300 units,
Adam, binary cross-entropy, hyper-parameters tuned on the validation set (footnote 25). Output: a
12-dimensional binary vector of the semitones above the bass that are figured (644).

**[FACT, §3.3.4]** Ten-fold cross-validation. Network: 80% training, 10% validation (also used for early
stopping, footnote 27), 10% test. Trees: 90% training, 10% test, *"matching the DNN test sets"* (644).
**What a fold is cut by — chorale or slice — is not stated in the pages as read.**

**[FACT, §3.3.5]** *"The Decision Trees and Deep Neural Networks respectively achieved classification
accuracies of 84.3±0.5% and 85.9±0.6% on BCFB."* The ± is *"standard error across cross-validation
folds"* (footnote 28). The accuracies are *"calculated based on the evaluation metrics proposed in
Section 3.2.2"* (644).

**What the accuracy counts is not defined in the pages as read** — per slice is the natural reading of
a per-slice classifier, but no sentence states the unit. *(CONJECTURE, not carried.)*

### The discussion (§4, 644–645)

**[FACT, §4]** One common error: missing *"figures that indicate the resolution of a suspension, such as
the 9–8 shown in Fig. 4(a), m. 8.4. This may be because the features we used did not contain sufficient
voice-leading information to detect such suspensions."*

**[FACT, §4]** Two disagreements the authors judge *"theoretically acceptable"*: a generated "♯" at BWV
145.05 m. 2.3 where Bach wrote none (the D is sharpened in the soprano), and a generated "♯7" at m. 3.2
(644).

**[FACT, §4]** Bach's own inconsistency, three kinds: accidentals (the first "♯" unlabelled at m. 2.3, the
second labelled at m. 3.3), suspensions (*"sometimes labelled … and sometimes omitted them"*), and the
same chord labelled sometimes 4/2 and sometimes 6/4/2. *"So, one cannot expect 100% agreement to be
achievable, given such variability. Bach, like everyone, was sometimes inconsistent with himself, which
imposes an artificial performance ceiling on our models [12]."* (644)

**[FACT, Fig. 4 caption, 645]** The best-performing model's figures are produced by predicting interval
classes and generating the figure *"based on the intervals between the bass note and each predicted
interval class"*.

### The conclusion (§5, 645)

**[FACT, §5]** *"our models achieved classification accuracies of 85.3% and 85.9% on BCFB,
respectively. A potential reason the machine learning models did not outperform the rule-based model may
be the relatively small size of BCFB."*

**★ [FACT, §5] The direction the authors propose for harmonic analysis.** Existing methods *"tend to
either identify chords directly from the music [13–15], or identify and remove non-chord tones from the
score and then generate chord labels from the remaining chord tones [16,17]. A new approach would be to
first generate figured bass automatically from the music and then convert the figures to chord labels;
this would allow a chord classifier to take advantage of knowledge implicitly learned from Bach's ground
truth FBAs by a figured bass annotator during its training."* **[CONJECTURE — the authors' proposal; no
such system is built or measured in the paper.]**

**[FACT, §5]** Named refinements: add voice-leading information; improve the rule-based model by
analysing the trained decision trees; add figured bass from other Bach works and other Baroque composers.

## Measured results, as the paper states them

| Method | Metric | Value | Where |
|---|---|---|---|
| Simple rule-based (every interval above the bass) | exact match with Bach's figures | **3%** | §3.2.1, 642 |
| Simple rule-based | equivalence metric of §3.2.2 | **64.5%** | §3.2.3, 643 |
| Improved rule-based (two added rules; rules selected on BCFB itself, footnote 20) | equivalence metric | **85.3%** | §3.2.3, 643; §5 |
| Decision trees, ten-fold cross-validation | equivalence metric | **84.3 ± 0.5%** (standard error across folds) | §3.3.5, 644 |
| Feedforward network, ten-fold cross-validation | equivalence metric | **85.9 ± 0.6%** | §3.3.5, 644 |

Corpus for all rows: BCFB, 120 of its 139 chorales (§3.1). Ground truth: Bach's own figures as printed in
the NBA.

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score of **four-voice, largely homorhythmic
chorales** with **separated voices and an identified bass** (rule (1) and the ornamental-note rule both
need to know which voice a note is in and whether it moves by step); **note-onset slices** with each
note marked as struck or held (§3.3.2); **metrical position** at three levels — downbeat, other beat,
fractional beat; and the score's **pitch spelling**, used to turn interval classes back into figures with
the right accidentals and the right number (§3.3.1). It assumes **no key, no chord, no root and no
segmentation into chords**. Everything it reads is in the notated score.

**What it HANDS downstream.** For each note-onset slice, a **set of intervals above the bass** — the
predicted interval classes — rendered as figures with flats and sharps for lowered and raised intervals
and **no continuation lines** (footnote 12). A slice can be left unfigured. It hands on **no chord, no
root, no quality, no key and no inversion as a label**; the figures are intervals above the bass, and
the figure follows what Bach wrote, which includes suspension figures (4–3, 9–8) and omits ornamental
notes.

**Its own STATED SCOPE and limits.** Bach's four-voice chorales with Bach's own figures; 120 chorales
after exclusions; the authors name the dataset's small size as a possible reason the machine-learning
models did not beat the rules (§5), name missing voice-leading features as the likely cause of missed
suspension figures (§4), and state that Bach's own inconsistency sets an artificial ceiling (§4).

## What an L3 detail specification could adopt, adapt, or must argue against

*(The L3 charter, `FRAMEWORK.md` §5 "L3 — The read-off facts": L3 answers "given a settled tonal reading,
what else does a harmonic analysis of this music say?", consumes L2's published facts plus L0's and L1's,
may not revise L2, and publishes, among other facts, "the figured bass".)*

- **Adopt — the equivalence rules of §3.2.2 as the grading rule for any figured bass L3 publishes.** They
  are stated, sourced to Arnold, and they move the simple algorithm from a 3% exact match to 64.5%. A
  measurement of L3's figured bass against Bach's figures would need them or rules doing the same work.
- **Adopt — the unit: a figure is the set of intervals above the bass in one slice, with the score's
  spelling deciding the number and accidental.** That is what a figured bass is in this ground truth.
- **Must argue against, or at least answer — the placement.** The paper produces figured bass **from the
  notes alone, with no chord and no key**, and its §5 proposes the reverse of L3's order: figured bass
  first, chord labels from it. Under consequence (i) of `reading_pass/candidacy_upgrades.md`'s criterion,
  a method the chosen placement excludes is a candidate and the specification must carry the exclusion.
  The L3 charter places figured bass after the settled tonal reading. The paper does not measure a
  chord-based alternative, so it neither supports nor contradicts that placement; it is the
  **rival-shaped** upstream route, and the L3 specification owes a sentence saying why it is not taken.
- **Adapt — what a figured bass read off settled chords would miss.** Bach's figures often carry
  suspension figures (the paper's examples are 4–3 and 9–8; the equivalence rules also name 6–5), though
  he *"sometimes omitted them"* (§4); and the authors' rule (2) removes ornamental notes from the figure
  to come closer to his figures. A figured bass computed only from a decided chord and its inversion would
  not produce the suspension figures. **This side's reading: L3's figured bass would need L2's published
  elaboration relations (which notes are suspensions, passing tones and so on) as well as the chord**, if
  it is meant to agree with this ground truth. Whether L2 publishes enough for that is a question for the
  L3 derivation, not answered here.

## ★ Findings, routed and not applied

**(1) A statement in `FRAMEWORK.md` pairs this paper's figures wrongly.** `FRAMEWORK.md` Appendix B, §S2
(the first-stage draft, kept whole and unedited), says: *"a rule-based labeller matches his figures
exactly 3% of the time and 85.3% under a music-theoretic equivalence metric — the gap is notation
convention, not analysis."* At the paper: the **3%** is the **simple** rule-based algorithm's exact match
(642); the same simple algorithm under the equivalence metric scores **64.5%** (643); the **85.3%** is
the **improved** algorithm, after two added rules, one of which removes passing tones, neighbour tones,
escape tones and anticipations (643). So the 3%-to-85.3% gap is **not** one labeller under two metrics,
and part of it comes from an analytical step (finding ornamental notes), not from notation convention.
The paper does not say "the gap is notation convention". **Each number is printed in the paper; the
pairing and the conclusion drawn from it are not.** *Where it sits:* Appendix B is the sealed first-stage
draft, and the main body's R-1 cites figured bass only as a source of an agreement figure, which stands.
This side found no CHOSEN design point whose defense rests on the sentence, from the searched lines only
(a search of `FRAMEWORK.md` for "figured bass" and its variants); it has not established that none does.
**Routed to the user as a finding of its own; nothing is amended.**

**(2) The 85.3% is a figure the rules were selected against** (footnote 20). Any later use of it as a
measured accuracy carries that qualification (principle #20). The cross-validated figures are 84.3% and
85.9%.

**(3) BCFB is a figured-bass ground truth on Bach chorales.** Routed to measurement design and to the
corpus needs list. **Not checked:** whether BCFB is held in this repository, and which of its chorales
overlap the regression corpus. If they overlap, `D-514` (an annotation set whose works overlap the
regression corpus is record-only without a user ruling) would apply; this side has not established the
overlap.

**(4) The paper's slice is not this project's slice.** The paper cuts a new slice at every note
**onset** only (§3.2.1); this project's slice (`DECISIONS.md` terms table) begins when any note starts
**or stops**. Recorded for any L3 derivation that would compare against BCFB slice by slice.

**(5) No falsifier.** Nothing read contradicts any CHOSEN design point. The paper's upstream route is
rival-shaped against the L3 placement, as stated above, and measures nothing against it. **No STOP
fires** under the commission's §6 on this paper's content; finding (1) is a wrong citation in the
framework's sealed appendix, put to the user on its own.

## Centrality

**CENTRAL** — L3 publishes the figured bass, this is the one producer of it in the read set (the row's
recorded reason), and its claims would carry load in the L3 detail specification: the grading rule, the
unit, and the upstream route the specification must answer. **A second independent extraction is owed**
under the commission's §4 and is a separate later act; it has not been performed.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity. It does not
check whether BCFB is held in this repository, and it does not follow the paper's links.

## The read-back, recorded

After the sections above were written, the text was read back against the page images, and swept for
absolutes (only, never, every, all, none, whole, complete and the like), each hit read at its line.
**Changed at that check:** the adapt bullet said Bach's figures "carry" suspension figures and "drop"
ornamental notes — the page says he sometimes omitted suspension figures, and the ornamental-note
removal is the authors' rule, not a statement about Bach; it now says so. The adopt bullet said a
measurement "needs" the equivalence rules; now "would need", with the 3% to 64.5% figures beside it. One
sentence called the method a reader of "notes only" while it also reads metrical position and spelling;
now "everything it reads is in the notated score". The independence note's "read FRAMEWORK.md nowhere"
became "had not opened".

---

*Provenance: written 2026-10-14 by the Cowork session that booted on
`records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_four.md` and performed the
ordinary session-start read. The paper was read at the object as page images, pp. 640–646. No shell
command was run in the container or on the device; the container copy used for writing this file is
declared. Every value above is the paper's own (#17f, D-431).*
