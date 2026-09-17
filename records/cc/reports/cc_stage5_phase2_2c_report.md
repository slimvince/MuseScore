# CC report — Stage-5 Phase 2.2c: RETIRE-4 (GateA held) · per-carrier scoping (O-9) · bwv392 class-(b) · candidate re-selection sweep

**Dispatch:** `cc_instruction_stage5_phase2_2c.md` (Cowork, 2026-07-05) · **HEAD at dispatch:** `3f52f088ad` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** the sixth CC increment. Executes the ratified retirements, hits a byte-identity STOP on Gate A (surfaced; the user chose to un-retire Gate A → **RETIRE-4**), delivers the O-9 per-carrier scoping mechanism (values unchanged), score-verifies the bwv392 blocker, and runs the candidate re-selection sweep. **No fitted value adopted; no `tools/corpus/` write; no push.**

---

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — retire GateA | `89c7f55f3c` | `refactor(composing):` | (later reverted by #6) |
| 2 — retire GateF | `7ea8201d43` | `refactor(composing):` | Gate F removed; byte-identical |
| 3 — retire GateGB | `15831825ea` | `refactor(composing):` | Gate G-B removed; byte-identical |
| 4 — retire GateGC | `d2becff50c` | `refactor(composing):` | Gate G-C removed; byte-identical |
| 5 — retire GateK | `a4da727d71` | `refactor(composing):` | Gate K + `kGateKMargin` removed; byte-identical |
| 6 — un-retire GateA | `c9909be4f8` | `refactor(composing):` | **Gate A restored** (winner-byte-identical but alternatives-differing on 36 Baroque; user Option 1). Net = **RETIRE-4** |
| 7 — dispositions + manifest | `9823ce75fc` | `docs(composing):` | §6 RETAIN-4/DEFER-5 + manifest GateK row → `retired` |
| 8 — per-carrier scoping | `6a468f82ac` | `feat(tools):` | O-9 bassNoteRootBonus + kWStepIn per-carrier (values unchanged) + manifest preset_scope |
| 9 — measurement tools | `37603ab217` | `feat(tools):` | the 2.2c drivers (byteproof/3way/winnerdiff/sweep) + `stage5_2_2c_sweep.jsonl` trade curve |
| — this report | *(this commit)* | `docs(cowork):` | `cc_stage5_phase2_2c_report.md` (force-add) |
| — the fold | *(next commit)* | `docs(cowork):` | STATUS 22q · COWORK_HANDOFF · design (O-9/§14) · `cc_instruction_stage5_phase2_2c.md` (force-add) |

---

## Task 0 — state check

HEAD `3f52f088ad`, branch `master`, fork-only. Dirty set matched the dispatch expectation exactly (COWORK_HANDOFF.md · STATUS.md · cowork_stage5_fitter_design.md + known scratch). Corpus `tools/corpus/{baroque,jazz,default}` each 352 `.ours.json`; manifest `git_hash 0dd64660f4`. **No STOP at Task 0.**

## Task 1 — RETIRE-5 → byte-identity STOP → the diagnosis → Option 1 (un-retire GateA) → RETIRE-4

**Executed** the five retirements as five commits (each: code block + `PostScoringRule` enum member + name-map entry + synthetic fixtures + `PostScoringRuleDisable` test + `docs/scoring_model.md` §6 sync). Suites (retirement binary): **composing 1116 → 1096 (−20 vacated)**, notation 53, snapshots 11 — green.

**The byte-identity proof tripped the STOP** (Baroque 36 differing `.ours.json`; Jazz/Default 0). I diagnosed rather than assume:

| test (Baroque) | diffs | reading |
|---|---|---|
| frozen `0dd64660f4` vs baseline `3f52f088ad` (built) | **0** | frozen is NOT stale; the intervening override/ruleOff commits were genuinely byte-identical |
| baseline `3f52f088ad` vs retirement HEAD | **36** | the RETIRE-5 changed 36 Baroque scores |
| **WINNER-only diff, all 352 scores** | **0 winners** | every byte-diff is **`alternatives[]`-only** |
| per-gate (`disable_rule` on the baseline binary, ≡ deletion) | GateA alone = all 36 (alternatives-only, 0 winner); **GateF/GB/GC/K = 0 diff** | only GateA carries the diff |

**Mechanism** (verified `bwv17.7@…`): the region winner is `F#m7/A` in both cases. GateA re-ranks via `std::swap(results[0], results[bestAltIdx])` (reusing the existing `A6` result object in `alternatives[]`); with GateA gone, the retained **FM2** promotes the *same winner* via `results.push_back(buildResult(...))` — a freshly-built object. Same winner, different `alternatives[]`. So the 2.2b firing-site ledger (which measured the **winner** root/symbol → GateA = 0 sites) was **correct**; the dispatch's proof is over the full `.ours.json` including `alternatives[]`, a stricter surface. This is a **carry-contract surprise**, not "the evidence was wrong" — surfaced as a STOP.

**User decision (Option 1):** un-retire GateA (commit `c9909be4f8` — restore its block + enum + name + fixtures + docs; `git revert` of `89c7f55f3c` with the three dependent-chain conflicts hand-resolved to the RETIRE-4 state), keep the four fully-byte-identical retirements (F/GB/GC/K). Net = **RETIRE-4**.

**RETIRE-4 verification:** rebuild → **composing 1101** (1096 + 5 restored GateA fixtures), notation 53, snapshots 11 — green. **Byte-identity regen ×3 vs frozen = 0 diffs on ALL THREE presets (alternatives included) — PASS.**

## Task 1g — dispositions + manifest (commit `9823ce75fc`)

- `scoring_model.md` §6: **RETAIN-as-structural (4)** GateI/FM2/GateJ/GateL, **DEFER (5)** BiasCorrection/GateE/GateH/GateGD/GateGE — one line each, 2.2b evidence refs; plus a "**Gate A retirement HELD**" note (winner-byte-identical, alternatives-differing).
- `tools/param_manifest.json`: G7 `kGateKMargin` row → `status: retired` (Gate K removed with its margin constant); value untouched.

## Task 2 — per-carrier scoping (O-9; commit `6a468f82ac`; mechanism only, values UNCHANGED)

Made `bassNoteRootBonus` (a `ChordAnalyzerPreferences` field) and `kWStepIn` (a `harmonicfunctionlayer.h` global) **per-carrier deliverable** in `batch_analyze.cpp`:
- each preset branch sets `chordPrefs.bassNoteRootBonus` explicitly (all carriers 0.70);
- `kWStepIn` is delivered per preset via `params::applyGlobalOverride("kWStepIn", …)` — the **same registered-global writer the override loader uses** — written **before** the `--param-override` load, so a fitting override cleanly overrides it and a Jazz run with no override stays pinned (byte-identical by construction).

**Byte-identity:** full-corpus regen ×3 = 0 diffs (all three presets); `batch_analyze` regression test green; composing/notation/snapshot suites unaffected (analysis lib untouched). Manifest `preset_scope` for both rows: shared → per-preset (O-9 ref).

**★ Production-path question (STOP-AND-REPORTED, not improvised).** The production/notation path has **no preset-selection moment** — it uses `kDefaultChordAnalyzerPreferences` (the `bassNoteRootBonus` struct default, `analysistypes.h:177`) + the `kWStepIn` global initializer (`harmonicfunctionlayer.h`), i.e. it delivers **only the Default carrier**. For the Default carrier both levers therefore already have a production delivery surface (struct default / initializer), and a future Default fit ships to production through those. But **a future *non-Default*-carrier production delivery has no surface** — production never runs Baroque/Jazz carriers. This dispatch delivers per-carrier for the **batch/fitting path only** (no production behavior change; values unchanged). The kStepBudget derivation (`kWStepIn + kWStepOut + 0.01`) is recomputed by the override loader when the fit moves `kWStepIn`; a future adoption that bakes a non-0.10 `kWStepIn` into the preset config (not the override file) must recompute `kStepBudget` alongside — flagged for the adoption artifact.

## Task 3 — score-verify `bwv392@17520` (guardrail (2))

The candidate (`bassNoteRootBonus 0.775, sameRootInversionBonus 0.475, kWStepIn 0.125`) **re-segments** bwv392 around tick 17520. From the a8 union-of-boundaries grid (WiR = `Chorales/289/analysis.txt` per `find_wir_file`):

| cell | baseline our→WiR | candidate our→WiR |
|---|---|---|
| 17040–17520 | F/G (5) → D (2), disagree | F/G (5) → D (2), disagree |
| 17520–17760 | *(in the 17040–17760 F/G cell)* → D (2), disagree | **Dm/F (2) → D (2), AGREE** (fixed) |
| 17760–18240 | Gm9 (7) → G (7), **AGREE** | **Dm/F (2) → G (7), DISAGREE** (over-grab) |

The candidate's `Dm/F` (D minor, root 2) **over-grabs the WiR Gm (vi, root 7) region 17760–18240**. Both readings are **Minor triads** — **pitch-class-decidable roots, not symmetric (not dim7/aug/whole-tone), not a named share-tone template** → **class-(b)** (a8 `cell_class` = b; "default to (b) on any doubt" also applies). Net over 17040–18240 the candidate is **root-worse** (agree 240 vs baseline 480; disagree 960 vs 720). **Verdict: class-(b) — a genuine functional root error; a hard blocker for any candidate that creates it.** Confirms the 2.2b classification.

## Task 4 — candidate re-selection sweep under the full-corpus hard stop

**Setup.** Sweep `bassNoteRootBonus ∈ {0.70, 0.7125, 0.725, 0.7375, 0.75, 0.7625, 0.775}` at the fixed `(sameRootInversionBonus 0.475, kWStepIn 0.125)` [delivered to Baroque + Default; **Jazz pinned = byte-identical by construction**]. Per point: full-Baroque regen → fitting-split (261) feasibility (§4.2: no new class-(b) batch case + class-(b) dur non-increase) + full-Baroque surface; Default full regen only for fitting-feasible points. Baselines reproduced exactly (fitting Baroque 63.5026, full Baroque 63.3234). Committed ledger `tools/fit_ledgers/stage5_2_2c_sweep.jsonl`.

**Trade curve** (`stage5_2_2c_sweep.py`; fitting gain vs the 63.5026 all-on fitting baseline; full-corpus new class-(b) batch cases vs 53/24/53; Jazz byte-identical by construction, always +0):

| bnrb | fit root (Δ) | fit-feasible | held-out Δ | full Baroque batch, new-clsB | full Default batch, new-clsB | full-feasible |
|---|---|---|---|---|---|---|
| 0.70   | 63.5607 (+0.058)  | ✗ `bwv379@11520` | — | 53, +{bwv379, bwv392} | — | — |
| 0.7125 | 63.7979 (+0.2952) | ✗ `bwv379@11520` | — | 52, +{bwv379, bwv392} | — | — |
| 0.725  | 63.8052 (+0.3025) | ✗ `bwv379@11520` | — | 52, +{bwv379, bwv392} | — | — |
| 0.7375 | 63.9329 (+0.4302) | ✓ | — | **49, +{bwv392}** | **50, +{bwv392}** | **✗** |
| 0.75   | 63.9256 (+0.4229) | ✓ | — | 49, +{bwv392} | 50, +{bwv392} | ✗ |
| 0.7625 | 63.9073 (+0.4047) | ✓ | — | 49, +{bwv392} | 50, +{bwv392} | ✗ |
| **0.775** | 64.0168 (+0.5142) | ✓ | **+0.5874** (held-out, new clsB `bwv392@17520`) | 49, +{bwv392} | 50, +{bwv392} | ✗ |

**★ Selection: NONE — the coupled family is NOT adoptable at any swept value.** Two blockers, one per feasibility tier:
- **Low bnrb (0.70–0.725):** fitting-**infeasible** — the `sameRootInversionBonus 0.475 + kWStepIn 0.125` bump creates a new fitting class-(b) case `bwv379@11520` that the lower bass-root bonus does not absorb (the mirror of the 2.2b coupling: a *higher* bass-root bonus absorbs it — bwv379 is gone by 0.7375).
- **High bnrb (0.7375–0.775):** fitting-**feasible** (bwv379 absorbed) but full-corpus-**infeasible** — the **Task-3-verified class-(b) `bwv392@17520`** appears on **both Baroque and Default** at every fitting-feasible value. It is present at 0.70 too (full Baroque) — i.e. bwv392 is driven by the fixed `srib/kw` bump, not by bnrb, so no bnrb value removes it.

So the S-3 rejection loop rejects every swept point. The fitting gain (+0.43…+0.51) and the full-Baroque batch **drop 53→49** (the candidate fixes ~5 baseline class-(b) cases) are real, but the single new class-(b) `bwv392@17520` is a hard R10 stop on Baroque **and** Default. The **0.775 point reproduces the 2.2b Config I candidate exactly** (fitting +0.5142, held-out +0.5874, full Baroque 49/+bwv392, full Default 50/+bwv392); its complete decision surface — DLC probe corelli/mozart/schumann +1.37/+0.54/+0.15, snapshot 11/11 refresh, D-4 Default **ineligible** (newB=1), Jazz shared-scope duration −0.607 — is in `cc_stage5_phase2_2b_report.md` §3.1 and is **not re-run** here (it is not a selected candidate). **No prepared adoption artifact** — there is nothing adoptable to prepare; the decision (a gentler `srib/kw` that does not create bwv392, a per-preset re-scope, a Layer-4 fix for the bwv392 over-grab, or accepting a smaller uncoupled gain) is the user's.

**★ The genuine finding:** bwv392@17520 is not a bassNoteRootBonus artifact — it is created by the `sameRootInversionBonus 0.475 + kWStepIn 0.125` pair (present even at bnrb=0.70), a **segmentation over-grab** (the candidate reads `Dm/F` (iii6) across the WiR `Gm` (vi) boundary, Task 3). This is a **Layer-2/Layer-4 boundary/root problem surfaced by the weight bump**, not a weight the fit can tune around — consistent with the O-1 cross-layer-budget caveat (the BIR=false set is distributed across layers, not a Layer-5 residual).

## Task 5 — sandwich + suites + reuse/new

### Sandwich (end-of-run acceptance)
`characterise_bir_false.py` on the **REAL per-preset dirs**: Baroque **53** / Jazz **24** / Default **53** (326/352 WiR coverage each). `tools/corpus/` **git status clean** (byte-untouched; every regen — RETIRE proofs, per-carrier proof, the sweep — went to `C:/tmp/stage5_2_2c/…` scratch), so the stem@tick case-identity sets are **identical to CLAUDE.md, set-diff empty both directions by construction** (the RETIRE-4 corpus is byte-identical to the frozen `0dd64660f4`).

### Suites
composing **1101** (1116 −20 vacated +5 GateA-restored), notation **53**, pipeline_snapshot **11** — all green, **no golden refresh** (the RETIRE-4 corpus is byte-identical; the sweep candidates were never applied). `batch_analyze` regression test green (per-carrier scoping). The composing-count drop is net **−15** vs the 1116 dispatch-entry baseline (the four retired rules' 15 vacated fixtures; GateA's 5 restored).

### What retires (the arc's first real retirements)
**GateF, GateGB, GateGC, GateK** — retired, fully byte-identical (regen ×3, 0 diffs incl. `alternatives[]`). **`kGateKMargin`** retired with Gate K. **Gate A: retirement HELD** (winner-byte-identical but alternatives-differing; awaits the byte-identity-contract decision).

### Reuse-vs-new
- **Reuses (verbatim):** `run_bach_preset.py` regen, `a8_rebaseline_measure.py`, `characterise_bir_false.py`, `stage5_fit_driver.py` (`regen`/`measure`/`write_override`), the frozen corpus, `stage5_split_registry.json` (261/65), `stage5_2_2b_snapshot_preview.py` + `run_dlc_baseline.py --param-override` (for Task 4b), `dcml_parser`.
- **New (committed):** `tools/stage5_2_2c_byteproof.py` (byte-identity ×3), `tools/stage5_2_2c_3way.py` (frozen/baseline/retirement diagnosis), `tools/stage5_2_2c_winnerdiff.py` (winner-vs-alternatives isolation), `tools/stage5_2_2c_sweep.py` (the re-selection sweep) + `tools/fit_ledgers/stage5_2_2c_sweep.jsonl`.

## Repo state
5 retire + 1 un-retire + 2 docs/feat commits, local/unpushed. Working tree src == HEAD; RETIRE-4 binary. **No `tools/corpus/` write** (all regen to `C:/tmp/…` scratch; frozen `git status` clean, manifest `0dd64660f4`). **No push. No fit value adopted.**
