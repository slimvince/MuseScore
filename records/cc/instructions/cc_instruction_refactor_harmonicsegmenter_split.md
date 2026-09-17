# CC Instruction — Refactor: split harmonicsegmenter.cpp (byte-identical)

> **Next pure split** (assessment §5, candidate #3). `harmony/harmonicsegmenter.cpp` (943) conflates the
> boundary-detection **primitives** (`collectNoteChangeTicks` et al.) with the `greedyExpandSegmentation`
> policy god-function. **STRICTLY BYTE-IDENTICAL — pure code movement, NO logic/scoring/inference change.**
> **Commit locally → Cowork verifies the committed object** (binding workflow).

---

## §1 — The purity rule (same as the prior splits)
Only: (a) cut a function/helper **verbatim** out of `harmony/harmonicsegmenter.cpp` into a new sibling TU;
(b) prefix any moved anon-namespace helper (internal-linkage rename ⇒ byte-identical); (c) register the new
`.cpp` in `CMakeLists.txt`. **No logic/constant/behavior change. Move ONLY already-verbatim-liftable code.**
The declaring header stays unchanged. **As in sectionanalyzer: if a piece is an anon-namespace helper whose
sole caller is the residual, moving it needs a linkage promotion + new declaration — that is NOT a verbatim
move → STOP and surface it, do not force.** If a move can't be byte-identical → STOP.

## §2 — The split (per assessment §5)
Peel the **boundary-detection primitives** (`collectNoteChangeTicks` and the sibling boundary helpers the
assessment named) off the `greedyExpandSegmentation` policy function → a new TU (e.g.
`harmony/segmentationprimitives.cpp`), leaving `greedyExpandSegmentation` (+ whatever is genuinely entangled
with it) as the residual. **Re-confirm each candidate's call sites + linkage at source first** (committed
object / fresh reads): move a function only if it is **already external/header-declared OR an anon-ns helper
that can move WITH all its callers** (so no linkage promotion is needed). Anything that would need a
linkage change to separate → surface, don't move.

## §3 — Acceptance gate (MANDATORY — byte-identical)
1. Build green. 2. `composing_tests` + `notation_tests` pass. 3. `pipeline_snapshot_tests` 11/11, **no
`--update-goldens`**. 4. 3-preset `.ours.json` **0-diff** + **BIR 57/23/57**. Any deviation = STOP.

## §4 — Deliver: COMMIT LOCALLY (unpushed) → Cowork verifies the committed object
Do the split + gate in your worktree, then **commit locally, UNPUSHED**: *refactor: split
harmonicsegmenter.cpp — lift boundary-detection primitives into own TU (byte-identical).* Report the
**commit hash** + gate result + move list in `cc_refactor_harmonicsegmenter_report.md`. **Cowork verifies the
COMMITTED OBJECT** (`git show <hash> --numstat` move-only + the verbatim `comm` check + `:path`) — the only
reliable path. **If a problem, revert** (`git reset --soft HEAD~1`). **Do NOT push.**

## §5 — Stop conditions
- Any non-byte-identical step (golden / `.ours.json` / BIR / test move) → STOP.
- Any logic/scoring/inference change or "fix" → STOP (purity violation).
- A piece needing a linkage promotion / new declaration to separate (the sectionanalyzer Pass-4 case) →
  STOP, surface (do not force — it is not a verbatim move).
- Any edit outside the new TU + `harmonicsegmenter.cpp` + `CMakeLists.txt` (+ a declaring header if it
  genuinely must change — flag it) → STOP. Any push → STOP.
