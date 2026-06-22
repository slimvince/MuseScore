#!/usr/bin/env python3
"""Layer-3 key/mode DECODER corpus driver (DIAGNOSTIC, read-only).

Runs the isolated Layer-3 key/mode sequence decoder (`batch_analyze
--decode-keymode --preset <P>`) over the canonical 353-stem music21 Bach-chorale
corpus (`tools/corpus/*.xml`) and writes the decoder's per-slice key/mode to
`<out>/<preset>/<stem>.decode.json` — the same region shape the held-out
ground-truth harness (`cc_layer3_keymode_baseline.py`) reads from `*.ours.json`.

`--decode-keymode` returns BEFORE any analysis runs (the analysis pipeline is
never invoked), so this is read-only: production analysis output is unchanged and
the decoder is NOT wired into the live analyzer. This driver only iterates the
corpus, invokes the diagnostic, and collects its per-stem JSON.

On Windows, batch_analyze MUST be launched via Git Bash (a direct Python
subprocess of the Qt headless exe triggers an access violation) — mirrors
run_bach_preset.py / validate_slices_corpus.py.

Usage:
    python tools/decode_keymode_corpus.py --preset Baroque --out tools/corpus_decode
    python tools/decode_keymode_corpus.py --preset Jazz    --out tools/corpus_decode

Then grade with:
    python tools/cc_layer3_keymode_baseline.py --decode-dir tools/corpus_decode
"""
import argparse
import json
import platform
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent


def _find_batch_analyze(hint):
    candidates = ([Path(hint)] if hint else []) + [
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze",
        _REPO_ROOT / "ninja_build" / "batch_analyze",
    ]
    return next((p for p in candidates if p.exists()), None)


def _find_git_bash():
    return next((p for p in [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ] if p.exists()), None)


def _to_unix_path(p):
    s = str(Path(p).resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')


def _run_one(exe, xml_path, preset, extra_args=""):
    """Run batch_analyze --decode-keymode on one stem; return (rc, parsed_json_or_None, err).

    extra_args (BOUNDED L3 SWEEP): an optional string of decode-only
    KeyModeSequencePreferences overrides (e.g. "--seq-change-base 1.5"). Read only on
    the --decode-keymode path, so production stays byte-identical."""
    try:
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = (f'{_to_unix_path(exe)} "{_to_unix_path(xml_path)}" '
                       f'--decode-keymode --preset {preset} {extra_args}'.rstrip())
                r = subprocess.run([str(bash), '-c', cmd],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=300)
            else:
                r = subprocess.run([str(exe), str(xml_path), '--decode-keymode',
                                    '--preset', preset] + extra_args.split(),
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=300)
        else:
            r = subprocess.run([str(exe), str(xml_path), '--decode-keymode',
                                '--preset', preset] + extra_args.split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               timeout=300)
        out = r.stdout.decode('utf-8', 'replace').strip()
        parsed = None
        if out:
            try:
                parsed = json.loads(out)
            except Exception as e:
                return (r.returncode, None,
                        f"unparseable JSON: {e}; raw[:200]={out[:200]!r}")
        return (r.returncode, parsed, r.stderr.decode('utf-8', 'replace').strip())
    except subprocess.TimeoutExpired:
        return (-1, None, "timeout")
    except Exception as e:
        return (-1, None, f"exception: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-analyze", default=None)
    ap.add_argument("--corpus-dir", default=str(_REPO_ROOT / "tools" / "corpus"),
                    help="dir of *.xml input stems (the canonical 353 chorales)")
    ap.add_argument("--preset", required=True, help="Baroque | Jazz | Default | ...")
    ap.add_argument("--out", default=str(_REPO_ROOT / "tools" / "corpus_decode"),
                    help="output root; per-stem JSON goes to <out>/<preset>/<stem>.decode.json")
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--extra-args", default="",
                    help="BOUNDED L3 SWEEP: extra decode-only flags passed verbatim to "
                         "batch_analyze (e.g. '--seq-change-base 1.5'). Decode-path only.")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    exe = _find_batch_analyze(args.batch_analyze)
    if not exe:
        print("ERROR: batch_analyze not found.", file=sys.stderr)
        sys.exit(1)
    print(f"Using batch_analyze: {exe}")

    corpus = Path(args.corpus_dir)
    stems = sorted(corpus.glob("*.xml"))
    print(f"Corpus: {corpus}  ({len(stems)} stems)  preset={args.preset}")
    if not stems:
        print("ERROR: no *.xml stems found in corpus dir.", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(args.out) / args.preset.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    failures = []

    if args.extra_args:
        print(f"Decode overrides (decode-path only): {args.extra_args}")

    def work(xml):
        rc, parsed, err = _run_one(exe, xml, args.preset, args.extra_args)
        return (xml.stem, rc, parsed, err)

    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for i, (stem, rc, parsed, err) in enumerate(ex.map(work, stems), 1):
            if parsed is None:
                failures.append((stem, rc, err))
            else:
                (out_dir / f"{stem}.decode.json").write_text(
                    json.dumps(parsed, indent=2), encoding="utf-8")
                written += 1
            if i % 50 == 0:
                print(f"  ... {i}/{len(stems)}")

    print("\n" + "=" * 70)
    print(f"Decoder JSON written: {written}/{len(stems)}  ->  {out_dir}")
    if failures:
        print(f"\n!! {len(failures)} stem(s) failed:")
        for stem, rc, err in failures[:20]:
            print(f"   {stem}: rc={rc} {err[:160]}")
    sys.exit(0 if written == len(stems) else 1)


if __name__ == "__main__":
    main()
