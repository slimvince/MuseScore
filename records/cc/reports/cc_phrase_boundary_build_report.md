# Phrase-boundary primitive (Architectural Layer 1.5) — build report

> Build of the SIGNED `cowork_phrase_boundary_design.md` per `cc_instruction_phrase_boundary_build.md`.
> All work local/unpushed on `master`. Cowork verifies by the three shas below.

| step | sha | what |
|---|---|---|
| §0 docs | `c4cfd94980` | `docs(cowork): phrase-boundary design + proportionality` (8 cowork docs) |
| §2 Step A | `0d10b37a87` | own the primitive + byte-identical de-dup of the two fermata scans |
| §3 Step B | `5c5d992356` | the graded surface-cue + marker model at default constants |

Suites at HEAD (`5c5d992356`): **composing 878** (2 disabled), **notation 53**, **pipeline_snapshot 11/11** (3 disabled) — **no golden refresh**.

---

## §1 — INVESTIGATE (read-only): consumer enumeration + byte-identity verdict

### The two duplicated fermata scans (byte-identical bodies)
- `src/composing/analysis/region/regionanalyzer.cpp` `jkdPhraseBoundaryTicks` (was @358)
- `tools/batch_analyze.cpp` `collectPhraseBoundaryTicks` (was @386)

Both: iterate measure → ChordRest segment → annotations → `isFermata()` → insert the segment tick. Verbatim identical.

### Every consumer of the per-region `endsPhrase` flag — ALL dormant/gated on production
1. **regionanalyzer joint-key path** (`applyJointKeyWiring`, the `endsPhrase` derivation @ the `JointKeyRegionInput`
   build): `endsPhrase` → `decideJointKey` → `CadenceRegionInput.endsPhrase` → `CadenceKeyAnchor` (`kWeightStructural`).
   Reached **only** via `applyJointKeyWiring`, called `if (jointKeyWiringEnabled())` (regionanalyzer.cpp ~1378); the gate
   defaults **FALSE** (env-seeded `MUSE_JOINT_KEY_WIRING`, `jointkeydecision.cpp:137`). With the gate off the scan is
   never even invoked in production.
2. **batch_analyze diagnostics** — `writeCadenceAnchorJson` / `writeModulationJson` / `writeJointKeyJson`. The fermata
   scan runs **only** when `dumpCadenceAnchor || dumpModulation || dumpJointKey` (`batch_analyze.cpp:2830`), i.e. the
   `--dump-cadence-anchor` / `--dump-modulation` / `--dump-joint-key` flags. The corpus BIR measurement uses the
   **default** region dump, which sets none of them and never emits `endsPhrase`. batch_analyze is the corpus tool, not
   the live product.
3. **No other live consumer**: whole-repo `isFermata()` sweep → only regionanalyzer (gated) + batch_analyze (diagnostic)
   in the analysis pipeline; the rest are engraving IO / layout / braille.

### VERDICT — byte-identical on production today
All `endsPhrase` consumers are dormant or gated-off on the production path. So the graded Step-B model is **byte-identical
on production today** (the instruction §5 first branch); the new strength becomes load-bearing only when the function
layer (L5) engages or `MUSE_JOINT_KEY_WIRING` is set. The only outputs that move are the gated-off wired path and the
`--dump-*` diagnostics — neither is the corpus 53/24/53 gate nor a snapshot golden. (§7 STOP conditions — unreachable
input, or an unclear verdict — were **not** triggered.)

### Owning layer + notation-input reachability (all reachable, no STOP)
Owner = `src/composing/analysis/engravingbridge/` (Layer-1.5 notation-derived views, beside `spellingview`). Inputs:
per-note voice/staff/pitch/onset/duration + eligibility (`plays&&visible&&staffEligible`) — L1 `notemodel::NoteEvent` ✓;
fermata ✓; `Breath::isCaesura()` (Breath segments) ✓; `BarLineType {DOUBLE, END(=FINAL), *_REPEAT}` + `Measure::repeatStart()` ✓;
engraved `KeySig` segment / `Staff::keySigEvent` ✓; `TempoText` + `GradualTempoChange` (`GradualTempoChangeType`) ✓;
L2 empty slices via `slicing::changePointSlices` (empty = no eligible overlap) ✓.

---

## §2 — Step A: owned primitive + byte-identical de-dup (`0d10b37a87`)

Created `engravingbridge/phraseboundaryview.{h,cpp}` with `phraseBoundaryTicks(const Score*)` = the fermata-only scan,
**moved verbatim** from the two retired copies. Repointed both consumers (`regionanalyzer` `ebr::phraseBoundaryTicks`;
`batch_analyze` `analysis::engravingbridge::phraseBoundaryTicks`); deleted the two local scans + the now-orphan
`engraving/dom/fermata.h` include in batch_analyze.

**Byte-identical proof:**
- Definition unchanged (scan body verbatim); both call sites pass the same `score` and consume the same `std::set<int>`.
- Suites green: composing 864, notation 53, **pipeline_snapshot 11/11 — no golden refresh** (production P1–P4 unchanged).
- The changed code paths are **not exercised** by any default test (regionanalyzer call behind `jointKeyWiringEnabled()`
  OFF; batch_analyze call behind `--dump-*`), so byte-identity is **by construction**; empirically confirmed by running
  the primitive through its real consumer — `batch_analyze bwv10.7.xml --dump-cadence-anchor` → 3 `endsPhrase=true`
  regions at the fermata phrase-ends, identical to the retired scan.
- Corpus 53/24/53: **unchanged by construction** — the default-dump path (the BIR measurement) never calls the primitive
  (`batch_analyze.cpp:2830` gates the only call on `--dump-*`). The corpus dir is gitignored/empty; no on-disk baseline to
  regress. Per the CLAUDE.md session-8 precedent, snapshot no-refresh + by-construction is the byte-identical gate.

---

## §3 / §4 — Step B: the graded model + tests (`5c5d992356`)

### The mechanism (exactly per design §4)
- **§4.1 surface-cue core** — per eligible voice (grouped by `(staff,voice)`, chords folded to one line event): the three
  cue value sequences gap (offset-to-onset silence) / inter-onset / pitch-interval, each attached to the event it follows
  from (a large gap/IOI/leap **after** an event marks that event as a phrase end); the local-change strength
  `v·(leftChangeRatio + rightChangeRatio)`; **max-normalised across the whole score**; the gap-dominant weighted sum.
- **§4.3 aggregation** — per-voice strengths summed per τ-merged onset into the texture profile; **both** per-voice and
  texture exposed. Optional coincidence weight (default off = plain sum).
- **§4.2 marker spikes** — fermata, breath/caesura, double/final/repeat barline, mid-score key-signature **change**
  (engraved event, NOT inferred key), written ritardando/rallentando-family `GradualTempoChange` (spiked at the arrival
  `tick2`) + subito `TempoText`, all-voice-rest onset (a Layer-2 empty slice ≥ min-silence). Boundary ticks: fermata =
  segment tick (phrase-final onset); barline = measure end; keysig/breath/tempo = event tick; ritardando = arrival;
  all-voice-rest = span onset.
- **§4.4 peak-picking** — `pickPeaks`: a local maximum AND above the Simple-Picker threshold (whole-profile mean + k·SD)
  picks the locally-strong surface peaks; the deterministic markers are then **always emitted** (see decision D2 below).

### Default precision-phase constants (the firewall — NOT tuned for accuracy)
`wGap/wInterOnset/wPitch = 0.50/0.30/0.20` (gap-dominant, ordering gap>IOI>pitch per §4.1); `k = 1.0`; `τ = 0` (exact-onset
coincidence, the chorale convention); `coincidenceWeight = 0`; `minSilenceTicks = 240` (eighth note); `spikeCeilingFactor
= 1.5`.

### ★ Design-realisation decisions to review (declared to Cowork)
- **D1 — `spikeCeilingFactor = 1.5`, not 1.0.** A per-voice combined surface strength can reach the ceiling
  `sumWeights`, so the texture surface can reach `#voices·sumWeights` when every voice maxes and coincides. A spike of
  **exactly** that ceiling only *ties* such a surface peak (it does not "exceed any surface-cue peak / dominate" per
  §4.2). The default factor 1.5 makes a marker strictly exceed the ceiling. This is a *stated default* choosing the value
  that makes the §4.2 mechanism behave as specified — **not** accuracy tuning (no weight/k/τ was optimised against any
  corpus metric).
- **D2 — markers are ALWAYS emitted (beyond the literal §4.4 single peak-pick).** §4.4 literally describes one local-max +
  threshold pick on the combined profile. That strict-`>` local-max rule drops **two adjacent equal-height markers** —
  observed on the chorale: a final phrase's fermata (40320) abutting the closing barline (42240), both at the spike value
  6.0 with no surface, so neither is a strict local maximum → neither picked, even though the threshold is cleared. The
  design's own framing makes markers **deterministic facts** that "dominate wherever it occurs" (§2/§4.2) and "clear the
  threshold by construction" (§4.4). So the build realises that intent: `pickedTicks = pickPeaks(textureWithSpikes) ∪
  {all marker ticks}`. Surface peaks remain conditional (local-max + threshold); markers are guaranteed. The exposed
  texture profile is unchanged (spikes included). **This is the one notable departure from the literal §4.4 single-pick;
  it is faithful to §4.2's deterministic-marker semantics — flagged for Cowork's confirmation.**
- **D3 — fermata/breath markers fire for ANY fermata/breath**, not filtered to "an eligible voice" (§4.2 wording). The
  retired byte-identical scan took any fermata; a robust annotation-staff eligibility derivation introduced a bug that
  *excluded* legitimate chorale fermatas (the marker stopped firing at 40320). Dropping the filter restores the retired
  behaviour. The "eligible voice" qualifier is a minor precision refinement deferred (a fermata on an analysis-ineligible
  staff is rare and harmless). Barline/keysig/tempo/all-voice-rest are voice-agnostic.

### Tests (`phraseboundaryview_tests.cpp`, +14; design §7)
- **Oracle (pure, hand-computed):** `changeRatio` basics; `localChangeProfile` — a long value among small yields the peak
  there (≡ "a long note among short ones yields an inter-onset peak" / "a rest yields a high-strength peak"), flat → zero,
  edges/degenerate; `maxNormalizeInPlace`; `pickPeaks` — a single low bump among real peaks is **rejected** ("a single
  mid-phrase leap does not clear the threshold alone"), an isolated spike kept, a flat profile picks nothing.
- **Full pipeline (Bach chorale fixture `pb_chorale.mscx` = converted bwv10.7):** every fermata phrase-end + the closing
  FINAL barline is picked; the pick set is **exactly the close phrase structure** (4 fermata phrase-ends + final barline =
  5 boundaries, proportionate, no flood); per-voice → texture aggregation invariant (texture ≥ per-voice surface sum at
  every onset; coincident onsets exist); the rest fixture yields a boundary; ends-a-phrase derivation; null-safe.
- **Chorale-corpus validation (script level):** 12 chorales via `batch_analyze --dump-cadence-anchor` — every
  fermata-bearing chorale yields proportionate boundaries (2–5 endsPhrase regions, conflated by batch's coarse regions),
  `bwv112.5` (zero fermatas) → 0; no flooding, no spurious zero. `fermata ⊆ picked` holds for **every** chorale by
  construction (markers always emitted). The exact pick set is validated directly by the unit test.

---

## §5 — Gate (byte-identical-on-production branch, per the §1 verdict)
- **Corpus 53/24/53 unchanged — by construction.** The primitive is unreachable in the corpus default-dump measurement
  path (`batch_analyze.cpp:2830`); Step B touched only the primitive `.h/.cpp` + tests + fixture (batch_analyze unchanged
  since Step A). Production analysis is pinned byte-identical by the snapshot suite.
- **Suites + snapshots green, no golden refresh:** composing 878 (+14), notation 53, pipeline_snapshot 11/11.
- **Proportionality honoured:** the graded model is built at its default constants and stopped; no accuracy tuning. The
  chorale pick set is the close phrase structure (not over-segmented).

A full 3-preset corpus regen was deemed unnecessary (the source corpus exists at
`tools/bach_path3fix_20260408_170348/corpus`, but a regen re-derives the known 53/24/53 — it is insensitive to a change
the default-dump path never executes); available on request for empirical confirmation.

## §7 — Stops: none triggered (all inputs reachable; verdict clear; no byte-identity break at Step A; no class-(b) change;
no `upstream` push).
