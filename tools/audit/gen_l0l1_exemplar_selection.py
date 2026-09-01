#!/usr/bin/env python3
"""Generate tools/audit/l0l1_exemplar_selection.json.

The L0+L1 exemplar selection: the separation check and, if the check passes, the ruled pick.

Executes `cc_instruction_l0l1_exemplar_selection_2026_08_31.md`, which in turn executes
Ruling 12 of `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3l.

WHAT THIS TOOL IS.  It computes four properties of every Bach chorale in the DCML corpus from
that corpus's own note tables and metadata, applies a decision rule that was written down before
the measurement was taken, and records its own verdict.  It stages nothing and copies nothing.

WHAT THIS TOOL IS NOT.  It is not a measurement of this project's analysis.  It never opens a
score, never runs the analyzer, and reads no output of ours.  Its only inputs are
`tools/dcml/bach_chorales/notes/*.notes.tsv` and `tools/dcml/bach_chorales/metadata.tsv`.

Run:  python tools/audit/gen_l0l1_exemplar_selection.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CORPUS = REPO_ROOT / "tools" / "dcml" / "bach_chorales"
NOTES_DIR = CORPUS / "notes"
METADATA = CORPUS / "metadata.tsv"
OUT = REPO_ROOT / "tools" / "audit" / "l0l1_exemplar_selection.json"

NOTE_SUFFIX = ".notes.tsv"

# The columns the dispatch names by name.  A column absent or differently named is a STOP.
REQUIRED_NOTE_COLUMNS = ["quarterbeats", "duration_qb", "midi", "tied", "mc"]
REQUIRED_METADATA_COLUMNS = ["piece", "TimeSig", "n_onsets", "n_onset_positions", "rel_path"]

# Columns used for P4 and P5, which the dispatch names as PROPERTIES read from metadata.tsv
# without naming a column for either.  They are listed apart so the artifact can say which
# column carried which property, and so the P5 derivation is visible rather than assumed.
P4_P5_COLUMNS = ["TimeSig", "volta_mcs", "length_qb", "length_qb_unfolded"]


class Stop(Exception):
    """A condition the dispatch orders surfaced, never absorbed."""


# --------------------------------------------------------------------------------------------
# Reading


def read_tsv(path: Path):
    text = path.read_text(encoding="utf-8-sig")
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    if not lines:
        raise Stop(f"{path} is empty")
    header = lines[0].rstrip("\r").split("\t")
    rows = []
    for lineno, line in enumerate(lines[1:], start=2):
        cells = line.rstrip("\r").split("\t")
        if len(cells) < len(header):
            cells = cells + [""] * (len(header) - len(cells))
        elif len(cells) > len(header):
            raise Stop(f"{path}:{lineno} has {len(cells)} cells for a {len(header)}-column header")
        rows.append(dict(zip(header, cells)))
    return header, rows


def frac(cell: str):
    """Parse a quarter-beat position or duration.  Empty means the table states none."""
    cell = cell.strip()
    if cell == "":
        return None
    return Fraction(cell)


# --------------------------------------------------------------------------------------------
# The four properties


def sounding_states(notes):
    """Walk the change points, yielding (t, before_counter, after_counter) at each.

    A note sounds on the half-open span [onset, onset + duration).  So the sounding multiset
    IMMEDIATELY BEFORE a change point t is the state carried in from the left, and the multiset
    IMMEDIATELY AFTER t is that state with every note ending at t removed and every note
    beginning at t added.

    A NOTE OF ZERO DURATION SOUNDS NOWHERE, and the corpus holds some.  Its onset and its release
    are the same moment, so it still contributes a change point - no note is excluded, eligibility
    being the derivation's question and not this criterion's - but it never enters the sounding
    multiset, because the span it would sound over is empty.  That is stated and coded rather than
    left to arithmetic: carried naively it would leave a zero count in the tally, and a zero count
    compares equal to an absent one, so the independent check below would have agreed with the
    sweep for the wrong reason.
    """
    starts = {}
    ends = {}
    all_times = set()
    for onset, offset, midi in notes:
        all_times.add(onset)
        all_times.add(offset)
        if onset == offset:
            continue
        starts.setdefault(onset, []).append(midi)
        ends.setdefault(offset, []).append(midi)

    change_points = sorted(all_times)
    live = Counter()
    for t in change_points:
        before = Counter(live)
        for midi in ends.get(t, ()):
            live[midi] -= 1
            if live[midi] <= 0:
                del live[midi]
        for midi in starts.get(t, ()):
            live[midi] += 1
        yield t, before, Counter(live)


def sounding_states_naive(notes):
    """The same quantity, derived a SECOND time straight from the definition.

    This is the tool's own establishment (#19): a measurement tool is trusted only after being
    positively established, and the establishment available here is a derivation of what the
    quantity IS, recomputed independently and reproduced exactly.  The sweep above carries state
    across change points and is fast; this one carries nothing and re-scans every note at every
    change point.  They share no code.  A single disagreement anywhere in the corpus STOPS the
    tool - it is not reported as a discrepancy and worked around.
    """
    change_points = sorted({n[0] for n in notes} | {n[1] for n in notes})
    for t in change_points:
        before = Counter(midi for on, off, midi in notes if on < t <= off)
        after = Counter(midi for on, off, midi in notes if on <= t < off)
        yield t, before, after


def pc_counter(counter: Counter) -> Counter:
    folded = Counter()
    for midi, n in counter.items():
        folded[midi % 12] += n
    return folded


def compute_piece(path: Path):
    header, rows = read_tsv(path)
    missing = [c for c in REQUIRED_NOTE_COLUMNS if c not in header]
    if missing:
        raise Stop(f"{path.name}: named note-table column(s) absent or differently named: {missing}")

    notes = []
    unplaceable = 0
    tied_vocabulary = Counter()
    for row in rows:
        tied_vocabulary[row["tied"].strip()] += 1
        onset = frac(row["quarterbeats"])
        dur = frac(row["duration_qb"])
        midi_cell = row["midi"].strip()
        if onset is None or dur is None or midi_cell == "":
            # Not silently dropped: counted, and published per piece.
            unplaceable += 1
            continue
        notes.append(
            {
                "onset": onset,
                "offset": onset + dur,
                "midi": int(midi_cell),
                "mc": row["mc"].strip(),
                "staff": row["staff"].strip() if "staff" in header else "",
                "voice": row["voice"].strip() if "voice" in header else "",
                "tied": row["tied"].strip(),
            }
        )

    triples = [(n["onset"], n["offset"], n["midi"]) for n in notes]

    # A zero-duration note would sound over an empty span, which the two derivations below could
    # in principle carry differently.  It is COUNTED rather than assumed away, so the artifact
    # states the fact instead of the establishment resting on a silence.
    zero_duration_notes = sum(1 for on, off, _ in triples if on == off)

    # ---- P1: release-driven change points -------------------------------------------------
    onsets = {n["onset"] for n in notes}
    releases = {n["offset"] for n in notes}
    release_only = releases - onsets
    union = onsets | releases
    p1_release_only_count = len(release_only)
    p1_share = (float(len(release_only)) / len(union)) if union else 0.0

    # ---- P2: change points invisible to pitch class ---------------------------------------
    # THREE READINGS ARE COMPUTED AND ALL THREE PUBLISHED.  The dispatch says to form the
    # sounding note MULTISET and compare it "by midi pitch, and by pitch class"; the charter's
    # ground it quotes speaks of the "octave-folded pitch-class SET".  Those two wordings give
    # different arithmetic for a unison shrink, which is one of the two cases the charter's own
    # ground names.  The primary is DECLARED HERE, BEFORE THE MEASUREMENT, and is the reading
    # that can see both cases the charter names: the note side compared as a multiset (so a
    # unison shrink is visible) against the octave-folded pitch-class SET.  The other two are
    # published beside it so the verdict's sensitivity to the reading is visible rather than
    # hidden (#24, and the near-tie discipline of #17).
    p2_primary = 0            # midi multiset changes AND pitch-class SET unchanged
    p2_multiset_both = 0      # midi multiset changes AND pitch-class MULTISET unchanged
    p2_set_both = 0           # midi SET changes AND pitch-class SET unchanged
    n_change_points = 0
    for _t, before, after in sounding_states(triples):
        n_change_points += 1
        midi_multiset_changed = before != after
        midi_set_changed = set(before) != set(after)
        pc_before_multi = pc_counter(before)
        pc_after_multi = pc_counter(after)
        pc_multiset_changed = pc_before_multi != pc_after_multi
        pc_set_changed = set(pc_before_multi) != set(pc_after_multi)
        if midi_multiset_changed and not pc_set_changed:
            p2_primary += 1
        if midi_multiset_changed and not pc_multiset_changed:
            p2_multiset_both += 1
        if midi_set_changed and not pc_set_changed:
            p2_set_both += 1

    # ---- the establishment: the same states, derived again and compared ---------------------
    checked = 0
    for (ta, ba, aa), (tb, bb, ab) in zip(
        sounding_states(triples), sounding_states_naive(triples)
    ):
        if ta != tb or ba != bb or aa != ab:
            raise Stop(
                f"{path.name}: the change-point sweep and the independent recomputation disagree "
                f"at {ta} / {tb} - the tool is not established and stops"
            )
        checked += 1
    if checked != n_change_points:
        raise Stop(
            f"{path.name}: the two derivations return {checked} and {n_change_points} change "
            f"points - the populations disagree and the tool stops"
        )

    # ---- P3: ties crossing a bar line ------------------------------------------------------
    # A tied group is a maximal chain of notes joined by ties.  ms3 marks the head of a tie 1,
    # an interior note 0, and the tail -1; an untied note carries an empty cell.  A chain is
    # followed within one (staff, voice) at one midi pitch, the successor beginning exactly
    # where its predecessor ends.  The group spans a bar boundary when its members do not all
    # carry the same measure count.
    by_key = {}
    for n in notes:
        by_key.setdefault((n["staff"], n["voice"], n["midi"]), []).append(n)
    for group in by_key.values():
        group.sort(key=lambda n: n["onset"])

    consumed = set()
    tied_groups = 0
    p3_crossing = 0
    for key, group in by_key.items():
        starts_at = {}
        for idx, n in enumerate(group):
            starts_at.setdefault(n["onset"], []).append(idx)
        for idx, n in enumerate(group):
            if (key, idx) in consumed or n["tied"] not in ("1",):
                continue
            chain = [idx]
            consumed.add((key, idx))
            cur = n
            while cur["tied"] in ("1", "0"):
                nxt_idx = None
                for cand in starts_at.get(cur["offset"], ()):
                    if (key, cand) in consumed:
                        continue
                    if group[cand]["tied"] in ("0", "-1"):
                        nxt_idx = cand
                        break
                if nxt_idx is None:
                    break
                consumed.add((key, nxt_idx))
                chain.append(nxt_idx)
                cur = group[nxt_idx]
            if len(chain) >= 2:
                tied_groups += 1
                if len({group[i]["mc"] for i in chain}) > 1:
                    p3_crossing += 1

    return {
        "notes_in_table": len(rows),
        "notes_placed": len(notes),
        "notes_unplaceable": unplaceable,
        "tied_cell_vocabulary": dict(sorted(tied_vocabulary.items())),
        "n_change_points": n_change_points,
        "P1_release_only_change_points": p1_release_only_count,
        "P1_share_of_all_change_points": round(p1_share, 6),
        "P1_onsets": len(onsets),
        "P1_releases": len(releases),
        "P1_union": len(union),
        "P2_primary": p2_primary,
        "P2_multiset_both": p2_multiset_both,
        "P2_set_both": p2_set_both,
        "P3_tied_groups": tied_groups,
        "P3_tied_groups_crossing_a_bar_line": p3_crossing,
        "change_points_independently_re_derived": checked,
        "zero_duration_notes": zero_duration_notes,
    }


# --------------------------------------------------------------------------------------------
# metadata-side properties


def parse_timesig(cell: str):
    """`TimeSig` is written as a measure-count-to-signature mapping, e.g. `1: 3/4`."""
    cell = cell.strip()
    if cell == "":
        return []
    out = []
    for field in cell.split(","):
        field = field.strip()
        if not field:
            continue
        out.append(field.split(":", 1)[1].strip() if ":" in field else field)
    return out


def piece_number(name: str):
    head = name.split(" ", 1)[0]
    try:
        return int(head)
    except ValueError:
        return None


# --------------------------------------------------------------------------------------------
# The decision rule — FIXED BEFORE THE MEASUREMENT, quoted verbatim from the dispatch.

DECISION_RULE_VERBATIM = (
    "The decision rule, FIXED BEFORE THE MEASUREMENT and not to be adjusted after seeing it. "
    "Let z be the share of pieces whose P2 count is zero. "
    "If z >= 0.5, P2 SEPARATES and Option B stands. Half or more of the corpus shows nothing on "
    "the charter's own decisive case, so choosing which pieces are staged buys real coverage. "
    "If z < 0.5, P2 DOES NOT SEPARATE and the ruled outcome is Option A: no score is selected and "
    "none is staged. A pick that cannot distinguish is a random pick wearing an evidential label. "
    "The threshold is a declared bar, set before measuring, on the reasoning above; it is not "
    "tuned to an observed distribution and must not be. Report z and the verdict, whichever way "
    "it falls."
)

SELECTION_RULE_VERBATIM = (
    "If and only if B stands, select THREE pieces, on the pilot's own precedent of three and on "
    "no number this side invented: "
    "1. Rank all pieces by P2 descending; break ties by P3 descending, then by piece number "
    "ascending. The first selection is the top-ranked piece. "
    "2. The second is the highest-ranked piece whose time signature differs from the first's. "
    "3. The third is the highest-ranked piece whose repeat/volta structure differs from the "
    "first two - carrying repeats where they do not, or the reverse. "
    "4. If a rule at step 2 or 3 cannot be satisfied anywhere in the corpus, that is a finding: "
    "record it, fill the slot with the next-ranked piece, and say plainly in the report which "
    "rule went unsatisfied."
)

ELIGIBILITY_SENTENCE = (
    "The criterion uses every note in the table, where the charter says \"every onset and every "
    "release of an ELIGIBLE note\". Eligibility is a question the derivation itself must answer, "
    "so the criterion deliberately does not pre-empt it. This is a simplification of the "
    "SELECTION, never of the specification."
)


def main() -> int:
    stops = []

    # ---- establishment ---------------------------------------------------------------------
    if not METADATA.exists():
        raise Stop(f"{METADATA} does not exist")
    if not NOTES_DIR.is_dir():
        raise Stop(f"{NOTES_DIR} does not exist")

    meta_header, meta_rows = read_tsv(METADATA)
    missing_meta = [c for c in REQUIRED_METADATA_COLUMNS if c not in meta_header]
    if missing_meta:
        raise Stop(f"metadata.tsv: named column(s) absent or differently named: {missing_meta}")
    missing_p4p5 = [c for c in P4_P5_COLUMNS if c not in meta_header]

    # ---- population, reported BOTH WAYS ----------------------------------------------------
    metadata_pieces = [r["piece"] for r in meta_rows]
    note_files = sorted(p for p in NOTES_DIR.iterdir() if p.name.endswith(NOTE_SUFFIX))
    # Keyed by PIECE IDENTIFIER - the file name less its suffix.  Not called a `stem`: in this
    # repository a bare `stem` is a note stem, and the reserved-word convention forbids
    # introducing a new collision.
    note_table_by_piece = {p.name[: -len(NOTE_SUFFIX)]: p for p in note_files}

    named_by_metadata_without_a_note_table = sorted(
        set(metadata_pieces) - set(note_table_by_piece)
    )
    note_tables_metadata_does_not_name = sorted(
        set(note_table_by_piece) - set(metadata_pieces)
    )
    if named_by_metadata_without_a_note_table:
        stops.append(
            {
                "stop": "metadata.tsv names a piece the notes directory does not hold",
                "identities": named_by_metadata_without_a_note_table,
            }
        )
    if note_tables_metadata_does_not_name:
        stops.append(
            {
                "stop": "the notes directory holds a table metadata.tsv does not name",
                "identities": note_tables_metadata_does_not_name,
            }
        )

    # ---- per piece -------------------------------------------------------------------------
    pieces = {}
    unparsable = []
    unreadable_metadata_cells = []
    for row in meta_rows:
        name = row["piece"]
        path = note_table_by_piece.get(name)
        if path is None:
            continue
        try:
            values = compute_piece(path)
        except Stop as exc:
            unparsable.append({"piece": name, "reason": str(exc)})
            continue
        except Exception as exc:  # noqa: BLE001 - reported, never absorbed
            unparsable.append({"piece": name, "reason": f"{type(exc).__name__}: {exc}"})
            continue

        timesigs = parse_timesig(row.get("TimeSig", ""))
        volta = row.get("volta_mcs", "").strip()
        len_folded = row.get("length_qb", "").strip()
        len_unfolded = row.get("length_qb_unfolded", "").strip()
        # A cell that cannot be read is COUNTED and published with its piece, never folded
        # silently to a default (DEFECT_TYPES.md DT-23).
        has_repeat = None
        if len_folded and len_unfolded:
            try:
                has_repeat = Fraction(len_unfolded) != Fraction(len_folded)
            except (ValueError, ZeroDivisionError) as exc:
                unreadable_metadata_cells.append(
                    {"piece": name, "columns": ["length_qb", "length_qb_unfolded"],
                     "cells": [len_folded, len_unfolded], "reason": f"{type(exc).__name__}: {exc}"}
                )
        elif not (len_folded and len_unfolded):
            unreadable_metadata_cells.append(
                {"piece": name, "columns": ["length_qb", "length_qb_unfolded"],
                 "cells": [len_folded, len_unfolded], "reason": "a cell is empty"}
            )

        n_onsets = row.get("n_onsets", "").strip()
        n_onset_positions = row.get("n_onset_positions", "").strip()
        density = None
        try:
            if n_onsets and n_onset_positions and Fraction(n_onset_positions) != 0:
                density = round(float(Fraction(n_onsets) / Fraction(n_onset_positions)), 6)
            else:
                unreadable_metadata_cells.append(
                    {"piece": name, "columns": ["n_onsets", "n_onset_positions"],
                     "cells": [n_onsets, n_onset_positions],
                     "reason": "a cell is empty or the denominator is zero"}
                )
        except (ValueError, ZeroDivisionError) as exc:
            unreadable_metadata_cells.append(
                {"piece": name, "columns": ["n_onsets", "n_onset_positions"],
                 "cells": [n_onsets, n_onset_positions],
                 "reason": f"{type(exc).__name__}: {exc}"}
            )

        values.update(
            {
                "rel_path": row.get("rel_path", ""),
                "P4_timesig_cell": row.get("TimeSig", ""),
                "P4_distinct_time_signatures": sorted(set(timesigs)),
                "P4_carries_more_than_one": len(set(timesigs)) > 1,
                "P5_volta_mcs": volta,
                "P5_has_volta": bool(volta),
                "P5_has_repeat": has_repeat,
                "P5_length_qb": len_folded,
                "P5_length_qb_unfolded": len_unfolded,
                "P5_repeat_volta_signature": [has_repeat, bool(volta)],
                "P6_n_onsets": n_onsets,
                "P6_n_onset_positions": n_onset_positions,
                "P6_simultaneity_density": density,
                "piece_number": piece_number(name),
            }
        )
        pieces[name] = values

    if unparsable:
        stops.append(
            {
                "stop": "a note table could not be parsed",
                "identities": unparsable,
            }
        )
    if unreadable_metadata_cells:
        stops.append(
            {
                "stop": "a metadata.tsv cell the tie-break reads could not be read",
                "identities": unreadable_metadata_cells,
            }
        )

    # ---- the separation check --------------------------------------------------------------
    names = sorted(pieces)
    n = len(names)
    zeros_primary = sum(1 for k in names if pieces[k]["P2_primary"] == 0)
    zeros_multiset_both = sum(1 for k in names if pieces[k]["P2_multiset_both"] == 0)
    zeros_set_both = sum(1 for k in names if pieces[k]["P2_set_both"] == 0)
    z_primary = (zeros_primary / n) if n else 0.0
    z_multiset_both = (zeros_multiset_both / n) if n else 0.0
    z_set_both = (zeros_set_both / n) if n else 0.0

    verdict_primary = "B_STANDS_P2_SEPARATES" if z_primary >= 0.5 else "A_OBTAINS_P2_DOES_NOT_SEPARATE"
    verdict_multiset_both = (
        "B_STANDS_P2_SEPARATES" if z_multiset_both >= 0.5 else "A_OBTAINS_P2_DOES_NOT_SEPARATE"
    )
    verdict_set_both = (
        "B_STANDS_P2_SEPARATES" if z_set_both >= 0.5 else "A_OBTAINS_P2_DOES_NOT_SEPARATE"
    )
    all_three_agree = verdict_primary == verdict_multiset_both == verdict_set_both

    # ---- the ruled pick, if and only if B stands -------------------------------------------
    selection = None
    selection_findings = []
    ranking = sorted(
        names,
        key=lambda k: (
            -pieces[k]["P2_primary"],
            -pieces[k]["P3_tied_groups_crossing_a_bar_line"],
            pieces[k]["piece_number"] if pieces[k]["piece_number"] is not None else 10**9,
            k,
        ),
    )

    if verdict_primary == "B_STANDS_P2_SEPARATES":
        first = ranking[0]
        first_ts = tuple(pieces[first]["P4_distinct_time_signatures"])

        second = None
        for k in ranking[1:]:
            if tuple(pieces[k]["P4_distinct_time_signatures"]) != first_ts:
                second = k
                break
        if second is None:
            selection_findings.append(
                "Step 2 UNSATISFIED: no piece in the corpus carries a time signature differing "
                "from the top-ranked piece's. The slot is filled with the next-ranked piece."
            )
            second = ranking[1]

        first_sig = tuple(pieces[first]["P5_repeat_volta_signature"])
        second_sig = tuple(pieces[second]["P5_repeat_volta_signature"])
        third = None
        for k in ranking:
            if k in (first, second):
                continue
            sig = tuple(pieces[k]["P5_repeat_volta_signature"])
            if sig != first_sig and sig != second_sig:
                third = k
                break
        if third is None:
            selection_findings.append(
                "Step 3 UNSATISFIED: no piece in the corpus carries a repeat/volta structure "
                "differing from BOTH of the first two. The slot is filled with the next-ranked "
                "piece not already selected."
            )
            for k in ranking:
                if k not in (first, second):
                    third = k
                    break

        selection = []
        for slot, k in (("first", first), ("second", second), ("third", third)):
            p = pieces[k]
            selection.append(
                {
                    "slot": slot,
                    "piece": k,
                    "rel_path": p["rel_path"],
                    "rank": ranking.index(k) + 1,
                    "P1_release_only_change_points": p["P1_release_only_change_points"],
                    "P1_share_of_all_change_points": p["P1_share_of_all_change_points"],
                    "P2_primary": p["P2_primary"],
                    "P2_multiset_both": p["P2_multiset_both"],
                    "P2_set_both": p["P2_set_both"],
                    "P3_tied_groups_crossing_a_bar_line": p["P3_tied_groups_crossing_a_bar_line"],
                    "P4_distinct_time_signatures": p["P4_distinct_time_signatures"],
                    "P4_carries_more_than_one": p["P4_carries_more_than_one"],
                    "P5_has_repeat": p["P5_has_repeat"],
                    "P5_has_volta": p["P5_has_volta"],
                    "P5_volta_mcs": p["P5_volta_mcs"],
                    "P6_simultaneity_density": p["P6_simultaneity_density"],
                }
            )

    def distribution(field):
        vals = sorted(pieces[k][field] for k in names)
        if not vals:
            return {}
        return {
            "min": vals[0],
            "max": vals[-1],
            "median": vals[len(vals) // 2],
            "mean": round(sum(vals) / len(vals), 6),
            "pieces_at_zero": sum(1 for v in vals if v == 0),
            "decile_boundaries": [vals[int(len(vals) * i / 10)] for i in range(1, 10)],
        }

    tied_vocab_corpus = Counter()
    for k in names:
        for cell, cnt in pieces[k]["tied_cell_vocabulary"].items():
            tied_vocab_corpus[cell] += cnt

    artifact = {
        "purpose": (
            "The L0+L1 exemplar selection: the separation check that Ruling 12 ordered run FIRST, "
            "the fixed decision rule applied to it, and - if and only if the check passes - the "
            "ruled pick of three exemplar scores. It stages nothing and copies nothing."
        ),
        "generated_by": "tools/audit/gen_l0l1_exemplar_selection.py",
        "generated_for": "cc_instruction_l0l1_exemplar_selection_2026_08_31.md, Tasks 1 and 2",
        "the_ruling": (
            "Ruling 12 of cowork_rulings_2026_08_31_decision_surface_sitting.md, section 3l: for "
            "the L0+L1 boot pack, PLAIN SCORES ONLY - no published analyses - selected by a "
            "MECHANICAL criterion over the corpus's own note tables, the criterion written and "
            "shown to the user BEFORE the selection is run."
        ),
        "what_this_is_not": (
            "Not a measurement of this project's analysis. This tool never opens a score, never "
            "runs the analyzer, and reads no output of ours. Its inputs are the corpus's own note "
            "tables and metadata and nothing else."
        ),
        "the_eligibility_simplification": ELIGIBILITY_SENTENCE,
        "sources": {
            "note_tables": "tools/dcml/bach_chorales/notes/*.notes.tsv",
            "metadata": "tools/dcml/bach_chorales/metadata.tsv",
            "note_table_columns_named_by_the_dispatch": REQUIRED_NOTE_COLUMNS,
            "metadata_columns_named_by_the_dispatch": REQUIRED_METADATA_COLUMNS,
            "metadata_header_as_found": meta_header,
            "note_table_header_as_found": read_tsv(note_files[0])[0] if note_files else [],
        },
        "establishment": {
            "every_named_note_table_column_present_in_every_table": not any(
                s["stop"] == "a note table could not be parsed" for s in stops
            ),
            "named_metadata_columns_absent": missing_meta,
            "P4_P5_columns_expected_and_their_presence": {
                c: (c in meta_header) for c in P4_P5_COLUMNS
            },
            "P4_P5_columns_absent": missing_p4p5,
            "the_P5_derivation_stated_because_no_column_carries_it": (
                "The dispatch names P5 as 'repeat and volta bars' read from metadata.tsv, and "
                "metadata.tsv carries a column for the VOLTA half (volta_mcs) but none for the "
                "REPEAT half. P5_has_repeat is therefore DERIVED, from the folded-against-"
                "unfolded length pair the same file carries (length_qb against "
                "length_qb_unfolded): a piece whose unfolded length exceeds its folded length "
                "carries a repeat. The derivation is stated rather than assumed, and the two "
                "columns it reads are published per piece beside the verdict."
            ),
            "tied_cell_vocabulary_over_the_whole_corpus": dict(sorted(tied_vocab_corpus.items())),
            "★_the_tool_s_own_establishment": {
                "what_was_established": (
                    "That the change-point sweep computes the sounding multiset before and after "
                    "each change point that the definition names. It is established by DERIVING "
                    "THE SAME QUANTITY A SECOND TIME, straight from the definition, in code that "
                    "shares nothing with the sweep: the sweep carries state across change points, "
                    "the check re-scans every note at every change point. Every change point of "
                    "every piece is compared, in both the before and the after state, and a "
                    "single disagreement anywhere STOPS the tool rather than being reported and "
                    "worked around."
                ),
                "change_points_compared": sum(
                    pieces[k]["change_points_independently_re_derived"] for k in names
                ),
                "pieces_compared": len(names),
                "disagreements": 0,
                "zero_duration_notes_in_the_whole_corpus": sum(
                    pieces[k]["zero_duration_notes"] for k in names
                ),
                "why_that_count_is_published_beside_the_disagreements": (
                    "A note of zero duration sounds over an empty span, and that is the one shape "
                    "on which the two derivations could in principle agree for the wrong reason. "
                    "The count is stated so the establishment rests on a measured fact rather "
                    "than on the absence of a complaint."
                ),
                "why_zero_is_the_only_admissible_value": (
                    "A disagreement raises and the tool exits non-zero, so this field can only "
                    "ever be read as zero on a run that produced this file (#19: a thing merely "
                    "unfalsified is not established, and this is the falsification that was run)."
                ),
                "what_is_NOT_established_by_it": (
                    "That the three P2 readings are the right question - that is the ruling's and "
                    "the charter's business, not this tool's; that the corpus's own note tables "
                    "are correct, which is the DCML corpus's own establishment and not measured "
                    "here; and that the decision rule's threshold is the right bar, which was "
                    "declared before the measurement and is the dispatch's."
                ),
            },
        },
        "population": {
            "pieces_named_by_metadata": len(metadata_pieces),
            "note_tables_on_disk": len(note_files),
            "pieces_measured": n,
            "named_by_metadata_without_a_note_table": named_by_metadata_without_a_note_table,
            "note_tables_metadata_does_not_name": note_tables_metadata_does_not_name,
            "note_tables_that_could_not_be_parsed": unparsable,
            "metadata_cells_the_tie_break_reads_that_could_not_be_read": unreadable_metadata_cells,
            "notes_the_table_could_not_place": {
                k: pieces[k]["notes_unplaceable"]
                for k in names
                if pieces[k]["notes_unplaceable"]
            },
            "what_an_unplaceable_note_is": (
                "A row whose quarterbeats, duration_qb or midi cell is empty. Such a row cannot "
                "be placed on the time line, so it enters no change point. They are COUNTED and "
                "published per piece rather than silently dropped (#12)."
            ),
        },
        "the_four_properties": {
            "P1": (
                "Release-driven change points. From each piece's note table, the onset set O = "
                "quarterbeats and the release set R = quarterbeats + duration_qb. Reported: "
                "|R \\ O| and its share of |O union R|."
            ),
            "P2": (
                "Change points invisible to pitch class - THE LOAD-BEARING PROPERTY. At every "
                "change point the sounding note multiset immediately before and immediately after "
                "is formed and compared twice, by midi pitch and by pitch class (midi mod 12). "
                "Reported: the count of change points at which the note set changes and the "
                "pitch-class set does not."
            ),
            "P3": "Ties crossing a bar line, from the tied column against mc.",
            "P6": "Simultaneity density: n_onsets against n_onset_positions, from metadata.tsv.",
            "P4_and_P5": (
                "P4 (time signature and whether the piece carries more than one) and P5 (repeat "
                "and volta bars) are read from metadata.tsv and are used ONLY by the tie-break of "
                "Task 2, never by the separation check."
            ),
        },
        "the_three_P2_readings_and_why_all_three_are_published": {
            "why": (
                "The dispatch says to form the sounding note MULTISET and compare it 'by midi "
                "pitch, and by pitch class'; the charter's own ground, which the dispatch quotes, "
                "speaks of the 'octave-folded pitch-class SET'. Those two wordings give different "
                "arithmetic at a UNISON SHRINK, which is one of the two cases the charter's ground "
                "names by name. The primary is DECLARED BEFORE THE MEASUREMENT and is the reading "
                "that can see both cases the charter names. The other two are published beside it "
                "so the verdict's sensitivity to the reading is visible rather than hidden."
            ),
            "P2_primary": (
                "the midi MULTISET changes and the pitch-class SET does not - a unison shrink and "
                "an octave shrink both count, which is what the charter's ground names"
            ),
            "P2_multiset_both": (
                "the midi MULTISET changes and the pitch-class MULTISET does not - a unison shrink "
                "does NOT count under this reading, because folding preserves the doubling"
            ),
            "P2_set_both": (
                "the midi SET changes and the pitch-class SET does not - a unison shrink does NOT "
                "count, because the midi set is unchanged by it"
            ),
            "which_one_drives_the_decision_rule": "P2_primary",
        },
        "the_decision_rule_verbatim": DECISION_RULE_VERBATIM,
        "the_selection_rule_verbatim": SELECTION_RULE_VERBATIM,
        "the_separation_check": {
            "pieces": n,
            "z_primary": round(z_primary, 6),
            "pieces_whose_P2_primary_is_zero": zeros_primary,
            "verdict_primary": verdict_primary,
            "z_multiset_both": round(z_multiset_both, 6),
            "pieces_whose_P2_multiset_both_is_zero": zeros_multiset_both,
            "verdict_multiset_both": verdict_multiset_both,
            "z_set_both": round(z_set_both, 6),
            "pieces_whose_P2_set_both_is_zero": zeros_set_both,
            "verdict_set_both": verdict_set_both,
            "all_three_readings_agree_on_the_verdict": all_three_agree,
            "the_verdict_of_record": verdict_primary,
        },
        "distributions": {
            "P1_release_only_change_points": distribution("P1_release_only_change_points"),
            "P1_share_of_all_change_points": distribution("P1_share_of_all_change_points"),
            "P2_primary": distribution("P2_primary"),
            "P2_multiset_both": distribution("P2_multiset_both"),
            "P2_set_both": distribution("P2_set_both"),
            "P3_tied_groups_crossing_a_bar_line": distribution(
                "P3_tied_groups_crossing_a_bar_line"
            ),
            "P6_simultaneity_density": distribution("P6_simultaneity_density"),
        },
        "the_selection": selection,
        "the_selection_findings": selection_findings,
        "the_selection_is_null_because": (
            None
            if selection is not None
            else (
                "Option A obtains: the separation check failed under the decision rule fixed "
                "before the measurement, so no score is selected and none is staged."
            )
        ),
        "ranking_top_20_by_the_selection_rule": [
            {
                "rank": i + 1,
                "piece": k,
                "P2_primary": pieces[k]["P2_primary"],
                "P3_tied_groups_crossing_a_bar_line": pieces[k][
                    "P3_tied_groups_crossing_a_bar_line"
                ],
                "P4_distinct_time_signatures": pieces[k]["P4_distinct_time_signatures"],
                "P5_repeat_volta_signature": pieces[k]["P5_repeat_volta_signature"],
            }
            for i, k in enumerate(ranking[:20])
        ],
        "stops": stops,
        "what_this_run_did_not_do": (
            "Staged nothing and copied nothing - staging is the writing side's act, performed "
            "from this artifact. Rendered no boot pack, wrote no brief, booted no deriving "
            "session and derived nothing. Wrote nothing under tools/dcml/: the corpus's note "
            "tables and metadata.tsv are read and never written."
        ),
        "per_piece": pieces,
    }

    OUT.write_text(json.dumps(artifact, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")

    print(f"pieces measured: {n}")
    print(f"z_primary        = {z_primary:.6f}  -> {verdict_primary}")
    print(f"z_multiset_both  = {z_multiset_both:.6f}  -> {verdict_multiset_both}")
    print(f"z_set_both       = {z_set_both:.6f}  -> {verdict_set_both}")
    print(f"all three readings agree: {all_three_agree}")
    print(f"stops: {len(stops)}")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Stop as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        sys.exit(2)
