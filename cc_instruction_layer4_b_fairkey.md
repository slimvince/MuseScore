# CC Instruction — Layer 4 Increment B: fresh build+test + the fair-key re-measurement (read-only)

> Increment B (`5f6b9828a5`) is committed locally and Cowork-verified at source (isolated; the `beatTypeForOnsetTick`
> refactor confirmed a faithful, byte-identical extraction). Two **read-only** checks before any move to Increment C —
> nothing wired, no production change, no new commit required (the fair-key diagnostic stays local):
> **(1)** re-run the build+test to confirm B's gate on the **current** tree (the recorded numbers are relayed from the
> prior session, not re-run); **(2)** the **fair-key re-measurement** — feed B the real Layer-3 per-slice key — to test
> whether the −15.4 residual is the **key handicap** (the report's attribution) or a real per-slice limitation.

## §1 — Fresh build+test (re-confirm B's gate on the CURRENT tree)
- Build the current tree (HEAD `5f6b9828a5`).
- Run `composing_tests` + `notation_tests` (incl. `pipeline_snapshot_tests`). Confirm, with **freshly re-run** numbers
  (not relayed):
  - `composing` **617/617**;
  - pipeline snapshots **11/11, NO golden refresh** (the byte-identity proof — the wired L3 path's output must not move);
  - `notation` **52/57** — the **same 5** held-WIP failures, **no new failure**. **A new notation failure → STOP** (something
    drifted in the held WIP or leaked into production).
- Report the actual re-run numbers.

## §2 — The fair-key re-measurement (test the −15.4 attribution)
The isolated B grades with the **single notated key signature** for the whole piece; the per-region baseline has the
**wired L3 decoder's** key. To test whether the residual is mostly that handicap:
- Add a **decode-only** mode (e.g. `--decode-chords-l3key`) that, per slice, runs the **L3 decoder**
  (`keymodesequence::decode` — the same per-slice key the wired decoder produces) and feeds **each slice's L3 key/mode**
  to the chord decoder, in place of the single notated key. It runs under the diagnostic (returns before
  `analyzeScore`) — **production byte-identical, no wiring.** This simulates exactly what the wiring increment's
  key feed-forward would deliver.
- Re-grade chord-root (dur-weighted, held-out TEST, both presets), reusing the existing grader (**one grading path**).
- Report the comparison:

  | chord-root, dur-wt (TEST) | Baroque | Jazz |
  |---|---|---|
  | per-region baseline | 73.8 | 73.7 |
  | B — single notated key (current) | 58.4 | 58.3 |
  | **B — real L3 per-slice key (this test)** | **?** | **?** |

- Break it down: how much of the −15.4 closes with the real key, and what residual remains (the symmetric/relative
  root confusions the Increment-C spelling-pin targets)?

## §3 — The verdict (the decision input for Increment C)
State plainly:
- **If B-with-L3-key climbs toward ~70%** (closes most of the gap): the attribution holds, the per-slice thesis is
  validated, and the remaining residual is the Increment-C spelling-pin → proceed to C.
- **If B-with-L3-key barely moves from 58.4**: the key handicap is **not** the explanation → the attribution is wrong
  → **STOP and surface for investigation** before any C / wiring spend.
Report the evidence; Cowork + user decide whether C proceeds.

## §4 — Constraints
- **Read-only / decode-only.** Production byte-identical (the L3-key feed runs only under the diagnostic; the live
  per-region path untouched). One grading path. **No wiring.**
- The fair-key diagnostic may stay **local (uncommitted)**, like the tpc measurement — deliver the report; commit only
  if/when we proceed (your call; local is fine). Held WIP stays unstaged.
- `upstream` untouched.

## §5 — Deliverable
`cc_layer4_build_b_fairkey_report.md` (held/gitignored): the §1 fresh build+test numbers, the §2 fair-key comparison
table + breakdown, and the §3 verdict.

## §6 — Stop conditions
- A new `notation` failure beyond the known 5, or any production output moves → STOP.
- The L3-key feed touches the live analysis path (not decode-only) → STOP.
- A push would target `upstream` → STOP.
