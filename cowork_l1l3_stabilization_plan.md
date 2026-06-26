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

## Ordering principle — build-it-right BEFORE tune-precision (user-ratified 2026-06-25)
Two phases, strictly in order:
- **Build-it-right** — refactoring + architectural design + algorithmic completion, building each layer to use **all
  available evidence** (the **maximal-information** principle — *including the notated spelling / tpc capability*). This
  plan's Phases 1–4, then the L4/L5/L6 algorithmic builds. **No reactive precision-chasing here.**
- **Tune-precision (Phase B — LAST, after the whole L1–L6 stack is built)** — the reactive *"actively understand why
  inference isn't as good as we hoped"* work: the measured key-quality levers (scale-membership), the leading-tone
  de-brittling, the L3 tpc-weight calibration. **No inference-problem-fixing happens until all refactoring,
  architectural design, and algorithmic completion is done.**

Within build-it-right, strict bottom-up: the **bounded-context foundation** (Phases 1–3) first; then the **tpc spelling
capability** (Phase 4 — a *maximal-information foundation*, built early so L4 is spelling-aware from the start; **this
is capability, not precision tuning**). The foundation phases (1–3) are **byte-identical on the corpus** (degenerate
"selection = score", no extension fires); the tpc capability (4) is built with its term safely defaulted so it stays
**BIR-flat** — its precision *realisation* is a Phase-B tuning item. **No phase here is allowed to chase the key
numbers.**

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

## Phase 4 — the tpc spelling **capability** (the maximal-information foundation; build-it-right, BIR-flat)
Build the **one shared spelling-derived view** (Architectural Layer 1 already carries the notated tpc) — used by
Architectural Layer 3 (key) **and** Architectural Layer 4 (chord) — so the algorithm uses **all** the evidence the
score provides, never spelling-blind. **This is capability, not precision tuning:**
- **The shared spelling view + Architectural Layer 4's deterministic spelling-pin** (the symmetric-root pin: the
  notated spelling *names* the root — no degradation) are the capability. Build them here, **before L4**, so L4 is
  spelling-aware from the start and never retrofitted. Unification: **one** spelling view, used by both layers, never
  duplicated.
- **The L3 key emission reads tpc-aware evidence**, but with its term **safely defaulted / gated** so the build is
  **BIR-flat** — the *weight* that realises the precision gain (and that costs stable regions without Layer-5 function
  gating) is a **Phase-B tuning item**, not turned on here.
- **Gate:** BIR-flat on both presets (the capability lands without moving the numbers); both suites green. A small
  read-only design precedes the build.

## Phase 5 — re-verify, sync specs to as-built, sign off L1–L3 (build-it-right complete for L1–L3)
- Re-run the spec↔implementation delta-check over L1–L3 — zero DIVERGENCE, operations present, predicates qualified.
- **Sync the L1–L3 specs to as-built:** the bounded-context contract (built), reach-back, the tpc capability; move
  build state to the delivery notes, keep the architecture prose code-free.
- Confirm the standing net: both suites pass, **BIR gate byte-flat** through Phases 1–4, snapshots untouched.
- **Then L4 is cleared to build** — on a stable, correctly-bounded, spelling-aware L1–L3.

---

## Phase B — tune-precision (DEFERRED to LAST; only after the full L1–L6 algorithmic build)
**Not done in this plan.** The reactive *"why isn't inference as good as we hoped"* work runs **only after**
refactoring + architectural design + algorithmic completion (L4/L5/L6) are done — per the ordering principle. Recorded
here so the items are not lost:
- **B1 — scale-membership scorer lever** (measured ~+57…+73 / +38…+68 decode-only; apply + calibrate the production
  magnitude; two-tier BIR gate).
- **B2 — leading-tone presence-gate de-brittling** (the diagnosed non-Bach C→F key regression; weight-scale the char/lt
  `>0.1` gate; gate = the three xfail'd notation tests flip to C + BIR holds; diagnosis: L3 §11 +
  `cc_keyregression_diagnosis_report.md`).
- **B3 — L3 tpc-weight calibration** (turn up the Phase-4 spelling term once Layer-5 function can gate the
  tonicization-vs-modulation cost — the precision *realisation* of the capability).
- **B4 — remaining L3 follow-ups**: Step-2 scaleMembership reweight, P4 tick-local path, S1 seed-retire, sequence-margin
  confidence redesign, "uncertain"-recall raise. Each measured/gated; take only net-positive.

---

## Dependency summary
```
Phase 0 (baseline)
   └─> Phase 1  L1 build-selection + extend   [byte-identical corpus]   ──(1b index: deferrable)
          └─> Phase 2  L2 re-slice on extend  [byte-identical corpus]   ✓ DONE
                 └─> Phase 3  L3 reach-back    [byte-identical corpus + partial-selection tests]
                        └─> Phase 4  tpc spelling CAPABILITY  [BIR-flat; term defaulted]
                               └─> Phase 5  re-verify + spec sync + sign-off  ─> L4 cleared
                                      └─> … L4/L5/L6 algorithmic build …
                                             └─> Phase B  tune-precision (scale lever, de-brittling, tpc-weight) — LAST
```

## Notes
- **Each phase is its own gated Claude-Code instruction**, written when we reach it; the non-trivial ones (Phase 1
  especially) get a **read-only design** first.
- **Phases 1–3 should not move a single corpus number.** If they do, the degenerate-case byte-identity is broken —
  STOP and investigate, do not refresh snapshots to "fix" it.
- **No phase in this plan moves the key numbers** — Phases 1–3 are byte-identical, and Phase 4 lands the tpc
  capability BIR-flat (term defaulted). The numbers move only in **Phase B (tune-precision), which is deferred to last**
  (after the L4/L5/L6 build), under the two-tier BIR gate.
- **`upstream` untouched throughout** (fork-local; the cfc7eb5e39 distribution constraint stands); push to `origin`
  only, when each gated step is ratified.
- The L4 build backlog (`cowork_delta_check_dispositions.md`) is **not** part of this plan — it runs after Phase 5.
