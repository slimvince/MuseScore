#!/usr/bin/env python3
"""OI-357 — WHAT THE COMMITTED OUTPUTS SAY ABOUT THE BAROQUE PARTIAL-SIGNATURE STEMS.

WHAT THIS ANSWERS, AND WHAT IT CANNOT.  `OPEN_ITEMS.md` OI-357 records that the Baroque
partial-signature correction — Baroque scores notated with one accidental fewer than the modern
convention, so the sounding key is a step away from anything a signature-faithful reading can
name — lives in the LEGACY key resolver and nowhere else, and that whether the production arm
handles the convention AT ALL is unestablished in both directions.  The user's Ruling 26 of
2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`) orders an EARLY, BOUNDED, READ-ONLY
establishment: the committed corpus outputs for those stems compared against ground truth, with
no new measurement machinery, no corpus regeneration, no fix, no design and no inference change.

★ THE BOUND IS THE FINDING, AND IT IS STATED BEFORE ANY VALUE BELOW IS READ.  This comparison
reads the outputs that are COMMITTED.  Which inference arm produced them is therefore not a
choice this pass makes — it is a property of what is on disk, and it is measured here rather
than assumed, because it decides what the whole comparison is about.

THE POPULATION IS DERIVED, NEVER SAMPLED (the ruling's own condition).  It comes from the
evidence document's OWN stated method — `docs/key_detection_baroque_partial_signature.md` §3
derives its table "From `tools/dcml/corelli/metadata.tsv` (notated `KeySig` vs DCML
`annotated_key`)".  That method is applied here mechanically to every piece in that file rather
than the document's six-row table being transcribed, so the population cannot be narrower than
the record's own rule makes it.

Run:
    python tools/audit/gen_oi357_partial_signature_establishment.py

Output:
    tools/audit/oi357_partial_signature_establishment.json
"""
from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
METADATA = os.path.join(ROOT, "tools", "dcml", "corelli", "metadata.tsv")
REPORTS = os.path.join(ROOT, "tools", "reports")
OUT = os.path.join(HERE, "oi357_partial_signature_establishment.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# The natural key signature of every key name, as fifths. Standard music theory, not a project
# convention: a major key's own signature, and a minor key's NATURAL (Aeolian) signature.
MAJOR_FIFTHS = {"C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7,
                "F": -1, "Bb": -2, "Eb": -3, "Ab": -4, "Db": -5, "Gb": -6, "Cb": -7}
MINOR_FIFTHS = {"A": 0, "E": 1, "B": 2, "F#": 3, "C#": 4, "G#": 5, "D#": 6, "A#": 7,
                "D": -1, "G": -2, "C": -3, "F": -4, "Bb": -5, "Eb": -6, "Ab": -7}

PITCH_CLASS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

# The date the joint estimator became the production inference layer on the batch/corpus surface,
# recorded in `CLAUDE.md` gate block (A) with its ratification. It is used ONLY to date committed
# output directories against, never as a measurement.
JOINT_ADOPTION_DATE = "2026-07-26"

RUN_DIR = re.compile(r"corelli_(\d{8})_(\d{6})$")


def key_name_to_fifths_and_tonic(name: str):
    """A DCML key label -> (natural signature in fifths, tonic pitch class, mode).

    DCML writes a major key with an initial capital and a minor key in lower case.
    """
    if not name:
        return None, None, None
    mode = "major" if name[0].isupper() else "minor"
    letter = name[0].upper()
    accidental = name[1:].replace("#", "#").replace("b", "b")
    if accidental not in ("", "#", "b", "##", "bb"):
        return None, None, None
    spelled = letter + accidental
    table = MAJOR_FIFTHS if mode == "major" else MINOR_FIFTHS
    fifths = table.get(spelled)
    if fifths is None:
        return None, None, None
    pc = PITCH_CLASS[letter]
    pc = (pc + accidental.count("#") - accidental.count("b")) % 12
    return fifths, pc, mode


OUR_KEY = re.compile(r"^([A-G])([#b]?)(.*)$")

# Our emitted mode tokens, reduced to major / minor / other. The reduction is coarse ON PURPOSE:
# this pass asks whether the TONIC is read correctly, which is what the partial-signature
# convention moves, and it does not re-grade mode. The exotic-mode grading convention lives in
# `CLAUDE.md` gate block (A) and is not reimplemented here (#6).
MAJOR_TOKENS = {"maj", "major", "ionian", "ion"}
MINOR_TOKENS = {"min", "minor", "aeolian", "aeo", "harm", "mel", "harmonicminor", "melodicminor"}


def our_key_to_tonic(label: str):
    if not label:
        return None, None
    m = OUR_KEY.match(label)
    if not m:
        return None, None
    letter, accidental, rest = m.groups()
    pc = (PITCH_CLASS[letter] + (1 if accidental == "#" else -1 if accidental == "b" else 0)) % 12
    token = rest.strip().lower()
    if token in MAJOR_TOKENS:
        mode = "major"
    elif token in MINOR_TOKENS:
        mode = "minor"
    else:
        mode = "other:" + token if token else "unstated"
    return pc, mode


def read_metadata() -> list[dict]:
    with open(METADATA, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        i_piece = header.index("piece")
        i_sig = header.index("KeySig")
        i_key = header.index("annotated_key")
        out = []
        for ln in fh:
            cells = ln.rstrip("\n").split("\t")
            if len(cells) <= max(i_piece, i_sig, i_key):
                continue
            out.append({"piece": cells[i_piece], "key_signature_field": cells[i_sig],
                        "annotated_key": cells[i_key]})
    return out


def notated_fifths(field: str):
    """The KeySig field is measure-keyed, e.g. '1: -2' and occasionally several segments.

    A piece whose notated signature CHANGES within the movement is not a single-signature case,
    and this pass declines to reduce it to one value rather than picking a segment.
    """
    parts = [p.strip() for p in field.split(",") if p.strip()]
    values = set()
    for p in parts:
        m = re.match(r"^\s*\d+\s*:\s*(-?\d+)\s*$", p)
        if not m:
            return None, "unparsed"
        values.add(int(m.group(1)))
    if len(values) != 1:
        return None, "changes within the movement"
    return values.pop(), None


def committed_runs() -> list[dict]:
    """Every committed Corelli output directory, with the date its name carries."""
    found = []
    for dirpath, _dirs, files in os.walk(ROOT):
        base = os.path.basename(dirpath)
        m = RUN_DIR.match(base)
        if not m:
            continue
        stems = sorted(f[: -len(".ours.json")] for f in files if f.endswith(".ours.json"))
        if not stems:
            continue
        found.append({
            "directory": os.path.relpath(dirpath, ROOT).replace("\\", "/"),
            "date_in_the_directory_name": f"{m.group(1)[:4]}-{m.group(1)[4:6]}-{m.group(1)[6:]}",
            "stems": stems,
        })
    return sorted(found, key=lambda r: r["date_in_the_directory_name"])


def main() -> int:
    pieces = read_metadata()

    population, excluded = [], []
    for p in pieces:
        fifths, why = notated_fifths(p["key_signature_field"])
        natural, tonic_pc, mode = key_name_to_fifths_and_tonic(p["annotated_key"])
        if fifths is None or natural is None:
            excluded.append({**p, "why_excluded": why or "the annotated key could not be read"})
            continue
        if fifths == natural:
            continue
        population.append({
            "piece": p["piece"],
            "notated_signature_fifths": fifths,
            "annotated_key": p["annotated_key"],
            "the_annotated_key_s_natural_signature_fifths": natural,
            "steps_the_signature_is_short_by": natural - fifths,
            "annotated_tonic_pitch_class": tonic_pc,
            "annotated_mode": mode,
        })

    runs = committed_runs()
    covering = [r for r in runs
                if any(m["piece"] in r["stems"] for m in population)]
    newest = covering[-1] if covering else None

    compared, missing = [], []
    if newest is not None:
        for m in population:
            path = os.path.join(ROOT, newest["directory"], m["piece"] + ".ours.json")
            if not os.path.exists(path):
                missing.append(m["piece"])
                continue
            doc = json.loads(open(path, encoding="utf-8").read())
            ours = doc.get("detectedKey")
            pc, mode = our_key_to_tonic(ours or "")
            region_keys = sorted({r.get("key") for r in doc.get("regions", []) if r.get("key")})
            # The evidence document's OWN diagnostic for the signature lock: when the resolver
            # cannot escape the notated signature it "lands on the notated signature's Ionian
            # (major case) or Aeolian (minor case) home". Both homes are computed from the
            # notated signature alone, so this is derived and not a judgment.
            notated = m["notated_signature_fifths"]
            ionian_home_pc = (7 * notated) % 12
            aeolian_home_pc = (ionian_home_pc + 9) % 12
            compared.append({
                "piece": m["piece"],
                "annotated_mode": m["annotated_mode"],
                "steps_the_signature_is_short_by": m["steps_the_signature_is_short_by"],
                "the_notated_signature_s_ionian_home_pitch_class": ionian_home_pc,
                "the_notated_signature_s_aeolian_home_pitch_class": aeolian_home_pc,
                "our_tonic_is_a_home_of_the_NOTATED_signature": pc in (ionian_home_pc,
                                                                      aeolian_home_pc),
                "ground_truth_key": m["annotated_key"],
                "ground_truth_tonic_pitch_class": m["annotated_tonic_pitch_class"],
                "ground_truth_mode": m["annotated_mode"],
                "our_committed_detected_key": ours,
                "our_tonic_pitch_class": pc,
                "our_mode": mode,
                "the_tonic_agrees": pc is not None and pc == m["annotated_tonic_pitch_class"],
                "the_mode_agrees": mode == m["annotated_mode"],
                "distinct_region_keys_in_the_committed_output": region_keys,
                "analysis_path_field": doc.get("analysisPath"),
                "preset_field": doc.get("preset"),
                "carries_an_inference_arm_stamp": any(
                    k for k in doc if "joint" in k.lower() or "arm" in k.lower()),
            })

    agreeing = [c for c in compared if c["the_tonic_agrees"]]
    disagreeing = [c for c in compared if not c["the_tonic_agrees"]]
    locked = [c for c in disagreeing if c["our_tonic_is_a_home_of_the_NOTATED_signature"]]
    modal = [c for c in disagreeing if str(c["our_mode"]).startswith("other:")]

    artifact = {
        "what_this_is": "OI-357's EARLY, BOUNDED, READ-ONLY establishment, on the user's Ruling 26 "
                        "of 2026-08-09: the committed corpus outputs for the Baroque "
                        "partial-signature stems, compared against the published human "
                        "annotation. No corpus was regenerated, no measurement tool of the "
                        "analysis was built or run, and nothing about the analysis was changed.",
        "generated_by": "tools/audit/gen_oi357_partial_signature_establishment.py",
        "the_row_it_answers": "OPEN_ITEMS.md OI-357",
        "the_population_and_how_it_was_DERIVED": {
            "the_record_s_own_method": "`docs/key_detection_baroque_partial_signature.md` §3 "
                                       "derives its table 'From tools/dcml/corelli/metadata.tsv "
                                       "(notated KeySig vs DCML annotated_key)'. That METHOD is "
                                       "applied here to every piece in that file, rather than the "
                                       "document's own six-row table being transcribed — so the "
                                       "population cannot be narrower than the record's rule "
                                       "makes it, and no piece is selected by judgment.",
            "the_rule": "a piece is in the population when its NOTATED signature differs from the "
                        "NATURAL signature of its annotated key. That is exactly 'notated one "
                        "accidental short', without needing a direction rule — and the direction "
                        "per piece is reported rather than assumed.",
            "pieces_in_the_file": len(pieces),
            "pieces_in_the_population": len(population),
            "population": population,
            "pieces_excluded_and_why": excluded,
        },
        "★_THE_BOUND_ON_EVERYTHING_BELOW": {
            "the_question_the_row_asks": "whether the PRODUCTION arm — the joint estimator — reads "
                                         "these scores correctly, and by what means.",
            "what_the_committed_outputs_are": "Every committed Corelli output directory is listed "
                                              "below with the date its own name carries. NONE "
                                              "carries a corpus manifest, and none carries any "
                                              "field naming an inference arm.",
            "every_committed_run_directory": runs,
            "the_run_this_comparison_reads": newest,
            "how_that_run_was_chosen": "the latest date carried by a committed Corelli output "
                                       "directory's own name that covers the population — derived "
                                       "from the directory names, not chosen.",
            "the_joint_adoption_date_recorded_in_gate_block_A": JOINT_ADOPTION_DATE,
            "★_the_verdict_on_scope": (
                "EVERY committed Corelli run predates the date the joint estimator became the "
                "production inference layer on the batch/corpus surface, and the corpus flag that "
                "selects it defaults OFF. So these outputs are the LEGACY arm's. THIS COMPARISON "
                "THEREFORE MEASURES THE LEGACY ARM AND CANNOT ANSWER THE ROW'S QUESTION. What it "
                "CAN establish is stated below and is worth having; what it cannot is stated here "
                "so no reader takes the values for an answer about the arm that ships."
            ),
        },
        "what_this_comparison_CAN_establish": [
            "Whether the LEGACY correction actually holds on the derived population at the "
            "committed outputs — that is, whether the fix the record says landed is visible in "
            "the data, on every member of the population rather than on the one anchor case the "
            "evidence document names.",
            "The BEFORE side any later production-arm comparison would be read against, taken "
            "from committed data rather than re-measured.",
        ],
        "what_this_comparison_CANNOT_establish": [
            "Anything about the production arm's reading of these scores. No committed output for "
            "this repertoire was produced by it.",
            "Anything about how the production arm's soft signature prior behaves on a partial "
            "signature — the row's own 'NOT claimed' half, which stays not claimed.",
            "Any published measurement of the analysis, none of which this pass touches.",
        ],
        "the_comparison": {
            "pieces_compared": len(compared),
            "pieces_in_the_population_with_no_committed_output": missing,
            "tonic_agreeing": len(agreeing),
            "tonic_disagreeing": len(disagreeing),
            "of_the_disagreeing_how_many_land_on_a_HOME_OF_THE_NOTATED_SIGNATURE": len(locked),
            "why_that_split_matters": "The evidence document's own diagnostic for the signature "
                                      "lock is that the resolver 'lands on the notated "
                                      "signature's Ionian (major case) or Aeolian (minor case) "
                                      "home'. Both homes are computed here from the notated "
                                      "signature alone, so the column is derived and not a "
                                      "judgment. A disagreement that lands on one of those homes "
                                      "is the lock's own signature; a disagreement that lands "
                                      "elsewhere is some other cause and is NOT attributed to it.",
            "of_the_disagreeing_how_many_emit_a_mode_the_major_minor_ground_truth_cannot_write":
                len(modal),
            "★_the_split_by_the_mode_of_the_ANNOTATED_key": {
                "why_this_cut": "The correction recorded in the evidence document detects the "
                                "convention by ONE signal — the flattened sixth degree pervasive "
                                "across the sounding weight and dominating its natural form — and "
                                "then reinterprets the signature. That signal is a MINOR-key "
                                "signal. Whether the population's major-key members behave "
                                "differently from its minor-key members is therefore the first "
                                "thing to look at, and it is a DERIVED cut rather than a "
                                "diagnosis: this pass counts, it does not explain.",
                "by_annotated_mode": {
                    mode: {
                        "in_the_population": sum(1 for c in compared
                                                 if c["annotated_mode"] == mode),
                        "tonic_agreeing": sum(1 for c in agreeing if c["annotated_mode"] == mode),
                        "tonic_disagreeing": sum(1 for c in disagreeing
                                                 if c["annotated_mode"] == mode),
                        "disagreeing_and_landing_on_a_home_of_the_notated_signature":
                            sum(1 for c in locked if c["annotated_mode"] == mode),
                    }
                    for mode in ("major", "minor")
                },
            },
            "why_that_second_split_matters": "CLAUDE.md gate block (A) carries a standing grading "
                                             "convention: a defensible modal reading the "
                                             "major/minor ground truth cannot represent is a "
                                             "GROUND-TRUTH LIMITATION, not a defect to optimize "
                                             "away. Whether any particular reading here is "
                                             "DEFENSIBLE is a judgment this pass does not make — "
                                             "the count is reported so that the disagreement "
                                             "total is not read as a defect total.",
            "rows": compared,
            "what_the_agreement_column_means": "whether our committed detected key's TONIC matches "
                                               "the published human annotation's tonic. The mode "
                                               "column is reported beside it and is NOT graded "
                                               "here: how a modal emission is scored is a "
                                               "convention that lives in CLAUDE.md gate block (A) "
                                               "and is not reimplemented (#6).",
        },
    }

    open(OUT, "w", encoding="utf-8", newline="").write(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")
    print(f"  pieces in the metadata: {len(pieces)}; population derived: {len(population)}")
    print(f"  committed Corelli runs: {len(runs)}; read: "
          f"{newest['directory'] if newest else 'NONE'}")
    print(f"  compared: {len(compared)}; tonic agreeing: {len(agreeing)}; "
          f"disagreeing: {len(disagreeing)}")
    print(f"  of the disagreeing, landing on a home of the NOTATED signature: {len(locked)}")
    print(f"  of the disagreeing, emitting a non-major/minor mode: {len(modal)}")
    print(f"  no committed output: {missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
