# FETCHED CONTENT RECORD — Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, "Towards a Unified Model of Chords in Western Harmony" (Music Encoding Conference 2021)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the author's open copy
> `https://apmcleod.github.io/pdf/mec-chord-model.pdf`. Environment bound as for every fetch of
> this pass: PDF binary not savable here; STRUCTURED CONTENT RECORD from two prompted extraction
> calls over the whole text — a bounded, declared read. Population row 3; CENTRAL — second
> independent pass owed. Note the author set: this is a DCML-family paper (Hentschel, Moss,
> Neuwirth, Rohrmeier) with McLeod — the disposition surface filed it in the McLeod & Rohrmeier
> family, which the author list supports.

## Call 1 — problem and model

Problem: fragmented, heterogeneous chord representations across styles and annotation systems;
"the consistent representation and comparison of harmony across a wide range of styles…is a
challenging task."

Pitch-class types, three, hierarchically related: **generic** (letter A–G), **spelled** (letter +
accidental), **enharmonic** (MIDI mod 12). Conversion is one-directional — "An SPC can be
converted into an EPC or a GPC, but not vice versa" — so abstraction never destroys spelling.
Equivalences (octave, enharmonic) are FLAGS applied per pitch class or per chord, never
destructive normalization.

Modes are first-class: MODE := Maj | Min | Dor | … | INTERVAL* — the diatonic modes by name plus
arbitrary interval collections (octatonic, hexatonic, pentatonic representable); a KEY is tonic +
MODE + optional hierarchy type (Global/Local/Secondary). Where a mode defines exactly one spelled
interval per generic pitch class, scale degrees map one-to-one; otherwise relative pitches stay
interval-defined.

Chord: a graph structure — CHORD := <POS, HARMONY>; HARMONY := <NOTE*, [KEY],
[(CHORDFUNC [of: THEORY])*], …> with chord type, inversion, enharmonic flag optional. A NOTE's
PITCH may be a pitch class + octave, an interval above a reference, or a scale degree. The model
is "well-defined for theories which do not specify information at each level," representing what
is explicit and "inducing others where possible."

## Call 2 — standards, operations, limits, availability

Standards discussed for translation: figured bass, Roman numerals (generic and specific),
Riemannian function symbols, absolute chord syntax (Harte et al.), Forte pitch-class sets,
Tonfeld labels. Secondary dominants and borrowings handled by the key's Type feature. **The
cadential six-four is NOT discussed as a translation flashpoint in this paper** (the disposition
surface's flashpoint claim for DP-N rests on the When-in-Rome meta-corpus paper, not on this
one).

Operations: PC-type conversions; scale-degree derivation from root + key; interval re-expression;
equivalence flags; graph queries — example given: "What scale degrees occur as suspensions in V
chords?"

Suspensions representable as note functions — "Suspension [of: (NOTEFUNC | PITCH)]"; non-chord
tones ignorable per standard; seventh-chord type vocabulary MajMaj7 … AugMin7; no worked ♯11/♭9
encodings beyond the interval framework.

Limits/future: "While the model may not be exhaustive, its general and flexible nature ensures
its extensibility: Its only requirement is that 'chord' in the sense of a collection of pitches
is a meaningful concept in this style." — "a first step."

Availability: formal definition, standards comparison and examples at
`https://github.com/DCMLab/chord-model`.
