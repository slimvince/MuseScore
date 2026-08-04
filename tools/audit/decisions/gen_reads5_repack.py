#!/usr/bin/env python3
"""READ WAVE 5's RE-PACK of the reading regime, and the finding that forced it.

WHAT THIS IS.  The user ruled on 2026-08-04 that the reading regime be re-packed so that a wave
SPANS length terciles rather than falling inside one, and that the predicted yield bands be
RE-REGISTERED for the re-packed waves before any of them is read (#17b).  This artifact is that
re-pack and that re-registration.

WHY THE REGIME ARTIFACT IS NOT REGENERATED, AND WHY THAT IS NOT A DODGE.  The re-pack was to be
made in `gen_phase1n_reading_regime.py`, and the packing RULE is: that generator owns
`stratified_repack`, which this file imports rather than copying (#6).  What could not be done
there is RUNNING it.  The regime artifact is a REGISTRATION -- an ordering, a band per document
and a wave schedule, all recorded before the reads they govern -- and re-deriving it today does
not reproduce it, for a reason this file measures rather than asserts:

  * the ORDERING KEY is whichever proxy correlates best with yield on the 36 already-read
    documents;
  * one of the four candidate proxies is `named_in_a_user_ratified_surface_count`;
  * writing a delegation into a user-ratified surface -- which is exactly what the register's own
    homing work has been doing, six documents on 2026-08-03 and three more on 2026-08-04 --
    INCREMENTS that proxy for documents whose yield is already known.

So the project's own recording acts edit a feature the proxy is graded on (#20), and the measured
consequence is below.  Re-deriving the schedule would silently re-order all 66 owed documents by a
different key and destroy the record of which documents each completed wave read (#12).  The
regime generator now STOPS instead, loudly, with that reason; this file applies the re-pack to the
REGISTERED rows, read verbatim.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : nothing about the schedule.  The ruling text, and the prose naming what the finding
             is -- both imported from the regime generator, where the rule lives.
  derived  : which documents are already read (from each completed wave's own yield artifact);
             the remainder; the wave count; the dealing; every band and point (read VERBATIM off
             the registration, never recomputed); the tercile composition of every wave, completed
             and re-packed; and the correlation measurement above.

Run:  python tools/audit/decisions/gen_reads5_repack.py [--check]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
REGIME = os.path.join(HERE, "phase1n_reading_regime.json")
BACKBONE = os.path.join(HERE, "backbone_decisions.json")
OUT = os.path.join(HERE, "reads5_repack.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

import gen_phase1n_reading_regime as regime_gen  # noqa: E402
import gen_phase1m_measurements as p1m           # noqa: E402

COMPLETED_YIELD_ARTIFACTS = [f"reads{i}_yield.json" for i in (1, 2, 3, 4)]

RULING = (
    "User, 2026-08-04 (READ WAVE 5, dispatch `cc_instruction_reads_5.md` §0a ruling R5): re-pack "
    "the reading regime so a wave SPANS length terciles, and re-register the predicted bands for "
    "the re-packed waves BEFORE any of them is read. The existing bands were registered against "
    "the old ordering and may not be reused as they stand — grading a re-packed wave against a "
    "prediction made for a different grouping grades it against a prediction never made about it.")


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def measure_the_proxy_contamination(regime: dict) -> dict:
    """The measurement this file's own premise rests on, computed here so it is reproducible
    (#17f, D-431): re-derive the four proxy correlations on today's files and report whether the
    registered ordering key still wins."""
    backbone = load(BACKBONE)
    unresolved, _surface = p1m.unresolved_by_file()
    homed: dict[str, int] = {}
    for d in backbone["decisions"]:
        doc = d["home"].split(":")[0].replace("\\", "/")
        homed[doc] = homed.get(doc, 0) + 1
    read_docs = [r["document"] for r in regime["read_rows"]]

    def named_now(doc: str) -> int:
        base = doc.split("/")[-1]
        n = 0
        for s in p1m.RATIFIED_SURFACES:
            with open(os.path.join(ROOT, s), encoding="utf-8", errors="replace") as fh:
                for line in fh.read().splitlines():
                    if base in line:
                        n += 1
        return n

    rows = [{"document": d, "lines": p1m.file_facts(d)["lines"], "named": named_now(d),
             "unres": unresolved.get(d, 0), "yield": homed.get(d, 0)} for d in read_docs]
    ys = [float(r["yield"]) for r in rows]
    proxies = {
        "document_length_lines": [float(r["lines"]) for r in rows],
        "unresolved_cluster_count": [float(r["unres"]) for r in rows],
        "named_in_a_user_ratified_surface_count": [float(r["named"]) for r in rows],
        "named_in_a_user_ratified_surface_boolean": [1.0 if r["named"] else 0.0 for r in rows],
    }
    registered = regime["proxy"]["correlations_with_yield_on_the_read_set"]
    now = {}
    for name, xs in proxies.items():
        rho = round(regime_gen.spearman(xs, ys, "average"), 4)
        was = registered[name]["spearman_rho_average_ties"]
        now[name] = {"registered": was, "recomputed_2026_08_04": rho,
                     "moved_by": round(rho - was, 4),
                     "ci95_registered": registered[name]["ci95_on_the_average_ties_figure"]}
    winner = max(now, key=lambda k: now[k]["recomputed_2026_08_04"])
    registered_key = regime["proxy"]["strongest"]
    moved_docs = [r["document"] for r in rows
                  if r["named"] != next(x["named_in_ratified_surfaces"]
                                        for x in regime["read_rows"]
                                        if x["document"] == r["document"])]
    return {
        "what_is_measured": (
            "Whether the regime's registered ORDERING KEY — the proxy with the highest measured "
            "correlation with yield on the 36 read documents — is still the winner when the "
            "correlations are recomputed against the files as they stand today."),
        "registered_ordering_key": registered_key,
        "recomputed_winner": winner,
        "the_key_flips_if_the_regime_is_regenerated": winner != registered_key,
        "per_proxy": now,
        "read_documents_whose_naming_count_moved_since_registration": moved_docs,
        "why_it_moved": (
            "Delegations WRITTEN INTO USER-RATIFIED SURFACES. `named_in_a_user_ratified_surface_"
            "count` counts the lines of `ARCHITECTURE.md`, `CLAUDE.md` and "
            "`cowork_engage_arc_plan.md` that name a document. The user wrote six delegations on "
            "2026-08-03 (the OI-293 write list) and three more on 2026-08-04 (OI-327), and each "
            "one increments that count for the document it names."),
        "why_this_is_a_defect_and_not_a_curiosity": (
            "The register's own homing work EDITS A FEATURE THE PROXY IS GRADED ON, for documents "
            "whose yield is already known. That is the fit/evaluation separation #20 forbids, "
            "arriving by a route nobody designed: the feature is not being tuned, it is being "
            "moved by unrelated correct work. And the margin is far inside the uncertainty the "
            "regime artifact itself records for these figures, so under #24 the flip is not even "
            "a finding about which proxy is better — it is a coin landing the other way. What "
            "makes it consequential is that the ordering key is read off that coin, and the whole "
            "reading order, the wave schedule and the record of what each completed wave read "
            "hang from it."),
    }


def build() -> dict:
    regime = load(REGIME)
    owed = {r["document"]: r for r in regime["owed_rows"]}
    anchor_tokens = regime["schedule"]["capacity_anchor"]["est_tokens"]

    # ── which documents are already read, from each wave's own yield artifact ──
    completed, done = [], set()
    for i, name in enumerate(COMPLETED_YIELD_ARTIFACTS, 1):
        art = load(os.path.join(HERE, name))
        docs = sorted(r["document"] for r in art["rows"])
        planned = sorted(regime["schedule"]["waves"][i - 1]["documents"])
        completed.append({
            "wave": i,
            "yield_artifact": name,
            "documents_read": len(docs),
            "matches_the_registered_packing": docs == planned,
            "length_terciles": sorted({owed[d]["length_tercile"] for d in docs}),
            "documents_per_tercile": {t: sum(1 for d in docs if owed[d]["length_tercile"] == t)
                                      for t in sorted({owed[d]["length_tercile"] for d in docs})},
            "register_entries_produced": art["counts"]["register_entries_produced"],
        })
        done |= set(docs)

    remaining = sorted((owed[d] for d in owed if d not in done),
                       key=lambda r: r["reading_order"])
    terciles_remaining = sorted({r["length_tercile"] for r in remaining})
    dealt, n_waves = regime_gen.stratified_repack(remaining, anchor_tokens)

    repacked = []
    for j, group in enumerate(dealt):
        per_t = {t: [r for r in group if r["length_tercile"] == t] for t in terciles_remaining}
        repacked.append({
            "wave": len(completed) + j + 1,
            "packing": "stratified round-robin over the length terciles still owed",
            "documents": [r["document"] for r in group],
            "document_count": len(group),
            "est_tokens": sum(r["est_tokens"] for r in group),
            "fits_the_measured_capacity": sum(r["est_tokens"] for r in group) <= anchor_tokens,
            "length_terciles": sorted({r["length_tercile"] for r in group}),
            "documents_per_tercile": {t: len(v) for t, v in per_t.items()},
            "registered_bands": [
                {"document": r["document"], "reading_order": r["reading_order"],
                 "lines": r["lines"], "est_tokens": r["est_tokens"],
                 "length_tercile": r["length_tercile"],
                 "predicted_yield_band": r["predicted_yield_band"],
                 "predicted_yield_point": r["predicted_yield_point"]} for r in group],
            "the_discriminating_prediction": {
                "registered": "2026-08-04, before any document of this wave is read (#17b)",
                "claim": (
                    "This wave spans more than one length tercile, so the proxy makes DIFFERENT "
                    "predictions inside it and the ordering between them is falsifiable within a "
                    "single wave — the comparison the previous packing could not produce. The "
                    "registered claim: the mean measured yield of this wave's documents, grouped "
                    "by tercile, falls in the same order as the point predictions below."),
                "point_prediction_per_tercile": {
                    t: (v[0]["predicted_yield_point"] if v else None) for t, v in per_t.items()},
                "documents_per_tercile": {t: len(v) for t, v in per_t.items()},
                "what_would_falsify_it": (
                    "A wave in which the shorter-tercile documents out-yield the longer-tercile "
                    "ones. That is a RESULT, not a defect, and it is the first real test the "
                    "proxy has had."),
            },
        })

    return {
        "header": {
            "purpose": "READ WAVE 5's re-pack of the reading regime, with the predicted bands "
                       "re-registered for the re-packed waves before any of them is read, and "
                       "the finding that forced the re-pack.",
            "generator": "tools/audit/decisions/gen_reads5_repack.py",
            "ruling": RULING,
            "the_packing_rule_lives_in":
                "tools/audit/decisions/gen_phase1n_reading_regime.py -> stratified_repack(), "
                "imported here rather than copied (#6).",
            "authored_inputs": ["nothing about the schedule; the ruling text, and the prose "
                                "naming the finding, which is imported from the regime generator"],
            "derived_from": ["phase1n_reading_regime.json (the REGISTRATION: every ordering, "
                             "band, point and tercile, read verbatim and never recomputed)",
                             "reads1..reads4_yield.json (which documents each completed wave "
                             "actually read)",
                             "backbone_decisions.json + the three user-ratified surfaces (the "
                             "contamination measurement only)"],
        },
        "why_the_re_pack": {
            "the_finding": regime_gen.REPACK_WHY,
            "the_rule": regime_gen.REPACK_RULE,
            "what_changed_and_what_did_not": (
                "CHANGED: the grouping of the documents still owed. UNCHANGED: which documents "
                "are read — all of them, `no_tail_is_bounded` is untouched — the ordering key, "
                "the tercile cuts, every per-document band and point, the read set those bands "
                "are fitted on, and the measured capacity anchor."),
            "the_evidence_in_the_completed_waves": (
                "Below, per completed wave: the length terciles it actually spanned. Waves 2, 3 "
                "and 4 each span exactly one, which is what the ruling was made on."),
        },
        "why_the_regime_artifact_is_read_and_not_regenerated":
            measure_the_proxy_contamination(regime),
        "completed_waves": completed,
        "the_remainder": {
            "documents": len(remaining),
            "est_tokens": sum(r["est_tokens"] for r in remaining),
            "length_terciles_still_owed": terciles_remaining,
            "documents_per_tercile": {
                t: sum(1 for r in remaining if r["length_tercile"] == t)
                for t in terciles_remaining},
            "the_constraint_this_re_pack_ran_into": (
                "MEASURED AND REPORTED RATHER THAN WORKED AROUND: only the terciles listed above "
                "are still owed. Every LONG-tercile document has already been read — the ordering "
                "is length-descending, so the longest went first — and none remains to deal into "
                "a wave. A re-packed wave can therefore span the terciles that remain and no "
                "more, which is the strongest form of the ruling this population admits. Stated "
                "so it is not overclaimed: the discriminating comparison these waves can make is "
                "between the terciles listed above, not across the proxy's whole range, and a "
                "pass establishes correspondingly less."),
            "wave_count_derived": n_waves,
            "how_the_wave_count_was_derived":
                "ceil(remaining est_tokens / the anchor wave's measured est_tokens).",
        },
        "repacked_waves": repacked,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="rebuild into memory and report whether the artifact matches")
    args = ap.parse_args()

    built = build()
    if args.check:
        if not os.path.exists(OUT):
            print("STALE: the artifact does not exist")
            return 1
        if load(OUT) != built:
            print("STALE: reads5_repack.json does not re-derive")
            return 1
        print("reads5_repack.json re-derives")
        return 0

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(built, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    rem = built["the_remainder"]
    print(f"remaining owed: {rem['documents']} documents / {rem['est_tokens']} est tokens; "
          f"terciles still owed: {', '.join(rem['length_terciles_still_owed'])}")
    for w in built["repacked_waves"]:
        print(f"  wave {w['wave']}: {w['document_count']} docs, {w['est_tokens']} tok, "
              f"terciles {w['documents_per_tercile']}")
    c = built["why_the_regime_artifact_is_read_and_not_regenerated"]
    print(f"ordering key flips if the regime is regenerated: "
          f"{c['the_key_flips_if_the_regime_is_regenerated']} "
          f"({c['registered_ordering_key']} -> {c['recomputed_winner']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
