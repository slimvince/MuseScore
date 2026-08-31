# EXTRACT — McLeod & Rohrmeier 2021, "A Modular System for the Harmonic Analysis of Musical Scores using a Large Vocabulary" (ISMIR 2021) — population row 1, CENTRAL, first pass

> **Establishment bound on every claim below:** read 2026-08-30 via three prompted extraction
> calls over the full text at the author's open copy (see the fetched content record beside this
> file for the retrieval method and its declared limits). Locations are given at section/table
> granularity as the tool relayed them, not at page/line. CENTRAL: a second, independent pass
> (fresh session, no consultation of this extract) is owed; disagreements resolve at the paper.

## Claims, labeled

- **[FACT — Table 1]** On the authors' internal corpus (742 pieces), the modular system (best
  variant CSM-T) reaches CSR root 77.6 / root+type 70.0 / +inversion 62.8 / key 70.2 / full 46.9
  against the end-to-end baseline (Micchi, Gotham & Giraud 2020) at 57.0 / 47.7 / 37.6 / 64.9 /
  29.0. On the Functional-Harmony corpus (201 pieces): CSM-T full 45.9 vs baseline full 42.8.
- **[FACT — Table 1 + discussion]** The end-to-end baseline's KEY column is competitive with the
  modular system's (64.9 vs 66.9–70.2 internal) while its chord columns are far behind; the
  authors' own diagnosis, verbatim: *"the key depends on outputs from the other components,
  adding noise to the process, which isn't a factor for the end-to-end baseline."*
- **[FACT — §system]** The chord label is decided HOLISTICALLY over 1540 whole symbols, not as
  separate root/type/inversion heads, with the stated reason that separate per-field outputs can
  combine inconsistently.
- **[FACT — §system]** Segmentation is part of the search: beam search ranges over segmentations
  consistent with the transition model's thresholds, jointly with chord and key labels; a merge
  rule was added because the transition model OVER-SEGMENTS and its thresholds were hard to tune.
- **[FACT — §system]** Applied chords are represented as brief, potentially recursively embedded
  KEY CHANGES, not as a separate chord-label field.
- **[FACT — §results]** Chord-vocabulary invariance in the sequence model (CSM-I/CSM-T) helps
  mainly the KEY column, on the smaller F-H corpus (full 40.5 → 45.9); on the internal corpus the
  three variants sit within ≤2.0 CSR.
- **[FACT — §results]** Inversion accuracy falls steeply below root position: 71.5 / 54.4 / 38.3
  / 40.5 (root/1st/2nd/3rd).
- **[FACT — §scope]** The output lacks suspensions, altered chordal tones and pedal tones by the
  paper's own statement; these are named future work.
- **[THEORY]** None carried — the paper is a system-and-measurement paper; its design arguments
  are positions, not established theory.
- **[CONJECTURE — §discussion]** That modules can be retrained per input format (MIDI/audio:
  retrain CTM+CCM only) while the rest carries over — stated, not measured.

## Coupling facts (mandatory)

- **Assumes upstream:** a SPELLED symbolic score (A♯ ≠ B♭), polyphonic, notes with octave,
  onset/offset, duration, and METRICAL LEVELS (downbeat/beat/sub-beat/other) already present —
  i.e., exactly the L0 contract this project's framework gives (spelling, meter given); no voice
  membership required. Quantization implicit.
- **Hands downstream:** a segmentation (chord windows), an absolute chord symbol (spelled root,
  type, inversion) per segment, a local key (spelled tonic, mode) per segment. No chord-tone
  assignment, no elaboration relations, no rivals published (beam holds alternatives during
  search and commits one) — so nothing like the framework's DP-K rival stream crosses its output
  boundary.
- **Stated scope:** notated Western tonal repertoire, 16th–20th c. corpus; Roman-numeral-style
  ground truth; suspensions/alterations/pedals excluded from the label space.

## Measured results (corpus, metric, value)

See Table 1 as carried in the fetched content record: CSR at five widths, two corpora, the
Micchi et al. 2020 baseline and three CSM variants; inversion-position accuracies; minor 44.6 vs
major 40.9 CSR.

## Bearing on the framework (first-pass reading; verdicts belong to the findings surface)

- **DP-A (no division of the deciding by published field):** the CCM's holistic 1540-symbol
  output is the same direction — the paper avoids per-field heads for the chord label itself.
  But the SYSTEM as a whole is a modular pipeline whose own authors document key-error
  inheritance — supporting the framework's ground for one entangled decision (and confirming the
  disposition surface's relayed MR015 claim at the primary).
- **DP-B/DP-E (tonality with the chords):** key decisions ride on chord outputs here (KTM/KSM
  read the chord stream), and the measured cost is stated by the authors themselves.
- **DP-C (segmentation decided with):** joint beam over segmentations+labels supports "with";
  their over-segmenting standalone transition model is evidence about boundary-first designs.
- **DP-D:** chord-tone assignment absent entirely — the 2024 companion paper (population row 2)
  is where that lives.
- **DP-K:** rivals are NOT published — consistent with the disposition surface's honest caution
  that no surveyed system publishes segmentation-differing rivals.
- **L2 detail-specification input:** the relative-chord line-of-fifths encoding, the ±14-fifths
  bounded key transitions, the α balance between key-change and chord-continuation scores, and
  the count-based smoothed initial-chord prior are all concrete mechanism candidates.

## Verification targets touched (population §3)

- None of V1–V13's figures originates here (the framework predates this paper's entry into the
  record and cites none of its numbers). No divergence to report.
