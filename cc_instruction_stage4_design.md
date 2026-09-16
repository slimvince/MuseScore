# CC Instruction: Stage 4 design — key as a path (design-only, ratification-gated)

## Context

Stage 4 leads the re-grounded back half: it directly addresses S2 (genuine key error,
10.2%, the `key_disagree ≠global` half) AND produces the **KeyArea spans** that Stage 6's
tonicization labeler needs to close S1 (17.7%, the biggest slice). It is decoder-
independent and measurable immediately on the L1 `--key-breakdown` rung just built.

**Design-only, ratification-gated** (decoder-design treatment): produces
`docs/key_path_design.md`, no production code, probes allowed (uncommitted) to ground
claims. Base `f8c6b3932a`. Method A–H; **HELD means `git add` ok, `git commit` NOT**
(handoff convention, now unambiguous). Ratification arrives as an addendum file.

Mandatory reads: `cowork_target_architecture_review.md` rec.2 (key-as-HMM-path, the
part-1 target); `cc_precision_headroom_dossier.md` §1.5 (the S1/S2 split, the 39.9%
localkey≠globalkey fact, the relative-major/minor + partial-signature error pattern);
`docs/precision_metric_design.md` §3.2 L1 (how Stage 4 is measured) + the
tonicization-vs-modulation contract row (§3.1); ARCHITECTURE.md §4.2 (the existing
`KeyModeAnalyzer`: 252 candidates, the scoring helpers) + §5.2 (the bridge key
resolution, piece-start shortcut); `keyresolver.cpp` / `keymodeanalyzer.{h,cpp}` (what
exists — `resolveKeyAndModeRanked`, `promoteWinnerInPlace`, the partial-signature fix
`81978321e3`); the Stage-1c keyresolver pins (`regionanalysis_tests.cpp` — incl. the
`promoteWinnerInPlace` confidence-wart pin, the Stage-4 rebaseline anchor); redesign_plan
"Step 3 — Key-as-distribution ⛔ SHELVED" (the prior attempt + why it shelved).

## The design document must cover (section per item)

1. **Scope + what S2 actually is.** The measured target: S2 = 1032 regions (10.2%) where
   our global key ≠ DCML global — dominated by relative major↔minor confusion and the
   partial-signature pattern (dossier §1.5/S2, sampled). State what Stage 4 fixes (S2)
   vs what it ENABLES but doesn't itself fix (S1 tonicization — needs Stage 6 consuming
   KeyArea). And what it must not regress (the `81978321e3` partial-signature fix, the
   Corelli C-minor detection it already gets right).

2. **Key-as-a-path — the HMM, concretely.** Per part-1 rec.2: states = (tonic × mode)
   candidates; emissions = the EXISTING `KeyModeAnalyzer` per-window scores (252
   candidates — reuse, don't rebuild the scorer); transitions = a modulation penalty by
   circle-of-fifths distance (relative/parallel/closely-related cheaper than distant).
   Decode (Viterbi) over the score's windows → a key PATH, not per-window argmax.
   Spell out: the window/observation unit, how the 252 emission scores feed the HMM,
   the transition-penalty parameterization (and that its weights are Stage-5-fitted, not
   hand-tuned — design the structure, defer the numbers).

3. **Why the path beats per-window argmax on S2 — derived, not asserted.** The dossier
   says relative major↔minor is the dominant S2 error. Walk it: a per-window scorer
   flips a↔C at local evidence; a path with a modulation penalty resists the flip
   (staying in the established key is cheaper than a spurious relative-key hop). Probe
   2–3 actual S2 cases (e.g. the bwv16.6/420 a↔C, bwv244.54/343 d↔F from the dossier)
   for the per-window score margins, and show whether a circle-of-fifths transition
   penalty of plausible magnitude would hold the correct key. **If the margins show the
   path would NOT fix them (the evidence genuinely favors the wrong key locally), say so**
   — that's a finding (it would mean S2 needs richer emission, not just a path), exactly
   as the Δ=+7a derivation was.

4. **KeyArea spans — the first-class output Stage 6 consumes.** Define the `KeyArea`
   structure (span = contiguous same-key region; tonic, mode, start/end tick,
   confidence). This is what `unified_analysis_pipeline.md` wanted and what the
   tonicization labeler (S1) reads to decide `V/V` vs local-key `V`. Spell the interface:
   how a region inside a KeyArea but tonicizing a secondary is distinguished from a
   genuine local-key modulation — **the tonicization-vs-modulation boundary** (metric
   contract §3.1 row; this is where Stage 4.2 meets Stage 6, stub the interface).

5. **Relationship to the existing key machinery (reuse map).** `resolveKeyAndModeRanked`
   already returns a ranked distribution (the redesign_plan noted the ranked list is
   discarded at `.front()`). The HMM consumes that distribution as emissions instead of
   discarding it. `promoteWinnerInPlace`'s hysteresis (the Stage-1c confidence wart —
   re-ranks without recomputing confidence) is SUPERSEDED by the path (the decode is the
   principled hysteresis). State what's reused (the 252-candidate scorer, the
   partial-signature fix folded into emissions), what's replaced (per-window argmax +
   promoteWinnerInPlace), what's removed.

6. **The Step-3 "key-as-distribution shelved" reconciliation.** redesign_plan shelved
   key-as-distribution because the motivating Corelli case turned out to be a
   signature-lock bug (fixed) and "no live case showed the correct key at rank 1/2."
   The headroom dossier now PROVIDES live cases (S2 = 1032 of them, measured). State why
   Stage 4 is no longer premature: it's not "distribution for its own sake," it's an
   HMM path motivated by 1032 measured relative/partial-signature errors, measurable on
   the L1 rung. Address whether the prior shelving evidence (normalizedConfidence
   unreliable) affects the HMM (it shouldn't — the decode uses raw emission scores, not
   the sigmoid confidence).

7. **Measurement plan (on the L1 rung).** How success is measured: `--key-breakdown`
   S2 (`≠global`) shrinking, with no S1 regression and no `81978321e3` regression;
   DCML-only, the granularity-robust unit; both the Bach gate (`--wir-bach`) and the
   non-Bach corpora (where key error is ~2× harder — dossier §1.4). Expected-direction
   table per case class (relative-key, partial-signature, genuine modulation).

8. **Single-commit-path / config / cost.** The key path must serve all consumers
   (batch + the bridge/P3 + the decoder's emission `snapshot.keyTonicPc/scale`) through
   one path (no new parallel key logic — the Stage-2 "one pipeline one truth" principle).
   Config-agnostic (prefs in). The decode-once cache (3.1b) interaction. Per-window cost.

9. **Migration sequencing → roadmap; risks; rollback.** Sub-steps; the riskiest
   assumption (the §3 derivation — does the path actually fix S2?); flag-vs-in-place;
   how a key change ripples into chord emission (key feeds `basisIndep` — a key change
   IS a behavior change on the chord axis too, so the byte-identity story ends here:
   Stage 4 is the second intentional behavior change, gated like 3.2 would have been —
   measured, DCML-adjudicated, ratified, with the chord-axis side effects measured too).

10. **§Open Questions for Cowork/user** — genuine forks (e.g. if §3 shows the path
    underperforms on partial-signature vs relative-key; the KeyArea/tonicization
    interface granularity; whether Stage 4 and the Stage-6 contract must co-ratify).

## Report — `cc_stage4_design_report.md`

§1 probes + the §3 S2 derivation (the load-bearing part — real margins); §2 section map
+ the three most load-bearing claims w/ evidence; §3 Open Questions inline; §4 unknowns.
Design doc uncommitted until ratification.

Stop conditions: the §3 derivation showing the path does NOT fix S2 (report — it
reshapes Stage 4's value the way the beam finding reshaped 3.2); a reuse assumption about
`KeyModeAnalyzer`/`resolveKeyAndModeRanked` proving false on read (report — changes the
build/reuse split); scope creep into Stage-6 functional labeling beyond the KeyArea
interface stub; into Stage-5 weight numbers beyond the transition STRUCTURE.
