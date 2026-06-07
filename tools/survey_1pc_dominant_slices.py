#!/usr/bin/env python3
"""Survey 1-PC degree-5-in-minor slices across the DCML corpora.

For the A2 dominant-quality fix in applyTonicPriorToSparseChord, we need the
keyConfidence distribution for natural-minor regions whose root is the 5th
scale degree and whose distinctPcs == 1, currently emitted as Minor (v) or
Power. The threshold (currently undecided) discriminates between:
  - target promote-to-V cases (e.g. Corelli op01n08d m1 b3, kc=0.9615)
  - regression risk cases   (e.g. Chopin bi105_op30_2 tick 23040, kc=0.6273)

Runs batch_analyze --preset Baroque --dump-regions notation on each score,
caches output under C:/Temp/dominant_survey/<corpus>/. Read-only thereafter.
"""

from __future__ import annotations

import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path("C:/s/MS")
BATCH_ANALYZE = REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe"
DCML_ROOT = REPO_ROOT / "tools" / "dcml"
OUT_ROOT = Path("C:/Temp/dominant_survey")

# (corpus_name, MS3 directory). The 10 DCML corpora + Bach chorales.
CORPORA: list[tuple[str, Path]] = [
    ("corelli",            DCML_ROOT / "corelli"            / "MS3"),
    ("chopin_mazurkas",    DCML_ROOT / "chopin_mazurkas"    / "MS3"),
    ("bach_en_fr_suites",  DCML_ROOT / "bach_en_fr_suites"  / "MS3"),
    ("mozart_piano_sonatas", DCML_ROOT / "mozart_piano_sonatas" / "MS3"),
    ("bach_chorales",      DCML_ROOT / "bach_chorales"      / "MS3"),
    ("ABC",                DCML_ROOT / "ABC"                / "MS3"),
    ("cpe_bach_keyboard",  DCML_ROOT / "cpe_bach_keyboard"  / "MS3"),
    ("grieg_lyric_pieces", DCML_ROOT / "grieg_lyric_pieces" / "MS3"),
    ("schumann_kinderszenen", DCML_ROOT / "schumann_kinderszenen" / "MS3"),
    ("dvorak_silhouettes", DCML_ROOT / "dvorak_silhouettes" / "MS3"),
    ("tchaikovsky_seasons", DCML_ROOT / "tchaikovsky_seasons" / "MS3"),
]

# Key tonic PC lookup. The dump emits keys like "Cmin", "F#min", "Bbmin",
# "Cmel", "Cdor", "Charm". Strip mode suffix, parse "C", "C#", "Bb" etc.
TONIC_PC = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
    "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9,
    "A#": 10, "Bb": 10, "B": 11, "Cb": 11,
}

# Mode parsing. The fix target is natural minor (v -> V). We also collect
# other minor-leaning modes for context (mel, harm, dor) — these are not
# fix targets but help us understand the distribution shape.
MINOR_MODE_SUFFIXES = {"min", "mel", "harm", "dor", "aeo", "phr"}
NATURAL_MINOR_SUFFIX = "min"


def parse_key(key: str) -> tuple[int | None, str | None]:
    """Return (tonic_pc, mode_suffix) for a dump key string like 'Cmin' or 'F#mel'."""
    m = re.match(r"^([A-G][#b]?)(.+)$", key or "")
    if not m:
        return None, None
    tonic_name, mode = m.group(1), m.group(2).lower()
    return TONIC_PC.get(tonic_name), mode


def output_path_for(corpus: str, score_path: Path) -> Path:
    return OUT_ROOT / corpus / (score_path.stem + ".json")


def need_dump(corpus: str, score_path: Path) -> bool:
    out = output_path_for(corpus, score_path)
    if not out.exists():
        return True
    # Tolerate non-empty existing files; rerun if obviously empty.
    return out.stat().st_size < 100


def run_one(corpus: str, score_path: Path, timeout_s: int = 120) -> tuple[Path, int, str]:
    """Invoke batch_analyze once. Returns (out_path, exit_code, message)."""
    out = output_path_for(corpus, score_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(BATCH_ANALYZE),
        str(score_path),
        str(out),
        "--preset", "Baroque",
        "--dump-regions", "notation",
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
        if r.returncode != 0:
            return out, r.returncode, f"exit={r.returncode}: {r.stderr[:200]}"
        return out, 0, "ok"
    except subprocess.TimeoutExpired:
        return out, -1, "timeout"
    except Exception as e:  # noqa: BLE001
        return out, -2, f"error: {e}"


def discover_scores(corpus: str, ms3_dir: Path) -> list[Path]:
    if not ms3_dir.exists():
        return []
    return sorted(ms3_dir.glob("*.mscx"))


def beat_for_tick(tick: int, ticks_per_quarter: int = 480) -> str:
    """Crude beat label using tick / 480. Returns 'tick=N' as suffix only."""
    q = tick // ticks_per_quarter
    return f"q{q}"


def match_region(r: dict) -> bool:
    """1-PC, root=degree-5, minor-mode current quality, in a minor key."""
    if r.get("noteCount", 0) < 1:
        return False
    pcs_count = bin(r.get("pitchClassSet", 0)).count("1")
    if pcs_count != 1:
        return False
    # Current quality is Minor (natural-minor v) or Power (1-PC sparse).
    q = r.get("quality")
    if q not in ("Minor", "Power"):
        return False
    tonic_pc, mode = parse_key(r.get("key", ""))
    if tonic_pc is None or mode is None:
        return False
    if mode not in MINOR_MODE_SUFFIXES:
        return False
    root_pc = r.get("rootPitchClass")
    if root_pc is None:
        return False
    if (root_pc - tonic_pc) % 12 != 7:
        return False
    return True


def analyze_dump(corpus: str, score_stem: str, dump_path: Path) -> list[dict]:
    """Parse one dump JSON, return matching region records."""
    try:
        with open(dump_path) as f:
            d = json.load(f)
    except Exception as e:  # noqa: BLE001
        sys.stderr.write(f"[warn] {dump_path}: {e}\n")
        return []
    out = []
    for r in d.get("regions", []):
        if not match_region(r):
            continue
        tonic_pc, mode = parse_key(r.get("key", ""))
        out.append({
            "corpus": corpus,
            "score": score_stem,
            "measure": r.get("measureNumber"),
            "beat": r.get("beat"),
            "tick": r.get("startTick"),
            "keyConfidence": r.get("keyConfidence"),
            "quality": r.get("quality"),
            "roman": r.get("romanNumeral"),
            "rootPc": r.get("rootPitchClass"),
            "key": r.get("key"),
            "mode": mode,
            "noteCount": r.get("noteCount"),
            "pitchClassSet": r.get("pitchClassSet"),
        })
    return out


def run_phase(workers: int = 8) -> None:
    """Phase 1: ensure all dumps exist, running batch_analyze in parallel."""
    tasks: list[tuple[str, Path]] = []
    for corpus, ms3 in CORPORA:
        scores = discover_scores(corpus, ms3)
        if not scores:
            print(f"[skip] {corpus}: no scores at {ms3}", flush=True)
            continue
        missing = [s for s in scores if need_dump(corpus, s)]
        print(f"[corpus] {corpus}: {len(scores)} total, {len(missing)} need dump", flush=True)
        for s in missing:
            tasks.append((corpus, s))

    if not tasks:
        print("[run] all dumps present, skipping batch_analyze phase", flush=True)
        return

    print(f"[run] launching {len(tasks)} batch_analyze jobs (workers={workers})", flush=True)
    t0 = time.time()
    done = 0
    failed = []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, c, s): (c, s) for c, s in tasks}
        for fut in cf.as_completed(futs):
            c, s = futs[fut]
            _, code, msg = fut.result()
            done += 1
            if code != 0:
                failed.append((c, s.name, msg))
            if done % 25 == 0 or done == len(tasks):
                el = time.time() - t0
                print(f"  [{done}/{len(tasks)}] {el:.1f}s elapsed ({len(failed)} failed)", flush=True)
    if failed:
        print(f"[run] {len(failed)} failures:", flush=True)
        for c, n, m in failed[:20]:
            print(f"    {c}/{n}: {m}", flush=True)


def analyze_phase() -> list[dict]:
    """Phase 2: parse all dumps and find matching regions."""
    matches: list[dict] = []
    counts_per_corpus: dict[str, int] = {}
    for corpus, ms3 in CORPORA:
        scores = discover_scores(corpus, ms3)
        n = 0
        for s in scores:
            dump = output_path_for(corpus, s)
            if not dump.exists() or dump.stat().st_size < 100:
                continue
            recs = analyze_dump(corpus, s.stem, dump)
            matches.extend(recs)
            n += len(recs)
        counts_per_corpus[corpus] = n
    print()
    print("=" * 70)
    print("MATCHES PER CORPUS (1-PC, degree-5 root, minor-mode key, quality Minor or Power)")
    print("=" * 70)
    for c in counts_per_corpus:
        print(f"  {c:30s} {counts_per_corpus[c]:5d}")
    print(f"  {'TOTAL':30s} {sum(counts_per_corpus.values()):5d}")
    print()
    return matches


def print_table(matches: list[dict]) -> None:
    matches_sorted = sorted(matches, key=lambda r: -r["keyConfidence"])
    print("=" * 110)
    print("SORTED TABLE — by keyConfidence descending")
    print("=" * 110)
    hdr = f"{'kc':>7}  {'corpus':22} {'score':28} {'m.b':>6} {'tick':>6}  {'key':8} {'q':9} {'rn':>6}"
    print(hdr)
    print("-" * len(hdr))
    for r in matches_sorted:
        mb = f"{r['measure']}.{r['beat']}"
        print(f"{r['keyConfidence']:7.4f}  {r['corpus']:22} {r['score'][:28]:28} {mb:>6} {r['tick']:>6}  "
              f"{r['key']:8} {r['quality']:9} {r['roman'] or '-':>6}")
    print()


def print_histogram(matches: list[dict]) -> None:
    print("=" * 70)
    print("keyConfidence HISTOGRAM (bucket width 0.05)")
    print("=" * 70)
    n = len(matches)
    if n == 0:
        print("(no matches)")
        return
    buckets: dict[int, int] = {}
    for r in matches:
        kc = r["keyConfidence"]
        b = min(int(kc / 0.05), 19)  # 0..19, top bucket = [0.95, 1.00]
        buckets[b] = buckets.get(b, 0) + 1
    # Print high-to-low
    print(f"  bucket           count   bar")
    for b in range(19, -1, -1):
        lo = b * 0.05
        hi = lo + 0.05
        c = buckets.get(b, 0)
        bar = "#" * c
        marker = " <-- ANCHORS HERE" if (b == 19) else (
            " <-- regression case here" if (b == 12) else ""
        )
        # 0.6273 is in bucket 12 (0.60-0.65). 0.9615 is in bucket 19 (0.95-1.00).
        print(f"  [{lo:0.2f},{hi:0.2f})    {c:4d}   {bar}{marker}")
    print(f"  total            {n:4d}")
    print()


def main() -> int:
    if not BATCH_ANALYZE.exists():
        print(f"FATAL: batch_analyze not found at {BATCH_ANALYZE}", file=sys.stderr)
        return 1
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    print(f"[init] OUT_ROOT={OUT_ROOT}")
    print(f"[init] BATCH_ANALYZE={BATCH_ANALYZE}")
    print(f"[init] preset=Baroque, dump-regions=notation")
    print()
    run_phase(workers=8)
    matches = analyze_phase()
    print_table(matches)
    print_histogram(matches)
    return 0


if __name__ == "__main__":
    sys.exit(main())
