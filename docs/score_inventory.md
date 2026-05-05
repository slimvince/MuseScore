# Score & corpus inventory

Last updated: 2026-05-04.

This document is a **usage map**: for any task that needs scores (validation,
snapshot tests, manual QA, LLM-triage, qualitative review), it tells you which
folder to reach for and why. It complements two existing references:

- `tools/REPRODUCIBILITY.md` — *how to recreate* each corpus from public
  sources if `tools/` is wiped. Read that before re-cloning; read this before
  picking a corpus to use.
- `tools/corpus_registry.json` and `tools/extra_scores_registry.json` —
  machine-readable per-run / per-score metadata consumed by `batch_analyze`
  and the `run_*_validation.py` scripts.

If you only have a minute, read the **quick-pick table** below and the
**Hard rules** section at the bottom.

---

## Quick-pick table

| If you want to… | Use | Path | Notes |
|---|---|---|---|
| Run unit tests / mismatch report | In-tree fixtures | `src/composing/tests/data/`, `src/composing/tests/scores/` | Wired into `composing_tests`. The synthetic catalog drives the mismatch report; **do not edit without explicit approval** (see Hard rules) |
| Run pipeline snapshot tests | `src/composing/tests/scores/` | 8 real-music scores | Snapshot diffs gate refactors. Adding/removing scores changes baselines |
| Validate analyzer against Roman-numeral annotations | DCML annotated corpora | `tools/dcml/<repo>/MS3/` + `harmonies/` | ~1,700 scores total; consumed by `run_*_validation.py` and `compare_when_in_rome.py` |
| Validate jazz analysis (single-line / Real Book) | Effendi, Omnibook | `tools/corpus_effendi_src/`, `tools/corpus_omnibook_src/omnibook_xml/` | No RNA ground truth — comparison is via `compare_omnibook.py` heuristics |
| Validate jazz analysis (big-band / multi-horn) | Rampageswing | `tools/corpus_rampageswing_full/` | 36 MXL scores; no ground truth |
| Random sampling across many genres | PDMX spot-check | `tools/pdmx/spot_check/` | 5 MXL files sampled from PDMX/Zenodo |
| Qualitative review / "does this sound right" | `tools/extra scores/` | 163 user-curated `.mscz` files | No ground truth. **Quote the path** — has a space |
| LLM-triage corpus (Mode 2 quality work) | `tools/extra scores/hiromi/` | 20 Hiromi Uehara scores | Designated qualitative-review corpus per memory `reference_hiromi_corpus.md`. **Not** for `pipeline_snapshot_tests` or analyzer ground truth |
| Re-derive analyzer outputs over a corpus | `tools/corpus_*/` working copies | Various `corpus_<name>_v2/`, `corpus_<name>_<timestamp>/` | These hold `.ours.json` outputs only — regenerable; don't treat them as score sources |

---

## In-tree fixtures (wired into `composing_tests`)

These are the **only** scores actually exercised by the C++ test binary.

### `src/composing/tests/data/`

- `chordanalyzer_catalog.musicxml` — the synthetic C-major catalog that drives
  the mismatch report read after every test run. Every chord shape we claim
  to recognize has at least one entry. Per memory
  `project_composing_tests_baseline_synthetic.md`, **the entire 135-mismatch
  baseline came from this single file**, so the on-disk numbers reflect
  catalog choices, not real-music quality. Currently pinned at 4 RealDiff
  mismatches.
- `chordanalyzer_context.musicxml` — context fixtures used by analyzer unit
  tests.
- `chord_analysis_test.musicxml`, `mono_smoke_test.musicxml`,
  `solid theory.musicxml` — small targeted fixtures.
- `francis-poulenc-o-magnum-mysterium.mxl`,
  `organ-sonata-n1-in-e-flat-major-bwv-525-i-allegro.mxl` — real-music
  smoke fixtures consumed by the data-side tests.

### `src/composing/tests/scores/`

The **pipeline snapshot suite**. Eight real-music scores whose analyzer
output is checkpointed into `pipeline_snapshot_tests`. Refactors must produce
byte-identical snapshots or the diff is investigated.

- `clair-de-lune-claude-debussy.mxl`
- `jesu-meine-freude-bwv-227-johann-sebastian-bach.mxl`
- `like-someone-in-love-bill-evans.mxl`
- `piston examples.musicxml`
- `slask Tillägnan SMzATB.mxl`
- `slask you must believe in spring SMATB.mxl`
- `xxxxx.mxl`

**These eight gate refactors.** Adding or removing a score changes the
snapshot baseline — coordinate with the unified-pipeline reviewer before
touching them.

---

## DCML annotated corpora — `tools/dcml/<repo>/`

Twelve sub-repositories cloned from `github.com/DCMLab` and from
`MarkGotham/When-in-Rome`. Each has a `MS3/` folder of `.mscx` scores and a
`harmonies/` folder of TSV annotations in DCML/Roman-numeral syntax. The
validation runners pair them up.

| Sub-repo | Scores | Style | Validation script |
|---|---:|---|---|
| `bach_chorales/` | 361 | SATB chorales | `run_bach_preset.py`, `run_validation.py` |
| `corelli/` | 149 | Baroque trio sonatas | `run_corelli_validation.py` |
| `bach_en_fr_suites/` | 89 | Keyboard suites | (no dedicated runner — use `run_validation.py`) |
| `ABC/` | 71 | Beethoven string quartets | `run_beethoven_validation.py` |
| `cpe_bach_keyboard/` | 66 | Galant keyboard | `run_cpe_bach_validation.py` |
| `grieg_lyric_pieces/` | 66 | Late-romantic piano | `run_grieg_validation.py` |
| `mozart_piano_sonatas/` | 58 | Classical piano | `run_mozart_validation.py` |
| `chopin_mazurkas/` | 56 | Romantic piano | `run_chopin_validation.py` |
| `schumann_kinderszenen/` | 13 | Romantic piano | `run_schumann_validation.py` |
| `dvorak_silhouettes/` | 12 | Late-romantic piano | `run_dvorak_validation.py` |
| `tchaikovsky_seasons/` | 12 | Romantic piano | `run_tchaikovsky_validation.py` |
| `when_in_rome/` | 762 | Mixed (When-in-Rome anthology) | `compare_when_in_rome.py` |

**Total ~1,715 scores with RNA ground truth.**

**when_in_rome path quirk:** scores are stored as `Corpus/<style>/<composer>/<piece>/<number>/score.mxl` — every file is named `score.mxl`. Any tool that writes output keyed by basename must use per-score subdirectories to avoid collisions (the llm-triage batch runner does this under `outputs/when_in_rome/<relative-path>/`). This is the load-bearing
validation set for *root agreement* and *quality* metrics whenever a
classical-or-romantic-period change is being evaluated.

When a runner produces output, it lands in a timestamped
`tools/corpus_<name>_<timestamp>/` or `tools/corpus_<name>_v2/` directory as
`.ours.json` files paired with the source scores. Those output trees are
regenerable — see `tools/REPRODUCIBILITY.md`.

---

## Jazz / non-classical corpora

### `tools/corpus_effendi_src/` — Effendi Real Book (368 files)

Lead-sheet-style MusicXML. Typically a single horn line + chord symbols.
Filtered by `filter_effendi.py` to scores with usable harmony tags. Use
`compare_analyses.py` for ad-hoc comparison; there is no RNA ground truth.
**Useful for:** sanity-checking the chord-symbol-comparison path, exposing
extension-handling edge cases.

### `tools/corpus_omnibook_src/omnibook_xml/` — Charlie Parker Omnibook (50 files)

Single-line bebop transcriptions. Driven by `compare_omnibook.py`.
**Useful for:** regression-testing monophonic jazz analysis (Phase 1a). Per
ARCHITECTURE.md, the open corpus-availability gap is for *fully voiced* jazz
scores — Omnibook doesn't fill that gap.

**Path quirk:** the XML files are one level deeper than the directory name
suggests — they live in `omnibook_xml/Omnibook xml/` (note the space). Any
script that globs `omnibook_xml/*.xml` finds nothing; use
`omnibook_xml/Omnibook xml/*.xml` or `rglob` with `__MACOSX` filtered out.

### `tools/corpus_rampageswing_full/` — Big-band charts (36 MXL files)

Multi-horn arrangements crawled from rampageswing.com. The exact crawl
script wasn't preserved (see `REPRODUCIBILITY.md`).
**Useful for:** stress-testing the analyzer on dense vertical harmony with
horns in multiple keys.

### `tools/pdmx/spot_check/` — PDMX random sample (5 MXL files)

A handful of randomly sampled scores from the PDMX dataset
(`Zenodo: 10.5281/zenodo.15571083`). Filename hashes in the form
`Qm…mxl` come from the IPFS-style content addressing PDMX uses.
**Useful for:** smoke-testing across genres without committing to a full
PDMX run; full PDMX is ~217 GB and not stored locally.

### `tools/corpus/` — music21 Bach chorale exports (353 XML + JSON)

Legacy Bach chorale corpus exported from `music21`. Each `bwvNNN.N.xml`
score is paired with a `.music21.json` analysis. Likely overlaps with
`dcml/bach_chorales/MS3/` (different export of largely the same repertoire).
**Useful for:** music21-vs-ours comparisons via `compare_analyses.py` and
`inject_m21_rn.py`. Don't treat as additional scores when totaling.

---

## Curated extra scores — `tools/extra scores/`

163 `.mscz` files, manually downloaded by Vincent for qualitative work.
**No ground-truth annotations.** Documented in
`tools/extra_scores_registry.json` (path, title, composer, preset, style,
`ground_truth: false`, occasional notes about thin/partial transcriptions).
The path **contains a space** — always quote it in shell commands:
`"tools/extra scores"` or `'tools/extra scores'`.

Top-level mix: jazz piano transcriptions (Bill Evans, Keith Jarrett, Brad
Mehldau, Herbie Hancock, Wayne Shorter, Chick Corea, Michel Petrucciani,
Oscar Peterson), modern fusion / jazz-pop (Snarky Puppy, Dirty Loops,
Jacob Collier), Pentatonix a-cappella arrangements, jazz-band charts, and
some Tom Jobim / Antonio Carlos Jobim / bossa nova.

### Sub-folders

- **`hiromi/`** (20 scores) — Hiromi Uehara solo piano transcriptions. The
  designated qualitative-review corpus per memory
  `reference_hiromi_corpus.md`. **Always quote the path** because of the
  space in `extra scores`. Use this for: manual QA loops, LLM-triage
  workflows. **Do NOT use for** `pipeline_snapshot_tests` (it would change
  baselines without RNA ground truth) or analyzer accuracy claims (no labels).
- **`Steely dan/`** (23 scores) — Steely Dan / Donald Fagen transcriptions.
  Useful for: extension-heavy reharm tests.
- **`piazzolla/`** (6 scores) — Astor Piazzolla tango. Useful for: minor-key
  / chromatic-counterpoint stress.

### When to use `extra scores/`

- You want a "does this sound right" pass on real music outside the
  classical canon.
- You're feeding the LLM-triage workflow (per `docs/llm_triage_design.md`).
- You're building a private smoke test for a specific style.

### When NOT to use `extra scores/`

- Anything that requires ground-truth comparison — there is none.
- Snapshot/regression tests — use `src/composing/tests/scores/` instead.
- Headline accuracy numbers — `tools/dcml/` is the validation source of
  truth for those.

---

## Output / working directories (no scores live here)

These contain only `.ours.json` analyzer outputs, not source scores. They
can be safely deleted and regenerated. Naming patterns:

- `tools/corpus_<name>_v2/` — current "good" output run for a given corpus
- `tools/corpus_<name>_<YYYYMMDD_HHMMSS>/` — historical runs
- `tools/reports/` — JSON / HTML reports (~1 GB)
- `tools/refresh_divergence_*/`, `tools/bach_path3fix_*/`,
  `tools/validation_bach_postport/` — experimental / one-off snapshots
- `tools/tools/` — superseded earlier output tree from `music21_batch.py`

If you see a `corpus_*` directory in `tools/` and it's empty or contains
only `.json`, it's a working/output dir, not a score source. Cross-check
against the table in `REPRODUCIBILITY.md` ("`tools/corpus_*/` (working
copies)") for the source-corpus pairing.

---

## Out-of-tree references

Memory holds a few corpus-relevant notes — check them when in doubt:

- `reference_hiromi_corpus.md` — Hiromi corpus location and intended use
- `project_composing_tests_baseline_synthetic.md` — why the 4 mismatches
  are not a real-music quality measure
- `feedback_cadence_test_fixtures.md` — small synthetic fixtures don't
  clear the 0.8 confidence gate; use Corelli-scale fixtures for cadence
  smokes

ARCHITECTURE.md cites a few **benchmark passages** for manual visual
inspection — see the table around line 279 (e.g. "Bach BWV 227.7 bars 1-2,
8-10, final cadence" → `tools/corpus/bwv227.7.xml`). Use those when a
corpus number moves and you want a 2-minute eyeball check.

---

## Hard rules

1. **Do NOT modify `chordanalyzer_catalog.musicxml`** without explicit
   approval. CLAUDE.md flags it as ground-truth; per memory, all current
   composing_tests mismatches trace to this one file.
2. **Do NOT add or remove files in `src/composing/tests/scores/`** without
   coordinating — the eight scores there are the snapshot baseline.
3. **Quote `"tools/extra scores"` and `"tools/extra scores/hiromi"`** in
   every shell command. Path has a space; unquoted commands fail silently
   on subset matches.
4. **Don't conflate `tools/corpus/` with `tools/dcml/bach_chorales/`** —
   they overlap but aren't byte-identical (different export pipelines).
5. **Use DCML for headline numbers, `extra scores/` for taste.** The
   only RNA-annotated corpus we have is DCML; everything in `extra scores/`
   is `ground_truth: false`.
6. **`pipeline_snapshot_tests` baseline is the snapshot suite, not the
   catalog mismatches.** Don't conflate the two test suites when reporting
   results — the synthetic catalog produces the mismatch report; the eight
   real-music scores produce the snapshot diffs.

---

## Why this wasn't documented before

For the record, in case CC re-asks. The inventory drifted into three
incompatible forms over time:

- `tools/REPRODUCIBILITY.md` — written first, focused on *recreation if
  `tools/` is wiped*. Doesn't mention `extra scores/`, in-tree fixtures, or
  use-case pairing.
- `tools/corpus_registry.json` + `tools/extra_scores_registry.json` —
  machine-readable, consumed by `batch_analyze` and the run scripts. Dense
  JSON; nothing summarizes it for a human reader.
- ARCHITECTURE.md — references corpora in scattered prose, including a
  benchmark-passages table around line 279, but never as a complete index.

CLAUDE.md gave CC build/test paths only; nothing pointed at the corpora.
This file is the missing index. CLAUDE.md now links here so future sessions
find it before starting any score-related work.
