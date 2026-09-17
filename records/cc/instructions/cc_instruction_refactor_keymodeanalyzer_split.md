# CC Instruction — Refactor: split keymodeanalyzer.cpp (byte-identical) — feasibility-gated

> **Next pure-split candidate** (assessment §5, #4). `key/keymodeanalyzer.cpp` (942) — the assessment flagged
> **display formatting** as "a clean win" and the **mode-data / scorer library** as "pure-with-a-shared-header
> -caveat." **STRICTLY BYTE-IDENTICAL — pure verbatim movement, NO logic/scoring/inference change. Commit
> locally → Cowork verifies the committed object.**

---

## §0 — FEASIBILITY GATE FIRST (the harmonicsegmenter lesson)
Before moving anything, **at source confirm each candidate block is VERBATIM-liftable** — i.e. its functions
are **already external/header-declared OR an anon-ns cluster movable WITH all its callers** (no linkage
promotion, no new declaration). **If a candidate block turns out to be a private internal-linkage cluster
whose sole caller is the residual (the harmonicsegmenter case), it is COHESIVE → SKIP it and surface; do NOT
force a linkage promotion** (that exposes internals, isn't verbatim, and isn't better layering). Check:
`git grep` each candidate symbol for cross-TU reuse, and read the header to see what's external. Only split
what passes this gate.

## §1 — The purity rule (same as the prior splits)
Only: (a) cut a function/helper **verbatim** into a new sibling TU; (b) prefix a moved anon-ns helper
(internal-linkage rename ⇒ byte-identical) **only if it moves with all its callers**; (c) register the new
`.cpp` in `CMakeLists.txt`; (d) `scoring_model.md`/doc pointers only IF a moved block is referenced there
(flag; do not bundle the working-tree-dirty `ARCHITECTURE.md`). **No logic/constant/behavior change. Do NOT
"fix" anything.** The declaring header stays unchanged. Non-verbatim → STOP, surface.

## §2 — The candidate split(s) (per assessment §5, each feasibility-gated)
- **Display formatting** ("clean win") → if its functions are external/header-declared (verify), lift them
  into `key/keymodeformatting.cpp`. This is the most likely clean verbatim win.
- **Mode-data / scorer library** ("shared-header caveat") → only if it passes §0 verbatim-feasibility;
  the "shared-header caveat" suggests it may NOT be a clean verbatim move — if separating it needs a new
  shared header or a linkage change, **SKIP + surface**, do not force.
Do each passing block as a **separate step** with its own gate (§3). Residual = the orchestrator.

## §3 — Acceptance gate (MANDATORY per extraction — byte-identical)
1. Build green. 2. `composing_tests` + `notation_tests` pass. 3. `pipeline_snapshot_tests` 11/11, **no
`--update-goldens`**. 4. 3-preset `.ours.json` **0-diff** + **BIR 57/23/57**. Any deviation = STOP.

## §4 — Deliver: COMMIT LOCALLY (unpushed) → Cowork verifies the committed object
Do the passing split(s) + gate in your worktree, then **commit locally, UNPUSHED**: *refactor: split
keymodeanalyzer.cpp — lift <block> into own TU (byte-identical).* Report the **commit hash** + gate + move
list + **any blocks SKIPPED per §0** in `cc_refactor_keymodeanalyzer_report.md`. **Cowork verifies the
COMMITTED OBJECT** (`git show <hash> --numstat` + verbatim `comm` + `:path`). **If a problem, revert.** **Do
NOT push.** If NO block passes the feasibility gate (all cohesive), make NO commit — just report the skip.

## §5 — Stop conditions
- A candidate block is a private internal-linkage cluster (needs linkage promotion / new decl) → SKIP +
  surface (the harmonicsegmenter precedent); do not force.
- Any non-byte-identical step (golden / `.ours.json` / BIR / test move) → STOP.
- Any logic/scoring/inference change or "fix" → STOP (purity violation).
- Any edit outside the new TU(s) + `keymodeanalyzer.cpp` + `CMakeLists.txt` (+ a declaring header if it
  genuinely must change — flag it) → STOP. Any push → STOP.
