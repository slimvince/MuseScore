# Stage 2.2a — Corpus-measurement hardening (M3 fix) — report

**Base:** `8598cbd245`. **Bookkeeping commit (Commit 2):** `6f1e3dc807`.
**Tooling commit (Commit 1):** staged, awaiting Cowork confirmation (proposal §8).

Tooling-only. **No metric definitions changed** — alignment/classification logic in
`compare_analyses.py` / `compare_rn.py` / `dcml_parser.py` is untouched; `git status`
shows zero `.cpp`/`.h` changes and no C++ build was needed. The fix makes the M3
shared-`tools/corpus` contamination **structurally impossible** (per-preset dirs +
clean-slate) and **loudly detected** (manifest + fingerprint validation).

---

## 1. Design decisions + deviations

| # | Design point | Decision |
|---|---|---|
| 1 | Per-preset corpus dirs | `tools/corpus/baroque/` + `tools/corpus/jazz/` (subdirs, already gitignored by `/tools/corpus/`). Both exist side-by-side → both-preset checks no longer overwrite each other. |
| 2 | Stamp + completeness | `run_bach_preset.py` writes `corpus_manifest.json` (preset, expected/ours count, `complete` flag, git hash, timestamp, batch_analyze size+mtime, **per-score status + sha256**). On any non-`OK`/missing score it prints a `!!!` banner to stderr and `exit(1)`. |
| 3 | `characterise --corpus-dir` + validate | New `--corpus-dir` (default `tools/corpus/baroque`) + `--wir-dir`. `validate_corpus_dir()` refuses a dir with no manifest / incomplete / extra-or-missing `.ours.json` / **fingerprint mismatch** (contamination); exit 2 with a clear error. No classification-logic change. |
| 4 | Other consumers | Surveyed (§2). |

**Deviations / judgment calls (all stated):**

- **Per-score sha256, not just mtime/size.** The prompt allowed "mtime/size"; I store
  size **and sha256** of each `.ours.json`. Reason: the contamination probe copies a
  *different preset's reading of the same score* — same path, possibly same size; only
  a content hash reliably distinguishes it. Hashing 353 small JSONs is sub-second.
- **Self-contained per-preset dir.** `characterise` reads `{stem}.ours.json` **and**
  `{stem}.music21.json` from one dir. So `run_bach_preset.py` copies the
  (preset-independent) `*.music21.json` into the output dir when it differs from the
  input `--corpus-dir`. This keeps `characterise` reading exactly one dir and makes the
  manifest a complete description of what's measured. `.xml` is **not** copied
  (`characterise` never reads it).
- **`--corpus-dir` default = `tools/corpus/baroque`** (the primary preset) rather than
  the old flat `tools/corpus`, so a bare `characterise` invocation measures a valid
  manifest-stamped dir.
- **Clean-slate guard.** `run_bach_preset.py` deletes existing `*.ours.json` + manifest
  at the start of a fresh regen **only when** output-dir ≠ corpus-dir and neither
  `--resume` nor `--skip-cpp` is set (so re-aggregation paths are preserved). New
  `--resume` flag skips the clean-slate.
- **`characterise.main` refactored to `run()` + `main(argv)`.** Needed so the validation
  gate lives in `main()` while the existing classifier (`run()`) is unit-testable
  directly. Mechanical; output strings preserved verbatim.

---

## 2. Survey of `tools/corpus` consumers

`grep` over `tools/**.py` for the flat dir. Treatment decided per the prompt:

| Consumer | Reads flat `tools/corpus`? | Treatment |
|---|---|---|
| `run_bach_preset.py` | writes (was `--output-dir tools/corpus`) | **Fixed** — per-preset dirs + manifest + fail-loud. |
| `characterise_bir_false.py` | yes (hard-wired `_CORPUS_DIR`) | **Fixed** — `--corpus-dir` + manifest validation. |
| `tools/run_*_validation.py` (Beethoven, Corelli, Chopin, Mozart, Schumann, Tchaikovsky, Dvorak, Grieg, CPE-Bach, Bach-suites) | **No** — `'corpus'` there is a *report label string*; they read `tools/dcml/<name>/` and write `tools/reports/<corpus>_<ts>/`. | **Untouched.** Confirmed scope does **not** balloon (verified `--output` default `tools/reports/`). |
| `analyze_inversion_errors.py` | yes — but it is the **separate secondary `bassIsRoot` metric** (27/22), *not* the 13/7 characterise gate (per `reference_bir_metric_scripts.md`). Not in the authorized file list. | **Deferred follow-up**, documented in CLAUDE.md / build_and_test.md / `tools/corpus/README.md`. Left reading the legacy flat dir. |
| Frozen one-offs: `dump_bir_cases.py`, `dump_birfalse_cases.py`, `iter{90,92,94,95}_*.py`, `diag_iter{8,32,54,63}_*.py`, `analyze_{bir_true_iter19,wrong_root_iter90,iter90_regressions}.py`, `compare_gatej.py`, `gate_n_fp_scan_iter39.py`, etc. | yes (hard-wired) | **Untouched** — historical diagnostics tied to a past iteration's flat corpus; not part of the live gate. |
| `music21_batch.py` | writes `.xml`+`.music21.json` (`--output tools/corpus`) | **Untouched** — it produces the preset-independent ground truth that stays at flat-dir top level (now the input source for `run_bach_preset.py`). |

No live workflow breaks: the BIR gate moves to per-preset dirs; the secondary metric
and frozen diagnostics keep their flat-dir inputs (the `.xml`+`.music21.json` and the
legacy `.ours.json` remain in place).

---

## 3. New-test inventory (`tools/tests/test_metric_scripts.py`)

Existing **54 green** → **63 green** (+9). Existing tests unchanged except one
**mechanical** edit: `TestCharacteriseBirFalse._run_main` now calls `cbf.run(corpus,
corpus)` directly instead of patching `_CORPUS_DIR` + `cbf.main()` (main() now parses
argv). A `corpus_manifest.json` fixture was added to `tools/tests/fixtures/bir_corpus/`.

New tests:
1. `TestCharacteriseBirFalse.test_main_validates_manifest_then_runs` — end-to-end via
   `main(["--corpus-dir", fixture, ...])`: manifest validates, prints `Corpus OK:
   preset=Baroque`, BIR=false=1.
2. `TestCorpusManifestValidation.test_write_manifest_records_fingerprints_and_complete`
3. `…test_write_manifest_incomplete_when_status_failed` — a `FAILED` worker ⇒ `complete=False` (the fail-loud trigger).
4. `…test_validate_accepts_complete_clean_corpus`
5. `…test_validate_rejects_missing_manifest`
6. `…test_validate_rejects_incomplete_corpus` (`INCOMPLETE` error)
7. `…test_validate_rejects_contamination_by_overwrite` — **the M3 scenario**: a foreign
   file overwrites a listed score ⇒ `CONTAMINATION` error (not a wrong number).
8. `…test_validate_rejects_extra_unlisted_file` — foreign stem ⇒ `CONTAMINATION`.
9. `…test_validate_rejects_missing_ours_file`.

---

## 4. Verification table

All commands per the instruction. `git status` confirmed **no `.cpp`/`.h`** change;
`batch_analyze.exe` mtime `Jun 10 21:15` (the report's build-under-test identity).

| Step | Result |
|---|---|
| `python -m unittest discover -s tools/tests` | **63 tests OK** (54 existing + 9 new) |
| `run_bach_preset --preset Baroque --output-dir tools/corpus/baroque` | `353/353`, `complete=True`, manifest written, **exit 0** |
| `run_bach_preset --preset Jazz --output-dir tools/corpus/jazz` | `353/353`, `complete=True`, manifest written, **exit 0** |
| `characterise --corpus-dir tools/corpus/baroque` | `Corpus OK: preset=Baroque 353/353` → **BIR=false 13** |
| `characterise --corpus-dir tools/corpus/jazz` | `Corpus OK: preset=Jazz 353/353` → **BIR=false 7** |
| **Contamination probe** (copy `baroque/bwv10.7.ours.json` → `jazz/`) | `characterise` **exit 2**: `ERROR: CONTAMINATION: bwv10.7.ours.json fingerprint differs from the Jazz manifest (foreign-preset / stale file)` |
| Restore `jazz/bwv10.7.ours.json` | `characterise` exit 0 → **BIR=false 7** again |

### Identity sets (compared, not just totals)

**Baroque (13)** — matches the report §2 set exactly (8 Baroque-only floaters + 5 shared):
`bwv102.7, bwv14.5, bwv17.7, bwv174.5, bwv245.17, bwv245.40, bwv261, bwv269, bwv301,
bwv381, bwv422, bwv432, bwv45.7` ✓

**Jazz (7)** — matches the documented set exactly:
`{bwv244.15, bwv245.17, bwv245.40, bwv422, bwv432, bwv45.7, bwv74.8}` ✓

No new finding — both clean regens reproduce the documented identities, so the
stop-condition ("identity sets do NOT match → NEW finding") is **not** triggered.

---

## 5. CLAUDE.md / build_and_test.md diffs

**CLAUDE.md** (Gate-threshold-and-preset-policy corpus-check block):
```diff
-# Baroque
-cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
-cd C:\s\MS && python tools/analyze_inversion_errors.py
-# Jazz  (run immediately after — reuses same output dir)
-cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
-cd C:\s\MS && python tools/analyze_inversion_errors.py
+# Baroque (per-preset dir — clean-slated and manifest-stamped each regen)
+cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque
+cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque
+# Jazz (independent dir — no contamination; order no longer matters)
+cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus/jazz
+cd C:\s\MS && python tools/characterise_bir_false.py --corpus-dir tools/corpus/jazz
```
plus an explanatory paragraph (manifest/fail-loud/refuse + case-identity gate) and a
note that `analyze_inversion_errors.py` is the separate secondary metric (deferred).

**build_and_test.md** (Corpus Regression Check block): identical command swap + a
**Stage 2.2a** note. Full text in `git diff CLAUDE.md BUILD_AND_TEST.md`.

---

## 6. Old flat `tools/corpus/` disposition

**Decision: KEEP the flat dir + add a README breadcrumb** (not delete).

Justification: the flat dir's top level holds the **preset-independent ground truth**
(`*.xml` + `*.music21.json`) that `run_bach_preset.py` still reads as its input
`--corpus-dir`; it cannot be deleted. The stale top-level `*.ours.json` (last mixed
regen) are now **unread by the hardened gate** but are still consumed by the secondary
`analyze_inversion_errors.py` and the frozen `iterNN` diagnostics, so deleting them
would break those without a benefit. A local `tools/corpus/README.md` documents the
new layout and warns "do not measure BIR off the flat dir." Everything under
`tools/corpus/` is gitignored, so this is a working-tree-only choice (the committed
documentation lives in CLAUDE.md / build_and_test.md).

---

## 7. Interim-gate retirement

With manifest validation in place, **"Baroque ≤ 13 / Jazz ≤ 7" regain their plain
meanings.** The Stage-2.1 interim wording (read the integer only off a hand-verified
clean 353/353 single-preset regen, because a shared mutable dir could silently mix
presets) can be **retired**: a contaminated or partial corpus now produces an *error*
(`run_bach_preset` exit 1 / `characterise` exit 2), not a number. The case-identity
sets remain the precise pass condition; the integer is now safe to read because it can
only come from a manifest-validated, single-preset, complete corpus. (Cowork will
update the handoff accordingly.)

---

## 8. Commits

- **Commit 2 (bookkeeping, done):** `6f1e3dc807` — `docs: session bookkeeping — Stage 1
  completion, Stage 2.1, M3 investigation`. Staged exactly STATUS.md, COWORK_HANDOFF.md,
  docs/implementation_roadmap.md (accumulated prior-session updates, coherence-checked,
  not rewritten).

- **Commit 1 (tooling, awaiting confirmation):** proposed message
  `tools: per-preset corpus dirs + manifest validation (Stage 2.2a — M3 fix)`.
  Staging set:
  - `tools/run_bach_preset.py`
  - `tools/characterise_bir_false.py`
  - `tools/tests/test_metric_scripts.py`
  - `tools/tests/fixtures/bir_corpus/corpus_manifest.json` (new)
  - `CLAUDE.md`
  - `BUILD_AND_TEST.md`

  (`tools/corpus/README.md` is gitignored and intentionally **not** committed.)

**Stop-conditions:** none hit — no classification-logic change was required; the
`run_*_validation.py` survey did not balloon scope; both clean regens reproduced the
documented identity sets exactly.
