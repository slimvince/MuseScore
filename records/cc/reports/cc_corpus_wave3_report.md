# CC Corpus Wave 3 — full-needs acquisition + inventory

> **Executes `cc_instruction_corpus_wave3.md` (2026-07-04).** Scope set by the user-disposed census §8c
> FULL-NEEDS AUDIT (`cowork_census_full_needs_audit.md`): jazz/pop GT · cadence/dual-annotator/form beds ·
> figured bass · trees/reduction · WiR interior inventory · plain-score stress · census/registry bookkeeping ·
> the re-discovery trigger CHECK. **HEAD at run: `a228e2bef6`.** Clone + hash-pin + inventory + bookkeeping ONLY —
> **no `src/`, no code, no analysis run; the frozen gate corpus is byte-untouched.** Gate reproduces **53 / 24 / 53**,
> case-identity set-diff **empty both directions**, all three presets (§9). Registry commit `63de0df27a`; fold commit
> `8aae19f586`; this report is commit #3 (force-added per the `/cc_*.md` convention).

---

## 0. Headline

- **10 beds cloned + hash-pinned** under a new gitignored `corpora/gt/` (GT) + `corpora/plain/` (stress) subtree
  (kept separate from the Wave-2 `corpora/annot/` beds and the idiom-discovery inputs in `corpora/ship|expl/`). All
  **research-tier, hash-pin-only, held-out** (never tuned against). The native WJD SQLite is pinned by **sha256**
  (non-git, pinnable-source rule).
- **3 inventory rows** (already-held material, no new clone): the ChoCo `jazz-corpus` (160 jams) + `weimar` (916 jams)
  partitions, and the **WiR interior** per-slice inventory.
- **6 gated / unavailable / walked / enumerated records** with precise access paths: EWLD (Zenodo request-access),
  HookTheory full (HF academic gate), Sears Haydn (no public deposit), GTTM (no single artifact), `DCMLab/figured-bass`
  (**WALKED = a realization script, not a GT corpus**), and the `humdrum-tools/humdrum-data` enumeration (71 repos, cloned nothing).
- **Every paper-claim verified at the cloned data** — three benign **mismatches reported, not silently accepted**:
  OpenEWLD **486** .mxl (not 502); algomus fugues has **bach-wtc-i only (23 ref.dez)** — the 12 Shostakovich fugues are
  NOT in the repo; `schenker41`'s git HEAD is **README-only** (the 41 excerpts were never committed).
- **Registry v2 gains an additive `wave3_sources` section (19 rows)**; the 40 DLC + 16 other + 3 bed rows are byte-identical.
  Every row carries a full-vector **N1–N20 `needs_coverage`** note (census §8c intake rule). Regeneration deterministic
  (`total=78`, two runs byte-identical). Census + REPRODUCIBILITY.md + score_inventory.md updated.
- **N9 gating inspection delivered** (§5): protovoice-annotations is the nearest thing to stream GT in the whole
  enumeration — verdict = **partially usable, via a derivation→surface-stream step; does not by itself close N9**.
- **WiR dual-annotation overlap computed** (the audit's open N2 number): **Tymoczko∩DCML = 0** by (composer, work,
  movement); the only co-located dual set is the **27 TAVERN A/B pairs** (§6). One audit assumption **corrected**: KMT is
  NOT a confirmed analyzed slice at this WiR pin.
- **Re-discovery trigger: FIRED** (recorded only, never run — §8): Wave 3 makes substantial new chord-symbol mass
  available (CoCoPops, OpenEWLD).
- **No-contamination proof holds:** nothing under `src/`; the frozen gate corpus byte-untouched; gate **53 / 24 / 53**,
  set-diff empty both directions ×3 presets (§9).

Pins (source of truth = `tools/score_census_registry.json → wave3_sources[].pinned_commit`, read live from the clones):

| bed | repo / source | pin | needs |
|---|---|---|---|
| CoCoPops | github Computational-Cognitive-Musicology-Lab/CoCoPops | `6b04f4f994…` | N3 N12-adj N16-adj N17 |
| OpenEWLD | github 00sapo/OpenEWLD | `ec03cbd809…` | N12 N3-adj |
| BCFB | github juyaolongpaul/Bach_chorale_FB | `431c5c019a…` | N10 |
| algomus-data | gitlab algomus.fr/algomus-data | `a1801b5b42…` | ★ N16 N4 N18 N20 N11-adj N3-adj |
| protovoice-annotations | github DCMLab/protovoice-annotations | `8ccb995e2e…` | N9(gating) N11 |
| schenker41 | github pkirlin/schenker41 | `3ec7eed342…` | N11 (README-only) |
| WJD native | jazzomat.hfm-weimar.de/wjazzd.db | `sha256:af6a0d9d…` | N3 N4 N16 N17 |
| OpenScore Lieder | github OpenScore/Lieder | `6b2dc542ce…` | Tier S, N1-carrier |
| OpenScore StringQuartets | github OpenScore/StringQuartets | `d13289cd70…` | Tier S, N7-mat |
| ASAP | github fosfrancesco/asap-dataset | `afc815c75c…` | Tier S (not N15) |

---

## 1. Task 1 — jazz/pop analysis GT (N3, N12)

**CoCoPops** — `Computational-Cognitive-Musicology-Lab/CoCoPops` @ `6b04f4f994…`. CC-BY. Cloned in full.
**Claim verified:** README states **414 complete melodic-harmonic transcriptions of 398 unique tracks** (Billboard =
McGill Billboard in Humdrum + 214 new melody transcriptions; RollingStone = RS200). Measured at pin: **628 `.hum`**
(Billboard 428 + RollingStone 200 — the extra files are variant/partial encodings above the 414 "complete" figure).
Fully symbolic; spines on a sample file: **`**harm` (RN) + `**kern` (melody) + `**harte` + `**harmony` + `**phrase` +
`**form` + metadata**. → **the top Tier-J acquisition (N3)**; N12-adj (chords over a symbolic melody, not a full realized
score); N16-adj (`**form/phrase`); N17. **Dedupe:** the symbolic superset of McGill-Billboard + RS200 (both held as ChoCo
partitions / registry rows) — recorded in the row's `needs_coverage`.

**OpenEWLD** — `00sapo/OpenEWLD` @ `ec03cbd809…`. **PD.** **Mismatch reported:** **486** `.mxl` PD lead sheets at pin,
not the ~502 census/paper figure (living-repo / PD-filter variance — reported, not accepted). One `.csv` filename
contains `?` (NTFS-illegal), so the Windows working-tree checkout is partial; **pin + inventory taken from git objects
(`git ls-tree`)** — the bed is hash-pin-only/held-out, so the partial working tree is immaterial (a Linux consumer checks
out fully). Zenodo DOI `10.5281/zenodo.4332855`. → N12 (symbol+melody leadsheet), N3-adj. **EWLD** (the ~5,000 superset)
is **gated** (§7).

**HookTheory / HLSD full** — attempted `m-a-p/HookTheory` (HF): **gated** — academic-affiliation gate + accept-conditions,
CC-BY-NC-4.0, 112 GB; not obtainable in a non-interactive session (matches the standing "pending HF access" note). The
sample entry (`hooktheory_hlsd`, `wayne391/lead-sheet-dataset`) is left **as-is**. Access path recorded (§7).

**Jazz Corpus (Granroth-Wilding & Steedman)** — inventoried from the pinned ChoCo clone: `corpora/ship/choco/partitions/
jazz-corpus` = **160 `.jams`** (choco/jams + jams-converted; the census's 76-piece function set). Chords-only (no engraved
score), research-tier. → the rare **harmonic-FUNCTION jazz GT (N3)**. **Dedupe:** a ChoCo partition, not a new acquisition;
the native MCR/Steedman set is the upstream. Registry row `choco_jazz_corpus_slice` (status=inventory).

**WJD native** — downloaded `wjazzd.db` from `jazzomat.hfm-weimar.de/download/downloads/wjazzd.db`, **hash-pinned by
sha256 `af6a0d9debf042c3581565bd75baad591d32e166cd2ec7298519883de614bf12`** (42.5 MB, pinnable-source rule). **Verified at
the DB:** **456 solos** (`solo_info` + `transcription_info`), 200,809 `melody` rows, tables incl. `sections` (the native
phrase/form layer beyond the ChoCo chord slice) + `beats`; **`db_info` = v2.1 / DB 2.2 (2018), license = ODbL** (embedded).
→ N3 + **N4** (`sections`) + **N16** (form) + N17. **Dedupe:** the ChoCo `weimar` slice (916 jams, held) is the chord-only
re-encoding of this DB — the native adds the phrase/form/beat layers ChoCo drops (registry rows `weimar_jazz_database` +
`choco_weimar_slice`).

## 2. Task 2 — cadence / dual-annotator / form beds (N2, N4, N5, N16, N18)

**Sears Haydn cadences** — **unavailable.** No public GitHub/Zenodo/OSF deposit found across three targeted searches;
widely cited (Sears et al. 2018 — 270 cadence tokens / 50 expositions, two annotators, + key/mode/modulation/pivot) but
not openly deposited. Access = contact the authors (David Sears) or the paper supplementary. A top multi-need node
(N2+N4+N5) — recorded as an access path (`sears_haydn_cadences`, status=unavailable). Per-source failure = report line,
not a wave STOP.

**algomus Mozart string quartets** — located inside the **`algomus.fr/algomus-data`** monorepo (the backing store for
algomus.fr/data) @ `a1801b5b42…`, ODbL. `quartets/mozart` = **32 `-ref.dez`** — **matches the paper's 32 movements
exactly**. Dezrann format: `labels` of `type` **Structure** (EXPOSITION/DEVELOPMENT/RECAPITULATION/…), **Cadence**,
**Harmony**, each `start`+`duration` in **seconds** + `line`; `meta.cite` = "Learning sonata form structure on Mozart's
string quartets". → **the ratified best N16** (form/section GT) + N4 (cadences). **Alignment caveat:** onsets are in
seconds keyed to a specific score/recording, not ticks — a mapping step is owed before load-bearing use.

**algomus Bach fugues** — same monorepo, `fugues/bach-wtc-i` = **23 `-ref.dez`** (of the 24 WTC-I fugues) + a
`fugues.ref` consolidated file + per-performance audio-`synchro/` JSONs (not GT). GT gives subjects/countersubjects,
cadences, pedals. → N4 + **N18** (the adopted contrapuntal/imitative GT: subjects/CS) + **N20** (fugue pedal-point labels).
**Mismatch reported:** the **12 Shostakovich fugues are NOT in the repo** (the paper's 24+12=36; the Shostakovich analyses
are website-only at algomus.fr/fugues/shosta). Bonus in the same monorepo: `jazz-arbres/treebank/treebank.json` (1170
entries — jazz harmony trees, N11/N3-adj), recorded in the `algomus_data` row.

## 3. Task 3 — figured bass (N10)

**BCFB** — `juyaolongpaul/Bach_chorale_FB` @ `431c5c019a…`, CC-BY. **Verified at data:** BCFB v2.0 = **139 chorales /
143 canonical files** (BWV 10.07/161.06/38.06/177.05 have two NBA versions) — kern **143**, mei 146, musicXML_master 248
(in-progress additions per the README); `reference_table.csv` present. Encodings: **MusicXML + `**kern` + MEI**, NBA
critical edition. → **N10** — the gate repertoire's own composer-stated harmony evidence (L4 evidence channel R-4). Also
Zenodo 5084914.

**DCMLab/figured-bass — WALKED (§7→§1 promotion).** Cloned @ `9d638f605b…` and inspected: the repo is **ONE file**
(`figured-bass.py`) + README — a bass-figure→chord **realization SCRIPT** (e.g. `-k 80 -n 5 9` → a realized second-inversion
triad), **NOT a figured-bass ground-truth corpus.** The census §7 residual ("DCMLab/figured-bass uninspected") assumed a
possible GT source; the walk finds it does **not** serve N10 as GT. Recorded (`dcmlab_figured_bass`, status=walked,
N10-NEGATIVE) so it is never re-mistaken for GT; the census §7→§1 promotion carries this finding.

**DLC `figbass` column** — registry note only (no code, per the one-change-class rule): the `_notes` clarifying clause now
records that every held DLC harmonies TSV carries a parser-dropped **`figbass`** column (inversion figured-bass, N10) and a
**`pedal`** column (N20) beside the already-noted `cadence`/`phraseend`; the parser exposure is the queued post-wave increment.

## 4. Task 4 — trees / reduction / streams (N11, N9)

**Kirlin Schenker41** — `pkirlin/schenker41` @ `3ec7eed342…`. **Access finding (mismatch):** the pinned GitHub repo
contains **only `README.md`** at HEAD *and in its entire history* (`git log --all` — the 41 MusicXML + analysis files were
never committed). The README lists all 41 excerpts (18 Mozart / 7 Haydn / 5 Beethoven / 4 Schubert / 3 Bach / 2 Chopin /
1 Handel / 1 Clementi) and points to the dissertation page `cs.rhodes.edu/~kirlinp/diss.html` for the data. → recorded as
the **classical-side N11** with the access path; data not obtained this wave (a newer 2024 set exists: arXiv 2408.07184).
`schenker41`, status=recorded.

**GTTM database** — located at `gttm.jp/gttm/database/`: **~300 melody/analysis pairs** with grouping / metrical /
time-span / prolongational / harmonic trees (MusicXML + GTTM XML). **Not pinnable cleanly:** distributed as ~157+ per-piece
ZIP archives at `gttm.jp/gttm/wp-content/uploads/2015/12/` (numbered), **no single bulk artifact, no explicit license
shown** — per the pinnable-source rule (no stable artifact) the access path is recorded and mass-download deferred
(license unclear about mirroring). → N6 + N4 + N11-melodic. `gttm_database`, status=recorded.

**protovoice-annotations — INSPECTED (the N9 gate).** `DCMLab/protovoice-annotations` @ `8ccb995e2e…`. Contents:
**38 `.analysis.json` derivations + 63 MusicXML + 5 `.piece.json`** (bach 3 / examples 2 / theory-article 33), WIP. A
`.analysis.json` is a proto-voice derivation: `topSegments` → `trans.edges` (`regular` + `passing` edges) + `rslice.notes`
(reduction slices), loadable in the DCMLab protovoice viewer; each derivation is paired with a MusicXML score (score-aligned).

## 5. Task-4.3 — the N9 (stream / implied-polyphony GT) verdict

**Usable as stream / voice-separation GT: PARTIALLY — because the derivations ARE note-level voice-connection data but
encoded as hierarchical reductions, not flat surface-stream labels, and are small (38).** In detail: the `regular` and
`passing` **edges connect individual notes** — this IS the raw material a stream/voice-separation task needs (which note
continues which line). But they encode a **hierarchical reduction** (surface → background prolongation), not a flat
per-note surface-stream/voice labelling; extracting surface streams requires a **derivation→surface-stream projection
step**. The set is also **small (38 derivations)** and WIP. **Conclusion:** protovoice-annotations is the **nearest thing
to stream GT in the entire enumeration** (bach_solo is material-only), and it is worth carrying, but it does **not by
itself close N9** — the Cowork-side N9 union search should still run, now informed by this: the search wants flat
surface-stream / voice-separation labels (Foscarin/partitura-class), for which protovoice is a partial, extraction-gated
source, not a drop-in bed.

## 6. Task 5 — When-in-Rome interior inventory (N2, N5 — exposure, no new clone)

Read-only against the already-pinned WiR clone `tools/dcml/when_in_rome` @ `aa7539f1cf…`. **Layout finding:** this pin is
**genre-reorganized** (`Corpus/{Chamber_Other, Early_Choral, Keyboard_Other, OpenScore-LiederCorpus, Orchestral,
Piano_Sonatas, Quartets, Textbooks, Variations_and_Grounds}` + a parallel `Anthology/`) — there are **no** named
`TAVERN/KMT/BPS-FH/HaydnSun` directories; the sub-corpora are folded into the genre tree. Per-slice presence verified by
mapping + counting `analysis.txt` / `analysis_B.txt` / `score.mxl`:

| audit sub-corpus | maps to (this pin) | analyses | dual `analysis_B.txt` | scores.mxl |
|---|---|---:|---:|---:|
| **TAVERN** ★ | `Variations_and_Grounds/{Beethoven, Mozart}` | 27 (17 + 10) | **27 (17 + 10 — ALL)** | 0 (analysis-only slices) |
| **HaydnSun** | `Quartets/Haydn` | 32 | 0 | 0 |
| **BPS-FH** | `Piano_Sonatas/Beethoven` | 86 | 0 | 0 |
| **WTC-I preludes** | `Keyboard_Other/Bach` | 31 | 0 | 24 |
| **OpenScore Lieder RN** | `OpenScore-LiederCorpus` | 179 | 0 | 404 |
| (DCML Mozart sonatas) | `Piano_Sonatas/Mozart` | 54 | 0 | 54 |

- **TAVERN dual = 27 A/B pairs** (Beethoven 17 + Mozart 10, each with a second-annotator `analysis_B.txt`) — **the N2
  flagship on-disk dual-annotation set**, verified.
- **Tymoczko-vs-DCML dual-annotation OVERLAP = 0** (the N2 pre-coverage number the audit could not compute). Method:
  bucket every `analysis.txt` by its RomanText **`Analyst:` line** and key by (composer, collection, movement). Analyst
  buckets across 1259 analyses: **DCML 988 / Tymoczko 419 / Gotham 161 / TAVERN-Devaney 54 / BPS 32.** Piece-key
  intersection: **Tymoczko-only 420, DCML-only 494, BOTH = 0.** Inside WiR the two analyst sets sit on **completely
  disjoint pieces** — the "Tymoczko-vs-DCML pairs" the audit listed for N2 are NOT co-located dual annotations (they would
  require cross-referencing WiR-Tymoczko pieces against the separate `tools/dcml/` corpora by identity). The only
  co-located dual annotation in WiR is the 27 TAVERN A/B pairs.
- **Audit correction (verify-at-source):** **KMT is NOT a confirmed analyzed slice at this pin.** `Textbooks/` holds
  Kostka (Tonal Harmony), Reger (Modulation), Aldwell (Harmony and Voice Leading) as **201 scores with 0 `analysis.txt`** —
  the "textbook local-key/modulation RN GT" the audit attributed to WiR is **not present as RN on disk** at `aa7539f1`.
  Flagged for Cowork (a state-column correction, not a wave STOP).

Recorded as a single additive registry row `wir_interior_inventory` (status=inventory; the smallest additive change,
Wave-2 precedent) with all per-slice counts + the overlap + the KMT correction in its `needs_coverage`. **Read-only:** no
reorganization, no re-pin, no parsing change.

## 7. Task 6 — plain-score stress material (Tier S) + craigsapp closure

**OpenScore Lieder** — `OpenScore/Lieder` @ `6b2dc542ce…`, **CC0**, `--depth 1`. Verified **1462 `.mxl` / 1352 `.mscx`**
at pin (>1,300 claim ✓). The CC0 score half of the WiR OpenScore-Lieder RN subset; best chromatic-stress bed. Not gate
material (dormant-build discipline) — held-out stress/soak.
**OpenScore StringQuartets** — `OpenScore/StringQuartets` @ `d13289cd70…`, **CC0**, `--depth 1`. Verified **122 `.mscx`**
(>100 claim ✓). The texture gap between chorales and piano (N7-material, no GT).
**ASAP** — `fosfrancesco/asap-dataset` @ `afc815c75c…`, `--depth 1`. Verified **235 `.xml` / 1302 `.mid`** (~222 distinct
romantic-piano scores). The performance MIDIs ride along but are **not our material**. Explicitly **NOT N15** (piano =
fixed intonation; the alignment is timing, not intonation — N15 ruled audio-domain / out of corpus scope).

**craigsapp closure (enumeration only — CLONE NOTHING).** `humdrum-tools/humdrum-data` is a Makefile/`.lists`-based
download interface (no `.gitmodules`). Fetched `.lists/LIST.txt` (Humdrum table, `**ghname`/`**ghrepo` columns) and
enumerated the complete manifest: **71 distinct repos across 16 GitHub orgs (821 file entries).** Highlights:
`craigsapp/*` (bach-370-chorales, beethoven/haydn/mozart/scarlatti sonatas, chopin-mazurkas/preludes, joplin),
**josquin-research-project** (22 composer repos), **TassoInMusicProject**, **SEILSdataset**, `ccarh/essen` (already held
as the Wave-2 phrase bed), `Computational-Cognitive-Musicology-Lab/CoCoPops` (onboarded this wave), and
**`DDMAL/Flexible_harmonic_chorale_annotations`** (a harmonic-chorale annotation set = N1-residual, newly surfaced). This
closes the census's named craigsapp/KernScores mechanical partial; acquisition of individual sets is NOT this wave. Full
list captured in `scratch_artifacts/humdrum_data_closure_71repos.txt` and summarised in the `humdrum_data_closure`
registry row.

**Gated / unavailable (access paths, §1–§4):** EWLD (`zenodo.org/records/1476555`, restricted — request-access form:
name/institution/role/non-commercial statement/research explanation); HookTheory full (`m-a-p/HookTheory`, HF academic
gate, CC-BY-NC-4.0, 112 GB); Sears Haydn (no public deposit); GTTM (per-piece zips, no single artifact, license unclear).

## 8. Task 8 — the idiom re-discovery trigger check (checked, NOT run)

**Trigger: FIRED — recorded only; the re-discovery run is its own protocol / future dispatch and no part of it ran here.**

The trigger fires on a *material change to the discovery-input corpora*. This wave makes available **substantial new
chord-symbol mass** that the harmonic discovery view consumes. Per-corpus reasoning (which discovery view each enters):

- **CoCoPops (628 .hum, `**harm` RN + `**kern` melody)** → **enters the HARMONIC view.** New pop/rock functional-harmony
  mass — exactly the kind of chord-symbol data idiom discovery clusters. The `**kern` melody is monophonic (no voice pairs)
  → does **not** enter the VL motion view. **Primary firing cause.**
- **OpenEWLD (486 leadsheets, chords+melody)** → **enters the HARMONIC view.** New standards/pop chord-symbol mass. Melody
  single-line → not the VL view. **Secondary firing cause.**
- **WJD native (456 monophonic jazz solos + chord metadata)** → marginal: monophonic melody (not VL); chord content is
  thin per-solo metadata. Weak harmonic-view contribution.
- **EWLD, HookTheory full** → **gated, NOT on disk** → contribute **no** material change now (records only).
- **ChoCo jazz-corpus / weimar slices** → **already held** (`corpora/ship/choco` is an existing discovery input);
  inventorying adds no new mass.
- **Lieder / StringQuartets / ASAP (note-level multi-voice scores)** → could feed the **VL motion view** if promoted to
  discovery inputs, but they were placed in `corpora/plain/` (held-out), not the discovery-input tree.
- **algomus-data, BCFB, protovoice, schenker41** → label/reduction/figured-bass GT, not chord-symbol or note-stream
  discovery inputs.

**Nuance:** the clones physically sit in `corpora/gt|plain/` (held-out), and `corpora/ship|expl/` + `idiom_discovery/` are
**byte-untouched** — so nothing auto-triggers a re-run. The trigger fires as a **recorded future action** (CoCoPops +
OpenEWLD are the new harmonic-view mass a re-discovery run should incorporate), not an automatic consequence of this wave.
Per the instruction: **record only.** The re-discovery run is its own dispatch and was not started.

## 9. Acceptance — no-contamination proof + discipline

**No `src/`, gate corpus byte-untouched.** `git status` (tracked) shows exactly the Wave-3 files: `tools/build_score_
census_registry.py`, `tools/score_census_registry.json`, `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md` (commit
`63de0df27a`) + the fold (`STATUS.md`, `COWORK_HANDOFF.md`, `cowork_score_census.md`, `cowork_census_full_needs_audit.md`,
`cc_instruction_*`, commit `8aae19f586`). **No path under `src/`; no path under `tools/corpus/`.** All bed clones are
gitignored (`git check-ignore` confirms `corpora/gt|plain/…`; the WJD `.db` too).

**Gate reproduction** (`characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}`, each "Processed 352
scores (326 with WiR coverage)"), before AND after the wave:

| preset | count | before^after (byte-stability) | set-diff vs CLAUDE.md (both directions) |
|---|---|---|---|
| Baroque | **53** | EMPTY | EMPTY ✅ |
| Jazz | **24** | EMPTY | EMPTY ✅ |
| Default | **53** | EMPTY | EMPTY ✅ |

Set-diff computed by parsing each run's "Full BIR=false enumeration" block into `stem@tick` identities and diffing
against both the pre-wave run and the authoritative CLAUDE.md sets (`scratch_artifacts/gate_setdiff.py`): **all diffs
empty.** The gate is byte-untouched — as it must be, since the wave changed no `src/` and no gate-corpus dir.

**Held-out discipline:** every Wave-3 bed is `split=held-out` (never tuned against); the WiR-interior inventory row is
`split=dev` because WiR is itself the gate GT container (inventory of an existing dev container, not a new held-out bed).
Nothing here creates or touches a held-out *designation change*; nothing is tuned against anything.

**Reuse-vs-new + what retires.**
- **Reused verbatim:** the clone + `git checkout <pin>` mechanism; the gitignored-tree hash-pin-only convention
  (`.git/info/exclude → /corpora/`); the deterministic registry generator + registry-v2 schema; the census §1 / §7
  surgical-addition form; `characterise_bir_false.py` as the gate-reproduction oracle; the REPRODUCIBILITY.md /
  score_inventory.md provenance sections.
- **New (minimal):** the `corpora/gt/` + `corpora/plain/` subtrees (under the already-excluded `/corpora/`); the registry
  `wave3_sources` section + the `needs_coverage` field + `_corpora_sha`/`_file_sha256` helpers + `wave3_rows()` in the
  generator; the census §1/§7/§8b Wave-3 markers; REPRODUCIBILITY.md + score_inventory.md Wave-3 sections.
- **Retires:** nothing.

## 10. STOP conditions — none tripped

Checked each global STOP: nothing would touch `src/` or any code (registry generator is `tools/`, not `src/`; no parser
change); the frozen gate corpus is byte-identical (§9); the gate sandwich passes; **no license situation ambiguous about
LOCAL mirroring** (all cloned beds permit a local gitignored research clone — CC0 / PD / CC-BY / ODbL; the WALKED and
gated/unavailable items were recorded, not mirrored); the Task-8 check was answered **without running any
discovery/analysis** (pure reasoning + inventory); the registry regeneration is deterministic (§0). No condition met.

Per-source failures (report lines, not STOPs): OpenEWLD 486≠502; algomus Shostakovich fugues absent; schenker41 data not
in git; Sears Haydn no public deposit; EWLD + HookTheory gated; GTTM no single artifact; DCMLab/figured-bass = tool not GT.
Each recorded precisely with its access path.

## 11. Commits (local, unpushed, fork-only)

`git add` used explicit paths only; the `cc_instruction_*` and this report are force-added per the `/cc_*.md` gitignore
convention. Per the 22j / D-L3a precedent, this report (commit #3) cites the prior commits' SHAs; its own SHA is recorded on commit.

| # | scope | SHA | files |
|---|---|---|---|
| 1 | registry `wave3_sources` + provenance | `63de0df27a` | `tools/build_score_census_registry.py`, `tools/score_census_registry.json`, `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md` |
| 2 | `docs(cowork):` fold + census Wave-3 bookkeeping | `8aae19f586` | `STATUS.md`, `COWORK_HANDOFF.md`, `cowork_score_census.md`, `cowork_census_full_needs_audit.md`, `cc_instruction_corpus_wave3.md` (-f), `cc_instruction_dl3a_closeout.md` (-f) |
| 3 | this report | (recorded on commit; force-added) | `cc_corpus_wave3_report.md` |

Nothing pushed; `upstream` push remains disabled; fork (`origin = slimvince/MuseScore`) only. The clones themselves are
gitignored/hash-pin-only — the pins live in the committed registry + this report.
