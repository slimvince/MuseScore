# Outgoing reference snapshot — before the OI-168 signature-mask correctness re-baseline (2026-07-14)

**Why this exists (O-12 / guiding principle #16).** The OI-168 fix changes committed chord output on
the Jazz preset, so it re-baselines the `tools/robust_stop/` reference. Before any instrument or
source file changed, the **outgoing** reference was snapshotted here, byte-for-byte, so the
superseded reference is explicitly preserved and not merely git-recoverable.

**What this is.** An exact copy of the committed `tools/robust_stop/` reference as it stood after
the OI-132/OI-144 mode-grading + calibration re-baseline — the diff base that governed the hard
regression stop from 2026-07-13 until this event.

- `summary.json`, `manifest.json` — the a8 aggregates + provenance.
- `{preset}_variant_{a,b}_root_fail_runs.txt` — the run enumerations (the diff base:
  6506 / 6689 / 6522 variant-(b) root-failing runs, Baroque / Jazz / Default).
- `{preset}_mapping.json` — the batch→robust old→new mapping.
- `README.md`, `batch_stop_frozen_history.json`, `corpus_transposition_offsets.json` — the
  reference's own docs and data, copied verbatim.

**The ratified figures this snapshot preserves** (variant b, root-agree at 326/352 coverage;
Baroque / Jazz / Default):

| column | figure |
|---|---|
| root-agree | 66.04 / 64.98 / 65.93 % |
| RN-agree | 46.33 / 44.10 / 46.23 % |
| key-agree vs HOME (global) | 71.42 / 67.83 / 70.65 % |
| key-agree vs LOCAL | 65.99 / 62.98 / 65.71 % |
| class-(b) root-disagree duration (the hard stop) | 2 714 000 / 2 784 160 / 2 718 080 ticks |
| variant-(b) root-failing runs | 6506 / 6689 / 6522 |

**Provenance of this snapshot.**

- Snapshotted at repo HEAD `bf6388d43a` (the OI-168 magnitude-measurement commit), before any
  source edit of the fix.
- Corpus: `tools/corpus/{baroque,jazz,default}`, verified at-HEAD-reproducible on all three presets
  (`cc_oi168_magnitude_report.md` §3, arm 1).
- Superseded by: the OI-168 signature-mask fix (report `cc_oi168_fix_report.md`).

**What changes at the re-baseline.** `analyzeChord`'s two key-consuming scoring terms
(`dim7CharacteristicBonus`, `diatonicRootContribution`) stop testing membership in the
mode-tonic-anchored set `{ (keyTonicPc + scale[i]) mod 12 }` and test the key signature's own
diatonic collection instead (`pcInMask(diatonicMaskFromFifths(fifths), pc)`). The two sets are
provably identical for the 19 `KeySigMode` values whose tonic offset equals their diatonic parent's,
and differ (by a semitone transposition) for `Altered` and `AlteredDomBB7`.

Measured effect (`cc_oi168_magnitude_report.md`, confirmed at the fix):

- **Baroque and Default: byte-identical** — 352/352 `.ours.json` unchanged, run sets unchanged,
  class-(b) duration unchanged (+0).
- **Jazz: 9 files change; exactly ONE committed chord flips** — `bwv145.5@12960` (local key `D#alt`):
  `Ebm` (root pc 3) → `B/Eb` (root pc 11), which is the DCML ground-truth root and the music21 root.
- **Run-level set-diff: removal-only, one run.** Class-(b) root-disagree duration Jazz
  −480 ticks (2 784 160 → 2 783 680); Baroque/Default +0. Zero additions on any preset.
  `robust_stop_diff.py` verdict: **OVERALL PASS** (a strict improvement).
