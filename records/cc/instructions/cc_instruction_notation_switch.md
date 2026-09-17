# CC instruction — THE SWITCH (user-ratified 2026-07-27): the notation path flips to the record arm — ONE revertible commit

> **Read first (every session):** `C:\s\MS\CLAUDE.md` (gate block (A) — you will update its
> STAGED SCOPE text in this very commit; read it as the outgoing state), `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), the P7 completeness artifact
> (`tools/notation_seams/partition_completeness.json`) and the P6 classified report
> (`tools/notation_seams/dualarm_classified_report.json`) — **the report is this commit's
> verified-correct precondition and your golden-diff oracle.**
>
> **THE USER HAS RATIFIED THE SWITCH (2026-07-27).** This dispatch performs the behavior
> change: the in-app notation analysis is produced by the record path. ONE revertible,
> provenance-stamped commit (#14); the ratification, the P6 report, and the establishment
> chain are cited in the commit body.
>
> **Current state:** branch `master`; expected HEAD `4967d6b724` (P7, pushed) — verify;
> mismatch = STOP. Riding Cowork edit: `cowork_handoff.md` (the ratification block; commit
> with the switch — verify it is the only non-yours tracked diff). This dispatch file stays
> untracked.
>
> **STOP conditions:** any unit-class test failure (never edited to pass); **any refreshed
> golden's diff containing a difference class the P6 classified report does not explain**
> (identical / inference-driven / presentation-rule / input-scoping-zero are the explained
> classes — anything else is a STOP); any change to the committed corpus, `tools/robust_stop/`,
> or any non-pipeline-snapshot golden (the flag is notation-side; the batch surface must not
> move — verify explicitly); any need to touch a file class not listed. A surprise during an
> adoption-class commit is a STOP, not a workaround (#13).
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-27, at the user's ratification. **One commit, one change
event** — the legacy path stops being the notation output producer; its code stays compiled
and dormant (deletion is the OI-180 retirement map's business, later dispatches).

**Touchable set:** the flag default site(s) (`composingconfiguration.cpp` + the interface doc
comment), `src/notation/tests/pipeline_snapshot_tests/**` goldens (the sanctioned refresh),
any test that pins the DEFAULT arm and must now pin it explicitly (see disposal below),
`CLAUDE.md` (gate block (A) staged-scope text), `STATUS.md` + `STATUS_ARCHIVE.md` (the
OI-205(a) sweep), `ARCHITECTURE.md`, `OPEN_ITEMS.md` + `open_items/` (the row/note updates
below), the riding Cowork file. Nothing else.

---

## The commit's contents (all of it, together, revertible as one)

1. **The flip:** `useJointNotationRecord` default OFF → ON (`Val(false)` → `Val(true)`); the
   interface comment updated — the flag now selects the LEGACY arm when explicitly false, and
   the flag AND the legacy branch retire together at the OI-180 map.
2. **Test disposal, per kind (the ratified rule):**
   - Tests that explicitly scope the flag (the RAII-guard record-arm and dual-arm tests, and
     any legacy-arm test that explicitly sets false) are UNTOUCHED — they pin their declared
     arm and remain valid until the map.
   - Tests that pin the DEFAULT arm's output: snapshot-class → refreshed (below); unit-class →
     if one fails under the new default, STOP and report (never edit to pass). If a legacy
     unit test merely needs the flag explicitly false to keep pinning the legacy arm (a
     scoping fix, not an assertion change), that is permitted and enumerated in the report.
3. **The golden refresh:** `pipeline_snapshot_tests.exe --update-goldens`, then re-run to
   green. **Then the establishment step: diff every refreshed golden against its predecessor
   and reconcile the diff against the P6 classified report** — every difference must belong
   to an explained class (inference-driven / presentation-rule with its rule; input-scoping
   must be absent). Write the reconciliation as a small generated artifact
   (`tools/notation_seams/switch_golden_reconciliation.json`: per golden, per difference
   class, counts + spot citations). An unexplained class ⟹ STOP.
4. **Suites:** all three green under the new default (plus the explicitly-scoped arms). The
   batch surface proven unmoved: `test_batch_analyze_regressions` passes; no
   `tools/corpus/` or `tools/robust_stop/` diff exists (verify with git status before
   committing).
5. **The doc/register sync (#10, same commit):**
   - `CLAUDE.md` gate block (A): the STAGED SCOPE paragraph updated — the notation layer now
     runs the joint estimator's record path (user-ratified switch 2026-07-27, this commit);
     the migration state is CLOSED on both surfaces; the legacy analysis remains compiled,
     dormant, awaiting the OI-180 map.
   - `STATUS.md`: the switch entry (facts + the reconciliation artifact's counts) **and the
     OI-205(a) archive sweep**: superseded dated entries move VERBATIM to
     `STATUS_ARCHIVE.md` (keep: the switch entry, the partition-close entry, the active
     next-action pointers); reconcile the moved text byte-exact (the doc-split discipline —
     state the method in the report).
   - `ARCHITECTURE.md`: the record-path section's dual-arm posture → SWITCHED (the record
     path is THE notation path; the legacy arm dormant until the map).
   - Register: `open_items/OI-180.md` dated note — the forward exit EXECUTED on the notation
     surface, the retirement map now fully live; `OPEN_ITEMS.md` OI-205 row → half (a) done
     (this commit), half (b) open; `open_items/OI-203.md` dated note — the latency is now on
     the DEFAULT path, the cache increment's priority rises. INDEX rows only where status
     actually changes.
6. **Commit + push origin only.** Message: `THE NOTATION SWITCH: the record path is the
   production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens
   refreshed against the P6-classified record output; staged scope CLOSED` + the provenance
   citations in the body.

## Report

The hash; the golden-reconciliation counts (per class — and the explicit statement that no
unexplained class arose); the test-disposal list (any legacy test given explicit flag-false
scoping, enumerated); the suite totals (new default + scoped arms); the batch-surface
no-change proof; the STATUS sweep's reconciliation method + moved-entry count; every doc/row
touched; anomalies (a surprise is a STOP). Standing self-check before reporting: re-read the
actual diff of every touched file against the principles and `DEFECT_TYPES.md`.
