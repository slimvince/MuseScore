# FETCHED CONTENT RECORD — McLeod & Rohrmeier 2021, "A Modular System for the Harmonic Analysis of Musical Scores using a Large Vocabulary" (ISMIR 2021)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass (commission
> `cowork_reading_pass_commission_2026_08_30.md`) from the author's open copy
> `https://apmcleod.github.io/pdf/ismir-harmony.pdf` (also at
> `https://archives.ismir.net/ismir2021/paper/000054.pdf`). **This environment cannot save the
> PDF binary** (the same bound `docs/research_papers/BIBLIOGRAPHY.md` already records for its own
> folder), and the session's web-fetch tool answers structured prompts over the full text rather
> than returning it verbatim. This file is therefore a STRUCTURED CONTENT RECORD assembled from
> three prompted extraction calls over the whole paper — **a bounded, declared read: the whole
> text was machine-read; what stands here is relayed through that tool, not page-images read at
> the object.** Anything carrying load cites this bound. Population row 1; CENTRAL — the second,
> independent extraction pass is owed and must re-fetch rather than consult this file.

## Call 1 — the system (prompt: modules, vocabulary, decoding, input/output, spelling)

Six modules, pipeline order:
- **Chord Transition Model (CTM).** Input: note sequence ordered by onset — spelled pitch class
  (A–G, double-flat…double-sharp), octave, normalized MIDI height, metrical levels, duration,
  inter-note intervals. Output: per note, a binary "begins a new chord" decision (first output
  fixed 1; simultaneous notes forced 0). Feed-forward + Bi-LSTM.
- **Chord Classification Model (CCM).** Input: note subsequence with two flanking context notes
  each side; relative temporal position, relative pitch, relative octave. Output: distribution
  over all 1540 absolute chord symbols, holistic — the paper's stated reason: separate per-field
  outputs can produce inconsistent combinations ("It would be possible to treat each aspect of a
  chord symbol… as separate features… However, this approach doesn't make sense conceptually…
  important that every feature of a chord is considered holistically.")
- **Chord Sequence Model (CSM).** Input: relative chord symbols (root as line-of-fifths interval
  above the key tonic). Output: distribution over the next relative chord (1276 within ±14
  fifths). Variants: CSM (full), CSM-I (inversion-invariant, 348), CSM-T (triad-reduced, shared
  weights).
- **Key Transition Model (KTM).** Input: relative chord sequence from the piece's start; at a key
  change the hidden state is reverted and the chord re-encoded in the new key. Output: P(chord i
  is in a different key than chord i−1).
- **Key Sequence Model (KSM).** Same input; output: distribution over the new key — tonic within
  ±14 fifths of the previous key, mode major/minor, 58 possibilities at a change; active only on
  key changes.
- **Initial Chord Model (ICM).** Input: mode; output: prior over the first relative chord —
  counts from training data with additive smoothing (1/1540 per count).

Vocabulary: **1540 chords** = 35 spelled roots × 12 types (major, minor, augmented, diminished
triads; major-7, minor-7, dominant-7, diminished-7, half-diminished-7 and further seventh
variants) × inversions (3 for triads, 4 for sevenths). **70 keys** = 35 spelled tonics × 2 modes.
Spelled pitch throughout (A♯ ≠ B♭); relative roots on the line of fifths −14…+14.

Decoding: beam search over complete labeled paths — all segmentations consistent with CTM
thresholds (ctmin/ctmax, a maximum window duration C_durmax, valid predecessor/successor), each
window assigned chord and key. A merge rule lets consecutive identical-chord windows merge where
the CCM rates both high — introduced to override CTM over-segmentation. Path probability:
P(cm) = Pct(cm) · [Pcc(cm)·Pkt(cm)·Pseq(cm)]^(1/|cm|), the exponent normalizing by window count;
α scales the KSM (70 keys) against the CSM (>1000 chords).

Input: symbolic score — per note: spelled pitch class, octave, onset/offset, duration (in whole
notes), metrical level of onset and offset (downbeat / beat / sub-beat / other). Output: per
segment, absolute chord symbol (root, type, inversion) + local key (tonic, mode) + boundaries —
"nearly equivalent to a full RNA, lacking only altered chordal tones such as suspensions, and
pedal tones".

Design-position quotes captured: "Our modular design is such that each component models one
specific aspect of the full harmonic analysis task at the appropriate level, receiving only input
that is relevant to that aspect, and at the appropriate step length." / "Its output is highly
interpretable, which has significantly aided in its development…(1) locate mislabeled segments;
(2) examine the outputs of each component…"

## Call 2 — experiments and results (prompt: corpora, metrics, tables, ablations, error analysis)

Corpora: **internal corpus, 742 pieces** (16th–20th c.; Bach, Couperin, Grieg, Beethoven, Schütz,
Mozart, Corelli, Chopin, Kozeluh, Monteverdi, Mendelssohn, Schubert with ≥20 each + 99 more
composers; public subsets: Annotated Mozart Sonatas, ABC), and the **Functional-Harmony corpus,
201 pieces** (Beethoven 119, Schubert 29, Bach 24, others 19; TAVERN + BPS-FH + RomanText
combined). Both split 80/10/10 train/validation/test, random; hyperparameters and inference
parameters tuned on validation.

Metric: Chord Symbol Recall (CSR — proportion of TIME the ground truth matches), at root /
root+type / root+type+inversion / key / full (chord+key).

Table 1 as relayed:
| Model | Corpus | Root | +Type | +Inv. | Key | Full |
|---|---|---|---|---|---|---|
| Micchi et al. 2020 baseline | Internal | 57.0 | 47.7 | 37.6 | 64.9 | 29.0 |
| CSM | Internal | 76.6 | 68.8 | 62.1 | 66.9 | 44.7 |
| CSM-I | Internal | 76.5 | 68.7 | 62.0 | 69.0 | 46.3 |
| CSM-T | Internal | 77.6 | 70.0 | 62.8 | 70.2 | 46.9 |
| Micchi et al. 2020 baseline | F-H | — | — | — | — | 42.8 |
| CSM | F-H | 73.3 | 65.4 | 55.6 | 60.8 | 40.5 |
| CSM-I | F-H | 75.0 | 66.8 | 56.9 | 67.0 | 44.6 |
| CSM-T | F-H | 75.4 | 67.8 | 58.1 | 69.4 | 45.9 |

Ablation notes relayed: the three CSM variants within ≤2.0 CSR on the internal corpus; on F-H the
invariance helps mainly the KEY column (CSM-T 45.9 vs CSM 40.5 full). Inversion accuracy: root
position 71.5% / first 54.4% / second 38.3% / third 40.5%. Minor keys 44.6 vs major 40.9 CSR.
Standard CSM's distribution "more flat than desired"; rare chords get low probability, "makes the
model prefer key changes in these cases". Merge rule exists because "the CTM was over-segmenting
the input, and the thresholds were difficult to tune. However, the CCM's outputs were relatively
accurate."

Error-inheritance quote (verbatim as relayed): "Interestingly, the baseline performs relatively
well on key detection (even on our internal corpus), which points to one downside of our modular
approach: the key depends on outputs from the other components, adding noise to the process,
which isn't a factor for the end-to-end baseline."

## Call 3 — scope, assumptions, related work, availability

Scope and limits, in the paper's words: output "nearly equivalent to a full RNA, lacking only
altered chordal tones such as suspensions, and pedal tones, which we intend to include in future
work"; applied chords are not output directly — "we treat them as brief, potentially recursively
embedded, key changes."

Input assumptions: symbolic, spelled ("we use spelled pitches (where an A♯ is a different pitch
from a B♭)"), polyphonic, notes ordered by onset (equal onsets by increasing pitch), metrical
levels required; quantization implicit.

Related-work positions: prior statistical models (Raphael & Stoddard 2004; Temperley 2009;
Aitken, O'Donnell & Rohrmeier SMC 2018) use "an enharmonic MIDI pitch representation…a small
vocabulary of chord types, and no inversions". Chen & Su 2018 uses piano-roll/MIDI pitch; Chen &
Su 2021 spelled output but reduced pitch-class set; the comparison baseline is **Micchi, Gotham &
Giraud 2020 (TISMIR 3(1) 42–54)** — same pitch representation and roughly the same chord
vocabulary.

Future work: suspensions and pedal tones; graded metrics; MIDI/audio front-ends (retrain CTM+CCM
only); a human-in-the-loop annotation tool re-running the search after expert edits; annotation
differences between the two corpora.

Availability: "All code and models are available online. http://github.com/apmcleod/harmonic-inference".
Licence not stated in the paper (the disposition surface records GPL-3.0 for the implementation —
verify at the repository before any use).

*(The disposition surface's relayed claim that the implementation takes MusicXML in and writes
annotations onto MuseScore3 files was NOT confirmed or denied by these three calls — it concerns
the repository, not the paper text. To be established at the repository if it ever carries load.)*
