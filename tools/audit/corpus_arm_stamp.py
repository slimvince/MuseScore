#!/usr/bin/env python3
"""THE INFERENCE ARM OF A CORPUS: READ IT, RECORD IT, AND REFUSE TO CONFUSE THE TWO.

THIS FILE PRINTS ASCII ONLY (the OI-297 author-side remedy), and routes its printing through
tools/audit/output_encoding.py besides.

WHY THIS EXISTS.  `batch_analyze` produces the same `.ours.json` SHAPE from either of two
pipelines: the joint estimator (`--joint-inference`; the production inference layer on the
batch/corpus surface since the OI-178 adoption) or the legacy `analyzeScore` path.  The flag
is opt-in -- `jointInferenceDir` is initialised empty at `tools/batch_analyze.cpp:4917` and
the joint path runs only under `if (!jointInferenceDir.empty())` at `:5590`.  Until
2026-08-03 `corpus_manifest.json` stamped the BINARY and not its invocation, so two corpora
produced by different pipelines were indistinguishable in the record -- and
`tools/corpus/<preset>` is the directory `tools/a8_rebaseline_measure.py` reads for the
CLAUDE.md block-(A) hard stop, which `run_bach_preset.py` clean-slates before a regen.
`OPEN_ITEMS.md` OI-307.

WHAT MAKES THE ANSWER ESTABLISHABLE RATHER THAN NARRATED.  Every `.ours.json` already stamps
its own producer: the joint writer emits `"analysisPath": "joint"`
(`tools/batch_analyze.cpp:4695`), the standard writer emits `"analysisPath": "batch"`
(`:1448`).  So the arm of an existing corpus is not a matter of remembering which command was
run -- it is readable at the object, per file, which is what #15 asks for and what makes a
back-stamp evidence rather than an assertion.

THE FOUR MODES.
    --scan                  report every corpus directory under tools/corpus/ and the arm its
                            files report.  Reads; writes nothing.
    --check                 THE GUARD.  Every corpus directory the block-(A) hard stop reads
                            carries a RECORDED arm, and it is the joint arm.  A directory that
                            is not present at all is reported ABSENT and passes -- the corpus
                            is gitignored, so a fresh checkout has none, and a guard that
                            failed there would be reporting on the checkout, not the corpus.
    --apply                 BACK-STAMP: for each gate corpus (add --all for every corpus dir),
                            verify the manifest still describes the files present, read the
                            arm from those files, and record it WITH the evidence.  Refuses to
                            stamp anything the files do not settle.
    --establish [--check]   the measured detection this instrument owes under D-436: a
                            wrong-arm corpus is actually detected, a right-arm one is not
                            refused, and none of the checks that existed before was weakened.

Run:
    python tools/audit/corpus_arm_stamp.py --scan
    python tools/audit/corpus_arm_stamp.py --check
    python tools/audit/corpus_arm_stamp.py --apply
    python tools/audit/corpus_arm_stamp.py --establish --check
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 -- the findings must survive a non-console stdout

sys.path.insert(0, os.path.join(ROOT, "tools"))
import characterise_bir_false as cbf             # noqa: E402
import run_bach_preset as rbp                    # noqa: E402

CORPUS_ROOT = os.path.join(ROOT, "tools", "corpus")

# The three directories the block-(A) hard stop reads (tools/a8_rebaseline_measure.py
# PRESETS). Every other directory under tools/corpus/ is a named experiment's scratch output
# and gates nothing.
GATE_PRESETS = ["baroque", "jazz", "default"]

# The arm every CLAUDE.md gate block (A) baseline was measured on (the OI-178 adoption,
# user-ratified 2026-07-26).
GATE_ARM = cbf.ARM_JOINT

BACKSTAMP_OUT = os.path.join(HERE, "corpus_arm_backstamp.json")
ESTABLISH_OUT = os.path.join(HERE, "corpus_arm_establishment.json")

# The two writers, cited wherever a back-stamp records what it read. Not a figure and not a
# count -- a pointer to the code that puts the value in the file.
WRITER_CITATIONS = {
    "joint": "tools/batch_analyze.cpp:4695 -- writeJointInferenceJson emits "
             "\"analysisPath\": \"joint\"",
    "legacy": "tools/batch_analyze.cpp:1448 -- the standard writeJson emits the analysisPath "
              "it is handed; the batch corpus path passes \"batch\"",
    "flag": "tools/batch_analyze.cpp:4917 (initialised empty) and :5590 (entered only when "
            "non-empty) -- the joint path is opt-in, so one binary produces either arm",
}


# ── reading an existing corpus directory ─────────────────────────────────────────────────

def _ours_files(corpus_dir: str) -> list[str]:
    if not os.path.isdir(corpus_dir):
        return []
    return sorted(f for f in os.listdir(corpus_dir) if f.endswith(".ours.json"))


def observe_dir(corpus_dir: str) -> dict:
    """What the FILES in corpus_dir say about which pipeline produced them.

    Reads each .ours.json's analysisPath (the head of the file only) and tallies. No manifest
    is consulted: this is the object-level reading a manifest field is then checked against.
    """
    values: dict = {}
    for name in _ours_files(corpus_dir):
        with open(os.path.join(corpus_dir, name), "rb") as fh:
            head = fh.read(4096)
        v = rbp._analysis_path_of(head)
        values[v] = values.get(v, 0) + 1
    return {
        "analysis_path_values": {(k if k is not None else "<absent>"): v
                                 for k, v in sorted(values.items(),
                                                    key=lambda kv: (kv[0] is None, kv[0]))},
        "observed_arm": rbp._observed_arm(values),
        "ours_files": sum(values.values()),
    }


def read_manifest(corpus_dir: str) -> dict | None:
    path = os.path.join(corpus_dir, cbf.MANIFEST_NAME)
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:                      # a manifest that will not parse is a finding
        return {"_unparseable": str(exc)}


def corpus_dirs() -> list[str]:
    """Every directory under tools/corpus/ carrying a manifest, gate dirs first."""
    if not os.path.isdir(CORPUS_ROOT):
        return []
    found = [d for d in sorted(os.listdir(CORPUS_ROOT))
             if os.path.exists(os.path.join(CORPUS_ROOT, d, cbf.MANIFEST_NAME))]
    gate = [d for d in GATE_PRESETS if d in found]
    return gate + [d for d in found if d not in gate]


def state_of(name: str) -> dict:
    corpus_dir = os.path.join(CORPUS_ROOT, name)
    manifest = read_manifest(corpus_dir)
    obs = observe_dir(corpus_dir)
    if manifest is None:
        recorded_arm, recorded_state = None, "NO MANIFEST"
    elif "_unparseable" in manifest:
        recorded_arm, recorded_state = None, "UNPARSEABLE MANIFEST"
    else:
        recorded_arm, recorded_state = cbf.corpus_arm(manifest)
    return {
        "dir": f"tools/corpus/{name}",
        "gates": name in GATE_PRESETS,
        "preset": (manifest or {}).get("preset"),
        "manifest_schema": (manifest or {}).get("schema"),
        "recorded_arm": recorded_arm,
        "recorded_state": recorded_state,
        "observed_arm": obs["observed_arm"],
        "analysis_path_values": obs["analysis_path_values"],
        "ours_files": obs["ours_files"],
        "agrees": (recorded_state == "RECORDED" and recorded_arm == obs["observed_arm"]),
    }


# ── --scan ───────────────────────────────────────────────────────────────────────────────

def do_scan() -> int:
    names = corpus_dirs()
    if not names:
        print("no corpus directory under tools/corpus/ carries a manifest "
              "(tools/corpus is gitignored; a fresh checkout has none)")
        return 0
    print(f"{len(names)} corpus director(ies) with a manifest under tools/corpus/")
    print("  gate = read by the CLAUDE.md block-(A) hard stop\n")
    for name in names:
        s = state_of(name)
        mark = "GATE" if s["gates"] else "    "
        print(f"  [{mark}] {name:<24} recorded={str(s['recorded_arm']):<8} "
              f"({s['recorded_state']:<8}) observed={s['observed_arm']:<8} "
              f"files={s['ours_files']:<4} {s['analysis_path_values']}")
    return 0


# ── --check (the guard) ──────────────────────────────────────────────────────────────────

def do_check() -> int:
    faults = []
    for name in GATE_PRESETS:
        corpus_dir = os.path.join(CORPUS_ROOT, name)
        if not os.path.isdir(corpus_dir):
            print(f"  [ABSENT] tools/corpus/{name} -- nothing to check "
                  f"(the corpus is gitignored)")
            continue
        s = state_of(name)
        if s["recorded_state"] != "RECORDED":
            faults.append(f"tools/corpus/{name}: {s['recorded_state']} -- no established arm")
            print(f"  [FAIL]   tools/corpus/{name} {s['recorded_state']}")
            continue
        if s["recorded_arm"] != GATE_ARM:
            faults.append(f"tools/corpus/{name}: recorded arm is {s['recorded_arm']}, and "
                          f"every block-(A) baseline was measured on the {GATE_ARM} arm")
            print(f"  [FAIL]   tools/corpus/{name} arm={s['recorded_arm']}")
            continue
        if not s["agrees"]:
            faults.append(f"tools/corpus/{name}: the manifest records {s['recorded_arm']} and "
                          f"the files report {s['observed_arm']}")
            print(f"  [FAIL]   tools/corpus/{name} manifest={s['recorded_arm']} "
                  f"files={s['observed_arm']}")
            continue
        print(f"  [OK]     tools/corpus/{name} arm={s['recorded_arm']} "
              f"(manifest and files agree)")
    if faults:
        print("\nSTOP: the block-(A) hard stop would read a corpus whose arm is not the one "
              "its baselines were measured on:")
        for f in faults:
            print(f"  - {f}")
        return 1
    print("every gate corpus present carries an established joint arm")
    return 0


# ── --apply (the back-stamp) ─────────────────────────────────────────────────────────────

def backstamp_one(name: str) -> dict:
    """Establish and record one directory's arm, or report why it cannot be established."""
    corpus_dir = os.path.join(CORPUS_ROOT, name)
    rec = {"dir": f"tools/corpus/{name}"}

    manifest = read_manifest(corpus_dir)
    if manifest is None or "_unparseable" in manifest:
        rec["outcome"] = "NOT ESTABLISHED"
        rec["why"] = "no readable corpus_manifest.json"
        return rec

    # The manifest must still DESCRIBE the files present before its arm field means anything
    # about them. This is the existing guard, run unchanged and with no arm expectation.
    try:
        cbf.validate_corpus_dir(Path(corpus_dir))
    except cbf.CorpusValidationError as exc:
        rec["outcome"] = "NOT ESTABLISHED"
        rec["why"] = f"the manifest does not describe the files present: {exc}"
        return rec

    obs = observe_dir(corpus_dir)
    rec.update({
        "preset": manifest.get("preset"),
        "schema_before": manifest.get("schema"),
        "ours_files": obs["ours_files"],
        "analysis_path_values": obs["analysis_path_values"],
        "observed_arm": obs["observed_arm"],
        "arm_before": manifest.get("inference_arm"),
    })

    if obs["observed_arm"] not in (cbf.ARM_JOINT, cbf.ARM_LEGACY):
        rec["outcome"] = "NOT ESTABLISHED"
        rec["why"] = (f"the files do not settle it (observed {obs['observed_arm']}). Left "
                      f"ARM-UNKNOWN rather than guessed, and NOT regenerated to find out -- "
                      f"regenerating to learn what a corpus was is the re-baseline this is "
                      f"forbidden to perform.")
        return rec

    manifest["schema"] = rbp.MANIFEST_SCHEMA
    manifest["inference_arm"] = obs["observed_arm"]
    manifest["inference_arm_source"] = ("back-stamped 2026-08-03 from the produced .ours.json "
                                        "files (their analysisPath)")
    manifest["inference_arm_observed"] = obs["observed_arm"]
    manifest.setdefault("inference_arm_requested", None)
    manifest.setdefault("joint_inference_dir", None)
    manifest["analysis_path_values"] = obs["analysis_path_values"]
    manifest["inference_arm_evidence"] = {
        "read_at": "every .ours.json in this directory, its analysisPath field",
        "writers": WRITER_CITATIONS,
        "the_manifest_still_describes_these_files":
            "characterise_bir_false.validate_corpus_dir passed before this stamp was written "
            "-- every OK score present and sha256-matching, no extra file",
        "corroboration": [
            "CLAUDE.md gate block (A): the joint estimator IS the production inference layer "
            "on the batch/corpus surface (OI-178 adoption, user-ratified 2026-07-26; "
            "measurement provenance d615152c51)",
            "tools/robust_stop/manifest.json -> reproduce_status.note: the reference is "
            "reproduced by regenerating each preset with "
            "run_bach_preset.py --joint-inference C:/s/MS/tools/joint_estimator",
            "tools/robust_stop/manifest.json -> provenance.corpus_git_hash: tools/corpus is "
            "gitignored, so the corpus has no commit of its own and this stamp is the only "
            "arm record it will ever carry",
        ],
        "what_this_is_not": "not a claim about which command was typed. The value is what the "
                            "files say about themselves; the corroboration is why that reading "
                            "is unsurprising, not why it is believed.",
    }
    path = os.path.join(corpus_dir, cbf.MANIFEST_NAME)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(manifest, indent=2, sort_keys=True))
    rec["outcome"] = "ESTABLISHED"
    rec["arm_after"] = obs["observed_arm"]
    return rec


def do_apply(all_dirs: bool) -> int:
    names = corpus_dirs() if all_dirs else [d for d in GATE_PRESETS
                                            if os.path.isdir(os.path.join(CORPUS_ROOT, d))]
    records = [backstamp_one(n) for n in names]
    established = [r for r in records if r["outcome"] == "ESTABLISHED"]
    unestablished = [r for r in records if r["outcome"] != "ESTABLISHED"]

    artifact = {
        "purpose": "The record of one act: which corpus directories had their inference arm "
                   "ESTABLISHED and back-stamped, from what evidence, and which were left "
                   "ARM-UNKNOWN because their own files do not settle it.",
        "generated_by": "tools/audit/corpus_arm_stamp.py --apply",
        "generated_for": "cc_instruction_phase1y_corpus_arm_stamping.md, Task 3",
        "this_is_a_record_of_an_act_not_a_derivation":
            "It is written once, by the act it records. It is NOT re-derived by --check and "
            "must not be regenerated to see whether it still reproduces: the directories it "
            "describes are gitignored working-tree state, so a later run describes a later "
            "tree. --check asserts the PROPERTY instead (the gate corpora carry an "
            "established joint arm), which is stable and machine-independent.",
        "scope": ("every corpus directory under tools/corpus/ carrying a manifest"
                  if all_dirs else
                  "the corpus directories the CLAUDE.md block-(A) hard stop reads"),
        "the_corpus_is_not_under_version_control":
            ".gitignore:26 ignores /tools/corpus/. There is no commit that produced these "
            "directories and no git object to compare them against; their manifest is the "
            "whole of their provenance record.",
        "established": established,
        "not_established": unestablished,
        "counts": {"established": len(established), "not_established": len(unestablished)},
    }
    with open(BACKSTAMP_OUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(BACKSTAMP_OUT, ROOT)}")
    for r in records:
        print(f"  [{r['outcome']}] {r['dir']} "
              f"{r.get('arm_after', '')} {r.get('why', '')}".rstrip())
    return 0


# ── --establish (D-436: the measured detection, both directions) ─────────────────────────

_JOINT_BODY = b'{\n  "source": "x.xml",\n  "preset": "Baroque",\n  "analysisPath": "joint",\n  "regions": []\n}\n'
_LEGACY_BODY = b'{\n  "source": "x.xml",\n  "preset": "Baroque",\n  "analysisPath": "batch",\n  "regions": []\n}\n'
_NO_PATH_BODY = b'{\n  "source": "x.xml",\n  "preset": "Baroque",\n  "regions": []\n}\n'


def _build_corpus(dirpath: str, bodies: dict, requested_arm=None, schema=None) -> dict:
    """Write a corpus of {stem: body} plus a manifest, through the production writer."""
    os.makedirs(dirpath, exist_ok=True)
    for stem, body in bodies.items():
        with open(os.path.join(dirpath, f"{stem}.ours.json"), "wb") as fh:
            fh.write(body)
    manifest = rbp._write_manifest(
        Path(dirpath), "Baroque", {s: "OK" for s in bodies},
        expected_count=len(bodies), git_hash="t", timestamp="t", exe=None,
        requested_arm=requested_arm)
    if schema is not None:
        # An OLD manifest: the arm fields did not exist, so they are removed rather than
        # overwritten -- a schema-1 manifest that carries them would not be a schema-1
        # manifest, and the probe would be testing something that never existed.
        for k in ("inference_arm", "inference_arm_source", "inference_arm_requested",
                  "inference_arm_observed", "joint_inference_dir", "analysis_path_values"):
            manifest.pop(k, None)
        manifest["schema"] = schema
        with open(os.path.join(dirpath, cbf.MANIFEST_NAME), "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2, sort_keys=True)
    return manifest


# A probe runs against a REAL directory, so a refusal message names a real path -- and the
# probe directory is a fresh temporary one on every run, which would make this artifact
# unreproducible BY CONSTRUCTION. Caught by running --check straight after --establish, the
# same failure shape phase 1x met with a commit sha in captured output. The temporary root is
# replaced by a stable token in the CAPTURED messages only; the directory's own name survives,
# so the message still says which probe it came from, and no verdict is touched either way.
_PROBE_TMP_ROOT = ""


def _norm(message: str) -> str:
    return message.replace(_PROBE_TMP_ROOT, "<probe-tmp>") if _PROBE_TMP_ROOT else message


def _validate(dirpath: str, expect_arm=None) -> dict:
    """Offer a probe corpus to the production validator and record everything it did.

    The validator's own stderr is CAPTURED rather than left to escape, for two reasons. It is
    what the ARM-UNKNOWN notice is: a probe that deliberately builds an old-schema corpus
    provokes that warning on purpose, so the warning is EVIDENCE and belongs in the probe
    record -- which also lets probe 5 measure that the notice was actually printed, rather
    than only that nothing was raised. And letting it escape made this run's output carry a
    fresh temporary path, which is how `tools/audit/guard_state.json` (which captures this
    tool's output verbatim) became unreproducible by construction; caught by running that
    artifact's own --check twice in a row.
    """
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        try:
            cbf.validate_corpus_dir(Path(dirpath), expect_arm=expect_arm)
            result = {"refused": False, "message": ""}
        except cbf.CorpusValidationError as exc:
            result = {"refused": True, "message": _norm(str(exc))}
    result["stderr"] = [_norm(ln) for ln in buf.getvalue().splitlines() if ln.strip()]
    return result


def establish() -> dict:
    global _PROBE_TMP_ROOT
    tmp = tempfile.mkdtemp(prefix="corpus_arm_")
    _PROBE_TMP_ROOT = tmp
    try:
        joint_dir = os.path.join(tmp, "joint")
        legacy_dir = os.path.join(tmp, "legacy")
        old_dir = os.path.join(tmp, "old_schema")
        mixed_dir = os.path.join(tmp, "mixed")
        lied_dir = os.path.join(tmp, "invocation_disagrees")
        tampered_dir = os.path.join(tmp, "tampered")

        m_joint = _build_corpus(joint_dir, {"a": _JOINT_BODY, "b": _JOINT_BODY},
                                requested_arm=cbf.ARM_JOINT)
        m_legacy = _build_corpus(legacy_dir, {"a": _LEGACY_BODY, "b": _LEGACY_BODY},
                                 requested_arm=cbf.ARM_LEGACY)
        m_old = _build_corpus(old_dir, {"a": _NO_PATH_BODY}, schema=1)
        m_mixed = _build_corpus(mixed_dir, {"a": _JOINT_BODY, "b": _LEGACY_BODY},
                                requested_arm=cbf.ARM_JOINT)
        m_lied = _build_corpus(lied_dir, {"a": _LEGACY_BODY},
                               requested_arm=cbf.ARM_JOINT)

        # The pre-existing guard, unchanged: a file overwritten after the manifest was
        # written must still be caught as CONTAMINATION.
        _build_corpus(tampered_dir, {"a": _JOINT_BODY, "b": _JOINT_BODY},
                      requested_arm=cbf.ARM_JOINT)
        with open(os.path.join(tampered_dir, "a.ours.json"), "wb") as fh:
            fh.write(_JOINT_BODY + b"\n")

        right = _validate(joint_dir, expect_arm=cbf.ARM_JOINT)
        wrong = _validate(legacy_dir, expect_arm=cbf.ARM_JOINT)
        no_demand = _validate(legacy_dir, expect_arm=None)
        old = _validate(old_dir, expect_arm=cbf.ARM_JOINT)
        mixed = _validate(mixed_dir, expect_arm=cbf.ARM_JOINT)
        tampered = _validate(tampered_dir, expect_arm=cbf.ARM_JOINT)

        probes = {
            "1_the_stamp_reads_the_arm_off_the_files": {
                "what_it_measures": "That the recorded arm comes from the OUTPUT, not from the "
                                    "flag: two corpora written by the same call differ only in "
                                    "their files' analysisPath and are recorded differently.",
                "expected": "joint for the joint bodies, legacy for the batch bodies, and both "
                            "sourced to the files.",
                "observed": {"joint_dir_arm": m_joint["inference_arm"],
                             "joint_dir_source": m_joint["inference_arm_source"],
                             "legacy_dir_arm": m_legacy["inference_arm"],
                             "legacy_dir_source": m_legacy["inference_arm_source"]},
                "verdict": "READS THE OBJECT" if (
                    m_joint["inference_arm"] == cbf.ARM_JOINT
                    and m_legacy["inference_arm"] == cbf.ARM_LEGACY
                    and "produced" in m_joint["inference_arm_source"]) else "DOES NOT",
            },
            "2_a_wrong_arm_corpus_is_REFUSED": {
                "what_it_measures": "The detection D-436 asks for: a corpus produced by the "
                                    "other pipeline, offered to a measurement that declared "
                                    "which arm it is about.",
                "expected": "refused, with a message naming both arms.",
                "observed": wrong,
                "verdict": "DETECTED" if (wrong["refused"]
                                          and "WRONG INFERENCE ARM" in wrong["message"])
                           else "NOT DETECTED",
            },
            "3_a_right_arm_corpus_is_NOT_refused": {
                "what_it_measures": "The other half D-436 asks for: the check must not refuse "
                                    "the corpus it was built to admit.",
                "expected": "not refused.",
                "observed": right,
                "verdict": "ADMITTED" if not right["refused"] else "FALSELY REFUSED",
            },
            "4_an_undeclared_expectation_refuses_nothing": {
                "what_it_measures": "That the refusal is driven by a caller's DECLARED "
                                    "expectation, not by the arm value itself -- every "
                                    "existing caller passes no expectation and must behave "
                                    "exactly as before.",
                "expected": "the legacy corpus is not refused when nothing was expected.",
                "observed": no_demand,
                "verdict": "UNCHANGED" if not no_demand["refused"] else "BEHAVIOUR CHANGED",
            },
            "5_an_old_schema_manifest_is_ARM_UNKNOWN_and_NOT_fatal": {
                "what_it_measures": "The declared, bounded transition (#23): a manifest written "
                                    "before the field must be loud and must not be treated as "
                                    "if it carried an arm -- and must not be a hard failure "
                                    "while what those corpora are is still being established.",
                "expected": "not refused; corpus_arm reports ARM-UNKNOWN; and the notice is "
                            "actually PRINTED -- 'loud, named in the output, not a silent "
                            "pass' is the requirement, and a state that is merely tolerated "
                            "without being announced would satisfy the first two alone.",
                "observed": {"validate": old,
                             "corpus_arm": list(cbf.corpus_arm(m_old))},
                "retirement_condition": "characterise_bir_false.ARM_UNKNOWN_IS_FATAL flips to "
                                        "True once every corpus a measurement reads carries an "
                                        "established arm; this probe's expected verdict flips "
                                        "with it.",
                "verdict": "TRANSITION HOLDS" if (
                    not old["refused"]
                    and cbf.corpus_arm(m_old)[1] == "ARM-UNKNOWN"
                    and any("ARM-UNKNOWN" in ln for ln in old["stderr"]))
                    else "TRANSITION BROKEN",
            },
            "6_a_mixed_arm_directory_is_REFUSED": {
                "what_it_measures": "A directory holding output from both pipelines -- the "
                                    "shape a --resume or a partial regen produces. It is "
                                    "reported as mixed rather than resolved by majority.",
                "expected": "recorded arm 'mixed', and refused.",
                "observed": {"recorded_arm": m_mixed["inference_arm"], "validate": mixed},
                "verdict": "DETECTED" if (m_mixed["inference_arm"] == cbf.ARM_MIXED
                                          and mixed["refused"]) else "NOT DETECTED",
            },
            "7_a_disagreement_between_flag_and_output_is_VISIBLE": {
                "what_it_measures": "The case the manifest could not previously express: the "
                                    "invocation asked for one arm and the produced files "
                                    "report the other. Both are recorded, so the disagreement "
                                    "is in the record rather than resolved silently.",
                "expected": "requested joint, observed legacy, arm of record legacy (the "
                            "object wins over the intent).",
                "observed": {"requested": m_lied["inference_arm_requested"],
                             "observed": m_lied["inference_arm_observed"],
                             "arm_of_record": m_lied["inference_arm"]},
                "verdict": "VISIBLE" if (m_lied["inference_arm_requested"] == cbf.ARM_JOINT
                                         and m_lied["inference_arm_observed"] == cbf.ARM_LEGACY
                                         and m_lied["inference_arm"] == cbf.ARM_LEGACY)
                           else "HIDDEN",
            },
            "8_the_checks_that_existed_before_still_fire": {
                "what_it_measures": "The negative control: the arm work must not have weakened "
                                    "the guard it was added to. A file altered after the "
                                    "manifest was written is still CONTAMINATION.",
                "expected": "refused, on the fingerprint, before the arm is ever reached.",
                "observed": tampered,
                "verdict": "PRESERVED" if (tampered["refused"]
                                           and "CONTAMINATION" in tampered["message"])
                           else "WEAKENED",
            },
        }
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        _PROBE_TMP_ROOT = ""

    good = {"READS THE OBJECT", "DETECTED", "ADMITTED", "UNCHANGED", "TRANSITION HOLDS",
            "VISIBLE", "PRESERVED"}
    return {
        "purpose": "The measured establishment of the corpus inference-arm stamp and the check "
                   "that reads it: that a wrong-arm corpus is DETECTED, that a right-arm one is "
                   "NOT refused, and that nothing which used to be refused now passes.",
        "generated_by": "tools/audit/corpus_arm_stamp.py --establish",
        "generated_for": "cc_instruction_phase1y_corpus_arm_stamping.md, Tasks 1 and 2",
        "the_row_it_answers": "OPEN_ITEMS.md OI-307, whose remedy states the obligation in "
                              "these words: a corpus regenerated on the wrong arm must "
                              "actually be detected, and a correct one must not be refused.",
        "why_these_are_probes_and_not_assertions": "Every probe builds a real corpus directory "
                                                   "on disk, writes its manifest through the "
                                                   "production writer, and offers it to the "
                                                   "production validator. Nothing is simulated "
                                                   "and no branch is asserted from reading.",
        "one_normalization_and_why": "A refusal message names the directory it refused, and the "
                                     "probe directory is a fresh temporary one on every run. "
                                     "The temporary ROOT is replaced by '<probe-tmp>' in the "
                                     "captured messages, without which this artifact would be "
                                     "unreproducible by construction. Each probe directory's "
                                     "own name survives; no verdict is affected.",
        "probes": probes,
        "verdicts": {k: v["verdict"] for k, v in probes.items()},
        "established": all(v["verdict"] in good for v in probes.values()),
    }


def do_establish(check: bool) -> int:
    artifact = establish()
    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"
    rc = 0
    if check:
        have = ""
        if os.path.exists(ESTABLISH_OUT):
            with open(ESTABLISH_OUT, encoding="utf-8") as fh:
                have = fh.read()
        if have != text:
            print("STALE vs the run: corpus_arm_establishment.json does not re-derive")
            rc = 1
        else:
            print("the corpus-arm establishment re-derives")
    else:
        with open(ESTABLISH_OUT, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        print(f"wrote {os.path.relpath(ESTABLISH_OUT, ROOT)}")
    for name, verdict in artifact["verdicts"].items():
        print(f"  {name}: {verdict}")
    print(f"established: {artifact['established']}")
    return rc or (0 if artifact["established"] else 1)


def main(argv: list[str]) -> int:
    if "--establish" in argv:
        return do_establish("--check" in argv)
    if "--apply" in argv:
        return do_apply("--all" in argv)
    if "--check" in argv:
        return do_check()
    if "--scan" in argv:
        return do_scan()
    print(__doc__.strip().splitlines()[0])
    print("usage: --scan | --check | --apply [--all] | --establish [--check]")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
