# Candidate open items — the four-perspective review pass of 2026-08-01/02 (Cowork, while the register-completion dispatch runs)

> **STATUS: SUPERSEDED BY ROWING (2026-08-02, after the user's review).** Every finding below now
> has its register disposition: NEW ROWS OI-243…OI-257; dated notes on OI-239 (B-1/B-14), OI-228
> (B-5), OI-74 (B-11), OI-213 (C-2 re-scope), OI-238 (C-4); C-3 deduplicated against OI-242
> (CC found it independently); B-13/B-15/C-7/C-8-inventory items carried in OI-257 or left as
> recorded inventory here. This file remains as the review-pass provenance record. Original
> banner follows.
>
> **STATUS (original): CANDIDATE FINDINGS — NOT YET ROWS.** Produced by Cowork during the user's absence via
> four parallel read-only reviews (the perspective-inventory channels: population variation,
> oracle/invariant checking, feature census, requirement-side enumeration). **Nothing here has
> been written into the open-items register**: the register-completion dispatch is in flight and
> owns that surface (the recorded concurrent-edit hazard, OI-85), and rowing candidate findings is
> a deliberate act after user review. **Establishment status: every finding below was produced by
> a sub-agent review session; items marked ★verified were re-checked by Cowork at the cited
> source; the rest are cited but not independently re-read.** No fix, no design, no repository
> change was made by any of this work.
>
> Disposition vocabulary used below: NEW ROW (a distinct undiscovered issue) · EXTENDS <OI-n> (new
> instances of a rowed issue) · RE-SCOPES <OI-n> (changes what an existing row means) · DOC-SYNC
> (a #10 item for the named file's next touch) · DECISION-SURFACE INPUT (feeds a pending ruling,
> no row needed) · INVENTORY (a fact worth recording, no defect).

---

## A. The transposition-equivariance probe (invariant check — the headline finding)

**A-1. The production decode is NOT transposition-equivariant. ★verified (mechanism sites).**
Protocol: 12 pieces (deterministic sample), established first — the untransposed decode reproduces
the committed `decode_parity_ref.json` 12/12 exactly; predictions registered before measuring
(≥99 % segment equivalence expected). **Measured: 811/1224 segments (66.26 %); only 6 of 36
piece×shift conditions fully equivariant; segment boundaries moved in 27 of 36; per shift +2 =
83.3 %, −3 = 65.2 %, +6 = 50.2 %, with three near-total collapses at +6 (worst 0/32).** Music
theory says a transposed piece has the transposed analysis; the six bit-exact conditions prove the
apparatus itself is sound. Diagnosed mechanisms, both ★verified at the source by Cowork:
- **(i) The spelling factor is anchored to a canonical per-tonic spelling** —
  `tools/joint_estimator/probe_decoder.py:743` (`key_lof = _PC_TO_FIFTHS[tonic % 12]`), with the
  fitted note-table binning relative to that anchor (`gen_note_tables.py:218-233` per the probe's
  diagnosis). A uniformly respelled edition moves the anchor by ±12 fifths for wrap-set tonics,
  re-binning a whole tonality's diatonic tones as pooled chromatic (or a competitor's chromatic as
  diatonic); content scores move, and with them the semi-Markov segmentation. The signature prior
  is exonerated (its fold is invariant, `probe_decoder.py:406-412`).
- **(ii) The key-prune tie-break is not transposition-covariant** — `probe_decoder.py:1045` ranks
  by `(−fit, absolute tonic pitch class, mode)`; under transposition the tie order permutes and
  the expected shifted key can fall out of the kept top-K entirely (5 of 17 label-only violations).
  This compounds **OI-226**: the candidate-admission prune that entered production with no
  ratified basis is now ALSO measured representation-non-covariant.
Caveat carried: the probe models transposition as a uniform respelling (an engraver's choice);
+6 semitones is genuinely enharmonically ambiguous, so SOME +6 divergence is defensible — but
moved boundaries and 0/32 collapses are not an enharmonic-frame difference. Artifacts:
`outputs/transposition_probe/report.md`, `transpose_state.json`, `run_probe.py` (agent-written
measurement script — itself unestablished beyond the P1 check; a repo-side re-run belongs to any
rowing of this finding). **Disposition: NEW ROW (likely two — the spelling-anchor
representation-sensitivity; the non-covariant prune tie-break folding into the OI-226 family);
also DECISION-SURFACE INPUT to the struck-vs-sounding family design (the family's subject is
"what the model reads"; this adds "and in which representation").**

## B. The notation-feature census (the fact adapter's input surface vs the ratified Layer-1/2 rules)

The adapter collects notes with exactly three rules — drop grace, drop non-positive duration,
drop excluded staves (`jointfactadapter.cpp:393-399`) — and never reads the Layer-1 eligibility
flags (`plays`, `visible`, `staffEligible`) or voice identity. Against the ratified rules
(`ARCHITECTURE.md:1045-1053`), per feature:

**B-1. Eligibility ignored wholesale: invisible notes, muted/non-playing notes, hidden staves,
and percussion staves ALL enter the harmonic evidence.** The Layer-2 rule admits a note iff
`plays && visible && staffEligible` and the Layer-1 header claims non-playing notes are "excluded
from every analysis view" (`note_model.h:77-79`) — now false on the production path. Highest
impact: a drum staff's arbitrary pitch numbers enter pitch-class evidence and the bass pick.
**Disposition: EXTENDS OI-239 (its difference (1), made concrete as four feature classes);
the drum-staff case may deserve its own row.**

**B-2. Grace notes are dropped unconditionally, while the ratified Layer-2 rule says a grace note
opens a boundary by its span** (`jointfactadapter.cpp:393` vs `ARCHITECTURE.md:1073-1077`,
`slicer.cpp:43-48`). And the tree now carries THREE different eligibility rules for one Layer-1
surface: the adapter (only `!isGrace`), the slicer (the three flags, no grace exclusion), the
legacy views (three flags AND `!isGrace`). One question, three answers (#6). **Disposition:
NEW ROW (the three-rules inconsistency), with the grace-note handling one of its faces.**

**B-3. Concert vs written pitch are MIXED inside one record on transposing instruments:** the
pitch-class field comes from sounding pitch (`ppitch`), the line-of-fifths spelling field from the
WRITTEN tpc when the score displays written pitch, and the signature prior from the concert key
(`note_model.cpp:93-94`, `note.cpp:826-829`, `jointfactadapter.cpp:360`). On a B♭-clarinet score
the spelling factor and the key prior are fed contradictory evidence — and finding A-1 shows the
spelling factor is exactly where representation errors bite. Unexercised by the chorale corpus.
**Disposition: NEW ROW.**

**B-4. The key signature is read from staff 0 at tick 0 only** (`jointfactadapter.cpp:358-367`):
mid-score key changes never enter the prior, and staff 0 is read without any eligibility or
exclusion check (it could be the program's own chord track, or a drum staff). **Disposition:
NEW ROW.**

**B-5. Anacrusis notes are dropped from the decode but their boundaries stay in the lattice**
(`jointdecoder.cpp:103-136` skips `measure == 0`; the lattice was built from all notes,
`jointfactadapter.cpp:458-462`) — manufacturing pickup events with empty onset evidence, a
second source (beside release boundaries) of the zero-onset windows the OI-228 family documents.
**Disposition: EXTENDS the OI-215/226/227/228 family enumeration.**

**B-6. The meter arithmetic is wrong off common time:** `nQuarter = num*4/den` integer-divides
(3/8→1, 7/8→3, 6/16→1, `jointfactadapter.cpp:352`); compound meter is recognized only at
denominator 8 (`:119-122`); the mid-strong beat class can only fire in 4-quarter bars (`:79`).
The beat-strength class is a FITTED covariate of the boundary factor, so segmentation evidence is
systematically mis-classified in those meters. **Disposition: NEW ROW.**

**B-7. The reconstructed metrical grid assumes a constant nominal bar length and detects only a
leading pickup** (`jointfactadapter.cpp:163-184`); a mid-score meter irregularity drifts the grid
permanently (acknowledged only for "pathological xml" at `:126-129`). **Disposition: NEW ROW
(shares a design surface with B-6).**

**B-8. Repeats, voltas and jumps are not unfolded, and no recorded rule says so** (zero references
to the repeat list anywhere under `src/composing`): volta-1's last bar and volta-2's first bar are
treated as temporally adjacent by the transition and cadence-approach machinery — a progression
that is never heard. **Disposition: NEW ROW (an unstated-decision finding of the OI-226 class:
the rule needs deciding, then recording).**

**B-9. A two-note tremolo is read as two sequential half-length chords** rather than one sustained
dyad (`chord.cpp:540-571` duration halving; no tremolo handling anywhere in the analysis path).
**Disposition: NEW ROW (low priority; unexercised by fit corpus).**

**B-10. Bar-repeat signs (`MeasureRepeat`) contribute zero notes** — those bars are silent to the
analysis (`measurerepeat.h:33` is a Rest; `note_model.cpp:227` takes chords only). **Disposition:
NEW ROW (information loss, #12).**

**B-11. Voice identity is destroyed at the adapter** (`NoteRec` has no voice field,
`jointdecoder.h:47-51`) and the melodic approach/departure covariate pairs notes across merged
voices and staves of a Part (`jointfactadapter.cpp:279-320`) — soprano paired with alto on a
shared staff. The shared-surface voice-blindness is rowed (OI-74); the melodic-covariate
consequence is new. **Disposition: EXTENDS OI-74 (the joint-module face).**

**B-12. Fermata detection is track-exact** (`note_model.cpp:81`): a fermata on voice 1 does not
flag a simultaneous voice-2 chord — and the flag feeds both the boundary factor and the cadence
covariate. **Disposition: NEW ROW (small, fitted-covariate-affecting).**

**B-13. Ottava lines and guitar capo offsets enter the bass pick** through `ppitch()`
(`note.cpp:2515-2560`): an 8vb line changes which note is "the bass" relative to the written
score. Defensible (sounding pitch is sounding), but nowhere decided. **Disposition: INVENTORY,
unless the family design rules otherwise.**

**B-14. The adapter deliberately builds its lattice from the tie-UNRESOLVED note surface** (each
tie continuation a separate onset) for parity with the fitting extraction, while the ratified
Layer-2 slicer merges tie chains — so "the atomic analysis unit" (register entry D-023) is not the
same object in the two halves of the system, recorded only in a header comment
(`jointfactadapter.h:53-66`). **Disposition: EXTENDS OI-239 (a fourth recorded difference,
deliberate-but-unspecified).**

**B-15. A part excerpt analyzed through the same seam as a full score carries no marker of being
a single-part analysis.** **Disposition: INVENTORY / future input-scoping question.**

## C. The requirement-side review (outside-in: user tasks → mechanisms → establishment)

**C-1. The status-bar harmonic annotation is NOT localized and NOT wired to the accessibility
tree:** raw string concatenation with no translation call (`notationcomposingbridge.cpp:835-844`),
appended to the accessibility info as plain text (`notationaccessibility.cpp:203-207`), never
entering `screenReaderInfo`. `ARCHITECTURE.md:5815-5819` (§12.1) mandates MuseScore's Qt
localization for ALL new user-visible strings (English + Swedish) and MuseScore's accessibility
patterns — a ratified statement the production path departs from, and precisely the user's
2026-08-01 i18n point. **Disposition: NEW ROW (non-conformance, the OI-231 pattern: decision
cited, departing code cited).**

**C-2. `addAnalyzedHarmonyToSelection` is unreachable from the UI:** implemented, interfaced,
mocked, behavior-snapshot-tested — and registered to no action, no menu, no shortcut (repo-wide:
no caller). The three annotate action codes route to `addHarmonicAnnotationsToSelection` instead.
**Disposition: NEW ROW; RE-SCOPES OI-213 (its N-produce multiplier concerns a command no user can
currently invoke — the cost fact stands, its exposure does not).**

**C-3. §12.1a claims interactive analysis cost is "negligible (well under 1ms)"** — measured
seconds-per-query on the default path (OI-203/OI-206). **Disposition: DOC-SYNC (a false claim at
the canonical home, the OI-232 class).**

**C-4. §5.13's caller column is stale beyond what OI-238 records:** the implode bridge contains no
call to `analyzeHarmonicContextAtTick` at all; the tuning bridge calls different functions.
**Disposition: EXTENDS OI-238.**

**C-5. Test-coverage gaps against principle #11**, enumerated: `NotationAccessibility` — no test
anywhere; the context-menu model — no test; the single-write `addAnalyzedHarmony` and the per-note
"Tune as" — no test; the record arm has NO cache/incremental-recompute test (the existing decode-
cache tests exercise the legacy arm only — the fixture never sets the flag); every large-score
test is `DISABLED_` (measurement, not a gate), and the enabled golden corpus caps at 16 measures;
the golden suite is arm-mixed (two snapshot keys built by direct legacy calls while three go
through the flag-ON seams). **Disposition: NEW ROW (one row, the enumerated list inside it —
feeds OI-199's record-seams partition rather than duplicating it).**

**C-6. §12.1b documents 2 of the 9 registered harmonic-analysis actions.** **Disposition:
DOC-SYNC.**

**C-7. The tuning-anchor score marking ("altezza di riferimento" Expression) is a user-facing
behavior with no menu presence and no test** (`ARCHITECTURE.md:4968-5013`,
`notationtuningbridge.cpp:479`). **Disposition: INVENTORY + the C-5 test-gap list.**

**C-8. Right-clicking a CHORD anchors analysis on `notes().front()`** — an undocumented
representative-note choice (`notationcontextmenumodel.cpp:210-214`). **Disposition: INVENTORY /
doc-sync at the layer specification.**

## D. Extent-evidence distillation (no new rows — decision-surface inputs)

The full fact sheet feeds the OI-210 surface draft (`cowork_extent_decision_surface.md`). Two
points worth naming here: the OI-207 adjudication's dated note on OI-210 establishes that the
EXTENT axis was last ruled BOUNDED (D-030/D-031, user-ratified 2026-07-02, postdating the 3.1b
shelving) — so the open questions narrow to WHICH bounded form, the re-read FREQUENCY, and
whole-piece's place on the effort dial; and every cost figure feeding that surface comes from
generators not yet audited (the OI-199 measurement-tools partition), so the surface labels each
figure's establishment status rather than treating it as settled.

## E. What this pass says about the method (one paragraph)

Four channels of the perspective inventory ran; all four produced findings, and the two
highest-yield ones were exactly the two the precedent predicted: an invariant check nobody had
run (A-1) and input populations the envelope never contained (B-1…B-15 — thirteen of the fifteen
census features are unexercised by the fit corpus). The requirement-side channel found the
only-user-visible defects (C-1, C-2) that no code-inward audit had reached. This is the measured
case for adopting the §6 program of `cowork_oi200_perspective_inventory.md` when OI-200's turn
comes.
