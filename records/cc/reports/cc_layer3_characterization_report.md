# CC — Layer 3 key/mode DECODER: characterization scaffold report

**Date:** 2026-06-22 (session 9h follow-up — the characterization increment)
**Status:** HELD / gitignored (`cc_*.md`), local-only — stays unpushed.
**Scope:** measurement only. NO production change, NOTHING wired, NO decoder tuning.
The only code change is the additive `--decode-keymode` serialization (the full ranked
`alternatives` array; confidence + `uncertain` were already emitted) + the four read-only
measurements added to `tools/cc_layer3_keymode_baseline.py` (`--characterize`). Production
analysis output is byte-identical (the diagnostic returns before `analyzeScore`; composing
596 / notation 57 / snapshots 11 all green and un-refreshed; `batch_analyze.cpp` is not
linked into the test suites; `.ours.json` uses the non-decode path).

This is a **gate, not a fix**: it tells us which of the decoder's remaining errors are
genuinely fixable *before* any sweep is attempted.

---

## 0. What was measured

All four sections grade the **existing** committed decoder (`c453315faa`) — the per-slice
key/mode sequence Viterbi — against the held-out **When-in-Rome** local-key ground truth, on
the **TEST split** (deterministic `md5(stem)%100 < 20`, out-of-sample), per preset. One
grading path: the same `our_key_tonic_fixed` extractor, `align_dcml_regions` aligner,
`_dcml_key_tonic` GT parser, and held-out split as the Increment-B harness — extended, not
forked.

**Anchor (Increment-B directional, reproduced this run, TEST split):**

| preset  | decoder unambiguous full-match | per-region baseline | Δ        | modulation top-1 (baseline→decoder, STATUS) |
|---------|--------------------------------|---------------------|----------|---------------------------------------------|
| Baroque | **84.3 %** (2933/3478)         | 87.3 % (1136/1301)  | −3.0 pts | 9.9 % → 31.2 % (+21.3)                       |
| Jazz    | **78.5 %** (2731/3478)         | 61.5 % (766/1245)   | +17.0 pts| 18.9 % → 30.8 % (+11.9)                      |

(The unambiguous bucket = stable ∧ two-parser-concur, ~56 % of scorable. The numbers below
operate on **all scorable** test-split regions — 6240 per preset — which is harder than the
unambiguous subset, hence lower absolute full-match.)

---

## §1a — Calibration (the core measurement)

**Do confidence (the sequence margin) and the `uncertain` flag track correctness?**

### Reliability curve — confidence bin → agreement-with-GT

| confidence bin | Baroque n | Baroque acc | Jazz n | Jazz acc |
|----------------|-----------|-------------|--------|----------|
| [0.0, 0.5)     | 323       | 41.5 %      | 455    | 42.9 %   |
| [0.5, 1.0)     | 308       | 47.4 %      | 397    | 43.1 %   |
| [1.0, 1.5)     | 264       | 51.9 %      | 323    | 43.3 %   |
| [1.5, 2.0)     | 290       | 53.1 %      | 333    | 55.0 %   |
| [2.0, 3.0)     | 450       | 50.9 %      | 596    | 50.3 %   |
| [3.0, 5.0)     | 795       | 54.1 %      | 1132   | 55.4 %   |
| [5.0, ∞)       | 3810      | 67.3 %      | 3004   | 65.5 %   |

**Verdict: calibrated and (weakly) monotone.** Low-confidence bins sit at ~41–43 %
agreement; the high-confidence bin (which holds ~50–60 % of the mass) is ~66–67 %. The
ordering is monotone except a single ~3-pt dip at the [2.0,3.0) bin in both presets (noise at
that bin size). The signal is real but **shallow** — even the bottom bin is ~42 %, not near
0 %; the decoder's margin separates "more likely right" from "less likely right", it does not
cleanly isolate a wrong set. This is the honest basis for the "honest about ambiguity" claim:
the confidence is informative but not a hard discriminator.

### Uncertainty precision / recall on the error set

| metric                                                              | Baroque | Jazz   |
|---------------------------------------------------------------------|---------|--------|
| **recall** — of WRONG slices, fraction flagged `uncertain`          | 14.4 %  | 18.3 % |
| **precision (strict)** — of `uncertain` slices, fraction WRONG      | 55.6 %  | 57.0 % |
| **precision (inclusive)** — of `uncertain`, fraction wrong **or** structurally-ambiguous¹ | 66.9 % | 74.2 % |

¹ structurally-ambiguous = the region is a modulation/tonicization seam (GT local≠global) **or**
the reading is the relative major/minor of GT — both computed from the **key GT alone**, no
chord/function evidence (in L3 scope).

**Verdict: the `uncertain` flag is conservative — high precision, low recall.** When it
fires, it is justified ~56 % (wrong) / ~67–74 % (wrong-or-ambiguous) of the time. But it only
catches ~14–18 % of the actual errors — most wrong slices are **not** flagged (they are
decided with high margin and are simply wrong). The current `uncertainThreshold = 1.0` is
therefore tuned for **precision over recall**: it under-claims uncertainty. **(Not changed —
moving the threshold is the later, separately-ratified sweep, §5.)**

### Alternative-recall

| metric                                                          | Baroque | Jazz   |
|-----------------------------------------------------------------|---------|--------|
| of WRONG slices, fraction where the TRUE key/mode is in the carried `alternatives` | **77.1 %** | **71.9 %** |

**Verdict: strong.** On ~72–77 % of the slices the decoder got wrong, the correct answer was
**carried in the alternatives** (it lost the argmax but survived in the lattice). This is the
single most actionable calibration result: a later re-ranking / gated step that consults the
carried alternatives has the right answer available ~3 times out of 4 — the error is a
**selection** failure, not a **coverage** failure, on the bulk of misses.

---

## §1b — Residual buckets (both presets)

Every **scorable miss** (decoder ≠ GT local) bucketed (priority order: relative-pair →
tonicization-boundary → modal-GT-representational → genuinely-wrong-resolvable → other):

| bucket                          | Baroque (of 2444 miss) | Jazz (of 2657 miss) | resolvable in L3? |
|---------------------------------|------------------------|---------------------|-------------------|
| relative-pair                   | 741 (30.3 %)           | 654 (24.6 %)        | partly — note-undecidable, needs the relative-pair tiebreak / declared-mode hint |
| tonicization-boundary           | 1209 (49.5 %)          | 1255 (47.2 %)       | **NO** — needs chord/cadence/function evidence (later layer) |
| modal-GT-representational (narrow²) | 1 (0.0 %)          | 1 (0.0 %)           | n/a — representational, not error |
| genuinely-wrong-resolvable      | 460 (18.8 %)           | 289 (10.9 %)        | **YES** — plain maj/min, stable, wrong → the actionable set |
| other (= tonic-displaced church-modal rotations³) | 33 (1.4 %) | 458 (17.2 %)        | mostly representational (defensible modal rotation, see §1c) |

² narrow modal-GT bucket = church-modal label ∧ tonic matches GT ∧ stable ∧ not-relative.
Only 1 case each — most modal misses are tonic-displaced (collection rotations), which land in
`other`, or sit in modulation regions, which land in tonicization-boundary.

³ by construction the `other` bucket is exactly *stable ∧ church-modal ∧ tonic-mismatch* — i.e.
modal **rotations** (same pitch collection, different chosen tonal center, e.g. `AMixolyd` vs
GT `Dmaj`). Jazz emits these heavily (the modal palette is enabled there); Baroque almost
never (it stays Ionian/Aeolian).

**structurally-undecidable (symmetric dim7 / whole-tone / augmented)** is **NOT separable from
the key GT alone** — identifying a symmetric sonority needs the slice's pitch/chord content,
which the decode JSON does not carry and which is out of L3-key scope (§5 stop, surfaced — it
belongs to a later chord/function layer). As a weak proxy, the uncertain-flagged share of the
genuinely-wrong + other buckets is 115 (Baroque) / 138 (Jazz) — a hint of how much of the
"resolvable" mass may in fact be the ambiguous floor, not a hard count.

---

## §1c — Modal-bucket audit (guard against excusing real errors as "modal")

For **every** miss where the decoder emitted a genuine church-mode label (Dor/Mix/Lyd/Phryg/
Loc…), classified by the slice's **actual pitch content** (from the corpus `*.xml`): does the
characteristic scale degree of the claimed mode appear, and is the contradicting (plain
major/minor) degree absent?

| preset  | church-modal misses | sampled | confirmed-defensible | actually-wrong | inconclusive⁴ |
|---------|---------------------|---------|----------------------|----------------|---------------|
| Baroque | 71                  | 71      | 21                   | **10**         | 40            |
| Jazz    | 895                 | 80      | 25                   | **8**          | 47            |

⁴ inconclusive = the single slice contains neither the distinguishing degree nor its
contradiction (small slice / few notes) — the modal reading is neither confirmed nor refuted
by that slice's notes in isolation (the decoder's coherence comes from the surrounding window,
not the slice alone).

**Verdict: the modal caveat is NOT broadly hiding real errors.** Of the slices where the notes
*are* distinguishing, confirmed-defensible outnumbers actually-wrong ~2:1 (Baroque 21:10) to
~3:1 (Jazz 25:8). Only ~8–10 of the sampled modal misses are *clearly* wrong (the notes
contradict the claimed mode). The large inconclusive share is honest — most modal misses are
collection rotations (e.g. `AMixolyd` = the 5th mode of `D major`), where the notes support
multiple modal centers and a single slice cannot decide. Jazz's large `other` bucket (§1b,
458) is dominated by exactly these defensible rotations.

---

## §1d — Granularity-robust metric (does the region-level win survive per-beat?)

Re-graded the decoder at the **quarter-note grid** (per-beat) vs per-slice, TEST split:

| preset  | region-level full-match | per-beat full-match | delta      |
|---------|-------------------------|---------------------|------------|
| Baroque | 60.8 % (3796/6240)      | 61.0 % (2452/4018)  | **+0.2 pts** |
| Jazz    | 57.4 % (3583/6240)      | 57.6 % (2316/4018)  | **+0.2 pts** |

**Verdict: the win survives — there is essentially no granularity penalty.** Unlike the CHORD
gate (≈7× harsher at section vs batch granularity), the key/mode metric is granularity-robust
here because the Layer-2 change-point slices are *already* near-beat-fine, so per-slice and
per-beat agree to within +0.2 pts. The modulation-region gains (STATUS: top-1 9.9%→31.2%
Baroque / 18.9%→30.8% Jazz) are read where a consumer would actually read the key, not an
artifact of coarse regions.

---

## §2 — Attribution of the residual (the §3 deliverable)

Mapping each preset's scorable-miss mass to its resolution path:

### Baroque (2444 misses, decoder unambiguous 84.3 %)
- **~7.4 % of scorable (460, "genuinely-wrong-resolvable") = the actionable L3 set.** Plain
  maj/min, stable region, wrong — these are what a later L3 sweep (threshold/cost tuning, or
  the carried-alternative re-rank, given the 77 % alternative-recall) can move.
- **~49 % of misses (tonicization-boundary) needs a later layer** (chord/cadence/function to
  decide tonicized-vs-real) — NOT fixable in key-only L3.
- **~30 % of misses (relative-pair) is note-undecidable** — the relative major/minor tiebreak
  (the decoder's declared-mode hint + change-cost) is the only L3 lever; residual is genuine.
- modal-GT / rotation mass is negligible (1.4 %) and largely representational.

### Jazz (2657 misses, decoder unambiguous 78.5 %)
- **~4.6 % of scorable (289, "genuinely-wrong-resolvable") = the actionable L3 set** —
  proportionally *smaller* than Baroque.
- **~47 % of misses (tonicization-boundary) needs a later layer** — same as Baroque.
- **~25 % (relative-pair) note-undecidable.**
- **~17 % (other = modal rotations) is largely modal-representational** (§1c: defensible ~3:1
  over actually-wrong) — the major/minor GT cannot credit a Mixolydian/Dorian center. This is
  the bulk of the "Jazz looks worse" gap and is **not a fixable error** so much as a
  GT-representation limit.

### Cross-cutting
- **Alternative-recall ~72–77 %** ⇒ the dominant error mode is **selection, not coverage**:
  the correct key is usually carried. The highest-leverage L3 improvement is a smarter
  *selection* among carried alternatives (a gated re-rank), not a wider lattice.
- **The `uncertain` flag is high-precision / low-recall** (catches only ~15–18 % of errors).
  If L3 is to "abstain honestly", recall must rise — that is a `uncertainThreshold` move,
  reserved for the ratified sweep.
- **structurally-undecidable (symmetric dim7 / whole-tone / aug)** could not be isolated from
  key GT alone — surfaced as out-of-L3-scope (needs the chord/function layer).

**Bottom line for the sweep decision:** of each preset's ~40 % all-scorable miss rate, only
~5–7 pts is genuinely-wrong-and-L3-resolvable; ~half is a later-layer (tonicization) problem;
~a quarter is note-undecidable relative-pair; and the Jazz-specific extra is mostly defensible
modal rotation. The biggest *L3* lever is the carried-alternative re-rank (77 % recall), not
threshold widening.

---

## §3 — Deliverables / files

- **Committed (scaffold):**
  - `tools/batch_analyze.cpp` — additive `alternatives` array in `--decode-keymode` (diagnostic-only).
  - `tools/cc_layer3_keymode_baseline.py` — `--characterize` mode (§1a–d), reusing the
    Increment-B grading path.
- **Local/gitignored (not pushed):** this report; `tools/corpus_decode/` (regenerated decode
  JSON, now carrying `alternatives`); `/tmp/charz.json` machine dump.

## §4 — Gate / constraint compliance
- No production change; nothing wired; composing 596 / notation 57 / snapshots 11 green,
  no golden refresh; decode path returns before `analyzeScore`.
- No decoder setting changed (topK / window / costs / `uncertainThreshold` untouched).
- One grading path (extended `cc_layer3_keymode_baseline.py`, no second metric).
- `upstream` never targeted; push is `origin`-only.
- structurally-undecidable / symmetric-sonority isolation surfaced as needing a later
  chord/function layer (out of L3-key scope) rather than fabricated.
