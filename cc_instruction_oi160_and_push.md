# CC instruction — OI-160 (collapse the joint-probe artifacts to one) + push wave 1 to the fork

**Dispatch author:** Cowork, 2026-07-13, on the user's rulings. **Type:** evidence-record hygiene on
`tools/reports/` + a fork push. **NOT `src/` work, NOT a governing re-baseline.** The joint-probe evidence
is non-governing; the establishment battery stays byte-identical. On completion, OI-145 wave 1 is closed
AND pushed.

Read first (the convention): `CLAUDE.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`, `STATUS.md`. Re-locate
every reference by symbol.

---

## 1. Governing constraints

The standing set: Premise Gate #17 (predictions before measuring); byte-identity of the governing surfaces
as the success condition; no self-invented labels; self-check on every diff; the VS Code bash rules;
**fork-only push (origin only, NEVER upstream — verify with `git remote -v` that upstream push is
disabled)**; discovery/STOP protocol. No `src/composing` or `src/notation` file is touched.

---

## 2. Task 0 — register commit

Commit any waiting Cowork register/handoff edits (verify `git status --porcelain`; STOP if the tree differs
from what this dispatch describes). Leave `cowork_joint_key_chord_design.md` unstaged.

---

## 3. Task 1 — OI-160: collapse the two joint-probe artifacts to one; re-confirm both rulings

**The ruling (option A):** `tools/reports/joint_probe_measure.json` (the old arc-12 chord-axis run) is a
verified strict subset of the fuller OI-43 run from the same instrument (`measure_joint_probe.py`) — the
OI-43 run adds the key-axis fields (menu-containment, chord-flip-under-GT, keyConf) on top of all the
chord-axis fields (fire-rate, benefit corr/harm/neutral, beam-width, pedal). Do not maintain two; collapse
to one canonical, current artifact.

**Do:**
- **Identify both committed artifacts** of `measure_joint_probe.py` (the arc-12 `joint_probe_measure.json`
  and the separately-named OI-43 evidence file the OI-159 refresh touched). Confirm at the files that the
  older is a strict subset of the newer (the newer contains every field the older has, plus the key-axis
  block). If that subset relation does NOT hold at the files, STOP and report — the collapse premise is
  wrong.
- **Snapshot the outgoing** committed artifact(s) first (O-12), as with every re-baseline of committed
  evidence.
- **Refresh ONE canonical artifact** by re-running `measure_joint_probe.py` (read-only; it writes only its
  report) against the current corpus + the OI-142-corrected ground truth, writing the full run (both axes)
  to the instrument's natural committed target. **Retire the redundant file** so exactly one committed
  artifact remains for this instrument (#6 — one artifact per concern).
- **Re-point every citation**: update each decision record and `cc_*` report that cites either old file to
  cite the one canonical artifact (the arc-12 chord-axis no-go record AND the OI-43/OI-44 shelve record).
- **Record both re-confirmations** with the corrected numbers: the arc-12 chord-axis **no-go stands** (net
  corr−harm +9/+6/+10, a fraction of a percent of ~6,200 scored regions — far from any go threshold; the
  fire-rate is byte-identical, so our analyzer's behavior did not change, only the GT sort corrected); the
  OI-43/OI-44 **shelve stands** (already re-confirmed at OI-159 — menu-containment 75.6/68.7/72.5 %, still
  under the 80 % bar).

**Proof:** the establishment battery stays byte-identical (this artifact feeds no governing metric — a8
+0/−0, calib 4/4, validate 3/3). If any governing figure moves, STOP. Flip OI-160 to resolved with
provenance (the subset confirmation, the O-12 snapshot, the retired file, the two re-confirmations).

---

## 4. Task 2 — push wave 1 to the fork

After Task 1 lands and both suites are green: **push all accumulated commits to `origin`** (the user's fork,
`slimvince/MuseScore`). First `git remote -v` and confirm `upstream` (`musescore/MuseScore`) push is
disabled — it must remain so. Push `origin` only. The do-not-merge-upstream constraint on the MusicXML
declared-mode patch (`cfc7eb5e39`) still holds: an `origin` push is fine, an `upstream` push/PR is a HARD
STOP. Report the push result (branch, commit range pushed, `origin` confirmed, `upstream` untouched).

---

## 5. Premise Gate — predictions before measuring (#17b)

Task 1: the refreshed canonical artifact's fire-rate fields are byte-identical to the retired subset's (our
analyzer's property); only the GT-graded corr/harm split re-sorts to +9/+6/+10; the establishment battery
is byte-identical (no governing surface touched). Task 2: the push updates `origin` only; `upstream`
unchanged. Write these before running; any deviation is the STOP.

---

## 6. Deliverables and commit plan

- **Task-0 register commit**, then the **OI-160 commit** (the O-12 snapshot + the collapsed/refreshed
  artifact + the retired file + the re-pointed citations + the OI-160 row flip with provenance).
- **A `docs(cc)` fold**: `cc_oi160_report.md` (the subset confirmation, the two re-confirmations with
  corrected numbers, the retired duplicate, the battery byte-identity) + the OI-160 row + `STATUS.md` +
  `cowork_handoff.md` updates stating **OI-145 wave 1 is closed and pushed**, wave 2 next. Force-add this
  instruction file.
- **The push happens after the fold** (so the fork receives a clean, self-consistent state).
- **If the subset premise fails or any governing figure moves,** stop at a clean boundary, leave OI-160
  open with the finding, and report before pushing.

**On completion:** OI-145 wave 1 (the measurement chain) is fully hardened, closed, and on the fork; the
next move is wave 2 — the `src/` substrate (OI-86, OI-13, OI-87, the file-table reasons) toward lifting the
key-layer readiness gate. Report the collapse result, both re-confirmations, and the push (origin only,
upstream untouched).
