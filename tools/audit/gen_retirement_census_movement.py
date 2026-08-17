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

# AUTHORED — the commit whose git object carries the OUTGOING census: the last commit before this
# re-pin, at which the artifact still holds the previous reading. An explicit hash, the only git
# read D-253 permits.
#
# ★ IT MOVES WITH EVERY RE-PIN, AND THE PREVIOUS VALUE IS RECORDED RATHER THAN OVERWRITTEN (#12).
# The seventh batch's Task 2 compared against `5c38b41166` (its own Task 1's commit, at which the
# census still held the reading measured at `6529d10ae4`). This batch's Task 3 compares against
# Task 2's commit below, at which the census still holds the reading measured at `5c38b41166`.
# The NINTH batch's Task 4 compares against Task 3's commit below, at which the census still holds
# the reading measured at `d499027a8c`.
OUTGOING_COMMIT = "15dfb0e1729c3d34bcef18ab37415909139c69a8"
OUTGOING_COMMIT_HISTORY = [
    {"dispatch": "cc_instruction_preparation_seventh.md, Task 2",
     "outgoing_commit": "5c38b41166e79faeb8a539994dbee16290404f15",
     "the_reading_it_carried_was_measured_at": "6529d10ae4"},
    {"dispatch": "cc_instruction_preparation_eighth.md, Task 3",
     "outgoing_commit": "b0b51ee657e2fb988a999215a4c2bef567958756",
     "the_reading_it_carried_was_measured_at": "5c38b41166"},
]

GROWTH = "(iii) the tree's ordinary growth"
SPLIT = "(i) the split's effect"
DISCARD = "(ii) the discard's residue"

# ★★ A FOURTH CLASS, ADDED 2026-08-17 FOR THE EIGHTH BATCH'S RE-PIN, AND DECLARED RATHER THAN
# TAKEN SILENTLY. The three classes above were authored for the SEVENTH batch's re-pin, whose
# causes were the split, the earlier discard and the tree's growth. THIS re-pin has a fourth cause
# and it is the act the batch was dispatched to perform: the census is regenerated under the four
# USER-RULED inputs of the 2026-08-17 callers sitting — the nine KIND-UNDERIVABLE callers ruled
# ENUMERATOR-class, and the ruling that a prose citation and a data-record naming hold nothing.
# A naming that stopped HOLDING for that reason is none of the three: it did not leave a governing
# file, it did not leave a rendered register surface, and neither it nor its caller left the tree.
#
# ★ IT IS DERIVED, NOT AUTHORED PER MOVEMENT, on the same shape as the other three: the relation
# is tested against the NEW census's OWN published fields, which name every such naming, with the
# ruled input that placed it quoted from the artifact. So a movement placed here can be checked at
# the artifact rather than trusted, and a movement the relation does not reach still STOPS.
RULED = "(iv) the callers sitting's ruled inputs"

# ★★ A FIFTH CLASS, ADDED 2026-08-17 FOR THE NINTH BATCH'S RE-PIN, AND DECLARED RATHER THAN TAKEN
# SILENTLY. Its dispatch names the cause in terms: the callers sitting ruled that a MANDATORY-READ
# OR BOOT LISTING HOLDS a retirement candidate, so changing the read regime moves what holds
# candidates. This batch changed it twice — Task 1 amended the open-items register's rule (a) so a
# session reads the derived gating answer and opens the INDEX when it needs a row, and Task 3
# demoted `BUILD_AND_TEST.md` from an unconditional session-start read to a conditional one.
#
# ★ IT IS DERIVED, NOT AUTHORED PER MOVEMENT, on the same shape as the other four: the relation is
# that the governing document's OWN NAMING LINES for the named file DIFFER between the two measured
# commits while the file was neither added to nor removed from the tree and is named at both. The
# before and after lines are published per movement, so a placement can be checked at the objects
# rather than trusted, and a movement the relation does not reach still falls through to the tests
# below and, failing all of them, still STOPS.
#
# ★ IT IS TESTED BEFORE THE GROWTH RELATION, and that ordering is finding F47's lesson applied
# rather than rediscovered: a broader relation that is TRUE OF a movement is not its cause, and the
# growth relation is broad enough to swallow this one.
#
# ★ AN EMPTY CLASS IS A MEASUREMENT AND IS PUBLISHED AS ONE. If no movement satisfies the relation,
# that is the finding — the read regime changed and moved no candidacy, because the files it
# re-classed are governing documents rather than retirement candidates — and it is published rather
# than left as the silence of a class nobody looked for.
READ_REGIME = "(v) the read-regime change"
READ_REGIME_SUBJECT = "CLAUDE.md"

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


RULED_NOTHING = "namings_whose_HOLDER_KIND_was_ruled_to_hold_nothing_published_not_dropped"
RULED_ENUMERATOR = "enumerator_namings_published_as_data_holding_nothing"
USER_RULED_MARK = "USER-RULED at the 2026-08-17 callers sitting"


def ruled_to_hold_nothing(census: dict) -> dict[tuple[str, str], str]:
    """Every (flagged file, caller) pair the callers sitting's inputs stopped from holding.

    Read from the NEW census's own published fields — the two the regeneration added and the one
    it already carried — so the relation is a fact about the artifact rather than a judgment here.
    """
    out: dict[tuple[str, str], str] = {}
    for row in census["candidacies"]:
        for member in row["every_member"]:
            for entry in member.get(RULED_NOTHING, []):
                out[(member["path"], entry["caller"])] = entry["why_it_holds_nothing"]
            for entry in member.get(RULED_ENUMERATOR, []):
                if entry.get("how_the_caller_kind_was_settled") == USER_RULED_MARK:
                    out[(member["path"], entry["caller"])] = (
                        USER_RULED_MARK + " (§1): the caller is one of the nine the derivation "
                        "could not place, ruled ENUMERATOR-class at its published reason, so its "
                        "namings are published as data and hold nothing")
    return out


def candidacy_of_member(census: dict) -> dict[str, str]:
    return {member["path"]: row["candidacy"]
            for row in census["candidacies"] for member in row["every_member"]}


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
                 old_commit: str, new_commit: str,
                 ruled_nothing: dict[tuple[str, str], str] | None = None) -> None:
        self.added, self.removed = added, removed
        self.ruled_nothing = ruled_nothing or {}
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

    def retired_text(self, when: str = "now") -> str:
        """The register's `retired_entries` block, at one of the two measured commits.

        ★ TAKEN AT THE COMMITS RATHER THAN AT THE WORKING TREE, AND THE REASON IS THE SAME ONE THE
        COMPANION SPLIT USES. The block now holds MORE THAN ONE retirement — the fifth batch's
        soft-discard and the eighth batch's residue discard — so a single read of the tree can say
        that a subject is retired but not BY WHICH ACT. Reading it at both measured commits
        separates them: a subject already in the block at the outgoing reading's own commit was
        retired by the earlier act; one that reaches it only at the new commit was retired by the
        later one.
        """
        if when not in self._retired:
            source = (self.text_now(REGISTER_DATA) if when == "now"
                      else self.text_before(REGISTER_DATA))
            try:
                data = json.loads(source) if source else {}
            except json.JSONDecodeError:
                data = {}
            self._retired[when] = json.dumps(data.get("retired_entries", {}), ensure_ascii=False)
        return self._retired[when]

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

    def read_regime_moved(self, named: str | None) -> dict | None:
        """Did the GOVERNING DOCUMENT's own naming lines for this file change between the two trees?

        The relation, stated so a placement can be checked rather than trusted: `CLAUDE.md` names
        the file at BOTH measured commits, and the SET of its lines that name the file DIFFERS
        between them. A file that entered or left the tree is excluded by the caller, and a file
        the governing document names at only one of the two commits is left to the relations that
        already answer that case. What a read-regime change looks like is exactly this: the file is
        still there, still named, and the line naming it has moved between a mandatory listing and
        a conditional one.
        """
        if not named:
            return None
        before_text = self.text_before(READ_REGIME_SUBJECT)
        after_text = self.text_now(READ_REGIME_SUBJECT)
        before = sorted(ln.strip() for ln in before_text.splitlines() if named in ln)
        after = sorted(ln.strip() for ln in after_text.splitlines() if named in ln)
        if not before or not after or before == after:
            return None
        return {
            "evidence": (f"`{READ_REGIME_SUBJECT}` names `{named}` at BOTH measured commits and "
                         f"the set of lines naming it DIFFERS between them, while the file was "
                         f"neither added to nor removed from the tracked tree — the shape a "
                         f"read-regime change makes. The two line sets are published beside this "
                         f"so the placement can be checked at the objects."),
            "before": before,
            "after": after,
        }

    def place(self, subject: str, direction: str, line: str | None,
              named: str | None = None) -> dict:
        """`subject` is the path the movement is about; `line` its naming text if it had one."""
        # ★ THE RULED RELATION IS TESTED FIRST, and only where the NEW census still PUBLISHES the
        # naming. A pair that appears in one of the ruled-nothing fields is one the scan still
        # finds and the ruling stopped from holding — so neither the caller nor the named file can
        # have left the tree, and there is no relation for it to compete with.
        if direction == "removed" and named is not None:
            why = self.ruled_nothing.get((named, subject))
            if why:
                return {"the_class": RULED,
                        "the_evidence": "the naming is still found at the new commit and is "
                                        "PUBLISHED in the new census beside the member it names — "
                                        "what changed is that it no longer HOLDS, by a ruled "
                                        f"input: {why}",
                        "the_ruled_input_that_placed_it": why}
        # ★ THE READ-REGIME RELATION IS TESTED BEFORE GROWTH (F47's lesson): the growth relation is
        # broad enough to be true of a read-regime movement without being its cause.
        regime = self.read_regime_moved(named)
        if regime is not None and named not in self.added and named not in self.removed:
            return {"the_class": READ_REGIME, "the_evidence": regime["evidence"],
                    "the_naming_lines_before": regime["before"],
                    "the_naming_lines_after": regime["after"]}
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
            # ★ THE FLAGGED FILE IS SOUGHT BY ITS BASE NAME, NOT BY ITS PATH, and the correction is
            # the census's own test rather than a widening invented here (#6): the census defines a
            # REFERENCE as a base-name match, and a register entry that names a measurement tool
            # writes the tool's name, not its directory. Measured rather than reasoned about — with
            # the path test this relation missed a naming that left `decisions/group_H.md` because
            # the entry carrying it (D-399, whose verbatim names the tool) was retired by this
            # batch's own Task 2, and the movement fell through to the content-level growth
            # relation, which is true of it and is not its cause.
            base = os.path.basename(named) if named else None
            if REGISTER_RENDERED.match(subject) and base and base in self.retired_text():
                which = ("the fifth batch's soft-discard — the subject was already inside the "
                         "retired block at the outgoing reading's own commit"
                         if base in self.retired_text("before") else
                         "THIS batch's Task 2, the residue sitting's discard — the subject reaches "
                         "the retired block only at the new commit")
                return {"the_class": DISCARD,
                        "the_evidence": "the naming left a RENDERED register surface while its "
                                        "subject is still named inside the register data's "
                                        "`retired_entries` block, whose own words are that "
                                        "nothing in it is rendered into the INDEX or the group "
                                        "files — so the entry carrying the naming was retired by "
                                        f"a soft-discard. Retired by: {which}",
                        "which_act_retired_it": which}

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
    member_candidacy = candidacy_of_member(new)

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

    # ★ A MEMBER VERDICT THAT MOVED BECAUSE ITS OWN HOLDINGS WERE RULED TO HOLD NOTHING INHERITS
    # THAT CLASS, and the inheritance is derived rather than authored: the member's holdings are
    # already placed above, so its own movement takes their class instead of being placed again.
    ruled_members = {path for (path, _caller) in cls.ruled_nothing}

    def add_member(path: str, direction: str, before, after) -> None:
        if direction == "changed" and path in ruled_members:
            rows.append({
                "the_unit": "FLAGGED MEMBER", "the_identity": path,
                "the_direction": direction, "the_subject_path": path,
                "before": before, "after": after, "the_class": RULED,
                "the_evidence": "its member verdict moved because the namings that held it were "
                                "ruled to hold nothing; each of those namings is placed above and "
                                "is still published beside this member in the new census",
            })
            return
        add("FLAGGED MEMBER", path, direction, path, before, after, named=path)

    old_m, new_m = flagged_members(old), flagged_members(new)
    for path in sorted(set(old_m) - set(new_m)):
        add_member(path, "removed", old_m[path], None)
    for path in sorted(set(new_m) - set(old_m)):
        add_member(path, "added", None, new_m[path])
    for path in sorted(set(old_m) & set(new_m)):
        if old_m[path] != new_m[path]:
            add_member(path, "changed", old_m[path], new_m[path])

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

    ruled_callers = {caller: why for (_member, caller), why in cls.ruled_nothing.items()}

    def add_kind(caller: str, direction: str, before, after) -> None:
        rec = {"the_unit": "CALLER KIND", "the_identity": caller, "the_direction": direction,
               "the_subject_path": caller, "before": before, "after": after}
        side = direction if direction != "changed" else "added"

        # ★ A KIND THAT *CHANGED* RATHER THAN APPEARED OR VANISHED CANNOT INHERIT FROM ONE SIDE.
        # The inheritance below reads the namings that put a caller INTO or OUT OF the table; a
        # caller whose kind moved while it kept naming the same files has no such naming, and the
        # seventh batch never met the case because no kind changed at that re-pin. Here nine did,
        # by the ruled input that changed them, so the class is taken from the same published
        # evidence that placed their namings — derived at the artifact, not authored here.
        if direction == "changed" and caller in ruled_callers:
            rec["the_class"] = RULED
            rec["the_evidence"] = ("this caller's kind moved by a ruled input, and the same input "
                                   "is published in the new census beside every naming of its "
                                   f"that stopped holding: {ruled_callers[caller]}")
            rec["the_ruled_input_that_placed_it"] = ruled_callers[caller]
            rows.append(rec)
            return

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
            rec["the_class"] = next(k for k in (RULED, SPLIT, DISCARD, GROWTH) if k in classes)
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

    # ★ A CANDIDACY VERDICT IS PLACED LAST AND BY INHERITANCE, for the reason the caller kind is:
    # a candidacy's verdict does not move on its own — it moves because its MEMBERS' verdicts did,
    # and those are already placed above. The classes its members carry are read off the rows just
    # written, so the placement stays derived; a mixed inheritance is recorded exactly as it is for
    # a caller kind, taking the ruling's own order from the specific cause to the general.
    by_member_class: dict[str, set[str]] = {}
    for rec in rows:
        if rec["the_unit"] == "FLAGGED MEMBER":
            candidacy = member_candidacy.get(rec["the_subject_path"])
            if candidacy:
                by_member_class.setdefault(candidacy, set()).add(rec["the_class"])

    old_v, new_v = verdicts(old), verdicts(new)
    for candidacy in sorted(set(old_v) | set(new_v)):
        if old_v.get(candidacy) == new_v.get(candidacy):
            continue
        rec = {"the_unit": "CANDIDACY VERDICT", "the_identity": candidacy,
               "the_direction": "changed", "the_subject_path": candidacy,
               "before": old_v.get(candidacy), "after": new_v.get(candidacy)}
        classes = by_member_class.get(candidacy, set())
        if classes:
            rec["the_class"] = next(k for k in (RULED, SPLIT, DISCARD, GROWTH) if k in classes)
            rec["the_evidence"] = ("inherited from the movements of this candidacy's own members — "
                                   "a candidacy's verdict appears or moves with the member "
                                   "verdicts that produce it")
            if len(classes) > 1:
                rec["★_it_inherits_more_than_one_class"] = sorted(classes)
                rec["★_why_this_one"] = ("the order runs from the specific cause to the general, "
                                         "so a movement with a specific cause among its causes is "
                                         "not merely growth; every class it inherits is published "
                                         "above")
            rows.append(rec)
        else:
            rec["what_it_could_inherit_from_carries"] = sorted(classes)
            unclassed.append(rec)

    return rows, unclassed


def build() -> dict:
    new = json.loads(read(CENSUS))
    old = json.loads(git("show", f"{OUTGOING_COMMIT}:{CENSUS}"))
    old_at, new_at = old["measured_at_commit"], new["measured_at_commit"]
    if old_at == new_at:
        raise Stop(f"both readings are measured at {old_at[:10]} — there is no re-pin to report")

    added, removed = tree_delta(old_at, new_at)
    cls = Classifier(added, removed, old_at, new_at, ruled_to_hold_nothing(new))
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
        "dispatch": "cc_instruction_preparation_eighth.md, Task 3; first run "
                    "cc_instruction_preparation_seventh.md, Task 2",
        "the_ruling": "Ruling 2 of cowork_rulings_2026_08_17_sixth_return.md: the census is "
                      "regenerated fresh at this task's own commit, every movement published and "
                      "classed — the split's effect, the discard's residue, and the tree's "
                      "ordinary growth separated — and the artifact re-pinned there. This run "
                      "carries it forward for the eighth batch's re-pin, which regenerates the "
                      "census under the four USER-RULED inputs of the 2026-08-17 callers sitting.",
        "the_outgoing_reading": {
            "measured_at_commit": old_at,
            "read_from_the_git_object_at": OUTGOING_COMMIT,
            "★_the_previous_comparisons_this_tool_made": OUTGOING_COMMIT_HISTORY,
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
        "★_every_class_this_tool_tests_including_the_ones_that_placed_nothing": {
            name: by_class.get(name, {}) for name in
            (SPLIT, DISCARD, GROWTH, RULED, READ_REGIME)
        },
        "★_why_an_empty_class_is_published_rather_than_omitted":
            "A class with no members is a MEASUREMENT — the relation was tested against every "
            "movement and held for none — and omitting it would make the absence of a cause "
            "indistinguishable from nobody having looked for it. `movements_by_class` above "
            "carries only what placed something, which is what a reader counts with; this field "
            "carries what was TESTED.",
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
