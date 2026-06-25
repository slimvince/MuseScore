# L1–L3 stabilization plan — bring the lower layers to production shape before building Architectural Layer 4

> **Why this exists.** We will build Architectural Layer 4 **once, on a stable, correctly-bounded L1–L3** — not on the
> current code, which (a) bakes in the "whole score is always loaded, no layer ever asks for more" assumption the
> product does not have, and (b) still carries measured-but-unapplied key-inference improvements. Every lower-layer
> change ripples up; doing them after L4 sits on top means re-validating L4 too. So we stabilise L1–L3 first.
>
> **Discipline applied throughout:** knowledge-based (measure before building); investigate-by-default (a read-only
> design precedes each non-trivial step); total unification (one path per concern); byte-identity guards where a step
> must not move output; the two-tier BIR gate + both test suites + pinned snapshots as the standing safety net. Each
> step below becomes its **own** gated Claude-Code instruction when we reach it — this document is the **sequence and
> the gates**, not the build instructions.

## Ordering principle
Strict bottom-up. The **bounded-context foundation** (Phase 1–3) comes first, because it is the assumption everything
above inherits and the expensive thing to retrofit. The **L3 key-quality levers** (Phase 4) come after the foundation,
since they are L3-internal and ride on top of it. The foundation phases are **byte-identical on the corpus** (the
whole-score run is the degenerate "selection = score" case, where no extension fires) — so they move no metric and are
gated on byte-identity + new partial-selection behaviour tests. Only Phase 4 moves the key numbers, gated on BIR + the
key metric.

---

## Phase 0 — baseline & guards (no code change)
- Re-confirm, freshly run, the current BIR identity sets (Baroque 57 / Jazz 23 / Default 57) and the pinned snapshot
  state — the gate references every later phase is measured against.
- Establish the **byte-identity guard** for Phases 1–3: the whole-score corpus run must stay byte-identical through
  them (the degenerate case). Any corpus movement in Phases 1–3 is a STOP — it means the degenerate case is not
  byte-identical, i.e. a real bug.

## Phase 1 — Architectural Layer 1: build-over-selection + the *extend* operation (the foundation; the non-trivial piece)
*Read-only design first* (the index-under-extension is the genuinely hard part; design it before coding).
- **1a — the contract, with an interim rebuild.** Implement *build over a selection* + *extend(direction, stop,
  bound)* (append-only, clamp at the score boundary, report boundary-reached) per `cowork_bounded_context_design.md`.
  **Interim:** on extend, Architectural Layer 1 may **rebuild over the enlarged span** (correctness first) — the
  *contract* is what the layers above are written against, so the interim is invisible to them. **Gate:** the
  degenerate case (selection = score, never extended) is **byte-identical** → corpus byte-identical; plus new unit
  tests for extend (append-only, idempotent re-request, boundary clamp/report).
- **1b — incremental index (DEFERRED, byte-identical perf).** Replace the interim rebuild with an incremental/extending
  look-up index. **Gate:** byte-identical to 1a (a pure performance step) + the index ≡ linear-scan property over
  extended spans. *Deferrable past L4 — it changes no behaviour; the contract from 1a is what matters now.*

## Phase 2 — Architectural Layer 2: re-slice on extend
- Produce change-point slices for the **newly loaded region** on extend (additive — existing-region slices are a local
  fact and must not change), preserving complete coverage and slice identity over the enlarged span; mark
  context-span slices as evidence (not output). **Gate:** degenerate case byte-identical (corpus); the existing
  whole-corpus `--validate-slices` property holds over extended spans; existing-region slices proven unchanged by an
  extension.

## Phase 3 — Architectural Layer 3: reach-back as an extension request
- Wire reach-back to the Phase-1 *extend*: direction = earlier, stop = *"the prevailing key before the selection is in
  view,"* hard bound = a max reach, terminating at the score start. Output only for the selection; context slices
  anchor the carried-in key. **Gate:** the corpus (whole stems) **never fires reach-back** (a piece start has nothing
  earlier) → byte-identical; new **partial-selection behaviour tests** — reach-back fires and terminates, the
  leading-edge key is anchored by the carried-in context, a selection at the score start truncates cleanly; and the
  **equivalence invariant** — analysing a selection with extension equals a fresh run over the final loaded span.

*End of Phase 3: the bounded-context foundation is built, the assumption is correct, and the corpus is byte-identical.*

## Phase 4 — Architectural Layer 3 key-quality (the measured levers; these move the numbers, gated)
- **4a — the scale-membership scorer lever.** Apply the measured sharpening of the out-of-candidate-scale penalty to
  the shared per-window scorer (direction validated: ~+57…+73 Baroque / +38…+68 Jazz key-inference, decode-only). It
  is now applicable (the wiring it waited for has landed). **Gate:** **no BIR-false regression on either preset**
  (two-tier gate), pinned snapshots refreshed only if the change is confirmed correct, both test suites green; report
  the key-metric gain.
- **4b — tpc spelling plumbing (do not hold — user-ratified).** Build the **one shared spelling-derived view** (used
  by L3 now and L4 later — unification, never duplicated) and read tpc-aware evidence in the L3 emission. Handle the
  measured wrinkle — tpc as a standalone L3 term costs stable regions until function (Layer 5) can gate it — by
  **gating/calibrating** the term, not deferring the code; the plumbing lands now so it is never retrofitted, and the
  full precision gain realises when Layer 5 arrives. **Gate:** BIR no-regression + key metric + the byte-identity
  discipline where applicable.
- **4c — leading-tone presence-gate de-brittling (the diagnosed non-Bach key regression).** Weight-scale the
  characteristic-pitch / true-leading-tone terms instead of the brittle `>0.1` binary gate
  (`keymodeanalyzer.cpp:344,374`), so a weak-but-present leading tone (the Mozart B♮ at 0.093) is not treated as
  absent. **Gate:** the three xfail'd notation tests (`MozartK279…`, `HarmonyPinning RN`/`Nashville`) flip back to C,
  the two-tier **BIR gate holds on both presets**, the key metric does not regress, snapshots refreshed only if
  confirmed correct. Diagnosis (the scale lever is *not* the fix): L3 spec §11 + `cc_keyregression_diagnosis_report.md`.
  Needs a small read-only design (the right replacement for the binary gate) before the build. The principled
  spelling/function-aware leading tone is a later enhancement (folds in with 4b tpc / future L5), not required here.
- **4d — remaining deferred L3 follow-ups**, each measured/gated as warranted: the Step-2 scaleMembership reweight,
  the P4 tick-local path, the S1 seed-retire, the sequence-margin confidence redesign, and raising the "uncertain"
  recall (currently high-precision/low-recall). Take only the ones that measure net-positive under the gate; drop the
  rest.

## Phase 5 — re-verify, sync specs to as-built, sign off L1–L3
- Re-run the spec↔implementation delta-check (`cc_instruction_spec_impl_delta_L1L4.md`) over L1–L3 — confirm zero
  DIVERGENCE, the operations all present, predicates qualified from the now-built values.
- **Sync the L1–L3 specs to as-built:** the bounded-context contract (built, not "designed-but-unbuilt"), the scorer
  lever, the tpc plumbing, the resolved follow-ups; move build state to the delivery notes, keep the architecture
  prose code-free per the standard.
- Confirm the standing net: both test suites pass, BIR gate holds both presets, snapshots refreshed only on
  confirmed-correct changes.
- **Then L4 is cleared to build** — on a stable, correctly-bounded, production-quality L1–L3.

---

## Dependency summary
```
Phase 0 (baseline)
   └─> Phase 1  L1 build-selection + extend   [byte-identical corpus]   ──(1b index: deferrable)
          └─> Phase 2  L2 re-slice on extend  [byte-identical corpus]
                 └─> Phase 3  L3 reach-back    [byte-identical corpus + partial-selection tests]
                        └─> Phase 4  L3 key-quality (4a scorer → 4b tpc → 4c follow-ups)  [moves numbers, BIR-gated]
                               └─> Phase 5  re-verify + spec sync + sign-off  ─> L4 cleared
```

## Notes
- **Each phase is its own gated Claude-Code instruction**, written when we reach it; the non-trivial ones (Phase 1
  especially) get a **read-only design** first.
- **Phases 1–3 should not move a single corpus number.** If they do, the degenerate-case byte-identity is broken —
  STOP and investigate, do not refresh snapshots to "fix" it.
- **Phase 4 is the only place key numbers change**, and only under the BIR two-tier gate.
- **`upstream` untouched throughout** (fork-local; the cfc7eb5e39 distribution constraint stands); push to `origin`
  only, when each gated step is ratified.
- The L4 build backlog (`cowork_delta_check_dispositions.md`) is **not** part of this plan — it runs after Phase 5.
