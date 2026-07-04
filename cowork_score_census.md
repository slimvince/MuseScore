# The score & corpus census — once-and-for-all, enumerated to closure

> **Status: v1 DELIVERED (Cowork, 2026-07-02); for user disposition of the acquisition tiers (§5).**
> The definitive census of obtainable symbolic scores and harmonic ground-truth corpora, built to end the recurring
> "we discovered another corpus" pattern (latest instance: DCML `wagner_overtures`, found only during the 2026-07-02
> architecture review). Full evidence tables live in the two appendix drafts, produced by parallel deep-research
> agents 2026-07-02 and retained verbatim:
> **`cowork_score_census_gt_draft.md`** (annotated GT corpora — ~101 rows, ≈85 distinct after cross-container dedup)
> and **`cowork_score_census_plain_draft.md`** (plain-score collections — 54 rows, ≈52 collections).
> Facts therein are marked **[verified]** (page fetched) vs **[reported]** (snippet-level; re-verify before
> load-bearing use), per the verify-at-source rule.

## 1. Why corpora kept being "discovered" — and the method that closes it

Every previous hunt was **keyword-driven sampling**: search, take good hits, stop when the current question was
answered. That finds exemplars, never closure. This census instead **enumerates containers to their end**:

| Container class | Closure state (v1) |
|---|---|
| DCMLab GitHub org — **127 repos**, incl. `distant_listening_corpus` (**40 submodules** — the census's original "41" was an overcount, corrected at Wave-1 onboarding from the live `.gitmodules`, 2026-07-02), `dcml_corpora` (12), `romantic_piano_corpus` (9); also `schema_annotation_data` (voice-leading-schema GT over Mozart sonatas) | **Fully enumerated** [verified; Wave-1 ONBOARDED — all 40 present, hash-pinned, registry v2 `tools/score_census_registry.json`] · [Wave-2 ONBOARDED the DCMLab-org `schema_annotation_data` **annotation bed** — see `cc_corpus_wave2_report.md`] |
| When-in-Rome meta-corpus — full component list | **Fully enumerated** |
| ChoCo — all 18 partner datasets | **Fully enumerated** |
| SOTA-paper dataset tables (AugmentedNet / RNBert / AnalysisGNN / ChordGNN — the field's de-facto RN-GT census; AnalysisGNN's list = 1,719 pieces) | **Fully harvested** (AugmentedNet exact manifest partial) |
| OpenScore family, Mutopia, KernScores highlights, MuseData, early-music projects (JRP/CRIM/Tasso/Marenzio/CMME), Wikifonia→EWLD lineage, Lakh→MetaMIDI→GigaMIDI lineage, main folk containers (Essen, MTC, Nottingham) | **Fully enumerated** [Wave-2 ONBOARDED the Essen `ccarh/essen-folksong-collection` **phrase-boundary bed** (Humdrum kern) — see `cc_corpus_wave2_report.md`] · [Wave-3 ONBOARDED `OpenScore/Lieder` (1462 mxl, CC0) + `OpenScore/StringQuartets` (122 mscx, CC0) plain-score stress + `fosfrancesco/asap-dataset` (235 MusicXML); the KernScores/craigsapp mechanical partial CLOSED by enumerating `humdrum-tools/humdrum-data` = 71 repos/16 orgs (cloned nothing) — see `cc_corpus_wave3_report.md`] |
| **algomus / Dezrann** (algomus.fr GitLab org + dezrann.net) — symbolic-music analysis annotation datasets (texture, cadence, form) | **Enumerated** [Wave-2 ONBOARDED `symbolic-texture-dataset` (Couturier et al. ISMIR 2022) as an **annotation bed**; moved here from §7 residual risk — see `cc_corpus_wave2_report.md`] · [Wave-3 ONBOARDED `algomus.fr/algomus-data` monorepo: `quartets/mozart` (32 sonata-form ref.dez — the N16 candidate), `fugues/bach-wtc-i` (23 subject/CS/cadence/pedal ref.dez — N4/N18/N20; the 12 Shostakovich fugues are website-only, NOT in-repo), `jazz-arbres` treebank (1170; N11/N3) — see `cc_corpus_wave3_report.md`] |
| **Tier-J jazz/pop analysis GT** (CoCoPops, EWLD/OpenEWLD, HookTheory, Weimar Jazz Database, ChoCo jazz/weimar slices) | **Enumerated** [Wave-3: ONBOARDED `CoCoPops` (628 .hum, **harm+**kern), `00sapo/OpenEWLD` (486 PD .mxl), the native WJD SQLite (456 solos, ODbL, sha256-pinned), + INVENTORIED the ChoCo jazz-corpus (160 jams) / weimar (916 jams) slices; **GATED, access path recorded:** EWLD (Zenodo request-access), HookTheory full (HF academic gate) — see `cc_corpus_wave3_report.md`] |
| **Figured-bass / trees-reduction GT** (BCFB, DCMLab/figured-bass, Kirlin Schenker41, GTTM, protovoice-annotations) | **Enumerated** [Wave-3: ONBOARDED `juyaolongpaul/Bach_chorale_FB` (BCFB, 139/143, N10) + `DCMLab/protovoice-annotations` (38 derivations — the N9 gating inspection); `pkirlin/schenker41` pinned but README-only (data at the dissertation page); GTTM located (no single artifact); **`DCMLab/figured-bass` WALKED = a realization SCRIPT, not a GT corpus** (§7→§1) — see `cc_corpus_wave3_report.md`] |
| Partial: per-repo DLC piece counts; MuseScore.com beyond PDMX (ToS-unwalkable); CPDL/IMSLP symbolic subsets; craigsapp's ~100 kern repos (closure tool exists: `humdrum-tools/humdrum-data`); abcnotation.com long tail | **Named, bounded** |

**The standing process rule this census institutes:** from now on, *"a new corpus was discovered" is a census
defect* — the fix is to add its **container** to the table above and re-enumerate that container to closure, not to
ingest one repo and move on. **Re-sweep cadence: yearly** (new ISMIR proceedings + the `mirdata` loader list + the
`ismir/mir-datasets` index are the mechanical catch-alls), and at any Stage-5/6 corpus decision.

## 2. What the census found — the headline

- **The single biggest untapped asset requires zero new tooling** *(✅ EXECUTED, Wave 1, 2026-07-02)*: the project
  used **10** of the DLC's **40** DCML sub-corpora (plus the standalone `bach_chorales`, not a DLC member — Wave-1
  correction); the **other 30** — now onboarded, 30/30 parse-clean — are format-identical to what `dcml_parser.py`
  already parses — including
  `beethoven_piano_sonatas` (all 32), `wagner_overtures`, `liszt_pelerinage`, `rachmaninoff_piano`, `scriabin`-era
  chromatic material, `monteverdi_madrigals`/`sweelinck_keyboard`/`peri_euridice` (pre-Baroque), `scarlatti_sonatas`,
  `bartok_bagatelles` (20th c.), and `schulhoff_suite_dansante_en_jazz` (a jazz-idiom art-music set — directly
  relevant to the Jazz preset). Style span extends from ~1600 to ~1930 in one format.
- **Cadence/phrase GT exists and we use none of it:** the algomus Bach WTC-I fugue cadences (36 fugues, 1,000+
  labels), the algomus Mozart quartet sonata-form+cadence set, the Sears Haydn-quartet cadence set (dual annotators)
  — plus **cadence labels already inside the DCML Mozart-sonatas TSVs the project has cloned** (a free win; feeds the
  L5 §5.2 detector's validation and the L4 rotation-pinning).
- **RN-GT with phrase/annotator-disagreement data:** BPS-FH (Beethoven sonatas, RN + phrase boundaries), TAVERN
  (1,060 phrase-level analyses, **two annotators each** — the best calibration data for the A-1 Class-P reliability
  fitting and the tonicization-band evaluation policy), HaydnSun op.20.
- **Key/modulation GT aimed at our exact residual:** KMT (Key Modulations & Tonicizations, textbook-authoritative
  local-key GT, inside When-in-Rome) — squarely the key-disagreement class (S1/S2).
- **Pop/jazz harmony with score-side alignment (the gate-grade jazz want):** HookTheory/TheoryTab (tens of thousands
  of key-relative, RN-convertible crowd annotations), CoCoPops (RS200 + McGill unified into Humdrum `**harm`, 414
  transcriptions), EWLD/OpenEWLD (502 PD lead sheets, native MusicXML + chords) + Charlie Parker Omnibook.
- **Plain-score stress/soak material:** OpenScore Lieder (1,300+ late-romantic songs, CC0, proofread, mscx→MusicXML
  pipeline — the best chromatic stress bed), OpenScore String Quartets (CC0, texture gap between chorales and piano),
  KernScores/craigsapp classical sets, PDMX (250k PD MusicXML for scale testing, quality-filterable by its rating
  metadata).
- **Two verified negatives worth recording:** DCMLab/`bach_chorales` (358 scores) carries **no harmony labels** — the
  Bach-chorale RN GT is the Tymoczko/WiR set the project already uses (consistent with `score_inventory.md`); DIAMM
  is image-only (closes the early-music class).

## 3. Inclusion criteria (what "a corpus we can use" means)

A source enters the registry only with all five fields decided: **(a) GT type** (RN / chords / key / cadence /
phrase / none); **(b) machine-readable score alignment** (symbolic score + annotation anchored to it — chords-only or
audio-aligned sets are research-tier at best); **(c) format** (parseable today vs converter needed); **(d) license
class** (PD/CC0/CC-BY committable; NC/unclear → hash-pin-only, the established mechanism); **(e) decision tier** (§5).

## 4. Overlap hazard (the accounting rule)

The containers re-encode the same works (WiR↔DCML↔ChoCo; KernScores↔craigsapp↔music21↔MuseData; GigaMIDI absorbs
Lakh/MetaMIDI). **Dedupe by work, not by container** — the registry keys on (composer, work, movement), and a work
entering the gate corpus from one container is excluded as GT from every other (the M3 contamination lesson,
generalized).

## 5. Decision tiers (proposed; user disposes)

- **Tier G (gate-candidate GT):** the unused DLC sub-corpora (chromatic/romantic first: beethoven_sonatas,
  wagner_overtures, liszt, rachmaninoff); KMT; BPS-FH; TAVERN. Enter as research-tier; promotion to any gate is its
  own ratified re-baseline event (engage-criteria discipline).
- **Tier J (the jazz/pop GT path, per the 2026-07-02 ratification):** HookTheory (RN-convertible) + CoCoPops +
  OpenEWLD as the score-aligned core; JHT/iRealPro/McGill stay research-tier where alignment is weak.
- **Tier C (cadence/phrase GT):** the DCML Mozart cadence labels (already on disk!), algomus ×2, Sears — validation
  beds for L5 §5.2 and the L1.5 primitive.
- **Tier S (plain-score stress/soak):** OpenScore Lieder + String Quartets, KernScores classical sets; PDMX for
  scale; the Tristan Prelude specifically via `wagner_overtures` (presence to confirm at clone time).
- **Tier X (recorded, not pursued):** performance-MIDI aggregates, image-only, audio-aligned-only sets — listed in
  the appendices with reasons, so they are never "re-discovered".

## 6. Implementation (CC riders — not this doc's work)

1. Extend `tools/corpus_registry.json`/`extra_scores_registry.json` to the §3 schema (one entry per census row,
   decision tier + license + alignment fields); the census appendices are the source of truth for v1 population.
2. The corpus-expansion CC instruction (roadmap block): clone + hash-pin the ratified Tier-G/J/C/S sets via the
   established REPRODUCIBILITY mechanism; confirm Tristan-Prelude presence in `wagner_overtures`; report per-corpus
   piece counts (closing the census's "?" cells).
3. Add the yearly re-sweep to the maintenance notes (mirdata loaders + ismir/mir-datasets + new ISMIR proceedings).

## 7. Residual risk (named, so it is bounded)

Zenodo/university-hosted annotation sets without GitHub presence (more algomus/Dezrann material — the algomus/Dezrann
container is now an **enumerated §1 row**, with `symbolic-texture-dataset` onboarded at Wave 2 **and the
`algomus-data` monorepo (Mozart-quartet sonata-form + Bach-fugue) onboarded at Wave 3**; the Shostakovich fugues +
any remaining cadence/form sets stay in this residual bucket), figured-bass
corpora (**`DCMLab/figured-bass` WALKED at Wave 3 = a figured-bass REALIZATION SCRIPT, not a GT corpus — §7→§1
promoted with that finding; the actual figured-bass GT is BCFB, onboarded Wave 3, plus the parser-dropped DLC
`figbass` column**), scattered Humdrum `**harm` spines on kern.ccarh.org (**now enumerated: the
`humdrum-tools/humdrum-data` manifest = 71 repos/16 orgs, incl. `DDMAL/Flexible_harmonic_chorale_annotations` — Wave-3
closure, cloned nothing**), national-library MEI
editions, the ABC long tail, non-Western symbolic sets (SymbTr, jingju), and 2025–26 releases (POP909-CL surfaced
mid-census). Each is a container-class now on the §1 list — the yearly re-sweep walks them; none is expected to hide
gate-grade common-practice RN GT (that class is closed by the SOTA-paper harvest).

## 8. The comprehensiveness claim, precisely stated — and the mitigation plan (added 2026-07-02, user question)

**What the census can prove:** closure **over the enumerated container classes** (§1). **The strong claim:**
gate-grade common-practice RN/harmony GT is **citation-closed** — the field is small and cross-citing, so every
serious GT corpus is used by a SOTA paper, aggregated by WiR/ChoCo, or indexed by mirdata/awesome-lists within ~a
year of release; a corpus outside all of those is almost certainly not gate-grade. **The bounded (not closed)
claim:** plain-score collections and peripheral/niche GT — the risk lives in **unknown containers** (Zenodo-only
deposits, national-library editions, non-English sources, brand-new releases), which no enumeration can prove absent.

**Why some sources are deliberately not fully enumerated:** (a) **unwalkable** (MuseScore.com ToS beyond PDMX; IMSLP
= PDF scans without a symbolic index) — cost exceeds value, content mostly non-machine-readable; (b) **mechanically
closable later** (craigsapp via `humdrum-tools/humdrum-data`; DLC piece counts at clone time) — closure rides the
acquisition instruction; (c) **snippet-verified rows** ([reported] marks) — a budget choice made visible, verified at
acquisition; (d) **out of analytical scope by decision** (non-Western symbolic sets — the tonal model class does not
cover them; review F-15) — closed by ruling, not enumeration.

**Mitigations (each cheap, each catching a different miss mode):**
1. **Citation-closure sweep** — harvest the dataset/related-work sections of the *citing* papers of the four SOTA
   systems (Semantic Scholar cited-by walk) + each new ISMIR/TISMIR proceedings; this is the mechanism that catches
   any GT corpus the moment the field first uses it.
2. **Index subscriptions** — the yearly re-sweep (§1) pinned to concrete indexes: the `mirdata` loader list, the
   `ismir/mir-datasets` repo, Zenodo/OSF keyword alerts ("Roman numeral annotation", "cadence dataset", "harmonic
   analysis corpus"), Hugging Face datasets search. Catches index-only releases GitHub misses.
3. **One community query round** — the WiR README maintains its own curated corpus list (a census to DIFF against,
   cheap cross-validation); a short ask to the DCML / When-in-Rome / music21 maintainers ("what exists that we
   missed?") catches private/in-progress sets no index has. Highest catch-rate per unit effort for unknown unknowns.
4. **Verification rides acquisition** — every [reported] row is verified at the moment it is cloned/pinned (the CC
   corpus-onboarding instruction), so the verification debt never needs a separate campaign.
5. **Close the mechanical partials** in the same instruction (craigsapp closure; DLC counts; AugmentedNet manifest
   from its repo).
6. **Scope rulings recorded** — each class excluded by decision (non-Western; performance-MIDI; image-only) carries
   its reason in the appendix tables, so exclusion is auditable and reversible, never a silent omission.

## 8b. The recurring-discovery finding, and the PURPOSE-DRIVEN sweep trigger (user observation, 2026-07-03)

**The observation (user):** several times we believed the corpus search was complete, and each time later work
surfaced more — the pattern has repeated enough to be a process fact, not bad luck.

**Why it happens (diagnosed, two mechanisms — neither is a §8 failure, but §8 alone does not prevent them):**
1. **Containers are walked lazily by design.** Closure is over container CLASSES; the contents surface only when
   a wave walks the container (the Wave-2 beds all lived inside §1/§7 rows: `schema_annotation_data` inside the
   already-enumerated DCMLab org; the algomus texture set inside the §7 algomus/Dezrann residual; Essen inside
   the folk-containers row). These are census WALKS, not census misses — but they *feel* like discoveries.
2. **Topic-blind enumeration cannot see purpose-specific GT.** The census enumerated with the HARMONIC axis's
   questions in mind. When a NEW purpose appeared (axis 2: texture / phrase / schema / stream GT; the lever
   sweep: figured bass, hierarchical trees), targeted per-duty searches immediately surfaced material the
   enumeration had no reason to rank (BCFB; the JHT's *tree* annotations as a distinct GT layer over an
   already-held source). A census is only as complete as the list of questions it was asked with.

**The standing trigger instituted (complements the yearly re-sweep + the wave triggers):** whenever a **new
analysis purpose** enters the project — a new axis, a new component with a GT need, a new lever class — a
**targeted, purpose-specific census sweep runs for that purpose** before its design doc is signed (the axis-2
§6b sweep is the founding precedent: three census-grade finds in one pass, two on corpora already held). The
sweep's finds enter via the census as always; "we already enumerated the container" does not discharge the duty
to ASK THE NEW QUESTION against it.

**Pending container/GT-layer additions from the 2026-07-03 sweeps (for the next census/registry edit — Wave-3
natural home):** BCFB (Bach Chorales Figured Bass, ISMIR 2020 — figured-bass GT on the gate repertoire);
the **JHT hierarchical tree annotations** as a distinct GT layer (the JHT source is already held as research
material; its trees are a separate annotation layer for lever R-7); `DCMLab/figured-bass` (already a §7
residual — promote to a walked row at Wave 3). *(The Wave-2 beds are already onboarded/enumerated.)*

**★ ALL THREE EXECUTED AT WAVE 3 (2026-07-04, `cc_corpus_wave3_report.md`):** BCFB onboarded (`juyaolongpaul/Bach_chorale_FB`,
139 chorales / 143 files, MusicXML+kern+MEI — registry `wave3_sources.bcfb`, N10); the **JHT `syntax-tree` GT layer** was
already registry-recorded (`other_sources.jazz_harmony_treebank.gt_layers = ["chords","syntax-tree"]`, N11) — this note
records that fact (the census §1 prose never carried it; bookkeeping only); `DCMLab/figured-bass` **WALKED and §7→§1
promoted** — the walk found it is a figured-bass REALIZATION SCRIPT, **not a GT corpus** (registry `wave3_sources.dcmlab_figured_bass`,
status=walked, N10-NEGATIVE). Each Wave-3 row is marked "entered at Wave 3, provenance `cc_corpus_wave3_report.md`" in the
registry `wave3_sources` array.

## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)

**The question that created this section:** is a corpus search useful that is NOT driven by one architectural
need — the "need" being the sum of all needs? **Answer: yes, but the search is step 3 of 3.** The sum of all
needs must first exist as an artifact, and once it does, re-scoring the EXISTING enumeration against it is
cheaper and likely higher-yield than new searching (the Wave-2 lesson: the finds were already inside enumerated
containers — the dismissals were purpose-relative, made with harmonic-axis eyes only).

**★ FIRST RUN EXECUTED + DISPOSED (2026-07-04):** the audit ran at Wave-3 scoping per this section — full
record + per-row scoring: `cowork_census_full_needs_audit.md`. User rulings at disposition: **N18/N19/N20
ADOPTED** (N20 rationale, user: improves inference precision AND no information loss), **N15 scope ruling
RATIFIED**. The union search round (step 3) is scoped to **N9 (after the protovoice inspection), N13, N14,
N12-realized-half, N19**; N16 needs no search (candidate already enumerated). State columns below carry
the audit's updates, marked *(audit)*.

**The mechanism (run at natural checkpoints; first run = at Wave-3 scoping, BEFORE its disposition):**
1. **The needs-vector (maintained here; §8b's trigger adds a row per new purpose):**

| # | need (GT/material class) | consumer | state (2026-07-03; *(audit)* = updated 2026-07-04) |
|---|---|---|---|
| N1 | common-practice RN/harmony GT, score-aligned, human | gate, Stage-5 fitter | well-covered (DLC/WiR) |
| N2 | dual/multi-annotator disagreement data | Class-P calibration (C1/C2) | *(Wave-3 MEASURED, corrects the audit)* the on-disk co-located dual set = **the 27 TAVERN A/B pairs** (Beethoven 17 + Mozart 10, verified at the WiR clone AND by Cowork glob). The audit's "Tymoczko-vs-DCML pairs" are NOT co-located: within WiR the two analyst sets sit on disjoint pieces (overlap **0**; DCML 988 / Tymoczko 419 analyses); CROSS-container pairs (WiR-Tymoczko × the separate `tools/dcml/` DCML corpora) remain possible but need identity work — recorded, not assumed. Sears (dual, cadence): **no public deposit** (access = authors). CASD (4×, audio) + RS200 (2×) unchanged. *(Wave-3 ADDENDUM, `cc_wave3_addendum_report.md`)* **NEW candidate: `DDMAL/Flexible_harmonic_chorale_annotations`** cloned+pinned+walked — 571 chorales (371 Bach + 200 Praetorius) with **permutational ('flexible') multi-reading** harmonic analyses (multiple valid readings per slice + filtering functions, vs single-reading RN) → a SECOND annotation layer over gate-class Bach chorales. ⚠ **RECORD-ONLY** (its 371 Bach chorales overlap the gate repertoire; any use over gate pieces is a future user ruling — census §4 dedupe). WALK caveat: the analysis GT ships as an R-package BINARY (kernData/ .krn are **kern-only) |
| N3 | jazz/pop analysis GT, score-aligned | A-7 mark retirement, idioms 3–5 | Tier J queued (Wave 3); *(audit)* walk-list adds: Jazz Corpus (function GT, 76), WJD native (phrase/form), Real Book (license-check) |
| N4 | cadence + punctuation/phrase GT | L5 §5.2, L1.5, L6 | rich (corpus-wide since 21k); *(audit)* jazz side = WJD native |
| N5 | key/modulation GT | L3, S1/S2 | *(Wave-3 MEASURED, corrects the audit)* **KMT is NOT present as analyses at the WiR pin** `aa7539f1` (Corpus/Textbooks = 201 scores / **0** analysis.txt — verified by CC AND by Cowork glob); KMT acquisition = the DDMAL `key_modulation_dataset` upstream (direct-acquisition candidate, next corpus increment). Sears pivots: no public deposit. SWD score-aligned local keys unchanged (ChoCo). WiR analyses still carry local keys generally (N5 partial). *(Wave-3 ADDENDUM, `cc_wave3_addendum_report.md`)* **★ KMT ACQUIRED:** `DDMAL/key_modulation_dataset` @ `6602ae6a` cloned+pinned+walked — **201 annotated Humdrum .krn** (aldwell 7 / kostka-payne 15 / reger 117 / rimsky-korsakov 37 / tchaikovsky 25), key/modulation as `*C:` key-designation tokens + inline `NEWKEY=>:RN` markers in the **text spine; CC-BY-SA scores / MIT code; held-out. The direct-acquisition candidate is now on disk (README checkbox list ~135 < actual 201 = living-repo growth, reported) |
| N6 | melodic-phrase GT (monophonic ok) | VL-E | Essen onboarded (Wave 2); *(audit)* depth reserves MTC/GTTM |
| N7 | texture GT (per-bar / per-piece) | VL-C validation, §15-1 | algomus bed onboarded (Wave 2) |
| N8 | voice-leading schema GT | VL-F | schema bed onboarded (Wave 2) |
| N9 | stream/implied-polyphony GT | VL-D target task | *(union search 2026-07-04 — `cowork_union_search_record.md` §1)* **notated-polyphony half now has real candidates:** piano_svsep (393 pieces, per-note voice+staff GT over DCML piano scores WE HOLD — the SOTA task set) + MCMA (~475, CC-BY, hand-exploded Baroque voices) + vocsep_ijcai2023 (1,054, notation-derived); **implied-polyphony half CONFIRMED ABSENT** (VoiSe/Gray-Bunescu never released; final). Held: protovoice (38, partial, reduction-encoded). *(ACQUISITION ROUND 2026-07-04, `cc_acquisition_round_report.md`)* **★ ALL THREE ACQUIRED + pinned + verified at the data:** piano_svsep @ `1462e7c2` (MIT code; GT graphs FETCHED AT RUNTIME from `fosfrancesco/piano_corpora_dcml` — PIN = the code repo, fetch path recorded, `jpop` confirmed non-public), MCMA @ `2bdb12e2` (475 .mxl, track split **153/239/83 VERIFIED**; ★ license = **CC-BY-NC-SA-4.0**, NOT the record's CC-BY — corrected), vocsep_ijcai2023 @ `82152a95` (~1,054 graphs BUILT AT RUNTIME from bach-370-chorales + Haydn/Mozart SQ + MCMA; ★ license = **MIT**, NOT the record's "unstated" — corrected). All held-out; the actual GT for the two runtime-built beds lives at their fetch/source paths (follow-on pin candidates). Implied-polyphony half stays the confirmed-final negative |
| N10 | figured-bass GT | L4 evidence channel (R-4) | *(Wave-3)* **BCFB OBTAINED** (139 chorales / 143 kern + MEI + MusicXML, CC-BY, pinned) — the gate repertoire's composer-stated harmony. **DCMLab/figured-bass WALKED = a realization SCRIPT, N10-NEGATIVE** (never re-mistake it for GT). Third source: the DLC `figbass` column (parser-dropped; exposure = the queued post-wave increment) |
| N11 | hierarchical harmony trees | grammar lever (R-7) | *(Wave-3)* JHT trees held; **NEW: algomus `jazz-arbres` treebank obtained inside algomus-data (1,170 entries — ~8× the JHT)**; Kirlin Schenker41 = README-only repo, the 41 excerpts were never committed (access = dissertation page; 2024 successor arXiv 2408.07184); GTTM located (~300 pairs) but no single artifact + license unclear — access recorded, not mirrored |
| N12 | notated chord symbols aligned with realized scores | E-8 symbols-as-input, T-17 QA | *(union search 2026-07-04, record §4)* leadsheet half rich (held). **Realized half: the big lever is ALREADY HELD — PDMX preserves MuseScore chord symbols (`<harmony>` in the shipped mxl, verified feasible); the symbol-bearing multi-voice subset is unmeasured → a cheap local read-only counting pass is the next step.** Small clean add: GuitarSet (360, CC-BY, instructed-chart vs performed comping). Open Hymnal verified symbol-less; no cleaner jazz set exists. *(ACQUISITION ROUND 2026-07-04, `cc_acquisition_round_report.md`)* **GuitarSet ACQUIRED** — annotation.zip sha256 `8daa02e6…`, **360 .jams verified**, CC-BY-4.0; the 4 audio zips (657 MB–3.61 GB) recorded, NOT downloaded. **★ PDMX counting pass ATTEMPTED + STOPPED, NOT measured:** the HELD form is METADATA-ONLY (`tools/pdmx/PDMX.csv` 250k-row index + `jazz_candidates.csv` + 5 spot-check .mxl) with **NO chord-symbol column** (`n_annotations`/`has_annotations` conflate all annotation types; `tracks`=instrument codes); the raw MXL (`mxl.tar.gz`) + per-score MusicRender JSON live ONLY in the Zenodo archive, not on disk → counting `<harmony>` needs a re-download/acquisition (a future user decision the read-only, do-not-re-download dispatch forbids). No proxy invented; the symbol-bearing multi-voice subset stays **UNMEASURED** |
| N13 | ornament-realization pairs | R-1 ornament expansion | *(union search 2026-07-04, record §2)* **negative CONFIRMED** — no symbol→realization dataset exists; nearest = Batik-plays-Mozart (trill realizations recoverable by heuristic, unlabeled; ★ multi-need: also carries harmony+cadence GT on 12 Mozart sonatas); R-1 ships rule-based/unvalidated as predicted; build-paths recorded |
| N14 | difficulty/grading labels (syllabus, exam grades) | T-32 | *(union search 2026-07-04, record §3)* **found:** CIPI (652 pieces, Henle 1–9, MusicXML — Zenodo gated/research-only) + Mikrokosmos (147, open) + PSyllabus (7,901 exam-board-labeled recordings, no scores) + pianosyllabus.com (28k, website-only). No machine-readable ABRSM/RCM/Henle dumps exist. **T-32 caveat: all real label sources research-only/proprietary — commercial use needs a license path.** *(ACQUISITION ROUND 2026-07-04, `cc_acquisition_round_report.md`)* **Mikrokosmos ACQUIRED** @ `f77aebc1` (147 MusicXML verified, henle 3-class difficulty labels, **no LICENSE file** → hash-pin-only). **CIPI recorded GATED** (Zenodo 8037327 request-access; **USER ACTION: the access form still pending**). **PSyllabus recorded** (Zenodo 14794592; audio/MIDI only, no symbolic scores → N14-adj). The T-32 commercial-license caveat rides the product-tool register |
| N15 | performed-intonation reference material | T-21/T-24 | **★ SCOPE RULING RATIFIED (user, 2026-07-04):** audio-domain, out of corpus scope; T-21/T-24 validate by theory/listening |
| N16 | form/section GT (sonata form etc.) | L6 §9-D3 deferred, T-9 | *(Wave-3)* **algomus Mozart SQ OBTAINED** (32 ref.dez, Structure+Cadence+Harmony labels; caveat: onsets in SECONDS keyed to a reference score/recording — a tick-mapping step is owed before load-bearing use) + WJD native `sections` + CoCoPops `**form`; DCML TSV `form` column VERIFIED chord-morphology, NOT form GT |
| N17 | style/era metadata | idiom lenses, calibration C4 | held (registry fields) |
| N18 | contrapuntal/imitative-structure GT (fugue subjects/answers/countersubjects, imitation points) | T-12, VL-F/VL-D neighborhood | **ADOPTED (user, 2026-07-04, audit §1).** *(Wave-3)* **algomus Bach fugues OBTAINED** (bach-wtc-i, 23 of 24 ref.dez; the 12 Shostakovich analyses are website-only, NOT in the repo — mismatch recorded); CRIM observations remain a candidate |
| N19 | part-writing error/exercise GT (marked errors in species/part-writing exercises) | VL-H, T-12 | **ADOPTED (user, 2026-07-04).** *(union search 2026-07-04, record §5)* **no public dataset exists — CONFIRMED build-not-download** (Harmonia/Artusi hold it commercially closed). Validation seeds found: the Dahn manuscript-checked 46 consecutive-5th/8ve instances in the Bach chorales + Fitsioris-Conklin 18 (real-music positives, small transcription job) + the synthetic-violation route. Construction owned by VL-H's design gate |
| N20 | pedal-point GT | pedal-point-span validation (its owning layer's design) | **ADOPTED (user, 2026-07-04):** covered — VERIFIED DLC `pedal` TSV column on every held corpus (parser-dropped) + algomus fugue pedals; exposure pending. Completes the §2.15 span-kind↔needs mapping |

2. **The audit:** re-score every enumerated census row (both appendices + registry) against the needs columns —
   offline, no searching; each row gains a needs-coverage note; multi-need rows get flagged (a container serving
   several needs outranks single-need alternatives that any one purpose-sweep would have preferred).
3. **The union search round:** targeted searches ONLY for columns still uncovered/unassessed after the audit.
   *(As scoped by the first-run audit + disposition, 2026-07-04: N9 — after the protovoice inspection —,
   N13, N14, N12-realized-half, N19. The pre-audit guess "N9, N12, N13, N14, N16" is superseded: N16 came
   back covered-by-candidate.)* Findings enter via the census as always.

**Relation to the other triggers:** §8b (purpose sweep at each new purpose) keeps the vector current; the yearly
re-sweep catches new releases; the full-needs audit catches the CROSS-purpose and re-scoring misses both leave.

**★ STAGE-5 FITTING-POOL LICENSE CONSTRAINT (user-ratified 2026-07-04 — binding on the fitter design):**
the Stage-5 fitter's design doc must **declare its data pool explicitly, per license class**, before fitting:
- **Weights intended to SHIP (any future commercial distribution): fit only on the PD / CC0 / CC-BY(-SA)
  pool** (gate chorales PD · WiR analyses CC-BY-SA · CoCoPops · BCFB · GuitarSet · OpenEWLD · OpenScore…).
- **NC-class sources (all 40 DCML corpora, MCMA, Essen, Chordonomicon, NC ChoCo partitions) and
  no-license sources (Mikrokosmos, Batik, iRb…): held-out validation / QA / statistics ONLY** — they must
  not shape shipped parameters without a license arrangement. (Fitting on NC data for a shipped commercial
  product is the "trained on NC" gray zone; internal research use is unaffected — the current fork is
  private research, so nothing is violated today; this constraint exists so commercialization never
  silently inherits an NC-derived parameter set.)
- The A-8 metric may keep DCML as its measurement GT (measurement ≠ shipped parameters), but the fitter's
  OBJECTIVE-vs-VALIDATION split must state which sources feed which. T-32 (difficulty) already carries its
  own harder version of this caveat (no commercially usable label source exists at all).
- Ride: the constraint enters `docs/implementation_roadmap.md`'s Stage-5 block at the next CC docs commit,
  and the fitter design doc restates it in its §2/§6 (data declaration) — not optional.

**The intake rule (user, 2026-07-03 — the converse of step 2):** a find made FOR one need is **scored against
the FULL needs-vector at intake**, never single-purpose-tagged. Three consequences, each binding:
1. **Already-satisfied needs stay open to supersession** — a new find may serve a "passed" need better or
   cheaper than its current bed; the intake scoring records that even when no action follows.
2. **Future/inactive needs get pre-coverage** — a find's coverage of a not-yet-active column is recorded at
   intake, so when that purpose's §8b sweep eventually runs it starts non-empty.
3. **Every GT LAYER of a container is inventoried at intake, not just the layer that motivated the find** — the
   founding counter-example: the JHT entered for the harmonic idiom study and its hierarchical TREE annotations
   (a distinct GT layer, lever R-7's footing) went unrecorded until a different question was asked at it a week
   later. The registry's per-row needs-coverage note (audit step 2) is where the intake scoring lands.

**The supersession decision protocol (user, 2026-07-03 — what happens when a find serves an already-passed
need):** a "go back and rework now" vs "postpone" question is NEVER decided by enthusiasm or by default silence.
The protocol, reusing the project's standing shapes:
1. **Record first:** the finding lands as an open item in the affected component's §15 (open items) + a STATUS
   plan line — it cannot get lost regardless of the decision.
2. **Cheap impact measurement before any decision** (investigate-by-default): a read-only re-validation of the
   component's signed conclusions against the new material. The question it answers: does the new bed
   **contradict** a conclusion the design rests on, or merely **enrich/extend** the validation?
3. **The fork, by measured outcome:**
   - **Contradiction (a premise-invalidation):** surfaced IMMEDIATELY as a tripwire event (the D5-test pattern) —
     the user decides rework-now vs accept-with-recorded-caveat; downstream work that builds on the invalidated
     conclusion is named in the surfacing (the compounding cost of waiting is part of the decision material).
   - **Enrichment only:** DEFAULT = postpone to the component's next natural touch (the §15 item carries it);
     pulling the rework forward is a user priority call, informed by the measurement.
4. **The decision is the user's in both branches** — the protocol fixes what is measured and what is recorded,
   never the outcome. (This is the corpus-side analogue of the gate re-baseline discipline: evidence first,
   deliberate ratification second, nothing reopened by silence.)
