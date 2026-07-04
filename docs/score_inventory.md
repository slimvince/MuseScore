# Score & corpus inventory

Last updated: 2026-06-11 (corpus-hygiene pass — audit C1–C4).

This document is a **usage map**: for any task that needs scores (validation,
snapshot tests, manual QA, LLM-triage, qualitative review), it tells you which
folder to reach for and why. It complements:

- `tools/REPRODUCIBILITY.md` — *how to recreate* each corpus from public
  sources if `tools/` is wiped, with the **pinned clone commits**.
- `tools/snapshot_sources_manifest.json` — the **per-file sha256 + clone-commit
  pins** for the 11 snapshot-gate sources and the When-in-Rome BIR annotation set
  (audit C1). `tools/tests/test_snapshot_sources.py` fails if disk drifts from it.
- `tools/corpus_registry.json` and `tools/extra_scores_registry.json` —
  machine-readable per-run / per-score metadata.

If you only have a minute, read the **quick-pick table** and the **Hard rules**.

---

## Quick-pick table

| If you want to… | Use | Path | Notes |
|---|---|---|---|
| Run unit tests / mismatch report | In-tree fixtures | `src/composing/tests/data/` | Wired into `composing_tests` (498/498). The synthetic catalog drives the mismatch report; **do not edit without explicit approval** (Hard rules) |
| Run pipeline snapshot tests | 11 DCML `.mscx`, loaded from `tools/dcml/*/MS3/` | `src/notation/tests/pipeline_snapshot_tests/` (test + goldens) | Snapshot diffs gate refactors. Sources are pinned in `tools/snapshot_sources_manifest.json` |
| Measure the BIR gate | `tools/corpus/baroque/` or `…/jazz/` | per-preset `.ours.json` + `.music21.json` + manifest | `characterise_bir_false.py --corpus-dir …` (Baroque 53, Jazz 24, Default 53 — re-baselined 2026-06-13 + L3-wiring delta 2026-06-26; see CLAUDE.md) |
| Validate analyzer against Roman-numeral annotations | DCML annotated corpora | `tools/dcml/<repo>/MS3/` + `harmonies/` | ~1,700 scores; `run_*_validation.py`, `compare_when_in_rome.py` |
| Validate jazz analysis (single-line / Real Book) | Effendi, Omnibook | `tools/corpus_effendi_src/`, `tools/corpus_omnibook_src/omnibook_xml/` | No RNA ground truth — `compare_omnibook.py` heuristics |
| Validate jazz analysis (big-band / multi-horn) | Rampageswing | `tools/corpus_rampageswing_full/` | 36 MXL; no ground truth |
| Random sampling across many genres | PDMX spot-check | `tools/pdmx/spot_check/` | 5 MXL sampled from PDMX/Zenodo |
| Qualitative review / "does this sound right" | `tools/extra scores/` | user-curated `.mscz` files | No ground truth. **Quote the path** — has a space |
| LLM-triage corpus (Mode 2 quality work) | `tools/extra scores/hiromi/` | 20 Hiromi Uehara scores | Qualitative-review corpus. **Not** for snapshots or ground truth |
| Re-derive analyzer outputs over a corpus | `tools/corpus_*/` working copies | Various `corpus_<name>_v2/`, `…_<timestamp>/` | `.ours.json` outputs only — regenerable; not score sources |

---

## In-tree fixtures (wired into `composing_tests`)

### `src/composing/tests/data/`

The **only** scores actually exercised by the C++ test binary.

- `chordanalyzer_catalog.musicxml` — the synthetic C-major catalog that drives
  the mismatch report read after every test run. Per memory
  `project_composing_tests_baseline_synthetic.md`, **the entire mismatch baseline
  came from this single file**, so the on-disk numbers reflect catalog choices,
  not real-music quality (currently pinned at 4 RealDiff).
- `chordanalyzer_context.musicxml` — context fixtures for analyzer unit tests.
- `chord_analysis_test.musicxml`, `mono_smoke_test.musicxml`,
  `solid theory.musicxml` — small targeted fixtures.
- `francis-poulenc-o-magnum-mysterium.mxl`,
  `organ-sonata-n1-in-e-flat-major-bwv-525-i-allegro.mxl` — real-music smoke
  fixtures consumed by the data-side tests.

The `regionanalysis_tests.cpp` suite also loads ~9 minimal `.mscx` fixtures under
`src/composing/tests/` (engraving test-env copies); these are unit pins.

### `src/composing/tests/scores/` — DELETED (audit C4.3)

This directory (7 files incl. one literally named `xxxxx.mxl`) was referenced by
**nothing** — no `.cpp`, `.h`, `CMakeLists.txt`, `.cmake`, or `.py` consumed it
(verified by full-repo sweep, 2026-06-11: filenames and stems, all file types).
Earlier editions of this inventory wrongly called it "the pipeline snapshot suite
(eight scores)" — doubly wrong (it held 7, and the real suite is the 11 DCML
scores below). The dead committed binaries were removed.

---

## Pipeline snapshot suite — 11 DCML scores (the real refactor gate)

The snapshot test is **`src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`**
(a separate binary from `notation_tests`). Its `kCorpus` loads **11 `.mscx` files
from the gitignored `tools/dcml/*/MS3/` clones**; goldens live next to it under
`snapshots/`. Refactors must produce byte-identical snapshots (11/11) or the diff
is investigated. Sources are **pinned** in `tools/snapshot_sources_manifest.json`
(per-file sha256 + upstream clone commit).

| Snapshot id | Source `.mscx` (under `tools/dcml/`) |
|---|---|
| `bach_chorale_001` | `bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx` |
| `bach_chorale_003` | `bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx` |
| `bach_chorale_137` | `bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx` |
| `bach_bwv806_prelude` | `bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx` |
| `bach_bwv806_gigue` | `bach_en_fr_suites/MS3/BWV806_10_Gigue.mscx` |
| `mozart_k279_1` | `mozart_piano_sonatas/MS3/K279-1.mscx` |
| `mozart_k280_1` | `mozart_piano_sonatas/MS3/K280-1.mscx` |
| `chopin_bi105_op30_1` | `chopin_mazurkas/MS3/BI105-1op30-1.mscx` |
| `chopin_bi105_op30_2` | `chopin_mazurkas/MS3/BI105-2op30-2.mscx` |
| `corelli_op01n08a` | `corelli/MS3/op01n08a.mscx` |
| `schumann_kinderszenen_n01` | `schumann_kinderszenen/MS3/n01.mscx` |

Because these live in unpinned, gitignored clones, the goldens are byte-meaningful
only against the manifest's recorded commits. **License:** the four CC BY-NC-SA 4.0
repos (mozart/chopin/corelli/schumann) plus the no-LICENSE repos
(bach_chorales/bach_en_fr_suites) make an in-tree copy **GPL-incompatible** —
hash-pinning (not copying) is the chosen mechanism (audit C1 license check).

---

## DCML annotated corpora — `tools/dcml/<repo>/`

Twelve sub-repositories cloned from `github.com/DCMLab` and `MarkGotham/When-in-Rome`.
Each has a `MS3/` of `.mscx` scores and a `harmonies/` of TSV/rntxt annotations.
**Pinned commits in `tools/REPRODUCIBILITY.md` and the snapshot manifest.**

| Sub-repo | Scores | Style | Validation script |
|---|---:|---|---|
| `bach_chorales/` | 361 | SATB chorales | `run_bach_preset.py`, `run_validation.py` |
| `corelli/` | 149 | Baroque trio sonatas | `run_corelli_validation.py` |
| `bach_en_fr_suites/` | 89 | Keyboard suites | (use `run_validation.py`) |
| `ABC/` | 71 | Beethoven string quartets | `run_beethoven_validation.py` |
| `cpe_bach_keyboard/` | 66 | Galant keyboard | `run_cpe_bach_validation.py` |
| `grieg_lyric_pieces/` | 66 | Late-romantic piano | `run_grieg_validation.py` |
| `mozart_piano_sonatas/` | 58 | Classical piano | `run_mozart_validation.py` |
| `chopin_mazurkas/` | 56 | Romantic piano | `run_chopin_validation.py` |
| `schumann_kinderszenen/` | 13 | Romantic piano | `run_schumann_validation.py` |
| `dvorak_silhouettes/` | 12 | Late-romantic piano | `run_dvorak_validation.py` |
| `tchaikovsky_seasons/` | 12 | Romantic piano | `run_tchaikovsky_validation.py` |
| `when_in_rome/` | 762 | Mixed (When-in-Rome anthology) | `compare_when_in_rome.py` |

**when_in_rome path quirk:** every score file is named `score.mxl` under
`Corpus/<style>/<composer>/<piece>/<number>/`; any tool keying output by basename
must use per-score subdirectories. The Bach-chorale slice is the BIR gate's human
annotation ground truth (consumed via `dcml_parser.find_wir_file`).

### DLC container completed — corpus wave 1 (2026-07-02, research-tier)

The 12 repos above are the pre-wave-1 set. Corpus wave 1 onboarded the **remaining
30 Distant Listening Corpus sub-corpora** into `tools/dcml/` (the DLC has **40**
submodules total; the 10 pre-wave-1 DLC members + these 30 = all 40). They are
**research-tier and NOT gate-load-bearing** — style span ~1600 (Peri, Sweelinck,
Frescobaldi, Monteverdi) to ~1930 (Bartók, Schulhoff, Ravel, Poulenc), including
`beethoven_piano_sonatas`, `wagner_overtures` (Tristan + Meistersinger preludes),
`liszt_pelerinage`, `rachmaninoff_piano`, `scarlatti_sonatas`, and the jazz-idiom
`schulhoff_suite_dansante_en_jazz`. All 30 parse cleanly through `dcml_parser.py`
(0 quarantines) and share the `MS3/` + `harmonies/` layout.

The authoritative per-source registry (schema v2 — gt_type / license_class /
distribution / tier / **split (dev|held-out)** / pinned_commit) is
`tools/score_census_registry.json`, generated by
`tools/build_score_census_registry.py`. Pins + reproduction are in
`tools/REPRODUCIBILITY.md`; descriptive per-corpus baselines via
`tools/run_dlc_baseline.py --all-new`. Every DLC `harmonies` TSV also carries
`cadence` and `phraseend` GT columns that the parser currently drops (the "free
cadence win" — see `cc_corpus_wave1_report.md`). Full provenance:
`cc_corpus_wave1_report.md`.

---

## The BIR gate corpus — `tools/corpus/` (music21 Bach chorales, post-2.2a)

`tools/corpus/` is **gitignored**. Layout since Stage 2.2a:

- **Top level — `*.xml` + `*.music21.json` (353 each):** the preset-independent
  input / ground-truth corpus, generated by `tools/music21_batch.py`.
  `run_bach_preset.py` consumes the `.xml` and copies each `.music21.json` into
  the per-preset dir. (The 353 flat `*.ours.json` — byte-identical duplicates of
  `baroque/` — were **deleted** in this pass, audit C4.1; the only reader was the
  legacy no-arg default of `analyze_inversion_errors.py`, now superseded by
  `--corpus-dir`.)
- **`baroque/`, `jazz/` — per-preset measurement dirs:** each holds that preset's
  `*.ours.json`, a copy of every `*.music21.json`, and a `corpus_manifest.json`
  (preset stamp + per-score sha256 + informational `music21_version`).
  `characterise_bir_false.py --corpus-dir tools/corpus/<preset>` validates the
  manifest and refuses an incomplete/contaminated dir (Baroque 53, Jazz 24, Default 53 —
  re-baselined 2026-06-13 + L3-wiring delta 2026-06-26).

### music21 provenance (audit C2)

The `*.music21.json` were produced by **music21 v.9.9.1** — established by probe:
the paired `*.xml` exports embed `<software>music21 v.9.9.1</software>`
(`<encoding-date>2026-04-05</encoding-date>`); the env as of 2026-06-11 is also
9.9.1. They are **canonical as-committed**; regenerating with any music21 version
is a deliberate BIR re-baseline, not a refresh. Full record in
`tools/corpus/README.md`.

### Chorale-selection provenance (audit C3)

The 353 are music21's bach corpus filtered by `_is_bach_chorale` (has `bwv`, not a
variant suffix, not a non-chorale BWV, exactly 4 SATB parts) — the `410 → 353`
filter. (`corpus_registry.json` records an earlier "352 genuine SATB from 410"; the
current filter yields 353. The +1 is not separately logged.) **These are NOT a
subset of DCML `bach_chorales/MS3` (361):** they use music21 **BWV** identifiers
(`bwv10.7`), DCML uses **Riemenschneider** numbers with no BWV in its
`metadata.tsv`. A stem-level diff is **not recoverable in-repo** without an
external BWV↔Riemenschneider concordance — the two are independent selections, not
super/subset. Corpus-expansion / cross-validation is a Stage-5 decision; do not
silently treat one as a superset of the other.

### WiR human-annotation coverage — the gate's denominator (Stage 2.3 Rider 2)

**Only 326 of the 353 chorales resolve to a When-in-Rome human annotation** (324
distinct analysis files; some chorales share an analysis). **The other 27 scores can
never produce a "genuine" gate error** — with no human-adjudicated Roman numeral there
is nothing for `music21_dcml_agree` to agree *with*, so they are silently outside the
denominator the BIR=false count (Baroque 53 / Jazz 24 / Default 53, re-baselined 2026-06-13)
is measured over. The headline gate
therefore carries **three stacked qualifiers**, all narrowing what it sees:
1. **human-adjudicated** — only the 326 WiR-covered chorales count;
2. **music21-filtered** — a region is "genuine" only where music21 *and* WiR agree
   against us (the three-way `music21_dcml_agree` split);
3. **batch granularity** — measured at cross-barline batch regions, which undercounts
   the user-visible per-beat error rate ~7× (CLAUDE.md gate-granularity caveat).

A granularity-robust metric over the full annotated set is **roadmap 5.2** — until then,
read "Baroque 53 / Jazz 24 / Default 53" as *candidate cases among the 326 human-covered
chorales at batch granularity*, not an absolute quality figure — and note (re-baseline
2026-06-13) that ~95% of these are **legitimate ambiguity** (symmetric fully-diminished-7th,
viio↔V7 share-tones; the genuinely-actionable subset is only ~9–10 Baroque / ~4 Jazz), so the
raw count is even less an "absolute quality figure" than the old 13/7 was. A fourth implicit
qualifier — **pitch-class-root resolvable** — now applies: the symmetric-dim7 members
(≈53% Baroque) are root-undefined by construction and await a spelling-aware / two-tier gate.

---

## Jazz / non-classical corpora

(unchanged — see `tools/REPRODUCIBILITY.md` for retrieval)

- `tools/corpus_effendi_src/` — Effendi Real Book lead sheets; no RNA ground truth.
- `tools/corpus_omnibook_src/omnibook_xml/Omnibook xml/` — Charlie Parker Omnibook;
  `compare_omnibook.py`. **Path quirk:** XML is one level deeper (note the space).
- `tools/corpus_rampageswing_full/` — 36 big-band MXL; no ground truth.
- `tools/pdmx/spot_check/` — 5 randomly sampled PDMX MXL.

---

## Curated extra scores — `tools/extra scores/`

User-curated `.mscz` for qualitative work. **No ground-truth annotations.**
Documented in `tools/extra_scores_registry.json` (`ground_truth: false`). The path
**contains a space** — always quote it: `"tools/extra scores"`. Sub-folders:
`hiromi/` (20, designated LLM-triage corpus), `Steely dan/`, `piazzolla/`.

---

## The idiom-discovery corpora — `corpora/` (research data, NOT regression ground truth)

Added 2026-06-30 for the harmonic-idiom-discovery study (`cowork_idiom_discovery_findings.md`,
`idiom_discovery/`). **Gitignored** (`.git/info/exclude`) and **research-only — NOT for the analyzer's regression
tests or the BIR gate.** These are chord-symbol lead-sheet / chord-sequence corpora (no note-level scores, no
Roman-numeral ground truth for the analyzer), plus a few note-level arrangements without GT.

- `corpora/ship/` **[ship-licensed]**: ChoCo (18-source JAMS aggregator), Nottingham (folk ABC), McGill-Billboard
  (CC0 salami chords), iRealPro `iRb` (Humdrum jazz), `lda_tpcs` (Moss method reference).
- `corpora/expl/` **[expl / non-commercial — exploration only]**: the DCML clones (mozart/beethoven/romantic/scarlatti
  — **redundant with `tools/dcml/`**; only `dcml_scarlatti` is new), Jazz Harmony Treebank, Hooktheory HLSD (sample),
  POP909, `chordonomicon` (679k chord progressions, CC-BY-NC), `improvisor` (2,604 modal-jazz `.ls`; content licence
  unresolved), the converted curated `.mxl` (Steely Dan / Piazzolla / Hiromi — note-level, **no GT**).

**Why not regression material.** The gate is **byte-identity against the frozen reference set** (DCML RN + the 353
music21 chorales); adding scores would move baselines, against the dormant-build discipline. And these are chord-symbol
data (nothing to *analyze* into RN) or note-level-without-GT — so they can't be GT-regression. When **jazz/pop
analysis validation** is eventually tackled (deferred), the jazz/pop lead sheets become relevant, but real
GT-regression still needs the **jazz/pop analysis ground truth** (the standing want — none exists). The note-level
curated/arrangement scores could extend the *qualitative-review* corpus (`tools/extra scores/`), not the gate.

### `corpora/annot/` — axis-2 annotation/validation beds (corpus wave 2, 2026-07-03)

A **separate subtree** under the same gitignored `corpora/` tree, holding three **annotation/validation beds** for
axis 2 (voice leading) — expert **label layers over scores** or a standalone phrase-marked melody bed. **Research-tier,
hash-pin-only, held-out (never tuned against), NOT gate/analysis corpora.** Kept apart from the idiom-discovery inputs
in `corpora/ship|expl/` by design (they annotate scores already held, or fall outside the discovery views).

- `schema_annotation_data` (DCMLab) — galant **voice-leading-schema** annotations over 18 Mozart sonatas (VL-F footing).
- `symbolic-texture-dataset` (algomus, GitLab) — per-bar **symbolic-texture** labels, 9 Mozart mvts (VL-C validation).
- `essen-folksong-collection` (CCARH kern) — **phrase-boundary** marks on ~6.2k European monophonic folksongs (VL-E).

Pins + verification: `tools/score_census_registry.json → annotation_beds`; reproduction in `tools/REPRODUCIBILITY.md`;
full inventory in `cc_corpus_wave2_report.md`.

### `corpora/gt/` + `corpora/plain/` — Wave-3 GT & stress beds (corpus wave 3, 2026-07-04)

Two more subtrees under the same gitignored `corpora/` tree, from the census §8c FULL-NEEDS AUDIT disposition.
**Research-tier, hash-pin-only, held-out (never tuned against), NOT gate/analysis corpora.** `corpora/gt/` = ground-truth
beds; `corpora/plain/` = plain-score stress material.

- `CoCoPops` (Georgia Tech CCML) — pop/rock **melodic+harmonic transcriptions** (Humdrum `**harm` RN + `**kern`
  melody), the top Tier-J jazz/pop analysis-GT acquisition (N3/N12).
- `OpenEWLD` (00sapo) — 486 PD MusicXML **lead sheets** (chords+melody, N12); the committable subset of the gated EWLD.
- `Bach_chorale_FB` (BCFB) — 139 chorales / 143 files, **figured-bass** GT in MusicXML/kern/MEI (N10).
- `algomus-data` (algomus GitLab) — Mozart-quartet **sonata-form** (32, N16) + Bach-fugue subjects/CS/cadences/**pedals**
  (23 WTC-I, N4/N18/N20) + a jazz-arbres treebank (N11/N3).
- `protovoice-annotations` (DCMLab) — 38 **protovoice reduction derivations** over MusicXML (the N9 gating inspection).
- `schenker41` (pkirlin) — pinned but **README-only** at HEAD; the 41 Schenkerian excerpts (N11) live at the dissertation page.
- `weimar-jazz-database/wjazzd.db` — native WJD SQLite (456 solos, ODbL), sha256-pinned (non-git artifact).
- `plain/Lieder`, `plain/StringQuartets` (OpenScore, CC0), `plain/asap-dataset` (romantic piano MusicXML) — Tier-S
  chromatic/texture stress (no GT; **not** gate material — dormant-build discipline).

**Wave-3 addendum (2026-07-04, `cc_wave3_addendum_report.md`) — two DDMAL direct pickups under `corpora/gt/`:**
- `key_modulation_dataset` (DDMAL, KMT) — 201 annotated Humdrum `.krn` (5 textbooks: aldwell/kostka-payne/reger/
  rimsky-korsakov/tchaikovsky), **key/modulation** GT (N5) + textbook RN; CC-BY-SA scores / MIT code.
- `Flexible_harmonic_chorale_annotations` (DDMAL) — 571 chorales (371 Bach + 200 Praetorius), **permutational
  multi-reading** harmony GT in an R-package binary (N2 candidate); GPLv3. **⚠ RECORD-ONLY** — its 371 Bach
  chorales overlap the gate repertoire; never wired to / compared against the gate corpus (future user ruling).

**Acquisition round (2026-07-04, `cc_acquisition_round_report.md`) — the union-search-approved pickups under `corpora/gt/`:**
- `piano_svsep` (CPJKU, ISMIR 2024) — **N9 voice/staff separation**; ships CODE (MIT), GT graphs fetched at runtime from
  `fosfrancesco/piano_corpora_dcml` (393 DCML piano pieces; `jpop` companion confirmed non-public).
- `mcma` (skalo, GitLab) — **N9**; 475 `.mxl` one-voice-per-track Baroque counterpoint (split 153/239/83 verified);
  **CC-BY-NC-SA-4.0** (record said CC-BY — corrected).
- `vocsep_ijcai2023` (manoskary, IJCAI 2023) — **N9**; ships CODE (**MIT** — record said unstated), ~1,054 graphs built at
  runtime from bach-370-chorales + Haydn/Mozart SQ + MCMA.
- `Mikrokosmos-difficulty` (PRamoneda) — **N14 difficulty**; 147 MusicXML, henle 3-class labels; **no LICENSE** → hash-pin-only.
- `guitarset/annotation.zip` (Zenodo 3371780) — **N12**; sha256-pinned JAMS artifact, 360 excerpts (instructed vs performed
  chords + notes/beats/key); CC-BY-4.0; audio NOT downloaded.
- `batik_plays_mozart` (huispaty) — **multi-need**; 12 Mozart sonatas (36 mvts) harmony/cadence/phrase CSVs (N1/N4) + `.match`
  trill-mark structure (N13-partial, verified — no extraction built); **no LICENSE** → hash-pin-only. ⚠ its harmony/cadence GT =
  the DCML Annotated Mozart Sonatas we already hold (recorded, never wired to the gate).
- **Recorded (no clone):** CIPI (Zenodo 8037327, gated, USER access form pending) + PSyllabus (Zenodo 14794592, no scores).
- **PDMX N12 counting pass: STOPPED** — the held form is metadata-only (no chord-symbol column; raw MXL only on Zenodo); a
  count would need a re-download the read-only dispatch forbids (see the report §Task-3 + the `pdmx` registry row).

Pins + verification: `tools/score_census_registry.json → wave3_sources`; reproduction in `tools/REPRODUCIBILITY.md`;
full inventory + paper-claim verification + the gated/unavailable/enumerated records in `cc_corpus_wave3_report.md`
(+ the two addendum pickups + the `figbass`/`pedal` parser exposure in `cc_wave3_addendum_report.md`; + the acquisition
round in `cc_acquisition_round_report.md`).

---

## Hard rules

1. **Do NOT modify `chordanalyzer_catalog.musicxml`** without explicit approval.
   CLAUDE.md flags it as ground-truth; all current composing_tests mismatches trace
   to this one file.
2. **Do NOT add/remove the 11 snapshot sources** (in `tools/dcml/*/MS3/`, listed
   above) or bump their clone pins without coordinating — they are the snapshot
   baseline and are hash-pinned in `tools/snapshot_sources_manifest.json`. A pin
   bump is a deliberate golden + BIR re-baseline.
3. **Quote `"tools/extra scores"`** in every shell command. Path has a space.
4. **Don't conflate `tools/corpus/` (music21 BWV export) with
   `tools/dcml/bach_chorales/` (DCML Riemenschneider)** — overlapping repertoire,
   orthogonal identifiers, different export pipelines (audit C3).
5. **Use DCML/WiR for headline numbers, `extra scores/` for taste.** The only
   RNA-annotated corpus is DCML; everything in `extra scores/` is `ground_truth: false`.
6. **Measure BIR off the per-preset dirs only** (`tools/corpus/baroque|jazz`), never
   a flat or hand-assembled dir — `characterise_bir_false.py` validates the manifest
   for exactly this reason.

---

## Out-of-tree references

- `reference_hiromi_corpus.md` — Hiromi corpus location and intended use.
- `project_composing_tests_baseline_synthetic.md` — why the catalog mismatches are
  not a real-music quality measure.
- `feedback_cadence_test_fixtures.md` — small synthetic fixtures don't clear the
  0.8 confidence gate; use Corelli-scale fixtures for cadence smokes.
