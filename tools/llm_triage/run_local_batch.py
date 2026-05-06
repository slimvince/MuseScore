#!/usr/bin/env python3
# Python interpreter: C:\s\MS\.venv\Scripts\python.exe
"""run_local_batch.py — Run llm_triage binary on all scores without LLM calls.

Score sources (all included by default):
  extra scores/              163 user-curated .mscz (flat scan, not registry-only)
    hiromi/                    20 Hiromi Uehara scores
    Steely dan/                23 Steely Dan scores
    piazzolla/                  6 Piazzolla scores
    (root)                    114 jazz / pop / bossa nova mix
  tools/dcml/*/MS3/          DCML classical corpora (11 subcorpora, ~952 .mscx)
  tools/dcml/ABC/             71 Beethoven SQ .mscx
  tools/dcml/when_in_rome/  1174 .mxl (When-in-Rome anthology — flat basename collision
                                       → each score gets its own output sub-dir)
  tools/corpus_effendi_src/  368 Real Book .xml
  tools/corpus_omnibook_src/ omnibook_xml/  50 Charlie Parker .xml/.mxl
  tools/corpus_rampageswing_full/  36 big-band .mxl/.xml
  tools/pdmx/spot_check/       5 PDMX random-sample .mxl
  tools/corpus/*.xml          353 music21 Bach chorale exports

Produces per score:
  <basename>.analyzer_response.json
  <basename>.chordIdentifierPopJazz_response.json
  <basename>.triage_queue.md / .json   (with --compare)

For When-in-Rome scores each gets its own sub-directory under
  <output-dir>/when_in_rome/<relative-path-from-Corpus/>/
because every file is named score.mxl.

Usage:
  python run_local_batch.py [options]

Options:
  --output-dir   DIR    Where to write output files (default: <worktree>/outputs/)
  --binary       PATH   Path to llm_triage.exe (default: auto-detected)
  --no-dcml             Skip DCML classical corpora
  --no-when-in-rome     Skip When-in-Rome anthology (large, 1174 scores)
  --no-jazz             Skip jazz corpora (effendi, omnibook, rampageswing, pdmx)
  --no-bach             Skip music21 Bach corpus (overlaps with dcml/bach_chorales)
  --compare             Run compare_triage.py after each score
  --force               Re-run even if output files already exist
  --dry-run             Print what would be done without running anything
  --limit        N      Stop after N scores (0 = no limit)
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

# Force UTF-8 output on Windows so score names with non-ASCII characters
# (e.g. "água", "Esbjörn") don't cause UnicodeEncodeError when printing.
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_WORKTREE       = Path(__file__).resolve().parents[2]
_MS_ROOT        = Path(r"C:\s\MS")
_BINARY_DEFAULT = _WORKTREE / "ninja_build_llm_triage" / "llm_triage.exe"
_COMPARE_PY     = Path(__file__).resolve().parent / "compare_triage.py"
_PYTHON         = sys.executable


# ---------------------------------------------------------------------------
# Score entry: path + the output dir to use for this specific score
# ---------------------------------------------------------------------------

class ScoreEntry:
    __slots__ = ("path", "output_dir")
    def __init__(self, path: Path, output_dir: Path):
        self.path = path
        self.output_dir = output_dir


# ---------------------------------------------------------------------------
# Corpus loaders
# ---------------------------------------------------------------------------

def _entries(paths: list[Path], output_dir: Path) -> list[ScoreEntry]:
    return [ScoreEntry(p, output_dir) for p in paths]


def load_extra_scores(output_dir: Path) -> list[ScoreEntry]:
    """All .mscz files under tools/extra scores/ (flat directory scan)."""
    root = _MS_ROOT / "tools" / "extra scores"
    if not root.exists():
        return []
    return _entries(sorted(root.rglob("*.mscz")), output_dir)


def load_dcml_paths(output_dir: Path) -> list[ScoreEntry]:
    """MSCX/MSCZ scores from all DCML classical subcorpora (MS3/ folders + ABC root)."""
    dcml = _MS_ROOT / "tools" / "dcml"
    if not dcml.exists():
        print(f"Warning: DCML directory not found: {dcml}", file=sys.stderr)
        return []
    entries: list[ScoreEntry] = []
    for subdir in sorted(dcml.iterdir()):
        if not subdir.is_dir() or subdir.name == "when_in_rome":
            continue
        if subdir.name == "ABC":
            # ABC uses MS3/ like all other DCML corpora (no root-level scores)
            ms3 = subdir / "MS3"
            if ms3.is_dir():
                for p in sorted(ms3.glob("*.mscx")) + sorted(ms3.glob("*.mscz")):
                    entries.append(ScoreEntry(p, output_dir))
            continue
        ms3 = subdir / "MS3"
        if ms3.is_dir():
            for p in sorted(ms3.glob("*.mscx")) + sorted(ms3.glob("*.mscz")):
                entries.append(ScoreEntry(p, output_dir))
    return entries


def load_when_in_rome(base_output_dir: Path) -> list[ScoreEntry]:
    """When-in-Rome anthology: each score.mxl lives in its own sub-directory.

    To avoid basename collisions (every file is named 'score'), each score
    gets its own output sub-directory mirroring its position under Corpus/.
    """
    wir = _MS_ROOT / "tools" / "dcml" / "when_in_rome" / "Corpus"
    if not wir.exists():
        wir = _MS_ROOT / "tools" / "dcml" / "when_in_rome"
        if not wir.exists():
            return []
    entries: list[ScoreEntry] = []
    for score_file in sorted(wir.rglob("*.mxl")):
        # Mirror the directory structure under base_output_dir/when_in_rome/
        rel = score_file.parent.relative_to(wir.parent)
        out = base_output_dir / rel
        entries.append(ScoreEntry(score_file, out))
    # Also pick up any .xml or .musicxml score files in when_in_rome
    for score_file in sorted(wir.rglob("*.xml")):
        if score_file.stem == "score" or not any(score_file.stem == e.path.stem
                                                  for e in entries
                                                  if e.path.parent == score_file.parent):
            rel = score_file.parent.relative_to(wir.parent)
            out = base_output_dir / rel
            entries.append(ScoreEntry(score_file, out))
    return entries


def load_effendi(output_dir: Path) -> list[ScoreEntry]:
    d = _MS_ROOT / "tools" / "corpus_effendi_src"
    if not d.exists():
        return []
    return _entries(sorted(d.glob("*.xml")) + sorted(d.glob("*.mxl")) +
                    sorted(d.glob("*.musicxml")), output_dir)


def load_omnibook(output_dir: Path) -> list[ScoreEntry]:
    # Scores live in a nested subfolder "Omnibook xml/" (with a space)
    d = _MS_ROOT / "tools" / "corpus_omnibook_src" / "omnibook_xml" / "Omnibook xml"
    if not d.exists():
        # Fallback: rglob from the parent to handle any layout
        d = _MS_ROOT / "tools" / "corpus_omnibook_src"
        if not d.exists():
            return []
        paths = sorted(d.rglob("*.xml")) + sorted(d.rglob("*.mxl")) + \
                sorted(d.rglob("*.musicxml"))
        return _entries([p for p in paths if "__MACOSX" not in p.parts], output_dir)
    return _entries(sorted(d.glob("*.xml")) + sorted(d.glob("*.mxl")) +
                    sorted(d.glob("*.musicxml")), output_dir)


def load_rampageswing(output_dir: Path) -> list[ScoreEntry]:
    d = _MS_ROOT / "tools" / "corpus_rampageswing_full"
    if not d.exists():
        return []
    return _entries(sorted(d.glob("*.xml")) + sorted(d.glob("*.mxl")) +
                    sorted(d.glob("*.musicxml")), output_dir)


def load_pdmx(output_dir: Path) -> list[ScoreEntry]:
    d = _MS_ROOT / "tools" / "pdmx" / "spot_check"
    if not d.exists():
        return []
    return _entries(sorted(d.glob("*.mxl")) + sorted(d.glob("*.xml")) +
                    sorted(d.glob("*.musicxml")), output_dir)


def load_bach_corpus(output_dir: Path) -> list[ScoreEntry]:
    """music21 Bach chorale exports — overlaps with dcml/bach_chorales/MS3/."""
    corpus = _MS_ROOT / "tools" / "corpus"
    if not corpus.exists():
        return []
    return _entries(sorted(corpus.glob("*.xml")), output_dir)


# ---------------------------------------------------------------------------
# Skip logic
# ---------------------------------------------------------------------------

def already_processed(basename: str, output_dir: Path) -> bool:
    return (
        (output_dir / f"{basename}.analyzer_response.json").exists()
        and (output_dir / f"{basename}.chordIdentifierPopJazz_response.json").exists()
    )


# ---------------------------------------------------------------------------
# Per-score runner
# ---------------------------------------------------------------------------

def run_binary(score_path: Path, output_dir: Path, binary: Path) -> tuple[bool, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            [str(binary), str(score_path), str(output_dir)],
            check=False,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        return False, "timeout after 300s"

    if result.returncode != 0:
        err = (result.stderr or result.stdout or "").strip()
        return False, f"exit {result.returncode}: {err[:200]}"

    regions = _extract_count(result.stdout, "regions:")
    plugin  = _extract_count(result.stdout, "plugin regions:")
    return True, f"regions={regions}  plugin_regions={plugin}"


def _extract_count(text: str | None, label: str) -> str:
    if not text:
        return "?"
    for line in text.splitlines():
        if label in line:
            parts = line.split(label)
            if len(parts) > 1:
                return parts[1].strip().split()[0]
    return "?"


def run_compare(basename: str, output_dir: Path) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            [_PYTHON, str(_COMPARE_PY), basename, str(output_dir)],
            check=False,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        return False, "compare timeout after 60s"

    if result.returncode != 0:
        err = (result.stderr or result.stdout or "").strip()
        return False, f"compare exit {result.returncode}: {err[:200]}"

    return True, (result.stdout or "").strip() or "ok"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run llm_triage binary on all corpus scores (no LLM calls)."
    )
    parser.add_argument("--output-dir", default=str(_WORKTREE / "outputs"))
    parser.add_argument("--binary", default=str(_BINARY_DEFAULT))
    parser.add_argument("--no-dcml", action="store_true",
                        help="Skip DCML classical corpora (~952 scores)")
    parser.add_argument("--no-when-in-rome", action="store_true",
                        help="Skip When-in-Rome anthology (1174 scores)")
    parser.add_argument("--no-jazz", action="store_true",
                        help="Skip jazz corpora (effendi/omnibook/rampageswing/pdmx)")
    parser.add_argument("--no-bach", action="store_true",
                        help="Skip music21 Bach corpus (overlaps dcml/bach_chorales)")
    parser.add_argument("--compare", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    binary = Path(args.binary)
    if not args.dry_run and not binary.exists():
        sys.exit(f"Error: llm_triage binary not found: {binary}")

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Build score list.
    scores: list[ScoreEntry] = []
    scores += load_extra_scores(out)
    if not args.no_dcml:
        scores += load_dcml_paths(out)
    if not args.no_when_in_rome:
        scores += load_when_in_rome(out)
    if not args.no_jazz:
        scores += load_effendi(out)
        scores += load_omnibook(out)
        scores += load_rampageswing(out)
        scores += load_pdmx(out)
    if not args.no_bach:
        scores += load_bach_corpus(out)

    total = len(scores)
    counts = {
        "extra_scores": len(load_extra_scores(out)),
        "dcml": 0 if args.no_dcml else len(load_dcml_paths(out)),
        "when_in_rome": 0 if args.no_when_in_rome else len(load_when_in_rome(out)),
        "jazz": 0 if args.no_jazz else (
            len(load_effendi(out)) + len(load_omnibook(out)) +
            len(load_rampageswing(out)) + len(load_pdmx(out))
        ),
        "bach_corpus": 0 if args.no_bach else len(load_bach_corpus(out)),
    }

    print(f"Batch run: {total} scores")
    print(f"  extra_scores={counts['extra_scores']}  dcml={counts['dcml']}  "
          f"when_in_rome={counts['when_in_rome']}  jazz={counts['jazz']}  "
          f"bach_corpus={counts['bach_corpus']}")
    print(f"  output={out}  binary={binary}")
    if args.dry_run:
        print("DRY-RUN — no commands will be executed.\n")

    skipped = ok = failed = processed = 0
    t_start = time.monotonic()

    for i, entry in enumerate(scores, 1):
        basename = entry.path.stem
        prefix = f"[{i}/{total}]"

        if not entry.path.exists():
            print(f"{prefix} MISSING  {entry.path.name}")
            failed += 1
            continue

        if not args.force and already_processed(basename, entry.output_dir):
            skipped += 1
            continue

        if args.dry_run:
            print(f"{prefix} WOULD RUN  {entry.path.name}  -> {entry.output_dir}")
            processed += 1
            if args.limit and processed >= args.limit:
                break
            continue

        success, msg = run_binary(entry.path, entry.output_dir, binary)
        if success:
            print(f"{prefix} OK       {basename}  {msg}")
            ok += 1
        else:
            print(f"{prefix} FAILED   {basename}  {msg}")
            failed += 1

        if success and args.compare:
            cok, cmsg = run_compare(basename, entry.output_dir)
            status = "COMPARE_OK" if cok else "COMPARE_FAIL"
            print(f"         {status}  {cmsg}")

        processed += 1
        if args.limit and processed >= args.limit:
            print(f"\nReached --limit {args.limit}; stopping early.")
            break

    elapsed = time.monotonic() - t_start
    print(
        f"\nDone in {elapsed:.1f}s  "
        f"ok={ok}  skipped={skipped}  failed={failed}  "
        f"total_seen={ok + skipped + failed}"
    )
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
