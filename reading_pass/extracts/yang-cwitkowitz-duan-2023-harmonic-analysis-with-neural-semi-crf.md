# EXTRACT — Yang, Cwitkowitz & Duan, "Harmonic Analysis with Neural Semi-CRF" (Harana) — Task B candidacy row 19, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eight pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints page numbers 676–683 (the proceedings' pagination); **every location below is
> the printed page number and the section, equation, figure or table number as printed.**
>
> **Why this paper and its place in L2's slice.** It is row 19 of `reading_pass/candidacy_upgrades.md`
> (line 81), ADMITTED there as *"The neural semi-CRF; DP-C's largest-ablation-contributor evidence, and
> a current candidate architecture for L2."* `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4
> (line 66) places it in L2's slice: *"A current candidate architecture for L2; DP-C's ablation
> evidence."* It is third in group 2 of the proposed reading order ("segmentation decided with the
> labelling": rows 10, 11, 19, 20, 18, 4, 47). **The record cites this paper at one ratified place and
> one verified figure:** `FRAMEWORK.md` §9 DP-C (lines 696–697): *"the joint segmentation component the
> single largest contributor in a third system's ablation"* [FACT — each reported by the work named];
> and the findings surface's verification table carries **V10 VERIFIED**, whose
> `reading_pass/population.md` row (line 111) reads *"Largest ablation contributor = Harana (Yang et al.
> 2023), §5.3 + Table 2: 'Among the missing components, semi-CRF leads to the largest performance drop…
> an indispensable component to capture boundary information'"*. `FRAMEWORK.md` §14.1 (lines
> 1008–1010) names *"the two symbolic systems built on it [the semi-Markov formalism] whose measured
> gains over event-level tagging are quoted at DP-C"* — this paper is the second of the two, row 10 the
> first. The progress record carries two things from row 11 to this row (its "Next" section): re-verify
> V10's figure at the object, and note which semi-CRF feature form this paper uses. Ruling 1 of
> `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before L2's slice
> of Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — NO finding

Qiaoyu Yang, Frank Cwitkowitz and Zhiyao Duan, University of Rochester. Printed title: **"HARMONIC
ANALYSIS WITH NEURAL SEMI-CRF"** (p. 676). The running header on pp. 677–683 prints *"Proceedings of the
24th ISMIR Conference, Milan, Italy, November 5-9, 2023"*; the licence block on p. 676 prints *"© Q.
Yang, F. Cwitkowitz, and Z. Duan. Licensed under a Creative Commons Attribution 4.0 International
License (CC BY 4.0)"* with the attribution line naming *"Proc. of the 24th Int. Society for Music
Information Retrieval Conf., Milan, Italy, 2023"*. The bibliography's row
(`docs/research_papers/BIBLIOGRAPHY.md` line 33) names *Yang, Cwitkowitz & Duan, "Harmonic Analysis
with Neural Semi-CRF" (Harana), ISMIR 2023*, the ISMIR archive URL, held ✓, tier *CC (recent ISMIR CC
BY)*. **Title, authors, venue, year and licence tier all match at the object.** The name "Harana" is
the paper's own (p. 676, Abstract: *"a novel approach named Harana"*), not printed in the title. Eight
printed pages (676–683); eight numbered sections (1 Introduction; 2 Related Works; 3 Methods, with §3.1
Data Representation — §3.1.1 Symbolic Music Input, §3.1.2 Harmony — §3.2 Semi-CRF, §3.3 Frame-Level
Estimation, §3.4 Attention-Based Score Function, §3.5 Absence Score, §3.6 Optimization; 4 Experiments,
with §4.1 Data, §4.2 Implementation Details, §4.3 Evaluation Metrics, §4.4 Baseline Models; 5 Results,
with §5.1 Frame-Level Accuracy, §5.2 Segmentation Quality, §5.3 Ablation Studies; 6 Conclusions; 7
Acknowledgements; 8 References, 33 entries); two figures, four tables, fifteen numbered equations, one
footnote (the GitHub URL). Nothing in the record's characterisation of the paper is contradicted by its
identity.

**File:** `docs/research_papers/yang_cwitkowitz_duan_2023_ismir_harana_neural_semi_crf.pdf` (318,293
bytes at the listing).

## Claims, labeled

### What the method decides, and from what

**★ [FACT, p. 676 Abstract and §1; p. 677 §3] The model decides a SEGMENTATION of the piece into
harmonic regions and a LABEL per region, TOGETHER, in one semi-CRF decode over a neural score.**
*"we introduce a novel approach named Harana, to jointly detect the labels and boundaries of harmonic
regions using neural semi-CRF"* (Abstract); *"Targeting the two indispensable components of harmonic
analysis simultaneously, we propose an approach to jointly predict the boundaries and labels of
harmonic regions using neural semi-Markov conditional random field (semi-CRF)"* (§1, p. 676). The
three-stage structure the paper states for itself (§3, p. 677): *"we first estimate the harmony
(including root, quality, and pitch activation in this work) at the frame-level; then we aggregate the
frame-level estimation into region-level segment scores based on candidate segments; finally, we use
semi-CRF to find the best segmentation candidate and its corresponding labels."*

**★ [FACT, p. 677 §3.1.2] The label is a (ROOT, QUALITY) pair. NO TONALITY is decided, and the paper
says why in terms: the full Roman-numeral label space is too large, and deciding the components
independently is incompatible with a semi-CRF because every component's boundaries must coincide.**
*"A popular representation of music harmony in symbolic music is the Roman numeral encoding, where the
full harmonic context of a label, including tonic and degree, is considered [22]. However, the
combination of all the components produces 47k different harmony labels, which is intractable for a
classification model with limited training data. A possible solution is to classify each harmony
component independently, but this is incompatible with semi-CRF because the boundary of each component
must be the same. As a compromise, we use a subset of the harmony components, root and quality, and
model them jointly."* Root: a 12-d one-hot over pitch classes; quality: a 10-d one-hot over *"10
commonly used classes"* (the classes are not enumerated in the held document); in addition, a pitch
class activation vector, 12-d multi-hot, *"circularly shifted from the pitch-class activation vectors
rooted at C"*, used as a harmony representation inside the score function. **So the label is
unspelled (12 pitch classes) and tonality-free; the same tonality-absent shape row 10's extract
records for Masada & Bunescu.**

**★ [FACT, p. 677 §3.1.1] The input is a FIXED METRICAL FRAME GRID — frames of one eighth of a beat —
each frame a 24-d vector: a 12-d pitch-class distribution weighted by duration, and a 12-d one-hot of
the bass (lowest) note's pitch class.** *"we slice it into short frames of one eighth of a beat long.
We use beat instead of note duration in order to represent the basic time unit because music with
different meters may have different distributions on the note length. The pitch information in each
frame is summarized with a 12-d pitch class distribution vector, which describes the normalized
distribution of the duration of each pitch class in the frame. To help distinguish between harmonies
with the same pitch class vector, we also include the bass note (the lowest note) in the input to the
model; it is represented as a 12-d one-hot vector indicating the bass pitch class in each frame."* The
candidate boundaries are therefore frame positions on this grid, not note onsets or offsets; and the
spelling the score carries is discarded at input.

**★ [FACT, p. 677 §3.2; p. 678 eqs. 1–3] The semi-CRF, as this paper states it, and the FORM its
segment score takes — this is the answer to the question carried from row 11.** A sequence of frames
X = ⟨X_1 … X_N⟩; segments Y_i = (u_i, v_i, l_i) — onset, offset, label — contiguous and non-overlapping.
P(Y|X) = e^{W F(Y,X)} / Z(X) (eq. 1) is generalised to a neural score S(Y,X): P(Y|X) = e^{S(Y,X)} / Z(X)
(eq. 2), Z summing over *"all possible segmentation and labeling of the input sequence"*. Then: *"With
the assumption that the harmony labels are Markovian given the music input, the score function could be
decomposed into the sum of segment-level scores that are dependent only on the current and the
previous segments. S(Y,X) = Σ_{i=1}^{K} S_i(Y_i, X; Y_{i−1}) (3). To simplify the notation, we treat
Y_{i−1} as a parameter for the i-th segment's score function and omit it in the following sections."*
**The general statement (eq. 3) is row 11's eq. 2 — the segment score may depend on the previous
segment. But the score the paper actually builds does NOT: its content score (eqs. 6–7, 11) is a
function of the candidate segment and its own label alone, and the previous label enters ONLY through a
separate transition score (eq. 8) read from a pre-computed table.** That is the "weak" form row 10's
extract records for Masada & Bunescu (following Muis & Lu 2016) — label-independent segment features
plus separate label-transition features — reached here by construction rather than named. **Of the
three semi-CRF papers in the slice, then: row 11 (the formalism) admits previous-label-conditioned
segment scores; rows 10 and 19 (both musical systems) both use the weak form.**

**★ [FACT, p. 678 §3.3, eq. 4; Figure 2 p. 679] The frame-level front end is a DenseNet–GRU–MLP
producing, per frame, a root distribution (softmax), a quality distribution (softmax) and a pitch-class
activation (sigmoid).** *"Followng Micci et al. [23], the frame-level estimation of harmony information
is achieved with a DenseNet-GRU architecture."* (as printed) — eq. 4: E(n) = MLP(GRU(DenseNet(X_n)));
D̂_R(n) = Softmax(FC_R(E(n))); D̂_Q(n) = Softmax(FC_Q(E(n))); P̂C(n) = Sigmoid(FC_PC(E(n))).

**★ [FACT, p. 678 §3.4, eqs. 5–7] The segment content score is an ATTENTION-weighted similarity between
the candidate label's representation and the frames of the candidate region.** The stated motivation:
*"A simple method would be taking the average or the mode, but we note that a harmonic region is not
likely to contain homogeneous harmonic content. In order to dynamically weigh the harmonic importance
of each frame within a region, an attention module is proposed to focus on the frames that are most
similar to the candidate harmony label."* Scaled dot-product attention (eq. 5, citing [24]) with the
candidate label's harmony representation H(l_i) as query and the estimated frame-level harmony sequence
Ĥ(u_i : v_i) as both key and value gives the candidate-informed embedding Ĥ_CI(Y_i) (eq. 6); the
similarity score is the dot product S^H_i(Y_i, X) = H(l_i)^T Ĥ_CI(Y_i) (eq. 7, p. 679), computed for
each harmony representation H ∈ {root D_R, quality D_Q, pitch-class activation PC}.

**★ [FACT, p. 679 §3.4, eq. 8] The transition score is a PRE-COMPUTED table of frame-level transition
log-probabilities counted from the training ground truth — not a learned parameter — and it carries a
LENGTH-PROPORTIONAL self-transition term.** *"To further model the transition probability between
adjacent harmony labels and enforce more inductive bias in decoding, a transition score between segments
is computed: S^T_i(Y_i) = T[l_{i−1}, l_i] + (v_i − u_i) T[l_i, l_i] (8), where T is the transition matrix
containing log-probabilities of harmony transitions at the frame level. It is pre-computed from the
ground-truth labels in the training data."* The segment score (eq. 9): S_i(Y_i, X) = Σ_H S^H_i(Y_i, X) +
λ S^T_i(Y_i), λ *"a hyperparameter to balance the two score components"*; §4.2 (p. 680): *"The λ in Eq.
(12) is chosen empirically to be 0.001."*

**★ [FACT, p. 679 §3.5, eqs. 10–12] The ABSENCE score: the complement of the input pitch-class vector
is passed through the same front end, and the resulting "inactive" harmony estimate is compared with the
candidate label, with the similarity to be minimised.** Motivation in the authors' words: *"this
comparison may not be robust when there are many non-chordal notes or missing chordal notes in the
estimation. In this case, the estimated class distributions D̂_R and D̂_Q in Eq. (4) would be relatively
flat and the pitch class activation vector P̂C would not align well with a chord template … we introduce
an absence score to allow the model to filter out pitch activations that are not active within the input
music, the majority of which represent non-chordal notes that should not intersect with chordal notes of
the underlying harmony."* X_n[1:12] = 1 − X_n[1:12] (eq. 10); AS^H_i(Y_i, X) = −H(l_i)^T Ĥ^inact_CI(Y_i)
(eq. 11); the complete score S_i(Y_i, X) = Σ_H S^H_i(Y_i, X) + AS^H_i(Y_i, X) + λ S^T_i(Y_i) (eq. 12).
(The held text writes the absence term inside the sum's scope ambiguously; the equation as printed
places one AS^H term beside the sum.)

**★ [FACT, p. 679 §3.6, eq. 13] Learning is exact conditional maximum likelihood over labeled
segmentations; inference maximises the score; both use the original semi-CRF's dynamic programming.**
*"NLL(θ) = −log P_θ(Y|X) = log(Z_θ(X)) − S_θ(Y,X) (13)"*; *"During inference, where only the input music
frames are provided, the goal becomes finding the correct segmentation and the corresponding labels that
maximize the probability P(Y|X). Since the normalization factor as a sum of exponential scores stays
positive, maximizing the score function S(Y,X) suffices to decode the segments and labels. In both
training and inference, we used the algorithms based on dynamic programming proposed in the original
semi-CRF paper to expedite the optimization process [6]."* **No maximum segment length L is stated
anywhere in the held document**; the conclusion's complexity statement (below) is what the paper says
about cost.

### The experimental setting (p. 680 §4.1–§4.4)

**★ [FACT, p. 680 §4.1, Table 1] Data: four symbolic corpora as collected by Micchi et al.; transposed
to all twelve keys; a 2:1 train/test split of disjoint subsets.** *"A collection of datasets from various
sources [22, 25–27] organized by Micchi et al. [28] is used to train and evaluate the proposed
architecture. … MusPy [29] is used to read the compressed MusicXML files and a parser adapted from [28]
is employed to handle the proposed data representations. To increase the size of the dataset and help
alleviate possible data imbalance, each piece is transposed to 12 different keys. The dataset is split
into disjoint subsets for training and testing with a 2:1 split."* Table 1, every cell as printed:

| Dataset | Pieces | Crotchet | Chord Annotations |
|---|---|---|---|
| BPSFH | 32 | 23554 | 8615 |
| Roman Text | 82 | 18208 | 7935 |
| Tavern | 27 | 20673 | 10723 |
| Lopez | 180 | 31367 | 16666 |

Derived from the cells (this extract's arithmetic, not the paper's): 321 pieces, 93,802 crotchets,
43,939 chord annotations in total. Whether the 2:1 split was made before or after the twelve-fold
transposition — that is, whether a transposed copy of a test piece can sit in the training set — is
NOT stated in the held document. (As printed, reference [28] is *"G. Micchi, K. Kosta, G. Medeot, and
P. Chanquion, 'A deep learning method for enforcing coherence in automatic chord recognition,' ISMIR
2017, pp. 443–451"*, and [23] is Micchi, Gotham & Giraud, TISMIR 2020 — candidacy row 45; recorded as
printed, no verdict.)

**★ [FACT, p. 680 §4.2] Training samples are cut at MEASURE boundaries, 96 frames long; the front end
pools in time; Adam 10⁻⁴, weight decay 10⁻², dropout 0.2.** *"Guided by the observation that harmony
changes usually occur on average at a lower frequency than the frame rate, pooling layers are added
between blocks to reduce the temporal resolution of the harmony output. To ensure continuity and
completeness of harmony regions in the training samples, we force the sample boundaries to be aligned
with measure boundaries. A sample is chosen as 96 frames because it is divisible by all the common
measure lengths existed in the dataset. Additionally, to avoid over-sampling from music pieces with
longer length, the piece index is sampled uniformly first before a music sample is selected from the
piece."* (At one eighth of a beat per frame, 96 frames is twelve beats.) At test time *"the result is
averaged across all frames in a song"* (§4.3).

**★ [FACT, p. 680 §4.3, eqs. 14–15] Two metric families: frame-level accuracy (root, quality, a
reduced major/minor quality, and "overall"), and a SEGMENTATION QUALITY score from mir_eval's directional
Hamming distance.** *"the frame-level accuracy is computed for both root and quality. The accuracy on a
reduced dictionary of quality including only major and minor is also reported due to its prevalence in
the literature and adequacy in many practical uses."* DHD(Î, I) = Σ_{Î_i∈Î} (|Î_i| − max_{I_j∈I} |Î_i ∩
I_j|) / Σ_{Î_i∈Î} |Î_i| (eq. 14); *"a large DHD(Î, I) often indicates under-segmentation, while a large
DHD(I, Î) often indicates over-segmentation"*; SQ = 1 − max(DHD(I, Î), DHD(Î, I)) (eq. 15). Under Seg
and Over Seg in the tables are the two one-sided scores; Overall Seg is SQ. What "Overall Acc" is
(root-and-quality jointly correct, or some other combination) is not defined in words in the held
document; its values are below both root and quality accuracy in every row, consistent with a joint
criterion, but that reading is this extract's and not the paper's.

**★ [FACT, p. 680 §4.4] Three baselines, all sharing parts of the architecture: a plain CRNN [23]; frog
[28], a CRNN with a NADE decoder over the harmony components (root and quality only, here); and a
RULE-BASED semi-CRF after Masada & Bunescu [21] — reimplemented with TWO of its features.** *"A third
baseline worth comparing to is the rule-based semi-CRF proposed by Masada and Bunescu [21]. It uses
handcrafted rules as features to compute the segment scores in semi-CRF. For simplicity, we implemented
the two most important features, chord coverage and segment purity, in our experiment."* (Reference
[21] as printed is the ISMIR 2017 conference version, pp. 272–278, not the TISMIR 2019 article the
bibliography holds as row 10.) So the "RuleSCRF" row below is NOT row 10's system as published; it is
a two-feature reimplementation over this paper's own frame grid and data, and every comparison against
it is bounded by that.

### Measured results (p. 681, Tables 2–4; §5.1–§5.3)

**★ [FACT, Table 2, p. 681] The ablation — every cell as printed (bold in the paper marks the column
best):**

| Model | Root Acc | Quality Acc | Overall Acc | Under Seg | Over Seg | Overall Seg |
|---|---|---|---|---|---|---|
| Harana | **0.744** | 0.743 | **0.651** | **0.722** | 0.747 | 0.649 |
| Harana − no semi-CRF | 0.732 | 0.715 | 0.634 | 0.678 | 0.740 | 0.639 |
| Harana − no Attention Fusing | 0.741 | 0.738 | 0.650 | 0.716 | **0.749** | 0.645 |
| Harana − no Absence Score | 0.743 | **0.746** | 0.643 | 0.719 | 0.748 | **0.650** |

Derived differences, VARIANT minus full model, so a negative value is a loss on removal (this
extract's arithmetic from the cells): no semi-CRF — root −0.012, quality −0.028, overall −0.017,
under-seg −0.044, over-seg −0.007, overall seg −0.010; no attention — −0.003, −0.005, −0.001, −0.006,
+0.002, −0.004; no absence — −0.001, +0.003, −0.008, −0.003, +0.001, +0.001. **Removing the semi-CRF is
the largest loss on every one of the six columns (on Over Seg the other two removals are small gains),
and by far the largest on Under Seg.** The paper's reading
(§5.3, p. 681): *"We can see that the full architecture achieves the best result overall. Among the
missing components, semi-CRF leads to the largest performance drop. That confirms semi-CRF is an
indispensable component to capture boundary information in harmony analysis. The attention module,
although also helpful, produces relatively smaller performance gain. It is expected because after the
neural front-end, the frame-level estimations to be aggregated may be already harmonically coherent; The
attention module only helps to focus on the most representative frames. The effect of removing the
absence score is less significant. Without it, the quality accuracy and overall segmentation quality
even slightly improved. The phenomenon could result from the more difficult training objective.
Inactive pitch class activations of the input music are an extreme scenario of noisy harmonic
information. More data and a larger neural front-end might be needed to fully leverage the advantage of
the absence score [33]."* **What the "no semi-CRF" variant decodes with instead — a per-frame argmax,
or something else — is NOT stated in the held document.**

**★ [FACT, Tables 3 and 4, p. 681] Against the baselines — every cell as printed:**

| Model | Root | Quality | Majmin | Overall |
|---|---|---|---|---|
| CRNN | 0.735 | 0.714 | 0.865 | 0.634 |
| frog | 0.733 | 0.542 | 0.815 | 0.459 |
| RuleSCRF | 0.684 | 0.645 | 0.847 | 0.600 |
| Harana | **0.744** | **0.743** | **0.886** | **0.651** |

| Model | Under Seg | Over Seg | Overall |
|---|---|---|---|
| CRNN | 0.681 | 0.738 | 0.639 |
| frog | 0.681 | 0.724 | 0.624 |
| RuleSCRF | 0.666 | 0.741 | 0.625 |
| Harana | **0.722** | **0.747** | **0.649** |

The paper's reading (§5.1–§5.2): *"Harana outperforms the baseline models on all the measures. The
large gap between Harana and the rule-based semi-CRF model demonstrates the value of a neural score
function. Without a neural front-end, the rule-based model even has weaker performance than the plain
CRNN. We also notice that frog has lower accuracy than the plain CRNN model. While the autoregressive
decoding in frog could help enforce coherence between harmony components, it may require the full
spectrum of the harmony components including key and degree. However, only root and quality were used
in our experiments. Complete harmony information is difficult to collect so we believe Harana has a
greater potential to leverage larger datasets in the future."* And on segmentation: *"Higher
under-segmentation score of Harana means there are fewer missing boundaries in the estimation. Higher
over-segmentation score shows that most detected boundaries are indeed true boundaries. An interesting
observation is that the rule-based semi-CRF yields the most severe under-segmentation even though it is
optimized on the segmentation boundaries. The reason for this might be that rule based-features are
unable to clean noises such as the non-chordal notes and missing chordal notes in the input music but
directly compute features from them. The noise in the features of short regions may be confused with
the intrinsic noise of longer regions."* Derived (this extract's arithmetic): the plain CRNN, which
decodes no segmentation at all, is within 0.009 of the full model on root accuracy and within 0.010 on
overall segmentation quality; the rule-based semi-CRF sits below the CRNN on every frame-level column
and on Under Seg and Overall Seg.

### The paper's own scope statement and limitation (p. 681 §6)

**[FACT, p. 681 §6]** *"Although our experiments focused on music input of symbolic format, the
architecture could be adapted to audio input by simple modifications on the neural front-end. One
limitation of the semi-CRF architecture is that it has quadratic time complexity with respect to
sequence length so it is difficult to train the model on very long sequences. To capture the long-term
dependency of harmony progression, more efficient sequence modeling methods could be explored in the
future."* **The quadratic statement is the paper's own; read against row 11's "linear in L", it is
consistent only if this system bounds no segment length (L = N), and the held document does not say.**

**[THEORY, as the paper cites it]** Sarawagi & Cohen 2004 [6] (row 11) for the semi-CRF and its
dynamic programming; Vaswani et al. 2017 [24] for scaled dot-product attention; Huang et al. 2017
[30] for DenseNet; Micchi, Gotham & Giraud 2020 [23] (row 45) for the DenseNet–GRU front end; Masada &
Bunescu [21] (row 10, in its 2017 conference form) for the rule-based semi-CRF; Tymoczko et al. 2019
[22] for the Roman-numeral encoding; Raffel et al. 2014 [31] and Harte 2010 [32] for the segmentation
metrics; Pauwels et al. 2019 [5] for *"harmonic regions in music do not always share the same length"*.

**[CONJECTURE — the authors' own, labelled as such here]** That frog's weaker result is because it
*"may require the full spectrum of the harmony components including key and degree"* (§5.1, "may");
that the rule-based semi-CRF's under-segmentation comes from feature noise on short regions (§5.2,
"might be"); that the absence score's non-effect comes from *"the more difficult training objective"*
and would reverse with more data and a larger front end (§5.3, "could", "might"); that the front end's
frame estimates are *"already harmonically coherent"* (§5.3, "may be").

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- Symbolic input with a BEAT available: frames are one eighth of a beat, so the input must carry a
  beat grid (MusicXML via MusPy in the paper). Pitch as unspelled pitch classes — spelling, if present
  in the source, is discarded at input. The bass (lowest sounding pitch class) per frame. No voice
  membership, no meter beyond the beat, no key signature, no explicit note onsets or offsets.
- A label set of 12 roots × 10 qualities; no tonality label in the training data is consumed even
  where the corpora carry one (the paper's own statement that Roman-numeral labels were reduced *"as a
  compromise"*).
- Training data as labeled segmentations (region boundaries and labels both given), cut into 96-frame
  measure-aligned samples; a transition table counted from those labels at the frame level.
- The candidate boundary grid is every frame position; the maximum segment length is not stated.

**What it HANDS downstream.**
- One best labeled segmentation: contiguous, non-overlapping harmonic regions, each carrying one (root,
  quality) pair; boundaries on the eighth-of-a-beat grid.
- In principle the normalised distribution P(Y|X) over all labeled segmentations (eq. 2, with Z
  computed exactly for training) — but the paper reports only the argmax decode and publishes no rival
  readings and no confidence.
- Per frame, as intermediate products: root and quality distributions and a pitch-class activation
  vector (eq. 4) — the front end's estimate of which pitch classes are chord tones, which is a chord-tone
  assignment at the pitch-class level, produced BEFORE the decode and not conditioned on the decoded
  label.
- No tonality, no scale degree, no inversion or figure, no per-note chord-tone assignment.

**Its own STATED SCOPE and limits.**
- **Domain:** symbolic music, MIDI-like, classical repertoire (the four corpora); audio named as an
  adaptation the front end could absorb (§1, §6).
- **Decision scope:** segmentation and (root, quality); tonality and degree explicitly excluded, with
  the stated reason (§3.1.2).
- **Cost:** *"quadratic time complexity with respect to sequence length"* (§6); training on 96-frame
  samples.
- **Fitting:** end-to-end discriminative, exact NLL (eq. 13), Adam with weight decay and dropout; the
  transition table counted and frozen, λ set *"empirically"* to 0.001 with no statement of the set it was
  chosen on; a 2:1 disjoint split whose relation to the twelve-fold transposition is unstated; single
  numbers reported with no variance, no fold count and no confidence interval.
- **Coupling:** segmentation and label decided together; one product label per segment; the previous
  label enters only through the counted transition table; no second label axis.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (the "with" machinery on symbolic music, a second instance beside row 10):** a semi-Markov
  decode over candidate regions with an exact normaliser, trained by conditional likelihood, on
  symbolic classical input — the machinery `FRAMEWORK.md` §14.1 names as *"the two symbolic systems
  built on it"*. This paper's contribution over row 10 is the SCORE: learned rather than hand-built,
  and the ablation says the learned score is what carries the result (RuleSCRF below CRNN).
- **Adapt (the segment content score as a label-conditioned aggregation over frames):** eq. 6's
  attention uses the CANDIDATE LABEL as the query over the region's frames — a segment score that
  weights the region's moments by their fit to the reading being scored, rather than averaging them.
  That is a published, measured shape for "how does a span's content score a candidate chord when the
  span is not homogeneous", though the ablation puts its worth at 0.001 of overall accuracy here.
- **Adapt (the absence score as a learned analogue of the missing-tone penalty):** eq. 11 scores a
  candidate label against what is NOT sounding. The record's own missing-tone penalty (D-534) is
  counted per chord factor; this is the same question answered by a learned term, and the paper's own
  ablation finds it without effect on this data. A datum beside D-534, not a rival.
- **Adapt (the transition term's shape — a datum for row 11's factorization test):** eq. 8's second
  term, (v_i − u_i)·T[l_i, l_i], is a segment-length term LINEAR in length. By row 11's §2.3 test that
  term is decomposable into per-frame terms (an exponential-length prior), so the semi-Markov decode
  does no work for it; whatever segmental power this system has comes from the attention content score
  and the absence score, which are not sums over frames. An L2 detail specification classing its own
  terms by that test has here a worked example of each side.
- **Must argue against (the label space):** the paper's stated reason for dropping tonality —
  component-wise independent classification is *"incompatible with semi-CRF because the boundary of each
  component must be the same"*, and the joint Roman-numeral space is *"intractable … with limited
  training data"* — is a published argument against exactly the product state the framework's L2
  chooses (D-526: a (tonic, mode, degree) state; DP-A: no division by published field). The charter's
  answer is that tonality and chord boundaries are the SAME boundaries by design (DP-E: a tonality change
  is located at a harmonic boundary), which is what makes the product label admissible; the cost
  objection (47k labels, limited data) is the one the detail specification must meet with its own
  admission rule and tables. A rival ground, stated in the paper's own words, for a design point already
  chosen.
- **Must argue against (the grid):** an eighth-of-a-beat frame grid with measure-aligned 96-frame
  training windows is a "before (every fixed grid)" answer to the boundary grid question, against the
  L1 charter's change-point grid (V8). Every boundary this system can place is a frame edge; a harmony
  change inside a frame is unreachable. The paper does not measure what this costs.
- **Must argue against (unspelled input, no tonality, no rivals published):** three things L0 gives or
  L2 must publish that this system discards or lacks — DP-F's given spelling, the tonality half of the
  entangled decision, and the rival readings with their mass. Its measured figures are therefore for a
  narrower decision than L2's, and comparison against them is comparison on the boundary-and-chord half
  alone.

## ★ Findings, routed and not applied

**(1) IDENTITY: NO finding.** Printed title, authors, venue, year and CC BY 4.0 licence all match the
bibliography's row 33 at page 1 and the running header. The one datum for the bibliography
reconciliation: this paper cites Masada & Bunescu in its ISMIR 2017 conference form ([21], pp.
272–278), a version the bibliography does not hold (row 10 is the TISMIR 2019 article; the held file is
the arXiv preprint). No verdict.

**(2) V10's "largest ablation contributor" RE-VERIFIED at the object, with four precisions to how the
[FACT] is read.** The sentence `population.md` line 111 quotes is at §5.3, p. 681, verbatim, and Table 2
bears it out on every one of its six columns. The precisions: (a) the MAGNITUDES — removing the semi-CRF
costs 0.017 of overall frame accuracy and 0.010 of overall segmentation quality, and 0.044 of the
under-segmentation score, where the other two components cost 0.001–0.008; "largest" is true and the
absolute size is small; (b) what the "no semi-CRF" variant decodes with is not stated in the held
document, so what the drop measures (the decode, or the decode plus the transition table it carries) is
not establishable; (c) the "no absence score" variant BEATS the full model on quality accuracy (0.746
vs 0.743) and overall segmentation (0.650 vs 0.649), which the paper itself reports; and (d) the
figures are single runs with no variance stated (#24), so the smaller differences carry no stated
uncertainty. Nothing is owed to the [FACT] as a statement of the ablation's ordering. Routed to the
findings surface's V10 row and DP-C block. No verdict.

**(3) The question carried from row 11 is ANSWERED at the object: Harana uses the WEAK form.** Its
general statement (eq. 3) admits previous-segment conditioning, but the score it builds conditions the
content score on the candidate segment and its own label only, and the previous label enters solely
through the counted transition table of eq. 8. So both musical semi-CRFs in the slice (rows 10 and 19)
use the weak form, and only the formalism paper (row 11) states the strong one. Routed to L2's detail
specification beside DP-C and the rows 10 and 11 extracts; no verdict.

**(4) The transition table is COUNTED from the training ground truth and FROZEN, while the score
network is fitted discriminatively — a published instance of the staged-fit shape (D-525: counted tables
frozen, a small set of combination weights fitted), here with one counted table, a neural score, and one
hand-set balance weight λ = 0.001.** Beside rows 10's and 11's fully discriminative fits, this is the
third symbolic-or-formal semi-CRF in the slice and the first of the three to freeze a counted table.
Routed to L2's detail specification beside D-525 and DP-P; no verdict.

**(5) The transition score's self-transition term is LINEAR in segment length — by row 11's §2.3 test
a term the segmental decode does no work for.** The segmental power of the system therefore rests on
the attention content score and the absence score, which are not per-frame sums. A worked example for
the design check finding (4) of the row 11 extract proposes. Routed to L2's detail specification beside
row 11's finding (4) and row 20; no verdict.

**(6) NO TONALITY, by explicit design, with the paper's stated reasons — the same tonality-absent
shape as row 10, and a published argument against a product label.** *"47k different harmony labels,
which is intractable … classify each harmony component independently … is incompatible with semi-CRF
because the boundary of each component must be the same. As a compromise, we use … root and quality."*
On L2's entangled decision this system answers the boundary-and-chord half and is silent on the tonality
half; its ADMITTED verdict and group 2 placement stand (the candidacy row admits it for its architecture,
which is what it carries). The compatibility argument is a rival ground against D-526 / DP-A's product
state, answered in the record by DP-E (one boundary set for tonality and chord); the cost argument is
one the detail specification's admission rule must meet. Routed to the findings surface's DP-A and DP-E
blocks and to L2's detail specification; no verdict.

**(7) The rule-based semi-CRF reimplementation UNDERPERFORMS a plain CRNN that decodes no segmentation
at all, on every frame-level column and on under- and overall segmentation** (Table 3: 0.684/0.645/0.600
against 0.735/0.714/0.634; Table 4: 0.666/0.625 against 0.681/0.639). Read with finding (2): the
segmental decode helps HERE only over a learned score; over a two-feature hand-built score it hurts.
Bounded by the reimplementation being two of row 10's features on this paper's grid and data, not row
10's system — so this is not evidence about row 10's published figures. A datum beside DP-C's "with"
and beside the record's own D-531 (hand-built emission confirmed, learned replacement not triggered):
the sign of "hand-built versus learned" reported here is the opposite of the record's, on a different
question and input. Routed to the findings surface's DP-C block and to L2's detail specification; no
verdict.

**(8) The candidate boundary grid is a FIXED METRICAL FRAME GRID (one eighth of a beat), with
training windows cut at measure boundaries** — a "before (every fixed grid)" instance for the grid
question, opposite to the L1 charter's change-point grid (V8, Pardo & Birmingham's partition points),
unmeasured by the paper as to cost. Also a datum beside D-030/D-031 (bounded context): the system is
trained on twelve-beat windows and evaluated on whole pieces, with the decode's window at test time
unstated. Routed to the L1 and L2 detail specifications; no verdict.

**(9) The input DISCARDS SPELLING and carries the BASS explicitly.** Twelve pitch classes at input;
the bass pitch class as a separate one-hot *"to help distinguish between harmonies with the same pitch
class vector"*. The first is a consumer that throws away what L0 gives (DP-F); the second is a published
symbolic precedent for the bass as an explicit input to the chord decision beside D-449's per-event bass
factor and row 3's decoded bass chain. Routed to L2's detail specification; no verdict.

**(10) The front end's per-frame PITCH-CLASS ACTIVATION is a chord-tone estimate made BEFORE the
decode and not conditioned on the decoded label** — the "input, from an elaboration detector running
first" shape DP-D's candidate list names and does not choose, here inside one network and trained
end-to-end through the decode's likelihood, so neither cleanly "first" nor DP-D's chosen "part of one
decision". A datum for DP-D's candidate list beside row 10's hand-rule figuration heuristics and row
35's detector. Routed to the findings surface's DP-D block; no verdict.

**(11) Fit/evaluation and uncertainty, at the object:** a 2:1 disjoint split whose relation to the
twelve-fold transposition is unstated (a transposed copy of a test piece may or may not be in
training); λ *"chosen empirically"* on an unnamed set; single figures with no variance, fold count or
uncertainty range (#24); test-time accuracy averaged over all frames of a song, so long pieces weigh
more. Routed to measurement design beside rows 8's, 26's, 30's and 5's fit findings; no verdict.

**(12) The segmentation-quality metric — mir_eval's directional Hamming distance in both directions,
combined as 1 − max — is a published, tool-backed convention for grading BOUNDARY placement separately
from labels, with under- and over-segmentation separable.** A datum beside the robust unit (D-115),
the segment-level F-measure convention of row 10, and D-606. Routed to measurement design; no verdict.

**(13) The paper's own cost statement — quadratic in sequence length — beside row 11's linear-in-L.**
Consistent only if no segment-length bound is imposed, which the held document does not state either
way. A datum beside D-004 (the decode segment cap) and row 11's finding (5); no verdict.

**(14) Exact normaliser and posterior available; nothing published from it.** Eq. 2's Z is computed
exactly in training; at inference only the argmax is decoded and no rival or confidence is reported. The
same datum as row 11's finding (10), now on a musical instance, beside D-006, D-008 and DP-K. Routed to
L2's detail specification; no verdict.

**(15) No falsifier.** Nothing read contradicts any CHOSEN design point. The one ratified [FACT]
resting on this paper (the ablation ordering in DP-C's ground, part of V10) is re-verified at the
object with its magnitudes now recorded; the paper's argument against a product label (finding 6) is
a rival's ground the framework already answers at DP-E and is not a measurement against a chosen
point. **No STOP fires** under the remedial commission's §5.

## Centrality

**CENTRAL, challengeable at the progress record.** Ratified text rests on it at one place — DP-C's
*"single largest contributor in a third system's ablation"* [FACT] (`FRAMEWORK.md` lines 696–697) — and
the original commission's §4 makes a paper *"whose claims would carry load in a detail specification or
against a design point"* central; further, it is the candidacy row's *"current candidate architecture
for L2"* and the only paper in the slice that builds DP-C's chosen machinery with a LEARNED score on
symbolic classical music, so findings (3), (4), (5), (6) and (7) are claims an L2 detail specification
would cite this paper for directly (the weak form on a musical system; a counted-and-frozen transition
table beside a fitted score; a decomposable length term; the published argument against a product
label; hand-built segmental scoring below a plain frame model). **The ground on which NOT CENTRAL could
be argued, stated so the challenge is easy to make:** the one figure the record rests on is already
verified by the pass at `population.md` §3 (V10) and this read adds magnitudes and precisions, not a new
verification; the system decides no tonality and discards spelling, so it measures a narrower decision
than L2's; and its ablation differences are small and carry no stated uncertainty. **A second
independent extraction is therefore OWED** on this verdict.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`
and `cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (14) are routed and
written nowhere else. It does not fetch the GitHub repository the footnote names, Masada & Bunescu's
ISMIR 2017 version, Micchi et al.'s dataset collection or parser, MusPy, mir_eval, or any of the four
corpora. It opens no code, touches no measurement tool, no corpus, no golden and nothing under
`tools/`. It writes no open-items row and allocates no decisions-register identity. It reads no other
paper and takes no decision about the order of the remaining slice.

---

*Provenance: written 2026-09-06 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_twenty_three.md`, on the user's opening instruction naming row 19,
after the ordinary session-start read (`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md` whole, the
derived gating answer). Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` whole
(row 19 at line 81), `cowork_l2_task_b_slice_derivation_2026_09_05.md` at line 66,
`docs/research_papers/BIBLIOGRAPHY.md` at line 33, `FRAMEWORK.md` at lines 386–425 (the L2 charter),
669–684 (DP-A), 685–701 (DP-B and DP-C), 712–719 (DP-E to DP-H), 802–806 (DP-P) and 1004–1013 (§14.1),
located by a `Grep` of the staged tree for "Harana", "Cwitkowitz", "neural semi-CRF" and "ablation
contributor"; the findings surface at lines 150–211 (the DP-C block and the opening of DP-D);
`reading_pass/population.md` at lines 60–129 (§1–§3a; V10 at line 111); the progress record whole; both
commissions whole; and the row 11 extract whole, for the form and for the carried question. The paper
itself was read at the object as page images, all eight pages. No shell command was run on the
repository or on any staged copy of it for content or for listings; the saved root listing was
consulted by `Grep` only. No figure of this project's own measurement is restated (#17f, D-431); every
value above is the paper's own, and every derived difference or sum is marked as this extract's
arithmetic.*
