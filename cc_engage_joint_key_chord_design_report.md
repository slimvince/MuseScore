# Engage arc #10 — the joint key-and-chord step, architecture design: REPORT

> **Status: DESIGN DELIVERED (CC, 2026-07-07). READ-ONLY / STRUCTURE-ONLY — no `src/` change, no build, no
> corpus write, no constant fitted or tuned.** Executes `cc_instruction_engage_joint_key_chord_design.md`
> (engage arc #10). Deliverable: `cowork_joint_key_chord_design.md`. This report states what the design
> settles, its grounding, the owed-build spec, the owed-measurement list, and all SHAs.

---

## §0 — Headline

The joint key-and-chord step's architecture is designed as a **bounded coupling step** (not a unified
`(key,chord)` hidden state) that is the **total-unification completion (#6) of the built `decideJointKey`
machinery**. The one finding the whole design turns on: `decideJointKey` (J-key-i/ii/iii) already realizes the
**key-axis half** of the joint step — a key-state lattice, a Viterbi with a **key-transition prior**, a measured
**coupled minority** (~13.5%), and a **config-B chord→key coupling** — while its **chord axis is explicitly
deferred to "a faithful mechanism"** (`regionanalyzer.cpp:388-395` `[code]`). That deferred chord re-decode is
**exactly** the per-key re-decode C3 found computed nowhere. So the design is: **complete config-B's
one-directional coupling into a bidirectional (key, chord) beam by adding the deferred chord re-decode axis** —
gated on the C3 coupled minority, publishing forward to Part-1 L5 selection.

---

## §1 — What the design settles (per task)

- **Task 1 — Placement (§1 of the design).** A **bounded coupling step** at the L3/L4→L5 seam, **NOT** a unified
  joint hidden state. Decided against three binding constraints: **#7+#6** (L3/L4 are built as separate layers
  with separate decoders — a unified state discards and rebuilds both; the research's single-state model is a
  *modeling* choice, the *recipe* — beam + transition prior + re-decode — is factoring-independent); **magnitude
  realism** (the joint win is qualitative on the ~13.5% coupled minority, so a bounded coupling that fires only
  there and is a pass-through on the majority is proportionate); **acyclicity** (the step is forward-only — it
  consumes L3's *already-carried* key alternatives, *drives* L4's pure re-decode, re-ranks the key **inside its
  own bounded closure**, and publishes one settled (key,chord) forward — no L3←L4 back-edge). The
  cycle-introducing placement (L4 writing back into L3's committed key + re-running L3's Viterbi) is named and
  avoided.

- **Task 2 — Coupling mechanism (§2).** A **beam of (key, chord) hypotheses** per coupled region; the chord
  **re-decoded under each carried key** via the existing `ChordSliceDecoder` (the owed axis; the "faithful
  mechanism" J-key-iii named, since the decoder is a pure function of (slices,key) with no multi-pass artifact);
  the **key-transition prior reused** from `decideJointKey.transitionPenalty` / the L3 `changeCost` (#6); an
  **additive, monotone, no-veto composition** (keyEmissionFit + chordFit|k + couplingTerm + −transitionCost) over
  the **re-decoded** chord (the completion of config-B); a **single forward beam/Viterbi pass** (recommended over
  a bounded fixpoint — linear, convergent, forward-only); and a **declared Class-M joint-decision confidence** =
  the margin of the winning joint hypothesis over the best different-key-or-root hypothesis, squashed (R5). All
  constants precision-phase; nothing fitted.

- **Task 3 — Trigger + interface (§3).** The **trigger is C3**, realized as a **two-stage gate**: a cheap
  pre-filter `(a)` key-uncertain (`HarmonicRegion.keyConfidence` < the sequence-margin bar 1.0, the D-L3a
  boundary confidence) `∧ (a′)` chord-structurally-ambiguous (L4 `openQuestion`/`Abstain`/low `composite`, or the
  `chordPinned=false` proxy); then the **exact `(b)`** (the winner root flips under a carried key) computed **by
  the step's own per-key re-decode** — which is *why* C3 was un-computable read-only (b IS the owed build). Only
  `(a)∧(b)` commits a coupled decision; the rest is a pass-through. **Interface:** reads L3's carried
  `keyAlternatives`/`keyConfidence` (the step is the long-awaited consumer of that in-memory carry, #12) + L4's
  per-key carry; emits the settled `(k*, c*)` + joint confidence **forward** to L5, which **selects within the
  settled key** (Part-1 §4.1 boundary kept); L5 never re-ranks the key (that is the joint step's job) — acyclicity
  held.

- **Task 4 — the owed build (§4).** Specified by layer, enumerated not built: **B1** the per-key re-decode
  driver (Layer 4 — N forward calls of the built decoder, no new decoder; prerequisite = the distinct-root-
  preserving carry owed at E4); **B2** the beam/coupling driver (the joint step — a **generalization of
  `decideJointKey` config-B**, NEW = the chord axis + joint-margin confidence, not a parallel module); **B3** the
  two-stage trigger gate; **B4** the production wiring (completing J-key-iii's deferred chord axis, behind its
  existing held flag). The whole build is forward-only, bounded, and **E4-adjacent** (builds on the engaged
  decoder).

- **Task 5 — owed measurements (§5).** Six flagged, each with its read-only instrument, none assumed: [owed-1]
  the true C3 fire-rate (the ~13.5% `coupled` is a structural proxy, not `(a)∧(b)`; un-measurable until B1);
  [owed-2] the coupling benefit magnitude (the robust-stop sandwich on the coupled set, post-B2 — the eventual
  acceptance gate); [owed-3] the per-key winner flip-rate; [owed-4] beam width / fixpoint depth; [owed-5] the
  chord→key coupling term under re-decode; [owed-6] all precision-phase constants (Stage-5 fits).

---

## §2 — Grounding (every load-bearing claim tagged, #1)

- **The built key-axis half + the deferred chord axis:** `section/jointkeydecision.{h,cpp}` — the lattice
  (`jointkeydecision.h:53-56`), the coupled flag (`jointkeydecision.cpp:289-297`), `couplingScore`
  (`:275-287`), the Viterbi transition prior (`:300-314`, `JointKeyWeights.transitionPenalty`), the held wiring
  flag (`jointkeydecision.h:205-215`); the explicit chord-axis deferral `regionanalyzer.cpp:388-395`. `[code]`
- **The C3 trigger definition + un-computability:** `cowork_confidence_contract.md` §6-C3 `[contract]`;
  `cc_engage_c3_measurement_report.md` §2.3 (per-key re-decode computed nowhere) `[data]`.
- **The research recipe:** `cowork_functional_analysis_research_grounding.md` §3 (beam + key-transition prior +
  chord re-decoded under alternative keys; Raphael & Stoddard single state = a modeling choice; Wu & Yoshii
  parallel/branching/sequential taxonomy; magnitude realism — qualitative win on hard cases). `[research]`
- **The built layers consumed:** L3 carry `HarmonicRegion.keyAlternatives`/`keyConfidence`
  (`harmonicrhythm.h:118-119`, in-memory, no consumer yet); L4 decoder `ChordSliceDecoder::decode` (a pure
  function of (slices,key); "this increment takes one key", `chordslicedecoder.h:130-133`); the L3 change cost
  (`keymodesequence.h:124-131`, `:261`); the "never forced" residual (`keymodesequence.h:70-72`). `[code]`
- **The L5 boundary + carry contract:** `cowork_layer5_engagement_design.md` §2 (distinct-root carry, exclusion
  tail #12), §4.1 (the joint step is a distinct downstream step, a bounded forward instance; L5 selects within a
  fixed key), §4.3 (the O-18/C3 hinge — the exclusion tail is carried *so the joint step can re-rank the key*).
- **The doc is the O-4 deliverable** ("the C3 joint-step design document", `cowork_stage5_fitter_design.md` O-4).

---

## §3 — The owed-build spec (for the eventual, separately-ratified build event)

| # | Build | Layer | Reuse/new | Prerequisite |
|---|---|---|---|---|
| B1 | per-key chord re-decode driver | Layer 4 (decoder caller) | reuse the built decoder (N forward calls) | distinct-root-preserving carry (E4) |
| B2 | beam/coupling driver + joint confidence | the joint step (L3/L4→L5 seam) | generalize `decideJointKey` config-B; NEW = chord axis + joint margin | B1 |
| B3 | two-stage C3 trigger gate | joint step entry | reuse `keyConfidence` + L4 `openQuestion`/`composite`; (b) from B1 | B1 |
| B4 | production wiring (complete J-key-iii's chord axis) | region orchestrator + L5 input | complete J-key-iii, behind its held flag | B1/B2/B3 |

**Acceptance gate for the build event:** the robust-unit stop (class-(b) root-disagree DURATION non-increasing
per preset, `a8_rebaseline_measure.py` → `robust_stop_diff.py`) + the batch 52/24/52 secondary; the build must
move the robust stop **favorably** on the coupled set ([owed-2]). Held until ratified (#14), exactly as
J-key-iii is.

---

## §4 — Sandwich (trivial — read-only)

- **No `src/` touched** ⟹ both regression stops **green by construction**, byte-identical to HEAD `32709a9e7a`
  (STATUS records batch **52/24/52** set-diff empty + robust sandwich identity-PASS at this HEAD; no analysis
  code changed ⟹ both inherit the green state; no re-measurement run — nothing perturbs them).
- **No build** ⟹ suites unchanged (**1101 / 53 / 11**), no golden refresh.
- **No corpus write, no constant fitted or tuned** (R5; #8). Corpus frozen `c50002fee1`.

---

## §5 — Acceptance checklist (this pass)

- ✅ **Placement decided vs the acyclicity rule (#7), grounded** — bounded coupling step, not a unified state;
  the cycle-introducing placement named and avoided (design §1).
- ✅ **Coupling mechanism designed structure-only, constants precision-phase (R5)** — beam + per-key re-decode +
  reused key-transition prior + additive composition + declared Class-M joint confidence (§2).
- ✅ **Trigger grounded in C3 + interface to Part-1 selection** — the two-stage `(a)∧(a′)`+exact-`(b)` gate; the
  forward interface; acyclicity kept (§3).
- ✅ **Minimal owed build specified by layer, not built** — B1–B4 (§4), a generalization of `decideJointKey`.
- ✅ **Owed-measurements flagged, not assumed (#5)** — six, each with its read-only instrument (§5).
- ✅ **Design doc + report + fold with SHAs** (this report + `cowork_joint_key_chord_design.md`; HEAD
  `32709a9e7a`).
- ✅ **No src/build/corpus/fit; both stops green; pushed fork-only** — §4 above.

---

## §6 — SHAs / provenance

- HEAD at design: **`32709a9e7a`** (branch `master`, fork-only, ahead 0).
- Corpus frozen: **`c50002fee1`**.
- Deliverable: `cowork_joint_key_chord_design.md` (force-add).
- Report: this file (force-add).
- Fold (`docs(cowork):`): the design doc + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
  `cowork_stage5_fitter_design.md` (O-26 + O-4 close) · the instruction (force-add).
- Push **fork-only** — never toward `upstream`/`musescore/MuseScore` (`cfc7eb5e39` HARD STOP honored).

*CC, 2026-07-07. Engage arc #10 — the joint key-and-chord step, architecture design (read-only, structure-only).
On this report: Cowork verifies at objects → presents the design + the owed build/measurements to the user.*
