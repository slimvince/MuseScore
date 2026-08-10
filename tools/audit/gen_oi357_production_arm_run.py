#!/usr/bin/env python3
"""OI-357 — THE PRODUCTION ARM, RUN OVER THE DERIVED PARTIAL-SIGNATURE POPULATION.

WHAT THIS IS.  The user's **Ruling 35(b)** of 2026-08-09
(`cowork_rulings_2026_08_09_fifth_stop.md`) licenses ONE bounded EXPLORATIONAL run: the
production arm over the same derived stem population the committed-outputs pass measured,
"outputs to a scratch artifact — no corpus promotion, no golden, no `tools/corpus/` or
`tools/robust_stop/` movement, the gate unmoved — compared identically to the committed-outputs
pass, stamped corpus-hash + tool-commit (#16)".  It answers `OPEN_ITEMS.md` OI-357 in the one
direction the committed outputs could not: **every committed Corelli output predates the joint
estimator's adoption as the production inference layer, so those files are the LEGACY arm's.**

WHAT IT IS NOT.  It is not a corpus regeneration, not a re-baseline, not a promotion, and not a
measurement of the gate.  Nothing it writes enters `tools/corpus/` or `tools/robust_stop/`; the
frozen gate corpus is untouched, and the research-tier-on-entry rule (`CLAUDE.md` gate block (A))
is not disturbed — this repertoire is research material and stays so.  **It proposes no fix, no
design and no inference change.**  Under the scope-of-surprise clause (#5, #17–#19) a surprise here
is explorational and is ROWED, not built around.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  derived  : the population (imported from `gen_oi357_partial_signature_establishment.py`, whose
             own derivation is the evidence document's stated method — never re-implemented, #6);
             every stamp; every per-piece outcome of the run.
  authored : nothing.  This tool takes no verdict and makes no comparison — the comparison is the
             SAME tool as the committed-outputs pass, run against this run's directory.

THE FLAG IS NOT OPTIONAL, and that is the whole point of the run.  `batch_analyze` runs the LEGACY
pipeline without `--joint-inference` (`BUILD_AND_TEST.md`, the corrected invocation note): a
flag-less recipe would measure exactly the arm the committed outputs already are, and the pass
would answer nothing.  The flag is passed here and its presence is recorded in the run record.

Run:
    python tools/audit/gen_oi357_production_arm_run.py [--limit N]

Output:
    scratch_artifacts/oi357_production_arm/<stem>.ours.json   (the run's outputs)
    tools/audit/oi357_production_arm_run.json                 (the run record + the #16 stamps)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SCORES = os.path.join(ROOT, "tools", "dcml", "corelli", "MS3")
JOINT = os.path.join(ROOT, "tools", "joint_estimator")
OUT_DIR = os.path.join(ROOT, "scratch_artifacts", "oi357_production_arm")
OUT = os.path.join(HERE, "oi357_production_arm_run.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
from gen_oi357_partial_signature_establishment import (   # noqa: E402  (path set above)
    METADATA, key_name_to_fifths_and_tonic, notated_fifths, read_metadata,
)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

BATCH = os.path.join(ROOT, "ninja_build_rel", "batch_analyze.exe")
GIT_BASH = [r"C:/Program Files/Git/usr/bin/bash.exe",
            r"C:/Program Files (x86)/Git/usr/bin/bash.exe"]


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def head_commit(repo: str) -> str | None:
    """The pinned commit of a repository, as a git OBJECT query (D-253's sanctioned form)."""
    try:
        return subprocess.check_output(["git", "-C", repo, "rev-parse", "HEAD"],
                                       text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return None


def to_unix(path: str) -> str:
    s = os.path.abspath(path)
    if len(s) >= 2 and s[1] == ":":
        s = "/" + s[0].lower() + s[2:]
    return s.replace("\\", "/")


def to_win(path: str) -> str:
    return os.path.abspath(path).replace("\\", "/")


def git_bash() -> str | None:
    for c in GIT_BASH:
        if os.path.exists(c):
            return c
    return None


def population() -> list[dict]:
    """The derived partial-signature population — the comparison tool's own rule, imported.

    A piece is in it when its NOTATED signature differs from the NATURAL signature of its
    annotated key.  The rule is not restated here; it is the same code the committed-outputs
    pass runs (#6), so the two passes cannot drift apart in what they are about.
    """
    out = []
    for p in read_metadata():
        fifths, _why = notated_fifths(p["key_signature_field"])
        natural, tonic_pc, mode = key_name_to_fifths_and_tonic(p["annotated_key"])
        if fifths is None or natural is None or fifths == natural:
            continue
        out.append({"piece": p["piece"], "annotated_key": p["annotated_key"],
                    "notated_signature_fifths": fifths,
                    "annotated_tonic_pitch_class": tonic_pc, "annotated_mode": mode})
    return out


def run_one(score: str, out_path: str, joint: bool = True) -> tuple[bool, str]:
    """One `batch_analyze` invocation, with or without `--joint-inference`.

    On Windows it goes through Git Bash: a direct subprocess launch of this binary triggers a Qt
    access violation, which is a recorded property of this environment rather than a preference.

    ★ THE `joint=False` FORM IS THE CONTROL, AND IT EXISTS FOR A MEASUREMENT REASON.  The committed
    Corelli outputs are the legacy arm's, but they were produced two months before this run — so a
    production-versus-committed comparison confounds THE ARM with everything else that moved in
    between, and neither #19 nor #24 admits a difference attributed to a cause that is not the only
    one available.  Running the legacy arm at the SAME commit, over the same scores, isolates the
    arm.  It writes to its own scratch directory and is otherwise identical.
    """
    flag = f' --joint-inference "{to_win(JOINT)}"' if joint else ""
    args = f'"{to_win(score)}" "{to_win(out_path)}" --preset Baroque{flag}'
    try:
        if platform.system() == "Windows" and git_bash():
            cmd = f"{to_unix(BATCH)} {args}"
            r = subprocess.run([git_bash(), "-c", cmd], stdout=subprocess.DEVNULL,
                               stderr=subprocess.PIPE, timeout=300)
        else:
            argv = [BATCH, score, out_path, "--preset", "Baroque"]
            if joint:
                argv += ["--joint-inference", JOINT]
            r = subprocess.run(argv, stdout=subprocess.DEVNULL,
                               stderr=subprocess.PIPE, timeout=300)
        if r.returncode != 0:
            return False, r.stderr.decode("utf-8", errors="replace").strip()[:300]
        return os.path.exists(out_path), "" if os.path.exists(out_path) else "no output written"
    except subprocess.TimeoutExpired:
        return False, "timed out"
    except Exception as exc:                                   # pragma: no cover - environment
        return False, f"{type(exc).__name__}: {exc}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0,
                    help="run only the first N of the population (diagnostic; a limited run is "
                         "recorded as limited and is NOT a measurement of the population)")
    ap.add_argument("--legacy-arm", action="store_true",
                    help="the SAME-COMMIT CONTROL: run without --joint-inference, so the legacy "
                         "arm is measured at this commit rather than at the two-month-old one the "
                         "committed outputs carry. Writes to its own scratch directory.")
    args = ap.parse_args()

    joint = not args.legacy_arm
    out_dir = OUT_DIR if joint else OUT_DIR + "_legacy_control"
    out_record = OUT if joint else OUT.replace(".json", "_legacy_control.json")

    if not os.path.exists(BATCH):
        raise SystemExit(f"STOP: batch_analyze not found at {os.path.relpath(BATCH, ROOT)}")
    if joint and not os.path.isdir(JOINT):
        raise SystemExit(f"STOP: the joint-estimator table directory is missing: "
                         f"{os.path.relpath(JOINT, ROOT)} — the flag cannot be passed, and a "
                         "flag-less run would measure the legacy arm")
    if not os.path.isdir(SCORES):
        raise SystemExit(f"STOP: the Corelli scores are missing: {os.path.relpath(SCORES, ROOT)}")

    os.makedirs(out_dir, exist_ok=True)
    pop = population()
    todo = pop[: args.limit] if args.limit else pop

    ran, failed, absent = [], [], []
    for m in todo:
        score = os.path.join(SCORES, m["piece"] + ".mscx")
        if not os.path.exists(score):
            absent.append(m["piece"])
            continue
        out_path = os.path.join(out_dir, m["piece"] + ".ours.json")
        ok, why = run_one(score, out_path, joint=joint)
        (ran if ok else failed).append(m["piece"] if ok else {"piece": m["piece"], "why": why})

    # ── the #16 stamps, each derived rather than typed ───────────────────────
    score_hashes = {m["piece"]: sha256_file(os.path.join(SCORES, m["piece"] + ".mscx"))
                    for m in todo if os.path.exists(os.path.join(SCORES, m["piece"] + ".mscx"))}
    corpus_hash = hashlib.sha256(
        json.dumps(sorted(score_hashes.items()), ensure_ascii=False).encode("utf-8")).hexdigest()
    joint_files = sorted(f for f in os.listdir(JOINT) if os.path.isfile(os.path.join(JOINT, f)))
    joint_hash = hashlib.sha256(json.dumps(
        sorted((f, sha256_file(os.path.join(JOINT, f))) for f in joint_files),
        ensure_ascii=False).encode("utf-8")).hexdigest()

    record = {
        "what_this_is": "OI-357's PRODUCTION-ARM run, on the user's Ruling 35(b) of 2026-08-09: a "
                        "bounded EXPLORATIONAL run of the arm that ships over the derived "
                        "partial-signature population, whose outputs live in a scratch directory "
                        "and nowhere else. It takes no verdict; the comparison is performed by "
                        "`gen_oi357_partial_signature_establishment.py --run-dir`, the SAME tool "
                        "the committed-outputs pass used (#6).",
        "generated_by": "tools/audit/gen_oi357_production_arm_run.py",
        "the_row_it_feeds": "OPEN_ITEMS.md OI-357 (and OI-363, which gains the production-arm "
                            "column beside its committed-outputs one)",
        "★_the_bounds_this_run_was_performed_inside": {
            "the_ruling": "User, 2026-08-09, Ruling 35(b) of "
                          "`cowork_rulings_2026_08_09_fifth_stop.md`.",
            "outputs_go_where": os.path.relpath(out_dir, ROOT).replace("\\", "/"),
            "nothing_under_tools_corpus_or_tools_robust_stop": True,
            "no_corpus_promotion_no_golden_no_re_baseline": True,
            "the_gate_is_unmoved": "This repertoire is not the gate corpus, and nothing here "
                                   "promotes it. The research-tier-on-entry rule in `CLAUDE.md` "
                                   "gate block (A) is untouched.",
            "explorational": "#5 fact-finding under the scope-of-surprise clause: a surprise here "
                             "is ROWED, and nothing is designed or fixed for it.",
        },
        "★_which_arm_this_run_is": (
            "the PRODUCTION arm (joint estimator)" if joint else
            "the LEGACY arm, AS A SAME-COMMIT CONTROL. The committed Corelli outputs are also the "
            "legacy arm's, but they were produced two months before this run — so a "
            "production-versus-committed comparison confounds THE ARM with everything else that "
            "moved between the two commits, and a difference may not be attributed to a cause that "
            "is not the only one available (#19, #24). This run isolates the arm: same scores, same "
            "commit, same population, same comparison code — one flag apart. It is a WIDENING of "
            "Ruling 35(b)'s letter, which licenses the production-arm run, and it is REPORTED as "
            "one rather than taken silently (the D-654 discipline: a widening reported is "
            "reviewable, a widening hidden is not)."),
        "★_the_flag_is_the_point": {
            "invocation": ("batch_analyze <score> <out> --preset Baroque --joint-inference "
                           "<tools/joint_estimator>" if joint else
                           "batch_analyze <score> <out> --preset Baroque   (NO --joint-inference: "
                           "this is the legacy-arm control)"),
            "why_it_is_not_optional": "Without `--joint-inference` batch_analyze runs the LEGACY "
                                      "pipeline (`BUILD_AND_TEST.md`, the corrected invocation "
                                      "note), which is exactly the arm the committed outputs "
                                      "already are — a flag-less run would answer nothing.",
            "why_the_preset_is_named_and_why_it_does_not_decide_anything": "Production inference is "
                                      "PRESET-INDEPENDENT (`CLAUDE.md` gate block (A), the OI-178 "
                                      "adoption), so the preset is a presentation carrier here. It "
                                      "is stated because a recorded invocation must be "
                                      "reproducible, not because it moves a value.",
        },
        "★_the_reproducibility_stamps_16": {
            # `CLAUDE.md` #16 names this stamp with the collided word *instrument*; the field is
            # named in the disambiguated form the Conventions require, and the rule it satisfies
            # is cited rather than its wording copied.
            "measurement_tool_commit": head_commit(ROOT),
            "corpus_pinned_commit": head_commit(os.path.join(ROOT, "tools", "dcml", "corelli")),
            "corpus_hash_over_the_population_s_scores": corpus_hash,
            "joint_estimator_table_hash": joint_hash,
            "metadata_tsv_sha256": sha256_file(METADATA),
            "how_the_corpus_hash_is_built": "sha256 over the sorted (piece, sha256-of-.mscx) pairs "
                                            "of every score this run read. Derived, so a corpus "
                                            "that moves cannot be mistaken for the one measured.",
        },
        "the_population": {
            "how_it_is_derived": "IMPORTED from gen_oi357_partial_signature_establishment.py — the "
                                 "evidence document's own stated method, applied to every piece in "
                                 "the corpus metadata. Not re-implemented here (#6), so the two "
                                 "passes cannot drift apart in what they are about.",
            "pieces_in_the_population": len(pop),
            "pieces_attempted_in_this_run": len(todo),
            "this_run_was_limited": bool(args.limit),
            "★_what_a_limited_run_is_worth": "A limited run is a diagnostic, not a measurement of "
                                             "the population: reading it as one is the silent cap "
                                             "the standing rules forbid. The flag above says which "
                                             "this is.",
        },
        "the_outcome": {
            "pieces_analysed": len(ran),
            "pieces_that_failed": failed,
            "pieces_with_no_score_file": absent,
        },
    }

    open(out_record, "w", encoding="utf-8", newline="").write(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(out_record, ROOT)}")
    print(f"  arm: {'joint (production)' if joint else 'legacy (same-commit control)'}")
    print(f"  population {len(pop)}; attempted {len(todo)}; analysed {len(ran)}; "
          f"failed {len(failed)}; no score file {len(absent)}")
    print(f"  outputs in {os.path.relpath(out_dir, ROOT)}")
    return 0 if not failed and not absent else 1


if __name__ == "__main__":
    sys.exit(main())
