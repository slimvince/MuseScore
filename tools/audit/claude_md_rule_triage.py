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

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

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
    # Both arrived in CLAUDE.md by READ WAVE 5's own act, 2026-08-04, and are triaged here so
    # this check's failure list does not widen by that act alone (the OI-319 shape).
    "D-557": (KNOWLEDGE, "The same judgment as D-172, which this rule is now the widened form "
                         "of: whether a change is inference-problem-driven, and whether the "
                         "refactoring and the architectural design are done, are both judgments. "
                         "(The two entries record ONE rule at ONE home after the widening, which "
                         "is OPEN_ITEMS.md OI-329.)"),
    "D-576": (KNOWLEDGE, "The rule governs how a reported figure is READ, not how it is "
                         "produced. Nothing a checker can inspect distinguishes a root figure "
                         "read with the caveat from one read without it."),
    # Arrived in CLAUDE.md by READ WAVE 6's own act, 2026-08-04 — the gate block's root-cause
    # attribution clause entered as its own entry — and triaged here so this check's failure
    # list does not widen by that act alone (the OI-319 shape, as with D-557 above).
    "D-638": (KNOWLEDGE, "An ATTRIBUTION of cause plus a prohibition on the wrong remedy: the "
                         "rotation churn belongs to the chord layer and is only surfaced by a "
                         "key change, so no key-layer change is the fix. Deciding that a "
                         "particular churn is symmetric-rotation churn rather than a functional "
                         "regression is the same judgment D-191's guardrails already place on a "
                         "reader — verified at the score, per case, defaulting to the barred "
                         "class on any doubt — and no mechanism can make it. What IS mechanical "
                         "is the consequence rather than the attribution: `tools/robust_stop_"
                         "diff.py` enforces the class-(b) non-increase this rule explains."),
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
    "D-193": (OWED, "SPLIT BY USER RULING, AND THE ENTRY IS IN THE DEFECT CLASS ON THE MECHANICAL "
                    "SUBSET ONLY (Rulings 28, 29 and 32 of 2026-08-09, "
                    "`cowork_rulings_2026_08_09_fifth_stop.md`). **The DEEP half is ruled "
                    "KNOWLEDGE and that limb CLOSES:** no mechanical test can decide whether a "
                    "two-place word names its argument without understanding the sentence, and a "
                    "noisy checker gets switched off, which is worse than none (D-473) — so "
                    "predicate discipline and prose quality remain the writer's method stated in "
                    "`cowork_design_doc_template.md`, the per-session self-check (D-434) and the "
                    "reading passes. **The MECHANICAL subset is ruled IN SCOPE and is not built:** "
                    "status-banner presence, terms-table presence on a new specification, and "
                    "section structure judged against the KIND LIST — the enumeration Ruling 28 "
                    "puts in `cowork_design_doc_template.md`, where a document of an unlisted kind "
                    "is a STOP rather than a silent pass. All three read a document's own "
                    "structure rather than its prose, which is why they fall on this side of the "
                    "line the deep half fails. THE MECHANISM IS NOT BUILT BY THOSE RULINGS: it "
                    "joins the D-436 mechanism backlog like every other member of this class, and "
                    "the split carries its own open-items row, OPEN_ITEMS.md OI-364. FORMER "
                    "CLASS, PRESERVED (#12): KNOWLEDGE, on the ground `Qualified predicates and "
                    "defined terms are properties of prose.` — which the ruling confirms for the "
                    "deep half and refutes for the three structural checks above."),
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
    "D-197": (EXISTS, "BUILT at phase 1q: `tools/audit/local_patches_check.py` verifies each "
                      "recorded patch is present at HEAD, deriving its patch list from "
                      "`CLAUDE.md`'s own section so a newly recorded patch is covered without a "
                      "code change, and STOPPING on a recorded patch it has no marker for. "
                      "Established at `tools/audit/local_patches_establishment.json` by "
                      "detecting deliberately unpatched content. PARTIAL for THIS entry: D-197 "
                      "is the FORK-LOCAL distribution constraint on D-199's patch, not a patch "
                      "of its own, and no check enforces a distribution constraint — a push is "
                      "the act it forbids."),
    "D-198": (EXISTS, "See D-197 — the same check covers the recorded patches. CLAUDE.md's "
                      "section carries THREE patch subsections; the four entries here include "
                      "D-197, which is a disposition rather than a patch."),
    "D-199": (EXISTS, "See D-197 — the same check covers the recorded patches."),
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
    "D-253": (OWED, "NEW at phase 1p; BUILT and ESTABLISHED then, ARMED by the user at phase "
                    "1r, WIDENED at phase 1s. It stays in the defect class on ONE ground, and "
                    "the ground is stated so it is not read as a backlog item: "
                    "`tools/audit/shell_read_guard.py` binds the EXECUTING side only — the "
                    "hook matcher names that side's shell tools and the writing side's carries "
                    "a different name — so the rule is enforced on one side and must not be "
                    "described as enforced. Two coverage limits closed 2026-08-03 (phase 1s, "
                    "user ruling Y1): `git status` is now DENIED, which became affordable only "
                    "once `tools/audit/changed_paths.py` gave a sanctioned way to enumerate "
                    "changed paths; and the measured FALSE DENY on a quoted grep pattern is "
                    "fixed and re-established. `git log` and `git rev-parse HEAD` remain "
                    "deliberately unenforced — nothing replaces them, so denying them would "
                    "fire on legitimate work. `tools/audit/guard_armed_check.py` puts the "
                    "arming requirement in the record while `.claude/settings.json` stays out "
                    "of it, which answers the OI-285 objection that kept it unarmed."),
    "D-254": (KNOWLEDGE, "Recognising that a step could be measured first is the judgment."),
    "D-294": (EXISTS, "PARTIAL. The variant-(b) DCML-only unit is the mechanism — the graded "
                      "surface reads the human annotation and nothing else. That no "
                      "self-annotation enters a measurement is not separately checked."),
    "D-308": (OWED, "The corpus manifest could carry an explicit tier, and the gate tooling "
                    "could refuse to measure against material not marked gate-tier. The rule "
                    "names exactly that condition, and nothing enforces it — a newly arrived "
                    "corpus is kept out of the gate by discipline alone."),
    "D-316": (EXISTS, "See D-197 — the same check covers the recorded patches."),
    "D-430": (EXISTS, "`tools/audit/decisions/gen_home_classification.py --check` re-derives "
                      "every entry's section home from its document's own headings, and the "
                      "class the criterion gives it. (It replaced `gen_section_homes.py`, which "
                      "applied this ruling to a staged subset.)"),
    "D-432": (EXISTS, "APPLIED at phase 1q by the same tool as D-430: the bar's per-document "
                      "form grade is authored once in "
                      "`tools/audit/decisions/gen_phase1p_delegation_bar.py`'s FORMS table, "
                      "whose anchors are LOCATED in the delegating file on every run, so a "
                      "delegation that moves or is reworded stops the pass rather than passing "
                      "a stale citation."),
    "D-433": (EXISTS, "Same tool as D-432; the shelving question never enters its verdict, "
                      "which is what the ruling says."),
    "D-546": (OWED, "PARTIAL, and the missing half is the one that matters. What the pass "
                    "already does mechanically: `gen_phase1p_delegation_bar.mentions()` searches "
                    "the three ratified surfaces for a document's BY-NAME mention and stops if a "
                    "grade disagrees with it, and a glob is not a by-name mention, so no glob "
                    "can silently become a delegation through that route. What NOTHING checks is "
                    "the rule's actual subject: that a delegation's membership is DETERMINATE. A "
                    "check exists in mechanical form -- flag any delegating clause whose named "
                    "targets include a wildcard, an ellipsis or a prose description rather than "
                    "a filename -- and it would have found this clause without a reading wave. "
                    "Nothing implements it. (k1) and (k2) are confirmations of D-432 and D-430, "
                    "so their mechanisation is those entries' and is not counted twice here."),
    "D-639": (KNOWLEDGE,
              "Whether a document's account of ITSELF changes how a reader reads its analysis "
              "content is a judgment about that document's content, and the ruling settles it by "
              "giving three worked examples rather than a predicate. A mechanical form would have "
              "to decide, for an arbitrary banner or note, whether a reader would conclude "
              "something false about the system — which is the point of the rule, not an "
              "incidental difficulty. What IS mechanical is already built and is not this rule: "
              "D-307's anchor convention removes the whole OUT class at its source, and "
              "`gen_true_half_reach.py` refuses to record a verdict that names no worked example, "
              "so a case the test did not decide cannot be argued into one silently — which is "
              "how the ruling's own FALLBACK is enforced."),
    "D-435": (EXISTS, "The two roles are separate inputs to the same pass and cannot be "
                      "conflated by it: the DELEGATING side is the fixed list of three "
                      "user-ratified surfaces the pass searches, and the TARGET side is the "
                      "home document being graded. A surface being in the first list gives it "
                      "no standing in the second."),
    "D-468": (EXISTS, "The rule IS a mechanism: `tools/a8_rebaseline_measure.py` carries the "
                      "declared arm and `characterise_bir_false.validate_corpus_dir` refuses a "
                      "mismatch, with no human step. Its detection and its non-interference are "
                      "both measured -- `tools/audit/corpus_arm_establishment.json` (a wrong-arm "
                      "corpus refused, a right-arm one admitted, an undeclared caller "
                      "unaffected) and `tools/audit/instrument_arm_declaration_effect.json` (the "
                      "declaration moves no measured value). What it does NOT do is prevent the "
                      "corpus being destroyed, which is why OPEN_ITEMS.md OI-312 stays open."),

    # ── AUTHORED 2026-08-09 (CC, `cc_instruction_return_continuation.md` Task 3) on the user's
    # Ruling 8 of 2026-08-09 (`cowork_rulings_2026_08_09_return.md`): the continuation session
    # authors the owed entries per THIS TOOL'S OWN CRITERIA, each verdict with its reason, and the
    # set goes to the user's review as a ratification-queue reading file. Nothing here is
    # self-ratifying, nothing here edits CLAUDE.md, and no rule is retired.
    #
    # WHY FIFTEEN WERE OWED, which is the same shape the D-557/D-576/D-638 comments above record:
    # every homing wave that writes a decision into CLAUDE.md ADDS to this tool's derived
    # population, and the triage is authored. The population is derived and the class is not, so a
    # homing act cannot supply its own triage and this check fails until a session writes one.
    # ---------------------------------------------------------------------------------------
    "D-315": (EXISTS, "See D-197 — `tools/audit/local_patches_check.py` covers the recorded "
                      "patches, deriving its list from CLAUDE.md's own local-patches section, so "
                      "this patch was covered by the same check the moment its subsection was "
                      "written. PARTIAL in the same way D-197 is: the check verifies the patch is "
                      "PRESENT at HEAD, which is the silent failure a dependency update produces; "
                      "it does not enforce the distribution disposition beside it (D-316), "
                      "because a push is the act that would breach one."),
    "D-437": (EXISTS, "PARTIAL, and the mechanical half is the one that could rot silently. "
                      "`tools/audit/gen_phase3_gate_partition.py --check` re-derives the "
                      "registered partition: every per-item verdict carries its reason, every "
                      "source quote is LOCATED in the file it cites, and the STOP the ruling "
                      "attaches — a NON-GATING item that yields a family member falsifies the "
                      "partition — is recorded with it. So the prediction cannot be quietly "
                      "re-authored after the items run, which is what makes it falsifiable. What "
                      "is NOT mechanical: whether a family design actually waited for the gating "
                      "searches, and whether a given item's search space could contain a fact "
                      "about what the model reads — the second is the judgment the ruling is."),
    "D-438": (EXISTS, "PARTIAL. `tools/audit/gen_nongating_apparatus_rows.py --check` derives the "
                      "non-gating set from the INDEX itself and STOPS if any candidate row lacks "
                      "a verdict or any verdict names a row the INDEX no longer carries open — "
                      "so the declaration cannot silently outlive the rows it classifies, in "
                      "either direction, and no verdict can be hand-added to a row the cut never "
                      "reached. What is NOT mechanical is the test itself: whether a row's "
                      "subject bears on the analysis, its inputs or a measurement tool is the "
                      "judgment, and the establishment exemption depends on recognising an "
                      "obligation under #19 rather than on any property of the row's text."),
    "D-439": (KNOWLEDGE, "It settles WHERE an enumeration lives and WHICH of its members a "
                         "pointing clause reaches. Nothing mechanical separates a clause that "
                         "POINTS at a section from one that RESTATES it — that distinction is #6 "
                         "applied by a reader — and the four per-channel scope verdicts each rest "
                         "on a reading of the channel's own text. A checker could at best assert "
                         "that the clause names no subjects of its own, which would fire on any "
                         "legitimate rewording."),
    "D-451": (KNOWLEDGE, "A desk simulation is a hand trace. Whether a table value was declared "
                         "provisional before use, and whether a verdict would flip inside that "
                         "value's plausible range, are properties of the reasoning rather than of "
                         "any file a checker can inspect. The adjacent mechanical half belongs to "
                         "D-180, which already records that a checker can confirm the artifacts "
                         "exist and not that the acts were performed."),
    "D-452": (KNOWLEDGE, "Same ground as D-451, one clause over: whether a trace ran at identity "
                         "weights is a property of how the trace was performed. It is worth "
                         "noting WHY no mechanism follows from the rule's own strength — identity "
                         "weights ARE the design's mandatory ablation baseline, so the rule "
                         "imports no new premise, but a hand trace has no artifact a checker "
                         "could read the weights off."),
    "D-473": (KNOWLEDGE, "Whether a claim is load-bearing, and whether a source was actually "
                         "fetched and read rather than reconstructed from a snippet, are both "
                         "judgments. A mechanical form was considered and is NOT proposed: "
                         "flagging an equation attributed to a source absent from the repository's "
                         "papers directory would fire on every legitimately read source that was "
                         "not stored, and a guard that fires on legitimate work gets switched "
                         "off. The independent cross-extraction is an act, not a state."),
    "D-474": (KNOWLEDGE, "A FACT OF ABSENCE established by search: no published study reports the "
                         "figure. There is nothing for a mechanism to check — the rule's force is "
                         "that a session may not satisfy principle #21 by citation, which is a "
                         "constraint on what a reader may conclude. The obligation it creates is "
                         "tracked as an open row (OI-179) and the work it names is a measurement, "
                         "not a check."),
    # RE-CLASSED 2026-08-09 EXISTS -> OWED on the user's Ruling 22 of
    # `cowork_rulings_2026_08_09_fourth_stop.md`, applied by
    # `cc_instruction_return_continuation_4.md` Task 0. The FORMER class and its whole ground are
    # preserved below (#12); nothing about the two halves' factual account is re-decided, and the
    # denominator half is still mechanised exactly as that account says.
    "D-486": (OWED, "PARTIAL IN FACT, AND THE ENTRY IS IN THE DEFECT CLASS ON THE UNCOVERED HALF "
                    "(user, Ruling 22 of 2026-08-09). The COVERAGE DENOMINATOR half IS "
                    "mechanical where it matters: gate block (A)'s figures are regenerated from "
                    "the measurement's own summary by `tools/robust_stop_restamp.py`, which is "
                    "established by reproducing the outgoing manifest exactly, so a published "
                    "figure carries the block it was computed from and cannot be stated at a "
                    "denominator the run did not have. The PER-CORPUS half is NOT mechanised: "
                    "the gate corpora are split per PRESET, which is a different cut, and "
                    "nothing checks that a figure reported over several repertoires is broken "
                    "down by them. `process_check.py` has only the adjacent shape -- it flags a "
                    "bare quantity, not an aggregate that hides which corpus moved. THE RULING'S "
                    "GROUND for putting the entry here rather than leaving it partial: the "
                    "convention's own reason -- a single aggregate can hide which corpus moved -- "
                    "bears on measurement integrity (#9, #24), so an uncovered half of it is a "
                    "defect and not merely an absence. THE MECHANISM IS NOT BUILT BY THAT RULING: "
                    "it joins the D-436 mechanism backlog like every other member of this class, "
                    "and the re-class carries its own open-items row, OPEN_ITEMS.md OI-359. "
                    "FORMER CLASS, PRESERVED (#12): MECHANISM-EXISTS, on the account of the two "
                    "halves given above, which is unchanged."),
    "D-564": (KNOWLEDGE, "A CORRECTION OF RECORD to a recorded apportionment: it says that a "
                         "published share is overstated because over-grabbed segmentation "
                         "corrupts the bass and not only the pitch-class window. What it governs "
                         "is how a reader interprets an existing caveat; there is no state a "
                         "checker could compare it against, and the apportionment it corrects is "
                         "prose in a gate block rather than a computed field."),
    "D-582": (KNOWLEDGE, "Whether a collapsed value is RECOMPUTABLE from what is kept is a "
                         "judgment about a derivation, made case by case — and the rule exists "
                         "precisely as the guard against over-flagging, so a mechanical form "
                         "would have to decide the same question in order not to report every "
                         "summary as a fault. That is the point of the rule, not an incidental "
                         "difficulty."),
    "D-602": (EXISTS, "PARTIAL, and only the abstention half. The stop is abstain-aware by "
                      "construction (D-212): the one abstain decision is "
                      "`compare_rn._our_key_ident`, the abstain duration is published beside the "
                      "percentage, and `robust_stop_diff.py` flags any rise in the candidate's "
                      "abstain rate — so an agreement figure cannot be improved by declining more "
                      "often without the rise being reported. What is NOT mechanical is the other "
                      "half, which is the rule's own subject: whether the cases a layer declined "
                      "were ones it SHOULD have declined is a judgment about each case."),
    "D-603": (KNOWLEDGE, "Whether the pipeline is still being rebuilt, and whether an increment "
                         "moved the specific defects it was meant to move, are both judgments. "
                         "The rule settles WHETHER a fixed bar is admissible at all during a "
                         "rebuild; how a bar is set once one is set is D-574's, and that one has "
                         "an order a mechanism could in principle check — measure the baseline, "
                         "then fix the bar — which this rule does not."),
    "D-604": (KNOWLEDGE, "Whether an emitted mode is a DEFENSIBLE modal reading of the passage is "
                         "the judgment the rule turns on, and no mechanism can make it. The "
                         "adjacent mechanical act is a different rule's and is already built: "
                         "D-210's shared reduction decides how a modal emission is SCORED, in one "
                         "place. This rule decides what a REMAINING disagreement MEANS, which is "
                         "principle #21 applied at the point of reading."),
    # ── AUTHORED 2026-08-09 (CC, `cc_instruction_return_continuation_4.md` Task 0) ──────────────
    # The same shape the D-557/D-576/D-638 comments above record, and the shape §2 of the triage
    # reading file states in general terms: every homing wave that writes a decision into CLAUDE.md
    # ADDS to this tool's derived population and cannot supply its own class, so the check STOPS
    # until a session authors one. These three arrived by the user's Ruling 20 and Ruling 21 of
    # 2026-08-09, and they are triaged here so this check's failure list does not widen by that act
    # alone (the OI-319 shape). NOTHING HERE IS RATIFIED: the three verdicts are authored proposals
    # and are recorded as newly owed in the triage reading file's closing state, exactly as the
    # fifteen before them were.
    "D-651": (KNOWLEDGE, "A COMMISSIONING plus the rule that ends a contact route. Neither half has "
                         "a state a checker could read. Whether a reply arrived, and whether a "
                         "reasonable wait has elapsed, are facts about an external channel that "
                         "lives outside this repository; and the work the commissioning creates is "
                         "a MEASUREMENT that opens with phase 2, not a check that fires. The "
                         "adjacent mechanical question — is a measurement tool being built before "
                         "phase 2 opens — would have to decide when phase 2 opened, which is the "
                         "same judgment D-231 is classified KNOWLEDGE for. It sits beside D-474, "
                         "which is KNOWLEDGE for the neighbouring reason: a fact of absence has "
                         "nothing for a mechanism to check."),
    "D-652": (KNOWLEDGE, "The rule turns on a CLASSIFICATION — per accumulated ruling, is this a "
                         "decision the register carries or the exercise of one it already holds — "
                         "and that is precisely the judgment no mechanism can make: an exercise "
                         "correctly carries no entry, so the absence of an entry is not evidence of "
                         "anything by itself. The adjacent mechanical half is D-230's and is "
                         "already counted there: a check that a commit touching a ruling surface "
                         "also touches the register data, which is in that entry's defect class and "
                         "is not counted twice here. What this rule adds is the recovery procedure "
                         "once that check would have fired and did not, and a procedure is followed "
                         "rather than enforced."),
    "D-656": (KNOWLEDGE, "The prohibition is on one SEMANTIC change to the grading comparison — "
                         "amending it so that a tonicization label counts as agreeing with the "
                         "annotator's modulated numeral — and no property of a diff distinguishes "
                         "that change from a legitimate correction to the same code. A behaviour "
                         "pin over the grader is the available mechanical form and is explicitly "
                         "NOT proposed: it would freeze the comparison against ALL change, "
                         "including the grading corrections the record has repeatedly made and "
                         "ratified (the exotic-mode reduction, the transposition-offset fix, the "
                         "home/local key split), so it would fire on legitimate work — the class "
                         "boundary this tool's own criterion draws. Its side-by-side neighbour "
                         "D-606 is KNOWLEDGE on the adjacent ground, and the two are separate "
                         "rules that a session can breach independently."),
    # ── AUTHORED 2026-08-09, cc_instruction_return_continuation_6.md Task 0 ───────────────────
    # Both entries were homed in CLAUDE.md by the user's Ruling 36 of that date, which is what put
    # them into this tool's derived population and stopped the check. Authoring a verdict for a row
    # the cut DID reach is what this tool requires; neither verdict is hand-added for a row the cut
    # did not reach, which is the act the record forbids.
    "D-660": (KNOWLEDGE, "The rule's antecedent is authorship, twice over: a mechanism would have "
                         "to know WHICH terms carry correspondence to the published research, and "
                         "WHICH site is a given term's introduction site. The record states both "
                         "in terms — deciding research-tied-ness and locating an introduction "
                         "site 'is authorship of the same kind as the per-candidate verdicts' — "
                         "and the derived population that would supply the first was MEASURED and "
                         "is neither sound nor bounded (D-661; the values are at "
                         "tools/audit/reserved_word_scanner.json). The neighbouring limb was "
                         "closed for exactly this reason: whether a given USE of a word is the "
                         "non-musical sense is a semantic judgment, and a checker that fires on "
                         "every legitimate musical use gets switched off, which is worse than "
                         "none (D-436's third condition). The ORDER half — governing surfaces "
                         "first, per-word batches the user rules — is a sequencing rule a session "
                         "follows rather than a state a check reads. ★ WHAT WOULD MAKE THE "
                         "ANNOTATION HALF MECHANICAL, said rather than left implicit: an AUTHORED "
                         "list of research-tied terms with their introduction sites. That list "
                         "does not exist and creating it is a named act of its own, so the "
                         "mechanical form is a condition on a future act rather than an "
                         "obligation standing now — which is why this is KNOWLEDGE and not the "
                         "defect class."),
    "D-662": (EXISTS, "A mechanism enforces it and was built in the act that ruled it. "
                      "tools/audit/index_status_lint.py owns the canonical vocabulary, the row "
                      "split and the leading-token test, and reports every non-canonical opening; "
                      "the ONE index parser reads a row's state through that same function and "
                      "STOPS on a row that does not split rather than skipping it. The lint is in "
                      "the guard population with its authored invocation, so it runs with no "
                      "human step (D-436's first condition), and its detection basis is the "
                      "both-ways normalization record at "
                      "tools/audit/index_status_normalization.json — no rate is "
                      "restated here (D-431). What no mechanism covers is the choice of which "
                      "open-state word a row's author means, which is a judgment about the row "
                      "and not about the rule."),
    # ── AUTHORED 2026-08-09, cc_instruction_return_continuation_8.md Task 0 ───────────────────
    # Homed in CLAUDE.md by the user's Ruling 42 of that date, which is what put it into this
    # tool's derived population and stopped the check. Authoring a verdict for a row the cut DID
    # reach is what this tool requires; nothing is hand-added for a row the cut did not reach.
    "D-664": (EXISTS, "PARTIAL, and the split runs exactly along the rule's own two halves. THE "
                      "DEFAULT HALF IS MECHANISED: the population the rule speaks about — every "
                      "entry whose home document is named in no user-ratified surface, or only in "
                      "a form the delegation bar excludes — is DERIVED at "
                      "tools/audit/decisions/home_classification.json and "
                      "tools/audit/decisions/phase1p_delegation_bar.json, and "
                      "tools/audit/decisions/gen_finish_line_item1_routes.py assigns the ruled "
                      "route to every open member with the authored route preserved beside it "
                      "(#12), so a session cannot reach one of these entries and quietly take the "
                      "other route. gen_item1_rehome_blocker.py is in the guard population and "
                      "STOPS when an authored route and the register disagree, which is how the "
                      "seam Ruling 38 itself created in the route table was caught rather than "
                      "reported as a completed act never having happened. Both run with no human "
                      "step (D-436's first condition). WHAT NO MECHANISM COVERS IS THE EXCEPTION "
                      "HALF, and it is stated rather than left to be discovered: whether a "
                      "document has been excepted at all is a fact about a user ruling, and "
                      "whether that ruling was taken BEFORE that document's entries were "
                      "re-homed — which is what decides validity — is a fact about the ORDER of "
                      "two acts in the record. A mechanism would need an AUTHORED list of excepted "
                      "documents with the date each was excepted; the exception list was ruled "
                      "EMPTY, so that list does not exist and creating it is a named act of its "
                      "own. ★ SO THE MECHANICAL FORM OF THE EXCEPTION HALF IS A CONDITION ON A "
                      "FUTURE ACT RATHER THAN AN OBLIGATION STANDING NOW — the same distinction "
                      "that keeps D-660's annotation half out of the defect class — which is why "
                      "this entry is not classed MECHANISABLE-AND-NOT and the defect class does "
                      "not move."),
    "D-666": (KNOWLEDGE, "The antecedent is authorship and cannot be derived: deciding that an "
                         "entry's whole content is an EVENT a standing mechanism produced — rather "
                         "than a rule that mechanism operates under — is a reading of what the "
                         "entry says, and the rule's own two exclusions turn on the same reading. "
                         "The half that LOOKS mechanical is not: a check could ask whether an "
                         "entry's evidence points at a mechanism's output surface, but an entry "
                         "wrongly closed under this rule points there too, so the test would pass "
                         "on exactly the case it exists to catch. What DOES exist is the guard "
                         "beside it — the finish line's route table and its blocker STOP when an "
                         "authored route and the register disagree — and that mechanism decides "
                         "which route CLOSES an entry, never whether an entry is in this class at "
                         "all. Enforcement is therefore the homing act's own discipline and the "
                         "per-session self-check, as for every other rule whose antecedent is a "
                         "reading."),
    "D-667": (KNOWLEDGE, "Same shape as its sibling above and for a sharper reason: whether a "
                         "recorded verdict IS an establishment verdict about one corpus, one "
                         "measurement tool or one gate is a judgment about what the verdict says, "
                         "and #19's own subject — a thing positively established versus a thing "
                         "merely unfalsified — is exactly what no property of the text carries. "
                         "The rule's CONVERSE, which is its load-bearing half, is even further "
                         "from a check: it forbids writing such a verdict INTO a rule-stating "
                         "section, and a mechanism would have to read a candidate home text and "
                         "decide whether the sentence about to be written is a dated finding about "
                         "one held collection or a rule. That is the same semantic judgment the "
                         "deep conformance limb was closed over, and a noisy checker on it would "
                         "fire on legitimate homing acts (D-436's third condition). Enforcement is "
                         "the homing act's discipline, the register's own status fields, and the "
                         "reading passes."),
    "D-606": (KNOWLEDGE, "A mechanism cannot know that the change in front of it is a modulation "
                         "detector, which is the antecedent the whole rule hangs on — and the "
                         "rule's own reason is that the agreement percentage is GAMEABLE BY THE "
                         "CHANGE UNDER TEST, so no property of the reported number distinguishes "
                         "a compliant grading from a non-compliant one. The de-masking diagnostic "
                         "it names is a measurement that must be BUILT and read, not a check that "
                         "fires."),
    # ── AUTHORED 2026-08-11, cc_instruction_apply_the_bearing_cut.md Task 1 ────────────────────
    # The user's Rulings 65 and 66 of `cowork_rulings_2026_08_11_fifteenth_stop.md` were homed into
    # CLAUDE.md by that task, which ADDS them to this tool's derived population; they are triaged
    # here so this check's failure list does not widen by that act alone (the OI-319 shape, as with
    # D-557, D-638 and every later homing wave). NOTHING HERE IS RATIFIED: both verdicts are
    # authored proposals with their grounds, offered for the user to correct.
    "D-675": (EXISTS, "PARTIAL, and the split is stated so the un-mechanised half is not hidden. "
                      "WHAT IS ENFORCED at this tree: the cut is DERIVED and never hand-classified "
                      "— tools/audit/gen_nongating_apparatus_rows.py is the ONE place a verdict is "
                      "authored, and it STOPS both on a first-cut candidate with no verdict and on "
                      "a verdict for a row the INDEX no longer carries open, so a gating verdict "
                      "cannot be hand-added; and tools/audit/gen_phase1_finish_line.py derives "
                      "every population and every gate verdict and STOPS on a population no item "
                      "carries, so the list cannot quietly stop being exhaustive. WHAT IS NOT yet "
                      "enforced: the finish line's own PER-ITEM gate is not cut by D-438's test, "
                      "the #19 carve-out is not encoded in that cut, and the falsification test "
                      "the ruling requires does not run on regeneration. All three are named by "
                      "the ruling's own text and are owed to it."),
    "D-676": (EXISTS, "PARTIAL. WHAT IS ENFORCED at this tree: the lapse POPULATION is derived "
                      "rather than chosen — it is the NON-GATING set of "
                      "tools/audit/nongating_apparatus_rows.json, whose two STOPs keep the "
                      "authored table from drifting away from the register in either direction — "
                      "and the rule's clause that a lapsed row's status cell does not move holds "
                      "BY CONSTRUCTION, since no derivation writes that cell (D-662 owns it). "
                      "WHAT IS NOT yet enforced: the rule's own STOP, that a row with no named "
                      "grading does not lapse, and whether each lapsing row actually carries its "
                      "per-row lapse record. WHAT NO MECHANISM COVERS AT ALL: whether a recorded "
                      "lapse reason is the right READING of the row — which is the judgment the "
                      "rule deliberately leaves to a later reader who would re-open the row by "
                      "challenging that recorded derivation."),
    # ── AUTHORED 2026-08-13, cc_instruction_ruling69_discard_input.md Task 1 ───────────────────
    # The user's Ruling 69 of `cowork_rulings_2026_08_13_seventeenth_stop.md` was homed into
    # CLAUDE.md by that task, which ADDS it to this tool's derived population; it is triaged here
    # so this check's failure list does not widen by that act alone (the OI-319 shape, as with
    # every homing wave before it). NOTHING HERE IS RATIFIED: the verdict is an authored proposal
    # with its ground, offered for the user to correct.
    "D-677": (EXISTS, "A mechanism enforces the rule's guard and was built in the batch that "
                      "homed it. tools/audit/gen_discard_records.py is the ONE place a discard "
                      "record reaches the cut: it LOCATES each of the three elements — finding, "
                      "date, reason — inside the record's own span in the record's own surface on "
                      "every run, so a reworded record halts it rather than leaving a citation to "
                      "text nobody re-read, and a record missing an element is published as NOT "
                      "CONFORMING and is not consumed, which is the ruling's own wording. The #19 "
                      "carve-out is DERIVED from the committed apparatus declaration's recorded "
                      "gate grounds and a record naming a row it keeps gating is a STOP. "
                      "tools/audit/gen_phase1_completion_inventory.py then consumes the conforming "
                      "set as one input to the gate it already derived, keeps each row's D-438 "
                      "verdict beside the result (#12), recomputes the same cut with the input OFF "
                      "and STOPs on any mover that carries no conforming discard record — so the "
                      "rule's clause that the gate stays DERIVED is enforced rather than trusted. "
                      "The tool is in the guard population with its authored invocation, so it "
                      "runs with no human step (D-436's first condition), and its patterns are "
                      "measured against positive AND negative seeds the record actually holds "
                      "rather than asserted. ★ TWO THINGS NO MECHANISM COVERS, stated so the "
                      "PARTIAL is visible rather than implied. (1) Whether a discard verdict is "
                      "the right READING of a row — the judgment the ruling deliberately leaves to "
                      "a later reader, who re-opens the row by challenging the recorded reason "
                      "rather than by rediscovering the issue. (2) COMPLETENESS over the whole "
                      "record: the completeness STOP reaches the open-items register's own two "
                      "surfaces and no further, so a discard recorded elsewhere reaches the cut "
                      "only by being entered in the authored table. That bound is stated on the "
                      "tool's own artifact, and the error it leaves runs in the safe direction — a "
                      "gate is KEPT that a record may have discarded. ★ THE FORMER CLASS, "
                      "PRESERVED (#12): MECHANISABLE-AND-NOT, authored one commit earlier in the "
                      "same batch, when the rule was written and entered and nothing implemented "
                      "it yet. It was true when written and is retired because the mechanism "
                      "landed, never because it was wrong."),
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
            "strongest_candidate": "BUILT at phase 1q. It was D-197/D-198/D-199/D-316, the "
                                   "local patches, stated as do-not-revert against a dependency "
                                   "update — the silent failure a check catches and a reader "
                                   "does not. `tools/audit/local_patches_check.py` now covers "
                                   "them, so they have left the defect set; what remains of "
                                   "D-197 is its distribution constraint, which no check can "
                                   "enforce.",
        },
        "what_was_executed": "NO CLAUDE.md TEXT WAS RETIRED, at phase 1p or at phase 1q. That "
                             "was recorded here as a failure under the test then in force — a "
                             "mechanism must retire the prose it replaces, or it is apparatus "
                             "growth — and the USER WITHDREW THAT TEST on 2026-08-03 as a "
                             "structural proxy standing in for a behavioral quantity, "
                             "unvalidated (#17d). The test from here is three measured "
                             "conditions (register entry D-436, homed at "
                             "cowork_audit_protocol.md): runs automatically with no human step; "
                             "a measured detection rate against known instances; a measured "
                             "false-positive rate at or near zero. Four mechanisms now stand "
                             "against rules in this table (D-196, D-253, D-430/D-432, "
                             "D-197's group), each with an establishment artifact; none retires "
                             "prose, and under D-436 that is no longer a defect.",
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
