# CC Instruction — Phase 5c Step 1: the progression model + base Roman-numeral derivation (L5, dormant)

> **Plan: `cowork_phase5c_l5_build_plan.md` Step 1. Spec: `cowork_layer5_function_design.md` §5.0 + §5.1 (the contract —
> implement its mechanism, do not re-spec).** Step 0 is GREEN/ratified; the two surfaced items are closed (F1: §5.5 now
> rules `symmetric-rotation`; F2: Step 4 will reuse `localmodulationdetector` — not this step). Build the function layer's
> **shared evidence + deterministic derivation**, **DORMANT** (new module behind a default-OFF capability gate, no
> production consumer) → **byte-identical on production**. **Default constants (the firewall) — no tuning. Reuse, do not
> duplicate. Proportionality: build the mechanism right and stop.** *(Reminder: the never-bash rule is Cowork's; it does
> not constrain your build/test runs.)*

## §0 — Preamble (sweep)
Commit local-only the unstaged Cowork docs (the Phase-5c plan + the F1/F2 design syncs + the phrase-boundary/L2/L5 edits):
`docs(cowork): L5 build plan + Step-0 F1/F2 resolutions`. **Also fix the F6 cosmetic duplicated sentence you flagged in
the Step-0 dossier when you commit** (you know its location). Report the sha.

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read-only, confirm and report:
- **The progression model's inputs (§5.0):** the **ordered committed-chord stream over a region** is reachable (the L4
  decoder's committed `ChordSliceCandidate` per slice, or the region chord results), and the key (the L3 region key) — so
  "the progression," "prevailing harmony" (nearest metrically-strong committed chord, via the §3 metric-weight contract),
  and "established next function" (next committed or cadence-anchored function) are all derivable from existing data.
- **The base-RN reuse (§5.1):** confirm `diatonicDegreeForRootPc` (degree) and `ChordSymbolFormatter::formatRomanNumeral`
  (the full numeral: quality, inversion as figured bass, chromatic alteration, aug6, inline applied) are **consumable as
  a library** for L5's base RN — so L5 **wraps** them, not re-implements. Flag any gap that would force duplication.
- **Placement:** the new dormant L5 module's home (a new `function/`-side unit; **do NOT** rename or touch the misnamed
  `harmonicfunctionlayer` — that's an engage-step structural item). State where it lands.
If the progression inputs aren't reachable, or the base-RN emission can't be reused (forcing a duplicate formatter), or a
structural change beyond a new dormant module is needed → **STOP and report.**

## §2 — BUILD the progression model (§5.0), dormant
- The **licensed (real) progression** predicate: given two functions (committed chords read in the key), is the root
  motion one of the **enumerable** standard successions — descending-fifth (dominant); descending-third or ascending-second
  functional step; the resolution of an applied/leading-tone chord to its tonicized target; or a cadential motion? A
  stated, closed test (no preference; the numeric preference *among* licensed readings is Phase B).
- **"The progression"** (the ordered committed-chord/function stream over a region), **"prevailing harmony"** (the
  committed chord of the nearest metrically-strong slice at/before a slice, in the region), and **"established next
  function"** (the next committed non-abstained function, or the next cadence-anchored one) — exactly per §5.0.
- This is **key-/chord-fed surface logic** — no cadence yet (Step 2), no resolution decisions (Step 3). Pure predicates.

## §3 — BUILD the base Roman-numeral derivation (§5.1), dormant
- The L5 base-RN entry point: degree (+ chromatic alteration), quality, inversion — by **wrapping** `diatonicDegreeForRootPc`
  + `formatRomanNumeral` (per §1), at **full DCML/RomanText completeness, no simplification** (§3 Produces). Deterministic;
  introduces no judgment beyond the key+chord it is given. **Reuse the one formatter — do not add a second.**

## §4 — Constants
- None to tune here: the progression model is an enumerable rule set; the base RN is deterministic. (No weights/thresholds
  at this step — those begin at Step 2's cadence vote and are precision-phase regardless.)

## §5 — Tests (oracle-asserted)
- **Progression model:** a descending-fifth motion is **licensed**; an applied-chord→target resolution is **licensed**; an
  arbitrary non-functional root motion (e.g. a tritone leap with no resolution) is **not** licensed; "prevailing harmony"
  and "established next function" resolve correctly on a small fixture.
- **Base RN:** a known chord-in-key emits the correct full numeral (degree + quality + figured-bass inversion + a chromatic
  case), matching the existing formatter (the wrap is faithful, not a re-derivation).

## §6 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh (the new module has **no production consumer**). Movement → STOP.

## §7 — Deliver
Commit **locally (unpushed)**: the new dormant L5 module (progression model + base RN) + the §5 tests. Write
`cc_phase5c_step1_report.md` (gitignored): the §1 confirm (incl. the reuse verdict + placement), the §2/§3 build, the §5
tests, the §6 gate result, and the commit sha — so Cowork verifies the module is dormant (no production reach) and the
base RN reuses the one formatter.

## §8 — Stops
- Base-RN reuse impossible (would duplicate the formatter), or progression inputs unreachable, or a structural change
  beyond a new dormant module → STOP, report.
- Any production movement (not byte-identical) → STOP. Any threshold/weight **tuning** → STOP (firewall). `upstream` → STOP.
