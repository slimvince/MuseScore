#!/usr/bin/env python3
"""gen_note_events.py — the note-event extraction (the note-side table fit, part 2 of 2; §1).

READ-ONLY / FIT-LAYER-OWNED. No src/ change, no corpus mutation, no gate change, no metric/decoder
consulted (the DT-2 firewall — grep-provable: only music21 read-only + the corpus xml + the OI-142
WiR substrate + the committed Default .ours.json for the establishment reconciliation). This is the
substrate for the emission (§3), spelling (§4) and event-boundary (§5) tables. Dispatch:
`cc_instruction_note_table_fit.md` (Cowork 2026-07-19).

WHAT IT PRODUCES — one compact committed artifact `note_events/note_events.json` (chosen layout: ONE
file, all 326 WiR-covered stems; per-stem note list + event lattice), provenance-stamped. The fitter
`gen_note_tables.py` reads this cache (no second music21 parse).

REUSE (#6): music21 9.9.1 (the established corpus toolchain — `music21_batch.py` uses the same
`TICKS_PER_QUARTER=480`, `round(offset*TPQ)` tick convention and reads the same corpus xml). This
module writes NO second note reader; it is the only note-event extractor in tools/joint_estimator/.
The fold coverage list is `fold_assignment.json` (OI-176). music21 native `.measureNumber`
(0 = anacrusis, MATCHING the WiR m0 convention — verified in the dispatch probe) and `.beat`
(1-indexed) supply metric position and the anacrusis marker with no ours-anchor dependency.

PER NOTE (§1): onset tick, duration tick, pitch-class, midi, notated spelling as a line-of-fifths
position (step+alter), part index (voice), measure number, beat, metric class, melodic approach and
departure (step<=2 semitones / leap / none, per same-voice temporal adjacency), tied-from-previous
flag, and (addendum, algorithm-completion step 1) a FERMATA flag (a music21 expressions.Fermata on
the note/chord). THE EVENT LATTICE (§1): the minimal segments between consecutive note onsets/offsets
(the Pardo & Birmingham partition) with >=1 sounding note; each event carries its start/end tick,
measure, beat, metric class, and whether ANY sounding note carries a fermata.

FERMATA ADDENDUM (algorithm-completion step 1, Cowork dispatch 2026-07-19): the fermata mark is the
ratified boundary/cadence-location factor's evidence (factorization §3.8; the chorale phrase-end
convention, de Clercq EMR 2015). It is APPENDED to the note/event records (note element 12, event
element 5), so every previously-existing field is byte-identical to the pre-addendum extraction
(proven field-wise in main()). No existing field, order, or count changes.

ESTABLISHMENT (#19): (i) byte-reproducible; (ii) a spot reconciliation on 3 pieces (incl. bwv145.5):
the extracted pcs sounding across a NAMED pitch-class-constant region equal the committed .ours.json
region `pitchClassSet` (the analyzer's own region set is finer than a raw span union on
non-pc-constant regions — its Layer-2 segmentation — so the reconciliation is on pc-constant regions,
where the two readers of the score must agree exactly; a mismatch there is a STOP).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_ROOT / "tools" / "joint_estimator"))

from music21 import converter, expressions         # noqa: E402  (the established corpus toolchain)
import gen_label_tables as glt                      # noqa: E402  (reuse the ONE _beat_class — #6)

# The single metric-class definition (part 1's; part 1 is frozen, so we import rather than copy — #6).
_beat_class = glt._beat_class

TICKS_PER_QUARTER = 480                             # the corpus tick convention (music21_batch.py)

WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")
CORPUS_XML_DIR = _ROOT / "tools" / "corpus"        # bwv*.xml music21 exports (the read-only score inputs)
DEFAULT_OURS_DIR = _ROOT / "tools" / "corpus" / "default"   # committed .ours.json (establishment only)
FOLD_ARTIFACT = _ROOT / "tools" / "joint_estimator" / "fold_assignment.json"
OUT_DIR = _ROOT / "tools" / "joint_estimator" / "note_events"
OUT_JSON = OUT_DIR / "note_events.json"
OUT_SUMMARY = OUT_DIR / "note_events_summary.txt"

EXTRACTION_VERSION = ("note-events-v1+fermata (part2 §1; music21 recurse, offset*480, line-of-fifths "
                      "spelling; +fermata flag APPENDED to note[12]/event[5], existing fields invariant)")

# line-of-fifths position of a natural step (F=-1 .. B=5); a sharp is +7, a flat -7.
_STEP_LOF = {"F": -1, "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5}

# metric-class codes (part-1 _beat_class categories); approach/departure codes.
_MC = {"downbeat": 0, "mid_strong": 1, "other_tactus": 2, "sub_tactus": 3}
_MC_INV = {v: k for k, v in _MC.items()}
_MV = {"none": 0, "step": 1, "leap": 2}
_MV_INV = {v: k for k, v in _MV.items()}


def _git_head() -> str:
    out = subprocess.run(["git", "-C", str(_ROOT), "rev-parse", "HEAD"],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def _rel(p) -> str:
    return Path(p).resolve().relative_to(_ROOT).as_posix()


def _line_of_fifths(step: str, alter: float) -> int:
    return _STEP_LOF[step] + 7 * int(round(alter))


def _measure_map(part):
    """{measure_number: start_tick} from a part's Measure elements (music21 native offsets)."""
    mm = {}
    for m in part.getElementsByClass("Measure"):
        mm[m.number] = round(float(m.offset) * TICKS_PER_QUARTER)
    return mm


def _time_signature(score):
    """(beats, beat_type, n_quarter, multi) from the score's time signatures. n_quarter = quarter-beats
    per measure (4/4->4, 3/4->3, 6/8->3 by 4*beats/beat_type). multi = more than one distinct meter."""
    tss = list(score.recurse().getElementsByClass("TimeSignature"))
    if not tss:
        return None, None, None, False
    distinct = sorted({(t.numerator, t.denominator) for t in tss})
    beats, bt = tss[0].numerator, tss[0].denominator
    n_quarter = beats * 4 // bt
    return beats, bt, n_quarter, len(distinct) > 1


def extract_stem(stem: str) -> dict | None:
    """Extract notes + the event lattice for one covered stem. Returns None if the xml is missing."""
    xml = CORPUS_XML_DIR / f"{stem}.xml"
    if not xml.exists():
        return None
    score = converter.parse(str(xml))
    beats, bt, n_quarter, multi_meter = _time_signature(score)

    # ── per-part note extraction (global tick via getOffsetInHierarchy; native measure/beat) ──
    # per-part list of dicts, so melodic approach/departure is computed within each voice.
    parts_notes: list[list[dict]] = []
    beat_fallbacks = 0                              # DT-23: count, never silently swallow
    for pi, part in enumerate(score.parts):
        mm = _measure_map(part)
        pnotes = []
        for n in part.recurse().notes:
            onset = round(float(n.getOffsetInHierarchy(score)) * TICKS_PER_QUARTER)
            dur = round(float(n.duration.quarterLength) * TICKS_PER_QUARTER)
            if dur <= 0:
                continue
            meas = n.measureNumber
            try:
                beatpos = float(n.beat)
            except Exception:
                beatpos = 1.0
                beat_fallbacks += 1
            tied = bool(n.tie and n.tie.type in ("stop", "continue"))
            # fermata: a music21 expressions.Fermata attached to the note/chord (shared by all its
            # pitches). The chorale phrase-end convention (factorization §3.8; de Clercq EMR 2015).
            ferm = any(isinstance(e, expressions.Fermata) for e in n.expressions)
            for p in (n.pitches if n.isChord else [n.pitch]):
                pnotes.append({
                    "onset": onset, "dur": dur, "pc": p.pitchClass, "midi": p.midi,
                    "lof": _line_of_fifths(p.step, p.alter or 0.0),
                    "part": pi, "measure": meas, "beat": round(beatpos, 4), "tied": tied,
                    "fermata": ferm,
                })
        parts_notes.append(pnotes)

    # ── melodic approach / departure per voice (temporal adjacency within the same part) ──
    for pnotes in parts_notes:
        pnotes.sort(key=lambda d: (d["onset"], d["midi"]))
        for i, nd in enumerate(pnotes):
            nd["approach"] = _melodic(pnotes, i, direction=-1)
            nd["departure"] = _melodic(pnotes, i, direction=+1)

    notes = [nd for pnotes in parts_notes for nd in pnotes]
    notes.sort(key=lambda d: (d["onset"], d["part"], d["midi"]))

    # ── the event lattice: minimal segments between consecutive onsets/offsets, >=1 sounding note ──
    m1_map = _measure_map(score.parts[0]) if score.parts else {}
    bounds = sorted({nd["onset"] for nd in notes} | {nd["onset"] + nd["dur"] for nd in notes})
    events = []
    for a, b in zip(bounds, bounds[1:]):
        sounding = [nd for nd in notes if nd["onset"] <= a and nd["onset"] + nd["dur"] >= b]
        if not sounding:
            continue                                  # a silent gap is not a harmonic event
        meas, beatpos = _tick_to_measure_beat(a, m1_map, n_quarter)
        ev_ferm = any(nd["fermata"] for nd in sounding)   # any sounding note carries a fermata
        events.append({"start": a, "end": b, "measure": meas, "beat": round(beatpos, 4),
                       "fermata": ev_ferm})

    # ── metric class per note (from native beat) and per event (from measure-derived beat) ──
    for nd in notes:
        nd["mc"] = _beat_class(nd["beat"], n_quarter) if n_quarter else "sub_tactus"
    for ev in events:
        ev["mc"] = _beat_class(ev["beat"], n_quarter) if n_quarter else "sub_tactus"

    return {
        "stem": stem,
        "meter": [beats, bt] if beats is not None else None,
        "n_quarter": n_quarter, "multi_meter": multi_meter,
        "beat_fallbacks": beat_fallbacks,
        "notes": [_pack_note(nd) for nd in notes],
        "events": [_pack_event(ev) for ev in events],
    }


def _melodic(pnotes: list[dict], i: int, direction: int) -> str:
    """Step (<=2 semitones) / leap (>2) / none, against the temporally-adjacent same-voice note.
    prev/next = the nearest DISTINCT onset in the part (min |Δmidi| among a same-onset group);
    'none' unless that note is temporally contiguous (no rest gap) with this one."""
    cur = pnotes[i]
    if direction < 0:
        cand = [nd for nd in pnotes if nd["onset"] < cur["onset"]]
        if not cand:
            return "none"
        o = max(nd["onset"] for nd in cand)
        grp = [nd for nd in cand if nd["onset"] == o]
        other = min(grp, key=lambda nd: abs(nd["midi"] - cur["midi"]))
        contiguous = (other["onset"] + other["dur"] == cur["onset"])
    else:
        cand = [nd for nd in pnotes if nd["onset"] > cur["onset"]]
        if not cand:
            return "none"
        o = min(nd["onset"] for nd in cand)
        grp = [nd for nd in cand if nd["onset"] == o]
        other = min(grp, key=lambda nd: abs(nd["midi"] - cur["midi"]))
        contiguous = (cur["onset"] + cur["dur"] == other["onset"])
    if not contiguous:
        return "none"
    return "step" if abs(other["midi"] - cur["midi"]) <= 2 else "leap"


def _tick_to_measure_beat(tick: int, m1_map: dict, n_quarter: int):
    """Measure number + quarter-beat position of a tick, from the first part's measure offsets."""
    if not m1_map:
        return None, 1.0
    starts = sorted(m1_map.items(), key=lambda kv: kv[1])
    meas, mstart = starts[0][0], starts[0][1]
    for mn, st in starts:
        if st <= tick:
            meas, mstart = mn, st
        else:
            break
    pos = (tick - mstart) / TICKS_PER_QUARTER + 1.0
    return meas, pos


# compact packing: notes and events as arrays; codes documented in the artifact header. The fermata
# flag is APPENDED (note[12] / event[5]) so elements 0..11 (notes) / 0..4 (events) are byte-identical
# to the pre-addendum extraction — the invariance obligation, proven field-wise in main().
def _pack_note(nd: dict) -> list:
    return [nd["onset"], nd["dur"], nd["pc"], nd["midi"], nd["lof"], nd["part"], nd["measure"],
            nd["beat"], _MC[nd["mc"]], _MV[nd["approach"]], _MV[nd["departure"]], int(nd["tied"]),
            int(nd["fermata"])]


def _pack_event(ev: dict) -> list:
    return [ev["start"], ev["end"], ev["measure"], ev["beat"], _MC[ev["mc"]], int(ev["fermata"])]


NOTE_FIELDS = ["onset", "dur", "pc", "midi", "lof", "part", "measure", "beat",
               "metric_class_code", "approach_code", "departure_code", "tied", "fermata"]
EVENT_FIELDS = ["start", "end", "measure", "beat", "metric_class_code", "fermata"]
# the count of pre-addendum fields (the invariance obligation compares exactly these leading elements).
NOTE_PREEXISTING = 12
EVENT_PREEXISTING = 5


# ══════════════════════════════════════════════════════════════════════════
# Establishment (#19) — pc reconciliation on pc-constant regions
# ══════════════════════════════════════════════════════════════════════════

def _mask(pcs) -> int:
    m = 0
    for p in pcs:
        m |= (1 << p)
    return m


def reconcile_stem(stem: str, packed: dict) -> dict:
    """For every committed Default .ours.json region of `stem`, if the sounding pc-set is CONSTANT
    across [startTick,endTick), assert the extracted union == the region's pitchClassSet. Returns
    counts + one cited clean region."""
    ours = json.loads((DEFAULT_OURS_DIR / f"{stem}.ours.json").read_text(encoding="utf-8"))
    notes = [(n[0], n[1], n[2]) for n in packed["notes"]]   # (onset, dur, pc)
    bounds = sorted({o for o, d, pc in notes} | {o + d for o, d, pc in notes})

    def sounding(t):
        return frozenset(pc for o, d, pc in notes if o <= t < o + d)

    const_tot = const_match = 0
    cited = None
    mismatch = None
    for r in ours.get("regions", []):
        st, en = r["startTick"], r["endTick"]
        inside = [t for t in bounds if st <= t < en]
        base = sounding(st)
        if base and all(sounding(t) == base for t in inside):
            const_tot += 1
            want = frozenset(i for i in range(12) if r["pitchClassSet"] & (1 << i))
            if base == want:
                const_match += 1
                if cited is None:
                    cited = {"startTick": st, "endTick": en, "pcs": sorted(want)}
            elif mismatch is None:
                mismatch = {"startTick": st, "endTick": en,
                            "extracted": sorted(base), "ours": sorted(want)}
    return {"pc_constant_regions": const_tot, "matched": const_match,
            "cited_clean_region": cited, "mismatch": mismatch}


# ══════════════════════════════════════════════════════════════════════════
# Fermata addendum (algorithm-completion step 1) — invariance check + census
# ══════════════════════════════════════════════════════════════════════════

def check_field_invariance(prev: dict | None, pieces: dict) -> dict:
    """The invariance obligation (dispatch Task 1): every PRE-ADDENDUM field is byte-identical after
    regeneration. Compares, against the prior on-disk artifact, each note's leading NOTE_PREEXISTING
    elements and each event's leading EVENT_PREEXISTING elements, plus the per-piece scalars and the
    note/event counts — MECHANICALLY (element-wise), not by eyeball. Returns {ok, checked, first_diff}.
    If prev is None (no prior artifact) the check is vacuously ok=None (nothing to compare against)."""
    if prev is None:
        return {"ok": None, "reason": "no prior note_events.json on disk to compare against"}
    prev_pieces = prev.get("pieces", {})
    scalars = ("stem", "meter", "n_quarter", "multi_meter", "beat_fallbacks")
    checked = {"pieces": 0, "notes": 0, "events": 0}
    for stem, rec in pieces.items():
        pp = prev_pieces.get(stem)
        if pp is None:
            return {"ok": False, "first_diff": {"stem": stem, "why": "stem absent from prior artifact"}}
        for k in scalars:
            if pp.get(k) != rec.get(k):
                return {"ok": False, "first_diff": {"stem": stem, "scalar": k,
                                                    "prev": pp.get(k), "new": rec.get(k)}}
        if len(pp["notes"]) != len(rec["notes"]) or len(pp["events"]) != len(rec["events"]):
            return {"ok": False, "first_diff": {"stem": stem, "why": "note/event count changed",
                                                "prev": [len(pp["notes"]), len(pp["events"])],
                                                "new": [len(rec["notes"]), len(rec["events"])]}}
        for i, (a, b) in enumerate(zip(pp["notes"], rec["notes"])):
            if a[:NOTE_PREEXISTING] != b[:NOTE_PREEXISTING]:
                return {"ok": False, "first_diff": {"stem": stem, "note_index": i,
                                                    "prev": a[:NOTE_PREEXISTING], "new": b[:NOTE_PREEXISTING]}}
        for i, (a, b) in enumerate(zip(pp["events"], rec["events"])):
            if a[:EVENT_PREEXISTING] != b[:EVENT_PREEXISTING]:
                return {"ok": False, "first_diff": {"stem": stem, "event_index": i,
                                                    "prev": a[:EVENT_PREEXISTING], "new": b[:EVENT_PREEXISTING]}}
        checked["pieces"] += 1
        checked["notes"] += len(rec["notes"])
        checked["events"] += len(rec["events"])
    return {"ok": True, "checked": checked,
            "note_preexisting_fields": NOTE_PREEXISTING, "event_preexisting_fields": EVENT_PREEXISTING}


def fermata_census(pieces: dict) -> dict:
    """Per-piece fermata census: note-fermata count, event-fermata count, and the list of pieces with
    ZERO fermatas (worth listing — a chorale should carry fermatas at nearly every phrase end)."""
    per_piece = {}
    zero_fermata = []
    tot_note_ferm = tot_event_ferm = 0
    for stem, rec in sorted(pieces.items()):
        nf = sum(1 for n in rec["notes"] if n[12])          # note fermata flag (element 12)
        ef = sum(1 for ev in rec["events"] if ev[5])         # event fermata flag (element 5)
        per_piece[stem] = {"notes_with_fermata": nf, "events_with_fermata": ef}
        tot_note_ferm += nf
        tot_event_ferm += ef
        if nf == 0:
            zero_fermata.append(stem)
    with_ferm = [s for s in pieces if per_piece[s]["notes_with_fermata"] > 0]
    return {
        "pieces_total": len(pieces),
        "pieces_with_fermata": len(with_ferm),
        "pieces_zero_fermata": zero_fermata,          # the full list (dispatch: "worth listing")
        "pieces_zero_fermata_count": len(zero_fermata),
        "total_notes_with_fermata": tot_note_ferm,
        "total_events_with_fermata": tot_event_ferm,
        "per_piece": per_piece,
    }


# ══════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prev = json.loads(OUT_JSON.read_text(encoding="utf-8")) if OUT_JSON.exists() else None
    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"].keys())

    pieces = {}
    total_notes = total_events = 0
    parse_fail = []
    for stem in covered:
        try:
            rec = extract_stem(stem)
        except Exception as e:                          # a parse failure is surfaced, never hidden (#12)
            parse_fail.append((stem, f"{type(e).__name__}: {e}"))
            continue
        if rec is None:
            parse_fail.append((stem, "xml missing"))
            continue
        pieces[stem] = rec
        total_notes += len(rec["notes"])
        total_events += len(rec["events"])

    if parse_fail:
        raise SystemExit(f"STOP: {len(parse_fail)} stems failed extraction: {parse_fail[:5]}")
    total_beat_fallbacks = sum(p["beat_fallbacks"] for p in pieces.values())

    # establishment (#19-ii): pc reconciliation on 3 named pieces incl. bwv145.5
    recon = {}
    for stem in ("bwv145.5", "bwv352", "bwv254"):
        recon[stem] = reconcile_stem(stem, pieces[stem])
        r = recon[stem]
        if r["matched"] != r["pc_constant_regions"] or r["mismatch"] is not None:
            raise SystemExit(f"STOP: pc reconciliation FAILED on {stem}: {r}")

    # fermata addendum (step 1): the field-invariance obligation + the fermata census
    invariance = check_field_invariance(prev, pieces)
    if invariance["ok"] is False:
        raise SystemExit("STOP (Task 1 invariance): a pre-addendum field changed after regeneration: "
                         + json.dumps(invariance["first_diff"]))
    census = fermata_census(pieces)

    provenance = {
        "generator": _rel(Path(__file__)),
        "corpus_git_hash": _git_head(),
        "extraction_version": EXTRACTION_VERSION,
        "ticks_per_quarter": TICKS_PER_QUARTER,
        "corpus_xml_dir": _rel(CORPUS_XML_DIR),
        "wir_dir": _rel(WIR_DIR),
        "covered_stems": len(covered),
        "beat_fallbacks_total": total_beat_fallbacks,   # DT-23: music21 .beat fallbacks (expect 0)
        "note_fields": NOTE_FIELDS,
        "event_fields": EVENT_FIELDS,
        "metric_class_codes": _MC,
        "melodic_codes": _MV,
        "note_field_notes": (
            "onset/dur/end in ticks (480/quarter); pc=midi%12; lof=line-of-fifths (step+alter, F=-1..B=5, "
            "sharp +7 flat -7); part=voice index; measure (0=anacrusis, music21 native = WiR m0); "
            "beat=1-indexed quarter-beat; approach/departure vs the temporally-adjacent same-voice note "
            "(step<=2 semitones / leap>2 / none if a rest gap or voice edge); tied=1 if tied from previous; "
            "fermata=1 if a music21 expressions.Fermata is on the note/chord (APPENDED element 12)."),
        "event_notes": (
            "minimal segments between consecutive note onsets/offsets with >=1 sounding note (the "
            "Pardo & Birmingham partition); [start,end,measure,beat,metric_class_code,fermata]; "
            "fermata=1 if ANY sounding note carries a fermata (APPENDED element 5)."),
        "fermata_addendum": {
            "field_invariance": invariance,       # element-wise proof: every pre-addendum field unchanged
            "invariance_baseline": ("the on-disk note_events.json read before this regeneration (the "
                                    "committed pre-addendum artifact on the first run)"),
            "census": census,
        },
        "establishment": {
            "byte_reproducible": "run twice; note_events.json byte-identical",
            "pc_reconciliation": recon,
            "pc_reconciliation_note": (
                "extracted sounding-pc union == committed Default .ours.json pitchClassSet on every "
                "pitch-class-constant region of the 3 cited pieces; non-pc-constant regions differ only "
                "by the analyzer's own Layer-2 region granularity, not by note extraction."),
        },
    }
    out = {"provenance": provenance, "pieces": pieces}
    OUT_JSON.write_text(json.dumps(out, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "=== note-event extraction (part 2 §1 + fermata addendum) — summary ===",
        f"corpus git_hash: {provenance['corpus_git_hash']}",
        f"covered stems extracted: {len(pieces)}  (parse failures: {len(parse_fail)})",
        f"total notes: {total_notes}   total events: {total_events}",
        "",
        "-- fermata addendum (algorithm-completion step 1) --",
        (f"  field invariance vs pre-addendum artifact: {invariance['ok']}"
         + (f"  (checked {invariance['checked']['notes']} notes[:12] + "
            f"{invariance['checked']['events']} events[:5] over {invariance['checked']['pieces']} pieces)"
            if invariance['ok'] else f"  ({invariance.get('reason', invariance.get('first_diff'))})")),
        f"  pieces with fermata: {census['pieces_with_fermata']}/{census['pieces_total']}",
        f"  pieces with ZERO fermata ({census['pieces_zero_fermata_count']}): "
        f"{census['pieces_zero_fermata'] if census['pieces_zero_fermata'] else 'none'}",
        f"  total notes with fermata: {census['total_notes_with_fermata']}   "
        f"total events with fermata: {census['total_events_with_fermata']}",
        "",
        "-- establishment: pc reconciliation on pc-constant regions --",
    ]
    for stem, r in recon.items():
        lines.append(f"  {stem}: {r['matched']}/{r['pc_constant_regions']} pc-constant regions match "
                     f"(cited clean region {r['cited_clean_region']})")
    OUT_SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print(f"\nwrote {_rel(OUT_JSON)} ({OUT_JSON.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
