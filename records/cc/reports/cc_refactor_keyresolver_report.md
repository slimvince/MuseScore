# Refactor report — split keyresolver.cpp — **SKIP (cohesive, not conflated)**

**Date:** 2026-06-17
**Target:** `src/composing/analysis/key/keyresolver.cpp` (361 lines)
**Candidate (assessment §5, #5):** `partialSignatureCorrection` (flagged "mild — one seam")
**Outcome:** **SKIP per §0 feasibility gate.** No commit made. No build/test run (no split attempted).

---

## §0 feasibility gate — FAILED

The candidate `partialSignatureCorrection` (keyresolver.cpp:107–190) is a **private,
internal-linkage (anonymous-namespace) helper whose sole caller is the residual.**

Verified facts (via `git grep`):

| Symbol | Linkage | Sole caller(s) | Cross-TU reuse |
|---|---|---|---|
| `partialSignatureCorrection` (:107) | anon-ns (internal) | `resolveKeyAndModeRanked` :261 | none |
| `ionianScaleSet` (:71) | anon-ns (internal) | `partialSignatureCorrection` :126–127 | none |
| `fallbackResult` (:55) | anon-ns (internal) | `resolveKeyAndModeRanked` :320 | none |
| `promoteWinnerInPlace` (:195) | anon-ns (internal) | `resolveKeyAndModeRanked` :336 | none |

- All non-source hits for `partialSignatureCorrection` are documentation / STATUS / design
  files. The `keyresolver.h:71` hit is a **doc comment** on the `correctedFifths` dump field,
  **not** a declaration — the symbol is **not** header-declared/external.
- `ionianScaleSet` (the only anon-ns helper `partialSignatureCorrection` depends on) is used
  **exclusively** by `partialSignatureCorrection`, so it would move cleanly with it — there is
  no residual-table dependency (not the `keyModeScaleIntervals` failure mode).

**Why this is a hard SKIP:** the candidate's sole caller — `resolveKeyAndModeRanked` — is the
**residual** function and does **not** move. Lifting `partialSignatureCorrection` into a sibling
TU would therefore require **linkage promotion** (declaring it in a header / giving it external
linkage so the residual can call it across the TU boundary). That is explicitly disallowed:

- §0: *"If it is a private internal-linkage helper whose sole caller is the residual … → SKIP +
  surface; do NOT force."*  ← exact match.
- §1 purity rule (b): an anon-ns helper may move *"only if it moves with all callers"* — its
  caller does not move.

## Cohesion assessment

`keyresolver.cpp` is a **single-responsibility cohesive unit**, not a conflation of layers:

- **One** public function: `resolveKeyAndModeRanked` (windowed key/mode resolution).
- **Four** private helpers that exist only to serve it: `fallbackResult`, `ionianScaleSet`,
  `partialSignatureCorrection`, `promoteWinnerInPlace`. Each has the residual (or another of
  these helpers) as its sole caller. None is reused elsewhere in the codebase.

There is no second public responsibility to peel off, and no anon-ns cluster movable *with* its
callers. Splitting would only fragment one function's private helpers across two TUs behind a
newly-promoted linkage — net loss of cohesion, and a behavior-neutrality risk for zero structural
gain.

This matches the **harmonicsegmenter precedent** (assessment): a cohesive unit where SKIP is the
correct, expected outcome.

## Disposition

- **No split. No commit. No code change. No build/test run** (per §4: §0 fail → no commit, report only).
- `keyresolver` is reported as **cohesive-not-conflated**.
- **Assessment §5 pure-split candidates are now EXHAUSTED.** Next per the standing instruction is
  the read-only **LAYER-BY-LAYER AUDIT** of each now-separated layer (deferred acceptance review),
  to be scoped separately by Cowork.
