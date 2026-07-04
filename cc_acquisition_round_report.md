# CC Acquisition Round — union-search-approved pickups + the PDMX symbol-count attempt

> **Executes `cc_instruction_acquisition_round.md` (2026-07-04).** Clone + hash-pin + inventory + bookkeeping
> the Wave-3 mechanism verbatim, plus ONE read-only counting measurement (Task 3). Executes the user-approved
> disposition of the union search round (`cowork_union_search_record.md` §6, all five items). **HEAD at run:
> `9441e94551`** (Wave-3 addendum fold). Nothing under `src/`; no production code; the frozen gate corpus stays
> byte-untouched. Gate reproduces **53 / 24 / 53**, case-identity set-diff **empty both directions**, all three
> presets, **before AND after** (§6). Commits: (1) `4997757298` registry+provenance · (2) this fold (SHA recorded on commit).

---

## 0. Headline

- **6 sources cloned/pinned + inventoried; 2 recorded (gated/no-clone); 1 counting pass STOPPED.** All beds
  held-out, hash-pin-only, gitignored under `corpora/gt/`. Every paper-claim re-verified at the cloned data.
- **★ TWO record license mismatches CORRECTED at the data (reported-not-accepted):** **MCMA = CC-BY-NC-SA-4.0**
  (the record §1 / VL-design §15-4 said "CC BY 4.0"; the NC clause matters for T-32); **vocsep = MIT** (the record
  §1 said license "unstated"). Both corrections applied to the census, the record, the registry, and the VL design.
- **Two of the three N9 beds ship CODE, not committed GT graphs** — piano_svsep FETCHES its GT at runtime from
  `github.com/fosfrancesco/piano_corpora_dcml`; vocsep BUILDS its ~1,054 graphs at runtime from bach-370-chorales +
  Haydn/Mozart SQ + MCMA. The pin captures the loader + fetch/build path (per the dispatch's "pin what is pinnable
  and record the fetch path"); the raw GT is a recorded follow-on pin.
- **Registry `wave3_sources` = 29 rows** (was 21; total 80→88), regenerated **deterministically** (two runs
  byte-identical); purely additive (DLC + beds byte-identical, no pre-existing wave3 row changed, only the `pdmx`
  row gained a `needs_coverage` note). Each new row carries the full-vector N1–N20 `needs_coverage` note.
- **★ Task 3 (PDMX `<harmony>` count) STOPPED, correctly (not a wave stop):** the HELD PDMX form is
  **metadata-only** (`tools/pdmx/PDMX.csv` 250k-row index + `jazz_candidates.csv` + 5 spot-check `.mxl`) — it has
  no chord-symbol column and the raw MXL lives only in the Zenodo archive. Counting `<harmony>` would require a
  re-download the read-only dispatch forbids. No proxy invented; the subset stays UNMEASURED (§Task-3).
- **No-contamination proof holds:** nothing under `src/`; the frozen gate corpus byte-untouched; gate **53 / 24 / 53**,
  set-diff empty both directions ×3 presets, before==after byte-identical ×3 (§6).

Pins (source of truth = `tools/score_census_registry.json → wave3_sources[].pinned_commit`, read live from the clones):

| source | need | repo / artifact | pin | license (verified at data) |
|---|---|---|---|---|
| piano_svsep | N9 | github CPJKU/piano_svsep | `1462e7c28d…` | MIT (code) |
| MCMA | N9 | gitlab skalo/mcma | `2bdb12e233…` | **CC-BY-NC-SA-4.0** (record: CC-BY ✗) |
| vocsep_ijcai2023 | N9 | github manoskary/vocsep_ijcai2023 | `82152a9591…` | **MIT** (record: unstated ✗) |
| Mikrokosmos-difficulty | N14 | github PRamoneda/Mikrokosmos-difficulty | `f77aebc1d4…` | none (no LICENSE) |
| GuitarSet (annotation) | N12 | Zenodo 3371780 `annotation.zip` | `sha256:8daa02e6…` | CC-BY-4.0 |
| Batik-plays-Mozart | N1/N4/N13-p | github huispaty/batik_plays_mozart | `30256ca48f…` | none (no LICENSE) |
| CIPI | N14 | Zenodo 8037327 | — (gated) | research-only |
| PSyllabus | N14-adj | Zenodo 14794592 | — (recorded) | research-only |

---

## 1. Task 1 — N9 voice-separation beds (three clones)

### 1.1 piano_svsep — `CPJKU/piano_svsep` @ `1462e7c28d7adaae033150883a7cb00238ee364a` (MIT)

Cloned in full, gitignored. **Verified at the data — the repo ships CODE, NOT the GT graphs.** Top level:
`LICENSE (MIT) · README · piano_svsep/ (package) · pretrained_models/ · artifacts/ (one test_score) · launch_scripts/`.
The GT dataset is fetched at runtime: `piano_svsep/data/dataset.py :: DCMLPianoCorporaDataset` sets
`url = "https://github.com/fosfrancesco/piano_corpora_dcml.git"` and reads `scores/<collection>/*.musicxml` (per-note
voice/staff GT derived from the engraving). So the **393 pieces / 77-test** figure is the fetched dataset's split, not
committed material.

- **PIN = the code repo; the actual GT lives at the fetch path** (`fosfrancesco/piano_corpora_dcml`) — a recorded
  follow-on pin candidate, **NOT fetched this round** (the dispatch directs "pin what is pinnable + record the fetch path").
- **`jpop` re-confirmed non-public** (the access-path line): README — "the `jpop` dataset we used in our paper is not
  public"; `MusescoreJPopDataset` docstring — "This dataset is not publicly available. The code here is therefore only
  for reference." Not chased.
- **N9 role:** per-note **voice + staff + chord-cluster** GT incl. homophonic (chord) voices and CROSS-STAFF voices —
  the SOTA piano voice/staff task set. Caveat carried (record §1): labels originate from engraved notation; for piano,
  engraving-voice ≈ the inference target (the SOTA field accepts this) — stated at intake.

### 1.2 MCMA — `skalo/mcma` (GitLab) @ `2bdb12e233420163d4d1b52c5ecba3d2bd84231e`

Cloned in full, gitignored. **Verified at the data:** `mcma/mcma/` = **475 `.mxl`** (matches the record's ~475) + 12
`metadata.csv` + 11 json, one INDEPENDENT PART PER TRACK (voice = the track), hand-exploded Baroque counterpoint
(albinoni, bach_js {goldberg, inventions, kunst_der_fuge, sinfonias, WTC I, WTC II}, becker, buxtehude, lully, …).

- **Track-count split RE-COUNTED at the data** from every `metadata.csv`'s "Number of Tracks" column: **153 two-track /
  239 three-track / 83 four-plus** (73×4 + 8×5 + 2×6) = 475 — **EXACTLY the record's 239/153/83.**
- **★ LICENSE MISMATCH reported-not-accepted:** the `LICENSE` file is **Attribution-NonCommercial-ShareAlike 4.0
  International (CC-BY-NC-SA-4.0)**, NOT the record's "CC BY 4.0". The NC + SA clauses matter for any commercial use
  (T-32) and for VL-H's downstream posture; research mirroring (hash-pin-only, held-out) is unaffected.

### 1.3 vocsep_ijcai2023 — `manoskary/vocsep_ijcai2023` @ `82152a9591ba2759a556a6f9f52fd8eab771ca4a`

Cloned in full, gitignored. **Verified at the data — CODE repo; the graph collection is BUILT at runtime.** Top level:
`LICENSE (MIT) · README · main.py · vocsep/ (package)`. `vocsep/data/datasets/` holds the loaders `bach_chorales.py`
(`url = github.com/craigsapp/bach-370-chorales`), `haydn_string_quartets.py`, `mozart_string_quartets.py`, `mcma.py`;
the **~1,054-graph** note-collection is built from those at runtime.

- **PIN = the code repo;** source scores are fetched/held separately (and dedupe: shared with our MCMA clone + the held
  Bach chorales).
- **★ LICENSE MISMATCH reported-not-accepted:** the `LICENSE` file is **MIT** (Copyright 2023 Emmanouil Karystinaios),
  NOT the record's "unstated". vocsep IS MIT-licensed.
- **Content note:** the committed loaders are chorales / Haydn-SQ / Mozart-SQ / MCMA — the record's "Inventions/WTC"
  arrive via the MCMA dependency (the README results table reports Inventions / WTC I / WTC II). Caveat (record §1):
  notation-derived voice labels — weaker as an inference GT except the WTC fugues (which come through MCMA).

---

## 2. Task 2 — the other approved pickups

### 2.1 Mikrokosmos-difficulty — `PRamoneda/Mikrokosmos-difficulty` @ `f77aebc1d4f2b06d5161c95575972540a8dc5b80`

Cloned in full, gitignored. **Verified:** `musicxml/` = **147 `.xml`** (matches the record's 147); `metadata/` =
bartok/books/henle JSONs + `mikrokosmos_metadata.csv` (the `henle_difficulty` column, e.g. "Piano 1 easy", is the
3-class label source); `splits.json` = CV folds. **NO LICENSE file** (matches record §3) → hash-pin-only. N14 primary
(the open, symbolic-score difficulty half); the T-32 commercial-license caveat rides the product-tool register.

### 2.2 GuitarSet (annotation artifact only) — Zenodo `10.5281/zenodo.3371780`, `sha256:8daa02e6417ccca1685feb44b135e95928ad7037e5032ecb326b5791856fda99`

Per the pinnable-source rule (like the WJD SQLite): the **ANNOTATION artifact only** was downloaded + sha256-pinned.
`annotation.zip` = **39,132,574 bytes** (matches the Zenodo `size` exactly), **360 `.jams`** verified inside (matches
the record's 360). Excerpt names encode style/tempo/key + `comp|solo` (e.g. `03_SS1-100-C#_comp.jams`,
`04_Jazz2-110-Bb_solo.jams`) — the instructed-chart vs performed-comping pair contrast (N12). License **CC-BY-4.0**
(Zenodo metadata). **The 4 AUDIO artifacts are NOT our material** — recorded, none downloaded: `audio_mono-mic.zip`
(657 MB), `audio_mono-pickup_mix.zip` (683 MB), `audio_hex-pickup_original.zip` (3.21 GB), `audio_hex-pickup_debleeded.zip`
(3.61 GB).

### 2.3 Batik-plays-Mozart — `huispaty/batik_plays_mozart` @ `30256ca48f4a1a77425b2ed47f0ce2cd2a672758` (multi-need)

Cloned in full, gitignored. **Verified at the data (the multi-need intake — record §2 star):**

- **N1/N4 harmony + cadence GT:** `score_parts_annotated/` has per-movement CSVs. `kv279_1_spart_harmony.csv` carries
  the full DCML columns (`globalkey, localkey, chord, numeral, chord_type, chord_label`); `_spart_cadence.csv` +
  `_spart_phrases.csv` = cadence + phrase layers. **36 scores = 12 Mozart sonatas × 3 movements.**
- **N13-partial trill structure VERIFIED on one file (`kv279_1.match`):** partitura match format; **49** score notes
  carry the `trill-mark` attribute (e.g. `snote(n30-1,[C,n],5,2:3,0,1/16,…,[v1,staff1,trill-mark])-note(…)`) and there
  are **163 `insertion` lines** (performed notes with no score counterpart — where the realized trill notes appear).
  So the trill realizations are recoverable by a grouping heuristic, NOT shipped as labeled pairs. **Structure verified;
  NO extraction built** (per the dispatch).
- **The `annotations/` dir is an UNPOPULATED git submodule** (the upstream DCML "Annotated Mozart Sonatas" — not fetched
  by a plain clone; the materialized annotations live in `score_parts_annotated/`).
- **NO LICENSE file** (matches record §2 "none visible") → hash-pin-only.
- **⚠ Overlap recorded:** the harmony/cadence GT = the DCML Annotated Mozart Sonatas = our held `mozart_piano_sonatas`
  (DLC) + the WiR Mozart RN. Recorded, **NOT wired / diffed against the gate** (census §4 dedupe / M3 lesson).

### 2.4 Recorded rows (no clone)

- **CIPI** — Zenodo `8037327`: 652 pieces, Henle 1–9, MusicXML included; **gated** (request-access, research-only).
  **USER ACTION: the access form is still pending.** Full needs row recorded (status=gated); lands on grant.
- **PSyllabus** — Zenodo `14794592`: 7,901 exam-board-labeled recordings, **no symbolic scores** (audio/MIDI only) →
  **N14-adj**. Full needs row recorded (status=recorded).

---

## Task-3 — the PDMX `<harmony>` counting pass: ATTEMPTED + STOPPED (correctly)

**Located the held copy** (registry row `pdmx`; `tools/REPRODUCIBILITY.md` §tools/pdmx). **The held form is
metadata-only** — verified at the data:

| held artifact | what it is |
|---|---|
| `tools/pdmx/PDMX.csv` (225 MB) | the 250k-row metadata index (62 columns: path/mxl/metadata/rating/complexity/n_tracks/tracks/n_annotations/has_annotations/… + subset flags) |
| `tools/pdmx/jazz_candidates.csv` | a derived jazz filter (from `pdmx_jazz_candidates.py`) |
| `tools/pdmx/spot_check/` | 5 sampled `.mxl` (from `pdmx_spot_check.py`, downloaded ad hoc) |

**Why (1) cannot be answered read-only from the held form:**
- **No chord-symbol column exists.** `n_annotations` / `has_annotations` conflate **all** annotation types (chord
  symbols + dynamics + tempo + text — `analyze_pdmx.py`'s own comment states this); `tracks` = instrument-program codes
  (e.g. `'0-0'`); there is no `n_chords` / `n_harmony` field. A column-name scan for chord/harmony/symbol = **empty**.
- **The raw MXL and per-score JSON are NOT on disk.** The `mxl` column paths (e.g. `./mxl/1/11/Qmbb….mxl`) point into
  `mxl.tar.gz`, and the `metadata` column paths (e.g. `./metadata/5/5740212.json` — the MusicRender JSON) point into the
  metadata archive; **both live only in the Zenodo record (15571083), not locally.**

**STOP decision (per the dispatch's own STOP wording):** counting `<harmony>` (MusicXML) or `ChordSymbol` (the
MusicRender JSON) would require fetching `mxl.tar.gz` + parsing per file, or obtaining the JSON form — a
**re-download / acquisition**, which the read-only, **do-not-re-download** dispatch forbids (and the "measure only, don't
become an extraction/subset-builder" STOP). **No proxy was invented** (`has_annotations` would over-count and is not
chord-specific). **The symbol-bearing multi-voice subset stays UNMEASURED.** The N12 lever's *feasibility* is unchanged
(PDMX does preserve `<harmony>` in the mxl) — the *held artifact* is simply the wrong form to measure it from; the
measurement is a future increment gated on a user decision to fetch the MXL tarball. Recorded in the `pdmx` registry
row's `needs_coverage` note + census §8c N12 + the union-search record §4.

**Joint table (1)/(2)/(3): NOT PRODUCED** — the STOP precedes it (there is no symbol-bearing set to break down by the
`complexity`/`rating` buckets). The buckets exist in the CSV and would be the breakdown axis once (1) is measurable.

---

## 4. Overlap notes (dispatch-required)

- **piano_svsep ↔ our held DCML:** the 393 pieces are DCML piano corpora fetched from `fosfrancesco/piano_corpora_dcml`
  (composers parsed from `scores/<composer>_<type>/` folder names). By WORK this is the same family as our held DLC piano
  members — `mozart_piano_sonatas`, `beethoven_piano_sonatas`, `chopin_mazurkas`, `scarlatti_sonatas`, `kozeluh_sonatas`,
  `grieg_lyric_pieces`, etc. The **exact 393↔DLC mapping needs the `piano_corpora_dcml` manifest** (not fetched this
  round) — recorded as the follow-on. Consequence: piano_svsep's value to us is the **voice/staff GT layer** over scores
  we largely already hold — the Wave-2 "labels over held scores" pattern again.
- **MCMA ↔ held WTC/Bach material:** MCMA's `bach_js/` includes WTC I & II + Inventions + Sinfonias + Goldberg + Kunst
  der Fuge. By WORK the WTC I overlaps the **WiR WTC-I interior slice** (24 scores) + the **algomus `bach-wtc-i` fugue
  labels** (23 `.dez`); the Inventions/Sinfonias are new relative to our held sets. Recorded, **NOT wired**.
- **vocsep ↔ held material:** vocsep's graphs are built from bach-370-chorales + Haydn/Mozart SQ + **MCMA** — so it
  shares source material with our just-cloned MCMA and the held Bach chorales. Its GT is a derived transform, not new scores.
- **Batik ↔ held Mozart:** harmony/cadence GT = the DCML Annotated Mozart Sonatas = held `mozart_piano_sonatas` + WiR
  Mozart RN (§2.3). Recorded, NOT wired.

---

## 5. Bookkeeping delivered

- **Registry** (commit 1 `4997757298`): +8 additive `wave3_sources` rows via the deterministic generator
  (`build_score_census_registry.py → wave3_rows()`); `wave3` 21→29, `total` 80→88; two runs byte-identical; pins read
  live (git sha / sha256). The `pdmx` row gained a `needs_coverage` note (Task-3 STOP). Purely additive: DLC + beds
  byte-identical, no pre-existing wave3 row changed, only `pdmx` changed.
- **`cowork_union_search_record.md` §1–§4** (fold): an "ACQUIRED @ pin" (or gated/recorded/STOPPED) annotation appended
  per item — the record doc is the provenance home (the audit-§7.1 precedent).
- **Census `cowork_score_census.md` §8c** (fold): N9 / N12 / N14 needs-vector state columns updated to
  acquired/recorded/measured-STOPPED states.
- **`tools/REPRODUCIBILITY.md` + `docs/score_inventory.md`** (commit 1 / fold): the acquisition-round clone/pin/download
  commands + bed notes + the CIPI/PSyllabus recorded lines + the PDMX-STOP note.
- **`cowork_voiceleading_axis_design.md` §15-4** (fold): the MCMA-license correction (CC-BY → CC-BY-NC-SA-4.0) + the
  ACQUIRED annotation; **`cowork_product_tool_register.md` T-32** carries the pre-existing disposition caveat.

---

## 6. Acceptance — no-contamination proof + discipline

**No `src/`; gate corpus byte-untouched.** Commit 1 = `tools/` registry + provenance + `docs/score_inventory.md`. All
new clones/artifacts are gitignored (`git check-ignore` confirms `corpora/gt/{piano_svsep,mcma,vocsep_ijcai2023,
Mikrokosmos-difficulty,batik_plays_mozart,guitarset/annotation.zip}`); nothing under `corpora/` shows in `git status`.

**Gate sandwich** (`characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}`), BEFORE and AFTER the
whole round (each preset "Processed 352 scores (326 with WiR coverage)"):

| preset | count | set-diff vs CLAUDE.md (both directions) | before==after (byte-stability) |
|---|---|---|---|
| Baroque | **53** | EMPTY ✅ | BYTE-IDENTICAL |
| Jazz | **24** | EMPTY ✅ | BYTE-IDENTICAL |
| Default | **53** | EMPTY ✅ | BYTE-IDENTICAL |

The round touches no `src/`, no `tools/corpus/`, no gate GT path — so the byte-identity is structural as well as
measured. Any diff would have been a STOP; none occurred.

**Held-out discipline:** every new bed `split=held-out` (never tuned against). Batik + the Flexible-class overlaps are
recorded, never wired to the gate.

**Reuse-vs-new + what retires.**
- **Reused verbatim:** the clone + `git checkout <pin>` + gitignored hash-pin-only mechanism; the sha256 pinnable-source
  rule (GuitarSet artifact, as WJD); the deterministic registry generator + `wave3_rows()` schema + `needs_coverage`
  field + the `_corpora_sha` / `_file_sha256` helpers; the `characterise_bir_false.py` gate oracle + the `gate_setdiff`
  parser; the census §8c / union-record §7.1 bookkeeping form; the "generator IS the registry mechanism" resolution of
  the "no tool code" tension (the addendum precedent, Cowork-owned).
- **New (minimal):** 8 `wave3_sources` rows + the `pdmx` `needs_coverage` note; the acquisition-round REPRODUCIBILITY /
  score_inventory subsections; two new `gt_type` values ('voice', 'difficulty').
- **Retires:** **nothing** (as expected). The N9 acquisition candidates the union search queued are now on disk; the N14
  open half is on disk; the N12 clean-add is on disk. CIPI (user form) + the PDMX MXL-tarball fetch remain the only
  named open corpus items.

---

## 7. STOP conditions — one tripped (Task-3, correctly), zero wave stops

- **Task-3 STOP TRIPPED and correctly reported** (the held PDMX form cannot answer the count read-only; not re-downloaded,
  no extraction/subset built) — this is the dispatch's own anticipated STOP, and it does **not** stop the wave.
- Every other STOP checked and NOT met: nothing touched `src/` or tracked production code (the registry generator is the
  directed registry mechanism, the addendum precedent); the frozen gate corpus + the held PDMX copy were not modified;
  no license is genuinely ambiguous about LOCAL mirroring (MCMA NC-SA / no-license repos all permit a gitignored research
  clone); the counting script stayed a read-only inspector (never an extraction/subset-builder); the registry regen stayed
  deterministic (two runs byte-identical).

Per-source facts (report lines, not STOPs): MCMA license = CC-BY-NC-SA-4.0 (record: CC-BY); vocsep license = MIT
(record: unstated); piano_svsep + vocsep ship code (GT fetched/built at runtime); Batik `annotations/` is an unpopulated
submodule.

## 8. Loose ends surfaced (per "surfacing anything else dirty")

- `idiom_discovery/vl_discovery_out.txt`, `idiom_discovery/vl_orthogonality_out.txt`, `scratch_artifacts/` — pre-existing
  deliberately-untracked dumps, unchanged.
- `cowork_product_tool_register.md` + `cowork_voiceleading_axis_design.md` were **already dirty at session start** (the
  Cowork union-search disposition edits); folded here (the VL design additionally gains this round's MCMA-license fix +
  ACQUIRED annotation).

## 9. Commits (local, unpushed, fork-only)

`git add` used explicit paths only. Per the 22j/D-L3a precedent, this report (in the fold commit) cites the prior
commit's SHA; its own commit SHA is recorded on commit.

| # | scope | SHA | files |
|---|---|---|---|
| 1 | registry + provenance | `4997757298` | `tools/build_score_census_registry.py`, `tools/score_census_registry.json`, `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md` |
| 2 | `docs(cowork):` fold + this report | (recorded on commit; force-added) | `STATUS.md`, `COWORK_HANDOFF.md`, `cowork_score_census.md`, `cowork_union_search_record.md`, `cowork_product_tool_register.md`, `cowork_voiceleading_axis_design.md`, `cc_instruction_acquisition_round.md` (-f), `cc_acquisition_round_report.md` (-f) |

Nothing pushed; `upstream` push remains disabled; fork (`origin = slimvince/MuseScore`) only. The clones are
gitignored/hash-pin-only — the pins live in the committed registry + this report.
