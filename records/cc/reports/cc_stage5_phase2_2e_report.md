# CC report — Stage-5 Phase 2.2e: THE ADOPTION EVENT — kWStepIn 0.10→0.125 (Baroque/Default carriers) + the first frozen-corpus re-baseline

**Dispatch:** `cc_instruction_stage5_phase2_2e.md` (Cowork, 2026-07-05; ratified adoption event) · **HEAD at dispatch:** `ce10fe74dc` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** THE first fitted-value adoption of the Stage-5 arc. Unlike every prior increment, this one **changes a committed value, refreshes goldens, and (the one-time ratified exception) writes `tools/corpus/`**. Candidate: **(sameRootInversionBonus 0.40 [UNCHANGED], kWStepIn 0.10→0.125)**, Baroque/Default carriers, Jazz pinned byte-identical — the 2.2d recommended point.

---

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — adoption | `c50002fee1` | `feat(analysis):` | kWStepIn 0.10→0.125 (+ derived kStepBudget) + the per-carrier delivery + kStepBudget-leak fix + doc-sync + unit tests + 11 refreshed goldens |
| 2 — corpus | *(this commit)* | `chore(corpus):` | corpus re-baseline 52/24/52 + CLAUDE.md re-stamp + A-8 baselines + fit-driver per-preset/RATIFIED + O-10 liveness + this report (force-add) |
| — the fold | *(next commit)* | `docs(cowork):` | STATUS · COWORK_HANDOFF · design (O-11 adoption record) · `cowork_candidate_lever_register.md` · `cc_instruction_stage5_phase2_2e.md` (force-add) |

---

## Task 0 — state check + pre-flight (PASS)

HEAD `ce10fe74dc` (the 2.2d fold), branch `master`, fork-only. Dirty set matched the dispatch expectation (the Cowork fold files + known scratch). Binary + frozen corpus = the 2.2d state (manifest `git_hash 0dd64660f4`, 352×3).

**Pre-flight (existing drivers; frozen corpus read-only, candidate regen → scratch):** the 2.2d surface reproduced **exactly** at the candidate (srib 0.40, kw 0.125, bnrb 0.70):

| metric | frozen | candidate | Δ |
|---|---|---|---|
| fitting(261) root | 63.5026 | **63.5391** | **+0.0365** |
| full Baroque root | 63.3234 | 63.3581 | +0.0347 |
| full Baroque batch | 53 | **52** | −1, **removal-only `{bwv244.32@5760}`**, newB=**0** |

All four pre-flight checks PASS (fitting 63.5391 ✓, batch 52 ✓, removal exactly `{bwv244.32@5760}` ✓, newB=0 ✓). **No STOP at Task 0.**

---

## Task 1 — the adoption commit (`feat(analysis):` `c50002fee1`)

### 1.1 The value + the kStepBudget audit
- **`harmonicfunctionlayer.h`:** `kWStepIn` initializer **0.10 → 0.125**. `kStepBudget = kWStepIn + kWStepOut + 0.01` recomputes to **0.235** (the expression-initializer preserved; the derived value is NOT a hardcoded literal). Asserted in a unit test: `functionlayer_tests.cpp` `EXPECT_NEAR(kStepBudget, 0.235, 1e-12)` — **passes**.
- **grep-audit — every site that could assume the old 0.21, with its disposition:**

| # | site | disposition |
|---|---|---|
| 1 | `harmonicfunctionlayer.h:116` comment "(not the literal 0.21)" | → "(not the literal 0.235)" |
| 2 | `functionlayer_tests.cpp:115` `EXPECT_NEAR(kStepBudget, 0.21)` | → 0.235 (Task 1) |
| 3 | `functionlayer_tests.cpp` step-guard boundary competitor `0.78` | → **0.76** (the 0.235 budget lowers the guard threshold `1.0−budget` 0.79→0.765, so the "just-outside" competitor is now 0.76; comment refreshed. The "inside" competitor 0.80 and the wDim-guard 0.70/0.85 competitors stay on the correct side of both thresholds — comments refreshed to 0.765/+0.125) |
| 4 | `paramoverride_tests.cpp:119` `0.10+0.10+0.01` | → `0.125+0.10+0.01` |
| 5 | `docs/scoring_model.md:435` "(≈ 0.21)" | → "(0.235 Baroque/Default, 0.21 Jazz/others — derived from kWStepIn)" |
| 6 | `stage5_fit_driver.py:100` `kStepBudget val=0.21` | → per-preset {0.235 / 0.21 / 0.235} (Task 2, so the fixture stays a valid identity) |
| **7** | **`batch_analyze.cpp` per-carrier delivery — ★ THE LOAD-BEARING ONE** | **fixed (see 1.2); the single-key override does NOT recompute the derived kStepBudget, so the new 0.235 init would leak into the pinned-0.10 carriers.** |

### 1.2 ★ The kStepBudget-leak finding (the non-obvious, load-bearing one)
`kStepBudget` is DERIVED (`= kWStepIn + kWStepOut + 0.01`). The recompute lives **only** in the FILE loader `loadAndApply` (`paramoverride.cpp:365`); a **single-key `applyGlobalOverride` does NOT recompute it**. The O-9 per-carrier delivery in `batch_analyze.cpp` delivers `kWStepIn` via a single-key `applyGlobalOverride`, and a plain corpus regen (`run_bach_preset.py` with no `--param-override`) never calls `loadAndApply`. So after the adoption moved the **initializer** to `kWStepIn=0.125` (`kStepBudget=0.235`), the carriers that pin `kWStepIn` back DOWN to 0.10 (**Jazz + Standard/Modal/Contemporary**) would keep the **0.235** initializer for `kStepBudget` instead of their correct **0.21** — silently running the m7-family surgical guard at the wrong tolerance and **breaking Jazz byte-identity**.

**Fix:** after the per-carrier `kWStepIn` delivery, `batch_analyze.cpp` now **re-derives `kStepBudget` per carrier** (`getRegisteredGlobal("kWStepIn") + getRegisteredGlobal("kWStepOut") + 0.01`), mirroring `loadAndApply`'s recompute (Baroque/Default → 0.235; Jazz/other → 0.21). **This is squarely "the derived kStepBudget" the STOP condition explicitly permits to change.**

**PROVEN load-bearing** (Task 2.2 diagnostic R2, below): forcing `kStepBudget=0.235` on Jazz changes **7** `.ours.json` files. Without the fix, Jazz would NOT have been byte-identical. The fix is not belt-and-suspenders.

### 1.3 The per-carrier delivery (O-9) + enumerated/pinned presets (mandate 4c)
`batch_analyze.cpp` preset branches, ALL enumerated:

| preset branch | kWStepIn | note |
|---|---|---|
| **Baroque** | **0.125** | 2.2e-adopted idiom-#2 fit |
| **Default** | **0.125** | 2.2e-adopted (== global initializer / production carrier) |
| **Jazz** | **0.10** | PINNED, not adopted |
| **else — Standard / Modal / Contemporary** | **0.10** | PINNED EXPLICITLY, not adopted |
| local initializer (dead default, all branches reassign) | 0.125 | updated to keep "== production/global initializer" true |

`sameRootInversionBonus` NOT touched anywhere (0.40 stands; Jazz 0.15). `bassNoteRootBonus` unchanged (0.70). Production has no preset-selection moment → ships ONLY the Default carrier via the global initializer (0.125), O-11 iii.

### 1.4 param_manifest + doc-sync + tests + goldens
- **`param_manifest.json`:** `kWStepIn` row value **0.125**, per-preset `{Baroque 0.125, Jazz 0.10, Default 0.125}`, and the **FIRST `license_provenance` fill**: *"fitted on: reference-corpus fitting split (PD scores / CC-BY-SA WiR annotations), idiom #2 ground truth, only — adoption 2026-07-05"*. `kStepBudget` row value **0.235**, per-preset {0.235/0.21/0.235} (derived).
- **`docs/scoring_model.md` §4** (the CLAUDE.md sync rule): `w_stepIn` heading per-carrier; a new adoption note; the kStepBudget-derivation caveat.
- **Unit tests** updated + green (see 1.1 dispositions).
- **Golden refresh:** ran `pipeline_snapshot_tests` (0/11 pass pre-refresh — exactly the 11 goldens the 2.2d preview flagged). **Confirmed the intended fit effect:** the diffs are chord-region **root re-selections** (e.g. bwv806_gigue C♯→D) and **boundary/tick shifts** (e.g. bach_chorale_003 17280→17760, bwv806_prelude 36720→34800) — the Pass-B step-bonus signature, JSON structure intact, no corruption. Then `--update-goldens` → **11/11 green**. The 11 refreshed goldens ride this commit.
- **Suites:** composing **1101** / notation **53** (0 failed, 4 pre-existing skips) / snapshots **11** — all green on the refreshed goldens.

---

## Task 2 — the frozen-corpus re-baseline (`chore(corpus):`)

### 2.1 Regen (the ratified corpus write)
All three presets regenerated into `tools/corpus/{baroque,jazz,default}` with the adopted binary (`run_bach_preset.py`, no override — the adopted values are the code). Each **352/352 complete**; manifests stamped **`git_hash c50002fee1`** (the Task-1 commit). Clean-slate preserves `.music21.json` GT (removes only `.ours.json` + manifest).

### 2.2 Verified outcome — EXACTLY the promised diff

| preset | count | set-diff vs old CLAUDE.md | verdict |
|---|---|---|---|
| **Baroque** | **52** | removal-only **`{bwv244.32@5760}`**, 0 added | ✓ |
| **Jazz** | **24** | **empty both directions** (identical) | ✓ |
| **Default** | **52** | removal-only **`{bwv244.32@5760}`**, 0 added | ✓ |

`characterise_bir_false.py` ×3 (`--corpus-dir tools/corpus/<preset>`), case-identity sets parsed from the full-enumeration table and diffed element-wise against the CLAUDE.md ratified sets. **No STOP** — the diff is precisely removal-only `{bwv244.32@5760}` ×{Baroque,Default} + Jazz-identical, as the 2.2d surface promised.

**★ Jazz byte-identity — a methodology note + the rigorous proof.** `tools/corpus/` is **gitignored** (`.gitignore:26`), so the frozen `.ours.json` are NOT version-controlled, and the re-baseline regen overwrote the old frozen Jazz **in place** — there is no `git diff` reference and no pre-regen copy was taken (a process gap; see the handoff). I reconstructed the pre-adoption Jazz **rigorously** and proved byte-identity:
- **R1 (reconstruction):** the adopted binary, Jazz, `--param-override {kWStepIn 0.10, kStepBudget 0.21}` (the exact pre-adoption Jazz constants, delivered via the trusted `loadAndApply` path). Since the **composing library object code is unchanged** (only the header initializer *values* + the `batch_analyze` driver changed), this is byte-exact to the pre-adoption binary's Jazz. **plain `tools/corpus/jazz` vs R1 = 0 differing files** → Jazz is byte-identical to the pre-adoption frozen Jazz. ✓
- **R2 (leak diagnostic):** the adopted binary, Jazz, forced `{kWStepIn 0.10, kStepBudget 0.235}` (the would-be leak). **plain vs R2 = 7 differing files** → the leak WOULD have changed Jazz on 7 scores; the kStepBudget re-derivation fix (1.2) is exactly what preserves Jazz byte-identity, and confirms the plain regen runs at 0.21 (not 0.235).

Together with the case-set identity (Jazz-24 empty diff) and the root/RN reproducing the prior 62.37/42.40, Jazz byte-identity is established.

### 2.3 CLAUDE.md re-stamp
- Identity-set section: **Baroque 52** + **Default 52** (both = the prior sets − `{bwv244.32@5760}`, dated 2.2e provenance line), **Jazz 24** unchanged.
- A new `★ CURRENT STATE 52/24/52` header above the preserved L3-wiring history.
- The A-8 dual-track note (baselines below) + the `batch 52/24/52` gate reference updated. Historical provenance (the L3-wiring −4/+1/−4 delta; the Stage-4a-patch "57/23/57" record) preserved.

### 2.4 A-8 baselines re-measured (adopted `tools/corpus`, one consistent run)

| preset | root % | RN % | key % | batch |
|---|---|---|---|---|
| Baroque | **63.36** (63.3581) | 44.58 | 68.19 | 52 |
| Jazz | **62.37** (62.3664) | 42.40 | 64.52 | 24 |
| Default | **63.25** (63.2539) | 44.41 | 67.77 | 52 |
| fitting-split (261) | **63.5391** | 44.86 | 68.27 | — |

Prior: 63.32/62.37/63.22, RN 44.56/42.40/44.40, key 68.11/64.43/67.50. **Jazz root/RN reproduce the prior 62.37/42.40 exactly** (byte-identity corroboration at the governing metric); its key figure (64.52 vs 64.43) reflects the a8 re-measure, not a 2.2e change (Jazz `.ours.json` proven byte-identical). Recorded in CLAUDE.md's dual-track note. Fit-driver **RATIFIED** fixture vector updated to {63.36 / 62.37 / 63.25}; **PARAMS** kWStepIn/kStepBudget made per-preset so the identity fixture reproduces the adopted binary per carrier. Fitting-split baseline (63.5391) recorded.

**Fixture verification (+ a driver-consistency fix surfaced here).** The `fixture` mode writes an identity
override of ALL `PARAMS` and regens each preset — it failed initially because `PARAMS` still listed
**`kGateKMargin`** and `POST_SCORING_RULES` still listed **`GateK`**, both **retired with Gate K** (Stage 5,
2026-07-05; `isRegisteredGlobal("kGateKMargin") == false`, `isKnownRuleName("GateK") == false`). The stale
`kGateKMargin` made every score's override an unknown-name rejection. **This is a PRE-EXISTING driver staleness
(dead since the Gate-K retirement), NOT a 2.2e regression** — surfaced by running the fixture. Removed both
(neither changes any scoring value or the gate; the `POST_SCORING_RULES` comment mandates matching the C++
`postScoringRuleNames()`). With that + the per-preset `kWStepIn`/`kStepBudget` and the new RATIFIED vector,
the fixture **PASSES**: full-root **63.36 / 62.37 / 63.25 = MATCH** on all three carriers (batch 52/24/52; fitting-split 63.54), i.e. the identity override reproduces the adopted binary exactly.

### 2.5 O-10 first application — retained-rule liveness
Firing sites re-measured on the adopted corpus (the 2.2b regen-diff method, reused verbatim from `stage5_2_2b_evidence.firing_sites`), diffed vs the adopted `tools/corpus` baseline; ledger `tools/fit_ledgers/stage5_2_2e_liveness.jsonl`. New driver `tools/stage5_2_2e_liveness.py`.

| rule | carrier | sites (2.2e) | prior (2.2b) | Δ | live |
|---|---|---|---|---|---|
| FM2 | Baroque | 16 | 16 | 0 | ✓ |
| GateI | Baroque | 29 | 28 | +1 | ✓ |
| GateI | Jazz | 186 | 186 | 0 | ✓ |
| GateI | Default | 31 | 30 | +1 | ✓ |
| GateJ | Baroque | 132 | 133 | −1 | ✓ |
| GateJ | Jazz | 248 | 248 | 0 | ✓ |
| GateJ | Default | 138 | 139 | −1 | ✓ |
| GateL | Jazz | 18 | 18 | 0 | ✓ |

**All four retained rules LIVE on every measured carrier — no collapse.** Deltas within ±1 (the expected small drift from the kWStepIn re-segmentation on the two adopted carriers; Jazz counts unchanged, corroborating byte-identity). No finding to report.

---

## Task 3 — adoption record + reuse/new + suites

### Fitted-set artifact (design §7)
- **idiom label:** idiom #2 (Chromatic-functional) · **carriers:** Baroque + Default (production via Default) · **vector:** `kWStepIn = 0.125` (sameRootInversionBonus 0.40 unchanged, bassNoteRootBonus 0.70 unchanged) · **ledger refs:** `stage5_2_2d_sweep.jsonl` / `stage5_2_2d_surface.jsonl` (the surface), `stage5_2_2e_liveness.jsonl` (O-10) · **provenance:** *"fitted on: reference-corpus fitting split (PD scores / CC-BY-SA WiR annotations), idiom #2 ground truth, only — adoption 2026-07-05"*.

### Reuse-vs-new
- **Reuses (verbatim):** `stage5_fit_driver.py` (regen/measure/write_override/split), `run_bach_preset.py`, `characterise_bir_false.py`, `a8_rebaseline_measure.py`, `stage5_2_2b_evidence.py` (firing_sites — reused by the O-10 driver), the 2.2d surface ledgers, the frozen split registry.
- **New (committed):** `tools/stage5_2_2e_liveness.py` (the O-10 liveness driver) + `tools/fit_ledgers/stage5_2_2e_liveness.jsonl` (the liveness ledger).
- **Modified (committed):** the Task-1 adoption set; `stage5_fit_driver.py` (PARAMS `kWStepIn`/`kStepBudget` per-preset + RATIFIED vector + **removed the stale retired-Gate-K refs** `kGateKMargin` from PARAMS and `GateK` from POST_SCORING_RULES); CLAUDE.md.

### What retires
**Nothing retires.** This is an adoption + re-baseline. The batch stop REMAINS the hard stop (dual-track unchanged — a set re-stamp within the policy, 53/24/53 → 52/24/52, NOT the R10 dissolution).

### Suites
composing **1101** / notation **53** / pipeline_snapshot **11** — all green on the refreshed goldens.

---

## Repo state
Local/unpushed, fork-only. Two commits so far: `c50002fee1` (`feat(analysis):` adoption) + the corpus chore (this report + re-baseline). The fold follows. **No push.**
