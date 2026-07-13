# CC instruction — OI-158 + OI-125 + OI-159 (the wave-1 finalizers, user-ruled 2026-07-13)

**Dispatch author:** Cowork, 2026-07-13, on the user's rulings of the hygiene-sweep findings. **Type:** a
measurement-instrument fix pass on `tools/` — **NOT `src/composing` inference, NOT a re-baseline of any
governing metric.** All three items are byte-identical on the governing surfaces; anything that would move
a graded figure is a STOP. On completion, OI-145 wave 1 (the measurement chain) is truly closed and wave 2
(the `src/` substrate) opens.

Read first (the convention): `CLAUDE.md` in full, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`, `STATUS.md`.
Re-locate every line reference by symbol.

---

## 1. Governing constraints

The standing set (Premise Gate #17 — predictions before measuring; byte-identity as the success condition;
no self-invented labels; self-check on every diff; the VS Code bash rules; fork-only push; the
discovery/STOP protocol — any graded figure that moves or any new issue → its own register row in the same
commit + STOP-and-report). Layer discipline: every fix lands in its proper layer (these are all `tools/`
measurement instruments); **no `src/composing` or `src/notation` file is touched.**

**One discipline to hold this time** (the hygiene sweep flagged it): a fix and the register row that records
its discovery travel in the **same commit** (#14 revertibility + the discovery protocol). Group by row, not
by file — if two rows share a file, they can still be separate commits touching that file.

---

## 2. Task 0 — register commit

Commit any waiting Cowork register/handoff edits (verify `git status --porcelain`; STOP if the tree differs
from what this dispatch describes). Leave `cowork_joint_key_chord_design.md` unstaged. Each fix below then
lands in its own commit with its own row flip.

---

## 3. Task 1 — OI-158: remove the dead FloatingKey block; keep the evidence question open

**The ruling (option 3):** the block is dead **by bug** — `music21.analysis.floatingKey` exports no
`FloatingKey` in v9.9.1 (the class is `KeyAnalyzer`), so the constructor always raised and `local_key` has
always fallen back to the global key. Remove the dead machinery; do **not** activate `KeyAnalyzer` (that
would put an unvalidated heuristic under load, #19, and re-base the corroborator, #16); do **not** foreclose
the question (that would discard a possible evidence source, #12).

**Do:**
- In `tools/music21_batch.py`, remove the unreachable FloatingKey path: the `_HAS_FLOATING_KEY`
  import/flag, the `fk_analyzer` construction block (the `FloatingKey()` call + the `numFlats`/`numSharps`
  ±4 config), and the `if fk_analyzer is not None:` local-key branch — `local_key` becomes plainly
  `global_key`. Keep the corrected docstring/comments (state that music21 corroborates at the **global**
  key, and cite OI-158 for the history).
- **Prove byte-identical at the artifact:** regenerate the `.music21.json` corroborator to a scratch dir
  and sha256-compare against the committed set — it MUST be identical (the removed code never affected
  output; `key`/`romanNumeral` were already global-key on every region). This is the analog of the harness
  `.ours.json` regen proof. If ANY file differs, STOP — the block was not as inert as believed.
- Run the establishment battery (expected fully byte-identical; music21's key feeds only diagnostics, not
  the governing hard stop).

**File the evidence question (do NOT decide it here):** add to `cowork_evidence_inventory.md` (OI-146) and
carry on OI-158 the open question — *"should the key layer consume a music21 `KeyAnalyzer` local-key
second opinion as an (unvalidated, non-ground-truth) cross-check?"* — gated on the key-layer design
conversation. OI-158's dead-code half CLOSES with this fix; its evidence half stays OPEN with that gate.
The publish-broadly rule applies: if it is ever added, it enters as an explicitly-unvalidated field, never
under load until established (#19).

---

## 4. Task 2 — OI-125: apply the derived-measure-length fix (byte-identical)

**The ruling: apply now.** In `tools/compare_analyses.py`, `_dcml_tick_for` extrapolates a ground-truth
onset beyond the anchor measures using `EXTRAPOLATION_BEATS_PER_MEASURE (=4) * tpb` (audit refs
:592/:596). Replace the hard-coded 4/4 with each stem's **derived measure length** (already computed three
lines above — use that value, do not re-derive it). This removes the silent 4/4 assumption from a shared
graded resolver.

**Prove byte-identical:** the resolver feeds the a8 governing path, so the establishment battery is the
proof — `a8_diff` +0/−0 all presets, class-(b) Δ+0, calib 4/4, validate 3/3, key columns unmoved. It fires
162× across 15 stems, all currently 4.0 beats, so the derived value equals `4 * tpb` on every current
firing → byte-identical by construction. If ANY figure moves, STOP (do not adjust anything to compensate) —
that would mean a current stem is not 4/4, a discovery to report.

Flip OI-125: the extrapolation half closes (the resolver is now meter-correct for the planned non-4/4
corpus). **The two genuinely-load-bearing #19 tolerance establishments remain owed and stay tracked** —
`calibration_fit`'s min-cell and near-logistic gates, each with the concrete experiment the sweep recorded;
they are NOT in this dispatch (they need those experiments, scheduled at the calibration/Stage-5 work).
Keep OI-125/OI-133(c) open on exactly that named remainder.

---

## 5. Task 3 — OI-159: refresh the stale OI-43 probe evidence (shelve re-confirmed)

The OI-142 correction (and, secondarily, the OI-157 fold) staled the committed OI-43 joint-probe evidence.
The shelve ruling is **unchanged and re-confirmed** — chord-flip-under-GT byte-identical at 7/8/6,
menu-containment risen to 68.7–75.6 % but still under its 80 % bar. This is an evidence/doc-sync fix (#10),
not a decision.

**Do:** snapshot the outgoing committed evidence first (O-12), then refresh the committed OI-43 probe
artifact to the current numbers, with provenance attributing the drift (OI-142 −196/−187/−191;
the OI-157 fold −11/−20/−8) and stating the shelve re-confirmation. Update any `cc_*` report that cites the
stale figures. No governing figure is involved; the battery stays byte-identical. Flip/annotate OI-159.

---

## 6. Premise Gate — predictions to write before measuring (#17b)

Whole-dispatch: every governing surface reproduces byte-identical (a8_diff +0/−0, calib 4/4, validate 3/3,
key columns unmoved). Task 1: the `.music21.json` regen is sha256-identical to the committed set (the dead
block never touched output). Task 2: the derived measure length equals `4 * tpb` on all 162 current firings
→ battery byte-identical. Task 3: evidence-artifact-only, no governing surface. Write each before running;
any deviation is the STOP.

---

## 7. Deliverables and commit plan

- **One commit per row** (OI-158, OI-125, OI-159), each carrying its own `OPEN_ITEMS.md` flip with
  provenance; the OI-146 evidence-inventory entry lands in the OI-158 commit.
- **A `docs(cc)` fold**: a short report `cc_wave1_finalize_report.md` (the `.music21.json` regen sha256
  proof; the OI-125 battery byte-identity; the OI-159 refresh with the drift attribution and shelve
  re-confirmation; the OI-158 evidence question as filed). Update the OI rows, `STATUS.md`, and
  `cowork_handoff.md` — including the statement that **OI-145 wave 1 is now closed** and wave 2 (the `src/`
  substrate: OI-86, OI-13, OI-87, the file-table reasons) is next. Force-add this instruction file.
- **If any byte-identity proof fails,** stop at a clean boundary with the battery green, leave that row open
  with the discovery, and report.

**On completion:** wave 1 (the measurement chain) is fully hardened and closed — every graded surface
established and byte-identical, the key columns intact — and the key-layer readiness gate's next obligation
is wave 2. Report the three proofs (all expected byte-identical), the evidence question as filed, and any
discovery.
