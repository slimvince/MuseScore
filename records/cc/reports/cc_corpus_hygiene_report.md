# Corpus-hygiene report — pin the gate's ground truth (audit C1–C4)

*CC, 2026-06-11. Base `9e52147b04`. Implements the Disposition table of
`cowork_corpus_audit.md`. Provenance + hygiene only — no metric/classification
logic touched, no score content edited, `chordanalyzer_catalog.musicxml`
untouched, `muse/` untouched. Tags: [probe] = observed by running/reading;
[code] = read from source.*

---

## §1 — Manifest contents + clone commits (C1)

New file `tools/snapshot_sources_manifest.json` (schema 1). Contents:

**The 11 snapshot sources** (enumerated from `kCorpus` in
`pipeline_snapshot_tests.cpp` [code], not from the audit's list — they agree):
each gets `{id, path, repo, upstream_url, clone_commit, clone_state, size,
sha256}`. All 11 hashed [probe]. Repo → clone commit (all **clean** working
trees [probe]):

| repo (snapshot sources) | clone commit | license |
|---|---|---|
| bach_chorales (×3 scores) | `b8169ca06d9e183c59f317cce3b3b1e369f70d78` | no LICENSE file |
| bach_en_fr_suites (×2) | `9cd6d362ed8246ed8edfc425944862ed88ddf1a5` | no LICENSE file |
| mozart_piano_sonatas (×2) | `5337257a5318711e6302cfe85c3f1a6ade3c6271` | CC BY-NC-SA 4.0 |
| chopin_mazurkas (×2) | `5931135e614985023b96de2a291c74b7ef90b287` | CC BY-NC-SA 4.0 |
| corelli (×1) | `65608a1a193bb2375a018060b266645ba05a0bc4` | CC BY-NC-SA 4.0 |
| schumann_kinderszenen (×1) | `ee929c1556bc937fe1ea7303cac4476e37caa4d1` | CC BY-NC-SA 4.0 |

**The BIR gate's WiR annotation inputs** (C1, derived **by probe** — ran
`dcml_parser.find_wir_file` over the 353 chorale stems and logged the resolved
paths [probe], not assumed): of 353 stems, **326 resolve** to a When-in-Rome
`analysis.txt`, **324 distinct** files, **27 uncovered**. Recorded with the
`when_in_rome` clone commit `aa7539f1cf480997a68998405c0783ebf6339c16` (clean),
the full 324-path list, per-file hashing, and an **aggregate sha256**
`a2bce164b577e9a254c46a1e5416a6de12ad97cb9fc0db2d5c9c6a3405db5d4e`
(sha256 over the newline-joined sorted per-file digests).

**Drift test** `tools/tests/test_snapshot_sources.py` (3 tests, all pass
[probe]): verifies the 11 sources against the manifest and fails with *"source
corpus drifted — see tools/snapshot_sources_manifest.json"*; a second test
re-derives the WiR aggregate; both **skip cleanly** when `tools/dcml` (or
`when_in_rome`) is absent. Nothing wired into the C++ suite this run (kept tight).

**REPRODUCIBILITY.md**: every clone command now pins its commit
(`git clone … && git -C … checkout <hash>`), split into gate-load-bearing vs
other repos, with an explicit "bumping a pin is a deliberate re-baseline" note.
The other 5 (non-gate) repos were also pinned for reproducibility — **`ABC` was
DIRTY at pin time [probe]; recorded verbatim, not guessed** (ABC is Beethoven, not
a gate source, so its dirtiness does not affect gate integrity).

## §2 — License findings (facts only, audit C1)

[probe] LICENSE files in the consumed clones:

- **CC BY-NC-SA 4.0:** mozart_piano_sonatas, chopin_mazurkas, corelli,
  schumann_kinderszenen (LICENSE file = "Attribution-NonCommercial-ShareAlike 4.0
  International").
- **No LICENSE file:** bach_chorales, bach_en_fr_suites, when_in_rome.

Plain statement (deciding nothing): CC BY-NC-SA 4.0 is **NonCommercial +
ShareAlike**, which is incompatible with this repo's **GPL-3.0** (GPL forbids the
NC use-restriction and the SA-to-non-GPL conflict); a repo with **no LICENSE**
defaults to all-rights-reserved, also not redistributable. **An in-tree copy of
the 11 scores would NOT be GPL-redistribution-compatible.** The hash-pin mechanism
(this manifest) is therefore the correct choice; **no copies made this run.**

## §3 — music21 verdict (C2): ESTABLISHED, not freeze-by-fiat

[probe] The generator is `tools/music21_batch.py`. The `.music21.json` carry **no**
embedded version. But the paired `tools/corpus/*.xml` (same generator) each embed
`<software>music21 v.9.9.1</software>` with `<encoding-date>2026-04-05</encoding-date>`
(checked across 5 files — all agree). The installed env as of 2026-06-11 is **also
music21 9.9.1**. So the generating version is **established: 9.9.1**.

Caveat recorded honestly: the `.music21.json` mtime is 2026-04-21 (a later pass
than the 2026-04-05 XML export) — a separate write, same generator family. Recorded
in `tools/corpus/README.md` with a **freeze anchor** (regeneration = deliberate
re-baseline) and "environment today = 9.9.1" noted as environment, not provenance.

Manifest field: `run_bach_preset.py` now copies the detected music21 version into
each `corpus_manifest.json` as an informational `music21_version` (probed from the
first source `.xml`'s `<software>` tag). **Not enforced** by `validate_corpus_dir`
[code] — verified the validator only checks preset/count/complete/per-score sha256,
so the new field cannot break validation. Helper returns `9.9.1` on the live corpus
[probe].

## §4 — The 353 / 361 / 410 trace (C3)

[code] **410 → 353 filter** recovered from `music21_batch._is_bach_chorale`: keep a
music21 bach-corpus entry iff path contains `bwv`, basename not ending in a variant
suffix (`-sc -lpz -lz -w -inst -a -2 -s -b -c`), BWV not in `{846, 846a}`, **and
exactly 4 parts (SATB)**.

[probe] **352 vs 353:** `tools/corpus_registry.json:16` records an earlier run as
"352 genuine SATB chorales (from 410 retrieved)"; the current filter yields **353**
(353 `.xml` on disk). The exact +1 between historical 352 and current 353 is **not
separately logged** — honest unknown, low stakes (one extra chorale now passes the
4-part filter).

**361 vs 353 diff list — NOT recoverable in-repo, and here is the evidence why**
(rather than a guessed mapping): DCML `bach_chorales/MS3` = 361 files [probe], named
by **Riemenschneider** number + title (`001 Aus meines Herzens Grunde.mscx`). Our
353 use music21 **BWV** identifiers (`bwv10.7`). DCML's `metadata.tsv` has **no BWV
column** — `workNumber`, `workTitle`, `source`, `copyright` are **all empty across
all 361 rows** [probe]; a regex BWV extraction matched **0/361**. The two corpora
are therefore **independent selections with orthogonal identifiers, not
subset/superset**; a stem-level diff requires an external Riemenschneider↔BWV
concordance that is not in the tree. Documented as such in `score_inventory.md` and
`tools/corpus/README.md`. **Recommendation (Stage 5, not this run):** if the corpus
is to be expanded/cross-validated, source a BWV↔Riemenschneider table first; do not
silently treat one corpus as a superset of the other.

## §5 — Deletion evidence (C4)

**C4.1 flat `tools/corpus/*.ours.json` (353):** [probe] byte-identical to the
manifested `baroque/*.ours.json` (3 samples `cmp`-equal; music21.json too).
[code/probe] Reader survey:
- `run_bach_preset.py` reads flat `.xml` + `.music21.json` (its `--corpus-dir`
  default), **never** `.ours.json` → unaffected.
- `characterise_bir_false.py` defaults to `tools/corpus/baroque` → unaffected.
- The committed Python suite uses `tools/tests/fixtures/`, **not** flat
  `tools/corpus` → unaffected (68/68 still green after deletion).
- **The one live reader:** `analyze_inversion_errors.py`'s *no-argument* default
  `_CORPUS_DIR = tools/corpus` globs flat `*.ours.json` [code]. `build_and_test.md`
  documents this no-arg path as "legacy flat dir (no manifest, no validation)".
- **Deprecated `--ours-dir` alias** [code]: reads whatever dir you give it and
  prints `WARNING: --ours-dir is deprecated`; it does **NOT** validate the manifest
  (only `--corpus-dir` validates). Pointing it at the now-empty flat dir would error
  "No .ours.json files".

Action: deleted the 353 flat `.ours.json` (gitignored — filesystem only, no git
diff). The `.xml` + `.music21.json` inputs remain (353 + 353). **Consequence
surfaced, not hidden:** the legacy `python tools/analyze_inversion_errors.py`
(no args) now errors instead of reporting Baroque 24/13; the canonical
`--corpus-dir tools/corpus/baroque` path is unaffected. I did **not** change the
script's default (that would desync `build_and_test.md`, which is outside this
pass's authorized file set, and is a behavior change beyond "manifest/validation
plumbing"). **Recommendation:** the owner of `build_and_test.md` should drop or
repoint its no-arg "legacy flat" line (its §4), and optionally repoint
`analyze_inversion_errors._CORPUS_DIR` → `tools/corpus/baroque` to match
`characterise_bir_false.py`.

**C4.2 accident dirs:** `tools/corpus/corpus/` and `tools/corpus/reports/` confirmed
**empty** (0 entries incl. hidden) [probe] → removed (gitignored, filesystem only).

**C4.3 `src/composing/tests/scores/` (7 files):** full-repo sweep beyond the audit's
grep [probe] — filenames AND stems, all file types, plus docs/memory:
- **Zero** `CMakeLists.txt` / `.cmake` references (composing-tests CMakeLists lists
  test `.cpp` explicitly + `MODULE_TEST_DATA_ROOT`; never `scores/`).
- **Zero** `.cpp`/`.h` references (the only `scores/` hits in `src` are
  `vtest/scores/...` engraving visual-test paths — unrelated).
- **Zero** `.py` references.
- Doc/registry hits are not consumers: `score_inventory.md` (the stale claim being
  fixed), the audit, STATUS, COWORK_HANDOFF; and a **filename collision** —
  `like-someone-in-love` also appears in `tools/extra_scores_registry.json` and
  `lsil_artifacts.json`, but those point at the `tools/extra scores/` copy, not the
  test dir.

→ truly zero consumers. Deleted the directory via `git rm` (7 tracked binaries,
own commit H4; easy to revert). No CMakeLists touched → **no C++ build required**.

**C4.4 stray `C:tmpbuild_out`-class junk:** none found [probe] — clean.

## §6 — Unknowns / honest gaps

1. The historical **352 → 353** +1 chorale identity is not logged (§4). Low stakes.
2. The **361↔353** stem diff is not computable in-repo (orthogonal identifiers, §4)
   — stated, not guessed.
3. `when_in_rome` and `bach_chorales`/`bach_en_fr_suites` have **no LICENSE file**;
   their license is whatever the GitHub repo states at the pinned commit (not
   re-verified online this run) — flagged in the manifest as "verify upstream
   before any redistribution".
4. The 27 chorale stems with **no WiR coverage** are expected (When-in-Rome's Bach
   slice is a subset); they fall out of the three-way gate by construction, not a
   defect.

## §7 — Proposed commit set (await confirmation)

Tracked changes only. **Note:** C4.1/C4.2 deletions are under gitignored
`tools/corpus/` → **no commit** (filesystem hygiene only); the audit's "H3" is moot.

- **H1** `tools: pin snapshot/gate source corpora — manifest + drift test + REPRODUCIBILITY pins (corpus audit C1)`
  → `tools/snapshot_sources_manifest.json` (new), `tools/tests/test_snapshot_sources.py` (new),
    `tools/REPRODUCIBILITY.md` (clone-commit pins **and** the C2 music21-version pin — same file).
- **H2** `tools: record music21 provenance in corpus manifest (corpus audit C2)`
  → `tools/run_bach_preset.py` (`music21_version` informational field + `_detect_music21_version`).
  *(C2/C3 prose also went to `tools/corpus/README.md`, which is **gitignored** — not committed.)*
- **H4** `chore: remove unreferenced test scores from src/composing/tests/scores (corpus audit C4.3)`
  → the 7 `git rm`-staged binaries.
- **H5** `docs: refresh score_inventory.md to post-2.2a reality (corpus audit C4.4)`
  → `docs/score_inventory.md`.

This report (`cc_corpus_hygiene_report.md`) left untracked, matching the other
`cowork_*`/`cc_*` reports in the tree.

**Verification:** Python suite **68/68** [probe] (was 65 + 3 new); spot-check
`characterise_bir_false --corpus-dir tools/corpus/baroque` → **13** genuine
BIR=false, manifest validates OK, "326 with WiR coverage" matches §1 [probe]. No
C++ change → no build (no CMakeLists touched).
