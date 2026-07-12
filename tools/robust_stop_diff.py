#!/usr/bin/env python3
"""robust_stop_diff.py — the R10 successor-stop diff (batch->robust handover).

READ-ONLY / DIFF-ONLY. Thin orchestration over the pinned A-8 instrument's outputs
(constraint-10 total-unification: it re-implements NO scoring or comparison logic — it
diffs the run-identity sets and the class-split durations the A-8 instrument already
produced). This is the robust-unit analogue of `characterise_bir_false.py`'s role for
the batch stop.

The R10 successor sandwich a future increment runs:
    # 1. measure the candidate (a8 self-validates grid==oracle on every piece)
    python tools/a8_rebaseline_measure.py --out-dir <cand_out> [--corpus-root <scratch>]
    # 2. diff the candidate vs the committed reference
    python tools/robust_stop_diff.py --candidate <cand_out>

Pass/fail rule (per preset, root respect, variant (b) DCML-only):
  (a) HARD STOP  — class-(b) (pitch-class-decidable-root) root-disagree DURATION must be
                   NON-INCREASING vs the reference. Any preset increasing => FAIL.
  (b) DIAGNOSTIC — the run-level set-diff vs the reference (added/removed runs, each with
                   its two-tier class) is ALWAYS listed. It never fails by itself; it is the
                   mandatory explained-diff the dual-track requires (zero-new-case cannot
                   scale to ~7k runs).
  (c) TRACKED    — class-(a) (symmetric/share-tone coin-flip) root-disagree duration is
                   reported as a delta; a LARGE net increase trips mandatory investigation
                   (the CLAUDE.md guardrail (3) carry-over), but it is not an automatic stop.

Exit code 0 iff every preset passes (a). Non-zero on any class-(b) duration increase.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

_ROOT = Path(__file__).resolve().parent.parent
PRESETS = ["baroque", "jazz", "default"]

# a LARGE class-(a) net increase (ticks) that trips mandatory investigation. Advisory
# threshold only (never an automatic stop) — the CLAUDE.md guardrail-(3) carry-over. A
# quarter-note in this corpus is 480 ticks; 20 quarter-notes ~ a whole piece's worth of
# symmetric-rotation churn moving at once is the "many symmetric sonorities destabilized"
# signal. Tune at R10-b if the user prefers a different tripwire.
CLASS_A_INVESTIGATE_TICKS = 9600


# stem may carry a hyphen (multi-movement stems, e.g. bwv248.33-3), so [\w.\-]+ not [\w.]+
_RUN_RE = re.compile(
    r'([\w.\-]+)@(\d+)\s+\[(\d+),(\d+)\)\s+dur=\s*(\d+)\s+'
    r'our=.*?\((-?\d+)\)\s+->\s+dcml_root=(-?\d+)\s+cls=(\w)')


def parse_runs(path: Path):
    """Return {(stem, start, our_root, dcml_root): (dur, cls)} keyed by run identity.

    Fails loudly (no silent drops) if a non-header, non-blank line does not match the
    run format — a format drift or a new stem pattern must not silently shrink the diff
    base. The first two lines are the enumeration's title + count header."""
    runs = {}
    if not path.exists():
        raise FileNotFoundError(f"missing run enumeration: {path}")
    skipped = []
    for i, ln in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if i < 2 or not ln.strip():          # title + count header, blank lines
            continue
        m = _RUN_RE.match(ln)
        if not m:
            skipped.append(ln)
            continue
        stem, start = m.group(1), int(m.group(2))
        dur, orr, dr, cls = int(m.group(5)), int(m.group(6)), int(m.group(7)), m.group(8)
        runs[(stem, start, orr, dr)] = (dur, cls)
    if skipped:
        raise ValueError(
            f"{path.name}: {len(skipped)} run line(s) failed the parse — refusing to "
            f"silently drop them from the diff base. First: {skipped[0]!r}")
    return runs


def class_durs_from_summary(summary_path: Path, preset: str):
    """Read the variant-(b) class-(a)/(b) root-disagree durations from an a8 summary.json."""
    S = json.load(open(summary_path, encoding="utf-8"))
    a = S[preset]["agg"]
    return a["b_cls_b_dur"], a["b_cls_a_dur"]


def ref_class_durs(manifest_path: Path, preset: str):
    M = json.load(open(manifest_path, encoding="utf-8"))
    p = M["presets"][preset]
    return p["class_b_root_disagree_dur"], p["class_a_root_disagree_dur"]


def key_pcts_from_summary(summary_path: Path, preset: str):
    """Candidate key-agreement % vs the home (global) key AND vs the local key (OI-143).
    Local is None if the summary predates the dual-column instrument."""
    S = json.load(open(summary_path, encoding="utf-8"))
    a = S[preset]["agg"]
    scored = a["scored_dur"]
    home = (100.0 * a["b_key_agree"] / scored) if scored else 0.0
    local = ((100.0 * a["b_key_agree_local"] / scored)
             if (scored and "b_key_agree_local" in a) else None)
    return home, local


def ref_key_pcts(manifest_path: Path, preset: str):
    """Reference key-agreement % (home, local) from the manifest; either may be None if the
    committed reference predates the OI-143 dual column."""
    M = json.load(open(manifest_path, encoding="utf-8"))
    p = M["presets"][preset]
    return p.get("key_agree_pct"), p.get("key_agree_pct_local")


def cand_coverage(summary_path: Path, preset: str):
    """Candidate WiR coverage (OI-140): (wir_covered, wir_parse_fail, wir_parse_fail_stems).
    parse_fail/stems are None if the candidate summary predates the OI-140 fields."""
    S = json.load(open(summary_path, encoding="utf-8"))
    cov = S[preset].get("coverage", {})
    return (cov.get("wir_covered"), cov.get("wir_parse_fail"),
            cov.get("wir_parse_fail_stems"))


def ref_coverage(manifest_path: Path, preset: str):
    """Reference WiR coverage (OI-140): wir_covered from the committed manifest, or None if the
    manifest predates the coverage block (then coverage cannot be reconciled)."""
    M = json.load(open(manifest_path, encoding="utf-8"))
    return M["presets"][preset].get("coverage", {}).get("wir_covered")


def ref_summary_class_b(ref_dir: Path, preset: str):
    """The reference's OWN class-(b) duration from the sibling summary.json (a8's direct output),
    for cross-checking against the manifest baseline (OI-124b). None if no summary.json ships beside
    the reference manifest."""
    sp = ref_dir / "summary.json"
    if not sp.exists():
        return None
    S = json.load(open(sp, encoding="utf-8"))
    return S.get(preset, {}).get("agg", {}).get("b_cls_b_dur")


def wir_source_from_summary(summary_path: Path, preset: str):
    """Candidate WiR source fingerprint (OI-124) from the a8 summary coverage; None if absent."""
    S = json.load(open(summary_path, encoding="utf-8"))
    return S[preset].get("coverage", {}).get("wir_source_sha256")


def ref_wir_source(manifest_path: Path, preset: str):
    """Reference WiR source fingerprint (OI-124) from the committed manifest coverage; None if absent."""
    M = json.load(open(manifest_path, encoding="utf-8"))
    return M["presets"][preset].get("coverage", {}).get("wir_source_sha256")


def key_abstain_from_summary(summary_path: Path, preset: str):
    """Candidate key-ABSTAIN % (OI-33): the fraction of scored duration where OUR key is
    unparseable/absent (b_key_fail) and is therefore EXCLUDED from the key-agree denominator
    (which is only agree+disagree). A metric that abstains on hard slices can flatter its
    key-agree-%; this figure is reported beside key-agree so opting out cannot hide."""
    S = json.load(open(summary_path, encoding="utf-8"))
    a = S[preset]["agg"]
    scored = a.get("scored_dur", 0)
    return (100.0 * a.get("b_key_fail", 0) / scored) if scored else 0.0


def ref_key_abstain(manifest_path: Path, preset: str):
    """Reference key-abstain % (OI-33) from the committed manifest (key_parse_fail_pct); None if absent."""
    M = json.load(open(manifest_path, encoding="utf-8"))
    return M["presets"][preset].get("key_parse_fail_pct")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reference", default=str(_ROOT / "tools" / "robust_stop"),
                    help="committed reference dir (manifest.json + *_variant_b_root_fail_runs.txt)")
    ap.add_argument("--candidate", required=True,
                    help="a8 --out-dir for the candidate (summary.json + *_variant_b_root_fail_runs.txt)")
    ap.add_argument("--show-runs", type=int, default=12,
                    help="max added/removed runs to list per preset per direction (0 = all)")
    args = ap.parse_args()

    ref_dir = Path(args.reference)
    cand_dir = Path(args.candidate)
    manifest = ref_dir / "manifest.json"
    cand_summary = cand_dir / "summary.json"

    overall_pass = True
    for preset in PRESETS:
        ref_runs = parse_runs(ref_dir / f"{preset}_variant_b_root_fail_runs.txt")
        cand_runs = parse_runs(cand_dir / f"{preset}_variant_b_root_fail_runs.txt")
        ref_cb, ref_ca = ref_class_durs(manifest, preset)
        cand_cb, cand_ca = class_durs_from_summary(cand_summary, preset)

        # OI-124b — internal consistency of the REFERENCE: the manifest's class-(b) baseline must
        # equal the sibling summary.json's b_cls_b_dur (a8's direct output). A partial re-baseline
        # (one artifact re-stamped, the other stale) would otherwise compare against a wrong figure.
        ref_summary_cb = ref_summary_class_b(ref_dir, preset)
        ref_consistent = ref_summary_cb is None or ref_summary_cb == ref_cb

        # (a) HARD STOP — class-(b) duration non-increase
        d_cb = cand_cb - ref_cb
        cb_pass = d_cb <= 0
        # (c) TRACKED — class-(a) duration
        d_ca = cand_ca - ref_ca

        # (b) DIAGNOSTIC — run-level set-diff (identity = stem,start,our_root,dcml_root)
        added = sorted(set(cand_runs) - set(ref_runs))
        removed = sorted(set(ref_runs) - set(cand_runs))

        # OI-140 — WiR COVERAGE reconcile: a systematic WiR-parse breakage in the candidate
        # would drop pieces -> LOWER the class-(b) duration -> silently PASS the non-increase
        # hard stop. Reconcile the candidate's wir_covered against the committed reference; a
        # SHRINK fails the diff loudly (the automated gate the mandatory explained run-diff alone
        # did not enforce).
        cand_cov, cand_pf, cand_pf_stems = cand_coverage(cand_summary, preset)
        ref_cov = ref_coverage(manifest, preset)
        cov_ok = True
        if ref_cov is not None and cand_cov is not None and cand_cov < ref_cov:
            cov_ok = False

        print(f"=== {preset} ===")
        print(f"  runs: reference={len(ref_runs)} candidate={len(cand_runs)}  "
              f"(+{len(added)} / -{len(removed)})")
        cov_tag = "OK" if cov_ok else "COVERAGE SHRUNK"
        print(f"  WiR COVERAGE: reference={ref_cov} candidate={cand_cov}  -> {cov_tag}")
        if cand_pf:
            print(f"  !! WiR PARSE FAILURE on {cand_pf} candidate stem(s): {cand_pf_stems}")
        if not cov_ok:
            print(f"  !! COVERAGE SHRANK by {ref_cov - cand_cov} score(s) — the class-(b) "
                  f"population is smaller than the reference; a non-increase can be an artifact "
                  f"of dropped pieces, not a real improvement. FAIL.")
        # OI-124b — the reference manifest baseline must agree with its own summary.json.
        if not ref_consistent:
            print(f"  !! REFERENCE INCONSISTENT: manifest class-(b)={ref_cb} but sibling "
                  f"summary.json b_cls_b_dur={ref_summary_cb} — a PARTIAL re-baseline; the diff "
                  f"base is unreliable. FAIL.")
        # OI-124 — WiR source drift: the candidate graded against a different WiR clone than the
        # reference. Surfaced loudly (informational; the class-(b)/coverage gates are the hard stop).
        cand_ws = wir_source_from_summary(cand_summary, preset)
        ref_ws = ref_wir_source(manifest, preset)
        if cand_ws and ref_ws and cand_ws != ref_ws:
            print(f"  !! WiR SOURCE DRIFT: candidate graded against a different WiR clone than the "
                  f"reference (cand {cand_ws[:12]}… vs ref {ref_ws[:12]}…) — gradings may not be "
                  f"comparable; verify the WiR checkout (REPRODUCIBILITY.md).")
        print(f"  (a) HARD STOP class-(b) root-disagree dur: ref={ref_cb} cand={cand_cb} "
              f"delta={d_cb:+d}  -> {'PASS' if cb_pass else 'FAIL'}")
        ca_flag = "  ** INVESTIGATE (large net increase)" if d_ca > CLASS_A_INVESTIGATE_TICKS else ""
        print(f"  (c) TRACKED  class-(a) root-disagree dur: ref={ref_ca} cand={cand_ca} "
              f"delta={d_ca:+d}{ca_flag}")

        # key-agreement, dual home/local column (OI-143) — informational, not a stop
        cand_kh, cand_kl = key_pcts_from_summary(cand_summary, preset)
        ref_kh, ref_kl = ref_key_pcts(manifest, preset)
        def _kp(x):
            return f"{x:.4f}%" if x is not None else "n/a"
        print(f"  (—) KEY-AGREE home:  ref={_kp(ref_kh)} cand={_kp(cand_kh)}    "
              f"local: ref={_kp(ref_kl)} cand={_kp(cand_kl)}")
        # OI-33 — the ABSTAIN-AWARE convention: the key-agree % denominator EXCLUDES abstained
        # (key-unparseable) cells, so a key-agree rise can be an artifact of abstaining more, not
        # better inference. The abstain coverage is reported BESIDE key-agree so opting out cannot
        # flatter a result; a candidate abstain ABOVE the reference is flagged (informational — key
        # is not the hard stop; the root respect counts an abstained cell as a DISAGREEMENT).
        cand_ka = key_abstain_from_summary(cand_summary, preset)
        ref_ka = ref_key_abstain(manifest, preset)
        # Compare at the manifest's stored precision (4 dp) so the rounding of a re-stamped
        # reference does not fire a false flag; only a MEANINGFUL abstain rise trips it.
        abstain_flag = ("  ** KEY-ABSTAIN ROSE — a key-agree gain may be abstention-flattered (OI-33)"
                        if (ref_ka is not None and cand_ka is not None
                            and round(cand_ka, 4) > round(ref_ka, 4))
                        else "")
        print(f"  (—) KEY-ABSTAIN (OI-33; excluded from the key-agree denominator): "
              f"ref={_kp(ref_ka)} cand={_kp(cand_ka)}{abstain_flag}")

        def _fmt(k):
            dur, cls = (cand_runs.get(k) or ref_runs.get(k))
            return f"{k[0]}@{k[1]}  our_root={k[2]} -> dcml_root={k[3]}  dur={dur} cls={cls}"

        def _dump(label, keys):
            n = len(keys)
            show = keys if args.show_runs == 0 else keys[:args.show_runs]
            a_ct = sum(1 for k in keys if (cand_runs.get(k) or ref_runs.get(k))[1] == 'a')
            b_ct = n - a_ct
            print(f"  (b) DIAGNOSTIC {label}: {n} runs (class-b {b_ct} / class-a {a_ct})")
            for k in show:
                print(f"        {_fmt(k)}")
            if args.show_runs and n > args.show_runs:
                print(f"        ... (+{n - args.show_runs} more; --show-runs 0 for all)")

        _dump("ADDED (candidate not in reference)", added)
        _dump("REMOVED (reference not in candidate)", removed)
        overall_pass = overall_pass and cb_pass and cov_ok and ref_consistent

    print(f"\nOVERALL: {'PASS' if overall_pass else 'FAIL'} "
          f"(hard stop = class-(b) duration non-increase + WiR coverage non-shrink, all presets)")
    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
