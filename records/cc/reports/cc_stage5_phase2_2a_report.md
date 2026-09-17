# CC report — Stage-5 fitter, Phase 2.2a: the rule-disable mechanism + the §6-block dissolution AUDIT (measurement only)

**Dispatch:** `cc_instruction_stage5_phase2_2a.md` (Cowork, 2026-07-05) · **Design:** `cowork_stage5_fitter_design.md` (SIGNED, P1-ratified; §4.4 family 2, D-7, §15 O-7/O-8)
**HEAD at dispatch:** `49640eef5f` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** the fourth CC increment of the Stage-5 arc — builds the **rule-disable mechanism** (the same safety class as the A-6 constant override) and runs the **per-rule dissolution audit at CURRENT weights**. This is the evidence base for the Phase-2.2b joint fit. **NOTHING is adopted; no committed constant value changed; NO rule retired here.** Also carries the two O-8 housekeeping fixes.

---

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — the mechanism | **`0296e38f63`** | `feat(composing):` | §6-block per-rule disable (paramoverride enum/API + 14 postscoringgates guards + batch_analyze message/help + 20 tests) + `docs/scoring_model.md` §6 doc-sync. Byte-identical when absent. |
| 2 — the tools | **`7367c7ae96`** | `feat(tools):` | fit-driver `audit` mode + `evaluate --disable-rule` + committed `tools/fit_ledgers/` path (O-8) + `run_dlc_baseline.py --param-override` (O-8). Additive. |
| 3 — this report | *(this commit)* | `docs(cowork):` | `cc_stage5_phase2_2a_report.md` (force-add; `/cc_*.md` is gitignored) |
| 4 — the fold | *(next commit)* | `docs(cowork):` | STATUS 22o · COWORK_HANDOFF · design (O-7/O-8 + §4.1/§4.3 P-markers) · layer4 (O4) · `cc_instruction_stage5_phase2_2a.md` (force-add) |

---

## Task 0 — state check

- **HEAD** `49640eef5f`, branch `master`, fork-only, local/unpushed.
- **Dirty set matched the dispatch's expectation exactly:** the four Cowork narrative fold files (`COWORK_HANDOFF.md`, `STATUS.md`, `cowork_stage5_fitter_design.md`, `cowork_layer4_chordsymbol_design.md`) + the deliberately-untracked scratch (`idiom_discovery/vl_*_out.txt`, `scratch_artifacts/`). Nothing else. **No STOP.**
- **Corpus:** baroque/jazz/default each **352 `.ours.json` + 352 `.music21.json` + 352 `.xml`**; manifest `git_hash 0dd64660f4` (unchanged). Reference corpus read-only throughout (git-clean at end).
- **Suites at entry:** composing 1096 / notation 53 / snapshots 11.

---

## Task 1 — housekeeping (O-8), two additive fixes

### 1.1 — Fit ledgers become committed artifacts (O-8 (1))

The driver's **compact per-run** ledgers now write to `tools/fit_ledgers/` — verified **NOT gitignored** (`git check-ignore tools/fit_ledgers/x.jsonl` → not ignored; `.gitignore` line 25 ignores only `tools/reports/`). The **DRIVER PATH** moved (never `.gitignore`): `stage5_fit_driver.py` `FIT_LEDGER_DIR = tools/fit_ledgers`; the fit `--out` default + the new audit `--out` default point there. The **shared full-row append-log** (`tools/reports/stage5_fit_ledger.jsonl`) and the a8 per-cell mappings **stay** gitignored scratch — the A-8 "large per-cell enumerations stay regenerable" precedent (design §7 as amended by O-8). Both readings of O-8 are honored: the per-run ledgers are committed; the unbounded append-log is not.

The Phase-2.1 family-1 ledger files **still existed in scratch**, so per the instruction they are committed under the new path (not re-run): `tools/fit_ledgers/stage5_fit_kPowerChord3PcPenalty.jsonl` (13 rows = the family-1 fit ladder). Committed in SHA 2.

### 1.2 — One validation runner gains `--param-override` (O-8 (2), the S-5 gap closer)

**Chosen runner: `tools/run_dlc_baseline.py`** — the least-change choice. Rationale: it is the **config-driven unified driver** that already computes **per-style DCML root-agree** (`root_agree_pct` via `compare_rn.score_corpus`) over the DLC clones, and it already invokes `batch_analyze` in one place (`_run_one`). The ~30 copied `run_*_validation.py` scripts and `run_validation.py` would each need the same edit; `run_dlc_baseline.py` closes the S-5 gap for **every** DLC sub-corpus at once. Change: an additive `--param-override FILE` arg threaded into `_run_one` (git-bash + native paths); **no new comparison logic**.

**Proof (corelli, first 3 movements):**

| run | invocation | vs baseline (A) |
|---|---|---|
| **A** | no flag | — (baseline `.ours.json`) |
| **B** | `--param-override <identity: kForeignPenalty 0.45>` | **0 diffs (byte-identical)** |
| **C** | `--param-override <perturbed: bassNoteRootBonus 0.0>` | **3/3 differ (live)** |

`A_vs_B_diffs=0`, `A_vs_C_diffs=3` → **PASS**. The absent-flag path is guarded by `if args.param_override`, so it is provably unchanged. (An earlier probe with `kForeignPenalty 0.9` gave A≡C — that value is genuinely inert on those three movements; a direct `batch_analyze` test confirmed the mechanism is live and that value simply flips no winner there. The proof uses a value proven-live by that direct test.)

---

## Task 2 — the rule-disable mechanism (same safety class as A-6; flag-gated, byte-identical absent)

**Grammar decision (declared):** the existing `name value` override-file grammar is extended with a reserved-keyword line **`disable_rule <Name>`** (chosen over a boolean namespace: it is self-documenting, does not collide with the numeric `name value` grammar, and reuses the existing two-token line parser). `<Name>` is one of the 14 canonical names in `paramoverride.h` `PostScoringRule`: **`BiasCorrection FM2 GateA GateE GateF GateGE GateGB GateGC GateGD GateH GateI GateK GateL GateJ`**. Strict: an unknown rule name aborts the run; `disable_rule` alone (no name) is a malformed line.

**Reach — each §6 member individually.** Every rule maps to exactly ONE clean skip in `applyPostScoringGates()`: a `!ruleOff(PostScoringRule::X) &&` prepended to that rule's top-level `if`. With nothing disabled, `ruleOff` returns `false`, so each guard collapses to `true && <cond>` = `<cond>` — **no logic restructuring** (R9 stays parked). Process-global disable state defaults to all-enabled; only a loaded `disable_rule` line writes it.

**Coupling STOPs — NONE.** All 14 rules skip cleanly. The two shared-state neighbours were handled as clean skips, not restructures, and are recorded:
- The **G-family `rawCandidates` pull/pop** is shared infrastructure serving all four G-sub-gates; each G-sub-gate disable skips only its own swap `if`, leaving the pull (which is inert without a firing sub-gate via the pop-back). Not a coupling STOP.
- **Gate A → FM2 cascade** (both gate on `didEnharmonicFlip`): disabling Gate A alone leaves `didEnharmonicFlip=false`, so FM2 becomes eligible — this is the *real* marginal-contribution semantics the audit measures, not a coupling that needs restructuring.

**Byte-identity proofs (the Phase-1 discipline):**
1. **Full-corpus regen ×3 vs frozen corpus = 0 diffs.** New binary + **no** override, `run_bach_preset.py` regen to scratch, `cmp` each `.ours.json` vs `tools/corpus/<preset>`: **Baroque 352/0 · Jazz 352/0 · Default 352/0 → TOTAL_DIFFS=0, ALL_IDENTICAL.**
2. **An identity override file with zero disables ⇒ byte-identical again** — unit test `ParamOverride.IdentityFileWithNoDisableLeavesAllRulesEnabled` (every rule enabled) + `param-override: applied … 0 §6 rules disabled` message on an identity file (direct `batch_analyze` check).
3. **Snapshots 11/0, no golden refresh** — the P1–P4 goldens are unchanged, an independent byte-identity witness on the notation path.

**Unit tests (+20; composing 1096 → 1116):**
- **Grammar (`paramoverride_tests.cpp`, +6):** the 14 names known (`postScoringRuleNames`), count = 14, `GateB`/unknown rejected; a `disable_rule` line sets the flag + counts (`rulesDisabled`); mixes with value overrides; **unknown rule name throws**; bare `disable_rule` throws; identity-with-no-disable leaves all rules enabled.
- **Per-rule provably-not-firing (`postscoringgates_tests.cpp`, +14):** `PostScoringRuleDisable.<Rule>_DisabledDoesNotFire` reconstructs each rule's canonical firing fixture and asserts the ENABLED arm fires (matching the pinned outcome) and the DISABLED arm does **not** fire (winner unchanged). The fixture resets the process-global disable state around every test.

**Doc-sync (same commit, SHA 1):** `docs/scoring_model.md` §6 gains a one-line note — the §6 rules are individually disable-able via the override file, measurement-only, default absent, retires no rule.

---

## Task 3 — the per-rule dissolution AUDIT at current weights (measurement only; the 2.2b evidence base)

Carrier **Baroque**, fitting split **261**, current weights, via the driver `audit` mode; every run ledgered to `tools/fit_ledgers/stage5_rule_dissolution_audit.jsonl`. **Baseline (all rules on):** root-agree **63.5026 %**, RN 44.8517 %, key 68.2587 %, batch **46** (two-tier class split **b:22 / a:24**), class-(b) disagree duration 2 313 320, class-(a) 87 360. (Root + batch reproduce the ratified fitting-split baseline exactly.)

### The per-rule audit table — objective Δ (variant-(b) root, fitting split; RN/key tracked), batch subset-diff (explained per case), fixtures, firing info

| rule | Δroot | RN | key | batch | batch set-diff (fitting, explained) | clsB dur Δ | clsA dur Δ | pinned fixtures (postscoringgates_tests.cpp) | provisional class |
|---|---|---|---|---|---|---|---|---|---|
| **BiasCorrection** | **+0.0036** | 44.8772 | 68.2769 | 45 | **−`bwv60.5@30960` (class-b, FIXED off)** | −480 | +240 | BiasCorrection_Fires / _MarginBracket / _SeventhExemption | **active, disable-beneficial** |
| **FM2** | **−0.0584** | 44.8298 | 68.2587 | 47 | **+`bwv227.7@18000` (class-b, REGRESSED off)** | +3840 | 0 | GateA_FM2_PullsMinorAltFromRawCandidates / _BelowThreshold… | **(b) load-bearing** |
| GateA | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateA_FastPath / _PresetOff / _PlainMajorWinner | (a) disable-inert |
| **GateE** | **+0.0073** | 44.8517 | 68.2587 | 46 | EMPTY | −480 | 0 | GateE_MinorWinnerFlipsToMajorAtPlus8 / _NoStepwise / _AltRootBelow | active, disable-beneficial |
| GateF | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateF_MajorWinnerFlipsToMajorAtPlus5 / _NoStepwise | (a) disable-inert |
| GateGE | +0.0000 | 44.8663 | 68.2514 | 46 | EMPTY | −1440 | +1440 | GateGE_KeyFunctionFlip / _PullsHalfDim… / Ordering_Sub9a / GateG_Popped | (a) obj-inert (1440 b→a reshuffle) |
| GateGB | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateGB_ForwardEvidenceFlips | (a) disable-inert |
| GateGC | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateGC_RecentRootAndStepwiseFlips | (a) disable-inert |
| GateGD | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateGD_ConsecutiveStepwiseBoundary | (a) disable-inert |
| **GateH** | **+0.0073** | 44.8590 | 68.2587 | 46 | EMPTY | 0 | −480 | GateH_RotatesPlus4 / _Plus8 / _NoContext / _PresetOff | active, disable-beneficial |
| **GateI** | **−0.0292** | 44.8225 | 68.2806 | 46 | EMPTY | +1920 | 0 | GateI_MarginBracket / _NonDiatonic / _AltRootBelow | **(b) load-bearing** |
| GateK | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateK_MarginBracket / _MajorSharpFifth | (a) disable-inert |
| GateL | +0.0000 | 44.8517 | 68.2587 | 46 | EMPTY | 0 | 0 | GateL_MarginBracket / _AugmentedSeventhWinner | (a) disable-inert |
| **GateJ** | **+0.0547** | 44.8371 | 68.2806 | 46 | EMPTY | −3600 | 0 | GateJ_DimTriad…SwapsToV65 / _DimSeventh / _DominantRootBelow / _AltWithout… | **★ active, disable-beneficial — inference-adjacent (DECLARE)** |

Denominators, named: **Δroot / RN / key** are variant-(b) **duration-weighted** agreement percentages on the **fitting split (261 scores, 326-cell WiR coverage restricted to fitting stems)**; **batch** is the fitting-subset batch-stop (BIR=false) case count; **clsB/clsA dur** are the aggregate class-(b)/class-(a) **root-disagree durations** over the fitting cells (MuseScore ticks). The removed/added cases' two-tier class was verified against the frozen-baseline a8 mapping (`bwv60.5@30960` = class-b; `bwv227.7@18000` = class-b, from the FM2 row's `new_class_b_batch_cases`).

### Batch subset-diff — every change explained (only two rules move the fitting batch SET)

- **BiasCorrection disabled → −1 batch case: `bwv60.5@30960` (class-b) becomes root-correct.** Disabling the bias deduction *fixes* a pitch-class-decidable root error the correction was *causing* → class-(b) batch count 22→21, objective +0.0036. No new class-(b), no new class-(a).
- **FM2 disabled → +1 batch case: `bwv227.7@18000` (class-b) regresses.** FM2's raw-candidate Minor-partner pull *prevents* a class-(b) root error → its removal adds a class-(b) case, objective −0.0584. Load-bearing for a class-(b) case.
- **All other 12 rules: EMPTY batch set-diff** (no case added/removed/class-changed). GateE/GateH/GateJ/GateI/GateGE move only the *aggregate* class-duration (sub-batch-threshold), not the batch case set.

### Pinned-fixture replay (Task 3.3)

**Every rule has ≥1 pinned test** — a positive finding: the §6 block has **full pin coverage** (no rule lacks a pinned fixture; mapped in the table above). The replay is realized as the +14 `PostScoringRuleDisable.<Rule>_DisabledDoesNotFire` tests: for each rule the ENABLED arm reproduces the rule's pinned firing outcome and the DISABLED arm shows non-firing — i.e. the rule's "fires" fixtures **would fail** with the rule disabled (their pinned post-state is no longer reached), while the "no-flip/guard" fixtures are unaffected. All 14 pass (composing 1116/0). The existing pinned gate tests all pass with rules enabled (the baseline). No rule needed an invented test.

### Firing-count telemetry (Task 3.4)

**No existing diagnostic counts §6 rule firings** (grep for `gateFired`/`firingCount`/… = none; `diagnoseChord` replays the pipeline but exposes no per-gate firing count). Per the instruction, **none was built.** The disable-delta *is* the corpus-level firing evidence: a rule with Δroot = 0 **and** an empty batch/class movement fires on **zero fitting-split cells** or does so scoring-neutrally there (the seven exact-zero rows); a non-zero row is a rule that fires and moves the objective/classes.

### Provisional classification (measurement only — NO verdict; each verdict is 2.2b's, per D-7)

- **(a) disable-inert at current weights (fitting split)** — retirement CANDIDATES for 2.2b (which tests whether *fitted* weights reproduce the pinned fixtures): **GateA, GateF, GateGB, GateGC, GateGD, GateK, GateL** (Δroot = 0.0000, batch unchanged, zero class movement — they fire on no fitting-split cell, or scoring-neutrally). **GateGE** is (a) for the objective and the batch SET, with a noted **1440-duration class-b→class-a reshuffle** (no root-agreement change, no batch case change) — sub-threshold symmetric-rotation churn, provisionally (a).
- **(b) disable-harmful / load-bearing** — joint-fit subjects (the correction the fit must reproduce with continuous weights): **FM2** (−0.0584; +1 class-(b) batch case) and **GateI** (−0.0292; +1920 class-(b) duration).
- **Active, disable-BENEFICIAL on the fitting split** — a distinct provisional category surfaced by the measurement: **NOT inert, NOT harmful; the rule's correction slightly *harms* the root-only fitting objective.** **BiasCorrection** (+0.0036; fixes a class-(b) batch case), **GateE** (+0.0073), **GateH** (+0.0073), and **★ GateJ** (+0.0547; class-(b) duration −3600 — the largest-magnitude finding). These are strong 2.2b refit/verification subjects; **no verdict here.**
- **(c) coupled / unresolvable (the Task-2 STOP class)** — **NONE.** All 14 rules disabled cleanly.

### ★ Inference-adjacent finding — DECLARED to Cowork, NOT acted on (GateJ)

Disabling **GateJ** (the vii°→V7 completion — the rule the roadmap expects to survive **longest** as a structural fact a continuous weight cannot encode) **improves** the root-only fitting objective by **+0.0547** and **reduces** class-(b) disagree duration by 3600, while it **worsens RN agreement (−0.0146)** and slightly raises key (+0.0219). Mechanism: Gate J re-roots a diminished triad to a dominant-7th a major third below; where DCML labels the sonority `vii°` (the diminished root), Gate J's `V7` reading disagrees **on the root** — so the **root-only** objective, which is quality/function-silent, penalizes a structurally-motivated re-rooting that the **RN** respect (the full functional label) rewards. This is a signal about the **objective vs the rule**, not evidence Gate J is wrong. Per the standing instruction, this is **declared as an inference-quality observation, not acted on**: Gate J's retirement question is 2.2b's, decided by **per-case verification against the actual notes / music21 GT region** (is `V7/A♯` or `vii°/A♯` the DCML-correct root at each firing?), never by this aggregate. The root-only-objective / structural-rule tension this exposes is exactly why D-7 makes dissolution an **audited per-rule verdict**, not a bulk deletion.

### Cost / determinism

**14 rule evals + 1 baseline = 15 evaluations, ~50 s/eval (~12.5 min total)** — regen-dominated, within the Phase-0 figure (far under the 4× / STOP). Deterministic (fixed rule order; the shared `evaluate()` determinism proof stands).

---

## Task 4 — sandwich + suites (end-of-run acceptance)

- **Sandwich — `characterise_bir_false.py` on the REAL per-preset dirs ×3:** Baroque **53** / Jazz **24** / Default **53**; **stem@tick set-diff EMPTY both directions** vs the CLAUDE.md canonical sets (parsed from the full enumeration + compared, all three). `SANDWICH_RESULT: ALL_MATCH_SETDIFF_EMPTY`.
- **Reference corpus byte-untouched:** `git status tools/corpus/` = 0 dirty; manifest `git_hash 0dd64660f4` unchanged. Every regen (byte-identity proof, audit, dlc proof) went to scratch.
- **Suites (all-flags-absent binary; no golden refresh — nothing adopted):** composing **1116** (+20 new) / notation **53** / snapshots **11**; **0 FAILED**.

---

## Reuse-vs-new + what retires

- **Reuses (verbatim):** `run_bach_preset.py` regen + `--param-override`, `a8_rebaseline_measure.py`, `characterise_bir_false.py`, `compare_rn.score_corpus`, the frozen corpus, `stage5_split_registry.json` (261/65), the `batch_analyze --param-override` loader — all Phase-1/2.1 landings, unmodified.
- **New (committed):** the §6 per-rule disable mechanism (`0296e38f63`, byte-identical absent) + doc-sync; the fit-driver `audit` mode + `evaluate --disable-rule` + committed ledger path + `run_dlc_baseline --param-override` (`7367c7ae96`, additive); the committed compact ledgers under `tools/fit_ledgers/`.
- **New (gitignored scratch, regenerable):** the shared full-row append-log + a8 per-cell mappings under `tools/reports/`; the byte-identity / audit / dlc scratch under `C:/tmp/s5_scratch/`.
- **Retires: NOTHING.** This dispatch produces the *evidence* for retirements (the audit table), not retirements — each retirement is its own 2.2b audited, user-ratified commit (D-7).

---

## STOP conditions — status (none tripped)

- **Any behavior change with all flags absent:** DID NOT fire — full-corpus regen ×3 = 0 diffs; snapshots 11/0; 33 new tests green (identity-file & no-disable arms).
- **Any committed constant / rule value change:** none — only the additive mechanism + tools + doc-sync + ledgers + this report. No `chordanalyzer.cpp`/`postscoringgates.cpp` constant changed value; no rule retired.
- **A rule that cannot be cleanly skipped (coupling STOP):** none — all 14 clean; the two shared-state neighbours (G-family pull/pop; A→FM2 cascade) handled as clean skips and recorded, not restructured.
- **Any write under `tools/corpus/`:** none (git-clean).
- **Sandwich mismatch / suite regression:** none.
- **Cost > 4×:** not tripped (~50 s/eval × 15 ≈ 12.5 min, within budget).

---

## Checkpoint — the evidence, not a verdict

The mechanism is proven **byte-identical absent** (the acceptance) and the **14-rule audit table** is complete with every diff explained and every rule's pinned fixtures replayed. The evidence for 2.2b: **7 rules disable-inert** (retirement candidates), **2 load-bearing** (FM2, GateI — the fit must reproduce their class-(b) corrections), and **4 active-but-disable-beneficial on the root-only fitting objective** (BiasCorrection, GateE, GateH, and — most sharply — **GateJ**, which the root-only metric penalizes while RN rewards: an **inference-adjacent signal declared, not acted on**). **No rule retires by this dispatch** — the joint fit + per-case verification (2.2b, D-7, user-ratified) decides each verdict on this evidence.
