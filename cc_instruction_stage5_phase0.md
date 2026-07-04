# CC Instruction — Stage-5 Phase 0: parameter inventory + evaluation cost (read-only) + the fold

> **ACTIVE DISPATCH (Cowork, 2026-07-04).** First CC increment of the Stage-5 fitter arc, per the SIGNED
> design `cowork_stage5_fitter_design.md` (user-ratified 2026-07-04; read §0, §2, §3, §4.1, §7 before
> starting — they define every term this instruction uses). This is Phase 0: **READ-ONLY on all code and
> corpora — no `src/` change, no tools behavior change, no constant change, no fit.** The only writes are:
> the two new committed artifacts (the parameter manifest + the Phase-0 report), one roadmap docs edit
> (Task 2), and the `docs(cowork):` fold (Task 1).

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (top entries), `C:\s\MS\BUILD_AND_TEST.md`.
> **This session reads scoring logic** (no changes): also read `C:\s\MS\docs\scoring_model.md` in full —
> the inventory is checked against its §2–§6.
>
> **Current state (Cowork-verified 2026-07-04):** branch `master`, local/unpushed, fork-only
> (`origin` = `slimvince/MuseScore`; NEVER push `upstream`). The working tree is EXPECTED DIRTY with
> exactly the Cowork narrative files listed in Task 1 — anything else dirty is a STOP. Batch gate
> (the hard regression stop): **Baroque 53 / Jazz 24 / Default 53** case-identity sets per CLAUDE.md;
> frozen corpus 352/352 per preset (last recorded manifest `git_hash = 0dd64660f4`, per the C1 report
> provenance — re-read the actual value from `tools/corpus/*/corpus_manifest.json` and report it).
> Last recorded suites: composing 1083 / notation 53 / snapshots 11 — re-verify, do not assume.
> **Hard stops:** any `src/` or tools code modification; any write under `tools/corpus/`; any batch-stop
> set-diff ≠ empty at the end-of-run sandwich; any push.
>
> **VS Code bash rules apply to every command:** append `; echo "exit:$?"`; redirect large output to a
> file and read with `head`.

---

## Task 0 — repo state + the OWED fold SHA

1. Report `git rev-parse --short HEAD`, `git status --short` (to a file if long), current branch.
2. **The acquisition-round fold commit's SHA is OWED** (its content is corroborated at the live files
   but the SHA was never stated — 22g precedent). Identify it in `git log` (the `docs(cowork):` fold
   that followed `4997757298`), verify with `git show --stat <sha>` that it contains the expected
   acquisition-round narrative files, and **state the SHA + file list in the report** (§1).
3. Confirm the dirty set equals the Task-1 fold list (+ this instruction file and the two files this
   task will create). Anything else dirty: STOP and report.

## Task 1 — the fold (`docs(cowork):`, exactly this list)

One commit containing EXACTLY these files (the accumulated Cowork narrative + the signed design + this
instruction record):
- `STATUS.md` (the 22k tail + the new 22l entry)
- `cowork_handoff.md` (the updated START HERE header)
- `cowork_score_census.md` (the §8c fitting-pool block)
- `cowork_union_search_record.md` (the two in-place license fixes)
- `cowork_stage5_fitter_design.md` (SIGNED)
- `cc_instruction_stage5_phase0.md` (this file)

Nothing under `src/`. Cite the commit SHA in the report (the report follows as its own commit citing it —
the 22j fold precedent for the same-commit/cite-SHA exclusivity).

## Task 2 — the roadmap rider (O-3; one docs edit)

Add to `docs/implementation_roadmap.md`'s **Stage 5** block: the ★ FITTING-POOL LICENSE CONSTRAINT
(restate from census §8c: ship-intended weights fit only on the PD/CC0/CC-BY(-SA) pool; NC-class — all 40
DLC corpora, MCMA, Essen… — and no-license sources are held-out validation/QA only; the fitter's
objective-vs-validation split is declared in `cowork_stage5_fitter_design.md` §3a) + one line: "Stage-5
design SIGNED 2026-07-04: `cowork_stage5_fitter_design.md`; A-3 ruled = Jazz fit deferred to the jazz-GT
conversion." Commit as its own `docs:` commit (or fold into Task 1 if you judge one commit cleaner —
state which you did and why).

## Task 3 — the parameter inventory (THE deliverable)

Produce the **parameter manifest** per design §4.1/§7, as a new committed file
`tools/param_manifest.json` (machine-readable; one row per parameter) plus a human-readable summary
table in the report. Enumerate **at source, with file+line anchors**, every hand-chosen numeric constant
in the scoring pipeline:

1. The `docs/scoring_model.md` §4 bonus/penalty terms and §5 joint terms — verified against
   `src/composing/analysis/chord/chordanalyzer.cpp` (values read at source, not from the doc).
2. The §6-block entry thresholds/margins in `postscoringgates.cpp` (incl. the outer-guard constants).
3. The per-preset values in `tools/batch_analyze.cpp` (the preset definitions).
4. The confidence squash constants and abstention bars at the contract-§3 sites (L3 margin bar, L4
   composite floors, L5 combined k, L1.5, VL-C floors — read `cowork_confidence_contract.md` §3/§5 for
   the row list).
5. The two frame θ/override constants at the F-A/F-B call sites (`forwardoverride` per contract §7 D-FS).
6. The L5 §15-13 site: the function resolver's both-licensed fall-through (family 4's home) — locate and
   anchor it; no value exists yet (that is the point); record the site.

Per manifest row: `name · site (file:anchor) · family (continuous / §6-block threshold / abstention /
§15-13 / squash / θ) · current value(s) · preset scope (shared | per-preset, with the per-preset values)
· declared style scope (style-invariant + rationale | idiom-varying, with the §4.1 rationale) · consuming
path(s) (production | dormant | both — determined by reading the call chain, stated per row with the
evidence anchor) · status (fit | frozen + rationale per design §4.6)`.

**Cross-checks (report, do not fix code):**
- Reconcile the inventory against `docs/scoring_model.md` §2–§6 both ways; every discrepancy (a constant
  in code absent from the doc, or vice versa, or a differing value) is listed in the report as a
  doc-drift defect with its evidence. Do NOT edit scoring_model.md in this dispatch (one change class per
  dispatch); the fixes ride the next scoring docs commit.
- **E-13 check (design O-6):** determine at source whether any inventoried parameter is read by the
  tuning bridge; state the finding with anchors.

## Task 4 — objective-evaluation cost (timing only; scratch only)

Measure wall-clock cost of ONE full objective evaluation, per design §4.1(2):
1. Per-preset case: regen ONE preset to a **manifest-stamped scratch dir** (never `tools/corpus/`) via
   `run_bach_preset.py --output-dir <scratch>`, then `a8_rebaseline_measure.py` limited to that preset if
   its interface allows (state if it does not — do NOT modify it; a full 3-preset measure is an
   acceptable substitute, timed as such), then `characterise_bir_false.py --corpus-dir <scratch>`.
2. All-presets case: the same ×3 (the shared-scope parameter cost).
3. Report each leg's time separately (regen / A-8 measure / batch-stop check) + totals, and the derived
   evaluations-per-hour for both cases — the checkpoint-P1 optimizer decision reads these numbers.

The frozen corpus is byte-untouched throughout (all regen to scratch); prove with `git status
tools/corpus/` at the end.

## Task 5 — the sandwich + report

1. **End-of-run sandwich:** `characterise_bir_false.py` on the REAL per-preset dirs ×3 — the 53/24/53
   case-identity sets must match CLAUDE.md exactly, set-diff empty both directions. Any difference: STOP.
2. Re-run `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` — green, no golden refresh.
3. Report `cc_stage5_phase0_report.md` (force-add; `/cc_*.md` is gitignored), its own commit citing the
   SHAs of Task 1/2/3 commits. Contents: Task-0 state + **the owed fold SHA**; the manifest summary
   (counts per family, per style-scope, per consuming path; the full row set is the JSON); the doc-drift
   list; the E-13 finding; the cost table; the sandwich record; **reuse-vs-new + what retires**
   (expected: reuses everything, new = manifest + report, retires nothing).

## STOP conditions

- Any need to modify any pinned instrument, any `src/` file, or `docs/scoring_model.md` to complete a task.
- The Task-0 dirty-set mismatch; the Task-5 sandwich mismatch; a suite regression.
- A parameter whose consuming path CANNOT be determined by reading (do not guess — mark the row
  `path: UNRESOLVED` with what was read, and continue; >5 unresolved rows = STOP and report).
- The acquisition-round fold commit cannot be identified unambiguously in the log.

## Acceptance

Fold commit exact-list ✓ · roadmap rider landed ✓ · manifest committed, every row anchored at source ✓ ·
cost table with per-leg times ✓ · sandwich 53/24/53 set-diff empty ×3 ✓ · suites green ✓ · report with
ALL commit SHAs ✓ · the owed acquisition-round fold SHA stated ✓.
