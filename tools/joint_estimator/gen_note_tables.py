#!/usr/bin/env python3
"""gen_note_tables.py — the note-side table fit (part 2 of 2; §3 emission, §4 spelling, §5 event
boundary). Dispatch: `cc_instruction_note_table_fit.md` (Cowork 2026-07-19).

READ-ONLY / FIT-LAYER-OWNED. No src/ change, no corpus mutation, no gate change, NO DECODING, NO
EVALUATION, no accuracy metric consulted (the DT-2 firewall — grep-provable: no import of
a8_rebaseline_measure / compare_analyses grading / compare_rn scoring / robust_stop_diff / any
decoder; the only compare_analyses use is `_dcml_time_spans`, the pure measure-anchor GT->tick
resolver, imported untouched; the only compare_rn use is `_dcml_key_tonic`, the shared key-string
reduction; music21 `roman` is the oracle for the template ESTABLISHMENT only, never a decode).

Produces fitted TABLES as committed artifacts (per training fold + all-326); nothing is graded. All
reported figures come from the generated inventory (#17f/DT-11), never hand-typed.

REUSE (#6):
  - gen_note_events.note_events.json            : the part-2 §1 note+event substrate (one reader)
  - gen_label_tables.katz_distribution / estimate_conditional / THRESHOLD / ALPHA / N_FOLDS /
    OI184_FLAGGED / _git_head / _rel                                     : the part-1 fit machinery
  - dcml_parser.load_wir_regions (OI-142 substrate), compare_rn._dcml_key_tonic (the one key
    reduction), normalize.normalize_label (the OI-186a class), compare_analyses._dcml_time_spans
    (the established GT (measure,beat)->tick resolver — imported untouched)
  - music21.roman                              : the template-mapping oracle (establishment #19 only)

THE TEMPLATE MAPPING (fit-layer logic, dispatch §3) is documented in `member_pcs` below and
established against music21 (99.94% of 18,418 GT tokens; residual enumerated). Any class the mapping
cannot resolve -> a counted `template_unmapped` bucket, never guessed.

OI-184 / meter exclusions (dispatch §2), BINDING on all three tick-anchored tables:
  - the 7 flagged local-misalignment pieces and the 2 multi-meter pieces (bwv304, bwv362) are
    EXCLUDED ENTIRELY;
  - for anacrusis pieces the WiR m0 segment is dropped and counting starts at m1 b1 (music21 numbers
    the pickup measure 0, matching WiR — notes/events with measure 0 are skipped).
"""
from __future__ import annotations

import bisect
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.path.insert(0, str(_ROOT / "tools" / "joint_estimator"))

import dcml_parser as dcml                 # noqa: E402
import compare_rn as crn                   # noqa: E402
import compare_analyses as ca              # noqa: E402  (only _dcml_time_spans — the GT tick resolver)
import normalize as norm                   # noqa: E402
import gen_label_tables as glt             # noqa: E402  (the part-1 fit machinery — reused)
from music21 import roman, key as m21key   # noqa: E402  (template oracle — establishment only)

WIR_DIR = str(_ROOT / "tools" / "dcml" / "when_in_rome")
DEFAULT_OURS_DIR = _ROOT / "tools" / "corpus" / "default"
NOTE_EVENTS = _ROOT / "tools" / "joint_estimator" / "note_events" / "note_events.json"
FOLD_ARTIFACT = _ROOT / "tools" / "joint_estimator" / "fold_assignment.json"
PART1_INVENTORY = _ROOT / "tools" / "joint_estimator" / "table_fit_inventory.json"

OUT_DIR = _ROOT / "tools" / "joint_estimator"
FIT_VERSION = "note-tables-v1 (part2 §3/§4/§5)"

THRESHOLD = glt.THRESHOLD
ALPHA = glt.ALPHA
N_FOLDS = glt.N_FOLDS
FLAGGED = set(glt.OI184_FLAGGED)
MULTIMETER = {"bwv304", "bwv362"}
COUNTED_METERS = {(4, 4), (3, 4)}

_MC_INV = {0: "downbeat", 1: "mid_strong", 2: "other_tactus", 3: "sub_tactus"}
_MV_INV = {0: "none", 1: "step", 2: "leap"}

# ══════════════════════════════════════════════════════════════════════════
# The template mapping (fit-layer logic; dispatch §3) — established vs music21 below
# ══════════════════════════════════════════════════════════════════════════
_DEG = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7}
_MAJ_SCALE = [0, 2, 4, 5, 7, 9, 11]        # major scale-degree semitones from tonic
_MIN_SCALE = [0, 2, 3, 5, 7, 8, 10]        # natural-minor scale-degree semitones
_DIMQ = {"Dim", "Dim7", "HalfDim7", "HalfDim"}
# quality -> chord-member intervals from the root
_QUAL_TEMPLATE = {
    "Maj": (0, 4, 7), "Min": (0, 3, 7), "Dim": (0, 3, 6), "Aug": (0, 4, 8),
    "Dom7": (0, 4, 7, 10), "Maj7": (0, 4, 7, 11), "Min7": (0, 3, 7, 10),
    "MinMaj7": (0, 3, 7, 11), "Dim7": (0, 3, 6, 9), "HalfDim7": (0, 3, 6, 10),
    "HalfDim": (0, 3, 6), "Aug7": (0, 4, 8, 10), "AugMaj7": (0, 4, 8, 11),
}
# the LOCAL key's collection (relative to tonic): major scale; minor = the ratified composite
# (natural minor + raised 6th (+9) and raised 7th (+11)) — dispatch §3.
_MAJ_COLLECTION = frozenset(_MAJ_SCALE)
_MIN_COLLECTION = frozenset(set(_MIN_SCALE) | {9, 11})

# line-of-fifths of a natural step; a sharp is +7, a flat -7 (same basis as gen_note_events).
_STEP_LOF = {"F": -1, "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5}


def _split_degree(base: str):
    acc = 0
    for ch in base:
        if ch == "b":
            acc -= 1
        elif ch == "#":
            acc += 1
        else:
            break
    num = _DEG.get(base.lstrip("b#"))
    return num, acc


def _chord_root(base: str, quality: str, tonic: int, is_major: bool):
    """Root pc of a degree in a key. Honors the accidental prefix and the standard minor-mode raised
    root of a secondary/leading-tone diminished chord: in minor, a diatonic (no explicit accidental)
    diminished/half-diminished chord on degree 7 is the LEADING-TONE chord (root +11, not the +10
    subtonic) and on degree 6 the RAISED-submediant chord (root +9, not the +8 submediant). These two
    rules are what the DCML/rntxt convention encodes; validated against music21 below."""
    num, acc = _split_degree(base)
    if num is None:
        return None
    semi = (_MAJ_SCALE if is_major else _MIN_SCALE)[num - 1] + acc
    if (not is_major) and acc == 0 and quality in _DIMQ:
        if num == 7:
            semi = 11
        elif num == 6:
            semi = 9
    return (tonic + semi) % 12


def _framework_and_root(cls: "norm.LabelClass", tonic: int, is_major: bool):
    """Shared framework/root derivation for member_pcs and chord_factor_pcs (#6 — ONE path). Returns
    (fw_tonic, fw_major, root_pc): fw_* are the tonicized framework a class is read in (its target's
    key for applied classes, else the local key); root_pc is the chord root pc for a standard
    triad/seventh quality, or None for a chromatic class (AugSixth/Neapolitan — special member
    content, no standard root/third/fifth roles). Returns None entirely for an unmappable class
    (raw_unnormalized, multi-level applied, bad target degree, or a quality with no template)."""
    if cls.raw_unnormalized:
        return None
    q = cls.quality
    fw_tonic, fw_major = tonic, is_major
    if cls.target:
        if "/" in cls.target:                       # multi-level applied — unmappable, counted
            return None
        tbase = cls.target.lstrip("b#")
        tnum = _DEG.get(tbase.upper())
        if tnum is None:
            return None
        tacc = sum(1 if c == "#" else -1 for c in cls.target if c in "#b")
        fw_tonic = (tonic + (_MAJ_SCALE if is_major else _MIN_SCALE)[tnum - 1] + tacc) % 12
        fw_major = tbase[:1].isupper()
    if q in ("AugSixth", "Neapolitan"):             # chromatic — special content, no standard root
        return (fw_tonic, fw_major, None)
    if q not in _QUAL_TEMPLATE:
        return None
    root = _chord_root(cls.degree_base, q, fw_tonic, fw_major)
    if root is None:
        return None
    return (fw_tonic, fw_major, root)


def member_pcs(cls: "norm.LabelClass", tonic: int, is_major: bool):
    """The realized chord-member pc set of a normalized class in a (tonic, mode) key, or None if the
    class is unmappable (multi-level applied, or raw_unnormalized). Root = tonic + degree interval
    (accidentals honored); applied classes anchor to the TARGET's tonicized key (framework mode = the
    target's own case: uppercase major, lowercase minor); members from the quality template. The
    augmented-sixth and Neapolitan chromatic classes carry their textbook pc content. Dispatch §3."""
    fr = _framework_and_root(cls, tonic, is_major)
    if fr is None:
        return None
    fw_tonic, fw_major, root = fr
    q = cls.quality
    if q == "AugSixth":                             # It6 = flat-6, tonic, sharp-4 of the (target) key
        return frozenset((fw_tonic + i) % 12 for i in (8, 0, 6))
    if q == "Neapolitan":                           # flat-II major triad
        return frozenset((fw_tonic + i) % 12 for i in (1, 5, 8))
    pcs = set((root + i) % 12 for i in _QUAL_TEMPLATE[q])
    if cls.inversion.startswith("9"):               # a ninth carries the ninth as a member
        pcs.add((root + (1 if "b9" in cls.inversion else 2)) % 12)
    return frozenset(pcs)


def chord_factor_pcs(cls: "norm.LabelClass", tonic: int, is_major: bool):
    """The ordered (role, pc) chord factors of a STANDARD triad/seventh class in a (tonic, mode) key,
    or None when the class has no standard root/third/fifth roles (chromatic AugSixth/Neapolitan,
    multi-level applied, raw_unnormalized, unmapped quality). Roles in template order: root, third,
    fifth, and — seventh chords only — seventh. Ninth extensions are NOT factors here. Reuses the same
    framework/root derivation as member_pcs (#6). The chord-factor presence table
    (cowork_sensitive_cell_probe.md finding 3, option 3a) is built from this."""
    fr = _framework_and_root(cls, tonic, is_major)
    if fr is None:
        return None
    _fw_tonic, _fw_major, root = fr
    if root is None:                                # chromatic class — no standard factor roles
        return None
    tmpl = _QUAL_TEMPLATE[cls.quality]
    roles = ("root", "third", "fifth", "seventh")
    return [(roles[i], (root + tmpl[i]) % 12) for i in range(len(tmpl))]


def note_category(pc: int, mem: frozenset, tonic: int, is_major: bool) -> str:
    if pc in mem:
        return "member"
    coll = _MAJ_COLLECTION if is_major else _MIN_COLLECTION
    return "within" if (pc - tonic) % 12 in coll else "outside"


def tonic_lof(local_key: str) -> int:
    """Line-of-fifths of a key's tonic from its spelled name. Key strings are LETTER-FIRST with
    trailing accidentals (e.g. 'b' = B minor, 'Bb', 'f#'), so the letter is position 0."""
    letter = local_key[0].upper()
    accs = local_key[1:]
    return _STEP_LOF[letter] + 7 * (accs.count("#") - accs.count("b"))


def spelling_bin(rel: int, is_major: bool) -> str:
    """Bin a note's line-of-fifths position RELATIVE to the local tonic (rel = note_lof - tonic_lof)
    into the seven diatonic degrees, raised 6th / raised 7th (minor), and pooled flatward / sharpward
    chromatic bins. Dispatch §4."""
    if is_major:
        if -1 <= rel <= 5:
            return f"dia:{rel}"                      # 4th(-1) 1st(0) 5th(1) 2nd(2) 6th(3) 3rd(4) 7th(5)
        return "chr_flat" if rel < -1 else "chr_sharp"
    # minor
    if -4 <= rel <= 2:
        return f"dia:{rel}"                          # b6(-4) b3(-3) b7(-2) 4th(-1) 1st(0) 5th(1) 2nd(2)
    if rel == 3:
        return "raised6"
    if rel == 5:
        return "raised7"
    return "chr_flat" if rel < -4 else "chr_sharp"


_SPELL_CLASS = {"raised6": "raised", "raised7": "raised", "chr_flat": "chromatic", "chr_sharp": "chromatic"}


def _spelling_parent(cell: str):
    if cell == "BASE":
        return None
    if cell.startswith("CLASS:"):
        return "BASE"
    if cell.startswith("dia:"):
        return "CLASS:diatonic"
    return f"CLASS:{_SPELL_CLASS.get(cell, 'chromatic')}"


# ══════════════════════════════════════════════════════════════════════════
# GT segments (the counting population; established GT->tick resolver)
# ══════════════════════════════════════════════════════════════════════════

def gt_segments(stem: str):
    """Kept GT segments for a stem: (start, end, local_key, raw_label, tonic, is_major, mem, cls).
    WiR (measure,beat) resolved to ticks via compare_analyses._dcml_time_spans (imported untouched),
    anchored to the committed Default .ours.json regions. The m0 (anacrusis) segments are dropped."""
    ours_path = DEFAULT_OURS_DIR / f"{stem}.ours.json"
    if not ours_path.exists():
        return []
    _, ours = ca.load_analysis(ours_path)
    dregs = dcml.load_wir_regions(WIR_DIR, stem)
    spans = ca._dcml_time_spans(ours, dregs)
    segs = []
    for (st, en), d in zip(spans, dregs):
        if st < 0 or en <= st or d.measure_number == 0:
            continue
        lk = getattr(d, "local_key", None)
        tonic, is_major = crn._dcml_key_tonic(lk)
        cls = norm.normalize_label(d.chord_symbol or "")
        mem = member_pcs(cls, tonic, is_major) if (tonic is not None and is_major is not None) else None
        segs.append({"start": st, "end": en, "local_key": lk, "raw": d.chord_symbol or "",
                     "tonic": tonic, "is_major": is_major, "mem": mem, "cls": cls})
    return segs


def _seg_for_tick(segs, starts, tick):
    """The kept GT segment whose [start,end) contains tick, or None."""
    i = bisect.bisect_right(starts, tick) - 1
    if 0 <= i < len(segs) and segs[i]["start"] <= tick < segs[i]["end"]:
        return segs[i]
    return None


# ══════════════════════════════════════════════════════════════════════════
# Per-stem counting (fold-independent; aggregated per stem set)
# ══════════════════════════════════════════════════════════════════════════

def per_stem_counts(stem: str, piece: dict):
    """All three tables' raw counts for one stem, plus diagnostics. Returns None + a reason for an
    excluded stem (flagged / multi-meter / meter not in {4/4,3/4})."""
    if stem in FLAGGED:
        return None, "flagged"
    if stem in MULTIMETER or piece["multi_meter"]:
        return None, "multi_meter"
    meter = tuple(piece["meter"]) if piece["meter"] else None
    if meter not in COUNTED_METERS:
        return None, "meter_not_counted"

    segs = gt_segments(stem)
    starts = [s["start"] for s in segs]

    emission = defaultdict(Counter)     # (mc,appr,dep,tied) -> Counter(category)
    spelling = {True: Counter(), False: Counter()}
    boundary = {c: [0, 0] for c in _MC_INV.values()}    # class -> [boundaries, events]
    boundary_robust = {c: [0, 0] for c in _MC_INV.values()}
    diag = Counter()

    # ── emission + spelling (per note whose onset falls in a kept GT segment) ──
    for n in piece["notes"]:
        onset, dur, pc, midi, lof, part, measure, beat, mc_c, ap_c, dp_c, tied = n
        if measure == 0:                            # OI-184 (a): pickup notes excluded
            continue
        seg = _seg_for_tick(segs, starts, onset)
        if seg is None:
            diag["note_unassigned"] += 1
            continue
        diag["notes_in_segment"] += 1
        if seg["tonic"] is None or seg["is_major"] is None:
            diag["note_indeterminate_key"] += 1
            continue
        if seg["mem"] is None:
            diag["template_unmapped"] += 1
            continue
        cat = note_category(pc, seg["mem"], seg["tonic"], seg["is_major"])
        combo = (_MC_INV[mc_c], _MV_INV[ap_c], _MV_INV[dp_c], bool(tied))
        emission[combo][cat] += 1
        diag["emission_notes"] += 1
        rel = lof - tonic_lof(seg["local_key"])
        spelling[seg["is_major"]][spelling_bin(rel, seg["is_major"])] += 1
        diag["spelling_notes"] += 1

    # ── event-level boundary (per event; boundary iff a GT label starts at its tick) ──
    gt_start_set = set(starts)
    # robust variant: the FIRST event (min start) of each kept GT segment is a boundary
    first_event_of_seg = {}
    for ev in piece["events"]:
        start, end, measure, beat, mc_c = ev
        if measure == 0:
            continue
        seg = _seg_for_tick(segs, starts, start)
        if seg is not None:
            fe = first_event_of_seg.get(seg["start"])
            if fe is None or start < fe:
                first_event_of_seg[seg["start"]] = start
    robust_boundary_ticks = set(first_event_of_seg.values())
    for ev in piece["events"]:
        start, end, measure, beat, mc_c = ev
        if measure == 0:
            continue
        cls = _MC_INV[mc_c]
        boundary[cls][1] += 1
        if start in gt_start_set:
            boundary[cls][0] += 1
        boundary_robust[cls][1] += 1
        if start in robust_boundary_ticks:
            boundary_robust[cls][0] += 1
    # GT starts that land on no event boundary (the sub-beat analyst-vs-note jitter; a measurement
    # caveat, not an inference item — related to OI-184).
    event_ticks = {ev[0] for ev in piece["events"] if ev[2] != 0}
    diag["gt_starts_kept"] += len(starts)
    diag["gt_starts_off_lattice"] += sum(1 for s in starts if s not in event_ticks)

    return {"emission": emission, "spelling": spelling, "boundary": boundary,
            "boundary_robust": boundary_robust, "diag": diag}, None


# ══════════════════════════════════════════════════════════════════════════
# Fitting a stem set into the three tables
# ══════════════════════════════════════════════════════════════════════════

def _emit_context_chain(combo):
    mc, ap, dp, tied = combo
    cs = int((ap == "step") or (dp == "step") or (mc == "sub_tactus") or bool(tied))
    return [f"L0:{mc}|{ap}|{dp}|{int(tied)}", f"L1:{ap}|{dp}", f"L2:{cs}", "BASE"]


def _emit_display(combo):
    return f"{combo[0]} | {combo[1]} | {combo[2]} | {int(combo[3])}"


def fit_tables(stem_counts: list):
    """Aggregate per-stem counts and fit the three tables. Returns (tables, meta)."""
    emission = defaultdict(Counter)
    spelling = {True: Counter(), False: Counter()}
    boundary = {c: [0, 0] for c in _MC_INV.values()}
    boundary_robust = {c: [0, 0] for c in _MC_INV.values()}
    diag = Counter()
    for sc in stem_counts:
        for combo, cc in sc["emission"].items():
            emission[combo].update(cc)
        for m in (True, False):
            spelling[m].update(sc["spelling"][m])
        for c in boundary:
            boundary[c][0] += sc["boundary"][c][0]
            boundary[c][1] += sc["boundary"][c][1]
            boundary_robust[c][0] += sc["boundary_robust"][c][0]
            boundary_robust[c][1] += sc["boundary_robust"][c][1]
        diag.update(sc["diag"])

    # ── emission: P(category | covariate combo) with covariate back-off (part-1 machinery) ──
    pair_counts = {(combo, cat): n for combo, cc in emission.items() for cat, n in cc.items()}
    emis_rows, emis_meta = glt.estimate_conditional(
        pair_counts, _emit_context_chain, lambda o: None, _emit_display)
    # marginal + covariate-support split (the headline aggregates; every covariate combo is
    # well-populated so the fitted rows sit at L0, hence these read from the raw counts).
    cat_totals = Counter()
    support_split = {0: Counter(), 1: Counter()}
    for combo, cc in emission.items():
        cs = int((combo[1] == "step") or (combo[2] == "step") or (combo[0] == "sub_tactus") or bool(combo[3]))
        for cat, n in cc.items():
            cat_totals[cat] += n
            support_split[cs][cat] += n
    emis_tot = sum(cat_totals.values()) or 1
    emission_marginal = {c: cat_totals[c] / emis_tot for c in ("member", "within", "outside")}
    emission_by_support = {}
    for cs in (0, 1):
        tt = sum(support_split[cs].values()) or 1
        emission_by_support[f"L2:{cs}"] = {c: support_split[cs][c] / tt for c in ("member", "within", "outside")}

    # ── spelling: P(bin | mode), per mode, outcome pooling to class then base ──
    spell = {}
    spell_meta = {}
    for m, name in ((True, "major"), (False, "minor")):
        dist, meta = glt.katz_distribution(dict(spelling[m]), _spelling_parent)
        spell[name] = {"dist": dist, "raw_counts": dict(spelling[m])}
        spell_meta[name] = meta

    # ── event boundary: Bernoulli per beat class ──
    t_bound = {}
    for c, (b, s) in boundary.items():
        t_bound[c] = {"boundary": b, "events": s, "prob": (b / s if s else None)}
    t_bound_robust = {}
    for c, (b, s) in boundary_robust.items():
        t_bound_robust[c] = {"boundary": b, "events": s, "prob": (b / s if s else None)}

    free_params = {
        "emission": emis_meta["free_params"],
        "spelling": spell_meta["major"]["free_params"] + spell_meta["minor"]["free_params"],
        "boundary": len([c for c in t_bound if t_bound[c]["events"]]),  # one Bernoulli per populated class
    }
    free_params["total"] = free_params["emission"] + free_params["spelling"] + free_params["boundary"]
    tokens = {
        "emission": int(diag["emission_notes"]),
        "spelling": int(diag["spelling_notes"]),
        "boundary": sum(v["events"] for v in t_bound.values()),
    }
    tokens["total"] = tokens["emission"] + tokens["spelling"] + tokens["boundary"]

    tables = {
        "emission_category_by_covariate": emis_rows,
        "spelling_position_by_mode": spell,
        "event_boundary_by_beat_class": t_bound,
        "event_boundary_by_beat_class_robust_firstevent": t_bound_robust,
    }
    meta = {"free_params": free_params, "tokens": tokens, "diagnostics": dict(diag),
            "emission_meta": emis_meta, "spelling_meta": spell_meta,
            "emission_marginal": emission_marginal, "emission_by_support": emission_by_support}
    return tables, meta


# ══════════════════════════════════════════════════════════════════════════
# Establishment: template mapping vs the music21 oracle (#19)
# ══════════════════════════════════════════════════════════════════════════

def validate_template(covered):
    """Compare member_pcs(normalize(label), key) to music21 RomanNumeral(label, key).pitches over all
    distinct (raw label, local key) GT combos, weighted by token count. Report agreement + residual."""
    combo_tokens = Counter()
    for stem in covered:
        for r in dcml.load_wir_regions(WIR_DIR, stem):
            combo_tokens[(r.chord_symbol or "", getattr(r, "local_key", None))] += 1
    tot = agree = unmap = skip = 0
    residual = []
    for (raw, lk), n in combo_tokens.items():
        tonic, is_major = crn._dcml_key_tonic(lk)
        if tonic is None or is_major is None:
            skip += n
            continue
        tot += n
        mine = member_pcs(norm.normalize_label(raw), tonic, is_major)
        if mine is None:
            unmap += n
            continue
        try:
            opcs = frozenset(p.pitchClass for p in roman.RomanNumeral(raw, m21key.Key(lk)).pitches)
        except Exception:
            skip += n
            continue
        if mine == opcs:
            agree += n
        else:
            residual.append({"label": raw, "key": lk, "tokens": n,
                             "mine": sorted(mine), "oracle": sorted(opcs)})
    residual.sort(key=lambda d: -d["tokens"])
    return {"tokens_checked": tot, "agree": agree, "agree_pct": round(100 * agree / tot, 3) if tot else None,
            "template_unmapped_tokens": unmap, "indeterminate_key_tokens": skip,
            "residual_disagreements": residual[:20], "residual_total_tokens": sum(r["tokens"] for r in residual)}


# ══════════════════════════════════════════════════════════════════════════
# Hand-checks (dispatch §6) and sanity anchors
# ══════════════════════════════════════════════════════════════════════════

def hand_checks(all_stem_counts_index, note_events):
    """The desk-sim sensitive-cell classification arithmetic (dispatch §6a/b/c), computed from the
    template mapping + the actual extracted notes."""
    checks = {}

    def notes_in_span(stem, lo, hi):
        return [n for n in note_events["pieces"][stem]["notes"] if lo <= n[0] < hi]

    # (a) bwv145.5 m10 b1-b2 under (E major, V6 then V6/5): D#/F#/B/A all chord members. Each note is
    # classified against ITS OWN onset's GT segment (the real fit logic) — b1 is V6 (triad D#/F#/B),
    # b2 is V6/5 (adds A as the seventh); every sounding pc is a member, no spurious NCT (the C1 finding).
    segs = gt_segments("bwv145.5")
    starts = [s["start"] for s in segs]
    a = {"segments_b1_b2": [{"start": s["start"], "raw": s["raw"], "member_pcs": sorted(s["mem"])}
                            for s in segs if 12960 <= s["start"] < 13920 and s["mem"]], "notes": []}
    for n in notes_in_span("bwv145.5", 12960, 13920):
        seg = _seg_for_tick(segs, starts, n[0])
        a["notes"].append({"onset": n[0], "pc": n[2], "seg_raw": seg["raw"],
                           "cat": note_category(n[2], seg["mem"], seg["tonic"], seg["is_major"])})
    a["all_chord_members"] = all(nd["cat"] == "member" for nd in a["notes"])
    checks["a_bwv145.5_Emajor_V"] = a

    # (b) bwv352 m1 b4 under (a minor, vi/o7): C/E/F#/A all members; and under (a minor, i): F#'s category
    segs = gt_segments("bwv352")
    seg = next((s for s in segs if s["start"] <= 1440 < s["end"]), None)
    mem_vio7 = member_pcs(norm.normalize_label("vi/o7"), 9, False)
    mem_i = member_pcs(norm.normalize_label("i"), 9, False)
    b = {"seg_local_key": seg["local_key"], "seg_raw": seg["raw"],
         "member_pcs(a minor, vio7)": sorted(mem_vio7), "member_pcs(a minor, i)": sorted(mem_i),
         "under_vio7": [], "under_i_Fsharp": None}
    for n in notes_in_span("bwv352", 1440, 1920):
        b["under_vio7"].append({"pc": n[2], "cat": note_category(n[2], mem_vio7, 9, False)})
        if n[2] == 6:   # F#
            b["under_i_Fsharp"] = {"pc": 6, "cat_under_i": note_category(6, mem_i, 9, False),
                                   "covariates": {"metric": _MC_INV[n[8]], "approach": _MV_INV[n[9]],
                                                  "departure": _MV_INV[n[10]], "tied": bool(n[11])},
                                   "rel_lof": n[4] - tonic_lof(seg["local_key"]),
                                   "spelling_bin": spelling_bin(n[4] - tonic_lof(seg["local_key"]), False)}
    checks["b_bwv352_sharetone"] = b

    # (c) one V-labeled minor segment showing the raised-7th chord-member classification
    for stem in sorted(note_events["pieces"]):
        if stem in FLAGGED or stem in MULTIMETER:
            continue
        segs = gt_segments(stem)
        for s in segs:
            if s["is_major"] is False and s["cls"].degree_base == "V" and s["mem"] is not None \
               and s["cls"].quality in ("Maj", "Dom7") and not s["cls"].target:
                # raised 7th of minor tonic = tonic + 11; it is the THIRD of V (a member)
                lt = (s["tonic"] + 11) % 12
                if lt in s["mem"]:
                    checks["c_minor_V_raised7"] = {
                        "stem": stem, "local_key": s["local_key"], "raw": s["raw"],
                        "tonic_pc": s["tonic"], "raised7_pc": lt,
                        "member_pcs": sorted(s["mem"]),
                        "raised7_is_member": lt in s["mem"],
                        "raised7_category": note_category(lt, s["mem"], s["tonic"], False)}
                    break
        if "c_minor_V_raised7" in checks:
            break
    return checks


def sanity_anchors(all_stem_counts_index, note_events, spelling_all):
    """Report (no tuning): in minor V-labeled segments, raised-7 note frequency vs flat-7; and the
    fitted minor spelling table's leading-tone (raised7) cell vs subtonic (dia:-2) cell. Dispatch §6."""
    raised7 = flat7 = 0
    for stem in sorted(note_events["pieces"]):
        if stem in FLAGGED or stem in MULTIMETER:
            continue
        segs = gt_segments(stem)
        starts = [s["start"] for s in segs]
        for n in note_events["pieces"][stem]["notes"]:
            if n[6] == 0:
                continue
            seg = _seg_for_tick(segs, starts, n[0])
            if seg is None or seg["is_major"] is not False or seg["cls"].degree_base != "V" \
               or seg["cls"].target:
                continue
            rel = n[4] - tonic_lof(seg["local_key"])
            if rel == 5:
                raised7 += 1
            elif rel == -2:
                flat7 += 1
    minor_dist = spelling_all["spelling_position_by_mode"]["minor"]["dist"]
    return {
        "minor_V_segments_raised7_note_count": raised7,
        "minor_V_segments_flat7_note_count": flat7,
        "raised7_much_greater_than_flat7": raised7 > flat7,
        "minor_spelling_P_raised7": minor_dist.get("raised7"),
        "minor_spelling_P_subtonic_dia_minus2": minor_dist.get("dia:-2"),
        "leading_tone_cell_greater_than_subtonic": (minor_dist.get("raised7", 0) or 0) > (minor_dist.get("dia:-2", 0) or 0),
    }


# ══════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════

def _write(path, obj):
    path.write_text(json.dumps(obj, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")


def main():
    fa = json.loads(FOLD_ARTIFACT.read_text(encoding="utf-8"))
    covered = sorted(fa["stem_index"].keys())
    fold_of = {s: fa["stem_index"][s]["fold"] for s in covered}
    note_events = json.loads(NOTE_EVENTS.read_text(encoding="utf-8"))

    # per-stem counts (fold-independent), + exclusion tally
    per_stem = {}
    excluded = defaultdict(list)
    for stem in covered:
        res, reason = per_stem_counts(stem, note_events["pieces"][stem])
        if res is None:
            excluded[reason].append(stem)
        else:
            per_stem[stem] = res
    counted_stems = sorted(per_stem)

    part1 = json.loads(PART1_INVENTORY.read_text(encoding="utf-8"))["capacity_bound_summary"]
    part1_grid_table6 = json.loads(
        (OUT_DIR / "tables_all.json").read_text(encoding="utf-8"))["table6_boundary_by_beat_class"]

    # anacrusis pieces among the counted set (a WiR m0 segment was dropped) — reported for §2.
    anacrusis_counted = sorted(
        s for s in counted_stems
        if any(d.measure_number == 0 for d in dcml.load_wir_regions(WIR_DIR, s)))

    def stem_set(name):
        if name == "all":
            return counted_stems
        f = int(name[4:])
        return [s for s in counted_stems if fold_of[s] != f]

    fits = {}
    for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]:
        stems = stem_set(name)
        tables, meta = fit_tables([per_stem[s] for s in stems])
        fits[name] = {"tables": tables, "meta": meta, "n_stems": len(stems)}

    # establishment + hand-checks + sanity (computed on all-326)
    template_valid = validate_template(covered)
    checks = hand_checks(per_stem, note_events)
    sanity = sanity_anchors(per_stem, note_events, fits["all"]["tables"])

    # combined capacity (part 1 + part 2), per fold
    capacity = {}
    for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]:
        p2 = fits[name]["meta"]
        p1 = part1[name]
        combined_params = p1["free_params"] + p2["free_params"]["total"]
        combined_tokens = p1["total_tokens"] + p2["tokens"]["total"]
        capacity[name] = {
            "part1_free_params": p1["free_params"], "part1_tokens": p1["total_tokens"],
            "part2_free_params": p2["free_params"], "part2_tokens": p2["tokens"],
            "combined_free_params": combined_params, "combined_tokens": combined_tokens,
            "combined_tokens_per_param": round(combined_tokens / combined_params, 2) if combined_params else None,
            "passes_combined_bound": combined_tokens >= 10 * combined_params,
            "part2_per_table_tokens_per_param": {
                t: (round(p2["tokens"][t] / p2["free_params"][t], 2) if p2["free_params"][t] else None)
                for t in ("emission", "spelling", "boundary")},
            "passes_part2_per_table_bound": all(
                (p2["free_params"][t] == 0) or (p2["tokens"][t] >= 10 * p2["free_params"][t])
                for t in ("emission", "spelling", "boundary")),
        }
        if not capacity[name]["passes_combined_bound"]:
            raise SystemExit(f"STOP: combined capacity bound FAILED for {name}: {capacity[name]}")

    # ── write the fitted-table artifacts (per fold + all) ──
    prov = {
        "generator": glt._rel(Path(__file__)), "corpus_git_hash": glt._git_head(),
        "fit_version": FIT_VERSION, "protocol": "cowork_prefit_gates.md (OI-176/OI-177), user-ratified 2026-07-19",
        "threshold": THRESHOLD, "alpha": ALPHA, "n_folds": N_FOLDS,
        "note_events_artifact": glt._rel(NOTE_EVENTS),
        "gt_tick_resolver": "compare_analyses._dcml_time_spans (measure-anchor, imported untouched)",
        "counted_stems": len(counted_stems), "excluded": {k: sorted(v) for k, v in excluded.items()},
        "anacrusis_convention": "WiR m0 segments dropped; music21 measure-0 (pickup) notes/events skipped",
    }
    for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]:
        suffix = "all" if name == "all" else name.replace("fold", "fold")
        obj = {"provenance": dict(prov, fit_scope=name, n_training_stems=fits[name]["n_stems"]),
               **fits[name]["tables"]}
        _write(OUT_DIR / f"note_tables_{suffix}.json", obj)

    # ── the inventory (capacity, establishment, hand-checks, sanity, headline cells) ──
    all_tabs = fits["all"]["tables"]
    inventory = {
        "purpose": "part-2 note-side fit: parameter inventory, combined capacity, establishment, hand-checks, sanity.",
        "provenance": prov,
        "counted_population": {
            "counted_stems": len(counted_stems),
            "anacrusis_pieces_m0_dropped": len(anacrusis_counted),
            "counted_tokens": {"emission_notes": fits["all"]["meta"]["tokens"]["emission"],
                               "spelling_notes": fits["all"]["meta"]["tokens"]["spelling"],
                               "boundary_events": fits["all"]["meta"]["tokens"]["boundary"]},
            "excluded_counts": {k: len(v) for k, v in excluded.items()},
            "excluded": {k: sorted(v) for k, v in excluded.items()},
            "all326_diagnostics": fits["all"]["meta"]["diagnostics"],
            "gt_start_alignment_caveat": {
                "gt_starts_kept": fits["all"]["meta"]["diagnostics"].get("gt_starts_kept", 0),
                "gt_starts_off_event_lattice": fits["all"]["meta"]["diagnostics"].get("gt_starts_off_lattice", 0),
                "note": ("a small fraction of GT label starts (resolved through the mandated measure-anchor "
                         "machinery) land between note onsets/offsets — sub-beat analyst-vs-note beat placement, "
                         "a MEASUREMENT-layer property (OI-184 domain), not an inference item. Emission/spelling "
                         "assign each note by onset-in-span (robust to this); the event boundary reports both the "
                         "exact-tick and the first-event-of-segment (robust) variants, which agree to <0.3%."),
            },
        },
        "capacity": capacity,
        "per_fit_free_params_and_tokens": {name: {"free_params": fits[name]["meta"]["free_params"],
                                                  "tokens": fits[name]["meta"]["tokens"],
                                                  "n_training_stems": fits[name]["n_stems"]}
                                           for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]},
        "template_mapping_establishment": template_valid,
        "emission_headline": {
            "base_category_distribution": fits["all"]["meta"]["emission_marginal"],
            "covariate_support_effect": fits["all"]["meta"]["emission_by_support"],
        },
        "spelling_headline": {
            "minor_leading_tone_vs_subtonic": {
                "P_raised7_leading_tone": all_tabs["spelling_position_by_mode"]["minor"]["dist"].get("raised7"),
                "P_subtonic_dia_minus2": all_tabs["spelling_position_by_mode"]["minor"]["dist"].get("dia:-2"),
            },
            "major_dist": all_tabs["spelling_position_by_mode"]["major"]["dist"],
            "minor_dist": all_tabs["spelling_position_by_mode"]["minor"]["dist"],
        },
        "event_boundary_vs_grid": {
            "part2_event_level": all_tabs["event_boundary_by_beat_class"],
            "part2_event_level_robust_firstevent": all_tabs["event_boundary_by_beat_class_robust_firstevent"],
            "part1_grid_level_SUPERSEDED_for_A": part1_grid_table6,
            "note": ("the part-1 grid variant (16th-note denominator) is reproduced here BESIDE the event-level "
                     "variant and marked superseded-for-A (dispatch §5); the part-1 file is NOT edited. The "
                     "event denominator raises sub_tactus P from the grid's silent-slot-diluted value to the "
                     "true per-event rate."),
        },
        "hand_checks_desk_sim": checks,
        "sanity_anchors": sanity,
        "template_unmapped_size": {"all326_notes": fits["all"]["meta"]["diagnostics"].get("template_unmapped", 0),
                                   "all326_tokens_in_labels": template_valid["template_unmapped_tokens"]},
    }
    _write(OUT_DIR / "note_table_fit_inventory.json", inventory)
    _write_summary(inventory, capacity, template_valid, sanity, all_tabs)
    print(f"wrote note_tables_*.json (6 fits), note_table_fit_inventory.json")
    print(f"counted stems: {len(counted_stems)}  excluded: {{"
          + ", ".join(f'{k}:{len(v)}' for k, v in excluded.items()) + "}")
    print(f"template oracle agreement: {template_valid['agree']}/{template_valid['tokens_checked']} "
          f"({template_valid['agree_pct']}%)  unmapped tokens: {template_valid['template_unmapped_tokens']}")
    print(f"combined capacity (all): {capacity['all']['combined_tokens_per_param']} tokens/param "
          f"(pass={capacity['all']['passes_combined_bound']})")


def _write_summary(inventory, capacity, template_valid, sanity, all_tabs):
    L = ["=== note-side table fit (part 2 §3/§4/§5) — summary ===",
         f"corpus git_hash: {inventory['provenance']['corpus_git_hash']}",
         f"counted stems: {inventory['counted_population']['counted_stems']}  "
         f"excluded: {inventory['counted_population']['excluded_counts']}",
         "",
         f"template mapping vs music21 oracle: {template_valid['agree']}/{template_valid['tokens_checked']} "
         f"({template_valid['agree_pct']}%); unmapped {template_valid['template_unmapped_tokens']} tokens; "
         f"residual disagree {template_valid['residual_total_tokens']} tokens",
         "",
         "-- combined capacity (part1 + part2), per fold --"]
    for name in ["all"] + [f"fold{i}" for i in range(N_FOLDS)]:
        c = capacity[name]
        L.append(f"  {name:6s} params {c['combined_free_params']:5d}  tokens {c['combined_tokens']:7d}  "
                 f"tok/param {c['combined_tokens_per_param']:8.2f}  pass={c['passes_combined_bound']}")
    L += ["",
          "-- emission base category rates --",
          f"  {inventory['emission_headline']['base_category_distribution']}",
          "-- covariate-support effect (L2:0 unsupported vs L2:1 supported) --"]
    for k, v in inventory["emission_headline"]["covariate_support_effect"].items():
        L.append(f"  {k}: {v}")
    L += ["",
          "-- spelling: minor leading-tone (raised7) vs subtonic (dia:-2) --",
          f"  P(raised7)={sanity['minor_spelling_P_raised7']}  P(subtonic)={sanity['minor_spelling_P_subtonic_dia_minus2']}  "
          f"leading>subtonic={sanity['leading_tone_cell_greater_than_subtonic']}",
          "-- sanity: minor V-labeled note counts raised7 vs flat7 --",
          f"  raised7={sanity['minor_V_segments_raised7_note_count']}  flat7={sanity['minor_V_segments_flat7_note_count']}  "
          f"raised7>>flat7={sanity['raised7_much_greater_than_flat7']}",
          "",
          "-- event-level boundary P (event denominator) vs robust first-event --"]
    for c in ("downbeat", "mid_strong", "other_tactus", "sub_tactus"):
        e = all_tabs["event_boundary_by_beat_class"][c]
        r = all_tabs["event_boundary_by_beat_class_robust_firstevent"][c]
        L.append(f"  {c:13s} exact P={e['prob']}  ({e['boundary']}/{e['events']})   "
                 f"robust P={r['prob']}  ({r['boundary']}/{r['events']})")
    (OUT_DIR / "note_table_fit_inventory_summary.txt").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
