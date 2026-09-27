# CC INSTRUCTION — THE L2 PACK BUILD, CLOSE: FINISH §12(d) TO §13 OF THE STOPPED BATCH (2026-09-27)

> **STATUS: RELEASED 2026-09-27.** Written by Cowork after reading, whole,
> `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` (49,458 bytes at staging) and
> checking its STOP at the two tool sources. **Run R0 to R6 in order. If any expected result does not
> appear, stop at that step and report it. Do not continue to the next one, and do not resolve a bar
> that contradicts a step.**

**What this dispatch does.** The batch of
`records/cc/instructions/cc_instruction_l2_pack_build_second_half_2026_09_27.md` (pinned at blob
`7d5267c5c60f6380dd87d151e0ebc4c4a2eec234`; called "the pinned dispatch" below) stopped at its §12(c).
This dispatch finishes it: one correction to the batch's own `STATUS.md` entry, then the pinned
dispatch's §12(d), §12(e), §13(a) and §13(b), unchanged except where this file says so.

**Why the STOP is resolved by NOT expecting the member, and nothing else.** The pinned dispatch's
§12(c) expected `tools/audit/gen_evidence_pin_membership.py` to publish
`tools/audit/gen_withheld_family_reading.py` as an UNRESOLVED pinned-evidence member. That expectation
was a PREDICTION, first written at §5 of `records/cc/reports/cc_report_l2_ruling_writeback_2026_09_05.md`
without running the tool, carried into the wording of Ruling 8 of
`records/cowork/rulings/cowork_rulings_2026_09_05_l2_boot_list_sitting.md`, and relayed into the pinned
dispatch by the Cowork side without checking the pin tool's detection shape. **Checked now, at both
tool sources, by the Cowork side:** the pin tool recognises a generated document only through a
module-level constant matching its `NAMES_SURFACE` pattern plus a write through that constant
(`writes_it`); `gen_withheld_family_reading.py` declares its output as the value `"out"` inside its
`SUBJECTS` table (line 50) and writes it through a local variable (`open(out, "w", …)`, line 468).
So the regeneration's result — seven members, none UNRESOLVED, the L2 reading document filed as named
but not generated — **is the true output of the tool as it stands.** The pin tool's blind spot is a
finding for the user and is **reported, not repaired** (D-436). The regenerated
`tools/audit/evidence_pin_membership.json` is committed as it stands.

---

## Bars

**The pinned dispatch's B2 to B9 bind this dispatch unchanged.** **B1 is NARROWER here: NO tool source
is edited by this dispatch at all** — not `tools/audit/gen_derivation_boot_pack.py`, not
`tools/audit/gen_status_batch_bound.py`, not `tools/audit/gen_evidence_pin_membership.py`, not
`tools/audit/gen_withheld_family_reading.py`, not any other. The tool edits the stopped batch already
made are committed as they stand on disk.

**No figure in this file is written into any artifact (D-431).** The blob hashes in R0 are start-state
bars read from the report's §10; that report is uncommitted and relayed, and R0 is where they are
established.

---

## R0 — the start state, established before anything is written

1. Read `.git/refs/heads/master` and `.git/refs/remotes/origin/master` **with the file tools**.
   `master` must read `a84e2375301973b48cb2a0cc5a0fb13e6ec41c24`; `origin/master` must read
   `9909492ff02b19e4163eaed73ce163e7c62f742c`. *(Both read so by the Cowork side at the ref files.)*
   Anything else: **STOP**.
2. `python tools/audit/changed_paths.py`. **Nothing may be staged.** The modified tracked paths must
   be exactly: `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/derivation_boot_pack.json`,
   `tools/audit/evidence_pin_membership.json`, `tools/audit/gen_derivation_boot_pack.py`,
   `tools/audit/gen_status_batch_bound.py`, `tools/audit/l0_l1_outgoing_population.json`,
   `tools/audit/status_batch_bound.json` and the held-back `tools/audit/claude_md_finer_archive.json`;
   the new paths from that batch are the ten files of `tools/audit/derivation_boot_pack/l2/` and the
   report; the new path from the Cowork side is this dispatch (and, if it exists,
   `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md`); the rest is the
   standing untracked population. **Any other modified tracked path: STOP.**
3. `git hash-object` each of these and compare with the report's §10: the boot-pack tool
   `9c3c78fcbd89dcf34f303881451610049cbdb6e9`; the manifest `3fa7d30c67f63f3efd660dfd4f6c0e7dc3cf881a`;
   `STATUS.md` `2c8ace0d624cbe9fcb902b4aabcba9eb542f2809`; `STATUS_ARCHIVE.md`
   `160ece0f9274a0669bd2a52ec601a0cb08a4df78`; `tools/audit/status_batch_bound.json`
   `a29df6799a5962747c8980e16e69994ea229c842`; `tools/audit/evidence_pin_membership.json`
   `92f4522642d88f1ef754c1cdb3843c17d0749e7b`; `tools/audit/l0_l1_outgoing_population.json`
   `e310fb57ac53f9a06f8a9295d70c17ec143e3ce3`. **Any mismatch: STOP** — the tree changed after the
   stop.
4. Run `python tools/audit/gen_derivation_boot_pack.py --check`. Expected: `the derivation boot pack
   re-derives` and the three `FROZEN — N file(s) at their recorded blobs` lines, exit 0. Otherwise
   **STOP**.

## R1 — one correction to this batch's OWN `STATUS.md` entry

The entry the stopped batch wrote at the head of `STATUS.md`'s dated entries says the leak list goes
to the user *"together with the pinned-evidence members the regeneration published"*. No member was
published. In `STATUS.md`, the string

```
together with the pinned-evidence members the regeneration published.
```

must occur **exactly once** (STOP otherwise). Replace it with:

```
together with the finding that the regeneration published NO pinned-evidence member for the L2 reading document, `tools/audit/gen_evidence_pin_membership.py` not recognising the table-declared output of `tools/audit/gen_withheld_family_reading.py` (former wording, preserved (#12): "together with the pinned-evidence members the regeneration published").
```

Nothing else in `STATUS.md` changes. This is the batch's own entry of this batch, written at its
12(a); no earlier batch's sentence is touched. **This is now the last write to `STATUS.md` in this
batch.**

## R2 — the two regenerations re-checked after R1

`tools/audit/gen_l0_l1_outgoing_population.py` reads `STATUS.md` (it reads every member of the
`governing-documents` class of `tools/audit/artifact_inventory.json`). So, in this order:

```
python tools/audit/gen_l0_l1_outgoing_population.py --check
```

If it prints `l0_l1_outgoing_population.json re-derives` (exit 0), do nothing more with it. If it
reports STALE, run `python tools/audit/gen_l0_l1_outgoing_population.py` and then its `--check`
again, which must exit 0 — this is the same Ruling 8 regeneration re-run on the final `STATUS.md`,
not a new act. Then:

```
python tools/audit/gen_evidence_pin_membership.py --check
```

Expected exit 0 (that tool does not read `STATUS.md`). Record every output and exit code verbatim.
A `STOP:` line or a traceback from either: **STOP**.

## R3 — the pinned dispatch's §12(d), unchanged

Run exactly the four commands of the pinned dispatch's §12(d) and record all four outputs and exit
codes verbatim. Both `--check` runs must exit 0; a `STOP:` line or a traceback is a **STOP**. Do not
edit either tool.

## R4 — the pinned dispatch's §12(e), unchanged

The closing guard capture, compared **verdict by verdict** against the opening capture the stopped
batch saved at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\4be43c84-f33e-4ed4-ba31-5011217eded4\scratchpad\guard_open.txt`.
**If that file is not there, STOP and report it** — do not reconstruct it. The condition is the pinned
dispatch's: no guard whose verdict was PASS at the opening may carry any other verdict now; FAIL → PASS
is allowed and reported. `tools/audit/gen_guard_classification.py` is expected to STOP (B8): run it,
report it whole, carry on.

## R5 — the pinned dispatch's §13(a) and §13(b), with the candidate set restated

**One batch commit, by explicit path, never a directory pathspec.** The candidate set is exactly:

1. `tools/audit/gen_derivation_boot_pack.py`
2. `tools/audit/derivation_boot_pack.json`
3. the ten files of `tools/audit/derivation_boot_pack/l2/`, each by its own path
4. `STATUS.md`
5. `STATUS_ARCHIVE.md`
6. `tools/audit/gen_status_batch_bound.py`
7. `tools/audit/status_batch_bound.json`
8. `tools/audit/evidence_pin_membership.json`
9. `tools/audit/l0_l1_outgoing_population.json`
10. `tools/audit/session_start_read_size.json`
11. `tools/audit/defense_share.json`
12. `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` (with R6's addition)
13. `records/cc/instructions/cc_instruction_l2_pack_build_close_2026_09_27.md` (this dispatch)
14. the guard set's own artifacts, **only those the enumeration reports as modified** — name each.

**Prove the staged set is EXACTLY this set before committing.** Nothing under
`tools/audit/derivation_boot_pack/harmony-boundary/`, `…/scoring-model/` or `…/l0-l1/` may be staged
(B3). **Held back:** `tools/audit/claude_md_finer_archive.json` (B9); entry 252 if it exists (it lands at
the next batch's Task 0); and every other path the enumeration reports. Confirm each is absent from the
staged set.

**Then push** every branch that received commits (`master`: the two Task 0 commits and this one).
`origin` is the fork; `upstream` is not used; **never `--force`**. Read
`.git/refs/remotes/origin/master` with the file tools afterwards and confirm it equals `master`. If the
push fails for any reason, report it.

## R6 — the report

**Append** to `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` — additions only,
nothing above rewritten — a section headed `## 12. The close, resumed under cc_instruction_l2_pack_build_close_2026_09_27.md`,
carrying in step order every output this file says to record, the verdict-by-verdict comparison naming
every guard that moved and in which direction, the commit hash, the pushed branches and
`origin/master` after the push. Change the report's STATUS line only by appending, after it, one line
saying the batch was closed by this dispatch; the original line stays.

**What goes to the user, named rather than counted:** the leak list (already in the report); the pin
tool's blind spot — a generator that declares its ratification-document output in a table rather than
in a module-level constant is not seen, so its document is filed as not generated; and any STOP.

---

*Provenance: Cowork, 2026-09-27 (Stockholm), the sitting booted on entry 250, after the stopped
batch's report was read whole. Checked at the objects by that sitting: both ref files; the pin tool's
`NAMES_SURFACE`, `writes_it` and `generated_documents`; `gen_withheld_family_reading.py` lines 47–50 and
its `open(` calls; `tools/audit/evidence_pin_membership.json`'s counts and its named-but-not-generated
list; §5 of the 2026-09-05 writeback report; `STATUS.md`'s head entry; the listing of
`tools/audit/derivation_boot_pack/l2/`. The blob hashes of R0 item 3 are relayed from the report and
are established at R0.*
