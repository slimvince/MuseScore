# CC — The combined re-baseline: parent-collection mode grading + the calibration refit (OI-132 / OI-144) — report

**Dispatch:** `cc_instruction_key_grading_and_calibration_rebaseline.md` (Cowork, 2026-07-13). Two
corrections that both move recorded figures, executed as ONE ritual event: one outgoing snapshot,
sequential implementation with clean attribution, one ratification pause with everything side by
side, then two separately-revertible landing commits.

**Ruling:** the user, 2026-07-12 (OI-132) — the dominant-family exotic modes reduce by the
PARENT-COLLECTION rule, uniformly, all five modes.
**Ratified:** the user, 2026-07-13 — "Land both A and B".

| | commit |
|---|---|
| Register (Cowork's waiting edits) | `0bc49b4b48` |
| **O-12 outgoing snapshot** (before any change) | **`23e21da8ea`** |
| **A — the grading consolidation** | **`800f1a12bf`** |
| **B — the routing + calibration refit** | **`b3511fd28a`** |
| The fold (this report) | this commit |

HEAD at start `c1bc9bb513`; corpus `c50002fee1` (untouched); **no `src/` change; no constant tuned;
no golden refreshed; no score and no ground-truth file edited.**

---

## 1. The headline: a load-bearing premise of the dispatch was FALSE, and is recorded, not absorbed

The instruction stated, as the basis for Correction B's whole verification plan:

> "The maps are consumed at analysis time, so this is a **PRODUCTION-BEHAVIOR change** … any changed
> `.ours.json` is part of the adoption … if the drift is LARGE … stop and report."

**At the code, they are not consumed at analysis time.** Enumerated repo-wide:

- The four `tools/calibration_maps/*.json` are read by **exactly two Python instruments** —
  `tools/conformal_check.py` and `tools/theta_fit.py`. Both declare themselves measurement-only
  (`theta_fit`: "RECORDED, NOTHING WIRED … No behaviour change"; `calibration_fit`, the producer:
  "MEASUREMENT + ARTIFACT ONLY. No behaviour change").
- **No C++, CMake, or resource file references them** (grep over `src/`, `muse/`, all `*.cpp/h/txt/cmake/qrc`).
- `tools/batch_analyze.cpp` — the harness that produces every `.ours.json` — reads **only the score
  and its command-line parameters**; its single `QFile` is the *output* file.
- `tools/run_bach_preset.py` (the corpus producer) imports **only stdlib** and shells out to the binary;
  it cannot see a calibration map.

**Established empirically as well as at the code** (#19 — positively established, not merely unfalsified):
the mandated full corpus regeneration was run anyway, through the committed gate
(`hardening_battery.py --corpus-regen`: 352 scores × 3 presets, every `.ours.json` sha256'd against the
committed corpus):

```
[PASS] corpus_regen   baroque: 0 differ; jazz: 0 differ; default: 0 differ
```

**Consequence:** the refit is a **measurement-artifact re-baseline**, not a production-behavior change.
No production region moved; **no golden refresh was owed**; the "if drift is large, stop" contingency was
moot. The insulation claim's false-negative path (#17e) is enumerated above: the only way a map could
reach production is through a reader, and every reader is named.

*Why this is reported at the top rather than buried: the premise was checkable and unchecked (#18), and
the correct response to a refuted premise is to surface it before building around it (#13). It changed no
implementation — the refit was correct and needed either way — only which verification was owed.*

---

## 2. Correction A — the parent-collection mode grading (OI-132), landed `800f1a12bf`

### 2.1 What was built

The five dominant-family modes have a **major tonic triad** but a **minor parent collection** — each is a
rotation of a harmonic- or melodic-minor scale. They now reduce to the **minor key of that parent**:

| emitted mode | rotation | parent tonic | example |
|---|---|---|---|
| PhrygDom | 5th mode of harmonic minor | emitted − 7 | C♯PhrygDom → **F♯ minor** |
| Mix♭6 | 5th mode of melodic minor | emitted − 7 | A Mix♭6 → **D minor** |
| Lyd♭7 | 4th mode of melodic minor | emitted − 5 | D Lyd♭7 → **A minor** |
| Lyd+ | 3rd mode of melodic minor | emitted − 3 | C Lyd+ → **A minor** |
| alt | 7th mode of melodic minor | emitted + 1 | D♯alt → **E minor** |

Implemented **once**, in the shared substrate `compare_rn._our_key_tonic`
(`_KB_PARENT_COLLECTION_MODES` + `_parent_collection_reduction`), which every graded surface reads
(a8 / the robust unit, `c1_reliability` and the calibration fit through it, the key-disagreement
classifier, `measure_joint_probe`). The **second** key parser — `oracle_root_metric.parse_our_key` /
`parse_dcml_key`, the DT-6 divergence — is **folded onto it**: its divergent copy is deleted and the two
functions are thin adapters that only re-shape `(tonic_pc, is_major)` into that tool's
`(tonic_pc, 'major'|'minor')` convention. **One reduction, one home.**

Modes NOT in the table keep the prefix rule **verbatim**, so no cell outside the five can move — the
property is structural, not merely observed.

### 2.2 What moved — every figure landed on the probe's written prediction, to the digit

| preset | key-agree HOME | key-agree LOCAL | key-abstain (ticks) |
|---|---|---|---|
| Baroque | 71.2909 → **71.4182** (+0.1273) | 65.7238 → **65.9900** (+0.2662) | 7 680 → **0** |
| Jazz | 67.4887 → **67.8274** (+0.3387) | 62.4942 → **62.9805** (+0.4863) | 10 800 → **4 080** |
| Default | 70.5183 → **70.6514** (+0.1331) | 65.3852 → **65.7093** (+0.3241) | 33 120 → **2 400** |

The probe (`cc_mode_grading_adjudication_probe_report.md`) predicted **71.4182 / 65.9900 / 67.8274 /
62.9805 / 70.6514 / 65.7093** and the abstain drops **0 / 4 080 / 2 400**. Every number reproduced exactly.
**Zero surprise (#3): the fact/theory basis was complete before the build.**

### 2.3 The ROOT axis is byte-identical (the hard stop)

```
=== baroque ===  runs: reference=6506 candidate=6506  (+0 / -0)
  (a) HARD STOP class-(b) root-disagree dur: ref=2714000 cand=2714000 delta=+0  -> PASS
=== jazz ===     runs: reference=6689 candidate=6689  (+0 / -0)
  (a) HARD STOP class-(b) root-disagree dur: ref=2784160 cand=2784160 delta=+0  -> PASS
=== default ===  runs: reference=6522 candidate=6522  (+0 / -0)
  (a) HARD STOP class-(b) root-disagree dur: ref=2718080 cand=2718080 delta=+0  -> PASS
OVERALL: PASS
```

Root 66.04/64.98/65.93 and RN 46.33/44.10/46.23 unchanged; class-(a) Δ+0; WiR coverage 326/326/326.
**Structural corroboration:** of the reference's 12 artifact files, only `summary.json` and `manifest.json`
changed — the six run enumerations and three mappings are byte-identical, because they are root-derived.

**Why the root axis cannot move here, at the code:** `compare_rn.classify_pair` (the 5-bucket verdict) does
not call the key reduction at all — it infers its `key_disagree` bucket from the roman-numeral case. The key
reduction feeds only the `b_key_*` counters. The insulation is structural, and the measurement agrees.

### 2.4 Establishment (never at assertion — #15/#19)

1. **The implementation IS the ruled rule.** Re-running the adjudication probe: its `ruleB` column now reads
   **Δ +0.0000** against the new baseline on all six columns.
2. **Nothing outside the five modes moved.** The probe's check (b) —
   `excl-population ruleA==ruleB==baseline: OK` — passes on all three presets.
3. **Two independent instruments agree cell-for-cell.** a8's counters reproduce the probe's own
   union-of-boundaries harness exactly (Baroque agree 5 923 200 / disagree 2 370 480 / fail 0; Jazz
   5 623 920 / 2 663 520 / 4 080; Default 5 859 600 / 2 431 680 / 2 400).
4. **Post-landing, the probe's check (a) — "baseline reproduces the committed columns" — is
   `ESTABLISHMENT PASS` on all three presets** against the re-baselined reference. The loop is closed.
5. **The oracle-root tool's ROOT sets are SET-IDENTICAL** before/after (charged 3878/4084/3910, charged_set
   3858/4066/3890, floor_set 4285/4276/4285). Only its KEY tiers shuffle — 5 / 9 / 11 identities
   (Baroque/Jazz/Default), **all of them out of** KEY-HARD / KEY-TONICIZATION and into
   OVER-GRAB / CHORD-ID / AMBIGUOUS: the same direction as the key-agreement gain, i.e. spans that used to
   be scored as key errors are no longer key errors under the ruled reduction.

### 2.5 Desk-check of the reduction against the annotators (the probe's cases, re-verified in code)

`C#PhrygDom → F♯ minor` · `A Mix♭6 → D minor` · `D Lyd♭7 → A minor` · `C Lyd+ → A minor` ·
`D♯alt → E minor` · `E PhrygDom → A minor` — and `Dor♭2` still abstains (see §5, OI-150), exactly as the
probe's Rule B did. Unchanged modes (`Cmaj`, `Amin`, `DDor`, `Gharm`, `B♭maj`) reduce as before.

---

## 3. Correction B — the routing + the calibration refit (OI-144), landed `b3511fd28a`

### 3.1 What was built

Discovery D3 found that three "secondary" When-in-Rome consumers are in fact **graded surfaces** still
reading the RAW `parse_rntxt_file`, so the 12 transposed editions were graded against the wrong pitch level.
Routed onto the ONE corrected substrate `dcml_parser.load_wir_regions`:

- `c1_reliability._load_wir` — and through it `calibration_fit`, which fits the committed maps;
- `oracle_root_metric.load_dir` — the charged/floor root figures.

All four `tools/calibration_maps/*.json` were then **refit on the corrected substrate and re-committed**.

### 3.2 The map deltas, attributed per correction

Fitting was run at both stages so each correction's contribution is separable (A alone, then A+B):

| map | A moves it? | B moves it? | max pointwise change in the fitted probability |
|---|---|---|---|
| L3 key margin (Baroque) | **yes** | yes | A 0.0079 · B 0.0925 |
| L3 key margin (Default) | **yes** | yes | A 0.0094 · B 0.0889 |
| L4 chord composite (Baroque) | **no** (byte-identical) | yes | A 0.0000 · B 0.0410 |
| L4 chord composite (Default) | **no** (byte-identical) | yes | A 0.0000 · B 0.0410 |

The shape is exactly right and self-explaining: **A changes key correctness, so it moves only the key-margin
maps; the chord-composite maps, whose target is root correctness, are untouched by it.** B changes both.

**Held-out correctness rises on every map** (they are now fit against correct labels):
L3 0.67916 → 0.68503 (Baroque) and 0.67315 → 0.67902 (Default); L4 0.47309 → 0.48002 and 0.47246 → 0.47940.

**Reported, not hidden:** the held-out calibration error (the honesty number) rises slightly with it —
L3 0.0262 → 0.0373 (Baroque), 0.0333 → 0.0471 (Default); L4 0.0167 → 0.0183, 0.0159 → 0.0191. The isotonic fit
gains a few knots (34 → 44 on L3 Baroque) against the corrected labels, generalizing marginally less tightly.
No gate is defined on this figure; it is recorded so the next consumer reads a true number.
The L3 fit cell count also rises (14 845 → 14 848 Baroque; 14 804 → 14 841 Default) — the key-abstain cells
Correction A rescued now enter the fit.

### 3.3 a8 is BYTE-IDENTICAL under Correction B — so no governing figure is attributable to it

a8 already read the corrected substrate, so the routing must leave it untouched. **Falsifiable prediction,
verified:** `summary.json` and all six run-enumeration files are byte-identical between the A-only and the
A+B measurement. Every governing figure in this event is therefore attributable to **Correction A alone**.

### 3.4 The oracle-root movement is confined to exactly the 12 transposed stems

Set-verified against `tools/robust_stop/corpus_transposition_offsets.json`: the stems whose charged set moved
are **precisely** the 12 transposed editions (`bwv115.6, bwv126.6, bwv145.5, bwv148.6, bwv177.5, bwv180.7,
bwv184.5, bwv244.62, bwv267, bwv30.6, bwv39.7, bwv73.5`) — identical on all three presets, nothing else.

**The direction, read at the code, not guessed:** the tool's FLOOR is *events where music21 and DCML disagree
with each other* (the oracle is unusable there); a CHARGE requires the two authorities to concur. Correcting
the 12 editions makes them concur, so **625 events per preset LEAVE the floor** (4285 → 3665) and become
scoreable: ~445 prove correct, and **~180 surface as genuine root errors that were previously invisible**
(charged 3878 → 4055 Baroque, 4084 → 4275 Jazz, 3910 → 4090 Default). **This is a coverage gain, not a
regression** — the metric now sees events it previously had to discard. It is consistent with the OI-142
adoption, where the same correction *decreased* class-(b) root-disagree duration on a8 (which grades against
DCML alone and needs no oracle consensus).

---

## 4. Suites, gates, and the post-landing state

| check | result |
|---|---|
| composing_tests | **1101 / 1101 passed** (2 disabled) |
| notation_tests | **53 passed + 4 skipped** (57 ran) |
| pipeline_snapshot_tests | **11 passed + 1 skipped** (a report generator; 3 disabled) — **no golden refresh owed** |
| robust-stop hard stop | **PASS** all presets (class-(b) Δ+0, runs +0/−0, coverage 326/326/326) |
| corpus regen (352 × 3) | **0 `.ours.json` differ** on every preset |
| establishment battery (post-landing) | **PASS** — a8_diff (+0/−0), **calib 4/4 byte-identical**, validate 3/3 |
| adjudication probe (post-landing) | **ESTABLISHMENT PASS** all presets |

The post-landing `calib 4/4 byte-identical` is the proof that the maps committed in `b3511fd28a` are
**reproducible from the code on disk** — not a one-off artifact.

**Reference re-baselined** (`tools/robust_stop/`): `summary.json` + `manifest.json` only. The manifest was
re-stamped **programmatically from the a8 summary** (`restamp_manifest.py`, session scratch) — **no figure in
it was typed by hand** (#17f). The outgoing key column is preserved inside it
(`reproduce_status.superseded_oi142_oi143`) and byte-for-byte in the O-12 snapshot (#12).

---

## 5. What was surfaced and NOT absorbed (new register rows)

- **OI-150 — the remaining key-parse abstain.** The shared reduction's fallback mode regex is `[A-Za-z]+`,
  so it still abstains on any mode name containing an accidental or a digit. Exactly one such mode survives
  in the corpus: **Dorian ♭2** (4 080 ticks Jazz / 2 400 Default / 0 Baroque). Deliberately left: fixing it
  moves the key figures **outside the five modes the user ruled on**, so it deserves its own measured
  ratification. **The user corrected CC's proposed reduction target, and the row records the correction:**
  Dorian ♭2 is the **2nd mode of melodic minor** — D Dorian ♭2 is the notes of **C melodic minor** — so it
  grades as **C minor (parent tonic = emitted − 2), not D minor**. Same-tonic-minor is precisely the
  unprincipled reduction the OI-132 ruling retired. The row also declares (without deciding) the boundary
  question: the plain church modes `Dor`/`Phryg` keep same-tonic-minor under a separate standing declared
  choice at `_KB_MAJOR_MODE_PREFIXES`; whether that should be revisited under the same principle is for
  Cowork/the user.
- **OI-151 — a destructive default output path (DT-24, sibling of OI-130).**
  `mode_grading_adjudication_probe.py` writes to `tools/reports/mode_grading_adjudication_probe.json` by
  default with **no `--out` flag**, and that file is a **committed artifact** — the evidence the user's OI-132
  ruling rests on. Discovered by doing it: a self-check re-run overwrote it (the new content is legitimate but
  is *not* the pre-ruling evidence, and `cc_mode_grading_adjudication_probe_report.md` cites the old figures).
  The committed file was restored with `git checkout`; the self-check output kept in scratch. The probe
  post-dates OI-130, so this is a fresh instance of a closed defect type, not a leftover.

**Also noted, not a defect:** six untracked `*_root_fail_cells.txt` files sit in `tools/robust_stop/` from the
2026-07-12 re-baseline. a8 emits them; the committed reference has only ever tracked the `*_runs.txt` set. The
established file set was preserved and they were left untracked.

---

## 6. Self-check (over every diff on disk, before reporting done)

- **Read the diff, not the memory of writing it.** Doing so caught two things: a docstring line I wrote that
  described Correction B *before it existed* (fixed on the spot — doc-sync #10), and the probe-evidence
  overwrite now filed as OI-151.
- **No `src/` change; no constant tuned; no gate threshold touched; no golden refreshed; no score or
  ground-truth file edited.** The corpus is byte-identical (proven, not asserted).
- **#6 (one path per concern):** the event *removes* a duplicated derivation (the second key parser) and a
  second ground-truth view; it adds none. `compare_rn` and `oracle_root_metric` do not import each other
  circularly (verified in a fresh interpreter, both import orders).
- **#12 (no information loss):** the outgoing reference and the outgoing maps are snapshotted byte-for-byte
  (O-12, `23e21da8ea`); the superseded key column is preserved inside the manifest; the pre-ruling probe
  evidence was restored.
- **#14 (one revertible, provenance-stamped commit per behavior change):** two commits, each independently
  revertible — `oracle_root_metric.py` carries hunks from both corrections, and the A-only version of that
  file was staged for commit A so that reverting either commit leaves a coherent, runnable tree (verified:
  commit A's staged file still calls the raw loader).
- **#17f (no hand-transcribed figures):** every figure in the manifest is derived programmatically from the
  generated a8 summary; every figure in this report comes from a generated artifact or a tool's own printed
  output.
- **No self-invented labels or jargon:** "Correction A / Correction B", "parent collection", "conflict mode"
  are the dispatch's and the probe's own terms; mode names and parent derivations are standard music theory.
  American English throughout.
- **Git:** only my own files staged by name; `cowork_joint_key_chord_design.md` (the known carry) left
  unstaged throughout; `cc_*.md` gitignored and force-added. `git remote -v` confirmed `upstream` push is
  **disabled**; pushed to `origin` only.
