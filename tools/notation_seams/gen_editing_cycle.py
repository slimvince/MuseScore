#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""gen_editing_cycle.py — OI-206 / cc_instruction_analysis_cost_profile.md Task 3.

Cost PER USER ACTION in the composing/editing loop, on the RECORD arm (useJointNotationRecord ON = the
production default since the notation switch). Combines the CODE-CITED call-path facts (how many
whole-score produceNotationRecord calls each action triggers) with the MEASURED whole-score produce cost
(tools/notation_seams/noteseam_latency.json + large_score_decode_profile.json). No new C++ run — the
produce count per action is a control-flow fact (cited to file:line), the produce cost is already
measured (#19: never conflate the two, so both are carried with their source).

★ THE UNDO-COUNTER / CACHE-KEY FACT (cited). The legacy bounded-window cache keys on
(score, changeToken, excludeStaves) where changeToken = undoStack->currentIndex()
(notationcomposingbridge.cpp:400). So:
  - a PITCH EDIT commits via apply() -> the undo stack pushes -> currentIndex() ADVANCES -> any memo keyed
    on it is invalidated; AND NotationUndoStack::notifyAboutNotationChanged() fires m_notationChanged
    (notationundostack.cpp:55/77/101 -> :281) -> NotationAccessibility::updateAccessibilityInfo ->
    (single note still selected) -> the note-seam funnel -> one whole-score produceNotationRecord.
  - a NAVIGATION step (next/prev element) fires only m_selectionChanged.notify()
    (notationinteraction.cpp:395); it pushes NO undo command, so currentIndex() is UNCHANGED. On the
    LEGACY arm the window cache would serve it warm; on the RECORD arm there is NO cache
    (produceNotationRecord memoizes nothing — OI-203), so it pays one whole-score produce.
  - a MULTI-NOTE add-harmony command calls the funnel ONCE PER SELECTED NOTE
    (notationinteraction.cpp:8256/8311 — OI-213), so N notes -> N whole-score produces.

So on the record arm EVERY interactive action pays >= 1 full whole-score decode; the legacy window cache
served navigation and warm re-queries from a bounded window, which the record arm does not. This is the
OI-203 / OI-206 regression, quantified per action here.

Artifact (#17f): tools/notation_seams/editing_cycle.json. Read-only.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
NS = REPO / "tools" / "notation_seams"


def load(p):
    p = Path(p)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(REPO)).decode().strip()
    except Exception:
        return "unknown"


# produces-per-action (control-flow FACTS, cited); each maps to whole-score produceNotationRecord calls.
ACTIONS = [
    {
        "action": "navigation step (next/prev element; e.g. left/right arrow)",
        "is_edit": False,
        "advances_undo_index": False,
        "produces_record_arm": 1,
        "produces_legacy_arm": 0,   # served warm from the bounded-window cache after the first build
        "citations": [
            "src/notation/internal/notationinteraction.cpp:395 (m_selectionChanged.notify on move)",
            "src/notation/internal/notationaccessibility.cpp:118/203 (single-note -> funnel)",
            "src/notation/internal/notationcomposingbridge.cpp:732 (record-arm produceNotationRecord)",
            "src/notation/internal/notationcomposingbridge.cpp:400 (changeToken = undoStack currentIndex — UNCHANGED on navigation)",
        ],
        "note": "Selection change, no edit. Undo index unchanged. Record arm: 1 whole-score produce, "
                "no cache. Legacy arm: served from the bounded-window cache (warm).",
    },
    {
        "action": "pitch change (up/down arrow on a selected note)",
        "is_edit": True,
        "advances_undo_index": True,
        "produces_record_arm": 1,   # via notationChanged -> updateAccessibilityInfo (single note stays selected)
        "produces_legacy_arm": 1,   # the cache is invalidated (undo index advanced), so the legacy arm also rebuilds
        "citations": [
            "src/notation/internal/notationundostack.cpp:55/77/101 -> :281 (apply/undo/redo -> notifyAboutNotationChanged)",
            "src/notation/internal/notationaccessibility.cpp:48/110 (notationChanged -> updateAccessibilityInfo)",
            "src/notation/internal/notationcomposingbridge.cpp:732 (record-arm produceNotationRecord)",
            "src/notation/internal/notationcomposingbridge.cpp:400 (changeToken advances on the commit)",
        ],
        "note": "An EDIT: apply() pushes to the undo stack (currentIndex advances -> any memo keyed on it "
                "is invalidated) and fires notationChanged -> the funnel -> one whole-score produce. The "
                "undo-index advance is why a (score, change-token) record cache is re-paid EACH keystroke "
                "on a sustained pitch-edit session (it is a NEW key every keystroke). A produce that also "
                "re-notifies the selection could add a second produce (call-path q2 caveat); >=1 per keystroke.",
    },
    {
        "action": "add analyzed harmony to selection (multi-note command)",
        "is_edit": True,
        "advances_undo_index": True,
        "produces_record_arm": "N (once per selected note)",
        "produces_legacy_arm": "N",
        "citations": [
            "src/notation/internal/notationinteraction.cpp:8256 (addAnalyzedHarmonyToSelection)",
            "src/notation/internal/notationinteraction.cpp:8311 (funnel call inside the per-note loop over byStaffTick)",
        ],
        "note": "N-note selection -> N whole-score produces (OI-213). A keyed (score, change-token) record "
                "cache would collapse the N to 1 (the note views are microsecond lookups into the one record).",
    },
]


def main():
    latency = load(NS / "noteseam_latency.json")
    decode = load(NS / "large_score_decode_profile.json")

    # produce_cold per size class (ms) — from the measured latency (perf corpus) + decode profile (orchestral)
    produce_cost = []
    if latency:
        for s in latency.get("scores", []):
            produce_cost.append({
                "id": s["id"], "sizeClass": s.get("sizeClass"), "measures": s.get("measures"),
                "notes": s.get("notes"), "produce_cold_ms": s.get("produce_cold_ms_median"),
                "source": "noteseam_latency.json (C++ whole-score produceNotationRecord, cold)",
            })
    if decode:
        for s in decode.get("scores", []):
            if "phase3_decode_ms" in s:
                total = (s.get("phase1_build_facts_ms", 0) + s.get("phase2_load_tables_ms", 0)
                         + s.get("phase3_decode_ms", 0) + s.get("phase4_assemble_ms", 0))
                produce_cost.append({
                    "id": s["id"], "sizeClass": s.get("sizeClass", "large"),
                    "events": s.get("adapterEvents"), "notes": s.get("adapterNotes"),
                    "produce_cold_ms": total,
                    "source": "large_score_decode_profile.json (phase1+2+3+4, the whole produce)",
                })

    # cost per action = produces_record_arm * produce_cold_ms, tabulated per size class
    per_action = []
    for a in ACTIONS:
        entry = dict(a)
        costs = []
        for pc in produce_cost:
            n = a["produces_record_arm"]
            if isinstance(n, int) and pc.get("produce_cold_ms") is not None:
                costs.append({"id": pc["id"], "produce_cold_ms": pc["produce_cold_ms"],
                              "record_arm_cost_ms": n * pc["produce_cold_ms"]})
        entry["record_arm_cost_by_score"] = costs
        entry["multi_note_note"] = ("cost = N x produce_cold_ms; for an N-note selection on a score whose "
                                    "produce is P ms, the command costs N*P ms.") if not isinstance(a["produces_record_arm"], int) else None
        per_action.append(entry)

    out = {
        "provenance": {
            "generator": "tools/notation_seams/gen_editing_cycle.py",
            "instrument_commit": git_hash(),
            "open_item": "OI-206 / cc_instruction_analysis_cost_profile.md Task 3",
            "arm": "record (useJointNotationRecord ON = production default since the notation switch)",
            "method": "produces-per-action is a control-flow FACT (cited to file:line); produce_cold_ms is "
                      "the MEASURED whole-score produceNotationRecord cost (noteseam_latency.json + "
                      "large_score_decode_profile.json); cost-per-action = produces x produce_cold (#19: "
                      "the two are carried with their sources, never conflated).",
        },
        "undo_counter_fact": {
            "change_token": "undoStack->currentIndex() (notationcomposingbridge.cpp:400)",
            "edit_advances_index": True,
            "navigation_advances_index": False,
            "consequence": "On the record arm there is no cache, so every action pays >=1 whole-score "
                           "produce. A (score, change-token) record cache would serve navigation and "
                           "warm re-queries; but a sustained pitch-edit session advances the token every "
                           "keystroke, so the cache is re-paid each keystroke there (the edit loop is the "
                           "hard case a cache alone does not solve — the extent/frequency axes do).",
        },
        "produce_cost_by_score": produce_cost,
        "actions": per_action,
    }
    (NS / "editing_cycle.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                           encoding="utf-8")
    print("wrote", NS / "editing_cycle.json")
    for a in per_action:
        print(f"  {a['action'][:40]:40s} edit={a['is_edit']} undo+={a['advances_undo_index']} "
              f"produces(record)={a['produces_record_arm']}")


if __name__ == "__main__":
    main()
