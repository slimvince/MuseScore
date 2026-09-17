# CC Instruction — Phase 5c: Step-5 V7/IV fix + Step 6 output assembly (L5 §7, dormant)

> **Two tasks, both dormant + byte-identical.** **(A)** A small Step-5 correction: the unified relational-label emitter
> must emit `V7/IV` (matching production), per the corrected §5.6. **(B)** Step 6 — assemble the L5 output (§7). Plan:
> `cowork_phase5c_l5_build_plan.md` Step 6. Spec: `cowork_layer5_function_design.md` §5.6 (corrected) + §7 + §9-D1.
> **Default constants (firewall). Reuse, do not duplicate. Proportionality.** *(Reminder: the never-bash rule is Cowork's.)*

## §0 — Preamble (sweep)
Commit local-only the unstaged Cowork docs (the §5.3 Step-4 note + the §5.6 applied-trigger correction):
`docs(cowork): Phase-5c Step-5 ratification + §5.6 applied-trigger fix`. Report the sha.

---
## PART A — Step-5 correction: emit `V7/IV` (the applied-trigger fix)

> **Why.** Cowork ruling on your declared divergence: `V7/IV` **is** a genuine applied dominant; its chromaticism is the
> **♭7̂** (the target IV's leading tone — the third degree — is *diatonic*), so the raised-leading-tone-only trigger + the
> inherited chromatic-LT guard wrongly **drop** it, while the production `formatRomanNumeral` correctly **emits** it. A
> dormant emitter that drops `V7/IV` would **regress at engagement** and **mis-measure at Step M**. §5.6 is corrected.

### A1 — The change (in `function/functionrelationallabel.{h,cpp}` / the unified applied path)
- **Broaden the applied trigger** to recognise **a chromatic dominant-function chord of a non-tonic diatonic degree** — the
  chromaticism being a raised secondary leading tone **or** a **♭7̂** (the `V7/IV` case). So `V7/IV` is emitted, matching
  the production `formatRomanNumeral` behaviour.
- **Keep the false-positive guard for a *genuinely diatonic* chord** (no chromaticism at all → not applied). Do not widen
  it to admit non-chromatic chords.
- Reuse the production emission (`formatRomanNumeral`'s inline applied path already emits `V7/IV`) — **do not fork it.**

### A2 — Tests + gate
- `V7/IV` (a ♭7̂-chromatic dominant resolving to IV) **is** emitted as the applied label; a genuinely diatonic IV is **not**
  mislabeled applied; the existing `V/V` etc. still emit.
- **Dormant + byte-identical:** corpus 53/24/53, suites + snapshots green, no golden refresh (production paths untouched).
  Movement → STOP. If broadening the trigger causes any false positive you cannot guard cleanly → STOP and report (do not
  proceed to Part B).

---
## PART B — Step 6: output assembly (§7), dormant

### B1 — INVESTIGATE-confirm (read-only)
Confirm the per-unit outputs of Steps 1–5 are assemblable into the §7 contract: the **base Roman numeral** (Step 1) +
**relational label** (Step 5); the **function confidence** (from the §5.2 cadence-vote weight / the §5.0 licensed-
progression fit / the margin to the next-best reading — §7); the **open mark** (Step 3 resolver, on the genuinely
undecided); the per-region **cadence + key markers** (Steps 2/4). Report.

### B2 — BUILD the L5 output assembly (§7), dormant
- Assemble, per analysis unit: the **Roman numeral at full DCML/RomanText completeness, no simplification** (§3 Produces) +
  the **function confidence** (its components: cadence-vote weight / licensed-progression fit / margin — combination
  weights precision-phase, the components fixed) + the **open mark** where unresolved; and per region the **local key
  (possibly modulated) + the cadence markers**. The structure is **additive over the Layer-4 result** (annotates +
  resolves; does not replace the committed chord identity).
- The **L5→L6 contract** is this output (the Roman numeral + cadence/key markers + any open mark).
- **The T/S/D derived read-out is NOT built** (deferred, §9-D1).

### B3 — Constants
- The **function-confidence combination weights** stay at default (firewall); the components are fixed. No tuning.

### B4 — Tests (oracle-asserted)
- A resolved unit carries the full Roman numeral + a function confidence; an undecided unit carries the **open mark**; a
  region carries its local key + cadence markers; the output is **additive** over the L4 result (the committed identity is
  not replaced).

### B5 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, suites + snapshots green, no golden refresh (no production
  consumer). Movement → STOP.

## §7 — Deliver
Commit **locally (unpushed)**, Part A and Part B as separate commits. Write `cc_phase5c_step6_report.md` (gitignored): the
A1 fix + its test/gate, the B1 confirm, the B2 assembly, the B4 tests, the B5 gate, any declared decisions, and the shas —
so Cowork verifies `V7/IV` now emits, the output is additive over L4, and the T/S/D read-out is correctly absent.
**Steps 0–6 then complete → next is Step M (the read-only measure + engage GO/NO-GO).**

## §8 — Stops
- Part A's broadened trigger causes an unguardable false positive → STOP (do not proceed to B). The output assembly would
  **replace** rather than annotate the L4 identity, or needs a structural change beyond a dormant unit → STOP.
- Any production movement, any threshold **tuning**, building the T/S/D read-out → STOP. `upstream` → STOP.
