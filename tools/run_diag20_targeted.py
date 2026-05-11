#!/usr/bin/env python3
"""
run_diag20_targeted.py — Run batch_analyze on only the 19 chorales that have
Cat 2 Minor→HalfDim mismatches, capturing DIAG20 stderr to diag20_raw.txt.

Much faster than a full corpus run: ~19 chorales instead of 353.

Usage:
    cd C:\s\MS && python tools/run_diag20_targeted.py
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT   = Path(__file__).resolve().parent.parent
_CORPUS = _ROOT / "tools" / "corpus"
_EXE    = _ROOT / "ninja_build_rel" / "batch_analyze.exe"
_DIAG   = _ROOT / "tools" / "diag20_raw.txt"
_PRESET = "Baroque"

# Unique stems from the 24 Cat 2 MHD cases
TARGET_STEMS = [
    "bwv11.6",
    "bwv254",
    "bwv26.6",
    "bwv268",
    "bwv291",
    "bwv295",
    "bwv301",
    "bwv327",
    "bwv334",
    "bwv350",
    "bwv381",
    "bwv391",
    "bwv397",
    "bwv40.3",
    "bwv40.8",
    "bwv407",
    "bwv424",
    "bwv425",
    "bwv46.6",
    "bwv48.7",
    "bwv64.8",
]


def _to_unix(p: Path) -> str:
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')


def _find_git_bash() -> Path | None:
    return next((p for p in [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ] if p.exists()), None)


def main():
    if not _EXE.exists():
        print(f"ERROR: {_EXE} not found. Build first.", file=sys.stderr)
        sys.exit(1)

    bash = _find_git_bash()
    if bash is None:
        print("ERROR: Git Bash not found.", file=sys.stderr)
        sys.exit(1)

    # Truncate diagnostic file at start
    _DIAG.write_text("", encoding='utf-8')

    ok_count = 0
    fail_count = 0

    with tempfile.TemporaryDirectory() as tmp:
        tmp_out = Path(tmp) / "out.json"

        with _DIAG.open('a', encoding='utf-8') as diag_fh:
            for stem in TARGET_STEMS:
                xml_path = _CORPUS / f"{stem}.xml"
                if not xml_path.exists():
                    print(f"  SKIP {stem}  (no XML file)")
                    continue

                diag_fh.write(f"[PROCESSING] {stem}\n")
                diag_fh.flush()

                cmd = (f'{_to_unix(_EXE)} "{_to_unix(xml_path)}"'
                       f' "{_to_unix(tmp_out)}" --preset {_PRESET}')
                try:
                    r = subprocess.run(
                        [str(bash), '-c', cmd],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.PIPE,
                        timeout=120,
                    )
                    if r.stderr:
                        diag_fh.write(r.stderr.decode('utf-8', 'replace'))
                        diag_fh.flush()
                    if r.returncode == 0:
                        print(f"  OK   {stem}")
                        ok_count += 1
                    else:
                        print(f"  FAIL {stem}  (exit {r.returncode})")
                        fail_count += 1
                except subprocess.TimeoutExpired:
                    print(f"  TIMEOUT {stem}")
                    fail_count += 1
                except Exception as exc:
                    print(f"  ERROR {stem}: {exc}")
                    fail_count += 1

    print(f"\nDone: {ok_count} OK, {fail_count} failed.")
    print(f"Diagnostic output: {_DIAG}")

    diag_lines = sum(1 for l in _DIAG.read_text(encoding='utf-8').splitlines()
                     if '[DIAG20-' in l)
    print(f"DIAG20 lines captured: {diag_lines}")


if __name__ == "__main__":
    main()
