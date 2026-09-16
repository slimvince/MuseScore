# Second extraction — Sarawagi & Cohen, "Semi-Markov Conditional Random Fields for Information Extraction"

**STATUS: SECOND INDEPENDENT EXTRACTION, WRITTEN WITHOUT CONSULTING THE FIRST EXTRACT.** Row 11 of
Task B's L2 slice. Written under `cowork_reading_pass_commission_2026_08_30.md` §4, fourth bullet, as
that rule is quoted verbatim at the hundred-and-sixty-ninth handoff entry's §3, and by the eight-step
order that entry's §3 states. The commission itself was not opened by this side, so this file's
compliance with the commission's form is a relay through that entry; a later side that wants it
established opens the commission's §4.

---

## §0 — What was read, and the bound on this read's independence

**The held file.** `docs/research_papers/sarawagi_cohen_2004_nips_semi_markov_crf.pdf`, **87,343
bytes** at a bridge listing of `docs/research_papers/` and the same at the staging call that brought
it into this session's container. **Eight pages, established AT THE TOOL** by a deliberately
out-of-range page request, which answered *"PDF has 8 pages"*. No value from the reading-progress
record was available to match either against: **the progress record was not opened by this side at
all.**

**What was read, named rather than counted.** All eight pages as page images, in two requests — pages
1 to 4 and pages 5 to 8 — **and then every one of the eight again at the read-back, in four further
requests named at §8.1.** *(★ CORRECTED AT THE USER-ORDERED CHECK, §10. FORMER WORDING, PRESERVED
(#12): the sentence ended at *"pages 5 to 8"*, which was true when written and was made incomplete by
this read's own read-back — cadence 8's class, a sentence about the sitting's own state going false
while the sitting works.)* **Every image was present and legible, checked at the images themselves and
not at the calls' success lines** (the page-image fault the cadence list names did not fire; that is
not evidence it is gone). The out-of-range request returned the refusal it was made for and no image.

**What was NOT read.** Row 11's first extract — `reading_pass/extracts/sarawagi-cohen-2004-semi-markov-conditional-random-fields.md`,
**36,476 bytes** at a listing of that one directory — **was not opened before the cross-check step,
and its name and its size are the only things taken from that listing.** Not read, not searched, not staged by this
side: `FRAMEWORK.md` at all, `OPEN_ITEMS.md`, `ARCHITECTURE.md`,
`reading_pass/l2_slice_reading_progress.md` at all, the findings surface, `population.md`, the slice
derivation, `docs/research_papers/BIBLIOGRAPHY.md`, both commissions, every other extract, every other
paper, and every file under `docs/research_papers/polyph9-release/`.

**THE INDEPENDENCE BOUND, DECLARED AND NOT CLAIMED AWAY.** This side booted on the
hundred-and-seventy-fifth handoff entry and read the hundred-and-seventy-fourth, -seventy-third and
-sixty-ninth whole, and the hundred-and-seventieth at its §1, as the boot ordered. *(★ CORRECTED AT THE
USER-ORDERED CHECK, §10: the former wording named the hundred-and-seventieth in the same breath as the
three read whole, which would have a reader take it for a whole read.)* **Those entries say nothing about this paper's
content.** What this side did read about row 11 before opening the paper is one line — row 11's line
73 of `reading_pass/candidacy_upgrades.md`, which states the row's verdict (**ADMITTED**) and its
reason: *"The formalism under DP-C's chosen option, including the linear-versus-exponential result the
design point carries. An L2 detail specification adopts or adapts it."* **That sentence told this side
in advance that the paper carries a linear-versus-exponential result, and that is contamination of a
kind: this read did not discover that the result exists.** It is written down rather than argued away.
What the line did NOT carry: the direction of the result, its argument, its conditions, any value, any
table, or any of the paper's scope limits.

**One further piece of form, not content.** Row 10's second extract was opened **at its section
headings alone**, by a heading search, to take this line's own section form rather than invent one.
**No content line of that file was read.**

---

## §1 — What the paper is, and one finding at the identity axis

**Printed title:** *"Semi-Markov Conditional Random Fields for Information Extraction"*, page 1.

**Printed authors and affiliations,** page 1, in the two-column arrangement the page carries: **Sunita
Sarawagi**, Indian Institute of Technology, Bombay, India, `sunita@iitb.ac.in`; **William W. Cohen**,
Center for Automated Learning & Discovery, Carnegie Mellon University, `wcohen@cs.cmu.edu`.

**★ FINDING AT THE IDENTITY AXIS — THE HELD FILE PRINTS NO VENUE, NO YEAR AND NO COPYRIGHT OR RIGHTS
LINE ON ANY OF ITS EIGHT PAGES AS READ.** The record's own row for this member names **NIPS 2004**.
Nothing on the eight pages confirms or contradicts that: there is no conference line, no proceedings
header, no page-range header, no submission or camera-ready marker, and no copyright statement
anywhere in the file as read. **So the venue and the year in the record's row are NOT established at
this object**, and a reader who wants them established has to go to a source outside the held file.
**Stated at the width of the act: this is a negative over the eight pages as read, not a claim that
the published version carries no such line.**

*What the file's own internal evidence does place it after:* its reference list cites work dated 2004
— **[3]** Bunescu & Mooney, *"Proceedings of the ICML-2004 Workshop on Statistical Relational Learning
(SRL-2004), Banff, Canada, July 2004"*; **[6]** Cohen & Sarawagi, *"Proceedings of the Tenth ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining, 2004"*; **[18]** Sutton, Rohanimanesh
& McCallum, *"ICML, 2004"* — and one item **to appear** in 2005 (**[10]** Kraut, Fussell, Lerch &
Espinosa, *"To appear in the Journal of Organizational Behavior, 2005"*). **That is consistent with a
2004 writing and is not a venue.** It is this read's inference from the reference list and is labeled
as such.

**No licence, copyright or rights line was met on any of the eight pages as read**, so nothing about
redistribution is established either way; nothing was redistributed.

**What the paper is, in its own terms.** It introduces **semi-Markov conditional random fields
(semi-CRFs)** — described in the abstract as *"a conditionally trained version of semi-Markov
chains"* — and gives inference and learning algorithms for them, an argument about their cost and
expressiveness against order-*L* CRFs, and an experimental comparison against two conventional CRF
formulations on five named entity recognition tasks drawn from three corpora. The stated application
throughout is **named entity recognition (NER)** in text; the paper names gene-finding and NP-chunking
as tasks for which *"similar arguments might be made"* and does not run either.

**The abstract's own summary of the contribution,** quoted as printed: *"Intuitively, a semi-CRF on an
input sequence **x** outputs a "segmentation" of **x**, in which labels are assigned to segments
(i.e., subsequences) of **x** rather than to individual elements x_i of **x**. Importantly, features
for semi-CRFs can measure properties of segments, and transitions within a segment can be
non-Markovian. In spite of this additional power, exact learning and inference algorithms for
semi-CRFs are polynomial-time—often only a small constant factor slower than conventional CRFs."*

---

## §2 — The method, as the paper states it

Everything in this section is the paper's, at the page named. Where this read adds anything of its
own it says so at the sentence.

### §2.1 The baseline the paper generalizes, and the two conventional formulations it compares against

**The CRF it starts from** (§2.1, page 2). A CRF models Pr(**y**|**x**) *"using a Markov random field,
with nodes corresponding to elements of the structured object **y**, and potential functions that are
conditional on (features of) **x**"*. Learning sets parameters to maximize the likelihood of a set of
(**x**,**y**) pairs given as training data. For the NER application, **x** is a sequence of words and
**y** a sequence in {*I*,*O*}^|**x**|, where *y_i* = *I* indicates *"word x_i is inside a name"* and
*y_i* = *O* indicates the opposite.

**The local feature functions** (page 2). A vector **f** = ⟨*f*¹,…,*f*^K⟩ of *local feature
functions*, each mapping a pair (**x**,**y**) and an index *i* to a measurement *f^k*(*i*,**x**,**y**)
∈ R; **F**(**x**,**y**) = Σ_i **f**(*i*,**x**,**y**). The paper's own worked example, quoted:
*f*¹³(*i*,**x**,**y**) = ⟦*x_i* is capitalized⟧ · ⟦*y_i* = *I*⟧, so that *F*¹³(**x**,**y**) *"would be
the number of capitalized words x_i paired with the label I"*.

**Equation (1),** the conventional CRF: Pr(**y**|**x**,**W**) = (1/*Z*(**x**)) · *e*^(**W**·**F**(**x**,**y**)),
with *Z*(**x**) = Σ_**y′** *e*^(**W**·**F**(**x**,**y′**)).

**The two conventional formulations used as baselines** (§3.1, page 4). **CRF/1** *"labels words inside
and outside entities with I and O, respectively"*. **CRF/4** *"replaces the I tag with four tags B, E,
C, and U, which depend on where the word appears in an entity"*, cited to **[2]**. The paper does not
say in the text what the four letters stand for; the four-tag family is standard in the NER literature
and this read does not supply an expansion the paper does not print.

### §2.2 The unit the model works on, and where boundaries may fall

**The segmentation** (§2.1, page 2). **s** = ⟨*s*₁,…,*s_p*⟩ denotes a *segmentation* of **x**, where a
*segment* *s_j* = ⟨*t_j*, *u_j*, *y_j*⟩ *"consists of a start position t_j, an end position u_j, and a
label y_j ∈ Y"*. *"Conceptually, a segment means that the tag y_j is given to all x_i's between i =
t_j and i = u_j, inclusive."*

**The four conditions on a valid segmentation, as printed:** *"We assume segments have positive
length, and completely cover the sequence 1…|**x**| without overlapping: that is, that t_j and u_j
always satisfy t₁ = 1, u_p = |**x**|, 1 ≤ t_j ≤ u_j ≤ |**x**|, and t_{j+1} = u_j + 1."*

**The paper's own worked segmentation,** for the sentence *"I went skiing with Fernando Pereira in
British Columbia"*: **s** = ⟨(1,1,*O*),(2,2,*O*),(3,3,*O*),(4,4,*O*),(5,6,*I*),(7,7,*O*),(8,9,*I*)⟩,
corresponding to the label sequence **y** = ⟨*O*,*O*,*O*,*O*,*I*,*I*,*O*,*I*,*I*⟩.

**What this fixes about boundaries, stated as the conditions above state it:** a boundary can fall only
between two adjacent elements of the input sequence, every element belongs to exactly one segment, and
there is no gap and no overlap. **The finest boundary a semi-CRF can express is therefore a boundary of
the element sequence it is given** — this read's restatement of the four conditions, not a separate
claim of the paper's.

### §2.3 The model

**The segment feature functions** (§2.1, page 2). A vector **g** = ⟨*g*¹,…,*g*^K⟩ of *segment feature
functions*, each mapping a triple (*j*,**x**,**s**) to *g^k*(*j*,**x**,**s**) ∈ R, with
**G**(**x**,**s**) = Σ_j^|**s**| **g**(*j*,**x**,**s**).

**The restriction on the features — the paper's analogue of the Markov assumption,** quoted: *"We also
make a restriction on the features, analogous to the usual Markovian assumption made in CRFs, and
assume that every component g^k of **g** is a function only of **x**, s_j, and the label y_{j−1}
associated with the preceding segment s_{j−1}."* **Equation (2)** states it: *g^k*(*j*,**x**,**s**) =
*g*′^k(*y_j*, *y_{j−1}*, **x**, *t_j*, *u_j*). The paper then drops the *g*′ notation and uses *g* for
both versions.

**Equation (3),** the semi-CRF: Pr(**s**|**x**,**W**) = (1/*Z*(**x**)) · *e*^(**W**·**G**(**x**,**s**)),
with *Z*(**x**) = Σ_**s′** *e*^(**W**·**G**(**x**,**s′**)).

**★ The two things that sit together here, and they are the paper's own pairing.** A segment feature
may depend on the whole segment — its extent, its content, arbitrary properties of it — so **within a
segment the model is not restricted to a Markov chain**; between segments the dependence is on the
preceding segment's label alone, which is first-order. The abstract states the same pairing in words:
*"features for semi-CRFs can measure properties of segments, and transitions within a segment can be
non-Markovian."*

### §2.4 Inference

**The problem** (§2.2, page 2): *"given **W** and **x**, find the best segmentation, argmax_**s**
Pr(**s**|**x**,**W**), where Pr(**s**|**x**,**W**) is defined by Equation 3."*

**The reduction** (page 3): argmax_**s** Pr(**s**|**x**,**W**) = argmax_**s** **W**·**G**(**x**,**s**)
= argmax_**s** **W**·Σ_j **g**(*y_j*, *y_{j−1}*, **x**, *t_j*, *u_j*).

**The quantities:** *L* is *"an upper bound on segment length"*; **s**_{*i*:*y*} denotes *"the set of
all partial segmentations starting from 1 (the first index of the sequence) to i, such that the last
segment has the label y and ending position i"*; *V*_{**x**,**g**,**W**}(*i*,*y*) denotes *"the
largest value of **W**·**G**(**x**,**s′**) for any **s′** ∈ **s**_{i:y}"*.

**Equation (4)** — *"the following recursive calculation implements a semi-Markov analog of the usual
Viterbi algorithm"*:

- *V*(*i*,*y*) = max_{*y′*, *d*=1…*L*} [ *V*(*i*−*d*,*y′*) + **W**·**g**(*y*,*y′*,**x**,*i*−*d*+1,*i*) ]  if *i* > 0
- *V*(*i*,*y*) = 0  if *i* = 0
- *V*(*i*,*y*) = −∞  if *i* < 0

*"The best segmentation then corresponds to the path traced by max_y V(|**x**|,y)."*

### §2.5 Learning

**The objective** (§2.4, page 3). Over a training set *T* = {(**x**_ℓ, **s**_ℓ)}_{ℓ=1}^N, and
*"following the notation of Sha and Pereira [16]"*, **Equation (5)**: *L*(**W**) = Σ_ℓ log
Pr(**s**_ℓ|**x**_ℓ,**W**) = Σ_ℓ ( **W**·**G**(**x**_ℓ,**s**_ℓ) − log *Z*_**W**(**x**_ℓ) ).

**Convexity and the optimizer** (page 4), quoted: *"Equation 5 is convex, and can thus be maximized by
gradient ascent, or one of many related methods. (In our implementation we use a limited-memory
quasi-Newton method [13, 14].)"*

**The gradient, Equations (6) and (7):** ∇*L*(**W**) = Σ_ℓ **G**(**x**_ℓ,**s**_ℓ) − [ Σ_**s′**
**G**(**s′**,**x**_ℓ) *e*^(**W**·**G**(**x**_ℓ,**s′**)) ] / *Z*_**W**(**x**_ℓ) = Σ_ℓ
**G**(**x**_ℓ,**s**_ℓ) − *E*_{Pr(**s′**|**W**)} **G**(**x**_ℓ,**s′**).

**The forward recursion** (page 4). α(*i*,*y*) is defined as the value of Σ_{**s′** ∈ **s**_{i:y}}
*e*^(**W**·**G**(**s′**,**x**)), and for *i* > 0:

α(*i*,*y*) = Σ_{*d*=1}^{*L*} Σ_{*y′* ∈ Y} α(*i*−*d*,*y′*) · *e*^(**W**·**g**(*y*,*y′*,**x**,*i*−*d*+1,*i*))

*"with the base cases defined as α(0,y) = 1 and α(i,y) = 0 for i < 0"*, and *Z*_**W**(**x**) = Σ_y
α(|**x**|,*y*).

**The feature-expectation recursion** (page 4). For the *k*-th component of **G**, η^k(*i*,*y*) is the
value of Σ_{**s′** ∈ **s**_{i:y}} *G^k*(**s′**,**x**_ℓ) *e*^(**W**·**G**(**x**_ℓ,**s′**)),
*"restricted to the part of the segmentation ending at position i"*, computed by

η^k(*i*,*y*) = Σ_{*d*=1}^{*L*} Σ_{*y′* ∈ Y} ( η^k(*i*−*d*,*y′*) + α(*i*−*d*,*y′*) ·
*g^k*(*y*,*y′*,**x**,*i*−*d*+1,*i*) ) · *e*^(**W**·**g**(*y*,*y′*,**x**,*i*−*d*+1,*i*))

and finally *E*_{Pr(**s′**|**W**)} *G^k*(**s′**,**x**) = (1/*Z*_**W**(**x**)) Σ_y η^k(|**x**|,*y*).

**The space remark, footnote 2 on page 4,** quoted: *"As in the forward-backward algorithm for chain
CRFs [16], space requirements here can be reduced from ML|Y| to M|Y|, where M is the length of the
sequence, by pre-computing an appropriate set of β values."*

### §2.6 The comparison against order-*L* CRFs — the result the design point carries

All of this is §2.3, page 3.

**On cost,** quoted: *"Since conventional CRFs need not maximize over possible segment lengths d,
inference for semi-CRFs is more expensive. However, Equation 4 shows that the additional cost is only
linear in L. For NER, a reasonable value of L might be four or five.¹ Since in the worst case L ≤
|**x**|, the semi-Markov Viterbi algorithm is always polynomial, even when L is unbounded."* Footnote 1:
*"Assuming that non-entity words are placed in unit-length segments, as we do below."*

**On expressiveness and on the order-*L* CRF's cost,** quoted: *"For fixed L, it can be shown that
semi-CRFs are no more expressive than order-L CRFs. For order-L CRFs, however the additional
computational cost is exponential in L. The difference is that semi-CRFs only consider sequences in
which the same label is assigned to all L positions, rather than all |Y|^L length-L sequences. This is
a useful restriction, as it leads to faster inference."*

**So the linear-versus-exponential result, stated exactly as the paper states it:** the extra cost of
raising the segment-length bound is **linear in *L* for a semi-CRF** and **exponential in *L* for an
order-*L* CRF**, and the reason given is that the semi-CRF ranges over the |Y| uniform label
assignments of a length-*L* window rather than over all |Y|^L assignments. **The expressiveness half —
that for fixed *L* a semi-CRF is no more expressive than an order-*L* CRF — is asserted with the words
*"it can be shown"*, and no proof, derivation or citation for it appears anywhere in the eight pages as
read** (§7.1 carries this as a defect rather than leaving it here).

**The two length features, and the one place the paper draws the Markovian line by construction.**

- **A Gaussian length feature.** With *d_j* the length of a segment and μ *"the average length of all
  segments with label I"*, the segment feature *g*^{k₁}(*j*,**x**,**s**) = (*d_j* − μ)² · ⟦*y_j* = *I*⟧.
  *"After training, the contribution of this feature toward Pr(**s**|**x**) associated with a length-d
  entity will be proportional to e^{w_k·(d−μ)²}—i.e., it allows the learner to model a Gaussian
  distribution of entity lengths."*
- **An exponential length feature, which DOES decompose into local features.** *(★ THE HEADING WAS
  CORRECTED AT THE USER-ORDERED CHECK, §10. FORMER WORDING, PRESERVED (#12): "which is NOT
  non-Markovian" — a double negative where a plain phrase exists, which the writing standards forbid.)* *g*^{k₂}(*j*,**x**,**y**) = *d_j* ·
  ⟦*y_j* = *I*⟧, of which the paper says: *"In contrast to the Gaussian-length feature above, g^{k₂} is
  "equivalent to" a local feature function f(i,**x**,**y**) = ⟦y_i = I⟧, in the following sense: for
  every triple **x**,**y**,**s**, where **y** is the tags for **s**, Σ_j g^{k₂}(j,**x**,**s**) = Σ_i
  f(i,**s**,**y**). Thus a semi-CRF model based on the single feature g^{k₂} could also be represented
  by a conventional CRF."*
- **The general statement, which is the test:** *"In general, a semi-CRF model can be factorized in
  terms of an equivalent order-1 CRF model if and only if the sum of the segment features can be
  rewritten as a sum of local features. Thus the degree to which semi-CRFs are non-Markovian depends on
  the feature set."* **This too is asserted without proof in the eight pages as read.**

---

## §3 — Coupling facts

The commission's form makes these mandatory: what the method assumes of whatever comes before it, what
it hands to whatever comes after it, and the scope it claims for itself. **Every item is at the page
named, and the restatements in this section are marked where they are this read's.**

### §3.1 What it ASSUMES about its upstream

- **A finite input sequence with a total order and an index.** **x** is indexed 1…|**x**| (§2.1, page
  2). In the paper's application the elements are words, obtained by a tokenization the paper does not
  describe anywhere in the eight pages as read.
- **That the element sequence carries every boundary the answer may need.** A segment's endpoints are
  element indices and segments tile the sequence exactly (§2.1's four conditions, page 2), so nothing
  finer than an element boundary is expressible. *(This read's restatement of those conditions.)*
- **A fixed finite label set Y** (§2.1, page 2), with one label per segment. **Nothing in the eight
  pages as read gives a segment more than one label**, and there is no product or joint label
  structure anywhere in the model as printed; the order-*L* experiment does construct a product label
  set, but it does so for the BASELINE, by *"replacing the label set Y with Y^L"* (footnote 5, page 6).
- **An upper bound *L* on segment length, supplied from outside the model.** In the experiments *"a
  fixed value of L was chosen for each dataset based on observed entity lengths"* (§3.3, page 5) — so
  *L* is set by inspecting the data, not fitted by the learner.
- **A convention that puts everything not an entity into unit-length segments.** Footnote 1 (page 3)
  makes this explicit for the cost argument — *"Assuming that non-entity words are placed in
  unit-length segments, as we do below"* — and §3.1 (page 4) states it as what was done: *"we trained
  semi-CRFs to mark entity segments with the label I, and put non-entity words into unit-length
  segments with label O."*
- **Training data as SEGMENTATIONS, not as per-element labels.** The training set is *T* =
  {(**x**_ℓ, **s**_ℓ)} (§2.4, page 3) — each training item carries a segmentation. **A ground truth
  that labels elements without grouping them does not supply what this objective needs**; it would
  have to be converted, and the paper says nothing about such a conversion. *(The reading of what the
  objective needs is this read's; the definition of T is the paper's.)*
- **Feature functions that can be evaluated on an arbitrary (segment, preceding label) pair**,
  including features that are not decomposable over elements — the paper's dictionary distances are
  stated to be exactly that (§3.2, page 5: *"All of the distance metrics are non-Markovian—i.e., the
  distance-based segment features cannot be decomposed into sums of local features."*)

### §3.2 What it HANDS downstream

- **One best segmentation.** The inference problem is defined as *argmax*_**s** (§2.2, page 2), and
  *"the best segmentation then corresponds to the path traced by max_y V(|**x**|,y)"* (page 3). **That
  is the whole of the published output in the eight pages as read.**
- **A label per segment in that segmentation, from Y**, with the segment's own extent (*t_j*, *u_j*) —
  so the extent of the answer is part of the answer rather than an input to it.
- **The model's value for the winning segmentation**, **W**·**G**(**x**,**s**), which the recursion
  computes as **max_y *V*(|**x**|,*y*)** (§2.2, pages 2–3). *(★ CORRECTED AT THE USER-ORDERED CHECK,
  §10. FORMER WORDING, PRESERVED (#12): "computes as *V*(|**x**|,*y*)", which names the best value
  ending in a PARTICULAR label and not the winner; the paper's own sentence takes the maximum over y.)*
- **And what it does NOT hand, which is the half that matters for a design that publishes
  uncertainty.** **No ranked alternatives, no k-best list, no per-segment confidence and no marginal
  probability of a segment or a boundary appears anywhere in the eight pages as read.** The machinery
  from which such quantities are usually taken IS in the paper — the normalizer *Z*_**W**(**x**), the
  forward values α(*i*,*y*), and the feature expectations η^k (§2.4, page 4) — **but it is introduced
  for the gradient and is not published as an output, and the paper does not state a marginal, a
  posterior over segmentations, or a confidence anywhere.** *(Negative stated at the width of the act:
  met nowhere in the eight pages as read.)*

### §3.3 Its own STATED scope and limits

- **The task is information extraction, and the worked task throughout is named entity recognition in
  English text** (§1, page 1; §3, pages 4–6). *"We focus here on named entity recognition (NER), in
  which a segment corresponds to an extracted entity; however, similar arguments might be made for
  several other tasks, such as gene-finding [11] or NP-chunking [16]."* **Gene-finding and NP-chunking
  are named as candidates and neither is run.**
- **The evaluation is F1 over entity segments** (§3.3, page 5, with footnote 3 defining F1 as
  *"2*precision*recall/(precision+recall)"*). **Nothing else is measured in the eight pages as read** —
  no runtime, no memory, no training time, and no measurement of the cost claim of §2.3.
- **The label set in every experiment is small and flat:** {*I*,*O*} for CRF/1 and semi-CRF, and four
  entity-position tags plus *O* for CRF/4 (§3.1, page 4).
- **The order-*L* comparison is bounded by computation, and the bound is stated:** footnote 5, page 6 —
  *"Order-L CRFs were implemented by replacing the label set Y with Y^L. We limited experiments to L ≤
  3 for computational reasons."*
- **The internal-dictionary feature carries a stated precaution against leakage**, §3.2, page 5: *"when
  finding the closest neighbor of **x**_{s_j} in the internal dictionary, we excluded all strings
  formed from **x**, thus excluding matches of **x**_{s_j} to itself (or subsequences of itself)."* The
  paper offers an interpretation of the same feature: *"This feature could be viewed as a sort of
  nearest-neighbor classifier; in this interpretation the semi-CRF is performing a sort of bi-level
  stacking [21]."*
- **The external dictionaries are stated to be weak on their own**, §3.2, page 5: *"Due to variations
  in the way entity names are written, rote matching these dictionaries to the data gives relatively
  low F1 values, ranging from 22% (for the job-title extraction task) to 57% (for the person-name
  task)."*
- **What the paper says it does not deliver, §4, page 7:** models *"strictly more expressive than the
  semi-Markov models described here"* can be had by creating a random variable for each possible
  segment, *"however, for these methods, inference is not tractable, and hence approximations must be
  made in training and classification"*, and whether this paper's extension helps them is left as *"an
  interesting question for future research"*.
- **Nothing in the eight pages as read makes any claim about music, about pitch, or about any
  non-textual sequence.** *(Negative at the width of the act.)*

---

## §4 — Claims, labeled

Each claim is labeled **FACT** (stated or measured in this paper, at the place named), **THEORY**
(established published theory the paper leans on), or **CONJECTURE** (asserted in the paper without
derivation, measurement or citation). **The labels are this read's; the claims are the paper's**, and
the numbering is plain sequence with no scheme behind it.

**Claim 1 — FACT, by construction.** A semi-CRF is the conditional model of Equation 3 over
segmentations, with the segment feature vector **G** in the exponent. (§2.1, page 2.) Nothing turns on
interpretation: the estimator is exhibited.

**Claim 2 — FACT, by construction.** A feature may depend on the whole segment and on the preceding
segment's label only (Equation 2), so the model is non-Markovian *within* a segment and first-order in
the label *between* segments. (§2.1, page 2.)

**Claim 3 — FACT, exhibited.** Exact inference for the best segmentation is the recursion of Equation
4. (§2.2, pages 2–3.)

**Claim 4 — FACT of the printed algorithm, asserted and not measured in this paper.** *"the additional cost is only
linear in L"* (§2.3, page 3). The claim is readable off Equation 4's maximization over *d* = 1…*L*.
**No runtime measurement of any kind appears in the eight pages as read**, so the claim stands as a
property of the recursion and not as a measured one.

**Claim 5 — FACT of the printed algorithm.** *"Since in the worst case L ≤ |**x**|, the semi-Markov
Viterbi algorithm is always polynomial, even when L is unbounded."* (§2.3, page 3.)

**Claim 6 — CONJECTURE at this object.** *"For fixed L, it can be shown that semi-CRFs are no more
expressive than order-L CRFs."* (§2.3, page 3.) **The paper gives no proof, no derivation and no
citation for it on any of the eight pages as read.** It may well be provable and may be proved
elsewhere; what this read establishes is that it is not established *here*. **Two further things about
its shape, both at the page: the claim is an UPPER bound — *no more expressive than* — and the
paper's own concluding sentence states what is bought one notch narrower than the abstract does,
*"offer much of the power of higher-order models without the associated computational cost"* (§5, page
7).** *(★ ADOPTED AT THE CROSS-CHECK, §9.4: the first extract of this row carries both precisions and
this read had neither. The §5 sentence was verified at page 7 by this read before it was written in —
and this read's own Finding 10 records that the same sentence spells *tractable* as *tractible*.)*

**Claim 7 — THEORY, with the paper's own implementation statement beside it.** *"For order-L CRFs,
however the additional computational cost is exponential in L"*, the reason given being that an
order-*L* CRF ranges over all |Y|^L length-*L* label sequences where the semi-CRF ranges only over
those in which one label is assigned throughout (§2.3, page 3). The paper supplies no derivation, but
its own experiment implements order-*L* CRFs *"by replacing the label set Y with Y^L"* (footnote 5,
page 6), which is the construction the exponential count follows from. **The pairing of Claim 4 with
Claim 7 is the linear-versus-exponential result the record's own row for this member names.**

**Claim 8 — CONJECTURE at this object.** *"In general, a semi-CRF model can be factorized in terms of
an equivalent order-1 CRF model if and only if the sum of the segment features can be rewritten as a
sum of local features."* (§2.3, page 3.) Asserted with no proof; the paper does exhibit one instance of
each direction's easy case (the Gaussian-length feature, which is not so rewritable, and the
exponential-length feature, which is).

**Claim 9 — THEORY, asserted without citation.** *"Equation 5 is convex"* (§2.4, page 4). The
convexity of the conditional log-likelihood of a log-linear model is standard published theory; **this
paper states it and cites nothing for it.**

**Claim 10 — FACT, measured.** *"In the baseline configuration in which no dictionary features are
used, semi-CRFs perform best on all five of the tasks."* (§3.3, page 6.) **Checked against Table 1 by
this read and it holds on all five** (§6).

**Claim 11 — FACT, measured.** With internal-dictionary features, semi-CRF performance *"is often
improved, and never degraded by more than 2.5%"* (§3.3, page 6). **Checked: it holds, and the true
worst case in Table 1 is a loss of 0.8%** (§6) — so the stated bound is loose rather than wrong.

**Claim 12 — FACT, measured.** *"Semi-CRFs perform best on nine of the ten task variants for which
internal dictionaries were used."* (§3.3, page 6.) **Checked: exactly nine of ten, and the single
exception is identifiable** — Address\_State with internal dictionary features only, where CRF/1's
44.5 beats the semi-CRF's 35.5 (§6).

**Claim 13 — FACT, measured.** *"The external-dictionary features are helpful to all the
algorithms."* (§3.3, page 6.) **Checked: every one of the fifteen external-dictionary changes relative
to baseline in Table 1 is positive** (§6).

**Claim 14 — FACT, measured.** *"Semi-CRFs performs best on three of five tasks in which only external
dictionaries were used."* (§3.3, page 6.) **Checked: exactly three — title, person and city — with
CRF/1 best on state and CRF/4 best on company** (§6).

**Claim 15 — MEASURED CLAIM THIS READ COULD NOT REPRODUCE FROM THE PAPER'S OWN TABLE.** *"If we
consider the tasks with and without external dictionary features as separate "conditions", then
semi-CRFs using all available information⁴ outperform both CRF variants on eight of ten
"conditions"."* (§3.3, page 6, with footnote 4 defining *all available information* as *"the
both-dictionary version when external dictionaries are available, and the internal-dictionary only
version otherwise"*.) **Under the two readings of that sentence this read can construct, Table 1 gives
nine of ten and seven of ten respectively — neither is eight.** The computation, both ways and cell by
cell, is at §6, and the finding is at §7.1.

**Claim 16 — FACT, measured.** *"For these tasks, the performance of CRF/4 and CRF/1 does not seem to
improve much by simply increasing order."* (§3.3, page 6, of Table 2.) **Checked at Table 2's own
cells** (§6): over *L* = 1, 2, 3 the largest movement on any one of the six learner-and-task
combinations is **3.9 points** — CRF/1 on Email\_persons, 67.6 down to 63.7 and back up to 66.7 — and
the direction of movement differs across the six, named rather than counted: CRF/1 falls on
Address\_State and rises on Address\_City; CRF/4 rises then holds on Address\_State, rises then falls
on Address\_City, and falls on Email\_persons.
**The paper's word is *"much"*, which it does not quantify, so the claim is checked for what it asserts
and not graded against a bar the paper never set.**

*(★ THIS ENTRY CARRIED A WRONG COUNT WHEN IT WAS FIRST WRITTEN AND IT IS CORRECTED HERE, IN THE ACT
THAT DERIVED THE VALUE. FORMER WORDING, PRESERVED (#12): "the movement is within 1.9 points on every
one of the six baseline-and-task combinations". **That number was put on this read's own reading of
the table before the ranges were computed, and computing them refutes it** — the Email\_persons row
alone moves 3.9. It is reported as an instance of the user's first named degradation tell at §8.3, not
filed as an ordinary slip. The phrase *"baseline-and-task"* was wrong as well: the six combinations are
the two CRF formulations across the three tasks.)*

**Claim 17 — FACT asserted, with no value in this paper.** *"However, semi-CRFs perform somewhat
better, on average, than our perceptron-based learning algorithm."* (§4, page 7, of the authors' own
earlier work **[6]**.) **No number, no table and no test supports this anywhere in the eight pages as
read** — the comparison is stated and its evidence is not carried here.

**Claim 18 — CONJECTURE, a judgment the paper states without evidence.** *"Probabilistically-grounded
approaches like CRFs also are preferable to margin-based approaches like the voted perceptron in
certain settings, e.g., when it is necessary to estimate confidences in a classification."* (§4, page
7.)

**Claim 19 — CONJECTURE, offered as an interpretation.** That the internal-dictionary feature makes the
semi-CRF *"a sort of nearest-neighbor classifier"* performing *"a sort of bi-level stacking"* (§3.2,
page 5). The paper's own hedging is in the quoted words.

**Claim 20 — FACT, asserted by construction.** *"All of the distance metrics are non-Markovian—i.e.,
the distance-based segment features cannot be decomposed into sums of local features."* (§3.2, page 5.)

**Claim 21 — THEORY, a related-work characterization.** *"Semi-CRFs are similar to nested HMMs [1],
which can also be trained discriminatively [17]. The primary difference is that the "inner model" for
semi-CRFs is of short, uniformly-labeled segments with non-Markovian properties, while nested HMMs
allow longer, diversely-labeled, Markovian "segments"."* (§4, page 7.)

**Claim 22 — MEASURED CLAIM REFUTED BY THE PAPER'S OWN TABLE.** Figure 1's caption, page 6: *"We do
not use internal dictionary features for CRF/4 since they lead to reduced accuracy."* **Table 1's CRF/4
internal-dictionary row for Address\_State rises from 15.0 to 25.4, a change of +69.3% — an
improvement, on the very task the figure's leftmost panel shows.** The finding is at §7.1.

---

## §5 — Measured results, with corpus, measure and value as the paper states them

### §5.1 The three corpora and the five tasks

All of §3.1, page 4, quoted or transcribed:

- **Address** — *"contains 4,226 words, and consists of 395 home addresses of students in a major
  university in India"*, cited **[1]**. Tasks: *"extraction of city names and state names"*.
- **Jobs** — *"contains 73,330 words, and consists of 300 computer-related job postings"*, cited
  **[4]**. Tasks: *"extraction of company names and job titles"*.
- **Email** — *"The 18,121-word Email corpus contains 216 email messages taken from the CSPACE email
  corpus [10], which is mail associated with a 14-week, 277-person management game."* Task:
  *"extraction of person names"*.

**Five tasks over three corpora**, which is what the text's *"five NER problems, associated with three
different corpora"* states. **Table 1 names its five rows *state*, *title*, *person*, *city* and
*company* and does NOT say which corpus each belongs to**; the pairing has to be recovered from §3.1.
Table 2 does carry corpus-prefixed labels for the three tasks it covers.

### §5.2 The measure, and what it is measured over

**F1 over entity segments.** §3.3, page 5: *"We evaluated F1-measure performance³ of CRF/1, CRF/4, and
semi-CRFs, with and without internal and external dictionaries."* Footnote 3: *"F1 is defined as
2*precision*recall/(precision+recall)."* Figure 1's own vertical axis is labeled *F1 span accuracy*;
the body text calls the same quantity *F1* without that word. *(No sweep for the word was run, so
nothing is claimed about where else it occurs.)*

**Nothing else is measured.** No runtime, no memory use, no training time, no significance test and no
dispersion of any kind appears in the eight pages as read.

### §5.3 The protocol, as the paper states it

Every clause here is §3.3, page 5, quoted: *"In each experiment performance was averaged over seven
runs, and evaluation was performed on a hold-out set of 30% of the documents. In the table the learners
are trained with 10% of the available data—as the curves show, performance differences are often
smaller with more training data. Gaussian priors were used for all algorithms, and for semi-CRFs, a
fixed value of L was chosen for each dataset based on observed entity lengths. This ranged between 4
and 6 for the different datasets."*

**Four things the protocol does not state, and they bear on how the values may be cited.** *(Negatives
at the width of the act: met nowhere in the eight pages as read.)*

1. **What varies between the seven runs is never said** — whether it is the train/hold-out split, an
   initialization, or something else. So *"averaged over seven runs"* cannot be read as a bound of any
   particular kind.
2. **No spread is reported for any averaged value** — no standard deviation, no range, no
   uncertainty range, nowhere in either table or in the figure.
3. **The Gaussian prior's strength is not given**, for any algorithm.
4. **The per-dataset value of *L* is not given** — only that it *"ranged between 4 and 6"*. Which
   dataset got which value is not stated, so no result in Table 1 or Table 2 can be tied to a
   particular *L*.

### §5.4 Table 1, transcribed

**Caption, quoted as printed:** *"Table 1: Comparing various methods on five IE tasks, with and without
dictionary features. The column Δbase is percentage change in F1 values relative to the baseline. The
column Δextern is is change relative to using only external-dictionary features."* (The doubled *"is
is"* is the paper's; it is quoted as printed.)

Values as printed, and **the paper's own bold marks are carried as bold here**. *Δbase* and *Δextern*
are the paper's columns, not this read's arithmetic. *(★ CORRECTED AT THE USER-ORDERED CHECK, §10.
FORMER WORDING, PRESERVED (#12): "with the paper's own bold marks recorded in the last column of each
block rather than typographically" — **a sentence left over from an arrangement this file does not
use**, and false of the tables directly beneath it.)*

**CRF/1**

| task | baseline F1 | +internal dict F1 | Δbase | +external dict F1 | Δbase | +both F1 | Δbase | Δextern |
|---|---|---|---|---|---|---|---|---|
| state | 20.8 | **44.5** | 113.9 | **69.2** | 232.7 | 55.2 | 165.4 | −67.3 |
| title | 28.5 | 3.8 | −86.7 | 38.6 | 35.4 | 19.9 | −30.2 | −65.6 |
| person | 67.6 | 48.0 | −29.0 | 81.4 | 20.4 | 64.7 | −4.3 | −24.7 |
| city | 70.3 | 60.0 | −14.7 | 80.4 | 14.4 | 69.8 | −0.7 | −15.1 |
| company | 51.4 | 16.5 | −67.9 | 55.3 | 7.6 | 15.6 | −69.6 | −77.2 |

**CRF/4**

| task | baseline F1 | +internal dict F1 | Δbase | +external dict F1 | Δbase | +both F1 | Δbase | Δextern |
|---|---|---|---|---|---|---|---|---|
| state | 15.0 | 25.4 | 69.3 | 46.8 | 212.0 | 43.1 | 187.3 | −24.7 |
| title | 23.7 | 7.9 | −66.7 | 36.4 | 53.6 | 14.6 | −38.4 | −92.0 |
| person | 70.9 | 64.5 | −9.0 | 82.5 | 16.4 | 74.8 | 5.5 | −10.9 |
| city | 73.2 | 70.6 | −3.6 | 80.8 | 10.4 | 76.3 | 4.2 | −6.1 |
| company | 54.8 | 20.6 | −62.4 | **61.2** | 11.7 | 25.1 | −54.2 | −65.9 |

**semi-CRF**

| task | baseline F1 | +internal dict F1 | Δbase | +external dict F1 | Δbase | +both F1 | Δbase | Δextern |
|---|---|---|---|---|---|---|---|---|
| state | **25.6** | 35.5 | 38.7 | 62.7 | 144.9 | **65.2** | 154.7 | 9.8 |
| title | **33.8** | **37.5** | 10.9 | **41.1** | 21.5 | **40.2** | 18.9 | −2.5 |
| person | **72.2** | **74.8** | 3.6 | **82.8** | 14.7 | **83.7** | 15.9 | 1.2 |
| city | **75.9** | **75.3** | −0.8 | **84.0** | 10.7 | **83.6** | 10.1 | −0.5 |
| company | **60.2** | **59.7** | −0.8 | 60.9 | 1.2 | **60.9** | 1.2 | 0.0 |

**The bold marks are the paper's and this read takes them to mark the best value in their column
block** — a reading, not a printed statement, and it was checked at all twenty cells of the four
F1 columns: in each of the four blocks the bolded value in each task row is the largest of the three
learners' values for that task, and no Δ cell carries a bold mark.

### §5.5 Table 2, transcribed

**Caption, quoted:** *"Table 2: F1 values for different order CRFs"*.

| task | CRF/1 L=1 | CRF/1 L=2 | CRF/1 L=3 | CRF/4 L=1 | CRF/4 L=2 | CRF/4 L=3 | semi-CRF |
|---|---|---|---|---|---|---|---|
| Address\_State | 20.8 | 20.1 | 19.2 | 15.0 | 16.4 | 16.4 | **25.6** |
| Address\_City | 70.3 | 71.0 | 71.2 | 73.2 | 73.9 | 73.7 | **75.9** |
| Email\_persons | 67.6 | 63.7 | 66.7 | 70.9 | 70.7 | 70.4 | **72.2** |

**Two things about this table that the paper does not state and this read establishes at the cells
(§6).** First, **Table 2 covers three of the five tasks** — the two Jobs tasks, *title* and *company*,
are absent, and no reason is given for the subset (footnote 5's *"computational reasons"* is given for
the bound *L* ≤ 3, not for the choice of tasks). Second, **every value in Table 2's *L* = 1 columns and
in its semi-CRF column equals the corresponding baseline cell of Table 1 exactly**, which places the
whole of Table 2 in the no-dictionary configuration — a condition stated neither in Table 2's caption
nor in the paragraph that introduces it.

### §5.6 Figure 1, and what is legible in it

**Caption, quoted:** *"Figure 1: F1 as a function of training set size. Algorithms marked with "+dict"
include external dictionary features, and algorithms marked with "+int" include internal dictionary
features. We do not use internal dictionary features for CRF/4 since they lead to reduced accuracy."*

**What the panels are:** three panels, titled *Address\_State*, *Address\_City* and *Email\_Person*.
The horizontal axis is *Fraction of available training data*, ticked from 0.05 to 0.5 on all three; the
vertical axis is *F1 span accuracy*, **and its range differs between panels** — the *Address\_State*
panel runs from 10 to 100 while the other two run from 65 to 90, so the three panels are not visually
comparable and a reader must take the tick labels rather than the curve heights. **Four series are in
the legend of each panel:** *CRF/4*, *SemiCRF*, *CRF/4+dict*, *SemiCRF+int+dict*. **CRF/1 does not
appear in the figure at all.**

**★ ONE ARITHMETIC ADDENDUM ON THIS SECTION IS AT §6** — the Δextern column's denominator, which the
caption's wording does not identify.

**No value is transcribed from Figure 1 by this read.** The curves are plotted without printed values
and without error bars; reading a value off them would be this read's estimate and not the paper's
statement. **The one thing taken from the figure is the composition just described** — three tasks,
four series, differing axis ranges, no error bars — and the caption's claim, which Claim 22 records as
refuted by Table 1.

---

## §6 — Arithmetic this read performed on the paper's own printed values

**Everything in this section is this read's arithmetic over values transcribed at §5.** No value here
is the paper's statement; where a computation reproduces a printed value, that is said.

### §6.1 The Δbase column reproduces at every cell, two of them only within rounding

**The rule that reproduces the column is (value − baseline) / baseline, as a percentage.** All
forty-five Δbase cells of Table 1 were computed. **Forty-three reproduce the printed value exactly at
one decimal.** The two that do not are off by one step of that decimal and are explained by the F1
values themselves being printed to one decimal: the semi-CRF *title* row's external-dictionary cell
computes 21.6 where 21.5 is printed, and CRF/1's *company* row's both-dictionaries cell computes
−69.65, which prints either way. **So the column is internally consistent and no cell of it is
wrong.**

### §6.2 ★ The Δextern column's denominator is the BASELINE, which the caption does not say

The caption reads *"The column Δextern is is change relative to using only external-dictionary
features."* **A reader takes *relative to* as naming the denominator**, and computes (both − extern) /
extern. **That reading reproduces no cell in the table.** On CRF/1's *state* row it gives
(55.2 − 69.2)/69.2 = −20.2%, against the printed −67.3.

**The rule that does reproduce the column is (both − extern) / BASELINE:** (55.2 − 69.2)/20.8 =
−67.3%. Computed on all fifteen cells, **fourteen reproduce the printed value exactly** — CRF/1
−67.3, −65.6, −24.7, −15.1, −77.2; CRF/4 −24.7, −92.0, −10.9, −6.1, −65.9; semi-CRF 9.8, 1.2, −0.5,
0.0 — **and the fifteenth, semi-CRF *title*, computes −2.7 against a printed −2.5, which the
one-decimal rounding of 40.2 and 41.1 accounts for** (an unrounded difference near −0.85 gives −2.5).

**So both Δ columns are percentages OF THE BASELINE**, and the caption says so of the first and not of
the second. A reader who takes the caption at its word will read the Δextern column as some 3.3 times
smaller than it is on the CRF/1 *state* row. The finding is at §7.1.

### §6.3 The paper's five reproducible summary claims, checked cell by cell

- **Claim 10 (best on all five in the baseline configuration): HOLDS.** state 25.6 > 20.8, 15.0;
  title 33.8 > 28.5, 23.7; person 72.2 > 70.9, 67.6; city 75.9 > 73.2, 70.3; company 60.2 > 54.8, 51.4.
- **Claim 11 (with internal dictionaries, semi-CRF never degraded by more than 2.5%): HOLDS, and the
  bound is loose.** The semi-CRF's internal-dictionary Δbase values are +38.7, +10.9, +3.6, −0.8 and
  −0.8, so the worst degradation in the table is 0.8%.
- **Claim 12 (best on nine of the ten task variants for which internal dictionaries were used):
  HOLDS EXACTLY, and the exception is identifiable.** The ten variants are the five
  internal-dictionary cells and the five both-dictionaries cells. The semi-CRF is the largest of the
  three learners in nine of them; **the single exception is Address\_State with internal dictionary
  features only, where CRF/1's 44.5 beats the semi-CRF's 35.5.**
- **Claim 13 (external-dictionary features helpful to all the algorithms): HOLDS.** All fifteen
  external-dictionary Δbase values are positive — CRF/1 +232.7, +35.4, +20.4, +14.4, +7.6; CRF/4
  +212.0, +53.6, +16.4, +10.4, +11.7; semi-CRF +144.9, +21.5, +14.7, +10.7, +1.2.
- **Claim 14 (best on three of five tasks with only external dictionaries): HOLDS EXACTLY.** The
  semi-CRF is largest on title (41.1), person (82.8) and city (84.0); **CRF/1 is largest on state
  (69.2) and CRF/4 on company (61.2)** — the two cells the paper's own bold marks single out.

### §6.4 ★ Claim 15's *"eight of ten conditions"* is not reproducible from Table 1

The sentence is *"If we consider the tasks with and without external dictionary features as separate
"conditions", then semi-CRFs using all available information outperform both CRF variants on eight of
ten "conditions""*, with footnote 4 fixing *all available information* as the both-dictionary version
where external dictionaries are available and the internal-dictionary-only version otherwise. **Ten
conditions = five tasks × two conditions.** This read can construct two readings of what the CRF
variants are then compared at, and computed both.

**Reading A — each learner in the same column.** Without external dictionaries the comparison is in
the internal-dictionary column; with them, in the both-dictionaries column.

| condition | semi-CRF | CRF/1 | CRF/4 | semi-CRF wins? |
|---|---|---|---|---|
| state, no external | 35.5 | 44.5 | 25.4 | **no** |
| title, no external | 37.5 | 3.8 | 7.9 | yes |
| person, no external | 74.8 | 48.0 | 64.5 | yes |
| city, no external | 75.3 | 60.0 | 70.6 | yes |
| company, no external | 59.7 | 16.5 | 20.6 | yes |
| state, with external | 65.2 | 55.2 | 43.1 | yes |
| title, with external | 40.2 | 19.9 | 14.6 | yes |
| person, with external | 83.7 | 64.7 | 74.8 | yes |
| city, with external | 83.6 | 69.8 | 76.3 | yes |
| company, with external | 60.9 | 15.6 | 25.1 | yes |

**Nine of ten, the one loss being Address\_State without external dictionaries.**

**Reading B — each learner at its own best available configuration in that condition.** Without
external dictionaries each learner takes the better of its baseline and its internal-dictionary cell;
with them, the better of its external-dictionary and its both-dictionaries cell.

| condition | semi-CRF best | CRF/1 best | CRF/4 best | semi-CRF wins? |
|---|---|---|---|---|
| state, no external | 35.5 | 44.5 | 25.4 | **no** |
| title, no external | 37.5 | 28.5 | 23.7 | yes |
| person, no external | 74.8 | 67.6 | 70.9 | yes |
| city, no external | 75.9 | 70.3 | 73.2 | yes |
| company, no external | 60.2 | 51.4 | 54.8 | yes |
| state, with external | 65.2 | 69.2 | 46.8 | **no** |
| title, with external | 41.1 | 38.6 | 36.4 | yes |
| person, with external | 83.7 | 81.4 | 82.5 | yes |
| city, with external | 84.0 | 80.4 | 80.8 | yes |
| company, with external | 60.9 | 55.3 | 61.2 | **no** |

**Seven of ten.**

**So the printed *eight of ten* matches neither reading — one gives nine and the other seven.** *(Bound
on this finding: it is a negative over the two readings this read could construct from the sentence and
its footnote. A rule that yields eight may exist and be unrecoverable from the text as printed; what is
established is that the sentence as printed does not let a reader reproduce its own count.)*

**★ AND READING A's TEN COMPARISONS ARE THE SAME TEN CELLS AS CLAIM 12's, WHICH THE PAPER PUTS AT
NINE.** Claim 12's *"ten task variants for which internal dictionaries were used"* are exactly the
internal-dictionary and both-dictionaries columns, and *"perform best"* is the same test as
*"outperform both CRF variants"*. **So on reading A the paper states nine of ten and eight of ten
about one set of comparisons, two sentences apart — and the nine is the one that checks out.**

### §6.5 Table 2's L = 1 and semi-CRF columns reproduce Table 1's baseline exactly

CRF/1: 20.8, 70.3, 67.6 at *L* = 1 against Table 1's baseline 20.8 (state), 70.3 (city), 67.6
(person). CRF/4: 15.0, 73.2, 70.9 against 15.0, 73.2, 70.9. semi-CRF: 25.6, 75.9, 72.2 against 25.6,
75.9, 72.2. **All nine agree digit for digit, which places Table 2 in the no-dictionary configuration
— a condition stated neither in Table 2's caption nor in the paragraph that introduces it.**

**And the semi-CRF beats every order-*L* value in Table 2**, on all three tasks and at every *L*: 25.6
against a best CRF value of 20.8, 75.9 against 73.9, 72.2 against 70.9.

### §6.6 The cost of Equation 4, counted — this read's derivation, not the paper's

Equation 4 computes one value for each position *i* ∈ 1…|**x**| and each label *y* ∈ Y, and each is a
maximum over *y′* ∈ Y and *d* ∈ 1…*L*. **So the count of segment-feature evaluations is |**x**| · |Y| ·
|Y| · *L***, that is, time linear in the sequence length, linear in *L*, and quadratic in the label
set. The paper states neither this product nor any complexity expression; **it states only that the
additional cost is *"linear in L"*, which is what the *d* = 1…*L* maximization gives, and footnote 2
gives the space reduction from *ML*|Y| to *M*|Y|.** **An order-*L* CRF over the label set Y^L has
|Y|^L states and a transition table of |Y|^{2L} entries, which is the exponential growth the paper
asserts** — also this read's count, from the paper's own stated implementation of *"replacing the
label set Y with Y^L"*.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Inconsistencies and defects inside the paper

**Finding 1 — the held file carries no venue, no year and no rights line on any of its eight pages as
read**, while the record's row names NIPS 2004. Stated at §1, and it is the only identity-axis finding
of this read.

**Finding 2 — the summary claim *"eight of ten conditions"* cannot be reproduced from the paper's own
Table 1, and on the reading that makes its comparison set explicit it contradicts the paper's own
count of nine two sentences earlier.** Both computations are at §6.4. **It is the only finding of this
read that bears on a COUNT the paper reports** — Finding 4 below bears on how fifteen reported values
are to be read, which is a different thing. It does not move any transcribed value: every cell of
Table 1 is transcribed as printed and was checked twice against the page, and the two verifiable
counts around it — nine of ten, three of five — check out exactly.

**Finding 3 — Figure 1's caption gives a blanket reason that the paper's own Table 1 refutes on the
task the figure's leftmost panel shows.** The caption: *"We do not use internal dictionary features
for CRF/4 since they lead to reduced accuracy."* Table 1's CRF/4 internal-dictionary cells move
−66.7%, −9.0%, −3.6% and −62.4% on title, person, city and company — **and +69.3% on state**, from 15.0
to 25.4. The body text is properly hedged where the caption is not: *"the less-natural local version of
these features **often** leads to substantial performance losses for CRF/1 and CRF/4"*. **The same
exception holds for CRF/1, whose state cell rises from 20.8 to 44.5 (+113.9%) with internal dictionary
features** — the single cell where the semi-CRF is beaten in Claim 12's ten, so the exception is
load-bearing twice over.

**Finding 4 — the Δextern column's denominator is the baseline and the caption names something else**
(§6.2). **On the row where the two readings diverge most — CRF/1's *state* row — they differ by a
factor of 3.3**, which is the ratio of that row's external-dictionary value to its baseline (69.2
against 20.8); that ratio is what the two candidate denominators differ by, row for row.

**Finding 5 — Table 1 does not say which corpus each of its five task rows belongs to**, while Table 2
does for the three it covers. A reader must carry the pairing from §3.1's prose.

**Finding 6 — the order-*L* comparison runs on three of the five tasks and no reason is given for the
subset.** The two omitted tasks, *title* and *company*, are the two from the largest corpus (Jobs,
73,330 words). Footnote 5's *"computational reasons"* is given for the bound *L* ≤ 3, not for the choice
of tasks. **Since this comparison is the paper's only empirical support for preferring a semi-CRF to a
higher-order CRF, its population matters.**

**Finding 7 — two of the paper's structural claims are asserted without proof, derivation or
citation**: that for fixed *L* a semi-CRF is no more expressive than an order-*L* CRF (*"it can be
shown"*), and the if-and-only-if condition for a semi-CRF to factorize into an order-1 CRF (Claims 6
and 8). **Both are load-bearing for the paper's own argument about when a semi-CRF buys anything.**

**Finding 8 — the abstract makes a runtime claim the paper does not measure.** *"exact learning and
inference algorithms for semi-CRFs are polynomial-time—often only a small constant factor slower than
conventional CRFs"*. **No runtime, no training time and no memory measurement appears anywhere in the
eight pages as read.** On the count at §6.6 the extra factor over a first-order CRF is *L* itself, and
*L* was 4 to 6 in the experiments — so *"a small constant factor"* is a statement about *L* being
small, and is not a measured comparison of two implementations.

**Finding 9 — four notational slips, each read at its own line.**

- *g*^{k₂}(*j*,**x**,**y**) is written with **y** as its third argument (§2.3, page 3) where §2.1
  defines every segment feature function on a triple (*j*,**x**,**s**).
- In the same paragraph the equivalence is printed as Σ_j *g*^{k₂}(*j*,**x**,**s**) = Σ_i
  *f*(*i*,**s**,**y**), where the local feature function was defined two pages earlier as
  *f*(*i*,**x**,**y**) — **s** stands where **x** belongs.
- Both dictionary features are defined with *argmax* and then described as distances: *g*^{D,sim}(*j*,**x**,**s**)
  = *argmax*_{*u*∈D} *sim*(**x**_{s_j}, *u*), glossed *"i.e., the distance from the word sequence
  **x**_{s_j} to the closest element in D"* (§3.2, page 5). **An *argmax* over a similarity returns the
  nearest element, not a distance to it**; the same form recurs for the local version
  *f*^{D,sim}(*i*,**x**,**y**).
- Footnote 2 (page 4) uses *M* for the length of the sequence, which the body writes |**x**|
  throughout.

**Finding 10 — printed language defects, named rather than counted.** Table 1's caption reads *"The
column Δextern is is change relative to"*; page 4 reads *"However, to compute the the normalizer"*; §4
reads *"whether the tractible extension to CRF inference considered here can can be used"*; **the word *tractable* is spelled *tractible* twice — in §4 and in
§5's first sentence — and correctly once, in §4's *"inference is not tractable"***; §4 carries a space
before a closing parenthesis, *"compute a partition function. )"*; §3.2 reads *"For instance, city names
in the Address data, we used a web page listing cities in India"*; §3.3 reads *"A detailed tabulation of
the results are shown in Table 1"*; and reference **[13]** names the journal *"Mathematic
Programming"*, and reference **[1]** reads *"Santa Barabara,USA"*. **The same task is named three ways
across the paper** — *person* in Table 1, *Email\_persons* in Table 2, *Email\_Person* in Figure 1.
*(The reference list runs [1] to [21]; two of its items are named here and no sweep of the other
nineteen for language defects was run.)*

**Finding 11 — a precision rather than a defect: the suggested *L* and the used *L* are not the same
range.** §2.3 says *"For NER, a reasonable value of L might be four or five"*; §3.3 says the fixed
value *"ranged between 4 and 6 for the different datasets"*. The two sentences are about different
things — one about NER in general, one about these datasets — so this is not a contradiction, but a
reader taking *"four or five"* as the paper's own operating range would be wrong about its own
experiments.

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered

*Every item is a negative at the width of the act: met nowhere in the eight pages as read.*

1. **No dispersion of any kind on any reported value** — no standard deviation, no range, no
   uncertainty range, no significance test, in either table or the figure, although every value is an
   average over seven runs.
2. **What varies between the seven runs is not stated.**
3. **No runtime, training-time or memory measurement**, which is what Finding 8 turns on.
4. **The per-dataset value of *L* is not given**, only that it ranged between 4 and 6.
5. **Where the *"observed entity lengths"* that set *L* were observed is not stated** — training
   portion, whole corpus, or the hold-out included. **The paper therefore does not exclude a path by
   which a quantity of the evaluation data entered a model constant.**
6. **The strength of the Gaussian priors is not given, for any algorithm.**
7. **The tokenization that produces **x** is never described.**
8. **The expansion of CRF/4's four tags B, E, C, U is not stated** — only cited to **[2]**.
9. **How the internal segment dictionary is maintained during training is not stated** — it is built
   *"on the fly"* from segments labeled as entities in the training data, and whether it is rebuilt per
   iteration, per fold or once is not said.
10. **No tie-break rule for Equation 4's maximization is stated**, so two segmentations of equal value
    have no declared winner.
11. **No marginal, posterior, k-best list or per-segment confidence is defined or published** (§3.2).
12. **The comparison against the authors' earlier perceptron-based semi-Markov learner carries no
    value** (Claim 17).

### §7.3 What is both measured and structural here, for a design that would adopt this formalism

**THE BOUND ON THIS WHOLE SUBSECTION, STATED FIRST.** This side opened **no** object of this
project's record for this paper — not `FRAMEWORK.md`, not the findings surface, not the slice
derivation, not the bibliography row, and no design point at its own text. **So nothing here is a
claim about what the record says of this paper, and nothing here routes a finding to a design point.**
The only statements of this project that this side read at an object are `DECISIONS.md`'s INDEX lines
— one line per decision, not the entries — and row 11's own line of `reading_pass/candidacy_upgrades.md`.
Each is named where it is used, and **an index line is a one-sentence summary of a decision whose full
entry this side did not open.**

**(a) The linear-versus-exponential result is exhibited and not merely asserted, but only on the cost
half.** Equation 4's maximization over *d* = 1…*L* is the linear-in-*L* half, and it is on the page.
The exponential half follows from the order-*L* construction the paper states for its own experiment
(*"replacing the label set Y with Y^L"*). **What is NOT established at this object is the
expressiveness half** — that for fixed *L* nothing is lost by taking the semi-Markov restriction
(Claim 6, Finding 7). A design that adopts the formalism *because* it buys the same reach at lower cost
is resting on the unproven half, and the proof is not in this paper.

**(b) One label per segment, and what a joint label would cost in this formalism.** The model as
printed assigns one label from one set Y per segment (§2.1). **A design whose segment label is a
compound — a tonality together with a chord identity, say — either forms the product label set, which
is exactly the construction the paper measures the cost of and calls exponential, or carries the
compound some other way that this paper does not supply.** *(This is this read's inference from the
model as printed, and it is the one structural consequence of the formalism this read would put in
front of a design decision.)*

**(c) The formalism supplies a decision, and not an uncertainty surface.** Its published output is one
best segmentation (§3.2). `DECISIONS.md`'s index lines record, among this project's standing decisions,
**D-006** — *"The published uncertainty surface is two full candidate lists, with no truncation"* —
**D-027** — *"Every layer emits ranked candidates plus a confidence, never a forced point estimate"* —
and **D-331** — *"Every chord decision carries its ranked alternatives and its confidence — committed,
inherited, and abstained alike, never pruned"*. **So an adoption of this formalism owes a construction
this paper does not carry.** The pieces a construction would be built from are in the paper — the
normalizer, the forward values, the feature expectations — but the paper defines them for the gradient
and states no marginal. *(What each of those three decisions requires in detail was not read: only the
index line.)*

**(d) The tie question is live and the paper is silent on it.** `DECISIONS.md`'s index line for
**D-565** reads *"Exact score ties in the decode are real and are broken by a declared TOTAL ORDER on
paths, implemented identically in every decoder — no epsilon, no platform dependence"*. **Equation 4 is
a maximum with no stated tie-break** (§7.2, item 10), so an adoption owes the tie-break rule from its
own side.

**(e) The segment-length bound is an input, not a fitted quantity, and where it comes from is exactly
what this paper leaves unstated.** `DECISIONS.md`'s index line for **D-004** is *"The decode state
space and the segment cap"* — this project already has a cap of its own, whose value this side did not
open. **What this read adds is the caution, not the parallel:** this paper sets *L* from observed entity
lengths without saying which data were observed (§7.2, item 5), and this project's own standing rule at
principle #20 is that every fit event declares its held-out data and its capacity budget before
fitting. **A design that takes *L* from the data owes that declaration; the paper is not a precedent
for skipping it.**

**(f) What the formalism assumes of the ground truth.** Training items are (sequence, segmentation)
pairs (§2.4). **A design adopting it needs ground truth that groups elements and not only labels
them.** Whether this project's ground truth does so was **not checked by this side** — no corpus, no
annotation file and no measurement tool was opened — so this is stated as a requirement of the
formalism and not as a finding about our data.

**(g) The one feature-design consequence that is the paper's own test.** Claim 8's condition — that a
semi-CRF collapses into an order-1 CRF exactly when the segment features can be rewritten as a sum of
local features — **is the test of whether a segmental design buys anything at all.** The paper's own
worked pair shows both sides of it: a squared-deviation length feature that does not so decompose, and
a plain length feature that does. **A design that adopts segments while using only decomposable
features has taken the cost of *L* and none of the reach** — the paper's own words being that *"the
degree to which semi-CRFs are non-Markovian depends on the feature set"*.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

**Every one of the eight pages was re-opened after §1 to §7 had been written**, in four requests, in
this order: page 3 (the equations and the cost-and-expressiveness paragraphs), pages 6 and 7 (Table 1,
Figure 1, the summary claims, Table 2, the related-work and concluding sections), pages 4 and 5 (the
gradient and forward recursions, the corpora, the features, the protocol), pages 1 and 2 (the identity
axis, the abstract, the definitions and the four segmentation conditions), and page 8 (the reference
list). **So no page of this paper carries a claim in this file that has had one pass and not two.**

**Every image was present and legible at every one of those requests, checked at the images and not at
the calls' success lines.**

**What the read-back checked, stated exactly:** each quotation in §1 to §7 against the printed
sentence; each of Table 1's **one hundred and twenty** values and Table 2's twenty-one values against
its printed cell; the twenty bold marks, one in each column-and-task combination; and each of §7.1's
language and notation findings at its own line. *(★ CORRECTED AT THE USER-ORDERED CHECK, §10. FORMER
WORDING, PRESERVED (#12): "each of Table 1's forty-five values" — **forty-five is the count of that
table's Δbase cells alone**, and the sentence is contradicted by §5.4 and §9.2, which both put the
table at one hundred and twenty. A count of this side's own act, written without being derived at the
sentence.)* **What it did
NOT do:** it opened no other paper, no record object, and no dictionary, corpus or measurement tool,
and it ran no search of this repository.

### §8.2 What the read-back and the sweep struck in this side's own writing

**Nine changes, named rather than counted. Every one is at its site, and where a claim changed the
former wording is preserved (#12).**

1. **★ A COUNT THIS SIDE PUT ON ITS OWN READING OF TABLE 2 AND NEVER DERIVED.** Claim 16 said the
   movement over *L* was *"within 1.9 points on every one of the six baseline-and-task combinations"*.
   **Computing the six ranges refutes it** — CRF/1 on Email\_persons moves 3.9 — and the phrase
   *baseline-and-task* was wrong as well, the six being two learners across three tasks. Corrected at
   Claim 16 with the former wording preserved. **Reported as a degradation tell at §8.3, not filed
   here as an ordinary slip.**
2. **An absolute wider than the act that produced it**, at §0: the first extract's listing was said to
   have yielded *"the only thing"* of its size, where its **name** was taken from the same listing and
   is what this file's own name follows.
3. **An unbounded negative about a word this side never searched for**, at §5.2: *"the only place the
   word span appears in the measure's name"*. **No sweep for that word was run**, so the clause is
   struck and replaced by what was actually read.
4. **A two-place word with no argument, twice** — *"a condition the paper does not state anywhere
   around that table"*, at §5.5 and at §6.5. **What *around* meant was never named**; both now name
   the two places actually read, Table 2's caption and the paragraph that introduces it.
5. **Two absolutes about the paper as a whole where the act reaches the eight pages as read** —
   Claim 4's *"never measured"* and Finding 8's *"the paper never measures"* — both narrowed to what
   this paper does not do, with the eight-page bound carried in the body where it already stood.
6. **A claim of coverage this side had not stated at its width**, at §5.4: the reading that the bold
   marks mark the column-block best now says that it was checked at all twenty F1 cells and that no Δ
   cell carries one.
7. **A claim about this side's own transcription**, at Finding 2: *"every cell of Table 1 is as
   printed"* now says it was checked twice against the page, which is what happened.
8. **★ A COMPACT PHRASE OF THIS SIDE'S OWN MAKING**, at Finding 4: *"the largest-affected row"*, a
   coinage used once and explained nowhere. Replaced by the row named with its ratio. **Reported as a
   degradation tell at §8.3** under the user's ruling of 2026-08-22.
9. **A finding of this read stated too widely**, at Finding 2: it called itself *"the one finding of
   this read that bears on a reported number"*, where **Finding 4 bears on how fifteen reported values
   are to be read.** Narrowed to the only finding bearing on a reported COUNT.

**And two things the read-back ADDED rather than struck**, both printed defects found only on the
second pass: page 4's *"to compute the the normalizer"*, and reference **[1]**'s *"Santa
Barabara,USA"*. Both are at Finding 10.

### §8.3 The degradation tells, reported unprompted

**The user's standing rule of 2026-08-15 asks this side to recognise its own degradation tells, to say
so unprompted, and — when two or more appear — to report it and recommend handover at a verified
stop. TWO OF THE NAMED TELLS FIRED IN THIS SITTING'S OWN WRITING — the count tell more than once.**

*(★ THE HEADING FORMERLY ENDED "one instance each", PRESERVED (#12), and was made false by the
user-ordered check recorded at §10, which found a second instance of the count tell in this file and
two more in the handoff entry. It is amended here rather than left standing with a note, because a
heading is where a hurried reader takes the count from. The threshold conclusion is unchanged and is
strengthened by the further instances.)*

- **A count put on this side's own reading without deriving it. The instance caught before landing:**
  *"within 1.9 points on every one of the six"* (§8.2, item 1). **Caught in the act of computing the
  ranges the sentence was about**, inside §6, before this file landed at all. **A second instance in
  this file was caught only at the user-ordered check** — *"forty-five values"* for Table 1's cells at
  §8.1 — **and two more in the handoff entry**, both at §10. **This is the same tell the three entries
  before this one each report of themselves** — the hundred-and-seventy-third, -seventy-fourth and
  -seventy-fifth, each read at its own text by this side — **and the hundred-and-seventy-second's
  instance is a relay through the hundred-and-seventy-fifth, that entry not having been opened here.**
  *(★ THE RELAY CLAUSE AND THE COUNT WERE CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING,
  PRESERVED (#12): "This is the same tell the four entries before this one each report of themselves —
  the hundred-and-seventy-second, -seventy-third, -seventy-fourth and -seventy-fifth" — **a claim about
  four entries' own texts where this side opened three of them.**)*
- **Compact jargon of this side's own making where a plain phrase exists. One instance:**
  *"the largest-affected row"* (§8.2, item 8). **The user's ruling of 2026-08-22 counts an unexplained
  self-invented term as a degradation tell in its own right**, and the hundred-and-seventy-third entry
  records an instance of exactly this shape. **Caught at the sweep.**

**What this does and does not mean.** Both were caught by this side's own passes and before the file
landed; **the hundred-and-seventy-fourth and -seventy-fifth entries both record in terms that catching
a tell before landing does not lower the count**, and this file follows them. **Two named tells is the
threshold the rule states**, so the report is made here and the recommendation is made in the
conversation and in this sitting's handoff entry: **the close is a verified stop and the next member
should be taken by a fresh session.** It is not a recommendation to abandon anything mid-thing.

### §8.4 The bound on this section

**The read-back and the sweep are further passes by the same side over the same writing.** **Eight of
the nine defects at §8.2 were struck at the sweep and not at the read-back** — the read-back checked
quotations and values against the pages, and an unbounded claim is not the kind of thing it catches —
**and the ninth, item 1, was written into the claims section and struck only when the arithmetic
section that sentence summarised was actually computed.** **So nothing about their yield establishes
that the remainder of this file is clean**, and §10 is the demonstration: a further pass over the same
writing found more. *(★ CORRECTED AT THE USER-ORDERED CHECK, §10. FORMER WORDING, PRESERVED (#12):
"Two of the defects they struck had already survived the act of writing the sentence they sat in, and
one of them — item 1 — had survived into a section whose whole purpose was arithmetic." **Two counts
neither of which was derived: eight of the nine survived writing, and item 1 did not survive INTO the
arithmetic section — the arithmetic is what struck it.**)*

**And the record-side half of this member is silence, not a second opinion.** No object of this
project's record for this paper was opened by this side (§7.3's bound), so on everything the record
says about this paper this file states nothing at all.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**The first extract was opened for the first time AFTER §1 to §8 of this file had landed** — the order
the hundred-and-sixty-ninth entry's §3 fixes, step 7 after step 6. It is
`reading_pass/extracts/sarawagi-cohen-2004-semi-markov-conditional-random-fields.md`, **36,476 bytes**
at the listing and the same at the staging call, **read whole** (452 lines, one call). It is dated
2026-09-06 and states that it read all eight pages at the object.

**The independence bound, restated where it bites.** Before this read began, this side knew from row
11's candidacy line that the paper carries a linear-versus-exponential result (§0). **It did not know
the direction, the argument, any value, or anything the first extract found.** The comparison below was
made after this file's §1 to §8 were fixed on disk, so nothing in them could have been shaped by the
other read.

**What was re-consulted to settle the comparison:** nothing. **No page image was fetched at the
cross-check** — every point below was settled against pages this read had already read twice, and the
one place where a re-verification was needed (the §5 sentence adopted into Claim 6) had been read twice
before the adoption. *(So this cross-check opened no page; the read-back of §8.1 is where the second
pass over the pages happened.)*

### §9.2 Every value both extracts transcribed agrees, digit for digit

**Table 1 in full — all one hundred and twenty values.** The first extract carries the same table in a
one-row-per-learner-and-task form; **every baseline value, every internal-, external- and
both-dictionary value, every Δbase and every Δextern in all fifteen rows is identical to this read's
transcription.**

**Table 2 in full — all twenty-one values**, across the two learners' three *L* columns and the
semi-CRF column, on all three tasks.

**And every other value both reads carry:** the three corpora's word counts (4,226 / 73,330 / 18,121)
and document counts (395 / 300 / 216); the CSPACE game's 14 weeks and 277 people; the
rote-match dictionary range (22% to 57%); the protocol values (seven runs, 30% hold-out, 10% training,
*L* between 4 and 6); and the held file's size, 87,343 bytes.

**No disagreement anywhere among them.**

**★ THE BOUND ON THAT AGREEMENT, SHARPENED AT THE SECOND PASS OF THE USER-ORDERED CHECK (§10.4).** It
is agreement over the values **TAKEN FROM THE PAPER** that both files carry, and over nothing else.
**The first extract also carries values that point INTO this project's record — the bibliography row's
line, the slice derivation's line, two `FRAMEWORK.md` line ranges and a `population.md` line — and not
one of those was checked by this side, at any object.** Neither file transcribes Figure 1's curves, so
nothing is established about them either. *(FORMER WORDING, PRESERVED (#12): "*(Bound: this is agreement
over the values BOTH files carry. Neither file transcribes Figure 1's curves, so nothing is established
about them.)*" — true as far as it went, and it let *"every other value both reads carry"* be read as
reaching the record-side citations, which this side never opened.)*

**Both reads also independently reach the same identity finding** — that the held document prints no
venue, no year and no copyright or licence line — and the first extract adds what this read could not
have: that the bibliography's row (its line 25) names *"Semi-Markov Conditional Random Fields," NIPS
2004* with a proceedings URL and tier LINK, and that the printed title carries the row's title as a
prefix.

### §9.3 The disagreements, named rather than counted

**Three, all going against the first extract, and none of them moves a value.**

**(a) A QUOTATION SILENTLY REPAIRED — the first extract quotes the paper's §5 as *"Semi-CRFs are a
tractable extension of CRFs"*, at two places (its line 109 and its line 240). THE PAPER PRINTS
*"tractible"*.** Established twice at page 7 by this read, at the whole read and at the read-back.
**Why it is worth reporting rather than waving through: the repair hides one of the paper's own
inconsistencies** — the word is printed *tractible* in §4 and in §5 and *tractable* once, in §4's
*"inference is not tractable"*, which the first extract quotes correctly in that third place. **So the
same file renders the paper's spelling right where the paper is right and wrong where the paper is
wrong**, and this read's Finding 10 rests on the difference. **No value moves and the sense is
unchanged.**

**(b) A CLAIM ABOUT FIGURE 1's OWN LEGEND, REFUTED AT THE FIGURE.** The first extract says the figure
plots *"for CRF/4, SemiCRF+int, CRF/4+dict and SemiCRF+int+dict"*. **The legend of all three panels
prints the second series as *SemiCRF*, with no *+int*** — read at the figure image twice, at the whole
read and at the read-back. **It matters because the caption defines *+int* as marking internal
dictionary features**, so naming that series *SemiCRF+int* asserts that the plain semi-CRF curve
carries internal-dictionary features when the legend says it does not. **No value moves.**

**(c) A GLOSS ON WHAT FIFTEEN REPORTED VALUES MEAN, REFUTED BY THE CELLS THEMSELVES.** The first
extract writes that *"Δbase and Δextern are the paper's percentage changes relative to the baseline and
to the external-only condition"*, which is the caption's own wording. **Computed on all fifteen cells,
the Δextern column's denominator is the BASELINE, not the external-only value** (§6.2): fourteen cells
reproduce exactly under that rule and the fifteenth under it within one-decimal rounding, while the
external-only denominator reproduces no cell at all. **No transcribed value moves — both files carry
the same fifteen numbers — but what they mean does, by a factor of up to 3.3.** *(This one is not the
first extract's invention: it repeats the paper's caption, which is Finding 4. What the cross-check
establishes is that the caption's reading was passed through rather than checked.)*

**Nothing went against this side at the cross-check.** Stated exactly: **no claim of this extract was
refuted by the first extract, and no value of this extract moved.** **That is not a claim that this file
is clean** — nine defects of this side's own were struck earlier, one during the writing and eight at
the sweep, two of them instances of the user's named degradation tells, and they are at §8.2 and §8.3;
**and the user-ordered check at §10 then struck more, after this section had been written.**

**One tension resolved by narrowing rather than by refutation.** The first extract's finding (7) calls
this paper an instance of *"fit/evaluation separation at the object (30% hold-out, seven runs; #20)"*;
this read's §7.2 item 5 records that where the *"observed entity lengths"* that set *L* were observed is
not stated. **Taken to the paper, neither is refuted: the separation the first extract names holds for
the fitted weight vector and the reported F1, and the gap this read names is about one hand-set
constant.** Both stand, and together they are sharper than either.

### §9.4 What the doubling produced that neither read had alone, in both directions

**From the first extract, which this read cannot match: the whole of the record-side half.** It reaches
`docs/research_papers/BIBLIOGRAPHY.md`'s row, the slice derivation's own line, `FRAMEWORK.md` at DP-C
and at §14.1, the findings surface's V10 row and `population.md`'s line for it, and the row 10
extract's carried question — **and this side opened none of those objects, so on that half this is not a
second opinion but silence.** It also carries the centrality verdict with the ground for challenging
it. **This read takes no position on centrality**, for exactly that reason.

**Two precisions this read lacked, one of them adopted.** The first extract's finding (2) records that
the expressiveness claim is an upper bound, and that the paper's own concluding width is *"much of the
power"*. **Both are adopted into Claim 6 and marked there**, the §5 sentence having been read twice at
page 7 by this side before it was written in. **It also answers a question the row 10 extract had
carried** — whether the original semi-CRF's segment features see the previous segment's label — which
this read establishes independently at Equation 2 and which the first extract routes to the record.

**Four things in this read and not the first, the two substantial ones first.**

1. **★ The paper's *"eight of ten conditions"* is not reproducible from its own Table 1, and on the
   reading that makes its comparison set explicit it contradicts the paper's own *"nine of the ten"*
   two sentences earlier** (§6.4, Finding 2). **The first extract quotes the whole passage, *"eight of
   ten"* included, as [FACT], without computing it.**
2. **★ Figure 1's caption justification is refuted by the paper's own Table 1 on the task the figure's
   leftmost panel shows** — CRF/4 with internal dictionary features rises from 15.0 to 25.4 on
   Address\_State (Finding 3). **The first extract quotes that caption and does not notice.**
3. **The Δextern denominator** (§9.3(c)), which is the same object as disagreement (c) seen from this
   side.
4. **The paper's printed language and notation defects** — named at Findings 9 and 10 — and **the
   derivation that places Table 2 in the no-dictionary configuration** (§6.5). The first extract
   records none of these.

**Two corroborations, recorded because agreement derived twice is worth more than agreement asserted
once.** The first extract's derived range for the semi-CRF's baseline gain over the better CRF baseline,
*"1.3 to 5.4 F1 points"*, **was recomputed by this read at the five cells and holds exactly** (4.8, 5.3,
1.3, 2.7, 5.4). And its structural counts — **seven numbered equations, five footnotes, 21 references,
five sections and an appendix** — are **confirmed by this read at the pages**, equations (1) to (7),
footnotes 1 to 5, references [1] to [21].

**One gloss the paper does not print, noted and not called a defect.** The first extract renders
footnote 2's *"β values"* as *"backward values"*, outside quotation marks. **The paper never says what
β is**; the gloss is the standard one for a forward-backward recursion and it is a paraphrase rather
than a quotation, so it is recorded here as an enrichment and not as an error.

### §9.5 What the cross-check does NOT establish

- **It is not a verification of the record's half.** No object of this project's record was opened by
  this side, so the first extract's statements about `FRAMEWORK.md`, the findings surface,
  `population.md`, the bibliography, the slice derivation and the row 10 extract are **neither
  confirmed nor challenged here.**
- **It is not exhaustive over either file.** It ran over what both files carry, plus the four things
  this read carries alone; a later reader may find more, in either direction.
- **It establishes nothing about Figure 1's plotted values**, which neither file transcribes.
- **The first extract is UNTOUCHED.** Its three defects are recorded here and **whether they are
  corrected at their own sites is the user's**, on this line's standing ground that rewriting another
  read's text destroys what the doubling compares.

---

## §10 — The user-ordered fact- and source-check, run after this file had landed twice

### §10.1 What the check was

**The user's standing rule of 2026-09-12 extends the pre-landing check to landed work on four axes —
completeness, coherence, correctness, and misuse of hyperbole and absolutes — and his opening
instruction to this sitting ordered it over everything this side had written, the closing report to him
included.** **This file was re-read WHOLE as landed at 83,208 bytes, at the device's own copy staged
back rather than at this side's container copy** — **in five reads: four consecutive spans covering
lines 1 to 1171, and the closing §9.5 bullets, which had been read at the second landing's own proof
just before.** The sitting's handoff entry was re-read whole the same way; and the closing report to the
user was checked as part of the same body of writing. *(★ CORRECTED AT THE SECOND PASS (§10.4). FORMER
WORDING, PRESERVED (#12): "in four calls" — **a count of this side's own act that omitted the read the
whole-file coverage depends on.**)*
**Every correction below is at its own site with the former wording preserved (#12).**

### §10.2 What it found in this file — named rather than counted

1. **§0's account of what was read stopped at the first two page requests**, which was true when
   written and was made incomplete by this read's own read-back. **Cadence 8's class.**
2. **§0 named the hundred-and-seventieth entry alongside three entries read whole**, where it was read
   at its §1 alone.
3. **§2.6's bullet heading carried a double negative** — *"which is NOT non-Markovian"* — where a plain
   phrase exists.
4. **§3.2 named the wrong quantity at an equation**: the winning segmentation's value is max_y
   *V*(|**x**|,*y*), not *V*(|**x**|,*y*). **The only correction of this check that touches the
   mathematics**, and it moves no transcribed value of the paper's.
5. **§5.4 carried a sentence left over from an arrangement this file does not use**, describing the
   bold marks as recorded in a column — false of the tables printed directly beneath it.
6. **★ §8.1 put Table 1 at *"forty-five values"***, which is the count of its Δbase cells alone, and is
   contradicted by §5.4 and §9.2. **This is a second instance of the count tell §8.3 reports** — a
   count of this side's own act written without being derived at the sentence — **and it survived the
   read-back, the sweep and the cross-check**, being caught only here.
7. **§8.3 claimed four entries report that tell of themselves** where this side opened three of them.
8. **§8.4 carried two counts neither of which was derived** — how many defects survived the act of
   writing, and a claim that item 1 had *"survived into"* the arithmetic section when the arithmetic is
   what struck it.
9. **§9.3 said the nine defects were struck *"at the read-back and the sweep"***, where one was struck
   during the writing.

### §10.3 What the check did NOT do, and what it does not establish

**It fetched no page image, opened no paper, did not re-open the first extract as a file, ran no web
access, swept no repository, and changed no transcribed value, no byte count, no modification time, no
row number and no verdict.** Every value of the paper's in this file stands exactly as it stood after
the cross-check.

**And it is a further pass over the same writing by the same side.** **Item 6 is the very tell this file
reports at §8.3, in a section written to report it** — which is the sharpest thing this check
establishes: **reporting a defect class is not immunity from it.** Two of the nine items were defects in
this file's account of its OWN acts (items 1 and 9) and one was in its account of another file's text
(item 7), which is the same distribution the two entries before this one record of their own checks.
**Nothing about this check's yield says the remainder is clean.**

### §10.4 A SECOND PASS OF THE SAME CHECK, ORDERED AFTER THE FIRST HAD LANDED, AND WHAT IT FOUND HERE

**The user ordered the check again over everything written, on the four axes, after the third landing
of this file and the second of the handoff entry.** It found **two defects in this file**, both
corrected at their sites above with the former wordings preserved (#12):

- **§9.2's bound was too narrow for the sentence it bounded.** *"And every other value both reads
  carry"* could be read as reaching the first extract's citations into this project's record — the
  bibliography row, the slice derivation, two `FRAMEWORK.md` ranges and a `population.md` line — **none
  of which this side opened at any object.** The bound now says the agreement is over values taken from
  the paper and over nothing else. **This is a completeness defect in a bound, which is the worst place
  for one**: a bound exists to stop a reader taking more from a claim than the act supports.
- **§10.1 put the whole-file re-read at *"four calls"*** where five reads were needed to cover the
  file, the fifth being the closing bullets read at the previous landing's proof. **A count of this
  side's own act, and the third of that shape in this file** — §8.1's and this one — after §8.3 was
  written to report the class.

**What this second pass did NOT do.** It fetched no page image, opened no paper, re-opened no other
file of the record, ran no web access, swept no repository, and **changed no transcribed value, no
count of the paper's, no byte count, no modification time and no verdict.** **It is a third pass over
the same writing by the same side, and it found a defect in the very sentence the first pass had left
standing as a bound** — so a further pass kept finding things, and no pass of this side's own
establishes that the remainder is clean. *(★ THE CLAUSE FORMERLY READ "which is the plainest evidence
available that a further pass keeps finding things", PRESERVED (#12) — **a superlative over evidence
this side never enumerated**, struck in the act of re-reading this very section.)*

