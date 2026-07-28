#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# MuseScore-Studio-CLA-applies
#
# MuseScore Studio
# Music Composition & Notation
#
# Copyright (C) 2026 MuseScore Limited
"""gen_ground_truth_inventory.py — OI-206 / cc_instruction_analysis_cost_profile.md Task 5.

READ-ONLY inventory of the Roman-numeral / harmonic-analysis annotated (ground-truth) material on disk
under tools/dcml/. Answers plainly: is there, on disk TODAY, annotated material both substantially
LARGER and substantially MORE CHROMATIC than a Bach chorale? Enumerates each DCML sub-corpus with its
score count, harmony-TSV (annotation) count, total label count, measure range (from the .mscx last
measure number where cheaply available), and a coarse era/chromaticism class.

Does NOT download, convert, or onboard anything (the dispatch's hard constraint). Derived figures only
(#17f). Writes tools/notation_seams/ground_truth_inventory.json + a printed summary.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DCML = REPO / "tools" / "dcml"
NS = REPO / "tools" / "notation_seams"

# coarse era / chromaticism class by corpus dir name (documentary; from the repertoire, not measured)
ERA = {
    "bach_chorales": ("Baroque chorale", "low (diatonic) — the BASELINE"),
    "corelli": ("Baroque", "low-moderate"),
    "bach_en_fr_suites": ("Baroque", "low-moderate"),
    "bach_solo": ("Baroque", "low-moderate"),
    "scarlatti_sonatas": ("late Baroque", "moderate"),
    "couperin_clavecin": ("Baroque", "low-moderate"),
    "couperin_concerts": ("Baroque", "low-moderate"),
    "handel": ("Baroque", "low-moderate"),
    "frescobaldi": ("early Baroque", "low"),
    "sweelinck": ("Renaissance/Baroque", "low"),
    "monteverdi": ("early Baroque", "moderate (madrigal)"),
    "peri_euridice": ("early Baroque", "moderate"),
    "pergolesi": ("Baroque/Classical", "moderate"),
    "kleine_geistliche_konzerte": ("Baroque", "moderate"),
    "mozart_piano_sonatas": ("Classical", "moderate"),
    "beethoven_piano_sonatas": ("Classical→Romantic", "HIGH"),
    "ABC": ("Classical→Romantic (Beethoven quartets)", "HIGH"),
    "cpe_bach": ("Classical", "moderate"),
    "jc_bach": ("Classical", "moderate"),
    "wf_bach": ("Baroque/Classical", "moderate"),
    "kozeluh": ("Classical", "moderate"),
    "pleyel": ("Classical", "moderate"),
    "chopin_mazurkas": ("Romantic", "HIGH"),
    "schubert_winterreise": ("Romantic (Lieder)", "HIGH"),
    "grieg_lyric_pieces": ("late Romantic", "HIGH"),
    "tchaikovsky_seasons": ("Romantic", "HIGH"),
    "dvorak_silhouettes": ("late Romantic", "HIGH"),
    "liszt_pelerinage": ("Romantic", "VERY HIGH"),
    "medtner_tales": ("late Romantic", "VERY HIGH"),
    "rachmaninoff_piano": ("late Romantic", "VERY HIGH"),
    "wagner_overtures": ("Romantic (Tristan/Meistersinger)", "EXTREME — the most chromatic"),
    "mahler_kindertotenlieder": ("late Romantic (orch. song)", "VERY HIGH"),
    "debussy_suite_bergamasque": ("Impressionist", "VERY HIGH"),
    "ravel_piano": ("Impressionist", "VERY HIGH"),
    "schulhoff_suite_dansante_en_jazz": ("20th c. jazz-idiom", "VERY HIGH (extended)"),
    "bartok_bagatelles": ("early modern", "VERY HIGH"),
    "c_schumann_lieder": ("Romantic (Lieder)", "HIGH"),
    "schumann_kinderszenen": ("Romantic", "HIGH"),
    "schumann_liederkreis": ("Romantic (Lieder)", "HIGH"),
    "mendelssohn_quartets": ("Romantic", "HIGH"),
    "poulenc": ("20th c.", "VERY HIGH"),
    "when_in_rome": ("annotation-only (no scores)", "mixed (RN analyses incl. the chorale GT)"),
}


def git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(REPO)).decode().strip()
    except Exception:
        return "unknown"


def count_tsv_labels(tsv_dir):
    """Total non-header rows across every .harmonies.tsv (a coarse label count) + file count."""
    n_files, n_labels = 0, 0
    if not tsv_dir.is_dir():
        return 0, 0
    for f in tsv_dir.glob("*.tsv"):
        n_files += 1
        try:
            with open(f, encoding="utf-8", newline="") as fh:
                rows = sum(1 for _ in fh) - 1  # minus header
            n_labels += max(0, rows)
        except Exception:
            pass
    return n_files, n_labels


def max_measure(ms3_dir):
    """Cheap upper-bound on movement size: the largest <irregular?>/measure count seen by counting
    <Measure> tags in the largest .mscx (documentary, not exact bars)."""
    if not ms3_dir.is_dir():
        return None, 0
    best = 0
    n_scores = 0
    for f in ms3_dir.glob("*.mscx"):
        n_scores += 1
    # sample the largest file only (by size) for a measure-tag count (cheap)
    scores = sorted(ms3_dir.glob("*.mscx"), key=lambda p: p.stat().st_size, reverse=True)
    if scores:
        try:
            txt = scores[0].read_text(encoding="utf-8", errors="replace")
            best = txt.count("<Measure ") + txt.count("<Measure>")
        except Exception:
            best = 0
    return (best or None), n_scores


def main():
    corpora = []
    if DCML.is_dir():
        for d in sorted(DCML.iterdir()):
            if not d.is_dir():
                continue
            name = d.name
            n_tsv, n_labels = count_tsv_labels(d / "harmonies")
            largest_measures, n_scores = max_measure(d / "MS3")
            era, chroma = ERA.get(name, ("(unclassified)", "(unclassified)"))
            corpora.append({
                "corpus": name,
                "era": era,
                "chromaticism": chroma,
                "scores_MS3": n_scores,
                "harmony_tsvs": n_tsv,
                "total_labels": n_labels,
                "largest_movement_measure_tags": largest_measures,
                "annotations_present": n_tsv > 0,
            })

    # the plain answer to Task 5
    larger_and_more_chromatic = [
        c for c in corpora
        if c["annotations_present"] and c["chromaticism"] not in ("low (diatonic) — the BASELINE",)
        and (c["chromaticism"].startswith("HIGH") or "VERY HIGH" in c["chromaticism"]
             or "EXTREME" in c["chromaticism"])
        and (c["largest_movement_measure_tags"] or 0) > 57   # a chorale tops out ~57 measures
    ]

    out = {
        "provenance": {
            "generator": "tools/notation_seams/gen_ground_truth_inventory.py",
            "instrument_commit": git_hash(),
            "open_item": "OI-206 / cc_instruction_analysis_cost_profile.md Task 5",
            "note": "READ-ONLY enumeration of tools/dcml/. label counts = non-header TSV rows (coarse); "
                    "largest_movement_measure_tags = <Measure> tag count in the largest .mscx per corpus "
                    "(documentary size proxy, not exact bars). No download / convert / onboard.",
            "chorale_baseline": "bach_chorales: SATB, ~7-57 measures/movement, 4 voices, largely diatonic; "
                                "its RN ground truth lives in when_in_rome/ (the bach_chorales repo carries "
                                "no harmonies/ on disk).",
        },
        "n_corpora": len(corpora),
        "n_corpora_with_annotations": sum(1 for c in corpora if c["annotations_present"]),
        "answer_larger_and_more_chromatic_than_a_chorale": {
            "verdict": "YES" if larger_and_more_chromatic else "NO",
            "examples": sorted(larger_and_more_chromatic,
                               key=lambda c: -(c["total_labels"] or 0))[:10],
            "wagner_tristan_on_disk": any(c["corpus"] == "wagner_overtures" and c["annotations_present"]
                                          for c in corpora),
        },
        "corpora": sorted(corpora, key=lambda c: -(c["total_labels"] or 0)),
    }
    (NS / "ground_truth_inventory.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {NS / 'ground_truth_inventory.json'}")
    print(f"{out['n_corpora']} corpora, {out['n_corpora_with_annotations']} with annotations")
    print(f"larger+more-chromatic-than-chorale: {out['answer_larger_and_more_chromatic_than_a_chorale']['verdict']}"
          f"  (Tristan on disk: {out['answer_larger_and_more_chromatic_than_a_chorale']['wagner_tristan_on_disk']})")
    for c in out["answer_larger_and_more_chromatic_than_a_chorale"]["examples"][:6]:
        print(f"   {c['corpus']:26s} labels={c['total_labels']:6d} tsvs={c['harmony_tsvs']:3d} "
              f"largest~{c['largest_movement_measure_tags']} measures  [{c['chromaticism']}]")


if __name__ == "__main__":
    main()
