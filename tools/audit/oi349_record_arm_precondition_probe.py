#!/usr/bin/env python3
"""THE OI-349 PROBE: what does the PRODUCTION record arm supply to the key-area grouping pass,
and does it satisfy the stabilization precondition D-472 names?

WHY THIS TOOL EXISTS.  `OPEN_ITEMS.md` OI-349 records an arm split found on 2026-08-07: the
key-area grouping pass is SHARED and runs on the production record arm, while the
smoothing-and-stabilization step D-472 names as its precondition has one call site, inside the
LEGACY arm.  The row states two possibilities and asserts neither -- the record arm may satisfy
the precondition by other means, or the live path may be grouping un-stabilized regions -- and
records that the check which found the split "did not test what the record arm feeds the
grouping pass".  This probe tests exactly that, READ-ONLY, on the user's Ruling 9 of 2026-08-09
(`cowork_rulings_2026_08_09_return.md`), which settles the timing question the row reserved.

WHAT IT IS AND IS NOT.  It is a POINT-IN-TIME RECORD of a reading of the code, in the class the
2026-08-04 ruling R4 defines: it records what was read at one tree, not a live invariant, so it
carries no re-derivation mode and is deliberately outside the derived guard-candidate population.
It changes nothing, proposes nothing, and authorizes nothing -- no fix, no design, no inference
change.  The freeze is not relaxed by it.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : the QUESTIONS, the anchors to read them at, and the reading each anchor supports.
  derived  : every file-and-line citation, located in the file itself on each run.  A moved,
             reworded or ambiguous anchor STOPS the run rather than emitting a stale citation --
             the same discipline the delegation-bar generator uses, and the reason no line number
             in the artifact is transcribed (D-431, CLAUDE.md #17f).

Run:  python tools/audit/oi349_record_arm_precondition_probe.py
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "oi349_record_arm_precondition_probe.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout


class Stop(Exception):
    """An anchor has moved, gone or become ambiguous. Never a warning."""


def locate(rel: str, anchor: str) -> dict:
    """The one line of `rel` carrying `anchor`, with the line as the file holds it."""
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise Stop(f"the probe names a file the tree does not have: {rel}")
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    hits = [(i, ln) for i, ln in enumerate(lines, 1) if anchor in ln]
    if not hits:
        raise Stop(f"anchor not found in {rel}: {anchor!r} -- the code has moved or been "
                   "reworded; re-read it before re-aiming anything")
    if len(hits) > 1:
        raise Stop(f"anchor is ambiguous in {rel} (lines {[h[0] for h in hits]}): {anchor!r}")
    ln, text = hits[0]
    return {"at": f"{rel}:{ln}", "line": text.strip()}


def find_all(rel: str, anchor: str) -> list[dict]:
    """Every line of `rel` carrying `anchor`. Absence is a STOP; multiplicity is the point."""
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise Stop(f"the probe names a file the tree does not have: {rel}")
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    hits = [{"at": f"{rel}:{i}", "line": ln.strip()}
            for i, ln in enumerate(lines, 1) if anchor in ln]
    if not hits:
        raise Stop(f"anchor not found in {rel}: {anchor!r}")
    return hits


# ── AUTHORED: what was read, where, and what the reading supports ────────────────────────────
STEPS = [
    ("1_which_arm_ships",
     "Is the record arm the production notation arm at HEAD?",
     [("src/composing/composingconfiguration.cpp",
       "setDefaultValue(USE_JOINT_NOTATION_RECORD, Val(true))"),
      ("src/notation/internal/notationcomposingbridge.cpp",
       "const bool useRecord = prefs && prefs->useJointNotationRecord();")],
     "YES. The flag's default value is true, and the span-annotation emitter branches on it and "
     "returns from the record branch without reaching the legacy path below."),

    ("2_the_grouping_pass_on_the_record_arm",
     "Does the shared grouping pass run on the record arm, and on what?",
     [("src/composing/analysis/section/sectionrecordadapter.cpp",
       "Key-areas: the shared confidence-gated grouping"),
      ("src/composing/analysis/section/sectionanalyzer.cpp",
       "Lifted verbatim out of analyzeSection")],
     "YES, and it is ONE definition shared by both arms (#6). It reads each region's stored "
     "(keySignatureFifths, mode) and the stored hasAssertiveExposure boolean; it re-decides no key."),

    ("3_the_named_precondition_is_legacy_only",
     "Where is the stabilization step D-472 names as its precondition called?",
     [("src/composing/analysis/section/sectionanalyzer.cpp",
       "stabilizeHarmonicRegionsForDisplay(displayRegions);"),
      ("src/composing/analysis/section/sectionrecordadapter.cpp",
       "A's decode is CONTIGUOUS by construction")],
     "ONE call site, in the legacy arm's Pass 4. The record adapter states in its own comment "
     "that the legacy machinery is NOT ported. This is the split OI-349 already recorded; the "
     "probe re-confirms it rather than assuming it."),

    ("4_what_the_stabilization_step_actually_does",
     "What are the two halves of the legacy stabilization step, so 'satisfied by other means' "
     "can be judged half by half rather than as a whole?",
     [("src/composing/analysis/section/sectionanalyzer.cpp",
       "1-region-island key stabilization"),
      ("src/composing/analysis/section/sectionanalyzer.cpp",
       "region.chordResult.function.keyTonicPc = tonicPc;"),
      ("src/composing/analysis/section/sectionanalyzer.cpp",
       "cra::refineSparseChordQualityFromKeyContext(region.chordResult,")],
     "TWO halves, and only the first is the precondition D-472 names. (a) Layer B, a 1-region "
     "key-island smoother: a region whose key differs from the running stable key, and whose "
     "successor does not agree with it, is OVERWRITTEN with the running key. (b) A derived-field "
     "loop recomputing degree / keyTonicPc / keyMode / diatonicToKey per region, plus a legacy "
     "sparse chord-quality refinement, which is a CHORD concern and outside this precondition."),

    ("5_the_record_arm_supplies_half_b_natively",
     "Does the record arm supply half (b)'s derived fields?",
     [("src/composing/analysis/section/sectionrecordadapter.cpp",
       "fn.keyTonicPc = seg.tonicPc;"),
      ("src/composing/analysis/section/sectionrecordadapter.cpp",
       "kmr.keySignatureFifths   = seg.keySignatureFifths;")],
     "YES, natively, from the record's own committed fields -- degree, diatonicToKey, keyTonicPc "
     "and keyMode are read off the segment rather than recomputed. So half (b) is not a gap."),

    ("6_where_the_record_arm_key_comes_from",
     "Is the per-segment key the record supplies the output of a GLOBAL sequence decision, or a "
     "per-segment independent choice?",
     [("src/composing/analysis/joint/jointnotationrecord.cpp",
       "rs.keySignatureFifths = keySignatureFifths(s.tonicPc, s.isMajor, sigRef);"),
      ("src/composing/analysis/joint/jointdecoder.cpp",
       "const double stay = wKey * adapter.keyTransLogp(tonic, major, tonic, major);"),
      ("src/composing/analysis/joint/jointdecoder.cpp",
       "// (c) key-change transition + entry"),
      ("src/composing/analysis/joint/jointdecoder.cpp",
       "std::vector<SegmentSummary> segs;")],
     "GLOBAL. The record's per-segment key is copied verbatim from the decoder's committed "
     "SegmentSummary, and those are produced by backtracking the best full-coverage path of a "
     "dynamic program whose state carries (tonic, mode, chord class). The key sequence is scored "
     "by an explicit key-transition term with SEPARATE stay and change branches, so a key change "
     "must pay for itself against the content evidence. That is a smoothing layer over the key "
     "sequence, arrived at by optimization rather than by a post-hoc patch."),

    ("7_the_legacy_arm_states_this_reasoning_itself",
     "Does the record's own codebase already state this reasoning anywhere, or is it the probe's?",
     [("src/composing/analysis/section/sectionanalyzer.cpp",
       "Viterbi decision (decideJointKey IS the smoothing layer), so this island"),
      ("src/composing/analysis/section/jointkeydecision.cpp",
       'std::getenv("MUSE_JOINT_KEY_WIRING")')],
     "IT IS ALREADY STATED, but for a DIFFERENT mechanism, and the difference matters. The legacy "
     "arm makes Layer B inert when the J-key-iii re-key wiring is on, on exactly this ground -- "
     "the per-region key is then already a global decision, so island smoothing would re-smooth "
     "it. That wiring is default OFF (an environment variable, absent by default), so on the "
     "legacy arm Layer B does run. The reasoning transfers to the record arm; the code path does "
     "not, and the two must not be conflated."),
]

# The incidental finding, kept apart from the probe's own question because it is not an answer to
# it: six comments in `src/` describe the record path as default OFF while the configuration sets
# its default to true. Derived, not authored -- the sites are found by search, so the count cannot
# be quietly wrong.
STALE_DEFAULT_SITES = [
    "src/notation/internal/notationcomposingbridge.cpp",
    "src/notation/internal/notationimplodebridge.cpp",
    "src/notation/internal/notationtuningbridge.cpp",
    "src/composing/analysis/section/sectionrecordadapter.h",
    "src/composing/analysis/CMakeLists.txt",
]


def stale_default_comments() -> list[dict]:
    out: list[dict] = []
    for rel in STALE_DEFAULT_SITES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            raise Stop(f"the probe names a file the tree does not have: {rel}")
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
        for i, ln in enumerate(lines, 1):
            low = ln.lower()
            if "usejointnotationrecord" in low and "default" in low and "off" in low:
                out.append({"at": f"{rel}:{i}", "line": ln.strip()})
    if not out:
        raise Stop("the incidental finding names no site -- either it was corrected (in which "
                   "case remove this block) or the search no longer matches")
    return out


def main() -> int:
    steps = []
    for key, question, anchors, reading in STEPS:
        steps.append({
            "step": key,
            "question": question,
            "read_at": [locate(rel, a) for rel, a in anchors],
            "what_it_establishes": reading,
        })

    artifact = {
        "purpose": "The OI-349 read-only probe: what the PRODUCTION record arm supplies to the "
                   "key-area grouping pass, compared against the stabilization precondition "
                   "D-472 states. A reading of the code, recorded; not a measurement of the "
                   "analysis, not a fix, not a design, and not an authorization for either.",
        "generated_by": "tools/audit/oi349_record_arm_precondition_probe.py",
        "generated_for": "cc_instruction_return_continuation.md, Task 1 -- the user's Ruling 9 of "
                         "2026-08-09 (`cowork_rulings_2026_08_09_return.md`), which settles the "
                         "timing question `OPEN_ITEMS.md` OI-349 reserved to the user and runs "
                         "the probe now.",
        "why_it_carries_no_re_derivation_mode":
            "It is a POINT-IN-TIME RECORD of a reading, in the class the 2026-08-04 ruling R4 "
            "defines: it says what the code said at one tree. A mode that re-asserted it would "
            "measure the clock rather than the repository, and would also put this file in the "
            "derived guard-candidate population, where a historical record does not belong. Every "
            "citation is nonetheless LOCATED on each run, so re-running it is how a reader "
            "confirms the anchors still resolve.",
        "★_the_finding": "SATISFIED BY OTHER MEANS, and the means is named. The production record "
                         "arm does not run the legacy stabilization step, and does not need to: "
                         "the per-segment key it groups on is the output of the joint decoder's "
                         "GLOBAL dynamic program, whose state carries the key and whose key "
                         "transitions are scored with separate stay and change branches -- a "
                         "smoothing layer over the key sequence arrived at by optimization. The "
                         "derived-field half of the legacy step is supplied natively by the "
                         "record. So the second possibility OI-349 states -- that the live path "
                         "groups un-stabilized regions -- is NOT what the code does.",
        "★_what_therefore_needs_correcting_and_is_NOT_corrected_here":
            "D-472's own wording. Its verbatim says key areas are grouped 'over the "
            "already-stabilized regions' and its recorded defense says the rule 'leverages the "
            "key/mode fields and the stabilization Pass 4 already performed'. Pass 4 is the "
            "legacy arm's, and on the arm that ships the precondition is met by a different "
            "design. Correcting the specification is its own act on OI-349's row and is NOT "
            "performed here: this batch's freeze admits the probe and nothing after it.",
        "★_the_one_way_the_two_mechanisms_are_NOT_equivalent, stated rather than smoothed over":
            "They do not produce identical region key sequences. Layer B ERASES a one-region key "
            "island unconditionally; the decoder's key-transition term only makes an island "
            "expensive, so an island survives where the content evidence outweighs two key "
            "changes. That difference does not leave the grouping un-preconditioned, because "
            "D-472's own confidence test is what decides whether a divergent region opens a new "
            "area: a surviving island that is not assertively exposed is grouped into the "
            "enclosing area and keeps its own key for display, which is the rule's stated intent. "
            "But it is a real behavioural difference between the arms and is recorded as one.",
        "what_this_probe_did_NOT_test": [
            "Whether the decoder's key sequence is BETTER than Layer B's on any corpus -- no "
            "measurement was taken and none is implied by the finding.",
            "The chord-quality half of the legacy step (the sparse refinement), which is a chord "
            "concern outside this precondition and is separately not ported.",
            "Any other consumer of the legacy stabilization step.",
        ],
        "steps": steps,
        "incidental_finding_kept_apart": {
            "what": "Comments in `src/` describe the record path as DEFAULT OFF. The "
                    "configuration sets its default to true, and says so in the comment directly "
                    "above the call -- 'default TRUE since the user-ratified switch (2026-07-27)'.",
            "why_it_is_here_and_not_in_the_finding": "It is not an answer to OI-349's question. It "
                                                     "was met while establishing which arm ships, "
                                                     "which is step 1, and a reader of any of "
                                                     "these sites learns which arm runs and learns "
                                                     "it wrong.",
            "why_it_is_not_corrected_here": "Every site is a `src/` file, which this batch's "
                                            "freeze does not admit. Rowed and left.",
            "the_true_default": locate("src/composing/composingconfiguration.cpp",
                                       "setDefaultValue(USE_JOINT_NOTATION_RECORD, Val(true))"),
            "the_sites_saying_otherwise": stale_default_comments(),
        },
    }

    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  steps read: {len(steps)}")
    print(f"  FINDING: SATISFIED BY OTHER MEANS -- the joint decoder's global key path")
    print(f"  incidental: {len(artifact['incidental_finding_kept_apart']['the_sites_saying_otherwise'])} "
          "site(s) in src/ describe the production record path as default OFF")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
