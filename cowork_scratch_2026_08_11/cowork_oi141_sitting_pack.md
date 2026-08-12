# OI-141 — the reading pack for the design sitting, and the one question that must be settled before it opens

> **STATUS: COWORK WORKING DRAFT, written 2026-08-11 while
> `cc_instruction_return_continuation_14.md` is still running. OUTSIDE the tree by design —
> Cowork is READ-ONLY on the repository until that dispatch stops.**
>
> **★ LANDING NOTE (2026-08-11, appended at the verified STOP; the banner above is preserved
> as written, #12).** That dispatch has COMPLETED and the file is now IN the tree, at
> `cowork_scratch_2026_08_11/`. So the words *outside the tree* describe where it was
> WRITTEN, not where it is — the read-only condition they state has lapsed. **Nothing else in
> the banner changes: this is still a draft, still not ratified, and it still designs
> nothing.**
>
> **★ IT DESIGNS NOTHING, AND THAT IS NOT MODESTY BUT THE RULE.** D-231 forbids fix DESIGN
> until phases 1 and 2 complete, and #8's three-clause gate stands. This file assembles what
> the sitting READS and states one question that bears on whether the sitting can proceed on
> the material it has. It proposes no option, ranks nothing, and recommends no design.
>
> Every claim below is cited to the row or the document that makes it. Nothing is carried
> from memory (the never-work-from-memory rule), and no figure is transcribed — the figures
> live at the artifacts the row names (**D-431**).

---

## 1. What the sitting is, in the record's own words

The commissioning surface groups OI-141 under **what blocks it: a user ruling**, and states
the act as *"The key-menu design conversation itself. The row records the diagnosis, the
drift grounding, the mechanism pinned at the code and the design opening as all delivered —
what is left is the user's."*

So the sitting is not blocked on a measurement, a probe or a session's work. Four inputs
were delivered and the fifth act is the conversation.

---

## 2. The four delivered inputs, in the order they were made

Read from `open_items/OI-141.md`, which carries each with its provenance.

1. **The reframing (user, 2026-07-12)** — *"understand why our key/mode inference does not
   work."* With it, four recorded directions: that the key/mode inference is measurably not
   good enough; that needing chord-derived evidence is a HYPOTHESIS to test rather than
   assume, refined by the probe's fact that chord roots cannot split relative keys; that the
   isolated key check already exists and what was missing was the DIAGNOSIS; and that the
   present-but-outranked half is likely solvable by published methods (#2).

2. **The diagnosis (`cc_key_mode_inference_diagnosis_report.md`)** — the failing mass broken
   down by cause, reconciled exactly to the then-ratified key column on all three presets.
   Its two structural findings: roughly half of the failing mass is **not a genuine inference
   error** (the tonicization/modulation label gap dominates, plus a corpus transposition
   mismatch that became OI-142); and among the genuine errors, **wrong-key-area drift
   dominates ahead of relative-key confusion**. **Six of its eight written predictions
   FAILED**, which the row itself records as a diagnosis-worthy incompleteness under #17/#3.

3. **The drift grounding (`cowork_key_drift_research_grounding.md`)** — Temperley 2002 read
   and verified in-paper; the repository's own prior findings mined first; Feisthauer and the
   local-key-estimation field at abstract level, with the unfetchable source flagged rather
   than filled. It ends in six grounded implications, the first of which is a checkable
   premise it declares owed before any design.

4. **The mechanism pinned at the code (`cc_l3_key_decode_mechanism_report.md`, read-only)** —
   which answers that first premise: **the decoder is NOT full-lattice.** The per-slice
   emission scores every state with no prune, but the whole-sequence Viterbi runs over a
   pruned lattice — the global union of each slice's emission top-8 — so a key never top-8 at
   any slice is absent from the search entirely. Within that set the Viterbi is exhaustive
   and global. **Cowork's three predictions: one met, two failed or refined.** Three genuine
   errors were re-traced at the decoder's own numbers and produced **three distinct
   mechanisms, none of them a carried-list beam drop** — a local-emission failure, an
   emission-model absence, and a change-cost over-smoothing — which **corrects the diagnosis
   report's own "drops off the beam" phrasing.**

5. **The design opening (`cowork_key_layer_design_opening.md`)** — seven design decisions
   with grounded options and written expectations, under the user's stated frame that
   **maximum precision governs (#4)**: complexity, code volume, architectural redesign and
   long analysis times are all acceptable, with the effort preset as the sanctioned latency
   valve. Three cheapest read-only deciders are named there as the recommended first acts.

---

## 3. ★ THE QUESTION THAT MUST BE SETTLED BEFORE THE SITTING OPENS

**It is raised as a QUESTION, and it is not a finding.** Cowork has checked dates, which is
all that is checked below; it has NOT read the code, and no claim about what the production
arm does is made here.

**The dates, each read at the record:**

- OI-141's mechanism report, its grounding and its design opening are all dated
  **2026-07-12**.
- The joint estimator became the **production inference layer on the batch/corpus surface**
  at the OI-178 adoption, **2026-07-26**, and on the **in-app notation surface** at the
  notation switch, **2026-07-27** — both recorded in `CLAUDE.md`'s gate block (A), which
  states in terms that the migration state is now CLOSED on BOTH surfaces and that the legacy
  notation path remains compiled and dormant.

**So the mechanism the sitting's fourth input pins — the top-8 emission-union lattice, the
three hand-set change costs, the four-beat emission window, the single start-tick anchoring —
was traced at the code TWO WEEKS BEFORE the arm it was traced on stopped being the production
arm.** Whether that mechanism still describes the shipping path, describes it partly, or
describes the dormant legacy path only, **is not established anywhere Cowork has read**, and
the answer changes what the seven design decisions are decisions ABOUT.

**Why this is surfaced rather than rowed and left.** D-641's test is whether a finding's
subject bears on the analysis, its inputs, or an instrument a measurement depends on. The
subject here is which code path performs key inference on the shipping arm, which is the
analysis itself. The rule says such a thing is surfaced to the user **whatever its size**.

**Why it is not checked here.** The freeze, the one-dispatch-at-a-time rule and the read-only
hold while CC runs all point the same way. The check is small and nameable: **establish, at
the call graph, whether the joint estimator's decode consults `keymodesequence` /
`keymodeanalyzer` on the production arm, or carries its own key path** — which is the same
shape as OI-220's act and adjacent to OI-357's, both already on the finish line. It is a
session's act on a licence, not something to be assumed either way.

**What it does NOT imply.** It does not imply the four inputs are void. The diagnosis is a
measurement against ground truth and is arm-independent in what it counts; the grounding is
published research and is independent of our code entirely. **It is specifically the fourth
input — the pinned mechanism — whose subject is a particular code path**, and specifically
the design decisions that rest on that mechanism (retiring the top-8 prune; the change-cost
model; the emission window) whose object could have moved.

---

## 4. What the sitting will need in front of it

In the order the record puts them, and pointed at rather than summarized (#6):

1. `cowork_key_layer_design_opening.md` — the seven decisions and the three cheapest
   read-only deciders.
2. `cowork_key_drift_research_grounding.md` — the published basis, with its unfetchable
   source flagged.
3. `cc_l3_key_decode_mechanism_report.md` — the pinned mechanism, read WITH §3's question
   beside it.
4. `cc_key_mode_inference_diagnosis_report.md` and
   `tools/reports/key_mode_inference_diagnosis.json` — the cause breakdown and its six failed
   predictions.
5. `CLAUDE.md` gate block (A) — the current baselines, and **D-576's caveat**, which bears
   directly on this sitting: the root-agreement measurement **understates what a wrong key
   costs**, because root and bass are largely key-independent while quality, Roman numeral
   and some inversions are corrupted by a misread tonality.
6. The two grading conventions that decide how a remaining key disagreement is READ: that a
   **defensible modal reading the major/minor ground truth cannot represent is a ground-truth
   limitation, not a defect to optimize away**; and that the **binding metric for a modulation
   detector is modulation correctness, explicitly not the agreement percentage.**

---

## 5. The standing constraint the sitting sits under, stated so it is not re-argued

**D-231 orders three phases strictly, and phase 1 is open.** The conversation the row names
is the user's to open, and the record places it on the finish line; **what it may produce
without breaching D-231 and #8 is a matter for the user, not something this file decides.**
The three cheapest deciders the design opening recommends are read-only probes, which is the
middle stage of #17's funnel — desk-simulate, then read-only probe, then build — and the
funnel's own scope clause allows surprises in explorational runs while forbidding them when
inference code is being built.

---

## 6. What this file does not do

It designs nothing and ranks nothing. It authorizes no probe, no measurement and no edit. It
moves no row and proposes no ruling. It states one question with its date grounding and names
the act that would settle it, and it settles nothing itself.

---

## 7. ★ §3's QUESTION IS SETTLED, AND ALL SEVEN DECISIONS ARE RE-PINNED AT THE ARM THAT SHIPS

> **Rewritten 2026-08-11 (Cowork) after the premise re-pin ran. §§1–6 are untouched (#12). The
> FORMER §7 is preserved whole at §7b below — it is the text the re-pin was commissioned against,
> and it was wrong in both directions. The defect is Cowork's; the re-pin that found it is CC's,
> read at `cowork_away_returns.md` §2.20 and §2.22 in full rather than from any summary.**

**The act §3 named was performed** — a read-only call-graph establishment — and then a **premise
re-pin over all seven decisions**: one question each, *what is the corresponding mechanism on the
shipping arm, and does the decision have an object?* Both traces, with their code citations, are
at `cowork_away_returns.md` §2.20 and §2.22 and are not restated here (#6). The production path is
`produceNotationRecord` → `decodePiece`, and the batch surface reaches the same decode.

**★ HOW THE FORMER §7 WAS WRONG.** It recorded that three decisions had lost their object and
named the top-8 prune, the change-cost model and the emission window. Three do have no object —
but two of them are **not** those, and the change-cost model is the opposite of absent. The error's
shape is the trap the re-pin itself refused: *the pinned mechanism is absent* was treated as *the
decision has no object*, when the shipping arm carries a different mechanism serving the same
decision.

**No object at all — decisions 1, 6 and 7.** Decision 1's top-8 emission-union prune is absent; the
shipping arm prunes keys by a different construction. **Decisions 6 and 7 have no object because
they were SUPERSEDED by ratified decisions, not because they are unbuilt** — the 252-state,
21-mode inventory does not exist on this arm (**D-524** in force, twenty-four keys), and decision
7's own document is banner-marked superseded by the joint-estimator architecture (**D-001**).
**That distinction matters more than the count: 6 and 7 are not repair candidates, they are already
decided**, and tabling them would re-open ratified architecture.

**Largely delivered — decisions 3 and 5.** Decision 3's key-proximity-structured change costs are
**built and fitted**, and its cadence-to-key channel is **built** as key-agnostic tonic-relative
features with their own fitted weights; only the phrase-boundary modulation inside it has no
object. Decision 5's output surface is **delivered and larger than the decision asked for** — a
full untruncated candidate list on both axes with the committed index — while its per-alternative
confidence half **has no object BY RULING** (**D-007**, content scores in nats rather than
confidences; **D-019**, the raw gap published unremapped).

**Split — decisions 2 and 4.** Decision 2's spelling-aware half is **built** as its own weighted
factor and its profile fitting is an object; its input-weighting question is already answered on a
row ([[OI-277]]); its window treatment has **no object**. Decision 4's declared-mode anchoring is
**built and already satisfies the decision** as a graded prior under its own weight; its
re-anchoring at a mid-piece notated key change has **no object**, and that half is already
[[OI-247]]'s subject, now confirmed at the shipping arm.

**Five analogies were met and NONE was ruled**, each reported with what the code settles and what
it does not. Ruling one would be a design judgment inside a fact-gathering act, which #8 forbids.

**★ WHAT THIS DOES TO THE SITTING — it is smaller and sharper than seven decisions.** Two are
already decided by ratified architecture and should not be tabled. Two would be re-stated as
largely delivered. **What is genuinely live is decision 1 re-framed against the prune that ships
rather than the one that does not, decision 2's window and leading-tone questions, decision 3's
phrase-boundary modulation, and decision 4's re-anchoring half — and the last already has a row.**
**This is a fact about the seven, not a proposal about any of them:** nothing here re-opens, ranks
or proposes a design decision, and what the sitting reads is the user's.

**What is NOT affected.** The diagnosis and its cause breakdown are a measurement against ground
truth and are arm-independent in what they count; the research grounding is published work and
independent of our code. Both stand.

**The by-product, rowed rather than fixed.** The call-graph trace answered a question a set of
committed comment verdicts had been HELD on, so [[OI-371]] records that `jointdecoder.h`'s
*"DORMANT (no production consumer)"* is false at HEAD. No comment was edited.

**One thing checked and closed, recorded so it is not raised a third time.** The trace establishes
there is no partial-signature correction anywhere on the shipping path, and Cowork asked whether
that undercuts OI-357's answered verdict. **It does not** — read at the two artifacts' own columns,
the production arm agrees with the annotation on that population markedly more often than the
legacy arm's explicit correction does, and the signature-lock signature very largely disappears;
no value is restated here (**D-431**). **The bound the artifacts declare themselves does survive:**
the cross-arm column rests on a derived duration-weighted stand-in established on one arm and with
no coverage on the other (#19). That bound was on the record when the verdict was ruled.

---

## 7b. ★ THE FORMER §7, PRESERVED WHOLE (#12)

> **This is the text §7 carried from 2026-08-11 until the premise re-pin replaced it the same day.
> It is kept because it is what the re-pin was commissioned against and the record of what was
> wrongly expected. It is wrong as described at §7 and must not be read as current.**

### ANNOTATION — §3's QUESTION IS SETTLED, AND THE ANSWER IS THE THIRD OUTCOME

> **Appended 2026-08-11 (Cowork), after the settling act ran. Everything above is preserved
> exactly as written (#12); nothing in §§1–6 is reworded, and this section corrects no
> sentence there — it reports what the act returned.**

**The act §3 named was performed** — dispatch `cc_instruction_row_landing_and_oi141_arm_check.md`,
Task 2, commit `f4339ab43b`, read-only, no `src/` edit — and the full trace with its citations
is at `cowork_away_returns.md` §2.20.

**The answer is outcome (iii): the pinned mechanism describes the DORMANT path only.** The
joint estimator's decode consults neither `keymodesequence` nor `keymodeanalyzer` on either
shipping surface; it carries its own key path. None of the four elements §3 names is running.
Cowork verified each citation at the code rather than at the report: the shipping prune is a
per-segment ranking over the twenty-four major and minor keys that always keeps the notated
signature's key, which is not a global emission union; the key transition is a fitted
distribution with a fitted weight applied to it, not three hand-set costs; and a four-beat window does
exist but belongs to the cadence detector — the same number reached by a different mechanism.

**What this does to the sitting, stated plainly.** §4's third input stands as a record of a
mechanism, and stops standing as a description of the arm that ships. Three of the seven
decisions §4's first input carries — retiring the top-8 prune, the change-cost model, the
emission window — therefore have **no object on the production arm** and cannot be taken in
the terms the design opening states them in. **The sitting should not run against §4 as
listed until that is repaired**, and repairing it is a fresh act, not a re-reading of this
file.

**What is NOT affected, and §3 already said so.** The diagnosis and its cause breakdown are a
measurement against ground truth and are arm-independent in what they count. The research
grounding is published work and is independent of our code entirely. Both stand.

**The by-product, rowed rather than fixed.** The trace answered a call-graph question a set of
committed comment verdicts had been HELD on, so `OPEN_ITEMS.md` [[OI-371]] now records that
`jointdecoder.h`'s *"DORMANT (no production consumer)"* is false at HEAD. No comment was
edited.

**One thing checked and NOT carried forward, recorded so it is not raised a third time.** The
trace establishes there is no partial-signature correction anywhere on the shipping path, and
Cowork asked whether that undercuts OI-357's answered verdict. **It does not.** Read at the two
artifacts' own columns — `tools/audit/oi357_production_arm_comparison.json` and
`tools/audit/oi357_legacy_arm_same_commit_control.json`, no value restated here (D-431) — the
production arm agrees with the annotation on this population markedly more often than the
legacy arm's explicit correction does, and the signature-lock signature the evidence document
diagnoses very largely disappears. The correction's absence is not a gap. **The bound the
artifacts declare themselves does survive and is not new:** the cross-arm column rests on a
derived duration-weighted stand-in whose establishment check can only run on the arm that
publishes both surfaces, so it is established on one side and has no coverage on the other
(#19). That bound was on the record when the verdict was ruled.

*Provenance: Cowork, 2026-08-11, at the STOP following
`cc_instruction_row_landing_and_oi141_arm_check.md`, every code citation and every artifact
column re-read at the object rather than taken from the executing session's report.*
