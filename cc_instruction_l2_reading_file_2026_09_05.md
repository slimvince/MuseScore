# CC INSTRUCTION — render L2's withheld-family READING FILE from the verdict table, by a generator enrolled in the guard set; two small repairs ride at the front (2026-09-05)

> **STATUS: DISPATCH.** Written by the Cowork writing side, 2026-09-05, at tip
> `8457c97445ff9a6c506fe999128681b80969e9ba` (`refs/heads/master` and `refs/remotes/origin/master`
> both at that hash, read at the two ref files with the file tools before this file was written).
> **Nothing was running when this was written and no other dispatch is out.**
>
> **Where this sits.** The verdict pass is finished: `tools/audit/gen_derivation_boot_pack.py` →
> `VERDICTS["l2"]` carries one proposal — IN, OUT or UNPLACED, with its finding and its reason — for
> each of L2's 244 candidates (`cc_report_l2_verdict_pass_2026_09_05.md`). Ruling 81 (§3cj of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md`) rules that the lists go to the user one
> per turn and that no identity is withheld he has not ruled. **The reading file is the surface
> those lists go to him on.** This dispatch produces it.
>
> **Why a generator and not a hand-written file.** The pilot's reading file
> (`ratification_surfaces/cowork_withheld_family_harmony_boundary_reading.md`) was hand-authored
> from a 75-row table. L2's table is 244 rows. A hand copy of 244 findings is a second copy of the
> verdict text that can drift from the table it copies (#6), and every count in it would be
> transcribed (D-431). So the file is RENDERED from the generator's own table and the published
> candidate list by a small tool with a `--check`, enrolled in the guard set in the act that creates
> it (the standing new-tool rule, as the L0/L1 population tool was enrolled on 2026-09-02).
>
> **The one-sentence statement of the whole job:** regenerate two artifacts the OI-378 row staled
> and prove only positions moved, append one dated note to OI-378's detail file, then create the
> reading-file generator, enrol it, render L2's reading file, and change nothing else.

---

## Read first — the vocabulary this dispatch uses, in plain words

- **The reading file** is the document the user reads to rule the three lists: for each of the
  244 candidates its identity, its register group, its title, the finding (what the entry's own
  text says) and the reason, arranged as LIST ONE (IN), LIST TWO (OUT), LIST THREE (UNPLACED),
  with the subject, the criterion, the test and what he is asked to rule stated around them.
- **A verdict is a proposal.** Nothing in this batch withholds anything, and the reading file says
  so on itself.
- **The guard set** is `tools/audit/gen_guard_state.py`: it runs every `tools/audit/*.py` that
  carries a `--check`, `--verify` or `--establish` mode, and HALTS on one that has no authored
  invocation in its `AUTHORED` list. That is why the new tool is enrolled in the same commit that
  creates it.
- **A stale artifact** is a generated file whose generator's `--check` says the file no longer
  matches what a fresh run produces. Two are stale because the OI-378 row, inserted at line 278 of
  `OPEN_ITEMS.md` by the last batch, shifted every recorded line position below it by one.

---

## What this dispatch may NOT do — read before Task 0

- **Author no verdict, change no verdict.** `VERDICTS` is read by the new tool and not written by
  anything. Not one tuple moves.
- **Withhold nothing.** `WITHHELD` is not touched; no `l2` key is added to it.
- **Render no pack and boot no session.** No file under `tools/audit/derivation_boot_pack/` is
  created, edited, deleted or read for writing, and `tools/audit/derivation_boot_pack.json` is not
  regenerated. `write_all` is never reached; the only mode of that generator you run is `--check`.
- **Do not touch `EXTRAS`, `FROZEN`, the `CRITERION` table, `KEYWORDS`, `L2_KEYWORDS` or `DATE`.**
- **Do not edit `gen_phase3_gate_partition.py` or `gen_l0_l1_outgoing_population.py`.** Task 1(a)
  RUNS them to regenerate their artifacts; it does not re-aim an `expected_line` or change a line
  of either tool. A tool edit is a separate act.
- **Do not edit the `OPEN_ITEMS.md` INDEX.** Task 1(b) appends a dated note to a DETAIL file, which
  that file's own closing line permits; the INDEX row stays as it is.
- **Create no open-items row**, flip or discard none, allocate no `D-NNN`, and write nothing into
  `DECISIONS.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` or any ruling record, other than
  the one `STATUS.md` entry Task 5 orders.
- **Put no choice question to the user and recommend nothing** about any list or any UNPLACED
  entry (D-658). The reading file gathers facts; the rulings are taken at Cowork, one list per turn.
- **Take the reading file to the user yourself in no form.** It is landed; the Cowork side puts it
  to him.

**STOP conditions, each of which ends the batch with a report and no further task — except
condition 5, which reverts one commit and lets the batch continue, and says so:**

1. The tip at boot is not `8457c97445ff9a6c506fe999128681b80969e9ba` at **both** ref files. Read
   `cowork_away_returns.md` before anything else and write nothing into the tree.
2. The sanctioned enumeration tool reports **any** tracked modification at boot. **The writing
   side did NOT verify the tree's cleanliness — it has no enumeration tool — so this is an
   expectation and not a measured start state.** A tracked modification is itself the finding.
3. `python tools/audit/gen_derivation_boot_pack.py --check` does not exit 0 at any point. Nothing
   here can move a rendered byte; drift means something else happened.
4. Anything under `tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json`
   differs from its committed blob at any point after Task 0.
5. **Task 1(a)'s object comparison shows a change in EITHER regenerated artifact other than a
   recorded LINE POSITION** — see Task 1(a) for the exact field names that may move. **This one
   condition does NOT end the batch**: revert Task 1(a)'s commit as Task 1(a) says, which restores
   the tree to a known state with nothing half-done, report the comparison in full, and CONTINUE
   with Task 1(b) and Task 2 — a change of content in a recorded prediction or a derived population
   is a finding for the user, and the reading file does not wait on it.
6. The new tool exits with `STOP:` on its render run, or its `--check` does not exit 0 immediately
   after the render, or `gen_guard_state.py --check` HALTS (as distinct from reporting drift) after
   Task 2.
7. The rendered reading file's three list counts do not read **IN 110 / OUT 132 / UNPLACED 2**,
   total **244** — the figures the verdict-pass report states at its Task 2 table and the figures
   the writing side counted at the generator's table after that batch closed. A different count
   means the table or the candidate list moved under this batch.

---

## Task 0 — land this dispatch

**One commit. The paths are: this dispatch and the Task 0 enumeration artifact. Nothing else.**

```
cc_instruction_l2_reading_file_2026_09_05.md
```

Enumerate first, with the sanctioned enumeration tool rather than with `git status`:

```
cd C:\s\MS && python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_reading_file_task0.json
```

Redirect the run's output to a scratch file **outside the repository** and read it with the file
tools. **Expect ZERO tracked modifications**, this dispatch present as an untracked addition, and
the standing untracked `cc_*` root population present and correctly not landed. **Any tracked
modification is STOP condition 2.**

Commit both paths together:

```
docs(cowork): land the L2 reading-file dispatch

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

**On the trailer.** That is the form this repository's own history carries. If a system-level
attribution instruction in force for your session mandates a different form, follow that
instruction and **declare the difference in the report** — the three preceding batches did exactly
this and the departure is expected, not an error. The commit subject and body are this dispatch's,
verbatim, either way.

Push. Report the commit hash, read at both ref files with the file tools.

---

## Task 1 — two small repairs, each its own commit, BEFORE the reading file

Neither can be stopped partway, so both go first with nothing large in front (D-670). **If either
halts (a tool that raises, a lint that fails), the batch ends there with nothing half-done — the
reading file has not been started.** Condition 5 is the one exception: it reverts and continues.

### (a) Regenerate the two artifacts the OI-378 row staled, and prove at the objects that only recorded positions moved

**What is wrong, at the object.** The verdict-pass report (§5 of
`cc_report_l2_verdict_pass_2026_09_05.md`) established that `tools/audit/gen_phase3_gate_partition.py
--check` and `tools/audit/gen_l0_l1_outgoing_population.py --check` both report drift because each
records line positions into `OPEN_ITEMS.md` and the OI-378 row shifted those positions by one. That
batch left both standing because its licence named one measurement. **The writing side wrote that
licence, so this is not a user decision; it is corrected here, under a proof.** The user may
overrule it in one sentence, and the alternative — leaving twelve reds where ten are inherited — is
recorded in the report.

**What may move, and nothing else.** In `tools/audit/phase3_gate_partition.json`: the fields
`found_lines`, `anchor_ok` and `drift` of a source record whose `file` is `OPEN_ITEMS.md` (the
tool's `locate()` writes exactly those three from the file it reads; `expected_line` is AUTHORED in
the tool and must not change). In `tools/audit/l0_l1_outgoing_population.json`: the fields
`line_number` and `first_line_number_as_a_locator_only` of a hit whose path is `OPEN_ITEMS.md`.
**Two further kinds may move and are named in the report if they do: a run stamp (a time, a HEAD
hash), and a summary count whose only inputs are those position fields.** Any other changed key —
a verdict, a gating verdict, a member, a quote, a population — is STOP condition 5.

**Step 1.** Record the tip before the act: read both ref files with the file tools; call it
`BEFORE`.

**Step 2.** Regenerate both, each redirected to scratch and read with the file tools:

```
cd C:\s\MS && python tools/audit/gen_phase3_gate_partition.py
cd C:\s\MS && python tools/audit/gen_phase3_gate_partition.py --check
cd C:\s\MS && python tools/audit/gen_l0_l1_outgoing_population.py
cd C:\s\MS && python tools/audit/gen_l0_l1_outgoing_population.py --check
```

Expect each `--check` to **exit 0** after its regeneration. If a regeneration itself STOPs or
halts, that is a finding: do not commit, restore the two artifacts with `git checkout --
tools/audit/phase3_gate_partition.json tools/audit/l0_l1_outgoing_population.json` (a git write,
not a working-tree read), and end the batch with the halt quoted in full.

**Step 3.** Commit the two artifacts together:

```
audit: regenerate the two artifacts the OI-378 row staled — recorded line positions only

Both tools record line positions into OPEN_ITEMS.md; the OI-378 row shifted
every position below line 278 by one. Neither tool is edited; no
expected_line is re-aimed. The object comparison is in the report.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push; read the tip at both ref files; call it `AFTER`.

**Step 4 — the proof, at the git objects by explicit hash and at nothing else (D-253's licence).**
For each of the two paths, take both committed versions as objects:

```
git show <BEFORE>:tools/audit/phase3_gate_partition.json > <scratch>\p3_before.json
git show <AFTER>:tools/audit/phase3_gate_partition.json  > <scratch>\p3_after.json
git show <BEFORE>:tools/audit/l0_l1_outgoing_population.json > <scratch>\l01_before.json
git show <AFTER>:tools/audit/l0_l1_outgoing_population.json  > <scratch>\l01_after.json
```

with `<BEFORE>` and `<AFTER>` written out as the full forty-character hashes. Then run this
read-only script from the scratchpad (it reads scratch files only, never the tree; `%TEMP%` does
not expand in this shell — use the scratchpad path as the preceding batches did):

```python
# compare_positions_only.py — READ-ONLY over two git-object dumps in scratch. Lists every leaf
# key path whose value differs between BEFORE and AFTER, then says whether every one of them is
# a permitted position field. Never touches the repository.
import json, sys

PERMITTED_LEAF_NAMES = {
    "found_lines", "anchor_ok", "drift",                       # gen_phase3_gate_partition: locate()
    "line_number", "first_line_number_as_a_locator_only",      # gen_l0_l1_outgoing_population
}

def leaves(node, path=()):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from leaves(v, path + (str(k),))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from leaves(v, path + (f"[{i}]",))
    else:
        yield path, node

def compare(before_path, after_path, label):
    b = dict(leaves(json.load(open(before_path, encoding="utf-8"))))
    a = dict(leaves(json.load(open(after_path, encoding="utf-8"))))
    changed = sorted(set(k for k in set(b) | set(a) if b.get(k, "<absent>") != a.get(k, "<absent>")))
    print(f"== {label}: {len(changed)} differing leaf path(s)")
    bad = []
    for k in changed:
        name = next((seg for seg in reversed(k) if not seg.startswith("[")), "")
        ok = name in PERMITTED_LEAF_NAMES or (
            # a `drift` record is an object; its children `expected`/`actual` sit under it.  And
            # gen_phase3_gate_partition republishes every drifted verification record WHOLE under
            # `quote_verification.anchor_drift`, so a newly drifted anchor appears there as a whole
            # new record; that list is derived from the position fields and nothing else.
            len(k) >= 2 and any(seg in ("drift", "anchor_drift") for seg in k))
        print(("   ok   " if ok else "   BAD  ") + "/".join(k), "|", repr(b.get(k, "<absent>")), "->", repr(a.get(k, "<absent>")))
        if not ok:
            bad.append(k)
    print(f"== {label}: {'ALL PERMITTED' if not bad else f'{len(bad)} NOT PERMITTED'}")
    return not bad

ok1 = compare(sys.argv[1], sys.argv[2], "phase3_gate_partition.json")
ok2 = compare(sys.argv[3], sys.argv[4], "l0_l1_outgoing_population.json")
print("RESULT:", "POSITIONS ONLY" if (ok1 and ok2) else "CONTENT CHANGED — STOP CONDITION 5")
sys.exit(0 if (ok1 and ok2) else 1)
```

Redirect its output to scratch and read it with the file tools. **Every differing leaf must print
`ok`.** Two kinds of leaf printed `BAD` are nonetheless permitted, and each must be NAMED in the
report with its key path and both values: a run stamp (a time, a HEAD hash), and a summary COUNT
whose only inputs are the position fields (a count of anchors found or of anchors drifted). A
`BAD` leaf of any other kind — a verdict, a gating verdict, a member, a quote, a population — is
not permitted. **Any such leaf is STOP condition 5**: revert the
commit with `git revert --no-edit <AFTER>` (a git write), push, read the tip at both ref files, and
put the full comparison output in the report — the user decides what a changed prediction or a
changed population means. **Then continue with Task 1(b)**: the revert has restored the two
artifacts to their `BEFORE` blobs, so nothing is half-done, and the two reds stay standing as the
previous batch left them.

Report the two commit hashes and the comparison's summary lines, with every differing leaf path.

### (b) Append the fourth guard observation to `open_items/OI-378.md`

The verdict-pass batch recorded (its §7 departure 3) a fourth observation of the shell-read guard's
denial behaviour — a `python -c` opening two plain RELATIVE repository paths, DENIED — and did not
write it into OI-378, its dispatch having named three. OI-378's detail file closes with *"Resolution
belongs in the INDEX row; dated notes may be appended here."* **Append, after that closing line, this
note and nothing else** — no existing line of the file or of the INDEX changes:

```

---

**Dated note, 2026-09-05 (CC, `cc_instruction_l2_reading_file_2026_09_05.md` Task 1(b)) — a FOURTH
observation, relayed from `cc_report_l2_verdict_pass_2026_09_05.md` §7 departure 3 and not
re-measured.** A `python -c` that opened `cc_report_l2_candidate_list_2026_09_05.md` and
`cowork_away_returns.md` — two plain RELATIVE repository paths inside interpreter code — was
**DENIED** by the guard, the denial naming `CLAUDE.md`'s conventions, D-253 and the guard-family
ruling of 2026-08-08. It differs from observation (3) above in the paths being relative rather than
absolute, and in the utility from observation (1), which was not denied. **As before: no cause is
asserted, none may be read in, no remedy is proposed, and the INDEX row is unchanged** — a fourth
data point is recorded, not a conclusion drawn.
```

Re-read the appended note with the file tools. Run `python tools/audit/index_status_lint.py` and
`python tools/open_items_split_check.py` (redirected, read with the file tools) and report both
results — the INDEX did not change, so both are expected to pass unchanged. Commit the one path
(plus `open_items/register_check.json` if the split check rewrote it, as it did last batch):

```
docs(open-items): OI-378 — a fourth guard observation appended as a dated note, no cause asserted

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the hash and the zero-deletion proof at the object (`git show --stat <hash>`).

---

## Task 2 — the reading-file generator, its enrolment, and the rendered reading file: ONE commit

### (a) Create the tool

Write `tools/audit/gen_withheld_family_reading.py` with exactly this content. It imports the
boot-pack generator as a module and reads `VERDICTS`, `CRITERION`, the keyword tuple and
`group_title()` from it — no second copy of any of them — and it locates L2's charter sentence in
`FRAMEWORK.md` on every run, stopping if it is not there exactly once.

```python
"""THE WITHHELD-FAMILY READING FILE for a deriving subject — rendered from the generator's own
authored verdict table and the subject's published candidate list, never hand-written.

  python tools/audit/gen_withheld_family_reading.py --subject l2            # render
  python tools/audit/gen_withheld_family_reading.py --subject l2 --check    # re-render and compare, exit 1 on drift

WHAT IT IS.  A reading surface for the user: the three verdict lists — IN, OUT, UNPLACED — that
`tools/audit/gen_derivation_boot_pack.py` carries in `VERDICTS[<subject>]` as PROPOSALS, each row
with the entry's identity, its register group, its title, the finding the verdict was made on and
the reason, so the user can rule the lists one per turn (Ruling 81, §3cj of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`).  It renders; it decides nothing.

WHY A GENERATOR AND NOT A HAND-WRITTEN FILE.  The pilot's reading file was hand-authored from a
75-row table.  This subject's table is 244 rows, and a hand copy of 244 findings is a second copy of
the verdict text that can drift from the table it copies (#6).  Rendering from the table keeps one
home for every verdict and lets `--check` prove the file is what the table says.

WHAT IT READS.  `VERDICTS[subject]`, `CRITERION[subject]`, the keyword tuple and `group_title()` —
imported from the boot-pack generator, so there is no second copy of any of them here; the
subject's candidate-list artifact, for each candidate's register group, title and the sizing; and
`FRAMEWORK.md`, to locate the subject's charter sentence and STOP if it is no longer there once.

WHAT IT DOES NOT DO.  It authors no verdict, withholds nothing, renders no pack, boots no session,
edits no table, and makes no recommendation on any UNPLACED entry (D-658).  Every STOP below is a
halt, never a warning.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from output_encoding import use_utf8_output          # noqa: E402  (path set above)

use_utf8_output()

import gen_derivation_boot_pack as boot_pack         # noqa: E402  (path set above)


class Stop(Exception):
    """An input is missing, a table and its candidate list disagree, or an anchor drifted."""


# ── AUTHORED, per subject: where its candidate list is, where the reading file goes, the prose ──
SUBJECTS = {
    "l2": {
        "candidate_list": "tools/audit/l2_candidate_list.json",
        "out": "ratification_surfaces/cowork_withheld_family_l2_reading.md",
        "title": "The WITHHELD FAMILY for the L2 subject — put to the user for a ruling",
        "subject_in_plain_words": (
            "The tonal reading: over this music, what is the tonality at each moment, where does "
            "each harmony give way to the next, which sounding notes belong to the harmony and "
            "which elaborate it, and what chord is read over each span?"),
        # The charter sentence is LOCATED in FRAMEWORK.md on every run and the run STOPs if it is
        # not there exactly once, so the test the verdicts were made against cannot drift from the
        # charter silently.  The needle carries the bold "Question" label of the L2 building block
        # because the same sentence is restated later in the file under an italic label; the bold
        # form occurs once.
        "charter_file": "FRAMEWORK.md",
        "charter_label": "**Question, in one sentence:** ",
        "charter_sentence": (
            "over this music, what is the tonality at each moment, where does each\n"
            "  harmony give way to the next, which sounding notes belong to the harmony and which "
            "elaborate it, and\n"
            "  what chord is read over each span?"),
        "charter_heading": "### L2 — The tonal reading. The one entangled decision.",
        "criterion_rulings": (
            "Ruling 82 (§3ck) fixed the group term; Ruling 86 (§3co) the keyword list; Rulings 87 "
            "and 88 (§3cp, §3cq) the home-document list, with the `ARCHITECTURE.md` passage term "
            "empty; Ruling 89 (§3cr) struck one document from that list. All in "
            "`cowork_rulings_2026_08_31_decision_surface_sitting.md`."),
        "verdicts_authored": (
            "by Claude Code on 2026-09-05 under `cc_instruction_l2_verdict_pass_2026_09_05.md` "
            "Task 2, at each entry's own published verbatim and plain restatement in the candidate "
            "list, in the fixed group order that dispatch names"),
    },
}

# The order the verdict pass wrote the groups in, and the order the lists below keep: the six
# groups the ruled group term names first, then the twelve reached only by the keyword or
# home-document terms.  A group absent from a subject's candidate list is simply skipped.
GROUP_ORDER = ["A", "C", "D", "E", "F", "G", "B", "H", "I", "J", "K", "L", "M", "N", "Q", "S", "T", "U"]

LIST_HEADINGS = {
    boot_pack.VERDICT_IN: (
        "LIST ONE — IN: proposed to be WITHHELD from the pack",
        "A deriving session that read one of these would know, in whole or in part, what the ruled "
        "answer to the charter question is.  Each row says what in the entry's own text discloses it."),
    boot_pack.VERDICT_OUT: (
        "LIST TWO — OUT: proposed to be ADMITTED to the pack",
        "These reached the candidate list, were read, and bear on another unit.  Each row says what "
        "the entry bears on instead."),
    boot_pack.VERDICT_UNPLACED: (
        "LIST THREE — UNPLACED: the entry's own published text does not settle it",
        "These could not be defended either way in one sentence at the entry's own verbatim, so "
        "they were not guessed.  Each row says what was read.  NO RECOMMENDATION IS MADE ON ANY OF "
        "THEM (D-658): where the record does not settle the question, the surface gathers facts."),
}


def read_text(rel: str) -> str:
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise Stop(f"{rel} is not in the tree")
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def read_json(rel: str):
    return json.loads(read_text(rel))


def cell(text: str) -> str:
    """One table cell: no pipe, no newline, so the row still splits into its columns."""
    return " ".join(str(text).split()).replace("|", "\\|")


def locate_once(haystack: str, needle: str, what: str) -> None:
    n = haystack.count(needle)
    if n != 1:
        raise Stop(f"{what}: expected exactly one occurrence, found {n}")


def render(subject: str) -> str:
    if subject not in SUBJECTS:
        raise Stop(f"no authored reading-file entry for subject {subject!r}")
    spec = SUBJECTS[subject]
    if subject not in boot_pack.VERDICTS:
        raise Stop(f"the boot-pack generator carries no VERDICTS table for {subject!r}")
    if subject not in boot_pack.CRITERION:
        raise Stop(f"the boot-pack generator carries no CRITERION entry for {subject!r}")
    verdicts = boot_pack.VERDICTS[subject]
    criterion = boot_pack.CRITERION[subject]
    art = read_json(spec["candidate_list"])
    cands = art["the_candidates"]
    by_id = {c["id"]: c for c in cands}

    # ── the table and the candidate list must agree exactly (the generator's own STOPs, re-run
    #    here because build_subject() cannot be called for a subject with no WITHHELD entry) ──────
    missing = [c["id"] for c in cands if c["id"] not in verdicts]
    orphan = sorted(set(verdicts) - set(by_id))
    if missing:
        raise Stop(f"{len(missing)} candidate(s) carry no verdict: {missing[:10]}{'…' if len(missing) > 10 else ''}")
    if orphan:
        raise Stop(f"verdict(s) for entries the candidate list does not carry: {orphan}")
    bad = sorted({v[0] for v in verdicts.values()} - set(boot_pack.VERDICTS_VOCABULARY))
    if bad:
        raise Stop(f"verdict(s) outside the closed vocabulary: {bad}")
    for cid, v in verdicts.items():
        if len(v) != 3 or not all(str(x).strip() for x in v):
            raise Stop(f"the verdict for {cid} lacks its verdict, its finding or its reason")

    # ── the charter sentence, located at its home ──────────────────────────────────────────────
    framework = read_text(spec["charter_file"]).replace("\r\n", "\n")
    locate_once(framework, spec["charter_heading"], f"{spec['charter_file']} heading")
    locate_once(framework, spec["charter_label"] + spec["charter_sentence"],
                f"{spec['charter_file']} charter sentence under its bold label")
    charter_one_line = " ".join(spec["charter_sentence"].split())

    counted = {v: sum(1 for t in verdicts.values() if t[0] == v) for v in boot_pack.VERDICTS_VOCABULARY}
    per_group = {}
    for cid, (v, _f, _r) in verdicts.items():
        g = by_id[cid]["register_group"]
        per_group.setdefault(g, {vv: 0 for vv in boot_pack.VERDICTS_VOCABULARY})
        per_group[g][v] += 1
    groups_present = [g for g in GROUP_ORDER if g in per_group]
    unknown_groups = sorted(set(per_group) - set(GROUP_ORDER))
    if unknown_groups:
        raise Stop(f"candidate(s) in register group(s) not in the fixed order: {unknown_groups}")

    def rows_for(verdict: str):
        for g in groups_present:
            ids = sorted((cid for cid, t in verdicts.items()
                          if t[0] == verdict and by_id[cid]["register_group"] == g),
                         key=lambda s: int(s.split("-")[1]))
            for cid in ids:
                yield g, by_id[cid], verdicts[cid]

    L = []
    w = L.append
    w(f"# {spec['title']}")
    w("")
    w("> **STATUS: READING SURFACE — FOR RULING. NOTHING BELOW IS APPLIED.** Every verdict in this")
    w("> file is a PROPOSAL carried in `tools/audit/gen_derivation_boot_pack.py` → `VERDICTS[\"" + subject + "\"]`.")
    w("> No identity is withheld, no pack is rendered and no session is booted until you have ruled the")
    w("> lists (Ruling 81, §3cj of `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity")
    w("> is withheld that the user has not ruled*).")
    w(">")
    w("> **GENERATED FILE — do not hand-edit.** Rendered by `tools/audit/gen_withheld_family_reading.py`")
    w(f"> from that verdict table and from `{spec['candidate_list']}`; its `--check` re-renders and")
    w("> compares.  Every count below is computed from those two objects, none is transcribed (D-431).")
    w(">")
    w(f"> The verdicts were authored {spec['verdicts_authored']}.")
    w("")
    w("---")
    w("")
    w("## 1. The words used here, explained first")
    w("")
    w("- **A deriving session** — a session that writes what the analysis *should* do for one unit,")
    w("  from the domain and from your ratified design intent, without reading what the current code or")
    w("  the current specifications say it *does*.")
    w("- **The boot pack** — the self-contained directory such a session opens at boot, and nothing")
    w("  else.  L2's pack does not exist yet; its members are a later ruling.")
    w("- **The withheld family** — the recorded decisions, documents and passages cut out of that pack")
    w("  for one subject, so that the answer the session is chartered to derive does not reach it.")
    w("- **A candidate** — a decisions-register entry the ruled criterion picked as possibly disclosing")
    w("  some part of that answer.  Being a candidate is not a judgment; the verdict is.")
    w("- **A verdict** — one of three words written against one candidate: **IN** (withhold it), **OUT**")
    w("  (admit it), **UNPLACED** (the entry's own text does not settle it).  Each carries a *finding* —")
    w("  what the entry's own text says — and a *reason* — why that makes it IN, OUT or UNPLACED.")
    w("- **The register group** — the letter under which `DECISIONS.md` lists an entry.  It is a")
    w("  property of the entry and decided no verdict.  Note that register group **E** is titled")
    w("  *Layer 2 — the slicer* while this subject is called **L2**: they are different units in two")
    w("  different numbering schemes (`ARCHITECTURE.md`'s Layer 1–6 and the framework's L0/L1/L2).")
    w("")
    w("## 2. The subject the deriving session will derive, stated from scratch")
    w("")
    w(f"> **{spec['subject_in_plain_words']}**")
    w("")
    w(f"That is L2's charter question, located on this run at `{spec['charter_file']}` under the heading")
    w(f"`{spec['charter_heading']}` — *\"{charter_one_line}\"* — and it asks FOUR things at once: the")
    w("tonality at each moment; where one harmony ends and the next begins; which sounding notes are")
    w("chord tones and which elaborate; and what chord is read over each span.  The pilot subject asked")
    w("only the second of these.  A verdict here is IN if the entry discloses the ruled answer to ANY of")
    w("the four, in whole or in part.")
    w("")
    w("## 3. What this family protects, and what is not ruled for L2")
    w("")
    w("For the pilot, a separate ruling named one oracle passage the family protected.  **No ruling")
    w("names an oracle passage for L2.** Ruling 81's own record states that the record was searched")
    w("before it was taken and that no ruling reached L2's family; Ruling 81 rules that the pack")
    w("carries a family derived over a criterion built from the charter, and stops there; and none of")
    w("Rulings 82 to 89, which fix the criterion's terms, names one.  What the family protects is")
    w("therefore the entries themselves: the recorded current answers to the four limbs, which are the")
    w("IN rows below.  This file does not restate any of those answers beyond the one-sentence finding")
    w("each row carries, and it does not invent an oracle.")
    w("")
    w("## 4. How the candidate list was derived, and the bound on it")
    w("")
    w("The family was not hand-picked.  The boot-pack generator's own `candidates()` walks the")
    w("DESIGN-INTENT class of the ratified rulings sort and returns as a candidate every entry meeting")
    w(f"any one term of the ruled criterion — {spec['criterion_rulings']}  The terms, read from the")
    w("generator's committed table on this run:")
    w("")
    groups = criterion["groups"]
    w("- **its register group is one of** " + ", ".join(
        f"**{g}** ({boot_pack.group_title(g)})" for g in groups) + ";")
    w("- **its recorded home is one of these documents:** " + ", ".join(
        f"`{d}`" for d in criterion["home_documents"]) + ";")
    w("- **any of its title, verbatim, plain restatement or search patterns contains one of these "
      f"{len(criterion['keywords'])} words or phrases:** " + ", ".join(
        f"*{k}*" for k in criterion["keywords"]) + ";")
    w("- the `ARCHITECTURE.md` passage term is **EMPTY** by ruling, and no identity is named by any "
      "ruling for this subject, so the named-identity term is **EMPTY**.")
    w("")
    pop = art["the_population"]
    w(f"**The population and the bound.** The class walked holds **{pop['design_intent_class']}** "
      f"design-intent entries of the sort artifact's **{pop['sort_entries_total']}**; the criterion "
      f"returned **{pop['candidates']}** candidates.  The population is the sort artifact's and NOT the "
      "decisions register's, so register entries outside it are reached by no term (D-661, #24).  The "
      "keyword term is a plain substring match whose reach is UNMEASURED; an entry bearing on this "
      "subject in words none of the terms carry does not appear here at all, and the candidate list "
      "says so on itself.  A keyword can match inside a longer word; every such match is published "
      f"with its context at `{spec['candidate_list']}` → `the_candidates` → `matched_by`, and no "
      "keyword match was treated as a reason for IN.")
    w("")
    sizing = art["the_sizing"]["by_register_group_and_term"]
    w("**The candidates by register group, and the verdicts proposed in each:**")
    w("")
    w("| group | register-group title | candidates | reached by the group term | by a keyword | by a home document | IN | OUT | UNPLACED |")
    w("|---|---|---|---|---|---|---|---|---|")
    for g in groups_present:
        s = sizing.get(g, {})
        n = sum(per_group[g].values())
        w(f"| {g} | {cell(boot_pack.group_title(g))} | {n} | {s.get('group', 0)} | {s.get('keyword', 0)} | "
          f"{s.get('home-document', 0)} | {per_group[g][boot_pack.VERDICT_IN]} | "
          f"{per_group[g][boot_pack.VERDICT_OUT]} | {per_group[g][boot_pack.VERDICT_UNPLACED]} |")
    total = sum(counted.values())
    w(f"| **all** | | **{total}** | | | | **{counted[boot_pack.VERDICT_IN]}** | "
      f"**{counted[boot_pack.VERDICT_OUT]}** | **{counted[boot_pack.VERDICT_UNPLACED]}** |")
    w("")
    w("## 5. The test each verdict was made against")
    w("")
    w("From the pilot's own dispatch, with L2's four-limbed question in place of the pilot's one:")
    w("")
    w("- **IN** — a deriving session that read this entry would know, in whole or in part, what the")
    w("  ruled answer to the charter question is.")
    w("- **OUT** — the entry bears on another unit, and reading it tells the session nothing about that")
    w("  answer.  The reason says what it bears on instead.")
    w("- **UNPLACED** — the entry's own published text does not settle it.  The reason says what was read.")
    w("")
    w("**Default nothing:** a verdict that could not be defended in one sentence at the entry's own")
    w("verbatim was recorded UNPLACED rather than guessed.  **Every verdict was written at the published")
    w("text** — the entry's verbatim and plain restatement in the candidate list — and no entry's home")
    w("document was opened to decide one; the register group and the LEGACY mark were forbidden to")
    w("decide anything, and the executing side's report states that they did not.")
    w("")
    for verdict in (boot_pack.VERDICT_IN, boot_pack.VERDICT_OUT, boot_pack.VERDICT_UNPLACED):
        heading, gloss = LIST_HEADINGS[verdict]
        w("---")
        w("")
        w(f"## {heading}")
        w("")
        w(f"*{gloss}*  **{counted[verdict]} entries.**")
        w("")
        if counted[verdict] == 0:
            w("*The list is empty on this run.  The heading stays because the value stays in the "
              "generator's closed three-value vocabulary.*")
            w("")
            continue
        w("| ID | group | Title | Finding — what the entry's own text says | Reason |")
        w("|---|---|---|---|---|")
        for g, c, (v, finding, reason) in rows_for(verdict):
            w(f"| {c['id']} | {g} | {cell(c['title'])} | {cell(finding)} | {cell(reason)} |")
        w("")
    w("---")
    w("")
    w("## 6. What is NOT in this file yet, and why")
    w("")
    w("- **No leak list.** The pilot's fourth list named entries the pack's generated members could not")
    w("  render because their text pointed into the implementation.  A leak is found when a pack is")
    w("  rendered, and L2's pack is not rendered until the family is ruled and its members are ruled.")
    w("- **No derived cross-reference additions.** When a pack is built, every entry whose own text")
    w("  quotes or cross-references a withheld identity is withheld with it, derived and published whole")
    w("  and not ruled.  Ruling 84 (§3cm) bounds that derivation: it may ADD a withholding to an entry")
    w("  you have not ruled on, and may NOT overturn a verdict you have ruled.  None exists for L2 yet.")
    w("- **No withheld passages.** A passage is a cut inside a member the boot list quotes WHOLE.  L2's")
    w("  boot list is not ruled, so there is no member to cut.")
    w("- **The date each verdict carries.** Ruling 81 requires it.  The generator stamps every verdict")
    w("  with one module constant at render time, which is the pilot's authoring date and would be false")
    w("  for these; the gap is recorded as owed to the batch that builds L2's pack, and the authoring date")
    w("  of every group block stands in the table's own heading comments meanwhile.")
    w("")
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
    w("## 8. What the ruling does NOT do")
    w("")
    w("- **It boots no session and renders no pack.**")
    w("- **It moves no register entry and no status.** Withholding an entry from one pack says nothing")
    w("  about that entry's standing in `DECISIONS.md`.")
    w("- **It edits no governing document** and closes no open item.")
    w("- **It does not settle who derives**, nor L2's boot-list members, nor the date mechanism.")
    w("- **It does not claim the candidate list is complete.** The criterion's reach is unmeasured, and")
    w("  §4 says so.")
    w("")
    w("---")
    w("")
    w(f"*Provenance: rendered by `tools/audit/gen_withheld_family_reading.py --subject {subject}` from")
    w(f"`tools/audit/gen_derivation_boot_pack.py` → `VERDICTS[\"{subject}\"]` and `CRITERION[\"{subject}\"]`,")
    w(f"`{spec['candidate_list']}`, and the charter sentence located at `{spec['charter_file']}`.  Every")
    w("row's finding and reason is the generator's authored text, byte for byte; every count is computed")
    w("on the run.  TOWARDS the ultimate objective and TOWARDS the guiding principles.*")
    w("")
    return "\n".join(L)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--subject", required=True, choices=sorted(SUBJECTS))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    text = render(a.subject)
    out_rel = SUBJECTS[a.subject]["out"]
    out = os.path.join(ROOT, out_rel)
    if a.check:
        if not os.path.exists(out):
            print(f"FAIL: {out_rel} does not exist")
            return 1
        with open(out, encoding="utf-8", newline="") as fh:
            on_disk = fh.read()
        if on_disk == text:
            print(f"PASS: {out_rel} re-renders byte-identically")
            return 0
        print(f"FAIL: {out_rel} differs from what the generator now renders")
        return 1
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"wrote {out_rel} ({len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as e:
        print(f"STOP: {e}")
        sys.exit(2)
```

**Two things about that code you must check at the objects before running it, and report:**

1. `from output_encoding import use_utf8_output` — the boot-pack generator does the same import
   from the same directory (its own line `from output_encoding import use_utf8_output`), so the
   module is there; confirm with `Glob` that `tools/audit/output_encoding.py` exists.
2. The `charter_label` + `charter_sentence` strings are the L2 building block's question line as it
   stands in `FRAMEWORK.md` under the heading `### L2 — The tonal reading. The one entangled
   decision.` — the bold label `**Question, in one sentence:** ` followed by the sentence wrapped
   across three lines with two-space continuation indents. The writing side read it there and
   confirmed the labelled form occurs exactly once (the sentence is restated later in the file under
   an italic label, which the needle deliberately does not match). If the tool STOPs with
   `FRAMEWORK.md charter sentence under its bold label: expected exactly one occurrence, found 0`,
   the wrapping in the file differs from the string: **do not edit `FRAMEWORK.md`**; correct the
   string in the tool to the file's exact bytes (read with the file tools), and declare the
   correction in the report as a fact about this dispatch.

### (b) Enrol the tool in the guard set, in the same act

In `tools/audit/gen_guard_state.py`, in the `AUTHORED` list, insert the following entry
**immediately after** the entry whose first element is
`"tools/audit/gen_l0_l1_outgoing_population.py"` (the entry that ends with the words
`moving the population silently"),`) and before the comment line
`# ---- AUTHORED 2026-08-15, cc_instruction_artifact_inventory.md`:

```python
    # ---- AUTHORED 2026-09-05, cc_instruction_l2_reading_file_2026_09_05.md Task 2 ---------------
    # Registered in the act that creates the tool, for the reason the entries above give: a derived
    # candidate with no authored invocation is this runner's own STOP.
    ("tools/audit/gen_withheld_family_reading.py", ["--subject", "l2", "--check"],
     "L2's withheld-family reading file re-renders from the boot-pack generator's own authored "
     "verdict table and the published candidate list, with the charter sentence located at "
     "FRAMEWORK.md. What it guards is that the file the user rules from is what the table says — "
     "every row's finding and reason byte-identical to the generator's authored text, every count "
     "computed — so an edit to the table without a re-render, a hand edit to the file, or a "
     "candidate list that no longer matches the table turns this red rather than leaving the user "
     "reading a surface that has drifted from its source"),
```

Nothing else in that file changes.

### (c) Render, check, and prove the pack untouched

```
cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l2
cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l2 --check
cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check
```

each redirected to scratch and read with the file tools. Expect: `wrote
ratification_surfaces/cowork_withheld_family_l2_reading.md (<n> bytes)`; then `PASS: … re-renders
byte-identically`, exit 0; then the boot-pack generator's `--check` at **exit 0** (STOP condition 3
otherwise). A `STOP:` line from the new tool is STOP condition 6 — quote it in full.

**Read the rendered file with the file tools** — the banner, §1 to §5, the head of each list, §6
to §8 — and check with `Grep` that the three list headings each carry their count: LIST ONE
`**110 entries.**`, LIST TWO `**132 entries.**`, LIST THREE `**2 entries.**`, and that the summary
table's last row reads `**244**`. Any other figure is STOP condition 7. Count the table rows under
each list heading with `Grep` (`^\| D-\d+ \|`) and confirm 244 in all.

### (d) Commit the three paths together

`tools/audit/gen_withheld_family_reading.py`, `tools/audit/gen_guard_state.py`,
`ratification_surfaces/cowork_withheld_family_l2_reading.md`:

```
audit(l2): the withheld-family reading file, rendered from the verdict table by a guard-enrolled generator

The pilot's reading file was hand-authored from 75 rows; L2's 244 are rendered
from VERDICTS["l2"] and the published candidate list so the file cannot drift
from its source (#6, D-431). The tool is enrolled in the guard set in this
act. Nothing is withheld; every verdict remains a proposal.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the hash.

---

## Task 3 — prove nothing else moved

```
cd C:\s\MS && python tools/audit/changed_paths.py --json tools/audit/changed_paths_l2_reading_file_task3.json
```

Redirect and read with the file tools. **Expect ZERO tracked modifications** and the Task 3
artifact itself, which will not appear in its own listing. Anything under
`tools/audit/derivation_boot_pack/` or `tools/audit/derivation_boot_pack.json` appearing as
modified is STOP condition 4.

Then the standing guard set:

```
cd C:\s\MS && python tools/audit/gen_guard_state.py --check
```

Report the exit code and the summary. **Expected: drift (exit 1), NOT a halt** — the population
grew by one (the new tool) and two artifacts were regenerated, so the committed `guard_state.json`
no longer re-derives; a HALT naming `gen_withheld_family_reading.py` as a candidate without an
invocation is STOP condition 6 and means the enrolment in Task 2(b) did not land as written. **Do
not regenerate here** — record it and carry on to Task 4, so the batch closes finished rather than
mid-flight; the end state regenerates it. Run the new tool's `--check` once more on its own and
report it (expected exit 0).

Commit the Task 3 enumeration artifact alone:

```
audit: Task 3 enumeration for the L2 reading-file batch

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Report the hash.

---

## Task 4 — the report

Write `cc_report_l2_reading_file_2026_09_05.md` at the repository root, untracked, and commit it in
Task 5's commit. It carries, in this order:

1. **The tip at boot and the tip at close**, each read at both ref files with the file tools, with
   the close tip written in the batch's last commit on the convention the two preceding reports
   state at their own tables.
2. **Task 0's result** — the commit hash and the enumeration showing zero tracked modifications.
3. **Task 1(a)** — `BEFORE` and `AFTER`, both `--check` exit codes after regeneration, and the
   object comparison's output IN FULL: every differing leaf path with its before and after value,
   and the two summary lines. If any leaf was a run stamp, say so and name it. **State plainly that
   no tool was edited and no `expected_line` re-aimed.**
4. **Task 1(b)** — the appended note quoted, the lint and split-check results, the zero-deletion
   proof at the commit object.
5. **Task 2** — the two object checks of 2(a); whether the charter string needed correcting; the
   render line with its byte count; the tool's `--check` result; the boot-pack generator's
   `--check` result; the three list counts and the total as read at the rendered file; the number
   of table rows; and the commit hash.
6. **Task 3's results**, including the guard summary and whether it was drift or a halt.
7. **Any STOP reached**, in full, with what was and was not done.
8. **A declared-departures section** — anything you did that this dispatch does not order, stated
   rather than absorbed, including any shell command that read a repository file (D-253) and the
   commit trailer if it differs.

**Recommend nothing. Take no position on any list or any candidate. Put no question to the user.**

---

## Task 5 — `STATUS.md` and close

Add ONE dated entry at the head of `STATUS.md`'s entry list, in the established form, recording:
the two staled artifacts regenerated with only recorded positions moved, proven at the objects;
the fourth guard observation appended to OI-378's detail file as a dated note; the reading-file
generator created and enrolled and L2's reading file rendered from the verdict table; that nothing
was withheld, no verdict changed, no pack rendered, no session booted, no `D-NNN` allocated and no
open-items row created, flipped or discarded; and the guard-set result. **Per the OI-222 pointer
convention this entry is a POINTER and no figure is restated in it (D-431).**

Commit `STATUS.md` and the Task 4 report together:

```
docs(status): record the L2 reading-file batch — two artifacts regenerated, the reading file rendered

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

Push. Then write the close section into `cowork_away_returns.md` in the established form (a
descriptive heading naming this dispatch, no ordinal, on the convention the last sections of that
file state), and one further commit carrying the end-state guard artifact, so that the batch reads
as FINISHED rather than mid-flight. **In the end-state commit regenerate `guard_state.json` and,
where this batch's own acts staled it, the read-size measurement (`gen_session_start_read_size.py`)
— and declare both.** Expected end state: **77 guards run, TEN failing — the ten inherited and no
other — with `gen_withheld_family_reading.py --subject l2 --check` PASSING**, and neither
`gen_phase3_gate_partition` nor `gen_l0_l1_outgoing_population` failing any longer; **or TWELVE
failing if Task 1(a) was reverted under condition 5**, the two staying exactly as the previous
batch left them. If the failing set is anything else, report the set exactly and do not adjust
anything to reach the expected number.

**On the close test.** Follow the practice of the preceding batch and state in the close section's
commit table which form you used (close section and end-state artifact in the same commit, or one
apart).

---

## What this dispatch deliberately leaves to later acts, named so it is not lost

- **The three rulings**, taken at Cowork one list per turn from the rendered reading file, each
  with its surface first and its question in a later turn (D-249). Not this batch's, and not
  Claude Code's at all.
- **Writing the ruled lists back** to `VERDICTS["l2"]`, re-rendering the reading file (its
  `--check` will go red the moment the table moves, which is the point), and recording the rulings.
- **L2's boot-list members and `EXTRAS["l2"]`**, a separate ruling; then `WITHHELD["l2"]` authored
  from the ruled IN list; then the pack built — and at that batch, **the `DATE` mechanism**, which
  stamps every verdict with the pilot's authoring date and is recorded as owed there.
- **The re-aiming of the `expected_line` values** in `gen_phase3_gate_partition.py`, which this
  batch does not touch: after Task 1(a) that artifact carries `anchor_ok: false` and a `drift`
  record for every `OPEN_ITEMS.md` quote below line 278, as it already carried for the re-aimings of
  2026-08-03. That is a tool edit and is the user's to call for.

---

## The writing side's self-check, run before this dispatch was released (D-434)

1. *Principles.* #6 — the reading file has one source, the generator's own table, and the tool
   imports rather than copies the table, the criterion, the keywords and the group titles; the
   charter sentence is located at its home, not copied as truth. #17f/D-431 — every count in the
   reading file is computed; the seven figures this dispatch states (110/132/2/244 and the segment
   figures it does not restate) are cited to the verdict-pass report and were re-counted by the
   writing side at the generator's table. #12 — nothing is deleted anywhere; the appended note and
   the rendered file are additions; the regenerated artifacts preserve their authored
   `expected_line` values and record drift beside them rather than overwriting it. #18/#19 — the
   Task 1(a) claim that only positions moved is not assumed: it is proved at two git objects by
   explicit hash, and anything else is a STOP. #24 — the tree's cleanliness is declared an
   expectation; the guard's end-state count is stated as expected and the dispatch forbids
   adjusting anything to reach it.
2. *Conventions.* American English in the tool's prose and the dispatch's; the vocabulary block
   precedes first use; *measurement tool*, *check*, *generator*, never *instrument*; no
   self-invented label — *the reading file*, *a stale artifact*, *the guard set* are described in
   plain words where first used.
3. *The bars.* No verdict moves; nothing is withheld; no pack, no session; no INDEX edit; no tool
   edit except the one creation and the one enrolment; no choice question anywhere.
4. *The record.* Ruling 81 is cited for what it says; Ruling 84 for the add-not-overturn bound on
   derived additions (read at §3cm's heading); the criterion rulings are named through the
   generator's own comment and the tool's authored string, not paraphrased; D-670 for the ordering;
   D-658 for no recommendation on UNPLACED; D-661/#24 for the population bound.

### ★ THE FACT CHECK OF THIS DISPATCH, RUN AGAINST THE OBJECTS BEFORE IT WAS LANDED — TWO PASSES, THE SECOND SEARCHING FOR EACH CORRECTED TEXT

1. **The tip.** `8457c97445ff9a6c506fe999128681b80969e9ba` at both ref files, read after the
   verdict-pass batch closed; equal to the close hash Claude Code reported.
2. **The verdict counts.** Counted at the generator's table with `Grep` over the whole file: 126
   IN, 191 OUT, 2 UNPLACED tuples in all; the pilot's table holds 75 with 16 IN (Ruling 81's own
   count of the pilot family), so L2's holds 110 / 132 / 2, total 244 — the report's figures
   reproduce.
3. **The two stale tools' field names.** Read at the tools: `gen_phase3_gate_partition.py`'s
   `locate()` writes `expected_line`, `found_lines`, and on a mismatch `anchor_ok` and `drift`
   (`expected`/`actual`); `gen_l0_l1_outgoing_population.py` writes `line_number` and
   `first_line_number_as_a_locator_only`. `expected_line` is authored in the first tool (its own
   comments record re-aimings of 2026-08-03) and is therefore NOT a permitted change.
4. **Both tools regenerate without a flag and check with `--check`.** Read at each tool's `main`.
5. **The guard runner's candidate rule.** Read at `gen_guard_state.py` `candidates()`: every
   `tools/audit/*.py` carrying `--check`, `--verify` or `--establish`; the new tool carries
   `--check` and so must be enrolled or the runner HALTS — hence Task 2(b) in the same commit, on
   the 2026-09-02 precedent recorded in that list's own comment.
6. **The enrolment anchor.** Read at `gen_guard_state.py`: the L0/L1 population entry ends
   `moving the population silently"),` and is followed by the comment
   `# ---- AUTHORED 2026-08-15, cc_instruction_artifact_inventory.md`.
7. **The charter sentence — a correction the fact check made.** The tool's needle was first the
   bare sentence. Read at `FRAMEWORK.md`, that sentence occurs TWICE with IDENTICAL wrapping — at
   the L2 building block (line 388, under a bold `**Question, in one sentence:**` label) and in a
   later restatement (line 1699, under an italic `*Question, in one sentence:*` label) — so the
   bare needle would have made the tool STOP on its first run. The needle now carries the bold
   label, which `Grep` finds exactly once, as does the heading `### L2 — The tonal reading. The one
   entangled decision.` (the restatement's heading reads *joint decision* and is not a heading).
   The file's line endings were checked to be LF; the tool normalizes CRLF anyway before locating.
   Second pass: the earlier claim that the restatement had "a different wrapping" was searched for
   and removed from this file; it was false.
8. **The pilot's reading-file form.** Read at
   `ratification_surfaces/cowork_withheld_family_harmony_boundary_reading.md`: words-first, the
   subject from scratch, the oracle, the derivation and its bound, the test, the lists, what was
   ruled, what the ruling does not do, provenance. The tool renders the same sections in the same
   order, with §3 stating that no oracle passage is ruled for L2 rather than inventing one.
9. **OI-378's closing line.** Read at `open_items/OI-378.md`: *"Resolution belongs in the INDEX
   row; dated notes may be appended here."* is the last line; the fourth observation is at
   `cc_report_l2_verdict_pass_2026_09_05.md` §7 departure 3 and reads as relayed in Task 1(b).
10. **Corrections made on the second pass.** The dispatch first named the split check's output as
    `split_reconciliation.json` in the previous batch and was corrected by Claude Code to
    `register_check.json`; this dispatch names the file Claude Code actually saw rewritten. The
    guard end-state count is 77 because the new tool joins a population of 76, read at the
    committed `guard_state.json` summary. The tool's source and the comparison script were each
    compiled once in the writing side's own scratch, and the comparison script was run there on
    synthetic data of both shapes (positions only → `POSITIONS ONLY`; one added verdict key →
    `CONTENT CHANGED`) — a test of the writing side's own files, not a run against the repository.
    The permitted-leaf rule was widened on that test's evidence to name run stamps and
    position-only summary counts as reportable rather than as STOPs, and both places that state the
    rule were changed together.
11. **A third pass, on the user's instruction to source and fact-check the dispatch, changed four
    things.** (i) Read at `gen_phase3_gate_partition.py` `build()`: the artifact republishes every
    drifted verification record WHOLE under `quote_verification.anchor_drift`, so a newly drifted
    anchor appears there as a whole new record, and the comparison script would have printed every
    leaf of it `BAD`; the script now permits the `anchor_drift` subtree, and was re-tested on a
    synthetic new drifted record (`POSITIONS ONLY`). (ii) Read at `gen_l0_l1_outgoing_population.py`:
    it also searches `OPEN_ITEMS.md` for its admitting and recorded terms, so a new row could add a
    HIT and not only shift positions; the OI-378 row's text was checked against every term in both
    lists and contains none, but if a hit appears it is content and condition 5 fires — which is why
    condition 5 was changed from ending the batch to reverting one commit and continuing, so an
    apparatus finding cannot block the reading file. (iii) The reading file's §3 claim that no
    oracle passage is ruled for L2 is now sourced to three things — Ruling 81's own statement that
    the record was searched, what Ruling 81 rules, and the absence of any oracle in Rulings 82–89
    (the word occurs once in the whole sitting record, at line 859, before §3cj) — instead of being
    asserted. (iv) The reading file's §5 statement that the register group and the LEGACY mark
    decided nothing is now attributed to the dispatch's prohibition and the executing side's report,
    not stated as this side's own observation. The tool in Task 2(a) and the writing side's scratch
    copy were confirmed byte-identical after each change.
