#!/usr/bin/env python3
"""WHAT THE BLOCK-(A) INSTRUMENT'S ARM DECLARATION DOES TO THE MEASUREMENT: NOTHING, OR REFUSE.

THIS FILE PRINTS ASCII ONLY (the OI-297 author-side remedy), and routes its printing through
tools/audit/output_encoding.py besides.

WHY THIS EXISTS.  `tools/a8_rebaseline_measure.py` is the instrument `CLAUDE.md` gate block (A)
calls PINNED -- every baseline in that block was produced by it.  On 2026-08-03 (phase 1y,
`OPEN_ITEMS.md` OI-307) it gained a declared expectation about which inference arm produced the
corpus it reads, defaulting to the joint arm, and it now REFUSES a corpus whose stamp disagrees.
Changing a pinned instrument is a thing the record has to be able to check rather than be told,
and the claim the record makes for this one is narrow and testable: IT CANNOT MOVE A MEASURED
VALUE, IT CAN ONLY REFUSE.

WHAT IS MEASURED HERE, AND WHAT IS MEASURED ELSEWHERE.  Two halves, and only the first is this
tool's:

  half 1, HERE  -- the instrument at HEAD, run over the production corpus by gate block (A)'s own
                   two commands, produces a candidate the committed reference cannot tell from
                   itself: run-level set-diff empty in both directions on every preset, and every
                   value the diff reports identical.  That is the "cannot move a value" half, and
                   it is a run rather than a reading of the source.
  half 2, NOT HERE -- that the declaration CAN refuse, that it does not refuse a corpus it was
                   built to admit, and that a caller declaring nothing is unaffected.  Those are
                   measured at `tools/audit/corpus_arm_establishment.json` (probes 2, 3 and 4) and
                   are not repeated here (#6).

WHY A SEPARATE ARTIFACT AT ALL.  The phase-1z dispatch asked whether this result was in a
committed artifact or only in a session report, and it was only in a session report.  A record
that cites a session report for a value is the defect D-431 exists against, so the measurement is
generated before the record cites it.

WHAT THIS DOES NOT DO.  It makes no judgment about whether the baselines are right, whether the
corpus is the right corpus, or whether declaring the arm was a good idea.  It runs the documented
procedure and records what came back.

Run:
    python tools/audit/instrument_arm_declaration_effect.py            # measure, write artifact
    python tools/audit/instrument_arm_declaration_effect.py --check    # measure, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "instrument_arm_declaration_effect.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout

# The two commands CLAUDE.md gate block (A) states for running the hard stop, in its own order.
# They are quoted here rather than paraphrased: this tool's whole claim is that it ran THE
# documented procedure and not a variant of it.
MEASURE = "tools/a8_rebaseline_measure.py"
DIFF = "tools/robust_stop_diff.py"

# The three per-preset corpus directories the instrument reads. Absent on a fresh checkout: the
# corpus is gitignored (.gitignore:26), which is why an absent corpus is reported and not failed.
CORPUS_PRESETS = ["baroque", "jazz", "default"]

# ── the diff's own report lines, parsed rather than transcribed (#17f) ───────────────────────
RE_PRESET = re.compile(r"^=== (\w+) ===$")
RE_RUNS = re.compile(
    r"^\s*runs: reference=(\d+) candidate=(\d+)\s+\(\+(\d+) / -(\d+)\)$")
RE_COVER = re.compile(
    r"^\s*WiR COVERAGE: reference=(\d+) candidate=(\d+)\s+-> (\w+)$")
RE_HARD = re.compile(
    r"^\s*\(a\) HARD STOP class-\(b\) root-disagree dur: ref=(-?\d+) cand=(-?\d+) "
    r"delta=([+-]\d+)\s+-> (\w+)$")
RE_TRACKED = re.compile(
    r"^\s*\(c\) TRACKED\s+class-\(a\) root-disagree dur: ref=(-?\d+) cand=(-?\d+) "
    r"delta=([+-]\d+)$")
RE_KEY = re.compile(
    r"^\s*\(.\) KEY-AGREE home:\s+ref=([\d.]+)% cand=([\d.]+)%\s+"
    r"local: ref=([\d.]+)% cand=([\d.]+)%$")
RE_ABSTAIN = re.compile(
    r"^\s*\(.\) KEY-ABSTAIN \(OI-33; excluded from the key-agree denominator\): "
    r"ref=([\d.]+)% cand=([\d.]+)%$")
RE_ADDED = re.compile(
    r"^\s*\(b\) DIAGNOSTIC ADDED \(candidate not in reference\): (\d+) runs "
    r"\(class-b (\d+) / class-a (\d+)\)$")
RE_REMOVED = re.compile(
    r"^\s*\(b\) DIAGNOSTIC REMOVED \(reference not in candidate\): (\d+) runs "
    r"\(class-b (\d+) / class-a (\d+)\)$")
RE_OVERALL = re.compile(r"^OVERALL: (\w+)\b")


class Stop(Exception):
    """A line of the diff's report this parser does not understand. Never a warning: an
    unparsed line means the verdict below was computed from an incomplete reading."""


def _normalize(text: str, tmp: str) -> list[str]:
    """The candidate out-dir is a fresh temporary directory on every run and both commands print
    it. Without replacing it this artifact is unreproducible by construction -- the phase-1x
    lesson, met again. Narrow: only that one path, in both the native and the forward-slash form.
    No verdict is affected."""
    for form in (tmp, tmp.replace("\\", "/"), tmp.replace("/", "\\")):
        if form:
            text = text.replace(form, "<candidate-out-dir>")
    return text.splitlines()


def _run(rel: str, args: list[str], tmp: str) -> dict:
    proc = subprocess.run([sys.executable, os.path.join(ROOT, rel), *args],
                          capture_output=True, cwd=ROOT)
    return {
        "command": f"python {rel} " + " ".join(
            a.replace(tmp, "<candidate-out-dir>") for a in args),
        "exit_code": proc.returncode,
        "stdout": _normalize(proc.stdout.decode("utf-8", errors="replace"), tmp),
        "stderr": _normalize(proc.stderr.decode("utf-8", errors="replace"), tmp),
    }


def parse_diff(lines: list[str]) -> tuple[dict, str]:
    """Read the diff's report into per-preset records. Any line that is neither blank nor
    recognised is a STOP."""
    per_preset: dict = {}
    cur = None
    overall = ""
    for line in lines:
        if not line.strip():
            continue
        m = RE_PRESET.match(line)
        if m:
            cur = m.group(1)
            per_preset[cur] = {}
            continue
        m = RE_OVERALL.match(line)
        if m:
            overall = m.group(1)
            continue
        if cur is None:
            raise Stop(f"a report line arrived before any preset heading: {line!r}")
        rec = per_preset[cur]
        m = RE_RUNS.match(line)
        if m:
            rec["runs"] = {"reference": int(m.group(1)), "candidate": int(m.group(2)),
                           "added": int(m.group(3)), "removed": int(m.group(4))}
            continue
        m = RE_COVER.match(line)
        if m:
            rec["wir_coverage"] = {"reference": int(m.group(1)),
                                   "candidate": int(m.group(2)), "verdict": m.group(3)}
            continue
        m = RE_HARD.match(line)
        if m:
            rec["hard_stop_class_b_duration"] = {
                "reference": int(m.group(1)), "candidate": int(m.group(2)),
                "delta": int(m.group(3)), "verdict": m.group(4)}
            continue
        m = RE_TRACKED.match(line)
        if m:
            rec["tracked_class_a_duration"] = {
                "reference": int(m.group(1)), "candidate": int(m.group(2)),
                "delta": int(m.group(3))}
            continue
        m = RE_KEY.match(line)
        if m:
            rec["key_agree_percent"] = {
                "home": {"reference": m.group(1), "candidate": m.group(2)},
                "local": {"reference": m.group(3), "candidate": m.group(4)}}
            continue
        m = RE_ABSTAIN.match(line)
        if m:
            rec["key_abstain_percent"] = {"reference": m.group(1), "candidate": m.group(2)}
            continue
        m = RE_ADDED.match(line)
        if m:
            rec["added_runs"] = {"total": int(m.group(1)), "class_b": int(m.group(2)),
                                 "class_a": int(m.group(3))}
            continue
        m = RE_REMOVED.match(line)
        if m:
            rec["removed_runs"] = {"total": int(m.group(1)), "class_b": int(m.group(2)),
                                   "class_a": int(m.group(3))}
            continue
        raise Stop(f"unparsed line in the diff's report: {line!r}")
    return per_preset, overall


def verdict_for(rec: dict) -> str:
    """MOVED NOTHING is the strong reading and the one the record needs: not merely that the hard
    stop passed, but that the candidate and the reference are indistinguishable everywhere the
    diff reports. A pass with any movement is reported as MOVED SOMETHING, which is a finding."""
    required = ("runs", "wir_coverage", "hard_stop_class_b_duration",
                "tracked_class_a_duration", "key_agree_percent", "key_abstain_percent",
                "added_runs", "removed_runs")
    missing = [k for k in required if k not in rec]
    if missing:
        raise Stop(f"the diff's report did not carry {missing} for a preset")
    same = (rec["runs"]["added"] == 0
            and rec["runs"]["removed"] == 0
            and rec["runs"]["reference"] == rec["runs"]["candidate"]
            and rec["wir_coverage"]["reference"] == rec["wir_coverage"]["candidate"]
            and rec["hard_stop_class_b_duration"]["delta"] == 0
            and rec["tracked_class_a_duration"]["delta"] == 0
            and rec["key_agree_percent"]["home"]["reference"]
            == rec["key_agree_percent"]["home"]["candidate"]
            and rec["key_agree_percent"]["local"]["reference"]
            == rec["key_agree_percent"]["local"]["candidate"]
            and rec["key_abstain_percent"]["reference"]
            == rec["key_abstain_percent"]["candidate"]
            and rec["added_runs"]["total"] == 0
            and rec["removed_runs"]["total"] == 0)
    return "MOVED NOTHING" if same else "MOVED SOMETHING"


def corpus_absent() -> list[str]:
    return [p for p in CORPUS_PRESETS
            if not os.path.isdir(os.path.join(ROOT, "tools", "corpus", p))]


def measure() -> dict:
    tmp = tempfile.mkdtemp(prefix="arm_effect_")
    try:
        runs = {
            "the_measurement": _run(MEASURE, ["--out-dir", tmp], tmp),
            "the_diff_against_the_committed_reference": _run(DIFF, ["--candidate", tmp], tmp),
        }
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    per_preset, overall = parse_diff(runs["the_diff_against_the_committed_reference"]["stdout"])
    if not per_preset:
        raise Stop("the diff produced no per-preset report")
    verdicts = {k: verdict_for(v) for k, v in per_preset.items()}

    return {
        "purpose": "The measured effect, on the CLAUDE.md gate block (A) hard stop, of the pinned "
                   "instrument declaring which inference arm its baselines were measured on: it "
                   "moves no measured value, and can only refuse.",
        "generated_by": "tools/audit/instrument_arm_declaration_effect.py",
        "generated_for": "cc_instruction_phase1z_commit_and_instrument_record.md, Task 2.2 -- "
                         "the dispatch's assumption A2 (that this result was already in a "
                         "committed artifact) came back ABSENT, and its accepted-outcomes "
                         "section says the measurement is generated into an artifact before the "
                         "record cites it.",
        "the_claim_it_establishes": "The instrument change recorded in CLAUDE.md gate block (A)'s "
                                    "provenance CANNOT MOVE A MEASURED VALUE, ONLY REFUSE. The "
                                    "refusal half is measured elsewhere and is not repeated here.",
        "what_is_measured_elsewhere": "That a wrong-arm corpus is detected, that a right-arm one "
                                      "is not refused, and that a caller declaring nothing is "
                                      "unaffected: tools/audit/corpus_arm_establishment.json, "
                                      "probes 2, 3 and 4.",
        "why_this_is_a_run_and_not_a_reading_of_the_source": "The instrument at HEAD is executed "
                                                            "over the production corpus by gate "
                                                            "block (A)'s own two commands, and "
                                                            "its output is compared with the "
                                                            "committed tools/robust_stop/ "
                                                            "reference by the diff tool that "
                                                            "block names. Nothing is inferred "
                                                            "from reading the arm code.",
        "one_normalization_and_why": "Both commands print the candidate out-dir, which is a fresh "
                                     "temporary directory on every run; it is replaced by "
                                     "'<candidate-out-dir>' in the captured text and in the "
                                     "recorded command lines. Without it this artifact would be "
                                     "unreproducible by construction. Narrow, and no verdict is "
                                     "affected.",
        "the_procedure": [
            "python tools/a8_rebaseline_measure.py --out-dir <candidate-out-dir>",
            "python tools/robust_stop_diff.py --candidate <candidate-out-dir>",
        ],
        "the_reference_it_is_diffed_against": "tools/robust_stop/ -- the committed diff base "
                                              "CLAUDE.md gate block (A) names, unmoved by this "
                                              "run and by the wave that recorded it.",
        "runs": runs,
        "per_preset": per_preset,
        "per_preset_verdicts": verdicts,
        "overall_from_the_diff": overall,
        "verdict_rule": "MOVED NOTHING requires more than the hard stop passing: the candidate "
                        "and the reference must be indistinguishable at every value the diff "
                        "reports, in both directions of the run-level set-diff.",
        "established": bool(verdicts) and all(v == "MOVED NOTHING" for v in verdicts.values())
        and overall == "PASS",
    }


def main(argv: list[str]) -> int:
    absent = corpus_absent()
    if absent:
        print("CORPUS-ABSENT: tools/corpus/ is gitignored (.gitignore:26) and this checkout "
              f"has no {', '.join(absent)} directory.")
        print("This check measures the instrument against the production corpus, so with no "
              "corpus there is nothing to measure and nothing to compare; reported, not failed.")
        return 0

    artifact = measure()
    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"

    if "--check" in argv:
        have = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the run: instrument_arm_declaration_effect.json does not re-derive")
            drift = 1
        else:
            print("the instrument arm declaration effect re-derives")
            drift = 0
    else:
        open(OUT, "w", encoding="utf-8", newline="").write(text)
        print(f"wrote {os.path.relpath(OUT, ROOT)}")
        drift = 0

    for preset, v in artifact["per_preset_verdicts"].items():
        print(f"  {preset}: {v}")
    print(f"overall from the diff: {artifact['overall_from_the_diff']}")
    print(f"established: {artifact['established']}")
    return drift or (0 if artifact["established"] else 1)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
