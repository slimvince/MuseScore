# FETCHED CONTENT RECORD — "BACHI: Boundary-Aware Symbolic Chord Recognition Through Masked Iterative Decoding on Pop and Classical Music" (arXiv:2510.06528v2; the disposition surface files it as ICASSP 2026)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from `https://arxiv.org/html/2510.06528`
> (the abs page yielded only the abstract; the HTML full text yielded the body). Author names were
> not relayed by the extraction call — to be filled at the second pass or from the demo page.
> Environment bound as for every fetch of this pass: STRUCTURED CONTENT RECORD from prompted
> extraction over the full text — a bounded, declared read. Population row 12 (not central;
> benchmarking comparable per the disposition surface).

## Input and output

Input: piano roll P ∈ {0,1}^(T×88) — **MIDI pitch, not spelled pitch** — at 12 frames per beat;
1D-CNN patch embedding (kernel 6) to d_model 512, temporal reduction T→T/6, GLU normalization.
Output: per chord, root × quality × bass (e.g. C/G = C root, major quality, G bass).

## Architecture

- **Boundary detection:** six transformer encoder blocks → hidden states H; an MLP predicts a
  binary chord-boundary sequence e (binarized from chord labels — a SEPARATELY SUPERVISED
  signal). Boundaries condition the model by feature-wise linear modulation:
  Z_t = LN(H_t)⊙(1+γ_t)+β_t with (γ_t, β_t) from [H_t; e_t]. Boundaries are NOT a decoded
  variable of the labeling search.
- **Masked iterative decoding:** single-layer transformer decoder over the three chord elements;
  all three start [MASK]; per iteration the highest-softmax-confidence element is committed;
  three iterations; no autoregression. Framed as mirroring ear-training practice.

## Data and results

Classical corpus: When-in-Rome + DCML functional-harmony repositories, deduplicated, ~1,500
pieces, annotations converted to absolute chord labels via music21; 9:1 split, 12-key
augmentation. POP909-CL: corrected POP909 (909 Chinese pop songs, MIDI) — professional musicians
fixed 40.6% misaligned start beats, 14.2% missing key-signature changes, 2.6% wrong time
signatures.

Macro-accuracy per piece (root / quality / bass / full):
- Classical: rule-based 54.6/45.8/50.5/28.4; AugmentedNet 73.9/74.2/72.3/57.2; ChordGNN
  73.0/73.7/71.0/58.5; Harmony Transformer v2 76.1/76.8/75.2/62.1; **BACHI 77.8/79.0/77.0/68.1**.
- POP909-CL: rule-based 85.9/69.7/85.8/65.0; AugmentedNet 88.6/84.5/90.5/78.7; ChordGNN
  80.7/82.0/82.7/71.6; HT v2 90.5/86.9/92.1/82.2; **BACHI 89.6/86.8/91.3/82.4**.

Ablation (classical, full-chord column): without boundary detection & iterative decoding 66.1;
without iterative decoding 65.6; with key detection 67.6; full BACHI 68.1. (Note: the root/
quality/bass columns barely move across ablations — the gains concentrate in the FULL-chord
joint column, i.e. in consistency of the three elements.)

## The repertoire-ordered decoding finding (as quoted by the extraction)

Classical: "the model tends to predict quality first (with the ratio 40.8%). The most frequent
prediction chain is quality→root→bass (33.2%)…" Pop: "the model tends to predict bass first
(66.9%), as the most frequent chain is bass→root→quality (56.4%). This is consistent with
bass-led cues in pop." — "confidence-ordered decoding adapts to genre-specific patterns."

## Availability

Code, trained models and POP909-CL released: `https://andyweasley2004.github.io/BACHI/`.
