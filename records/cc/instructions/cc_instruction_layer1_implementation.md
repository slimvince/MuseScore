# CC Instruction — LAYER 1 (Note Model): IMPLEMENTATION — close all gaps

> Design **SIGNED + amended** (`cowork_layer1_note_model_design.md`); audit **done + reconciled**
> (`cc_layer1_audit_dossier.md`). Build the lossless note model and close **all six gaps**. **★ This is a
> CORRECTNESS change, not a refactor: downstream output WILL move on the bug-fix cases (ties, long sustains), and
> that is the intended point.** The gate is correctness + a holds-or-improves oracle metric — **NOT
> byte-identity.** Commit locally; Cowork verifies; user ratifies. North star: the note model is faithful to the
> **score**; the downstream movement is toward the **DCML/music21 oracle**.

## §1 — Build the note model (lossless, one path, its own module)
A first-class representation — every sounding note in the score, annotated, queryable by tick range:
`{ pitch, tpc, staff, voice, onset, release, duration, isGrace, plays, visible, staffEligible, isCue }`.
- **★ Tie resolution (the critical fix).** Merge each tied group into **one** note: `onset = firstTiedNote()`'s
  onset, `release = lastTiedNote()`'s release (use the DOM `firstTiedNote()`/`lastTiedNote()`/
  `playTicksFraction()` — `note.cpp:1193-1199,3693-3733`). **One** onset per group; the continuation chordrests do
  NOT produce additional note events. (Fixes the double-onset / repetition-boost inflation / false-onset defects
  the audit proved.)
- **True spans + overlap query (cap fix).** Store each note's real `[onset, release)`; "what sounds in `[t0,t1)`"
  is `onset < t1 && release > t0`. **No `Fraction(4,1)` horizon, no backward walk.** A note sustaining any length
  is found.
- **Collect-and-annotate, never drop.** Grace, `!play`, `!visible`, ineligible-staff, and **cue** notes are
  **kept and flagged** (`isGrace`, `plays`, `visible`, `staffEligible`, `isCue`) — not `continue`'d away. Derive
  `staffEligible` from the existing predicate (hidden/drumset/chord-track) as an annotation. Distinguish **cue**
  (`importmusicxmlpass2.cpp:7236` `play(!cue)`) from user-muted, both of which are `play()==false` today.
- **One construction path.** A single note-model builder replaces the two divergent readers. Put it in its **own
  unit** (e.g. `note_model.{h,cpp}`), so the note-reading responsibility is cleanly separated (closes §4.5 *for
  the note model*; the co-located slicing/context helpers stay put and relocate when layers 2/3 are built — do
  NOT move them now).

## §2 — Re-express the old collectors as derived VIEWS over the model
The consumers keep their current semantics; only their *source* changes to the corrected note model. **The views
preserve the old filtering** (grace/`!play`/`!visible`/ineligible excluded from analysis) — so keeping those
notes in the model is downstream-neutral. The only fixes that propagate are **ties** and the **cap**.
- **`weightedPcView(noteModel, range, prefs)`** reproduces `collectRegionTones` (duration×beat, repetition,
  cross-voice, pedal boosts, PC aggregation, normalized weights, bass pick) — **recomputed** from the model, with
  the derived per-tone fields (`weight, durationInRegion, distinctMetricPositions, simultaneousVoiceCount,
  onsetAtRegionStart, isBass`) computed here, **counting one onset per tied group** (the de-inflation).
- **`soundingAt(noteModel, tick)` (+ bass = min pitch)** reproduces `collectSoundingAt`+`buildTones` (per-note,
  unweighted); `buildTones` becomes a trivial adapter or retires.
- **segment-PC-set query** for `regionanalyzer.cpp:287` (onset-Jaccard) — the PC set sounding at a segment.

## §3 — Rewire the consumers (per the audit's consumer map)
Point all call-sites at the views (no downstream *logic* change): `regionanalyzer.cpp` (541-542 cb, 610, 640, 813,
867, 1017, 1063, and 287 for the PC-set), `sectionanalyzer.cpp` (449, 648, 673, 698), `harmonicsegmenter.cpp`
(378, 530, 723, 803, 895 via callback), `findTemporalContext` (422, 480, 482), the notation bridges
(`notationcomposingbridge.cpp` 590/610, `notationcomposingbridgehelpers.cpp` pass-throughs,
`notationimplodebridge.cpp:633`), and the tests. `batch_analyze` is indirect (via the region orchestrator).

## §4 — Build the score-level tests (T1–T8 from the audit spec)
Implement `cc_layer1_audit_dossier.md` §4 as real tests: T1 (tie across barline — the pinned `solid theory.musicxml`
voice-2 A4 fixture), T2 (tie chain ≥3), T3 (sustain > 4-whole-note cap), T4 (grace kept+flagged), T5 (cross-staff),
T6 (multi-voice unison — both voices retained), T7 (invisible/non-playing + cue, kept+flagged), T8
(percussion/hidden/chord-track — kept + `staffEligible=false`). Each asserts the **correct note model** (faithful
to the score). T1/T2 specifically assert **one merged span, no repetition inflation, no false onset** — NOT
"the note reappears."

## §5 — The gate (correctness + measured improvement; downstream movement EXPECTED)
1. **Layer-1 correctness:** T1–T8 pass; the note model is faithful to the score.
1b. **Full coverage of the NEW code (standing objective, `cowork_handoff.md`):** every branch of the new
   note-model builder + the derived views is exercised by a test — T1–T8 plus targeted unit tests for any branch
   they don't reach (empty region, no eligible staff, all-rest region, single-note, grace-only, etc.). Don't ship
   uncovered new paths. (Report a branch-coverage check on the new files.)
2. **Both test suites** (`composing_tests`, `notation_tests`) pass; **pipeline snapshots** will move — inspect each
   diff, confirm it traces to a tie/cap fix and is correct vs the oracle, then update goldens (verified, not blind).
3. **Oracle-root metric (the standing per-event tiered gate) HOLDS-OR-IMPROVES** on Baroque/Jazz/Default — the
   tie de-inflation + cap recovery should move charged-error **down or flat**, never up by an un-explained case.
   Report the before/after tiers; any increase must be traced to a specific case and justified or fixed.
4. **BIR** reported as secondary (case-identity), but it is NOT the gate — the oracle-root metric is.
5. **Diagnostic (not a goal):** confirm the views reproduce the old output on **un-fixed** cases (no ties, within
   cap) — to prove we changed *only* via the intended fixes, not by accident. A change there is a bug to find;
   a change on tie/cap cases is the point.

## §6 — Workflow + deliver
Commit **locally (unpushed)**. Write `cc_layer1_impl_report.md`: the note-model design as built, the views + the
consumer rewiring, T1–T8 results, the per-event oracle-root before/after (with the changed cases traced to
ties/cap), the snapshot-diff inspection, and both suites. Cowork verifies at the committed object (the note model,
the tie-merge, the views reproduce old behavior except ties/cap, the oracle direction). User ratifies.

## §7 — Stop conditions
- The oracle-root metric **regresses** (charged-error up) with any case **not** explained by an intended tie/cap
  fix → STOP + report (an accidental regression, not the point).
- An un-fixed case (no tie, within cap) changes output → STOP (the view diverges from the old collector — a
  refactor bug).
- The note model needs a field the design lacks → STOP + surface (spec gap), do not assume.
- The change requires touching slicing/key/chord *logic* (downstream layers are frozen — only their *source* of
  notes changes, via the views) → STOP; rewiring is allowed, logic edits are not.
- Tie-merge would require a DOM change → STOP (use the existing `firstTiedNote`/`lastTiedNote`/`playTicksFraction`).
