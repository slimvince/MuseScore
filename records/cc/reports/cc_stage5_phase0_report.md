# CC report — Stage-5 fitter, Phase 0 (inventory + cost; read-only)

**Dispatch:** `cc_instruction_stage5_phase0.md` (Cowork, 2026-07-04) · **Design:** `cowork_stage5_fitter_design.md` (SIGNED)
**HEAD at dispatch:** `459c92c46d` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** READ-ONLY on all code/corpora. No `src/` change, no tool-behavior change, no constant change, no fit.

---

## Commit SHAs (this dispatch)

| Task | Commit | Type | Contents |
|---|---|---|---|
| Task 1 — the fold | **`4b510b9ac7`** | `docs(cowork):` | EXACTLY 6 files: STATUS.md · COWORK_HANDOFF.md · cowork_score_census.md · cowork_union_search_record.md · cowork_stage5_fitter_design.md · cc_instruction_stage5_phase0.md (force-added; `/cc_*.md` gitignored). Nothing under `src/`. |
| Task 2 — roadmap rider (O-3) | **`0f05e78690`** | `docs:` | docs/implementation_roadmap.md — the Stage-5 FITTING-POOL LICENSE CONSTRAINT + the "design SIGNED 2026-07-04 / A-3 = Jazz fit deferred" line. **Separate commit** (not folded into Task 1): the fold's file list is exact/closed, so folding the roadmap edit in would violate the exact-list contract — one commit cleaner is the closed-list fold. |
| Task 3 — the manifest | **`981e942ded`** | `feat(tools):` | tools/param_manifest.json — the 78-row parameter inventory (the deliverable). |
| Task 5 — this report | *(this commit; follows, cites the three above)* | `docs(cowork):` | cc_stage5_phase0_report.md (force-add; gitignored). |

---

## Task 0 — repo state + the OWED acquisition-round fold SHA

- **HEAD** `459c92c46d`, branch `master`, fork-only, local/unpushed.
- **★ OWED acquisition-round fold SHA — DISCHARGED: `459c92c46d`** (= HEAD at dispatch start; the `docs(cowork):` fold immediately following `4997757298`). `git show --stat` confirms the expected acquisition-round narrative file set (8 files, +612/−20): COWORK_HANDOFF.md · STATUS.md · cc_acquisition_round_report.md · cc_instruction_acquisition_round.md · cowork_product_tool_register.md · cowork_score_census.md · cowork_union_search_record.md · cowork_voiceleading_axis_design.md. *(Cowork-verified at the object per the ruling; cited here as discharged.)*
- **Corpus manifest** (re-read at source): all three presets `complete: true`, `ours_count 352 / expected 352`, **`git_hash: 0dd64660f4`** (differs from HEAD as expected — the intervening commits are docs-only folds that do not change chord output; the corpus stays valid).

### Task-0.3 dirty-set STOP — raised, Cowork-ruled PROCEED (recorded)

The tree carried, beyond the Task-1 fold list, three untracked items: `idiom_discovery/vl_discovery_out.txt`, `idiom_discovery/vl_orthogonality_out.txt`, `scratch_artifacts/` (≈100 files). Per the dispatch's listed STOP ("The Task-0 dirty-set mismatch"), I stopped and surfaced it with the full facts (all three are pre-existing benign regenerable scratch/output — not `src/`, not `tools/corpus/`, not tracked code; the Task-1/2/3 commits use explicit file lists so the extras cannot be staged).

**Cowork ruling (user-relayed): PROCEED as-is.** The extras are the known *deliberately-untracked dumps/scratch* on record in STATUS 22e/22g; the Task-0.3 check omitting them was a **Cowork instruction defect (Cowork-owned)**, recorded here per the ruling. `.gitignore` was NOT touched this dispatch (out of the change class).

**gitignore-gap record (for a future hygiene pass, NOT actioned here):** neither `.gitignore` nor `git check-ignore -v` covers `idiom_discovery/*_out.txt` or `scratch_artifacts/` (verified: no `scratch|idiom` rule; check-ignore -v returns no rule for either). By contrast `cc_instruction_stage5_phase0.md` and this report are correctly ignored by `/cc_*.md` (`.gitignore:118`) — hence both needed `git add -f` to fold in.

---

## Task 3 — the parameter manifest (the deliverable)

`tools/param_manifest.json` — **78 rows**, each anchored at source (`file:line`, value read at source, not from the doc). Full row set is the JSON; the summary:

**By family:** continuous **45** · abstention **16** · §6-block threshold **8** · squash **2** · θ **2** · §15-13 **5**.
**By consuming path:** both **49** · production-only **10** · dormant **19** · unresolved **0**.
**By style scope (declared hypothesis):** idiom-varying **34** · style-invariant **44**.
**By status (declared):** fit **61** · frozen **17**.

Row groups (site anchors): G1 chord-scoring vertical constexpr (chordanalyzer.cpp:57–128, 1364/1372/1399/1425) · G2 chord-scoring prefs (analysistypes.h:177–207) · G3 inversion context bonuses (analysistypes.h:226–268, **preset-varying**) · G4 gate/correction prefs (analysistypes.h:293/298/308/355) · G5 segmentation/pedal/misc prefs (:319–386, incl. **preset-varying** extensionThreshold) · G6 progression signals (**harmonicfunctionlayer.h:109–113**) · G7 §6-block gate margins (**postscoringgates.cpp:52/53/54/287**) · G8 L5 confidence + resolver (functionoutput.h:108, forwardoverride.h:81–82, functionresolver.h:197–200/258) · G9 the §15-13 site · G10 L3 annotate gate (sectionanalyzer.h:86) · G11 L4 sufficiency (chordslicedecoder.h:263) · G12 L1.5 phrase strength (phraseboundaryview.h:85–114) · G13 VL-C axis-2 (textureclassifierreference.h:36–38, voiceleadingprofiles.h:80).

### Key Phase-0 findings (for Checkpoint P0)

- **★ Fit surface / D-9 shared-constant fact.** The dormant L4 `SliceChordDecoder` **reuses the legacy scorer**: `chordslicedecoder.cpp:453` calls `analyzer.analyzeChord(...)` with the same `ChordAnalyzerPreferences`. So **every chord-competition constant is on BOTH the production and dormant fit surfaces** (49 "both" rows) — the design-D-9 case: fit on production, track the dormant chain's numbers alongside. Caveat (harness-phase, not Phase 0): the decoder invokes `analyzeChord` on a **reduced/null temporal context** (`chordslicedecoder.cpp:46`), so the *firing* of the progression/temporal signals is attenuated on the dormant path even though the constants are read there. The **post-scoring gates run production-only** (no `applyPostScoringGates` in the decoder; it projects `analyzeChord`'s raw ranked results).
- **★ The §15-13 site (family 4's home) — recorded, NO value.** `functionresolver.cpp:223` (the `aIn != bIn` branch) falls through at **:233** (TransitionVsContinuation) and **:279** (CloseReading) to `tieBreakOrOpen()` when both readings are licensed. Verified at source: **no hand-chosen numeric preference constant exists at the both-licensed fall-through** — the fitted weight would be introduced immediately before those `return tieBreakOrOpen();`. DORMANT (`functionresolver.h:77-79`: "NO production consumer"). Row value = `null` (the one null-value row — that is the point).
- **Freeze list (declared, 17 rows):** structural predicates/thresholds — the dim7 rotation-selector (`kDim7CharacteristicBonus`, its non-diatonic-♭♭7 rotation role), presence thresholds (kSus4StructuralFourth/kBassSupportPresence/kSeventh/kPresence/kExtension-file), `minDistinctPcsForCandidate` (entry gate), `kStepBudget` (derived tolerance), `maxTotalInversionContextBonus` (INERT/non-binding cap), `preferMinorOverMajorAdd6` (bool), `sufficiencyChordTones` (int floor), `maxForwardExtendSlices` (span bound), the 4 VL-C axis-2 study-derived floors, `kOtherToneFactor` (=1.0 reference).
- **Flags for the fitter (surfaced, not acted on):**
  1. **Gate R invariant** — the min inversion bonus (`sameRootInversionBonus`) must strictly exceed `kNonBassPenalty` (0.40 > 0.35 on Baroque/Default; the Gate R equivalence proof in scoring_model.md §4 rests on this). **Jazz sets it to 0.15 < 0.35**, so the Jazz preset does not carry the equivalence in the same form — a joint constraint any continuous fit must respect.
  2. **No runtime override surface** for the hardcoded progression constants (`kWSeq/kWDim/kWStepIn/kWStepOut`, harmonicfunctionlayer.h) — they are NOT in `analysistypes.h::bounds()`; the D-6 parameter-override plumbing (Phase 1) must reach them for the fitter to move them.
  3. The 19 `bounds()` entries (analysistypes.h:428–446) are the existing optimizer-target set; the file-level constexpr scoring constants are fit candidates with no current override surface.

### Doc-drift defects (scoring_model.md §2–§6 vs source; both directions; RECORDED, not fixed)

Per the dispatch, these are recorded here; the fixes ride the next scoring-docs commit (one change class per dispatch — I did NOT edit scoring_model.md).

1. **MISSING CONSTANT (code → doc):** `kHalfDimFirstInversionBonus = 0.55` (postscoringgates.cpp:287) — a hand-chosen additive bonus inside the §6 correction block (fires under `preferMinorOverMajorAdd6`; Iter-61 "Option B") — is **absent from scoring_model.md §6**. (The doc's only 0.55 is the unrelated `kDom7FlatFiveTpcPenalty`.)
2. **LOCATION DRIFT (progression signals):** §4 documents `w_stepIn/w_stepOut/w_seq/w_dim` as "Lambda at chordanalyzer.cpp:~L2157/~L2165/~L2190/~L2209", but the functions and their constants live in **harmonicfunctionlayer.h:109–113 + harmonicfunctionlayer.cpp:44–95** (the Stage-3.3 migration to the competition pipeline). Values match (kWSeq 0.20 / kWDim 0.15 / kWStepIn=kWStepOut 0.10 / kStepBudget 0.21); the file+line anchors are stale.
3. **LINE DRIFT (approximate anchors):** several §4 "~Lxxxx" application-site anchors no longer match — `w_complete` "~L2084" (kWComplete is chordanalyzer.cpp:1399); `dim7CharacteristicBonus` "chordanalyzer.cpp:1117" (the constexpr is :103, the call site :1352). Values match.
4. **LOCATION DRIFT (§6 gate table):** the §6 gate-table "~Lxxxx" locations (bias ~L2639, Gate I ~L3044, K ~L3080, L ~L3117, J ~L3151) predate refactor #1's move to postscoringgates.cpp; actual: outer guard :65, bias margin :270, Gate I const :52 (fire :474), K :53/:510, L :54/:544. The §6 intro acknowledges the file move but the table anchors were not updated.

**No VALUE drift found** — every constant documented in §2–§6 matches its source value. **Template-count staleness check:** scoring_model.md §2 "currently 17" == `analysis::kTemplateCount` 17 (chordanalyzer.h:63) — **MATCH.**

**Scope note:** this reconciliation is scoring_model.md §2–§6 (the chord scorer). The confidence-layer constants (kBoundary, forwardoverride baseBar/confidenceScale, VL-C floors, L1.5 phrase weights, sufficiencyChordTones, resolver params, kAnnotateKeyConfidenceThreshold) are documented in their own specs (cowork_confidence_contract.md §3, cowork_voiceleading_axis_design.md, decoder_design.md) — not scoring_model.md — so their absence there is by design, not drift.

### E-13 check (design O-6) — the fit surface does NOT touch the tuning bridge

Verified at source: `notationtuningbridge.cpp` reads harmonic-analysis **RESULTS** (`analyzeNoteHarmonicContext` / `analyzeHarmonicRhythm`) + tuning config (`tuningMode`, `tonicAnchoredTuning`, `minimizeTuningDeviation`, …); it reads **NO `ChordAnalyzerPreferences` field and NO scoring constant**. Evidence contrast: `notationcomposingbridge.cpp:617/624/627` explicitly passes `kDefaultChordAnalyzerPreferences` to chord analysis — the tuning bridge does not. **⇒ E-13/O-6: the tuning bridge does NOT enter the retirement map at this edit.**

---

## Task 4 — objective-evaluation cost (timing; scratch only; frozen corpus byte-untouched)

All regen to a manifest-stamped scratch dir; a8 + characterise read the real corpus read-only. **Proof the frozen corpus is byte-untouched: `git status tools/corpus/` = 0 dirty throughout** (checked before, mid, and after — 0 lines every time).

**a8_rebaseline_measure.py interface note (design §4.1(2)):** a8 has **no single-preset and no custom-dir interface** — it hardcodes `tools/corpus/<preset>` (line 244) and loops all three presets (`PRESETS`, line 53). Per the dispatch I did NOT modify it; the **full 3-preset a8 run is the acceptable substitute, timed as such**.

### Measured legs (wall-clock, seconds)

| Leg | measured | notes |
|---|---|---|
| **A. Corpus regen** (`run_bach_preset.py`, 352 scores → scratch) | Baroque **39** · Jazz **37** · Default **37** | the dominant cost; full-corpus (a fitting-split subset regen will be proportionally cheaper) |
| **B. Robust-unit measure** (`a8_rebaseline_measure.py`, all 3 presets — no single-preset mode) | **14** (all 3; ≈**4.7**/preset marginal) | reads real corpus read-only; self-validates grid==oracle on all 326×3 covered pieces; reproduced batch_gate 53/24/53 |
| **C. Batch-stop check** (`characterise_bir_false.py`, 1 preset) | **1–2** (real dir) · **5** (cold scratch first-run) | read-only; reproduced Baroque-53 on the fresh scratch regen |

### Derived per-evaluation cost + evaluations/hour (the checkpoint-P1 input)

| Case | composition | cost | evals/hr |
|---|---|---|---|
| **Per-preset** (natural fitter unit; with a single-preset a8, B≈4.7s) | A(1) + B/3 + C(1) ≈ 38 + 4.7 + 2 | **≈ 45 s** | **≈ 80** |
| **Per-preset** (today; a8 full-3 substitute, B=14s) | A(1) + B(14) + C(1) ≈ 38 + 14 + 2 | **≈ 54 s** | **≈ 67** |
| **All-presets** (shared-scope param) | A×3 + B(one full-3 run) + C×3 = 113 + 14 + 4 | **≈ 131 s** | **≈ 27** |

**Reading for Checkpoint P1 (design D-3 optimizer decision):** the **regen dominates (~85 % of a per-preset evaluation)**. At ~45–54 s / single-preset eval and ~131 s / all-presets eval, the derivative-free **coordinate/pattern search default is budget-feasible** — e.g. one coordinate sweep over the 19 `bounds()` params × ~5 steps ≈ 95 single-preset evals ≈ **70–85 min/pass**. Two cheap Phase-1 harness wins the numbers point to: (1) a **single-preset a8 mode** (cuts B from 14 s to ~5 s); (2) **fitting-split-only regen** (the 37–39 s full-corpus regen shrinks with the split, dropping the dominant term). The D-6 parameter-override materialization will make the regen the per-vector floor.

*(Bonus, not required: the a8 run reproduced the ratified variant-(b) root-agree baselines the fit starts from — Baroque 63.32 % / Jazz 62.37 % / Default 63.22 % at 326/352 coverage — and validated grid==oracle byte-identically on every covered piece.)*

---

## Task 5 — the sandwich + suites (acceptance)

### End-of-run sandwich — `characterise_bir_false.py` on the REAL per-preset dirs ×3

| preset | expected (CLAUDE.md) | measured | set-diff (both directions) |
|---|---|---|---|
| Baroque | 53 | **53** | **empty — MATCH** |
| Jazz | 24 | **24** | **empty — MATCH** |
| Default | 53 | **53** | **empty — MATCH** |

Verified by stem@tick set comparison against the CLAUDE.md 53/24/53 identity sets (script output: `SANDWICH_RESULT: ALL_MATCH_SETDIFF_EMPTY`). Corpus 0-dirty after. *(Corroboration: a8 independently reported batch_gate 53/24/53; the fresh scratch Baroque regen also reproduced 53.)*

### Suites (no golden refresh)

| suite | result |
|---|---|
| `composing_tests` | **1083 PASSED** |
| `notation_tests` | **53 PASSED** |
| `pipeline_snapshot_tests` | **11 PASSED** (ran WITHOUT `--update-goldens`; no refresh) |

Build note: no rebuild needed (no `src/` change; binaries current at HEAD).

---

## Reuse-vs-new + what retires

- **Reuses (verbatim, unmodified):** the three pinned instruments `run_bach_preset.py` / `a8_rebaseline_measure.py` / `characterise_bir_false.py`; the frozen corpus; the existing `analysistypes.h::bounds()` optimizer-range table; scoring_model.md / the confidence contract / the roadmap as reconciliation references.
- **New (committed):** `tools/param_manifest.json` (the deliverable, `981e942ded`); `cc_stage5_phase0_report.md` (this report); the roadmap Stage-5 rider (`0f05e78690`); the fold (`4b510b9ac7`). *(A throwaway scratch `verify_sets.py` was used for the sandwich set-diff — scratch, not committed.)*
- **Retires:** **NOTHING.** Read-only Phase 0 — no `src/` change, no tool-behavior change, no constant change, no fit. (Matches the dispatch's expectation exactly.)

---

## STOP conditions — none tripped (after the Task-0 ruling)

Task-0 dirty-set: raised, Cowork-ruled PROCEED (recorded above). Sandwich: 53/24/53 set-diff empty ×3. Suites: green. No `src/`/tools code touched; no write under `tools/corpus/`; no push. Corpus byte-untouched (proven). ≤5 unresolved manifest rows (actual: 0).

## For Checkpoint P0 (the user's call)

The material is in hand: the **fit surface** (78 rows: both 49 / production 10 / dormant 19; the D-9 shared-constant fact), the declared **freeze list** (17 rows), the **family homes** (continuous 45 / §6-block 8 / abstention 16 / squash+θ 4 / §15-13 5), the **cost numbers** (~45–54 s per-preset, ~131 s all-presets), the **doc-drift list** (4 defects, fixes queued for the next scoring-docs commit), and the **E-13 clean** finding. Sensitivity is NOT available (Phase-1b) — the optimizer/staging decisions sit at Checkpoint P1, not P0, per the design.
