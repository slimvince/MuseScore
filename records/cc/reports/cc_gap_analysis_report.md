# CC gap-analysis report — implementation ↔ spec, plus the seven review riders

> **Run type:** READ-ONLY audit. No production edit, no golden refresh, no corpus regen, no commit.
> **Instruction:** `cc_instruction_gap_analysis_spec_vs_impl.md` (this file's dispatch), post-E0″ revalidation (2026-07-02).
> **HEAD:** `5f7cb7376e8d653c268496d56a6f7483fc4ae214` (local, unpushed E0-arc tip).
> **Baseline (run from existing binaries, this run):** composing **998/998 PASSED** (2 disabled); notation
> **53/53 PASSED** (57 total, 4 skipped); pipeline_snapshot **11/11 PASSED** (1 skipped, 3 disabled). All green.
> **Gate:** BIR case-identity Baroque 53 / Jazz 24 / Default 53 (unchanged; not re-measured — nothing changed).
> **Method:** each layer/spec walked §-by-§ against source by a dedicated read-only auditor; every claim carries a
> file:line; load-bearing rider claims independently re-verified by CC at source (marked ✔CC below). Rows never
> asserted from memory; unverifiable items are in §5 Unknowns, not guessed.

**Verdict legend.** Status ∈ {FAITHFUL, DEVIATION, MISSING, EXTRA}. Verdict ∈ {SPEC-RIGHT/CODE-GAP (code must
change later), CODE-RIGHT/SPEC-STALE (doc must change later), UNDECIDABLE (needs a Cowork/user ruling — question
stated), N/A-faithful}. "Dormant" = the module has no production consumer (byte-identical by construction); dormancy
is a property, **not** a gap. The whole L4-decoder + L5-function spine is dormant: the only non-test caller of
`ChordSliceDecoder` / `detectFunctionalCadences` / `resolveCarriedReadings` is `tools/batch_analyze.cpp` (✔CC grep,
this run) — production is L2→L3 in `regionanalyzer.cpp` only.

---

## §0. Headline results (the five spec-level claims the architecture review leaned on + the two new riders)

| Rider | Claim under test | Result |
|---|---|---|
| **1** | No production back-edge anywhere in the rebuilt spine | **CONFIRMED — no back-edge.** Every cross-layer call is data-supply-down (to L1/shared primitives/type-headers), intra-layer, forward, or the §8 forward-override (forward + re-entrancy-guarded + selection-only). ✔CC |
| **2** | L4→L5 carried-readings contract fully populated | **CONFIRMED with one qualification:** `alternatives` + `confidenceModel` populated on every decision kind; topK cap + sibling-exclusion + lock-in test present. **Qualification:** 2 of 6 `AmbiguityKind` values (`SymmetricRotation`, `CloseReading`) have code sites but no lock-in test, `SymmetricRotation`'s only live trigger is augmented-only (dim7 deferred to G5), `NoteMembership` is reserved/never populated. |
| **3** | The §8 override sites' actual confidence scales | **CONFIRMED (D-FS live).** F-A incumbent `homeKeyConfidence` [0,1] vs contradiction `cadentialWeight` **unbounded**; F-B incumbent `s.confidence.composite` [0,1] vs contradiction `bestPlaus−committedPlaus` **unbounded**. Only squash is the defensive clamp on `earlierConfidence` inside `overrideBar`. ✔CC — the code is already annotated with the contract's frame names. |
| **4** | The three cadence implementations' call graphs | **CONFIRMED.** Legacy `detectCadences`/`detectPivotChords` = the only cadence functions with **production** callers (notation bridges); `cadencekeyanchor` + L5 `functioncadence` = tools+tests only. Grounds R2 (retire legacy — needs bridge migration first) and R3 (keep anchor as diagnostic). |
| **5** | B-swap readiness (producer-agnostic seams) | **CONFIRMED.** `decideSlice` scorer-independent; L5 units hand-injectable over POD views; Vocabulary calls back into no decision layer. One intended (not accidental) entanglement: `functionrelationallabel` binds the shared spelling interpreter + `formatRomanNumeral` by design. |
| **6** | Confidence inventory (A-1 §3 close-out) | **DELIVERED (§3 below).** Both L3 numbers confirmed co-existing (D-L3a). One correction to the auditor: the `0.5` legacy sentinel **does** exist — `regionanalyzer.cpp:393` `kJointModulationFallbackConfidence = 0.5` ✔CC (the auditor searched only keyresolver/keymodeanalyzer). |
| **7** | Systematic projection sweep (carry-gap class closure) | **CONFIRMED — no CANDIDATE-GAP.** 10 projection sites enumerated (inter- + intra-layer). The two structurally load-bearing ones (L4→L5 cell carry; L5 resolver `toPC`) are exactly the recent carry-fix sites (`4b3d054d89`, `3aaa2cbd63`) and are now covered (honest-carry `extensionsKnown` flag; verbatim `chosen`/`reading` emit path). |

**Net:** the architecture-review's spec-level claims hold at source. No highest-severity finding (no back-edge; no
undeclared carry-gap). The residue is (a) a cluster of spec-deferred-by-design MISSING rows, (b) a handful of
UNDECIDABLE spec-vs-code ambiguities, (c) pervasive stale line-number citations in the L2/L3 specs, and (d) the
already-declared D-FS commensurability gap (Stage-5 calibration, not a code bug now).

---

## §1. Per-layer gap tables

### §1.1 Layer 1 — note model (`cowork_layer1_note_model_design.md`)

| Spec § | Rule (short) | Code site | Status | Tested? | Verdict |
|---|---|---|---|---|---|
| §1/§4/§9 | Tie-resolved: tied group = ONE note (first onset→last release) | note_model.cpp:181-196; dur via `playTicksFraction()` :60-61 | FAITHFUL | T1_TieAcrossBarline, T2, T3 | N/A |
| §1 | Slurred notes NOT merged (only ties) | only `tieBack()` special-cased :181,190 | FAITHFUL | NONE | N/A (faithful-by-omission) |
| §1/§5/§4 | Lossless: keep every note, mark never drop | :146-150 `consider` keeps all | FAITHFUL | T4/T7/T8 | N/A |
| §1/§7 | Keep-but-mark flags plays/visible/staffEligible | :63-65,163 | FAITHFUL | T7,T8 | N/A |
| §3/§9/§2 | "Sounding during A–B" overlap, NO backward horizon (old 4-whole cap killed) | overlapping() :307-325; note_model.h:46-47 | FAITHFUL | T3, IDX1/3, T12 | N/A |
| §3 | "Which notes start within A–B?" onsetIn | :327-342 | FAITHFUL | transitive only; **no dedicated onsetIn test** | UNDECIDABLE (§10 branch-coverage: is transitive use enough?) |
| §3/§5 | Numeric index (onset array + max-release segment tree) | NoteQueryIndex :239-305 | FAITHFUL | IDX1-4 | N/A |
| §3/§9 | extend(dir,int) append-only, one step, clamp+report | :204-237 | FAITHFUL | EXT1-7 | N/A (dormant — no layer calls extend()) |
| §3/§11 | Interim: build re-walks whole score even for a selection | :89-97,118-202 | FAITHFUL (spec §11 discloses the debt) | EXT2/3 | N/A |
| §7 | 11 fields per NoteEvent | note_model.h:80-92 | FAITHFUL | field checks T4-8 | N/A |
| §13 | `isCue` specced then REMOVED (`plays` subsumes) | note_model.h:71-79 | FAITHFUL | — | N/A (code+spec agree) |
| §6/§8 | Grace kept, flagged, parent tick | :176-186 | FAITHFUL | T4 | N/A |
| §5/§1 | Derived summary views = separate lossy module on top | regiontonecollector.cpp:44,87-90 | FAITHFUL | T9-14 | N/A |

**L1 rows: 15 FAITHFUL / 0 DEVIATION / 0 MISSING / 0 EXTRA** (one UNDECIDABLE is a coverage question, not a behavior gap).

### §1.2 Layer 1.5 — phrase boundary + spelling view (`cowork_phrase_boundary_design.md`)

| Spec § | Rule (short) | Code site | Status | Tested? | Verdict |
|---|---|---|---|---|---|
| §4.1 | Three cue profiles (gap, inter-onset, pitch-interval) | phraseboundaryview.cpp:315-323 | FAITHFUL | LocalChange_*, oracle | N/A |
| §4.1 | Local-change rule `x·(leftRatio+rightRatio)`, ratio `|a−b|/(a+b)` | :222-241 | FAITHFUL | ChangeRatio_basics, LocalChange_* | N/A |
| §4.1 | Max-normalise each cue | :338-356 normalizeAcrossVoices | **DEVIATION (subtle)** | MaxNormalize (helper only) | **UNDECIDABLE** — §4.1 says "per-score maximum", §4.3 says "across all voices"; code normalises across voices. Spec-internal contradiction; which reading is canonical? The standalone `maxNormalizeInPlace` (:243) is **unused** by the pipeline. |
| §4.1 | Combined = gap-dominant weighted sum | :368-370; defaults .50/.30/.20 | FAITHFUL | PerVoiceAggregatesIntoTexture | N/A |
| §4.2 | Marker spikes after combine, height>max surface | :411-440; 1.5× ceiling | FAITHFUL | Chorale_fermata*, finalBarline | N/A |
| §4.2 | Fermata marker | :113 isFermata | FAITHFUL | Chorale_fermata* | N/A |
| §4.2 | Breath/caesura marker | :120-128 | FAITHFUL | **NONE** | SPEC-RIGHT/CODE-GAP (coverage only — code present) |
| §4.2 | Double/final/repeat barline marker | :162-171 | FAITHFUL | Chorale_finalBarline | N/A |
| §4.2 | Mid-score key-sig CHANGE (engraved, not inferred) | :130-159 (reads concertKey) | FAITHFUL | **NONE** | SPEC-RIGHT/CODE-GAP (coverage only) |
| §4.2 | Subito tempo change / written ritardando | :113,176-195 | DEVIATION | NONE | CODE-RIGHT/SPEC-STALE — fires at ANY tempo tick incl. opening (disclosed §11-2b; inert while dormant) |
| §4.2 | All-voice-rest onset marker (empty slice ≥ min-silence) | :199-213 | FAITHFUL | RestFixture_producesABoundary | N/A |
| §4.2 | Fermata/breath "on an ELIGIBLE voice" | :93-97,113 — eligibility NOT applied | DEVIATION | NONE | CODE-RIGHT/SPEC-STALE (disclosed §11-2b; harmless on chorales; inert dormant) |
| §4.3 | Cues per eligible voice; eligibility=plays&visible&staffEligible | :61-86 | FAITHFUL | PerVoiceAggregates | N/A |
| §4.3 | Texture strength = Σ per-voice per τ-merged onset | :378-402 | FAITHFUL | PerVoiceAggregates | N/A |
| §4.3 | Expose BOTH per-voice + texture profiles | phraseboundaryview.h:132-137 | FAITHFUL | PerVoiceAggregates | N/A |
| §4.4 | Peak-pick: local max AND >mean+k·SD | :257-281 | FAITHFUL | PickPeaks_* | N/A |
| §4.4 | Markers emitted UNCONDITIONALLY (union), not threshold-gated | :454-456 | FAITHFUL | Chorale_finalBarline, pickSet | N/A (as-built ratified 2026-06-26) |
| §4.5/§2 | Excluded: cadence/harmonic-rhythm/inferred-key (acyclicity) | no such reads in the file | FAITHFUL | NullScoreIsSafe smoke | N/A |
| §11-5 | Per-part vs global marker scope; provenance | not built (scope-blind pickedTicks) | MISSING | NONE | N/A (spec §11-5 explicitly defers to inference phase) |
| **Spelling view** §per-note | lineOfFifths = tpc−TPC_C; presence via `tpcIsValid()` not `>=0` | spellingview.cpp:36-42 | FAITHFUL | LineOfFifthsIsTpcMinusTpcC, FlatSide*, InvalidTpc*, GSharpAFlat | N/A (flat-side trap avoided) |
| **Spelling view** §per-note | sharpFlatSense = sign of LoF | :44-51 | FAITHFUL | SharpFlatSenseIsSign* | N/A |
| **Spelling view** §span | spanSpelling centroid + distribution, signature-agnostic | :53-76 | FAITHFUL | SpanAggregateMatchesHandComputed | N/A |
| **Spelling view** capability | Only consumer = dormant L4 pin; legacy tpc reader coexists (fold not done) | spellingview.h:44-49 | FAITHFUL | — | N/A (dormancy; the tpc-fold is R4/E4) |

**L1.5 rows: 18 FAITHFUL / 3 DEVIATION / 1 MISSING / 0 EXTRA.** 2 of 3 DEVIATIONs are self-disclosed §11-2b
first-cut simplifications (SPEC-STALE, inert while dormant); the normalization DEVIATION is a genuine spec-internal
contradiction (UNDECIDABLE).

### §1.3 Layer 2 — slicing (`cowork_layer2_slicing_design.md`)

| Spec § | Rule (short) | Code site | Status | Tested? | Verdict |
|---|---|---|---|---|---|
| §4/§5.1/§9 | Boundary at every eligible onset AND release | slicer.cpp:39-49 | FAITHFUL | slicer_tests S1,S4 | N/A |
| §2/§4/§8 | Zero interpretation (no thresholds/smoothing/merge/note-kind casing) | :44-46 | FAITHFUL | S5 grace | N/A |
| §2/§5 | Consumes L1 eligibility; never re-decides | :40 | FAITHFUL | S8a/b/c | N/A |
| §5.1 | Sort+dedup boundary moments | :53-54 | FAITHFUL | S7c | N/A |
| §5.2/§9 | Cover whole span incl. silence as explicit EMPTY slices | :99-105 | FAITHFUL | S6 | N/A (emptiness implicit — matches §7 "stores no notes") |
| §5.2 | <2 boundaries → no slices | :58-61,95-97 | FAITHFUL | S7a,S7b | N/A |
| §7 | Slice=[start,end) half-open, stores no notes | slicer.h:84-87 | FAITHFUL | all | N/A |
| §7 | Slice identity = exact note set, not octave-folded pc set | slicer.h:52-54 | FAITHFUL | S4b | N/A |
| §8/§11 | Deterministic, O(n log n) | :53 single sort | FAITHFUL | **no dedicated determinism unit test** (relies on corpus tool) | N/A |
| §8/§2.5 | Clip boundary set to loaded span; inert on whole-score | :63-97 | **EXTRA** | CP1–CP7 | **CODE-RIGHT/SPEC-STALE** — clip step real+tested+in slicer.h:59-64 but the §5/§9 **body prose never mentions it** (lives only in the §8 cross-cut sentence + companion `cowork_layer2_reslice_design.md`) |
| §2/§13 | Wired: L3 reads slices via `changePointSlices` | regionanalyzer.cpp:605 | DEVIATION | reachback/regionanalysis | **CODE-RIGHT/SPEC-STALE** — spec repeatedly cites `regionanalyzer.cpp:579` (§2 L47, §4 L162, §11 L173, §13 L195; slicer.h:68); actual call is **line 605**; 579 is now unrelated. |

**L2 rows: 9 FAITHFUL / 1 DEVIATION / 0 MISSING / 1 EXTRA.**

### §1.4 Layer 3 — key/mode (`cowork_layer3_keymode_design.md`)

| Spec § | Rule (short) | Code site | Status | Tested? | Verdict |
|---|---|---|---|---|---|
| §1/§4 | Whole-sequence decode over slices | keymodesequence.cpp:401-415; regionanalyzer.cpp:606-609 | FAITHFUL | decode_keymode_tests | N/A |
| §1 | 252 space = 12 tonics × 21 modes | keymodesequence.cpp:46 | FAITHFUL | fixtures | N/A |
| §5.1 | Local-fit emission via L1 indexed query | :78-92 | FAITHFUL | fixture path | N/A |
| §5.1 | Keep top-K per slice ∪ running incumbent | :138,156-159 (global union of per-slice top-K) | **DEVIATION** | l3_coverage/keymode_branch | **UNDECIDABLE** — realized as path-independent global top-K union, NOT explicit incumbent injection. Header (keymodesequence.h:55-63) argues equivalence; but §5.1 says keep "the key the sequence is **currently in** even when a slice scores something else higher" — the union only preserves the incumbent if it is top-K on *some* slice. Is the union a faithful realization or a silent weakening? |
| §4/§5.2/§9 | Change cost = base + per-fifth·CoF + relative-pair; stay=0 | :232-241 | FAITHFUL | decode_keymode_tests | N/A (defaults 2.0/0.60/2.0) |
| §4 | Distance = circle-of-fifths steps (C→F♯=C→G♭=6) | :62-70 | FAITHFUL | :106 | N/A |
| §4 | No slice-count/duration threshold — pure fit-vs-cost | (no such term) | FAITHFUL | :165,184 | N/A |
| §5.3 | Best whole sequence via forward Viterbi + back-pointers | :266-322 | FAITHFUL | :269 | N/A |
| §5.4/§9 | Confidence = sequence margin (winner vs best-forced-different) | :324-383 | FAITHFUL | :147,225 | N/A |
| §5.4/§7 | "uncertain" mark when confidence<threshold | :383 (default 1.0) | FAITHFUL | :147,225 | N/A |
| §3/§7 | Per-slice: chosen + ranked alts + confidence + uncertain | keymodesequence.h:152-158; :385-395 | FAITHFUL | :241 | N/A |
| §3/§5 | redecodeRange with endpoints pinned == matching slice of full decode | :417-456 | FAITHFUL | :256,419 | N/A |
| §2/§5/§9 | Reach-back loop in orchestrator, gated OFF (default false) | regionanalyzer.cpp:631-693 | FAITHFUL | reachback_tests | N/A (dormant; spec cites 585-666, actual 631-693 — stale) |
| §1 | Region carries ranked ALT keys + confidence forward (additive) | regionanalyzer.cpp:245-249,738-815,1014-1034 | **EXTRA** | forwardoverride_tests | CODE-RIGHT/SPEC-STALE — implemented (region candidate-key menu); L3 spec body still frames it as a pending "requirement". |
| §11 | Leading-tone/char-pitch hard-gated at >0.1 window weight | keymodeanalyzer.cpp:339,374 | FAITHFUL (as documented defect) | keymodeanalyzer_tests | **UNDECIDABLE** — spec §11 flags this to fix in "Phase B (B2)"; still present verbatim (spec cites 344; found 339). Is Phase B still open, or is the note stale? |
| §15 | Notated-tpc as key evidence | absent (pc-only emission) | MISSING | — | N/A (spec §15 "Status: deferred") |
| §15 | Dominant-implication emission term (F-10/A-3) | absent | MISSING | — | N/A (spec §15 defers, design-first) |

**L3 rows: 13 FAITHFUL / 2 DEVIATION / 2 MISSING / 1 EXTRA.** Both MISSING rows are spec-deferred-by-design (they
are the A-3 capability track). **D-L3a two-numbers confirmed** — see §3 rows 2–3.

### §1.5 Layer 4 — chord decoder (`cowork_layer4_chordsymbol_design.md`)

| Spec § | Rule (short) | Code site | Status | Tested? | Verdict |
|---|---|---|---|---|---|
| §4.1/§5.1 | Complete candidate listing, fit-scored (reuses one scorer's cube) | chordslicedecoder.cpp:425-482 | FAITHFUL | decode_chord ranking | N/A |
| §5.1 | Absent CT = mild shortfall; extra note carried not penalised | inherited from `verticalScore` :51-55 | FAITHFUL | indirect | UNDECIDABLE (shortfall lives in reused scorer; "mild" not re-verified here) |
| §5.2 | Key + prevailing-chord preference (2nd reading) | key: h:130-133 (signature prior); prevailing ∪ :762-782 | **DEVIATION** | partial | **UNDECIDABLE** — key enters as ONE signature prior, NOT per-slice L3 feed-forward score adjustment ("a later refinement"); the §5.2 *score lean* on the 2nd reading is absent. Accepted dormant gap? |
| §5.3 t1 | Both-sides stepwise → NCT regardless of weight | :344-349 | FAITHFUL | yes | N/A |
| §5.3 t2 | Both-sides leap → CT extension regardless of weight | :360-363 | FAITHFUL | yes | N/A |
| §5.3 t3 | One-sided → metric weight + prevailing decides | :350-357 | FAITHFUL | yes | N/A |
| §5.3 | Template tone through same ladder = plausibility penalty | :812-823 | FAITHFUL | yes | N/A |
| §4.3/§5.4 | Sufficiency ≥3 distinct CT; margin gate; commit/inherit/abstain; never commit too-few | :1000-1063; sufficiency h:263 | FAITHFUL | yes (phantom-root, transition) | N/A |
| §4/§5.4 | Two-reading both-sides inherit; continuation vs transition gate | :1031-1049,1114-1147 | FAITHFUL | TwoReading tests | N/A |
| §5 sym | Symmetric root pinned from notated spelling; defer only unspelled/contradicted | :620-671,705-717 (uses `lineOfFifths`) | FAITHFUL | spelling-pin tests | N/A |
| §5 | Incomplete-chord handling (dyad/key/inherit/bass) | minDistinctPcs=1 h:182; :1031-1049 | DEVIATION | partial | SPEC-RIGHT/CODE-GAP — steps (1)(3)(4) present; §5 step-(2) key-picks-quality-from-scale-degree not a distinct mechanism (subsumed into scorer's diatonic term) |
| §7 | Result = symbol+CT+NCT+alternatives+confidence+open-question | SliceChord h:396-423 | FAITHFUL | yes | N/A |
| §7 | Carry extension identity + naturalFifthPresent for L5 (2026-07-02) | ChordSliceCandidate h:306-320; :464-506 | FAITHFUL | CarryFix tests :1410-1484 | N/A (honest-carry `extensionsKnown`) |
| §7 | isPedalPoint/pedalBassPc NOT carried | absent | FAITHFUL | — | N/A (correct per §7) |
| §7/§8 | Composite = margin⊕sufficiency⊕cleanliness, low for EITHER | computeConfidence :865-899 | FAITHFUL | tests :840-903 | N/A (MIN of three [0,1] — see §3 row 4) |
| §7/§12/§15-O1 | Named open question + AmbiguityKind | nameOpenQuestion :901-969; enums h:343-363 | **DEVIATION** | partial | **UNDECIDABLE** — `NoteMembership` reserved/never populated; `SymmetricRotation` (augmented-only trigger, dim7→G5) & `CloseReading` have code sites but **no lock-in test** (Rider 2). |
| §8 | Never a pooled recompute; per-slice from indexed notes | :142-165 (`overlapping`) | FAITHFUL | indirect | N/A |
| §2/§3 | Adaptive lazy-extend bounded window | :186-211 | FAITHFUL | indirect | N/A |
| §2 | Bounded-context: request extension at selection/score edge | :197-200 (clamps, proceeds truncated) | DEVIATION | no | SPEC-RIGHT/CODE-GAP — no "request one harmony's extension" path; silently truncates. Accepted for dormant diagnostic? |
| §2/§15-O3 | Phrase/texture-boundary window truncation | — | MISSING | no | N/A (spec "not built now", 2026-07-01) |
| §3 | redecodeRange | :1246-1258 | FAITHFUL | indirect | N/A |
| §15-O1b | alternatives topK cap + spelling-pinned siblings excluded | :720-757 | FAITHFUL | yes (:189,:1073) | N/A |
| §15-O1b | Lock-in test pins carry on Commit/Inherit | decode_chord_tests.cpp:1360-1400 | FAITHFUL | OverrideReadiness_* | N/A |
| §C2/G5 | New dim7/mMaj7 TYPES | — | MISSING | — | N/A (deferred to engage, h:97-103) |

**L4 rows: 16 FAITHFUL / 5 DEVIATION / 3 MISSING / 0 EXTRA.** All 3 MISSING are spec-deferred. The two
UNDECIDABLE DEVIATIONs (§5.2 key-lean; §7 AmbiguityKind coverage) are the substantive L4 items.

### §1.6 Layer 5 — function (`cowork_layer5_function_design.md`)

| Spec § | Rule (short) | Code site | Status | Tested? | Verdict |
|---|---|---|---|---|---|
| §5.1 | Base RN: degree/quality/inversion, chromatic prefix, no key change | functionromannumeral.cpp:35-44 | FAITHFUL | functionromannumeral_tests | N/A |
| §5.2 | Cadence on EVENT PAIR, key-agnostic, feature-scored | functioncadence.cpp:494-527 | FAITHFUL | functioncadence_tests | N/A |
| §5.2 | Cadential 6/4 collapse first | :105-115,254-263,223-225 | FAITHFUL | yes | N/A |
| §5.2 | Authentic gate = seq + dom-approach (V/viio) + LT resolves; 7th = strengthener not gate | :234-267 | FAITHFUL | yes | N/A (matches 2026-06-26 amendment) |
| §5.2 | Perfect ⟺ both root position; imperfect = complement | :269-275 | FAITHFUL | yes | N/A |
| §5.2 | Melodic/top-voice arrival = soft nudge, never a test | absent | MISSING | — | CODE-RIGHT/SPEC-STALE — spec §15-0 demotes to optional-not-a-gate; absence permitted |
| §5.2 | Half cadence: phrase-final on dominant; inverted/7th admitted at LOWER weight; Phrygian iv6→V | :346-391 | **DEVIATION** | yes | **UNDECIDABLE** — Phrygian+seq faithful, but `tryHalf` requires `arr.quality==Major` (:355) and applies **no inversion discount** (§5.2 says "admitted but at lower weight"). Intended simplification or gap? |
| §5.2 | Deceptive: dom set-up → submediant (♭VI minor) | :289-343 | FAITHFUL | yes | N/A |
| §5.2 | Plagal: subdominant-family→tonic, no dominant, lower conf | :394-432 | FAITHFUL | yes | N/A |
| §5.2 | Evaded: dom set-up, arrival replaced | :438-490 | FAITHFUL | yes | N/A |
| §5.2 | Chorale phrase gate | :220,295,352,400,444 | FAITHFUL | yes | N/A |
| §5.2 | Tonic vote = monotone weighted sum − per-type discount | :159-197 | FAITHFUL | yes | N/A |
| §5.3 | Default tonicization; modulation iff cadence-confirm AND persistence | functionmodulation.cpp:50-86 | FAITHFUL | functionmodulation_tests | N/A |
| §5.3 | (a) necessary gate (no cadence ⇒ never modulation) | :60,84 | FAITHFUL | yes | N/A |
| §5.3 | (b) hysteresis over duration+weight, not a beat count; break-even tonicizes | :64-86 | FAITHFUL | yes | N/A |
| §5.3 | Detector reuse keeps `kEstablishmentMinChords` floor as pre-filter (Step-M owed) | :103 | FAITHFUL | localmodulationdetector_tests | UNDECIDABLE (the Step-M "does the floor reject a real short modulation" is a deferred measurement, not code) |
| §5.3 | Notated-spelling key signal, function-gated, one soft input | :70,77 (`wSpelling` 0.5) | FAITHFUL | yes | N/A |
| §5.4 | Confirmed modulation → bounded forward re-run, key-closed | :107-159 | FAITHFUL | yes | N/A |
| §5.5 | Transition / share-tone / relative-pair / close / symmetric resolution | functionresolver.cpp:216-339 | FAITHFUL (one DEVIATION below) | functionresolver_tests | N/A |
| §5.5 | Relative pair: cadence vote + same-collection cues | :249-264 | DEVIATION | yes | UNDECIDABLE — "raised leading tone" + "phrase-final emphasis" cues only *folded into* the cadence vote (:253-255), not separately scored. Sufficient, or is a distinct cue owed? |
| §5.5/§8 | Case-4 fine-grain override: Commit-only; select carried alts/neighbour; never re-derive | :379-496 | FAITHFUL | yes | N/A |
| §5.5 (carry-fix 2) | Emitted reading = selected source's committed identity VERBATIM | :363,482,184; candidateFromProg RETIRED | FAITHFUL | yes | N/A ✔CC (grep: candidateFromProg gone) |
| §5.6 | Precedence aug6→Neapolitan→applied→mixture, first-match | functionrelationallabel.cpp:319-343 | FAITHFUL | functionrelationallabel_tests | N/A |
| §5.6 | Applied trigger + general foreign-tone necessary-cond guard | :215-315 | FAITHFUL | yes | N/A |
| §5.6 | V/iv tonic-rooted over-trigger inference-deferred (not a guard matter) | :281-284 | FAITHFUL | yes | N/A (guard-inertness, §5.6) |
| §5.6 | Neapolitan / aug6 spelling-aware (Ger6↔V7 via LoF) | :72-151 | FAITHFUL | yes | N/A |
| §5.6 | Modal mixture = residual borrowed degree, no key change | :185-209 | DEVIATION | yes | CODE-RIGHT/SPEC-STALE — borrowed-quality-on-diatonic-root detected only in Ionian (:196); declared scope in code comment (:155-158) |
| §5.7 | Bass-degree soft prior (tie-break only) | :113-145,199-213 | FAITHFUL | yes | N/A |
| §7 | Per-unit RN + 3-component confidence + open mark; additive | functionoutput.cpp:66-138 | FAITHFUL | functionoutput_tests | N/A |
| §7 (D-L5a) | Publish combinedBoundary = combined/(combined+k); §8 sites don't read raw combined | :124-132 | FAITHFUL | yes | N/A ✔CC |
| §8 | 4-case model = one localized forward recompute + one-pass closure; bar scales with confidence [0,1] | forwardoverride.cpp:26-100 | FAITHFUL | forwardoverride_tests | N/A ✔CC (re-entrancy guard read) |
| §13/§15-5 | `harmonicfunctionlayer` misnomer renamed/retired | harmonicfunctionlayer.h:52 ("E4 planned") | MISSING | — | UNDECIDABLE (spec-deferred to engage — R7) |
| §9-D1 | Three-role T/S/D read-out | absent | MISSING | — | N/A (spec defers) |

**L5 rows: 27 FAITHFUL / 4 DEVIATION / 5 MISSING / 0 EXTRA.** All 5 MISSING are spec-deferred. Substantive items:
the half-cadence inverted/7th admission (§5.2) and the relative-pair cue folding (§5.5).

### §1.7 Vocabulary (`cowork_progression_schema_dictionary.md`) — dormant (`89c4c6cb06`)

Full table in the auditor record; the material rows (34 FAITHFUL / 4 DEVIATION / 3 MISSING / 1 EXTRA):

| Spec § | Rule (short) | Code site | Status | Verdict |
|---|---|---|---|---|
| §1/§2 | Knowledge not a tool; const queries; decides nothing (matchScore hardcoded 1.0) | harmonicvocabulary.h:254-277; .cpp:414 | FAITHFUL | N/A (firewall) |
| §4 | browse/recognise/suggest/expand each return ranked candidates | .cpp:404,469,586,621 | FAITHFUL | N/A |
| §5.1 | viio7/x "(or viiø7/x)" — half-dim secondary LT | .cpp:632 (dim7 only) | DEVIATION | SPEC-RIGHT/CODE-GAP (viiø7/x variant not generated) |
| §5.1 | Diatonic-function families + licensed root motions | absent (delegated to functionprogression per h:54-56) | MISSING | UNDECIDABLE — catalog rows here, or delegate to L5? (F-6/A-6 store question) |
| §5.2 | Half cadence (…→V) standalone | absent | MISSING | UNDECIDABLE — deferred to L5 cadence detector, or a gap? |
| §5.2 | Galant Ponte + Quiescenza | absent (5 of 7 schemata present) | DEVIATION | SPEC-RIGHT/CODE-GAP (both pedal-defined; deferred pending voice-leading?) |
| §5.2 | Bass/pop loops: chromatic-lament variant + Axis rotations | absent (declared VL elaboration :292-294) | DEVIATION | SPEC-RIGHT/CODE-GAP (minor, declared) |
| §6/§12.1 | One hierarchical style taxonomy | 3-value {Baroque,Jazz,Default} placeholder | DEVIATION | UNDECIDABLE — placeholder accepted v1 pending ratified taxonomy? |
| §7 | Degree via inline `pcOffset` (reimplements region primitive chromatic) | .cpp:155-161 | EXTRA | N/A (correct no-back-reference) |

**Vocabulary rows: 34 FAITHFUL / 4 DEVIATION / 3 MISSING / 1 EXTRA.** All gaps are dormant-catalog gaps (no runtime
effect). The one architecturally-live item is the F-6/A-6 two-stores question (delegated pairwise motions).

**Aggregate across §1: ~132 FAITHFUL / 19 DEVIATION / 14 MISSING / 3 EXTRA rows.** Of the 14 MISSING, **all** are
spec-deferred-by-design. Of the 19 DEVIATION, ~7 are self-disclosed SPEC-STALE simplifications and the rest split
between UNDECIDABLE (need a ruling) and small CODE-GAPs.

---

## §2. The seven riders (evidence-first)

### Rider 1 — no production back-edge (HIGHEST severity check) — **PASS, no back-edge** ✔CC

Cross-layer call inventory (production spine + orchestrator):

| Caller | Callee | Direction | Class |
|---|---|---|---|
| regionanalyzer.cpp:605 | `slc::changePointSlices` | orch→L2 | LEGAL |
| regionanalyzer.cpp:607-609 | `KeyModeSequenceDecoder::decode` | orch→L3 (forward) | LEGAL |
| regionanalyzer.cpp:677-680 | re-slice+re-decode (reach-back, default OFF) | orch→L2/L3 forward, enlarged span | LEGAL (loop in orchestrator, decoder stays pure) |
| chordslicedecoder.cpp:436,447,160,603 | weightedPcView / analyzeChord / regionMetricWeight / lineOfFifths | L4→L1-adjacent + scorer (data) | LEGAL data-supply-down |
| functionresolver.cpp:130,143 | `region::diatonicDegreeForRootPc` | L5→shared pc→degree map | LEGAL data-supply-down |
| functioncadence.cpp:92 | `isLicensedProgression` | L5→L5 | LEGAL intra-layer |
| functionresolver.cpp:489 / functionmodulation.cpp:150 | `closure.forwardRecompute(i+1,…)` / `(firstSlice,…)` | L5→L5 §8 | LEGAL forward (below) |

L5 `.cpp` reach L4/L3 **only via header type includes** (`chordslicedecoder.h`, `chordanalyzer.h`,
`analysistypes.h`) — carried-reading data contracts, not decision calls. The resolver reads L4's committed identity
verbatim (`carryThrough`, functionresolver.cpp:363 `r.reading = s.chosen`) and on override selects among carried
alternatives (`r.reading = bestAlt`, :482) — never re-derives.

The §8 forward-recompute + re-entrancy guard (forwardoverride.cpp / .h ✔CC read this run):
- Grows-only ledger `m_closed` (markFinal :52-56); `tryOverride` refuses a closed decision (:61-62), marks final on fire (:67).
- `forwardRecompute` (:71-93): `if (m_recomputing) return -1;` (re-entrant refused) then a **forward ascending** sweep `firstSlice→lastSlice`; callers pass `i+1` (strictly downstream). `reread` re-runs only `resolveAbstained` (selection among carried readings) / re-reads each slice in the new key — neither re-invokes an L3/L4 decision function.

**Verdict: no back-edge.** The mechanism is forward, re-entrancy-guarded, selection-only. The one legal "backward-looking" recompute is convergence-bounded by the closure ledger + the `m_recomputing` guard.

### Rider 2 — L4→L5 carried-readings contract — **CONFIRMED, one qualification**

- `alternatives` populated on every decision kind: filled in `decideSlice` (chordslicedecoder.cpp:744-782) **before** the trichotomy; no path in `applyCommitDecision` (:1004-1063) clears it. Lock-in asserts non-empty on Commit (decode_chord_tests.cpp:1376), Inherit (:1396), Abstain (:446).
- `confidenceModel` populated on every return path: `populateForwardContract` called at :984 (decision-off), :992 (no-chord abstain), :1007 (Commit), :1045 (Inherit), :1061 (Abstain). Lock-in :1377-1379,:1397.
- topK cap (:753-755) + spelling-pinned-sibling exclusion (`isResolvedSibling` :720-757, tested :1073) — both present.
- Lock-in test pinning the carry: `OverrideReadiness_CommitAndInheritCarryAlternativesAndConfidence` (:1360); extension carry pinned by `CarryFix_Dom7ChosenCarriesMinorSeventh` (:1410), `CarryFix_CarriedSeventhDrivesAppliedV7Label` (:1440).
- **Qualification (the one gap):** of the six `AmbiguityKind` values, `None`/`InsufficientEvidence`/`TransitionVsContinuation`/`ShareTone`/`RelativePair` are reachable+tested; **`SymmetricRotation`** has a code site (:960) but its only live abstain trigger is both-readings-`Augmented` (:959) — the dim7 rotation case is pinned away before abstain (enum comment concedes "dim7 once G5 lands", h:359) — and **`CloseReading`** (:945,953,966) — neither has a lock-in test; **`NoteMembership`** (h:348) is declared reserved and confirmed never populated. → 2/6 kinds untested, 1/6 never emitted. Feeds the D-INV / engage-readiness list.

### Rider 3 — the §8 override sites' confidence scales (A-1 evidence, D-FS) — **CONFIRMED** ✔CC

Both frames read + verified at source this run; the code already carries the contract's frame-name annotations.

- **Frame F-A** (cadence-confirmed modulation recompute, functionmodulation.cpp:136-137): `closure.tryOverride(keyDecisionId, homeKeyConfidence, modulation.cadentialWeight, …)`.
  - Incumbent `homeKeyConfidence` = L3 key-of-span (Class-M squashed sequence margin), assumed [0,1].
  - Contradiction `cadentialWeight` = Σ tonicVote in candidate key (:52-61) — **unbounded ≥0, NOT squashed**.
- **Frame F-B** (fine-grain chord override, functionresolver.cpp:466): `tryOverride(i, s.confidence.composite, contradictionStrength, …)` with `contradictionStrength = bestPlaus − committedPlaus` (:448).
  - Incumbent `s.confidence.composite` = L4 composite, **genuinely [0,1]** (min of three [0,1]).
  - Contradiction = plausibility margin (each plausibility ∈[0,3] at default weights → diff bounded [−3,3] but **not squashed**), gated `>0` (:449).
- **Only squash at the boundary:** the defensive `clamp01` on `earlierConfidence` inside `overrideBar` (forwardoverride.cpp:31-37). The θ (`baseBar`/`confidenceScale`) is a DEFAULT seed, explicitly Stage-5 (functionresolver.cpp:463-465; functionmodulation.cpp:133-135).
- **No third caller:** the only `tryOverride` callers are F-A + F-B; the only `forwardRecompute` callers are their two downstream re-reads (✔CC grep). No undeclared override site.

This is exactly **contract §7 D-FS**: incumbents [0,1], contradictions unbounded/unsquashed — the live
commensurability gap. It is a declared Stage-5 calibration item, **not a behavior bug now** (all dormant).
**D-L5a is separately CLOSED** and correctly NOT the §8 input: `combinedBoundary` published at functionoutput.cpp:131
(✔CC), and neither F-A nor F-B reads `FunctionConfidence.combined` (the source comments state this explicitly).

### Rider 4 — the three cadence implementations' call graphs — **CONFIRMED**

| Implementation | Symbol | Callers | Context |
|---|---|---|---|
| Legacy circular | `detectCadences` (sectioncadencedetection.cpp:55) | notationcomposingbridge.cpp:70,1233; notationimplodebridge.cpp:73,1284; notationannotate_tests.cpp ×8 | **PRODUCTION** + test |
| Legacy circular | `detectPivotChords` (:140) | notationcomposingbridge.cpp:71,1038,1247; notationannotate_tests.cpp ×5 | **PRODUCTION** + test |
| Instrument | `cadencekeyanchor` (:122) | tools/batch_analyze.cpp:956; cadencekeyanchor_tests.cpp ×16 | tools + test only |
| L5 | `detectFunctionalCadences` (functioncadence.cpp:495) | tools/batch_analyze.cpp:2743; functioncadence_tests.cpp ×~20 | tools + test only |

**R2** (retire legacy detector): the legacy pair are the **only** cadence functions with production callers (both
notation bridges) — retirement requires first migrating those two sites to the L5 path, which is dormant. **R3**
(keep `cadencekeyanchor` as diagnostic): confirmed diagnostic-only (sole non-test caller = batch_analyze;
header self-documents "MEASURED only … the production key resolver never calls it").

### Rider 5 — B-swap readiness (producer-agnostic seams) — **CONFIRMED**

- L4 `decideSlice` (chordslicedecoder.h:535-540, cpp:673-785) is **scorer-independent**: it takes a precomputed `std::vector<ChordSliceCandidate>` and depends only on `.score` (a plain double) via `candidateBetter` (:60-72). No `RuleBasedChordAnalyzer`/`NoteModel`/`analyzeChord` inside. Header states the seam explicitly (h:515-521). The hand-built scorer is entangled **only** in `candidatesForWindow` (:425-482, the generation step) — a clean upstream boundary. Soft coupling: `.score` semantics + `uncertaintyMargin` seeds are in the scorer's units (a learned emission must emit comparable scores or re-tune the seeds), but structurally the swap is drop-in.
- L5 units hand-injectable over POD views: `functioncadence` (POD `CadenceEvent`), `functionresolver` (`FunctionSlice` unions the §5.0 view + L4 value-structs from `chordslicedecoder.h`, not the engine), `functionprogression`/`functionoutput` (pure POD), `functionmodulation` (`reread` is a `std::function` seam). `tonicizationlabeler` input is plain POD.
- **Named entanglement (intended, not accidental):** `functionrelationallabel` (functionrelationallabel.cpp:23-28) `#include`s `spellingview.h` + `chordanalyzer.h` (`ChordSymbolFormatter`) — it binds the one shared spelling interpreter + `formatRomanNumeral` **by design** (§5.6 "the one shared spelling interpreter"; §3 "no second formatter"). Its input is still POD (`RelationalLabelInput`), so a hand-built scorer *can* inject, but must supply real `rootTpc`/`noteTpcs` for the aug6 spelling read. This is reuse, not a swap-blocker.
- Vocabulary: depends downward only (`analysistypes.h` + `chordanalyzer.h`); no decision-layer include; only non-test caller is its own test (✔CC grep). The `region::diatonicDegreeForRootPc` reference in the header is a design note, not a call (the component reimplements it inline as `pcOffset`). Clean for B-swap.

### Rider 6 — confidence inventory — see §3.

### Rider 7 — systematic projection sweep — **CONFIRMED, no CANDIDATE-GAP**

10 projection sites (inter- + intra-layer). Every dropped field is either re-queried by design or covered by a
recent carry-fix:

| Site | Source→Dest | Dropped | Consumed downstream? | Verdict |
|---|---|---|---|---|
| L1→L2 slicer.h:46-48,93 | NoteEvent→Slice{start,end} | pitch/tpc/voice/weight | No — notes re-queried via NoteModel index | harmless |
| L2→L3 keymodesequence.cpp:78-92 | Slice→PitchContext window | none | — | harmless |
| L3→L4 chordslicedecoder.h:475-480 | L3 key result→(fifths+mode) args | normalizedConfidence, margin, alternatives | Header: per-slice L3 feed-forward is "a later refinement" (h:130-133) | harmless (by-design; not yet wired) |
| **L4→L5 carry** chordslicedecoder.cpp:454-479 | ScoringCell→ChordSliceCandidate | extensions/naturalFifthPresent on alts w/o matching result | Yes (V7/x, aug6) — **guarded by `extensionsKnown`** (honest-carry) | **known-fixed (4b3d054d89)** |
| **L5 resolver toPC** functionresolver.cpp:42-45 | ChordSliceCandidate→ProgressionChord{root,quality} | bass, extensions, naturalFifthPresent, score | Licensing uses root+quality; bass/ext survive via the SEPARATE verbatim `chosen`/`reading` carry | **known-fixed (3aaa2cbd63)** |
| L5 buildProgression :54-68 | FunctionSlice→ProgressionSlice | decision/openQuestion/alternatives/confidence/chosen | Read directly off `region` (FunctionSlice), not via prog | harmless |
| L5→L6 functionoutput.cpp:105-134 | FunctionUnitAssembly→FunctionAnalysisUnit | chord, committed (used only in-fn by licensedFit) | Not needed downstream of the unit | harmless |
| L5→L6 committedIdentity :118 | verbatim `=` | none | full ChordIdentity preserved | harmless (verbatim) |
| Intra-L5 modulation :103 | key spans→ModulationDecision | evidence magnitudes | Output reads only isModulation/tonicPc/minorMode | harmless |
| Intra-L5 cadence→vote :159-197 | cues→scalar tonicVote | individual cue booleans | scalar is the consumed quantity | harmless (intended reduction) |

The two load-bearing projections are the recent carry-fix sites and are now covered. **No new carry-gap of the
`4b3d054d89`/`3aaa2cbd63` class was found** — the class is closed for the enumerated sites.

---

## §3. Confidence inventory (Rider 6 → A-1 §3 / D-INV close-out)

| # | Confidence | Formula (as-built) | Range | Squash? | Consumers | Source |
|---|---|---|---|---|---|---|
| 1 | L1.5 phrase-boundary | per-voice `Σ w·cue`, cues `localChangeProfile` then **max-normalised across voices**; texture = Σ per-voice + marker spike; pick = local-max AND `>mean+k·SD` | cues [0,1]; texture unbounded; pickedTicks boolean | max-norm (not sigmoid) at cpp:243-255,338-356; picker :257-281 | dormant/gated only (joint-key re-key; `--dump-cadence-anchor/-modulation`) — no production reader | phraseboundaryview.cpp:358-447 |
| 2 | **L3 sequence margin** (`SliceKeyMode.confidence`) | `winnerTotal − secondBest` (fwd α + bwd β Viterbi totals); single-state sentinel `1e3` | unbounded ≥0 (emission-score units) | **NOT squashed** | `uncertain = <1.0` (:383); `region.keyConfidence` (regionanalyzer.cpp:1015,1034) → the F-A override incumbent | keymodesequence.cpp:378-383; h:156 |
| 3 | **L3 emission `normalizedConfidence`** (the SECOND L3 number, D-L3a) | `1/(1+exp(−1.5·(gap−2.0)))`, gap = chosen − bestOther at the slice | (0,1) sigmoid | **sigmoid** (`populateEmissionConfidence` :224-227) | the "0.8 downstream key-confidence gates" (h:82,200-203); regionanalyzer.cpp:454,496,501 | keymodesequence.cpp:201-228 |
| 4 | L4 `SliceConfidence.composite` (+3 components) | sufficiency=present/required·clamp; membershipCleanliness=focalCT/focalPcs·clamp; marginCertainty=min(1,margin/(2·uncertaintyMargin)); **composite = min(all three)** | composite [0,1]; raw `margin` field unbounded | composite bounded by MIN-of-[0,1] (not sigmoid) | L5 resolver via `FunctionSlice.confidence` — the **F-B override incumbent** | chordslicedecoder.cpp:865-899; h:373-378 |
| 5 | L5 `FunctionConfidence.combined` + `combinedBoundary` | `combined = wCadenceVote·cadenceVote + wLicensedFit·licensedFit + wNextBestMargin·nextBestMargin`; **`combinedBoundary = combined/(combined+k)`**, k=1.0 | combined unbounded ≥0 (~25 observed); combinedBoundary [0,1) | **squashed** at functionoutput.cpp:131-132 (D-L5a, `0a88747e7f`) | dormant; explicitly NOT read by resolver/modulation (the OUTPUT confidence) | functionoutput.cpp:120-132; h:85-99 |
| 6 | cadence `tonicVote` | `wBase(+wBassFiveToOne)(+wLeadingTone)(+wSeventh) + wMetric·metricWeight (+wPhraseBoundary)(+wFinalBar) − discount{Half/Plagal/Evaded}`, clamp ≥0 | unbounded ≥0 | **NOT squashed** (clamp at 0 only) | `FunctionConfidence.cadenceVoteWeight` (functionoutput.cpp:39,121); resolver cadence step; the **F-A contradiction** | functioncadence.cpp:159-197; h:178 |
| 7 | legacy `normalizedConfidence` + sentinels | sigmoid `1/(1+exp(−steepness·(gap−midpoint)))`, gap = winner − runnerUp; **fallback sentinel `0.0`** (keyresolver.cpp:331) **and `0.5`** (see correction) | (0,1); sentinels 0.0 / 0.5 | sigmoid; sentinels bypass it | keyresolver.cpp:319 dynamic-lookahead gate; regionanalyzer.cpp:454,496,501,524 | keymodeanalyzer.cpp:762-778; keyresolver.cpp:55-67,331 |

**Correction to the Rider-6 auditor (✔CC this run):** the auditor reported it could not find a `0.5` confidence
sentinel. It exists — `regionanalyzer.cpp:393` `constexpr double kJointModulationFallbackConfidence = 0.5;` (the
joint-modulation fallback path, not the base resolver, which is why a keyresolver/keymodeanalyzer-scoped search
missed it). This matches the contract §3 / D-LEG "0.0 / 0.5 hard-coded" reference. The `0.0` fallback
(keyresolver.cpp:331, called with `0.0,0.0`) is also confirmed.

**D-L3a confirmed:** two distinct L3 numbers ride the boundary — the sequence margin (row 2, the F-A incumbent) and
the emission sigmoid (row 3, the 0.8-gate input). Contract §7 D-L3a's "declare the margin THE boundary confidence,
demote the sigmoid to diagnostic" is a **doc/wiring** action, not yet reflected in the two-field code.

---

## §4. Ranked summary — top-10 gaps by severity (with suggested verdict)

Ranked by engage-risk / correctness-relevance / undeclared-drift. Nothing here is a back-edge or an undeclared
carry-gap (both classes came back clean).

1. **D-FS — §8 contradiction scales unbounded vs [0,1] incumbents (F-A `cadentialWeight`, F-B plausibility-diff).**
   Verdict: **SPEC-RIGHT/CODE-GAP, already declared** (contract §7 D-FS). The live commensurability gap; the E0
   override net-harm (968 fires / 45 corrections) is its symptom. Not a bug while dormant; **the** thing Stage-5
   calibration (C2) must close before engage. *(§2 Rider 3; ✔CC.)*
2. **L3 top-K-union vs explicit incumbent (§5.1).** Verdict: **UNDECIDABLE** — is the path-independent global
   top-K union a faithful realization of "keep the key the sequence is currently in", or can it silently drop an
   incumbent that is top-K on no slice? Correctness-relevant at engage. **Question for Cowork/user.** *(§1.4.)*
3. **L4 AmbiguityKind under-coverage (Rider 2 qualification).** `SymmetricRotation` fires augmented-only (dim7 →
   G5), `CloseReading` untested, `NoteMembership` never populated. Verdict: **SPEC-RIGHT/CODE-GAP** (carry-contract
   completeness) — 2/6 kinds need lock-in tests + the dim7 trigger is owed at G5. *(§1.5, §2 Rider 2.)*
4. **L4 §5.2 key-preference *score lean* on the 2nd reading absent** (key enters only as one signature prior, not
   per-slice L3 feed-forward). Verdict: **UNDECIDABLE → likely CODE-GAP** — is the deferred key-lean an accepted
   dormant-state gap, or owed before engage? *(§1.5.)*
5. **L4 §2 bounded-context "request extension" at a selection/score edge missing** (window silently truncates).
   Verdict: **SPEC-RIGHT/CODE-GAP** — acceptable for the single-run diagnostic; the selection-edge extension
   contract is unbuilt. *(§1.5.)*
6. **L5 §5.2 half-cadence: inverted/7th dominant not admitted-at-lower-weight** (`tryHalf` requires
   `arr.quality==Major`, no inversion discount). Verdict: **UNDECIDABLE** — intended simplification or gap? *(§1.6.)*
7. **L1.5 §4.1-vs-§4.3 normalization contradiction** ("per-score maximum" vs "across all voices"; code does
   across-voices; `maxNormalizeInPlace` helper is unused). Verdict: **UNDECIDABLE** — a spec-internal contradiction
   requiring a canonical-reading ruling. *(§1.2.)*
8. **Test-coverage CODE-GAPs (no behavior gap):** L1.5 breath/caesura + key-sig-change markers have no test; L4
   `SymmetricRotation`/`CloseReading` have no lock-in test; L1 `onsetIn` has no dedicated test. Verdict:
   **SPEC-RIGHT/CODE-GAP (coverage)** — closes with test additions, ride the coverage-seal (G4). *(§1.1, §1.2, §1.5.)*
9. **Pervasive stale line-number citations in the L2/L3 specs.** `regionanalyzer.cpp:579` (actual 605), reach-back
   `585-666` (actual 631-693), keymodeanalyzer `344` (actual 339), slicer.h:68. Verdict: **CODE-RIGHT/SPEC-STALE**
   — a line-number refresh pass on the L2/L3 specs. Low severity but load-bearing for navigation/verification. *(§1.3, §1.4.)*
10. **Vocabulary catalog omissions** (galant Ponte + Quiescenza; half-cadence entry; viiø7/x variant; Axis
    rotations; chromatic-lament variant) **and** the F-6/A-6 two-stores question (pairwise motions delegated to
    `functionprogression`). Verdict: **SPEC-RIGHT/CODE-GAP (dormant catalog)** for the omissions;
    **UNDECIDABLE** for the store question (decide at recognition-consumer build per A-6). *(§1.7.)*

**Also noted, not ranked (out of spec-vs-code scope but adjacent):** the `harmonicfunctionlayer` rename (R7,
E4-deferred); the F-8/A-8 gate-granularity move (evaluation methodology, not a code↔spec gap); the L3 §11
leading-tone `>0.1` presence-gate (documented Phase-B defect — is Phase B still open? UNDECIDABLE).

**What is clean (the load-bearing negatives):** no production back-edge (Rider 1); no undeclared override site
(Rider 3); no projection CANDIDATE-GAP (Rider 7); the two recent carry-fixes verified in place (`candidateFromProg`
gone; `combinedBoundary` published; extension honest-carry); all three suites green; gate unchanged.

---

## §5. Unknowns (stated as such — never guessed)

- **L3 §5.1 top-K union equivalence** — the header *asserts* incumbent-preservation via the union; whether that
  holds on a slice where the incumbent is top-K on no slice is a behavioral question the audit could not settle by
  reading alone. Needs a targeted test or a Cowork ruling (ranked #2).
- **L1.5 §4.1 "per-score maximum" canonical reading** — genuine spec-internal ambiguity vs §4.3 "across all
  voices"; the code picks across-voices. A human must declare which is canonical (ranked #7).
- **L3 §11 leading-tone `>0.1` presence-gate** — still present verbatim (keymodeanalyzer.cpp:339,374); whether
  "Phase B (B2)" remains an open accepted-defect item or the spec note is stale is undetermined.
- **L4 "mild shortfall" fit weighting** — lives in the reused `analyzeChord` scorer (chordslicedecoder.cpp:51-55),
  not audited here; whether it still matches the §5.1 "mild" intent is not re-verified.
- **Empirical confidence ranges (§3)** — ranges are read from formulas/comments (e.g. L5 `combined` "~25 on the E0
  spine" per functionoutput.h:91), not independently measured this run (no analyzer run — read-only, nothing changed).
- **Exhaustive external-caller proof of dormancy** — dormancy is verified by grep over `src/` + `tools/` (only
  `tools/batch_analyze.cpp` + tests call the L4/L5 spine, ✔CC); a header could in principle contain an inline
  decision call not surfaced by an include+cpp grep, but none was found and the symbol-grep is negative.
- **L1 `onsetIn` branch coverage** — exercised transitively; whether §10 "every branch" is satisfied without a
  dedicated test is a coverage-policy question, not a behavior gap.
- **Vocabulary deferrals** — for each catalog omission (Ponte/Quiescenza/half-cadence/viiø7·x) whether it is
  intended-deferred or a gap needs a per-item ruling; all are dormant so none has runtime effect.

---

*End of report. Load-bearing rider claims independently re-verified at source by CC (marked ✔CC): no back-edge
(forwardoverride.h/.cpp guard); F-A/F-B override scales (functionmodulation.cpp:136, functionresolver.cpp:448-466 —
code carries the frame-name annotations); D-L5a `combinedBoundary` (functionoutput.cpp:131); `candidateFromProg`
retired (grep miss); L4/L5 dormancy (grep: only tools/batch_analyze.cpp + tests); the `0.5` sentinel correction
(regionanalyzer.cpp:393). Suites green at baseline (998 / 53 / 11). No file modified except this report; no commit.*

LINE COUNT: this file is 435 lines.
