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
