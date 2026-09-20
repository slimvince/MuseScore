# CC build report — the PROGRESSION-RECOGNITION CONSUMER (dormant build + dev-bed validation)

> **Status: HELD for Cowork.** Dormant, additive, byte-identical-by-construction. Three fork-only local
> commits (below). Gate **53 / 24 / 53 exact**; suites green, no golden refresh. On this report Cowork
> verifies at the committed objects before ratifying. Spec: `cowork_progression_schema_design.md` (v4, fully
> ratified 2026-07-02) §3/§4; component consumed: `cowork_progression_schema_dictionary.md`.

## 0. Result at a glance

| Deliverable | State |
|---|---|
| Task 1 — the dormant module (§4.1–§4.6) | ✅ `analysis/progression/progressionrecognizer.{h,cpp}` |
| Task 2 — the D5 riders (consistency test + mirrored cross-comments + doc-sync) | ✅ (Option A per the ruling) |
| Task 3 — oracle tests (16) + §7 dev-bed validation | ✅ |
| Suites | composing **1051** (1035→+16), pipeline snapshot **11** (no refresh), notation **53** |
| Corpus gate | **Baroque 53 / Jazz 24 / Default 53 — EXACT** |
| Dormancy | grep-proven — `recognizeProgressions` has **no production caller** |
| θ / tuning | **none** — every §4.5/§4.6 value is a declared precision-phase default |
| Commits (local, unpushed, fork-only) | `3ccf963b8f` module · `45000aae70` tests+riders+doc-sync · `1d23be8984` validation |

**Stop conditions honoured:** no production reach; no §5.3/F-C wiring; no tuning; and the one catalog↔grammar
consistency STOP was surfaced *before* building around it (§1 below) and resolved by the ratified ruling.

## 1. The consistency-test STOP and its ruling (the load-bearing event of this build)

Task 2.1 asserts D5's containment: *every adjacent chord pair of every catalog entry passes
`isLicensedProgression`*. Building the check revealed the containment **does not hold** — the §5.0 grammar
(`functionprogression.cpp:96`) licenses exactly the root-motion deltas **{1, 2, 5, 8, 9}**, and **6 chord-degree
entries carry 11 motions outside it**:

| Entry | Failing pair(s) | delta | reading |
|---|---|---|---|
| Plagal cadence (IV–I) | IV→I | 7 | plagal / ascending-5th |
| Axis (I–V–vi–IV) | I→V | 7 | tonic→dominant |
| Pachelbel (I–V–vi–iii–IV–I–IV–V) | I→V, vi→iii, IV→I | 7,7,7 | ascending-5ths |
| Romanesca (I–V–vi–iii) *[vlDefined]* | I→V, vi→iii | 7,7 | ascending-5ths |
| Andalusian (i–♭VII–♭VI–V) | i→♭VII, ♭VII→♭VI, ♭VI→V | 10,10,11 | descending-2nds (Phrygian) |
| Circle-of-fifths (full) | IV→viio | 6 | diatonic diminished-5th |

**Both readings, per the D5 stop condition — ruled reading (b) GRAMMAR GAPS, not mis-encodings** (each entry is
musically correct; the §5.0 set descends from the old scoring-bonus signals and omits plagal/ascending-fifth,
descending-second and the diatonic diminished-fifth). The STOP was surfaced with this table; the ruling
(Cowork, 2026-07-02) was **A now / B routed / C rejected**:
- **A (this build):** the consistency test asserts the *true* containment — every pair is licensed OR on the
  explicit ruled known-gap list; any 7th failure, or a listed gap that later passes, turns the suite red. A pin
  plus a tripwire, **not** a silent log. Executed (§4).
- **B (routed to Cowork, NOT this build):** the §5.0 grammar-completion amendment is L5-owned future work
  (L5 spec §15-12); `functionprogression` is untouched this run.
- **C rejected:** the entries are musically correct; data is not re-encoded to fit code.

**Count reconciliation (a verified-facts note for Cowork):** Cowork's addendum and L5 §15-12 cite *"12 motions"*;
the measured count is **11** (Plagal 1 + Axis 1 + Pachelbel 3 + Romanesca 2 + Andalusian 3 + Circle 1). The 11
pairs are enumerated verbatim in the test (§4) and asserted (`EXPECT_EQ(failing.size(), 11u)`). The "12" appears
to double-count one motion; the authoritative set is the measured 11. L5 §15-12's "12-motion" wording is
Cowork-owned — flagged here for Cowork to reconcile at the grammar-completion step.

## 2. Task 1 — the module

### 2.1 Placement + naming (declared decision)
New sub-namespace **`mu::composing::analysis::progression`**, files
`src/composing/analysis/progression/progressionrecognizer.{h,cpp}`, entry point **`recognizeProgressions`**.
Rationale: it is the *consumer* that bridges the Harmonic Vocabulary (the catalog) and Layer 5's committed
progression, producing the Layer-6 annotation — neither the grammar owner (`function/functionprogression`) nor
the catalog owner (`vocabulary/harmonicvocabulary`); a dedicated dir keeps that separation visible and avoids a
name collision with `functionprogression`. American spelling (`recognizer`, `recognizeProgressions`) per the
repo convention, while the module calls the Vocabulary's existing `recognise()`.

### 2.2 The contract (producer-agnostic POD views — the established L5-unit pattern)
- **Input** `CommittedProgression` = `vector<CommittedChord>`; each `CommittedChord` embeds the Vocabulary's own
  `SpanChord` (the recognise-query chord — REUSED, one span type, not two) + ticks + `committed` (Commit/Inherit
  vs abstain) + `compositeConfidence` (the §8 threshold-scaling input) + `rankedCandidates` (the L4 §7 abstained
  readings, each with a §5.5 functional-plausibility score).
- **Output** `ProgressionRecognitionOutput`: the §4.5 `weights` (exposed — the future auto-detect); the §4.4
  `schemaSpans` (progression-schema-spans); the §4.3 `abstainedFeatures` and `overrides`; the §4.6 `sequences`.

### 2.3 The rules as built
- **§4.1 recognition** — `HarmonicVocabulary::recognise` over the committed span (exact matches only, v1;
  substitution-aware). All admitted recognitions carried; schema-spans ordered longer-then-more-specific.
- **§4.5 three phases (forward-only, loop-free)** — (1) weight-free recognise; (2) `w = blend(seed, histogram)`,
  `blend` = `(1-α)·seedNorm + α·histNorm`, `α = E/(E+blendRate)` (E=0 ⇒ w=seed; E→∞ ⇒ histogram dominates);
  (3) prior `= matchScore × max(w over IdiomSet)` (**max, not sum**), × mode-cue factor if the entry's Mode
  contradicts the local key's mode, × chords-only factor if `voiceLeadingDefined`; admission = prior strictly
  above the threshold. Phase-2 input is phase-1 output only.
- **§4.2/§4.4 annotation** — one `ProgressionSchemaSpan` per admitted recognition (name, idiom set, index+tick
  span, match score, prior strength, D7 `chordsOnly` mark, substituted-member read-outs). The literal Roman
  numeral is never changed (D4) — the substitution is recorded only as the read-out.
- **§4.3 evidence (both conditions, SELECTION-only)** — abstained positions: one §5.5 feature naming the ranked
  candidate that fills the member, weighted by the prior; committed positions: the frame-F-B override
  contribution when the literal member demands a different root/quality (substituted members §4.2-excluded). The
  §8 firing (threshold, tie, once-per-pass) is **Layer 5's, not run here** — no new comparison frame.
- **§4.6 sequences** — ALWAYS emitted: a run of ≥2 non-overlapping same-entry recognitions at a constant nonzero
  transposition of the anchor root; typed `{name, step, span, repetitions, prior}`. The §5.3 consumption is
  **F-C-gated, NOT wired** (the output existing is the whole obligation).

### 2.4 Reuse vs new (the firewall discipline)

| Concern | Decision |
|---|---|
| The recognise matcher | **REUSE** `HarmonicVocabulary::recognise` — no second matcher |
| The per-position chord | **REUSE** the Vocabulary's `SpanChord` (embedded in `CommittedChord`) |
| Chord quality / extension | **REUSE** `analysis::ChordQuality` + `Extension` bitmask |
| The licensing grammar | **REUSE** (referenced only, via the D5 map) — never re-implemented |
| Input/output view types, the §4.5 weight vector, the three §4.3/§4.4/§4.6 output types | **NEW** (the consumer's own contract) |
| The §4.5 blend / prior-strength / F-B-contribution rules | **NEW** pure functions, unit-tested in isolation |

## 3. Task 2 — the D5 riders (shown verbatim)

### 3.1 The mirrored cross-comment blocks
Added verbatim (mirror pair) at **`functionprogression.h`** ("the GRAMMAR owner") and **`harmonicvocabulary.h`**
("the CATALOG owner"). Each states the dependency map: *grammar changes → `functionprogression` only; catalog
changes → the Vocabulary only; the two are not derived from each other; the ONE coupling is the consistency test,
one-way (catalog → grammar), in `progressionrecognizer_tests.cpp*`* — plus the ruled known gaps (the 6 entries /
11 motions, ruled grammar gaps, L5 §15-12). (Full text in the committed headers; commit `45000aae70`.)

### 3.2 Doc-sync (same commit set)
- `cowork_progression_schema_dictionary.md`: **§1** the D5 map restatement (one owner per concern + the one-way
  consistency test); **§5.1** the owner note (the licensed-motions list is descriptive, not a second
  implementation — `functionprogression` owns the grammar).
- `cowork_layer5_function_design.md` **§5.0**: the D5 map restatement (this layer is the grammar owner; the
  named progressions live in the Vocabulary; the one-way consistency-test coupling; the ruled grammar gaps →
  §15-12).

### 3.3 The consistency test — final text VERBATIM (per the instruction)
```cpp
TEST(ProgressionRecognizerD5Consistency, EveryCatalogPairIsLicensedOrARuledGrammarGap)
{
    // The ruled known-gap list: (entry name, adjacent-pair start index). Exactly the
    // 6 entries / 11 motions found 2026-07-02, each verdict "musically correct; §5.0
    // grammar gap (L5-owned, L5 §15-12)".
    const std::set<std::pair<std::string, int>> knownGaps = {
        { "Plagal cadence (IV–I)", 0 },                                   // IV→I  delta 7 (plagal / ascending 5th)
        { "Axis (I–V–vi–IV)", 0 },                                        // I→V   delta 7
        { "Pachelbel (I–V–vi–iii–IV–I–IV–V)", 0 },                        // I→V   delta 7
        { "Pachelbel (I–V–vi–iii–IV–I–IV–V)", 2 },                        // vi→iii delta 7
        { "Pachelbel (I–V–vi–iii–IV–I–IV–V)", 4 },                        // IV→I  delta 7
        { "Romanesca (I–V–vi–iii)", 0 },                                  // I→V   delta 7
        { "Romanesca (I–V–vi–iii)", 2 },                                  // vi→iii delta 7
        { "Andalusian cadence (i–♭VII–♭VI–V)", 0 },                       // i→♭VII delta 10 (descending 2nd)
        { "Andalusian cadence (i–♭VII–♭VI–V)", 1 },                       // ♭VII→♭VI delta 10
        { "Andalusian cadence (i–♭VII–♭VI–V)", 2 },                       // ♭VI→V  delta 11 (descending semitone)
        { "Circle-of-fifths (full, I–IV–viio–iii–vi–ii–V–I)", 1 },        // IV→viio delta 6 (diminished 5th)
    };

    HarmonicVocabulary vocab;

    // Scan: every adjacent chord pair of every chord-degree PROGRESSION entry. (Bass-
    // and melody-line skeletons are LINE degrees, not chord-root sequences, so they
    // are outside isLicensedProgression's domain — declared; substitution entries have
    // no skeleton.)
    std::set<std::pair<std::string, int>> failing;
    for (const Entry& e : vocab.entries()) {
        if (e.kind != EntryKind::Progression || e.skeleton.kind != SkeletonKind::ChordDegrees) {
            continue;
        }
        const std::vector<ChordDegreeStep>& steps = e.skeleton.chordSteps;
        for (std::size_t i = 0; i + 1 < steps.size(); ++i) {
            // Realise the key-relative degrees at tonic = C (0); quality carried for the
            // applied-resolution sub-predicate.
            ProgressionChord from{ steps[i].degreeOffset,     steps[i].triadQuality };
            ProgressionChord to{   steps[i + 1].degreeOffset, steps[i + 1].triadQuality };
            if (!isLicensedProgression(from, to)) {
                failing.insert({ e.name, static_cast<int>(i) });
            }
        }
    }

    // (1) Every failure must be a RULED known gap. A failure that is NOT on the list is
    //     a mis-encoded entry OR a new grammar gap — either way, investigate; do NOT
    //     tag around it (D5 stop condition).
    for (const std::pair<std::string, int>& f : failing) {
        EXPECT_TRUE(knownGaps.count(f) == 1)
            << "UNEXPECTED consistency failure at entry \"" << f.first << "\" pair #" << f.second
            << " — either the entry is MIS-ENCODED (fix the Vocabulary) OR a NEW grammar gap "
               "was found (extend functionprogression / L5 §5.0). Do not tag around it.";
    }
    // (2) Every ruled known gap must still be a real failure. If the §15-12 grammar
    //     completion licenses one, it stops failing ⇒ shrink this list + tighten.
    for (const std::pair<std::string, int>& k : knownGaps) {
        EXPECT_TRUE(failing.count(k) == 1)
            << "STALE known-gap: entry \"" << k.first << "\" pair #" << k.second
            << " now PASSES the grammar — remove it from the known-gap list (the §15-12 "
               "grammar completion has landed) and tighten the test.";
    }
    // (3) The measured counts, pinned.
    EXPECT_EQ(failing.size(), 11u);
    EXPECT_EQ(knownGaps.size(), 11u);
}
```

## 4. Task 3 — the oracle test table (16 tests, all green)

| Test | Asserts (design §) |
|---|---|
| `RecognisesPlainIiVITriads` | §4.1 a ii–V–I recognised, longer-span-first ordering |
| `RecognisesTritoneSubstitutedIiVI` | §4.2 the subV member recorded (read-out), literal RN unchanged |
| `EmitsHarmonicSequenceForMonteChain` | §4.6 a ii–V ×3 up a whole step → one sequence (step 2, reps 3) |
| `LoneRecognitionEmitsNoSequence` | §4.6 a single recognition is not a sequence |
| `MixtureNoEvidenceReturnsSeed` | §4.5 phase-2: empty histogram ⇒ w = seed |
| `MixtureEvidenceMovesWeightTowardHistogram` | §4.5 phase-2: evidence moves w toward the histogram |
| `PriorStrengthUsesMaxNotSumOverIdioms` | §4.5 phase-3: max over IdiomSet, never sum |
| `AdmissionThresholdGatesEmission` | §4.5 admission: default admits; a high threshold admits nothing |
| `ModeCueAndChordsOnlyFactorsScaleThePrior` | §4.5 the two soft cues (< 1) scale, and compound |
| `VoiceLeadingDefinedEntryCarriesTheChordsOnlyMark` | §4.4/D7 the chords-only mark (a bass-line Prinner) |
| `AbstainedPositionEmitsSelectionOnlyFeature` | §4.3 abstained: selects an existing candidate, weighted by prior |
| `CommittedOverrideContributionCarriesFBSemantics` | §4.3 committed: F-B contribution, the member is the selection |
| `ExactMatchProducesNoCommittedOverride` | §4.3/§8 the override path is structurally inert under exact match |
| `NothingRecognisedEmitsNothing` | §3 nothing recognised → nothing emitted; weights stay at seed; empty input handled |
| `RecognisedEvidenceMovesTheMixtureWeights` | §4.5 phases 1→2 at the integration level (Diatonic evidence lifts w[0]) |
| `…D5Consistency.EveryCatalogPairIsLicensedOrARuledGrammarGap` | Task 2.1 (§3.3 above) |

## 5. §7 dev-bed validation (read-only; the dormant consumer over the DCML dev beds)

Mechanism: `batch_analyze --dump-progressions` (default OFF — the established diagnostic pattern; fullspine output
byte-identical without it) builds the committed progression from each spine's chord-bearing slices (the L4
committed reading + local key + composite confidence + ranked alternatives) and runs `recognizeProgressions` with
the equal seed and default params. `compare_progressions_oracle.py` grades it over the 16 dev beds against the GT
`cadence` column (±one-beat, the same tick basis as `compare_l6_oracle`).

**Full sweep — 16 dev beds, 718 movements (recognition census + cadence-span P/R).** `cov%` = positions under
≥1 admitted recognition; `abst`/`ovr` = §4.3 abstained-feature / committed-override counts; `cadP/cadR` = cadence-
span precision/recall vs the GT `cadence` column; `jp` = jazz/pop-family (empirically-unvalidated) recognitions.

| corpus | mv | positions | spans | cov% | seq | abst | ovr | cadP | cadR | jp |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| ABC (no cadence GT) | 70 | 65391 | 1714 | 5.2 | 15 | 1879 | 0 | — | — | 16 |
| bach_en_fr_suites | 89 | 16463 | 410 | 4.9 | 1 | 612 | 0 | 17.9 | 12.2 | 5 |
| chopin_mazurkas | 55 | 16859 | 615 | 7.2 | 8 | 520 | 0 | 13.3 | 22.1 | 9 |
| corelli | 149 | 16917 | 663 | 7.8 | 1 | 857 | 0 | 15.3 | 9.3 | 8 |
| cpe_bach_keyboard (0 regions) | 66 | 0 | 0 | 0.0 | 0 | 0 | 0 | — | — | 0 |
| dvorak_silhouettes | 12 | 3060 | 101 | 7.0 | 0 | 108 | 0 | 26.6 | 18.0 | 6 |
| grieg_lyric_pieces | 66 | 18928 | 440 | 4.6 | 3 | 412 | 0 | 13.8 | 13.2 | 20 |
| mozart_piano_sonatas | 54 | 34224 | 1200 | 7.0 | 7 | 1668 | 0 | 16.9 | 17.8 | 8 |
| schumann_kinderszenen | 13 | 1509 | 63 | 8.3 | 0 | 63 | 0 | 35.5 | 27.8 | 0 |
| tchaikovsky_seasons | 12 | 5514 | 159 | 5.7 | 0 | 138 | 0 | 28.2 | 23.8 | 2 |
| beethoven_piano_sonatas | 64 | 51032 | 1265 | 5.0 | 10 | 1474 | 0 | 18.6 | 16.7 | 16 |
| wagner_overtures (no cadence GT) | 2 | 2124 | 33 | 3.2 | 2 | 33 | 0 | — | — | 3 |
| liszt_pelerinage | 19 | 16431 | 185 | 2.2 | 2 | 214 | 0 | 18.0 | 11.8 | 3 |
| rachmaninoff_piano | 22 | 2394 | 37 | 3.1 | 0 | 46 | 0 | 21.6 | 16.3 | 0 |
| schulhoff_suite_dansante_en_jazz | 6 | 1019 | 11 | 2.2 | 0 | 18 | 0 | 36.4 | 11.1 | 0 |
| monteverdi_madrigals (no cadence GT) | 19 | 4805 | 133 | 5.5 | 0 | 138 | 0 | — | — | 3 |
| **TOTAL** | **718** | **256670** | **7029** | **5.4** | **49** | **8180** | **0** | — | — | **99** |
| **cadence-GT-bearing (12 beds)** | 601 | | 4979 spans | | | | | **17.4** | **15.3** | |

Admitted-span histogram (all beds): Authentic V–I **3469**, Plagal IV–I **1164**, Authentic minor V–i **1120**,
Phrygian-half **385**, Deceptive minor **347**, Deceptive **316**, ii–V–I triads **92**, Incomplete ii–V **72**,
Descending-thirds **22**, Doo-wop **14**, Prinner **12**, Backdoor **5**, Axis **4**, iiø7–V7–i **3**, Lament **3**,
Turnaround I–vi–ii–V **1**.

**Notes on the table.** (a) `ovr = 0` on **all 718 movements** — the empirical confirmation of the committed-
override structural inertness (§2.3/§7-U). (b) ABC / wagner / monteverdi carry **no `cadence` GT column** (gt=0),
so cadP/cadR are undefined ("—"), not zero accuracy; the ABC 1714 unmatched spans are excluded from the honest P/R.
(c) `cpe_bach_keyboard` produces **0 positions** — the documented C.P.E. Bach sparse-texture 0-region substrate
property (a Layer-2 admission matter, not a consumer issue). (d) The honest cadence-span P/R on the 12 GT-bearing
beds is **≈17% precision / 15% recall** — the exact-match v1 ceiling (§8): the recogniser catches the 2-chord
cadence formulas (the histogram is cadence-dominated) and misses seventh/inverted/interpolated realisations. The
multi-chord entries (ii–V–I, turnarounds, sequences) fire rarely — precisely the under-recognition §7 exists to
size, and the target of the Stage-5 partial matcher.

**Reading the numbers.**
- **Coverage sizes the exact-match under-recognition (design §8).** v1 admits only exact realisations, so coverage
  is low — most real cadences involve sevenths / inversions / interpolated chords the exact matcher misses. This
  is the measurement §8 predicted; the Stage-5 partial matcher is where it moves.
- **`ovr` (committed overrides) is 0 everywhere.** This is the *structural* inertness of the §4.3 committed-override
  path under exact-match v1 (a literal member matches the committed reading by construction; a substituted member
  is §4.2-excluded) — built and directly unit-tested, live at Stage-5 partial matching. It is a scaffolding
  property, not a bug.
- **Cadence-span precision/recall** grades OUR recognised cadence schema-spans (Authentic/Plagal/Deceptive/
  Phrygian-half, arrival ≈ span end) against the GT `cadence` markers. Low recall is again the exact-match ceiling.
- **The evidence-contribution as RN-accuracy CHANGE on covered positions (design §7) is NOT produced.** The §5.5
  feature and §8 override are DORMANT (not wired into Layer 5), so an end-to-end RN-accuracy delta cannot be
  measured without engagement; coverage is the honest proxy (the surface the contribution would act on). Marked,
  not faked.
- **Jazz/pop mark.** `jp` counts recognitions carrying a jazz/pop-family idiom with no common-practice idiom;
  these carry the **empirically-unvalidated** mark (no score-aligned jazz/pop GT on these beds — the census Tier-J
  want, dictionary §8 / design §7).

## 6. Declared decisions

1. **Placement/naming** (§2.1) — a dedicated `progression/` sub-namespace beside the L5 units.
2. **The recognise-query chord at abstained positions** — the caller supplies the top-ranked candidate as
   `CommittedChord.chord` (there is no committed chord at an abstain); `rankedCandidates` is read only by the §4.3
   feature. In the dump this is the L4 final reading; `committed = !uncertain`.
3. **§4.5 declared defaults** (NOT tuned; directions fixed by §4.5): `blendRate = 1.0`; `admissionThreshold = 0.0`
   (inert-permissive floor); `modeCueFactor = 0.5`; `chordsOnlyFactor = 0.5`. The seed defaults to all-equal
   (no preset→idiom map is wired — that is a consumer/preset joint decision, dictionary §12, not this build).
4. **§4.6 sequence shape** — repetitions = the count of matched windows in the run (≥2); a single recognition of an
   internally-sequential entry (circle-of-fifths, Monte) is NOT counted as a repeat (see Unknown U1).
5. **§4.3 for line-defined entries** — a bass/melody-line member is a line degree, not a chord, so line entries
   contribute no §4.3 chord evidence (they still emit the §4.4 annotation with the D7 mark).
6. **Consistency-test domain** — chord-degree progression entries only; bass/melody-line and substitution entries
   are outside `isLicensedProgression`'s chord-root-motion domain (declared in the test).
7. **The committed-override path is present but structurally inert under exact-match v1** — built for Stage-5,
   directly unit-tested (§4.3 semantics), and asserted empty end-to-end (`ExactMatchProducesNoCommittedOverride`).

## 7. Unknowns / items declared to Cowork (no inference-problem coding)

- **U1 — §4.6 single vs repeated sequences.** The spec defines a harmonic sequence as "the same progression
  repeated at successive transpositions"; the build requires ≥2 transposed windows. Whether a *single* recognition
  of an internally-sequential entry (circle-of-fifths, Monte, Fonte) should itself emit a sequence (with an
  internal step/repeat count) is a spec ambiguity — declared, not resolved. Left as ≥2-window repetition.
- **U2 — the "12 vs 11 motions" count** (§1) — the measured known-gap count is 11; Cowork's §15-12 says 12.
  Reconcile at the grammar-completion step; the measured 11 is authoritative and pinned in the test.
- **U3 — the evidence contribution's RN-accuracy delta** is unmeasurable while the feature is dormant (§5); it
  becomes measurable at engagement (the §5.5 feature + §8 override wired into Layer 5).
- **U4 — the L6 `SchemaSpan` host** carries the stale "sequence-span" wording (predates the D6
  `progression-schema-span` rename); renaming that struct is the Cowork doc-pass propagation rider, not this build.
  No wiring to L6 was done (dormant).
- **No inference problems were encountered inside the module** — the module recognises what the layers already
  decided; every accuracy question (under-recognition, the partial matcher) is a declared Stage-5 item, not fixed.

## 8. Gate + dormancy proof

- **Corpus gate — EXACT.** Baroque **53**, Jazz **24**, Default **53** (`characterise_bir_false.py` on the
  per-preset validated dirs; first cases match the documented sets, e.g. `bwv10.7@36000`). Byte-identical
  production by construction: the only changes to existing code are comment-only header edits + a default-OFF
  tools dump; the module has no production caller.
- **Suites — green, no golden refresh.** composing 1051 (+16), pipeline snapshot 11, notation 53.
- **Dormancy — grep-proven.** `recognizeProgressions` is called only from `progressionrecognizer_tests.cpp`
  (12 sites) and the default-OFF `batch_analyze --dump-progressions`; no `src/` production file includes
  `progressionrecognizer.h`.

## 9. Commits (local, unpushed, fork-only)

| Commit | Change class |
|---|---|
| `3ccf963b8f` | the dormant module + CMake registration |
| `45000aae70` | oracle tests + the D5 consistency test + the mirrored cross-comments + doc-sync |
| `1d23be8984` | `--dump-progressions` + `compare_progressions_oracle.py` (§7 validation) |

Cowork's out-of-band working-tree edits (ARCHITECTURE.md, STATUS.md, cowork_design_doc_template.md,
cowork_layer6_grouping_design.md, cowork_progression_schema_design.md, the two `cowork_spec_polish_findings_*`)
were **left untouched** — not staged into any commit.

---
*Report lines: 335.*
