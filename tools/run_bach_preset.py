#!/usr/bin/env python3
"""
run_bach_preset.py — Run Bach chorale corpus with a specific preset and compare
against existing music21.json files (which serve as ground truth).

Usage:
    python tools/run_bach_preset.py [OPTIONS]
    --preset NAME         Preset name (Standard, Baroque, Modal, Jazz, Contemporary)
    --batch-analyze PATH  Path to batch_analyze executable
    --corpus-dir DIR      Directory containing *.xml and *.music21.json (default: tools/corpus)
    --output-dir DIR      Where to write *.ours.json output (default: tools/corpus_<preset>)
    --skip-cpp            Skip batch_analyze, re-use existing .ours.json files
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import io
import json
import multiprocessing
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import compare_analyses as cmp

_REPO_ROOT = Path(__file__).resolve().parent.parent

# Stage 2.2a — every corpus output dir carries a manifest stamping the preset and
# a per-score fingerprint, so a metric script can refuse to measure a contaminated
# or incomplete corpus. Kept in sync with characterise_bir_false.MANIFEST_NAME.
MANIFEST_NAME = "corpus_manifest.json"

# Accepted --preset names. The first five are the batch tuning presets
# (mode priors + ChordAnalyzerPreferences). "Default" (Stage 2.4 V4) is NOT a
# tuning preset: it reproduces the live product's out-of-box configuration —
# the app's registered mode-prior settings defaults (composingconfiguration.cpp,
# which differ from the "Standard" preset on 11 of 21 modes) plus untouched
# ChordAnalyzerPreferences struct defaults. It exists so the configuration users
# actually run can be corpus-measured (informational; no gate). Kept in sync with
# batch_analyze.cpp applyPreset()/chordPrefs handling.
PRESET_CHOICES = ["Standard", "Baroque", "Modal", "Jazz", "Contemporary", "Default"]

# ── THE INFERENCE ARM (OPEN_ITEMS.md OI-307) ─────────────────────────────────────────────
# batch_analyze produces the same .ours.json SHAPE from either of two pipelines: the joint
# estimator (--joint-inference; the production inference layer on the batch/corpus surface,
# CLAUDE.md gate block (A)) or the legacy analyzeScore path. The flag is opt-in —
# jointInferenceDir is initialised empty at tools/batch_analyze.cpp:4917 and the joint path
# runs only under `if (!jointInferenceDir.empty())` at :5590 — so ONE binary produces either
# arm depending on how it was invoked.
#
# Until 2026-08-03 this manifest stamped the BINARY (path/size/mtime) and not its invocation,
# so two corpora produced by different pipelines were indistinguishable in the record. That
# matters here and not somewhere harmless: tools/corpus/<preset> is the directory
# tools/a8_rebaseline_measure.py reads for the block-(A) hard stop, and this script
# clean-slates its output directory before regenerating.
#
# The arm is recorded TWICE, because the two answer different questions:
#   requested — what the INVOCATION asked for (intent, from the flag actually passed);
#   observed  — what the produced files SAY (fact). Both writers stamp "analysisPath":
#               batch_analyze.cpp:4695 writes "joint", the standard writer at :1448 writes
#               "batch". Verifying at the object rather than at the assertion is #15, and it
#               is what lets a disagreement between the two be DETECTED rather than assumed
#               impossible.
ARM_JOINT = "joint"
ARM_LEGACY = "legacy"
ARM_MIXED = "mixed"
ARM_UNKNOWN = "unknown"

# The manifest schema that carries the arm. A manifest below it cannot be read as if it did.
MANIFEST_SCHEMA = 2

# analysisPath is the 4th line of every .ours.json; 4 KiB is far past it and bounds the scan.
_ANALYSIS_PATH_RE = re.compile(rb'"analysisPath"\s*:\s*"([^"]*)"')

# The two analysisPath values a CORPUS can legitimately carry. Any other value (the
# --dump-* diagnostics write "fullspine", "fanout", "joint-probe", ... ; the notation dump
# writes "notation") is not a corpus arm and is reported as itself rather than mapped.
_ARM_BY_ANALYSIS_PATH = {"joint": ARM_JOINT, "batch": ARM_LEGACY}


def _analysis_path_of(data: bytes) -> str | None:
    """The analysisPath value a .ours.json stamps on itself, or None if it carries none."""
    m = _ANALYSIS_PATH_RE.search(data[:4096])
    return m.group(1).decode("utf-8", "replace") if m else None


def _observed_arm(analysis_path_values: dict) -> str:
    """The arm the PRODUCED FILES say they came from.

    analysis_path_values maps each distinct analysisPath value seen (None for a file that
    carries none) to its count. More than one distinct value means the directory does not
    hold the output of a single run — reported as MIXED rather than resolved by majority,
    because a majority reading would hide exactly the contamination this field exists to
    catch.
    """
    if not analysis_path_values:
        return ARM_UNKNOWN
    if len(analysis_path_values) > 1:
        return ARM_MIXED
    only = next(iter(analysis_path_values))
    return _ARM_BY_ANALYSIS_PATH.get(only, ARM_UNKNOWN)


def _file_fingerprint(path: Path, data: bytes | None = None) -> dict:
    """Size + sha256 of a file's bytes — the per-score identity recorded in the
    manifest and re-checked by characterise_bir_false at measurement time.

    `data` lets a caller that has already read the bytes pass them in rather than read the
    file twice; None keeps the historical single-argument behaviour."""
    if data is None:
        data = path.read_bytes()
    return {"size": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def _detect_music21_version(corpus_dir: Path) -> str | None:
    """Best-effort provenance copy-through (corpus audit C2): the *.xml inputs are
    music21 exports and embed `<software>music21 v.X.Y.Z</software>`. Read it from
    the first source score so the manifest records which music21 produced the
    ground-truth `.music21.json`. Purely informational — validate_corpus_dir does
    NOT enforce it; a None just means the version could not be read."""
    for xml in sorted(corpus_dir.glob("*.xml")):
        try:
            head = xml.read_text(encoding="utf-8", errors="replace")[:4000]
        except Exception:
            continue
        m = re.search(r"<software>\s*music21\s*v\.?\s*([0-9][0-9.a-zA-Z]*)\s*</software>", head)
        if m:
            return m.group(1)
    return None


def _write_manifest(out_dir: Path, preset: str, score_status: dict,
                    expected_count: int, git_hash: str, timestamp: str,
                    exe: Path | None, music21_version: str | None = None,
                    requested_arm: str | None = None,
                    joint_inference_dir: str | None = None) -> dict:
    """Write corpus_manifest.json into out_dir and return it.

    score_status maps stem -> status string ('OK', 'FAILED', ...). For every 'OK'
    score the matching {stem}.ours.json must exist in out_dir; its fingerprint is
    recorded. The corpus is 'complete' iff every expected score is 'OK' and the OK
    count equals expected_count.

    requested_arm / joint_inference_dir record the INVOCATION (ARM_JOINT when
    --joint-inference was passed, ARM_LEGACY when it was not, None when the caller makes no
    claim — a --skip-cpp or --resume run does not regenerate every file, so what this
    invocation asked for says nothing about the files it left alone). The arm the files
    themselves report is read alongside and the two are both recorded; see the OI-307 block
    above for why one of them is not enough.
    """
    scores = {}
    ok_count = 0
    analysis_path_values: dict = {}      # analysisPath value (None if absent) -> count
    analysis_path_stems: dict = {}       # the same, value -> stems (the contamination evidence)
    for stem, status in sorted(score_status.items()):
        entry = {"status": status}
        if status == "OK":
            ours = out_dir / f"{stem}.ours.json"
            if ours.exists():
                data = ours.read_bytes()
                entry.update(_file_fingerprint(ours, data))  # size + sha256 (the .ours.json identity)
                ap = _analysis_path_of(data)
                analysis_path_values[ap] = analysis_path_values.get(ap, 0) + 1
                analysis_path_stems.setdefault(ap, []).append(stem)
                ok_count += 1
                # OI-124: fingerprint the paired .music21.json GROUND TRUTH too. An OK score
                # went through compare_files, so its .music21.json exists and is parseable; record
                # its identity so validate_corpus_dir can detect a stale/foreign/version-mismatched
                # GT export (REPRODUCIBILITY C2's "canonical as-committed" was enforced by nothing).
                m21 = out_dir / f"{stem}.music21.json"
                if m21.exists():
                    fp = _file_fingerprint(m21)
                    entry["music21_size"] = fp["size"]
                    entry["music21_sha256"] = fp["sha256"]
                else:
                    entry["music21_status"] = "MISSING_M21"
            else:
                entry["status"] = "MISSING_OURS"
        scores[stem] = entry

    complete = (ok_count == expected_count
                and all(e["status"] == "OK" for e in scores.values()))

    exe_id = None
    if exe is not None and Path(exe).exists():
        st = Path(exe).stat()
        exe_id = {"path": str(exe), "size": st.st_size, "mtime": int(st.st_mtime)}

    observed_arm = _observed_arm(analysis_path_values)
    if observed_arm in (ARM_JOINT, ARM_LEGACY):
        arm, arm_source = observed_arm, "the produced .ours.json files (their analysisPath)"
    elif observed_arm == ARM_MIXED:
        arm, arm_source = ARM_MIXED, "the produced .ours.json files (their analysisPath)"
    elif requested_arm in (ARM_JOINT, ARM_LEGACY):
        # No file said anything (a corpus of outputs that carry no analysisPath). The
        # invocation is then the only evidence there is, and the source field says so.
        arm, arm_source = requested_arm, "the invocation (no produced file carries an analysisPath)"
    else:
        arm, arm_source = ARM_UNKNOWN, "neither the invocation nor the produced files say"

    manifest = {
        "schema": MANIFEST_SCHEMA,
        "corpus": "Bach chorales",
        "preset": preset,
        "timestamp": timestamp,
        "git_hash": git_hash,
        "expected_count": expected_count,
        "ours_count": ok_count,
        "complete": complete,
        # OI-307: which inference pipeline produced these outputs. `inference_arm` is the
        # value of record; the three fields under it are the evidence it was derived from,
        # kept so a reader can see WHICH of the two sources answered and whether they agreed.
        "inference_arm": arm,
        "inference_arm_source": arm_source,
        "inference_arm_requested": requested_arm,
        "inference_arm_observed": observed_arm,
        "joint_inference_dir": joint_inference_dir,
        "analysis_path_values": {(k if k is not None else "<absent>"): v
                                 for k, v in sorted(analysis_path_values.items(),
                                                    key=lambda kv: (kv[0] is None, kv[0]))},
        # Informational provenance copy-through (audit C2): which music21 produced
        # the ground-truth .music21.json. NOT enforced by validate_corpus_dir.
        "music21_version": music21_version,
        "batch_analyze": exe_id,
        "scores": scores,
    }
    if observed_arm == ARM_MIXED:
        # Only on a mixed corpus, where the per-value stem lists ARE the finding. On a clean
        # corpus they would be 352 stems of no information.
        manifest["analysis_path_stems"] = {
            (k if k is not None else "<absent>"): sorted(v)
            for k, v in sorted(analysis_path_stems.items(), key=lambda kv: (kv[0] is None, kv[0]))}
    (out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    return manifest


def _find_batch_analyze(hint):
    candidates = ([Path(hint)] if hint else []) + [
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build" / "batch_analyze.exe",
        _REPO_ROOT / "ninja_build_rel" / "batch_analyze",
        _REPO_ROOT / "ninja_build" / "batch_analyze",
    ]
    return next((p for p in candidates if p.exists()), None)


def _to_unix_path(p):
    s = str(p.resolve())
    if len(s) >= 2 and s[1] == ':':
        s = '/' + s[0].lower() + s[2:]
    return s.replace('\\', '/')


def _to_win_path(p):
    """Resolved Windows path with forward slashes (e.g. 'C:/s/MS/foo.xml').

    Used for the input/output ARGUMENTS handed to the native batch_analyze.exe.
    The historical code passed unix-form args ('/c/s/MS/...') and relied on
    MSYS2's automatic POSIX→Windows argument conversion to make them openable by
    the native exe. That conversion is DISABLED whenever MSYS_NO_PATHCONV=1 (the
    default in the Claude Code / VS Code Git Bash integration), so the unix-form
    args reached the exe verbatim and every score failed with
    "failed to load score: /c/s/MS/...". A drive-letter forward-slash path is a
    valid Windows path the exe opens directly, is left untouched by MSYS whether
    or not conversion is on, and needs no backslash escaping inside a bash -c
    string — so it loads regardless of the shell's path-conversion state. The exe
    records only the score basename in its output, so the arg form is
    analysis-neutral (byte-identical JSON)."""
    return str(Path(p).resolve()).replace('\\', '/')


def _find_git_bash():
    return next((p for p in [
        Path("C:/Program Files/Git/usr/bin/bash.exe"),
        Path("C:/Program Files (x86)/Git/usr/bin/bash.exe"),
    ] if p.exists()), None)


def _qt_subprocess_env():
    """Environment for the batch_analyze subprocess, hardened for headless runs (F16).

    batch_analyze constructs a QGuiApplication, which must load a Qt platform
    plugin (platforms/qwindows.dll). In a headless/cron context — or any session
    whose Qt platform discovery differs from a normal desktop shell — that init
    fails ("could not load the Qt platform plugin 'windows'") and the entire
    corpus gate goes dark, even though batch_analyze is a headless CLI that needs
    no window. We select the 'offscreen' platform so no windowing display is ever
    required. This is analysis-neutral: batch_analyze reads the score model, not
    any display, so chord/key output is byte-identical to the 'windows' platform
    (verified). A caller that has explicitly set QT_QPA_PLATFORM is respected
    (no override), so this is a strict no-op-or-improvement.

    Returns a full env dict (os.environ + the override) for subprocess.run.
    """
    env = dict(os.environ)
    env.setdefault("QT_QPA_PLATFORM", "offscreen")
    return env


def _run_batch_analyze(exe, xml_path, out_path, preset, diag_fh=None, extra_args=""):
    # extra_args: extra batch_analyze flags appended verbatim (Stage 4b-i:
    # "--ignore-declared-mode" for the mode-absent measurement floor). Empty by
    # default → byte-identical to the historical invocation.
    extra = f" {extra_args}" if extra_args else ""
    run_env = _qt_subprocess_env()
    try:
        import platform
        if platform.system() == 'Windows':
            bash = _find_git_bash()
            if bash:
                cmd = (f'{_to_unix_path(exe)} "{_to_win_path(xml_path)}"'
                       f' "{_to_win_path(out_path)}" --preset {preset}{extra}')
                r = subprocess.run([str(bash), '-c', cmd],
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.PIPE, timeout=120, env=run_env)
                if diag_fh is not None and r.stderr:
                    diag_fh.write(r.stderr.decode('utf-8', 'replace'))
                    diag_fh.flush()
                if r.returncode != 0:
                    print(f"    failed: {r.stderr.decode('utf-8','replace').strip()[:200]}",
                          file=sys.stderr)
                    return False
                return True
        native_cmd = [str(exe), str(xml_path), str(out_path), '--preset', preset]
        if extra_args:
            native_cmd += extra_args.split()
        r = subprocess.run(native_cmd,
                           stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                           timeout=120, env=run_env)
        if diag_fh is not None and r.stderr:
            diag_fh.write(r.stderr.decode('utf-8', 'replace'))
            diag_fh.flush()
        return r.returncode == 0
    except subprocess.TimeoutExpired:
        print("    timed out", file=sys.stderr); return False
    except Exception as e:
        print(f"    error: {e}", file=sys.stderr); return False


def _get_git_hash():
    try:
        r = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                           capture_output=True, text=True, cwd=str(_REPO_ROOT))
        return r.stdout.strip() if r.returncode == 0 else 'unknown'
    except Exception:
        return 'unknown'


def _process_one(args_tuple):
    """Process a single chorale in a worker process.

    Returns (idx, stem, status, stats_or_None, diag_text, error_msg) where
    status is one of 'OK', 'SKIP_NO_M21', 'SKIP_NO_EXE', 'FAILED',
    'SKIP_NO_OURS', 'ERROR'.
    """
    idx, exe, xml_path, ours_path, m21_path, preset, skip_cpp, extra_args = args_tuple
    stem = xml_path.stem

    if not m21_path.exists():
        return (idx, stem, 'SKIP_NO_M21', None, '', None)

    diag_buf = io.StringIO()

    if not skip_cpp or not ours_path.exists():
        if exe is None:
            return (idx, stem, 'SKIP_NO_EXE', None, '', None)
        diag_buf.write(f"[PROCESSING] {stem}\n")
        ok = _run_batch_analyze(exe, xml_path, ours_path, preset, diag_buf, extra_args)
        if not ok:
            return (idx, stem, 'FAILED', None, diag_buf.getvalue(), None)

    if not ours_path.exists():
        return (idx, stem, 'SKIP_NO_OURS', None, diag_buf.getvalue(), None)

    try:
        ours_meta, m21_meta, compared = cmp.compare_files(ours_path, m21_path)
    except Exception as exc:
        return (idx, stem, 'ERROR', None, diag_buf.getvalue(), str(exc))

    counts = cmp.summarize(compared)
    ci_n, ci_rate = cmp.chord_identity_agreement(counts)
    total_r = sum(counts.values())
    m21_n = len(m21_meta.get("regions", []))
    unaligned = counts.get('unaligned', 0)

    stats = {
        'ci_n': ci_n,
        'ci_rate': ci_rate,
        'total_r': total_r,
        'm21_n': m21_n,
        'unaligned': unaligned,
    }
    return (idx, stem, 'OK', stats, diag_buf.getvalue(), None)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preset", default="Baroque",
                        choices=PRESET_CHOICES)
    parser.add_argument("--batch-analyze", metavar="PATH")
    parser.add_argument("--corpus-dir", metavar="DIR", default="tools/corpus")
    parser.add_argument("--output-dir", metavar="DIR")
    parser.add_argument("--skip-cpp", action="store_true")
    parser.add_argument("--ignore-declared-mode", action="store_true",
                        help="Stage 4b-i: pass --ignore-declared-mode to batch_analyze "
                             "(mode-absent measurement floor). Default off.")
    parser.add_argument("--resume", action="store_true",
                        help="Keep existing .ours.json (skip the clean-slate); "
                             "regenerate only missing files.")
    parser.add_argument("--dump-cadence-anchor", action="store_true",
                        help="Stage 4c-i: pass --dump-cadence-anchor to batch_analyze "
                             "(appends the read-only cadence anchor to each .ours.json; "
                             "scoring byte-identical). Default off.")
    parser.add_argument("--dump-tonicization", action="store_true",
                        help="Stage 6-tonic-i: pass --dump-tonicization to batch_analyze "
                             "(appends the read-only tonicization labels to each "
                             ".ours.json; scoring byte-identical). Default off.")
    parser.add_argument("--dump-fullspine", action="store_true",
                        help="E0: pass --dump-fullspine to batch_analyze (write the "
                             "full-spine L1->L5 per-stem side file; diagnostic, returns "
                             "before analyzeScore, byte-identical). Default off.")
    parser.add_argument("--fullspine-no-override", action="store_true",
                        help="EG-2 G3: pass --fullspine-no-override to batch_analyze "
                             "(only with --dump-fullspine; disables the §5.5 fine-grain "
                             "override — the probe arm). Default off.")
    parser.add_argument("--dump-l5", action="store_true",
                        help="Phase 5c Step M: pass --dump-l5 to batch_analyze "
                             "(appends the read-only dormant Layer-5 would-be Roman "
                             "numerals to each .ours.json; scoring byte-identical). "
                             "Default off.")
    parser.add_argument("--dump-modulation", action="store_true",
                        help="Stage 4d-i: pass --dump-modulation to batch_analyze "
                             "(appends the read-only local-modulation spans to each "
                             ".ours.json; scoring byte-identical). Default off.")
    parser.add_argument("--dump-joint-key", action="store_true",
                        help="J-key-i: pass --dump-joint-key to batch_analyze "
                             "(appends the read-only scoped-joint key decision to each "
                             ".ours.json; scoring byte-identical). Default off.")
    parser.add_argument("--joint-key-wiring", action="store_true",
                        help="J-key-iii: pass --joint-key-wiring to batch_analyze "
                             "(WIRES the scoped-joint key decision into production: "
                             "overrides each region's key + re-emits the chord under it). "
                             "INTENTIONAL behavior change; not byte-identical. Default off.")
    parser.add_argument("--param-override", metavar="FILE",
                        help="Stage-5 fitter (design D-6): pass --param-override FILE to "
                             "batch_analyze so the regen uses fitted scoring-constant values. "
                             "Pass a Windows-form path (e.g. C:/tmp/x.txt); MSYS path "
                             "conversion is off. Byte-identical to the un-passed run when the "
                             "file sets every constant to its current value. Default off.")
    parser.add_argument("--joint-inference", metavar="DIR",
                        help="OI-178 ADOPTION (user-ratified 2026-07-26): pass --joint-inference DIR "
                             "to batch_analyze so each .ours.json is produced by the joint estimator's "
                             "decode (tables + selected weights read from DIR, e.g. "
                             "C:/s/MS/tools/joint_estimator) instead of the legacy analyzeScore "
                             "pipeline. INTENTIONAL behavior change; not byte-identical. Pass a "
                             "Windows-form path (MSYS path conversion is off). Default off.")
    parser.add_argument("--diag-out", metavar="FILE",
                        help="Append batch_analyze stderr to this file (for diagnostics)")
    args = parser.parse_args()

    corpus_dir = Path(args.corpus_dir)
    if args.output_dir:
        out_dir = Path(args.output_dir)
    else:
        out_dir = _REPO_ROOT / "tools" / f"corpus_{args.preset.lower()}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Per-preset isolation (Stage 2.2a): when writing into a dedicated output dir,
    # clean-slate the .ours.json + manifest first so a FAILED worker can never leave
    # a previous-preset file countable (the M3 contamination mechanism). --resume or
    # --skip-cpp keep the existing files (re-aggregation / fill-missing).
    out_is_separate = out_dir.resolve() != corpus_dir.resolve()
    if out_is_separate and not args.resume and not args.skip_cpp:
        for stale in list(out_dir.glob("*.ours.json")) + [out_dir / MANIFEST_NAME]:
            if stale.exists():
                stale.unlink()

    exe = _find_batch_analyze(args.batch_analyze)
    if exe is None and not args.skip_cpp:
        print("ERROR: batch_analyze not found.", file=sys.stderr); sys.exit(1)
    if exe:
        print(f"Using batch_analyze: {exe}")

    diag_fh = None
    if args.diag_out:
        diag_fh = open(args.diag_out, 'w', encoding='utf-8')
        print(f"Diagnostic stderr → {args.diag_out}")

    xml_files = sorted(f for f in corpus_dir.glob("*.xml")
                       if not f.stem.endswith("_m21"))
    total = len(xml_files)
    if total == 0:
        print(f"ERROR: no .xml files in {corpus_dir}", file=sys.stderr); sys.exit(1)

    print(f"\nBach chorales — preset={args.preset}  ({total} files)\n")

    # Make the per-preset dir self-contained: characterise_bir_false reads
    # {stem}.music21.json alongside {stem}.ours.json from a single --corpus-dir.
    # The ground-truth music21 files are preset-independent, so copy (not regen).
    if out_is_separate:
        for xml_path in xml_files:
            m21_src = corpus_dir / f"{xml_path.stem}.music21.json"
            if m21_src.exists():
                shutil.copy2(m21_src, out_dir / m21_src.name)

    agree_sum = 0.0
    compared_n = 0
    total_regions = 0
    total_agree = 0
    total_chord = 0
    score_status: dict[str, str] = {}

    extra_flags = []
    if args.ignore_declared_mode:
        extra_flags.append("--ignore-declared-mode")
    if args.dump_cadence_anchor:
        extra_flags.append("--dump-cadence-anchor")
    if args.dump_tonicization:
        extra_flags.append("--dump-tonicization")
    if args.dump_l5:
        extra_flags.append("--dump-l5")
    if args.dump_fullspine:
        extra_flags.append("--dump-fullspine")
    if args.fullspine_no_override:
        extra_flags.append("--fullspine-no-override")
    if args.dump_modulation:
        extra_flags.append("--dump-modulation")
    if args.dump_joint_key:
        extra_flags.append("--dump-joint-key")
    if args.joint_key_wiring:
        extra_flags.append("--joint-key-wiring")
    if args.param_override:
        extra_flags.append(f"--param-override {args.param_override}")
    if args.joint_inference:
        extra_flags.append(f"--joint-inference {args.joint_inference}")
    extra_args = " ".join(extra_flags)
    work_items = [
        (idx, exe, xml_path,
         out_dir / f"{xml_path.stem}.ours.json",
         corpus_dir / f"{xml_path.stem}.music21.json",
         args.preset, args.skip_cpp, extra_args)
        for idx, xml_path in enumerate(xml_files, 1)
    ]

    workers = min(multiprocessing.cpu_count(), len(xml_files))
    print(f"  Parallelising over {workers} workers ({total} chorales)...\n")

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_process_one, item): item[0] for item in work_items}
        for future in concurrent.futures.as_completed(futures):
            try:
                idx, stem, status, stats, diag_text, err = future.result()
            except Exception as exc:
                print(f"  worker crashed: {exc}", file=sys.stderr)
                continue

            if diag_text and diag_fh is not None:
                diag_fh.write(diag_text)
                diag_fh.flush()

            score_status[stem] = status

            if status == 'SKIP_NO_M21':
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no music21.json)")
                continue
            if status == 'SKIP_NO_EXE':
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no exe)")
                continue
            if status == 'FAILED':
                print(f"  [{idx:>3}/{total}] {stem:<30}  FAILED")
                continue
            if status == 'SKIP_NO_OURS':
                print(f"  [{idx:>3}/{total}] {stem:<30}  SKIP (no ours.json)")
                continue
            if status == 'ERROR':
                print(f"  [{idx:>3}/{total}] {stem:<30}  ERROR: {err}", file=sys.stderr)
                continue

            print(f"  [{idx:>3}/{total}] {stem:<30}  m21:{stats['m21_n']:>3}"
                  f"  ours:{stats['total_r']:>3}  chord_id:{stats['ci_n']:>3}"
                  f"  {stats['ci_rate']:.0%}")

            agree_sum += stats['ci_rate']
            compared_n += 1
            total_regions += stats['total_r']
            total_agree += stats['ci_n']
            total_chord += stats['total_r'] - stats['unaligned']

    print(f"\n{'='*65}")
    print(f"Bach chorales — preset={args.preset} — aggregate results")
    print(f"{'='*65}")
    print(f"Chorales compared   : {compared_n}/{total}")
    if total_chord:
        print(f"Total aligned regions: {total_chord}")
        print(f"Chord identity agree : {total_agree} ({100*total_agree/total_chord:.1f}%)")
    if compared_n:
        print(f"Mean per-chorale    : {agree_sum/compared_n:.1%}")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = _REPO_ROOT / "tools" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    sp = report_dir / f"bach_{args.preset.lower()}_{timestamp}.json"
    sp.write_text(json.dumps({
        'corpus': 'Bach chorales',
        'preset': args.preset,
        'timestamp': timestamp,
        'git_hash': _get_git_hash(),
        'chorales_compared': compared_n,
        'chorales_total': total,
        'aggregate': {
            'total_aligned': total_chord,
            'chord_identity_agree': total_agree,
            'chord_identity_pct': round(100*total_agree/total_chord, 2) if total_chord else 0,
            'mean_per_chorale_pct': round(100*agree_sum/compared_n, 2) if compared_n else 0,
        },
        'out_dir': str(out_dir),
    }, indent=2), encoding='utf-8')
    print(f"\nReport written to {sp}")
    print(f"ours JSON written to {out_dir}")

    if diag_fh is not None:
        diag_fh.close()
        print(f"Diagnostic stderr written to {args.diag_out}")

    # ── Manifest stamp + fail-loud completeness check (Stage 2.2a) ────────────
    # OI-307: the invocation makes a claim about the arm only when it regenerated everything.
    # --skip-cpp and --resume both keep files this run did not produce, so this run's flags
    # say nothing about them; the claim is then withheld and the files are the only evidence.
    requested_arm = None
    if not args.skip_cpp and not args.resume:
        requested_arm = ARM_JOINT if args.joint_inference else ARM_LEGACY

    manifest = _write_manifest(out_dir, args.preset, score_status,
                               expected_count=total, git_hash=_get_git_hash(),
                               timestamp=timestamp, exe=exe,
                               music21_version=_detect_music21_version(corpus_dir),
                               requested_arm=requested_arm,
                               joint_inference_dir=args.joint_inference)
    print(f"Manifest written to {out_dir / MANIFEST_NAME}  "
          f"(preset={args.preset}, complete={manifest['complete']}, "
          f"{manifest['ours_count']}/{total}, arm={manifest['inference_arm']})")

    # ── OI-307: the arm the invocation asked for and the arm the files report must agree ──
    # This cannot fire on a normal run; it fires when the directory holds output from more
    # than one pipeline, or when the flag and the output disagree. Both are states in which
    # any figure measured off this corpus describes a system nobody named, so it is a stop
    # rather than a warning.
    arm_faults = []
    if manifest["inference_arm"] == ARM_MIXED:
        arm_faults.append(
            f"the directory mixes analysisPath values: {manifest['analysis_path_values']}")
    if (requested_arm in (ARM_JOINT, ARM_LEGACY)
            and manifest["inference_arm_observed"] in (ARM_JOINT, ARM_LEGACY)
            and requested_arm != manifest["inference_arm_observed"]):
        arm_faults.append(
            f"the invocation asked for the {requested_arm} arm and the produced files report "
            f"the {manifest['inference_arm_observed']} arm")
    if arm_faults:
        print("\n" + "!" * 65, file=sys.stderr)
        # ASCII only (OI-297): this module reconfigures stdout (:30) and NOT stderr, and
        # every line of this block goes to stderr.
        print(f"!! INFERENCE-ARM FAULT: preset={args.preset}", file=sys.stderr)
        for f in arm_faults:
            print(f"!!   {f}", file=sys.stderr)
        print("!!   This corpus is NOT safe to measure; see OPEN_ITEMS.md OI-307.",
              file=sys.stderr)
        print("!" * 65, file=sys.stderr)
        sys.exit(1)

    if not manifest['complete']:
        bad = sorted(s for s, st in score_status.items() if st != 'OK')
        missing = sorted(x.stem for x in xml_files if x.stem not in score_status)
        print("\n" + "!" * 65, file=sys.stderr)
        print(f"!! CORPUS INCOMPLETE — preset={args.preset}: "
              f"{manifest['ours_count']}/{total} OK", file=sys.stderr)
        if bad:
            print(f"!!   non-OK scores ({len(bad)}): {', '.join(bad)}", file=sys.stderr)
        if missing:
            print(f"!!   never reported ({len(missing)}): {', '.join(missing)}",
                  file=sys.stderr)
        print("!!   This corpus is NOT safe to measure — re-run before reading a "
              "BIR count.", file=sys.stderr)
        print("!" * 65, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
