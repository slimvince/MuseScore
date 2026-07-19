# CC instruction — the OI-184 anacrusis-alignment establishment probe (read-only)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + the 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, the **OI-184 and OI-186 rows in `OPEN_ITEMS.md`**, and
> `cowork_factorization_desk_simulation.md` §4.5 (the finding this dispatch establishes).
>
> **Current state:** branch `master`, HEAD `dcd1b64349` (verify; working tree carries two
> Cowork-authored uncommitted doc edits that ride YOUR commit — see §Commit). **This dispatch is
> PYTHON-ONLY and MEASURE-ONLY** — no build, no test-suite run, no golden, no corpus regen, and
> ABSOLUTELY NO re-baseline or alignment "fix": if a systematic offset is found, it is a FINDING for
> Cowork/user disposition (an alignment correction would move the ratified grading columns and is a
> ratified re-baseline event of its own, the OI-142 pattern — not yours to start).
>
> **Hard stops, always:** any edit under `src/`; any edit to the pinned instruments
> (`a8_rebaseline_measure.py`, `compare_rn.py`, `dcml_parser.py`, `robust_stop_diff.py`) or
> `tools/robust_stop/` — import only; any golden/corpus/baseline touch.

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — the OI-184 establishment step the
ratified OI-176 protocol requires before boundary/metric-table counts are drawn from
anacrusis-bearing pieces (`cowork_prefit_gates.md`, held-out protocol item 7). **The question to
answer positively (#19), either way:** what convention maps WiR `(measure, beat)` chorale annotations
to OUR tick grid, and is it correct on anacrusis-bearing pieces? The desk simulation's hand-mapping
of `bwv110.7` (our m0 = WiR `m0 b4`, verified at the region data) left the GT chord stream reading
one beat later than our verified region contents across m2–m3 while the chord-content pairing was
exact — hand-mapping error, WiR numbering convention, and local GT misalignment are all still live
hypotheses. Establishing "the mapping is correct, the hand-mapping erred" is as valuable as finding
an offset.

## Task 1 — document the actual mapping code path (read-and-report)

Trace and report, with file:line citations, how a WiR chorale `analysis.txt` region's
`(measure_number, beat)` (from `dcml_parser.parse_rntxt_file`) becomes a TICK span when graded
against our regions (`a8_rebaseline_measure.build_piece_grid` / whatever `compare_rn` path it uses):
where the measure→tick table comes from (our `.ours.json` fields? a fixed measure length?), how the
anacrusis/pickup measure (WiR `m0`) is handled, how 3/4 vs 4/4 pieces differ, and whether
`abs_tick` (the DCML-TSV path) plays any role for the rntxt chorales (expected: no — cite the code).
No speculation: every claim a file:line.

## Task 2 — the alignment probe (new read-only instrument)

**New `tools/joint_estimator/gen_wir_alignment_probe.py`** → committed artifact
`tools/joint_estimator/wir_alignment_probe.json` (+ short generated summary txt). For each of the 326
covered stems (Default corpus dir; loaders imported from the pinned instruments):

1. **Anacrusis classification:** whether OUR score starts with a pickup (first region
   `measureNumber == 0`, corroborated where cheap by the measure-tick arithmetic) and whether the
   WiR analysis carries an `m0` line — report the 2×2 contingency (ours-pickup × WiR-m0); any
   mismatched pair is itself a finding.
2. **Per-piece best-offset measurement:** for candidate GLOBAL time offsets of the GT stream in
   {−960, −480, 0, +480, +960} ticks, re-run the grid root-comparison (the imported a8/compare_rn
   machinery, GT boundaries shifted by the candidate offset) and record the duration-weighted
   root-agreement per offset. Report per piece: the argmax offset, its agreement, the margin over
   offset 0, and the piece's anacrusis class. (Root-agreement is the established alignment signal —
   a systematically better nonzero offset means the mapping, not the analysis, is off.)
3. **Aggregates:** the argmax-offset distribution split by anacrusis class (the load-bearing table:
   if anacrusis-bearing pieces cluster at ±480 while non-anacrusis pieces cluster at 0, the
   convention is established as broken exactly there); the list of pieces whose margin over offset 0
   exceeds 2 % agreement (candidates for the `bwv245.40`/`bwv429` local-misalignment class vs a
   systematic convention error — distinguish by whether the whole anacrusis class moves or only
   isolated pieces).
4. **The named case:** `bwv110.7`'s full per-offset profile, explicitly, resolving the desk-sim §4.5
   question for that piece.
5. **Establishment of the probe itself (#19):** byte-reproducible on a second run; and a sanity
   anchor — at offset 0 the aggregate root-agreement must reproduce the block-(A) Default figure to
   within rounding (it is the same computation; state the reconciliation in the report; a
   discrepancy is a STOP, the probe is then mis-built).

## Commit

**One commit:** `tools: the OI-184 WiR anacrusis-alignment probe + artifact (measure-only)` —
the probe, its artifacts, this instruction file (force-add, `/cc_*.md`), **plus the two
Cowork-authored doc edits already on disk that ride this commit:** `OPEN_ITEMS.md` (the new OI-186
row — verify that is its only diff) and `cowork_handoff.md` (the state/pending update — verify that
is its only diff). Push **origin only** (the standing `cfc7eb5e39` hard stop).

## Self-check before reporting (standing rule)

Re-read the actual diff: nothing outside `tools/joint_estimator/` + this instruction file + the two
named doc files; pinned instruments untouched (empty diff proven); no re-baseline, no fix, no
behavior change anywhere; artifacts generated, no hand-typed figure. **Report:** the Task-1 code-path
description; the 2×2 anacrusis contingency; the argmax-offset distribution by class; the >2 %-margin
piece list; `bwv110.7`'s profile; the offset-0 reconciliation against block (A); reuse-vs-new;
anomalies (#13 — surface, do not build around).
