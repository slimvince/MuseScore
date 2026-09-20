# Phase 5c — Step 2 (Layer 5 / FUNCTION): the cadence detector (§5.2)

> **Discipline:** Step 2 of `cowork_phase5c_l5_build_plan.md`, against the SIGNED contract
> `cowork_layer5_function_design.md` §5.2 + the §5.0 shared defs. Built **DORMANT** (new unit, no production
> consumer) → **byte-identical on production**. **Default constants only — firewall, no tuning (§3).** Reuse the
> key-agnostic frame; BUILD the corrected event-pair + leading-tone-RESOLUTION logic. This dossier is gitignored.
>
> **HEAD `20b1185057`** (Step-2 code). Prior: `2ea81834b8` (§0 docs sweep), `811272bdd1` (Step 1).

## 0. Result — GREEN, built, all gates pass

- **§0 sweep** committed `2ea81834b8`. **§2/§4 build + tests** committed `20b1185057`.
- **Build clean**; **composing 895 → 908 (+13)**; **notation 53** (4 skipped, baseline); **pipeline_snapshot 11/11
  — NO golden refresh** (the byte-identical proof). **Corpus 53/24/53 unchanged by construction** (no production reach).
- **§1 verdict:** all event-pair inputs reachable; the phrase gate consumable; one finding declared (the seventh is
  not on the L4 projection → derive from pitch content). No structural change beyond the dormant unit → no STOP.

---

## §0 — Sweep (done)

Committed local-only `2ea81834b8` (`docs(cowork): Phase-5c Step-1 ratification + §5.0 syncs`):
`cowork_layer5_function_design.md` — the Step-1 §5.0 shared-defs syncs (the parameter-free "metrically strong" note +
the same-root quality-resolution-is-not-a-progression note). `scratch_artifacts/` is gitignored and was not committed.

---

## §1 — INVESTIGATE-confirm (read-only) — GREEN, no STOP

### (a) The event-pair inputs are reachable — ✅ (one finding declared)

| §5.2 input | Reachable from | Source (verified) |
|---|---|---|
| **Committed chords of the approach→arrival pair + inversion/bass** | L4 `ChordSliceCandidate` | `chord/chordslicedecoder.h:297` (`rootPc`, `quality`, `bassPc`, `bassIsRoot()`); region path `ChordIdentity` (`chordanalyzer.h:260`) carries the same |
| **Leading-tone RESOLUTION as a voice-motion event (L1 voices across the boundary)** | L4 `FocalNote` (per note, per voice) | `chord/chordslicedecoder.h:416` (`pitch`, `voice`, `onset`, `release`, `pc()`), projected from the L1 NoteEvent stream via the indexed `NoteModel::overlapping` |
| **Genuine dominant (a seventh / tritone resolving)** | the **pitch content** (per-voice notes), NOT the projection | see ★ finding below |
| **Bass scale-degree pair** | `bassPc` of both events, relative to the candidate tonic (the arrival/dominant-implied root) | key-agnostic — the cadencekeyanchor frame (`normalizePc(a.rootPc − 7)`) |

**★ Finding declared (no STOP — the faithful route needs no structural change).** The seventh is **NOT** on the L4
`ChordSliceCandidate` projection: its `quality` is the `ChordQuality` enum, which has **no seventh** — V and V7 both
read as `Major` (the seventh lives on `ChordIdentity.extensions` `Extension::MinorSeventh`, `chordanalyzer.h:273`, dropped
by the slice projection). So §5.2's "a genuine dominant (a seventh or its tritone resolving)" and its leading-tone
**resolution** — both pitch-content / voice-motion events by definition — are read from the **per-voice notes** the
resolution event already needs, NOT from the quality label. This is the faithful reading of §5.2's event framing and
requires no structural change (no new field forced onto the L4 projection). It IS why the unit's input view carries
per-voice notes (`CadenceVoiceNote`), not just the committed-chord identity.

### (b) The phrase gate is consumable — ✅

`engravingbridge::phraseBoundaryTicks(score)` (`engravingbridge/phraseboundaryview.h:175`) returns the picked
phrase-boundary ticks (fermata / section-end / final-bar, the graded Layer-1.5 model). The dormant detector consumes a
per-event `endsPhrase` flag (the cadencekeyanchor `CadenceRegionInput::endsPhrase` precedent); at engage the flag is
computed from `phraseBoundaryTicks`. Producer-agnostic: the detector takes the flag, not the score.

### (c) Reuse vs build — precise

- **REUSE (the key-agnostic frame + primitives):** the cadencekeyanchor frame — V→I read purely from root pc + quality
  (`root(dom) = root(tonic)+7`), the `endsPhrase` / salience inputs, and the salience-weighted tonic-vote shape
  (`aggregateGlobalAnchor`'s monotone weighted-sum convention, incl. the `wBase 1.0 / wStructural 2.0` seed style);
  plus the Step-1 `functionprogression::isLicensedProgression` for the pre-dominant→dominant **sequence** test.
- **BUILD (the corrected logic that REPLACES the broken presence test):** the cadencekeyanchor genuine-cadence gate is
  a leading-tone-**PRESENCE** test (`pcInMask(a.pitchClassMask, leadingTone)`, `cadencekeyanchor.cpp:79`) — the major
  third is present in **every** major triad, so it false-positives on I→IV / I→V. This unit does **NOT** reuse that
  logic. It builds: (1) the leading-tone **RESOLUTION** event (`leadingToneResolves` — the 7̂→1̂ **same-voice** motion
  across the boundary); (2) the **genuine-dominant** gate (`isGenuineDominant` — a seventh present, or the 7̂–4̂ tritone
  resolving to 1̂–3̂); (3) the inversion-anchored typology; (4) the **cadential-6/4 collapse**; (5) the chorale phrase
  gate. Together (1)+(2) kill the I→IV false positive (a plain tonic triad has no seventh and no resolving tritone).
- **NOT touched:** the circular production `detectCadences()` (`section/sectioncadencedetection.cpp:55`, key-dependent
  on the resolved `function.degree`) — its retirement is Phase 5d.

**No input unreachable; the corrected detector is a clean new dormant unit (no structural change); the broken
presence test is NOT reused → proceeded.**

---

## §2 — The cadence detector (§5.2), dormant — `function/functioncadence.{h,cpp}`

Key-agnostic, event-pair, feature-scored. Producer-agnostic view types (`CadenceVoiceNote{voice,pitch}`,
`CadenceEvent{rootPc,quality,bassPc,notes,metricWeight,startTick,endTick,endsPhrase,isFinalBar}`); output
`FunctionalCadence{type,approachTick,arrivalTick,tonicPc,minorMode,tonicVote,+evidence flags}`; enum
`FunctionalCadenceType{None,PerfectAuthentic,ImperfectAuthentic,Half,PhrygianHalf,Deceptive,Plagal,Evaded}`.

- **Cadential-six-four collapse FIRST.** `isSecondInversionTonicTriad` (a Maj/Min triad whose bass is its own fifth)
  **never registers as a tonic arrival**; and when such a 6/4 (root = candidate tonic) sits over the **held bass** of a
  root-position dominant, it is collapsed into the dominant approach (`sixFourCollapsed`), so the predominant sequence
  reads past it and the cadential bass reads 5̂→1̂ from the dominant to the tonic.
- **Authentic test.** Dominant form V (Major on 5̂) **or** a viio leading-tone chord (Diminished on 7̂); **and**
  `leadingToneResolves` (7̂→1̂ same-voice event, never presence); **and** `isGenuineDominant` (seventh present, OR the
  7̂–4̂ tritone resolving to 1̂–3̂); **and** the §5.2 **sequence** (a pre-dominant before the dominant — subdominant-family
  degree OR `isLicensedProgression` into the dominant; the 6/4 collapse handled).
- **Typology by the BASS-DERIVED INVERSION criterion** (the §5.2 amendment): **PAC** ⟺ a V with BOTH chords root
  position (bass reads 5̂→1̂); **IAC** is the complement (inverted dominant/tonic, or the viio substitution). **The
  top-voice arrival is NOT used** — no top-voice requirement, no melody identification (honoured: the unit reads no
  soprano line). **Half** (terminal phrase-final dominant); **Phrygian half** (iv6 bass b6̂ → V bass 5̂, a descending
  semitone, minor mode); **deceptive** (a dominant set up to cadence arriving on vi/bVI); **plagal** (subdominant-family
  → tonic at a phrase boundary, no intervening dominant) and **evaded** (a set-up dominant whose tonic arrival is
  replaced) at **lower confidence** by rule.
- **Chorale phrase-gate:** every type is admitted only when the arrival `endsPhrase` (consumes the phrase-boundary flag).
- **Weighted tonic-vote** (`cadenceTonicVote`): a monotone-increasing weighted sum of the evidence cues (bass 5̂→1̂,
  leading-tone resolution, genuine seventh) and salience cues (metric weight, phrase boundary, final bar), minus the
  per-type lower-confidence discount (half/plagal/evaded). **Key-agnostic** — the vote reads no resolved key; it
  *informs* the key. Clamped at 0; direction fixed.

### Build-detail decisions (declared, not assumed)

1. **"Bass 5̂→1̂" is operationalized as the PERFECT criterion, not a hard authentic gate.** §5.2's authentic paragraph
   lists "bass 5̂→1̂" among the requirements, but the §5.2 amendment + the §4 oracle (IAC = inverted tonic) make
   perfect/imperfect the **inversion split** and admit an inverted IAC whose bass does **not** read 5̂→1̂. So the
   authentic *family* gate is (form V / viio) ∧ LT-resolution ∧ genuine-dominant ∧ sequence; `bassFiveToOne` (both root
   position) then distinguishes PAC from IAC and is an evidence cue in the vote. This matches §4 exactly.
2. **A plain triad V→I (no seventh, no resolving tritone) is NOT detected as authentic** — the deliberate, stated §5.2
   choice ("a genuine dominant (a seventh or its tritone resolving)") that kills the I→IV false positive. Accepted per
   proportionality (build the spec, don't widen).
3. **`chromaticLeadingTone` (a cadencekeyanchor primitive) is NOT in the §5.2 vote.** §5.2's vote cues are evidence
   (bass/LT/seventh) + salience (metric/fermata/section/final) − discount; the chromatic-LT marker is not among them, so
   the unit takes no `keySignatureFifths` and stays signature-free. Available to reuse later if a precision-phase tier
   wants it; not added now (firewall).
4. **Evaded is the loosest, lowest-confidence type** (no §4 oracle): a genuine dominant set up to cadence (LT present +
   pre-dominant + genuine) whose phrase-final successor is NEITHER tonic, submediant, nor dominant. Conservative;
   gated by the phrase boundary like the rest. The "re-launch" form is not separately detected (out of scope; HC/evaded
   are the literature's weak end — held low, not chased).
5. **Half-cadence ambiguity is accepted, not chased.** Key-agnostically, any phrase-final major triad can read as a V
   of (root−7); the pre-dominant guard + phrase gate + the per-type discount are the §5.2 design. HC held at low
   confidence by rule (the weakest link).
6. **Namespace / placement:** the unit is `mu::composing::analysis` in `analysis/function/` beside
   `functionprogression` / `functionromannumeral`. The detector function is named `detectFunctionalCadences`
   (distinct from the production `detectCadences` in the same namespace — no collision).

---

## §3 — Constants

The tonic-vote weights and per-type discounts are **provisional DEFAULT seeds** (`FunctionCadenceParams`), NOT tuned —
the firewall (Phase B fits them). Only the **direction** is fixed (every evidence/salience cue non-negative; half /
plagal / evaded carry a lower-confidence discount). Seeds mirror the cadencekeyanchor convention (`wBase 1.0`, the
structural/phrase term the largest single bonus `wPhraseBoundary 2.0`, evidence cues `1.0`, discounts `0.5`). The half
cadence is held at the modest default — not chased.

---

## §4 — Tests (oracle-asserted) — +13

`tests/functioncadence_tests.cpp` (13), asserted against theory (not analyzer echoes):

- **PAC vs IAC by inversion:** a root-position V7→I (both root position) is **PerfectAuthentic** (bass 5̂→1̂, LT
  resolves, genuine seventh); the same with an inverted tonic is **ImperfectAuthentic** — **by inversion, with the
  soprano still on C** (the §5.2 amendment, pinned: the top voice does not force the call); a **viio substitution**
  (Bdim→C, the tritone resolving) is **ImperfectAuthentic**.
- **Cadential six-four:** ii→I64(C/G)→V7→I reads a **PerfectAuthentic** with `sixFourCollapsed` true and the bass 5̂→1̂;
  the I64 is **never** a tonic arrival; a bare …→I64 ending a phrase yields no authentic cadence.
- **Phrygian half:** iv6 (Dm/F, bass b6̂) → V (E, bass 5̂) with the descending-semitone bass is **PhrygianHalf**,
  tonic A, minor mode.
- **Deceptive:** ii→V7→vi is **Deceptive**, voting for C, major key (vi).
- **A passing I→IV is NOT a cadence:** in I→IV→V7→I only the phrase-final V7→I PAC is found; the mid-phrase I→IV
  produces no cadence (no arrival at its tick).
- **The corrected discriminators:** `isGenuineDominant` is **false** on a plain major triad, **true** on a V7 (seventh)
  and on a viio whose tritone resolves; `leadingToneResolves` is an **event** — true only on a 7̂→1̂ **same-voice**
  motion (false when the LT is merely present/sustained, false when C arrives in a different voice).
- **Structural predicates** (`isRootPosition`, `isSecondInversionTonicTriad`); **plagal** (IV→I at a boundary); the
  **weighted vote** (a PAC outvotes a half at equal salience; the half still casts a positive, discounted vote for the
  right tonic).

(All 13 green on the first full run.)

---

## §5 — Gate — PASS (dormant + byte-identical)

| Gate | Result |
|---|---|
| Build | clean (`scratch_artifacts/build_step2.log`; the only "error/failed" grep hits are a CMake VLA probe + an opus comment) |
| `composing_tests` | **908/908** (895 + 13; 2 disabled pre-existing) |
| `notation_tests` | **53** passed (4 skipped — baseline) |
| `pipeline_snapshot_tests` | **11/11** PASSED, **NO golden refresh** (1 skipped pre-existing) |
| Corpus **53/24/53** | **unchanged by construction** — not re-measured (see below) |
| Production reach | **none** — grep of `src/` + `tools/` finds the new identifiers only in the two module files, the test file, and the two CMakeLists |
| Production `detectCadences()` | **untouched** (no edit to `sectioncadencedetection.cpp`) |

**Why the corpus regen was not run** (the Step-1 / session-9 precedent + CLAUDE.md scoping): the new unit has **no
production consumer** (verified by grep), touches **no** scoring/gate/template code, and the pipeline snapshots refreshed
**zero** goldens — so P1–P4 output is byte-identical and the BIR gate cannot move. The corpus-regen gate is scoped to
gate/scoring changes; this is neither.

---

## §6 — Stops — none triggered

Every event-pair input reachable; the corrected detector is a clean dormant unit (no structural change); the broken
leading-tone-presence logic was **not** reused (the corrected resolution event replaces it); the live `detectCadences()`
was not touched; no threshold/weight tuned (firewall); no production movement; no `upstream` touched.

## Commits (local, unpushed)
- `2ea81834b8` — `docs(cowork): Phase-5c Step-1 ratification + §5.0 syncs`.
- `20b1185057` — `feat(function): L5 key-agnostic event-pair cadence detector (Phase 5c Step 2, dormant)`.
