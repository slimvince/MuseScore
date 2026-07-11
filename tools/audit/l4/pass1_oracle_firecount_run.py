#!/usr/bin/env python3
"""Drive batch_analyze over the pinned Baroque corpus to harvest the default-OFF oracle
fire counts (Layer-4 audit pass-1, oracle session). Invokes batch_analyze.exe DIRECTLY
(native subprocess, no git-bash wrapper) so the Windows-path MU_ORACLE_FIRECOUNT value is
passed through verbatim (the run_bach_preset path routes through `bash -c`, whose MSYS
entry rewrites a Windows-path env value to POSIX form and breaks fopen). Serial, so the
shared-file JSONL append is race-free. Read-only w.r.t. the committed reference: writes only
under the given --out-dir and the fire file. Usage:
    python tools/audit/l4/pass1_oracle_firecount_run.py <corpus_xml_dir> <out_dir> <fire_jsonl>
"""
import os, sys, glob, subprocess

CORPUS = sys.argv[1] if len(sys.argv) > 1 else "tools/corpus"
OUT = sys.argv[2]
FIRE = sys.argv[3]
EXE = os.path.abspath("ninja_build_rel/batch_analyze.exe")

os.makedirs(OUT, exist_ok=True)
if os.path.exists(FIRE):
    os.remove(FIRE)

env = dict(os.environ)
env["QT_QPA_PLATFORM"] = "offscreen"      # headless (F16), analysis-neutral
env["MU_ORACLE_FIRECOUNT"] = FIRE          # Windows path, native process -> fopen works

xmls = sorted(glob.glob(os.path.join(CORPUS, "*.xml")))
print(f"scores: {len(xmls)}  exe: {EXE}")
ok = 0
fail = 0
for i, xml in enumerate(xmls):
    stem = os.path.splitext(os.path.basename(xml))[0]
    out = os.path.join(OUT, stem + ".ours.json")
    try:
        r = subprocess.run([EXE, xml, out, "--preset", "Baroque"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           env=env, timeout=180)
        if r.returncode == 0:
            ok += 1
        else:
            fail += 1
            print(f"  FAIL rc={r.returncode}: {stem}")
    except subprocess.TimeoutExpired:
        fail += 1
        print(f"  TIMEOUT: {stem}")
    if (i + 1) % 50 == 0:
        print(f"  ... {i+1}/{len(xmls)}")
print(f"done: ok={ok} fail={fail}")
