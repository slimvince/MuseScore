# Sha & Pereira 2003 — "Shallow Parsing with Conditional Random Fields" — SECOND INDEPENDENT EXTRACT

> **STATUS: READING-PASS EXTRACT, SECOND PASS. NOTHING HERE IS RULED.** Written 2026-09-19 by the Cowork
> session that booted on `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_six.md`,
> under `cowork_reading_pass_commission_2026_08_30.md` §4 (a CENTRAL source is extracted in a second
> independent pass and the two extracts cross-checked) and the eight-step order of handoff entry 169 §3,
> as amended at its naming point by Ruling 2 of entry 186 §2. **The paper is Task B, L2's slice, row 14**
> (row numbers are `reading_pass/candidacy_upgrades.md`'s). Held file:
> `docs/research_papers/sha_pereira_2003_naacl_shallow_parsing_crf.pdf`, 198,866 bytes at this session's
> staging call; **8 pages, established at the tool** by a deliberately out-of-range request (page 20
> refused with "PDF has 8 pages"). Read whole in two requests, pages 1–4 and 5–8; **every page image was
> present in both** (checked at the images, not at the call's success line).
>
> Page numbers below are the PDF's own (1–8). The paper's first page carries a proceedings header giving
> its printed pagination as pp. 134–141; that header is quoted at §1.3 and the PDF's own numbering is used
> everywhere else.

## §0 — Declarations of independence and its bound

- **What this side read before opening the paper, that bears on it:** the progress table
  `reading_pass/l2_slice_reading_progress.md` was searched for the owed rows' numbers, and **the whole
  row-14 line (line 100) was read**, including its identity cell, its grade cell, its centrality cell and
  its "Second pass" cell. That is a wider contamination than row 12's second extract declares (it read two
  strings of its row), and it is stated as such: this side read, before opening the paper, the first
  extract's centrality reasoning as the table summarises it, the table's statements about the printed
  header, the venue wording, the pagination, the absence of a licence line and the identity-match shape.
  The table line also names the task (NP chunking of English text on CoNLL-2000, with a development set
  from WSJ section 21). **None of that is a statement about the paper's method, its model or its
  results**, and none of it is relied on below; every claim in §2–§7 is located to a page or marked as
  this reader's derivation. `docs/research_papers/BIBLIOGRAPHY.md` line 28 was
  read (the row: authors, short title, venue, a URL, a held mark, and the tier CC (ACL Anthology)).
- **Name-only look-up, declared under Ruling 2 (entry 186 §2):** `reading_pass/extracts/` was listed by
  file name earlier in this sitting, for the row-12 act, and the listing was reused to find the first
  extract's name: `sha-pereira-2003-shallow-parsing-with-conditional-random-fields.md` (24,365 bytes,
  modification time 1789146130901). The progress table's row-14 line names the same path. **It was not
  opened before §9.** The file name carries author, year and the paper's own title, which the paper
  supplies.
- **Contamination from the record's own text about this paper, beyond the table line:** of the records
  read at boot (entries 196, 195, 188 at its head and §4–§5, 186, 169, 152 at (v)–(x), 118 at its
  bridge-fault section; `CLAUDE.md` at its six spans; `DECISIONS.md`; `STATUS.md`; the gating answer),
  none summarises this paper's content; entry 196 §3 names it as the next member with its file name and
  size. Row 12's second extract was read at §0–§1 (its form) and §9 (its cross-check), and row 12's first
  extract at three sites and its banner, for the row-12 act; row 12's paper is this paper's cited
  ancestor, and what this side knows of it from those reads is declared here. `FRAMEWORK.md`,
  `population.md`, the findings surface, the slice derivation and the candidacy file were **not** opened.
- **General knowledge is the larger contamination and is named as such:** this side knows conditional
  random fields, conjugate-gradient and quasi-Newton optimisation, and the CoNLL-2000 chunking task as
  method classes from outside this repository. **Every mechanism statement below is therefore located to
  a page**, and a statement this side could make from general knowledge but could not find on a page is
  written as ABSENT (§7), not as a fact.
- **What this file is not:** it is not a record-facing extract. What `FRAMEWORK.md` or any design point
  says about this paper, and the paper's centrality verdict, are the first extract's half and are not
  re-derived here (entry 169 §5(vii)).

## §1 — Identity, checked at page 1

- **§1.1 Title, as printed:** *"Shallow Parsing with Conditional Random Fields"* (page 1, head).
- **§1.2 Authors and affiliation, as printed:** Fei Sha and Fernando Pereira, Department of Computer and
  Information Science, University of Pennsylvania, 200 South 33rd Street, Philadelphia, PA 19104;
  e-mail `(feisha|pereira)@cis.upenn.edu` (page 1).
- **§1.3 Venue:** page 1 carries a header at its top right, in a typewriter face, reading
  *"Proceedings of HLT-NAACL 2003 / Main Papers , pp. 134-141 / Edmonton, May-June 2003"*. **The venue,
  year and pagination are therefore printed on the page.** No copyright line, no licence line and no
  per-page page numbers appear on the pages as rendered. The bibliography row (line 28) writes *"NAACL
  2003"* where the header prints *"HLT-NAACL 2003"*; recorded, not graded.
- **§1.4 Match to the bibliography row:** the row's title *"Shallow Parsing with Conditional Random
  Fields"* is the printed title in full; the authors match by name and order. **No identity finding.**
- **§1.5 Length and structure:** 8 pages. Sections as printed: Abstract; 1 Introduction; 2 Conditional
  Random Fields; 3 Training Methods (3.1 Preconditioned Conjugate Gradient; 3.2 Limited-Memory
  Quasi-Newton; 3.3 Voted Perceptron); 4 Shallow Parsing (4.1 Data Preparation; 4.2 CRFs for Shallow
  Parsing; 4.3 Parameter Tuning; 4.4 Evaluation Metric; 4.5 Significance Tests); 5 Results (5.1 F
  Scores; 5.2 Convergence Speed; 5.3 Labeling Accuracy); 6 Conclusions; Acknowledgments; References.
  Figures 1–3 (Figure 2 in two panels (a) and (b)); Tables 1–4; two footnotes; equations numbered (1) to
  (4). The reference list was counted at page 8 during this read: seventeen entries begun in the left
  column and eighteen in the right, thirty-five in all.

## §2 — Claims, labeled

The labels are the commission's: **FACT** = stated or measured in the paper, with its location;
**THEORY** = established published theory the paper invokes; **CONJECTURE** = the paper's own
speculation, or a claim it makes without a measurement or a citation. Quotations are verbatim from the
page as rendered.

### §2.1 The problem the paper sets, and its headline claim (Abstract and §1, pages 1–2)

- **[FACT, p. 1 Abstract]** The paper's own summary: *"We show here how to train a conditional random
  field to achieve performance as good as any reported base noun-phrase chunking method on the CoNLL
  task, and better than any reported single model. Improved training methods based on modern
  optimization algorithms were critical in achieving these results."*
- **[FACT, p. 1 §1]** The task: NP chunking, *"which finds the non-recursive cores of noun phrases
  called base NPs"*, introduced as a machine-learning problem by Ramshaw and Marcus (1995) and extended
  by the CoNLL-2000 shared task (Tjong Kim Sang and Buchholz, 2000), *"which is now the standard
  evaluation task for shallow parsing."*
- **[FACT, p. 1 §1]** The two prior approaches the paper positions itself against: *k*-order
  generative models of paired input and label sequences (HMMs; multilevel Markov models), and *"a
  sequence of classification problems, one for each of the labels in the sequence"*, where the result
  at each position *"may depend on the whole input and on the previous k classifications."*
- **[FACT, p. 1 §1]** The paper's stated defect of generative models: *"effective generative models
  require stringent conditional independence assumptions"*; non-independent features of the inputs
  *"are important in dealing with words unseen in training, but they are difficult to represent in
  generative models."*
- **[FACT, pp. 1–2 §1]** The paper's stated merit and defect of sequential classifiers: they handle
  correlated features and *"are trained to minimize some function related to labeling error, leading
  to smaller error in practice if enough training data are available. In contrast, generative models
  are trained to maximize the joint probability of the training data, which is not as closely tied to
  the accuracy metrics of interest if the actual data was not generated by the model, as is always the
  case in practice."* But: *"since sequential classifiers are trained to make the best local decision,
  unlike generative models they cannot trade off decisions at different positions against each other.
  In other words, sequential classifiers are myopic about the impact of their current decision on later
  decisions (Bottou, 1991; Lafferty et al., 2001)."*
- **[FACT, p. 2 §1]** The paper's positioning of CRFs: *"Conditional random fields (CRFs) bring
  together the best of generative and classification models. Like classification models, they can
  accommodate many statistically correlated features of the inputs, and they are trained
  discriminatively. But like generative models, they can trade off decisions at different sequence
  positions to obtain a globally optimal labeling."*
- **[FACT, p. 2 §1]** The headline result, as stated: *"CRFs beat all reported single-model NP
  chunking results on the standard evaluation dataset, and are statistically indistinguishable from
  the previous best performer, a voting arrangement of 24 forward- and backward-looking support-vector
  classifiers (Kudo and Matsumoto, 2001)."* And what it took: *"we had to abandon the original
  iterative scaling CRF training algorithm for convex optimization algorithms with better convergence
  properties."*
- **[CONJECTURE, p. 2 §1]** *"The generalized perceptron proposed by Collins (2002) is closely
  related to CRFs, but the best CRF training methods seem to have a slight edge over the generalized
  perceptron."* — "seem to" is the paper's own hedge; the measured comparison is at §4 below.

### §2.2 The model (§2, pages 2–3)

- **[THEORY, p. 2 §2]** The CRF, as the paper defines it: for input sequence **x** = x₁…xₙ and label
  sequence **y** = y₁…yₙ of the same length, a CRF is specified by a vector **f** of local features and
  a weight vector **λ**; each local feature is a state feature s(y, **x**, i) or a transition feature
  t(y, y′, **x**, i). The global feature vector is **F**(**y**, **x**) = Σᵢ **f**(**y**, **x**, i), and
  the conditional distribution is p_λ(**Y**|**X**) = exp(**λ**·**F**(**Y**, **X**)) / Z_λ(**X**)
  (equation (1)), with Z_λ(**x**) = Σ_y exp(**λ**·**F**(**y**, **x**)). Features *"may also depend on
  global properties of the input, or be non-zero only at some positions, for instance features that
  pick out the first or last labels."*
- **[THEORY, p. 2 §2]** The representational claim, with its citation: *"Any positive conditional
  distribution p(Y|X) that obeys the Markov property … can be written in the form (1) for appropriate
  choice of feature functions and weight vector (Hammersley and Clifford, 1971)."*
- **[THEORY, p. 2 §2]** Decoding: ŷ = argmax_y p_λ(**y**|**x**) = argmax_y **λ**·**F**(**y**, **x**),
  *"because Z_λ(x) does not depend on y. F(y, x) decomposes into a sum of terms for consecutive pairs
  of labels, so the most likely y can be found with the Viterbi algorithm."*
- **[THEORY, pp. 2–3 §2]** Training maximises the log-likelihood L_λ = Σ_k [**λ**·**F**(**y**_k,
  **x**_k) − log Z_λ(**x**_k)]; its gradient (equation (2)) is Σ_k [**F**(**y**_k, **x**_k) −
  E_{p_λ(Y|x_k)} **F**(**Y**, **x**_k)]. *"In words, the maximum of the training data likelihood is
  reached when the empirical average of the global feature vector equals its model expectation."* The
  expectation is computed by a variant of the forward–backward algorithm over the per-position
  transition matrix M_i[y, y′] = exp(**λ**·**f**(y, y′, **x**, i)), with Z_λ(**x**) = α_n · **1**ᵀ.
- **[FACT, p. 3 §2]** Regularisation: *"To avoid overfitting, we penalize the likelihood with a
  spherical Gaussian weight prior (Chen and Rosenfeld, 1999)"*, giving L′_λ = L_λ − ‖**λ**‖²/(2σ²) +
  const and a gradient with the extra term −**λ**/σ².

### §2.3 Training methods (§3, pages 3–4)

- **[FACT, p. 3 §3]** Why iterative scaling was abandoned: the original CRF training used iterative
  scaling, which is *"very simple and guaranteed to converge, but as Minka (2001) and Malouf (2002)
  showed for classification, their convergence is much slower than that of general-purpose convex
  optimization algorithms when many correlated features are involved."*
- **[FACT, p. 3 §3]** The paper's own claim about scale: *"Our work shows that preconditioned
  conjugate-gradient (CG) (Shewchuk, 1994) or limited-memory quasi-Newton (L-BFGS) (Nocedal and Wright,
  1999) perform comparably on very large problems (around 3.8 million features)."* Concurrent work by
  Wallach (2002) tested CG and second-order methods *"on a small shallow parsing problem"*.
- **[FACT, p. 3 §3]** The compared trainers: preconditioned CG, generalized iterative scaling (GIS;
  Darroch and Ratcliff, 1972), non-preconditioned CG, and voted perceptron (Collins, 2002). *"All
  algorithms except voted perceptron maximize the penalized log-likelihood"*.
- **[FACT, pp. 3–4 §3.1]** The preconditioner: the inverse Hessian is the ideal preconditioner but is
  *"not applicable to CRFs for two reasons. First, the size of the Hessian is dim(λ)², leading to
  unacceptable space and time requirements for the inversion"*; second, every Hessian element involves
  the expectation of a product of global feature values, and *"computing those expectations is
  quadratic in sequence length, as the forward-backward algorithm can only compute expectations of
  quantities that are additive along label sequences."* The paper's remedy: discard the off-diagonal
  terms and approximate the expectation of the square of a global feature by the expectation of the sum
  of squares of the corresponding local features at each position. *"If this approximation is
  semidefinite, which is trivial to check, its inverse is an excellent preconditioner for early
  iterations of CG training. However, when the model is close to the maximum, the approximation becomes
  unstable, which is not surprising since it is based on feature independence assumptions that become
  invalid as the weights of interaction features move away from zero. Therefore, we disable the
  preconditioner after a certain number of iterations, determined from held-out data. We call this
  strategy mixed CG training."*
- **[FACT, p. 4 §3.2]** L-BFGS: a second-order method estimating curvature from previous gradients
  and updates. *"There is no theoretical guidance on how much information from previous steps we should
  keep to obtain sufficiently accurate curvature estimates. In our experiments, storing 3 to 10 pairs of
  previous gradients and updates worked well, so the extra memory required over preconditioned CG was
  modest."*
- **[FACT, p. 4 §3.3]** Voted perceptron (Collins, 2002): the update λ_{t+1} = λ_t + **F**(**y**_k,
  **x**_k) − **F**(ŷ_k, **x**_k) (equation (3)), ŷ_k the Viterbi path under λ_t; the voted variant
  averages the λ_t. *"Collins (2002) reported and we confirmed that this averaging reduces overfitting
  considerably."*

### §2.4 The chunking model and its features (§4, pages 4–5)

- **[FACT, p. 4 §4]** Labels: each word is labelled O (outside a chunk), B (starts a chunk) or I
  (continues a chunk); the first line of Figure 1 is labelled BIIBIIOBOBIIO.
- **[FACT, p. 4 §4.1]** Data: the RM data set of Ramshaw and Marcus (1995) and the CoNLL-2000 version
  of Tjong Kim Sang and Buchholz (2000). *"Although the chunk tags in the RM and CoNLL-2000 are somewhat
  different, we found no significant accuracy differences between models trained on these two data
  sets. Therefore, all our results are reported on the CoNLL-2000 data set."* A development test set,
  provided by Michael Collins, derived from WSJ section 21 tagged with the Brill (1995) POS tagger.
- **[FACT, p. 4 §4.2]** The Markov order and how it is obtained: *"Our chunking CRFs have a
  second-order Markov dependency between chunk tags. This is easily encoded by making the CRF labels
  pairs of consecutive chunk tags. That is, the label at position i is y_i = c_{i−1}c_i, where c_i is
  the chunk tag of word i, one of O, B, or I."* OI is impossible; the constraints y_{i−1} = c_{i−2}c_{i−1},
  y_i = c_{i−1}c_i, c₀ = O *"are enforced by giving appropriate features a weight of −∞, forcing all the
  forbidden labelings to have zero probability."*
- **[FACT, p. 4 §4.2]** Feature selection: *"Our choice of features was mainly governed by computing
  power, since we do not use feature selection and all features are used in training and testing."*
- **[FACT, pp. 4–5 §4.2]** The factored feature form (equation (4)): f(y_{i−1}, y_i, **x**, i) =
  p(**x**, i) q(y_{i−1}, y_i), a predicate on the input at the position times a predicate on the label
  pair; *"Because the label set is finite, such a factoring of f(y_{i−1}, y_i, x, i) is always
  possible, and it allows each input predicate to be evaluated just once for many features that use it,
  making it possible to work with millions of features on large training sets."*
- **[FACT, p. 5 §4.2 and Table 1]** The feature set: Table 1 lists the label predicates q (y_i = y;
  y_i = y and y_{i−1} = y′; c(y_i) = c) and the input predicates p (true; the word at offsets −2 to +2;
  word pairs at (−1, 0) and (0, +1); the POS tag at offsets −2 to +2; tag pairs at (−2, −1), (−1, 0),
  (0, +1), (+1, +2); tag triples at (−2, −1, 0), (−1, 0, +1), (0, +1, +2)), with the second block of q
  paired with the second block of p. *"The use of chunk tags as well as labels provides a form of
  backoff from the very small feature counts that may arise in a second-order model, while allowing
  significant associations between tag pairs and input predicates to be modeled."*
- **[FACT, p. 5 §4.2]** Two feature-set sizes: *"we used only the 820,000 features that are
  supported in the CoNLL training set, that is, the features that are on at least once. For our highest
  F score, we used the complete feature set, around 3.8 million in the CoNLL training set, which
  contains all the features whose predicate is on at least once in the training set. The complete
  feature set may in principle perform better because it can place negative weights on transitions that
  should be discouraged if a given predicate is on."*

### §2.5 Tuning, metric and significance (§4.3–§4.5, page 5)

- **[FACT, p. 5 §4.3]** *"We also need to choose the number of training iterations since we found
  that the best F score is attained while the log-likelihood is still improving. The reasons for this
  are not clear, but the Gaussian prior may not be enough to keep the optimization from making weight
  adjustments that slighly improve training log-likelihood but cause large F score fluctuations."*
  (The page prints *"slighly"*.) The development set is used to set the prior and the iteration count.
- **[FACT, p. 5 §4.4]** The metric: precision P (fraction of output chunks that exactly match the
  reference chunks), recall R (fraction of reference chunks returned), F₁ = 2·P·R/(P + R). *"The
  relationships between F score and labeling error or log-likelihood are not direct, so we report both
  F score and the other metrics for the models we tested."*
- **[FACT, p. 5 §4.5]** Significance: McNemar's test on labeling disagreements is used, because
  *"bootstrap variances in preliminary experiments were too high to allow any conclusions"*. The
  paper also says of the field: *"reported results sometimes leave out details needed for accurate
  comparisons."*

### §2.6 Conclusions (§6, page 7)

- **[FACT, p. 7 §6]** *"We have shown that (log-)linear sequence labeling models trained
  discriminatively with general-purpose optimization methods are a simple, competitive solution to
  learning shallow parsers. These models combine the best features of generative finite-state models
  and discriminative (log-)linear classifiers, and do NP chunking as well as or better than 'ad hoc'
  classifier combinations, which were the most accurate approach until now."*
- **[CONJECTURE, p. 7 §6]** *"There is no reason why the same techniques cannot be used equally
  successfully for other types or for other related tasks, such as POS tagging or named-entity
  recognition."* And on parsing: log-linear parsing models *"have the potential to supplant the
  currently dominant lexicalized PCFG models"*, *"avoiding the label bias problem that may have
  hindered earlier classifier-based parsers (Ratnaparkhi, 1997)"* — stated as potential, with the
  algorithmic challenges named and no measurement.

## §3 — Coupling facts (mandatory)

- **What it assumes upstream:** tokenised English text with a part-of-speech tag per word, the tags
  supplied by an automatic tagger (the development set is tagged with the Brill tagger, p. 4 §4.1; the
  CoNLL-2000 data's own tagging is not described in the pages). The input predicates read words and
  tags at offsets −2 to +2 (Table 1); no other input is named in Table 1 or in §4.2.
- **What it hands downstream:** one chunk tag per word from {O, B, I}, decoded as the single most
  probable label sequence by Viterbi (p. 2 §2). The paper reports no posterior marginals, no n-best
  list and no confidence per position; the model is a distribution over whole label sequences but only
  its argmax is used or evaluated in the pages.
- **Its stated scope:** base-NP chunking of English newswire (CoNLL-2000, WSJ), with a second-order
  label dependency, a fixed hand-listed feature set, one Gaussian prior width σ = 1.0 for the runtime
  comparison (p. 6 §5.2), and a development set for the prior and the iteration count. The conclusions
  extend the claim to other phrase types and tasks as a stated expectation, not a result (§2.6).
- **What is coupled to what:** the F score is not the training objective — the objective is penalised
  log-likelihood — and the paper says in terms that the best F score is reached before the likelihood
  stops improving (p. 5 §4.3) and that *"there is no direct relationship between F scores and
  log-likelihood"* while *"in these experiments F score tends to follow log-likelihood"* (p. 6 §5.2).
- **What the training method decides and what it does not:** the trainer is a choice among ways to
  reach the same objective's maximum (all but voted perceptron maximise L′_λ, p. 3 §3); Table 3 shows
  the trainers reaching different F scores at the target likelihood, and footnote 2 records that the
  method with the highest penalised likelihood (L-BFGS) has a lower data likelihood than the two CG
  variants. So the objective's maximum is not what the F scores are measured at, and the trainer choice
  is entangled with the stopping rule.

## §4 — Measured results, as the paper states them

- **§4.1 Hardware and implementation (p. 6 §5):** a Java implementation of CRFs *"designed to handle
  millions of features"*, on 1.7 GHz Pentium IV processors with Linux and IBM Java 1.3.0. Voted
  perceptron and MEMMs are *"minor variants"* with the same feature encoding.
- **§4.2 Table 2, NP chunking F scores (p. 6), as printed:**

  | Model | F score |
  |---|---|
  | SVM combination (Kudo and Matsumoto, 2001) | 94.39% |
  | CRF | 94.38% |
  | Generalized winnow (Zhang et al., 2002) | 93.89% |
  | Voted perceptron | 94.09% |
  | MEMM | 93.70% |

  The text beside it (p. 6 §5.1): the CRF row is *"our best model, with the complete set of 3.8 million
  features"*; the MEMM row is an MEMM *"trained with the mixed CG method using an approximate
  preconditioner"*; the published voted-perceptron F score is 93.53% *"with a different feature set
  (Collins, 2002)"*, the 94.09% here being *"for the supported feature set; the complete feature set
  gives a slightly lower score of 94.07%"*; and *"Zhang et al. (2002) reported a higher F score (94.38%)
  with generalized winnow using additional linguistic features that were not available to us."* **So
  the table's 93.89% for generalized winnow is not that paper's best published figure; the paper
  states the higher one in the text beside the table.**
- **§4.3 Table 3, runtime for various training methods (p. 6), as printed** — time in minutes to
  reach a target penalised log-likelihood, with prior σ = 1.0, on the 820,000 supported features:

  | training method | time | F score | L′_λ |
  |---|---|---|---|
  | Precond. CG | 130 | 94.19% | −2968 |
  | Mixed CG | 540 | 94.20% | −2990 |
  | Plain CG | 648 | 94.04% | −2967 |
  | L-BFGS | 84 | 94.19% | −2948 |
  | GIS | 3700 | 93.55% | −5668 |

  The text (p. 6 §5.2): *"GIS is the only method that failed to reach the target, after 3,700
  iterations"* — so the GIS row's 3700 is an iteration count at which it had not reached the target,
  where the other rows are minutes to the target; the table's column heading says *"time"* for all
  five rows and the text is what distinguishes them. Voted perceptron is absent from the table *"as it
  does not optimize log-likelihood and does not use a prior"*; *"it reaches a fairly good F-score above
  93% in just two training sweeps, but after that it improves more slowly, to a somewhat lower score,
  than preconditioned CG training."*
- **§4.4 Table 4, McNemar's tests on labeling disagreements (p. 6), as printed:**

  | null hypothesis | p-value |
  |---|---|
  | CRF vs. SVM | 0.469 |
  | CRF vs. MEMM | 0.00109 |
  | CRF vs. voted perceptron | 0.116 |
  | MEMM vs. voted perceptron | 0.0734 |

  The text (p. 7 §5.3): *"These tests suggest that MEMMs are significantly less accurate, but that
  there are no significant differences in accuracy among the other models."* The test is on labelling
  decisions, not on F scores (p. 5 §4.5; p. 6 §5.3: labelling accuracy *"is over-optimistic as an
  accuracy measure for shallow parsing"*, with the example that a chunk BIIIIIII labelled OIIIIIII
  scores 87.5% labelling accuracy and recall 0).
- **§4.5 Convergence (p. 6 §5.2, Figures 2a, 2b and 3):** each CG iteration involves a line search
  that *"may require several forward-backward procedures (typically between 4 and 5 in our
  experiments)"*; penalised log-likelihood is plotted against the number of forward–backward
  evaluations; the objective *"achieves close proximity to the maximum in a few iterations (typically
  10)"*; GIS *"increases L′_λ rather slowly, never reaching the value achieved by CG"*; mixed CG
  *"converges slightly more slowly than preconditioned CG"*; plain CG *"converges much more slowly
  than both preconditioned CG and mixed CG training. However, it is still much faster than GIS."*
  Figure 2a's x-axis is ticked from 6 to 256 forward–backward evaluations, Figure 2b's and Figure 3's
  from 0 to 500; the y-axis of Figure 3 is F score from 0.45 to 0.95. The paper attributes the CG advantage to
  approximate second-order information, *"confirmed by the performance of L-BFGS, which also uses
  approximate second-order information."*
- **§4.6 Derived here, not printed:** the spread of Table 2's five F scores is 94.39 − 93.70 = 0.69
  points; the CRF–SVM difference is 0.01 points, which Table 4 grades as not significant (p = 0.469).
  In Table 3, the two trainers with equal F score (94.19%) differ in time by a factor of 130/84 ≈ 1.5,
  and the best F score in that table (mixed CG, 94.20%) is at the lowest penalised likelihood of the
  four that reached the target (−2990 against −2968, −2967 and −2948). These are this reader's arithmetic over printed cells.

## §5 — What the paper states about uncertainty, reproducibility and ground truth (against #24, #16, #21)

- **Uncertainty:** no F score in Tables 2 or 3 carries a spread, a standard error or a repeat count;
  each is one figure. The uncertainty statement the paper does make is Table 4's McNemar p-values on
  labelling disagreements, and the paper's own reason for not reporting bootstrap variances on F is
  that they *"were too high to allow any conclusions"* (p. 5 §4.5). The paper also says in terms that
  F score *"fluctuations"* occur late in training (p. 5 §4.3).
- **Reproducibility:** hardware, JVM, data set, feature set sizes, prior width for the runtime
  comparison, and the 3-to-10-pair L-BFGS memory are stated; the number of preconditioned iterations
  before the mixed-CG switch is *"determined from held-out data"* and its value is not printed; the
  prior width used for the Table 2 best model is not printed on the pages as read; the feature-set
  distinction (supported 820,000 versus complete 3.8 million) is stated per experiment.
- **Ground truth:** the CoNLL-2000 chunk annotations are used as given; the paper reports no
  inter-annotator agreement and no error rate for the reference chunks, and states that RM and
  CoNLL-2000 tags differ *"somewhat"* with no significant effect on the models (p. 4 §4.1). The POS
  tags of the development set are automatically produced (Brill tagger), so one input is itself a
  model's output; the paper does not discuss this.

## §6 — Terms the paper uses, in the paper's sense

- **Shallow parsing / NP chunking:** identifying non-recursive cores of noun phrases (base NPs); the
  chunker labels each word O, B or I (p. 1 §1; p. 4 §4).
- **State feature / transition feature; global feature vector:** as at §2.2, the paper's own
  definitions (p. 2 §2).
- **Supported features:** features that are on at least once in the training set (820,000);
  **complete feature set:** all features whose input predicate is on at least once (about 3.8
  million) (p. 5 §4.2).
- **Mixed CG training:** preconditioned CG with the preconditioner disabled after a held-out-chosen
  number of iterations (p. 4 §3.1).
- **F score:** F₁ = 2PR/(P + R) over chunks, called *"just F score in what follows"* (p. 5 §4.4).

## §7 — Stated ABSENT: things a reader might supply from the method class that the pages do not say

- **No per-position confidence, marginal or n-best output.** The model is a distribution over label
  sequences; the pages use and evaluate only the Viterbi argmax.
- **No feature selection and no feature-weight inspection.** The paper says so in terms for selection
  (p. 4 §4.2); no weights are reported.
- **No statement of the prior width behind Table 2**, and no printed value for the mixed-CG switch
  point; both are set on held-out data (pp. 4–5).
- **No run-to-run variation.** No reported figure carries a repeat count or a spread; the one
  repetition statement is
  that the F score is attained *"while the log-likelihood is still improving"* and fluctuates late.
- **No third-order or higher model, and no comparison of Markov orders.** The second order is stated
  as the design (p. 4 §4.2) with no measured alternative on the pages.
- **No mention of segment-level (semi-Markov) modelling, of duration, or of any score normalisation
  beyond the global partition function Z_λ(x).** The chunk is expressed only through per-word tags.
- **Nothing musical.** A note, chord, key, score or corpus of music is met nowhere in the eight pages
  as read; every claim carried out of this paper into a musical setting crosses a domain boundary and
  must say so at the point of use.

## §8 — The read-back and the sweep (steps 4 and 5 of entry 169 §3), written after the text above was finished

**§8.1 The read-back against the pages.** Every quotation in §2, §3, §4 and §5 was re-read at its
page image (the images from this session's two requests, still in the session), and every cell of
Tables 2, 3 and 4 and every predicate of Table 1 was re-checked. The quotations stood. **What the
read-back found in this side's own text, corrected before this section was added:**
- §4.6 said the best Table 3 F score sat at the *"second-lowest"* penalised likelihood of the four
  trainers that reached the target; −2990 is the lowest of the four. Corrected, with the four values
  printed beside it.
- §4.5 said Figure 2a's x-axis *"runs to about 300"*; its printed ticks run from 6 to 256. Corrected
  to the ticks as printed.
- §0 said the progress table's row-14 line contained nothing about the paper's data; it names the
  task and the data set. Corrected; the claim now reaches method, model and results only.

**§8.2 The sweep for absolutes.** Every hit on *every, all, none, never, nowhere, only, no, complete,
exhaustive, independent, first, always, whole* was read at its line. Hits inside quotations are the
paper's and stand. This side's own hits were bounded where they were not already: §3's *"Nothing else
is read"* became *"no other input is named in Table 1 or in §4.2"*; §7's *"The eight pages contain no
note…"* became a reader's negative, *"met nowhere in the eight pages as read"*; §7's *"Every reported
figure is one run"* became *"No reported figure carries a repeat count or a spread"*, which is what
the pages support. The remaining absolutes of this side's own are each tied to an act named beside
them: the page images (both requests), the reference count (page 8, counted this read), the absence
of copyright, licence and page-number lines (the eight images, *"as rendered"*), and the §7 absents
(negatives over the pages as read, which is what §7's heading says they are).

**§8.3 Mechanism supplied from general knowledge, checked.** Each mechanism statement in §2.2–§2.3 was
checked for a page location. Two places were this side's gloss rather than the page's words and are
marked as such: §3's fourth and fifth bullets (the coupling of trainer, stopping rule and F score,
and the L-BFGS footnote reading) are this reader's reading of pages 5–6, built from quoted sentences,
and §4.6 is arithmetic over printed cells. Nothing in §2 rests on a mechanism the pages do not state.

**§8.4 What the read-back did not do.** It did not open the first extract (that is step 7, §9). It
did not re-request any page from the tool; it re-read the images already returned. It did not check
the CoNLL-2000 or RM data sets, the cited works, or the anthology URL. Whether this extract is a
better read than the first is not a question this section answers.

## §9 — The cross-check against the first extract (step 7 of entry 169 §3), written after §0–§8 had landed

**§9.1 What was read, and when.** This file was landed and proved (34,985 bytes, modification time
1789770853850, last content line 436 read) **before** the first extract was opened. Then
`reading_pass/extracts/sha-pereira-2003-shallow-parsing-with-conditional-random-fields.md` (24,365
bytes, modification time 1789146130901 — the file the progress table names; its banner dates it to the
sitting of 2026-09-08 to 2026-09-11, with a fact-check of 2026-09-11 recorded at its §8) was staged and
read **whole**, 335 lines, in one call. Every disagreement below was resolved **at the page image
already in this session**, re-read at the sentence.

**§9.2 Agreements, named.** The two reads agree on: the held file's size and its eight pages; the
printed title, both authors, the affiliation and the proceedings header with its venue, year and
pagination; the venue wording difference against the bibliography row (HLT-NAACL against NAACL),
recorded and not graded by either; the absence of a licence line; the O/B/I labelling and the
second-order label pairing with OI impossible and forbidden labellings forced to zero by a weight of
−∞; the factored feature form; the three trainers and the abandonment of iterative scaling; the
spherical Gaussian prior with its citation; mixed CG training and its held-out switch; L-BFGS's three to
ten stored pairs; the development set from WSJ section 21 tagged by the Brill tagger; the 820,000
supported and about 3.8 million complete features; the prior and the iteration count both set on the
development set; the F₁ definition; McNemar's test and the bootstrap sentence; **every one of Table
2's five F scores** (94.39, 94.38, 93.89, 94.09, 93.70) and the text's 93.53 and 94.07; **every cell
of Table 3** (130 / 94.19 / −2968; 540 / 94.20 / −2990; 648 / 94.04 / −2967; 84 / 94.19 / −2948; 3700 /
93.55 / −5668) and σ = 1.0; **every one of Table 4's four p-values** (0.469, 0.00109, 0.116, 0.0734)
and the authors' reading of them; footnote 2; the 87.5% / recall 0 example; the *"no direct
relationship"* sentence and the *"tends to follow"* qualification; and the domain bound. **No table
value and no numeric value differs between the two reads.**

**§9.3 Disagreements, each resolved at the page.**

- **(a) A dash inside a quotation of the page header.** The first extract's lines 42–43 render the
  header in italics as *"pp. 134–141"* with an en dash; **the page (1, header) prints a hyphen,
  *"pp. 134-141"*.** The paper goes against the first extract by one character of punctuation, of a
  typographic kind; whether a dash normalisation inside a quotation counts as a misquotation is not
  settled by anything this side read. No value moves.
- **(b) A misprint of the page silently normalised inside a quotation.** The first extract's line 232,
  inside a quotation from §4.3, reads *"weight adjustments that slightly improve training
  log-likelihood"*; **the page (5, §4.3) prints *"slighly"*.** This extract quotes the page as printed
  and marks the misprint (§2.5). The paper goes against the first extract's quotation by one letter,
  in the direction of correcting the page; no value moves.
- **(c) A statement wider than the page, outside a quotation.** The first extract's §9 (lines
  310–311) says *"with iterative scaling failing to reach the target at all"*. **The page (6, §5.2)
  says GIS *"failed to reach the target, after 3,700 iterations"* and, of the theory, that *"GIS would
  eventually converge to the L′_λ optimum, but in practice convergence may be so slow that L′_λ
  improvements may fall below numerical accuracy, falsely indicating convergence."*** The first
  extract's own §6(2) carries the hedge (*"may fail to reach the target at all"*); its §9 drops it. No
  value moves.
- **Against this (second) extract, this comparison found nothing the page contradicts.** That is a
  statement about what the comparison reached — the quotations both extracts carry and the values
  both transcribed — and not a claim that this extract is the better read; its own read-back struck and
  corrected things first (§8.1).

**§9.4 Things one read carries and the other does not, neither contradicted by the page.**

- This extract carries Table 1's predicates, the §3.1 preconditioner mechanism in the paper's words,
  the Hammersley–Clifford representational statement, the Viterbi decoding sentence, the reference
  count (thirty-five, counted at page 8), the figure axes, and the derived arithmetic of §4.6; the
  first extract carries none of these.
- The first extract carries the paper's place against DP-C and DP-P, its findings (1) to (7), its
  three sweeps and ten whole readings, and its centrality verdict — its record-facing half, which
  **lies outside this cross-check** (entry 169 §5(vii)); none of those objects was opened, and nothing
  here confirms or challenges them. Its finding (3) quotes the same §4.3 sentence this extract
  quotes at §2.5 and reads it as an instance of the premise DP-P rests on; that reading is not
  checked here.
- The first extract's §8 records its own fact-check of 2026-09-11 and three corrections; this
  extract records its own read-back at §8. Neither bears on the other.

**§9.5 What is done about (a) to (c), and what is not.** Step 8 of entry 169 §3 says to correct
whichever extract the paper goes against, at its site, former wording preserved. **The first extract is
NOT edited by this sitting.** Entry 186's Ruling 3 (row 46), entry 188 §4's ruling (row 15) and the
ruling of 2026-09-19 on entry 196 §2 (row 12) were each for that row only and each records the class
question as not ruled. Whether row 14's first extract is corrected at its three sites is therefore put
to the user as a decision, and until he rules the first extract stands as it is. **This file's
statements above are the record of the three sites either way.** Of the three, (a) is typographic and
(b) corrects a misprint of the page; the user may reasonably rule them differently from (c).

*(★ MADE STALE 2026-09-19 AND LEFT STANDING (#12): the user ruled Option 2 of entry 197 §3 — corrected, all
three sites, for row 14 only — and the first extract was corrected at (a), (b) and (c) at its own sites,
former wording preserved, with a banner note recording the ruling. §9.3 above is the ground for each
correction and is unchanged. The class question for other rows is not ruled by it.)*

**§9.6 The independence bound, restated once.** Before the paper was opened this side had read: the
whole row-14 line of the progress table (§0, declared as the wider contamination), the bibliography
row, the file name of the first extract, and row 12's two extracts at the sites named in §0. It
carried general knowledge of the method class, declared at §0. It had read no summary of this paper's
method or results from any record. The first extract was opened only after this file's §0–§8 were
landed and proved.
