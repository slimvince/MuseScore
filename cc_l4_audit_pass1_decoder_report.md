# CC REPORT — Layer-4 (chord) audit, PASS 1 (blind), session 1 of 3: the dormant slice decoder

> **EG-7 / OI-84 / OI-102.** Session 1 of the three-way split of the layer-4 pass-1
> row work (register row OI-102). Files audited: `chord/chordslicedecoder.h` and
> `chord/chordslicedecoder.cpp` (the dormant-but-surviving per-slice chord-symbol
> decoder). Protocol: `cowork_audit_protocol.md` — P1 inventory (inherited), P2
> dispositions, P3 contract-direction, P4 behavioral characterization. **Blind first
> pass**: the signature sweep (P8 pass 2) and certification are NOT done here.
>
> **Read-only fact-finding.** No production behavior changed; no constant tuned; no
> golden refreshed; `tools/robust_stop/` and `tools/corpus/` untouched. No
> instrumentation was added — behavioral characterization used only existing default-OFF
> diagnostics (`--decode-chords`, `--dump-fullspine`) and the test suite, so no rebuild
> and no byte-identity question arises.

## 1. Scope, provenance, and when the withheld files were opened

- **Population:** all three inventory files tag this decoder `L4-DECODER` — the
  **dormant-but-surviving** population (b): not on the production path (reachable only
  through `batch_analyze --decode-chords` / `--dump-fullspine` and the test suites), but
  it is the engagement's clean target, audited as surviving code in full. The tag was
  re-affirmed per row; no mis-tag found on these two files.
- **Inventory source:** the committed layer-4 inventory (`tools/audit/l4/*.csv`,
  `manifest.json`; inventory HEAD `7f57aad4b5`, corpus `c50002fee1`). Rows whose file is
  `chordslicedecoder.{h,cpp}`: **311** — 43 functions, 8 cross-layer includes, 61 fields,
  72 literals, 127 branches. This matches the ~311 the split instruction anticipated.
- **Session HEAD:** `d9e1912aaa` (ancestor check vs `d9e1912aaa` passed). Corpus
  `c50002fee1` (352 stems; `tools/corpus/baroque/corpus_manifest.json` git_hash
  confirmed).
- **Withheld files first opened:** none opened during the blind pass (Tasks 0–3). The
  Task-4 unblind reads (`OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `STATUS.md`, the parent
  `cc_l4_audit_pass1_report.md`) are recorded in §7 with their reconciliation.

## 2. Disposition summary (protocol P2)

Every one of the 311 rows carries a closed-set verdict in
`tools/audit/l4/pass1_dispositions_decoder.csv/.json`. "No issue" is a recorded claim
with a stated reason.

| Row kind | Verdict tally |
|---|---|
| function (43) | SURVIVES 43 |
| cross-layer include (8) | SURVIVES 8 |
| field (61) | PUBLISHED 30 · SURVIVES(setting/internal) 28 · TRAPPED 2 · SILOED 1 |
| literal (72) | ESTABLISHED 63 · UNFIT 9 |
| branch (127) | SURVIVES 127 |

- **Functions / branches — SURVIVES throughout**, as expected for the engagement's clean
  target. Four functions and the whole `decodeSelection` family are **declared-dormant
  staging** (`redecodeRange`, `decisionIsRelevant`, `edgeClampAtSlice`,
  `edgeIncrementTicks`, `decodeSelection`) — reached only by the tests, never by the
  live decode route; the header documents each as dormant.
- **Fields — the fact-publication check (the instruction's emphasis).** Everything the
  decoder computes per slice that a layer above needs **reaches an output surface**:
  the chosen chord, the ranked alternatives (∪ prevailing), the margin/confidence, the
  commit/inherit/abstain decision, the composite-confidence model, the named open
  question + its two competing readings, the per-note chord-tone/non-chord-tone
  membership, and the L4→L5 extension carry (with an honest-carry known/unknown flag).
  30 fields are PUBLISHED on `--decode-chords` and/or `--dump-fullspine` and consumed
  (present or named-future). **No genuine silo** — every derived fact is either published
  + consumed or declared-dormant with a named future consumer. Three fields are flagged
  (§4).
- **Literals — 9 UNFIT** are the decoder's hand-set tunable **seeds** (window sizes,
  thresholds, weights, caps), documented in the header as "sensible seeds, not tuned
  values" to be swept later on this dormant path. **Only 1 of the 9**
  (`sufficiencyChordTones`) appears in `tools/param_manifest.json` (see §4, finding).
  The other 63 literals are ESTABLISHED structural constants (pitch-class cardinality
  12, interval/cardinality math, `[0,1]` clamps, divide-by-zero epsilons, documented
  sentinels).

## 3. Contract-direction check (protocol P3)

From `ARCHITECTURE.md` §"Layer 4 — the per-slice chord-symbol decoder" and the roadmap's
engagement stage, the decoder must: **decode a chord symbol per Layer-2 slice against the
one scorer's candidate cube, carry the alternatives, commit / inherit / abstain with a
stated margin, and hand a governed result forward.** Each expected behavior located in
the code:

| Contract expectation | Located in code | Status |
|---|---|---|
| One scorer, no second scorer | `candidatesForWindow` runs `analyzeChord` + projects its cube; `verticalScore` == `DiagnosticOracleCell::verticalScore` | ✅ present, #6-clean |
| Per-slice window over the indexed L1 view | `adaptiveWindow` + `eligibleNotesInSpan` over `weightedPcView` / `NoteModel::overlapping` | ✅ present (no region aggregate / DOM walk) |
| Choose the winner; rank + cap alternatives; ∪ prevailing | `decideSlice` | ✅ present (topK cap binds on 100% of slices) |
| Confidence = margin to the best DIFFERENT chord | `decideSlice` (excludes inversions + spelling-resolved siblings) | ✅ present |
| Commit / inherit / abstain + sufficiency gate (G1) | `applyCommitDecision` | ✅ present (Commit 34.4% / Inherit 3.0% / Abstain 62.6%) |
| Per-note chord-tone / NCT membership (G2/G3) | `classifyMembership` + the three-tier `classifyTone` ladder | ✅ present |
| Composite confidence + named open question (G6) | `computeConfidence` + `nameOpenQuestion` + `populateForwardContract` | ✅ present, representational-only |
| Symmetric-root spelling-pin (G4/C1) via the shared spelling primitive | `spellingPinnedRoot` → `symmetricRotationSet` / `spellingRootOf` via `engravingbridge::lineOfFifths` | ✅ present, one spelling reader |
| L4→L5 carry: alternatives, margins, membership, per-note evidence, open questions, extensions | the `SliceChord` / `ChordSliceCandidate` DTO surface (§2 fields) | ✅ complete |
| Byte-identical production (dormant, returns before `analyzeScore`) | `--decode-chords` / `--dump-fullspine` diagnostic paths only; no production caller | ✅ dormant |

**Absences (findable only in this direction) — none that are decoder defects.** Two
deliberate contract boundaries were confirmed, not missing:
- The decoder does **not** run the post-scoring gates (`applyPostScoringGates`, Gates
  A–L) — those are the *retiring* population, and their key-function chord reselections
  are to be re-homed in Layer 5, not the decoder (the decoder abstains where the gates
  would have reselected, handing the open question forward). This is the documented
  engagement design, not an absence.
- The four-note dim7 / minor-major chord TYPES (Increment C2 / G5) are deferred to the
  engage step (they would move the shared production catalogue). The decoder's
  spelling-pin therefore resolves dim7 rotations from the *existing* diminished triad +
  the four dim7 pcs; this is documented and is why one G6 ambiguity kind is currently
  unreachable (§4).

The scoring-doc sync invariant was checked from the decoder side: `docs/scoring_model.md`
§2 states `kTemplateCount = 17`; `chordanalyzer.cpp` declares
`std::array<TemplateDef, kTemplateCount>` with a `static_assert`. The decoder consumes
`kTemplateCount` / `kTemplateIntervals` as the single source (`templateToneCount`) — no
drift, no second interval set.

## 4. Flagged rows (each with file:line and a plain-language sentence)

Findings are recorded as candidate register rows; none is a patch (guiding principle 8).
Register reconciliation is in §7.

1. **param_manifest coverage gap** — `chordslicedecoder.h:165–314` (the settings block).
   The decoder has ~13 tunable settings; **only `sufficiencyChordTones` (h:263) is
   inventoried in `tools/param_manifest.json`** (group G11). The other seeds
   (`uncertaintyMargin`, `topK`, `contextSlices`, `maxContextSlices`, `minHarmonyPcs`,
   `minDistinctPcs`, `membershipSalienceThreshold`, `membershipReferenceDurationQn`,
   `membershipPenaltyWeight`, `stepwiseGapToleranceTicks`, `maxEdgeExtendSteps`,
   `edgeExtendIncrementSlices`) are absent from the fitter's fit-surface inventory. In
   plain words: the decoder's tunable knobs are not fully listed on the one page that is
   supposed to list every fittable number, so a future sweep could miss most of them.
2. **`AmbiguityKind::SymmetricRotation` never fires** — `chordslicedecoder.cpp:966–967`.
   This open-question label is produced only when two *augmented* rotations compete at an
   abstain; the dim7 case awaits the deferred G5 four-note type. It fires on **0 / 29080**
   corpus slices and has **no dedicated behavior test**. In plain words: one branch of the
   "why is this ambiguous" labeller is currently unreachable and untested — expected while
   G5 is deferred, but worth tracking so it is exercised when G5 lands.
3. **`OpenQuestionLabel::contestedPc` reserved, never populated** —
   `chordslicedecoder.h:423`. Always `-1`; `OpenQuestion::NoteMembership` is never
   produced. The header declares it reserved for a future per-note-membership open
   question. In plain words: a field and an enum value that nothing writes yet — declared
   dormancy, not waste, but flagged so it is not mistaken for a live signal.
4. **`SliceChord::clippedBySelectionEdge` / `cueDenied` set only by the dormant
   `decodeSelection`** — `chordslicedecoder.h:459–460`. No live route (neither
   `--decode-chords` nor `--dump-fullspine`, both of which call `decode()`) ever sets or
   reads them; only the dormant bounded-context `decodeSelection` does. In plain words:
   two provenance flags that are real but currently reachable only through code that has
   no caller — declared dormancy (the bounded-context design names the future selection
   consumer).
5. **`isSemitoneStep` is misnamed** — `chordslicedecoder.cpp:242–246`. It returns true for
   `|pitch1 − pitch2|` of 1 **or 2** semitones — i.e. a minor *or major* second — so it is
   a "melodic step (≤ major 2nd)" test, matching its own comment but not its name. In
   plain words: the function does the right thing (both step sizes count) but its name says
   "semitone", which could mislead a future reader.
6. **`param_manifest.json` consuming-path note understates the diagnostic caller** —
   `tools/param_manifest.json` (G11 / D9). It states the decoder is referenced "ONLY by
   the dormant L5 function headers … NOT by regionanalyzer/batch_analyze/bridges", but
   `batch_analyze.cpp` **does** call `ChordSliceDecoder::decode` on the `--decode-chords`
   and `--dump-fullspine` diagnostics. This is a stale note in the fitter manifest (an
   instrument doc), not a decoder defect.

**Boundary note (not a decoder verdict — deferred to the scoring-oracle / L5 session).**
`chordslicedecoder.cpp:30` includes `function/harmonicfunctionlayer.h` (an L5-named TU)
for `ScoringSnapshot` / `ScoringCell` (the scorer's candidate cube) and
`bassIsTemplateChordTone` (the chord-tone oracle). These are L4-scorer concerns declared
in an L5-named header — a layer-*home* question. The decoder's reuse is correct (one cube,
one chord-tone oracle, no duplication); where the cube types should *live* belongs to the
oracle session (session 2) and likely coincides with the `harmonicfunctionlayer` rename.

## 5. Behavioral characterization (protocol P4)

Two reachable routes; the per-row route is in the disposition CSV's `fire_route` column.
Numbers are generated (`tools/audit/l4/pass1_decoder_aggregate_*.py`,
`pass1_decoder_behavior.txt`), corpus `c50002fee1`, Baroque, 352 stems / 29080 slices.

**Route A — test suite** (`composing_tests` → `Composing_DecodeChord`): **67/67 pass**
(1101/1101 overall, 2 disabled). The 67 tests cover every public method and every
mechanism tier: `Decide_*` (ranking / margin / alternatives / prevailing / empty),
`G1_*` (commit / inherit / abstain / sufficiency / phantom-root), `Memb_*` (the three
ladder tiers, suspension, Cadd9 discriminator, plausibility penalty), `SpellingPin_*`
(dim7, augmented, absent, contradicted, disabled, non-symmetric, plain-dim), `G6_*`
(composite + open-question kinds), `TwoReading_*` (continuation vs transition), `EDGE1–7`
(the dormant `decodeSelection` + edge extension), and `Fixture_*` (note-model end-to-end,
`redecodeRange`, determinism). **Gap:** no dedicated test for
`AmbiguityKind::SymmetricRotation` (finding §4.2).

**Route B — `--decode-chords`, full corpus** (notated key):

| Mechanism | Fire count | Rate | Matches documented intent? |
|---|---|---|---|
| `decode` / `decideSlice` (all slices) | 29080 | 100% | yes |
| commit ∪ inherit (`hasChord`) | 10877 | 37.4% | yes — "proven where it commits" |
| abstain (`!hasChord`) | 18203 | 62.6% | yes — "abstains where function decides" (seed `uncertaintyMargin`) |
| alternatives carried (≥1) | 29080 | 100% | yes — carried readings for the engagement |
| topK cap binds (≥6 alts) | 29080 | 100% | yes — the cube always exceeds topK |
| membership NCT non-empty | 1676 | 5.8% | yes |
| no-competitor sentinel (`kNoCompetitorConfidence`) | 0 | 0% | **never fires on corpus** — defensive/degenerate branch (test-covered) |
| committed quality Augmented / Diminished | 6 / 0 | — | spelling-pin population is rare on Baroque; dim sonorities largely abstain |

**Route C — `--dump-fullspine`, full corpus** (live home key; the decision + open-question
fields `--decode-chords` does not emit):

| Mechanism | Fire count | Rate |
|---|---|---|
| Commit | 10004 | 34.4% |
| Inherit | 882 | 3.0% |
| Abstain | 18194 | 62.6% |
| openQuestion Root / Quality / None | 17345 / 849 / 10886 | 59.6 / 2.9 / 37.4% |
| ambiguity TransitionVsContinuation | 8790 | 30.2% |
| ambiguity CloseReading | 4438 | 15.3% |
| ambiguity ShareTone | 3343 | 11.5% |
| ambiguity InsufficientEvidence | 1018 | 3.5% |
| ambiguity RelativePair | 605 | 2.1% |
| ambiguity **SymmetricRotation** | **0** | **0% (never — finding §4.2)** |
| composite confidence < 0.5 | 16198 | 55.7% |
| chosen extension known / honest-unknown | 16777 / 12303 | — |

Routes B and C agree on the abstain total to within 9 slices (18203 vs 18194 — the
key-source difference), confirming both measurements. Every G1/G6 branch fires in a
realistic proportion **except** `SymmetricRotation` (finding §4.2) and the three master
switches' OFF-arms + the `decodeSelection` family (dormant / test-only, expected).
`fire rate not measured` on the corpus for: the spelling-pin (no emitted pinned-flag —
test-confirmed instead) and `redecodeRange` / `decodeSelection` (no corpus caller —
test-only).

**Read of the numbers:** the 62.6% abstain and the dominant TransitionVsContinuation
ambiguity are consistent with the documented conservative decoder ("abstains where
function decides") at the default seed `uncertaintyMargin = 0.5`; the abstain population
is mostly 3–4-pitch-class slices (low margin), not thin phantom-root slices. This is a
fire-rate observation, not an inference-quality claim (grading is out of scope).

## 6. Retiring-code note

None. Both audited files are population (b) `L4-DECODER` in full; there is no retiring
(population (a)) code in the decoder. (The retiring gates / competition live in
`postscoringgates.cpp` / `function/` and are other sessions' scope.)

## 7. Unblind reconciliation (Task 4)

_To be completed after the Task-3 freeze lifts the withheld list: read `OPEN_ITEMS.md`,
`DEFECT_TYPES.md`, `STATUS.md`, `cc_l4_audit_pass1_report.md`; reference existing rows
where findings coincide; open new register rows for genuinely new findings; promote any
new problem type into `DEFECT_TYPES.md`._
