# Outgoing evidence snapshot — before the OI-159 refresh of the OI-43 joint probe (2026-07-13)

**Why this exists (O-12 / guiding principle #16).** The OI-159 refresh re-runs
`tools/measure_joint_probe.py` at HEAD and overwrites the committed OI-43/OI-44 evidence
`tools/reports/mode_key_chord_probe.json`. Before that write, the **outgoing** artifact is
snapshotted here byte-for-byte, so the superseded evidence is explicitly preserved and not merely
git-recoverable.

**What this is.** An exact copy of `tools/reports/mode_key_chord_probe.json` as it stood when the
OI-43/OI-44 shelve ruling was taken — the run stamped `git 243cfd2165`, corpus `c50002fee1`, which
**pre-dates the OI-142 transposition correction** to `dcml_parser.load_wir_regions` and the OI-157
mode-classification fold.

**The figures this snapshot preserves** (Baroque / Jazz / Default):

| figure | snapshotted value |
|---|---|
| key-disagree regions | 1982 / 2143 / 2019 |
| menu-containment (PREDICTION 3) | 1322 / 1320 / 1295 = 66.7 / 61.6 / 64.1 % |
| chord-flip-under-GT (PREDICTION 1's mechanism) | 7 / 8 / 6 regions (coupled 3 / 4 / 2) |

**Why it was superseded, and what did NOT change.** The ground truth these figures are graded
against was corrected after the run (OI-142 applied the 12 transposed editions' offsets to the WiR
ground truth; the OI-157 fold then routed the probe's carried-key grading through the one shared
mode reduction). The refreshed run at HEAD moves the **key-axis** figures — key-disagree
−207 / −207 / −199, menu-containment up to 75.6 / 68.7 / 72.5 % — but **chord-flip-under-GT is
byte-identical at 7 / 8 / 6** (coupled 3 / 4 / 2, same durations). The OI-43/OI-44 shelve ruling
rests on that number and on menu-containment clearing an 80 % bar: the coupling is still inert and
containment is still below the bar, so **the ruling is re-confirmed, not reopened** — only the
recorded figures were stale.

**Provenance of this snapshot.**

- Snapshotted at repo HEAD `6725329381`, before the refreshing run was written.
- Corpus `c50002fee1` (unchanged — no score, ground-truth file, or `src/` file is edited by the
  refresh).
- Superseded by: the OI-159 refresh (report `cc_wave1_finalize_report.md`; register row OI-159).
