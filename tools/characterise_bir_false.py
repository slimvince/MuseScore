#!/usr/bin/env python3
"""characterise_bir_false.py — C3/C4 characterisation of the 22 Baroque BIR=false residuals.

Reuses pairing logic from compare_analyses.py (time-overlap alignment to
music21 and to DCML/WiR). A case enters the BIR=false residual set iff:

  - our region is chord_disagree vs music21
  - the winner had bassIsRoot == False
  - music21 AND WiR/DCML agree (three_way_classify == 'music21_dcml_agree')

For each such case, compute delta = (our_root - dcml_root + 12) % 12 in the
prompt's convention (our root MINUS dcml root). Then group by delta and dump
the full case list for the β (delta=5, P4 above DCML) and γ (delta=2, M2 above)
subgroups.

Read-only. No source code or corpus mutations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT       = Path(__file__).resolve().parent.parent
# Default to the Baroque per-preset corpus (Stage 2.2a). Pass --corpus-dir to
# measure a different preset's dir (e.g. tools/corpus/jazz).
_CORPUS_DIR = _ROOT / "tools" / "corpus" / "baroque"
_WIR_DIR    = _ROOT / "tools" / "dcml" / "when_in_rome"

# Kept in sync with run_bach_preset.MANIFEST_NAME.
MANIFEST_NAME = "corpus_manifest.json"

sys.path.insert(0, str(_ROOT / "tools"))
import compare_analyses as cmp
import dcml_parser as dcml


class CorpusValidationError(Exception):
    """Raised when a corpus dir is missing its manifest, is incomplete, or holds a
    file whose fingerprint does not match the manifest (preset contamination — the
    M3 mechanism). The measurement must then refuse to run rather than emit a number
    off a mixed/partial corpus."""


def validate_corpus_dir(corpus_dir: Path) -> dict:
    """Validate that corpus_dir is a single-preset, complete, uncontaminated corpus.

    Returns the parsed manifest on success. Raises CorpusValidationError otherwise.
    Checks, in order: manifest present & parseable; corpus marked complete with
    ours_count == expected_count; every OK score's {stem}.ours.json present and
    sha256-matching the manifest; no extra *.ours.json beyond the OK set.
    """
    manifest_path = corpus_dir / MANIFEST_NAME
    if not manifest_path.exists():
        raise CorpusValidationError(
            f"no {MANIFEST_NAME} in {corpus_dir} — regenerate with "
            f"run_bach_preset.py --preset <P> --output-dir {corpus_dir}")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise CorpusValidationError(f"{manifest_path} is not valid JSON: {exc}")

    preset = manifest.get("preset", "?")
    expected = manifest.get("expected_count")
    ours_count = manifest.get("ours_count")
    if not manifest.get("complete", False) or ours_count != expected:
        raise CorpusValidationError(
            f"corpus is INCOMPLETE (preset={preset}, {ours_count}/{expected} OK) — "
            f"a partial corpus cannot be measured; re-run run_bach_preset.py")

    scores = manifest.get("scores", {})
    ok_stems = {s for s, e in scores.items() if e.get("status") == "OK"}
    present = {p.stem.replace(".ours", "") for p in corpus_dir.glob("*.ours.json")}

    extra = present - ok_stems
    if extra:
        raise CorpusValidationError(
            f"CONTAMINATION: {len(extra)} .ours.json file(s) not in the "
            f"{preset} manifest: {', '.join(sorted(extra))}")
    missing = ok_stems - present
    if missing:
        raise CorpusValidationError(
            f"{len(missing)} manifest score(s) have no .ours.json: "
            f"{', '.join(sorted(missing))}")

    for stem in sorted(ok_stems):
        path = corpus_dir / f"{stem}.ours.json"
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != scores[stem].get("sha256"):
            raise CorpusValidationError(
                f"CONTAMINATION: {stem}.ours.json fingerprint differs from the "
                f"{preset} manifest (foreign-preset / stale file)")
        # OI-124: the paired .music21.json GROUND TRUTH is fingerprinted too when the manifest
        # carries it (a manifest predating the OI-124 stamp skips this check, backward-compatible).
        # A stale/foreign/version-mismatched GT export — read by the a8 variant-(a) genuine filter
        # and the BIR gate — otherwise passed this guard undetected.
        m21_expected = scores[stem].get("music21_sha256")
        if m21_expected is not None:
            m21_path = corpus_dir / f"{stem}.music21.json"
            if not m21_path.exists():
                raise CorpusValidationError(
                    f"{stem}.music21.json GROUND TRUTH missing though the {preset} manifest "
                    f"fingerprints it — regenerate the corpus")
            if hashlib.sha256(m21_path.read_bytes()).hexdigest() != m21_expected:
                raise CorpusValidationError(
                    f"CONTAMINATION: {stem}.music21.json GROUND TRUTH fingerprint differs from "
                    f"the {preset} manifest (stale / foreign / music21-version-mismatched export)")
    return manifest

PC_NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

INTERVAL_NAMES = {
    0:  "unison           (quality-only diff)",
    1:  "m2 above DCML    (semitone)",
    2:  "M2 above DCML    γ (whole-tone)",
    3:  "m3 above DCML",
    4:  "M3 above DCML    (our root = M3 of DCML)",
    5:  "P4 above DCML    β (our root = 4th of DCML)",
    6:  "tritone above DCML",
    7:  "P5 above DCML    (our root = 5th of DCML; classic V-instead-of-I)",
    8:  "m6 above DCML",
    9:  "M6 above DCML    (our root = 6th of DCML)",
    10: "m7 above DCML    (our root = b7 of DCML)",
    11: "M7 above DCML    (our root = lead-tone of DCML)",
}

def pc_name(pc):
    return PC_NAMES[pc % 12] if pc is not None and pc >= 0 else "?"

def parse_pc_set(bitmap):
    if bitmap is None:
        return set()
    return {i for i in range(12) if bitmap & (1 << i)}

def run(corpus_dir: Path, wir_dir: Path):
    ours_files = sorted(corpus_dir.glob("*.ours.json"))
    print(f"Loaded {len(ours_files)} corpus files")

    cases = []
    processed = 0
    wir_coverage = 0

    for ours_path in ours_files:
        stem = ours_path.stem.replace(".ours", "")
        m21_path = corpus_dir / f"{stem}.music21.json"
        if not m21_path.exists():
            continue
        try:
            _, ours_regions = cmp.load_analysis(ours_path)
            _, m21_regions  = cmp.load_analysis(m21_path)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            print(f"[characterise_bir_false] DROPPED {stem} — load failed "
                  f"({type(exc).__name__}: {exc})", file=sys.stderr)
            continue
        if not ours_regions:
            continue

        wir_regions = []
        try:
            # THE shared WiR loading substrate (applies the OI-142 transposition correction).
            wir_regions = dcml.load_wir_regions(str(wir_dir), stem)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            # OI-140/OI-123 diagnostic-side: name a WiR parse failure (this is the batch diagnostic,
            # not the governing hard stop — a8_rebaseline_measure carries the hard-stop-side surfacing).
            print(f"[characterise_bir_false] {stem}: WiR parse failed "
                  f"({type(exc).__name__}: {exc})", file=sys.stderr)
            wir_regions = []
        if wir_regions:
            wir_coverage += 1

        aligned     = cmp.align_regions(ours_regions, m21_regions)
        wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None]*len(ours_regions)
        processed  += 1

        for i, (our_r, their_r) in enumerate(aligned):
            if cmp.classify(our_r, their_r).category != "chord_disagree":
                continue
            if our_r.bass_is_root:               # only BIR=false residuals
                continue
            if not wir_regions or i >= len(wir_aligned):
                continue
            wir_r  = wir_aligned[i]
            wir_pc = wir_r.root_pc if wir_r is not None else None
            cat    = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
            if cat != "music21_dcml_agree":
                continue

            dcml_root = their_r.root_pc        # equals wir_pc (both agree)
            our_root  = our_r.root_pc
            our_bass  = our_r.bass_pc if our_r.bass_pc is not None else our_root

            # Prompt's convention: delta = our - dcml (positive = above DCML)
            delta = (our_root - dcml_root + 12) % 12

            # DCML root presence in our pc-set / our alts
            pcs_present = parse_pc_set(our_r.pitch_class_set)
            dcml_in_pcs = (dcml_root in pcs_present)
            dcml_in_alts = any(int(alt.get("rootPitchClass", -99)) == dcml_root
                               for alt in (our_r.alternatives or []))

            cases.append({
                "stem":          stem,
                "measure":       our_r.measure_number,
                "beat":          our_r.beat,
                "tick":          our_r.start_tick,
                "our_root":      our_root,
                "our_bass":      our_bass,
                "our_quality":   our_r.quality,
                "our_sym":       our_r.chord_symbol,
                "dcml_root":     dcml_root,
                "dcml_label":    their_r.chord_symbol,
                "wir_label":     wir_r.chord_symbol if wir_r else "",
                "delta":         delta,
                "distinct_pcs": len(pcs_present),
                "pcs_present":   sorted(pcs_present),
                "dcml_in_pcs":   dcml_in_pcs,
                "dcml_in_alts":  dcml_in_alts,
                "key_tonic":     our_r.key,
                "key_conf":      our_r.key_confidence or 0.0,
                "note_count":    our_r.note_count or 0,
                "margin":        our_r.chord_score_margin or 0.0,
                "score":         our_r.chord_score or 0.0,
                "alternatives":  [
                    f"{a.get('chordSymbol','?')}[r={a.get('rootPitchClass','?')},q={a.get('quality','?')}]s={a.get('score',0):.2f}"
                    for a in (our_r.alternatives or [])[:4]
                ],
            })

    n = len(cases)
    print(f"Processed {processed} scores ({wir_coverage} with WiR coverage) -> {n} genuine BIR=false cases")

    # ── Delta-group summary ──────────────────────────────────────────────────
    delta_counts = Counter(c["delta"] for c in cases)
    print("\n══════════════════════════════════════════════════════════════════════")
    print(" Delta = (our_root - dcml_root + 12) % 12  group counts")
    print("══════════════════════════════════════════════════════════════════════")
    print(f"  {'delta':>5}  {'count':>5}   {'interval'}")
    for d in range(12):
        c = delta_counts.get(d, 0)
        if c == 0:
            continue
        bar = "█" * c
        print(f"  +{d:3d}  {c:5d}   {bar} {INTERVAL_NAMES[d]}")

    print(f"\nTOTAL genuine BIR=false: {n}")

    # ── Per-group full case dump ────────────────────────────────────────────
    def dump_group(d, label):
        sub = sorted([c for c in cases if c["delta"] == d], key=lambda c: (c["stem"], c["tick"]))
        print(f"\n══════════════════════════════════════════════════════════════════════")
        print(f" Delta=+{d} subgroup — {label}  ({len(sub)} cases)")
        print("══════════════════════════════════════════════════════════════════════")
        for k, c in enumerate(sub, 1):
            pcs_str = ",".join(pc_name(p) for p in c["pcs_present"])
            alts = " | ".join(c["alternatives"])
            print(f"\n  [{k}] {c['stem']}  m{c['measure']}.b{c['beat']}  tick={c['tick']}")
            print(f"      our  = {c['our_sym']:<14} root={pc_name(c['our_root'])} bass={pc_name(c['our_bass'])} q={c['our_quality']}")
            print(f"      DCML = {c['dcml_label']:<14} root={pc_name(c['dcml_root'])}    WiR={c['wir_label']}")
            print(f"      key  = {c['key_tonic']} (kConf={c['key_conf']:.2f})   noteCount={c['note_count']}  distinctPcs={c['distinct_pcs']}")
            print(f"      pcs  = {{{pcs_str}}}   DCML_root_present={c['dcml_in_pcs']}   DCML_root_in_alts={c['dcml_in_alts']}")
            print(f"      score={c['score']:.2f} margin={c['margin']:.3f}")
            print(f"      alts = {alts}")

    # Order non-zero deltas by count desc
    nonzero_sorted = [d for d, _ in sorted(delta_counts.items(), key=lambda kv: -kv[1]) if d != 0]
    for d in nonzero_sorted[:2]:
        dump_group(d, INTERVAL_NAMES[d])

    # Always dump β and γ explicitly even if not top-2
    for d, lbl in [(5, "β P4 above"), (2, "γ M2 above")]:
        if d not in nonzero_sorted[:2] and delta_counts.get(d, 0) > 0:
            dump_group(d, INTERVAL_NAMES[d])

    # ── Mozart k280 cases ───────────────────────────────────────────────────
    moz = [c for c in cases if "k280" in c["stem"].lower() or "k279" in c["stem"].lower() or "mozart" in c["stem"].lower()]
    print(f"\n══════════════════════════════════════════════════════════════════════")
    print(f" Mozart cases (k279/k280) in BIR=false set: {len(moz)}")
    print("══════════════════════════════════════════════════════════════════════")
    for c in moz:
        print(f"  {c['stem']}  m{c['measure']}.b{c['beat']}  delta=+{c['delta']}  our={c['our_sym']} -> DCML={c['dcml_label']}")
    if not moz:
        print("  (none — Mozart sonatas are not in the Bach Baroque BIR corpus)")

    # ── Compact full enumeration sorted by stem+tick ────────────────────────
    print(f"\n══════════════════════════════════════════════════════════════════════")
    print(f" Full BIR=false enumeration (all {n} cases) sorted by stem,tick")
    print("══════════════════════════════════════════════════════════════════════")
    print(f"  {'#':>3} {'stem':<14} {'m':>3} {'b':>5} {'tick':>6}  {'our':<14} {'DCML':<14} {'Δ':>2}  {'kConf':>5} {'mar':>6}")
    for k, c in enumerate(sorted(cases, key=lambda c: (c["stem"], c["tick"])), 1):
        print(f"  {k:3d} {c['stem']:<14} {c['measure']:3d} {c['beat']:5.2f} {c['tick']:6d}  "
              f"{c['our_sym']:<14} {c['dcml_label']:<14} +{c['delta']:>1}  "
              f"{c['key_conf']:5.2f} {c['margin']:6.3f}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Characterise the genuine BIR=false residuals of a single-preset "
                    "corpus dir (validates the corpus manifest before measuring).")
    parser.add_argument("--corpus-dir", metavar="DIR", default=str(_CORPUS_DIR),
                        help=f"Per-preset corpus dir to measure (default: {_CORPUS_DIR}).")
    parser.add_argument("--wir-dir", metavar="DIR", default=str(_WIR_DIR),
                        help="When-in-Rome (DCML) annotation dir.")
    args = parser.parse_args(argv)

    corpus_dir = Path(args.corpus_dir)
    try:
        manifest = validate_corpus_dir(corpus_dir)
    except CorpusValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
    print(f"Corpus OK: preset={manifest['preset']}  "
          f"{manifest['ours_count']}/{manifest['expected_count']} scores  "
          f"(git {manifest.get('git_hash', '?')})")

    run(corpus_dir, Path(args.wir_dir))


if __name__ == "__main__":
    main()
