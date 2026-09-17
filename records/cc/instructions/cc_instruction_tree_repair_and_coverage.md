# CC Instruction — working-tree integrity repair + authoritative test-coverage audit

> **Why.** The Cowork-side Linux sandbox sees a **suspicious working-tree state** that must be confirmed/repaired on
> YOUR machine, and we will **not** sign Phases 1–4 as "tested" until there is (a) a clean, building tree, (b) a
> verified green suite run with **captured artifacts**, and (c) a **measured** test-adequacy + branch-coverage audit.
> This instruction does all three, in that order. **This is repair + measurement + audit ONLY** — NO production logic
> changes, NO new tests, NO inference-fixing (the standing discipline). The only writes are git-repair of confirmed
> corruption, clearing a stale lock, and capturing reports.
>
> **What the sandbox sees (to confirm, not to trust):** 3 core files look **truncated** — `note_model.h` (158 vs HEAD
> **235** lines), `slicer.h` (vs **105**), `slicer.cpp` (vs **109**), each ending mid-comment; ~11 other analysis files
> show **balanced +/- churn** (every line counted changed — the signature of CRLF/encoding normalization), with
> `section/localmodulationdetector.h` now seen as **binary**; and a **0-byte stale `.git/index.lock`** dated 10:30.
> HEAD is intact (`NoteEvent`/`NoteModel` present in the committed blob) — nothing committed is lost. The sandbox git
> is **known to diverge** from your Windows git this session, so the truth is whatever YOUR `git` reports.

## Part A — Working-tree integrity (DIAGNOSE first, then minimal SAFE fix — do NOT blanket-reset)
- **A1 — authoritative status.** Run `git status --short` and `git diff --stat HEAD`. Report verbatim whether the tree
  is clean or carries modifications. Confirm the working line counts of `note_model.h` / `slicer.h` / `slicer.cpp`
  against HEAD (235 / 105 / 109).
- **A2 — stale lock.** If **no git process is running**, remove the 0-byte `.git/index.lock` (dated 10:30); confirm
  removed. If a git process IS running, do not — report it.
- **A3 — classify EACH modified source file (this is the careful step).** For every modified `src/`/`tools/` file,
  decide which of three it is, with evidence:
  (i) **genuine content change** — real intended edits → **report, do NOT discard**;
  (ii) **line-ending/encoding-only churn** — identical content modulo EOL/encoding (test with `git diff
  --ignore-all-space` and/or check whether the diff collapses under EOL normalization);
  (iii) **truncation/corruption** — working copy shorter/incomplete vs HEAD (the 3 files above, and any others you find).
- **A4 — repair ONLY the safe cases:**
  - **Confirmed truncated/corrupt** files where HEAD is the correct complete version **and** there is no intended newer
    content → restore from HEAD: `git checkout HEAD -- <file>`. *(Phases 1–4 were committed; HEAD is authoritative; no
    uncommitted source work is expected — so a truncated file vs a complete HEAD blob is corruption to restore.)*
  - **Pure line-ending/encoding churn** → report the cause (`core.autocrlf` / missing `.gitattributes`). Do **NOT**
    mass-renormalize in this pass; flag it as a separate hygiene decision.
  - **Any file with genuine intended-looking new content you cannot attribute to a known commit** → **STOP and report**;
    do not discard — it may be unexpected work to preserve.
- **A5 — final state.** After safe repair the tree must be free of corruption and must BUILD. Report the final
  `git status`.

## Part B — Verified green build + CAPTURED artifacts (the "is it actually tested" evidence)
- **B1.** Clean build per `BUILD_AND_TEST.md`. Report success/failure. *(If the build fails, the tree was not actually
  good — STOP and report; do not paper over it.)*
- **B2.** Run all three suites, **capturing raw output to files** (gitignored, per the large-output rule — redirect,
  then tail): `composing_tests`, `notation_tests`, `pipeline_snapshot_tests`. Report exact pass/fail/skip counts **and
  paste the raw tail** of each.
- **B3.** Run the corpus BIR characterisation for **Baroque + Jazz + Default**; capture the `corpus_manifest.json`
  sha256 fingerprints and confirm the **53 / 24 / 53** identity sets (the SET, per CLAUDE.md, not just the integer).
- These are **evidence** — in your summary, paste the **actual captured numbers and sha256s**, not "all green."

## Part C — Test-adequacy + branch-coverage audit (what Cowork did statically — now MEASURED)
Cowork ran a parallel four-criteria audit (1: input classes per spec; 2: robustness / odd-empty-null input no-crash;
3: outcome set per spec; 4: every branch). **Confirm or REFUTE each headline gap at source, and MEASURE criterion 4.**

- **C1 — confirm/refute Cowork's headline gaps** (cite file:line; correct any that are wrong, as you did with
  `mono_smoke_test`):
  - **Robustness (criterion 2) is the weakest everywhere** — empty/single-note/unison/atonal/out-of-range inputs are
    largely unasserted at the L3 emission scorer and the L4 `analyzeChord`. Confirm the specific missing cases.
  - **L2 clip has ZERO direct tests** — `changePointSlices` is only ever called on whole-score `build(score)` in tests;
    the sustained-in/out clip, the seam-aware edge-extend, and the **re-slice-equivalence invariant** (the spec's "one
    invariant that must hold") are unpinned. Confirm.
  - **L4 spec↔production divergence** — the shipped per-region path (`analyzeChord` + `applyHarmonicFunction`) has **no
    abstain/inherit/uncertain/spelling-pin**, so the spec's "declare uncertainty rather than guess" outcome is
    untestable in production; the spec-conformant `chordslicedecoder` that has it is production-dead; the spelling-pin
    is unbuilt. Confirm.
  - **Zero/weak direct coverage:** `chordvoicing` (`closePositionVoicing`/`chordTonePitchClasses` — zero tests),
    `chordpostpasses` (indirect only), `ChordSymbolFormatter::formatNashvilleNumber` (one test). Confirm.
  - **L3 untested production threads:** `excludeStaves`, `ignoreDeclaredMode`, the dynamic-lookahead loop, the C1
    `populateEmissionConfidence` side-effect, the brittle leading-tone presence-gate (no regression pin). Confirm.
- **C2 — RUN AN INSTRUMENTED COVERAGE BUILD (criterion 4 — the thing Cowork CANNOT do).** Using whatever the toolchain
  supports (OpenCppCoverage for MSVC, or `gcov`/`llvm-cov` for a gcc/clang build), produce **per-module branch + line
  coverage** for L1–L4 over `composing_tests` (+ notation/snapshot where relevant). Report the **uncovered branches per
  module** and capture the coverage report to a file. **If coverage instrumentation is not readily available on the
  toolchain, say so explicitly** and instead deliver the best per-function static branch-gap list — do not fake numbers.
- **C3 — reconcile.** State where the measured coverage **agrees vs disagrees** with Cowork's static gap list, and flag
  any gap Cowork **missed or wrongly called**.
- **C4 — do NOT write new tests in this pass.** This is audit + measurement. The test-backfill is the **next** ratified
  step, driven by this report.

## Deliver
Write `cc_tree_repair_and_coverage_report.md` (gitignored): Part A diagnosis + exactly what was repaired (and why each
was safe), Part B captured green-run counts + manifest sha256s, Part C the four-criteria matrices + **measured coverage
numbers** + the reconciliation with Cowork's audit. In your summary to the user, **paste the headline captured numbers**
(suite counts, BIR sets, coverage %) — evidence, not assertion.

## Stop conditions
- You find genuine uncommitted source work you cannot classify or attribute → STOP, report, **do not discard**.
- The clean build fails → STOP and report (the tree was not good).
- You are about to write a new test, change production logic, or fix an inference problem → STOP (out of scope; this is
  repair + measurement + audit).
- A push targets `upstream` → STOP.
