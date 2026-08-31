# FETCHED CONTENT RECORD — de Berardinis et al. 2023, "ChoCo: a Chord Corpus and a Data Transformation Workflow for Musical Harmony Knowledge Graphs" (Scientific Data 10) — with the Polifonia representation-ontology family it carries

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the open article at
> `https://www.nature.com/articles/s41597-023-02410-w`. STRUCTURED CONTENT RECORD from one
> prompted extraction call over the whole text — a bounded, declared read (standing bound in
> `reading_pass/additions.md`). Population row 8 (representation ontologies): this one paper
> covers ChoCo itself, the JAMS Ontology and the Roman Chord Ontology (both members of the
> Polifonia Ontology Network); the older Music Ontology / Chord Ontology remain a separate
> small item.

## What ChoCo is

An integration of **18 source datasets** of harmonic annotations into one collection: 20,086
JAMS files (2,283 audio-timed; 17,803 symbolic/score-timed), 60,263 annotations — 20,530 chord
and 20,029 tonality annotations; 1,575,409 chord occurrences over 7,281 unique chord classes.

## Representation and workflow

Four notational families harmonized — Harte (the conversion reference), Roman numerals,
leadsheet dialects, polychords — all encoded in JAMS (audio time in seconds; symbolic time in
measures/beats). Pipeline: (1) a metadata extractor over heterogeneous source formats (LAB,
CSV, TXT, SQL, MusicXML, ABC, iReal, proprietary) → JAMS; (2) a chord converter — music21 for
Roman numerals, context-free grammars for leadsheet dialects, direct parsing for polychords —
into Harte; (3) JAMS → RDF via SPARQL Anything with the JAMS Ontology and the **Roman Chord
Ontology** (functional-harmony elements), both in the Polifonia Ontology Network; a ~30-million-
triple knowledge graph with 4,000+ external links.

## The information-preservation position (verbatim as relayed)

"if the original annotation contains Roman Numerals chords, the new (converted) annotation is
added to the existing one, since the Roman Numerals contain information that would otherwise be
lost, i.e. the harmonic functions that the chords hold within the piece." And on conversion
ambiguity: "whenever this happens, the generated conversion, although correct, may only be one
of several possible conversions."

## Validation and availability

Four musicians (5+ years training) reviewed 250 parsing rules and converted outputs; metadata
>90% accuracy/coverage on most collections. Open licences; JAMS data at Zenodo
(doi 10.5281/zenodo.7706751); ontologies at the polifonia-project GitHub.
