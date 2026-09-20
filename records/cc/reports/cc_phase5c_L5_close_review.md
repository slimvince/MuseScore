# CC — L5-closing QA review (source-level half): code · tests · corpora · staleness

> **Round:** the layer-closing QA before L6 opens. CC's **source-level** half (code, tests, corpora/test-data,
> staleness); Cowork takes architecture + documentation + synthesis. **Read-and-report + tidy the clear-cut only.**
> Everything algorithm/architecture/inference is **declared, not acted.** Firewall held: no inference fix, no
> production movement, dormancy + byte-identity preserved.
>
> **Verdict (source-level):** **complete AND correct, dormant, byte-identical.** Two clear-cut test-coverage gaps
> tidied (now green); one stale doc count tidied; **three discoveries declared** (one a clean-bill *strengthening* of
> the session-16 over-trigger ruling, one a measurement-completeness question, one a low-severity engage-time naming
> hazard). No structural defect found. The §8 closure has no back-edge, reuse is not duplicated, every L5 unit is
> dormant, and the corpus reproduces **53 / 24 / 53**.
>
> **Commits (local, unpushed, master):**
> - `4b8b0399be` `test(function): add Evaded cadence + symmetric-rotation cadence-pin coverage`
> - `9d4c3fb363` `docs(build): correct stale composing-test baseline 407 -> 974`
> - + the STATUS entry for this round.
> **Not mine, left untouched:** `contrapunctus_findings.md` carries a *Cowork* L6-research addendum (parallel work) —
> deliberately excluded from my commits.

---

## §0 — Scope + ground rules check

- Units reviewed at source: `functionprogression`, `functionromannumeral`, `functioncadence`, `functionresolver`,
  `forwardoverride`, `functionmodulation`, `functionrelationallabel`, `functionoutput` (+ the reused
  `tonicizationlabeler`, and the `--dump-l5` diagnostic in `tools/batch_analyze.cpp`).
- Invariants verified (details below): **dormancy** (no `src/` production consumer), **reuse-not-duplicate**, **§8 no
  back-edge**, **default constants** (firewall), **corpus 53/24/53**.
- Tidies applied are **tests + one doc count only**. Everything touching algorithm/contract/inference is in §5
  (declared, not acted).

---

## §1 — Code review (per-unit, at source)

Legend: **C** = correct vs its §5.x spec rule · **D** = dormant · **R** = reuse (no duplication) · **Q** = quality.

| Unit | C | D | R | Q | Notes |
|---|---|---|---|---|---|
| `functionprogression` | ✅ | ✅ | ✅ | ✅ | §5.0 licensed successions (desc-5th/desc-3rd/asc-2nd/applied) as pure predicates; `isMetricallyStrong` = parameter-free local-max (≥ on both sides; out-of-range = −∞). `prevailingHarmonyIndex` returns the slice itself for a committed-strong slice — by design; the resolver's case-4 deliberately uses a *separate* backward loop for "the neighbours" (documented at `functionresolver.cpp:401`). |
| `functionromannumeral` | ✅ | ✅ | ✅ | ✅ | Faithful wrap of the ONE emitter (`diatonicDegreeForRootPc` + `formatRomanNumeral`). No second formatter. |
| `functioncadence` | ✅ | ✅ | ✅ | ✅ | §5.2 key-agnostic event-pair detector; LT-**resolution** event (not presence); the cadential-6/4 collapse; PAC/IAC by bass inversion; the §5.2-amendment plain-triad V→I; the documented key-agnostic limit. **Evaded branch had no test → tidied (§2).** |
| `functionresolver` | ✅ | ✅ | ✅ | ✅ | §5.5 selection per ambiguity kind + §5.7 soft prior + §5.5-case-4 fine-grain override through §8. SELECTION-only (no re-derivation). **Symmetric-rotation cadence-pin branch had no test → tidied (§2).** `tieBreakOrOpen` reads `readingA.bassPc` as "the slice bass" — correct: both carried readings share the one physical bass (`chordslicedecoder.h` — readings differ in root/quality, not bass). |
| `forwardoverride` | ✅ | ✅ | ✅ | ✅ | The §8 mechanism: confidence-clamped monotone bar, strict-`>` tie-to-incumbent, one-pass closure (grows-only), re-entrancy-guarded forward sweep. **No back-edge** — only the `reread` callback fires; nothing upstream; nested recompute refused (−1). |
| `functionmodulation` | ✅ | ✅ | ✅ | ✅ | §5.3 default-tonicize + cadence-gate + persistence/hysteresis (strict `>` ⇒ break-even tonicizes); §5.4 recompute = the §8 channel #1 (REUSES `OnePassClosure`); `detectAndDecideModulations` REUSES `detectLocalModulations` end-to-end. |
| `functionrelationallabel` | ✅ | ✅ | ✅ | ✅ | §5.6 fixed precedence (aug6→Neap→applied→mixture, first match wins); ONE spelling read (Ger6↔V7 via `lineOfFifths`); REUSE `formatRomanNumeral` + the guarded `tonicizationlabeler`. **The `V/iv`-on-tonic over-trigger lives here** (the `tl.isApplied` early-return precedes the §5.6 foreign-tone guard) — **confirmed matching the session-16 inference ruling; see §5 D1 for why the guard ordering is provably inert.** |
| `functionoutput` | ✅ | ✅ | ✅ | ✅ | §7 assembly: full RN (relational.label verbatim), 3-component confidence at default weights, open mark, region local-key/cadences, additive over L4. `cadenceVoteForUnit` uses half-open `[start,end)` (test-pinned: arrival AT `endTick` belongs to the next unit). T/S/D read-out correctly absent (§9-D1). |
| `tonicizationlabeler` (reused) | ✅ | ✅ | n/a | ✅ | Live reuse target of `emitAppliedLabel`; its raised-LT guard + the foreign-tone admission are the basis of §5 D1. |

**Dormancy (re-greps, naming every includer):** the eight L5 headers are included only by (a) their own `.cpp`, (b)
sibling L5 units, (c) their `*_tests.cpp`, (d) `src/composing/analysis/CMakeLists.txt`. The L5 *function symbols*
(`classifyRelationalLabel`, `assembleFunctionOutput`, `resolveCarriedReadings`, `detectFunctionalCadences`,
`decideTonicizationVsModulation`, `deriveBaseRomanNumeral`, …) appear outside the module/tests **only** in
`tools/batch_analyze.cpp` (the `--dump-l5` diagnostic) and `STATUS.md`/CMake. **Zero `src/` production consumer.**

**Reuse (delegations live, not forked):** `formatRomanNumeral` (the one RN string), `labelTonicizations` (the applied
path), `detectLocalModulations` (the modulation substrate), `forwardoverride::OnePassClosure` (both §8 channels),
`region::diatonicDegreeForRootPc` (degree), `engravingbridge::lineOfFifths` (the one spelling read). No second
formatter / no re-implemented detector.

**Quality:** no `TODO/FIXME/XXX/HACK` in the module (grep-clean); no dead branches or unused fields found; comments
accurate. The template-count size-coupling invariant is intact: `kTemplateCount = 17` (`chordanalyzer.h`) ==
`std::array<TemplateDef, kTemplateCount>` decl == `docs/scoring_model.md §2` ("currently 17").

---

## §2 — Test-case audit (coverage matrix + tidies)

94 L5 unit tests pre-round (progression 10 · romannumeral 7 · cadence 17 · forwardoverride 11 · resolver 13 ·
modulation 6 · relationallabel 22 · output 8). **Oracle quality: strong** — assertions are against known theory
(licensed vs unlicensed motion; PAC/IAC by inversion; bII6; It/Fr/Ger by spelling; the §8 bar values), not echoes of
the implementation. The cadence suite even *pins* the key-agnostic I→IV/V→I limit as a documented by-design fact.

Coverage matrix (rule / kind / label / type → covered?):

| Dimension | Item | Covered |
|---|---|---|
| §5.x rule | §5.0 progression · §5.1 base RN · §5.2 cadence · §5.3 toniciz-vs-mod · §5.4 recompute · §5.5 resolver · §5.6 relational · §5.7 prior · §7 assembly · §8 override | ✅ all |
| Ambiguity kind | Transition·ShareTone·RelativePair·Close·Insufficient·SymmetricRotation | ✅ all (Symmetric had **applied-resolution + open** but **not the cadence-pin** branch → **added**) |
| Relational label | applied (V/x, V7/x, viio/x, viio7/x, viiø7/x) · Neapolitan · aug6 It/Fr/Ger (+Ger↔V7) · modal mixture | ✅ all |
| Cadence type | PAC·IAC·Half·PhrygianHalf·Deceptive·Plagal·**Evaded** | Evaded had **zero** tests → **added** |
| §8 + closure | bar/monotone/clamp/tie · markFinal · tryOverride · forwardRecompute · nested-refused · re-target-refused · reset | ✅ all |
| §7 output | RN · 3-component confidence · open mark · region key · modulation · additive · cadence-vote-by-tick | ✅ all |

**Tidies added (dormant, oracle-asserted, build-green):**
1. `FunctionCadence.GenuineDominantToAbandonedArrivalIsEvaded` — `ii → V7 → iii(Em)` at a phrase end: the §5.2 Evaded
   residual (genuine dominant, abandoned tonic arrival = the mediant; votes for the implied C; discounted below a PAC).
2. `FunctionResolver.SymmetricRotation_ResolvedByCadencePin` — a dim7 as the last slice (no applied target) with a
   cadence on A pins `G#dim7` (A's viio) — the §5.5 `pinHits==1` branch, distinct from the applied-resolution branch.

**Declared gap (NOT added — judgment-call expectation, §2 rule):** a characterization test for the **`V/iv`-on-tonic
over-trigger** itself. Its "correct" expected output is precisely the inference question session-16 deferred (structural
layer emits `V/iv`; whether that is right is a §5.3–§5.5 decision), so encoding an expectation here would pre-judge an
inference matter. Recommend Cowork rule whether to pin it as an as-built *characterization* (asserting "emits V/iv,
deferred" — a regression guard, not a correctness claim).

---

## §3 — Corpora / test-data verification

- **Gate reproduces 53 / 24 / 53.** `characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}` all
  return rc=0 ("Corpus OK 353/353", manifests validated — the script refuses on missing/incomplete manifest or
  fingerprint mismatch, so rc=0 *is* the byte-identity + manifest-integrity proof) and count **53 / 24 / 53**.
  Containment check: every `stem@tick` the detail enumeration prints (baroque 30 / jazz 20 / default 29 — the detail
  sections enumerate a subset of the delta groups, not all 53/24/53) is a member of the CLAUDE.md gate sets — zero
  outliers. The corpus was generated at `4f63d2ab40` (session 12); it still reproduces at HEAD ⇒ the intervening L5
  sessions (13–16) are corpus-confirmed byte-identical. *Methodology note:* I verified via the **manifest-validated
  existing dirs** (byte-identical `.ours.json`), not a fresh clean regen; a regen is available if Cowork wants the
  stronger check, but it is byte-identical by construction (test-only changes; `batch_analyze` was not recompiled).
- **Harness correct + read-only.** `tools/cc_stepM_l5_measure.py` present; `batch_analyze --dump-l5` present, default
  OFF, runs (rc=0 on `bwv272`), substrate = the legacy `AnalyzedRegion` source (as documented), and is additive (each
  `l5` entry carries `rootPitchClass` = the L4 committed root verbatim; the standard `.ours.json` is unchanged). It
  also emits the unguarded `inlineRomanNumeral` baseline for the §5.6 divergence measurement — confirmed exposing the
  labeler-vs-inline divergences (see §5 D2).
- **DCML ground truth no-regression.** `tools/test_dcml_parser.py` passes (rc=0); it oracle-asserts the parser-rebaseline
  fix (applied `/X` relative-root rooting: `V/v`→pc2, `IV/III`→pc8, `ii/III`, `iii/III`, `vi/III`, `I/III`, `V6/III`).
  The `characterise` DCML roots are sensible (`bwv10.7` DCML root=G `V4/3/iv`; `bwv144.6` root=Bb `viio4/3`).
- **Test-data hygiene.** No corpus / `docs/score_inventory.md` do-not-touch file modified by this round (tidies are
  test + one doc only); working tree clean apart from my files + Cowork's `contrapunctus_findings.md` + gitignored
  `scratch_artifacts/`.

---

## §4 — Staleness sweep

- **`fully-diatonic guard` premise (reverted session-16):** the only two carriers — `STATUS.md` (current entry) and
  `cowork_layer5_function_design.md §5.6` — both describe the **corrected** ruling ("an earlier framing of this as a
  'fully-diatonic guard gap' was a corrected error — the chord is not diatonic"). **Not stale.** (Spec text is Cowork's;
  reported, not edited.)
- **"engage / Phase 5d as next" framing:** current docs say engage is **deferred indefinitely, L6 next** (STATUS
  session-16). L5 code comments say "load-bearing **when** the function layer engages (Phase 5d)" — conditional, still
  accurate (Phase 5d remains the *name* of the engage step). ARCHITECTURE.md / `implementation_roadmap.md` carry no
  stale "engage is next" claim. **Not stale.**
- **Template-count invariant:** consistent (17 across `kTemplateCount`, the array decl, and `scoring_model.md §2`).
- **§7 contract / §5.x rules vs code:** cross-checked — the design §7 produces (full RN, function confidence, open mark,
  local key, cadence markers, additive over L4, T/S/D deferred §9-D1) match `FunctionLayerOutput`; the §5.6 precedence
  matches `classifyRelationalLabel`; the two session-16 inference inputs (the `V/iv` over-trigger; the
  tonicization-vs-modulation None-role residual) are recorded in §5.6 / STATUS. **No drift.**
- **Tidied (clear-cut, doc-only):** `BUILD_AND_TEST.md §2` composing baseline **407 → 974** (superseded count; verified
  this session: 974 active + 2 disabled). Commit `9d4c3fb363`.
- **Out-of-scope note (not tidied):** CLAUDE.md / STATUS / BUILD_AND_TEST carry a self-flagged inconsistency on the
  *secondary* `analyze_inversion_errors.py` split ("24/13, 35/7 — stale/pending under the corrected parser" vs
  `cc_functional_residual_dossier.md` which says it WAS re-measured to 47/57, 81/23). This predates L5 and touches the
  measurement-doc layer, not the L5 build; flagged for Cowork, not tidied (CLAUDE.md edits are high-stakes + out of this
  round's L5 scope).

---

## §5 — Discoveries (declared, NOT acted)

### D1 — clean bill that *strengthens* the session-16 over-trigger ruling (the guard ordering is provably inert)
The `V/iv` over-trigger is the `tl.isApplied` early-return in `emitAppliedLabel` firing **before** the §5.6 foreign-tone
guard (the broaden path's guard only runs on chords the labeler *declines*). One could read that as a guard-placement
bug ("emits before its guard"). **It is not** — and the proof is at source:
- The labeler (`tonicizationlabeler.cpp`) admits an applied chord ONLY when its target degree `d`'s leading tone
  `lt = (d+11) mod 12` is **chromatic** to the key collection (`pcInMask(collMask, lt)` ⇒ `continue`), AND
  - AppliedDominant: `lt` (the chord's major third) is **present** in the chord's `pitchClassMask`, OR
  - AppliedLeadingTone: the chord **root** `≡ lt`.
- Either way the labeler-fired chord **contains `lt ∉ collMask`** ⇒ it has ≥1 foreign tone over the **same**
  `diatonicMaskFromFifths(keyFifths)` the §5.6 guard uses.
- Therefore `hasForeignTone = (pitchClassMask & ~collMask) != 0` is **always true** for a labeler-fired chord ⇒ if the
  foreign-tone guard ran on the labeler path it would **never reject** it.

⇒ Running the §5.6 guard "earlier" changes nothing. The over-trigger (e.g. the major/Picardy tonic and `V/iv` being
pitch-class-identical, both carrying the raised third = `iv`'s LT) is genuinely undecidable by any structural foreign-tone
test and **correctly belongs to §5.3–§5.5 inference**, exactly as session-16 ruled. **The guard asymmetry is safe; the
ruling is sound at the code level.** (No action — recorded as evidence Cowork can fold into the complete-and-correct
verdict.)

### D2 — the over-trigger *family* is broader than `V/iv` (a measurement-completeness question)
STATUS characterizes the would-be regressions as "ALL `legacy=I → L5=V/iv` (62/29/56 units, 12/6/13 regressions)." The
`--dump-l5` harness on `bwv272` (Baroque) shows the labeler also emits **`V/VII` at tick 9120 where the unguarded inline
path reads `IV6`** — a labeler-vs-inline divergence of a *non-`V/iv`* shape (a D-major chord into G read as an applied
dominant of the subtonic vs an altered/first-inversion subdominant). By D1 this is the same inference class (the chord
genuinely carries a foreign tone; structural tests cannot decide tonicization-vs-altered-diatonic), so **no structural
fix is implied.** But it shows the divergence *family* is wider than the literal `V/iv`. **Declare:** confirm whether the
measured 12/6/13 regression set is genuinely all-`V/iv`, or whether non-`V/iv` divergences (`V/VII`, and the agreeing
`V/v`, `viio7/V`, `V7/III` also seen in the same dump) were fully swept in the Step-M measurement — a
characterization-completeness check, not a defect.

### D3 — two incompatible "confidence" scales coexist (low-severity engage-time hazard)
`functionoutput.h` `FunctionConfidence.combined` is an **unbounded additive score** (Σ of three non-negative components
at default weight 1.0 — the output test asserts `5.0`), whereas `forwardoverride.h` treats `earlierConfidence` as
**clamped to [0,1]**. They are **currently disjoint** (the §8 override consumes `SliceConfidence.composite` /
`homeKeyConfidence`, never `FunctionConfidence.combined`), so no contract is violated. But the shared name "confidence"
across incompatible ranges is a latent hazard: if a future engage wiring ever feeds the §7 combined confidence into a §8
bar it would saturate at 1.0 and silently mis-scale the override. **Declare:** a scale-normalization (and/or naming)
decision to make at engage; flag the dual meaning now while it is cheap.

### Otherwise — a clean bill
No back-edge in the §8 closure (forward-only, re-entrancy-guarded — source + tests); reuse not duplicated; every L5 unit
dormant; default constants; corpus 53/24/53; the §7 contract and §5.x rules match the code. No contract the as-built
cannot honor was found; no reuse is subtly wrong; the spec does not assume anything the data contradicts beyond the two
already-recorded inference inputs.

---

## §6 — Gate (this round moves nothing in production)

| Check | Result |
|---|---|
| composing_tests | **974 PASSED** (+2: Evaded + cadence-pin), 2 disabled — no regressions |
| notation_tests | **53 PASSED**, 4 skipped (baseline) |
| pipeline_snapshot_tests | **11 PASSED**, 3 disabled — **NO golden refresh** |
| corpus BIR | **53 / 24 / 53** — manifests validated, containment-confirmed, byte-identical |
| dormancy | intact — zero `src/` production consumer (re-grep) |
| constants | default seeds unchanged (firewall) |
| `upstream` | not touched |

Tidies are **tests + one doc count only**; no production code, no constant/threshold, no inference fix, no golden
refresh.

---

## §7 — Deliverables

- **Commits (local, unpushed, on `master`):**
  - `4b8b0399be` — `test(function): add Evaded cadence + symmetric-rotation cadence-pin coverage`
  - `9d4c3fb363` — `docs(build): correct stale composing-test baseline 407 -> 974`
  - + the STATUS entry recording this round.
- **This report** — `cc_phase5c_L5_close_review.md` (gitignored).
- **Excluded from my commits:** `contrapunctus_findings.md` (a Cowork L6-research addendum, parallel work).
- **For Cowork to rule (declared, not acted):** D1 (fold the inert-guard proof into the verdict), D2 (regression-set
  completeness), D3 (engage-time confidence-scale/naming), and the §2 declared gap (whether to pin the `V/iv`
  over-trigger as a characterization test). Plus the §4 out-of-scope `analyze_inversion_errors.py` doc inconsistency.

**Bottom line:** L5 is **complete, correct, dormant, byte-identical** at the source level. The value of this round is the
three declared discoveries — chiefly **D1**, which converts the session-16 over-trigger *ruling* into a *source-level
proof* that the structural guard cannot help and inference is genuinely required.
