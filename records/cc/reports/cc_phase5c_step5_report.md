# CC report — Phase 5c Step 5: relational labels + unify the tonicization paths (L5 §5.6, dormant)

> **Plan:** `cowork_phase5c_l5_build_plan.md` Step 5. **Spec (SIGNED):** `cowork_layer5_function_design.md` §5.6 + §8 +
> the §5.0 shared defs. **Discipline:** dormant + byte-identical, reuse-heavy, default constants (firewall — the labels
> are deterministic triggers, no constants), proportionality (build the emitter right and stop).
> **Outcome: DONE, dormant, byte-identical on production by construction.**

## §0 — Sweep (commit the unstaged Cowork doc)
Committed local-only the modified `cowork_layer5_function_design.md` (the §5.3 Step-4 build note: reuse of
`localmodulationdetector` + `forwardoverride`; the persistence hysteresis layered on the detector's committed spans with
the establishment floor as a candidate pre-filter; the §8 modulation contradiction strength = cadential weight; the one
Step-M check).
- **`12b899330f`** `docs(cowork): Phase-5c Step-4 ratification`.

## §1 — INVESTIGATE-confirm the reuse map (read-only, all GREEN — no STOP)
Confirmed at source that this step is reuse-heavy and every reuse target is consumable:

| Reuse target | Where | What it gives Step 5 | Verdict |
|---|---|---|---|
| `ChordSymbolFormatter::formatRomanNumeral` | `chordsymbolformatter.cpp:827` | **aug6** `It+6/Fr+6/Ger+6` (root `♭6̂` + `SharpThirteenth` + `naturalFifthPresent`[Ger]/`SharpEleventh`[Fr], lines 884–899); **inline applied** `V7/x, vii°/x` when `nextRootPc≥0` (lines 909–962); **chromatic numerals** `bII, bVI, bVII` (`csfChromaticRoman`, lines 831–857); **figured-bass inversion** `csfRomanWithInversion` → `bII6` for a major-triad first inversion (line 687-694) | **Reusable as-is** — the relational labels WRAP/EXTEND it; no second formatter built |
| `tonicizationlabeler::labelTonicizations` | `tonicizationlabeler.cpp:64` | the dormant applied-chord labeler: **chromatic-LT false-positive guard** (`pcInMask(collMask, lt)` → skip diatonic-LT) + the **LT-present** check + the plain-triad `V/d` the inline path drops | **Consumable** as the basis of the unified emitter; the guard is worth keeping |
| `engravingbridge::lineOfFifths` | `spellingview.{h,cpp}` | `lineOfFifths(tpc) = tpc − TPC_C`; the +10-tone's **line-of-fifths distance** from the root: **+10 ⇒ augmented sixth** (sharp side), **−2 ⇒ minor seventh** (flat side) — the decisive Ger6↔V7 separator | **Consumable** — the one place spelling is read |
| `region::diatonicDegreeForRootPc` | `sparsechordrefinement.h:42` | the scale degree the base RN + the mixture residual key on (same source as the §5.1 wrap) | **Reusable** |
| `analysisutils` `normalizePc` / `pcInMask` / `diatonicMaskFromFifths` | `analysisutils.h` | the shared pc / signature-collection primitives | **Reusable** (already shared) |

**The four triggers (confirmed):**
- **augmented sixth** — root `== ♭6̂` (`tonic+8`), Major quality, the +10 tone spelled as an augmented sixth (LoF +10);
  It/Fr/Ger by the added degree (`naturalFifthPresent`→Ger, `SharpEleventh`→Fr, else It);
- **Neapolitan** — a Major triad on `♭2̂` (`tonic+1`), conventionally first inversion → the chromatic numeral + figure `bII6`;
- **applied/secondary** — a raised secondary leading tone of a non-tonic diatonic degree (the chromatic-LT guard) → `V/x, V7/x, vii°/x, …`;
- **modal mixture** (residual) — a quality-altering borrowed degree (chromatic root, or in a major key a borrowed
  diatonic-triad quality) matching **none** of the above → the chromatic/altered base numeral (`bVI`, `iv`, …).

**Reuse-vs-build map + unification plan reported:** one new dormant unit
`function/functionrelationallabel.{h,cpp}` that (a) classifies the relational role in the fixed §5.6 precedence and
delegates the string to `formatRomanNumeral` (no second formatter), reading `spellingview` only for Ger6↔V7; (b) owns
`emitAppliedLabel()` — the single applied/tonicization emitter that subsumes the two existing paths by reusing
`labelTonicizations` (guard kept). **No label forced a duplicate; spelling is reachable for Ger6 → no STOP.**

## §2 — BUILD the relational labels (§5.6), dormant
`classifyRelationalLabel(in)` tests the four labels in the **fixed precedence, first match wins** —
**augmented sixth → Neapolitan → applied/secondary → modal mixture** — with **modal mixture the residual** (decided by
*non-match*, not a positive "is borrowed" test):
- **`tryAugmentedSixth`** — structural gate (Major quality + root `♭6̂`), then the **spelling read** `augSixthSpellingSign`
  via `lineOfFifths` (the pc of a tpc is `(LoF·7) mod 12`, used to find the +10 tone among `noteTpcs`; its LoF distance
  from the root is +10 ⇒ aug6, −2 ⇒ min7). On aug6 it ensures `SharpThirteenth` on a copy and calls `formatRomanNumeral`
  → `It+6/Fr+6/Ger+6`. On a min7 spelling (or spelling absent) the aug6 label does **not** fire (held uncertain, §11).
- **`tryNeapolitan`** — Major triad on `♭2̂` → `baseNumeral` = the chromatic numeral + inversion figure (`bII6`).
- **applied** — delegated to `emitAppliedLabel` (§3).
- **`tryModalMixture`** (residual) — fires only when nothing earlier matched: a chromatic root, or (Ionian only) a diatonic
  root whose triad family differs from the major-key diatonic triad on that degree → `baseNumeral` (`bVI`, `iv`).
- role **None** (a plain diatonic chord) carries the base numeral, so the caller always gets a complete RN.

**Spelling-aware only where the distinction is a spelling distinction** (§8): the ONE `spellingview` read is the
Ger6↔V7 call. The notated spelling *implies the resolution* (aug6 expands outward, the min7 resolves down), so reading the
spelling **is** reading "which resolution the notated spelling implies" — no separate next-chord voice-motion check is
needed (declared build-detail decision below).

## §3 — Unify the two tonicization paths (one owned dormant emitter)
`emitAppliedLabel(in)` is the single owned applied/tonicization emitter. It **subsumes** the two paths that label
tonicization today by **reusing** `labelTonicizations` over the pair `[this chord → next chord's root]` — the dormant
labeler's algorithm with its **chromatic-LT guard kept** (maximal reuse, not a re-implementation). It maps the
`TonicizationLabel` → `RelationalLabel` (role `AppliedSecondary`, the `V/x` string, the target degree/pc).
- **Production untouched:** `tonicizationlabeler.cpp` and `chordsymbolformatter.cpp` are **byte-identical** (`git diff`
  empty). The retirement of the two existing paths + the production switch land at the **joint engage (Phase 5d)** — not
  here — so this step stays byte-identical. The unification *exists*; production still runs the inline +
  dormant-labeler paths.

## §5 — Tests (oracle-asserted, +16, all green)
`functionrelationallabel_tests.cpp` (16 tests):
- **applied target degree (local key):** `D` major→`G` = `V/V` (the plain-triad applied dominant the inline path drops);
  `D7`→`G` = `V7/V`; `F♯ø7`→`G` = `viiø7/V`; the kept guard rejects `V7`→`I` (target is the tonic).
- **Neapolitan:** a `♭2̂` first-inversion major triad → `bII6`.
- **aug6 by degree + spelling:** `It+6` (Ab-C-F♯), `Fr+6` (Ab-C-D-F♯), `Ger+6` (Ab-C-Eb-F♯); the **SAME** pcs spelled with
  `Gb` (minor seventh) → **not** aug6 (`bVI7`) — the Ger6↔V7 separation by spelling.
- **modal mixture residual:** `iv` (F minor in C, borrowed quality on a diatonic degree); `bVI` (Ab major, chromatic root).
- **precedence first-match:** a `♭2̂` major triad → Neapolitan (not mixture); a `♭6̂`-aug6 → aug6 (not mixture); a major-II
  resolving to V → applied `V/V` (not mixture).
- **role None / direct emitter:** a plain `V` → role None + base numeral; `emitAppliedLabel` produces `V/V` and returns
  None for a non-applied chord.

## §6 — Gate (dormant + byte-identical — no movement, no STOP)
- **composing 942 → 958 (+16** FunctionRelationalLabel).
- **notation 53** (4 skipped baseline).
- **pipeline_snapshot 11/11 — NO golden refresh** (chord output byte-identical).
- **corpus 53/24/53 unchanged BY CONSTRUCTION** — no production consumer: a grep of `src/` + `tools/` finds the new
  identifiers (`functionrelationallabel`, `classifyRelationalLabel`, `emitAppliedLabel`, `RelationalLabelInput`,
  `RelationalRole`) **only** in the module, its test, and the two `CMakeLists.txt`; the existing `tonicizationlabeler` /
  `chordsymbolformatter` paths are byte-identical (`git diff` empty). The corpus regen was **not** run — consistent with
  the Step-1/2/3 dormant-no-production-reach precedent (the snapshot no-refresh proves chord-output identity, and no
  scoring/gate/template/region/bridge code is touched).

## §7b — Declared build-detail decisions (Cowork review)
1. **The unified emitter reuses `labelTonicizations` (guarded), choosing the labeler's behaviour over the inline path's.**
   The two existing paths **disagree** on the lowered-7th applied dominant of IV: `formatRomanNumeral`'s inline path emits
   `V7/IV` unguarded (any dom7 a fifth above a non-tonic target), but the §5.6 trigger is a **raised secondary leading
   tone** and the tonicizationlabeler's chromatic-LT guard **rejects** `V7/IV` (IV's leading tone `3̂` is *diatonic*; the
   chromaticism of `V7/IV` is the `♭7̂`, not a raised target-LT). §3 says "keep its chromatic-LT guard," so the unification
   follows the **guarded** behaviour. **This is an inference-problem-shaped divergence the unification surfaces — declared,
   not resolved here** (it is a spec clarification / Phase-5d reconciliation item: whether the raised-LT trigger should be
   widened to the `♭7̂`-applied-dominant-of-a-subdominant case). Per the standing rule I did not invent logic to bridge it.
2. **Ger6↔V7: the spelling read is the decisive separator and *is* the implied resolution.** The notated spelling (LoF
   +10 aug6 vs −2 min7) determines which resolution the chord implies (aug6 expands outward to V; the seventh resolves
   down), so reading the spelling through `spellingview` suffices — I do **not** additionally verify the next-chord
   voice motion. (§5.0/§5.6 frame the distinction as "which resolution the notated spelling implies" — the spelling implies
   it.)
3. **The aug6 string is L5-spelling-authoritative.** When the spelling read says aug6, `tryAugmentedSixth` ensures
   `SharpThirteenth` on the copy passed to `formatRomanNumeral`, so the `It/Fr/Ger+6` emission is driven by **this layer's**
   spelling decision (read through the one shared interpreter), not by whether an upstream extension bit happened to be set.
   The It/Fr/Ger sub-type still follows the chord's `naturalFifthPresent` / `SharpEleventh` content.
4. **Modal-mixture residual scope (declared, proportional).** Borrowed-quality detection on a **diatonic** root is measured
   only in a **major (Ionian)** key (the canonical iv-in-major case) against the fixed major-key triad-quality table — this
   avoids the harmonic-minor-dominant misfire (a major `V` in minor would otherwise look "borrowed" against the
   natural-minor collection). In non-Ionian keys only the **chromatic-root** mixture fires. The residual is a best-effort
   **role tag**; the emitted **label string is always the formatter's correct numeral**. Minor/modal borrowed-quality is a
   precision-phase (Phase B) refinement if measured needed.
5. **`♭6̂` collision resolved by precedence.** The aug6 root and the `bVI` mixture root are the same degree; the precedence
   (aug6 first, gated on the aug6 spelling) decides — a `♭6̂` Major chord *with* the aug6 spelling is aug6, *without* it is
   `bVI` mixture. (Demonstrated by the Ger-vs-V7 and the bVI tests.)
6. **Placement / naming.** New unit beside the Step-1..4 function units (`function/`), namespace
   `mu::composing::analysis`. The `harmonicfunctionlayer` rename + the `function/` directory split remain engage-step
   structural items (unchanged).

## Commits (local, unpushed)
- **`12b899330f`** `docs(cowork): Phase-5c Step-4 ratification` (the §0 sweep).
- **`a654df255c`** `feat(function): L5 relational labels + the unified tonicization emitter (Phase 5c Step 5, dormant)`.

## Status
**Steps 0–5 of `cowork_phase5c_l5_build_plan.md` COMPLETE** (progression model + base RN + cadence detector + resolver +
the §8 forward-override + tonicization-vs-modulation + the modulation recompute + the two §15-3 pins + the relational
labels + the unified tonicization emitter — all dormant / byte-identical). **Next: Step 6 — L5 output assembly (§7): the
Roman numeral at full DCML completeness, the function confidence, the open mark, the cadence + key markers, the L5→L6
contract (the T/S/D read-out deferred, §9-D1).**
