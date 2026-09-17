# CC Instruction — Phase 5c Step 3: the resolver + the fine-grain override (L5 §5.5 + §8, dormant)

> **Plan: `cowork_phase5c_l5_build_plan.md` Step 3. Spec: `cowork_layer5_function_design.md` §5.5 + §8 + the §5.0 shared
> defs (the contract — implement its mechanism, do not re-spec).** Step 2 complete. Build the **resolver** (L5's O1 core:
> select among Layer 4's carried readings for each abstained slice) **and** the **fine-grain override** (the §8 case-4
> channel), building the **shared confidence-weighted-forward-recompute mechanism** (§8) that **Step 4 reuses**. Dormant,
> **byte-identical**. **Default constants (firewall) — no tuning. Select, never re-derive. Proportionality: the measured
> function-only residual is small (chiefly share-tone + relative-pair) — build the per-kind rules right and stop.**
> *(Reminder: the never-bash rule is Cowork's.)*

## §0 — Preamble (sweep + STATUS)
Commit local-only the unstaged Cowork docs (the §5.2 key-agnostic-limit correction, the §5.5 symmetric-rotation rule, the
§5.0 syncs): `docs(cowork): Phase-5c Step-2 resolution + Step-3 prep`. **Also add a STATUS.md session entry** recording the
L5 build progress (Steps 0–2 complete: progression model + base RN + key-agnostic cadence detector, all **dormant /
byte-identical**) — the living doc currently lacks it. Report the shas.

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read-only, confirm and report:
- **The carried-reading contract per ambiguity kind:** for an abstained `SliceChord`, the `OpenQuestionLabel`
  (`readingA`/`readingB`), the ranked `alternatives`, the `AmbiguityKind` (all six: transition, share-tone, relative-pair,
  close, insufficient, **symmetric-rotation**), and `SliceConfidence` — all reachable.
- **The resolver's evidence:** the **progression model** (Step 1 `functionprogression`), the **cadence tonic-vote** (Step 2
  `functioncadence`), the **soft bass-scale-degree prior** (§5.7), and the **neighbouring committed harmony** (the adjacent
  committed slices in the region) — all consumable.
- **The §8 override mechanism's needs:** confirm the inputs for the **confidence-weighted threshold** (the earlier layer's
  `SliceConfidence`) and that a **one-pass closure flag** + a **localized forward recompute** can be expressed over the
  region without a back-edge. Report.
If a kind's evidence is unreachable, or the §8 mechanism needs structure beyond a dormant unit → **STOP and report.**

## §2 — BUILD the resolver (§5.5), dormant
For each Layer-4-abstained slice, **select among the carried readings** by the named kind — never re-derive, never invent:
- **transition** → by the progression: does the slice reduce to a passing/neighbour figure within the prevailing harmony,
  or belong to the arriving function? Select the reading consistent with the licensed continuation.
- **share-tone** → select the reading that **participates in a licensed progression (§5.0)** into the established next
  function.
- **relative-pair** → the **cadence tonic-vote (§5.2)** + the **same-collection tonal-centre cues** (cadential arrival /
  raised leading tone / phrase-final emphasis).
- **close** → **functional plausibility** (the §5.5 fixed-feature score: licensed-out-of-prevailing + into-next + cadential
  fit) with the **bass-degree prior** as tie-breaker.
- **insufficient** → the same functional-plausibility score; where it does not separate, **carry the open mark (§7)**.
- **symmetric-rotation** → select the rotation that **resolves as a licensed leading-tone/applied chord to its target**
  (the resolution context names the root), or that the cadence pins; else **carry the open mark** (the §5.5 / F1 rule).
- **Residual:** where the function evidence decides nothing, **carry the honest open mark** — do not guess.

## §3 — BUILD the §8 override mechanism + the fine-grain override (case-4 #2), dormant
- **The shared mechanism (§8):** a confident earlier inference is overturned **only when** the contradicting later evidence
  **crosses a threshold scaled to the earlier layer's confidence**; the overturned decision is **marked final for the pass**
  (a one-pass closure flag), and a **localized forward recompute** re-reads the affected region — never a back-edge, never
  a loop. **Build this as the reusable mechanism** (Step 4's modulation recompute is its other instance).
- **The fine-grain override (§5.5 case-4 / §10):** when Layer 4 **confidently committed** a fine-grain reading the
  established function/cadence contradicts (the class-(b) override duty), **override** it by **selecting** the corrected
  reading from the **carried alternatives or the neighbouring committed harmony** (never re-deriving), firing per the §8
  threshold.

## §4 — Constants
- The §8 **override threshold** and the §5.5 **functional-plausibility weights / deciding margin** stay at the spec's
  stated **defaults** — **no tuning** (firewall; Phase B).

## §5 — Tests (oracle-asserted)
- One per ambiguity kind: a share-tone resolved by the licensed progression; a relative-pair by the tonic-vote; a
  symmetric-rotation by the resolution context; a transition by the continuation; a genuinely-undecidable slice → **open
  mark** (not a guess).
- The **fine-grain override**: a confident-but-contextually-wrong fine-grain commit is overridden by selecting the
  corrected carried/neighbour reading; the **§8 closure** holds (the overturned decision is not re-opened in the pass — no
  recursion).

## §6 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh (no production consumer). Movement → STOP.

## §7 — Deliver
Commit **locally (unpushed)**: the resolver + the §8 mechanism + the fine-grain override + the §5 tests. Write
`cc_phase5c_step3_report.md` (gitignored): the §1 confirm, the §2/§3 build (incl. any build-detail decisions declared for
Cowork), the §5 tests, the §6 gate, and the shas — so Cowork verifies the resolver only **selects** (never re-derives) and
the §8 mechanism is reusable + closure-safe.

## §7b — Note for Cowork
Declare any build-detail decisions (as in Steps 1–2) for ratification rather than assuming — especially anything where
§5.5 / §8 is ambiguous against the as-built carried-reading contract.

## §8 — Stops
- A resolver kind would require **re-deriving** a reading (not selecting), or the §8 mechanism needs a back-edge / structure
  beyond a dormant unit → STOP, report.
- Any production movement, any threshold **tuning** → STOP. `upstream` → STOP.
