# CC report — L3→region key-alternatives forward-carry (byte-identical)

**Instruction:** close the override-readiness gap on the key layer (L3) — carry the
already-computed ranked alternative keys + sequence-margin confidence forward to the
region level so the Layer-5 confidence-weighted forward override can SELECT among the
keys the key layer carried (never re-derive). Byte-identical; add two lock-in tests.

**HEAD at start:** working tree on `master`; §0 docs committed at `08d1b541c1`.
**Code commit (this work):** `001199ac33` (local, unpushed).

---

## §0 — Preamble sweep

Committed the unstaged Cowork docs **locally** (`08d1b541c1ddc5e1c61b5890fea03c92f749e02f`):
`docs(cowork): L5 spec + confidence-weighted-override + override-readiness assessment`.
Files: `cowork_layer5_function_design.md` (new), `cowork_layer5_function_methods.md` (new),
`cowork_l1l4_completion_ledger.md`, `cowork_layer3_keymode_design.md`,
`cowork_layer4_chordsymbol_design.md`, `cowork_target_architecture.md` (modified).
`scratch_artifacts/` deliberately left untracked (not a Cowork doc).

---

## §1 — Investigate-confirm (VERIFIED at source)

### 1. The gap is real (L3), and L4/L2 are not impacted

- **L3 (the gap).** The slice→region key reduction `localKeyForRegion`
  (`regionanalyzer.cpp`, the lambda at ~684) consumed **only** `SliceKeyMode.chosen`
  (`return sliceKeys[best->repSlice].chosen;`). `HarmonicRegion` (`harmonicrhythm.h`)
  carried only the single chosen key (`keyModeResult`) + scalar confidence; its
  `alternatives` field is `ChordAnalysisResult` **chord** candidates, **not** keys —
  so L5 had no carried key menu at the region level. CONFIRMED.
- **The producer DOES carry the material on every slice.** `KeyModeSequenceDecoder::decodeLattice`
  (`keymodesequence.cpp` 351–397) populates `chosen`, `confidence` (sequence margin),
  `alternatives` (ranked, capped at `maxAlternatives=4`) and `uncertain` for **every**
  slice `t` in `for (t=0..T)`, not only at seams. The `alternatives` list is non-empty
  whenever ≥2 lattice states survive (the norm for a real multi-slice decode). The live
  `analyzeRegions` path runs the decode unconditionally (`regionanalyzer.cpp` 580–583);
  reach-back is default-off. CONFIRMED.
- **L4 already satisfies override-readiness.** `chordslicedecoder` fills `alternatives`
  (decideSlice) and `confidenceModel` (applyCommitDecision via `populateForwardContract`,
  called on **every** branch — Commit/Inherit/Abstain) and the commit/inherit/abstain
  split never prunes them (the inherit branch 991–997 does not touch `sc.alternatives`).
  No change needed; locked by a test (§3). CONFIRMED.
- **L2 not impacted** (deterministic fact-grid, no key alternatives). No change.

### 2. ★ The byte-identity gate — serializer check (the load-bearing check)

The new field is added to `HarmonicRegion`. Every production serializer that touches a
region reads **named sub-fields** and none reflects over the whole struct, so a new
sibling field is invisible to all of them:

| Serializer | Production output | How it reads the region | New field reaches it? |
|---|---|---|---|
| `tools/batch_analyze.cpp` | `.ours.json` (BIR corpus) | copies named fields (`hr.keyModeResult`, `hr.tones`, `hr.chordResult`, `hr.alternatives`) into an emitter-local `AnalyzedRegion`, then serializes **that** | **No** — not copied into `ar` |
| `notationimplodebridge.cpp` | implode chord track + key annotations | `region.keyModeResult.{keySignatureFifths,mode,normalizedConfidence}`, `region.tones`; region-equality is a **named-field** `&&` chain (305–308) | **No** |
| `notationcomposingbridge.cpp` | annotation / tick-regional context | named sub-fields (`it->keyModeResult.*`, `temporalExtensions`) | **No** |
| `notationtuningbridge.cpp` | tuning offsets | `region.keyModeResult` sub-fields | **No** |
| `pipeline_snapshot_tests.cpp` | P1–P4 snapshot goldens | `r.keyModeResult.{keySignatureFifths,mode}`, `temporalExtensions` | **No** |

`HarmonicRegion` is a plain aggregate (no defaulted `operator==`/spaceship, not hashed,
no `memcmp`), so nothing compares it wholesale. → adding the field is **byte-identical**.
The chosen key (`keyModeResult`) and every consumed value are unchanged: the reduction's
`chosen` is computed by the identical vote/`repSlice` logic (`rep.chosen` == the old
return). The Pass-3 merges (`coalesceShortSameRootRuns` `std::move(regions[longestIdx])`,
`absorbShortRegions`/`tryCollapseSameChordRegion` extend-in-place) move/preserve whole
region structs, so the new field travels **with** `keyModeResult` automatically.

### 3. The reduction (v1)

Default v1: carry the **representative slice's** `alternatives` (the `repSlice` that
already determines the region's chosen key) + that slice's **sequence-margin
`confidence`** (`SliceKeyMode.confidence` — the value otherwise dropped at the region
level; distinct from `keyModeResult.normalizedConfidence`, which the chosen key already
carries). Kept in **one** clearly-named reduction (`localKeyForRegion` → `RegionKeyReduction`)
so the later precise pin (the first L5-modulation task, §15-3) is a single-site change.
Sub-regions inherit the parent's carry via one helper `inheritRegionKeyContext` (the
parent's reduction is what determined a sub-region's inherited chosen key — the faithful
choice).

### 4. No stop condition

The field is added cleanly without entering any production serializer; the reduction has
a stable `repSlice` by construction. No design question for Cowork.

**Known v1 limitation (flagged, not a blocker):** the gated-OFF J-key-iii path
(`applyJointKeyWiring`, default `jointKeyWiringEnabled()==false`) overrides
`region.keyModeResult` without re-deriving the new fields. Since it is off in the
byte-identical baseline and the field has **no consumer**, the carry retains the
Pass-1/2/2b reduction values there — acceptable for v1, to be pinned when L5 consumes it.

---

## §2 — The byte-identical forward-carry (key layer)

- **`harmonicrhythm.h`** — added two additive fields to `HarmonicRegion`:
  `std::vector<KeyModeAnalysisResult> keyAlternatives;` and `double keyConfidence = 0.0;`,
  documented as IN-MEMORY-ONLY (deliberately not serialized; no consumer yet — for L5).
- **`regionanalyzer.cpp`** —
  - new aggregate `RegionKeyReduction { chosen; alternatives; confidence; }`;
  - `localKeyForRegion` now returns `RegionKeyReduction` (the two early `seedKey`
    fallbacks return `{ seedKey, {}, 0.0 }`; the success path returns
    `{ rep.chosen, rep.alternatives, rep.confidence }` from the winning `repSlice`);
  - the Pass-1 call site binds `localKey = localKeyRed.chosen` (byte-identical to the old
    return) and the two construction sites set `keyAlternatives`/`keyConfidence`;
  - new helper `inheritRegionKeyContext(child, parent)` replaces the six
    `X.keyModeResult = parentRegion.keyModeResult;` Pass-2/2b inherit sites, so the carry
    travels with `keyModeResult`.

The chosen-key vote, the confidence scale, and every downstream key consumer (KeyArea,
cadence, pivot) are untouched. No production serializer entered.

---

## §3 — The two override-readiness lock-in tests

- **Key layer** (`regionanalysis_tests.cpp` —
  `Composing_RegionAnalysisTests.OverrideReadiness_ConfidentRegionCarriesKeyAltsAndConfidence`):
  runs `analyzeRegions` on `s1c_seg_changes.mscx` (C major I–V–vi–IV) and asserts a
  **confident** region (carried confidence ≥ the decoder's `uncertainThreshold`, i.e. not
  an uncertain seam) carries a **non-empty** ranked `keyAlternatives` + a positive
  `keyConfidence`, and each alternative is a key **other** than the chosen. Locks the
  forward-carry against silent removal at the reduction.
- **Chord layer** (`decode_chord_tests.cpp` —
  `Composing_DecodeChord.OverrideReadiness_CommitAndInheritCarryAlternativesAndConfidence`):
  asserts that a **Commit** slice and an **Inherit** slice each still carry a non-empty
  `alternatives` list AND a computed `confidenceModel` (`confidenceModel.margin ==
  confidence`), not only an Abstain — locking the override material L4 already provides.

Both assert the **contract** (presence + shape), not analyzer-echoed values.

---

## §4 — Gate (byte-identical)

| Check | Result |
|---|---|
| Build | green (27/27 targets; only the pre-existing `notationcontextmenumodel.cpp` C4100 warning) |
| `composing_tests` | **864/864** (862 baseline + 2 new; 2 disabled) |
| `notation_tests` | **53/53** |
| `pipeline_snapshot_tests` | **11/11 against EXISTING goldens — NO refresh** (P1–P4 output byte-identical) |
| BIR corpus | **Baroque 53 / Jazz 24 / Default 53** — unchanged |
| `.ours.json` byte-diff vs prior corpus (`c9633aebc4` baseline) | **0/353 changed on ALL three presets** |

**Method.** The existing per-preset corpora were generated at `c9633aebc4`; every commit
since (the dormant-L4 build `f21273ce3b`..`1e74f21ea4`, plus doc/tools-runner commits) is
byte-identical on the production batch path per STATUS, and `batch_analyze.cpp` is untouched
by this work. I fingerprinted all 353 `.ours.json` per preset (sha256) **before** regen,
regenerated each preset with the new binary, and re-fingerprinted: **0/353 differ on
Baroque, Jazz, and Default.** Byte-identity is strictly stronger than the BIR count, so the
`stem@tick` identity sets are preserved by construction; `characterise_bir_false.py` then
re-measured **53 / 24 / 53** (353/353 complete, manifest-validated, 326 WiR coverage) —
matching the gate exactly. No movement anywhere → byte-identical confirmed.

---

## §5/§6 — Assessment & delivery

- Production is **byte-identical**: no serializer changed; the snapshot goldens were not
  refreshed and pass; the `.ours.json` corpus is unchanged (<FILL>).
- The forward-carry is additive plumbing of already-computed data with **zero production
  consumers** — it exists for Layer 5.
- Commit (local, unpushed): `001199ac33` — the key-layer additive field + populate + the
  two lock-in tests (the §0 docs are the separate `08d1b541c1`). `upstream` untouched.
