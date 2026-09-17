# CC Instruction — UNION branch coverage (`composing_tests` ∪ `notation_tests`) — the true L1–L4 baseline

> **Why.** The clang spike measured **`composing_tests` only** → 69.75% branch over `src/composing/analysis`, with three
> files at **0%** (`sectionanalyzer`, `sectioncadencedetection`, `keymodeformatting`) hypothesized to be
> **`notation_tests`-driven**. Before we triage the unhit branches into add-test / wire-or-remove / exclude-defensive,
> we need the **whole-corpus** number across **both** test suites. This extends the **same proven cheap-path runner** to
> also instrument-run `notation_tests` and merge. **Measurement only — NO `src/` edits, NO production-build/gate change,
> NO test changes.** Reuse/extend `tools/coverage/run_branch_coverage.ps1`.

## §1 — Extend the runner to `notation_tests` (the same cheap mixed-link path)
- Reuse the already-instrumented `composing_analysis` (built with `-fprofile-instr-generate -fcoverage-mapping`).
- Relink `notation_tests` against that instrumented lib + the **existing MSVC-built** notation/engraving/muse/Qt/gtest
  libs + the clang profile runtime, using **`lld-link`** (the proven fix for the profile-names section). Run it →
  `notation_tests` `.profraw`.
- **If `notation_tests` cannot relink/run on the cheap path without `src/` edits → STOP and report** exactly what's
  needed (link/runtime error or required source change). Do **not** edit `src/`, do **not** rebuild engraving/Qt under
  clang to force it.

## §2 — Merge + report the UNION
- `llvm-profdata merge` the `composing_tests` + `notation_tests` `.profraw` → `union.profdata`.
- `llvm-cov report` + `llvm-cov show --show-branches=count` scoped to `src/composing/analysis` → **union per-module
  branch%**.
- Report:
  - the **union branch% per L1–L4 module** (the true criterion-4 baseline);
  - **the 0%-files verdict** — do `sectionanalyzer` / `sectioncadencedetection` / `keymodeformatting` lift from 0% under
    `notation_tests`? (confirm or refute the hypothesis, with the new numbers);
  - the **union list of still-unhit branch directions** (file + location) — this is the real gap Cowork will triage.

## §3 — Gate & scope
- **Production MSVC build + BIR 53/24/53 + snapshots untouched** (measurement-only) — confirm.
- **No `src/` edits; build-config / runner only.** If `src/` must change → STOP.
- **No test changes** — use the existing `composing_tests` + `notation_tests` binaries.
- `upstream` never; local commit of the **runner extension only**.

## §4 — Deliver
Write `cc_union_branch_coverage_report.md` (gitignored): the union per-module branch%, the 0%-files verdict, the
union still-unhit-direction list, and the runner-extension **commit sha** (so Cowork verifies it's build-config-only by
sha).

## §5 — Stop conditions
- `notation_tests` won't relink/run on the cheap path without `src/` edits → STOP, report (do not force / do not rebuild
  Qt under clang).
- Any `src/` production / production-build / `setup_and_build.bat` / gate change enters the picture → STOP.
- A push targets `upstream` → STOP.
