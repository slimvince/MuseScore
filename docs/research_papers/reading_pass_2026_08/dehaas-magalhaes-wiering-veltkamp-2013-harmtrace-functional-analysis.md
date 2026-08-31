# FETCHED CONTENT RECORD — de Haas, Magalhães, Wiering & Veltkamp 2013, "Automatic Functional Harmonic Analysis" (Computer Music Journal 37(4)) — the HarmTrace system

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the author's open copy
> `https://dreixel.net/research/pdf/hafha.pdf` (also: Utrecht TR CS-2011-023; publisher
> doi 10.1162/COMJ_a_00209). Environment bound as for every fetch of this pass: PDF binary not
> savable; STRUCTURED CONTENT RECORD from three prompted extraction calls over the whole text —
> a bounded, declared read. Population row 5; CENTRAL — second independent pass owed.

## Call 1 — input/output, grammar, error-correction, modulation

Input: a sequence of symbolic chord labels (Harte et al. 2005 syntax) + the KEY, given
externally ("key signatures in the score, or by applying an automatic key-finding algorithm").
No notes, no voicing. Output: a parse tree — chord labels as leaves, internal nodes the
functional structure.

Grammar: Haskell generalized algebraic datatypes; ~25 specifications expanded by parametrization
(mode, chord class, scale degree). Top categories tonic/dominant/subdominant, "where a
subdominant structure must always precede a dominant structure." Secondary dominants: Spec 16 —
"every scale degree, independently of its mode, chord class, and root interval, can be preceded
by a chord of the dominant class, one fifth up"; parallel-mode borrowing by Specs 23–24 (mode
change, root kept). Interference: "Spec. 16 and 17 interfere with Spec. 4–11, however, causing
multiple analyses. Because we prefer, e.g., a II m, V 7, and I to be explained as Sub, Dom, and
Ton, we constrain the application of Spec. 16 and 17."

Error-correcting parsing: "Chords that do not fit the structure are automatically deleted or
preceded by inserted chords"; search over deletion/insertion combinations to depth three,
fewest-corrections preferred. On 5,028 songs "the parser never crashes or refuses to produce
valid output" (3.38 deletions, 9.85 insertions per song average).

**Modulation, verbatim:** "even with a constrained modulation specification that allows
modulation only to specific other keys, and restricts the number of modulations, the total
number of ambiguous analyses quickly explodes" → "we chose to first explore the usability of
HarmTrace without modulation." Recommended route: external key-finding segments the piece into
single-key sections, HarmTrace per section.

## Call 2 — experiments, ambiguity, style, runtime

Datasets: 72 manually-checked jazz-leaning sequences; 5,028 user-generated Band-in-a-Box
sequences (jazz, Latin, pop, classical — "real world", with errors and modulations).
Parse statistics: deletions/song 0.83 / 3.38; insertions/song 2.79 / 9.85; corrections/song
3.63 / 13.24; chords/song 42.49 / 62.05; parse time/song 10.00 / 76.53 ms; totals 0.72 s /
384.81 s. Deleted chords under 6% of chords parsed (large set). No retrieval/MAP results in this
paper.

Ambiguity: preferred analyses selected by CONSTRAINING rule application (typed structure);
recursion-depth parameter 5–7 (too low → bad analyses; high → slow error correction); residual
ambiguity accepted in small numbers; "for some pieces, the number of parse trees grows
exponentially."

Style: ONE grammar with a declared jazz bias ("the harmony model exhibits a bias towards jazz
harmony"); ii–V–I and tritone substitution built in; a Bach chorale shown analyzable. No
separate per-style grammars in this paper.

## Call 3 — theory base, limits, validation, citations

Theory: Rohrmeier's generative grammar (2007 SMC; 2011 JMM 5(1) 35–53), Riemann's three
functions, hierarchical recursion in the GTTM spirit; Steedman 1984 jazz grammar cited.

Limits: no modulation (mode change only, root fixed); voice leading explicitly ignored ("For
simplicity, we ignored voice-leading"); phrase clustering deferred to post-processing on
metrical positions.

**Validation: parse statistics only — no ground-truth comparison of the analyses themselves**;
correctness shown by worked examples and downstream use (Chordify). "we evaluate its parsing
performance" — parsing, not harmonic accuracy.

No probabilistic or semi-Markov models cited; rule precedence, not probability.
