# EXTRACT — Karystinaios & Widmer, "Roman Numeral Analysis with Graph Neural Networks: Onset-wise Predictions from Note-wise Features" (ChordGNN) — Task B candidacy row 49, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-06).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the remedial commission
> (`cowork_reading_pass_remedial_commission_2026_08_31.md` §3) binds unchanged.
>
> **The grade.** All eight pages of the held PDF were read AT THE OBJECT: staged through the bridge
> and read with the file tools as page images. **No relay, no web-fetch read, no prompted
> extraction.** The held document is an arXiv deposit and prints no proceedings page numbers, so
> every location below is given as the printed section, table or figure number together with the
> page of the eight-page document. **Page 5 — the page carrying Table 1 and Table 2, from which
> every value in this extract is taken — was read a second time and every transcribed cell
> re-checked against the image.**
>
> **★ ROW 49 IS GROUP 3's THIRD MEMBER** ("the scoring architecture and its fitting",
> `reading_pass/candidacy_upgrades.md` line 177), after rows 45 and 48. **Two ratified items rest on
> it**: DP-A's *"a learned reconciliation pass over all heads, raising the Roman numeral from .462
> to .491"*, and `population.md` V8's onset-level representation. **The first of them is a FIGURE
> rather than a description, which the progress record's carried item (a) states is new for group 3
> — derived at the progress record read whole this session, where group 3's other read members are
> rows 45, whose item is a quotation, and 48, whose item is a structural description.** **Both
> verifications were
> performed FIRST, before anything else was extracted**, exactly as the progress record's carried
> items (a) asked. See "The verification target" below.
>
> **Where the record cites this paper, established by `Grep` of the staged tree BEFORE extracting,
> never inherited. What was searched and where, stated as a rule rather than as a tally.** Over the
> staged tree: the bare word **"ChordGNN"**, the split spelling **"Chord GNN"**, the bare author
> name **"Karystinaios"**, the arXiv identifier **"2307.03544"**, and **"onset-wise"** in both cases
> — bare words as well as phrases, on the method fact the row 47 read carried forward (a phrase can
> be split across a line break; here none was). **And a second sweep for the FIGURE rather than the
> identity** — **".462"**, **".491"**, **"46.2"**, **"49.1"**, **"reconciliation pass"** and
> **"coherence"** — on the method fact the row 48 read carried forward, that a live recorded ground
> can state a paper's contribution while naming neither the paper, the system nor any author.
> **`FRAMEWORK.md` DP-A and §S4(a) were also READ WHOLE, not only searched.**
>
> **The record bears on this paper in EIGHT places outside this line's own working files.** The
> candidacy row (`reading_pass/candidacy_upgrades.md` line 121); the slice derivation
> (`cowork_l2_task_b_slice_derivation_2026_09_05.md` line 84); the bibliography
> (`docs/research_papers/BIBLIOGRAPHY.md` line 68); **`FRAMEWORK.md` DP-A lines 679–680, the LIVE
> ground**, which states the reconciliation pass and its figures while naming neither the paper, the
> system nor any author; **`FRAMEWORK.md` §S4(a) lines 1564–1565**, the sealed first-stage text,
> which does name ChordGNN; `reading_pass/population.md` line 109 (**V8**) and line 110 (**V9**);
> and `cowork_reading_pass_findings_2026_08_31.md` line 187, which prints a figure for this system
> inside the DP-C block's BACHI item.
>
> **★ THE METHOD FACT ROW 48 PAID FOR WORKED HERE, AND ITS LIMIT IS NOW VISIBLE.** DP-A's sentence
> about THIS system carries the two figures, so the figure sweep reached line 680 where an
> identity search could not. **Row 48's sentence, in the same paragraph, carries neither that
> paper's identity nor any figure**, which is why that read found it only by reading DP-A; the claim
> here is about those two kinds of token and not that no string in it is searchable. **So the lesson
> stands in its stronger form:
> search the identity, search the figure, AND read the design point's own text; a ground stated as a
> description alone carries no token for either search.**
>
> **Recorded so they are not mistaken for citations of this paper:** the bare-word "Karystinaios"
> hits at `docs/research_papers/BIBLIOGRAPHY.md` lines 52 and 83, at
> `reading_pass/candidacy_upgrades.md` lines 100, 142 and 220, at `reading_pass/population.md` lines
> 102 and 107 and in the progress record's row 20 finding are **other works by an overlapping author
> set** — the 2022 cadence-detection graph network (candidacy row 38), Dilemmadata (row 59) and
> AnalysisGNN (row 52) — not this paper. **The bound on the eight-place claim:** it is a claim about
> the files in this session's staged tree, which the provenance below enumerates, and not about
> every file in the repository.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## ★ The verification target (a) — the ratified FIGURE, CONFIRMED at the primary, with three precisions

The record states the item in three places and attributes the mechanism in the third:

- **`FRAMEWORK.md` DP-A, lines 679–680 (the LIVE ground):** *"…a learned reconciliation pass over
  all heads, raising the Roman numeral from .462 to .491; …"* — **the paper is not named here.**
- **`FRAMEWORK.md` §S4(a), lines 1564–1565 (the sealed first-stage text):** *"ChordGNN adds a
  learned reconciliation pass over all heads and measures the Roman numeral rising from .462 to
  .491"*.
- **`reading_pass/population.md` V9, line 110:** *".462→.491 = ChordGNN 2023, Table 1, BPS set
  (ChordGNN RN 46.2 → ChordGNN+Post 49.1, the learned coherence post-processing of Micchi et al.
  2021)"*.

**So the question was the one the progress record set: are those two cells at that table, in that
condition, and is the post-processing what the record says it is?**

**BOTH CELLS CONFIRMED, at Table 1, page 5.** Table 1 is split into a **BPS** block and a **Full**
block. In the BPS block, the RN column reads **ChordGNN (Ours) 46.2** and **ChordGNN+Post (Ours)
49.1**. The locator is exact: the table, the set and the two rows are all as V9 states them. The
whole of Table 1 is transcribed in "The measured results" below, so the pair can be read in its
context.

**THE MECHANISM CONFIRMED.** §3.3.1 "Post-processing", page 4, in the paper's own words:

> *"We enhance our model with a post-processing phase after the model has been trained. The
> post-processing phase combines the logits of all tasks' predictions by concatenating them and
> then, feeds them to a single-layer bidirectional LTSM block. Then, again the embeddings of the
> sequential block are distributed to 11 one-layer MLPs, one for each task."*

*(«LTSM» is the paper's own spelling and is recorded as printed.)* Figure 4, page 4, draws it:
"Previous Predictions" (the ten labelled heads) → CONCATENATE → LSTM → ten MLPs → "New
Predictions". **A learned pass over all heads is exactly what it is, so nothing is owed to DP-A's
or §S4(a)'s sentence as a structural claim, and no STOP of either class fires on this item.**

**PRECISION (1) — THE PASS IS APPLIED AFTER THE DECIDING, AND THE PAPER SAYS SO IN TERMS.** The
first words of §3.3.1 are *"after the model has been trained"*; the input to the pass is the eleven
heads' logits and its output is a fresh prediction for each of the same eleven tasks. **So the
separation is undone after the deciding, not in it** — the eleven heads still sit on one shared
encoder and are still decided in one pass, which is the shape DP-A excludes. This is the same
distinction row 48's read recorded for AugmentedNet's re-fusion (its finding (2), reconstruction
rather than deciding), reached here at a different mechanism and stated by the authors themselves.
**Recorded BESIDE row 48's finding (2), row 47's finding (3) and row 45's finding (1), and merged
with none.**

**PRECISION (2) — V9's PARENTHESIS ATTRIBUTES THE POST-PROCESSING TO A WORK THIS PAPER CITES FOR
SOMETHING ELSE.** V9 calls it *"the learned coherence post-processing of Micchi et al. 2021"*. At
the object, **§3.3.1 cites nothing at all**; the mechanism is presented as the authors' own. The
paper's Micchi citations are **[6]**, the 2020 CRNN (candidacy row 45), and **[8]**, *Micchi,
Kosta, Medeot & Chanquion, "A deep learning method for enforcing coherence in Automatic Chord
Recognition," ISMIR 2021* — and **[8] is cited for NADE**, which is a different mechanism the paper
describes at §2, page 2, as *"introducing intra-dependent layers to inform in an orderly fashion
the prediction of one task with the previously predicted task"*, and which appears as its **own
separate row of Table 2**, distinct from the post-processing. **So the two values verify, V9's
VERIFIED verdict does not move, and what is precise is the parenthesis's attribution.** Routed to
the findings surface's V9 row; **applied nowhere.** See finding (4) for what [8] settles.

**PRECISION (3) — TABLE 1 PRINTS NO UNCERTAINTY OF ANY KIND, so the 2.9-point difference the record
rests on is a single run with nothing beside it** (#24). Table 2 does print a spread — five repeats
of five configurations, mean ± value — but Table 2 is on the **Full** test set and **without
post-processing**, so it does not bound the BPS pair. **And Table 2's ± values are recorded as
printed and not reconciled:** they read 0.001 to 0.010 beside values printed as 45.2 to 50.4, which
is not a consistent unit; the paper does not say which. What can be said either way is that every
difference Table 2 shows between configurations is larger than the spread printed on either cell it
is taken from — but that is a statement about Table 2, not about the record's BPS pair.

## ★ The verification target (b) — V8's onset-level representation, CONFIRMED

`reading_pass/population.md` V8, line 109, cites this paper's **title + §1** for *"a recent
graph-based system replaces frame quantisation with one representation per onset and reports it as
the fix"*, quoting three things. All three verify:

- *"Onset-wise Predictions from Note-wise Features"* — the printed subtitle, page 1. **Verbatim.**
- fixed frames *"unnatural for scores… capturing varying amounts of musically relevant context"* —
  §1, page 1: *"However, such a representation is unnatural for scores and has the added practical
  disadvantage of being time-limited (for example regarding notes extending beyond the current
  window) and, due to the fixed-length (in terms of score time) constraint, capturing varying
  amounts of musically relevant context."* **Verbatim, the record's ellipsis compressing the
  time-limited clause.**
- edge-contraction pooling *"yields the learned representation at the onset level"* — §1, page 1:
  *"an edge contraction pooling layer that combines convolution at the note level but yields the
  learned representation at the onset level."* **Verbatim.**

§3.2, page 3, states the same as the design: *"Our approach to automatic Roman Numeral analysis no
longer treats the score as a sequence of quantized time frames but rather as a graph."* §2, page 2,
gives the authors' reason: *"Should a musicologist perform music analysis on a piece of music, they
would consider the individual notes existing in the score. Thus, a time frame representation would
come across as unnatural for symbolic music and in particular for such an analysis task."*
**Nothing is owed to V8.**

**ONE PRECISION, for the L1 charter rather than for V8.** The representation is **onset-wise
only**. The graph's nodes are notes and its edge types are *onset* (notes starting together),
*during* (one starting while another sounds), *follow* (one starting when another ends) and
*silence* (§3.2, page 3); the pooling contracts along the ONSET edges, so the sequence handed to
the recurrent part has one element per onset (§3.3, equations 2–3, page 4). **Offsets enter as edge
relations and not as partition points.** The record's L1 partition-point ground — Pardo and
Birmingham, whose partition points are the note onsets **and offsets** — is therefore a different
grid from this one, not the same one. Routed to the L1 and L2 detail specifications beside V8;
**V8's own wording, "one representation per onset", is exactly right and nothing is owed to it.**

## Identity — a MILD finding, of a shape new to this slice

**Printed title, page 1:** *"ROMAN NUMERAL ANALYSIS WITH GRAPH NEURAL NETWORKS: ONSET-WISE
PREDICTIONS FROM NOTE-WISE FEATURES"*. **Authors:** Emmanouil Karystinaios¹ and Gerhard Widmer^(1,2)
— ¹ Institute of Computational Perception, Johannes Kepler University Linz, Austria; ² LIT AI Lab,
Linz Institute of Technology, Austria. **The arXiv stamp down the left margin of page 1:**
*"arXiv:2307.03544v2 [cs.SD] 12 Jul 2023"*. **The attribution box at the foot of page 1:** *"© E.
Karystinaios and G. Widmer. Licensed under a Creative Commons Attribution 4.0 International License
(CC BY 4.0). **Attribution:** E. Karystinaios and G. Widmer, 'Roman Numeral Analysis with Graph
Neural Networks: Onset-wise Predictions from Note-wise Features', in Proc. of the 24th Int. Society
for Music Information Retrieval Conf., Milan, Italy, 2023."*

**The bibliography's row** (`docs/research_papers/BIBLIOGRAPHY.md` **line 68**) reads in full:
*"ChordGNN, ISMIR 2023 | https://arxiv.org/abs/2307.03544 | ✓ | LINK"*.

**(a) The row names NO AUTHORS**, as the progress record warned, so the page-1 check has only the
venue, the year and the URL to match on. **What the record does name is right:** `population.md` V8
writes *"ChordGNN (Karystinaios & Widmer 2023)"*, and that matches the printed authors exactly.

**(b) THE ROW'S TITLE IS THE MODEL'S NAME, NOT THE PAPER'S.** *ChordGNN* is not the printed title,
nor a prefix or leading word of it; it is the name the paper gives its model, printed in the
abstract and used throughout (§3.3, §4, §5). Rows 45, 47 and 48 each matched their bibliography
row's short title as a **prefix or leading word** of the printed title; this one matches nothing in
the printed title and is instead the system's name. **No "first" is asserted, and the reason is a
row this slice has already read: row 28's held document also prints a title unlike its bibliography
row's** — by a different route, a differently titled document rather than a model name. Recorded for
the bibliography reconciliation.

**(c) THE ARXIV-VERSUS-VENUE SHAPE DOES NOT PRODUCE A FINDING HERE.** The row says ISMIR 2023 while
the URL and the held file are arXiv, which is the shape that produced identity findings at rows 3,
10 and 11 — but this held arXiv deposit **prints the ISMIR camera-ready attribution box**, naming
the 24th ISMIR conference, Milan, 2023. **So the venue the row states is established at the held
document itself**, and whether the proceedings deposit differs from this v2 is not a question the
document leaves open in the way rows 3 and 10 did.

**(d) A TIER PRECISION.** The row's redistribution tier is **LINK**; the document prints **CC BY
4.0**, which is the register's own **CC** tier. Same shape as row 30's tier precision, in the same
direction as row 30's. Routed to the bibliography reconciliation.

**The input, established at §3.2, page 3: SYMBOLIC ONLY, AND SPELLED.** *"For our model, we used
pitch spelling, note duration, and metrical position features."* **No audio anywhere** — §2's first
sentence sets audio aside explicitly (*"we focus on the problem of automatic Roman Numeral Analysis
in the symbolic domain"*), and §6 names extending to audio as future work. **So no domain caveat
under the candidacy derivation's consequence (ii) applies to this row**: it is symbolic Western
classical music, our own input kind, and it is a **consumer of L0's given spelling**, as rows 45 and
48 are.

**Structure of the held document:** eight numbered sections — 1 Introduction; 2 Related Work; 3
Methodology (§3.1 Roman Numeral Analysis; §3.2 Graph Representation of Scores; §3.3 Model, with
§3.3.1 Post-processing); 4 Experiments and Corpora (§4.1 Datasets; §4.2 Configuration); 5 Results
(§5.1 Quantitative Results; §5.2 Configuration Study; §5.3 Latest developments; §5.4 A Musical
Example); 6 Conclusion; 7 Acknowledgements; 8 References. **Five figures, two tables, twenty-nine
numbered references** — the reference list runs [1] to [29] and was read whole. Eight pages.

**File:** `docs/research_papers/chordgnn_2023_arxiv.pdf` (1,933,753 bytes at this session's
`docs/research_papers/` listing, the one file of that listing whose name matches the row).

## Claims, labeled

### The task and the model (§1, §3, pages 1, 3–4)

- **[FACT]** The problem is automatic Roman numeral analysis of symbolic music, treated as a
  multi-task problem after [5]–[9]: *"the primary and secondary degree …, the local key at the time
  point of prediction, the root of the chord, the inversion of the chord, and the quality (such as
  major, minor, 7, etc.)"* (§2, page 2) — six components.
- **[FACT]** *"we replace the CNN encoder that works on quantized frames of the score in previous
  approaches, with a graph convolutional network followed by an edge contraction layer"* (§3.1,
  page 3).
- **[FACT]** The encoder is heterogeneous graphSAGE [19] over a note graph with the four edge types
  named above; after edge contraction the onset-level sequence passes through *"an MLP layer and 2
  GRU layers"*, and *"an MLP head is attached per task"* (§3.3, pages 3–4, Figure 3).
- **[FACT]** Training uses the dynamically weighted loss of [20], the per-task weights being
  *"learned scalars"* (§3.3, equation 4, page 4).
- **[FACT]** §3.1 states the two Roman numeral reconstructions it takes from [7]: *"Roman Numeral
  prediction involving the 5 tasks as conventional RN, and the combined prediction of key,
  inversion, and restricted RN vocabulary alternative RN, as RN_alt, in accordance with [7]."*
- **[FACT]** §3.1 states, of [7]'s restricted vocabulary: *"[7] indicated that only three tasks
  would be sufficient for 98% of the Roman Numeral annotations in our dataset."*
- **[FACT — and recorded as printed, not reconciled]** §3.3.1 and §5.3 both say the model has
  **eleven** tasks (*"11 one-layer MLPs, one for each task"*; *"now with 11+3=14 individual
  tasks"*), while **Figures 3 and 4 print TEN labelled heads** — Key, Degree, Quality, Inversion,
  Root, Com RN, Hrhythm, Bass, Ton Key, PC-set. *[CONJECTURE — this reader's, not the paper's: §3.1
  describes the degree as "primary and secondary", so the figures' single "Degree" box plausibly
  stands for two tasks. The paper does not say so, and the discrepancy is left as printed.]*
- **[FACT]** The tasks beyond the conventional ones are named at §3.1 and cited to [7]: Harmonic
  Rhythm, *"which is used to infer the duration of a Roman Numeral at a given time point"*;
  Tonicization, *"a multiclass classification task that refers to a tonicized key implied by the
  Roman Numeral label and is complementary to the local key"*; Pitch Class Sets, *"which includes a
  vocabulary of different pitch class sets"*; and the Bass task, *"which aims to predict the lowest
  note in the Roman Numeral label"*.

### The post-processing (§3.3.1, Figure 4, page 4)

- **[FACT]** Quoted in full under "The verification target (a)" above: after training, the logits of
  all tasks are concatenated, passed through a single-layer bidirectional LSTM, and redistributed to
  one-layer MLPs, one per task.

### Data, fitting and evaluation (§4, §4.1, §4.2, §5, pages 4–5)

- **[FACT]** *"We run experiments with our model in the exact same way as described in the paper
  [7], including the specific data splits, so that our results are directly comparable to the
  figures reported there."*
- **[FACT]** *"we compare our model with the updated version v1.9.1 of the state-of-the-art model
  Augmented-Net [21]"* — the [21] citation being Nápoles López's 2022 PhD dissertation.
- **[FACT]** Six data sources combined into one "Full" dataset: the Annotated Beethoven Corpus
  (ABC), the annotated Beethoven Piano Sonatas (BPS), the Haydn String Quartets (HaydnSun), TAVERN,
  a part of When-in-Rome (WiR), and the Well-Tempered-Clavier (WTC), *"which is also part of the WiR
  dataset"*. **300 pieces training, 56 testing**; the BPS test set *"includes 32 Sonata first
  movements"*; the full test set *"also includes the 7 Beethoven piano sonatas"*.
- **[FACT]** Augmentation is texturization [27] and transposition *"to all the keys that lie within
  a range of key signatures that have up to 7 flats or sharps"*, and *"the augmentations are only
  applied in the training split."*
- **[FACT]** §4.2: AdamW, hidden size 256, learning rate 0.0015, weight decay 0.005, dropout 0.5.
- **[FACT]** §5: *"As an evaluation metric, we use Chord Symbol Recall (CSR) [29] where for each
  piece, the proportion of time is collected during which the estimated label matches the ground
  truth label. We apply the CSR at the 32nd note granularity level, in accordance with [6,7,9]."*
  [29] is Harte's 2010 dissertation.

### The measured results (§5.1, §5.2, Tables 1 and 2, page 5)

**[FACT] Table 1, transcribed whole, both blocks, every cell re-checked at the image on a second
read of the page.** The caption states: *"RN stands for Roman Numeral, RN_alt for the alternative
Roman Numeral computations discussed in Section 3.1. RN(Onset) refers to onset-wise prediction
accuracy, all other scores use the CSR score (see Section 5). Note that model CSM-T reports Mode
instead of Quality."* A dash is printed where the model reports no value.

| Set | Model | Key | Degree | Quality | Inversion | Root | RN | RN (Onset) | RN_alt |
|---|---|---|---|---|---|---|---|---|---|
| BPS | Micchi (2020) | 82.9 | 68.3 | 76.6 | 72.0 | – | 42.8 | – | – |
| BPS | CSM-T (2021) | 69.4 | – | – | – | 75.4 | 45.9 | – | – |
| BPS | AugNet (2021) | 85.0 | 73.4 | 79.0 | 73.4 | 84.4 | 45.4 | – | 49.3 |
| BPS | ChordGNN (Ours) | 79.9 | 71.1 | 74.8 | 75.7 | 82.3 | **46.2** | 46.6 | 48.6 |
| BPS | ChordGNN+Post (Ours) | 82.0 | 71.5 | 74.1 | 76.5 | 82.5 | **49.1** | 49.4 | 50.4 |
| Full | AugNet (2021) | 82.9 | 67.0 | 79.7 | 78.8 | 83.0 | 46.4 | – | 51.5 |
| Full | ChordGNN (Ours) | 80.9 | 70.1 | 78.4 | 78.8 | 84.8 | 48.9 | 48.4 | 50.4 |
| Full | ChordGNN+Post (Ours) | 81.3 | 71.4 | 78.4 | 80.3 | 84.9 | 51.8 | 51.2 | 52.9 |

**[FACT] Table 2** — *"Configuration Study: Chord Symbol Recall on Roman Numeral analysis on the
full test set… Every experiment is repeated 5 times with the same ChordGNN model as Table 1 without
post-processing."* WLoss is the dynamically weighted loss of §3.3 (*"same as the model in Table
1"*), R-GradN is Rotograd with Gradient Normalization, and the baseline is *"the ChordGNN model
(without post-processing) with standard CE loss and no weighing"*.

| Variant | RN | RN_alt |
|---|---|---|
| ChordGNN (Baseline) | 46.1 ± 0.003 | 47.8 ± 0.007 |
| ChordGNN + WLoss | 48.9 ± 0.001 | 50.4 ± 0.010 |
| ChordGNN + Rotograd | 45.5 ± 0.003 | 47.1 ± 0.005 |
| ChordGNN + R-GradN | 45.2 ± 0.006 | 46.7 ± 0.005 |
| ChordGNN + NADE | 48.2 ± 0.005 | 49.9 ± 0.005 |

- **[FACT]** §5.1: *"Note that the AugmentedNet model exhibits higher prediction scores on the
  individual Key, Degree, Quality, and Root tasks, which are used jointly for the prediction of the
  Roman numeral. These results indicate that our model obtains more meaningfully interrelated
  predictions, with respect to the Roman numeral prediction, resulting in a higher accuracy score."*
- **[FACT]** §5.1: *"Our model surpasses AugmentedNet with and without post-processing in all fields
  apart from local key prediction and quality. Our model obtains up to 11.6% improvement in
  conventional Roman Numeral prediction."* And: *"In both experiments, post-processing has been
  shown to improve both RN and RN_alt. However, ChordGNN without post-processing already surpasses
  the other models."*
- **[FACT]** §5.2's own reading of Table 2: *"using the dynamically weighted loss yields better
  results compared to other methods such as the Baseline or Gradient Normalization techniques.
  Furthermore, the dynamically weighted loss is comparable to NADE but also more robust on
  Conventional Roman Numeral prediction on our datasets."*
- **[FACT]** §6: *"A configuration study suggests that gradient normalization techniques or
  techniques for carrying prediction information across tasks are not particularly beneficial or
  necessary for such a model."*
- **[FACT]** §5.3: an adapted model *"now with 11+3=14 individual tasks and including the Mozart
  data"* reaches *"a 53.5 CSR score on conventional Roman Numeral"*, and *"post-processing can
  improve the results by up to two additional percentage points"*. **Neither figure appears in any
  table.** Footnote 1: *"Unfortunately, we cannot directly compare these numbers to [21], as their
  results are not reported in comparable terms."*
- **[FACT]** §5.4 and Figure 5, the worked example on Haydn's op. 20 no. 3, movement 4: *"our model
  predicts a harmonic rhythm of eighth notes, which disagrees with the annotator's half-note
  marking"*, and *"The ChordGNN solution accommodates both interpretations as it doesn't attempt to
  group chords at a higher level, treating each eighth note as an individual chord rather than a
  passing event."*
- **[FACT]** §6, future work: pre-training with self-supervised methods; *"we aim to enrich the
  number of tasks for joint prediction by including higher-level analytical targets such as cadence
  detection and phrase boundary detection"*; and extending to audio.

### Derived here, with the sign convention stated, and read as directions only

**No uncertainty is printed on any Table 1 cell, so every difference below is a direction and not a
result** (#24).

- **[DERIVED] The post-processing gain, with-post minus without-post, positive meaning the
  reconciliation is the more accurate:** BPS **RN +2.9** (46.2 → 49.1), BPS **RN_alt +1.8** (48.6 →
  50.4), Full **RN +2.9** (48.9 → 51.8), Full **RN_alt +2.5** (50.4 → 52.9). **It is positive on
  every one of the four, and the same +2.9 on the Roman numeral for both test sets.**
- **[DERIVED] ChordGNN without post-processing minus AugNet, Full block, positive meaning ChordGNN
  higher:** Key −2.0, Degree +3.1, Quality −1.3, Inversion **0.0**, Root +1.8, RN +2.5, **RN_alt
  −1.1**.
- **[DERIVED] ChordGNN+Post minus AugNet, Full block:** Key −1.6, Degree +4.4, Quality −1.3,
  Inversion +1.5, Root +1.9, RN +5.4, RN_alt +1.4.
- **[DERIVED] ChordGNN without post-processing minus AugNet, BPS block:** Key −5.1, Degree −2.3,
  Quality −4.2, Inversion +2.3, Root −2.1, **RN +0.8**, RN_alt −0.7. **This is the pattern §5.1
  describes in words** — AugmentedNet higher on the individual components, ChordGNN higher on the
  Roman numeral built from them.
- **[DERIVED] The "11.6%" is a RELATIVE figure, not percentage points:** Full RN 46.4 → 51.8 is +5.4
  points, and 5.4 / 46.4 = 11.6 %. Recorded so a later citation does not take it for points.
- **[DERIVED] Table 2, variant minus baseline:** WLoss **+2.8** RN, NADE **+2.1** RN, Rotograd −0.6,
  R-GradN −0.9. **Variant minus WLoss:** NADE **−0.7** RN.
- **[DERIVED] RN(Onset) against RN, onset-wise minus duration-weighted, on the four rows carrying
  both:** BPS ChordGNN +0.4, BPS ChordGNN+Post +0.3, Full ChordGNN −0.5, Full ChordGNN+Post −0.6.
  **The two granularities never differ by more than 0.6 on any row that carries both**, and the sign
  is not constant across the two sets.

## Coupling facts (mandatory)

**What the method ASSUMES about its upstream.**
- A **notated symbolic score carrying pitch spelling**, note durations and metrical positions — the
  three node features named at §3.2. Spelling is an input requirement, not something the method
  infers.
- **A note-level graph**, built by the four stated relations from onsets and durations. No fixed
  frame grid anywhere in the input.
- **No voices, no dynamics, no bar lines or beat positions as such** (metrical position is a node
  feature; the paper does not describe it further).
- For TRAINING: the Roman numeral annotations of [7]'s six datasets, on [7]'s own splits, with
  texturization and transposition augmentation confined to the training split.

**What it HANDS downstream.**
- **Per-onset labels for every task** — the text says eleven tasks; the figures label ten: Key,
  Degree, Quality, Inversion, Root, Com RN, Hrhythm, Bass, Ton Key, PC-set — **with no consistency
  enforced between them inside the model.**
- **Two reconstructions of the full Roman numeral**, RN from the five conventional tasks and RN_alt
  from key, inversion and the restricted common-Roman-numeral vocabulary, both taken from [7]. **The
  reconstruction is an assembly of head outputs, not a decision the model takes.**
- **A second, post-hoc pass over all heads** whose output is a fresh set of the same labels.
- **NO segmentation decision of any kind.** There is no boundary variable, no segment and no length
  term. A chord boundary exists only where two adjacent onsets carry different labels; §5.4 states
  the consequence in the authors' own words — the model *"doesn't attempt to group chords at a
  higher level"*.
- **The harmonic-rhythm head IS consumed** — its logits enter the post-processing concatenation.
  **This is the one place this system differs from row 48 on the same head**, where the same task is
  learned and consumed by nothing.
- **No rivals, no confidence, no posterior.** Eleven softmaxes exist and nothing is published from
  any of them, before or after the reconciliation.
- **No figured bass, no cadence, no phrase or section grouping** — the last two named as future
  work.

**Its own STATED SCOPE and limits.**
- **Domain:** Western classical symbolic music, six datasets, Beethoven to Bach with Haydn and
  Mozart added in §5.3's later experiment.
- **Decision scope:** what key, degree, quality, inversion, root, common-Roman-numeral class,
  tonicized key, bass, pitch-class set, and whether a Roman numeral's duration begins — **per
  onset**. **Not** where the harmony changes as a decision; **not** which notes are harmonic.
- **Fitting:** [7]'s splits, reused so that the figures are directly comparable; augmentation
  confined to training. **No validation split, no model-selection procedure and no hyperparameter
  search is described anywhere in the document.**
- **The authors' own bounds:** the model does not group chords at a higher level (§5.4); the §5.3
  figures cannot be compared to [21] (footnote 1); the audio domain is out of scope (§2, §6).

## What an L2 detail specification could adopt, adapt, or must argue against

- **★ MUST ARGUE AGAINST — the multi-head architecture, which is DP-A's rival for the third row of
  group 3 running.** Eleven heads on one shared encoder, decided in one pass with no consistency
  enforced, and the machinery that undoes the separation applied **after training** over the heads'
  logits. The progress record's summaries of the two earlier reads, read whole this session, record
  row 45's system as six such heads and row 48's as eleven with a re-fused *reconstruction*; this
  one has eleven with a re-deciding *pass*, read here at its own object. **What a detail
  specification must meet is that all three undo the separation downstream of the deciding**, which
  is where DP-A's own cut is. Routed to L2's detail specification and to the findings surface's DP-A
  block.
- **★ A MEASURED ARGUMENT FOR DP-A's CHOSEN "NO" THAT THE RECORD DOES NOT CARRY, STATED BY AUTHORS
  INSIDE THE RIVAL LINEAGE.** §5.1's sentence, quoted in full above, plus the BPS block: AugmentedNet
  scores **higher on Key, Degree, Quality and Root** and **lower on the Roman numeral built from
  them**, and the authors read that as their own model obtaining *"more meaningfully interrelated
  predictions"*. **A per-component win that does not become a joint win is DP-A's argument**, and
  here it is measured rather than asserted. Its bound travels with it: the comparison is between two
  different architectures and not an ablation inside one, no uncertainty is printed on any of the
  cells, and the effect on the Roman numeral column of the BPS block is +0.8. Routed to the findings
  surface's DP-A block and to L2's detail specification; **applied nowhere.**
- **★ A PRECISION ON WHAT "UNDOING THE SEPARATION" BUYS, FROM THIS PAPER'S OWN CONFIGURATION
  STUDY.** The paper measures **two different kinds** of cross-head machinery and reports them
  differently. The post-processing — a reconciliation over all heads after training — gains **+2.9**
  Roman numeral points on both test sets. **NADE — the intra-task-dependency mechanism of [8], which
  is the very work V9's parenthesis names** — gains **+2.1** over the baseline but is **−0.7**
  against the dynamically weighted loss, and §6 concludes that *"techniques for carrying prediction
  information across tasks are not particularly beneficial or necessary for such a model."* **The
  conclusion's sentence is stronger than the table read on its own**, NADE beating the baseline; both
  are recorded. **So "machinery to undo the separation" is not one thing**, and a detail
  specification citing DP-A's lineage sentence should say which kind it means. Routed to the
  findings surface's DP-A block.
- **ADAPT — the graph score representation with edge-contraction pooling to the onset level.** This
  is V8's own item and it is L1's territory. **With the precision recorded above: the grid is onsets
  only**, where the L1 charter's partition points are onsets and offsets. Routed to the L1 and L2
  detail specifications.
- **A DATUM ON THE EVALUATION GRID, of a shape the slice has met before.** The model predicts
  onset-wise and the metric is applied on a **fixed 32nd-note grid**, *"in accordance with
  [6,7,9]"*, using **Chord Symbol Recall — a duration-weighted metric**. The paper publishes
  **RN(Onset) beside RN** so the two granularities can be read against each other, and the derived
  differences above are at most 0.6 in either direction. Routed to measurement design beside D-115,
  row 19's mir_eval finding and row 20's WCSR.
- **MUST ARGUE AGAINST — no segmentation decision and no length term at all**, the class rows 45, 47
  and 48 are in. **The sub-shape here is the opposite of row 48's:** the harmonic-rhythm head exists
  AND its logits are consumed by the reconciliation pass, so this system carries a boundary-bearing
  signal into a later stage without ever deciding a boundary. Routed to L2's detail specification.
- **A DP-C DATUM — over-segmentation, worked at the score by the authors.** §5.4's example predicts
  an eighth-note harmonic rhythm against the annotator's half note, and the authors defend it on the
  ground that the model does not group at a higher level. **`reading_pass/l2_slice_reading_progress.md`'s
  summary of the row 45 read records over-segmentation as that paper's authors' most common error
  class** — cited to the progress record, where it was read this session, because **neither row 45's
  extract nor row 45's paper was opened here**. Routed to the findings surface's DP-C block,
  **unmerged with row 18's finding (3)**.
- **A DP-D DATUM.** The Pitch Class Sets task is present, as in row 48, and there is no chord-tone
  assignment: nothing in the model decides which sounding notes belong to the harmony. Routed to the
  findings surface's DP-D block.
- **A DATUM ON WHERE THIS LINEAGE IS GOING, not a finding.** §6 names cadence detection and phrase
  boundary detection as tasks to add — which is the direction candidacy row 52 (AnalysisGNN) takes,
  and which row 52's own reading will meet. Recorded, carried nowhere.

## ★ Findings, routed and not applied

**(1) THE RATIFIED FIGURE IS CONFIRMED AT ITS OWN PRIMARY, WITH THREE PRECISIONS.** Set out in full
at "The verification target (a)". DP-A (lines 679–680), §S4(a) (lines 1564–1565) and V9 (line 110)
all state the pair; Table 1's BPS block carries **46.2** and **49.1** in the RN column at the two
rows V9 names, and §3.3.1 describes a learned pass over all heads. **Nothing is owed to any of the
three as a structural claim, and no STOP of either class fires.** The three precisions: the pass is
applied **after training** and so undoes the separation downstream of the deciding; **V9's
attribution** of the post-processing to Micchi et al. 2021 is not what the paper says; and **Table 1
prints no uncertainty**, so the 2.9-point difference is a single run. Routed to the findings
surface's V9 row and DP-A block; **applied nowhere.**

**(2) V8's ONSET-LEVEL ITEM IS CONFIRMED VERBATIM**, all three quoted fragments, with one precision
for the L1 charter rather than for V8: the representation is **onset-only**, where the charter's
partition-point ground places a partition point at every onset **and offset**. Routed to the L1 and
L2 detail specifications; **applied nowhere.**

**(3) A MILD IDENTITY FINDING, AND A TIER PRECISION.** The bibliography's row names no authors and
its "title" is the **model's name**, which is not a prefix or leading word of the printed title;
row 28's held document is the one this slice has already read whose printed title also differs from
its row's, so **no "first" is asserted**. The printed authors match what `population.md` V8 names.
The arXiv-versus-ISMIR shape produces **no** venue finding, the held deposit printing the ISMIR
camera-ready attribution box. The row's **LINK** tier understates the printed **CC BY 4.0**. Routed
to the bibliography reconciliation, where this slice's earlier identity and tier findings are
already routed.

**(4) ★ THE CARRIED "MICCHI ET AL. 2021" QUESTION IS ANSWERED — THE WORK IS IDENTIFIED, IT IS NOT
HELD, AND ITS IDENTIFICATION NARROWS V9's PARENTHESIS RATHER THAN CONFIRMING IT.** This paper's
reference **[8]** is *G. Micchi, K. Kosta, G. Medeot and P. Chanquion, "A deep learning method for
enforcing coherence in Automatic Chord Recognition," in Proceedings of the International Society
for Music Information Retrieval Conference (ISMIR), 2021.* That is the work `population.md` V9
calls *"Micchi et al. 2021"*, and its title is where the phrase *"coherence"* in that parenthesis
comes from. **Three things follow and no more.** *(i)* `docs/research_papers/BIBLIOGRAPHY.md` does
**not** hold it, and `reading_pass/extracts/` holds **no extract for it** — both checked at their
own listings this session, on the method warning row 48's read paid for. **So nothing is carried out
of it: it is not held and was not read.** *(ii)* **ChordGNN cites it for NADE, not for the
post-processing** — §2's *"intra-dependent layers"* sentence and Table 2's NADE row — and §3.3.1
cites nothing, so the record's attribution of ChordGNN's post-processing to that work is not
supported at this object. *(iii)* This is a **bibliography-reconciliation** datum and a **wording
precision on V9's parenthesis**; **V9's VERIFIED verdict does not move and neither value changes.**
Routed to the bibliography reconciliation and to the findings surface's V9 row; **applied
nowhere.**

**(5) THE PAPER'S OWN SUMMARY SENTENCE IS NOT BORNE OUT BY ITS OWN TABLE ON TWO CELLS.** §5.1 says
the model *"surpasses AugmentedNet with and without post-processing in all fields apart from local
key prediction and quality"*. Derived at Table 1's Full block, sign convention ChordGNN minus
AugNet, positive meaning ChordGNN higher: **without post-processing, RN_alt is −1.1** (50.4 against
51.5) and **Inversion is 0.0** (78.8 against 78.8, a tie rather than a surpassing); RN_alt is not
among the two exceptions the sentence names. **With post-processing the sentence holds on every
field.** Recorded as a **bound on what the sentence can be cited for**, not as a defect in the
measurement: every value it rests on is the paper's own and is printed in its own table. Routed to
the findings surface's DP-A block; **applied nowhere.**

**(6) THE "11.6% IMPROVEMENT" IS RELATIVE.** Derived above: Full RN 46.4 → 51.8 is +5.4 points and
5.4 / 46.4 = 11.6 %. Recorded so a later citation does not take it for percentage points. Routed to
measurement design.

**(7) FIT AND EVALUATION AT THE OBJECT.** [7]'s splits are reused deliberately so the figures are
comparable, and augmentation is confined to the training split — both good practice and both stated.
**So the held-out question is answered by inheritance rather than by this document**, which
describes **no validation split, no model-selection procedure and no hyperparameter search** of its
own; Table 1's figures carry **no uncertainty at all**; and Table 2's five-run spreads are printed
in a unit inconsistent with the values beside them. **What the three read rows of group 3 now give
the slice is three differently reported protocols on one lineage** — row 45's, recorded in the
progress record's summary as reporting every figure on a validation split with no held-out test set;
row 48's, read at that extract this session, which tunes on validation and runs once on a test split;
and this one's, read here at its object, which reuses row 48's splits and describes no procedure of
its own. **The row 45 half is cited to the progress record, that extract not having been opened
here.** Routed to measurement design beside D-097, D-574, principle #20 and principle #24; **applied
nowhere.**

**(8) ★ THE CARRIED QUESTION (g) ANSWERED: THE PAPER DOES NOT PRESENT ITS POST-PROCESSING AS
ANSWERING ROW 45's §5.1 PROPOSAL.** The proposal, **quoted here from
`reading_pass/l2_slice_reading_progress.md`'s carried item (g), which is where it was read this
session** — row 45's own extract and paper were not opened — is *"a combination of learned and/or
deterministic post-processing to enforce the kind of consistency between labels discussed above"*;
this paper
builds a learned post-processing over all heads and **says nothing about that proposal** — §3.3.1
cites nothing, and the paper's Micchi citations are [6] (2020, the CRNN baseline, which is row 45)
and [8] (2021, for NADE). **So §S4(a)'s narrative — that the lineage's later systems answer the
earlier one's stated problem — stays confirmed from ONE END ONLY**, as row 48's read also left it.
**A datum, not a defect.** Routed to the findings surface's DP-A block.

**(9) THE TASK COUNT IS PRINTED THREE WAYS AND EVERY ONE IS RECORDED AS PRINTED.** §2 names **six**
components of a Roman numeral; §3.1 says conventional RN involves *"the 5 tasks"*; §3.3.1 and §5.3
say the model has **eleven** tasks; and Figures 3 and 4 print **ten** labelled heads. **The paper
reconciles none of them and neither does this extract.** *(A reading of the eleven-against-ten
difference is offered above and is labelled as this reader's conjecture, not the paper's
statement.)*

**(10) THIS PAPER MEASURES THREE OTHER SYSTEMS AGAINST ITSELF, AND NONE OF THOSE FIGURES IS THAT
SYSTEM'S OWN.** Table 1's BPS block carries **Micchi (2020) — candidacy row 45**, **AugNet (2021) —
candidacy row 48**, and **CSM-T (2021)**, which is reference [9], *McLeod and Rohrmeier, "A modular
system for the harmonic analysis of musical scores using a large vocabulary," ISMIR 2021*. Recorded
as a successor's report and **not** as those papers' own figures, the treatment row 48's read gave
its own comparator table. **`reading_pass/extracts/` already holds extracts for row 45 and for
McLeod & Rohrmeier 2021** — checked at the directory listing this session — **so nothing here is
called unread.**

**(11) §5.3's 53.5 IS NOT A TABLE 1 FIGURE.** It comes from an adapted model with fourteen tasks and
added Mozart data, is reported in prose only, and the authors state they cannot compare it to [21].
Recorded so a later citation does not take it for a Table 1 cell.

**(12) THE FINDINGS SURFACE'S "ChordGNN 58.5" IS NOT COMPARABLE WITH ANYTHING IN THIS PAPER.**
`cowork_reading_pass_findings_2026_08_31.md` line 187 prints it inside the DP-C block's BACHI item,
where it is **BACHI's relayed report** under a different metric (full-chord macro-accuracy) on a
different corpus. **Not comparable, not merged** — the same treatment row 48's read gave
*"AugmentedNet 57.2"* at the same line.

**(13) NO FALSIFIER of a chosen design point, so NO STOP of the falsifier class; and NO CORRECTED
STRUCTURAL CLAIM on a live recorded ground, so NO STOP of the remedial commission §5 class either.**
Both ratified items resting on this paper are CONFIRMED at the paper's own text.

## Centrality — CENTRAL, and a second independent extraction is OWED

**CENTRAL**, on the ground this slice has used throughout, and here it is doubled: **two ratified
items rest on this paper** — DP-A's and §S4(a)'s **.462→.491 pair**, which is a measured FIGURE and
not only a description, and **V8's onset-level representation** — and this read verifies both at the
paper's own text. A detail specification arguing DP-A's chosen "no" will cite this system's pair,
and findings (1) and (4) change what may be said when it does; an L1 detail specification writing
the partition-point rule will meet finding (2)'s onset-only precision. **A second independent
extraction is OWED.**

**The ground on which NOT CENTRAL could be argued, stated in full so the verdict is challengeable
here.** Both items were already marked VERIFIED at V8 and V9, and this read confirms rather than
corrects them, so no value and no verdict moves. Nothing in the architecture would be adopted: an
eleven-head graph network is DP-A's rival, not a candidate. The paper decides no segmentation, no
chord-tone assignment and no boundary, so it is silent on DP-C's and DP-D's own questions except as
an instance. And the figure the record rests on is a **single run with no uncertainty printed**,
which bounds how much any argument can lean on it. **A reader who weighs those points may grade this
row NOT CENTRAL and drop the second pass; the facts for both readings are above.**

## What this extract does NOT do

It amends nothing. `FRAMEWORK.md` (DP-A, DP-C, DP-D, §S4(a)), `reading_pass/candidacy_upgrades.md`,
`cowork_l2_task_b_slice_derivation_2026_09_05.md`, `reading_pass/population.md`,
`cowork_reading_pass_findings_2026_08_31.md` and `docs/research_papers/BIBLIOGRAPHY.md` all stand
exactly as they stand. **Row 18's finding (3), row 47's two corrected structural claims and row 45's
finding (1) are not applied, not restated as settled and not built on** by anything here; where this
paper's text bears on the same passages, it is recorded **beside** them. Row 48's finding (2) is
treated the same way.

**Not read, and nothing carried out of any of it:** the paper's released source code
(`https://github.com/manoskary/chordgnn`); its six corpora (ABC, BPS, HaydnSun, TAVERN, WiR, WTC)
and the Annotated Mozart Sonatas added in §5.3; and every work it cites — among them **Micchi,
Kosta, Medeot & Chanquion 2021 (reference [8]), which finding (4) identifies and which is not
held** — together with Pauwels et al. 2019, Temperley 2004, Raphael & Stoddard 2004, Magalhaes & de
Haas 2011, Chen & Su 2018, Micchi et al. 2020, Nápoles López et al. 2021, McLeod & Rohrmeier 2021,
Jeong et al. 2019, Karystinaios & Widmer 2022, Karystinaios, Foscarin & Widmer 2023,
Hernandez-Olivan et al. 2023, Zhang et al. 2014, Guo et al. 2018, Chen et al. 2018, Javaloy & Valera
2022, Navon et al. 2022, Hamilton et al. 2017, Liebel & Körner 2018, Nápoles López 2022 and 2017,
Neuwirth et al. 2018, Devaney et al. 2015, Gotham et al. 2019, Gotham & Jonas 2021, Nápoles López &
Fujinaga 2020, Hentschel et al. 2021 and Harte 2010 — **were not fetched and are not read; only the
held file was.** The ISMIR 2023 proceedings deposit of this paper was not fetched; the held arXiv
v2 PDF is what was read.

---

*Provenance: Cowork, 2026-09-06, the fourteenth reading session of L2's slice, after the ordinary
session-start read (`CLAUDE.md` whole, loaded by the harness; `DECISIONS.md` whole; `STATUS.md`
whole; the derived gating answer at `tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer`, its three counts and its `gating_ids` list whole), the
hundred-and-twenty-ninth handoff entry whole, the hundred-and-eighteenth entry whole for its
bridge-fault section, `reading_pass/l2_slice_reading_progress.md` whole,
`reading_pass/candidacy_upgrades.md` whole, both commissions whole,
`cowork_l2_task_b_slice_derivation_2026_09_05.md` whole, `docs/research_papers/BIBLIOGRAPHY.md`
whole, the row 48 extract at its heading list, banner, verification target, identity, coupling
facts, adopt-or-argue, first finding, centrality and closing sections for the form, `FRAMEWORK.md`
at the design-point opening with DP-A to DP-L (660–769) and at §S4's L0 bullets with §S4(a), (b) and
(c) whole and §S4(d) as far as line 1597, `reading_pass/population.md` at its verification rows V1 to
V13, and `cowork_reading_pass_findings_2026_08_31.md` at the two passages that name DP-A's ground
(118–134) and at the BACHI item that names DP-C (178–201) — **the section names taken from those
passages' own text and not from a heading list, which was not read at that file**. The `reading_pass/extracts/` and
`docs/research_papers/` directory listings were both read, the first on the method warning row 48's
read paid for. The tip was re-read at both ref files with the file tools and stands at
`911f5f7cdaa3fb53b9b5a2bdefb82e793c65eafb`. Every file was read with the file tools from
bridge-staged copies; no shell read repository content or any staged copy of it. No figure of this
project's own measurement is restated (#17f, D-431); every value above is this paper's own or is
derived here from this paper's own table with the sign convention stated.*
