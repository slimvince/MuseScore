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

### tools/dcml/ — corpus wave 1 (DLC container completed, 2026-07-02)

The Distant Listening Corpus (`github.com/DCMLab/distant_listening_corpus`) has
**40 submodules** (verified from its `.gitmodules`; the census's "41" was an
overcount). The project used 10 of them (the gate-relevant repos above, minus
`bach_chorales`/`when_in_rome` which are not DLC submodules); corpus wave 1
onboarded the **other 30** as **research-tier** clones under `tools/dcml/`. These
are **NOT gate-load-bearing** — cloning/removing them does not touch the BIR gate
or the 11-score snapshot suite. Each is `--depth 1` cloned; the pinned commit is
clone-time HEAD of the default branch (the exact shas are the source of truth in
`tools/score_census_registry.json → distant_listening_corpus.members[].pinned_commit`;
regenerate that file with `python tools/build_score_census_registry.py`).

**License:** only 12 of the 40 DLC repos carry an explicit `LICENSE`
(CC BY-NC-SA 4.0); the other 28 have **no in-repo LICENSE** (org statement is
CC BY-NC-SA [reported]). All 40 are gitignored under `tools/dcml/` and therefore
**hash-pin-only, never committed in-tree** (the C1 mechanism) regardless of
license — so the missing-LICENSE repos raise no distribution risk.

```bash
cd tools/dcml
# 30 corpus-wave-1 clones (research-tier; pins as of 2026-07-02).
git clone https://github.com/DCMLab/bach_solo && git -C bach_solo checkout dce67f753ced46b43dbfb16779fe3a19233893da
git clone https://github.com/DCMLab/bartok_bagatelles && git -C bartok_bagatelles checkout c6221f6ecb4dbcd476e827f6bf8705bdcb15c8a9
git clone https://github.com/DCMLab/beethoven_piano_sonatas && git -C beethoven_piano_sonatas checkout ea7181bff88abc8713257234f7ec4033178c57a9
git clone https://github.com/DCMLab/c_schumann_lieder && git -C c_schumann_lieder checkout 9ed9255559c670a79a76bc1b21a911b16efe492d
git clone https://github.com/DCMLab/couperin_clavecin && git -C couperin_clavecin checkout 3bd00fc56d3473b26f1bea5fe50d1a1f2458c462
git clone https://github.com/DCMLab/couperin_concerts && git -C couperin_concerts checkout 49efcdd24c39d48bf009d60f8aa3bbc1a1d9713a
git clone https://github.com/DCMLab/debussy_suite_bergamasque && git -C debussy_suite_bergamasque checkout 322ece590e536924308a551a69d9c1520248d3d5
git clone https://github.com/DCMLab/frescobaldi_fiori_musicali && git -C frescobaldi_fiori_musicali checkout e17de917111e900929db785bfa2d0313968ca5d4
git clone https://github.com/DCMLab/handel_keyboard && git -C handel_keyboard checkout d3b42765e0d2457b6abb1bdb3e8dd622db61b084
git clone https://github.com/DCMLab/jc_bach_sonatas && git -C jc_bach_sonatas checkout ac9fd07905eb62c3d8cfbd96811491170a216232
git clone https://github.com/DCMLab/kleine_geistliche_konzerte && git -C kleine_geistliche_konzerte checkout b3cc43d4ffc9a141b85400ab460aaeb95c29ea4a
git clone https://github.com/DCMLab/kozeluh_sonatas && git -C kozeluh_sonatas checkout 23c1983a48809647af1a08d54b1fade39ec93995
git clone https://github.com/DCMLab/liszt_pelerinage && git -C liszt_pelerinage checkout f1cfd308adba5763aad3a18885eac48d42449fc4
git clone https://github.com/DCMLab/mahler_kindertotenlieder && git -C mahler_kindertotenlieder checkout 9122b6d313b94185ad6a42710ad09b7c59d31af5
git clone https://github.com/DCMLab/medtner_tales && git -C medtner_tales checkout 1d2e58ba8d329463829e45e75900af43be4256bf
git clone https://github.com/DCMLab/mendelssohn_quartets && git -C mendelssohn_quartets checkout b92a90c5ce2423a3f0d32536dc5c1304fe6d0369
git clone https://github.com/DCMLab/monteverdi_madrigals && git -C monteverdi_madrigals checkout 6e1adc73a865b50fb8b8f38661f06c4fad8c2b53
git clone https://github.com/DCMLab/pergolesi_stabat_mater && git -C pergolesi_stabat_mater checkout b24d5432884d641ba98cf49b107c47d199d38100
git clone https://github.com/DCMLab/peri_euridice && git -C peri_euridice checkout f02fc6643ac489776aaed5418c1109e88381648f
git clone https://github.com/DCMLab/pleyel_quartets && git -C pleyel_quartets checkout 8b3d7f5e966290631571274067de6d3a9206a737
git clone https://github.com/DCMLab/poulenc_mouvements_perpetuels && git -C poulenc_mouvements_perpetuels checkout 7793981bf4bc9dbcc1d14de4c17abb4cb412ce4b
git clone https://github.com/DCMLab/rachmaninoff_piano && git -C rachmaninoff_piano checkout a73f3246a764215863000357c81309b210a43f15
git clone https://github.com/DCMLab/ravel_piano && git -C ravel_piano checkout 5a97ccee5383a87dc38688733a59dba499ef44d9
git clone https://github.com/DCMLab/scarlatti_sonatas && git -C scarlatti_sonatas checkout 7750a6086db69c48e5e65f71565d24bd0f68513a
git clone https://github.com/DCMLab/schubert_winterreise && git -C schubert_winterreise checkout da2e281eec9bbcf8ae1e981f63f913a1a99b5edb
git clone https://github.com/DCMLab/schulhoff_suite_dansante_en_jazz && git -C schulhoff_suite_dansante_en_jazz checkout e558f2d2505dcdf827b4212e87fda875e0440908
git clone https://github.com/DCMLab/schumann_liederkreis && git -C schumann_liederkreis checkout 226b788546e0b5c4907b996cb35f94bb4a38e980
git clone https://github.com/DCMLab/sweelinck_keyboard && git -C sweelinck_keyboard checkout 0c2a4f5b613e44b6ab06e876d1f0d9afb9f1d445
git clone https://github.com/DCMLab/wagner_overtures && git -C wagner_overtures checkout fe316b6ce8ba1e5f5ee01a01b323f3d13a876382
git clone https://github.com/DCMLab/wf_bach_sonatas && git -C wf_bach_sonatas checkout 379e50dd389dbdbcf77f5eb88ecac7841c7ed0e4
```

  Each has the same `MS3/` (`.mscx`) + `harmonies/` (`.harmonies.tsv`) layout as
  the pre-wave-1 members, so `tools/run_dlc_baseline.py` and `dcml_parser.py`
  consume them unchanged. Descriptive baselines: `python tools/run_dlc_baseline.py
  --all-new --grid` (outputs to gitignored `tools/corpus_dlc_wave1/`).

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
  BIR denominators, not a refresh. `run_bach_preset.py` now copies the
  detected music21 version into each `corpus_manifest.json` (`music21_version`,
  informational — not validated).

  **Freeze anchor (replicated here from the gitignored `tools/corpus/README.md`
  so the committed record is self-contained):** the committed `*.music21.json`
  are **canonical as-committed**. Regenerating them with *any* music21 version is
  a **deliberate re-baseline event** (it shifts the BIR denominators), not a
  refresh — coordinate it like a golden update.

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

---

## corpora/annot/ — axis-2 annotation beds (corpus wave 2, 2026-07-03)

- **Content:** Three **annotation/validation beds** for axis 2 (voice leading) —
  expert label layers over scores, or a standalone phrase-marked melody bed. They
  are **research-tier, hash-pin-only, held-out** (never tuned against) and
  **NOT** analysis/gate corpora. The `corpora/` tree is gitignored via
  `.git/info/exclude` (see `docs/score_inventory.md`); these live in a new
  `corpora/annot/` subtree so they stay separate from the idiom-discovery inputs
  in `corpora/ship|expl/`.
- **Source of truth for the pins:** `tools/score_census_registry.json →
  annotation_beds[].pinned_commit` (regenerate with
  `python tools/build_score_census_registry.py`; shas read live from the clones).
  Full inventory + paper-claim verification: `cc_corpus_wave2_report.md`.
- **Licenses (recorded, all hash-pin-only regardless):** schema — no in-repo
  LICENSE (DCMLab org CC BY-NC-SA [reported] → unclear); texture — GPLv3 (code) +
  ODbL-1.0 (data); Essen — CCARH MuseData **non-commercial** (no commercial/
  derivative distribution). None forbids a local gitignored research clone.

```bash
mkdir -p corpora/annot && cd corpora/annot
# VL-F footing — galant voice-leading-schema annotations over 18 Mozart sonatas
git clone https://github.com/DCMLab/schema_annotation_data \
  && git -C schema_annotation_data checkout 76f810a1a5522fc599f389ffae0c6a0c5cf94b5c
# VL-C validation — per-bar symbolic-texture annotations, 9 Mozart mvts (K279/280/283)
git clone https://gitlab.com/algomus.fr/symbolic-texture-dataset \
  && git -C symbolic-texture-dataset checkout 3dce4ab8cff8c50d540783ec435480551a1d71c6
# VL-E footing — Essen Folksong Collection (Humdrum **kern, phrase-boundary marks)
git clone https://github.com/ccarh/essen-folksong-collection \
  && git -C essen-folksong-collection checkout 2d0ca75e87dc7a725556c8090e3681c1fa3a0452
```

  The schema and texture beds add **labels over Mozart piano sonatas already held**
  (`tools/dcml/mozart_piano_sonatas`); Essen is a self-contained monophonic melody
  bed (no chord symbols, no voice pairs). Alignment details in the wave-2 report.
