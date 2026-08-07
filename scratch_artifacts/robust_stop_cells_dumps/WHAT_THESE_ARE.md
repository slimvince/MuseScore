# The six `*_root_fail_cells.txt` dumps, moved out of `tools/robust_stop/`

> **Scratch. Not a measurement reference, not committed, not read by anything.** Moved here
> 2026-08-04 on the user's ruling R1 (dispatch `cc_instruction_finish_line_item1.md`). Preserved
> rather than deleted (#12).

## What they are

Per-preset, per-variant enumerations of the **root-respect failing CELLS** — the grid-cell level
below the run level. `tools/a8_rebaseline_measure.py` writes them at `_write_cells`, beside the
run-level enumerations, into whatever `--out-dir` it is given:

| file | what it enumerates |
|---|---|
| `{preset}_variant_a_root_fail_cells.txt` | variant (a), music21-filtered, root-respect failing cells |
| `{preset}_variant_b_root_fail_cells.txt` | variant (b), DCML-only, root-respect failing cells |

Line format, from the files' own headers: `stem@cellStartTick  [start,end) w=<dur>  our=<sym>(<root>)
-> dcml=<rn>(<root>)  bucket=… key=… cls=… 3way=…`.

## Which measurement produced them

**Established by reading their own recorded counts against the committed reference**, not assumed:
each file's header count equals the corresponding field of `tools/robust_stop/summary.json` for its
preset — `grid_a_root_fail_cells` for the variant-(a) files, `grid_b_root_fail_cells` for the
variant-(b) files, on all three presets. That summary is the committed reference of the **OI-178
joint-estimator adoption re-baseline** (user-ratified 2026-07-26; `CLAUDE.md` gate block (A)). So
these are the cell-level enumeration of the same measurement the committed reference records.

**What is NOT established:** which act placed them in `tools/robust_stop/`. Their modification time
is 2026-07-26 11:30; the committed reference files beside them (the `_runs.txt` enumerations,
`summary.json`, `manifest.json`) are 11:22 the same day. `robust_stop_restamp.py` copies only the
run-level and mapping files, so it did not put them there. Nothing further is derivable from the
tree and nothing is asserted here.

## Why they are not part of the committed reference

`tools/robust_stop_restamp.py` states it in terms, in the comment above its `PER_PRESET_FILES`
list: *"The `_cells` files the instrument also emits are diagnostics and are deliberately NOT part
of the committed reference (only the run-level enumerations are — the run is the stop's identity
unit)."* They were untracked in `tools/robust_stop/` for that reason, and gate block (A) names the
run-level enumerations, the `summary.json` aggregates and the `manifest.json` as the reference —
not these.

## Why moving them is measurement-neutral

Every consumer of `tools/robust_stop/` reads it **by explicit filename**; none globs the directory,
so none of them can see these files whether they are present or absent. Enumerated and checked at
the objects on 2026-08-04:

| consumer | how it reads the directory |
|---|---|
| `tools/robust_stop_diff.py` | `{preset}_variant_b_root_fail_runs.txt`, `manifest.json`, `summary.json` — explicit names |
| `tools/robust_stop_restamp.py` | `manifest.json`; writes the explicit `PER_PRESET_FILES` templates |
| `tools/joint_estimator/adoption_measure_b.py` | `{preset}_variant_b_root_fail_runs.txt`, `manifest.json` — explicit names |
| `tools/audit/hardening_battery.py` | passes `--reference` to `robust_stop_diff.py`; reads nothing itself |
| `tools/audit/instrument_arm_declaration_effect.py` | runs the two gate-block-(A) commands; reads through them |
| `tools/mode_grading_adjudication_probe.py` | `summary.json` |
| `tools/joint_estimator/gen_wir_alignment_probe.py` | `summary.json`, `corpus_transposition_offsets.json` |
| `tools/dcml_parser.py` | `corpus_transposition_offsets.json` |
| `tools/audit/gen_signature_sweep.py` | `tools/robust_stop` is a string PREFIX for scanning source-code argparse defaults (DT-24); never reads the directory |
| `tools/audit/gen_inventory.py` | EXCLUDES `tools/robust_stop/` from its enumeration domain by design |

`tools/a8_rebaseline_measure.py` — the tool that WRITES these files — takes a required `--out-dir`
and reads nothing from this directory at all.

**And it was measured rather than argued.** After the move, the gate-block-(A) sandwich was run over
the production corpus by that block's own two commands, and the candidate is indistinguishable from
the committed reference on every preset: run counts equal, set-diff `+0 / −0` in both directions,
class-(b) and class-(a) durations `delta=+0`, key columns and abstain identical, `OVERALL: PASS`.
