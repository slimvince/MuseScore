# L1–L3 stabilization plan — bring the lower layers to production shape before building Architectural Layer 4

> **Why this exists.** We will build Architectural Layer 4 **once, on a stable, correctly-bounded L1–L3** — not on the
> current code, which (a) bakes in the "whole score is always loaded, no layer ever asks for more" assumption the
> product does not have, and (b) still carries measured-but-unapplied key-inference improvements. Every lower-layer
> change ripples up; doing them after L4 sits on top means re-validating L4 too. So we stabilise L1–L3 first.
>
> **Discipline applied throughout:** knowledge-based (measure before building); investigate-by-default (a read-only
> design precedes each non-trivial step); total unification (one path per concern); byte-identity guards where a step
> must not move output; the two-tier BIR gate + both test suites + pinned snapshots as the standing safety net. Each
> step below becomes its **own** gated Claude-Code instruction when we reach it — this document is the **sequence and
> the gates**, not the build instructions.

## Ordering principle — build-it-right BEFORE tune-precision (user-ratified 2026-06-25)

**★ THE RULE ITSELF IS HOMED AT `CLAUDE.md` PRINCIPLE #8, AND THIS SECTION POINTS AT IT RATHER THAN
RESTATING IT (user-ruled 2026-08-04; D-557).** The ordering principle this plan was written under —
build-it-right BEFORE tune-precision, strictly, with all three of the refactoring, the architectural
design and the algorithmic completion finished before any inference-problem fixing anywhere — was
widened into `CLAUDE.md` principle #8 on that date, in the fuller form this section had carried since
2026-06-25. One rule, one home (#6): the governing document states it, this plan applies it. The
former wording of this section is preserved verbatim in **D-557**'s provenance (#12).

What this plan adds, and what is therefore still stated here: **which of ITS OWN phases fall on each
side of the principle.** Build-it-right covers this plan's Phases 1–4 and then the L4/L5/L6
algorithmic builds, each layer built to use **all available evidence** (the **maximal-information**
principle — *including the notated spelling / tpc capability*); **no reactive precision-chasing
happens in them.** Tune-precision is **Phase B — LAST, after the whole L1–L6 stack is built** — the
reactive *"actively understand why inference isn't as good as we hoped"* work: the measured
key-quality levers (scale-membership), the leading-tone de-brittling, the L3 tpc-weight calibration.

Within build-it-right, strict bottom-up: the **bounded-context foundation** (Phases 1–3) first; then the **tpc spelling
capability** (Phase 4 — a *maximal-information foundation*, built early so L4 is spelling-aware from the start; **this
is capability, not precision tuning**). The foundation phases (1–3) are **byte-identical on the corpus** (degenerate
"selection = score", no extension fires); the tpc capability (4) is built with its term safely defaulted so it stays
**BIR-flat** — its precision *realisation* is a Phase-B tuning item. **No phase here is allowed to chase the key
numbers.**

## Audit-derived items (folded in 2026-06-26 — `cowork_l1l4_architecture_audit.md`)
The L1–L4 audit found the *target* architecture sound; the debt is **unretired legacy on the orchestrator** plus
housekeeping. Each item is **build-it-right** (refactoring / unification / coverage / docs — none is precision work),
slotted into the existing order, NOT acted on out of sequence:
- **Immediate, ungated — doc-truth (do now; it actively misleads every session start):** `STATUS.md` and ~8 docs still
  present the stale **57/23/57** gate while CLAUDE.md is on the ratified **53/24/53** — the two session-start docs
  contradict each other. Also the stale CMake "NOT wired" comments (slicer / `keymodesequence` / `jointkeydecision`
  ARE wired), orphaned test fixtures, and stale tool corpus-dir defaults. Doc-only, no code, no gate risk → its own CC
  instruction, not blocked by any phase. (This is the deferred doc-hygiene refresh, **promoted** because of the gate
  contradiction.)
- **Phase 5 (pre-L4 house-cleaning) gains** the byte-identical structural refactors + coverage backfill.
- **New Phase 6 (legacy retirement / unification) gains** the live-duplication fixes — they can only land once the new
  paths are load-bearing (after the L4/L5/L6 build), so they sit between the build and Phase B.

---

## Phase 0 — baseline & guards (no code change)
- Re-confirm, freshly run, the current BIR identity sets (**Baroque 53 / Jazz 24 / Default 53** — the ratified set; the
  prior 57/23/57 here was stale, corrected 2026-06-26) and the pinned snapshot state — the gate references every later
  phase is measured against.
- Establish the **byte-identity guard** for Phases 1–3: the whole-score corpus run must stay byte-identical through
  them (the degenerate case). Any corpus movement in Phases 1–3 is a STOP — it means the degenerate case is not
  byte-identical, i.e. a real bug.

## Phase 1 — Architectural Layer 1: build-over-selection + the *extend* operation (the foundation; the non-trivial piece)
*Read-only design first* (the index-under-extension is the genuinely hard part; design it before coding).
- **1a — the contract, with an interim rebuild.** Implement *build over a selection* + *extend(direction, stop,
  bound)* (append-only, clamp at the score boundary, report boundary-reached) per `cowork_bounded_context_design.md`.
  **Interim:** on extend, Architectural Layer 1 may **rebuild over the enlarged span** (correctness first) — the
  *contract* is what the layers above are written against, so the interim is invisible to them. **Gate:** the
  degenerate case (selection = score, never extended) is **byte-identical** → corpus byte-identical; plus new unit
  tests for extend (append-only, idempotent re-request, boundary clamp/report).
- **1b — incremental index (DEFERRED, byte-identical perf).** Replace the interim rebuild with an incremental/extending
  look-up index. **Gate:** byte-identical to 1a (a pure performance step) + the index ≡ linear-scan property over
  extended spans. *Deferrable past L4 — it changes no behaviour; the contract from 1a is what matters now.*

## Phase 2 — Architectural Layer 2: re-slice on extend
- Produce change-point slices for the **newly loaded region** on extend (additive — existing-region slices are a local
  fact and must not change), preserving complete coverage and slice identity over the enlarged span; mark
  context-span slices as evidence (not output). **Gate:** degenerate case byte-identical (corpus); the existing
  whole-corpus `--validate-slices` property holds over extended spans; existing-region slices proven unchanged by an
  extension.

## Phase 3 — Architectural Layer 3: reach-back as an extension request
- Wire reach-back to the Phase-1 *extend*: direction = earlier, stop = *"the prevailing key before the selection is in
  view,"* hard bound = a max reach, terminating at the score start. Output only for the selection; context slices
  anchor the carried-in key. **Gate:** the corpus (whole stems) **never fires reach-back** (a piece start has nothing
  earlier) → byte-identical; new **partial-selection behaviour tests** — reach-back fires and terminates, the
  leading-edge key is anchored by the carried-in context, a selection at the score start truncates cleanly; and the
  **equivalence invariant** — analysing a selection with extension equals a fresh run over the final loaded span.

*End of Phase 3: the bounded-context foundation is built, the assumption is correct, and the corpus is byte-identical.*

## Phase 4 — the tpc spelling **capability** (the maximal-information foundation; build-it-right, BIR-flat)
Build the **one shared spelling-derived view** (Architectural Layer 1 already carries the notated tpc) — used by
Architectural Layer 3 (key) **and** Architectural Layer 4 (chord) — so the algorithm uses **all** the evidence the
score provides, never spelling-blind. **This is capability, not precision tuning:**
- **The shared spelling view + Architectural Layer 4's deterministic spelling-pin** (the symmetric-root pin: the
  notated spelling *names* the root — no degradation) are the capability. Build them here, **before L4**, so L4 is
  spelling-aware from the start and never retrofitted. Unification: **one** spelling view, used by both layers, never
  duplicated.
- **The L3 key emission reads tpc-aware evidence**, but with its term **safely defaulted / gated** so the build is
  **BIR-flat** — the *weight* that realises the precision gain (and that costs stable regions without Layer-5 function
  gating) is a **Phase-B tuning item**, not turned on here.
- **Gate:** BIR-flat on both presets (the capability lands without moving the numbers); both suites green. A small
  read-only design precedes the build.

## Phase 5 — pre-L4 house-cleaning: byte-identical refactors, coverage backfill, spec sync, sign-off
*Clear the structural + coverage debt the audit found BEFORE building L4 on top — all build-it-right, all byte-identical
or test-only (no behaviour change, no number movement).*
- **Byte-identical layering refactors (audit Q1/Q2)** — each its own gated step, **gate = byte-identical corpus + both
  suites + snapshots** (corpus by-construction acceptable for a provably value-preserving refactor when the suites
  exercise the affected logic; see the `batch_analyze` prerequisite note below):
  - **kMasks single-source (audit Q1.3) — ✅ COMPLETE (`a0b983839a` + `e391f381e6`).** `kMasks` derives from the
    canonical `kTemplateIntervals`, AND `chordanalyzer.cpp`'s `templates[]` now consumes `kTemplateIntervals` too
    (`templateIntervalsVec()`, line ~1219) — one interval source feeds both, byte-identical. (Audit Q1.3 closed.)
  - **Types-only header (audit Q2) — LAST, with its own read-only investigation.** The *most* involved refactor:
    `KeyModeAnalyzer::PitchContext` is **nested**, so extracting it (plus `ChordAnalysisTone`/`ChordTemporalContext`/
    `ChordAnalyzerPreferences`) to a leaf `analysis/types/` header needs un-nesting + a full reference-graph chase.
    Grounded, then designed, then built.
  - *(The `function/` split — moving the L5/L6 `tonicizationlabeler` out of the L4 dir — is **DEFERRED to Phase 7**:
    its L5/L6 home does not exist yet, so doing it now is premature structure. It moves with the L5 build.)*
  - *(Open design question — whether winner-selection becomes its own unit — deferred to the L5 design.)*
- **Coverage backfill (audit Q3 + the stable-half branch triage) — round 1 DONE `d042a03a03`; round 2 is the ~321
  stable-branch ADD-TEST gaps** in `cowork_phase5_branch_backfill_spec.md` (oracle-asserted; the ~62 defensive branches
  annotated-excluded; the ~16 deferred). Tests-only, no production change; the moving ~600 branches triage at Phase 6.
- Re-run the spec↔implementation delta-check over L1–L3 — zero DIVERGENCE, operations present, predicates qualified.
- **Sync the L1–L3 specs to as-built:** the bounded-context contract (built), reach-back, the tpc capability; move
  build state to the delivery notes, keep the architecture prose code-free.
- Confirm the standing net: both suites pass, **BIR gate byte-flat** through Phases 1–4, snapshots untouched.
- **Then L4 is cleared to build** — on a stable, correctly-bounded, spelling-aware, structurally-clean L1–L3.

---

## Phase 5b — L4 algorithmic build + engagement (make the new spine load-bearing)
*★ AS-BUILT (2026-06-26): the L4 BUILD is **complete + proven, but DORMANT** — `chordslicedecoder` (G1–G6, two-reading,
spelling-pin) is built and measured (better where it commits; ~85% of abstention genuinely function-dependent → L5).
Per the ratified **engage-with-L5** strategy, ENGAGEMENT (the production switch off legacy `analyzeChord`/`ChordPathDecoder`)
+ the Phase-6 legacy retirement are **joint with L5**, not done here. Build state below; the engage decision lives in
`cowork_phase5b_l4_build_plan.md` Step M.*

> **HARD PREREQUISITE (RESOLVED `5357f5a7ed`).** `batch_analyze` was down earlier this session (the runner passed unix
> paths under `MSYS_NO_PATHCONV=1` — the Qt-plugins framing was a red herring); it is **restored** (Windows-forward-slash
> paths + `QT_QPA_PLATFORM=offscreen`), so the empirical corpus two-tier BIR gate is measurable again (and was, for Step M).
- **Build L4** per `cowork_layer4_chordsymbol_design.md`: the per-slice chord namer (`chordslicedecoder`) with
  commit / inherit / **abstain (declare uncertainty, not guess)**, the symmetric-root **spelling-pin** (consuming the
  Phase-4 spelling primitive), and the membership / NCT backlog in `cowork_delta_check_dispositions.md`.
- **Engage:** switch production (`region/regionanalyzer.cpp`) onto the new L1→L4 spine (the bounded-context engagement
  + the new chord path). This is the behaviour-changing step the foundation phases deferred.
- **Gate:** two-tier BIR + both suites + snapshots; any *meaningful* (class-b) movement examined, not refreshed.

## Phase 6 — L1–L4 SEAL: legacy retirement + dead-branch resolution + criterion-4 completion (BEFORE L5)
*Now that the new paths are load-bearing (Phase 5b), retire the legacy and finish the test seal. This is the step that
makes **"nothing left on L1–L4."** It sits **before L5** — there is no legacy L5/L6 to retire, so this is purely L1–L4's
sealing. Still build-it-right (unification), still no precision-chasing.*
- **One segmenter (Q1.1):** retire legacy `harmony/greedyExpandSegmentation` (`regionanalyzer.cpp:757`) onto
  `slicing/changePointSlices` — collapse the two live change-point grids to one.
- **One pitch-context builder (Q1.2):** collapse `collectPitchContext` (legacy, via `keyresolver`) and
  `pitchContextOverSpan` (new, via `keymodesequence`) to a single builder.
- **Resolve the staged scaffolding + dead branches (audit Q5 + the branch-coverage triage):** `chordslicedecoder`,
  `redecodeRange`, `tonicizationlabeler`, and the inert `DecodeQualityLevel::Normal/Deep` each reach a **wired-or-removed**
  verdict (decided by the Phase-5b build). The branch-coverage map's unhit directions are routed **three ways**: *add a
  test* → fold back to the coverage backfill; *wire-or-remove* → here; *exclude as intentional-unreachable* → defensive
  "can't-happen" code is **annotated, never deleted** (removing safety code to lift a coverage number is forbidden).
- **Criterion-4 seal:** with dead code resolved and defensive branches excluded, **union** branch coverage
  (`composing_tests` ∪ `notation_tests`) over the truly-reachable L1–L4 set reaches the ratified adequacy bar — every
  *reachable* branch covered.
- **Gate:** each retirement is its own ratified CC instruction under the **two-tier BIR gate + snapshots + both suites**;
  meaningful (class-b) movement is examined, not refreshed.

### ✅ L1–L4 COMPLETE — the *nothing-left* gate (the precondition for L5)
Restructured, built, **engaged**, legacy-free, dead-branch-resolved, specs synced to as-built, and regression +
*reachable-branch* tested to adequacy. **L5 does not begin until this gate is green.**

## Phase 7 (L5 function) · Phase 8 (L6 grouping) — on the sealed foundation
Each layer **designed → built → tested** in order, on the sealed L1–L4 (and L5 for L6): its own read-only design first,
its own four-criteria adequacy + branch tests. They are *new* — no legacy to retire — so each ends at its own
"complete" gate. The whole L1–L6 stack must be built and tested before Phase B.

---

## Phase B — tune-precision (DEFERRED to LAST; only after the full L1–L6 algorithmic build)
**Not done in this plan.** The reactive *"why isn't inference as good as we hoped"* work runs **only after**
refactoring + architectural design + algorithmic completion (L4/L5/L6) are done — per the ordering principle. Recorded
here so the items are not lost:
- **B1 — scale-membership scorer lever** (measured ~+57…+73 / +38…+68 decode-only; apply + calibrate the production
  magnitude; two-tier BIR gate).
- **B2 — leading-tone presence-gate de-brittling** (the diagnosed non-Bach C→F key regression; weight-scale the char/lt
  `>0.1` gate; gate = the three xfail'd notation tests flip to C + BIR holds; diagnosis: L3 §11 +
  `cc_keyregression_diagnosis_report.md`).
- **B3 — L3 tpc-weight calibration** (turn up the Phase-4 spelling term once Layer-5 function can gate the
  tonicization-vs-modulation cost — the precision *realisation* of the capability).
- **B4 — remaining L3 follow-ups**: Step-2 scaleMembership reweight, P4 tick-local path, S1 seed-retire, sequence-margin
  confidence redesign, "uncertain"-recall raise. Each measured/gated; take only net-positive.

---

## Dependency summary
```
(ungated, do now) Doc-truth: STATUS.md + ~8 docs → 53/24/53; stale CMake/fixtures/tool-defaults   [doc-only]

Phase 0 (baseline)
   └─> Phase 1  L1 build-selection + extend   [byte-identical corpus]   ──(1b index: deferrable)
          └─> Phase 2  L2 re-slice on extend  [byte-identical corpus]   ✓ DONE
                 └─> Phase 3  L3 reach-back    [byte-identical corpus + partial-selection tests]
                        └─> Phase 4  tpc spelling CAPABILITY  [BIR-flat; term defaulted]
                               └─> Phase 5  pre-L4 house-cleaning: byte-id refactors + coverage + spec sync  ─> L4 cleared
                                      └─> Phase 5b  L4 build + engagement (new spine load-bearing)  [two-tier BIR gate]
                                             └─> Phase 6  L1–L4 SEAL: retire legacy + dead-branch + criterion-4 (union)
                                                    └─> ✅ L1–L4 COMPLETE (nothing left) ── precondition for L5
                                                           └─> Phase 7 (L5 fn) ─> Phase 8 (L6 grouping)  [each built+tested]
                                                                  └─> Phase B  tune-precision (LAST, whole stack sealed)
```

## Notes
- **Each phase is its own gated Claude-Code instruction**, written when we reach it; the non-trivial ones (Phase 1
  especially) get a **read-only design** first.
- **Phases 1–3 should not move a single corpus number.** If they do, the degenerate-case byte-identity is broken —
  STOP and investigate, do not refresh snapshots to "fix" it.
- **Three movement classes, by phase:** **Phases 1–4 do not move the numbers** (1–3 byte-identical; 4 BIR-flat, term
  defaulted) — any movement there is a bug, STOP. **Phases 5b–8 are behaviour-changing build-it-right** (engagement,
  legacy retirement, the L4/L5/L6 builds): they run under the **two-tier BIR gate** — **zero** class-(b)
  (pitch-class-decidable) regressions ever; only small, every-case-verified class-(a) symmetric churn is tolerated.
  This is *correctness/architecture* movement, **not** precision-chasing. **Phase B is the only precision-tuning** — the
  reactive "better the inference" work, last, over the whole sealed stack.
- **The build-it-right → tune-precision firewall:** no inference-problem-fixing anywhere in Phases 0–8. Phase B does not
  start until the **L1–L6 stack is built and tested** (and L1–L4 specifically is at its "✅ COMPLETE — nothing-left"
  gate before L5 even begins).
- **`upstream` untouched throughout** (fork-local; the cfc7eb5e39 distribution constraint stands); push to `origin`
  only, when each gated step is ratified.
- The L4 build backlog (`cowork_delta_check_dispositions.md`) feeds **Phase 5b** (the L4 algorithmic build), not the
  earlier phases.
