# CC Instruction — clang / llvm-cov BRANCH coverage (feasibility spike → conditional delivery)

> **Why.** Criterion 4 ("every branch hit at least once") needs **true branch coverage**. OpenCppCoverage is line-only
> (`branches-valid="0"`). `llvm-cov --show-branches=count` over a clang-instrumented build is the path. **This is a
> SEPARATE, additive measurement build for the coverage target ONLY** — the production MSVC/ninja build,
> `setup_and_build.bat`, and the BIR/snapshot gates stay **exactly as they are** and keep being measured on MSVC.
> **Tooling / build-config only — NO production source changes, NO new tests** (the backfill already added them).
>
> **Feasibility-first and honest:** a large Qt/MuseScore codebase may not build cleanly under clang-cl, and LLVM may not
> be installable without admin. If so, **STOP and report the precise blocker** — do **not** force it, do **not** edit
> `src/` to satisfy the compiler, do **not** fake numbers. A clean "blocked, here's why" is a successful outcome of the
> spike (we fall back to the line+static-branch proxy).

## §0 — Preamble: protect the uncommitted Cowork docs (sweep-protection)
Commit, **local-only**, the unstaged Cowork doc edits — `COWORK_HANDOFF.md` (the NEVER-BASH standing rule) and any other
modified `cowork_*`/`COWORK_*` docs: `docs(cowork): never-bash standing rule + handoff update`. Confirm
`git show --stat <sha>` lists only doc files (no source). Report the sha.

## §1 — Feasibility probe (do this FIRST; report before building anything heavy)
1. **Toolchain availability:** is `clang`/`clang-cl` + `llvm-profdata` + `llvm-cov` present, or installable **without
   admin** (the portable route you used for OpenCppCoverage)? Report versions, or the blocker.
2. **Minimal instrumentable target:** determine the **smallest** build that yields L1–L4 branch coverage — ideally
   `composing_analysis` (the L1–L4 source) compiled with `-fprofile-instr-generate -fcoverage-mapping`, linked into a
   runnable `composing_tests`. You decide the minimal feasible configuration (e.g. instrument only `composing_analysis`
   and link MSVC-built `engraving`/`muse` as-is, if clang-cl ABI allows; or a thin test harness). **Do a trial
   configure/compile/link and report what actually happens.**
3. **The hard gate:** if making it build requires **production `src/` edits** (MSVC-isms, pragmas, warnings-as-errors,
   Qt-MOC quirks) → **STOP and report exactly what would need to change.** Only a *separate* build-config / toolchain /
   preset file is permitted to be created. Never edit `src/` to satisfy clang.

## §2 — If §1 is clean: stand up the instrumented coverage build (isolated, additive)
- Add a **separate** CMake preset / toolchain file (e.g. `tools/coverage/clang-coverage.cmake` or a dedicated preset)
  that builds the instrumented coverage target. The production preset and `setup_and_build.bat` are **untouched**.
- Build → run `composing_tests` under instrumentation → `.profraw` → `llvm-profdata merge` → `llvm-cov report` +
  `llvm-cov show --show-branches=count` scoped to the L1–L4 modules. Capture raw output to files.
- Report **per-module BRANCH coverage** (the real criterion-4 number) and the **list of uncovered branches** — this is
  the map the backfill's line-coverage + static audit could only approximate.

## §3 — Gate & scope
- **Production MSVC build + BIR 53/24/53 + snapshots are UNCHANGED and still the gates** — the clang build is
  measurement-only and must not route or alter them. Confirm the production build/gates are untouched.
- **NO production source changes.** Build-config/tooling files only. If `src/` must change → STOP (§1.3).
- **NO test changes** — use the existing `composing_tests`. This is a measurement capability, not a test pass.
- `upstream` never; local commit of the build-config + runner only; report gitignored.

## §4 — Deliver
Write `cc_clang_branch_coverage_report.md` (gitignored):
- **If feasible:** the instrumented-build setup (the separate preset), per-module **branch%**, the uncovered-branch
  list (the real criterion-4 map), and the commit sha of the build-config (so Cowork verifies by sha).
- **If blocked:** the precise blocker (clang/LLVM unavailable / target won't build under clang-cl without `src/` edits —
  name them / link or runtime failure), so we decide the fallback. No forcing, no faked numbers.

## §5 — Stop conditions
- LLVM/clang unavailable and not installable without admin → STOP, report.
- The minimal coverage target won't build/link/run under clang **without production `src/` edits** → STOP, report what's
  needed.
- You edit any `src/` production file, or change the production build / `setup_and_build.bat` / the gates → STOP.
- A push targets `upstream` → STOP.
