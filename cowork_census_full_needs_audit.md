# The FULL-NEEDS AUDIT — first run (Wave-3 scoping), 2026-07-04

> **Status: ★ DISPOSED (user, 2026-07-04).** §6-C rulings: **(1) N18 ADOPTED · (2) N19 ADOPTED · (3) N15
> scope ruling RATIFIED · (4) = option B, N20 pedal-point GT as its OWN needs row** (user rationale: can
> improve inference precision AND no information loss). The census §8c needs-vector + state columns carry
> the ratified updates (applied 2026-07-04, same session). The union search round (§6-D) is thereby scoped:
> N9 (after the protovoice inspection), N13, N14, N12-realized-half, N19.
>
> *(Original status: AUDIT DELIVERED, Cowork 2026-07-04, for user disposition of §6.)* First run of the census §8c
> union-of-needs mechanism, executed at Wave-3 scoping BEFORE any disposition, per the pinned queue
> (`cowork_handoff.md` START-HERE header). Offline re-scoring only — **no searching was done** (the union
> search round is §6-D, gated on this audit's ratification). Runs in parallel with the D-L3a CC dispatch;
> no shared files.
>
> **Sources read this session (live file tools):** `cowork_score_census.md` (incl. §8b/§8c),
> `cowork_score_census_gt_draft.md` (full), `cowork_score_census_plain_draft.md` (full),
> `tools/score_census_registry.json` (full: 40 DLC members + 15 other sources + 3 annotation beds),
> `cowork_candidate_lever_register.md` (R-1…R-13), `cowork_product_tool_register.md` (T/E row scan),
> and one at-source verification read: `tools/dcml/mozart_piano_sonatas/harmonies/K279-1.harmonies.tsv`
> (header row). Verification tags per the standing convention: **[verified]** = read at source this
> session; **[reg]** = from the committed registry/appendix row, not independently re-verified; **[prov]**
> = provisional, needs verification before load-bearing use.

## 1. Needs-vector currency check (before re-scoring)

**No new analysis purpose has entered the project since the vector was written (2026-07-03).** Sessions
22i/22j were metric/calibration measurement (served by N2's consumer) and the D-L3a close-out is internal
wiring — no §8b purpose-sweep is owed.

**Two consumer-register scans surfaced GT classes with named consumers but NO needs row** (proposed
additions — user disposes, §6-C):

- **N18 (proposed) — contrapuntal/imitative-structure GT** (fugue subjects/answers/countersubjects,
  imitation points). Consumers: **T-12** (counterpoint pedagogy / fugue entry detection), VL-F/VL-D
  neighborhood. The enumeration ALREADY holds candidates: the algomus Bach-fugues set (subjects,
  countersubjects, cadences, pedals — GT draft §5) and CRIM's imitation observations (plain draft §3).
- **N19 (proposed) — part-writing error/exercise GT** (graded species/part-writing exercises with marked
  errors). Consumers: **VL-H** (design-gated part-writing checker), T-12. **No candidate anywhere in the
  enumeration** — joins the union search round only if adopted.

**One verified layer with no home row:** every DLC harmonies TSV carries a **`pedal` column**
(pedal-point GT over all 40 held corpora) **[verified at K279-1 header]** — recorded here as an N4-family
note (consumer: pedal-point-span validation); a row of its own only if the user wants it.

**Deliberately NOT proposed as needs rows:** instrument-range/tessitura reference data (T-16/T-29, R-10)
— reference tables, not a corpus class.

**One correction to a [prov] reading this audit almost imported:** registry note 27 says DLC TSVs carry
"cadence/form/phraseend columns". The **`form` column is DCML chord-morphology** (label-grammar suffix:
o/+/%/M…), **NOT form/section GT** **[verified at K279-1: `form` sits between `numeral` and `figbass`]**.
N16 is NOT covered by the DLC. The same header verifies **`figbass`** (inversion figured-bass info on
every held DLC corpus) — direct N10-relevant cross-check material, exactly as lever R-4 noted.

## 2. The re-scored enumeration (audit step 2)

Notation: plain code = serves the need directly; *(adj)* = adjacent/partial (alignment, license, or
quality caveat); *(mat)* = raw material only, no GT. **★ = multi-need row** (§8c: outranks single-need
alternatives). Status from the registry where onboarded.

### 2.1 GT draft §1a — DLC (40 sub-corpora, ALL onboarded, hash-pinned) [reg]

Every member: **N1 + N4 (phraseend; cadence where counted) + N17**, plus the verified extra TSV layers
(`pedal`, `figbass`) above. Rows with coverage beyond the family profile:

| Row | Needs | Note |
|---|---|---|
| mozart_piano_sonatas ★ | N1 N4(cad) N7 N8 | The densest node: both Wave-2 beds (texture, schema) key to it. |
| wagner_overtures | N1 | + R-8 (neo-Riemannian) validation bed; Tristan capability track. |
| schulhoff_suite_dansante_en_jazz ★ | N1 N3(adj) | The only jazz-idiom row with full RN GT. |
| bach_solo | N1 N9(mat) | Implied-polyphony material (no stream GT) — VL-D dev material. |
| corelli, bach_en_fr_suites, wf_bach_sonatas… | N1 N4(cad) | Nonzero cadence counts per registry. |
| monteverdi/sweelinck/peri/frescobaldi/kleine_geistliche | N1 | Modal/pre-tonal breadth edge. |

### 2.2 GT draft §1b — DCMLab outside the DLC

| Row | Needs | Note |
|---|---|---|
| bach_chorales (DCML) | — | Scores-only (verified-negative retained); tier S, onboarded. |
| JazzHarmonyTreebank ★ | N3(adj) N11 | Trees = the §8b pending GT-layer add; the registry ALREADY carries `syntax-tree` in `gt_layers` [reg] — the census §1b table does not. Bookkeeping only. |
| choro | N3(adj) N16(adj) N17 | Chord symbols + formal structure, no engraved score. |
| schema_annotation_data | N8 | Onboarded Wave-2 bed (273 at pin). |
| protovoice-annotations ★ | N11(adj) N9(cand) [prov] | Proto-voice derivations decompose texture into voices — the nearest thing to stream GT the whole enumeration contains. Small, uninspected. §6-A inspection candidate. |
| figured-bass | N10 | §8b pending promote; uninspected. |
| debussy_piano (+8) | — | Likely scores-only [reported]; S chromatic soak. |

### 2.3 GT draft §2 — When-in-Rome (pinned, onboarded as one container) [reg]

| Row | Needs | Note |
|---|---|---|
| WiR umbrella ★ | N1 N2 N4 N5 N17 | The richest single held container. **TAVERN, KMT, BPS-FH, HaydnSun are INSIDE the pinned clone** [reg: registry content field] — Tier-G "remainder" is largely EXPOSURE (parsing/inventory), not acquisition. Per-slice presence verification rides the Wave-3 CC instruction. |
| TAVERN ★ | N1 N2 N4 | Dual analyses preserved (analysis.txt + analysis_B.txt); 1,060 phrases. The N2 flagship. |
| KMT ★ | N5 N1 | Textbook local-key/modulation/tonicization GT — the S1/S2 residual's exact shape. |
| BPS-FH ★ | N1 N4 | RN + phrase boundaries. |
| Tymoczko TAOM Bach-371 | N1 | The gate GT source (held, frozen). |
| Tymoczko misc ★ | N1 N2 | Dual-annotation pairs vs DCML (Beethoven 36 mvts; 2nd Chopin-mazurka set). |
| HaydnSun op.20 / WTC-I / Variations_and_Grounds | N1 | |
| OpenScore Lieder RN subset ★ | N1 N17 | The only large song/Lieder RN GT; chromatic-stress GT. |

### 2.4 GT draft §3 — SOTA paper tables

Method/closure evidence, not corpus rows — nothing to score.

### 2.5 GT draft §4 — ChoCo (18 partitions; container onboarded, held-out) [reg]

Audio-aligned partitions (Isophonics, JAAH, Billboard, CASD, Robbie Williams, USPop, RWC, WJD-slice) fail
the §3(b) score-alignment criterion for gate-grade use — research-tier; N17 metadata throughout. Beyond
that profile:

| Row | Needs | Note |
|---|---|---|
| Schubert-Winterreise SWD ★ | N5 N3(adj) N2(adj) | **Score-aligned local keys** (measure:beat) — an N5 source beside KMT; dual encoding vs DCML schubert_winterreise. |
| CASD (Chordify) ★ | N2 | 4 annotators/song — chord-level disagreement data (audio-aligned caveat). |
| Jazz Corpus (Granroth-Wilding/Steedman) ★ | N3 | **Harmonic-FUNCTION analyses for jazz** — rare; small (76), chords-only. |
| Rock Corpus RS200 ★ | N3 N2 | RN, 2 analysts (native set has both). |
| The Real Book | N3(adj) | 2,486 symbolic-origin; license ?. |
| Wikifonia / iReal / BiaB / Nottingham | N3(adj) N12(adj) | Symbol+melody class (see N12 verdict §3). |
| WJD (native, §6) ★ | N3(adj) N4 N16 | Jazz **phrase + form GT** — the jazz-side N4/N16. |

### 2.6 GT draft §5 — cadence/phrase GT

| Row | Needs | Note |
|---|---|---|
| DCML Mozart cadence layer | N4 | Exposed since 21k (parser reads cadence/phraseend). |
| algomus Bach fugues ★ | N4 N18(cand) | Subjects/countersubjects = the proposed-N18 footing; + pedals. |
| algomus Mozart string quartets ★ | N4 N16 | **Sonata-form structure GT — the best N16 candidate in the whole enumeration**; already AnalysisGNN-used. |
| Sears Haydn cadences ★ | N4 N2 N5 | Dual annotators + key/modulation/**pivot** annotations. |
| Essen | N6 | Onboarded Wave-2 bed. |
| MTC-ANN | N6 | + motif/similarity annotations (VL-adjacent). |
| GTTM database ★ | N6 N4 N11(adj) | Grouping/metrical/**time-span trees** — melodic-side hierarchy GT. |
| POP909 (+CL) ★ | N4 N16 N3(adj) N12(adj) | Semi-automatic chord labels (weak); phrase/section hand labels; MIDI arrangement + chords = a realized-score N12 candidate (weak). Onboarded [reg]. |

### 2.7 GT draft §6/§7 — jazz/pop + misc

| Row | Needs | Note |
|---|---|---|
| HookTheory/TheoryTab ★ | N3 N5(adj) N12(adj) | Largest key-relative pop GT; sample pinned, full HLSD pending [reg]. |
| CoCoPops ★ | N3 N12(adj) | **harm RN + kern melody, fully symbolic — the top Tier-J acquisition. |
| OpenEWLD / EWLD ★ | N3(adj) N12 | MusicXML lead sheets; OpenEWLD committable. |
| Chordonomicon | N16(adj) N17 | No scores; recorded [reg]. |
| iRb | N3(adj) | Chords-only; onboarded [reg]. |
| Kirlin Schenker41 ★ | N11 | **The common-practice tree/reduction GT counterpart to JHT** — N11's classical half, already enumerated. |
| GTTM | (see 2.6) | |
| Kostka-Payne | N1(adj) N5(adj) | Overlaps KMT conceptually. |
| UCI Bach / music21 RN | — | Superseded (recorded to stay closed). |

### 2.8 Plain draft (54 rows) — needs-relevant highlights only

The bulk is Tier S/X exactly as tiered; re-scoring changes little. Nonzero-yield rows:

| Row | Needs | Note |
|---|---|---|
| OpenScore Lieder ★ | S + N1(carrier) | CC0 score half of the WiR RN subset. |
| OS String Quartets | S, N7(mat) | Texture-gap material (no GT). |
| KernScores/craigsapp ★ | S + N1(residual) N6(adj) | Scattered **harm spines (residual-risk item 7); folk subsets. |
| JRP ★ | S | Dual editorial-accidental versions = **pitch-spelling stress** — directly relevant to the L4 notated-spelling root pin's robustness. Audit note, no needs row. |
| CRIM | N18(adj, cand) | Imitation observations (intertextual). |
| Tasso / Gesualdo / Marenzio | S | Chromatic/modal extreme-value stress. |
| ASAP ★ | S | 222 REAL MusicXML romantic piano scores (+ performance MIDI). NOT N15 (piano = fixed intonation; timing ≠ intonation). |
| PDMX | S | Rating metadata = QUALITY filter, **not difficulty** — N14 stays open. |
| Hymnary / Open Hymnal | S | Chorale-adjacent breadth beyond Bach — gate-style regression diversification. |
| DadaGP / McKenzie | N12(adj) | Realized notation + symbols, both license-grey. |
| SymbTr / jingju | — | Non-Western: closed by ruling (F-15), stays closed. |
| Lakh/MMD/GigaMIDI, MAESTRO/ATEPP/SMD/PiJAMA, YCAC, NES-MDB, RISM | — | X as tiered; nothing re-scores. |

## 3. Per-need verdicts after the audit (the transpose)

| # | Verdict | Change vs vector state |
|---|---|---|
| N1 | Well-covered, held. | none |
| N2 | **Covered ON DISK** — TAVERN (dual) inside pinned WiR + Tymoczko-vs-DCML pairs + Sears (dual, cadence) + CASD (4×, audio) + RS200 (2×). | "TAVERN queued (Wave 3)" → **acquisition already done via WiR; Wave 3 = exposure + per-slice verification** |
| N3 | Tier-J core stands (HookTheory + CoCoPops + OpenEWLD). Audit adds candidates: Jazz Corpus (function GT), WJD native (phrase/form), Real Book (license-check). | additions to the Tier-J walk list |
| N4 | Rich; jazz side now named (WJD). Plus the verified DLC `pedal` layer (pedal-point-span validation). | note added |
| N5 | Better covered than stated: KMT (on disk in WiR) + Sears pivot annotations + SWD score-aligned local keys. | state sharpened |
| N6 | Essen ✓; MTC/GTTM depth reserves. | none |
| N7 | Bed ✓; OS String Quartets future material. | none |
| N8 | Bed ✓ (273 at pin). | none |
| N9 | **GAP STANDS** — but the enumeration contains ONE candidate never scored for it: **protovoice-annotations** (small, uninspected) + bach_solo as material-only. | inspection candidate found; union search still on |
| N10 | Three-source: BCFB (pending add) + DCMLab/figured-bass (pending promote) + **verified `figbass` column on every held DLC corpus**. | coverage upgraded; Wave-3 natural |
| N11 | JHT trees held (registry layer recorded) + **Kirlin Schenker41 = the common-practice counterpart** + GTTM melodic trees. | classical-side candidate found |
| N12 | **Split verdict:** symbol+melody (leadsheet) class rich (EWLD/OpenEWLD/HookTheory/Wikifonia/Nottingham); symbol+REALIZED-score class thin (POP909 semi-auto; McKenzie/DadaGP grey). | half-covered; union search targets the realized half |
| N13 | Nothing in the entire enumeration. | union search (expect scarce — R-1 predicted rule-based shipping) |
| N14 | Nothing (PDMX ratings are quality, not difficulty). | union search (syllabus/grade mappings: ABRSM/RCM/Henle class) |
| N15 | No symbolic corpus can carry it. | **propose scope RULING: audio-domain, out of corpus scope; T-21/T-24 validate by theory/listening** |
| N16 | **Best candidate already enumerated: algomus Mozart SQ (sonata-form)**; pop-side sections (WJD/POP909/choro/Chordonomicon). DLC `form` column verified NOT form GT. | covered-by-candidate; **no search needed** |
| N17 | Held. | none |

## 4. Verified corrections & bookkeeping facts

1. **DCML `form` column ≠ form/section GT** [verified] — chord-morphology. Registry note 27's wording is
   correct but trap-prone; the census/registry edit (§6-B) should carry one clarifying clause.
2. **DLC `figbass` + `pedal` columns exist on every held corpus** [verified at K279-1] — free N10
   cross-check + pedal-point GT, currently dropped by `dcml_parser.py` (known since Wave 1).
3. **JHT `syntax-tree` layer is already in the registry** [reg] — the §8b "pending row" reduces to a
   census §1b-table note.
4. **Tier-G remainder is mostly exposure, not acquisition** — TAVERN/KMT/BPS-FH/HaydnSun live inside the
   pinned WiR clone [reg]; per-slice presence verification rides the Wave-3 CC instruction.
5. **Supersession check (intake rule):** nothing found contradicts any signed conclusion — all findings
   are enrichment-class → postpone-by-default applies; no tripwire fires.

## 5. Multi-need ranking (what §8c step 2 exists to produce)

Top multi-need nodes, by count of needs served with acquisition/exposure still owed:
1. **WiR interior walk** (N1 N2 N4 N5) — on disk; exposure only.
2. **Sears Haydn** (N2 N4 N5) — small, dual-annotator, pivot GT.
3. **algomus Mozart SQ** (N4 N16) — the N16 candidate.
4. **algomus Bach fugues** (N4 + proposed N18) — with pedals.
5. **CoCoPops** (N3 N12-adj) / **HookTheory full** (N3 N5-adj N12-adj) — the Tier-J core as ratified.
6. **WJD native** (N3-adj N4 N16) — jazz phrase/form.
7. **BCFB + DCMLab/figured-bass + DLC figbass exposure** (N10, three sources, one duty).
8. **protovoice-annotations** (N9-cand N11-adj) — inspect before any search for N9.
9. **Kirlin Schenker41 + GTTM** (N11) — research-tier reserves.

## 6. Wave-3 disposition surface (user disposes — nothing below is commissioned)

**A. Onboarding/exposure candidates** (census-mechanism entry; research-tier unless said otherwise):
the §5 ranking above, plus the ratified Tier-J core, plus Tier G/S remainder per the queue. The
protovoice inspection (A-8) is the one item that should precede the N9 union search.

**B. Bookkeeping riders** (next census/registry edit, CC-fold or Wave-3 instruction): BCFB row (N10);
DCMLab/figured-bass §7→§1 promote; JHT tree-layer note in census §1b; the `form`-column clarifying
clause; the N2/N5/N10/N11/N16 state-column updates from §3; the needs-vector additions IF ratified.

**C. Rulings sought from the user — ★ ALL RULED (2026-07-04, see status banner):**
1. Adopt **N18** (contrapuntal/imitative structure GT)? Candidates already enumerated. → **ADOPTED.**
2. Adopt **N19** (part-writing error/exercise GT)? Would join the union search. → **ADOPTED.**
3. Ratify the **N15 scope ruling** (audio-domain, out of corpus scope). → **RATIFIED.**
4. Pedal-point GT: N4-family note (default) or its own needs row? → **OWN ROW (N20)** — user: can improve
   inference precision AND no information loss; also completes the §2.15 span-kind↔needs mapping.

**D. The union search round** (§8c step 3 — runs ONLY after this audit's disposition): targeted searches
for **N9** (stream/implied-polyphony GT — after the protovoice inspection), **N13**
(ornament-realization pairs), **N14** (difficulty/grade mappings), **N12-realized-half** (chord symbols
over realized scores), plus **N19** if adopted. N16 needs NO search (candidate held). Expected side
effect (handoff note): Wave 3 likely fires the idiom re-discovery trigger via new chord-symbol mass —
the check rides the Wave-3 CC instruction as at Wave 2.

*After disposition: Cowork applies the ratified census/registry-adjacent doc edits (Cowork-owned files)
and writes the Wave-3 CC instruction just-in-time, per the one-dispatch rule (D-L3a must report first).*

## 7. POST-WAVE CORRECTIONS (Wave 3 measured, 2026-07-04 — two audit claims falsified, owned)

Both corrections come from CC's Wave-3 measurement and were **independently corroborated by Cowork at the
live WiR clone** (glob counts). Both were audit claims sourced [reg] from the registry's one-line WiR
content field — provisional readings this audit treated as stronger than they were:

1. **N2 — "Tymoczko-vs-DCML dual pairs" do NOT exist co-located inside WiR.** Measured by Analyst-line
   bucketing: piece-key overlap Tymoczko∩DCML = **0** (Tymoczko-only 420 / DCML-only 494). The genuine
   on-disk dual set is the **27 TAVERN A/B pairs** (verified: exactly 27 `analysis_B.txt`, Beethoven 17 +
   Mozart 10). Cross-CONTAINER pairs (WiR-Tymoczko × `tools/dcml/` DCML corpora) remain possible but
   require identity work — recorded as such, no longer assumed.
2. **N5 — KMT is not an analyzed slice at the WiR pin** `aa7539f1`: `Corpus/Textbooks` = 201 scores /
   **0** `analysis.txt` (verified by glob: zero matches). KMT as key/modulation GT requires its own
   acquisition — the DDMAL `key_modulation_dataset` upstream is the direct candidate (queued for the next
   corpus increment, no search needed).

Lesson recorded: a registry `content` summary is enumeration provenance, not presence-of-layers evidence —
per-slice presence must be measured (which is exactly what the wave's Task 5 was for). The census §8c
N2/N5 state columns carry the corrections.

### 7.1 WAVE-3 ADDENDUM — the two DDMAL direct pickups (2026-07-04, `cc_wave3_addendum_report.md`)

The two repos the §7 corrections above pointed at are now **acquired** — cloned + hash-pinned + walked under
gitignored `corpora/gt/`, registry rows added (`wave3_sources`), all held-out. Two rows, each entered at the
Wave-3 addendum, provenance = `cc_wave3_addendum_report.md`:

1. **N5 — `DDMAL/key_modulation_dataset` (KMT) ACQUIRED** @ `6602ae6a`. The direct-acquisition upstream the §7-N5
   correction named (KMT was NOT present as analyses at the WiR pin). Verified at data: **201 annotated Humdrum
   `.krn`** across 5 textbooks (aldwell 7 / kostka-payne 15 / reger 117 / rimsky-korsakov 37 / tchaikovsky 25),
   every file bearing a `**text` annotation spine; key/modulation encoded as Humdrum key-designation tokens
   (`*C:`, `*G:`) + inline `NEWKEY=>:RN` modulation markers, with the `**text` spines also carrying textbook-relative
   Roman numerals (N1-adj). CC-BY-SA scores / MIT code. **Mismatch reported-not-accepted:** the README "Dataset"
   checkbox list enumerates ~135 examples; the pinned repo holds 201 (living-repo growth; KP 15 = ex18-3 split
   a/b per NOTES.md). N5 primary, N1-adj, N17. This closes the N5 acquisition the correction queued.
2. **N2 — `DDMAL/Flexible_harmonic_chorale_annotations` cloned + WALKED** @ `87efd245`. Surfaced by the Wave-3
   humdrum-data closure (§7 of the Wave-3 report). **571 chorales** (371 J.S. Bach + 200 Praetorius; 572 `.krn` =
   371 + 201 Praetorius files, 130a/130b split; README says 571 — reported) with **permutational ("flexible")
   multi-reading** harmonic analyses → a candidate SECOND annotation layer over gate-class Bach chorales (N2) +
   N1-residual. **WALK finding:** the analysis GT ships as an **R-package binary** (`FlexibleChoraleHarmonicAnalysis`
   0.8.0, 6.8 MB data.table); the `kernData/` `.krn` are **`**kern`-only scores (verified 572/572)** — no analysis
   spine. GPLv3. **⚠ RECORD-ONLY this dispatch:** its 371 Bach chorales overlap the gate repertoire (Breitkopf/Dörffel
   371 Four-Part Chorales, KernScores lineage = the music21 gate corpus's works); it must NOT be wired to /
   compared against / bulk-diffed with the gate corpus — any use over gate pieces is a future **user** ruling
   (census §4 dedupe / the M3 contamination lesson). The 200 Praetorius chorales are new and outside the gate.

*(Bookkeeping-location note: the addendum instruction said "Census §1: two rows"; the two rows land here in this
§7.1 addendum — the fold-list-designated §7 corrections home — plus the census §8c N2/N5 state-column updates and
the two `wave3_sources` registry rows. Relocate if a different home is preferred.)*
