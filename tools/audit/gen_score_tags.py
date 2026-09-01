#!/usr/bin/env python3
"""Count notated elements in every .mscx of a named set of directories.

WHAT THIS IS. A counting pass over score files, producing one row per file at
``tools/audit/score_tags_l0l1_sweep.json``. Every value in a row is a COUNT or a
verbatim string taken from the file. Nothing here is an estimate and nothing is a
judgment: there is no suitability column, no ranking, and no tag that says a file
is worth staging.

WHAT IT IS NOT. It is not a measurement of this project's analysis. No count below
is an output of the analyzer; every one is a property of a score file as written.
Whole-corpus counts say what the held corpora cannot exercise; they must not be
used to choose an exemplar, which is a representativeness question this pass does
not answer (Ruling 20, bound 4).

THE SCOPE IS AN ARGUMENT, NOT A HIDDEN CONSTANT. ``DIRECTORIES`` below is the
default and may be replaced wholesale on the command line. The sweep is
NON-RECURSIVE: exactly the ``*.mscx`` files in each named directory, never a
subdirectory of one.

Usage:
    python tools/audit/gen_score_tags.py [--out PATH] [DIR ...]
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

# --- The default scope. Replaceable on the command line; never hidden. -------
DIRECTORIES = [
    "tools/dcml/bach_chorales/MS3",
    "tools/dcml/couperin_clavecin/MS3",
    "tools/dcml/scarlatti_sonatas/MS3",
    "tools/dcml/handel_keyboard/MS3",
    "tools/dcml/cpe_bach_keyboard/MS3",
    "tools/dcml/bach_en_fr_suites/MS3",
    "tools/dcml/frescobaldi_fiori_musicali/MS3",
    "tools/audit/derivation_exemplars/l0-l1",
]

DEFAULT_OUT = "tools/audit/score_tags_l0l1_sweep.json"

# A grace-note marker is an EMPTY child element of <Chord> whose tag is one of
# these. The vocabulary is the MuseScore file format's own; every distinct
# empty-child tag actually observed is reported beside the counts, so a marker
# outside this set is visible rather than silently uncounted.
GRACE_TAG_RE = re.compile(r"^(appoggiatura|acciaccatura|grace\d+(after)?)$")

# Numeric columns, in report order. Each is a count taken from the file.
NUMERIC_COLUMNS = [
    "bytes",
    "harmony", "figured_bass", "staff_text",
    "part_list_staves", "body_staves",
    "fermata", "fermata_articulations", "tie_starts", "tie_spanner_endpoints", "pedal",
    "start_repeat", "end_repeat", "volta", "barline_double", "rest",
    "distinct_time_signatures", "distinct_key_signatures",
    "notes_invisible", "notes_non_sounding",
    "measures", "chords", "notes",
    "articulations_total", "ornament_articulations",
    "appoggiatura", "acciaccatura", "grace_chords",
    "tremolo", "trill", "cue_sized_small",
]

# Categorical columns: a verbatim string read from the file.
CATEGORICAL_COLUMNS = [
    "sha256", "musescore_version", "program_version", "program_revision",
]


def _text(elem):
    return (elem.text or "").strip() if elem is not None else None


def _subtype_of(elem):
    """The <subtype> child's text, or the marker for an element carrying none."""
    child = elem.find("subtype")
    return _text(child) if child is not None else "(no subtype element)"


def scan_file(path):
    """Return one row for one .mscx file. A parse failure is REPORTED in the row."""
    row = {"path": path.replace(os.sep, "/")}
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        row["read_error"] = "%s: %s" % (type(exc).__name__, exc)
        return row

    row["bytes"] = len(data)
    row["sha256"] = hashlib.sha256(data).hexdigest()

    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        row["parse_error"] = "%s: %s" % (type(exc).__name__, exc)
        return row

    # --- The complete element-tag histogram. Every other count is checked
    # --- against it, so no derived figure can exceed what the file holds.
    tag_counts = {}
    total_elements = 0
    parent_of = {}
    for parent in root.iter():
        for child in parent:
            parent_of[id(child)] = parent
    for elem in root.iter():
        total_elements += 1
        tag_counts[elem.tag] = tag_counts.get(elem.tag, 0) + 1
    row["_tag_histogram"] = dict(sorted(tag_counts.items()))
    row["total_elements"] = total_elements

    def n(tag):
        return tag_counts.get(tag, 0)

    # --- (a) Identity and fitness ------------------------------------------
    row["musescore_version"] = root.get("version")
    row["program_version"] = _text(root.find("programVersion"))
    row["program_revision"] = _text(root.find("programRevision"))

    score = root.find("Score")
    if score is None:
        row["structure_error"] = "no <Score> element"
        return row

    row["harmony"] = n("Harmony")
    row["figured_bass"] = n("FiguredBass")
    row["staff_text"] = n("StaffText")

    part_list_staves = sum(len(part.findall("Staff")) for part in score.findall("Part"))
    body_staves = len(score.findall("Staff"))
    row["part_list_staves"] = part_list_staves
    row["body_staves"] = body_staves

    # --- (b) Notated elements ----------------------------------------------
    row["fermata"] = n("Fermata")
    row["tie_starts"] = n("Tie")
    row["tie_spanner_endpoints"] = sum(
        1 for e in root.iter("Spanner") if e.get("type") == "Tie"
    )
    row["pedal"] = n("Pedal")
    row["start_repeat"] = n("startRepeat")
    row["end_repeat"] = n("endRepeat")
    row["volta"] = n("Volta")

    barline_subtypes = {}
    for elem in root.iter("BarLine"):
        subtype = _subtype_of(elem)
        barline_subtypes[subtype] = barline_subtypes.get(subtype, 0) + 1
    row["barline_subtypes"] = dict(sorted(barline_subtypes.items()))
    row["barline_total"] = n("BarLine")
    row["barline_double"] = barline_subtypes.get("double", 0)

    row["rest"] = n("Rest")

    time_sigs = []
    for elem in root.iter("TimeSig"):
        sig_n = _text(elem.find("sigN"))
        sig_d = _text(elem.find("sigD"))
        time_sigs.append("%s/%s" % (sig_n, sig_d))
    row["time_signatures_listed"] = sorted(set(time_sigs))
    row["time_signature_elements"] = len(time_sigs)
    row["distinct_time_signatures"] = len(row["time_signatures_listed"])

    key_sigs = []
    for elem in root.iter("KeySig"):
        acc = elem.find("accidental")
        key_sigs.append(_text(acc) if acc is not None else "(no accidental element)")
    row["key_signatures_listed"] = sorted(set(key_sigs))
    row["key_signature_elements"] = len(key_sigs)
    row["distinct_key_signatures"] = len(row["key_signatures_listed"])

    # Invisibility is a <visible>0</visible> CHILD element in this format, not a
    # visible="0" attribute. Both forms are counted so the absent one is visible
    # as absent rather than assumed away.
    notes_invisible = 0
    notes_non_sounding = 0
    for note in root.iter("Note"):
        vis = note.find("visible")
        if vis is not None and _text(vis) == "0":
            notes_invisible += 1
        if note.get("visible") == "0":
            notes_invisible += 1
        play = note.find("play")
        if play is not None and _text(play) == "0":
            notes_non_sounding += 1
    row["notes_invisible"] = notes_invisible
    row["notes_non_sounding"] = notes_non_sounding
    row["visible_attribute_form_seen"] = any(
        e.get("visible") is not None for e in root.iter()
    )

    row["measures"] = n("Measure")
    row["chords"] = n("Chord")
    row["notes"] = n("Note")

    # --- (c) Elements bearing on the open faces -----------------------------
    # COUNTS OF NOTATED ELEMENTS AND NOTHING MORE. No row here claims that any of
    # these opens a change point or sounds; that is the deriving session's question.
    artic_subtypes = {}
    for elem in root.iter("Articulation"):
        subtype = _subtype_of(elem)
        artic_subtypes[subtype] = artic_subtypes.get(subtype, 0) + 1
    row["articulation_subtypes"] = dict(sorted(artic_subtypes.items()))
    row["articulations_total"] = n("Articulation")
    # "ornament" is the format's own name prefix on these subtype strings — a
    # lexical fact about the file, not a judgment about what an ornament is.
    row["ornament_articulations"] = sum(
        count for name, count in artic_subtypes.items() if name.startswith("ornament")
    )
    row["ornament_articulation_subtypes"] = {
        name: count for name, count in sorted(artic_subtypes.items())
        if name.startswith("ornament")
    }
    # A fermata is written EITHER as a <Fermata> element OR as an <Articulation>
    # whose subtype begins "fermata". Both forms occur in the swept population, so
    # the <Fermata> count alone would understate where a fermata exists. Both are
    # reported; neither is folded into the other.
    row["fermata_articulations"] = sum(
        count for name, count in artic_subtypes.items() if name.startswith("fermata")
    )
    row["fermata_articulation_subtypes"] = {
        name: count for name, count in sorted(artic_subtypes.items())
        if name.startswith("fermata")
    }

    row["appoggiatura"] = n("appoggiatura")
    row["acciaccatura"] = n("acciaccatura")

    grace_markers = {}
    grace_chords = 0
    chord_child_tags = set()
    for chord in root.iter("Chord"):
        matched = False
        for child in chord:
            chord_child_tags.add(child.tag)
            if GRACE_TAG_RE.match(child.tag):
                grace_markers[child.tag] = grace_markers.get(child.tag, 0) + 1
                matched = True
        if matched:
            grace_chords += 1
    row["grace_chord_markers"] = dict(sorted(grace_markers.items()))
    row["grace_chords"] = grace_chords
    row["_chord_child_tags"] = sorted(chord_child_tags)

    row["tremolo"] = n("Tremolo")
    row["trill"] = n("Trill")

    small_parents = {}
    for parent in root.iter():
        for child in parent:
            if child.tag == "small":
                small_parents[parent.tag] = small_parents.get(parent.tag, 0) + 1
    row["cue_sized_small"] = n("small")
    row["cue_sized_small_parents"] = dict(sorted(small_parents.items()))

    # --- The reconciliation. DT-26: a derived count that does not reconcile
    # --- against the file's own element totals is REPORTED, never absorbed.
    checks = {
        "part_list_plus_body_staves_equals_Staff_tag_count":
            part_list_staves + body_staves == n("Staff"),
        "barline_subtype_histogram_sums_to_BarLine_tag_count":
            sum(barline_subtypes.values()) == n("BarLine"),
        "articulation_subtype_histogram_sums_to_Articulation_tag_count":
            sum(artic_subtypes.values()) == n("Articulation"),
        "time_signature_elements_equals_TimeSig_tag_count":
            len(time_sigs) == n("TimeSig"),
        "key_signature_elements_equals_KeySig_tag_count":
            len(key_sigs) == n("KeySig"),
        "grace_marker_total_equals_appoggiatura_plus_acciaccatura_plus_graceN":
            sum(grace_markers.values())
            == n("appoggiatura") + n("acciaccatura")
            + sum(c for t, c in tag_counts.items() if re.match(r"^grace\d+(after)?$", t)),
        "grace_chords_not_greater_than_chords": grace_chords <= n("Chord"),
        "notes_invisible_not_greater_than_notes": notes_invisible <= n("Note"),
        "notes_non_sounding_not_greater_than_notes": notes_non_sounding <= n("Note"),
        "tie_starts_not_greater_than_tie_spanner_endpoints":
            n("Tie") <= row["tie_spanner_endpoints"],
    }
    row["reconciliation"] = checks
    row["reconciliation_all_pass"] = all(checks.values())
    return row


def enumerate_directory(directory):
    """The .mscx files directly in ``directory``. NON-RECURSIVE by design."""
    if not os.path.isdir(directory):
        return None
    names = sorted(
        name for name in os.listdir(directory)
        if name.lower().endswith(".mscx")
        and os.path.isfile(os.path.join(directory, name))
    )
    return [os.path.join(directory, name) for name in names]


def distribution(rows):
    """Per column: zero count, min, max, distinct values — over the whole sweep."""
    out = {}
    for column in NUMERIC_COLUMNS:
        values = [r[column] for r in rows if isinstance(r.get(column), int)]
        entry = {
            "kind": "numeric",
            "files_with_a_value": len(values),
            "files_with_zero": sum(1 for v in values if v == 0),
            "files_non_zero": sum(1 for v in values if v != 0),
            "minimum": min(values) if values else None,
            "maximum": max(values) if values else None,
            "distinct_values": len(set(values)),
        }
        entry["non_discriminating"] = entry["distinct_values"] <= 1
        out[column] = entry
    for column in CATEGORICAL_COLUMNS:
        values = [r[column] for r in rows if r.get(column) is not None]
        distinct = sorted(set(values))
        entry = {
            "kind": "categorical",
            "files_with_a_value": len(values),
            "distinct_values": len(distinct),
            "non_discriminating": len(distinct) <= 1,
        }
        # A digest is distinct per file by construction; listing 600+ of them
        # would bury the finding. Every other categorical column lists its values.
        if column != "sha256":
            entry["values"] = distinct
        out[column] = entry
    return out


def per_corpus_non_zero(rows_by_dir):
    out = {}
    for directory, rows in rows_by_dir.items():
        entry = {"files": len(rows)}
        for column in NUMERIC_COLUMNS:
            values = [r[column] for r in rows if isinstance(r.get(column), int)]
            entry[column] = sum(1 for v in values if v != 0)
        out[directory] = entry
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directories", nargs="*", default=None,
                        help="directories to sweep (default: the DIRECTORIES constant)")
    parser.add_argument("--out", default=DEFAULT_OUT)
    args = parser.parse_args(argv)

    directories = args.directories if args.directories else list(DIRECTORIES)

    script_path = os.path.abspath(__file__)
    with open(script_path, "rb") as handle:
        script_sha256 = hashlib.sha256(handle.read()).hexdigest()

    swept = []
    missing = []
    rows = []
    rows_by_dir = {}
    for directory in directories:
        files = enumerate_directory(directory)
        if files is None:
            missing.append(directory)
            continue
        swept.append({"directory": directory, "mscx_files": len(files)})
        dir_rows = [scan_file(path) for path in files]
        rows_by_dir[directory] = dir_rows
        rows.extend(dir_rows)

    failures = [r["path"] for r in rows if "parse_error" in r or "read_error" in r
                or "structure_error" in r]
    unreconciled = [r["path"] for r in rows if r.get("reconciliation_all_pass") is False]

    ok_rows = [r for r in rows if r.get("reconciliation_all_pass") is not None]

    dist = distribution(ok_rows)
    non_discriminating = sorted(
        name for name, entry in dist.items() if entry["non_discriminating"]
    )

    # --- Task 4: the four lists, as paths and nothing more. No ranking, no
    # --- recommendation, no candidate mark.
    grace_files = [
        {"path": r["path"], "grace_chords": r["grace_chords"],
         "by_marker": r["grace_chord_markers"]}
        for r in ok_rows if r.get("grace_chords")
    ]
    ornament_files = [
        {"path": r["path"], "ornament_articulations": r["ornament_articulations"],
         "by_subtype": r["ornament_articulation_subtypes"]}
        for r in ok_rows if r.get("ornament_articulations")
    ]
    multi_timesig_files = [
        {"path": r["path"], "time_signatures": r["time_signatures_listed"]}
        for r in ok_rows if r.get("distinct_time_signatures", 0) > 1
    ]
    fermata_files = [
        {"path": r["path"],
         "fermata_elements": r["fermata"],
         "fermata_articulations": r["fermata_articulations"]}
        for r in ok_rows
        if r.get("fermata") or r.get("fermata_articulations")
    ]
    plain_files = [
        r["path"] for r in ok_rows
        if r.get("harmony") == 0 and r.get("figured_bass") == 0
        and r.get("staff_text") == 0
    ]
    plain_per_corpus = {
        directory: sum(
            1 for r in dir_rows
            if r.get("harmony") == 0 and r.get("figured_bass") == 0
            and r.get("staff_text") == 0
        )
        for directory, dir_rows in rows_by_dir.items()
    }

    # The whole observed vocabulary, so nothing counted-by-name is invisible.
    all_chord_child_tags = sorted({
        t for r in ok_rows for t in r.get("_chord_child_tags", [])
    })
    all_articulation_subtypes = sorted({
        s for r in ok_rows for s in r.get("articulation_subtypes", {})
    })
    all_barline_subtypes = sorted({
        s for r in ok_rows for s in r.get("barline_subtypes", {})
    })
    # Every element name in the whole swept population. This is the DT-26 defense
    # for the named columns: a reader can check here that no element spelling a
    # named column is about was missed, without opening 648 rows.
    all_tags = {}
    for r in ok_rows:
        for tag, count in r.get("_tag_histogram", {}).items():
            all_tags[tag] = all_tags.get(tag, 0) + count

    # Population totals for the list-valued columns, so "each subtype named and
    # counted" is answered over the whole sweep and not only per file, and so the
    # distinct-value count of a list-valued column is readable.
    def population_totals(field):
        totals = {}
        files_carrying = {}
        for r in ok_rows:
            for name, count in r.get(field, {}).items():
                totals[name] = totals.get(name, 0) + count
                files_carrying[name] = files_carrying.get(name, 0) + 1
        return {
            "distinct_values": len(totals),
            "elements_total": dict(sorted(totals.items())),
            "files_carrying_it": dict(sorted(files_carrying.items())),
        }

    def population_value_sets(field):
        totals = {}
        for r in ok_rows:
            for value in r.get(field, []):
                totals[value] = totals.get(value, 0) + 1
        return {
            "distinct_values": len(totals),
            "files_carrying_it": dict(sorted(totals.items())),
        }

    list_valued = {
        "articulation_subtypes": population_totals("articulation_subtypes"),
        "ornament_articulation_subtypes":
            population_totals("ornament_articulation_subtypes"),
        "fermata_articulation_subtypes":
            population_totals("fermata_articulation_subtypes"),
        "barline_subtypes": population_totals("barline_subtypes"),
        "grace_chord_markers": population_totals("grace_chord_markers"),
        "cue_sized_small_parents": population_totals("cue_sized_small_parents"),
        "time_signatures_listed": population_value_sets("time_signatures_listed"),
        "key_signatures_listed": population_value_sets("key_signatures_listed"),
    }

    document = {
        "what_this_is": (
            "One row per .mscx file: counts of notated elements and verbatim "
            "identity strings, taken from the file. No value here is an output of "
            "this project's analyzer, and no column is a judgment, a suitability "
            "mark or a ranking. Whole-corpus counts say what the held corpora "
            "cannot exercise; they answer an EXISTENCE question and must not be "
            "used to pick an exemplar, which is a representativeness question "
            "this pass does not answer."
        ),
        "generated": datetime.date.today().isoformat(),
        "script": {
            "path": "tools/audit/gen_score_tags.py",
            "sha256": script_sha256,
        },
        "scope": {
            "directories_swept": swept,
            "directories_missing_reported_and_skipped": missing,
            "recursive": False,
            "pattern": "*.mscx",
            "total_files": len(rows),
        },
        "failures": {
            "files_that_failed_to_parse_or_read": failures,
            "files_whose_counts_did_not_reconcile": unreconciled,
        },
        "format_vocabulary_observed": {
            "chord_direct_child_tags": all_chord_child_tags,
            "articulation_subtypes": all_articulation_subtypes,
            "barline_subtypes": all_barline_subtypes,
            "every_element_tag_in_the_swept_population":
                dict(sorted(all_tags.items())),
        },
        "distribution_over_the_swept_population": dist,
        "distribution_of_the_list_valued_columns": list_valued,
        "non_discriminating_columns": non_discriminating,
        "files_with_a_non_zero_value_per_corpus_per_column": per_corpus_non_zero(rows_by_dir),
        "the_two_open_slots_answered_by_existence": {
            "a_grace_note_files": grace_files,
            "a_ornament_files": ornament_files,
            "b_more_than_one_distinct_time_signature": multi_timesig_files,
            "c_non_zero_fermata": fermata_files,
            "d_plain_files": plain_files,
            "d_plain_files_per_corpus": plain_per_corpus,
        },
        "rows": rows,
    }

    out_path = args.out
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        json.dump(document, handle, indent=1, ensure_ascii=False, sort_keys=False)
        handle.write("\n")

    print("files swept: %d" % len(rows))
    print("directories swept: %d, missing: %d" % (len(swept), len(missing)))
    print("parse/read failures: %d" % len(failures))
    print("rows failing reconciliation: %d" % len(unreconciled))
    print("non-discriminating columns: %d" % len(non_discriminating))
    print("wrote %s" % out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
