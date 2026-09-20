# CC — the TSV-oracle infrastructure: cadence + phraseend parsing + the L6 validation metrics

> **Status: HELD for Cowork** (gitignored; `git add` OK, commit of THIS file NOT until an approval file says so).
> Executes `cc_instruction_tsv_oracle_infrastructure.md` (the L6 §15-1 build prerequisite). HEAD at dispatch:
> `30b23d9f5c`. Gate baseline **53/24/53** — this run changed **no `src/`** and **no gate corpus**; proof in §1.4.
> Three fork-only commits (one more than the two Python ones — the user ratified the third, a C++ tool dump, mid-run):
> `add9499002` (parser) · `16404edef9` (batch_analyze boundary dump) · `9a42714f45` (metrics module).

---

## 0. Headline

- **Task 1 done, additive & gate-safe.** `dcml_parser` now reads the DCML `cadence`/`phraseend` GT columns; the
  RN/root/key read surface is byte-untouched (BIR gate **53/24/53** exact on all three presets).
- **One carry-contract surprise, surfaced and resolved.** The instruction assumed OUR L1.5 boundary ticks were
  readable "via the existing diagnostic dump path" — **no such dump existed** (verified exhaustively). Surfaced as a
  STOP; the user chose **Option A** (add a gate-safe `phraseBoundaryTicks` array to `--dump-fullspine`, a tool change,
  standard `.ours.json` byte-identical). Built.
- **A material parser-design finding.** **10.7%** of `phraseend` markers (and 1.1% of `cadence` markers) sit on
  **rest rows** the RN region stream skips — so a dedicated `parse_cadence_phrase_markers()` (reads every row) is
  required for a complete GT tick set. Built + tested.
- **Both metrics built and measured (dev beds, read-only).** Punctuation-span-boundary **P=34.8% / R=22.4%**;
  cadence-location **P=35.9% / R=1.6%** — the honest baseline of the **EXISTING dormant detectors** (no constant
  moved). The low cadence recall is a substrate property: the dormant L5 detector fires **295** cadences against
  **6,463** GT labels on this repertoire (and **0** on cpe_bach — 0 committed units).

---

## 1. Task 1 — parser extension (commit `add9499002`)

### 1.1 What changed (additive only)

- **`DcmlRegion`** gains two optional fields `cadence: Optional[str] = None`, `phraseend: Optional[str] = None`,
  populated in **`parse_abc_harmonies_file`** (the harmonies-TSV read path) from `row.get('cadence')` /
  `row.get('phraseend')` (stripped; `None` when empty). `form` stays unread (chord-FORM, excluded per Wave-1 §4).
  The other two constructors (`parse_dcml_file`, `parse_rntxt_file`) are unchanged — the dataclass defaults keep them
  valid.
- **`parse_cadence_phrase_markers(path)`** — a new reader returning `(cadence_markers, phraseend_markers)` as
  `DcmlMarker(abs_tick, label, measure_number, beat, kind)`, scanning **every** row (numeral-independent). Tick
  derivation reuses the exact RN-path arithmetic (`round(Fraction(<quarterbeats col>) * 480)`, all-endings/plain
  fallback), so marker ticks and region ticks share one basis.

### 1.2 Why the dedicated reader is necessary (finding)

A `cadence`/`phraseend` cell can sit on a **rest row** (numeral `.`/`~`/`@none`/empty) that the RN region stream
`continue`s past. Measured across the 16 dev beds:

| marker | total | on rest rows | % on rest rows |
|---|---:|---:|---:|
| `phraseend` | 14,102 | 1,511 | **10.7%** |
| `cadence` | 6,463 | 74 | 1.1% |

Attaching markers only to numeral-bearing regions would silently drop ~11% of GT phrase boundaries — corrupting the
punctuation-span-boundary GT set. The region fields (Task-1 spec) are kept for the future L4 cadence-to-region
tie-in; the **metric** consumes the complete `parse_cadence_phrase_markers()` set. (The `DcmlRegion` docstring records
this so the two are not confused.)

### 1.3 Column vocabulary observed (dev beds) — within the documented set

- `cadence`: `{PAC, IAC, HC, DC, EC, PC}` (no HC sub-types present in the dev-bed `cadence` column, though `HC.SIM`
  etc. exist corpus-wide; the parser carries any sub-type verbatim — the unit test pins `HC.SIM`).
- `phraseend`: `{ '{', '}', '}{', '\\' }` (the backslash bracket is literally two backslash chars — carried
  verbatim, not unescaped). No value outside the documented vocabulary → no `record+skip` STOP fired.

### 1.4 Additivity proof

- **Unit tests:** 4 new (`L6OracleColumnTests`): region-field population (incl. `HC.SIM` + `local_key`/RN untouched);
  the rest-row marker capture (5 phraseend incl. the `\\`@5760 rest-row bracket vs 4 region-carried); and a
  columns-absent fixture parsing **identically** (fields `None`, RN/root byte-for-byte equal on shared rows). All
  green.
- **Full metric suite:** `python -m unittest discover -s tools/tests` → **107 passed** (unchanged).
- **BIR gate:** `characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}` →
  **53 / 24 / 53** exact (each "Processed 352 scores (326 with WiR coverage)"). Byte-identical to CLAUDE.md baseline.
- **C++ suites** (post-build): composing **1015** / notation **53** / snapshots **11/11** — no golden refresh.

---

## 2. Task 2 — the two validation metrics (commits `16404edef9`, `9a42714f45`)

### 2.1 The boundary-source resolution (the STOP → Option A)

Metric 1 needs OUR boundary ticks = the L1.5 `phraseBoundaryTicks` picked set. **No existing dump emitted it** —
verified across `--dump-fullspine` (computes `phraseTicks` internally, emitted nothing), `--dump-cadence-anchor`
(only a per-cadence `endsPhrase` **boolean**, region-granular — too coarse for ±1-beat P/R), `--validate-slices`
(`boundaries` = a change-point slice **count**, not phrase ticks), and `--dump-regions batch/notation` (nothing).
`eb::phraseBoundaryTicks` is a real engraving-model detector (texture peaks + fermata/breath/keysig-change/barline/
ritardando/all-rest markers), not Python-reimplementable.

Surfaced as a carry-contract STOP; **user chose Option A** → **commit `16404edef9`** adds an additive top-level
`"phraseBoundaryTicks": [...]` array to the `--dump-fullspine` JSON (the path already computes the set). `batch_analyze`
is `tools/` (not `src/`); the standard `.ours.json` `writeJson` path is byte-identical, so the gate is unaffected
(re-confirmed 53/24/53). One fullspine run now yields **both** metrics' OUR side.

### 2.2 Module choice + method (commit `9a42714f45`)

- **A new module `tools/compare_l6_oracle.py`** (declared) — *not* overloaded into `compare_rn.py`, whose
  `align_dcml_regions` is a **region-overlap** aligner: the wrong primitive for a point/boundary task. Both metrics
  share **ONE** tolerance point-matcher `match_points()` (never a second one) — greedy 1-1, candidate pairs sorted by
  `(distance, our_tick, gt_tick)`, each tick used once; deterministic.
- **Tolerance = `TOLERANCE_TICKS` = 480** (one quarter-note beat) — a **declared constant, not tuned** (verified
  inclusive at 480, exclusive at 481). Tick basis is `dcml_parser`'s (`quarterbeats*480`) — the same basis OUR ticks
  use; no second tick arithmetic introduced.
- **Metric 1 — boundary P/R:** OUR `phraseBoundaryTicks` vs GT `phraseend` ticks (deduped; `}{` at one tick = one
  boundary). P = matched/|OUR|, R = matched/|GT|.
- **Metric 2 — cadence-location P/R:** OUR `cadences[].arrivalTick` vs GT `cadence`-row ticks, **LOCATION-scoped**
  (design §10). Cadence **type** reported as a `{PAC,IAC,HC,DC,EC,PC}` **confusion matrix over matched pairs only —
  explicitly NOT a gate** (type attribution is harmony-dependent and, as §3.3 shows, poor). OUR fullspine type names
  fold to GT families (`PerfectAuthentic→PAC`, `Half`/`PhrygianHalf→HC`, `Deceptive→DC`, `Plagal→PC`, `Evaded→EC`).
- **Scope:** the **16 dev beds** (registry `split=dev`); held-out untouched (E2). **Zero-cadence corpora auto-skip**
  the cadence metric (data-driven: 0 GT cadence labels) with a printed note — among dev beds that is **ABC, wagner,
  monteverdi** (3).

---

## 3. Task 3 — the first read-only measurement (dev beds)

**Baseline of the EXISTING dormant detectors — no constant moved in response to any number.** `DEFAULT` config,
`--dump-fullspine` per movement, tolerance ±480t.

### 3.1 Per-corpus (boundary + cadence-location)

| corpus | mv | boundary P | boundary R | (m / ours / gt) | cadence P | cadence R | (m / ours / gt) |
|---|--:|--:|--:|---|--:|--:|---|
| ABC | 70 | 15.0% | 31.2% | 301/2004/964 | — | — | *skip (0 GT)* |
| bach_en_fr_suites | 89 | 66.1% | 21.7% | 240/363/1106 | 47.4% | 1.5% | 9/19/584 |
| chopin_mazurkas | 55 | 58.3% | 17.8% | 203/348/1139 | 25.8% | 2.3% | 8/31/344 |
| corelli | 149 | 41.3% | 26.5% | 476/1153/1794 | 19.8% | 1.6% | 17/86/1061 |
| cpe_bach_keyboard | 66 | 56.6% | 18.0% | 317/560/1762 | 0.0% | 0.0% | 0/0/796 |
| dvorak_silhouettes | 12 | 46.8% | 19.5% | 51/109/262 | 42.9% | 2.2% | 3/7/139 |
| grieg_lyric_pieces | 66 | 35.0% | 27.6% | 298/852/1081 | 48.5% | 3.7% | 16/33/433 |
| mozart_piano_sonatas | 54 | 45.4% | 21.3% | 403/887/1893 | 22.2% | 0.4% | 4/18/1115 |
| schumann_kinderszenen | 13 | 65.3% | 27.5% | 47/72/171 | 100.0% | 5.1% | 4/4/79 |
| tchaikovsky_seasons | 12 | 50.8% | 11.1% | 65/128/586 | 83.3% | 2.7% | 5/6/185 |
| beethoven_piano_sonatas | 64 | 33.5% | 20.1% | 470/1404/2339 | 41.1% | 1.7% | 23/56/1370 |
| wagner_overtures | 2 | 4.8% | 7.7% | 1/21/13 | — | — | *skip (0 GT)* |
| liszt_pelerinage | 19 | 20.4% | 36.1% | 175/857/485 | 53.6% | 5.5% | 15/28/272 |
| rachmaninoff_piano | 22 | 38.1% | 33.1% | 43/113/130 | 50.0% | 4.1% | 2/4/49 |
| schulhoff_..._jazz | 6 | 51.4% | 25.0% | 19/37/76 | 0.0% | 0.0% | 0/3/36 |
| monteverdi_madrigals | 19 | 30.3% | 15.3% | 46/152/301 | — | — | *skip (0 GT)* |
| **AGGREGATE** | **717** | **34.8%** | **22.4%** | **3155/9060/14102** | **35.9%** | **1.6%** | **106/295/6463** |

(`mv` = movements scored ok, 0 failures. `chopin` = 55 of 56 mscx — `BI105-1op30-1` has no matching harmonies TSV,
excluded. `boundary gt total 14102` matches the §1.2 phraseend count exactly — every rest-row marker captured,
`dropped_no_tick = 0`.)

### 3.2 Reading the numbers (no action taken — these inform the L6 build, nothing else)

- **Boundary:** the L1.5 detector is **sparse** relative to DCML phrase brackets — it emits ~9,060 boundaries against
  ~14,102 GT (R=22.4%), with precision varying by texture (66% on the sparser bach suites, 15% on the dense
  polyphonic ABC where surface peaks over-fire). Liszt is the one bed where OUR set *exceeds* GT (R=36%, P=20%).
- **Cadence-location:** near-floor recall (**1.6%**) — the dormant L5 detector fires **295** cadences vs 6,463 GT and
  **0** on cpe_bach (0 committed units on that per-slice substrate). Precision where it fires is moderate (35.9%).
  This is the expected substrate property of a Bach-chorale-region-tuned detector run on the per-slice sonata
  substrate — a §4 Unknown surfaced to Cowork, **not** a fix.

### 3.3 Cadence-type confusion (matched pairs only — NOT a gate)

| GT → OUR | count | | GT → OUR | count |
|---|--:|---|---|--:|
| HC → PC | 26 | | IAC → HC | 8 |
| HC → HC | 23 | | IAC → PC | 6 |
| PAC → HC | 21 | | PAC → PAC | 2 |
| PAC → PC | 10 | | DC → HC | 1 |
| PC → PC | 9 | | | |

**Type attribution is poor** — of 106 located matches, only ~34 have the right family (`HC→HC` 23, `PC→PC` 9,
`PAC→PAC` 2); the dominant confusions are `HC→PC` and `PAC→HC`. This is exactly why the instruction scopes the metric
to **location** and marks type a caveated confusion matrix, not a gate.

### 3.4 Top-5 failure exemplars (stem@tick, for the L6-build design record)

**Boundary false-negatives (GT phrase-end, no OUR boundary):**
- corelli: `op01n01a@3840, @9600, @10080, @15360, @15600`
- beethoven: `01-1@13920, @29280, @30720, @33120, @34560`
- mozart: `K279-1@3840, @7680, @22080, @29760, @36480`
- liszt: `160.01_Chapelle_de_Guillaume_Tell@480, @9120, @19200, @23040, @28800`

**Boundary false-positives (OUR boundary, no GT phrase-end):**
- corelli: `op01n01a@26880, op01n01b@53760, @72960, op01n01c@53280, op01n01d@141120`
- mozart: `K279-1@18960, @32640, @72240, @192000, K279-2@29880`

**Cadence-location false-negatives (GT cadence, no OUR detect):**
- corelli: `op01n01a@2880, @9600, @15360, @20160, @24960`
- beethoven: `01-1@14400, @29280, @33120, @36960, @77280`
- mozart: `K279-1@3840, @7680, @18720, @22080, @29040`

**Cadence-location false-positives (OUR cadence, no GT):**
- corelli: `op01n04c@22080, @39360, op01n07c@24480, op01n08b@19200, op01n08c@26880`
- beethoven: `01-1@128160, 01-4@20160, 02-2@113760, 02-4@209280, @258240`

### 3.5 The chorale-fermata secondary view (metric 1 secondary) — documented, §11

The instruction asks the chorale-fermata oracle as a **secondary view** with the §11 non-independence caveat and the
§15-4 `bwv112.5` exclusion. Two facts scope it honestly:

1. **Non-independent by construction (code-verified).** `phraseboundaryview.cpp` §4.2 (lines 448–456) *always* adds
   every fermata/breath/barline/etc. marker tick to `pickedTicks`, regardless of the peak test. So fermata ∈
   `phraseBoundaryTicks` **by construction** → fermata *recall* ≈ 100% trivially. It is a consistency check, **not**
   an independent oracle — the independent one is the `phraseend` primary view (§3.1). The §15-4 rule (`bwv112.5` has
   no fermata → excluded from the fermata-recall denominator) applies to the WiR gate-chorale set.
2. **Quantification is blocked, not done here.** The dev beds are not chorales; the chorale set is `bach_chorales`
   (`.mscx`), and **music21 cannot parse `.mscx`** (`converter.parse` → "cannot find a format extension"). A faithful
   quantified fermata oracle therefore needs either a MuseScore→MusicXML conversion pass or a fermata-only
   `batch_analyze` marker dump — a further tool step **outside** this build's scope (and low value given point 1).
   Recorded as a §4 Unknown; **not** faked with a fragile hand-rolled tick reconstruction.

---

## 4. Unknowns / surfaced-to-Cowork (no fixes — declaration only)

1. **Dormant-detector sparsity is a substrate property, not a metric bug.** The L5 cadence detector was tuned on the
   Bach-chorale **region** substrate; on the per-slice sonata substrate it fires 295/6,463 (R=1.6%), and **0** on
   cpe_bach (0 committed units). The L1.5 boundary detector under-fires vs DCML phrase brackets (R=22.4%). These are
   the honest **baselines of what exists** — surfaced as an inference/architecture matter for the L6 build +
   later calibration, per the no-inference-driven-coding rule.
2. **Cadence type-attribution is weak** (§3.3) — `HC→PC`/`PAC→HC` dominate. A cleaner type oracle (or a type-aware L5
   pass) is the design's stated open item; here it is measured and caveated only.
3. **The fermata secondary view is unquantified** (§3.5) — blocked on `.mscx` fermata extraction; the §11 recall is
   ~100% by code construction. Flagged for a future fermata-tick dump if an independent fermata oracle is wanted.
4. **Granularity.** The boundary/cadence P/R here is at the raw detector-tick level with a ±1-beat tolerance; it is
   **not** the batch/region granularity of the BIR gate and not directly comparable to it (the granularity-robust
   metric is a separate Stage-5 concern per CLAUDE.md).
5. **`chopin BI105-1op30-1`** has an `.mscx` but no `harmonies/*.tsv` (55/56 scored) — a corpus-hygiene note, not
   investigated.
6. **STATUS.md** carries a pre-existing **uncommitted Cowork edit** (the session-21j entry) at session start; per the
   Wave-1 precedent I did **not** bundle it into my commits (explicit per-file staging). It remains in the working
   tree for Cowork to commit.

---

## 5. Commits + gate proof

**Three fork-only, unpushed commits** (the user ratified the third, C++, one mid-run via Option A):
- `add9499002` — `dcml_parser` cadence/phraseend columns + `parse_cadence_phrase_markers` + fixtures + 4 tests.
- `16404edef9` — `batch_analyze --dump-fullspine` `phraseBoundaryTicks` array (gate-safe boundary source).
- `9a42714f45` — `compare_l6_oracle.py` (both metrics, one shared matcher).

Nothing under `src/`; no gate corpus dir touched. Measurement outputs (`tools/corpus_l6_oracle/`) and this report are
gitignored/HELD.

**Gate proof (end of run):** composing **1015** / notation **53** / snapshots **11/11**; metric suite **107**;
`characterise_bir_false.py` → **Baroque 53 / Jazz 24 / Default 53** exact.

**On this report:** Cowork re-reads the instruction, reads this in full, verifies the parser additivity + the commit
shapes at the committed objects before ratifying — then writes the L6 dormant-build instruction.

Report length: 247 lines.
