# FETCHED CONTENT RECORD — Nápoles López, Feisthauer, Levé & Fujinaga 2020, "On Local Keys, Modulations, and Tonicizations" (DLfM 2020; doi 10.1145/3424911.3425515)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the author's open copy
> `https://napulen.github.io/media/modulation_tonicization/napoles20local.pdf` (HAL's copy is
> behind an access gate for this environment). STRUCTURED CONTENT RECORD from two prompted
> extraction calls over the whole text — a bounded, declared read. **The per-textbook model
> scores below were relayed as APPROXIMATIONS read off the paper's Figure 3, not table values —
> carry none of them as exact.** Population row 13 (not central).

## Definitions (as quoted)

Modulation: "the change from one key to another" (departure and destination keys); Grove's line —
"a firmly established change of key, as opposed to a passing reference". Tonicization: "a brief
deviation to a different key, usually with the intention of emphasizing a certain scale degree or
harmony". Local keys: "predictions of the musical key provided by a local-key-estimation
algorithm" — with "no music-theoretical meaning inferred" a priori. Kostka & Payne acknowledged:
"The line between modulation and tonicization is not clearly defined in tonal music."

## Contributions

A methodology comparing local-key predictions against BOTH modulation and tonicization ground
truths; a new annotated dataset — 201 excerpts, 2,002 labels, from five theory textbooks
(Aldwell/Schachter/Cadwallader 7 files, Kostka & Payne 15, Reger 117, Rimsky-Korsakov 37,
Tchaikovsky 25; modulations 8/21/220/44/60; tonicizations 7/11/40/107/38); an evaluation of
three symbolic local-key models.

## Methodology mechanics

Onset-level key labels: every note onset carries a key from the modulation column (departure key
held until destination reached) and from the tonicization column (roman-numeral-implied key where
a tonicization is annotated, else copied from the modulation column). Score = duration-weighted
sum of w(k_i, l_i) over onsets (d_i in quarter notes): accuracy weights (1/0) and MIREX weights
(exact 1.0; dominant/subdominant 0.5; relative 0.3; parallel 0.2; other 0.0).

## Models and findings

M1 Nápoles López HMM (key profiles + key-distance tables); M2 Feisthauer proximity measure (M2a
untrained defaults, M2b trained on Mozart string quartets); M3 Micchi et al. 2020 LSTM; baseline
music21 global key. All symbolic input.

Findings as stated: M1 and M3 show a similar performance shape; both do poorly against
Rimsky-Korsakov's MODULATION ground truth and better against his TONICIZATION ground truth; M2b
worst overall and the only model better on modulations than tonicizations; MIREX weighting adds
roughly 10–20 points of partial credit. **Headline conclusion, verbatim:** local-key models
"show an inclination toward the tonicization predictions, rather than the modulation ones. This
is unexpected, as most researchers do not describe their local-key-estimation models as
'tonicization finders'."

Annotator diversity documented: Rimsky-Korsakov and Tchaikovsky tonicize 41.63% and 15.97% of
onsets respectively; the other three textbooks far fewer. "Roman numeral annotations are subject
to issues such as ambiguity and disagreement, which may have implications for determining where
the changes of key occur." Some tonicization roman numerals were supplied by the authors where
textbooks omitted them. Dataset too small to train on (no splits).

## Availability

Dataset CC BY 4.0 at `https://github.com/DDMAL/key_modulation_dataset` (Humdrum **kern +
harmalysis roman numerals).
