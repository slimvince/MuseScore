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
key signature assigned to each note**, and interval vectors with binary chord-type indicators);
graph-aware features (the first 20 eigenvectors of the Laplacian of the adjacency matrix); and
cadence-related note features *"similar to those in [4]"* — that is, row 37's.

**★ [FACT, §3.1] The deliberate weakening of row 37's frame, and its stated purpose.** *"in contrast to
[4], we restrict these to only consider the immediate local context of a note instead of using positional
features relating to predefined past 'cadence anchor points'. In this way, we wish to demonstrate the
generality of our representation and learning approach, which will hopefully learn more long-distance
aspects automatically."* And: *"we do not use any information about events that occur on previous beats
… While these features are more restricted compared to [4] they are also more general, since we make no
assumptions and reference to 'cadence anchor points' (e.g., the occurrence of the preceding subdominant
and dominant harmony), which in [4] are identified with specialized heuristics."*

**[FACT, §5]** The model is **Stochastic GraphSMOTE**: a GraphSAGE encoder, a SMOTE layer applied in the
encoder's *latent* space to force a 1:1 class balance per batch, a decoder generating edges for the
synthetic nodes, and a GraphSAGE classifier over the generated adjacency. The total loss is cross-entropy
plus a weighted edge-reconstruction loss.

**★ [FACT, §1, §6.1] Prediction granularity is a property of the representation, not of the task.** *"our
model can provide predictions at three different scales, note-wise, onset-wise and beat-wise (the latter
two simply by aggregation)"*, whereas *"The reference model [4] can only classify at the beat level."*

## Measured results, as the paper states them

**Corpora (Table 1).** Bach Fugues — 24 pieces, 24,567 nodes, 229,107 edges, PAC 237, rIAC 78, HC 15.
Haydn String Quartets — 45 pieces, 38,661 nodes, 441,491 edges, PAC 434, rIAC 24, HC 340. Mozart String
Quartets — 31 pieces, 68,190 nodes, 762,796 edges, PAC 1,089, HC 1,930. *"Cadence nodes constitute less
than 2% of all nodes."* Scores from kern.ccarh.org, parsed with partitura.

**Table 2 — half for training, half for testing; F₁ for the positive (cadence) class:**

| Dataset | Model | F₁ Note | F₁ Onset | F₁ Beat | Prec. Beat | Recall Beat |
|---|---|---|---|---|---|---|
| Bach Fugues (PAC) | Bigo et al. | – | – | **0.80** | 0.89 | 0.72 |
| | Stochastic GraphSMOTE | 0.85 | 0.75 | 0.73 | 0.70 | 0.77 |
| | Pretrained SGSMOTE | **0.90** | **0.83** | 0.80 | 0.74 | **0.89** |
| Bach Fugues (rIAC) | Bigo et al. | – | – | 0.68 | 0.71 | 0.65 |
| | Stochastic GraphSMOTE | **0.87** | **0.75** | **0.73** | **0.75** | 0.72 |
| | Pretrained SGSMOTE | 0.87 | 0.73 | 0.71 | 0.62 | **0.82** |
| Haydn String Quartets (PAC) | Bigo et al. | – | – | **0.69** | 0.60 | **0.82** |
| | Stochastic GraphSMOTE | 0.77 | 0.56 | 0.59 | 0.47 | 0.78 |
| | Pretrained SGSMOTE | **0.81** | **0.63** | 0.64 | 0.54 | 0.78 |
| Haydn String Quartets (HC) | Bigo et al. | – | – | **0.29** | 0.19 | **0.56** |
| | Stochastic GraphSMOTE | 0.65 | 0.32 | 0.30 | 0.33 | 0.27 |
| | Pretrained SGSMOTE | **0.69** | **0.44** | **0.41** | **0.41** | 0.41 |

**★ [FACT, §6.1] The authors' own summary of that table.** *"Our model matches or slightly surpasses the
state of the art in rIAC detection on Bach fugues and on HCs in Haydn string quartets but does not reach
the reference model's F1 results in PAC detection."* Pre-training on the other dataset *"is the price we
pay for the generality of the graph representation and the consequent size (number of parameters) of the
deep network."* And the comparison of error shapes: *"In the PAC detection tasks, in particular, we
observe comparable or higher recall of our model compared to the reference, but lower precision."*

**★ [FACT, §6.1] The independent replication.** *"Generally, our results agree with [4] in implying that
half cadences (HC) seem significantly harder to identify than authentic cadences, both perfect and
imperfect."*

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
level, we observed some instabilities emerging in the learning model."*

**[FACT, §6.2] The false positives are diagnosed, not just counted.** *"many false positive predictions
resemble cadences, in terms of tonal structure or implications, and could be considered and annotated as
such, but lack some main components."* The worked case is Haydn Op. 54 No. 1 II, mm. 33–45, where a
modulating melodic and harmonic sequence ends each statement with a cadential pattern: *"A harmonic
analysis of these bars indicates a proper PAC preparation with text-book voice leading on the cadence
arrival point in every occasion. These two false positive PACs form part of a modulating melodic and
harmonic sequence; whether to classify them as cadences is a matter of higher-level musicological
considerations."* And the stated boundary of the method: *"by design cannot consider higher-level
musical considerations such as, e.g., whether PAC-like patterns that occur in sequence should count as
PACs or not."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A parsed symbolic score giving, per note and per rest, onset in
score-relative beats, duration in beats and MIDI pitch, **plus the time signature and the key signature
as global attributes attached to every node**. Notes and rests both. No chord segmentation, no harmonic
analysis, no decided tonality — **but the key signature is used as a feature**, which the L0 contract
also gives, as a weak prior and never as a fact about the tonality.

**What it HANDS downstream.** A cadence label per **note**, and by aggregation per onset and per beat —
binary in the first experiment, three-class in the second. Nothing else: no chord, no key, no
segmentation.

**Its own STATED SCOPE and limits.** Baroque and Classical cadences, three corpora, focused on PAC with
rIAC and HC *"where our annotated datasets permit"*. The Bach HC count is 15 and the Haydn rIAC count 24,
and the paper says in a footnote that it ignores *"the HC in Bach and rIAC in Haydn, because of their low
numbers."* Pre-training on a second dataset is required for the best figures. Convolution beyond 2-hop
destabilises. The method cannot reach form-level judgements, by design.

## What an L1 detail specification could adopt, adapt, or must argue against

- **Adopt as evidence, not as machinery — the granularity result.** A cadence cue can be carried at the
  **note** level and aggregated upward, and the note-level figures are consistently the highest of the
  three. Our L1 publishes cues per change point; this is measured support that the finer grain is not a
  loss.
- **Adapt — the finding that local features plus non-local structure beat local features alone.** The
  general-feature arm of Table 3 shows a graph's neighbourhood supplies context that hand-designed anchor
  heuristics were previously carrying. **For L1 this is a caution rather than a design**: L1 decides
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

**(2) The independent replication the charter's DP-I rests on is real and is stated as such.** *"our
results agree with [4] in implying that half cadences seem significantly harder to identify than
authentic cadences"* — an independent method, a different corpus, the same conclusion. **DP-I's split —
cues at L1, type at L3 — is supported by two primaries rather than one, and both are now at the object.**

**(3) ★ A finding that sharpens what the charter means by a cue, and that the derivation should carry.**
This paper deliberately **removed** row 37's anchor-point heuristics and still reached comparable results
by letting a graph supply the surrounding context. Read together, the two papers say the cue is carried
by **local musical evidence plus some view of its surroundings**, and that the surroundings can be
supplied either by hand-named anchors or learned. **For L1 that is a boundary statement, not a licence:**
the charter has L1 publish evidence at change points and decide nothing, so the surrounding-context half
belongs to the layer that sees the span. **Routed to the L1 and L2 detail specifications; nothing is
amended.**

**(4) A ceiling caution, agreeing with row 37's from the other side.** Row 37 records that at least five
of its Haydn PAC false positives *"can be seen as actual cadences"*. This paper's §6.2 says the same in
its own words and works an example: cadential patterns inside a modulating sequence, textbook-correct at
the arrival, counted as false positives because whether they are cadences *"is a matter of higher-level
musicological considerations."* **Two independent studies report that the annotation, not only the
method, bounds the measured figure.** Principle #21's shape on the cadence axis. **Routed to measurement
design.**

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
