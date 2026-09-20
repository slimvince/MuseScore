# CC — Phase 5b Step 2: G2/G3 — three-tier membership ladder + plausibility fix

**Commit (local, unpushed):** `1b7fee1cd5` — `feat(composing): L4 G2/G3 — three-tier membership ladder +
plausibility check (Phase-5b Step 2, dormant)`. `git show --stat` lists exactly **three** files:
`chordslicedecoder.cpp`, `chordslicedecoder.h`, `decode_chord_tests.cpp` — decoder + tests only, no production
wiring. (The working-tree `cowork_phase5b_l4_build_plan.md` change is the Step-0 grounded-order doc edit — *not
mine*, left uncommitted; excluded from this commit.)

**Method:** INVESTIGATE-confirm (§1) → BUILD G2/G3 dormant (§2) → RE-MEASURE new-vs-legacy, accuracy **and**
coverage (§3) → ASSESS (§5). Build-it-right per the signed spec (`cowork_layer4_chordsymbol_design.md` §5 step 3 /
§5 step 4); no inference-quality tuning. `upstream` untouched.

---

## TL;DR — the assessment FAILED → **STOP (do not push to Step 3)**

1. **The membership ladder (G2) + plausibility check (G3) are built per spec and are ACCURACY-NEUTRAL.** Replacing
   the flat weak-OR-stepwise rule with the three-tier structure-first ladder, and re-pointing the plausibility
   penalty at the **required (template)** tones, moved among-committed chord-root only **77.0 % → 76.9 %** (Baroque,
   coverage-matched 66.9 % → 66.7 %) — i.e. a wash on accuracy, while correctly raising NCT recall (4.7 % → 11.8 %).
   This part is sound.
2. **The inherit RELAXATION (§5 step 4, also mandated by Step 2) is the regressor.** Relaxing inherit to "a thin
   slice whose extra notes are stepwise NCTs of the prevailing chord inherits it" **dropped abstention materially**
   (53.0 % → 48.9 %, +4.1 pts coverage — the intended effect) **but regressed accuracy**: among-committed
   **76.9 % → 72.6 %** (−4.3, now −1.3 vs the legacy 73.8 %) and **coverage-matched 66.7 % → 64.8 %** (−1.9). The
   newly-inherited duration is ~79 % **wrong**.
3. **Why:** the note-only inherit rule cannot tell a **continuation** of the prevailing chord from a **transition**
   to the next one — a thin slice whose notes are stepwise embellishments *of the prevailing chord* is just as often
   heading *to the next chord*. Distinguishing them needs the next chord / function — **Architectural Layer 5**. The
   new misses are overwhelmingly thin slices (Baroque: 45 → **300**), exactly the inherit targets.
4. **Per plan §5/§7 this is a STOP** ("accuracy regresses → STOP, report (amend)"). The G2/G3 ladder+plausibility is
   committed (correct, dormant, byte-identical, green). The sequence does **not** advance to Step 3. The open
   question for Cowork: the spec's §5-step-4 note-only inherit over-inherits as measured — does the inherit need
   **Layer-5 (next-chord/function) evidence**, the **§15-O2 bounded-window joint resolution**, or a **tighter
   structural inherit condition**? (Decomposition/spec question — flagged, not decided here.)

---

## §1 — INVESTIGATE-confirm (the incremental check — maps cleanly onto the as-built decoder, no STOP)

Read the spec's membership rule (`cowork_layer4_chordsymbol_design.md` §5 step 3 + step 4) against the as-built
`chordslicedecoder` flat membership. All three Step-2 hooks map onto the decode loop without a structural change
beyond the decoder:

- **The three tiers map onto the per-tone classification.** The as-built `isStepwiseTreated` already computes the
  per-side step signals (a passing tone = "approached AND left by step between chord tones"; a suspension = "held
  from prev, resolves down by step to a CT"). The ladder needs only to **expose** those signals per side and read
  them: (1) **both-sides-stepwise OR suspension → NCT regardless of weight** (the old `isStepwiseTreated == true`
  case, unchanged ✓); (2) **reached AND left by leap → chord-tone extension regardless of weight** (the **weak-leap**
  fix — old rule called a weak one NCT); (3) **stepwise on one side only → metric weight decides** (appoggiatura that
  resolves by step → NCT even when strong; escape tone → weight). A genuine refinement found at build time: a tier-2
  "no stepwise connection" must mean **reached AND left by LEAP** (both neighbours present, both leaps) — an
  **isolated** note (no neighbour) is neither a step nor a leap and falls to metric weight, not auto-CT.
- **The plausibility fix (G3) — which tones it should test.** Step-0 found the as-built `implausibilityPenalty`
  "tests the wrong tones": it charges a candidate for the **extra** (non-template) structural notes it absorbs. Per
  spec, the plausibility check runs the candidate's **required (template)** tones through the same ladder: a template
  tone that behaves as a **Tier-1 embellishment** makes the candidate implausible (the spurious seventh of a triad,
  the passing `D` heard as `Cadd9`'s ninth). Step-0's own wording is decisive — the old penalty "catches 'strong
  extra ⇒ prefer richer chord' **one way**, but **cannot** catch 'the candidate's own 9th is really a passing
  tone'." → the fix **adds** the template-tone test; it does **not** remove the extra-note feedback (see §2, the
  margin lesson).
- **The inherit coupling.** G1's inherit was template-only (`notesConsistentWithPrevailing` ⇒ every focal pc is a
  template tone of prevailing). The membership ladder is exactly what its **stepwise-relaxation** needs: a focal note
  is consistent with prevailing if it is a template tone **or** classifies as an embellishment (NCT) of prevailing;
  a focal note that classifies as a **structural** extension of prevailing (a real foreign chord tone) is *not* an
  embellishment ⇒ inconsistent.
- **No structural change beyond the decoder** was required → no §1 STOP.

## §2 — BUILD G2/G3 (dormant — `chordslicedecoder.{h,cpp}`, production-dead)

All in `chordslicedecoder.{h,cpp}`; one `analyzeChord` cube, decision logic only. No second scorer; no new chord
type; no spelling pin.

- **G2 — three-tier ladder.** `isStepwiseTreated` (single bool) refactored into `stepwiseSignals` (per-side
  `stepIn`/`stepOut`/`leapIn`/`leapOut`/`suspension`) + a new `classifyTone` implementing the ordered ladder:
  Tier 1 (`suspension || (stepIn && stepOut)`) → NCT (`tier1Embellishing`); Tier 3 (`stepIn || stepOut`) →
  appoggiatura (`stepOut`) → NCT else escape → weight; Tier 2 (`leapIn && leapOut`) → CT-extension; fallthrough
  (isolated / single open side) → weight. `classifyMembership` calls `classifyTone` for every focal note.
- **G3 — plausibility on template tones.** In `classifyMembership`, a **required** tone is still labelled a chord
  tone of the chosen chord, but is run through the same ladder; a Tier-1-embellishing required tone adds its salience
  to `implausibilityPenalty` (the spec's "implausible chord tones"). The pre-existing **extra-note** structural
  feedback is **retained** (an extra note the chord can only absorb as an added 6th/9th charges the candidate — the
  richer-chord selection margin). The two contributions are the two directions of the chord-vs-membership decision.
- **Inherit relaxation.** `notesConsistentWithPrevailing` now takes the window + neighbour chords and uses
  `classifyTone`: a focal note is consistent with prevailing if it is a template tone **or** an embellishment (NCT)
  of it; a structural extension of prevailing ⇒ inconsistent. `applyCommitDecision` gained `window` + `prevChord` +
  `nextChord` params (threaded from `finalizeSlice`; an empty window degrades to the conservative template-only
  reading — preserves the Step-1 G1 unit tests).
- **Docs synced** (header build-state, `classifyMembership`/`applyCommitDecision`/`implausibilityPenalty` doc
  comments, the two membership preference comments).

**The margin lesson (a build-time correction, not inference tuning).** A first cut implemented G3 as a *replacement*
(test template tones only; an extra CT-extension is the added note, **un**charged — the literal reading of spec §5
step 1). That collapsed the per-slice **margin** over the default ±1 pooled window: with no extra-note feedback,
two complete chords over a pooled `{C,D,E,G,B}` score within ~0.13, every slice goes uncertain, and the first slice
abstaining starves the prevailing chain → **the whole `s1c_seg_changes` fixture (4 clean triads) named ZERO chords**
(unit test `Fixture_CompleteCandidateListSurfacedAndRanked` failed). Diagnosed at the score (a temporary debug
dump): confidence 0.11–0.14 everywhere. Re-reading Step-0's G3 note ("catches one way, but cannot catch …") confirms
the fix is to **add** the template-tone test, not remove the extra-note feedback — the extra-note penalty, computed
over the **focal** slice, is the membership→selection feedback that gives the focal-fitting chord its margin.
Restoring it fixed the fixture and is what is committed.

## §3 — RE-MEASURE (the assess checkpoint — accuracy AND coverage, before→after)

Same Step-1 harness: `--decode-chords` over the 353-stem corpus (Baroque + Default), graded held-out (TEST split),
dur-weighted = the granularity-comparable line. **BEFORE = G1** (`corpus_decode_chord_g1`); **AFTER = G2**
(`corpus_decode_chord_g2`). A third **isolation** variant (G2-iso) — ladder+plausibility ON but inherit reverted to
template-only (G1) — was decoded under a temporary one-line revert (rebuilt, then reverted) to attribute the change.
Graders: `cc_layer4_chord_baseline.py`, `cc_layer4_residual_decompose.py` (committed, unchanged). Decoder is
preset-identical Baroque≡Default (null-context vertical) so the chord axis is the same for both; Default Δ tracks
Baroque.

### Chord-root, dur-weighted, Baroque (TEST split)

| variant | among-committed | coverage (committed dur) | abstain | coverage-matched (reduced-to-region) |
|---|---|---|---|---|
| per-region **legacy** baseline | 73.8 % | (full) | — | 73.8 % |
| **G1 (before)** | **77.0 %** | 908 040 (47.0 %) | **53.0 %** | **66.9 %** |
| **G2-iso** (ladder+plausibility, template-only inherit) | **76.9 %** | 867 720 (45.0 %) | 55.0 % | **66.7 %** |
| **G2 (after — + inherit relaxation)** | **72.6 %** | 986 760 (51.1 %) | **48.9 %** | **64.8 %** |

- **Δ G1 → G2-iso (the ladder + plausibility alone):** among-committed −0.1 (77.0 → 76.9), coverage-matched −0.2
  (66.9 → 66.7), coverage −2.0 (the penalty re-ranking makes a few more slices uncertain). **Accuracy-neutral.**
- **Δ G2-iso → G2 (the inherit relaxation alone):** among-committed **−4.3** (76.9 → 72.6), coverage-matched
  **−1.9** (66.7 → 64.8), coverage **+6.1** (45.0 → 51.1). Of the +118 040 newly-committed ticks, only ≈+49 200 are
  correct (~42 %) and the full-duration **correct** ticks *fell* (1 288 080 → 1 251 480) — some previously-correct
  reads also flipped. **The relaxation is the sole regressor.**

### NCT membership (TEST split) — Baroque

| | NCT precision | NCT recall | CT precision | over-read |
|---|---|---|---|---|
| G1 (before) | 83.3 % | 4.7 % | 78.6 % | 22.2 % |
| G2 (after) | 60.2 % | 11.8 % | 79.5 % | 22.2 % |

The ladder catches **more** true NCTs (recall 4.7 → 11.8 %) but with lower precision (83.3 → 60.2 %) — ~40 % of its
NCT calls are actually chord tones. (These numbers are confounded by the different committed-slice denominators, so
they are read as direction, not a clean A/B.) The lower NCT precision is part of the over-inherit mechanism: a
foreign focal note wrongly called an "embellishment of prevailing" → wrongly consistent → inherit.

### Miss shape (Baroque, AFTER decompose)

Misses 678 → **943**; the increase is overwhelmingly **thin slices** (≤2 named chord tones) **45 → 300** and
**phantom roots** 147 → 270 — i.e. the inherit/commit targets the relaxation newly admitted. `wrong root (root∉GT)`
is the dominant bucket throughout (64 %).

### Default

Identical decoder output (preset-agnostic): G1 among-committed 77.0 % (+3.4 vs legacy 73.6), G2 72.6 % (−1.0). Same
direction and magnitude as Baroque.

## §4 — Gate (production byte-identity PASSED; new tests PASSED; build green)

- **Production byte-identical.** Baroque `.ours.json` **353/353 byte-identical** to the committed
  `tools/corpus/baroque` (fresh regen + `cmp`, 0 diffs); `pipeline_snapshot_tests` **11/11 zero-diff** (no goldens
  refreshed — live P1–P4 path unchanged); `composing 841/841`, `notation 53/53`. The decoder is referenced only by
  `batch_analyze --decode-chords` (returns before `analyzeScore`) + the unit tests — **not** on the live path. →
  corpus **53/24/53 unchanged** (Default/Jazz follow by the same production-dead, preset-agnostic argument). **No
  production movement.**
- **New unit tests** (`decode_chord_tests.cpp`, +7 — composing 834 → 841, all oracle-asserted): `Memb_Tier1_
  AccentedPassingToneIsNonChordTone` (accented passing → NCT regardless of weight), `Memb_Tier2_WeakLeapIsChordTone
  Extension` (weak arpeggiated leap → CT-extension), `Memb_Tier3_StrongAppoggiaturaIsNonChordTone`,
  `Memb_Tier3_EscapeToneDecidedByWeight` (weak→NCT / strong→CT), `Memb_G3_PlausibilityChargesImplausibleRequiredTone`
  (a required 7th behaving as a neighbour → charged; a genuine 7th → not), `Memb_G2_CVsCadd9Discriminator` (passing
  D → C; structural D → Cadd9), `G2_InheritsThroughStepwiseNct` (inherits with the window, abstains template-only).
  The two pre-existing membership tests whose penalty expectations the G3 framing touched were updated (the strong
  6th / weak leap are charged as the absorbed extension); the six G1 `applyCommitDecision` call sites were updated to
  the new signature (passing `focal` as window preserves their outcomes).
- **Build green** (only the two pre-existing `C4100` warnings).

## §5 — ASSESS (does the sequence hold? — NO → STOP)

- **Expected (plan §5):** membership correct per spec **AND** abstain rate drops materially **with among-committed
  accuracy holding** → proceed to Step 3.
- **Measured:** membership is correct per spec; the ladder+plausibility are **accuracy-neutral** (G2-iso); the
  inherit relaxation **dropped abstention** (53.0 → 48.9 %) **but regressed accuracy** (among-committed 76.9 → 72.6,
  coverage-matched 66.7 → 64.8). Accuracy did **not** hold. **→ FAILED assessment → STOP (plan §5/§7).** Not pushed
  to Step 3.
- **Diagnosis (the §5 "assess whether inherit needs more (Layer-5 territory?)" question, answered):** the regressor
  is precisely the inherit relaxation, isolated by the G2-iso A/B. The note-only inherit rule (spec §5 step 4) cannot
  separate a **continuation** of the prevailing chord from a **transition** to the next chord — both look like "a
  thin slice whose notes are stepwise embellishments of the prevailing chord." That separation is the next chord /
  function = **Architectural Layer 5**. A secondary contributor: the ladder's NCT precision (≈60 %) lets some foreign
  structural notes be mis-called embellishments of prevailing → wrongly consistent → inherit.
- **This is a SEQUENCE / SPEC question for Cowork (declared, not decided):** the spec's §5-step-4 inherit, as
  measured on the corpus, over-inherits. Candidate amendments (Cowork's call): (a) gate the inherit on **next-chord
  agreement** (Layer-5-aware — but that reaches past the note layer); (b) the **§15-O2 bounded-window joint
  resolution** (pick the chords+membership that best explain a few-slice window together); (c) a **tighter structural
  inherit condition** (e.g. require the slice's *strongest* note to be a template tone of prevailing, or cap the
  inherited run length); (d) keep G1's template-only inherit and let Layer 5 resolve the rest. The
  ladder+plausibility (accuracy-neutral) stand regardless.

## §6 — Deliver

- **Committed locally (unpushed):** `1b7fee1cd5` — `chordslicedecoder.{h,cpp}` + `decode_chord_tests.cpp` only
  (verifiable by sha; production byte-identical). The commit body records the FAILED assessment + STOP.
- This report (`cc_phase5b_step2_report.md`, gitignored).

## §7 — Stops honored
- A tier / plausibility fix needed no structural change beyond the decoder → no §1 STOP (the isolated-note Tier-2
  refinement is decoder-local).
- **No production movement** → no leak STOP (§4 byte-identical, 353/353 + snapshots 11/11).
- **Accuracy regressed** (the inherit relaxation) → **STOP honored: did NOT push to Step 3**; reported here +
  declared to Cowork as a sequence/spec amendment question. The build is committed; the sequence is paused.
- No `upstream` push; commit is local, unpushed; decoder + tests only.

## Artifacts (gitignored / untracked, under `scratch_artifacts/`)
- AFTER decode JSONs: `corpus_decode_chord_g2/{baroque,default}` (353/353 each); isolation: `corpus_decode_chord_g2iso/baroque`.
- Grading logs: `grade_g2_{before,after}.log`, `decompose_g2_{before,after}.log`, `grade_g2iso.log`, `decompose_g2iso.log`.
- Production byte-identity: `corpus_ours_check_g2/baroque` (regen) + 353/353 `cmp` match.
- Builds/tests: `build_g2b.log`, `g2_composing.log` (841), `g2_notation.log` (53), `g2_snap.log` (11/11).
