# FETCHED CONTENT RECORD — Feisthauer 2021, "Annotation automatisée des métadonnées structurelles dans les partitions musicales: cas des modulations et des cadences pour la forme sonate" (PhD thesis, Université de Lille, CRIStAL; defended 2021-05-18) — population row 16, "the Lille thesis"

> **Retrieval record.** Fetched 2026-08-30 from the university's open deposit
> `https://pepite-depot.univ-lille.fr/LIBRE/EDSPI/2021/2021LILUI032.pdf` (identity confirmed at
> the title page last slice). **Read grade, declared:** this is a CHAPTER-LEVEL STRUCTURED READ
> of a book-length French thesis — three prompted extraction calls covering the structure and
> contributions, chapter 5 (tonality/modulations) in detail, and chapters 6–7 (cadences, medial
> caesura, conclusions). It is NOT a page-by-page whole read; if the user wants that, it is its
> own session slice. The standing environment bound of `reading_pass/additions.md` applies.

## Structure and contributions

Seven chapters: introduction; musicological foundations (tonality, cadence typology, sonata
form); state of the art; corpora; tonality/modulation estimation; cadence and medial-caesura
detection; conclusion. Contributions: Mendelssohn string-quartet encodings (6 quartets + 4
pieces, staged quality assessment); Mozart string-quartet annotations (keys, modulations,
cadential points, form); a modulation corpus from five theory textbooks (the DLfM 2020
collaboration's material); a dynamic-programming tonality tracker on three criteria; a
descriptor-based cadence classifier; medial-caesura detection.

## Chapter 5 — the tonality/modulation model

Three criteria: tonal anchoring (a V→I strength measure per beat and key), note compatibility
(diatonic distance of sounding notes to a candidate key's collection), and key proximity
(Weber-style weighted distance between consecutive keys). States = beat × 24 keys; dynamic
programming minimizes the combined distance; output = a key per beat + modulation points.
Input: the symbolic score with beats; no chord analysis presupposed. Reported: tonality correct
on "about 85% of the corpus's beats" (Mozart quartets); comparisons discussed against the
Nápoles López HMM and Micchi et al. 2020 (the extraction relays ~82.9% for the neural model on
Mozart themes) largely qualitatively; no ablation of the three criteria. Stated limits:
beat-segmentation dependency; the stability penalty can miss rapid modulations in developments;
chromatic alterations outside the scale under-covered; the modulation/tonicization boundary
"porous".

## Chapters 6–7 — cadences, medial caesura, conclusions

Cadence detection by high-level descriptors (arrival-chord, rhythmic, local-context and
longer-past descriptors) + a classifier: PAC F1 0.80 on the 48 Bach WTC fugues; PAC F1 0.69 on
Haydn quartets (precision > 80%); HC F1 0.29 (high false-positive rate) — PAC "satisfaisante",
HC "peut être améliorée". Medial caesura: more abstract descriptors (dominant arrival,
prolongation, hammer blows, texture change); located correctly "for half the corpus" on a very
small training set. Conclusions: the ~85% tonality figure, the three corpora, and the open
items — half-cadence detection, medial-caesura data scarcity, scaling to full sonata-form
analysis, and "refining the interplay between local and global tonality estimation". Key
estimation and cadence detection are built as SEPARATE problems; their circularity is noted
theoretically, not formalized.

## The dual-tonality statement (chapter 2 §2.2, verbatim as relayed)

"à chaque moment de la partition, on pourra associer deux tonalités, celle de la modulation et
celle de la tonicisation" — at each moment of the score one can associate TWO tonalities, the
modulation's and the tonicization's. The specialized corpus annotates both; the chapter-5
algorithm reports modulation performance without separate tonicization metrics.
