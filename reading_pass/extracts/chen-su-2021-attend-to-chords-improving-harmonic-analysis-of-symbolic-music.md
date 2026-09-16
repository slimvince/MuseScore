# EXTRACT — Chen & Su, "Attend to Chords: Improving Harmonic Analysis of Symbolic Music Using Transformer-Based Models" — Task B candidacy row 47, SECOND of the row's two papers, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All thirteen pages of the held PDF were read AT THE OBJECT: staged through the
> bridge and read with the file tools as page images. **No relay, no web-fetch read, no prompted
> extraction.** The held document prints journal page numbers 1–13 and a running header, so every
> location below is given as the printed section, table, figure or equation number together with the
> journal page.
>
> **★ ONE ROW, TWO PAPERS.** `reading_pass/candidacy_upgrades.md` row 47 (line 119) carries **two
> papers in one row** — the 2019 ISMIR "Harmony Transformer" and this one. **The decision was TWO
> EXTRACTS, one per held file**, on the ground that the commission's §4 makes the PAPER the unit of
> the form (*"Every population paper is read WHOLE. Per paper, one extraction file"*). The decision,
> its reason and the record's citation map for the row are stated ONCE, in the companion extract
> `reading_pass/extracts/chen-su-2019-harmony-transformer-incorporating-chord-segmentation-into-harmony-recognition.md`,
> and are not restated here (#6). **The ROW's centrality verdict and its second-pass debt are stated
> HERE, once, for the row.**
>
> **Where the record cites this paper.** Nowhere by name. The `Grep` of the staged tree recorded in
> the companion extract found **no occurrence of "Attend to Chords" outside the bibliography's own
> row (line 66) and this line's own files**, and **no `[FACT]` in the record names it; nor is any
> figure DP-A's or DP-C's ground cites a figure of this paper**, checked figure by figure at those
> two grounds. The bound on how far that check reaches is stated in the companion and not restated
> here (#6).
> The findings surface's *"Harmony Transformer v2"* (lines 186–187) **is this paper's model** — its
> Note 2 gives the implementation as `Harmony-Transformer-v2` — but the surface names neither the
> paper nor its authors, and the 62.1 figure it carries is BACHI's report of it at second hand.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — NO finding

Tsung-Ping Chen and Li Su, Institute of Information Science, Academia Sinica, TW; corresponding
author Tsung-Ping Chen (`tearfulcanon@iis.sinica.edu.tw`). Printed title, page 1: **"Attend to
Chords: Improving Harmonic Analysis of Symbolic Music Using Transformer-Based Models"**. The
journal's own citation block is printed at the head of page 1: *"Chen, T.-P., and Su, L. (2021).
Attend to Chords: Improving Harmonic Analysis of Symbolic Music Using Transformer-Based Models.
Transactions of the International Society for Music Information Retrieval, 4(1), pp. 1–13. DOI:
https://doi.org/10.5334/tismir.65"*, marked **RESEARCH**. The back matter on page 13 repeats it and
adds: *"Submitted: 10 May 2020 Accepted: 07 January 2021 Published: 24 February 2021"* and
*"Copyright: © 2021 The Author(s). This is an open-access article distributed under the terms of the
Creative Commons Attribution 4.0 International License (CC-BY 4.0)…"*, published by Ubiquity Press.

**The bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` line 66) names *Chen & Su,
"Harmony Transformer," ISMIR 2019; **"Attend to Chords," TISMIR 2021***, URL
`https://transactions.ismir.net/articles/10.5334/tismir.65`, held ✓, tier **CC**.

**What matches, at the object.** Authors, short title, venue, year, DOI and licence tier all match —
the row's *"Attend to Chords"* is the held title's own leading phrase, the venue TISMIR and the year
2021 are printed twice, the DOI resolves to the row's URL, and the printed CC-BY 4.0 matches the
row's CC tier. **The identity check closes with NO finding.** Keywords printed: *automatic chord
recognition; functional harmony recognition; symbolic music; Transformer; multi-head attention; chord
segmentation*.

**The input, established at §3.2: SYMBOLIC ONLY.** *"The musical pieces in the repertoire are
represented as binary piano rolls with the time resolution of one 16th note, resulting in sequences
of 88-dimensional feature vectors. A sliding window of length 128 (equal to 32 quarter notes) with a
hop size of 16 is applied to the piano rolls to generate the instances for recognition."* **No audio
anywhere** — unlike the companion, which carries both domains. So **no domain caveat under the
candidacy derivation's consequence (ii) applies to this half of row 47**: it is symbolic classical
piano music, our own input kind and close to our own repertoire.

**Structure of the held document:** five numbered sections (1 Introduction, with §1.1 Automatic Chord
Recognition, §1.2 ACR in Audio Domain, §1.3 ACR in the Symbolic Domain, §1.4 Functional Harmony
Recognition, §1.5 Attend to the Chords; 2 Transformer for Chord Recognition, with §2.1 Building
Blocks of Transformer, §2.2 BTC versus HT, §2.3 Improving the Transformer-Based Models; 3
Experiments, with §3.1 Testing Corpora, §3.2 Data Representation, §3.3 Experimental Setting, §3.4
Evaluation Metrics, §3.5 Results (§3.5.1 Ablation Study and Comparison of BTC and HT, §3.5.2
Improvement on the HT); 4 Discussion and Future Work; 5 Conclusion), then Notes (2), Acknowledgements,
Competing Interests and References. Four figures, four tables, five numbered equations. Thirteen
pages, 1–13.

**File:** `docs/research_papers/chen_su_2021_tismir_attend_to_chords.pdf` (2,915,635 bytes at the
listing).

## Claims, labeled

### ★ The authors' own statement of the Harmony Transformer's decision ORDER

**[FACT — §2.2's opening summary of the two models being studied, page 3. This is the passage that
settles the companion extract's finding (2) in the authors' own words rather than by this reader's
reading of the mechanism.]** Verbatim: *"the BTC utilized a self-attention mechanism to capture the
long-term dependency in musical sequences, and showed its ability to segment chord sequences; **the
HT estimated chord transitions (or chord boundaries), and then recognized chords via attending to the
segmentation-informed sequence.**"*

**And §1.5, page 2, in the same terms:** *"Recently, two Transformer-based models, the bi-directional
Transformer for chord recognition (BTC) (Park et al., 2019) and the Harmony Transformer (HT) (Chen
and Su, 2019), were proposed for the first time to tackle the ACR task."* — with §2.2 continuing:
*"In contrast to the BTC, the HT retains the encoder-decoder architecture for the sake of integrating
the chord change prediction into the chord recognition process."*

**[FACT — §2.2, page 4: the mechanism is unchanged from 2019.]** *"the HT includes a computational
block called regionalization (not shown in Figure 1c) to pass the chord change prediction to the
decoder; also, softmax-normalized layer weights are employed to compute the weighted sum of the
outputs from all repeated layers."* **So the hard-thresholded chord-change decision and the
region-averaged pooling the companion extract transcribes from the 2019 §3.3 and §3.4 are carried
into HT* unchanged; nothing in this paper alters the ORDER of the two decisions.**

### What HT* changes, and why

**[FACT — §2.3, pages 4–5.]** Two additions, both about locality and position, neither about the
segmentation decision. *(i) Intra-block intra-MHA*, equation (4): *"the intra-block intra-MHA unit
splits a sequence into B blocks of equal length m and captures the local dependency within each block
with the bidirectional intra-MHA"* — the stated motivation being that *"the frame sizes (which may be
on the scale of 100 milliseconds for audio and of a 16th note for symbolic music) are somewhat small
for encoding harmonic content"*, and that the MHAs otherwise *"access all the time steps of a
sequence in parallel at the expense of ignoring the sequential order."* m = 4. *(ii) Relative
positional encodings and positional attention*: *"the relative positional encodings enable the MHA to
consider the pairwise relationships between its input elements, while the positional attention
incorporates positional information directly into the attention process."* The fully-connected FFNs
are replaced by **convolutional FFNs** (equation 3). The authors' own reading of the combination:
*"the combination of the intra-block intra-MHA and the bi-directional intra-MHA functions in a way
similar to a convolutional recurrent neural network (CRNN) which captures local features with
convolutions first and models long-term structure with recurrences thereafter."*

### The experimental setting (§3, pages 5–7)

**[FACT — §3.1, the corpora.]** *"two corpora are used: the BPS-FH dataset and the Bach Preludes,
where symbolic music and human-annotated RN labels are provided. The former includes complete first
movements of the Beethoven Piano Sonatas (32 movements in total), and the latter consists of 24
preludes from the first book of Bach's Well Tempered Clavier. We use the BPS-FH dataset because it
was used to evaluate the HT. In addition, we include the Bach Preludes as it has similar properties
to the BPS-FH dataset (both comprise piano solos). **We leave other datasets (e.g., the ABC dataset
and the TAVERN dataset) for future work.**"* And: *"The analytic information of the Bach Preludes is
transcribed into the tabular format of the BPS-FH for unifying the notation system of the two
corpora. We additionally derive chord symbols from the RN annotations for the chord recognition task.
In sum, there are **11478 labels in the BPS-FH, and 2615 labels in the Bach Preludes**. All analyzed
chords in the two corpora are categorized into 10 classes, as shown in Table 2."*

**[FACT — Table 2, the quality mapping.]** Ten annotated qualities mapped to the major-minor
vocabulary: Major → M; Minor → m; Augmented → others; Diminished → others; Major Seventh → M; Minor
Seventh → m; Dominant Seventh → M; Diminished Seventh → others; Half-diminished Seventh → others;
Augmented Sixth → M. **A published mapping decision worth having on the record: a dominant seventh
and an augmented sixth are both graded as MAJOR, and every diminished and half-diminished sonority
falls into an 'others' class the evaluation excludes.**

**[FACT — §3.2, the chord vocabulary.]** *"For the chord recognition task, we use the maj-min chord
vocabulary (including 24 major and minor chords plus an additional 'others' class which is excluded
from evaluation). The mapping of the chord qualities is shown in Table 2. We choose this vocabulary
rather than other vocabularies of larger size for two reasons. First, both the BTC and the HT were
evaluated using the same vocabulary. Second, there is still room for improvement in ACR even using
this relatively small vocabulary."*

**[FACT — Table 3 and §3.2, the functional-harmony vocabularies. THIS IS WHERE THE 2019 FIVE-HEAD
FORM IS ABANDONED.]** *"For the functional harmony recognition task, we decompose the RN labels into
two parts, i.e., **the key and the RN**, whose vocabulary sizes are **42 and 5040** respectively, as
delineated in Table 3."* Table 3's own components: *Key* — *"21 tonics"* (*"{C, D, E, F, G, A, B} by
{♮, ♯, ♭}"*) × *"2 modes"* (*"{major, minor}"*) = **42**; *Roman Numeral* — *"9 primary degrees"*
(*"{1, 2, 3, 4, 5, 6, 7, ♭2, ♭7}"*) × *"14 secondary degrees"* (*"{1, 2, 3, 4, 5, 6, 7, ♯1, ♯3, ♯4,
♭1, ♭3, ♭6, ♭7}"*) × *"10 qualities"* × *"4 inversions"* (*"{root position, 1st, 2nd, 3rd}"*) =
**5040**. (9 × 14 × 10 × 4 = 5040, derived here from the table's own component lists; the table's own
figure agrees.) **The keys are SPELLED — 21 letter-and-accidental tonics, not 12 pitch classes — on
input that discards spelling.**

**[FACT — §3.3, the experimental setting.]** *"We evaluate the BTC, the HT, and the HT* on the chord
recognition and the functional harmony recognition tasks; and 4-fold cross validation is performed on
each corpus. To create cross-validation sets, we naively assign a fold id to a piece according to the
piece's id: fold_id = piece_id % 4. The training data are augmented via modulations (from 3 semitones
down to 6 semitones up), leading to 10 times the original amount of data. As a result, the amounts of
training and validation data are around (54320, 294) for the BPS-FH and (5380, 26) for the Bach
Preludes."* Hyperparameters: *"We set h = 4, d = 32, and n = 3 for the experiments"* (Table 1);
*"We set the number of repetitive layers to 2 for all models."* **And the sentence that decides how
the figures are read: *"During training, we set the dropout rate to 0.1; early stopping is applied
once the model's performance stops improving on validation data for 10 consecutive epochs, and we
report the best performance for evaluation."*** (Its footnote 2 is the code URL and nothing else.)

**[FACT — §3.3, the ablation variants.]** *BTC-singleBi*: *"the pair of uni-directional intra-MHAs is
replaced with a single bi-directional intra-MHA."* *BTC-FC*: *"the convolutional FFN is replaced with
a fully-connected FFN."* ***HT-noReg**: "the regionalization unit is removed."* *HT-noW*: *"only the
output of the final layer is used instead of the weighted sum of all the layers."* *CRNN*: *"10
one-dimensional convolution layers (convolving along the time dimension) with kernel size = 9 (equal
to a window size of 2 quarter notes) plus 1 bi-directional Long Short-Term Memory (LSTM) layer"*,
*"modified from the network of Micchi et al. (2020), whose number of parameters is made comparable to
the HT*"*, and *"we regard it as the benchmark for the HT* since they have a similar network
topology."*

**[FACT — §3.4, the two evaluation metrics.]** *"All models are evaluated in two aspects: 1)
frame-wise chord recognition accuracy, 2) chord segmentation quality. The former shows the capability
of a model to correctly predict chords at the frame level, while the latter assesses the predicted
chord sequences from the perspective of chord segmentation. We utilize the directional Hamming
distance (DHD) (Mauch and Dixon, 2010; Oudre et al., 2011) to evaluate the segmentation quality
(SQ):"* — equation (5): **SQ = 1 − max(DHD(**S**, **Ŝ**), DHD(**Ŝ**, **S**))**, with
DHD(**S**, **Ŝ**) = Σ_n (|**S**_n| − max_ñ |**S**_n ∩ **Ŝ**_ñ|) / Σ_n |**S**_n | — *"where **S**_n
denotes the frames belonging to the nth segment of the annotated segmentation **S**, and **Ŝ**_ñ
denotes the frames belonging to the ñth segment of the predicted segmentation **Ŝ**. The SQ value
reflects the similarity of two segmentations, ranging from 0 to 1. The higher the value, the better
the segmentation quality. In particular, a value of 1 indicates that the two segmentations are
exactly the same."*

### The measured results (§3.5, Table 4, page 8)

**[FACT — Table 4, transcribed cell by cell and re-read at the page for the fact check.]** Caption:
*"Evaluations with the BPS-FH dataset and the Bach Preludes. All the scores (in percentage) are
averaged over 4 validation sets; **the standard deviations of the scores are also provided.**"*
(Bold in the source marks the best value within each model family; it is reproduced below.)

**BPS-FH**

| Model | Chord symbol: Accuracy | Chord symbol: Segmentation | Functional: Key | Functional: Roman numeral | Functional: Segmentation |
|---|---|---|---|---|---|
| BTC | **82.46**±1.55 | **81.30**±1.08 | 77.65±1.83 | **37.98**±1.34 | 66.73±4.05 |
| BTC-singleBi | 82.16±1.66 | 80.78±1.39 | 75.96±0.79 | 35.77±1.85 | **68.83**±1.69 |
| BTC-FC | 82.06±1.83 | 81.24±1.26 | **78.40**±2.10 | 37.60±1.76 | 65.56±1.86 |
| HT | **83.19**±1.65 | **83.47**±1.22 | **77.94**±2.24 | **37.00**±2.88 | 71.93±2.72 |
| HT-noW | 83.06±1.58 | 83.26±0.71 | 77.13±1.78 | 36.84±2.39 | **73.53**±1.26 |
| HT-noReg | 83.19±1.31 | 83.33±1.26 | 76.70±1.26 | 35.33±1.79 | 70.51±1.16 |
| CRNN | 79.79±0.84 | 81.49±1.91 | 75.56±2.84 | 34.83±1.38 | 67.75±3.59 |
| **HT\*** | **83.98**±1.08 | **85.09**±0.96 | **79.07**±2.70 | **41.74**±2.63 | **75.50**±1.72 |

**Bach Preludes**

| Model | Chord symbol: Accuracy | Chord symbol: Segmentation | Functional: Key | Functional: Roman numeral | Functional: Segmentation |
|---|---|---|---|---|---|
| BTC | 74.12±0.12 | 77.20±3.64 | **48.63**±4.48 | **25.25**±1.76 | **64.19**±2.08 |
| BTC-singleBi | **75.67**±1.42 | **78.85**±4.81 | 46.24±5.90 | 23.35±1.99 | 60.40±6.25 |
| BTC-FC | 75.53±1.22 | 77.81±4.51 | 46.05±1.84 | 22.97±2.19 | 57.24±4.37 |
| HT | **77.18**±1.24 | 80.46±1.36 | **51.15**±2.47 | 23.75±2.20 | 66.82±4.52 |
| HT-noW | 76.51±1.45 | **81.14**±3.31 | 48.95±2.88 | **24.99**±1.32 | **67.61**±4.75 |
| HT-noReg | 76.33±1.23 | 80.76±4.40 | 50.62±1.93 | 23.82±2.43 | 65.23±4.80 |
| CRNN | 69.79±1.15 | 79.47±2.03 | 47.03±6.59 | 18.53±2.23 | 61.79±1.83 |
| **HT\*** | **78.54**±2.06 | **83.86**±2.24 | **56.28**±2.53 | **25.95**±1.67 | **73.60**±1.80 |

*Transcription check, run at the page twice and recorded because it is what makes the table safe to
cite.* Three of the paper's own §3.5 sentences cross-check the cells by counting, and all three
close against the transcription above. **(i)** *"In comparison with the BTC, the HT appears to be
more competent for it is more accurate in eight out of the ten measures (four from each corpus)."* —
counted at the table: on BPS-FH the HT exceeds the BTC on Accuracy, Segmentation, Key and Functional
Segmentation and falls short on Roman numeral (4 of 5); on the Bach Preludes the same four and the
same shortfall (4 of 5); **8 of 10, agreeing exactly.** **(ii)** *"the HT surpasses the HT-noW in
nearly all measures on the BPS-FH (while they are more or less comparable on the Bach Preludes)."* —
on BPS-FH the HT exceeds HT-noW on four of five, the exception being Functional Segmentation
(71.93 against 73.53). **(iii)** *"the HT outperforms the HT-noReg in four out of the five measures
on the BPS-FH and in three measures on the Bach Preludes."* — on BPS-FH four exceed and one is
**exactly equal** (Accuracy 83.19 both), which is what makes "four out of five" right rather than
five; on the Bach Preludes three exceed and two fall short. **Every one of the three counts closes
against the transcribed cells, in both corpora, which is the strongest cross-check any table in this
slice has carried.** No cell is transcribed that was not read at the image, and the two readings
agreed cell for cell. **The two 'others'-excluded conventions (§3.2) and the maj-min vocabulary bound
every Accuracy cell; no cell is a Roman-numeral-vocabulary accuracy except the two columns headed
Roman numeral.**

**[FACT — the authors' own readings, §3.5.1, page 7.]** On the BTC ablations: *"using single
bi-directional MHAs instead of uni-directional MHA pairs appears to lower the recognition accuracy
when the amount of data increases (the case of the BPS-FH) and when the complexity of the task
increases (the case of functional harmony). However, this may result from the fact that the number of
parameters in the model is half of that in the BTC."* On the layer weights: *"the HT surpasses the
HT-noW in nearly all measures on the BPS-FH … indicating that it might be beneficial to use
information from all the layers of the network."* On the regionalization unit: *"the HT outperforms
the HT-noReg in four out of the five measures on the BPS-FH and in three measures on the Bach
Preludes, **validating the employment of the regionalization unit**."* **And the sentence about
segmentation:** *"In particular, the worst HT variant even outperforms all the BTC variants in terms
of chord segmentation quality, **showing that the concurrent estimation of harmonic changes benefits
the outcome of chord segmentation**."*

**[FACT — §3.5.2, page 8.]** *"the HT* substantially outperforms the CRNN benchmark in all cases… In
comparison to the HT, the HT* obtains a consistent gain in overall performance, and the boost in
segmentation quality is especially notable, validating the proposed improvement on learning the
localized and position-related information. More strikingly, the HT* outperforms all the other models
in comparison and sets new records for the current experiments."* And the paper's own bound on that
claim, in the same paragraph: *"However, it should still be noted that these results are obtained by
evaluating the model on only two piano solo corpora. Experiments using more diverse data are required
for a more comprehensive assessment of the model."*

**[FACT — the attention-map observations, §3.5.2 and Figure 4, pages 8–9.]** *"two attention heads in
the intra-MHA of the decoder display distinct attention patterns: one head (on the left hand side)
appears to be aware of the chord regions, hence blocks of the attentive regions are formed along the
diagonal of the attention map; the other head emphasizes more on the harmonic changes, resulting in
several vertical lines traversing the attention map."* And for the inter-MHA: *"the attention map on
the left hand side reveals that the HT* is capable of recognizing the boundaries between the chords
(as there are many darker lines around the positions where the chords change); while the attention
map on the right hand side indicates that the tonic chord (F:m) and the dominant chord (C:M) put
emphasis on different parts of the encoder sequence."* The input segment is *"Beethoven's Piano
Sonata No. 1, MM. 1–8."* *No value is transcribed from these figures; the authors' own sentences are
what is recorded.*

### ★ The authors' own statement of DP-A's trade-off (§4, page 9)

**[FACT — verbatim, and it is the whole of the paper's statement on the question.]** *"Moreover,
designing reasonable output vocabularies is also important. **Chen and Su (2019) predict the
components of each RN label individually, while in the current experiments, they are combined into a
single RN. The former reduces the output size of each component, but makes the components somewhat
independent of each other; the latter alleviates the dependency issue but enlarges its output
vocabulary size. Therefore, it is required to mediate between the two approaches.** In addition, RN
analysis is a fundamental tool for music theorists to uncover the tonal structure of music; hence
human-in-the-loop approaches to functional harmony recognition are also valuable (Micchi et al.,
2020)."*

**[FACT — the paper's other stated future directions, §4, page 9.]** On ground truth: *"several
different annotations for the same harmonic entity are often equally viable due to the analytic
essence of the recognition process, and the subjectivity in the ground truth will affect the
evaluation of ACR systems (Ni et al., 2013). It is possible to take into account the relations
between different annotations or predictions, and develop new loss functions for optimizing a deep
learning model (Carsault et al., 2018)."* On segmentation: *"Chord segmentation quality is another
useful criterion for assessing frame-based ACR models, as the chord progressions obtained from these
models should not be fragmented. **Considering that chord boundary detection and chord recognition
are intertwined problems**, the ACR task may benefit from other advanced segmentation strategies,
such as hierarchical representation…, segmentation gates…, and segment-directed attention…. Instead
of the frame-wise chord recognition, it is also worthwhile to explore methods for recognizing chords
at a higher hierarchical level (Korzeniowski and Widmer, 2018)."* On data: *"currently available
datasets for symbolic ACR are usually small and homogeneous. More work devoted to creation of
symbolic datasets is thus welcomed."*

**[FACT — §5 Conclusion, page 10.]** *"We systematically studied two Transformer-based ACR models in
terms of model architecture, chord recognition accuracy, and chord segmentation quality… we further
improved the performance by leveraging the local context and the positional information of input
music. In addition, experimental results showed that multi-head attention has the potential to
capture various harmonically meaningful features in the scenario of ACR."*

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- A **binary piano roll at 16th-note resolution, 88 dimensions**, windowed at length 128 (32 quarter
  notes) with hop 16. **Spelling is discarded**; so are voices, dynamics, articulation and any meter
  beyond the 16th-note grid.
- For TRAINING: RN annotations, from which the key and RN labels, the chord symbols and (through the
  inherited HT encoder) the chord-change labels are all derived.
- Nothing at test time beyond the piano roll.

**What it HANDS downstream.**
- For the chord-recognition task: one label per 16th-note frame from a 24-class maj-min vocabulary,
  with an 'others' class **excluded from evaluation**.
- For the functional-harmony task: **two labels per frame** — a key out of 42 spelled tonic-and-mode
  classes, and a whole Roman numeral out of 5040.
- A chord-change sequence from the encoder, published only through the SQ score.
- **No rivals, no confidence, no posterior.** A softmax exists at every frame and nothing is
  published from it. Sixth instance in the slice, after rows 11, 19, 20, 18 and the companion.
- No chord-tone assignment, no elaboration relation, no segment-length statement, no inversion or
  figure published separately from the composite Roman numeral.

**Its own STATED SCOPE and limits.**
- **Domain:** symbolic classical piano solo — Beethoven's 32 first movements (11478 labels) and 24
  Bach preludes from WTC Book I (2615 labels). *"only two piano solo corpora"*, the authors' own
  bound.
- **Decision scope:** where the chord changes, what the chord is, and — on the functional task — what
  key and what Roman numeral. The key is one of two parallel outputs of the same forward pass; it
  never re-enters the chord decision.
- **Fitting:** 4-fold cross-validation by `piece_id % 4`; training augmented ×10 by modulation;
  **early stopping on the validation data and the BEST performance on that data reported** — so the
  reported figures are model-selected on the same sets they are reported over (see finding (5)).
- **Coupling:** unchanged from the companion — one network, two supervised losses, the chord-change
  decision hard-thresholded and committed before the label decision reads it through region
  averaging.

## What an L2 detail specification could adopt, adapt, or must argue against

- **★ Must argue against, WITH A MEASURED COST NOW ATTACHED (the committed-segmentation shape).**
  The companion extract establishes the shape; **this paper measures the machinery that carries it.**
  `HT-noReg` removes the regionalization unit — the one path by which the committed segmentation
  reaches the labelling — and finding (2) below shows every one of the ten resulting differences is
  smaller than the standard deviation the paper itself reports on the corresponding HT figure. **An
  L2 detail specification arguing against the "before" rival now has, on symbolic classical input, a
  published ablation of exactly that rival's coupling mechanism whose effect is not separable from
  its own reported spread.**
- **Adapt (the segmentation-quality metric, with a precision).** SQ = 1 − max of the two directional
  Hamming distances is the same family as the mir_eval directional-Hamming score row 19 uses, but it
  **collapses under- and over-segmentation into a worst-case maximum**, where row 19's convention
  keeps them separable and reports them apart. For a project whose own hard stop is duration-weighted
  and whose robust unit is a union of boundaries, **the separable form is the more informative one**
  and this paper's is the cautionary variant. Routed to measurement design beside D-115, D-606 and
  row 19's finding.
- **A datum, not a candidate (the composite Roman-numeral label).** The 5040-way composite is the
  authors' own answer to the incoherence DP-A names, and their §4 states the cost — *"enlarges its
  output vocabulary size"* — and asks for a middle way. **The record's own D-526 (a scale-degree-valued
  chord axis) and the AugmentedNet re-fusion §S4(a) cites are the same move**; this is a third
  instance, dated 2021 and by the lineage's founding authors. Routed to L2's detail specification and
  to the findings surface's DP-A block.
- **A datum for the tonality axis (42 SPELLED keys on unspelled input).** The key vocabulary is 21
  letter-and-accidental tonics × 2 modes, on a binary piano roll that carries no spelling — so the
  model must produce a spelled key label from unspelled evidence. **The same 42-spelled-key state
  space as row 30's**, reached from the opposite input contract. A datum beside DP-F, D-450 and row
  19's spelling-discarding finding; routed to L2's detail specification.
- **Must argue against (the fixed 16th-note grid and the frame-wise decision).** Every boundary is a
  16th-note edge and every decision is per frame — against the L1 charter's change-point grid. The
  authors themselves name the frame-wise formulation as a limitation and point at *"recognizing
  chords at a higher hierarchical level"*, citing row 20.
- **A datum, and a caution, on the grading conventions (Table 2).** Dominant seventh and augmented
  sixth are both graded MAJOR; every diminished, half-diminished and augmented sonority falls into an
  'others' class **excluded from evaluation**. Any accuracy cell above is therefore an accuracy over
  a repertoire with its most ambiguous sonorities removed. Routed to measurement design.

## ★ Findings, routed and not applied

**(1) ★ THE COMPANION'S FINDING (2) IS SETTLED IN THE AUTHORS' OWN WORDS, NOT ONLY BY THIS READER'S
READING OF THE MECHANISM.** The companion extract reads the 2019 model's mechanism — a
separately-supervised chord-change head, hard-thresholded at 0.5, then region-averaged into the
decoder — as deciding the segmentation BEFORE the labelling and training the two together. **§2.2 of
this paper says it in the authors' own summary of their own earlier model: *"the HT estimated chord
transitions (or chord boundaries), **and then** recognized chords via attending to the
segmentation-informed sequence."*** So the candidacy row's *"decides segmentation and labelling
together"* is imprecise against a sentence the same authors wrote about the same model. **This moves
no verdict** — the row stays ADMITTED, more squarely rather than less, under the derivation's
consequence (i) — **and it moves nothing in `FRAMEWORK.md`**, which cites neither paper at DP-C.
Recorded here because the companion's finding is materially strengthened by it, and pointed at from
the companion (#6).

**(2) ★ THE MECHANISM THAT MAKES THE LABELLING SEE THE COMMITTED SEGMENTATION IS ABLATED, AND EVERY
ONE OF ITS TEN MEASURED EFFECTS IS SMALLER THAN THE PAPER'S OWN REPORTED SPREAD.** `HT-noReg` is the
HT with the regionalization unit removed (§3.3). Differences below are **HT minus HT-noReg**, so a
positive number means the regionalization unit helped; each is set against the standard deviation
Table 4 reports **on the HT figure it is taken from**.

*BPS-FH:* Accuracy 83.19 − 83.19 = **0.00** (σ 1.65); Chord-symbol Segmentation 83.47 − 83.33 =
**+0.14** (σ 1.22); Key 77.94 − 76.70 = **+1.24** (σ 2.24); Roman numeral 37.00 − 35.33 = **+1.67**
(σ 2.88); Functional Segmentation 71.93 − 70.51 = **+1.42** (σ 2.72).
*Bach Preludes:* Accuracy 77.18 − 76.33 = **+0.85** (σ 1.24); Chord-symbol Segmentation 80.46 −
80.76 = **−0.30** (σ 1.36); Key 51.15 − 50.62 = **+0.53** (σ 2.47); Roman numeral 23.75 − 23.82 =
**−0.07** (σ 2.20); Functional Segmentation 66.82 − 65.23 = **+1.59** (σ 4.52).

**All ten differences are smaller in absolute value than the standard deviation reported on the HT
cell each is taken from**, and two of the ten run the other way. Every difference above is derived
here from the cells transcribed in this file and from nothing else, with the sign convention stated;
the paper states none of them. **The paper nevertheless reads the same comparison as *"validating the
employment of the regionalization unit."***

*Stated carefully, because the arithmetic must not be overclaimed.* A standard deviation across four
folds is **not** a confidence interval and this comparison is **not** a significance test. What is
established is only this: **the paper's own reported spread is, in every one of the ten cells, at
least as large as the effect the paper attributes to the mechanism** — which is what principle #24
asks a reader to notice, and which the paper's own sentence does not. **Nothing here says the
mechanism does nothing; it says the paper's numbers do not separate it from its own noise.**

*Why it matters to us and where it is routed.* The regionalization unit is the ONLY path by which the
committed segmentation reaches the labelling in this architecture. So this is the nearest thing the
slice holds to a measured answer to *"what does a committed segmentation buy the labelling?"* on
**symbolic classical input**, and the answer is: not enough to separate from the fold-to-fold spread
on either corpus. **Routed to the findings surface's DP-C block, beside the rival-shaped BACHI item
which this row's papers are the named comparable for, and to L2's detail specification. No verdict
moved and no design point touched: DP-C's ground is C27 and the four measurements at rows 10, 11, 19
and 18, none of which is this.**

**(3) ★ THE AUTHORS ABANDON THE FIVE-HEAD FORM AND STATE DP-A's TRADE-OFF IN THEIR OWN WORDS — WHICH
IS WHY `FRAMEWORK.md` §S4(a)'s UNIVERSAL IS FALSE AND ITS ARGUMENT IS STRONGER THAN IT STATES.**
§4's sentence is quoted in full above: the 2019 paper *"predict[s] the components of each RN label
individually, while in the current experiments, they are combined into a single RN. The former
reduces the output size of each component, **but makes the components somewhat independent of each
other**; the latter alleviates the dependency issue but enlarges its output vocabulary size."*

*The consequence for the record, stated at the width the companion's finding (3) sets out.*
`FRAMEWORK.md` §S4(a) line 1553 says *"Every system from Chen and Su 2018 onward predicts key,
primary degree, secondary degree, quality and inversion as separate heads"*. **At the object this
paper does not**: Table 3 gives two outputs, a 42-way key and a 5040-way composite Roman numeral.
**The universal is false of the lineage's own founding authors' 2021 system.** And §S4(a)'s next
sentence — *"Every later system adds machinery to undo the separation"* — names AugmentedNet,
ChordGNN, AnalysisGNN and RNBert but **not this paper, which is an instance of it and is dated
earlier than three of the four** — *the three derived by year at the bibliography: ChordGNN 2023,
RNBert 2024, AnalysisGNN 2025. AugmentedNet is also 2021 (this paper prints "Published: 24 February
2021"; AugmentedNet is ISMIR 2021) and the order within that year is NOT established from anything
read here, so it is left undetermined rather than counted either way.* So the passage both overstates its universal and understates its
own evidence, and correcting it would **strengthen DP-A**, whose live text (lines 671–683) carries no
universal at all and is untouched by this.

**NOTHING IS AMENDED.** §S4(a) is the sealed first-stage text, and this is a precision of the same
class as row 27's finding that *"Appendix B's sealed first-stage draft names Catteau by name where the
live charter says 'another'"*. Routed to the findings surface's DP-A block and put to the user with
this extract.

**(4) THE CARRIED ITEM (c) IS ANSWERED FOR BOTH OF THE ROW'S PAPERS: NO SEGMENT-LENGTH TERM OF ANY
KIND.** This paper changes the attention and the positional encoding and leaves the segmentation
machinery untouched (§2.2, §2.3). There is no duration distribution, no length feature, no maximum
segment length and no transition cost between adjacent regions in either paper. **Row 47 therefore
adds a fourth possibility to the slice's three worked shapes — modelling the length not at all** —
and the reasoning is stated in the companion's finding (5) and not restated here (#6).

**(5) THE REPORTED FIGURES ARE MODEL-SELECTED ON THE SETS THEY ARE REPORTED OVER.** §3.3: *"early
stopping is applied once the model's performance stops improving on validation data for 10
consecutive epochs, and **we report the best performance for evaluation**"*, and Table 4's caption:
*"All the scores … are averaged over 4 **validation** sets."* **No third, untouched split is
described anywhere.** With validation sets of around 294 (BPS-FH) and 26 (Bach Preludes) instances,
the selection is over few data. This is the fit/evaluation pattern rows 5, 8 and 30 supplied, in its
model-selection form rather than its parameter-fitting form; it is the opposite of row 18's declared
and correctly-read "cheating" condition. **Routed to measurement design beside D-097, D-574,
principle #20 and the earlier instances. It does not move any figure above; it bounds what they
mean.**

**(6) THE FIRST PAPER IN THIS SLICE TO CARRY AN UNCERTAINTY ON EVERY REPORTED FIGURE (#24).** Every
one of Table 4's eighty cells prints a standard deviation across the four folds. The slice has
recorded *"no stated uncertainty"* at rows 18, 19, 20, 30 and the companion; **this is the first
counter-instance**, and it is what makes finding (2) derivable at all. **Recorded as a positive
instance rather than a defect**, and routed to measurement design as the pattern to want: a paper
whose own spread is printed is a paper whose ablations a reader can grade.

**(7) THE TWO CORPORA'S FUNCTIONAL FIGURES ARE FAR APART AND THE PAPER DOES NOT ACCOUNT FOR IT.**
The best model's Roman-numeral accuracy is **41.74** on BPS-FH and **25.95** on the Bach Preludes,
and its key accuracy **79.07** against **56.28** — on two corpora the paper introduces as having
*"similar properties … (both comprise piano solos)"*. The Bach Preludes carry 2615 labels against
BPS-FH's 11478, and their per-fold training set is roughly a tenth the size. **The paper offers no
explanation and runs no experiment separating repertoire from data quantity.** Recorded as a bound on
reading either corpus's figure as a statement about symbolic classical music generally, and routed to
measurement design; it is also a datum for our own corpus-expansion decisions (D-500) that a
Bach-keyboard corpus of this size supports materially lower Roman-numeral accuracy in a
current-architecture system than a Beethoven-sonata corpus does.

**(8) TWO NAMED CORPORA LEFT FOR FUTURE WORK ARE CANDIDACY ROWS OF OURS.** §3.1: *"We leave other
datasets (e.g., the ABC dataset and the TAVERN dataset) for future work."* Those are rows 54 and 53
of `candidacy_upgrades.md`, both NOT ADMITTED there as corpora and both already routed at principle
#21 / D-474. Recorded as a datum for the measurement-design routing and for OI-179's own reading of
which corpora carry dual annotation; **nothing is carried out of it about either corpus.**

**(9) THE AUTHORS NAME BOUNDARY DETECTION AND CHORD RECOGNITION "INTERTWINED PROBLEMS".** §4:
*"Considering that chord boundary detection and chord recognition are intertwined problems, the ACR
task may benefit from other advanced segmentation strategies."* **This is a published-position
statement of the interdependence C27 argues and which row 18's finding (3) shows DP-C's first-named
measurement actually establishes** — from authors whose own system takes the "before" route. Recorded
as an ENRICHES-shaped datum for DP-C's chosen "with", routed to the findings surface's DP-C block,
**and explicitly NOT merged with row 18's finding (3), which is open with the user** (the progress
record's carried item (d)).

**(10) NO TONALITY FEEDS THE CHORD DECISION.** The key is one of two parallel per-frame outputs and
is never consumed by the Roman-numeral head or by the chord-symbol head. So on L2's entangled
decision this row answers the boundary-and-label half and **emits** a tonality without **using** it —
a third shape beside rows 10 and 19 (which decide no tonality at all and say why) and row 18 (which
does not raise it). Recorded so the row is not later read as evidence about the coupling; routed to
the findings surface's DP-B and DP-E blocks as a datum with no verdict.

**No falsifier of a chosen design point, so no STOP of the falsifier class. Findings (1) and (3) —
with the companion's findings (2) and (3), which are the same two — are corrected structural claims
and are put to the user with these extracts; nothing is amended and nothing is applied.**

## Centrality — stated ONCE for the ROW

**NOT CENTRAL, and NO second independent extraction is owed — with the ground on which CENTRAL could
be argued stated in full so the verdict is challengeable at this row.**

*The ground for NOT CENTRAL.* The commission's test for central is a paper *"whose claims would carry
load in a detail specification or against a design point"*. **No ratified text NAMES either of row
47's papers, and neither DP-A's nor DP-C's cited figures are theirs** — the searches and the
figure-by-figure comparison that establish this, and the bound on how far they reach, are the
companion extract's citation-map block and are not restated here (#6). The one near-miss,
*"Harmony Transformer v2 62.1"*, is BACHI's report of it inside a RELAYED read, carrying a figure
neither paper contains. Nothing in
either paper is machinery an L2 detail specification would adopt: the architecture is a Transformer
over a fixed 16th-note or 100 ms grid with a hard-thresholded boundary head, publishing one best label
and no rivals. And the two corrected claims the reading produced — the candidacy row's *"together"*
and §S4(a)'s *"every system"* — **correct a derivation file's reason and a sealed first-stage
sentence, and move no verdict in either direction**.

*The ground on which CENTRAL could be argued, stated rather than waved away.* Finding (2) is a
measured ablation of a committed segmentation's coupling mechanism on symbolic classical input, and
DP-C is a chosen design point about exactly that placement; a detail specification arguing against the
"before" rival could cite it, which is the commission's own test. Against that: the figures are not
separable from the paper's own reported spread — which is what makes the finding a **bound on what can
be claimed** rather than a claim — and a reader who cited it as evidence FOR our chosen "with" would be
citing an inconclusive ablation as a result. **A claim that cannot be carried does not carry load**,
which is why NOT CENTRAL is chosen.

*What follows.* No second independent extraction is owed for either of row 47's papers, on the same
footing as rows 3 and 29, whose centrality verdicts are likewise challengeable at the progress record.
**If the user reads finding (2) as load-bearing for DP-C, the verdict flips to CENTRAL and a second
extraction becomes owed** — which is stated here so the choice is his and visible.

## What this extract does NOT do

It amends no document. It moves no verdict in `reading_pass/candidacy_upgrades.md`, no placement in
the slice derivation, no design point in `FRAMEWORK.md` — live or sealed — no row of
`reading_pass/population.md` and nothing in `cowork_reading_pass_findings_2026_08_31.md`. It writes no
open-items row and no decisions-register entry. It lifts no gate: Ruling 1 of
`cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps *no derivation before L2's slice of Task B
is read*, and 21 of the 36 rows are still unopened after this row. It fetches nothing: the BPS-FH and
Bach Prelude data, the authors' two GitHub repositories, and every one of the cited works — Park et
al. 2019 (the BTC), Vaswani et al. 2017, Devlin et al. 2019, Micchi et al. 2020, Masada & Bunescu 2017
and 2019, Korzeniowski & Widmer 2016/2017/2018, Sheh & Ellis 2003, Mauch & Dixon 2010, Oudre et al.
2011, Ni et al. 2013, Carsault et al. 2018, Devaney et al. 2015, Neuwirth et al. 2018, Tymoczko et al.
2019 among them — were not fetched and are not read; only the held file was. **Row 18's finding (3)
is open with the user and is neither applied, restated as settled, nor built on here**; where this
row's own text bears on DP-C's ground it is recorded beside it, unmerged (finding (9)).

---

*Provenance: Cowork, 2026-09-06, the eleventh reading session of L2's slice, booted on
`cowork_handoff_entry_one_hundred_and_twenty_six.md` at tip
`911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb` (both ref files read with the file tools). The session's
full read list is in the companion extract's provenance and is not restated here (#6). The held PDF
was read as page images, all thirteen pages, with page 8 re-read for the fact check. Every file was
read with the file tools from bridge-staged copies; no shell read repository content. No figure of
this project's own measurement is restated (#17f, D-431); every arithmetic difference in finding (2)
is derived from the cells transcribed in this file, with its sign convention stated.*
