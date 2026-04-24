#!/usr/bin/env python3
"""
music21_batch.py — Export music21 corpus scores to MusicXML and produce a
JSON harmonic analysis for each score.

The JSON format matches the output of batch_analyze (our C++ tool) so that
compare_analyses.py can align and compare the two without format translation.

Key design notes:
  - music21's romanNumeralFromChord() is STATELESS — it has no temporal context
    and operates on a single chord snapshot.  This means Roman numerals may
    differ from ours in transitional passages.
  - Key detection is performed two ways and both are stored:
      "key"      — Krumhansl-Schmuckler global key (score.analyze('key'))
      "keyLocal" — FloatingKey local sliding-window key (where available)
  - Tick offsets use 480 ticks per quarter note (matching MuseScore / batch_analyze).

Usage:
    python tools/music21_batch.py [--composer COMPOSER] [--output DIR] [--single NAME]
    python tools/music21_batch.py --composer beethoven --output tools/corpus
    python tools/music21_batch.py --single bach/bwv66.6

Options:
    --composer NAME  Composer name as used in music21 corpus (default: bach)
    --output DIR     Directory to write .xml and .music21.json files
                     (default: tools/corpus relative to CWD)
    --single NAME    Process one score and print a diagnostic to stdout
    --help           Show this message
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import traceback
from pathlib import Path

try:
    from music21 import corpus, roman
    from music21.analysis import floatingKey as m21_floatingKey
    _HAS_FLOATING_KEY = True
except ImportError:
    _HAS_FLOATING_KEY = False

try:
    import music21  # noqa: F401
except ImportError:
    print("music21 is not installed.  Install it with:  pip install music21",
          file=sys.stderr)
    sys.exit(1)

# Canonical source location for music21 corpus files (read-only, do not modify).
# Working copies (exported XML + JSON analyses) live in tools/corpus/.
# XML files annotated with music21 Roman numerals live in tools/corpus_m21_xml/.
# Detected dynamically so the path is correct regardless of Python installation.
try:
    M21_CORPUS_ROOT = Path(music21.__file__).parent / "corpus"
except Exception:
    M21_CORPUS_ROOT = Path(
        r"C:\Users\vince\AppData\Local\Python\pythoncore-3.14-64"
        r"\Lib\site-packages\music21\corpus"
    )
M21_CORPUS_BACH_DIR = M21_CORPUS_ROOT / "bach"


# ── Constants ──────────────────────────────────────────────────────────────

TICKS_PER_QUARTER = 480   # must match MuseScore's Constants::DIVISION


# ── Chorale filter ─────────────────────────────────────────────────────────

# Variant suffixes to exclude — keep only canonical editions.
_VARIANT_SUFFIXES = {"-sc", "-lpz", "-lz", "-w", "-inst",
                     "-a", "-2", "-s", "-b", "-c"}

# Known non-chorale BWV numbers (keyboard works, etc.).
_NON_CHORALE_BWV = {"846", "846a"}


def _is_bach_chorale(path: str, score) -> bool:
    """
    Returns True only for SATB Bach chorales.
    Excludes: keyboard works, motets, variant/duplicate editions.
    """
    p = str(path).lower()

    # Must have BWV number
    if "bwv" not in p:
        return False

    # Exclude variant suffixes — keep only canonical editions
    basename = os.path.splitext(os.path.basename(p))[0]
    for suffix in _VARIANT_SUFFIXES:
        if basename.endswith(suffix):
            return False

    # Exclude known non-chorale BWV numbers
    bwv_match = re.search(r'bwv(\d+)', p)
    if bwv_match and bwv_match.group(1) in _NON_CHORALE_BWV:
        return False

    # Verify exactly 4 parts (SATB) — excludes keyboard and motet movements
    try:
        if len(score.parts) != 4:
            return False
    except Exception:
        return False

    return True


def _chorale_reject_reason(path: str, score) -> str:
    """Return a short rejection-reason string for logging purposes."""
    p = str(path).lower()
    if "bwv" not in p:
        return "no_bwv"
    basename = os.path.splitext(os.path.basename(p))[0]
    for suffix in _VARIANT_SUFFIXES:
        if basename.endswith(suffix):
            return "variant_suffix"
    bwv_match = re.search(r'bwv(\d+)', p)
    if bwv_match and bwv_match.group(1) in _NON_CHORALE_BWV:
        return "non_chorale_bwv"
    try:
        n = len(score.parts)
        return f"wrong_part_count_{n}"
    except Exception:
        return "part_count_error"


# ── Quality mapping ────────────────────────────────────────────────────────

_QUALITY_MAP: dict[str, str] = {
    "major":             "Major",
    "minor":             "Minor",
    "diminished":        "Diminished",
    "augmented":         "Augmented",
    "half-diminished":   "HalfDiminished",
    "dominant-seventh":  "Major",   # dominant 7th has a major triad
    "major-seventh":     "Major",
    "minor-seventh":     "Minor",
    "suspended-second":  "Suspended2",
    "suspended-fourth":  "Suspended4",
    "power":             "Power",
}


def _normalize_quality(m21_quality: str) -> str:
    return _QUALITY_MAP.get(m21_quality.lower(), "Unknown")


# ── Key formatting ─────────────────────────────────────────────────────────

def _key_to_str(k) -> str:
    """Return a key string in the same format as batch_analyze: 'E major', 'b minor'."""
    if k is None:
        return "unknown"
    return str(k)           # music21 Key.__str__ gives e.g. "E major", "b minor"


# ── Single-chorale analysis ────────────────────────────────────────────────

def analyze_chorale(score, source_name: str) -> dict:
    """
    Run harmonic analysis on a music21 Score and return a dict in the same
    schema as batch_analyze's JSON output.

    Fields produced:
        source, detectedKey, keyConfidence, regions[]
        Each region: measureNumber, beat, startTick, endTick, duration,
                     rootPitchClass, quality, chordSymbol, romanNumeral,
                     key, keyLocal, diatonicToKey (always null — music21 doesn't
                     expose this directly), alternatives (always empty — music21
                     returns only one candidate).
    """
    # ── Global key (Krumhansl-Schmuckler) ──────────────────────────────────
    try:
        global_key = score.analyze("key")
        key_confidence = float(getattr(global_key, "correlationCoefficient", 0.0))
    except Exception:
        global_key = None
        key_confidence = 0.0

    # ── Optional: FloatingKey local sliding window ─────────────────────────
    fk_analyzer = None
    if _HAS_FLOATING_KEY:
        try:
            fk_analyzer = m21_floatingKey.FloatingKey()
            fk_analyzer.numFlats = 4
            fk_analyzer.numSharps = 4
        except Exception:
            fk_analyzer = None

    # ── Chordify ───────────────────────────────────────────────────────────
    try:
        chordified = score.chordify()
    except Exception as exc:
        return {
            "source":         source_name,
            "detectedKey":    _key_to_str(global_key),
            "keyConfidence":  key_confidence,
            "regions":        [],
            "error":          str(exc),
        }

    regions = []

    for elem in chordified.flatten().getElementsByClass("Chord"):
        root = elem.root()
        if root is None:
            continue

        # ── Tick positions (480 ticks per quarter note) ────────────────────
        start_tick = int(float(elem.offset) * TICKS_PER_QUARTER)
        dur_ql     = float(elem.duration.quarterLength)
        end_tick   = int((float(elem.offset) + dur_ql) * TICKS_PER_QUARTER)

        # ── Local key ─────────────────────────────────────────────────────
        local_key = global_key
        if fk_analyzer is not None:
            try:
                local_key = fk_analyzer.analyze(score, elem.offset)
            except Exception:
                local_key = global_key

        # ── Roman numeral ─────────────────────────────────────────────────
        rn_str = "?"
        if local_key is not None:
            try:
                rn = roman.romanNumeralFromChord(elem, local_key)
                rn_str = rn.figure
            except Exception:
                rn_str = "?"

        # ── Chord symbol ───────────────────────────────────────────────────
        chord_sym = elem.commonName or root.name
        try:
            chord_sym = elem.pitches[0].name if not chord_sym else chord_sym
        except Exception:
            pass

        region = {
            "measureNumber":  getattr(elem, "measureNumber", None),
            "beat":           float(getattr(elem, "beat", 1.0)),
            "startTick":      start_tick,
            "endTick":        end_tick,
            "duration":       round(dur_ql, 6),
            "rootPitchClass": int(root.pitchClass),
            "quality":        _normalize_quality(elem.quality),
            "chordSymbol":    chord_sym,
            "romanNumeral":   rn_str,
            "key":            _key_to_str(local_key),
            "keyGlobal":      _key_to_str(global_key),
            # music21 doesn't expose a direct diatonic-to-key boolean;
            # compare_analyses.py derives this from the romanNumeral figure
            "diatonicToKey":  None,
            # music21's romanNumeralFromChord returns a single result; no alternatives
            "alternatives":   [],
        }
        regions.append(region)

    return {
        "source":        source_name,
        "detectedKey":   _key_to_str(global_key),
        "keyConfidence": round(key_confidence, 4),
        "regions":       regions,
    }


# ── Name helpers ──────────────────────────────────────────────────────────

def stem_from_corpus_path(corpus_path: str) -> str:
    """
    Derive a short, stable output stem from a music21 corpus path or full path.

    Uses the corpus-relative path so subdirectory scores get a unique prefix:

        ".../bach/bwv1.6.mxl"                   →  "bwv1.6"
        ".../beethoven/opus132.mxl"              →  "beethoven_opus132"
        ".../beethoven/opus59no1/movement1.mxl"  →  "beethoven_opus59no1_movement1"
        "bach/bwv66.6"   (short corpus name)     →  "bwv66.6"
        "beethoven/opus59no1/movement1"          →  "beethoven_opus59no1_movement1"

    Bach names keep their existing short form (no "bach_" prefix) to preserve
    backward compatibility with already-exported corpus files.
    """
    p = Path(corpus_path)
    # Strip known music-file extensions
    if p.suffix.lower() in (".mxl", ".xml", ".musicxml", ".mscz", ".mscx"):
        p = p.with_suffix("")

    # Try to make path relative to the known music21 corpus root
    try:
        rel = p.relative_to(M21_CORPUS_ROOT)
        parts = rel.parts   # e.g. ("bach", "bwv1.6") or ("beethoven", "opus59no1", "movement1")
        if len(parts) == 2 and parts[0] == "bach":
            return parts[1]   # backward compat: just "bwv1.6"
        return "_".join(parts)
    except ValueError:
        pass

    # Fallback: short corpus name like "bach/bwv66.6" or "beethoven/opus59no1/movement1"
    parts = corpus_path.replace("\\", "/").rstrip("/").split("/")
    # Strip any remaining extension from the last component
    last = parts[-1]
    for ext in (".mxl", ".xml", ".musicxml", ".mscz", ".mscx"):
        if last.lower().endswith(ext):
            last = last[: -len(ext)]
            break
    parts[-1] = last
    if len(parts) == 2 and parts[0] == "bach":
        return parts[1]   # backward compat
    return "_".join(parts)


# ── Corpus access ──────────────────────────────────────────────────────────

def get_composer_paths(composer: str) -> list[str]:
    """
    Return music21 corpus paths for all MXL/XML scores by the given composer.

    For 'bach', pre-filters to files containing 'bwv' as a cheap path-level
    check.  The full SATB chorale filter (_is_bach_chorale) is applied in
    run_batch() after each score is loaded.
    For all other composers, returns every .mxl / .xml file found.
    """
    try:
        paths = corpus.getComposer(composer)
    except Exception as exc:
        print(f"WARNING: could not enumerate {composer!r} corpus: {exc}", file=sys.stderr)
        return []
    result = []
    for p in paths:
        s = str(p).lower()
        if not any(s.endswith(ext) for ext in (".mxl", ".xml", ".musicxml")):
            continue
        if composer.lower() == "bach" and "bwv" not in s:
            continue
        result.append(str(p))
    return result


def get_bach_chorale_paths() -> list[str]:
    """Backward-compatible alias for get_composer_paths('bach')."""
    return get_composer_paths("bach")


# ── Single-chorale mode ────────────────────────────────────────────────────

def run_single(name: str) -> None:
    """Process one chorale and print a detailed per-region diagnostic to stdout."""
    print(f"Loading {name!r} from music21 corpus …", file=sys.stderr)
    try:
        score = corpus.parse(name)
    except Exception as exc:
        print(f"ERROR: could not load {name!r}: {exc}", file=sys.stderr)
        sys.exit(1)

    analysis = analyze_chorale(score, name.replace("/", "_"))
    analysis["corpusName"] = name

    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"  Detected key : {analysis['detectedKey']}  (confidence {analysis['keyConfidence']:.2f})")
    print(f"  Regions      : {len(analysis['regions'])}")
    print(f"{'='*60}\n")

    print(f"  {'Meas':>4}  {'Beat':>5}  {'Ticks':>12}  {'Root':>4}  {'Qual':<15}  {'Symbol':<12}  {'RN':<8}  Key")
    print(f"  {'-'*4}  {'-'*5}  {'-'*12}  {'-'*4}  {'-'*15}  {'-'*12}  {'-'*8}  ---")
    for r in analysis["regions"]:
        tick_range = f"{r['startTick']}-{r['endTick']}"
        print(
            f"  {r['measureNumber']:>4}  {r['beat']:>5.1f}  {tick_range:>12}  "
            f"{r['rootPitchClass']:>4}  {r['quality']:<15}  {r['chordSymbol']:<12}  "
            f"{r['romanNumeral']:<8}  {r['key']}"
        )
    print()


# ── Batch mode ─────────────────────────────────────────────────────────────

def process_chorale(corpus_path: str, output_dir: Path, score=None) -> dict | None:
    """
    Process one chorale: export MusicXML and write a .music21.json analysis.
    Returns the analysis dict on success, None on failure.

    If ``score`` is passed (a pre-loaded music21 Score), it is used directly
    and the corpus.parse() call is skipped — avoids double-loading when the
    caller already parsed the score for filter checks.
    """
    stem = stem_from_corpus_path(corpus_path)

    xml_path  = output_dir / f"{stem}.xml"
    json_path = output_dir / f"{stem}.music21.json"

    if score is None:
        try:
            score = corpus.parse(corpus_path)
        except Exception as exc:
            print(f"  ERROR loading {corpus_path!r}: {exc}", file=sys.stderr)
            return None

    # Export MusicXML (skip if already exported).
    # Some scores contain inexpressible durations that music21 cannot re-encode
    # as standard MusicXML.  Fall back to copying the original MXL — our C++
    # batch_analyze can still open it, and the analysis uses the in-memory score.
    if not xml_path.exists():
        try:
            score.write("musicxml", fp=str(xml_path))
        except Exception as exc:
            print(f"  WARNING: MusicXML export failed for {corpus_path!r}: {exc}; "
                  "trying MXL copy …", file=sys.stderr)
            src = Path(corpus_path)
            if src.exists() and src.suffix.lower() == ".mxl":
                import shutil
                mxl_path = xml_path.with_suffix(".mxl")
                shutil.copy2(src, mxl_path)
                # Point xml_path at the MXL so downstream tools can find it
                xml_path = mxl_path
                print(f"  Copied original MXL to {mxl_path.name}", file=sys.stderr)
            else:
                print(f"  ERROR: no fallback available for {corpus_path!r}", file=sys.stderr)
                return None

    # Analyse (uses the already-loaded in-memory score regardless of export outcome)
    try:
        analysis = analyze_chorale(score, stem)
    except Exception as exc:
        print(f"  ERROR analysing {corpus_path!r}: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None

    analysis["corpusName"] = corpus_path

    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(analysis, fh, indent=2)

    return analysis


def run_batch(output_dir: Path, composer: str = "bach") -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = get_composer_paths(composer)
    if not paths:
        print(f"No scores found for composer {composer!r} in the music21 corpus.",
              file=sys.stderr)
        sys.exit(1)

    total        = len(paths)
    apply_filter = composer.lower() == "bach"
    print(f"Retrieved {total} {composer} path(s) from music21 corpus.")
    if apply_filter:
        print("Applying SATB chorale filter …")

    ok               = 0
    accepted         = 0
    rejected         = 0
    reject_reasons: dict[str, int] = {}

    for idx, path in enumerate(paths, 1):
        stem = stem_from_corpus_path(path)

        # Load the score once — used for both filter check and analysis.
        try:
            score = corpus.parse(path)
        except Exception as exc:
            print(f"  [{idx:>3}/{total}] {stem:<40}  ERROR loading: {exc}",
                  file=sys.stderr)
            continue

        # For Bach: apply the SATB chorale filter before processing.
        if apply_filter and not _is_bach_chorale(path, score):
            reason = _chorale_reject_reason(path, score)
            reject_reasons[reason] = reject_reasons.get(reason, 0) + 1
            rejected += 1
            print(f"  [{idx:>3}/{total}] {stem:<40}  filtered ({reason})")
            continue

        accepted += 1
        result  = process_chorale(path, output_dir, score=score)
        status  = "ok" if result is not None else "FAILED"
        regions = len(result["regions"]) if result else 0
        key     = result.get("detectedKey", "?") if result else "?"
        print(f"  [{idx:>3}/{total}] {stem:<40}  {status}  {regions:>4} regions  key={key}")
        if result is not None:
            ok += 1

    print()
    print(f"{'-'*60}")
    print(f"  Total retrieved : {total}")
    if apply_filter:
        print(f"  Accepted        : {accepted}")
        print(f"  Rejected        : {rejected}")
        for reason, count in sorted(reject_reasons.items(), key=lambda x: -x[1]):
            print(f"    {reason:<30} {count}")
    print(f"  Succeeded       : {ok} / {accepted if apply_filter else total}")
    print(f"  Output dir      : {output_dir}/")
    print(f"{'-'*60}")


# ── CLI ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export Bach chorales from music21 to MusicXML + harmonic analysis JSON.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--composer", default="bach",
                        help="Composer name as in music21 corpus (default: bach)")
    parser.add_argument("--output", default="tools/corpus",
                        help="Directory for output files (default: tools/corpus)")
    parser.add_argument("--single", metavar="NAME",
                        help="Process one score and print diagnostic to stdout")
    args = parser.parse_args()

    if args.single:
        run_single(args.single)
    else:
        run_batch(Path(args.output), composer=args.composer)


if __name__ == "__main__":
    main()
