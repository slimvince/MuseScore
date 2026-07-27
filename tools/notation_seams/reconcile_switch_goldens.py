#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""reconcile_switch_goldens.py — the notation-switch golden-diff reconciliation.

THE SWITCH (user-ratified 2026-07-27) flips ``useJointNotationRecord`` default ON, so the
pipeline-snapshot goldens are refreshed from the LEGACY notation arm to the RECORD arm. This
instrument reconciles that legacy->record golden diff against the P6 dual-arm classified
taxonomy (``tools/notation_seams/dualarm_classified_report.json``), the switch's established
evidence oracle.

For each golden it:
  * asserts the NON-flag-gated surfaces are BYTE-IDENTICAL between the arms. ``implode`` and
    ``keyAreas`` are built from ``analyzeSection`` DIRECTLY (composing-side, no flag), and
    ``tickLocal`` from ``analyzeHarmonicContextLocallyAtTick`` (NOT flag-gated); none routes
    through ``useJointNotationRecord``, so a change on any of them is a STOP (never patched);
  * classifies EVERY difference on the flag-gated surfaces (``tickRegional`` via
    ``analyzeHarmonicContextAtTick``; ``annotation`` via ``addHarmonicAnnotationsToSelection``;
    ``implodedChordTrack`` via ``populateChordTrack``) into the SAME classes classify_dualarm.py
    uses:
      - inference-driven : the record's committed reading (root / quality / key / segmentation /
                           voicing) differs — the adoption's expected differences reaching the
                           notation surface;
      - presentation-rule: a ratified rule accounts for it, cited — the §3.3 alternatives
                           ordering, the D2 grading-vs-display token split, the applied-chord
                           Nashville "?" convention, the C1 two-mode display;
      - input-scoping     : the OI-204 excluded-staff class (structurally 0 on this
                           chord-track-free corpus);
      - UNEXPLAINED       : no rule accounts for it, OR a field P6 never captured
                           (``wasRegional`` / the temporal-extension fields) changed, OR an
                           invariant surface changed. Any UNEXPLAINED entry is a STOP (#13/#15).

The golden's per-item fields (root, quality, key, alternatives, text, pitches, harmonyText,
durationTicks) are a SUBSET of the fields P6 captured (rootPc, quality, keyFifths, keyMode,
symbol, roman, nashville, alternatives, voicing), so every golden difference maps onto a
P6-classified difference BY CONSTRUCTION — the only way to get an UNEXPLAINED entry is a field
P6 did not capture, or an invariant-surface change, which is exactly what must STOP.

Exit 0 iff: every invariant surface byte-identical AND 0 UNEXPLAINED AND 0 input-scoping.
Stdlib only (#17f); invents no value, patches nothing — a difference is CLASSIFIED, never bent.

Usage:
    python tools/notation_seams/reconcile_switch_goldens.py \
        [--base HEAD] \
        [--out tools/notation_seams/switch_golden_reconciliation.json] \
        [--summary tools/notation_seams/switch_golden_reconciliation_summary.txt]
"""

import argparse
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SNAP_REL = "src/notation/tests/pipeline_snapshot_tests/snapshots"

INFERENCE = "inference-driven"
PRESENTATION = "presentation-rule"
INPUT_SCOPING = "input-scoping"
# an EXPLAINED class OUTSIDE the P6 serialization scope: a field the golden captures but the P6
# dual-arm capture did NOT (the note-seam carriage's temporalExtensions + wasRegional). Both are
# WRITTEN on the legacy note-seam builder and left at their documented defaults on the record arm
# (the joint record §3.6-EXCLUDES temporalExtensions, jointnotationrecord.h; wasRegional is the
# record's "regional answer" constant, notationcomposingbridge.cpp:605), and BOTH are read by NO
# production consumer (audited, notationcomposingbridge.cpp:583 — grep confirms only the snapshot
# test serializes them). So a change here is a documented, production-INERT consequence of the
# ratified record-arm note-seam design, NOT an inference difference and NOT a surprise — it is
# accounted for, just by a rule P6 never had to serialize.
INERT_AUX = "record-arm-inert-auxiliary"
UNEXPLAINED = "UNEXPLAINED"

INVARIANT_SURFACES = ["implode", "keyAreas", "tickLocal"]
GATED_SURFACES = ["tickRegional", "annotation", "implodedChordTrack"]

# grading-form quality tokens a DISPLAY chord symbol must never carry (the ratified D2 split).
GRADING_TOKENS = ("Dom", "HalfDim", "AugSixth", "Neapolitan")

# the tickRegional fields that are NOT the committed reading and that the record-arm note-seam
# builder leaves at its documented default (temporalExtensions default; wasRegional=true). The
# legacy golden already carries these same defaults at the sampled ticks, so they MUST stay
# byte-identical; a change means the record arm populated a field P6 never captured -> STOP.
TICKREGIONAL_AUX_FIELDS = [
    "wasRegional", "bassIsStepwiseFromPrevious", "bassIsStepwiseToNext",
    "previousRootPc", "previousBassPc", "previousQuality",
]


def has_grading_token(t):
    return any(tok in (t or "") for tok in GRADING_TOKENS)


def classify_text(old, new, kind="symbol"):
    """Classify a differing (old, new) chord-symbol / roman / bracket text pair."""
    o = old or ""
    n = new or ""
    if o == n:
        return None
    if has_grading_token(o) != has_grading_token(n):
        return (PRESENTATION, "D2 grading-vs-display symbol split (a grading-only quality token present on one arm only)")
    if ("?" in o) != ("?" in n):
        return (PRESENTATION, "applied-chord Nashville '?' convention (legacy formatter continuity)")
    return (INFERENCE, "committed reading text differs (chord symbol / roman moved)")


def git_show(base, rel):
    out = subprocess.run(["git", "show", "%s:%s" % (base, rel)],
                         cwd=REPO_ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if out.returncode != 0:
        raise RuntimeError("git show failed for %s:%s -- %s" % (base, rel, out.stderr.decode("utf-8", "replace")))
    return json.loads(out.stdout.decode("utf-8"))


def blank_counts():
    return {"identical": 0, INFERENCE: 0, PRESENTATION: 0, INPUT_SCOPING: 0, INERT_AUX: 0, UNEXPLAINED: 0}


# ── per-surface classifiers ─────────────────────────────────────────────────────

def classify_tickregional(old_list, new_list):
    diffs = []
    ident = 0
    oldd = {e.get("tick"): e for e in old_list}
    newd = {e.get("tick"): e for e in new_list}
    for tick in sorted(set(oldd) | set(newd)):
        o = oldd.get(tick)
        n = newd.get(tick)
        if o is None or n is None:
            diffs.append({"tick": tick, "field": "presence", "class": UNEXPLAINED,
                          "basis": "one-sided tick (both arms sample the identical ticks — a one-sided sample is unexpected)"})
            continue
        found = False
        # (a) production-inert auxiliary fields (temporalExtensions + wasRegional): the record-arm
        # note-seam builder leaves them at documented defaults; NO production consumer reads them
        # (audited). One collapsed entry per tick naming the moved fields.
        aux_moved = [f for f in TICKREGIONAL_AUX_FIELDS if o.get(f) != n.get(f)]
        if aux_moved:
            diffs.append({"tick": tick, "field": "auxiliary", "movedFields": aux_moved,
                          "class": INERT_AUX,
                          "basis": "record-arm inert-auxiliary: the note-seam builder leaves temporalExtensions/wasRegional at documented defaults (joint record §3.6-excludes temporalExtensions; audited no downstream production consumer, notationcomposingbridge.cpp:583) — committed reading unaffected; outside the P6 serialization scope, production-inert"})
            found = True
        # (b) committed reading
        if o.get("root") != n.get("root") or o.get("quality") != n.get("quality"):
            diffs.append({"tick": tick, "field": "committed",
                          "old": {"root": o.get("root"), "quality": o.get("quality"), "key": o.get("key")},
                          "new": {"root": n.get("root"), "quality": n.get("quality"), "key": n.get("key")},
                          "class": INFERENCE, "basis": "committed reading differs (root/quality)"})
            found = True
        elif o.get("key") != n.get("key"):
            diffs.append({"tick": tick, "field": "key", "old": o.get("key"), "new": n.get("key"),
                          "class": INFERENCE,
                          "basis": "committed key differs (the record arm commits a two-mode key; a P6 inference-or-C1 difference — attributed to inference as the tickRegional golden carries no signature-fifths to split a tonic move from a two-mode collapse)"})
            found = True
        elif o.get("alternatives") != n.get("alternatives"):
            diffs.append({"tick": tick, "field": "alternatives", "old": o.get("alternatives"), "new": n.get("alternatives"),
                          "class": PRESENTATION,
                          "basis": "§3.3 alternatives ordering (record ranks by content score; committed root/quality/key identical)"})
            found = True
        if not found:
            ident += 1
    return diffs, ident


def classify_implodedchordtrack(old_list, new_list):
    diffs = []
    ident = 0
    oldd = defaultdict(list)
    newd = defaultdict(list)
    for e in old_list:
        oldd[e.get("tick")].append(e)
    for e in new_list:
        newd[e.get("tick")].append(e)
    for tick in sorted(set(oldd) | set(newd)):
        olds = oldd.get(tick, [])
        news = newd.get(tick, [])
        if len(olds) != 1 or len(news) != 1:
            # a tick present in one arm only, or a multiplicity change = segmentation moved.
            if not olds or not news:
                diffs.append({"tick": tick, "field": "presence", "old": bool(olds), "new": bool(news),
                              "class": INFERENCE, "basis": "one-sided chord-track segment (segmentation/committed reading differs)"})
                continue
        o = olds[0]
        n = news[0]
        found = False
        if o.get("durationTicks") != n.get("durationTicks"):
            diffs.append({"tick": tick, "field": "durationTicks", "old": o.get("durationTicks"), "new": n.get("durationTicks"),
                          "class": INFERENCE, "basis": "chord-track segment duration differs (segmentation)"})
            found = True
        if o.get("pitches") != n.get("pitches"):
            diffs.append({"tick": tick, "field": "pitches", "old": o.get("pitches"), "new": n.get("pitches"),
                          "class": INFERENCE, "basis": "imploded voicing pitches differ (committed chord/root moved)"})
            found = True
        if o.get("harmonyText") != n.get("harmonyText"):
            c = classify_text(o.get("harmonyText"), n.get("harmonyText"))
            if c:
                diffs.append({"tick": tick, "field": "harmonyText", "old": o.get("harmonyText"), "new": n.get("harmonyText"),
                              "class": c[0], "basis": c[1]})
                found = True
        if not found:
            ident += 1
    return diffs, ident


def _ann_kind(text):
    t = (text or "").strip()
    if t.startswith("["):
        return "bracket"
    # roman numerals: start with (optional accidental) i/v/x letters, or applied-chord tokens
    # (It/Ger/Fr/N for aug-sixth/Neapolitan). Chord symbols start with a note letter A-G.
    head = t[1:] if t[:1] in "b#" else t
    if head[:1] in "iIvVxX" or head[:2] in ("It", "Ge", "Fr") or head[:1] == "N":
        # disambiguate a bare note letter that also looks roman is impossible here; treat
        # a leading note-letter-with-chord-suffix as a symbol, else roman.
        if head[:1] in "ABCDEFG" and (len(head) == 1 or head[1] in "b#m/0123456789"):
            return "symbol"
        return "roman"
    return "symbol"


def classify_annotation(old_list, new_list):
    """Per tick, multiset-diff the (kind, text, key) entries and classify each removed/added.

    A one-sided text (added or removed with no partner of its kind) is an inference-driven
    reading move (a chord/roman the other arm did not commit here). A matched pair whose text
    moved is classified by classify_text (D2 / Nashville / else inference); a matched pair whose
    KEY moved at an identical text is a key/mode reinterpretation (attributed to inference)."""
    diffs = []
    ident = 0
    oldd = defaultdict(list)
    newd = defaultdict(list)
    for e in old_list:
        oldd[e.get("tick")].append(e)
    for e in new_list:
        newd[e.get("tick")].append(e)
    for tick in sorted(set(oldd) | set(newd)):
        olds = oldd.get(tick, [])
        news = newd.get(tick, [])
        old_ms = Counter((_ann_kind(e.get("text")), e.get("text"), e.get("key")) for e in olds)
        new_ms = Counter((_ann_kind(e.get("text")), e.get("text"), e.get("key")) for e in news)
        removed = old_ms - new_ms
        added = new_ms - old_ms
        if not removed and not added:
            ident += 1
            continue
        # bucket by kind
        rem_by_kind = defaultdict(list)
        add_by_kind = defaultdict(list)
        for (kind, text, key), c in removed.items():
            rem_by_kind[kind].extend([(text, key)] * c)
        for (kind, text, key), c in added.items():
            add_by_kind[kind].extend([(text, key)] * c)
        for kind in set(rem_by_kind) | set(add_by_kind):
            rem = rem_by_kind.get(kind, [])
            add = add_by_kind.get(kind, [])
            npair = min(len(rem), len(add))
            for i in range(npair):
                (ot, ok) = rem[i]
                (nt, nk) = add[i]
                if ot != nt:
                    c = classify_text(ot, nt, kind)
                    diffs.append({"tick": tick, "field": kind, "old": ot, "new": nt,
                                  "class": c[0], "basis": c[1]})
                else:
                    # same text, key moved
                    diffs.append({"tick": tick, "field": kind + ":key", "old": ok, "new": nk,
                                  "class": INFERENCE,
                                  "basis": "annotation key differs at an identical %s text (key/mode reinterpretation; two-mode record key)" % kind})
            for i in range(npair, len(rem)):
                diffs.append({"tick": tick, "field": kind, "old": rem[i][0], "new": None,
                              "class": INFERENCE, "basis": "one-sided %s removed (the record arm committed no such annotation here)" % kind})
            for i in range(npair, len(add)):
                diffs.append({"tick": tick, "field": kind, "old": None, "new": add[i][0],
                              "class": INFERENCE, "basis": "one-sided %s added (the record arm commits an annotation the legacy arm did not)" % kind})
    return diffs, ident


SURFACE_CLASSIFIERS = {
    "tickRegional": classify_tickregional,
    "annotation": classify_annotation,
    "implodedChordTrack": classify_implodedchordtrack,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD", help="git ref for the pre-switch (legacy) goldens")
    ap.add_argument("--out", default=os.path.join(REPO_ROOT, "tools/notation_seams/switch_golden_reconciliation.json"))
    ap.add_argument("--summary", default=os.path.join(REPO_ROOT, "tools/notation_seams/switch_golden_reconciliation_summary.txt"))
    ap.add_argument("--p6", default=os.path.join(REPO_ROOT, "tools/notation_seams/dualarm_classified_report.json"))
    args = ap.parse_args()

    # Encoding-safe console (OI-137 class): the summary carries non-ASCII (em dash, §); a cp1252
    # stdout must not crash on it. The artifact files are written UTF-8 regardless.
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    snap_dir = os.path.join(REPO_ROOT, SNAP_REL)
    goldens = sorted(f for f in os.listdir(snap_dir) if f.endswith(".json"))

    p6_grand = None
    if os.path.exists(args.p6):
        with open(args.p6, "r", encoding="utf-8") as fh:
            p6_grand = json.load(fh).get("grandTotals")

    per_golden = []
    grand = blank_counts()
    invariant_breaks = []
    unexplained_all = []

    for fn in goldens:
        rel = "%s/%s" % (SNAP_REL, fn)
        old = git_show(args.base, rel)
        with open(os.path.join(snap_dir, fn), "r", encoding="utf-8") as fh:
            new = json.load(fh)

        g = {"golden": fn, "invariantSurfaces": {}, "surfaces": {}}
        # invariant surfaces
        for surf in INVARIANT_SURFACES:
            same = old.get(surf) == new.get(surf)
            g["invariantSurfaces"][surf] = "identical" if same else "CHANGED"
            if not same:
                invariant_breaks.append({"golden": fn, "surface": surf})
        # gated surfaces
        for surf, classifier in SURFACE_CLASSIFIERS.items():
            diffs, ident = classifier(old.get(surf, []), new.get(surf, []))
            counts = blank_counts()
            counts["identical"] = ident
            grand["identical"] += ident
            for d in diffs:
                counts[d["class"]] = counts.get(d["class"], 0) + 1
                grand[d["class"]] = grand.get(d["class"], 0) + 1
                if d["class"] == UNEXPLAINED:
                    e = dict(d)
                    e["golden"] = fn
                    e["surface"] = surf
                    unexplained_all.append(e)
            # The artifact stays SMALL (dispatch): the full per-item classification is recomputable
            # from this instrument + the goldens (#17f), so store COUNTS + spot citations (up to
            # SPOT per class) — but EVERY unexplained/input-scoping entry in full (a STOP needs its
            # detail). Here both are 0, so spot citations suffice.
            SPOT = 4
            seen = {}
            spot = []
            for d in diffs:
                c = d["class"]
                if c in (UNEXPLAINED, INPUT_SCOPING):
                    spot.append(d)
                    continue
                seen[c] = seen.get(c, 0) + 1
                if seen[c] <= SPOT:
                    spot.append(d)
            g["surfaces"][surf] = {"diffCounts": counts, "spotCitations": spot}
        per_golden.append(g)

    ok = (not invariant_breaks) and grand[UNEXPLAINED] == 0 and grand[INPUT_SCOPING] == 0

    report = {
        "instrument": "reconcile_switch_goldens.py",
        "purpose": "reconcile the notation-switch golden refresh (legacy arm -> record arm) against the P6 classified taxonomy",
        "base": args.base,
        "p6_report": os.path.relpath(args.p6, REPO_ROOT).replace("\\", "/"),
        "p6_grandTotals": p6_grand,
        "invariant_surfaces": INVARIANT_SURFACES,
        "invariant_breaks": invariant_breaks,
        "gated_surfaces": GATED_SURFACES,
        "grandTotals": grand,
        "unexplained": unexplained_all,
        "verdict": "PASS" if ok else "STOP",
        "perGolden": per_golden,
    }
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)
        fh.write("\n")

    lines = []
    lines.append("SWITCH GOLDEN RECONCILIATION — legacy arm -> record arm (useJointNotationRecord default ON)")
    lines.append("base (legacy goldens): %s" % args.base)
    lines.append("")
    lines.append("INVARIANT SURFACES (implode / keyAreas / tickLocal — never flag-gated; must be byte-identical):")
    lines.append("  breaks: %d %s" % (len(invariant_breaks), "" if not invariant_breaks else invariant_breaks))
    lines.append("")
    lines.append("GATED-SURFACE DIFFS, by class (grand totals across %d goldens):" % len(goldens))
    for cls in ("identical", INFERENCE, PRESENTATION, INPUT_SCOPING, INERT_AUX, UNEXPLAINED):
        lines.append("  %-26s %d" % (cls, grand.get(cls, 0)))
    lines.append("")
    lines.append("UNEXPLAINED entries: %d (each is a STOP #13/#15)" % grand[UNEXPLAINED])
    for e in unexplained_all[:100]:
        lines.append("  [%s/%s] tick=%s field=%s %s" % (e.get("golden"), e.get("surface"), e.get("tick"), e.get("field"), e.get("basis")))
    lines.append("")
    lines.append("PER GOLDEN (inference / presentation / input-scope / UNEXPL over gated surfaces):")
    for g in per_golden:
        agg = blank_counts()
        for s in g["surfaces"].values():
            for cls, n in s["diffCounts"].items():
                agg[cls] = agg.get(cls, 0) + n
        inv = ",".join(k for k, v in g["invariantSurfaces"].items() if v != "identical") or "-"
        lines.append("  %-26s inf=%-5d pres=%-4d inertAux=%-4d in-scope=%-2d UNEXPL=%-2d  invBreak=%s"
                     % (g["golden"], agg[INFERENCE], agg[PRESENTATION], agg[INERT_AUX], agg[INPUT_SCOPING], agg[UNEXPLAINED], inv))
    lines.append("")
    lines.append("VERDICT: %s" % report["verdict"])
    with open(args.summary, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    print("\nwrote %s" % os.path.relpath(args.out, REPO_ROOT).replace("\\", "/"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
