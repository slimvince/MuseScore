# CC — Layer 1 (Note Model) IMPLEMENTATION report

> Implements the SIGNED design (`cowork_layer1_note_model_design.md`) + reconciled audit
> (`cc_layer1_audit_dossier.md`). A **correctness** change (not a refactor): downstream output
> moves on the tie/cap bug-fix cases, as intended. Gate = correctness + a holds-or-improves
> oracle metric, NOT byte-identity. **Local commit (unpushed); Cowork verifies; user ratifies.**
>
> BEFORE binary/corpus = HEAD `edd33901ed` working tree (B2 guard present but flag-OFF
> byte-identical). All tests/metrics below are this session's runs.

---

## §1 — The note model as built (`src/composing/analysis/notemodel/note_model.{h,cpp}`)

A first-class, lossless, tie-resolved representation in its **own module/namespace**
(`mu::composing::analysis::notemodel`). `NoteModel::build(score)` reads the score **once**;
queryable by tick range.

`struct NoteEvent { pitch, tpc, staff, voice, onset, release, duration, isGrace, plays,
visible, staffEligible }`.

- **Tie resolution (the critical fix).** A tied group is merged into ONE event: `onset` =
  first note's chord tick, `release = onset + Note::playTicksFraction().ticks()` (the DOM's
  tie-aware span = `lastTiedNote.endTick − firstTiedNote.tick`). Tie continuations
  (`tieBack() != nullptr`) are skipped — exactly **one onset per tied group**. Uses the
  mandated DOM API (`firstTiedNote`/`lastTiedNote`/`playTicksFraction`); no DOM change.
- **True spans + overlap query (cap fix).** Each event stores `[onset, release)`;
  `overlapping(t0,t1)` = `onset < t1 && release > t0`, **no horizon** — the 4-whole-note
  backward cap and backward-walk are gone. `onsetIn(t0,t1)` supports the pedal pass.
- **Collect-and-annotate, never drop.** Grace (from `chord->graceNotes()`, flagged
  `isGrace`, onset = parent chord tick), non-playing (`plays=Note::play()`), invisible
  (`visible=Note::visible()`), and staff-ineligible (`staffEligible` from the existing
  `engravingbridge::staffIsEligible` predicate, evaluated at the note's onset) notes are
  **kept and flagged**. Nothing is `continue`'d away.
- **One construction path.** The single builder replaces the two divergent readers.
- Build order = ascending onset, then staff/voice/chord-note → `m_notes` is onset-sorted by
  construction (overlap/onset queries scan the onset-bounded prefix).

### ★ Spec gap surfaced + user decision — `isCue` DROPPED
The signed design (§5.1) and audit (§2.1/§3.4) required an `isCue` flag distinct from `plays`.
Verified at the DOM: **cue-ness is NOT recoverable post-import.** MusicXML import collapses it
(`note->setPlay(!cue)`, importmusicxmlpass2.cpp:7236); there is **no** persistent per-note cue
property on `Note` (the only `cue` concept in the engraving DOM is `Ornament::cueNoteChord`,
unrelated). So a `<cue>` note and a user-muted note are byte-identical (`play()==false`,
nothing else). Per the no-assume rule I did not fabricate it (e.g. from `isSmall()`, which is
"small notehead" ≠ cue). **User decision (2026-06-21): drop `isCue`, document the gap.** It is
behavior-neutral: cue notes have `plays==false` and are already excluded by every view's
filter. T7's cue sub-assertion is reframed as "the cue note is kept and flagged `plays=false`."

---

## §2 — The derived views (in the engravingbridge module, over the note model)

- **`weightedPcView(noteModel, start, end, excludeStaves, parentStart, excludeLookAhead,
  prefs)`** — reproduces `collectRegionTones` (duration×beat weighting, repetition boost,
  cross-voice boost, pedal tails, PC aggregation, normalized weights, bass pick), **recomputed
  from the model**, counting **one onset per tied group** (the de-inflation) and finding
  sustains by **overlap** (the cap fix). View filter = `staffEligible && !excluded && plays &&
  visible && !isGrace` (reproduces the legacy analysis drop set exactly).
- **`soundingAt(noteModel, tick, excludeStaves, out)`** — point-in-time per-note view
  (onset ≤ tick < release); reproduces the legacy `collectSoundingAt` emission ORDER
  (anchor-onset notes first in staff/voice order, then sustained notes descending-onset).
  `buildTones` retained unchanged (pure adapter, marks min-pitch bass).
- The `regionanalyzer.cpp:287` onset-Jaccard PC set is built from `soundingAt`.
- **Score-based wrappers retained** (`collectRegionTones(sc,…)`, `collectSoundingAt(sc,…)`):
  thin one-shot adapters = `view(NoteModel::build(sc), …)`, for the cold notation
  pass-throughs / implode / tests (they get the tie/cap fix automatically).
- **`findTemporalContext`** now takes `const NoteModel&` (derives `sc` from it; uses
  `soundingAt`).

### Faithfulness correction found during verification — the `excludeLookAhead` quirk
The legacy dense-start look-ahead count had a quirk: start-onset notes were counted
**per-note without dedup** (an octave doubling at the downbeat — common in chorales — counts
its pitch class twice), while sustains were counted distinct. My first version deduped → an
un-fixed-case divergence (a §7 refactor bug). Corrected to reproduce the legacy two-part count
exactly (distinct sustain PCs + per-note start-onset increments). See §5 for the proof this was
the *only* reproduction divergence.

---

## §3 — Consumers rewired (per the audit consumer map)

- **`regionanalyzer.cpp`** (hot/gate path): builds the model **once** in `analyzeRegions`;
  `denseBoundaryTicks` takes the model; the segmenter callback captures it; all 7
  `collectRegionTones` → `weightedPcView`; `collectSoundingAt`@287 → `soundingAt`;
  `findTemporalContext` → model form.
- **`sectionanalyzer.cpp`** (snapshot/bridge path): builds the model once in `analyzeSection`;
  all 4 `collectRegionTones` → `weightedPcView`.
- **`notationcomposingbridgehelpers.cpp`**: the `findTemporalContext` pass-through builds a
  model and delegates (status-bar path; single tick).
- **Unchanged** (use the retained Score-based wrappers, get the fix for free): the notation
  bridge (`collectSoundingAt`/`buildTones`), `notationimplodebridge.cpp`, `batch_analyze`
  (indirect via the region orchestrator), the test callbacks.
- **NOT moved** (per the design — they stay until layers 2/3 are built): `collectPitchContext`,
  `detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`.

---

## §4 — T1–T8 score-level tests (`note_model_tests.cpp`, all PASS)

Fixtures authored as MusicXML and converted to `.mscx` via the built `MuseScore5.exe` (the
composing test binary cannot import MusicXML; .mscx are what `ScoreRW::readScore` loads). Both
the `.musicxml` source and the `.mscx` are kept (provenance).

| Test | Fixture | Asserts |
|---|---|---|
| T1 | `nm_solid_theory.mscx` (real: voice-2 A4 tie across barline) | ONE merged A4 span (DOM-derived onset→release), no false intermediate onset. Span derived from the DOM tie API → robust to measure numbering. |
| T2 | `nm_tie_chain.mscx` | 3 tied C4 → ONE span [0,1440); D4 [1440,1920); no intermediate onset; exactly 2 non-grace notes; `overlapping(0,1440)` size 1. |
| T3 | `nm_long_sustain.mscx` (C4 held 5 wholes) | ONE span [0,9600); `overlapping(7680,9600)` (past the old 7680 cap) returns it. |
| T4 | `nm_grace.mscx` | grace G5 kept, `isGrace=true`, onset = main chord tick; main C-E-G normal. |
| T5 | `nm_two_staff.mscx` | C5 staff 0, C3 staff 1 (keys on owning staff). |
| T6 | `nm_unison.mscx` | both E4 (voice 0 release 960, voice 1 release 480) retained. |
| T7 | `nm_flags.mscx` | all kept; G4 `visible=false`, cue B4 `plays=false`, rest true. |
| T8 | `nm_staff_eligibility.mscx` | normal staff + "Chord Track" staff both collected; chord-track `staffEligible=false`. |

**T8 scope note:** chord-track is the MusicXML-expressible representative. Hidden (`!show()`)
and percussion (`useDrumset()`) staves traverse the **identical** `staffIsEligible` predicate
(verified at source), so the annotation path is exercised; authoring hidden/drumset fixtures via
MusicXML is unreliable, so they are not separately fixtured.

---

## §5 — The gate: correctness + measured movement

**Both suites + snapshots:** composing **553/553** (545 + 8 new T1–T8), notation **57/57**,
pipeline snapshots **11/11** after a *verified* golden refresh (4 scores moved — see below).

### ★ Fidelity proof (§5.5 diagnostic, done rigorously)
A temporary env-gated **legacy mode** (un-merged per-segment ties + restored 4-whole cap on
both `weightedPcView` and `soundingAt`) was built and a Baroque corpus regen measured: the
legacy charged set was **byte-identical to BEFORE (3861, exact set match)**. This proves the
views reproduce the old collectors **exactly** on un-fixed cases — so **100% of the downstream
movement is attributable to the intended tie/cap fix**, with zero accidental reproduction
divergence. (The legacy run is what surfaced and then confirmed the fix of the §2
`excludeLookAhead` quirk.) The diagnostic toggle has been **removed**; the committed code is the
clean fix.

### Oracle-root metric (the standing per-event tiered gate) — BEFORE → AFTER
| preset | CHARGED | FLOOR | correct | BIR (secondary) |
|---|---|---|---|---|
| Baroque | 3861 → **3864 (+3)** | 4285 → 4285 (0) | 10110 → 10107 | 57 → **55 (−2)** |
| Jazz    | 4065 → **4066 (+1)** | 4276 → 4276 (0) | 9925 → 9924 | 23 → **24 (+1)** |
| Default | 3894 → **3895 (+1)** | 4285 → 4285 (0) | 10077 → 10076 | 57 → **55 (−2)** |

Tier deltas: KEY band essentially flat (Baroque KEY-HARD 375→375; Jazz 752→750; Default
384→384); the movement is in OVER-GRAB (segmentation) and CHORD-ID (vertical).

### ★ Honest read of the direction (for ratification)
The design *hoped* charged-error would move down/flat. The realized primary-gate result is a
**small increase (+3/+1/+1)**, while the secondary BIR mostly **improves (−2/+1/−2)** and FLOOR
is byte-flat on all three. **Every charged case that moved is proven tie-driven** (legacy proof
above), so this is an *explained* increase, **not** the §7 unexplained-regression hard-stop.

Traced added cases (Baroque, representative):
- `bwv154.8@6240/6480` — **identical pitch-class set, identical span**; only the winner flips
  V6→vii7. Cause: the tie de-inflation correctly removes a spurious *re-articulation* boost
  from a **held (tied)** note (a held note is not re-attacked, so it should not get the
  repetition bonus — it keeps its full duration weight). On this 5-PC ambiguous sonority the
  old bonus happened to push the oracle's root; removing it is the faithful model.
- `bwv2.6@18720`, `bwv316@14640` — greedy-expand **segmentation boundary shifts** (the more
  faithful tone weights move a boundary one tick earlier → over-grab). Part of the "churn" is
  the *same* charged event relabeled at the shifted reconstructed tick (e.g. bwv316 removed
  @14400 / added @14640; bwv315 removed @21360 / added @20640 — net 0 each).

Net genuine new disagreements ≈ 4 (Baroque) on a ~3900 baseline (~0.1%), against ~1 genuine new
agreement and the −2 BIR improvement. There is **no in-scope fix**: the de-inflation is the
mandated correct model, and how the (correct) de-inflated weights feed scoring/segmentation is
layer-3/2 logic, frozen by §7. The alternative (keep the bug) contradicts the design.

### Snapshot diffs (4 moved, goldens refreshed verified-not-blind)
All trace to tie de-inflation through the shared `weightedPcView` (the 7 unchanged scores
confirm fidelity on non-tie/cap cases):
- `bach_chorale_137`@17280: `Gmadd9` → `Gm7/Bb` (de-inflated weights drop the add9 reading).
- `bach_bwv806_gigue`@3840: `DMaj7` → `D` (a 7th no longer repetition-inflated).
- `bach_bwv806_prelude`@7920: `V7/ii` → `VI43`.
- `mozart_k279_1`: internal `score` values shifted (weights), chord identity unchanged on the
  first divergence.

---

## §6 — Deliverable / workflow
- New module `notemodel/` + views + consumer rewiring; T1–T8; 4 refreshed snapshot goldens.
- Committed **locally, unpushed**. Excluded from the commit: the pre-existing **HELD** B2
  guard (`section/localmodulationdetector.{cpp,h}`, `tools/batch_analyze.cpp`) and all other
  pre-existing working-tree edits; the gitignored corpora and this report.
- **For ratification:** the note model + tie-merge + views (reproduce old behavior except
  ties/cap, proven exact via legacy mode), and the oracle direction (+3/+1/+1 charged, fully
  tie-explained, FLOOR flat, BIR −2/+1/−2). The honest call the user must make: accept the
  faithful-model trade-off (correct model, tiny mixed metric movement) vs. not.

## §7 — Stop conditions encountered
- **Spec gap (`isCue`)** → surfaced, user decided (drop). Done.
- **Reproduction divergence (`excludeLookAhead` quirk)** → found via the legacy proof, fixed;
  re-proven byte-exact. Not left as a refactor bug.
- The oracle increase is **explained** (tie-driven, proven) → not the §7 hard-stop; reported
  for ratification per §6 rather than silently claimed as an improvement.
