# CC Instruction — Foundation Stage 3a: triage the 5 committed notation failures (READ-ONLY, at the score)

> **Context.** The last foundation issue: committed HEAD has **5 failing `notation_tests`** (composing 624/624 and
> pipeline snapshots 11/11 both pass). They predate the L4 work and were "last touched by the Stage-4b key commits" —
> so the likely story is a **ratified key-path change moved the output and the goldens/assertions were never updated**
> — but that is a hypothesis to **confirm per test, not assume.** This stage **determines the correct answer at the
> score for each failure and classifies it**; it **changes nothing** (no golden refresh, no code fix, no commit). The
> disposition is a separate, gated **Stage 3b** after Cowork + user review this report.
>
> **The governing rule (CLAUDE.md):** *a pinned snapshot is refreshed only after the change is confirmed correct.* So
> the whole point of 3a is the confirmation.

## §1 — The 5 failures (from the Stage-0 baseline)
| # | Test | Symptom | Likely layer |
|---|---|---|---|
| 1 | `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian` | key fifths **−1 vs 0** | L3 key/mode |
| 2 | `Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord` | chord **"G" vs "Gm"** | L4 chord / segmentation |
| 3 | `Notation_ImplodeTests.PopulateChordTrackEmitsCadenceMarkersOnCorelli` | cadence markers | cadence / function |
| 4 | `NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral` | **"V" vs "I"** | function (Roman numeral) |
| 5 | `NotationInteractionHarmonyPinning.BehaviorSnapshot_Nashville` | **"5" vs "1"** | function (Nashville) |

(#4 and #5 are very likely the *same* underlying harmony rendered two ways — confirm and treat as one root cause if so.)

## §2 — For EACH failure, determine and report
1. **What the test asserts** — the expected value, and whether it is a **behavior snapshot** (pins current output, refreshable) or a **musical-property assertion** (asserts a *desirable* property, e.g. "opening prefers C major" / "does not smear the previous chord"). This distinction matters: a snapshot that drifted is usually a refresh; a *property* that now fails is usually a **regression** (the analysis lost a property it should hold).
2. **The actual current output** at HEAD (the analyzer's reading + where it diverges).
3. **The correct answer, at the score** — examine the actual notes. Use the **ground-truth analysis if the piece is in a corpus** (Corelli Op.1 may be); otherwise reason from the score by music theory, the way the `bwv10.7@36000` spot-check was done. State the musically-correct key / chord / function and *why*.
4. **Classification** (one of):
   - **REFRESH** — the current output is **correct**; the golden/snapshot is merely stale (a ratified change moved it). Behavior-neutral to update.
   - **FIX** — the current output is **wrong** (a real regression); name the **layer** and the **cause**, and whether it is in a path we keep (L3 key) or one being rebuilt (old L4/L5 chord-function).
   - **ACCEPTED-UPDATE** — the output changed because of a **ratified** change and the test's *assertion* is now outdated; the assertion should be updated (with justification), not the code fixed.
   - **DEFER-TO-REBUILD** — the failure is in a path the layered rebuild will replace, so a fix now is moot; flag how 3b should keep the suite green meanwhile (refresh to current, or a tracked skip) — a judgement for Cowork + user.
   - cite the **test file:line** and the **score evidence**.

## §3 — Anchor (don't assume refresh)
The "ratified Stage-4b key change → stale goldens" hypothesis predicts **REFRESH**, but the two Implode *property*
assertions (#1 prefers-C-major, #2 do-not-smear) assert things the analysis is *supposed* to do — if those now fail,
that is a **lost property = regression**, not a drift. So **confirm correctness at the score** before calling any of
them REFRESH; do not refresh a property assertion just to make it green.

## §4 — Deliverable
`cc_stage3a_notation_triage_report.md` (gitignored): per-failure — the assertion (and snapshot-vs-property), the actual
output, the **score-verified correct answer** + evidence, the classification + rationale, and the layer/cause for any
FIX. A summary: how many REFRESH vs FIX vs ACCEPTED-UPDATE vs DEFER, and (if #4/#5 are one root cause) say so.

## §5 — Constraints & stop conditions
- **READ-ONLY.** No golden refresh, no `--update-goldens`, no code fix, no commit. The disposition is Stage 3b, gated
  on this report + Cowork's at-the-score verification + user ratification.
- Every "correct answer" call cites the **score** (notes / GT), not just the test's expectation.
- The stash `bc4fa79c4a…` stays intact; the working tree stays clean.
- `upstream` never; `origin` held.
- You start refreshing a golden or editing code → STOP (that is 3b).
