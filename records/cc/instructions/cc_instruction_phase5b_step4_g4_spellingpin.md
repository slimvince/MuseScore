# CC Instruction — Phase 5b Step 4: G4 — the symmetric-root spelling-pin (Increment-C1, the LAST build increment)

> **Why.** Final build increment of the grounded `cowork_phase5b_l4_build_plan.md`. Step 0 found G4: the symmetric-root
> (dim7/aug) root is chosen **key-dependently** (`dim7CharacteristicBonus`); the Phase-4 `engravingbridge/spellingview`
> primitive exists but is **unconsumed**. Build the spec's **spelling-pin**: the **notated spelling deterministically
> names the symmetric root** (G♯dim7 vs A♭dim7 by spelling — no degradation), consuming `spellingview`'s per-note
> line-of-fifths. This is the clean **deterministic** tpc use — **build-it-right (algorithmic completion), NOT
> inference-tuning** (it reads the score's spelling, not a heuristic). Small (~3.1% per Step 0). **C1 (spelling-pin)
> ONLY — the new four-note dim7/mMaj7 types (C2/G5) are DEFERRED to the engage step (gated, so they don't move legacy
> output — Step-0 F-4).** Decoder production-dead → **byte-identical on production.** *(Reminder: the never-bash rule is
> Cowork's.)*

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read the spec's spelling-pin (G4) + the `spellingview` primitive + the as-built symmetric-root selection
(`dim7CharacteristicBonus`) in `chordslicedecoder`. Confirm and report:
- The **spelling-pin** consumes `spellingview` (per-note `lineOfFifths` / spelling) to **deterministically** pick the
  symmetric root from the **notated spelling** of the slice's notes — confirm the slice's `tpc` spellings reach the
  decoder (they should, via L1) so the pin is real, not a fallback.
- **Where it plugs in:** for symmetric (pitch-class-ambiguous) roots only — dim7, augmented — the spelling-pin
  **replaces/overrides** the key-dependent `dim7CharacteristicBonus` choice; non-symmetric roots are untouched.
- **C2 is OUT of scope:** the new four-note dim7/mMaj7 *types* (G5) are NOT added here (they'd move legacy output) — only
  the spelling-pin on the existing catalogue. Confirm the pin works on the current types without adding C2.
- If the spelling isn't available at the slice, or the pin needs a structural change beyond the decoder → **STOP and
  report.**

## §2 — BUILD G4 / C1 (in `chordslicedecoder`, dormant)
- Consume `spellingview` to **pin the symmetric root** from the notated spelling (the deterministic rotation choice for
  dim7/aug). Keep the one `analyzeChord` cube; this is the root-selection wiring for symmetric sonorities.
- **No new chord types** (C2 deferred). **No key-dependent heuristic where spelling is present** — the spelling is the
  determiner (that's the whole point: a deterministic pin, not a tuned bonus).

## §3 — RE-MEASURE (the assess checkpoint — corrected gate)
New-vs-legacy, Baroque + Default, judged by **coverage-matched accuracy + correct abstention**. Expect the
**symmetric-root cases** to resolve correctly (the spelling-fixable ~3.1% — e.g. `bwv272@4320` G♯dim7, `bwv289@20160`
A♯dim7), with coverage-matched accuracy **holding-or-improving**. Report the before(G6)→after(G4) numbers + a spot-check
that a notated G♯dim7 is pinned G♯ (not the key-dependent alternative).

## §4 — Gate
- **Production byte-identical:** corpus 53/24/53, both suites, snapshots unchanged (decoder dead). **Movement → STOP.**
- **New unit tests** (oracle-asserted): **G♯dim7 vs A♭dim7 pinned by spelling** (same pitch classes, opposite notated
  spelling → opposite root), an augmented case, and a non-symmetric root untouched by the pin. Build green.

## §5 — ASSESS (this closes the build)
- **Expected:** the spelling-pin resolves the symmetric-root cases deterministically, coverage-matched accuracy
  holds-or-improves → **all Phase-5b build increments (G1–G6, two-reading, G4/C1) are complete.** Next is **Step M** —
  the engage GO/NO-GO + the deferred decisions (§15-O2, C2 new types, bounded-context G7, section-grouping F-3, the
  German-bass fix, the F17 dense-start alignment).
- **If the pin doesn't resolve the symmetric cases, regresses, or needs C2/structure beyond the decoder → STOP and
  report.**

## §6 — Deliver
Commit **locally (unpushed)**: G4/C1 + unit tests (decoder + tests only). Write `cc_phase5b_step4_report.md`
(gitignored): the §1 confirm, the §2 build, the §3 re-measure + spelling spot-check, the §5 assessment (build complete),
and the commit sha — so Cowork verifies by sha that only `chordslicedecoder.*` + tests changed, production byte-identical.

## §7 — Stops
- Spelling unavailable at the slice, or the pin needs structure beyond the decoder → STOP.
- C2 new types creep in (they belong at engage) → STOP.
- Any production movement → STOP. `upstream` → STOP.
