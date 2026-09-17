# CC Instruction — Phase 5c Step 2 AMENDMENT: relax the authentic-cadence gate (plain V→I is authentic)

> **Why.** Cowork evaluation of your Step-2 build decision (b): the **genuine-dominant (seventh/tritone) test must be a
> vote *strengthener*, not a family gate**. A *plain* triad V→I with the leading-tone resolution **is** an authentic
> cadence (Caplin's V(7)→I — the seventh is parenthetical), and it is the **common Bach-chorale phrase-end** — excluding
> it would make the detector miss most chorale cadences and break the chorale validation. Your stated rationale (the 7th
> is "the I→IV discriminator") is the issue: **the leading-tone *resolution* event already discriminates I→IV** (the
> leading tone is the third of V, not present in I), so the 7th/tritone is a redundant gate that only costs real cadences.
> The signed spec is corrected (`cowork_layer5_function_design.md` §5.2, 2026-06-26). Dormant + byte-identical — same gate.
> *(Reminder: the never-bash rule is Cowork's.)*

## §1 — The change (in `function/functioncadence.{h,cpp}`)
- **The authentic-family gate becomes:** a **dominant-function approach** — a chord on scale-degree five, **or** a
  leading-tone chord (seventh-degree diminished triad/seventh) standing in for it — **resolving to the tonic**, **with the
  leading-tone-resolution event** across the boundary. **Drop `genuineDominant` (the seventh/tritone) as a *requirement*
  for admission.**
- **Keep the seventh/tritone as the vote strengthener** it already is (the `+wSeventh` term) — a V7→I scores higher than a
  plain V→I, but both are authentic.
- **Perfect/imperfect unchanged** (bass five-to-one = perfect; the complement = imperfect — your decision (a), confirmed).
- **Confirm no I→IV regression:** the leading-tone-resolution gate already rejects I→IV (I carries no leading tone to
  resolve); a plain I→IV must still **not** be a cadence after the change. (The leading-tone chord `vii°→I` case stays
  admitted via the dominant-function approach + its own leading-tone resolution.)

## §2 — Tests (adjust/add)
- A **plain triad V→I** (no seventh) with the leading-tone resolution is now **authentic** (perfect if both root
  position) — add this case (it was previously excluded).
- A **V7→I** is authentic with a **higher vote** than the plain V→I (the seventh strengthener) — assert the ordering.
- A **plain I→IV** is **still NOT** a cadence (no leading-tone resolution) — the discriminator holds.
- The existing PAC/IAC-by-inversion, Phrygian, deceptive, six-four-collapse tests still pass unchanged.

## §3 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh (the unit has no production consumer). Movement → STOP.

## §4 — Deliver
Commit **locally (unpushed)**: the gate relaxation + the test adjustments. Append to `cc_phase5c_step2_report.md` (or a
short amendment note) the change + the I→IV-still-rejected confirmation + the commit sha.

## §5 — Stops
- The leading-tone-resolution gate does **not** by itself reject I→IV after dropping the seventh gate (a regression) →
  STOP and report (do not re-add the seventh gate; report so Cowork re-evaluates the discriminator).
- Any production movement, or threshold **tuning** (the vote weights stay at their default seeds) → STOP. `upstream` → STOP.
