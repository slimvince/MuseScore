# CC DISPATCH — REGENERATE THE DERIVATION BOOT PACKS

*Written by the Cowork writing side, 2026-08-26, against tip
`68c42b7f7743c02bdebefacdd9ed06ca9060fbbe`. Executes the first act named by the sixty-sixth entry
of `cowork_handoff.md`. This dispatch carries NO ruling and NO decision. It is a regeneration.*

---

## Why this exists, in one paragraph

Three clause amendments landed in `CLAUDE.md` at principles #18, #19 and #24 on 2026-08-26. The two
derivation boot packs render the guiding principles and the ratified design intent, and they were
generated before that landing, because the amendment-landing dispatch's §6 forbade touching the
generator, the manifest and the pack directories. So both packs now render the PRE-AMENDMENT text.
Any pilot or derivation session booting from either pack reads rules that are no longer the rules —
which is the precise failure the amendments were ruled to prevent. This dispatch cures it and does
nothing else.

---

## Task 0 — start state

(a) Take the session-start read (#6): `CLAUDE.md`, `STATUS.md`, `DECISIONS.md` in full;
`BUILD_AND_TEST.md` conditional; rule (a)'s `gating_ids`.

(b) Read `.git/refs/heads/master`. It must read
`68c42b7f7743c02bdebefacdd9ed06ca9060fbbe`. **If it does not, STOP and report** — this dispatch was
written against that tip and nothing below is safe on another.

(c) **Do NOT run `git status`** — the `PreToolUse` guard refuses it (D-253). Run:

```
python tools/audit/changed_paths.py
```

Record the untracked population count. Do not commit any of it; the standing untracked population is
already routed.

(d) The 2026-08-26 handoff merge is ALREADY DONE — `cowork_handoff_entry_66_pending.md` does not
exist and the sixty-sixth entry is merged at the top of `cowork_handoff.md`. **Do not re-perform it
and do not create the pending file.**

---

## Task 1 — measure the drift before curing it

```
python tools/audit/gen_derivation_boot_pack.py --check
```

Expected: **exit 1**, reporting drift across `tools/audit/derivation_boot_pack.json` and four pack
files under `tools/audit/derivation_boot_pack/`.

Record the exact list of paths it names as drifted, verbatim.

**If it exits 0, STOP and report.** This dispatch's whole premise is that the packs are stale; if
they are not, the premise is false and the writing side must be told rather than have the dispatch
proceed on it.

---

## Task 2 — regenerate

```
python tools/audit/gen_derivation_boot_pack.py
```

(No flag is write mode; `--check` is verify mode. `--subject` scopes to one subject and is **not**
used here — both subjects are stale.)

Then immediately:

```
python tools/audit/gen_derivation_boot_pack.py --check
```

Expected: **exit 0**. **If it is not 0, STOP and report** with the tool's full output.

---

## Task 3 — the blinding check. THIS IS A HARD STOP.

The packs exist to give an implementation-blind session a boot surface with a withheld family
applied. `--check` re-renders with the withholding applied, and the generator carries its own
numbered stop conditions for a malformed or leaking withheld table. That is not sufficient here,
because this dispatch changes the source text the withholding is applied to.

Report, **for each of the two subjects** `harmony-boundary` and `scoring-model`, as rendered in the
NEW pack:

- the count of withheld identities;
- the count of withheld documents;
- the count of withheld passages.

Compare each of the six numbers with the same number in the pack as it stood before Task 2.

**If any of the six changed, STOP and report.** A regeneration that changes what is withheld is not
a regeneration, and the writing side must rule on it.

**Do not quote any withheld passage, withheld identity string or withheld document name into the
report.** Counts only. The report is read by sessions that must stay blind.

---

## Task 4 — the STATUS.md entry and the forward bound

(a) Write ONE entry in `STATUS.md` for this batch. Per the OI-222 remedy it is a **POINTER** to
`cc_report_boot_pack_regeneration.md`; per **D-431** it restates no count, no identity and no
rendered value.

(b) Move the forward bound with the tool, not by hand. `tools/audit/gen_status_batch_bound.py` is
the **named carve-out** under which a `.py` source edit is permitted for its aiming constants — and
the constants are **five**, not three: the previous batch found that `ACT_DATE` and `TASK` are
interpolated into the archive header, so leaving them would write two false statements into a
governing document.

Read the tool's own argument parser and its constants first, re-aim it, run it, and **report the
exact command line you used** and the exact constant values you set. Do not infer the flag from this
dispatch — this dispatch does not state it, deliberately, because the writing side did not open the
tool.

This is the ONLY `.py` source edit this dispatch permits.

---

## Task 5 — the sweep

Run the guard sweep as ruled and classify every red.

**Three reds are STANDING and are NOT this batch's to cure. Expect them, name them, leave them:**

1. `[[OI-372]]` — the one standing DECISION red, and it is **never regenerated**.
2. `apply_soft_discard.py --check` — conflates the live record before the 2026-08-16 act with the
   block's running population invariant.
3. `apply_residue_discard.py --check` — hard-codes the live-record size of 2026-08-17; one of its
   two limbs reconciles at no value of any field once an entry is added.

Curing (2) or (3) means running a ruled discard act in write mode. **This dispatch does not
authorise that.**

**For any red that is not one of those three: if you cannot tell whether it is a decision red or a
regeneration red, treat it as a DECISION red and STOP.** The sweep rule is absolute.

Note the standing blast radius when you read the sweep: one register row moves five artifacts, two
of them invisible to any instruction phrased as regenerating only what goes red. This dispatch
orders no register row, so that radius should not open — if it does, that is itself a finding.

---

## Task 6 — report and commit

Write `cc_report_boot_pack_regeneration.md` at the repository root. Then commit.

In the report, state explicitly and separately:

- the Task 1 drift list, verbatim;
- the two `--check` exit codes, before and after;
- the six blinding counts and their six comparisons;
- the exact `gen_status_batch_bound.py` command line and constant values;
- the sweep result, with every red named and classified;
- **every departure from this dispatch, and every instruction in it you found you could not obey.**

When you state a hash, **say which side you measured** — a worktree hash and a blob hash do not
agree for a CRLF file. **Never write a file's own hash into that file.**

---

## §7 THE FENCE

Writes are permitted at **exactly** these paths and nowhere else:

- `tools/audit/derivation_boot_pack.json`
- everything under `tools/audit/derivation_boot_pack/`
- `tools/audit/gen_status_batch_bound.py` — aiming constants only, under its named carve-out
- `STATUS.md` — one pointer entry
- `cc_report_boot_pack_regeneration.md` — new file
- **any file that a tool this dispatch orders you to run writes as that tool's own output** (this
  covers the sweep's state file and any `changed_paths_*.json`). Name each one in the report.

**Explicitly forbidden.** No `CLAUDE.md` edit. No `ARCHITECTURE.md` edit. No entry in the decisions
register — a regeneration is not a ratification, so register rule (c) is not engaged, and this
dispatch is deliberately shaped to keep the two broken discard-act checks out of its path. No
`src/` change, no test changed, moved or run, no golden. Nothing under `tools/corpus/` or
`tools/robust_stop/`. No open-items row created, flipped or discarded. No finding number allocated.
No admission to the empirical findings ledger. Do not open either blind derivation output. No other
`.py` source edited.

**★ AND THE CLAUSE THAT MATTERS MOST, BECAUSE THE WRITING SIDE HAS BROKEN IT TWICE IN CONSECUTIVE
DISPATCHES:**

**If obeying any instruction in this dispatch would require a write outside this fence, STOP and
report the conflict. Do not choose a route. Do not widen the fence yourself. Do not pick a weaker
form of the instruction to stay inside it.** The last two dispatches each ordered a write their own
fence forbade — `cc_instruction_register_reconciliation.md` Task 2, and
`cc_instruction_amendment_landing.md` Task 5, which stopped. You stopping and reporting is the
correct outcome, not a failure of the batch.
