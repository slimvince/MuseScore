#!/usr/bin/env python3
"""Parse an OpenCppCoverage cobertura XML into per-file and per-layer LINE coverage.

OpenCppCoverage emits LINE coverage only (no per-branch data). This rolls the
per-<class> line hits up into the composing module's L1-L4 layer buckets so a
before/after backfill delta is readable at a glance.

Usage:  python tools/coverage/parse_cobertura.py <cobertura.xml> [--only src\\composing]
"""
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

# Map a source path fragment -> layer label. First match wins (order matters).
LAYERS = [
    ("analysis/notemodel",       "L1 notemodel"),
    ("analysis/engravingbridge", "L1.5 engravingbridge"),
    ("analysis/slicing",         "L2 slicing"),
    ("analysis/harmony",         "L2 harmony"),
    ("analysis/key",             "L3 key"),
    ("analysis/chord",           "L4 chord"),
    ("analysis/function",        "L4 function"),
    ("analysis/decode",          "decode"),
    ("analysis/region",          "region"),
    ("analysis/section",         "section"),
    ("analysis/scoreharvest",    "scoreharvest"),
]


def layer_of(path: str):
    p = path.replace("\\", "/").lower()
    for frag, label in LAYERS:
        if frag in p:
            return label
    return None  # not an analysis source (e.g. a *_tests.cpp) -> skip


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    xml_path = sys.argv[1]
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1].replace("\\", "/").lower()

    tree = ET.parse(xml_path)
    root = tree.getroot()

    # filename -> (covered, valid). De-dup classes that share a filename.
    files = {}
    for cls in root.iter("class"):
        fn = cls.get("filename", "")
        fnl = fn.replace("\\", "/").lower()
        if only and only not in fnl:
            continue
        if layer_of(fn) is None:
            continue
        cov = val = 0
        for ln in cls.iter("line"):
            val += 1
            if int(ln.get("hits", "0")) > 0:
                cov += 1
        c0, v0 = files.get(fn, (0, 0))
        files[fn] = (c0 + cov, v0 + val)

    def pct(c, v):
        return (100.0 * c / v) if v else 0.0

    # Per-file
    print(f"{'file':52} {'line%':>7} {'lines':>10}")
    print("-" * 74)
    for fn in sorted(files, key=lambda k: pct(*files[k])):
        c, v = files[fn]
        short = fn.replace("\\", "/")
        short = short[short.lower().find("analysis/") + len("analysis/"):] if "analysis/" in short.lower() else short
        print(f"{short:52} {pct(c, v):7.1f} {f'{c}/{v}':>10}")

    # Per-layer
    layer = defaultdict(lambda: [0, 0])
    for fn, (c, v) in files.items():
        lab = layer_of(fn)
        layer[lab][0] += c
        layer[lab][1] += v
    print("\n=== per-layer (line%) ===")
    order = [lab for _, lab in LAYERS]
    tc = tv = 0
    for lab in order:
        if lab in layer:
            c, v = layer[lab]
            tc += c
            tv += v
            print(f"{lab:28} {pct(c, v):6.1f}%  {c}/{v}")
    print(f"{'TOTAL (composing analysis)':28} {pct(tc, tv):6.1f}%  {tc}/{tv}")


if __name__ == "__main__":
    main()
