# Lafferty, McCallum & Pereira 2001 — "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data" — SECOND INDEPENDENT EXTRACT

> **STATUS: READING-PASS EXTRACT, SECOND PASS. NOTHING HERE IS RULED.** Written 2026-09-18 by the Cowork
> session that booted on `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_five.md`,
> under `cowork_reading_pass_commission_2026_08_30.md` §4 (a CENTRAL source is extracted in a second
> independent pass and the two extracts cross-checked) and the eight-step order of handoff entry 169 §3,
> as amended at its naming point by Ruling 2 of entry 186 §2. **The paper is Task B, L2's slice, row 12**
> (row numbers are `reading_pass/candidacy_upgrades.md`'s). Held file:
> `docs/research_papers/lafferty_mccallum_pereira_2001_icml_conditional_random_fields.pdf`, 307,737 bytes
> at this session's folder listing; **8 pages, established at the tool** by a deliberately out-of-range
> request (page 20 refused with "PDF has 8 pages"). Read whole in two requests, pages 1–4 and 5–8; **every
> page image was present in both** (checked at the images, not at the call's success line).
>
> Page numbers below are the PDF's own (1–8); the paper prints no page numbers on its pages as rendered.

## §0 — Declarations of independence and its bound

- **What this side read before opening the paper, that bears on it:** the progress table
  `reading_pass/l2_slice_reading_progress.md` was searched for its row numbers and its "Second pass"
  cells only, and the row-12 line was opened for **two strings only**: the head of the row (the paper's
  identity, printed title and authors — the first 160 characters) and the first extract's file path. The
  row's Grade, Centrality and any verdict text were **not** read. `docs/research_papers/BIBLIOGRAPHY.md`
  line 26 was read (the row: authors, short title, venue, a URL, a held mark, and the tier word LINK).
- **Name-only look-up, declared under Ruling 2 (entry 186 §2):** `reading_pass/extracts/` was listed by
  file name to find the first extract's name. It holds **two** files for this paper:
  `lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data.md`
  (63,127 bytes, modification time 1788718189940 — the one the progress table names) and
  `…-sequence-data-1.md` (62,394 bytes, modification time 1788718777145). **Neither was opened before
  §9.** The file names carry author, year and the paper's own title words, which the paper supplies.
- **Contamination from the record's own text about this paper:** this side had read, at boot, nothing
  that summarises the paper's content — of the handoff entries read (195, 190, 188, 186, 169, and 185 at
  §3, 152 at (i)–(x), 118 at its bridge-fault section), none summarises it; entry 188 head (4) names
  "row 12" as next and nothing more. The commission was read whole. `FRAMEWORK.md`,
  `population.md`, the findings surface, the slice derivation and the candidacy file were **not** opened.
- **General knowledge is the larger contamination and is named as such:** this side knows conditional
  random fields as a method class from outside this repository. Entry 185 §3 item 2 records that both
  reads of row 46 supplied mechanism and run-count claims from general knowledge of the method class.
  **Every mechanism statement below is therefore located to a page**, and a statement this side could
  make from general knowledge but could not find on a page is written as ABSENT (§7), not as a fact.
- **What this file is not:** it is not a record-facing extract. What `FRAMEWORK.md` or any design point
  says about this paper, and the paper's centrality verdict, are the first extract's half and are not
  re-derived here (entry 169 §5(vii)).

## §1 — Identity, checked at page 1

- **§1.1 Title, as printed:** *"Conditional Random Fields: Probabilistic Models for Segmenting and
  Labeling Sequence Data"* (page 1, head).
- **§1.2 Authors and affiliations, as printed:** John Lafferty (†∗), Andrew McCallum (∗†), Fernando
  Pereira (∗‡); ∗ WhizBang! Labs–Research, Pittsburgh; † School of Computer Science, Carnegie Mellon
  University; ‡ Department of Computer and Information Science, University of Pennsylvania (page 1).
- **§1.3 Venue:** the pages as rendered carry **no venue line, no copyright line, no proceedings header
  and no page numbers**. The bibliography row (line 26) says ICML 2001; the held file's name says
  `icml`. **The venue is therefore taken from the record, not from the page.** The paper's own
  self-references are consistent with a 2001 date (it cites "Punyakanok & Roth, 2001 … Forthcoming",
  page 8) but do not state its own venue.
- **§1.4 Match to the bibliography row:** authors and title match line 26 of `BIBLIOGRAPHY.md` by
  name and by the short title *"Conditional Random Fields"* as a prefix of the printed title. **No
  identity finding.**
- **§1.5 Length and structure:** 8 pages. Sections as printed: Abstract; 1 Introduction; 2 The Label
  Bias Problem; 3 Conditional Random Fields; 4 Parameter Estimation for CRFs; 5 Experiments (5.1
  Modeling label bias; 5.2 Modeling mixed-order sources; 5.3 POS tagging experiments); 6 Further
  Aspects of CRFs; 7 Related Work and Conclusions; Acknowledgments; References. Figures 1–4; three
  footnotes; equations numbered (1) and (2) only.

## §2 — Claims, labeled

The labels are the commission's: **FACT** = stated or measured in the paper, with its location;
**THEORY** = established published theory the paper invokes; **CONJECTURE** = the paper's own
speculation, or a claim it makes without a measurement or a citation. Quotations are verbatim from the
page as rendered.

### §2.1 The problem the paper sets

- **[FACT, page 1, abstract]** The paper presents *"conditional random fields, a framework for building
  probabilistic models to segment and label sequence data."*
- **[FACT, page 1, §1]** Generative models (HMMs, stochastic grammars) *"assign a joint probability to
  paired observation and label sequences; the parameters are typically trained to maximize the joint
  likelihood of training examples."* Doing so *"needs to enumerate all possible observation sequences"*
  and *"it is not practical to represent multiple interacting features or long-range dependencies of the
  observations, since the inference problem for such models is intractable."*
- **[FACT, page 1, §1]** The stated motivation for conditional models: a conditional model *"does not
  expend modeling effort on the observations, which at test time are fixed anyway"*, and *"the
  conditional probability of the label sequence can depend on arbitrary, non-independent features of the
  observation sequence without forcing the model to account for the distribution of those
  dependencies."*
- **[FACT, page 1, §1, footnote 1]** *"Output labels are associated with states; it is possible for
  several states to have the same label, but for simplicity in the rest of this paper we assume a
  one-to-one correspondence."*

### §2.2 The label bias problem (§2, pages 2–3)

- **[FACT, page 2, §1 and §2]** MEMMs and *"other non-generative finite-state models based on next-state
  classifiers"* share *"a weakness we call here the label bias problem: the transitions leaving a given
  state compete only against each other, rather than against all other transitions in the model."* The
  per-state normalisation implies *"a 'conservation of score mass' (Bottou, 1991) whereby all the mass
  that arrives at a state must be distributed among the possible successor states."* Consequence stated:
  *"This causes a bias toward states with fewer outgoing transitions. In the extreme case, a state with a
  single outgoing transition effectively ignores the observation."*
- **[FACT, page 2, Figure 1 and §2]** The worked example is a finite-state model distinguishing the
  words *rib* and *rob* over the observation sequence *r i b*: after *r*, mass splits *"roughly equally"*
  between states 1 and 4; on observing *i*, *"state 4 has no choice but to pass all its mass to its
  single outgoing transition, since it is not generating the observation, only conditioning on it."* So
  *"the top path and the bottom path will be about equally likely, independently of the observation
  sequence"*, and whichever word is slightly more common in training *"will always win."*
- **[FACT, page 2, §2]** The paper says this behaviour *"is demonstrated experimentally in Section 5"*.
- **[FACT, pages 2–3, §2]** Two prior remedies are attributed to Bottou (1991): changing the
  state-transition structure (collapsing states 1 and 4 — *"a special case of determinization (Mohri,
  1997), but determinization of weighted finite-state machines is not always possible, and even when
  possible, it may lead to combinatorial explosion"*), and starting from a fully-connected model and
  letting training find a structure (*"But that would preclude the use of prior structural knowledge that
  has proven so valuable in information extraction tasks (Freitag & McCallum, 2000)."*).
- **[FACT, page 3, §2]** The paper's stated requirement: *"Proper solutions require models that account
  for whole state sequences at once by letting some transitions 'vote' more strongly than others depending
  on the corresponding observations."* And its claim of uniqueness, hedged in its own words: *"To the best
  of our knowledge, CRFs are the only model class that does this in a purely probabilistic setting, with
  guaranteed global maximum likelihood convergence."*
- **[FACT, page 2, §1]** The stated critical difference: *"a MEMM uses per-state exponential models for
  the conditional probabilities of next states given the current state, while a CRF has a single
  exponential model for the joint probability of the entire sequence of labels given the observation
  sequence. Therefore, the weights of different features at different states can be traded off against
  each other."*

### §2.3 The model (§3, pages 3–4)

- **[FACT, page 3, §3, Definition]** *"Let G = (V, E) be a graph such that Y = (Y_v)_{v∈V}, so that Y
  is indexed by the vertices of G. Then (X, Y) is a conditional random field in case, when conditioned on
  X, the random variables Y_v obey the Markov property with respect to the graph: p(Y_v | X, Y_w, w ≠ v)
  = p(Y_v | X, Y_w, w ∼ v), where w ∼ v means that w and v are neighbors in G."* The paper adds: *"a CRF
  is a random field globally conditioned on the observation X."*
- **[FACT, page 3, §3]** The paper does not model the marginal: *"we construct a conditional model
  p(Y | X) from paired observation and label sequences, and do not explicitly model the marginal p(X)."*
- **[FACT, page 3, §3]** X *"may also have a natural graph structure; yet in general it is not necessary
  to assume that X and Y have the same graphical structure, or even that X has any graphical structure
  at all."* The paper restricts itself: *"in this paper we will be most concerned with sequences."*
- **[THEORY, page 3, §3, eq. (1)]** For G a tree, *"by the fundamental theorem of random fields
  (Hammersley & Clifford, 1971)"*, the conditional has the form
  p_θ(y | x) ∝ exp( Σ_{e∈E,k} λ_k f_k(e, y|_e, x) + Σ_{v∈V,k} μ_k g_k(v, y|_v, x) ), with f_k edge
  features and g_k vertex features, both *"given and fixed"*. (The cited Hammersley & Clifford 1971 is
  listed in the references as an *"Unpublished manuscript."*, page 8.)
- **[FACT, page 3, §3]** The estimation objective is the conditional log-likelihood
  O(θ) = Σ_i log p_θ(y^(i) | x^(i)), *"∝ Σ_{x,y} p̃(x, y) log p_θ(y | x)"*, with p̃ the empirical
  distribution of the training data D = {(x^(i), y^(i))}_{i=1..N}.
- **[FACT, page 3, §3]** *"As a particular case, we can construct an HMM-like CRF by defining one feature
  for each state pair (y', y), and one feature for each state-observation pair (y, x)"*; the
  corresponding parameters *"play a similar role to the (logarithms of the) usual HMM parameters"*.
  Boltzmann chain models are named as similar in form but using a single normalisation constant,
  *"whereas CRFs use the observation-dependent normalization Z(x) for conditional distributions."*
- **[FACT, page 4, §3 and Figure 2]** For the chain case the paper adds start and stop states Y_0 and
  Y_{n+1}, defines the |Y|×|Y| matrix M_i(x) with entries exp(Λ_i(y', y | x)), gives the partition
  function as the (start, stop) entry of the matrix product M_1(x)···M_{n+1}(x), and writes
  p_θ(y | x) as the product of the M_i(y_{i−1}, y_i | x) over the (start, stop) entry of the product.
  Figure 2 draws HMM (left), MEMM (centre) and chain CRF (right); *"An open circle indicates that the
  variable is not generated by the model."*
- **[FACT, page 4, §3]** Two stated attractions: *"the features do not need to specify completely a state
  or observation, so one might expect that the model can be estimated from less training data"*, and
  *"the convexity of the loss function; indeed, CRFs share all of the convexity properties of general
  maximum entropy models."* (Page 2, footnote 2, bounds the convexity claim: *"In the case of fully
  observable states, as we are discussing here; if several states have the same label, the usual local
  maxima of Baum-Welch arise."*)

### §2.4 Parameter estimation (§4, pages 4–5)

- **[FACT, page 4, §4]** Two iterative-scaling algorithms are given, *"both … based on the improved
  iterative scaling (IIS) algorithm of Della Pietra et al. (1997)"*. The IIS update for an edge feature
  solves Ẽ[f_k] = Σ p̃(x) Σ_y p(y|x) Σ_i f_k(e_i, y|_{e_i}, x) e^{δλ_k T(x,y)}, where T(x, y) is the
  *"total feature count"*.
- **[FACT, page 4, §4]** The difficulty named: T(x, y) *"is a global property of (x, y), and dynamic
  programming will sum over sequences with potentially varying T."* **Algorithm S** uses a *"slack
  feature"* s(x, y) = S − Σ f − Σ g with S chosen so s ≥ 0 on the training set, making T(x, y) = S;
  **Algorithm T** *"keeps track of partial T totals."*
- **[FACT, pages 4–5, §4]** Forward vectors α_i(x) and backward vectors β_i(x) are defined with the
  usual base cases and recurrences α_i = α_{i−1} M_i, β_i^T = M_{i+1} β_{i+1}. Under Algorithm S the
  updates are δλ_k = (1/S) log(Ẽf_k / Ef_k), δμ_k = (1/S) log(Ẽg_k / Eg_k), with Ef_k and Eg_k the
  model expectations computed from α, β and Z_θ(x) (page 5, left column). The paper says the marginal
  p_θ(Y_i = y | x) = α_i(y|x) β_i(y|x) / Z_θ(x) and that *"This algorithm is closely related to the
  algorithm of Darroch and Ratcliff (1972), and MART algorithms used in image reconstruction."*
- **[FACT, page 5, §4]** A stated limitation of Algorithm S: *"The constant S in Algorithm S can be quite
  large, since in practice it is proportional to the length of the longest training observation sequence.
  As a result, the algorithm may converge slowly, taking very small steps toward the maximum in each
  iteration."*
- **[FACT, page 5, §4, eq. (2)]** Algorithm T defines T(x) = max_y T(x, y), accumulates expectations
  a_{k,t} and b_{k,t} by value of T(x) = t, and sets δλ_k = log β_k, δμ_k = log γ_k where β_k, γ_k are
  *"the unique positive roots"* of Σ_{t=0}^{T_max} a_{k,t} β_k^t = Ẽf_k and the analogous equation for
  g_k, *"which can be easily computed by Newton's method."*
- **[FACT, page 5, §4]** *"A single iteration of Algorithm S and Algorithm T has roughly the same time and
  space complexity as the well known Baum-Welch algorithm for HMMs."*
- **[FACT, page 5, §4]** Convergence: the paper says *"we can derive an auxiliary function to bound the
  change in likelihood from below; this method is developed in detail by Della Pietra et al. (1997). The
  full proof is somewhat detailed; however, here we give an idea of how to derive the auxiliary
  function."* The sketch given (right column) bounds O(θ') − O(θ) below by A(θ', θ) via *"the convexity
  of − log and exp"*, and *"Differentiating A with respect to δλ_k and setting the result to zero yields
  equation (2)."* **So the paper sketches, and does not itself print, the convergence proof.**

### §2.5 Further aspects (§6, page 7) and related work (§7, pages 7–8)

- **[CONJECTURE, page 7, §6]** CRFs *"can be trained using the exponential loss objective function used
  by the AdaBoost algorithm"* via the parallel update algorithm of Collins et al. (2000); *"This requires a
  forward-backward algorithm to compute efficiently certain feature expectations, along the lines of
  Algorithm T, except that each feature requires a separate set of forward and backward accumulators."*
  Stated as possible; not run.
- **[CONJECTURE, page 7, §6]** Feature selection and induction: *"the feature induction algorithms
  presented in Della Pietra et al. (1997) can be adapted to fit the dynamic programming techniques of
  conditional random fields."* Stated as possible; not run.
- **[FACT, page 7, §7]** The paper's own priority claim, hedged: *"As far as we know, the present work is
  the first to combine the benefits of conditional models with the global normalization of random field
  models."* Local conditional models (Berger et al. 1996; Ratnaparkhi 1996; McCallum et al. 2000) *"may
  suffer from label bias."*
- **[FACT, pages 7–8, §7]** Named alternatives and their stated shortcomings: non-probabilistic local
  decision models (Brill 1995; Roth 1998; Abney et al. 1999) — *"Label bias would be expected to be a
  problem here too"*; generate-candidates-then-rerank (Schwartz & Austin 1993; Collins 2000) — *"these
  methods fail when the correct output is pruned away in the first pass"*; gradient-descent over local
  classifiers with a smooth loss (LeCun et al. 1998) — *"their loss function is not convex, so they may
  get stuck in local minima."*
- **[FACT, page 8, §7]** The paper's own summary of properties: *"discriminatively trained models for
  sequence segmentation and labeling; combination of arbitrary, overlapping and agglomerative observation
  features from both the past and future; efficient training and decoding based on dynamic programming;
  and parameter estimation guaranteed to find the global optimum."* And its own stated main limitation:
  *"Their main current limitation is the slow convergence of the training algorithm relative to MEMMs, let
  alone to HMMs, for which training on fully observed data is very efficient."*
- **[CONJECTURE, page 8, §7]** Future work named: *"alternative training methods such as the update
  methods of Collins et al. (2000) and refinements on using a MEMM as starting point"*; *"More general
  tree-structured random fields, feature induction methods, and further natural data evaluations."*

## §3 — Coupling facts (mandatory)

- **§3.1 What the method ASSUMES upstream (stated input requirements).**
  - Paired observation and label sequences for training: D = {(x^(i), y^(i))} (page 3, §3). Labels are
    **fully observed** in the setting the paper treats (page 2, footnote 2; page 3 "fully observable
    states").
  - A **fixed graph** G over the labels, assumed known: *"Throughout the paper we tacitly assume that the
    graph G is fixed"* (page 3, §3); for everything from §3's chain case on, a **chain**: *"For the
    remainder of the paper we assume that the dependencies of Y, conditioned on X, form a chain"* (page
    4, §3).
  - A **finite label alphabet** Y (page 3, §3), with start and stop states added (page 4).
  - Features f_k, g_k **given and fixed** in advance (page 3, §3); the paper's feature induction is
    future work (page 7, §6). Features may depend on the whole observation sequence x, past and future
    (page 1, §1; page 8, §7).
  - For the POS experiments, tokenised words with a given tag set of 45 tags (page 7, §5.3).
  - The label sequence has the **same length as the observation sequence** in the chain case (one Y_i
    per position i, page 4, §3). **The paper does not treat segmentation of the observation sequence into
    variable-length units as a separate object**; "segmenting" in the title is realised as per-position
    labeling (pages 3–4, and the POS task, page 7). *(This is a reading of what the pages define, stated
    so that a later chain judgment does not assume a segmental model here.)*
- **§3.2 What it HANDS downstream (outputs and their form).**
  - A conditional distribution p_θ(y | x) over whole label sequences (page 3, eq. (1); page 4, the matrix
    form).
  - Per-position marginals p_θ(Y_i = y | x) = α_i(y|x) β_i(y|x) / Z_θ(x) (page 5, §4).
  - A decoded labeling: the experiments use *"the Viterbi algorithm … to label a test set; the
    experimental results do not significantly change when using forward-backward decoding to minimize the
    per-symbol error rate"* (page 6, §5.2).
  - Trained parameters θ = (λ_1, λ_2, …; μ_1, μ_2, …) (page 3, §3).
- **§3.3 Its own STATED SCOPE and limits.**
  - Scope: sequence segmentation and labeling (page 1); chain-structured label graphs for the results
    given (page 4); tree-structured fields named as future work (page 8).
  - Limits stated by the paper: slow training convergence relative to MEMMs and HMMs (page 8, §7; page 5,
    §4 on Algorithm S's small steps; page 7, §5.3: CRF from the uniform start *"had not converged even
    after 2,000 iterations"* while MEMM converged *"in around 100 iterations"*); the convexity guarantee
    holds for fully observable states only (page 2, footnote 2); the synthetic experiments *"are not
    designed to demonstrate the advantages of the additional representational power of CRFs and MEMMs
    relative to HMMs"* (page 6, Figure 3 caption) and *"do not use overlapping features of the
    observations"* (page 6, §5).

## §4 — Measured results, as the paper states them

- **§4.1 Label bias, synthetic (page 6, §5.1).** Data generated from *"a simple HMM which encodes a noisy
  version of the finite-state network in Figure 1"*; each state emits its designated symbol with
  probability 29/32 and any other with probability 1/32. MEMM and CRF trained with the same topologies;
  observation features are *"the identity of the observation symbols."* *"In a typical run using 2,000
  training and 500 test samples, trained to convergence of the iterative scaling algorithm, the CRF error
  is 4.6% while the MEMM error is 42%."* **The paper says "a typical run"; it states no number of runs
  and no spread.**
- **§4.0 The paper's own summary of what §5 shows (page 6, §5 opening).** *"results clearly indicate
  that even when the models are parameterized in exactly the same way, CRFs are more robust to inaccurate
  modeling assumptions than MEMMs or HMMs, and resolve the label bias problem, which affects the
  performance of MEMMs."* And: *"We also show that the addition of overlapping features to CRFs and MEMMs
  allows them to perform much better than HMMs, as already shown for MEMMs by McCallum et al. (2000)."*
- **§4.2 Mixed-order sources, synthetic (page 6, §5.2 and Figure 3).** Five labels (|Y| = 5), 26
  observation values (|X| = 26) — *"however, the results were qualitatively the same over a range of
  sizes for Y and X"*; data from a mixed-order HMM with transition p_α(y_i | y_{i−1}, y_{i−2})
  = α p_2(·) + (1 − α) p_1(·) and emission p_α(x_i | y_i, x_{i−1}) = α p_2(·) + (1 − α) p_1(·); α = 0
  is a standard first-order HMM. Conditional tables constrained sparse: *"p_α(·|y, y') can have at most
  two nonzero entries, for each y, y', and p_α(·|y, x') can have at most three nonzero entries for each
  y, x'."* *"For each randomly generated model, a sample of 1,000 sequences of length 25 is generated for
  training and testing."* CRF trained with Algorithm S (*"since the length of the sequences and number
  of active features is constant, Algorithms S and T are identical"*); *"typically taking approximately
  500 iterations for the model to stabilize"*, *"approximately 0.2 seconds"* per iteration on *"the 500
  MHz Pentium PC"*; MEMM *"stabilizing after approximately 100 iterations."* Viterbi decoding for both.
  Parameterisation: *"The figure compares models parameterized as μ_y, λ_{y',y}, and λ_{y',y,x}; results
  for models parameterized as μ_y, λ_{y',y}, and μ_{y,x} are qualitatively the same."*
  Result: *"As shown in the first graph, the CRF generally outperforms the MEMM, often by a wide margin
  of 10%–20% relative error. (The points for very small error rate, with α < 0.01, where the MEMM does
  better than the CRF, are suspected to be the result of an insufficient number of training iterations
  for the CRF.)"* Figure 3's caption: *"the CRF typically significantly outperforms the MEMM"* (left
  plot); *"the HMM outperforms the MEMM"* (centre); in the right plot *"each open square represents a
  data set with α < 1/2, and a solid circle indicates a data set with α ≥ 1/2"*, and *"when the data is
  mostly second order (α ≥ 1/2), the discriminatively trained CRF typically outperforms the HMM."* The
  axes run 0–60 (error, in the units the plots print). **Figure 3 prints points, not a table; no numeric
  cell beyond the "10%–20% relative error" sentence and the α < 0.01 caveat is stated in text.**
- **§4.3 POS tagging, Penn treebank (page 7, §5.3 and Figure 4).** *"each word in a given input sentence
  must be labeled with one of 45 syntactic tags"*; *"first-order models trained on 50% of the 1.1 million
  word corpus. The oov rate is 5.45%."* Figure 4, transcribed cell by cell (model — error — oov error):
  HMM — 5.69% — 45.99%; MEMM — 6.37% — 54.61%; CRF — 5.55% — 48.05%; MEMM⁺ — 4.81% — 26.99%;
  CRF⁺ — 4.27% — 23.76%; where ⁺ = *"Using spelling features"*. The paper's reading of the first block:
  *"the HMM outperforms the MEMM, as a consequence of the label bias problem, while the CRF outperforms
  the HMM."* Of the second: *"both the MEMM and the CRF benefit significantly from the use of these
  features, with the overall error rate reduced by around 25%, and the out-of-vocabulary error rate
  reduced by around 50%."* Spelling features named: *"whether a spelling begins with a number or upper
  case letter, whether it contains a hyphen, and whether it ends in one of the following suffixes: -ing,
  -ogy, -ed, -s, -ly, -ion, -tion, -ity, -ies."* Training detail: MEMM⁺ *"was trained to convergence in
  around 100 iterations. Its parameters were then used to initialize the training of CRF⁺, which
  converged in 1,000 iterations. In contrast, training of the same CRF from the uniform distribution had
  not converged even after 2,000 iterations."* The paper says *"the results are qualitatively similar for
  other splits of the data"* and reports no spread. **The text of §5.3 refers to "Figure 5.3"; the figure
  is captioned "Figure 4".** (A labelling inconsistency inside the paper, page 7, both occurrences.)
- **§4.4 A derivation this side can make from the printed cells, and its status.** Relative to the HMM's
  5.69%, the CRF's 5.55% is 0.14 points lower (about 2.5% relative); the MEMM's 6.37% is 0.68 points
  higher. Relative to CRF (5.55%), CRF⁺ (4.27%) is 1.28 points lower, which is a 23% relative
  reduction; relative to MEMM (6.37%), MEMM⁺ (4.81%) is 1.56 points lower, 24% relative — consistent
  with the paper's *"around 25%"*. On oov: CRF 48.05% → CRF⁺ 23.76% is a 51% relative reduction; MEMM
  54.61% → MEMM⁺ 26.99% is 51% — consistent with *"around 50%"*. **These derivations are this side's
  arithmetic over the printed cells, not the paper's statements.** Note also that on the oov column
  without spelling features the CRF (48.05%) is **worse** than the HMM (45.99%), which the paper's text
  does not remark on.

## §5 — What the paper states about uncertainty, reproducibility and ground truth (against #24, #16, #21)

- **No spread, confidence interval or significance test is met in the 8 pages as read**;
  §5.1 reports *"a typical run"*, §5.2 shows scatter plots over randomly generated models without a
  count of models stated in text, §5.3 reports one 50%-50% split with a qualitative statement about other
  splits.
- The synthetic data generators are specified (§4.1, §4.2 above) to the level of the mixture form and
  sparsity constraints; random seeds, the number of generated models, and the p_1, p_2 tables are not
  printed.
- The POS ground truth is the Penn treebank's tags; the paper says nothing about annotation agreement
  or a ceiling.

## §6 — Terms the paper uses, in the paper's sense

- *label bias problem* — the paper's own name (page 2), attributed to the per-state normalisation of
  MEMMs and similar next-state classifiers.
- *conservation of score mass* — quoted from Bottou (1991) (page 2).
- *MEMM* — maximum entropy Markov model, McCallum et al. (2000) (page 1).
- *slack feature*, *total feature count*, *forward vectors*, *backward vectors* — the paper's terms in §4
  (pages 4–5).
- *oov* — out-of-vocabulary words, *"which are not observed in the training set"* (page 7).

## §7 — Stated ABSENT: things a reader might supply from the method class that the pages do not say

Each item below was looked for at the page and met nowhere in the 8 pages as read.

- **No gradient-based (L-BFGS or similar) training** is described; the two algorithms given are
  iterative scaling (§4). Gradient methods are mentioned only as the training of *other* models (LeCun
  et al. 1998; page 8) and as future work is not named for CRFs beyond Collins et al. (2000) updates.
- **No regularisation** (no Gaussian prior, no penalty term) is met in the pages as read; the objective
  is the bare conditional log-likelihood (page 3).
- **No statement about initialisation other than** page 7's: *"One usually starts training from the all
  zero parameter vector, corresponding to the uniform distribution. However, for these datasets, CRF
  training with that initialization is much slower than MEMM training."*
- **No semi-Markov or segment-level formulation**: one label per position (page 4). *(The semi-Markov
  extension is Sarawagi & Cohen 2004, a different row of this slice, and is not this paper's.)*
- **No feature templates beyond those named**: HMM-like state-pair and state-observation features
  (page 3), observation identity (page 6), tag-word and tag-tag pairs plus the listed spelling features
  (page 7).
- **No statement of the number of runs** behind §5.1's *"typical run"* or of the number of random models
  behind Figure 3.
- **No music, audio, or harmony content of any kind**; the paper's domains are synthetic sequences and
  POS tagging, with biology and NLP named as motivating fields (page 1).
- **No venue, copyright or page-number line printed on the pages as rendered** (§1.3).

## §8 — The read-back and the sweep (steps 4 and 5 of entry 169 §3), written after the text above was finished

**§8.1 The read-back.** Every quotation in §2–§4 was re-read against its page image after the draft was
written. Number lists were read entry by entry (entry 185 §3 item 1): Figure 4's ten cells, the suffix
list of nine, the two synthetic-experiment counts (2,000 / 500; 1,000 sequences of length 25; 29/32 and
1/32; 500 and 100 iterations; 0.2 seconds; 1,000 and 2,000 iterations; 45 tags; 1.1 million; 5.45%). No
transcription created a contradiction the paper does not show. **What the read-back changed:** a
quotation at §2.2 that had been cut mid-sentence was completed to the page's full stop; three
qualifications the page carries and the draft had dropped were added — §5.2's *"qualitatively the same
over a range of sizes for Y and X"*, its second parameterisation sentence, and page 7's initialisation
sentence (now at §7); and the paper's own summary sentences at the head of §5 were added as §4.0, since a
first extract is likely to lean on them.

**§8.2 The sweep for absolutes and for mechanism supplied from general knowledge** (entry 169 cadence 7;
entry 185 §3 item 2). Each hit read at its line. Two negatives of this side's own were reworded from
*"anywhere"* to the ruled form *met nowhere in the pages as read* (§5, §7). Every sentence stating how the
method works was checked for a page locator; each has one. Every sentence stating how often something
ran was checked: the paper itself gives *"a typical run"* (§4.1) and no run count, and this file says so
rather than supplying one. The word *only* occurs in this side's own voice at §1.5 (*"equations numbered
(1) and (2) only"*) — checked over all eight pages, no other numbered equation is printed — and at §0
(*"two strings only"*), which describes this side's own act. The remaining absolutes are inside
quotations and are the paper's.

**§8.3 A labelling inconsistency inside the paper, noted and not resolved:** §5.3's text twice says
*"Figure 5.3"* where the figure is captioned *"Figure 4"* (page 7). Recorded at §4.3; it moves no value.

**§8.4 What the read-back did not do.** It did not re-open the PDF through a fresh request; it re-read
the page images already returned. It ran no web access to check the venue (§1.3 stands as taken from the
record). It did not open either first-extract file.

## §9 — The cross-check against the first extract (step 7 of entry 169 §3), written after §0–§8 had landed

**§9.1 What was read, and when.** This file was landed and proved (33,424 bytes, modification time
1789748025729, last content line 398 read) **before** the first extract was opened. Then
`reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data.md`
(63,127 bytes, modification time 1788718189940 — the file the progress table names; dated 2026-09-06 in
its own banner) was staged and read **whole**, 742 lines, in one call. The stray sibling
`…-sequence-data-1.md` (62,394 bytes) was **not** opened. Every disagreement below was resolved **at the
page image already in this session**, re-read at the sentence.

**§9.2 Agreements, named.** The two reads agree on: the printed title, the three authors and the three
affiliations; the absence of any printed venue, copyright, licence or page-number line; the eight pages and
the section structure; the two numbered equations and the three footnotes; the definition of a CRF; equation
(1) and its "given and fixed" features; the matrix form and the placement of Z_θ(x); the Boltzmann-chain
contrast; the MEMM contrast and footnote 2's qualification of convexity; the HMM-like construction; the
label-bias mechanism; both of Bottou's rejected remedies and the "proper solutions" sentence; the two
algorithms, the slack feature, Algorithm T's roots, the Baum-Welch complexity statement and the
Darroch–Ratcliff remark; §5.1's 29/32, 1/32, 2,000, 500, **4.6% and 42%**; §5.2's |Y| = 5, |X| = 26, the
sparsity limits, 1,000 sequences of length 25, ≈500 and ≈100 iterations, 0.2 seconds, the 500 MHz PC, the
"10%–20% relative error" sentence and the α < 0.01 caveat, and Figure 3's caption; **every one of Figure
4's ten cells** (5.69, 45.99, 6.37, 54.61, 5.55, 48.05, 4.81, 26.99, 4.27, 23.76), the 45 tags, the 50%
split, the 1.1 million words, the 5.45% oov rate, the nine suffixes, "around 25%" and "around 50%", the
100 / 1,000 / 2,000 iteration figures; the "Figure 5.3" labelling inconsistency; §6's two further aspects;
§7's priority claim, its three named rivals with the paper's grounds, the summary of properties and the
stated main limitation; and the 25-entry reference list, which this side counted at the page during this
cross-check (seven entries begun in the left column, eighteen in the right) and found equal to the first
extract's count. **No table value and no numeric value differs between the two reads.**

**§9.3 Disagreements, each resolved at the page.**

- **(a) The first extract misquotes the worked example.** Its line 194–195 reads *"state 4 has almost never
  seen this observation; but regardless, state 4 has no choice but to pass all its mass…"*. **The page (2,
  §2, right column) reads *"but like state 1, state 4 has no choice but to pass all its mass…"*.** The
  paper goes against the first extract; *"regardless"* is not on the page. No value moves.
- **(b) The first extract drops a word from a quotation.** Its line 344 reads *"adjust the parameters of
  all the local classifiers"*. **The page (8, §7, left column top) reads *"all of the local
  classifiers"*.** The paper goes against the first extract. No value moves.
- **(c) A punctuation difference inside a quotation.** Its line 164 reads *"indeed CRFs share all of the
  convexity properties"*. **The page (4, §3, left column) reads *"indeed, CRFs share…"*.** The paper goes
  against the first extract by one comma. No value moves.
- **Against this (second) extract, this comparison found nothing the page contradicts.** That is a
  statement about what the comparison reached — the quotations both extracts carry and the values both
  transcribed — and not a claim that this extract is the better read; its own read-back struck and added
  things first (§8.1).

**§9.4 Things one read carries and the other does not, neither contradicted by the page.**

- The first extract quotes page 2's enumeration of the model classes subject to label bias (*"Classical
  probabilistic automata … are all potential victims of the label bias problem"*) and makes it the bound
  on its finding (4); this extract does not quote that sentence. Checked at the page: the first extract's
  quotation of it is exact.
- This extract records that decoding used Viterbi and that forward-backward decoding *"do[es] not
  significantly change"* the results (page 6), the second parameterisation sentence of §5.2, and the
  *"qualitatively the same over a range of sizes"* qualification; the first extract does not carry those
  three sentences.
- This extract's §4.4 derives relative reductions from Figure 4's cells and notes that CRF's oov error
  without spelling features (48.05%) is worse than the HMM's (45.99%); the first extract prints the cells
  and derives nothing from them.
- The first extract's record-facing half — its identity routing, its sweeps of the staged tree, its
  findings (2) to (16), its "what an L2 detail specification could adopt" section and its centrality
  verdict — **lies outside this cross-check** (entry 169 §5(vii)); none of those objects was opened, and
  nothing here confirms or challenges them.

**§9.5 What is done about (a) to (c), and what is not.** Step 8 of entry 169 §3 says to correct whichever
extract the paper goes against, at its site, former wording preserved. **The first extract is NOT edited
by this sitting.** Entry 186's Ruling 3 corrected row 46's first extract *"for row 46 ONLY"* and records the
same question for other rows as not ruled; entry 188 §4's ruling ("Option 2") did the same for row 15
only. Whether row 12's first extract is corrected at its three sites is therefore put to the user as a
decision, and until he rules the first extract stands as it is. **This file's statements above are the
record of the three sites either way.**

*(★ MADE STALE 2026-09-19 AND LEFT STANDING (#12): the user ruled Option 2 of entry 196 §2 — corrected, for
row 12 only — and the first extract was corrected at (a), (b) and (c) at its own sites, former wording
preserved, with a banner note recording the ruling. §9.3 above is the ground for each correction and is
unchanged. The class question for other rows is not ruled by it.)*

**§9.6 The independence bound, restated once.** Before the paper was opened this side had read: two
strings of the progress table's row-12 line (§0), the bibliography row, and the file names of both
first-extract files. It carried general knowledge of the method class, declared at §0. It had read no
summary of the paper's content from any record. The first extract was opened only after this file's §0–§8
were landed and proved.
