# CC Instruction — B2: build the SUBDOMINANT #4 guard (measure-first, byte-identical in production)

> **Ratified direction (Cowork rec, pending user): build the subdominant half of the #4 guard.** The B
> scoping (`cc_b_guard_scoping_dossier.md`, Cowork-verified at source) measured it **separable + convergent**
> (Bach modulation precision 47→51%, fixes mozart_k279 + bwv806_gigue) while the dominant half is unseparable
> (deferred — the calibration wall). Build ONLY the subdominant guard, measure-first. **HELD; no flip-ON;
> the wiring stays dormant.** Production must stay **byte-identical** (the guard feeds only the dormant
> decision + the diagnostic).

---

## §1 — What this is

Add a commit-time **subdominant guard** to `detectLocalModulations` so it stops committing the spurious
subdominant-of-anchor spans that the key-agnostic cadence detector produces (the structural I→IV misread,
B dossier §1). This raises the in-scope 4d-i modulation precision (+4pp measured) AND removes 2 of the 3
J-key-iii snapshot regressions. **Do NOT build a dominant guard** (measured anti-convergent — it removes
more genuine V-modulations than spurious ones; corelli stays unfixed, by design). **Do NOT flip the wiring
ON** (corelli's dominant regression remains; the flip stays gated).

## §2 — Scope + the byte-identity premise

`src/composing/analysis/section/localmodulationdetector.{h,cpp}` (the guard) + `tools/` (measurement). The
guard is byte-identical in PRODUCTION **iff** `detectLocalModulations` is reached only by the dormant
`decideJointKey` (flag-OFF) + the `--dump-modulation` diagnostic — **verify that at source first** (grep its
callers; confirm none is on the non-dormant production resolve path). If a non-dormant production caller
exists, STOP and surface (the byte-identity premise fails).

## §3 — The guard (B dossier §4)

At the span-commit block in `detectLocalModulations` (`localmodulationdetector.cpp:212-224`, **after**
`agreesWithAnchor` is computed — it has `result.anchor` + the span fields, key-agnostic, no resolved-key
dependency): **suppress** a span `S` (do not commit / do not emit as a key state) when:
- `S.agreesWithAnchor == false`, AND
- `S.tonicPc == (anchor.tonicPc + 5) mod 12` (mode-aware **subdominant-of-anchor**), AND
- the anchor is **confident**: `anchor.confidence ≥ 0.5` (provisional `[empirical — Stage-5 fits]`; mozart
  0.679 / bwv806 0.533 clear it; the gate avoids firing on low-confidence relative-pair-confused anchors).

**Dominant-seventh recall refinement (measure BOTH with and without):** only suppress when the span's
confirming cadence's dominant region does **NOT** carry the target's flat-7 (`pc (S.tonicPc+10) mod 12`) —
i.e. it is a *plain* I→IV, not a genuine V7→IV. The B dossier §3.5 hypothesizes this recovers most of the
−2.3pp recall; **measure it at build** (the seventh is computable from the region `pcMask`). Report the
guard's effect **with** and **without** the refinement so the recall recovery is quantified.

## §4 — Measure (all three presets where applicable)

1. **4d-i modulation precision/recall** (`cc_b_guard_separability.py` / the modulation measure): confirm the
   relationship-only guard hits **~47→51% precision, ~−2.3pp recall**, and report the refinement's recall
   recovery. A precision result materially below the measured +4pp ⇒ STOP (the prediction didn't hold).
2. **The 3 snapshot regressions** (flag-ON, bridge path): **mozart_k279 + bwv806_gigue cleared**; corelli
   still regresses (dominant — expected, not addressed here). Re-adjudicate the flag-ON snapshot gate: 2/3
   cleared.
3. **Production byte-identity (flag-OFF):** `.ours.json` 0-diff on all 3 presets vs the committed `5fee657578`
   baseline; **BIR 57/23/57**; suites composing/notation/snapshots green, goldens unchanged. (The guard
   changes only the dormant path ⇒ this must hold; if it doesn't, the guard leaked into production — STOP.)

## §5 — Deliver: HELD + report

`cc_b2_subdominant_guard_report.md` (gitignored, HELD, no commit): the byte-identity confirmation, the
precision/recall with+without the refinement, the snapshot re-adjudication (2/3), and the explicit standing
note that **the global flip-ON remains gated on corelli's dominant case** (the calibration wall) → the wiring
stays dormant; the flip decision (scope / hold / fold into calibration) returns after this. Cowork verifies
at source; user ratifies the commit (this IS a real source change to `localmodulationdetector`, though
byte-identical in production — commit only on a clean measurement, like the gate-policy changes).

## §6 — Stop conditions
- A non-dormant production caller of `detectLocalModulations` exists (byte-identity premise fails) → STOP.
- Production not byte-identical flag-OFF (`.ours.json` / BIR / snapshot moves) → STOP (the guard leaked).
- The measured precision gain is materially below +4pp, or recall loss materially worse than −2.3pp even
  with the refinement → STOP, surface (the measured prediction didn't transfer).
- Building a dominant guard / flipping the wiring ON / scoping by repertoire → STOP (out of scope here).
- Any edit outside `src/composing/analysis/section/localmodulationdetector.*` + `tools/` → STOP.
