# CC Instruction — doc-truth: sync the gate baseline + as-built comments (DOCS/COMMENTS ONLY, no code logic)

> **Context.** The L1–L4 audit (`cowork_l1l4_architecture_audit.md`) found a **high-impact contradiction**: the
> session-start docs disagree on the live BIR gate. `CLAUDE.md` is on the ratified **53/24/53**; `STATUS.md` and ~8
> other docs still present the stale **57/23/57**. This is the "immediate, ungated" item folded into the stabilization
> plan — **doc + comment corrections only, zero code-logic change, zero gate risk.** **`CLAUDE.md` is the SOURCE OF
> TRUTH** for the 53/24/53 set (with stem@tick identities); this is a **sync TO CLAUDE.md, NOT a re-measurement** —
> invent no number, run no corpus.
>
> **Two hard rules for this pass:**
> 1. **Do NOT rewrite history.** `STATUS.md` is a session log; its *past* entries ("GATE RE-BASELINED 13/7/14 →
>    57/23/57") were accurate **for those sessions** and must stay. Correct only the **current-state / live-gate
>    claims**, and add a dated note that the L3-wiring delta moved it to 53/24/53.
> 2. **Touch no `.cpp`/`.h` logic, no tool/script logic, no test logic.** Only doc files (`.md`) and **code comments**
>    (e.g. CMake `#` comments). Nothing that changes a build artifact or a measurement.

## §0 — Preamble: protect the uncommitted Cowork docs (sweep-protection)
Commit, **local-only**, the uncommitted Cowork doc edits now in the working tree — the audit, the plan update, and the
Phase-4 instruction/design corrections: `cowork_l1l4_architecture_audit.md`, `cowork_l1l3_stabilization_plan.md`,
`cc_instruction_tpc_capability_build.md`, `cowork_tpc_capability_design.md` (and any other `cowork_*`/`cc_instruction_*`
with unstaged edits). Message: `docs(cowork): L1-L4 audit + plan fold-in (Phase 5/6) + Phase-4 span-scope correction`.
Confirm `git show --stat` lists only those doc files (no source).

## §1 — STATUS.md: correct the current-state gate (not the history)
- Update the **top / "Last updated" current-state** so the live gate reads **Baroque 53 / Jazz 24 / Default 53**, with
  a one-line dated note: *"L3-wiring delta (−4/+1/−4) moved the prior 57/23/57 → 53/24/53; case-identity sets in
  CLAUDE.md; the set, not the integer, is the gate."*
- **Leave the historical session entries intact** — do not change "57/23/57" where it records what a past session did.
  If a past entry is the *only* place a reader would look for "current," add a forward-pointer, don't rewrite it.

## §2 — Reference/operational docs that state the CURRENT gate → 53/24/53
For each doc the audit flagged, correct **only statements asserting the present/live gate or a must-hold invariant**;
take the numbers + identities from `CLAUDE.md` (do not re-derive):
- `docs/score_inventory.md`, `docs/decoder_design.md`, `docs/implementation_roadmap.md` — operational guidance citing
  "57/23/57" as current → **53/24/53**.
- The stage-design docs (`docs/beam_widening_design.md`, `docs/back_half_design.md`, `docs/stage6_functional_layer_design.md`,
  `docs/scoped_joint_design.md`, `docs/stage4d_local_modulation_design.md`, `docs/stage4c_cadence_key_design.md`,
  `docs/stage4b_design.md`) — these are largely **historical records of a past stage**. **Do NOT rewrite their bodies.**
  Where one states "the gate is now 57/23/57" as a live must-hold, add a **one-line superseding note**: *"(Superseded
  2026-06-26: current gate 53/24/53 — see CLAUDE.md.)"* Prefer a note over a rewrite when in doubt.
- If you find a doc citing the older `13/7/14`, leave it (clearly historical) unless it claims to be current.

## §3 — As-built code comments (comment-only; the headers are already correct)
Correct the stale **CMake comments** the audit flagged — `src/composing/analysis/CMakeLists.txt` still says the
`slicer`, `keymodesequence`, and `jointkeydecision` are "NOT wired" / "ISOLATED," but they are wired
(`regionanalyzer.cpp:475/579/581`; the headers already say so). Make the comments as-built-accurate. **Comment text
only — change no target, no source list, no flag.**
- Optional-minor: `CLAUDE.md` references `build_and_test.md`; the file on disk is `BUILD_AND_TEST.md` — fix the casing
  in the reference if trivial.

## §4 — Verify + LIST the orphaned fixtures / stale tool-defaults (do NOT delete or change tool logic here)
The audit flagged orphaned test fixtures and stale tool corpus-dir defaults. **This pass does not remove files or edit
tool code** (deletions and tool-logic changes are their own decisions). Instead:
- **Re-verify zero references** (whole-repo grep) for: `chord_analysis_test.{musicxml,json,py}` (the literal "content
  moved" stubs), `data/mono_smoke_test.musicxml`, `data/solid theory.musicxml`. Report each as confirmed-orphan or not.
- **List** the stale tool defaults (`run_bach_preset.py`, `music21_batch.py`, the iter-diagnostic scripts defaulting to
  the deprecated shared `tools/corpus`) — report, do not edit.
- End with a short "cleanup candidates (need explicit go)" list. Removal/tool-fixes are a **separate** ratified step.

## §5 — Gate (doc/comment-only ⇒ build output unchanged)
- **No `.cpp`/`.h` logic, no test, no tool/script logic touched** — confirm `git diff` for the commit shows only `.md`
  files and CMake **comment** lines. Both suites and snapshots are unaffected (nothing compiled changed); you need not
  re-run the corpus. If any non-comment source line appears in the diff → STOP (scope breach).
- The gate numbers in the docs after this pass must **match CLAUDE.md exactly** (53/24/53 + identity sets).

## §6 — Deliver
Commit **locally (unpushed)**: the doc + comment corrections (the §0 Cowork-doc commit is separate, first). Write
`cc_doctruth_gate_sync_report.md` (gitignored): every file changed with the before→after gate text, confirmation that
no history was rewritten and no source logic touched, and the §4 cleanup-candidate list.

## §7 — Stop conditions
- You invent or re-measure a gate number (anything not taken from CLAUDE.md) → STOP.
- You rewrite a historical STATUS.md / stage-design entry instead of annotating it → STOP.
- Any non-comment source, test, or tool-logic line enters the diff → STOP (this is docs/comments only).
- You delete a fixture or change a tool default → STOP (that is the separate §4 follow-up, needs explicit go).
- A push targets `upstream` → STOP.
