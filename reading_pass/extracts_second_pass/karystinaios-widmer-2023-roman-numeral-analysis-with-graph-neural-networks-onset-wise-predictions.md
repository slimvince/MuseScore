# Second extraction — Karystinaios & Widmer, "Roman Numeral Analysis with Graph Neural Networks: Onset-wise Predictions from Note-wise Features"

**WHAT THIS FILE IS.** The SECOND independent extraction of Task B's L2-slice row 49, written under
`cowork_reading_pass_commission_2026_08_30.md` §4's fourth bullet, which requires a CENTRAL source to be
extracted in a second independent pass that does not consult the first extract, the two extracts then
cross-checked, and disagreements resolved at the paper or recorded as unresolved.

**THE PAPER IS THE SOURCE OF EVERY VALUE OF THE PAPER BELOW.** No figure, table cell, quotation or
protocol constant attributed to this paper is taken from any other document. Where a statement in this
file comes from somewhere other than the paper, that is said at the statement — and there are three such
places, named here so the opening sentence is not read wider than it is true: **the held file's byte size**
(this side's own staging call and its own directory listing, §0), **the candidacy row transcribed in §0**,
and **one date from this project's own bibliography, quoted beside the paper's in §7.4**.

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**THE PAPER IS THE ONLY SOURCE FOR EVERY
VALUE BELOW.**" — **an absolute over this file that this file's own §0 and §7.4 refute**, three values
in it coming from elsewhere and being marked as such at their sites.)*

**LOCATION CONVENTION.** This document prints NO page numbers of its own. It is the arXiv copy
(`arXiv:2307.03544v2 [cs.SD] 12 Jul 2023`, stamped in the left margin of its first page), not the
proceedings copy, so there is no proceedings pagination to cite. Every location in this file is therefore
given as **the paper's own section number together with the PDF page as the reading tool delivers it** —
written as, for example, "§5.1, PDF page 5". A reader with the proceedings copy will have different page
numbers; the section numbers are the paper's own and are stable.

---

## §0 — What was read, and the bound on this read's independence

**READ AT THE OBJECT, BY THIS SIDE, THIS SITTING.** The held file
`docs/research_papers/chordgnn_2023_arxiv.pdf`, **1,933,753 bytes**, established at this side's own
staging call and again at its own non-recursive listing of `docs/research_papers/`. **Eight pages**,
established AT THE TOOL by a deliberately out-of-range page request, which answered *"PDF has 8 pages"*.
**All eight pages were read whole**, as two image requests of four pages each, and **every image was
checked for presence and legibility at the image itself and not at the call's success line** (the standing
page-image fault).

**NOTHING ELSE ABOUT THIS PAPER WAS READ ANYWHERE.** No sweep of this repository was run for this paper —
not for its authors, not for its title, not for its model name, not for any of its values. **This side
therefore asserts NOTHING about what this project's record says of this paper**, and takes no position on
any claim the first extract makes about the record. `FRAMEWORK.md` was not opened at any point.
`reading_pass/l2_slice_reading_progress.md` was not opened at any point. The first extract was not opened
before §9 of this file.

**★ THE INDEPENDENCE BOUND, DECLARED EXACTLY RATHER THAN CLAIMED AWAY** (the hundred-and-sixty-ninth
entry's §3, which says a booting session's contamination must be written down). Three things reached this
side before the paper was opened, and each is named here so a later reader can discount this read by
exactly what it knew:

1. **The handoff entry that booted this session** carries no content of this paper at all. Row 49 appears
   in it as a row number and nothing else.
2. **`reading_pass/candidacy_upgrades.md` was opened at rows 45 to 52**, to establish which paper row 49
   is — no entry of the handoff line names it. That row reads `| 49 | ChordGNN, ISMIR 2023 | ✓ |
   **ADMITTED** | V8's onset-level representation, and the learned coherence pass of DP-A's .462→.491. |`.
   **So this side knew, before opening the paper, that the record values this paper for an onset-level
   representation and for a learned coherence pass.** That is content contamination and it is carried into
   this read knowingly. **The verdict on that row is the CANDIDACY verdict — whether the paper is admitted
   to the reading population — and NOT the first extract's own grading**, which the record places in the
   progress record, unopened here.
3. **`docs/research_papers/BIBLIOGRAPHY.md` was read**, which prints for this paper only the bare line
   `ChordGNN, ISMIR 2023` with a URL, a local mark and a redistribution tier. It names no author and no
   title.

**NOT read, not searched, not staged:** the first extract (before §9), `FRAMEWORK.md`, the progress
record, `population.md`, the slice derivation, the findings surface, either commission, `OPEN_ITEMS.md`,
`ARCHITECTURE.md`, and every other paper.

**★ A NAMING DEPARTURE, DECLARED BECAUSE IT IS ONE AND BECAUSE IT COULD NOT HAVE BEEN AVOIDED WITHOUT
BREAKING THE PROCEDURE.** This line's convention, visible at every other paired member, is that **a second
extract carries the SAME file name as its first extract, in the other folder** — rows 18, 45 and 48 each
do. **This file does not.** It is
`karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks-onset-wise-predictions.md`
where the first extract is
`karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks.md`, differing by a trailing
`-onset-wise-predictions`. **The cause is the procedure itself:** the name had to be chosen at step 4,
when the extract was written, and the first extract's name could not be looked up before step 7 without
breaking the independence bound. **This file is NOT renamed**, because the path it was landed at before
step 7 is part of what evidences that independence. **It is left for the user to rule**, and it is flagged
rather than left to be found, because `reading_pass/extracts/` already carries one unexplained pair
differing only by a trailing suffix — the two Lafferty, McCallum and Pereira 2001 extracts at 63,127 and
62,394 bytes, confirmed at this side's own listing — and a second pair of that shape should not be created
silently.

---

## §1 — What the paper is, and the identity axis

### §1.1 The identity, as the document itself prints it

Every item below was read at the document's own first page unless otherwise said.

- **Title:** "ROMAN NUMERAL ANALYSIS WITH GRAPH NEURAL NETWORKS: ONSET-WISE PREDICTIONS FROM NOTE-WISE
  FEATURES"
- **Authors:** Emmanouil Karystinaios¹, Gerhard Widmer¹,²
- **Affiliations:** ¹ Institute of Computational Perception, Johannes Kepler University Linz, Austria;
  ² LIT AI Lab, Linz Institute of Technology, Austria
- **Contact:** `firstname.lastname@jku.at`
- **Preprint identifier, in the left margin of page 1:** `arXiv:2307.03544v2 [cs.SD] 12 Jul 2023`
- **Licence:** the Creative Commons BY logo, with "© E. Karystinaios and G. Widmer. Licensed under a
  Creative Commons Attribution 4.0 International License (CC BY 4.0)."
- **The attribution line the licence block prints, verbatim:** "**Attribution:** E. Karystinaios and G.
  Widmer, "Roman Numeral Analysis with Graph Neural Networks: Onset-wise Predictions from Note-wise
  Features", in *Proc. of the 24th Int. Society for Music Information Retrieval Conf.*, Milan, Italy,
  2023."
- **Source code:** the abstract states "The full source code of this work is available at
  `https://github.com/manoskary/chordgnn`".

**What is NOT printed anywhere in the eight pages as read:** a DOI; a submission, acceptance or
publication date other than the arXiv stamp; proceedings page numbers; a running header or footer on any
page; a printed page number on any page.

### §1.2 ★ THREE THINGS THE IDENTITY AXIS LEAVES OWED, AND THEY ARE OWED BECAUSE OF WHAT THE RECORD HOLDS, NOT BECAUSE OF WHAT THE PAPER PRINTS

**(a) THE RECORD NAMES THIS PAPER BY ITS MODEL AND NOT BY ITS TITLE, AND NAMES NO AUTHOR.** Both places
this side read — the candidacy row and the bibliography — give `ChordGNN, ISMIR 2023` and nothing more.
**The paper's title contains the word "ChordGNN" nowhere**; ChordGNN is the name of the model the paper
introduces, used throughout its body in italics. So there is no author string and no title string in this
project's record against which the document's own face could be checked, **and the identity axis here
closes against the document alone.** This is a weaker position than a member whose citation the record
carries in full, and it is stated rather than passed over.

**(b) THE VENUE IS CONFIRMED AT THE DOCUMENT'S OWN LICENCE BLOCK AND NOT ONLY AT THE REGISTER.** The
register says "ISMIR 2023". The document's own attribution line says *Proc. of the 24th Int. Society for
Music Information Retrieval Conf., Milan, Italy, 2023*. **These agree**, and the agreement is established
at the document rather than assumed from the register.

**(c) THIS IS THE arXiv COPY AND NOT THE PROCEEDINGS COPY.** The file name says `arxiv`, the left margin
carries an arXiv identifier and a version (`v2`), and no proceedings pagination is printed. **NOT
established by this read:** that this v2 text is identical to the camera-ready proceedings text. Nothing
in the eight pages states the relation between them. A later reader citing a page number from the
proceedings copy should not assume it matches anything here.

### §1.3 What the paper is about, in the paper's own frame

The abstract, verbatim:

> "Roman Numeral analysis is the important task of identifying chords and their functional context in
> pieces of tonal music. This paper presents a new approach to automatic Roman Numeral analysis in
> symbolic music. While existing techniques rely on an intermediate lossy representation of the score, we
> propose a new method based on Graph Neural Networks (GNNs) that enable the direct description and
> processing of each individual note in the score. The proposed architecture can leverage notewise
> features and interdependencies between notes but yield onset-wise representation by virtue of our novel
> edge contraction algorithm. Our results demonstrate that *ChordGNN* outperforms existing
> state-of-the-art models, achieving higher accuracy in Roman Numeral analysis on the reference datasets.
> In addition, we investigate variants of our model using proposed techniques such as NADE, and
> post-processing of the chord predictions. The full source code of this work is available at
> https://github.com/manoskary/chordgnn"

**The problem the paper says it is solving, in its §1 (PDF page 1), is a REPRESENTATION problem and not an
accuracy problem in the first instance.** Its stated complaint against the prior art is that models "such
as CNNs whose inputs must be in fixed-sized chunks" force an audio-inspired strategy of "dividing a
musical score into fixed-length time frames ("windows")", and that "such a representation is unnatural for
scores and has the added practical disadvantage of being time-limited (for example regarding notes
extending beyond the current window) and, due to the fixed-length (in terms of score time) constraint,
capturing varying amounts of musically relevant context."

**The paper's own argument for why the note is the right unit** is stated in §2 (PDF page 2) and is a
musicological one rather than a measured one: "Should a musicologist perform music analysis on a piece of
music, they would consider the individual notes existing in the score. Thus, a time frame representation
would come across as unnatural for symbolic music and in particular for such an analysis task."

---

## §2 — The method, as the paper states it

### §2.1 The lineage the paper places itself in (its §2, PDF page 2)

The paper's own account of the prior art, which is the part a reader of this project's record will want at
its own words rather than summarised:

- **Before deep learning:** "Notable work includes statistical models such as *Melisma* [2], HMM-based
  models [3], and grammar-based approaches [4]."
- **The multitask turn:** "Due to the large vocabulary of possible Roman Numerals, the problem has been
  divided into several component subtasks, thus resulting in a multitask learning setting [5]."
- **The six components, verbatim:** "As a multitask problem, a Roman Numeral is characterized by the
  following components: the primary and secondary degree (as illustrated in Figure 1), the local key at
  the time point of prediction, the root of the chord, the inversion of the chord, and the quality (such
  as major, minor, 7, etc.)."
- **★ THE REDUNDANCY CLAIM, WHICH IS THE ONE SENTENCE OF THIS SECTION A DESIGN CONSUMER SHOULD READ AT
  ITS OWN WORDS:** "Although the root can be derived from the other components, it was pointed out by [6]
  that redundancy is assisting Roman Numeral analysis systems to learn." **[6] is Micchi, Gotham & Giraud
  2020** (reference list, PDF page 7). So the paper carries a redundant, derivable target on the authority
  of another paper, and states no measurement of its own for it.
- **The frame-based lineage:** "Most deep learning approaches to Roman Numeral analysis are inspired by
  work in audio classification, cutting a score into fixed-size chunks (in terms of some constant score
  time unit; e.g., a 32nd note) and using these as input to deep models. Using this quantized time frame
  representation, [6] introduced a CRNN architecture to predict Roman Numerals. Other work has continued
  to build on the latter by introducing more tasks to improve performance such as the *AugmentedNet* model
  [7], or introducing intra-dependent layers to inform in an orderly fashion the prediction of one task
  with the previously predicted task, such as the model introduced by [8]. Other architectures, such as
  the CSM-T model, have demonstrated good results by introducing modular networks which treat a score as a
  sequence of notes ordered first by onset and then by pitch [9]."
- **The parameter-sharing claim:** "Automatic Roman Numeral analysis, as a multitask problem, is mostly
  tackled with hard parameter-sharing models. These models share part of the model across all tasks as an
  encoder, and then the common embeddings are branched to a classification model per task [6–8]. However,
  some approaches separate tasks prior to a more modular or soft parameter sharing approach [9]."
- **Graphs elsewhere in this domain:** "Recently, modeling scores as graphs has also been demonstrated to
  be beneficial for problems such as expressive performance generation [10], cadence detection [11], voice
  separation [12], or boundary detection [13]." **[11] and [12] are the first author's own prior work**
  (reference list, PDF page 7).
- **The multitask-optimisation literature it draws on:** "Issues with multi-objective optimization have
  been early addressed by Zhang et al. [14] and recent solutions have been proposed for the multitask
  setting in the form of dynamic task prioritization [15], gradient normalization [16], rotation matrices
  [17], or even game-theoretic approaches [18]."

### §2.2 The task decomposition (its §3.1, PDF page 3)

**The five conventional tasks, verbatim:** "The Roman Numeral prediction can be viewed as a simultaneous
prediction of the local key, degree (primary and secondary), quality, inversion, and root. Each one of
these tasks is a categorical, multiclass classification problem."

**★ NOTE THE SHIFT FROM SIX TO FIVE, WHICH THE PAPER MAKES WITHOUT REMARKING ON IT.** Its §2 names **six**
components, counting primary and secondary degree separately. Its §3.1 names **five** tasks, with "degree
(primary and secondary)" as ONE task. **The paper does not say that this is the same decomposition counted
two ways.** It is, on the paper's own wording, and this file states it so that a reader meeting "the 5
tasks" two paragraphs after "those 6 components" is not left to work it out.

**The restricted-vocabulary result it imports:** "However, [7] indicated that only three tasks would be
sufficient to reach 98% of the Roman Numeral annotations in our dataset (detailed in Section 4.1). These
three tasks comprise the prediction of a restricted vocabulary of common Roman Numeral symbols in
combination with the local key and the inversion."

**The two reconstruction methods, verbatim and with their names as the paper fixes them:** "We refer to
Roman Numeral prediction involving the 5 tasks as *conventional RN*, and the combined prediction of key,
inversion, and restricted RN vocabulary alternative RN, as *RN_alt*, in accordance with [7]."

**★ BOTH THE 98 % FIGURE AND THE ALTERNATIVE RECONSTRUCTION ARE IMPORTED FROM [7], NOT MEASURED HERE.**
The paper says "in accordance with [7]" in terms. **[7] is Nápoles López, Gotham & Fujinaga 2021**
(reference list, PDF page 7) — which is row 48 of this same slice.

**The four additional tasks, verbatim:** "Other tasks have been introduced that have been shown to improve
the performance of related models [7]. These include the Harmonic Rhythm, which is used to infer the
duration of a Roman Numeral at a given time point; the Tonicization task, a multiclass classification task
that refers to a tonicized key implied by the Roman Numeral label and is complementary to the local key;
the Pitch Class Sets task, which includes a vocabulary of different pitch class sets, and the Bass task,
which aims to predict the lowest note in the Roman Numeral label."

### §2.3 The graph representation (its §3.2, PDF page 3)

**The node features, verbatim:** "The input to the GNN encoder is an attributed graph G = (V, E, X) where
V and E denote its node and edge sets and X represents the node feature matrix, which contains the
features of the notes in the score. For our model, we used **pitch spelling, note duration, and metrical
position** features."

**★ PITCH SPELLING IS AN INPUT FEATURE, STATED IN TERMS.** This is a coupling fact and is carried to §3.

**The four edge types, transcribed exactly as the paper's bullets print them.** "A labeled edge (u, r, v)
of type r between two notes u, v belongs to E if the following conditions are met:"

| Relation | The paper's stated condition | The paper's words for it |
|---|---|---|
| `onset` | `on(u) = on(v) → r = onset` | "notes starting at the same time" |
| `during` | `on(u) > on(v) ∧ on(u) ≤ on(v) + dur(v) → r = during` | "note starting while the other is sounding" |
| `follow` | `on(u) + dur(u) = on(v) → r = follow` | "note starting when the other ends" |
| `silence` | `on(u) + dur(u) < on(v) ∧ ∄v' ∈ V, on(v') < on(v) ∧ on(v') > on(u) + dur(u) → r = silence` | "note starting after a time frame when no note is sounding" |

**The heterogeneity claim, verbatim:** "We model our score generally following Karystinaios and Widmer
[11], but we opt for a heterogeneous graph convolution approach, i.e., including different edge
relations/types. Furthermore, we develop an edge contraction pooling layer that learns onset-wise
representations from the note-wise embeddings and therefore yields a sequence."

**What the architecture replaces, in the paper's own words:** "In essence, we replace the CNN encoder that
works on quantized frames of the score in previous approaches, with a graph convolution followed by an
edge contraction layer."

### §2.4 The convolution (its §3.3, PDF page 3, equation 1)

"ChordGNN uses heterogeneous graphSAGE [19] convolutional blocks defined as:"

```
h^(l+1)_{N_r(v)} = mean( { h^l_u , ∀u ∈ N_r(v) } )
h^(l+1)_{v_r}    = σ( W · concat( h^l_v , h^(l+1)_{N_r(v)} ) )
h^(l+1)_v        = (1/|R|) Σ_{r ∈ R} h^(l+1)_{v_r}                 (1)
```

"where h^(0)_v = x_v and x_u is the input features for node u, N(u) are the neighbors of node u, and σ is
a **ReLU** activation function. We name the output representations of all nodes after graphSAGE
convolution H = { h^(L)_u | u ∈ V } where L is the total number of convolutional layers."

**Read exactly:** the per-relation representations are combined by an **unweighted mean over the relation
types** — `(1/|R|) Σ` — so the four edge types contribute equally and no relation weight is learned at
this point.

### §2.5 ★ THE EDGE CONTRACTION, WHICH IS WHAT THE PAPER CALLS ITS NOVEL CONTRIBUTION (its §3.3, PDF page 4, equations 2 and 3)

"Given the hidden representation H of all nodes, and onset edges E_On = {(u,v) | on(u) = on(v)}, the onset
edge contraction is described by the following equations: first, we update the hidden representation with
a learned weight, H' = HW^(pool). Subsequently we need to unify the representations for every node u, such
that ∀v ∈ N_On(u), h^(cp)_u = h^(cp)_v:"

```
h^(cp)_u = h_u + Σ_{v ∈ N_On(v)} h_v            (2)

V' = { v ∈ V | ∀u ∈ V, (v,u) ∈ E_On  ⟹  u ∉ V' }   (3)
```

"where, h_u and h_v belong to H'. Subsequently, we filter the vertices: … Therefore, H^(cp) = { h^(cp)_u |
u ∈ V' } are the representations obtained. Sorting the representations by the onset on which they are
attributed we obtain a sequence S = [ h^(cp)_{u1}, h^(cp)_{u2}, … h^(cp)_{uk} ] such that on(u1) < on(u2)
< ··· < on(uk)."

**★ WHAT THIS DOES, IN PLAIN WORDS, BECAUSE IT IS THE MECHANISM THE ABSTRACT ADVERTISES.** Notes that
begin at the same moment are joined by `onset` edges. After convolution, every such group is collapsed to
a single vector by SUMMING the group's (re-weighted) note vectors, one survivor is kept per group, and the
survivors are put in order of onset time. **The result is a sequence with one element per distinct onset**
— which is what lets a note-level encoder feed a sequence model whose targets are onset-level.

**★ TWO THINGS ABOUT EQUATIONS (2) AND (3) THIS READ RECORDS AS PRINTED, WITHOUT PROPOSING ANYTHING.**
*(i)* Equation (2)'s summation is printed as **`Σ_{v ∈ N_On(v)}`** — **the summation variable and the
argument of the neighbourhood function are the same symbol `v`**, so the index set is defined in terms of
the variable it is meant to bind, while the left-hand side is `h^(cp)_u`. The surrounding prose says the
purpose is to "unify the representations for every node u, such that ∀v ∈ N_On(u)", which is `u`'s
neighbourhood. **This read verified the printed form at a second opening of that page at the read-back,
records it as printed, and does not correct it**; whether it is a typographical slip is not settled by
anything in the eight pages. *(ii)* Equation (3) defines `V'` **by a condition that refers to
`V'` itself** (`u ∉ V'`), so it is not a closed-form definition; read with the prose it is a
choose-one-survivor-per-onset-group filter, and the paper states no tie-break rule for WHICH member
survives. **No value in this paper depends on that choice as far as the eight pages state**, because the
contraction sum (2) has already made the surviving vectors equal within a group.

### §2.6 The sequence model and the heads (its §3.3, PDF page 4)

"The sequence S is then passed through an MLP layer and **2 GRU layers**. This concludes the hard-sharing
part of our model. Thereafter, an MLP head is attached per task, as shown in Figure 3."

### §2.7 The loss (its §3.3, PDF page 4, equation 4)

"For training, we use the dynamically weighted loss introduced by [20]. The total loss L_tot of our
network is calculated as a weighted sum of the individual losses for every task, where the weights are
learned during training:"

```
L_tot = Σ_{t ∈ T} L_t · 1/(2γ_t²) + log(1 + γ_t²)        (4)
```

"where T is the set of tasks; L_t is the cross-entropy loss relating to task t; the γ_t are learned
scalars that give the weight for each task t; and the log expression is a regularization term [20]."

**Read exactly:** the per-task weights are **learned**, not set; **[20] is Liebel & Körner 2018**
(reference list, PDF page 7), so the loss form is imported and not derived here.

### §2.8 The post-processing block (its §3.3.1, PDF page 4)

"We enhance our model with a post-processing phase after the model has been trained. Our post-processing
phase combines the logits of all tasks' predictions by concatenating them and, then, feeds them to a
single-layer bidirectional LTSM block. Then, again the embeddings of the sequential block are distributed
to **11 one-layer MLPs, one for each task**. The post-processing block is sketched in Figure 4."

**★ THE POST-PROCESSING IS A SECOND, SEPARATELY TRAINED STAGE OVER THE LOGITS, NOT A CHANGE TO THE
MODEL.** It runs "after the model has been trained", takes all tasks' logits concatenated, and emits a
fresh prediction per task. **This is the mechanism behind every "+Post" row of Table 1**, and it is the
paper's own instrument for the task-interdependence problem it raises in §1.

**★ "LTSM" IS PRINTED IN THE BODY WHERE FIGURE 4 PRINTS "LSTM".** Recorded as printed; it is a
transposition of the standard abbreviation and nothing turns on it.

### §2.9 The corpora (its §4.1, PDF pages 4–5)

**The six sources of the "Full" dataset, transcribed exactly as the paper names and cites them:**

| The paper's name for it | Its citation in this paper |
|---|---|
| the Annotated Beethoven Corpus (ABC) | [22] |
| the annotated Beethoven Piano Sonatas (BPS) dataset | [5] |
| the Haydn String Quartets dataset (HaydnSun) | [23] |
| the TAVERN dataset | [24] |
| a part of the When-in-Rome (WiR) dataset | [25, 26] |
| the Well-Tempered-Clavier (WTC) dataset | [25] |

**The paper's own overlap remark, verbatim:** the WTC dataset "is also part of the WiR dataset".

**★ SO THE SIX SOURCES ARE NOT STATED TO BE DISJOINT, AND THE PAPER SAYS SO ITSELF FOR ONE PAIR.** It
takes "a part of" WiR and also takes WTC, which it says is inside WiR. **What the paper does NOT say is
whether the part of WiR it took excludes WTC.** Recorded as a gap in what is stated, with nothing
proposed.

**The split, verbatim:** "Training and test splits for the full dataset were also provided by [7]. It is
worth noting that the BPS subset splits were already predefined in [5]. In total, approximately **300
pieces were used for training, and 56 pieces were used for testing**, proportionally taken from all the
different data sources. We draw a distinction for the BPS test set, which includes **32 Sonata first
movements** and for which we ran an additional experiment. The full test set also includes the **7
Beethoven piano sonatas**."

**★ THE SPLITS ARE IMPORTED, NOT MADE HERE**, and the paper says so twice — "provided by [7]" and "already
predefined in [5]". **So the split protocol is [7]'s and [5]'s, and this paper inherits whatever
properties those splits have.** The paper's stated reason is comparability: "We run experiments with our
model in the exact same way as described in the paper [7], including the specific data splits, so that our
results are directly comparable to the figures reported there" (§4, PDF page 4).

**The augmentations, verbatim:** "we include data augmentations identical to the ones described in [7]:
texturization and transposition. The texturization is based on a dataset augmentation technique introduced
by [27]. The transposition augmentation boils down to transposing a score to all the keys that lie within
a range of key signatures that have up to 7 flats or sharps. **It should be noted that the augmentations
are only applied in the training split.**"

**The late addition, verbatim:** "For our last experiment (to be reported on in Section 5.3 below), we add
additional data that were recently introduced by [21]. The additional data include the annotated Mozart
Piano Sonatas (MPS) dataset [28] for which we also applied the aforementioned augmentations."

### §2.10 The training configuration (its §4.2, PDF page 5)

Transcribed in full, because these are the paper's only stated hyper-parameters:

| Constant | Value as printed |
|---|---|
| optimizer | AdamW |
| hidden size | 256 |
| learning rate | 0.0015 |
| weight decay | 0.005 |
| dropout | 0.5, "applied to each learning block of our architecture" |

**★ WHAT §4.2 DOES NOT STATE, and a later reader must not assume it is elsewhere in these eight pages:**
the number of convolutional layers `L`, the number of training epochs, the batch size, any early-stopping
or model-selection rule, and the random seeds. **`L` is named as a symbol in §3.3 and given no value
anywhere in the eight pages as read.**

### §2.11 The evaluation measure (its §5, PDF page 5)

"As an evaluation metric, we use **Chord Symbol Recall (CSR)** [29] where for each piece, the proportion
of time is collected during which the estimated label matches the ground truth label. We apply the CSR at
the **32nd note granularity level**, in accordance with [6, 7, 9]."

**★ TWO PROPERTIES OF THIS MEASURE THAT BEAR ON HOW EVERY VALUE IN TABLE 1 IS READ, stated because the
paper's own wording makes them both explicit.** *(i)* **It is DURATION-weighted** — "the proportion of
time" — not event-weighted, so a long wrong label costs more than a short one. *(ii)* **It is evaluated on
a fixed 32nd-note grid**, imported "in accordance with [6, 7, 9]", so the comparison against those models
is on their grid. **[29] is Harte 2010** (reference list, PDF page 8).

**★ AND THE PAPER REPORTS A SECOND, DIFFERENT MEASURE BESIDE IT, WHICH TABLE 1's OWN CAPTION DEFINES:**
"RN(Onset) refers to onset-wise prediction accuracy, all other scores use the CSR score". **So the
RN(Onset) column is NOT a CSR figure and is not duration-weighted**, and a value is printed in it for this
paper's own models alone.

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**it is reported only for this paper's own
models — the caption's dashes in that column for every other model are not omissions but the absence of a
comparable number**" — **the second half is this read's inference offered as the caption's.** The caption
explains the dash for exactly ONE cell, CSM-T's Quality, and nowhere defines what a dash means in
general; see §7.1(q).)*

---

## §3 — Coupling facts

*(What this paper assumes upstream, what it hands downstream, and the scope it states for itself. Every
item is at the paper's own words or is marked as this read's inference from them.)*

### §3.1 What it ASSUMES about its upstream

- **A symbolic score with SPELLED pitch.** §3.2 names "pitch spelling" as one of three node features. The
  model therefore cannot run on a pitch-class-only or MIDI-only input without that feature being supplied
  from somewhere. **Stated at the paper; not qualified there in any way.**
- **Note durations and metrical positions.** The other two named node features (§3.2). The metrical
  position feature implies a barline and a time signature, or something standing for them; **the paper
  does not say how metrical position is encoded**, and no encoding is printed in the eight pages.
- **Exact onset and offset times, to the resolution that decides identity of onsets.** All four edge rules
  (§3.2) are equalities or inequalities over `on(·)` and `on(·) + dur(·)`, and the whole edge-contraction
  step (§3.3) is driven by `on(u) = on(v)`. **So what counts as "the same onset" is decided upstream of
  this model, and the paper states no tolerance, quantisation or tie rule for it.**
- **Ground-truth Roman Numeral annotations decomposed into the model's task set.** The eleven heads are
  trained with cross-entropy (§3.3, equation 4), so each needs a label. The decomposition is [7]'s
  (§3.1).
- **Splits it does not make.** §4.1, twice: the full-dataset splits come from [7], the BPS splits from
  [5].

### §3.2 What it HANDS downstream

- **One prediction per task, per ONSET** — not per time frame and not per note. This is the whole point of
  the edge contraction (§3.3): the sequence `S` has one element per distinct onset, and the heads sit on
  that sequence.
- **A Roman Numeral reconstructed in one of two declared ways** (§3.1): *conventional RN* from the five
  tasks, and *RN_alt* from key, inversion and a restricted common-RN vocabulary.
- **Logits for all tasks**, which the post-processing block consumes (§3.3.1). **That block is the only
  further use of the raw head outputs described in the eight pages as read**, and **the paper nowhere in
  those pages states how a single prediction is taken from a head's output.**

  *(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**This is the only place the paper says
  what the raw head outputs are used for beyond argmax.**" — **an unbounded negative over the paper, and
  it imported "argmax", a word the paper does not use.**)*
- **★ WHAT IT DOES NOT HAND DOWN, AND THE PAPER IS EXPLICIT ABOUT ONE OF THEM.** §5.4 (PDF page 6) says of
  its own model: "The ChordGNN solution accommodates both interpretations as it **doesn't attempt to group
  chords at a higher level, treating each eighth note as an individual chord rather than a passing
  event**." **So there is no grouping, prolongation or passing-chord layer in this model**, stated by the
  authors as a property of the solution rather than as a limitation.
- **No uncertainty surface is described anywhere in the eight pages** — no ranked alternatives, no
  confidence, no calibrated probability. The logits exist internally and are consumed by the
  post-processing block; nothing in the paper describes publishing them.

### §3.3 Its own STATED scope and limits

- **Symbolic, Western classical, and the six corpora of §4.1.** The conclusion says "Finally, we aim to
  extend our method to the audio domain", which is the paper's own statement that it is not there.
- **The augmentations are training-only** (§4.1), stated in terms.
- **The transposition range is up to 7 flats or sharps** (§4.1).
- **Its comparability claim is bounded to [7]'s protocol** (§4): "in the exact same way as described in
  the paper [7], including the specific data splits, so that our results are directly comparable to the
  figures reported there."
- **★ AND IT STATES ONE COMPARABILITY FAILURE ITSELF, IN A FOOTNOTE.** Footnote 1 on PDF page 6:
  "Unfortunately, we cannot directly compare these numbers to [21], as their results are not reported in
  comparable terms." **That bounds §5.3's whole experiment**, which is the one that produces the paper's
  highest figure.

---

## §4 — Claims, labeled

*(Under the theory-grounding corollary to #1/#2: every load-bearing claim is labeled **FACT** — stated or
measured in this paper, which was fetched and read whole — **THEORY** — established published theory the
paper imports — or **CONJECTURE**. The label says what KIND of support the claim has in THIS document; it
is not a verdict on whether the claim is true.)*

| # | The claim | Label | Where, and on what support |
|---|---|---|---|
| C1 | ChordGNN reaches the Table 1 values on the BPS and Full test sets | **FACT** | §5.1 and Table 1, PDF page 5. Measured here, by these authors, on splits imported from [7]. |
| C2 | ChordGNN's conventional-RN score exceeds every model it is compared against, on both test sets | **FACT**, bounded | Table 1. True of the RN column as printed. **See §7.1(a): the paper's own wider sentence about "all fields" is not true of all fields.** |
| C3 | Post-processing improves both RN and RN_alt on both test sets | **FACT** | Table 1, all four pairs. §5.1: "In both experiments, post-processing has been shown to improve both RN and RN_alt." |
| C4 | A note-level graph representation is more natural for symbolic music than fixed-length time frames | **CONJECTURE** | §1 and §2, PDF pages 1–2. The argument given is the musicologist analogy; **no measurement isolates the representation**, because ChordGNN differs from the frame-based models in encoder, pooling and training regime together. |
| C5 | The edge-contraction pooling layer is novel | **CONJECTURE** as printed | Abstract: "our novel edge contraction algorithm". No survey supporting the novelty claim is cited at that word. |
| C6 | The dynamically weighted loss beats the plain baseline and the gradient-normalisation variants on this problem | **FACT** | Table 2 and §5.2, PDF page 5. Five runs each, with a stated ± whose unit is not defined — see §7.1(c). |
| C7 | Gradient-normalisation techniques are not beneficial here | **FACT** for the two tested variants | Table 2: Rotograd 45.5/47.1 and R-GradN 45.2/46.7, both BELOW the 46.1/47.8 baseline. |
| C8 | Techniques for carrying prediction information across tasks are "not particularly beneficial or necessary" | **CONJECTURE**, and **refuted on its own Table 2 for NADE** | §6 conclusion, PDF page 6. See §7.1(b). |
| C9 | Redundant targets (the root, derivable from the other components) help the system learn | **THEORY** imported | §2: "it was pointed out by [6]". No measurement of it in this paper. |
| C10 | Three tasks suffice for 98 % of the Roman Numeral annotations in this dataset | **THEORY** imported | §3.1: "[7] indicated". Not re-measured here. |
| C11 | ChordGNN's higher RN score with LOWER component scores shows "more meaningfully interrelated predictions" | **CONJECTURE** | §5.1, PDF page 5. This is a causal reading of a pattern in Table 1, offered without a measurement that separates interrelation from any other cause. **The pattern itself is FACT — see §6.3.** |
| C12 | The 14-task model with Mozart data reaches 53.5 CSR on conventional RN | **FACT** as a reported number | §5.3, PDF page 6. **Reported in prose only, in no table, with no ±, and against a dataset that changed — see §7.1(d).** |
| C13 | Post-processing adds "up to two additional percentage points" to that model | **FACT** as a reported bound, **with no value printed** | §5.3. No figure, no table. |
| C14 | In the Figure 5 passage the ground truth is wrong and ChordGNN is right about the inversion | **FACT** about the score, **argued and not measured** | §5.4, PDF page 6. The argument is that the cello's F♯ is the lowest sounding note and is the root of vii°. **The acknowledgements say this analysis came from an anonymous reviewer — see §7.3.** |
| C15 | CSR is the appropriate comparison measure at 32nd-note granularity | **THEORY** imported | §5: "[29]" and "in accordance with [6, 7, 9]". |

---

## §5 — Measured results and printed values, transcribed as the paper prints them

### §5.1 Table 1, transcribed whole (PDF page 5)

**The caption, verbatim:** "Model comparison on two different test sets, the Beethoven Piano Sonatas
(BPS), and the full test set. *RN* stands for Roman Numeral, *RN_alt* for the alternative Roman Numeral
computations discussed in Section 3.1. *RN(Onset)* refers to onset-wise prediction accuracy, all other
scores use the CSR score (see Section 5). Note that model *CSM-T* reports *Mode* instead of *Quality*."

**Block BPS**

| Model | Key | Degree | Quality | Inversion | Root | RN | RN (Onset) | RN_alt |
|---|---|---|---|---|---|---|---|---|
| Micchi (2020) | 82.9 | 68.3 | 76.6 | 72.0 | – | 42.8 | – | – |
| CSM-T (2021) | 69.4 | – | – | – | 75.4 | 45.9 | – | – |
| AugNet (2021) | **85.0** | **73.4** | **79.0** | 73.4 | **84.4** | 45.4 | – | 49.3 |
| ChordGNN (Ours) | 79.9 | 71.1 | 74.8 | 75.7 | 82.3 | 46.2 | 46.6 | 48.6 |
| ChordGNN+Post (Ours) | 82.0 | 71.5 | 74.1 | **76.5** | 82.5 | **49.1** | **49.4** | **50.4** |

**Block Full**

| Model | Key | Degree | Quality | Inversion | Root | RN | RN (Onset) | RN_alt |
|---|---|---|---|---|---|---|---|---|
| AugNet (2021) | **82.9** | 67.0 | **79.7** | 78.8 | 83.0 | 46.4 | – | 51.5 |
| ChordGNN (Ours) | 80.9 | 70.1 | 78.4 | 78.8 | 84.8 | 48.9 | 48.4 | 50.4 |
| ChordGNN+Post (Ours) | 81.3 | **71.4** | 78.4 | **80.3** | **84.9** | **51.8** | **51.2** | **52.9** |

**Bold is the paper's own**, transcribed cell for cell as printed. **The dash is the paper's own** and,
per the caption, marks either a measure the model does not report (CSM-T's Quality, given as Mode) or a
column with no comparable value (RN(Onset) for every model but this paper's).

### §5.2 Table 2, transcribed whole (PDF page 5)

**The caption, verbatim:** "Configuration Study: Chord Symbol Recall on Roman Numeral analysis on the full
test set. *RN* stands for Roman Numeral, *RN_alt* refers to the alternative Roman Numeral computations
discussed in section 3.1. WLoss stands for the dynamically weighted loss described in Section 3, and
R-GradN stands for Rotograd with Gradient Normalization. **Every experiment is repeated 5 times with the
same ChordGNN model as Table 1 without post-processing.**"

| Variant | RN | RN_alt |
|---|---|---|
| ChordGNN (Baseline) | 46.1 ± 0.003 | 47.8 ± 0.007 |
| ChordGNN + WLoss | **48.9** ± 0.001 | **50.4** ± 0.010 |
| ChordGNN + Rotograd | 45.5 ± 0.003 | 47.1 ± 0.005 |
| ChordGNN + R-GradN | 45.2 ± 0.006 | 46.7 ± 0.005 |
| ChordGNN + NADE | 48.2 ± 0.005 | 49.9 ± 0.005 |

### §5.3 The values printed in prose and in no table

| Value | Where | What it is said to be |
|---|---|---|
| **98 %** | §3.1, PDF page 3 | The share of Roman Numeral annotations in this dataset reachable by three tasks — **[7]'s figure, not measured here.** |
| **11.6 %** | §5.1, PDF page 5 | "Our model obtains up to 11.6% improvement in conventional Roman Numeral prediction." |
| **53.5** | §5.3, PDF page 6 | The conventional-RN CSR of the 14-task model with Mozart data. |
| **"up to two additional percentage points"** | §5.3 | What post-processing adds to that model. **No number is printed.** |
| **11+3 = 14** | §5.3 | The task count of the adapted model. |
| **≈300 / 56 / 32 / 7** | §4.1, PDF pages 4–5 | Training pieces, test pieces, BPS-test Sonata first movements, Beethoven piano sonatas in the full test set. |
| **7 flats or sharps** | §4.1 | The transposition-augmentation range. |
| **32nd note** | §5, PDF page 5 | The CSR granularity. |
| **256 / 0.0015 / 0.005 / 0.5** | §4.2, PDF page 5 | Hidden size, learning rate, weight decay, dropout. |
| **v1.9.1** | §4, PDF page 4 | The AugmentedNet version compared against in the last experiment. |
| **2 GRU layers** | §3.3, PDF page 4 | The sequence model's depth. |
| **11** | §3.3.1, PDF page 4 | The number of one-layer MLPs in the post-processing block, "one for each task". |

### §5.4 The acknowledgements, as printed (PDF page 7)

> "We gratefully acknowledge the musical analysis of the vii° passage in Fig. 5 (Section 5.4) that was
> offered by an anonymous reviewer, and which we took the liberty of adopting for our text. This work is
> supported by the European Research Council (ERC) under the EU's Horizon 2020 research & innovation
> programme, grant agreement No. 101019375 ("Whither Music?"), and the Federal State of Upper Austria (LIT
> AI Lab)."

---

## §6 — Arithmetic this read performed on the paper's own printed values

*(Every input below is a value transcribed in §5 from the paper itself. Nothing external enters. Where a
derivation supports rather than refutes the paper, that is said as plainly as where it refutes.)*

### §6.1 The 11.6 % claim closes, and it is a RELATIVE improvement that the paper does not label as one

§5.1 says "Our model obtains up to 11.6% improvement in conventional Roman Numeral prediction."

On the Full test set, AugNet's RN is 46.4 and ChordGNN+Post's is 51.8. The **absolute** difference is
**5.4 points**. The **relative** difference is 5.4 / 46.4 = **11.64 %**, which rounds to the printed 11.6.

On the BPS set the same pair gives 49.1 − 45.4 = 3.7 points, relative 3.7 / 45.4 = **8.15 %**, which is
smaller — so "up to" is satisfied by the Full-set figure being the larger of the two.

**★ THE CLOSURE IS EXACT AND THE LABEL IS MISSING.** Of the readings this side tested, the relative one on
the Full-set RN column is the one that produces 11.6: the absolute difference on that pair is 5.4, the
same relative figure on BPS is 8.15, and the relative figures for the other Full-set columns comparing
AugNet against ChordGNN+Post are 6.6 (Degree), 1.9 (Inversion), 2.3 (Root) and 2.7 (RN_alt). **The paper
writes "11.6% improvement" beside a table whose every cell is itself a percentage**, so a reader who takes
it as percentage points reads a gain of 11.6 where the table gives 5.4. Nothing in the sentence
distinguishes them.

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**The only reading of the printed values that
produces 11.6 is the relative one.**" — **a uniqueness claim over a space of readings this side never
enumerated.** What it tested is now named.)*

### §6.2 ★ THE "ALL FIELDS" SENTENCE IS REFUTED BY TABLE 1 AT TWO FURTHER AXES, BOTH ON THE WITHOUT-POST-PROCESSING HALF

§5.1 states: "Our model surpasses AugmentedNet **with and without post-processing** in all fields apart
from local key prediction and quality."

Tested against the Full block, column by column, AugNet against each of the two ChordGNN rows:

| Field | AugNet | ChordGNN (no post) | ChordGNN+Post | Does the sentence hold? |
|---|---|---|---|---|
| Key | 82.9 | 80.9 | 81.3 | excepted by the sentence — **holds** |
| Degree | 67.0 | 70.1 | 71.4 | both surpass — **holds** |
| Quality | 79.7 | 78.4 | 78.4 | excepted by the sentence — **holds** |
| **Inversion** | **78.8** | **78.8** | 80.3 | **NO — without post-processing the two are EQUAL, and a tie is not a surpassing** |
| Root | 83.0 | 84.8 | 84.9 | both surpass — **holds** |
| RN | 46.4 | 48.9 | 51.8 | both surpass — **holds** |
| RN (Onset) | – | 48.4 | 51.2 | **vacuous** — AugNet prints no value, so there is nothing to surpass |
| **RN_alt** | **51.5** | **50.4** | 52.9 | **NO — without post-processing ChordGNN is 1.1 points LOWER** |

**So the sentence excepts two fields and is untrue of two more**, on the half of it that says *without*
post-processing. **On the with-post-processing half it holds at every field it claims.** No value moves;
what is wrong is the scope of a sentence, and the table it sits directly beneath is what refutes it.

**★ AND THE SAME PARAGRAPH CLOSES WITH A SECOND SENTENCE OF THE SAME SHAPE, ADDED AT THE READ-BACK.**
Four lines further on, §5.1 ends: "However, *ChordGNN* without post-processing already **surpasses the
other models**." **On the RN column that is true on both test sets** — BPS 46.2 against 45.4, 45.9 and
42.8; Full 48.9 against 46.4. **On RN_alt in the Full block it is untrue by the same 1.1 points**, 50.4
against AugNet's 51.5. The sentence names no column, and it follows immediately after a sentence about
**both** RN and RN_alt, so the unqualified reading is the natural one and the table refutes it.

### §6.3 The BPS observation the paper DOES make closes exactly, cell for cell

§5.1: "Note that the AugmentedNet model exhibits higher prediction scores on the individual Key, Degree,
Quality, and Root tasks, which are used jointly for the prediction of the Roman numeral."

| Task | AugNet (BPS) | ChordGNN | ChordGNN+Post | AugNet higher than both? |
|---|---|---|---|---|
| Key | 85.0 | 79.9 | 82.0 | yes |
| Degree | 73.4 | 71.1 | 71.5 | yes |
| Quality | 79.0 | 74.8 | 74.1 | yes |
| Root | 84.4 | 82.3 | 82.5 | yes |
| *Inversion* | *73.4* | *75.7* | *76.5* | *no — and the sentence correctly omits it* |

**The sentence is exactly right, including in what it leaves out.** And the conventional RN goes the other
way: AugNet 45.4 against ChordGNN 46.2 and ChordGNN+Post 49.1.

**★ ONE THING THIS DERIVATION ADDS THAT THE PAPER DOES NOT SAY.** Conventional RN is built from five
tasks. On BPS, **the single one of those five on which ChordGNN beats AugNet is INVERSION**, and ChordGNN
nonetheless wins the conventional RN. **NOT claimed:** that inversion is what produces the difference.
Nothing in the paper isolates it, and this read proposes no mechanism.

### §6.4 ★ THE RECONSTRUCTED ROMAN NUMERAL IS FAR MORE ACCURATE THAN INDEPENDENT COMPONENTS WOULD GIVE, IN EVERY ROW THAT PRINTS ALL FIVE

*(★ DECLARED: knowing to run this test is not this read's own idea. The handoff entry that booted this
session records that row 48's second extract found the same shape on that paper. **The arithmetic below is
this read's own, on this paper's values; the idea of looking is a boot contamination and is declared
here.**)*

If the five conventional component decisions failed independently, the conventional RN accuracy would be
about their product. Taking each printed value as a proportion:

| Row | Key × Degree × Quality × Inversion × Root | Product | Printed RN | RN minus product |
|---|---|---|---|---|
| BPS AugNet | .850 × .734 × .790 × .734 × .844 | 30.5 | 45.4 | **+14.9** |
| BPS ChordGNN | .799 × .711 × .748 × .757 × .823 | 26.5 | 46.2 | **+19.7** |
| BPS ChordGNN+Post | .820 × .715 × .741 × .765 × .825 | 27.4 | 49.1 | **+21.7** |
| Full AugNet | .829 × .670 × .797 × .788 × .830 | 29.0 | 46.4 | **+17.4** |
| Full ChordGNN | .809 × .701 × .784 × .788 × .848 | 29.7 | 48.9 | **+19.2** |
| Full ChordGNN+Post | .813 × .714 × .784 × .803 × .849 | 31.0 | 51.8 | **+20.8** |

**What follows, and it is a structural fact about this task rather than about either model:** the
component errors **CO-OCCUR** — the same stretches of music are wrong on several components at once —
rather than compounding into independent failures. A design that treated these five decisions as
independent estimators and multiplied their confidences would understate the joint accuracy by between
fifteen and twenty-two points on these figures.

**★ AND THE EXCESS IS LARGER FOR ChordGNN THAN FOR AugNet ON BOTH TEST SETS** — BPS 19.7 and 21.7 against
14.9; Full 19.2 and 20.8 against 17.4. **This is consistent with the paper's own §5.1 claim** that its
model "obtains more meaningfully interrelated predictions" (claim C11 of §4). **NOT claimed:** that it
establishes C11. Several causes produce that pattern, and **the eight pages as read report no measurement
that separates them.**

*(★ NARROWED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**and the paper measures none of them**" — an
unbounded negative over the paper, where what this read can say is bounded to the eight pages it opened.)*

**★ THE BOUND ON THIS WHOLE DERIVATION, STATED BECAUSE IT IS REAL.** CSR is a **duration-weighted
proportion of time** (§2.11), not a per-decision success rate, so a product of CSR values is not literally
a probability of joint success. **The comparison is therefore indicative of co-occurrence and is not an
exact independence test.** The direction and the size of the gap are what this read reports; the exact
points are arithmetic on the printed values under an independence assumption the measure does not
strictly license.

### §6.4a ★ TWO DIFFERENCE SETS ADOPTED FROM THE FIRST EXTRACT AT THE CROSS-CHECK, RE-DERIVED HERE AT THIS FILE'S OWN TABLE

*(★ ADOPTED AT THE CROSS-CHECK (§9). Both were in the first extract and not in this read's first writing.
**The pointer is adopted and the arithmetic re-run at the printed cells**, which is this line's standing
rule for an adoption.)*

**(i) THE POST-PROCESSING GAIN, WITH-POST MINUS WITHOUT-POST:**

| Test set | RN | RN_alt |
|---|---|---|
| BPS | 46.2 → 49.1 = **+2.9** | 48.6 → 50.4 = **+1.8** |
| Full | 48.9 → 51.8 = **+2.9** | 50.4 → 52.9 = **+2.5** |

**Positive on all four, and the Roman-numeral gain is the same +2.9 on both test sets** — sets whose sizes
and repertoires differ. The paper remarks on neither the consistency nor the coincidence.

**(ii) THE ONSET-WISE COLUMN AGAINST THE DURATION-WEIGHTED ONE**, on the four rows carrying both,
RN(Onset) minus RN:

| Row | RN | RN (Onset) | Difference |
|---|---|---|---|
| BPS ChordGNN | 46.2 | 46.6 | **+0.4** |
| BPS ChordGNN+Post | 49.1 | 49.4 | **+0.3** |
| Full ChordGNN | 48.9 | 48.4 | **−0.5** |
| Full ChordGNN+Post | 51.8 | 51.2 | **−0.6** |

**The two granularities never differ by more than 0.6 on any row that carries both, and the sign is not
constant between the test sets** — positive on BPS, negative on Full. **This is the paper's own evidence
on how much the choice of grid moves the reported figure on this task**, and it is small. **NOT claimed:**
that it generalises beyond these four rows, or that a duration-weighted and an onset-wise measure would
stay this close on other music or at another granularity.

### §6.5 Table 2's weighted-loss row IS Table 1's model, and the two agree to the digit

Table 2's `ChordGNN + WLoss` prints RN **48.9** and RN_alt **50.4**. Table 1's Full-block `ChordGNN
(Ours)` prints RN **48.9** and RN_alt **50.4**. **Identical.** This agrees with Table 2's caption ("the
same ChordGNN model as Table 1 without post-processing") and with §5.2 ("same as the model in Table 1").

**★ WHAT THE AGREEMENT LEAVES UNSETTLED.** Table 2's caption says "Every experiment is **repeated 5 times**"
and §5.2 says the results are "**averaged over five runs** with random initialization". Table 1 prints a
single figure with no ± at all. **So either Table 1's 48.9 is that five-run mean — in which case Table 1
publishes a mean while suppressing its spread — or it is one run that happens to match the mean to the
digit.** The paper does not say which, and no other value in Table 1 carries an uncertainty of any kind.

### §6.6 ★ TABLE 2's ± CANNOT BE IN THE SAME UNIT AS THE VALUE IT SITS BESIDE

Every RN and RN_alt value in Table 2 lies between 45.2 and 50.4 — the same scale as Table 1, which §5
establishes as a CSR percentage. Every ± lies between 0.001 and 0.010.

Read in the same unit, `46.1 ± 0.003` claims that five runs with **random initialization** agreed to
**three thousandths of one percentage point**. Read on a 0-to-1 scale, the same ± is **0.3 percentage
points**, which is an ordinary spread for five seeds.

**The caption defines no unit for the ±, and neither does §5.2.** So the table either prints a value and
its uncertainty in two different units in one cell, or reports a reproducibility that would itself be the
paper's most remarkable result and goes unremarked. **This read does not choose between them** — it
records that the printed cells do not determine which is meant, and that **both of the two conclusions
§5.2 draws from Table 2 depend on which it is** — that the weighted loss beats the baseline and the
gradient-normalisation variants, and that it is "comparable to NADE but also more robust". On the 0-to-1
reading the WLoss-over-NADE gap of 0.7 points is several standard deviations and the second conclusion
stands; on the same-unit reading every gap in the table is hundreds of standard deviations, which is not a
credible reading of a five-seed experiment.

*(★ SHARPENED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**every conclusion §5.2 draws from Table
2**" — **a quantifier over a set this file had not enumerated.** §5.2 draws two, and they are now named.)*

### §6.7 ★ THE CONCLUSION SAYS SOMETHING ABOUT NADE THAT ITS OWN TABLE 2 REFUTES ON ONE OF THE TWO AVAILABLE READINGS

The conclusion (§6, PDF page 6): "A configuration study suggests that gradient normalization techniques or
techniques for carrying prediction information across tasks are **not particularly beneficial or
necessary** for such a model."

**For gradient normalisation the claim holds and is understated.** Rotograd 45.5 / 47.1 and R-GradN 45.2 /
46.7 both sit **BELOW** the baseline's 46.1 / 47.8. They are not merely unhelpful; on these figures they
are harmful.

**For NADE — which is what "carrying prediction information across tasks" names, §2 describing [8] as
"introducing intra-dependent layers to inform in an orderly fashion the prediction of one task with the
previously predicted task" — the two readings give opposite answers:**

| Reading of "beneficial" | NADE against | The arithmetic | Verdict |
|---|---|---|---|
| beneficial **relative to the baseline** | 46.1 / 47.8 | 48.2 / 49.9, i.e. **+2.1 and +2.1** | **refuted** — it is clearly beneficial |
| necessary **given the weighted loss** | 48.9 / 50.4 | 48.2 / 49.9, i.e. **−0.7 and −0.5** | **supported** — it is not needed |

**The sentence does not say which it means**, and its two readings have opposite truth values on the same
table. **§5.2's own wording is the careful one** and says neither: "the dynamically weighted loss is
comparable to NADE but also more robust on Conventional Roman Numeral prediction on our datasets." **So
the conclusion states about NADE something stronger than the body it summarises.**

### §6.8 ★ THE 53.5 IS INVITED INTO A COMPARISON THE PAPER HAS NOT ESTABLISHED AS LIKE-FOR-LIKE

§5.3 reports 53.5 and says in the same sentence "(compare this to row "ChordGNN (Ours)" in Table 1)",
which prints 48.9 — a gap of 4.6 points.

**Two things change at once between those two numbers**, both stated by the paper itself: the task set
goes from 11 to 14, and the data are extended with the Mozart Piano Sonatas corpus. **Neither is
isolated**, so nothing in the paper attributes the 4.6 to either.

**And the more consequential gap is that the paper does not state whether the TEST set is the same.** §4.1
says the MPS data were added and augmented, and that "the augmentations are only applied in the training
split" — which is a statement about augmentations, **not about whether MPS pieces enter the test split**.
If they do, 53.5 and 48.9 are measured on different test sets and the invited comparison is not one.
**This read does not settle it: it records that the eight pages do not.**

### §6.9 ★ FIGURE 1's CAPTION NAMES AN INVERSION ITS OWN STATED ROOT AND BASS CONTRADICT

Figure 1's caption (PDF page 2) reads, of the third chord: "The V⁶₅ indicates a major with a seven quality
in **second inversion**. The bass (lowest chord note) of that chord is **F sharp**, the root is **D**, and
the local key is C major."

Two things in the caption fix the inversion, and they agree with each other and not with the word:

- **The figured bass.** For a seventh chord, ⁶₅ is the figure for **first** inversion — the third in the
  bass. Second inversion is ⁴₃.
- **The caption's own root and bass.** With root **D** and bass **F♯**, the bass note is the **third** of
  the chord, which is **first** inversion.

**So the caption's words say second inversion where its own two other statements both say first.** No
value in the paper moves — Figure 1 is explanatory and no measurement rests on it — but it is the one
place a reader new to the vocabulary is told what an inversion label means, and it tells them wrong.

### §6.10 ★ THE TASK COUNT DOES NOT CLOSE: THE TEXT SAYS ELEVEN AND THE PAPER'S OWN ENUMERATION GIVES TEN

The paper states the count twice: §3.3.1 says the post-processing block feeds "**11** one-layer MLPs, one
for each task", and §5.3 says the adapted model has "**11+3=14** individual tasks".

Enumerating the tasks the paper itself names:

| Source | Tasks named there | Count |
|---|---|---|
| §3.1, the conventional set | Key, Degree, Quality, Inversion, Root | 5 |
| §3.1, the additional tasks | Harmonic Rhythm, Tonicization, Pitch Class Sets, Bass | 4 |
| §3.1, the restricted vocabulary used for RN_alt (labelled *Com RN* in Figures 3 and 4) | common Roman Numeral | 1 |
| | **total** | **10** |

**And Figures 3 and 4 label ten heads** — Key, Degree, Quality, Inversion, Root, Com RN, Hrhythm, Bass,
Ton Key, PC-set. **Both figures were re-opened at the read-back and the labels counted at the images
themselves**, Figure 4 carrying the same ten names on each of its two sides.

**The one reconciliation the paper's own text offers, and its standing.** §2 names **six** components by
counting primary and secondary degree separately, which with the four additional tasks and the restricted
vocabulary would give **eleven** — and would make the figures' single "Degree" box stand for two heads.
§3.1 lists **five** items — "the local key, degree (primary and secondary), quality, inversion, and root"
— says "Each one of these tasks is a categorical, multiclass classification problem", and calls them "the
5 tasks", which gives **ten**. **The paper nowhere states which count is the number of heads, and nothing
in the eight pages resolves it.** The degree-splitting reconciliation is therefore **a live conjecture and
not a refuted one**; this read records the discrepancy as printed and takes no position on it.

*(★ NARROWED AT THE CROSS-CHECK (§9). FORMER WORDING, PRESERVED (#12): "**The one reconciliation the
paper's own text offers, and why it does not work.** … **But §3.1, which is where the task set is actually
defined, explicitly makes degree ONE task** … **So under the paper's own definition of its task set the
total is ten, and the text says eleven in two places.**" — **that treated a live reading as refuted.**
§3.1's sentence is about how the Roman Numeral prediction is decomposed, and it does not settle how many
HEADS the network carries; "degree (primary and secondary)" is as readable as shorthand for two heads as
for one. **The first extract labels the same reconciliation an explicit CONJECTURE and leaves the
discrepancy as printed, which is the better treatment, and this file now takes it.**)*

**No printed result moves.** The count appears in an architectural description and in the arithmetic
`11+3=14`, and no accuracy in either table depends on it.

---

## §7 — What this read found in the paper, and what the paper does not settle

### §7.1 Defects and inconsistencies inside the paper

*(These are defects of the PAPER. **Nothing is proposed**, no result of the paper is said to be wrong, and
none of them is a defect of THIS file. Each points at the §6 derivation that established it, and the
derivations are not restated here.)*

*(★ CORRECTED AT THE SWEEP. FORMER WORDING, PRESERVED (#12): "**none of them is a defect of either
extract**" — **a statement about the first extract, written in a section produced BEFORE that file was
opened.** This read had at that point no standing to say anything about it at all.)*

| | What it is | Does any printed result move? |
|---|---|---|
| **(a)** | **The "all fields" sentence of §5.1 is untrue of two further fields on its without-post-processing half** — Inversion, where the two are equal, and RN_alt, where AugNet is 1.1 points higher (§6.2). | No |
| **(b)** | **The conclusion's claim about techniques for carrying prediction information across tasks is refuted by Table 2 on one of its two available readings**, and the body's own wording says neither (§6.7). | No |
| **(c)** | **Table 2's ± values cannot be in the same unit as the values beside them**, and no caption or section defines their unit (§6.6). | No — but every conclusion §5.2 draws depends on which unit is meant |
| **(d)** | **Figure 1's caption says "second inversion" where its own stated root and bass, and the figured bass ⁶₅ it is explaining, both give first inversion** (§6.9). | No |
| **(e)** | **The task count does not close** — the text says eleven twice, while §3.1's own list and both figures give ten, and the paper nowhere says which is the number of heads (§6.10). | No |
| **(f)** | **The 11.6 % is a relative improvement printed without being labelled as one, beside a table of percentages** where the corresponding absolute gain is 5.4 points (§6.1). | No |
| **(g)** | **§5.3 invites a comparison across a changed task set AND a changed corpus, without stating whether the test set is the same** (§6.8). | No |
| **(h)** | **Equation (2) sums over `N_On(v)` while defining `h^(cp)_u`**, in an equation whose stated purpose is about `u`'s onset-neighbourhood (§2.5). | No |
| **(i)** | **"LTSM" in §3.3.1 where Figure 4 prints "LSTM"** (§2.8). | No |
| **(j)** | **Table 1 prints no uncertainty on any cell**, while Table 2 reports the same model over five runs with a spread (§6.5). | No |
| **(k)** | **Reference [23] is given as "Ph.D. dissertation, Master's thesis"** — both, in one entry (§7.4). | No |
| **(l)** | **Reference [28] prints "no. ARTICLE"** — an unresolved bibliographic placeholder (§7.4). | No |
| **(m)** | **Reference [13] names no venue at all**, giving only authors, title and "2023" (§7.4). | No |
| **(n)** | **Reference [5] prints "T.-P. Chen, L. Su et al."** — an "et al." after both authors of a two-author paper (§7.4). | No |
| **(o)** | **Figure 5 labels the comparator "AugNet (2022)" where Table 1 labels it "AugNet (2021)"** — the paper's §5.3 explains that the Figure 5 models are the updated ones, so this is **not** an inconsistency, but the two labels differ and only the surrounding prose says why. | No |

**★ (p) ONE AMBIGUITY IN FIGURE 5's OWN COLOUR LEGEND, RECORDED BECAUSE IT GOVERNS HOW THE FIGURE IS
READ.** §5.4 gives the legend: "Marked in red are false predictions, and marked in yellow are correct
predictions of the model with wrong ground-truth annotations." **But Figure 5's own caption says "The red
(wrong) markings on Human Analysis and AugNet (2022) are from [21]"** — so red appears on the *Human
Analysis* row, which is not a prediction and cannot be a "false prediction" under §5.4's legend. **The two
statements do not define the same thing for the same mark**, and the figure carries red on a row the
legend's wording does not reach.

**★ (q) TABLE 1's DASH IS DEFINED FOR ONE CELL AND USED FOR SEVERAL DIFFERENT THINGS.** The caption
explains exactly one: "Note that model *CSM-T* reports *Mode* instead of *Quality*", which accounts for
the dash in that one cell. **The other dashes are left undefined** — CSM-T's Degree and Inversion,
Micchi's Root, Micchi's and CSM-T's RN_alt, and the whole RN(Onset) column for the three comparators —
and a reader cannot tell from the table whether a dash means the model does not perform the task, does
not report it, or reports something not comparable. No printed value moves.

**★ (r) §5.2's LIST OF WHAT WAS TESTED DOES NOT MAP CLEANLY ONTO TABLE 2's FIVE ROWS.** §5.2 says the
architecture was tested "using the dynamically weighted loss described in Section 3.3 (same as the model
in Table 1), **Rotograd [17] and GradNorm [16] for Gradient Normalization**, and NADE [8]". Table 2's five
rows are Baseline, WLoss, Rotograd, **R-GradN** and NADE, and its caption defines R-GradN as "Rotograd
with Gradient Normalization". **So there is no row for GradNorm on its own.** The sentence admits two
readings — that Rotograd and GradNorm were each tested as gradient-normalisation methods, in which case a
tested method has no row; or that Rotograd and GradNorm name the two components of R-GradN, in which case
the list is complete. **The paper does not say which**, and no printed value moves either way.

### §7.2 What the paper leaves without a value — a later reader must not assume these are answered elsewhere in the eight pages

- **The number of convolutional layers `L`.** Named as a symbol in §3.3, given no value anywhere.
- **Epochs, batch size, early stopping, model selection, seeds.** §4.2 lists five hyper-parameters and
  none of these.
- **The unit of Table 2's ±** (§6.6).
- **Whether Table 1's figures are single runs or means** (§6.5).
- **The post-processed score of the 14-task model.** §5.3 says "up to two additional percentage points"
  and prints no number (§5.3 of this file).
- **Whether the six corpora overlap beyond the one pair the paper names**, and whether the part of WiR
  taken excludes WTC (§2.9).
- **Whether the MPS data enter the test split** (§6.8).
- **Any accuracy at all for five of the eleven-or-ten heads.** Table 1 reports Key, Degree, Quality,
  Inversion, Root, RN, RN(Onset) and RN_alt. **It reports nothing for Harmonic Rhythm, Tonicization, Pitch
  Class Sets, Bass, or the restricted common-RN vocabulary** — the four additional tasks the paper
  introduces from [7] and the fifth that RN_alt is built from. **So the tasks the paper adds to improve
  the Roman Numeral are never scored on their own terms anywhere in the eight pages.**
- **How metrical position is encoded** as a node feature (§3.1 of this file).
- **Any tie-break for which node survives the edge contraction** (§2.5).
- **Any uncertainty, alternative-reading or confidence surface** (§3.2 of this file).
- **The relation between this arXiv v2 text and the proceedings camera-ready** (§1.2).

### §7.3 ★ WHAT IS BOTH MEASURED AND STRUCTURAL HERE, for a reader deciding what this paper can bear

*(This section says what a consumer could rest on. It proposes nothing and recommends nothing.)*

1. **The co-occurrence result (§6.4) is the most transferable thing in the paper, and it does not depend
   on the architecture.** It is arithmetic on published values of TWO different models on TWO test sets,
   and it says the same thing in all six rows: the components of a Roman Numeral fail together. **It is
   bounded** by CSR being duration-weighted (§6.4's own bound), and it is **six rows of two models**, not a
   general law.
2. **The onset as the unit of prediction is a structural claim with a working demonstration.** The edge
   contraction (§2.5) is a concrete mechanism for going from note-level evidence to onset-level decisions,
   and the paper reports an onset-wise accuracy column beside the time-weighted one. **What the paper does
   NOT supply is a measurement isolating the representation**: ChordGNN differs from the frame-based
   comparators in encoder, pooling and loss together (claim C4 of §4).
3. **Post-processing over concatenated task logits improves the joint label in all four printed pairs**
   (§5.1's table; BPS RN 46.2→49.1 and RN_alt 48.6→50.4; Full RN 48.9→51.8 and RN_alt 50.4→52.9).
   **This is a measured, repeated effect with a stated mechanism** (§2.8), and it is the paper's own answer
   to the task-interdependence problem it raises in §1. It is also the effect §6.2 shows the
   without-post-processing claims depend on.
4. **Gradient-normalisation techniques measured BELOW the plain baseline on this problem** (§6.7), which
   is a stronger and cleaner negative result than the conclusion's wording claims for it.
5. **★ AND ONE THING THE PAPER ITSELF ATTRIBUTES ELSEWHERE.** The qualitative musical argument of §5.4 —
   the vii° passage, the cello's F♯, and the two conflicting readings — is, by the acknowledgements'
   own words, "the musical analysis … that was **offered by an anonymous reviewer**, and which we took the
   liberty of adopting for our text" (§5.4 of this file). **A reader weighing that argument should know it
   is the reviewer's and not the authors', because the paper says so.** No verdict is taken on the
   argument itself.

### §7.4 The reference list, transcribed, and the bound on what it shows

*(Transcribed from PDF pages 7 and 8. Abbreviated venue strings are the paper's own.)*

[1] Pauwels, O'Hanlon, Gómez, Sandler et al., "20 years of Automatic Chord Recognition from Audio," ISMIR
2019. · [2] D. Temperley, *The cognition of basic musical structures*, MIT press, **2004**. · [3] Raphael
& Stoddard, "Functional Harmonic Analysis Using Probabilistic Models," *Computer Music Journal* 28(3),
45–52, 2004. · [4] Magalhaes & de Haas, "Functional Modelling of Musical Harmony: an experience report,"
*ACM SIGPLAN Notices* 46(9), 156–162, 2011. · [5] T.-P. Chen, L. Su **et al.**, "Functional Harmony
Recognition of Symbolic Music Data with Multi-task Recurrent Neural Networks," ISMIR 2018. · [6] Micchi,
Gotham & Giraud, "Not all roads lead to Rome: Pitch representation and model architecture for automatic
harmonic analysis," *TISMIR* 3(1), 42–54, 2020. · [7] Nápoles López, Gotham & Fujinaga, "AugmentedNet: A
Roman Numeral Analysis Network with Synthetic Training Examples and Additional Tonal Tasks," ISMIR 2021. ·
[8] Micchi, Kosta, Medeot & Chanquion, "A deep learning method for enforcing coherence in Automatic Chord
Recognition," ISMIR 2021. · [9] McLeod & Rohrmeier, "A modular system for the harmonic analysis of musical
scores using a large vocabulary," ISMIR 2021. · [10] Jeong, Kwon, Kim & Nam, "Graph Neural Network for
Music Score Data and Modeling Expressive Piano Performance," ICML 2019. · [11] Karystinaios & Widmer,
"Cadence Detection in Symbolic Classical Music using Graph Neural Networks," ISMIR 2022. · [12]
Karystinaios, Foscarin & Widmer, "Musical Voice Separation as Link Prediction," IJCAI 2023. · [13]
Hernandez-Olivan, Llamas & Beltran, "Symbolic Music Structure Analysis with Graph Representations and
Changepoint Detection Methods," **2023** (no venue printed). · [14] Zhang, Luo, Loy & Tang, "Facial
Landmark Detection by Deep Multi-task Learning," ECCV 2014. · [15] Guo, Haque, Huang, Yeung & Fei-Fei,
"Dynamic Task Prioritization for Multitask Learning," ECCV 2018. · [16] Chen, Badrinarayanan, Lee &
Rabinovich, "GradNorm," ICML 2018. · [17] Javaloy & Valera, "RotoGrad," ICLR 2022. · [18] Navon,
Shamsian, Achituve, Maron, Kawaguchi, Chechik & Fetaya, "Multi-task Learning as a Bargaining Game," ICML
2022. · [19] Hamilton, Ying & Leskovec, "Inductive representation learning on large graphs," *NeurIPS* 30,
2017. · [20] Liebel & Körner, "Auxiliary tasks in multi-task learning," arXiv:1805.06334, 2018. · [21] N.
Nápoles López, "Automatic roman numeral analysis in symbolic music representations," Ph.D. dissertation,
Schulich School of Music McGill University, December 2022. · [22] Neuwirth, Harasim, Moss & Rohrmeier,
"The Annotated Beethoven Corpus (ABC)," *Frontiers in Digital Humanities* 5, p. 16, 2018. · [23] N.
Nápoles López, "Automatic Harmonic Analysis of Classical String Quartets from Symbolic Score," **Ph.D.
dissertation, Master's thesis**, Universitat Pompeu Fabra, 2017. · [24] Devaney, Arthur, Condit-Schultz &
Nisula, "TAVERN," ISMIR 2015. · [25] Gotham, Tymoczko & Cuthbert, "The RomanText Format," ISMIR 2019. ·
[26] Gotham & Jonas, "The Openscore Lieder Corpus," MEC 2021. · [27] Nápoles López & Fujinaga, "Harmonic
Reductions as a Strategy for Creative Data Augmentation," Late-Breaking Demo at ISMIR 2020. · [28]
Hentschel, Neuwirth & Rohrmeier, "The Annotated Mozart Sonatas: Score, Harmony, and Cadence," *TISMIR*
4, **no. ARTICLE**, 67–80, 2021. · [29] C. Harte, "Towards automatic extraction of harmony information
from music signals," Ph.D. dissertation, Queen Mary University of London, 2010.

**★ WHAT THIS LIST SHOWS, AND THE BOUND ON SAYING IT.** Twenty-nine references. **[6], [7], [8] and [9]
are the four models the paper measures itself against**, and [7] additionally supplies its task
decomposition, its splits, its augmentations and its 98 % figure. **[11] and [12] are the first author's
own.** **[14] to [20] are general machine-learning sources**, not music ones. **NOT claimed:** any count
of how many references fall in any category beyond the ones named here, or any statement about what this
list omits — this read enumerated no literature of its own and is in no position to say what is missing.

**★ ONE DISAGREEMENT BETWEEN THIS PAPER'S REFERENCE [2] AND THIS PROJECT'S OWN BIBLIOGRAPHY, RECORDED
WITH NO VERDICT.** This paper prints Temperley, *The cognition of basic musical structures*, MIT press,
**2004**. `docs/research_papers/BIBLIOGRAPHY.md`, read by this side this sitting, prints the same book as
**(2001)**. **Both values are recorded and neither is called right**: this read checked no third source,
and this project's bibliography is not an authority on a publisher's date.

---

## §8 — The read-back and the sweep, written in the act that ran them

### §8.1 What the read-back was, and which pages it re-opened

After §0 to §7 were written and before this file was landed, **SEVEN of the eight pages were re-opened —
pages 2 through 8**, in three requests — pages 2–3, pages 4–5, pages 6–8 — and each assertion of this file
was checked at the page it cites. **PAGE 1 WAS NOT RE-OPENED**, and it is the page carrying the title, the
authors, the licence block and the abstract, **so §1's identity items and §1.3's quotation of the abstract
rest on a single reading of that page** where everything else in this file rests on two or three.

*(★ CORRECTED AT THE USER-ORDERED CHECK. FORMER WORDING, PRESERVED (#12): "**every page of the paper was
re-opened**" — **refuted by the three requests named in the same sentence**, which cover pages 2 through 8.
It is a count of this side's own acts wrong against the list beside it, which is the tell §8.3 reports.)* **Every image was present and legible, checked at the image and not at the call's success
line.** The page-image fault did not fire at any of the five requests this sitting made, which is **not**
evidence that it is gone.

**What the re-openings were for, named rather than counted:**

- **Pages 2 and 3** — to read Figure 1's caption word for word, and to **count the labelled heads in
  Figure 3 at the image** rather than from the first reading's impression. Both were the load-bearing
  checks of §6.9 and §6.10.
- **Pages 4 and 5** — to verify **every cell of Tables 1 and 2 against this file's transcription**, to
  read §5.1's two claim sentences and §5.2's list of tested configurations at their own words, and to
  read equation (2)'s printed summation.
- **Pages 6, 7 and 8** — to verify the conclusion's sentence, §5.3's figures, Figure 5's caption against
  §5.4's legend, the acknowledgements, and the five reference entries this file singles out.

**Tables 1 and 2 came back identical to this file's transcription, cell for cell**, bolding included.
**Figure 3's ten labelled heads and Figure 4's ten on each side were counted at the images.** Figure 1's
caption, the conclusion's sentence and the five reference entries came back word for word as transcribed.

### §8.2 What the read-back and the sweep struck in this side's own writing

**Every correction is at its own site above with the former wording preserved (#12).** Named rather than
counted:

- **An absolute over this file that this file itself refutes.** The header said "THE PAPER IS THE ONLY
  SOURCE FOR EVERY VALUE BELOW", where §0 carries a byte size from this side's own staging call and a
  transcribed candidacy row, and §7.4 carries a date from this project's bibliography. **The three are now
  named in the sentence.**
- **A uniqueness claim over a space never enumerated.** §6.1 said the relative reading is "the only
  reading of the printed values that produces 11.6". **What this side actually tested is now named** — six
  comparisons — and the claim is bounded to them.
- **A STATEMENT ABOUT A FILE THIS READ HAD NOT OPENED.** §7.1's preamble said the defects listed there are
  not defects "of either extract", written in a section produced before the first extract was opened at
  all. **Corrected to say what this read could say: not defects of THIS file.**
- **This side's own inference offered as the caption's.** §2.11 said Table 1's dashes mark "the absence of
  a comparable number". **The caption defines the dash for exactly one cell and nowhere in general**; the
  inference is withdrawn and the fact is now a finding at §7.1(q).
- **A quantifier over an un-enumerated set.** §6.6 said "every conclusion §5.2 draws from Table 2"
  depends on the unit. **§5.2 draws two and they are now named.**
- **An unbounded negative over the paper.** §6.4 said "the paper measures none of them". **Bounded to the
  eight pages as read.**
- **An imported word the paper does not use.** §3.2 said the logits are used "beyond argmax". **The paper
  never says how a prediction is taken from a head's output**, and the sentence now says that instead.
- **A description of equation (2) that understated what is printed.** This file said the sum is over
  `v`'s neighbourhood rather than `u`'s. **What is printed is `Σ_{v ∈ N_On(v)}` — the summation variable
  and the neighbourhood's argument are the same symbol** — which is a stronger statement, verified at a
  second opening.

**What the read-back ADDED rather than struck**, because it found things the first writing did not have:

- **§5.1's closing sentence, "*ChordGNN* without post-processing already surpasses the other models"**,
  which has the same shape as the "all fields" sentence and fails on the same RN_alt cell. Written into
  §6.2.
- **§7.1(q)**, the undefined dash.
- **§7.1(r)**, the mismatch between §5.2's list of tested methods and Table 2's five rows.

### §8.3 The degradation tells, reported unprompted

**Two of the user's named degradation tells fired in this side's own writing**, and under the standing
rule of 2026-08-15 that is reported rather than left to be noticed. **The instances are NAMED and
deliberately NOT totalled.**

**Tell — a count, a proportion or a superlative put on this side's own reading without deriving it.**
*(i)* "THE PAPER IS THE ONLY SOURCE FOR EVERY VALUE BELOW", an absolute about this file refuted by this
file. *(ii)* "the only reading of the printed values that produces 11.6", a uniqueness claim over a space
never enumerated. *(iii)* "every conclusion §5.2 draws", a quantifier over a set never listed. **All three
were caught at the sweep and struck at their sites.** *(iv)* **★ AND A FOURTH, CAUGHT ONLY AT THE
USER-ORDERED CHECK THAT RAN AFTER THIS SECTION WAS FIRST WRITTEN: §8.1 SAID "every page of the paper was
re-opened" AND NAMED THREE REQUESTS COVERING PAGES 2 THROUGH 8.** **Page 1 was not re-opened**, so the
sentence is refuted by the list standing inside it. **It is the worst-placed of the four**, being a false
statement about the thoroughness of the very pass this section exists to report, **and it was missed by
both the sweep and the cross-check** — which is the plainest evidence in this file that a further pass
does not come back empty.

**Tell — an assertion about a thing this side had not examined.** *(iv)* §7.1's preamble said the listed
defects are not defects "of either extract", **written before the first extract had been opened**. *(v)*
§2.11 stated as the caption's meaning something the caption does not say. **Both caught at the sweep.**

**★ THAT EVERY ONE WAS CAUGHT BY A PASS OF THIS SIDE'S OWN DOES NOT LOWER THE COUNT.** The three entries
this line most recently produced each record exactly that of their own sittings, and this one records it
too.

**★ AND ONE CONTAMINATION IS DECLARED RATHER THAN CAUGHT, because it was never hidden.** The idea of
testing the reconstructed Roman Numeral against the product of its components (§6.4) came from the handoff
entry that booted this session, which records the previous member's read finding the same shape. **The
arithmetic is this read's own on this paper's values; the idea of looking is not**, and it is declared at
the site as well as here.

### §8.4 The bound on this section

**The read-back caught what the writing did not, and the sweep caught what the read-back did not.** Both
are further passes over the same writing by the same side. **Nothing here establishes that a third pass
would come back empty**, and two of what the sweep found are instances of the very tell this section
reports.

**What neither pass did:** neither ran any web access, opened the first extract, swept this repository, or
read any file of this project other than the ones §0 names. **Neither changed a transcribed value of the
paper.** Every value in §5 is as it was first written, and the read-back's whole yield on the tables was
agreement.

---

## §9 — The cross-check against the first extract, written in the act that ran it

### §9.1 What the cross-check was, and the independence bound

**This file was landed and proved BEFORE the first extract was opened** — §0 to §8 committed twice, staged
back, and proved at its last content line read and at its size. **Only then was
`reading_pass/extracts/karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks.md`,
50,392 bytes, staged and read whole.** Its own banner records it as a first-pass read at the object, dated
2026-09-06.

**Every disagreement was resolved AT THE PAPER**, by a third opening of the pages carrying the disputed
text, and not by preferring either file.

**★ THE BOUND, AND IT IS LARGE.** The first extract's work divides in two. **One half is about this
paper**, and that half is what this cross-check compares. **The other half is about THIS PROJECT'S
RECORD** — its verification of `FRAMEWORK.md` DP-A's figures and §S4(a)'s sentence, of
`population.md`'s V8 and V9, its bibliography and redistribution-tier findings, its eight-places claim,
its routing of five findings, and its statements about rows 18, 20, 28, 45, 47 and 48. **This side opened
none of those files and takes NO POSITION on any of it.** On that half this is silence, not a second
opinion.

### §9.2 What both reads transcribed, and where they agree

**★ EVERY PRINTED CELL BOTH READS TRANSCRIBED AGREES.** Table 1 was transcribed whole by both — both
blocks, all eight rows, all eight columns, dashes included — and **the two transcriptions match cell for
cell**. Table 2 was transcribed whole by both, values and ± alike, and **matches cell for cell**. Every
protocol constant both carry agrees: AdamW, 256, 0.0015, 0.005, 0.5; 32nd-note granularity; 7 flats or
sharps; approximately 300 training and 56 test pieces; 32 Sonata first movements; 7 Beethoven piano
sonatas; v1.9.1; 2 GRU layers; 53.5; 11+3=14. The held file's size agrees at 1,933,753 bytes. The
identity agrees in full — title, both authors, both affiliations, the arXiv stamp, the CC BY 4.0
attribution box and its ISMIR wording.

**★ AND FIVE THINGS THE TWO READS REACHED INDEPENDENTLY AND BY THE SAME REASONING, WHICH IS THE STRONGEST
RESULT THIS CROSS-CHECK PRODUCED:**

1. **That §5.1's "all fields" sentence is untrue of two further fields** — Inversion at 0.0, a tie rather
   than a surpassing, and RN_alt at −1.1 — **both on the without-post-processing half**. This read's
   §6.2 and the first extract's finding (5) reach the same two cells by the same arithmetic. **Neither
   read saw the other.**
2. **That the "11.6 %" is a relative figure and not percentage points**, both computing 5.4 / 46.4.
3. **That Table 2's ± values are not in a consistent unit with the values beside them**, and that the
   paper does not say which is meant.
4. **That Table 1 prints no uncertainty on any cell.**
5. **That the task count does not close** — the text's eleven against ten labelled heads in Figures 3 and
   4 — **and that the degree-splitting reconciliation is a conjecture the paper does not state.**

### §9.3 ★ The disagreements — three, all against the first extract, all resolved at the paper, and none moves a transcribed value

**(a) A QUOTATION WHOSE WORDS ARE NOT THE PAPER'S, AT §3.1.** The first extract quotes: *"[7] indicated
that only three tasks would be sufficient **for** 98% of the Roman Numeral annotations in our dataset."*
**The paper prints: *"However, [7] indicated that only three tasks would be sufficient TO REACH 98% of the
Roman Numeral annotations in our dataset (detailed in Section 4.1)."*** — established at the printed §3.1
at the whole read and again at a third, separate opening of that page at this cross-check. The
parenthetical cross-reference is also dropped. **The sense is unchanged and no value moves.**

**(b) A CHANGED WORD INSIDE A QUOTATION, TOGETHER WITH A WRONG SECTION LOCATOR.** The first extract
quotes, and cites to **§3.1**: *"we replace the CNN encoder that works on quantized frames of the score in
previous approaches, with a **graph convolutional network** followed by an edge contraction layer"*. **The
paper prints "with a GRAPH CONVOLUTION followed by an edge contraction layer", and the sentence stands in
§3.2**, in the continuation of "Graph Representation of Scores" in the right-hand column — established at
a third opening of that page. **Two defects in one citation, and neither moves a value.** The changed word
is not neutral in kind: *graph convolution* names an operation and *graph convolutional network* names an
architecture, and the paper's own sentence is about replacing one encoder component with another.

**(c) TWO SMALL DEPARTURES INSIDE THE §3.3.1 QUOTATION, WHICH THAT FILE GIVES AS ITS CENTRAL EVIDENCE FOR
THE VERIFIED MECHANISM.** It quotes *"**The** post-processing phase combines the logits … concatenating
them **and then,** feeds them"*. **The paper prints *"**Our** post-processing phase combines the logits …
concatenating them **and, then,** feeds them"*** — established at a third opening of PDF page 4. **The
sense is unchanged and no value moves.** It is recorded because that quotation is the one the first
extract's own verification of a ratified item rests on, and a quotation carrying a verification is the
one that most needs to be exact.

**★ AND ONE THING THAT IS NOT A DISAGREEMENT AND IS RECORDED SO IT IS NOT MISTAKEN FOR ONE.** The first
extract writes, immediately after quoting Table 1's caption, "A dash is printed where the model reports no
value." **The caption does not say that** — it explains one dash only, CSM-T's Quality. The gloss is that
file's own and is unmarked as such, and **this read does not contradict it**: it is a plausible reading
and this read found no cell that refutes it. **This file's §7.1(q) records the same fact from the other
side — that the paper leaves the dash undefined.** The two treatments differ; the paper settles neither.

### §9.4 What the first extract has that this read did not — adopted here and marked at its site

**Two difference sets, both adopted into §6.4a and re-derived there at this file's own transcription of
Table 1** rather than copied from that file's text:

1. **The post-processing gain as explicit differences** — +2.9, +1.8, +2.9, +2.5 — and with it the fact
   that **the Roman-numeral gain is the same +2.9 on both test sets**.
2. **The onset-wise column against the duration-weighted one** — +0.4, +0.3, −0.5, −0.6 — **never more
   than 0.6, and the sign not constant between the sets.** This is a measured statement about how much the
   evaluation grid moves the figure, and this read had both columns and had not differenced them.

**And one NARROWING of this read's own, forced by the comparison and made at its site (§6.10).** This file
first said the degree-splitting reconciliation of the eleven-against-ten task count "does not work". **The
first extract labels the same reconciliation an explicit CONJECTURE and leaves the discrepancy as
printed.** Re-read at the paper, §3.1's sentence is about how the Roman Numeral prediction is decomposed
and does not settle the number of heads, **so the reconciliation is live and this file's wording was too
strong.** Corrected with the former wording preserved (#12), **and recorded here so that this
cross-check's ledger is not read as one-sided.**

### §9.5 What this read has that the first extract does not

**Named rather than counted.** The four that bear on how a printed value or a stated claim of the paper is
read are:

- **★ FIGURE 1's CAPTION NAMES AN INVERSION ITS OWN STATED ROOT AND BASS CONTRADICT** (§6.9) — "second
  inversion" where the figured bass ⁶₅ and the caption's own "root is D, bass is F sharp" both give first
  inversion. **This is the one with a musical consequence**, because Figure 1 is where the paper explains
  to a reader what its inversion task means.
- **★ THE RECONSTRUCTED ROMAN NUMERAL EXCEEDS THE PRODUCT OF ITS OWN COMPONENT ACCURACIES IN ALL SIX ROWS
  THAT PRINT ALL FIVE** (§6.4), by between 14.9 and 21.7 points, and by MORE for ChordGNN than for AugNet
  on both test sets. *(The idea of testing this is a declared boot contamination, §8.3; the arithmetic is
  this read's own.)*
- **★ §5.3's 53.5 IS INVITED INTO A COMPARISON WITH TABLE 1's 48.9 ACROSS TWO SIMULTANEOUS CHANGES — the
  task set and the corpus — WITH THE TEST-SET COMPOSITION NEVER STATED** (§6.8).
- **★ THE ACKNOWLEDGEMENTS ATTRIBUTE §5.4's WHOLE MUSICAL ARGUMENT TO AN ANONYMOUS REVIEWER** (§5.4 and
  §7.3) — "which we took the liberty of adopting for our text". The first extract transcribes §5.4's
  argument and does not record its stated authorship.

**The rest are at §7.1 and §7.2 rather than listed here** — among them the four reference-list defects,
the undefined dash, §5.2's list of tested methods against Table 2's five rows, Figure 5's colour legend
against its own caption, the six-against-five shift between §2 and §3.1, and equation (2)'s printed
self-referential summation.

### §9.6 What the cross-check does NOT establish

- **NOT that either read is complete.** It ran over what both files carry. A later reader may find more in
  either.
- **NOT that the agreements prove correctness.** Two reads of the same eight pages can be wrong together,
  and the cells they agree on were transcribed from the same images.
- **NOT anything about the first extract's repository half** (§9.1), which this side did not open.
- **NOT that the three disagreements are all of them.** They are the ones this comparison surfaced.
- **AND NOT that this read was the better one.** It produced no contradiction at the paper against itself
  and one narrowing forced by the other file, where the other produced three against itself — **but the
  first extract also carries a whole half this read did not attempt at all**, and it reached four of this
  read's five load-bearing findings independently.

---
