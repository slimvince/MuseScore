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
        "subject_name": "L2",
        # ── THE SUBJECT-SPECIFIC PROSE.  Moved here from render() on 2026-10-15 by
        #    `cc_instruction_l3_reading_file_2026_10_15.md` Task 2, so that a second subject can carry
        #    its own.  Every string below is the text render() wrote for L2 before the move, byte for
        #    byte; the proof is that `--subject l2 --check` passes before and after the move.
        "words_boot_pack": (
            "- **The boot pack** — the self-contained directory such a session opens at boot, and nothing",
            "  else.  L2's pack does not exist yet; its members are a later ruling.",
        ),
        "words_register_group": (
            "- **The register group** — the letter under which `DECISIONS.md` lists an entry.  It is a",
            "  property of the entry and decided no verdict.  Note that register group **E** is titled",
            "  *Layer 2 — the slicer* while this subject is called **L2**: they are different units in two",
            "  different numbering schemes (`ARCHITECTURE.md`'s Layer 1–6 and the framework's L0/L1/L2).",
        ),
        "charter_gloss": (
            "and it asks FOUR things at once: the",
            "tonality at each moment; where one harmony ends and the next begins; which sounding notes are",
            "chord tones and which elaborate; and what chord is read over each span.  The pilot subject asked",
            "only the second of these.  A verdict here is IN if the entry discloses the ruled answer to ANY of",
            "the four, in whole or in part.",
        ),
        "section_3": (
            "## 3. What this family protects, and what is not ruled for L2",
            "",
            "For the pilot, a separate ruling named one oracle passage the family protected.  **No ruling",
            "names an oracle passage for L2.** Ruling 81's own record states that the record was searched",
            "before it was taken and that no ruling reached L2's family; Ruling 81 rules that the pack",
            "carries a family derived over a criterion built from the charter, and stops there; and none of",
            "Rulings 82 to 89, which fix the criterion's terms, names one.  What the family protects is",
            "therefore the entries themselves: the recorded current answers to the four limbs, which are the",
            "IN rows below.  This file does not restate any of those answers beyond the one-sentence finding",
            "each row carries, and it does not invent an oracle.",
        ),
        "empty_terms_line": (
            "- the `ARCHITECTURE.md` passage term is **EMPTY** by ruling, and no identity is named by any "
            "ruling for this subject, so the named-identity term is **EMPTY**."),
        "bound_tail": (
            "  The keyword term is a plain substring match whose reach is UNMEASURED; an entry bearing on this "
            "subject in words none of the terms carry does not appear here at all, and the candidate list "
            "says so on itself.  A keyword can match inside a longer word; every such match is published "
            "with its context at `tools/audit/l2_candidate_list.json` → `the_candidates` → `matched_by`, and no "
            "keyword match was treated as a reason for IN."),
        "sizing_by_term": True,
        "test_intro": "From the pilot's own dispatch, with L2's four-limbed question in place of the pilot's one:",
        "test_in": (
            "- **IN** — a deriving session that read this entry would know, in whole or in part, what the",
            "  ruled answer to the charter question is.",
        ),
        "not_yet": (
            "- **No leak list.** The pilot's fourth list named entries the pack's generated members could not",
            "  render because their text pointed into the implementation.  A leak is found when a pack is",
            "  rendered, and L2's pack is not rendered until the family is ruled and its members are ruled.",
            "- **No derived cross-reference additions.** When a pack is built, every entry whose own text",
            "  quotes or cross-references a withheld identity is withheld with it, derived and published whole",
            "  and not ruled.  Ruling 84 (§3cm) bounds that derivation: it may ADD a withholding to an entry",
            "  you have not ruled on, and may NOT overturn a verdict you have ruled.  None exists for L2 yet.",
            "- **No withheld passages.** A passage is a cut inside a member the boot list quotes WHOLE.  L2's",
            "  boot list is not ruled, so there is no member to cut.",
            "- **The date each verdict carries.** Ruling 81 requires it.  The generator stamps every verdict",
            "  with one module constant at render time, which is the pilot's authoring date and would be false",
            "  for these; the gap is recorded as owed to the batch that builds L2's pack, and the authoring date",
            "  of every group block stands in the table's own heading comments meanwhile.",
        ),
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
                "the entries stating what the tonality does with a cadence vote (D-336, D-494) "
                "are withheld already.",
                "**Ruling 3.** D-453 is withheld because the same text settled the pilot's narrower "
                "question IN (Ruling 1 of `cowork_rulings_2026_08_22_withheld_family_sitting.md`) and "
                "cannot settle the superset question less; D-535 is admitted as the checking stage's "
                "own outcome, reporting no value and no rule, what it discloses about the tables "
                "being stated in full by the withheld D-525.",
            ),
        },
    },
    # ── L3, added 2026-10-15 by `cc_instruction_l3_reading_file_2026_10_15.md` Task 2 ─────────────
    # Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`: the lists are ruled one
    # per turn, as for L2, from a surface rendered from the table.  No `ruling` block: the lists are
    # not ruled, so the file renders as a reading surface FOR RULING.
    "l3": {
        "candidate_list": "tools/audit/l3_candidate_list.json",
        "out": "ratification_surfaces/cowork_withheld_family_l3_reading.md",
        "title": "The WITHHELD FAMILY for the L3 subject — put to the user for a ruling",
        "subject_name": "L3",
        "subject_in_plain_words": (
            "The read-off facts: given a settled tonal reading, where does each phrase end and how do "
            "phrases group into sections, what cadence stands at each phrase end and of what type, what "
            "is the chord symbol, what is the figured bass, and what is the harmonic rhythm?"),
        # Located on every run, as for L2.  L3's block labels its question `**Question:**` (L2's
        # carries `**Question, in one sentence:**`); the bold form occurs once, an italic restatement
        # later in the file does not match it.
        "charter_file": "FRAMEWORK.md",
        "charter_label": "**Question:** ",
        "charter_sentence": "given a settled tonal reading, what else does a harmonic analysis of this music say?",
        "charter_heading": "### L3 — The read-off facts",
        "criterion_rulings": (
            "Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` ruled that it reaches "
            "the whole design-intent class, and `cc_instruction_l3_criterion_write_2026_10_14.md` wrote it "
            "as a group term naming every group of the decisions register's own table."),
        "verdicts_authored": (
            "by Claude Code on 2026-10-14 under "
            "`cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md` Task 3, at each entry's own "
            "published verbatim and plain restatement in the candidate list, in the decisions register's "
            "own group order"),
        # The verdict pass wrote L3's groups in the register's own order; the lists keep it.
        "group_order": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Q", "S",
                        "T", "U"],
        "words_boot_pack": (
            "- **The boot pack** — the self-contained directory such a session opens at boot, and nothing",
            "  else.  L3's pack does not exist yet; its members are a later ruling.",
        ),
        "words_register_group": (
            "- **The register group** — the letter under which `DECISIONS.md` lists an entry.  It is a",
            "  property of the entry and decided no verdict.  Note that register group **F** is titled",
            "  *Layer 3 — key and mode* while this subject is called **L3**, and that register group **H**,",
            "  *Layer 5 and Layer 6 — function, cadence, grouping*, carries much of what the framework puts",
            "  at L3: they are different units in two different numbering schemes (`ARCHITECTURE.md`'s",
            "  Layer 1–6 and the framework's L0 to L3).",
        ),
        "charter_gloss": (
            "and the same block's **Publishes** line names the FIVE",
            "facts this layer reads off that settled reading: the cadence at each phrase end, with its type;",
            "the phrase and section grouping; the chord symbol — root pitch class, quality and bass note; the",
            "figured bass; and the harmonic rhythm.  L3 may not revise L2: the tonality, where one harmony",
            "gives way to the next, which sounding notes are chord tones, and the chord read over each span",
            "reach it settled.  A verdict here is IN if the entry discloses the ruled answer to how L3 reads",
            "off ANY of the five, in whole or in part.",
        ),
        "section_3": (
            "## 3. What this family protects, and what is not ruled for L3",
            "",
            "For the pilot, a separate ruling named one oracle passage the family protected.  **No ruling",
            "names an oracle passage for L3.** Ruling 1 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`",
            "rules that L3's pack carries a withheld family, and Ruling 2 that every design-intent entry is a",
            "candidate; neither names one.  What the family protects is therefore the entries themselves: the",
            "recorded current answers to how L3 reads off its five facts, which are the IN rows below.  This",
            "file does not restate any of those answers beyond the one-sentence finding each row carries, and",
            "it does not invent an oracle.",
        ),
        "empty_terms_line": (
            "- the home-document, keyword and `ARCHITECTURE.md` passage terms are **EMPTY**, and no identity "
            "is named by any ruling for this subject, so the named-identity term is **EMPTY**: the group term "
            "names every group of the decisions register's own table, so it alone reaches the whole "
            "design-intent class (Ruling 2)."),
        "bound_tail": (
            "  Every design-intent entry of the sort is a candidate, so none of that class is missing here; "
            "the rulings recorded only in a ruling record since the register's rule (c) was suspended are "
            "outside the sort as well, and the candidate list states that bound on itself."),
        "sizing_by_term": False,
        "test_intro": "From the pilot's own dispatch, with L3's five published facts (§2) in place of the pilot's one question:",
        "test_in": (
            "- **IN** — a deriving session that read this entry would know, in whole or in part, the ruled",
            "  answer to how L3 reads off ANY of its five facts (§2).",
        ),
        "not_yet": (
            "- **No leak list.** The pilot's fourth list named entries the pack's generated members could not",
            "  render because their text pointed into the implementation.  A leak is found when a pack is",
            "  rendered, and L3's pack is not rendered until the family is ruled and its members are ruled.",
            "- **No derived cross-reference additions.** When a pack is built, every entry whose own text",
            "  quotes or cross-references a withheld identity is withheld with it, derived and published whole",
            "  and not ruled.  Ruling 84 (§3cm of `cowork_rulings_2026_08_31_decision_surface_sitting.md`)",
            "  binds L3 as written (§2 of the L3 sitting record): an addition that would withhold an entry you",
            "  have ruled admitted is put to you as its own list rather than standing.  None exists for L3 yet.",
            "- **No withheld passages.** A passage is a cut inside a member the boot list quotes WHOLE.  L3's",
            "  boot list is not ruled, so there is no member to cut.",
            "- **The date each verdict carries.** Ruling 2 of the L3 sitting record requires it.  The",
            "  generator's per-subject verdict-date table carries no `l3` entry, and the generator STOPs when",
            "  it builds a subject with graded candidates and no date there; the date is owed to the batch that",
            "  builds L3's pack, and the authoring date of every group block (2026-10-14) stands in the table's",
            "  own heading comments meanwhile.",
        ),
        # The UNPLACED list's heading, corrected for this subject.  The shared heading cites D-658 for
        # making no recommendation; that requirement of D-658 is superseded (`CLAUDE.md`, Conventions,
        # the order of a decision surface's rules, step 8).  L2's ruled file keeps the shared heading.
        "unplaced_gloss": (
            "These could not be defended either way in one sentence at the entry's own verbatim, so "
            "they were not guessed.  Each row says what was read.  This file makes no recommendation on "
            "any of them; a recommendation, with its grounds, comes on the decision surface that puts this "
            "list to you (`CLAUDE.md`, Conventions, the order in which a decision surface's rules apply, "
            "step 5)."),
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
    order = spec.get("group_order", GROUP_ORDER)
    groups_present = [g for g in order if g in per_group]
    unknown_groups = sorted(set(per_group) - set(order))
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
    ruling = spec.get("ruling")
    if ruling:
        w(f"> **STATUS: RULED {ruling['date']} — the lists below are the RULED lists.** The ruling record is")
        w(f"> `{ruling['record']}`, three rulings, one per list.  Every verdict below is carried in")
        w("> `tools/audit/gen_derivation_boot_pack.py` → `VERDICTS[\"" + subject + "\"]` as ruled.  **No identity is")
        w(f"> withheld yet and no pack exists**: the withheld family is authored from LIST ONE only after {spec['subject_name']}'s")
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
    for line in spec["words_boot_pack"]:
        w(line)
    w("- **The withheld family** — the recorded decisions, documents and passages cut out of that pack")
    w("  for one subject, so that the answer the session is chartered to derive does not reach it.")
    w("- **A candidate** — a decisions-register entry the ruled criterion picked as possibly disclosing")
    w("  some part of that answer.  Being a candidate is not a judgment; the verdict is.")
    w("- **A verdict** — one of three words written against one candidate: **IN** (withhold it), **OUT**")
    w("  (admit it), **UNPLACED** (the entry's own text does not settle it).  Each carries a *finding* —")
    w("  what the entry's own text says — and a *reason* — why that makes it IN, OUT or UNPLACED.")
    for line in spec["words_register_group"]:
        w(line)
    w("")
    w("## 2. The subject the deriving session will derive, stated from scratch")
    w("")
    w(f"> **{spec['subject_in_plain_words']}**")
    w("")
    w(f"That is {spec['subject_name']}'s charter question, located on this run at `{spec['charter_file']}` under the heading")
    w(f"`{spec['charter_heading']}` — *\"{charter_one_line}\"* — {spec['charter_gloss'][0]}")
    for line in spec["charter_gloss"][1:]:
        w(line)
    if ruling:
        w("")
        w(ruling["test_note"])
    w("")
    for line in spec["section_3"]:
        w(line)
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
    if criterion["home_documents"]:
        w("- **its recorded home is one of these documents:** " + ", ".join(
            f"`{d}`" for d in criterion["home_documents"]) + ";")
    if criterion["keywords"]:
        w("- **any of its title, verbatim, plain restatement or search patterns contains one of these "
          f"{len(criterion['keywords'])} words or phrases:** " + ", ".join(
            f"*{k}*" for k in criterion["keywords"]) + ";")
    # The authored line below states the passage and named-identity terms EMPTY; a criterion that
    # carries either would make it false, so that is a STOP rather than a silently wrong sentence.
    if criterion["architecture_spans"] or criterion["always"]:
        raise Stop(f"CRITERION[{subject!r}] carries a passage or a named-identity term, which the "
                   f"authored empty-terms line does not describe")
    w(spec["empty_terms_line"])
    w("")
    pop = art["the_population"]
    w(f"**The population and the bound.** The class walked holds **{pop['design_intent_class']}** "
      f"design-intent entries of the sort artifact's **{pop['sort_entries_total']}**; the criterion "
      f"returned **{pop['candidates']}** candidates.  The population is the sort artifact's and NOT the "
      "decisions register's, so register entries outside it are reached by no term (D-661, #24)."
      + spec["bound_tail"])
    w("")
    total = sum(counted.values())
    w("**The candidates by register group, and the verdicts proposed in each:**")
    w("")
    if spec["sizing_by_term"]:
        sizing = art["the_sizing"]["by_register_group_and_term"]
        w("| group | register-group title | candidates | reached by the group term | by a keyword | by a home document | IN | OUT | UNPLACED |")
        w("|---|---|---|---|---|---|---|---|---|")
        for g in groups_present:
            s = sizing.get(g, {})
            n = sum(per_group[g].values())
            w(f"| {g} | {cell(boot_pack.group_title(g))} | {n} | {s.get('group', 0)} | {s.get('keyword', 0)} | "
              f"{s.get('home-document', 0)} | {per_group[g][boot_pack.VERDICT_IN]} | "
              f"{per_group[g][boot_pack.VERDICT_OUT]} | {per_group[g][boot_pack.VERDICT_UNPLACED]} |")
        w(f"| **all** | | **{total}** | | | | **{counted[boot_pack.VERDICT_IN]}** | "
          f"**{counted[boot_pack.VERDICT_OUT]}** | **{counted[boot_pack.VERDICT_UNPLACED]}** |")
    else:
        # One term only, so the candidate list sizes by group alone; its count must equal the
        # table's own, group by group, or the file would show the user two numbers for one thing.
        sizing = art["the_sizing"]["by_register_group"]
        if set(sizing) != set(per_group):
            raise Stop(f"the candidate list sizes groups {sorted(sizing)}, the verdict table grades "
                       f"groups {sorted(per_group)}")
        w("| group | register-group title | candidates | IN | OUT | UNPLACED |")
        w("|---|---|---|---|---|---|")
        for g in groups_present:
            n = sum(per_group[g].values())
            if sizing[g] != n:
                raise Stop(f"register group {g}: the candidate list's sizing says {sizing[g]}, the "
                           f"verdict table grades {n}")
            w(f"| {g} | {cell(boot_pack.group_title(g))} | {n} | {per_group[g][boot_pack.VERDICT_IN]} | "
              f"{per_group[g][boot_pack.VERDICT_OUT]} | {per_group[g][boot_pack.VERDICT_UNPLACED]} |")
        w(f"| **all** | | **{total}** | **{counted[boot_pack.VERDICT_IN]}** | "
          f"**{counted[boot_pack.VERDICT_OUT]}** | **{counted[boot_pack.VERDICT_UNPLACED]}** |")
    w("")
    w("## 5. The test each verdict was made against")
    w("")
    w(spec["test_intro"])
    w("")
    for line in spec["test_in"]:
        w(line)
    w("- **OUT** — the entry bears on another unit, and reading it tells the session nothing about that")
    w("  answer.  The reason says what it bears on instead.")
    w("- **UNPLACED** — the entry's own published text does not settle it.  The reason says what was read.")
    if ruling:
        w("")
        w(ruling["test_note"])
    w("")
    w("**Default nothing:** a verdict that could not be defended in one sentence at the entry's own")
    w("verbatim was recorded UNPLACED rather than guessed.  **Every verdict was written at the published")
    w("text** — the entry's verbatim and plain restatement in the candidate list — and no entry's home")
    w("document was opened to decide one; the register group and the LEGACY mark were forbidden to")
    w("decide anything, and the executing side's report states that they did not.")
    w("")
    for verdict in (boot_pack.VERDICT_IN, boot_pack.VERDICT_OUT, boot_pack.VERDICT_UNPLACED):
        heading, gloss = LIST_HEADINGS[verdict]
        if verdict == boot_pack.VERDICT_UNPLACED and "unplaced_gloss" in spec:
            gloss = spec["unplaced_gloss"]
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
    for line in spec["not_yet"]:
        w(line)
    w("")
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
        w(f"**The withheld family itself is authored from LIST ONE in a later act**, together with {spec['subject_name']}'s")
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
        w(f"together with {spec['subject_name']}'s pack members, which are a separate ruling.")
        w("")
    w("## 8. What the ruling does NOT do")
    w("")
    w("- **It boots no session and renders no pack.**")
    w("- **It moves no register entry and no status.** Withholding an entry from one pack says nothing")
    w("  about that entry's standing in `DECISIONS.md`.")
    w("- **It edits no governing document** and closes no open item.")
    w(f"- **It does not settle who derives**, nor {spec['subject_name']}'s boot-list members, nor the date mechanism.")
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
