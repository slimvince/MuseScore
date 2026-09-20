# CC — Architectural Layer 4 (CHORD SYMBOL + NON-CHORD TONES) read-only pre-build audit dossier

**Status:** READ-ONLY pre-build audit complete. **No production code changed; no behaviour change; no corpus
regenerated; no production commit; `upstream` untouched.** Output is this dossier only. Cowork verifies the citations +
that nothing production changed; user ratifies; THEN the Layer-4 build begins.

**Spec:** `cowork_layer4_chordsymbol_design.md` (SIGNED, user, 2026-06-22). **Models this audit:**
`cc_layer3_decoder_audit_dossier.md` — the prior Layer-3 read-only pre-build audit, whose structure and rigor this
dossier follows. Cited as **[L3-audit]**; some of its line numbers predate the L3 wiring commit `a6b08af3fe`, so the
seam line numbers below were re-confirmed at HEAD this session and supersede it where they differ.

**No-assume rule:** every as-is statement cites `file:line` from a source read **this session**. The chord-path core
(§1, §2, §4, §5-seam) was read line-by-line by the main session. Breadth items (the note-model query API, the window
builders' signatures, the metric tooling, the test-fixture inventory) were gathered by read-only sub-agents this
session and the **load-bearing** ones (`NoteModel::overlapping` usage, the `NoteEvent` fields, the result cap, the
template count) were re-verified by the main session; items NOT main-session-verified are tagged **[agent-sourced]** at
the citation and the genuinely-unconfirmable ones are listed in §8. Nothing is guessed.

---

## §0 — Headline findings (decision-relevant)

1. **The complete candidate cube already exists internally and is surfaced byte-identically — exactly the L3-style
   reuse lever.** `analyzeChord` builds a `fn::ScoringSnapshot` whose `cells` vector is **every (bass × root × template)
   candidate** — `bassCandidates.size() × 12 × kTemplateCount(17)` cells, each with its vertical fit score
   ([`chordanalyzer.cpp:1390-1432`](src/composing/analysis/chord/chordanalyzer.cpp#L1390-L1432)) — and moves it out
   through the optional `snapshotOut` parameter with zero behaviour change when null
   ([`chordanalyzer.cpp:1481-1483`](src/composing/analysis/chord/chordanalyzer.cpp#L1481-L1483)). **But the public
   return is capped at top-3** (`if (results.size() >= 3) break;` —
   [`harmonicfunctionlayer.cpp:509-515`](src/composing/analysis/function/harmonicfunctionlayer.cpp#L509-L515)). So
   **"complete generation is the lever" (spec §4) is satisfiable by surfacing the snapshot cube the same way the L3
   decoder surfaced the 252-candidate key dump** — no new scorer. **Feasibility: confirmed.**
2. **The candidate cube is over QUALITY TEMPLATES ONLY; extensions/6ths/dim7/9ths are detected AFTER ranking, on the
   single winner.** The 17 templates ([`chordanalyzer.cpp:1198-1216`](src/composing/analysis/chord/chordanalyzer.cpp#L1198-L1216))
   are the triads + a fixed set of sevenths/sus shells; the 6th, dim7, 9/11/13 and alterations are an **`Extension`
   bitmask** computed by `detectExtensions()` **inside `buildChordResult()`** on the chosen cell only
   ([`chordanalyzer.cpp:870-892`](src/composing/analysis/chord/chordanalyzer.cpp#L870-L892)), not a dimension of the
   candidate cube. **This is the single most important §1/§7 reconciliation point** (detailed in §1.4 + §8-contradiction-A):
   the spec's "complete generation" is over *every tertian chord*; the as-is cube is complete only over the 17 quality
   shells, with the extension axis resolved post-hoc on the winner. Not a blocker — but the build must decide whether
   the L4 candidate list keeps the template×extension factoring or enumerates the extended set.
3. **The chord scorer already consumes a FLATTENED region aggregate — this IS the "union recompute" the spec replaces.**
   `analyzeChord` builds a 12-bin `pcWeight` histogram by summing every tone's weight
   ([`chordanalyzer.cpp:974-986`](src/composing/analysis/chord/chordanalyzer.cpp#L974-L986)); no per-note identity
   survives into scoring. **No per-note chord-tone-vs-NCT membership decision exists anywhere in `src/composing`** — the
   sole per-note membership predicate is `cptIsBassChordTone()` (bass-vs-pedal only)
   ([`chordpostpasses.cpp:43-107`](src/composing/analysis/chord/chordpostpasses.cpp#L43-L107)). The spec's per-slice,
   neighbour-aware, two-pass membership decision (spec §4-§5) is **largely new** — confirmed.
4. **tpc IS threaded into the chord path, but the symmetric-dim7 root is selected by KEY non-diatonicity, not by
   notated spelling.** Every tone carries `tpc` ([`chordanalyzer.h:90`](src/composing/analysis/chord/chordanalyzer.h#L90)),
   the scorer reads it (`tpcConsistencyBonus`, `scoreExtraNotes` sus/min disambiguation, `countTpcMatches`), and the
   root is *named* from spelling (`rootTpc = ctx.tpcForPc[rootPc]` —
   [`chordanalyzer.cpp:870`](src/composing/analysis/chord/chordanalyzer.cpp#L870)). **But the dim7 rotation is chosen
   by `dim7CharacteristicBonus`, which rewards the rotation whose ♭♭7 is *non-diatonic in the current key***
   ([`chordanalyzer.cpp:452-485`](src/composing/analysis/chord/chordanalyzer.cpp#L452-L485)) — a **key-dependent**
   selector that *moves with the key* (the very rotation churn CLAUDE.md class-(a) tracks), **not** the deterministic
   spelling-pin the spec mandates (spec §5/§9). The spelling-aware, key-independent dim7/aug root is the **largely-new**
   part of §4 — aligned with the spec calling it new. (Augmented falls back to *bass* when tpc is absent —
   [`chordanalyzer.cpp:846-867`](src/composing/analysis/chord/chordanalyzer.cpp#L846-L867).)
5. **The result carrier lacks the spec's certainty/membership fields.** `ChordAnalysisResult = { identity, function }`
   ([`chordanalyzer.h:296-299`](src/composing/analysis/chord/chordanalyzer.h#L296-L299)) — **no confidence, no
   "uncertain" mark, no chord-tone set, no non-chord-tone set.** Ranked alternatives exist only at the *region* level
   (`region.alternatives`, a `≤2`-entry `vector<ChordAnalysisResult>` —
   [`regionanalyzer.cpp:785-788,831`](src/composing/analysis/region/regionanalyzer.cpp#L785-L788)). The spec §7 result
   (chord-tone set + NCT set + ranked alternatives + confidence + "uncertain") needs **new carrier fields** — newly
   written.
6. **The window/index floor is ALREADY met for chords (better than L3's start).** The chord tone collector
   `weightedPcView` queries the **indexed** `NoteModel::overlapping` over `[startTick,endTick)`
   ([`regiontonecollector.cpp:217`](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L217)); the indexed
   span-anchored key-context builder `pitchContextOverSpan` does the same
   ([`regiontoneprimitives.cpp:242`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L242)).
   `NoteModel::overlapping` is O(log N + result)
   ([`note_model.h:97,158`](src/composing/analysis/notemodel/note_model.h#L97-L158)). **Unlike L3** (whose legacy
   `collectPitchContext` is an un-indexed DOM walk), the chord path's reusable window builder is **already on the
   index** — so the per-slice perf floor is met by construction if the build reuses `weightedPcView`/`pitchContextOverSpan`.
7. **The production seam is one call site, re-confirmed at HEAD (shifted by the L3 wiring).** The live per-region chord
   call is `chordAnalyzer->analyzeChord(tones, localKeyFifths, localKeyMode, &temporalCtx, attemptPrefs, &gateCtx)` at
   [`regionanalyzer.cpp:763-764`](src/composing/analysis/region/regionanalyzer.cpp#L763-L764) — **not ~:668** (that was
   the [L3-audit]-era number; the L3 decoder wiring `a6b08af3fe` shifted it). `localKey` is now the L3 decoder's key
   ([`regionanalyzer.cpp:730-733`](src/composing/analysis/region/regionanalyzer.cpp#L730-L733)). This per-region call is
   what the L4 build re-points **per-slice**.
8. **No NCT-membership metric exists; the BIR two-tier gate is doc-only.** The chord-root (BIR) + quality metric tooling
   is present (`characterise_bir_false.py`, `oracle_root_metric.py`, `analyze_inversion_errors.py`, `compare_rn.py`),
   but **no per-note chord-tone-vs-NCT precision/recall metric exists** (spec §10 build deliverable), and the
   "two-tier" symmetric/decidable split lives only in CLAUDE.md prose, not in `characterise_bir_false.py` code
   ([agent-sourced]; §6).

---

## §1 — The existing chord scorer (the reuse core)

### §1.1 — Template set and `kTemplateCount` (the recognized vocabulary)
- **`kTemplateCount = 17`** ([`chordanalyzer.h:74`](src/composing/analysis/chord/chordanalyzer.h#L74)) — single source of
  truth for every template-sized array (the `templates` array, the three score matrices, and `kMasks` in
  `harmonicfunctionlayer.cpp`). Cross-checked against `docs/scoring_model.md §2` ("currently 17" —
  [`docs/scoring_model.md:72-73`](docs/scoring_model.md#L72-L73)): **in sync.** Compile-time `static_assert` enforces
  extent ([`chordanalyzer.cpp:1217-1218`](src/composing/analysis/chord/chordanalyzer.cpp#L1217-L1218)).
- **The 17 templates** ([`chordanalyzer.cpp:1198-1216`](src/composing/analysis/chord/chordanalyzer.cpp#L1198-L1216)),
  each `{quality, intervals-from-root, tpc-deltas-from-root}` (`TemplateDef` —
  [`chordanalyzer.cpp:340-344`](src/composing/analysis/chord/chordanalyzer.cpp#L340-L344)):

  | # | quality | intervals | gloss |
  |---|---|---|---|
  | 0 | Major | {0,4,7} | major triad |
  | 1 | Major | {0,4,7,11} | maj7 |
  | 2 | Major | {0,4,7,10} | dom7 |
  | 3 | Major | {0,4,6,10} | dom7♭5 |
  | 4 | Minor | {0,3,7} | minor triad |
  | 5 | Minor | {0,3,7,10} | min7 |
  | 6 | Diminished | {0,3,6} | diminished **triad** |
  | 7 | Suspended4 | {0,5,6,10} | sus4♭5 (precedes HalfDim, tie-break) |
  | 8 | HalfDiminished | {0,3,6,10} | ø7 |
  | 9 | Augmented | {0,4,8} | augmented triad |
  | 10 | Augmented | {0,4,8,10} | aug7 (C7♯5) |
  | 11 | Suspended2 | {0,2,7} | sus2 |
  | 12 | Suspended4 | {0,5,7,10} | sus4(7) |
  | 13 | Suspended4 | {0,5,7,11} | sus4+maj7 |
  | 14 | Suspended4 | {0,5,8,10} | sus4♯5 |
  | 15 | Suspended4 | {0,6,7} | sus♯4 |
  | 16 | Power | {0,7} | open fifth |

- **`ChordQuality` enum** = Unknown, Major, Minor, Diminished, Augmented, HalfDiminished, Suspended2, Suspended4, Power
  ([`chordanalyzer.h:76-86`](src/composing/analysis/chord/chordanalyzer.h#L76-L86)).
- **Vocabulary vs spec §1 — coverage and two gaps** (full reconciliation in §8-contradiction-A):
  - **Triads (4):** maj/min/dim/aug — all present (#0,4,6,9). ✔
  - **Sevenths:** dom7(#2), maj7(#1), min7(#5), half-dim7(#8) present ✔; **diminished-seventh has NO template** — it is
    a `Diminished` triad (#6) + the `DiminishedSeventh` `Extension` flag
    ([`chordanalyzer.h:206`](src/composing/analysis/chord/chordanalyzer.h#L206)) selected by `dim7CharacteristicBonus`;
    **minor-major seventh (min-maj7, {0,3,7,11}) has NO template and NO quality output** — the bare `mMaj7` template was
    *tried and rejected* (B1, 2026-06-03; memory `backlog_b1_mmaj7_template.md`, deferred to "Phase E"). Spec §1
    *recognizes* min-maj7 → **gap to reconcile.**
  - **Sixths (maj6/min6):** no template; handled via the `AddedSixth` `Extension` flag
    ([`chordanalyzer.h:209`](src/composing/analysis/chord/chordanalyzer.h#L209)) + the `preferMinorOverMajorAdd6` pref
    ([`chordanalyzer.h:479`](src/composing/analysis/chord/chordanalyzer.h#L479)). Expressible, but on the extension axis.
  - **Extended/altered (9/11/13, alt-dom):** the full `Extension` bitmask
    ([`chordanalyzer.h:202-219`](src/composing/analysis/chord/chordanalyzer.h#L202-L219)) — again the extension axis,
    detected post-ranking, preset-gated by `extensionThreshold` ([`chordanalyzer.h:517`](src/composing/analysis/chord/chordanalyzer.h#L517)).

### §1.2 — `analyzeChord` scoring shape (how a pitch set scores against a template)
The per-cell vertical score = `(basisIndep + basisDep) × complexityFactor × augFactor + wCompleteBonus`
([`chordanalyzer.h:738-740`](src/composing/analysis/chord/chordanalyzer.h#L738-L740) for the formula;
[`chordanalyzer.cpp:1293-1330`](src/composing/analysis/chord/chordanalyzer.cpp#L1293-L1330) for the matrices), where
`basisIndep` (bass-independent, computed once per root×template,
[`chordanalyzer.cpp:1293-1299`](src/composing/analysis/chord/chordanalyzer.cpp#L1293-L1299)) sums:
- `scoreTemplateTones` — weighted presence of the template's tones (HarmAn "P")
  ([`chordanalyzer.cpp:353-366`](src/composing/analysis/chord/chordanalyzer.cpp#L353-L366));
- `scoreExtraNotes` — positive for extensions, **negative for contradictions and foreign notes** (HarmAn "−(N+M)")
  ([`chordanalyzer.cpp:376-447`](src/composing/analysis/chord/chordanalyzer.cpp#L376-L447));
- `dim7CharacteristicBonus` (key-driven rotation selector, §4) + `structuralPenalties` + `tpcConsistencyBonus` +
  `diatonicRootContribution` (the **key diatonic prior**) ([`chordanalyzer.cpp:1296-1299`](src/composing/analysis/chord/chordanalyzer.cpp#L1296-L1299)).

This is precisely the **partial-template-match `S = P − (N + M)`** the spec §14 names (Pardo & Birmingham HarmAn) — the
incomplete-chord tolerance is built in (absent tones contribute ~0; foreign tones penalise). **Reusable as-is** for the
spec's "score how well the pitches fit each candidate."

`bassNoteRootBonus` (0.70), `diatonicRootBonus` (0.30), `tpcConsistencyBonusPerTone` (0.20), and the inversion-context
bonuses are the tunables ([`chordanalyzer.h:348-439`](src/composing/analysis/chord/chordanalyzer.h#L348-L439)); the
**progression** signals (`rootContinuityBonus`, `resolutionBonus`, w_seq/w_dim/step) have **migrated to the competition
pipeline** (`fn::applyHarmonicFunction`) and are no longer in the oracle
([`chordanalyzer.h:380-385`](src/composing/analysis/chord/chordanalyzer.h#L380-L385);
[`chordanalyzer.cpp:1434-1471`](src/composing/analysis/chord/chordanalyzer.cpp#L1434-L1471)). **Note for L4 minimality
(spec §2/§14):** these progression signals are exactly the "chord-sequence / voice-leading proxies" the spec defers to
Layer 5 — the L4 build must decide which stay (they currently fire on the live per-region path).

### §1.3 — `ChordAnalysisResult` output fields
- `ChordAnalysisResult = { ChordIdentity identity; ChordFunction function; }`
  ([`chordanalyzer.h:296-299`](src/composing/analysis/chord/chordanalyzer.h#L296-L299)).
- `ChordIdentity` ([`chordanalyzer.h:249-271`](src/composing/analysis/chord/chordanalyzer.h#L249-L271)): `score`,
  `rootPc`, **`rootTpc`** (spelling), `bassPc`, **`bassTpc`**, `naturalFifthPresent`, `quality`, `tiePriority`
  (template index), `extensions` (bitmask), `isPedalPoint`, `pedalBassPc`. **So root, quality, bass/inversion, score,
  and the extension set are all present per result** — the bass/inversion distinction the home BIR metric scores is
  carried (`bassPc` vs `rootPc`).
- **Absent (spec §7 needs them, → new):** no `confidence`, no `uncertain` mark, no `chordTone`/`nonChordTone` sets. The
  `function` half (`ChordFunction` — [`chordanalyzer.h:276-290`](src/composing/analysis/chord/chordanalyzer.h#L276-L290))
  is the Roman-numeral/degree state that belongs to **Layer 5**, not L4 — its presence on the L4-era result is a
  pre-existing layering smudge to note (§7).

### §1.4 — Candidate-generation mechanism — **complete cube internally, top-3 externally**
- **The complete cube is generated:** the scoring loop fills `snapshot.cells` with **one `fn::ScoringCell` per
  `(bassCandidate, rootPc∈0..11, templateIdx∈0..16)`** —
  `reserve(bassCandidates.size() * 12 * templates.size())` and the triple loop
  ([`chordanalyzer.cpp:1390-1432`](src/composing/analysis/chord/chordanalyzer.cpp#L1390-L1432)). `ScoringCell` carries
  bass/root/template/quality + every score component ([`harmonicfunctionlayer.h:185`](src/composing/analysis/function/harmonicfunctionlayer.h#L185);
  fields populated at [`chordanalyzer.cpp:1406-1429`](src/composing/analysis/chord/chordanalyzer.cpp#L1406-L1429)).
- **It is surfaced byte-identically:** `if (snapshotOut) { *snapshotOut = std::move(snapshot); }`
  ([`chordanalyzer.cpp:1481-1483`](src/composing/analysis/chord/chordanalyzer.cpp#L1481-L1483)) — the
  L3-`dumpOut`-analogue (zero cost when null). `diagnoseChord` already consumes it to expose all cells
  ([`chordanalyzer.h:1036-1041`](src/composing/analysis/chord/chordanalyzer.h#L1036-L1041)).
- **The public path returns only top-3:** `fn::applyHarmonicFunction` clears `results`, ranks, and stops at 3
  (`if (results.size() >= 3) break;` → push — [`harmonicfunctionlayer.cpp:355,509-515`](src/composing/analysis/function/harmonicfunctionlayer.cpp#L355-L515)),
  plus a single diff-root append ([`harmonicfunctionlayer.cpp:519-533`](src/composing/analysis/function/harmonicfunctionlayer.cpp#L519-L533)).
  The interface contract says so: "Returns up to 3 candidates"
  ([`chordanalyzer.h:813-815`](src/composing/analysis/chord/chordanalyzer.h#L813-L815)).
- **Consequence for the spec lever (§4 "generation is the lever, not re-ranking"):** the lever is *available without a
  new scorer* — surface the snapshot cube, rank-and-prune K (the L3 pattern), keep the spec's ranked alternatives.
  **The one caveat is §0.2:** the cube spans the 17 quality shells, **not** the extended/6th set (those are the
  post-ranking `detectExtensions` axis); "complete generation over every tertian chord" must reconcile the
  template×extension factoring (§8-A).

---

## §2 — Sparse / incomplete + bass / post-pass logic (reuse, to be integrated)

### §2.1 — Sparse-chord key-prior passes (`sparsechordrefinement.{h,cpp}`)
Namespace `mu::composing::analysis::region`; declared in
[`sparsechordrefinement.h:38-75`](src/composing/analysis/region/sparsechordrefinement.h#L38-L75):
- `refineSparseChordQualityFromKeyContext(result, tones, keyFifths, keyMode)` — upgrades a sparse `Unknown` result to
  the diatonic triad quality implied by the resolved key when the sounding tones are compatible (it already **defers**
  the too-ambiguous case rather than hardening it) ([`sparsechordrefinement.h:44-50`](src/composing/analysis/region/sparsechordrefinement.h#L44-L50)).
- `applyTonicPriorToSparseChord(...)` — Iter 75/76 diatonic-quality prior for ≤2-distinct-PC thin regions
  ([`sparsechordrefinement.h:52-64`](src/composing/analysis/region/sparsechordrefinement.h#L52-L64)).
- `forceChordTrackQualityFromKeyContext(result, keyMode)` — force-assigns the diatonic triad quality for chord-track
  regions still `Unknown` (no Aeolian lone-tonic exclusion) ([`sparsechordrefinement.h:71-73`](src/composing/analysis/region/sparsechordrefinement.h#L71-L73)).
- `diatonicDegreeForRootPc(rootPc, keyFifths, keyMode)` — the shared degree helper
  ([`sparsechordrefinement.h:42`](src/composing/analysis/region/sparsechordrefinement.h#L42)).
- **As-is they run as a POST-PASS** over the committed `chosenResult`, *after* `analyzeChord` + gates, at the seam:
  [`regionanalyzer.cpp:779-782`](src/composing/analysis/region/regionanalyzer.cpp#L779-L782). This is the
  key-diatonic-prior-for-sparse logic the spec §5 reuses — **to be *integrated into generation/scoring*** (spec
  "incomplete chords" path: partial template matching → key prior → prevailing chord → bass), **not** left a bolt-on.

### §2.2 — Bass-anchoring / pedal logic (`chordpostpasses.cpp`)
- `cptIsBassChordTone(bassPc, rootPc, quality, extensions)` — classifies the **bass note** as a chord tone of the
  winning chord (triad intervals per quality + explicitly-detected 7th/9th/11th/13th extensions), used to decide
  slash-chord vs structural **pedal point** ([`chordpostpasses.cpp:43-107`](src/composing/analysis/chord/chordpostpasses.cpp#L43-L107)).
  This is the **only per-note membership predicate in the module** (§3) and the bass→root / slash-vs-pedal logic the
  spec's bass-anchoring reuses.
- The Iter-86 (bass-♭7 promotion) / Iter-91 (bass-as-root promotion) / two-pass pedal detection run as
  `applyIter8691Pedal()` ([`chordanalyzer.h:989-993`](src/composing/analysis/chord/chordanalyzer.h#L989-L993)), invoked
  at the seam between `analyzeChord` and the gates ([`regionanalyzer.cpp:775`](src/composing/analysis/region/regionanalyzer.cpp#L775)).
- `pedalConfidenceThreshold` (0.65) gates pedal confirmation ([`chordanalyzer.h:557`](src/composing/analysis/chord/chordanalyzer.h#L557));
  `bassPassingToneMinWeightFraction` (0.05) filters passing-tone basses
  ([`chordanalyzer.h:503`](src/composing/analysis/chord/chordanalyzer.h#L503)).
- **As-is these are post-passes / external gates** (`applyPostScoringGates`, gates A-L —
  [`chordanalyzer.h:976-980`](src/composing/analysis/chord/chordanalyzer.h#L976-L980)), run after `analyzeChord` at the
  seam ([`regionanalyzer.cpp:775-776`](src/composing/analysis/region/regionanalyzer.cpp#L775-L776)). The spec folds the
  bass-anchoring into generation; the gates' fate at L4 is a build decision (many are Baroque-tuned identity gates, not
  bass-anchoring — keep out of L4's minimal core unless they encode bass-anchoring).

---

## §3 — NCT / membership (the largely-NEW part — the gap, pinned)

- **No per-note chord-tone-vs-NCT classifier exists in `src/composing`.** Exhaustive read-only search (keywords:
  nonChordTone / non-chord / NCT / passingTone / neighbour-tone / suspension / anticipation / chordTone / membership /
  embellish / ornament) found **none** [agent-sourced, corroborated by the main session's read of the chord path]. The
  **only** per-note membership decision is `cptIsBassChordTone` (bass-vs-pedal, §2.2) — not an NCT classifier.
- **The current path analyses a flattened aggregate, not per-note membership.** `analyzeChord` sums every tone into a
  12-bin `pcWeight` histogram ([`chordanalyzer.cpp:974-986`](src/composing/analysis/chord/chordanalyzer.cpp#L974-L986));
  `distinctPcs` is the count of bins > 0.05 ([`chordanalyzer.cpp:1146-1151`](src/composing/analysis/chord/chordanalyzer.cpp#L1146-L1151)).
  The tone collector likewise aggregates **per pitch class**, not per note: `weightedPcView` reduces overlapping notes
  to a `ChordAnalysisTone` per pc with `durationInRegion` / `distinctMetricPositions` / `simultaneousVoiceCount` /
  `onsetAtRegionStart` accumulated across notes ([`chordanalyzer.h:94-116`](src/composing/analysis/chord/chordanalyzer.h#L94-L116);
  builder [`regiontonecollector.cpp:184,217`](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L184-L217)
  [agent-sourced for the PcAccum reduction body]). **Per-note identity is aggregated away before scoring** — exactly the
  lossy "union recompute" the spec replaces (spec §13 "anchor over-reading").
- **Per-note inputs that a future NCT decision can use are present in Layer 1's `NoteEvent`** (main-session-verified):
  `pitch`, `tpc`, `staff`, `voice`, **`onset`**, **`release`**, **`duration`**, `isGrace`, `plays`, `visible`,
  `staffEligible` ([`note_model.h:80-92`](src/composing/analysis/notemodel/note_model.h#L80-L92)). The note's **metric
  position** is derivable from `onset` (via the score's measure/beat lookup); its **stepwise relation** is derivable
  from `pitch`/`tpc` of neighbouring slices. **But there is NO per-note `beatWeight`/`metricWeight` field** — the beat
  weight is computed *during* tone collection and folded into the pc aggregate (a `beatWeight()` lambda multiplied into
  the per-pc `totalWeight` — [agent-sourced, `regiontonecollector.cpp` ~168-175]); it is **not** retained per note. So
  the spec's per-note membership cue (metric weight + stepwise treatment) requires reading the metric position **per
  note** from the Layer-1 `NoteEvent` stream (which `NoteModel::overlapping` supplies losslessly), **not** from the
  aggregated tone view. **This is the largely-new build surface — confirmed, and the inputs exist to build it.**

---

## §4 — tpc / spelling (maximal-information)

- **The note model carries tpc** (`NoteEvent::tpc`, 0-34 circle-of-fifths spelling, -1 = absent —
  [`note_model.h:82`](src/composing/analysis/notemodel/note_model.h#L82)) and it is threaded into the chord scorer:
  `ChordAnalysisTone::tpc` ([`chordanalyzer.h:90`](src/composing/analysis/chord/chordanalyzer.h#L90)) → `tpcForPc[12]`
  lookup ([`chordanalyzer.cpp:1131-1140`](src/composing/analysis/chord/chordanalyzer.cpp#L1131-L1140)) → consumed by:
  - `scoreExtraNotes` (sus4-vs-minor ♯9/♭3 disambiguation by E♭ vs D♯ spelling —
    [`chordanalyzer.cpp:424-437`](src/composing/analysis/chord/chordanalyzer.cpp#L424-L437));
  - `tpcConsistencyBonus` / `countTpcMatches` (per-tone spelling-match bonus, `tpcConsistencyBonusPerTone` 0.20 —
    [`chordanalyzer.cpp:487-531,648`](src/composing/analysis/chord/chordanalyzer.cpp#L487-L531));
  - `nonBassAdjustment` (tpc-based; [`chordanalyzer.cpp:240,276`](src/composing/analysis/chord/chordanalyzer.cpp#L240-L276));
  - **root naming:** `rootTpc = ctx.tpcForPc[rootPc]` ([`chordanalyzer.cpp:870`](src/composing/analysis/chord/chordanalyzer.cpp#L870)),
    stamped to `r.identity.rootTpc` ([`chordanalyzer.cpp:928`](src/composing/analysis/chord/chordanalyzer.cpp#L928)).
  **So the chord path is NOT pitch-class-only — it reads spelling.** ✔ (Cell `bassTpc` is also carried through the cube,
  [`chordanalyzer.cpp:1408`](src/composing/analysis/chord/chordanalyzer.cpp#L1408).)
- **The gap the spec names is the SYMMETRIC root selector, not the absence of tpc.** For a symmetric **dim7**, the root
  *pc* is chosen by `dim7CharacteristicBonus`, which rewards the rotation whose ♭♭7 (root+9) is **non-diatonic in the
  current key** ([`chordanalyzer.cpp:452-485`](src/composing/analysis/chord/chordanalyzer.cpp#L452-L485)) — a
  **key-dependent** selector that *moves with the key* (the rotation churn CLAUDE.md class-(a) tracks), and the comment
  itself calls it a "ROTATION-SELECTION MECHANISM" tied to key non-diatonicity
  ([`chordanalyzer.cpp:1283-1292`](src/composing/analysis/chord/chordanalyzer.cpp#L1283-L1292)). For a symmetric
  **augmented**, root selection falls back to the **bass** when tpc is absent
  ([`chordanalyzer.cpp:846-867`](src/composing/analysis/chord/chordanalyzer.cpp#L846-L867)). `tpcConsistencyBonus`
  provides *partial* spelling pressure on rotation, but **there is no deterministic, key-independent "pin the dim7/aug
  root from the notated spelling" selector** — which is precisely what the spec §5/§9 mandates ("spelling does not move
  with the key, so no rotation churn arises"). **This spelling-aware symmetric-root logic is the largely-new part of §4
  — aligned with the spec, and it is the source of the tracked class-(a) churn** (so building it *dissolves* that churn
  at L4, per spec §11). Detailed reconciliation in §8-contradiction-B.

---

## §5 — The seam, the window, the index

### §5.1 — Seam (the per-region chord call site, re-confirmed at HEAD)
The live chord call in `analyzeRegions`' Pass-1 lambda:
- `analysis::PostScoringGateContext gateCtx; auto results = chordAnalyzer->analyzeChord(tones, localKeyFifths,
  localKeyMode, &temporalCtx, attemptPrefs, &gateCtx);`
  ([`regionanalyzer.cpp:762-764`](src/composing/analysis/region/regionanalyzer.cpp#L762-L764)) — **the seam the L4 build
  re-points per-slice. (~:763, NOT the instruction's ~:668 — that predates the L3 wiring `a6b08af3fe`; re-confirmed at
  HEAD this session.)**
- `localKey` (the key fed to the chord scorer) is now the **L3 decoder's** duration-majority key over the region's slice
  run: `const KeyModeAnalysisResult localKey = localKeyForRegion(regionStart.ticks(), regionEnd.ticks());`
  ([`regionanalyzer.cpp:730-733`](src/composing/analysis/region/regionanalyzer.cpp#L730-L733)) — so the **key→chord
  feed-forward order the spec mandates already holds at the seam.**
- Downstream consumers of the chord result at the seam (all per-region, all to become per-slice):
  - `applyIter8691Pedal` + `applyPostScoringGates` ([`regionanalyzer.cpp:775-776`](src/composing/analysis/region/regionanalyzer.cpp#L775-L776));
  - `refineSparseChordQualityFromKeyContext` + `applyTonicPriorToSparseChord`
    ([`regionanalyzer.cpp:779-782`](src/composing/analysis/region/regionanalyzer.cpp#L779-L782));
  - `inferNextRootPc(...)` (next-region root for joint scoring —
    [`regionanalyzer.cpp:748-749`](src/composing/analysis/region/regionanalyzer.cpp#L748-L749));
  - `region.alternatives` (≤2 carried) + `region.chordResult` + `region.keyModeResult = localKey`
    ([`regionanalyzer.cpp:785-836`](src/composing/analysis/region/regionanalyzer.cpp#L785-L836)).
- The path state is owned by the **`decode::ChordPathDecoder`** (Stage 3.1, beam-1, byte-identical greedy commit;
  `decoder.commit(chosenResult.identity, gateCtx)` — [`regionanalyzer.cpp:695-698,790`](src/composing/analysis/region/regionanalyzer.cpp#L695-L790)).
  **Note:** this is the *chord-path* decoder (`ChordTemporalContext`), distinct from the L3 key decoder; the L4 build
  re-expresses the per-slice orchestration here, and the existing beam-1 decoder is the scaffold (design `docs/decoder_design.md`).

### §5.2 — Window / context primitives (available for the spec's adaptive lazy-extend window)
- **`weightedPcView(noteModel, startTick, endTick, excludeStaves, parentStartTick, excludeLookAheadOnDenseStart, prefs)`**
  → `vector<ChordAnalysisTone>` — the chord tone collector, over a half-open span, **already on the index**:
  `noteModel.overlapping(startTickInt, endTickInt)` ([`regiontonecollector.cpp:217`](src/composing/analysis/engravingbridge/regiontonecollector.cpp#L217),
  main-session-verified; signature [agent-sourced `regiontonecollector.h:160-167`]). Called at the seam
  ([`regionanalyzer.cpp:645,712-714`](src/composing/analysis/region/regionanalyzer.cpp#L712-L714)). **This is the
  reusable per-slice tone window** — narrow the `[start,end)` to the slice ± neighbours and it composes the spec's
  lazy-extend window.
- **`pitchContextOverSpan(model, windowStart, windowEnd, anchorStart, anchorEnd, excludeStaves, beatPrefs, weights, out)`**
  — the indexed, span-anchored key-context builder, distance-weighted from an anchor, on the index
  (`model.overlapping(windowStart, windowEnd)` — [`regiontoneprimitives.cpp:242`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp#L242),
  main-session-verified). Its un-indexed point-anchored predecessor `collectPitchContext` (DOM segment walk,
  `regiontoneprimitives.cpp:123-200` [agent-sourced]) is **legacy** — the spec's window must reuse the indexed
  `pitchContextOverSpan`, not the DOM walk (the same R1/perf lesson the L3 build applied).
- `ChordTemporalContext` ([`chordanalyzer.h:639-706`](src/composing/analysis/chord/chordanalyzer.h#L639-L706)) is the
  existing neighbour/prevailing-chord carrier (previousRootPc/Quality/BassPc, nextRootPc/BassPc, recentRootPcs[3],
  regionMetricWeight, predecessor-confidence channel) — the spec's prevailing/neighbour context.

### §5.3 — Index (the perf floor)
- `NoteModel::overlapping(t0, t1)` = all notes with `onset < t1 && release > t0`, **O(log N + result)** via the
  max-release segment tree `NoteQueryIndex` ([`note_model.h:155-158`](src/composing/analysis/notemodel/note_model.h#L155-L158);
  complexity [`note_model.h:94-107`](src/composing/analysis/notemodel/note_model.h#L94-L107); `onsetIn` O(log N) at
  [`note_model.h:160-162`](src/composing/analysis/notemodel/note_model.h#L160-L162)). `NoteModel::build(score)` reads the
  **whole score** once ([`note_model.h:147-150`](src/composing/analysis/notemodel/note_model.h#L147-L150)).
- **The L2 slice grid:** `struct Slice { int start; int end; }` + `changePointSlices(const NoteModel&)`
  ([`slicer.h:77-80,91`](src/composing/analysis/slicing/slicer.h#L77-L91) [agent-sourced, matches [L3-audit §2.1]
  verbatim]) is the per-slice observation unit the L4 build re-points the seam onto.
- **Verdict:** because `weightedPcView`/`pitchContextOverSpan` already query `overlapping`, the per-slice chord window is
  **O(N log N) by construction** if the build reuses them. **The L3 O(N²) risk does NOT recur on the chord path** — the
  chord tone collector was already indexed (a strictly better starting position than the L3 key window).

---

## §6 — Metrics & fixtures

### §6.1 — Chord-root (BIR) + quality metric tooling (the home metric)
[agent-sourced; corroborated by CLAUDE.md + BUILD_AND_TEST.md]:
- **`tools/characterise_bir_false.py`** — the BIR=false gate: a case is BIR=false iff our region is `chord_disagree`
  vs music21, our winner has `bassIsRoot == False`, and music21 ∧ DCML agree. Reads `.ours.json` + `.music21.json` from
  the validated per-preset dir. The **57/23/57** identity sets (Baroque/Jazz/Default, stem@tick) are in CLAUDE.md.
- **`tools/oracle_root_metric.py`** — the standing per-event tiered chord-root metric (root pc only, bass-decoupled);
  KEY band split KEY-HARD vs KEY-TONICIZATION; the dual-preset hard-stop the L3 build graded against.
- **`tools/analyze_inversion_errors.py`** — the BIR=true (inversion) secondary metric (`bassIsRoot`=true; margin /
  quality / noteCount distributions); `--corpus-dir` validated.
- **`tools/compare_rn.py`** — Roman-numeral compare; **quality is scored distinctly from root** here
  (`quality_disagree` bucket via `_same_quality` / `extract_quality`).
- **`tools/compare_analyses.py`** — `three_way_classify(our_pc, m21_pc, dcml_pc)` (the shared root-agreement predicate).
- **The "two-tier" symmetric/decidable split is doc-only** (CLAUDE.md class-(a)/(b) prose) — **not** encoded in
  `characterise_bir_false.py` (no code branch separates dim7/aug from decidable roots). The spec's two-tier gate (§10)
  is therefore a **build deliverable**, consistent with [L3-audit §3] / CLAUDE.md "Stage 5/6 spelling-aware gate."

### §6.2 — The missing membership metric (spec §10 build deliverable)
- **No per-note chord-tone-vs-NCT precision/recall metric exists** in `tools/` or `src/composing/tests/` [agent-sourced
  absence; searched membership/non-chord/NCT/passing/chordTone/precision/recall]. The chord-root (BIR) metric does
  **not** measure membership. **The spec §10's NCT-membership precision/recall against the human-analysis chord tones is
  a NEW build deliverable** — confirmed absent.

### §6.3 — Chord test fixtures (the behaviour-test base the build extends)
[agent-sourced]:
- `src/composing/tests/chordanalyzer_tests.cpp` (~197 `TEST(`s) — direct `analyzeChord` unit tests (qualities, bass-root
  tiers, weight-threshold passing-tone *filtering* — not membership scoring, tonicization labels).
- `src/composing/tests/chordanalyzer_musicxml_tests.cpp` (~7 catalog tests) over
  `src/composing/tests/data/chordanalyzer_catalog_standard.musicxml` + `chordanalyzer_catalog_jazz.musicxml` +
  `chordanalyzer_context.musicxml` (the do-not-touch ground-truth catalog — gate-approval per CLAUDE.md).
- **`nm_*` `.mscx`/`.musicxml` fixtures** (e.g. `nm_slice_passing`, `nm_slice_held_melody`, `nm_slice_release`,
  `nm_tie_chain`, `nm_unison`) — the **slice-level** note-model fixtures most relevant to L4's per-slice behaviour
  tests; the spec §10 behaviour fixtures (clean triad / passing-tone / suspension / symmetric-dim7 "uncertain")
  extend this set. (Memory's `s1c_*` key fixtures were **not** found by the agent — they are key-layer, not chord;
  noted as a minor [L3-audit] discrepancy, immaterial to L4.)
- Pinned snapshot surface: `pipeline_snapshot_tests` (11 goldens at
  `src/notation/tests/pipeline_snapshot_tests/snapshots/`) — moves when L4 changes chord output; refresh only after
  verified correct (CLAUDE.md / [L3-audit §4]).

---

## §7 — Unification preview (so the build starts clean)

**Reuses (from source):**
- the **17-template scorer** + the `(basisIndep+basisDep)×cf×af+wComplete` HarmAn-style partial match
  (`scoreTemplateTones`/`scoreExtraNotes`) — §1.2;
- the **complete candidate cube** `fn::ScoringSnapshot.cells` surfaced via `snapshotOut` — §1.4 (the generation lever);
- the **sparse key-prior** passes (`refineSparseChordQualityFromKeyContext`, `applyTonicPriorToSparseChord`,
  `forceChordTrackQualityFromKeyContext`) and the **bass-anchoring / pedal** logic (`cptIsBassChordTone`,
  `applyIter8691Pedal`) — §2 (to be *integrated into generation*, not bolt-ons);
- the **tpc threading** (`tpcForPc`, `tpcConsistencyBonus`, `rootTpc`) — §4;
- the **indexed windows** `weightedPcView` / `pitchContextOverSpan` over `NoteModel::overlapping`, the L2 `Slice` grid,
  and the `ChordTemporalContext` neighbour carrier — §5;
- the `keyModeResult` carrier on the region/slice (the L3 key feed-forward) — §5.1.

**Newly written:**
- **per-slice orchestration** (re-point the @763 seam onto the `changePointSlices` grid, two-pass);
- the **per-note, neighbour-aware, binary chord-tone-vs-NCT membership decision** (metric weight from `NoteEvent.onset`
  + stepwise relation across neighbour slices) — §3 (the real lever, spec §11);
- the **adaptive lazy-extend window** (narrow slice±neighbours, bounded to one harmony) — §5.2;
- the **deterministic spelling-aware symmetric (dim7/aug) root pin** (key-independent) that *replaces* the key-driven
  `dim7CharacteristicBonus` rotation selector — §4 (dissolves class-(a) churn);
- the **result-carrier additions** (`confidence`, `uncertain`, chord-tone set, NCT set; promote ranked alternatives onto
  the per-slice result) — §1.3;
- the **NCT-membership precision/recall metric** and the **two-tier (decidable/deferred) BIR gate** in code — §6.2/§6.1.

**Retires at the eventual wiring:**
- the **per-region** chord path (one coarse `analyzeChord` per region) → per-slice;
- the **sparse / bass post-passes as bolt-ons** (`refineSparse…`/`applyTonicPrior…`/`applyIter8691Pedal` run *after* a
  committed winner) → folded into generation/scoring;
- the **region-level flattened `pcWeight` aggregate** as the membership input → the lossless per-note `NoteEvent` stream;
- the **key-driven dim7 rotation selector** (`dim7CharacteristicBonus` as a root *chooser*) → spelling-pin (its
  *diatonic-evidence* role may survive as a prior, but not as the rotation arbiter).

**Pre-existing duplication / layering smudges to surface (so the build does not entrench them):**
1. **Two tone-window families** (`regiontonecollector.{h,cpp}` chord-side vs `regiontoneprimitives.cpp` key-side) and a
   **legacy DOM-walk `collectPitchContext`** alongside the indexed `pitchContextOverSpan` — the L4 window should
   consolidate on the indexed builders, not add a third.
2. **The extension axis is detached from the candidate cube** — `detectExtensions` runs in `buildChordResult` on the
   winner only ([`chordanalyzer.cpp:870-892`](src/composing/analysis/chord/chordanalyzer.cpp#L870-L892)); "complete
   generation" must decide whether to fold extensions into the enumerated candidates (§8-A).
3. **`ChordFunction` rides on the L4-era `ChordAnalysisResult`** ([`chordanalyzer.h:296-299,276-290`](src/composing/analysis/chord/chordanalyzer.h#L276-L299))
   — Roman-numeral/degree state is Layer 5; carrying it on the chord result blurs the L4/L5 boundary.
4. **Progression signals fire on the live chord path** (`rootContinuityBonus`/`resolutionBonus`/w_seq/w_dim/step in
   `fn::applyHarmonicFunction`) — by spec minimality these are Layer-5 (chord-sequence/voice-leading proxies); the build
   must decide which leave L4.

**End-state:** one per-slice chord-and-membership path; generation = the surfaced cube + integrated sparse/bass + the
new spelling pin; membership = the new per-note decision; output = symbol + chord-tone/NCT sets + ranked alternatives +
confidence + uncertain.

---

## §8 — Deliverables, `[unverified]` items, spec-vs-source contradictions, stop conditions

**Delivered:** this dossier (`cc_layer4_audit_dossier.md`, held / gitignored). **No production code; no behaviour
change; no corpus regen; no commit; no snapshot refresh; `upstream` untouched.** Read-only inspection only (Read / Grep
/ Glob + read-only sub-agents).

### Spec-vs-source contradictions / reconciliations to settle BEFORE building
- **A — "Complete candidate generation" vs the template×extension factoring (the main one).** Spec §4/§9/§11: generate
  the *complete* set of *every tertian chord* the pitches could spell, then select. Source: the cube is complete over
  the **17 quality shells** ([`chordanalyzer.cpp:1390-1432`](src/composing/analysis/chord/chordanalyzer.cpp#L1390-L1432)),
  but **6ths, dim7, and 9/11/13 are an `Extension` bitmask detected post-ranking on the winner**
  ([`chordanalyzer.cpp:870-892`](src/composing/analysis/chord/chordanalyzer.cpp#L870-L892)), and **min-maj7 has no
  template at all** (B1 rejected; `backlog_b1_mmaj7_template.md`). So the as-is "complete generation" is *not* complete
  over the extended vocabulary the spec §1 names. **Reconcile:** does L4 enumerate the extended set into the candidate
  list, or keep template-cube + post-hoc extension detection and treat extensions as a within-candidate refinement? Not
  a blocker (the templates *can* express the core triad/seventh vocabulary), but the lever's exact shape depends on this.
- **B — Symmetric-root: key-driven rotation vs deterministic spelling-pin.** Spec §5/§9: pin the dim7/aug root from the
  **notated spelling** (deterministic, "does not move with the key, so no rotation churn"). Source: the dim7 rotation is
  selected by **key non-diatonicity** (`dim7CharacteristicBonus`, [`chordanalyzer.cpp:452-485`](src/composing/analysis/chord/chordanalyzer.cpp#L452-L485)) —
  key-dependent, the documented source of the class-(a) churn — and aug falls back to **bass**
  ([`chordanalyzer.cpp:846-867`](src/composing/analysis/chord/chordanalyzer.cpp#L846-L867)). These **conflict in
  mechanism** (the spec's selector is spelling, the as-is selector is key). **This is expected** (the spec calls the
  spelling pin "largely new") — flagged so the build *replaces*, not augments, the key-driven selector for the rotation
  decision (the diatonic evidence may stay a prior). Not a STOP — the templates/tpc *can* express it; building it
  dissolves the tracked churn (spec §11), consistent with CLAUDE.md's "retires when Layer 4 pins the rotation."
- **C — Result carrier missing certainty/membership fields** (§1.3) — additive, not a conflict; the spec's §7 fields are
  new struct members, and the per-region `alternatives` (≤2) promote onto the per-slice result. No contradiction.
- **D — The `minDistinctPcsForCandidate = 3` gate** ([`chordanalyzer.cpp:1152-1154`](src/composing/analysis/chord/chordanalyzer.cpp#L1152-L1154))
  returns `{}` for <3 distinct PCs; many per-slice sonorities (dyads, single arpeggio notes) are sparser. The
  greedy-expand path already relaxes it to 1 ([`chordanalyzer.h:519-526`](src/composing/analysis/chord/chordanalyzer.h#L519-L526));
  the per-slice build needs the relaxed gate + the sparse refinement *in generation* (spec §5 incomplete-chord/arpeggio
  path). Additive, flagged.

**None of A-D requires building the gated joint key-and-chord step or any production change now** — they are
reconciliation notes for the build's first increment.

### `[unverified]` (not main-session-confirmed at source this session — listed, not guessed)
1. The **PcAccum reduction body** of `weightedPcView` (the per-note→per-pc aggregation, beat-weight lambda ~`regiontonecollector.cpp:168-237`)
   and the **DOM-walk body** of the legacy `collectPitchContext` (`regiontoneprimitives.cpp:123-200`) — [agent-sourced];
   the main session verified only the `overlapping(...)` call sites (`regiontonecollector.cpp:217`,
   `regiontoneprimitives.cpp:242`) and the `NoteEvent`/`overlapping` API. The aggregation *being* per-pc (not per-note)
   is corroborated by the main session's read of `ChordAnalysisTone` (per-pc accumulation fields,
   [`chordanalyzer.h:94-116`](src/composing/analysis/chord/chordanalyzer.h#L94-L116)).
2. The **window-builder signatures** in `regiontonecollector.h` (`weightedPcView` ~:160, `collectRegionTones` ~:172,
   `pitchContextOverSpan` ~:267, `collectPitchContext` ~:234) — [agent-sourced]; the `.cpp` call sites and index usage
   are main-session-verified.
3. The **metric-tooling internals** (`characterise_bir_false.py` line numbers, `oracle_root_metric.py` tiers,
   `compare_rn.py` quality buckets) and the **fixture inventory** (test counts, catalog sizes, `nm_*`/`s1c_*` lists) —
   [agent-sourced]; corroborated by CLAUDE.md + BUILD_AND_TEST.md, not re-read line-by-line by the main session.
4. The **`slicer.h` Slice/`changePointSlices` line numbers** (:77-80, :91) — [agent-sourced], identical to the
   main-session-read [L3-audit §2.1].
5. The exact line range of the legacy `collectPitchContext` DOM walk and the `beatWeightAtOnset` lambda — [agent-sourced].

### Stop conditions (instruction §9) — status: none breached
- No production / behaviour / scoring change; no probe altered analysis output (read-only).
- Every as-is item is main-session-confirmed at source or tagged `[agent-sourced]`/`[unverified]` above.
- The findings do **not** require building the gated joint key-and-chord step (the symmetric-root spelling pin is an L4
  job per spec §5; the *re-spelling* of unspelled/contradicted symmetric chords stays deferred to the later step).
- The two spec-vs-source mechanism conflicts (A, B) are **flagged for reconciliation, not designed around silently** —
  per instruction §9 they are recorded here for Cowork/user before the build, and neither blocks (the templates+tpc can
  express the spec's vocabulary; the complete candidate list exists internally; tpc is genuinely present). **No
  instruction-§9 hard STOP is triggered.**

**Next (after Cowork citation-verification + user ratification):** the Layer-4 build — re-point the @763 seam per-slice
over `changePointSlices`, surface the candidate cube as the generation lever, integrate the sparse/bass logic into
generation, add the per-note neighbour-aware membership decision + the deterministic spelling-pin, extend the result
carrier (confidence/uncertain/membership sets), and add the NCT-membership metric + two-tier gate — graded by the
dual-preset BIR gate (no new class-(b)), the new membership metric, and the 11 pipeline snapshots (refreshed only after
verified correct).
