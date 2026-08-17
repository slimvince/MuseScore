#!/usr/bin/env python3
"""WHAT MOVED IN THE RETIREMENT CENSUS WHEN IT WAS RE-PINNED — every difference classed, or a STOP.

THE RULING THIS EXISTS FOR.  User, 2026-08-17, Ruling 2 of
`cowork_rulings_2026_08_17_sixth_return.md` (the user's word: "A."): *"The next dispatch
regenerates the census fresh at its own commit (`--at` that commit), every movement published and
classed — the split's effect (the F35 namings), the discard's residue, and the tree's ordinary
growth separated — and the artifact re-pinned there ... A census crossing confers CANDIDACY only."*

WHY A SEPARATE TOOL RATHER THAN A FIELD IN THE CENSUS.  The census is a statement about ONE tree;
this is a statement about the DIFFERENCE between two of them.  Folding the second into the first
would make the census carry a comparison that goes stale the moment it is re-pinned again, which
is the OI-330 shape.  So the census stays what it is, and the movement is published beside it.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  DERIVED   both readings — the OUTGOING one from the git OBJECT of the commit that carried it,
            the INCOMING one from the artifact on disk; every movement, at four units of identity;
            the class of every movement, from the tree itself.
  AUTHORED  the two commits being compared, and the three class NAMES the ruling gives.  No
            movement is placed by hand: a movement the derivation cannot class is a STOP.

THE FOUR UNITS OF IDENTITY, so a movement is a thing rather than a diff line.  A byte diff of the
two artifacts runs to tens of thousands of lines, almost all of it one naming per line, and a
count of lines says nothing about what changed.  The units are:

  1. NAMING            — a (flagged file, caller) pair from `who_does_the_naming`.
  2. CALLER KIND       — a caller and the kind the ruled reading derived for it.
  3. FLAGGED MEMBER    — a file in some candidacy's flagged population.
  4. CANDIDACY VERDICT — a candidacy and its verdict.

  Every scalar the census publishes — the verdict tally, the kind tally, the parsed-source count,
  the flagged population size — is a SUM over those units, so it is published as a movement with
  its own before/after and explicitly NOT classed: classing a sum would double-count the causes
  already carried by the units it sums.

THE THREE CLASSES, and the derivation of each — the ruling's own names.

  (iii) THE TREE'S ORDINARY GROWTH.  The movement's subject path was ADDED to, or REMOVED from,
        the tracked tree between the two measured commits.  Derived from `git diff --name-status`
        between them, both named by explicit hash.  This is the class the ruling names last and
        the one that carries most of the volume: new tools and new records name things.

  (i)   THE SPLIT'S EFFECT.  The subject is a naming that LEFT a governing file because the span
        carrying it was archived by the ruled governing-surface split — established by finding the
        naming's own line byte-present in that file's ARCHIVE COMPANION at the new commit.  This
        is finding F35 measured rather than asserted: archiving a span removes namings from the
        governing record, and retirement candidacy moves with them.

  (ii)  THE DISCARD'S RESIDUE.  The subject is a naming that left a RENDERED decisions-register
        surface because the fifth batch's soft-discard retired the entry carrying it — established
        by finding the naming's line byte-present in the register's own retired-entry surface at
        the new commit.

  A movement fitting none of the three is a STOP, which is the dispatch's own instruction.

★ WHAT THIS DOES NOT ESTABLISH, stated before its first use.  That a class is the movement's
CAUSE.  Each class is a derived RELATION between the movement and the tree — a path that appeared,
a line that is now in a companion — and a movement can satisfy one relation while another act
produced it.  The relations are tested in the order above and the first that holds is recorded
WITH its evidence, so a reader can check the placement rather than trust it.

Run:
  python tools/audit/gen_retirement_census_movement.py --outgoing <commit>   # measure and write
  python tools/audit/gen_retirement_census_movement.py --check              # re-derive
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output          # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

CENSUS = "tools/audit/retirement_caller_check.json"
OUT = os.path.join(HERE, "retirement_census_movement.json")

# AUTHORED — the commit whose git object carries the OUTGOING census. Task 1 of this dispatch,
# which is the last commit before the re-pin. An explicit hash, the only git read D-253 permits.
OUTGOING_COMMIT = "5c38b41166e79faeb8a539994dbee16290404f15"

GROWTH = "(iii) the tree's ordinary growth"
SPLIT = "(i) the split's effect"
DISCARD = "(ii) the discard's residue"

# AUTHORED — where an archived span went. The five parent/companion pairs the ruled split created
# or continued; a naming that left a parent and is byte-present in its companion left BY THAT ACT.
COMPANION = {
    "CLAUDE.md": "CLAUDE_ARCHIVE.md",
    "OPEN_ITEMS.md": "OPEN_ITEMS_ARCHIVE.md",
    "DECISIONS.md": "DECISIONS_ARCHIVE.md",
    "STATUS.md": "STATUS_ARCHIVE.md",
    "BUILD_AND_TEST.md": "BUILD_AND_TEST_ARCHIVE.md",
}

# AUTHORED — the rendered decisions-register surfaces, and the register data whose `retired_entries`
# block holds what the fifth batch's soft-discard took out of the LIVE record. That block's own
# words: "Nothing in this block is rendered into the register's INDEX or its group files: a retired
# entry has left the LIVE record, which is what the discard is." So a naming that left a rendered
# surface while its subject is still named inside that block left BY THAT ACT.
REGISTER_RENDERED = re.compile(r"^(DECISIONS\.md|decisions/group_[A-Z]+\.md)$")
REGISTER_DATA = "tools/audit/decisions/backbone_decisions.json"


class Stop(Exception):
    """A movement the derivation cannot class, or a premise it rests on that is not true."""


def git(*args: str) -> str:
    proc = subprocess.run(["git", "-C", ROOT, *args], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"git {' '.join(args[:2])} failed — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8", "replace")


def read(path: str) -> str:
    with open(os.path.join(ROOT, path), "r", encoding="utf-8", newline="") as fh:
        return fh.read()


HOLDERS = "★_every_surviving_holder_BY_KIND_and_the_question_DEFERRED_to_it"
KINDS = "★_the_caller_kind_classification"
UNDERIVABLE = "★_the_KIND_UNDERIVABLE_list_returning_to_the_user"


def holdings(census: dict) -> dict[tuple[str, str], str]:
    """Every SURVIVING holding naming — a (flagged file, holder) pair with the line it sits on."""
    out = {}
    for rows in census[HOLDERS]["holders_by_kind"].values():
        for r in rows:
            out[(r["flagged_file"], r["held_by"])] = r["the_line_the_naming_was_found_on"]
    return out


def caller_kinds(census: dict) -> dict[str, str]:
    return {r["caller"]: r["caller_kind"] for r in census["who_does_the_naming"]}


def flagged_members(census: dict) -> dict[str, str]:
    out = {}
    for row in census["candidacies"]:
        for member in row["every_member"]:
            out[member["path"]] = f"{row['candidacy']} / {member['member_verdict']}"
    return out


def verdicts(census: dict) -> dict[str, str]:
    return {row["candidacy"]: row["verdict"] for row in census["candidacies"]}


def scalars(census: dict) -> dict[str, object]:
    kinds = census[KINDS]
    return {
        "the_tally": census["the_tally"],
        "the_kind_tally": kinds["the_kind_tally"],
        "tracked_python_sources_parsed": kinds["tracked_python_sources_parsed"],
        "generators_whose_own_source_enumerates_the_tracked_tree":
            len(kinds["generators_whose_own_source_enumerates_the_tracked_tree"]),
        "KIND_UNDERIVABLE_callers_returning_to_the_user":
            len(kinds[UNDERIVABLE]["callers"]),
        "the_flagged_population_size": census["the_flagged_population_size"],
        "the_holder_kind_tally": census[HOLDERS]["the_holder_kind_tally"],
    }


def tree_delta(old_commit: str, new_commit: str) -> tuple[set[str], set[str]]:
    added, removed = set(), set()
    out = git("diff", "--name-status", "-z", old_commit, new_commit)
    fields = [f for f in out.split("\0") if f != ""]
    i = 0
    while i < len(fields) - 1:
        status, path = fields[i], fields[i + 1].replace("\\", "/")
        i += 2
        if status.startswith("A"):
            added.add(path)
        elif status.startswith("D"):
            removed.add(path)
        elif status.startswith("R"):
            # a rename carries a second path; the source is gone and the destination is new
            removed.add(path)
            if i < len(fields):
                added.add(fields[i].replace("\\", "/"))
                i += 1
    return added, removed


class Classifier:
    """The three ruled classes, derived from the tree. Nothing is placed by hand."""

    def __init__(self, added: set[str], removed: set[str],
                 old_commit: str, new_commit: str) -> None:
        self.added, self.removed = added, removed
        # BOTH sides are read at the commits the two READINGS were MEASURED at, never at the
        # working tree and never at the commit that happens to carry an artifact. A relation
        # between two measurements must be taken at the two trees they describe, or it is a
        # statement about a third tree neither of them is about.
        self.old_commit, self.new_commit = old_commit, new_commit
        self._companions: dict[str, str] = {}
        self._companions_before: dict[str, str] = {}
        self._retired: dict[str, str] = {}
        self._now: dict[str, str] = {}
        self._before: dict[str, str] = {}

    def companion_text(self, parent: str) -> str | None:
        name = COMPANION.get(parent)
        return None if name is None else self.text_now(name)

    def companion_text_before(self, parent: str) -> str:
        """The companion as it stood at the OUTGOING reading's own measured commit.

        This separates the two acts that archive a span of the same parent: the ruled split
        itself, and Ruling 3's residue move, which completes it under Ruling 4's own line. Both
        are the split's effect; which one did it is a fact worth publishing rather than blurring.
        """
        return self.text_before(COMPANION[parent])

    def text_now(self, path: str) -> str:
        if path not in self._now:
            try:
                self._now[path] = git("show", f"{self.new_commit}:{path}")
            except Stop:
                self._now[path] = ""
        return self._now[path]

    def text_before(self, path: str) -> str:
        if path not in self._before:
            try:
                self._before[path] = git("show", f"{self.old_commit}:{path}")
            except Stop:
                self._before[path] = ""
        return self._before[path]

    def named_in(self, path: str, files, commit_now: bool) -> bool:
        text = self.text_now if commit_now else self.text_before
        return any(path in text(f) for f in files)

    def left_the_governing_record(self, path: str) -> str | None:
        """Did this file stop being NAMED by the governing record because a span was archived?

        This is finding F35 measured rather than asserted: the citation split that decides which
        members of a mixed class are flagged is re-scanned at the governing record as it stands,
        so a file whose only naming sat inside an archived span crosses into the flagged
        population — and a crossing confers CANDIDACY only.
        """
        if not self.named_in(path, COMPANION, commit_now=False):
            return None
        if self.named_in(path, COMPANION, commit_now=True):
            return None
        if not self.named_in(path, COMPANION.values(), commit_now=True):
            return None
        return (f"`{path}` is NAMED by the governing record at the outgoing measured commit, is "
                f"named by none of the five governing files at the new one, and IS named in an "
                f"archive companion there — so its naming left the governing record with an "
                f"archived span (finding F35)")

    def entered_the_governing_record(self, path: str) -> str | None:
        if self.named_in(path, COMPANION, commit_now=False):
            return None
        if not self.named_in(path, COMPANION, commit_now=True):
            return None
        return (f"`{path}` is named by none of the five governing files at the outgoing measured "
                f"commit and IS named by one at the new one — the governing record grew to name "
                f"it")

    def retired_text(self) -> str:
        if "all" not in self._retired:
            data = json.loads(read(REGISTER_DATA))
            self._retired["all"] = json.dumps(data.get("retired_entries", {}),
                                              ensure_ascii=False)
        return self._retired["all"]

    @staticmethod
    def probe_of(line: str) -> str:
        """The naming line, made safe to search with.

        The census publishes a WINDOW around the naming and marks each cut end with an ellipsis,
        so a bare substring test fails on exactly the longest lines — which are the ones a
        governing document carries, every dated entry being one line of several thousand
        characters. Both ellipses are dropped and the window between them is searched.
        """
        probe = line.strip()
        if probe.startswith("..."):
            probe = probe[3:].lstrip()
        if probe.endswith("..."):
            probe = probe[:-3].rstrip()
        return probe

    def place(self, subject: str, direction: str, line: str | None,
              named: str | None = None) -> dict:
        """`subject` is the path the movement is about; `line` its naming text if it had one."""
        if direction == "added" and subject in self.added:
            return {"the_class": GROWTH,
                    "the_evidence": f"`{subject}` was ADDED to the tracked tree between the two "
                                    f"measured commits"}
        if direction == "removed" and subject in self.removed:
            return {"the_class": GROWTH,
                    "the_evidence": f"`{subject}` was REMOVED from the tracked tree between the "
                                    f"two measured commits"}
        if direction in ("added", "changed") and named and named in self.added:
            return {"the_class": GROWTH,
                    "the_evidence": f"the named file `{named}` was ADDED to the tracked tree "
                                    f"between the two measured commits"}
        if direction == "removed" and named and named in self.removed:
            return {"the_class": GROWTH,
                    "the_evidence": f"the named file `{named}` was REMOVED from the tracked tree "
                                    f"between the two measured commits"}
        if direction == "removed" and line:
            probe = self.probe_of(line)
            companion = self.companion_text(subject)
            if companion is not None and probe and probe in companion:
                before = self.companion_text_before(subject)
                which = ("the ruled split itself — the span was already in the companion at the "
                         "outgoing reading's own commit"
                         if probe in before else
                         "Ruling 3's residue move, which completes the same split under Ruling 4's "
                         "own line — the span reaches the companion only at the new commit")
                return {"the_class": SPLIT,
                        "the_evidence": f"the naming's own line is byte-present in "
                                        f"`{COMPANION[subject]}` at the new commit, so the span "
                                        f"carrying it was archived. Archived by: {which}",
                        "which_act_archived_it": which}
            if REGISTER_RENDERED.match(subject) and named and named in self.retired_text():
                return {"the_class": DISCARD,
                        "the_evidence": "the naming left a RENDERED register surface while its "
                                        "subject is still named inside the register data's "
                                        "`retired_entries` block, whose own words are that "
                                        "nothing in it is rendered into the INDEX or the group "
                                        "files — so the entry carrying the naming was retired by "
                                        "the soft-discard"}

        # A naming that ARRIVED in an archive companion arrived because a span was archived into
        # it. Tested before the growth relation below, so an archiving act is never reported as a
        # file that happened to grow.
        if direction == "added" and subject in COMPANION.values() and line:
            probe = self.probe_of(line)
            if probe and probe not in self.text_before(subject) \
                    and probe in self.text_now(subject):
                return {"the_class": SPLIT,
                        "the_evidence": f"the naming ARRIVED in the archive companion "
                                        f"`{subject}`: its line is byte-present there at the new "
                                        f"commit and absent at the outgoing reading's own commit, "
                                        f"so a span carrying it was archived into it"}

        # ★ THE GROWTH RELATION AT CONTENT LEVEL, and the one place it is deliberately NOT
        # available. A holder that is not itself a governing parent may gain or lose a naming
        # because its own text grew or shrank, which is ordinary. For one of the five governing
        # parents a LOST naming has exactly one admissible cause — the span went to the companion,
        # tested above — so this relation is withheld there and the movement STOPs instead. That
        # is the whole point of the STOP: a naming vanishing from the governing record with
        # nothing holding it is what a reader needs told.
        # A file that CROSSED the citation split — it stopped, or started, being named by the
        # governing record — takes its class from the crossing, and every naming that follows the
        # crossing takes it too. Tested before the growth relation so F35's effect is never
        # reported as a file that happened to grow.
        if named:
            why = (self.left_the_governing_record(named) if direction == "added"
                   else self.entered_the_governing_record(named))
            if why:
                return {"the_class": SPLIT if direction == "added" else GROWTH,
                        "the_evidence": why}

        if subject not in COMPANION and line:
            probe = self.probe_of(line)
            here_now, here_before = self.text_now(subject), self.text_before(subject)
            if direction == "added" and probe and probe in here_now and probe not in here_before:
                return {"the_class": GROWTH,
                        "the_evidence": f"`{subject}` gained the naming in its own text between "
                                        f"the two measured commits — the line is byte-present "
                                        f"there now and absent at the outgoing commit"}
            if direction == "removed" and probe and probe not in here_now \
                    and probe in here_before:
                return {"the_class": GROWTH,
                        "the_evidence": f"`{subject}` lost the naming from its own text between "
                                        f"the two measured commits — the line is byte-present "
                                        f"there at the outgoing commit and absent now"}
        return {}


def movements(old: dict, new: dict, cls: Classifier) -> tuple[list[dict], list[dict]]:
    rows, unclassed = [], []

    def add(unit: str, identity: str, direction: str, subject: str,
            before, after, line: str | None = None, named: str | None = None,
            extra: dict | None = None) -> None:
        placed = cls.place(subject, direction, line, named)
        rec = {"the_unit": unit, "the_identity": identity, "the_direction": direction,
               "the_subject_path": subject, "before": before, "after": after}
        if extra:
            rec.update(extra)
        if placed:
            rec.update(placed)
            rows.append(rec)
        else:
            unclassed.append(rec)

    old_n, new_n = holdings(old), holdings(new)
    for key in sorted(set(old_n) - set(new_n)):
        add("HOLDING NAMING", f"{key[0]} held by {key[1]}", "removed", key[1], "holds",
            "does not hold", line=old_n[key], named=key[0])
    for key in sorted(set(new_n) - set(old_n)):
        add("HOLDING NAMING", f"{key[0]} held by {key[1]}", "added", key[1], "does not hold",
            "holds", line=new_n[key], named=key[0])

    old_m, new_m = flagged_members(old), flagged_members(new)
    for path in sorted(set(old_m) - set(new_m)):
        add("FLAGGED MEMBER", path, "removed", path, old_m[path], None, named=path)
    for path in sorted(set(new_m) - set(old_m)):
        add("FLAGGED MEMBER", path, "added", path, None, new_m[path], named=path)
    for path in sorted(set(old_m) & set(new_m)):
        if old_m[path] != new_m[path]:
            add("FLAGGED MEMBER", path, "changed", path, old_m[path], new_m[path], named=path)

    # ★ CALLER KIND is placed LAST and by INHERITANCE, because a caller's kind does not move on
    # its own: it appears or vanishes because that caller started or stopped naming a flagged
    # file, and those namings are already placed above. Inheriting the class they carry keeps the
    # placement derived rather than authored a second time — and a caller whose namings carry no
    # single class, or none at all, is left unplaced and STOPs.
    by_caller: dict[tuple[str, str], set[str]] = {}
    for rec in rows:
        if rec["the_unit"] == "HOLDING NAMING":
            by_caller.setdefault((rec["the_subject_path"], rec["the_direction"]),
                                 set()).add(rec["the_class"])

    by_member: dict[tuple[str, str], str] = {
        (rec["the_subject_path"], rec["the_direction"]): rec["the_class"]
        for rec in rows if rec["the_unit"] == "FLAGGED MEMBER"}

    def add_kind(caller: str, direction: str, before, after) -> None:
        rec = {"the_unit": "CALLER KIND", "the_identity": caller, "the_direction": direction,
               "the_subject_path": caller, "before": before, "after": after}
        side = direction if direction != "changed" else "added"

        placed = cls.place(caller, direction, None, None)
        if placed:
            rec.update(placed)
            rows.append(rec)
            return

        classes = set(by_caller.get((caller, side), set()))
        inherited_from = "this caller's own namings"
        if not classes:
            # A caller whose namings HOLD nothing — an enumerator, or a record published as data —
            # has no holding naming to inherit from. It entered or left the caller table because a
            # MEMBER crossed the flagged population, so the class is inherited from the members it
            # names, which is derived at the caller's own text rather than assumed.
            text = cls.text_now(caller) if side == "added" else cls.text_before(caller)
            # The census's OWN definition of a reference is a BASE-NAME match, so the inheritance
            # uses it too rather than a stricter path match — a stricter test here would fail to
            # find the very naming that put the caller in the table (#6, the test is imported in
            # substance rather than re-decided).
            classes = {klass for (path, d), klass in by_member.items()
                       if d == side and os.path.basename(path) in text}
            inherited_from = ("the flagged members this caller's own text names, by the census's "
                              "own base-name reference test")
        if classes:
            # ★ A MIXED INHERITANCE IS RECORDED, NEVER RESOLVED BY PREFERENCE. A caller can enter
            # or leave the table for more than one reason at once, and the placement then takes
            # the class that comes FIRST in the ruling's own order — split, discard, growth, which
            # runs from the specific cause to the general one — while EVERY class it inherits is
            # published beside the verdict. Counting it once keeps the tally a partition; printing
            # all of them keeps the mixture visible, which a single label would hide.
            rec["the_class"] = next(k for k in (SPLIT, DISCARD, GROWTH) if k in classes)
            rec["the_evidence"] = (f"inherited from {inherited_from} — a caller's kind appears or "
                                   f"vanishes with the namings that put it in the table")
            if len(classes) > 1:
                rec["★_it_inherits_more_than_one_class"] = sorted(classes)
                rec["★_why_this_one"] = ("the ruling's own order runs from the specific cause to "
                                         "the general, so a movement with a specific cause among "
                                         "its causes is not merely growth; every class it "
                                         "inherits is published above")
            rows.append(rec)
        else:
            rec["what_it_could_inherit_from_carries"] = sorted(classes)
            unclassed.append(rec)

    old_k, new_k = caller_kinds(old), caller_kinds(new)
    for caller in sorted(set(old_k) - set(new_k)):
        add_kind(caller, "removed", old_k[caller], None)
    for caller in sorted(set(new_k) - set(old_k)):
        add_kind(caller, "added", None, new_k[caller])
    for caller in sorted(set(old_k) & set(new_k)):
        if old_k[caller] != new_k[caller]:
            add_kind(caller, "changed", old_k[caller], new_k[caller])

    old_v, new_v = verdicts(old), verdicts(new)
    for candidacy in sorted(set(old_v) | set(new_v)):
        if old_v.get(candidacy) != new_v.get(candidacy):
            add("CANDIDACY VERDICT", candidacy, "changed", candidacy,
                old_v.get(candidacy), new_v.get(candidacy))

    return rows, unclassed


def build() -> dict:
    new = json.loads(read(CENSUS))
    old = json.loads(git("show", f"{OUTGOING_COMMIT}:{CENSUS}"))
    old_at, new_at = old["measured_at_commit"], new["measured_at_commit"]
    if old_at == new_at:
        raise Stop(f"both readings are measured at {old_at[:10]} — there is no re-pin to report")

    added, removed = tree_delta(old_at, new_at)
    cls = Classifier(added, removed, old_at, new_at)
    rows, unclassed = movements(old, new, cls)
    if unclassed:
        # The STOP prints the unplaced records WHOLE. A halt that names a count and five
        # identities sends the next session hunting for what it already knew; the record is what
        # a reader needs to decide whether a fourth class exists or a relation is too narrow.
        head = json.dumps(unclassed[:10], indent=1, ensure_ascii=False)
        raise Stop(f"{len(unclassed)} movement(s) fit none of the three ruled classes — the "
                   f"dispatch's own instruction is a STOP-and-report. The first ten, whole, with "
                   f"the newly flagged members for comparison "
                   f"{sorted(set(flagged_members(new)) - set(flagged_members(old)))}:\n{head}")

    by_class: dict[str, dict[str, int]] = {}
    for rec in rows:
        cell = by_class.setdefault(rec["the_class"], {})
        cell[rec["the_unit"]] = cell.get(rec["the_unit"], 0) + 1

    old_s, new_s = scalars(old), scalars(new)
    moved_scalars = {k: {"before": old_s[k], "after": new_s[k]}
                     for k in old_s if old_s[k] != new_s[k]}

    return {
        "what_this_is":
            "WHAT MOVED IN THE RETIREMENT CALLER-CHECK WHEN IT WAS RE-PINNED, at four units of "
            "identity, with every movement placed in one of the three classes the ruling names "
            "and a STOP on any that fits none. A COMPARISON ONLY: it archives, moves, renames and "
            "deletes nothing, and it moves no verdict — a census crossing confers CANDIDACY only. "
            "Every figure here is computed; none is transcribed (D-431).",
        "generated_by": "tools/audit/gen_retirement_census_movement.py",
        "dispatch": "cc_instruction_preparation_seventh.md, Task 2",
        "the_ruling": "Ruling 2 of cowork_rulings_2026_08_17_sixth_return.md: the census is "
                      "regenerated fresh at this task's own commit, every movement published and "
                      "classed — the split's effect, the discard's residue, and the tree's "
                      "ordinary growth separated — and the artifact re-pinned there.",
        "the_outgoing_reading": {
            "measured_at_commit": old_at,
            "read_from_the_git_object_at": OUTGOING_COMMIT,
        },
        "the_incoming_reading": {"measured_at_commit": new_at},
        "★_what_the_classes_are_and_are_not":
            "Each class is a derived RELATION between a movement and the tree — a path that "
            "appeared or vanished, a naming's line now sitting in an archive companion or in the "
            "register's retired records. A relation is evidence about a movement's origin, not "
            "proof of its cause, and the relations are tested in a fixed order with the first "
            "that holds recorded WITH its evidence, so a placement can be checked rather than "
            "trusted.",
        "the_units_of_identity": {
            "HOLDING NAMING": "a (flagged file, holder) pair — a naming that HOLDS the file, with "
                              "the line it was found on",
            "CALLER KIND": "a caller and the kind the ruled reading derived for it",
            "FLAGGED MEMBER": "a file in some candidacy's flagged population, with its member "
                              "verdict",
            "CANDIDACY VERDICT": "a candidacy and its verdict",
        },
        "the_tree_delta_between_the_two_measured_commits": {
            "paths_added": len(added),
            "paths_removed": len(removed),
            "how": "git diff --name-status between the two measured commits, both named by "
                   "explicit hash",
        },
        "movements": len(rows),
        "movements_by_class": by_class,
        "movements_that_fit_none_of_the_three": len(unclassed),
        "★_the_scalars_that_moved_are_published_and_NOT_classed":
            "Every scalar below is a SUM over the units above, so its movement is already "
            "accounted for by the itemized movements that produced it. Classing it as well would "
            "count the same cause twice.",
        "the_scalars_that_moved": moved_scalars,
        "★_the_KIND_UNDERIVABLE_population_at_the_new_pin": {
            "the_ruling": "A census crossing confers CANDIDACY only — every ruled condition on "
                          "candidacies stands untouched, and no fate moves by this artifact.",
            "count": new_s["KIND_UNDERIVABLE_callers_returning_to_the_user"],
            "callers": [c["caller"] for c in new["★_the_caller_kind_classification"]
                        ["★_the_KIND_UNDERIVABLE_list_returning_to_the_user"]["callers"]],
        },
        "the_movements": rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="re-derive; do not write")
    args = ap.parse_args()

    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if args.check:
        try:
            with open(OUT, "r", encoding="utf-8") as fh:
                committed = fh.read()
        except FileNotFoundError:
            print(f"FAIL: {os.path.relpath(OUT, ROOT)} does not exist")
            return 1
        if committed != text:
            print(f"FAIL: the census movement does not re-derive: {os.path.relpath(OUT, ROOT)}")
            return 1
        print("the retirement-census movement re-derives")
    else:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  movements: {art['movements']}, unclassed: "
          f"{art['movements_that_fit_none_of_the_three']}")
    for name, cell in sorted(art["movements_by_class"].items()):
        print(f"  {name}: " + ", ".join(f"{k} {v}" for k, v in sorted(cell.items())))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
