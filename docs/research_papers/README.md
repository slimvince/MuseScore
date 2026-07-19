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

## Binary git home (2026-07-19)

Every PDF in this folder, plus the full batch-downloaded set of `BIBLIOGRAPHY.md` "wanted" rows and
the `tools/BCMH_dataset/` copy, is gitignored here and lives in git only in the private repo
**`slimvince/research-papers`** (visibility confirmed private before any push). This folder and
`tools/BCMH_dataset/` stay populated on disk for local reading — see `.gitignore`. `BIBLIOGRAPHY.md`
in this folder remains the canonical register; the private repo's `docs/BIBLIOGRAPHY.md` is a mirror.
