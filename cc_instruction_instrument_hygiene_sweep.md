# CC instruction — the measurement-instrument hygiene sweep (OI-145 wave-1 close)

**Dispatch author:** Cowork, 2026-07-13, at the user's direction to proactively close the measurement-chain
hygiene rows still gated passively on "the next touch" rather than leave them to a trigger that may never
fire. **Type:** a hygiene / dedup / establishment pass on the `tools/` measurement instruments — **NOT
`src/composing` inference coding, and NOT a re-baseline.** Every fix here is duplication removal, output
discipline, or provenance establishment. **Byte-identity on every governing metric is the whole-dispatch
success condition;** anything that would move a graded figure is a STOP, not a landing.

This closes OI-145 wave 1 (the measurement chain) before wave 2 (the `src/` substrate). It exists because
the OI-155 work showed the OI-132 consolidation had under-propagated across duplicate copies — so the
remaining duplicates get folded now, not discovered later.

Read first (the convention): `CLAUDE.md` in full, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`, `STATUS.md`.
Re-locate every line reference below by symbol — the audit refs may have drifted.

---

## 1. Governing constraints (all tasks)

Same standing set as the harness-group and OI-155 dispatches: the Premise Gate (#17) — write the
quantitative prediction BEFORE measuring; byte-identity is the success condition (§2); no self-invented
labels; the self-check on every diff (read the diff, not the memory of it); the VS Code bash rules
(`; echo "exit:$?"`, no large single-call output); fork-only push (`origin`, never `upstream`); the
discovery/STOP protocol — any graded figure that moves, any newly-found issue → its own register row in
the same commit + STOP-and-report.

**Layer discipline (the user's standing reminder):** every amendment lands in its proper layer. The dedup
fixes route duplicates through the ONE already-existing owner (the shared reduction / the shared helper) —
they do not create a new parallel path. No `src/composing` file is touched.

---

## 2. The proof — the establishment battery, and what "byte-identical" means per item

Run `tools/audit/hardening_battery.py` (`979e07db46`) before any change and after each: `a8_diff` +0/−0
all presets + class-(b) Δ+0, `calib` 4/4 sha256-identical, `validate` 3/3, `fixture` root
66.04/64.98/65.93, and the Python metric suites green. The key columns stay home 71.42/67.83/70.65 / local
65.99/62.98/65.71.

For instruments that are **not** in the battery (the two probes, Tasks A and B), the battery proves the
GOVERNING surfaces are untouched; the item's own proof is (i) the fix is correct, and (ii) any change to a
committed probe-evidence artifact is expected, explained, and made non-destructive (Task B is exactly
about that). A probe re-run that would silently overwrite committed evidence is itself a defect to fix, not
a step to take.

---

## 3. Task 0 — register commit

Commit any waiting Cowork register/handoff edits staged for you (verify `git status --porcelain` first;
STOP if the tree differs from what this dispatch describes). Leave `cowork_joint_key_chord_design.md`
unstaged (the standing carry). Then proceed; each fix below carries its own row flip in its own commit
(#14).

---

## 4. Tier 1 — dedup + output hygiene (byte-identical on the governing metric)

### Task A — OI-157: fold the third mode-classification copy into the one shared reduction
`tools/measure_joint_probe.py`'s `_MAJOR_MODE_IDX` enum-index table (audit ref :86) is a THIRD copy of the
mode classification that went stale at OI-132: it still encodes the superseded same-tonic prefix rule, and
an `(enum-index → is_major)` table cannot express the parent-collection tonic move at all. The probe already
carries the region key STRING (`ourKeyStr`) — so derive the key identity from **`compare_rn._our_key_tonic`
/ `_our_key_ident`** (the ONE reduction, OI-155) instead of the local index table, or **delete the table**
if the probe is retired (the joint step is shelved — OI-43/OI-44; confirm its status before choosing).
- The probe is read-only and not in the battery, so no governing figure moves. Its own faithfulness
  self-check (:307–314) should pass against the shared reduction after the fold.
- If a re-run would rewrite a committed probe artifact, apply Task B's discipline (scratch default) so the
  committed evidence is not silently overwritten.
- Prove the battery byte-identical (expected trivially — the probe feeds nothing graded). Flip OI-157.

### Task B — OI-151: stop the adjudication probe overwriting its own committed evidence
`tools/mode_grading_adjudication_probe.py` writes `tools/reports/mode_grading_adjudication_probe.json` **by
default with no `--out` flag** — and that path is committed force-added evidence the OI-132 ruling rests on.
Default `--out` to a scratch path (the `calibration_fit` / `music21_batch` / `stage5_fit_driver` pattern);
writing the committed evidence path must be **explicit**. No measurement changes — a pure output-path fix.
Verify the committed artifact is untouched by a default run. Flip OI-151.

### Task C (opportunistic, only if clean and byte-identical) — the remaining `tools/` dedup residuals
Fold these **only** where the change is mechanically byte-identical; anything subtler is left to its row:
- **OI-132(b)** — the two cross-language value-copies `INVERSION_SUSPICION_MARGIN`=0.70 (copies the C++
  `inversionSuspicionMargin` pref) and `TICKS_PER_QUARTER`=480 (copies MuseScore `Constants::DIVISION`).
  They cannot be Python-single-sourced, but they CAN be mechanically guarded: add a cross-language **pin
  test** that parses the C++ source and asserts the Python copy matches — the same producer-parsing pattern
  the OI-155 completeness test and the OI-135 sync test use. Turns a silent value-copy into a red-on-drift
  guard. Flip the OI-132(b) residual note.
- **OI-127** sub-items, each at its own file (this sweep is that touch): (b) the `_load_region` `root_pc`
  `-1` sentinel that lets two rootless regions compare equal in `_roots_match` (a narrow false-agreement
  edge — fix only with a byte-identical proof that no real pair is affected, else leave it); (a) the
  `_QUALITY_NORMALISE` pass-through completeness (a producer-vocabulary pin, like OI-155's); (e) the
  `gen_inventory` `import platform` crosslayer false-positive + the disposition-generator proliferation
  (OI-95(a)) — tooling-only. Take the clean ones; leave any that risk a figure move to their row.

---

## 5. Tier 2 — tolerance establishment (#19), establish-and-report (NOT a silent value change)

OI-125 and OI-133(c) are the hand-set grading tolerances. OI-125's constants are already centralized into
one named block in `compare_analyses.py` with `[hand-set; re-derivation flagged]` notes
(`ALIGN_OVERLAP_FRACTION`=0.5, `ALIGN_BEAT_DISTANCE_TOL`=0.5, `EXTRAPOLATION_BEATS_PER_MEASURE`=4);
OI-133(c) is the sibling set of ~13 scattered grading tolerances (beat window ±0.26, noteCount≥3,
margin≥2.0, near_logistic 0.05, min-cell 50/20, FloatingKey ±4). The remaining work is #19: establish each
value's provenance — derive or justify it from the music-theory/measurement first principles it encodes,
not merely re-state that it is hand-set.

**The discipline that keeps this safe:**
- Establish each tolerance's derivation and **document it at the constant** (provenance, what it measures,
  why the value is right). If the current value is justified, this is **byte-identical** — no figure moves,
  and the row closes as established.
- **If establishing a value shows the current setting is WRONG, that is a STOP, not a fix.** A tolerance
  change moves graded figures → a re-baseline event requiring the O-12 ritual and the user's ratification.
  Do not land it in this hygiene sweep — surface it with the evidence and let the user decide.
- If a value's true establishment genuinely needs work beyond a hygiene pass (an oracle study, a
  corpus-expansion dependency), **document the derivation plan and leave the row open with a concrete
  gate** — do not force a number. State plainly which tolerances were established byte-identically and
  which remain owed, so the register reflects reality.

Flip OI-125 / OI-133(c) to reflect exactly what was established vs what remains, with provenance.

---

## 6. Explicitly OUT of scope (do not touch; surface if you find a reason to)

- **OI-131** (fit-manifest single-source / `PARAMS` triple-representation) — assigned to the Stage-5/EG-5
  manifest work, not this sweep.
- **OI-152** (the Dor♭2 key-parse abstain), **OI-156** (the bridge's 4th `0.25` literal), the **OI-34**
  corpus-line-ending amendment — all user-deferred to their proper later touches.
- Any **`src/composing` or `src/notation`** change, and anything that **moves a graded figure** — those
  are re-baselines or inference work, not hygiene.

---

## 7. Premise Gate — the predictions to write before measuring (#17b)

Whole-dispatch: the battery reproduces byte-identical (a8_diff +0/−0, calib 4/4, validate 3/3, key columns
unmoved); the two probes feed nothing graded, so folding/redirecting them moves no governing figure; the
OI-132(b) pin test and any OI-127 fold are byte-identical by construction; the tolerance establishment is
byte-identical unless it surfaces a wrong value (→ STOP). Per-task, write the specific prediction and its
fire condition. A landing on-prediction is the expectation; any graded-figure movement is the STOP.

---

## 8. Deliverables and commit plan

- **One fix commit per row** (OI-157, OI-151, OI-132(b), each taken OI-127 sub-item, OI-125, OI-133(c)),
  each carrying its own `OPEN_ITEMS.md` flip with provenance.
- **A `docs(cc)` fold**: a report `cc_instrument_hygiene_sweep_report.md` (the battery before/after showing
  zero governing movement; per-row what was folded/established; for the tolerances, exactly what was
  established byte-identically vs left owed with a gate; any discovery). Update the OI rows, `STATUS.md`,
  and `cowork_handoff.md`. Force-add this instruction file.
- **If any tolerance establishment surfaces a needed value change,** stop at a clean boundary with the
  battery green, leave that row open with the evidence and a proposed re-baseline, and report — the user
  rules on it.

**On completion:** OI-145 wave 1 (the measurement chain) is closed — the harness group, OI-155, and the
instrument-hygiene rows all discharged — and the next move is wave 2 (the `src/` substrate hygiene: OI-86,
OI-13, OI-87, the file-table reasons) toward the key-layer readiness gate lifting. Report the battery
deltas (expected: all zero), the per-row disposition, and any tolerance found owed or wrong.
