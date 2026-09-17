# CC Instruction — Phase 5c Step 4: tonicization vs modulation + the modulation recompute (L5 §5.3 + §5.4, dormant)

> **Plan: `cowork_phase5c_l5_build_plan.md` Step 4. Spec: `cowork_layer5_function_design.md` §5.3 + §5.4 + §8 (the
> contract — implement its mechanism, do not re-spec).** Step 3 complete (the §8 mechanism + resolver). Build §5.3
> (tonicization-vs-modulation) + §5.4 (the modulation recompute — the §8 case-4 instance #1, **reusing Step-3's
> `forwardoverride`**), **REUSING** the dormant key-axis primitives, and **HONOUR THE TWO STANDING PINS**. Dormant,
> **byte-identical**. **Default constants (firewall) — no tuning. Reuse, do not re-implement. Proportionality: build the
> mechanism right and stop.** *(Reminder: the never-bash rule is Cowork's.)*

## §0 — Preamble (sweep)
Commit local-only the unstaged Cowork docs (the §5.5 override-scope / Step-M note): `docs(cowork): Phase-5c Step-3
ratification + Step-4 prep`. Report the sha.

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read-only, confirm and report — **the reuse landscape is the heart of this step:**
- **`localmodulationdetector` (`detectLocalModulations`)** — the dormant **established + cadence-confirmed** local-key-span
  signal (verified Step-0 F2: "exactly the brief-vs-sustained signal that separates a real modulation from a passing
  tonicization"). Confirm it is consumable as the **§5.3 substrate**, and note where its **sustained-run gate** differs
  from §5.3's **change-cost/hysteresis** (the part to adapt).
- **`jointkeydecision` + the J-key-iii re-key path** (`applyJointKeyWiring`, gated off) — the **§5.4 recompute** substrate.
- **The L3 region key-alternatives carry** (`HarmonicRegion::keyAlternatives`/`keyConfidence`) — currently the **v1
  placeholder** (representative-slice alternatives), the **reduction pin** target.
- **The cadence tonic-vote** (Step 2 `functioncadence`) for the cadence-confirmation; **`forwardoverride`** (Step 3) for
  the recompute.
If a reuse target isn't consumable, or a pin can't be done byte-identically (see §6) → **STOP and report.**

## §2 — BUILD §5.3 (tonicization vs modulation), dormant — REUSE, do not re-implement
- **Reuse** `localmodulationdetector`'s cadence-confirmed-modulation substrate; build §5.3 on it: **default-tonicize**;
  the **cadence-confirmation gate** (an authentic/half cadence in the candidate key — the necessary condition);
  **persistence as a change-cost (hysteresis)** over the L3 local-key carry — **adapt** the existing sustained-run gate to
  the §5.3 hysteresis form (the cost falls with the candidate area's duration + accumulated cadential weight); the
  **break-even defaults to tonicization**.
- Consume the **notated-spelling key signal** here (function-gated, §5.3).

## §3 — BUILD §5.4 (the modulation recompute, §8 case-4 #1), dormant — REUSE `forwardoverride`
- On a **confirmed modulation**, fire the **localized, forward, convergence-bounded recompute** of the region **through
  Step-3's `forwardoverride`** (the one-pass closure + bounded forward sweep — no back-edge), reusing `jointkeydecision` +
  the J-key-iii re-key path. A cadence is the decisive later evidence overturning a confident key (§8 case 4).
- **★ THE TWO STANDING PINS — FIRST TASKS OF THIS STEP (spec §15-3):**
  1. **Pin the region key-alternatives reduction precisely.** Replace the L3 carry's **byte-identical v1** (representative-
     slice alternatives) with the **reduction this override actually selects among** (the candidate keys the modulation
     recompute chooses between). **Update the L3 carry + its lock-in test** to the pinned reduction.
  2. **Re-derive the carry in the J-key-iii re-key path.** The gated-off re-key overrides the chosen key **without**
     updating the carry today; make it **re-derive `keyAlternatives`/`keyConfidence`** alongside its override, so the
     carried menu cannot go stale against an overridden key.

## §4 — Constants
- The **change-cost/hysteresis magnitude**, the **cadence-confirmation threshold**, and the §8 **override threshold** stay
  at the spec's stated **defaults** — **no tuning** (firewall; Phase B).

## §5 — Tests (oracle-asserted)
- A **tonicization stays home** (a cadence-less lean → applied chord, home key holds); a **cadence-confirmed + persistent**
  candidate **modulates** and the recompute **re-reads the region** in the new key; the **break-even defaults to
  tonicization**; the **relative-pair** is decided by the tonic-vote; the **§8 closure** holds on the recompute (no
  re-open, no recursion). The **pinned reduction** lock-in test (the region carries the pinned ranked alternatives).

## §6 — Gate (read this — the pins are the byte-identity risk)
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, suites + snapshots green, no golden refresh.
- **Why the pins are still byte-identical:** the **region key-alternatives carry has no production consumer** (it exists
  for the dormant L5), so changing the v1 reduction to the pinned one is **byte-identical on production**; the **J-key-iii
  re-key is gated off** (default), so re-deriving the carry inside it is **byte-identical**. **Verify** both: confirm no
  production path reads `keyAlternatives`, and that `jointKeyWiringEnabled()` is still default-OFF. **If pinning the
  reduction moves any production output (53/24/53 or `.ours.json`) → STOP** (a consumer leaked).

## §7 — Deliver
Commit **locally (unpushed)**: §5.3 + §5.4 + the two pins + the §5 tests. Write `cc_phase5c_step4_report.md` (gitignored):
the §1 reuse confirm, the §2/§3 build (incl. the hysteresis adaptation + both pins), the §5 tests, the §6 gate (with the
byte-identity proof for the two pins), declared build-detail decisions, and the shas — so Cowork verifies the reuse (not a
re-implementation), the pins landed byte-identically, and the recompute is closure-safe.

## §8 — Stops
- A pin moves production output, or a reuse target isn't consumable, or the recompute needs a back-edge → STOP, report.
- Re-implementing `localmodulationdetector` instead of reusing it → STOP (reuse is the instruction). Any threshold
  **tuning** → STOP. Any production movement → STOP. `upstream` → STOP.
