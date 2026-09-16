# Second extraction — Chen & Su, "Functional Harmony Recognition of Symbolic Music Data with Multi-Task Recurrent Neural Networks"

> **What this file is.** The SECOND independent extraction of row 46 of the L2 slice of Task B, written
> under `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, as the hundred-and-sixty-ninth
> handoff entry's §3 records the eight steps. **That commission was NOT opened by this side**; the
> rule's wording is taken from the hundred-and-sixty-ninth entry's quotation of it, so this file's
> compliance with the commission's form is a RELAY, declared here and not claimed.
>
> **Nothing in this file is ruled.** It records what one read of the paper found. It proposes no
> amendment to any governing document, moves no verdict and applies nothing.
>
> **Written 2026-09-16** by the Cowork side, booted from the hundred-and-eighty-fourth handoff entry.
> The paper was read from `docs/research_papers/chen_su_2018_ismir_bpsfh_functional_harmony.pdf`,
> **671,916 bytes at this sitting's own staging call.**
>
> **Section form.** The section headings follow row 52's second extract, read at its HEADINGS ALONE by
> a heading search; no content line of that file was read.

---

## §0 — What was read, and the bound on this read's independence

### What was read for this extract

- **The paper, all eight PDF pages**, in two requests (pages 1–4 and 5–8), every image checked present
  and legible at the image. **The page count was established at the tool** by a deliberately
  out-of-range request for page 99, which answered *"Requested page 99 is outside the document (PDF
  has 8 pages)"*. The paper's printed page numbers run **90 to 97**; this file cites the PRINTED page
  number and gives the PDF page beside it where the two could be confused.
- **Further openings, named at their own sections:** all eight pages again at the read-back, after §0
  to §7 were first written (§8.1); printed pages 92, 93 and 95 singly, and row 46's first extract whole,
  at the cross-check after §0 to §8 had landed (§9.1). *(★ POINTER ADDED AT THE USER-ORDERED CHECK, the
  handoff entry's §6; no wording struck.)*

### What was NOT read, and is therefore not behind anything in this file

- **Row 46's first extract** — not opened before this file's §0 to §8 were written and landed (step 7
  of the procedure).
- `reading_pass/candidacy_upgrades.md`, `reading_pass/l2_slice_reading_progress.md`,
  `docs/research_papers/BIBLIOGRAPHY.md`, `FRAMEWORK.md`, `population.md`, the findings surface, both
  commissions, and every other extract's content.
- **No web access of any kind.** The dataset and code repository the paper announces were not visited.
- **No sweep of this repository** for the paper's authors, title, dataset name or values. **This file
  therefore asserts nothing about what this project's record says of the paper.**

### The contamination that is real, stated exactly rather than claimed away

Before the paper was opened, this side had read one line describing row 46, in the
hundred-and-eighty-fourth handoff entry's §1 table: *"Chen & Su, ISMIR 2018, functional harmony
recognition (**BPS-FH**)"*, with the held file's name and size and the first extract's name and size.
That line names the subject and the dataset and **states no conclusion about the paper**. This side
also read, in that entry and in the hundred-and-sixty-ninth, general procedural lessons from earlier
members (empty table cells transcribed by pattern; shortened reference lists labelled transcribed;
page-count agreement by construction). **Those lessons shaped how this side looked, not what it
concluded.** The progress table, whose verdict cells state each first extract's conclusion, was not
opened at all.

### The independence bound, stated plainly

This read is independent of row 46's first extract up to the point in §9 where that file is opened.
It is NOT independent of the procedural lessons named above, and it cannot establish from the inside
that nothing else reached it (principle #18's clause on conditions of a session: declared, not
established).

---

## §1 — What the paper is, and the identity axis

### §1.1 The identity, as the document itself prints it

- **Title** (printed in capitals on page 90): *FUNCTIONAL HARMONY RECOGNITION OF SYMBOLIC MUSIC DATA
  WITH MULTI-TASK RECURRENT NEURAL NETWORKS*.
- **Authors:** Tsung-Ping Chen and Li Su, **Institute of Information Science, Academia Sinica,
  Taiwan**; the e-mail line reads `{tearfulcanon, lisu}@iis.sinica.edu.tw`.
- **Venue**, from the running header of pages 91 to 97: *Proceedings of the 19th ISMIR Conference,
  Paris, France, September 23-27, 2018*. Printed pages **90–97**.
- **Licence**, the box at the foot of page 90's left column: *"© Tsung-Ping Chen and Li Su. Licensed
  under a Creative Commons Attribution 4.0 International License (CC BY 4.0)."* followed by an
  attribution line naming the paper and *"19th International Society for Music Information Retrieval
  Conference, Paris, France, 2018."*
- **Apparatus:** three figures and three tables, numbered 1 to 3 each; **no numbered equation is met in
  the eight pages as read.** *(★ ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK, §9.4, and checked
  against this read's own openings of all eight pages.)*
- **Announced resources:** the abstract states that *"The dataset and the source code of the proposed
  system is announced at"* `https://github.com/Tsung-Ping/functional-harmony`. **Not visited.**
- **The dataset the paper introduces** is named *Beethoven Piano Sonata with Function Harmony
  (BPS-FH)* on page 91. **The word printed there is "Function", not "Functional"**; §6 on page 95
  prints the same dataset as *"Beethoven Piano Sonata with Functional Harmony dataset"*, and the title
  uses "Functional".

### §1.2 What the identity axis leaves owed

**The tie between row 46 and this file** is the hundred-and-eighty-second sitting's matching of
author, year and subject, relayed through the hundred-and-eighty-third and hundred-and-eighty-fourth.
**This side confirms it at the paper's own face**: authors Chen and Su, ISMIR 2018, functional
harmony recognition, BPS-FH — every element of the relayed description is printed on pages 90–91.
**What this side did not check** is the register row's own wording, the candidacy file not having been
opened; so the tie is confirmed from the paper's side only.

### §1.3 What the paper is about, in the paper's own frame

The paper (FACT, page 90) argues that chord recognition work has focused on chord symbols and
*"overlook[s] other essential features that matter in musical harmony"*, and it frames *functional
harmony recognition* **in an engineering sense** as the recognition of five components: **key,
primary degree, secondary degree, quality and inversion** (page 90, right column: *"Since there is no
unique and exact definition on functional harmony analysis of music, we alternatively consider the
functional harmony recognition problem as the recognition of the above-mentioned five aspects"*).
It contributes (i) the BPS-FH dataset and (ii) a bidirectional-LSTM recurrent network trained
multi-task over the five components, compared against five single-task networks.

**Footnote 2 (page 90) narrows its own term:** in the strict sense *chord function* refers to the
diatonic function (the Roman numeral and functions such as tonic, dominant and subdominant), and the
paper *"opt[s] to choose a rather loose definition by regarding key, degree, and inversion also as
some generalized 'functions' of a chord."* **So the paper's "function" is its five-component label,
which contains the Roman-numeral degree but is wider than it**, and no accuracy of a tonic / dominant
/ subdominant classification is reported in the eight pages as read.

---

## §2 — The method, as the paper states it

### §2.1 The lineage the paper places itself in (its §2, page 91)

- **Chord recognition and key detection (§2.1).** Audio: LSTM-based networks [6, 12, 30]; a word2vec
  model of *harmony tension* [26]. Symbolic: early hand-crafted rule systems for Roman-numeral
  recognition [13]; deep networks [19]; *"[15] applies deep learning to identify non-cord tones"*
  (sic, *cord*); *"[21] uses a semi-Markov conditional random field (CRF) model for symbolic-level
  chord recognition."* Key: most studies target the global key [9, 17]; local key detection [27].
- **Multi-task learning (§2.2).** Shared network, several label sets [20, 29]; in MIR [11]; chord and
  root-note recognition sharing a network [34]; the paper also names multi-chain HMMs [22] and the
  dynamic Bayesian network [24] as *"similar ideas"*.
- **Datasets (§2.3).** KSN (chord and key modulation, i.e. Roman numerals) [16]; TAVERN (Roman
  numerals) [8]; the Yale Classical Archive Corpus (local tonic label and chord) [33].

### §2.2 The dataset and its annotation (its §3 and §3.1, pages 91–92)

- **Content** (FACT, page 91): *"the symbolic musical data and functional harmony annotations of the
  1st movements of 23 of Beethoven's Piano Sonatas."* Footnote 4 lists them: **No. 1, 3, 5, 6, 8, 11,
  12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, and 32**, and adds *"And all the
  repetitions in the sonatas are unfold."* (sic). **The list has twenty-three entries**, counted at the
  footnote. The paper states *"As an ongoing work, the annotation will be extended to all the 32 piano
  sonatas."*
- **Annotator** (FACT, page 91): *"The BPS-FH dataset is annotated by an expert musicologist"* —
  **one annotator, unnamed**. No second annotation, no agreement figure and no review procedure is
  stated anywhere in the eight pages as read.
- **The four implicit steps the paper describes for the annotator's harmonic analysis** (page 91–92):
  key identification (local key; *"finding a later cadence which is in a key-steady context, and then
  analyzing chords backwards might give a solution"*); segmentation (taking *"the temporal rhythm and
  the harmonic rhythm"* into account); harmonic reduction (non-chord tones and absent harmonic tones
  named as confusions); inversion recognition (the lowest note of a segment is typically the bass,
  but *"the pedal point is one of such examples"* where it is not). Then labelling diatonic functions.
- **The paper's own statement of the ground truth's subjectivity** (page 92, left column): *"It should
  be acknowledged that harmonic analysis is inherently subjective, and the confounding effect of
  subjectivity may affect the performance of a chord recognition system in many ways [25]."* Its worked
  case: in Figure 3's excerpt *"the key modulation might occur at measure 83 as labeled, but might
  also occur at measure 84 or even 85."*

### §2.3 The label set (its §3.2, page 92, and Table 1, page 93)

Transcribed from the §3.2 bullets and Table 1:

- **Key** — the local key; Table 1: dimension **24**, *"24 major and minor keys"*.
- **Primary degree and secondary degree** — *"Primary degree indicates the position of the temporary
  tonic on the scale, while secondary degree denotes the position of the chord's root based on the
  temporary tonic; the couple of degrees is represented as secondary degree/primary degree."* For a
  diatonic chord the primary degree is always 1: *"the diatonic chord V is represented as 5/1, while
  the secondary chord V/IV is represented as 5/4."* Table 1: each dimension **21**, *"7 Roman numerals
  by 3 (neutral, ♯, ♭)"*.
- **Quality** — *"10 types of chord quality"*: major triad (M), minor triad (m), augmented triad (a),
  diminished triad (d), major seventh (M7), minor seventh (m7), dominant seventh (D7), diminished
  seventh (d7), half-diminished seventh (h7), augmented sixth (a6). Table 1: dimension **10**.
- **Inversion** — root position as 0th; 1st inversion (6 or 6/3 for a triad, 6/5 for a seventh chord);
  2nd inversion (6/4 for a triad, 4/3 for a seventh chord); 3rd inversion (4/2, seventh chords only).
  Table 1: dimension **4**, *"0th, 1st, 2nd, 3rd"*. *(The figured-bass numerals are small stacked glyphs
  in the page image; read at the image as given.)*
- **Figure 1** (page 92) shows diatonic functions in C major (I ii iii IV V vi vii°) and in C minor
  **on the harmonic minor scale** (I ii° III⁺ iv V VI vii°); its caption: *"Note that in minor key,
  the superscript ⁺ is added to the mediant because it is an augmented chord."* **The minor-key
  tonic is printed as an upper-case I over a C-minor chord** in the figure, while the §3.1 text says
  *"The capital numerals denote major chords, the lowercase numerals denote minor chords"* — see §7.1.

**Dataset totals** (FACT, page 92): *"the BPS-FH dataset contains 86,950 note events, 29 different
keys, 531 key modulations, and 7,394 chord labels."* Footnote 8 breaks the chords down: 3,438
inverted; 839 secondary; 2,951 major triads; 1,356 minor triads; 25 augmented triads; 286 diminished
triads; 30 major sevenths; 86 minor sevenths; 2,037 dominant sevenths; 453 diminished sevenths; 104
half-diminished sevenths; 66 augmented sixths.

### §2.4 The input representation (its §3.3, page 93)

- **A 61-key piano-roll, C1 to C6, middle C = C4.** Note durations *"measured in crotchet beats"*;
  **the minimal time step is a 32nd note**.
- **Out-of-range pitches:** *"All the note events out of this pitch range are transposed to fit in"*.
  **Short notes:** *"the durations of the note events whose lengths are shorter than the minimal time
  resolution are set to be the same as the time resolution."*
- **A frame** is the piano-roll at one time instance. **A segment** is the input of the LSTM cell,
  *"a segment of data with 32 frames. That is, for a musical piece with 4/4 meter, the length of a
  segment is 4 beats (or equivalently 1 bar)."* **A clip** contains 64 segments. *"The hop size for the
  neural networks is 4 frames (or half a beat.)"*

### §2.5 The networks (its §4, page 93, and Figure 2)

- **MTL-BLSTM-RNN with 1 task-specific layer** (Figure 2a): *"a simple BLSTM architecture with 1024
  hidden units"*; forward and backward outputs *"concatenated and form a 1024-by-2 matrix"*, flattened
  and connected through a fully-connected layer to *"a 80-D vector containing the classes for the five
  tasks listed in Table 1. Each class is one-hot encoding, and the Softmax function is used for the
  output vector."*
- **MTL-BLSTM-RNN with 2 task-specific layers** (Figure 2b): the same, *"but with an additional
  task-specific layer before the output layer, in order to further increase the model capacity."* The
  figure labels those layers **512, 512, 512, 256 and 128** units for key, primary degree, secondary
  degree, quality and inversion respectively.
- **STL-BLSTM-RNN** — the baseline: *"five networks in the STL-BLSTM-RNN model, each for one chord
  function recognition task respectively, and are trained individually in the experiment"*, using the
  same BLSTM.

### §2.6 Splits, augmentation and the two tasks (its §5.1, pages 93–94, and Table 2)

- **Table 2** (page 93), transcribed whole:

  | Set | Piece No. |
  |---|---|
  | Training | 1, 3, 5, 11, 16, 19 20, 22, 25, 26, 32 |
  | Validation | 6, 13, 14, 21, 23, 31 |
  | Testing | 8, 12, 18, 24, 27, 28 |

  *(The Training cell prints "19 20" with no comma between them; transcribed as printed.)*
- **Clips overlap:** *"Each clip contains 64 segments, and the overlap between two consecutive clips is
  32 segments."*
- **Augmentation:** *"To balance the data distribution among all possible keys, We perform data
  augmentation by transposing all the clips into 12 keys. As a result, there are 7,320 clips for
  training, 3,672 clips for validation, and 3,636 clips for testing."*
- **Chord symbol recognition:** 25 output classes — *"24 classes for 12 major triads and 12 minor
  triads, and an 'other' class for chords not belonging to either major triads or minor triads."*
  Tested with STL only.
- **Chord function recognition:** the five components; tested with both MTL and STL. Transcribed
  exactly: *"For the chord function recognition task with MTL scheme, the outputs of the five chord
  functions are translated to chord symbol to evaluate the performance in terms of chord symbol
  recognition. And for the chord function recognition task with STL scheme , five different networks
  are trained individually for the evaluation of chord function recognition."*

### §2.7 The training configuration (its §5.1, page 94), transcribed exactly

*"All networks are implemented with TensorFlow, and are trained using stochastic gradient descent with
the Adam optimization method. For training objective, we compute categorical cross-entropy between
targets labels and network outputs, and include a L2 regularization term. Moreover, to prevent
over-fitting and to speed up training convergence, recurrent batch normalization is applied, and the
dropout rate at the input and the output of the LSTM cell is set to be 0.5."*

**Not stated in the eight pages as read:** learning rate, batch size, number of epochs or stopping
rule, the L2 coefficient, how the five tasks' losses are combined in the MTL network (summed,
weighted, or otherwise), and how the validation set was used.

### §2.8 The evaluation metrics (its §5.2, page 95)

*"We compute the segment-level accuracy, the ratio between the number of correct detection and the
number of total segments in the testing set, for each category."* One accuracy for chord symbol
recognition; six for chord function recognition — key, degree, secondary chord, quality, inversion,
and overall. *"Note that the accuracy of secondary chord is computed when a secondary chord does
exist. The overall accuracy counts the segments in which the five chord function detections are all
correct. An extra translation accuracy is computed to examine the performance of chord function
recognition in terms of chord symbol recognition."* Table 3's caption adds: *"Degree stands for the
accuracy of correctly predicting both the primary and secondary degrees of all chords; while Secondary
indicates the accuracy of correctly predicting the degrees of secondary chords."*

---

## §3 — Coupling facts

### §3.1 What it ASSUMES about its upstream

- **An unspelled pitch input.** The piano-roll has 61 keys, one per semitone (FACT, §3.3). **A
  piano-roll carries no enharmonic spelling**, so the network cannot see whether a note is written
  D♯ or E♭ (THEORY — a property of the representation, not stated by the paper). The labels,
  however, include spelled keys and ♯/♭ degree alterations (Table 1). **The paper does not discuss
  this.**
- **A fixed 32nd-note grid in crotchet beats**, with shorter notes lengthened to one step (FACT).
  **No metre, barline, voice, staff or articulation information is in the input as described** — the
  segment is 32 frames whatever the metre, and the paper's *"1 bar"* holds only for 4/4 (FACT, as
  quoted in §2.4).
- **A pitch range C1–C6**, out-of-range notes transposed into it (FACT). *Transposed* by how many
  octaves, and whether this changes the lowest sounding note — which is what the annotation guide
  says determines inversion (§2.2) — is not stated.
- **Repeats unfolded** (FACT, footnote 4).

### §3.2 What it HANDS downstream

- **Per segment, an 80-dimensional output** over key (24), primary degree (21), secondary degree (21),
  quality (10) and inversion (4), for which *"the Softmax function is used"* (FACT, §4). **Whether one
  softmax runs over all eighty classes or one per component is not stated.** **The paper reports accuracies
  only**; it does not describe publishing or using the per-class probabilities,
  ranked alternatives, or any confidence.
- **No segmentation decision.** The prediction is segment-wise; the paper itself states that *"there
  are numbers of discontinuities in the predicted sequences"* and that *"This issue can be addressed by
  further incorporating temporal smoothing models such as the CRF [21] in the future"* (FACT, page 95).
- **No coupling constraint between the five outputs** is described: nothing in the eight pages as
  read prevents, for example, a quality and a secondary degree that no diatonic chord in the predicted
  key could carry (CONJECTURE that such incoherent tuples occur; the paper neither reports nor
  excludes them).
- **A translation to chord symbols** exists for evaluation (§2.6); its rule is not given (§7.2).
- **No chord root and no bass are among the predicted labels** — Table 1's five labels are the whole
  output. *(★ ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK, §9.4, and re-derived here at this
  file's own transcription of Table 1 and of §4's 80-D sentence.)*

### §3.3 Its own STATED scope and limits, in the paper's own words

- *"This is one attempt to challenge the end-to-end chord recognition task from the perspective of
  functional harmony"* (abstract).
- *"This work marks a preliminary step towards a holistic approach of modeling functional harmony"*
  (§6, page 95).
- The dataset is *"an ongoing work"* covering first movements of 23 sonatas (page 91).
- The definition of function is *"a rather loose definition"* (footnote 2).
- Harmonic analysis is *"inherently subjective"* (page 92).

---

## §4 — Claims, labeled

| # | Claim | Where | Label | What stands behind it in the eight pages |
|---|---|---|---|---|
| 1 | Previous chord recognition work mainly focuses on chord symbols and overlooks functional features | abstract; page 90 | THEORY (a characterisation of the literature) | citations [2, 6, 12, 18, 21, 23, 35] and others; no survey is performed |
| 2 | The paper compiles a new professionally annotated dataset | abstract; §3 | FACT (as a statement of what the authors did) | the dataset's description and totals; the files themselves not checked |
| 3 | MTL-BLSTM with one task-specific layer outperforms the single-task baseline for all chord functions | §5.3 | FACT at Table 3 | every one of the seven Chord Function columns, checked in §6.2 |
| 4 | Employing MTL instead of STL gives "a promising improvement" | abstract; §5.3; §6 | CONJECTURE as a general claim | one split, no repeated runs reported, no uncertainty; the two-layer MTL model is below STL on three of the five component columns (§6.3) |
| 5 | The degree and inversion improvements "are the most significant" | §5.3 | FACT as an ordering; unestablished as *significance* | the differences reproduce (§6.2); no statistical test or uncertainty is printed |
| 6 | Degree and inversion "benefit more from multi-task learning" because they are relatively difficult in classical music | §5.3 | CONJECTURE | offered as *"This consequence may result from"* |
| 7 | Chord function recognition "is much more challenging" than chord symbol recognition, *"partly because there are as many as 10 chord qualities for the model to predict, and partly because tonal harmony itself is complicated and equivocal"* | §5.3; §6 | FACT as an ordering of the paper's printed accuracies; CONJECTURE as to the two reasons | the two tasks use different label sets and different correctness conditions (§7.1 item 1) |
| 8 | 72.71% chord-symbol accuracy "is acceptable" against other works on classical datasets [12, 21] | §5.3 | CONJECTURE | no figure from [12] or [21] is printed, and this paper does not state which data they used (§7.1 item 6b) |
| 9 | Some "wrong" predictions in Figure 3d are correct as chord symbols, and the measure-85 prediction reflects a meaningful tonicization | §5.3 | CONJECTURE (one excerpt, the authors' reading) | Figure 3 only |
| 10 | The model "does provide more insight into the analysis of tonal structure in this excerpt, as an expert analyzer can do" | §5.3 | CONJECTURE | one excerpt |
| 11 | Harmonic analysis is inherently subjective and the subjectivity may affect a recognition system's performance | page 92 | THEORY | citation [25] |

---

## §5 — Measured results and printed values, transcribed as the paper prints them

### §5.1 Table 3, transcribed whole (page 95)

| Task | Model | Key | Degree | Secondary | Quality | Inversion | Overall | Translation |
|---|---|---|---|---|---|---|---|---|
| Chord Symbol | STL-BLSTM-RNN | – | – | – | – | – | 72.71 | - |
| Chord Function | STL-BLSTM-RNN | 67.06 | 48.31 | 9.38 | 61.87 | 57.95 | 23.57 | 56.05 |
| Chord Function | MTL-BLSTM-RNN with 1 task-specific layer | 68.48 | 50.49 | 10.96 | 62.31 | 60.04 | 25.53 | 56.91 |
| Chord Function | MTL-BLSTM-RNN with 2 task-specific layers | 66.65 | 51.79 | 3.97 | 60.59 | 59.10 | 25.69 | 56.25 |

*(The table prints "Chord Function" once, spanning its three rows; it is repeated here per row. The
Chord Symbol row's five component cells are dashes; its Translation cell is rendered as a shorter
mark than those dashes in the page image, and is transcribed as a hyphen — see §8 for how that was
checked. No cell in the table is set in bold in the page image as read.)*

Caption, transcribed: *"Table 3: Accuracy (in %) of functional harmony recognition and comparison
between multi-task BLSTM and single-task BLSTM. In the table, Degree stands for the accuracy of
correctly predicting both the primary and secondary degrees of all chords; while Secondary indicates
the accuracy of correctly predicting the degrees of secondary chords."*

### §5.2 Table 1, transcribed whole (page 93)

| Label | Dim | Content |
|---|---|---|
| Key | 24 | 24 major and minor keys |
| Pri. deg. | 21 | 7 Roman numerals by 3 (neutral, ♯, ♭) |
| Sec. deg. | 21 | 7 Roman numerals by 3 (neutral, ♯, ♭) |
| Quality | 10 | M, m, a, d, M7, m7, D7, d7, h7, a6 |
| Inversion | 4 | 0th, 1st, 2nd, 3rd |

Caption: *"Table 1: Chord function labels in the BPS-FH dataset, including key, primary degree (pri.
deg.), secondary degree (sec. deg.), chord quality, and chord inversion."*

Table 2 is transcribed at §2.6.

### §5.3 Figure 3, its annotation grid transcribed, and its caption (page 94)

**Figure 3** shows Beethoven's Piano Sonata No. 8, first movement, measures 82–89, in five panels.
Panel (b), the expert's analysis, measure by measure as printed:

| | M.82 | M.83 | M.84 (first half) | M.84 (second half) | M.85 | M.86 | M.87 | M.88 | M.89 |
|---|---|---|---|---|---|---|---|---|---|
| Chord symbol | C7 | Fm | B♭7 | Bdim7 | Cm | Fm7/A♭ | E♭/B♭ | B♭ | E♭ |
| Chord function | Fm: V⁷ | E♭: ii | V⁷ | vii°⁷/vi | vi | ii⁶₅ | I⁶₄ | V | I |

Panel (c), the same analysis as the five components:

| | M.82 | M.83 | M.84 (1st) | M.84 (2nd) | M.85 | M.86 | M.87 | M.88 | M.89 |
|---|---|---|---|---|---|---|---|---|---|
| Key | Fm | E♭ | E♭ | E♭ | E♭ | E♭ | E♭ | E♭ | E♭ |
| Sec. deg. | 5 | 2 | 5 | 7 | 6 | 2 | 1 | 5 | 1 |
| Pri. deg. | 1 | 1 | 1 | 6 | 1 | 1 | 1 | 1 | 1 |
| Quality | D7 | m | D7 | d7 | m | m7 | M | M | M |
| Inversion | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |

*(Panel (c) prints the key once per span — "Fm" over measure 82 and "Eb" over the rest — and a value
once per run of equal values; repeated here per cell. The measure-84 split is read from the panel's
cell boundaries and from panel (b)'s placing of two symbols in that measure.)*

Panel (d) is the model's output on the same grid with wrong predictions marked in red; panel (e)
translates the wrong predictions lasting at least a quarter note into chord symbols, printed as
*"C7 Fm   E♭m Ddim7/C  Cm   Fm  E♭7/G   B♭/D"*. **Panel (d)'s individual red cells are too small in
the page image to transcribe value by value, and this file does not transcribe them.**

Caption, transcribed: *"Figure 3: (a) An excerpt from the 1st movement of Beethoven's Piano Sonata No.
8, MM. 82-89. (b) The harmonic analysis of this excerpt represented in both chord symbol and chord
function. Note that the slash used in chord symbol stands for an inversion, and the note behind the
slash denotes the bass of the chord. In the analysis, this expert starts from F minor, modulates to
E♭ major at measure 83, and finally ends with an authentic cadence. (c) 5 types of annotations
representing the functions in (b). (d) The testing result of chord function recognition of the
excerpt. Wrong predictions are marked in red. (e) The translation of the result in (d) to chord
symbol. For the sake of concision, only the wrong predictions lasting at least one quarter note are
translated."*

### §5.4 The values printed in prose and in no table

- 72.71% chord-symbol accuracy; *"the best overall accuracy among all chord function recognition tasks
  is only 25.69%"*; the degree and inversion improvements *"with 2.18% and 2.09% increases in accuracy
  respectively"* (all page 95).
- The dataset totals and footnote 8's breakdown (page 92, at §2.3 above).
- The clip counts 7,320 / 3,672 / 3,636 (page 94).
- The input and network sizes: 61 keys, C1–C6, 32nd-note step, 32 frames per segment, 64 segments per
  clip, 32-segment clip overlap, hop 4 frames, 1024 hidden units, 80-D output, dropout 0.5.

---

## §6 — Arithmetic this read performed on the paper's own printed values

### §6.1 Footnote 8's quality counts sum exactly to the chord-label total

2,951 + 1,356 + 25 + 286 + 30 + 86 + 2,037 + 453 + 104 + 66 = **7,394**, the *"7,394 chord labels"*
of the main text. **The ten counts are the ten qualities of Table 1, one each**, so the breakdown is
complete and closes.

### §6.2 The one-task-specific-layer MTL model against STL, every column

Differences, MTL-1 minus STL, in percentage points: Key **+1.42**; Degree **+2.18**; Secondary
**+1.58**; Quality **+0.44**; Inversion **+2.09**; Overall **+1.96**; Translation **+0.86**. **All
seven are positive**, so *"outperforms the single-task one for all chord functions"* holds at the
printed values. **Degree and inversion are the two largest of the five component columns**, and they
are exactly the paper's *2.18%* and *2.09%* — which are percentage-point differences, not relative
increases.

### §6.3 The two-task-specific-layer MTL model against STL and against MTL-1

MTL-2 minus STL: Key **−0.41**; Degree **+3.48**; Secondary **−5.41**; Quality **−1.28**; Inversion
**+1.15**; Overall **+2.12**; Translation **+0.20**.

MTL-2 minus MTL-1: Key **−1.83**; Degree **+1.30**; Secondary **−6.99**; Quality **−1.72**; Inversion
**−0.94**; Overall **+0.16**; Translation **−0.66**.

*(★ ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK, §9.4, and re-derived here from the fourteen
differences against STL printed in §6.2 and in this section: **the largest absolute value among the fourteen differences against STL is the
Secondary column's −5.41** for the two-layer model; the next largest is that model's Degree +3.48.)*

**So the second multi-task model is below the single-task baseline on three of the five component
columns (key, secondary, quality)**, and below the first multi-task model on four of the five. The
paper's text reports the secondary-degree drop (*"adding one more task-specific layer even degrades
its performance"*) and the best overall accuracy of 25.69%, which is this model's; **it does not
mention the key, quality and inversion drops.** The abstract's claim of *"a promising improvement of
the system by employing multi-task learning instead of single-task learning"* is therefore true of
one of the two multi-task models on every column and of the other on four of the seven printed columns
(degree, inversion, overall, translation).

### §6.4 The label dimensions sum to the output size

24 + 21 + 21 + 10 + 4 = **80**, the *"80-D vector"* of §4. Closes.

### §6.5 The splits reconcile with the dataset list, and the clip counts are all multiples of twelve

- Table 2's three rows hold **11 + 6 + 6 = 23** piece numbers, and their union is **exactly** footnote
  4's list, member for member.
- 7,320 = 12 × 610; 3,672 = 12 × 306; 3,636 = 12 × 303. **Every set's clip count is divisible by 12**,
  which is what *"transposing all the clips into 12 keys"* predicts **for the validation and testing
  sets as well as for training**.
- **Figure 3's excerpt, Sonata No. 8, is a member of the Testing row**, consistent with its caption's
  *"The testing result"*.

### §6.6 The time grid closes

32 frames × a 32nd note = 32 32nd notes = **4 crotchet beats**, the paper's *"4 beats"*. A hop of 4
frames = 4 32nd notes = an eighth note = **half a crotchet beat**, the paper's *"half a beat"*. Both
close in crotchet beats; the *"1 bar"* equivalence holds only in 4/4, as the paper itself says.

### §6.7 Two derivations about the chord-symbol task and the key axis, stated as derived

- **Share of chord labels that fall to the chord-symbol task's "other" class**, at the level of chord
  LABELS: major and minor triads are 2,951 + 1,356 = 4,307 of 7,394, so **3,087 labels, 41.75%**, are
  neither and fall to *other*. **This is a share of labels, not of segments**; the segment-level share,
  which is what the 72.71% is computed over, depends on durations and is not derivable from the paper.
- **Twenty-nine keys into twenty-four classes.** The dataset has *"29 different keys"* and the key
  output has 24 classes, so **the data has at least five more keys than the model has key classes, and
  at least one class must stand for more than one of the dataset's keys**. How
  they are mapped is not stated (§7.2).

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

Named rather than counted. **None of them moves a value in Table 3.**

1. **"Much more challenging" rests on two accuracies with different correctness conditions.** The
   72.71% is a 25-class accuracy in which, at the chord-label level, 41.75% of labels share one
   *other* class (§6.7); the 25.69% requires five components to be simultaneously correct. **The
   like-for-like figure the paper also prints is the Translation column, 56.05–56.91**, which is also
   below 72.71 — by **15.80** points at the best translation, 72.71 − 56.91 *(★ this subtraction ADOPTED
   FROM THE FIRST EXTRACT AT THE CROSS-CHECK, §9.4, re-derived here from this file's Table 3)* — so the ordering the paper claims is supported at its own printed values. **But the gap
   its sentence *"only 25.69%, which is far from that of chord symbol recognition"* points at mixes a
   difference in what counts as correct with any difference in difficulty, and the paper does not
   separate the two.**
2. **"Most significant" with no significance test and no uncertainty.** One split, no repeated runs
   reported, no seeds, no intervals, no per-piece figures anywhere in the eight pages as read. The testing set is
   six pieces, and by §6.5 its clip count is consistent with all twelve transpositions of those six
   pieces being scored, **which would make the tested clips twelve transposed copies of the same six
   movements rather than independent observations** — the paper does not say in terms whether the
   reported accuracies are computed over the transposed test clips.
3. **The abstract's general MTL claim is wider than its table.** §6.3.
4. **The key axis: 29 keys in the data, 24 classes in the model, no mapping stated.** §6.7.
5. **Figure 1(b)'s minor-key tonic is printed as upper-case "I"** over a C-minor triad, while the
   paper's convention says *"The capital numerals denote major chords, the lowercase numerals denote minor
   chords"*; the same panel prints the subdominant as lower-case *iv* over F minor, following the
   convention. **Stated at its width:** that convention sentence sits in the bullet that opens *"In a
   major key, the following Roman numerals are used"*, and then refers the reader to Figure 1 for *"both
   major and minor keys"*. *(Read at the page image at two openings, §8.)*
6. **The dataset's name is printed two ways**: *"Beethoven Piano Sonata with Function Harmony"* on page
   91, *"Beethoven Piano Sonata with Functional Harmony dataset"* on page 95.
6a. **The translation to chord symbols is described for the MTL scheme only, but Table 3 prints a
   Translation accuracy for the STL chord-function model too** (56.05). §5.1's sentence gives the
   translation to *"the chord function recognition task with MTL scheme"* and describes the STL scheme
   only as five networks trained individually; how the STL model's five outputs were translated is not
   stated.
6b. **A comparison cited to an audio paper.** §5.3 calls 72.71% acceptable against *"other existing
   works which also estimate chord symbols on classical music datasets such as [12,21]"*; reference
   [12]'s printed title is *"Music chord recognition from audio data using bidirectional
   encoder-decoder LSTMs"*. **This file checks the title only**; what data [12] used was not checked.
7. **Figure 3(e)'s translation renders sevenths and slash-bass symbols** (*C7, Ddim7/C, E♭7/G, B♭/D*),
   while the chord-symbol task that the Translation accuracy is measured against has 25 classes —
   major triads, minor triads and *other* (§2.6). **So either the scored translation rule is coarser
   than the figure's, or the figure shows something the metric does not score**; the paper states
   neither.
8. **How overlapping segments and clips are resolved at evaluation is not stated.** Segments are 32
   frames with a 4-frame hop, clips overlap by 32 segments, and accuracy is *"the number of correct
   detection and the number of total segments in the testing set"*. Which prediction counts for a
   stretch of music covered by several segments or two clips is not given, so the denominator of every
   accuracy in Table 3 is not recoverable from the paper.
9. **Typographic slips**, named: a stray full stop under the *INTRODUCTION* heading (page 90);
   *"have been adopt"*, *"has Roman number chord annotation"* (page 91); *"a 32th note"* (page 93);
   *"keys, We perform"* and *"STL scheme ,"* (page 94); *"non-cord tones"* (page 91); *"And all the repetitions in the sonatas
   are unfold"* (footnote 4); *"the the non-chord tone G"* (page 92); Table 2's *"19 20"* with no comma;
   *"multi-task leaning"* (page 93); *"a 80-D vector"* (page 93); *"targets labels"* (page 94); *"the
   all the translation accuracies"* (page 95); *"The dataset and the source code … is announced"*
   (abstract). **None changes a meaning.**

### §7.2 What the paper leaves without a value

- The number of segments in the testing set, and the number of secondary chords in it (the Secondary
  column's denominator).
- Whether *"when a secondary chord does exist"* is decided by the ground truth or by the prediction.
- How the five losses are combined in the multi-task networks; learning rate, batch size, epochs,
  stopping rule, L2 coefficient; how the validation set was used.
- The translation rule from five components to a chord symbol, and the granularity at which the
  Translation accuracy is scored.
- The mapping from the dataset's 29 keys to 24 key classes, and how transposition augmentation
  relabels keys, degrees and qualities (the last should be invariant, the first not).
- How many octaves an out-of-range note is moved, and whether that can change the lowest sounding note.
- Any inter-annotator agreement, any second annotation, or any review procedure for the dataset.
- Any per-piece, per-quality or per-key breakdown of the accuracies.

### §7.3 What is both measured and structural here, for a reader deciding what this paper can bear

- **The ground truth is one unnamed expert's reading**, and the paper says in terms that harmonic
  analysis is inherently subjective (page 92). **Nothing in the eight pages measures how far a second
  expert would agree**, so every accuracy in Table 3 is an agreement with one reader, not an accuracy
  against a measured ceiling.
- **The secondary-degree accuracies are 3.97 to 10.96%**, with the denominator unstated (§7.2), and
  the paper itself calls them *"very low for all experiment settings"*.
- **The input carries no spelling and no metre**, while the labels carry spelled keys and ♯/♭ degrees
  (§3.1). Any spelling-dependent distinction the labels make can reach the network only through
  musical context (THEORY, from the representation); the paper does not measure how often the network
  gets such a distinction right.
- **The output is segment-wise with no segmentation and no smoothing**, and the paper names the
  resulting discontinuities as unaddressed (§3.2).
- **What the paper does establish at its own values**: that on this split, a single BLSTM with a shared
  representation and one output layer over five components scored above five separately trained
  BLSTMs on every column it prints (§6.2), and that adding a task-specific layer raised degree and
  overall accuracy while lowering key, secondary, quality and inversion accuracy (§6.3). **Both are
  results with no repeated runs reported and no uncertainty.**

### §7.4 The reference list, listed for identification, and the bound on what it shows

**Thirty-five references, numbered [1] to [35], on printed pages 96–97.** They are listed here by
first author and year ONLY, to identify them. **This list is SHORTENED and is NOT a transcription** —
titles, venues and co-authors are omitted.

[1] Aldwell 2003; [2] Boulanger-Lewandowski 2013; [3] Chai 2005; [4] Cook 1987; [5] de Haas 2013;
[6] Deng 2017; [7] Deng 2018; [8] Devaney 2015; [9] Gómez 2006; [10] Granroth-Wilding 2013;
[11] Hamel 2013; [12] Hori 2017; [13] Illescas 2007; [14] Jacoby 2015; [15] Ju 2017; [16] Kaneko 2010;
[17] Korzeniowski 2017 (key estimation); [18] Korzeniowski 2017 (frame-level language models);
[19] Kröger 2008; [20] Liu 2015; [21] Masada 2017; [22] Mauch 2010; [23] McFee 2017; [24] Ni 2012;
[25] Ni 2013; [26] Nikrang 2017; [27] Papadopoulos 2009; [28] Raphael 2004; [29] Ruder 2017;
[30] Sigtia 2015; [31] Temperley 1999; [32] White 2015; [33] White 2016; [34] Yang 2016; [35] Zhou 2015.

**What it does not show:** that any cited result is as the paper characterises it. No cited work was
opened.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**All eight pages were re-opened after §0 to §7 were first written**, in four requests — pages 1–2,
3–4, 5–6 and 7–8 — **page 1 included**, every image checked present and legible at the image. Each
quotation, each transcribed cell and each located claim in §1 to §7 was compared against the page it
cites. **Then the text was swept for absolutes** — *only, never, no, none, nothing, every, all,
always, exactly, complete, whole, independent, any, cannot, must, most* — with every hit read at its
own line, not counted.

**Two glyph-level checks named in the first writing were made at this opening:** Figure 1(b)'s
minor-key tonic reads as an upper-case *I* at this resolution, at both openings; and Table 3's Chord
Symbol row prints its Translation cell with a mark visibly shorter than the dashes in the five cells
to its left, at both openings. **Both are calls on a rendered page image at one fixed resolution; a
reader with a text-extractable copy settles either in one act.**

### §8.2 What the read-back and the sweep struck in this side's own writing

Named rather than counted. Each is corrected at its site; this file had not landed, so no former
wording is preserved there, and the struck wording is recorded here instead.

- **An assumed mechanism.** §3.2 said *"a softmax-normalised 80-dimensional output"*, which reads as one
  softmax over all eighty classes; the paper says only that *"the Softmax function is used for the
  output vector"*. Now states that the arrangement is not given.
- **A second assumed mechanism.** §3.2 said the paper reports *"argmax-derived accuracies"*; the paper
  never names how a prediction is taken from the output. Struck to *accuracies only*.
- **A count of runs the paper never states.** §4 row 4, §7.1 item 2 and §7.3 said *"one run per
  model"* / *"single-run results"*; **the paper reports no repeated runs, which is not the same as
  stating one.** Narrowed at all three sites.
- **An assertion about data this side never examined.** §4 row 8 said the cited works' *"datasets
  differ"*. Neither [12] nor [21] was opened. Narrowed to what this paper states.
- **A claim about what a downstream consumer could bear.** §7.3 said no model recognises secondary
  chords *"at a level a downstream consumer could put load on"* — a judgment about consumers, not a
  fact of the paper. Struck to the printed range and the paper's own words.
- **An over-reach on the chord-symbol comparison.** §7.1 item 1 said the gap *"is the size of a
  difference in definitions, not in difficulty alone"*, which apportions the gap without anything that
  measures the apportionment. Narrowed to: the sentence mixes the two and the paper does not separate
  them.
- **An unbounded negative.** §1.3 said a tonic / dominant / subdominant classification is something
  *"the paper never measures"*. Bounded to *the eight pages as read*, and the same sentence now says
  the five-component label contains the Roman-numeral degree rather than standing apart from function
  theory.
- **An arithmetic statement worded wider than the arithmetic.** §6.7 said *"at least five of the
  dataset's keys share a class with another key"*; 29 keys into 24 classes gives five more keys than
  classes, which forces at least one shared class but does not fix how many keys share. Reworded to
  what the count forces.
- **A truncated quotation with no mark of truncation.** §2.5's STL quotation stopped before *"in the
  experiment"*. Completed.
- **A sentence broken by this side's own edit** during the sweep, in §7.3 — a clause cut in half by a
  replacement. Caught at the next search and rewritten whole.

### §8.3 What the read-back ADDED to the findings

**The read-back found things in the paper the first writing had not seen**, and each is now at its
site:

- **The dataset's name is printed two ways** (§7.1 item 6). The first writing reported only page 91's
  *"Function Harmony"*; page 95 prints *"Functional Harmony"*. **The first writing's framing — that
  the paper names its dataset differently from its title — was incomplete, not wrong.**
- **A Translation accuracy for the STL model that §5.1 describes a translation for only under MTL**
  (§7.1 item 6a).
- **A comparison cited to a paper whose title names audio data** (§7.1 item 6b), checked at the
  reference's title only.
- **The stated purpose of the transposition augmentation** — *"To balance the data distribution among
  all possible keys"* — now quoted at §2.6.
- **The paper's own two reasons for the chord-function gap**, now at §4 row 7.
- **The width of the Roman-numeral convention**: it sits in the major-key bullet and refers to Figure
  1 for both modes (§7.1 item 5).
- **Six further typographic slips** (§7.1 item 9).

### §8.4 ★ Candidate findings dropped because this side could not establish them

- **Whether panel (d) of Figure 3 agrees with the prose account of measure 85.** The red cells are too
  small at this resolution to transcribe value by value; the prose's *"whole-bar error predictions in
  key and secondary degree at measure 85"* is consistent with a red key span over that measure in the
  image, and **nothing further is claimed**.
- **Whether the figure's "vii°7/vi" carries a diminished or a half-diminished sign.** The glyph is too
  small; panel (c) gives quality **d7** for that cell, and §5.3's prose sets the superscript as a
  circle. Recorded as read with that bound.

### §8.5 The degradation tells, reported unprompted

**Two of the user's named tells fired in this file's first writing**, and the instances are named at
§8.2 rather than totalled:

- **Tell A — a count asserted without deriving it:** the *"one run per model"* count, at three sites.
- **Tell B — assertions about things this side had not examined:** the two assumed mechanisms (one
  softmax; argmax), the *datasets differ* claim, and the claim about what a downstream consumer could
  bear.

**All were caught at the read-back and sweep, and being caught does not lower the count.** The
standing rule of 2026-08-15 therefore applies at this sitting's close: **this side recommends that the
next member be taken by a fresh session**, at a verified stop.

### §8.6 The bound on this section

The read-back is a second pass over the same writing by the same side. **Nothing here establishes that
it found everything**, and the cross-check at §9 is the first comparison with a read this side did not
write.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**Row 46's first extract,
`reading_pass/extracts/chen-su-2018-functional-harmony-recognition-of-symbolic-music-data-with-multi-task-rnn.md`,
57,123 bytes at this sitting's staging call, was opened only after §0 to §8 of this file had landed**
(47,340 bytes at the staging call that followed that landing), and read whole — 715 lines in three
calls. The places the two files carry the same object were compared as this side met them in that one
whole read, and **each disagreement that turns on what a page prints was resolved at a THIRD opening of
that page**: printed pages 92, 93 and 95, each opened singly. Disagreement (g) turns on an absence
across the paper and was resolved at this read's two whole readings rather than at a single page.

**The comparison reaches the PAPER-FACING half of the first extract only.** Its record-facing half — its
four places where this project's record bears on the paper, its verification of `FRAMEWORK.md` §S4(a)'s
universal, its routings to design points, its reading of the reference list against candidacy rows, its
cross-primary check against row 47's extract, and its centrality verdict — **is outside the comparison
entirely: this side opened none of those objects**, so on that half this file is silent and is not a
second opinion.

### §9.2 ★ What the two reads reached independently

Named rather than counted, and the page count listed separately because it is not independent:

- **Every numeric cell of Table 3**, all twenty-two, identical in both files.
- **Every cell of Table 1**, identical.
- **Table 2's Validation and Testing rows**, identical, and the missing comma in *"19 20"*, recorded by
  both as printed. *(The Training row is disagreement (a) below.)*
- **Footnote 8's ten quality counts summing to 7,394**, derived by both.
- **24 + 21 + 21 + 10 + 4 = 80**, the output dimension, derived by both.
- **The seven differences MTL-1 minus STL and the seven MTL-2 minus STL**, identical to the hundredth,
  in the same sign convention; both reads found MTL-2 below STL on three columns (key, secondary,
  quality).
- **The 29 keys against 24 key classes, unreconciled in the paper**, found by both.
- **The input discards spelling and transposes out-of-range notes into C1–C6**, found by both.
- **No segmentation decision**, with the paper's own *discontinuities* sentence and its CRF [21] remedy,
  found by both.
- **One annotator and no agreement figure**, found by both.
- **Transposition augmentation reaching the validation and testing sets as well as training** — stated
  by the first extract as *"applied to training, validation and testing alike"*, and reached by this file
  from *"all the clips"* together with the clip counts' divisibility by twelve.
- **No uncertainty and no significance test on any figure**, found by both.
- **The licence box and running header**, transcribed identically in substance.
- **Figure 2(b)'s per-task layer sizes 512 / 512 / 512 / 256 / 128**, identical.
- **The page count, eight — an agreement BY CONSTRUCTION and not an independent one**: both reads put an
  out-of-range page request to the same tool (page 20 there, page 99 here), which is one measurement
  asked twice.

### §9.3 ★ The disagreements — resolved at the paper

**All of them go against the first extract. None was found against this file.** Named rather than
counted; each call states its ground.

**(a) ★ TABLE 2's TRAINING ROW, AND THE FINDING BUILT ON IT.** The first extract transcribes the
Training row as *"1, 3, 5, 11, 16, 19 20, 22, 23, 25, 26, 32"* — **twelve numbers, including 23** — and
its finding (6) derives from that that **piece No. 23 is in both the training and the validation set**
(*"12 + 6 + 6 = 24 against 23 distinct pieces"*), routing it to measurement design as a training/validation
overlap. **At the third opening of page 93, the Training row reads "1, 3, 5, 11, 16, 19 20, 22, 25, 26,
32" — eleven numbers, no 23**, as this file transcribed it at its first reading and its read-back.
**The ground for the call, beyond three readings of the same cell:** with eleven entries the three rows
hold 11 + 6 + 6 = 23 numbers and their union is exactly footnote 4's twenty-three-piece list, so the
table and the footnote agree; the twelve-entry reading is the one that manufactures a contradiction the
paper does not otherwise show. **On the priming test the call is strong** — *"22, 25"* is two
two-digit numbers side by side, and a reader completing a sequence 22, 23, … is the reader primed
toward the wrong one. **The first extract's finding (6) therefore rests on a transcription the page
does not support.** It moves no Table 3 value. **Whether that finding has already been carried into
any other part of the record is unknown to this side**, which opened neither the progress record nor
the findings surface.

**(b) A MISQUOTATION IN THE AUTHORS' OWN EXPLANATION.** The first extract quotes §5.3 as *"partly
because **functional** harmony itself is complicated and equivocal"*. **Page 95 prints "partly because
tonal harmony itself is complicated and equivocal"**, read at the third opening. The substituted word
is the paper's own title term, which is the word a reader of this paper is primed to supply. No value
moves.

**(c) A SECOND WORD SUBSTITUTED IN A QUOTATION.** The first extract quotes *"the **detection** of the
modulation to C minor at measure 85 is also meaningful"*. **Page 95 prints "the prediction of the
modulation to C minor at measure 85"**, read at the third opening. No value moves.

**(d) A SECTION LOCATOR.** The first extract places the subjectivity sentence — *"It should be
acknowledged that harmonic analysis is inherently subjective…"* — at *"§3.2, page 92"*. **On page 92 it
stands in the left column above the heading "3.2 Annotations in the BPS-FH Dataset"**, so it belongs to
§3.1's continuation, read at the third opening. The page is right; the section is not. No value moves.

**(e) AN INPUT CLAIM WIDER THAN THE PAGE.** The first extract's coupling facts say *"**Meter is given
and is load-bearing**: the segment length is defined as '4 beats (or equivalently 1 bar)' for a 4/4
piece and the hop as 'half a beat', so the beat and the bar are read off the notation rather than
inferred."* **At the third opening of page 93**, §3.3 measures durations *"in crotchet beats"* and
defines the segment as 32 frames of a 32nd-note grid; the *"1 bar"* is an equivalence stated for a 4/4
piece. **Nothing on the page says the metre or the barlines enter the input or that segments are
aligned to bars**, and a hop of 4 frames under a 32-frame segment does not align them. **The beat half
of the claim is supported** (the crotchet unit comes from the notated durations); **the metre and bar
half is not.** No value moves.

**(f) A MECHANISM THE PAGE DOES NOT STATE.** The first extract says *"A softmax exists over every one of
the five label sets at every segment"*. §4 on page 93 says only *"the Softmax function is used for the
output vector"*, of an 80-D vector. **Whether it is one softmax or five is not stated.** This file's
first writing made the opposite assumption and struck it at its read-back (§8.2), **so this is a defect
both reads made and one of them caught.** No value moves.

**(g) A RUN COUNT THE PAPER DOES NOT STATE.** The first extract says *"every difference below is a
difference of single runs"* and *"Every cell of Table 3 is a single number from a single run"*. **The
paper reports no repeated runs; it does not state that there was one.** This file's first writing made
the same assertion and struck it at its read-back (§8.2) — **again a defect both reads made and one
caught.** No value moves.

**(h) A PUNCTUATION MARK INSIDE A QUOTATION.** The first extract quotes §3.3's hop sentence ending
*"(or half a beat)"*; page 93 prints *"(or half a beat.)"*, the full stop inside the parenthesis. Trivial,
recorded because it sits in a quotation.

**A difference of RENDERING, not called as a defect of either file.** Table 3's Chord Symbol row,
Translation cell: the first extract renders it as an en dash like the cells beside it; this file
renders it as a hyphen, the mark being visibly shorter in the page image at all three openings of page
95. And the first extract sets **72.71** in bold in its own table without saying whether the page does;
**no cell of Table 3 is bold in the page image**. Neither changes a value, and **a reader with a
text-extractable copy settles both in one act.**

### §9.4 What the first extract has that this read did not — adopted here and marked at its site

Each re-derived at this file's own transcriptions rather than copied from that file's text:

- **No chord root and no bass among the predicted labels** — §3.2.
- **The largest absolute difference against STL is the two-layer model's Secondary −5.41** — §6.3.
- **The 15.80-point gap** between direct chord-symbol recognition and the best translation — §7.1 item 1.
- **Three figures, three tables and no numbered equation** — §1.1.

### §9.5 What this read has that the first extract does not

Named rather than counted. Those that bear on how a printed value or a stated claim is read are listed
first:

- **The Translation accuracy printed for the STL model, where §5.1 describes a translation only for the
  MTL scheme** (§7.1 item 6a).
- **Twelve transpositions of six test pieces**, so the tested clips are not independent observations if
  the reported accuracies are computed over them, which the paper does not state in terms (§7.1 item 2).
- **The denominator of every Table 3 accuracy is not recoverable**, because the resolution of
  overlapping segments and clips is not given (§7.1 item 8).
- **Figure 3(e) renders sevenths and slash-bass symbols while the chord-symbol task scores 25 classes**
  (§7.1 item 7).
- **At the chord-label level, 41.75% of labels fall to the chord-symbol task's *other* class** (§6.7).
- **The two-layer MTL model is below the one-layer model on four of the five component columns**, and the
  paper's text reports only the secondary drop (§6.3).
- **A comparison cited to a reference whose title names audio data** (§7.1 item 6b).
- **Figure 1(b)'s upper-case minor tonic against the paper's own case convention** (§7.1 item 5).
- **The dataset's name printed two ways** (§7.1 item 6).
- **Whether "when a secondary chord does exist" is decided by the ground truth or by the prediction** is
  not stated (§7.2).
- **The measure-by-measure transcription of Figure 3's panels (b) and (c)** (§5.3).
- **The typographic slips named as slips** (§7.1 item 9). The first extract carries several of them
  inside its quotations as printed, and flags as the paper's own typesetting only the missing comma in
  Table 2, as far as that file was read here.

### §9.6 What the cross-check does NOT establish

- **That nothing further is wrong in either file.** The comparison ran over what both files carry.
- **That this read is the better one.** This file's own read-back had already struck ten things in its
  first writing (§8.2), and two of the defects found in the first extract — (f) and (g) — are defects
  this file made too and caught.
- **Anything about the first extract's record-facing half**, including whether its finding (6) was
  carried anywhere.
- **Step 8 of the procedure** — the paper went against the FIRST extract at every disagreement above and
  against this file at none the comparison reached. **That file is untouched and its defects are
  recorded here as standing with the user**, on this line's standing ground that rewriting another
  read's text destroys what the doubling compares.
  (★ MADE STALE 2026-09-16 BY THE USER'S RULING OF THAT DATE, AND LEFT STANDING (#12). The user ruled
  that row 46's first extract is corrected at each of the eight sites (a) to (h), with every former
  wording preserved in place, for row 46 only. **That correction was made the same day**; the first
  extract's own banner records it, and its finding (6) is withdrawn there. **The list at §9.3 above is
  unchanged** and remains the ground for each correction.)
