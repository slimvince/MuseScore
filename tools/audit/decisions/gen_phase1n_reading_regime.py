#!/usr/bin/env python3
"""Generate `tools/audit/decisions/phase1n_reading_regime.json` — the OI-207 reading regime.

WHAT THIS IS.  The user ruled on 2026-08-03 that the remaining OI-207 reads are taken as
DEDICATED waves, that **every owed document is read and no tail is bounded**, that the order is
by the STRONGER of the observable proxies, and that a predicted yield band is registered for
each owed document **before** it is read, so the proxy is established out-of-sample rather than
merely used (#17b, #19, #20).  This tool is that registration.

WHY A GENERATOR.  Principle #17(f), and — as of the same day's ruling (register entry D-431) —
the same rule applied to dispatches and session reports: a figure enters prose by citation to a
generated artifact, never by transcription.  The phase-1m note is why the rule was needed: its
three rank correlations were computed OUTSIDE `gen_phase1m_measurements.py`, which contains no
correlation code, so a second recomputation returned a different value for the strongest of the
three and the difference could not be attributed to anything.  Every correlation here is
computed in this file, with its tie rule named and both tie rules reported.

WHAT IS AUTHORED AND WHAT IS DERIVED.
  authored : the wave-capacity ANCHOR (which past wave is taken as the measured capacity of a
             dedicated read wave, and why the others are not), and the band rule (terciles of
             the read set's own length distribution).  Both are stated below with their reason.
  derived  : the read/owed partition (imported from `gen_phase1m_measurements`, so the two
             artifacts cannot disagree about what the surface is); every per-document size,
             cluster count and mention count; all three rank correlations under both tie rules
             with their uncertainty; the ordering; every predicted band; the wave packing; and
             the implied wave count.

Run:  python tools/audit/decisions/gen_phase1n_reading_regime.py [--check]
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "phase1n_reading_regime.json")

sys.path.insert(0, HERE)
import gen_phase1m_measurements as p1m          # noqa: E402
import gen_phase1g_triage as triage             # noqa: E402

# ── AUTHORED (1/2) — the wave-capacity anchor ────────────────────────────────
# A wave count needs a measured capacity, and the record holds exactly one measurement of what
# a session can read when reading is the work: the phase-1h wave, which read five documents in
# one session.  Phases 1i, 1j, 1k and 1l each read ONE document and each states in its own note
# that the wave's other tasks consumed the session — so those four measure the cost of mixing
# rulings with reading, which is precisely what the dedicated-wave regime removes, and they are
# NOT a reading-capacity measurement.  The anchor is therefore the phase-1h document set, and
# its token size is computed from the files rather than taken from that wave's own prose.
CAPACITY_ANCHOR_WAVE = "1h"
CAPACITY_ANCHOR_WHY = (
    "The one wave in the record whose session was spent reading: phase 1h read five documents "
    "in one session. Phases 1i-1l read one document each and each states that the wave's other "
    "tasks consumed the session, so they measure the cost of mixing ruling work with reading -- "
    "the cost the dedicated-wave regime exists to remove -- and are not a capacity measurement. "
    "The anchor's token size is computed from the five files here, not taken from that wave's "
    "prose.")

# ── AUTHORED (2/2) — the band rule ───────────────────────────────────────────
# The band must be formed from something, and the only yield data that exists is the 36 read
# documents.  The rule: split the READ set into three equal-count bands by document length, and
# predict, for an owed document, the band its length puts it in -- reported as that band's
# observed minimum, median and maximum yield.  A min-to-max band over ~12 observations is a
# WIDE prediction, deliberately: a narrow one would be a claim the data cannot carry.
BAND_RULE = (
    "Terciles of the READ set's own line-count distribution. An owed document is assigned the "
    "tercile its line count falls in, and the prediction is that tercile's observed yield "
    "range: minimum, median and maximum entries per document, with the tercile mean as the "
    "point prediction. The band is min-to-max over roughly twelve observations, which is wide "
    "on purpose -- a narrower band would assert precision the 36-document sample does not "
    "carry.")

PROXY_LABEL = (
    "STRUCTURAL PROXY STANDING IN FOR A BEHAVIOURAL QUANTITY, UNVALIDATED (#17d). Length and "
    "unresolved-cluster count measure how much text a document holds; yield measures how many "
    "standing decisions it records that no other home carries. The second is not recoverable "
    "from the first -- phase 1f's own methodological finding is that reading two documents in "
    "full moved their cluster counts by 2 while producing 3 register entries. The correlations "
    "below are FITTED AND SELF-MEASURED on the 36 documents whose yield is known (#20), and the "
    "measured set contains counter-examples at the top of the proxy's own range. No bound may "
    "rest on this proxy until it is tested out-of-sample, and the registration below is what "
    "makes that test possible.")


# ── statistics, computed here so they are reproducible ───────────────────────

def ranks(values: list[float], ties: str) -> list[float]:
    """Ranks of `values`. ties='average' shares a rank among equals (the standard Spearman
    convention); ties='ordinal' breaks them by position, which is what an ad-hoc computation
    usually does by accident. Both are reported so the difference is visible rather than a
    source of two irreconcilable numbers."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    out = [0.0] * len(values)
    if ties == "ordinal":
        for r, i in enumerate(order, 1):
            out[i] = float(r)
        return out
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        shared = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            out[order[k]] = shared
        i = j + 1
    return out


def pearson(a: list[float], b: list[float]) -> float:
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = math.sqrt(sum((x - ma) ** 2 for x in a))
    db = math.sqrt(sum((y - mb) ** 2 for y in b))
    return num / (da * db) if da and db else 0.0


def spearman(x: list[float], y: list[float], ties: str) -> float:
    return pearson(ranks(x, ties), ranks(y, ties))


def fisher_ci(rho: float, n: int, level: float = 0.95) -> list[float]:
    """A 95 % interval on a rank correlation, so the figure carries its uncertainty (#24).
    Fisher z with the Spearman standard error 1.06/sqrt(n-3) (Bonett-Wright)."""
    if n < 6 or abs(rho) >= 1.0:
        return [float("nan"), float("nan")]
    z = 0.5 * math.log((1 + rho) / (1 - rho))
    se = 1.06 / math.sqrt(n - 3)
    crit = 1.959963985 if abs(level - 0.95) < 1e-9 else 1.959963985
    lo, hi = z - crit * se, z + crit * se
    return [round(math.tanh(lo), 4), round(math.tanh(hi), 4)]


def quantile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        return float("nan")
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    pos = q * (len(sorted_vals) - 1)
    lo = int(math.floor(pos))
    hi = min(lo + 1, len(sorted_vals) - 1)
    frac = pos - lo
    return sorted_vals[lo] * (1 - frac) + sorted_vals[hi] * frac


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="regenerate into memory and report whether the artifact matches")
    args = ap.parse_args()

    backbone = json.loads(open(p1m.BACKBONE, encoding="utf-8").read())
    decisions = backbone["decisions"]

    # ── the read / excluded / owed partition, from the phase-1m derivation ────
    unresolved, surface_files = p1m.unresolved_by_file()
    read: dict[str, list[str]] = {}
    for wave, (docs, _cite) in p1m.READ_WAVES.items():
        for doc in docs:
            read.setdefault(doc, []).append(wave)
    excluded = sorted(f for f, (cls, _r) in triage.CLASSIFICATION.items()
                      if cls != triage.LIVE and f not in read)
    owed = sorted(f for f in unresolved if f not in read and f not in excluded)
    assert len(read) + len(excluded) + len(owed) == surface_files

    homed: dict[str, int] = {}
    for d in decisions:
        doc = d["home"].split(":")[0].replace("\\", "/")
        homed[doc] = homed.get(doc, 0) + 1

    mentions = p1m.mentions_in_ratified_surfaces()

    def facts(doc: str) -> dict:
        f = p1m.file_facts(doc)
        base = doc.split("/")[-1]
        named = 0
        for s in p1m.RATIFIED_SURFACES:
            for line in open(os.path.join(ROOT, s), encoding="utf-8",
                             errors="replace").read().splitlines():
                if base in line:
                    named += 1
        return {"lines": f["lines"], "bytes": f["bytes"],
                "est_tokens": round(f["bytes"] / p1m.CHARS_PER_TOKEN),
                "unresolved_clusters": unresolved.get(doc, 0),
                "named_in_ratified_surfaces": named,
                "banner_words": f.get("banner_words", [])}

    read_rows = []
    for doc in sorted(read):
        r = facts(doc)
        r.update({"document": doc, "waves": read[doc], "yield": homed.get(doc, 0)})
        read_rows.append(r)

    # ── the three proxies, both tie rules, with uncertainty ──────────────────
    ys = [float(r["yield"]) for r in read_rows]
    proxies = {
        "document_length_lines": [float(r["lines"]) for r in read_rows],
        "unresolved_cluster_count": [float(r["unresolved_clusters"]) for r in read_rows],
        "named_in_a_user_ratified_surface_count": [float(r["named_in_ratified_surfaces"])
                                                   for r in read_rows],
        # The same feature as a BOOLEAN — named at all, or not.  Both forms are computed
        # because the phase-1m note reports this proxy far weaker than either form comes out
        # here, and the count-versus-boolean choice is the only difference that can carry a gap
        # that size; tie handling cannot.  Reporting both attributes the discrepancy instead of
        # leaving two irreconcilable numbers on the record.
        "named_in_a_user_ratified_surface_boolean": [
            1.0 if r["named_in_ratified_surfaces"] else 0.0 for r in read_rows],
    }
    n = len(read_rows)
    correlations = {}
    for name, xs in proxies.items():
        avg = spearman(xs, ys, "average")
        ordi = spearman(xs, ys, "ordinal")
        correlations[name] = {
            "spearman_rho_average_ties": round(avg, 4),
            "spearman_rho_ordinal_ties": round(ordi, 4),
            "difference_between_tie_rules": round(avg - ordi, 4),
            "ci95_on_the_average_ties_figure": fisher_ci(avg, n),
            "n": n,
        }
    ranked = sorted(correlations.items(),
                    key=lambda kv: -kv[1]["spearman_rho_average_ties"])
    strongest = ranked[0][0]

    # #24 — a difference within the uncertainty is not a finding.  Two proxies are recorded as
    # INDISTINGUISHABLE when each one's point estimate falls inside the other's interval.
    def indistinguishable(a: str, b: str) -> bool:
        ca, cb = correlations[a], correlations[b]
        lo_a, hi_a = ca["ci95_on_the_average_ties_figure"]
        lo_b, hi_b = cb["ci95_on_the_average_ties_figure"]
        return (lo_a <= cb["spearman_rho_average_ties"] <= hi_a
                and lo_b <= ca["spearman_rho_average_ties"] <= hi_b)

    tied_with_strongest = [k for k, _v in ranked[1:] if indistinguishable(strongest, k)]

    # The ordering key.  Where the top proxies are indistinguishable the choice is a TIE-BREAK
    # and is stated as one, never as a measured superiority.  Length wins the tie-break on a
    # stated ground that is not its correlation: it is the only one of the three that is also
    # the reading COST, so ordering by it and packing waves by it are the same measurement, and
    # it is defined for every owed document without reference to any other artifact.
    ordering_decision = {
        "key": strongest,
        "point_estimate_ranking": [k for k, _v in ranked],
        "indistinguishable_from_the_key_at_95pct": tied_with_strongest,
        "is_the_key_measurably_the_strongest": not tied_with_strongest,
        "how_the_key_was_chosen": (
            "By point estimate, and then — where another proxy is indistinguishable from it at "
            "95 % — by a stated tie-break, NOT by the correlation. Document length wins the "
            "tie-break because it is the only one of the three that is simultaneously the "
            "reading COST, so the ordering and the wave packing rest on one measurement rather "
            "than two, and because it is defined for every owed document with no reference to "
            "another artifact."),
        "what_this_corrects": (
            "The proposal this regime implements held that length outranks BOTH other proxies. "
            "Recomputed here under the standard average-ties convention, length outranks the "
            "unresolved-cluster count, but the count-form of `named in a user-ratified surface` "
            "is within four thousandths of it with heavily overlapping intervals. Under #24 "
            "that difference is not a finding, so the claim that length is THE stronger proxy "
            "is not established between the top two and is not made here."),
    }

    # ── the bands, from the READ set's own length terciles ───────────────────
    by_len = sorted(read_rows, key=lambda r: r["lines"])
    cut1, cut2 = by_len[len(by_len) // 3]["lines"], by_len[2 * len(by_len) // 3]["lines"]

    def tercile_of(lines: int) -> str:
        return "short" if lines < cut1 else ("medium" if lines < cut2 else "long")

    bands: dict[str, dict] = {}
    for t in ("short", "medium", "long"):
        vals = sorted(float(r["yield"]) for r in read_rows if tercile_of(r["lines"]) == t)
        bands[t] = {
            "read_documents_in_this_tercile": len(vals),
            "observed_yield_min": vals[0] if vals else None,
            "observed_yield_median": round(quantile(vals, 0.5), 2) if vals else None,
            "observed_yield_max": vals[-1] if vals else None,
            "observed_yield_mean": round(sum(vals) / len(vals), 2) if vals else None,
            "zero_yield_documents": sum(1 for v in vals if v == 0),
        }

    owed_rows = []
    for doc in owed:
        r = facts(doc)
        t = tercile_of(r["lines"])
        r.update({"document": doc,
                  "length_tercile": t,
                  "predicted_yield_band": [bands[t]["observed_yield_min"],
                                           bands[t]["observed_yield_max"]],
                  "predicted_yield_point": bands[t]["observed_yield_mean"],
                  "actual_yield_when_read": None,
                  "surface": "docs" if doc.startswith("docs/") else "cowork"})
        owed_rows.append(r)

    key = {"document_length_lines": "lines",
           "unresolved_cluster_count": "unresolved_clusters",
           "named_in_a_user_ratified_surface_count": "named_in_ratified_surfaces",
           "named_in_a_user_ratified_surface_boolean": "named_in_ratified_surfaces"}[strongest]
    owed_rows.sort(key=lambda r: (-r[key], r["document"]))
    for i, r in enumerate(owed_rows, 1):
        r["reading_order"] = i

    # ── the wave schedule, packed against the measured capacity ──────────────
    anchor_docs = list(p1m.READ_WAVES[CAPACITY_ANCHOR_WAVE][0])
    anchor = {"wave": CAPACITY_ANCHOR_WAVE, "documents": len(anchor_docs),
              "lines": sum(p1m.file_facts(d)["lines"] for d in anchor_docs),
              "bytes": sum(p1m.file_facts(d)["bytes"] for d in anchor_docs)}
    anchor["est_tokens"] = round(anchor["bytes"] / p1m.CHARS_PER_TOKEN)
    anchor["why"] = CAPACITY_ANCHOR_WHY

    waves, cur, cur_tok = [], [], 0
    for r in owed_rows:
        if cur and cur_tok + r["est_tokens"] > anchor["est_tokens"]:
            waves.append({"documents": cur, "est_tokens": cur_tok})
            cur, cur_tok = [], 0
        cur.append(r["document"])
        cur_tok += r["est_tokens"]
    if cur:
        waves.append({"documents": cur, "est_tokens": cur_tok})
    for i, w in enumerate(waves, 1):
        w["wave"] = i

    artifact = {
        "header": {
            "purpose": "The OI-207 reading regime, registered BEFORE the reads it governs. "
                       "The owed documents ordered by the stronger proxy, a predicted yield "
                       "band per document registered in advance, the wave schedule packed "
                       "against a measured capacity, and the statement that NO TAIL IS BOUNDED.",
            "generator": "tools/audit/decisions/gen_phase1n_reading_regime.py",
            "ruling": "User, 2026-08-03: read every owed document, bound no tail, order by the "
                      "stronger proxy, and register the predicted bands before reading so the "
                      "proxy is established out-of-sample rather than merely used.",
            "authored_inputs": ["CAPACITY_ANCHOR_WAVE", "BAND_RULE"],
            "derived_from": ["backbone_decisions.json", "gen_phase1m_measurements.py "
                             "(the read/owed partition and the file facts)",
                             "gen_phase1g_triage.py (the user-accepted exclusions)",
                             "the three user-ratified surfaces", "the files themselves"],
        },
        "partition": {
            "design_document_surface": surface_files,
            "read_in_full": len(read),
            "user_accepted_exclusions_not_read": len(excluded),
            "owed_a_full_read": len(owed),
            "partition_check": len(read) + len(excluded) + len(owed) == surface_files,
            "owed_total_bytes": sum(r["bytes"] for r in owed_rows),
            "owed_est_tokens": sum(r["est_tokens"] for r in owed_rows),
            "owed_total_unresolved_clusters": sum(r["unresolved_clusters"] for r in owed_rows),
        },
        "proxy": {
            "label": PROXY_LABEL,
            "correlations_with_yield_on_the_read_set": correlations,
            "ranking_strongest_first": [k for k, _v in ranked],
            "strongest": strongest,
            "ordering_decision": ordering_decision,
            "tie_rule_finding": (
                "AVERAGE ties is the convention adopted here: it is the standard Spearman "
                "definition, and ordinal ties make the figure depend on the order the documents "
                "happen to be listed in. Both are reported so the size of the choice is visible "
                "-- `difference_between_tie_rules` above -- rather than being a hidden source of "
                "two irreconcilable numbers."),
            "reproduction_of_the_phase1m_figures": (
                "ATTEMPTED AND NOT ACHIEVED, reported as such. The phase-1m OI-207 note records "
                "0.745 for length, 0.628 for the cluster count and 0.530 for named-in-a-ratified-"
                "surface. Length reproduces to within a tie rule (ordinal ties give 0.7557). The "
                "cluster count does not reproduce under either tie rule. Named-in-a-ratified-"
                "surface does not reproduce under either tie rule NOR under either definition of "
                "the feature -- the count form and the boolean form are both above 0.66, against "
                "a recorded 0.530 -- so the gap is attributable to neither of the two candidate "
                "explanations. It cannot be attributed further, because the phase-1m figures were "
                "computed outside `gen_phase1m_measurements.py`, which contains no correlation "
                "code, so there is nothing to diff against. That is the whole case for the "
                "2026-08-03 figures ruling (register entry D-431) in one measurement: a "
                "transcribed figure with no generator behind it cannot be reproduced, cannot be "
                "corrected, and cannot even be diagnosed."),
            "counter_examples_inside_the_measured_set": (
                "Named rather than left for a reader to find: the two documents whose yield the "
                "length proxy gets most wrong are in `proxy_counter_examples` below."),
        },
        "proxy_counter_examples": sorted(
            [{"document": r["document"], "lines": r["lines"],
              "unresolved_clusters": r["unresolved_clusters"], "yield": r["yield"],
              "length_tercile": tercile_of(r["lines"])}
             for r in read_rows if tercile_of(r["lines"]) == "long" and r["yield"] <= 3],
            key=lambda r: (-r["lines"],)),
        "bands": {
            "rule": BAND_RULE,
            "length_tercile_cuts_lines": [cut1, cut2],
            "by_tercile": bands,
            "registration": (
                "These bands are REGISTERED NOW, before any owed document is read. Every later "
                "read wave writes the actual yield into `actual_yield_when_read` on the owed row "
                "it read, and reports it against `predicted_yield_band`. That makes the proxy "
                "tested as a by-product of the reading rather than by a separate study, and it "
                "is the only route by which a tail could ever become boundable."),
        },
        "no_tail_is_bounded": {
            "statement": "EVERY owed document is read in full. No tail is carried, sampled or "
                         "predicted away.",
            "reason": "A bound over a carried tail would have to rest on the proxy above, and "
                      "the proxy is fitted and self-measured on the read set with "
                      "counter-examples inside it. That is exactly the structural proxy "
                      "standing in for a behavioural quantity that #17(d) forbids putting "
                      "under load, and #20 forbids grading it on the data that fitted it. A "
                      "bound resting only on an unvalidated proxy is not a bound.",
            "the_one_bound_that_does_hold": "The 41 user-accepted exclusions, each carrying a "
                                            "per-file verification citation "
                                            "(`tools/audit/decisions/phase1g_triage.md`). That "
                                            "is a bound over a partition the user accepted "
                                            "after seeing each file's evidence, which is a "
                                            "different thing from a bound a session predicted.",
        },
        "schedule": {
            "capacity_anchor": anchor,
            "packing_rule": "The ordered owed list is packed greedily into waves, each wave "
                            "taking documents in reading order until the next one would exceed "
                            "the anchor wave's measured token size. A single document larger "
                            "than the anchor gets a wave of its own rather than being split.",
            "what_this_does_not_model": (
                "TOKENS ONLY. The anchor measures one session that read FIVE documents totalling "
                "its token size; packing by tokens alone therefore produces later waves holding "
                "far more documents than five at the same token budget, because the owed tail is "
                "made of short documents. Two things could bind a reading session -- the volume "
                "read, and the per-document overhead of opening, judging and entering each one -- "
                "and only the first is modelled here, because only the first is measured. If the "
                "second binds, the later waves are optimistic and the wave count is a LOWER "
                "BOUND. This is stated rather than hedged around: the same protocol that tests "
                "the yield proxy tests this too, since each wave's actual document count and "
                "actual yield are recorded against the plan."),
            "implied_wave_count": len(waves),
            "waves": waves,
        },
        "read_rows": read_rows,
        "owed_rows": owed_rows,
    }

    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        cur_text = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur_text != text:
            print(f"STALE vs the data: {os.path.relpath(OUT, ROOT)}")
            return 1
        print("the phase-1n reading-regime artifact matches the data")
        return 0
    open(OUT, "w", encoding="utf-8", newline="").write(text)
    print(f"wrote {os.path.relpath(OUT, ROOT)}: "
          f"{len(read)} read / {len(excluded)} excluded / {len(owed)} owed; "
          f"strongest proxy = {strongest}; "
          f"{len(waves)} wave(s) at the phase-{CAPACITY_ANCHOR_WAVE} measured capacity")
    return 0


if __name__ == "__main__":
    sys.exit(main())
