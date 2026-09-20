# EXTRACT — Karystinaios & Widmer 2022, "Cadence Detection in Symbolic Classical Music using Graph Neural Networks" — Task B candidacy row 38, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** All eight pages read AT THE OBJECT as page images through the bridge. **No relay, no
> web-fetch read.**
>
> **Why this paper.** Row 38 of `reading_pass/candidacy_upgrades.md`, ADMITTED as *"the second half of
> V6, and a different method for the same L1/L3 split."* Fourth member of the L1 slice **Ruling 10**
> made the phase's first reading. It is read immediately after row 37 because it is that paper's direct
> comparator and reports row 37's own numbers beside its own.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**
>
> **★ CORRECTED 2026-09-20 UNDER THE STANDING RULE OF HANDOFF ENTRY 198 §7.** The second independent
> extraction (`reading_pass/extracts_second_pass/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md`,
> its §9.3, items (a) to (k)) found departures from the page that move no value, numbered finding or
> verdict. Each is corrected at its site, with a note carrying its former wording (#12). **Three places inside or
> beside a finding or verdict (that file's §9.4: finding (2) and the words beside it, the "Adopt"
> verdict, the "Adapt" verdict) are NOT corrected here; they stand with the user.** No digit, finding or
> verdict was changed. *(★ The sentence on the three places is made stale by the paragraph below and is
> left standing, #12.)*
>
> **★ AND CORRECTED 2026-09-20 ON THE USER'S RULING, his words: "I agree with 1 for all three."** — the three places of that file's §9.4 are corrected at their
> sites, each with a note carrying its former wording (#12): (A) the heading before the Table 3
> paragraph, finding (2) and finding (4) now say the method differs from [4]'s and the Haydn corpus and
> its annotations are shared, in the page's words; (B) the "Adopt" verdict is bounded to Tables 2 and 4
> and states Table 3's contrary cells; (C) the "Adapt" verdict rests on Table 4 at its scope, and
> finding (3) carries a note on the same ground. **No digit changed. The findings and verdicts keep
> their direction; what changed is the ground and the scope they state.** The paper was not re-opened
> for the act; the ground is the second extract's §9.4 and §5.

## Identity

Emmanouil Karystinaios & Gerhard Widmer, "Cadence Detection in Symbolic Classical Music using Graph
Neural Networks", *Proceedings of the 23rd International Society for Music Information Retrieval
Conference (ISMIR 2022)*, Bengaluru. arXiv:2208.14819v1, 31 Aug 2022. Institute of Computational
Perception, Johannes Kepler University Linz; LIT AI Lab. CC BY 4.0.

**File:** `docs/research_papers/karystinaios_widmer_2022_arxiv_cadence_detection_gnn.pdf`.

## Claims, labeled

### What the method is

**[FACT, §1, §3]** Cadence detection is posed as **imbalanced node classification on a graph**. The
score becomes a *homogeneous* graph: every note **and every rest** is a node; three kinds of undirected
edge join them — `E_on` between notes sharing an onset, `E_cons` between consecutive notes, and `E_dur`
between a longer note and notes whose onsets fall during it.

**[FACT, §3.1]** **135 features per node**, in three categories: general note-wise features (onset in
score-relative beats, duration in beats, MIDI pitch, plus **global attributes such as time signature and
key signature assigned to each note** (the key signature: Figure 1's caption, p. 2), and interval vectors
with binary chord-type indicators);
graph-aware features (the first 20 eigenvectors of the Laplacian of the adjacency matrix); and
cadence-related note features *"similar to those in [4]"* — that is, row 37's.
*(★ CORRECTED 2026-09-20 — a locator added: §3.1's text names the time signature; the key signature is
in Figure 1's caption. Former wording, preserved (#12): "…such as time signature and key signature
assigned to each note**, and interval vectors…" with no locator.)*

**★ [FACT, §3.1] The deliberate weakening of row 37's frame, and its stated purpose.** *"in contrast to
[4], we restrict these to only consider the immediate local context of a note instead of using positional
features relating to predefined past 'cadence anchor points'. In this way, we wish to demonstrate the
generality of our representation and learning approach, which will hopefully learn more long-distance
aspects automatically."* And: *"we do not use any information about events that occur on previous beats
… While these features are more restricted compared to [4] they are also more general, since we make no
assumptions on and reference to 'cadence anchor points' (e.g., the occurrence of the preceding subdominant
and dominant harmony), which in [4] are identified with specialized heuristics."*
*(★ CORRECTED 2026-09-20 — the page prints "no assumptions on and reference to" (p. 3). Former wording,
preserved (#12): "no assumptions and reference to".)*

**[FACT, §5]** The model is **Stochastic GraphSMOTE**: a GraphSAGE encoder, a SMOTE layer applied in the
encoder's *latent* space to force a 1:1 class balance per batch, a decoder generating edges for the
synthetic nodes, and a GraphSAGE classifier over the generated adjacency. The total loss is cross-entropy
plus a weighted edge-reconstruction loss.

**★ [FACT, §1, §6.1] Prediction granularity is a property of the representation, not of the task.** *"our
model can provide predictions at three different levels, note-wise, onset-wise and beat-wise predictions
(the latter two simply by aggregation)"*, whereas *"The reference model [4] can only classify at the beat
level."*
*(★ CORRECTED 2026-09-20 — the page prints "three different levels, note-wise, onset-wise and beat-wise
predictions" (p. 4, §6.1). Former wording, preserved (#12): "three different scales, note-wise,
onset-wise and beat-wise (the latter".)*

## Measured results, as the paper states them

**Corpora (Table 1).** Bach Fugues — 24 pieces, 24,567 nodes, 229,107 edges, PAC 237, rIAC 78, HC 15.
Haydn String Quartets — 45 pieces, 38,661 nodes, 441,491 edges, PAC 434, rIAC 24, HC 340. Mozart String
Quartets — 31 pieces, 68,190 nodes, 762,796 edges, PAC 1,089, HC 1,930. *"Cadence nodes constitute less
than 2% of all nodes."* Scores from kern.ccarh.org, parsed with partitura.

**Table 2 — half for training, half for testing; F₁ for the positive (cadence) class:**

| Dataset | Model | F₁ Note | F₁ Onset | F₁ Beat | Prec. Beat | Recall Beat |
|---|---|---|---|---|---|---|
| Bach Fugues (PAC) | Bigo et al. | – | – | **0.80** | **0.89** | 0.72 |
| | Stochastic GraphSMOTE | 0.85 | 0.75 | 0.73 | 0.70 | 0.77 |
| | Pretrained SGSMOTE | **0.90** | **0.83** | **0.80** | 0.74 | **0.89** |
| Bach Fugues (rIAC) | Bigo et al. | – | – | 0.68 | 0.71 | 0.65 |
| | Stochastic GraphSMOTE | **0.87** | **0.75** | **0.73** | **0.75** | 0.72 |
| | Pretrained SGSMOTE | 0.87 | 0.73 | 0.71 | 0.62 | **0.82** |
| Haydn String Quartets (PAC) | Bigo et al. | – | – | **0.69** | **0.60** | **0.82** |
| | Stochastic GraphSMOTE | 0.77 | 0.56 | 0.59 | 0.47 | 0.78 |
| | Pretrained SGSMOTE | **0.81** | **0.63** | 0.64 | 0.54 | 0.78 |
| Haydn String Quartets (HC) | Bigo et al. | – | – | 0.29 | 0.19 | **0.56** |
| | Stochastic GraphSMOTE | 0.65 | 0.32 | 0.30 | 0.33 | 0.27 |
| | Pretrained SGSMOTE | **0.69** | **0.44** | **0.41** | **0.41** | 0.41 |

*(★ CORRECTED 2026-09-20 — four bold marks, as read twice at page 5 at the size the file tool delivers:
the reference model's Bach PAC precision 0.89, the pretrained model's Bach PAC beat F1 0.80 and the
reference model's Haydn PAC precision 0.60 are bold on the page; the reference model's Haydn HC beat F1
0.29 is plain. Former marking, preserved (#12): 0.89, 0.80 (pretrained) and 0.60 plain; 0.29 bold. No
digit changed.)*

**★ [FACT, §6.1] The authors' own summary of that table.** *"Our model matches or slightly surpasses the
state of the art in rIAC detection in Bach fugues and on HCs in Haydn string quartets but does not reach
the reference model's F1 results in PAC detection."* *(★ CORRECTED 2026-09-20 — the page prints "in Bach
fugues" (p. 5). Former wording, preserved (#12): "on Bach fugues".)* Pre-training on the other dataset *"is the price we
pay for the generality of the graph representation and the consequent size (number of parameters) of the
deep network."* And the comparison of error shapes: *"In the PAC detection tasks, in particular, we
observe comparable or higher recall of our model compared to the reference, but lower precision."*

**★ [FACT, §6.1] The agreement with [4] — a different method on shared data.** *"Generally, our results
agree with [4] in implying that half cadences (HC) seem significantly harder to identify than authentic
cadences, both perfect and imperfect."* The paper uses *"two datasets also used by Bigo et al. [4]"*
(p. 3) and *"the same data and train/test setup"* (p. 4).
*(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): "★ [FACT, §6.1] The
independent replication." — the page describes a different method on the same datasets, not an
independent replication.)*

**Table 3 — three-class classification (no cadence / PAC / rIAC or HC), 5-fold cross-validation, macro-averaged F₁**, comparing all features against *general* (excluding the cadence-specific engineered
category): Bach Fugues general 0.602 note / 0.667 beat against all 0.653 / 0.702; Haydn general 0.542 /
0.610 against all 0.648 / 0.663; Mozart general 0.584 / 0.569 against all 0.588 / 0.606. The authors'
reading: the engineered features help, *"However, also the general-purpose category 1 and 2 features
alone support non-trivial cadence recognition and discrimination performance, which implies that the
relational graph representation in combination with a convolutional approach manages to enrich highly
local features with relevant non-local score context."*

**Table 4 — neighbour-convolution depth on Bach PAC** (F₁ note / onset / beat): none 0.833 / 0.671 /
0.667; 1-hop 0.854 / 0.707 / 0.701; **2-hop 0.869 / 0.737 / 0.732**; 3-hop 0.836 / 0.706 / 0.659. *"Best
results are achieved when using a convolution depth of 2. Increasing the receptive field beyond that
level, we observed some instabilities emerging in the learning model, …"* — the page continues *"which
could be attributed to the common vanishing gradient problem in deep GCNs [22]"* (p. 6).
*(★ CORRECTED 2026-09-20 — the quotation had closed with a full stop mid-sentence. Former wording,
preserved (#12): "…emerging in the learning model."*".)*

**[FACT, §6.2] The false positives are diagnosed, not just counted.** *"many false positive predictions
resemble cadences, in terms of tonal structure or implications, and could be considered and annotated as
such, but lack some main components."* One of the three worked cases is Haydn Op. 54 No. 1 II, mm. 33–45 (the
others: fugue no. 19 of WTC I at bar 23, and the passage of [4]'s Figure 4), where a
modulating melodic and harmonic sequence ends each statement with a cadential pattern: *"A harmonic
analysis of these bars indicates a proper PAC preparation with text-book voice leading on the cadence
arrival point in every occasion. These two false positive PACs form part of a modulating melodic and
harmonic sequence; whether to classify them as cadences is a matter of higher-level musicological
considerations."* And the stated boundary of the method: *"by design cannot consider high-level
musical considerations such as, e.g., whether PAC-like patterns that occur in sequence should count as
PACs or not."*
*(★ CORRECTED 2026-09-20 — two places in this paragraph. §6.2 works three examples, not one; and the
page prints "high-level musical considerations" (p. 6). Former wording, preserved (#12): "The worked case
is Haydn Op. 54 No. 1 II, mm. 33–45, where a" and "cannot consider higher-level musical
considerations".)*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A parsed symbolic score giving, per note and per rest, onset in
score-relative beats, duration in beats and MIDI pitch, **plus the time signature and the key signature
as global attributes attached to every node**. Notes and rests both. No chord segmentation, harmonic
analysis or decided tonality is described in the pages as read — **but the key signature is used as a
feature**, which the L0 contract also gives, as a weak prior and never as a fact about the tonality.
*(★ CORRECTED 2026-09-20 — a negative given its bound: the page describes none of those steps, and does
not say it lacks them. Former wording, preserved (#12): "No chord segmentation, no harmonic analysis, no
decided tonality —".)*

**What it HANDS downstream.** A cadence label per **note**, and by aggregation per onset and per beat —
binary in the first experiment, three-class in the second. No chord, key or segmentation is described as
an output; the classifier's softmax values, which the page calls *"the predicted class probabilities"*
(p. 4), are not said to be published. *(★ CORRECTED 2026-09-20 — a negative given its bound. Former
wording, preserved (#12): "Nothing else: no chord, no key, no segmentation.")*

**Its own STATED SCOPE and limits.** Baroque and Classical cadences, three corpora, focused on PAC with
rIAC and HC *"where our annotated datasets permit"*. The Bach HC count is 15 and the Haydn rIAC count 24,
and the paper says in a footnote that it ignores *"the HC in Bach and rIAC in Haydn, because of their low
numbers."* The best beat-wise figures in three of Table 2's four blocks are the model's pre-trained on the
other dataset; in the Bach rIAC block they are the model's without pre-training. Convolution beyond 2-hop
destabilises. By design the method *"cannot consider high-level musical considerations such as, e.g.,
whether PAC-like patterns that occur in sequence should count as PACs or not"* (p. 6).
*(★ CORRECTED 2026-09-20 — two places: a claim wider than Table 2, and an unprinted gloss in the stated
scope. Former wording, preserved (#12): "Pre-training on a second dataset is required for the best
figures." and "The method cannot reach form-level judgements, by design.")*

## What an L1 detail specification could adopt, adapt, or must argue against

- **Adopt as evidence, not as machinery — the granularity result.** A cadence cue can be carried at the
  **note** level and aggregated upward. In Tables 2 and 4 the note-level figure is the highest of the
  three in every row that reports it; **Table 3 prints the note-level macro F1 below the beat-level one
  in five of its six cells** (p. 6). Our L1 publishes cues per change point; on Tables 2 and 4 this is
  measured support that the finer grain is not a loss.
  *(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): "and the note-level
  figures are consistently the highest of the three. Our L1 publishes cues per change point; this is
  measured support that the finer grain is not a loss.")*
- **Adapt — the finding that local features plus non-local structure beat local features alone.** The
  paper's measurement of the graph's contribution is Table 4 — PAC in the Bach fugues only, one value per
  depth, no spread printed: depth 2 gives the highest figure at all three levels, and no convolution
  the lowest at note and onset level (p. 6). Table 3 does not measure it: both of its arms carry the
  graph convolution and neither carries [4]'s anchor heuristics; that the general features' performance
  *"implies"* graph-supplied context is the authors' reading (p. 6).
  *(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): "The general-feature
  arm of Table 3 shows a graph's neighbourhood supplies context that hand-designed anchor heuristics
  were previously carrying.")* **For L1 this is a caution rather than a design**: L1 decides
  nothing, so it may publish cues but must not acquire a learned context stage of its own — that context
  belongs to L2, which sees the whole span.
- **Must argue against — nothing here.** Like row 37, this is a primary under a chosen point, not a rival
  to one.

## ★ Findings, routed and not applied

**(1) ★ THE FRAMEWORK'S ".29 AND .41" PAIR IS VERIFIED, AND BOTH VALUES SIT IN THIS ONE TABLE.** The L1
charter carries: *"the half cadence reaches F .29 and .41 in those same two studies."* Table 2 of this
paper reports **0.29** for the Bigo et al. reference model on Haydn HC — the same value row 37's own
Table 3 reports — and **0.41** for this paper's own pretrained model on the same target. **Both halves of
the charter's figure verify at the object, and the two studies are now both read whole. No correction is
owed.**

**(2) The agreement the charter's DP-I rests on is real, and it is two methods on shared data.** *"our
results agree with [4] in implying that half cadences (HC) seem significantly harder to identify than
authentic cadences"* — a different method, on *"two datasets also used by Bigo et al. [4]"* (p. 3) with
*"the same data and train/test setup"* (p. 4); the Haydn half-cadence comparison is on the Haydn corpus
annotated by *"Sears and colleagues [19]"* (p. 3), and [4]'s figures are *"taken from [4]"* (p. 5).
**DP-I's split — cues at L1, type at L3 — is supported by two primaries rather than one, and both are
now at the object; their methods differ, their Haydn corpus and its annotations are shared.**
*(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): the heading "The
independent replication the charter's DP-I rests on is real and is stated as such."; the quotation
without "(HC)"; "— an independent method, a different corpus, the same conclusion."; and the closing
sentence without its last clause.)*

**(3) ★ A finding that sharpens what the charter means by a cue, and that the derivation should carry.**
This paper deliberately **removed** row 37's anchor-point heuristics and still reached comparable results
by letting a graph supply the surrounding context. Read together, the two papers say the cue is carried
by **local musical evidence plus some view of its surroundings**, and that the surroundings can be
supplied either by hand-named anchors or learned. **For L1 that is a boundary statement, not a licence:**
the charter has L1 publish evidence at change points and decide nothing, so the surrounding-context half
belongs to the layer that sees the span. **Routed to the L1 and L2 detail specifications; nothing is
amended.**
*(★ NOTE 2026-09-20 ON THE USER'S RULING: "comparable" is the paper's own word, and "by letting a graph
supply the surrounding context" is the paper's own attribution — its "implies", read off Table 3
(p. 6). The page's measurement of the graph's contribution is Table 4, at the scope the "Adapt"
verdict above states. The finding's text is otherwise unchanged.)*

**(4) A ceiling caution, agreeing with row 37's from the other side.** Row 37 records that at least five
of its Haydn PAC false positives *"can be seen as actual cadences"*. This paper's §6.2 says the same in
its own words and works an example: cadential patterns inside a modulating sequence, textbook-correct at
the arrival, counted as false positives because whether they are cadences *"is a matter of higher-level
musicological considerations."* **Two studies — different methods, the same Haydn annotations by
Sears and colleagues [19] (p. 3) — report that the annotation, not only the method, bounds the
measured figure.** *(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): "Two
independent studies report that the annotation, not only the method, bounds the measured figure.")*
Principle #21's shape on the cadence axis. **Routed to measurement design.**

**(5) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL** — the second primary under V6 and under DP-I's recorded ground. **A second independent
extraction is owed** and has not been performed.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. The paper was read
at the object as page images, all eight pages. No shell command was run on the repository or on any
staged copy of it for content or for listings; the container copy used for writing this file is declared.
Every value above is the paper's own (#17f, D-431).*
