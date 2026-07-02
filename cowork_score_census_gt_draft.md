# Census of Symbolic-Music Corpora WITH Analytic Ground-Truth Annotations (draft)

**Date:** 2026-07-02 · **Method:** container enumeration to closure (no keyword sampling).
**Verification tags:** `[verified]` = the page/file itself was fetched during this census; `[reported]` = from a search snippet or secondary source; `?` = unknown, not fabricated.

Containers walked: (1) the entire DCMLab GitHub org (127 repos, all listed), incl. the
`distant_listening_corpus` (DLC), `dcml_corpora`, and `romantic_piano_corpus` submodule manifests;
(2) the When-in-Rome meta-corpus README (full component list); (3) the dataset sections of
AugmentedNet, RNBert, AnalysisGNN, ChordGNN; (4) the ChoCo README partition table (18 partitions);
(5) cadence/phrase datasets (DCML Mozart, algomus, Sears, Essen, MTC, GTTM, POP909);
(6) targeted sweeps for stragglers (CoCoPops, Chordonomicon, HookTheory, KMT, UCI, Kirlin).

---

## 1. DCMLab corpora (DCML harmony standard 2.x, MuseScore `.mscx` + ms3 TSV extracts)

The DCMLab org contains **127 repos** `[verified — full org listing scraped]`. The annotated-corpus
subset below is complete. All DLC members share the same format: MuseScore scores + `harmonies/`,
`notes/`, `measures/`, `chords/` TSVs with **Roman-numeral-style DCML labels including local keys,
applied chords, phrase-boundary markers**; some (Mozart, Corelli) also carry **cadence labels**.
License for the corpus repos is CC BY-NC-SA 4.0 unless noted `[reported — spot-checked, verify per repo]`.

**Container manifests fetched `[verified]`:** `distant_listening_corpus/.gitmodules` (41 submodules),
`dcml_corpora/.gitmodules` (12), `romantic_piano_corpus/.gitmodules` (9, all also in DLC).

### 1a. The Distant Listening Corpus — all 41 sub-corpora `[verified list]`

| Name | Content/composer | Size | GT type + standard | Score format + alignment | License | URL | Notes |
|---|---|---|---|---|---|---|---|
| ABC | Beethoven, all 16 string quartets | 70 movements [verified] | RN harmony, DCML 1.0/2.x | .mscx, label-aligned | CC BY-NC-SA [reported] | github.com/DCMLab/ABC | Founding DCML corpus (Neuwirth et al. 2018) |
| mozart_piano_sonatas | Mozart, complete piano sonatas | 18 sonatas / 54 mvts [verified] | RN harmony + **cadence labels**, DCML 2.x | .mscx, aligned | CC BY-NC-SA [reported] | github.com/DCMLab/mozart_piano_sonatas | TISMIR 2021 "Score, harmony, and cadence" [verified] |
| corelli | Corelli trio sonatas | ? (dozens of mvts) | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/corelli | Already in project use |
| beethoven_piano_sonatas | Beethoven piano sonatas (complete) | all 32 sonatas [reported] | RN harmony DCML 2.x | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/beethoven_piano_sonatas | Largest single DLC member; WiR conversion had 64 mvts at conversion time [verified] |
| chopin_mazurkas | Chopin mazurkas | 56 works [verified via WiR README] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/chopin_mazurkas | Project already uses |
| bach_en_fr_suites | J.S. Bach English+French Suites | ~90 mvts [verified ≈, README table] | RN harmony DCML 2.3 | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/bach_en_fr_suites | Project already uses |
| bach_solo | J.S. Bach solo pieces (cello/violin etc.) | ~70 mvts [verified ≈] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/bach_solo | Monophonic/implied harmony — interesting stress test |
| bartok_bagatelles | Bartók 14 Bagatelles op. 6 | 14 pieces [verified title] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/bartok_bagatelles | Post-tonal edge |
| c_schumann_lieder | Clara Schumann Lieder | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/c_schumann_lieder | |
| couperin_clavecin | Couperin, L'art de toucher le clavecin | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/couperin_clavecin | French baroque |
| couperin_concerts | Couperin, Concerts Royaux | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/couperin_concerts | |
| cpe_bach_keyboard | C.P.E. Bach keyboard works | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/cpe_bach_keyboard | Project already uses ("cpe_bach") |
| debussy_suite_bergamasque | Debussy | 4 mvts [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/debussy_suite_bergamasque | |
| dvorak_silhouettes | Dvořák Silhouettes op. 8 | 12 pieces [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/dvorak_silhouettes | Project already uses |
| frescobaldi_fiori_musicali | Frescobaldi Fiori Musicali (1635) | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/frescobaldi_fiori_musicali | Pre-tonal/modal |
| grieg_lyric_pieces | Grieg Lyric Pieces (complete) | 66 pieces [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/grieg_lyric_pieces | Project already uses |
| handel_keyboard | Handel, Grobschmied Variations HWV 430 | 1 set [verified] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/handel_keyboard | Small |
| jc_bach_sonatas | J.C. Bach keyboard sonatas | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/jc_bach_sonatas | Galant style |
| kleine_geistliche_konzerte | Schütz, Kleine Geistliche Konzerte | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/kleine_geistliche_konzerte | 17th-c. sacred |
| kozeluh_sonatas | Koželuch piano sonatas | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/kozeluh_sonatas | Classical-era breadth |
| liszt_pelerinage | Liszt, Années de Pèlerinage | ? (~19-26 pieces) | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/liszt_pelerinage | Late-romantic chromaticism |
| mahler_kindertotenlieder | Mahler Kindertotenlieder | 5 songs [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/mahler_kindertotenlieder | Orchestral song |
| medtner_tales | Medtner, Tales (Skazki) | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/medtner_tales | |
| mendelssohn_quartets | Mendelssohn string quartets | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/mendelssohn_quartets | |
| monteverdi_madrigals | Monteverdi madrigals | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/monteverdi_madrigals | Distinct from Tymoczko's WiR madrigal analyses |
| pergolesi_stabat_mater | Pergolesi Stabat Mater | ? (12 mvts) [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/pergolesi_stabat_mater | |
| peri_euridice | Peri, Euridice (1600) | 1 opera | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/peri_euridice | Earliest surviving opera — modal edge |
| pleyel_quartets | Pleyel string quartets | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/pleyel_quartets | |
| poulenc_mouvements_perpetuels | Poulenc | 3 pieces [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/poulenc_mouvements_perpetuels | 20th-c. |
| rachmaninoff_piano | Rachmaninoff piano pieces | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/rachmaninoff_piano | |
| ravel_piano | Ravel piano pieces | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/ravel_piano | |
| scarlatti_sonatas | D. Scarlatti keyboard sonatas | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/scarlatti_sonatas | |
| schubert_winterreise (DCML) | Schubert Winterreise | 24 songs [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/schubert_winterreise | NOT the same as Weiß et al. SWD (§6) |
| schulhoff_suite_dansante_en_jazz | Schulhoff, Suite dansante en jazz | ? (6 mvts) [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/schulhoff_suite_dansante_en_jazz | Jazz-idiom classical — useful for Jazz preset |
| schumann_kinderszenen | R. Schumann Kinderszenen | 13 pieces [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/schumann_kinderszenen | Project already uses |
| schumann_liederkreis | R. Schumann Liederkreis | ? (12 songs op. 39) [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/schumann_liederkreis | |
| sweelinck_keyboard | Sweelinck organ/keyboard | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/sweelinck_keyboard | Renaissance/early-baroque |
| tchaikovsky_seasons | Tchaikovsky, The Seasons | 12 pieces [reported] | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/tchaikovsky_seasons | Project already uses |
| wagner_overtures | Wagner overtures | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/wagner_overtures | Orchestral, heavy chromaticism |
| wf_bach_sonatas | W.F. Bach keyboard sonatas | ? | RN harmony DCML | .mscx | CC BY-NC-SA [reported] | github.com/DCMLab/wf_bach_sonatas | |
| distant_listening_corpus (container) | All 41 above as submodules + concatenated Frictionless datapackage | ~1,200+ pieces total (AnalysisGNN counts 1,719 incl. AugmentedNet overlap) [reported] | DCML 2.x | .mscx + TSV | per-repo | github.com/DCMLab/distant_listening_corpus | One-ZIP download of all TSVs [verified] |

### 1b. DCMLab annotated repos OUTSIDE the DLC `[verified org listing]`

| Name | Content/composer | Size | GT type + standard | Score format + alignment | License | URL | Notes |
|---|---|---|---|---|---|---|---|
| bach_chorales (DCML) | J.S. Bach chorales (Kaiser edition) | 358 chorales [verified] | **NO harmony labels — `labels` column is 0 for every file** [verified] | MuseScore 3.6.2, known accidental-conversion errors [verified] | CC0 [verified] | github.com/DCMLab/bach_chorales | ⚠ Scores-only. If the project treats "DCML bach_chorales" as GT, the RN GT actually comes from music21/Tymoczko (WiR), not this repo |
| JazzHarmonyTreebank | Jazz standards (from iRealPro) | 150 chord sequences [verified] | **Hierarchical harmonic syntax trees** (open+complete constituent trees), JSON | chords-only (no score alignment) | CC BY 4.0 [reported] | github.com/DCMLab/JazzHarmonyTreebank | Harasim et al. ISMIR 2020; project already uses |
| choro | Brazilian choro (Choro Songbook transcriptions) | 295 pieces, 44,067 chord tokens [reported] | **Chord symbols + formal structure** | symbolic transcriptions (no engraved score) | ? | github.com/DCMLab/choro | Moss et al. 2020 JNMR; genre outside current corpus mix |
| schema_annotation_data | Galant schemata annotations | ? | Schema instances (not RN) | aligned to scores | ? | github.com/DCMLab/schema_annotation_data | Analytic GT, adjacent to harmony |
| protovoice-annotations | Protovoice (voice-leading reduction) analyses | ? (small) | Proto-voice derivations | aligned | ? | github.com/DCMLab/protovoice-annotations | Reduction GT, not RN |
| figured-bass | Figured bass data | ? | Figured-bass labels | ? | ? | github.com/DCMLab/figured-bass | Not inspected; figured bass = quasi-harmonic GT |
| debussy_piano (+ 8 debussy_* repos) | Debussy complete solo piano | ~100 pieces [reported] | **likely scores-only (no DCML harmony labels)** [reported — verify before use] | .mscx | ? | github.com/DCMLab/debussy_piano | Only debussy_suite_bergamasque is harmony-annotated (in DLC) |

---

## 2. When-in-Rome meta-corpus — full component list `[verified from README]`

Meta-total: **~2,000 analyses of ~1,500 distinct works** [verified]. Format: RomanText (`analysis.txt`)
+ `score.mxl` or `remote.json`; music21-parsable; new content CC BY-SA 4.0, converted content keeps
origin license [verified]. URL: github.com/MarkGotham/When-in-Rome

| Name | Content/composer | Size | GT type + standard | Score format + alignment | License | URL | Notes |
|---|---|---|---|---|---|---|---|
| WiR ← DCML ABC | Beethoven quartets | 70 mvts [verified] | RN (RomanText, converted from DCML) | .mxl aligned | CC BY-SA conversion [verified] | (in WiR) | |
| WiR ← DCML Mozart sonatas | Mozart | 18 sonatas [verified] | RN RomanText | .mxl | as above | (in WiR) | |
| WiR ← DCML romantic_piano_corpus | Chopin mazurkas (56), Beethoven sonatas (64 mvts) + 7 more collections | several hundred pieces [verified] | RN RomanText | .mxl | as above | (in WiR) | |
| WiR ← TAVERN | Mozart+Beethoven keyboard variations | 27 sets [verified] | RN RomanText (from Humdrum **harm) | .mxl | original TAVERN license | (in WiR) | Dual analyses preserved as analysis.txt + analysis_B.txt [verified] |
| WiR ← Haydn Op20 ("HaydnSun") | Haydn op. 20 quartets | 6 quartets / 24 mvts [verified] | RN RomanText (from **harm) | .mxl | Zenodo record 1095630 [verified] | (in WiR) | Nápoles López harmonic annotations |
| WiR ← KMT (Key Modulations and Tonicizations) | Examples from 5 theory textbooks (Aldwell, Kostka, etc.) | ? (hundreds of short examples) | **Local key / modulation / tonicization GT** | .mxl | see github.com/DDMAL/key_modulation_dataset [reported] | (in WiR, Corpus/Textbooks) | Nápoles López et al. DLfM 2020 [verified reference] |
| WiR ← BPS-FH | Beethoven sonata 1st movements | 32 mvts [verified] | RN RomanText (from BPS-FH csv) | .mxl | ? | (in WiR) | |
| WiR ← Tymoczko TAOM: Monteverdi | Madrigals books 3–5 | 48 works [verified] | RN RomanText (native) | .mxl | ? | (in WiR) | Also in music21 corpus |
| WiR ← Tymoczko TAOM: Bach chorales | 371 chorales | 371 [verified] | RN RomanText (native) | .mxl | ? | (in WiR) | Superset of the music21 20-chorale set — this IS the biggest Bach-chorale RN GT |
| WiR ← Tymoczko TAOM: misc | Beethoven sonatas (36 mvts), 2nd Chopin-mazurka analysis set, others | ~100+ [verified] | RN RomanText | .mxl | ? | (in WiR) | Gives dual-annotation pairs vs DCML |
| WiR native: WTC-I preludes | Bach, Well-Tempered Clavier I preludes | 24 [verified] | RN RomanText (Gotham et al.) | .mxl | CC BY-SA [verified] | (in WiR) | |
| WiR native: OpenScore Lieder RN subset | 19th-c. songs incl. complete Winterreise, Schwanengesang, Dichterliebe, many women composers | ~200+ songs (exact ?) | RN RomanText | .mxl / remote CC0 scores [verified] | CC BY-SA analyses, CC0 scores [verified] | (in WiR) | The only large **song/Lieder** RN GT |
| WiR native: Variations_and_Grounds | Bach + Purcell ground-bass works | ? (small) | RN RomanText | .mxl | CC BY-SA | (in WiR) | |

---

## 3. SOTA-paper dataset tables (the field's de-facto RN-GT census)

| Paper | Training/eval corpora | Verification |
|---|---|---|
| **AugmentedNet** (Nápoles López et al., ISMIR 2021 + PhD 2022) | ABC, BPS(-FH), HaydnSun (op20), KMT, MPS (Mozart sonatas), TAVERN, WiR (subset), WTC-I preludes — distributed as one preprocessed `dataset.zip`; + synthetic texturized examples | Test-set table in README lists WiR/HaydnSun/ABC/TAVERN/WTC/BPS [verified]; KMT+MPS in training set [reported] |
| **ChordGNN** (Karystinaios & Widmer, arXiv 2307.03544) | Same AugmentedNet compilation ("the reference datasets") | [verified abstract; composition reported] |
| **RNBert** (Sailor, ISMIR 2024) | When-in-Rome meta-corpus (RomanText), key + RN tasks | README fetched (no dataset table) [verified]; WiR as source [reported from paper] |
| **AnalysisGNN** (arXiv 2509.06654) | AugmentedNet dataset + **Distant Listening Corpus** + Bach WTC cadence dataset (algomus) + **Mozart string-quartet cadence dataset** (algomus) + **Haydn string-quartet cadence dataset** (Sears) = **1,719 annotated pieces** | [verified — paper HTML fetched, §4 Corpora] |

No RN-GT dataset appears in these four papers that is not already in §§1–2 or §5 — the papers confirm closure of the classical-RN world.

---

## 4. ChoCo (Chord Corpus) — all 18 partitions `[verified from README table]`

Container: github.com/smashub/choco — 20,080 JAMS files (2,283 audio / 17,803 symbolic), 20,530 chord
annotations (Harte-normalized) + 20,029 key/modulation annotations + 554 structure + 286 beat
annotations. License CC BY 4.0 except Chordify/Mozart/JAAH-derived (CC BY-NC-SA 4.0) [verified].

| Name | Content | Size | GT type | Symbolic-score alignment? | License (orig.) | URL | Notes |
|---|---|---|---|---|---|---|---|
| Isophonics | Beatles/Queen/Zweieck pop-rock | 300 [verified] | Harte chords (+keys, structure) | **No — audio-aligned (seconds)** | research | (via ChoCo) | |
| JAAH | Jazz recordings | 113 [verified] | Harte chords, audio-aligned | No — audio | CC BY-NC-SA | (via ChoCo) | Project already uses |
| Schubert-Winterreise (SWD) | 25 songs, 9 performances | 25 (S) + 25×9 (A) [verified] | Harte chords + **local keys** | **Yes — score (measure:beat) AND audio versions** | CC BY-NC-SA [reported] | (via ChoCo; Weiß et al. JOCCH 2021) | The rare score+audio dual GT |
| McGill Billboard | US pop charts 1958–91 | 890 (740 unique) [verified] | Harte chords, expert | No — audio | research | (via ChoCo) | Project already uses |
| Chordify (CASD) | Pop, 4 annotators each | 50×4 [verified] | Harte chords | No — audio | CC BY-NC-SA | (via ChoCo) | Annotator-subjectivity GT |
| Robbie Williams | Pop | 61 [verified] | Harte chords | No — audio | research | (via ChoCo) | |
| The Real Book | Jazz standards | 2,486 [verified] | Harte chords (from leadsheets) | Symbolic origin, measure:beat | ? | (via ChoCo) | |
| USPop 2002 | Pop | 195 [verified] | Harte chords | No — audio | research | (via ChoCo) | |
| RWC-Pop | Pop | 100 [verified] | Harte chords | No — audio | RWC license | (via ChoCo) | |
| Weimar Jazz Database | Jazz solos | 456 [verified] | Leadsheet chords + solo transcription (+phrases in WJD proper) | audio-aligned; melody symbolic | research | (via ChoCo) | Project already uses |
| Wikifonia | Various leadsheets | 6,500+ [verified] | Leadsheet chord symbols | **Yes — MusicXML leadsheets** | discontinued/gray | (via ChoCo) | Project already uses |
| iReal Pro | Jazz+various playlists | 2,000+ [verified] | Leadsheet chords | Symbolic chart (no notation) | community | (via ChoCo) | Project already uses |
| Band-in-a-Box (De Haas) | Various | 5,000+ [verified] | Leadsheet chords | symbolic charts | research | (via ChoCo) | Not previously on project's list |
| When in Rome (subset) | Classical | 450 [verified] | Roman numerals | Yes (RomanText origin) | CC BY-SA | (via ChoCo) | |
| Rock Corpus (RS200) | Rock canon | 200 [verified] | **Roman numerals** (har format) + melodic transcriptions | timing-aligned to audio, not scores | free research | (via ChoCo; rockcorpus.midside.com) | deClercq & Temperley |
| Mozart Piano Sonatas (DCML) | Classical | 54 (18) [verified] | RN (DCML) | Yes | CC BY-NC-SA | (via ChoCo) | |
| Jazz Corpus (Granroth-Wilding & Steedman) | Jazz | 76 [verified] | Hybrid chords + **harmonic-function analyses** | chords-only | research | (via ChoCo) | Small but has functional GT for jazz |
| Nottingham | British/Irish folk | 1,000+ [verified] | ABC chord symbols | **Yes — ABC notation (symbolic)** | free | (via ChoCo) | Project already uses |

---

## 5. Cadence / phrase / segmentation ground truth

| Name | Content/composer | Size | GT type + standard | Score format + alignment | License | URL | Notes |
|---|---|---|---|---|---|---|---|
| DCML Mozart sonatas cadence layer | Mozart 18 sonatas | cadence labels across 54 mvts (count ?) | PAC/IAC/HC/EC/DC labels in the harmony TSVs | .mscx aligned | CC BY-NC-SA [reported] | github.com/DCMLab/mozart_piano_sonatas | Already-owned corpus; cadence layer is a free add-on [verified paper title] |
| algomus Bach fugues | WTC-I 24 fugues + 12 Shostakovich fugues | 36 pieces, 1,000+ labels [reported] | Subjects, countersubjects, **cadences**, pedals | symbolic (kern refs), Dezrann-viewable | research/open [reported] | algomus.fr/data | Giraud et al., Computational Fugue Analysis (CMJ 2015) |
| algomus Mozart string quartets | Sonata-form movements | 32 mvts, 2,000+ labels [reported] | **Sonata-form structure + cadences** | symbolic, aligned | open [reported] | algomus.fr/data | = AnalysisGNN's "Mozart SQ cadence dataset" [verified use] |
| Sears Haydn quartet cadences | Haydn quartet expositions 1771–1803 | 270 cadence tokens / 50 expositions [reported] | Cadence category GT, dual annotators, + key/modulation/pivot annotations | kern (kern.ccarh.org scores) | research [reported] | via Sears et al. 2018 / Zenodo | = AnalysisGNN's Haydn cadence set [verified use] |
| BPS-FH phrase layer | Beethoven 32 sonata 1st mvts | 32 mvts | **phrase boundaries** + beats/downbeats (besides RN) | note-event csv + MIDI | ? | github.com/Tsung-Ping/functional-harmony | Phrases verified in README [verified] |
| TAVERN phrase layer | Mozart+Beethoven variations | **1,060 phrases** (939 major / 121 minor) [verified] | Phrase-model functional analysis per phrase, 2 annotators | Humdrum **harm + kern, joined files | ? (research) | github.com/jcdevaney/TAVERN | Verified README |
| Essen Folksong Collection | German/European/Chinese folk melodies | ~9,000+ melodies [reported] | **Phrase boundaries** (EsAC hard breaks), keys | EsAC + kern conversions; melody-level | free research [reported] | essen db / kern.humdrum.org | The classic phrase-GT corpus |
| MTC-ANN 2.0.1 (Meertens) | Dutch folk songs | 360 melodies / 26 tune families [reported] | **Phrase segmentation**, similarity, motif annotations | **kern/MIDI/humdrum, symbolic | open [reported] | liederenbank.nl/mtc | MTC-FS-INST (~18k melodies) has phrase data too [reported] |
| GTTM database (Hamanaka) | Classical melodies | 300 melodies [reported] | **Grouping structure (phrases)**, metrical + time-span trees | MusicXML, aligned | research [reported] | gttm.jp | Phrase GT with full hierarchy |
| POP909 (+ POP909-CL) | Chinese pop piano arrangements | 909 songs [reported] | chords, keys, beats, **phrase/section boundaries** (tempo hand-labeled; chords/keys MIR-algorithm, later human-corrected in derivatives; POP909-CL = cleaned chord labels, ICASSP 2026) | **MIDI, aligned** | research [reported] | github.com/music-x-lab/POP909-Dataset | GT quality mixed — treat chord labels as semi-automatic |

---

## 6. Jazz / pop / crowd-sourced harmonic GT not in ChoCo (or beyond it)

| Name | Content | Size | GT type | Symbolic alignment? | License | URL | Notes |
|---|---|---|---|---|---|---|---|
| HookTheory / TheoryTab | Crowd-sourced pop/rock/game music excerpts | tens of thousands of excerpts (Donahue et al. sampled ~28k pieces; 50h aligned subset) [reported] | **Melody + chords + key, scale-degree-relative (RN-convertible)** | Yes — symbolic (proprietary XML/JSON), audio-alignable | user content, research releases [reported] | hooktheory.com / github.com/chrisdonahue (Sheet Sage release) | Largest relative-to-key pop harmony GT in existence |
| Chordonomicon | Ultimate-Guitar scrape | 666,000 progressions [verified count via paper] | Chord symbols + **section structure** + genre metadata | No scores — chords-only | research (HF) [reported] | huggingface.co/datasets/ailsntua/Chordonomicon | Project already uses |
| CoCoPops | McGill Billboard + RS200 unified, + new melodies | 414 transcriptions / 398 tracks [reported] | **harm (RN) + **kern melody, humdrum | **Yes — humdrum symbolic** | research [reported] | github.com/Computational-Cognitive-Musicology-Lab/CoCoPops | ISMIR 2023; upgrades two audio-timed corpora to symbolic |
| iRb corpus (Shanahan/Broze) | iRealPro jazz standards in humdrum | ~1,200 charts [reported] | **jazz chord syntax | symbolic charts | research [reported] | via Shanahan et al. Zenodo | Source corpus of the JHT's 150 |
| OpenEWLD / EWLD | Wikifonia-derived leadsheets, PD subset | OpenEWLD ~500; EWLD ~5,000 [reported] | Chord symbols + melody | **Yes — MusicXML** | OpenEWLD CC0-ish (PD works) [reported] | github.com/00sapo/OpenEWLD | Cleaner licensing than raw Wikifonia |
| Weimar Jazz Database (native) | 456 jazz solos | 456 [verified via ChoCo] | chords + phrases + form + melody transcriptions | symbolic melody, audio-timed | research | jazzomat.hfm-weimar.de | Native DB richer than ChoCo slice (phrase/form GT) |

---

## 7. Other analytic-GT corpora (misc.)

| Name | Content | Size | GT type | Format | License | URL | Notes |
|---|---|---|---|---|---|---|---|
| UCI Bach Chorale Harmony | Bach chorales | 60 chorales / 5,665 chord events [reported] | chord labels (pitch-class sets → chord names) | event lists (no score) | UCI ML repo | archive.ics.uci.edu | Radicioni & Esposito 2010; superseded by WiR-371 for most uses |
| Kostka-Payne corpus (Temperley) | Theory-textbook excerpts | 46 excerpts [reported] | RN harmony + meter | MIDI + text | research [reported] | via Temperley (Melisma) | Overlaps KMT conceptually |
| Kirlin Schenker dataset ("Schenker41") | Common-practice excerpts | 41 excerpts [reported] | **Schenkerian reductions (MOP trees)** | symbolic, aligned | research [reported] | via Kirlin ISMIR 2014 | Only machine-readable Schenker GT |
| music21 built-in RN corpora | Bach chorale subset (20), Monteverdi, Beethoven excerpts | ~100 [reported] | RN (RomanText) | music21 corpus | BSD/mixed | github.com/cuthbertLab/music21 | Project already uses; superseded by WiR |
| RS200 / Rock Corpus (native) | 200 rock songs | 200 [verified via ChoCo] | RN analyses (2 analysts) + melody + timing | text har/mel + audio timestamps | free [reported] | rockcorpus.midside.com | Native version has BOTH analysts; ChoCo carries one view |

---

## Containers enumerated to closure

**Fully enumerated (container manifest itself fetched):**
- DCMLab GitHub org: all **127 repos** listed by name (HTML listing pages scraped); corpus subset extracted.
- `distant_listening_corpus/.gitmodules`: all **41** sub-corpora.
- `dcml_corpora/.gitmodules` (12) and `romantic_piano_corpus/.gitmodules` (9) — both subsets of the above.
- When-in-Rome README: complete component/origin list (§2).
- ChoCo README: complete 18-partition table with counts.
- AnalysisGNN paper §4: complete corpus list (verified from paper HTML).
- BPS-FH, TAVERN, RNBert, AugmentedNet READMEs fetched directly.

**Partially enumerated:**
- Per-repo sizes of most DLC members (repo names/composers/DOIs verified; piece counts mostly "?" or [reported]).
- AugmentedNet exact training manifest (test sets verified from README; KMT/MPS membership from paper, [reported]).
- RNBert training data (= When-in-Rome) from the paper, not from a fetched dataset table.
- HookTheory, Chordonomicon, CoCoPops, MTC, Essen, GTTM, Sears, algomus, POP909: verified via search snippets ([reported]) not primary fetches.
- "Awesome MIR"-style indexes were not exhaustively crawled; targeted sweeps only.

## Residual risk — where more GT could still hide

1. **Zenodo/university-hosted corpora with no GitHub presence** (e.g. further Dezrann/algomus annotation sets — algomus.fr/data hosts more than the two sets listed; the Osnabrück/Weiß audio-chord world).
2. **Figured-bass corpora** (DCMLab/figured-bass uninspected; Bach chorale figured-bass encodings; the "Bass and Continuo" datasets from the BachSources world) — quasi-harmonic GT this census only touched.
3. **Non-Western / non-English collections**: Chinese pop (POP909 relatives, CCMusic), Turkish makam, flamenco — some carry chord or phrase GT.
4. **Schenkerian & reduction GT** beyond Kirlin (e.g. protovoice-annotations growth, reductive_analysis_app outputs).
5. **Commercial/withheld data**: Hooktheory's full DB (only research slices released), iRealPro playlists (community-legal gray), Ultimate-Guitar derivatives.
6. **Very new releases** (2025–26): POP909-CL (ICASSP 2026) surfaced during this census; more BACHI-style relabeled corpora likely appearing — re-sweep arXiv/ISMIR 2026 proceedings before treating this census as final.
7. **Humdrum **harm spines scattered across kern.ccarh.org** beyond the named datasets (unindexed **harm files exist in KernScores).
