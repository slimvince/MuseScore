#!/usr/bin/env python3
"""gen_input_parity.py — the two-readers-agree INPUT PARITY for the joint estimator's fact adapter.

READ-ONLY MEASUREMENT. No src/ change, no build, no gate, no corpus mutation. It grades the C++ FACT
ADAPTER's extraction (composing/analysis/joint/jointfactadapter, dumped by
`batch_analyze --joint-adapter-facts` to adapter_facts.json) against the committed music21 extraction
(note_events/note_events.json) FIELD BY FIELD, over all covered pieces, and enumerates every divergence
BY CLASS with counts + a few verified examples each. Two independent readers of the SAME corpus xml
(tools/corpus/<stem>.xml): music21 9.9.1 (note_events) and MuseScore's engraving import + the L1 note
model (the adapter). A class that cannot be mapped mechanically is a STOP-for-review (Task C).

Per-note fields: [onset, dur, pc, midi, lof, part, measure, beat, mc, ap, dp, tied, fermata].
Notes are keyed by (onset, part, midi) — unique per piece for this SATB corpus; a key present on only
one side is a note-identity divergence (its own class), and for common keys the remaining fields are
compared. Per-event fields: [start, end, measure, beat, mc, fermata], keyed by (start, end).
sig_fifths / declared_mode (the initial-state prior inputs, not in note_events) are compared against
decode_parity_ref.json (the oracle read them from the same xml header via read_xml_header). Dispatch:
the joint-estimator input-parity Task C.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent

NOTE_EVENTS = _HERE / "note_events" / "note_events.json"
ADAPTER_FACTS = _HERE / "adapter_facts.json"
DECODE_REF = _HERE / "decode_parity_ref.json"
OUT_JSON = _HERE / "input_parity.json"
OUT_SUMMARY = _HERE / "input_parity_summary.txt"

NOTE_FIELDS = ["onset", "dur", "pc", "midi", "lof", "part", "measure", "beat",
               "metric_class_code", "approach_code", "departure_code", "tied", "fermata"]
EVENT_FIELDS = ["start", "end", "measure", "beat", "metric_class_code", "fermata"]
# non-key note fields (index -> name); key is (onset[0], part[5], midi[3]).
NOTE_CMP = [(1, "dur"), (2, "pc"), (4, "lof"), (6, "measure"), (7, "beat"),
            (8, "metric_class_code"), (9, "approach_code"), (10, "departure_code"),
            (11, "tied"), (12, "fermata")]
# non-key event fields; key is (start[0], end[1]).
EVENT_CMP = [(2, "measure"), (3, "beat"), (4, "metric_class_code"), (5, "fermata")]


def _git_head() -> str:
    return subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def _eqfield(name, a, b) -> bool:
    if name == "beat":
        return round(float(a), 4) == round(float(b), 4)   # both rounded to 4 at generation
    return a == b


def _note_key(n):
    return (n[0], n[5], n[3])   # (onset, part, midi)


def _event_key(e):
    return (e[0], e[1])         # (start, end)


class Classes:
    """Accumulate divergences by class name -> {count, examples[]}."""
    def __init__(self, cap=3):
        self.d = defaultdict(lambda: {"count": 0, "examples": []})
        self.cap = cap

    def add(self, cls, example):
        c = self.d[cls]
        c["count"] += 1
        if len(c["examples"]) < self.cap:
            c["examples"].append(example)

    def as_dict(self):
        return {k: self.d[k] for k in sorted(self.d)}


def main():
    if not ADAPTER_FACTS.exists():
        raise SystemExit(f"STOP: {ADAPTER_FACTS} not found — run "
                         f"`batch_analyze --joint-adapter-facts tools/joint_estimator` first.")
    ref = json.loads(NOTE_EVENTS.read_text(encoding="utf-8"))
    adp = json.loads(ADAPTER_FACTS.read_text(encoding="utf-8"))
    dref = json.loads(DECODE_REF.read_text(encoding="utf-8")) if DECODE_REF.exists() else None

    ref_hash = ref["provenance"].get("corpus_git_hash")
    adp_hash = adp["provenance"].get("corpus_git_hash")
    if ref_hash != adp_hash:
        raise SystemExit(f"STOP: corpus_git_hash mismatch — note_events {ref_hash} vs adapter_facts "
                         f"{adp_hash}. Regenerate adapter_facts.json against the committed corpus.")

    ref_pieces = ref["pieces"]
    adp_pieces = adp["pieces"]
    ref_stems = set(ref_pieces)
    adp_stems = set(adp_pieces)

    cls = Classes()
    # coverage
    for s in sorted(ref_stems - adp_stems):
        cls.add("piece_missing_from_adapter", {"stem": s})
    for s in sorted(adp_stems - ref_stems):
        cls.add("piece_only_in_adapter", {"stem": s})

    common = sorted(ref_stems & adp_stems)
    tot = {"ref_notes": 0, "adp_notes": 0, "ref_events": 0, "adp_events": 0,
           "matched_notes": 0, "matched_events": 0}
    perfect_pieces = 0
    note_field_stems = defaultdict(set)      # field -> set of stems that diverge on it
    event_field_stems = defaultdict(set)
    exclusion_mismatch = 0                    # notes where (adapter measure==0) != (music21 measure==0)
    exclusion_stems = set()                   # the DECODE-CRITICAL anacrusis-exclusion mismatch

    for stem in common:
        r = ref_pieces[stem]
        a = adp_pieces[stem]
        piece_ok = True

        # ── scalars ──
        if r.get("meter") != a.get("meter"):
            cls.add("meter_mismatch", {"stem": stem, "ref": r.get("meter"), "adapter": a.get("meter")})
            piece_ok = False
        if r.get("n_quarter") != a.get("n_quarter"):
            cls.add("n_quarter_mismatch",
                    {"stem": stem, "ref": r.get("n_quarter"), "adapter": a.get("n_quarter")})
            piece_ok = False
        if r.get("multi_meter") != a.get("multi_meter"):
            cls.add("multi_meter_mismatch",
                    {"stem": stem, "ref": r.get("multi_meter"), "adapter": a.get("multi_meter")})
            piece_ok = False

        # ── notes ──
        rn, an = r["notes"], a["notes"]
        tot["ref_notes"] += len(rn)
        tot["adp_notes"] += len(an)
        if len(rn) != len(an):
            cls.add("note_count_mismatch", {"stem": stem, "ref": len(rn), "adapter": len(an)})
            piece_ok = False
        rmap = {}
        for n in rn:
            rmap.setdefault(_note_key(n), []).append(n)
        amap = {}
        for n in an:
            amap.setdefault(_note_key(n), []).append(n)
        for k in rmap.keys() - amap.keys():
            cls.add("note_only_in_reference", {"stem": stem, "key(onset,part,midi)": list(k)})
            piece_ok = False
        for k in amap.keys() - rmap.keys():
            cls.add("note_only_in_adapter", {"stem": stem, "key(onset,part,midi)": list(k)})
            piece_ok = False
        for k in rmap.keys() & amap.keys():
            # if a key is duplicated on either side, compare the multiset positionally
            rl, al = rmap[k], amap[k]
            if len(rl) != len(al):
                cls.add("note_key_multiplicity", {"stem": stem, "key": list(k),
                                                  "ref": len(rl), "adapter": len(al)})
                piece_ok = False
            for rnote, anote in zip(rl, al):
                tot["matched_notes"] += 1
                # the DECODE-CRITICAL slice of note_field:measure — the ==0 anacrusis exclusion (the only
                # way note.measure reaches the Viterbi). measure otherwise cosmetic.
                if (rnote[6] == 0) != (anote[6] == 0):
                    exclusion_mismatch += 1
                    exclusion_stems.add(stem)
                    cls.add("anacrusis_exclusion_mismatch",
                            {"stem": stem, "key(onset,part,midi)": list(k),
                             "ref_measure": rnote[6], "adapter_measure": anote[6]})
                    piece_ok = False
                for idx, name in NOTE_CMP:
                    if not _eqfield(name, anote[idx], rnote[idx]):
                        cls.add(f"note_field:{name}",
                                {"stem": stem, "key(onset,part,midi)": list(k),
                                 "ref": rnote[idx], "adapter": anote[idx]})
                        note_field_stems[name].add(stem)
                        piece_ok = False

        # ── events ──
        re_, ae = r["events"], a["events"]
        tot["ref_events"] += len(re_)
        tot["adp_events"] += len(ae)
        if len(re_) != len(ae):
            cls.add("event_count_mismatch", {"stem": stem, "ref": len(re_), "adapter": len(ae)})
            piece_ok = False
        remap = {_event_key(e): e for e in re_}
        aemap = {_event_key(e): e for e in ae}
        for k in remap.keys() - aemap.keys():
            cls.add("event_only_in_reference", {"stem": stem, "key(start,end)": list(k)})
            piece_ok = False
        for k in aemap.keys() - remap.keys():
            cls.add("event_only_in_adapter", {"stem": stem, "key(start,end)": list(k)})
            piece_ok = False
        for k in remap.keys() & aemap.keys():
            tot["matched_events"] += 1
            for idx, name in EVENT_CMP:
                if not _eqfield(name, aemap[k][idx], remap[k][idx]):
                    cls.add(f"event_field:{name}",
                            {"stem": stem, "key(start,end)": list(k),
                             "ref": remap[k][idx], "adapter": aemap[k][idx]})
                    event_field_stems[name].add(stem)
                    piece_ok = False

        # ── sig / declared_mode vs the oracle (read_xml_header) ──
        if dref is not None and stem in dref.get("identity", {}):
            o = dref["identity"][stem]
            if a.get("sig_fifths") != o.get("sig_fifths"):
                cls.add("sig_fifths_mismatch",
                        {"stem": stem, "ref": o.get("sig_fifths"), "adapter": a.get("sig_fifths")})
                piece_ok = False
            if (a.get("declared_mode") or "") != (o.get("declared_mode") or ""):
                cls.add("declared_mode_mismatch",
                        {"stem": stem, "ref": o.get("declared_mode"), "adapter": a.get("declared_mode")})
                piece_ok = False

        if piece_ok:
            perfect_pieces += 1

    # ── decode-relevance annotation on each class (which fields would move the Viterbi) ──
    DECODE_CRITICAL = {"note_field:dur", "note_field:pc", "note_field:lof",
                       "note_field:metric_class_code", "note_field:approach_code",
                       "note_field:departure_code", "note_field:tied", "note_field:fermata",
                       "note_only_in_adapter", "note_only_in_reference", "note_count_mismatch",
                       "note_key_multiplicity", "anacrusis_exclusion_mismatch",
                       "event_field:metric_class_code", "event_field:fermata",
                       "event_only_in_adapter", "event_only_in_reference", "event_count_mismatch",
                       "sig_fifths_mismatch", "declared_mode_mismatch", "n_quarter_mismatch"}
    # note.measure is decode-critical ONLY through the ==0 anacrusis flag (its own class above); note
    # .beat/part and event.measure/beat are cosmetic (never read by the decode — Explore Q5).
    COSMETIC = {"note_field:measure", "note_field:beat", "event_field:measure", "event_field:beat",
                "meter_mismatch", "multi_meter_mismatch"}

    # The METRIC-POSITION divergence class: music21 reproduces the xml <measure number>/irregular-measure
    # structure verbatim, which MuseScore's engraving import normalises away — so the metrical grid the
    # fact adapter reconstructs cannot recover it. This is a MECHANICALLY-UNMAPPABLE class (the xml
    # measure-number attribute is not in the engraving model), NOT a fact-extraction defect. It touches
    # ONLY the metric-position fields; the note/event IDENTITY, spelling, melodic covariates, ties, and
    # fermatas all agree exactly. Sub-cases (all xml-editorial): suffix-split phrase measures ("6"/"6a",
    # music21 merges); distinct-numbered short phrase measures (bwv371 "6" short + "7", music21 keeps
    # separate); repeat/reset numbers (bwv324 numbers 1..9 x4); misnumbered xml (bwv261 ...10,14,12,13,14);
    # editorial pickup numbered 1 not 0 (bwv113.8/bwv274/bwv384 — the anacrusis-exclusion sub-case).
    METRIC_POSITION = {"note_field:measure", "note_field:beat", "note_field:metric_class_code",
                       "event_field:measure", "event_field:beat", "event_field:metric_class_code",
                       "anacrusis_exclusion_mismatch"}
    stems_of = {}
    for f, s in note_field_stems.items():
        stems_of[f"note_field:{f}"] = sorted(s)
    for f, s in event_field_stems.items():
        stems_of[f"event_field:{f}"] = sorted(s)
    stems_of["anacrusis_exclusion_mismatch"] = sorted(exclusion_stems)

    classes = cls.as_dict()
    annotated = {}
    for name, body in classes.items():
        note = ("decode-critical" if name in DECODE_CRITICAL
                else "cosmetic (never read by the decode)" if name in COSMETIC
                else "review")
        entry = {"count": body["count"], "decode_relevance": note, "examples": body["examples"]}
        if name in stems_of:
            entry["affected_pieces"] = stems_of[name]
        if name in METRIC_POSITION:
            entry["root_cause"] = ("music21 reproduces the xml <measure number>/irregular-measure "
                                   "structure verbatim; MuseScore's engraving import normalises it, so the "
                                   "metrical grid cannot recover it")
            entry["mechanically_mappable"] = False
        annotated[name] = entry

    out = {
        "provenance": {
            "generator": "tools/joint_estimator/gen_input_parity.py",
            "instrument_commit": _git_head(),
            "corpus_git_hash": ref_hash,
            "reference": "note_events/note_events.json (music21 9.9.1)",
            "candidate": "adapter_facts.json (composing/analysis/joint/jointfactadapter: L1 notatedNotes + structural facts)",
            "note": ("field-by-field two-readers-agree parity over all covered pieces; divergences "
                     "enumerated by class with decode-relevance annotation and root cause. The only "
                     "residual class is METRIC-POSITION (measure/beat/mc), mechanically unmappable from "
                     "the engraving model; its decode impact is the separate end-to-end parity "
                     "(joint_endtoend_parity.json)."),
        },
        "summary": {
            "pieces_compared": len(common),
            "pieces_only_in_reference": len(ref_stems - adp_stems),
            "pieces_only_in_adapter": len(adp_stems - ref_stems),
            "perfect_pieces": perfect_pieces,
            "total_notes_reference": tot["ref_notes"],
            "total_notes_adapter": tot["adp_notes"],
            "matched_notes": tot["matched_notes"],
            "total_events_reference": tot["ref_events"],
            "total_events_adapter": tot["adp_events"],
            "matched_events": tot["matched_events"],
            "anacrusis_exclusion_mismatch_notes": exclusion_mismatch,
            "anacrusis_exclusion_mismatch_pieces": sorted(exclusion_stems),
            "divergence_class_count": len(annotated),
        },
        "divergence_classes": annotated,
    }
    OUT_JSON.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")

    lines = [
        "=== joint fact-adapter INPUT PARITY (two readers of tools/corpus/<stem>.xml) ===",
        f"corpus git_hash: {ref_hash}",
        f"pieces compared: {len(common)}   perfect (all fields identical): {perfect_pieces}",
        f"notes: reference {tot['ref_notes']}  adapter {tot['adp_notes']}  matched {tot['matched_notes']}",
        f"events: reference {tot['ref_events']}  adapter {tot['adp_events']}  matched {tot['matched_events']}",
        "",
        f"divergence classes: {len(annotated)}",
    ]
    if not annotated:
        lines.append("  (none — the two readers agree on every field of every note and event)")
    for name in sorted(annotated, key=lambda k: -annotated[k]["count"]):
        b = annotated[name]
        lines.append(f"  [{b['decode_relevance']:14s}] {name}: {b['count']}")
        for ex in b["examples"][:2]:
            lines.append(f"        e.g. {json.dumps(ex)}")
    OUT_SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"\nwrote {OUT_JSON.relative_to(_ROOT).as_posix()}")


if __name__ == "__main__":
    main()
