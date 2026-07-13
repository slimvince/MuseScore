# Outgoing calibration maps — before the OI-144 refit on the corrected ground truth (2026-07-13)

**Why this exists (O-12 / guiding principle #16).** The combined re-baseline event of 2026-07-13
refits the four committed calibration maps on the OI-142-corrected When-in-Rome ground truth
(register row OI-144, discovery D3: the committed maps were fit through the RAW
`parse_rntxt_file`, so the 12 transposed editions were graded against the wrong pitch level).
The refit moves all four maps, so the **outgoing** maps are snapshotted here byte-for-byte before
anything changed.

**What this is.** An exact copy of the four committed `tools/calibration_maps/*.json` as fit at
Stage-5 Phase 3 and carried unchanged through the OI-142/OI-143 re-baseline.

| file | sha256 |
|---|---|
| `stage5_classP_l3_key_margin_baroque.json` | `09e3ebedf282afcda5a95c33705fafb56285f08c7636e99337f5e20dbf0313e3` |
| `stage5_classP_l3_key_margin_default.json` | `90c80ab970bc27b1a940e4ff24ff6caa7b81c72138b78b56a125eac546ccabab` |
| `stage5_classP_l4_chord_composite_baroque.json` | `90f50b896c2f88d7a0790fd5178e7ed411b670dbf958b99edbb85e99245fffd4` |
| `stage5_classP_l4_chord_composite_default.json` | `6c5f440b6249d4df84de6ca1c25b21db060eaafbbed797de4fb3046c93680d95` |

**Provenance of this snapshot.**

- Snapshotted at repo HEAD `0bc49b4b48` (the register commit for this event), before any
  instrument change.
- Corpus `c50002fee1`; the maps' fitting substrate is the committed per-preset corpus plus the
  When-in-Rome ground truth read through `dcml_parser`.
- Superseded by: the OI-144 refit (report `cc_key_grading_and_calibration_rebaseline_report.md`).

**Who reads these maps.** Two measurement instruments only — `tools/conformal_check.py` and
`tools/theta_fit.py`. No C++ code and no analysis-time path reads them (verified repo-wide at this
event: `tools/batch_analyze.cpp` reads the score and its command-line parameters and nothing else).
They are a measurement artifact, not a production input.

**Companion snapshot:** `tools/robust_stop/snapshot_2026-07-13_pre_oi132_oi144/` holds the outgoing
regression-stop reference for the same event.
