# Second extraction — Yang, Cwitkowitz & Duan, "Harmonic Analysis with Neural Semi-CRF"

> **What this file is.** The SECOND independent extraction of row 19 of Task B's L2 slice, written
> under `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, which was read at its own
> source in this sitting and not relayed: *"CENTRAL sources — any paper whose claims would carry
> load in a detail specification or against a design point — are extracted in a SECOND independent
> pass (a fresh session, or a cleanly separated re-read that does not consult the first extract) and
> the two extracts cross-checked; disagreements are resolved at the paper or recorded as
> unresolved."*
>
> **Nothing in this file is a ruling.** It records what one read of the paper found. Where it says
> the paper is wrong about itself, the derivation is printed so the verdict can be checked rather
> than trusted.

---

## §0 — What was read, and the bound on this read's independence

**The held document.** `docs/research_papers/yang_cwitkowitz_duan_2023_ismir_harana_neural_semi_crf.pdf`,
**318,293 bytes**, proved at this sitting's own staging call. **Eight pages**, established AT THE
TOOL by a deliberately out-of-range page request, which answered *"PDF has 8 pages"* — not taken
from any row of the record, the progress record having not been opened in this sitting at all.

**All eight pages were read whole as page images, and all eight were then re-opened at the
read-back** — the requests are named at §8.1 rather than counted here. **Every image was checked for
presence and legibility at the image itself, not at the call's success line** — the page-image fault
the record carries can return a success line and no image.

**The independence bound, stated rather than claimed away.** This read did not consult the first
extract before its §9 was written; the first extract was not opened, staged, listed or searched
until step 7 of the procedure. **But independence here is partial and the contamination is named:**

- **The candidacy line was read before the paper was opened**, and it carries a reason.
  `reading_pass/candidacy_upgrades.md` **line 81** reads: *"Yang, Cwitkowitz & Duan, ISMIR 2023,
  harmonic analysis with neural semi-CRF (Harana)"*, held, **ADMITTED**, reason *"The neural
  semi-CRF; DP-C's largest-ablation-contributor evidence, and a current candidate architecture for
  L2."* **So this read knew before opening the paper that the record expects an ablation result from
  it, and which direction that result is expected to point.** That is contamination and it is
  written down rather than claimed away.
- **The handoff entries of this line were read whole at boot** — the hundred-and-seventy-sixth, the
  hundred-and-seventy-fifth, the hundred-and-seventy-fourth and the hundred-and-sixty-ninth. **None
  of them states anything about this paper's content**; the hundred-and-seventy-sixth names row 19
  by its authors, venue and the candidacy line's reason, and nothing more.
- **The section form of this file was taken from row 11's second extract's SECTION HEADINGS ALONE**,
  by a heading search. **No content line of that file was read.**

**What this read did NOT do, so no reader assumes it did.** **No sweep of the repository was run for
this paper** — not for its authors, not for its title, not for any of its values. `FRAMEWORK.md` was
not opened at all. The findings surface, `population.md`, the slice derivation,
`docs/research_papers/BIBLIOGRAPHY.md` and `reading_pass/l2_slice_reading_progress.md` were not
opened at all. **So this file asserts NOTHING about what the record says of this paper.** That half
lives in the first extract, and §9 records exactly how far the cross-check reaches into it.

**None of the paper's own references was opened.** Where this file says something about a cited
work, it says it from the reference list as printed on pages 7 and 8, and says so at the point.

---

## §1 — What the paper is, and the identity axis

**Title, as printed on page 1:** HARMONIC ANALYSIS WITH NEURAL SEMI-CRF.

**Authors, as printed:** Qiaoyu Yang, Frank Cwitkowitz, Zhiyao Duan. **Affiliation:** University of
Rochester. Contact addresses are printed beneath the affiliation.

**Venue and year.** The running header on pages 2 through 8 reads *"Proceedings of the 24th ISMIR
Conference, Milan, Italy, November 5-9, 2023"*. Page 1 carries an attribution line: *"Q. Yang, F.
Cwitkowitz, and Z. Duan, "Harmonic Analysis with Neural Semi-CRF", in Proc. of the 24th Int. Society
for Music Information Retrieval Conf., Milan, Italy, 2023."*

**Printed page numbers:** 676 through 683.

**Licence, printed on page 1.** *"© Q. Yang, F. Cwitkowitz, and Z. Duan. Licensed under a Creative
Commons Attribution 4.0 International License (CC BY 4.0)."*

**★ NO IDENTITY FINDING.** Every axis the candidacy line carries — authors, venue, year, subject —
is printed in the held document and agrees with it. **This is worth stating because it is not what
the two members before this one produced**: the entries this side read record row 11's held document
as printing no venue, no year and no copyright or licence line on any page, and row 10's held
document as the arXiv preprint rather than the article the record's row names. **This one prints all
of it, licence included.**

**The system has a name:** **Harana**. The paper gives a source-code location in a footnote on page
1 (a GitHub repository under the first author's account). **That repository was not visited** — no
web access was made in this sitting.

**Grant acknowledgement, page 7:** two National Science Foundation grants are named by number, and a
third NSF grant is named for the second author's synergistic activities.

---

## §2 — The method, as the paper states it

### §2.1 The problem the paper says it is solving, and the gap it claims

The paper's own framing, §1: harmonic analysis has **two components — recognising harmony labels and
finding their time boundaries** — and the abstract says *"Most of the previous attempts focused on
the first component, while time boundaries were rarely modeled explicitly. Lack of boundary modeling
in the objective function could lead to segmentation errors."*

§2 states the shape of the prior work it is departing from: two-stage methods where *"the first stage
outputs frame-level chord labels and the second stage smooths frame-level labels with
post-processing"*, which the paper says *"could still suffer from segmentation errors"*. It then
names **Masada and Bunescu** as having *"relaxed the constraint on fixed-size time-span of the output
prediction"* with a semi-CRF, **and states the limitation it builds on**: *"the features to the
semi-CRF are entirely rule-based, which means they are not necessarily optimal for the end task."*

**The paper's three stated contributions, as its own bullet list prints them (§1):**

1. *"Proposing the first neural semi-CRF model to jointly estimate harmony labels and their time
   boundaries"*;
2. *"Proposing an attention-based score function to alleviate the influence of extra non-chordal
   notes and missing chordal notes"*;
3. *"Proposing a novel absence score to improve the robustness to imperfect harmony profiles."*

### §2.2 The input representation

**Framing.** §3.1.1: the piece is sliced into frames **one eighth of a beat long**. The paper gives
its reason: *"We use beat instead of note duration in order to represent the basic time unit because
music with different meters may have different distributions on the note length."*

*(★ CORRECTED AT THE CROSS-CHECK, AND THE DEFECT WAS THIS SIDE'S. FORMER WORDING, PRESERVED (#12):
*"We use beat instead of note duration **to represent** the basic time unit …"* — **two words, *in
order*, dropped from inside a quotation with no ellipsis.** Resolved at printed page 677, read a
third time at the page. **The first extract quotes the sentence correctly, and it is that file's
having it right that exposed this one's error** — the same shape the hundred-and-seventy-fifth
records of its own member. No value moves and the sense does not change; the standing ground is that
a quotation is reproduced as printed.)*

**Per frame, 24 dimensions:**

- a **12-dimensional pitch-class distribution vector**, described as *"the normalized distribution of
  the duration of each pitch class in the frame"*;
- a **12-dimensional one-hot bass vector** indicating the pitch class of **the lowest sounding note**
  in the frame. The paper's stated reason: *"To help distinguish between harmonies with the same
  pitch class vector."*

### §2.3 The label representation, and what the paper deliberately gave up

§3.1.2 is where the paper states a scope decision rather than a method. It names the Roman-numeral
encoding as *"a popular representation … where the full harmonic context of a label, including tonic
and degree, is considered"*, and then states two obstacles:

- *"the combination of all the components produces 47k different harmony labels, which are
  intractable for a classification model with limited training data"*;
- classifying each component independently *"is incompatible with semi-CRF because the boundary of
  each component must be the same."*

**The compromise the paper states:** *"we use a subset of the harmony components, root and quality,
and model them jointly."*

- **Root:** a 12-dimensional one-hot vector over the 12 pitch classes.
- **Quality:** a 10-dimensional one-hot vector over *"10 commonly used classes"*. **The ten classes
  are named nowhere in the eight pages as read.**
- **A third representation, used only inside the neural scoring function:** the **pitch-class
  activation vector**, 12-dimensional and **multi-hot**, *"circularly shifted from the pitch-class
  activation vectors rooted at C"*. The paper attributes the effectiveness of this label encoding to
  a prior work by citation.

### §2.4 Semi-CRF, as the paper sets it up

§3.2. Input frames `X = ⟨X₁ … X_N⟩`; output `Y = ⟨Y₁ … Y_K⟩`, a sequence of **contiguous
non-overlapping labelled segments**, `N` the number of frames and `K` the number of segments. Each
segment is a three-part tuple `Yᵢ = (uᵢ, vᵢ, lᵢ)` — **onset frame, offset frame and label**.

Equation (1) is the conventional semi-CRF: `P(Y|X) = e^{WF(Y,X)} / Z(X)`, with `F` a feature vector,
`W` a learnable weight matrix, and `Z(X) = Σ_Y e^{WF(Y,X)}` described as *"a normalization factor
summarizing all possible segmentation and labeling of the input sequence"*.

Equation (2) is the paper's generalisation: the weighted-feature quantity is replaced by a **neural
score function** `S(Y,X)`, giving `P(Y|X) = e^{S(Y,X)} / Z(X)`.

Equation (3) decomposes it, **under a stated assumption** — *"With the assumption that the harmony
labels are Markovian given the music input"* — into `S(Y,X) = Σ_{i=1}^{K} Sᵢ(Yᵢ, X; Y_{i−1})`, and
the paper then drops `Y_{i−1}` from the notation.

**Figure 1** (page 3) illustrates the arrangement on a 16-frame example. Its caption: *"The semi-CRF
architecture in the context of harmonic analysis. The total score is computed from music input and a
set of candidate harmony segments. Numbers in the blue squares are the frame indices. Numbers in the
green rectangles are the indices of candidate harmony segments."* **Read at the figure image**: four
candidate segments partition frames 1–16 as **1–3, 4–8, 9, and 10–16** — lengths 3, 5, 1 and 7,
summing to 16 — and the total is printed as
`S(Y,X) = S₁(Y₁,X) + S₂(Y₂,X) + S₃(Y₃,X) + S₄(Y₄,X)`.

### §2.5 The frame-level front end

§3.3. The architecture is a **DenseNet–GRU** followed by fully connected layers, with **separate
linear heads** for the three harmony representations. Softmax produces the root and quality class
distributions; **sigmoid** produces the pitch-class activations. Equation (4):

- `E(n) = MLP(GRU(DenseNet(X_n)))`
- `D̂_R(n) = Softmax(FC_R(E(n)))`
- `D̂_Q(n) = Softmax(FC_Q(E(n)))`
- `P̂C(n) = Sigmoid(FC_PC(E(n)))`

The paper attributes the DenseNet–GRU choice to a cited work (see §7.1 for a defect at that
sentence).

### §2.6 The attention-based scoring function — the paper's second contribution

§3.4. The stated problem: for each candidate region the frame-level estimates must be aggregated,
and *"A simple method would be taking the average or the mode, but we note that a harmonic region is
not likely to contain homogeneous harmonic content."* The stated remedy: weigh frames by how similar
they are to the candidate label.

Equation (5), which the paper calls *"the scaled dot-product attention"* and attributes by citation:

`A(Q,K,V) = Σ_{i=1}^{N} Qᵀ Kᵢ Vᵢ / √d`

with `Q` the query vector, `K` the key sequence, `V` the value sequence, `d` the vector size. **This
equation as printed carries no softmax; see §7.1.**

Equation (6) instantiates it — the estimated frame-level harmony sequence of the candidate region is
**both key and value**, and the candidate region-level harmony is **the query**:

`Ĥ_CI(Yᵢ) = A(H(lᵢ), Ĥ(uᵢ : vᵢ), Ĥ(uᵢ : vᵢ))`

where `H(lᵢ)` is the candidate label's harmony representation — *"which can be root `D_R`, quality
`D_Q` or pitch class activation `PC`"* — and `Ĥ(uᵢ : vᵢ)` is the estimated frame-level sequence over
the region's frames.

Equation (7) is the similarity, by dot product: `S_iᴴ(Yᵢ, X) = H(lᵢ)ᵀ Ĥ_CI(Yᵢ)`.

Equation (8) is the transition part:
`S_iᵀ(Yᵢ) = T[l_{i−1}, lᵢ] + (vᵢ − uᵢ) T[lᵢ, lᵢ]`,
where **`T` is a transition matrix of frame-level harmony transition log-probabilities,
pre-computed from the ground-truth labels in the training data** — not learned by gradient descent
with the rest.

Equation (9) combines them across the three harmony representations, with a balancing
hyperparameter: `Sᵢ(Yᵢ, X) = Σ_H S_iᴴ(Yᵢ, X) + λ S_iᵀ(Yᵢ)`.

**Figure 2** (page 4) shows the pipeline: a music segment enters DenseNet → GRU → fully connected,
producing estimated root (softmax), quality (softmax) and pitch activations (sigmoid); the candidate
segment harmony supplies the query and the estimated harmonies supply key and value to an attention
block, whose output feeds the segment score.

### §2.7 The absence score — the paper's third contribution

§3.5. The stated problem: when there are many non-chordal notes or missing chordal notes, the
estimated distributions *"would be relatively flat"* and the pitch-class activation vector *"would
not align well with a chord template"*.

The mechanism: **the complement of the input pitch-class vector is sent through the same front end.**
Equation (10): `X_n[1:12] = 1 − X_n[1:12]`. The harmony information estimated from this **inactive**
music is then compared against the candidate harmony vectors, and **that similarity is to be
minimised**. Equation (11): `AS_iᴴ(Yᵢ, X) = − H(lᵢ)ᵀ Ĥ_CIᶦⁿᵃᶜᵗ(Yᵢ)` — a **negated** dot product.

Equation (12) is the complete segment score:
`Sᵢ(Yᵢ, X) = Σ_H S_iᴴ(Yᵢ, X) + AS_iᴴ(Yᵢ, X) + λ S_iᵀ(Yᵢ)`.

*(★ A PRECISION ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK and marked here (§9.4): **the
scope of the `Σ_H` in Equation (12) is ambiguous as printed.** The equation is set over two lines
with the summation sign opening the second, so whether the absence term and the transition term sit
inside the sum over harmony representations or beside it cannot be told from the typesetting.
**Re-checked at the page image at the cross-check and the ambiguity stands.** This read wrote the
equation out without noticing it; the first extract records it.)*

### §2.8 Training and inference

§3.6. Training maximises Equation (2), equivalently minimising the negative log likelihood.
Equation (13): `NLL(θ) = − log P_θ(Y|X) = log(Z_θ(X)) − S_θ(Y,X)`.

At inference only the frames are given; the paper states that because the normalisation factor stays
positive, **maximising `S(Y,X)` alone suffices** to decode segments and labels.

Both training and inference use *"the algorithms based on dynamic programming proposed in the
original semi-CRF paper"*.

---

## §3 — Coupling facts

The commission makes these mandatory, on the user's ruled widening, *"because choices are evaluated
as chains, and a method's admissibility at one layer depends on what its neighbours must then be."*
Everything below is read at the paper; where the paper does not say, this section says that instead
of filling it in.

### §3.1 What it ASSUMES about its upstream

**(a) A beat grid must already exist.** Frames are *"one eighth of a beat long"* (§3.1.1). **The
method does not find the beat; it is handed one.** Anything adopting this formalism inherits a
dependency on a metrical grid of that resolution.

**(b) Measure positions must be known, at training time at least.** §4.2: *"we force the sample
boundaries to be aligned with measure boundaries"*, and the 96-frame sample length is chosen
*"because it is divisible by all the common measure lengths existed in the dataset"*. **The paper
does not state whether measure alignment is required at inference time.**

**(c) Note onsets, offsets and durations.** The per-frame input is a **normalised distribution of the
duration of each pitch class within the frame**, so the upstream must supply sounding notes with
their durations inside each frame — not merely which notes are struck.

**(d) A lowest-sounding-note determination per frame.** The bass half of the input is a one-hot over
the pitch class of *"the lowest note"* in the frame. The paper does not state how the lowest note is
chosen when the lowest sounding note changes inside a frame.

**(e) PITCH CLASS ONLY — SPELLING IS DISCARDED AT THE INPUT.** Both input halves are 12-dimensional
over pitch classes, and the root is 12-dimensional over pitch classes. **Nothing in the eight pages
as read carries a spelled pitch anywhere in the representation.** A layer that must later produce
anything spelled inherits that absence from this formalism and has to supply the spelling itself.

**(f) Ground-truth harmony label segments at training**, with onsets and offsets, not just labels.

**(g) A ground-truth-derived transition matrix.** `T` in Equation (8) is *"pre-computed from the
ground-truth labels in the training data"* — so the model carries a component estimated from the
training annotations outside the gradient-descent fit, and it is a **frame-level** transition matrix
used inside a **segment-level** score.

**(h) Enough annotated data to fit a neural front end.** The paper states its own reason for dropping
the full Roman-numeral vocabulary as data scarcity (§3.1.2), so the label-space decision is itself a
function of the corpus available.

### §3.2 What it HANDS downstream

**(a) A complete partition of the input into contiguous non-overlapping harmonic regions**, each
with an onset frame index, an offset frame index and one label. Contiguity and non-overlap are
stated at §3.2 as properties of `Y`, so **there are no gaps and no abstention region**: every frame
belongs to exactly one labelled segment.

**(b) The label is a (root, quality) pair** — root one of 12 pitch classes, quality one of 10
unnamed classes.

**(c) What it does NOT hand downstream, stated because a chain-level reader needs the absence as
much as the presence.** In the eight pages as read the output carries **no tonality or tonic, no
scale degree, no Roman numeral, no inversion, no chord-member identity for the bass, no spelling,
and no alternative readings, margin or confidence of any kind.** The paper's model defines
`P(Y|X)` and therefore admits a posterior in principle, but **no candidate list, no probability and
no uncertainty is published for any decision anywhere in the eight pages as read.**

**(d) The temporal resolution of the output is NOT determinable from the paper.** §4.2 states that
*"pooling layers are added between blocks to reduce the temporal resolution of the harmony output"*
and gives the reason — *"harmony changes usually occur on average at a lower frequency than the
frame rate"* — **but states no pooling factor.** So although the input frame is one eighth of a
beat, **the granularity at which this method can place a boundary cannot be read off the paper.**
A downstream consumer that needs boundary precision would have to obtain that value elsewhere.

### §3.3 Its own STATED scope and limits

**(a) Symbolic input in the experiments; audio claimed adaptable, not shown.** §1: *"We focus on
MIDI-like symbolic music input in our experiments but the method could be easily adapted to audio."*
§6 repeats it as *"could be adapted to audio input by simple modifications on the neural front-end."*
**No audio experiment is reported.**

**(b) Quadratic time in sequence length, stated by the paper as its limitation.** §6: *"One
limitation of the semi-CRF architecture is that it has quadratic time complexity with respect to
sequence length so it is difficult to train the model on very long sequences."*

**(c) The label space is a deliberate reduction**, for the two reasons quoted at §2.3 above.

**(d) Two of the paper's own forward-looking statements are beliefs, and are labelled as such in
§4 below.** §5.1: *"we believe Harana has a greater potential to leverage larger datasets in the
future."* §5.3: *"More data and a larger neural front-end might be needed to fully leverage the
advantage of the absence score."*

**(e) Repertoire.** The four corpora named in Table 1 are the whole of the evidence. **The paper
states no claim about repertoire coverage and offers no per-corpus result** (§5.1 and §7.2 below).

---

## §4 — Claims, labeled

**The labels are the commission's: FACT** — stated or measured in the paper, with its location;
**THEORY** — established published theory; **CONJECTURE** — everything else. **A FACT label here
means the paper states it, never that this read endorses it**; where a FACT-labelled claim is
refuted by the paper's own values, the label stays FACT and the refutation is at §6 or §7.

**Claim 1 [FACT — §1, and §6 CONCLUSIONS].** The task of harmonic analysis has two components,
label recognition and boundary finding, and the two are related: *"Regions with strong confidence of
a candidate harmony label tend to possess the boundaries of a true segmentation … the oracle
segmentation could help the prediction of the true underlying harmony for the notes in each region."*
**The paper cites this to prior work rather than measuring it here.**

**Claim 2 [FACT — abstract, §1, §2].** Most previous attempts modelled the label component and
*"time boundaries were rarely modeled explicitly"*, and lack of boundary modelling in the objective
*"could lead to segmentation errors"*. **This is the paper's motivating claim and it is not measured
anywhere in the eight pages as read**; the closest thing to evidence for it is the semi-CRF ablation at §5.3,
which is a within-architecture comparison and not a survey of prior work.

**Claim 3 [FACT — §1, first contribution bullet].** *"Proposing the first neural semi-CRF model to
jointly estimate harmony labels and their time boundaries."* **A priority claim. The paper cites no
search, survey or enumeration in support of it anywhere in the eight pages as read**; it is recorded
here as the paper's assertion, and this read establishes nothing about whether it is right.

**Claim 4 [THEORY — §3.2, citing the original semi-CRF work].** Semi-CRF gives the conditional
probability of a sequence of contiguous non-overlapping labelled segments of variable length, and
both its training and its decoding admit dynamic-programming algorithms.

**Claim 5 [FACT — §1, §2].** Harmonic regions in music do not all have the same length, so a model
allowing variable label-span is more suitable for the task than a conventional fixed-span sequence
labeller. **Cited to prior work; not measured here.**

**Claim 6 [FACT — §3.1.2].** The full Roman-numeral encoding, with all components combined,
*"produces 47k different harmony labels"*. **No derivation of that value is given anywhere in the
eight pages as read**, and this read did not attempt to reproduce it, the component vocabularies not
being enumerated in the paper.

**Claim 7 [FACT — §3.1.2].** Classifying the harmony components independently *"is incompatible with
semi-CRF because the boundary of each component must be the same."* **This is an architectural claim
about the formalism and it is argued, not measured.** It is the load-bearing reason the paper gives
for reducing the label space, and anything adopting semi-CRF for a richer label inherits it.

**Claim 8 [FACT — §3.4].** A harmonic region *"is not likely to contain homogeneous harmonic
content"*, which is the stated reason for attention rather than averaging or taking the mode.
**Asserted, not measured.** The ablation at §5.3 measures the attention module's contribution, which
is a different proposition from this one.

**Claim 9 [FACT — §3.5].** Where non-chordal notes are many or chordal notes missing, the estimated
root and quality distributions *"would be relatively flat"* and the pitch-class activation vector
*"would not align well with a chord template"*. **Asserted, not measured**; no diagnostic of
flatness is reported.

**Claim 10 [FACT — §4.1, Table 1].** The experimental data is a collection organised by a cited
prior work, comprising four named corpora, with pieces, crotchet counts and chord-annotation counts
as transcribed at §5.1 below. Each piece is transposed to 12 different keys *"To increase the size
of the dataset and help alleviate possible data imbalance"*, and the data is *"split into disjoint
subsets for training and testing with a 2:1 split."*

**Claim 11 [FACT — §4.3].** Frame-level accuracy is computed for root and for quality, plus a
reduced quality dictionary of major and minor only; during inference *"the result is averaged across
all frames in a song."*

**Claim 12 [FACT — §4.3, Equations 14 and 15].** Segmentation quality uses the directional Hamming
distance from a named public evaluation package; a large `DHD(Î, I)` *"often indicates
under-segmentation"* and a large `DHD(I, Î)` *"often indicates over-segmentation"*; and the overall
segmentation quality is `SQ = 1 − max(DHD(I,Î), DHD(Î,I))`. **See §6.3 — the reported overall column
is not that quantity applied to the reported directional columns, in any of the eight rows.**

**Claim 13 [FACT — §5.1, Table 3].** *"Harana outperforms the baseline models on all the measures."*
**This one reproduces at every cell of Table 3** (§6.1).

**Claim 14 [FACT — §5.1, Table 3].** *"Without a neural front-end, the rule-based model even has
weaker performance than the plain CRNN."* **Reproduces at all four columns** (§6.1).

**Claim 15 [FACT — §5.1, Table 3].** *"We also notice that frog has lower accuracy than the plain
CRNN model."* **Reproduces at all four columns, but one of the four differences is 0.002, against a
table that reports no uncertainty at all** (§6.1 and §7.2).

**Claim 16 [CONJECTURE — §5.1, the paper's own hedge].** The reason offered for the second
baseline's weaker showing — that its autoregressive decoding *"may require the full spectrum of the
harmony components including key and degree"* — is stated as a possibility and **nothing in the
paper tests it.** The sentence that follows it, *"we believe Harana has a greater potential to
leverage larger datasets in the future"*, is labelled a belief by its own words.

**Claim 17 [FACT — §5.2, Table 4].** *"Harana provides improvement on segmentation quality compared
to other models"*, and *"the rule-based semi-CRF yields the most severe under-segmentation even
though it is optimized on the segmentation boundaries."* **Both reproduce at Table 4** (§6.2).

**Claim 18 [CONJECTURE — §5.2].** The reason offered for that last result — that rule-based features
*"are unable to clean noises such as the non-chordal notes and missing chordal notes in the input
music but directly compute features from them"*, and that *"The noise in the features of short
regions may be confused with the intrinsic noise of longer regions"* — is offered as *"might be"*
and is not tested.

**Claim 19 [FACT — §5.3, Table 2].** *"We can see that the full architecture achieves the best
result overall."* **★ THE PAPER'S OWN TABLE 2 CONTRADICTS THIS ON THREE OF ITS TWENTY-FOUR CELLS,
AND MARKS ALL THREE IN BOLD ITSELF. The paper acknowledges two of the three and not the third.**
The derivation is at §6.4 and the finding at §7.1.

**Claim 20 [FACT — §5.3, Table 2].** *"Among the missing components, semi-CRF leads to the largest
performance drop. That confirms semi-CRF is an indispensable component to capture boundary
information in harmony analysis."* **The comparative half reproduces at every one of Table 2's six
columns** (§6.4). **The word *indispensable* is the paper's, and what the table supports is a
largest-of-three ranking over drops whose own magnitudes are at §6.4** — the ranking and the strength
of the word are two different propositions, and only the first is checked here.

**Claim 21 [FACT — §5.3, Table 2].** Removing the absence score has *"less significant"* effect, and
*"Without it, the quality accuracy and overall segmentation quality even slightly improved."*
**Both directions reproduce** (§6.4). **The word *significant* is used here in its everyday sense:
no significance test is reported anywhere in the eight pages as read.**

**Claim 22 [CONJECTURE — §5.3].** The explanations offered for the absence score's weak showing —
*"could result from the more difficult training process"*, and that more data and a larger front end
*"might be needed"* — are stated as possibilities and are not tested.

**Claim 23 [FACT — §6].** The paper's own stated limitation: quadratic time complexity in sequence
length, *"so it is difficult to train the model on very long sequences."* **No timing, memory value
or sequence-length ceiling is reported anywhere in the eight pages as read.**

**Claim 24 [FACT — §4.2].** Implementation values, as stated: DenseNet in three blocks; 1-D
convolution along the time dimension; pooling between blocks; sample length 96 frames; PyTorch;
Adam; learning rate 10⁻⁴; weight decay 10⁻²; dropout rate 0.2 between GRU layers and after each
hidden fully connected layer; and *"The λ in Eq. (12) is chosen empirically to be 0.001."*
**No layer widths, no channel counts, no GRU hidden size, no parameter count and no training
schedule are stated** (§7.2).

---

## §5 — Measured results, with corpus, measure and value as the paper states them

**Every value below is transcribed from the page image. The paper prints four tables and no other
numbered result.** The tables carry **no standard deviation, no confidence interval, no spread of
any kind, and no significance test** — see §7.2, where that absence is stated with its bound.

### §5.1 Table 1, transcribed — the corpora

Caption as printed: *"Summary of statistics of the datasets."* The three column headings as printed
are **Pieces**, **Crotchet** and **Chord Annotations**.

| | Pieces | Crotchet | Chord Annotations |
|---|---|---|---|
| BPSFH | 32 | 23554 | 8615 |
| Roman Text | 82 | 18208 | 7935 |
| Tavern | 27 | 20673 | 10723 |
| Lopez | 180 | 31367 | 16666 |

**Twelve values.** The paper prints no row of totals; the sums this read computed are at §6.5, and
are this read's arithmetic and not the paper's.

**★ The column headed *Crotchet* is explained nowhere in the eight pages as read.** §4.1's whole
account of the table is *"Table 1 summarizes the statistics of the data included in our
experiments."* A crotchet is a quarter note, so the column plainly counts quarter-note units of
some kind, **but the paper never says so and never says of what** — sounded, notated, or of the
transposed corpus or the untransposed one.

**★ And the paper does not say whether these counts are before or after transposition.** §4.1 states
that each piece is transposed to 12 different keys; the table is introduced in the sentence before
that one. Under one reading the training corpus is twelve times what this table shows.

### §5.2 Table 2, transcribed — the ablation study

Caption as printed: *"The result of the ablation studies summarizing the effect of removing each
proposed component of the model on both frame-level accuracy and segmentation quality."*

Bold in the transcription is the paper's own bold, read at the page image.

| Model | Root Acc | Quality Acc | Overall Acc | Under Seg | Over Seg | Overall Seg |
|---|---|---|---|---|---|---|
| Harana | **0.744** | 0.743 | **0.651** | **0.722** | 0.747 | 0.649 |
| Harana - no semi-CRF | 0.732 | 0.715 | 0.634 | 0.678 | 0.740 | 0.639 |
| Harana - no Attention Fusing | 0.741 | 0.738 | 0.650 | 0.716 | **0.749** | 0.645 |
| Harana - no Absence Score | 0.743 | **0.746** | 0.643 | 0.719 | 0.748 | **0.650** |

**Twenty-four values. Six bold marks, of which THREE sit in an ablated row and not in the full
model's row** — Quality Acc and Overall Seg in the *no Absence Score* row, and Over Seg in the *no
Attention Fusing* row. **The paper's own typesetting therefore marks three cells where an ablated
model beats the full one.** What that does to Claim 19 is at §6.4 and §7.1.

### §5.3 Table 3, transcribed — frame-level accuracy against the baselines

Caption as printed: *"The frame-level accuracy for different models."*

| Model | Root | Quality | Majmin | Overall |
|---|---|---|---|---|
| CRNN | 0.735 | 0.714 | 0.865 | 0.634 |
| frog | 0.733 | 0.542 | 0.815 | 0.459 |
| RuleSCRF | 0.684 | 0.645 | 0.847 | 0.600 |
| Harana | **0.744** | **0.743** | **0.886** | **0.651** |

**Sixteen values**, with the whole Harana row bold.

### §5.4 Table 4, transcribed — segmentation quality against the baselines

Caption as printed: *"The segmentation quality for different models."*

| Model | Under Seg | Over Seg | Overall |
|---|---|---|---|
| CRNN | 0.681 | 0.738 | 0.639 |
| frog | 0.681 | 0.724 | 0.624 |
| RuleSCRF | 0.666 | 0.741 | 0.625 |
| Harana | **0.722** | **0.747** | **0.649** |

**Twelve values**, with the whole Harana row bold.

### §5.5 The three baselines, as the paper describes them

§4.4 names them and says why each was chosen — *"The chosen baselines are all relevant to our model
by sharing parts of the architecture."*

- **CRNN** — *"Since the neural front-end of Harana is CRNN, we first test if a plain CRNN model
  could achieve comparable results."*
- **frog** — *"also relies on CRNN to extract music features. In contrast to our model, it uses a
  neural autoregressive distribution estimation (NADE) to decode the harmony label."* The paper
  states that *"The same output harmony categories of root and quality output are considered in the
  NADE decoder."*
- **RuleSCRF** — the rule-based semi-CRF of the prior work the paper builds on. **★ And the paper
  states plainly that it did not implement the whole of it:** *"For simplicity, we implemented the
  two most important features, chord coverage and segment purity, in our experiment."* Chord
  coverage is described as *"what percentage of chordal notes are covered by the music segment"* and
  segment purity as *"what proportion of notes in the music segment are indeed chordal notes"*.
  **This bears directly on Claim 13 and on §5.1's reading of the gap between Harana and RuleSCRF**,
  and is taken up at §7.2.

### §5.6 The evaluation metrics, as stated

- **Frame-level accuracy** for root and for quality; plus **Majmin**, *"The accuracy on a reduced
  dictionary of quality including only major and minor … due to its prevalence in the literature and
  adequacy in many practical uses."* Averaged across all frames in a song at inference.
- **The three-column segmentation measurement**, from the directional Hamming distance of Equation
  (14), with the overall quantity defined at Equation (15) as `SQ = 1 − max(DHD(I,Î), DHD(Î,I))`.
- **★ The paper never defines its *Overall* accuracy column.** Root and quality accuracy are
  defined; *Overall* appears in Tables 2 and 3 with no definition anywhere in the eight pages as
  read. What this read could and could not establish about it is at §6.6.

---

## §6 — Arithmetic this read performed on the paper's own printed values

**Every computation below runs over the values transcribed at §5 and nothing else.** Where a
computation refutes a sentence of the paper, both the sentence and the derivation are printed.
**This section is this read's arithmetic, not the paper's**, and the paper reports none of it.

### §6.1 Claims 13, 14 and 15 reproduce at every cell of Table 3

**Claim 13, *"Harana outperforms the baseline models on all the measures"*: twelve comparisons,
all twelve in Harana's favour.** Margins, Harana minus the named baseline:

| | vs CRNN | vs frog | vs RuleSCRF |
|---|---|---|---|
| Root | +0.009 | +0.011 | +0.060 |
| Quality | +0.029 | +0.201 | +0.098 |
| Majmin | +0.021 | +0.071 | +0.039 |
| Overall | +0.017 | +0.192 | +0.051 |

**Claim 14, the rule-based model below the plain CRNN: four comparisons, all four negative** —
Root −0.051, Quality −0.069, Majmin −0.018, Overall −0.034.

**Claim 15, frog below the plain CRNN: four comparisons, all four negative** — Root −0.002,
Quality −0.172, Majmin −0.050, Overall −0.175. **★ The root margin is 0.002**, which is what the
last significant digit the table prints can express, and the paper reports no spread against which
to read it. That is a statement about what the table supports, not a claim that the difference is
noise — **nothing in the paper lets either verdict be reached** (§7.2).

### §6.2 Claim 17 reproduces at Table 4

Harana's Overall exceeds every baseline's: +0.010 over CRNN, +0.025 over frog, +0.024 over
RuleSCRF. It also leads both directional columns outright. And RuleSCRF's Under Seg, **0.666, is the
smallest of the four** — which, given the paper's own statement that a higher under-segmentation
value means fewer missing boundaries, is *"the most severe under-segmentation"* as the paper says.

### §6.3 ★ EQUATION (15) CANNOT BE REPRODUCED FROM THE PRINTED TABLES, IN ANY OF THE EIGHT ROWS

Equation (15) defines the overall segmentation quality as `SQ = 1 − max(DHD(I,Î), DHD(Î,I))`.
**If the two directional columns are each one minus their own directional distance — which is the
only reading on which the printed table and Equation (15) are about the same quantities — then
`SQ` is simply the SMALLER of the two directional columns.** Against that:

| Row | Under Seg | Over Seg | smaller of the two | *Overall* as printed | shortfall |
|---|---|---|---|---|---|
| CRNN (T4) | 0.681 | 0.738 | 0.681 | 0.639 | 0.042 |
| frog (T4) | 0.681 | 0.724 | 0.681 | 0.624 | 0.057 |
| RuleSCRF (T4) | 0.666 | 0.741 | 0.666 | 0.625 | 0.041 |
| Harana (T4 and T2) | 0.722 | 0.747 | 0.722 | 0.649 | 0.073 |
| no semi-CRF (T2) | 0.678 | 0.740 | 0.678 | 0.639 | 0.039 |
| no Attention Fusing (T2) | 0.716 | 0.749 | 0.716 | 0.645 | 0.071 |
| no Absence Score (T2) | 0.719 | 0.748 | 0.719 | 0.650 | 0.069 |

**Every row falls short, and every shortfall is in the same direction** — the printed *Overall* is
below what Equation (15) gives, by between 0.039 and 0.073.

**What this establishes and what it does not.** It establishes that **a reader cannot get the
printed overall column out of the printed directional columns by the paper's own Equation (15)**,
and that the failure holds in all eight rows and in one direction rather than at a stray cell. **It
does not establish that any value is wrong.** Two readings survive, and the paper settles neither:

- **[CONJECTURE]** the quantities are computed **per song and then averaged**, in which case the
  average of the per-song smaller value is necessarily at or below the smaller of the two averages,
  which is exactly the direction every row shows. **The paper states the aggregation level for
  frame-level accuracy — *"the result is averaged across all frames in a song"* — and states nothing
  at all about how the segmentation quantities are aggregated across songs.**
- **[CONJECTURE]** the two directional columns are not one minus their directional distances, in
  which case Equation (15) cannot be evaluated from the table at all.

**Either way the same practical consequence holds for anyone lifting these values: the three
segmentation columns are not related to one another by any rule the paper states.**

### §6.4 ★ Table 2 against Claims 19, 20 and 21 — the ablation, computed

Drops from the full model, positive meaning the full model is better:

| Removed component | Root Acc | Quality Acc | Overall Acc | Under Seg | Over Seg | Overall Seg |
|---|---|---|---|---|---|---|
| no semi-CRF | +0.012 | +0.028 | +0.017 | +0.044 | +0.007 | +0.010 |
| no Attention Fusing | +0.003 | +0.005 | +0.001 | +0.006 | **−0.002** | +0.004 |
| no Absence Score | +0.001 | **−0.003** | +0.008 | +0.003 | **−0.001** | **−0.001** |

**Claim 20 reproduces at every one of the six columns.** Removing semi-CRF costs more than removing
either other component in all six, so *"semi-CRF leads to the largest performance drop"* holds as a
ranking over the three ablations wherever it is read.

**★ But the magnitudes are worth reading beside the ranking, because they are what a design decision
would rest on.** The largest single drop in the whole table is **0.044** (Under Seg, no semi-CRF)
and the next largest **0.028** (Quality Acc, no semi-CRF). **Every drop attributable to the
attention module is at or below 0.006, and every one attributable to the absence score is at or
below 0.008** — and three of those twelve cells are gains rather than drops. **Against a table that
reports no spread of any kind, this read can state the magnitudes and cannot state what they
survive** (§7.2).

**★ Claim 19 is refuted by the paper's own Table 2 on three cells.** *"We can see that the full
architecture achieves the best result overall"*, against:

- **Quality Acc** — *no Absence Score* 0.746 against Harana's 0.743;
- **Overall Seg** — *no Absence Score* 0.650 against Harana's 0.649;
- **Over Seg** — *no Attention Fusing* 0.749 against Harana's 0.747.

**All three are marked bold by the paper's own typesetting**, read at the page image, so the table
marks them as the best in their columns while the sentence above it says the full model is.

**★ The paper acknowledges two of the three and not the third.** §5.3 says of the absence score:
*"Without it, the quality accuracy and overall segmentation quality even slightly improved"* — which
is exactly the first two, and **Claim 21 therefore reproduces**. **Of the attention module it says
only that it, *"although also helpful, produces relatively smaller performance gain"*, which does
not reach the over-segmentation cell where removing it helps.** So one of the three cells the
paper's own table bolds outside the full model's row goes unmentioned, under a component the text
calls helpful. This is taken up at §7.1.

### §6.5 ★ Table 1's own values, summed, and what the paper's stated sampling rule does with them

**Sums, this read's arithmetic; the paper prints no totals:** **321 pieces**, **93,802 crotchets**,
**43,939 chord annotations** across the four corpora.

**Shares of each total, by corpus:**

| | share of pieces | share of crotchets | share of annotations | crotchets per annotation |
|---|---|---|---|---|
| BPSFH | 10.0 % | 25.1 % | 19.6 % | 2.73 |
| Roman Text | 25.5 % | 19.4 % | 18.1 % | 2.29 |
| Tavern | 8.4 % | 22.0 % | 24.4 % | 1.93 |
| Lopez | 56.1 % | 33.4 % | 37.9 % | 1.88 |

**Two things follow from the paper's own values and its own stated rule, and neither is stated in
the paper.**

**(a) The corpora are annotated at materially different densities** — from 2.73 crotchets per
annotation in BPSFH to 1.88 in Lopez, a spread of about 1.45 times. A pooled aggregate over four
corpora of unequal annotation density is not the same quantity as any per-corpus value, **and the
paper reports no per-corpus result at all** (§7.2).

**(b) The stated sampling rule weights the corpora by PIECE COUNT, not by musical quantity.** §4.2:
*"to avoid over-sampling from music pieces with longer length, the piece index is sampled uniformly
first before a music sample is selected from the piece."* **Under uniform sampling over pieces,
Lopez supplies about 56 per cent of training samples while contributing about 33 per cent of the
crotchets.** The rule is stated as a guard against long pieces dominating; **its arithmetic
consequence is that the corpus with the most pieces dominates instead**, and the paper does not say
so. *(Bound: this is about the pooled corpus of Table 1. The composition of the train and test
subsets is not stated, so nothing here is a claim about the test set in particular — see §7.2(c).)*

### §6.6 ★ What the undefined *Overall* accuracy column can and cannot be

**It is NOT the product of root and quality accuracy, in any of the eight rows.** For the full
model, 0.744 × 0.743 = 0.553 against 0.651 printed; for CRNN 0.525 against 0.634; for frog 0.397
against 0.459; for RuleSCRF 0.441 against 0.600. **All four products are below the printed value**,
so root and quality correctness are not being multiplied as independent events.

**It IS consistent, in all eight rows of Tables 2 and 3, with the accuracy of getting root and
quality BOTH right on the same frame.** Such a quantity must lie between `max(0, R + Q − 1)` and
`min(R, Q)`:

| Row | lower bound | *Overall* printed | upper bound |
|---|---|---|---|
| Harana | 0.487 | 0.651 | 0.743 |
| CRNN | 0.449 | 0.634 | 0.714 |
| frog | 0.275 | 0.459 | 0.542 |
| RuleSCRF | 0.329 | 0.600 | 0.645 |
| no semi-CRF | 0.447 | 0.634 | 0.715 |
| no Attention Fusing | 0.479 | 0.650 | 0.738 |
| no Absence Score | 0.489 | 0.643 | 0.743 |

**All eight lie strictly inside their bounds.** **[CONJECTURE]** *Overall* is joint root-and-quality
accuracy. **The paper states no definition, so this is a reading consistent with every printed
value and not something the paper says**, and any use of the column downstream carries that.

### §6.7 Table 2's full-model row reproduces Tables 3 and 4 exactly

The six values Table 2 gives for Harana — 0.744, 0.743, 0.651, 0.722, 0.747, 0.649 — are the same
six Tables 3 and 4 give for Harana, digit for digit. **A consistency check that passes**, and worth
recording because the two failures at §6.3 and §6.4 are both about relations the paper asserts
rather than about disagreement between its tables.

### §6.8 Three internal checks of the paper's equations that pass

- **Equation (8)'s frame count is right.** A segment from frame `uᵢ` to frame `vᵢ` inclusive spans
  `vᵢ − uᵢ + 1` frames and therefore `vᵢ − uᵢ` transitions internal to it. Equation (8) multiplies
  the self-transition entry by exactly `vᵢ − uᵢ` and adds one boundary entry, so the segment is
  charged one frame-level transition per frame with no double count and no gap.
- **Equation (13)'s sign is right.** From Equation (2), `−log P(Y|X) = log Z(X) − S(Y,X)`, which is
  what the paper prints.
- **Equations (14) and (15) are bounded correctly.** Equation (14) divides by the total estimated
  span length, so each directional distance lies in `[0,1]` and Equation (15) lies in `[0,1]`.

### §6.9 The 96-frame sample length, checked as far as the paper permits

At one eighth of a beat per frame, **96 frames is 12 beats**. A measure of `b` beats is `8b` frames,
and `96 / 8b = 12 / b`, **an integer exactly when `b` is 1, 2, 3, 4, 6 or 12.** So the paper's
reason — *"because it is divisible by all the common measure lengths existed in the dataset"* —
**holds for measures of those lengths and fails for 5, 7, 8, 9, 10 and 11 beats**, an eight-beat
measure among them. **The measure lengths present in the data are enumerated nowhere in the eight
pages as read**, so the claim cannot be checked further than this.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

**F-1 ★ THE PAPER'S ABLATION CONCLUSION IS REFUTED BY ITS OWN TABLE ON THREE CELLS, AND ONE OF THE
THREE GOES UNMENTIONED.** §5.3 opens *"We can see that the full architecture achieves the best
result overall."* **The full model leads outright on exactly THREE of Table 2's six columns** — Root
Acc, Overall Acc and Under Seg — **and the table's own bolding marks exactly those three and no
others.** On the remaining three an ablated model is ahead: Quality Acc 0.746 and Overall Seg 0.650
under *no Absence Score*, and Over Seg 0.749 under *no Attention Fusing*, **each of them bolded by
the paper itself**. **The text acknowledges the first two by name and says nothing about the
third**, describing the attention module only as *"although also helpful"*. Derivation at §6.4.

**★ Stated exactly, because the two halves point different ways: Table 2's typesetting is
internally honest — it bolds the winner of every column, wherever the winner sits — and it is the
SENTENCE above it that reaches further than the table does.** **Why it is reported rather than waved
through: the opening sentence of §5.3 is where a reader takes the ablation's verdict from, and it is
the sentence a citing author would quote** — so a reader who quotes it without recomputing the
table carries a claim the table does not support. *(No ranking of this finding against the others in
this section is made; none was derived.)*

**F-2 ★ EQUATION (15) IS NOT REPRODUCIBLE FROM THE PRINTED TABLES IN ANY OF THE EIGHT ROWS.** The
printed *Overall* segmentation column is below the smaller of the two printed directional columns
everywhere, by 0.039 to 0.073. Derivation and the two surviving readings at §6.3. **No value is
shown to be wrong; what is shown is that the three segmentation columns are not related to each
other by any rule the paper states.**

**F-3 ★ EQUATION (5), AS PRINTED, CONTAINS NO SOFTMAX, AND THE PAPER CALLS IT *"the scaled
dot-product attention"* AND ATTRIBUTES IT BY CITATION.** What is printed is
`A(Q,K,V) = Σᵢ Qᵀ Kᵢ Vᵢ / √d` — a sum of value vectors weighted by raw scaled dot products, with no
normalisation over the keys. **The citation is reference 24, printed on page 7 as A. Vaswani and
seven co-authors, "Attention is all you need", NeurIPS 2017** — read at the reference list at the
read-back. **[THEORY]** The scaled dot-product attention of that work applies a softmax over the
keys before weighting the values; that is the standard published form. **Bound, stated because it
decides how far this finding reaches: this read did not open the cited work in this sitting**, so
what is established is what the paper prints and that it differs from the standard form in the
softmax, not anything about the cited paper's own text. **Whether the
implementation follows the printed equation or the standard form cannot be told from the paper**;
the source repository was not visited.

**F-4 ★ A MISSPELLING THE PAPER CONTRADICTS ELSEWHERE IN ITSELF — THE SAME SHAPE THIS LINE MET AT
ROW 11.** On page 4, immediately above Equation (12), the paper prints *"When the absense score is
used"*. **The word is spelled *absence* at the §3.5 heading *Absence Score*, in that section's own
text, and in Table 2's row label.** So the paper is internally inconsistent at a term it coined for
this work. **It is recorded because a quoting reader repairs such a spelling silently, and the
repair hides the inconsistency** — which is exactly what the hundred-and-seventy-sixth records of
row 11's first extract and the hundred-and-seventy-third of its own member.

**F-5 Four further typographical or grammatical defects, named rather than counted.**

- Page 2: *"Boulanger-Lewandowsk et al."* — the reference list on page 7 spells the same name
  **Boulanger-Lewandowski**, with a final letter the body text drops.
- Page 3, the opening of §3.3: *"Followng Micci et al."* — two in one clause: *Following* is
  printed without its `i`, and the name is printed **Micci** where the reference list and §4.1 both
  print **Micchi**.
- Page 2: *"regresses some sporadically outliers back to the harmonic streams"* — an adverb where
  the sentence needs an adjective.
- Page 5: *"divisible by all the common measure lengths existed in the dataset"*.

**F-6 A CITATION QUESTION THIS READ RECORDS AND DOES NOT ANSWER.** The paper attributes three
separate things to one reference numbered 28 — the organisation of the dataset collection, the
parser adapted for its data representations, and the second baseline system, which it names **frog**
— while attributing the DenseNet–GRU front end to a different reference, numbered 23. **On the
reference list as printed, 28 is a 2017 conference paper whose title is about enforcing coherence in
automatic chord recognition, and 23 is a 2020 journal article about pitch representation and model
architecture for automatic harmonic analysis.** **Whether each attribution lands on the right work
is NOT checked here** — neither cited work was opened, and no web access was made. It is recorded
because a later reader tracing the data provenance of these values will have to settle it.

**F-7 THE PAPER'S PRIORITY CLAIM CARRIES NO SUPPORT IN THE PAPER.** *"Proposing the first neural
semi-CRF model to jointly estimate harmony labels and their time boundaries"* is asserted in the
contribution list with no survey, search or enumeration behind it anywhere in the eight pages as
read. **This read establishes nothing about whether the claim is true.**

**F-8 ★ THE THIRD BASELINE IS A TWO-FEATURE REIMPLEMENTATION, AND A CONCLUSION IS DRAWN FROM IT AS
IF IT WERE THE PUBLISHED METHOD.** §4.4 states plainly: *"For simplicity, we implemented the two
most important features, chord coverage and segment purity, in our experiment."* **§5.1 then reads
the RuleSCRF row as a verdict on rule-based scoring in general:** *"The large gap between Harana and
the rule-based semi-CRF model demonstrates the value of a neural score function."* **The caveat is
not repeated where the conclusion is drawn**, and the RuleSCRF row is the widest of Harana's three
margins on root accuracy (§6.1). **Both statements are the paper's own and they sit one page apart.**

*(★ A CHAIN NOTE, CORRECTED AT THE READ-BACK, AND THE CORRECTION IS THE POINT. The work this
two-feature baseline reimplements is reference **21** as printed on page 7: **K. Masada and R. C.
Bunescu, "Chord recognition in symbolic music using semi-Markov conditional random fields", ISMIR
2017, pp. 272–278.** **That is NOT the Masada & Bunescu document at row 10 of this same slice** —
the hundred-and-seventy-fifth entry names row 10's paper as *"Chord Recognition in Symbolic Music: A
Segmental CRF Model, Segment-Level Features, and Comparative Evaluations on Classical and Popular
Music"* and records its held copy as the 2018 preprint of the 2019 journal article. **Same two
authors, different paper, six years apart in the record's own naming.** Bound: neither Masada &
Bunescu document was opened in this sitting, and this note rests on the reference line as printed
and on the hundred-and-seventy-fifth entry's own text.*

*FORMER WORDING, PRESERVED (#12): "the method this two-feature baseline reimplements is the paper at
**row 10 of this same slice** — the hundred-and-seventy-fifth entry names row 10 as Masada &
Bunescu's segmental CRF model … **So a reader comparing the two members should know that this
paper's RuleSCRF column is not row 10's own reported system.**" **It asserted an identity between
two documents on the strength of two shared author names, and the reference line refutes it.** The
practical warning it carried survives in a stronger form: **the RuleSCRF column is not the reported
system of EITHER Masada & Bunescu paper — it is this paper's own two-feature reimplementation of the
2017 one.**)*

**F-8a ★ THREE MEMBERS OF THIS SAME SLICE ARE IN THIS PAPER'S REFERENCE LIST, AND ONE OF THEM IS THE
FORMALISM'S ORIGIN.** Found at the read-back, by reading the reference list on pages 7 and 8 against
the candidacy lines this sitting had already opened at the object:

- **Reference 6 — S. Sarawagi and W. W. Cohen, "Semi-Markov conditional random fields for
  information extraction", NeurIPS 2004 — is ROW 11**, whose second extraction the previous sitting
  completed. **This paper cites it four times** — at the abstract's *"traditional semi-CRF"*, at §1
  twice for the variable-length argument and the rule-based scoring it departs from, and at §3.6 as
  *"the original semi-CRF paper"* whose dynamic-programming algorithms it uses. **So row 19's method
  is built directly on row 11's formalism**, and the two members' extracts are about the same
  machinery one layer apart.
- **Reference 11 — Burgoyne, Pugin, Kereliuk and Fujinaga, ISMIR 2007 — is ROW 17**, by the
  candidacy line at `reading_pass/candidacy_upgrades.md` line 79, read at the object in this
  sitting. Cited once, at §2, among the audio-side probabilistic decoders.
- **Reference 9 — Sheh and Ellis, ISMIR 2003 — is ROW 18**, by the candidacy line at line 80, read
  at the object. Cited twice at §2, in the HMM group and in the two-stage group.

**What this establishes, and its bound.** It establishes that this paper cites those three works and
that the candidacy file's rows 17, 18 and 11 name works with those authors, titles and venues.
**None of the three cited papers was opened in this sitting**, and nothing here is a claim about
what any of them says.

**F-9 *"significant"* AND *"less significant"* ARE USED IN THEIR EVERYDAY SENSE, AND NO SIGNIFICANCE
TEST IS REPORTED ANYWHERE IN THE EIGHT PAGES AS READ.** §5.3 says the effect of removing the absence score *"is
less significant"*. **No test, no p-value and no spread appears in any of the four tables or in the
text as read.** Recorded because the word invites exactly the reading the paper does not support.

**F-10 TWO COLUMNS OF PRINTED VALUES ARE UNDEFINED IN THE EIGHT PAGES AS READ.** The *Overall*
accuracy column of Tables 2 and 3 is defined nowhere in them (§6.6), and Table 1's column headed
*Crotchet* is explained nowhere in them (§5.1).

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

**(a) ★ NO UNCERTAINTY OF ANY KIND.** No standard deviation, no confidence interval, no repeated
runs, no seed, no significance test, anywhere in the four tables or in the text as read. **Every
comparison drawn in §5.1, §5.2 and §5.3 — the three sections where the paper reads its own tables —
is made between single values with no spread attached**, and that includes the 0.002 root margin of
§6.1 and the attention and absence-score drops of §6.4, none of which exceeds 0.008. *(Bound: met
nowhere in the eight pages as read.)*

**(b) ★ NO PER-CORPUS RESULT.** All reported accuracy and segmentation values are pooled across the
four corpora of Table 1, which §6.5 shows differ in annotation density by about 1.45 times. **No
table, sentence or appendix in the eight pages as read breaks any result down by corpus**, so it
cannot be told which corpus moved.

**(c) ★ THE TRAIN/TEST SPLIT'S UNIT IS NOT STATED, AND NEITHER IS ITS ORDER AGAINST THE
TRANSPOSITION.** §4.1 says only: each piece is transposed to 12 different keys, and *"The dataset is
split into disjoint subsets for training and testing with a 2:1 split."* **It does not say whether
the subsets are disjoint in PIECES or in SAMPLES, and it does not say whether the split is taken
before or after transposition.** Under one reading — transposing first, then splitting samples —
twelve transpositions of the same piece would be distributed across both sides, and the reported
accuracies would be measured partly on transposed copies of training material. **Nothing in the
paper says this happened and nothing in the paper rules it out.** **A project that requires fitting
and evaluation to be separated cannot settle that requirement from this paper's own text**, which is
what makes the gap worth naming. **It is recorded as a question, not as an accusation**, and no
ranking of it against the other gaps in this subsection is made — none was derived.

**(d) NO VALIDATION SET IS NAMED, AND THE ONE HYPERPARAMETER THE PAPER GIVES IS *"chosen
empirically"*.** §4.2 states λ = 0.001 for Equation (12) and calls the choice empirical. **The data
on which it was chosen is not stated**, and with only training and testing subsets named, the paper
does not establish that hyperparameter selection was separated from the test data.

**(e) ★ THE POOLING FACTOR IS NOT STATED, SO THE OUTPUT'S TEMPORAL RESOLUTION IS UNKNOWN.** §4.2
says pooling layers *"are added between blocks to reduce the temporal resolution of the harmony
output"* and gives no factor. **The input frame is one eighth of a beat; the granularity at which
the model can actually place a boundary cannot be read off the paper**, and a segmentation-quality
value is not interpretable without it.

**(f) The ten quality classes are never enumerated.** §3.1.2 says *"10 commonly used classes"* and
names none of them. So the quality accuracy column is over an unnamed vocabulary, and only the
reduced major/minor dictionary is identifiable.

**(g) No model size of any kind.** No layer widths, no channel counts, no GRU hidden size, no number
of parameters, no training time, no inference time and no hardware. **This is worth naming
specifically because the paper's own stated limitation is a complexity one** — quadratic time in
sequence length — **and it reports no timing against which that limitation could be sized.**

**(g1) ★ NO MAXIMUM SEGMENT LENGTH IS STATED — a precision ADOPTED FROM THE FIRST EXTRACT at the
cross-check and marked here (§9.4).** Semi-CRF decoding is ordinarily bounded by a maximum segment
length, and the eight pages as read state none. **That bears directly on (g) above**: the paper's
quadratic-complexity statement is what one expects when no such bound is imposed, so the missing
value and the stated limitation are the same gap seen twice. **This read did not have it; the first
extract did.**

**(h) The 47k label count is stated and not derived** (Claim 6), the component vocabularies it would
be computed from not being given.

**(i) Table 1's counts are not stated as pre- or post-transposition** (§5.1).

**(j) Two input questions the paper leaves open.** Whether measure alignment is required at
inference as well as in training-sample construction (§4.2 states it only for samples); and how the
bass pitch class is determined when the lowest sounding note changes within a frame.

**(k) No error analysis of any kind.** No confusion between quality classes, no breakdown by chord
type or by key, no worked example, and no qualitative output anywhere in the eight pages as read.

### §7.3 What is both measured and structural here, for a design that would adopt this formalism

**Nothing in this subsection is a recommendation, and none of it is checked against this project's
own record** — `FRAMEWORK.md` and every other governing surface were not opened. It states what
this paper would commit a design to, at the paper.

**(1) The joint component is the one the paper's own evidence supports best, and the support is a
ranking rather than a magnitude.** Removing semi-CRF costs more than removing either other proposed
component on all six of Table 2's columns (§6.4), so the ranking is robust across every metric the
paper reports. **The magnitudes are 0.044 at most and 0.007 at least**, against a table with no
spread, so what the paper establishes is *which* component matters most among the three and not
*how much* any of them is worth.

**(2) The label-space constraint is structural and is the paper's own argument, not a measurement.**
Claim 7: component-wise independent classification is incompatible with semi-CRF **because every
component would have to share one boundary set**. A design adopting this formalism for a richer
label than (root, quality) therefore faces the same fork the paper faced — one joint vocabulary,
whose size the paper puts at 47k for the full Roman-numeral encoding, or a deliberate reduction.
**A layer asked to produce tonality, degree, quality and inversion together meets this fork as soon
as it adopts the formalism**, which is why it is named here; no ranking against the other coupling
facts in this subsection is made.

**(3) Spelling is absent from end to end.** Input, label and output are pitch-class objects
throughout (§3.1 and §3.2(c)). **A layer that must hand spelled output downstream cannot take this
representation unchanged**, and the paper offers nothing on how a spelling would be recovered.

**(4) The formalism defines a posterior and the paper publishes none of it.** `P(Y|X)` is defined at
Equation (2) and the normalisation over all segmentations at Equation (1). **No candidate list, no
margin and no confidence is reported for any decision in the eight pages as read.** So the machinery
for ranked alternatives is present in the formalism and not delivered anywhere in those pages — a
design needing them would be adding reporting, not adding a mechanism.

**(5) The transition component is fitted outside the gradient fit and is weighted by a single
stated value.** `T` is precomputed from ground-truth training labels (§2.6), it is a FRAME-level
matrix used inside a SEGMENT-level score, and Equation (12) weights it by λ = 0.001. **The numeric
scales of the similarity term and the transition term are not stated anywhere in the eight pages as read**, so
this read cannot say what relative influence 0.001 represents. It is recorded because λ is the only
balance value the paper gives and a reader may otherwise take it for a small influence without the
scales that would settle it.

**(6) The absence score is cheap and transferable, and the paper's own ablation does not support
it on two of six columns.** The mechanism is one line — send the complement of the input pitch-class
vector through the same front end and negate the resulting similarity (Equations 10 and 11) — so it
costs a second forward pass and no new component. **Removing it improves quality accuracy and
overall segmentation quality in the paper's own Table 2** (§6.4), which the paper states.

**(7) Everything measured here is pooled over four corpora sampled uniformly by PIECE** (§6.5), so
the corpus contributing 56 per cent of pieces and 33 per cent of the crotchets dominates both the
training sampling and, so far as the paper says anything, the reported aggregate. **A design reading
these values as evidence about a repertoire inherits that weighting unexamined.**

**(8) The cost is quadratic in sequence length by the paper's own statement, and unmeasured.** A
bounded-context design would have to size that itself; the paper gives no timing at any length.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**Every one of the eight pages was re-opened after §0 to §7 were written**, in requests named rather
than counted: pages 5–6, then 2–4, then 7–8, then 1. **So every page of this paper has had two
passes, and no claim in this file rests on a page read once.** **This is what eight pages cost;
a next side with a longer paper should not read that as an instruction it can afford.**

**Every image was checked for presence and legibility at the image**, not at the call's success
line, at the read-back as at the whole read. **One further request, the deliberately out-of-range
one that established the page count, returned the refusal it was made for and no image. None of
this is evidence the page-image fault is gone.**

**What the read-back was for.** Each transcribed value, each quotation and each statement about
where something is printed was taken back to the page. **All sixty-four values of Tables 1 to 4
were re-read at the page images and every one of them stands as transcribed** — twelve in Table 1,
twenty-four in Table 2, sixteen in Table 3, twelve in Table 4 — **and the six bold marks of Table 2
were re-checked at the image, three in the full model's row and three outside it.**

### §8.2 What the read-back and the sweep struck in this side's own writing

**Named rather than totalled.**

**The read-back struck one thing and added two.**

- **★ A FALSE IDENTITY BETWEEN TWO DOCUMENTS, ASSERTED FROM TWO SHARED AUTHOR NAMES.** The first
  writing of F-8 said the work this paper's third baseline reimplements is the paper at row 10 of
  this same slice. **The reference line on page 7 refutes it**: reference 21 is Masada & Bunescu's
  ISMIR 2017 paper, and the hundred-and-seventy-fifth entry names row 10's document as their later
  segmental-CRF paper. **Corrected at the site with the former wording preserved (#12).**
- **A finding the first writing did not have: three members of this same slice are in this paper's
  reference list**, row 11 among them as the formalism's own origin, cited four times. **It was
  found only because the read-back read the reference list against the candidacy lines this sitting
  had already opened.** It is now F-8a.
- **F-1 was sharpened rather than corrected.** The first writing said three cells are bolded outside
  the full model's row, which is true and leaves the table looking careless. The read-back
  established the fuller statement: **the full model leads outright on exactly three of the six
  columns and the table bolds exactly those three, so the table is internally consistent and it is
  §5.3's opening sentence that overreaches.**

**The sweep struck the following, each hit read at its own line.**

- **★ Four superlatives over this read's OWN findings, none of them derived** — *"a coupling fact of
  the first importance"*, *"the finding of this read most likely to be lifted wrongly by a later
  reader"*, *"the gap of this paper most likely to matter to a project that separates fitting from
  evaluation"*, and *"the coupling fact most likely to bind a layer"*. **Each ranked this read's
  findings against one another on nothing.** All four are replaced by the reason without the
  ranking, and each site now says in terms that no ranking was made. **These are a degradation tell
  and are reported as one at §8.3.**
- **Five negatives stated as *"anywhere in the paper"*** where the act reaches the eight pages as
  read. All five now say so. **The distinction is not pedantry: a page image is checked for presence
  and legibility, not resolved character by character in every figure.**
- **A count of this side's own reading made stale by its own later acts** — §0 said the paper was
  read *"in two requests (1–4 and 5–8)"*, true of the whole read and false of the sitting once the
  read-back made four more. It now points at §8.1 instead of counting.
- **An interpretive word standing where a derivation belonged** — the Equation (15) failure was
  called *"systematic rather than a stray cell"*; it now states what was derived, that the shortfall
  holds in all eight rows and in one direction.
- **An unbounded universal over the paper's own reasoning** — *"Every comparison the paper draws"*,
  which this read never enumerated. It is now bounded to §5.1, §5.2 and §5.3, the three sections
  where the paper reads its own tables.
- **Three further claims stated wider than the act**: *"entirely undelivered in the paper"*; *"The
  paper never enumerates the measure lengths present in its data"*; and F-10's two *"never
  defined"* / *"never explained"*. All four are now bounded to the eight pages as read.

### §8.3 The degradation tells, reported unprompted

**The user's standing rule of 2026-08-15 asks this side to recognise when a working session has
degraded and to say so without being asked, and to recommend handover at a verified stop once two or
more of the named tells appear. TWO APPEARED.**

**Tell A — a superlative or ranking put on this side's own findings without deriving it. Its
instances are NAMED at §8.2, at §10 and in this sitting's handoff entry, and are deliberately NOT
totalled: every total this side put on them went stale at the next pass, which is itself the tell it
is counting.** The four the sweep caught were caught before this file landed. **That they were caught
before landing does not lower the count** — the hundred-and-seventy-fourth's, -seventy-fifth's and
-seventy-sixth's closes each record that it does not, and this side takes the same position about its
own.

*(★ AMENDED AT THE USER-ORDERED CHECK (§10), IN PLACE RATHER THAN ANNOTATED, BECAUSE A THRESHOLD
PARAGRAPH IS WHERE A STALE COUNT DOES DAMAGE. FORMER WORDING, PRESERVED (#12): "**Four instances,
named at §8.2 and not totalled a second time.** All four were caught at the sweep, before this file
landed." **Made false by that check, which found a fifth inside §8.4 — the section reporting the tell
— and two more in the handoff entry.** The threshold conclusion is unchanged and is strengthened, not
weakened, by the further instances.)*

**Tell B — citing a summary instead of the source. One instance, and it is the sharper of the two
because the source was already open.** The first writing of F-8 identified this paper's third
baseline by reading the hundred-and-seventy-fifth entry's account of row 10, **when the reference
line naming that baseline was printed on page 7 of the paper this side had already read whole.**
It asserted an identity between two documents on two shared author names. **Caught at the
read-back, which is the pass that went to the page.**

**What the threshold means here, stated plainly and without inflation.** **What fired is TWO named
tells — the superlative one repeatedly and the summary-instead-of-source one once — not several
different tells, and this side claims nothing more than that.** **The instances are named at §8.2, at
§10 and in the handoff entry rather than added up here**, for the reason the amendment note above
gives. The recommendation that follows is the one the rule names: **handover at a verified stop, the
next member taken by a fresh session.** It is not a recommendation that anything be abandoned
mid-thing.

*(★ AMENDED AT THE USER-ORDERED CHECK (§10). FORMER WORDING, PRESERVED (#12): "**one of them four
times and one of them once — not two dozen instances**". **A count made false by that same check**,
and the second stale total this section carried.)*

### §8.4 The bound on this section

**The read-back and the sweep are further passes over the same writing by the same side, and nothing
here establishes that they caught everything.** Two things about their yield are worth carrying:

- **Every defect they struck is in this side's own account — of its acts, of its bounds, or of how
  its findings rank against each other. None is in a value taken from the paper**, and the sixty-four
  transcribed values all stand as first written.
- **One of them was invisible to the sweep and was caught only by going back to the page** — the
  false identity at F-8. **A sweep over one's own prose cannot catch a claim that is well-formed and
  wrong**; only the object can. *(★ CORRECTED AT THE USER-ORDERED CHECK (§10). FORMER WORDING,
  PRESERVED (#12): "**The one that mattered most** was invisible to the sweep". **A ranking of this
  read's own defects against one another, never derived** — and the fourth instance of the very tell
  §8.3 reports, sitting inside the section that reports it.)*

**This section was written after those two acts ran and not before them**, and it is the closing
section the eight-step procedure holds back until this point.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened for the first time AFTER this file had landed**, which is step 7 of
the hundred-and-sixty-ninth entry's §3 procedure and the point of the independence declaration at
§0. It is
`reading_pass/extracts/yang-cwitkowitz-duan-2023-harmonic-analysis-with-neural-semi-crf.md`,
**44,701 bytes at this sitting's own staging call**, matching the size the hundred-and-seventy-sixth
entry records from its listing. **It was read WHOLE.** Its own banner dates it 2026-09-06 and states
it was written by the session that booted on the hundred-and-twenty-third entry.

**That file is UNTOUCHED.** Nothing in it was edited, and the standing ground for leaving it so is
this line's own: rewriting another read's text destroys what the doubling is comparing.

**Every disagreement below was resolved AT THE PAPER**, by re-opening the page image a third time —
printed pages 677, 679 and 681 — and not by preferring one text to the other.

### §9.2 Every value TAKEN FROM THE PAPER that both extracts transcribed agrees, digit for digit

- **All four tables in full, in both files: Table 1's twelve values, Table 2's twenty-four, Table 3's
  sixteen and Table 4's twelve.** No disagreement at any cell. **Table 2's six bold marks also agree
  in both files, three inside the full model's row and three outside it.**
- **The eighteen ablation differences both files derived independently agree in magnitude at every
  one of the eighteen** — the two files use opposite sign conventions and state so, one writing the
  drop from the full model and the other the variant minus the full model.
- **The three sums over Table 1 agree** — 321 pieces, 93,802 crotchets, 43,939 chord annotations —
  each computed independently from the same twelve cells.
- **Every stated protocol value agrees**: λ = 0.001, learning rate 10⁻⁴, weight decay 10⁻², dropout
  0.2, samples of 96 frames, the 2:1 train/test split, transposition to 12 keys, the 47k label
  count, the 12-dimensional root, the 10-dimensional quality, the 12-dimensional pitch-class
  activation, the 24-dimensional input frame, and the frame length of one eighth of a beat.
- **The held file's size agrees at 318,293 bytes**, and both files record eight pages printed 676
  to 683.
- **Both reads independently reach the same identity finding — that there is none.** Title, authors,
  venue, year and licence are printed and match, and the first extract adds that they match the
  bibliography's own row, which this read did not open.

**★ THE BOUND ON THAT AGREEMENT, STATED BECAUSE IT IS NARROWER THAN IT LOOKS.** It reaches values
**taken from the paper** and claims about the paper. **The first extract's citations INTO this
project's record — `FRAMEWORK.md` at DP-C and §14.1 and the L2 charter, the findings surface's V10
row, `population.md` line 111, the bibliography's line 33, the slice derivation's line 66, the
progress record, both commissions, and the row 10 and row 11 extracts — are OUTSIDE that agreement:
this side opened none of them**, and §0 says so.

### §9.3 The disagreements, named rather than counted

**Four, of which three go against the first extract and ONE GOES AGAINST THIS ONE. None moves a
transcribed value.**

**(a) ★ AGAINST THIS READ — two words dropped from inside a quotation.** This file quoted §3.1.1 as
*"We use beat instead of note duration **to represent** the basic time unit"*. **The paper prints
*"in order to represent"***, established at printed page 677 at the cross-check. **The first extract
quotes it correctly.** Corrected at §2.2 with the former wording preserved (#12). **It is recorded
first, and not last, because this read reports three quotation defects against the other file and
carried one of its own.**

**(b) AGAINST THE FIRST EXTRACT — a singular for a plural inside a quotation.** It quotes §3.1.2 as
*"produces 47k different harmony labels, which **is** intractable"*. **The paper prints *"which are
intractable"***, established at printed page 677. The quotation appears twice in that file, in its
claims section and again at its finding (6), **with the same alteration both times**.

**(c) ★ AGAINST THE FIRST EXTRACT — one word substituted inside a quotation, and it is the only one
of the four whose substitute means something different.** It quotes §3.5 as *"non-chordal notes that should not **intersect** with chordal
notes of the underlying harmony"*. **The paper prints *"should not interact with"***, established at
printed page 679. **Why it matters: *intersect* is a claim about set membership — that the two note
sets do not overlap — and *interact* is a claim about influence in the model.** The sentence is the
paper's statement of what the absence score is FOR, so the substitution changes what the mechanism
is said to do. **No value moves and the finding it sits in is unaffected**, but a later reader
lifting the quotation would carry the altered sense.

**(d) AGAINST THE FIRST EXTRACT — one word substituted inside a long block quotation of §5.3.** It
quotes *"The phenomenon could result from the more difficult training **objective**."* **The paper
prints *"the more difficult training process"***, established at printed page 681. **Why it is
reported rather than waved through: *objective* has a technical sense in this very paper** — the
training objective is the negative log likelihood of Equation (13) — **so the substitution reads as
a claim about the loss where the paper says only that the training was harder.**

**★ A FIFTH ITEM THAT IS NOT A QUOTATION DEFECT AND IS RECORDED SEPARATELY.** The first extract
states, of the tables, *"Under Seg and Over Seg in the tables are the two one-sided scores; Overall
Seg is SQ."* **§6.3 of this file computes that the printed Overall column cannot be Equation (15)
applied to the printed directional columns in any of the eight rows.** **Resolved at the paper:
neither read is refuted about the paper's text** — the paper does define `SQ` at Equation (15) and
does head the column *Overall*, so the identification follows the paper's own naming. **What the
paper does not state is the level at which the segmentation quantities are aggregated**, and that is
what the arithmetic exposes. **So this is a check one read ran and the other did not, and its result
bears on that sentence of the first extract rather than contradicting it.**

**★ AND ONE CLAIM OF THE FIRST EXTRACT THAT THE PAPER DOES NOT PRINT, recorded without a verdict.**
It calls the first baseline *"a plain CRNN that decodes no segmentation at all"*. **The paper does
not say what the CRNN baseline decodes**, and **Table 4 reports under-, over- and overall
segmentation values for CRNN**, so a segmentation was obtained from it somehow and the paper does
not say how. **Nothing here establishes that the first extract's characterisation is wrong** — a
frame-level model's segmentation is ordinarily read off runs of equal labels — only that it is not
printed in the eight pages as read.

### §9.4 What the doubling produced that neither read had alone, in both directions

**★ THE DIRECTIONS ARE NOT SYMMETRICAL, AND ON ONE HALF THIS READ SAYS NOTHING AT ALL.**
*(★ CORRECTED AT THE USER-ORDERED CHECK (§10). FORMER WORDING, PRESERVED (#12): "**AND THE HALF THIS
READ IS SILENT ON IS THE LARGER**". **A comparison of two bodies of material this read never
measured against each other** — it opened none of the record half, so it is in no position to say
which is larger.)*

**What the first extract holds and this read does not, and on which this read takes no position.**
The whole of what the RECORD says: `FRAMEWORK.md` at DP-C, at §14.1 and at the L2 charter and design
points; the findings surface's V10 row and its re-verification; `population.md`'s line for it; the
bibliography's row; the slice derivation's line; the question carried forward from row 11; the
placement of this paper against rows 10, 11, 20 and 45; and the routing of each of its fifteen
findings to a design point. **This side opened none of those objects, so on that half this is not a
second opinion but silence.** **This side takes no position on that file's CENTRAL verdict**, nor on
its routings, nor on its reading of the record.

**Two precisions ADOPTED from the first extract into this file at the cross-check, each marked at its
site:** that **no maximum segment length is stated** anywhere in the paper (now §7.2(g1)), and that
**Equation (12)'s summation scope is ambiguous as printed** (now marked at §2.7). **This read did not
have either.**

**★ And one thing the first extract had right from the start that this read got wrong and fixed by
its own read-back, stated because the doubling deserves no credit for it.** Reference 21 is Masada &
Bunescu's ISMIR 2017 paper and not row 10's document. **The first extract says so plainly in three
places. This read's first writing said the opposite, and its own read-back caught it before the
cross-check began** (§8.2). **The two files now agree, and the agreement is not a product of the
doubling.**

**What this read holds and the first extract does not. Named rather than counted.**

1. **§6.3 — Equation (15) does not reproduce from the printed tables in any of the eight rows**, with
   the shortfall computed per row and the two surviving readings stated. The first extract relays the
   identification without computing it.
2. **F-1 in full — §5.3's opening sentence is refuted by Table 2 on three of six columns, the paper
   acknowledges two of the three, and the table's own bolding is internally consistent throughout.**
   The first extract records two of the three cells, as precision (c) of its finding (2), and does
   not record the third or draw the contradiction against the sentence.
3. **F-3 — Equation (5) as printed carries no softmax**, although it is named the scaled dot-product
   attention and cited to Vaswani et al. The first extract records the equation and the citation and
   not the discrepancy.
4. **F-4 and F-5 — the *absense* / *absence* inconsistency inside the paper, and four further
   typographical or grammatical defects.** The first extract preserves *"Followng Micci et al."* and
   marks it *"(as printed)"*, which is correct practice, and records none of the others and treats
   none as a defect.
5. **§6.5 — the sampling arithmetic.** Both files computed the same three sums; only this one went on
   to the per-corpus shares, the 1.45-fold spread in annotation density, and what the paper's own
   uniform-over-pieces sampling rule does with them.
6. **§6.6 — the *Overall* accuracy column refuted as the product of root and quality in all eight
   rows, and shown to lie strictly inside the bounds a joint-correctness reading requires in all
   eight.** The first extract states the weaker check — that it is below both — and reaches the same
   conjecture.
7. **§6.8 and §6.9 — three of the paper's equations checked and found coherent, and the 96-frame
   sample length worked out to the measure lengths its stated reason holds for and fails for.**
8. **F-8a — three members of this same slice in the reference list**, row 11 cited four times as the
   formalism's origin, and rows 17 and 18 at §2. **The first extract places references 6, 21 and 23
   against rows 11, 10 and 45; this read places references 6, 9 and 11 against rows 11, 18 and 17.
   Neither read placed all of them**, and between them five references are tied to rows.

### §9.5 What the cross-check does NOT establish

- **It does not establish that either file is clean.** Defects of this side's own had already been
  struck at the read-back and the sweep before the first extract was opened at all (§8.2), **and one
  more — a dropped pair of words inside a quotation — was found only here**, after a read-back, a
  sweep and a landing.
- **It does not reach the record half at all.** The digit-for-digit agreement at §9.2 covers values
  taken from the paper; the first extract's citations into this project's record are outside it and
  were checked at no object by this side.
- **It is not exhaustive.** It ran over what both files carry, sentence by sentence, and a later
  reader may find more. **No claim is made that the comparison was complete.**
- **Nothing went against this read at the cross-check except item (a)** — no claim of this file was
  refuted by the first extract, and no transcribed value moved in either direction. **That is a
  statement about what the comparison found, not a verdict on either file.**

---

## §10 — The user-ordered fact- and source-check, run after this file had landed twice

### §10.1 What the check was

The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes —
**completeness, coherence, correctness, and misuse of hyperbole and absolutes** — and his opening
instruction to this sitting ordered it over everything this side has written, the closing report
included. **It ran over this file and over the sitting's handoff entry, and it reached the closing
report as part of the same body of writing.**

### §10.2 What it found in this file — named rather than counted

**★ AND THE STRUCTURAL FINDING FIRST, BECAUSE IT EXPLAINS THE REST: §8 AND §9 WERE WRITTEN AFTER THE
SWEEP, SO NEITHER WAS EVER SWEPT.** The sweep at §8.2 ran over §0 to §7, which is what existed when
it ran. **Every defect this check found in this file sits in §8 or §9** — the two sections written
after the only sweep this file has had. **A next side should read that as the general case: the
sections that report a file's own checking are the sections no check has passed over.**

- **★ §8.4 ranked this read's own defects against one another** — *"The one that mattered most was
  invisible to the sweep"* — **never derived, and sitting inside the section that reports the very
  tell it is an instance of.** Corrected at its site with the former wording preserved (#12).
- **★ §9.3(c) ranked the four disagreements by worth** — *"this is the one worth carrying"*. Replaced
  by what is actually derivable: it is **the only one of the four whose substituted word means
  something different**, which is a statement about the words and not about their importance.
- **★ §9.4 compared two bodies of material this read never measured against each other** — *"the half
  this read is silent on is THE LARGER"*. **This read opened none of the record half**, so it is in
  no position to say which is larger. Corrected at its site.
- **★ §8.3's tell tally and its threshold paragraph were both made stale by this check** — the tally
  by the instance above, and by two further instances the same check found in the handoff entry.
  **Both are amended IN PLACE rather than annotated**, on the hundred-and-seventy-sixth's ground that
  a heading and a threshold are where a hurried reader takes a count from, with the former wordings
  preserved (#12).

### §10.3 What the check did NOT do, and what it does not establish

**It fetched no page image, opened no paper, did not re-open the first extract as a file, ran no web
access, and swept no repository.** **It changed no transcribed value, no count of the paper's, no
byte count, no modification time, no row number and no verdict**, and **it touched the first extract
not at all.**

**And it is a further pass over the same writing by the same side.** **Every defect it found is an
instance of the tell §8.3 already reports**, which is the same thing the three entries before this
one establish of their own checks: **reporting a defect class is not immunity from it.**

**★ WHAT THE PASSES TOGETHER ESTABLISH, AND IT IS NOT THAT THIS FILE IS CLEAN.** The read-back, the
sweep, the cross-check and this check each found defects the passes before them had left standing,
**and this one found four inside the sections written to report the others.** **Every one of them is
in this side's account of its own acts, its own bounds, or how its own findings rank against each
other — none is in a value taken from the paper**, and the sixty-four transcribed values stand as
first written through all four passes. **A fifth pass would be a fifth pass by the same side, and
nothing here says it would come back empty.**
