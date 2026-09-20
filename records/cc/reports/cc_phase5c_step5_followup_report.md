# CC Report — Phase 5c Step-5 follow-up: generalize the applied trigger (L5 §5.6, dormant)

**Task:** `cc_instruction` Phase-5c Step-5 follow-up — Cowork ruling on the declared **A-D2**
(`viio/IV` divergence). Admit applied **leading-tone** chords as a class by **generalizing the
chromaticism test**, not by bolting on `viio/IV` as another special case. Spec:
`cowork_layer5_function_design.md` §5.6 (amended 2026-06-29). Default constants (firewall);
reuse, do not duplicate; generalize the one test, stop.

**Outcome:** DONE, **dormant + byte-identical on production**. `viio/IV` (and `viio7/IV`) now
emits via the generalized foreign-tone trigger; the false-positive guard still rejects the
genuinely-diatonic case; `V/V` and `V7/IV` (the prior instances) unchanged; production paths
untouched.

**Commit (local, unpushed):** `9bd60a063b` — `feat(function): L5 generalize the applied trigger to
the foreign-tone test (Phase 5c Step-5 follow-up, dormant)`.

---

## §1 — The change (`function/functionrelationallabel.{h,cpp}`, the unified applied path)

The single edit is inside `emitAppliedLabel()`'s **broadening** (the path taken after the
guarded `tonicizationlabeler` returns *not applied*). The prior broadening was the ♭7̂-only
special case (Step-5, 2026-06-26: a dominant seventh whose `♭7̂` is chromatic → `V7/IV`). It is
now the **general chromaticism test §5.6 always implied**:

> an applied **dominant-** or **leading-tone-function** chord of a **non-tonic diatonic degree**
> that contains **at least one tone foreign to the home-key collection**.

Concretely, after the labeler declines:

1. **Function class + relation to the target** (§5.6):
   - *dominant-function* (`Major` triad / dominant seventh) → root a perfect fifth **above** the
     target (`rootPc == nextRootPc + 7`);
   - *leading-tone-function* (`Diminished` / `HalfDiminished`, ± a seventh) → root a semitone
     **below** the target (`rootPc == nextRootPc + 11`).
2. **Non-tonic diatonic target**: `diatonicDegreeForRootPc(nextRootPc) > 0`.
3. **The general chromaticism test** (the necessary condition **and** the false-positive guard, in
   one): `pitchClassMask & ~diatonicMaskFromFifths(keyFifths) != 0` — at least one sounding pitch
   class foreign to the home-key collection.
4. **Emit via the production `formatRomanNumeral` inline path** (REUSE, no second formatter — §3);
   the result is committed as the applied label only after confirming the reused emitter produced
   an applied string (the `/<degree>` separator) — a defensive carry-to-`None` for the unreachable
   plain-triad fall-through, never a re-derivation.

The three named instances are now the **one** test's cases, not a closed enumeration:
- **raised secondary LT** (`V/V`) — handled by the kept guarded labeler;
- **♭7̂** (`V7/IV`) — the third degree (IV's LT) is diatonic, so the chromaticism is the ♭7̂;
- **the secondary-diminished's own foreign tone** (`viio/IV`, `viio7/ii`, …) — the diminished
  quality contributes the chromatic tone even where the target's own leading tone is diatonic.

The prior ♭7̂-structural sub-test (`pcInMask(collMask, rootPc+10)`) is **subsumed** by the general
foreign-tone test: for the dominant family, a labeler-dropped chord (raised LT of the target
diatonic ⟹ target is IV in major, or III/VI in minor) has a fully-diatonic plain triad in every
case, so only the chromatic seventh makes it foreign — i.e. the foreign test selects exactly the
dominant **sevenths**, matching the production formatter (which emits `V7/x`, never a `V`-triad
applied). No regression of the prior instances (verified by test — see §4).

**Header comments updated** (`functionrelationallabel.h` module overview + the emitter block) to
describe the generalized trigger. `pcInMask` is no longer used in the TU; the `analysisutils.h`
include comment was trimmed accordingly. **No constants** introduced (firewall, §3) — the trigger
is a deterministic structural + collection-membership test.

## §3 — Constants

None. The generalization removed a sub-test; it added no weight, threshold, or margin.

## §4 — Tests (oracle-asserted, `functionrelationallabel_tests.cpp`, +3 → 22 in the suite)

- **`AppliedLeadingToneTriadOfSubdominantViaGeneralizedTrigger`** — `E°→F` in C major emits
  `viio/IV` (target degree 3, target pc F). The labeler drops it (IV's LT, E, is diatonic); the
  generalized trigger keeps it (the diminished fifth B♭ is foreign).
- **`AppliedLeadingToneSeventhOfSubdominantViaGeneralizedTrigger`** — `E°7→F` in C major emits
  `viio7/IV` (the seventh variant; foreign B♭ and D♭).
- **`AppliedGeneralGuardRejectsDiatonicLeadingToneChord`** — `B°→C` in **A minor** (the diatonic
  `ii°→III`, B-D-F all diatonic) is **not** applied — the guard holds for the leading-tone family.

**Prior instances re-verified green (no regression):** `AppliedDominantTriadTargetDegree` (`V/V`),
`AppliedDominantSeventhTargetDegree` (`V7/V`), `AppliedLeadingToneSeventhTargetDegree`
(`viiø7/V`), `AppliedDominantSeventhOfSubdominantFlatSeven` (`V7/IV`),
`AppliedFlatSevenGuardRejectsDiatonicSeventh` (the natural-minor `bVII7→III` stays not-applied),
`AppliedFlatSevenTriadOfSubdominantIsNotApplied`. All 22 `FunctionRelationalLabel` tests pass.

## §5 — Gate (dormant + byte-identical on production)

- **composing_tests: 972 PASSED** (969 → 972, the +3 above). **notation_tests: 53 PASSED**
  (4 skipped baseline). **pipeline_snapshot_tests: 11 PASSED — NO golden refresh.**
- **No production consumer (grep re-confirmed):** `classifyRelationalLabel` / `emitAppliedLabel` /
  `functionrelationallabel` / `RelationalLabelInput` appear in `src/` only in the module, its test,
  the two `CMakeLists`, and `functionoutput.{h,cpp}`; `functionoutput` is itself consumed only by
  its own test. **Zero hits in `tools/`.** No production path (tonicizationlabeler,
  chordsymbolformatter, regionanalyzer, batch_analyze, chordanalyzer) is touched.
- **Corpus 53/24/53 unchanged BY CONSTRUCTION.** Only the dormant `functionrelationallabel.{h,cpp}`
  + its test changed; the unified emitter has no production reach and the production
  tonicization/RN paths are byte-identical, which `pipeline_snapshot 11/11` with **no** golden
  refresh independently proves (P1/P2/P3/P4 output identical). The full 3-preset corpus regen was
  **not run**, consistent with the established dormant-L5-step precedent (sessions 9–13) and
  CLAUDE.md's corpus-regen scoping (gate/scoring changes), neither of which this change is.

## §2 — Recorded divergence from the legacy inline path (for Step M / Phase 5d — NOT reconciled now)

The production `formatRomanNumeral` inline applied path is **unguarded** by chromaticism, so the
guarded unified emitter rejects two genuinely-diatonic cases the inline path would over-emit. The
generalization is *more* correct there, but whether each call is right is **measured at engage
against the DCML ground truth**, not decided now (§5.6 final bullet). The production path is
untouched.

| Sonority (home key) | Pitch classes | Inline path (unguarded) | Unified emitter (guarded) |
|---|---|---|---|
| `bVII7→III` — `G7→C` in A minor | G-B-D-F (all diatonic) | over-emits `V7/III` | rejects → diatonic numeral (prior, Step-5) |
| `ii°→III` — `B°→C` in A minor | B-D-F (all diatonic) | over-emits `viio/III` | rejects → `ii°` (**NEW, this generalization**) |

Both are pitch-class-fully-diatonic chords of a non-tonic degree where the inline path's
unguarded trigger fires but the §5.6 foreign-tone guard correctly does not. The second row is the
new divergence introduced by extending the broadening to the leading-tone family.

## §0 / §6 — Doc + deliver

- The **§5.6 amendment** in `cowork_layer5_function_design.md` (the general foreign-tone test, the
  three named instances, the divergence note) was already present in the working tree as the spec;
  it is committed **in the same commit** as the code + tests (the sync rule).
- `STATUS.md` to be updated as the session's last act.

## §7 — Stops

None hit. No false positive un-guardable by the chromatic test; no production movement; no
threshold tuning; no T/S/D read-out; no `upstream`. **Steps 0–6 + the A-D2 follow-up complete →
Step M** (the read-only measure + engage GO/NO-GO).
