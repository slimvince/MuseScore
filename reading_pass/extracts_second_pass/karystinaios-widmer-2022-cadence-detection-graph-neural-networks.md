# SECOND INDEPENDENT EXTRACTION — row 38 — Karystinaios & Widmer, *Cadence Detection in Symbolic Classical Music Using Graph Neural Networks* (ISMIR 2022; arXiv:2208.14819v1)

> **STATUS: a Cowork reading, 2026-09-20. Nothing in this file is ruled.** It is the second,
> independent extraction the reading-pass commission asks for on a source the first pass graded
> CENTRAL (`cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, as quoted in handoff
> entry 169 §3; the commission itself was not opened in this sitting). Its §0–§7 were written
> **before the first extract was opened**, and §8 was added and §0–§8 landed before it was opened; §9 is
> the cross-check that came after, and it changed nothing in §0–§8. **§10 is a user-ordered check that
> did correct §0–§9**, each correction at its site with the former wording kept. The first extract is
> `reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md`; this
> file takes the same name under `reading_pass/extracts_second_pass/` by Ruling 2 of handoff entry 186.
>
> **This file is paper-facing only.** It says what the pages carry. What the repository's record says
> about this paper, and whether the paper is central to anything, is the first extract's half and is
> not judged here.

## §0 — Declarations: what this reader knew, and how the read was run

**The object.** `docs/research_papers/karystinaios_widmer_2022_arxiv_cadence_detection_gnn.pdf`,
1,091,571 bytes at the staging result (device modification time 1784448963062), staged by the exact
path handoff entry 212 §3 gives. **8 PDF pages**, the tool's own number, obtained by a deliberately
out-of-range request (page 40) before any page was read.

**Read whole, at the page images, in two requests** (PDF pages 1–4, then 5–8). This reader looked at
the images themselves and not only at the calls' success lines: all eight were delivered; pages 1–7
carry the paper and page 8 carries only the last reference, [23]. The type was legible at the size
delivered, with a bound on the bold marks in Table 2 (§2).

**The independence bound — what this reader had seen before the paper, declared and not claimed away.**

- Handoff entries 212, 211, 210, 209 (at §2 and §6 as the boot order asks, and read whole in fact),
  200, 188, 186 and 169 whole; entry 206 at §3; entry 198 at §7; entry 152 at (v)–(x); entry 118 at
  its bridge-fault section. At what was read of them, this row is named as owed and as next after
  row 37, with its held file's name and size and its first extract's name and size (entry 212 §3).
  **Entry 212 §1 speaks of row 37's paper (reference [4] of this one) and carries two figures this
  paper's Table 2 also prints: a PAC F1 of .80 at the Bach row and 0.69 for Haydn's PAC.** This reader
  came to Table 2 knowing those two values.
- **That a second extraction is owed at all tells this reader the first pass graded the paper
  CENTRAL.**
- `reading_pass/candidacy_upgrades.md` at its lines 225–245 only, and **not below line 245**, on entry
  206's warning. **What those lines carried of this row:** line 243, the table row — *"Karystinaios &
  Widmer 2022, cadence detection using graph neural networks"*, *"AT THE OBJECT, whole, 8 pp."*, the
  first extract's path, *"CENTRAL"*, *"OWED"*; and line 226, which names rows 37 and 38 as *"the two
  halves of the cadence-cue evidence behind DP-I's split"*. **So this reader came to the paper knowing
  that the record reads it as cadence-cue evidence behind a split it calls DP-I** (what DP-I is was not
  looked up). Line 244 names row 39 as *"Sears, Pearce, Caplin & McAdams 2018, simulating expectations
  for tonal cadences"*, *"pp. 29–52"*, which bears on reference [19] of this paper (§3).
- **Ruling 2's name-only look-up**: `reading_pass/extracts/` was listed to verify entry 212 §1's
  figures; that listing showed this row's first-extract file name and its size, **13,786 bytes**, and
  the names and sizes of the other files in that folder. `reading_pass/extracts_second_pass/` was
  listed too; no file for this row stood there. The first extract was not opened before §0–§7 of this
  file stood.
- **Row 37's second extract** (the paper this one cites as [4]) at its heading list and its lines
  1–174, for the form. **Those lines carry, about [4]:** that it decides per beat; that its corpora are
  the 24 fugues of WTC I and *42* Haydn string-quartet expositions; and that its detected types are
  PAC (both corpora), PAC+rIAC (Bach) and HC (Haydn). This bears on two observations below (§7 items 2
  and 4), and is declared at each.
- **`DECISIONS.md` whole, as the session-start read.** Its index titles include D-081 and D-336 (the
  cadence detector is key-agnostic; it votes for the key), D-462 (cadence validation scoped to
  location; type only partially attributable) and D-584 (the perfect/imperfect call made on the
  bass-derived inversion). None names this paper, and whether any rests on it was not looked up.
- `FRAMEWORK.md`, the slice derivation, the L2 progress record, the findings surface,
  `docs/research_papers/BIBLIOGRAPHY.md` and the `docs/research_papers/` listing were **not** opened
  by this reader.
- **This reader is a language model; what it may hold of the paper from training cannot be inspected
  from inside the session and is declared as a bound.** The statements below were written from the
  page images in view, with their locators.

**No web access, no subagent, and no shell command in the container or on the device.** Counts, sums,
differences and recomputations below that are this reader's and not the paper's are marked
**DERIVED**; each was done by hand, not by a tool.

## §1 — Identity, at the first page (PDF page 1)

The page prints the title *"CADENCE DETECTION IN SYMBOLIC CLASSICAL MUSIC USING GRAPH NEURAL
NETWORKS"*; the authors *"Emmanouil Karystinaios¹ Gerhard Widmer¹·²"*; affiliations *"¹ Institute of
Computational Perception, Johannes Kepler University Linz, Austria"* and *"² LIT AI Lab, Linz Institute
of Technology, Austria"*; and an e-mail line at *jku.at*. The left margin carries the arXiv stamp
*"arXiv:2208.14819v1 [cs.SD] 31 Aug 2022"*. The licence box at the foot of the left column gives
*"Creative Commons Attribution 4.0 International License (CC BY 4.0)"* and the citation *"E.
Karystinaios, G. Widmer, "Cadence Detection in Symbolic Classical Music using Graph Neural Networks", in
Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022."*

**What the held file is.** The arXiv first version, carrying the ISMIR 2022 citation in its licence
box. **No printed page numbers were seen on any of the eight pages as delivered**, so the proceedings
pagination is not established from this file.

Against the candidacy table's *"Karystinaios & Widmer 2022"* ✓ and *"8 pp."* ✓ (the tool's count). The
table's title, *"cadence detection using graph neural networks"*, is the printed title with *"in
Symbolic Classical Music"* dropped; the words it keeps are the printed words, in order. The
bibliography was not opened, so no check against it is claimed. **No identity finding.**

## §2 — The document, and how to cite a place in it

Eight PDF pages; no printed page numbers (§1). **Locators below are PDF pages, written "p. N".**

Section headings, in order, as printed: *Abstract* p. 1; *1. Introduction* p. 1; *2. Related Work*
p. 2; *3. Modeling Scores as a Graph* p. 2 — *3.1 Feature Overview* p. 2; *4. Problem Setting &
Corpora* p. 3; *5. Model* p. 3 — *5.1 Graph Convolutional Network* p. 3, *5.2 Dealing with Extreme
Class Imbalance: Stochastic GraphSMOTE* p. 3; *6. Experiments* p. 4 — *6.1 Quantitative Results* p. 4,
*6.2 A Qualitative Look* p. 6; *7. Conclusion* p. 6; *8. Acknowledgements* p. 7; *9. References* pp.
7–8 (23 numbered references).

Four figures: 1, an example graph built from a one-bar score excerpt (p. 2); 2, multi-hop
neighbourhood sampling (p. 3); 3, Haydn op. 54 no. 1, mvt. II, mm. 33–45, the model's PAC output
(p. 5); 4, the model's predictions for fugue no. 19 of WTC I (p. 6). Four tables: 1, dataset statistics
(p. 4); 2, the comparison with the reference model (p. 5); 3, three-class classification by feature set
(p. 6); 4, convolution depth (p. 6). Three footnotes carry links: the code and full feature
specification (footnote 1, p. 2, `github.com/manoskary/cadet`), the generated graphs (footnote 2, p. 3,
`github.com/manoskary/tonnetzcad`), and the results and trained models (footnote 3, p. 4,
`wandb.ai/melkisedeath/CadenceDetection`). **None of the three was opened.**

**Bound on Table 2.** Some values are set in bold. The page does not state what bold means; as this
reader reads them they pick out the highest value per column within each block. Two ties for the
highest were met: the Bach PAC block's beat F1 0.80 (reference and pretrained), both bold as read; and
the Bach rIAC block's note-level 0.87 (the two models), of which only one is bold as read. *(★ CORRECTED
AT THE USER-ORDERED CHECK, 2026-09-20. Former wording, preserved (#12): "and at the one tie met (the
Bach rIAC block's note-level 0.87, twice) only one of the two is bold as read." — a second tie was
missed.)* The digits were
read without difficulty at the size delivered; **the bold marks are AS READ at that size** (a larger
rendering would need a shell renderer, which this sitting's rules bar, and none was sought). Tables 1,
3 and 4 are in ordinary type; Table 4's bold row was plain to see. The score excerpts in Figures 3 and
4 were not transcribed; their captions and legends were read.

## §3 — Coupling facts: what the paper assumes upstream, what it hands downstream, its stated scope

**Stated aim (p. 1).** The contribution is *"two-fold: a simple graph representation of scores
extended with local features, and a Graph Convolutional Network (GCN) model to tackle heavily
imbalanced classification tasks such as Cadence Detection."* And, of the reference model [4]: *"Our
new model proposed here will be shown to achieve comparable overall results; however, we will argue
that it makes fewer task-related and musical assumptions, resulting in more general applicability."*

**What it assumes upstream.**

- **The input is a symbolic score, one node per note and per rest.** *"We model a score as a graph
  with individual notes and rests as nodes and simple temporal relations as edges"* (p. 2, §3). Scores
  *"were retrieved from http://kern.ccarh.org and were parsed in python using the partitura package
  [14]"* (p. 3, §4). Whether voice separation is required is **not met in the pages as read**.
- **The notated time and key signatures are inputs.** *"we translate global attributes such as time
  signature and assign them to each note"* (p. 2, §3.1); Figure 1's caption: *"Global attributes such
  as time and key signatures are added as node features"* (p. 2). A key estimation step is **not met
  in the pages as read**; the paper does not say whether it uses one.
- **Chord-type information, where §3.1 names it, enters as interval-set matches**: *"binary features
  activated when intervallic content is identical to the interval set corresponding to particular chord
  types, i.e., major, minor, diminished, etc."* (p. 2, §3.1). What the Category 3 features and [15]'s
  generic features encode of chords is not stated beyond the words quoted in §4.2. A harmony analysis or
  chord segmentation step is **not met in the pages as read**.
- **The cadence-specific features are local to the note.** *"our features are calculated at the note
  level only, considering the time of onset for each note and its immediate neighbors, such as adjacent
  past onsets or simultaneous onsets. In particular, we do not use any information about events that
  occur on previous beats"* (p. 2, §3.1).
- **Ground truth is three prior human annotations** (p. 3, §4): the Bach fugues' cadence annotations
  *"were presented in [11]"*; the Haydn quartets' *"cadence annotations were produced by Sears and
  colleagues [19]"*; the Mozart quartets are *"annotated by Allegraud and al. [18]"*. Reference [19] is
  *"D. R. Sears, M. T. Pearce, W. E. Caplin, and S. McAdams, "Simulating melodic and harmonic
  expectations for tonal cadences using probabilistic models," Journal of New Music Research, vol. 47,
  no. 1, pp. 29–52, 2018"* (p. 7). **No agreement measure between annotators was met in the pages as
  read.**
- **The label is a beat, projected onto notes.** *"The manual annotations in these datasets mark a
  cadence as occurring on the beat where the final I (i) arrives. Our precise task thus is to predict,
  for every note of the score, whether this note is contained in a cadence's arrival beat"* (p. 3, §4).
- **Tooling and published methods taken as given**: partitura [14]; generic note-wise features *"as
  defined in [15]"*; interval vectors [16]; Laplacian eigenvectors [17]; GraphSAGE [20]; SMOTE [21];
  GraphSMOTE [5] (pp. 2–4).
- **Music-theory categories are taken as given**: PAC, rIAC (*"root position Imperfect Authentic
  Cadences"*) and HC (p. 3, §4; spelled out again in Table 2's caption, p. 5).

**What it hands downstream.** For each note, a class decision from the trained classifier: binary
(cadence of the target type, or not) in the first and third experiments, three-class in the second
(pp. 4–6). Onset-level and beat-level decisions are obtained *"simply by aggregation"* (p. 4, §6.1);
**the aggregation rule is not met in the pages as read.** The classifier's last layer is a softmax whose
output the page calls *"the predicted class probabilities of node i"* (p. 4, §5); whether those values
are published as an output beside the decision is **not met in the pages as read**. No harmonic label,
key or chord is described as an output.

**Its stated scope.**

- Repertoire: *"cadences of the Baroque and Classical periods"* (p. 3, §4); the 24 fugues of WTC I,
  Haydn string-quartet expositions, and 31 Mozart string-quartet movements (p. 3; Table 1, p. 4).
- Cadence types: *"The main focus will be on detecting Perfect Authentic Cadences (PAC); where our
  annotated datasets permit, we will also consider root position Imperfect Authentic Cadences (rIAC)
  and Half Cadences (HC)"* (p. 3, §4). Footnote 4 (p. 4): *"In accordance with [4], we ignore the HC in
  Bach and rIAC in Haydn, because of their low numbers."*
- The paper's own limit, stated at §6.2 (p. 6): the model *"by design cannot consider high-level
  musical considerations such as, e.g., whether PAC-like patterns that occur in sequence should count
  as PACs or not."*

## §4 — The method, as the paper states it

### §4.1 The graph (p. 2, §3)

*"Formally, let G = (V, E) be a graph, where V is the set of nodes and E ⊆ V × V the set of edges and
let A be the adjacency matrix of G. Each note and each rest in a score are represented as a node in the
graph."* Three undirected edge types, as printed:

- E_on = {(i, j) | on(n_i) = on(n_j)} — *"between notes that occur on the same onset"*;
- E_cons = {(i, j) | on(n_i) + dur(n_i) = on(n_j)} — *"between consecutive notes"*;
- E_dur = {[(i, j) | on(n_i) + dur(n_i) > on(n_j)] ∧ [on(n_i) < on(n_j)]} — *"between a note of longer
  duration and notes whose onsets occur during this time"*;
- E = E_on ∪ E_cons ∪ E_dur; *"All edges in E are undirected."*

*"where n_i is the i^th note. on denotes the onset of a note, dur the duration."* Figure 1 (p. 2)
colours E_on blue, E_cons green and E_dur red.

### §4.2 The node features (pp. 2–3, §3.1)

Three categories, **135 features per node in total** (*"In total, we store 135 features per node"*,
p. 3):

1. **General note-wise features** — *"the largest one"*: onset in score-relative beats, duration in
   beats and MIDI pitch (via partitura); the time signature and other global attributes assigned to
   each note; generic note-wise features *"as defined in [15]"*; interval vectors [16]; and the binary
   chord-type interval-set features (§3 above).
2. **Graph-aware features**: *"the first 20 eigenvectors from the Laplacian of the adjacency matrix
   [17]"*.
3. **Note-wise cadence-related features** *"similar to those in [4], such as voice leading information
   and voicing"*, restricted to the note's onset and its immediate neighbours (§3 above). *"While these
   features are more restricted compared to [4] they are also more general, since we make no
   assumptions on and reference to "cadence anchor points" (e.g., the occurrence of the preceding
   subdominant and dominant harmony), which in [4] are identified with specialized heuristics."* The
   page says this category *"is the only one that is designed with the specific classification target
   in mind"*.

How many of the 135 fall in each category is **not met in the pages as read**; the page points to
footnote 1's repository for *"a complete specification of all features"*.

### §4.3 The model — Stochastic GraphSMOTE (pp. 3–4, §5)

*"a Graph Convolutional Network with a built-in graph Auto-Encoder and Synthetic Minority
Over-sampling for imbalanced node classification. The model consists of 4 parts, the encoder, a SMOTE
layer in the encoder's latent space, the decoder, and the classifier. The structure of the model
follows GraphSMOTE [5] but with some major differences, mainly to adapt for stochastic training, which
is needed because of the large size of our score graphs"* (p. 3).

- **Encoder** — a GraphSAGE [20] stack, as printed:
  h^(l+1)_N(i) = mean({W^(l+1)_pool · h^l_j, ∀j ∈ N(i)});
  h^(l+1)_i = σ(W^(l+1)_enc · concat(h^l_i, h^(l+1)_N(i)));
  h^(l+1)_i = norm(h^l_i) — **printed with superscript l on the right-hand side** (§7 item 6).
  N(i) = {j | (i, j) ∈ E}; B ⊆ V a batch; H^(enc)_B = {h^(L+1)_u | u ∈ B} (p. 3).
- **SMOTE layer, per batch** (p. 3, §5.2): count μ_i per class; with μ_M the majority count and μ_m
  the minority count, generate (μ_M − μ_m) samples of the minority label, *"we force a 1 : 1 binary
  class distribution"*. Each synthetic sample is a random linear interpolation between a randomly
  chosen minority anchor and one of its k nearest same-class neighbours in the batch, *"in the
  euclidean space"*; the layer *"is applied in the latent space of the encoder"*. *"The main novelty of
  our model is that the SMOTE is performed for each batch separately."*
- **Decoder** (p. 4): A^(dec)_B = σ(H^(smote)_B · W^(dec) · transpose(H^(smote)_B)); A^(thr)_B =
  hardshrink(A^(dec)_B, τ), σ a sigmoid, τ the hard-shrinkage threshold. Regularisation loss
  L^(dec)_B = BCE(A^(dec)_B, A_B), binary cross-entropy against the batch's adjacency.
- **Classifier** (p. 4): one GraphSAGE layer on the thresholded generated adjacency, with a linear
  layer on top: h^(clf)_N(i) = mean(W^(pool) · A^(thr)_B[i, :] · H^(enc)_B); h^(clf)_i =
  norm(σ(W^(clf) · concat(h^(enc)_i, h^(clf)_N(i)))); h^(clf)_i = softmax(W^(proj) · h^(clf)_i).
  *"During training, we use H^(smote)_B and h^(smote)_i respectively instead of H^(enc)_B and
  h^(enc)_i."*
- **Total loss** (p. 4): L^(tot)_B = L^(CE)_B + γ · L^(dec)_B, L^(CE) the cross-entropy, γ a
  hyperparameter.
- **Stochastic training** (p. 4): each batch is a sampled node subset B; neighbours are retrieved up to
  depth k with *"a maximum number φ_l of neighbors per depth layer l"*.

### §4.4 The settings (p. 4, §6)

*"We fix our model with a hidden dimension of 256, with L = 2 hidden layers with φ₁ = 10 and φ₂ = 25
sampled neighbors for hidden layers 1 and 2 of the encoder, respectively, and one hidden layer of the
same dimension for the classifier. The learning rate is set at 0.007, the weight-decay at 0.007, with a
batch size of 1024, k = 3 for SMOTE, the decoder regularization loss multiplier γ = 0.5, and adjacency
threshold value τ = 0.5."* The optimiser, the number of epochs and the stopping rule are **not met in
the pages as read**.

### §4.5 The three experiments (p. 4, §6)

*"The first compares our model to the state of the art results in [4], using the same data and
train/test setup. The second experiment focuses on multi-class learning of the particular type of
cadence using different sets of features, in order to investigate how the model generalizes to a more
complex setting and inspect the relevance of different feature sets. The third experiment investigates
how neighbor convolution contributes to the model's performance."*

## §5 — Results, as the paper states them, and what this reader derived from them

### §5.1 Table 1 — dataset statistics (p. 4)

| Dataset | Pieces | Nodes | Edges | PAC | rIAC | HC |
|---|---|---|---|---|---|---|
| Bach Fugues | 24 | 24,567 | 229,107 | 237 | 78 | 15 |
| Haydn String Quartets | 45 | 38,661 | 441,491 | 434 | 24 | 340 |
| Mozart String Quartets | 31 | 68,190 | 762,796 | 1,089 | - | 1,930 |

Caption: *"Cadence nodes constitute less than 2% of all nodes."* Text (p. 3): *"cadences of all types
combined account for less than 2% of the total notes in the score. Our produced score graphs range
from approximately 25k nodes for the Bach fugues all the way to 70k nodes for the Mozart string
quartets with more than 750k edges."*

**DERIVED.** The text's figures agree with the table (24,567 ≈ 25k; 68,190 ≈ 70k; 762,796 > 750k).
**The page does not say whether the PAC, rIAC and HC columns count cadences or cadence nodes.** Read as
node counts, the row sums against the node column are: Bach (237 + 78 + 15) = 330 of 24,567, about
1.3 %; Haydn (434 + 24 + 340) = 798 of 38,661, about 2.1 %; Mozart (1,089 + 1,930) = 3,019 of 68,190,
about 4.4 %. **On that reading the caption's "less than 2%" does not hold for the Haydn and Mozart
rows.** Read as cadence counts, the caption cannot be checked from the table. See §7 item 1.

### §5.2 Table 2 — comparison with the reference model (p. 5)

Caption: *"Results using half of the dataset for training, half for testing. Bach: fugues no.1-12 were
used for training, no.13-24 for testing; Haydn: random 21:21 split. The pretrained network was trained
on the other dataset, i.e. Pretrained SGSMOTE for Bach Fugues was pre-trained on string quartets, etc.
Classification is binary, i.e., the presented F1 scores are for the positive class, i.e., the cadence
(PAC: Perfect Authentic Cadence; rIAC: root position Imperfect AC; HC: Half Cadence)."* The text
(p. 5): the reference model's figures are *"taken from [4]"*, and *"Only beat-wise scores are given for
the reference model"*.

Bold marks AS READ under §2's bound are shown in bold.

| Dataset | Model | F1 Note | F1 Onset | F1 Beat | Prec. Beat | Recall Beat |
|---|---|---|---|---|---|---|
| Bach Fugues (PAC), 12 fugues | Bigo et al. model | - | - | **0.80** | **0.89** | 0.72 |
| | SGSMOTE | 0.85 | 0.75 | 0.73 | 0.70 | 0.77 |
| | Pretrained SGSMOTE | **0.90** | **0.83** | **0.80** | 0.74 | **0.89** |
| Bach Fugues (rIAC), 12 fugues | Bigo et al. model | - | - | 0.68 | 0.71 | 0.65 |
| | SGSMOTE | **0.87** | **0.75** | **0.73** | **0.75** | 0.72 |
| | Pretrained SGSMOTE | 0.87 | 0.73 | 0.71 | 0.62 | **0.82** |
| Haydn String Quartets (PAC), 21 pieces | Bigo et al. model | - | - | **0.69** | **0.60** | **0.82** |
| | SGSMOTE | 0.77 | 0.56 | 0.59 | 0.47 | 0.78 |
| | Pretrained SGSMOTE | **0.81** | **0.63** | 0.64 | 0.54 | 0.78 |
| Haydn String Quartets (HC), 21 pieces | Bigo et al. model | - | - | 0.29 | 0.19 | **0.56** |
| | SGSMOTE | 0.65 | 0.32 | 0.30 | 0.33 | 0.27 |
| | Pretrained SGSMOTE | **0.69** | **0.44** | **0.41** | **0.41** | 0.41 |

**DERIVED — each beat-wise F1 recomputed from its printed precision and recall, F1 = 2PR / (P + R).**
Bach PAC: reference 0.796, SGSMOTE 0.733, pretrained 0.808; Bach rIAC: 0.679, 0.735, 0.706; Haydn PAC:
0.693, 0.587, 0.638; Haydn HC: 0.284, 0.297, 0.410. **All twelve agree with the printed F1 to within
the rounding of their two-decimal inputs**; the two furthest apart are the pretrained Bach PAC row
(0.808 against printed 0.80) and the reference Haydn HC row (0.284 against printed 0.29).

**DERIVED — beat-wise F1, the model minus the reference:**

| Block | SGSMOTE | Pretrained SGSMOTE |
|---|---|---|
| Bach PAC | −0.07 | 0.00 |
| Bach rIAC | +0.05 | +0.03 |
| Haydn PAC | −0.10 | −0.05 |
| Haydn HC | +0.01 | +0.12 |

**DERIVED — pre-training against no pre-training, beat-wise F1:** Bach PAC +0.07, Haydn PAC +0.05,
Haydn HC +0.11, **Bach rIAC −0.02**; at note level Bach rIAC is 0.87 either way.

**No variance, confidence range or number of runs is printed for any cell of Table 2**, and none was
met in the text as read.

**The authors' reading of Table 2** (p. 5): *"Our model matches or slightly surpasses the state of the
art in rIAC detection in Bach fugues and on HCs in Haydn string quartets but does not reach the
reference model's F1 results in PAC detection. We additionally present a pre-trained version of
Stochastic GraphSMOTE, where the network was first trained on additional data and fine-tuned for the
task."* And: *"Pre-training helps to (markedly) improve the results on HC, catch up with the reference
on PAC in Bach, and narrow the gap on PAC in Haydn."* And: *"Pre-training, and thus the need for
additional data, is the price we pay for the generality of the graph representation and the consequent
size (number of parameters) of the deep network."* And: *"Generally, our results agree with [4] in
implying that half cadences (HC) seem significantly harder to identify than authentic cadences, both
perfect and imperfect."* And: *"In the PAC detection tasks, in particular, we observe comparable or
higher recall of our model compared to the reference, but lower precision."*

**DERIVED, set against those sentences.** The sentences that state what the table shows agree with it
in direction; the sentence on *"the price we pay"* is the authors' explanation and is not a reading of
the table. Two places where the table is narrower than the words: **(a)** Haydn PAC recall is 0.78 for both of the model's
rows against the reference's 0.82, so *"comparable or higher recall"* holds there only under
*comparable*; **(b)** *"significantly"* is not backed by a significance test in the pages as read.

### §5.3 Table 3 — three-class classification by feature set (p. 6)

| Dataset | Features | F1 Note | F1 Beat |
|---|---|---|---|
| Bach Fugues (PAC & rIAC) | general | 0.602 | 0.667 |
| | all | 0.653 | 0.702 |
| Haydn String Quart. (PAC & HC) | general | 0.542 | 0.610 |
| | all | 0.648 | 0.663 |
| Mozart String Quart. (PAC & HC) | general | 0.584 | 0.569 |
| | all | 0.588 | 0.606 |

Caption: *"Three-class cadence classification with two different feature sets. Results were obtained
by 5 fold cross validation (70% of pieces for training, 10% validation, 20% testing); no pre-training.
Feature set all contains all features from Section 3.1; general excludes Category 3 cadence-specific
engineered features."* Text (pp. 5–6): the three classes are *"no cadence, PAC, rIAC (Bach) / HC
(Haydn, Mozart)"*; *"we chose to report the macro averaged F1 score over all three classes. (Macro
averaging was chosen to counter the overwhelming effect of the majority class no cadence)."*

**DERIVED — all minus general:** Bach +0.051 note, +0.035 beat; Haydn +0.106 note, +0.053 beat;
Mozart +0.004 note, +0.037 beat. **All six differences are positive; the Mozart note-level one is
+0.004.** No per-fold spread is printed.

**DERIVED, and this reader's reasoning rather than the page's.** The macro average includes the
*no cadence* class, which is more than 98 % of the notes by the paper's own statement (p. 3). A
classifier that got that class nearly right and both cadence classes wholly wrong would score close to
one third on this measure. **The page states no such floor and prints no baseline row for Table 3**, so
how far 0.54–0.70 stands above a trivial classifier is not given on the page.

**The authors' reading** (p. 6): *"The results (see Table 3) support the relevance of carefully devised
cadence-related features à la [4]. However, also the general-purpose category 1 and 2 features alone
support non-trivial cadence recognition and discrimination performance, which implies that the
relational graph representation in combination with a convolutional approach manages to enrich highly
local features with relevant non-local score context."* **DERIVED:** Table 3 compares two feature sets
with the graph convolution present in both; **it contains no run without the graph convolution**, so
the second sentence's *"implies"* does not rest on Table 3 alone. Table 4 (§5.4) is where the paper
varies the convolution.

### §5.4 Table 4 — convolution depth, PAC in Bach fugues (p. 6)

| Depth | F1 Note | F1 Onset | F1 Beat |
|---|---|---|---|
| None | 0.833 | 0.671 | 0.667 |
| 1-hop | 0.854 | 0.707 | 0.701 |
| 2-hop | **0.869** | **0.737** | **0.732** |
| 3-hop | 0.836 | 0.706 | 0.659 |

Caption: *"Effect of neighbor convolution depth on PAC prediction in Bach fugues. The F1
Note/Onset/Beat scores presented are binary, i.e., for the PAC class. Depth refers to neighbor
convolution depth. None means no graph convolution."* Text (p. 6): *"Convolution depth refers to the
number l of hidden layers of the encoder and the subsequent neighbor sampling up to l-hop neighbors.
Our results (see Table 4) suggest that neighbor convolution clearly contributes to learning non-local
features. Best results are achieved when using a convolution depth of 2. Increasing the receptive field
beyond that level, we observed some instabilities emerging in the learning model, which could be
attributed to the common vanishing gradient problem in deep GCNs [22]."*

**DERIVED.** None to 2-hop: +0.036 note, +0.066 onset, +0.065 beat. 3-hop's beat F1, 0.659, is below
None's 0.667. **The training and test split, and whether pre-training was used, are not stated for
Table 4**; the caption names only the task and the corpus. Its 2-hop row (0.869 / 0.737 / 0.732) is
not the Table 2 SGSMOTE Bach PAC row (0.85 / 0.75 / 0.73), though the settings of §4.4 fix L = 2; the
page does not say why the two differ. **No variance or number of runs is printed**, so whether
*"clearly"* exceeds run-to-run spread is not given on the page.

### §5.5 Figures used as evidence (pp. 5–6, §6.2)

The authors motivate the section by precision: *"Motivated by the fact that our model, while higher on
recall, seems to be lower on precision than the model in [4], we take a closer look at some of the
false positives in individual examples. Our findings suggest that many false positive predictions
resemble cadences, in terms of tonal structure or implications, and could be considered and annotated
as such, but lack some main components"* (p. 6). Three examples:

1. **Figure 4, fugue no. 19 (WTC I).** It is numbered among Table 2's test fugues (13–24); which
   trained model produced Figure 4 is not stated. *"The cadence prediction
   by our model on the downbeat of bar 23 is a false positive, according to the ground truth
   annotation. However, one could argue that the passage clearly has a cadence-like role, marking the
   end of the 2nd fugal episode and the return to the original tonality of A major [23]."* Reference
   [23] is a web page, *"Bach: Prelude and fugue no.19 in a major, bwv 864 analysis," May 2018*, at
   tonic-chord.com (p. 8).
2. **The passage of [4]'s Figure 4.** *"a pattern occurs that has all the technical ingredients of a
   PAC, but was not annotated as such for (debatable) higher-level musicological considerations. Again,
   our model's PAC prediction there counts as a false positive."* No figure of it is given in this
   paper.
3. **Figure 3, Haydn op. 54 no. 1, 2nd mvt., mm. 33–45.** *"We observe two false positive beat-wise
   predictions (8 if we count note-wise) in bars 39 and 44, respectively, following a true PAC on the
   beginning of bar 34. A harmonic analysis of these bars indicates a proper PAC preparation with
   text-book voice leading on the cadence arrival point in every occasion. These two false positive
   PACs form part of a modulating melodic and harmonic sequence; whether to classify them as cadences
   is a matter of higher-level musicological considerations."* Figure 3's caption: *"True negatives are
   marked with red, true positives with green, false positives with blue. A partial analysis shows the
   chords towards the end of cadences and highlights a modulating sequence where every sequence ends
   with a cadential pattern, which counts as false positive predictions by the network."* The figure's
   bands read *"Theme"*, *"1st Variation"* and *"Modulating Melodic and Harmonic Sequence"*.

The section's own bound (p. 6): *"We cite these few qualitative examples in an attempt to show that
our prediction model can identify many more cadential patterns than the raw experimental figures
suggest"*.

## §6 — The claims, labeled

Labels as the §4 form uses them: **FACT** — stated or measured in this paper, at the locator;
**THEORY** — established published method the paper adopts by citation; **CONJECTURE** — argued,
hedged or not measured in the pages as read. Where the paper hedges, the hedge is quoted.

1. **FACT (Table 2, p. 5).** On beat-wise F1 the model trails the reference on PAC in both corpora
   without pre-training (Bach −0.07, Haydn −0.10), ties it on Bach PAC with pre-training, and leads it
   on Bach rIAC and Haydn HC (DERIVED differences, §5.2). Single values; no spread printed.
2. **FACT, with a word the table does not fully carry (abstract, p. 1).** *"We obtain results that are
   roughly on par with the state of the art"* — true in direction by §5.2's differences; *"roughly"* is
   the authors' word for gaps up to 0.10 beat F1 on Haydn PAC.
3. **FACT (Table 2).** The model predicts at note, onset and beat level; the reference is reported at
   beat level only. Onset and beat levels are aggregations whose rule is not stated (§3).
4. **FACT (Table 2), with a scope the page does not state.** Pre-training on the other corpus raises
   beat F1 in three of four blocks and lowers it on Bach rIAC by 0.02 (DERIVED). The authors' sentence
   names the three gains and not the loss.
5. **FACT at the values; the adverb is not established (p. 5).** HC is harder than PAC and rIAC in
   these tables (Haydn HC beat F1 0.29–0.41 against 0.59–0.80 elsewhere). *"significantly"* carries
   no test in the pages as read.
6. **FACT (Table 3, p. 6).** Adding the cadence-specific Category 3 features raises macro F1 in all six
   cells, by +0.004 to +0.106 (DERIVED). Five-fold cross-validation; no spread printed.
7. **CONJECTURE (p. 6), the paper's *"implies"*.** That the graph convolution *"manages to enrich highly
   local features with relevant non-local score context"*, read off Table 3 — Table 3 holds the
   convolution fixed (§5.3). The page's measured support for a convolution effect is Table 4.
8. **FACT at one task, one corpus, one value per cell as printed (Table 4, p. 6); the paper hedges.**
   *(★ CORRECTED AT THE USER-ORDERED CHECK. Former wording, preserved (#12): "one run as printed" — the
   page does not say how many runs stand behind a value.)* Depth 2 is
   best on all three levels for Bach PAC; depth 3 falls below no convolution at beat level. The
   authors' verb is *"suggest"*; their adverb *"clearly"* is not set against a spread.
9. **CONJECTURE (p. 6).** The instability beyond depth 2 *"could be attributed to the common vanishing
   gradient problem in deep GCNs [22]"* — hedged by the authors; not measured.
10. **CONJECTURE (p. 1; argued, not measured).** That the model *"makes fewer task-related and musical
    assumptions, resulting in more general applicability"* — the authors say *"we will argue"*; no
    experiment in the pages as read measures applicability.
11. **CONJECTURE (p. 6, §6.2).** That *"many false positive predictions resemble cadences"* — the
    ground is *"these few qualitative examples"*, three in number, one of them resting on a web page
    [23]. No count of false positives reviewed was met in the pages as read. *(★ CORRECTED AT THE
    USER-ORDERED CHECK — a negative given its bound. Former wording, preserved (#12): "No count of false
    positives reviewed is given.")*
12. **FACT as a statement of design (p. 6, conclusion).** The model *"can learn using only local note
    features, without the need for any musical assumptions about cadence anchor points"*. Its local
    features include Category 3, cadence-specific engineered features (§4.2), in Table 2's runs
    (*"using all available features (as in the first experiment, feature set all in the table)"*,
    p. 5). The sentence is scoped to *anchor points*, and at that scope the page supports it.
13. **THEORY (pp. 3–4).** GraphSAGE [20], SMOTE [21] and GraphSMOTE [5] are adopted by citation. The
    changes the page names are *"some major differences, mainly to adapt for stochastic training"*,
    with *"The main novelty of our model is that the SMOTE is performed for each batch separately"*
    (§4.3). *(★ CORRECTED AT THE USER-ORDERED CHECK. Former wording, preserved (#12): "the changes the
    paper makes are per-batch SMOTE in the latent space and stochastic neighbour sampling" — stated as
    the whole of the changes, and with a latent-space placement the page does not call a change.)*
14. **CONJECTURE, stated by the authors as an assumption (p. 4).** *"Performing SMOTE in the latent
    space assumes that a more appropriate representation for the generation of the synthetic minority
    samples is learned."* And of the decoder: *"it should also give adequate edge predictions for
    synthetic nodes"* — not measured in the pages as read.
15. **Bounded by the authors (p. 2).** *"However, to our knowledge, there exists no method employing
    deep learning models to solve the task."*
16. **FACT as a coupling statement (p. 3).** The Haydn ground truth is Sears and colleagues' [19]; the
    Bach ground truth is [11]'s; the Mozart ground truth is [18]'s.

## §7 — Residues: print defects, and things this reader derived

1. **The "less than 2%" statement against Table 1** (p. 3 text; p. 4 caption). If the PAC, rIAC and HC
   columns count nodes, the Haydn row sums to about 2.1 % and the Mozart row to about 4.4 % of nodes
   (DERIVED, §5.1). The page does not say which the columns count. **Recorded as unresolved at the
   page.**
2. **The Haydn corpus size: 42 or 45.** p. 1 says [4] *"was tested on two annotated datasets: 24 Bach
   fugues and 42 Haydn string quartet expositions"*; p. 3 says *"we used two datasets also used by Bigo
   et al. [4]"* and that the second *"contains 45 movement expositions from Haydn string quartets"*;
   Table 1 prints 45 pieces; Table 2's Haydn split is *"random 21:21"*, which is 42 (DERIVED). The
   page does not reconcile the two counts. *(Declared: this reader knew from row 37's second extract,
   read for its form, that [4] reports 42 expositions.)*
3. **"the final I (i)" and half cadences** (p. 3, §4). The sentence *"The manual annotations in these
   datasets mark a cadence as occurring on the beat where the final I (i) arrives"* is written for
   every dataset, and HC is one of the classes detected. A half cadence arrives on V, so **as a
   description of the HC annotations the sentence is too narrow — this reader's reading of the music
   theory, not printed.** Where the HC labels sit is not otherwise stated.
4. **The Bach rIAC row label** (Table 2, p. 5). The block is labelled *"Bach Fugues (rIAC)"*; the
   caption glosses rIAC as *"root position Imperfect AC"*. Whether the reference model's 0.68 is for
   rIAC alone or for another grouping is not stated on these pages. *(Declared: row 37's second
   extract, read for its form, records [4]'s Bach target as PAC+rIAC. That is not checked here against
   [4], and it is not this paper's text.)* **Recorded as a question at the page, not as a defect.**
5. **Table 4 against Table 2** (pp. 5–6): the 2-hop Bach PAC values differ from Table 2's SGSMOTE Bach
   PAC values, and Table 4's setup is not stated (§5.4).
6. **A printed equation that reads as a slip** (p. 3, §5.1): the third encoder line is printed
   *"h^(l+1)_i = norm(h^l_i)"*. Normalising the layer's own new output would read norm(h^(l+1)_i).
   **Recorded as printed; the correction is this reader's inference.**
7. **One letter, two meanings** (pp. 3–4): *k* is the SMOTE nearest-neighbour count (*"k = 3 for
   SMOTE"*) and also the sampling depth (*"up to their k-hop neighbors"*); *L* and *l* are also used
   for depth (*"the number l of hidden layers"*, p. 6). Noted for a reader; no value is affected.
8. **Print slips that move no value**: *"higher lever information"* (p. 3; *level* is meant);
   *"tree-class problems"* (p. 5; *three-class*); *"Allegraud and al."* (p. 3); *"mtv ii"* in Figure
   3's header (p. 5), where the caption has *"Mvt. II"*; *"an Support Vector Machine"* (p. 1).
9. **A record-facing observation, not judged.** Reference [12] prints its authors as *"P. R. Illescas,
   D. Rizo, and J. M. I. Quereda"* (p. 7). The `reading_pass/extracts/` listing shows a file named
   `illescas-rizo-inesta-2007-harmonic-melodic-and-functional-automatic-analysis.md`. Whether the two
   name the same paper was not looked up.

## §8 — Closing: what the read-back and the sweep found, written after §0–§7 stood

**The read-back.** §0–§7 were checked claim by claim against the page images as delivered in this
sitting (the paper was not re-requested), and against this sitting's own reads for §0. Every quotation
was set against its page; every table value against its table; every DERIVED figure was recomputed a
second time by hand, including the twelve F1 recomputations of §5.2, whose two widest deviations
(0.808 against 0.80, 0.284 against 0.29) were checked against the rounding interval of their inputs
and lie inside it.

**What it found, corrected before landing** (the first wording was never landed, so it is recorded
here rather than preserved at its site):

- §2 said the best value per column *"is marked bold"*, which stated the meaning of the bold as the
  page's. The page does not state it, and the Bach rIAC block's tied 0.87 is bold once as read. Now
  stated as this reader's reading, with the tie.
- §3 said chord-type information *"enters only as interval-set matches"* — wider than §3.1's text,
  which does not say what the Category 3 and [15] features encode. Now bounded to where §3.1 names it.
- §4.3 joined two of the page's phrases into *"the Euclidean space of the latent representation"*. Now
  quoted as two phrases.
- §5.2 said *"Each sentence agrees with the table in direction"*, where one of the quoted sentences
  (*"the price we pay"*) is an explanation, not a reading of the table. Now scoped.
- §5.3 said *"more than 98 % of the nodes"*, where the page's statement is about notes. Corrected.
- §5.5 called fugue no. 19 *"a test-half fugue by Table 2's split"*, which could be read as saying
  Figure 4 came from that run. Now says the page does not state which model produced it.

**The sweep.** A search for *all, every, none, never, only, whole, complete, nothing, nowhere, always,
entire, exhaustive, total, any, each, clearly, independent* over the file, each hit read at its line.
Two of the corrections above came from it (*"only"* in §3; *"Each sentence"* in §5.2). The remaining
hits were quotations, counts this reader checked (*"All twelve"*, *"All six"*, *"all three levels"*),
or statements bounded to the pages as read.

**What neither act did.** Neither re-opened the page images at a larger size; the Table 2 bold marks
stand under §2's bound. Neither opened the first extract. Nothing here says a further pass would come
back empty.

## §9 — The cross-check against the first extract, run after §0–§8 had landed

§0–§8 landed at 42,588 bytes (device modification time 1789897025541) before the first extract was
opened. The first extract was then read whole (13,786 bytes, modification time 1788187991737, 201
lines), and **PDF page 5 was requested again alone** to settle the Table 2 marks; it confirmed §5.2's
reading. *(★ CORRECTED AT THE USER-ORDERED CHECK. Former wording, preserved (#12): "it came back at the
same size and confirmed" — the image's size was not measured.)* The line numbers below are the first extract's as read,
before any correction.

### §9.1 What the comparison reached

Every value both reads transcribed; every quotation of this paper the first extract carries, set against
its page *(★ CORRECTED AT THE USER-ORDERED CHECK. Former wording, preserved (#12): "every quotation the
first extract carries" — its quotations of the charter and of row 37's paper were not compared, as the
next sentence says)*;
and the first extract's claims, coupling facts, verdicts and findings, **at what they say about the
paper**. **Outside the comparison:** what the first extract says about the record — the charter's
*".29 and .41"* sentence, V6, DP-I, the L0 contract, row 37's own tables and false positives, and the
extract's centrality verdict. None of those objects was opened.

### §9.2 Where the two reads agree

Every digit of Tables 1 to 4; the 135 features and their three categories; the three edge types; the
four-part model; the note, onset and beat levels with aggregation; footnote 4's exclusions; and the
quotations at lines 41–45, 85–88, 97–100, 107–109, 110–113 and 131–133 and finding (4)'s *"is a matter
of higher-level musicological considerations"* (line 176), which stand on their pages as printed.
*(★ CORRECTED AT THE USER-ORDERED CHECK. Former wording, preserved (#12): "the quotations at lines 41–45,
97–100 and 110–113" — four agreeing quotations were left out of the list.)*

### §9.3 Departures that touch no value, finding or verdict — resolved at the page, and corrected in the first extract under the standing rule of handoff entry 198 §7

- **(a) Four bold marks in Table 2** (lines 70, 72, 76, 79). The page sets the reference model's
  Bach PAC precision 0.89, the pretrained model's Bach PAC beat F1 0.80 and the reference model's Haydn
  PAC precision 0.60 in bold, where the first extract prints them plain; and it sets the reference
  model's Haydn HC beat F1 0.29 plain, where the first extract prints it bold. Read twice at page 5, under
  §2's bound. **No digit differs.**
- **(b) A dropped word** (line 47): the page prints *"we make no assumptions on and reference to"*; the
  first extract drops *"on"*.
- **(c) A changed word and a dropped word** (lines 56–57): the page prints *"three different levels,
  note-wise, onset-wise and beat-wise predictions"*; the first extract has *"scales"* for *"levels"*
  and drops *"predictions"*. (Bare *scale* is also a reserved word under `CLAUDE.md`'s Conventions.)
- **(d) A changed word** (line 84): the page prints *"rIAC detection in Bach fugues"*; the first extract
  has *"on"*.
- **(e) A quotation stopped mid-sentence** (lines 104–105): it closes at *"in the learning model."*,
  where the page continues *", which could be attributed to the common vanishing gradient problem in
  deep GCNs [22]"*.
- **(f) A changed word** (line 114): the page prints *"high-level musical considerations"* (p. 6); the
  first extract has *"higher-level"*.
- **(g) A singular for three** (line 109): *"The worked case is Haydn Op. 54 No. 1 II"* — §6.2 works
  three examples (§5.5).
- **(h) Negatives without their bound** (lines 122 and 127–128): *"No chord segmentation, no harmonic
  analysis, no decided tonality"* and *"Nothing else: no chord, no key, no segmentation."* The page
  describes none of those steps or outputs; it does not say it lacks them, and its classifier's
  softmax is called *"the predicted class probabilities"* (p. 4).
- **(i) A claim wider than the table** (line 133): *"Pre-training on a second dataset is required for
  the best figures."* In the Bach rIAC block the best beat-wise figures are the model's without
  pre-training (§5.2).
- **(j) An unprinted gloss in the stated scope** (line 134): *"The method cannot reach form-level
  judgements, by design."* The page's limit is *"high-level musical considerations such as, e.g.,
  whether PAC-like patterns that occur in sequence should count as PACs or not"* (p. 6). *Form-level*
  is not its word.
- **(k) A locator** (lines 35–37): the key signature as a node feature is in Figure 1's caption (p. 2),
  not in §3.1's text, which names the time signature.

### §9.4 Three places inside or beside a finding or a verdict — NOT corrected; they stand with the user

Under the user's ruling of 2026-09-19 (handoff entry 200 §1 item 2), a word the page does not print or
does not bear, inside or beside a finding or verdict, goes to the user.

- **(A) "a different corpus"** — finding (2), line 161: *"an independent method, a different corpus,
  the same conclusion."* The page says the opposite for the corpus: *"we used two datasets also used by
  Bigo et al. [4]"* (p. 3), and the first experiment uses *"the same data and train/test setup"* as [4]
  (p. 4), whose figures are *"taken from [4]"* (p. 5). The Haydn HC comparison the finding rests on is
  on that shared corpus, and the Haydn annotations are Sears and colleagues' [19] (p. 3). The same shape
  appears beside it: the heading *"The independent replication"* (line 90), finding (4)'s *"Two
  independent studies"* on the annotation question (line 177), and finding (2)'s quotation, which drops
  the page's *"(HC)"* with no gap mark (line 160). **The method is different; the corpus and the
  annotations are not, at the page.**
- **(B) "consistently the highest"** — the "Adopt as evidence" verdict, lines 138–141: *"the note-level
  figures are consistently the highest of the three."* Tables 2 and 4 bear it. **Table 3 prints the
  note-level macro F1 below the beat-level one in five of its six cells** (§5.3). The page does not
  compare the levels itself; that F1 over notes and F1 over beats count different units is this
  reader's observation.
- **(C) "shows"** — the "Adapt" verdict, lines 142–144: *"The general-feature arm of Table 3 shows a
  graph's neighbourhood supplies context that hand-designed anchor heuristics were previously
  carrying."* Both arms of Table 3 carry the graph convolution, and neither carries [4]'s anchor
  heuristics (§5.3). The page's measurement of the convolution is Table 4, Bach PAC only, single values.
  Finding (3), lines 166–167, rests on the same ground (*"by letting a graph supply the surrounding
  context"*). There *"comparable"* is the paper's own word, and the attribution to the graph is the
  paper's *"implies"* (§6 item 7).

**Recommendation, as rows 7, 17, 35 and 37 were ruled:** correct each at its site, with the former
wording kept (#12): (A) to say the method differs and the corpus and annotations are shared, at the
page's words; (B) to bound the claim to Tables 2 and 4 and state Table 3's contrary cells; (C) to rest
the verdict on Table 4 at its scope, and to note the same ground at finding (3).

*(★ This section's heading, "NOT corrected; they stand with the user", is made stale by the user's
ruling of 2026-09-20, his words "I agree with 1 for all three.", and by the act under it: all three
places are corrected in the first extract at their sites, with the former wording kept. The heading and
the text above are left standing (#12).)*

### §9.5 What this read carries that the first extract does not

The Table 1 row sums against *"less than 2%"* (§7 item 1); the 42/45 Haydn count (§7 item 2); the
*"final I (i)"* sentence against HC (§7 item 3); the F1 recomputations and the model-minus-reference
differences (§5.2); pre-training's loss on Bach rIAC (§5.2); the macro-F1 floor and the absent baseline
in Table 3 (§5.3); Table 4's unstated setup and its difference from Table 2 (§5.4); the printed encoder
slip (§7 item 6); and the absence of any spread in Tables 2–4.

### §9.6 What the cross-check did not do

It did not open any object the first extract's record-facing half names, and it did not re-open any
page but page 5. **This file's §0–§8 are unchanged by §9.**

## §10 — The user-ordered check, 2026-09-20, written in the act that ran it

**The order, the user's words:** *"Fact AND source-check what you have written for completeness,
coherence, correctness and possible misuse of hyperboles and absolutes (everywhere, nowhere,
comprehensive, total, exhaustive, complete and the likes). Correct where needed."* It came in the same
message as the ruling on §9.4.

**What was checked.** This file was re-read whole as it stood after §9.4's note, each claim against its
object: the paper's page images as delivered in this sitting (no page re-requested for the check), the
first extract as read, and this sitting's own reads for §0. The first extract was re-read whole after
the act under the ruling. An absolutes search, widened by the user's words (*comprehensive, everywhere,
fully, wholly, consistently*) to the list §8 names, was run over both files, and each hit was read at
its line.

**What it found in this file, corrected at the sites with the former wording kept (#12):**

- §2: the account of the bold marks named *"the one tie met"*, where Table 2 has a second tie for
  highest (Bach PAC beat F1 0.80, reference and pretrained, both bold). §8's first bullet records the
  first wording and is left standing.
- §3: in the chord-type bullet, the quotation stood after a sentence it does not belong to. It was
  moved, and no words were changed.
- §6 item 8: *"one run"*, where the page prints one value per cell and does not say how many runs
  stand behind it.
- §6 item 11: a negative (*"is given"*) without its bound.
- §6 item 13: the changes to GraphSMOTE stated as the whole of them, with a latent-space placement the
  page does not call a change.
- §9 opening: *"came back at the same size"*, which was not measured.
- §9.1: *"every quotation the first extract carries"*, wider than the comparison, which left out its
  quotations of the charter and of row 37's paper.
- §9.2: the list of agreeing quotations left four out.
- Two lines were re-wrapped (§4.3, §5.2), with no words changed.

**What it found in the first extract, corrected:** the banner's sentence on the three places, now
stale, is marked so (#12); and one note line was re-wrapped. The act under the ruling was also checked
at each site against §9.4 and the pages quoted there.

**Hits read and left standing:** quotations of the paper, the commission's term *independent
extraction*, counts this reader checked (*"All twelve"*, *"All six"*, *"all three levels"*,
*"every row that reports it"*), and statements bounded to the pages as read. In the first extract,
several absolutes stand in its record-facing half: finding (1)'s *"both read whole"*, finding (5)'s
*"Nothing read contradicts any CHOSEN design point"*, and the provenance line *"Every value above is the
paper's own"*. The objects they rest on were not opened, so they are neither confirmed nor corrected
here. The Centrality sentence *"has not been performed"* is stale and is left for the progress update.

**What this check did not do.** It did not re-request any page, open the charter or any record the
first extract's record-facing half names, or re-read row 37's paper. Nothing here says a further pass
would come back empty.
