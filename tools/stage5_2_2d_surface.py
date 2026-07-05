#!/usr/bin/env python3
"""stage5_2_2d_surface.py — Phase 2.2d decision surface for the full-feasible candidate(s)
(MEASUREMENT ONLY; nothing adopted).

For each candidate (srib, kw) [bassNoteRootBonus fixed 0.70]:
  - held-out (65) scored ONCE + fitting (261) — the overfit check;
  - full-corpus x3 carriers: root/RN/key, batch set-diff vs the frozen 53/24/53 (explained
    per case with class), class-(b)/(a) durations;
  - D-4 Default adopt-with-Baroque eligibility (measured);
  - Jazz: BYTE-IDENTICAL by construction (srib is per-preset -> Baroque/Default adopt targets
    only; kw is O-9 per-carrier-delivered -> Jazz keeps 0.10; bnrb unchanged). Spot-verified
    ONCE by a no-Jazz-override regen == frozen jazz.
  - DLC generalization probe (run_dlc_baseline --param-override, Default config, 3 styles);
  - snapshot-impact preview (batch_analyze --dump-regions notation, 11 goldens, cand vs base).

Baseline = the FROZEN tools/corpus/<preset> (all-on, byte-identical to the RETIRE-4 binary),
measured read-only. The frozen corpus is NEVER regenerated/written. Reuses stage5_fit_driver
(regen/measure), run_dlc_baseline.py, batch_analyze. Writes committed
tools/fit_ledgers/stage5_2_2d_surface.jsonl.
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import stage5_fit_driver as drv  # regen, measure, write_override, split_scores_file

SCRATCH = Path("C:/tmp/stage5_2_2d/surface")
FROZEN = _ROOT / "tools" / "corpus"
LEDGER = _ROOT / "tools" / "fit_ledgers" / "stage5_2_2d_surface.jsonl"
BA = _ROOT / "ninja_build_rel" / "batch_analyze.exe"
BASH = Path("C:/Program Files/Git/usr/bin/bash.exe")
DLC_RESULTS = _ROOT / "tools" / "corpus_dlc_wave1" / "results.json"

BNRB = 0.70
# adopt targets get the fitted srib (per-preset); Jazz keeps its own default (A-3)
ADOPT_TARGETS = {"Baroque", "Default"}

# the 2 tied top-gain full-feasible candidates (srib, kw); bnrb fixed 0.70
CANDIDATES = [(0.40, 0.125), (0.425, 0.125)]

SNAP_SCORES = [
    "tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx",
    "tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx",
    "tools/dcml/bach_en_fr_suites/MS3/BWV806_01_Prelude.mscx",
    "tools/dcml/bach_en_fr_suites/MS3/BWV806_10_Gigue.mscx",
    "tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx",
    "tools/dcml/mozart_piano_sonatas/MS3/K280-1.mscx",
    "tools/dcml/chopin_mazurkas/MS3/BI105-1op30-1.mscx",
    "tools/dcml/chopin_mazurkas/MS3/BI105-2op30-2.mscx",
    "tools/dcml/corelli/MS3/op01n08a.mscx",
    "tools/dcml/schumann_kinderszenen/MS3/n01.mscx",
    "tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx",
]


def winpath(p):
    return str(Path(p).resolve()).replace("\\", "/")


def carrier_override(srib, kw, carrier):
    """The adoption override for `carrier`: kw + bnrb always; srib only on the adopt targets
    (per-preset -> Jazz keeps its own default). For Jazz this returns {} => byte-identical."""
    ov = {"kWStepIn": kw, "bassNoteRootBonus": BNRB}
    if carrier in ADOPT_TARGETS:
        ov["sameRootInversionBonus"] = srib
    return ov


def diffs(m, b):
    added = sorted((c, m["cases"][c]) for c in m["cases"] if c not in b["cases"])
    removed = sorted((c, b["cases"][c]) for c in b["cases"] if c not in m["cases"])
    changed = sorted((c, b["cases"][c], m["cases"][c]) for c in m["cases"]
                     if c in b["cases"] and m["cases"][c] != b["cases"][c])
    new_b = [c for c, cl in added if cl == "b"]
    return added, removed, changed, new_b


def dlc_probe(override_file, tag):
    cmd = [sys.executable, str(_ROOT / "tools" / "run_dlc_baseline.py"),
           "--corpora", "corelli,mozart_piano_sonatas,schumann_kinderszenen",
           "--limit", "12", "--timeout", "120"]
    if override_file:
        cmd += ["--param-override", str(override_file)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    res = {}
    if DLC_RESULTS.exists():
        try:
            data = json.loads(DLC_RESULTS.read_text(encoding="utf-8"))
            for style, v in data.items():
                if isinstance(v, dict) and v.get("root_agree_pct") is not None:
                    res[style] = round(v["root_agree_pct"], 2)
        except Exception as e:
            print(f"  DLC parse err ({tag}): {e}", flush=True)
    print(f"  DLC[{tag}] rc={r.returncode} {res}", flush=True)
    return res


def snapshot_preview(override_file, scratch):
    """Return the count (and list) of the 11 goldens whose Default --dump-regions notation
    output DIFFERS between candidate and baseline."""
    tmp = scratch / "snap"
    tmp.mkdir(parents=True, exist_ok=True)
    differ = []
    for i, sc in enumerate(SNAP_SCORES):
        base_out = tmp / f"base_{i}.json"
        cand_out = tmp / f"cand_{i}.json"
        for out, ov in ((base_out, None), (cand_out, override_file)):
            cmd = (f'{winpath(BA)} "{winpath(sc)}" "{winpath(out)}" --preset Default '
                   f'--dump-regions notation')
            if ov:
                cmd += f' --param-override "{winpath(ov)}"'
            subprocess.run([str(BASH), "-c", cmd], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, timeout=120)
        try:
            b = base_out.read_text(encoding="utf-8", errors="replace")
            c = cand_out.read_text(encoding="utf-8", errors="replace")
            if b != c:
                differ.append(Path(sc).stem)
        except Exception:
            differ.append(Path(sc).stem + "(read-err)")
    return differ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dlc", action="store_true", help="also run the DLC probe")
    ap.add_argument("--snapshot", action="store_true", help="also run the snapshot preview")
    ap.add_argument("--jazz-verify", action="store_true",
                    help="spot-verify Jazz byte-identity (no-override regen == frozen jazz)")
    args = ap.parse_args()

    SCRATCH.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text("")

    fit_file = drv.split_scores_file("fitting", SCRATCH)
    held_file = drv.split_scores_file("held_out", SCRATCH)

    print("== FROZEN baselines (all-on; NO regen) ==", flush=True)
    b_bar = drv.measure("Baroque", FROZEN, SCRATCH / "a8_b_bar")
    b_def = drv.measure("Default", FROZEN, SCRATCH / "a8_b_def")
    b_jazz = drv.measure("Jazz", FROZEN, SCRATCH / "a8_b_jazz")
    b_fit = drv.measure("Baroque", FROZEN, SCRATCH / "a8_b_fit", fit_file)
    b_held = drv.measure("Baroque", FROZEN, SCRATCH / "a8_b_held", held_file)
    print(f"  Baroque full root={b_bar['root_pct']:.4f} batch={b_bar['batch_gate']} | "
          f"Default full root={b_def['root_pct']:.4f} batch={b_def['batch_gate']} | "
          f"Jazz full root={b_jazz['root_pct']:.4f} batch={b_jazz['batch_gate']}", flush=True)
    print(f"  fitting(261) root={b_fit['root_pct']:.4f} | held-out(65) root={b_held['root_pct']:.4f}",
          flush=True)

    if args.jazz_verify:
        # adoption writes NO Jazz override -> regen Jazz with no override == frozen jazz
        jscratch = SCRATCH / "jazz_verify"
        drv.regen("Jazz", None, jscratch)
        m_jz = drv.measure("Jazz", jscratch, SCRATCH / "a8_jzv")
        same = (m_jz["cases"] == b_jazz["cases"] and m_jz["batch_gate"] == b_jazz["batch_gate"])
        print(f"  JAZZ byte-identity spot-check (no-override regen vs frozen): "
              f"batch {m_jz['batch_gate']} vs {b_jazz['batch_gate']} cases-match={m_jz['cases']==b_jazz['cases']} "
              f"-> {'PASS' if same else 'FAIL'}", flush=True)

    for srib, kw in CANDIDATES:
        tag = f"s{srib}_k{kw}"
        scratch = SCRATCH / tag
        scratch.mkdir(parents=True, exist_ok=True)
        print(f"\n== CANDIDATE srib={srib} kw={kw} bnrb={BNRB} ==", flush=True)

        # Baroque: regen once -> full + fitting + held-out
        ovb = scratch / "ov_baroque.txt"
        drv.write_override(carrier_override(srib, kw, "Baroque"), "Baroque", ovb)
        drv.regen("Baroque", str(ovb).replace("\\", "/"), scratch)
        m_bar = drv.measure("Baroque", scratch, scratch / "a8_bar")
        m_fit = drv.measure("Baroque", scratch, scratch / "a8_fit", fit_file)
        m_held = drv.measure("Baroque", scratch, scratch / "a8_held", held_file)

        # Default: regen -> full
        ovd = scratch / "ov_default.txt"
        drv.write_override(carrier_override(srib, kw, "Default"), "Default", ovd)
        drv.regen("Default", str(ovd).replace("\\", "/"), scratch)
        m_def = drv.measure("Default", scratch, scratch / "a8_def")

        ab, rb, cb, nbb = diffs(m_bar, b_bar)
        ad, rd, cd, nbd = diffs(m_def, b_def)
        d4_eligible = (round(m_def["root_pct"] - b_def["root_pct"], 4) > 0
                       and len(nbd) == 0 and (m_def["cls_b_dur"] - b_def["cls_b_dur"]) <= 0)

        rec = {
            "record": "surface", "sameRootInversionBonus": srib, "kWStepIn": kw,
            "bassNoteRootBonus": BNRB,
            "overfit": {
                "fitting_base": round(b_fit["root_pct"], 4), "fitting_cand": round(m_fit["root_pct"], 4),
                "fitting_delta": round(m_fit["root_pct"] - b_fit["root_pct"], 4),
                "heldout_base": round(b_held["root_pct"], 4), "heldout_cand": round(m_held["root_pct"], 4),
                "heldout_delta": round(m_held["root_pct"] - b_held["root_pct"], 4),
            },
            "baroque": {
                "root_base": round(b_bar["root_pct"], 4), "root_cand": round(m_bar["root_pct"], 4),
                "root_delta": round(m_bar["root_pct"] - b_bar["root_pct"], 4),
                "rn_delta": round(m_bar["rn_pct"] - b_bar["rn_pct"], 4),
                "key_delta": round(m_bar["key_pct"] - b_bar["key_pct"], 4),
                "batch_base": b_bar["batch_gate"], "batch_cand": m_bar["batch_gate"],
                "added": ab, "removed": rb, "changed": cb, "new_class_b": nbb,
                "cls_b_dur_delta": m_bar["cls_b_dur"] - b_bar["cls_b_dur"],
                "cls_a_dur_delta": m_bar["cls_a_dur"] - b_bar["cls_a_dur"],
            },
            "default": {
                "root_base": round(b_def["root_pct"], 4), "root_cand": round(m_def["root_pct"], 4),
                "root_delta": round(m_def["root_pct"] - b_def["root_pct"], 4),
                "rn_delta": round(m_def["rn_pct"] - b_def["rn_pct"], 4),
                "key_delta": round(m_def["key_pct"] - b_def["key_pct"], 4),
                "batch_base": b_def["batch_gate"], "batch_cand": m_def["batch_gate"],
                "added": ad, "removed": rd, "changed": cd, "new_class_b": nbd,
                "cls_b_dur_delta": m_def["cls_b_dur"] - b_def["cls_b_dur"],
                "cls_a_dur_delta": m_def["cls_a_dur"] - b_def["cls_a_dur"],
            },
            "jazz_byte_identical_by_construction": True,
            "d4_default_eligible": d4_eligible,
        }
        print(f"  OVERFIT fitting {b_fit['root_pct']:.4f}->{m_fit['root_pct']:.4f} "
              f"({m_fit['root_pct']-b_fit['root_pct']:+.4f}) | held-out "
              f"{b_held['root_pct']:.4f}->{m_held['root_pct']:.4f} "
              f"({m_held['root_pct']-b_held['root_pct']:+.4f})", flush=True)
        for cr, m, b, a, r, c, nb in (("Baroque", m_bar, b_bar, ab, rb, cb, nbb),
                                       ("Default", m_def, b_def, ad, rd, cd, nbd)):
            print(f"  [{cr}] root {b['root_pct']:.4f}->{m['root_pct']:.4f} "
                  f"({m['root_pct']-b['root_pct']:+.4f}) rn_d={m['rn_pct']-b['rn_pct']:+.4f} "
                  f"key_d={m['key_pct']-b['key_pct']:+.4f} batch {b['batch_gate']}->{m['batch_gate']} "
                  f"+{len(a)}/-{len(r)}/~{len(c)} newB={len(nb)} "
                  f"clsBd={m['cls_b_dur']-b['cls_b_dur']:+g} clsAd={m['cls_a_dur']-b['cls_a_dur']:+g}",
                  flush=True)
            print(f"      added={a}\n      removed={r}\n      changed={c}", flush=True)
        print(f"  D-4 Default eligible: {d4_eligible}", flush=True)

        if args.dlc:
            base_dlc = dlc_probe(None, "baseline")
            cand_dlc = dlc_probe(str(ovd).replace("\\", "/"), tag)  # Default adopt vector
            rec["dlc"] = {"baseline": base_dlc, "candidate": cand_dlc,
                          "delta": {k: round(cand_dlc.get(k, 0) - base_dlc.get(k, 0), 2)
                                    for k in base_dlc}}
            print(f"  DLC delta: {rec['dlc']['delta']}", flush=True)

        if args.snapshot:
            differ = snapshot_preview(ovd, scratch)  # Default adopt vector
            rec["snapshot_differ"] = differ
            rec["snapshot_differ_count"] = len(differ)
            print(f"  SNAPSHOT: {len(differ)}/11 goldens differ -> {differ}", flush=True)

        with open(LEDGER, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, sort_keys=True) + "\n")

    print(f"\nSURFACE DONE -> {LEDGER}", flush=True)


if __name__ == "__main__":
    main()
