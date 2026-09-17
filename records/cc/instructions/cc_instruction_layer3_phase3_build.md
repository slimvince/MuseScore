# CC Instruction — Architectural Layer 3, Phase 3: reach-back as a tested capability (production untouched)

> **Context.** Phase 3 per the **corrected** design `cowork_layer3_reachback_design.md` (read §0 — the production
> orchestrator decodes **whole-score on every path**, so reach-back is built as a **selection-aware capability** and
> **production `analyzeRegions` is left untouched**; the engagement that would switch production to selection-scoped is
> a **deferred** behaviour-change step, **not** this). This is **algorithmic completion of the bounded-context model**,
> **byte-identical on every gate** (the capability is not on the production path). **No inference-problem-fixing**
> (the discipline: refactoring/architecture/algorithmic-completion before any precision work).
>
> **Grounded facts (verified at source — §7 of the design / `cc_layer3_reachback_verify_report.md`):** orchestrator
> `analyzeRegions` (`regionanalyzer.cpp:488`): L1 build `:512`, L2 slice `:553`, L3 decode `:554-557`. The decoder is
> **key-only** — `keymodeseq::KeyModeSequenceDecoder::decode(slices, model, …)`, pure/`static`
> (`keymodesequence.h:192-199`). `SliceKeyMode.uncertain`/`confidence` (`:140-146`) is the leading-edge signal.
> `extend(Direction::Earlier, ticks)` + `boundaryReached()` are as Phase 1a built them. A separate `ChordPathDecoder`
> exists — **do not** use it.

## §0 — Preamble: protect the uncommitted Cowork docs
Commit, local-only, the uncommitted Cowork doc edits (the plan re-sequencing in `cowork_l1l3_stabilization_plan.md` and
the corrected/new `cowork_layer3_reachback_design.md`): `docs(cowork): two-phase plan re-sequence (tpc capability
early; tune-precision last) + Phase-3 reach-back design (selection-aware capability, production untouched)`. Confirm
`git show --stat` lists only those.

## §1 — Build the selection-aware reach-back capability — production `analyzeRegions` UNTOUCHED
Build a **selection-aware orchestration path** that does: `build(score, selStart, selEnd)` → `changePointSlices` →
`KeyModeSequenceDecoder::decode` → the reach-back loop (§2) → the **output-filter** (§2 step 7). **Do NOT change the
production path:** `regionanalyzer.cpp:512` stays `build(score)` (whole-score). Pick the form that **does not duplicate
the orchestration** (unification): a **parameter on `analyzeRegions`** defaulting to whole-score (so the production
call is byte-identical) **or** a thin sibling that *reuses* the same build/slice/decode calls — your call, reported in
the ledger. The loop lives **here**, never inside `decode()` (which stays pure).

## §2 — The reach-back loop (per design §2/§3)
- **Trigger:** the selection's leading in-selection slice(s) carry `uncertain == true` (or low `confidence`) — the
  opening had no earlier context. (Find the leading-edge slice from `selectionStart` reusing the existing
  region→slice `upper_bound` lookup, `regionanalyzer.cpp:561-580`.)
- **Extend:** `model.extend(NoteModel::Direction::Earlier, ticks)` where `ticks` = **one measure**, converted via the
  score's time signature (`model.score()`); ticks at the L1 boundary.
- **Re-slice** (`changePointSlices`) and **re-decode** (`decode`) the enlarged sequence — a **fresh** decode (interim;
  the incremental `redecodeRange` path is **deferred**, do not build it).
- **Convergence stop:** stop when the leading-edge key stops changing — use the proxy *"a settled, stable prevailing
  key (`uncertain==false`) is in view in the reached-back region."* Else stop at the **hard bound** (a max-measures
  setting) or the **score start** (`boundaryReached()`). Never guess an amount; the increment is an efficiency knob.
- **Output-filter (new work):** emit results **only for the selection** — drop the context-span slices/regions in
  `[loadedStart, selectionStart)`. (The L2 design assigns this to the consumer; it does not exist yet — build it here.)

## §3 — Tests (partial-selection fixtures — the only place this is exercised)
- **Reach-back fires + terminates:** a partial selection with an unsettled opening extends, anchors the leading-edge
  key from the carried-in context, and stops (convergence / hard bound / score start).
- **Convergence == determinism:** the in-selection result is **independent of the increment size** (same converged
  span reached in one big step vs several small ones → identical result). This also validates the §2 proxy.
- **Selection at the score start:** opening = score start → `extend` reports the boundary, the loop exits gracefully
  (no error), L3 proceeds with what exists.
- **Output = selection only:** context-span regions are not emitted.

## §4 — Gate (production byte-identical is the hard gate)
- **Corpus + `composing_tests` + `notation_tests` + `pipeline_snapshot_tests` ALL unchanged** — production
  `analyzeRegions` is untouched, so nothing on the live path moves. **Any movement → STOP** (something leaked onto the
  production path).
- New partial-selection tests pass; determinism holds.

## §5 — Doc staleness (correct while here)
Correct the `keymodesequence.h` ISOLATION block (`:74-78`) that still says the decoder is "NOT wired into the live
pipeline / production byte-identical" — it **is** wired (`regionanalyzer.cpp:555`; the same header's `:186` note;
CLAUDE.md's ratified L3-wiring delta). Make it as-built-accurate.

## §6 — Scope, unification, stops
- **Production stays whole-score.** Do **NOT** switch `:512` to the selection build, and do **NOT** drop production
  regions — that is the **deferred engagement** (needs the `notationharmonicrhythmbridge.cpp:131` range check + a
  ratified snapshot/notation delta), not Phase 3.
- **No duplicate orchestration**, **no second slicer/decoder**, **no incremental re-decode** (Phase-3b). End the report
  with the reuse-vs-new ledger and *"No new parallel path or logic duplication was introduced."*
- `upstream` never; `origin` held; local commit only.

## §7 — Deliver
Commit locally (unpushed): the capability + the new tests + the §5 doc fix (the §0 docs already committed). Write
`cc_layer3_phase3_report.md` (gitignored): the capability as built (which form, the reuse ledger), the §3 test results,
the production byte-identity proof, and confirmation the engagement was **not** done.

## §8 — Stop conditions
- Any corpus/suite/snapshot movement → STOP (production perturbed — a leak).
- You switch `:512` to selection-build, drop production regions, or otherwise change production output → STOP (deferred
  engagement).
- A duplicate orchestration / second decoder / incremental re-decode appears → STOP.
- A push targets `upstream` → STOP.
