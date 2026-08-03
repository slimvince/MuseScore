#!/usr/bin/env python3
"""Triage every `CLAUDE.md` rule as MECHANISM or KNOWLEDGE — a PROPOSAL, executed nowhere.

WHAT THIS IS.  Mechanism 4 of the phase-1p wave
(`cc_instruction_phase1p_home_rulings_and_mechanisms.md` §6.4): classify every process rule in
`CLAUDE.md` as something a mechanism can enforce or something a reader must understand, and
treat "could be a mechanism and is not" as a DEFECT.

WHAT IT DOES NOT DO.  It retires nothing and changes nothing.  The dispatch is explicit:
execute only where the replacement mechanism exists and passes IN THE SAME COMMIT; for
everything else produce the triage as a proposal and stop, because retiring ratified text is a
change to what the governing document says and that is the user's.  Nothing in this tool edits
`CLAUDE.md`.

THE POPULATION IS DERIVED, NOT CHOSEN (protocol P1, and #17f).  It is every register entry whose
home is `CLAUDE.md` — the register having enumerated that document in full — so no rule can be
left out by a search that did not think to look for it.  Only the CLASS of each rule is
authored, with its ground.

THE THREE CLASSES.
  MECHANISM-EXISTS      a mechanism already enforces it, or enforces a stated part of it; the
                        mechanism is named, and where it covers only part, the part is stated.
  MECHANISABLE-AND-NOT  a mechanical form exists that would catch real violations without
                        firing on legitimate work, and nothing implements it. **This is the
                        defect class**, and its members are rowed.
  KNOWLEDGE             it governs a judgment. Any mechanical form would either miss the point
                        of the rule or fire on legitimate work — and a guard that fires on
                        legitimate work gets switched off, which is worse than none.

Run:  python tools/audit/claude_md_rule_triage.py [--check]
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BACKBONE = os.path.join(HERE, "decisions", "backbone_decisions.json")
OUT = os.path.join(HERE, "claude_md_rule_triage.json")

EXISTS, OWED, KNOWLEDGE = "MECHANISM-EXISTS", "MECHANISABLE-AND-NOT", "KNOWLEDGE"

# AUTHORED — the class per rule, and the mechanism or the ground.
TRIAGE: dict[str, tuple[str, str]] = {
    "D-112": (EXISTS, "PARTIAL. `tools/audit/process_check.py` flags a claim about the code "
                      "carrying no `file:line`, which is the shape a from-memory assertion "
                      "arrives in. It cannot tell a wrong recollection from a right one."),
    "D-113": (OWED, "A word-list check over user-facing text: the twenty collided words are "
                    "enumerated in the rule itself, and the convention is mechanical — the "
                    "BARE word carries the musical sense, every non-musical use is qualified. "
                    "A check would flag a bare `score`, `key`, `measure` or `instrument` used "
                    "in the non-musical sense. Nothing implements it."),
    "D-115": (EXISTS, "`tools/robust_stop_diff.py` — the class-(b) duration non-increase per "
                      "preset, exit 0 only if every preset passes."),
    "D-165": (KNOWLEDGE, "What counts as established fact or published theory is a judgment."),
    "D-166": (KNOWLEDGE, "Whether a question is the specific open one is a judgment."),
    "D-167": (KNOWLEDGE, "Recognising a surprise is the judgment; a mechanism cannot."),
    "D-168": (KNOWLEDGE, "A goal, not a checkable condition."),
    "D-169": (KNOWLEDGE, "Whether facts are scarce is a judgment."),
    "D-170": (KNOWLEDGE, "Duplicate-detection tooling would flag ordinary similarity; what "
                         "counts as one concern is the judgment the rule is about."),
    "D-171": (KNOWLEDGE, "Layer membership of a method is a design judgment."),
    "D-172": (KNOWLEDGE, "Whether a change is inference-problem-driven is a judgment."),
    "D-173": (EXISTS, "PARTIAL. `run_bach_preset.py` exits nonzero on an incomplete corpus and "
                      "`characterise_bir_false.validate_corpus_dir` refuses a dir whose "
                      "manifest or fingerprints do not match — staleness is mechanical; "
                      "accuracy is not."),
    "D-174": (EXISTS, "PARTIAL. `gen_decisions_register.py --check`, "
                      "`gen_cluster_dispositions.py --verify` and "
                      "`tools/open_items_split_check.py` hold three surfaces to their data. "
                      "Specification prose against code is not covered."),
    "D-175": (EXISTS, "`composing_tests`, `notation_tests` and `pipeline_snapshot_tests` "
                      "against pinned goldens."),
    "D-176": (KNOWLEDGE, "Recognising the surprise is the act; the rule governs what to do "
                         "once it is recognised."),
    "D-177": (KNOWLEDGE, "Whether a change alters behavior is what the test suites answer; "
                         "whether it was ratified is not a property of the diff."),
    "D-178": (KNOWLEDGE, "What the full output surface is differs per change."),
    "D-179": (EXISTS, "`tools/robust_stop/manifest.json` with `tools/robust_stop_restamp.py`, "
                      "which regenerates every recorded figure from the candidate summary and "
                      "is established by reproducing the outgoing manifest exactly."),
    "D-180": (KNOWLEDGE, "The premise ledger, the written prediction and the desk simulation "
                         "are acts of reasoning; a mechanism can check that the artifacts "
                         "exist, which is not the same as checking that they were done."),
    "D-181": (KNOWLEDGE, "Whether a premise is load-bearing is a judgment."),
    "D-182": (EXISTS, "PARTIAL, and by instance rather than centrally: each measurement tool "
                      "carries its own `--establish` or `--check` "
                      "(`tools/a8_rebaseline_measure.py`'s self-validation, "
                      "`process_check.py --establish`, `shell_read_guard.py --establish`). "
                      "Nothing checks that a NEW tool has one."),
    "D-183": (KNOWLEDGE, "Which data helped fit a value is known to the fitter, not to a "
                         "checker outside it."),
    "D-184": (KNOWLEDGE, "Measuring annotator agreement is work, not a check."),
    "D-185": (KNOWLEDGE, "Whether a gate's declared protocol covers the largest change it will "
                         "meet is a judgment about the future."),
    "D-186": (KNOWLEDGE, "Declaring and bounding a migration is a design act."),
    "D-187": (OWED, "A check that a reported comparison between two measured quantities "
                    "carries an interval. `process_check.py` has the adjacent half — it flags "
                    "a bare quantity — but not the comparison-without-uncertainty shape, which "
                    "is one of the eight recorded instances it MISSES only because it was not "
                    "asked to look for it as such."),
    "D-188": (KNOWLEDGE, "Recording what the unconstrained best alternative is, is authorship."),
    "D-189": (KNOWLEDGE, "Which stage a piece of work is at is a judgment."),
    "D-190": (KNOWLEDGE, "Weighing designs is the judgment the rule constrains."),
    "D-191": (EXISTS, "`tools/robust_stop_diff.py` — the class-(a)/(b) split, with the "
                      "class-(a) INVESTIGATE flag at its declared threshold."),
    "D-192": (OWED, "A pre-commit check: a diff that touches a scoring term in "
                    "`chordanalyzer.cpp` must also touch `docs/scoring_model.md`. The rule "
                    "states the condition in exactly that form, and the staleness check it "
                    "names — the template count in §2 against `kTemplateCount` — is arithmetic. "
                    "Nothing implements either."),
    "D-193": (KNOWLEDGE, "Qualified predicates and defined terms are properties of prose."),
    "D-194": (OWED, "WEAK but real: a check for newly introduced identifiers of the shape a "
                    "private numbering scheme takes, against the labels the repository already "
                    "uses. It would flag candidates for a reader, not decide them."),
    "D-195": (EXISTS, "The register's `rationale` field, and the generated count of decisions "
                      "whose defense the record does not state — a gap that cannot be hidden "
                      "because the figure is computed."),
    "D-196": (EXISTS, "NEW at phase 1p, and only for the document half: "
                      "`tools/audit/process_check.py` reports a missing self-check section "
                      "(D-434). Whether the check was actually run over the diff is not "
                      "mechanical."),
    "D-197": (OWED, "Grouped with D-198, D-199 and D-316: a check that each recorded local "
                    "patch is still present in the file it patches. All four are stated as "
                    "do-not-revert against a dependency update, which is precisely the silent "
                    "failure a check catches and a reader does not. **This is the strongest "
                    "candidate in the owed set.**"),
    "D-198": (OWED, "See D-197 — the same check covers all four local patches."),
    "D-199": (OWED, "See D-197 — the same check covers all four local patches."),
    "D-200": (KNOWLEDGE, "A sequencing rule about when a trade-off may be considered."),
    "D-203": (KNOWLEDGE, "A ruling about what another rule permits."),
    "D-204": (KNOWLEDGE, "Whether two faults share a cause is the diagnosis itself."),
    "D-210": (EXISTS, "`compare_rn._our_key_tonic` — the one shared reduction every graded "
                      "surface routes through."),
    "D-211": (EXISTS, "The dual key column, carried by the measurement tooling wherever the "
                      "key column appears."),
    "D-212": (EXISTS, "`compare_rn._our_key_ident` for the one abstain decision, and "
                      "`robust_stop_diff.py`'s flag on any rise in the abstain rate."),
    "D-230": (OWED, "The same-commit half: a check that a commit touching a ruling surface "
                    "also touches `backbone_decisions.json`. The mandatory-read half is not "
                    "mechanisable."),
    "D-231": (KNOWLEDGE, "Which phase the work is in is a judgment."),
    "D-249": (KNOWLEDGE, "Whether the user has actually seen a surface is not a property of "
                         "any file."),
    "D-253": (OWED, "NEW at phase 1p, and it is BUILT BUT NOT ARMED, which keeps it in the "
                    "defect class. `tools/audit/shell_read_guard.py` is committed and "
                    "established; arming it means one block in `.claude/settings.json`, which "
                    "`.gitignore:112` puts OUTSIDE the record — a live control existing only "
                    "in an untracked file is the OI-285 class. It would cover the "
                    "TEXT-UTILITY half only, for sessions in this directory; the "
                    "branch-tip/index half is deliberately not enforced, and coverage of the "
                    "writing side is not established."),
    "D-254": (KNOWLEDGE, "Recognising that a step could be measured first is the judgment."),
    "D-294": (EXISTS, "PARTIAL. The variant-(b) DCML-only unit is the mechanism — the graded "
                      "surface reads the human annotation and nothing else. That no "
                      "self-annotation enters a measurement is not separately checked."),
    "D-308": (OWED, "The corpus manifest could carry an explicit tier, and the gate tooling "
                    "could refuse to measure against material not marked gate-tier. The rule "
                    "names exactly that condition, and nothing enforces it — a newly arrived "
                    "corpus is kept out of the gate by discipline alone."),
    "D-316": (OWED, "See D-197 — the same check covers all four local patches."),
    "D-430": (EXISTS, "`tools/audit/decisions/gen_section_homes.py --check` re-derives every "
                      "staged section home from its document's own headings."),
    "D-432": (EXISTS, "MEASUREMENT ONLY, and deliberately: "
                      "`tools/audit/decisions/gen_phase1p_delegation_bar.py` grades every "
                      "delegation and reports what the bar would move. It applies nothing — "
                      "the application is stopped at `OPEN_ITEMS.md` OI-291."),
    "D-433": (EXISTS, "Same tool as D-432; the shelving question never enters its verdict, "
                      "which is what the ruling says."),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    b = json.loads(open(BACKBONE, encoding="utf-8").read())
    rules = [e for e in b["decisions"]
             if e["home"].split(":")[0].replace("\\", "/") == "CLAUDE.md"]
    rules.sort(key=lambda e: int(e["id"].split("-")[1]))

    missing = [e["id"] for e in rules if e["id"] not in TRIAGE]
    if missing:
        raise SystemExit(f"CLAUDE.md rule(s) with no authored triage: {missing}")
    extra = sorted(set(TRIAGE) - {e["id"] for e in rules})
    if extra:
        raise SystemExit(f"triage for a rule that is not homed in CLAUDE.md: {extra}")

    rows, tally = [], collections.Counter()
    for e in rules:
        cls, ground = TRIAGE[e["id"]]
        tally[cls] += 1
        rows.append({"id": e["id"], "title": e["title"], "home": e["home"],
                     "nonspec_kind": e.get("nonspec_kind"),
                     "class": cls, "mechanism_or_ground": ground})

    owed = [r for r in rows if r["class"] == OWED]
    artifact = {
        "purpose": "Mechanism 4 of phase 1p: every CLAUDE.md rule classified MECHANISM or "
                   "KNOWLEDGE. A PROPOSAL — nothing here is executed, and this tool does not "
                   "edit CLAUDE.md. Retiring ratified text is a change to what the governing "
                   "document says, and that is the user's.",
        "population_derivation": "Every register entry whose home is CLAUDE.md, taken from "
                                 "tools/audit/decisions/backbone_decisions.json. The register "
                                 "enumerated that document in full, so the population is "
                                 "derived rather than searched for (protocol P1).",
        "classes": {
            EXISTS: "a mechanism already enforces it, or a stated part of it",
            OWED: "a mechanical form exists and nothing implements it — THE DEFECT CLASS",
            KNOWLEDGE: "it governs a judgment; any mechanical form would miss the point or "
                       "fire on legitimate work",
        },
        "totals": dict(tally),
        "rules_total": len(rows),
        "the_defect_set": {
            "count": len(owed),
            "rowed_at": "OPEN_ITEMS.md OI-292",
            "ids": [r["id"] for r in owed],
            "strongest_candidate": "D-197/D-198/D-199/D-316 — the four local patches. All four "
                                   "are stated as do-not-revert against a dependency update, "
                                   "which is a silent failure a check catches and a reader "
                                   "does not.",
        },
        "what_was_executed": "NOTHING. No CLAUDE.md text was retired. Two mechanisms were "
                             "BUILT in this wave and are recorded above against the rules they "
                             "cover (D-196, D-253); neither let any prose be deleted, and that "
                             "is stated rather than glossed.",
        "rules": rows,
    }
    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE: claude_md_rule_triage.json does not re-derive")
            return 1
        print("the CLAUDE.md rule triage re-derives")
        return 0
    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(rows)} rules")
    for cls in (EXISTS, OWED, KNOWLEDGE):
        print(f"  {cls}: {tally[cls]}")
    print(f"  the defect set ({len(owed)}): {', '.join(r['id'] for r in owed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
