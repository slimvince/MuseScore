# CC Instruction — Phase 5c Step 5: relational labels + unify the tonicization paths (L5 §5.6, dormant)

> **Plan: `cowork_phase5c_l5_build_plan.md` Step 5. Spec: `cowork_layer5_function_design.md` §5.6 (the contract —
> implement its mechanism, do not re-spec).** Steps 0–4 complete. Build the **relational labels** (applied/secondary,
> Neapolitan, augmented sixth, modal mixture) and **unify the two tonicization paths** into one **dormant** owned emitter.
> Most of this is **reuse** of the existing emission. Dormant, **byte-identical**. **Default constants (firewall) — the
> labels are deterministic triggers, almost no constants. Reuse, do not duplicate. Proportionality: build the emitter
> right and stop.** *(Reminder: the never-bash rule is Cowork's.)*

## §0 — Preamble (sweep)
Commit local-only the unstaged Cowork doc (the §5.3 Step-4 build note): `docs(cowork): Phase-5c Step-4 ratification`.
Report the sha.

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read-only, confirm and report — **this step is reuse-heavy:**
- **The existing emission** (`ChordSymbolFormatter::formatRomanNumeral`) already emits the **augmented-sixth** labels
  (It/Fr/Ger), **chromatic** numerals, and the **inline applied / secondary-dominant** labels — confirm these are
  reusable so the relational labels **wrap/extend** them, not re-implement.
- **The dormant `tonicizationlabeler`** (the applied-chord labeler with its **chromatic-leading-tone false-positive
  guard**) — confirm consumable as the basis of the unified applied/tonicization emitter; the guard is worth keeping.
- **`spellingview`** (the shared spelling interpreter / L4 spelling-pin primitive) — confirm consumable for the
  **Ger6↔V7** disambiguation (the one label that needs notated spelling).
- The **triggers**: a raised **secondary leading tone** (applied, target = the tonicized degree); a major triad on the
  **lowered second** in first inversion (Neapolitan, `bII6`); the **lowered-sixth/raised-fourth** augmented sixth + the
  degree selector (It/Fr/Ger); a borrowed/altered degree that is none of the above (mixture).
Report the reuse map + the unification plan. If a label can't reuse the existing emission (forcing a duplicate), or
spelling is unreachable for Ger6 → **STOP and report.**

## §2 — BUILD the relational labels (§5.6), dormant
- The four labels on their defining triggers, tested in the **fixed precedence — augmented sixth → Neapolitan →
  applied/secondary → modal mixture** (first match wins); **modal mixture is the residual** (a quality-altering borrowed
  degree matching none of the earlier labels).
- **Spelling-aware only where the distinction is a spelling distinction:** the **German sixth vs the dominant seventh** is
  separated by the notated spelling + its resolution (via `spellingview`) — the one place spelling is read.
- The **applied/secondary** label: target = the degree a semitone above the raised secondary leading tone, relative to the
  **local** key (the major-mode trap: the secondary LT of V is the diatonic seventh degree, not a raised one — read the
  spelling, not a presumed accidental).
- Reuse `formatRomanNumeral`'s aug6/applied/chromatic emission; **add no second formatter.**

## §3 — Unify the two tonicization paths (dormant emitter only; retirement is Phase 5d)
- Build **one owned emitter** that produces the applied/tonicization label, subsuming the dormant `tonicizationlabeler`
  (keep its chromatic-LT guard) and the inline `formatRomanNumeral` applied path — **dormant.**
- **Do NOT retire the two existing paths or switch production to the unified emitter** — that lands at the **joint engage
  (Phase 5d)** to stay byte-identical. Build the unified emitter; leave production on the existing paths.

## §4 — Constants
- The relational labels are deterministic triggers — **no constants to tune** (firewall). (If a label needs a threshold,
  STOP and report — it should not.)

## §5 — Tests (oracle-asserted)
- An applied chord emits `V/x` with the correct **target degree** (local key); a lowered-second first-inversion triad →
  `bII6`; an **It/Fr/Ger** is selected by the degree + (for Ger vs V7) the **spelling**; a borrowed quality-altering
  degree that matches none → **modal mixture** (the residual); an altered chord matching **multiple** triggers takes the
  **first** in the precedence.

## §6 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh — the unified emitter has **no production consumer**, and the
  existing `formatRomanNumeral` / `tonicizationlabeler` paths are **untouched** until Phase 5d. Movement → STOP.

## §7 — Deliver
Commit **locally (unpushed)**: the relational-label + unified-tonicization emitter (dormant) + the §5 tests. Write
`cc_phase5c_step5_report.md` (gitignored): the §1 reuse map, the §2/§3 build, the §5 tests, the §6 gate, any declared
build-detail decisions, and the sha — so Cowork verifies the labels reuse the one emitter and the unification is built
dormant (production paths untouched).

## §8 — Stops
- A label would need a second formatter, or spelling is unreachable for Ger6, or the unification can't be built without
  touching the live emission paths → STOP, report.
- Retiring/switching the production tonicization paths (that is Phase 5d) → STOP. Any production movement, any threshold
  **tuning** → STOP. `upstream` → STOP.
