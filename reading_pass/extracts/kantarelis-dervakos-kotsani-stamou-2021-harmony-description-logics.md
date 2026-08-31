# EXTRACT — Kantarelis, Dervakos, Kotsani & Stamou 2021, "Musical Harmony Analysis with Description Logics" (DL 2021, CEUR Vol-2954) — population row 6 (open precursor; JWS 2023 journal version paywalled), first pass

> **Establishment bound:** the workshop precursor read whole 2026-08-30 via one prompted
> extraction call over the open CEUR copy; the paywalled journal version's content is NOT
> carried — only its citation identity. Route and limits in the fetched content record.

## Claims, labeled

- **[FACT — §ontology]** A description-logic ontology (ALEHIF; 4,347 classes; 21,131 axioms)
  assigns tonic/dominant/subdominant functions — with parallel and LOCAL variants — to chords
  in symbol sequences, over a key vocabulary spanning ALL SEVEN diatonic modes plus
  harmonic/melodic minor.
- **[FACT — §input]** Function assignment presupposes the chord labels, and full (global)
  functional reading presupposes the TONALITY; where the key is unknown the system can only
  query local/parallel functions — "we are not able to define the tonic center."
- **[FACT — §evaluation]** Against HarmTrace on 16,883 chords the functional readings are "in
  most cases identical", with this system performing no insertions or deletions where
  HarmTrace's error-correcting parser performed 8,600; no ground-truth grading of either
  system's analyses exists in the paper.
- **[FACT — §evaluation]** Genre statistics: 55% dominant-function chords in the jazz corpus vs
  34% in pop-rock — corpus description, not analysis validation.
- **[CONJECTURE]** Education-tool and MIDI/MusicXML→RDF applications — future work.

## Coupling facts (mandatory)

- **Assumes upstream:** decided chord symbols; a decided tonality for global functions; single
  progression streams (hasNext chains). No notes, ever.
- **Hands downstream:** per-chord function classes (flat — no hierarchy, no cadences, no
  boundaries), SPARQL-queryable.
- **Stated scope:** knowledge representation and querying over given analyses; rhythm, melody,
  structure explicitly out.

## Bearing on the framework (first pass)

- **Δ4 confirmed again at a second, independent primary:** like HarmTrace (row 5), the
  functional-ontology branch DECIDES functions only over given chords with tonality assumed —
  its input is what the framework's L2 settlement already IS. Not counter-evidence to deriving
  the Roman numeral inside the one decision; exactly the disposition surface's reading.
- **The mode question:** a seven-mode FUNCTIONAL vocabulary exists formalized (against the
  list's "mode-specific functional harmony a larger gap still" — the gap claim survives in that
  the seven-mode part is formalization, not validated inference; nothing here infers a mode
  from notes).
- **DP-A/DP-O:** no bearing beyond what rows 5 and the surface already carry; flat
  classification, no hierarchy, no falsifier candidate.

## Verification targets touched

- None of V1–V13 originates here.
