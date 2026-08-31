# Second-pass extract — row 1: McLeod & Rohrmeier 2021, the modular harmonic analyzer

> **STATUS: SECOND INDEPENDENT EXTRACTION (session 2 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the independence protocol
> of `reading_pass/continuation.md` §2. **Neither `reading_pass/extracts/` nor
> `docs/research_papers/reading_pass_2026_08/` was opened before this file was written.** The
> paper was read at its source, `https://apmcleod.github.io/pdf/ismir-harmony.pdf`, in three
> separately-prompted passes.
>
> **THE GRADE OF THIS READ, DECLARED AT ITS FACE.** This environment's web-fetch tool answers
> prompted questions over a document rather than returning its text; it does not put the PDF
> before the reader as page images. So every claim below is **RELAYED**, not at-the-object, and
> quoted wording is the tool's relay of the paper's wording. This is the same bound
> `reading_pass/additions.md` declares for session 1's fetched rows. **The independence this
> extract has is session-and-prompt independence, not read-tool independence** — see the
> cross-check file for what that does and does not buy.

## Identity

Andrew McLeod & Martin Rohrmeier (EPFL), "A Modular System for the Harmonic Analysis of Musical
Scores using a Large Vocabulary", *Proceedings of the 22nd International Society for Music
Information Retrieval Conference* (ISMIR 2021, online).

## Claims, labeled

**[FACT] The system is six modules, each a separately trained model.** Named as the paper names
them: the **Chord Transition Model (CTM)**, the **Chord Classification Model (CCM)**, the **Chord
Sequence Model (CSM)**, the **Key Transition Model (KTM)**, the **Key Sequence Model (KSM)**, and
the **Initial Chord Model (ICM)**. (Method section.)

**[FACT] The vocabulary is 1,540 absolute chord symbols and 70 keys.** The chord symbol is a
(root, type, inversion) triple over 35 spelled roots (A–G with double-flat through double-sharp)
and 12 chord types; the key is a (tonic, mode) pair over the same 35 spelled tonics and two modes,
major and minor. (Method section; relayed wording "1540 chords (each with a root, type, and
inversion)" and "70 keys (with a tonic and mode)".)

**[FACT] Pitches are SPELLED, not enharmonically reduced.** Relayed verbatim: *"where an A♯ is a
different pitch from a B♭"*, and the paper positions this as uncommon in the existing work —
*"we also use spelled pitches … which is still uncommon in existing work."*

**[FACT] Applied chords are not an output category; they are represented as brief, possibly nested
key changes.** Relayed verbatim: *"Our model does not output applied chords (e.g., secondary
dominants like V/V) directly. Rather, we treat them as brief, potentially recursively embedded,
key changes."*

**[FACT] Chords and keys are decoded in ONE search, not one after the other.** The CTM's per-note
transition scores do not commit a segmentation; they *constrain which chord windows are valid*,
and the beam search then finds *"the most probable complete and labeled path through the score"*
over windows, chord labels and key labels together. A path's probability is the product, over its
chord windows, of the CTM probability, the CCM probability, the KTM probability and the sequence
probability, with an exponent on window count so that fewer, longer segments are not preferred by
construction. (Inference section, Eq. 1 and 3 as relayed.) **★ SEE THE CROSS-CHECK: one of this
session's own three prompted passes returned the opposite reading ("segmentation occurs before
classification") before a targeted third pass settled it at the Inference section. The
before-versus-jointly question is exactly what DP-C turns on, so the disagreement is recorded
rather than smoothed.**

**[FACT] Four inference parameters are tuned by grid search on the validation set:** `ctmin` and
`ctmax` (bounds on a window boundary's CTM score, so that *"the CTM is not ignored"*), `C_durmax`
(a maximum chord-window duration), and `α` (a scaling factor placing the several models' outputs
in a comparable range, needed because the KSM ranges over 70 keys while the CCM ranges over more
than a thousand chords).

**[FACT] Module implementations.** CTM and CCM: a feed-forward layer followed by a **bidirectional**
LSTM. CSM, KTM, KSM: a feed-forward layer followed by a (unidirectional) LSTM — KTM with a sigmoid
output, KSM with a softmax. ICM: **counts** of each chord's proportion in the training data with
additive smoothing — not a network.

**[FACT] The claimed advantage of modularity is interpretability during development, stated as a
practical benefit rather than an accuracy one.** Relayed verbatim: *"The modular design also gives
a practical, benefit over the single-model end-to-end design that is common in existing work. Its
output is highly interpretable, which has helped significantly in its development."* The paper
describes the resulting cycle as: locate a mislabeled segment in the output, then examine each
component's output for that segment.

**[FACT] The key axis is measured as noisier BECAUSE it is modular.** Relayed verbatim: *"the key
depends on outputs from the other components, adding noise to the process, which isn't a factor
for the end-to-end baseline."*

**[FACT] The system's output is stated as nearly a full Roman-numeral analysis, short of two named
things.** Relayed verbatim: *"Our system's output is nearly equivalent to a full RNA, lacking only
altered chordal tones such as suspensions, and pedal tones, which we intend to include in future
work."* (This is the same authors' own forward pointer to row 2 of this population.)

**[FACT] The corpora and the split.** An **internal corpus of 742 pieces**, 16th to 20th century
(J. S. Bach, Couperin, Grieg, Beethoven and others), and **F-H, 201 pieces** — 119 Beethoven, 29
Schubert, 24 J. S. Bach, 19 others — itself *"a combination of prior existing corpora: TAVERN,
BPS-FH, and Roman Text."* Each corpus split separately: *"randomly take 80% for training, and 10%
each for testing and validation."*

**[FACT] The two corpora's annotations differ systematically.** Relayed verbatim: *"there seems to
be a systematic difference between the annotations of the two corpora."*

**[CONJECTURE — the paper's own future work, not a result]** Applying the system to MIDI and audio
input; a human-in-the-loop annotation tool in which expert annotators correct the system's output.

## Coupling facts (the commission's mandatory widening)

**What it ASSUMES of its upstream (L0/L1 in our charters).** A symbolic score reduced to *"a
sequence of notes N ordered temporally by onset position"*, where each note carries: a **spelled**
pitch class (letter A–G plus an accidental from double-flat to double-sharp), an octave, a
duration, and — load-bearing — **the metrical level of both its onset and its offset**, quantised
to *downbeat / beat / sub-beat / other*. **So a metrical grid is a required input, not something
the system infers**, and the note stream must already be spelled. No voice separation is required.
No key signature is required as input; the key path is inferred.

**What it HANDS its downstream.** Per chord segment: an absolute chord symbol (spelled root, type,
inversion — inversion expressed in figured-bass terms) and a local key (spelled tonic, mode).
Applied chords arrive downstream **as key changes, not as applied-chord labels** — a consumer that
wants "V/V" must reconstruct it from a nested short key span. Nothing about suspensions, altered
chord tones or pedal tones is handed on. The output is not a distribution surface: the paper
publishes the best path.

**Its own STATED SCOPE and limits.** Symbolic scores only (MIDI and audio are named future work);
major and minor modes only (70 keys = 35 tonics × 2 modes — **no modal vocabulary**); no altered
chord tones, no suspensions, no pedal tones; applied chords only as embedded key changes; the key
axis explicitly noisier than an end-to-end baseline's by the modularity itself; and the two
evaluation corpora annotated differently enough that the paper says so in its own text.

## Measured results, as tabulated

Metric: **Chord Symbol Recall (CSR)** — relayed as *"proportion of time during which the estimated
label matches the ground truth label"*, i.e. duration-weighted, not per-segment.

| Corpus | Model | Root | +Type | +Inversion | Key | Full |
|---|---|---|---|---|---|---|
| Internal (742) | reference [24] baseline | 57.0 | 47.7 | 37.6 | 64.9 | 29.0 |
| Internal | CSM | 76.6 | 68.8 | 62.1 | 66.9 | 44.7 |
| Internal | CSM-I | 76.5 | 68.7 | 62.0 | 69.0 | 46.3 |
| Internal | CSM-T | 77.6 | 70.0 | 62.8 | 70.2 | 46.9 |
| F-H (201) | reference [24] baseline | — | — | — | — | 42.8 |
| F-H | CSM | 73.3 | 65.4 | 55.6 | 60.8 | 40.5 |
| F-H | CSM-I | 75.0 | 66.8 | 56.9 | 67.0 | 44.6 |
| F-H | CSM-T | 75.4 | 67.8 | 58.1 | 69.4 | 45.9 |

*(The three CSM variants are the paper's chord-sequence-model ablation arms. This second pass did
not establish what the -I and -T suffixes name; that is a gap in this extract, stated rather than
guessed, and it is carried into the cross-check.)*

## What this extract does NOT establish

- The beam width and any pruning rule: the Inference section as relayed states none.
- What the -I and -T variants of the CSM are.
- The training objective and loss of each module.
- Whether the reported figures are on the test split alone (stated as the protocol, not re-checked
  against the table's own caption).
- **Nothing here is at-the-object.** Every figure and every quotation is relayed.

*Provenance: second pass of the reading pass, 2026-08-31. Read at the source URL only. No
specification is derived here, no document amended, no code opened, no register touched.*
