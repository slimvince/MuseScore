# Cowork Session Handoff — MuseScore Studio Harmonic Analysis

*Written 2026-05-14. Last updated 2026-06-10 session 5 (explorationMode dual-path eliminated; HEAD `e7d4ba2b1a`).*

---

## STANDING RULE FOR COWORK (read every session)

**Cowork writes instruction files. CC executes them. Never the other way around.**

- When the user says "go", "do E2b", "execute", or similar: the response is
  "The instruction is ready at `cc_instruction_X.md` — give it to CC."
- Cowork MAY: read source files (grep/cat/sed -n), write `.md` instruction files,
  update `cowork_handoff.md` / `STATUS.md` summaries after CC reports.
- Cowork MUST NOT: spawn agents that run build commands or modify `src/` files;
  use Edit/Write tools on anything under `src/`; use bash redirects on source files.
- Violating this rule has broken the codebase twice (E1, E2b). Do not do it again.

---

## What this project is

MuseScore Studio. The active development area is `src/composing/`, which implements
harmonic analysis (chord detection, inversion scoring, key inference). The main file
is `src/composing/analysis/chord/chordanalyzer.cpp`. The bridge between the composing
module and the notation layer is `src/notation/internal/notationharmonicrhythmbridge.cpp`.

Mandatory reads at the start of every session:
- `C:\s\MS\STATUS.md` (header only, first ~10 lines) — current baselines and HEAD commit
- `C:\s\MS\build_and_test.md` — all build/test/tool commands

**When CC returns a report**, always do this before evaluating it:
1. Re-read the instruction file that CC was given (listed in "Next CC task" in Current state below)
2. Then read CC's report

CC's report references task numbers, design decisions, and deviations that only make sense against the original instruction. Evaluating the report without re-reading the instruction means accepting CC's framing uncritically — which is exactly the failure mode we guard against.

**THE WORKING METHOD (canonized 2026-06-12, user mandate — these principles produced
Stages 0–3.1b without a single unplanned regression; they are not optional):**

A. **Pin before you change.** No layer/gate/method is built upon until its current
   behavior is pinned (tests) and its instruments verified (metrics, corpora, source
   identity). Instruments first, measurements second, changes third.
B. **Byte-identity bridges for every restructure.** A refactor earns zero improvements;
   its gate is 0-diff across corpora (all relevant configs), snapshots, and suites,
   with FP near-tie canaries unmodified. Golden refreshes as a reflex are FORBIDDEN —
   a diff is a stop, not a chore.
C. **Behavior changes are deliberate, measured, ratified.** Never shipped as a side
   effect (the 3.1b lesson). The answer-delta is measured BEFORE the commit is
   proposed; ratification decides on data.
D. **Never guess — investigate or state the unknown** ([probe]/[code] tags, explicit
   Unknowns sections). Binds CC and Cowork equally. Read the call site, not just the
   qualifier (the completeTriad lesson).
E. **Stop conditions are designed in advance and honored.** The system's best moments
   were stops (snapshots 0/11; DCML-worse; tracked-junk deviation). A tripped stop is
   the process succeeding.
F. **Falsified decisions get re-decided, and their evidence gets committed** (Q1 →
   `p3_granularity_ab_3_1b.md`; the cap archaeology; the M3 reconstruction). Dead ends
   are documented so they are never re-walked.
G. **One change-class per commit, explicit staging, every commit independently
   verified** (`git show --stat` + host-side reads against the claims).
H. **Errors are owned by name** — Cowork's included (the snapshot-harness premise, the
   whole-score prior, the relay gaps). Ownership is what keeps the ledger honest.

**STANDING RULE — CC trust model (made permanent 2026-06-10, user mandate):**
1. **Never fully trust CC.** CC can hallucinate, guess, and present guesses as findings.
   Every consequential CC claim gets independent verification before acceptance:
   commit contents via `git show --stat`, code claims via host-side Read/Grep of the
   actual source, numeric claims against recorded baselines. Track record this session:
   CC has been right where verifiable most of the time, but produced at least one
   guessed mechanism stated as fact ("parallel batch path resolves ties
   nondeterministically" — wrong, batch_analyze has no threading) and one
   imprecise-memory claim (junk files "M/regenerated" — that one was Cowork's own
   stale-sandbox error; verification cuts both ways).
2. **CC does not hold the bigger picture — Cowork does.** CC optimizes the task in
   front of it. Cross-cutting consequences (gate semantics, baseline integrity, layer
   architecture, re-baseline bundling, what a finding means for Stages 2–6) are
   Cowork's to evaluate. When CC proposes a disposition for a finding ("log it for
   later", "not a blocker"), treat that as input, not a decision.
3. Both rules also bind Cowork's instructions to CC: the never-guess /
   investigate-or-state-unknown rule (introduced Stage 1d) is standing for ALL future
   instructions, not per-instruction boilerplate.
4. **All Cowork adjustments/approval-conditions go in INSTRUCTION FILES, never only in
   chat replies.** Chat-relayed adjustments were lost twice (2026-06-10: the H2
   extension + 326-fact rider after the hygiene pass; the chordanalyzer.h:62 comment +
   diagnose context banner after 2.3). Instruction files have a 100% delivery record.
   "Approved with additions" means: write the additions as an addendum instruction
   file, then approve.
   **"HELD" is now unambiguous (2 slips: 3.3, metric-L0L1): "held for Cowork" =
   `git add` is OK, `git commit` is NOT, until a ratification/approval file says so.
   A pre-authorized ship that may commit-on-green-proof will say exactly that.**
5. **Cowork reads every CC report IN FULL before ratifying or approving its commits.**
   Verification-against-primary-sources does not substitute for the report's Findings/
   Unknowns/caveat sections — CC under-weights its own findings in chat summaries
   (precedent: the 326/353 fact, the preset headline), and an unread caveat went
   unanswered at the Stage-3 design ratification (the bwv320 dual-classification
   question, caught only in the 2026-06-12 retrospective sweep). Chat summaries are
   navigation aids, not the artifact.

---

## Two worktrees

- `C:\s\MS` — **master** branch (main working tree — use this for all development)
- `C:\s\MS-llm-triage` — `llm-triage` branch (separate worktree, only for LLM triage work)

All active development is on **master**. Always confirm which worktree CC is in before giving it instructions.

---

## Architecture direction (decided 2026-06-09, session 4) — READ BEFORE ANY PHASE E WORK

**Single-pass, unified, no parallel paths.**

The redesign goal is a single comprehensive pass through properly layered components
where each layer passes its full evidence forward — not a multi-pass iterative loop.
The full design is in `docs/redesign_plan.md`.

Three non-negotiable principles for all Phase E work:

1. **Single commit path.** Pass 1, Pass 2 sub-region, Pass 2b sub-region, and the
   notation bridge must all flow through the same Layer 3 → Layer 4 → Layer 5 stack.
   `advanceTemporalContext` is called once, uniformly, at every commit site. The current
   manual inline assignments in Pass 2 and Pass 2b that bypass it are bugs to eliminate,
   not patterns to follow.

2. **No parallel paths, no code duplication.** Logic that exists in both the batch path
   and the notation path must be unified. `diagnoseChord` must be a view into the
   production pipeline, not a separate scorer. No new bypass paths.

3. **Resolve the `explorationMode` dual-path.** ✅ **RESOLVED — committed `e7d4ba2b1a`
   (2026-06-10).** `ChordAnalyzerPreferences` now carries `fn::ScoringPhase scoringPhase`
   (enum lives in `chordanalyzer.h`, `function` namespace — the include direction
   harmonicfunctionlayer.h → chordanalyzer.h forbids the originally planned placement);
   the 5 bonus/gate functions are stateless; the single check is `applyProgressionSignals`
   at the top of `applyHarmonicFunction`. Do not reintroduce per-function phase flags.

**What this means in practice:** do not add new gates, compensating fixes, or new
parallel scoring paths to the current feedforward pipeline. Phase E completes the
evidence picture (symmetric forward context alongside backward) and unifies the commit
paths. BIR re-calibration happens after the architecture is stable.

**MASTER PLAN (2026-06-10): `docs/implementation_roadmap.md` is the single consolidated
tracker.** Both reviews' conclusions (part 1 `cowork_target_architecture_review.md`, part 2
`cowork_implementation_review.md`) are mapped to ordered Stages 0–7 with per-stage
verification gates ("no surprises": pin/verify each layer before building on it —
Stage 0 hygiene → Stage 1 pin current behavior with tests → Stage 2 one-pipeline/one-truth
(Phase 4c move, batch parity, diagnoseChord fix) → Stage 3 decoder → Stage 4 key path →
Stage 5 weight fitting → Stage 6 functional layer). Check the traceability table there
before planning any new CC task; new work must slot into a stage.

**Architecture review (2026-06-10, session 5) — Phase E target renamed.** Full review in
`cowork_target_architecture_review.md`; adopted direction in `docs/redesign_plan.md`
"Architecture review addendum (2026-06-10)"; §2.14 reconciliation note added to
ARCHITECTURE.md. Core finding: the documented failure classes (Δ=+7a/b, gate cascades,
rcb dead ends) are all symptoms of greedy left-to-right commitment; the correct Phase E
target is **joint global decoding over a hypothesis lattice** (oracle = emissions,
progression signals = transitions, Viterbi/beam decode; key as an HMM path; weights
fitted against DCML corpora; functional labels as sequence labeling over the decoded
path). Phase E must NOT be designed as a pack of new locally-applied signals feeding the
greedy pipeline. Pending: part-2 session validating this against the as-built system
before any code direction is imposed.

---

## Current state (as of 2026-06-10, session 5)

- **HEAD:** `e7d4ba2b1a` on master (refactor: replace explorationMode flag with ScoringPhase
  enum — Phase E Step 5). Several commits ahead of origin, not pushed. Working tree dirty
  only with pre-existing uncommitted doc edits (ARCHITECTURE.md, CLAUDE.md,
  docs/redesign_plan.md + this file + STATUS.md) and the perpetually-dirty `muse` submodule
  (intentional Snap fix — never commit it).

  `e7d4ba2b1a` — explorationMode dual-path eliminated. `bool explorationMode` removed from
  `ChordAnalyzerPreferences` and from all 5 bonus/gate signatures (`wSeqBonus`, `wDimBonus`,
  `wStepInBonus`, `wStepOutBonus`, `gateRZeroesRootContinuity`) — now stateless and pure.
  Single control point: `applyProgressionSignals = (phase == ScoringPhase::Final)` at the
  top of `applyHarmonicFunction`; gates the 4 progression bonuses, Gate R, and the Pass B
  `applyStepBonusGuard` calls (Pass B needed explicit gating — pre-change it was suppressed
  only indirectly via the helpers returning 0; the guard's sole side effect is
  `cand.score += stepIn + stepOut`, so skipping the call is provably equivalent — verified
  in code by Cowork). `ScoringPhase` enum defined in `chordanalyzer.h` (`function` namespace,
  alongside the `ScoringSnapshot` forward-decl) — the instruction's `harmonicfunctionlayer.h`
  placement was backwards; CC's deviation verified correct. Two `harmonicsegmenter.cpp`
  sites (L348, L706) set `Segmentation`; sole production call site `chordanalyzer.cpp:2969`
  passes `prefs.scoringPhase`. `gater_tests.cpp` Branch 4 → end-to-end phase-gating test
  (`GateR_PhaseGated_FinalFiresSegmentationSkips`). `docs/scoring_model.md` synced in the
  same commit. 7 files, 416/416 · 52/52 · 11/11, zero snapshot diffs, no goldens refreshed;
  BIR 24/13 / 35/7 unchanged. **Verification basis: static code equivalence + zero snapshot
  diffs + BIR consistency — NOT a corpus A/B byte-diff** (report §5's "byte-identity on all
  353 scores" is an inference, not a measurement). Report:
  `cc_phase_e_exploration_mode_report.md`.

- **✅ Stage 0 COMPLETE (2026-06-10).** Commits `7bc1609159` (docs) ← `a236a0ff21`
  (hygiene: kTemplateCount six sites, dead fnCtx fields, tie-policy docs) ← `70fd8a686b`
  (tracked junk removed + gitignored; no generator — one-time redirect accidents swept
  into an old feature commit). All verified by Cowork (commit contents host-side).
  Gate 0→1 passed: 416/416 · 52/52 · 11/11, BIR 13/7 both presets. Deferred: CLAUDE.md
  "4-site atomic update" reconciliation with kTemplateCount (fold into a later doc pass).

- **✅ Stage 1a COMPLETE — `757efa5dbf`** (23 tests, composing 416→439/439; tests-only,
  production untouched; report `cc_stage1a_report.md`, verified by Cowork incl. full
  test-file read + fixture arithmetic). Findings: F1 (§2 Sus4♭5/HalfDim wording → doc
  pass list), F2+F5 (→ Stage 3 obligation list in roadmap 3.4), F3/F4 (pinned).
  Doc-pass backlog now: CLAUDE.md 4-site→kTemplateCount reconciliation + scoring_model §2
  F1 wording.

- **✅ Stage 1b COMPLETE — `6101a9b2c5`** (48 tests, composing 439→487/487; tests-only).
  Report `cc_stage1b_report.md` — definitive gate inventory + findings F1–F8. Cowork
  verified F1 (B/C/D dead code) in the production source and escalated the preset-cap
  finding: `maxTotalInversionContextBonus` has NO setter on any path and is non-binding
  at current sums (1.85 default / 0.75 Jazz) — the documented 2.5/0.6 "load-bearing"
  values exist nowhere.

- **✅ Doc pass COMPLETE — `af39f28179`** (4 files, verified by Cowork incl. CLAUDE.md
  via session context). Cap archaeology: ⛔ did NOT fire — **2.5/0.6 never set in any
  committed code** (aspirational doc-comment since `46c76ad67f`; zero `-G` assignment
  hits; the iteration plan itself prescribed the non-binding 2.0 default). Jazz
  baselines unaffected. Residual for next code-touching commit:
  `chordanalyzer.h:402–409` doc-comment still carries the 2.5/0.6 fiction + a stale
  signal list (nextRoot/consecutive/recentRoot/weakBeat).

- **✅ Stage 1c COMPLETE — `4656f43258`** (11 tests, composing 487→498/498; 9 minimal
  .mscx fixtures; composing tests can now load Scores via the engraving test env).
  Verified by Cowork (report + key tests + env file host-side). NOT-PINNED under scope
  valve (recorded as Gate 1→2 exceptions in roadmap 1.3): coalesceShortSameRootRuns,
  Pass 2/2b boundaries, sub-region bassIsStepwiseToNext. Findings G1–G5: G1 confidence
  wart pinned with real numbers (Stage-4 anchor), G2 root-agnostic absorb order-coupled
  with coalesce (Stage 3), G3 piece-start returns size-1 list, G4 sentinel confidences
  (0.0/0.5 hard-coded), G5 partial-sig correction is whole-score (Stage 4).

- **✅ Stage 1d COMPLETE — `bb48394b52` — GATE 1→2 PASSED.** 54 metric-script tests +
  hand-derived fixtures; scripts untouched; [code]/[probe] epistemic tagging honored;
  non-vacuousness mutation check. Findings F-1/F-2 (extract_quality dim-`o` miss,
  Ger65/N6/It6 mis-parses) + F-3 ("24" provenance untraced) → Stage 2.2 single
  re-baseline event. F-3 handoff wording already corrected by Cowork (BIR script note
  above).

- **✅ RESOLVED (2026-06-10): the Jazz "nondeterminism" was M3 — corpus-state
  contamination, not analysis nondeterminism.** Proven by probe (`cc_jazz_nondeterminism_report.md`):
  Jazz is deterministic 7, Baroque deterministic 13; 2 full regens, 0/353 JSON diffs —
  **C++ batch determinism proven, retroactively validating all historical A/B checks.**
  Mechanism: shared `tools/corpus` + FAILED-worker stale files (`run_bach_preset.py:113–122`)
  + `skip_cpp` reuse + no preset guard in characterise. Canonical Jazz 7-case identity
  set: {bwv244.15, 245.17, 245.40, 422, 432, 45.7, 74.8}.
  **INTERIM GATE (until 2.2a lands):** "Jazz ≤ 7" means a clean 353/353 regen yielding
  that identity set, with Baroque=13 + snapshots as co-gates — not the raw integer.

- **✅ Stage 2.1 COMPLETE — `eeca0dea30` (rider) + `8598cbd245` (Phase 4c move,
  Option D).** Snapshots 11/11 zero diffs (decisive). `analysis/section/sectionanalyzer.{h,cpp}`;
  notation helpers shrank ~900 lines to adapter surface; cadence/pivot tests stayed in
  notation tests (include updates). Dead weight/pitch-context shims (no live caller) →
  Stage-2 cleanup list.

- **✅ Stage 2.2a COMPLETE — `e20894c75b`** (tooling; verified by Cowork: exactly 6
  files) + bookkeeping docs `6f1e3dc807`. Per-preset dirs + sha256-fingerprinted manifest validation;
  63 Python tests; Baroque 13 + Jazz 7 exact identity sets verified; contamination
  probe errors. **Interim gate RETIRED** — "Baroque ≤ 13 / Jazz ≤ 7" plain meaning
  restored (clean manifest-validated regen). Deferred: analyze_inversion_errors.py
  --corpus-dir (rides with 2.2).

- **✅ Stage 2.2-i COMPLETE — `cc_stage2_2_ab_dossier.md` (no commits, by design).**
  Headline: section-level barely changes analysis (4 genuine root changes corpus-wide,
  net-negative, all on thin gap/split slices) but surfaces ~250 per-beat disagreements
  the coarse batch regions masked — **the 13/7 gate undercounts user-visible per-beat
  root errors ~7×** (rn corroborates independently: root_agree flat, all delta in
  root_err). F-3 closed (24/13 & 35/7 = analyze_inversion_errors three-way split).
  **DECISION (Cowork+user): gate stays batch-granularity**; granularity-robust metric
  now MANDATORY at Stage 5; 2.4 scope grew (Pass-0 prefs divergence + section-layer
  `inferGapRegion` default-prefs preset leak = likely cause of the 3 regressions).

- **⚠ CORPUS AUDIT (Cowork, 2026-06-10): `cowork_corpus_audit.md`.** Highest findings:
  **C1 — the snapshot gate's 11 source scores live in gitignored, revision-UNPINNED
  external clones** (`tools/dcml/*/MS3`; REPRODUCIBILITY clones at floating HEAD) — the
  byte-identity gate rests on files with no recorded identity; **C2 — the music21
  version that generated the 353 gate-corpus `.music21.json` is recorded nowhere**;
  C3 — 353-vs-361-vs-410 chorale filter provenance undocumented; C4 — stale flat
  `.ours.json` + empty accident dirs + `src/composing/tests/scores/` (7 files incl.
  `xxxxx.mxl`) referenced by NOTHING + `score_inventory.md` badly stale; C5 — ~850
  human-annotated scores unused (Stage-5 opportunity, noted in roadmap 5.2).
  Ground-truth verdict (sharpened by user mandate 2026-06-10): **the ONLY ground truth
  is the human annotation (WiR/DCML); music21 is NOT ground truth** — it is an
  algorithmic noise filter, and the 13/7 "genuine" counts are a music21-filtered LOWER
  BOUND on human-adjudicated errors (cases where music21 sides with us against DCML are
  excluded by an algorithm's opinion). Never describe the gate as "ground-truth
  agreement." Stage 5 must evaluate a DCML-only gate variant (roadmap 5.2). No
  self-annotations in any gate; catalog/goldens correctly used as regression pins only.
  Remediation = one hygiene instruction after 2.2-ii (see audit Disposition table).

- **✅ Stage 2.2-ii SHIPPED — `75a5815960`/`c7aeb24ae1`/`465450bf49`/`9e52147b04`**
  (verified by Cowork: cumulative diff exactly 8 files; F-1 at compare_rn.py:181,
  It6 routing in split_rn, shims gone; gate-neutral: 13&24/13, 7&35/7 exact identity
  sets, 65/65 Python). **Stage 2.2 COMPLETE** (2.2a + 2.2-i + 2.2-ii).

- **✅ Corpus hygiene COMPLETE — `a934574820`/`dd8a898015`/`3d8981bb57`/`0520a2dda2`**
  (verified by Cowork). Sources pinned (manifest + drift test + REPRODUCIBILITY commits;
  ABC clone DIRTY recorded verbatim; licenses: CC BY-NC-SA or no-LICENSE → in-tree
  copies NOT GPL-compatible, hash-pin is the mechanism). music21 ESTABLISHED v.9.9.1
  (embedded `<software>` tags; export chain incl. MuseScore 2.1.0). 410→353 filter
  recovered (`_is_bach_chorale`); 361↔353 diff non-computable (Riemenschneider vs BWV,
  evidenced); 352→353 +1 unknown (logged). Flat .ours.json + accident dirs deleted
  (disk-only); dead test scores removed (`3d8981bb57`). **KEY FACT: only 326/353 gate
  chorales have WiR human annotations — gate = human-adjudicated 326, music21-filtered,
  batch granularity (all three qualifiers in roadmap 5.2).**
  **Two approved adjustments MISSED the commit set (relay gap) — ride with the next
  instruction:** (a) `analyze_inversion_errors.py` no-arg default → `tools/corpus/baroque`
  + BUILD_AND_TEST §4 legacy line repoint (the no-arg path now errors); (b) the 326/353
  WiR-coverage fact into `score_inventory.md`.

- **✅ Stage 2.3 COMPLETE — `18dc9e1829` (diagnose replays production; kDiagTemplates +
  contextualBonuses removed; agreement invariant + Δ=+7b Gate-R dump tests; composing
  501/501) + `001b15df2d` (hygiene riders).** Verified by Cowork. Two approved
  additions missed the commits (relay gap #2 — see trust-model rule 4):
  addendum SHIPPED `fb8b980948` (comment fixes + conditional JSON "context"
  banner — NONE on the batch path, real context summary when threaded; verified).

- **Doc-staleness riders for the NEXT instruction (CC flagged, out of its scope;
  confirmed by Cowork):** CLAUDE.md:159/166 still lists kDiagTemplates as a template
  sync site (stale post-2.3); ARCHITECTURE.md:861 references the removed
  `contextualBonuses()`; layer_architecture_audit.md:84–92 carries a now-moot
  "Action for CC" item. Historical iteration records stay untouched (revisionism).
  Also: accumulated uncommitted bookkeeping (STATUS/handoff/roadmap) needs its
  periodic docs commit.

- **✅ Stage 2.4 COMPLETE — V1 `140ceb1a9e` / V2 `1a08e96d8a` / V4 `6be2b30a96`**
  (+ bookkeeping `4e91e3aa4c`). Decisions in ARCHITECTURE.md; D-PASS0 headline:
  chord-scoring presets are batch-only, live product = struct defaults matching NO
  preset; V4 measured the user config: **BIR=false 14 = Baroque-13 ∪ {bwv187.7}** —
  Baroque gate ≈ user reality (slightly conservative); Jazz-7 contains 2 preset-only
  artifacts (bwv244.15, bwv74.8); bwv187.7 = first user-experienced error outside all
  gates (mode-prior-surfaced; candidate Stage-3 acceptance case). App mode priors =
  bespoke set (11/21 diverge from all presets). D-GAP causal hypothesis falsified
  (structural); leak fixed anyway (live under Jazz). OPEN: Python-count reconciliation
  (68 → "67+2"), rides with 2.5.

- **✅ Stage 2.5 COMPLETE — P1 `3aa9db7676` (harness as DISABLED_ test in
  pipeline_snapshot_tests + `docs/perf_p3_baseline.md`) / P2 `c37b98321b`.** Numbers:
  P3 per-query median 33–215 ms, p95 up to 2.75 s, max 7 s (Mozart-scale); Pass-0 ≈
  99% of cost; P4 fallback 0/2231 (closes the 2.4 §1.3 unknown for loadable scores);
  budget: beam-1 p95 ≤ observed ×1.10. Python-count reconciled: 70 total = 67 metric
  + 3 snapshot-source tests; no bug, reporting-scope artifact (quote the two-file
  total henceforth). **KEY STAGE-3 INPUT: "decode once, query many" — the lattice
  makes P3 a lookup, fixing its tail AND the D-P4/D-BRIDGE cold-context contracts
  (roadmap 3.1 updated).**

- **🏁 STAGE 2 COMPLETE (2026-06-12).** All items: 2.1 Phase 4c move · 2.2a corpus
  hardening · 2.2-i A/B dossier · 2.2-ii package · corpus hygiene (audit C1–C4) ·
  2.3 diagnose production view + addendum · 2.3b queued · 2.4 divergence decisions +
  V4 user-config measurement · 2.5 perf baseline. One pipeline, one truth: gates
  pinned to identified bytes, metrics tested, user config measured
  (Default-14 = Baroque-13 ∪ {bwv187.7}), divergences decided in ARCHITECTURE.md,
  diagnostics trustworthy, perf envelope stated.

- **Stage 3 design draft REVIEWED (2026-06-12).** Verdict: ratified subject to ONE
  mandatory correction — the draft's `completeTriadInversionBonus` "region-local,
  pull from 3.3 bundle" claim is WRONG (Cowork verified `chordanalyzer.cpp:1613–1622`:
  the call-site gate is `bassIsStepwiseFromPrevious || bassIsStepwiseToNext` — the
  audit's "temporal" classification stands; CC read the qualifier and missed the
  call-site guard). All seven §13 Open Questions decided per recommendations
  (Q3 notably: identity-mutating gates retire BEFORE beam widens past them; Q7:
  decode-once = 3.1b after the byte-identity gate). Ratification addendum:
  `cc_instruction_stage3_design_ratification.md` (incl. a §correction-4 sweep:
  re-verify the other four signals' call-site guards for the same error class).

- **✅ Stage 3 design RATIFIED + COMMITTED `e2bdef7e13`** (correction applied:
  completeTriad = edge-gated emission, all FIVE signals migrate at 3.3; sweep clean —
  no second qualifier-vs-guard error; Q1–Q7 decided; hash-stamping deviation accepted).

- **📋 Full-report retrospective sweep (2026-06-12, trust-model rule 5 backfill) —
  doc-rider queue for the next docs-touching instruction:**
  1. **The Baroque-13 identity set is pinned in NO committed doc** (only Jazz-7 is; the
     full set with ticks exists only in gitignored cc_ reports — 2.2-ii §4:
     bwv102.7@17520, bwv14.5@8160, bwv17.7@46080, bwv174.5@6240, bwv245.17@4800,
     bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960, bwv381@4800,
     bwv422@23040, bwv432@5520, bwv45.7@20160). Commit it next to the Jazz set.
  2. The music21 **freeze anchor** prose lives only in gitignored
     `tools/corpus/README.md` (hygiene §3); replicate into committed REPRODUCIBILITY.md.
  3. 2.1's proposed ARCHITECTURE.md file-map sentence (sectionanalyzer location +
     Pass-0 injection contract) was never applied — verify and add.
  4. Frozen iterNN diagnostics lost their flat `.ours.json` inputs in the hygiene
     deletion (2.2a kept them partly FOR those scripts; the hygiene reader survey
     omitted them). Fail-loud if re-run — acceptable; recorded, no action.
  Parked: 2.1 §5.6 unused includes in trimmed helpers; Stage-1d NOT-PINNED WiR
  discovery plumbing (partially compensated by the snapshot-sources manifest).

- **✅ Stage 3.1 COMPLETE — `8e4bb4902d`** (7 files, +506/−28; report read in full by
  Cowork per rule 5; commit verified). The beam-1 decoder owns the commit chain at all
  three sites behind `decodeQualityLevel` (default FastBeam1). Byte-identity: 0/353 ×
  3 configs + empty `git diff tools/corpus` (manifest fingerprints = second proof);
  snapshots 11/11; composing 505; BIR sets exact ×3; perf within ×1.10; zero design
  deviations. Key structural fact: the decoder computes no score — FP-sensitive
  arithmetic untouched in `applyHarmonicFunction`.

- **⚠ 3.1b STOPPED CORRECTLY by CC (2026-06-12), Q1 RE-DECIDED.** The whole-score cache
  worked (warm ~0.0006 ms) but: (1) Cowork's instruction premise was wrong — the
  snapshot harness flows through the orchestrator, so snapshots went 0/11 (CC did NOT
  refresh — correct); (2) the answer-delta A/B FALSIFIED the design's whole-score
  prior: 32–40% tick changes on contrapuntal scores, DCML 59/41 in the WINDOW path's
  favor (Mozart 35/65 against whole-score). **This is the 2.2-i granularity finding
  recurring** — fine windows are more per-tick DCML-accurate; coarse whole-score is
  self-consistent. **Decision (Cowork): bounded-window cache (CC's recommendation);
  whole-score SHELVED with evidence; P3↔P1 consistency PARKED as a product/Stage-5
  question; D-P4/D-BRIDGE closure rolled back to the 2.4 contract; the A/B data
  promoted to committed Stage-5 evidence.** Revision instruction:
  `cc_instruction_stage3_1b_revision.md`.

- **✅ Stage 3.1b COMPLETE — B1′ `947519b2b6` + B2 `4f1754c26c`** (both verified).
  Bounded-window cache (memoized pure per-window section build; byte-identical by
  construction: snapshots 11/11 no-refresh, always-on equality test, AnswerDelta=0);
  warm re-click ~0.003 ms; pointer-reuse hazard closed pre-commit via
  `Notation::setScore()` lifecycle flush (no per-lifetime Score id exists —
  investigated; flush-before-install = no false-hit window). Whole-score variant
  SHELVED with evidence (`docs/p3_granularity_ab_3_1b.md`, Stage-5 input);
  Q1 re-decided; D-P4/D-BRIDGE rolled back to 2.4 contract (design §8 amendment).
  Full record: `cc_stage3_1b_report.md` §1–§6 (whole-score measurement) + §R
  (binding outcome) — read in full by Cowork.

- **3.3 Task-1 STOP resolved (2026-06-12): Gate R = reconstructed-credit
  (`fullBasisDep = cell.basisDep + cappedInv ≤ 0`).** CC's derivation proved the
  ratified pcWeight mechanism text WRONG (old Gate R fires ⟺ `cappedInv==0`; Dim's
  inversion credit includes a temporal gate no pure-vertical rule reproduces) —
  mechanism superseded as falsified-by-derivation (Method F); the reconstructed-credit
  form is the faithful execution of the ratified INTENT and closes Finding 6 fully
  intra-layer. The basisIndep ≤1-ULP reassociation: primary approach accepted; ANY
  A/B diff ⇒ switch to the pre-approved bit-identical fallback (expose `d`), no
  case-by-case reconciliation. Decision file: `cc_instruction_stage3_3_gater_decision.md`.

- **✅ Stage 3.3 COMPLETE — `548adb7b2e` (RATIFIED POST-HOC).** All five signals
  migrated (oracle now genuinely vertical — audit Finding 1 CLEARED); Gate R =
  reconstructed-credit (`fullBasisDep ≤ 0`, intra-layer — Finding 6 CLEARED); byte-
  identity 0/353×3 + snapshots 11/11 + all suites + identity sets ×3 + canaries
  unmodified; **re-pin ledger EMPTY** (defaulted cell flags — strongest outcome).
  basisIndep ≤1-ULP primary shipped, fallback unneeded (A/B zero diffs).
  ⚠ Process note: the commit was made BEFORE ratification despite "held" — content
  fully verified and ratified post-hoc, but "held" means held (do not repeat).
  Cleanup queued for 3.4: the retained 2-arg `gateRZeroesRootContinuity` test-compat
  overload (semantics subtly non-production) dies when Gate R is absorbed into the
  rcb edge.

- **✅ Stage 3.4-i COMPLETE — Ship #1 `da1b440845` (B/C/D removed) + Ship #2
  `a652dc1ba7` (Gate R → `rcbEdge()`, overload dropped); both 0/353×3 byte-identical.**
  Dossier `cc_stage3_4i_dossier.md` read in full (rule 5). **Reframing facts: gate
  retirement is BIR-free on Default (user config); ALL BIR movement is Jazz-only;
  A/E/F/G-family/H run only under Baroque. 3.2 risk concentrates in Gate I (5 Jazz fixes
  + Δ=+7b coupling).** Classes: C1 retire-now (E/F/K/Iter86) · C2 3.2-acceptance
  (I/bias/L/H/Iter91) · C4 defer (A/G-family) · C5 keeper (J, BIR-blind, fires huge).
  F4/F6/F8 re-decide inventory done (paper) — fixes carried by the owning gate's
  retirement, never silent.

- **✅ Stage 3.4-ii COMPLETE — ZERO gates retired (no commit; tree clean at `a652dc1ba7`).**
  The non-chorale spot-check + byte-level proof gate FALSIFIED all four C1 "dead"
  verdicts: K + Iter-86 change winners on non-chorale repertoire (Chopin op24-4,
  Mozart K310-1 — never truly C1 → C2 acceptance); E + F change only alternatives
  lists, winner-neutral, so NOT byte-identical to remove → C2′ alternatives-hygiene
  (the decoder's Q5 output-assembly subsumes them for free). CC implemented E-removal,
  hit the 2-Baroque-chorale sha256 diff (bwv245.3, bwv336), and reverted per the stop
  condition — exemplary. **Methodology correction (my instrument, not CC): 3.4-i §3's
  winner-region metric is BLIND to winner-neutral alternatives-list changes; the
  `.ours.json` sha256 is the authoritative deadness test.** DCML 3.2 inputs: Iter-86's
  fire is DCML-CORRECT (reproduce), K's is root-worse on chromatic-romantic
  (mis-fire — do NOT import). The C1 retire-now menu is empty; no identity-mutating
  gate was removed from the beam path. **Decision: E/F NOT retired now** — they fold
  into the decoder's alternatives-ordering at 3.5/output-assembly, not a standalone
  non-byte-identical re-decide.

- **⚠ STRATEGIC PIVOT (2026-06-13, Cowork-verified + user-directed): beam-widening
  SHELVED; the back half of the roadmap is being re-grounded on measured precision
  headroom.** The 3.2 design's §3 derivation (Cowork-verified against the independent
  June-9 redesign_plan numbers — AbMaj7 2.55>2.33, F#7 2.85>2.825, the rcb>margin
  arithmetic) proved **a wider beam does NOT fix Δ=+7a**: the transient is the
  HIGHEST-scoring node (locally correct, DCML root absent from its tones), so the
  continued-root wrong path is the genuine global optimum a decode finds exactly as
  greedy does. Re-ranking can't fix it; only re-weighting (Stage 5) or joint
  segmentation can. **Deeper consequence (Cowork): beam>1 is beam-1-substitutable for
  ALL currently-motivated work** — gate-folding and edge-reweighting are beam-1 ops, and
  beam>1 is BIR-free on Default — so its only justification was Δ=+7a, now void.
  decoder_design §11's "low-scoring transient" was a ratification miss (mine). User
  directive: *investigations first; long-term; major redesign OK; minimum surprises;
  maximum precision.* → **don't build beam speculatively; investigate where precision
  actually lives first.** `docs/beam_widening_design.md` SHELVED (retained for its §3
  derivation). decoder_design §11 Δ=+7a row needs erratum (next doc pass).
  **[UPDATE 2026-06-13 — APPLIED.** The decoder_design §11 erratum is now in the file
  (ERRATUM block at the top of §11), applied during the foundations-verification run
  (`cc_foundations_verification_report.md`, Task 6). The trailing "still queued" mentions
  in older dated entries below are historical; this ledger item is CLOSED.**]**

- **✅ Precision-headroom investigation COMPLETE — `cc_precision_headroom_dossier.md`
  (Cowork-verified).** Re-grounding facts: 95.2% of root errors are functional not
  vertical (`root_err 2706 = all_differ 2576 + m21-fixable 130` — structurally exact;
  the music21 gate sees only the 4.8%); key_disagree (27.9%, largest) = 63% tonicization
  label-gap (Stage 6, S1=17.7%, low-risk pure-add on correct readings) / 37% key error
  (Stage 4); headroom ≈ Stage 6 35–42% · Stage 4 20–24% · Stage 5 1.3%-batch (the
  fitter) · search ≈ 0. Verified: the identity is structural; the tooling reproduced the
  documented A3 27.6%/15.4%/6.3% baseline (proves it's real machinery). Recorded in
  roadmap (PRECISION-HEADROOM RE-GROUNDING block).

- **✅ Metric-design investigation COMPLETE + RATIFIED — `docs/precision_metric_design.md`
  (DRAFT; read in full + load-bearing probe verified against source by Cowork).** Key
  findings: `compare_rn` IS the DCML-only metric (reuse, not rebuild); `classify_pair`
  ALREADY credits a correctly-emitted secondary as `exact` — so the functional-axis gap
  is EMISSION (Stage 6), not the comparator; the granularity-robust unit = union-of-
  boundaries duration-weighted grid (segmentation-invariant by construction, kills the
  2.2-i ~7× artifact AND dissolves the deferred Default-section regen); the chicken-and-
  egg resolves via the L0–L4 ladder + a label-vocabulary contract that is a Stage-6
  output-spec co-ratified with the metric. Ratified: OQ-G1 → union-of-boundaries.
  Deferred to Stage-4/6 co-design: OQ-L1 (cadence token — genuine Stage-6 fork),
  OQ-L2 (secondary normalization), OQ-C1 (held-out split). OQ-V1 already on C2 list.

- **✅ L0–L1 metric primitives BUILT — `f8c6b3932a`** (tools-only; verified by Cowork:
  2 files, no C++, invariance test present + passes, dossier numbers reproduced via
  committed modes). `--wir-bach` (326/353), `--granularity-robust` (segmentation-
  invariant; swing 6.8pp→0.8pp), `--key-breakdown` (S1/S2 63/37). 70 metric tests
  unchanged + 21 new. The back half is now measurable.

- **✅ Stage 4 design investigation COMPLETE — `docs/key_path_design.md` (HELD, staged
  not committed — convention honored).** §3 finding (Cowork-verified: S2=1032 reproduces;
  bwv244.54 anchor rests on serialized runnerUp; logic airtight): **the key path fixes
  only ~10% of S2** (Class A spurious-flip); ~85% is Class B (emission prefers wrong key,
  correct key never rank-2 in 51.6% of S2) — unrecoverable by any path. **SECOND
  falsified structural fix → META-PRINCIPLE recorded in roadmap: precision lives in
  emission + functional labeling, NOT search/path.** The HMM path is the least valuable
  part of Stage 4 (~10%); KeyArea spans + the key-EMISSION fix are what deliver.
  **Decision (user): investigate the key-emission headroom before shaping Stage 4.**
  HMM path deferred under the beam-style "revisit when search genuinely matters" trigger.

- **✅ Key-emission headroom dossier COMPLETE — `cc_key_emission_headroom_dossier.md`;
  instrument committed `a4ae4a9203` (read-only key-candidate dump, byte-identity 0/353,
  verified by Cowork: 5 files, dump struct present).** **Result that INFORMS A-vs-B
  (verified — term-level dump evidence):** the Class-B key bulk is NOT a scorer ceiling.
  It splits at the declared-mode fault line: 349 restorable (mode DROPPED at MuseScore
  import for empty key signatures → `declaredModeOrdinal=-1`; xml carries `<mode>`), +
  a partial-sig subset (≈34–44% of S2 STRUCTURAL, one import fix); small FITTED
  (Stage-5 prior balance); ~127 CEILING = notation-vs-analyst CONVENTION disagreement
  (resolver faithfully follows the notated key; WiR picked the relative — arguably
  correct-behavior-penalized). **The biggest lever is a dropped-XML-tag plumbing bug,
  not a limit of hand-built analysis → strong evidence the hand-built emission has large
  concrete headroom (A), Level-2/learned NOT triggered on the key axis.** Stage-4 shape
  (scoped, not built): declared-mode import fix + GRADED declared prior (not the −7 wall)
  + KeyArea + hysteresis→path; HMM/search deferred. Caveat (§5.1): import root-site not
  read; fix robust either way.

- **✅ BACK-HALF RE-GROUNDING drafted — `docs/back_half_design.md` (DRAFT, NOT YET
  RATIFIABLE).** Resolves A-vs-B → A (hand-built) confirmed, B (learned) kept as
  triggered-fallback, on the key-emission evidence (faults are specific structural
  causes, not ceilings). Re-grounded order: metric(done) → Stage 4 (key import fix +
  graded prior + KeyArea) → Stage 6 (functional layer, largest lever; scope-cause first
  = the B-fallback check) → Stage 5 (fit last). Search deferred.

- **⚠ RATIFICATION GATED ON FOUNDATIONS VERIFICATION (user mandate 2026-06-13: facts
  first, never assume, old truths may be stale).** The re-grounding's KEYSTONE — the
  declared-mode-drop root cause — was unverified at source (CC's own §5.1), and it
  carries stale (non-Bach cross-corpus, June-3 pre-F1) + unrecorded (music21 version)
  facts. Ratifying now would violate the double-check mandate.

- **✅ Foundations verification COMPLETE — `cc_foundations_verification_report.md`; GATE
  GREEN.** Keystone CONFIRMED at source (Cowork independently re-read `addKey:5978`); 79/80
  zero-sig stems recoverable → 349 lever stands; bwv62.6 = same mechanism. Byte-identity
  re-confirmed (0/353). key→basisIndep current. music21 v9.9.1 already recorded. Cross-corpus
  "~2× harder" CONFIRMED by HEAD regen (50.7%/27.4%, 62110 regions). Four corrections folded
  into `docs/back_half_design.md` (keystone precision = default-key-match not 0-fifths;
  cross-corpus binary-stale not metric-stale; composing engraving-coupled / fix reaches both
  callers / favor option-b engraving-retains-mode; §11 erratum). §11 Δ=+7a erratum staged in
  `decoder_design.md` — **Cowork authorized committing it alone** (hash pending CC).
  Remaining qualifier (Stage-4-build confirm, not a blocker): native `.mscz` vs MusicXML-import
  mode-drop → "user-facing" vs "corpus-measurement" framing of the 349.
  **`docs/back_half_design.md` is now FOUNDATIONS-VERIFIED & RATIFIABLE** (status header
  lifted). §11 erratum committed `bcd4319aa7`. OQ-2/3/4 settled; **OQ-1 (A-vs-B) HELD
  pending the functional-residual investigation** (user 2026-06-13: settle the biggest
  call on evidence, not inference — "A confirmed" is proven on the key axis but only
  inferred on the largest slice).

- **🛑 GROUND-TRUTH PARSER BUG (2026-06-13, CC-spotted mid-investigation,
  Cowork-verified at source `dcml_parser.py:386`): the WiR/rntxt parser computes inline
  applied-chord (`V/V`, `viio6/V`, `V/III`…) root_pc from the PRIMARY numeral against the
  LOCAL key, discarding the applied target — wrong DCML root for every secondary on the
  ENTIRE Bach gate set (326/353).** Our analyzer/music21 resolve applied roots correctly →
  falsely flagged root_err. CONTAMINATES the DCML-only headroom (the 2576 "neither" /
  95%-functional), likely the metric-design "secondaries credited" finding (synthetic-probe
  artifact — real data: our correct root ≠ parser's wrong root), and the paused
  functional-residual classification. **Irony: the music21 filter we dropped was shielding
  the BIR 13/7 gate from this (filter excludes parser-wrong/we-right cases) — so the gate
  is probably clean, the UNFILTERED numbers are polluted.** TSV/non-Bach path is correct
  (uses `relativeroot`). **FUNCTIONAL-RESIDUAL INVESTIGATION + OQ-1 RATIFICATION HALTED
  until the parser is fixed and the numbers re-measured.** This is the user's
  "can-we-trust-the-corpora" risk, realized — the investigation-first/sample-real-cases
  discipline surfaced it before it was built on.

- **⏸ HELD (do NOT dispatch yet) — DCML applied-root fix:**
  `cc_instruction_dcml_parser_applied_root_fix.md`. Superseded as the immediate next step
  by the full pipeline audit below (user 2026-06-13: don't fix the one bug CC tripped
  over — find ALL measurement-error sources first, fix as ONE coordinated re-baseline).
  This fix becomes one line item in the audit's elimination plan.

- **✅ Functional-residual dossier COMPLETE — `cc_functional_residual_dossier.md` (read in
  full by Cowork; both parser bugs re-verified at source).** It primarily produced MORE
  measurement-bug evidence (vindicating the audit): a SECOND confirmed parser bug
  (minor-leading-tone `viio`, `_DEGREE_SEMITONES_MINOR:77` VII=+10 vs true +11, hits BOTH
  rntxt AND TSV paths), a Bach artifact rate (366/2576=14.2% ours-correct/parser-wrong;
  557=21.6% parser≠true), and the music21 `RomanNumeral` true-root oracle. Provisional
  OQ-1 read (A confirmed / B not triggered / <5% needs-richer; 92.1% ours==m21) **— but
  computed on CONTAMINATED ground truth, so the SIZES will shift after fixes. OQ-1 STAYS
  FROZEN; its qualitative direction is likely robust but unconfirmed on clean data.**
  Findings MERGED into the audit instruction (PRIOR EVIDENCE block).

- **✅ MEASUREMENT-PIPELINE AUDIT COMPLETE — `cc_measurement_pipeline_audit.md`
  (read in full; P0 verified at source by Cowork `:157`/`:178`).** FIVE defects:
  **P0 (headline, Cowork-verified)** — `float("1/2")`→ValueError→bare `except: continue`
  drops **58.9% of ALL TSV ground truth** (downbeat-only, easiest-biased) → the entire
  cross-corpus metric wrong ~8–10pp; **P1** rntxt applied-`/X`; **P2** minor-LT/vio table
  (both paths); **P3** mode-drop (S2 import, KEY axis only — does NOT corrupt root gate);
  **P4** (NEW) ABC/Beethoven repeat/numbering offset (naive qb-fix makes beethoven worse).
  **The BIR 13/7 gate is STRUCTURALLY CLEAN** (music21∩DCML double-filter excludes the
  corrupted cases — 0/13, 0/7 artifacts) → Stages 0–3 sound. ~46% of the gate is
  legitimate ambiguity; genuine actionable residual ~7 Baroque/~3 Jazz. CLEAN-confirmed:
  music21=filter-only, jazz=qualitative-only, snapshots=pins, quarterbeats origin exact,
  TSV relativeroot works, It6 refuted, repeats fine (except P4), tpb=480 stable.
  **Cowork humility note: the foundations pass "confirmed" the cross-corpus number while
  sitting on P0 — targeted verification ≠ holistic; the audit caught what the foundations
  check missed.** §4 = a coordinated one-batch re-baseline (P0→P1+P2→P3→P4→reporting).

- **EVERYTHING precision-derived FROZEN until the fix batch + re-measure:** cross-corpus
  numbers, the headroom "95% functional," the functional-residual sizes, OQ-1, the
  back-half ratification. ~~The BIR gate is the only precision-ish number that holds.~~
  **SUPERSEDED 2026-06-13 — the BIR gate moved too (see below); NOTHING precision-derived
  survives the fix batch unchanged.**

- **★ 2026-06-13 — INSULATION HYPOTHESIS FALSIFIED. The BIR gate is NOT insulated.**
  CC ran the metric re-baseline batch; the oracle-verified P1/P2 GT-parser fixes grow the
  gate **Baroque 13→57, Jazz 7→23** — STRICT SUPERSET (all 13/7 preserved, 0 lost; +44/+16
  added). Mechanism: the parser bug corrupted these chords' GT roots into the discarded
  `all_differ` (parser≠music21) bucket, hiding them from the gate as FALSE NEGATIVES. With
  correct roots they surface as genuine candidate cases. The +44 are exactly the P1/P2
  categories (viio7/V ×19, other viio*, half-dim, applied). The audit §3.A "0 parser
  artifacts" was right about the 13 PRESENT but missed the ~44+16 HIDDEN. **Cowork verified
  the fix at source** (dcml_parser.py `_compute_root_pc`:143-156 + `_resolve_dcml_key`:325 —
  case-disambiguated lowercase vi/vii→+9/+11, oracle-cited; P0 `_parse_fraction`:168 present;
  diff tools-only). Re-baseline: GT volume 37,886→90,851 (×2.40, P0 confirmed); per-ours
  root_agree 49.3%→64.2%; per-DCML 54.4%→50.3% (P4 recovers beethoven 48.2%→60.3% so the
  drop is −4.1pp not the audit's −7.7pp).

- **Caveats CC flagged (both real):** (1) like the original 13 (~46% judged legitimate
  ambiguity), some fraction of the +44/+16 will be ambiguity too — 57/23 is the GATE
  (candidate) count, not 57 genuine errors; the genuine subset needs characterization.
  (2) P2 is shared TSV+rntxt code, so the rntxt gate effect can't be separated from the
  TSV minor-LT correction the cross-corpus re-baseline needs (→ Option 3 "revert rntxt
  only" is not cleanly separable AND would discard a correct fix — REJECTED).

- **DECISION (Cowork, 2026-06-13): Option 2 — report only, no re-pin, no commit.** Told CC:
  reject Option 3 (revert = preserving a known-artifact number over the truth, the exact
  trap the audit exists to kill); don't take Option 1 yet (re-pinning tests + rewriting the
  CLAUDE.md 13/7 identity sets + the "hard-stop" policy is a FOUNDATIONAL ratification = the
  user's explicit call, not a tools-batch side effect). CC to: finish P5, write the full
  `cc_metric_rebaseline_report.md` incl. the gate finding, ENUMERATE the +44/+16 with
  stem@tick identities + category, give a first-pass genuine-vs-ambiguity triage; keep
  ALL staged + HELD; touch NEITHER the metric tests NOR CLAUDE.md/STATUS.md gate identities.

- **Cowork verification done (2026-06-13, Windows-side + git objects):** P2 fix CONFIRMED
  correct at source (dcml_parser `_compute_root_pc`:152-156 case-disambiguated +9/+11, both
  paths). Corpus HEAD-stable: only docs + byte-identical key-diagnostic `a4ea` + tools-metric
  `f8c6` between the stamp `a652dc1ba7` and HEAD → `.ours.json` valid at HEAD. Re-baseline
  coherent. **Substantive caveat that stands:** the triage's "~10 actionable" leans on the
  SOFT viio↔V7 share-tone bucket (~29 Baroque); the dim7-rotation bucket (Δ∈{3,6,9}) is solid
  (symmetric dim7 = genuinely root-ambiguous), but the share-tone bucket needs a hand-trace
  before the actionable count is trustworthy. CC itself flagged this.

- **⚠ SANDBOX NOTE (this session only):** Cowork's Linux bash mount was DEGRADED — it served
  NUL-padded copies of src files + a truncated `characterise_bir_false.py` that are
  DEMONSTRABLY FINE on the real disk (Windows-side Read showed chordanalyzer.cpp clean;
  CC's "tools-only, 3 files" is accurate). Lesson: this session's bash cannot be trusted for
  working-tree-file verification — use the Windows-side file tools / committed git objects, or
  have CC verify. The false-alarm was caught before surfacing. (NOT a real repo problem.)

- **DECISION (user, 2026-06-13): "Verify, then ratify."** Instruction DISPATCHED:
  `cc_instruction_gate_rebaseline_verify.md`. CC to (1) reproduce 57/23 via the CANONICAL
  `characterise_bir_false.py` at HEAD (regenerate both corpora; confirm strict-superset, 0
  lost) — because CC's original 57/23 came from a throwaway `/tmp/gate_ids.py` driver against
  the 3-commits-behind corpus; (2) hand-trace the soft viio↔V7 bucket (oracle-checked) to firm
  the actionable count. READ-ONLY + corpus regen; metric fixes stay STAGED/HELD, no commit,
  CLAUDE.md/STATUS.md UNTOUCHED.

- **VERIFY REPORT LANDED + Cowork-reviewed in full (2026-06-13):**
  `cc_gate_rebaseline_verify_report.md`. Verdict: **57/23 verified + ratifiable.** (1)
  Canonical `characterise_bir_false.py` reproduces 57/23 at HEAD (corpus regen 353/353,
  manifest `bcd4319aa7`) — no driver-vs-canonical gap. (2) Strict-superset PROVEN through the
  canonical tool: reverted parser to HEAD blobs → exactly 13/7 (the CLAUDE.md sets), restored
  (byte-identical), `comm -23` empty → 0 lost both presets. (3) 80/80 contested roots
  oracle-correct (100%). (4) My soft-bucket caveat RESOLVED FAVORABLY: ~18 of the report's
  "soft viio↔V7" are actually symmetric-dim7 (rootless-V7♭9 label, but {r,r+3,r+6,r+9} sounds
  → pitch-class unresolvable); only 11 genuinely soft, ALL traced to legitimate ambiguity
  (oracle, GT root present, ≥3 shared). Sonority-based unresolvable = 30/57 Baroque (53%), not
  the report's 12. (5) Actionable held/nudged DOWN: bwv227.7 reclassified genuine→segmentation;
  net ~9–10 Baroque / ~4 Jazz. No stop-condition triggered.

- **★ GATE-SECTION GAP I caught before rewriting:** CLAUDE.md line 108 has a THIRD config —
  **Default (user-run) = 14 = Baroque-13 ∪ {bwv187.7}** — which CC did NOT re-measure and is
  stale under the corrected parser. Rather than enshrine 57/23 next to a known-wrong Default-14
  (internally inconsistent doc → would mislead CC), DISPATCHED `cc_instruction_gate_default_measure.md`:
  measure NEW Default via canonical tool (OLD-14 reproduce + strict-superset + oracle-check the
  additions). Same READ-ONLY+regen / HELD / no-doc-edit regime.

- **✅ DEFAULT MEASURED + GATE RATIFIED (2026-06-13).** CC measured Default 14→57 (canonical
  tool, OLD-14 reproduced via A/B, strict superset 0 lost, 42/43 additions = the vetted
  Baroque set, 1 Default-specific = bwv227.7@18000 segmentation variant, oracle-correct).
  Verify report §5 has the full Default-57 set. **Cowork did the coherent gate-section rewrite:**
  - **CLAUDE.md** gate-identity block rewritten to the full **Baroque 57 / Jazz 23 / Default 57**
    `stem@tick` sets + the re-baseline provenance note (undercount cause, strict superset,
    100% oracle, ~95% ambiguity, symmetric-dim7 two-tier seed); the two stale "13/7" refs
    (granularity caveat + analyze_inversion note) updated; `analyze_inversion_errors` 24/13,
    35/7 explicitly marked stale/pending (NOT re-measured under the corrected parser).
  - **STATUS.md** new top entry documents the metric re-baseline + 57/23/57 gate, STAGED/HELD.
  - **Cowork cross-validated all three sets**: Baroque-57 derived two independent ways
    (Default-57 minus CC's delta; and old-13 ∪ +44 enumeration) — agree exactly. Jazz 7+16=23.
  - Sets are **staged for the USER to commit + push** (user: "i can push myself"). Nothing committed.

- **✅ DOC-RIDER DONE — living-doc gate-number sweep (2026-06-13).** All LIVING docs updated to
  57/23/57 (current-state claims fixed; historical "✅ DONE @commit — Baroque 13" / "Stage-3
  gate" records left intact + annotated with a re-baseline pointer so they're not falsified):
  **CLAUDE.md** (gate section, full sets), **STATUS.md** (new top entry), **ARCHITECTURE.md**
  (Stage-2.4 V4 finding + re-baseline note), **build_and_test.md** (gate identities + the
  analyze_inversion `# 24/13` command annotations → stale/pending), **docs/implementation_roadmap.md**
  (baseline-regime line), **docs/back_half_design.md** (Stage-4 verification gate → 57/23/57),
  **docs/score_inventory.md** (4 refs + the "not an absolute quality figure" framing extended
  with the ~95%-ambiguity + 4th pitch-class-resolvable qualifier), **docs/decoder_design.md**
  (banner + eval + targets table), **docs/beam_widening_design.md** (banner; also notes beam
  shelved). `docs/scoring_model.md` / `redesign_plan.md` / `layer_architecture_audit.md` have NO
  gate-count refs (verified). The ~50 historical cc_*.md / cowork_*.md reports left as-is (record).
  The `analyze_inversion_errors` 24/13·35/7 secondary split is consistently marked stale/pending
  everywhere. All staged for the USER's commit.

- **Next CC instruction READY (updated 2026-06-13): `cc_instruction_functional_residual_investigation.md`.**
  Was BLOCKED pending the parser fix; now UNBLOCKED + rewritten for the corrected metric. Key
  update: its old numbers (root_err 2706 / all_differ 2576 / 95.2% functional / S1 1791 / the
  headroom dossier) were computed on the BUGGY parser and are INVALID, so a **new Task 0**
  re-derives the headroom decomposition on the corrected metric FIRST (NEW-vs-OLD root_err
  split + corrected functional-vs-vertical % + S1 recount + a rider re-measuring
  `analyze_inversion_errors` 24/13·35/7 → corrected), and Tasks 1–4 retarget to the corrected
  residual; gate refs → 57/23/57; mandatory reads point to the rebaseline+verify reports
  (old dossier = METHOD-only, numbers stale); deliverable OVERWRITES the stale
  `cc_functional_residual_dossier.md` (its provisional "OQ-1=A" was on the buggy metric). This
  single instruction now folds in handoff-TODO items (2) analyze_inversion re-measure +
  (3) the frozen precision re-derivations, and gates OQ-1. READ-ONLY, no commit.

- **✅ DOSSIER LANDED + OQ-1 RATIFIED (2026-06-14).** `cc_functional_residual_dossier.md`
  re-derived on the corrected metric (Cowork read in full + verified: arithmetic consistent,
  OLD-repro validates the instrument, analyze_inversion BIR=false 57/23 independently matches
  the gate). Verdict: **A confirmed, B2=0/44, B not triggered.** Cowork caught the scope limit
  CC understated — **Bach-rntxt-ONLY**; B's literature edge is exactly the undecomposed non-Bach
  chromatic repertoire. **User ratified A, SCOPED TO BACH.** `back_half_design` §3/§5 + STATUS
  updated to RATIFIED with the Stage-5/6 re-open gate (non-Bach decomposition + ~100 sample +
  DROOT_ABSENT alignment-noise audit). Stage 4 proceeds (hand-built either fork).

- **⚠ COMMIT PREREQUISITE (CC-flagged, Cowork-endorsed):** the corrected metric (the staged
  tools fixes) MUST be committed before any Stage-5 weight fitting — else the fitter optimizes
  against 365 phantom + 75 mislabeled cases. User commits (the whole staged set: tools fixes +
  CLAUDE.md/STATUS.md/ARCHITECTURE.md/build_and_test.md + the docs/ sweep).

- **Cowork TODO next — Stage 4:** prepare the Stage-4 build instruction (declared-mode import
  fix at `importmusicxmlpass2.cpp:5978` = P3 + graded declared prior, not the −7 wall + KeyArea
  spans + hysteresis→path). **NEEDS ENGRAVING FILE-SET AUTHORIZATION** — touches
  `src/importexport/musicxml/` + `src/notation/`, OUTSIDE the composing autonomous zone
  (CLAUDE.md). Surface the file-set to the user for approval BEFORE dispatching. Scoping dossier:
  `cc_key_emission_headroom_dossier.md`. Stage-5/6 OQ-1 re-open gate is a parked follow-on.
- **Still pending the user:** commit + push the staged metric fixes + the doc updates (user:
  "i can push myself"). Nothing committed this arc.

- **Next CC task — DISPATCHED 2026-06-13: the tools-only metric re-baseline batch.**
  Decision taken (user 2026-06-13): "Tools-only metric batch now; P3 with Stage 4."
  Instruction: `cc_instruction_metric_rebaseline_batch.md`. Fixes P0 (fractional-onset
  via `Fraction` + `quarterbeats×480` alignment, keep the ~58.9% dropped annotations),
  P1 (rntxt applied `/X` resolution), P2 (minor-LT/vio degree table → viio +11), P4 (ABC
  downbeat-anchoring; QUARANTINE any movement that won't anchor cleanly rather than ship
  the naive +3.6pp-worse beethoven correction), P5 (coverage-denominator honesty +
  HEAD-aware `rerun_dcml_comparison`). ONE deliberate re-baseline + metric re-pin; HELD
  for Cowork commit (it moves every headline number). Built-in checks: BIR 13/7 UNCHANGED
  (insulation regression — moving = STOP/finding), corrected roots verified against the
  music21 `RomanNumeral` oracle, before/after re-baseline table + corrected headroom
  headline reported. **P3 mode-drop explicitly OUT — rides with the held Stage-4 engraving
  work** (ENGRAVING import change, outside the composing autonomous zone, KEY-axis only).
  The full functional-residual RE-decomposition + OQ-1 re-derivation are the SEPARATE
  follow-on on the corrected metric, not this run.
  *(Audit context, retained:)* the holistic, unprejudiced audit of ALL
  corpora, source → verdict, every stage (S1 source · S2 ours-ingestion [mode-drop lives
  here; pickup/repeats/ties HIGHEST-risk + LEAST-audited] · S3 GT-parsing [applied-root +
  the rest of dcml_parser] · S4 alignment [tick/pickup/measure-numbering — the classic
  corpus killer] · S5 comparison · S6 aggregation) × every corpus (Bach-rntxt, the 9 TSV,
  music21, jazz-no-GT, snapshot). Method: trace ≥20 flagged errors/corpus end-to-end,
  classify PIPELINE-ARTIFACT / GT-LIMITATION / GENUINE-ERROR / AMBIGUITY → the artifact
  rate per corpus = how inflated every headline number is. Output: the complete
  error-source ledger + a prioritized ONE-batch elimination plan. READ-ONLY, no fixes
  this run. **Everything downstream (functional-residual investigation, OQ-1, the
  back-half ratification, the headroom/95%-functional numbers) is FROZEN until the
  measurement chain is audited and the artifact rate is known.**

- **(BLOCKED — resumes after the parser fix) functional-residual investigation (GATES
  OQ-1):** `cc_instruction_functional_residual_investigation.md` — READ-ONLY decomposition of the
  **2576 "neither" root-err functional residual** (cadential-6-4/suspension/applied/pedal
  — where both we AND music21 miss DCML's functional root) three ways:
  RULE-REACHABLE (hand-built functional layer reaches it = A) / NEEDS-RICHER-MODEL
  (the B-trigger) / GENUINE-AMBIGUITY-or-CONVENTION (a ceiling for EVERYONE incl. B —
  sizing it bounds what any approach achieves). S1 tonicization (1791) confirmed-reachable
  separately (mechanical). Calibrated against the literature ceiling (rule-based
  Temperley/HarmAn vs neural AugmentedNet/RNBert) + an optional music21-RN probe.
  Output decides OQ-1: bucket-1+3 dominate → A confirmed; bucket-2 large → B strengthened.
  No build/commit. Then OQ-1 ratifies on evidence → the back half is locked → Stage-4 build.

- **(history) Foundations verification IN PROGRESS (Task 2 cross-corpus regen running):**
  Verdicts so far — **Task 1 KEYSTONE CONFIRMED at source + Cowork-re-verified
  independently** (`importmusicxmlpass2.cpp:5978` `addKey` fifths-only dedup
  `oldkey != key.key()` suppresses the piece-initial empty-sig KeySig → mode discarded →
  resolver sees `m_mode=UNKNOWN`; mode IS read at 6074–6096; census 79/80 zero-sig stems
  carry `<mode>` → **349 lever stands**). PRECISION CORRECTION: it's a *default-key-match*
  dedup, not "literally 0 fifths" — fix targets line 5978 (fixes notation-bridge AND
  batch_analyze callers at once). Task 0 byte-identity RE-CONFIRMED green (vs genuine
  pre-instrument baseline). Task 4 key→basisIndep CONFIRMED current post-3.3. Task 3
  music21 v9.9.1 already in REPRODUCIBILITY.md (the "unrecorded" note was stale — my
  error). Task 5 layer: composing PUBLIC-links engraving (importexport/notation-agnostic);
  fix as data to the resolver, no new dep. Task 6 doc-currency staged (§11 erratum applied,
  ledger closed, riders confirmed landed). **Task 2 = the QUARANTINE: cross-corpus
  50.7%/27.6% is BINARY-stale `.ours.json` (June-3 outputs; 5/6 spot scores flip at HEAD),
  NOT pre-F1-metric-stale (my framing was wrong — current metric reproduces it on June-3
  data). HEAD regen running for the definitive number; until then DO NOT quote
  50.7%/27.6% as current.**
  **⚠ OPEN NUANCE for the final report / Stage-4 (Cowork-flagged): the dedup is in the
  MusicXML import path — confirm whether the live product's NATIVE `.mscz` load has the
  same mode-drop or only MusicXML import does. Bears on "user-facing" vs "test-corpus"
  framing of the 349 lever (corpus is all `.xml` → fully exhibits it; .mscz users may
  not). Does not change the metric lever; sharpens its interpretation.** — recheck the facts before ratifying:
  (1) KEYSTONE — verify the mode-drop at the actual import site + `<mode>` presence
  across all 73 zero-sig stems + explain bwv62.6 (confirms/corrects the 349 lever &
  A-vs-B); (2) re-measure or quarantine the stale cross-corpus numbers at HEAD;
  (3) pin the music21 version; (4) confirm "key feeds basisIndep" is current post-3.3;
  (5) layer-check the proposed import fix (bridge vs engraving, Dependency Rule); (6)
  doc-currency sweep (the §11 erratum + contradicted "current" claims + rider-ledger
  close) so future sessions aren't misled. Verify/correct only — no fix built. Output
  gates the re-grounding ratification.

- **(superseded) QUEUED note: a deliberate BACK-HALF RE-GROUNDING design** — Cowork to write, user to ratify. Trigger: the architecture step-back
  (2026-06-13). The investigation phase produced ONE converging finding three ways
  (beam, key-path, music21-gate): **precision lives in the emission model + functional
  labeling, NOT in search/decode** (roadmap META-PRINCIPLE). The decode-centric part-1
  roadmap's consolidation is delivered, but its precision thesis is falsified; the
  back half is currently being patched fork-by-fork (an accumulating-amendment smell,
  ARCH §2.14). The re-grounding will (Level 1) re-derive the back half emission-centric
  — precision levers = emission quality + functional layer (the 17.7% tonicization
  pure-add label is the best risk/reward), search deferred until something needs it; and
  (Level 2) lay out the genuine design-GOALS fork the evidence raises: keep improving the
  HAND-BUILT emission (explainable, no-training-data, incremental, current path) vs plan
  toward a LEARNED emission (AugmentedNet/RNBert class, part-1 rec.5, higher ceiling
  ~45–50%+ full-RN vs our 27.6%, decoded by the lattice already built — costs
  explainability + DCML-training dependency). **The key-emission dossier's
  structural/fitted-vs-ceiling result is the deciding evidence for Level 2** (structural/
  fitted → hand-built has headroom, Level-1 suffices; ceiling → emission model is the
  limit, Level-2 serious). DO NOT write the re-grounding before the dossier lands (would
  pre-guess its result). Per user 2026-06-13.

- **Next CC task — key-emission headroom investigation (instruction ready):**
  `cc_instruction_key_emission_headroom.md` — measure what a key-EMISSION fix
  (partial-signature broadening / key-profile scoring) recovers of the ~85% Class-B S2
  bulk; the causal question (WHICH scoring term locks the relative-minor) needs the
  252-candidate breakdown → may build a read-only key-candidate dump as a byte-identity-
  gated diagnostic instrument (Stage 4 needs it regardless; diagnose-chord precedent).
  Output: scopes the emission fix (structural vs Stage-5-fitted vs ceiling), confirms the
  path-defer, recommends Stage 4's final shape.
  — key as an HMM path (states = tonic×mode, emissions = the existing 252-candidate
  KeyModeAnalyzer scores REUSED, transitions = circle-of-fifths modulation penalty,
  Viterbi decode → a key PATH). Targets S2 (1032 measured relative/partial-signature
  errors); PRODUCES KeyArea spans (Stage 6's tonicization labeler consumes them — the
  S1 unlock). Design-only, ratification-gated. **Load-bearing: §3 must DERIVE (real
  probe margins) that the path actually fixes S2 — if the local evidence favors the
  wrong key, that's a finding (S2 needs richer emission, not just a path), like the
  Δ=+7a finding.** Reconciles the redesign_plan "key-as-distribution SHELVED" (now has
  1032 live cases). Note: Stage 4 is the **2nd intentional behavior change** — key feeds
  chord emission (`basisIndep`), so byte-identity ends here; gated like 3.2 (measured/
  DCML-adjudicated/ratified, chord-axis side effects measured too). Measured on the L1
  `--key-breakdown` rung. Then Stage 6 (co-developed on KeyArea) → Stage 5 (fits last).
  Beam shelved; decoder_design §11 Δ=+7a erratum still queued. — tools-only, DCML-only, reuse-based, NO
  production/C++ change, NO Stage-6 vocabulary. Three primitives: (1) `compare_rn
  --wir-bach` (commit the Bach-WiR mode, 326/353 denominator explicit); (2) the
  duration-weighted union-of-boundaries unit (THE new primitive — load-bearing test =
  segmentation-invariance: same analysis at two segmentations → same score); (3)
  `--key-breakdown` (the S1/S2 = tonicization-gap/key-error split that makes Stage 4
  measurable). 70 existing metric tests stay unchanged; reproduce the dossier numbers
  via the committed modes. One commit, held. **This is the instrument the back half is
  aimed with; then Stage 4 (key path) leads, measured on L1.** Beam shelved;
  decoder_design §11 Δ=+7a erratum still queued for the next doc pass. — **user decision: design the metric
  BEFORE committing the Stage-4/5/6 order**, because the instrument that measures Stage
  4/6 success doesn't fully exist and a functional-precision metric needs a label
  vocabulary that is itself Stage-6 output (the chicken-and-egg). Design-only,
  ratification-gated. Establishes: compare_rn IS the DCML-only metric (reuse, don't
  rebuild; formalize its Bach-WiR mode); designs the granularity-robust unit (the 2.2-i
  ~7× gap); pins the functional-label vocabulary contract (Stage-6 output spec =
  metric input spec, co-designed once) + the incremental measurability ladder (Stage 4
  measurable now via key/degree; Stage 6 scored class-by-class as it ships) + the
  Stage-5 objective. Output: `docs/precision_metric_design.md` (DRAFT). Feeds a ratified
  back-half order. **Beam shelved; decoder_design §11 Δ=+7a erratum still queued.** — READ-ONLY measurement + map,
  no build. Decompose the total human-adjudicated (DCML-only, Default config, BOTH
  granularities) disagreement mass into mode/key vs functional-chord vs actual-root vs
  the ~40% "neither" residual; map each slice → unlocking mechanism (emission/transition
  reweight = Stage 5 incl. the relocated Δ=+7a fix / key path = Stage 4 / functional
  layer = Stage 6 / segmentation / structural ceiling); recommend the re-grounded
  Stage-4/5/6 ordering + the beam-revisit trigger. Output: `cc_precision_headroom_dossier.md`,
  feeds a ratified roadmap-reshape decision.
  — design-only, ratification-gated (like the decoder design): produces
  `docs/beam_widening_design.md`, 10 sections. The FIRST intentional behavior change —
  beam>1 behind the quality knob (Level-0 stays byte-identical default). Core: derive
  (not assert) HOW the wider decode fixes Δ=+7a (lattice walk of bwv102.7/bwv261, real
  probe if needed — if K=8 doesn't fix it, that's a finding); forward-edge promotion
  per Q2; K=8 per Q6; gate-folding sequence per Q3 (every gate mutates identity →
  retire/fold before widening past it). Must-not-break: Δ=+7b trio (Gate I + R coupled —
  the headline risk), identity sets ×3, snapshots. New gate: BIR/snapshot changes now
  ALLOWED but only on pre-ratified, DCML-adjudicated cases. K caution: reproduce
  Baroque target, NOT the chromatic-romantic mis-fire (3.4-ii). Design doc held for
  ratification; implementation is a separate later instruction.
  — **Cowork decision: spot-check non-chorale scores BEFORE retiring C1 gates** (the
  353-chorale "0 fires" doesn't prove E/F/K dead — they target classical/romantic
  inversion/augmented shapes; DCML mozart/chopin/corelli/beethoven MS3 already cloned).
  Per gate: fires on the non-chorale spread → KEEP as C2; fires nowhere → retire (own
  commit, 0/353×3 proof gate, held). The spot-check is the gating measurement; no
  removal pre-judged from chorale 0s. Then 3.2 (beam widening; Δ=+7a + the C2 set).
  — **with a Cowork correction to design §7: "decoder-subsumed after 3.3" is an
  UNPROVEN hypothesis** (beam-1 is numerically the old pipeline; gates exist because
  the bonuses didn't suffice) — so 3.4 ships in two phases. This run: two pre-authorized
  byte-identical ships (B/C/D dead removal with proof gate; Gate R absorbed into the
  rcb edge + 2-arg overload cleanup) + the per-gate differential dry-run (disable one
  gate at a time → pins-failing list, corpus×3 identity deltas, snapshot drift,
  classification C1 dead-in-practice / C2 beam-replaceable / C3 emission-fold /
  C4 functional-layer / C5 structural-keeper, + the Q3 beam-cap consequence per gate).
  NO behavior commits; the dossier's decision menu feeds 3.4-ii and 3.2's design.
  "Held means HELD" restated in the instruction (3.3 slip on record).
  — the hardest byte-identity gate yet: five signals MOVE between layers, so the FP
  composition must be replicated to the addition (Task 1 = a written FP-preservation
  plan BEFORE code: exact current composition quoted, capped-sum order, insertion
  points; vertical predicates become ScoringCell flags, temporal gating moves).
  Gate R's replacement condition must be DERIVED equal to the old proxy on every
  reachable input (incl. no-third qualities), then proven by 0/353×3. Deliberate
  re-pin ledger for unit tests encoding old slot semantics; end-to-end pins are NOT
  re-pinnable. One atomic commit, ratification-gated. Stop conditions include
  "FP composition unreplicable → options to Cowork" and "old/new Gate R disagree on a
  reachable input → design question". Then 3.4 → 3.2 (Δ=+7a).
  — decode-once cache for P3/P4 per design §8 + Q1/Q7. **Cowork sharpened the design's
  under-confronted point: whole-score-cached answers CAN differ from today's
  window-based P3 answers (window-edge segmentation) — this is the first live-product
  behavior change since the reviews, so the answer-delta is MEASURED (Task-3 A/B with
  DCML verdicts + P3-vs-P1 consistency quantification) and RATIFIED before any commit.**
  Conservative MVP: whole-cache invalidation on any edit (bounded re-decode = documented
  follow-up); no-reliable-change-signal = stop; snapshots stay on the raw cold functions
  (11/11 zero diffs hard gate); warm-perf must be materially better or it's a no-op stop.
  Carries the rule-5 doc riders (B2). Then 3.3 (signal migration + Gate R, atomic) →
  3.4 (gate retirement, leads 3.2) → 3.2 (beam widening; Δ=+7a target).
  — produces `docs/decoder_design.md`, 13 mandated sections: scope (chord path over
  EXISTING segmentation — joint seg+labeling explicitly out), lattice shape + memory
  envelope, term-by-term emission/transition factorization (with explicit treatment
  of the awkward non-pairwise terms: wDim post-bonus guard, Pass-B m7-budget,
  threshold/cap, Iter 86/91/pedal, gates A–L), beam-1 byte-identity argument + FP
  tripwires, path state vs advanceTemporalContext, oracle-signal migration + Gate R
  coupling redesign, per-gate retirement plan with Stage-1 pins as proof obligations,
  decode-once-query-many (closes D-P4/D-BRIDGE), quality↔beam mapping + perf budget,
  config-agnosticism, honestly-classified acceptance roster (what Stage 3 fixes vs
  must-not-break vs needs Stage 4/6), migration sequencing + rollback per step,
  §Open Questions for Cowork/user. Design-only; probes allowed (uncommitted);
  doc commit ratification-gated (rule 4 — ratification arrives as addendum file).
  — investigate → draft decisions → at most one surgical fix. HEADLINE INVESTIGATION:
  does the user's style/preset EVER reach the notation analysis path, or is the whole
  preset system batch-tools-only? (Gates the D-PASS0 decision; "presets never shipped
  to users" would be a product-level finding.) Decision drafts for D-P4/D-BRIDGE
  (lean: document cold-context contract, defer to Stage 3 decoder), D-PASS0
  (investigation-dependent), D-GAP (fix only if probe proves user+gate-neutral;
  3 regression cases re-run as causal validation). Commits V1/V2 are
  RATIFICATION-GATED (Cowork must approve the decision drafts first — rule 4 honored:
  ratification will arrive as an addendum instruction file); V3 bookkeeping direct.
  Carries the doc riders (CLAUDE.md kDiagTemplates checklist, ARCHITECTURE.md:861,
  audit moot item). Then 2.5 (P3 profile) closes Stage 2; Stage 3 (decoder) begins.
  — implements `cowork_corpus_audit.md` C1–C4: snapshot/gate source manifests with
  sha256 + clone commits + drift test + REPRODUCIBILITY pinning (license facts
  recorded, no in-tree copies), music21 provenance (establish or freeze-by-fiat),
  353/361/410 trace + diff lists, stale deletions (flat .ours.json, accident dirs,
  unreferenced src/composing/tests/scores after final sweep), score_inventory.md
  refresh. 5 proposed commits (H1–H5), await Cowork as a set. KEY stop condition:
  snapshot-source hashes not matching what goldens were generated from = gate-integrity
  question, report immediately. After this: Stage 2.3 (diagnoseChord production view),
  2.4 (divergence decisions incl. inferGapRegion preset leak), 2.5 (P3 profile).
  — Phase 4c move: `analyzeSection` + section-level analysis (cadences, pivots,
  stabilization, degree, key-resolution wrappers) from `notationcomposingbridgehelpers.cpp`
  into composing (suggested `analysis/section/`). Mechanical relocation, byte-identical;
  **zero snapshot diffs is the decisive proof** (snapshot tests call analyzeSection
  directly). Explicit file authorization includes the notation bridge/implode files
  (caller updates + code removal only). Test-ledger requirement (coverage provably not
  dropped). Rider: `chordanalyzer.h:402–409` doc-comment fix. TWO commits proposed
  (rider + move), both await Cowork. First production-code instruction since the
  reviews. Then 2.2 batch parity + single re-baseline (metric-bug decisions F-1/F-2,
  "24" provenance trace), 2.3 diagnoseChord, 2.4 P4/bridge decision, 2.5 P3 profile.

- **⚠ Cowork sandbox caveat (learned 2026-06-10):** Cowork's Linux-sandbox view of the
  repo can serve STALE git/file state (symptoms: spurious ` M` entries, index.lock unlink
  warnings, files appearing present after deletion). Host-side Read tool is authoritative
  for file contents; CC's native git is authoritative for git state. Do not overrule CC's
  git evidence from the sandbox view without a host-side Read cross-check.
  **Additionally:** Cowork's sandbox `git status` can LEAVE a stale `.git/index.lock`
  behind (it cannot unlink the lock it creates — blocked CC's `git add` once, 2026-06-10).
  Cowork should prefer `git --no-optional-locks status` / log/show in the sandbox; CC may
  safely remove a zero-byte stale index.lock after confirming no git process is running.

- **Previous CC task — Stage 0 hygiene (done, partially committed):**
  Instruction file: `cc_instruction_stage0_hygiene.md` (implements
  `docs/implementation_roadmap.md` Stage 0, items 0.1–0.6).
  Tasks: doc pass + doc commit (incl. committing untracked `layer_architecture_audit.md`
  and `implementation_roadmap.md`); delete repo junk; remove dead fnCtx keyFifths/keyMode
  fields; `kTemplateCount` shared constant across the 5 sync sites; FP tie-policy section
  in scoring_model.md; document onsetBoundaryThreshold + region-collapse divergences.
  Two commits: docs (commit immediately), code hygiene (propose, await Cowork).
  Hard constraint: byte-identical — 416/416 · 52/52 · 11/11, BIR 13/7 unchanged, both
  presets regenerated, tools/corpus restored to Baroque. Report: `cc_stage0_report.md`.

- **Previous HEAD:** `1bfc64d18c` (refactor: unify chord-commit path — Phase E Step 5).

  `1bfc64d18c` — adds `advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf, chosen, gateCtx)`
  overload in `chordanalyzer.h`; replaces three separate manual commit patterns in
  `regionanalyzer.cpp` (Pass 1, Pass 2, Pass 2b) with the unified call. Sub-region passes gain
  per-parent rolling-state variables (`subRunningStepwiseCount`, `subRecentRootsBuf`). Byte-identical
  (A/B verified, 0/353 diffs both corpora). 416/416 · 52/52 · 11/11. BIR 24/13 / 35/7 unchanged.

- **Prior lineage:** `90a52b5fee` (fix: bridge forward-lookahead in findTemporalContext).

  Recent master lineage: `90a52b5fee` (fix: bridge forward-lookahead in findTemporalContext) ←
  `bffb6c4e3d` (test: Gate R unit tests) ←
  `927e8b579d` (docs/chore: comment fixes — E1–E5) ←
  `0b51395527` (docs: STATUS.md Gate R baselines) ←
  `638ced1c12` (feat: Gate R — harmonicfunctionlayer.cpp + scoring_model.md + 6 goldens) ←
  `f9ba22157d` (fix: G-E phantom HalfDim + float literals — E3 Tasks 2+3) ← ...

- **Gate R — committed `638ced1c12` (2026-06-09):**
  - Fixes all three Δ=+7b targets: bwv245.28 (E), bwv296 (G), bwv320 (C) ✓
  - Bonus: bwv349 m13 fixed (Am → F/A = DCML root F, BIR=true error removed)
  - No regressions in either preset; full 353-score corpus rebuild verified
  - Two required refinements: `basisDep ≤ 0` condition + `!explorationMode` guard
  - 6 bridge-path snapshot goldens refreshed; all DCML-verified:
    - bach_chorale_003 tick 7680: Asus4→D major = DCML V6 (D/F#) **Improvement**
    - bwv806_prelude: E/G# = DCML I6 of local key E **Improvement**
    - bach_chorale_137: winner unchanged, rcb-inflated C-major alternative dropped **Neutral**
    - chopin_bi105_op30_2: alternatives-only, winner B minor unchanged **Neutral** *(CC's §8 correction: reported as winner change, was not)*
    - mozart_k279_1: spurious G/E alternative dropped, winner unchanged **Improvement**
    - bach_bwv806_gigue: runner-up alt change only **Neutral**
  - Golden path correction: goldens live at `src/notation/tests/pipeline_snapshot_tests/snapshots/`
    NOT `src/composing/tests/snapshots/` — update future git-add instructions accordingly
  - `tools/corpus/` holds stale PRE-Jazz regeneration; needs fresh regeneration before trusting numbers

- **Layer architecture audit complete (2026-06-09):** Full findings in
  `docs/layer_architecture_audit.md`. Key conclusions:
  - E2d split is sound; oracle/pipeline boundary is real
  - Five temporal signals remain in oracle as documented pre-existing debt
    (`chordanalyzer.h:329`) — do not move until Phase E
  - `harmonicfunctionlayer.h` basisIndep comment is inaccurate (claims "no progression signal")
  - `contextualBonuses` invariant at `chordanalyzer.cpp:1634` is stale
  - ~~Bridge path missing forward lookahead~~ — **FIXED `90a52b5fee`**: forward walk added to `findTemporalContext` mirroring backward walk; `nextRootPc`/`nextBassPc`/`bassIsStepwiseToNext` now populated via `seg->next1(ChordRest)` + cold analysis through full gate pipeline
  - Sub-regions always have `bassIsStepwiseToNext = false` (consistent, undocumented)
  - Gate R's `basisDep ≤ 0` depends on `sameRootInversionBonus` staying in oracle
  - **Recommended next CC tasks:** unit tests for `bassIsTemplateChordTone` + Gate R branches;
    comment fixes for 2a/2b/3/6; ChordSymbolFormatter extraction (low priority)
  - **Do NOT split `chordanalyzer.cpp` now** — wait for Phase E to motivate it

  Recent master lineage: `f9ba22157d` (fix: G-E phantom HalfDim + float literals to named constants — E3 Tasks 2+3) ← `a693b6ba82` (docs: COWORK_HANDOFF.md post-E2d housekeeping) ←
  `22b89ae521` (tools: iter 90–97 analysis scripts) ←
  `5b08465924` (docs: iteration logs, key detection, LLM integration) ←
  `0ea52ced98` (chore: gitignore CC/Cowork working-process files) ←
  `8f13aee8d3` (test: remove equivalence harness) ←
  `469d7830f2` (docs: CLAUDE.md scoring-doc process rules) ←
  `2917ec7571` (E2d redesign: scoring oracle / competition pipeline) ←
  `0ab219d4c5` (E2d-prereq Phase 1: extract Iter 86/91/pedal) ←
  `20f992a5e7` (E2c-infra: function-layer plumbing) ←
  `710d8dba12` (E2b: scoring snapshot) ← `80a7adf32e` (E2a: progression-signal
  lambdas) ← `dd29a04967` (E1: function layer shell) ← `3ac52e1198` (scoring_model.md
  + annotations) ← `945a9e2f18` (B2 aug7 template) ← `f3e0f5f72c` (Sub-9a Gate G-E
  fix) ← `81978321e3` (keyresolver partial-sig) ← `fe752fb6d9` (A4 Corelli) ←
  `a69a23e59b` (D2 + docs).

- **BIR baselines (lenient-OR `align_regions`, `tools/characterise_bir_false.py`):**
  Baroque BIR=true=24, BIR=false=13; Jazz BIR=true=35, BIR=false=7.
  Hard stops: Baroque BIR=false must not increase above 13; Jazz BIR=false must not increase above 7.
  Cumulative since Iter 91: Baroque BIR=false 188 → 13 (−175, ~93% reduction).
  **IMPORTANT — BIR script note (corrected 2026-06-10, Stage 1d F-3):** the **13**
  (BIR=false residual count) comes from `tools/characterise_bir_false.py` (lenient-OR
  align_regions comparator). That script does NOT compute the **24** (BIR=true) — the
  24's producing script was not established in the Stage-1d survey; treat it as a
  corpus-characterisation figure of unverified provenance until traced.
  `tools/analyze_inversion_errors.py` reports a DIFFERENT metric (music21∩DCML
  bassIsRoot three-way split) — these are NOT the same numbers and must not be used
  interchangeably in instructions.
  `tools/corpus/` = POST-Gate-R Baroque state (regenerated 2026-06-09, 353 scores).

- **Jazz BIR=false=10 — fully characterised (2026-06-08):** 8 cases shared with Baroque
  (Δ=+7 rootContinuity ×3, sus/quartal ×2, segmentation ×1, evidence-absent ×1,
  dim→dom absent-root ×1); 2 Jazz-only (bwv244.15 key-conf-0 root mis-selection;
  bwv74.8 added-tone tetrachord — Em7/D for Cadd9, the B4 6th/m7 ambiguity).
  Jazz's reduced individual inversion bonuses (0.20/0.20/0.15/0.20 vs Baroque
  defaults; NOT the cap — `maxTotalInversionContextBonus` is never set and
  non-binding, see 2026-06-10 doc-pass Task-1 finding) remove Baroque's absent-root
  inversion cases (bwv14.5, bwv174.5, bwv301, bwv381) from Jazz — confirmed by
  prior prediction. Nothing newly actionable beyond the absent-root guard (bwv45.7
  dim→dom absent-root, partial). Full table in `cc_stepback_report.md`.

- **Tests:** **416/416 composing** (+9 Gate R unit tests in `gater_tests.cpp`; equivalence
  harness removed — tautological post-redesign), **52/52 notation (fully green)**, 11/11
  pipeline snapshot (1 intentional skip = `PipelineDivergenceCObservation.GenerateReport`).
  Mismatch report: Jazz 130 (131→130 post-E2d path unification).

- **Part G commit (2026-06-09, session 3):**
  - `90a52b5fee` — bridge forward-lookahead fix. `findTemporalContext` in
    `regiontonecollector.cpp` now calls `seg->next1(ChordRest)`, cold-analyzes successor
    through full `applyIter8691Pedal` + `applyPostScoringGates` pipeline, sets
    `nextRootPc`/`nextBassPc`/`bassIsStepwiseToNext`. Only `regiontonecollector.cpp/.h`
    touched. 3 snapshot drifts — all P4 tickLocal, all improvements or neutral:
    - chorale_137 t2880: Dm → Bø7 — **Improvement** (G-B gate fires; matches batch)
    - chorale_001 t15600: Bm → G — **Improvement** (onset {G,B,D} = G major; old Bm impossible)
    - chorale_001 t11280: F#dim → F#ø7 — **Neutral** (root unchanged; quality refinement)
    Goldens refreshed. 416/416 · 52/52 · 11/11. BIR unchanged 24/13 / 35/7.
    Full report: `cc_bridge_lookahead_report.md`.

- **Part E + Part F commits (2026-06-09, follow-on to Gate R):**
  - `927e8b579d` — comment-only: (E1) `harmonicfunctionlayer.h` basisIndep accuracy; (E2)
    stale invariant clarified at `chordanalyzer.cpp ~L1634`; (E3) Gate R cross-layer
    dependency documented; (E4) bridge lookahead gap noted in `findTemporalContext`; (E5)
    golden path corrected in `BUILD_AND_TEST.md`. Byte-identical.
  - `bffb6c4e3d` — `bassIsTemplateChordTone` + `gateRZeroesRootContinuity` promoted to `fn`
    namespace (behavior-preserving); new `gater_tests.cpp` (9 Gate R unit tests). Composing
    416/416 (+9). Byte-identical (no BIR change).

- **Git status audit (2026-06-06, pass 2 complete):**
  - Stash: empty. Working tree clean.
  - `compare_rn.py`: already committed (`f6630b29cd`) — old handoff "pending commit" note was stale.
  - `bwv*_dcml.xml` (5 files): moved to `tools/dcml/` (intentionally gitignored — reproducible QA artifacts). Not committed; correct.
  - Root helper scripts deleted: `step3_build_and_test.ps1` (D2 experiment harness, superseded), `run_e2b_tests.bat` (E2b phase wrapper, superseded).
  - 2 untracked files remain in `tools/` — `.txt` data dumps, skip (generated output).
  - `ai-assistant/` is a separate project; ignore its untracked files here.

- **DCML cross-corpus baseline = 53.8%** (20256/37639, DCML-anchored, time-overlap,
  lenient-OR; 10 non-Bach corpora). Regenerated against the HEAD `a69a23e59b` binary
  on 2026-05-20. **Supersedes the prior 46.8% (15928/34022) at `53c4f2d50c`**, which was
  measured BEFORE STEP 1 + D2 changed chord output — a **+7.0 pp** gain with **every corpus
  improved** (biggest: Corelli +13.7, Mozart +9.4, Schumann +8.4; C.P.E. Bach still 0
  regions, excluded). Reports under `tools/reports/live_20260520_postd2/` (gitignored).
  Regenerate: run the 10 `tools/run_<corpus>_validation.py` scripts
  (`--output <dir> --batch-analyze ninja_build_rel/batch_analyze.exe`; the beethoven
  script writes to a dir named exactly `beethoven`) then
  `python tools/rerun_dcml_comparison.py --cross-corpus-root <dir>`.

- **STEP 1 — dim7-completeness guard + Gate J (committed `3d80d0a91d`):**
  Two coupled `chordanalyzer.cpp` changes. (1) The dim7 characteristic bonus now requires
  the **complete diminished triad** (root + ♭3 + ♭5) before it fires, so an incomplete
  diminished sonority stops out-scoring the dominant-seventh reading the evidence supports.
  (2) **Gate J** — a root-position diminished triad whose dominant root (a major third below)
  is present is treated as an **inverted V7** (vii° → V7 completion; canonical case
  bwv110.7 m10 `C#dim7 → F#7`); requires the complete diminished triad. Impact:
  **Jazz BIR=true 56→33 (−23)**, **Baroque BIR=false 25→23 (−2)** (Jazz fixes bwv282,
  bwv60.5, bwv65.2). 5 pipeline-snapshot goldens refreshed and DCML-verified.

- **D2 unification (committed `4d881e7418`, recorded in `a69a23e59b`):**
  `pass1MinDistinctPcsForCandidate=1` on the batch path — matching the bridge. This was the
  **last batch/bridge parameter divergence**; bridge and batch are now **fully unified** thin
  wrappers over `region::analyzeRegions()`. Both paths admit sparse 1–2 PC Pass-1 slices.
  `regionanalyzer.cpp` untouched (pure flag unification). Net error reduction both corpora
  (Baroque BIR=true 34→27 / false 25→23; Jazz BIR=true 56→33 / false 13→10).

- **Unification status:** Iter 97 Phases 2+3+4 + D2 are **complete**. Both parameter
  divergences are resolved: **D1 (`excludeLookAheadOnDenseStart`)** is confirmed
  load-bearing and **intentionally divergent** (batch passes `true`, bridge defaults
  `false`; unifying it regresses bridge/Corelli trio-sonata dominants); **D2
  (`pass1MinDistinctPcsForCandidate`)** is unified at `1` on both paths. The bridge and
  batch are fully unified thin wrappers over `regionanalyzer`.

- **Iter 98 — attempted and reverted (2026-05-23). Dead end documented — do not re-attempt.**
  Both the sparse-continuity suppression approaches tried in Iter 98 produced the same
  DCML-verified regression on mozart_k280-1 (m9/m12 IV→V65 over-merge), which means the
  failure is **intrinsic to suppressing sparse-predecessor continuity** — Alberti-bass
  textures genuinely need that continuity and neither a density gate nor an inversion-aware
  gate can separate bwv320 from mozart. Full dead-end analysis recorded in CC's Iter 98
  backlog memory. Baseline fully restored to HEAD `a69a23e59b`; nothing committed.

  Two approaches tried and rejected:
  - **Predecessor-sparse gate** (`previousRegionDistinctPcs ≤ 2` → suppress
    `rootContinuityBonus`): fixed bwv320, but hit mozart_k280 IV→V65 regression.
  - **Inversion-aware refinement** (suppress only when candidate `bassPc ≠ rootPc`):
    fixed bwv320 + Chopin test, improved BIR both corpora (Baroque 23→21, Jazz 10→9),
    but still produced the same mozart_k280 IV→V65 pipeline-snapshot regression (DCML-verified
    wrong). Same regression as the rejected orchestrator approach → intrinsic dead end.

  **bwv320 m27 (accepted residual — needs a different mechanism):** reads `G6/E` instead
  of `C`. An admitted 2-PC `Gm` Pass-1 slice overwrites `previousRootPc`, and
  `rootContinuityBonus` (+0.40) tips a 0.02-margin window to G. Margin-based and
  density-based discriminators **cannot** separate this from legitimate sparse-continuity
  cases in Alberti-bass textures. If revisited, needs a **targeted segmentation or
  merge-level fix** around tick 37440–38400 rather than a scoring gate.
  - **α-variant: `w_dim` rotation-only guard** — **DEAD END, do not re-attempt.**
    Tried 2026-05-23: requiring the pre-bonus winner to also be Dim/HalfDim regressed
    Baroque (+4 BIR=true, +1 BIR=false) and broke 2 bwv806 pipeline snapshots without
    fixing either target case. Root cause: wDim exists to elevate a non-dim winner to dim
    — requiring the pre-bonus winner to already be dim defeats its purpose. The two
    originally deferred target cases are not wDim problems at all (see below).
    - **schumann tick 480 (viio7/V = C#°7):** the 240-tick C#°7 region is absorbed by
      `absorbShortRegions` (Phase-4 removed Iter-77 Fix-A protection). P4 tickLocal has
      the right quality (dim7) but wrong rotation (G°7 vs C#°7) because `nextRootPc` is
      not plumbed into the per-tick path. Needs: (a) surgical absorption exception for
      short leading-tone dim regions, and/or (b) `nextRootPc` plumbing into P4. Both are
      upstream architectural issues, not scoring problems.
    - **chorale_003 Am→G#dim:** no authoritative ground truth (DCML doesn't cover Bach
      chorales). All Am regions are 3-PC triads — wDim is gated out by `distinctPcs>=4`
      by design. Accepted residual; do not pursue via wDim.
  - **δ: sparse-minor diatonic quality prior** — **DEAD END, do not re-attempt as a quality fix.**
    Diagnosed 2026-05-23: the remaining Corelli failure (`CorelliOp01n08dUserReportedChordTrackAudit`)
    is rooted in **key mis-detection**, not chord quality. The quality prior would read the
    wrong detected key (G minor instead of C minor) and reinforce wrong answers. The three
    remaining sub-failures are: m24 F→Fm (key symptom), m2 b3 G/B inversion (separate
    inversion issue), m18 missing Cm region (segmentation). Do not revive δ until the key is
    corrected.

  - **Key/mode detection — Baroque partial-signature bug: FIXED (`81978321e3`).**
    Option B landed: keyresolver now allows signature-flexible tonic candidates. Corelli
    op01 scores now detect C minor correctly. Full write-up in
    `docs/key_detection_baroque_partial_signature.md`.

  - **Dominant-quality fix — deferred (1-PC segmentation cascade). distinctPcs gate is a dead end.**
    Both the Corelli target (op01n08d m1 b3) and the Chopin regression source
    (bi105_op30_2 tick 23040) are **1-PC** — a `distinctPcs >= 2` gate suppresses both.
    Diagnosis from CC Step 2b investigation (2026-06-03):

    | | Corelli m1 b3 | Chopin tick 23040 |
    |---|---|---|
    | distinctPcs | 1 | 1 |
    | pitchClassSet | G only | F# only |
    | quality (current) | Minor / Gm | Minor / F#m |
    | key | C minor | B minor |
    | keyConfidence | **0.9615** | **0.6273** |

    The only signal that separates them is **`keyConfidence`**. A corpus-wide survey
    of all 267 matching slices was run (2026-06-03). **There is no bimodal gap** —
    the distribution is continuous from 0.00 to 1.00 with every 0.05-wide bucket
    non-empty. The distribution summary:

    ```
    [0.95,1.00)  17   ← Corelli anchor (0.9615) here; 82% drop from next bucket
    [0.90,0.95)   3
    [0.85,0.90)   3
    [0.80,0.85)   3
    [0.75,0.80)   5
    [0.70,0.75)   6
    [0.65,0.70)   5
    [0.60,0.65)   3   ← Chopin regression (0.6273) here
    [0.55,0.60)   1
    [0.50,0.55)  21   ← score-opening "no key evidence yet" sentinel values
    ...below 0.50: 149 slices (bulk of the ambiguous-v mass)
    ```

    The only clean structural break is at **0.95**: 17 → 3 (82% drop). This is a
    **tail effect, not a bimodal gap**. No contiguous near-zero band exists that
    would justify a principled "real V vs ambiguous v" cut at any lower threshold.

    **DEFINITIVE DEAD END — defer to Phase E. Do not re-attempt via keyConfidence alone.**

    Pre-inspection of the 17 highest-confidence cases (kc ≥ 0.95, 2026-06-03) found
    **5/17 clear false positives (29% FP rate)**:
    - Mozart K457-1 m180.2 (kc=1.0): DCML = III6 — single G is the third of E♭ first
      inversion, not a V root.
    - Mozart K457-3 m181.2 (kc=1.0): DCML = It6 (Italian aug-6th) — pre-dominant, not V.
    - Beethoven Op.130-ii m57.3 (kc=1.0): DCML = bVI in B♭ major; key disagreement
      (analyzer: C Dorian vs DCML: B♭ major) plus PC mis-detection.
    - Beethoven Op.130-ii m61.2 (kc=0.972): DCML = @none (silence/rest).
    - Tchaikovsky op37a06 m1.2 (kc=0.962): DCML = tonic i — analyzer mistakes the
      chord-tone 5th of a long G-minor tonic chord for a D-dominant root.

    These false positives require knowledge of adjacent harmonic context (voice-leading
    direction, resolution, cadence type) that `keyConfidence` does not encode. Even the
    top tier (kc=1.0) contains III6 and It6 misreadings. A gate on keyConfidence alone
    cannot separate them from genuine V chords at any threshold.

    **The correct fix belongs in Phase E** (harmonic function layer): cadence confirmation
    (detect a preceding leading-tone or V7→i resolution) distinguishes genuine dominant
    preparation from single-PC chord-tone arpeggiation. Until Phase E, Corelli m1 b3 stays
    at "Gm" (the notation test deferral comment remains in place).

    Survey artifacts: `tools/survey_1pc_dominant_slices.py`,
    `/tmp/dominant_survey_out.txt` (370 lines, full sorted table + histogram),
    `C:\Temp\dominant_survey\<corpus>\*.json` (948 fresh Baroque dumps, cached).

- ~~**Pre-existing issue to investigate:** BWV227.7 m9 pitch-class E~~ **RESOLVED** (`fc1206bd4e`) — test expectation fixed to use tick-overlap; no analyzer change.

- **Mozart k280_1 cascade (introduced A4, queued):** `mozart_k280_1` pipeline-snapshot
  golden was refreshed after the A4 hasStructuralBass gate caused a secondary change at
  one tick (Bb/F replaced Cadd11/F). Both the old and new readings diverge from DCML V43
  — neither is correct. Queued for C3/C4 characterisation.

- **Chord mismatch report:** 4 RealDiff (pinned), 127 ConventionDiff (Jazz)

---

## Roadmap — phased by dependency then risk

Phases are ordered: later phases depend on earlier ones, or carry higher architectural
risk that earlier phases de-risk. Within a phase, items are ordered lowest-risk first.

---

### Phase A — Foundation (in progress / immediate next)

These unblock everything below. Do not start B–F until A is stable.

**A1. Key/mode detection — Baroque partial-signature fix** *(CC in progress)*
Option B (`keyresolver.cpp`): allow signature-flexible tonic candidates. Full write-up in
`docs/key_detection_baroque_partial_signature.md`. Validate against both BIR presets +
notation + snapshots. Target: Corelli op01 scores detect correct key.

**A2. Dominant-as-major quality in minor keys** *(deferred to Phase E — keyConfidence insufficient)*
`sparsechordrefinement.cpp` — `applyTonicPriorToSparseChord` maps degree-5 in minor to
natural-minor v (Minor) instead of major V. Full investigation completed (2026-06-03):
both discriminators exhausted. `distinctPcs >= 2` cannot separate the cases (both 1-PC).
`keyConfidence` has no bimodal gap (267 slices, continuous distribution), and the top
kc ≥ 0.95 tier has a 5/17 (29%) DCML-verified FP rate (III6, It6, bVI, rest, tonic-5th
misreadings). Fix requires Phase E cadence-confirmation signal. Corelli m1 b3 stays "Gm"
with deferral comment in `CorelliOp01n08dOpeningAndSparseLateBeats`.

**A3. Roman numeral ground-truth comparison tooling** ✅ *DONE — `tools/compare_rn.py` + baseline `tools/reports/rn_baseline_f3e0f5f72c.txt`*

New script `tools/compare_rn.py` (single-piece / single-corpus / cross-corpus modes).
Reuses `compare_analyses.align_dcml_regions` (time-overlap, lenient-OR ≥50%). Normalises
key-prefix, modulation marker, figured-bass tokens; maps DCML `%` → our `ø`; case-sensitive
(case encodes quality). cpe_bach skipped (stem mismatch, orthogonal issue).

**Baseline — 9 non-Bach corpora, 520 movements, 61,233 matched regions (HEAD `f3e0f5f72c`):**

| metric | value |
|---|---|
| rn_agree | **27.6%** (16,905/61,233) |
| exact_match | 18.0% (11,027) |
| partial_match | 9.6% (5,878) — root+quality correct, inversion/extension differs |
| quality_err | **21.7%** (13,305) — root correct, quality wrong |
| root_err | 50.7% (31,023) — root wrong (= BIR=false set) |
| root_agree (parity) | 49.3% (30,210) |

Top-5 disagreement patterns:

| ours | → DCML | count |
|---|---|---|
| V | → I | 1,131 |
| I | → V | 660 |
| V | → V7 | 487 |
| IV | → I | 448 |
| III | → I | 438 |

**Key observations (classifier corrected 2026-06-04):**
- root_err (50.7%) dominates — consistent with BIR metric
- quality_err (21.7%) was **misleadingly named**. `_same_quality()` was a pure string
  comparison on the degree base (`"V" == "I"` → False), so V→I fired `quality_err`
  even though both are major quality. **Classifier fixed 2026-06-04** — `quality_err`
  replaced by two precise buckets:
  - **key_disagree = 15.4% (9,440/61,233)**: root + coarse quality agree, scale degree
    differs — key/mode detection error. E.g. V→I means "we say G is scale-degree 5 in
    C major; DCML says the same G is scale-degree 1 in G major." Phase E only.
  - **quality_disagree = 6.3% (3,865/61,233)**: root PC agrees, coarse quality genuinely
    differs — true chord-quality error. Sum 21.7% preserved; split 71% key / 29% quality.
- **Maj→Dom7 gap — INVESTIGATED AND CLOSED (2026-06-04):**
  Maj→Dom7 is 948 cases (24.5% of quality_disagree; top corpora: Beethoven 32%, Chopin 17%,
  Grieg 16%, Corelli 12%, Mozart 10%). Sampled 25 cases across 5 corpora with
  `tools/find_maj_to_dom7.py` — checked 7th-PC pcWeight for each:
  - 32% (8/25): 7th PC **entirely absent** from the sounding tones
  - 48% (12/25): 7th PC present but raw weight **below extensionThreshold (0.20)**
  - 20% (5/25): 7th PC present at ≥ 0.15 weight ratio (mostly Chopin add9 detections
    where we already detect a 9th extension and the DCML disagrees about which extension
    to model)
  **Conclusion: not an actionable bug.** DCML systematically labels *implied* dominant
  sevenths from harmonic-functional context even when the 7th doesn't sound. Our analyzer
  correctly withholds the extension without sounding evidence above extensionThreshold.
  Lowering the threshold to capture these would cause large-scale false-positive 7th chords.
  Accepted as extension-threshold gap. Phase E (harmonic function layer) is the correct fix.
- quality_disagree remaining after Maj→Dom7: ~2,917 regions — Min→Maj (714, 5.4%) and
  Maj→Min (~465, 3.5%) are the next-largest buckets (parallel major/minor confusion).
  Not yet investigated.
- partial_match (9.6%): root+quality right, inversion/extension off

**Corrected reports (2026-06-04):**
- `tools/reports/rn_corrected_classifier_f3e0f5f72c.txt` — cross-corpus summary with
  key_disagree / quality_disagree split
- `tools/reports/rn_corrected_breakdown_f3e0f5f72c.txt` — quality_disagree breakdown
- `tools/reports/maj_to_dom7_samples.txt` — 25-case 7th-pcWeight sample data
- New helper: `tools/find_maj_to_dom7.py`

**Pending commit:** `tools/compare_rn.py` (classifier fix) + the above new files.
Working tree is dirty with these tooling changes. Commit when convenient.

**Immediate actionable targets remaining from this analysis:**
1. ~~Fix compare_rn.py classifier~~ ✅ Done
2. ~~Maj→Dom7 gap~~ ✅ Investigated — closed as extension-threshold gap (not actionable)
3. Key/mode detection errors (key_disagree 15.4%, ~9,440 cases) — Phase E only
4. ~~Parallel major/minor confusion (quality_disagree Min→Maj 714 + Maj→Min ~465)~~ ✅
   Investigated (2026-06-08 step-back). **Closed as convention gap.** ~75% of 1,181 cases
   are thirdless (neither third above extensionThreshold) — analyzer infers quality from
   key/degree context; DCML labels functional role. Same conclusion as Maj→Dom7. Remaining
   ~25% are DCML function-over-sonority (sounding third agrees with our read; DCML overrides
   via modal mixture, raised thirds, Picardy, etc.). Not actionable via scoring/gate changes.
   rn_agree secondary metric largely frozen without Phase E.

**Corpus note:** The snapshot `tools/reports/live_20260603/` predates HEAD by one day;
<10 regions of 61k affected. The 49.3% root_agree here vs 53.8% at `a69a23e59b` is
a corpus/denominator difference (different regeneration run), not a regression.

**rn_agree=27.6% is now the secondary quality baseline** alongside root_agree=53.8%.
Every future code change must not regress rn_agree below 27.6%.

**A4. Remaining Corelli Test 2 sub-failures** ✅ *DONE — commit `fe752fb6d9`*
Both sub-failures resolved; notation suite now **52/52** (fully green).

- **m2 b3 G/B → G:** Score had only upper-register notes (violin G5+B4, bass staves
  rest). Bass-candidate enumeration was disabled; legacy fallback picked B4; stepwise-
  inversion bonus (+0.5 for C→B descending) tipped to V6. Fix: sparse-upper-register
  trigger for bass-candidate enumeration (`distinctPcs ≤ 2 && lowestPitch > 60 &&
  ≥2 regional candidates`); `hasStructuralBass` parameter gates inversion contextual
  bonuses (set false when `lowestPitch > 60 && distinctPcs < 3`). File:
  `chordanalyzer.cpp`.

- **m18 b1 missing Cm:** Pass 2b split Cm into four 240-tick sub-regions; each was
  individually absorbed by `absorbShortRegions` into the m17 Gm predecessor. Fix:
  `coalesceShortSameRootRuns` pre-pass in `regionanalyzer.cpp` — coalesces runs of
  ≥3 consecutive contiguous same-root sub-regions totalling ≥720 ticks before
  `absorbShortRegions` runs. Guarded by predecessor-root check.

BIR at time of A4: Baroque 27/23 → 28/22 (net flat, one case moved false→true). Jazz 33/10 → 35/10
(+2 true, false unchanged). 4 pipeline-snapshot goldens refreshed (DCML-verified):
`corelli_op01n08a`, `chopin_bi105_op30_1`, `mozart_k279_1`, `mozart_k280_1`.

**Known follow-up — Mozart k280_1 cascade:** the A4 fix caused a secondary change at
one k280_1 tick (Bb/F replaced former Cadd11/F). Both readings diverge from DCML V43
— neither is correct. The snapshot was refreshed to the new (also-wrong) reading.
Queued for C3/C4 characterisation or separate triage.

**A5. BWV227.7 m9 pitch-class E regression** ✅ *DONE — commit `fc1206bd4e`*
Test expectation error (Category 4). The analyzer correctly captured pc=E in the G
region anchored at m8 b3 (ticks [14400,16800), pcs include E), which physically
spans into m9. The test filtered by `measureNumber==9`, missing it; the only
`measureNumber=9` region was a tail Gadd9/F# with no E. Fix: switched detection to
tick-overlap against the m9 range [15360,17280). Test-only change; no analyzer code
touched. BIR baselines at A5 unchanged (Baroque 28/22, Jazz 35/10). Pre-existing since
before STEP 1/D2/A1–A4.

---

### Phase B — Template completeness (independent of A, but requires Phase E guard for any template whose PC set overlaps a common Baroque progression)

**⚠ B1 lesson:** Before attempting any new template, check whether its PC set is a
subset of a common Baroque progression in a minor or major key. If yes, the template
will fire in those contexts and requires a Phase E functional guard before it is safe.
B1 ({0,3,7,11}) overlaps {tonic+leading-tone-of-V}; a bare template cannot separate them.

Can be done in parallel with A or after. Each template addition is atomic and
independently verifiable against both BIR presets + snapshots.

**B1. Add MinorMajor7 template {0,3,7,11}** *(deferred to Phase E — leading-tone ambiguity)*
Attempted 2026-06-04. **REJECTED — do not re-attempt without Phase E guard.**
Approach A works mechanically (no new enum needed: `ChordQuality::Minor` +
`hasMajorSeventh` extension; `qualitySuffix` already emits `mMaj7` for that
combination). Three array-size sites to update when retrying: `analyzeChord`
`array<TemplateDef, 16>` at chordanalyzer.cpp:1923; `diagnoseChord` array at
:3334; three `array<array<double,16>,12>` score matrices at :1982–1984 (missing
those last three caused a stack-buffer overrun). Results: Baroque BIR=false 23→25
(+2, hard-stop limit); 2 DCML-wrong pipeline-snapshot winners (bach_chorale_003
V65 `E7/G#`→`AmMaj9`; bwv806_prelude tick 36720 `Bmadd9/C#`→`C#m`). Root cause:
bare {0,3,7,11} cannot distinguish {tonic+leading-tone-of-V} from a genuine i(maj7)
in Baroque minor-key contexts. A V→i suppression guard would defeat the jazz use
case (ii–V–i resolution is V→i). **Needs Phase E cadence confirmation to identify
whether the leading tone is resolving to i or is still the active dominant.**
Full rationale in `docs/backlog_b1_mmaj7_template.md`.

**B2. Add Augmented dominant 7th template {0,4,8,10}** (C7♯5) ✅ *DONE — commit `945a9e2f18`*
Guard: skip the 4-tone Augmented template for any root where either M3 (rootPc+4) OR
aug5 (rootPc+8) is absent below extensionThreshold (both required). Without both-tone
guard the template over-fired on complete major triads containing a minor seventh.
BIR: Baroque 28/16 (unchanged); Jazz BIR=true 35→36 (+1), BIR=false=10 (unchanged).
Jazz catalog: m285 Tristan→D7#5/C (3rd inversion, C bass) resolves 1 RealDiff (4→3);
m286 rest used for Tristan suffix coverage. Standard 0/1 unchanged.
Three template-addition sites (both TemplateDef arrays + three score matrices).
Iteration took 4 attempts: (1) first revert — struct field `tones` vs `intervals`;
(2) second revert — Tristan catalog slash bass missing (`D7#5` vs `D7#5/C`) and
Tristan suffix coverage broken; (3) third revert — M3-only guard too loose (Schumann
D-major V, Corelli G-major I flipped to aug7); (4) M3+aug5 dual guard succeeded.

**B3. Promote dim7 {0,3,6,9} to a dedicated template** *(DEFERRED — bonus is rotation-selector, not just scoring)*

Attempted 2026-06-05. **Do not re-attempt without addressing both root causes below.**

Investigation revealed that `dim7CharacteristicBonus` (kDim7CharacteristicBonus = 0.75,
chordanalyzer.cpp:2036 + :3426) is NOT merely a scoring offset — it is a
**rotation-selection mechanism** for the enharmonic dim7 ambiguity (C°7 = E♭°7 = G♭°7 = B♭♭°7).
Its gate includes a **non-diatonic check on the ♭♭7 PC** that asymmetrically rewards the
correct enharmonic root over the three spurious rotations. Without this check, all four
rotations score identically, and 6 Jazz catalog entries distinguishing Bdim7 from its
rotations (m370/372/374) break.

Two failure modes encountered:
1. **Bonus suppression → 6 Jazz RealDiff failures.** Rotation-selection mechanism lost;
   Bdim7 chords flipped to wrong D/F-rooted rotations.
2. **Template + bonus coexisting → `bach_chorale_003` snapshot regression.** At tick 17280,
   `Em7b5/C#` flipped to `Dm/E` (indirect segmentation side effect: bass C# = ♭♭7 of E°7
   activated the 4-tone template at root=E, though the chord is half-diminished not full dim7).

Option (a) — add the non-diatonic ♭♭7 check to the template guard — not attempted: C# is
non-diatonic in the key of chorale_003 at that point, so the check would not block the
spurious fire; segmentation regression would persist.

**Pre-conditions for future retry:**
- Template guard must include the non-diatonic ♭♭7 check (mirrors the bonus gate)
- Must resolve the chorale_003 segmentation artifact (why does `Em7b5/C#` shift when
  the 4-tone template fires at root=E with C# as bass?)
- Once both preconditions met: condition the bonus to not fire when the template passes

**B4. Evaluate 6th chord templates {0,4,7,9} / {0,3,7,9}** *(needs analysis first)*
C6 and Am7 share all four pitch classes — adding these templates creates new ambiguities
that bass evidence alone may not resolve. Investigate whether the net BIR effect is
positive before implementing.

---

### Phase C — Deferred residuals (depends on A being stable)

**C1. Schumann tick 480 — viio7/V (C#°7)**
Two independent fixes needed:
(a) Surgical absorption exception: preserve short leading-tone dim regions that resolve
    to the next root (re-introduce Iter-77 Fix-A intent without region-count explosion).
    Plan before coding — absorption logic is sensitive.
(b) `nextRootPc` plumbing into P4 tickLocal path so wDim picks correct dim7 rotation
    in per-tick analysis. Investigate first — verify whether P4 currently receives
    `nextRootPc` at all.

**C2. bwv320 m27 — G/E instead of C** *(⚠ STALE SECTION — resolved by Gate R `638ced1c12`.
This is the SAME case as the Δ=+7b bwv320 instance; bwv320 is absent from the current
Baroque-13 identity set. Kept for the Iter-98 dead-end history only. Reconciled
2026-06-12 after the stage3-design report's dual-classification question — the
"C2 rcb-near-tie residual class" has NO known live instance; decoder_design.md §11's
C2 row cites this dead example, so Stage 3.2's expected wins = Δ=+7a primarily.)*
rootContinuityBonus (+0.40) fires because the preceding sparse 2-PC Gm slice
(tick 36960) set previousRootPc=7. G major (root=G, bass=E) is a legitimate
template candidate scored 1.52; +0.40 context bonus → 1.92 beats Cmaj 1.90 by
0.02. C3/C4 pre-fix audit (2026-06-04) confirmed the Iter 98 diagnosis is
correct; an earlier "re-diagnosis" claiming a slash-synthesis path was WRONG
(diagnoseChord dump omits temporal-context bonuses). All Iter 98 suppression
approaches (sparse-predecessor gate, inversion-aware gate) regress mozart_k280-1
IV→V65 Alberti-bass. Accepted residual pending Phase E (function layer).

**C3/C4. β/γ mis-root characterisation** ✅ *COMPLETE — `tools/characterise_bir_false.py` added*

The Iter-96 β/γ framing (Δ=+5 / Δ=+2) is now numerically obsolete. At HEAD
`fc1206bd4e` the 22 Baroque BIR=false residuals consolidated into two dominant
clusters — both are winner-selection bugs, not scoring gaps:

**Δ=+9 Sub-9a: Gate G-E stale-reference bug** ✅ *FIXED — commit pending*
**Baroque BIR=false 22 → 16 (−6). All tests green. No regressions. Not yet committed.**
Scores affected: bwv245.17 m10, bwv258 m4+m10, bwv309 m5, bwv356 m19 + 1 borderline.
Precise mechanism: `winner` in Gate G-E (~L2896) is a live reference to `results[0]`.
The inversion-correction `stable_sort` had already moved Am7b5/C (rootPc=9) to
results[0]. Gate G-E read rootPc=9 → `gExpectedAltRoot=(9+9)%12=6` (F#/Gb, the
WRONG leading tone), pulled in dormant F#m7b5 from rawCandidates at score ~0.10.
Fix: captured `const int originalWinnerRootPc = winner.identity.rootPc` at L2636
(alongside existing `originalWinnerQuality`/`originalWinnerHasAddedSixth` at
L2635-2637); changed L2896 to use `originalWinnerRootPc`. Gate J and all other gates
unaffected. No goldens changed.

**Δ=+7: rootContinuityBonus cluster — split into two sub-mechanisms (2026-06-08 diagnostic)**

Predecessor-confidence diagnostic (`cc_deltaseven_predecessor_report.md`, 2026-06-08)
falsified the "sparse predecessor" framing and revealed the cluster is not homogeneous:

**Δ=+7a — arpeggiation segmentation + rcb cascade (NOT a vertical-oracle bug): bwv102.7, bwv261**
*(Reframed 2026-06-09 after full per-cell oracle dump — prior "wrong root wins vertically"
characterisation was incorrect.)*

In the **committed/run-opening regions** the DCML root is absent because the arpeggio places
it one step in the FUTURE — not as a sustaining note from the past. Exact tick data
(`cc_phase_d_investigation_report.md` 2026-06-09):
- bwv102.7: failing region starts t17520; Ab (DCML root) attacks at t17760 (+240 ticks)
- bwv261: failing region starts t33840; F# (DCML root) attacks at t34080 (+240 ticks)

The 240-tick micro-regions are produced by the **initial greedy-expand** (Pass 2), which
creates a new region boundary every time the set of simultaneously sounding notes changes.
An arpeggio moving through C→Eb→Ab creates one 240-tick region per step. Pass 2b's
`detectBassMovementSubBoundaries` is not involved — it has `minGapTicks = 960` (2 beats)
specifically to avoid micro-splits. `coalesceShortSameRootRuns` cannot rescue these because
the oracle-identified roots differ across the micro-regions (different incomplete tone sets).

**Dead end recorded:** changing `collectRegionTones`'s `noteEnd <= startTickInt` to `< startTickInt`
does not help — the boundary-touching predecessors are other chord tones (C, Eb; G, B), not
the root. The root hasn't attacked yet. Do not retry this fix.

In the **sibling regions where the DCML root sounds**, the oracle actually PREFERS the DCML
root (AbMaj7 raw 2.55 > Eb/Ab 2.33; F#7 raw 2.85 > C#m/F# 2.83). The wrong root prevails
ONLY because `rootContinuityBonus` +0.40 (fed by the wrong-root micro-region) tips it.

Gate R is structurally inapplicable: both present-root wrong readings carry inversion bonuses
(`basisDep > 0`: Eb/Ab = 0.90, C#m/F# = 1.40), so Gate R's `basisDep ≤ 0` guard correctly
spares them.

**Fix path: Phase E only. All gate approaches exhausted.**

Phase D dead ends (all 2026-06-09, documented in `docs/redesign_plan.md` Step 4):
1. `noteEnd <= startTickInt` → `< startTickInt` backward-walk fix: adds C/Eb not Ab; falsified.
2. External short-region merger: 0 qualifying runs (inline merge already fuses arpeggio slices).
3. Re-analysis of inline-merged aggregate with run-opening context: tried, reverted, corpus regressions.
   Full report: `cc_phase_d_merger_report.md`.

Phase E predecessor-confidence gate dead end (2026-06-09, `cc_phase_e_predecessor_survey_report.md`):
No threshold on `previousWinnerScore`, `previousWinnerMargin`, `previousDistinctPcs`, or
`previousWinnerRootPcWeight` separates the Δ=+7a arpeggio predecessors from legitimate
continuations. The rcb source is correctly confident about a transient (rootW 0.25–0.50,
score 3.05–3.30); Mozart Alberti control sits at rootW 0.00, below both Δ=+7a predecessors —
any gate that catches Δ=+7a also fires on correct continuations. Reconfirms Iter-98.

**What this means:** confidence can't encode "right now, wrong in 240 ticks." The fix requires
inter-region revision (Phase E): when the next region's evidence contradicts the committed
predecessor identity, revise the predecessor. This is architectural, not a gate.

Do NOT attempt further rcb gates. Full findings in `cc_deltaseven_7a_diagnostic_report.md`,
`cc_phase_d_investigation_report.md`, `cc_phase_d_merger_report.md`, and
`cc_phase_e_predecessor_survey_report.md`.

**Δ=+7b — correct predecessor, oracle tie broken by bonus (`contFired=1`): bwv245.28, bwv296, bwv320**
The predecessors are **correct, confident** chords (Bm=ii, D=vi, Gm=ii) — not sparse
or wrong. The bonus fires legitimately from a correct predecessor, then tips a
near-vertical-tie in the NEXT region the wrong way. Failing region scores:
bwv245.28/bwv296/bwv320 all show ~1.92 vs ~1.92 (exact or near tie in vertical oracle).
The old root (B, D, G) is still a real chord tone in the new PC set — the oracle cannot
distinguish "continued root" from "new V6 harmony" on vertical evidence alone. The bonus
is the sole tiebreaker. The correct reading requires voice-leading resolution context
(V6 resolving upward vs. ii lingering) — **Phase E territory.**

**Predecessor-confidence scaling approach: falsified.** Predecessors have pcWeight
0.60–0.82 (not 0.0); mozart_k280 control predecessor has pcWeight 1.00 (the highest
of the set). No (pcWeight, margin, distinctPcs) threshold separates the wrong cases from
the correct Alberti control. Full data in `cc_deltaseven_predecessor_report.md`.

**CC's proposed bass-aware gate: Iter 98 echo — do not attempt without explicit mozart test.**
CC proposed: withhold bonus when candidate is non-root-position (`bassPc ≠ rootPc`)
AND bass has moved (`bassPc ≠ previousBassPc`). This adds one condition to Iter 98's
rejected "inversion-aware refinement" (`bassPc ≠ rootPc` alone). The extra condition
does not save it: in Alberti-bass textures the bass moves to a different chord position
on every beat, so `bassPc ≠ previousBassPc` fires on both the wrong cases AND the
correct mozart continuity. Same dead end. If this is ever re-investigated, the mozart_k280
pipeline-snapshot test must be run before any commit.

**⚠ bwv320 m27 RE-DIAGNOSIS RETRACTED (2026-06-04):**
The "slash-synthesis" re-diagnosis above was WRONG. The diagnoseChord dump
used in C3/C4 characterisation omits temporal-context bonuses (rootContinuityBonus,
w_seq, w_dim) and uses legacy single-bass path — it falsely showed G/E as having
no template support. In reality, G major (root=G, bass=E) IS in the template loop
(rank 15 at score 1.52); rootContinuityBonus adds +0.40 because the preceding
sparse 2-PC Gm slice (tick 36960) set previousRootPc=7. Final score 1.92 beats
Cmaj 1.90 by exactly 0.02. This is the original Iter 98 diagnosis (fully correct,
documented in regionanalyzer.h and the Iter 98 dead-end section above). The Δ=+7
C2 entry below is also corrected.

**Remaining 16 cases (BIR=false=16 after Sub-9a fix) — fully characterised 2026-06-08:**

| Category | Count | Cases | Status |
|---|---|---|---|
| Δ=+7a: arpeggiation segmentation + rcb cascade | 2 | bwv102.7, bwv261 | **Phase E only** — Phase D fully exhausted (3 dead ends); oracle correct in present-root slice without rcb; rcb from wrong-root arpeggiated predecessor is the sole blocker |
| Δ=+7b: correct predecessor, oracle tie broken by bonus | 3 | bwv245.28, bwv296, bwv320 | ✅ **FIXED by Gate R** (`638ced1c12`) |
| Evidence-absent (DCML root not in pcs — genuine) | 2 | bwv17.7, bwv245.17 | Phase D only |
| Absent-OUR-root (DCML root IS present — actionable) | 3 | bwv14.5, bwv174.5, bwv301 | **Dead end — absent-root guard tried (2026-06-08) and reverted (net regression: 2 fixed, 4 broken). See below.** |
| B4 template tie (6th/m7 ambiguity) | 1 | bwv381 | Phase B4 (needs investigation) |
| Sus/quartal/whole-tone placeholder | 3 | bwv245.40, bwv422, bwv45.7 | Structural — no fix |
| Segmentation (region too wide) | 2 | bwv269, bwv432 | Complex — low priority |

**Segmentation cases (bwv269, bwv432) — characterised 2026-06-04:**

- **bwv269 m15** (t=20640–22080, 1440 ticks = full 3/4 measure): Analyzer emits D/F# Major.
  DCML has 4 events in this measure: V6 + V6/5 + I + viio6 (D/F#, D7/F#, G, F#°/A). F# is
  in the bass throughout, so the bass-run suppresses splits; Pass 2b doesn't find internal
  boundaries. The merged pcs={C,D,F#,A} is the union of all 4 events; G (DCML's beat-2 I)
  is entirely absent from it. Root cause: greedy-expand / Pass 2b doesn't split within a
  same-bass run even when the harmonic content changes.

- **bwv432 m3 b3.5** (t=5520–6480, 960 ticks = 2 beats, crosses barline): Analyzer emits
  Am/E Minor. DCML has 3 events: viio7 + i + V2 (E°7, Em, D7). Em's chord tones G and B
  fall out of the merged pcs; Am matches {A,C,E} with 2/3 present (C,E). Root cause: same
  over-merging pattern; viio7 → i boundary not detected.

**Sub-9b case (bwv14.5) — post-scoring absent-root promotion (2026-06-04):**

⚠ **Initial "Δ=+7 rootContinuityBonus" re-classification was WRONG — retracted.**
CC batch dump confirmed `previousRootPc = 10 (Bb)`, not 7 (G). rootContinuityBonus
fires on Bb-rooted candidates only (+0.40 → Bb major ~3.185), not on Gm.

**Actual mechanism (identified 2026-06-04):**
Joint scoring winner = Bb major (score ~2.785 base, ~3.185 with rootContinuityBonus).
All three emitted alternatives (Gm/Bb, Am/Bb, Gb+/Bb) have roots NOT in pcs
and score **below the 75% diagnostic threshold (2.089)** — meaning they are not in
the pre-context top 23 candidates at all. Some **post-joint-scoring pass** is
replacing Bb major with Gm/Bb. Gm/Bb score=2.660, root G absent from pcs.

The bass=Bb. All three alternatives share bass=Bb and have Bb as the 3rd of their root:
Bb = m3 of Gm (rootPc=7), Bb = M3 of Gb+ (rootPc=6), Bb as NCT of Am (rootPc=9).
This is an inversion-correction-style pass that asks "what chord could Bb be the third of?"
— then promotes a root-absent result over the correct Bb-rooted winner.

**Status: undiagnosed residual — investigation closed 2026-06-04.**

CC ran three diagnostic rounds (batch JSON dump, gate code audit + guard attempt, debug
print). Results:
- All known post-joint-scoring gates (B/C/D/E/F/G-E/H/I/J/K/L, Iter 91) were ruled out
  (all require quality conditions Bb major doesn't satisfy).
- An absent-root guard on the inversion-deduction block (L2839–2880) was tried and
  reverted: had no effect on bwv14.5 (the deduction block's `bestAltIdx` pointed at D
  Dom7, not Gm) but caused 5 snapshot regressions on legitimate cases.
- Debug print approach was issued but not yet reported; even so, the scope is clear:
  the Gm/Bb result likely comes from a **Pass 2/2b sub-region call** with different
  (smaller) pcs where G may actually be present, not from the parent-region gates.
- Score image (user-annotated) confirms bwv14.5 has at least two additional issues
  beyond m5 (opening-measure rootContinuityBonus stickiness). Even a correct m5 fix
  would leave a significantly wrong analysis overall.

**Root cause fully characterised (2026-06-04 debug print):**
The Gm/Bb result comes from a **sub-region analyzeChord call** with pcs={C,D,Bb}
(3 tones, distinctPcs=3, bass=Bb2 MIDI 46, context non-null). E from the parent
region (pcs={C,D,E,Bb}) was dropped on entry to this sub-region. G is absent from
the sub-region pcs as well — this is a genuine absent-root Minor-template win, not
a region-alignment artifact. Gm/Bb beats Bb major because F (Bb's 5th) is also
absent, and inversion-context bonuses tip the balance toward the first-inversion
reading. A general absent-root winner guard is the correct conceptual fix but the
one attempt (inversion-deduction-block guard, L2839–2880) caused 5 snapshot
regressions without affecting this case. Targeted fix requires identifying the
exact sub-region caller in regionanalyzer and scoping the guard narrowly.

**Decision: re-opened (2026-06-08 step-back). Previous closure was premature.**

The previous attempt failed because the guard was placed in the inversion-deduction
block (L2839–2880), which is the wrong location. The correct location is the
**winner-selection pass in `applyHarmonicFunction`**: reject a winner whose root PC
weight ≤ extensionThreshold when a within-margin present-root alternative exists.
Gate J is not a conflict — Gate J only fires when the dominant root IS present above
threshold (mutually exclusive conditions).

**3 Baroque target cases for the absent-root guard (reclassified 2026-06-08):**
- bwv14.5 Sub-9b (confirmed): root G absent from {C,D,Bb} sub-region. Already characterised above.
- bwv174.5: pcWeights {B:.6, Gb:.2, Ab:.2} — our root E absent; DCML root G#=Ab IS present (it's the bass).
- bwv301: pcWeights {B:1.25, D:1.25, A:1.05, C:.25, Ab:.2} — our root G absent; DCML root B strongly present (1.25).

These three were previously conflated in the "Evidence-absent (DCML root not in pcs)"
bucket. bwv174.5 and bwv301 are absent-OUR-root cases (DCML root IS in pcs; we emit a
root that is absent). Reclassified 2026-06-08.

1 Jazz target case: bwv45.7 (dim→dom absent-root, partial — Sus/quartal bucket by
primary mechanism, but absent-root guard would partially address it).

**Absent-root guard outcome (2026-06-08 — dead end, reverted):**

Guard implemented in `applyHarmonicFunction` (after `chosenPerBass` sort). Condition:
`pcWeight[winnerRootPc] == 0.0 AND distinctPcs >= 3 AND in-group alternative within
kAbsentRootGuardMargin=0.35`. Result:

| Case | Outcome |
|---|---|
| bwv301 (primary target) | ✅ Fixed |
| bwv269 (bonus) | ✅ Fixed |
| bwv174.5 | ⟲ Lateral — E/G# → B5, still wrong |
| bwv14.5 | ❌ Not reached (sub-region caller not the guard location) |
| bwv227.1 | ❌ New regression — DCML-correct absent-root reading (rootless E) |
| bwv342 | ❌ New regression — DCML-correct absent-root reading (rootless E) |
| bwv10.7 | ❌ Cascade regression (upstream root change → previousRootPc → rcb) |
| bwv337 | ❌ Cascade regression (same mechanism) |

Net: Baroque BIR=true +2, 6 snapshot goldens drifted. **Reverted entirely.**

Root cause: the premise "absent root ⇒ wrong reading" is false corpus-wide. bwv227.1
and bwv342 are DCML-correct absent-root readings. The cascade problem is structural —
any guard that changes a committed root poisons `previousRootPc` for all downstream
regions. These 3 cases (bwv14.5, bwv174.5, bwv301) remain open; bwv301 and bwv14.5
may be addressable only at Phase E or with a much more targeted sub-region guard.

CC note: `tools/dump_bir_cases.py` left as untracked helper (safe to keep or remove).
CC memory: `project_absent_root_guard_rejected.md` records the dead end.

**Score image (user-annotated, 2026-06-04):** Additional errors visible in the opening
measures (Gm read for Cm/Eb and G7/B at m1-2). This IS likely rootContinuityBonus from
the Gm pickup (different region, different previousRootPc context than m5). Those errors
are a separate Δ=+7 manifestation and accepted as Phase E residuals.
Roman numeral labeling errors (G/D → "I⁶₄" should be "V⁶₄") are downstream artifacts.

**Δ=+7 cluster (5 cases incl. bwv320) — NOT fixable with current tooling.**
All are rootContinuityBonus mis-fires on sparse predecessors. Same Iter 98
dead end. Do not attempt. Phase E only.

**Do NOT add a negative-margin guard** — would break Gate J and all other
intentional backward-swap gates (B/C/D/E/F/G/H/I/K/L, Iter 91).

New tooling: `tools/characterise_bir_false.py` (reusable BIR=false delta-group
analyser). Raw output: `/tmp/bir_false_char.txt` (uncommitted).
Diagnose dumps: `/tmp/bwv356_diag.txt`, `/tmp/bwv320_diag.txt`.

---

### Phase D — Voice-leading / non-harmonic tone model (high impact, higher complexity)

This is the deepest missing piece: without it the PC set fed to template matching is
always "dirty" (passing tones, suspensions, ornaments all contaminate it). Every
downstream layer currently compensates case-by-case rather than fixing the root input.

**D1. Non-harmonic tone classification**
Before tone collection feeds the scorer, classify tones as structural vs non-harmonic
(passing, neighbor, suspension, appoggiatura) using duration, metric position, and
voice-leading interval. Weight non-harmonic tones down or exclude them from PC set.
This unblocks many gate/bonus simplifications downstream.

**D2. Multi-voice / register awareness**
Assign voice roles (bass, tenor, alto, soprano) and weight evidence accordingly. Bass
voice carries harmonic root information; inner-voice passing motion should not dominate
root inference. Also needed for correct figured-bass analysis.

---

### Phase E — Harmonic function layer (architectural, depends on D being stable)

Introduce as a thin shell first (gates migrate in), then grow capabilities.

**E1. Introduce harmonic function layer shell** ✅ *DONE — commit `dd29a04967`*
`src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}` — `HarmonicFunctionContext`
(keyFifths, keyMode, previousRootPc, nextRootPc) + `applyHarmonicFunction()` no-op.
Added to `composing_analysis` target_sources (consistent with analysis-subdir pattern;
no separate CMake module). Three call sites in `regionanalyzer.cpp` gated on
`!prefs.explorationMode`: Pass 1 L457-464 (after BOTH refinement passes — fully refined
winner); Pass 2 L658-665; Pass 2b L844-851. `docs/scoring_model.md` §10 added.
Zero behavioral change. 407/407, 52/52, 11/11 — byte-identical to baseline.

**CMake note for E2/E3:** The function files are compiled into `composing_analysis`,
not a separate library. E2/E3 should continue this pattern unless there is a specific
build-isolation reason to extract a separate module.

**E2a. Move progression-signal lambdas to function layer** ✅ *DONE — commit `80a7adf32e`*
`rootContinuityBonus`, `wSeqBonus`, `wDimBonus` are now free functions in
`harmonicfunctionlayer.{h,cpp}`. `chordanalyzer.cpp` calls them via thin lambda
wrappers from their existing sites. `kWSeq` (0.20) and `kWDim` (0.15) constants
moved to the function layer header. The `w_dim` dual-scoring structure (two parallel
accumulators + post-bonus quality guard) is untouched. Code organisation only —
execution order and call sites unchanged. 407/407, 52/52, 11/11 — byte-identical.

**E2b. Expose scoring snapshot** ✅ *DONE — commit `710d8dba12`*
`ScoringCell` / `ScoringSnapshot` structs added to `harmonicfunctionlayer.h`.
`prefs.captureScoringSnapshot { nullptr }` added to `ChordAnalyzerPreferences`.
When non-null, `analyzeChord()` populates pre-step-bonus scoring cubes for both
the with-wDim and without-wDim variants (all bassCandidates × 12 rootPcs × N
templates). Also records `distinctPcs`, `acceptedWithWDim`, `chosenBassPc`,
`winnerBassPcWith/Without`. All existing callers pass nullptr — hot path unchanged.
407/407, 52/52, 11/11 — byte-identical to `80a7adf32e`.

**E2c. Function-layer plumbing** ✅ *DONE — commit `20f992a5e7`*
Infrastructure for signal migration: `tiePriority` added to `ChordIdentity`;
`bassTpc` and `jointScoringEnabled` added to `ScoringCell`/`ScoringSnapshot`;
`suppressProgressionSignals { false }` added to `ChordAnalyzerPreferences`.
`applyHarmonicFunction()` signature extended (candidates vector, chosenResult,
snapshot*, prefs*). Refinements reordered to run AFTER function layer at all
three regionanalyzer.cpp call sites. Function layer still receives nullptr →
no-op. 407/407, 52/52, 11/11 — byte-identical to `710d8dba12`.

Commit 2 (enable suppression) attempted and REVERTED. Two blockers found:
(1) Pass B (step bonus ±0.20–0.35) flips winners; function layer must replicate
it. (2) Cross-bass: suppressed-signal rawCandidates is one bass only; true
with-signals winner may be absent. E2d investigation underway.

**E2d. Scoring oracle / competition pipeline segregation** ✅ *DONE — commit `2917ec7571`*
Three failed incremental attempts (v2, v3, v3b) revealed the root cause: `applyHarmonicFunction`
was a hand-written replica of `analyzeChord`'s competition loop, and the replica was always
incomplete. A fourth attempt would have found more missing pieces. CC's independent architectural
review confirmed: the competition loop must live in exactly one place.

Fix: move the competition loop entirely to the function layer.

`analyzeChord` is now a **scoring oracle** — evaluates all (bass, root, template) cells,
computes metadata, packs into `ScoringSnapshot`, then calls `applyHarmonicFunction` internally.
`applyHarmonicFunction` is now the **competition pipeline** — owns all 7 steps: (1) rescore
cells with progression signals (rcb, wSeq, wDim), (2) Pass B step bonuses, (3) per-bass
quality guard, (4) cross-bass winner selection, (5) threshold, (6) build results[], (7) fill
gateCtx completely from the winning bass.

`suppressProgressionSignals` and `captureScoringSnapshot` fields deleted from
`ChordAnalyzerPreferences`. Three explicit `applyHarmonicFunction` calls in
`regionanalyzer.cpp` deleted (now called internally by `analyzeChord`).

Equivalence harness: 0 divergences (214/214 match; was 13 at baseline).
408/408, 52/52, 11/11 — byte-identical. BIR: Baroque 25/16, Jazz 36/10.
Architecture documented in `docs/scoring_model.md` §10/§11.

*Cleanup note:* Equivalence harness (`equivalence_harness_test.cpp`) is now tautological —
both pipelines are the same path. Safe to remove in a cleanup pass; not urgent.

**E3. Gate decoupling + G-E phantom fix** — Tasks 2+3 committed `f9ba22157d`; Task 1 deferred

Original E3 goal ("move Gates A–D, Gate J, dim7CharacteristicBonus to function layer")
was overtaken by E2d: all gates already live in the standalone `applyPostScoringGates`
called after `analyzeChord`. Investigation (2026-06-07, `cc_e3_investigation_report.md`)
found three real actionable items instead:

1. **Q6 coupling defect — DEFERRED (Task 1):** Gates H, I, J, K, L are nested inside the
   outer `inversionSuspicionMargin > 0 && inversionBonusReduction < 1.0 && results.size() >= 2 && distinctPcs >= 3`
   guard, but are logically independent of the bias correction. Prefs-only decouple
   (removing only the two prefs conditions while keeping `distinctPcs >= 3`) IS byte-
   identical for all current corpus runs. Dropping `distinctPcs >= 3` is NOT byte-identical
   — Schumann kinderszenen_n01 counterexample: 2-PC dyad slivers (distinctPcs=2) trigger
   structural gates when that condition is absent. `distinctPcs >= 3` is load-bearing.
   The latent bug has no urgency (all active presets have inversionSuspicionMargin=0.70);
   deferred indefinitely. When revisited: prefs-only decouple only — keep `distinctPcs >= 3`.

2. ✅ **G-E phantom HalfDim: COMMITTED (`f9ba22157d`):** Gate G-E appended a HalfDim from
   `rawCandidates` even when none of its four sub-gates fired, leaving a phantom in the
   alternatives list. Fix: `halfDimPulledFromRaw` flag + `results.pop_back()` if no sub-gate fires.

3. ✅ **Float literals → named constants: COMMITTED (`f9ba22157d`):** `0.45f`/`0.20f`/`0.35f`
   in Gates I/K/L are now `kGateIMargin`/`kGateKMargin`/`kGateLMargin`.

Note: temporal gates (B, C, D, G-B/C/D, H-B/C/D) cannot move into `applyHarmonicFunction`
byte-identically — they run after `applyIter8691Pedal` by design (pedal pass mutates
results[] that these gates read). File relocation to `harmonicfunctionlayer.cpp` would
require promoting `RawCandidate`/`buildChordResult`/`PostScoringGateContext` types.
Neither option is the right E3 scope.

`dim7CharacteristicBonus` is correctly placed in the scoring oracle's per-cell loop —
no progression context, rotation-selection only. Moving it was a misclassification.

**E4. Cadence detection**
Strongest harmonic punctuation in tonal music; most reliable signal for confirming key
and functional labels. Feeds both key detection (a PAC confirms the key) and functional
labeling (V→I resolution ground truth). Required before E5.

**E5. Functional labeling completeness**
Augmented sixth chords (It+6, Fr+6, Ger+6 — structurally distinct from dom7♭5 despite
PC overlap), Neapolitan (♭II / N6), borrowed chords / modal mixture (♭VII in major, iv
in major), extended tonicization chains beyond V/x and vii°/x.

---

### Phase F — Advanced / long-term

**F1. Confidence / uncertainty quantification**
Surface the score margin between top candidates as a meaningful signal. Flag ambiguous
regions rather than silently committing to a potentially wrong answer.

**F2. Harmonic rhythm modelling**
A chord lasting a full measure is structurally different from one lasting an eighth note.
Model harmonic rhythm as a structural parameter to improve segmentation decisions and
absorption logic.

**F3. Style / genre pattern recognition**
ii-V-I cycles, Baroque descending-fifth sequences, Neapolitan approach patterns. A
pattern layer above the function layer that uses known progressions to disambiguate
locally ambiguous chords.

**F4. Quartal / quintal templates**
{0,5,10}, {0,5,10,3} etc. Low priority for current Baroque/Jazz corpus but needed for
20th-century and contemporary repertoire.

---

### Architectural note — the long-term target stack

```
Tone collection
      ↓
Key / mode detection          (A1 — fix Baroque partial-signature; E4 cadence feeds back)
      ↓
Template scoring              (B — add mMaj7, aug7, dim7; D — clean PC set via NHT model)
      ↓
Harmonic function layer       (E — gates migrate here + cadence + functional labels)  [NEW]
      ↓
Segmentation / absorption     (C1 schumann fix; C2 bwv320 merge fix)
      ↓
Labels / output               (A3 roman-numeral validation; F1 confidence)
```

---

## Architectural redesign — layered comprehensive evidence flow (updated 2026-06-10)

Full detail: `docs/redesign_plan.md` and `ARCHITECTURE.md §2.14`. Summary here.

**Architecture decision (2026-06-09, updated 2026-06-10):** Single comprehensive pass
through properly layered components. All evidence is present at analysis time;
a single pass with symmetric backward/forward context is sufficient. Iteration is not a
design premise. Accumulating gates to compensate for missing context is the wrong
response — build the evidence picture (symmetric forward context alongside backward)
and unify the commit paths. Phase E completes that evidence picture and removes
all internal dual-paths. BIR re-calibration happens after the architecture is stable.

**Key implication:** the current 13 BIR=false residuals require richer evidence, not
more gates. The Δ=+7a cases require Phase D (arpeggio-aware segmentation) + Phase E
(inter-region revision when successor evidence contradicts the committed predecessor).
B1 mMaj7, A2 dominant-in-minor require Phase E cadence confirmation. Segmentation cases
require targeted structural fixes. Do not add compensating gates — add the missing evidence.

**The principle:** each layer should pass its full evidence alongside its committed
decision — not compress to the decision alone. Downstream layers must calibrate
how much to trust the upstream commitment. A wrong upstream commitment received
without confidence metadata is treated as ground truth: this is "passing a lie."

### What E2d already achieves

The oracle / pipeline split (E2d, `2917ec7571`) means **within-region deferred
commitment is already implemented.** `analyzeChord()` is a pure scoring oracle;
`applyHarmonicFunction()` applies all progression signals and selects the winner.
Commitment happens after functional signals — not before. The architecture is more
advanced than the Phase E description implies.

### The gap: inter-region channel is thin

After a winner is selected, `advanceTemporalContext` writes only
`previousRootPc / previousBassPc / previousQuality` into `ChordTemporalContext`.
Then `fnCtx` construction forwards even less to `HarmonicFunctionContext`:

```
fnCtx.previousRootPc = context ? context->previousRootPc : -1;
fnCtx.nextRootPc     = context ? context->nextRootPc     : -1;
fnCtx.previousBassPc = context ? context->previousBassPc : -1;
fnCtx.nextBassPc     = context ? context->nextBassPc     : -1;
```

Winner score, winner margin, predecessor root pcWeight — none forwarded.
`rootContinuityBonus` applies a flat +0.40 regardless of predecessor confidence.
A wrong committed predecessor receives the same reward as a correct one.
**This is the mechanism behind the entire Δ=+7 rootContinuityBonus cluster.**

### Wiring gap — fields already computed, not forwarded

`ChordTemporalContext` already has these fields; none reach `HarmonicFunctionContext`:

| Field | ChordTemporalContext | HarmonicFunctionContext |
|---|---|---|
| `previousQuality` | ✅ | ❌ |
| `recentRootPcs[3]` | ✅ | ❌ |
| `consecutiveBassStepwiseCount` | ✅ | ❌ |
| `regionMetricWeight` | ✅ | ❌ |
| winner score / margin | ❌ | ❌ |
| predecessor root pcWeight | ❌ | ❌ |

Forwarding the first four costs nothing (no new computation, just wiring).
The last three require new fields in `ChordTemporalContext` populated in
`advanceTemporalContext`.

### Key layer gap — status (2026-06-08)

`resolveKeyAndModeRanked` produces a ranked distribution of key candidates.
Both call sites in `regionanalyzer.cpp` (L305, L411) discard the list immediately
with `.front()`. Every downstream term (template scoring, diatonic root bonus,
scale construction) receives the key as a committed point estimate.

**The Corelli op01n08d "G minor instead of C minor" failure is already fixed** by
commit `81978321e3` (Option B Baroque partial-signature correction, 2026-06-03).
The resolver now returns C minor at rank 0 for every region.

Additionally, `KeyModeAnalysisResult.normalizedConfidence` is unreliable as a
scaling signal: `promoteWinnerInPlace` (keyresolver.cpp:311-321) re-ranks via
hysteresis/declared-mode without recomputing confidence, producing 0.025–1.00 for
the same correctly-keyed piece. Any future key-confidence design must define a new
metric (e.g. raw score gap between rank-0 and rank-1, post-promotion).

**Step 3 (key-as-distribution) is shelved** — no confirmed live target in the
51-piece corpus. See `cc_step3_key_investigation_report.md`.

### Failure case analysis — what this fixes and what it doesn't

*(Updated 2026-06-08 after predecessor-confidence diagnostic.)*

| Case | Root cause | Redesign effect |
|---|---|---|
| Δ=+7a bwv102.7, bwv261 (arpeggiation + rcb cascade) | Oracle correct in present-root slice without rcb (2.55 > 2.33); sole blocker is rcb +0.40 from wrong-root arpeggiated predecessor; Phase D exhausted (3 dead ends — aggregate weights still prefer Eb) | **Phase E only** — detect arpeggiated predecessor, suppress/reduce rcb |
| Δ=+7b bwv245.28, bwv296, bwv320 (correct predecessor, oracle tie) | Correct predecessor; near-tie in oracle broken by bonus toward old root | Phase E only — needs voice-leading resolution signal |
| bwv301 G-absent winner | Vertical scoring asymmetry (rootless triad over-rewarded) | Remains — absent-root guard addresses symptom |
| B1 mMaj7 leading-tone | Needs voice-leading resolution signal | Partially moves — still needs Phase E |
| B3 dim7 rotation | PC-identical rotations, no distribution helps | Unchanged |
| Corelli op01n08d key | Key layer commits with no distribution | **Already fixed** by `81978321e3` — not a live BIR=false case |

**The Δ=+7 cluster is correctly labelled Phase E.** The predecessor-confidence approach
was falsified by the 2026-06-08 diagnostic: predecessors have pcWeight 0.60–0.82 (not
0.0), and the mozart control predecessor has pcWeight 1.00 — the highest of the set.
No (pcWeight, margin, distinctPcs) threshold separates wrong cases from correct Alberti.
See `cc_deltaseven_predecessor_report.md` for full data.

### Redesign sequence

1. **Forward free ChordTemporalContext fields to HarmonicFunctionContext** (no new
   computation — just wiring `previousQuality`, `recentRootPcs`, etc. into `fnCtx`).
   Files: `harmonicfunctionlayer.h` (struct), `chordanalyzer.cpp` (fnCtx construction).

2. **Add predecessor confidence fields** (infrastructure for future Phase E signals).
   New fields in `ChordTemporalContext`: `previousWinnerScore`, `previousWinnerMargin`,
   `previousWinnerRootPcWeight`, `previousDistinctPcs`. Populated in
   `advanceTemporalContext`, forwarded to `HarmonicFunctionContext`.
   **Note:** Does NOT fix the Δ=+7 cluster (diagnostic falsified that premise). Useful
   as infrastructure for Phase E cadence/quality-aware bonus scaling.

3. **Key-as-distribution — ⛔ SHELVED.** Motivating case (Corelli op01n08d) already
   fixed by `81978321e3`. No confirmed live target in corpus. `normalizedConfidence`
   structurally unreliable as scaling signal. See `docs/redesign_plan.md` §Step 3.

4. **Phase E proper.** Cadence evidence, phrase context, functional labeling. Unblocks
   B1 (mMaj7), A2 (dominant in minor), Δ=+7b (voice-leading resolution).

---

## Iter 78 fixes (all committed, do not re-implement)

**Fix A** — `notationharmonicrhythmbridge.cpp`, `absorbShortRegions` lambda:
Short regions are only absorbed into the previous region when they share the same root
(`sharesPrevRoot`). A differently-rooted short region keeps its own boundary.

**Fix B** — `chordanalyzer.cpp` line ~129, `pitchClassName()`:
G# → Ab flattening is exempted at `keySignatureFifths == 0` (A minor), where G# is
the leading tone. Condition: `pc == 8 && keySignatureFifths < 3 && keySignatureFifths != 0`.

**Fix C** — `chordanalyzer.cpp` lines ~1762-1766:
Augmented template score ×0.5 when `distinctPcs <= 2` and root PC weight is at or
below `extensionThreshold`. Prevents root-absent 2-PC guesses winning as Augmented.

---

## Iters 79–84 — all committed

- **Iter 79** (`cbd7230c1f`) — augmented bare-root guard + qualitySuffix Dim/HalfDim fix
- **Iter 80** (`b4a375db45`) — refreshed 7 stale pipeline snapshot goldens
- **Iter 81** (`9d2a70cef4`) — removed dead Jaccard code; notation tests now 52 total / 50 passing
- **Iter 82** (`57511f012f`) — Gates E/I absent-root guard; BIR=false=118, BIR=true=4, Jazz BIR=false=7
- **Iter 83** (`1c57ebcac2`) — batch path anchor end-tick fix (port Iter 77 Fix B)
- **Iter 84** (`4da8252c9e`) — R4 narrow fix: G# leading-tone exemption extended to keyFifths=1 (A melodic minor regime)

## Iter 84 detail (do not re-implement)

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`, lines ~117–153

`pitchClassNameFromTpc()` had a G# (pc=8) exemption from Ab-normalization at `keyFifths==0`
(Iter 78 Fix B, for A natural minor). A melodic minor ("Amel") maps via `resolveToFifths()`
to its Dorian parent at `keyFifths=1`, falling outside the exemption → G# was spelled "Ab".

Fix: added `&& keySignatureFifths != 1` to the normalization condition, and extended the
TPC-disambiguation block to also fire at `keyFifths==1 && pc==8` (so flat-authored Ab with
tpc≤14 in that regime is still correctly spelled flat).

Result: bach_chorale_003 — 3 chord symbols corrected (Abm7b5/B→G#m7b5/B, E/Ab→E/G# ×2).
bach_chorale_003 golden refreshed. BIR unchanged (BIR operates on root_pc/bass_pc).

**Deferred — R4 family B (chorale_137, later iteration):**
- pc=6 (F#/Gb): no TPC-honor block exists for pc=6 at all; unconditionally returns Gb at keyFifths<0
- Flat-authored Ab bass in V/V context (tpc=10 in chorale_137 m2): heavier "chord-3rd-of-major-triad" override, out of scope

---

## Iters 85–89 + DCML comparator — all committed

- **Iter 87** (`2dd2f35c17`) — bass-b7 post-merge re-stamp in batch_analyze.cpp
  (`analyzeScore` merge discarded MinorSeventh extension stamped by Iter 86; post-filtered
  re-stamp pass at batch_analyze.cpp:1846–1880 fixes 281 of 293 b7-bass slash-chord cases)
- **Iter 88** (`bea00f3482`) — honor sharp F# TPC for pc=6 in flat keys (extends
  TPC-disambiguation block to fire at `keyFifths<0 && pc==6`; Gb→F# in D/F# and similar
  contexts)
- **Iter 89** (`2085f11322`) — honor sharp G# TPC for pc=8 across flat and mildly-sharp
  keys (removed pc=8 from Iter 78 flattening block; added `keyFifths<0 && pc==8` and
  `keyFifths==2 && pc==8` to TPC-honor block; survey script `tools/survey_pc8_flat_authored_bass.py`)
- **DCML comparator** (`eefa412b6f`) — new time-overlap comparator in compare_analyses.py
  (mode='time-overlap', lenient-OR-50% overlap threshold) + rerun_dcml_comparison.py
  re-aggregation driver. Old beat-snap 69.1% figure retired (biased +21pp). New primary
  metric: 47.8% weighted root agreement across 10 non-Bach corpora (DCML-anchored).
  Bach chorales: 64.9% overall, 87.2% chord-identity, 100% alignment.
  **Superseded:** the live baseline is now **53.8%** (regenerated 2026-05-20 at HEAD
  `a69a23e59b`; see "Current state" block above). The 47.8% figure is historical only.

**Iter 90 — shelved (no commit):**
122 wrong-root cases characterized (tools/analyze_wrong_root_iter90.py,
tools/iter90_wrong_root_characterization.txt). 84% are iii/III triad confusion — non-local
ambiguity. Both Variant A (+12 errors) and Variant B (+22 errors) regressed. Design note:
`docs/iter90_bass_as_root_promotion_shelved.md`. Future path: Iter 91, bridge-level
adjacent-context pass using nextRootPc/previousRootPc from ChordTemporalExtensions.

**Iter 91 — attempted and reverted (no commit):**
Temporal-context gate: when the winning chord's root is a third above the bass (iii/III
pattern), promote the bass-rooted reading from rawCandidates when `nextRootPc == bassPc`
(forward resolution signal). Tried both `previousRootPc OR nextRootPc` (too permissive —
fired on genuine I→I6 progressions) and `nextRootPc` only. Final result on `nextRootPc`
only: BIR=false 188→185 (−3), BIR=true 38→41 (+3) — net neutral at 226→226 total errors.
Reverted. Working tree clean at `2de18139c2`. Superseded by Iter 92 holistic design.

**Ground-truth QA session — 2026-05-16:**
Opened 5 DCML-annotated scores in MuseScore with GT and US labels injected side-by-side
(via `tools/inject_dcml_rn.py`). Visual review identified two distinct bugs causing
the bulk of BIR=false=188 errors:

- **Bug 1 — Passing-note bass contamination:** When the bass voice has two eighth notes
  within a beat window (e.g. G3 onset + F#3 passing), the lower-pitched passing note
  (entering mid-region) overrides the beat-onset structural note as bassPc. Mechanism
  confirmed by diagnostic: both G3 (MIDI 55) and F#3 (MIDI 54) appear in region
  [4800,5280) with equal pcWeight=0.20; F#3 wins because 54 < 55. This flips root
  inference (e.g. G major → Em/F# or Am/F# instead of correct G or G7).

- **Bug 2 — Incomplete slash chord beats complete root-position triad:** Given pitch
  classes {C,E,G} with C in bass, the template scores Em/C ~2.86 vs C major ~2.40 — a
  gap of ~0.46. Em/C "wins" even though B (the 5th of Em) is absent and C is not in Em.
  Root-position completeness is not rewarded. Seen on bwv310, bwv319, bwv103.6, bwv283.

**Iter 92 — committed (`80fe13b59b`):**
Joint (bass, chord) scoring with `w_complete` bonus (distinctPcs==3) and multi-bass
enumeration. Design at `docs/iter92_joint_bass_chord_scoring.md` (still authoritative
reference for the JOINT formula and follow-up scope). What landed:

- Struct fields added: `ChordAnalysisTone::onsetAtRegionStart` (bool) and
  `ChordTemporalContext::nextBassPc` (int, −1=unknown) in `chordanalyzer.h`.
- Joint enumeration loop in `chordanalyzer.cpp`: enumerate bass candidates from the bass
  register, score each (bass, root, template) triple = base score (bass-independent) +
  bass-dependent deltas (`appliedBassRootBonus`, `nonBassAdjustment`, inversion contextual)
  + `w_complete = +0.50` bonus when distinctPcs≥3 AND all three triad tones are present
  above extensionThreshold AND bass_candidate.pc == triad_root.
- Callers populated: `notationcomposingbridgehelpers.cpp::collectRegionTones` (onset flag),
  `notationharmonicrhythmbridge.cpp` and `tools/batch_analyze.cpp` (nextBassPc assignment).
- Pipeline snapshot goldens refreshed (10 of 11): bach_chorale_001/003/137,
  bach_bwv806_prelude/gigue, mozart_k279_1/k280_1, chopin_bi105_op30_1, corelli_op01n08a,
  schumann_kinderszenen_n01. Audited: clean Bug 2 fix patterns (D7/A→D7, FMaj7/E→FMaj7,
  F/C→F, G/C#→G, AMaj7/G#→AMaj7, E/B→E, E/G#→E, C/E→C, F/A→F). No regression patterns.
- BIR impact: Baroque BIR=false 188→46 (−142). Baroque BIR=true 38→41 (+3, bucket
  reclassifications). Jazz BIR=true 103→114 (+11). Jazz BIR=false 13→14.

**Iter 93 — committed (`f98586fa67`, plumbing only; Step 3b shelved):**

Landed: `collectRegionTones` (in both `notationcomposingbridgehelpers` and
`tools/batch_analyze`) gained an optional `parentStartTick` parameter (default −1 ⇒
falls back to `startTickInt` for un-split callers). Pass 2 / Pass 2b sub-region call
sites in `notationharmonicrhythmbridge.cpp` and `batch_analyze.cpp` pass the parent
region's startTick so the per-tone `trueAttackAtStart` flag is computed at full-region
scope rather than against the narrow sub-region boundary. `chordanalyzer.cpp` is
unchanged relative to Iter 92; the joint-scoring loop, the `w_complete` bonus, and the
`jointScoringEnabled` gate are intact. Baselines unchanged from Iter 92.

**Step 3b (`w_onset` / `w_passing` per-bass-candidate score deltas) — SHELVED:**

Three variants were attempted and all hit Baroque BIR=false hard stops:
- Symmetric (`+0.15` onset bonus, `−0.10` passing penalty): +7 BIR=false.
- Asymmetric penalty-only (`0` onset, `−0.10` passing): +4 BIR=false.
- Asymmetric + onset-gated (penalty only fires when at least one bass candidate has
  `onsetAtRegionStart=true`): +3 BIR=false.

Root cause: in Baroque polyphony the bass voice routinely moves mid-region to the
actual chord root (arpeggiated bass, melodic bass motion). The onset-position signal
is not a reliable proxy for "structural bass" in this corpus — the same signal that
would penalise a passing-note artefact also penalises a genuine arpeggiated structural
root. No further onset-position tuning is expected to clear this; the signal is wrong
for the corpus.

**Iter 94 — committed (`dbfe09fe6f` + STATUS backfill `a34b5c1e6c`):**

Iter 92's deferred Step 3c (`w_stepIn` / `w_stepOut` voice-leading bonuses) is now
active in `RuleBasedChordAnalyzer::analyzeChord`. Root-position candidates earn +0.10
when the bass moves by semitone or whole-tone from `context->previousBassPc` and +0.10
again on motion to `context->nextBassPc`. Parent-scope plumbing: bridge Pass 2 / Pass 2b
in `notationharmonicrhythmbridge.cpp` and the main loop in `tools/batch_analyze.cpp`
compute the predecessor / successor PARENT region's bass PC and override
`subCtx.previousBassPc` / `subCtx.nextBassPc` for each sub-region `analyzeChord` call
(the override happens AFTER the stepwise booleans, which intentionally remain
sub-region-scope for passing-tone / inversion signals, and BEFORE the call; the
post-call restore keeps the next iteration's stepwise boolean correct).

Four gates were required to keep the bonus safe — each motivated by a concrete
regression caught during iteration:

1. **`explorationMode` suppression** — new field `ChordAnalyzerPreferences::explorationMode`
   (default `false`). `greedyExpandSegmentation` sets it to `true` on every internal
   boundary-exploration `analyzeChord` call (Round 1 head/tail synthesis + Round 2 region
   scoring in `harmonicsegmenter.cpp::fillGap`). The bonus would otherwise bias
   sub-region bass selection toward stepwise candidates and redirect segmentation
   before the final per-region scoring pass runs.
2. **Root-position guard `candBassPc == cand.rootPc`** — the bonus is meant to reward
   "this chord's root moves smoothly in the bass line," not "this slash-chord's bass
   happens to step smoothly." Applying it to slash-chord bass caused a Jazz bwv430
   BIR=false +1 regression (a G#m7/F# bass stepping to a neighbouring bass gained
   credit even though its root G# was not the moving voice). Enforced both in the
   lambda body and in the Pass-B outer loop that skips non-root-position candidates.
3. **Corrected first-inversion-m7-family guard** — if any competitor in the same
   `perBass` block with quality in {HalfDiminished, Diminished, Minor7} sits at
   `(candBassPc - 3) mod 12` (i.e. its root is a minor third BELOW our bass, the
   first-inversion shape) AND scores within `kStepBudget = kWStepIn + kWStepOut + 0.01`
   of the candidate's unbonused score, both step bonuses are suppressed. Canonical
   case: Dm6 (candBassPc=2, rootPc=2) vs Bø7/D (competitor rootPc=11, bassPc=2) — the
   m7-family competitor's root is the minor third below our bass, not at our bass. The
   guard prevents the step bonus from tipping a fragile m6 root-position reading over
   an equally viable first-inversion m7-family reading on identical pitch evidence.
4. **Power-quality exclusion** — root+fifth-only templates are excluded outright. Five
   sparse-Jazz Tonic-on-strong-beat regressions (bwv20.7 m16b1, bwv227.1 m11b3,
   bwv245.40 m27b3, bwv384 m4b3, bwv422 m14b1) had Power `[Tonic]5` reads tip past
   viable triad reads when the bonus fired. Extending the exclusion to Suspended2/4
   caught a sus residual but regressed Jazz BIR=false (14 → 15) — beyond hard-stop
   scope, so the current cut is Power-only.

BIR impact (lenient-OR comparator):
- Baroque BIR=true 41→43 (+2, bucket reclassifications, not new errors)
- Baroque BIR=false 46→33 (−13, ~28% reduction)
- Jazz BIR=true 114→117 (+3)
- Jazz BIR=false 14 (flat)

Tests: 407/407 composing, 50/52 notation (same 2 pre-existing Corelli implode
failures), 11 passed / 1 skipped pipeline_snapshot — all 11 active goldens refreshed
(bach_chorale_001/003/137, bach_bwv806_prelude/gigue, mozart_k279_1/k280_1,
chopin_bi105_op30_1/2, corelli_op01n08a, schumann_kinderszenen_n01).

**Deferred — Iter 95 candidates (status after Iter 96):**
- **`w_onset` / `w_passing` via duration-weighting.** Still deferred — Iters 94–96
  continued harvesting BIR improvements without it. Reconsider only if a concrete
  failure pattern emerges that existing bonuses cannot reach.
- **`w_seq`** — landed as Iter 95. Done.
- **bwv320 Am 1-case residual.** Still deferred.

---

## Iter 96 — committed 2026-05-18

**Commits:** `0de94516ff` (code) + `7060f2c5db` (STATUS amendment)

**Change:** `w_dim` +0.15 bonus in `chordanalyzer.cpp`. New `wDimBonus` lambda
alongside `wSeqBonus`. Fires when a Diminished or HalfDiminished candidate's root
sits one semitone below `context->nextRootPc`
(`(nextRootPc - candRootPc + 12) % 12 == 1` — leading-tone resolution signal).

Gates: `jointScoringEnabled && !prefs.explorationMode && context &&
context->nextRootPc >= 0 && (quality == Diminished || quality == HalfDiminished)
&& distinctPcs >= 4`. No new plumbing — `nextRootPc` already populated by Iter 95.

Three variants were tried before committing:
1. **Loose (delta==1, no distinctPcs gate):** Baroque −3/0, Jazz +2/0.
   bwv296 m12 b4 direct misfire (3-PC region, G/B wrongly flipped to B°) +
   Corelli golden regression (F7/A → Adim dropping the structural 7th). Not committed.
2. **Tightened (delta==1, distinctPcs >= 4):** Baroque −3/−1, Jazz +1/0.
   bwv296 misfire and Corelli golden regression both eliminated by the gate.
   Jazz +1 residual is a cascade from an upstream w_dim fire (Cadd11, Major
   quality — not a direct w_dim misfire, not a hard stop). Committed.
3. **delta==2 variant:** not attempted — widening after delta==1 already produced
   misfires was expected to add more.

The `distinctPcs >= 4` gate intentionally suppresses the sparse-region tier.
Two improvements from the loose gate (`schumann bvo7→viio7/V` tick 480,
`chorale_003 Am→G#dim`) were inseparable from the misfires — both were
3-PC sparse regions where the bonus was a quality flip, not a rotation correction.
A future iteration may recover them by adding a rotation-only condition
(require the current winner to also be Dim/HalfDim).

**BIR impact (lenient-OR comparator):**

| Metric | Pre-96 | Post-96 | Δ |
|--------|--------|---------|---|
| Baroque BIR=true | 44 | 41 | −3 |
| Baroque BIR=false | 27 | 26 | −1 |
| Jazz BIR=true | 68 | 69 | +1 |
| Jazz BIR=false | 13 | 13 | 0 |
| **Total** | **152** | **149** | **−3** |

**Tests:** 407/407 composing, 50/52 notation (same 2 Corelli), 11/11 snapshot
(2 alt-only goldens refreshed: `bach_bwv806_gigue`, `schumann_kinderszenen_n01`).

**Deferred — Iter 97 candidates:**
- **α-variant: w_dim rotation-only** — add guard requiring the current winner to
  also be Dim/HalfDim before `wDimBonus` fires. Only the enharmonic rotation is
  in contest, not the quality. May recover `schumann bvo7→viio7/V` and
  `chorale_003 Am→G#dim` without the quality-flip misfires. Quick to try.
- **δ: sparse-minor diatonic quality prior** — when `distinctPcs <= 3` and the
  third is absent/weak, prefer the quality that the current key assigns to this
  scale degree. Directly fixes the 2 pre-existing Corelli notation failures
  (`CorelliOp01n08dOpeningAndSparseLateBeats`,
  `CorelliOp01n08dUserReportedChordTrackAudit`). Harder to gate safely.
- **β: P4-above mis-rooting** (~27 cases) — diffuse, no single fix, deferred.
- **γ: M2-above mis-root** (~17 cases) — diffuse, deferred.

---

## Standing rule — CC instruction preamble (MANDATORY, every single CC session)

CC starts with ZERO context every time. Every instruction to CC must open with:

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
> `C:\s\MS\build_and_test.md`
>
> **If this session touches scoring logic in `chordanalyzer.cpp`** (templates, bonuses,
> guards, gates, score matrices): also read `C:\s\MS\docs\scoring_model.md` before
> making any changes. The doc explains why each term exists and what invariants must
> not be broken. Any commit that changes scoring logic must also update that doc.
>
> **Current state:** Branch `master`, HEAD `f9ba22157d`, working tree clean.
> BIR baselines (lenient-OR): Baroque BIR=true=25, BIR=false=16; Jazz BIR=true=36,
> BIR=false=10. Hard stops: Baroque BIR=false ≤ 25, Jazz BIR=false ≤ 13.
> Tests: 407/407 composing, **52/52 notation (fully green)**, pipeline_snapshot
> 11/11 (1 skipped, no goldens touched).
> Mismatch report: Jazz 130 items; see chord_mismatch_report.txt.
> Roman numeral baseline (HEAD `f3e0f5f72c`, 9 non-Bach corpora, 61,233 regions):
> rn_agree=27.6% (16,905/61,233); corrected classifier: key_disagree=15.4%,
> quality_disagree=6.3%. Root_agree=49.3% parity check. Hard stop: rn_agree
> must not drop below 27.6%.
>
> **Unification is complete.** Both parameter divergences are resolved: D1
> (`excludeLookAheadOnDenseStart`) is intentionally divergent and load-bearing (batch
> `true`, bridge `false`); D2 (`pass1MinDistinctPcsForCandidate`) is unified at `1` on
> both paths (`4d881e7418`). STEP 1 (`3d80d0a91d`): the dim7 characteristic bonus now
> requires the complete diminished triad, and Gate J treats a complete root-position
> diminished triad over a sounding dominant root as an inverted V7 — Jazz BIR=true
> 56→33 (−23), Baroque BIR=false 25→23 (−2).
>
> Hard stops always: Baroque BIR=false > 25, Jazz BIR=false > 13, any test
> regression beyond the 2 known Corelli notation failures.

This preamble goes before EVERY task description, no exceptions.

---

## Standing rule — Investigation-first before implementation (MANDATORY for Cowork)

**Before writing any CC implementation instruction that touches existing scoring
mechanics**, either:

1. Read the relevant source code here in Cowork first (use the Read tool on
   `chordanalyzer.cpp` at the specific section), **or**
2. Write a pure read-and-report instruction first — CC reads and reports, no code
   changes — then write the implementation instruction based on that report.

"Touching existing mechanics" means: adding a template near an existing one,
modifying a bonus/gate/guard, changing a threshold, or anything where an existing
scoring term might interact with the proposed change.

**Why:** B2 took 4 attempts and B3 was reverted because implementation instructions
were written based on incomplete understanding of existing code. The `dim7CharacteristicBonus`
rotation-selection role was only discovered mid-task. An investigation pass first
would have caught this before a single line was written.

**The C1 investigation instruction is the correct model.** Pure read-and-report,
no edits, produces a design proposal. Only after the report comes back does the
implementation instruction get written — based on actual findings, not assumptions.

---

## Standing rule — Visual inspection before debugging (MANDATORY for BIR=false cases)

Before investing CC debugging effort on any BIR=false case, **look at the score with
our annotations first.** A single image reveals whether the error is isolated or
systemic; this determines whether a targeted fix is worthwhile or whether the case
should be accepted as a Phase E residual.

**How:** Ask the user for an annotated score image, or use
`tools/inject_dcml_rn.py` to overlay DCML Roman numerals alongside ours, then open
the resulting file in MuseScore. Even our annotations alone (without DCML ground truth)
expose systemic patterns (rootContinuityBonus over-stickiness, inversion mis-labeling,
Roman numeral errors) that the BIR metric cannot see.

**Decision rule based on the image:**
- **One wrong region, rest of score looks correct** → targeted fix is likely worth it.
  Proceed to CC debugging.
- **Multiple wrong regions sharing a mechanism (e.g. tonic stickiness throughout a phrase,
  or consistent inversion errors)** → systemic; check whether it's a known dead end
  (Iter 98 / Phase E). If yes, accept as residual. If not, characterise the scope before
  committing to a fix.
- **Widespread unrelated errors** → complex residual; accept, move on.

**Introduced 2026-06-04** after bwv14.5 image review showed rootContinuityBonus
stickiness in opening measures + an unrelated m5 post-scoring promotion + Roman numeral
labeling errors — three distinct issues in one score. Score image identified all three
faster than three rounds of CC programmatic debugging.

---

## Windows Snap fix — do not revert

File: `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`
Function: `calculateWindowSize()`

Two lines that set `ptMinTrackSize` equal to the full monitor work area were removed.
This prevented Windows Snap from working on maximised MuseScore windows.
`ptMaxSize` and `ptMaxPosition` are kept. `ptMinTrackSize` is intentionally left unset.

The fix is committed as a local-only branch in the muse submodule (`fix/windows-snap-ptmintracksize`
at `b9604805a`). The parent repo's master correctly pins the submodule pointer to this commit.
**Do not restore the `ptMinTrackSize` lines. Do not push the muse submodule to upstream.**

This is documented in `C:\s\MS\CLAUDE.md` which CC reads every session.

---

## Known CC/VS Code integration issues

**Stale `git index.lock`** — When CC loses contact with a running git process (a known
VS Code integration bug), `.git/index.lock` is left behind (0 bytes). Symptom: git
commands fail with "Unable to lock the index". Fix: verify no git process is running
(`tasklist | grep git`), then delete `.git/index.lock`. Safe to delete if file is
0 bytes and no git process is running.

**Silent disconnect — three distinct triggers (diagnosed 2026-05-14 from VS Code logs)**

VS Code sets the CC session to `idle` (handing control back to user) in these situations,
while the CC process keeps running invisibly. Dangerous to submit new tasks without waiting.

**Trigger 1 — Non-zero exit code:**
A bash command returns non-zero (failing tests, grep with no matches, etc.). The extension
sees this as an error and marks the session idle. CC keeps running.
Fix: append `; echo "exit:$?"` to every command that may return non-zero. The echo always
returns 0, so the extension sees a clean result.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Trigger 2 — stream_idle_partial (long bash output):**
When a bash command produces large output and CC takes >~15 seconds to process the result,
the API stream goes idle between chunks. The extension logs `[WARN] [Stall] stream_idle_partial`
and marks the session idle. CC is still running and will eventually complete.
Fix: break long commands into smaller steps that produce incremental output. Pipe through
`head -N` to limit output size. Write large results to a file and read separately rather
than capturing in one bash call.
- BAD:  `batch_analyze <score> --dump-regions notation`  (may produce thousands of lines)
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

**Trigger 3 — stream_idle_partial (API latency, bytesTotal=0):**
When the Anthropic API takes >15 seconds to send the first token of a response (server load,
network hiccup), the extension logs `stream_idle_partial lastChunkAgeMs=15xxx bytesTotal=0`.
This can silently drop the panel even though CC recovers and keeps running. No reliable
prevention — it's server-side latency. If the panel goes silent mid-task without any bash
errors, this is likely the cause. Check the VS Code output log before resubmitting.

Build commands (setup_and_build.bat) are launched via PowerShell Start-Process which
isolates the exit code — less affected by trigger 1.

---

## .vscode/settings.json — muse submodule noise

VS Code detects `muse/.git` (submodule gitdir pointer) and prompts to open it as a
separate repository. Two settings suppress this in `C:\s\MS\.vscode\settings.json`:
- `"git.detectSubmodules": false` — stops VS Code treating submodules as separate SCM providers
- `"git.ignoredRepositories": ["C:\\s\\MS\\muse"]` — belt-and-suspenders ignore by path

If CC hasn't applied these yet, ask it to edit `.vscode\settings.json` accordingly,
then Ctrl+Shift+P → "Reload Window".

---

## Build commands (quick reference)

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Tests (run from ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report location
src/composing/tests/chord_mismatch_report.txt
```

---

## Standing practices — build and corpus hygiene

Two silent failure modes that produce plausible-looking but wrong results:

**Stale build** — if the working tree has uncommitted changes and the binary
hasn't been rebuilt, corpus analysis runs against the old logic. BIR numbers
will look identical to the last clean run but the characterization is wrong.
**Always rebuild before any corpus run when the working tree has been modified**,
or when there is any doubt about whether the binary matches the source.

**Stale corpus output** — `analyze_inversion_errors.py` reads whatever JSON
files are already in `tools/corpus/`. If `run_bach_preset.py` was not run
first (or was run against a different binary), the analysis silently reads
old results. **Always run `run_bach_preset.py` immediately before
`analyze_inversion_errors.py`** — never rely on corpus JSON files left over
from a prior session or a prior build.

Canonical corpus analysis sequence (never skip steps):
```
# 1. Rebuild first if working tree has changes
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# 2. Regenerate corpus (Baroque)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus

# 3. Analyse (reads the freshly written JSONs)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Repeat steps 2–3 for Jazz if needed (reuses same output-dir)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## LLM integration design — completed 2026-05-15

A full architectural design session for "Claude Composer" — natural-language interaction
with scores via an LLM of the user's choice (analogous to Claude Code / Copilot in IDEs).

**Two documents created / updated:**

- `docs/llm_integration.md` — comprehensive design document (11 sections). Read this
  before any implementation work on the LLM bridge.
- `ARCHITECTURE.md` §19 — high-level overview and key decisions (4 subsections).

**Key conclusions that are not obvious from reading the docs:**

- The Core Access Layer is a **facade over existing INotation* interfaces** — not a new
  information model. §5.2 has the full interface inventory. The point is to avoid
  translation loss, not to redesign the data model.

- LLM bridge uses the **stateless tier** (tool calls, musical addresses, no object
  references). Plugin API uses the **stateful tier** (EID-backed handles, event
  subscriptions). These are different programming models; do not conflate them.

- **Event subscriptions keep dependency direction one-way.** When `ScoreEventSource`
  (Core Access Layer) subscribes to `async::Channel<ScoreChanges>`, the subscription
  is initiated *from* the Core Access Layer *into* MuseScore. `async::Channel` stores a
  callback and fires it — it has no reference back to the subscriber. No reverse
  dependency is created.

- `src/composing/` is **not part of official MuseScore** — it is this project's own
  development. §10 and ARCHITECTURE.md §19.3 both note this explicitly.

- **MusicalAddress is the cross-cutting join key.** There are NO direct object
  references from Note → Staff or Note → Measure. A Note's address (`partId`,
  `staffIndexInPart`, `measureNumber`, `beat`, `voice`, `tick`) is the only locator.
  Querying "all notes in measure 12 of the Oboe" is a pure filter over addresses —
  no graph traversal. Harmony, Annotation, and Note at the same MusicalAddress are
  co-located: matching on address is the equivalent of a SQL join on a composite key.

- **Address does NOT uniquely identify a Note.** Multiple notes in the same chord
  share an identical MusicalAddress (same part + staff + measure + beat + voice).
  A `NoteId` is required to unambiguously identify a single note. The information
  model must carry NoteId on the Note entity.

- Subsection numbering in `llm_integration.md` §7 and §8 had a drift (labels said
  6.x and 7.x respectively) — fixed 2026-05-15.

---

## ms-core-api branch — decisions made 2026-05-15

A new branch and worktree for the Core Access Layer (protocol-neutral facade over
`INotation*` and friends, shared foundation for plugin API and LLM bridge).

**Branch:** `ms-core-api`  
**Worktree:** `C:\s\MS-core-api` ✓ created 2026-05-15  
**VS Code window:** separate window on `C:\s\MS-core-api`  
**CC context:** automatically separate (different path = different CC project memory)  
**CLAUDE.md:** ✓ written and committed on the branch — scoped to CAL, composing-module sections removed

**Known gap — build script:** `setup_and_build.bat` inherited from master hardcodes
`c:\s\MS\ninja_build_rel`. A `setup_and_build.bat` specific to `C:\s\MS-core-api`
needs to be created (pointing to `C:\s\MS-core-api\ninja_build_rel`) before the
first build attempt in the new worktree.

**Current state:** CLAUDE.md committed, no code written yet. Next steps:
1. Create `setup_and_build.bat` for the worktree
2. Create `src/ms-core-api/` skeleton (CMakeLists.txt + first interface headers)
3. Wire into root CMakeLists.txt
4. Create junction points for extensions/plugins (see below)

**Why `ms-core-api` as a name:** "plugin-api-v2" would imply the QML/Q_PROPERTY
protocol; this layer is protocol-neutral. It exposes capabilities (score read/write,
settings, project, playback, instruments) without committing to any binding technology.
Protocol-specific layers (QML bindings, JSON/tool-call schema for LLM) sit above it.

**Architecture:**
```
Plugin bindings (QML)   LLM bridge (JSON)   future protocols
        └───────────────────┴──────────────────┘
                    ms-core-api
              (capabilities, no protocol)
                    INotation* family
                    MuseScore DOM
```

**Dev environment prerequisite — junction points (one-time, do before first test run):**

Extensions and plugins are in `share/extensions/` and `share/plugins/` but
`appDataPath()` on Windows resolves to one level up from the exe (`C:\s\MS\` when
running from `ninja_build_rel\`). MuseScore looks for `C:\s\MS\extensions\` and
`C:\s\MS\plugins\` — neither exists without junctions. Fix:
```
mklink /J "C:\s\MS-core-api\extensions" "C:\s\MS-core-api\share\extensions"
mklink /J "C:\s\MS-core-api\plugins"    "C:\s\MS-core-api\share\plugins"
```
(Run as Administrator in cmd.exe. Do this in the ms-core-api worktree.)

**Full-stack test loop once junction points exist:**
1. Write C++ in `src/ms-core-api/` → build MuseScore5.exe
2. Write a minimal test extension: `manifest.json` + JS/QML in `C:\s\MS-core-api\extensions\your-test\`
3. Launch MuseScore5.exe, open a score, run the extension
4. No install step needed — extensions load from the junction-pointed directory

**Extension anatomy (v2 system):**
- `manifest.json` — declares URI, type (macros/composite/form), actions
- `main.js` or `Form.qml` — the extension logic
- API surface available to extensions: `api.log`, `api.interactive`, `api.engraving`,
  `api.converter`, `api.websocket` (see `muse/framework/extensions/api/extapi.h`)
- ms-core-api methods will be added here once implemented

**Legacy v1 plugins** (QML, old API) live in `share/plugins/`. They use the
`muse/framework/extensions/api/v1/` path and the old `PluginAPI`/`qmlRegisterType`
system. Relevant for understanding what exists; NOT the target for ms-core-api work.

---

## AI Assistant extension MVP — work done 2026-05-16

Independent of CAL work. AI Assistant chat extension is the first concrete LLM-bridge
artefact per the [[llm-bridge-mvp-strategy]] memory (build v2 extension first, validate
where the API gaps actually bite). Lives in the ms-core-api worktree at
`share/extensions/ai-assistant/` (`Main.qml` + `manifest.json`). Committed as
**`87ff66b8e5`** on a new branch **`ai-assistant-mvp`** (cut from the same point as
`ms-core-api`), specifically so the CAL branch stays focused.

**Branch:** `ai-assistant-mvp` (in the `C:\s\MS-core-api` worktree; switch with
`git checkout ai-assistant-mvp` if you want the files materialised — they're committed
only on that branch).

**Deployed copies** (untracked or outside repo; used at runtime by MS4):
- `C:\Users\vince\AppData\Local\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml`
- `C:\s\MS\ai-assistant\Main.qml` (staging — was stale at v0.4.3, reconciled to v0.4.12 on 2026-05-16)

All three copies are byte-identical at 75225 bytes / v0.4.12.

**Four MS4 limitations discovered and worked around:**

1. **`Qt.labs.settings` not deployed in MS4 install** — `C:\Program Files\MuseScore 4\qml\Qt\labs\` ships only `platform/` and `qmlmodels/`; `settings/` is missing because windeployqt only ships modules MuseScore itself imports, and the main UI never imports `Qt.labs.settings`. Fix: switched to `import MuseScore 3.0; Settings { ... }` — that's the vendored `QQmlSettings` registered in `muse/framework/extensions/api/v1/extapiv1.cpp:40` via `qmlRegisterType("MuseScore", 3, 0, "Settings")`. Process-global registration, so it works from V2 extensions too, not just V1 plugins. No deployment dependency.

2. **`FlatButton` / `import Muse.*` deploy gate over-matched** — the grep pattern in the [[ms4-deploy-gate]] memory (`grep -c "FlatButton\|import Muse"` expecting 1 — the line-2 self-describing comment) over-matched after the Enter workaround landed in v0.4.11: caught `import MuseScore 3.0` strings, `import Muse.Ui\n` substrings inside `Qt.createQmlObject` calls, and doc comments. Tightened the gate to `grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)"` expecting empty output. Mirrors the actual extension validator in [extensionbuilder.cpp:42-60](muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp#L42-L60). Memory updated.

3. **Stale staging vs deployed divergence** — the staging copy at `C:\s\MS\ai-assistant\Main.qml` had been left at v0.4.3 (May 15) while UI work continued directly on the deployed copies up to v0.4.6 (scrollToBottom helper, copy-message button, TextArea → TextField swap, several others). If the v0.4.3 staging had been re-deployed without merging, ~40 lines of UI work + the Enter workaround would have been lost. Reconciled 2026-05-16 by copying v0.4.12 back to staging. **Going forward: edit in staging only, deploy via grep gate + copy** — the original workflow as documented in [[ms4-deploy-gate]] — rather than editing deployed copies directly.

4. **Enter-to-send in extension QML — the big one.** Took 11 diagnostic iterations (v0.4.5 → v0.4.11) and a deep dive. `TextField.onAccepted`, `Keys.onReturnPressed`, AND any QML `Shortcut` bound to Return/Enter ALL silently fail in MS4 extension QML. Root cause: MS4 implements its entire shortcut system as QML `Shortcut` elements registered in the main window ([muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml:53-60](muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml#L53-L60)), binding `Return`/`Enter` to `nav-trigger-control` ([src/app/configs/data/shortcuts.xml:80-85](src/app/configs/data/shortcuts.xml#L80-L85)). Anything an extension binds at the same key triggers an ambiguous-overload in Qt's resolver — both candidates are `Qt.WindowShortcut` context — and Qt fires *neither*, without any warning. The fix: dynamically build a `NavigationSection → NavigationPanel → NavigationControl` chain via `Qt.createQmlObject` (bypassing the extension's static-import-only deploy validator), register the control as active on input focus via `requestActive(false)`, and connect its `triggered` signal to send. MS4 then dispatches Enter to it. Documented in v0.4.12's in-file comment above `setupNavigation()` and in [[ms4-extension-input-workaround]]. Verified working at v0.4.11 in log `MuseScore_260516_120757.log`. The dynamic-import bypass works because the validator only scans literal `import` lines in `.qml` files; strings inside `Qt.createQmlObject` are ignored. The V2 extension QML engine still resolves `Muse.Ui` at runtime because it's a registered QML module (not file-path based), independent of the engine's import-path list.

**Open items (suggested follow-ups, not blockers):**

- ~~`extensions/` and `plugins/` junction directories in the ms-core-api worktree show as untracked in `git status` — they're per-machine setup per the worktree CLAUDE.md, should probably be added to `.gitignore` (worktree-local config). Not done.~~ **Done 2026-05-16:** added `/extensions/` and `/plugins/` (with explanatory comment) to `.gitignore` on the `ms-core-api` branch worktree. Modification still unstaged — needs a small standalone commit when convenient. `share/extensions/` content is unaffected (no leading-slash anchor avoidance issues).
- `share/extensions/hello-world/` is also untracked in the worktree — separate exploration, not part of the ai-assistant commit. Status unknown.
- The [[ai-assistant-sandbox-choice]] memory's open question (extension vs. plugin sandbox) is now better-informed: the Enter workaround works in the extension sandbox, so the motivation to migrate to a `MuseScore { pluginType: "dialog" }` plugin is weaker than when the memory was written. Decision still deferred to desktop Claude.
- Worktree-local `setup_and_build.bat`, `setup_and_build_fast.bat`, and `CLAUDE.md` have unstaged modifications on ms-core-api — intentional per-worktree configs, not yet decided whether they should be committed to the branch or kept as local-only.
- No push yet. `ai-assistant-mvp` is local-only. Pushing it to origin (`github.com/slimvince/MuseScore`) needs explicit decision — the branch could land as a PR target, or just live as a personal branch for now.

**Memory updates 2026-05-16:**
- [[ms4-extension-input-workaround]] — rewrote to cover both patterns (Ctrl/editing-key intercept + NavigationControl Enter workaround). The pre-existing description (TextArea + printable-char intercept) was obsolete after the v0.4.6 TextField swap.
- [[ms4-deploy-gate]] — corrected the grep pattern; old loose pattern documented as obsolete.
- `MEMORY.md` index — both descriptions updated.

---

## Key files

| File | Purpose |
|------|---------|
| `src/composing/analysis/chord/chordanalyzer.cpp` | Main analyzer — all scoring logic |
| `src/composing/analysis/region/regionanalyzer.cpp` | Canonical region orchestrator — Pass 1/2/2b, absorb, backfill, restamp |
| `src/notation/internal/notationharmonicrhythmbridge.cpp` | Bridge — thin wrapper over `regionanalyzer` |
| `docs/llm_integration.md` | LLM / Claude Composer full design document |
| `docs/quality_observations_iter76.md` | R1–R5 recurring themes for Iter 79+ |
| `docs/score_inventory.md` | Score paths for all test/corpus files |
| `STATUS.md` | Current baselines and HEAD — read every session |
| `build_and_test.md` | All build/test/tool commands |
| `CLAUDE.md` | Standing rules for CC — read every session |
| `tools/analyze_inversion_errors.py` | BIR corpus check |
| `muse/framework/extensions/api/extapi.h` | Current extension API surface (v2) |
| `muse/framework/extensions/internal/extensionsconfiguration.cpp` | Path resolution for extensions/plugins |
