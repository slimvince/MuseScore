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
| OpenScore family, Mutopia, KernScores highlights, MuseData, early-music projects (JRP/CRIM/Tasso/Marenzio/CMME), Wikifonia→EWLD lineage, Lakh→MetaMIDI→GigaMIDI lineage, main folk containers (Essen, MTC, Nottingham) | **Fully enumerated** [Wave-2 ONBOARDED the Essen `ccarh/essen-folksong-collection` **phrase-boundary bed** (Humdrum kern) — see `cc_corpus_wave2_report.md`] |
| **algomus / Dezrann** (algomus.fr GitLab org + dezrann.net) — symbolic-music analysis annotation datasets (texture, cadence, form) | **Enumerated** [Wave-2 ONBOARDED `symbolic-texture-dataset` (Couturier et al. ISMIR 2022) as an **annotation bed**; moved here from §7 residual risk — see `cc_corpus_wave2_report.md`] |
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
container is now an **enumerated §1 row**, with `symbolic-texture-dataset` onboarded at Wave 2; the remaining algomus
cadence/form sets stay in this residual bucket), figured-bass
corpora (DCMLab/figured-bass uninspected), scattered Humdrum `**harm` spines on kern.ccarh.org, national-library MEI
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
