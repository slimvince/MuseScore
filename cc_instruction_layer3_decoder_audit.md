# CC Instruction — ARCHITECTURAL LAYER 3 (key/mode) decoder: READ-ONLY pre-build audit

> Architectural Layer 3 (key/mode) is **signed** (`cowork_layer3_keymode_design.md` — read it first; it is the spec).
> Before any decoder code, do the **read-only pre-build audit**: confirm the as-is at source, pin the wiring and the
> deferred numbers, confirm the grading harness is ready, and specify the decoder test fixtures. **READ-ONLY — no
> production code, no behavior change, no production commit.** Output a dossier; Cowork verifies the citations; user
> ratifies; THEN code.
>
> **★ Build on the prior work, do not redo it:** the earlier Layer-3 read-only audit (`cc_layer3_keymode_audit_dossier.md`)
> already verified the as-is key resolver, the R1/R2/R3 scope items, and produced the held-out baseline; the
> Increment-B harness (`tools/cc_layer3_keymode_baseline.py`, pushed) already measures the direct key/mode metric.
> This audit **extends** those to the things the decoder rebuild specifically needs. Cite both where you rely on them.
>
> **★ Context you do NOT have:** Architectural Layer 3 decides **key/mode only**, as one coherent sequence over the
> Architectural-Layer-2 slices, evidence = notes only (no chord/function/cadence). The decoder = a Viterbi best-
> sequence over key/mode states; emission = the existing `KeyModeAnalyzer`; change cost = stay-cheap + key-distance
> + a large relative-pair penalty; output per slice = chosen key/mode + ranked alternatives + a sequence-margin
> confidence + an "uncertain" mark. **No-assume:** every as-is statement cites `file:line`; mark `[unverified]` where
> not confirmable, do not guess.

## §1 — Confirm/extend the as-is at source (the pieces the decoder reuses or replaces)
1. **The region-analyzer call site to be replaced** — the exact `file:line` where `regionanalyzer` calls
   `resolveKeyAndModeRanked` (the per-region key/mode argmax), what it passes in, and **what downstream consumes the
   per-region key result** (so the per-slice decoder can supply the same to those consumers). This is the wiring seam.
2. **The emission scorer (`KeyModeAnalyzer::analyzeKeyMode`) for per-slice reuse** — confirm its inputs (the
   pitch-context window it scores over) and outputs (the per-candidate scores over the 12 tonics × 21 modes, plus
   the confidence). Confirm it is callable per slice over a small window built from the Architectural-Layer-1 note
   model, unchanged. List the 21 modes it scores (cross-check against the layer doc §1 vocabulary).
3. **The preset → mode-prior path** — confirm how the user style preset (Standard / Baroque / Jazz) reaches the 21
   `modePrior…` values (the bridge override of the scorer's preferences). This is where the preset first enters
   (layer doc §2); the decoder must keep using it. `[verify]` the override path `file:line`.
4. **Today's hysteresis and look-back/look-ahead values** — read the current resolver's anti-flip margin(s)
   (`hysteresisMargin`, `relativeKeyHysteresisMargin`) and its fixed look-back / dynamic look-ahead settings
   (`LOOKBACK_BEATS`, `dynamicLookahead…`). These are the **starting values** for the decoder's change-cost
   magnitudes and emission-window size — report the exact current numbers.
5. **Dependency check (key/mode uses notes only):** confirm the emission evidence is pitch content + emphasis, with
   **no** chord/function/cadence input feeding the key/mode decision (so the signed dependency order holds). Flag any
   coupling.

## §2 — Pin the decoder specifics (numbers + shape, for the impl — verify feasibility, do not build)
- **A dedicated key-path (Viterbi) decoder** — confirm `ChordPathDecoder` is chord-specific and not reusable (prior
  audit said so; re-confirm `file:line`), so a dedicated decoder is needed; sketch its state = the per-slice pruned
  candidate set ∪ the running key.
- **Pruning count K** — propose a starting K (the layer doc lists "a short list of best candidates ∪ the current
  key"); state what K keeps the relative-pair and plausible-modulation candidates alive without bloating the lattice.
- **Change-cost shape + starting magnitudes** — stay = 0; switch = base penalty (from §1.4's hysteresis values) +
  key-distance (circle-of-fifths) + a large relative-major/minor penalty (from `relativeKeyHysteresisMargin`).
  Report the concrete starting numbers.
- **Emission-window size** — propose the small per-slice window (from §1.4's look-back/look-ahead), noting the path's
  change cost now carries the long-range coherence the old big look-back faked.
- **Confidence (sequence margin) + the "uncertain" threshold** — confirm the margin (best sequence vs best
  different-key sequence at a slice) is computable from the Viterbi table; propose a starting threshold.
- **Reach-back (R3)** — confirm the demand→supply protocol: how Architectural Layer 3 detects an unsettled opening
  and calls Architectural Layer 1's "widen the span earlier in time" operation; propose the backward cap + stop
  criterion (extend until the prevailing earlier key is established).
- **Incremental re-decode (R2)** — confirm a sub-range re-decode with the two boundary key/modes pinned is feasible
  in the Viterbi formulation.

## §3 — Grading readiness
- Confirm the Increment-B held-out ground-truth harness is ready to grade the decoder: the direct key/mode-vs-RN
  metric, the held-out split, and the baseline (~87% Baroque / ~61% Jazz) it must beat **directionally** (genuine
  rotation/relative-pair errors down). Restate the **modal-vs-major/minor-GT caveat** (do not optimise away
  defensible modal readings the major/minor ground truth cannot represent).
- Confirm the safety net: the oracle-root KEY tier on both presets (a worse number on either preset is a STOP).

## §4 — The snapshot-golden surface
Identify which pinned analysis snapshots (`pipeline_snapshot_tests`) will change when the per-slice decoder replaces
the per-region argmax — i.e. the surface that must be refreshed *after* the change is verified correct. (Do not
refresh anything in this read-only audit; just enumerate what will move.)

## §5 — Specify the deterministic decoder test fixtures (the impl's coverage spec)
Specify (author later, in the impl) the deterministic decoder fixtures, each with the expected per-slice key/mode:
a single-key passage → one key; a relative-major/minor near-tie with a whole-stretch tilt → the correct one,
consistently, with low confidence at the seam; a brief tonicization → key unchanged; a sustained, cadence-less
modulation → key changes; a near-vs-remote switch with equal local evidence → the near key; a selection beginning
mid-passage → forces reach-back. Also the property tests: sub-range re-decode == the matching slice of a full
decode; determinism.

## §6 — Deliver
Write `cc_layer3_decoder_audit_dossier.md`: the §1 as-is map (file:line + the exact current numbers for hysteresis /
look-back / look-ahead / mode-prior path), the §2 decoder pins (with concrete starting magnitudes), the §3 grading
readiness, the §4 snapshot surface, and the §5 fixture spec. **No production code.** Cowork verifies the citations
and that nothing production changed; user ratifies; then the decoder is implemented.

## §7 — Stop conditions
- Any production / behavior / scoring change, or a probe that alters analysis output → STOP (read-only).
- An as-is item cannot be confirmed at source → mark `[unverified]`, do not guess.
- The decoder design would require building the gated joint key-and-chord step to work → STOP (out of scope; Layer 3
  is bounded and leaves the residual flagged for that later step).
- The key/mode evidence turns out to be coupled to chord/function/cadence in the current code in a way the rebuild
  cannot cleanly sever → STOP and surface (it would threaten the signed dependency order).
