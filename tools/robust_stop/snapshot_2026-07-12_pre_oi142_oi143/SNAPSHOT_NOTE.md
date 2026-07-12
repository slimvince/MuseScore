# Outgoing reference snapshot — R10-b robust-unit stop, before the OI-142/OI-143 re-baseline

**Why this exists (O-12 / guiding principle #16).** The key-grading re-baseline event of
2026-07-12 (register rows OI-142 arithmetic corpus-transposition correction + OI-143 dual
home/local key columns) re-baselines the `tools/robust_stop/` reference artifacts. Before any
instrument changed, the **outgoing** R10-b reference was snapshotted here, byte-for-byte, so the
superseded reference is explicitly preserved (not only git-recoverable).

**What this is.** An exact copy of the committed `tools/robust_stop/` reference as it stood at the
end of the R10-b state — the diff base that governed the hard regression stop from R10-b
(2026-07-06) until this re-baseline.

- `summary.json`, `manifest.json` — the a8 aggregates + provenance (root/RN/key baselines
  63.36/62.37/63.25 root, 44.58/42.40/44.41 RN, 68.13/64.43/67.50 key vs the DCML **global** key).
- `{preset}_variant_{a,b}_root_fail_runs.txt` — the run enumerations (the diff base: ≈6868/7036/6883
  variant-(b) runs Baroque/Jazz/Default).
- `{preset}_mapping.json` — the batch→robust old→new mapping.
- `README.md`, `batch_stop_frozen_history.json` — the reference's own docs, copied verbatim.

**Provenance of this snapshot.**

- Snapshotted at repo HEAD `ebd37dfc7b` (the register commit for OI-142/OI-143), before any
  instrument or reference change.
- Corpus `c50002fee1` (unchanged by this event — no score and no ground-truth file is edited).
- Superseded by: the OI-142/OI-143 re-baseline (report `cc_key_grading_rebaseline_report.md`;
  adoption commit recorded there and in CLAUDE.md gate block (A)).

**What changed at the re-baseline.** The grading now applies each of 12 transposed pieces'
constant root offset to the When-in-Rome ground truth at the shared loading substrate
(`dcml_parser.load_wir_regions`), so those editions grade against what our score actually contains;
and the key-agreement column becomes two columns (vs the DCML global/home key as before, and vs the
DCML local key). No score file, no ground-truth file, and no `src/` code was edited.
