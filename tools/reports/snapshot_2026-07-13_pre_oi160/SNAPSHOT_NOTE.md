# Snapshot — the outgoing joint-probe evidence, before the OI-160 collapse (O-12)

**Taken:** 2026-07-13, at HEAD `edd4d3e4cf`, corpus `c50002fee1`.
**Why:** OI-160 collapses the **two** committed artifacts of ONE instrument
(`tools/measure_joint_probe.py`) down to **one** (#6 — one artifact per concern). O-12 requires the
outgoing reference be snapshotted before any re-baseline of committed evidence. Both outgoing files
are preserved here verbatim.

## What is preserved

| file | stamped `git_hash` | what it was |
|---|---|---|
| `joint_probe_measure.json` | `fa0a881aa4` | The **arc-12 chord-axis** run (engage arc #12, `cc_engage_stage3_joint_measure_report.md`) — the go/no-go the "joint step SHELVED on the chord axis" ruling rests on. Chord-axis blocks only. |
| `mode_key_chord_probe.json` | `6725329381` | The **OI-43 key-axis** run (refreshed at OI-159), same instrument — every chord-axis block the arc-12 file has, **plus** the `key_axis_desksim` block (menu-containment, chord-flip-under-GT, alt keyConf). |

## Why they were superseded

Two things were wrong at once, and the collapse fixes both.

1. **A #6 duplication.** One instrument, two committed artifacts. Proven at the files before the
   collapse: **every field of `joint_probe_measure.json` is present in `mode_key_chord_probe.json`**
   (0 fields missing), and the newer adds **exactly** the `key_axis_desksim` subtree (93 paths, 3
   presets) **and nothing else** — a strict superset. There was never a reason to keep two.

2. **Both were graded against the pre-OI-142 ground truth** in part: `joint_probe_measure.json`
   (stamped `fa0a881aa4`) **entirely** pre-dates the OI-142 transposition correction to
   `dcml_parser.load_wir_regions`, so its ground-truth-graded corr/harm split is stale. (The
   OI-159 refresh already fixed the key-axis file; OI-160 is the sibling it declared but was not
   dispatched to touch.)

## What replaced them

**One** canonical artifact: **`tools/reports/joint_probe_measure.json`** — a full both-axes run at
HEAD. That name is the instrument's own natural committed target, named in its `--out` help
(`measure_joint_probe.py:470-477`), and derived from the instrument's name. `mode_key_chord_probe.json`
is **retired**; every citation of either file now points at the one canonical artifact.

**Neither ruling moved.** Both were re-confirmed against the corrected ground truth in the same run:
the arc-12 chord-axis **no-go stands** (net corr−harm `+9 / +3 / +10` → `+9 / +6 / +10`, still ≈ +0.1 pp
of ~6,200 scored regions per preset — far below the +0.3 pp shelve floor), and the OI-43/OI-44
**shelve stands** (menu-containment 75.6 / 68.7 / 72.5 %, still under its 80 % bar; chord-flip-under-GT
byte-identical at 7 / 8 / 6 regions — the coupling still inert).

**No governing surface is involved** — no gate, threshold, fit, or baseline reads this artifact. The
establishment battery is byte-identical across the collapse (`a8_diff` +0/−0 all presets, `calib` 4/4,
`validate` 3/3).

Provenance: `cc_oi160_report.md`; `OPEN_ITEMS.md` OI-160 (and OI-159, the sibling row, same cause).
The prior O-12 snapshot from the OI-159 refresh is kept beside this one at
`tools/reports/snapshot_2026-07-13_pre_oi159/`.
