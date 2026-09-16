# EXTRACT — Sarawagi & Cohen, "Semi-Markov Conditional Random Fields for Information Extraction" — Task B candidacy row 11, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eight pages of the held PDF were read AT THE OBJECT: staged through the bridge and
> read with the file tools as page images. **No relay, no web-fetch read, no prompted extraction.** The
> held document prints no page numbers; **every location below is the page's position in the held
> document (1–8) and its section, equation or table number as printed.**
>
> **Why this paper and its place in L2's slice.** It is row 11 of `reading_pass/candidacy_upgrades.md`
> (line 73), ADMITTED there as *"The formalism under DP-C's chosen option, including the
> linear-versus-exponential result the design point carries. An L2 detail specification adopts or adapts
> it."* `cowork_l2_task_b_slice_derivation_2026_09_05.md` §4 (line 58) places it in L2's slice: *"The
> formalism under DP-C's chosen option."* It is second in group 2 of the proposed reading order
> ("segmentation decided with the labelling": rows 10, 11, 19, 20, 18, 4, 47). **The record cites this
> paper at two ratified places and one verified figure:** `FRAMEWORK.md` §9 DP-C (lines 690–701): *"the
> formal result that letting segment length be a decoded variable buys the expressive power of a
> high-order model at linear rather than exponential inference cost. [FACT — each reported by the work
> named.]"*; `FRAMEWORK.md` §14.1 (lines 1008–1010): *"The semi-Markov formalism, which gives the
> expressive power of a high-order model at linear rather than exponential inference cost, and the two
> symbolic systems built on it whose measured gains over event-level tagging are quoted at DP-C."*; and
> the findings surface's verification table carries **V10 VERIFIED**, whose `reading_pass/population.md`
> row (line 111) reads *"Linear-vs-exponential = Sarawagi & Cohen 2004, §2.3: semi-Markov cost 'only
> linear in L' against order-L CRFs' exponential cost (with their same-label restriction stated)"*. The
> row 10 extract (`reading_pass/extracts/masada-bunescu-2019-…`) cites it as the semi-CRF's THEORY
> primary and carries one question to it (below). Ruling 1 of
> `cowork_rulings_2026_09_05_l2_boot_list_sitting.md` keeps the gate: no derivation before L2's slice of
> Task B is read.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity — a finding of row 29's milder shape

Sunita Sarawagi, Indian Institute of Technology Bombay, and William W. Cohen, Center for Automated
Learning & Discovery, Carnegie Mellon University. Printed title: **"Semi-Markov Conditional Random
Fields for Information Extraction"**. The bibliography's row (`docs/research_papers/BIBLIOGRAPHY.md`
line 25) names *"Semi-Markov Conditional Random Fields," NIPS 2004*, with the NeurIPS proceedings URL
(`proceedings.neurips.cc/paper_files/paper/2004/…`), tier LINK. **The authors match; the printed title
carries the row's title as its first four words and adds "for Information Extraction"; the held
document prints NO venue, year, copyright or licence line anywhere** — no conference header, no page
numbers, no footer. So whether the held file is the NIPS 2004 proceedings text as published, or an
author's version, is not establishable from what is held; the row's URL is the only link to the venue.
Routed to the bibliography reconciliation beside rows 28's, 3's, 29's and 10's findings, as a milder
finding than row 29's (title a prefix match rather than a different title). Eight pages; five sections
(Introduction; CRFs and Semi-CRFs, with §2.1 Definitions, §2.2 An efficient inference algorithm, §2.3
Semi-Markov CRFs vs order-L CRFs, §2.4 Learning algorithm; Experiments with NER data, with §3.1
Baseline algorithms and datasets, §3.2 Features, §3.3 Results and Discussion; Related work; Concluding
Remarks), an Appendix (one paragraph), and 21 references; one figure, two tables, seven numbered
equations, five footnotes.

**File:** `docs/research_papers/sarawagi_cohen_2004_nips_semi_markov_crf.pdf` (87,343 bytes at the
listing).

## Claims, labeled

### What the method decides, and from what

**★ [FACT, p. 1 Abstract; p. 2 §2.1] The model decides a SEGMENTATION of an input sequence and a LABEL
per segment, TOGETHER, in one decode — the label is assigned to the segment, not to the elements.**
*"a semi-CRF on an input sequence x outputs a 'segmentation' of x, in which labels are assigned to
segments (i.e., subsequences) of x rather than to individual elements x_i of x. Importantly, features
for semi-CRFs can measure properties of segments, and transitions within a segment can be
non-Markovian."* (p. 1.) The formal object (p. 2): a segmentation s = ⟨s_1, …, s_p⟩ where segment
s_j = ⟨t_j, u_j, y_j⟩ has a start position t_j, an end position u_j and a label y_j ∈ Y; *"a segment
means that the tag y_j is given to all x_i's between i = t_j and i = u_j, inclusive"*; segments have
positive length and *"completely cover the sequence 1…|x| without overlapping"*: t_1 = 1, u_p = |x|,
1 ≤ t_j ≤ u_j ≤ |x|, t_{j+1} = u_j + 1.

**★ [FACT, p. 2 §2.1, eq. 2] The segment feature functions SEE THE PREVIOUS SEGMENT'S LABEL — the
"Markovian" restriction the paper makes is that every segment feature is a function of x, the current
segment s_j, and the label y_{j−1} of the preceding segment, and nothing earlier.** *"We now assume a
vector g = ⟨g^1, …, g^K⟩ of segment feature functions, each of which maps a triple (j, x, s) to a
measurement g^k(j, x, s) ∈ R, and define G(x, s) = Σ_j g(j, x, s). We also make a restriction on the
features, analogous to the usual Markovian assumption made in CRFs, and assume that every component
g^k of g is a function only of x, s_j, and the label y_{j−1} associated with the preceding segment
s_{j−1}. In other words, we assume that every g^k(j, x, s) can be rewritten as g^k(j, x, s) =
g'^k(y_j, y_{j−1}, x, t_j, u_j) (2)."* The estimator is Pr(s | x, W) = exp(W·G(x, s)) / Z(x) with
Z(x) = Σ_{s'} exp(W·G(x, s')) (eq. 3, p. 2). **This ANSWERS the question the row 10 extract carried:
the original semi-CRF gives its segment features access to the previous label; row 10's "weak"
semi-CRF (Muis & Lu 2016) is the restriction of eq. 2 to segment-label features f(s_k, y_k, x) that do
NOT see y_{k−1}, plus separate label-transition features g(y_k, y_{k−1}, x).** In the original form
there is no such split: one feature vector, every component of which may depend jointly on the
segment, its label and the previous label.

**★ [FACT, p. 3 §2.2, eq. 4] Inference is exact by a semi-Markov Viterbi recursion over segment
lengths d = 1…L and previous labels y′, with L an upper bound on segment length.** *"Let L be an upper
bound on segment length. … V(i, y) = max_{y′, d=1…L} V(i−d, y′) + W·g(y, y′, x, i−d+1, i) if i > 0;
0 if i = 0; −∞ if i < 0 (4). The best segmentation then corresponds to the path traced by
max_y V(|x|, y)."* (p. 3.) The argmax is over W·Σ_j g(y_j, y_{j−1}, x, t_j, u_j) (p. 3, top). **L is a
FIXED INPUT to the decode, not a decoded quantity**; the paper's own choice of it is at §3.3 below.

**★ [FACT, p. 3 §2.3] THE COST RESULT THE RECORD CITES, in the paper's own words, with its three
qualifications.** *"Since conventional CRFs need not maximize over possible segment lengths d,
inference for semi-CRFs is more expensive. However, Equation 4 shows that the additional cost is only
linear in L. For NER, a reasonable value of L might be four or five.¹ Since in the worst case L ≤ |x|,
the semi-Markov Viterbi algorithm is always polynomial, even when L is unbounded. For fixed L, it can
be shown that semi-CRFs are no more expressive than order-L CRFs. For order-L CRFs, however the
additional computational cost is exponential in L. The difference is that semi-CRFs only consider
sequences in which the same label is assigned to all L positions, rather than all |Y|^L length-L
sequences. This is a useful restriction, as it leads to faster inference."* Footnote 1: *"Assuming that
non-entity words are placed in unit-length segments, as we do below."* **The three qualifications, each
the paper's own:** (a) the expressiveness claim is an UPPER BOUND — semi-CRFs are *"no more
expressive than"* order-L CRFs, and *"it can be shown"* is asserted with no proof in the held document;
(b) what is bought at linear cost is the SAME-LABEL SUBSET of the order-L model's sequences, which the
paper calls *"a useful restriction"*; (c) the concluding remarks (p. 7 §5) state the claim at the width
the paper itself chooses: *"Semi-CRFs are a tractable extension of CRFs that offer MUCH OF the power of
higher-order models without the associated computational cost"* (emphasis added). So the framework's
*"buys the expressive power of a high-order model at linear rather than exponential inference cost"*
has its values at the object (linear in L; exponential in L) and its wording is one notch wider than
the paper's own *"much of the power"* — a precision, recorded at finding (2) below; no value moves.

**★ [FACT, p. 3 §2.3] The test for whether a feature actually needs the segmental model: a semi-CRF
factorizes into an order-1 CRF if and only if the sum of its segment features can be rewritten as a
sum of local features.** *"let d_j denote the length of a segment, and let μ be the average length of
all segments with label I. Now consider the segment feature g^{k1}(j, x, s) = (d_j − μ)²·[[y_j = I]].
After training, the contribution of this feature toward Pr(s|x) associated with a length-d entity will
be proportional to e^{w_k·(d−μ)²} — i.e., it allows the learner to model a Gaussian distribution of
entity lengths. An exponential model for lengths could be implemented with the feature g^{k2}(j, x, y)
= d_j·[[y_j = I]]. In contrast to the Gaussian-length feature above, g^{k2} is 'equivalent to' a local
feature function f(i, x, y) = [[y_i = I]], in the following sense: for every triple x, y, s, where y is
the tags for s, Σ_j g^{k2}(j, x, s) = Σ_i f(i, s, y). Thus a semi-CRF model based on the single feature
g^{k2} could also be represented by a conventional CRF. In general, a semi-CRF model can be factorized
in terms of an equivalent order-1 CRF model if and only if the sum of the segment features can be
rewritten as a sum of local features. Thus the degree to which semi-CRFs are non-Markovian depends on
the feature set."* (p. 3.)

**★ [FACT, p. 3–4 §2.4, eqs. 5–7] Learning: maximise the conditional log-likelihood over labeled
segmentations; the objective is convex; solved by a limited-memory quasi-Newton method; the gradient
needs the partition function and the feature expectations, computed by a forward–backward analogue
with the same L-fold inner sum.** *"L(W) = Σ_ℓ log Pr(s_ℓ | x_ℓ, W) = Σ_ℓ (W·G(x_ℓ, s_ℓ) − log
Z_W(x_ℓ)) (5) … Equation 5 is convex, and can thus be maximized by gradient ascent, or one of many
related methods. (In our implementation we use a limited-memory quasi-Newton method [13, 14].)"*
(pp. 3–4.) Gradient (eqs. 6–7): Σ_ℓ G(x_ℓ, s_ℓ) − E_{Pr(s′|W)} G(x_ℓ, s′). The forward quantity
(p. 4): *"α(i, y) = Σ_{d=1}^{L} Σ_{y′∈Y} α(i−d, y′) e^{W·g(y, y′, x, i−d+1, i)}"* with α(0, y) = 1 and
α(i, y) = 0 for i < 0; Z_W(x) = Σ_y α(|x|, y); and a recursion η^k(i, y) for the k-th feature's
expectation, restricted to segmentations ending at position i, with E_{Pr(s′|W)} G^k(s′, x) =
(1/Z_W(x)) Σ_y η^k(|x|, y). Footnote 2: space can be reduced from M·L·|Y| to M·|Y| (M the sequence
length) by pre-computing a set of backward values.

### The experimental setting (p. 4 §3.1; p. 5 §3.2)

**[FACT, p. 4 §3.1] The task is named entity recognition in TEXT; two conventional-CRF baselines.**
*"we trained semi-CRFs to mark entity segments with the label I, and put non-entity words into
unit-length segments with label O. We compared this with two versions of CRFs. The first version,
which we call CRF/1, labels words inside and outside entities with I and O, respectively. The second
version, called CRF/4, replaces the I tag with four tags B, E, C, and U, which depend on where the word
appears in an entity [2]."* Five NER problems on three corpora: the **Address** corpus (4,226 words,
395 home addresses of students at a major university in India; city names and state names), the
**Jobs** corpus (73,330 words, 300 computer-related job postings; company names and job titles), and
the **Email** corpus (18,121 words, 216 messages from the CSPACE corpus, a 14-week 277-person
management game; person names).

**[FACT, p. 5 §3.2] The features.** For CRFs: indicators for specific words at position i or within
three words of i, and capitalization/letter-pattern indicators (*"Aa+"*, *"D"*). For semi-CRFs: the
same word-level features and *"their logical extensions to segments"* — indicators for the phrase
inside a segment and the capitalization pattern inside a segment, words and capitalization patterns in
three-word windows before and after the segment, *"indicators for each segment length (d = 1, …, L)"*,
and all word-level features combined with indicators for the beginning and end of a segment. Beyond
these, **dictionary-derived segment features**: g^{D,sim}(j, x, s) = argmax_{u∈D} sim(x_{s_j}, u), the
distance from the segment's word sequence to its closest entry in a dictionary D, under three
similarity measures (Jaccard, TFIDF, JaroWinkler); *"All of the distance metrics are non-Markovian —
i.e., the distance-based segment features cannot be decomposed into sums of local features."* One
external dictionary per task (rote matching alone gives F1 from 22% for job titles to 57% for person
names); and an **internal segment dictionary** built on the fly from the training data's labeled
segments, with the segment's own string excluded when finding its nearest neighbour (*"a sort of
nearest-neighbor classifier … a sort of bi-level stacking [21]"*). Local (word-level) versions of the
dictionary features were also built for the CRF baselines.

### Measured results (pp. 5–7 §3.3; Table 1 p. 6; Table 2 p. 7; Figure 1 p. 6)

**[FACT, p. 5 §3.3] Protocol.** *"In each experiment performance was averaged over seven runs, and
evaluation was performed on a hold-out set of 30% of the documents. In the table the learners are
trained with 10% of the available data — as the curves show, performance differences are often smaller
with more training data. Gaussian priors were used for all algorithms, and for semi-CRFs, a fixed
value of L was chosen for each dataset based on observed entity lengths. This ranged between 4 and 6
for the different datasets."* F1 = 2·precision·recall/(precision + recall) (footnote 3).

**★ [FACT, Table 1, p. 6] F1 on the five tasks (state, title, person, city, company), in the four
conditions — baseline; with the internal dictionary; with the external dictionary; with both — every
cell as printed (Δbase and Δextern are the paper's percentage changes relative to the baseline and to
the external-only condition).**

| Learner | baseline F1 | +internal F1 (Δbase) | +external F1 (Δbase) | +both F1 (Δbase, Δextern) |
|---|---|---|---|---|
| CRF/1 state | 20.8 | 44.5 (113.9) | 69.2 (232.7) | 55.2 (165.4, −67.3) |
| CRF/1 title | 28.5 | 3.8 (−86.7) | 38.6 (35.4) | 19.9 (−30.2, −65.6) |
| CRF/1 person | 67.6 | 48.0 (−29.0) | 81.4 (20.4) | 64.7 (−4.3, −24.7) |
| CRF/1 city | 70.3 | 60.0 (−14.7) | 80.4 (14.4) | 69.8 (−0.7, −15.1) |
| CRF/1 company | 51.4 | 16.5 (−67.9) | 55.3 (7.6) | 15.6 (−69.6, −77.2) |
| CRF/4 state | 15.0 | 25.4 (69.3) | 46.8 (212.0) | 43.1 (187.3, −24.7) |
| CRF/4 title | 23.7 | 7.9 (−66.7) | 36.4 (53.6) | 14.6 (−38.4, −92.0) |
| CRF/4 person | 70.9 | 64.5 (−9.0) | 82.5 (16.4) | 74.8 (5.5, −10.9) |
| CRF/4 city | 73.2 | 70.6 (−3.6) | 80.8 (10.4) | 76.3 (4.2, −6.1) |
| CRF/4 company | 54.8 | 20.6 (−62.4) | 61.2 (11.7) | 25.1 (−54.2, −65.9) |
| semi-CRF state | 25.6 | 35.5 (38.7) | 62.7 (144.9) | 65.2 (154.7, 9.8) |
| semi-CRF title | 33.8 | 37.5 (10.9) | 41.1 (21.5) | 40.2 (18.9, −2.5) |
| semi-CRF person | 72.2 | 74.8 (3.6) | 82.8 (14.7) | 83.7 (15.9, 1.2) |
| semi-CRF city | 75.9 | 75.3 (−0.8) | 84.0 (10.7) | 83.6 (10.1, −0.5) |
| semi-CRF company | 60.2 | 59.7 (−0.8) | 60.9 (1.2) | 60.9 (1.2, 0.0) |

The paper's own reading (pp. 6–7): *"In the baseline configuration in which no dictionary features are
used, semi-CRFs perform best on all five of the tasks. When internal dictionary features are used, the
performance of semi-CRFs is often improved, and never degraded by more than 2.5%. However, the
less-natural local version of these features often leads to substantial performance losses for CRF/1
and CRF/4. Semi-CRFs perform best on nine of the ten task variants for which internal dictionaries
were used. The external-dictionary features are helpful to all the algorithms. Semi-CRFs performs best
on three of five tasks in which only external dictionaries were used. Overall, semi-CRF performs quite
well. If we consider the tasks with and without external dictionary features as separate 'conditions',
then semi-CRFs using all available information⁴ outperform both CRF variants on eight of ten
'conditions'."* Footnote 4: *"I.e., the both-dictionary version when external dictionaries are
available, and the internal-dictionary only version otherwise."* Figure 1 (p. 6) plots F1 against the
fraction of available training data (0.05 to 0.5) for Address_State, Address_City and Email_Person,
for CRF/4, SemiCRF+int, CRF/4+dict and SemiCRF+int+dict; the caption: *"We do not use internal
dictionary features for CRF/4 since they lead to reduced accuracy."*

**★ [FACT, Table 2, p. 7] Raising the ORDER of a conventional CRF does not recover the semi-CRF's
gain.** F1 for order-L CRFs, L = 1, 2, 3, against the semi-CRF: Address_State — CRF/1 20.8 / 20.1 /
19.2, CRF/4 15.0 / 16.4 / 16.4, semi-CRF 25.6; Address_City — CRF/1 70.3 / 71.0 / 71.2, CRF/4 73.2 /
73.9 / 73.7, semi-CRF 75.9; Email_persons — CRF/1 67.6 / 63.7 / 66.7, CRF/4 70.9 / 70.7 / 70.4,
semi-CRF 72.2. *"For these tasks, the performance of CRF/4 and CRF/1 does not seem to improve much by
simply increasing order."* (pp. 6–7.) Footnote 5: *"Order-L CRFs were implemented by replacing the
label set Y with Y^L. We limited experiments to L ≤ 3 for computational reasons."*

### Related work and the paper's own bound (p. 7 §4, §5)

**[FACT, p. 7 §4]** Semi-CRFs are *"similar to nested HMMs [1], which can also be trained
discriminatively [17]"*, differing in that the inner model is *"of short, uniformly-labeled segments
with non-Markovian properties"*. **Models with a random variable per possible segment are strictly
more expressive and NOT tractable:** *"by creating a random variable for each possible segment, one
can learn models strictly more expressive than the semi-Markov models described here. However, for
these methods, inference is not tractable, and hence approximations must be made in training and
classification."* Against the authors' earlier voted-perceptron semi-Markov learner [6, 7]:
*"semi-CRFs perform somewhat better, on average"*, and *"Probabilistically-grounded approaches like
CRFs also are preferable to margin-based approaches like the voted perceptron in certain settings,
e.g., when it is necessary to estimate confidences in a classification."*

**[FACT, p. 7 §5]** *"Semi-CRFs are a tractable extension of CRFs that offer much of the power of
higher-order models without the associated computational cost. A major advantage of semi-CRFs is that
they allow features which measure properties of segments, rather than individual elements. For
applications like NER and gene-finding [11], these features can be quite natural."* Appendix: an
implementation at crf.sourceforge.net and a NER package at minorthird.sourceforge.net.

**[THEORY, as the paper cites it]** Lafferty, McCallum & Pereira 2001 [12] (row 12) for the CRF;
Sha & Pereira 2003 [16] (row 14) for the CRF notation and forward–backward; semi-Markov chain models
[8, 9]; nested HMMs [1, 17]; L-BFGS [13, 14].

**[CONJECTURE — the authors' own, labelled as such here]** That the tractable extension studied
could improve inference for the more expressive per-segment-variable models (*"An interesting question
for future research"*, p. 7).

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- A discrete input sequence x = ⟨x_1, …, x_|x|⟩ of elements — words, in the paper — over which a
  segmentation is defined by integer positions; the grid of admissible boundaries is every position.
- A fixed label set Y, one label per segment; in the paper's own use, non-entity elements are forced
  into unit-length segments labelled O (footnote 1), so the semi-Markov machinery is exercised only on
  the entity segments.
- A fixed upper bound L on segment length, supplied before the decode; chosen in the paper *"based on
  observed entity lengths"* per dataset (4 to 6).
- Training data as labeled segmentations (x_ℓ, s_ℓ) — segment boundaries and labels both given.
- Features may be arbitrary real-valued functions of the whole input x, the current segment's
  boundaries and label, and the previous segment's label (eq. 2) — including non-decomposable ones
  such as edit-distance to a dictionary entry.

**What it HANDS downstream.**
- One best labeled segmentation: contiguous, non-overlapping segments covering the whole input, each
  with one label (the argmax of eq. 3 by eq. 4).
- A normalised conditional distribution Pr(s | x, W) over all labeled segmentations (eq. 3), with the
  partition function computable exactly (p. 4) — so posterior quantities are available in principle,
  though the paper reports only F1 of the best path; it names confidence estimation as a setting where
  the probabilistic form is preferable (p. 7 §4).

**Its own STATED SCOPE and limits.**
- **Domain:** information extraction from text — named entity recognition on three English-language
  corpora; gene-finding and NP-chunking named as tasks where *"similar arguments might be made"*
  (p. 1). **Nothing musical anywhere in the paper.**
- **Expressiveness:** for fixed L, no more expressive than an order-L CRF; the same-label restriction;
  non-Markovian only to the degree the feature set is (p. 3 §2.3); strictly less expressive than a
  model with a variable per possible segment, which is intractable (p. 7 §4).
- **Cost:** decode and training both linear in L over the first-order CRF's cost; polynomial even for
  unbounded L since L ≤ |x| (p. 3).
- **Fitting:** discriminative (conditional likelihood), convex, quasi-Newton, Gaussian priors;
  30% hold-out, seven runs averaged; training on 10% of the data in the table, with the authors'
  own statement that the differences shrink with more training data (p. 5).
- **Coupling:** segmentation and label decided together; one label per segment; the previous
  segment's label available to every feature; no hierarchy, no second label axis.

## What an L2 detail specification could adopt, adapt, or must argue against

- **Adopt (the formalism of DP-C's chosen "with"):** the labeled-segmentation state space, the
  semi-Markov Viterbi of eq. 4 over (previous label, segment length ≤ L), and the exact
  forward–backward of §2.4 for normalisation — the machinery `FRAMEWORK.md` §14.1 names and row 10
  instantiates on music.
- **Adopt (a feature form richer than row 10's):** eq. 2 lets every segment feature see the previous
  label. Row 10 restricted itself to the weak form for speed; the original form admits, at the same
  asymptotic cost (eq. 4 already maximises over y′), a segment-content score conditioned on what came
  before — the shape a chord-transition term that depends on the whole segment, or a tonality-aware
  segment score, would take.
- **Adapt (the factorization test as a design check):** §2.3's if-and-only-if — a segment feature
  needs the segmental decode exactly when its sum cannot be rewritten as a sum of per-element
  features. A Gaussian (or any non-linear) segment-length prior needs it; a length-proportional one
  does not. Every candidate term of L2's score can be classed by this test, and the class decides
  whether the segmental machinery is doing work for that term.
- **Adapt (the maximum segment length L as a declared input):** the paper sets L per dataset from the
  observed lengths of the thing being segmented. `CLAUDE.md` records the decode segment cap's value as
  a founding instance of the "derivation not recorded" gap (D-004); this paper is a published
  precedent for deriving such a cap from the observed length distribution of the annotated segments —
  a datum, not a derivation.
- **Adapt (the label axis):** the formalism carries ONE label per segment. L2's entangled decision
  (tonality, boundary, chord tones, chord) fits it only as a product label — a (tonality, chord) pair
  per segment, at |Y| multiplied — or as a structure this paper does not describe. The paper's Table 2
  and footnote 5 show the cost of enlarging Y by a power (order-L CRFs as Y^L, limited to L ≤ 3 *"for
  computational reasons"*), which is the same growth a product label incurs.
- **Must argue against:** nothing in the paper decides a musical question; its measured gains are on
  text with hand-built dictionaries, at 10% training data, with differences the authors say shrink with
  more data (Table 1, Figure 1) — so it carries the FORMAL result and no musical evidence; the
  same-label restriction is the paper's own statement of what the formalism does NOT express, and an
  L2 design that needs within-segment label change (none is on the record) would be outside it; and
  the per-segment-variable models the paper names as *"strictly more expressive"* are its own stated
  intractable rival.

## ★ Findings, routed and not applied

**(1) IDENTITY: the printed title is "Semi-Markov Conditional Random Fields for Information
Extraction", the bibliography's row names "Semi-Markov Conditional Random Fields," NIPS 2004; the
authors match; the held document prints no venue, year, copyright or licence line.** A prefix match
on the title, so milder than row 29's finding; whether the held file is the proceedings text is not
establishable from what is held. Routed to the bibliography reconciliation with the tier precision
that no licence is printed (the row's tier reads LINK). No verdict.

**(2) V10's linear-versus-exponential result RE-VERIFIED at the object, with three precisions to the
[FACT]'s wording.** The values: *"the additional cost is only linear in L"* against order-L CRFs'
*"exponential in L"* — at §2.3, p. 3, as `population.md` line 111 records, same-label restriction
included. The precisions: (a) the paper's expressiveness claim is an UPPER BOUND — semi-CRFs are *"no
more expressive than order-L CRFs"* — stated with *"it can be shown"* and no proof in the held
document; (b) the paper's own width for what is bought is *"much of the power of higher-order models"*
(§5), where `FRAMEWORK.md` lines 697–698 and 1008–1009 read *"the expressive power of a high-order
model"*; (c) the qualification the paper attaches — *"the degree to which semi-CRFs are non-Markovian
depends on the feature set"* — means the result is about the DECODE's cost for a given feature set,
not a property that holds independently of which segment features are used. Nothing is owed to the
[FACT] as a cost statement; the wording precision (b) is routed to the findings surface's V10 row and
DP-C block. No verdict.

**(3) The question carried from row 10 is ANSWERED at the object: the original semi-CRF's segment
features DO see the previous segment's label (eq. 2, p. 2).** Row 10's weak form is a restriction of
this, made *"for faster inference"* by row 10's authors following Muis & Lu 2016, not a property of the
formalism. Consequence for the record: where DP-C or an L2 detail specification cites "the semi-Markov
formalism", the formalism admits previous-label-conditioned segment scores at no asymptotic cost
beyond eq. 4's maximisation over y′; the split into label-independent segment features and separate
transition features is row 10's choice. Routed to L2's detail specification beside DP-C and the row 10
extract; no verdict.

**(4) The factorization test (§2.3) as a design check for L2's score terms.** A segment term needs the
segmental decode if and only if it is not a sum of per-element terms; the paper's own example puts a
Gaussian segment-length prior on the needs-it side and an exponential one on the does-not side. A
datum for L2's detail specification (which terms of the score earn the segmental machinery) and beside
row 20 (Korzeniowski & Widmer's duration model, next-but-one in the order), whose segment-duration
model would be classed by this test. No verdict.

**(5) L, the maximum segment length, is a DECLARED INPUT chosen from the observed length distribution
of the annotated segments — a published precedent beside D-004's unrecorded derivation.** *"a fixed
value of L was chosen for each dataset based on observed entity lengths. This ranged between 4 and 6"*
(p. 5). `CLAUDE.md`'s defense-at-home rule names *"the decode segment cap's value (4)"* as a founding
instance of a decision recorded with no derivation. This paper does not derive our cap; it shows one
published way such a cap is set. Routed to L2's detail specification beside D-004; no verdict.

**(6) The measured gains are TEXT-DOMAIN and bounded by the authors' own protocol.** Five NER tasks;
semi-CRF over the better CRF baseline by 1.3 to 5.4 F1 points at baseline features (Table 1: state
25.6 vs 20.8; title 33.8 vs 28.5; person 72.2 vs 70.9; city 75.9 vs 73.2; company 60.2 vs 54.8);
trained on 10% of the data with the authors' statement that differences *"are often smaller with more
training data"*; the largest gains come with the non-decomposable dictionary features, which are the
paper's own point (segment-level features, not the decode alone). Table 2 shows that order-2 and
order-3 CRFs do not close the gap. **Nothing here is evidence about music**; the musical measurements
under DP-C are rows 10's and 19's. Routed to the findings surface's DP-C block as a domain-bounded
datum, so the formalism paper is not later cited as if it measured the musical gain; no verdict.

**(7) A second published instance, beside row 10's, of a fully discriminative, convex, regularised fit
with no frozen counted table** — the opposite shape to D-525's staged fit — and with fit/evaluation
separation at the object (30% hold-out, seven runs; #20). Routed to L2's detail specification beside
D-525 and DP-P, and to measurement design; no verdict.

**(8) The paper's own stated rival: models with a random variable per possible segment are strictly
more expressive and intractable (§4).** A bound for any L2 design that would score every candidate
segment independently rather than through a chain over segments — the paper says exact inference is
then unavailable. Routed to L2's detail specification; no verdict.

**(9) One label per segment; no second axis.** The formalism as published carries a single label
alphabet per segment; L2's entangled state is expressible in it only as a product label, whose cost
growth the paper's own Table 2 / footnote 5 illustrate for the analogous Y^L construction. Neither
for nor against any chosen point — the framework's joint state is already a product (tonic, mode,
degree) by D-526's design — but a datum on where the decode cost goes. Routed to L2's detail
specification beside D-004 (the state space) and D-526; no verdict.

**(10) Posterior quantities are available exactly (Z and the expectations, §2.4), and the authors name
confidence estimation as a setting where the probabilistic form is preferable (§4).** A datum beside
D-006 (two full candidate lists, no truncation), D-008 (true probabilities deferred) and DP-K: the
formalism can publish a normalised distribution over labeled segmentations, not only the best path.
Routed to L2's detail specification; no verdict.

**(11) No falsifier.** Nothing read contradicts any CHOSEN design point. The one ratified [FACT] resting
on this paper (the cost result in DP-C's ground, part of V10) is re-verified at the object; its wording
is one notch wider than the paper's own and the precision is routed. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL, on a narrow ground, challengeable at the progress record.** Ratified text rests on it at one
place — DP-C's *"formal result"* [FACT] (`FRAMEWORK.md` lines 697–698), restated at §14.1 — and the
original commission's §4 makes a paper *"whose claims would carry load in a detail specification or
against a design point"* central; further, it is the formalism named by the candidacy row as what *"an
L2 detail specification adopts or adapts"*, and findings (3), (4) and (5) are claims an L2 detail
specification would cite this paper for directly (previous-label access; the factorization test; the
cap-from-observed-lengths precedent). **The ground on which NOT CENTRAL could be argued, stated so the
challenge is easy to make:** the paper carries no musical content and no musical measurement; the one
figure the record rests on is a cost statement already verified by the pass at `population.md` §3
(V10), so this whole-paper read adds precisions and no new verification; and the musical instances of
the formalism (rows 10 and 19) are the papers a detail specification would cite for what the machinery
does on our input. **A second independent extraction is therefore OWED** on this verdict.

## What this extract does NOT do

It derives no specification statement. It amends no document — `FRAMEWORK.md`,
`reading_pass/candidacy_upgrades.md`, `reading_pass/population.md`, `docs/research_papers/BIBLIOGRAPHY.md`
and `cowork_reading_pass_findings_2026_08_31.md` are untouched; findings (1) to (10) are routed and
written nowhere else. It does not fetch the NIPS 2004 proceedings version, the authors' earlier
voted-perceptron paper [6], Muis & Lu 2016, the crf.sourceforge.net implementation, or any of the three
corpora. It opens no code, touches no measurement tool, no corpus, no golden and nothing under
`tools/`. It writes no open-items row and allocates no decisions-register identity. It reads no other
paper and takes no decision about the order of the remaining slice.

---

*Provenance: written 2026-09-06 by the Cowork session that booted on
`cowork_handoff_entry_one_hundred_and_twenty_two.md`, on the user's opening instruction naming row 11,
after the ordinary session-start read (`CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md` whole, the
derived gating answer). Read for this extract, at the files: `reading_pass/candidacy_upgrades.md` whole
(row 11 at line 73), `cowork_l2_task_b_slice_derivation_2026_09_05.md` at line 58,
`docs/research_papers/BIBLIOGRAPHY.md` at lines 1–40 (row 11 at line 25), `FRAMEWORK.md` at lines
686–703 (DP-B's close and DP-C) and 1000–1015 (§14.1), located by a `Grep` of the staged tree for
"Sarawagi", "semi-Markov" and "semi-CRF"; the findings surface at lines 150–209 (the DP-C block);
`reading_pass/population.md` at lines 98–115 (§3, the load-bearing table; V10 at line 111); the progress
record whole; both commissions whole; and the row 10 extract at its opening, identity, model, coupling,
adopt-or-argue, findings, centrality and provenance sections (lines 1–130 and 395–601), for the form and
for the carried question. The paper itself was read at the object as page images, all eight pages. No
shell command was run on the repository or on any staged copy of it for content or for listings; the
saved root listing was consulted by `Grep` only. No figure of this project's own measurement is
restated (#17f, D-431); every value above is the paper's own.*
