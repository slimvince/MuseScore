# EG-2 Scoping — Rebuilt-vs-Legacy Go/No-Go, Opened Under the Premise Gate

> **Cowork, 2026-07-10 (session 36). The FIRST work item opened under CLAUDE.md #17–#19.**
> EG-2 (`cowork_engage_arc_plan.md` Stage-3 entry gate): *does the REBUILT chord path (decoder
> carry + the intended selection) beat the LEGACY production path against the DCML root ground
> truth?* — the go/no-go on the whole E4 engagement. This document is the **desk-simulate-stage
> opening**: the premise ledger v1, the #19 instrument-establishment plan, and the desk-simulation
> plan. **The probe is NOT specified here** — per the #17 funnel it may only be specified after
> the desk simulation is done and its predictions are recorded, and may only RUN after the
> instrument is established. Instrument facts below were grounded by a read-only sweep
> (citations at file:line); no code changed.

## §1 The measured question, stated precisely

**Target quantity:** class-(b)-style (pitch-class-decidable-root) root-disagree DURATION vs DCML,
per preset, on the a8 union-of-boundaries unit (variant-b, segmentation-invariant,
duration-weighted) — the same unit as the robust stop. **Comparison:** the E0 full-spine chain
output vs the committed legacy `.ours.json`, both graded by the identical substrate.
**Verdict form:** rebuilt beats legacy iff its class-(b) root-disagree duration is lower per
preset by more than the desk-sim-predicted noise band, with the win/loss set-diff explained
per run (the block-(A) discipline). **Jazz is excluded from any correctness claim** (EG-6: no
licensed jazz GT; Jazz may be run consistency-only, labeled as such).

## §2 Premise ledger v1

**P1 (ASSUMPTION — the go/no-go claim itself).** "The rebuilt path is more root-correct than the
legacy path." This is the claim under test; its written quantitative prediction (direction +
magnitude band per preset + per failure class) is OWED at the end of the desk simulation (§4),
BEFORE the probe is specified. No prediction, no probe.

**P2 (FACT — the grading substrate is established).** The a8 unit self-validates byte-for-byte
against `compare_rn.grid_score_regions()` per piece (`tools/robust_stop/README.md:59-60`); the
E0 grader reuses it verbatim ("no new comparator", `cc_e0_fullspine_report.md:70-72`); the joint
probe already maps decoder output to DCML spans via the shared `_dcml_time_spans` +
`_active_index_at` (`measure_joint_probe.py:59-70`). Segmentation-invariance is load-bearing
here — the two paths segment differently (per-slice vs coarse regions) and the variant-b unit
absorbs that by construction. The legacy baseline is committed
(`tools/robust_stop/`, 63.36/62.37/63.25 root-agree, corpus `c50002fee1`).

**P3 (PROXY→TARGET — every gap between "E0 chain today" and "post-E4 production", declared per
#17(d)).** The probe's subject is a **proxy**; the target is post-E4 production. The gaps:

| # | gap | direction of bias | ledger treatment |
|---|---|---|---|
| G1 | **Key feed:** E0 gives the decoder ONE home key (`inferLocalKey[0]`, `cc_e0_fullspine_report.md:51`); E4 feeds per-slice L3 keys | **Handicaps the rebuilt path on modulating pieces** — a rebuilt WIN under G1 is strong evidence; a LOSS is ambiguous (could be the handicap) | asymmetric read of the verdict, declared up front |
| G2 | **Carry shape:** `topK=6` voicing cap (`chordslicedecoder.cpp:746-789`); the distinct-root carry is owed at E4 | the full-fan-out selection is NOT measurable; top-roots behavior is | probe measures the top-of-carry path only; stated in the verdict |
| G3 | **Selection:** the E0 chain runs the AS-BUILT resolver — progression-first + `attemptFineGrainOverride` UNCONDITIONAL (the Tier-1 traps, `functionresolver.cpp:221-246/529-531`) — NOT the intended selection (arc #9) | the override is measured net-harmful (−756): running it in the probe poisons the rebuilt arm with a known-bad component | **the probe arm must run with the override DISABLED** (the Phase-3 finding: "best measurable θ disables it") and must declare that the channel re-ordering is NOT exercised — the probe measures *decoder carry + argmax (+key/cadence arms as-built minus override)*, a LOWER BOUND on the intended selection |
| G4 | **Extensions carry gap:** `ScoringCell→ChordSliceCandidate` never assigns `extensions`/`naturalFifthPresent` (defaults 0, `chordslicedecoder.cpp:443-453`; `cc_e0_fullspine_report.md:227-254`) — seventh/aug6 labels structurally non-firable on the E0 chain | affects QUALITY labels; root grading mostly insulated — but per #17(e) the false-negative path must be enumerated: a missing seventh CAN flip a root where the seventh disambiguates rotation (dim7/V7♭9 family) | desk-sim case 3 (bwv272) probes exactly this; if the desk sim shows root flips from G4, the carry-fix precedes the probe |
| G5 | **Deferred C2/G5 chord types** (`chordslicedecoder.h:97-103`) | equal for both arms (shared template catalogue) — non-differential | declared, no action |

**P4 (Class B / #19 — the E0 instrument is NOT established).** What exists: flag-OFF
byte-identity to production (`cc_e0_fullspine_report.md:86-95`) and the established grader
substrate (P2). What does NOT exist: (a) the fs_* dumps carry a **stale manifest stamp**
(`d1d4d3d7f0` vs corpus `c50002fee1`) and the collector never calls `validate_corpus_dir`
(`cc_engage_c3_measurement_report.md:173-188`); (b) **no reproduce-check** of the chain output
(two runs byte-identical); (c) the **86-vs-2181 granularity reconciliation is unresolved**
(`cc_e0_fullspine_report.md:327-329`) — note: grading on the a8 unit (P2) makes this moot for
ROOT duration specifically, but that insulation claim itself must be checked (#17(e)): the unit
is segmentation-invariant only over covered spans; confirm equal coverage between arms.
Establishment plan in §3. **The probe may not run before §3 completes.**

**P5 (FACT — failure-population structure, the basis for per-class predictions).** From the O1
investigation (`CLAUDE.md` block (D)): ~60 % Baroque of the legacy residual is
spelling-resolvable, most of the rest bass/inversion or segmentation over-grab (which
`changePointSlices` removes by construction), and the genuinely function-only remainder is the
small share-tone set. The rebuilt path's wins should therefore concentrate in the over-grab and
spelling classes; the share-tone class should NOT move without the intended selection (G3).
These become quantitative per-class predictions at the end of the desk sim.

**P6 (THEORY — why the rebuilt path should win at all).** Per-slice decoding over the L2
change-point grid removes the over-grab class structurally (segmentation research grounding,
`cowork_functional_analysis_research_grounding.md`); the decoder's spelling-pin addresses the
symmetric-rotation class (Micchi/McLeod spelling line). Both are cited-specific (#2), but their
MAGNITUDE on this corpus is exactly what the desk sim + probe must put numbers on.

## §3 The #19 establishment plan for the E0 instrument (before any probe)

1. **Re-dump** `--dump-fullspine` ×presets on the pinned corpus at current HEAD; stamp a
   manifest (corpus `git_hash` + instrument commit + flag set) exactly per the a8 pattern;
   wire the collector through `characterise_bir_false.validate_corpus_dir` (the shared guard).
2. **Reproduce-check:** run twice; assert byte-identical output (the R10-b lesson: identity, not
   assumption).
3. **Derive what the unit measures on the E0 shape:** confirm the per-slice `regions[]` grade on
   the a8 unit covers the same DCML span set as the legacy arm (coverage equality check —
   the P4(c) insulation check). Any coverage asymmetry is a STOP.
4. **Override-off variant:** confirm the probe arm can run with `attemptFineGrainOverride`
   disabled via the existing dormant θ/params (no `src/` change; if a flag is needed, that is a
   separate revertible instrument `feat` per #14).

## §4 The desk-simulation plan (the #17(c) stage — hours, not a session)

Trace BY HAND, at the score, legacy-vs-decoder-under-home-key on five known failing runs —
"which term moves, by how much, on this actual case?" — and record the predicted winner per
case BEFORE any probe output is seen:

| case | class | what to trace | prior expectation to check |
|---|---|---|---|
| `bwv10.7@36000` | segmentation over-grab (5-note scale across `i43`/`iv532`) | does the slice grid split what legacy over-grabbed, and does each slice decode to the GT root? | rebuilt WINS by construction (P6) — if the trace does NOT show it, P6 is in trouble early |
| `bwv352@1440` | share-tone function-only (Am6↔F♯ø7) | pc-identical: does ANY decoder term separate the rotations under the home key? | NO CHANGE without the intended selection (G3) — a flip here would be a surprise (STOP) |
| `bwv272@4320` | symmetric dim7 rotation (G♯dim7) | the spelling-pin vs the key-gated `dim7CharacteristicBonus`; AND the G4 seventh-carry false-negative path | uncertain — this case DECIDES whether G4 must be fixed pre-probe |
| `bwv174.5@6240` | bass/inversion vs root (E/G♯ beats G♯ø7) | bass channel treatment in the decoder vs legacy's inversion bonuses | trace to predict; no prior committed |
| `bwv416@10080` | segmentation-union fix precedent | does per-slice decoding preserve the fix the union produced? | rebuilt should HOLD the fix; regression here = the slicing premise needs refinement |

**Output of the desk sim (the gate to the probe):** the filled prediction table — per-preset
direction + magnitude band on class-(b) root-disagree duration, per-class fire-rate expectations
(over-grab, spelling, bass/inversion, share-tone), and the G4 disposition (carry-fix before
probe: yes/no). Recorded in this doc as §5 BEFORE the probe instruction is written.

## §5 Written predictions — ★ OWED (empty by design)

*To be filled at the end of the desk simulation, before the probe is specified. No prediction,
no probe (#17(b)).*

## §6 Sequencing (corrected at pre-registration, 2026-07-10)

**Strictly sequential, per the #17 funnel: (1) commit this doc with §5 EMPTY (pre-registration —
the plan is provenance-stamped before any measurement, #16/#17(b)); (2) desk sim (§4) — the
cheapest stage runs first and may kill or reshape the probe before the establishment re-dumps
are paid for; (3) instrument establishment (§3) only if the desk sim's filled predictions
warrant a probe; (4) probe spec, then run.** The probe itself is read-only (explorational
scope — surprises permitted there; they feed the ledger). The verdict comes back to the user
with the P3 asymmetry applied: a rebuilt win under the G1 handicap is decision-grade; a loss is
diagnosed before any conclusion is drawn.

*Cowork, 2026-07-10, session 36. Instrument grounding sweep citations:
`cc_e0_fullspine_report.md`, `cc_engage_c3_measurement_report.md`, `measure_joint_probe.py`,
`tools/robust_stop/README.md`, `chordslicedecoder.{h,cpp}`, `batch_analyze.cpp`,
`cc_anchor_redesign_dossier.md`, `cc_absent_root_investigation.md`,
`cowork_layer5_engagement_design.md`, `cowork_l1_l5_premise_debt_audit.md`.*
