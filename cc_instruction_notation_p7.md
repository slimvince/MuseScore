# CC instruction — seams-2 close-out (unit "P7"): partition-completeness verification + documentation consolidation

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (the INDEX),
> `C:\s\MS\cowork_notation_output_contract.md`, and — as the completeness checklist —
> `C:\s\MS\cc_instruction_notation_seams_2.md` (REFERENCE ONLY: the ratified partition P0–P7
> and amendments 1–6) plus the handoff's dated delivery blocks (P0…P6).
>
> **What this is:** the LAST unit of the seams-2 partition — no new behavior, no new code
> paths: a completeness verification + documentation consolidation, closing the partition so
> the switch ratification can be assembled on a verified-complete record.
>
> **Current state:** branch `master`; expected HEAD `89412b48b2` (P6 Task 3+4, pushed) —
> verify; mismatch = STOP. Riding Cowork edit: `cowork_handoff.md` (commit with your commit;
> verify only non-yours tracked diffs). This dispatch file stays untracked.
>
> **Hard stops:** origin only; NO code change (docs, register notes, and a read-only
> verification script output only — if the completeness check finds a GAP, that gap is a
> FINDING/STOP, never a quick fix inside this unit); three suites green unchanged; no golden.
> VS Code bash rules on every command.

**Dispatch author:** Cowork, 2026-07-27, at the P6 verification.

**Touchable set:** `ARCHITECTURE.md`, `STATUS.md`, `OPEN_ITEMS.md` + `open_items/` (dated
notes only), `cowork_handoff.md` (riding), `tools/notation_seams/` (the completeness-check
output artifact only). Nothing else.

---

## Task 1 — the partition-completeness verification (read-only)

Against the ratified partition (P0–P7 as re-partitioned: P0 flag / P1 constants / P2a gates /
P2b adapter / P3a annotation emitter / P-strings / P4 implode+tuning+bucket+OI-182 / the
merged note-seam / P6 OI-204+dual-arm) verify, at the code and the register, and record in a
small generated artifact (`tools/notation_seams/partition_completeness.json`):

1. Every audited consumer (the audit CSV's roster: composing bridge span+note paths, implode,
   tuning, section layer + cadence/pivot, interaction, context menu, accessibility chain) has
   its record-arm branch behind `useJointNotationRecord` — cite the branch site per consumer.
2. Every ratified ruling of the increment is implemented or explicitly carried: the raw-gap
   rule (no [0,1] remap anywhere on the record arm — grep-verify); the C1 two-mode display;
   the D2 grading/display split; the Nashville presentation path; the pedal suspension
   (OI-194 comment at the sites); the §4.1 constants at their declared sites (the two gap
   constants + the retired 0.35 + the re-homed 960); the boundary guard present and green.
3. Every seams-era register row is in its correct state: OI-182 EXECUTED, OI-195/197/202/204
   RESOLVED, OI-196/201/203 OPEN with their carried dispositions, OI-193/OI-194 OPEN
   (post-switch work) — the INDEX is the authority; fix nothing, report any mismatch as a
   FINDING.
4. The flag's default is OFF everywhere (the switch has NOT happened) and the three suites +
   13 snapshot tests are green at HEAD (run them; totals in the artifact).

**A gap found here is a FINDING/STOP for Cowork — this unit repairs nothing.**

## Task 2 — documentation consolidation (#10)

1. `ARCHITECTURE.md`: consolidate the accumulated per-unit record-path blocks into ONE
   coherent as-built section — the record path end-to-end (producer with input scoping →
   record → section adapter → the consumers; the presentation formatters and the boundary
   guard; the dual-arm instrument), the DUAL-ARM state named as the declared #23 migration
   posture awaiting the switch, the switch's scope named (flag default + goldens + docs).
   Remove nothing historical — consolidate forward.
2. `STATUS.md`: the partition-close entry — the P0…P7 delivery list (hashes), the P6
   classified counts, the pre-switch state ("awaiting the user's switch ratification; the
   evidence: `tools/notation_seams/dualarm_classified_report.json`"), the named post-switch
   agenda (OI-193, OI-194, OI-203, the OI-180 map, OI-198/199/200).
3. Dated close-out notes on the OI-180 detail file (the dual path's forward exit is ASSEMBLED,
   pending ratification) — the INDEX row untouched (the map executes post-switch).

## Report

The completeness artifact's verdicts (per consumer, per ruling, per row — all PASS or the
FINDING list); suite totals; the consolidation's diff summary; anomalies. ONE commit (docs +
artifact + riding handoff), message: `notation seams-2 P7: partition close-out — completeness
verified, docs consolidated (pre-switch state)`. Push origin. Standing self-check before
reporting.

**After this unit:** Cowork assembles the SWITCH decision surface for the user (§8.4: the one
ratified commit — flag default flips, goldens refresh against the established record with the
P6 classified report + the adoption record as the cited preconditions, CLAUDE.md staged-scope
block + STATUS + ARCHITECTURE + rows + the handoff dual-path line move together). The switch
commit is a separate, Cowork-written, user-ratified dispatch.
