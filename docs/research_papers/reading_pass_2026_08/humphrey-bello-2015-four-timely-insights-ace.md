# FETCHED CONTENT RECORD — Humphrey & Bello 2015, "Four Timely Insights on Automatic Chord Estimation" (ISMIR 2015) — the TRUE paper behind R-9's mis-filed file

> **Retrieval record.** Fetched 2026-08-30 by the reading pass. The register's local file
> `docs/research_papers/humphrey_bello_2015_ismir_four_timely_insights_ace.pdf` contains a
> DIFFERENT paper (Chen, Su & Yang, electric-guitar playing-technique detection, ISMIR 2015 —
> confirmed at the object, page 1). **The register's own URL for this row
> (`archives.ismir.net/ismir2015/paper/000119.pdf`) points at the WRONG paper number: the true
> paper is `archives.ismir.net/ismir2015/paper/000294.pdf`** — which is the likely cause of the
> mis-file, recorded here for the bibliography reconciliation. Retrieved via
> `https://scispace.com/pdf/four-timely-insights-on-automatic-chord-estimation-2y4dkex8il.pdf`
> (the ISMIR archive and Zenodo download were unreachable from this environment). STRUCTURED
> CONTENT RECORD from two prompted extraction calls over the whole text — a bounded, declared
> read. Population row 21; CENTRAL — second independent pass owed.

## The four insights (as quoted)

1. "music recordings that invalidate tacit assumptions about harmony and tonality result in
   erroneous and even misleading performance"
2. "standard lexicons and comparison methods struggle to reflect the natural relationships
   between chords"
3. "conventional approaches conflate the competing goals of recognition and transcription to
   some undefined degree"
4. "the perception of chords in real music can be highly subjective, making the very notion of
   'ground truth' annotations tenuous"

## Setup

Systems: a k-stream GMM-HMM with multiband chroma, and a deep convolutional network over
constant-Q spectrograms with Viterbi decoding — AUDIO chord estimation. Ground truth: Isophonics
(200 tracks), McGill Billboard (700+), MARL/USPop+RWC (295) → 1,217 unique tracks; Rock Corpus
(200 rock tracks, TWO expert annotators — a pianist and a guitarist). Vocabularies: root,
thirds, majmin, mirex, triads, sevenths, tetrads, 157-class.

## Annotation disagreement and the ceiling (all popular music, audio-side)

- Rock Corpus human-human agreement: root 0.932, thirds 0.903, majmin 0.905, **tetrads 0.835**.
- Systems against the better-matching human reference: kHMM tetrads 0.590, DNN 0.540 — **both
  well BELOW the human-human 0.835**; as relayed verbatim: "the human annotators do agree a deal
  more that is attained by either system."
- Yet on a four-reference Beatles case no two human references exceed 65% tetrads agreement,
  while each system agrees with AT LEAST ONE human annotation for 89.1% (DNN) / 92.3% (kHMM) of
  the song — the systems sit INSIDE the space of human readings.
- Annotation-problem taxonomy: intonation (non-A440 recordings), chord-vocabulary inadequacy for
  whole genres, hierarchical label relations unresolved by flat classification. No quantitative
  errors-traced-to-annotation proportion.

## Positions

Recognition vs transcription are "two slightly different problems" conflated ("Chord
transcription is an abstract task related to functional analysis… Chord recognition… is quite
literal"). Recommendation: "Subjectivity in reference annotations should be embraced rather than
resolved" — multinomial regression / structured prediction over a "continuous-valued chord
affinity vector" synthesizing multiple human perspectives, instead of one-best flat labels.
