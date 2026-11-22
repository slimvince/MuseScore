# Research papers — local copies (user-supplied 2026-07-19)

Primary sources for the joint-estimator work, obtained by the user after the term-level
theory-grounding audit flagged them unfetchable online (`cowork_term_theory_grounding.md` §5).
Each was read by Cowork on 2026-07-19; what was extracted is recorded in the grounding doc at the
cited section. Filenames are descriptive; originals as uploaded.

| File | Citation | Why it is here / what it settled |
|---|---|---|
| `raphael_stoddard_2003_ismir_harmonic_analysis_pgm.pdf` | Raphael & Stoddard, "Harmonic Analysis with Probabilistic Graphical Models," ISMIR 2003 | The reference joint (tonic, mode, chord) HMM (grounding §F1/§F10). This copy re-confirms the prose claims verbatim; equation numerals still extract garbled, so the parameter counts stay flagged as reconstructed. |
| `feisthauer_bigo_giraud_leve_2020_smc_keys_modulations.pdf` | Feisthauer, Bigo, Giraud & Levé, "Estimating keys and modulations in musical pieces," SMC 2020 | Was the one on-point cadence→key source left unverified. Now FACT-grade: current diatonic pitch set, ddiat, the V→I heuristic (≥2 of 3 voice leadings), the beats-since-V→I anchoring measure, weighted tonal-plan cost; 84.8 % on 38 Mozart movements (grounding §F4, also §F2 — the signature is the default accidental in CS(b)). |
| `catteau_martens_leman_2006_gfkl_key_chord_recognition.pdf` | Catteau, Martens & Leman, "A Probabilistic Framework for Audio-Based Tonal Key and Chord Recognition," GfKl 2006 (Springer 2007) | The Lerdahl-distance transition form, previously unverified. Now FACT-grade: P(Cₙ|Cₙ₋₁)=exp(−d/d_norm,C), P(Sₙ|Sₙ₋₁)=exp(−d/d_norm,S), single-stage Viterbi over (scale, chord); chord-distance table with γ=9, δ=2γ; P(C|S) as profile inner product (grounding §F10/§F5). |
| `teodoru_raphael_2007_ismir_pitch_spelling_voices.pdf` | Teodoru & Raphael, "Pitch Spelling with Conditionally Independent Voices," ISMIR 2007 | The generative spelling-given-key form, previously metadata-only. Now FACT-grade: hidden per-measure local-key Markov chain; voices as conditionally independent Markov chains given the keys; one DP jointly decodes spelling + key; trainable from unlabeled data but training produced no measured improvement (grounding §F3). |
| `chew_2002_spiral_array_key_boundaries.pdf` | Chew, "The Spiral Array: An Algorithm for Determining Key Boundaries," ICMAI 2002 | Spiral-array key-boundary search (BSA): modulation points as distance-minimizing segment boundaries in the spiral array; polynomial in onsets for a fixed boundary count (grounding §F10-adjacent). |
| `sears_verbeten_percival_2023_jephpp_harmonic_priming.pdf` | Sears, Verbeten & Percival, "Does Order Matter? Harmonic Priming Effects for Scrambled Tonal Chord Sequences," JEP:HPP 2023 | The BCMH corpus description (OI-179): 100 melodic-harmonic reductions, NCTs excluded, key + RN + scale-degree annotations, 10,056 chord tokens / 149 types (6,328/90 major, 3,728/93 minor), DCML-derived syntax. **No annotator identity or validation procedure is given** — the corpus citation is Verbeten & Sears 2019 (SMPC presentation, unpublished). |
| `mauch_dixon_2010_approximate_note_transcription.pdf` | Mauch & Dixon, "Approximate Note Transcription for the Improved Identification of Difficult Chords," ISMIR 2010 | NNLS-chroma audio front end (this is the ISMIR NNLS paper, not the 2010 TASLP DBN paper). Peripheral to the symbolic estimator; kept for the record. |

Copyright: personal-use copies for this project's research; do not redistribute (the Sears 2023 PDF
carries an explicit APA personal-use notice).

## Later additions, indexed under `BIBLIOGRAPHY.md` maintenance rule 2

The table above is the 2026-07-19 user-supplied set, and its sentence *"Each was read by Cowork on
2026-07-19"* is true of that set only. Files obtained later are indexed here so that sentence stays true.

| File | Citation | Added | State |
|---|---|---|---|
| `rohrmeier_2011_jmm_generative_syntax_tonal_harmony.pdf` (placed as `Rohrmeier2011.pdf`; renamed by the user later on 2026-09-12, confirmed at the listing) | Rohrmeier, "Towards a generative syntax of tonal harmony," *Journal of Mathematics and Music* 5(1), March 2011, pp. 35–53. DOI `10.1080/17459737.2011.573676`. **© 2011 Taylor & Francis — PAYWALL tier; do not redistribute.** | 2026-09-12, by the user | **NOT YET READ.** Identity established at page 1 only: title, author, journal, volume, issue, year, pagination and DOI all match `BIBLIOGRAPHY.md`'s row, whose title is title-cased where the article prints sentence case. 646,572 bytes, 20 PDF pages; pages 1, 2 and 20 opened, page 20 blank, pages 3–19 not opened. This is **candidacy row 22**, the grammar DP-O's *for* side rests on, and the user ruled it into L2's slice of Task B on the same date. |

| `granrothwilding_steedman_2012_icmc_statistical_parsing_jazz_chord_sequences.pdf` (placed as `icmc.pdf`; renamed by the user 2026-09-12, confirmed at the listing) | Granroth-Wilding & Steedman, "Statistical Parsing for Harmonic Analysis of Jazz Chord Sequences" — page 1 prints no venue or year; ICMC 2012 by row 25's citation | 2026-09-12, by the user | **NOT YET READ.** Page 1 only: title, two authors, University of Edinburgh; no licence line. 196,593 bytes, 8 pages. **Candidacy row 65**, ruled into L2's slice by the user the same day. |
| `granrothwilding_2013_phd_edinburgh_harmonic_analysis_ccg.pdf` (placed as `phd_thesis.pdf`; renamed by the user 2026-09-12, confirmed at the listing) | Granroth-Wilding, *Harmonic Analysis of Music Using Combinatory Categorial Grammar*, PhD thesis, University of Edinburgh, 2013 | 2026-09-12, by the user | **NOT YET READ.** Pages 1–2 only (title page; page 2 blank); no licence line seen. 1,331,533 bytes, 183 pages. **Candidacy row 66**, ruled into L2's slice the same day. |
| `jacoby_tishby_tymoczko_2015_jnmr_information_theoretic_chord_categorization.pdf` (placed as `jacobytishbytymockzo.pdf`; renamed by the user 2026-09-12, confirmed at the listing) | Jacoby, Tishby & Tymoczko, "An Information Theoretic Approach to Chord Categorization and Functional Harmony," *JNMR* 2015, DOI `10.1080/09298215.2015.1036888`. **Taylor & Francis download — PAYWALL tier; do not redistribute.** | 2026-09-12, by the user | **NOT YET READ.** Page 1 only, a publisher cover page. 2,217,625 bytes, 27 pages. **Candidacy row 67**, ruled into L2's slice the same day. |
| `A10383.pdf` (name as placed) | Hamanaka, Hirata & Tojo, "Grouping Structure Generator Based on Music Theory GTTM," IPSJ Journal 48(1), Jan. 2007, pp. 284–299. JAIST repository copy — LINK tier by default, licence not checked. | 2026-11-03, by the user | **Read at page images** by the Cowork sittings that booted on handoff entries 494 and 495, as handoff entry 495 and the OQ-L3-5 ruling record (`records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md`) relay; entry 495 records that its own read lacked the Japanese prose because the PDF does not embed its Japanese fonts, and the fix it found. 1,297,684 bytes, 17 PDF pages (a JAIST cover sheet, then pp. 284–299). Bears on OQ-L3-5 (GPR6, pp. 291–292). |
| `Camb_MusPerc2006.pdf` (name as placed) | Cambouropoulos, "Musical Parallelism and Melodic Segmentation: A Computational Approach," *Music Perception* 23(3), 2006, pp. 249–267. **© 2006 Regents of the University of California, all rights reserved — PAYWALL tier; do not redistribute.** | 2026-11-03, by the user | **READ WHOLE at page images** on 2026-11-03 by the sitting that booted on handoff entry 496 (its ruling record's §0). 1,177,256 bytes, 20 PDF pages, p. 268 blank. Bears on OQ-L3-5. |
| `CMA2016.pdf` (name as placed) | Hirata, Tojo & Hamanaka, "An Algebraic Approach to Time-Span Reduction," ch. 10 of an edited book, from p. 251; the book is not identified at the page read. PAYWALL tier by default. | 2026-11-03, by the user | **No read beyond its opening page is on the record.** 992,695 bytes. |
| `20068.pdf` (name as placed) | Tojo & Hirata, "Distance and Similarity of Time-span Trees," *Journal of Information Processing* 21(2), Apr. 2013, pp. 256–263, DOI `10.2197/ipsjjip.21.256`. LINK tier by default, licence not checked. | 2026-11-03, by the user | **No read beyond PDF pages 1 and 2 is on the record** (page 1 a JAIST cover sheet). 1,024,898 bytes. |

*The three renames were ordered by the user, could not be performed from the Cowork session of
2026-09-12 (the device shell reported the folder unreachable, and a copy under the new name would have
left the original beside it), and were then made by the user the same day; the rows above were updated in
one act after the folder's listing showed the new names and no old one.*

**★ A DUPLICATE IS RECORDED AND NOT ACTED ON.** The folder's own listing of 2026-09-12 shows
**`dcrr004.pdf`** at **1,648,192 bytes**, the same size as **`rohrmeier_2006_dcrr004_harmonic_movement.pdf`**,
which is the file `BIBLIOGRAPHY.md`'s DCRR-004 row points at and the one candidacy row 23 was read from.
**Whether the two are byte-identical was NOT checked** — no shell was run over either — and neither file
was deleted, moved or renamed. It is recorded here so a later session does not mistake it for a second
work by the same author. **★ RESOLVED BY THE USER LATER ON 2026-09-12: `dcrr004.pdf` was DELETED by the
user, and the folder's listing afterwards shows `rohrmeier_2006_dcrr004_harmonic_movement.pdf` alone, at
1,648,192 bytes, unchanged. Byte-identity was not checked by the session that recorded the duplicate, no earlier check is on the
record, and it is now not checkable; the
deletion was the user's decision. The paragraph above stands as the record of the question, #12.**

## Binary git home (2026-07-19)

Every PDF in this folder, plus the full batch-downloaded set of `BIBLIOGRAPHY.md` "wanted" rows and
the `tools/BCMH_dataset/` copy, is gitignored here and lives in git only in the private repo
**`slimvince/research-papers`** (visibility confirmed private before any push). This folder and
`tools/BCMH_dataset/` stay populated on disk for local reading — see `.gitignore`. `BIBLIOGRAPHY.md`
in this folder remains the canonical register; the private repo's `docs/BIBLIOGRAPHY.md` is a mirror.
