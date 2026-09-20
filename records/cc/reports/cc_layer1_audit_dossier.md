# CC — Layer 1 (Note Model) READ-ONLY Audit Dossier

> Scope: read-only audit preceding the layer-1 implementation. Verifies the `[verify]` items in the **signed**
> design (`cowork_layer1_note_model_design.md`, user 2026-06-21), maps the consumers, and specifies the §6
> score-level test cases. **NO code / behavior / test-file change. HEAD `edd33901ed`.**
> North star: the note model must faithfully represent the **score**.
>
> **Provenance (no-assume rule):** every "currently does" / "the DOM does" statement below is from a source read
> this session, cited as `file:line`. Nothing is inferred from memory. Items I could not settle from source
> without a build are flagged explicitly with the best-evidenced reading and a proposed read-only probe.

---

## §0 — Headline verdict (what I confirm vs correct)

| Design claim | Verdict | Evidence |
|---|---|---|
| §4.0 engravingbridge has **no tie logic** | **CONFIRMED** | grep over `src/composing` — only `harmonicsegmenter.cpp` (a *different*, layer-2 module) touches `tieBack`/`tieFor`; the three collectors do not. |
| §4.0 per-note duration = `actualTicks()` (own length, not tied total) | **CONFIRMED** | `regiontonecollector.cpp:176,278`; `regiontoneprimitives.cpp:60` |
| §4.0 **mechanism**: tied continuations are "normally `play()=false`, skipped by the play filter → span truncated to first segment → backward query misses the sustain" | **CORRECTED — mechanism is wrong** | `note.h:273,501` (`m_play=true` default, plain user property); MusicXML import sets `play(!cue)` = **true** for non-cue notes and **never** `setPlay(false)` for a tie-stop (`importmusicxmlpass2.cpp:7236`); `.mscz` read restores the saved flag (`read460/tread.cpp:3332`). A tie-stop continuation therefore has **`play()==true`** and **is collected**, as a *separate* note event. See §1. |
| §4.1 grace/`!play`/`!visible`/ineligible are hard `continue` drops | **CONFIRMED** | all four collectors (citations in §2.1) |
| §4.2 fixed `Fraction(4,1)` backward cap in both collectors; header comment "4 quarter notes" wrong | **CONFIRMED** (cap = 4 **whole** notes = 16 quarter notes) | `regiontonecollector.cpp:148`; `regiontoneprimitives.cpp:83`; stale comment `regiontonecollector.h:110` |
| §4.3 `collectRegionTones` collapses to ≤12 PC accumulators | **CONFIRMED** | `regiontonecollector.cpp:91,395-416` |
| §4.4 two divergent paths only | **CONFIRMED** | `collectRegionTones` vs `collectSoundingAt`+`buildTones`; no third reader (§3) |
| §4.5 multi-responsibility module | **CONFIRMED** | slicing detectors + temporal context + pitch context co-located (§2.5) |

**Bottom line for §1:** the tie gap is **real and must be closed** (the note model must merge tied groups into one
span), but the design's *stated failure mode* is inaccurate. Ties are **not** silently dropped/truncated-and-lost;
they are **double-represented** — each tied segment is an independent note event with `play()==true`. The damage is
**inflation and false structure**, not omission (within the 4-whole-note cap). The corrected statement should
replace §4.0's mechanism before implementation, because the implementation's correctness tests differ accordingly
(we must assert "one merged span, no repetition-boost inflation, no false onset" — not "the note reappears").

---

## §1 — ★ Tie handling, end-to-end (the critical item)

### 1.1 What the module does (verified at source)
The engravingbridge module computes every note's sounding end as `segTick + cr->actualTicks()`:
- `regiontonecollector.cpp:176` (backward walk) and `:278` (forward walk) — `const int noteEnd = segTickInt + cr->actualTicks().ticks();`
- `regiontoneprimitives.cpp:60` (`collectSoundingAt`) — `const Fraction noteEnd = s->tick() + toChord(cr)->actualTicks();`

`DurationElement::actualTicks()` (`durationelement.h:57`) is the chordrest's **own** notated length. It is **not**
tie-aware. The DOM *does* expose the tied total — `Note::playTicksFraction()` (`note.cpp:1193-1199`):
```
if (!m_tieBack && !m_tieFor && chord()) return chord()->actualTicks();
return lastTiedNote()->chord()->endTick() - firstTiedNote()->chord()->tick();   // full tied span
```
— and `firstTiedNote()`/`lastTiedNote()` (`note.cpp:3693-3733`) walk the chain. **None of these are called anywhere
in the composing module** (grep: 0 hits for `playTicks`/`firstTiedNote`/`lastTiedNote` under `src/composing`). So the
collectors are tie-blind by construction.

### 1.2 The decisive fact — tie-stop notes have `play()==true`
The design assumed tied continuations are skipped by `!n->play()`. They are not:
- `note.h:273` `bool play() const { return m_play; }`; `note.h:501` `bool m_play = true;` — default **true**, a plain
  user "Play" toggle. Nothing in the DOM sets it from tie state.
- MusicXML import: `importmusicxmlpass2.cpp:7236` `note->setPlay(!cue);` — a non-cue note (the normal case, incl. a
  tie-stop) gets `play(true)`. The only import `setPlay(false)` paths are **cue** notes (`:7236`) and **grace** notes
  *when the main chord doesn't play* (`:2619`). There is **no** tie-stop → `play(false)` path (the tie code at
  `:2355`, `:7337`, `:8419` never touches `play`).
- `.mscz` read restores the persisted flag verbatim (`read460/tread.cpp:3332` `n->setPlay(e.readInt())`); a tied note
  saved by MuseScore carries `play=1`.

**Corroborating in-codebase evidence:** `harmonicsegmenter.cpp:192-198` filters `!n->play() || !n->visible()`
*first*, then **additionally** `if (n->tieBack()) continue;` (and symmetrically `:246` `if (n->tieFor()) continue;`).
That explicit second check would be dead code if `play()` already excluded tied continuations. Its presence is direct
evidence — by an author who needed tie-awareness — that **tied notes survive the `play()` filter**.

### 1.3 Corrected end-to-end behavior (the actual `onset`/`release` the pipeline sees)
A tie is stored as ≥2 separate `Chord`/`Note` objects on consecutive ChordRest segments, **all** `play()==true`,
`visible()==true`. Therefore:

- **Forward walk (`collectRegionTones`, within a region):** each tied segment is collected as its own event. For a
  PC accumulator (`regiontonecollector.cpp:296-308`) this means one held tied note contributes:
  - `durationInRegion` += each segment's clipped length → the **sum** ≈ the true sustained duration (incidentally OK);
  - `metricTicks.insert(segTickInt)` at **every** tied segment → `distinctMetricPositions` over-counts, so the
    **Pass-2 repetition boost** (`:315-324`, `×(1 + 0.3·(distinct−1))`) **fires on a single held note**, inflating
    its weight as if it were re-articulated. A note tied across 3 onsets is boosted ~×1.6. **This is a real defect.**
  - `trueAttackAtStart`/`onsetAtRegionStart` (`:301-303`) and `voiceCountAtTick` (`:300`) gain **false onsets** at each
    tie-continuation tick.

- **Backward walk (sustain reaching into a region from before `startTick`):** a tied note that attacks before the
  region: its *first* segment ends at the tie point (`noteEnd <= startTickInt` → skipped at `:184`), **but** the
  *continuation* segment that actually straddles `startTick` is a separate ChordRest, is itself visited by the same
  backward loop, has `play()==true`, and its own `actualTicks()` carries `noteEnd > startTickInt` → **it is collected.**
  So the sustain is **NOT missed** — contrary to §4.0 — *as long as that continuation segment lies within the
  `Fraction(4,1)` cap.* The only way a tied sustain is truly *lost* is the §4.2 cap (a tie chain longer than 4 whole
  notes), which is the cap defect, not a tie defect.

- **`collectSoundingAt` (point-in-time):** same — a note sounding at the anchor via a continuation segment is found
  through that continuation chordrest (`regiontoneprimitives.cpp:59-63`), not through tie-following. It then appears in
  `buildTones` as one tone (PC dedup happens downstream), so the point-in-time *set* is usually correct; the harm is
  again at the region/weighting level and in the per-event onset structure.

### 1.4 Does anything upstream merge ties before tone collection?
**No.** The only tie-aware code in the analysis path is `harmonicsegmenter.cpp`:
- `:196-198` onset detection skips `tieBack()` continuations (so a tie does not create a false slice boundary);
- `:241-258` release detection skips `tieFor()` notes (so a held tie does not emit a false note-off boundary).

This means **slicing is tie-aware but tone collection is not** — an asymmetry the design does not name. The segmenter
decides *where* region boundaries go using ties, then hands `[startTick,endTick)` to the tie-**blind**
`collectRegionTones`. `scoreharvest` (`metricweights.{h,cpp}`) has **no** note-reading or tie logic — it is beat
weights, decay, and the pedal-window index only (`metricweights.h:50-114`). No `scoreharvest`/pedal/beat helper
supplies a note fact that depends on ties.

### 1.5 §1 VERDICT
- **Tie logic is absent from the note-collection layer (engravingbridge): CONFIRMED.** The fix in the signed design
  (merge a tied group into one span, first onset → last release) is **necessary**.
- **The design's stated mechanism is INCORRECT and should be amended:** tied continuations are **not** `play()=false`
  and are **not** dropped; they are collected as **multiple independent onsets**. The end-to-end harm is
  **repetition-boost inflation + false onset/attack flags + per-segment (un-merged) spans**, plus a *capped* (not
  unbounded) loss only for tie chains exceeding the 4-whole-note backward horizon. The note-model layer must produce
  `playTicksFraction()`-equivalent **single spans** (via `firstTiedNote`/`lastTiedNote`) and count **one** onset per
  tied group.
- **Evidence basis:** source reads of the DOM (`note.h`, `note.cpp`), the importer (`importmusicxmlpass2.cpp`), the
  `.mscz` reader (`read460/tread.cpp`), the three collectors, and the segmenter — no build required. The
  `play()`-on-tie fact is established three independent ways (DOM default, import path, and the segmenter's redundant
  guard), so I state it as verified, not guessed.
- **Optional confirming probe (not required for the verdict):** a one-off read-only assertion in a scratch test —
  load `src/composing/tests/data/solid theory.musicxml`, fetch the voice-2 A4 tie-stop note in m17 (see §4), and check
  `note->play()==true && note->tieBack()!=nullptr && note->playTicksFraction() > note->chord()->actualTicks()`. This
  would empirically pin all three claims in one shot; it requires a build, so it is offered, not performed.

---

## §2 — Gap confirmations at source (the rest of §4 / the `[verify]` items)

### 2.1 Drop-not-annotate (§4.1) — CONFIRMED
Every read path hard-`continue`s on the filtering predicates; there is **no annotate-and-keep path**:
- grace: `regiontonecollector.cpp:173,233,274`; `regiontoneprimitives.cpp:56,171,241,331,412,470` (`cr->isGrace()`).
- `!play() || !visible()`: `regiontonecollector.cpp:178,237,289`; `regiontoneprimitives.cpp:66,177,248,335`.
- staff-eligibility: `staffIsEligible()` gate at `regiontonecollector.cpp:167,227,268`;
  `regiontoneprimitives.cpp:74,88,165,236,322,406,464`. The predicate itself (`regiontonecollector.h:88-102`) drops
  hidden (`!show()`), drumset (`useDrumset()`), and "Chord Track" staves.

**Boundary cases flagged:**
- **Cue notes** — imported with `play(false)` (`importmusicxmlpass2.cpp:7236`), so they are dropped by the `!play()`
  filter, *indistinguishably from user-muted notes*. The note model must flag cue-ness separately (it is a real
  sounding/engraved fact) rather than collapsing it into `plays=false`.
- **Grace notes** — dropped by `isGrace()` regardless of `play()`. Note: a grace note's `play()` is **true** unless its
  main chord doesn't play (`importmusicxmlpass2.cpp:2613-2621`). Target §6.1 wants grace **kept + flagged + attached
  to next slice**.
- **Editorial/tuning-invisible** — `!visible()` notes dropped; the inline comment at `regiontoneprimitives.cpp:67`
  ("skip … invisible tuning artifacts") shows this filter is doing double duty (intentional tuning artifacts *and*
  editorial cues are conflated). The model must keep `visible` as a flag and let downstream decide.
- **Unpitched-but-visible** — handled only via the drumset staff drop; a pitched note on a non-drumset staff with an
  unusual notehead is not specially handled (no evidence of a per-note unpitched flag in the collectors).

### 2.2 Fixed backward cap (§4.2) — CONFIRMED
- `regiontonecollector.cpp:148` `const Fraction backLimit = startTick - Fraction(4, 1);` (loop `:160-162`).
- `regiontoneprimitives.cpp:83` `const Fraction backLimit = anchorTick - Fraction(4, 1);` (loop `:84-86`).
- `Fraction(4,1)` = 4/1 = **4 whole notes** (16 quarter notes). The header doc comment
  `regiontonecollector.h:110` ("Walks backward up to 4 quarter notes") is **stale/wrong** — confirmed.
- Nothing represents a note's true span; range membership relies entirely on the backward walk + cap + per-segment
  `actualTicks()`. A note sustaining (or tie-chaining) longer than the cap, attacking before the window, is invisible.

### 2.3 PC-collapse (§4.3) — CONFIRMED
`collectRegionTones` aggregates into `PcAccum accum[12]` keyed by `ppitch()%12` (`regiontonecollector.cpp:91,197,296`).
Per PC it keeps only the **lowest** pitch/tpc (`:202-205,305-308,361-364`). Output is ≤12 `ChordAnalysisTone`
(`:394-416`). **Lost note-level facts:** voice identity, register beyond the lowest member of each PC, upper-voice
spelling (only the lowest member's tpc survives), and the individual onset of each note (only an aggregated
`distinctMetricPositions` count + an `onsetAtRegionStart` bool remain). `collectSoundingAt`+`buildTones` does **not**
PC-collapse (one tone per note, `regiontoneprimitives.cpp:111-117`) — the two paths differ here (see §2.4).

### 2.4 Two paths (§4.4) — CONFIRMED (these are the only two readers)
- **Path A — `collectRegionTones`** (`regiontonecollector.cpp:44-419`): region `[start,end)`, forward walk +
  backward-sustain reach, duration×beat weighting, repetition/cross-voice/pedal boosts, PC aggregation, bass pick by
  weight-fraction, normalized weights. Output: ≤12 weighted PC tones.
- **Path B — `collectSoundingAt` + `buildTones`** (`regiontoneprimitives.cpp:46-119`): point-in-time read at one
  anchor segment (+ backward reach for sustains), **no** weighting, **no** PC-collapse, one tone per note, lowest
  pitch flagged `isBass`. Output: per-note tones.
- Semantic differences: A is region-scoped/weighted/PC-folded; B is tick-scoped/unweighted/per-note. Both share the
  same filters (grace/play/visible/staff) and the same `Fraction(4,1)` backward cap, and **both are tie-blind**. No
  third note reader exists in production (grep §3). `collectPitchContext` (`regiontoneprimitives.cpp:121-198`) and the
  two sub-boundary detectors (`:200-370`) re-walk the score for *other* purposes (key context; slicing) — they read
  notes too but produce key/segmentation outputs, not the "what sounds" tone set; they are §4.5 co-tenants, not a
  third tone path.

### 2.5 Multi-responsibility module (§4.5) — CONFIRMED
`engravingbridge` (the `regiontonecollector.{h,cpp}` + `regiontoneprimitives.cpp` pair) co-locates, beyond note
reading:
- **Slicing/layer-2 detectors:** `detectOnsetSubBoundaries` (`regiontoneprimitives.cpp:200-289`),
  `detectBassMovementSubBoundaries` (`:291-370`).
- **Temporal context/layer-3:** `findTemporalContext` (`:372-512`) — actually *runs the chord analyzer* on neighbors.
- **Pitch context for key/mode (layer-3):** `collectPitchContext` (`:121-198`).
- **Weighting (layer-3 derived view):** the entire boost/normalize/bass-pick tail of `collectRegionTones`
  (`:314-418`).
All of these belong to other layers per the target; the note-model layer is reading + annotation only.

### 2.6 §4.6 minor `[verify]` items
- **Grace intent:** confirmed grace is dropped by `isGrace()` (not by `play()`); target wants keep+flag+attach-next.
- **`play()`/`visible()` semantics:** `play()` is the user mute/cue flag (`note.h:273`); `visible()` is engraving
  visibility (also used to drop "tuning artifacts", `regiontoneprimitives.cpp:67`). Both must become **flags**, and
  cue must be distinguished from mute (both currently land as `play()==false`).
- **scoreharvest/pedal/beat helpers:** confirmed they contribute **no note fact** (beat weight, decay, pedal windows
  only — `metricweights.h`). Pedal is a weighting concern (target §6 agrees), not a note-model fact.

---

## §3 — Consumer map (scopes what must adapt)

Full call-site set (grep `collectRegionTones|collectSoundingAt|buildTones` over `**/*.cpp`, plus the public
pass-throughs). `ebr::` = `mu::composing::analysis::engravingbridge`.

### 3.1 `collectRegionTones` — wants the **weighted-PC view**
| Call site | Purpose | Representation needed |
|---|---|---|
| `region/regionanalyzer.cpp:541-542` (callback wired), `:610`, `:640`, `:813`, `:867`, `:1017`, `:1063` | main region chord analysis + next-region lookahead + sub-region/lookahead | weighted-PC tones |
| `section/sectionanalyzer.cpp:449` (gap), `:648`, `:673`, `:698` (opening/display/carried-measure regions) | section-scope region analysis | weighted-PC tones |
| `harmony/harmonicsegmenter.cpp:378,530,723,803,895` | via `callbacks.collectRegionTones`; region/head/tail tone read during segmentation | weighted-PC tones |
| `notation/internal/notationcomposingbridgehelpers.cpp:199-206` | thin public pass-through to `ebr::collectRegionTones` | (re-export) |
| `notation/internal/notationimplodebridge.cpp:633` | implode feature region read | weighted-PC tones |
| `tools/batch_analyze.cpp` | **indirect** — delegates to `region::` orchestrator (`batch_analyze.cpp:547-554`), which wires the callback to `ebr::collectRegionTones` (`regionanalyzer.cpp:542`) | weighted-PC tones |
| tests: `regionanalysis_tests.cpp:315-316`, `notationimplode_tests.cpp:634,639`, `synthetic_tests.cpp:537` (ref) | fixtures | weighted-PC tones |

→ **Becomes a derived view** (`weightedPcView(noteModel, range, prefs)`) computed over the note model.

### 3.2 `collectSoundingAt` (+`buildTones`) — wants the **point-in-time per-note view (+ bass)**
| Call site | Purpose | Representation needed |
|---|---|---|
| `region/regionanalyzer.cpp:287` | onset-change Jaccard mask — uses only `sn.ppitch % 12` (PC set at a segment) | PC set sounding at tick (bass unused here) |
| `engravingbridge/regiontoneprimitives.cpp:422,480` (inside `findTemporalContext`) | cold-analyze prev/next neighbor chord → `buildTones` → `analyzeChord` | per-note list + `isBass` |
| `notation/internal/notationcomposingbridge.cpp:590,610` | status-bar single-tick chord readout | per-note list + `isBass` |
| `notation/internal/notationcomposingbridgehelpers.cpp:130-135` | using-decl pass-throughs of `collectSoundingAt`/`buildTones` | (re-export) |
| `notation/internal/notationcomposingbridge.cpp:65-66` | using-decls | (re-export) |

→ **Becomes a point-in-time query** (`soundingAt(noteModel, tick)` → notes; `bass` is `min(pitch)`); `buildTones`
becomes a trivial adapter from the queried note set, or is retired in favor of the model's note list.

### 3.3 `buildTones` — direct callers
`regiontoneprimitives.cpp:424,482` (in `findTemporalContext`) and `notationcomposingbridge.cpp:610`. All consume a
per-note tone list with `isBass`. No caller needs `buildTones` independently of `collectSoundingAt`.

### 3.4 Consumer-driven model requirements
- Two derived views suffice for all consumers: **(a)** weighted-PC region view, **(b)** point-in-time per-note set with
  bass. Both are queries over one note set.
- `regionanalyzer.cpp:287` needs only an **onset/sounding PC set per segment** — a third trivial query, satisfiable
  from the model.
- **No consumer needs a representation the design's §5 model lacks** — the model's
  `{pitch,tpc,staff,voice,onset,release,duration,isGrace,plays,visible,staffEligible}` covers every consumer above.
  (Possible additions to consider, not blockers: a **cue** flag, distinct from `plays`, given §2.1; and the four
  derived per-tone fields `ChordAnalysisTone` carries today —
  `weight/durationInRegion/distinctMetricPositions/simultaneousVoiceCount/onsetAtRegionStart/isBass` — which must be
  **recomputed by the weighted-PC view**, not stored on the note, and which the tie fix changes by counting one onset
  per tied group.)

---

## §4 — Score-level test-case spec (the §6 oracle) — SPEC ONLY, not built

Format per case: **fixture** → **correct note model** (the notes that truly sound, with onset/release/voice/flags).
"Minimal described score" cases are precise and synthesizable; one real corpus fixture is pinned for the tie case.
All ticks below use `Constants::DIVISION = 480` (quarter = 480, half = 960, whole = 1920).

### T1 — Tie across a barline (the critical case)
**Fixture (real, verified):** `src/composing/tests/data/solid theory.musicxml`, voice 2, pitch **A4**, half note in
m16 with `<tie type="start"/>` (`solid theory.musicxml:754-767`) tied into the m17 first half note with
`<tie type="stop"/>` (`:793-806`).
**Correct note model:** **one** A4 note, `onset` = m16 beat-3 tick, `release` = m17 beat-2 end tick (i.e. one span of
1920 ticks = the two half notes merged), `voice=2`, `plays=true`, `visible=true`, `staffEligible=true`.
**Must NOT produce:** two A4 spans of 960; two onsets; `distinctMetricPositions==2` for that PC; any repetition boost
attributable to the tie. (This is the exact case §1.3 shows the current code mishandles.)

### T2 — Tie chain of ≥3
**Fixture (minimal):** one voice, 4/4, three tied quarter notes C4 across ticks 0→480→960 (`tie start`, `tie
continue`/start+stop, `tie stop`), then a D4 quarter at 1440.
**Correct note model:** **one** C4 span `onset=0, release=1440` (`firstTiedNote.onset → lastTiedNote.release`), plus one
D4 span `onset=1440,release=1920`. Exactly two notes, two onsets. A region query over `[0,1440)` sees C4 as a single
held note (not three articulations).

### T3 — Sustain longer than the 4-whole-note cap
**Fixture (minimal):** one voice, a single (untied) note held for **5 whole notes** (or a tie chain spanning >4 whole
notes), onset at tick 0, release at tick 9600; then a query region `[7680, 9600)` (entirely inside the held note,
beginning >4 whole notes after onset).
**Correct note model:** the held note is returned for the query region (overlap query: `onset < rangeEnd &&
release > rangeStart`). **Current code fails this** (the `Fraction(4,1)` backward cap at `regiontonecollector.cpp:148`
cannot reach onset 0 from `startTick=7680`); the new overlap-query model must succeed with no horizon.

### T4 — Grace note
**Fixture (minimal):** an acciaccatura grace G5 immediately before a main chord C-E-G at tick 480.
**Correct note model:** the grace G5 is **kept**, flagged `isGrace=true`, attached-to-next per target §6.1 (its onset
groups with the tick-480 slice; it is **not** its own slice and **not** dropped). The main chord notes are normal
spans. (Today the grace is silently dropped by `isGrace()` `continue`.)

### T5 — Cross-staff
**Fixture (minimal):** 2-staff piano part; a note written on staff 2 but belonging (cross-staff beamed) visually to
staff 1, plus normal notes on both staves; both staves eligible.
**Correct note model:** every note present with its **owning staff index** and voice; eligibility flagged per staff.
No note dropped or double-counted because of cross-staff notation. (Tests that the model keys on the note's actual
`staff/track`, not on visual placement.)

### T6 — Multi-voice unison (two voices, same pitch)
**Fixture (minimal):** one staff, voice 1 and voice 2 both sounding **E4** at tick 0 (different durations, e.g. voice 1
half, voice 2 quarter).
**Correct note model:** **two** distinct E4 notes with `voice=1` and `voice=2` and their respective releases — both
represented. (Today `collectRegionTones` PC-collapses them into one accumulator and only records a
`simultaneousVoiceCount`; the note model must retain both with voice identity so the count is a *derived* fact.)

### T7 — Invisible / non-playing notes
**Fixture (minimal):** a chord C-E-G where E is `visible=false` (editorial) and a separate note B is `play=false`
(user-muted), alongside a normal note.
**Correct note model:** **all** notes kept; E flagged `visible=false`, B flagged `plays=false`, the rest `true`. The
keep/drop decision is a separate downstream step. (Today both E and B are dropped at the `!play()||!visible()` filter.)
Sub-case to assert: a **cue** note (imported `play=false`, `importmusicxmlpass2.cpp:7236`) is flagged distinctly from a
user-muted note — the model needs a cue flag to avoid conflating them (see §2.1, §3.4).

### T8 — Percussion / hidden / chord-track staff
**Fixture (minimal):** 3 staves — a normal pitched staff, a drumset staff (`useDrumset()`), and a part named
"Chord Track" — with notes on each.
**Correct note model:** notes on all three staves are **collected**, with `staffEligible=false` flagged on the drumset
and chord-track staff notes (and on any `!show()` hidden staff), `true` on the normal staff. (Today the entire staff is
hard-skipped by `staffIsEligible()`; the model must annotate, not silently omit, so a later view can still inspect
them.)

### T9 (corroborating, optional) — onset/release vs `actualTicks`
**Fixture:** the T1 tie-stop A4.
**Assertion:** `note->playTicksFraction() (1920) != note->chord()->actualTicks() (960)` and `note->play()==true` —
the empirical pin for §1.2/§1.3. (Requires a build; listed as the confirming probe, not a unit of the spec.)

**Coverage check:** T1–T2 (tie across barline + ≥3 chain), T3 (cap), T4 (grace), T5 (cross-staff), T6 (multi-voice
unison), T7 (invisible/non-playing + cue), T8 (percussion/hidden/chord-track) — all §4 mandated cases covered. Pedal is
deliberately **excluded** (target §6: pedal is a weighting concern, not a note fact; confirmed §2.6).

---

## §5 — Deliverable summary
- **§1 tie verdict:** gap CONFIRMED (engravingbridge is tie-blind; must merge tied groups into one span); design's
  *mechanism* CORRECTED with evidence (tie-stop notes have `play()==true`, so the harm is double-onset
  inflation/false structure + a capped sustain loss, **not** silent truncation/omission). Established from DOM,
  importer, `.mscz` reader, and the segmenter's redundant guard — no build needed.
- **§2 gap confirmations:** §4.1–§4.5 all CONFIRMED at `file:line`; §4.6 boundary cases (cue vs mute, grace,
  tuning-artifact conflation) flagged.
- **§3 consumer map:** complete; two derived views (weighted-PC region; point-in-time per-note+bass) + a segment PC-set
  query cover every consumer; the §5 model fields suffice, with a recommended **cue** flag.
- **§4 test-case spec:** T1–T8 (+ optional T9 probe) specified with fixtures and expected note models.

**`[verify]` outcome:** CONFIRMED — §4.1, §4.2 (incl. stale "4 quarter notes" comment), §4.3, §4.4, §4.5, no
upstream/scoreharvest tie-merge. **CORRECTED** — §4.0 mechanism (`play()` on tie / truncation-and-loss). **FLAGGED for
the model spec** — a `cue` flag distinct from `plays` (§2.1, §3.4).

**READ-ONLY — HEAD `edd33901ed`. No code, test-file, or production change made.** Cowork reconciles; user ratifies
before the implementation (which closes all gaps) is scoped.
