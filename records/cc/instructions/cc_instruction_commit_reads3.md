# CC dispatch — commit read wave 3

> **Status: ACTIVE DISPATCH, written 2026-08-04 (Cowork).** One act.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_commit_reads3.md`.

## 0. THE RULING LEDGER

- **R1 — RULED by the user, 2026-08-04:** commit read wave 3's work. The authorization the phase's
  standing convention requires is given here explicitly; read wave 3's Task 7 presupposed a commit it
  never authorized, which was a defect in Cowork's dispatch and is corrected by this one.

## 1. The act

Commit read wave 3 as **one provenance-stamped commit**.

- Verify what is being committed through `tools/audit/changed_paths.py` first. **If anything is
  modified outside read wave 3's own work, STOP and report.**
- Commit by git plumbing.
- **Re-run every guard at the COMMITTED tree**, with the list derived by `gen_guard_state.py` — the
  previous run was at the working tree, as the report correctly said. Report the pre-existing
  failures as moved or unmoved, and **fix none**.
- Where the commit itself drifts an anchor, re-aim per citation from the verifier's own numbers.

## 2. What this dispatch does NOT license

No fix, no design, no inference change, no `src/` edit, no tool built or repaired. The freeze holds.
**OI-326 is not settled by this wave** — it is with the user, and every wave-3 entry stays a
documentation gap until it is ruled.

## 3. Self-check (D-434)

- The ruling ledger carries the authorization whose absence caused the defect this dispatch fixes.
- No figure asserted (D-431); the changed-path set is named as the tool's output, not transcribed.
- Scope is one act, stated once.
