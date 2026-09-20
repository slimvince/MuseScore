# CC INSTRUCTION — THE FROZEN SUBJECT'S MANIFEST RECORD DESCRIBES ITS DIRECTORY (2026-09-20)

**This dispatch executes two user rulings taken 2026-09-20 and recorded at
`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty.md` §3 and §4.** Read that
entry's §2, §3 and §4 before Task 1. Nothing in this dispatch restates a measured figure; every
figure it names is a figure you are ordered to measure, or one you read at the object named beside
it.

**RULING 1 (the user's words: "C it is then.")** — for a subject in the generator's `FROZEN` table,
the manifest record DESCRIBES THE PACK DIRECTORY, not a re-render of today's sources.

**RULING 2 (the user's words: "I'll go with your recommendation.")** — the drift stays, PRINTED and
UNCOMPARED: the figures a re-render would produce go on being computed exactly as they are computed
now, are printed as ordinary lines of `--check`'s output, and are excluded from what the check
compares, so they never set the exit code.

---

## 0. What this batch is, in plain words

`tools/audit/gen_derivation_boot_pack.py` renders a *derivation boot pack* — one directory per
subject, holding the curated set of documents a later session is given to read. Three subjects
exist and all three are SPENT: their sessions have run, so their directories are FROZEN, pinned
file by file at a git blob hash under D-646, and the generator writes nothing into them.

The generator also writes a MANIFEST, `tools/audit/derivation_boot_pack.json` — a record file
describing those directories, and part of none of them. Today the generator builds every subject in
full on every run and writes the manifest from that build, so a frozen subject's manifest record
carries figures measured on the sources AS THEY STAND TODAY rather than on the files the freeze
pins. When a source moves, the manifest stops re-deriving, `--check` prints a drift line and exits
1 — and that red says nothing at all about any pack.

This batch makes a frozen subject's measured fields describe its directory, and turns the
today's-sources figures into printed output that sets no exit code.

**IT IS NOT A REPAIR OF THE PACKS, AND IT TOUCHES NO PACK.** No file under
`tools/audit/derivation_boot_pack/` is read for content, written, moved or renamed by any task here.
The freeze's own hash STOP is untouched, still called, and still a STOP.

---

## 1. Bars, and the footprint assumption

**B1 — ONE tool source is edited: `tools/audit/gen_derivation_boot_pack.py`.** The single named
exception is the forward bound's own re-aiming of `tools/audit/gen_status_batch_bound.py` at the
close, which Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md`
requires of every close. No other file under `tools/` has its source edited.

**B2 — NOTHING under `tools/audit/derivation_boot_pack/` is written, deleted, renamed or moved**,
and no file in any of those directories is opened for editing. Task 2 reads those files' LENGTHS
through the generator's own code and nothing else.

**B3 — no `src/` file, no build, no test, no golden, no score corpus, nothing under
`tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis.**

**B4 — no governing document is amended.** Not `CLAUDE.md`, not `ARCHITECTURE.md`, not
`FRAMEWORK.md`, not `DECISIONS.md`, not `OPEN_ITEMS.md`. No open-items row is created, flipped or
discarded. No decisions-register entry is written and no `D-NNN` is allocated. `STATUS.md` and
`STATUS_ARCHIVE.md` are written by the close alone, in the close's own two acts.

**B5 — no paper is opened, no extract is edited, no reading-pass file is touched.** The three
reading-pass extracts entry 220 §2 names as the sources that moved are NOT to be inspected,
reverted, or brought back into agreement with anything. Their having moved is the condition this
batch makes harmless, not a defect to repair.

**THE FOOTPRINT ASSUMPTION, written from the enumerated paths this batch's own tasks touch — not
wider than they are.** This batch's own orders modify exactly these existing files:
`tools/audit/gen_derivation_boot_pack.py` (Task 1), `tools/audit/derivation_boot_pack.json`
(Task 3), and — in the close alone — `STATUS.md`, `STATUS_ARCHIVE.md`,
`tools/audit/gen_status_batch_bound.py` and `tools/audit/status_batch_bound.json`. It creates
exactly one new file, your own report. Every other path this batch commits is a file that was
ALREADY uncommitted on disk when the batch opened and is committed unchanged; §6 names them and
orders each one's unchangedness proved rather than assumed.

**IF ANY BAR ABOVE CONTRADICTS A TASK BELOW, STOP AND REPORT IT.** Do not resolve it yourself and
do not proceed on the reading that lets the task run.

---

## 2. Task 0 — pin this dispatch and its subject, and capture the start state

**0(a).** Record the current commit of every ref you can read, and run the guard set ONCE as the
OPENING CAPTURE, exactly as the previous close ran it. Save the capture to a file OUTSIDE the
repository working tree and name that file in your report. **No condition in this dispatch is
written on any guard's printed OUTPUT TEXT — every condition is on a guard's VERDICT.** That is the
user's ruling recorded at handoff entry 220 §4 item 4, and its ground is this batch's own subject:
the line this batch adds to `--check`'s output moves whenever a source moves, so a condition over
output text would stop a batch for a green guard.

**0(b).** Pin this dispatch and the file Task 1 edits to git blobs:

```
git hash-object -w records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_2026_09_20.md
git hash-object -w tools/audit/gen_derivation_boot_pack.py
```

Record both hashes in your report. **Take every later re-read of this dispatch from
`git cat-file blob <its hash>` and never from the working tree.** The writing side has declared, on
this dispatch's face, that it will not touch this file or `tools/audit/gen_derivation_boot_pack.py`
while this batch runs.

**0(c).** Before any edit, check the working tree for mid-write corruption:

```
git status
git diff --stat
```

For any file carrying a real content diff, read its last bytes. A trailing NUL byte or a
mid-token truncation is a STOP: report it and make no edit. **Expect `tools/audit/claude_md_finer_archive.json`
to appear as modified with no cause established by anybody** — it is held back by §6 and is not to
be staged, reverted, or investigated by this batch.

**0(d).** Confirm at the file that `tools/audit/gen_derivation_boot_pack.py` carries, verbatim, each
of the four passages Task 1 replaces. If any one of them does not match character for character,
STOP and report which, with what the file actually carries. Do not fuzzy-match and do not adapt an
edit to a passage that has moved.

---

## 3. Task 1 — the four edits, each given verbatim

Every edit below is EXACT. Replace the OLD block with the NEW block, once, and make no other change
to the file.

### 1(a) — `build()` returns what it displaced

**OLD** (the signature line):

```python
def build() -> tuple[dict, dict[str, dict[str, str]]]:
```

**NEW:**

```python
def build() -> tuple[dict, dict[str, dict[str, str]], list[dict]]:
```

**OLD** (the subject loop):

```python
    subjects, packs = {}, {}
    for subject in sorted(WITHHELD):
        rec, files = build_subject(subject, sort["entries"], backbone)
        if subject in FROZEN:
            rec["★_FROZEN"] = frozen_block(subject)
        subjects[subject] = rec
        packs[subject] = files
```

**NEW:**

```python
    # EVERY SUBJECT IS STILL BUILT IN FULL, frozen or not, and that is deliberate: this tool's own
    # STOPs — an anchor no longer found exactly once, a withheld passage that no longer matches, a
    # verdict left unpaired — run only because the build runs.  Stopping the build for a spent
    # subject would leave this tool checking almost nothing, all three subjects being spent.  What
    # changes for a FROZEN subject is what the manifest KEEPS of that build (Ruling 1, 2026-09-20).
    subjects, packs, displaced = {}, {}, []
    for subject in sorted(WITHHELD):
        rec, files = build_subject(subject, sort["entries"], backbone)
        if subject in FROZEN:
            rec["★_FROZEN"] = frozen_block(subject)
            displaced.extend(frozen_from_disk(subject, rec))
        subjects[subject] = rec
        packs[subject] = files
```

**OLD** (the return, the last line of `build`):

```python
    return manifest, packs
```

**NEW:**

```python
    return manifest, packs, displaced
```

### 1(b) — the new function, and the `frozen_block` prose it makes false

Insert the function below IMMEDIATELY AFTER `frozen_block` ends and BEFORE the line
`def write_all(manifest: dict, packs: dict, only: str | None) -> None:`, separated from each
neighbour by two blank lines:

```python
def frozen_from_disk(subject: str, rec: dict) -> list[dict]:
    """Re-point a FROZEN subject's MEASURED fields at its pack directory, and return what that displaced.

    Ruling 1 of the sitting recorded at handoff entry 220 §3: for a frozen subject the manifest
    DESCRIBES THE DIRECTORY, never a re-render.  The subject goes on being BUILT — every STOP this
    tool carries runs over the live sources for every subject — and what changes is only what the
    manifest KEEPS of that build.

    What is re-measured, what is dropped, and why the two differ:

      * `characters` on a member record IS recoverable from the directory, the pack holding exactly
        one file per member, so it is MEASURED AT THAT FILE and keeps its name.
      * a per-SPAN `lines_rendered`, a per-PART `characters`, and a filter's record of the text it
        removed are NOT recoverable from the directory: the pack holds the joined file and not its
        parts, so recovering them would mean re-rendering, which is the act this ruling removed.
        They are DROPPED rather than carried, because a figure describing what WOULD be rendered
        describes nothing this directory holds.  The AUTHORED structure beside them — which source,
        which anchors, what was cut and why — stays: it is this tool's own constant.
      * members (5) and (6) count what today's inputs yield, so their counts are dropped on that
        same ground.

    Returns the displaced per-file figures.  Ruling 2 keeps them: they are NOT written into the
    manifest, and `check_all` PRINTS them, where they set no exit code.
    """
    d = pack_dir(subject)
    displaced: list[dict] = []
    for r in rec["the_members_as_rendered"]:
        p = os.path.join(d, r["file"])
        if not os.path.exists(p):
            raise Stop(f"{subject} is FROZEN and its directory does not hold {r['file']}, which "
                       f"this tool renders for it — the manifest cannot describe a file that is "
                       f"not there")
        # `newline=""` so that no line ending is translated on the way in: `write_all` wrote these
        # files with `newline=""` too, so this is the length of the file AS IT STANDS, which is
        # what "the directory holds" has to mean if the figure is to be checkable from outside.
        in_the_directory = len(open(p, encoding="utf-8", newline="").read())
        displaced.append({
            "subject": subject,
            "file": r["file"],
            "characters_in_the_directory": in_the_directory,
            "characters_a_re_render_would_produce": r["characters"],
        })
        r["characters"] = in_the_directory
        for s in r.get("spans", []):
            s.pop("lines_rendered", None)
        for part in r.get("parts", []):
            part.pop("characters", None)
            for s in part.get("spans", []):
                s.pop("lines_rendered", None)
            for f in part.get("filters_applied", []):
                for k in ("the_text_removed", "characters_removed", "heading", "closes_before"):
                    f.pop(k, None)
        for k in ("entries_rendered", "rows_rendered", "columns_kept"):
            r.pop(k, None)
        r["★_where_this_record's_measures_COME_FROM"] = (
            "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at "
            "the frozen file itself and never at a re-render. The per-span, per-part and "
            "per-filter measures are NOT CARRIED AT ALL: the directory holds the joined file and "
            "not its parts, so they could come only from a re-render, and a figure describing what "
            "WOULD be rendered describes nothing this pack holds. The sources, the anchors, the "
            "filters and their reasons stay — they are this tool's own authored constants.")
    rec["counted"]["files_in_the_pack"] = len(
        [n for n in os.listdir(d) if os.path.isfile(os.path.join(d, n))])
    rec["counted"]["★_which_of_these_counts_describe_the_DIRECTORY"] = (
        "`files_in_the_pack` is COUNTED IN THE PACK DIRECTORY. The other counts here are over this "
        "tool's authored tables and over the candidate derivation against today's inputs; they are "
        "NOT measurements of the frozen files and are not offered as any.")
    return displaced
```

Then, inside `frozen_block`, replace the second prose field — which this edit makes false, and
which is therefore superseded with its former wording preserved in place (#12).

**OLD:**

```python
        "★_so_read_the_member_records_below_with_this_in_mind": (
            "They are built from the sources AS THEY STAND TODAY, because every subject is built "
            "the same way and the ruling keeps this subject's entry. Where a member's sources "
            "have grown since the pack was rendered, the record's counts describe what WOULD be "
            "rendered and NOT what the frozen directory holds. THE DIGESTS ARE THE AUTHORITY ON "
            "WHAT THE DIRECTORY HOLDS."),
```

**NEW:**

```python
        "★_so_read_the_member_records_below_with_this_in_mind": (
            "Their MEASURED fields describe THIS DIRECTORY. `characters` on each member record is "
            "the length of the file the freeze pins, measured at that file. The per-span, "
            "per-part and per-filter measures are not carried at all, the directory holding the "
            "joined file and not its parts. What stands beside them — which source, which "
            "anchors, what was cut and why — is this tool's own authored constant, not a "
            "measurement. THE DIGESTS REMAIN THE AUTHORITY ON WHAT THE DIRECTORY HOLDS."),
        "★_the_former_wording_of_the_clause_above_PRESERVED_12": (
            "SUPERSEDED 2026-09-20 by Ruling 1 of the sitting recorded at handoff entry 220 §3, "
            "which made it false of this record. IT READ: \"They are built from the sources AS "
            "THEY STAND TODAY, because every subject is built the same way and the ruling keeps "
            "this subject's entry. Where a member's sources have grown since the pack was "
            "rendered, the record's counts describe what WOULD be rendered and NOT what the "
            "frozen directory holds. THE DIGESTS ARE THE AUTHORITY ON WHAT THE DIRECTORY "
            "HOLDS.\""),
```

### 1(c) — `check_all` prints the drift and never compares it; `main` passes it

**OLD:**

```python
def check_all(manifest: dict, packs: dict) -> int:
    drift: list[str] = []
    frozen_checked: dict[str, dict] = {}
```

**NEW:**

```python
def check_all(manifest: dict, packs: dict, displaced: list[dict]) -> int:
    # RULING 2 of the sitting recorded at handoff entry 220 §3: the drift a frozen subject's
    # sources have accumulated is PRINTED and never COMPARED.  It joins no drift list, it reaches
    # no exit code, and NO BATCH CONDITION MAY BE WRITTEN ON THIS TEXT — a condition over this
    # guard belongs on its VERDICT, because these lines move whenever a source moves and an
    # equality over them would stop a batch for a green guard (entry 220 §4 item 4).
    #
    # THE SCOPE OF WHAT IS PRINTED, stated because a scope that is not stated reads as total: one
    # line per frozen pack FILE whose re-render length differs from the length on disk.  The
    # per-span, per-part and per-filter figures the manifest no longer carries are computed on
    # every run, by the ordinary build, and are not printed — printing every one of them would
    # bury the file-level difference this line exists to show.
    moved = [m for m in displaced
             if m["characters_in_the_directory"] != m["characters_a_re_render_would_produce"]]
    print(f"FROZEN SOURCES: {len(moved)} of {len(displaced)} frozen pack file(s) would render at a "
          f"different length from the sources as they stand today. NOT COMPARED; sets no exit "
          f"code.")
    for m in sorted(moved, key=lambda x: (x["subject"], x["file"])):
        print(f"  - {m['subject']}/{m['file']}: the directory holds "
              f"{m['characters_in_the_directory']} characters; today's sources would render "
              f"{m['characters_a_re_render_would_produce']}")
    drift: list[str] = []
    frozen_checked: dict[str, dict] = {}
```

**OLD** (in `main`):

```python
    manifest, packs = build()
```

**NEW:**

```python
    manifest, packs, displaced = build()
```

**OLD** (in `main`):

```python
        return check_all(manifest, packs)
```

**NEW:**

```python
        return check_all(manifest, packs, displaced)
```

### 1(d) — the tool's own account of itself, at the two places this edit makes incomplete

**OLD** (the header block, the paragraph headed `WHAT THE FREEZE DOES.`):

```
  WHAT THE FREEZE DOES.  `write_all` writes NOTHING into a frozen subject's directory.
  `check_all` verifies that subject against its RECORDED DIGESTS instead of against a re-render,
  in both directions -- every recorded file present, every present file recorded, every digest
  equal -- and any mismatch is a STOP rather than a drift line, because a moved frozen file is
  not staleness to be regenerated away.  The manifest CONTINUES TO CARRY both subjects' entries.
```

**NEW:**

```
  WHAT THE FREEZE DOES.  `write_all` writes NOTHING into a frozen subject's directory.
  `check_all` verifies that subject against its RECORDED DIGESTS instead of against a re-render,
  in both directions -- every recorded file present, every present file recorded, every digest
  equal -- and any mismatch is a STOP rather than a drift line, because a moved frozen file is
  not staleness to be regenerated away.  The manifest CONTINUES TO CARRY EVERY FROZEN SUBJECT'S
  ENTRY.
  ★ AMENDED 2026-09-20, FORMER WORDING PRESERVED (#12): that last sentence read "The manifest
  CONTINUES TO CARRY both subjects' entries", which was written when two subjects were frozen and
  went stale when `l0-l1` was frozen on 2026-09-04.

  AND SINCE 2026-09-20 THE MANIFEST'S RECORD OF A FROZEN SUBJECT DESCRIBES ITS DIRECTORY (user,
  Ruling 1 of the sitting recorded at handoff entry 220 §3).  Every subject is still BUILT, so
  every STOP above still runs for every subject; what changes is what the manifest KEEPS of a
  frozen subject's build.  `frozen_from_disk` re-measures `characters` at the frozen file itself
  and `files_in_the_pack` by counting the directory, and DROPS the per-span, per-part and
  per-filter measures, which the directory cannot supply without a re-render.  The figures a
  re-render WOULD produce are not thrown away: Ruling 2 of the same sitting keeps them PRINTED at
  `--check` and EXCLUDED FROM THE COMPARISON, so they set no exit code, and no batch condition may
  be written on that printed text -- a condition over this guard is written on its VERDICT.
```

**OLD** (STOP 12 in the header list):

```
 12. a FROZEN subject whose directory does not hold EXACTLY the recorded files, or one of whose
     files does not carry its recorded digest, STOPS it -- in both directions, so neither an
     added file nor a removed one passes; a FROZEN entry naming a subject this tool does not
     build STOPS it; and a freeze record missing its finding, its date or its reason STOPS it,
     on the same demand every other authored input here answers.
```

**NEW:**

```
 12. a FROZEN subject whose directory does not hold EXACTLY the recorded files, or one of whose
     files does not carry its recorded digest, STOPS it -- in both directions, so neither an
     added file nor a removed one passes; a FROZEN entry naming a subject this tool does not
     build STOPS it; a freeze record missing its finding, its date or its reason STOPS it, on the
     same demand every other authored input here answers; and a FROZEN subject whose directory
     does not hold a file this tool renders for it STOPS it, because the manifest cannot describe
     a file that is not there.
```

**OLD** (the manifest's own `what_is_DERIVED` list, its last element):

```python
            "every rendered file, byte for byte, and every count",
```

**NEW:**

```python
            "every rendered file, byte for byte, and every count",
            "AND, FOR A FROZEN SUBJECT, ITS MEASURED FIELDS ARE MEASURED AT THE PACK DIRECTORY "
            "INSTEAD (Ruling 1 of the sitting recorded at handoff entry 220 §3): `characters` at "
            "the frozen file itself, `files_in_the_pack` by counting that directory, and the "
            "per-span, per-part and per-filter measures not carried at all. The figures a "
            "re-render would produce are PRINTED at `--check` and compared against nothing.",
```

**OLD** (the manifest's own `the_STOPS` list, its last element):

```python
            "a FROZEN subject whose directory does not hold EXACTLY the recorded files, or one "
            "of whose files does not carry its recorded blob digest — checked in both "
            "directions; a FROZEN entry naming a subject this tool does not build; and a freeze "
            "record missing its finding, its date or its reason",
```

**NEW:**

```python
            "a FROZEN subject whose directory does not hold EXACTLY the recorded files, or one "
            "of whose files does not carry its recorded blob digest — checked in both "
            "directions; a FROZEN entry naming a subject this tool does not build; a freeze "
            "record missing its finding, its date or its reason; and a FROZEN subject whose "
            "directory does not hold a file this tool renders for it",
```

---

## 4. Task 2 — prove the edit before it writes anything

Run, and report each result verbatim:

```
python tools/audit/gen_derivation_boot_pack.py --check
```

**EXPECTED AT THIS POINT: exit 1, and a drift list whose ONLY member is
`derivation_boot_pack.json does not re-derive`.** That is the manifest on disk still being the
pre-change one; Task 3 regenerates it. The run must ALSO print, before the drift verdict, the
`FROZEN SOURCES:` line and one line per frozen pack file whose lengths differ.

**FOUR STOP CONDITIONS AT THIS STEP, each ending the batch where it fires:**

1. **A `STOP:` line of any kind.** The edit has broken a check that was passing; report the STOP
   text whole and revert `tools/audit/gen_derivation_boot_pack.py` to the blob pinned at Task 0(b).
2. **A traceback of any kind**, `KeyError` above all — report it whole and revert as above.
3. **Any drift line naming a subject or a pack file** rather than the manifest alone. The freeze's
   own verification must not have started reporting drift; report the line whole and revert.
4. **The `FROZEN SOURCES:` line absent.** It must print on every `--check` run, whatever it counts.

   And **report, without treating it as a stop, if that line counts ZERO files.** Entry 220 §2
   establishes at the objects that three of member (8)'s five sources have grown since the manifest
   was last written, and the `FROZEN` table's own findings record members (2) and (4) of the other
   two subjects as stale, so a zero would be a surprise with two possible causes and this dispatch
   does not decide between them: either the new code is measuring the same quantity twice, or the
   lengths happen to coincide despite the sources having moved. Report the zero and the full output
   and let the user read it.

**Do not adapt the code to make this step pass.** If it does not pass as written, the edit is wrong
or the file has moved under it, and either is a STOP for the user rather than a repair for you.

---

## 5. Task 3 — regenerate the manifest ONCE, then prove the check is green and stable

**3(a).** Regenerate:

```
python tools/audit/gen_derivation_boot_pack.py
```

Report its printed summary verbatim. **This command writes the manifest and, by the freeze, writes
nothing into any pack directory** — `write_all` skips every subject in `FROZEN` before it creates a
directory or opens a file, and all three subjects are frozen. Prove that rather than assume it:
after the run, confirm with `git status` that `tools/audit/derivation_boot_pack.json` is the only
path under `tools/audit/` that this command modified, and that NO path under
`tools/audit/derivation_boot_pack/` appears as modified, added or deleted. **A pack file appearing
in that output is a STOP** — report it and make no commit.

**3(b).** Run the check twice, with nothing touched between the two runs:

```
python tools/audit/gen_derivation_boot_pack.py --check
python tools/audit/gen_derivation_boot_pack.py --check
```

**EXPECTED, BOTH TIMES: exit 0**, the line `the derivation boot pack re-derives`, one
`FROZEN — N file(s) at their recorded blobs` line per frozen subject, and the `FROZEN SOURCES:`
lines. **Report the exit code and the full output of both runs.** The second run is the stability
test: if the two outputs differ in any character, or the exit codes differ, that is a STOP — report
both outputs whole.

**3(c) — the one measurement this batch is asked for, beyond its own result.** Ruling 1's stated
intent is that a frozen subject's manifest record comes to depend on this tool's own authored
constants and on the pack files alone. This batch does not claim that reached. Measure the residue
mechanically and REPORT IT; **change nothing on the strength of it.**

For the subject `l0-l1`, list every TOP-LEVEL key of its record in the regenerated
`tools/audit/derivation_boot_pack.json`, and for each key name the code site — function and line —
in `tools/audit/gen_derivation_boot_pack.py` that sets it, and which of these three its value is
built from:

- **(i) this tool's own authored constants** (`MEMBERS`, `EXTRAS`, `WITHHELD`, `CRITERION`,
  `VERDICTS`, `FROZEN`, `DATE`, `READ_ME`, `DEFECT_TABLE_HEADER`, `DEFECT_COLUMNS_KEPT`);
- **(ii) the pack directory** `tools/audit/derivation_boot_pack/l0-l1/`;
- **(iii) an input outside both** — naming the input: a member source file,
  `tools/audit/rulings_sort_classification.json`, `tools/audit/decisions/backbone_decisions.json`,
  or `DEFECT_TYPES.md`.

Report it as a table, one row per top-level key. **This is an enumeration of code sites, not a
judgment about whether any of them should change.** Where a key's value is built from more than one
of the three, say so and name each. Where you cannot place a key from the code, write CANNOT PLACE
and say what you read; do not guess.

---

## 6. The close

**6(a) — the guard set, as a NON-REGRESSION test written on the VERDICT.** Run the guard set as the
CLOSING CAPTURE and compare it against the opening capture from Task 0(a), **verdict by verdict**:

> **THE CONDITION: no guard whose VERDICT was PASS at the opening capture may carry any other
> verdict at the close.** A guard that moves FAIL → PASS is ALLOWED and is REPORTED. A guard that
> was FAIL at both is reported and is not a stop. **No condition is written on any guard's printed
> OUTPUT TEXT, on any count in that text, or on the number of failing guards** — this batch's own
> change adds a line to one guard's output that moves whenever a source moves, and an equality over
> output would stop this batch for a green guard.

`tools/audit/gen_derivation_boot_pack.py --check` is expected to move FAIL → PASS. That is this
batch's own ordered consequence and is reported, not stopped on.

**If a PASS becomes anything else, STOP: commit nothing, and report which guard, both verdicts and
both outputs whole.**

**6(b) — the commit, BY EXPLICIT PATH.** Never a directory pathspec. The candidate set is exactly:

1. `tools/audit/gen_derivation_boot_pack.py` — modified by Task 1.
2. `tools/audit/derivation_boot_pack.json` — regenerated by Task 3(a).
3. `records/cc/instructions/cc_instruction_boot_pack_frozen_manifest_2026_09_20.md` — this
   dispatch, new.
4. `records/cc/reports/cc_report_boot_pack_frozen_manifest_2026_09_20.md` — your report, new.
5. `records/cc/reports/cc_report_backup_third_close_2026_09_20.md` — uncommitted since the third
   backup's close.
6. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nineteen.md` — uncommitted.
7. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty.md` — uncommitted.
8. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twenty_one.md` — the next entry, if
   the writing side has landed it by close time; if that path does not exist, say so and commit the
   other members. **Do not wait for it.**
9. `STATUS.md` and `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py` and
   `tools/audit/status_batch_bound.json` — written by 6(c) and 6(d) below.

**Before staging, establish the set rather than asserting it.** For each of members 5, 6 and 7 —
the three this batch does not itself write — prove that the file on disk is unchanged from what the
writing side landed: read its size at a directory listing and its last non-empty line, and report
both. **A last line that is not ordinary text, or a NUL byte at the tail, is a STOP.** Then stage,
and prove the staged set is EXACTLY the candidate set and nothing else before committing.

**HELD BACK, NAMED SO IT IS NOT SWEPT IN:** `tools/audit/claude_md_finer_archive.json`. It is
modified on disk, no side has established why, and establishing that is not this batch's work.
Confirm in your report that it is absent from the staged set. **Anything else `git status` reports
as modified or untracked that is not in the candidate set above is REPORTED AND LEFT**, not staged
and not investigated.

**6(c) — `STATUS.md`.** Write ONE new dated entry for this batch, as a POINTER under the OI-222
convention: what the batch did, and that the whole of it is your report. **Restate no figure**
(D-431). Leave every existing entry unchanged.

**6(d) — the forward bound.** Re-aim `tools/audit/gen_status_batch_bound.py` at THIS batch's own
base commit and run its `--apply`, so that the previous batch's entries move to
`STATUS_ARCHIVE.md` in the same act that writes this batch's own entry. Then run its `--check` and
report the result. This is the single exception B1 names.

**6(e) — push.** After the commit, push every branch that received it to the central remote. Use
the remote name the repository is configured with — check `git remote -v`. **If a push fails, for
any reason, REPORT IT; do not skip it silently, and never pass `--force`.** Name the pushed branches
in your report.

---

## 7. The report

Write `records/cc/reports/cc_report_boot_pack_frozen_manifest_2026_09_20.md`, carrying:

1. Both hashes from Task 0(b), and the path of the opening capture file.
2. The `git status` and `git diff --stat` of Task 0(c), and what you found at any tail you read.
3. Confirmation, per passage, that each of Task 1's OLD blocks matched character for character
   before it was replaced — and, for each, the number of occurrences found.
4. Task 2's full output and exit code.
5. Task 3(a)'s printed summary, and the `git status` proving no pack file moved.
6. Task 3(b)'s two outputs and two exit codes, and whether they are identical.
7. Task 3(c)'s table.
8. The guard comparison of 6(a), **by verdict**: every guard whose verdict moved, in which
   direction, and the statement that no PASS became anything else.
9. The established set of 6(b): per held-over file, its size at the listing and its last non-empty
   line; the staged set proved to be exactly the candidate set; and the confirmation that
   `tools/audit/claude_md_finer_archive.json` is not in it.
10. The commit hash, the forward bound's `--check` result, and the pushed branches.
11. **What you did NOT do**, named rather than counted — and in particular, that no pack file was
    read for content, written, or moved, and that no reading-pass extract was opened.

**Report anything you could not do, and why, rather than working around it.** If a task's expected
result does not appear, stop at that task and report; do not continue to the next one.
