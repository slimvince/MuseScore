# CC Instruction: Corpus hygiene — pin the gate's ground truth (audit C1–C4)

## Context

Implements the Disposition table of `cowork_corpus_audit.md` (read it first, fully).
Base: `9e52147b04`. The audit's verified findings: the snapshot gate's 11 source scores
live in revision-unpinned gitignored clones (C1); the music21 version behind the 353
gate-corpus JSONs is recorded nowhere (C2); the 353-vs-361-vs-410 chorale filter is
undocumented (C3); several stale/dead artifacts mislead (C4). Goal: the gates' ground
truth gets recorded identity, provenance, and a current map.

Standing rules (handoff): never guess — investigate or state the unknown; explicit
staging; `muse` never; metric/classification logic untouched (this is provenance and
hygiene, not measurement change).

**Authorized:** `tools/**` (scripts: manifest/validation plumbing only), new manifest
files, `docs/score_inventory.md`, `tools/REPRODUCIBILITY.md`, `tools/corpus/README.md`,
`src/composing/tests/scores/**` (deletion only, Task 4), `src/notation/tests/**` (only
if the hash pre-check lands there), CMakeLists as needed, .gitignore. NOT authorized:
any score-content edit anywhere; `chordanalyzer_catalog.musicxml` (hard rule).

---

## Task 1 — C1: pin the snapshot/gate source corpora

1. Build `tools/snapshot_sources_manifest.json`: for each of the 11 snapshot source
   `.mscx` (enumerate from `pipeline_snapshot_tests.cpp`, don't trust the audit's list)
   — sha256, size, path, owning repo, and the repo's CURRENT clone commit
   (`git -C tools/dcml/<repo> rev-parse HEAD` — if a clone is not a git repo or is
   dirty, record that fact verbatim; never guess a commit).
2. Extend the manifest to the BIR gate's annotation inputs: the WiR Bach analysis files
   that `characterise_bir_false`/`find_wir_file` actually consumes for the 353 (derive
   the consumed-file list by probe — run the resolver, log the paths — not by
   assumption), with the when_in_rome clone commit. Hash the full consumed set
   (one aggregate sha256 over sorted per-file hashes is fine; record both).
3. Cheap drift check: a Python test in `tools/tests/` that verifies the 11 snapshot
   sources against the manifest and FAILS with "source corpus drifted — see
   snapshot_sources_manifest.json" (skip with a clear message when tools/dcml is
   absent, e.g. fresh checkout). Wire nothing into the C++ suite this run (option
   noted for later — keep scope tight).
4. `REPRODUCIBILITY.md`: pin every clone command to the recorded commit
   (`git clone … && git checkout <hash>`), with a note that bumping a pin requires
   regenerating goldens/baselines deliberately.
5. **License check (investigate, decide nothing):** record in the report the LICENSE
   of each DCML/WiR repo consumed; state plainly whether an in-tree copy of the 11
   scores would be redistribution-compatible with this repo's GPL. No copies this run.

## Task 2 — C2: music21 provenance

1. Hunt for the generating script + any recoverable version evidence
   (`music21_batch.py`?, `inject_m21_rn.py`, registry notes, JSON internals — some
   music21 exports embed version strings; probe a few files).
2. If a version is established [probe/code]: record it in `tools/corpus/README.md` and
   add a `music21_version` field to the corpus-manifest schema (written by
   `run_bach_preset.py` as informational copy-through; validation does NOT enforce it).
3. If NOT establishable: freeze-by-fiat — README states the 353 `.music21.json` are
   canonical as-committed (sha256 aggregate recorded), regeneration with any music21
   version is a DELIBERATE re-baseline event, and the current installed music21 version
   (probe `python -c "import music21; print(music21.VERSION_STR)"` — may differ from
   the generator!) is recorded as "environment today", not provenance.

## Task 3 — C3: the 353/361/410 trace

1. Recover the filter: what produced 353 from the music21 retrieval (the registry note
   says "352 genuine SATB from 410" — find the script/criteria; note the 352→353
   discrepancy too). [probe/code] or honest unknown.
2. Produce the diff list: DCML `bach_chorales/MS3` 361 stems vs our 353 stems — which
   are missing on each side (stem-normalization may be needed; show your mapping).
3. Document both in `score_inventory.md` (Task 5) — recommendation only; expanding the
   corpus is a Stage-5 decision, NOT this run.

## Task 4 — C4 deletions (each its own verification)

1. Flat `tools/corpus/*.ours.json` (353 stale pre-2.2a outputs): confirm nothing reads
   them anymore (Rider 1 landed; grep tools/ for flat-dir .ours.json readers — the
   deprecated `--ours-dir` alias path counts: report what using the alias does NOW and
   whether it validates), then delete. Update `tools/corpus/README.md` (inputs only:
   xml + music21.json + per-preset subdirs).
2. Empty accident dirs `tools/corpus/corpus/`, `tools/corpus/reports/`: confirm empty,
   delete.
3. `src/composing/tests/scores/` (7 files incl. `xxxxx.mxl`): final full-repo sweep
   beyond the audit's grep — filenames AND stems, all file types, plus docs/memory
   references (a docs hit ≠ a consumer, but list it). If truly zero consumers: delete
   the directory in its OWN commit (removes committed binaries; easy to revert).
   If any consumer surfaces: stop, report.
4. Stray `C:tmpbuild_out`-class junk: none expected — confirm clean.

## Task 5 — Refresh `docs/score_inventory.md`

Update to current reality: snapshot suite = 11 DCML-sourced scores (list them + manifest
pointer), `tools/corpus` post-2.2a layout (per-preset subdirs + manifests + flat inputs),
the C3 provenance section, deletion of the dead scores dir, mismatch-count touch-up,
"Last updated" date. Keep its excellent quick-pick/hard-rules format.

## Task 6 — Verify + commits

Python suite green (65 + new manifest test); no C++ change expected → no build needed
UNLESS Task 4.3 touches a CMakeLists (then build + full suites). One clean-regen
spot-check: `characterise_bir_false --corpus-dir tools/corpus/baroque` → 13.

Commits (propose, await Cowork confirmation as a set):
- H1 `tools: pin snapshot/gate source corpora — manifests + drift test + REPRODUCIBILITY pins (corpus audit C1)`
- H2 `tools: record music21 + chorale-corpus provenance (corpus audit C2-C3)` (may fold into H1 if small)
- H3 `chore: delete stale corpus outputs and accident dirs (corpus audit C4.1-2)`
- H4 `chore: remove unreferenced test scores from src/composing/tests/scores (corpus audit C4.3)`
- H5 `docs: refresh score_inventory.md to post-2.2a reality (corpus audit C4.4)`

## Report — `cc_corpus_hygiene_report.md`

§1 manifest contents summary + clone commits (or dirty/non-git facts); §2 license
findings (facts only); §3 music21 verdict (established vs freeze-by-fiat); §4 the
353/361/410 trace + diff lists; §5 deletion evidence (sweep results, alias behavior);
§6 unknowns; §7 commit set. Tag claims [probe]/[code].

Stop conditions: a snapshot-source clone is dirty or its file hashes don't match what
the goldens were generated from (gate-integrity question — report immediately); any
consumer of the to-be-deleted scores; anything needing a score-content or metric-logic
change.
