# The union search round — record (census §8c step 3, first run; 2026-07-04)

> **Status: ★ DISPOSED (user, 2026-07-04) — §6 items 1–5 ALL APPROVED:** (1) N9 acquisitions
> (piano_svsep + MCMA + vocsep research-tier) go into the next corpus dispatch; (2) the N13 negative is
> a ratified ruling (R-1 ships rule-based/unvalidated; Batik heuristic parked; Batik-plays-Mozart
> itself = intake candidate); (3) N14: Mikrokosmos acquires now, CIPI via the Zenodo request (USER
> ACTION: the access form), PSyllabus recorded, the T-32 commercial caveat recorded in the product-tool
> register; (4) the PDMX `<harmony>` counting pass + GuitarSet approved; (5) the N19 build-not-download
> ruling is ratified — construction owned by VL-H's design gate (seeds: Dahn 46 + F&C 18 + synthetic).
> The acquisition dispatch is written just-in-time AFTER the active Wave-3 addendum reports + ratifies.
>
> *(Original status: DELIVERED, for user disposition of §6.)* The targeted searches the
> disposed FULL-NEEDS AUDIT scoped: **N9** (stream/voice-separation GT), **N13** (ornament-realization
> pairs), **N14** (difficulty/grade labels), **N12-realized-half** (chord symbols over realized scores),
> **N19** (part-writing error GT). Run as five parallel deep-search agents (web only, no local files);
> **[verified] tags are the agents' (primary page fetched)** — per the census convention, every claim is
> re-verified at acquisition. Negatives are recorded so they are never re-searched. This doc is the
> census-grade record; findings enter the census/registry only via a future acquisition dispatch.

## 1. N9 — stream / voice-separation GT: the GAP is now materially smaller

The audit-era negative ("no candidate found") is **superseded for notated polyphony** and **confirmed for
implied polyphony**:

| find | what it is | size | fit |
|---|---|---|---|
| **piano_svsep (CPJKU, ISMIR 2024)** | per-note **voice + staff + chord** GT graphs over DCML-corpus piano scores (cross-staff voices included) — the SOTA voice-separation task set; labels over scores WE ALREADY HOLD (the Wave-2 pattern again) | 393 pieces (77 test) | **best fit** [verified] github.com/CPJKU/piano_svsep (code MIT; underlying DCML licenses per-repo; the companion "jpop" 811-score set is explicitly NOT public) |
| **MCMA** | Baroque contrapuntal works hand-"exploded" one-voice-per-track (incl. keyboard fugues) | ~475 files | flat per-note voice GT; license **CC-BY-NC-SA-4.0 — corrected at the repo LICENSE at acquisition** (the search agent's "CC BY 4.0 [verified]" came from the docs site, superseded; NC matters for T-32) — mcma.readthedocs.io |
| **vocsep_ijcai2023 (IJCAI 2023)** | chorales/WTC/Inventions/Haydn-quartet note graphs with per-note voice links | 1,054 graphs | notation-derived (weaker as inference GT except WTC) [verified] github.com/manoskary/vocsep_ijcai2023 |
| de Valk lute data / JosquIntab | per-note voice labels on 16th-c. lute TABLATURE (notation carries no voices → true annotation) | 64+? pieces | niche texture, genuine labels [verified/reported] |

**Negatives (do not re-search):** implied-polyphony GT over monophonic instruments — CONFIRMED ABSENT
(VoiSe 2005 and Gray & Bunescu's perceptual-stream pop corpus were never released; VISA excerpt sets not
public; Chew&Wu/Guiomard-Kagan reused notated voices). Caveat to carry: piano_svsep/vocsep labels
originate from engraved notation — for piano, engraving-voice ≈ the inference target (the SOTA field
accepts this), but say so at intake.

> **ACQUISITION ROUND (2026-07-04, `cc_acquisition_round_report.md`) — all three ACQUIRED + pinned + verified:**
> **piano_svsep** ACQUIRED @ `1462e7c28d…` (MIT code); verified at data — the repo ships CODE, and its GT
> graphs are FETCHED AT RUNTIME from `github.com/fosfrancesco/piano_corpora_dcml` (pin = the code repo; the
> actual per-note voice+staff GT is a follow-on pin at that fetch path). `jpop` re-confirmed non-public
> (README + `MusescoreJPopDataset` docstring). **MCMA** ACQUIRED @ `2bdb12e233…`; 475 `.mxl` verified, track
> split **153 two / 239 three / 83 four-plus RE-COUNTED at the data** (= the record's 239/153/83). ★ **License
> CORRECTED: CC-BY-NC-SA-4.0, not the record's "CC BY 4.0"** (NC clause matters for T-32). **vocsep_ijcai2023**
> ACQUIRED @ `82152a9591…`; ships CODE, ~1,054 graphs BUILT AT RUNTIME from bach-370-chorales + Haydn/Mozart SQ
> + MCMA loaders. ★ **License CORRECTED: MIT, not "unstated".** All held-out.

## 2. N13 — ornament-realization pairs: negative essentially CONFIRMED; two build-paths named

No symbol→realization dataset exists. Nearest assets:

- **Batik-plays-Mozart** [verified at file level] — 12 Mozart sonatas, performance MIDI note-aligned to
  the score, `trill-mark`-anchored score notes with the realization notes adjacent as UNLABELED
  insertions → trill realizations are **recoverable by a small grouping heuristic**, not shipped as
  pairs. ★ Multi-need at intake: the corpus also carries **harmony + cadence annotations** (N1/N4) —
  github.com/huispaty/batik_plays_mozart, license ?.
- The **match file format** defines exactly the needed `trill(Anchor)-note` link type [verified spec],
  but the public corpora don't populate it (the ones that did — Magaloff/Zeilinger — are rights-locked).
- Historical parallel sources (Corelli op.5 Walsh-1725 "Graces"; Bach's written-out sarabande
  agréments) exist only as scans — a small in-house encoding project, not a download [verified negative
  on existing encodings].
- ASAP confirmed negative (ornaments are an alignment error source there, never segmented).

**Consequence:** R-1's prediction stands — ornament expansion ships rule-based with the
empirically-unvalidated mark; optional cheap validation = the Batik heuristic extraction (a future
read-only measurement) or the small encoding project (park unless prioritized).

> **ACQUISITION ROUND (2026-07-04) — Batik-plays-Mozart ACQUIRED @ `30256ca48f…`** (multi-need intake). Verified
> at the data: 36 movements / 12 Mozart sonatas; harmony/cadence/phrase GT materialized as `score_parts_annotated/`
> CSVs (N1: `_spart_harmony.csv` full DCML columns globalkey/localkey/numeral/chord_type; N4: `_spart_cadence.csv`).
> **N13-partial trill structure VERIFIED on `kv279_1.match`:** 49 score notes bearing the `trill-mark` attribute +
> 163 `insertion` lines → trill realizations recoverable by a grouping heuristic (NOT shipped as pairs; **no
> extraction built**, per the dispatch). The `annotations/` dir is an unpopulated git submodule (the upstream DCML
> Annotated Mozart Sonatas — which we already hold; recorded, never wired to the gate). No LICENSE file → hash-pin-only.

## 3. N14 — difficulty/grade labels: real datasets exist; license posture is the open risk

| find | labels | scores? | size | access |
|---|---|---|---|---|
| **CIPI** (Ramoneda) | Henle 1–9, expert-verified | **MusicXML included** | 652 pieces | Zenodo GATED (request form, research-only) [verified] |
| **Mikrokosmos-difficulty** | 3 classes (composer/publisher-derived) | MusicXML in repo | 147 | open repo, no license file [verified] |
| **PSyllabus** | unified 11-level scale from real exam-board syllabi (ABRSM/RCM/Trinity…) | NO (audio+MIDI) | 7,901 recordings | Zenodo, CC-BY badge but "research use only" text [verified] |
| PS/FS (PDF-difficulty) | 9/5 levels | images only (OMR needed) | 2,816+4,193 | Zenodo [reported] |
| pianosyllabus.com | multi-board piece→grade | no | >28,000 entries | website, no API/dump; scraping rights ? [verified site] |
| PDMX `complexity` | MuseScore auto-metric 0–3 | yes (held) | ? non-null | weak labels, not pedagogical [verified] |

**Negatives:** no machine-readable ABRSM/RCM/Trinity syllabus, no Henle dump, no violin/guitar grade
dataset. **T-32 caveat recorded:** every real label source is research-only/proprietary at origin — a
COMMERCIAL grading feature needs a license path or own labels; CIPI+Mikrokosmos suffice for research
validation.

> **ACQUISITION ROUND (2026-07-04) — Mikrokosmos ACQUIRED @ `f77aebc1d4…`** (147 MusicXML verified; henle
> 3-class difficulty labels in `metadata/mikrokosmos_metadata.csv`; splits.json CV folds; **no LICENSE file** →
> hash-pin-only). **CIPI recorded GATED** (Zenodo `8037327`; request-access, research-only — **USER ACTION: the
> access form is still pending**; lands on grant). **PSyllabus recorded** (Zenodo `14794592`; 7,901 recordings,
> audio/MIDI only, **no symbolic scores** → N14-adj). T-32 commercial caveat now rides the product-tool register.

## 4. N12 realized-half — one big lever we ALREADY HOLD + one small clean add

- **★ PDMX harmony-filter [verified feasible]:** PDMX (held, PD, 250k MusicXML incl. the raw `.mxl`)
  preserves MuseScore chord symbols (a dedicated `ChordSymbol` class in its reader; `<harmony>` elements
  in the mxl). Nobody has published the chord-symbol-bearing subset size — **a local read-only counting
  pass over our held copy** (filter `<harmony>` + multi-voice texture) is the cheap measurement that
  turns this into the largest symbols-over-realized-texture bed anywhere. No new acquisition needed.
- **GuitarSet** [verified] — 360 excerpts, instructed-chart chord vs performed polyphonic comping
  (audio/JAMS domain), CC-BY 4.0 — a small clean validation pair set.
- FiloBass [reported] — symbols + verified bass lines (single voice — near-miss; bass/inversion channel
  value only).
- **Negatives:** Open Hymnal has realization but NO chord symbols (sampled ABC verified); no cleaner
  Doug-McKenzie-class jazz set exists; hymnal/CCLI world is copyrighted; no published PDMX
  harmony-subset derivative exists (the filter is novel work).

> **ACQUISITION ROUND (2026-07-04) — GuitarSet ACQUIRED; PDMX counting pass STOPPED.** **GuitarSet:** the
> ANNOTATION artifact `annotation.zip` downloaded + **sha256-pinned** `8daa02e6417ccca1685feb44b135e95928ad7037e5032ecb326b5791856fda99`
> (39.1 MB, CC-BY-4.0); **360 `.jams` verified** (comp/solo variants = instructed-chart vs performed-comping);
> the 4 audio zips (657 MB–3.61 GB) recorded, NOT downloaded. **★ PDMX `<harmony>` counting pass ATTEMPTED +
> STOPPED (Task-3 STOP, correctly reported — NOT a wave stop):** the HELD form is **metadata-only** — `tools/pdmx/PDMX.csv`
> (a 250k-row index) + derived `jazz_candidates.csv` + 5 spot-check `.mxl`. It has **NO chord-symbol column**
> (`n_annotations`/`has_annotations` conflate all annotation types — chord symbols + dynamics + tempo + text;
> `tracks` = instrument-program codes), and the raw MXL (`mxl.tar.gz`) + per-score MusicRender JSON live ONLY in
> the Zenodo archive, not on disk. Counting `<harmony>`/`ChordSymbol` would require fetching `mxl.tar.gz` + parsing
> per file (a re-download/acquisition = a **future user decision**), which the read-only, do-not-re-download
> dispatch forbids. **No proxy invented; the symbol-bearing multi-voice subset stays UNMEASURED** (the lever's
> feasibility is unchanged — the *held form* is simply the wrong artifact to measure it from).

## 5. N19 — part-writing error GT: confirmed BUILD-NOT-DOWNLOAD; validation seeds found

No exercise+error-label dataset exists publicly (Harmonia and Artusi hold exactly this data internally,
commercially closed; every academic checker shipped software, not labeled corpora). What exists:

- **Real-music positive seeds [verified]:** Luke Dahn's manuscript-checked list of ALL 46 consecutive-5th/8ve
  instances in the ~410 Bach chorales (categorized: 26 fermata / 13 NCT / 7 chordal), + Fitsioris &
  Conklin's 18 machine-found genuine parallel-5th passages — HTML/PDF, small transcription job, gives a
  true-positive set on the gate repertoire's own style.
- **The synthetic route (every checker precedent's internal strategy):** mutate correct solutions (Fux
  sample files, Sposobin-style solution banks, chorales) and auto-label the injected violation.
- Category-(b) tooling precedents recorded for VL-H's design: music21 theoryAnalyzer, FuxCP, Palestrina
  Pal, Check-Fux plugin, Harmonia/Artusi (commercial demand evidence).

**Consequence:** VL-H's validation GT is a construction task owned by VL-H's design doc (the two routes
above), not a census acquisition. Record in the VL-H design gate when it opens.

## 6. Disposition surface (user disposes; nothing commissioned)

1. **N9 acquisitions** (next corpus addendum): piano_svsep (+ its GT graphs over our held DCML scores) +
   MCMA (license corrected at acquisition: CC-BY-NC-SA) [+ vocsep_ijcai2023 as research-tier]; implied-polyphony stays a recorded gap (VL-D
   design decides whether notated-voice GT suffices for v1).
2. **N13 ruling:** accept the confirmed negative — R-1 ships rule-based/unvalidated as predicted; park
   the Batik heuristic extraction as an optional future measurement (also intake Batik-plays-Mozart
   itself: multi-need N1/N4 + the N13-partial).
3. **N14 acquisitions:** Mikrokosmos (open) now; CIPI via the Zenodo request (user action needed for the
   form); PSyllabus recorded; the T-32 commercial-license caveat rides the product-tool register.
4. **N12 measurement:** a read-only PDMX `<harmony>`-count pass over the HELD copy (cheap CC task;
   measurement, no inference) + GuitarSet acquisition (small).
5. **N19 ruling:** accept build-not-download; the Dahn/F&C seed transcription + synthetic-violation
   corpus become VL-H-design-owned tasks; census records the negative.
