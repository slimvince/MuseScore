# Outgoing reference snapshot — the O-12 copy taken at the OI-178 adoption MEASUREMENT (2026-07-26)

**Why this exists (O-12 / guiding principle #16; OI-178 sequence step (c)).** The joint
estimator ("A") adoption protocol (`cowork_prefit_gates.md`, OI-178) requires the outgoing
`tools/robust_stop/` reference to be snapshotted **before** A's first full-corpus measured decode,
so the superseded reference is explicitly preserved rather than merely git-recoverable, whichever
way the eventual adoption ruling goes.

**★ NO RE-BASELINE OCCURS IN THIS EVENT.** The dispatch `cc_instruction_adoption_measurement.md`
is **MEASUREMENT ONLY** — it produces the adoption RECORD for the user's ratification and performs
no adoption act. The committed `tools/robust_stop/` reference is **unchanged** by this event; this
snapshot is a byte-for-byte copy of it, taken now as the protocol's pre-declared O-12 step. If the
user later ratifies A's adoption, that separate commit re-baselines the reference and this snapshot
is its outgoing-reference preservation; if A is not adopted, this snapshot is a no-op copy that
records the reference state at the measurement.

**What this is.** An exact copy of the committed `tools/robust_stop/` reference as it stood after
the OI-168 signature-mask correctness re-baseline (2026-07-14) — the diff base that governs the
hard regression stop at the time of the adoption measurement.

- `summary.json`, `manifest.json` — the a8 aggregates + provenance.
- `{preset}_variant_{a,b}_root_fail_runs.txt` — the run enumerations (the diff base:
  6506 / 6688 / 6522 variant-(b) root-failing runs, Baroque / Jazz / Default).
- `{preset}_mapping.json` — the batch→robust old→new mapping.
- `README.md`, `batch_stop_frozen_history.json`, `corpus_transposition_offsets.json` — the
  reference's own docs and data, copied verbatim.

**The ratified figures this snapshot preserves** (variant b, root-agree at 326/352 coverage;
Baroque / Jazz / Default — CLAUDE.md block (A), the OI-168 re-baseline):

| column | figure |
|---|---|
| root-agree | 66.04 / 64.98 / 65.93 % |
| RN-agree | 46.33 / 44.10 / 46.23 % |
| key-agree vs HOME (global) | 71.42 / 67.83 / 70.65 % |
| key-agree vs LOCAL | 65.99 / 62.98 / 65.71 % |
| class-(b) root-disagree duration (the hard stop) | 2 714 000 / 2 783 680 / 2 718 080 ticks |
| variant-(b) root-failing runs | 6506 / 6688 / 6522 |

**Provenance of this snapshot.**

- Snapshotted at repo HEAD `020baca347` (the Task-C end-to-end decode-parity commit), before the
  adoption measurement's artifacts were written. No instrument, source, golden, or reference file
  was modified.
- Copied files are byte-identical to the parent `tools/robust_stop/` reference (verified by `diff`
  at snapshot time).
- The measurement that this snapshot accompanies: the adoption record
  `tools/joint_estimator/adoption_record.json` + `adoption_record_summary.txt` (report
  `cc_adoption_measurement_report.md`).
