# SECOND INDEPENDENT EXTRACTION — row 37 — Bigo, Feisthauer, Giraud & Levé, *Relevance of Musical Features for Cadence Detection* (ISMIR 2018)

> **STATUS: a Cowork reading, 2026-09-20. Nothing in this file is ruled.** It is the second,
> independent extraction the reading-pass commission asks for on a source the first pass graded
> CENTRAL (`cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, as quoted in handoff
> entry 169 §3; the commission itself was not opened in this sitting). Its §0–§8 were written
> **before the first extract was opened**; §9 came after and changed nothing in §0–§8; **§10 is a
> user-ordered check that did correct §0–§9**, each correction at its site with the former wording kept
> or recorded in §10. The first extract is
> `reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md`;
> this file takes the same name under `reading_pass/extracts_second_pass/` by Ruling 2 of handoff
> entry 186.
>
> **This file is paper-facing only.** It says what the pages carry. What the repository's record says
> about this paper, and whether the paper is central to anything, is the first extract's half and is
> not judged here.

## §0 — Declarations: what this reader knew, and how the read was run

**The object.** `docs/research_papers/bigo_feisthauer_giraud_leve_2018_ismir_cadence_detection_features.pdf`,
587,805 bytes at the staging result (device modification time 1784448962776). **7 PDF pages**, the
tool's own number, obtained by a deliberately out-of-range request (page 40) before any page was read.

**Read whole, at the page images, in one request** (PDF pages 1–7), then PDF page 5 (Table 2) again
alone, which came back at the same size. This reader looked at the page images themselves and not only
at the call's success line: all seven carry print and were legible at the size delivered, with a bound
for the small type of Table 2 (§2).

**The independence bound — what this reader had seen before the paper, declared and not claimed away.**

- Handoff entries 211, 210, 209, 186 and 169 whole; entry 206 at §3; entry 200 at §1–§5; entry 198 at
  §7; entry 188 at §4–§5; entry 152 at (v)–(x); entry 118 at its bridge-fault section. At what was read
  of them, this row is named as owed and as next after row 7; **none of them, at what was read, says
  anything of this paper's content.**
- **That a second extraction is owed at all tells this reader the first pass graded the paper
  CENTRAL.**
- `reading_pass/candidacy_upgrades.md` at its lines 225–245 only, read directly, and **not below line
  245**, on entry 206's warning. **What those lines carried of this row:** line 242, the table row —
  *"Bigo, Feisthauer, Giraud & Levé 2018, relevance of musical features for cadence detection"*, *"AT
  THE OBJECT, whole, pp. 355–361"*, the first extract's path, *"CENTRAL"*, *"OWED"*; and line 226,
  which names rows 37 and 38 as *"the two halves of the cadence-cue evidence behind DP-I's split"*.
  **So this reader came to the paper knowing that the record reads it as cadence-cue evidence behind a
  split it calls DP-I** (what DP-I is was not looked up). The extraction below covers the paper whole;
  the reader's attention on the features themselves cannot be shown to have been unsteered by that
  line.
- **Ruling 2's name-only look-up was satisfied from the table cell at line 242.** Separately, and
  before this row was established at the table, `reading_pass/extracts/` was listed to verify row 7's
  first extract at entry 211 §1's figures; **that listing also showed this row's first-extract file name
  and its size, 12,399 bytes**, and the names and sizes of the other files in that folder. The first
  extract was not opened before §0–§8 of this file had landed. *(★ CORRECTED AT THE USER-ORDERED CHECK,
  §10. FORMER WORDING, PRESERVED (#12): "before this row was chosen … and the names of every other first
  extract. The first extract was not opened before §0–§7 of this file stood." — the row had been named by
  entry 211 before the listing; the listing showed files, not a set of extracts known to be complete; and
  the banner's bound is §0–§8.)*
- `docs/research_papers/` was listed (names only, no subfolder opened) to find the held file.
- **Row 7's second extract** (another paper, Temperley & Sleator 1999) at its heading list and its
  lines 1–104, for the form. Nothing in those lines speaks of this paper.
- **`DECISIONS.md` whole, as the session-start read.** Its index titles include decisions on cadence
  detection: D-081 and D-336 (the cadence detector is key-agnostic; it votes for the key), D-462
  (cadence validation scoped to location; type only partially attributable) and D-584 (the
  perfect/imperfect call made on the bass-derived inversion, the soprano arrival degree demoted). This
  reader saw those titles before reading the paper; none names this paper, and whether any rests on
  it was not looked up.
- `FRAMEWORK.md`, the slice derivation, the progress record, the findings surface and
  `docs/research_papers/BIBLIOGRAPHY.md` were **not** opened by this reader.
- **This reader is a language model; what it may hold of the paper from training cannot be inspected
  from inside the session and is declared as a bound.** The statements below were written from the
  page images in view, with their locators.

**No web access and no subagent. ONE SHELL COMMAND was run in the container, after §0–§7 and the
read-back and sweep were done: `true`, a slip; it read nothing and wrote nothing, and nothing in this
file rests on it. None was run on the device.** *(★ CORRECTED BEFORE LANDING. FORMER WORDING, PRESERVED
(#12): "No web access, no subagent, and no shell command in the container or on the device." — true
when written, false before the file landed.)* Counts, sums,
ratios and recomputations below that are this reader's and not the paper's are marked **DERIVED**.

## §1 — Identity, at the first page (PDF page 1)

The page prints the title *"RELEVANCE OF MUSICAL FEATURES FOR CADENCE DETECTION"*; the authors *"Louis
Bigo¹ Laurent Feisthauer¹ Mathieu Giraud¹ Florence Levé²·¹"*; affiliations *"¹ CRIStAL, UMR 9189, CNRS,
Université de Lille, France"* and *"² MIS, Université de Picardie Jules Verne, Amiens, France"*; and an
e-mail line at *algomus.fr*. The licence box at the foot of the left column gives *"Creative Commons
Attribution 4.0 International License (CC BY 4.0)"* and the citation *"19th International Society for
Music Information Retrieval Conference, Paris, France, 2018."* The running head on pp. 356–361 reads
*"Proceedings of the 19th ISMIR Conference, Paris, France, September 23-27, 2018"*. Printed page
numbers run 355 to 361.

Against the candidacy table's *"Bigo, Feisthauer, Giraud & Levé 2018"* and *"pp. 355–361"* ✓. The
bibliography was not opened, so no check against it is claimed. **No identity finding.**

## §2 — The document, and how to cite a place in it

Seven PDF pages; PDF page *k* is printed page *k* + 354. Locators below are printed page numbers.

Section headings, in order, as printed: *Abstract* 355; *1. Introduction* 355 — *1.1 Cadences* 355,
*1.2 Cadences, Musicology and MIR* 355, *1.3 Contents* 356; *2. Musical Features at Three Onsets* 356 —
*2.1 Features on the Arrival Point Z or around it* 356, *2.2 Rhythmic Features around the Arrival Point
Z* 357, *2.3 Features on the Point Y or around it* 357, *2.4 Features on the Cadence Preparation (Point
X)* 358; *3. Classification Process* 358; *4. Experiments and Discussion* 358 — *4.1 Corpora and
Implementations* 358, *4.2 Discussion on Feature Statistics* 358, *4.3 Learning Process* 360, *4.4
Discussion on Detection Results* 360; *5. Conclusion* 360; *Acknowledgements* 361; *6. References* 361
(25 numbered references).

Four figures, each a score excerpt with X, Y, Z marked above and Roman numerals below: 1 Haydn op. 17/4,
iv, PAC at measure 8 (356); 2 Haydn op. 17/5, i, HC at measure 8 (356); 3 Bach, fugue #15 in G major
BWV 860, PAC at measure 83 (357); 4 Haydn op. 55/3, i, potential PACs at m67 and m71 (360). Four
tables: 1 the corpora (358); 2 feature tallies (359); 3 detection on the test sets (360); 4 F1 by
feature set (360).

**Bound on Table 2.** Each cell prints a count followed by a small expected count; significance is
marked by bold with an asterisk (presence) or italic (absence). The small figures and the asterisks
were read at the page image as delivered (the file tool returned the page at this size alone too; a larger rendering would need a shell
renderer, which this sitting's rules bar, and none was sought). Every
Table 2 value in §5.3 is AS READ at that size. Where an italic cell shows no asterisk as rendered, that
is recorded as seen (§7), not corrected. Tables 1, 3 and 4 are in ordinary type and were read without
difficulty. The score excerpts in the figures were not transcribed; their captions were read.

## §3 — Coupling facts: what the paper assumes upstream, what it hands downstream, its stated scope

**Stated aim and stance (356, §1.3).** *"Our goal is to identify binary, musical, and local features
that coincide with cadences and that can be used to train a model that detects new cadences, either
PAC/rIAC or HC. Rather than agnostically discovering cadential features on the musical surface, we
intend here to confirm and study traditional music theory knowledge regarding cadences."* And: *"The
proposed strategy avoids chord segmentation, which is itself a difficult MIR problem."*

**What it assumes upstream.**

- **The unit of decision is the beat.** *"Each beat Z of the score is considered as the potential
  arrival point of a cadence"* (356, §2); in §3, *"Assuming that the arrival points of cadences do not
  fall between beats, each beat (quarter note, or three eights depending on the time signature) of
  each piece is described by"* a boolean vector and a boolean class (358).
- **No harmony analysis, no chord segmentation, no key estimation.** *"We therefore do not start from
  a complete harmony analysis nor a chord segmentation, that can be error-prone"* (356, §2). *"We do
  not perform tonality estimation [13, 23] because of the usual difficulty of algorithms to
  disambiguate adjacent tonalities in the circle of fifths"* (357, §2.1).
- **Intervals are taken relative to a bass.** Footnote 1 (356): *"Pitches in underlined figures (i.e.
  1, 3, etc.) are here computed by the interval modulo octave relative to the bass. As some chords are
  not in root position, these pitches may differ from the actual function."* For the voice-leading
  features the bass meant is Z's: *"the interval being still relative to the bass of Z"* (357, §2.1).
  For the Y features the page does not repeat which bass; *Y-has-7*'s gloss *"the leading tone"* (357)
  reads naturally only against Z's bass — **this reader's inference, not printed.**
- **Voice-separated input for some features.** *"Pieces were downloaded as voice-separated .krn files
  from kern.ccarh.org [11]. Note that the features proposed here could also apply to non-separated
  files, except for after-Z-rest-\* and Y-Z-bass-same-voice. In this case, features on voice leading
  would only check that the coming note or the suspended note is found at the right place in the
  polyphonic texture"* (358, §4.1).
- **Tooling.** Features extracted with code based on music21 [6]; classifiers computed with
  scikit-learn [8]; Fisher tests with scipy (358–359).
- **Ground truth is two prior human annotations**: the Bach corpus's cadence annotations *"were taken
  from our previous work [9]"*; the Haydn corpus is *"annotated with cadences by Sears and colleagues
  [22]"* (358, §4.1). The page says of them: *"Even if these annotated corpora model cadences in the
  light of a global analysis of the form, we have used them as a benchmark on our local feature-based
  detection"* (358). No agreement measure between annotators was met in the pages as read.
- **Music-theory categories are taken as given** (355, §1.1): PAC, IAC, rIAC, HC, DC, the evaded
  cadence, and the plagal progression, with the ordering *"The strongest cadence is the PAC, followed
  in turn by the rIAC, IAC, HC, and the DC and related cadences [20]"*.

**What it hands downstream.** For each beat, a boolean decision from a trained classifier: cadence of
the target type ending here, or not (358, §3). Per-feature tallies with significance marks (Table 2).
**No harmonic label, no key, no chord, no confidence value** is described as an output on the pages as
read.

**Its stated scope.**

- Cadence types detected: PAC (both corpora), PAC+rIAC (Bach), HC (Haydn); rIAC in Haydn (8) and HC in
  Bach (5) appear in Table 1 only in parentheses. Table 1's caption: *"We narrow to sets with
  significant number of cadences (PAC and HC for the Haydn corpus, PAC and PAC+rIAC for the Bach
  corpus)"* (358). That the parentheses mark the classes left out is **this reader's reading** of the
  caption; for the PAC column the parenthesised figure is headed *"(final)"*.
- Repertoire: the 24 fugues of WTC I; 42 Haydn string-quartet expositions (358, Table 1 and §4.1).
- Features are *local*: *"the surroundings of the cadential beat including its immediate past,
  presumably corresponding to the preparation of the cadence"* (356, §2).

## §4 — The method, as the paper states it

### §4.1 The three onsets (356–358)

*"What we propose here is a simple heuristic focusing on three specific onsets: Z, Y(Z) and X(Z), or
for short Z, Y, and X. Most of the features describe sets of notes sounding at these onsets (even when
they begin before), namely chord(Z), chord(Y), and chord(X)"* (356, §2). *"Even when the methods
finding Y(Z) and X(Z) return approximate onsets, the computed features may be relevant"* (356).

- **Z** — every beat, as the candidate arrival point (356).
- **Y** (357, §2.3): *"We thus propose to identify the point Y as the latest beat preceding Z for which
  the bass voice includes a sounding note, limited to one measure in the past. If the bass includes a
  rest just before Z, we look just before."* The page adds that the span of a cadential preparation
  depends on harmonic rhythm and style, so *"The beat resolution to search the Y point should therefore
  depend on the corpus."* In §4.1 (358): *"Points Y and X are searched at a beat resolution of a
  quarter note (Haydn) or eight note (Bach, see Figure 3)."* Figure 3's caption: *"To cope with the
  faster harmonic rhythm, every eighth before Z is considered as a potential Y"* (357).
- **X** (358, §2.4): *"the latest beat before Y whose lowest sounding note has a different pitch
  (modulo octave) than the lowest note of Y."*
- The idea stated for the targets: *"to try and detect SD-V-I progressions for a PAC/rIAC, and
  progressions ending with V for an HC"* (356).
- Figure 1's caption records the heuristic's limit in its own words: *"the heuristic choice of a single
  offset Y implies here that the features Y-in-V7-3 and Y-has-7 are not true, even if the dominant
  chord actually contain several pitches 3 and 7 (circled notes). Nevertheless, these pitches are caught
  by the tonality features ... and some of them are considered by the voice leading features"* (356).

### §4.2 The 44 features (356–358; listed in Table 2)

The abstract says *"44 cadential features"* and §2 *"A set of 44 binary features is computed at each
beat"* (355, 356). **DERIVED: Table 2 lists 44 rows** — 8 rhythmic, 21 at Z, 12 at Y, 3 at X — which
agrees.

**Rhythmic, around Z (357, §2.2)** — *"These textural features intend to detect either breaks or
continuation in music."*
- *R-Z-strong-beat*: *"Z is a strong beat (beat 1 and 3 for 4/4, and beat 1 for other time
  signatures)"*.
- *R-Z-same-rhythm-1* (resp. *-2*): *"There is exactly the same sequence of durations in the one (resp.
  the two) beat(s) preceding Z than on the one (resp. the two) beat(s) at onset Z"*.
- *R-Z-sustained-note*: *"At least one note sounding at Z started before Z"*.
- *R-after-Z-rest-highest*, *-lowest*, *-middle*: *"There is a rest in some voice right after the note
  at onset Z"*.
- *R-after-Z-one-voice-ends*: *"Z is the last onset in at least one voice (end of the piece)"*.

**At Z — the chord (356–357, §2.1).**
- *Z-in-perfect-major-triad* (resp. *Z-in-perfect-triad*): chord(Z) included in {1, 3M, 5} (resp.
  {1, 3m, 3M, 5}).
- *Z-in-perfect-triad-or-sus4*: chord(Z) included in {1, 3, 4, 5}.
- *Z-is-sus4*: chord(Z) is exactly {1, 4, 5}.
- *Z-highest-is-1* (resp. *Z-highest-is-3*): the highest note of chord(Z) is the tonic 1 (resp. the
  major or minor third 3), *"as expected for a PAC (rIAC)"*.

**At Z — voice leading (357, §2.1).** *"Z-β-comes-from-α means that the note β in chord(Z) is an
'immediate resolution' of a note α (the interval being still relative to the bass of Z) that is
exactly before β (even if this note is not at the onset Y that will be defined later)."* Example:
*Z-3-comes-from-4*, *"a 3 in chord(Z) that is an immediate resolution of a 4 (dominant seventh in the
case of a PAC, see ② on Figure 1)"*. *(★ CORRECTED AT THE USER-ORDERED CHECK, §10. FORMER WORDING,
PRESERVED (#12): "a 3 in chord(Z) that is an immediate resolution of a 4 (dominant seventh in the case of
a PAC)" — the parenthesis on the page (357) continues "see ② on Figure 1".)* Symmetric suspension features *Z-α-moves-to-β*, e.g. *Z-4-moves-to-3*: *"there is a
suspended fourth 4 in chord(Z) that is immediately resolved to the third 3"*. Table 2 lists eight
*comes-from* features (1←7, 1←1, 1←2, 3←4, 4←5, 5←5, 5←6, 6←7) and four *moves-to* features (2→1, 4→3,
6→5, 7→1).

**At Z — tonality by the bass (357, §2.1)**, without key estimation:
- *Z-bass-compatible-with-I* (resp. *-with-V*): *"Both notes 4 and 7 of the tonality that would be
  implied if the bass of Z is I (resp. V) are present in the four beats before Z"*.
- *Z-bass-compatible-with-I-scale*: *"The 8 previous beats exhibits the whole scale of the same implied
  tonality"*, with the note that Temperley suggests such PACs with SD before V–I feel more conclusive
  [24].
- The page's own caveat: these *"may be triggered by other events close on the circle of fifths: Both
  Z-bass-compatible-with-I and -with-I-scale may be triggered by a previous V/V (as on Figure 2) or, in
  minor, when Z is actually a III in root position"* (357).

**At Y (357–358, §2.3).**
- *Y-Z-offsets-at-most-1*: *"Y is at most one quarter note before Z"*.
- *Y-has-7* (resp. *Y-has-9*): *"chord(Y) contains 7 (resp. 9), that is the leading tone (resp. the
  dominant seventh or the dominant ninth) in the case of a candidate PAC"*.
- *Y-in-V7*: chord(Y) is included within a dominant seventh chord; *Y-in-V7-3*: included within a
  dominant seventh chord and contains a third.
- *Y'-Y-bass-moves-8ve*: *"The bass note preceding Y is at the same pitch but with an octave jump
  (expected on some V or V64 chords)"*.
- *Y'-Y-bass-moves-chromatic*: *"The bass note preceding Y is at a distance of one semitone (HC)"*
  (358).
- *Y-Z-bass-moves-2nd-min* (resp. *-2nd-Maj*); *Y-Z-bass-same-voice* (*"Bass notes of both chords are
  on the same voice"*); *Y-Z-bass-moves-compatible-V-I* (resp. *-I-V*): *"The bass moves by an
  ascending fourth or descending fifth (PAC) (resp. ascending fifth or descending fourth, HC I-V)"*
  (358).

**At X (358, §2.4)**, bass move X→Y: *X-Y-bass-moves-2nd-min* (V/V–V–I), *X-Y-bass-moves-2nd-Maj* (IV–V–I
or II6–V–I), *X-Y-bass-moves-4th* (expected in II–V–I).

### §4.3 The classification (358, §3; 360, §4.3)

- Each beat → a vector of booleans (the features) and a boolean class (*"whether the beat is annotated
  in the reference as a PAC/rIAC/HC or not"*). *"This way of representing data enables us to
  reformulate cadence detection as a classification task."*
- *"To avoid overfitting, each dataset is randomly divided into two subsets: a training set used to
  train a classifier and a test set left to evaluate the classifier performance at the end."* **The
  split proportion is not stated on the pages as read.** DERIVED from Table 3: the test sets hold 3583
  of Haydn's 7173 beats and 2357 of Bach's 4739 (about half of each), labelled *"(21 quatuors)"* and
  *"(12 fugues)"*.
- Hyper-parameters: *"The classifier and the value of its hyper-parameters have been selected by
  performing Leave-One-Piece-Out cross-validation over the training set."* The reason given against
  beat-level leave-one-out: *"leaving only one beat of one piece out of the training set would result
  here in overfitting due to intra-piece musical repetitions."* **Which hyper-parameters, and their
  chosen values, are not stated.**
- *"A linear Support Vector Machine (SVM) classifier was trained on each training set ... splitting the
  feature space with a hyperplane [5]. As datasets are unbalanced (about 98% of the beats are
  'non-cadential'), we assigned stronger weights to data belonging to the under-represented class,
  here the cadential beats."* **The weights are not stated.**
- *"Other classifying algorithms such as k-nearest-neighbor or decision trees were tested and turned out
  to provide comparable or inferior results"* — no figures for them.
- **One split per corpus is reported**; no repetition over splits, no seed, and no uncertainty on any
  figure of Tables 3 or 4 is given on the pages as read.

### §4.4 The feature statistics (359, Table 2 caption)

The table shows, per feature, *"the number of beats where this feature occurs (all beats, cadential
points or not), followed by its number of occurrences on beats labeled as cadences in the reference
annotation, and, as in small, its expected number should the feature be random and uniformly
distributed across the beats. (· means 0, and not significant)."* *"For each feature and each cadence
type, p-values are estimated by an exact Fisher test computed by the Python scipy package. Fisher tests
are computed independently. To account for the large number of tests, only features with p-values under
.001 (bold, \*) can be considered as significant, either by their absence (italic) or their
presence."*

## §5 — Results, as the paper states them, and what this reader derived from them

### §5.1 Table 1 — the corpora (358)

| corpus | description | pieces | voices | beats | PAC (final) | rIAC | HC |
|---|---|---|---|---|---|---|---|
| haydn-quartets | Haydn string quartets [22] | 42 expositions | 4 | 7173 | 99 (21) | (8) | 70 |
| bach-wtc-i | Bach fugues [9] | 24 fugues | 2 to 5 | 4739 | 63 (23) | 24 | (5) |

Caption: *"Corpora with manual annotations of cadences. Cadences are labeled at about 2% of the
beats."* §4.1: *"Only a minority of annotated PAC are final in the sense that they are included in the
last four measures of the piece (or of the exposition)."*

**DERIVED.** PAC 99 + 63 = **162** and HC **70** — the abstract's *"totaling 162 perfect authentic
cadences and 70 half cadences"* ✓. Share of beats labelled with any of the three types: Haydn (99 + 8 +
70) / 7173 = 2.5 %; Bach (63 + 24 + 5) / 4739 = 1.9 % — consistent with *"about 2%"*. Final PACs 21 of
99 and 23 of 63 — consistent with *"a minority"*.

### §5.2 Table 3 — detection on the test sets, all features (360)

| corpus | type | beats | ref | TP | FP | FN | F1 |
|---|---|---|---|---|---|---|---|
| haydn-quartets (21 quatuors) | PAC | 3583 | 51 | 42 | 28 | 9 | 0.69 |
| | HC | 3583 | 32 | 18 | 73 | 14 | 0.29 |
| bach-wtc-i (12 fugues) | PAC | 2357 | 36 | 26 | 3 | 10 | 0.80 |
| | PAC+rIAC | 2357 | 46 | 30 | 12 | 16 | 0.68 |

Caption: *"Number of beats annotated in the reference annotation (ref), true positives (TP), false
positives (FP), false negatives (FN), and F1 measure (harmonic mean of the recall and the precision)."*

**DERIVED — each row re-computed from its own counts.** TP + FN = ref in all four rows ✓. Recall /
precision / F1: Haydn PAC 42/51 = 0.824, 42/70 = 0.600, F1 0.694 ✓; Haydn HC 18/32 = 0.563, 18/91 =
0.198, F1 0.293 ✓; Bach PAC 26/36 = 0.722, 26/29 = 0.897, F1 0.800 ✓; Bach PAC+rIAC 30/46 = 0.652,
30/42 = 0.714, F1 0.682 ✓. False positives as a share of the test beats: Haydn PAC 28/3583 = 0.78 %;
Bach PAC 3/2357 = 0.13 %; Haydn HC 73/3583 = 2.04 %.

**The paper's statements against those counts.**
- Abstract (355): *"In these corpora, the classifier correctly identified more than 75% of perfect
  authentic cadences and 50% of half cadences, with low false positive rates."* §4.4 (360): *"The detection of PAC is
  good, with more than 75% PAC detected and a low false positive rate (< 1%)."* **DERIVED: the PAC
  recall is 82.4 % on the Haydn test set and 72.2 % on the Bach test set; pooled over both, 68/87 =
  78.2 %.** So *"more than 75%"* holds for Haydn and for the pooled count, and **not for the Bach test
  set on its own**; the page does not say which reading it means. *"< 1%"* holds for both PAC rows.
- §4.4: *"Half of them are detected, with about 2% FP"* (HC) — 56 % recall, 2.0 % ✓.
- §4.4: *"Adding rIAC (Bach corpus) lowers the results"* — F1 0.80 → 0.68 ✓.
- §4.4: *"we previously reported 82% of PAC detection in fugues [9] but with manual hard-coded rules
  that may have resulted in overfitting"* — a figure from another paper, not checkable here.

### §5.3 Table 2 — feature tallies (359), AS READ under §2's bound

Cells: count / expected; **b** = bold with asterisk (significant presence), *i\** = italic with
asterisk (significant absence), *i* = italic with no asterisk visible as rendered; · = 0.

| Feature | Bach beats | Bach PAC | Bach rIAC | Haydn beats | Haydn PAC | Haydn HC |
|---|---|---|---|---|---|---|
| R-Z-strong-beat | 1920 | 60/25 b | 24/9 b | 3126 | 98/43 b | 70/30 b |
| R-Z-same-rhythm-1 | 394 | 1/5 | ·/1 | 1254 | 2/17 *i\** | 2/12 *i\** |
| R-Z-same-rhythm-2 | 176 | ·/2 | ·/0 | 448 | 0/6 *i* | 1/4 |
| R-Z-sustained-note | 2341 | 14/31 *i\** | 5/11 *i* | 2521 | 1/34 *i\** | 8/24 *i\** |
| R-after-Z-rest-highest | 166 | 14/2 b | 1/0 | 501 | 56/6 b | 10/4 |
| R-after-Z-rest-middle | 477 | 22/6 b | 9/2 b | 1227 | 72/16 b | 35/11 b |
| R-after-Z-rest-lowest | 194 | 15/2 b | 13/0 b | 1130 | 59/15 b | 34/11 b |
| R-after-Z-one-voice-ends | 180 | 19/2 b | 2/0 | · | ·/0 | ·/0 |
| Z-in-perfect-major-triad | 1167 | 43/15 b | 12/5 | 2760 | 94/38 b | 53/26 b |
| Z-in-perfect-triad | 1819 | 56/24 b | 19/9 b | 3256 | 97/44 b | 53/31 b |
| Z-in-perfect-triad-or-sus4 | 2078 | 62/27 b | 20/10 b | 3434 | 97/47 b | 55/33 b |
| Z-is-sus4 | 680 | 20/9 b | 1/3 | 1308 | 14/18 | 4/12 *i* |
| Z-highest-is-1 | 592 | 55/7 b | 1/2 | 1765 | 96/24 b | 19/17 |
| Z-highest-is-3 | 1488 | 1/19 *i\** | 21/7 b | 1596 | 1/22 *i\** | 28/15 b |
| Z-bass-compatible-with-I | 1724 | 63/22 b | 23/8 b | 2279 | 98/31 b | 56/22 b |
| Z-bass-compatible-with-V | 1265 | 8/16 *i* | 4/6 | 1616 | 3/22 *i\** | 44/15 b |
| Z-bass-compatible-with-I-scale | 1902 | 63/25 b | 22/9 b | 2104 | 91/29 b | 46/20 b |
| Z-1-comes-from-7 | 663 | 52/8 b | 15/3 b | 1016 | 89/14 b | 30/9 b |
| Z-1-comes-from-1 | 180 | 13/2 b | 1/0 | 828 | 9/11 | 0/8 *i\** |
| Z-1-comes-from-2 | 523 | 23/6 b | 7/2 | 893 | 65/12 b | 27/8 b |
| Z-3-comes-from-4 | 1078 | 25/14 | 16/5 b | 1488 | 72/20 b | 45/14 b |
| Z-4-comes-from-5 | 197 | 4/2 | ·/0 | 291 | ·/4 | 9/2 |
| Z-5-comes-from-5 | 153 | 9/2 b | ·/0 | 769 | 2/10 *i* | 13/7 |
| Z-5-comes-from-6 | 510 | 1/6 | 2/2 | 495 | 0/6 *i* | 9/4 |
| Z-6-comes-from-7 | 200 | ·/2 | ·/1 | 130 | ·/1 | ·/1 |
| Z-2-moves-to-1 | 57 | ·/0 | ·/0 | 90 | 2/1 | 1/0 |
| Z-4-moves-to-3 | 160 | 2/2 | 1/0 | 340 | 2/4 | 11/3 b |
| Z-6-moves-to-5 | 138 | 1/1 | ·/0 | 180 | ·/2 | 8/1 b |
| Z-7-moves-to-1 | 7 | ·/0 | ·/0 | 105 | 2/1 | 1/1 |
| Y-in-V7 | 1267 | 52/16 b | 17/6 b | 3290 | 81/45 b | 15/32 *i\** |
| Y-in-V7-3 | 721 | 44/9 b | 14/3 b | 2413 | 69/33 b | 14/23 |
| Y-has-7 | 554 | 22/7 b | 7/2 | 767 | 66/10 b | 8/7 |
| Y-has-9 | 607 | 1/8 *i* | 4/3 | 486 | 2/6 | 5/4 |
| Y-Z-offsets-at-most-1 | 4525 | 63/60 | 24/22 | 5668 | 90/78 | 66/55 b |
| Y-Z-bass-same-voice | 4270 | 63/56 | 24/21 | 5297 | 98/73 b | 70/51 b |
| Y-Z-bass-moves-2nd-min | 1313 | 0/17 *i\** | 0/6 *i\** | 1328 | 1/18 *i\** | 35/12 b |
| Y-Z-bass-moves-2nd-Maj | 880 | 0/11 *i\** | ·/4 | 559 | 0/7 *i\** | 28/5 b |
| Y-Z-bass-moves-compatible-I-V | 125 | 1/1 | ·/0 | 448 | 2/6 | 6/4 |
| Y-Z-bass-moves-compatible-V-I | 512 | 62/6 b | 23/2 b | 578 | 95/7 b | 6/5 |
| Y'-Y-bass-moves-chromatic | 1139 | 6/15 *i* | 2/5 | 2050 | 10/28 *i\** | 33/20 |
| Y'-Y-bass-moves-8ve | 193 | 29/2 b | 7/0 b | 522 | 22/7 b | 6/5 |
| X-Y-bass-moves-2nd-min | 433 | 2/5 | 1/2 | 1060 | 10/14 | 10/10 |
| X-Y-bass-moves-2nd-Maj | 568 | 25/7 b | 12/2 b | 803 | 65/11 b | 5/7 |
| X-Y-bass-moves-4th | 670 | 11/8 | 4/3 | 1626 | 4/22 *i\** | 9/15 |
| **Total** | 4739 | 63 | 24 | 7173 | 99 | 70 |

The caption's worked example: *"There are 70 HC out of 7173 beats in the Haydn quartets corpus. There
are 35 beats corresponding to a HC with the feature Y-Z-bass-2nd-min, out of 1328 beats with this
feature, and compared to only 12 beats should this feature be random"* — the row as read gives 1328 and
35/12 ✓. And: *"the feature Y-Z-bass-2nd-min is significantly absent in PACs of both corpora (p <
10⁻⁷) and significantly present in HCs of the Haydn corpus (p < 10⁻⁸)"* — as read, 0/17 and 1/18 italic
with asterisk, 35/12 bold ✓. (On the name, §7.)

**DERIVED — the expected counts.** For the caption's example, 1328 × 70 / 7173 = 12.96, printed 12;
for R-Z-strong-beat in Haydn PAC, 3126 × 99 / 7173 = 43.1, printed 43. Whether the printed expected
counts are truncated or rounded is not stated; the first cell (12.96 printed 12) fits truncation,
which is this reader's inference from that one cell and was not checked across the table.

**The paper's statements about Table 2, against it (358, §4.2).**
- *"Unsurprisingly, features R-Z-strong-beat, Y-Z-bass-moves-compatible-V-I, Z-perfect-triad-or-sus4
  and Z-highest-note-is-1 are activated nearly for every PAC."* As read: 60/63 and 98/99; 62/63 and
  95/99; 62/63 and 97/99; 55/63 and 96/99. **DERIVED: 55/63 = 87 % for Z-highest-is-1 in Bach**, the
  lowest of the eight. (On the two names, §7.)
- *"Note that PAC lacking the fifth leap are the ones where the bass passes by another note before
  tonic resolution."* No count stands beside this sentence on the page.
- *"R-Z-sustained-note is absent in nearly all PACs in the Haydn corpus, whereas it can be found in
  some PACs in Bach fugues due to the contrapuntal writing"* — 1/34 and 14/31, both italic with
  asterisk as read, that is, significantly absent in both corpora.
- *"We were expecting to find more suspensions for both PAC and HC as a way to retain tension before
  the ultimate resolution but they do not appear significantly in these corpora."* As read, of the
  *moves-to* features only Z-4-moves-to-3 (11/3) and Z-6-moves-to-5 (8/1) carry bold, both in Haydn
  HC; Z-is-sus4 carries bold in Bach PAC (20/9). **The sentence does not match those three cells
  as read**; it may mean suspensions are not significant in the sense the authors intended, which the
  page does not spell out.
- *"We also notably lack strong significant features for HC. Indeed, the Y-Z bass move in a HC is
  variable (it is typically similar to X-Y moves in PAC)."*

### §5.4 Table 4 — F1 by feature set (360)

| features | Haydn PAC | Haydn HC | Bach PAC | Bach PAC+rIAC |
|---|---|---|---|---|
| All features XYZR | 0.69 | 0.29 | 0.80 | 0.68 |
| Features YZR | 0.69 | 0.27 | 0.71 | 0.68 |
| Features ZR | 0.59 | 0.24 | 0.52 | 0.34 |
| Features XYZ | 0.72 | 0.25 | 0.74 | 0.54 |

Caption: *"F1 measure while detecting cadences on the test sets of both corpora with different sets of
features."*

**The paper's statements about Table 4, against it (360, §4.4).**
- *"Some features in Z already consider the past. Nevertheless, the features around Y are essential to
  improve the overall detection."* ZR → YZR: 0.59 → 0.69, 0.24 → 0.27, 0.52 → 0.71, 0.34 → 0.68 ✓.
- *"Features on X bring a small but significant gain for PAC."* YZR → XYZR: **Haydn PAC 0.69 → 0.69, no
  change; Bach PAC 0.71 → 0.80.** The gain is in the Bach corpus only; and no test of significance on
  Table 4 is reported on the pages as read, so *"significant"* has no stated measurement behind it.
- *"Rhythmic features (R) bring an improvement especially for HC, in particular with R-Z-strong-beat
  that correctly filters out more than half of the beats."* XYZ → XYZR: Haydn HC 0.25 → 0.29 (+0.04);
  **Haydn PAC 0.72 → 0.69 (a fall)**; Bach PAC 0.74 → 0.80 (+0.06); Bach PAC+rIAC 0.54 → 0.68 (+0.14).
  **DERIVED: the largest gain from R is on Bach PAC+rIAC, not on HC, and R lowers Haydn PAC.** On
  *"more than half of the beats"*: R-Z-strong-beat is absent on 4739 − 1920 = 2819 of Bach's beats (59
  %) and 7173 − 3126 = 4047 of Haydn's (56 %) ✓ (reading *"filters out"* as the beats where the feature
  is false — this reader's reading).
- All Table 4 differences are single-split F1 values with no uncertainty stated (§4.3).

### §5.5 Figures used as evidence

- **Figure 4 (360)**, Haydn op. 55/3, i: *"The PAC at m67 is hard to detect with the silence at the
  bass. In their global analysis of the form, Sears et. al see the end of the secondary theme (called
  the EEC, for Essential Expositional Closure by [10]) at m67 and discard any further PAC in the
  following concluding section [22]: The PAC candidate at m71, found by the proposed strategy, is thus
  counted here as a FP. It could be debated whether the EEC is indeed at m67 ... or rather at m71."*
- §4.4: *"An inspection of the 28 PAC reported as FP in the Haydn corpus shows that at least 5 FP can be
  seen as actual cadences, for example measure 71 in Haydn op. 55/3, i, shown on Figure 4."* *(★
  CORRECTED AT THE USER-ORDERED CHECK, §10: the quotation formerly closed after "op. 55/3, i", mid-sentence,
  with no gap mark.)* And *"Other notable sources of
  FP are tonic chords following actual HC cadences activating significant features for PAC."* The other
  four are not named. **DERIVED, only as a bound the authors' sentence implies:** if those 5 were
  counted as true positives, Haydn PAC precision would rise from 42/70 to 47/70; the reference count
  would also change, which the page does not give, so no re-computed F1 is offered.
- *"The same Figure 4 shows an example of FN, where a silence in the bass makes the computation of many
  features fail"* (m67).
- *"The detection of HC is difficult (Haydn corpus), as there is not a single feature applicable to
  every case."* Table 2 as read: the highest HC count is 70/70 for R-Z-strong-beat and for
  Y-Z-bass-same-voice. **This reader's reading of that sentence**: *applicable* means *discriminating*,
  since two features are present at every HC — the page does not say.

## §6 — The claims, labeled

**FACT — stated or measured on the pages.**
1. A linear SVM on 44 binary per-beat features, trained on one random split per corpus with class
   weighting, gives on the test sets the counts and F1 values of Table 3 (360).
2. The F1 values of Table 4 for four feature sets (360).
3. The per-feature tallies of Table 2 with Fisher-test significance at p < .001 (359).
4. The corpora: 24 WTC I fugues with the authors' own annotations [9]; 42 Haydn quartet expositions
   with Sears and colleagues' annotations [22]; the counts of Table 1 (358).
5. k-NN and decision trees *"comparable or inferior"* — stated, with no figures (360).
6. At least 5 of the 28 Haydn PAC false positives *"can be seen as actual cadences"* — stated as the
   outcome of an inspection, with one example (360). The criterion of the inspection was not met in the
   pages as read.

**THEORY — taken from published music theory, with the page's citation.**
7. The cadence typology and its ordering by strength [20]; Blombach's definition [3]; Caplin on the
   plagal progression [4]; Schmalfeldt on the evaded cadence [19]; Hepokoski & Darcy's EEC [10];
   Temperley on SD before V–I [24] (355–357, 360).
8. The features as encodings of that theory: leading tone to tonic, seventh to third, the V–I bass
   leap, suspensions, the melodic arrival on 1 or 3 (356–358). The stance is stated: *"to confirm and
   study traditional music theory knowledge"* (356).

**CONJECTURE — the authors' interpretations, marked as such by their own wording or by the absence of
a measurement.**
9. *"that may have resulted in overfitting"* — of their earlier 82% [9] (360).
10. *"there may be too few such cadences to efficiently build the model"* — of rIAC (360).
11. That features at X give a *"significant"* gain for PAC, and that R helps *"especially"* HC (360) —
    stated as findings; §5.4 shows Table 4 bearing the X gain on Bach PAC only (none on Haydn PAC), no
    significance test on Table 4 met in the pages as read, and R's largest gain on Bach PAC+rIAC rather
    than on HC.
12. *"The experiment results are consistent with common knowledge that classification is more complex
    for half cadences than for authentic cadences"* (355).
13. Perspectives (360, §5): features *"not necessarily theory driven"* with metric values; automatic
    selection; comparing the X and Y heuristics with others; *"spans"* of onsets rather than single
    onsets, *"in order to improve the harmony relevance of the model"*. Stated as future work.

## §7 — Residues: print defects, and things this reader derived

**Print residues, as seen.**
- **One feature carries two names on the pages.** Table 2 prints *Y-Z-bass-moves-2nd-min*; its caption,
  twice, prints *Y-Z-bass-2nd-min* (359).
- **Two more names in §4.2 differ from Table 2**: *"Z-perfect-triad-or-sus4"* against the table's
  *Z-in-perfect-triad-or-sus4*, and *"Z-highest-note-is-1"* against *Z-highest-is-1* (358). The meaning
  is clear from context; the names are not the table's.
- **Italic cells with no asterisk visible, as rendered.** Under the caption's rule italic marks
  significant absence and goes with bold-asterisk p < .001; the cells 0/6 and 2/10 and 0/6 (Haydn PAC:
  R-Z-same-rhythm-2, Z-5-comes-from-5, Z-5-comes-from-6), 5/11 (Bach rIAC, R-Z-sustained-note), 8/16,
  1/8 and 6/15 (Bach PAC: Z-bass-compatible-with-V, Y-has-9, Y'-Y-bass-moves-chromatic) and 4/12 (Haydn
  HC, Z-is-sus4) show italic with no asterisk as read. **The page does not say what italic without an
  asterisk means**; subject to §2's rendering bound.
- *"(21 quatuors)"* labels Table 3's Haydn test set (360), where the corpus unit is *"42 expositions"*
  (358). 21 is half of 42; *quatuors* is the French word for quartets. Whether the test set is 21
  expositions is **this reader's reading**, not printed.
- *"eight note"* for *eighth note* (358, §4.1); *"Each cadence type provide"* (355); *"the dominant
  chord actually contain"* (356, Figure 1 caption); *"Sears et. al"* (360, Figure 4 caption); *"The 8
  previous beats exhibits"* (357). None changes a meaning.

**Unstated on the pages as read — gaps, not defects of the paper's reasoning.**
- The train/test split proportion, the random seed, the hyper-parameters tuned and their values, and
  the class weights (358, 360).
- Any variance or uncertainty on Tables 3 and 4; one split per corpus is reported.
- Whether the Haydn HC and Bach PAC+rIAC classifiers share a split with the PAC classifiers of the same
  corpus — Table 3 gives the same beat count per corpus (3583; 2357), which fits one split per corpus;
  **this reader's inference.**
- Which bass the Y features' intervals are taken against (§3).
- How the Haydn ground truth, built *"in the light of a global analysis of the form"* (358), bears on
  what a local detector can reach — the page raises it (Figure 4) and does not measure it.

**DERIVED values carried above, collected.** 44 features in Table 2 (§4.2); 162 PAC and 70 HC (§5.1);
labelled shares 2.5 % and 1.9 % (§5.1); test-set shares of about half (§4.3); the four Table 3 rows
re-computed, all ✓ (§5.2); **PAC recall 82.4 % Haydn, 72.2 % Bach, 78.2 % pooled against the stated
"more than 75%"** (§5.2); FP shares 0.78 %, 0.13 %, 2.04 % (§5.2); expected counts 12.96 and 43.1
(§5.3); 55/63 = 87 % (§5.3); **Table 4: X gives no change on Haydn PAC; R's largest gain is on Bach
PAC+rIAC and R lowers Haydn PAC** (§5.4); strong-beat absent on 59 % and 56 % of beats (§5.4).

## §8 — Closing: what the read-back and the sweep found, written after §0–§7 stood

**The read-back.** §0–§7 were read back against the page images, which were still in view, clause by
clause for every quotation and every value outside Table 2. **It found three defects, corrected before
landing:**
- a quotation that carried a *"resp."* the page does not print (§4.2, *Z-highest-is-1*: the page says
  *"as expected for a PAC (rIAC)"*);
- the abstract's sentence quoted without its opening *"In these corpora,"*, which bears on how the
  *"more than 75%"* claim is read (§5.2);
- a sentence on Table 2's expected counts that said nothing (§5.3), replaced with the one inference
  the cell supports and its bound.

Table 2 was not re-transcribed at the read-back. Its values stand as read once, under §2's bound.

**The sweep for absolutes** (a search for *all, every, none, never, only, no, nothing, always, whole,
complete, exhaustive, nowhere, independent*, each hit read at its line) **found three more, narrowed
before landing:** a claim that no larger rendering of Table 2 was *available*, where one was only
barred by this sitting's rules; and two negatives about the paper stated without the bound *"in the
pages as read"*, on the annotators' agreement (§3) and on the fifth-leap sentence (§5.3).

**One slip of this reader's, after the sweep:** a shell command, `true`, in the container. It read
nothing and wrote nothing. §0 is corrected at its site with the former wording kept.

**What this file does NOT do.** It does not open the first extract (that is the cross-check, after
landing). It does not re-read Table 2 at any larger size. It judges nothing about the record's use of
the paper.

## §9 — The cross-check against the first extract, run after §0–§8 had landed

### §9.1 What the comparison reached

The first extract (12,399 bytes at its staging result, modification time 1788187991388, last content line 192) was
read whole once, after this file landed at 41,143 bytes. Each of its paper-facing statements —
identity, quotations, values, method, coupling facts — was set against this file and, wherever the two
differ, against the page image, which was still in view. Its record-facing half (its *Why this paper*
note, findings (1) to (4) as they bear on the record, its adopt/adapt verdicts as they bear on the L1
charter, its centrality verdict) was read but is **outside this comparison**, as this file's banner
says.

### §9.2 Where the two reads agree

**Every value both reads transcribed agrees at each place compared:** Table 1 (every cell the first
extract carries), Table 3 (all four rows, every count and F1), Table 4 (all sixteen values), *"about
2%"*, *"about 98%"*, *"44"*, *"82%"*, *"< 1%"*, *"about 2% FP"*, *"at least 5"* of *"28"*. The two reads
also agree on the definitions of Y and X, the leave-one-piece-out reason, the class weighting, the
voice-separation caveat, and that the method assumes no key, no chord segmentation and no harmonic
analysis. The first extract did not transcribe Table 2, so no comparison ran there.

### §9.3 Departures that touch no value, finding or verdict — resolved at the page, and corrected in the first extract under the standing rule of handoff entry 198 §7

- **(a)** Its §4.4 quotation read *"with manual hand-coded rules but that may have resulted in
  overfitting"*; the page (360) prints *"[9] but with manual hard-coded rules that may have resulted
  in overfitting"*. **The page goes against the first extract.**
- **(b)** Its coupling fact on what the method hands downstream named the trained types *"(PAC, rIAC
  or HC)"*; the page trains PAC and PAC+rIAC (Bach) and PAC and HC (Haydn) — Table 1's caption (358)
  and Table 3 (360). **The page goes against the first extract.**
- **(c)** Its stated-scope paragraph paraphrased the suspension sentence as *"Suspensions were
  expected to be significant"*; the page (358) says *"We were expecting to find more suspensions"*.
  **The page goes against the paraphrase**; the quoted tail was right.

Each is corrected at its site in the first extract with a "★ CORRECTED 2026-09-20" note and the former
wording kept; a banner note records the rule. **No value, finding or verdict changed.**

**One small difference was left as it is:** the first extract's §2.1
tonality quotation opens *"we do not perform"* in lower case and marks the dropped citation *"[13, 23]"*
with an ellipsis, which is marked and changes nothing.

### §9.4 Two places inside or beside a finding or a verdict — NOT corrected; they stand with the user

Under the user's ruling of 2026-09-19 (handoff entry 200 §1 item 2), a word the page does not print
that stands inside or beside a finding still goes to the user.

- **(A) The quotation beside finding (2) and the "Adopt — the bass-implied-tonality construction"
  verdict.** The first extract quotes §2.1 as *"Both notes 4 and 7 of the tonality that would be implied
  by the bass of Z are present in the four beats before Z."* **The page (357) prints *"Both notes 4 and 7
  of the tonality that would be implied if the bass of Z is I (resp. V) are present in the four beats
  before Z"*.** The dropped condition is what separates the two features: for *-with-I* the implied
  tonality is the one whose tonic is Z's bass; for *-with-V*, the one whose dominant is Z's bass (the
  latter this reader's reading of *"resp. V"*). Finding (2) applies the quotation to *-with-I* only, and
  for that feature its reading matches the page. **This reader's judgment, which no record read
  settles: the correction would restore the quotation and move neither the finding nor the verdict.**
- **(B) The FACT-labelled gloss beside the "Adapt — the metric-strength cue as a filter" verdict.** The
  first extract writes *"**[FACT, §4.4]** Rhythmic features matter most where the harmony is weakest:"*
  before the authors' sentence *"Rhythmic features (R) bring an improvement especially for HC ..."*. **The
  page does not print the gloss**, and Table 4 as read (§5.4) gives R's largest gain on Bach PAC+rIAC
  (0.54 → 0.68), a smaller gain on Haydn HC (0.25 → 0.29), and a fall on Haydn PAC (0.72 → 0.69). The
  verdict itself rests on the quoted *"filters out more than half of the beats"*, which the page
  prints and Table 2 bears (§5.4). **This reader's judgment: the gloss is an inference standing as the
  paper's, and so is the authors' own *"especially for HC"* as against their Table 4; correcting the
  gloss would not move the verdict.**

*(★ RULED 2026-09-20, the user's words: "decision: 1 for both." Both places were then corrected in the
first extract at their sites, former wording preserved (#12), with a banner note recording the ruling.
At (B) the unprinted sentence is replaced by the authors' words and Table 4's four XYZ → XYZR values. This
section's heading, "NOT corrected; they stand with the user", is made stale by that act and left standing,
#12.)*

### §9.5 What this read carries that the first extract does not

- Table 2 whole, under §2's rendering bound (§5.3), with the eight italic cells that show no asterisk
  as rendered (§7).
- **The per-corpus reading of *"more than 75%"*:** PAC recall 82.4 % on Haydn, **72.2 % on Bach**,
  78.2 % pooled (§5.2); the abstract opens *"In these corpora,"*.
- **Table 4 against the authors' sentences:** X gives no change on Haydn PAC; R lowers Haydn PAC; R's
  largest gain is on Bach PAC+rIAC (§5.4).
- The suspension sentence against the three bold cells (§5.3); the feature-name mismatches, *"(21
  quatuors)"* and the other print residues (§7); what the pages leave unstated (split proportion, seed,
  hyper-parameters, weights, uncertainty) (§4.3, §7).
- **One observation on the record-facing half, reported and not judged:** the first extract's finding
  (1) verifies a charter phrase, *"hand-designed local features reach F .80 on perfect authentic
  cadences"*, at Table 3's Bach PAC row (0.80). **The same table gives 0.69 for Haydn PAC.** The charter
  was not opened by this reader, so whether its sentence names the corpus is not known here.

### §9.6 What the cross-check did not do

It did not re-open any page beyond what stayed in view from the read; did not re-read Table 2; did not
open the charter, `FRAMEWORK.md` or any record the first extract cites; and does not claim the
comparison found every difference — it ran over what both extracts carry. **The first extract's
Centrality sentence *"has not been performed"* is now stale** and is left standing for the progress
update.

## §10 — The user-ordered check, 2026-09-20, written in the act that ran it

On the user's instruction, this file was re-read whole as landed (47,638 bytes) and checked for
completeness, coherence, correctness, and misuse of absolutes and superlatives, each claim against the
object it rests on: the page images still in view, and the other files named. **It found defects, all
corrected, each at its site with the former wording kept where the site carried a quotation or a
declaration:**
- **a quotation closed early** — §4.2's *Z-3-comes-from-4* parenthesis, which on the page continues
  *"see ② on Figure 1"*. §8's read-back did not catch it;
- **a quotation stopped mid-sentence with no gap mark** (§5.5);
- in §0, **"before this row was chosen"**, where the row had been named by entry 211 before the listing;
  **"every other first extract"**, wider than a listing of files; and **"§0–§7"** where the banner's
  bound is §0–§8;
- **a negative about the paper without its bound** (§6 item 6);
- **a vague phrase, "the wider readings"** (§6 item 11), now stated as the three things §5.4 shows.

The §9.4 ruling note and this banner line were added in the same act.

**What the check confirmed at its objects, not struck:** §5.2's recomputations; the 44-row count; the
162/70 sums; the eight italic cells listed in §7; §9.2's list of agreeing values against the first
extract. **What it did NOT do:** re-read Table 2 at a larger size, re-transcribe it, or re-open the
pages beyond what stayed in view. **Nothing here says a further pass would come back empty.**
