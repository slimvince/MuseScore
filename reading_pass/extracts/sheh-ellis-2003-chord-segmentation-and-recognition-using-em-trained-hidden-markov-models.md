# EXTRACT — Sheh & Ellis, "Chord Segmentation and Recognition using EM-Trained Hidden Markov Models" — Task B candidacy row 18, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All seven pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.**
> **The held document prints NO page numbers** (see the identity section), so every location below is
> given as the printed section, table, figure or equation number, with the held file's own page order
> written as *"page n of 7 of the held file"* where a location needs one.
>
> **Why this paper and its place in L2's slice.** It is row 18 of `reading_pass/candidacy_upgrades.md`
> (line 80), ADMITTED there as *"DP-C's 68.8-against-23.3 primary, and its method is the
> boundaries-given-versus-found design that measurement is about."*
> `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 (line 65) places it in L2's slice: *"DP-C's
> boundaries-given-versus-found primary."* It is fifth in group 2 of the proposed reading order
> ("segmentation decided with the labelling": rows 10, 11, 19, 20, 18, 4, 47), and row 47 closes that
> group.
>
> **Where the record cites this paper, established by a `Grep` of the staged tree for "Sheh" and
> "Ellis" BEFORE extracting rather than inherited.** Three places, and only three: `FRAMEWORK.md`
> line 1595 (§S4(d), the sealed first-stage text's excluded alternative *"Segment first, then label"*)
> and line 1805 (DP3's ground); and `reading_pass/population.md` line 111 (the V10 verification row).
> **`FRAMEWORK.md`'s live DP-C, at lines 690–701, carries the figure WITHOUT the authors' names.**
> **`cowork_reading_pass_findings_2026_08_31.md` does not name this paper at all** — the search
> returned no occurrence in it, which answers the question the hundred-and-twenty-fifth handoff entry
> left open (it records that the findings surface was not searched for "Sheh").
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — a MILD finding; the input is AUDIO

Alexander Sheh and Daniel P.W. Ellis, LabROSA, Dept. of Electrical Engineering, Columbia University,
New York NY 10027 USA (`{asheh79,dpwe}@ee.columbia.edu`). Printed title, page 1 of 7 of the held file:
**"Chord Segmentation and Recognition using EM-Trained Hidden Markov Models"**. Keywords printed:
*audio, music, chords, HMM, EM*.

**The bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` line 32) names *Sheh & Ellis, "Chord
Segmentation and Recognition using EM-Trained HMMs," ISMIR 2003*, the URL
`https://www.ee.columbia.edu/~dpwe/pubs/ismir03-chords.pdf`, held ✓, tier **LINK (author copy)**.

**What matches and what does not, at the object.** The authors match. The title matches except that the
held document spells out **"Hidden Markov Models"** where the bibliography's row abbreviates **"HMMs"**
— the same words, one abbreviated. **No venue name, no conference line, no running header and no page
numbers are printed anywhere in the held document.** The only dated line is the permission notice in the
bottom-left box of page 1: *"Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are not made or distributed for
profit or commercial advantage and that copies bear this notice and the full citation on the first page.
©2003 Johns Hopkins University."*

**So the identity check answers the row's own question this far and no further.** The year is 2003 and
the copyright holder is the institution that hosted ISMIR 2003, which is consistent with the
bibliography's venue; but **whether the held file is the proceedings text or the author's own copy is
NOT establishable from what is held**, because the proceedings' pagination and conference line are
absent. That is exactly what the bibliography's own tier already says — *LINK (author copy)* — and the
URL is the second author's personal publications directory. **Recorded as a MILD identity finding of the
shape rows 29 and 11 carry, routed to the bibliography reconciliation; no verdict, and nothing in the
record's characterisation of the paper turns on it.** The consequence for this extract is only that no
location below can be given as a proceedings page number.

**The carried question (c) is answered at page 1: the input is AUDIO.** The Abstract's first sentence:
*"Automatic extraction of content description from commercial audio recordings has a number of important
applications…"*, and *"In this work, we build a system for automatic chord transcription using speech
recognition tools."* §3 states the material: twenty Beatles songs *"read from CD then downsampled and
mixed into mono files at 11025 Hz sampling rate."* **There are no notes, no score and no symbolic input
anywhere in the method.** So the paper is admitted for its METHOD with the audio domain travelling as a
caveat under the candidacy derivation's consequence (ii), exactly as rows 27, 3, 26 and 20 were.

**Structure of the held document:** five numbered sections (1 Introduction; 2 System, with §2.1 Pitch
Class Profile Features, §2.2 Hidden Markov Models, §2.3 Expectation Maximization, §2.4 Viterbi
Alignment, §2.5 Weighted Averaging of Rotated PCP Vectors; 3 Implementation and Experiments, with §3.1
Frame Accuracy Results, §3.2 Chord Confusion, §3.3 Model Means, §3.4 Output Example; 4 Future Work, with
§4.1 Training Parameters; 5 Conclusion), then Acknowledgments and References (7 entries); three figures;
four tables; six numbered equations. Seven pages in the held file.

**File:** `docs/research_papers/sheh_ellis_2003_ismir_chord_segmentation_em_hmm.pdf` (109,996 bytes at
the listing).

## Claims, labeled

### What the method decides, and from what

**[FACT — the task, Abstract and §1.]** *"Chord sequences are a description that captures much of the
character of a piece in a compact form and using a modest lexicon. Chords also have the attractive
property that a piece of music can (mostly) be segmented into time intervals that consist of a single
chord, much as recorded speech can (mostly) be segmented into time intervals that correspond to specific
words."* The analogy is stated in terms in §1: *"By making a direct analogy between the sequence of
discrete, non-overlapping chord symbols used to describe a piece of music, and the word sequence used to
describe recorded speech, much of the speech recognition framework can be used with minimal
modification."*

**[FACT — the front end, §2.1.]** Audio at 11 025 Hz, framed into overlapping windows of N = 4096 points
(Hanning), short-time Fourier transform (eq. 1); the STFT bins are mapped to Pitch Class Profile bins by
eq. 2, `p(k) = ⌊24 · log₂(k/N · f_sr/f_ref)⌋ mod 24`, and each PCP element sums the bins mapping to it
(eq. 3). *Recorded as printed rather than reconciled:* the prose says *"we calculate the value of each PCP
element by summing the magnitude of all frequency bins that correspond to a particular pitch class"*,
where eq. 3 sums `|X[k]|²`, the squared magnitude. Both are transcribed as they stand; the difference is
the paper's and is not resolved here. **The PCP vector has 24 dimensions, not 12** — *"Our
experiments use a finer grained PCP vector of 24 dimensions to give some flexibility in accounting for
slight variations in tuning."* Reference frequency 440 Hz (A4). *"A step size of 100ms, or 10 PCP frames
per second, is employed."*

**[FACT — the model, §2.2.]** *"PCP vectors are used as features to train a hidden Markov model (HMM)
with one state for each chord distinguished by the system."* The emission is **a single Gaussian in 24
dimensions with a diagonal covariance** — *"We additionally assume that the features are uncorrelated
with each other, so that Σᵢ consists only of variances, i.e. all off-diagonal elements are zero"* — so
each state carries 24 means and 24 variances, plus the transition probabilities. **This is the whole
model: one state per chord label, first-order Markov transitions between them.**

**[FACT — the training regime, §2.3.]** The chord labels of each frame are hidden; only the chord
SEQUENCE of a piece is known. *"If we knew which state (i.e. chord) generated each observation in our
training data, the model parameters could be directly estimated. Hand-marked chord boundaries could
provide the necessary information, but it is extremely time-consuming to create these files. In our
case, we assume only that the chord sequence of an entire piece is known, but treat the chord labels of
each frame as hidden values within the EM framework. This frees the researcher from the laborious and
problematic process of manual annotation."* Baum-Welch (forward-backward) re-estimation, eq. 4; *"M is
the model comprising the constraints on observations X, constructed by concatenating the states
specified in the known chord sequence into a single composite HMM for each song."*

**[FACT — the two decoding conditions, §2.4. THIS IS THE LOAD-BEARING PASSAGE OF THE WHOLE EXTRACT.]**
Verbatim: *"in forced alignment, observations are aligned to a composed HMM whose transitions are
limited to those dictated by a specific chord sequence, as in training i.e. **only the chord-change
times are being recovered, since the chord sequence is known**. In recognition, the HMM is unconstrained,
in that any chord may follow any other, subject only to the Markov constraints in the trained transition
matrix."* And the authors' own restatement in §3.1's discussion (page 5 of 7): *"Forced alignment always
outperforms recognition, as expected since the basic chord sequence is already known in forced alignment
**which then has only to determine the boundaries**, whereas recognition has to determine the chord
labels too."*

**[FACT — the purpose of running both, §2.4.]** *"We perform both sets of experiments to demonstrate
that even when pure recognition performance is quite poor, a reasonable accuracy under forced alignments
indicates that the models have succeeded in learning the desired chord characteristics to some extent."*

**[FACT — the output, §2.4.]** *"The output of the Viterbi algorithm is the single state-path labeling
with the highest likelihood given the model parameters. This best-path assigns a chord to every 100ms
time slice, resulting in a time-aligned song transcription."* One path; no rivals and no confidence are
published anywhere in the paper.

**[FACT — parameter pooling by transposition, §2.5.]** *"an improvement can be made by calculating a
weighted average of the models for every chord family (major, minor, maj7 etc.) across all root chromas
(A, A#, B, C, etc.). This involves rotating the PCP vectors from each chroma until PCP[0] is the root
pitch class, computing a weighted average across all the chromas (weighted by frequency of chord
occurrence), then un-rotating the weighted average PCP vectors back to their original positions to
construct new, regularized models for each chord."* Eq. 5 is the rotated weighted mean and eq. 6 the
un-rotation; *"(Variances are similarly pooled.)"* The stated motivation: *"by using values
characteristic to the entire family, a derived state model avoids overfitting its particular chord data.
There is also the advantage of increasing each individual chord's training set to the union of all chord
family members. The results below show that this simple approach gave very significant improvements."*

**[FACT — the label set, Table 2.]** Chord families: *maj, min, maj7, min7, dom7, aug, dim* (seven).
Roots: *A♭, B♭, C♭, D♭, E♭, F♭, G♭, A, B, C, D, E, F, G, A♯, B♯, C♯, D♯, E♯, F♯, G♯* (twenty-one spelled
roots). Caption: *"Definition of the 147 possible chords that can appear as HMM states. The label 'X' is
given to chords not covered by this set. In practice, only 32 labels occurred in our data."* (7 × 21 =
147, derived here from the table's own two lists; the caption's own figure agrees.) **The 'X' label is an
explicit out-of-vocabulary class, and it appears as a state in the confusion matrices of Table 4.**

### The experimental setting (§3, Tables 1–3)

**[FACT — the corpus, §3 and Table 1.]** Twenty songs from three early Beatles albums (*Beatles for
Sale*, *Help*, *A Hard Day's Night*), listed one per row in Table 1 with a *set* column marking two of
them **test** and the other eighteen **train**. Implemented with the HTK toolkit (Young et al., 1997).

**[FACT — where the labels come from, §3.]** *"The chord sequences for each song were produced by
mapping the progressions from a standard book of Beatles transcriptions (Paperback Song Series: The
Beatles, 1995) to a simpler set of chords as shown in table 2."*

**[FACT — where the ground truth comes from, §3.]** *"Two songs, 'Eight Days a Week' and 'Every Little
Thing', were designated as the test set, and for these songs the actual chord boundaries were
hand-labeled using WaveSurfer; this provided the ground-truth used to determine frame error rates."*
**So the frame-accuracy ground truth exists for exactly two songs, hand-marked by the authors, and the
training labels for the other eighteen are a commercial songbook's chords mapped down to the label set.**

**[FACT — the five feature configurations, §3.]** MFCC (24 MFCCs); MFCC_D (12 MFCCs plus deltas);
MFCC_0_D_A (7th-order MFCCs including c₀, with deltas and accelerations); PCP (24 dimensions); PCP_ROT
(the averaged rotated PCP models of §2.5, 24 dimensions). *"In each case, the total model dimensions
were kept at 24 to match the number of parameters in the PCP systems."*

**[FACT — the two training sets, §3.]** *"We trained on the 18 songs from our dataset not designated as
test examples. We also repeated the experiments training on all 20 songs — i.e. including the test
examples — to establish a performance ceiling in the optimistic condition when the test cases exactly
match part of the training set."* **train18 is the honest condition and train20 is declared, by the
authors, as the optimistic ceiling.**

**[FACT — the training procedure, §3.1's left column and the right column of page 4 of 7.]** *"Training
begins with the uniform segmentation and chord labeling of every training song, using chord sequence
information. HMM state chord models were initialized with global mean and variance values from the
entire dataset (so called flat-start EM initialization)… Prior to training, a single composite HMM for
each song is constructed according to the chord sequence information (see section 2.2), which constrains
the training process. EM proceeds for 13 to 15 iterations."* Then the averaged-rotated PCP models are
combined as in §2.5. For recognition, *"An appropriate chord loop is derived from the chord sequence
files of all training songs"* — i.e. **the recognition vocabulary is the set of chords seen in training,
and the transition matrix is the trained one.**

**[FACT — Table 3, transcribed cell by cell.]** Caption: *"Percent Frame Accuracy results. Within each
row, the first subrow refers to 'Eight Days a Week' and second subrow to 'Every Little Thing'. Columns
show the frame accuracy for forced alignment and recognition, using the train18 (excluding test cases)
and train20 (including test cases) sets."*

| Feature | Align train18 | Align train20 | Recog train18 | Recog train20 |
|---|---|---|---|---|
| MFCC — *Eight Days a Week* | 27.0 | 20.9 | 5.9 | 16.7 |
| MFCC — *Every Little Thing* | 14.5 | 23.0 | 7.7 | 19.6 |
| MFCC_D — *Eight Days a Week* | 24.1 | 13.1 | 15.8 | 7.6 |
| MFCC_D — *Every Little Thing* | 19.9 | 19.7 | 1.5 | 6.9 |
| MFCC_0_D_A — *Eight Days a Week* | 13.9 | 11.0 | 2.2 | 3.8 |
| MFCC_0_D_A — *Every Little Thing* | 9.2 | 12.3 | 1.3 | 2.5 |
| PCP — *Eight Days a Week* | 26.3 | 41.0 | 10.0 | 23.6 |
| PCP — *Every Little Thing* | 46.2 | 53.7 | 18.2 | 26.4 |
| PCP_ROT — *Eight Days a Week* | **68.8** | 68.3 | **23.3** | 23.1 |
| PCP_ROT — *Every Little Thing* | 83.3 | 83.0 | 20.1 | 13.1 |

*Transcription check, run at the page and recorded because it is what makes the table safe to cite.*
Three of the paper's own sentences cross-check cells: (i) *"models trained using the base PCP features
perform better than models trained using MFCCs in all cases except one (recognition of the first test
example using MFCC_D and train18)"* — 15.8 against PCP's 10.0, the one exception, so both cells are
confirmed by the prose; (ii) *"Using averaged-rotated PCPs (PCP_ROT) results in models that outperform
all MFCC-trained ones, as well as the base PCP models in all cases except, curiously, recognition based
on train20"* — PCP_ROT 23.1 and 13.1 against PCP 23.6 and 26.4, both cells confirmed; (iii) *"the
PCP_ROT models performing as much a four times better than the best MFCC counterparts"* (the paper's own
wording, printed with that slip) — 83.3 against the best MFCC align/train18 value in the second subrow,
19.9, is 4.2 times, which confirms 83.3. **The one cell with no prose cross-check of its own is
PCP_ROT / align / train20 / "Every Little Thing", read as 83.0 at two separate readings of the image; it
is corroborated in direction, not in digit, by the authors' statement that *"PCP_ROT achieves no benefit
from training on the test set"*, which requires the train20 align values to sit at or just below the
train18 ones (68.3 < 68.8 and 83.0 < 83.3).** No cell is transcribed that was not read at the image.

**[FACT — the abstract's headline figure, and where it is NOT.]** The Abstract states *"Our results on a
small set of 20 early Beatles songs show frame-level accuracy of around 75% on a forced-alignment
task."* **That number is in no table.** The two forced-alignment train18 cells of the best system are
68.8 and 83.3, whose mean is 76.05 (derived here, not printed). **Anyone citing "around 75%" from this
paper is citing the abstract's round of two test songs' alignment accuracies, not a measured cell.**

**[FACT — chord confusion, §3.2 and Table 4.]** Table 4 gives one confusion matrix per reference label
for *"recognition… using weight-averaged PCP HMMs (PCP_ROT), trained without using test songs
(train18)"*, for every frame in "Eight Days a Week", *"which we label with only 5 chords plus 'X'"* — the
six matrices are headed A MAJOR, D MAJOR, G MAJOR, B MINOR, E MAJOR and X CHORD. Caption:
*"Confusion matrices for recognition of 'Eight Days a Week', PCP_ROT, train18. Enharmonic equivalent
chords have been combined."* The stated reading: *"Notice the frequent confusion between major chords
and their minor version, which differ only by the semitone between major and minor third intervals.
Better discrimination of these chords might be achieved by increasing the system's frequency
resolution."*

**[FACT — the worked example, §3.4 and Figure 2.]** *"Figure 2 shows an eight-second segment of the song
'Eight Days a Week' taken about 16 seconds into the song"* (the axis prints 16.27 to 24.84 sec). Three
label strips are drawn under the PCP display, and their label sequences read: *true* — E, G, D, Bm, G;
*align* — E, G, D, Bm, G; *recog* — E, G, Bm, Am, Em7, Bm, Em7. **The align strip carries the true
strip's label sequence with its tick marks at slightly different places; the recog strip carries labels
the true strip does not** — the two conditions' difference made visible. *No boundary time is transcribed
from this figure: the tick positions are read from a small drawing and only the label sequences are
recorded.*

**[FACT — the train18/train20 comparison, §3.1 discussion.]** *"For the PCP system, testing on the
training set (train20) gives a significant increase in accuracy for both alignment and recognition,
indicating that these models are able to exploit the 'cheating' information of getting a preview of the
test cases. By contrast, PCP_ROT achieves no benefit from training on the test set (and even does
significantly worse on recognizing 'Every Little Thing', which may reflect some pathological case in the
local maximum found by EM). As a general rule, if including the test data in the training set does not
significantly increase performance, we can at least be confident that the models are not overfitting the
data."*

### The paper's own conclusion and its stated limits (§4, §5)

**[FACT — §5 Conclusion, verbatim.]** *"Our experiments show that HMM models trained by EM on PCP
features can successfully recognize chords in unstructured, polyphonic, multi-timbre audio."* And, in
the same section: *"Although recognition accuracy is not yet sufficient to provide usable chord
transcriptions of unknown audio, **the ability to find time alignments for known chord progressions may
be useful in itself.** Moreover, the minimally-supervised EM training approach means that the
incorporation of large amounts of additional training data should be straightforward, since no manual
annotation is required."*

**[FACT — §4 Future Work, the four named directions.]** *More data and parameters* (*"the PCP_ROT chord
family models show no signs of overfitting, so employing more parameters, e.g. by using Gaussian mixture
models rather than single Gaussians, should achieve further accuracy improvements"*, with the obstacle
named as *"finding a reliable source for the associated chord sequences"*); *Frequency Resolution*
(*"our recognition system most likely does not have enough frequency resolution"*, remedy: an 8192-point
Hanning window); *Adaptive Tuning* (estimate the song's tuning and centre the PCP bins on it); *Different
Features* (autocorrelation of subband energy envelopes at long lags).

**[CONJECTURE — the authors', §3.2.]** That better major/minor discrimination *"might be achieved by
increasing the system's frequency resolution"*. Stated as a possibility and not measured.

**[CONJECTURE — the authors', §3.1 discussion.]** That PCP_ROT's worse recognition of "Every Little
Thing" under train20 *"may reflect some pathological case in the local maximum found by EM"*. Stated as a
possibility and not investigated.

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- Audio at 11 025 Hz, mono. **No notes, no spelling, no beat grid, no meter, no voices, no key
  signature, no tonality of any kind.** The 24-dimensional PCP vector per 100 ms frame is everything the
  model reads about the music.
- For TRAINING: a chord SEQUENCE per song, without timings — the whole point of the EM construction. The
  sequences come from a commercial transcription book mapped to the 147-label set.
- For the FORCED-ALIGNMENT condition at test time: **the chord sequence of the song being decoded**,
  supplied as the constraint that composes the HMM. This is an input the recognition condition does not
  have.
- For measuring: hand-marked chord boundaries, which exist for two songs only.

**What it HANDS downstream.**
- One chord label per 100 ms frame — equivalently a segmentation into chord regions on a 100 ms grid,
  each carrying one of the 147 labels or 'X'. Nothing else.
- **No rivals, no confidence, no posterior.** The Viterbi best path is the entire published output.
- No tonality, no scale degree, no inversion, no bass, no chord-tone assignment, no segment-length
  statement.

**Its own STATED SCOPE and limits.**
- **Domain:** audio; twenty early Beatles songs; two test songs.
- **Decision scope:** the chord label and where it changes. Tonality is not decided or mentioned as a
  quantity anywhere in the paper.
- **Vocabulary:** 147 chord labels defined, 32 occurring, plus an explicit 'X' for anything else.
- **Fitting:** flat-start EM, 13–15 iterations, on 18 songs; the same experiments repeated on all 20 as a
  declared optimistic ceiling. No held-out validation set beyond the two test songs, and no uncertainty
  of any kind is stated on any reported figure (#24).
- **Self-assessed:** *"recognition accuracy is not yet sufficient to provide usable chord transcriptions
  of unknown audio"* (§5).
- **Coupling:** the label sequence and the boundaries are decided by ONE Viterbi decode over a
  first-order HMM whose states are chords. There is no separate segmentation stage and no separate
  labelling stage.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Must argue against (the model family itself).** This is a per-frame first-order HMM with one state
  per chord: the *"before (every fixed grid)"* member of DP-C's candidate list, on a 100 ms grid. Its
  segment lengths are whatever the self-transition probabilities imply. **Nothing in it is a candidate
  for L2's score;** what makes the row an upgrade is the MEASUREMENT it supplies and the design contrast
  it draws, not machinery an L2 detail specification would adopt.
- **Adapt (parameter pooling by transposition, §2.5, and it is MEASURED).** The chord models are pooled
  across roots by rotating each chord's feature vector until the root is at position zero, averaging
  within the chord family, and rotating back. The measured effect is the largest in the paper: 26.3 →
  68.8 and 46.2 → 83.3 on forced alignment, 10.0 → 23.3 and 18.2 → 20.1 on recognition (Table 3, PCP
  against PCP_ROT, train18). **This is a third published instance of the same idea the slice already
  holds twice** — row 3's chord-given-key conditional pooled by transposition, and row 20's random
  key-shift augmentation justified by *"harmonic relations are independent of the key, as in roman numeral
  analysis"* — and here it is the pooling of the EMISSION rather than of a transition table. The record's
  own scale-degree-valued chord axis (D-526) is the same invariance expressed in the state space rather
  than in the fitting; a detail specification deciding how the emission's tables are counted has three
  measured precedents for pooling across the root.
- **Adapt (training from sequence-only supervision).** The whole EM construction exists because
  frame-level labels are expensive: *"we assume only that the chord sequence of an entire piece is known,
  but treat the chord labels of each frame as hidden values."* Our own ground truth is time-aligned, so
  the need does not arise as theirs does; but the construction is the published answer to *"what can be
  fitted when only the label sequence is known"*, and it is worth having on the record beside D-525's
  staged fit if a future table is ever counted from an un-aligned source.
- **Must argue against (one best path, no rivals).** The output is the single Viterbi path. The L2
  charter publishes *"per span, the rivals with their mass — including rivals that differ in where the
  boundaries fall"*, which this system does not produce even in principle from what it publishes. Fourth
  instance in the slice, after rows 11, 19 and 20.
- **Must argue against (the 100 ms frame grid).** Every boundary the system can place is a 0.1 s frame
  edge, against the L1 charter's change-point grid and the L2 charter's *"boundaries are a subset of L1's
  change points"*. Its figures are therefore for a decision on a different candidate set from L2's and are
  not comparable with any figure the record publishes.
- **A datum for the candidate-admission boundary condition (the L2 charter's second fixed clause).** The
  system defines 147 labels, sees 32, and carries an explicit **'X'** class for *"chords not covered by
  this set"* which is decoded like any other state and appears in the confusion matrices. A published
  precedent for an explicit none-of-the-above candidate, routed to L2's detail specification where the
  admission rule and its defense live.

## ★ Findings, routed and not applied

**(1) IDENTITY: a MILD finding.** The held document's title spells out *"Hidden Markov Models"* where the
bibliography's row 32 abbreviates *"HMMs"*; the authors match; and **no venue, page numbers or conference
line are printed**, only *"©2003 Johns Hopkins University"* in the permission box. So whether the held
file is the ISMIR 2003 proceedings text or the author copy the row's own tier names is **not
establishable from what is held**. Same shape as rows 29 and 11. **Routed to the bibliography
reconciliation. No verdict; nothing in the record turns on it.**

**(2) THE CARRIED QUESTION (c) IS ANSWERED: the input is AUDIO** — commercial recordings, twenty Beatles
songs, 11 025 Hz mono, PCP features. The domain travels as a caveat under the derivation's consequence
(ii) and the ADMITTED verdict stands for the method. **No verdict moved.**

**(3) ★ THE LOAD-BEARING FINDING — V10's VALUES RE-VERIFY EXACTLY, AND THE RECORD'S DESCRIPTION OF WHAT
THE TWO CONDITIONS ARE IS INVERTED AT THE PRIMARY.**

*The values.* `reading_pass/population.md` line 111 records V10's first item as *"68.8 vs 23.3 = Sheh &
Ellis 2003 (ISMIR), Table 3, PCP_ROT row, train18, 'Eight Days a Week': forced alignment 68.8% vs
recognition 23.3% frame accuracy on the same song"*. **Every part of that locator is correct at the
object**: Table 3, the PCP_ROT row, the first subrow (which the caption assigns to "Eight Days a Week"),
the train18 columns, align 68.8 and recog 23.3. **RE-VERIFIED, as rows 10, 11 and 19 re-verified their
V10 items.**

*The description.* `FRAMEWORK.md` DP-C (line 693) states the ground as *"frame accuracy of 68.8% when
boundaries are given against 23.3% when the same model must find them on the same piece"*; §S4(d) (line
1595) as *"Sheh and Ellis report frame accuracy of 68.8% when the boundaries are given and 23.3% when the
same model must find them, on the same song"*; the candidacy row (line 80) as *"its method is the
boundaries-given-versus-found design that measurement is about"*; and the slice derivation (line 65) as
*"DP-C's boundaries-given-versus-found primary"*.

**At the object it is the CHORD SEQUENCE that is given in the 68.8 condition, and the BOUNDARIES ARE
FOUND IN BOTH.** §2.4: *"in forced alignment… only the chord-change times are being recovered, since the
chord sequence is known"*; §3.1's discussion: forced alignment *"has only to determine the boundaries,
whereas recognition has to determine the chord labels too"*; and the procedural statement on page 4 of 7:
*"In the case of alignment, the chord sequence file is used to generate a simple composite HMM with
allowable transitions determined by the song's progression. Recognition must be able to accommodate any
sequence drawn from the set of training song chords."* **Three independent statements in the paper, in
three different places, all saying the same thing.** So the pair measures **label-sequence-given
against nothing-given**, not **boundaries-given against boundaries-found**. The two descriptions name
opposite halves of the problem as the given one.

*What this does NOT do.* It moves no value: 68.8 and 23.3 are right, on the same song, the same model and
the same training set. It does not reverse the direction of the comparison: more given, better result. It
does not touch the other three measurements DP-C's ground carries (rows 10, 19 and 11, each re-verified
at its own object by this slice's earlier sittings), nor C27, which is DP-C's first and independent
ground.

*What it DOES do, stated carefully because this is the whole finding.* DP-C asks whether segmentation is
decided **before, with or after** chord identity. A measurement of *boundaries given against boundaries
found* would bear on that question directly, because "boundaries given" is what a segment-first stage
hands to a labelling stage. **A measurement of chord-sequence-given against nothing-given does not bear
on it directly**: neither condition is a segment-first design, and neither is a with-design against a
before-design. What the pair establishes at the object is that **the two decisions are strongly
interdependent — knowing the label sequence raises frame accuracy on the same song from 23.3 to 68.8** —
which is an argument of the same kind as C27 and reaches DP-C's conclusion by that route, not by the route
the sentence states. **The verdict is not moved and no rival is re-opened; the ground's wording is wrong
about its own primary.**

*Why it is surfaced rather than absorbed.* The remedial commission §5 makes a corrected structural claim
bearing on a chosen design point's recorded ground a **STOP** — written up on its own and put to the user
before the reading continues past it. This is that write-up. **Nothing is amended: `FRAMEWORK.md`, the
candidacy row, the slice derivation, `population.md` and the findings surface all stand exactly as they
stand.** It is the same shape as the V4 divergence (`reading_pass/stop_v4_divergence_2026_08_30.md`),
one step milder: V4's figure was attached to the wrong row of its own table, and here the figures are
right and the sentence about them is wrong.

**(4) THE CARRIED QUESTION (b) IS ANSWERED: the HMM's implicit segment-length model is the EXPONENTIAL
one.** Row 20's statement (carried at the progress record) is that an HMM implies an exponential
length distribution with one state per chord, or a negative-binomial one with several states per chord.
**§2.2 states one state per chord in terms** — *"a hidden Markov model (HMM) with one state for each
chord distinguished by the system"* — and no multi-state or duration construction appears anywhere in the
paper. **So row 18's HMM carries the exponential shape**, which by row 11's §2.3 factorization test is the
shape a segmental decode does no work for, and which is the same shape as row 19's linear self-transition
term and row 20's exponential baseline. **No figure in the paper bears on the duration model**: no
segment-length statistic is reported, the transition matrix is not published, and the length distribution
is never named as a modelling choice. **The slice's three worked shapes for the length term are unchanged
by this row; what this row adds is that DP-C's own oldest measurement was taken under the weakest of
them.** Routed to L2's detail specification and to the findings surface's DP-C block as a datum.

**(5) AN OBSERVATION OF THIS READER'S, LABELLED AS SUCH BECAUSE THE PAPER DOES NOT STATE IT.** In the
forced-alignment condition the label sequence is fixed, so the only thing deciding where a boundary falls
is the emission likelihood together with the implicit exponential length prior of finding (4). **The 68.8
figure is therefore, read structurally, a measurement of what a per-frame emission plus a geometric length
prior can do for boundary placement when the labels are known.** The paper does not decompose it that way
and reports no ablation of the transition structure, so this is an inference from the model's form and not
a claim of the authors'. Routed as a question, with no verdict.

**(6) THE GROUND TRUTH IS TWO HAND-LABELLED SONGS, AND THE TRAINING LABELS ARE A SONGBOOK'S.** Frame
accuracy is measured against boundaries the authors hand-marked for two songs; the eighteen training
songs' chords come from a commercial transcription book mapped down to the label set (§3). Every cell of
Table 3 is one song under one condition, with no uncertainty stated (#24). **This bounds what the
68.8/23.3 pair can carry, in a direction the record does not currently state anywhere:** it is one song,
in one system, in one 2003 audio front-end. Routed to measurement design beside principle #21 and the
fourth instance of the annotation-bounds-the-figure pattern the slice has already recorded at rows 10, 29,
30 and 37/38.

**(7) THE ABSTRACT'S "AROUND 75%" IS NOT A TABLE CELL.** It is a round of the two test songs'
forced-alignment train18 accuracies (68.8 and 83.3; their mean is 76.05, derived here). Recorded so that a
later citation of this paper's headline figure is not taken for a measured cell. Routed to the findings
surface's DP-C block as a caution; **the record does not currently cite it, so nothing is owed.**

**(8) A DECLARED, MEASURED AND CORRECTLY-READ "CHEATING" CONDITION.** The authors run the whole experiment
a second time with the test songs in the training set, name it in advance as *"a performance ceiling in the
optimistic condition"*, and then read the result the honest way: the base PCP system gains from it, so it
is exploiting the preview; PCP_ROT does not, from which they conclude *"we can at least be confident that
the models are not overfitting the data"*. **A published instance of the fit/evaluation separation being
handled explicitly rather than assumed** — the opposite of the pattern rows 5, 8 and 30 supplied — routed to
measurement design beside D-097, principle #20 and D-574.

**(9) PARAMETER POOLING BY TRANSPOSITION IS THE PAPER'S LARGEST MEASURED EFFECT.** PCP → PCP_ROT moves
alignment from 26.3/46.2 to 68.8/83.3 and recognition from 10.0/18.2 to 23.3/20.1 (Table 3, train18). The
authors' stated mechanism is regularisation plus a larger effective training set per chord. **Third
published instance in the slice of the root-invariance idea** (rows 3 and 20 are the others), and the first
where it is the emission that is pooled and where the gain is the paper's headline. Routed to L2's detail
specification beside D-526 and the emission's table-counting question, with the domain stated.

**(10) NO TONALITY, AND NOT EVEN AS A MISSING PIECE.** Unlike rows 10 and 19, which decide no tonality and
say why, this paper does not raise tonality at all — it is absent from the model, the label set, the
experiments and the future-work list. **On L2's entangled decision it answers the boundary-and-label half
only, in the weakest form the slice holds.** The ADMITTED verdict and the group 2 placement stand; recorded
so the row is not later read as evidence about the tonality half.

**(11) NO RIVALS, NO CONFIDENCE, NO POSTERIOR PUBLISHED.** The output is one Viterbi path. Fourth instance
in the slice, after rows 11, 19 and 20, and the plainest: an exact normaliser exists for this model and
nothing is published from it. Routed as a datum beside D-006, D-008 and DP-K.

**(12) THE CONFUSION STRUCTURE IS MAJOR-AGAINST-ITS-MINOR.** §3.2 and Table 4: the frequent recognition
error is between a major chord and the minor chord on the same root, *"which differ only by the semitone
between major and minor third intervals"*, attributed to insufficient frequency resolution. **An
audio-specific failure with no symbolic counterpart** — our L0 gives the notes — recorded so the paper's
error analysis is not carried across domains. No verdict, nothing routed.

**No falsifier of a chosen design point, so no STOP of the falsifier class. Finding (3) is a STOP of the
corrected-structural-claim class under the remedial commission §5 and is put to the user with this
extract.**

## Centrality

**CENTRAL, on a narrow ground, and a SECOND INDEPENDENT EXTRACTION IS OWED.**

*The ground.* A ratified [FACT] rests on this paper at two places in `FRAMEWORK.md` (DP-C's ground at line
693 and §S4(d)'s exclusion of *segment first, then label* at line 1595, with DP3 at line 1805 repeating
it), and the pass verified its figure at V10. **This read re-verifies the values and corrects the
description of the experiment they come from** — finding (3) — which is a claim that carries load in an
L2 detail specification and against a design point's recorded ground, which is the commission's own test
for central.

*The ground on which NOT CENTRAL could be argued, stated so the verdict is challengeable.* The paper is
audio, popular music, 2003, twenty songs and two test songs, with no tonality, no notes, no spelling and no
uncertainty on any figure; its method is a plain first-order HMM that an L2 detail specification would
adopt nothing from; its figure was already VERIFIED by the pass; and the correction finding (3) makes is to
the record's WORDING and moves no verdict. On that reading the paper is a supplier of one measured figure —
the class the candidacy criterion excludes — and the row would be NOT CENTRAL with nothing owed.

*Why CENTRAL is chosen anyway.* The criterion admits a paper whose method a specification *"could adopt,
adapt, or have to argue against"*, and finding (3) means the record currently argues against the wrong
thing at DP-C's first-named measurement. Getting that right is a claim a detail specification carries, and
a second reader should check it independently: it is a reading of two prose passages against four sentences
of the record, and it is exactly the kind of claim the double extraction exists to catch if it is wrong.

## What this extract does NOT do

It amends no document. It moves no verdict in `reading_pass/candidacy_upgrades.md`, no placement in the
slice derivation, no design point in `FRAMEWORK.md`, no row of `reading_pass/population.md` and nothing in
`cowork_reading_pass_findings_2026_08_31.md`. It writes no open-items row and no decisions-register entry.
It lifts no gate: Ruling 1 of `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps *no derivation
before L2's slice of Task B is read*, and 22 of the 36 rows are still unopened after this one. It fetches
nothing: the ISMIR 2003 proceedings version, the seven cited works (Bartsch & Wakefield 2001, Fujishima
1999, Gold & Morgan 1999, Logan 2000, the *Paperback Song Series* transcriptions, Raphael 2002, Young et
al. 1997), the HTK toolkit and the WaveSurfer annotations were not fetched and are not read; only the held
file was.

---

*Provenance: Cowork, 2026-09-06, the tenth reading session of L2's slice, booted on
`cowork_handoff_entry_one_hundred_and_twenty_five.md` at tip `911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb`
(both ref files read with the file tools). Read before this extract: the ordinary session-start read
(`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md` whole, the derived gating answer with its
`gating_ids` list whole), the hundred-and-twenty-fifth handoff entry whole, the hundred-and-eighteenth
entry whole for its bridge-fault section, `reading_pass/l2_slice_reading_progress.md` whole,
`reading_pass/candidacy_upgrades.md` whole, both commissions whole, the row 20 extract at its banner,
identity, coupling-facts and adopt-or-argue sections for the form, the L2 slice derivation whole, the
bibliography's row 32, `FRAMEWORK.md` at the L2 charter (lines 386–425), the design points DP-A to DP-J
(lines 669–728), §S4(d) (lines 1580–1614) and DP3 (lines 1795–1814), and `population.md` §3's rows V3 to
V13. The staged tree was searched with `Grep` for "Sheh" and "Ellis" before extracting. The held PDF was
read as page images, all seven pages, with pages 1, 2, 4 and 5 re-read for the fact check. Every file was
read with the file tools from bridge-staged copies; no shell read repository content. No figure of this
project's own measurement is restated (#17f, D-431).*
