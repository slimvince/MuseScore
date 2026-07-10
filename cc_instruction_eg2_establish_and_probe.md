# CC INSTRUCTION — EG-2: Establish the E0 Instrument, then Run the Rebuilt-vs-Legacy Probe

> **Issued by Cowork, 2026-07-10 (session 36).** Governing docs, READ FIRST in this order:
> `CLAUDE.md` (principles #1–#19 — especially the NEW #17–#19), `cowork_eg2_scoping.md` (the
> pre-registered ledger; §5 predictions are RECORDED — the probe verdict is read against them,
> never adjusted to them), `cowork_l1_l5_premise_debt_audit.md` (Tier-1 context),
> `cc_e0_fullspine_report.md` (the instrument you are establishing), `BUILD_AND_TEST.md`,
> `STATUS.md`. **Fork-only; NEVER push `upstream` (`cfc7eb5e39` HARD STOP). Commit only per the
> discipline below. All bash: append `; echo "exit:$?"`; redirect large output to files.**
>
> **Scope declaration:** Tasks 1–2 are instrument/establishment work; Task 3 is a READ-ONLY
> explorational probe (surprise-permitted scope — surprises are REPORTED as findings, never
> built around). NO production behavior change of any kind: no constant tuned, no golden
> refreshed, no robust-stop reference re-baselined, `tools/robust_stop/` untouched, no adoption.
> The verdict is handed UP (#8) — the go/no-go decision is Cowork's/the user's.

## Task 0 — Preconditions (verify, don't assume)

1. `git log --oneline -3` must show HEAD at or after `3d8cf74e52` (the desk-sim commit). If the
   working tree is dirty beyond your own work: STOP and report.
2. Read `cowork_eg2_scoping.md` §2 (ledger P1–P6, gaps G1–G5), §3, §5 IN FULL. Do not proceed
   without them in context.

## Task 1 — Establish the E0 full-spine instrument (#19; scoping §3)

The E0 chain (`batch_analyze --dump-fullspine`) is currently NOT established: stale manifest
stamp (`d1d4d3d7f0` vs corpus `c50002fee1`), no `validate_corpus_dir` wiring, no
reproduce-check, unresolved coverage question. Establish it:

1. **Exact invocation:** derive the correct `--dump-fullspine` CLI from
   `cc_e0_fullspine_report.md` + the `batch_analyze.cpp` source (`runFullSpine`,
   ~`:2889-3064`; dispatch ~`:3953/:4406`). Do NOT guess flags.
2. **Override-OFF variant (gap G3):** the E0 chain runs the resolver's fine-grain override
   live. The probe arm MUST run with it disabled. Check first whether the harness/params
   already expose a way (e.g. `FunctionResolverParams.override` θ / `baseBar` settable from the
   driver, or an existing flag). If NOT: add a **minimal default-OFF flag**
   (`--fullspine-no-override` or equivalent) to the diagnostic driver only — one revertible
   `feat` commit (#14), production byte-identity re-proven (flag-off default path untouched;
   both suites green; NO golden refresh). If this requires touching anything outside the
   diagnostic driver + resolver-params plumbing: STOP and report instead.
3. **Fresh dumps, stamped:** dump Baroque + Default (Jazz optional, consistency-only) to fresh
   scratch dirs (NOT `tools/corpus/<preset>` — never contaminate the validated corpus dirs).
   Stamp a `manifest.json` per the a8 pattern: corpus `git_hash` (must equal the pinned
   `c50002fee1` state — regen the corpus first if needed via `run_bach_preset.py`, which exits
   nonzero unless 352/352), instrument commit, flag set, timestamp.
4. **Reproduce-check:** run each dump TWICE; assert byte-identical (`diff -r`). Any
   non-determinism is a STOP (the R10-b lesson).
5. **Coverage-equality check (the P4(c) insulation check, #17(e)):** grade BOTH arms (fresh E0
   dump vs the committed legacy `tools/corpus/<preset>` `.ours.json`) with the a8 substrate and
   assert the per-piece DCML covered-span sets are EQUAL between arms (the unit is
   segmentation-invariant only over covered spans). Report per-piece coverage counts. Any
   asymmetry: STOP — the comparison is invalid until explained.
6. **Establishment record:** write the establishment evidence (invocation, manifest, reproduce
   hashes, coverage table) into the Task-4 report. The instrument is established ONLY when
   1–5 are all green.

## Task 2 — GATE

If ANY Task-1 item failed or was skipped: STOP. Write the report (Task 4) with what was
established and what was not, and do NOT run Task 3. An unestablished instrument is FORBIDDEN
from producing the go/no-go number (#19).

## Task 3 — The probe (read-only, explorational)

Grade rebuilt (E0, override-OFF) vs legacy (committed corpus) against DCML on the a8
union-of-boundaries unit, variant-b, root axis, per preset (Baroque, Default; Jazz
consistency-only if dumped):

1. **The number:** class-(b) (pitch-class-decidable-root) root-disagree DURATION per arm per
   preset, same classification machinery as the robust stop. Report both arms' totals + the
   delta in % (the §5 aggregate prediction band is −15…40 %).
2. **The explained set-diff:** per-run (stem@runStartTick) diff between arms — runs fixed by
   rebuilt, runs newly broken by rebuilt, each tagged with its two-tier class. Full
   enumerations to files; counts + the 20 largest-duration cases of each direction in the
   report.
3. **The five §5 cases:** report the rebuilt arm's actual root at each of
   `bwv10.7@36000`, `bwv352@1440`, `bwv272@4320`, `bwv174.5@6240`, `bwv416@10080`
   (both slices for the last) — side by side with the §5 prediction. Prediction hits and
   misses are BOTH findings; do not smooth.
4. **G4 confirm:** the dim7-rotation distribution on the rebuilt arm (how many symmetric dim7
   sonorities, how many spelled-pinned, how the pins score vs DCML) — confirms or refutes the
   "extensions gap has no root path" disposition.
5. **New-error mechanism census:** classify the newly-broken runs (item 2) — how many match the
   predicted "short passing tone completes a stronger template" mechanism (the bwv416-slice-2
   type)? A DIFFERENT dominant mechanism among new errors is a first-order finding: report it
   with 3 score-verified examples.
6. **RN + key tracked beside** (the robust-unit convention): report RN-agree and key-agree for
   both arms, clearly labeled secondary (G4 makes rebuilt RN/quality expectations LOW — that is
   declared, not a surprise).

## Task 4 — Report + fold

Write `cc_eg2_probe_report.md`: establishment record; the numbers; the set-diff summary; the
five-case table (prediction vs actual); G4; the new-error census; **an explicit
"§5 prediction vs measured" verdict line per prediction** — hit / miss / partial, with the G1
asymmetry applied as declared (a rebuilt win under the single-home-key handicap is
decision-grade; a loss is diagnosed, not concluded). NO recommendation to build — findings
only; the decision is handed up. Commits: the optional Task-1 `feat` (separate, revertible),
then one `docs(cc):` fold (report + force-add this instruction, which is gitignored). Update
STATUS.md's Last-updated block per convention. Push fork-only or leave unpushed — do NOT touch
`upstream`.

## Standing constraints (repeat, mandatory)

- Both suites must pass after any code change; pipeline snapshot goldens NOT refreshed.
- `tools/robust_stop/` reference artifacts UNTOUCHED (no re-baseline — nothing is adopted here).
- No constant fitted or tuned; no `src/composing` production-path change (the optional flag is
  driver/params plumbing only, default-OFF, byte-identity proven).
- Never hallucinate paths, flags, or numbers — read the source; verify at objects (#15).
- Any surprise in Tasks 1–2 (instrument work) is a STOP (#13). Surprises in Task 3 are
  explorational findings: report faithfully against §5.
