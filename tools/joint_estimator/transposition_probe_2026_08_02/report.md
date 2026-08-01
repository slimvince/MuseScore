# Transposition-equivariance probe — joint-estimator reference decode

Read-only exploratory measurement (the #17 funnel's read-only-probe stage; surprises are the
desired product of this stage, not a STOP). Nothing under the repository was written; all
artifacts live in this directory. Measurement tool: `run_probe.py` (this directory), driving the
repository's own pinned reference decoder `tools/joint_estimator/probe_decoder.py` at the
production configuration (seg_cap 4, the SELECTED weight vector from
`tools/joint_estimator/decode_parity_ref.json`, leftover freq, table_set all).

Sample: 12 pieces, every 27th of the name-sorted covered-stem list of the parity reference
(`bwv10.7, bwv153.1, bwv2.6, bwv245.37, bwv271, bwv297, bwv321, bwv347, bwv373, bwv398,
bwv420, bwv55.5`). Note-events source `tools/joint_estimator/note_events/note_events.json`,
provenance corpus git hash `e3d17c325d24e0de1213440043cbf02ac14f3d3e`.

## Input-transposition convention (declared before measurement)

k semitones maps to a raw line-of-fifths shift f_raw with 7*f_raw == k (mod 12), folded into
(-6, 6]: **+2 st -> +2 fifths; -3 st -> +3 fifths; +6 st -> +6 fifths** (the sharpward tritone
spelling is chosen for the ambiguous +6 case, and stated). Per piece the actual uniform respell
delta is engraver-style: the transposed signature is `sig_t = _fold_fifths_diff(sig + f_raw)`
(the repository's one fifths-folding helper, `tools/joint_estimator/gen_label_tables.py`), and
`delta_lof = sig_t - sig` (== f_raw mod 12). Every note: pc -> (pc+k) mod 12, midi -> midi+k,
lof -> lof+delta_lof; signature-fifths input -> sig_t; declared mode unchanged; contour, ties,
fermatas, meter unchanged.

## Predictions — REGISTERED BEFORE ANY TRANSPOSED DECODE (protocol step 3)

- **P1 (establishment, already measured):** the untransposed decode reproduces the committed
  parity reference exactly, 12/12 pieces (segments AND total_score). **Status: PASSED 12/12**
  (`establish_state.json`; header cross-check ok on all 12).
- **P2 (equivariance):** under each of +2, -3, +6 semitone transposition, the decode is
  equivariant — segment boundaries identical to the untransposed reading, key tonics and chord
  roots shifted by exactly k (mod 12), mode and chord-class labels identical — for **>= 99 % of
  segments** over the 12x3 = 36 piece-conditions.
- **P3 (violation locus):** the violations that do occur concentrate in **spelling-sensitive
  cells** — segments whose committed tonic or root pitch class crosses a canonical
  line-of-fifths wrap under the uniform respell (where
  `_PC_TO_FIFTHS[(pc+k)%12] != _PC_TO_FIFTHS[pc]+delta_lof`), i.e. spelling-table cells and
  signature-prior terms, not boundary placement. **+6 (the tritone) is the stress case** and is
  predicted to carry the majority of whatever violations exist; +2 and -3 are predicted
  near-perfect.

Per-violation diagnosis protocol (registered): for each violating segment, record piece, tick,
expected vs observed state; check whether the expected (shifted) state is even in the candidate
set; compare the per-factor feature vector of the original committed state on the original piece
vs the shifted expected state on the transposed piece, and name the factor that moved
(signature prior, spelling-table cell, or tie-break — a zero factor delta with a different
winner is a tie-break).

## Results

All 36 conditions (12 pieces x {+2, -3, +6}) decoded after the predictions above were registered.

### Per-piece, per-transposition results

| piece | k | sig -> sig_t | dlof | matched | boundaries identical | total-score delta | committed-tonic wrap pcs | anchor-wrap pcs (all 12) |
|---|---|---|---|---|---|---|---|---|
| bwv10.7 | +2 | -2 -> 0 | +2 | 27/38 | no | -1.7045 | [] | [6, 11] |
| bwv10.7 | -3 | -2 -> 1 | +3 | 25/38 | no | -0.2786 | [] | [4, 6, 11] |
| bwv10.7 | +6 | -2 -> 4 | +6 | 27/38 | no | -1.8612 | [7] | [2, 4, 6, 7, 9, 11] |
| bwv153.1 | +2 | 1 -> 3 | +2 | 19/29 | no | -1.1272 | [] | [6, 11] |
| bwv153.1 | -3 | 1 -> 4 | +3 | 11/29 | no | -0.3148 | [4] | [4, 6, 11] |
| bwv153.1 | +6 | 1 -> -5 | -6 | 12/29 | no | +2.1859 | [] | [0, 1, 3, 5, 8, 10] |
| bwv2.6 | +2 | -1 -> 1 | +2 | 22/32 | no | -3.8559 | [] | [6, 11] |
| bwv2.6 | -3 | -1 -> 2 | +3 | 16/32 | no | -2.8140 | [] | [4, 6, 11] |
| bwv2.6 | +6 | -1 -> 5 | +6 | 0/32 | no | -12.9678 | [2, 7] | [2, 4, 6, 7, 9, 11] |
| bwv245.37 | +2 | -3 -> -1 | +2 | 24/42 | no | +7.1134 | [] | [6, 11] |
| bwv245.37 | -3 | -3 -> 0 | +3 | 19/42 | no | +5.7752 | [] | [4, 6, 11] |
| bwv245.37 | +6 | -3 -> 3 | +6 | 14/42 | no | +4.9294 | [] | [2, 4, 6, 7, 9, 11] |
| bwv271 | +2 | 2 -> 4 | +2 | 23/34 | no | -1.6469 | [11] | [6, 11] |
| bwv271 | -3 | 2 -> 5 | +3 | 22/34 | no | -2.3683 | [4, 11] | [4, 6, 11] |
| bwv271 | +6 | 2 -> -4 | -6 | 21/34 | no | +1.8860 | [] | [0, 1, 3, 5, 8, 10] |
| bwv297 | +2 | 0 -> 2 | +2 | 36/36 | yes | +0.0000 | [] | [6, 11] |
| bwv297 | -3 | 0 -> 3 | +3 | 23/36 | no | -1.6180 | [] | [4, 6, 11] |
| bwv297 | +6 | 0 -> 6 | +6 | 2/36 | no | -15.0151 | [2, 9] | [2, 4, 6, 7, 9, 11] |
| bwv321 | +2 | -2 -> 0 | +2 | 26/26 | yes | -0.0000 | [] | [6, 11] |
| bwv321 | -3 | -2 -> 1 | +3 | 26/26 | yes | -0.0000 | [] | [4, 6, 11] |
| bwv321 | +6 | -2 -> 4 | +6 | 16/26 | no | -3.2763 | [] | [2, 4, 6, 7, 9, 11] |
| bwv347 | +2 | 3 -> 5 | +2 | 34/40 | no | -0.3689 | [11] | [6, 11] |
| bwv347 | -3 | 3 -> 6 | +3 | 22/40 | no | -2.6611 | [4, 11] | [4, 6, 11] |
| bwv347 | +6 | 3 -> -3 | -6 | 26/40 | no | -1.4450 | [] | [0, 1, 3, 5, 8, 10] |
| bwv373 | +2 | 1 -> 3 | +2 | 25/25 | yes | +0.0000 | [] | [6, 11] |
| bwv373 | -3 | 1 -> 4 | +3 | 19/25 | yes | -1.1451 | [] | [4, 6, 11] |
| bwv373 | +6 | 1 -> -5 | -6 | 21/25 | no | -0.9622 | [] | [0, 1, 3, 5, 8, 10] |
| bwv398 | +2 | 2 -> 4 | +2 | 38/38 | yes | +0.0000 | [] | [6, 11] |
| bwv398 | -3 | 2 -> 5 | +3 | 26/38 | no | -0.0672 | [4] | [4, 6, 11] |
| bwv398 | +6 | 2 -> -4 | -6 | 28/38 | yes | +0.8654 | [] | [0, 1, 3, 5, 8, 10] |
| bwv420 | +2 | 0 -> 2 | +2 | 29/31 | no | -0.4042 | [] | [6, 11] |
| bwv420 | -3 | 0 -> 3 | +3 | 21/31 | no | +0.2531 | [] | [4, 6, 11] |
| bwv420 | +6 | 0 -> 6 | +6 | 4/31 | no | -15.8116 | [2, 9] | [2, 4, 6, 7, 9, 11] |
| bwv55.5 | +2 | -2 -> 0 | +2 | 37/37 | yes | +0.0000 | [] | [6, 11] |
| bwv55.5 | -3 | -2 -> 1 | +3 | 36/37 | yes | -0.6677 | [] | [4, 6, 11] |
| bwv55.5 | +6 | -2 -> 4 | +6 | 34/37 | no | -0.0682 | [] | [2, 4, 6, 7, 9, 11] |

**Total: 811/1224 segments matched (66.26 %).** Per shift: k=+2: 340/408 (83.3 %); k=-3: 266/408 (65.2 %); k=+6: 205/408 (50.2 %).

**Exactly equivariant conditions (total-score delta 0.0, all segments matched): 6/36** — bwv297|+2, bwv321|+2, bwv321|-3, bwv373|+2, bwv398|+2, bwv55.5|+2.

### Every violation (piece | k, tick, expected vs observed)

Violation lines are `piece|k @tick [span]: expected (key, class, root_pc) vs observed`. `BND` marks a violation inside a condition whose segment boundaries moved (compared at the reference segment's start tick); `LBL` marks a label flip with identical boundaries.

```
BND bwv10.7|+2 @2400 exp span[2400, 2880] tonic9m V | Maj |  |  root4 | obs span[2400, 2880] tonic0M V | Dom7 |  | vi root4
BND bwv10.7|+2 @2880 exp span[2880, 3360] tonic9m I | Min |  |  root9 | obs span[2880, 3360] tonic0M VI | Min |  |  root9
BND bwv10.7|+2 @3360 exp span[3360, 3840] tonic9m V | Maj |  |  root4 | obs span[3360, 3840] tonic0M V | Maj |  | vi root4
BND bwv10.7|+2 @12480 exp span[12480, 13440] tonic9m IV | Min |  |  root2 | obs span[12480, 13440] tonic0M II | Min |  |  root2
BND bwv10.7|+2 @13440 exp span[13440, 13920] tonic9m I | Min |  |  root9 | obs span[13440, 13920] tonic0M VI | Min |  |  root9
BND bwv10.7|+2 @13920 exp span[13920, 15360] tonic9m V | Dom7 |  |  root4 | obs span[13920, 15360] tonic0M V | Dom7 |  | vi root4
BND bwv10.7|+2 @15360 exp span[15360, 18240] tonic9m I | Min |  |  root9 | obs span[15360, 18240] tonic0M VI | Min |  |  root9
BND bwv10.7|+2 @28800 exp span[28800, 30720] tonic0M V | Maj |  |  root7 | obs span[28800, 30240] tonic7M V | Maj |  | IV root7
BND bwv10.7|+2 @30720 exp span[30720, 32640] tonic9m II | Min |  |  root11 | obs span[30240, 32160] tonic7M V | Dom7 |  |  root2
BND bwv10.7|+2 @32640 exp span[32640, 33600] tonic9m I | Min |  |  root9 | obs span[32160, 33120] tonic9m I | Min |  |  root9
BND bwv10.7|+2 @33600 exp span[33600, 34080] tonic9m V | Min |  |  root4 | obs span[33120, 34080] tonic2m II | Min |  |  root4
BND bwv10.7|-3 @0 exp span[0, 960] tonic7M VI | Min |  |  root4 | obs span[0, 960] tonic4m I | Min |  |  root4
BND bwv10.7|-3 @960 exp span[960, 1920] tonic7M V | Maj |  |  root2 | obs span[960, 1920] tonic4m V | Maj |  | III root2
BND bwv10.7|-3 @1920 exp span[1920, 2400] tonic7M I | Maj |  |  root7 | obs span[1920, 2400] tonic4m III | Maj |  |  root7
BND bwv10.7|-3 @28800 exp span[28800, 30720] tonic7M V | Maj |  |  root2 | obs span[28800, 30240] tonic2M V | Maj |  | IV root2
BND bwv10.7|-3 @30720 exp span[30720, 32640] tonic4m II | Min |  |  root6 | obs span[30240, 32160] tonic2M V | Dom7 |  |  root9
BND bwv10.7|-3 @32640 exp span[32640, 33600] tonic4m I | Min |  |  root4 | obs span[32640, 33120] tonic4m I | Min |  |  root4
BND bwv10.7|-3 @33600 exp span[33600, 34080] tonic4m V | Min |  |  root11 | obs span[33120, 34560] tonic9m II | Min |  |  root11
BND bwv10.7|-3 @34080 exp span[34080, 34560] tonic9m I | Min |  |  root9 | obs span[33120, 34560] tonic9m II | Min |  |  root11
BND bwv10.7|-3 @34560 exp span[34560, 35520] tonic9m V | Maj |  |  root4 | obs span[34560, 36480] tonic9m V | Dom7 |  |  root4
BND bwv10.7|-3 @35520 exp span[35520, 36000] tonic9m I | Min |  |  root9 | obs span[34560, 36480] tonic9m V | Dom7 |  |  root4
BND bwv10.7|-3 @36000 exp span[36000, 36480] tonic9m II | Min |  |  root11 | obs span[34560, 36480] tonic9m V | Dom7 |  |  root4
BND bwv10.7|-3 @36480 exp span[36480, 38400] tonic9m I | Min |  |  root9 | obs span[36480, 36960] tonic9m I | Min |  |  root9
BND bwv10.7|-3 @38400 exp span[38400, 39360] tonic9m I | Min |  |  root9 | obs span[36960, 39360] tonic9m I | Min |  |  root9
BND bwv10.7|+6 @2400 exp span[2400, 2880] tonic1m V | Maj |  |  root8 | obs span[2400, 2880] tonic4M V | Dom7 |  | vi root8
BND bwv10.7|+6 @2880 exp span[2880, 3360] tonic1m I | Min |  |  root1 | obs span[2880, 3360] tonic4M VI | Min |  |  root1
BND bwv10.7|+6 @3360 exp span[3360, 3840] tonic1m V | Maj |  |  root8 | obs span[3360, 3840] tonic4M V | Maj |  | vi root8
BND bwv10.7|+6 @12480 exp span[12480, 13440] tonic1m IV | Min |  |  root6 | obs span[12480, 13440] tonic4M II | Min |  |  root6
BND bwv10.7|+6 @13440 exp span[13440, 13920] tonic1m I | Min |  |  root1 | obs span[13440, 13920] tonic4M VI | Min |  |  root1
BND bwv10.7|+6 @13920 exp span[13920, 15360] tonic1m V | Dom7 |  |  root8 | obs span[13920, 15360] tonic4M V | Dom7 |  | vi root8
BND bwv10.7|+6 @15360 exp span[15360, 18240] tonic1m I | Min |  |  root1 | obs span[15360, 18240] tonic4M VI | Min |  |  root1
BND bwv10.7|+6 @28800 exp span[28800, 30720] tonic4M V | Maj |  |  root11 | obs span[28800, 30240] tonic4M V | Maj |  |  root11
BND bwv10.7|+6 @30720 exp span[30720, 32640] tonic1m II | Min |  |  root3 | obs span[30240, 32160] tonic4M V | Dom7 |  | v root6
BND bwv10.7|+6 @32640 exp span[32640, 33600] tonic1m I | Min |  |  root1 | obs span[32640, 33120] tonic4M VI | Min |  |  root1
BND bwv10.7|+6 @33600 exp span[33600, 34080] tonic1m V | Min |  |  root8 | obs span[33120, 34080] tonic6m II | Min |  |  root8
BND bwv153.1|+2 @3360 exp span[3360, 3840] tonic11m V | Maj |  |  root6 | obs span[3360, 4320] tonic11m V | Maj |  |  root6
BND bwv153.1|+2 @3840 exp span[3840, 4320] tonic11m VII | Dim |  |  root10 | obs span[3360, 4320] tonic11m V | Maj |  |  root6
BND bwv153.1|+2 @5280 exp span[5280, 5760] tonic11m VI | Maj |  |  root7 | obs span[5280, 6120] tonic11m IV | Min |  |  root4
BND bwv153.1|+2 @5760 exp span[5760, 6240] tonic11m II | Dim |  |  root1 | obs span[5280, 6120] tonic11m IV | Min |  |  root4
BND bwv153.1|+2 @6240 exp span[6240, 6960] tonic11m V | Maj |  |  root6 | obs span[6120, 6960] tonic11m V | Maj |  |  root6
BND bwv153.1|+2 @11760 exp span[11760, 12240] tonic11m VI | Maj |  |  root7 | obs span[11760, 12720] tonic11m I | Min |  |  root11
BND bwv153.1|+2 @12240 exp span[12240, 12960] tonic11m I | Min |  |  root11 | obs span[11760, 12720] tonic11m I | Min |  |  root11
BND bwv153.1|+2 @12960 exp span[12960, 13440] tonic11m V | Maj |  |  root6 | obs span[12720, 13440] tonic11m V | Maj |  |  root6
BND bwv153.1|+2 @13440 exp span[13440, 14400] tonic11m I | Min |  |  root11 | obs span[13440, 14160] tonic11m I | Min |  |  root11
BND bwv153.1|+2 @14400 exp span[14400, 14880] tonic11m V | Maj |  |  root6 | obs span[14160, 14880] tonic11m V | Maj |  |  root6
BND bwv153.1|-3 @0 exp span[0, 1920] tonic6m I | Min |  |  root6 | obs span[0, 960] tonic6m I | Min |  |  root6
BND bwv153.1|-3 @4320 exp span[4320, 5280] tonic6m I | Min |  |  root6 | obs span[4320, 4800] tonic6m I | Min |  |  root6
BND bwv153.1|-3 @6240 exp span[6240, 6960] tonic6m V | Maj |  |  root1 | obs span[6240, 7200] tonic6m V | Maj |  |  root1
BND bwv153.1|-3 @6960 exp span[6960, 7680] tonic6m I | Min |  |  root6 | obs span[6240, 7200] tonic6m V | Maj |  |  root1
BND bwv153.1|-3 @8400 exp span[8400, 8640] tonic1m VII | Dim |  |  root0 | obs span[8400, 8640] tonic4M VII | Dim |  | vi root0
BND bwv153.1|-3 @8640 exp span[8640, 9120] tonic1m I | Min |  |  root1 | obs span[8640, 9120] tonic4M VI | Min |  |  root1
BND bwv153.1|-3 @9120 exp span[9120, 9600] tonic1m V | Maj |  |  root8 | obs span[9120, 9600] tonic4M V | Maj |  | vi root8
BND bwv153.1|-3 @9600 exp span[9600, 10560] tonic1m I | Min |  |  root1 | obs span[9600, 10560] tonic4M VI | Min |  |  root1
BND bwv153.1|-3 @10560 exp span[10560, 11040] tonic1m II | Dim |  |  root3 | obs span[10560, 11040] tonic4M VII | Dim |  |  root3
BND bwv153.1|-3 @11040 exp span[11040, 11520] tonic1m V | Maj |  |  root8 | obs span[11040, 11520] tonic4M V | Maj |  | vi root8
BND bwv153.1|-3 @11520 exp span[11520, 11760] tonic1m I | Min |  |  root1 | obs span[11520, 12000] tonic4M VI | Min |  |  root1
BND bwv153.1|-3 @11760 exp span[11760, 12240] tonic6m VI | Maj |  |  root2 | obs span[11520, 12000] tonic4M VI | Min |  |  root1
BND bwv153.1|-3 @12240 exp span[12240, 12960] tonic6m I | Min |  |  root6 | obs span[12000, 12480] tonic6m VI | Maj |  |  root2
BND bwv153.1|-3 @14880 exp span[14880, 16560] tonic6m I | Min |  |  root6 | obs span[14880, 15840] tonic6m I | Min |  |  root6
BND bwv153.1|-3 @16560 exp span[16560, 17040] tonic11m I | Min |  |  root11 | obs span[16560, 17280] tonic11m I | Min |  |  root11
BND bwv153.1|-3 @17040 exp span[17040, 18000] tonic11m I | Maj |  |  root11 | obs span[16560, 17280] tonic11m I | Min |  |  root11
BND bwv153.1|-3 @18000 exp span[18000, 18720] tonic1M VII | Dim7 |  |  root0 | obs span[18000, 18720] tonic6m VII | Dim7 |  | V root0
BND bwv153.1|-3 @18720 exp span[18720, 19200] tonic1M I | Maj |  |  root1 | obs span[18720, 19200] tonic6m V | Maj |  |  root1
BND bwv153.1|+6 @0 exp span[0, 1920] tonic3m I | Min |  |  root3 | obs span[0, 960] tonic3m I | Min |  |  root3
BND bwv153.1|+6 @4320 exp span[4320, 5280] tonic3m I | Min |  |  root3 | obs span[4320, 4800] tonic3m I | Min |  |  root3
BND bwv153.1|+6 @6240 exp span[6240, 6960] tonic3m V | Maj |  |  root10 | obs span[6240, 7200] tonic3m V | Maj |  |  root10
BND bwv153.1|+6 @6960 exp span[6960, 7680] tonic3m I | Min |  |  root3 | obs span[6240, 7200] tonic3m V | Maj |  |  root10
BND bwv153.1|+6 @8400 exp span[8400, 8640] tonic10m VII | Dim |  |  root9 | obs span[8400, 9600] tonic10m I | Min |  |  root10
BND bwv153.1|+6 @8640 exp span[8640, 9120] tonic10m I | Min |  |  root10 | obs span[8400, 9600] tonic10m I | Min |  |  root10
BND bwv153.1|+6 @9120 exp span[9120, 9600] tonic10m V | Maj |  |  root5 | obs span[8400, 9600] tonic10m I | Min |  |  root10
BND bwv153.1|+6 @10560 exp span[10560, 11040] tonic10m II | Dim |  |  root0 | obs span[10560, 10800] tonic10m II | Dim |  |  root0
BND bwv153.1|+6 @11040 exp span[11040, 11520] tonic10m V | Maj |  |  root5 | obs span[10800, 11520] tonic10m V | Maj |  |  root5
BND bwv153.1|+6 @11520 exp span[11520, 11760] tonic10m I | Min |  |  root10 | obs span[11520, 12000] tonic3m V | Min |  |  root10
BND bwv153.1|+6 @11760 exp span[11760, 12240] tonic3m VI | Maj |  |  root11 | obs span[11520, 12000] tonic3m V | Min |  |  root10
BND bwv153.1|+6 @12240 exp span[12240, 12960] tonic3m I | Min |  |  root3 | obs span[12000, 12480] tonic3m VI | Maj |  |  root11
BND bwv153.1|+6 @14880 exp span[14880, 16560] tonic3m I | Min |  |  root3 | obs span[14880, 15840] tonic3m I | Min |  |  root3
BND bwv153.1|+6 @16560 exp span[16560, 17040] tonic8m I | Min |  |  root8 | obs span[16560, 17280] tonic8m I | Min |  |  root8
BND bwv153.1|+6 @17040 exp span[17040, 18000] tonic8m I | Maj |  |  root8 | obs span[16560, 17280] tonic8m I | Min |  |  root8
BND bwv153.1|+6 @18000 exp span[18000, 18720] tonic10M VII | Dim7 |  |  root9 | obs span[18000, 18720] tonic3m VII | Dim7 |  | V root9
BND bwv153.1|+6 @18720 exp span[18720, 19200] tonic10M I | Maj |  |  root10 | obs span[18720, 19200] tonic3m V | Maj |  |  root10
BND bwv2.6|+2 @0 exp span[0, 960] tonic9m I | Min |  |  root9 | obs span[0, 960] tonic4m IV | Min |  |  root9
BND bwv2.6|+2 @2880 exp span[2880, 3360] tonic9m I | Min |  |  root9 | obs span[2880, 3840] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @3360 exp span[3360, 3840] tonic9m V | Maj |  |  root4 | obs span[2880, 3840] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @6240 exp span[6240, 6720] tonic9m I | Min |  |  root9 | obs span[6240, 7680] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @6720 exp span[6720, 7200] tonic9m V | Maj |  |  root4 | obs span[6240, 7680] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @7200 exp span[7200, 8160] tonic9m I | Min |  |  root9 | obs span[6240, 7680] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @14880 exp span[14880, 15840] tonic9m I | Min |  |  root9 | obs span[14880, 16560] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @15840 exp span[15840, 16320] tonic9m V | Maj |  |  root4 | obs span[14880, 16560] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @16320 exp span[16320, 16800] tonic9m I | Min |  |  root9 | obs span[14880, 16560] tonic9m I | Min |  |  root9
BND bwv2.6|+2 @16800 exp span[16800, 17760] tonic2m I | Min |  |  root2 | obs span[16560, 17280] tonic2m I | Min |  |  root2
BND bwv2.6|-3 @8160 exp span[8160, 8640] tonic11m V | Maj |  |  root6 | obs span[8160, 9120] tonic11m I | Min |  |  root11
BND bwv2.6|-3 @8640 exp span[8640, 9120] tonic11m I | Min |  |  root11 | obs span[8160, 9120] tonic11m I | Min |  |  root11
BND bwv2.6|-3 @9600 exp span[9600, 10560] tonic11m I | Min |  |  root11 | obs span[9600, 10320] tonic11m I | Min |  |  root11
BND bwv2.6|-3 @10560 exp span[10560, 11040] tonic11m IV | Min |  |  root4 | obs span[10320, 11040] tonic2M II | Min |  |  root4
BND bwv2.6|-3 @11040 exp span[11040, 11520] tonic11m V | Maj |  |  root6 | obs span[11040, 11520] tonic2M V | Maj |  | vi root6
BND bwv2.6|-3 @11520 exp span[11520, 11760] tonic11m I | Min |  |  root11 | obs span[11520, 12000] tonic2M VI | Min |  |  root11
BND bwv2.6|-3 @11760 exp span[11760, 12480] tonic4m VI | Maj |  |  root0 | obs span[11520, 12000] tonic2M VI | Min |  |  root11
BND bwv2.6|-3 @12480 exp span[12480, 12960] tonic4m III | Maj |  |  root7 | obs span[12480, 12960] tonic2M IV | Maj |  |  root7
BND bwv2.6|-3 @12960 exp span[12960, 13440] tonic4m VII | Maj |  |  root2 | obs span[12960, 13200] tonic2M I | Maj |  |  root2
BND bwv2.6|-3 @13440 exp span[13440, 14400] tonic4m I | Min |  |  root4 | obs span[13200, 14160] tonic4m I | Min |  |  root4
BND bwv2.6|-3 @16320 exp span[16320, 16800] tonic4m I | Min |  |  root4 | obs span[16320, 16560] tonic4m I | Min |  |  root4
BND bwv2.6|-3 @16800 exp span[16800, 17760] tonic9m I | Min |  |  root9 | obs span[16560, 17280] tonic9m I | Min |  |  root9
BND bwv2.6|-3 @17760 exp span[17760, 18240] tonic9m I | Min |  |  root9 | obs span[17280, 18240] tonic9m I | Min |  |  root9
BND bwv2.6|-3 @18240 exp span[18240, 18720] tonic9m V | Min |  |  root4 | obs span[18240, 18720] tonic4m I | Min |  |  root4
BND bwv2.6|-3 @18720 exp span[18720, 19680] tonic11M V | Maj |  |  root6 | obs span[18720, 19680] tonic4m V | Maj |  | V root6
BND bwv2.6|-3 @19680 exp span[19680, 21120] tonic11M I | Maj |  |  root11 | obs span[19680, 21120] tonic4m V | Maj |  |  root11
BND bwv2.6|+6 @0 exp span[0, 960] tonic1m I | Min |  |  root1 | obs span[0, 960] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @960 exp span[960, 1440] tonic1m VII | Dim |  |  root0 | obs span[960, 1440] tonic11M VII | Dim |  | ii root0
BND bwv2.6|+6 @1440 exp span[1440, 2400] tonic1m I | Min |  |  root1 | obs span[1440, 2400] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @2400 exp span[2400, 2880] tonic1m V | Maj |  |  root8 | obs span[2400, 2880] tonic11M V | Maj |  | ii root8
BND bwv2.6|+6 @2880 exp span[2880, 3360] tonic1m I | Min |  |  root1 | obs span[2880, 3360] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @3360 exp span[3360, 3840] tonic1m V | Maj |  |  root8 | obs span[3360, 3840] tonic11M V | Maj |  | ii root8
BND bwv2.6|+6 @3840 exp span[3840, 4320] tonic6m VI | Maj |  |  root2 | obs span[3840, 4320] tonic11M II | Min |  | IV root6
BND bwv2.6|+6 @4320 exp span[4320, 5760] tonic1m VII | Dim7 |  | V root7 | obs span[4320, 4800] tonic11M VII | Dim |  | vi root7
BND bwv2.6|+6 @5760 exp span[5760, 6240] tonic1m V | Maj |  |  root8 | obs span[5760, 6240] tonic11M V | Maj |  | ii root8
BND bwv2.6|+6 @6240 exp span[6240, 6720] tonic1m I | Min |  |  root1 | obs span[6240, 6720] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @6720 exp span[6720, 7200] tonic1m V | Maj |  |  root8 | obs span[6720, 7200] tonic11M V | Maj |  | ii root8
BND bwv2.6|+6 @7200 exp span[7200, 8160] tonic1m I | Min |  |  root1 | obs span[7200, 7680] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @8160 exp span[8160, 8640] tonic8m V | Maj |  |  root3 | obs span[8160, 8640] tonic11M V | Maj |  | vi root3
BND bwv2.6|+6 @8640 exp span[8640, 9120] tonic8m I | Min |  |  root8 | obs span[8640, 9120] tonic11M VI | Min |  |  root8
BND bwv2.6|+6 @9120 exp span[9120, 9600] tonic8m V | Maj |  |  root3 | obs span[9120, 9600] tonic11M V | Maj |  | vi root3
BND bwv2.6|+6 @9600 exp span[9600, 10560] tonic8m I | Min |  |  root8 | obs span[9600, 10560] tonic11M VI | Min |  |  root8
BND bwv2.6|+6 @10560 exp span[10560, 11040] tonic8m IV | Min |  |  root1 | obs span[10560, 11040] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @11040 exp span[11040, 11520] tonic8m V | Maj |  |  root3 | obs span[11040, 11520] tonic11M V | Maj |  | vi root3
BND bwv2.6|+6 @11520 exp span[11520, 11760] tonic8m I | Min |  |  root8 | obs span[11520, 12000] tonic11M VI | Min |  |  root8
BND bwv2.6|+6 @11760 exp span[11760, 12480] tonic1m VI | Maj |  |  root9 | obs span[11520, 12000] tonic11M VI | Min |  |  root8
BND bwv2.6|+6 @12480 exp span[12480, 12960] tonic1m III | Maj |  |  root4 | obs span[12480, 12960] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @12960 exp span[12960, 13440] tonic1m VII | Maj |  |  root11 | obs span[12960, 13440] tonic11M VII | Dim |  | IV root3
BND bwv2.6|+6 @13440 exp span[13440, 14400] tonic1m I | Min |  |  root1 | obs span[13440, 14160] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @14400 exp span[14400, 14880] tonic1m V | Maj |  |  root8 | obs span[14400, 14880] tonic11M V | Maj |  | ii root8
BND bwv2.6|+6 @14880 exp span[14880, 15840] tonic1m I | Min |  |  root1 | obs span[14880, 15840] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @15840 exp span[15840, 16320] tonic1m V | Maj |  |  root8 | obs span[15840, 16320] tonic11M V | Maj |  | ii root8
BND bwv2.6|+6 @16320 exp span[16320, 16800] tonic1m I | Min |  |  root1 | obs span[16320, 16800] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @16800 exp span[16800, 17760] tonic6m I | Min |  |  root6 | obs span[16800, 17280] tonic11M II | Min |  | IV root6
BND bwv2.6|+6 @17760 exp span[17760, 18240] tonic6m I | Min |  |  root6 | obs span[17760, 18240] tonic11M II | Min |  | IV root6
BND bwv2.6|+6 @18240 exp span[18240, 18720] tonic6m V | Min |  |  root1 | obs span[18240, 18720] tonic11M VI | Min |  | IV root1
BND bwv2.6|+6 @18720 exp span[18720, 19680] tonic8M V | Maj |  |  root3 | obs span[18720, 19680] tonic11M V | Dom7 |  | VI root3
BND bwv2.6|+6 @19680 exp span[19680, 21120] tonic8M I | Maj |  |  root8 | obs span[19680, 21120] tonic11M V | Maj |  | ii root8
BND bwv245.37|+2 @480 exp span[480, 1440] tonic0m I | Min |  |  root0 | obs span[480, 960] tonic0m V | Maj |  |  root7
BND bwv245.37|+2 @2400 exp span[2400, 2640] tonic0m I | Min |  |  root0 | obs span[2400, 2880] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @2640 exp span[2640, 3840] tonic0m V | Maj |  |  root7 | obs span[2400, 2880] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @3840 exp span[3840, 4320] tonic5m V | Min |  |  root0 | obs span[3840, 4320] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @6240 exp span[6240, 7680] tonic0m V | Maj |  |  root7 | obs span[6240, 6720] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @7680 exp span[7680, 9120] tonic0m I | Min |  |  root0 | obs span[7680, 8160] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @12000 exp span[12000, 12480] tonic5m IV | Min |  |  root10 | obs span[12000, 12480] tonic1M VI | Min |  |  root10
BND bwv245.37|+2 @12480 exp span[12480, 13440] tonic10m VII | Dim7 |  |  root9 | obs span[12480, 13440] tonic1M VII | Dim7 |  | vi root9
BND bwv245.37|+2 @13440 exp span[13440, 13920] tonic10m I | Min |  |  root10 | obs span[13440, 13680] tonic1M VI | Min |  |  root10
BND bwv245.37|+2 @13920 exp span[13920, 15840] tonic0m I | Maj7 |  |  root0 | obs span[13680, 14400] tonic0m VI | Min |  |  root8
BND bwv245.37|+2 @16320 exp span[16320, 17520] tonic0m I | Min |  |  root0 | obs span[16320, 16800] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @21120 exp span[21120, 21600] tonic0m IV | Min |  |  root5 | obs span[21120, 22080] tonic0m IV | Min |  |  root5
BND bwv245.37|+2 @21600 exp span[21600, 23040] tonic0m V | Maj |  |  root7 | obs span[21120, 22080] tonic0m IV | Min |  |  root5
BND bwv245.37|+2 @23040 exp span[23040, 24480] tonic0m I | Min |  |  root0 | obs span[23040, 23520] tonic0m I | Min |  |  root0
BND bwv245.37|+2 @27360 exp span[27360, 27840] tonic5m V | Maj |  | III root3 | obs span[27360, 27840] tonic8M V | Maj |  |  root3
BND bwv245.37|+2 @27840 exp span[27840, 28800] tonic5m III | Maj |  |  root8 | obs span[27840, 28800] tonic8M I | Maj |  |  root8
BND bwv245.37|+2 @28800 exp span[28800, 29280] tonic5m VII | Maj |  |  root3 | obs span[28800, 29280] tonic8M V | Maj |  |  root3
BND bwv245.37|+2 @29760 exp span[29760, 32640] tonic0m V | Maj |  |  root7 | obs span[29760, 30720] tonic0m I | Min |  |  root0
BND bwv245.37|-3 @0 exp span[0, 480] tonic9m IV | Maj |  |  root2 | obs span[0, 960] tonic7m V | Maj |  |  root2
BND bwv245.37|-3 @480 exp span[480, 1440] tonic7m I | Min |  |  root7 | obs span[0, 960] tonic7m V | Maj |  |  root2
BND bwv245.37|-3 @2400 exp span[2400, 2640] tonic7m I | Min |  |  root7 | obs span[2400, 2880] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @2640 exp span[2640, 3840] tonic7m V | Maj |  |  root2 | obs span[2400, 2880] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @3840 exp span[3840, 4320] tonic0m V | Min |  |  root7 | obs span[3840, 4320] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @6240 exp span[6240, 7680] tonic7m V | Maj |  |  root2 | obs span[6240, 6720] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @7680 exp span[7680, 9120] tonic7m I | Min |  |  root7 | obs span[7680, 8160] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @12000 exp span[12000, 12480] tonic0m IV | Min |  |  root5 | obs span[12000, 12480] tonic5m I | Min |  |  root5
BND bwv245.37|-3 @13920 exp span[13920, 15840] tonic7m I | Maj7 |  |  root7 | obs span[13920, 15360] tonic7m I | Maj7 |  |  root7
BND bwv245.37|-3 @16320 exp span[16320, 17520] tonic7m I | Min |  |  root7 | obs span[16320, 16800] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @17520 exp span[17520, 18240] tonic10M I | Maj |  |  root10 | obs span[17280, 18240] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @18240 exp span[18240, 19200] tonic10M IV | Maj |  |  root3 | obs span[18240, 19200] tonic7m VI | Maj |  |  root3
BND bwv245.37|-3 @19200 exp span[19200, 19680] tonic10M I | Maj |  |  root10 | obs span[19200, 19680] tonic5M IV | Maj |  |  root10
BND bwv245.37|-3 @19680 exp span[19680, 20160] tonic10M V | Maj |  |  root5 | obs span[19680, 20160] tonic5M I | Maj |  |  root5
BND bwv245.37|-3 @20160 exp span[20160, 20640] tonic10M I | Maj |  |  root10 | obs span[20160, 20640] tonic5M IV | Maj |  |  root10
BND bwv245.37|-3 @20640 exp span[20640, 21120] tonic10M VI | Min |  |  root7 | obs span[20640, 21120] tonic5M II | Min |  |  root7
BND bwv245.37|-3 @21120 exp span[21120, 21600] tonic7m IV | Min |  |  root0 | obs span[21120, 22080] tonic7m IV | Min |  |  root0
BND bwv245.37|-3 @21600 exp span[21600, 23040] tonic7m V | Maj |  |  root2 | obs span[21120, 22080] tonic7m IV | Min |  |  root0
BND bwv245.37|-3 @23040 exp span[23040, 24480] tonic7m I | Min |  |  root7 | obs span[23040, 23520] tonic7m I | Min |  |  root7
BND bwv245.37|-3 @27360 exp span[27360, 27840] tonic0m V | Maj |  | III root10 | obs span[27360, 27840] tonic3M V | Maj |  |  root10
BND bwv245.37|-3 @27840 exp span[27840, 28800] tonic0m III | Maj |  |  root3 | obs span[27840, 28800] tonic3M I | Maj |  |  root3
BND bwv245.37|-3 @28800 exp span[28800, 29280] tonic0m VII | Maj |  |  root10 | obs span[28800, 29280] tonic3M V | Maj |  |  root10
BND bwv245.37|-3 @29760 exp span[29760, 32640] tonic7m V | Maj |  |  root2 | obs span[29760, 30720] tonic7m I | Min |  |  root7
BND bwv245.37|+6 @480 exp span[480, 1440] tonic4m I | Min |  |  root4 | obs span[480, 960] tonic4m V | Maj |  |  root11
BND bwv245.37|+6 @2400 exp span[2400, 2640] tonic4m I | Min |  |  root4 | obs span[2400, 2880] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @2640 exp span[2640, 3840] tonic4m V | Maj |  |  root11 | obs span[2400, 2880] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @3840 exp span[3840, 4320] tonic9m V | Min |  |  root4 | obs span[3840, 4320] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @4320 exp span[4320, 4800] tonic9m I | Min |  |  root9 | obs span[4320, 4800] tonic4m IV | Min |  |  root9
BND bwv245.37|+6 @4800 exp span[4800, 5760] tonic9m VII | Dim7 |  |  root8 | obs span[4800, 5760] tonic9m V | Maj |  |  root4
BND bwv245.37|+6 @5760 exp span[5760, 6240] tonic9m I | Min |  |  root9 | obs span[5760, 6240] tonic4m IV | Min |  |  root9
BND bwv245.37|+6 @6240 exp span[6240, 7680] tonic4m V | Maj |  |  root11 | obs span[6240, 6720] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @7680 exp span[7680, 9120] tonic4m I | Min |  |  root4 | obs span[7680, 8160] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @9120 exp span[9120, 9600] tonic9m III | Maj |  |  root0 | obs span[9120, 9600] tonic4m VI | Maj |  |  root0
BND bwv245.37|+6 @10080 exp span[10080, 10560] tonic9m I | Min |  |  root9 | obs span[10080, 12000] tonic9m I | Min |  |  root9
BND bwv245.37|+6 @10560 exp span[10560, 11520] tonic9m V | Maj |  |  root4 | obs span[10080, 12000] tonic9m I | Min |  |  root9
BND bwv245.37|+6 @11520 exp span[11520, 12000] tonic9m I | Min |  |  root9 | obs span[10080, 12000] tonic9m I | Min |  |  root9
BND bwv245.37|+6 @12000 exp span[12000, 12480] tonic9m IV | Min |  |  root2 | obs span[12000, 12480] tonic2m I | Min |  |  root2
BND bwv245.37|+6 @13920 exp span[13920, 15840] tonic4m I | Maj7 |  |  root4 | obs span[13920, 15360] tonic4m I | Maj7 |  |  root4
BND bwv245.37|+6 @16320 exp span[16320, 17520] tonic4m I | Min |  |  root4 | obs span[16320, 16800] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @21120 exp span[21120, 21600] tonic4m IV | Min |  |  root9 | obs span[21120, 22080] tonic4m IV | Min |  |  root9
BND bwv245.37|+6 @21600 exp span[21600, 23040] tonic4m V | Maj |  |  root11 | obs span[21120, 22080] tonic4m IV | Min |  |  root9
BND bwv245.37|+6 @23040 exp span[23040, 24480] tonic4m I | Min |  |  root4 | obs span[23040, 23520] tonic4m I | Min |  |  root4
BND bwv245.37|+6 @24480 exp span[24480, 24960] tonic9m III | Maj |  |  root0 | obs span[24480, 24960] tonic4m VI | Maj |  |  root0
BND bwv245.37|+6 @25440 exp span[25440, 25920] tonic9m I | Min |  |  root9 | obs span[25440, 27360] tonic9m I | Min |  |  root9
BND bwv245.37|+6 @25920 exp span[25920, 26880] tonic9m V | Maj |  |  root4 | obs span[25440, 27360] tonic9m I | Min |  |  root9
BND bwv245.37|+6 @26880 exp span[26880, 27360] tonic9m I | Min |  |  root9 | obs span[25440, 27360] tonic9m I | Min |  |  root9
BND bwv245.37|+6 @27360 exp span[27360, 27840] tonic9m V | Maj |  | III root7 | obs span[27360, 27840] tonic0M V | Maj |  |  root7
BND bwv245.37|+6 @27840 exp span[27840, 28800] tonic9m III | Maj |  |  root0 | obs span[27840, 28800] tonic0M I | Maj |  |  root0
BND bwv245.37|+6 @28800 exp span[28800, 29280] tonic9m VII | Maj |  |  root7 | obs span[28800, 29280] tonic0M V | Maj |  |  root7
BND bwv245.37|+6 @29280 exp span[29280, 29760] tonic9m I | Min |  |  root9 | obs span[29280, 29760] tonic0M VI | Min |  |  root9
BND bwv245.37|+6 @29760 exp span[29760, 32640] tonic4m V | Maj |  |  root11 | obs span[29760, 30720] tonic4m I | Min |  |  root4
BND bwv271|+2 @3840 exp span[3840, 4800] tonic1m V | Maj |  |  root8 | obs span[3840, 4320] tonic4M V | Maj |  | vi root8
BND bwv271|+2 @4800 exp span[4800, 5760] tonic1m I | Min |  |  root1 | obs span[4320, 5280] tonic4M VI | Min |  |  root1
BND bwv271|+2 @5760 exp span[5760, 6240] tonic1m V | Maj |  |  root8 | obs span[5280, 6240] tonic4M V | Maj |  | vi root8
BND bwv271|+2 @15840 exp span[15840, 16800] tonic11M I | Maj |  |  root11 | obs span[15840, 16560] tonic11M I | Maj |  |  root11
BND bwv271|+2 @16800 exp span[16800, 17040] tonic11M VI | Min |  | IV root1 | obs span[16560, 17040] tonic11M VI | Min |  | IV root1
BND bwv271|+2 @17760 exp span[17760, 18240] tonic11M II | Min7 |  |  root1 | obs span[17760, 18240] tonic11M VI | Min |  | IV root1
BND bwv271|+2 @18240 exp span[18240, 18720] tonic11M V | Maj |  |  root6 | obs span[18240, 19200] tonic11M I | Maj7 |  |  root11
BND bwv271|+2 @18720 exp span[18720, 19200] tonic4M V | Maj |  |  root11 | obs span[18240, 19200] tonic11M I | Maj7 |  |  root11
BND bwv271|+2 @19200 exp span[19200, 19680] tonic4M I | Maj |  |  root4 | obs span[19200, 19680] tonic4M V | Maj |  | IV root4
BND bwv271|+2 @21600 exp span[21600, 22320] tonic1m I | Min |  |  root1 | obs span[21600, 22560] tonic4M VI | Min |  |  root1
BND bwv271|+2 @22320 exp span[22320, 23040] tonic1m V | Maj |  |  root8 | obs span[21600, 22560] tonic4M VI | Min |  |  root1
BND bwv271|-3 @3840 exp span[3840, 4800] tonic8m V | Maj |  |  root3 | obs span[3840, 4320] tonic11M V | Maj |  | vi root3
BND bwv271|-3 @4800 exp span[4800, 5760] tonic8m I | Min |  |  root8 | obs span[4320, 5280] tonic11M VI | Min |  |  root8
BND bwv271|-3 @5760 exp span[5760, 6240] tonic8m V | Maj |  |  root3 | obs span[5280, 6240] tonic11M V | Maj |  | vi root3
BND bwv271|-3 @12480 exp span[12480, 12960] tonic1m IV | Min |  |  root6 | obs span[12480, 12960] tonic11M VII | Dim |  | IV root3
BND bwv271|-3 @12960 exp span[12960, 13920] tonic1m I | Min |  |  root1 | obs span[12960, 13920] tonic11M VI | Min |  | IV root1
BND bwv271|-3 @13920 exp span[13920, 15360] tonic1m V | Maj |  |  root8 | obs span[13920, 15360] tonic11M V | Maj |  | ii root8
BND bwv271|-3 @16800 exp span[16800, 17040] tonic6M VI | Min |  | IV root8 | obs span[16800, 17280] tonic6M VI | Min |  | IV root8
BND bwv271|-3 @17040 exp span[17040, 17760] tonic6M V | Maj |  | IV root6 | obs span[16800, 17280] tonic6M VI | Min |  | IV root8
BND bwv271|-3 @18720 exp span[18720, 19200] tonic11M V | Maj |  |  root6 | obs span[18720, 19200] tonic6M I | Maj |  |  root6
BND bwv271|-3 @19200 exp span[19200, 19680] tonic11M I | Maj |  |  root11 | obs span[19200, 19680] tonic11M V | Maj |  | IV root11
BND bwv271|-3 @21600 exp span[21600, 22320] tonic8m I | Min |  |  root8 | obs span[21600, 22560] tonic11M VI | Min |  |  root8
BND bwv271|-3 @22320 exp span[22320, 23040] tonic8m V | Maj |  |  root3 | obs span[21600, 22560] tonic11M VI | Min |  |  root8
BND bwv271|+6 @3840 exp span[3840, 4800] tonic5m V | Maj |  |  root0 | obs span[3840, 4320] tonic5m V | Maj |  |  root0
BND bwv271|+6 @4800 exp span[4800, 5760] tonic5m I | Min |  |  root5 | obs span[4320, 5280] tonic5m I | Min |  |  root5
BND bwv271|+6 @5760 exp span[5760, 6240] tonic5m V | Maj |  |  root0 | obs span[5280, 6240] tonic5m V | Maj |  |  root0
BND bwv271|+6 @6240 exp span[6240, 8160] tonic8M VI | Min |  |  root5 | obs span[6240, 7920] tonic5m I | Min |  |  root5
BND bwv271|+6 @8160 exp span[8160, 8640] tonic8M VII | Dim |  |  root7 | obs span[7920, 8640] tonic8M VII | Dim |  |  root7
BND bwv271|+6 @12960 exp span[12960, 13920] tonic10m I | Min |  |  root10 | obs span[12960, 13680] tonic10m I | Min |  |  root10
BND bwv271|+6 @13920 exp span[13920, 15360] tonic10m V | Maj |  |  root5 | obs span[13680, 15360] tonic10m V | Maj |  |  root5
BND bwv271|+6 @16800 exp span[16800, 17040] tonic3M VI | Min |  | IV root5 | obs span[16800, 17280] tonic3M VI | Min |  | IV root5
BND bwv271|+6 @17040 exp span[17040, 17760] tonic3M V | Maj |  | IV root3 | obs span[16800, 17280] tonic3M VI | Min |  | IV root5
BND bwv271|+6 @18720 exp span[18720, 19200] tonic8M V | Maj |  |  root3 | obs span[18720, 19200] tonic3M I | Maj |  |  root3
BND bwv271|+6 @19200 exp span[19200, 19680] tonic8M I | Maj |  |  root8 | obs span[19200, 19680] tonic8M V | Maj |  | IV root8
BND bwv271|+6 @21600 exp span[21600, 22320] tonic5m I | Min |  |  root5 | obs span[21600, 22560] tonic5m I | Min |  |  root5
BND bwv271|+6 @22320 exp span[22320, 23040] tonic5m V | Maj |  |  root0 | obs span[21600, 22560] tonic5m I | Min |  |  root5
BND bwv297|-3 @0 exp span[0, 960] tonic11m I | Min |  |  root11 | obs span[0, 960] tonic9M VI | Min |  | IV root11
BND bwv297|-3 @960 exp span[960, 1440] tonic11m IV | Min |  |  root4 | obs span[960, 1440] tonic9M VII | Dim |  | IV root1
BND bwv297|-3 @1440 exp span[1440, 2400] tonic11m I | Min |  |  root11 | obs span[1440, 2400] tonic9M VI | Min |  | IV root11
BND bwv297|-3 @2400 exp span[2400, 3360] tonic6m I | Min |  |  root6 | obs span[2400, 2880] tonic6m I | Min |  |  root6
BND bwv297|-3 @3360 exp span[3360, 4320] tonic6m VI | Maj |  |  root2 | obs span[3360, 4320] tonic6m I | Min |  |  root6
BND bwv297|-3 @5760 exp span[5760, 6240] tonic11m I | Min |  |  root11 | obs span[5760, 6480] tonic11m I | Min |  |  root11
BND bwv297|-3 @6240 exp span[6240, 6720] tonic11m IV | Min |  |  root4 | obs span[5760, 6480] tonic11m I | Min |  |  root11
BND bwv297|-3 @6720 exp span[6720, 7200] tonic11m VII | Dim7 |  | V root5 | obs span[6480, 7200] tonic11m VII | Dim7 |  | V root5
BND bwv297|-3 @12000 exp span[12000, 12480] tonic11m IV | Min |  |  root4 | obs span[12000, 12480] tonic2M VI | Min |  | IV root4
BND bwv297|-3 @12480 exp span[12480, 12960] tonic11m V | Maj |  |  root6 | obs span[12480, 12960] tonic2M V | Dom7 |  | vi root6
BND bwv297|-3 @12960 exp span[12960, 13920] tonic11m I | Min |  |  root11 | obs span[12960, 13920] tonic2M VI | Min |  |  root11
BND bwv297|-3 @20160 exp span[20160, 20640] tonic11M V | Maj |  |  root6 | obs span[20160, 20520] tonic11M V | Maj |  |  root6
BND bwv297|-3 @20640 exp span[20640, 21600] tonic11M I | Maj |  |  root11 | obs span[20520, 21600] tonic11M I | Maj |  |  root11
BND bwv297|+6 @0 exp span[0, 960] tonic8m I | Min |  |  root8 | obs span[0, 960] tonic6M VI | Min |  | IV root8
BND bwv297|+6 @960 exp span[960, 1440] tonic8m IV | Min |  |  root1 | obs span[960, 1440] tonic6M VII | Dim |  | IV root10
BND bwv297|+6 @1440 exp span[1440, 2400] tonic8m I | Min |  |  root8 | obs span[1440, 2400] tonic6M VI | Min |  | IV root8
BND bwv297|+6 @2400 exp span[2400, 3360] tonic3m I | Min |  |  root3 | obs span[2400, 2880] tonic6M VI | Min |  |  root3
BND bwv297|+6 @3360 exp span[3360, 4320] tonic3m VI | Maj |  |  root11 | obs span[3360, 4320] tonic6M IV | Maj |  |  root11
BND bwv297|+6 @4320 exp span[4320, 5040] tonic3m V | Maj |  |  root10 | obs span[4320, 5040] tonic6M V | Maj |  | vi root10
BND bwv297|+6 @5040 exp span[5040, 5760] tonic8m V | Maj |  |  root3 | obs span[5040, 5760] tonic6M V | Maj |  | ii root3
BND bwv297|+6 @5760 exp span[5760, 6240] tonic8m I | Min |  |  root8 | obs span[5760, 6240] tonic6M VI | Min |  | IV root8
BND bwv297|+6 @6240 exp span[6240, 6720] tonic8m IV | Min |  |  root1 | obs span[6240, 6720] tonic6M II | Min |  | IV root1
BND bwv297|+6 @6720 exp span[6720, 7200] tonic8m VII | Dim7 |  | V root2 | obs span[6720, 7200] tonic6M VII | Dim |  | vi root2
BND bwv297|+6 @7200 exp span[7200, 8160] tonic8m V | Maj |  |  root3 | obs span[7200, 8160] tonic6M VI | Maj |  |  root3
BND bwv297|+6 @8160 exp span[8160, 9120] tonic8m I | Min |  |  root8 | obs span[8160, 9120] tonic11M VI | Min |  |  root8
BND bwv297|+6 @9120 exp span[9120, 9360] tonic11M II | Min |  |  root1 | obs span[9120, 9360] tonic11M VI | Min |  | IV root1
BND bwv297|+6 @9360 exp span[9360, 9600] tonic11M V | Maj |  |  root6 | obs span[9360, 10080] tonic11M V | Maj |  | IV root11
BND bwv297|+6 @9600 exp span[9600, 10080] tonic11M I | Maj |  |  root11 | obs span[9360, 10080] tonic11M V | Maj |  | IV root11
BND bwv297|+6 @10080 exp span[10080, 10560] tonic11M IV | Maj |  |  root4 | obs span[10080, 10560] tonic11M II | Min7 |  |  root1
BND bwv297|+6 @11040 exp span[11040, 11520] tonic11M I | Maj |  |  root11 | obs span[11040, 12000] tonic11M IV | Maj |  |  root4
BND bwv297|+6 @11520 exp span[11520, 12000] tonic11M IV | Maj |  |  root4 | obs span[11040, 12000] tonic11M IV | Maj |  |  root4
BND bwv297|+6 @12000 exp span[12000, 12480] tonic8m IV | Min |  |  root1 | obs span[12000, 12960] tonic11M III | Dom7 |  |  root3
BND bwv297|+6 @12480 exp span[12480, 12960] tonic8m V | Maj |  |  root3 | obs span[12000, 12960] tonic11M III | Dom7 |  |  root3
BND bwv297|+6 @12960 exp span[12960, 13920] tonic8m I | Min |  |  root8 | obs span[12960, 14400] tonic11M VI | Min7 |  |  root8
BND bwv297|+6 @13920 exp span[13920, 14880] tonic11M V | Maj |  | IV root11 | obs span[12960, 14400] tonic11M VI | Min7 |  |  root8
BND bwv297|+6 @14880 exp span[14880, 15360] tonic11M III | Min7 |  |  root3 | obs span[14400, 15360] tonic11M VI | Min |  | V root3
BND bwv297|+6 @15360 exp span[15360, 15600] tonic11M IV | Maj |  |  root4 | obs span[15360, 16800] tonic11M II | Min7 |  | V root8
BND bwv297|+6 @15600 exp span[15600, 15840] tonic11M V | Maj |  |  root6 | obs span[15360, 16800] tonic11M II | Min7 |  | V root8
BND bwv297|+6 @15840 exp span[15840, 16320] tonic11M I | Maj |  |  root11 | obs span[15360, 16800] tonic11M II | Min7 |  | V root8
BND bwv297|+6 @16320 exp span[16320, 16800] tonic11M VI | Min |  |  root8 | obs span[15360, 16800] tonic11M II | Min7 |  | V root8
BND bwv297|+6 @16800 exp span[16800, 17280] tonic11M I | Maj |  |  root11 | obs span[16800, 18240] tonic11M I | Maj |  |  root11
BND bwv297|+6 @17280 exp span[17280, 17760] tonic11M IV | Maj |  |  root4 | obs span[16800, 18240] tonic11M I | Maj |  |  root11
BND bwv297|+6 @17760 exp span[17760, 18240] tonic11M I | Maj |  |  root11 | obs span[16800, 18240] tonic11M I | Maj |  |  root11
BND bwv297|+6 @18240 exp span[18240, 18720] tonic11M V | Maj |  |  root6 | obs span[18240, 19200] tonic11M V | Maj |  |  root6
BND bwv297|+6 @18720 exp span[18720, 19200] tonic11M I | Maj |  |  root11 | obs span[18240, 19200] tonic11M V | Maj |  |  root6
BND bwv297|+6 @20160 exp span[20160, 20640] tonic8M V | Maj |  |  root3 | obs span[20160, 20640] tonic6M V | Maj |  | ii root3
BND bwv297|+6 @20640 exp span[20640, 21600] tonic8M I | Maj |  |  root8 | obs span[20640, 21600] tonic6M V | Maj |  | V root8
BND bwv321|+6 @2880 exp span[2880, 3360] tonic11M V | Maj |  |  root6 | obs span[2880, 3360] tonic4M V | Maj |  | V root6
BND bwv321|+6 @3360 exp span[3360, 3840] tonic11M I | Maj |  |  root11 | obs span[3360, 3840] tonic4M V | Maj |  |  root11
BND bwv321|+6 @3840 exp span[3840, 4320] tonic11M VII | Dim |  |  root10 | obs span[3840, 4320] tonic4M VII | Dim |  | V root10
BND bwv321|+6 @4320 exp span[4320, 5760] tonic11M I | Maj |  |  root11 | obs span[4320, 5760] tonic4M V | Maj |  |  root11
BND bwv321|+6 @5760 exp span[5760, 6720] tonic11M IV | Maj |  |  root4 | obs span[5760, 6720] tonic4M I | Maj |  |  root4
BND bwv321|+6 @6720 exp span[6720, 7200] tonic11M II | Min |  |  root1 | obs span[6720, 6960] tonic4M VI | Min |  |  root1
BND bwv321|+6 @7200 exp span[7200, 7680] tonic11M V | Maj |  |  root6 | obs span[6960, 7680] tonic11M V | Maj |  |  root6
BND bwv321|+6 @10080 exp span[10080, 12000] tonic11M I | Maj |  |  root11 | obs span[10080, 12480] tonic11M I | Maj |  |  root11
BND bwv321|+6 @12000 exp span[12000, 12960] tonic11M V | Maj |  |  root6 | obs span[10080, 12480] tonic11M I | Maj |  |  root11
BND bwv321|+6 @12960 exp span[12960, 13440] tonic11M I | Maj |  |  root11 | obs span[12480, 13440] tonic11M I | Maj |  |  root11
BND bwv347|+2 @11520 exp span[11520, 12000] tonic1m VII | Dim |  |  root0 | obs span[11520, 12000] tonic11M VII | Dim |  | ii root0
BND bwv347|+2 @12000 exp span[12000, 12960] tonic1m I | Min |  |  root1 | obs span[12000, 12480] tonic11M VI | Min |  | IV root1
BND bwv347|+2 @12960 exp span[12960, 13440] tonic1m I | Min |  |  root1 | obs span[12960, 13200] tonic11M VI | Min |  | IV root1
BND bwv347|+2 @13440 exp span[13440, 13920] tonic1m V | Maj |  |  root8 | obs span[13440, 13920] tonic11M V | Maj |  | ii root8
BND bwv347|+2 @13920 exp span[13920, 15360] tonic11M II | Min |  |  root1 | obs span[13920, 15360] tonic11M VI | Min |  | IV root1
BND bwv347|+2 @15360 exp span[15360, 15840] tonic11M III | Min |  |  root3 | obs span[15360, 15840] tonic11M VI | Min |  | V root3
BND bwv347|-3 @1920 exp span[1920, 2400] tonic1m V | Maj |  |  root8 | obs span[1920, 2400] tonic6M V | Maj |  | V root8
BND bwv347|-3 @2400 exp span[2400, 2880] tonic1m I | Min |  |  root1 | obs span[2400, 2880] tonic6M II | Min |  | IV root1
BND bwv347|-3 @2880 exp span[2880, 3360] tonic1M V | Maj |  |  root8 | obs span[2880, 3360] tonic6M V | Dom7 |  | V root8
BND bwv347|-3 @3360 exp span[3360, 4320] tonic1M I | Maj |  |  root1 | obs span[3360, 4320] tonic6M V | Maj |  |  root1
BND bwv347|-3 @4320 exp span[4320, 4800] tonic1M IV | Maj |  |  root6 | obs span[4320, 4800] tonic6M I | Maj |  |  root6
BND bwv347|-3 @4800 exp span[4800, 5280] tonic1M III | Min |  |  root5 | obs span[4800, 5280] tonic6M V | Maj |  | V root8
BND bwv347|-3 @5280 exp span[5280, 5760] tonic1M IV | Maj |  |  root6 | obs span[5280, 5760] tonic6M I | Maj |  |  root6
BND bwv347|-3 @5760 exp span[5760, 6720] tonic1M I | Maj |  |  root1 | obs span[5760, 6720] tonic6M V | Maj |  |  root1
BND bwv347|-3 @6720 exp span[6720, 7200] tonic1M V | Maj |  |  root8 | obs span[6720, 7200] tonic6M V | Maj |  | V root8
BND bwv347|-3 @7200 exp span[7200, 7680] tonic1M I | Maj |  |  root1 | obs span[7200, 7680] tonic6M V | Maj |  |  root1
BND bwv347|-3 @7680 exp span[7680, 8160] tonic1M VI | Min |  |  root10 | obs span[7680, 8160] tonic6M VI | Min |  | V root10
BND bwv347|-3 @8160 exp span[8160, 9120] tonic6M VI | Min |  |  root3 | obs span[8160, 9120] tonic6M IV | Maj7 |  |  root11
BND bwv347|-3 @11520 exp span[11520, 12000] tonic8m VII | Dim |  |  root7 | obs span[11520, 12000] tonic6M VII | Dim |  | ii root7
BND bwv347|-3 @12000 exp span[12000, 12960] tonic8m I | Min |  |  root8 | obs span[12000, 12480] tonic6M VI | Min |  | IV root8
BND bwv347|-3 @12960 exp span[12960, 13440] tonic8m I | Min |  |  root8 | obs span[12960, 13200] tonic6M VI | Min |  | IV root8
BND bwv347|-3 @13440 exp span[13440, 13920] tonic8m V | Maj |  |  root3 | obs span[13440, 13920] tonic6M V | Maj |  | ii root3
BND bwv347|-3 @13920 exp span[13920, 15360] tonic6M II | Min |  |  root8 | obs span[13920, 15360] tonic6M VI | Min |  | IV root8
BND bwv347|-3 @15360 exp span[15360, 15840] tonic6M III | Min |  |  root10 | obs span[15360, 15840] tonic6M VI | Min |  | V root10
BND bwv347|+6 @1920 exp span[1920, 2400] tonic10m V | Maj |  |  root5 | obs span[1920, 2400] tonic3M V | Maj |  | V root5
BND bwv347|+6 @2400 exp span[2400, 2880] tonic10m I | Min |  |  root10 | obs span[2400, 2880] tonic3M II | Min |  | IV root10
BND bwv347|+6 @2880 exp span[2880, 3360] tonic10M V | Maj |  |  root5 | obs span[2880, 3360] tonic3M V | Dom7 |  | V root5
BND bwv347|+6 @3360 exp span[3360, 4320] tonic10M I | Maj |  |  root10 | obs span[3360, 4320] tonic3M V | Maj |  |  root10
BND bwv347|+6 @4320 exp span[4320, 4800] tonic10M IV | Maj |  |  root3 | obs span[4320, 4800] tonic3M I | Maj |  |  root3
BND bwv347|+6 @4800 exp span[4800, 5280] tonic10M III | Min |  |  root2 | obs span[4800, 5280] tonic3M V | Maj |  | V root5
BND bwv347|+6 @5280 exp span[5280, 5760] tonic10M IV | Maj |  |  root3 | obs span[5280, 5760] tonic3M I | Maj |  |  root3
BND bwv347|+6 @5760 exp span[5760, 6720] tonic10M I | Maj |  |  root10 | obs span[5760, 6720] tonic3M V | Maj |  |  root10
BND bwv347|+6 @6720 exp span[6720, 7200] tonic10M V | Maj |  |  root5 | obs span[6720, 7200] tonic3M V | Maj |  | V root5
BND bwv347|+6 @7200 exp span[7200, 7680] tonic10M I | Maj |  |  root10 | obs span[7200, 7680] tonic3M V | Maj |  |  root10
BND bwv347|+6 @7680 exp span[7680, 8160] tonic10M VI | Min |  |  root7 | obs span[7680, 8160] tonic3M VI | Min |  | V root7
BND bwv347|+6 @8160 exp span[8160, 9120] tonic3M VI | Min |  |  root0 | obs span[8160, 9120] tonic3M IV | Maj7 |  |  root8
BND bwv347|+6 @12000 exp span[12000, 12960] tonic5m I | Min |  |  root5 | obs span[12000, 12480] tonic5m I | Min |  |  root5
BND bwv347|+6 @13920 exp span[13920, 15360] tonic3M II | Min |  |  root5 | obs span[13920, 15360] tonic5m I | Min |  |  root5
LBL bwv373|-3 @10080 exp Bmaj I | Maj |  |  root11 | obs Emaj V | Maj |  |  root11 | exp_in_cands=False | expected-state factor deltas={}
LBL bwv373|-3 @10560 exp Bmaj VI | Min |  | IV root1 | obs Emaj VII | HalfDim7 |  | V root10 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv373|-3 @11040 exp Bmaj V | Maj |  | IV root11 | obs Emaj V | Maj |  |  root11 | exp_in_cands=False | expected-state factor deltas={}
LBL bwv373|-3 @11520 exp Bmaj II | Min7 |  |  root1 | obs Emaj I | Maj |  |  root4 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv373|-3 @12000 exp Bmaj V | Maj |  |  root6 | obs Emaj V | Maj |  | V root6 | exp_in_cands=False | expected-state factor deltas={}
LBL bwv373|-3 @12480 exp Bmaj I | Maj |  |  root11 | obs Emaj V | Maj |  |  root11 | exp_in_cands=False | expected-state factor deltas={}
BND bwv373|+6 @10080 exp span[10080, 10560] tonic8M I | Maj |  |  root8 | obs span[10080, 10560] tonic1M V | Maj |  |  root8
BND bwv373|+6 @10560 exp span[10560, 11040] tonic8M VI | Min |  | IV root10 | obs span[10560, 10800] tonic8M VI | Min |  | IV root10
BND bwv373|+6 @11040 exp span[11040, 11520] tonic8M V | Maj |  | IV root8 | obs span[10800, 11520] tonic8M V | Maj |  | IV root8
BND bwv373|+6 @12480 exp span[12480, 13440] tonic8M I | Maj |  |  root8 | obs span[12480, 13440] tonic1M V | Maj |  |  root8
BND bwv398|-3 @12480 exp span[12480, 12960] tonic11M V | Dom7 |  | V root1 | obs span[12480, 12960] tonic6M V | Maj |  |  root1
BND bwv398|-3 @12960 exp span[12960, 13440] tonic11M V | Maj |  |  root6 | obs span[12960, 13440] tonic6M I | Maj |  |  root6
BND bwv398|-3 @13440 exp span[13440, 13920] tonic11M I | Maj |  |  root11 | obs span[13440, 13920] tonic6M IV | Maj |  |  root11
BND bwv398|-3 @13920 exp span[13920, 14400] tonic11M V | Maj |  |  root6 | obs span[13920, 14400] tonic6M I | Maj |  |  root6
BND bwv398|-3 @14400 exp span[14400, 14880] tonic11M V | Maj |  | V root1 | obs span[14400, 14880] tonic6M V | Maj |  |  root1
BND bwv398|-3 @14880 exp span[14880, 15840] tonic11M V | Maj |  |  root6 | obs span[14880, 15840] tonic6M I | Maj |  |  root6
BND bwv398|-3 @15840 exp span[15840, 16800] tonic11M I | Maj |  |  root11 | obs span[15840, 16800] tonic11M V | Maj |  | IV root11
BND bwv398|-3 @16800 exp span[16800, 17280] tonic11M I | Maj |  |  root11 | obs span[16800, 17760] tonic11M V | Dom7 |  | IV root11
BND bwv398|-3 @17280 exp span[17280, 17760] tonic4M V | Maj |  |  root11 | obs span[16800, 17760] tonic11M V | Dom7 |  | IV root11
BND bwv398|-3 @17760 exp span[17760, 19680] tonic4M I | Maj |  |  root4 | obs span[17760, 19680] tonic11M IV | Maj |  |  root4
BND bwv398|-3 @19680 exp span[19680, 20640] tonic1m I | Min |  |  root1 | obs span[19680, 20640] tonic11M II | Min |  |  root1
BND bwv398|-3 @21600 exp span[21600, 22560] tonic11M V | Maj |  |  root6 | obs span[21600, 22560] tonic6M I | Maj |  |  root6
LBL bwv398|+6 @12480 exp Abmaj V | Dom7 |  | V root10 | obs Ebmaj V | Maj |  |  root10 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @12960 exp Abmaj V | Maj |  |  root3 | obs Ebmaj I | Maj |  |  root3 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @13440 exp Abmaj I | Maj |  |  root8 | obs Ebmaj IV | Maj |  |  root8 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @13920 exp Abmaj V | Maj |  |  root3 | obs Ebmaj I | Maj |  |  root3 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @14400 exp Abmaj V | Maj |  | V root10 | obs Ebmaj V | Maj |  |  root10 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @14880 exp Abmaj V | Maj |  |  root3 | obs Ebmaj I | Maj |  |  root3 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @21600 exp Abmaj V | Maj |  |  root3 | obs Ebmaj I | Maj |  |  root3 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @24480 exp Abmaj VI | Min |  |  root5 | obs Fmin I | Min |  |  root5 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @24960 exp Abmaj V | Maj |  | vi root0 | obs Fmin V | Maj |  |  root0 | exp_in_cands=True | expected-state factor deltas={}
LBL bwv398|+6 @25440 exp Abmaj VI | Min |  |  root5 | obs Fmin I | Min |  |  root5 | exp_in_cands=True | expected-state factor deltas={}
BND bwv420|+2 @9120 exp span[9120, 10080] tonic11m I | Min |  |  root11 | obs span[9120, 9840] tonic11m VII | HalfDim7 |  | VII root8
BND bwv420|+2 @10080 exp span[10080, 11520] tonic11m V | Maj |  |  root6 | obs span[9840, 11520] tonic11m V | Maj |  |  root6
BND bwv420|-3 @2880 exp span[2880, 3840] tonic6m I | Min |  |  root6 | obs span[2880, 3120] tonic6m I | Min |  |  root6
BND bwv420|-3 @6240 exp span[6240, 6720] tonic11m I | Min |  |  root11 | obs span[6240, 7680] tonic11m I | Min |  |  root11
BND bwv420|-3 @6720 exp span[6720, 7200] tonic11m V | Maj |  |  root6 | obs span[6240, 7680] tonic11m I | Min |  |  root11
BND bwv420|-3 @7200 exp span[7200, 7680] tonic11m I | Min |  |  root11 | obs span[6240, 7680] tonic11m I | Min |  |  root11
BND bwv420|-3 @7680 exp span[7680, 8160] tonic11m V | Min |  |  root6 | obs span[7680, 8160] tonic6m I | Min |  |  root6
BND bwv420|-3 @8640 exp span[8640, 9120] tonic6m I | Min |  |  root6 | obs span[8640, 8880] tonic6m I | Min |  |  root6
BND bwv420|-3 @15360 exp span[15360, 15840] tonic9M I | Maj |  |  root9 | obs span[15360, 15600] tonic9M I | Maj |  |  root9
BND bwv420|-3 @15840 exp span[15840, 16080] tonic6m IV | Min |  |  root11 | obs span[15600, 16320] tonic6m IV | Min |  |  root11
BND bwv420|-3 @16080 exp span[16080, 16800] tonic6m I | Min |  |  root6 | obs span[15600, 16320] tonic6m IV | Min |  |  root11
BND bwv420|-3 @18720 exp span[18720, 19200] tonic11m V | Maj |  |  root6 | obs span[18720, 19200] tonic6M I | Maj |  |  root6
BND bwv420|+6 @0 exp span[0, 1440] tonic3m I | Min |  |  root3 | obs span[0, 1440] tonic6M VI | Min |  |  root3
BND bwv420|+6 @1440 exp span[1440, 1920] tonic3m V | Maj |  |  root10 | obs span[1440, 1920] tonic6M V | Maj |  | vi root10
BND bwv420|+6 @1920 exp span[1920, 2400] tonic3m I | Min |  |  root3 | obs span[1920, 2400] tonic6M VI | Min |  |  root3
BND bwv420|+6 @2400 exp span[2400, 2880] tonic3m VII | Dim |  |  root2 | obs span[2400, 2880] tonic6M VII | Dim |  | vi root2
BND bwv420|+6 @2880 exp span[2880, 3840] tonic3m I | Min |  |  root3 | obs span[2880, 3120] tonic6M VI | Min |  |  root3
BND bwv420|+6 @3840 exp span[3840, 4800] tonic3m I | Min |  |  root3 | obs span[3840, 4800] tonic6M VI | Min |  |  root3
BND bwv420|+6 @4800 exp span[4800, 5280] tonic8m V | Maj |  |  root3 | obs span[4800, 5280] tonic6M V | Maj |  | ii root3
BND bwv420|+6 @5280 exp span[5280, 5760] tonic8m I | Min |  |  root8 | obs span[5280, 5760] tonic6M VI | Min |  | IV root8
BND bwv420|+6 @5760 exp span[5760, 6240] tonic8m VII | HalfDim7 |  | III root10 | obs span[5760, 6000] tonic6M VII | Dim |  | IV root10
BND bwv420|+6 @6240 exp span[6240, 6720] tonic8m I | Min |  |  root8 | obs span[6240, 6720] tonic6M VI | Min |  | IV root8
BND bwv420|+6 @6720 exp span[6720, 7200] tonic8m V | Maj |  |  root3 | obs span[6720, 7200] tonic6M V | Maj |  | ii root3
BND bwv420|+6 @7200 exp span[7200, 7680] tonic8m I | Min |  |  root8 | obs span[7200, 7680] tonic6M VI | Min |  | IV root8
BND bwv420|+6 @7680 exp span[7680, 8160] tonic8m V | Min |  |  root3 | obs span[7680, 8160] tonic6M VI | Min |  |  root3
BND bwv420|+6 @8160 exp span[8160, 8640] tonic3m V | Maj |  |  root10 | obs span[8160, 8640] tonic6M V | Maj |  | vi root10
BND bwv420|+6 @8640 exp span[8640, 9120] tonic3m I | Min |  |  root3 | obs span[8640, 8880] tonic6M VI | Min |  |  root3
BND bwv420|+6 @9120 exp span[9120, 10080] tonic3m I | Min |  |  root3 | obs span[9120, 10080] tonic6M VI | Min |  |  root3
BND bwv420|+6 @10080 exp span[10080, 11520] tonic3m V | Maj |  |  root10 | obs span[10080, 11520] tonic6M V | Maj |  | vi root10
BND bwv420|+6 @11520 exp span[11520, 12240] tonic3m I | Min |  |  root3 | obs span[11520, 12480] tonic6M VI | Min |  |  root3
BND bwv420|+6 @12240 exp span[12240, 12960] tonic6M IV | Maj |  |  root11 | obs span[11520, 12480] tonic6M VI | Min |  |  root3
BND bwv420|+6 @15360 exp span[15360, 15840] tonic6M I | Maj |  |  root6 | obs span[15360, 15840] tonic6M V | Maj |  | IV root6
BND bwv420|+6 @15840 exp span[15840, 16080] tonic3m IV | Min |  |  root8 | obs span[15840, 16080] tonic6M VI | Min |  | IV root8
BND bwv420|+6 @16080 exp span[16080, 16800] tonic3m I | Min |  |  root3 | obs span[16080, 16320] tonic6M V | Dom7 |  | vi root10
BND bwv420|+6 @16800 exp span[16800, 17280] tonic3m VII | Dim7 |  | iii root5 | obs span[16800, 17280] tonic6M VII | Dim |  | vi root2
BND bwv420|+6 @17280 exp span[17280, 17760] tonic3m VI | Maj |  |  root11 | obs span[17280, 17760] tonic6M VI | Min |  | IV root8
BND bwv420|+6 @17760 exp span[17760, 18240] tonic3m I | Min |  |  root3 | obs span[17760, 18240] tonic6M VII | HalfDim7 |  | V root0
BND bwv420|+6 @18240 exp span[18240, 18720] tonic3m VII | Dim |  |  root2 | obs span[18240, 18720] tonic6M VII | Dim |  | vi root2
BND bwv420|+6 @18720 exp span[18720, 19200] tonic8m V | Maj |  |  root3 | obs span[18720, 19200] tonic6M VI | Maj |  |  root3
LBL bwv55.5|-3 @10560 exp Amin I | Min |  |  root9 | obs Cmaj VI | Min |  |  root9 | exp_in_cands=False | expected-state factor deltas={}
BND bwv55.5|+6 @14400 exp span[14400, 15360] tonic9M I | Maj |  |  root9 | obs span[14400, 16320] tonic9M I | Maj |  |  root9
BND bwv55.5|+6 @15360 exp span[15360, 15840] tonic9M III | Min |  |  root1 | obs span[14400, 16320] tonic9M I | Maj |  |  root9
BND bwv55.5|+6 @15840 exp span[15840, 16320] tonic9M I | Maj |  |  root9 | obs span[14400, 16320] tonic9M I | Maj |  |  root9
```

Violations: 396 boundary-affected (BND) + 17 label-only (LBL) = 413. Full machine-readable detail (per-violation candidate checks, content scores, factor vectors, per-condition boundary diffs) is in `transpose_state.json` beside this report.

### Verdicts

- **P1 — PASS.** 12/12 untransposed pieces reproduce `decode_parity_ref.json` (segments AND
  total_score, tolerance 1e-6; header cross-check ok on all 12). `establish_state.json`.
- **P2 — FAIL, decisively.** 811/1224 segments matched (66.26 %) against the predicted >= 99 %.
  Only 6/36 piece-conditions are equivariant, and segment boundaries moved in 27/36 conditions —
  the "identical boundaries" clause of the prediction is itself false, not just the label clause.
  Per shift: +2 = 83.3 %, -3 = 65.2 %, +6 = 50.2 %.
- **P3 — PARTIAL.** Direction confirmed: +6 (the tritone) is the worst case (50.2 %, and the
  three near-total collapses bwv2.6|+6 0/32, bwv297|+6 2/36, bwv420|+6 4/31 are all +6), and the
  driving mechanism IS spelling-sensitive cells — the signature prior is exonerated by code
  inspection (below). Falsified parts: +2/-3 are far from near-perfect, violations are NOT
  confined to segments whose committed tonic crosses a spelling wrap (conditions with an empty
  committed-tonic wrap set still lose 20-55 % of segments through competitor keys and boundary
  movement), and boundary placement is not preserved.

### Diagnosis — which factor moved, per violation class

**Exonerated: the signature prior.** `probe_decoder.py:406-412` scores
`_fold_fifths_diff(_collection_fifths(tonic, mode) - sig_fifths)`; under transposition both terms
shift by the same amount mod 12 and the fold maps the difference back to the identical residue in
(-6, 6], so the prior is exactly transposition-invariant. The six exact conditions (total-score
delta 0.0, every segment matched: bwv297|+2, bwv321|+2, bwv321|-3, bwv373|+2, bwv398|+2,
bwv55.5|+2) are the existence proof that when no spelling anchor wraps, the whole decode is
bit-exactly equivariant.

**Class 1 — spelling-table cell, via the canonical key-anchor wrap (the dominant class; all 396
BND violations and the catastrophic conditions).** The spelling factor anchors each key at its
CANONICAL line-of-fifths position, not at the piece's notated spelling frame:
`probe_decoder.py:743` `key_lof = glt._PC_TO_FIFTHS[tonic % 12]`, and
`gen_note_tables.py:218-233` bins `rel = note_lof - key_lof` into seven diatonic degrees
(major -1..5, minor -4..2 plus raised6/raised7) with everything outside pooled into
`chr_flat`/`chr_sharp`. The probe transposes note lofs uniformly by `delta_lof` (the engraver
respell), but `_PC_TO_FIFTHS[(tonic+k) % 12]` moves by `delta_lof +/- 12` for every tonic pc in
the anchor-wrap set (the last column of the results table — 1-2 pcs of 12 for +2/-3, 5-7 pcs for
+6). For a wrapped key every diatonic note rebins as pooled chromatic (or, in the favorable
direction, a competitor's chromatic notes rebin as diatonic), so that key's content score
collapses or spuriously rises. Because content scores drive the semi-Markov segmentation, the
damage moves BOUNDARIES, not just labels — which is why 27/36 conditions lost boundary identity
and why per-segment factor comparison was only possible for the 17 LBL cases. Evidence at the
condition level: the three collapses all have their committed tonics inside the wrap set
(total-score delta -12.97 to -15.81), while bwv245.37 (committed tonics unwrapped, all three
shifts) shows POSITIVE total-score deltas (+4.93 to +7.11) — the transposed decode finds a
strictly better-scoring path through competitor keys whose anchors wrapped favorably. Both signs
are the same defect.

**Class 2 — candidate-set tie-break (5 of the 17 LBL violations: bwv373|-3 @10080, @11040,
@12000, @12480; bwv55.5|-3 @10560).** The KEY-FIT prune `probe_decoder.py:1039-1052` ranks the
24 keys by `(-|onset_pcs & collection|, tonic_pc, major-before-minor)` and keeps the top
KEY_PRUNE_TOPK. The fit term is transposition-covariant, but the tie-break ranks by ABSOLUTE
tonic pitch class, which permutes under transposition — so at equal fit the keep/drop decision
at the top-K boundary differs between the original and transposed piece, and the expected
(shifted) state is not even in the transposed candidate set.

**Class 3 — competitor movement / decode-context propagation (the remaining 12 LBL
violations).** In every one of the 17 LBL cases the expected state's own factor vector is
byte-identical to the original committed state's (all per-factor deltas 0.000000) — the expected
reading did not get worse; something else got better. The observed winners sit at fifth- or
third-related tonics (observed-minus-expected tonic deltas: +7 in 7 cases, +5 in 6, +9 in 3,
+3 in 1), i.e. dominant/subdominant/relative neighbors whose own spelling cells wrapped
favorably (class 1 acting on the competitor) or which are reached through a `key_trans` chain
from an adjacent segment that had already flipped. These are score-driven flips, not exact-tie
flips: the observed content score differs from the expected one (both recorded per violation in
`transpose_state.json`), so the ratified section-5 exact-tie total order is NOT implicated.

### What this measurement establishes

The production reference decode is transposition-equivariant EXCEPT through exactly one feature
family: line-of-fifths spelling handled via a canonical per-tonic anchor plus binning
(`_PC_TO_FIFTHS` + `spelling_bin`), and one pruning detail: the absolute-tonic-pc tie-break in
the key-fit prune. The signature prior, the pc-based candidate filters, and the transition
factors showed no violation of their own (six bit-exact conditions; zero factor deltas on every
comparable expected state). This is a read-only fact-finding result (the surprise is the product
of the stage, not a STOP violation): the >= 99 % equivariance premise, if any design were to
carry load on it, is FALSE as stated and would need the spelling-anchor wrap behavior treated as
a first-class term.

### Artifacts

- `report.md` (this file; predictions registered before any transposed decode ran)
- `establish_state.json` — P1 raw results (12/12, per-piece scores and timings)
- `transpose_state.json` — the raw comparison JSON: all 36 conditions, every violation with
  expected/observed state, candidate-set check, content scores, per-factor deltas, boundary
  diffs, committed-tonic wrap flags
- `run_probe.py` — the measurement script (reads the repository read-only; decodes via the
  repository's own `tools/joint_estimator/probe_decoder.py` at the production configuration)

