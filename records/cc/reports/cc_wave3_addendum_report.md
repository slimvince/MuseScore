# CC Wave-3 ADDENDUM — two DDMAL pickups + the DLC figbass/pedal parser exposure

> **Executes `cc_instruction_wave3_addendum.md` (2026-07-04).** Two small tasks, one change class per commit:
> **Task A** = code-free acquisition (the Wave-3 clone+pin+inventory mechanism, verbatim) of two DDMAL repos;
> **Task B** = the queued additive parser exposure (`tools/dcml_parser.py` ONLY), byte-identity proven. The
> frozen gate corpus stays byte-untouched throughout. **HEAD at run: `be70738720`** (Wave-3 report commit).
> Gate reproduces **53 / 24 / 53**, case-identity set-diff **empty both directions**, all three presets (§4).
> Commits: (1) `c28f4064ee` registry+census · (2) `3713636dd9` parser+test · (3) this fold (SHA recorded on commit).

---

## 0. Headline

- **Two DDMAL direct pickups cloned + hash-pinned** under gitignored `corpora/gt/`, both held-out, both walked
  and inventoried at the data:
  - **KMT** — `DDMAL/key_modulation_dataset` @ `6602ae6a` — the **N5 key/modulation upstream** the Wave-3
    correction named (KMT was found ABSENT as analyses at the WiR pin). **201 annotated Humdrum `.krn`** across 5
    textbooks; CC-BY-SA scores / MIT code.
  - **Flexible** — `DDMAL/Flexible_harmonic_chorale_annotations` @ `87efd245` — **571 chorales** (371 Bach + 200
    Praetorius), **permutational ("flexible") multi-reading** harmony GT → an **N2 candidate**; GPLv3.
    **⚠ RECORD-ONLY** (its 371 Bach chorales overlap the gate repertoire).
- **Registry `wave3_sources` = 21 rows** (was 19; total 78→80), regenerated **deterministically** (two runs
  byte-identical). Each new row carries the full-vector N1–N20 `needs_coverage` note (census §8c intake rule).
- **Parser exposure landed (Task B):** `tools/dcml_parser.DcmlRegion` gains additive `figbass` (N10) + `pedal`
  (N20) fields, parsed in `parse_abc_harmonies_file` (mirroring the cadence/phraseend precedent). **Byte-identity
  PROVEN** two ways (§3): gate **53/24/53** set-diff empty ×3 vs CLAUDE.md + full characterise output
  byte-identical pre/post; A-8 `summary.json` + all per-preset enumerations byte-identical pre/post.
- **Exposure material size (§3.2):** **123,881 non-empty `figbass` + 23,476 non-empty `pedal` cells** across all
  40 DLC corpora — the N10/N20 fact the future L4-evidence-channel and pedal-point-span designs will cite.
- **Three paper/README mismatches reported-not-accepted:** KMT README checkbox list ~135 < actual 201 annotated
  (living-repo growth); Flexible 572 `.krn` vs README 571 (130a/130b split); the Flexible analysis GT is an
  **R-package binary** (kernData `.krn` are `**kern`-only) — a WALK finding.
- **No-contamination proof holds:** no `src/`; frozen gate corpus byte-untouched; gate 53/24/53 set-diff empty
  both directions ×3 (§4).

---

## 1. Task A — the two DDMAL pickups (code-free; clone + hash-pin + walk + inventory)

### 1.1 KMT — `DDMAL/key_modulation_dataset` @ `6602ae6a607edcbdf6384ee1899d2c414bf981b9`

Cloned in full, checked out to `master` HEAD, gitignored (`git check-ignore` confirms `corpora/gt/key_modulation_dataset`).

- **What it is:** key/modulation annotations over **music-theory-textbook examples** in Humdrum — the upstream
  the Wave-3 audit wrongly located inside When-in-Rome. DLfM-2020 lineage; ENC record names the encoders
  **Laurent Feisthauer and Nestor Napoles Lopez**.
- **Format / alignment (verified at data):** Humdrum, **4 `**kern` voices + 4 `**text` annotation spines**.
  Key/modulation is encoded as Humdrum **key-designation tokens** (`*C:`, `*G:` …) plus inline
  **`NEWKEY=>:RN` modulation markers** in the `**text` spine (e.g. `B-=>:i`, `c=>:viio6`), with plain Roman
  numerals (`i`, `V7`, `vi`, `ii6`, `viio6`, `iio65`, …) on the non-modulating slices. Score-aligned (annotations
  embedded per-note; the repo's spine-association scripts do the note↔annotation binding). → **N5 PRIMARY**
  (key/modulation/tonicization GT — the S1/S2 residual's exact shape); **N1-adj** (textbook-relative RN in the
  `**text` spines); **N17** (textbook provenance).
- **Counts per textbook (verified — every `.krn` bears a `**text` spine):**

  | textbook | `.krn` (all annotated) | README checkbox list |
  |---|---:|---:|
  | aldwell (Aldwell/Schachter/Cadwallader) | 7 | 7 ✓ |
  | kostka-payne | 15 | 14 (ex18-3 split a/b per NOTES.md) |
  | reger | 117 | "Examples 1-100" |
  | rimsky-korsakov | 37 | 7 |
  | tchaikovsky | 25 | 7 |
  | **TOTAL** | **201** | ~135 |

  **Mismatch reported-not-accepted:** the README "Dataset" checkbox list enumerates ~135 annotated examples; the
  pinned repo holds **201** annotated `.krn` — living-repo growth (consistent with Wave-3's OpenEWLD 486≠502 /
  schema 273≠244 discipline).
- **License:** MIT (code) + **CC-BY-SA-4.0** (the humdrum scores under the 5 textbook folders — README-stated,
  LICENSE header = MIT). Neither forbids a local gitignored research clone.

### 1.2 Flexible — `DDMAL/Flexible_harmonic_chorale_annotations` @ `87efd245d5ede4054af07bc8ab5b98929dd2500b`

Cloned in full, checked out to `master` HEAD, gitignored. **WALKED** (record-only re the gate).

- **What it is:** the companion repo to the **ISMIR 2018** paper (`283_Paper.pdf`); **permutational ("flexible")
  harmonic analyses** of **571 chorales** (371 J.S. Bach + 200 Praetorius). The README does not separately name
  the annotator beyond the linked paper (DDMAL lab).
- **Coverage (verified at data):** `kernData/` = **572 `.krn`** = **371 Bach** (`Chorales_Bach_001..371`) + **201
  Praetorius files** (199 numbered + `130a`/`130b` split = 200 logical chorales). **Mismatch reported:** README
  says 571 (371 + 200); the 130a/130b split makes 572 files. The 371 Bach chorales are the Breitkopf/Dörffel
  **371 Four-Part Chorales** (KernScores lineage); the 200 Praetorius chorales are new (not available elsewhere
  per the README).
- **WALK finding — the annotation GT is an R-package binary, NOT a readable spine:** all **572/572** `kernData`
  files carry **only `**kern`** (verified: no `**harm`/`**text`/analysis spine). The permutational analysis data
  lives entirely in the R package `FlexibleChoraleHarmonicAnalysis` 0.8.0 (`*.tar.gz`, **6.8 MB** `data.table`
  binary) + filtering functions — not directly parseable without R. → **N2 candidate** (a SECOND, MULTI-READING
  annotation layer over gate-class Bach chorales — multiple valid readings per slice, unlike single-reading RN)
  + **N1-residual**.
- **⚠ RECORD-ONLY (as instructed):** its 371 Bach chorales overlap the gate repertoire (the music21 gate corpus's
  works). It is **NOT** wired to / compared against / bulk-diffed with the gate corpus in this dispatch — any use
  over gate pieces is a **future user ruling** (census §4 dedupe / the M3 contamination lesson). Inventory +
  registry row + census row only.
- **License:** **GPL-3.0** (repo LICENSE). Hash-pin-only regardless.

### 1.3 Registry + census bookkeeping

- **Registry:** two additive `wave3_sources` rows via the established deterministic generator
  (`tools/build_score_census_registry.py → wave3_rows()`); `wave3=21` (was 19), `total=80` (was 78); **two runs
  byte-identical.** Both rows carry the full N1–N20 `needs_coverage` note. Pins read live from the clones.
- **Census / audit rows (entered at the Wave-3 addendum, provenance this report):**
  - `cowork_census_full_needs_audit.md` §7.1 — a new "WAVE-3 ADDENDUM" subsection with **two rows** (KMT
    acquired / Flexible walked), each provenance = this report — the fold-list-designated §7-corrections home.
  - `cowork_score_census.md` §8c — **N5** state column: KMT ACQUIRED (201 `.krn`); **N2** state column: Flexible
    cloned+walked (record-only, R-binary caveat).
  - `tools/REPRODUCIBILITY.md` + `docs/score_inventory.md` — the two clone commands + a bed note (provenance).
  - *(Bookkeeping-location note: the instruction said "Census §1: two rows"; I landed the two rows in the audit
    §7.1 addendum — the fold-list-designated corrections home — plus the §8c N2/N5 state updates and the two
    registry rows. Flagged here so Cowork can relocate if a different section is preferred.)*

---

## 2. Task B — the DLC figbass + pedal parser exposure (additive, `tools/dcml_parser.py` ONLY)

**Edit surface (two additive edits, insertions only — `git show 3713636dd9 --stat` = 2 files, +159/−0):**

1. `DcmlRegion` dataclass gains two `Optional[str] = None` fields **`figbass`** (inversion figured-bass, N10) and
   **`pedal`** (pedal-point, N20), placed after the existing `cadence`/`phraseend` oracle fields, with a comment
   describing them + the additive/no-consumer-reads-them-yet contract.
2. `parse_abc_harmonies_file` extracts `figbass`/`pedal` from the row (`(row.get(col) or '').strip() or None`,
   exactly the cadence/phraseend idiom) and passes them to the `DcmlRegion(...)` construction.

**Scope discipline (all verified):**
- **Additive only.** New fields with `None` defaults; **no existing field's parsing changed**; no signature break
  (all three `DcmlRegion` constructors — `parse_dcml_file`, `parse_abc_harmonies_file`, `parse_rntxt_file` — use
  keyword args, so trailing optional fields are safe).
- **Mirrors the cadence/phraseend precedent exactly** — those live only in `parse_abc_harmonies_file`; so do the
  new fields. The **rntxt path** (When in Rome has neither column) leaves both `None` by default (verified in the
  smoke test + a unit test). `parse_dcml_file` (the legacy simple reader) is untouched, consistent with its
  not carrying the L6 oracle columns either.
- **No consumer changes** — no tool reads the new fields in this dispatch (that is what makes the byte-identity
  hold). No `src/`, no gate-corpus, no other tool's logic touched.
- The `form` column (DCML chord-morphology, NOT section GT) was **not** touched; its existing/registry claim
  stays accurate.

**Unit test:** `tools/tests/test_dcml_parser_figbass_pedal.py` (5 tests, self-contained temp-TSV fixture — no
dependency on the gitignored clones): figbass/pedal carried verbatim; empty cells → `None`; a TSV **lacking** the
columns still parses (safe default); the RN/root/key read surface unchanged; the rntxt path leaves both `None`.
**Full `tools/tests` suite: 112 tests pass** (107 prior + 5 new; the pre-existing `test_metric_primitives_l0l1.py`
which constructs `DcmlRegion` is unaffected — the new fields default).

---

## 3. Proof obligations

### 3.1 Byte-identity of every existing output (measured, not argued)

Ran BEFORE and AFTER the parser change, on the frozen gate corpus (each preset "Processed 352 scores (326 with
WiR coverage)"):

| check | result |
|---|---|
| Gate count (Baroque / Jazz / Default) | **53 / 24 / 53** before AND after |
| Gate case-identity set-diff vs **CLAUDE.md** (both directions) ×3 | **EMPTY** (post−CLAUDE.md = ∅, CLAUDE.md−post = ∅) all 3 presets |
| `characterise_bir_false.py` **full stdout** diff, pre vs post ×3 | **BYTE-IDENTICAL** (all 3 presets) |
| A-8 instrument (`a8_rebaseline_measure.py`) `summary.json` diff, pre vs post | **BYTE-IDENTICAL** |
| A-8 per-preset enumeration files diff (`diff -rq`), pre vs post | **BYTE-IDENTICAL** (all outputs) |

The gate uses the **rntxt** GT path (`find_wir_file` + `parse_rntxt_file`), which never touches the modified TSV
path — so the byte-identity is structural as well as measured. Any diff would have been a STOP; none occurred.

### 3.2 The exposure statistics (the point of the increment)

Per-corpus counts of non-empty `figbass`/`pedal` cells across **all 40 DLC members** (every corpus carries both
columns on every file; `mozart_piano_sonatas` = the Mozart cadence-layer corpus, included):

| corpus | files | figbass cells | files w/ figbass | pedal cells | files w/ pedal |
|---|---:|---:|---:|---:|---:|
| ABC | 70 | 15979 | 70 | 2616 | 64 |
| bach_en_fr_suites | 89 | 6077 | 89 | 760 | 31 |
| bach_solo | 68 | 3682 | 68 | 259 | 10 |
| bartok_bagatelles | 14 | 725 | 14 | 36 | 3 |
| beethoven_piano_sonatas | 64 | 12351 | 64 | 2474 | 50 |
| c_schumann_lieder | 12 | 895 | 12 | 248 | 9 |
| chopin_mazurkas | 55 | 4812 | 55 | 1458 | 40 |
| corelli | 149 | 6267 | 148 | 16 | 2 |
| couperin_clavecin | 9 | 388 | 9 | 15 | 2 |
| couperin_concerts | 84 | 4366 | 84 | 56 | 2 |
| cpe_bach_keyboard | 66 | 5591 | 66 | 525 | 35 |
| debussy_suite_bergamasque | 4 | 658 | 4 | 62 | 4 |
| dvorak_silhouettes | 12 | 787 | 12 | 375 | 9 |
| frescobaldi_fiori_musicali | 48 | 2279 | 48 | 132 | 12 |
| grieg_lyric_pieces | 66 | 4746 | 66 | 1785 | 44 |
| handel_keyboard | 6 | 162 | 6 | 15 | 1 |
| jc_bach_sonatas | 29 | 2309 | 29 | 436 | 18 |
| kleine_geistliche_konzerte | 55 | 2628 | 55 | 23 | 2 |
| kozeluh_sonatas | 49 | 8014 | 49 | 4797 | 49 |
| liszt_pelerinage | 19 | 2917 | 19 | 1465 | 17 |
| mahler_kindertotenlieder | 5 | 331 | 5 | 158 | 5 |
| medtner_tales | 19 | 4154 | 19 | 573 | 18 |
| mendelssohn_quartets | 24 | 9333 | 24 | 1502 | 24 |
| monteverdi_madrigals | 19 | 995 | 19 | 121 | 10 |
| mozart_piano_sonatas | 54 | 8047 | 54 | 1194 | 41 |
| pergolesi_stabat_mater | 7 | 606 | 7 | 43 | 3 |
| peri_euridice | 6 | 442 | 6 | 6 | 1 |
| pleyel_quartets | 6 | 725 | 6 | 116 | 4 |
| poulenc_mouvements_perpetuels | 3 | 128 | 3 | 0 | 0 |
| rachmaninoff_piano | 22 | 603 | 22 | 73 | 4 |
| ravel_piano | 3 | 640 | 3 | 109 | 3 |
| scarlatti_sonatas | 69 | 5258 | 69 | 466 | 17 |
| schubert_winterreise | 24 | 1563 | 24 | 452 | 18 |
| schulhoff_suite_dansante_en_jazz | 6 | 451 | 6 | 7 | 2 |
| schumann_kinderszenen | 13 | 528 | 13 | 126 | 7 |
| schumann_liederkreis | 12 | 468 | 12 | 131 | 10 |
| sweelinck_keyboard | 1 | 218 | 1 | 15 | 1 |
| tchaikovsky_seasons | 12 | 1721 | 12 | 526 | 10 |
| wagner_overtures | 2 | 1126 | 2 | 196 | 2 |
| wf_bach_sonatas | 9 | 911 | 9 | 109 | 4 |
| **TOTAL (40 corpora)** | **1284** | **123881** | — | **23476** | — |

Reading: **figbass** is dense (an inversion figure on most non-root-position chords — 123,881 cells over 1,284
files); **pedal** is sparse and localized (23,476 cells; `poulenc_mouvements_perpetuels` has none). This is the
material-size fact the L4 notated-inversion evidence channel (R-4) and the pedal-point-span design (N20) will
cite. *(Counts are raw non-empty TSV cells — the honest material total; `DcmlRegion.figbass/pedal` surface these
on scoreable-numeral rows.)*

### 3.3 Existing tests

`test_metric_primitives_l0l1.py` (which builds `DcmlRegion`) and the rest of `tools/tests` stay green — 112/112.

---

## 4. Acceptance — no-contamination proof + discipline

**No `src/`, gate corpus byte-untouched.** Commit (1) = `tools/` registry + provenance (`build_score_census_
registry.py`, `score_census_registry.json`, `REPRODUCIBILITY.md`) + `docs/score_inventory.md`. Commit (2) =
`tools/dcml_parser.py` + `tools/tests/test_dcml_parser_figbass_pedal.py`. **No path under `src/`; no path under
`tools/corpus/`.** Both new clones are gitignored (`git check-ignore` confirms `corpora/gt/{key_modulation_dataset,
Flexible_harmonic_chorale_annotations}`).

**Gate reproduction** (`characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}`), before AND
after the whole addendum:

| preset | count | before==after (byte-stability) | set-diff vs CLAUDE.md (both directions) |
|---|---|---|---|
| Baroque | **53** | BYTE-IDENTICAL | EMPTY ✅ |
| Jazz | **24** | BYTE-IDENTICAL | EMPTY ✅ |
| Default | **53** | BYTE-IDENTICAL | EMPTY ✅ |

**Held-out discipline:** both new beds `split=held-out` (never tuned against). Nothing creates/touches a held-out
designation change; nothing is tuned against anything. Flexible is additionally RECORD-ONLY (never compared to the
gate).

**Reuse-vs-new + what retires.**
- **Reused verbatim:** the clone + `git checkout <pin>` + gitignored hash-pin-only mechanism; the deterministic
  registry generator + `wave3_rows()` schema + `needs_coverage` field; the `characterise_bir_false.py` /
  `a8_rebaseline_measure.py` byte-identity oracles; the cadence/phraseend additive-field pattern in `dcml_parser`;
  the census §7 / §8c bookkeeping form; the `unittest` + temp-fixture test convention.
- **New (minimal):** two `wave3_sources` rows; the additive `DcmlRegion.figbass/pedal` fields + their parse; one
  self-contained test file.
- **Retires:** the registry `_notes` "parser-dropped … exposure queued" clause is now closed (the exposure landed
  this addendum); otherwise **nothing** retires.

---

## 5. STOP conditions — none tripped

Checked each STOP: Task-B byte-identity held everywhere (gate set-diff empty ×3, characterise + A-8 outputs
byte-identical); neither DDMAL repo's content contradicted its record in a way that changes its handling (the
KMT-annotated-vs-README and Flexible-file-count mismatches are living-repo/edition variance, reported-not-accepted,
not handling-changing); the Flexible set was **NOT** compared/wired against the gate corpus (record-only honored);
nothing under `src/`; the registry regen stayed deterministic (two runs byte-identical). No condition met.

Per-source facts (report lines, not STOPs): KMT README ~135 < 201 annotated; Flexible 572 `.krn` vs README 571;
Flexible analysis GT is an R-package binary (kernData `**kern`-only).

## 6. Loose ends surfaced (per "surfacing anything else dirty")

- **`cowork_union_search_record.md`** (untracked) — a Cowork deliverable for the **union search round** (census
  §8c step 3), awaiting **user disposition** of its §6; per `COWORK_HANDOFF.md` it "rides the fold AFTER
  disposition." It is **NOT** in this addendum's fold list and is left untracked, unchanged.
- `idiom_discovery/vl_discovery_out.txt`, `idiom_discovery/vl_orthogonality_out.txt`, `scratch_artifacts/` —
  pre-existing deliberately-untracked dumps, unchanged.
- The bookkeeping-location interpretation for "Census §1: two rows" (§1.3 note) — flagged for Cowork.

## 7. Commits (local, unpushed, fork-only)

`git add` used explicit paths only; the census/audit/STATUS/handoff narrative docs are folded in commit (3); the
`cc_instruction_*` and this report are force-added per the `/cc_*.md` gitignore convention. Per the 22j/D-L3a
precedent, this report (in the fold commit) cites the prior commits' SHAs; its own commit SHA is recorded on commit.

| # | scope | SHA | files |
|---|---|---|---|
| 1 | Task A registry + provenance | `c28f4064ee` | `tools/build_score_census_registry.py`, `tools/score_census_registry.json`, `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md` |
| 2 | Task B parser + test | `3713636dd9` | `tools/dcml_parser.py`, `tools/tests/test_dcml_parser_figbass_pedal.py` |
| 3 | `docs(cowork):` fold + this report | (recorded on commit; force-added) | `STATUS.md`, `COWORK_HANDOFF.md`, `cowork_score_census.md`, `cowork_census_full_needs_audit.md`, `cc_instruction_wave3_addendum.md` (-f), `cc_wave3_addendum_report.md` (-f) |

Nothing pushed; `upstream` push remains disabled; fork (`origin = slimvince/MuseScore`) only. The clones are
gitignored/hash-pin-only — the pins live in the committed registry + this report.
