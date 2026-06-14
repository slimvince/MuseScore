# Back-Half Re-Grounding — the design for Stages 4–6, derived from measured evidence

> **Status: DRAFT — FOUNDATIONS VERIFIED, ready for user ratification
> (`cc_foundations_verification_report.md`, 2026-06-13).** The keystone was CONFIRMED at
> source (not corrected): the declared-mode drop is `addKey`'s fifths-only dedup at
> `importmusicxmlpass2.cpp:5978` (a *default-key-match*, not literally "0 fifths"); the
> mode is recoverable for **79/80** zero-sig stems → the 349 lever stands; bwv62.6 is the
> same mechanism (not a second path). Byte-identity of the dump instrument re-confirmed
> (0/353); "key→`basisIndep`" confirmed current post-3.3; music21 v9.9.1 already recorded.
> Four corrections folded in below (cross-corpus staleness reason; keystone precision;
> layer premise; the §11 erratum). The A-vs-B resolution (§3) STANDS on the verified
> keystone. Remaining qualifier (not a blocker, Stage-4-build confirm): the drop is in the
> **MusicXML-import path** — the 349 lever is solid for the all-`.xml` test corpus; its
> "user-facing" reading applies to MusicXML-imported scores (native `.mscz` load may not
> exhibit it — confirm at build). Replaces the
> decode-centric back half of the original (part-1) roadmap with a back half *derived*
> from this session's measurements, rather than amended fork-by-fork. Companion evidence:
> `cc_precision_headroom_dossier.md`, `cc_stage4_design_report.md`,
> `cc_key_emission_headroom_dossier.md`, `cc_stage3_2_design_report.md`. Roadmap
> META-PRINCIPLE block is the one-line version; this is the full derivation.
>
> *Written 2026-06-13 (Cowork). Base `f8c6b3932a` + instrument `a4ae4a9203`.*

---

## §1 — Why re-ground (the trigger)

The original roadmap's back half assumed precision lives behind the decoder (lattice,
beam, key-as-path, global search). Three design investigations this session each tested
a *structural* precision fix and each falsified it, for the **same** reason:

| Investigation | Structural fix tested | Result |
|---|---|---|
| 3.2 design | wider/global chord beam fixes Δ=+7a | NO — the transient wrong root is the genuine global optimum; search optimizes the objective the emission defines |
| Stage-4 design | HMM key path fixes the S2 bulk | NO — ~85% is Class-B, correct key not even rank-2; a path cannot recover an absent candidate |
| Headroom dossier | (measured the mass directly) | 95% of root errors are functional, not vertical; the music21 gate sees 4.8% |

**The convergent finding (META-PRINCIPLE):** inference *structure* (search / decode /
path / beam) cannot move an error the *emission model* consistently prefers. Precision
lives in **(a) the emission model** — the per-region/window scorer — **and (b) the
functional-labeling layer**. The decode machinery's value is *consolidation* (clean
oracle/competition factorization, single commit path, folded gates — all delivered),
not precision.

Continuing to amend a decode-centric plan ("beam shelved," "HMM deferred") is the
accumulating-amendment smell (ARCH §2.14). This document re-derives the back half from
the emission-centric truth.

## §2 — The hopeful corollary (what the key-emission probe added)

The meta-principle alone could read pessimistically ("the hand-built scorer is the
ceiling → we may need a learned model"). The key-emission headroom probe
(`cc_key_emission_headroom_dossier.md`) tested that directly and found the opposite on
the key axis: the Class-B bulk is **specific, structural, recoverable** —

- **349 regions:** the notated `<mode>` is *dropped at MuseScore import for empty key
  signatures* (`declaredModeOrdinal=-1` confirmed in the dump; the xml carries the mode).
  A data-plumbing bug — nothing to do with scorer quality.
- **a partial-signature subset:** the same dropped mode disables `partialSignatureCorrection`.
- **~127 regions:** a **notation-vs-analyst convention disagreement** — the resolver
  faithfully follows the notated key; the human annotator chose its relative as "the"
  tonic. This is arguably *correct behavior penalized by the metric*, not an error.

**The corollary:** the emission faults found so far are **specific identifiable causes
(a dropped tag, a too-hard penalty wall, a convention gap), not a fundamental ceiling.**
The hand-built emission has large, concrete, addressable headroom. The productive mode is
*scope-the-cause-then-fix*, which has now paid off three times.

**Keystone source-verified (foundations Task 1, Cowork-re-read).** The "dropped tag" is
`addKey`'s **fifths-only dedup** at `importmusicxmlpass2.cpp:5978`
(`if (oldkey != key.key() || key.custom() || key.isAtonal())` — the mode is read at
6074–6096 but the carrier `KeySig` element is suppressed when the new signature equals the
in-effect default). Precision: it is a **default-key-match** drop (only the piece-initial
empty signature hits it), *not* literally "0 fifths" — the fix must target the dedup, not
a `fifths==0` test. The mode is recoverable for **79/80** zero-sig stems (54 minor, 25
major); the lone exception bwv62.6 genuinely lacks `<mode>` in its source and was never in
the 349 set — it is the *same* mechanism, not a second path. The 349 lever is solid.

## §3 — The design-goals fork, resolved on the evidence: A (hand-built) confirmed; B (learned) NOT triggered, kept as the explicit fallback

The architecture step-back surfaced the real fork:

- **A — keep improving the hand-built rule-based emission** (better key handling,
  templates, features; fitted weights) + build the functional layer. Explainable, no
  training-data dependency, incremental, MuseScore-community-aligned. The path the whole
  project has taken.
- **B — replace the emission with a learned model** (AugmentedNet/ChordGNN/RNBert class,
  part-1 rec.5), decoded by the lattice already built. Higher published ceiling
  (~45–50%+ full-RN vs our 27.6% rn_agree), at the cost of explainability + a DCML
  training dependency.

**Resolution (on the key-axis evidence): A is confirmed; B is not triggered.** B's case
rests on the hand-built emission having a *fundamental ceiling*. The key-emission probe
found the opposite — the bulk is a plumbing bug + a design knob + a convention gap, all
addressable within A. There is no evidence the hand-built scorer *fundamentally cannot
distinguish* the cases; there is strong evidence it has specific recoverable faults.

**B is retained as the explicit fallback, with a concrete trigger:** if a future
*scope-the-cause* investigation of a major error slice finds it is **genuine ceiling**
(the scorer fundamentally cannot distinguish, even with structural fixes and fitting),
*that* is the signal to reconsider B for that slice — decoded by the substrate already
built (the §2.2 `IChordAnalyzer` interface makes it a drop-in). Until a measured ceiling
appears, A proceeds. **The one slice not yet decomposed structural-vs-ceiling is the
functional root-error mass (Stage 6's domain, §4) — its scoping is the next place B could
re-enter, and the part-1 view is that a functional *layer* (unbuilt) is the reachable
fix, not a learned model.**

> **OQ-1 RATIFIED 2026-06-14 — A confirmed, scoped to Bach (user decision).** The functional
> root-error mass — the one slice §3 left undecomposed — is now decomposed on the *corrected*
> metric (`cc_functional_residual_dossier.md`): the buggy parser had inflated the "functional"
> residual with 365 already-correct artifacts + 75 mis-attributed vertical cases; the cleaner
> 2153-region residual splits into rule-reachable + ambiguity/noise with an **empty
> needs-a-learned-model bucket (B2 = 0/44 sampled; corpus upper bound ~7%)**. music21's vertical
> RN analyzer fails the same functional roots (0/4) → it is a functional-*layer* problem (= A),
> not a vertical-scorer ceiling. So **A is confirmed on the functional axis too, B is not
> triggered.**
>
> **Explicit scope + re-check gate (the reason this is "scoped to Bach"):** the decomposition is
> **Bach WiR-rntxt only**. Per §3's own literature view, B's advantage is concentrated on harder,
> chromatic repertoire (Mozart/Chopin/Beethoven) — which was **not** decomposed (no `.music21.json`
> for the ABC sources). OQ-1 is therefore ratified A *for the Bach-calibrated pipeline* and remains
> **formally re-openable**: a **Stage-5/6 gate** must (a) decompose the non-Bach functional residual
> and (b) take a larger labeled sample (~100) + a lenient-alignment audit of DROOT_ABSENT (which
> currently inflates the ambiguity ceiling with S4 noise) before OQ-1 is closed in full. Stage 4
> (key path) is hand-built under *either* fork, so it proceeds now, unblocked. **Prerequisite: the
> corrected metric must be COMMITTED before any Stage-5 fitting** (else the fitter optimizes against
> the 365 phantom + 75 mislabeled cases).

## §4 — The re-grounded back half (derived order)

*(Cross-corpus note, foundations Task 2: the non-Bach "~2× harder" figure was confirmed
at HEAD by a fresh regen — root_err 50.7% / rn_agree 27.4% / 62110 regions. The
previously-cited June-3 figures rested on binary-output-stale `.ours.json` — NOT, as the
roadmap said, "pre-F1-metric stale" (the metric reproduces; the output had drifted). The
conclusion survives; the lesson is to regenerate, never quote the June-3 dirs.)*

Precision levers, sized (headroom dossier, % of matched Bach regions):
- **Stage 6 functional layer ~35–42%** — the largest; the rn_agree ceiling; S1
  tonicization (17.7%) is *root+global-key already correct, missing only the `V/V` label*
  — the best risk/reward in the whole map (pure-add label on correct readings).
- **Stage 4 key path ~20–24%** — now known to be ~34–44% of S2 *structurally* recoverable
  (the import fix), not a path problem.
- **Stage 5 emission/weight fitting ~1.3% direct** — but it is the *fitter* that tunes
  the edges/weights the other layers expose.
- **Search/decode ≈ 0** — deferred.

**Method, standing for every slice (the lesson that paid off thrice): scope the cause
before building.** Decompose the slice structural / fitted / ceiling (the key-emission
probe is the template); build the structural lever; route fitted to Stage 5; route
ceiling to accepted-ambiguity or flag it as a possible B-trigger. Derive, don't assert.

### The order

1. **Metric L0–L1 — DONE** (`f8c6b3932a`): the DCML-only, granularity-robust instrument.
   The back half is now measurable.
2. **Stage 4 — key emission, reshaped** (the next BUILD).
   > **◆ 4b-i LANDED + measured 2026-06-14 (HELD).** The −7 wall is removed (see `stage4b_design.md`
   > §2.7 + `cc_stage4b_i_report.md`): demoted to a 1.0 droppable hint, the piece-start anchor and the
   > hard declared-mode promotion deleted, and a `--ignore-declared-mode` floor toggle added.
   > **Measured both ways: demoting the wall is nearly free mode-present** (Default S2 685→687, gate
   > byte-identical 57/23/57) **but the no-crutch floor collapses ~3×** (Default S2 →2070). The
   > "~349 crutch upper bound" prediction is confirmed and sharpened: the crutch is almost entirely
   > **relative-pair disambiguation**, which is exactly what 4b-ii must move into note-based terms.
   > **★ REDIRECTED 2026-06-14 (user principle): infer mode/key from the MUSIC; the keysig tonal
   > mode is a LAST-RESORT HINT, never proof.** The keysig `<mode>` (major/minor/modal) sub-property
   > is being de-supported upstream (#9444 "hide the UI") and is absent/unreliable in most shipped
   > native scores — so the inferrer must NOT depend on it. The PRIMARY Stage-4 work is therefore a
   > **strong note-based major/minor inference** (tonal-centre + cadence evidence + scale-degree
   > salience, constrained by the *reliable* fifths). The declared mode is used ONLY as a low-weight
   > tiebreaker when the note-based inference is genuinely unsure — **so the −7 declared-mode wall is
   > REMOVED, not graded** (it treated declared mode as proof). The dossier's "~349 via restore+use
   > declared mode" is the CRUTCH upper bound = the size of the gap the note-based inference must
   > close on its own; it is NOT a shippable win to bank. Measure note-based-only (no declared-mode
   > crutch) or the metric overstates the shippable inferrer. (The import fix below is retained so
   > the hint is *available* when present + for corpus correctness + the #9444 repro — not as the
   > inference mechanism.)

   The pieces: declared-mode **import fix
   (target the `addKey:5978` default-key-match dedup, not a `fifths==0` test)** (makes the keysig
   mode available as the last-resort hint; also a corpus-correctness local patch) + **strong
   note-based mode inference** (the primary lever; declared mode a weak tiebreaker only) +
   **KeyArea spans** (the scaffold Stage 6 consumes) +
   hysteresis→path supersession. Gated as a behavior change (this ends the byte-identity
   era — resolved key feeds `analyzeChord`): the **57/23/57** gate identity sets (re-baselined
   2026-06-13; Baroque 57 / Jazz 23 / Default 57, see CLAUDE.md) + snapshots +
   DCML-adjudicate every movement, on the L1 rung. The HMM path stays deferred; the 127
   convention cases route to accepted ambiguity (revisited under the Stage-6 KeyArea label
   contract). **Layer note (foundations Task 5):** composing PUBLIC-links engraving
   (importexport/notation-agnostic), so the fix is layer-clean either way *provided the
   resolver gets the mode as a data value*; but both callers (notation bridge AND
   `batch_analyze`) lost the mode, so the mode-sourcing must be **shared, not bridge-local**
   — favor having engraving import RETAIN the mode (option b, true root cause; gate its
   render/export blast radius) over a per-caller re-parse (option a). **Build-confirm:**
   whether native `.mscz` load drops the mode too or only MusicXML import does (decides
   "user-facing" vs "MusicXML-import + corpus-measurement" framing of the 349).
3. **Stage 6 — functional layer, co-developed on KeyArea** (the largest lever): the
   tonicization/secondary labeler closes S1 (17.7%, consuming KeyArea to emit `V/V` not
   `II` — the comparator already credits it); then cadential-6-4 / suspension / applied
   labels for the functional root residual. **First a scope-the-cause investigation of
   the functional root mass** (structural-vs-ceiling, the key-emission template) — this is
   also the B-fallback check (§3). Measured class-by-class on the L2–L3 ladder via the
   co-ratified label-vocabulary contract.
4. **Stage 5 — the fitter, last:** fit the emission/transition/key weights against the
   DCML-only, granularity-robust objective on a held-out split (the residual prior
   balance, the relative-pair near-ties). Not before the edges to fit exist.

### Retained from the original roadmap (not discarded)
The consolidation is done and kept: the oracle/competition factorization, the single
commit path, the beam-1 decoder + decode cache, the folded/measured gates, the §2.2
ML-substitutability interface (which keeps B a drop-in). Nothing built is wasted; the
re-grounding changes *what we build next*, not what exists.

## §5 — Open questions for the ratifier

- **OQ-1 — ✅ RATIFIED 2026-06-14: A confirmed, scoped to Bach** (user decision; see the §3
  ratification block + `cc_functional_residual_dossier.md`). The functional residual decomposes
  with an empty B-trigger bucket on Bach; B retained as the fallback. **Re-openable at a Stage-5/6
  gate** that decomposes the non-Bach (Mozart/Chopin/Beethoven) functional residual + a larger
  sample + a DROOT_ABSENT alignment-noise audit. Stage 4 proceeds now (hand-built either way).
- **OQ-2 — Stage 4 before Stage 6, or interleave?** Stage 4's KeyArea is Stage 6's
  prerequisite (S1), so Stage 4 leads; but the label-vocabulary contract is co-designed.
  (Cowork rec: Stage 4 first, contract co-ratified during it.)
- **OQ-3 — the 127 convention cases:** accept as ambiguity (KeyArea carries "notated key ≠
  analytical key"), or pursue the risky structural override? (Cowork rec: accept; the
  override endangers the ~240 correctly-notated anchored stems.)
- **OQ-4 — declared-mode import fix location** (per key-emission §5.1): read the MusicXML
  `<mode>` in the bridge, or fix the engraving keysig import to retain `KeyMode` at 0
  fifths? A build-time decision for the Stage-4 instruction; flagged here as the one
  unverified root.

## §6 — What this does NOT change
- The working method (A–H) and trust model stand.
- The deferred items keep their triggers: beam (a non-monotone edge where global≠greedy
  and global matches DCML); joint segmentation (a granularity-robust metric — now exists,
  so its other blockers govern); B (a measured ceiling).
- decoder_design §11 Δ=+7a erratum + the other queued doc riders remain.

---

*DRAFT — awaiting user ratification. On ratification: fold the order into
`implementation_roadmap.md`, write the Stage-4 build instruction (the import fix + graded
prior + KeyArea), and queue the Stage-6 scope-the-cause investigation.*
