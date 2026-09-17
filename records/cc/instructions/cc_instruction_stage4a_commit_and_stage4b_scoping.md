# CC Instruction: commit Stage 4a (ratified) + read-only Stage 4b scoping

Two independent tasks. **Task 1** commits the already-verified Stage 4a patch (this instruction
is its ratification). **Task 2** is a READ-ONLY scoping investigation that produces the exact
`src/notation/` file-set for the user to authorize before any Stage-4b code is written. Do Task 1
first; Task 2 needs no build and touches no source.

---

## Task 1 — Commit Stage 4a (RATIFIED — you are authorized to commit)

Stage 4a was verified by Cowork at source (patch correct + minimal; only the authorized
`importmusicxmlpass2.cpp` touched; gate byte-identical 57/23/57 with identity sets unchanged;
isolation 79 zero-sig / 0 non-empty-sig; key win S2 −378 Default ≥ projected; no stop-condition).
The "HELD" hold is now **released for commit** by this instruction.

**Commit exactly the two already-staged files — nothing else:**
- `src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp`
- `CLAUDE.md` (the "Local patches — do not revert" entry)

Before committing, confirm `git diff --cached --name-only` lists **only** those two paths. The
report `cc_stage4a_mode_import_report.md` and the regenerated `tools/corpus/**` are gitignored —
**do not add them.** If anything else is staged, STOP and report.

**Commit message:**
```
fix(musicxml-import): retain declared <mode> for empty key signatures (Stage 4a local patch)

addKey() deduped key signatures on fifths only, so a 0-fifths key bearing an explicit
<mode> (parsed via setMode, e.g. <fifths>0</fifths><mode>minor</mode>) matched the
prevailing default fifths and was dropped, taking the declared mode with it
(KeyMode::UNKNOWN downstream) and breaking export/import round-trip of <mode>
(export writes it: exportmusicxml.cpp:2473-2497). Add an oldKeySig.mode() != key.mode()
term so a mode-bearing key at matching fifths is retained; a key matching in both fifths
AND mode still produces no KeySig (no spurious keysigs for plain C-major).

Local engraving patch (do NOT push upstream / see musescore/MuseScore#9444); documented in
CLAUDE.md "Local patches". Deliberate, measured behavior change: isolated to 79 zero-signature
stems, BIR gate byte-identical on all three presets (Baroque 57 / Jazz 23 / Default 57),
key-inference S2 -378 (Default). Report: cc_stage4a_mode_import_report.md.
```

**Do NOT push.** The user pushes (this is a local engraving patch they may keep off origin).
Report the new commit hash and the post-commit `git log --oneline -2`.

**Stop conditions (Task 1):** anything other than the two files staged; the working tree showing
unexpected tracked modifications under `src/` (report before committing — do not commit through it).

---

## Task 2 — Stage 4b scoping (READ-ONLY; produces the authorization request)

**Goal.** Stage 4b's design (per the user's redirect, ratified in `docs/back_half_design.md` §4):
make **note-based major/minor inference the PRIMARY mode/key signal**, **REMOVE the −7 declared-mode
wall** (not grade it), and demote declared mode to a **low-weight, droppable tiebreaker** consulted
only when the note-based inference is genuinely unsure. Stage 4a made the declared mode *available*
on the corpus; it is NOT the inference mechanism. This task SCOPES that change so the user can
authorize the precise off-limits file-set and Cowork can write the implementation instruction.

**Hard constraints:** READ-ONLY. No edits to any `src/` file. No commit. No build required (this is
source reading + measurement-planning). Reading `src/notation/` and `src/engraving/` is allowed;
editing them is NOT. Honor never-guess: read the actual call sites, quote them with file:line; tag
every empirical claim `[code]` (read in source) / `[probe]` (measured) / `[unknown]` (state it,
don't guess).

Deliverable: `cc_stage4b_scoping_dossier.md` (gitignored working file). It must contain:

1. **The −7 wall, located and characterized [code].** Find the actual −7 declared-mode penalty in
   the resolver (`src/composing/analysis/key/*` and/or `keymodeanalyzer`/`keyresolver`). Quote the
   exact code (file:line), how the penalty is applied, what reads it, and how `declaredModeOrdinal`
   / the declared mode flows in. Confirm whether removing it is purely a composing-zone change.
   (Cross-ref the key-emission dossier's "−7 wall" and the `--dump-key-candidates` term it appears in.)

2. **The current note-based mode/key inference, inventoried [code].** The KeyModeAnalyzer terms
   (tonal-centre, scale-degree salience, the ±0.20 Ionian/Aeolian triad prior, etc.) — what exists,
   which are strong, which are the weak link on the 0-sig major/minor decision. Identify what
   "strengthen note-based inference" concretely means in code and WHERE it lives (expect: composing
   autonomous zone). State explicitly which proposed changes are inside the autonomous zone vs not.

3. **KeyArea spans + hysteresis→path: the off-limits surface [code].** Locate the current
   key/mode stabilization, hysteresis, and any KeyArea-equivalent + the bridge wiring that would
   carry KeyArea to consumers — the parts that live in `src/notation/` (and/or `src/engraving/`).
   Produce a **precise file-set table**: each off-limits file, the specific function(s), and a
   one-line description of the change Stage 4b would make there. This table IS the authorization
   request. If the design can be achieved with FEWER (or zero) off-limits files — e.g. KeyArea
   computed in composing and only thin bridge plumbing in notation — say so and show the minimal set.

4. **Measurement plan under BOTH conditions [probe-design].** Stage 4b must be measured
   **mode-present AND mode-absent** (the shipped product often lacks a reliable declared mode), or
   we overfit to a corpus input the product won't have. Specify: how to produce the mode-absent
   condition (e.g. strip/ignore declared mode), the metric rung (L1 `--key-breakdown`, the
   granularity-robust unit), and the pass/fail framing. Name the concrete targets to recover:
   the **7 over-lock stems** (bwv64.2, bwv365, bwv33.6, bwv83.5, bwv276, bwv371, bwv437) and the
   **242 S2→S1** cases from the 4a report; and state what must NOT regress (the 47 improved + the
   −378 win should largely survive WITHOUT the declared-mode crutch — that is the real test).

5. **Behavior-change surface called out.** Stage 4b is the project's 2nd intentional behavior
   change: key feeds chord emission (`basisIndep`), so byte-identity ends on the CHORD axis too,
   not just the key axis. Note that the gate (57/23/57) and chord-axis `.ours.json` may move, will
   be DCML-adjudicated and ratified, and that this is expected — flag it, don't pre-decide it.

6. **Open questions for Cowork/user.** Anything that needs a design decision before implementation
   (e.g. how "genuinely unsure" is defined for the droppable-hint fallback; whether KeyArea is
   built now or deferred; partial-signature interaction). State unknowns explicitly.

**Do NOT** build the resolver change, strengthen inference, touch the wall, or edit any notation
file in this run. Scoping + authorization request only. The implementation is a later instruction,
gated on the user authorizing the §3 file-set.

**Stop conditions (Task 2):** discovering the change cannot avoid editing an off-limits file to even
*measure* (it shouldn't — measurement is read-only); the −7 wall not being where the dossier expects
(report the real location); any temptation to "just try" an edit (don't — read-only).
