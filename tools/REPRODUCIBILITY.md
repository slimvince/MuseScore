# tools/ corpora — reproduction instructions

The bulk corpora under `tools/` are excluded from version control (see
`.gitignore` entries like `/tools/dcml/`, `/tools/corpus_*/`, etc.) because
they are large and publicly re-fetchable or regenerable. This file documents
how to recreate each excluded directory.

Do not commit anything under these paths. The authoritative list of what is
tracked vs. ignored under `tools/` is `.gitignore`.

---

## tools/dcml/

- **Size:** ~1.9 GB (12 sub-repos cloned from GitHub)
- **Content:** Harmonic annotation corpora in DCML TSV format plus MS3
  (MuseScore 3 `.mscx`) score files. Used for automated validation by
  `run_*_validation.py` and `run_validation.py`.
- **Retrieval:** Clone each sub-repository AND check out its pinned commit. These
  are living research repos at floating upstream HEAD; the pipeline-snapshot
  goldens and the BIR baselines are byte-meaningful only against the exact
  commits below (corpus audit C1). Commits recorded 2026-06-11 from the working
  clones; the seven gate-relevant repos are also hash-pinned per-file in
  `tools/snapshot_sources_manifest.json` (the source of truth — bump there too).

```bash
cd tools/dcml

# ── Gate-load-bearing repos (snapshot sources + BIR WiR annotations) ──
git clone https://github.com/DCMLab/bach_chorales        && git -C bach_chorales        checkout b8169ca06d9e183c59f317cce3b3b1e369f70d78
git clone https://github.com/DCMLab/bach_en_fr_suites    && git -C bach_en_fr_suites    checkout 9cd6d362ed8246ed8edfc425944862ed88ddf1a5
git clone https://github.com/DCMLab/mozart_piano_sonatas && git -C mozart_piano_sonatas checkout 5337257a5318711e6302cfe85c3f1a6ade3c6271
git clone https://github.com/DCMLab/chopin_mazurkas      && git -C chopin_mazurkas      checkout 5931135e614985023b96de2a291c74b7ef90b287
git clone https://github.com/DCMLab/corelli              && git -C corelli              checkout 65608a1a193bb2375a018060b266645ba05a0bc4
git clone https://github.com/DCMLab/schumann_kinderszenen && git -C schumann_kinderszenen checkout ee929c1556bc937fe1ea7303cac4476e37caa4d1
git clone https://github.com/MarkGotham/When-in-Rome when_in_rome && git -C when_in_rome checkout aa7539f1cf480997a68998405c0783ebf6339c16

# ── Other annotated corpora (not gate-load-bearing; pinned for reproducibility) ──
git clone https://github.com/DCMLab/ABC                 && git -C ABC                 checkout b6b7d38500bacb30c81db7e09d8790df1a2edd46   # NOTE: working clone was DIRTY at pin time (2026-06-11)
git clone https://github.com/DCMLab/cpe_bach_keyboard   && git -C cpe_bach_keyboard   checkout 4b3511eab12b5fbfc7aa5c75819ee02225430da8
git clone https://github.com/DCMLab/dvorak_silhouettes  && git -C dvorak_silhouettes  checkout f228006fcd8696c809cfc8e701ed215cec3d07f1
git clone https://github.com/DCMLab/grieg_lyric_pieces  && git -C grieg_lyric_pieces  checkout 91a304563521f3f273b8c0aadec1ce2ede2d1384
git clone https://github.com/DCMLab/tchaikovsky_seasons && git -C tchaikovsky_seasons checkout 5af15033c5f9c282f38fcf71234b86349e61e8c3
```

  After cloning, each sub-repo's `MS3/` subdir holds the score files and
  `harmonies/` (or equivalent) holds the annotation TSVs expected by the
  validation runners.

  **Bumping a pin is a deliberate re-baseline event.** Moving any gate-relevant
  repo (the first block) to a newer commit can change the snapshot goldens and the
  BIR case-identity sets. Update `tools/snapshot_sources_manifest.json` first,
  then regenerate the affected goldens (`pipeline_snapshot_tests --update-goldens`)
  and re-measure the BIR gate — never silently. `tools/tests/test_snapshot_sources.py`
  fails if disk drifts from the manifest without the manifest being updated.

---

## tools/corpus/

- **Size:** ~58 MB
- **Content:** Bach chorale scores exported to MusicXML plus
  `.music21.json` harmonic analysis files. Generated from music21's
  built-in corpus. Used as input for `compare_analyses.py` and
  `inject_m21_rn.py`.
- **Retrieval:** Regenerate via:

```bash
python tools/run_validation.py --output tools/
```

  or, to only re-run the music21 export step:

```bash
python tools/music21_batch.py --composer bach --output tools/corpus
```

  Requires music21 to be installed (`pip install music21`).

  **music21 version pin (audit C2):** the committed `tools/corpus/*.xml` were
  exported by **music21 v.9.9.1** (recorded in each file's
  `<software>music21 v.9.9.1</software>` / `<encoding-date>2026-04-05</encoding-date>`
  tag), and the paired `*.music21.json` ground truth is from the same generator.
  Regenerating with a different music21 is a **deliberate re-baseline** of the
  BIR denominators, not a refresh. See `tools/corpus/README.md` for the full
  provenance record and the freeze anchor. `run_bach_preset.py` now copies the
  detected music21 version into each `corpus_manifest.json` (`music21_version`,
  informational — not validated).

---

## tools/corpus_when_in_rome/

- **Size:** ~33 MB
- **Content:** Working copies of When-in-Rome score + analysis pairs,
  extracted by `compare_when_in_rome.py` for validation alignment.
- **Retrieval:** Populated automatically when running
  `compare_when_in_rome.py` against `tools/dcml/when_in_rome/`.
  Requires `tools/dcml/when_in_rome/` to be present (see above).

---

## tools/corpus_omnibook_src/

- **Size:** ~11 MB
- **Content:** Charlie Parker Omnibook scores as MusicXML files.
  Used by `compare_omnibook.py` for jazz analysis validation.
- **Source:** https://homepages.loria.fr/evincent/omnibook/
- **Retrieval:** Download the MusicXML files from the Omnibook page at
  homepages.loria.fr/evincent/omnibook/. Extract into
  `tools/corpus_omnibook_src/`.

---

## tools/corpus_effendi_src/

- **Size:** ~29 MB
- **Content:** MusicXML scores used for Effendi jazz corpus validation.
  Filtered by `filter_effendi.py` to select scores with harmony tags.
- **Source:** https://effendi.me/jazz/repo/
- **Retrieval:** Fetch MusicXML files from the Effendi jazz repository at
  effendi.me/jazz/repo/. Extract into `tools/corpus_effendi_src/`.

---

## tools/corpus_rampageswing_full/

- **Size:** ~27 MB
- **Content:** Jazz big-band scores in MXL format. Used for jazz analysis
  validation.
- **Source:** https://www.rampageswing.com/
- **Retrieval:** Corpus was assembled by crawling www.rampageswing.com; the
  exact crawl script was not preserved. Re-crawl the site to reconstruct
  (typical pattern: walk the site's arrangement pages and download MXL
  files linked from each). Extract into `tools/corpus_rampageswing_full/`.

---

## tools/pdmx/

- **Size:** ~217 MB
- **Content:** PDMX (PolyphonyDAta Music eXtract) dataset files including
  `PDMX.csv` (metadata index) and spot-check MXL score downloads.
- **Source:** Zenodo record `10.5281/zenodo.15571083`
  - MXL archive: `https://zenodo.org/api/records/15571083/files/mxl.tar.gz/content`
- **Retrieval:**
  1. Download `PDMX.csv` from the Zenodo record above into `tools/pdmx/`.
  2. Run `python tools/pdmx_jazz_candidates.py` to produce
     `tools/pdmx/jazz_candidates.csv`.
  3. Run `python tools/pdmx_spot_check.py` to download spot-check MXLs
     into `tools/pdmx/spot_check/`.

---

## tools/corpus_*/ (working copies)

Most `corpus_*` directories are timestamped working copies produced by
running batch_analyze against a source corpus with a specific configuration.
They are all regenerable.

| Pattern | Source corpus | Regeneration script |
|---|---|---|
| `corpus_bach_*/` | `dcml/bach_chorales/` | `run_bach_preset.py` / `run_validation.py` |
| `corpus_beethoven_v2/` | `dcml/ABC/` | `run_beethoven_validation.py` |
| `corpus_chopin_*/` | `dcml/chopin_mazurkas/` | `run_chopin_validation.py` |
| `corpus_corelli_*/` | `dcml/corelli/` | `run_corelli_validation.py` |
| `corpus_dvorak_*/` | `dcml/dvorak_silhouettes/` | `run_dvorak_validation.py` |
| `corpus_grieg_*/` | `dcml/grieg_lyric_pieces/` | `run_grieg_validation.py` |
| `corpus_mozart_v2/` | `dcml/mozart_piano_sonatas/` | `run_mozart_validation.py` |
| `corpus_schumann_*/` | `dcml/schumann_kinderszenen/` | `run_schumann_validation.py` |
| `corpus_tchaikovsky_v2/` | `dcml/tchaikovsky_seasons/` | `run_tchaikovsky_validation.py` |
| `corpus_cpe_bach_*/` | `dcml/cpe_bach_keyboard/` | `run_cpe_bach_validation.py` (if present) |
| `corpus_omnibook*/` | `corpus_omnibook_src/` | `compare_omnibook.py` |
| `corpus_effendi_*/` | `corpus_effendi_src/` | `filter_effendi.py` |
| `corpus_rampageswing_*/` | `corpus_rampageswing_full/` | manual run |
| `corpus_standard*/`, `corpus_baroque/` | Internal test scores | `run_bach_preset.py` with alternate preset |
| `corpus_when_in_rome_*/` | `dcml/when_in_rome/` | `compare_when_in_rome.py` |

---

## tools/reports/

- **Size:** ~1.0 GB
- **Content:** JSON analysis output from `batch_analyze` runs. Each
  subdirectory is a timestamped run result.
- **Retrieval:** Regenerable by re-running the corresponding
  `run_*_validation.py` script. Use the `--output` flag to direct output
  to a new timestamped subdirectory.

---

## tools/tools/

- **Size:** ~312 MB
- **Content:** An earlier corpus output tree containing music21-exported
  Bach chorale XML files and analysis JSON. Superseded by `tools/corpus/`.
- **Retrieval:** Regenerable — same procedure as `tools/corpus/` above
  (`music21_batch.py`).

---

## tools/validation_bach_postport/ and tools/bach_path3fix_*/

- **Content:** Experimental / timestamped output directories from prior
  analysis runs. Not reproducible byte-identically.
- **Retrieval:** Recreate by re-running the relevant validation script
  against the current corpus and `batch_analyze` binary as needed. These
  directories document historical runs and are generally superseded by
  the `corpus_*/` + `reports/` pattern.
