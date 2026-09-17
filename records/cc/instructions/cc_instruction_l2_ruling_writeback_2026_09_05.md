# CC INSTRUCTION — write the three rulings of the L2 withheld-family sitting back to the verdict table and the reading file (2026-09-05)

> **STATUS: DISPATCH.** Written by the Cowork writing side, 2026-09-05, at tip
> `5ba82c9ea7f84e2ad0d45fde4fc35258a9841e4f` (`refs/heads/master` and `refs/remotes/origin/master`
> both at that hash, read at the two ref files with the file tools before this file was written).
> **Nothing was running when this was written and no other dispatch is out.**
>
> **Where this sits.** The user ruled L2's three verdict lists at the sitting whose record is
> `cowork_rulings_2026_09_05_l2_withheld_family_sitting.md` (untracked at the root; Task 0 lands it):
> LIST ONE as authored, LIST TWO as authored, and LIST THREE — D-453 IN, D-535 OUT. That record's §6
> orders one correction dispatch. **This is it.** It moves two verdicts in the authored table, amends
> the rendering tool's authored prose so the reading file states the test as ruled and shows RULED,
> re-renders the reading file, and changes nothing else.
>
> **What this dispatch is NOT.** It withholds nothing. `WITHHELD["l2"]` is authored only after L2's
> boot-list members are ruled, which is the next decision surface and is not put here. It renders no
> pack and boots no session.
>
> **The one-sentence statement of the whole job:** two tuples in `VERDICTS["l2"]` change their verdict
> word and their reason, five exact edits go into `gen_withheld_family_reading.py`'s authored strings
> and rendering branches, the reading file is re-rendered from them, and the counts read IN 111 /
> OUT 133 / UNPLACED 0.

---

## Read first — the vocabulary this dispatch uses, in plain words

- **The verdict table** is `VERDICTS["l2"]` in `tools/audit/gen_derivation_boot_pack.py`: one
  three-string tuple per candidate — the verdict word, the finding (what the entry's own text says),
  the reason. It is the ONE home of the verdicts; the reading file is rendered from it.
- **The reading file** is `ratification_surfaces/cowork_withheld_family_l2_reading.md`, rendered by
  `tools/audit/gen_withheld_family_reading.py --subject l2`, whose `--check` re-renders and compares.
  It is a generated file: it is never hand-edited, and a change to what it says is a change to the
  tool's authored strings or to the table it reads.
- **The ruling record** is the sitting record named above. Its §1–§3 are the three rulings; its §6
  is the order this dispatch executes. Every string this dispatch puts into the tool is that record's
  content, and the record is the source to check it against.

---

## What this dispatch may NOT do — read before Task 0

- **Move no verdict other than D-453 and D-535**, and change no finding string of any tuple. Task 1
  changes exactly two verdict words and two reason strings.
- **Withhold nothing.** `WITHHELD` is not touched; no `l2` key is added to it.
- **Render no pack and boot no session.** No file under `tools/audit/derivation_boot_pack/` is
  created, edited, deleted or read for writing, and `tools/audit/derivation_boot_pack.json` is not
  regenerated. `write_all` is never reached; the only mode of that generator you run is `--check`.
- **Do not touch `EXTRAS`, `FROZEN`, the `CRITERION` table, `KEYWORDS`, `L2_KEYWORDS` or `DATE`.**
- **Change nothing in the rendering tool beyond the five exact edits of Task 2(a).** No other line,
  no rewording, no reformatting.
- **Do not edit the ruling record.** It is a dated record; Task 0 lands it as it stands.
- **Create no open-items row**, flip or discard none, allocate no `D-NNN`, and write nothing into
  `DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md` or any ruling record,
  other than the one `STATUS.md` entry Task 5 orders.
- **Put no choice question to the user and recommend nothing.**

**STOP conditions, each of which ends the batch with a report and no further task:**

1. The tip at boot is not `5ba82c9ea7f84e2ad0d45fde4fc35258a9841e4f` at **both** ref files. Read
   `cowork_away_returns.md` before anything else and write nothing into the tree.
2. The sanctioned enumeration tool reports **any** tracked modification at boot. **The writing side
   did NOT verify the tree's cleanliness — it has no enumeration tool — so this is an expectation and
   not a measured start state.** A tracked modification is itself the finding.
3. `python tools/audit/gen_derivation_boot_pack.py --check` does not exit 0 at any point. Nothing
   here can move a rendered byte — `build()` iterates `WITHHELD`, which has no `l2` entry — so drift
   means something else happened.
4. Anything under `tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json`
   differs from its committed blob at any point after Task 0.
5. Either of Task 1's two anchor blocks is not found exactly once in the generator, byte for byte as
   quoted. Do not edit anything that does not match; report the mismatch.
6. Any of Task 2(a)'s five `old` blocks is not found exactly once in the rendering tool, byte for
   byte as quoted. Same rule.
7. After Task 2, the rendering tool exits with `STOP:`, or its `--check` does not exit 0 immediately
   after the re-render, or the re-rendered file's counts do not read **IN 111 / OUT 133 / UNPLACED
   0**, total **244**, with 244 table rows, and the LIST THREE heading followed by the empty-list
   sentence.

---

## Task 0 — land this dispatch and the ruling record

**One commit. The paths are: this dispatch, the ruling record, and the Task 0 enumeration artifact.
Nothing else.**

```
cc_instruction_l2_ruling_writeback_2026_09_05.md
cowork_rulings_2026_09_05_l2_withheld_family_sitting.md
```

Enumerate first, with the sanctioned enumeration tool rather than with `git status`:

```
cd C:\s\MS && python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_ruling_writeback_task0.json
```

Redirect the run's output to a scratch file **outside the repository** and read it with the file
tools. **Expect ZERO tracked modifications**, the two paths above present as untracked additions, and
the standing untracked `cc_*` root population present and correctly not landed. **Any tracked
modification is STOP condition 2.**

Commit the three paths together:

```
docs(cowork): land the L2 withheld-family sitting record and the ruling write-back dispatch

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

**On the trailer.** That is the form this repository's own history carries. If a system-level
attribution instruction in force for your session mandates a different form, follow that instruction
and **declare the difference in the report** — the four preceding batches did exactly this and the
departure is expected, not an error. The commit subject and body are this dispatch's, verbatim,
either way.

Push. Report the commit hash, read at both ref files with the file tools.

---

## Task 1 — the two ruled verdicts, written back to the table: ONE commit

In `tools/audit/gen_derivation_boot_pack.py`, inside `VERDICTS["l2"]`, group A's block. Each edit
keeps the tuple's FINDING string byte for byte and changes only the verdict word and the reason.

**(a) D-453 → IN (Ruling 3).** Replace exactly this (located by its text; it occurs once):

```python
        "D-453": (VERDICT_UNPLACED,
                  "Its verbatim is a verdict — 'the ratified factorization passes nine of ten "
                  "traces as specified; no finding requires re-ratifying the STRUCTURE (variables, "
                  "factors, decode)' — and states no variable, factor or decode rule.",
                  "The published text says that a structure survived checking without saying what "
                  "any part of that structure is, so it settles no limb either way."),
```

with exactly this:

```python
        "D-453": (VERDICT_IN,
                  "Its verbatim is a verdict — 'the ratified factorization passes nine of ten "
                  "traces as specified; no finding requires re-ratifying the STRUCTURE (variables, "
                  "factors, decode)' — and states no variable, factor or decode rule.",
                  "Ruled IN 2026-09-05 from UNPLACED (Ruling 3 of "
                  "`cowork_rulings_2026_09_05_l2_withheld_family_sitting.md`): its plain names the "
                  "counting granularity as the one thing sharpened and the variables, factors and "
                  "decode as ratified, so a session reading it learns that a ratified factorization "
                  "exists and which of its points was open; the pilot's family graded the same text "
                  "IN and that ruling stands, and the same text cannot settle the superset question "
                  "less than it settled the subset."),
```

**(b) D-535 → OUT (Ruling 3).** Replace exactly this (it occurs once):

```python
        "D-535": (VERDICT_UNPLACED,
                  "Its verbatim reports that across three passages the real counted values overturn "
                  "no desk-simulation verdict, that margins moved by 1.5–3.5 in both directions, "
                  "and that one margin expectation was plainly wrong.",
                  "The published text reports a checking stage's outcome without stating any table "
                  "value or any rule about the four limbs, so it settles nothing either way."),
```

with exactly this:

```python
        "D-535": (VERDICT_OUT,
                  "Its verbatim reports that across three passages the real counted values overturn "
                  "no desk-simulation verdict, that margins moved by 1.5–3.5 in both directions, "
                  "and that one margin expectation was plainly wrong.",
                  "Ruled OUT 2026-09-05 from UNPLACED (Ruling 3 of the same record): it bears on the "
                  "checking stage's own outcome — a confirmation that the real counted tables "
                  "overturned no desk-simulation verdict — reporting no value and no rule; what it "
                  "discloses about the tables, that they are counted from data and checked, D-525 "
                  "(withheld) states in full."),
```

**Prove it.** Re-read both tuples with the file tools. Run
`python tools/audit/gen_derivation_boot_pack.py --check` and expect **exit 0**, all three built
subjects FROZEN at their recorded blobs (STOP condition 3 otherwise). Run
`python tools/audit/gen_withheld_family_reading.py --subject l2 --check` and expect **`FAIL: …
differs`, exit 1** — the table moved and the committed reading file has not yet been re-rendered;
that FAIL is the tool doing its job, not a stop, and Task 2 clears it. **Do not re-render here**: the
tool's prose is amended in Task 2 and the file is rendered once, from both changes.

Commit the generator alone:

```
audit(l2): Ruling 3 written back — D-453 IN, D-535 OUT; findings unchanged

Two verdict words and two reasons move; no finding string changes. Nothing is
withheld: WITHHELD carries no l2 entry.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the hash.

---

## Task 2 — the rendering tool's authored prose, and the re-rendered reading file: ONE commit

### (a) Five exact edits to `tools/audit/gen_withheld_family_reading.py`

Each `old` block below occurs exactly once in the tool as landed by the preceding batch (the writing
side applied the five to a copy of that file and confirmed the result compiles and renders on
synthetic data — see the fact check). Apply them in order. **A block not found byte for byte is
STOP condition 6.** Every string inside the new `"ruling"` block is the ruling record's content;
Task 2(c) checks that.

#### Edit A — the ruling block, appended inside SUBJECTS["l2"] after its `verdicts_authored` tuple

**Replace exactly this** (located by its text; it occurs once):

```python
        "verdicts_authored": (
            "by Claude Code on 2026-09-05 under `cc_instruction_l2_verdict_pass_2026_09_05.md` "
            "Task 2, at each entry's own published verbatim and plain restatement in the candidate "
            "list, in the fixed group order that dispatch names"),
    },
}
```

**with exactly this:**

```python
        "verdicts_authored": (
            "by Claude Code on 2026-09-05 under `cc_instruction_l2_verdict_pass_2026_09_05.md` "
            "Task 2, at each entry's own published verbatim and plain restatement in the candidate "
            "list, in the fixed group order that dispatch names"),
        # RULED.  Present only once the user has ruled the lists; a subject without this block
        # renders as a reading surface FOR RULING.  Every string below is the ruling record's own
        # content, cited to it, and the verdict table carries the ruled verdicts themselves.
        "ruling": {
            "record": "cowork_rulings_2026_09_05_l2_withheld_family_sitting.md",
            "date": "2026-09-05",
            "rulings": (
                "**Ruling 1 — LIST ONE stands as authored: all 110 IN entries are withheld** (the "
                "user's word: \"A\").",
                "**Ruling 2 — LIST TWO stands as authored: all 132 OUT entries are admitted** (the "
                "user's word: \"A\").",
                "**Ruling 3 — LIST THREE: D-453 is IN (withheld); D-535 is OUT (admitted)** (the user's "
                "words: \"Recommendation: D-453 IN, D-535 OUT.\").  The list is now empty; the two "
                "verdicts were written back to the table by "
                "`cc_instruction_l2_ruling_writeback_2026_09_05.md`, and the lists below are the "
                "ruled lists.",
            ),
            # The test as RULED: Ruling 1(a) accepted a fifth ground beside the four limbs.
            "test_note": (
                "**And, by Ruling 1(a) of the sitting record, a fifth ground the four limbs do not "
                "name:** an entry is also IN where it states the recorded HOW of what the charter's "
                "L2 block has this layer PUBLISH — the rivals with their mass — because withholding "
                "the recorded how costs the deriving session nothing it needs (the charter itself "
                "tells it to publish rivals) while admitting it would make the session's derived "
                "answer on that point indistinguishable from recall.  Nine entries are IN on that "
                "ground: D-027, D-099, D-326, D-331, D-380, D-381, D-425, D-510, D-511."),
            "notes": (
                "**Ruling 1(b).** D-005 and D-010 are IN while D-095 is OUT on a disclosure of the "
                "same shape — that the reading is produced by the joint estimator and not by the "
                "older chord-by-chord path.  Recorded as harmless: the framework's L2 block already "
                "calls the reading 'the one entangled decision', so none of the three discloses more "
                "than the charter does.",
                "**Ruling 1(c).** Thirty-two of the 110 IN entries carry the LEGACY mark in "
                "`DECISIONS.md` (the sitting's count at the index's marks).  They are withheld on the "
                "reasoning the pilot applied at D-317 and D-318: a project-specific former answer to "
                "the same question contaminates a blind session's recall as much as the current "
                "answer does.  The mark decided nothing; the reasoning is recorded so the scale of "
                "its application is visible.",
                "**Ruling 2.** D-495 is admitted as a rule about the cadence detector's own mechanics; "
                "the entries stating what the tonality does with a cadence vote (D-336, D-337, D-494) "
                "are withheld already.",
                "**Ruling 3.** D-453 is withheld because the same text settled the pilot's narrower "
                "question IN (Ruling 1 of `cowork_rulings_2026_08_22_withheld_family_sitting.md`) and "
                "cannot settle the superset question less; D-535 is admitted as the checking stage's "
                "own outcome, reporting no value and no rule, what it discloses about the tables "
                "being stated in full by the withheld D-525.",
            ),
        },
    },
}
```

#### Edit B — the STATUS banner, made conditional on the ruling block

**Replace exactly this** (located by its text; it occurs once):

```python
    w("> **STATUS: READING SURFACE — FOR RULING. NOTHING BELOW IS APPLIED.** Every verdict in this")
    w("> file is a PROPOSAL carried in `tools/audit/gen_derivation_boot_pack.py` → `VERDICTS[\"" + subject + "\"]`.")
    w("> No identity is withheld, no pack is rendered and no session is booted until you have ruled the")
    w("> lists (Ruling 81, §3cj of `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity")
    w("> is withheld that the user has not ruled*).")
    w(">")
```

**with exactly this:**

```python
    ruling = spec.get("ruling")
    if ruling:
        w(f"> **STATUS: RULED {ruling['date']} — the lists below are the RULED lists.** The ruling record is")
        w(f"> `{ruling['record']}`, three rulings, one per list.  Every verdict below is carried in")
        w("> `tools/audit/gen_derivation_boot_pack.py` → `VERDICTS[\"" + subject + "\"]` as ruled.  **No identity is")
        w("> withheld yet and no pack exists**: the withheld family is authored from LIST ONE only after L2's")
        w("> boot-list members are ruled, which is a separate decision (Ruling 81, §3cj of")
        w("> `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity is withheld that the user")
        w("> has not ruled*).")
    else:
        w("> **STATUS: READING SURFACE — FOR RULING. NOTHING BELOW IS APPLIED.** Every verdict in this")
        w("> file is a PROPOSAL carried in `tools/audit/gen_derivation_boot_pack.py` → `VERDICTS[\"" + subject + "\"]`.")
        w("> No identity is withheld, no pack is rendered and no session is booted until you have ruled the")
        w("> lists (Ruling 81, §3cj of `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity")
        w("> is withheld that the user has not ruled*).")
    w(">")
```

#### Edit C — §2, the test note after the four-limb sentence

**Replace exactly this** (located by its text; it occurs once):

```python
    w("only the second of these.  A verdict here is IN if the entry discloses the ruled answer to ANY of")
    w("the four, in whole or in part.")
    w("")
```

**with exactly this:**

```python
    w("only the second of these.  A verdict here is IN if the entry discloses the ruled answer to ANY of")
    w("the four, in whole or in part.")
    if ruling:
        w("")
        w(ruling["test_note"])
    w("")
```

#### Edit D — §5, the same test note after the three verdict definitions

**Replace exactly this** (located by its text; it occurs once):

```python
    w("- **UNPLACED** — the entry's own published text does not settle it.  The reason says what was read.")
    w("")
    w("**Default nothing:**```

**with exactly this:**

```python
    w("- **UNPLACED** — the entry's own published text does not settle it.  The reason says what was read.")
    if ruling:
        w("")
        w(ruling["test_note"])
    w("")
    w("**Default nothing:**```

#### Edit E — §7, "What was ruled" when the ruling block is present

**Replace exactly this** (located by its text; it occurs once):

```python
    w("## 7. What you are asked to rule")
    w("")
    w("**Three lists, one per turn, in the order above**, as the pilot's were ruled: LIST ONE (IN),")
    w("LIST TWO (OUT), LIST THREE (UNPLACED).  For each list you may take it as authored, or move named")
    w("entries between lists, or return a list for re-reading.  An UNPLACED entry must end IN or OUT")
    w("before any family is authored, and this file recommends neither for either.  Each ruling is")
    w("recorded in a ruling record, and the ruled lists are then written back to the generator's table")
    w("by a dispatch; **the withheld family itself is authored from the ruled IN list in a later act**,")
    w("together with L2's pack members, which are a separate ruling.")
    w("")
```

**with exactly this:**

```python
    if ruling:
        w("## 7. What was ruled")
        w("")
        w(f"**{ruling['date']}, one list per turn, in the order above.  The record is `{ruling['record']}`.**")
        w("")
        for i, r in enumerate(ruling["rulings"], 1):
            w(f"{i}. {r}")
        w("")
        w("**Recorded beside the rulings, at the user's acceptance of the sitting's stated caveats:**")
        w("")
        for n in ruling["notes"]:
            w(f"- {n}")
        w("")
        w("**The withheld family itself is authored from LIST ONE in a later act**, together with L2's")
        w("pack members, which are a separate ruling not yet taken.")
        w("")
    else:
        w("## 7. What you are asked to rule")
        w("")
        w("**Three lists, one per turn, in the order above**, as the pilot's were ruled: LIST ONE (IN),")
        w("LIST TWO (OUT), LIST THREE (UNPLACED).  For each list you may take it as authored, or move named")
        w("entries between lists, or return a list for re-reading.  An UNPLACED entry must end IN or OUT")
        w("before any family is authored, and this file recommends neither for either.  Each ruling is")
        w("recorded in a ruling record, and the ruled lists are then written back to the generator's table")
        w("by a dispatch; **the withheld family itself is authored from the ruled IN list in a later act**,")
        w("together with L2's pack members, which are a separate ruling.")
        w("")
```

### (b) Re-render, and check

```
cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l2
cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l2 --check
cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check
```

each redirected to scratch and read with the file tools. Expect `wrote … (<n> bytes)`; then `PASS: …
re-renders byte-identically`, exit 0; then the boot-pack generator's `--check` at **exit 0**. A
`STOP:` line from the rendering tool is STOP condition 7 — quote it in full.

**Read the re-rendered file with the file tools** and confirm, each with `Grep`:

- the banner's first line begins `> **STATUS: RULED 2026-09-05` and names the ruling record;
- §2 and §5 each carry the sentence beginning `**And, by Ruling 1(a) of the sitting record, a fifth
  ground` (two occurrences in the file);
- the LIST ONE heading carries `**111 entries.**`, LIST TWO `**133 entries.**`, LIST THREE
  `**0 entries.**` followed by the sentence `*The list is empty on this run.`;
- the summary table's last row reads `| **all** | | **244** | | | | **111** | **133** | **0** |`;
- the rows matching `^\| D-\d+ \|` number **244**;
- `D-453` appears in LIST ONE (between the LIST ONE and LIST TWO headings) and `D-535` in LIST TWO;
- `## 7. What was ruled` is present and `## 7. What you are asked to rule` is absent.

Any of these failing is STOP condition 7.

### (c) Check the ruling block against the record

With the file tools, open `cowork_rulings_2026_09_05_l2_withheld_family_sitting.md` (landed at Task
0) and confirm: the three ruling headings (§1–§3) say what the tool's three `rulings` strings say;
the user's words are `"A"`, `"A"`, `"Recommendation: D-453 IN, D-535 OUT."`; the nine identities in
`test_note` are the nine named at the record's Ruling 1(a); the count "thirty-two" and the three
sub-counts in the `notes` are the record's Ruling 1(c); D-495's treatment is the record's Ruling 2;
D-453's and D-535's grounds are the record's Ruling 3. **A disagreement between the tool's string and
the record is a finding about this dispatch: report it, follow the record, and declare the
correction.**

### (d) Commit the two paths together

`tools/audit/gen_withheld_family_reading.py` and
`ratification_surfaces/cowork_withheld_family_l2_reading.md`:

```
audit(l2): the reading file re-rendered as RULED — the test as ruled, the three rulings and their notes

The rendering tool gains an authored ruling block for l2, cited to the
sitting record; the banner, §2, §5 and §7 render from it. Nothing is
withheld: the family is authored only after the boot-list members are ruled.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the hash.

---

## Task 3 — prove nothing else moved

```
cd C:\s\MS && python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_ruling_writeback_task3.json
```

Redirect and read with the file tools. **Expect ZERO tracked modifications** and the Task 3 artifact
itself, which will not appear in its own listing. Anything under `tools/audit/derivation_boot_pack/`
or `tools/audit/derivation_boot_pack.json` appearing as modified is STOP condition 4.

Then the standing guard set:

```
cd C:\s\MS && python tools/audit/gen_guard_state.py --check
```

Report the exit code and the summary. **Expected: either exit 0, or drift (exit 1) that is NOT a
halt** — this batch changed the rendering tool and its artifact, and the guard runner records each
tool's stdout, so the committed `guard_state.json` may or may not re-derive; say which. **Do not
regenerate here**; the end state does. The failing set is expected to be **the ten inherited and no
other**, with `gen_withheld_family_reading.py --subject l2 --check` PASSING. Report the failing set
exactly, whatever it is, and adjust nothing to reach a number.

Commit the Task 3 enumeration artifact alone:

```
audit: Task 3 enumeration for the L2 ruling write-back batch

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the hash.

---

## Task 4 — the report

Write `cc_report_l2_ruling_writeback_2026_09_05.md` at the repository root, untracked, and commit it
in Task 5's commit. **Its two close-tip cells carry a named marker and no value until the hash has
been read at both ref files with the file tools** — two of the three preceding batches (the
candidate-list batch and the reading-file batch) each wrote an invented value there at first drafting
and caught it; write the marker first. It carries, in this order:

1. **The tip at boot and the tip at close**, each read at both ref files with the file tools, the
   close tip written in the batch's last commit on the standing convention.
2. **Task 0's result** — the commit hash and the enumeration showing zero tracked modifications.
3. **Task 1's result** — both tuples re-read and quoted, the boot-pack `--check` exit code, the
   rendering tool's expected FAIL, the commit hash.
4. **Task 2's result** — the five edits applied (each `old` found once), the render line with its
   byte count, both `--check` results, every Grep of 2(b) with what it returned, the record check of
   2(c) with any disagreement, the commit hash.
5. **Task 3's results**, including the guard summary, whether it was clean, drift or a halt, and
   the failing set exactly.
6. **Any STOP reached**, in full, with what was and was not done.
7. **A declared-departures section** — anything you did that this dispatch does not order, stated
   rather than absorbed, including any shell command that read a repository file (D-253) and the
   commit trailer if it differs.
8. **The writing side's own declared departure, relayed so it is on the record**: while preparing
   Task 2(a) the writing side ran a script in its own sandbox that READ a container copy of the
   landed `tools/audit/gen_withheld_family_reading.py` to confirm the five `old` blocks each occur
   once and that applying them reproduces its tested copy. That is a sandbox read of repository
   content through an interpreter — the shape D-253's 2026-08-08 widening names — and it is counted
   as that session's error 2 (error 1 being the `ls | grep` of an earlier dispatch). Nothing rests
   on it that Task 2(a)'s own STOP condition 6 does not re-establish at the tree.

**Recommend nothing. Put no question to the user.**

---

## Task 5 — `STATUS.md` and close

Add ONE dated entry at the head of `STATUS.md`'s entry list, in the established form, recording: the
three rulings of the sitting written back — D-453 IN and D-535 OUT in the table, the reading file
re-rendered as RULED with the test as ruled and the three rulings' notes; that nothing is withheld,
no pack rendered, no session booted, no `D-NNN` allocated and no open-items row touched; and the
guard-set result. **Per the OI-222 pointer convention this entry is a POINTER and no figure is
restated in it (D-431).**

Commit `STATUS.md` and the Task 4 report together:

```
docs(status): record the L2 ruling write-back — the reading file stands RULED

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Then write the close section into `cowork_away_returns.md` in the established form (a
descriptive heading naming this dispatch, no ordinal), and the end-state commit carrying the
regenerated guard artifact and, where this batch's own acts staled it, the read-size measurement —
both declared — in the single-commit form the preceding batches used, stated as such in the close
section's commit table. Expected end state: **77 guards run, TEN failing — the ten inherited and no
other.** Report the set exactly and adjust nothing to reach it.

---

## What this dispatch deliberately leaves to later acts, named so it is not lost

- **L2's boot-list members** — which documents and passages the deriving session reads at boot — the
  next decision surface, taken at Cowork on the pilot's pattern (`EXTRAS["l2"]` and the members).
- **`WITHHELD["l2"]`**, authored from the ruled LIST ONE only after that ruling; then the pack built,
  with the derived cross-reference additions (Ruling 84's bound: add, never overturn) and the leak
  check run — and at that batch **the `DATE` mechanism**, still owed.
- **The pluralisation "1 entries"** the rendering tool would print for a one-member list: a cosmetic
  defect the writing side noticed on synthetic data; no list of L2's has one member, and it is noted
  here rather than fixed in a batch whose scope is the ruling.

---

## The writing side's self-check, run before this dispatch was released (D-434)

1. *Principles.* #6 — the verdicts move in their one home, the table; the reading file is
   re-rendered, never hand-edited; the ruling block's strings are the record's content and the
   dispatch orders them checked against the record. #12 — both findings are kept byte for byte; the
   former verdict word is preserved in each new reason ("from UNPLACED"). #17f/D-431 — the counts
   111 / 133 / 0 are the ruled arithmetic of the record's §4 and are read back at the rendered file,
   not carried. #18/#19 — the five edits were established to occur once and to reproduce a compiled,
   synthetically rendered copy; the tree's cleanliness is declared an expectation.
2. *Conventions.* American English; plain words; *the verdict table*, *the reading file*, *the
   ruling record* described where first used; *measurement tool*, never *instrument*.
3. *The bars.* Two verdicts and no more; nothing withheld; no pack, no session; five edits and no
   more in the tool; the record untouched; no question anywhere.

### ★ THE FACT CHECK OF THIS DISPATCH, RUN AGAINST THE OBJECTS BEFORE IT WAS LANDED — TWO PASSES, THE SECOND SEARCHING FOR EACH CORRECTED TEXT

1. **The tip.** `5ba82c9ea7f84e2ad0d45fde4fc35258a9841e4f` at both ref files, read after the
   reading-file batch closed and again before this file was written.
2. **The two anchor tuples of Task 1.** Read at the generator as landed: the D-453 tuple at its
   group-A position and the D-535 tuple later in the same block, each quoted here byte for byte
   including the en dash in "1.5–3.5" and the em dashes in the findings.
3. **The five `old` blocks of Task 2(a).** Each confirmed to occur exactly once in the landed tool,
   and the five applied in order reproduce the writing side's amended copy, which compiles and
   renders on synthetic data in both branches (with and without the ruling block): banner RULED, the
   test note in §2 and §5, §7 "What was ruled", LIST THREE empty with its sentence, `--check` PASS
   after render.
4. **The ruling block's content against the record.** The three rulings, the user's three verbatim
   words, the nine identities of Ruling 1(a), the count and sub-counts of Ruling 1(c), the D-495
   ground of Ruling 2 and the two grounds of Ruling 3 were each read at the record this side wrote
   earlier this session and compared string by string.
5. **The counts.** 110 + 1 = 111 IN, 132 + 1 = 133 OUT, 0 UNPLACED, total 244 — the record's §4.
6. **A correction made on the second pass.** The dispatch's own name is cited inside the tool's
   Ruling 3 string (`cc_instruction_l2_ruling_writeback_2026_09_05.md`); the file was first saved
   under that name and the string checked against it, so the tool does not name a dispatch that does
   not exist.
7. **A second correction made on the second pass.** Task 4 first said "the two preceding batches"
   invented a close-tip hash; read at the three reports, the two were the candidate-list batch
   (disclosed in chat, written into the record by the verdict-pass batch) and the reading-file batch
   (disclosed in its own report §8(vii)) — the verdict-pass batch between them did not. Corrected to
   "two of the three preceding batches", and the phrase was searched for elsewhere in this file.
8. **The Task 1 anchor lines.** Each of the twelve lines of the two `old` tuples was searched for
   as a whole anchored line in the generator with the file tools and found — twelve matches for
   twelve lines.
