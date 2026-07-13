# Outgoing reference snapshot — before the mode-grading + calibration-refit re-baseline (2026-07-13)

**Why this exists (O-12 / guiding principle #16).** The combined re-baseline event of 2026-07-13
(register rows OI-132 — the user's parent-collection ruling on the dominant-family modes — and
OI-144 — the calibration maps refit on the OI-142-corrected ground truth) moves recorded figures.
Before any instrument changed, the **outgoing** reference was snapshotted here, byte-for-byte, so
the superseded reference is explicitly preserved and not merely git-recoverable.

**What this is.** An exact copy of the committed `tools/robust_stop/` reference as it stood after
the OI-142/OI-143 key-grading re-baseline — the diff base that governed the hard regression stop
from 2026-07-12 until this event.

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
| key-agree vs HOME (global) | 71.29 / 67.49 / 70.52 % |
| key-agree vs LOCAL | 65.72 / 62.49 / 65.39 % |
| class-(b) root-disagree duration (the hard stop) | 2 714 000 / 2 784 160 / 2 718 080 ticks |

**Provenance of this snapshot.**

- Snapshotted at repo HEAD `0bc49b4b48` (the register commit for this event), before any
  instrument change.
- Corpus `c50002fee1` (unchanged by this event — no score and no ground-truth file is edited;
  no `src/` code is edited).
- Superseded by: the OI-132/OI-144 re-baseline (report
  `cc_key_grading_and_calibration_rebaseline_report.md`; adoption commits recorded there and in
  the CLAUDE.md gate block (A)).

**What changes at the re-baseline.** (A) The key grading reduces the five dominant-family exotic
modes (Phrygian dominant, altered, Lydian dominant, Lydian augmented, Mixolydian flat-six) to the
minor key of their parent collection, in the one shared parsing substrate; the second key-parser
path folds onto it. This moves the key-agreement columns only — the root columns and the
root-failing run sets are untouched. (B) The four calibration maps are refit on the
OI-142-corrected ground truth.

**Companion snapshot:** `tools/calibration_maps/snapshot_2026-07-13_pre_oi132_oi144/` holds the
outgoing calibration maps for the same event.
