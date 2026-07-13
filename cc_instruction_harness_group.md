# CC instruction — the harness group (OI-145 wave-1 remainder): OI-135 / OI-136 / OI-137 + the OI-153 register lint

**Dispatch author:** Cowork, 2026-07-13. **Type:** a FIXING session on the shared measurement harness
`tools/batch_analyze.cpp` and the establishment/register tooling — **NOT inference coding.** No
`src/composing` analysis behavior may change. This is the last wave-1 item of the OI-145 key-layer
readiness gate; the two figure-moving wave-1 remainders (OI-132, OI-144) already landed user-ratified,
so this dispatch's governing outcome is **byte-identical: no grading digit moves, the committed corpus
regenerates bit-for-bit, no golden refresh is owed.**

Read first, in this order (the standing convention): `CLAUDE.md` in full (#1–#19 + the fact-publication
corollary + the conventions + the self-check section + the VS Code bash rules), then `OPEN_ITEMS.md`
(the ONE register), then `BUILD_AND_TEST.md` and `STATUS.md` for the current HEAD/baselines. Do not rely
on memory for HEAD, baselines, or line numbers — read them, and re-locate every cited line by symbol
(the audit line-refs below are as-of the L5 pass-1 harness report and may have drifted).

---

## 0. Scope, and what is explicitly NOT in scope

**In scope (the harness group):**
- **OI-135** — single-source `batch_analyze.cpp`'s value-copied inference-affecting constants (the 21
  hand-copied "Default" mode priors + the hard-coded `onsetBoundaryThreshold = 0.25`).
- **OI-136** — surface the six undocumented harness measurement flags in `printHelp()` (or mark them
  internal-only in the help contract).
- **OI-137** — the output line-ending discipline (standard-output CRLF vs diagnostic LF) + the
  exit-path asymmetry (force-exit vs normal return): **fix only if provably inert; otherwise establish
  and document.**
- **OI-153** — the register ID-collision lint (a duplicate `| OI-N |` check) added to the establishment
  battery / register tooling, per the OI-153 row's "the lint lands at the next dispatch (the harness
  group's opening batch)."
- **OI-52** — build the one shared "does our root equal the GT root" helper across the four Python graded
  sites (this is the Python-instrument sibling of the harness single-sourcing; user-directed to fold in,
  2026-07-13). Its row is already DECIDED-BUILD and ASSIGNED to "the next measurement-instrument
  touch = the OI-145 wave-1 remainder" — which is this dispatch.

**NOT in scope — do not fold these in without a separate user instruction** (surface them, do not act):
- The OI-125 / OI-133(c) hand-set grading-tolerance re-derivations (#19; the OI-145 row schedules them
  "later") and OI-127.

Note: this dispatch now touches BOTH the C++ harness (`batch_analyze.cpp`, Tasks 1–3) AND the Python
measurement instruments (Task 4, OI-52). The establishment battery covers both sides — `regen` proves the
C++ recompile inert, `a8_diff` proves the Python root-comparison fold inert.

---

## 1. Governing constraints (apply to every task)

1. **Byte-identity is the whole-dispatch success condition.** Every fix here is to duplication,
   documentation, tooling, or output-discipline — none may move a measurement. Prove it (see §2).
2. **The Premise Gate (#17).** Before each code change, write the quantitative prediction (§6) BEFORE
   measuring. The standing prediction for this dispatch is "0 `.ours.json` differ, all 352×3 per-score
   sha256 identical, the establishment battery reproduces byte-for-byte, both C++ suites + the harness
   regression test stay green." A measured deviation from that prediction is a STOP (#13), not something
   to absorb.
3. **No self-invented labels / abbreviations / numbering / jargon** (the convention). Use the names the
   repository already has — OI-N, DT-N, the principle numbers, "the establishment battery," "the
   reproduce-check," "the harness group." If a thing has no name, describe it in plain words.
4. **The self-check after every coding exercise.** After each change and BEFORE reporting: re-read the
   actual diff of every touched file (not your memory of writing it) against the guiding principles, the
   conventions, the gate/threshold policies, and `DEFECT_TYPES.md`. Any violation is surfaced
   immediately (its own `OPEN_ITEMS.md` row if it cannot be corrected in scope).
5. **The VS Code bash rules (mandatory, every command):** append `; echo "exit:$?"` to any command that
   may return non-zero; never let one bash call produce large output — redirect to a file and `head` it.
   Build via `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`.
6. **Fork-only push discipline.** Commit only what these tasks authorize; push to `origin` only, never to
   `upstream` (confirm push-disabled with `git remote -v`). The Snap fix and the MusicXML declared-mode
   fix are do-not-revert local patches — leave them.
7. **Discovery protocol.** Any grading digit that moves, any poisoned/overwritten committed artifact, any
   newly discovered issue → its own register row **in the same commit that records the discovery** +
   STOP-and-report to the user. Never silently absorbed (#3/#13).

---

## 2. The establishment battery — run it as the proof, every fix

`tools/audit/hardening_battery.py` (`979e07db46`) already orchestrates the committed instruments against
the committed reference. Record its clean starting state before any fix, and re-run the relevant gates
after each fix and at the end:

| Gate | What it proves | When |
|---|---|---|
| `a8_diff` | `a8_rebaseline_measure` → scratch, then `robust_stop_diff` vs `tools/robust_stop`: exit 0, every preset (+0/−0), WiR coverage unchanged, class-(b) Δ+0 | after every fix |
| `calib` | `calibration_fit` → scratch: all 4 `tools/calibration_maps/*.json` reproduce sha256-identical | after every fix |
| `validate` | `validate_corpus_dir` on all 3 presets (352/352, git `c50002fee1`) | after every fix |
| `fixture` | `stage5_fit_driver` fixture: root-% stability vs the ratified 66.04/64.98/65.93, batch 54/24/54 | start + end |
| **`regen`** | **`run_bach_preset` → scratch, per-score sha256 vs `tools/corpus` for all 3 presets** | **MANDATORY here — this dispatch touches `batch_analyze.cpp`** |

**The `regen` gate is the load-bearing one for this dispatch.** Prior wave-1 sessions could skip it
because none touched `batch_analyze.cpp`; you are recompiling the harness, so a full 352×3 scratch regen
matched per-score sha256 against the committed `tools/corpus/{baroque,jazz,default}` is the proof that
OI-135's single-sourcing changed nothing. Additionally run, per `CLAUDE.md`: `composing_tests.exe`,
`notation_tests.exe`, `pipeline_snapshot_tests.exe`, and the harness regression test
`tools/tests/test_batch_analyze_regressions.py` — all must stay green with no golden refresh.

---

## 3. Task 0 — commit Cowork's waiting register/design edits (staged by name, unread), then add the OI-153 lint

**(0a) Commit the uncommitted working-tree edits Cowork left staged for you.** Per the handoff, the
following are Cowork-authored and awaiting a Task-0 register commit; stage them **by name** and commit
them **without reading/altering their content** (they are this session's authored context, not your
audit surface):

- `OPEN_ITEMS.md` (the OI-152 renumber + the new OI-153 and OI-154 rows)
- `cowork_evidence_inventory.md` (§8b explainability)
- `cowork_key_layer_design_opening.md` (the keep-vocabulary refinement + the governing late-binding framing)
- `cowork_handoff.md` (the current session-close block)

**`cowork_joint_key_chord_design.md` stays UNSTAGED** (the standing known carry — do not commit it).

Before committing: run `git status --porcelain` and confirm the working tree matches this expectation. If
any OTHER file is modified, or one of the four is missing, **STOP and report** — do not commit a working
tree that differs from what the handoff describes. Commit message: a `docs` register commit naming the
rows moved (OI-152 renumber, OI-153, OI-154) — no self-invented tag.

**(0b) Add the OI-153 register-ID-collision lint.** A duplicate-`| OI-N |` check, run at every fold.
Preferred home: fold it into the establishment battery / register tooling so it runs mechanically
(the OI-153 row calls it "trivially scriptable"). It must scan `OPEN_ITEMS.md`, report any OI number that
appears as a row ID more than once, and exit non-zero on a collision. Verify it flags a synthetic
duplicate and passes clean on the current register (the OI-150→OI-152 renumber already resolved the one
real collision). Flip the OI-153 row to resolved with provenance in the commit that lands the lint.

---

## 4. Task 1 — OI-135: single-source the value-copied harness constants (the substantive task)

Two value-copies, both currently kept in sync only by a code comment, neither in `param_manifest.json`:

**(a) The 21 "Default" mode priors.** `applyPreset()`'s "Default" branch (audit ref `batch_analyze.cpp`
~:196–216) hand-copies the 21 app `MODE_PRIOR_*` `setDefaultValue` defaults from
`composingconfiguration.cpp init()`. The NAMED presets already read the single source
`modePriorPresets()` — only the "Default" branch duplicates. The values are **proven copies today**, so
single-sourcing must be **exactly byte-identical**.

- **Preferred fix (#6 total unification):** have the "Default" branch read the composing configuration's
  own default values rather than a hand-copied literal block — i.e. the CLI initializes/reads the
  composing Settings-framework defaults (this is the config-unification the handoff names). This is the
  real engineering: a CLI tool pulling the Settings defaults may require initializing that framework.
  **Desk-simulate it first (#17c):** trace, by hand, whether `batch_analyze` can obtain the
  `composingconfiguration` defaults without dragging in unwanted runtime state, and confirm the values it
  would read are bit-identical to the current literals. Write that prediction before you build.
- **Documented fallback (only if the Settings-framework read proves infeasible/heavy):** a mechanical
  sync test on the `modepriorpresets_tests` pattern that FAILS if the harness "Default" literals drift
  from the app defaults. This guarantees byte-identity trivially (no behavior change) but is a guard, not
  a true single-source; if you take it, record WHY the single-source route was rejected, as a note and (if
  it leaves a residual) an `OPEN_ITEMS.md` line.

**(b) `onsetBoundaryThreshold = 0.25`** is hard-coded at three sites (audit refs :597, :2555, :3718),
duplicating the `IComposingAnalysisConfiguration` default (fallback 0.25) the user-facing bridge reads.
Unify to one source so a config-default change cannot make the harness silently stop measuring the user
pipeline. Byte-identical (the value coincides today).

**Proof for Task 1:** BUILD, then the full `regen` gate (352×3 sha256 identical) + the rest of the
battery + all four test suites green. This is the one task where the compiled binary changes, so the
reproduce-check is non-negotiable. If ANY `.ours.json` differs, the single-sourcing is not value-identical
— STOP, do not adjust goldens.

Flip OI-135 to resolved with provenance; if (b)'s roadmap-0.6 divergence note or a chosen-fallback
residual remains, keep the row open on that named remainder rather than closing it falsely.

---

## 5. Task 2 — OI-136: document the six undocumented harness flags

`batch_analyze.cpp` parses `--reachback-ab` (audit ref :3982) and the five
`--key-in-neither/-keysig-only/-candidate-only/-both/-leading-tone` emission-weight flags (:4093) in
`main()`, but `printHelp()` lists none and `BUILD_AND_TEST.md` defers to `--help`. Both are default-off
diagnostic-only paths (production byte-identical) — this is a **contract-completeness** fix (DT-25), not a
behavior change.

Add the six flags to `printHelp()` (or, if they are genuinely internal measurement scaffolding, mark them
explicitly as internal/diagnostic in the help contract so the contract surfaces their existence). Verify
`--help` output and re-run the harness regression test. Doc/text-only — byte-identity of the corpus is
untouched (but still confirm the battery is clean). Flip OI-136 with provenance.

---

## 6. Task 3 — OI-137: line-ending discipline + exit-path asymmetry (fix only if provably inert)

Two latent items; **neither is a defect today** and both interact with the committed corpus, so the
default posture is **establish-and-document, not change**:

**(a) Line endings.** The standard output file opens `QIODevice::Text` (audit ref :4593) → on Windows the
committed `.ours.json` corpus is CRLF, while the diagnostic paths write `std::ofstream(std::ios::binary)`
(LF). **Prediction to write first:** changing the standard path to binary/LF would rewrite every committed
`.ours.json` byte → the `regen` gate would show all 352×3 differing = a full-corpus re-baseline event,
which is **out of scope for a byte-identical dispatch and requires explicit user ratification (O-12
ritual).** So do **not** flip the standard path here. The authorized action is to (i) confirm that
prediction with a scoped one-file test, (ii) document the two-discipline split and its dependence on
Windows+Text-mode regeneration (compounding the O-12/OI-34 corpus git-tracking decision), and (iii) if the
diagnostic-vs-standard mismatch can be made consistent WITHOUT changing the committed corpus bytes (e.g.
aligning the diagnostic writers, which are not corpus), do that and prove the corpus regen is still
byte-identical.

**(b) Exit-path asymmetry.** The standard path force-exits (`::TerminateProcess`/`std::_Exit`, :4615–4621,
to dodge a Qt-TLS hang) while the ~10 diagnostic early-returns return normally. Whether the diagnostic
returns are exposed to the hang is UNESTABLISHED (not observed this arc). **Establish it:** determine
whether unifying the exit discipline is provably safe (no reintroduced hang) and provably inert (exit
codes unchanged — note `--validate-slices` returns a MEANINGFUL 0/2 a crash could mask). If provably inert
AND safe, unify with the justification recorded; if not, document the asymmetry and the reason the
force-exit exists, and leave it. Do not risk the Qt-TLS hang to tidy this.

Flip OI-137 with provenance describing exactly what was changed vs documented. If it ends as
document-only, the row can close as established-and-documented (a #16 establishment item), or stay open on
the deferred corpus-line-ending re-baseline if you judge that a real future obligation — your call, stated.

---

## 6b. Task 4 — OI-52: the one shared root-comparison helper (Python instruments)

"Does our root equal the ground-truth root" is a bare `==` re-implemented at every graded site —
`a8_rebaseline_measure.py` (the GOVERNING hard stop; audit ref :148), `compare_analyses.py` (`_roots_match`,
:243–244), `compare_rn.py` (the robust-unit grid, :352/:370/:474). The derivation behind it is
single-owned; only the one-line comparison repeats. The row is **DECIDED: BUILD the shared helper** (the
A6 verdict, user-ratified 2026-07-10 under OI-42 — "add the one shared helper at the next instrument touch;
close the row then").

**The substance is NOT `a == b` — it is the abstain convention (OI-33).** "What does a missing/abstained
root mean" must be decided **identically** at every site; today `a8_rebaseline_measure.py:34` states it in
prose and the other sites each re-implement the comparison. This is exactly the construction that produced
OI-132's discovery D2 (two copies of one comparison embedding divergent readings, so folding them moved a
graded figure). So:

- Extract ONE helper that encodes the root-equality-plus-abstain rule once, and route all four sites
  through it.
- Because `a8_rebaseline_measure` is the governing hard-stop metric, **any behavioral divergence between
  the current per-site `==` logic and the shared helper shows up directly in `a8_diff`.** A/B it: the
  helper must reproduce each site's current verdicts exactly. If ANY preset moves (+0/−0 fails, or the
  key/root columns shift), the fold is NOT value-identical — STOP and report (a D2-class discovery), do
  not re-baseline silently.
- Prove byte-identical: `a8_diff` +0/−0 all presets, class-(b) Δ+0, the Python metric suites green, and
  `compare_analyses`/`compare_rn` outputs unchanged on a spot check.

Flip OI-52 to resolved with provenance. Per the A6 verdict it "need not be its own commit" — you may land
it folded into the measurement-instrument tooling touch, but it must carry its own `OPEN_ITEMS.md` row
flip (#14).

---

## 7. The Premise Gate — write these predictions BEFORE measuring (#17b)

Record, before running the battery for each task, the expected result and the fire condition. The
whole-dispatch prediction (state it up front): every gate reproduces byte-identical; `regen` = 352×3
sha256 identical; `a8_diff` +0/−0 all presets with class-(b) Δ+0; `calib` 4/4; `validate` 3/3; `fixture`
root 66.04/64.98/65.93; all four suites green; key columns unmoved (home 71.42/67.83/70.65, local
65.99/62.98/65.71). Per-task, add the specific desk-sim prediction (Task 1's value-identity trace; Task
3(a)'s "all 352×3 differ if I flip Text→binary"; Task 3(b)'s exit-code inertness). A landing on-prediction
to the digit is what right looks like; any surprise is the STOP.

---

## 8. Deliverables and commit plan

- **Task-0 register commit** (Cowork's four edits, staged-by-name-unread; `cowork_joint_key_chord_design.md`
  left unstaged) + the OI-153 lint (its own commit or folded into Task-0's tooling touch, with the OI-153
  row flipped).
- **One fix commit per OI**, each carrying its own `OPEN_ITEMS.md` row flip with provenance (the standing
  one-revertible-provenance-stamped-commit-per-change discipline, #14).
- **A `docs(cc)` fold** at the end: a report `cc_harness_group_report.md` (the establishment-battery
  before/after tables, the regen proof, each task's prediction-vs-outcome, any discoveries), the OI row
  updates, and the `STATUS.md` + `cowork_handoff.md` updates. Force-add this instruction file.
- **If ANY task cannot land byte-identical or safe,** stop at a clean row boundary with the battery green,
  leave that OI open with the reason, and report — exactly as the measurement-chain session deferred this
  very group at a clean boundary.

**On completion:** the OI-145 wave-1 remainder is closed (subject to any OI-137/OI-135 residual you
name); waves 2–3 follow, and the key-layer readiness gate lifts when all its listed rows close. Report
back with the battery deltas (expected: all zero), the regen result (expected: 352×3 identical), and any
discovery surfaced.
