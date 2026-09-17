# CC Instruction: Stage 4b-i — demote the declared-mode wall + measure the honest floor

## Authorization + scope

Implements the **ratified** `docs/stage4b_design.md` §2 (4b-i), itself implementing the user's
Stage-4 redirect (`docs/back_half_design.md` §4). Scoped by `cc_stage4b_scoping_dossier.md`
(Cowork-verified at source). **User ratified 2026-06-14.**

This is the project's **2nd intentional behavior change** — key resolution feeds chord emission
(`basisIndep`) and rendered RNs, so byte-identity ends on the **key AND chord axes** for affected
scores. That is expected and is the point; it is **measured and ratified, not shipped as a side
effect**.

**Zone:** ALL changes are inside `src/composing/` (CLAUDE.md autonomous zone) + `tools/`
(`batch_analyze`). **NO `src/notation/` or `src/engraving/` PRODUCTION file may be edited** — the
scoping proved none is needed (the bridge does no key inference; it overrides only the 21 mode priors
and delegates to the shared resolver — verified at both pref sites). If any such edit appears
necessary, **STOP and surface it**. The only off-limits-zone artifact that may change is
**snapshot-golden test data** (`pipeline_snapshot_tests --update-goldens`), refreshed ONLY for
DCML-verified-correct diffs.

**Never-guess:** read each call site before editing; tag every empirical claim `[probe]`/`[code]`/
`[oracle]`/`[unknown]`. **HELD — no commit** (4b-i is the floor measurement; the commit + the 4b-ii
plan are ratified on the data).

---

## The change — demote four declared-mode mechanisms + build the measurement toggle

### 1. The −7 penalty → a small declared HINT (`keymodeanalyzer`)
- **Site** [code]: `keymodeanalyzer.cpp:571-577` subtracts `prefs.declaredModePenalty` from candidates
  incompatible with the declared class. Default `7.0` at `keymodeanalyzer.h:319`.
- **Change:** reduce the default `7.0 → 1.0` (`[empirical — Stage-5 fits the final]`). Keep the
  application point and logic unchanged — a small magnitude makes it a genuine tiebreaker (flips the
  winner only within a ~1.0 note-based gap; cannot override clear note evidence) and it is droppable
  (not applied when `declaredMode == nullopt`).
- **⚠ Bounds gotcha** [code]: `keymodeanalyzer.h:454` declares the parameter bounds `{3.0, 15.0, true}`.
  `1.0` is **below** the current lower bound `3.0` — update the lower bound to allow the new small value
  **and 0.0** (e.g. `{0.0, 15.0, true}`), so the mode-absent / fully-dropped exploration is expressible.
  Verify there is no other clamp on this field.
- Update the `keymodeanalyzer.h:319` doc-comment to describe it as a **small declared hint, not a wall**.
  Renaming the field to `declaredHintWeight` is OPTIONAL (CC's discretion); if renamed, update ALL refs
  (the `--dump-key-candidates` `declaredPenalty` field, `.h:157`, any tests) in the same change.

### 2. The hard post-hoc promotion → REMOVE outright (`keyresolver`)
- **Site** [code]: `keyresolver.cpp:344-367` ("Strong declared-mode prior") promotes the highest-ranked
  declared-compatible result to the front **regardless of score gap** (a hard veto). **Remove this whole
  block.** The residual declared influence is now only the §1 hint.
- **⚠ DO NOT touch the hysteresis block immediately above** (`keyresolver.cpp:320-342`). It ALSO calls
  `promoteWinnerInPlace`, but it is **note-based** (`prevResult`-mode hysteresis), NOT a declared-mode
  mechanism — it stays. Only the §344-367 declared-mode promotion is removed. Confirm at source you are
  deleting the right block (the one guarded by `if (declaredMode.has_value())` with the "composer's
  intent overrides note-content inference" comment).

### 3. The piece-start anchor → note-based opening (`keyresolver`)
- **Site** [code]: `keyresolver.cpp:274-287` short-circuits the whole analysis at piece start when a
  declared mode exists, returning a declared anchor (`path:"anchor"`). **Remove this short-circuit** so
  the normal `analyzeKeyMode` lookahead path (`:289+`) runs from piece start.
- **Verify** [code/probe]: confirm the normal path handles `prevResult == nullptr` at piece start
  gracefully — the lookback window logic (`:262-266` when `tick < lookbackDuration`) and the
  insufficient-PCs fallback (`:314-318`). Report whether any degenerate piece-start case appears (if so,
  that is a finding to surface, not to patch around silently).

### 4. Partial-signature correction → UNCHANGED for 4b-i (`keyresolver`)
- `keyresolver.cpp:248` stays declared-gated (`if (declaredMode.has_value())`). It is inherently
  crutch-dependent (off mode-absent) — that is intended; the 4 partial-sig over-lock stems
  (bwv83.5/276/371/437) are recoverable only mode-present in 4b-i. A note-triggered detector is a
  DEFERRED later sub-step. Do not build it here.

### 5. The mode-absent measurement toggle (`tools/` + small in-zone resolver hook)
- Add `--ignore-declared-mode` to `batch_analyze` (`tools/`, writable) that forces
  `declaredMode = std::nullopt` into the resolver. The resolver derives `declaredMode` internally
  (`keyresolver.cpp:224-239`), so add a minimal `prefs`/parameter path to suppress it (composing-zone).
  **Flag default OFF = no-op** — prove this is byte-identical (0/353 × 3 presets with the flag unset)
  so the toggle itself introduces no behavior change; only the §1-3 demotions do.

### Doc sync (CLAUDE.md sync rule, same change-set)
Update `docs/scoring_model.md` (the `declaredModePenalty` term → small hint; the removed promotion +
anchor) and note the change in `docs/stage4b_design.md` / `back_half_design.md` §4. The
`docs/scoring_model.md` §2 template-count invariant is unaffected (no template change).

---

## Measurement (report all) — mode-present AND mode-absent

Regenerate all three presets (Default = user config, Baroque, Jazz) at the patched build. Score each
**both ways** (declared-mode present = the post-4a corpus state; and `--ignore-declared-mode` = the
no-crutch floor). Metric = corrected DCML-only granularity-robust **L1 `--key-breakdown`** (the
`a96f179f40` instrument), every root `[oracle]`-checked against music21 `RomanNumeral`.

1. **Key axis [probe]:** S2 (genuine key error) for each preset × condition. Report (a) mode-present S2
   delta vs the 4a baseline (1063 Default), and (b) the **mode-absent S2 floor** — the headline number
   (how much of 4a's +378 survives with no declared mode).
2. **The 7 over-lock stems [oracle]:** do bwv64.2 / bwv365 / bwv33.6 / bwv83.5 / bwv276 / bwv371 /
   bwv437 recover (mode-present and mode-absent separately)? bwv64.2 is the stress case.
3. **The 242 S2→S1 cases [probe]:** do they hold in S1 (global key correct) **mode-absent** — i.e. does
   note-based inference alone keep the global key right without the crutch?
4. **Chord-axis gate [probe/oracle]:** `characterise_bir_false.py` on the regenerated corpora, BOTH
   conditions, all three presets. Report the 57/23/57 identity-set delta (added/removed `stem@tick`).
   **DCML-adjudicate EVERY moved case** against the oracle. An **un-adjudicated BIR=false increase on
   any preset, either condition, is a HARD STOP** for ratification (surface immediately).
5. **Snapshots [oracle]:** report every `pipeline_snapshot_tests` golden diff with DCML adjudication;
   refresh (`--update-goldens`) ONLY verified-correct diffs; list each (stem@tick, before→after, DCML).
6. **Suites:** composing + notation green (report counts); note any test that pins the removed
   promotion/anchor — those are deliberate re-pins (re-pin to the new behavior, list them).

**No hard 4b-i key-axis pass-bar** — this run *measures* the floor. The full-4b mode-absent pass-bar
(OQ6) is set by the user AFTER this report. The 4b-i ratification gate is purely: chord-axis gate
movement fully DCML-adjudicated + no un-adjudicated BIR=false increase + suites green.

---

## Held / report

HELD — `git add` ok, **no commit**. Report `cc_stage4b_i_report.md`: the four demotions (with the
verified call sites + the bounds fix + the "hysteresis untouched" confirmation), the byte-identity
proof of the flag-off toggle, the full mode-present/mode-absent measurement (1-6), the gate delta with
per-case DCML adjudication, the snapshot diffs, and a first-pass read of what the mode-absent floor
implies for 4b-ii (which note terms to strengthen). Every number `[probe]`, every root `[oracle]`.

Note for the commit decision (later): the §5 `--ignore-declared-mode` toggle is byte-identical
(flag-off) and is separable into its own infra commit; the §1-3 demotions are the behavior-change
commit. Propose the split in the report; do not commit either yet.

## Stop conditions
- Any `src/notation/` or `src/engraving/` **production** edit appearing necessary (surface for
  authorization — the scoping says none is).
- Editing/deleting the wrong `promoteWinnerInPlace` block (the note-based hysteresis at :320-342 must
  stay; only the declared-mode promotion at :344-367 is removed).
- An un-adjudicated BIR=false increase on any preset, either condition (ratification stop).
- A degenerate piece-start case after removing the §3 short-circuit (report as a finding, don't patch around).
- The mode-absent floor collapsing far below the mode-present win is a **finding, not a failure** —
  report it plainly; it quantifies crutch-dependence and shapes 4b-ii.
