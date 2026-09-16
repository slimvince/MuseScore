# CC instruction — the joint estimator's embedded-tables codegen (Decision D1 executed) + Task 0: the second ratification-record commit

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, and the two ratified governing documents this dispatch
> executes: `C:\s\MS\cowork_notation_output_contract.md` (★ ratified 2026-07-26 — §2
> provenance-on-the-surface and Decision D1's delivery are THIS dispatch's scope) and
> `C:\s\MS\cowork_notation_adoption_increment.md` (§5 Decision D1; §8 the verification plan).
> `OPEN_ITEMS.md` at session start as always.
>
> **Current state:** branch `master`; expected HEAD `21422ee77d` (the audit-artifacts commit,
> pushed) — verify by `git show --stat 21422ee77d` and that HEAD matches; mismatch = STOP.
> The working tree carries FOUR Cowork-authored uncommitted edits riding Task 0:
> `cowork_notation_output_contract.md` (new, ratified), `cowork_notation_adoption_increment.md`
> (§9 closure note + §10 audit-findings/pedal-ruling section), `OPEN_ITEMS.md` (the OI-194 row's
> pedal sharpening), `cowork_handoff.md` (audit-verification + contract blocks). Verify these
> are the only non-yours diffs; anything else unexpected is a STOP. This dispatch file stays
> untracked (`/cc_*.md` ignore policy).
>
> **Hard stops, always:** push toward `upstream` (origin only); any file outside the touchable
> set below; a surprise (#13) — during an establishment step especially, a surprise is a STOP,
> never a workaround. VS Code bash rules apply to every command (`; echo "exit:$?"`; redirect
> large output).
>
> **No mid-flight steering:** this instruction is self-sufficient; anything not covered waits
> for the report.

**Dispatch author:** Cowork, 2026-07-26, at the user's ratification of the output-surface
contract. **This dispatch changes NO inference value and NO committed output** — it changes the
tables' DELIVERY (filesystem → embedded source) and must PROVE value-neutrality. The notation
path stays untouched and legacy; the joint module stays production only on the batch/corpus
surface.

**Touchable set:** `src/composing/analysis/joint/**` (+ its tests under `src/composing/tests/`
and their CMake lists), `tools/joint_estimator/gen_embedded_tables.py` (new generator),
`tools/batch_analyze.cpp` (the table/weight loading switch only), `ARCHITECTURE.md` (the
joint-estimator as-built section's delivery note), `STATUS.md` (your closing entry), plus the
Task-0 files above. Nothing else.

---

## Task 0 — the second ratification-record commit (ONE commit, first)

Commit the four riding Cowork files exactly (verify nothing else staged), message:
`ratification record: P1 pedal-point ruling (voice-independent ornament class, OI-194) + the
notation output-surface contract (user, 2026-07-26)`. Push origin only. Report the hash.

## Task 1 — the generator and the embedded artifacts

**The ratified design (D1 + contract §2), stated precisely:**

1. **New generator `tools/joint_estimator/gen_embedded_tables.py`** (read-only over the
   artifacts; #17f — the generated file is written by the tool, never by hand). Inputs, by
   exact path: `tools/joint_estimator/tables_all.json`, `note_tables_all.json`,
   `factor_presence_all.json`, `fermata_boundary_addendum.json`, `mode_marginal.json`, and the
   SELECTED weight vector — extracted from `decode_parity_ref.json`'s `selected_weights` (the 13
   named weights; embed the extracted vector + its provenance label `random07`, NOT the whole
   parity file). Output: ONE generated C++ file in `src/composing/analysis/joint/` (descriptive
   name, e.g. `jointembeddedartifacts.cpp` + a small header) containing:
   - each artifact's JSON **bytes verbatim** as a string constant (no re-serialization, no
     parsed-structure codegen — the bytes ARE the artifact);
   - each artifact's **sha256** and the generator's provenance header (source paths, hashes,
     generation command, date, the corpus/instrument provenance quoted from the artifacts'
     own manifest fields where present);
   - the **§2 provenance constants** the contract publishes on the record: the artifact hashes,
     the weight-vector identity string, and a decoder-version string (the module's own; define
     it here). These are DECLARED DORMANCY (fact-publication corollary): their named consumer
     is the record build (the next dispatch) — say so in the header comment.
2. **Why verbatim bytes (the ratified reasoning, for your header comment):** the existing
   `JointTables::load` / `FittedAdapter` JSON parsing is the ESTABLISHED path (#19, carried
   forward); embedding bytes and parsing them through the same code keeps ONE parse path (#6)
   and makes the establishment check trivial (byte equality). Generating parsed C++ structures
   would be a second, unestablished representation — rejected.
3. **Loading:** the module gains an embedded-source construction (`load`-equivalent reading the
   embedded strings). **The production table/weight source becomes the embedded data
   everywhere the joint decode runs in production** — `tools/batch_analyze.cpp`'s
   `--joint-inference` path switches to it (the `<artifact-dir>` argument remains for the
   corpus/reference inputs the diagnostics read — `note_events.json`, parity references — which
   are measurement data, not fitted values). Filesystem table-loading remains ONLY in
   tests/diagnostics, where it is the establishment comparator, and says so in a comment.

## Task 2 — establishment (#19; all of it BEFORE the report claims delivery)

1. **The drift guard (a permanent unit test):** embedded bytes' sha256 == the committed artifact
   files' sha256, per artifact, and the embedded weight vector == `decode_parity_ref.json`'s
   `selected_weights` value-exact. This test is the standing guard that the embedded data can
   never silently diverge from the committed artifacts (DT-2's structural reinforcement).
2. **Decode invariance at the objects:** regenerate the corpus via
   `run_bach_preset.py --joint-inference` (all three preset dirs) against the embedded-source
   build; the result must be **byte-identical to the committed corpus** (the tables are
   byte-identical and the decoder unchanged, so any diff is a defect — STOP). Then the pinned
   sandwich: `a8_rebaseline_measure.py` + `robust_stop_diff.py` → run-diff **(+0/−0)** on every
   preset, every column identical to the digit, OVERALL PASS. No re-baseline, no snapshot, no
   golden refresh — nothing may move.
3. **Suites:** `composing_tests` (including the new drift guard + the existing joint tests —
   which now also exercise embedded loading), `notation_tests`, `pipeline_snapshot_tests` — all
   green, NO golden touched (the notation path is not on the joint module; any snapshot change
   is a STOP).

## Task 3 — doc sync (#10, same commit as the code)

- `ARCHITECTURE.md` joint-estimator as-built section: the delivery paragraph — tables/weights
  embedded as generated source (provenance-locked at build time), the regeneration step
  (`gen_embedded_tables.py`) as the fit-event's new mechanical step, the drift guard named.
- `STATUS.md`: your closing entry (facts + figures from the artifacts of this dispatch, not
  prose memory).

## Commits and report

Task 0 first (one commit). The codegen work: ONE commit (generator + generated file + loading
switch + drift guard + doc sync — one change-class: the delivery mechanism), after all of Task 2
passes. Push origin only. **Report:** both hashes; the generated file's provenance header
excerpt; the drift-guard result; the regen byte-identity result and the robust-stop diff output
(+0/−0 per preset); suite totals; the reuse-vs-new / what-retires section (what retires: the
production path's filesystem table dependence — name where file-loading remains and why);
anomalies (any deviation from byte-identity anywhere = STOP, already). The standing self-check
(CLAUDE.md) before reporting: re-read the actual diffs of both commits against the principles
and `DEFECT_TYPES.md`.
