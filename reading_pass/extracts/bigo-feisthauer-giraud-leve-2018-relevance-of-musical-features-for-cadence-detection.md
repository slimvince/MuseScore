# EXTRACT — Bigo, Feisthauer, Giraud & Levé 2018, "Relevance of Musical Features for Cadence Detection" — Task B candidacy row 37, first pass, AT THE OBJECT

> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under
> `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **The grade.** All seven printed pages (pp. 355–361) read AT THE OBJECT as page images through the
> bridge. **No relay, no web-fetch read.** Every quotation carries its printed page or section.
>
> **Why this paper.** Row 37 of `reading_pass/candidacy_upgrades.md`, ADMITTED because it is *"V6's
> primary, and the method behind DP-I's split: which cues are computable before the harmony is the L1
> charter's own content."* Third member of the L1 slice **Ruling 10** made the phase's first reading.
>
> **This extract derives no specification statement, amends no document, opens no code and writes no
> open-items row or decisions-register entry.**

## Identity

Louis Bigo, Laurent Feisthauer, Mathieu Giraud & Florence Levé, "Relevance of Musical Features for
Cadence Detection", *Proceedings of the 19th International Society for Music Information Retrieval
Conference (ISMIR 2018)*, Paris, pp. 355–361. CRIStAL UMR 9189, CNRS, Université de Lille; MIS,
Université de Picardie Jules Verne. CC BY 4.0.

**File:** `docs/research_papers/bigo_feisthauer_giraud_leve_2018_ismir_cadence_detection_features.pdf`.

## Claims, labeled

### ★ The two exclusions that make this L1's paper

**[FACT, §1.3]** *"The proposed strategy avoids chord segmentation, which is itself a difficult MIR
problem."* And **[FACT, §2]**: *"We therefore do not start from a complete harmony analysis nor a chord
segmentation, that can be error-prone. Even when the methods finding Y(Z) and X(Z) return approximate
onsets, the computed features may be relevant."*

**★ [FACT, §2.1]** *"we do not perform tonality estimation … because of the usual difficulty of
algorithms to disambiguate adjacent tonalities in the circle of fifths."* **The features reach for
tonality only as a hypothesis anchored on the bass of the arrival chord, never as a decided key.**

### What the method is

**[FACT, abstract, §2]** **44 binary, musical, local cadential features**, computed at **each beat** of
the score, turning cadence detection into a per-beat classification task. Features describe three
onsets: **Z**, the candidate arrival beat; **Y**, the chord preceding it; and **X**, the cadence
preparation.

**[FACT, §2.3]** Y is found heuristically: *"the latest beat preceding Z for which the bass voice
includes a sounding note, limited to one measure in the past."* Beat resolution for the search depends
on the corpus — quarter note for Haydn, eighth for Bach, *"to cope with the faster harmonic rhythm"*
(Figure 3).

**[FACT, §2.4]** X is *"the latest beat before Y whose lowest sounding note has a different pitch
(modulo octave) than the lowest note of Y."*

**★ [FACT, §2.1] The feature that IS the L1 charter's third cue.** *"Z-bass-compatible-with-I (resp.
Z-bass-compatible-with-V): Both notes 4 and 7 of the tonality that would be implied by the bass of Z are
present in the four beats before Z."* A companion feature, `Z-bass-compatible-with-I-scale`, asks whether
*"The 8 previous beats exhibits the whole scale of the same implied tonality."*

**[FACT, §2.1–2.4]** The other feature families, in the paper's own groupings: chord constitution at Z
(perfect triad, sus4, highest note is the tonic or the third); **voice-leading** features
`Z-β-comes-from-α` and `Z-α-moves-to-β` (an immediate resolution of one degree to another); **rhythmic
and break** features `R-Z-strong-beat`, `R-Z-same-rhythm`, `R-Z-sustained-note`, `R-after-Z-rest-*`;
features on Y (`Y-has-7`, `Y-in-V7`, `Y-Z-bass-moves-compatible-V-I`, `Y-Z-bass-same-voice`); and on X
(`X-Y-bass-moves-2nd-min`, `-2nd-Maj`, `-4th`).

**[FACT, §3]** A linear **SVM**, with **leave-one-piece-out** cross-validation for hyper-parameters —
chosen deliberately: *"the traditional Leave-One-Out (LOO) cross-validation approach that would consist
in leaving only one beat of one piece out of the training set would result here in overfitting due to
intra-piece musical repetitions."* Classes are unbalanced (about 98% non-cadential), so cadential beats
are weighted more heavily. *k*-nearest-neighbour and decision trees *"turned out to provide comparable
or inferior results."*

## Measured results, as the paper states them

**Corpora (Table 1).** `bach-wtc-i`: 24 fugues of the Well-Tempered Clavier book I, 2 to 5 voices, 4739
beats, PAC 63 (23 final), rIAC 24, HC (5). `haydn-quartets`: 42 expositions from Haydn string quartet
movements in sonata form, 4 voices, 7173 beats, PAC 99 (21), rIAC (8), HC 70. *"Cadences are labeled at
about 2% of the beats."* Bach annotations from the authors' own earlier fugue work; Haydn annotations
from Sears and colleagues.

**Table 3 — detection on the test sets, all features:**

| Corpus | Target | beats | ref | TP | FP | FN | F₁ |
|---|---|---|---|---|---|---|---|
| haydn-quartets (21 quatuors) | PAC | 3583 | 51 | 42 | 28 | 9 | **0.69** |
| haydn-quartets | HC | 3583 | 32 | 18 | 73 | 14 | **0.29** |
| bach-wtc-i (12 fugues) | PAC | 2357 | 36 | 26 | 3 | 10 | **0.80** |
| bach-wtc-i | PAC+rIAC | 2357 | 46 | 30 | 12 | 16 | **0.68** |

**Table 4 — F₁ by feature subset** (haydn PAC / haydn HC / bach PAC / bach PAC+rIAC): all features XYZR
0.69 / 0.29 / 0.80 / 0.68; YZR 0.69 / 0.27 / 0.71 / 0.68; ZR 0.59 / 0.24 / 0.52 / 0.34; XYZ 0.72 / 0.25
/ 0.74 / 0.54.

**[FACT, §4.4]** *"The detection of PAC is good, with more than 75% PAC detected and a low false
positive rate (< 1%)."* And, recorded because it is the authors' own caution about an earlier number:
*"Note that we previously reported 82% of PAC detection in fugues with manual hand-coded rules but that
may have resulted in overfitting."*

**★ [FACT, §4.2] The stated reason the half cadence is hard — and it is the framework's own sentence.**
*"We also notably lack strong significant features for HC. Indeed, the Y-Z bass move in a HC is variable
(it is typically similar to X-Y moves in PAC)."* **[FACT, §4.4]** *"The detection of HC is difficult
(Haydn corpus), as there is not a single feature applicable to every case. Half of them are detected,
with about 2% FP."*

**[FACT, §4.4]** Of 28 PAC false positives in Haydn, *"at least 5 FP can be seen as actual cadences"* —
the annotation itself is contestable at the margin.

**[FACT, §4.4]** Rhythmic features matter most where the harmony is weakest: *"Rhythmic features (R)
bring an improvement especially for HC, in particular with R-Z-strong-beat that correctly filters out
more than half of the beats."*

## Coupling facts (mandatory)

**What it ASSUMES about its upstream.** A symbolic score with **voices** (files were voice-separated
`.krn`; *"the features proposed here could also apply to non-separated files, except for after-Z-rest-*
and Y-Z-bass-same-voice"*), **metric position** (`R-Z-strong-beat` needs to know which beats are strong
for the time signature), **a bass voice**, and **durations**. It assumes **no key**, **no chord
segmentation** and **no harmonic analysis**. Features are extracted with music21; classification with
scikit-learn.

**What it HANDS downstream.** A per-beat binary verdict — this beat is or is not the arrival point of a
cadence of the trained type (PAC, rIAC or HC) — and, in the study itself, the per-feature significance
tallies of Table 2. It hands on **no chord, no key, no segmentation and no cadence type beyond the class
trained for.**

**Its own STATED SCOPE and limits.** Two corpora, Bach fugues and Haydn quartet expositions; the
annotations *"model cadences in the light of a global analysis of the form"* while the detection is
local, which the authors state as a known mismatch: *"we have used them as a benchmark on our local
feature-based detection."* Suspensions were expected to be significant for both PAC and HC and *"do not
appear significantly in these corpora."* The conclusion names the shape of the fix: *"Cadence
preparations could for example be described by features regarding contiguous 'spans' of onsets rather
than single onsets X and Y, in order to improve the harmony relevance of the model. Research along these
lines could significantly improve HC detection."*

## What an L1 detail specification could adopt, adapt, or must argue against

- **Adopt — the three-onset frame (X, Y, Z) as the shape of a local cue.** A cue is not a property of one
  moment but of an arrival and its named preparation, and the paper's own ablation shows the preparation
  earns its place: dropping X and Y (feature set ZR) costs 0.80 → 0.52 on Bach PAC.
- **Adopt — the bass-implied-tonality construction.** `Z-bass-compatible-with-I` is a *hypothetical*
  tonality anchored on the bass of the arrival, tested by the presence of degrees 4 and 7 in the
  preceding beats. **This is exactly what lets a cue be key-agnostic without being tonality-blind**, and
  it is the construction the L1 charter's third cue names.
- **Adapt — the metric-strength cue as a filter rather than as evidence.** `R-Z-strong-beat` *"correctly
  filters out more than half of the beats"*, which is a different role from contributing weight.
- **Must argue against — nothing here.** The paper is not a rival to any chosen point; it is the primary
  under one.

## ★ Findings, routed and not applied

**(1) The L1 charter's cadence-cue paragraph verifies at this primary, in three separate places.** The
charter says the cues are *"computable from the notation without knowing the tonality"* — §2.1 says the
authors do not perform tonality estimation, and §1.3/§2 say they avoid chord segmentation and harmonic
analysis. The charter says *"hand-designed local features reach F .80 on perfect authentic cadences
with, in the authors' words, no chord segmentation and no tonality estimation"* — Table 3, bach-wtc-i
PAC, F₁ **0.80**. The charter says the half cadence is weak *"because the bass motion into a half cadence
is variable"* — §4.2 in the authors' own words. **No correction is owed on any of the three.**

**(2) The framework's third cue is this paper's feature, and the precision is worth carrying into the
detail specification.** The charter's *"the sounding together of the fourth and seventh degrees of a
candidate tonality in the approach"* is `Z-bass-compatible-with-I`: degrees 4 and 7 **of the tonality
implied by the bass of the arrival chord**, present **in the four beats before it**. The phrase
*candidate tonality* is therefore not loose — it names a hypothesis anchored on a note the score gives,
which is what keeps the cue inside L1's *decides nothing* rule. **Recorded for the derivation; nothing
is amended.**

**(3) A caution the charter does not carry, and a derivation should.** The Haydn cadence annotations
this study is graded against *"model cadences in the light of a global analysis of the form"* while the
detection is local, and the authors say at least five of the twenty-eight Haydn PAC false positives
*"can be seen as actual cadences"*. **The ceiling on a local cue is partly an artefact of a
form-level ground truth** — principle #21's shape, on the cadence axis. **Routed to measurement design.**

**(4) No falsifier.** Nothing read contradicts any CHOSEN design point. **No STOP fires** under the
remedial commission's §5.

## Centrality

**CENTRAL** — it is the primary under a chosen design point's recorded ground and under verification
target V6. **A second independent extraction is owed** under the original commission's §4 and has not
been performed.

## What this extract does NOT do

It derives no specification statement, amends no document, opens no code, touches no measurement tool,
corpus or golden, writes no open-items row and allocates no decisions-register identity.

---

*Provenance: written 2026-08-31 by the Cowork session that booted on
`cowork_handoff_entry_eighty_seven.md` and performed the ordinary session-start read. The paper was read
at the object as page images, pp. 355–361. No shell command was run on the repository or on any staged
copy of it for content or for listings; the container copy used for writing this file is declared. Every
value above is the paper's own (#17f, D-431).*
