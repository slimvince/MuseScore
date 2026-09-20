# CC Corpus Wave 1 — DLC container completion + registry v2 + free cadence win

> **Status: HELD for Cowork** (gitignored; `git add` OK, no commit of this file until an approval file says so).
> Executes the census §5 Tier-G first wave + §6 riders 1–2. HEAD at run: `5f7cb7376e`. Gate baseline **53/24/53**
> — this instruction changed **no `src/`** and **no gate corpus**; verification in §7.

---

## 0. Headline

- **The DLC container is complete.** The project used **10** of the Distant Listening Corpus's DCML sub-corpora;
  wave 1 onboarded the **other 30** into `tools/dcml/` as research-tier clones. All 40 submodules are now present.
- **The census's "41 submodules" is an overcount — the DLC has 40** (verified from its live `.gitmodules`, 2026-07-02;
  the GT-draft §1a table independently lists 40). Corrected in the registry.
- **Parse smoke-test: 30/30 clean, 0 quarantines.** Every new sub-corpus parses through `dcml_parser.py` with 100%
  root-pc computation and all required columns present. No format/version drift breaks the parser.
- **Tristan = YES.** `wagner_overtures` = 2 pieces: Tristan Prelude (WWV090) + Meistersinger Prelude (WWV096).
- **The free cadence win is bigger than the census thought.** `cadence` + `phraseend` GT columns exist **corpus-wide**
  (not just Mozart) — **9,662 cadence labels across 921 files** — and `dcml_parser.py` **drops all of them**.
- **Registry v2** = a new `tools/score_census_registry.json` (56 sources: 40 DLC + 16 other), schema per census §3
  incl. the `split (dev|held-out)` field.

---

## 1. Task A — registry v2

**Choice (declared):** introduced a **new `tools/score_census_registry.json`** rather than overloading the existing
files. Rationale: `tools/corpus_registry.json` is an append-only **validation-run log** (per-run records) and
`tools/extra_scores_registry.json` is a per-**score** list; neither carries a per-**source** census schema. The new
file is generated deterministically by **`tools/build_score_census_registry.py`** (DLC rows read live from the clones —
sha via `git rev-parse`, counts via glob, `harmony_version` + cadence/phrase layer counts from the TSVs — so it never
drifts from disk; non-DLC rows hand-encoded from the census appendices with shas read live).

**Schema (per source):** `name, container, content, pieces, annotated_pieces, gt_type (rn|chords|key|cadence|phrase|
none), gt_layers, layer_label_counts, annotation_standard, score_format, alignment (score-aligned|chords-only|none),
license_class (PD|CC0|CC-BY|CC-BY-NC|unclear), distribution (committable|hash-pin-only), tier (G|J|C|S|X), status
(onboarded|pinned|recorded|rejected), split (dev|held-out), provenance_url, pinned_commit, notes`.

**Rows: 56 total** — 40 DLC members (`distant_listening_corpus.members`) + 16 `other_sources` (When-in-Rome, DCML
`bach_chorales` scores-only, the music21 gate corpus, and the research-tier jazz/pop + no-GT validation corpora:
ChoCo, Nottingham, McGill-Billboard, iRb, JHT, Hooktheory HLSD, POP909, Chordonomicon, lda_tpcs, Omnibook, Effendi,
Rampageswing, PDMX).

**`split` assignment** (per the CC dispatch revalidation note): dev = **16** {the 10 pre-wave-1 DLC members} ∪
{beethoven_piano_sonatas, wagner_overtures, liszt_pelerinage, rachmaninoff_piano, schulhoff_suite_dansante_en_jazz,
monteverdi_madrigals}; **held-out = 24** (all other newly onboarded members). Held-out is never tuned against;
demotion to dev only by explicit recorded decision.

---

## 2. Task B — onboarding (30 sub-corpora)

All cloned `--depth 1` into `tools/dcml/`; pinned to clone-time HEAD (shas in the registry + REPRODUCIBILITY.md).
**All layouts uniform** (`MS3/` `.mscx` + `harmonies/` `.harmonies.tsv`). **0 parse quarantines.**

### Batch 1 — chromatic/romantic (13)

| sub-corpus | pinned sha | mvts | annot | harmony_version | parse | cadence labels |
|---|---|---:|---:|---|---|---:|
| beethoven_piano_sonatas | ea7181bf | 91 | 64 | 2.3.0 (27 unstamped) | OK | 1370 |
| wagner_overtures | fe316b6c | 2 | 2 | 2.1.0 | OK | 0 |
| liszt_pelerinage | f1cfd308 | 19 | 19 | 2.1.1/2.3.0 | OK | 272 |
| rachmaninoff_piano | a73f3246 | 22 | 22 | 2.3.0 | OK | 49 |
| medtner_tales | 1d2e58ba | 19 | 19 | 2.3.0 | OK | 233 |
| ravel_piano | 5a97ccee | 5 | 3 | 2.1.0 (2 unstamped) | OK | 0 |
| schubert_winterreise | da2e281e | 24 | 24 | 2.1.0 | OK | 0 |
| schumann_liederkreis | 226b7885 | 12 | 12 | 2.1.0 | OK | 0 |
| mahler_kindertotenlieder | 9122b6d3 | 5 | 5 | 2.3.0 | OK | 30 |
| c_schumann_lieder | 9ed92555 | 12 | 12 | 2.3.0 | OK | 64 |
| debussy_suite_bergamasque | 322ece59 | 4 | 4 | 2.3.0 | OK | 29 |
| mendelssohn_quartets | b92a90c5 | 24 | 24 | 2.1.0 | OK | 0 |
| poulenc_mouvements_perpetuels | 7793981b | 3 | 3 | 2.3.0 | OK | 6 |

### Batch 2 — pre-Baroque / Baroque-adjacent (15)

| sub-corpus | pinned sha | mvts | annot | harmony_version | parse | cadence labels |
|---|---|---:|---:|---|---|---:|
| monteverdi_madrigals | 6e1adc73 | 19 | 19 | 2.1.0 | OK | 0 |
| sweelinck_keyboard | 0c2a4f5b | 1 | 1 | 2.1.0 | OK | 0 |
| peri_euridice | f02fc664 | 6 | 6 | 2.3.0 | OK | 342 |
| frescobaldi_fiori_musicali | e17de917 | 47 | 48 | unstamped | OK | 0 |
| scarlatti_sonatas | 7750a608 | 69 | 69 | 2.3.0 | OK | 809 |
| couperin_clavecin | 3bd00fc5 | 9 | 9 | 2.3.0 | OK | 57 |
| couperin_concerts | 49efcdd2 | 91 | 84 | 2.3.0 | OK | 744 |
| kleine_geistliche_konzerte | b3cc43d4 | 56 | 55 | 2.1.1 | OK | 0 |
| pergolesi_stabat_mater | b24d5432 | 12 | 7 | 2.2.0 (5 unstamped) | OK | 0 |
| handel_keyboard | d3b42765 | 6 | 6 | 2.3.0 | OK | 28 |
| jc_bach_sonatas | ac9fd079 | 29 | 29 | 2.3.0 | OK | 406 |
| wf_bach_sonatas | 379e50dd | 9 | 9 | 2.3.0 | OK | 109 |
| bach_solo | dce67f75 | 68 | 68 | 2.3.0 | OK | 192 |
| kozeluh_sonatas | 23c1983a | 49 | 49 | 2.1.0 | OK | 0 |
| pleyel_quartets | 8b3d7f5e | 6 | 6 | 2.3.0 | OK | 115 |

### Batch 3 — 20th-c. remainder (2)

| sub-corpus | pinned sha | mvts | annot | harmony_version | parse | cadence labels |
|---|---|---:|---:|---|---|---:|
| bartok_bagatelles | c6221f6e | 14 | 14 | 2.3.0 | OK | 35 |
| schulhoff_suite_dansante_en_jazz | e558f2d2 | 6 | 6 | 2.3.0 | OK | 36 |

Batch 4: empty (all 30 covered in batches 1–3; 10 pre-wave-1 members were already present → 40 total).

### Annotation-standard version drift (a finding, not normalized)

`harmony_version` (from each repo's `metadata.tsv`) spans **1.0.0 → 2.3.0** across the family: `1.0.0` (ABC only),
`2.1.0`, `2.1.1`, `2.2.0`, `2.3.0` (the majority). Some repos leave it **unstamped** (empty) for some/all movements
(e.g. `mozart_piano_sonatas`, `frescobaldi`, and 27 `beethoven_piano_sonatas` movements) — this is a metadata-stamping
gap, **not** missing annotations (those TSVs still parse 100%). `ms3_version` is 2.5.2–2.6.0. **The drift is
parse-transparent** for the read surface `dcml_parser.py` uses (numeral/chord/keys/onset columns are stable across
versions) — recorded, not silently normalized.

### Baseline measurements (Task B step 4)

Descriptive research-tier baselines (no target, no tuning, no gate), **DEFAULT config** (the user-run configuration),
via `tools/run_dlc_baseline.py` (the ONE generic driver replacing 30 copied scripts — declared choice). `root_agree`
+ `rn_agree` from `compare_rn.score_corpus`; grid = `--granularity-robust`. Outputs → gitignored
`tools/corpus_dlc_wave1/`.

| sub-corpus | run | ok/fail | root_agree | rn_agree | grid_root | grid_rn |
|---|---:|---:|---|---|---|---|
| bach_solo | 68 | 68/0 | 49.79% (1667/3348) | 26.19% (877/3348) | 34.61% | 17.39% |
| bartok_bagatelles | 14 | 14/0 | 46.23% (417/902) | 8.2% (74/902) | 37.89% | 6.03% |
| beethoven_piano_sonatas | 91 | 91/0 | 61.17% (9211/15057) | 36.73% (5530/15057) | 54.97% | 32.0% |
| c_schumann_lieder | 12 | 12/0 | 70.14% (465/663) | 46.3% (307/663) | 59.45% | 37.2% |
| couperin_clavecin | 9 | 9/0 | n/a (0-region) | n/a | - | - |
| couperin_concerts | 91 | 91/0 | 67.62% (2756/4076) | 43.01% (1753/4076) | 54.45% | 33.87% |
| debussy_suite_bergamasque | 4 | 4/0 | 57.48% (392/682) | 25.66% (175/682) | 50.37% | 22.19% |
| frescobaldi_fiori_musicali | 47 | 43/4 | 69.93% (3568/5102) | 24.36% (1243/5102) | 70.87% | 26.11% |
| handel_keyboard | 6 | 6/0 | 60.0% (51/85) | 51.76% (44/85) | 43.46% | 36.24% |
| jc_bach_sonatas | 29 | 29/0 | 64.81% (1974/3046) | 45.11% (1374/3046) | 53.5% | 36.65% |
| kleine_geistliche_konzerte | 56 | 56/0 | 84.91% (10083/11875) | 29.96% (3558/11875) | 83.14% | 28.38% |
| kozeluh_sonatas | 49 | 49/0 | 66.43% (5468/8231) | 43.64% (3592/8231) | 54.15% | 35.03% |
| liszt_pelerinage | 19 | 19/0 | 50.06% (2078/4151) | 22.77% (945/4151) | 45.54% | 20.51% |
| mahler_kindertotenlieder | 5 | 5/0 | 50.44% (519/1029) | 20.99% (216/1029) | 51.51% | 20.96% |
| medtner_tales | 19 | 19/0 | 55.43% (1479/2668) | 23.35% (623/2668) | 42.02% | 16.66% |
| mendelssohn_quartets | 24 | 24/0 | 62.83% (6051/9630) | 33.09% (3187/9630) | 55.49% | 27.65% |
| monteverdi_madrigals | 19 | 19/0 | 80.99% (2722/3361) | 41.0% (1378/3361) | 77.64% | 36.36% |
| pergolesi_stabat_mater | 12 | 12/0 | 74.85% (381/509) | 54.03% (275/509) | 55.58% | 39.73% |
| peri_euridice | 6 | 6/0 | 57.8% (2339/4047) | 25.6% (1036/4047) | 59.46% | 27.06% |
| pleyel_quartets | 6 | 6/0 | 66.31% (874/1318) | 44.61% (588/1318) | 62.32% | 41.72% |
| poulenc_mouvements_perpetuels | 3 | 3/0 | 48.12% (64/133) | 31.58% (42/133) | 33.12% | 21.56% |
| rachmaninoff_piano | 22 | 22/0 | 58.73% (370/630) | 33.02% (208/630) | 44.17% | 24.49% |
| ravel_piano | 5 | 4/1 | 56.59% (219/387) | 20.16% (78/387) | 49.78% | 16.52% |
| scarlatti_sonatas | 69 | 69/0 | n/a (0-region) | n/a | - | - |
| schubert_winterreise | 24 | 24/0 | 69.46% (1212/1745) | 46.19% (806/1745) | 60.46% | 39.58% |
| schulhoff_suite_dansante_en_jazz | 6 | 6/0 | 54.34% (288/530) | 11.13% (59/530) | 44.42% | 9.51% |
| schumann_liederkreis | 12 | 12/0 | 66.0% (398/603) | 46.93% (283/603) | 59.39% | 42.33% |
| sweelinck_keyboard | 1 | 1/0 | 81.09% (343/423) | 26.95% (114/423) | 74.59% | 24.39% |
| wagner_overtures | 2 | 2/0 | 60.62% (314/518) | 27.8% (144/518) | 44.3% | 17.79% |
| wf_bach_sonatas | 9 | 9/0 | 56.62% (453/800) | 33.88% (271/800) | 43.63% | 26.12% |

*root_agree = root-pc agreement over root-aligned regions; rn_agree = (exact+partial)/matched RN; grid_* =
granularity-robust beat-grid view (duration-weighted). Full numbers in `tools/corpus_dlc_wave1/results.json`.*

Notes on the baseline: (a) these run on **dev AND held-out alike** (measurement ≠ tuning; the held-out restriction
binds fixes/calibration, not descriptive baselines — per the dispatch note). (b) **"n/a" = 0 analyzable regions**, not
a failure: sparse keyboard textures (harpsichord dances, single-line galant) fall below the analyzer's 3-pitch-class
region threshold — the same 0-region phenomenon documented for `cpe_bach_keyboard`/`bach_en_fr_suites` dances. This is
an **inference/coverage observation surfaced to Cowork**, not a fix (per the no-inference-driven-coding rule).

---

## 3. Task B — Tristan answer

**YES.** `wagner_overtures` contains **2 pieces**, both harmony-annotated:
- `WWV090_Tristan_01_Vorspiel-Prelude_Ricordi1888Floridia.mscx` — **the Tristan Prelude** (the review's stress want).
- `WWV096-Meistersinger_01_Vorspiel-Prelude_SchottKleinmichel.mscx` — Meistersinger Prelude.

Both carry `harmony_version` 2.1.0 (1,433 harmony regions total). Cadence layer is empty for both; phrase layer sparse
(13 phraseend markers).

---

## 4. Task C — the free cadence win (read-only inventory)

**Which files/columns.** Every DCML `harmonies/*.harmonies.tsv` (the same files the RN pipeline already reads) carries
three GT columns beyond the RN: **`cadence`**, **`phraseend`**, and **`form`**. Correction: **`form` is chord-FORM**
(`o`/`%`/`M`/`+` = dim/half-dim/major/aug), a harmony sub-field — **not** a formal-structure/phrase layer; it is
excluded from the cadence/phrase accounting.

**Label vocabulary (`cadence` column, across all 40 DLC sub-corpora — 9,662 labels in 921 of 1,284 files):**

| label | count | meaning |
|---|---:|---|
| PAC | 4667 | perfect authentic cadence |
| HC | 2614 | half cadence |
| IAC | 1616 | imperfect authentic cadence |
| EC | 279 | evaded cadence |
| DC | 195 | deceptive cadence |
| PC | 86 | plagal cadence |
| HC.SIM / HC.CON / HC.PHR / HC.TEN | 113 / 40 / 37 / 15 | HC sub-types (simple/contrapuntal/phrygian/tenor) |

This matches the DCML cadence standard (PAC/IAC/HC/EC/DC/PC + HC sub-types). **`phraseend`** carries phrase-boundary
brackets (`{`, `}`, `\\`, `}{`; 24,436 markers) — a phrase-segmentation layer.

**Per-corpus counts** are in `tools/score_census_registry.json` (`layer_label_counts`) and §2 tables above. Richest
cadence beds: `beethoven_piano_sonatas` (1370), `mozart_piano_sonatas` (1115, pre-wave-1), `corelli` (1061,
pre-wave-1), `couperin_concerts` (744), `scarlatti_sonatas` (809), `cpe_bach_keyboard` (796, pre-wave-1). 12 sub-corpora
have the column but **0 cadence labels** (annotators didn't label cadences there): ABC, frescobaldi, kleine_geistliche,
kozeluh, mendelssohn, monteverdi, pergolesi, ravel, schubert_winterreise, schumann_liederkreis, sweelinck, wagner.

**Does `dcml_parser.py` read or drop them? → DROPS all three.** `parse_abc_harmonies_file` reads only `mn`/`mc`,
`mn_onset`, `globalkey`, `localkey`, `relativeroot`, `chord`, `numeral`, `quarterbeats*`. `cadence`/`phraseend`/`form`
are never referenced — the cadence/phrase GT is present on disk and silently unused. **Zero acquisition cost to light
it up.**

### One-page proposal sketch (NOT an implementation)

*Goal:* ground the L5 §5.2 cadence detector's **validation measure** (and inform L4 rotation-pinning) with the
already-owned DCML cadence GT.

1. **Parser extension (small, additive):** add an optional `cadence` (+ `phraseend`) field to `DcmlRegion`, populated
   in `parse_abc_harmonies_file` from the existing columns. Purely additive — no change to the RN read surface, so the
   BIR gate stays byte-identical.
2. **A cadence-comparison harness** (analogue of `compare_rn.py`): align our detected cadence points to GT cadence rows
   by tick (reuse the existing tick-overlap matcher), classify our cadence label vs GT (PAC/HC/IAC/…), and report
   precision/recall per cadence type per corpus. Descriptive only — a **validation bed**, not a gate.
3. **Evaluation policy:** cadence detection is a **span/point** task, not a per-region one; report boundary-tolerant
   precision/recall (± a beat) plus a confusion matrix over the 6+4 cadence types. Start on the richest dev beds
   (beethoven/mozart/corelli/cpe_bach), hold the held-out ones back.
4. **L4 tie-in:** at a GT PAC/HC, the cadential 6-4 → V → I rotation is pinned by cadence context — a candidate signal
   for the Layer-4 rotation-pinning job named in CLAUDE.md's two-tier-gate prose (the symmetric-rotation churn fix).
   Flagged as an inference/architecture opportunity for Cowork; **not built here.**

Scope note: this is the DCML cadence layer only. The algomus (Bach WTC / Mozart SQ) and Sears (Haydn) cadence sets
(census §5) remain separate Tier-C acquisitions.

---

## 5. Census corrections ([reported] rows verified/corrected at source)

1. **DLC submodule count: 41 → 40.** Verified from `distant_listening_corpus/.gitmodules` (live) + the GT-draft §1a
   table (40 named rows). The "41" in `cowork_score_census.md` §1/§2 and the GT draft prose is an overcount by one.
2. **"Project uses 11 of 41" → uses 10 DLC submodules** (+ the standalone `bach_chorales`, which the census §1b itself
   flags as **not** a DLC submodule). The 10: ABC, bach_en_fr_suites, chopin_mazurkas, corelli, cpe_bach_keyboard,
   dvorak_silhouettes, grieg_lyric_pieces, mozart_piano_sonatas, schumann_kinderszenen, tchaikovsky_seasons.
3. **License [reported]→verified per-repo:** only **12 of 40** DLC repos carry an explicit CC BY-NC-SA 4.0 `LICENSE`
   (ABC, beethoven_piano_sonatas, chopin_mazurkas, corelli, debussy_suite_bergamasque, dvorak_silhouettes,
   grieg_lyric_pieces, liszt_pelerinage, medtner_tales, mozart_piano_sonatas, schumann_kinderszenen,
   tchaikovsky_seasons). The **other 28 have no in-repo LICENSE** (org-level CC BY-NC-SA is [reported] only) →
   `license_class: unclear`. All 40 are hash-pin-only/gitignored, so this raises **no distribution risk**.
4. **Piece counts (census "?" cells closed)** — see §2 tables (mvts + annotated). Notable: beethoven_piano_sonatas
   91 mvts / 64 annotated; couperin_concerts 91/84; scarlatti_sonatas 69/69; bach_solo 68/68; kozeluh 49/49;
   kleine_geistliche_konzerte 56/55; sweelinck_keyboard just 1 movement; wagner_overtures 2.
5. **`schubert_winterreise` (DCML) has 24 scores but 48 harmonies TSVs** — two annotation TSVs per song (a variant/
   dual layer). Recorded (not resolved) — worth a look if it is used as GT.
6. **`form` column semantics** clarified (chord-form, not formal structure) — see §4.

---

## 6. Quarantines + Unknowns

- **Quarantines: NONE.** All 30 sub-corpora parsed cleanly (0 files failed, all required columns present).
- **Unknown — sparse-texture 0-region corpora (confirmed):** **`couperin_clavecin` (9 mvts) and `scarlatti_sonatas`
  (69 mvts)** produce **0 analyzable regions** across all movements → no root/rn baseline (`n/a` in the table), even
  though batch_analyze ran without error. Both are harpsichord textures largely at ≤2 simultaneous pitch classes,
  falling below the analyzer's 3-PC region threshold — the same 0-region phenomenon documented for `cpe_bach_keyboard`
  and `bach_en_fr_suites` dances. `scarlatti_sonatas` (69 mvts, 12,286 GT regions on disk) losing its entire baseline
  this way is a notable coverage gap. Surfaced to Cowork as an **inference/coverage matter**, not fixed here.
- **Analyze failures (2 corpora):** `frescobaldi_fiori_musicali` 4/47 movements and `ravel_piano` 1/5 failed
  batch_analyze (non-zero exit or no output within the 90 s per-movement timeout) — excluded from that corpus's
  denominator; recorded, not investigated (research-tier).
- **`wagner_overtures`:** both orchestral preludes analyzed fine within timeout (10.1 s total); root_agree 60.6%,
  rn_agree 27.8% (heavy chromaticism — as expected, low).
- **Unknown — dual-annotation `schubert_winterreise`** (48 TSV / 24 scores): which TSV is canonical is not resolved
  (baseline used the default `<stem>.harmonies.tsv` match; root_agree 69.5%).
- **Not re-verified:** the non-DLC census rows (ChoCo/HookTheory/CoCoPops piece counts etc.) carry their census
  [reported] tags forward in the registry; verifying those is a later Tier-J/C acquisition, not this wave.

---

## 7. Commits + gate no-contamination proof

**Gate no-contamination proof (run at report time, HEAD `5f7cb7376e` + this wave's uncommitted changes):**
`characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}` →
**Baroque 53 / Jazz 24 / Default 53** (each "Processed 352 scores (326 with WiR coverage)"). **Unchanged** from the
CLAUDE.md baseline. This wave touched no `src/`, no `chordanalyzer.cpp`, and no gate corpus dir — the new material is
entirely under gitignored `tools/dcml/` (clones) and `tools/corpus_dlc_wave1/` (regenerable outputs).

**Commits (local, unpushed, fork-only):**
- Task A: `tools/score_census_registry.json` + `tools/build_score_census_registry.py` + doc updates
  (`REPRODUCIBILITY.md`, `score_inventory.md`).
- Driver: `tools/run_dlc_baseline.py`.
- Nothing under `src/`; the frozen Bach gate corpus (`tools/corpus/`, `tools/dcml/bach_chorales`, `tools/dcml/when_in_rome`)
  byte-untouched.

**⚠ `docs/score_inventory.md` deferred from commit:** the file carried a **pre-existing uncommitted Cowork edit**
(the `## The idiom-discovery corpora — corpora/` section) at session start. My DLC-wave-1 subsection is written into the
working tree, but I did **not** commit `score_inventory.md` to avoid bundling Cowork's uncommitted work into my commit
(git add is whole-file). It is staged-in-working-tree only; commit it once the idiom-discovery section is separately
committed, or on Cowork's say-so. The equivalent provenance is committed via `REPRODUCIBILITY.md` + the registry.

**This report** (`cc_corpus_wave1_report.md`) is **HELD** (gitignored; not committed until an approval file says so).

Report length: 287 lines.
