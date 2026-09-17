# CC instruction — OI-155: restore abstain-on-unknown in the shared key reduction + file two deferred rows

**Dispatch author:** Cowork, 2026-07-13, after the user's ruling on the harness-group report. **Type:** a
grading-CONVENTION fix on the measurement chain (the OI-33 abstain family / OI-145 wave 1) — NOT
`src/composing` inference coding. One change in the ONE shared key reduction (proper layer, no
duplication). Plus two register rows filed for later, per the user's defer ruling.

**The user's ruling (recorded):** OI-155 resolves as **restore abstain-on-truly-unknown** (not "ratify
default-minor"). An emitted mode suffix that is not a known-major class, not a known-minor class, and not
one of the five parent-collection exotics must **abstain on the mode** (a keyfail on the mode axis, per
OI-33) instead of being silently graded minor. The two offered dedup items are **filed-and-deferred**, not
taken here.

Read first (the convention): `CLAUDE.md` in full, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`, `STATUS.md`.
Re-locate every line reference below by symbol — they are as-of this dispatch and may drift.

---

## 1. Governing constraints

Same as the harness-group dispatch: byte-identity is the success condition (this is a convention fix that
must not move a real grade — see §4); the Premise Gate (#17) — write the prediction before measuring; no
self-invented labels; the self-check on every diff; the VS Code bash rules; fork-only push (`origin`,
never `upstream`); the discovery/STOP protocol (any real grade that moves, any new issue → its own
register row in the same commit + STOP-and-report).

**This is a grading-instrument change, not inference.** It lives entirely in `tools/` (the shared
reduction and its consumers). Do not touch `src/composing` analysis behavior.

---

## 2. Ground the allowlist in the PRODUCER's vocabulary — do not guess it

The mode suffixes the chain actually emits are OWNED by the producer, `src/composing/analysis/key/
keymodeformatting.cpp` (with the mode set declared alongside `keymodeanalyzer.{h,cpp}`). The grader's
major/minor/exotic partition must be **derived from and checked against that emitted vocabulary**, not
hand-invented (#6 — the grader reads the producer's set, it does not re-decide it; the fact-publication
corollary).

**Task:** enumerate, at `keymodeformatting.cpp`, the complete set of mode-suffix spellings the engine can
emit. Partition them:
- **known-major** — the current major-prefix set (maj / ion / lyd / mix) and any other emitted mode whose
  parent is major;
- **known-minor** — the church/minor-family modes actually emitted (dorian, phrygian, aeolian, locrian,
  harmonic minor, melodic minor, and whatever else the producer lists as minor-parent);
- **the five parent-collection exotics** — PhrygDom / Mixb6 / Lydb7 / Lyd+ / alt (unchanged, OI-132);
- **everything else → abstain.**

Record the enumeration in the report so the allowlist's provenance is the producer, not this instruction.
If the producer emits a mode you cannot confidently place as major or minor, that is a STOP — surface it,
do not default it.

---

## 3. The fix — one change in the shared reduction

In `tools/compare_rn.py`, the single reduction `_our_key_tonic` (and its helper `_mode_is_major`):

- Replace the two-valued `_mode_is_major(mode) -> bool` with a three-valued classification
  `-> Optional[bool]`: **True** (major) for a known-major suffix, **False** (minor) for a known-minor
  suffix, **None** (abstain) for an unrecognized suffix. Ground the two known sets in §2.
- `_our_key_tonic`: after the parent-collection reduction (unchanged) and a successful
  `_KB_OURS_KEY_RE` match, return `(tonic_pc, <three-valued class>)`. A recognized tonic with an
  **unknown mode** therefore returns `(pc, None)` — tonic present, mode abstained — NOT `(pc, False)`.
  Full `(None, None)` still means a genuinely unparseable string (empty / regex miss, e.g. the OI-152
  accidental/digit case).
- `oracle_root_metric.parse_our_key` is already a thin adapter over this reduction; confirm it maps the
  three states to `(pc, "major") / (pc, "minor") / (pc, None)` and `(None, None)` — so
  `parse_our_key("Cweird") == (0, None)` again by the CODE, not by editing the test.

**★ The load-bearing step — audit every consumer of the second element.** Adding the `(pc, None)` state
(tonic known, mode abstained) is a new third case that consumers currently assuming a bool may
mishandle. Enumerate every reader of `_our_key_tonic(...)[1]` and of `parse_our_key`'s mode field —
`key_disagree_subtag`, the a8 / robust-unit key-agreement, `c1_reliability` and the calibration fit
through it, the key-disagreement classifier, the oracle tiers — and confirm each treats mode=None as a
**mode-abstain (keyfail on the mode axis)**, consistent with OI-33, rather than crashing or silently
folding it into major/minor. This audit is the real work; the reduction edit is small.

---

## 4. The two red tests — fix the CODE, not the expectations (except the stale one)

- **`test_oracle_root_metric.py::test_parse_our_key`** (the grading-semantics one): it goes green because
  §3 restores `parse_our_key("Cweird") == (0, None)`. **Do not edit its expectation** — that was CC's
  correct refusal; the test pins the OI-33 convention and the code is what was wrong.
- **`test_metric_primitives_l0l1.py::test_our_key_tonic_mode_qualified_normalization` line 361**
  (`EPhrygDom`): this one is genuinely stale — update the expectation to the correct **parent-collection**
  answer `(9, False)` = A minor (E PhrygDom is the 5th mode of A harmonic minor; offset −7). This is the
  OI-132 ruling, orthogonal to the abstain question.
- Add/confirm a test that a genuinely-unknown mode abstains on the mode axis (the positive assertion of
  the restored convention), if one is not already implied.

Both expectation changes land in one commit with the code fix.

---

## 5. Premise Gate — the prediction to write before measuring (#17b)

**Predicted: zero real-grade movement.** Every mode the producer actually emits is classifiable as
known-major, known-minor, or one of the five exotics, so no real corpus cell newly abstains; the abstain
path fires only on inputs that do not occur in the corpus (the test's "Cweird"). Therefore the full
establishment battery reproduces byte-identical: `a8_diff` +0/−0 all presets, class-(b) Δ+0, `calib` 4/4,
`validate` 3/3, key columns unmoved (home 71.42/67.83/70.65, local 65.99/62.98/65.71), Python metric
suites green, both named tests green.

**If ANY real cell newly abstains (a8 key-agree moves, or a stem drops from coverage): STOP.** That means
a real emitted mode fell outside the allowlist — a discovery (an emitted mode the producer lists that the
grader could not place), needing its own register row and a re-baseline decision (the O-12 ritual), NOT a
silent change. Report it; do not proceed.

---

## 6. File the two deferred rows (do NOT fix either — file only)

Per the user's ruling, both offered dedup items are tracked for their proper touch and left untouched now:

- **The bridge's 4th hard-coded `0.25` onset literal** (in `src/notation`, the user-facing bridge — a
  production path outside this dispatch's edit scope). File it as a **residual on OI-135** (or a new
  register row if OI-135 is closed), **assigned to the next `src/notation` config-unification touch**:
  the bridge should read the composing config default (now single-sourced via `kDefaultOnsetBoundaryThreshold`
  / the configuration) instead of a literal `0.25`. Proper-layer dedup, done at that touch, not now.
- **The corpus line-ending platform-dependence** (the committed `.ours.json` corpus is CRLF only because
  regeneration runs on Windows with `QIODevice::Text`; a Linux regen would move every fingerprint). Record
  this under **OI-34** (the corpus git-tracking decision), cross-referenced from **OI-137(a)** (which CC
  established-and-documented). It is the deferred "the committed corpus is platform-dependent" obligation
  for the O-12/OI-34 decision — not a code change here.

---

## 7. Deliverables and commit plan

- **One fix commit** carrying: the shared-reduction three-way classification + the consumer-audit
  adjustments (if any consumer needed a mode=None branch), both red-test fixes, and the OI-155 row flipped
  to resolved with provenance (the allowlist grounded in `keymodeformatting.cpp`; the consumer audit; the
  zero-movement proof).
- **The register rows for §6** land in that same commit (or the Task-0 register commit): the OI-135
  residual / new row for the bridge literal, and the OI-34 note for the line-endings. Each with provenance.
- **A `docs(cc)` fold**: a short report `cc_oi155_report.md` (the producer-vocabulary enumeration and the
  resulting allowlist, the consumer audit, the battery before/after showing zero movement, the two tests
  now green), plus the OI-155/OI-135/OI-34/OI-137 register updates and the `STATUS.md` + `cowork_handoff.md`
  updates. Force-add this instruction file.
- **If the zero-movement prediction fails,** stop at a clean boundary with the battery green, leave OI-155
  open with the discovered mode named, and report — do not re-baseline without the user.

On completion: OI-155 closes, the two red tests are green (one by the code fix, one by the parent-collection
expectation), and the harness group's follow-up is fully discharged; the two deferred rows carry the
remaining dedup obligations to their proper touches.
