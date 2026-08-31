# FETCHED CONTENT RECORD — Kantarelis, Dervakos, Kotsani & Stamou, "Musical Harmony Analysis with Description Logics" (DL 2021 workshop, CEUR Vol-2954 paper 20) — the open precursor of the Functional Harmony Ontology (population row 6)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the open workshop copy
> `https://ceur-ws.org/Vol-2954/paper-20.pdf`. **The journal version — "Functional harmony
> ontology: Musical harmony analysis with Description Logics", Journal of Web Semantics 2023,
> doi 10.1016/j.websem.2022.100754, same four authors (NTUA) — is PAYWALLED and no open copy
> was found in three attempts; its identity is pinned at the citation and its content is NOT
> carried here.** This record is the workshop precursor, read whole via one prompted extraction
> call (standing bound in `reading_pass/additions.md`).

## The ontology

Formalizes tertian chords (triads through thirteenths), suspended and non-tertian variants;
keys over ALL SEVEN diatonic modes (Ionian…Locrian) plus harmonic/melodic minor; the three
harmonic functions (tonic, dominant, subdominant) with RELATIVE/PARALLEL and LOCAL variants;
progressions via hasNext/hasPrevious. Expressivity ALEHIF (OWL 2 RL compatible); 4,347 classes,
4 object properties, 21,131 logical axioms. Function assignment by axioms of the shape
"CIonianFifth ∧ ∃hasNext.CIonianFirst ⊑ CIonianDominant"; local tonics by e.g.
"DominantChord ∧ ∃hasNext.LocalTonic ⊑ LocalDominant".

## Input assumptions

Chord-symbol sequences; the tonality GIVEN where full functional analysis is wanted (the
HarmTrace comparison needs the key), and where it is not known, only local/parallel-function
queries run — their own words: "the tonality of each song is not known, so we are not able to
define the tonic center." No notes, no voice leading, no cadence detection, flat classification
(no parse trees — HarmTrace's hierarchy noted as that system's benefit).

## Evaluation

Datasets: Isophonics Beatles; McGill Billboard (740 songs); Weimar Jazz Database (456
improvisations); a Hooktheory scrape (743 progressions). Against HarmTrace on 16,883 chords:
HarmTrace 1,253 s total (1.68 s/progression), 3,832 deletions + 4,768 insertions, 3,264
tonic-function and 7,604 dominant-function objects; this system 2,767 tonic / 7,529 dominant
with NO insertions or deletions; "resulting analyses are in most cases identical". Genre
statistics via SPARQL: jazz 55% dominant-function chords vs pop-rock 34% (25% subdominant).

## Scope notes for this project

Seven-mode support exists in the FORMALIZATION; the evaluation stays major/minor-leaning. No
inference from notes anywhere. Future work: education tools, MIDI/MusicXML→RDF.

*(A possibility recorded for the row-7 STOP rather than decided: this NTUA line formalizes all
seven modes with parallel/local functional readings — if the workbook's "Modal Harmony
Ontology" rows R170–R173 in fact describe this family rather than a separate Lazzari work, the
row-7 STOP dissolves into this row. Only the workbook's own row text can settle that.)*
