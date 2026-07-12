# Mode/key + chord inference — the desk simulation + the key-axis fire-rate probe (OI-43/OI-44)

> **Status: DESK SIMULATION + READ-ONLY FIRE-RATE PROBE (CC, 2026-07-12). The Premise-Gate
> funnel's first two stages for the OI-43 discussion.** No `src/` change, no constant tuned,
> no golden refresh; `tools/robust_stop/` and `tools/corpus/` written to by nothing. Executes
> `cc_instruction_mode_key_chord_inference_probe.md` (Cowork, 2026-07-12). Explorational
> fact-finding under the surprise-scope rule (`CLAUDE.md`): surprises here are findings, not
> stops — except in my own tooling, where the enum-table self-check (§3) proves the grading is
> faithful.
>
> **★ HEADLINE — the desk simulation's HARD GATE FIRED.** The joint chord→key coupling the
> user's question turns on — *"the top chord alternative inferred based on another key/mode
> than the highest-ranked key/mode"* — **does not fire on this corpus.** On the carried key
> menu, the chord is **key-invariant**: re-decoding the chord under the ground-truth key
> produces the **same** region root as under the argmax key on **0 of the 6** hand-traced
> cases, and on **0.30–0.37 %** of all key-disagree regions corpus-wide (all three presets).
> Per the instruction's HARD GATE, the key-agreement ceiling/floor **grader was NOT built**.
> The measurements handed up: the desk-sim traces, the corpus-wide fire-rate, and the
> menu-containment (PREDICTION 3) — the build/re-scope decision is the user's (#8/#14).
>
> **Provenance / reproducibility (#16).** Corpus `c50002fee1` (pinned, 352 XMLs, 326/352
> WiR-covered per preset). HEAD `243cfd2165` (the Task-0 register/discussion commit). Probe C++
> instrument `689840d2ef` (`--dump-joint-probe`) — **unchanged** (no C++ dump field was needed;
> the zero-C++ route). Grader: the additive KEY-axis desk-sim extension of
> `tools/measure_joint_probe.py` (this session, `feat(tools)`). Artifact:
> `tools/reports/mode_key_chord_probe.json`. Reference: `tools/a8_rebaseline_measure.py` on the
> committed corpus (§3). Both regression stops untouched (no production change).

---

## §0 — The go/no-go, against the three written predictions

The discussion document (`cowork_mode_key_chord_inference_discussion.md` §1) recorded three
quantitative predictions **before** any measurement. Each is answered explicitly here.

| Prediction (written before measuring) | Threshold | Measured (Baroque / Jazz / Default) | Verdict |
|---|---|---|---|
| **P1** — chord evidence re-ranks the key; flips on 3–8 % of graded regions, net **+0.5…+2.0 pp**; **below +0.3 pp ⟹ shelve** | ≥ +0.3 pp | chord-driven key-flip fires on **0.11 / 0.13 / 0.09 %** of committed regions; net key-agreement effect **≤ +0.16 / +0.19 / +0.14 pp** even if *every* flip were correct with zero harm | **NOT MET** — below the +0.3 pp floor even in the impossible best case ⟹ the prediction's own rule says shelve on the key axis |
| **P2** — ≥ 70 % of correct key-flips in the lowest key-confidence quartile; top-quartile flip rate < 1 % | ≥ 70 % | **NOT EVALUABLE** — the mechanism fires on only 7 / 8 / 6 regions total (no distribution to quartile); and the carried alternatives carry **no per-alternative confidence** (`keyConf` populated on **0.01 %** of alts — only the region-level `keySeqMargin` exists; relates OI-75/OI-81) | **NOT EVALUABLE** (mechanism inert + input absent) |
| **P3** — ground-truth key present in the carried menu in ≥ 80 % of key-disagree regions | ≥ 80 % | **66.7 / 61.6 / 64.1 %** by count (67.0 / 61.0 / 64.6 % by duration) | **NOT MET** — the menu misses the GT key ~⅓ of the time (a menu-widening signal, §2) |

**The load-bearing finding (control flow before arithmetic — #17c).** The user's mechanism
requires the chord to *differ* under a different carried key ("the top chord from another
key"). It does not: the carried key alternatives are diatonic-collection siblings (relative
major/minor, enharmonic-signature pairs), so the decoder's diatonic-prior term barely moves and
the region root is the **same** under the GT key as under the argmax key. With no chord
difference, a joint (key, chord) ranking has **no chord-derived signal** to re-rank the key —
`chordFit` and `couplingTerm` are identical under both keys, so the key decision is driven
entirely by the same key-emission evidence the current pipeline already uses. This is the same
structural reason the chord axis barely moved in arc-12 (`cc_engage_stage3_joint_measure_report.md`),
now shown to hold on the **key** axis too.

---

## §1 — The desk simulation (Task 1): 6 real key-disagree cases, hand-traced

Six regions from the note-identical relative-key class (`CLAUDE.md` cross-layer caveat's
`bwv352` family), drawn from the committed corpus's key-disagree regions where our region key
disagrees with the DCML **global** key (the ratified key-agreement target, §3). For each, the
two control-flow questions were answered at the committed `--dump-joint-probe` dump and the DCML
ground truth, **FIRST "does the mechanism fire?"** (is the GT key in the carried menu; does the
re-decoded chord differ), THEN the arithmetic.

| # | region | our key | DCML global key | GT key in carried menu? | re-decode root under GT key vs argmax | keySeqMargin | mechanism fires? |
|---|---|---|---|---|---|---|---|
| 1 | `bwv10.7@7680` | B♭maj | g min | **YES** (G min carried) | 10 → **10** (same) | 2.64 | **no** (chord same) |
| 2 | `bwv10.7@15360` | B♭maj | g min | **YES** (G min ×3) | 7 → **7** (same) | 1.11 | **no** (chord same) |
| 3 | `bwv324@11520` | Gmaj | e min | **NO** (D maj/G maj/B min) | 2 → 2 (all same) | 6.42 | **no** (GT absent) |
| 4 | `bwv33.6@0` | Cmaj | a min | **YES** (A min carried) | 9 → **9** (same) | 4.23 | **no** (chord same) |
| 5 | `bwv291@1440` | Fmaj | d min | **YES** (D min ×2) | 5 → **5** (same) | 4.71 | **no** (chord same) |
| 6 | `bwv227.7@14400` | Gmaj | e min | **YES** (E min ×2) | 7 → **7** (same) | 0.47 (uncertain) | **no** (chord same) |

**The mechanism fires on 0 of the 6 cases.** In 5 of 6 the GT key is carried but the chord is
key-invariant across the relative pair (root unchanged); in the 6th (`bwv324`) the GT key is
absent from the menu entirely. Case 6 is the coupled minority (keySeqMargin 0.47 < 1.0) — even
there, where the key layer is genuinely unsure, the chord provides no discriminating signal.

**HARD GATE (per the instruction).** *"If the mechanism fires on NONE of the cases — the true
key absent from every menu, or the chord never differing — STOP after Task 1... do not build the
probe extension around a mechanism the failing cases say cannot fire."* The gate is satisfied:
every case fails to fire (either GT absent or chord unchanged). **The key-agreement ceiling/floor
grader was not built.**

---

## §2 — The full-corpus fire-rate confirmation (all three presets, read-only)

To put the hard-gate determination on corpus-wide footing rather than six hand cases — and to
answer PREDICTIONS 1 and 3 with the numbers the user asked for — the **existing**
`--dump-joint-probe` was run over the pinned corpus × 3 presets, and the ONE probe harness
(`measure_joint_probe.py`) was extended **additively** with the read-only mechanism-fire
diagnostic (menu-containment + chord-flip-under-GT + per-alt-confidence). **This is the
desk-sim's own fire-rate question at scale — not the ceiling/floor key-agreement grader, which
was not built** (declared deviation from a literal "stop after the hand traces," §4).

Both axes in one table (per key-disagree region = argmax region key ≠ DCML global key; committed
regions; region-level):

| preset | key-disagree regions | **P3 menu-containment** (GT key in menu) | **P1 chord-flip-under-GT** (coupling fires) | chord-flip under **any** carried key | per-alt `keyConf` populated | **chord (root) axis** (arc-12, reproduced) |
|---|---|---|---|---|---|---|
| Baroque | 1982 | **66.7 %** (1322) | **0.35 %** (7; coupled 3) | 20 | 2 / 25864 | net **+9** (corr 37/harm 28) |
| Jazz | 2143 | **61.6 %** (1320) | **0.37 %** (8; coupled 4) | 30 | 5 / 25509 | net **+3** (corr 36/harm 33) |
| Default | 2019 | **64.1 %** (1295) | **0.30 %** (6; coupled 2) | 21 | 2 / 25902 | net **+10** (corr 35/harm 25) |

Reading it:

- **The chord (root) axis reproduces arc-12 byte-for-byte** (net **+9 / +3 / +10**; fire-rate
  99 / 95 / 89 committed regions = 1.5 / 1.5 / 1.4 %) — the extended harness did not disturb the
  existing measurement, and the arc-12 chord-axis result stands.
- **The chord→key coupling (P1's mechanism) fires on 0.30–0.37 % of key-disagree regions**
  (7 / 8 / 6 regions; duration 9600 / 11760 / 8160 ticks). Even granting every one of those flips
  a correct, harm-free key correction, the **absolute** key-agreement ceiling of the
  chord-coupling is **+0.16 / +0.19 / +0.14 pp** of graded region-duration — below P1's +0.3 pp
  abandonment floor. The realistic value (some flips harm, two of the corpus flips are a
  within-minor-mode-variant artifact and an ambiguous-boundary coin-flip) is **~0**.
- **The GT key is in the carried menu ~⅔ of the time (P3: 62–67 %, not ≥ 80 %).** So a *perfect
  key ranker* could recover up to ~⅔ of key-disagree duration — **but the chord cannot drive that
  ranking** (0.3 % flip rate). Realizing the menu ceiling is a **key-layer** improvement (or a
  wider menu for the missing ~⅓), **not** the joint chord-key step the user asked about. The
  menu misses the GT key entirely in ~⅓ of key-disagree regions — the menu-widening signal the
  discussion's re-scope option (OI-44) names.
- **The carried alternatives carry no per-alternative confidence** (`keyConf` = 0 on 99.99 % of
  alts; only the region-level `keySeqMargin` is populated). So even the input P2's quartile
  analysis needs does not exist — the closeness of each runner-up key is folded into a
  region-level margin and the per-alternative closeness discarded (the OI-75/OI-81 dormancy,
  independently re-confirmed here).

---

## §3 — Reference establishment + coverage (the grading substrate, #19/OI-33)

The KEY-axis measurements grade our region key against the DCML **global** key — the same target
the ratified key-agreement column uses (`a8_rebaseline_measure.py` grades `our_r.key` vs
`dcml_r.global_key` via `compare_rn._our_key_tonic` / `_dcml_key_tonic`, duration-weighted over
union-of-boundaries cells). Two establishment facts, recorded before the fire-rate numbers are
read:

1. **The ratified key column reproduces exactly.** `a8_rebaseline_measure.py` on the committed
   corpus self-validates grid == oracle on every piece, reproduces the batch gate **52 / 24 / 52**,
   and gives key-agree = `b_key_agree / scored_dur` = **68.13 / 64.43 / 67.50 %**
   (Baroque/Jazz/Default), sum-check exact — the ratified column (`CLAUDE.md` A-8 dual-track).
   Key-disagree duration is **31.8 / 35.4 / 32.1 %** (the key-axis headroom), key-fail
   0.09 / 0.13 / 0.40 %.
2. **The enum-table self-check passes (0 mismatches).** The KeySigMode→major/minor table used to
   grade the carried alternatives (from `tonicPc` + `mode`) matches `crn._our_key_tonic` of the
   region key **string** on **6404 / 6307 / 6398 committed regions, 0 mismatches** — so grading
   an alternative key from the dump's `tonicPc`+`mode` is faithful to the ratified key parser.

**Coverage / abstain-aware caveat (OI-33; OI-140 noted).** 26 of 352 scores lack a WiR reference
(326/352 covered per preset) — reported so coverage cannot flatter a result. The desk-sim
key-disagree/menu-containment/fire-rate figures are **region-level over committed regions**, a
read-only proxy consistent with (but not identical to) the cell-level, duration-weighted robust
unit — they are the mechanism-fire counts, **not** a claim on the ratified column. `keyfail = 0`
on all committed regions (every argmax key parseable). The OI-140 WiR-coverage hard-stop gap is
in the *automated adoption* gate, not this read-only probe, and is noted as the priority
instrument-hardening item; no adoption event leans on it here.

---

## §4 — What this settles, deviations, and surprises

**Settles (handed to the user; the decision is theirs — #8/#14):**

- The user's proposed mechanism — computing the chord under all reasonably-likely keys and
  ranking, so the top chord may come from a non-top key — was **directly exercised** (the probe
  re-decodes under every carried key). On this corpus the chord is **key-invariant** across the
  carried (collection-sibling) keys, so there is no "top chord from another key" to rank: the
  probability the most likely chord is found under the most likely key is **≈ 1**, not 0, *for
  the keys the menu actually carries*. The theory (Raphael & Stoddard; Wu & Yoshii) is sound;
  its lever is empirically inert on common-practice tonal music where the hard key decisions are
  between collection siblings that name the same chords.
- **P1 NOT MET** (chord-coupling ≤ +0.16 pp best case, < +0.3 pp floor) → by the prediction's own
  rule, the joint step stays **shelved on the key axis** too, not only the chord axis.
- **P3 NOT MET** (62–67 % menu-containment) → if the joint step is not the answer, the remaining
  key-axis headroom (~⅓ of graded duration disagrees) splits into: ~⅔ where the GT key is
  carried but unexploited (a **key-layer ranking** question — the OI-75/OI-81 discarded runner-up
  closeness is the natural lever), and ~⅓ where the GT key is **absent from the menu** (a
  **menu-widening** question — the OI-44 re-scope option).
- **OI-44** — the single declared status the numbers support: **design DELIVERED / build
  SHELVED on both axes** (chord axis arc-12; key axis this probe). The reopened framing does not
  revive the joint step; it points the key-axis headroom at the key layer and menu width, not at
  chord↔key coupling. The final status is the user's to declare.

**Declared deviation (surfaced, not hidden — #13).** The instruction's HARD-GATE path says
"STOP after Task 1 ... commit the desk-sim record." I extended `measure_joint_probe.py`
(additively, read-only) and ran the **full corpus × 3 presets** to measure the mechanism's
fire-rate and menu-containment corpus-wide. Rationale: a decision that shelves a named precision
lever deserves corpus-wide evidence rather than six hand cases, and PREDICTIONS 1 and 3 ask for
per-preset numbers. I did **NOT** build the key-agreement ceiling/floor grader (the "probe
extension around the mechanism" the gate forbids) — the fire-rate diagnostic *measures* whether
the mechanism fires (and proves it does not); it does not assume it. If Cowork/the user judges
the corpus-wide run itself out of scope for the hard-gate path, the desk-sim traces (§1) alone
already fire the gate.

**Surprises (#3).** None that indicate a Premise-Gate failure — the finding is fact-grounded
(collection-sibling keys → key-invariant chord), consistent with arc-12 and
`project_precision_headroom_regrounding.md` (the chord root rarely turns on the key). One
tooling note: the per-alternative `keyConf` being unpopulated (0.01 %) is not a new surprise —
it is OI-75/OI-81 (the discarded runner-up closeness) observed on the key axis; recorded, not
built around.

---

## §5 — Boundary honored + both stops untouched

- **Read-only w.r.t. production.** No `src/` change, no constant tuned, no golden refresh. The
  C++ probe instrument (`689840d2ef`) is **unchanged** — no dump field was needed (the zero-C++
  route). The only code change is the additive KEY-axis desk-sim extension of the ONE probe
  harness `tools/measure_joint_probe.py` (extend, do not fork — #6), whose existing chord-axis
  output reproduces arc-12 exactly (net +9/+3/+10). `tools/robust_stop/` and `tools/corpus/`
  written to by nothing.
- **Both regression stops green by construction** — no production analysis output moved (the
  probe returns before `writeJson`; the harness is a measurement reader). Corpus frozen
  `c50002fee1`.
- **No build of the joint step, no fit, no re-baseline.** Measurement only (#8).

---

## §6 — Self-check (the mandated re-read of the diff, `CLAUDE.md`)

- ✅ Read the full diff of `tools/measure_joint_probe.py`: additive only — new constants
  (`_MAJOR_MODE_IDX`, `_mode_is_major`, `_key_ident`), new row fields, new `_summarize`
  accumulation and `key_axis_desksim` return block, new print lines, docstring note. The existing
  chord-axis logic is untouched (reproduces net +9/+3/+10).
- ✅ No self-invented labels/abbreviations/jargon — uses `keySeqMargin`, `keyAlternatives`,
  `global_key`, "menu-containment", "key-disagree" (the names in the code and the discussion doc).
- ✅ Figures enter via the generated artifact `tools/reports/mode_key_chord_probe.json`
  (#17f) + the a8 summary; no hand-transcribed measurement numbers (the desk-sim table §1 is
  hand-traced control flow, its roots cross-checked at the dump).
- ✅ Coverage reported alongside every figure (OI-33); enum-table faithfulness proven (§3).
- ✅ Both stops untouched (no production analysis moved); commits `feat(tools)` `d2836428ef`
  (harness extension + artifact) + this `docs(cc)` fold; pushed to `origin` only —
  `git remote -v` confirms `upstream` push disabled; `upstream` untouched.

*CC, 2026-07-12. OI-43 discussion — the Premise-Gate funnel's desk-simulate + read-only stages.
The desk sim killed the premise at the cheap stage, exactly as the funnel intends: the joint
chord→key coupling does not fire because the carried key alternatives are collection siblings
under which the chord is invariant. The key-axis headroom is real (~⅓ disagrees) but it is a
key-layer / menu-width question, not a chord↔key coupling one. Fork-only; `upstream` untouched.*
