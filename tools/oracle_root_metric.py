#!/usr/bin/env python3
"""oracle_root_metric.py — the STANDING per-event, tiered oracle-root metric.

READ-ONLY MEASUREMENT TOOL. It only *reads* validated per-preset corpora and *emits*
case-identity sets — exactly like ``characterise_bir_false.py``. It touches no
production / analyzer / scoring / gate code and changes no threshold.

North star (the project rule): best = CORRECT vs the DCML/music21 oracle, not the BIR
gate. This tool measures that directly, at the oracle's native per-event grid, and reports
the decomposition **tiers separately** (no premature collapse) so effort is steered onto
genuine error, not convention boundaries.

It is the first committed tooling in the metric arc. It consolidates two throwaway
diagnostics — ``cc_round3_measure.py`` (the per-event charged/floor separation) and
``cc_decomp_measure.py`` (the KEY/OVER-GRAB/CHORD-ID/AMBIGUOUS decomposition) — into one
standing, manifest-validated, tested tool, with the KEY band further split into
KEY-HARD vs KEY-TONICIZATION (the design's mandated separation).

────────────────────────────────────────────────────────────────────────────────────────
GRANULARITY (round-3 semantics)
  * one scored "event" per DCML annotation (each place the oracle asserts a root);
  * event tick = the DCML annotation's ONSET tick, reconstructed from OUR region
    measure-anchors via ``compare_analyses._dcml_time_spans`` (the WiR .rntxt has no
    absolute-tick column);
  * our root and music21's root at that event = the root of the region (ours / music21)
    whose [start, end) CONTAINS the tick (tick-containment — no onset-vs-overlap choice).

PREDICATE (per event, bass-decoupled, pc-typed — reused verbatim)
  ``compare_analyses.three_way_classify(our_pc, m21_pc, dcml_pc)``.
  Our absent-root (-1) and music21 absent-root are normalized to None; ``three_way_classify``
  then returns ``no_dcml`` for them (so an absent-our-root event is NOT charged — it is the
  flagged residual, never silently charged).

THE TWO TOP-LEVEL BUCKETS (clean by construction — no event is ever both)
  CHARGED = {three_way_classify == 'music21_dcml_agree'}  (m21 == dcml != ours) — genuine
            oracle-root error. A charge requires m21 == dcml.
  FLOOR   = {events where m21 and dcml are both present and m21 != dcml} — the genuine
            same-event oracle dispute / symmetric-dim7. A floor requires m21 != dcml.
  CHARGED and FLOOR are NEVER summed.

THE 5 CHARGED SUB-TIERS (each charged event lands in exactly one)
  KEY-HARD          our key != DCML-local key, AND music21 corroborates DCML (m21 key ==
                    DCML key) — our key differs from BOTH oracles → genuine key-detection
                    error.
  KEY-TONICIZATION  our key != DCML-local key, but music21 disputes DCML's local key
                    (m21 key != DCML key) — the local-vs-global tonicization-labeling grain;
                    reported SEPARATELY (it is partly convention, never folded into KEY-HARD).
  OVER-GRAB         our key matches the oracle key, but our single region covering the event
                    spans >= 2 distinct oracle roots → segmentation under-grab.
  CHORD-ID          our key matches, region aligns ~1:1 (exactly 1 oracle root in its span),
                    root still wrong → vertical / competition miss.
  AMBIGUOUS         our key matches DCML but music21 disputes the oracle key (m21 != DCML),
                    or a key string is unparseable — cannot be cleanly bucketed; size
                    reported, never forced.
  KEY-HARD + KEY-TONICIZATION == the aggregate KEY band; the 5 tiers sum to the per-record
  charged total.

CASE-IDENTITY = ``stem@tick`` (the reconstructed DCML onset tick; preset-stable because the
reconstruction is done per-preset from our anchors). Two DCML annotations can reconstruct to
the same tick (co-tick); these are distinct *records* but share one identity string, so the
deduped identity-set size is slightly below the per-record count. The exact per-record and deduped
counts are the tool's OWN printed output (regenerable) — not hand-transcribed here (#17f), because
they drift with each L3-wiring / grading re-baseline (the former docstring figures 3882/4083/3914 &
3862/4065/3894 predated the −4/+1/−4 L3-wiring delta and the OI-142/OI-143 re-baseline).

Reuses ``characterise_bir_false.validate_corpus_dir`` (the anti-contamination manifest guard),
``compare_analyses`` (load_analysis, three_way_classify, _dcml_time_spans), and
``dcml_parser`` (find_wir_file, parse_rntxt_file, _key_to_tonic_pc, _NOTE_TO_PC) verbatim —
none of those modules is forked.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))

import compare_analyses as cmp           # noqa: E402  (reused verbatim)
import dcml_parser as dcml               # noqa: E402  (reused verbatim)
from characterise_bir_false import validate_corpus_dir  # noqa: E402 (reused verbatim)

_WIR_DIR = _ROOT / "tools" / "dcml" / "when_in_rome"

PC_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def pcn(p):
    return PC_NAMES[p % 12] if p is not None and p >= 0 else "?"


# ── key parsing (tool-local glue; mode-class only, third-of-the-mode for exotic modes) ──
# Ported verbatim from the ratified decomposition diagnostic; covered by the tool's tests.
#
# OI-132 / DISCOVERY D2 (OI-145 wave-1, 2026-07-12): this parse_our_key is a SECOND key-string
# parser alongside the shared substrate compare_rn._our_key_tonic (the one every GOVERNING graded
# surface — a8, the robust unit, the classifier, the probe — uses). They are NOT interchangeable:
# they embed DIFFERENT music-theory decisions for the DOMINANT-family exotic modes.
#   • parse_our_key (below, exact-set membership): PhrygDom -> MAJOR, alt -> MAJOR, Lydb7 -> None.
#   • compare_rn._our_key_tonic (prefix rule maj/ion/lyd/mix): PhrygDom -> minor, alt -> minor,
#     Lydb7 -> major.
# MEASURED consolidation impact (A/B, OI-145 wave-1): parse_dcml_key IS byte-identical to
# compare_rn._dcml_key_tonic, but swapping THIS parser for _our_key_tonic MOVES this tool's KEY-tier
# split (jazz +1 record, default +13 records shuffling KEY-HARD/KEY-TONICIZATION/AMBIGUOUS; the
# charged/floor ROOT sets are UNCHANGED on all 3 presets). So the DT-6 dedup is NOT a byte-identical
# hygiene fold — it needs a music-theory adjudication of the dominant-family mode classification
# (which reading is authoritative), then a coordinated re-baseline. NOT consolidated here; surfaced
# for the user's decision (cc_measurement_chain_hardening_report.md).
_OUR_MINOR_MODES = {"min", "harm", "mel", "Dor", "Dor#4", "Dorb2", "Phryg", "Loc#6"}
_OUR_MAJOR_MODES = {"maj", "Lyd", "Lyd#2", "Lyd+", "Mixolyd", "Mixb6", "PhrygDom", "alt"}


def parse_our_key(k: str):
    """'Gmin'/'Bbmaj'/'AMix(b6)' -> (tonic_pc, 'major'|'minor'|None)."""
    if not k:
        return None, None
    k = k.replace("♯", "#").replace("♭", "b")
    m = re.match(r"^([A-G][#b]?)(.*)$", k)
    if not m:
        return None, None
    tonic = dcml._key_to_tonic_pc(m.group(1))
    suf = m.group(2)
    if suf in _OUR_MINOR_MODES:
        return tonic, "minor"
    if suf in _OUR_MAJOR_MODES:
        return tonic, "major"
    return tonic, None  # unknown mode -> tonic only


def parse_dcml_key(k: str):
    """DCML local key 'g'/'Bb' -> (tonic_pc, 'major'|'minor')."""
    if not k:
        return None, None
    tonic = dcml._key_to_tonic_pc(k)
    mode = "minor" if k[0].islower() else "major"
    return tonic, mode


def parse_m21_key(k: str):
    """music21 key 'g minor'/'B- major'/'f# minor' -> (tonic_pc, 'major'|'minor').
    music21 uses '-' for flat and a ' major'/' minor' suffix; case = mode."""
    if not k:
        return None, None
    k = k.strip()
    m = re.match(r"^([A-Ga-g])([#\-b]*)\s+(major|minor)$", k)
    if not m:
        return None, None
    base = dcml._NOTE_TO_PC.get(m.group(1).upper())
    if base is None:
        return None, None
    acc = m.group(2)
    pc = (base + acc.count("#") - acc.count("-") - acc.count("b")) % 12
    return pc, m.group(3)


# ── corpus loading ──────────────────────────────────────────────────────────
def load_dir(corpus_dir: Path, wir_dir: Path):
    """Return {stem: (ours_regions, m21_regions, wir_regions)} for a corpus dir.

    Mirrors the throwaway loaders: a stem is included only when both {stem}.ours.json
    and {stem}.music21.json load and ours is non-empty. wir may be empty (the 27
    chorales without a When-in-Rome annotation contribute no scoreable events).
    """
    out = {}
    for ours_path in sorted(corpus_dir.glob("*.ours.json")):
        stem = ours_path.stem.replace(".ours", "")
        m21_path = corpus_dir / f"{stem}.music21.json"
        if not m21_path.exists():
            continue
        try:
            _, ours = cmp.load_analysis(ours_path)
            _, m21 = cmp.load_analysis(m21_path)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            # OI-128: narrow + surface the whole-stem drop (was a silent bare-except continue).
            print(f"[oracle_root_metric] DROPPED {stem} — load failed "
                  f"({type(exc).__name__}: {exc})", file=sys.stderr)
            continue
        if not ours:
            continue
        # OI-144 / DISCOVERY D3: raw WiR (parse_rntxt_file), NOT the OI-142-corrected load_wir_regions
        # — the 12 transposed editions grade UNCORRECTED here, so this tool's charged/floor root figures
        # are on pre-OI-142 WiR. Routing through load_wir_regions is a RE-BASELINE (moves the figures),
        # surfaced for the user; left raw this session (cc_measurement_chain_hardening_report.md).
        wir_path = dcml.find_wir_file(str(wir_dir), stem)
        wir = []
        if wir_path:
            try:
                wir = dcml.parse_rntxt_file(wir_path)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                print(f"[oracle_root_metric] {stem}: WiR parse failed, no GT root "
                      f"({type(exc).__name__}: {exc})", file=sys.stderr)
                wir = []
        out[stem] = (ours, m21, wir)
    return out


def region_at(regions, tick):
    """The region whose [start,end) contains tick (tick-containment), with a
    boundary fallback to a region starting exactly at tick (end-exclusive edge)."""
    for r in regions:
        if r.start_tick <= tick < r.end_tick:
            return r
    for r in regions:
        if r.start_tick == tick:
            return r
    return None


# ── the per-event classifier ─────────────────────────────────────────────────
TIERS = ["KEY-HARD", "KEY-TONICIZATION", "OVER-GRAB", "CHORD-ID", "AMBIGUOUS"]


def classify_charged_event(our_r, m21_r, dcml_events_in_region, dr):
    """Bucket ONE charged event into exactly one of the 5 tiers.

    `dcml_events_in_region` = the count of distinct oracle roots over the DCML events
    whose onset falls inside our covering region's [start, end) (the over-grab test).
    Returns (tier, why).
    """
    our_tonic, our_mode = parse_our_key(our_r.key if our_r else "")
    dcml_tonic, dcml_mode = parse_dcml_key(dr.local_key)
    m21_tonic, _ = parse_m21_key(m21_r.key if m21_r else "")

    # Unparseable key on either authoritative side -> cannot bucket cleanly.
    if our_tonic is None or dcml_tonic is None:
        return "AMBIGUOUS", "unparseable_key"

    # Does music21 (the corroborator) dispute DCML's local key at this event?
    oracle_key_disputed = (m21_tonic is not None and m21_tonic != dcml_tonic)

    tonic_match = (our_tonic == dcml_tonic)
    # mode compared only when both sides resolve to maj/minor
    mode_match = (our_mode is None or dcml_mode is None or our_mode == dcml_mode)
    key_match = tonic_match and mode_match

    if not key_match:
        # KEY band — split on whether music21 corroborates DCML (hard) or disputes it
        # (tonicization / local-vs-global grain). The separation is the whole point.
        if oracle_key_disputed:
            return "KEY-TONICIZATION", ("tonic" if not tonic_match else "mode-only")
        return "KEY-HARD", ("tonic" if not tonic_match else "mode-only")

    # our key matches DCML's local key
    if oracle_key_disputed:
        # our key matches DCML but m21 disputes it -> oracle key not cleanly established
        return "AMBIGUOUS", "oracle_key_disputed_keymatch"

    # all three agree on the key -> segmentation vs vertical
    if dcml_events_in_region >= 2:
        return "OVER-GRAB", f"{dcml_events_in_region}_oracle_roots_in_region"
    return "CHORD-ID", "1_oracle_root_in_region"


def run_preset(corpus_dir: Path, wir_dir: Path):
    """Compute the per-event tiered metric for one validated corpus dir.

    Returns a result dict with the round-3 charged/floor identity sets, the per-record
    decomposition tier sets, and the supporting totals + flagged residuals.
    """
    manifest = validate_corpus_dir(corpus_dir)
    data = load_dir(corpus_dir, wir_dir)

    charged_ids = set()      # round-3 charged identity set (deduped stem@tick)
    floor_ids = set()        # round-3 floor identity set (deduped stem@tick)
    tier_ids = {t: [] for t in TIERS}   # per-record (id may repeat on co-tick)
    tier_ids_set = {t: set() for t in TIERS}

    n_events = n_scoreable = n_correct = 0
    n_dcml_ours = 0          # floor sub: our sides with DCML vs m21
    n_all_differ = 0         # floor sub: m21 != dcml, three-way
    charged_records = 0      # per-record charged count (decomposition base)
    n_absent_our = 0         # flagged residual: oracle pair concurs, our root absent
    wir_cov = 0
    examples = defaultdict(list)   # tier -> a few worked examples

    for stem, (ours, m21, wir) in data.items():
        if not wir or not ours:
            continue
        wir_cov += 1
        spans = cmp._dcml_time_spans(ours, wir)

        # all DCML events with a valid reconstructed span (for the over-grab test)
        dcml_events = []
        for dr, (ds, de) in zip(wir, spans):
            if ds < 0 or de <= ds:
                continue
            dcml_events.append((ds, de, dr))

        for ds, de, dr in dcml_events:
            our_r = region_at(ours, ds)
            m21_r = region_at(m21, ds)
            our_pc = our_r.root_pc if (our_r and our_r.root_pc is not None and our_r.root_pc >= 0) else None
            m21_pc = m21_r.root_pc if (m21_r and m21_r.root_pc is not None and m21_r.root_pc >= 0) else None
            dcml_pc = dr.root_pc

            n_events += 1
            scoreable = (m21_pc is not None and dcml_pc is not None)
            if scoreable:
                n_scoreable += 1

            cat = cmp.three_way_classify(our_pc, m21_pc, dcml_pc)
            ident = f"{stem}@{ds}"

            # FLOOR: m21 and dcml both present and disagree (independent of our root).
            if scoreable and (m21_pc != dcml_pc):
                floor_ids.add(ident)
                if cat == "dcml_ours_agree":
                    n_dcml_ours += 1
                elif cat == "all_differ":
                    n_all_differ += 1

            if cat == "all_agree":
                n_correct += 1
                continue

            # flagged residual: oracle pair concurs (m21==dcml) but our root absent
            if (m21_pc is not None and dcml_pc is not None and m21_pc == dcml_pc
                    and our_pc is None):
                n_absent_our += 1

            if cat != "music21_dcml_agree":
                continue

            # ── CHARGED event ──────────────────────────────────────────────
            charged_records += 1
            charged_ids.add(ident)

            # over-grab test: distinct oracle roots over DCML events inside our region
            roots_in_region = set()
            if our_r:
                for ds2, de2, dr2 in dcml_events:
                    if our_r.start_tick <= ds2 < our_r.end_tick and dr2.root_pc is not None:
                        roots_in_region.add(dr2.root_pc)
            tier, why = classify_charged_event(our_r, m21_r, len(roots_in_region), dr)
            tier_ids[tier].append(ident)
            tier_ids_set[tier].add(ident)
            if len(examples[tier]) < 6:
                examples[tier].append({
                    "id": ident, "meas": dr.measure_number, "beat": dr.beat,
                    "dcml": f"{dr.local_key}:{dr.roman_numeral}->{pcn(dcml_pc)}",
                    "ours": f"{(our_r.key if our_r else '?')}:{(our_r.chord_symbol if our_r else '?')}->{pcn(our_pc)}",
                    "m21": f"{(m21_r.key if m21_r else '?')}->{pcn(m21_pc)}",
                    "why": why,
                })

    return {
        "preset": manifest.get("preset", "?"),
        "git_hash": manifest.get("git_hash", "?"),
        "scores": len(data),
        "wir_coverage": wir_cov,
        "n_events": n_events,
        "n_scoreable": n_scoreable,
        "n_correct": n_correct,
        "charged_records": charged_records,
        "charged_set": charged_ids,
        "floor_set": floor_ids,
        "floor_dcml_ours_agree": n_dcml_ours,
        "floor_all_differ": n_all_differ,
        "tier_records": {t: len(tier_ids[t]) for t in TIERS},
        "tier_sets": {t: tier_ids_set[t] for t in TIERS},
        "tier_ids": tier_ids,
        "absent_our_residual": n_absent_our,
        "examples": dict(examples),
    }


# ── reporting ────────────────────────────────────────────────────────────────
def format_report(res: dict) -> str:
    L = []
    rec = res["charged_records"]
    cset = len(res["charged_set"])
    fset = len(res["floor_set"])
    L.append("=" * 86)
    L.append(f" {res['preset']}  (git {res['git_hash']})  "
             f"{res['scores']} scores, {res['wir_coverage']} with WiR coverage")
    L.append("=" * 86)
    L.append(f"  scoreable events : {res['n_scoreable']:>6}   "
             f"correct: {res['n_correct']:>6}")
    L.append("")
    L.append(f"  CHARGED (genuine oracle-root error)  set-identity={cset}   "
             f"per-record={rec}   (co-tick +{rec - cset})")
    L.append(f"    {'tier':<18} {'records':>8} {'%charged':>9}   {'identities':>10}")
    L.append("    " + "-" * 52)
    key_rec = res["tier_records"]["KEY-HARD"] + res["tier_records"]["KEY-TONICIZATION"]
    L.append(f"    {'KEY (aggregate)':<18} {key_rec:>8} {100*key_rec/rec:>8.1f}%")
    for t in TIERS:
        n = res["tier_records"][t]
        idn = len(res["tier_sets"][t])
        pct = 100 * n / rec if rec else 0.0
        lead = "      " if t.startswith("KEY-") else "    "
        name = t if not t.startswith("KEY-") else t
        L.append(f"{lead}{name:<{18 if not t.startswith('KEY-') else 16}} {n:>8} {pct:>8.1f}%   {idn:>10}")
    tier_sum = sum(res["tier_records"][t] for t in TIERS)
    L.append("    " + "-" * 52)
    L.append(f"    {'(tier sum)':<18} {tier_sum:>8}   "
             f"{'OK' if tier_sum == rec else 'MISMATCH!'}")
    L.append("")
    L.append(f"  FLOOR (same-event oracle dispute m21!=dcml)  set-identity={fset}   "
             f"per-record={res['floor_dcml_ours_agree'] + res['floor_all_differ']}")
    L.append(f"    dcml_ours_agree (we side with DCML): {res['floor_dcml_ours_agree']}")
    L.append(f"    all_differ (three-way dispute)     : {res['floor_all_differ']}")
    L.append("")
    L.append(f"  FLAGGED residual (oracle pair concurs, our root ABSENT — NOT charged): "
             f"{res['absent_our_residual']}")
    return "\n".join(L)


def emit_json(results: list[dict]) -> dict:
    """Serialize case-identity sets for each preset (sets -> sorted lists)."""
    out = {}
    for res in results:
        out[res["preset"]] = {
            "git_hash": res["git_hash"],
            "scores": res["scores"],
            "wir_coverage": res["wir_coverage"],
            "n_scoreable": res["n_scoreable"],
            "n_correct": res["n_correct"],
            "charged_records": res["charged_records"],
            "charged_set_size": len(res["charged_set"]),
            "charged_set": sorted(res["charged_set"]),
            "floor_set_size": len(res["floor_set"]),
            "floor_set": sorted(res["floor_set"]),
            "floor_dcml_ours_agree": res["floor_dcml_ours_agree"],
            "floor_all_differ": res["floor_all_differ"],
            "tier_records": res["tier_records"],
            "tier_identities": {t: sorted(res["tier_ids"][t]) for t in TIERS},
            "absent_our_residual": res["absent_our_residual"],
            "examples": res["examples"],
        }
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Standing per-event tiered oracle-root metric (read-only). Validates "
                    "each corpus manifest, then emits CHARGED/FLOOR + the 5 charged "
                    "sub-tiers (KEY-HARD/KEY-TONICIZATION/OVER-GRAB/CHORD-ID/AMBIGUOUS) "
                    "with case-identity (stem@tick) sets.")
    parser.add_argument("--corpus-dir", metavar="DIR", action="append", required=True,
                        help="Per-preset corpus dir to measure (repeatable).")
    parser.add_argument("--wir-dir", metavar="DIR", default=str(_WIR_DIR),
                        help="When-in-Rome (DCML) annotation dir.")
    parser.add_argument("--emit-json", metavar="PATH", default=None,
                        help="Write the full per-tier case-identity sets to PATH as JSON.")
    args = parser.parse_args(argv)

    wir_dir = Path(args.wir_dir)
    results = []
    for d in args.corpus_dir:
        corpus_dir = Path(d)
        try:
            res = run_preset(corpus_dir, wir_dir)
        except Exception as exc:
            print(f"ERROR measuring {corpus_dir}: {exc}", file=sys.stderr)
            sys.exit(2)
        results.append(res)
        print(format_report(res))
        print()

    if args.emit_json:
        Path(args.emit_json).write_text(
            json.dumps(emit_json(results), indent=1), encoding="utf-8")
        print(f"Wrote case-identity sets -> {args.emit_json}")


if __name__ == "__main__":
    main()
