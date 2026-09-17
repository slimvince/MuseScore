# CC report — §15-12 grammar completion (+ the ripple ruling, executed)

**Status: COMPLETE — suites green, gate 53/24/53 set-identical, ready to commit.** The ratified §15-12 grammar
completion is implemented; the build then surfaced a **carry-contract surprise** (6 sibling-L5 consumer tests broke),
which I raised as a STOP (§2 below). Cowork ruled on it in `cc_instruction_grammar_completion_addendum.md` (2026-07-03)
— **no production/sibling-code changes; the both-licensed outcomes are the spec's firewall-era behaviour; the
preference-order remedy is deferred to Stage-5 / L5 §15-13**. I executed that ruling (Tasks A/B/C, §5 below): the
sibling-consumer TESTS are re-pointed/re-picked to preserve their subjects, two new both-licensed pins are added, and
one coupling-map clarification line is added at the grammar owner. All acceptance items met.

- HEAD at start: `1d23be8984` (`feat(tools): --dump-progressions + compare_progressions_oracle`).
- Suites: `composing_tests` **1056/1056**; `notation_tests` **53 pass / 4 pre-existing skips / 0 fail**;
  `pipeline_snapshot_tests` **11 pass / 1 skip / 3 disabled / 0 fail, NO golden refresh**.
- Gate (3-preset regen at HEAD `1d23be8984`, corpus 352/352): **Baroque 53 / Jazz 24 / Default 53, case-identity
  sets byte-identical** to the CLAUDE.md gate (set-diff empty both directions, all three presets). The Default set is
  thereby re-confirmed = Baroque-53 with `{bwv352@1440, bwv60.5@30960}` → `{bwv227.7@18000, bwv387@10560}` (resolving
  the CLAUDE.md "re-confirm at next regen" caveat).
- Dormancy re-proven: the three new predicates are referenced only in `functionprogression.{h,cpp}` + its test; no
  new production call site (grep). Production chord path uses `harmonicfunctionlayer`, not the new L5 stack.

---

## 1. What was implemented (Task 1 + Task 2 — the named scope, complete and green)

### Grammar (`analysis/function/functionprogression.{h,cpp}`) — the one grammar owner

Three new licensing sub-predicates, OR'd into `isLicensedProgression`, per the ratified §5.0 / §15-12 enumeration
(`cowork_layer5_function_design.md` §5.0 amendment block, lines ~203–226; §15-12, lines ~877–888):

| New predicate | Rule | Clears (of the 11 known gaps) |
|---|---|---|
| `isAscendingFifth(from,to)` | `rootMotion == 7`, unconditional on quality | I→V, IV→I, vi→iii → 7 motions (Plagal#0, Axis#0, Pachelbel#0/#2/#4, Romanesca#0/#2) |
| `isDescendingSecond(from,to)` | `rootMotion ∈ {10,11}`, unconditional | i→♭VII, ♭VII→♭VI, ♭VI→V → 3 motions (Andalusian#0/#1/#2) |
| `isDiatonicDiminishedFifth(from,to)` | `rootMotion == 6` **AND** `to.quality == Diminished` | IV→viiᵒ → 1 motion (Circle-of-fifths-full#1) |

Total = 11 = exactly the ruled known-gap set. Verified pair-by-pair against the actual catalog entries
(`harmonicvocabulary.cpp:237,267–269,283–284,287,289–291,300`): every *other* adjacent pair of those six entries is
already Δ5/Δ2/Δ8/Δ1 (licensed pre-amendment), so the three predicates clear exactly the 11, no more, no less.

**Reuse vs new:** the three predicates reuse the existing `rootMotion()` helper (`functionprogression.cpp:30`). They
are **new** boolean licensing tests with **no scoring-bonus analogue** — that is the point of §15-12 (the
pre-amendment set descended from wSeq/wDim/resolutionEdge bonuses and omitted these). The delta-6 realisation is the
amendment's "diatonic" qualifier made operational: a **bare** Δ6 license was explicitly NOT wanted (it would license
generic tritone root motion the grammar has never licensed), so it is gated on `to.quality == Diminished`. If Cowork
intended a different shape here, this is the one realisation choice to confirm — I did not choose a different shape
silently.

**Comment blocks updated (mandatory sync):**
- `functionprogression.h`: the REUSE note (now records the three no-bonus-analogue additions), the
  `isLicensedProgression` doc enumeration, and the D5-dependency-map "RULED KNOWN GAPS" note (marked ★ CLOSED by
  §15-12, 2026-07-03, historical note retained).
- `harmonicvocabulary.h`: the mirrored D5-dependency-map "RULED KNOWN GAPS" note (same ★ CLOSED marking + dating;
  records that no catalog edit was needed).

### Tests in the named scope (both green)

- `functionprogression_tests.cpp`: added `Ab=8`; three must-license tests (`AscendingFifthIsLicensed`,
  `DescendingSecondIsLicensed`, `DiatonicDiminishedFifthIsLicensedOnlyIntoADiminishedTriad`) covering I→V, IV→I,
  vi→iii, i→♭VII, ♭VII→♭VI, ♭VI→V, IV→viiᵒ; and the Δ6 quality condition tested **both** ways (Dim arrival licensed;
  Major and HalfDiminished arrivals not licensed). All existing negative controls stay green (the pre-existing
  `NonFunctionalTritoneLeapIsNotLicensed` C→F#(Major) is exactly the "Δ6 into a non-diminished arrival stays
  unlicensed" control — unchanged, still red-lines a bare tritone).
- `progressionrecognizer_tests.cpp`: the D5 consistency test **tightened to the clean invariant** — `knownGaps`
  list **deleted** (no vestigial list), renamed `EveryCatalogPairIsLicensed`, asserts `failing.empty()` with a
  per-offender named `ADD_FAILURE`. **PASSES** — confirming the three predicates license all 11 formerly-failing
  pairs and introduce no new failure.

**Named-scope test result:** `FunctionProgression.*` (13) green; `ProgressionRecognizerD5Consistency.*` green.

**What retires:** only the `knownGaps` list (deleted, as designed). Nothing else retires.

---

## 2. The carry-contract surprise (the STOP)

`composing_tests`: **1048 / 1054 pass; 6 FAIL**, all in Layer-5 sibling modules that consume
`isLicensedProgression` directly. The dispatch's D5 dependency map says: *"the grammar has ONE owner … Change that
module only … the only coupling is the one-way consistency test."* That is **incomplete** — grep of `src/` shows
four in-layer consumers of the grammar besides the D5 test: `functionresolver.cpp`, `functionoutput.cpp`,
`functioncadence.cpp` (and the resolver's `plausibility()` fit term). Their oracle fixtures were built against the
**narrower pre-amendment** licensed set; completing the grammar changes what they observe.

### Failure class (a) — definitional fit propagation (2 tests, mechanically repairable)

Both **explicitly premised on "ascending fifth (+7) = unlicensed"** — the exact motion §15-12 licenses first:
- `FunctionOutput.LicensedFitZeroForUnlicensedMotion` (`functionoutput_tests.cpp:110–123`) — comment (line 112):
  *"An ascending perfect fifth C→G (delta 7) … is NOT in §5.0's enumerated licensed set."* Now `licensedProgressionFit`
  is **1.0** (was 0.0). The test's whole purpose is now inverted.
- `FunctionOutput.CombinedBoundaryIsSquashedToUnitIntervalAndMonotone` (`functionoutput_tests.cpp:255–283`) — sweeps
  confidence with roots stepping by +7 *specifically to keep fit 0* (line 253/263). Now fit=1 shifts `combined`
  upward, breaking the pinned equalities.

These are repairable by swapping the fixtures' "unlicensed example" to a still-unlicensed motion (e.g. a genuine
tritone into a non-diminished arrival). But see §3 — I did not, deliberately.

### Failure class (b) — resolver disambiguation loses its uniqueness (4 tests, a DESIGN consequence)

The §5.5 resolver disambiguates a carried/abstained reading by selecting the rotation whose motion into the next
function is **uniquely** licensed: `functionresolver.cpp:221–224` and `241–245` both gate on `if (aIn != bIn)`. The
amendment makes the **competing** rotation's motion licensed too, so `aIn == bIn` now → the rule no longer fires →
the resolver falls through to tie-break / neighbour / **open**. Confirmed at the fixtures:

- `FunctionResolver.ShareTone_ResolvedByLicensedProgressionIntoNext` (`:135–154`) — fixture ii→{Am6 ↔ F#ø7}→V; the
  comment (line 137) relies on *"Am6→G (a descending whole step) is not licensed."* It now **is** (Δ10 descending
  second) → both rotations licensed → resolves **open** (was: F#ø7 via `Progression`). Expected `resolved=true,
  rootPc=Fs, basis=Progression`; got `resolved=false, openMark=true, rootPc=A, basis=None`.
- `FunctionResolver.Transition_ResolvedAsArrivingFunction` (`:156–174`) — fixture I→{D7 ↔ C}→V; relied on *"C→G
  ascending fifth not licensed."* Now licensed (Δ7) → both licensed → picks the prevailing-C reading instead of the
  arriving D7. Expected `rootPc=D, basis=Progression`; got `rootPc=C, basis≈NeighbourHarmony`.
- `FunctionResolver.L5EXT2_CutAbstain_RequestFiresAndResolves` (`:582–583`) — the same F#ø7 share-tone mechanism via
  the cut-abstain extension; the extension's headline capability ("resolved by licensed progression into V") no
  longer fires.
- `FunctionResolver.L5EXT5_ForwardExtension_DoesNotReopenClosedDecision` (`:637`) — same mechanism; the previously
  resolved reading is now open.

**Why this is a STOP, not a chore:** these four are **not** oracle-number updates. Their subject *is* the
disambiguation, and the amendment removes the uniqueness it stood on. To "fix" them I would either (i) rewrite the
oracles to bless the new open/flipped outcomes — ratifying an L5-resolver behavioural change by fiat (the forbidden
inference-driven coding), or (ii) re-pick fixtures that stay uniquely-licensed — changing what the tests
demonstrate. Both are Layer-5 **design** judgments Cowork owns, not local mechanical repairs.

**The architectural insight to surface:** once the grammar is *complete*, the resolver's **binary** use of
`isLicensedProgression` for disambiguation is weaker — more motions licensed ⇒ fewer unique-licensed splits. §5.0
itself anticipates the remedy: *"the numeric preference among licensed readings is a precision-phase weight."* The
resolver may need to disambiguate by a **preference/strength among licensed motions** (e.g. descending-fifth ≻
descending-second), not by binary licensed-uniqueness. That is a Layer-5 resolver design decision — flagged, not
taken.

---

## 3. Production dormancy (unaffected — the ripple is confined to the dormant L5 *test* surface)

The **production** chord path does not reach the new L5 stack: `chordanalyzer.cpp:25`, `regionanalyzer.cpp:44`,
`chorddiagnose.cpp:24` include only `harmonicfunctionlayer.h` (the old competition pipeline) — **not**
`functionresolver/output/progression`. `batch_analyze.cpp:101–104` links the L5 modules only for the diagnostic
`--dump-l5` / `--dump-fullspine` flags, which the gate corpus does not use. So the BIR gate and the pipeline
snapshots are architecturally untouched; the 6 failures are entirely within the **dormant L5 sibling unit tests**.

I have **not** run the 3-preset gate corpus regen yet: acceptance ("suites green, no refresh") is unreachable while
the suite is red, and the gate proof is moot until the ripple's disposition is ruled. I can run it as confirmation
of 53/24/53 on request — the architectural evidence above says it will be byte-identical.

I have **not** committed, and have **not** touched: `functionresolver.{h,cpp}`, `functionoutput.{h,cpp}`,
`functioncadence.{h,cpp}`, `functionresolver_tests.cpp`, `functionoutput_tests.cpp`, or the docs rider.

---

## 4. The ruling I need from Cowork

The grammar completion is correct and ratified; the question is the **disposition of the sibling-L5 ripple** the
dispatch's coupling map did not anticipate. Options:

- **A — I repair class (a) [2 fit tests] within this increment, and Cowork rules on class (b) [4 resolver tests].**
  Class (a) is pure definitional (swap the "unlicensed example" to a genuine tritone); class (b) is the design
  question (does the resolver disambiguation need a licensed-motion *preference* now that the grammar is complete?).
- **B — Cowork rules on the whole ripple as one; I make no sibling-module edits until told the intended new
  resolver semantics** (keep binary-uniqueness and accept the new opens as correct, vs. add a preference order).
- **C — Cowork amends the increment scope** to include the sibling-consumer updates explicitly, with the intended
  new-behaviour oracle for the 4 resolver tests specified, and I implement to that.

My recommendation: **B**, because the 4 resolver failures encode a real semantic decision (binary-licensed vs
preference-among-licensed) that belongs to the L5 resolver design, and even the 2 "trivial" fit tests may be better
turned into *positive* assertions of the new licensing than re-pointed at a tritone — Cowork's call. Nothing is
committed; I await the ruling.

---

## 5. Ruling executed (`cc_instruction_grammar_completion_addendum.md`, 2026-07-03)

Cowork ruled **B** in substance: **no production/sibling-module code changes** — the both-licensed → open/neighbour
outcomes are the signed spec's firewall-era behaviour (§5.0: *"the numeric preference among licensed readings is a
precision-phase weight; the licensing itself is the rule here"*), not a regression; the preference-order remedy is
**deferred to Stage-5 weight fitting** (recorded L5 §15-13, with a new §5.5 "both-licensed case" note — both already
in the docs rider). Verified at source: the §5.5 rules select by the progression test **only where it separates**
(`functionresolver.cpp` — the `if (aIn != bIn)` arms at the TransitionVsContinuation/ShareTone cases); where the
completed grammar licenses both, the case falls to the structural tie-breaks / honest open mark.

**Task A — the 2 `FunctionOutput` fit tests (mechanical re-point).** Re-pointed each fixture's "unlicensed example"
from the now-licensed ascending fifth (Δ7) to a still-unlicensed **ascending major third (Δ4)**; each test's subject
is unchanged (fit = 0 for an unlicensed motion; the boundary squash's monotonic sweep):

| Test | old motion | new motion | subject preserved |
|---|---|---|---|
| `LicensedFitZeroForUnlicensedMotion` | C→G (Δ7, now licensed) | C→E, I→iii (Δ4) | fit == 0.0 |
| `CombinedBoundaryIsSquashedToUnitIntervalAndMonotone` | root step +7 | root step +4 | combined == resolverConf, monotone squash |

**Task B — the 4 `FunctionResolver` tests (subject-preserving re-pick) + 2 new both-licensed pins.**

*Disambiguation-subject tests* — re-picked so exactly ONE reading is licensed into the next under the completed
grammar (unique-licensing arm preserved), same winner assertions:

| Test | old fixture | new fixture | why unique now |
|---|---|---|---|
| `ShareTone_ResolvedByLicensedProgressionIntoNext` | ii→{Am6↔F#ø7}→**V(G)** | ii→{Am6↔F#ø7}→**E♭** | F#ø7→E♭ Δ9 licensed; Am6→E♭ Δ6-into-non-dim not → winner F#ø7 (unchanged) |
| `Transition_ResolvedAsArrivingFunction` | I(C)→{D7↔C}→V(G) | **iii(Em)**→{D↔**E**}→V(G) | D→G Δ5 licensed; E→G Δ3 not → winner D (unchanged) |

*New both-licensed pins* (use the OLD fixtures, now both-licensed by construction; cite L5 §5.5 both-licensed note +
§15-13; expected to be deliberately revisited at Stage-5):

- `ShareTone_BothLicensedCarriesOpenMark` — ii→{Am6↔F#ø7}→V: F#ø7→G Δ1 **and** Am6→G Δ10 both licensed; no §5.7
  bass-prior split (bass A = 6̂ → no lean) → `resolved=false, openMark=true, basis=None`.
- `Transition_BothLicensedResolvesAsNeighbourWithinPrevailing` — I→{D7↔C}→V: D→G Δ5 **and** C→G Δ7 both licensed →
  falls to the passing/neighbour arm, the reading matching prevailing I (C) selected → `NeighbourHarmony`, conf 0.5.

*Extension-mechanics tests* — the share-tone was only the vehicle; re-pointed the forward function G→**E♭** so the
capability each demonstrates stays a *resolving* case (winner F#ø7 unchanged):

| Test | old→new vehicle | subject preserved |
|---|---|---|
| `L5EXT2_CutAbstain_RequestFiresAndResolves` | forward V(G) → **E♭** | cut abstain fires AND resolves (→ F#ø7) |
| `L5EXT5_ForwardExtension_DoesNotReopenClosedDecision` | interior V(G) + forward V(G) → **E♭** | closed interior decision not re-opened; edge finalized |

(`L5EXT1/3/4/6/7` untouched — they assert OFF-equality / refusal / boundary / determinism / fresh-run equivalence,
all invariant to whether the share-tone resolves or opens, and stay green.)

**Task C — coupling-map clarification (at the owner).** Added one bullet to the `functionprogression.h` D5
dependency-map block: the "only coupling" statement governs the **catalog↔grammar** relationship; the in-layer
consumers (`functionresolver`, `functionoutput`, `functioncadence`) are ordinary same-layer callers expected to move
with the grammar (mirrored nothing into `harmonicvocabulary.h`, per the ruling).

**Reuse-vs-new / what retires:** unchanged from §1 — the three predicates reuse `rootMotion()`, are new licensing
booleans; the only removal is the `knownGaps` list (deleted). The ruling adds no production code and retires nothing
further; the sibling-consumer edits are test-only.
