# CC Instruction — Refactor #1 (BUILD): chordanalyzer.cpp byte-identical layer-split

> **Execute the Cowork-verified split plan** (`cc_refactor1_split_design_dossier.md`, verified at source:
> file 3,679 lines; competition already extracted at `:2766`; seams clean). **STRICTLY BYTE-IDENTICAL — pure
> code movement, NO logic/scoring/inference change of any kind** (user constraint, 2026-06-16: "only
> refactoring into proper layers — no fixing or improving inferring"). 5 steps, each independently
> byte-identical-gated. **HELD for Cowork verification before commit; local, UNPUSHED.**

---

## §1 — The purity rule (the whole point — read first)

This is a **refactor**, not a change. The ONLY edits permitted are: (a) cut a body/helper out of
`chordanalyzer.cpp` and paste it **verbatim** into a new TU, (b) **rename** a moved anonymous-namespace
helper to its prefixed name (internal linkage ⇒ byte-identical), (c) add the new `.cpp` to
`analysis/CMakeLists.txt`, (d) at the end, update `docs/scoring_model.md` **file-location references** only.
- **Do NOT change any logic, constant, threshold, template, gate, or scoring/inference behavior.**
- **Do NOT "fix" the surfaced tangles** (T1–T4): do not de-triplicate the diatonic-scale tables, do not move
  `buildChordResult`, do not touch the gate bodies. They stay exactly as-is (refactor #2 / the audit own them).
- If any move cannot be made byte-identical without a logic change → **STOP and surface** (do not "improve"
  it to make it fit). `chordanalyzer.h` stays **unchanged** (the stable boundary).

## §2 — Scope
`src/composing/analysis/chord/` (the 5 new sibling TUs + the shrinking residual) + `analysis/CMakeLists.txt`
+ (final step) the `docs/scoring_model.md` location pointers. Nothing else.

## §3 — The 5 steps (design §4 order; per-TU includes + prefixes per design §3/§5.2)
Leaf/independent first, the gate layer **last** (the refactor-#2 target):
1. **`chordsymbolformatter.cpp`** — the formatter fns + Group A helpers (44–619) + `isValidBassNoteName` +
   tonicization helpers (3199–3239) + the Nashville block (3384–3464). Prefix moved anon-ns helpers **`csf*`**.
2. **`chordvoicing.cpp`** — `chordTonePitchClasses`, `closePositionVoicing` (no anon-ns helpers).
3. **`chorddiagnose.cpp`** — `diagnoseChord` (include `function/harmonicfunctionlayer.h`).
4. **`chordpostpasses.cpp`** — `applyIter8691Pedal` + `isBassChordTone` (prefix **`cpt*`**).
5. **`postscoringgates.cpp`** — `applyPostScoringGates` (+ its margin constants 1723–1725). **LAST.**

Residual `chordanalyzer.cpp` = the vertical oracle (scoring constants/helpers + `TemplateDef` + the
`kTemplateCount`-derived `templates` array + the three score matrices + `detectExtensions` +
`buildChordResult` + `analyzeChord` + factory) — these **do not move** (the size model stays put, design §5.1).

## §4 — Per-step acceptance gate (MANDATORY after EACH step — all must hold)
1. Build green (`setup_and_build.bat`).
2. `composing_tests` + `notation_tests` pass.
3. `pipeline_snapshot_tests` 11/11 — **no `--update-goldens`** (output is unchanged; a golden move means the
   step was NOT byte-identical → STOP).
4. 3-preset corpus regen `.ours.json` **0-diff** (Baroque/Jazz/Default) + **BIR 57/23/57**
   (`characterise_bir_false.py`).

**Any deviation (golden move, `.ours.json` diff, BIR move, test fail) = STOP** — the move introduced a
behavior change; do not proceed, surface it. Report each step's gate result.

## §5 — Deliver: HELD + report → Cowork verifies the diff is pure movement → commit
Write `cc_refactor1_split_build_report.md` (HELD): the per-step acceptance-gate results (all 5 byte-identical)
+ the final `scoring_model.md` reference sync. **Present HELD — do NOT commit yet.** Cowork verifies at
source that the `git diff` is **move-only** (each function's lines deleted from `chordanalyzer.cpp` appear
verbatim — modulo the `csf*`/`cpt*` prefix renames — in its new TU; no logic line changed). On Cowork's
confirmation, **commit (local, UNPUSHED)** as ONE commit: *refactor: split chordanalyzer.cpp into
single-responsibility layer TUs (byte-identical; oracle residual + formatter/voicing/diagnose/post-passes/
gates); isolates the gate layer for refactor #2.* Sync `docs/scoring_model.md` location pointers in the same
commit (CLAUDE.md sync rule). **Do NOT push.**

## §6 — Stop conditions
- Any non-byte-identical step (golden / `.ours.json` / BIR / test move) → STOP, surface.
- Any logic / constant / scoring / inference change, or any tangle-"fix" (T1–T4) → STOP (purity violation).
- Any change to `chordanalyzer.h` (beyond none) or any edit outside §2's scope → STOP.
- A move that needs a logic change to compile/work → STOP, surface (do not adapt the logic).
- Committing before Cowork verifies the move-only diff → STOP (present HELD first).
- Any push → STOP.
