# EXTRACT — de Berardinis et al. 2023, "ChoCo" (Scientific Data 10) — population row 8 (with the Polifonia ontology members it carries), first pass (single pass; not central)

> **Establishment bound:** read 2026-08-30 via one prompted extraction call over the open full
> text (route in the fetched content record).

## Claims, labeled

- **[FACT — §workflow]** Converting Roman numerals to absolute chord labels LOSES the
  functional information, and ChoCo's own rule is therefore ADDITIVE — the converted annotation
  is added beside the Roman-numeral original, never replacing it ("the Roman Numerals contain
  information that would otherwise be lost").
- **[FACT — §workflow]** Cross-notation conversion is acknowledged one-of-several-possible —
  "the generated conversion, although correct, may only be one of several possible conversions."
- **[FACT — §data]** Scale of the integration: 18 datasets, 20,086 files, 1.58M chord
  occurrences, 7,281 unique chord classes, dual audio/symbolic time bases in one JAMS schema;
  RDF via the JAMS Ontology + Roman Chord Ontology (Polifonia Ontology Network).
- **[CONJECTURE]** None carried — a resource paper.

## Coupling facts (mandatory)

- **Assumes upstream:** existing annotation datasets; per-family parsers.
- **Hands downstream:** one harmonized corpus + knowledge graph; additive multi-notation
  annotations.
- **Stated scope:** representation and integration; no analysis algorithm, no evaluation of any
  analysis.

## Bearing on the framework (first pass)

- **DP-L / §7 data design — same direction, independent of the McLeod family:** a large
  engineering effort arriving at the same two rules the framework's data design already
  carries — keep the functional (key-relative) reading first-class rather than collapsing to
  absolute labels, and treat cross-representation conversion as lossy/ambiguous rather than
  normalizing destructively (the unified chord model's non-destructive-equivalence position,
  row 3, from a different group).
- **Corpus intake (routed forward by the surface):** ChoCo's 18-dataset inventory is a ready
  index for any later corpus search; enters under the ruled intake discipline only, research
  tier.
- No bearing on any framework cut; no falsifier candidate.

## Verification targets touched

- None of V1–V13 originates here.
