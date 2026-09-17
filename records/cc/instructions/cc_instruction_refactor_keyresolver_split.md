# CC Instruction — Refactor: split keyresolver.cpp (byte-identical) — feasibility-gated

> **Last pure-split candidate** (assessment §5, #5, flagged "mild — one seam: `partialSignatureCorrection`").
> `key/keyresolver.cpp` (361). **STRICTLY BYTE-IDENTICAL — pure verbatim movement, NO logic/scoring/inference
> change. Commit locally → Cowork verifies the committed object.** Given it is small + "mild," it may be a
> COHESIVE single-responsibility unit → a SKIP is a perfectly good outcome (the harmonicsegmenter precedent).

---

## §0 — FEASIBILITY GATE FIRST (binding)
Before moving anything, at source confirm the candidate (`partialSignatureCorrection` and any sibling seam)
is **VERBATIM-liftable**: it must be **already external/header-declared OR an anon-ns cluster movable WITH
all its callers**, with **no residual dependency** (it must not read an anon-ns table/helper that stays in
the residual — the `keyModeScaleIntervals` case) and **no linkage promotion** needed. Check: `git grep` the
symbol for cross-TU reuse; read `keyresolver.h` for what's external; confirm the candidate's own dependencies
are self-contained or move with it. **If it is a private internal-linkage helper whose sole caller is the
residual, OR it depends on something staying in the residual → SKIP + surface; do NOT force.**

## §1 — The purity rule (same as the prior splits)
Only: (a) cut **verbatim** into a new sibling TU; (b) prefix a moved anon-ns helper only if it moves with all
callers; (c) register in `CMakeLists.txt`. **No logic/constant/behavior change. Do NOT "fix" anything.** The
declaring header stays unchanged. Non-verbatim → STOP, surface.

## §2 — The candidate
`partialSignatureCorrection` (+ anything genuinely self-contained with it) → a new TU (e.g.
`key/partialsignaturecorrection.cpp`), IF it passes §0. Residual = the resolver. If it fails §0 (private/
residual-dependent), **SKIP, make no commit, report keyresolver as cohesive-not-conflated.**

## §3 — Acceptance gate (MANDATORY, only if a split is made — byte-identical)
1. Build green. 2. `composing_tests` + `notation_tests` pass. 3. `pipeline_snapshot_tests` 11/11, **no
`--update-goldens`**. 4. 3-preset `.ours.json` **0-diff** + **BIR 57/23/57**. Any deviation = STOP.

## §4 — Deliver: COMMIT LOCALLY (unpushed) → Cowork verifies the committed object
If a split passes §0 + §3: **commit locally, UNPUSHED**: *refactor: split keyresolver.cpp — lift
partialSignatureCorrection into own TU (byte-identical).* Report the **commit hash** + gate + move list in
`cc_refactor_keyresolver_report.md`. **Cowork verifies the COMMITTED OBJECT** (`git show <hash> --numstat` +
verbatim `comm` + `:path`). **If a problem, revert.** **Do NOT push.** If §0 fails → no commit, just report
the cohesive-skip.

## §5 — Stop conditions
- Candidate is private internal-linkage / residual-dependent / needs linkage promotion → SKIP + surface.
- Any non-byte-identical step (golden / `.ours.json` / BIR / test move) → STOP.
- Any logic/scoring/inference change or "fix" → STOP (purity violation).
- Any edit outside the new TU + `keyresolver.cpp` + `CMakeLists.txt` (+ a declaring header if it genuinely
  must change — flag it) → STOP. Any push → STOP.

---

**After keyresolver (split or skip), the assessment §5 pure-split candidates are EXHAUSTED → next is the
read-only LAYER-BY-LAYER AUDIT** (each now-separated layer audited for its single responsibility,
correctness, completeness — the deferred acceptance review). Cowork will scope that separately.
