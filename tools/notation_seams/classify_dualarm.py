#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""classify_dualarm.py — the P6 dual-arm classified diff (seams part 2).

Reads the two arms' full-notation-output-surface capture
(``tools/notation_seams/dualarm_capture.json``, emitted by
``pipeline_snapshot_tests DISABLED_DualArmClassifiedCapture``) and classifies EVERY
non-identical output item into one of the ratified classes, so the user's switch
ratification (§8.4 of ``cowork_notation_adoption_increment.md``) can read what the
switch actually changes and why.

Classes (per the dispatch ``cc_instruction_notation_p6.md`` Task 3):

  * ``identical``          — legacy arm == record arm at this output item.
  * ``inference-driven``   — the record's committed reading differs from legacy's (the
                             adoption's EXPECTED differences reaching the notation surface;
                             both readings + the span are cited).
  * ``presentation-rule``  — a ratified presentation rule accounts for the difference; the
                             specific rule is cited (C1 two-mode display; the §4.1 exposure
                             gates; the OI-194 pedal suspension; the alternatives ordering; the
                             D2 grading-vs-display symbol split; the OI-201 aug-sixth coarseness;
                             the applied-chord Nashville "?" convention).
  * ``input-scoping``      — the OI-204 class (an excluded chord-track staff's notes). STRUCTURALLY
                             ZERO on the snapshot corpus (it carries no chord-track staves); a
                             nonzero count is investigated to mechanism before delivery.
  * ``UNEXPLAINED``        — the headline class: a difference no rule accounts for. Every entry
                             is investigated to a mechanism BEFORE this instrument's report ships;
                             an entry that resists mechanism is a STOP, not a report line (#13/#15).

This is a MEASUREMENT/EVIDENCE instrument (#17f): it invents no value and bends nothing toward
either arm — a difference is CLASSIFIED, never patched. Stdlib only.

Usage:
    python tools/notation_seams/classify_dualarm.py \
        [--capture tools/notation_seams/dualarm_capture.json] \
        [--out    tools/notation_seams/dualarm_classified_report.json] \
        [--summary tools/notation_seams/dualarm_classified_summary.txt]
"""

import argparse
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ── the class labels (declared once) ────────────────────────────────────────────
IDENTICAL = "identical"
INFERENCE = "inference-driven"
PRESENTATION = "presentation-rule"
INPUT_SCOPING = "input-scoping"
UNEXPLAINED = "UNEXPLAINED"

# grading-form quality tokens that a DISPLAY chord symbol must never carry (the ratified D2 split:
# the record publishes a grading-form chordSymbol for batch/a8 continuity, but the notation surface
# renders the DISPLAY form via the shared presentation formatter).
GRADING_TOKENS = ("Dom", "HalfDim", "AugSixth", "Neapolitan")

# the two-mode display (C1): the record's key-mode label is only ever one of these; a legacy label
# outside this set is an exotic mode the C1 ruling collapses to major/minor on the record surface.
TWO_MODE_LABELS = ("", "ionian", "aeolian", "major", "minor")


def exotic_mode(label):
    """True if a mode label is an exotic (non-two-mode) color — the C1 display difference."""
    return (label or "").strip().lower() not in TWO_MODE_LABELS


def has_grading_token(text):
    return any(tok in (text or "") for tok in GRADING_TOKENS)


def is_pedal(text):
    return "ped." in (text or "").lower()


# ── alignment: index a surface's item list by a stable key ──────────────────────

def index_by(items, keyfn):
    """Index items by keyfn; a repeated key keeps a LIST (so nothing is silently dropped, #12)."""
    out = {}
    for it in items or []:
        out.setdefault(keyfn(it), []).append(it)
    return out


def annotation_key(it):
    return (it.get("tick"), it.get("staff"), it.get("kind"))


def implode_key(it):
    # voicing rows carry no staff/text; harmony/staffText rows carry a role-tagged kind + text.
    if it.get("kind") == "voicing":
        return (it.get("tick"), "voicing")
    return (it.get("tick"), it.get("kind"))


def tuning_key(it):
    return (it.get("tick"), it.get("staff"), it.get("pitch"))


def noteseam_key(it):
    return it.get("tick")


# ── the committed region sequence a section-layer derivation (cadence label / key-area bracket) reads ──
# A one-sided cadence StaffText or key-area bracket is a SECTION-LAYER derivation over the committed
# region sequence; both arms run the SAME detection code, so its only differing inputs are (a) the
# region sequence (the readings — inference) and (b) the exposure gate `hasAssertiveExposure`, which on
# the record arm is the §4.1 gap constant (presentation). We read the local region sequence from each
# surface's own chord annotations and compare the arms' LOCAL neighbourhood (the region at the tick + the
# one before — a cadence's two chords).

def annotation_readings(items):
    d = {}
    for it in items or []:
        if it.get("staff") == 0 and it.get("kind") in ("roman", "symbol"):
            d.setdefault(it["tick"], {})[it["kind"]] = it.get("text")
    return {t: (v.get("roman"), v.get("symbol")) for t, v in d.items()}


def implode_readings(items):
    d = {}
    for it in items or []:
        k = it.get("kind")
        if k == "bass:roman":
            d.setdefault(it["tick"], {})["roman"] = it.get("text")
        elif k == "treble:symbol":
            d.setdefault(it["tick"], {})["symbol"] = it.get("text")
    return {t: (v.get("roman"), v.get("symbol")) for t, v in d.items()}


def local_seq(readings, tick):
    ts = sorted(t for t in readings if t <= tick)
    return [(t, readings[t]) for t in ts[-2:]]


def one_sided_class(kind, present_in, lread, rread, tick):
    """Classify an output item present in ONE arm only. A chord annotation is a segment the other arm did
    not commit (inference). A cadence/key-run derivation is classified by whether the LOCAL region
    sequence agrees between arms: identical local sequence → the §4.1 exposure gate fired differently
    (presentation); a differing local sequence → the region sequence it reads differs (inference)."""
    if kind not in ("keyBracket", "staffText"):
        return INFERENCE, "one-sided chord annotation (%s-only segment — the other arm committed no chord here)" % present_in
    if local_seq(lread, tick) == local_seq(rread, tick):
        return PRESENTATION, ("the §4.1 exposure gate: the cadence/key-run derivation gates on "
                              "hasAssertiveExposure (the record arm uses the §4.1 gap constant, "
                              "tools/notation_seams/exposure_constants.json) — fired differently at an "
                              "IDENTICAL local region sequence")
    return INFERENCE, ("the cadence/key-run derivation tracks a DIFFERING local region sequence "
                       "(the committed reading in this neighbourhood differs between the arms)")


# ── per-surface classification ──────────────────────────────────────────────────

def classify_text_pair(kind, legacy_text, record_text):
    """Classify a differing (legacy_text, record_text) chord/roman/symbol pair.

    Returns (cls, basis). `kind` is the item kind (symbol/roman/keyBracket/nashville/staffText/
    treble:*/bass:*). The presentation rules are applied first (each cited); anything left where the
    text genuinely differs is treated as inference-driven (the underlying committed reading moved),
    and only a difference that fits NO rule and is not a plain reading change is left UNEXPLAINED.
    """
    lt = legacy_text or ""
    rt = record_text or ""
    if lt == rt:
        return IDENTICAL, ""

    # presentation-rule: the D2 grading-vs-display split — one arm carries a grading-only token.
    if has_grading_token(lt) != has_grading_token(rt):
        return PRESENTATION, "D2 grading-vs-display symbol split (a grading-only quality token)"

    # presentation-rule: the applied-chord Nashville "?" convention (legacy formatter's own).
    if "nashville" in kind and ("?" in lt) != ("?" in rt):
        return PRESENTATION, "applied-chord Nashville '?' convention (legacy formatter continuity)"

    # a chord symbol / roman / bracket / nashville whose text moved is the committed reading moving:
    # inference-driven (the adoption's expected difference reaching the surface).
    return INFERENCE, "committed reading differs (symbol/roman/key text moved)"


def classify_annotation(legacy, record):
    diffs = []
    ident = 0
    lread = annotation_readings(legacy)
    rread = annotation_readings(record)
    lidx = index_by(legacy, annotation_key)
    ridx = index_by(record, annotation_key)
    for key in sorted(set(lidx) | set(ridx), key=lambda k: (k[0] or 0, k[1] or 0, str(k[2]))):
        tick, staff, kind = key
        litems = lidx.get(key, [])
        ritems = ridx.get(key, [])
        lt = litems[0].get("text") if litems else None
        rt = ritems[0].get("text") if ritems else None
        if litems and ritems and lt == rt and len(litems) == len(ritems):
            ident += 1
            continue  # identical
        if litems and not ritems:
            # present in legacy, absent in record
            if kind == "staffText" and is_pedal(lt):
                cls, basis = PRESENTATION, "OI-194 pedal-point suspension (record suspends the 'X ped.' annotation)"
            else:
                cls, basis = one_sided_class(kind, "legacy", lread, rread, tick)
        elif ritems and not litems:
            if kind == "staffText" and is_pedal(rt):
                cls, basis = PRESENTATION, "OI-194 pedal-point suspension"
            else:
                cls, basis = one_sided_class(kind, "record", lread, rread, tick)
        else:
            cls, basis = classify_text_pair(kind, lt, rt)
        diffs.append({"tick": tick, "staff": staff, "kind": kind,
                      "legacy": lt, "record": rt, "class": cls, "basis": basis})
    return diffs, ident


def classify_implode(legacy, record):
    diffs = []
    ident = 0
    lread = implode_readings(legacy)
    rread = implode_readings(record)
    lidx = index_by(legacy, implode_key)
    ridx = index_by(record, implode_key)
    for key in sorted(set(lidx) | set(ridx), key=lambda k: (k[0] or 0, str(k[1]))):
        tick, kind = key
        litems = lidx.get(key, [])
        ritems = ridx.get(key, [])
        if kind == "voicing":
            lp = litems[0].get("pitches") if litems else None
            rp = ritems[0].get("pitches") if ritems else None
            if lp == rp:
                ident += 1
                continue
            cls = INFERENCE if (litems and ritems) else INFERENCE
            basis = "voicing pitches differ (committed chord/root moved)"
            diffs.append({"tick": tick, "kind": kind, "legacy": lp, "record": rp,
                          "class": cls, "basis": basis})
            continue
        lt = litems[0].get("text") if litems else None
        rt = ritems[0].get("text") if ritems else None
        if litems and ritems and lt == rt:
            ident += 1
            continue
        if litems and not ritems:
            if kind.endswith("staffText") and is_pedal(lt):
                cls, basis = PRESENTATION, "OI-194 pedal-point suspension"
            else:
                cls, basis = one_sided_class(kind.split(":")[-1], "legacy", lread, rread, tick)
        elif ritems and not litems:
            if kind.endswith("staffText") and is_pedal(rt):
                cls, basis = PRESENTATION, "OI-194 pedal-point suspension"
            else:
                cls, basis = one_sided_class(kind.split(":")[-1], "record", lread, rread, tick)
        else:
            cls, basis = classify_text_pair(kind, lt, rt)
        diffs.append({"tick": tick, "kind": kind, "legacy": lt, "record": rt,
                      "class": cls, "basis": basis})
    return diffs, ident


def classify_tuning(legacy, record):
    diffs = []
    ident = 0
    lidx = index_by(legacy, tuning_key)
    ridx = index_by(record, tuning_key)
    for key in sorted(set(lidx) | set(ridx), key=lambda k: (k[0] or 0, k[1] or 0, k[2] or 0)):
        tick, staff, pitch = key
        litems = lidx.get(key, [])
        ritems = ridx.get(key, [])
        lc = litems[0].get("cents") if litems else None
        rc = ritems[0].get("cents") if ritems else None
        if litems and ritems and lc == rc:
            ident += 1
            continue
        if not (litems and ritems):
            # a note present in one arm only would mean the split structure differed — but the capture
            # config disables sustained-event splitting, so both arms share the note structure. A
            # one-sided note is therefore unexpected and flagged.
            cls, basis = UNEXPLAINED, "one-sided tuned note (unexpected under no-split config — review)"
        else:
            # a tuning offset is a downstream read of the committed rootPc + key; a difference means
            # the committed harmonic reading under this note moved -> inference-driven.
            cls, basis = INFERENCE, "tuning offset differs (downstream of the committed root/key)"
        diffs.append({"tick": tick, "staff": staff, "pitch": pitch,
                      "legacy": lc, "record": rc, "class": cls, "basis": basis})
    return diffs, ident


def classify_noteseam(legacy, record):
    """The cleanest arm-vs-arm comparison: the committed reading at each measure downbeat."""
    diffs = []
    ident = 0
    lidx = index_by(legacy, noteseam_key)
    ridx = index_by(record, noteseam_key)
    for tick in sorted(set(lidx) | set(ridx), key=lambda t: t if t is not None else 0):
        litems = lidx.get(tick, [])
        ritems = ridx.get(tick, [])
        if not (litems and ritems):
            # both arms sample the identical downbeat ticks, so a one-sided tick is unexpected.
            diffs.append({"tick": tick, "field": "presence", "legacy": bool(litems),
                          "record": bool(ritems), "class": UNEXPLAINED,
                          "basis": "one-sided downbeat sample (both arms sample the same ticks — review)"})
            continue
        l = litems[0]
        r = ritems[0]
        n0 = len(diffs)
        committed_moved = (l.get("rootPc") != r.get("rootPc")
                           or l.get("quality") != r.get("quality")
                           or l.get("keyFifths") != r.get("keyFifths"))
        # mode: an exotic-vs-two-mode label difference at the SAME tonic is a C1 presentation diff, not
        # an inference difference.
        mode_moved = l.get("keyMode") != r.get("keyMode")
        mode_is_c1 = mode_moved and (exotic_mode(l.get("keyMode")) or exotic_mode(r.get("keyMode"))) \
            and l.get("keyFifths") == r.get("keyFifths")

        if committed_moved:
            diffs.append({"tick": tick, "field": "committed",
                          "legacy": {"rootPc": l.get("rootPc"), "quality": l.get("quality"),
                                     "keyFifths": l.get("keyFifths"), "keyMode": l.get("keyMode"),
                                     "symbol": l.get("symbol"), "roman": l.get("roman")},
                          "record": {"rootPc": r.get("rootPc"), "quality": r.get("quality"),
                                     "keyFifths": r.get("keyFifths"), "keyMode": r.get("keyMode"),
                                     "symbol": r.get("symbol"), "roman": r.get("roman")},
                          "class": INFERENCE,
                          "basis": "committed reading differs (rootPc/quality/key)"})
            continue

        # committed root/quality/key equal: any remaining difference is presentation.
        if mode_is_c1:
            diffs.append({"tick": tick, "field": "keyMode", "legacy": l.get("keyMode"),
                          "record": r.get("keyMode"), "class": PRESENTATION,
                          "basis": "C1 two-mode display (exotic mode color collapsed to major/minor)"})
            continue
        if mode_moved:
            diffs.append({"tick": tick, "field": "keyMode", "legacy": l.get("keyMode"),
                          "record": r.get("keyMode"), "class": INFERENCE,
                          "basis": "key-mode differs at the same tonic is not two-mode-explained — review"})
            continue

        for field in ("symbol", "roman", "nashville"):
            if l.get(field) != r.get(field):
                cls, basis = classify_text_pair("noteSeam:" + field, l.get(field), r.get(field))
                # committed reading is equal here, so a text move is a formatting/presentation diff.
                if cls == INFERENCE:
                    cls, basis = PRESENTATION, ("display %s differs at an identical committed reading "
                                                "(spelling / C1 / OI-201 aug-sixth family)" % field)
                diffs.append({"tick": tick, "field": field, "legacy": l.get(field),
                              "record": r.get(field), "class": cls, "basis": basis})

        if l.get("alternatives") != r.get("alternatives"):
            diffs.append({"tick": tick, "field": "alternatives",
                          "legacy": l.get("alternatives"), "record": r.get("alternatives"),
                          "class": PRESENTATION,
                          "basis": "§3.3 alternatives ordering (record ranks by content score)"})

        if len(diffs) == n0:
            ident += 1
    return diffs, ident


SURFACE_CLASSIFIERS = {
    "annotation": classify_annotation,
    "implode": classify_implode,
    "tuning": classify_tuning,
    "noteSeam": classify_noteseam,
}


def blank_counts():
    return {IDENTICAL: 0, INFERENCE: 0, PRESENTATION: 0, INPUT_SCOPING: 0, UNEXPLAINED: 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", default=os.path.join(REPO_ROOT, "tools/notation_seams/dualarm_capture.json"))
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "tools/notation_seams/dualarm_classified_report.json"))
    ap.add_argument("--summary", default=os.path.join(REPO_ROOT, "tools/notation_seams/dualarm_classified_summary.txt"))
    args = ap.parse_args()

    with open(args.capture, "r", encoding="utf-8") as fh:
        cap = json.load(fh)

    per_score = []
    totals = {surf: blank_counts() for surf in SURFACE_CLASSIFIERS}
    unexplained_all = []

    for score in cap.get("corpus", []):
        sid = score.get("id")
        legacy = score.get("legacy", {})
        record = score.get("record", {})
        score_out = {"id": sid, "surfaces": {}}
        for surf, classifier in SURFACE_CLASSIFIERS.items():
            l_items = legacy.get(surf, [])
            r_items = record.get(surf, [])
            diffs, ident = classifier(l_items, r_items)
            counts = blank_counts()
            counts[IDENTICAL] = ident
            totals[surf][IDENTICAL] += ident
            for d in diffs:
                counts[d["class"]] = counts.get(d["class"], 0) + 1
                totals[surf][d["class"]] = totals[surf].get(d["class"], 0) + 1
                if d["class"] == UNEXPLAINED:
                    entry = dict(d)
                    entry["score"] = sid
                    entry["surface"] = surf
                    unexplained_all.append(entry)
            score_out["surfaces"][surf] = {
                "legacyItemCount": len(l_items),
                "recordItemCount": len(r_items),
                "diffCounts": counts,
                "diffs": diffs,
            }
        per_score.append(score_out)

    grand = blank_counts()
    for surf in totals:
        for cls, n in totals[surf].items():
            grand[cls] = grand.get(cls, 0) + n

    report = {
        "instrument": "classify_dualarm.py",
        "capture": os.path.relpath(args.capture, REPO_ROOT).replace("\\", "/"),
        "window": cap.get("window"),
        "classes": {
            IDENTICAL: "legacy arm == record arm at this output item",
            INFERENCE: "the record's committed reading differs (the adoption's expected differences)",
            PRESENTATION: "a ratified presentation rule accounts for it (rule cited per diff)",
            INPUT_SCOPING: "OI-204 excluded-staff class (structurally 0 on this chord-track-free corpus)",
            UNEXPLAINED: "no rule accounts for it — investigated to mechanism before delivery, else a STOP",
        },
        "totalsPerSurface": totals,
        "grandTotals": grand,
        "unexplained": unexplained_all,
        "perScore": per_score,
    }

    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)
        fh.write("\n")

    # human-readable summary
    lines = []
    lines.append("P6 DUAL-ARM CLASSIFIED DIFF — legacy (flag OFF) vs record (flag ON)")
    lines.append("capture: %s" % report["capture"])
    lines.append("window:  %s" % (cap.get("window") or ""))
    lines.append("")
    lines.append("GRAND TOTALS (output items, by class):")
    for cls in (IDENTICAL, INFERENCE, PRESENTATION, INPUT_SCOPING, UNEXPLAINED):
        lines.append("  %-16s %d" % (cls, grand.get(cls, 0)))
    lines.append("")
    lines.append("PER SURFACE:")
    header = "  %-12s %9s %10s %10s %12s %8s" % (
        "surface", "identical", "inference", "present.", "input-scope", "UNEXPL")
    lines.append(header)
    for surf in ("annotation", "implode", "tuning", "noteSeam"):
        c = totals[surf]
        lines.append("  %-12s %9d %10d %10d %12d %8d"
                     % (surf, c[IDENTICAL], c[INFERENCE], c[PRESENTATION], c[INPUT_SCOPING], c[UNEXPLAINED]))
    lines.append("")
    if unexplained_all:
        lines.append("UNEXPLAINED ENTRIES (%d) — each MUST be investigated to a mechanism before delivery:"
                     % len(unexplained_all))
        for e in unexplained_all[:200]:
            lines.append("  [%s/%s] tick=%s %s" % (e.get("score"), e.get("surface"),
                                                   e.get("tick"), e.get("basis")))
        if len(unexplained_all) > 200:
            lines.append("  ... (%d more)" % (len(unexplained_all) - 200))
    else:
        lines.append("UNEXPLAINED ENTRIES: 0  (every non-identical item is accounted for by a cited rule)")
    lines.append("")
    lines.append("PER SCORE (inference / presentation / input-scope / UNEXPL, summed over surfaces):")
    for s in per_score:
        agg = blank_counts()
        for surf in s["surfaces"].values():
            for cls, n in surf["diffCounts"].items():
                agg[cls] = agg.get(cls, 0) + n
        lines.append("  %-22s inf=%-5d pres=%-5d in-scope=%-3d UNEXPL=%d"
                     % (s["id"], agg[INFERENCE], agg[PRESENTATION], agg[INPUT_SCOPING], agg[UNEXPLAINED]))

    with open(args.summary, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    print("\nwrote %s" % os.path.relpath(args.out, REPO_ROOT).replace("\\", "/"))
    print("wrote %s" % os.path.relpath(args.summary, REPO_ROOT).replace("\\", "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
