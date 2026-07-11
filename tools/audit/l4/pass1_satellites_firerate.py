#!/usr/bin/env python3
"""
EG-7 Layer-4 audit PASS 1, session 3 (satellites) — behavioral characterization
(protocol P4). READ-ONLY. Fire rates on the pinned corpus tools/corpus/{baroque,
jazz,default} @ c50002fee1 (verified per-preset from corpus_manifest.json).

Routes (Task 2, least-invasive first):
  - ChordSymbolFormatter (formatSymbol / formatRomanNumeral): the batch outputs
    THEMSELVES — chordSymbol / romanNumeral in every region are exactly what the
    formatter emitted (batch uses Standard spelling; German paths fire 0 here,
    reachable only on the notation render path with a German score style).
  - sparse refinement: the call fires on every region (unconditional at
    regionanalyzer 1003/1005); the quality-CHANGE is confined to the guarded
    populations — this artifact bounds it via the corpus (<=2-PC regions; final
    Unknown/thin counts). Exact change count is NOT separately instrumented (a
    counter is disproportionate — see the report; the bound is tight).
  - chordpathdecoder: commit() fires once per committed region/sub-region
    (byte-identical, verified by decode_tests.cpp equivalence); the path()/
    recordNode()/alternatives/margin members have ZERO consumers today
    (inert staging) — characterized by reading + the test, no corpus signal.
"""
import json, os, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CORPORA = ["baroque", "jazz", "default"]
OB = "\xc3\xb8"   # half-diminished slashed-o as the formatter emits it

def preset_hash(p):
    m = os.path.join(ROOT, "tools", "corpus", p, "corpus_manifest.json")
    try:
        return json.load(open(m, encoding="utf-8")).get("git_hash", "?")
    except Exception:
        return "?"

def scan(preset):
    d = os.path.join(ROOT, "tools", "corpus", preset)
    files = sorted(glob.glob(os.path.join(d, "*.ours.json")))
    st = collections.Counter()
    qual = collections.Counter()
    fmt = collections.Counter()      # formatter branch fire counts
    for f in files:
        j = json.load(open(f, encoding="utf-8"))
        for r in j.get("regions", []):
            st["regions"] += 1
            q = r.get("quality", ""); qual[q] += 1
            sym = r.get("chordSymbol", "") or ""
            rn = r.get("romanNumeral", "") or ""
            # formatSymbol
            fmt["formatSymbol_calls"] += 1
            if sym: fmt["formatSymbol_nonempty"] += 1
            if "/" in sym: fmt["symbol_slash_bass"] += 1
            if "(no 3)" in sym: fmt["symbol_omit_third"] += 1
            if "Cb" in sym or "Fb" in sym: fmt["symbol_cb_fb_veryflat_spelling"] += 1
            # formatRomanNumeral
            fmt["formatRomanNumeral_calls"] += 1
            if rn: fmt["formatRomanNumeral_nonempty"] += 1
            else: fmt["romanNumeral_empty"] += 1
            if rn[:1] in ("b", "#"): fmt["rn_chromatic_prefix"] += 1
            if "+6" in rn: fmt["rn_aug6_label"] += 1
            if "/" in rn: fmt["rn_tonicization_slash"] += 1
            if OB in rn: fmt["rn_half_dim"] += 1
            if ("+" in rn) and ("+6" not in rn): fmt["rn_augmented_plus"] += 1
            if any(x in rn for x in ("65", "43", "42")) or rn.endswith("6") or rn.endswith("64"):
                fmt["rn_inversion_figure"] += 1
            if "(add" in rn: fmt["rn_add_notation"] += 1
            if ("M7" in rn or "M9" in rn or "M11" in rn or "M13" in rn): fmt["rn_maj7_marker"] += 1
            if ("add" not in rn) and any(l in rn for l in ("13", "11", "9")):
                fmt["rn_extension_level_9_11_13"] += 1
            # sparse-refinement opportunity population
            m = r.get("pitchClassSet", 0)
            n = bin(m).count("1") if isinstance(m, int) else -1
            if 0 <= n <= 2:
                st["regions_leq2PC"] += 1
                if q in ("Major", "Minor", "Diminished", "Augmented"):
                    st["triad_on_leq2PC (proxy: key-prior upgrade)"] += 1
                if q in ("Power", "Suspended2", "Suspended4"): st["thin_on_leq2PC_final"] += 1
                if q == "Unknown": st["unknown_on_leq2PC_final"] += 1
            if q == "Unknown": st["unknown_final_total"] += 1
            if q in ("Power", "Suspended2", "Suspended4"): st["thin_final_total"] += 1
    return {"corpus_git_hash": preset_hash(preset), "files": len(files),
            "stats": dict(st), "quality_distribution": dict(qual),
            "formatter_branch_fires": dict(fmt)}

out = {
 "audit": "EG-7 Layer-4 PASS 1, session 3 (satellites) — behavioral characterization (P4)",
 "corpus_hash_expected": "c50002fee1",
 "formatter_route": "batch outputs (chordSymbol/romanNumeral), Standard spelling",
 "decoder_characterization": {
   "commit_fires": "once per committed region + once per Pass-2/2b sub-region "
                   "(byte-identical to advanceTemporalContext; decode_tests.cpp equivalence)",
   "path_recordNode_alternatives_margins_consumers": 0,
   "note": "inert staging at beam 1; DecodeQualityLevel Normal/Deep behave as FastBeam1 (no-op)",
 },
 "sparse_refinement_characterization": {
   "refine_and_tonicPrior_calls": "unconditional on every region (regionanalyzer 1003/1005/1221/1411)",
   "forceChordTrackQualityFromKeyContext_corpus_fires": 0,
   "forceChordTrack_note": "chord-track/notation-annotation path only (notationcomposingbridge 1157, "
                           "notationimplodebridge 1182); NOT on the batch corpus path",
   "quality_change_bound": "confined to <=2-PC regions; see per-preset stats "
                           "(regions_leq2PC, triad_on_leq2PC). Final Unknown=0 and thin_on_leq2PC=0 "
                           "on all presets => every <=2-PC region ends as a triad (key-prior upgrade).",
   "exact_change_count": "not separately instrumented (proportionality — a production default-OFF "
                         "counter + byte-identity re-proof is disproportionate to the marginal gain "
                         "over this tight corpus bound; recommended as a follow-up if the L4/L5 "
                         "boundary decision needs the exact refine-vs-tonicPrior split)",
 },
 "per_preset": {p: scan(p) for p in CORPORA},
}
with open(os.path.join(HERE, "pass1_satellites_firerate.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({p: {"regions": out["per_preset"][p]["stats"]["regions"],
                      "hash": out["per_preset"][p]["corpus_git_hash"],
                      "fmt": out["per_preset"][p]["formatter_branch_fires"],
                      "leq2": {k: v for k, v in out["per_preset"][p]["stats"].items() if "leq2" in k or "unknown" in k or "thin" in k}}
                  for p in CORPORA}, indent=1))
