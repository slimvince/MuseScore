# CC Instruction — Phase 5c Step-5 follow-up: generalize the applied trigger (L5 §5.6, dormant)

> **One small task, dormant + byte-identical.** Cowork ruling on your declared **A-D2** (`viio/IV` divergence): admit
> applied **leading-tone** chords as a class — but by **generalizing the chromaticism test**, not by bolting on `viio/IV`
> as another special case. Spec: `cowork_layer5_function_design.md` §5.6 (amended 2026-06-29). **Default constants
> (firewall). Reuse, do not duplicate. Proportionality: generalize the one test, stop.** *(Reminder: the never-bash rule
> is Cowork's. All amendments land in the proper layer — this is L5 §5.6 algorithmic completion, not inference tuning.)*

## §0 — The ruling (why)
`viio/IV` is a genuine applied leading-tone chord. §5.6 **already** lists "a leading-tone chord" as an in-scope chord
type; the gap is that the *chromaticism* clause enumerated only two **dominant**-flavoured forms (raised secondary LT;
♭7̂), so `viio/IV` — whose foreign tone is the secondary diminished's own chromatic tone, not either of those — did not
trigger. The fix is to **generalize the chromaticism clause to the universal test it always implied** (≥1 tone foreign to
the home-key collection), with the two prior forms as *named instances*, not the closed set. This is the general
principle, so we stop discovering applied cases one at a time.

## §1 — The change (in the unified applied path, `function/functionrelationallabel.{h,cpp}`)
- **Generalize the trigger's chromaticism test** to: *a dominant- or leading-tone-function chord of a non-tonic diatonic
  degree that contains **at least one tone foreign to the home-key collection***. The raised secondary LT (`V/V`), the ♭7̂
  (`V7/IV`), and the secondary-diminished's foreign tone (`viio/IV`, `viio7/ii`) are then all instances of the one test.
- **Keep the chromatic-only false-positive guard** — exactly as the corrected §5.6 states: a chord **fully diatonic** to
  the home key is **not** applied (the natural-minor `bVII7→III`, all-diatonic, stays the diatonic numeral, **not**
  `V7/III`). Do **not** delegate the production inline path's *unguarded* trigger wholesale — the guard is the point.
- **Reuse** the production `formatRomanNumeral` inline emission for the label string (it already emits `viio/x`) — **add no
  second formatter.** You are broadening *which chords reach* the emitter, gated by the chromatic test; not re-implementing
  the emission.

## §2 — Do NOT reconcile the legacy divergence now (it is a Step-M / Phase-5d measurement)
The production inline path emits applied labels **without** the chromatic guard, so the unified (guarded) emitter will
**diverge** from it on the genuinely-diatonic case (production over-emits `V7/III`; the guard correctly rejects it). That
divergence is an *improvement*, but its correctness is **measured at engage against the DCML ground truth**, not decided
now. **Record** the divergence (which chords the guard rejects that the inline path would emit) in the report for Step M;
do **not** change the production path. (§5.6 final bullet.)

## §3 — Constants
- The trigger is a deterministic structural test — **no constants to tune** (firewall). If admitting the class needs a
  threshold, STOP and report — it should not.

## §4 — Tests (oracle-asserted)
- `viio/IV` (and a `viio7/x`) **is** emitted as the applied label via the generalized trigger; `V/V` and `V7/IV` still
  emit (no regression of the prior instances); a **genuinely diatonic** chord (the natural-minor `bVII7→III`) is **not**
  mislabeled applied (the guard holds).

## §5 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh — the unified emitter has **no production consumer** (confirm the grep
  again), the production paths are untouched. Movement → STOP.

## §6 — Deliver
Commit **locally (unpushed)**: the generalized trigger + the §4 tests, plus the §5.6 doc amendment in the same commit
(the sync rule). Append to `cc_phase5c_step6_report.md` (gitignored) or a short `cc_phase5c_step5_followup_report.md`: the
§1 change, the §4 tests, the §5 gate, the §2 recorded divergence (the rejected-diatonic cases, for Step M), and the sha —
so Cowork verifies `viio/IV` now emits, the guard still rejects the diatonic case, and production is byte-identical.

**Then Steps 0–6 + the A-D2 follow-up are complete → Step M (the read-only measure + engage GO/NO-GO).**

## §7 — Stops
- The generalized trigger causes a false positive you cannot guard with the chromatic test → STOP, report (do not widen
  the guard to admit non-chromatic chords). Reconciling/retiring the production inline path now (that is Phase 5d) → STOP.
  Any production movement, any threshold **tuning**, building the T/S/D read-out → STOP. `upstream` → STOP.
