# CC Instruction — Stage-5 R10-a: ASSEMBLE the batch→robust stop handover surface (measurement + draft only; the ratification follows as its own event)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** Tenth CC increment — the Stage-5 arc's closing assembly, per
> design §4.7 and the ratified A-8 dual-track (CLAUDE.md). **This dispatch PREPARES the R10 handover: the
> committed robust-unit reference artifacts, the old→new mapping, the measured operational procedure, and
> the DRAFT successor-stop text. It changes NO standing document's normative content (no CLAUDE.md gate
> rewrite), no committed value, no corpus, no push.** The handover itself is the user's ratification
> event (R10-b) on this surface.
>
> Read first: CLAUDE.md (the gate sections incl. the A-8 dual-track note — the text this arc will
> supersede) · design §4.7 + O-11 · `cc_stage5_phase2_2e_report.md` (the current baselines) ·
> `cc_a8_rebaseline_measure_report.md` §1 (the pinned unit/variant/identity definitions).
>
> **Current state (Cowork-verified 2026-07-06):** HEAD = the Phase-3 SHA-completion (`443e79dabd`);
> batch stop **52/24/52** (corpus `c50002fee1`, fingerprint-validated); A-8 ratified baselines
> 63.36/62.37/63.25 (root), RN 44.58/42.40/44.41, key 68.19/64.52/67.77 (the 2.2e re-measure); suites
> 1101/53(+4 skips)/11. Expected dirty: the Cowork fold files + known scratch.
> **Hard stops:** any normative doc change (the draft lives in the report); any corpus write; any push.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set; characterise ×3 = 52/24/52 set-diff empty (the batch stop's LAST run as THE
stop, if R10-b ratifies). Report.

## Task 1 — the committed robust-unit REFERENCE artifacts (the future diff base)

Run the pinned A-8 instrument (`a8_rebaseline_measure.py`) on the current corpus and COMMIT the
reference artifacts every future explained-diff will diff against, under a dedicated committed dir
(propose the name; e.g. `tools/robust_stop/`):
1. Per preset: the **variant-(b) root-fail RUN enumeration** (`stem@runStartTick`, the re-slice-stable
   identity per the A-8 §1.4 definition) with per-run: our root · WiR root · duration · two-tier class.
   Expected scale ≈ 6.9–7.0k runs/preset — committed (they are the diff base; the batch stop's 52-line
   set lived in CLAUDE.md, this one lives as artifacts with CLAUDE.md pointing at them).
2. Per preset: the summary block — scored duration · root/RN/key agree % · class-(b) and class-(a)
   root-disagree DURATIONS (the governing quantities) · run/cell counts. These summary numbers must
   reproduce the 2.2e-ratified baselines exactly (63.36/62.37/63.25 root; a mismatch = STOP).
3. A manifest stamping the corpus git_hash + instrument provenance (the O-12 pattern).

## Task 2 — the old→new mapping (every batch case accounted)

Locate each of the 52/24/52 batch cases on the run enumeration (the A-8 §3 method, at the current
corpus): expected = every case maps to a still-failing run under variant (b) (0 disappeared at the
original measurement; re-verify now). Any case that fails to map = report it with its mechanism
(do not hide it in an aggregate).

## Task 3 — the operational procedure, measured + drafted (the ratification material)

1. **The successor sandwich, timed:** the exact check a future increment runs — the a8 full-3 measure
   (~14 s at Phase-0 timing; re-time now) + per-preset: (a) **class-(b) root-disagree duration
   NON-INCREASE** vs the committed reference (the hard stop), (b) the **run-level set-diff vs the
   reference, explained** (added/removed runs listed with class; the mandatory diagnostic), (c) class-(a)
   duration tracked (the large-net-increase investigation tripwire carries over). State the exact
   commands + the pass/fail rule as a runnable snippet.
2. **The batch instrument's disposition (proposal):** `characterise_bir_false.py` + the 52/24/52 sets →
   KEPT-AS-DIAGNOSTIC (the R3 pattern): still runnable, no longer the stop; the CLAUDE.md identity sets
   freeze as a historical reference at R10-b. State what (if anything) breaks if it bit-rots — the
   retirement-by-silence guard.
3. **The DRAFT CLAUDE.md gate-section replacement text** (in the report only): the robust stop's
   definition (unit · variant (b) · root governs, RN/key tracked · the duration hard-stop + explained-diff
   semantics · the two-tier per-cell policy · the reference-artifact pointers · the re-baseline
   discipline for future adoptions — the 2.2e pattern generalized: adoptions re-baseline the reference
   artifacts with removal/addition diffs explained and ratified). Also the one-paragraph dual-track
   RETROSPECTIVE (what the batch stop was, where its history lives).
4. **Cost/practicality note:** the robust sandwich vs the batch sandwich (time, artifact size, failure
   readability) — the operational trade the user ratifies with eyes open.

## Task 4 — sandwich + report + fold
1. BOTH stops measured at end: characterise ×3 = 52/24/52 empty; the a8 summaries reproduce the
   baselines; corpus fingerprint-validated untouched; suites green.
2. Report `cc_stage5_r10_assembly_report.md` (force-add): the artifacts + mapping + procedure + draft
   text + cost note; reuse-vs-new + retires (nothing retires in THIS dispatch — R10-b does the
   retiring); all SHAs.
3. Fold (`docs(cowork):`): `STATUS.md` (22z) · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md` ·
   `cowork_confidence_contract.md` (the Phase-3 Cowork row-edits, now in the tree) ·
   `cc_instruction_stage5_r10_assembly.md` (force-add).

## STOP conditions
- The Task-1 summaries not reproducing the ratified baselines; a Task-2 unmapped case.
- Any normative doc change; any corpus write; any push; suites/sandwich regression.
- Cost >4× (~expect: one a8 full run + Python; well under an hour).

## Acceptance
Committed reference artifacts ×3 with manifest ✓ · every batch case mapped (or its exception mechanism
reported) ✓ · the successor sandwich runnable + timed ✓ · the characterise disposition + draft CLAUDE.md
text + retrospective in the report ✓ · both stops green at close ✓ · report + fold with SHAs ✓.
