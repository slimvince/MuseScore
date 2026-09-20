# CC report — doc-truth gate sync (53/24/53) + as-built comment fix

**Date:** 2026-06-26 · **Scope:** docs + comments only · **Source of truth:** `CLAUDE.md` (gate section, **53/24/53**).
This was a **sync TO CLAUDE.md, not a re-measurement** — no corpus regenerated, no gate integer invented or re-derived;
every new number was taken from CLAUDE.md. Two commits, both **local (unpushed)**: the §0 Cowork-doc commit (separate,
first), then the doc+comment corrections.

---

## §0 — Cowork docs protected (separate commit, first)

Commit **`4bc5e2e1f0`** — `docs(cowork): L1-L4 audit + plan fold-in (Phase 5/6) + Phase-4 span-scope correction`.
`git show --stat` lists **only doc files, no source**:

| File | Δ |
|---|---|
| `cowork_l1l3_stabilization_plan.md` | +modified |
| `cowork_l1l4_architecture_audit.md` | +new (162 lines) |
| `cowork_tpc_capability_design.md` | +modified |

`cc_instruction_tpc_capability_build.md` was named in the instruction but is **absent from the working tree** (not in
`git status`, not tracked) → nothing to commit for it. No other `cowork_*`/`cc_instruction_*` had unstaged edits.

---

## §1 — STATUS.md current-state → 53/24/53 (history preserved)

- **Added** a new top entry `*Last updated: 2026-06-26 (session 7 — DOC-TRUTH GATE SYNC …)*` stating the live gate
  **Baroque 53 / Jazz 24 / Default 53**, the L3-wiring delta (−4/+1/−4) note, and the CLAUDE.md identity-set pointer
  ("the SET, not the integer, is the gate").
- **Demoted** the prior `*Last updated: 2026-06-14 …*` line to `*Previous: 2026-06-14 …*` — a one-word prefix change
  (the doc's own append convention); **its content is byte-unchanged**, including its `57/23` figures.
- **No historical "Previous:" entry was edited.** Every prior session log (incl. the 2026-06-13 "GATE RE-BASELINED
  13/7/14 → 57/23/57 … STAGED/HELD" record) is **intact** — those `57/23/57` strings record what those sessions did.

## §2 — Operational + stage-design docs

**Operational docs (direct correction of live-gate citations → 53/24/53):**

| File | line(s) | before → after |
|---|---|---|
| `docs/score_inventory.md` | 27 | `(Baroque 57, Jazz 23, Default 57 — re-baselined 2026-06-13; see CLAUDE.md)` → `(Baroque 53, Jazz 24, Default 53 — re-baselined 2026-06-13 + L3-wiring delta 2026-06-26; …)` |
| `docs/score_inventory.md` | 144 | `(Baroque 57, Jazz 23, Default 57 — re-baselined 2026-06-13)` → `(Baroque 53, Jazz 24, Default 53 — … + L3-wiring delta 2026-06-26)` *(wrapped occurrence, fixed in a second pass)* |
| `docs/score_inventory.md` | 175, 185 | `Baroque 57 / Jazz 23 / Default 57` → `Baroque 53 / Jazz 24 / Default 53` |
| `docs/decoder_design.md` | 259–261 | `the gate is now **Baroque 57 / Jazz 23 / Default 57** … must hold against 57/23/57` → `**Baroque 53 / Jazz 24 / Default 53** … must hold against 53/24/53` (added "L3-wiring delta moved 57/23/57 → 53/24/53"; **13/7/14 and 24/13 left as historical/secondary**) |
| `docs/decoder_design.md` | 544 | `→ Default 57, see CLAUDE.md` → `→ Default 53 (L3-wiring delta 2026-06-26), see CLAUDE.md` |
| `docs/decoder_design.md` | 588 | table `→ **57**` → `→ **53** (L3-wiring delta)` |
| `docs/decoder_design.md` | 589 | table `→ **57 / 23 / 57** (CLAUDE.md)` → `→ **53 / 24 / 53** (CLAUDE.md; L3-wiring delta)` |
| `docs/implementation_roadmap.md` | 14–17 | `gate Baroque 57 / Jazz 23 / Default 57` → `gate Baroque 53 / Jazz 24 / Default 53`; `(false-halves = the 57/23 gate)` → `(false-halves = the then-57/23 gate; the L3-wiring delta later moved it → 53/24/53)`. **Secondary split `47/57 Baroque / 81/23 Jazz` left as-measured** (not re-measured post-delta; CLAUDE.md still lists it). |

**Stage-design docs (one superseding note; bodies NOT rewritten):** each got an inline
`*(superseded 2026-06-26: live gate now 53/24/53 — L3-wiring delta; CLAUDE.md authoritative)*` at its first
57/23/57 must-hold; the historical 57/23/57 figures remain as the pre-delta record.

| File | anchor |
|---|---|
| `docs/beam_widening_design.md` | re-baseline note block (parked/shelved doc) — superseding line appended |
| `docs/back_half_design.md` | `the **57/23/57** gate identity sets (… Baroque 57 / Jazz 23 / Default 57, see CLAUDE.md…)` |
| `docs/stage6_functional_layer_design.md` | `**BIR gate 57/23/57 byte-identical**` |
| `docs/scoped_joint_design.md` | `byte-identical: BIR 57/23/57, snapshots 11/11` |
| `docs/stage4d_local_modulation_design.md` | `the BIR gate (57/23/57) is **medium-risk**` |
| `docs/stage4c_cadence_key_design.md` | `(gate 57/57/23 byte-identical, the §3 decoupling proof)` |
| `docs/stage4b_design.md` | `the 57/23/57 BIR gate **will** move` |

**Two scope extensions beyond the literal §2 list (documented here):** both assert the *live* gate, same contradiction
class as the flagged docs.
- `BUILD_AND_TEST.md` — **direct correction** (L177 `Baroque 57 / Jazz 23 / Default 57` → `53 / 24 / 53` + L3-wiring
  delta note; L296 `now **57/23**, Default 57` → `now **53/24**, Default 53`). Rationale: it is the **other CLAUDE.md
  mandated session-start read** ("Always read these two files…"), so leaving it stale defeats the pass; it delegates
  identity sets to CLAUDE.md, so the integer swap is clean.
- `ARCHITECTURE.md` — **superseding note only** (L856), not a rewrite. Rationale: its body carries an embedded
  Default identity-swap detail (`{bwv227.7@18120, bwv60.5@30960} ↔ {bwv187.7@19200, bwv227.7@18000}`) that **diverges
  from CLAUDE.md's current (caveated) Default-53 set**; reconciling it would be a re-derivation, so I annotated instead.

## §3 — As-built CMake comments (comment-only)

`src/composing/analysis/CMakeLists.txt` — **3 comment blocks**, every changed line is a `#` line; **no `target_sources`
path, no flag, no source-list entry touched** (verified by `git diff` — all `${CMAKE_CURRENT_LIST_DIR}/…` lines are
unchanged context). Wiring verified at source before editing:

| module | was | now (as-built, verified) |
|---|---|---|
| `keymodesequence` | "ISOLATED … NOT wired … runs only under `--decode-keymode`; wiring is the next increment" | **WIRED live** — `KeyModeSequenceDecoder::decode` @ `regionanalyzer.cpp:581` replaces the per-region key argmax at the Pass-1 seam; still also a `--decode-keymode` diagnostic |
| `slicer` | "It is ISOLATED — NOT wired into the live analysis pipeline; consumed at layer 3" | **WIRED live** — `changePointSlices` @ `regionanalyzer.cpp:579`, consumed at layer 3 by the key/mode sequence decoder |
| `jointkeydecision` | "Built + MEASURED only; invoked solely from `--dump-joint-key`, never the production resolver (wiring is J-key-ii)" | **WIRED into the production resolver** via `applyJointKeyWiring` (J-key-iii) @ `regionanalyzer.cpp:1369`, **but gated on `jointKeyWiringEnabled()` (default OFF)** → production byte-identical by default; still `--dump-joint-key` |

Verification: `regionanalyzer.cpp` L556–583 (live Layer-3 decode), L355/L1365–1370 (`applyJointKeyWiring` gated OFF by
default). `cadencekeyanchor` / `localmodulationdetector` CMake comments say "not wired" and **remain correct** (no
`regionanalyzer.cpp` reference) — left untouched. `chordslicedecoder` / `tonicizationlabeler` "NOT wired" comments are
**correct** (still production-dead per audit Q5) — left untouched.

**§3 optional-minor:** `CLAUDE.md:41` `build_and_test.md` → `BUILD_AND_TEST.md` (filename casing only; on this
case-insensitive mount they resolve to the same file). **No gate content in CLAUDE.md was touched.**

## §5 — Gate (build output unchanged)

`git diff` for the corrections commit = **14 `.md` files + `src/composing/analysis/CMakeLists.txt` (comment lines
only)**. No `.cpp`/`.h` logic, no test, no tool/script logic. Nothing compiled changed → both suites + snapshots are
unaffected and were **not** re-run (correctly). The post-pass current-gate text matches CLAUDE.md exactly: **53/24/53**.

---

## §4 — Orphan re-verification + stale-default list (REPORT ONLY — no deletions, no tool edits)

Whole-repo grep performed; **the audit's orphan list is partly inaccurate — corrected below.**

| candidate | verdict | evidence |
|---|---|---|
| `src/composing/tests/chord_analysis_test.musicxml` / `.py` / **`_expected.json`** | **CONFIRMED ORPHAN** | `grep chord_analysis_test` → only the 3 literal "content moved" stub files themselves + the audit + a `score_inventory.md:50` fixture-list mention. No test/tool loads them. *(Note: the JSON is `chord_analysis_test_expected.json`, not `…_test.json` as the audit wrote.)* |
| `src/composing/tests/data/mono_smoke_test.musicxml` | **NOT AN ORPHAN — audit is WRONG** | `tools/test_batch_analyze_regressions.py:116–137` loads **both** `mono_smoke_test.mscx` and `mono_smoke_test.musicxml` and asserts on each. Do **not** delete. |
| `src/composing/tests/data/solid theory.musicxml` (space-named) | **NOT A CLEAN ORPHAN** | Not loaded by any test (tests load `nm_solid_theory.mscx`; composing_tests can't import MusicXML), **but** referenced by name in `note_model_tests.cpp:88,118` **comments** (documents the .mscx fixture's provenance) + `tools/refresh_divergence_20260424/solidtheory_*.json` (`source` field) + `score_inventory.md:51`. Removing it orphans the documented provenance; if removed, the `note_model_tests.cpp` provenance comments need updating (a `.cpp`-comment change — separate scope). |

**Stale tool corpus-dir defaults (deprecated shared `tools/corpus`) — list only:**
- `tools/run_bach_preset.py:250` `--corpus-dir` default `tools/corpus`; `:288` output default `tools/corpus_<preset>`
  (flat sibling, not the `tools/corpus/<preset>` per-preset layout). Works when invoked per CLAUDE.md (which passes
  `--output-dir tools/corpus/<preset>`), but the built-in default predates the per-preset layout.
- `tools/music21_batch.py:26` `--output` default `tools/corpus`.
- `tools/decode_keymode_corpus.py:104` (`--corpus-dir`), `tools/decode_chord_corpus.py:105` (`--corpus-dir`).
- `tools/cc_layer3_keymode_baseline.py:1569/1585`, `tools/cc_layer4_chord_baseline.py:334`,
  `tools/cc_layer4_residual_decompose.py:305` (`--corpus-root` defaults).
- Iter/diag scripts hardcoding `tools/corpus/*.ours.json`: `check_iter46_candidates.py:27`,
  `diag_iter63_genuine6_enumerate.py:5`, `diag_iter28_gate_k.py:15`, `enumerate_near_agree_iter38.py:93`,
  `iter45_step4_cluster_b.py`, `iter45_cluster_a_diagnostic.py`.
- inject/fix utilities referencing `tools/corpus`: `fix_keysig.py:100`, `inject_dcml_rn.py:11`, `inject_m21_rn.py:179`,
  `inject_dcml_rn_qa.py:11`.
- **Already fixed (NOT offenders):** `analyze_inversion_errors.py` (default `tools/corpus/baroque`, validated; keeps a
  deprecated `--ours-dir` alias) and `characterise_bir_false.py` (requires `--corpus-dir`, no shared default).

**Out-of-scope staleness discovered (flag for Cowork — NOT touched; §5 limits this pass to `.md` + CMake comments):**
- `src/composing/analysis/slicing/slicer.h:67` **also** says "It is NOT wired into the live analysis pipeline" — same
  staleness as the CMake comment just fixed. **The §3 premise "the headers already say so [are correct]" does NOT hold
  for `slicer.h`.** A `.h`-comment fix is needed in a separate pass.
- `src/composing/analysis/harmony/harmonicsegmenter.cpp:155` "It is isolated/not wired in" — refers to a *different*
  special-case path; verify independently before any change.
- `src/composing/analysis/chord/chordslicedecoder.h:77` "NOT wired into the live analysis" — **correct** (still
  production-dead); leave.

### Cleanup candidates (need explicit go — each is a SEPARATE ratified step)
1. Delete the `chord_analysis_test.{musicxml,py,_expected.json}` stubs (+ drop their `score_inventory.md:50` mention).
2. Fix the stale `slicer.h:67` `.h` comment (and check `harmonicsegmenter.cpp:155`) — a header-comment pass.
3. Repoint the stale tool corpus-dir defaults (run_bach_preset / music21_batch / decode_* / cc_layer* / iter-diag /
   inject-fix) to the per-preset layout — a tool-logic change.
4. **Do NOT** delete `mono_smoke_test.musicxml` (live) or `solid theory.musicxml` (provenance-referenced) — the audit's
   orphan claim for these is incorrect/incomplete.

## §7 — Stop conditions: none tripped
No gate number invented or re-measured (all taken from CLAUDE.md). No historical STATUS.md / stage-design entry
rewritten (added/annotated only). No non-comment source / test / tool-logic line entered the diff. No push to
`upstream` (both commits local, unpushed).
