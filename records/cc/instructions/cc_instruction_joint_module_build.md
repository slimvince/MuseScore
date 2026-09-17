# CC instruction — the joint-estimator C++ module build (the parallel path opens; OI-180 sanction in force)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, **`cowork_prefit_gates.md` — the sanctioned-dual-path
> section (its terms GOVERN this dispatch)**, `cowork_joint_estimator_factorization.md` (the
> ratified structure the module implements), and the probe/search records
> (`cc_direct_metric_search_report.md`, `e3d17c325d`, `3ff9017f4d`).
>
> **Current state:** branch `master`, HEAD `3ff9017f4d` (verify). One Cowork-authored uncommitted
> doc edit rides your FIRST commit: `cowork_handoff.md` (the rulings record + the dual-path status
> line). **THIS DISPATCH OPENS THE C++ PARALLEL PATH — the first `src/` work of the arc, under
> the sanction's terms, restated as hard rules:**
> - **New module only:** everything lives in a NEW directory `src/composing/analysis/joint/`.
>   The ONLY existing files you may touch: the build files needed to compile the new module
>   (CMake lists), NEW test files added to the composing test suite, and `tools/batch_analyze.cpp`
>   for one default-OFF driver flag (the established diagnostic-flag pattern). ANY other
>   existing-file edit is a STOP.
> - **Input surface:** the module reads ONLY the L1/L1.5 published fact surface (notes, notated
>   spellings, ticks, voices, ties, fermatas, meter, signature, declared mode) and the
>   dependency-free pitch primitives the sanction enumerates (`normalizePc`,
>   `diatonicMaskFromFifths` — the shared-predicate leaf). It must NOT include or call the legacy
>   L2/L3/L4/L5 analysis (no `chordanalyzer`, no `regionanalyzer`, no key/mode analyzer, no
>   gates). An include audit is part of the self-check.
> - **Production byte-identity:** the module is DORMANT by default. `composing_tests` and
>   `notation_tests` pass with every EXISTING test unmodified; `pipeline_snapshot_tests` pass
>   with NO golden refreshed. Prove all three after every commit.
> - Tables and weights are LOADED AT RUNTIME from the committed artifacts under
>   `tools/joint_estimator/` (the all-326 publishable tables + selected weights, and the identity
>   vector) — production packaging is an adoption-time question, not yours.
> - **No adoption act:** the OI-178 protocol runs later, as its own dispatch, on your built path.
> - The VS Code bash rules (CLAUDE.md) apply to every command; build via the PowerShell
>   Start-Process form.

**Dispatch author:** Cowork, 2026-07-20, at the user's direction (the fourth ruling: the build
opens). **What "done" means here: the C++ module decodes byte-equivalently to the established
Python probe** — the probe artifacts are the parity oracle — with its inputs proven equal to the
committed note events. Nothing more; nothing about production output changes.

## Task 1 — the module and its input surface

`src/composing/analysis/joint/` — the joint estimator: table/weight loading (from the committed
JSON), the event lattice built from the score's fact layer, the per-note covariates (metric
class, step approach/departure, tie), the factor scoring at the ratified granularities (per tone /
per event / per boundary, the §2 amendment), the below-threshold rule (§5), the initial-only
signature prior, and the exact block-factorized semi-Markov Viterbi with the posterior summary.
File organization is yours; report it. New-path test coverage is REQUIRED (the standing
full-coverage objective): the desk-simulation synthetic cases as DP fixtures (the same
hand-computed totals the Python parity used) plus unit tests per component, added as NEW test
files to the composing suite.

**Input-parity establishment (the two-readers-agree discipline, and the risk center of this
build):** for all 326 covered corpus pieces, the module's extracted facts must match the
committed `note_events/note_events.json` — note count, per-note (tick, duration, pitch class,
line-of-fifths spelling, voice threading, tie, fermata), the event lattice, meter, signature,
declared mode. The Python side read music21's rendering of the same scores; the C++ side reads
the analyzer's fact layer — genuine divergences (voice assignment is the likely one, and the
covariates depend on it) are FINDINGS to enumerate per class, not to paper over. Small mechanical
representation differences (tick conventions, spelling encodings) are mapped, with the mapping
stated. **If input parity cannot be reached on some enumerable class of pieces, STOP and report
the class** — the fact surface disagreeing with the established extraction is exactly the kind of
discovery this establishment step exists to force.

## Task 2 — decode parity against the oracle

With input parity holding: the module's decode must reproduce the committed probe decode
(`probe_corpus_decode.json` paths — state sequence and boundaries — and scores to 1e-6 relative)
on all 326 pieces, at BOTH the identity weights and the selected weights (the two committed
arms). Any path mismatch: STOP, diagnose which factor's scoring diverges (the per-factor score
decomposition makes this mechanical), report. The parity result is a generated artifact.

## Task 3 — the driver

One default-OFF flag in `tools/batch_analyze.cpp` (the established pattern) that runs the joint
module on a score and emits its decode as a diagnostic artifact — the hook the later OI-178
adoption measurement will use. OFF means byte-identical production output; prove it (the
suites + snapshots row above).

## Commits

Up to THREE, each independently green (suites + snapshots proven in each): (1) module skeleton +
build wiring + table loading; (2) the decoder + the new tests + input parity; (3) the driver +
decode parity artifacts. This instruction file force-added with the first; the riding
`cowork_handoff.md` edit with the first. Push **origin only** (the standing hard stop on the
upstream remote).

## Self-check before reporting (standing rule)

The include audit (no legacy analysis header reachable from the module — list the module's full
include closure); the diff audit (no existing file beyond the enumerated three classes); the
dormancy proof per commit; the input-parity and decode-parity artifacts generated; coverage of
the new paths demonstrated (name the tests per component). **Report:** the parity results and
every divergence class found; the include closure; reuse-versus-new (expected reuse: the fact
layer, the two pitch primitives, the build patterns; expected new: everything else; nothing
retires yet — the retirement map executes only at adoption); timings of the C++ decode vs the
Python probe; anomalies — a surprise here is a STOP-for-review, reported, never built around.
