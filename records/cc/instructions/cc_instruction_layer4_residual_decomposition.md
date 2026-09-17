# CC Instruction — Layer 4 Increment B: decompose the −15.4 chord-root residual (read-only) — gates Increment C

> Knowledge-based, not assumption-based: the fair-key test ruled out the key handicap (≈0% recovery). The −15.4
> chord-root residual (per-slice 58.4 vs per-region 73.8) is now split between **spelling-fixable** (the Increment-C
> spelling-pin target) and **per-slice-vs-per-region granularity** — unknown proportions. **Measure the split before
> any Increment-C code.** This is read-only / decode-only; no production change, no wiring, no C code. The verdict
> gates whether C proceeds.

## §1 — Decompose every chord-root MISS into three buckets (held-out TEST, both presets)
Over the Increment-B per-slice decoder output (the existing `--decode-chords`), bucket each miss (decoder root ≠ GT
root):

- **(a) Granularity — the decisive sub-test.** Reduce the per-slice chords to **region grain** (the duration-majority
  chord per region — the *same* reduction the L3 wiring used for key) and re-grade against the per-region baseline,
  same grader, both presets. Report **per-slice-reduced-to-region** chord-root.
  - If ≈ **73.8 / 73.7** → the per-slice *readings* are already as good as per-region; the −15.4 is a fine-grain
    measurement effect (per-slice graded at a harsher grain), not a real deficit.
  - If still well below → per-slice genuinely sees **less** than per-region at the same grain (the window is not
    gathering the chord's notes). Size that gap — it is the real concern.
- **(b) Spelling-fixable.** Misses where the decoder root and the GT root are the **same notes, different
  rotation/relative** — a symmetric dim7 rotation, or a relative-major/minor / share-tone pair — exactly what the
  Increment-C **notated-spelling root pin** would fix. Report the % of the residual, and **verify a sample at the
  score** (confirm the notes' spelling pins the GT root).
- **(c) Genuinely-wrong.** The remainder — misses that are neither a granularity effect nor a spelling-fixable
  rotation (wrong notes→chord, missed membership, an incomplete-slice misread the window should have caught).
  Characterize the top types.

## §2 — The verdict (gates Increment C)
State plainly, per preset: per-slice (slice grain) 58.4 → **per-slice-reduced-to-region** → per-region 73.8 (the
granularity size); the **spelling-fixable %**; the **genuinely-wrong %** + its top types. Then:
- **If** per-slice-reduced-to-region ≈ per-region **and** the residual is mostly spelling-fixable → the per-slice
  thesis holds, the spelling-pin is the remaining lever → **proceed to Increment C.**
- **If** per-slice-reduced is still well below per-region **or** the genuinely-wrong bucket is large → **STOP and
  surface.** Per-slice has a deeper gap (most likely the window not gathering the chord's notes) that the spelling-pin
  will *not* fix — that gets investigated and fixed before C.

## §3 — Constraints
- **Read-only / decode-only.** No production change, no wiring, **no Increment-C code**. One grading path (reuse the
  existing grader + the music21 GT roots/chord-tones). The decomposition tooling may stay **local (uncommitted)**, like
  the fair-key / tpc measurements. `upstream` untouched.
- If a bucket needs the spelling-pin or function evidence to *compute* (versus to *fix*), record it as that bucket —
  do not build the fix.

## §4 — Deliverable
`cc_layer4_residual_decomposition_report.md` (held/gitignored): the §1 three-bucket split per preset (with the
per-slice-reduced-to-region number), the score-verified spelling-fixable sample, the genuinely-wrong top types, and the
§2 verdict.

## §5 — Stop conditions
- Any production output moves, or the decoder lands on a live path → STOP (read-only).
- You start writing Increment-C spelling-pin logic → STOP (that is gated on this verdict).
- A push would target `upstream` → STOP.
