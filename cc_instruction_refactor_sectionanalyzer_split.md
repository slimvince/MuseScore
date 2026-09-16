# CC Instruction — Refactor: split sectionanalyzer.cpp (byte-identical)

> **Next pure split** (assessment §5, candidate #2). `sectionanalyzer.cpp` (971) conflates cadence + pivot
> detection (~200 lines, fully independent) and Pass-4 stabilization with the section orchestration.
> **STRICTLY BYTE-IDENTICAL — pure code movement, NO logic/scoring/inference change** (refactoring into
> layers only). **Commit locally → Cowork verifies the committed object** (the binding workflow).

---

## §1 — The purity rule (same as #1 / regiontonecollector)
Only permitted edits: (a) cut a function/helper verbatim out of `section/sectionanalyzer.cpp` and paste it
unchanged into a new sibling TU; (b) prefix any moved anon-namespace helper (internal-linkage rename ⇒
byte-identical); (c) register the new `.cpp` in `analysis/CMakeLists.txt`; (d) `docs/scoring_model.md`
location pointers only, IF a moved block is referenced there. **No logic/constant/behavior change. Do NOT
"fix" anything** (incl. the known Pass-4 details — move, don't touch). The declaring header(s) stay
unchanged. If a move can't be byte-identical → STOP, surface.

## §2 — The split (per assessment §5)
Two clean extractions; do whichever are genuinely independent, byte-identically:
- **Cadence + pivot detection** (~200 lines, "fully independent" per the assessment) → a new TU (e.g.
  `section/sectioncadencedetection.cpp`).
- **Pass-4 stabilization** → a new TU (e.g. `section/sectionstabilization.cpp`), IF it extracts clean.
Leaving the section orchestration as the `sectionanalyzer.cpp` residual.
**Re-confirm each moved function's call sites at source first** (committed-object / fresh reads) — move only
what is genuinely self-contained; if a piece is entangled with the residual (shared mutable state, a helper
split across the seam), STOP and surface it rather than forcing the split. Do them as **separate steps** if
both extract, each with its own gate (§3).

## §3 — Acceptance gate (MANDATORY per extraction — byte-identical)
1. Build green. 2. `composing_tests` + `notation_tests` pass. 3. `pipeline_snapshot_tests` 11/11, **no
`--update-goldens`** (golden move ⇒ NOT byte-identical ⇒ STOP). 4. 3-preset `.ours.json` **0-diff** + **BIR
57/23/57**. Any deviation = STOP.

## §4 — Deliver: COMMIT LOCALLY (unpushed) → Cowork verifies the committed object
Do the split + gate **in your worktree** (your git is fresh/authoritative), then **commit locally, UNPUSHED**:
*refactor: split sectionanalyzer.cpp — lift cadence/pivot detection [+ Pass-4 stabilization] into own TU(s)
(byte-identical).* Report the **commit hash** + gate result + move list in
`cc_refactor_sectionanalyzer_report.md`. **Cowork verifies the COMMITTED OBJECT** (`git show <hash> --numstat`
move-only + the verbatim-move `comm` check + `:path` content) — the only fully-reliable path. **If Cowork
finds a problem, revert** (`git reset --soft HEAD~1`). **Do NOT push.** (If both extractions are done, one
commit or two — your call; two is cleaner for per-extraction verification.)

## §5 — Stop conditions
- Any non-byte-identical step (golden / `.ours.json` / BIR / test move) → STOP.
- Any logic/scoring/inference change, or "fixing" anything → STOP (purity violation).
- A block entangled with the residual (not cleanly liftable) → STOP, surface (do not force).
- Any edit outside the new TU(s) + `sectionanalyzer.cpp` + `CMakeLists.txt` (+ a declaring header if it
  genuinely must change — flag it) → STOP.
- Any push → STOP.
