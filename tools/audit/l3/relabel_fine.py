#!/usr/bin/env python3
"""Layer-3 pass-2 fine-label re-derivation (EG-7 / OI-84 / OI-100).

Mechanical join of the hand-authored recorded judgment
(pass2_fine_relabel_judgments.json) against the FROZEN blind reading artifacts
(pass2_blind_reading.json / pass2_blind_errorrate.json). This script performs
ONLY parse / join / totality-check / axis-consistency-check / count / render.

The fine label per row is fixed by the row's reason code in the judgment file;
the reason -> (fine verdict, prose_decided, axis) map below is the protocol P2
vocabulary. No source file, no manifest, no re-measurement, blind to pass 1.

Outputs (never hand-edited):
  tools/audit/l3/pass2_fine_relabel_reading.csv / .json
  tools/audit/l3/pass2_fine_relabel_errorrate.csv / .json
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# reason code -> (fine verdict, prose_decided, axis it belongs to)
REASON_MAP = {
    "CODE_LIVE":               ("SURVIVES",                True,  "code"),
    "STRUCT_THEORY":           ("ESTABLISHED",             True,  "constants"),
    "STRUCT_MECH":             ("ESTABLISHED",             True,  "constants"),
    "STRUCT_BOUND":            ("ESTABLISHED",             True,  "constants"),
    "FITTED_UNRESOLVED":       ("UNRESOLVABLE-FROM-PROSE", False, "constants"),
    "FITTED_PROVISIONAL_UNFIT":("UNFIT",                   True,  "constants"),
    "PUB_CONSUMER":            ("PUBLISHED",               True,  "derived"),
    "DEAD_VESTIGIAL":          ("DEAD",                    True,  "constants"),
}

# one-sentence justification template per reason code (paraphrases the prose logic)
REASON_JUSTIFY = {
    "CODE_LIVE": "Prose asserts the code is correct/live with no deadness or retirement signal -> SURVIVES.",
    "STRUCT_THEORY": "Prose grounds the literal as a music-theory / pitch-class / scale-degree fact -> ESTABLISHED.",
    "STRUCT_MECH": "Prose grounds the literal as code mechanics (array size, capacity hint, mod-12, zero-init, div-guard, structural constant) -> ESTABLISHED.",
    "STRUCT_BOUND": "Prose identifies the literal as a fitter search-range bound with the default confirmed inside it -> ESTABLISHED.",
    "FITTED_UNRESOLVED": "Prose argues empirical/in-bounds/theory-ordering/live but never engages fit provenance, which separates ESTABLISHED from UNFIT -> UNRESOLVABLE-FROM-PROSE.",
    "FITTED_PROVISIONAL_UNFIT": "Prose explicitly flags the fit as provisional/not-final, so it is not positively established (#19); live, not dead -> UNFIT.",
    "PUB_CONSUMER": "Prose names a live consumer of the derived fact -> PUBLISHED.",
    "DEAD_VESTIGIAL": "Prose says the field/write is read nowhere / vestigial -> DEAD.",
}

# allowed fine verdicts per axis (protocol P2), plus the universal UNRESOLVABLE escape
AXIS_VERDICTS = {
    "code":      {"SURVIVES", "RETIRES", "UNRESOLVABLE-FROM-PROSE"},
    "constants": {"ESTABLISHED", "UNFIT", "DEAD", "UNRESOLVABLE-FROM-PROSE"},
    "derived":   {"PUBLISHED", "SILOED", "TRAPPED", "DUPLICATED", "UNRESOLVABLE-FROM-PROSE"},
}


def axis_of_row(kind, coarse):
    """Structural axis derived mechanically from the row's kind + coarse verdict."""
    if kind in ("branch", "function", "crosslayer"):
        return "code"
    if kind == "literal":
        return "constants"
    if kind == "field":
        # a field holding a numeric parameter/constant was coarse-labeled ESTABLISHED/DEAD;
        # a field carrying a derived data value was coarse-labeled PUBLISHED.
        if coarse in ("ESTABLISHED", "DEAD"):
            return "constants"
        if coarse == "PUBLISHED":
            return "derived"
    raise ValueError(f"cannot assign axis for kind={kind!r} coarse={coarse!r}")


def process(sample, frozen_path, judgments):
    frozen = json.load(open(frozen_path, encoding="utf-8"))
    rows = frozen["rows"]
    by_po = {r["process_order"]: r for r in rows}
    j_by_po = {}
    for j in judgments:
        if j["po"] in j_by_po:
            raise ValueError(f"{sample}: duplicate judgment for po={j['po']}")
        j_by_po[j["po"]] = j

    # totality (P1): every frozen row has exactly one judgment, no extra judgments
    frozen_pos = set(by_po)
    judged_pos = set(j_by_po)
    if frozen_pos != judged_pos:
        missing = sorted(frozen_pos - judged_pos)
        extra = sorted(judged_pos - frozen_pos)
        raise ValueError(f"{sample}: totality violated. missing judgments={missing} extra judgments={extra}")

    out_rows = []
    for po in sorted(by_po):
        r = by_po[po]
        j = j_by_po[po]
        reason = j["reason"]
        if reason not in REASON_MAP:
            raise ValueError(f"{sample} po={po}: unknown reason {reason!r}")
        fine, prose_decided, want_axis = REASON_MAP[reason]
        kind = r["kind"]
        coarse = r["verdict"]
        axis = axis_of_row(kind, coarse)
        # axis-consistency check (P2): the reason code's axis must match the row's structural axis
        if axis != want_axis:
            raise ValueError(f"{sample} po={po}: reason {reason} implies axis {want_axis} but row axis is {axis}")
        if fine not in AXIS_VERDICTS[axis]:
            raise ValueError(f"{sample} po={po}: fine {fine} not allowed on axis {axis}")
        # prose_decided is False iff the fine label is the unresolvable escape
        if (fine == "UNRESOLVABLE-FROM-PROSE") != (not prose_decided):
            raise ValueError(f"{sample} po={po}: prose_decided/fine mismatch")
        justification = REASON_JUSTIFY[reason]
        note = j.get("note", "")
        out_rows.append({
            "process_order": po,
            "row_id": r["row_id"],
            "kind": kind,
            "file": r["file"],
            "line": r["line"],
            "label": r["label"],
            "coarse_verdict": coarse,
            "axis": axis,
            "fine_verdict": fine,
            "prose_decided": "yes" if prose_decided else "no",
            "reason_code": reason,
            "justification": justification,
            "note": note,
            "coarse_reasoning": r["reasoning"],
        })

    # counts
    def tally(key):
        d = {}
        for o in out_rows:
            d[o[key]] = d.get(o[key], 0) + 1
        return dict(sorted(d.items()))

    fine_counts = tally("fine_verdict")
    axis_counts = tally("axis")
    prose_decided_counts = tally("prose_decided")
    # constants axis breakdown (the axis the coarse vocabulary most plausibly collapsed)
    constants_breakdown = {}
    for o in out_rows:
        if o["axis"] == "constants":
            constants_breakdown[o["fine_verdict"]] = constants_breakdown.get(o["fine_verdict"], 0) + 1
    constants_breakdown = dict(sorted(constants_breakdown.items()))

    summary = {
        "sample": sample,
        "n_rows": len(out_rows),
        "fine_verdict_counts": fine_counts,
        "axis_counts": axis_counts,
        "prose_decided_counts": prose_decided_counts,
        "constants_axis_breakdown": constants_breakdown,
    }

    base = os.path.join(HERE, f"pass2_fine_relabel_{sample}")
    cols = ["process_order", "row_id", "kind", "file", "line", "label",
            "coarse_verdict", "axis", "fine_verdict", "prose_decided",
            "reason_code", "justification", "note", "coarse_reasoning"]
    with open(base + ".csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for o in out_rows:
            w.writerow(o)
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "rows": out_rows}, f, indent=1)
    return summary


def main():
    judg = json.load(open(os.path.join(HERE, "pass2_fine_relabel_judgments.json"), encoding="utf-8"))
    summaries = {}
    summaries["reading"] = process("reading", os.path.join(HERE, "pass2_blind_reading.json"), judg["reading"])
    summaries["errorrate"] = process("errorrate", os.path.join(HERE, "pass2_blind_errorrate.json"), judg["errorrate"])
    print(json.dumps(summaries, indent=1))


if __name__ == "__main__":
    sys.exit(main())
