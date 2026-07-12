# CC — Layer-5 (function) certification audit, PASS 1, partition 1: the DORMANT RESOLVER pipeline

> **Session, 2026-07-12.** EG-7 / OI-84 / OI-116. Instruction:
> `cc_instruction_l5_audit_pass1_resolver.md` (Cowork, 2026-07-12), the first of three
> pass-1 partition sessions splitting the 3,372-deep-row L5+instruments inventory
> (`tools/audit/l5/`, frozen `0382c3275e`). This session dispositions the **L5-DORMANT**
> population — the built-but-unwired function pipeline the engagement will make production:
> **20 files, 815 deep rows.** READ-ONLY fact-finding; no production behaviour changed, no
> constant tuned, no golden refreshed; `tools/robust_stop/` and `tools/corpus/` untouched.
> Certification is **not** decided here (P8: certification needs both passes complete).

## 0. What this population is, and how it was audited

The L5-DORMANT population is the 10 module pairs (`.cpp`+`.h`) that implement the signed
Layer-5 function design (`cowork_layer5_function_design.md`, SIGNED 2026-06-26):

| module | design § | role |
|---|---|---|
| `functionromannumeral` | §5.1 | base Roman-numeral derivation (a faithful wrap of the one formatter) |
| `functionprogression` | §5.0 | the licensed-progression grammar — the **D5 grammar owner** |
| `functioncadence` | §5.2 | key-agnostic event-pair cadence detector |
| `functionmodulation` | §5.3/§5.4 | tonicization-vs-modulation arbiter + the §8 modulation recompute |
| `functionresolver` | §5.5 + §8 | resolve carried abstentions + the fine-grain override + bounded-context loop |
| `forwardoverride` | §8 | the ONE reusable confidence-weighted forward-override mechanism |
| `functionrelationallabel` | §5.6 | relational-label classifier (aug6/Neapolitan/applied/mixture) + unified applied emitter |
| `functionoutput` | §7 | output assembly (the L5→L6 contract) |
| `tonicizationlabeler` | §13 | the reused dormant applied-chord labeler |
| `progression/progressionrecognizer` | §4 (schema design) | progression-recognition consumer of the Harmonic Vocabulary |

**Method (protocol P1–P4).** The scope is the machine-generated inventory (not a chosen
sample): every deep row tagged L5-DORMANT in `tools/audit/l5/` (`file_table.csv`,
inventory `manifest.json`, `pass1_partition.json`). Row count cross-checked against the
partition: **815 rows** (functions 87, literals 183, branches 255, fields 225, decls 28,
io 0, crosslayer 37) — reconciles exactly with `pass1_partition.json`
(`L5-DORMANT: 815`). Each row received a verdict from the closed rubric (P2) via the
committed generator `tools/audit/l5/gen_resolver_dispositions.py`; findings are per-row
overrides, spelled out in §3. The negative-space direction (P3, spec→code) is §4. The
behavioural characterization (P4) is §5.

Scope reconciliation note: `harmonicfunctionlayer.{cpp,h}` sit in `analysis/function/`
but are tagged **L5-RETIRES** (the parent pass flagged them MIS-TAG — the legacy L4
chord-competition pipeline, not the L5 function machinery) and carry **0** deep rows in
the L5-DORMANT CSVs. Correctly outside this scope; verified at the file table.

## 1. Disposition summary (P2 — every one of 815 rows has a verdict)

Machine-tallied from `tools/audit/l5/pass1_dispositions_resolver.csv`:

| verdict | rows | meaning |
|---|---:|---|
| SURVIVES | 396 | functions / decls / crosslayer includes / branches: dormant, no production consumer, retained as engagement target |
| PUBLISHED | 225 | struct fields — on the dormant value/contract surface (read by tests + the engage consumer) |
| ESTABLISHED | 149 | literals: music-theory intervals, the octave modulus, array sizes, `[0,1]` clamps, zero/one identity defaults, the `1920.0` whole-note FACT, the `0.2` uniform idiom prior |
| UNFIT | 34 | firewall seeds: 28 named precision-phase param defaults + 6 inline §7 function-confidence magnitudes — hand-set "NOT tuned", declared |
| ASSUMPTION | 8 | flagged rows carrying an unratified/divergent premise (see §3) |
| FACT | 3 | the three §15-12 grammar motions — present and correct in code (flagged for a **doc**-staleness issue, §3) |
| **total** | **815** | |

**By dimension:** branch 255, field 225, literal 183, function 87, crosslayer 37, decl 28.
17 rows are flagged (§3). **No DEAD constant, no DUPLICATED fact, no backward (higher-layer)
include** was found. All 37 crosslayer includes are forward or lateral (external/std, or
L1–L4 + vocabulary/spelling substrate, or a sibling `function/` reuse) — consistent with the
§2 forward-only constraint.

**On the firewall seeds (UNFIT/34).** Every one is a declared precision-phase constant whose
*direction* is fixed by the design and whose *value* is a Stage-5 fit candidate. Only the
`forwardoverride` θ pair (`baseBar`, `confidenceScale`, forwardoverride.h:81-82) is registered
in `tools/param_manifest.json` (group G8, family θ, `consuming_path: dormant`). The other 28
named param defaults and the 6 inline confidence magnitudes are **not** in the manifest — see
finding *inline-function-confidence-magnitudes-unregistered* (§3) and the note there on the
broader registration gap.

## 2. Contract direction and the top-line finding

The dormant pipeline is a **faithful and near-complete** realization of the signed §1–§12
design. The base derivation (§5.1), the cadence typology (§5.2, all eight types), the
modulation hysteresis (§5.3) and its §8 recompute (§5.4), the six-ambiguity-kind resolver
(§5.5) with its §8 fine-grain override, the §5.6 relational-label precedence, the §5.7 soft
bass-degree prior, the §7 output assembly (including the D-L5a boundary-confidence squash),
and the §8 one-pass-closure/forward-recompute mechanism are all present and, where the design
fixes a direction, implemented in that direction. The §4 progression-recognition consumer and
the bounded-context forward-extension loop (companion designs) are likewise present and dormant.

The findings below are (a) three genuine code-vs-signed-design divergences, (b) five
documented/declared deferrals or scope limits I independently confirmed, and (c) one latent
edge and one registration gap. None changes production output (the whole population is dormant;
`src/` calls nothing here — confirmed by caller search, §5).

## 3. Every flagged row (file · line · one plain sentence)

Nine findings, 17 flagged rows. Slugs are plain-language descriptions (no invented numbering).

### 3a. Genuine code-vs-signed-design divergences

**(1) modulation-confirmation-admits-all-cadence-types** — `functionmodulation.cpp:52-60`
(also the enclosing `decideTonicizationVsModulation`).
The §5.3/§5.4 cadence-confirmation gate counts **any** `FunctionalCadence` whose `tonicPc`
and `minorMode` match the span and whose arrival falls inside it — it never checks
`c.type`. Both the signed design (§5.3(a): *"an authentic or half cadence whose tonic is the
candidate degree"*) and **this file's own header comment** restrict confirmation to an
authentic or half cadence. As coded, a **deceptive**, **plagal**, or **evaded** cadence with
a matching tonic would confirm a modulation — and a deceptive cadence by definition *denies*
the tonic arrival, so it is exactly the wrong evidence to confirm a key change. Dormant, so no
production effect; a real contract divergence to fix before engage. *(No test exercises a
non-authentic/half confirming cadence — see §5.)*

**(2) half-cadence-no-seventh-downweight** — `functioncadence.cpp:387` (in `tryHalf`).
§5.2 says a seventh (or inverted) dominant is *"admitted but at lower weight … a seventh …
weakens the reading — it is down-weighted, not excluded."* The code sets
`c.genuineDominant = false` **unconditionally** for every half cadence, so a seventh half and
a plain-triad half receive identical votes; there is no down-weight term at all. The code
comment even reads *"a seventh WEAKENS a half (not credited)"* — but *not credited* is neutral,
not weakening. The **direction** ("a seventh lowers a half's weight") is a fixed-direction
claim of §5.2, not a firewall magnitude, so its absence is a spec divergence, not deferred
tuning. Minor; dormant. *(Unimplemented ⇒ untested by construction.)*

**(3) grammar-amendment-landed-design-doc-stale** — `functionprogression.cpp:62,71,80`
(the three motion predicates) / `.h:164-182`.
`isAscendingFifth` (Δ7), `isDescendingSecond` (Δ10/11), and `isDiatonicDiminishedFifth`
(Δ6 into a diminished triad) — the three §15-12 grammar motions — are **implemented and
OR'd into `isLicensedProgression`**. Yet the signed design still describes the code as the
pre-amendment set: §5.0 *"Until that increment lands, the code implements the pre-amendment
set — a known, ruled spec-ahead-of-code state,"* and §15-12 *"the code increment is pending."*
The code is correct and complete; the **design document is stale relative to code**. Flagged
as verdict FACT (the code fact is right) with a doc-sync (#10) issue. *(Reconciled at unblind
— see §8; the code header and the D5 consistency test already treat the amendment as landed.)*

### 3b. Documented/declared deferrals and scope limits (independently confirmed)

**(4) applied-resolution-augmented-delta0-excluded** — `functionprogression.cpp:120-122`
(`isAppliedResolution`). The augmented→major/minor **same-root** (Δ0) resolution edge that
the legacy `resolutionEdgeBonus` carried is deliberately excluded (§5.0 licenses root
*motion*; Δ0 is no motion; an augmented triad is not an applied/leading-tone chord). The code
itself flags this to Cowork. An intentional, ruled scoping decision — recorded, not an error.

**(5) decision-context-stop-punctuation-boundary-subsumed** — `functionresolver.cpp:559-561,573`
(`isCutDecision`). The decision-context span has three stop conditions (bounded-context
design / L5 §5.0): (i) a cadence-anchored function, (ii) a punctuation boundary, (iii) the K/B
hard bound. The code implements (i) and (iii) and **folds (ii) into (i)** for the dormant
resolver ("a standalone L1.5 boundary tick is an engage input"). A documented
spec-ahead-of-code deferral of stop (ii); recorded.

**(6) modal-mixture-role-minor-key-incomplete** — `functionrelationallabel.cpp:196`
(`tryModalMixture`). The ModalMixture **role** is tagged only for a chromatic root, or (in an
Ionian key) a quality-altered diatonic degree. A quality-altered diatonic-root borrowing in a
**minor** key gets no role — though the emitted **label string** is always the formatter's
correct numeral. A documented scope limit, declared to Cowork. *(Untested branch — §5.)*

**(7) augmented-sixth-trigger-assumes-flat6-root** — `functionrelationallabel.cpp:118`
(`tryAugmentedSixth`). The aug6 trigger fires only when `identity.rootPc == tonic+8` (♭6̂). It
assumes Layer 4 roots an augmented-sixth sonority on the lowered submediant; aug6 chords have
a theoretically ambiguous root, so if L4 commits a different root the trigger silently does
not fire. An **input-contract assumption on the L4→L5 boundary** to validate at engage.

### 3c. Registration gap and latent edge

**(8) inline-function-confidence-magnitudes-unregistered** — `functionresolver.cpp:210,225,232,246,322,338`.
The emitted §7 `functionConfidence` magnitude (0.25 bass-degree prior · 0.5 neighbour-harmony
· 1.0 progression/cadence) is a **hand-set inline ordinal seed** not registered in
`tools/param_manifest.json`, unlike the `forwardoverride` θ pair which is. These are the §7
confidence the module publishes; they are precision-phase-appropriate given dormancy, but the
inconsistent registration means a Stage-5 fit sweep over the manifest would miss them. (The
same is true of the 28 named param defaults — only θ is registered; recorded for the manifest
owner.)

**(9) combined-boundary-no-kboundary-positivity-guard** — `functionoutput.cpp:131-132`.
`combinedBoundary = combined / (combined + kBoundary)` has no guard for `kBoundary <= 0`; with
`kBoundary = 0` and `combined = 0` it is `0/0` (NaN). The default `kBoundary = 1.0` is safe and
the path is dormant — a latent edge only if a future caller zeroes the seed. Very minor.

## 4. Spec → code, BOTH directions (protocol P3)

### 4a. Specified behaviour located in code (or its absence)

| design item | code home | status |
|---|---|---|
| §5.1 base RN = degree(root,key) + quality/inversion via the one formatter | `functionromannumeral.cpp deriveBaseRomanNumeral` | PRESENT (faithful wrap) |
| §5.0 licensed motions (pre-amendment 3) | `functionprogression` isDescendingFifth/Third, isAscendingSecond, isAppliedResolution | PRESENT |
| §5.0/§15-12 three added motions | isAscendingFifth/isDescendingSecond/isDiatonicDiminishedFifth | PRESENT (design doc stale — finding 3) |
| §5.0 prevailing harmony / established next / metrically-strong | prevailingHarmonyIndex / establishedNextFunctionIndex / isMetricallyStrong | PRESENT |
| §5.2 cadential-six-four collapse first | `tryAuthentic` sixFour branch | PRESENT |
| §5.2 authentic family gate (LT-resolves as event; seventh a strengthener) | `tryAuthentic` + isGenuineDominant | PRESENT |
| §5.2 perfect⟺bass 5̂→1̂ (both root position); imperfect the complement | `tryAuthentic` bassFiveToOne | PRESENT |
| §5.2 half / Phrygian / deceptive / plagal / evaded | tryHalf/tryDeceptive/tryPlagal/tryEvaded | PRESENT (half seventh down-weight ABSENT — finding 2) |
| §5.2 phrase-gate on the arrival | `arr.endsPhrase` in every type | PRESENT |
| §5.2 tonic-vote = monotone weighted sum − per-type discount | cadenceTonicVote | PRESENT |
| §5.3 default tonicization; modulation iff cadence-confirmed AND persists | decideTonicizationVsModulation | PARTIAL — confirmation admits all cadence types (finding 1) |
| §5.3 break-even → tonicization (strict inequality) | `persistenceEvidence > changeCost` | PRESENT |
| §5.3 notated-spelling signal as soft input to (b) | `wSpelling * spellingSupport` | PRESENT (but untested — §5) |
| §5.4 recompute via the §8 mechanism (localized/forward/closed) | modulationRecompute → OnePassClosure | PRESENT |
| §5.5 six ambiguity kinds, each by its rule | resolveAbstained switch | PRESENT (all six) |
| §5.5 case-4 fine-grain override (select, never re-derive) | attemptFineGrainOverride | PRESENT |
| §5.5 both-licensed → structural tie-break / open mark (§15-13) | bothLicensed telemetry + tieBreakOrOpen | PRESENT |
| §5.6 precedence aug6→Neapolitan→applied→mixture | classifyRelationalLabel | PRESENT |
| §5.6 general foreign-tone applied trigger + guard | emitAppliedLabel | PRESENT |
| §5.6 Ger6-vs-V7 by notated spelling (one spelling read) | augSixthSpellingSign via lineOfFifths | PRESENT |
| §5.7 soft bass-degree prior (never a gate) | degreeFunctionalBias / bassScaleDegreeBias | PRESENT |
| §7 verbatim carried-identity emit | carryThrough / override emits `chosen`/neighbour `chosen` | PRESENT |
| §7 confidence three fixed components + default combination | FunctionConfidence + assembleFunctionOutput | PRESENT |
| §7 D-L5a boundary form combined/(combined+k) | combinedBoundary | PRESENT (no k>0 guard — finding 9) |
| §8 four-case model; case-2/case-4 = one recompute | forwardoverride + resolver/modulation instances | PRESENT |
| §8 one-pass closure, grows-only, re-entrancy-refused | OnePassClosure | PRESENT |
| decision-context stop (ii) punctuation boundary | — | SUBSUMED into (i) (finding 5) |

### 4b. Code behaviour NOT in the signed §1–§12 body (the other direction)

Each is a **declared build-detail decision** in a companion design or the module header, not an
un-ratified surprise; recorded here for completeness so an unspecified behaviour in a dormant
pipeline is not carried silently:

- **The bounded-context forward-extension loop** (`resolveCarriedReadingsExtending`,
  `L5ForwardExtensionParams`, `clippedBySelectionEdge`/`cueDenied`) — specified in
  `cowork_bounded_context_design.md` §5, referenced by L5 §5.0. Dormant (default OFF ⇒
  byte-identical to the base resolver).
- **The `bothLicensed` telemetry field** — the §15-13 population diagnostic (fitter design
  §4.4 family 4); behaviour-neutral, read only by `--dump-fullspine`.
- **`roundCap = maxForwardExtendSlices + 4`** (`functionresolver.cpp:628`) — a "never-terminates"
  backstop; the `+4` margin is an implementation constant, not in any spec. Defensive; dormant.
- **The cadence-type priority order** authentic→deceptive→half→plagal→evaded
  (`detectFunctionalCadences`) — §5.2 does not fix an order; the code chose one and documents the
  types are "near-disjoint". Code-chosen, documented.
- **"Local key = the FIRST confirmed modulation"** (`assembleFunctionOutput`) — a declared
  build-detail decision; §7 says a region carries one local key.
- **The `tonicizationlabeler` diagnostic caller** — unlike the other modules (test-only), it is
  invoked by `tools/batch_analyze` as a read-only diagnostic; declared in its header.

## 5. Behavioural characterization (protocol P4) — test coverage of a dormant path

Production fire rates are **zero by construction**: a caller search over `src/` + `tools/`
(excluding the modules' own files) finds **no production `src/` consumer** of any L5-DORMANT
entry point. The only non-test caller is `tools/batch_analyze.cpp` (the diagnostic harness —
`--decode-chords`, `--dump-progressions`, `--dump-fullspine`, etc.). So characterization is via
the test suites, as the instruction directs; no production instrumentation is warranted.

`composing_tests.exe` (built at HEAD `d9c7ec6d2d`, corpus `c50002fee1`): **137 L5-DORMANT tests
across 11 suites, all PASS.** Per-module coverage:

| module | tests | branch coverage |
|---|---:|---|
| forwardoverride | 11 | monotone bar, tie-direction, fire-then-close, no-fire-below-bar, forward sweep, empty/inverted range refused, **nested-refused (−1)**, cannot-re-target-closed, reset — full OnePassClosure surface |
| functioncadence | 18 | all 8 types + cadential-6/4 + second-inversion-tonic rejection + key-agnostic-limit + phrase-gate + genuine-dominant + LT-resolves-as-event |
| functionprogression | 13 | all 7 licensed motions + same-root + missing-root + prevailing/established-next |
| functionrelationallabel | 22 | all 4 roles + full precedence + It/Fr/Ger + Ger-vs-V7 + the general/♭7̂/raised-LT guards |
| functionresolver | 26 | all 6 ambiguity kinds + both-licensed + fine-grain override (fires / doesn't on a very confident commit) + verbatim carry + all 7 bounded-context (L5EXT) paths |
| functionoutput | 9 | resolved/undecided units, licensed-fit 0/1, modulation vs home key, additive carry, boundary squash |
| functionmodulation | 6 | cadenceless→tonicization, confirmed-persistent→modulate+recompute, break-even→tonicization, relative-pair, recompute-closure-no-reopen, detector-substrate reuse |
| functionromannumeral | 7 | diatonic/seventh/chromatic + wrap-reproduces-formatter + empty |
| tonicizationlabeler | 9 | applied dominant/LT (triad/7) + chromatic guard + diatonic/tonic/deceptive/non-diatonic rejections |
| progressionrecognizer | 15 (+1 D5) | recognise + tritone-sub + sequence + mixture-blend + prior-max + admission + mode/chords-only factors + abstained/committed evidence + D5 catalog-consistency |

**Branches no test reaches (findings of their own rank):**
- **The §5.3 notated-spelling term** (`wSpelling * spellingSupport`, functionmodulation) — **no
  test** supplies a non-empty `spellingSupport`; every modulation test leaves it false. The
  spelling-support arm of the persistence evidence is **untested**.
- **A non-authentic/half confirming cadence in the modulation gate** — every FunctionModulation
  test uses `PerfectAuthentic`; the (over-permissive) admission of other cadence types (finding
  1) is untested, so the divergence is invisible to the suite.
- **The half-cadence seventh/inversion down-weight** (finding 2) — unimplemented, hence
  untested by construction.
- **The minor-key modal-mixture role** (finding 6) — unimplemented for that case, untested.
- **The progressionrecognizer committed-override contribution** is **structurally inert under
  the exact-match v1 recogniser** (a literal member equals the committed reading by
  construction); the tests confirm this (`ExactMatchProducesNoCommittedOverride`) and exercise
  the assembler directly (`CommittedOverrideContributionCarriesFBSemantics`) — built ahead for
  the Stage-5 partial matcher, documented.

## 6. When each withheld file was first opened

- **At session start (declared exception, safe read):** `cowork_layer5_function_design.md` —
  the signed design specification of exactly this pipeline (the P3 contract). Read in full.
- **Safe reads throughout:** `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`,
  `ARCHITECTURE.md` (as needed), `docs/scoring_model.md` (as needed), the raw inventory tables +
  `manifest.json`/`pass1_partition.json` under `tools/audit/l5/`, `tools/param_manifest.json`,
  and the source code.
- **No withheld file was opened before the Task-3 freeze commit.** (`DEFECT_TYPES.md`,
  `OPEN_ITEMS.md`, `STATUS.md`, `cowork_handoff.md`, every `cc_*_report.md`, and the audit-era
  `cowork_*` dossiers remained closed through the blind pass.)
- **After the freeze (Task 4):** *(filled at unblind — §8.)*

## 7. Self-check (CLAUDE.md, mandatory)

Ran over every touched file's diff before reporting: the generator
`gen_resolver_dispositions.py`, the two generated artifacts, this report. No production code,
no scoring constant, no golden, no corpus, no `robust_stop` artifact touched. The UNFIT
auto-detection was tightened after a self-check caught 7 over-catches (structural zero-inits /
indicator literals on lines that merely mention a param name); every UNFIT row now is a param
**initializer** or an inline confidence magnitude, hand-verified against source. Row total 815
reconciles to the partition. No self-invented numbering scheme (findings are plain-language
slugs). No inference-problem-driven change (read-only audit).

## 8. Unblind & reconcile (Task 4)

*(This section is filled after the Task-3 freeze commit, which lifts the withheld list.)*
