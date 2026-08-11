#!/usr/bin/env python3
"""
gen_callpath_facts.py — OI-206 Task 1: the note-seam call-path confirmation.

READ-ONLY code-fact extractor. Produces tools/notation_seams/callpath_facts.json:
a generated fact table (not prose assertions, #17f) that closes the OI-206
call-path questions AT THE CODE, with a verified citation for every claim.

Every load-bearing claim is anchored to a (file, line, must_contain) triple.
The script re-reads each cited line at the current checkout and FAILS LOUDLY
(exit 2) if the line does not contain the expected token — a citation that no
longer matches is a bit-rot / mismatch finding (a surprise -> STOP, #13), not a
silently stale figure. So the emitted table is reproducible and self-checking.

The four OI-206 Task-1 questions this answers:
  1. Which selection kinds invoke the note-seam funnel analyzeHarmonicContextAtTick.
  2. How many produceNotationRecord calls one single-note selection EVENT triggers.
  3. That the call is synchronous on the UI thread + no re-trigger loop.
  4. The other record-arm consumers' interactive frequency (per-action, not per-selection).

The "field-pattern reproduction" block maps each of the user's field-report
observations (OI-206 dated refinements) to the exact code branch that produces it.
A field observation the code cannot explain would be a finding.

Usage:
    python tools/notation_seams/gen_callpath_facts.py
    python tools/notation_seams/gen_callpath_facts.py --check   # verify only, no write

Deterministic: the only environment-derived value is the corpus/repo git hash
(git rev-parse HEAD), stamped into the manifest for reproducibility (#16).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "tools" / "notation_seams" / "callpath_facts.json"

# ── Anchors: (id, file, 1-based line, must_contain) ──────────────────────────
# Every fact below cites one or more anchor ids. The verifier asserts the cited
# line contains the substring at the current checkout.
ANCHORS = [
    # -- accessibility (status bar) subscription + dispatch --
    ("acc_sel_sub",   "src/notation/internal/notationaccessibility.cpp", 44,  "selectionChanged().onNotify"),
    ("acc_notn_sub",  "src/notation/internal/notationaccessibility.cpp", 48,  "notationChanged().onReceive"),
    ("acc_update",    "src/notation/internal/notationaccessibility.cpp", 110, "void NotationAccessibility::updateAccessibilityInfo()"),
    ("acc_is_single", "src/notation/internal/notationaccessibility.cpp", 118, "selection()->isSingle()"),
    ("acc_single_fn", "src/notation/internal/notationaccessibility.cpp", 119, "singleElementAccessibilityInfo()"),
    ("acc_is_range",  "src/notation/internal/notationaccessibility.cpp", 120, "selection()->isRange()"),
    ("acc_is_list",   "src/notation/internal/notationaccessibility.cpp", 122, "selection()->isList()"),
    ("acc_dedup",     "src/notation/internal/notationaccessibility.cpp", 136, "m_accessibilityInfo.val == infoStd"),
    ("acc_set",       "src/notation/internal/notationaccessibility.cpp", 140, "m_accessibilityInfo.set(infoStd)"),
    ("acc_isnote",    "src/notation/internal/notationaccessibility.cpp", 203, "element->isNote()"),
    ("acc_annot",     "src/notation/internal/notationaccessibility.cpp", 204, "harmonicAnnotation(toNote(element))"),

    # -- harmonicAnnotation -> Details -> funnel --
    ("ha_fn",         "src/notation/internal/notationcomposingbridge.cpp", 818, "std::string harmonicAnnotation(const Note* note)"),
    ("ha_calls",      "src/notation/internal/notationcomposingbridge.cpp", 826, "analyzeNoteHarmonicContextDetails(note)"),
    ("details_funnel","src/notation/internal/notationcomposingbridge.cpp", 965, "return analyzeHarmonicContextAtTick(sc, tick"),

    # -- the funnel: record-arm produce (the per-selection payer) --
    ("funnel_fn",     "src/notation/internal/notationcomposingbridge.cpp", 703, "NoteHarmonicContext analyzeHarmonicContextAtTick"),
    ("funnel_flag",   "src/notation/internal/notationcomposingbridge.cpp", 730, "prefs->useJointNotationRecord()"),
    ("funnel_produce","src/notation/internal/notationcomposingbridge.cpp", 733, "produceNotationRecord(score, std::string()"),
    ("funnel_view",   "src/notation/internal/notationcomposingbridge.cpp", 738, "buildNoteContextFromRecord(rec.record, tick)"),

    # -- select() emits selectionChanged exactly once, no notationChanged --
    ("select_fn",     "src/notation/internal/notationinteraction.cpp", 1001, "void NotationInteraction::select("),
    ("select_notify", "src/notation/internal/notationinteraction.cpp", 1025, "notifyAboutSelectionChangedIfNeed();"),
    ("notify_guard",  "src/notation/internal/notationinteraction.cpp", 387,  "if (!score()->selectionChanged())"),
    ("notify_emit",   "src/notation/internal/notationinteraction.cpp", 395,  "m_selectionChanged.notify()"),
    ("apply_notn",    "src/notation/internal/notationinteraction.cpp", 344,  "notifyAboutNotationChanged();"),

    # -- mouse press: single-click SINGLE vs ctrl-click ADD --
    ("mp_consider",   "src/notationscene/qml/MuseScore/NotationScene/notationviewinputcontroller.cpp", 830, "mousePress_considerSelect"),
    ("mp_single",     "src/notationscene/qml/MuseScore/NotationScene/notationviewinputcontroller.cpp", 852, "SelectType selectType = SelectType::SINGLE;"),
    ("mp_add",        "src/notationscene/qml/MuseScore/NotationScene/notationviewinputcontroller.cpp", 856, "selectType = SelectType::ADD;"),
    ("mp_select",     "src/notationscene/qml/MuseScore/NotationScene/notationviewinputcontroller.cpp", 873, "select({ ctx.hitElement }, selectType"),

    # -- muse::async synchronous same-thread dispatch --
    ("chan_send",     "muse/framework/global/thirdparty/kors_async/async/internal/channelimpl.h", 596, "void send(SendMode mode"),
    ("chan_sync",     "muse/framework/global/thirdparty/kors_async/async/internal/channelimpl.h", 487, "sendThdata.receiversCall(args ...)"),

    # -- other record-arm consumers (action-scoped) --
    ("emit_fn",       "src/notation/internal/notationcomposingbridge.cpp", 1386, "void addHarmonicAnnotationsToSelection"),
    ("emit_produce",  "src/notation/internal/notationcomposingbridge.cpp", 1497, "produceNotationRecord(score, std::string()"),
    ("implode_fn",    "src/notation/internal/notationimplodebridge.cpp", 1384, "bool populateChordTrack("),
    ("implode_produce","src/notation/internal/notationimplodebridge.cpp", 1421, "produceNotationRecord(score, std::string()"),
    ("tuning_fn",     "src/notation/internal/notationtuningbridge.cpp", 747, "bool applyRegionTuning("),
    ("tuning_produce","src/notation/internal/notationtuningbridge.cpp", 778, "produceNotationRecord(score, std::string()"),
    ("annot_sel_fn",  "src/notation/internal/notationinteraction.cpp", 8256, "void NotationInteraction::addAnalyzedHarmonyToSelection"),
    ("annot_sel_call","src/notation/internal/notationinteraction.cpp", 8311, "analyzeNoteHarmonicContext(note, keyFifths, keyMode)"),
    ("ctxmenu_call",  "src/notationscene/qml/MuseScore/NotationScene/notationcontextmenumodel.cpp", 194, "analyzeNoteHarmonicContextDetails(note)"),
]


def cite(anchor_id):
    return f"{ANCHOR_BY_ID[anchor_id][0]}:{ANCHOR_BY_ID[anchor_id][1]}"


ANCHOR_BY_ID = {a[0]: (a[1], a[2], a[3]) for a in ANCHORS}


def verify_anchors():
    """Assert every cited line contains its expected token. Returns list of failures."""
    failures = []
    cache = {}
    for aid, rel, line, needle in ANCHORS:
        p = REPO / rel
        if rel not in cache:
            cache[rel] = p.read_text(encoding="utf-8", errors="replace").splitlines()
        lines = cache[rel]
        if line < 1 or line > len(lines):
            failures.append(f"{aid} {rel}:{line} OUT OF RANGE (file has {len(lines)} lines)")
            continue
        actual = lines[line - 1]
        if needle not in actual:
            failures.append(f"{aid} {rel}:{line} expected <{needle}> got <{actual.strip()}>")
    return failures


def git_hash():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(REPO)).decode().strip()
    except Exception as e:  # pragma: no cover
        return f"UNKNOWN ({e})"


def build_facts():
    return {
        "open_item": "OI-206",
        "task": "Task 1 — the note-seam call-path confirmation (closed at the code, flag useJointNotationRecord ON = the switched/production arm)",
        "purpose": (
            "Confirm the OI-206 mechanism at the code: which selection kinds reach the note-seam funnel "
            "analyzeHarmonicContextAtTick; how many produceNotationRecord calls one single-note selection "
            "EVENT triggers; that the call is synchronous on the UI thread with no re-trigger loop; and the "
            "other record-arm consumers' interactive frequency. Every claim carries a verified code citation."
        ),

        # ── Q1: which selection kinds reach the funnel ──────────────────────
        "q1_selection_kind_dispatch": {
            "entry": (
                "NotationAccessibility subscribes selectionChanged()->updateAccessibilityInfo() and "
                "notationChanged()->updateAccessibilityInfo() (the status-bar text builder)."
            ),
            "entry_citations": [cite("acc_sel_sub"), cite("acc_notn_sub"), cite("acc_update")],
            "dispatch_branches": [
                {"selection": "single element", "predicate": "selection()->isSingle()",
                 "handler": "singleElementAccessibilityInfo()",
                 "reaches_funnel": "ONLY IF the single element is a Note (element->isNote())",
                 "citations": [cite("acc_is_single"), cite("acc_single_fn"), cite("acc_isnote"), cite("acc_annot")]},
                {"selection": "range", "predicate": "selection()->isRange()",
                 "handler": "rangeAccessibilityInfo()",
                 "reaches_funnel": "NO — builds a bar/beat string only; no harmonicAnnotation call",
                 "citations": [cite("acc_is_range")]},
                {"selection": "list (multi-element, e.g. ctrl-clicked notes)", "predicate": "selection()->isList()",
                 "handler": "literal \"List selection\"",
                 "reaches_funnel": "NO — a translated literal; no analysis call",
                 "citations": [cite("acc_is_list")]},
                {"selection": "none", "predicate": "(else)",
                 "handler": "empty",
                 "reaches_funnel": "NO", "citations": [cite("acc_update")]},
            ],
            "funnel_gate": (
                "singleElementAccessibilityInfo() calls harmonicAnnotation(toNote(element)) ONLY inside "
                "`if (element->isNote())`. harmonicAnnotation -> analyzeNoteHarmonicContextDetails(note) -> "
                "analyzeHarmonicContextAtTick -> (flag ON) produceNotationRecord (whole-score decode)."
            ),
            "funnel_gate_citations": [cite("acc_isnote"), cite("acc_annot"), cite("ha_fn"),
                                      cite("ha_calls"), cite("details_funnel"), cite("funnel_flag"),
                                      cite("funnel_produce")],
            "conclusion": (
                "The note-seam funnel is reached from the interactive selection path by EXACTLY ONE selection "
                "kind: a single-NOTE selection. Range, list (ctrl-click multi-note), single non-note (rest, "
                "fermata, key signature, clef, barline, repeat), and empty selections never reach it."
            ),
        },

        # ── Q2: produce calls per single-note selection event ───────────────
        "q2_produce_calls_per_single_note_event": {
            "answer": "EXACTLY ONE produceNotationRecord per single-note selection event (no multiplier).",
            "reasoning": [
                "A single-note mouse click routes mousePress_considerSelect -> select({hitElement}, SelectType::SINGLE); "
                "ctrl-click uses SelectType::ADD (making a list, not a single).",
                "select() calls notifyAboutSelectionChangedIfNeed() at most once per call; the notify is de-duplicated "
                "by score()->selectionChanged() and emits m_selectionChanged.notify() a single time.",
                "select() does NOT call notifyAboutNotationChanged() — notationChanged() is emitted from apply() "
                "(score edits) and layout ops, not from a plain selection. So the accessibility object's second "
                "subscription (notationChanged) does NOT fire on a plain single-note selection.",
                "Therefore updateAccessibilityInfo() runs once -> singleElementAccessibilityInfo() once -> "
                "harmonicAnnotation once -> ONE produceNotationRecord.",
            ],
            "citations": [cite("mp_consider"), cite("mp_single"), cite("mp_add"), cite("mp_select"),
                          cite("select_fn"), cite("select_notify"), cite("notify_guard"),
                          cite("notify_emit"), cite("apply_notn"), cite("funnel_produce")],
            "caveat": (
                "This counts the SELECTION event only. An event that BOTH re-selects a note AND relayouts the score "
                "(e.g. an edit that leaves a note selected) would additionally fire notationChanged -> a second "
                "updateAccessibilityInfo -> a second produce. That is an edit event, not the field-reported plain "
                "selection. No path fires the funnel more than once for a plain single-note click."
            ),
        },

        # ── Q3: synchronous on UI thread + no re-trigger loop ───────────────
        "q3_synchronous_and_no_loop": {
            "synchronous": (
                "m_selectionChanged.notify() -> Channel::send(SendMode::Auto) -> sendAuto(): when the receiver was "
                "registered on the SAME thread as the sender (accessibility is constructed and subscribes on the UI "
                "thread, the same thread select() runs on), the callback runs INLINE via sendThdata.receiversCall(...) "
                "— no queue, no event-loop hop. So the whole-score produceNotationRecord executes synchronously on the "
                "UI thread inside the select() call; UI paint and input dispatch are blocked until it returns."
            ),
            "synchronous_citations": [cite("notify_emit"), cite("chan_send"), cite("chan_sync"), cite("funnel_produce")],
            "no_loop": (
                "updateAccessibilityInfo() -> setAccessibilityInfo() writes m_accessibilityInfo.set() (a separate "
                "ValCh consumed by the status-bar text UI). It does not call select(), deselect, or any notation edit, "
                "so it cannot re-emit selectionChanged() or notationChanged(). The dedup guard "
                "(m_accessibilityInfo.val == infoStd) short-circuits even the ValCh notify on an unchanged string. "
                "There is NO re-trigger cycle: one selection event -> one decode. The earlier field 'total freeze' "
                "presentation is consistent with a burst of DISTINCT selection events (each a fresh synchronous "
                "whole-score decode), not a self-sustaining loop."
            ),
            "no_loop_citations": [cite("acc_set"), cite("acc_dedup"), cite("acc_update")],
        },

        # ── Q4: other record-arm consumers' interactive frequency ───────────
        "q4_other_consumers_frequency": {
            "note": (
                "Every non-note-seam producer of the record is USER-ACTION-scoped (fires once per explicit command), "
                "NOT per selection change. The note-seam status-bar path is the SOLE per-selection payer."
            ),
            "consumers": [
                {"consumer": "note-seam status bar (accessibility)",
                 "entry": "singleElementAccessibilityInfo -> harmonicAnnotation -> analyzeHarmonicContextAtTick",
                 "trigger_scope": "PER single-note SELECTION change (the interactive per-event payer)",
                 "produce_call_site": cite("funnel_produce")},
                {"consumer": "span-annotation emit (Add chord symbols/Roman numerals to selection)",
                 "entry": "addHarmonicAnnotationsToSelection -> produceNotationRecord",
                 "trigger_scope": "PER explicit annotate command over a range (once per invocation)",
                 "produce_call_site": cite("emit_produce"), "fn": cite("emit_fn")},
                {"consumer": "implode chord track",
                 "entry": "populateChordTrack -> produceNotationRecord",
                 "trigger_scope": "PER Implode command (once)",
                 "produce_call_site": cite("implode_produce"), "fn": cite("implode_fn")},
                {"consumer": "region tuning",
                 "entry": "applyRegionTuning -> produceNotationRecord",
                 "trigger_scope": "PER tuning-apply command (once)",
                 "produce_call_site": cite("tuning_produce"), "fn": cite("tuning_fn")},
                {"consumer": "add-analyzed-harmony to selection (per-note path)",
                 "entry": "addAnalyzedHarmonyToSelection -> analyzeNoteHarmonicContext(note,...) -> funnel",
                 "trigger_scope": "PER explicit add-harmony command, but calls the funnel ONCE PER SELECTED NOTE "
                                  "(a loop over byStaffTick) — an N-produce multiplier per command on the flag-ON arm; "
                                  "relevant to the fix surface (a keyed record cache collapses the N to 1)",
                 "produce_call_site": cite("annot_sel_call"), "fn": cite("annot_sel_fn")},
                {"consumer": "right-click note context menu (Tune as / analysis items)",
                 "entry": "appendNoteAnalysisItems -> analyzeNoteHarmonicContextDetails -> funnel",
                 "trigger_scope": "PER right-click that builds the note context menu (once per menu build)",
                 "produce_call_site": cite("ctxmenu_call")},
            ],
        },

        # ── Field-pattern reproduction (OI-206 dated refinements) ───────────
        "field_pattern_reproduction": {
            "note": (
                "Each field observation (OI-206 user field reports 2026-07-27) is mapped to the exact code branch. "
                "Every observation reproduces; there is no unexplained observation."
            ),
            "observations": [
                {"field": "selecting a SINGLE NOTE takes 3-4 s before the highlight renders",
                 "code_explanation": "isSingle && isNote -> harmonicAnnotation -> synchronous whole-score "
                                     "produceNotationRecord on the UI thread; paint blocked until it returns",
                 "match": True,
                 "citations": [cite("acc_is_single"), cite("acc_isnote"), cite("acc_annot"), cite("funnel_produce"), cite("chan_sync")]},
                {"field": "ctrl-clicking additional notes is INSTANT",
                 "code_explanation": "ctrl-click -> SelectType::ADD -> a LIST selection -> isList() branch -> "
                                     "literal \"List selection\"; the funnel is never reached",
                 "match": True,
                 "citations": [cite("mp_add"), cite("acc_is_list")]},
                {"field": "measures / ranges highlight at normal speed",
                 "code_explanation": "range selection -> isRange() -> rangeAccessibilityInfo() (bar/beat string only); "
                                     "no harmonicAnnotation call",
                 "match": True,
                 "citations": [cite("acc_is_range")]},
                {"field": "rests, fermatas, key signatures, repeats, clefs highlight at normal speed",
                 "code_explanation": "single non-note element -> isSingle() true but element->isNote() FALSE -> "
                                     "the harmonicAnnotation branch is skipped",
                 "match": True,
                 "citations": [cite("acc_is_single"), cite("acc_isnote")]},
                {"field": "spacebar start/stop works INSTANTLY once the highlight has rendered, and not before",
                 "code_explanation": "the synchronous whole-score decode blocks the UI thread; paint AND input "
                                     "dispatch (the spacebar shortcut) starve together and recover together when "
                                     "produceNotationRecord returns — consistent with UI-thread blocking, not an "
                                     "aborted chain (hypothesis (b) is dead)",
                 "match": True,
                 "citations": [cite("chan_sync"), cite("funnel_produce")]},
            ],
            "verdict": (
                "The field pattern is FULLY REPRODUCED by the code facts. The mechanism is a single synchronous "
                "whole-score produceNotationRecord on the UI thread, fired once per single-note selection through "
                "the status-bar accessibility path. One decode per event; no re-trigger loop; the note-seam "
                "status bar is the sole per-selection payer. This confirms OI-206 hypothesis (a) and closes the "
                "call-path confirmation the OI-206 dated notes owe before the fix decision surface."
            ),
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify anchors only; do not write the artifact")
    args = ap.parse_args()

    failures = verify_anchors()
    if failures:
        sys.stderr.write("ANCHOR VERIFICATION FAILED (a citation no longer matches the source — a finding, #13):\n")
        for f in failures:
            sys.stderr.write("  " + f + "\n")
        return 2

    if args.check:
        print(f"OK: all {len(ANCHORS)} anchors verified at HEAD {git_hash()[:10]}")
        return 0

    facts = build_facts()
    manifest = {
        "generated_by": "tools/notation_seams/gen_callpath_facts.py",
        "git_hash": git_hash(),
        "anchor_count": len(ANCHORS),
        "anchors_verified": True,
        "note": (
            "READ-ONLY code-fact extraction; no production code touched. Every claim's citation was re-verified "
            "against the source at this git_hash. Re-run to reproduce; an anchor mismatch exits nonzero."
        ),
    }
    doc = {"manifest": manifest, **facts}
    OUT.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} ({len(ANCHORS)} anchors verified) at HEAD {git_hash()[:10]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
