# CC Report — B2: SUBDOMINANT #4 guard — BUILT + MEASURED (HELD, no commit)

> **HELD — gitignored (`cc_*.md`), NO commit. Source changed in the working tree only.** The B2 instruction
> said: build the subdominant half of the #4 guard, measure-first, byte-identical in production, expect
> the in-scope 4d-i precision +4pp AND 2 of 3 J-key-iii snapshot regressions cleared.
>
> **Date:** 2026-06-16. Base `5fee657578`. Surface: `tools/corpus/default_mod_b2` (Default, WiR-Bach,
> 326/353 covered) + the 3 snapshot scores (bridge path) + the 3 production presets. New/changed code:
> `src/composing/analysis/section/localmodulationdetector.{h,cpp}` (the guard) + `tools/batch_analyze.cpp`
> (dump enrichment) + `tools/cc_b2_subdominant_guard_measure.py` (read-only measurement).

---

## 0. Headline — a SPLIT result, surfaced for ratification

| deliverable | result |
|---|---|
| **§4.3 Production byte-identity (flag-OFF)** | ✅ **CONFIRMED.** `.ours.json` **0-diff** on all 3 presets (353 each) vs baseline; **BIR 57/23/57**; suites composing 545 / notation 57 / snapshot 11 green, goldens unchanged. |
| **§4.1 Full-score 4d-i precision** | ✅ **+4.0pp TRANSFERS** (relationship-only 47.0→51.0%, −2.3pp recall, reproduces the dossier exactly). The **production conf-gated** guard is milder: **+1.8pp / −0.4pp**. |
| **§4.2 Snapshot fix (bridge path)** | ❌ **DOES NOT TRANSFER. 0 of 3 cleared (not 2/3).** mozart F + bwv806 D remain; corelli is even *false-suppressed* in some windows. |
| **§3.5 dominant-7th refinement** | ❌ **BUILT, MEASURED, REJECTED** — it backfires (a tonicized IV carries an applied V7), and the instruction's literal `(tonic+10)` formula is empirically null. Production guard = conf-gated, **no refinement**. |

**One-line answer.** The subdominant guard is correct and precision-positive *on the full-score region
frame the dossier measured* (+4pp relationship-only, +1.8pp conf-gated, byte-identical in production), **but
it does NOT clear the snapshot regressions**, because the bridge/notation path analyses a **16-measure
window whose key-agnostic cadence anchor is unstable / mis-resolved** — and the guard is **downstream of the
anchor**. When the bridge anchor mis-resolves to the subdominant itself (mozart → F), the over-commit span
becomes the apparent *home* and the guard correctly leaves it; when it mis-resolves to the dominant (corelli
→ Gm), the guard *false-suppresses the true home*. The dossier's 2/3 prediction was derived from the **stable
full-score** anchor (C 0.679 / A 0.533); it does not hold on the windowed bridge anchor. **The real blocker
is bridge-path anchor stability, upstream of the guard.** Surfaced, no commit.

---

## 1. Byte-identity premise — verified at source (instruction §2, §6 stop) `[code]`

The only callers of `detectLocalModulations`:
- `tools/batch_analyze.cpp:1018` — the read-only `--dump-modulation` diagnostic.
- `src/composing/analysis/section/jointkeydecision.cpp:197` — inside `decideJointKey`, which in production is
  reached **only** via `region::applyJointKeyWiring` ([regionanalyzer.cpp:1150-1151](src/composing/analysis/region/regionanalyzer.cpp#L1150-L1151)),
  **gated on `jointKeyWiringEnabled()` (default OFF, env `MUSE_JOINT_KEY_WIRING`)**. `sectionanalyzer.cpp:94`
  also only *inerts* Layer-B when the flag is on; it does not call the detector.
- the unit tests.

**No non-dormant production caller exists** → the byte-identity premise holds. Confirmed empirically in §5.

---

## 2. The guard as built + two surfaced design decisions

### 2.1 The guard (`localmodulationdetector.cpp`, commit block)
A commit-time filter after `agreesWithAnchor` is computed. A span `S` is **suppressed** (not committed) iff:
- `jointKeyWiringEnabled()` **(the gating decision — §2.2)**, AND
- `S.subdominantOfAnchor` = `anchor.detected && !S.agreesWithAnchor && S.tonicPc == (anchor.tonicPc+5) mod 12`, AND
- `anchor.confidence >= 0.5` (`kSubdominantGuardAnchorConfidenceFloor`, provisional `[empirical — Stage-5]`).

Three diagnostic fields are computed for **every** candidate span and emitted by `--dump-modulation`:
`subdominantOfAnchor`, `dominantSeventhPresent` (the V7 marker, pc `tonic+5`), `targetFlat7Present` (the
instruction-literal `tonic+10`). They do **not** gate suppression (the refinement was rejected — §4).

### 2.2 SURFACED DECISION #1 — the guard is gated on `jointKeyWiringEnabled()`, not unconditional
The instruction §3 describes an **unconditional** commit-time suppression. That is **infeasible in scope**: an
unconditional guard changes `detectLocalModulations`'s 2-arg output, which **breaks `composing_tests`**
(`localmodulationdetector_tests.HomeAndModulationSpansTagged`). In that synthetic test the key-agnostic anchor
resolves to **G major (conf 0.625)** via the chromatic-leading-tone weighting, so the C-major span becomes
`subdominant-of-anchor` (C = G+5) and an unconditional guard would suppress it → 1 span, but the test asserts
2. **§6 forbids editing the test** (outside `localmodulationdetector.*` + `tools/`), and the 2-arg signature
is shared by the test and by `decideJointKey`, so no default value satisfies both.

**Resolution:** gate suppression on `jointKeyWiringEnabled()`. This is also *semantically correct* — the
modulation spans only affect production when the wiring is live, so the guard activates exactly when the spans
become live. Result: **all unit tests stay green** (flag-off ⇒ unguarded), **production byte-identical**
(flag-off ⇒ uncalled *and* unguarded), the guard is active on the dormant flag-ON path (where the snapshot
regressions live), and the flag-off `--dump-modulation` diagnostic still emits the full unguarded span set
(with the decision fields) for measurement. *This is a deviation from the literal "unconditional" spec, required
to keep the suite green without touching the test — flagged for ratification.*

### 2.3 SURFACED DECISION #2 — the §3.5 flat-7 formula is musically wrong as written
The instruction parenthesises the refinement pc as `(S.tonicPc+10) mod 12` ("the target's flat-7"). For target
F that is E♭ — but the instruction's own example "**C7→F needs B♭**" is B♭ = `(tonicPc+5) mod 12` (the
*dominant's* minor seventh, the V7 marker). A genuine V7-of-F (C7) carries B♭, never E♭, so the literal
`tonic+10` formula can never fire. I implemented **both** as diagnostic fields and measured them: the literal
`targetFlat7Present` is set on **0** of 86 subdominant spans (confirming it is the wrong pc), while the V7
marker `dominantSeventhPresent` behaves as the §3.5 intent. *Moot in the end because the refinement is rejected
(§4), but flagged: the spec formula and its example disagree.*

---

## 3. §4.1 — full-score 4d-i region precision/recall, per variant `[probe][oracle]`

`tools/cc_b2_subdominant_guard_measure.py tools/corpus/default_mod_b2` (326 WiR pieces, 10109 aligned regions,
4036 DCML-modulated). Each variant is a per-span suppress predicate modeled from the enriched **unguarded**
dump (the guard does not fire flag-off, so every span carries its decision fields):

```
variant            nonHomeCommit  precision   recall    (overmod/wrongkey)
baseline               2867       47.0%       33.4%     (1044 / 476)
rel                    2462       51.0%       31.1%     ( 811 / 395)   relationship-only
conf                   2726       48.8%       33.0%     ( 951 / 445)   <- PRODUCTION
refine_v7              2762       48.6%       33.3%     ( 966 / 454)   conf & NOT V7-marker
refine_literal         2726       48.8%       33.0%     ( 951 / 445)   conf & NOT (tonic+10)  == conf
```

- **`rel` reproduces the dossier EXACTLY: +4.0pp / −2.3pp** (47.0→51.0% / 33.4→31.1%). The +4pp prediction
  **transfers** to the full-score region frame; this validates the C++ `subdominantOfAnchor` field against
  `cc_b_guard_separability.py`'s `suppress={"subdominant"}` row.
- **`conf` (production) = +1.8pp / −0.4pp.** The confident-anchor gate is much narrower — only **32 of 86**
  subdominant spans have an anchor ≥ 0.5 — so it suppresses far fewer (precision gain smaller, recall loss
  nearly gone). This is the §3-mandated confident-anchor gate, working as intended.
- **`refine_literal == conf`** (literal flat-7 set on 0 spans → never keeps anything): empirical proof the
  `tonic+10` formula is the wrong pc (§2.3).

Span-level scope: 86 subdominant-of-anchor spans; 32 with confident anchor; of those, 13 carry the V7 marker,
0 carry the literal flat-7.

---

## 4. §3.5 dominant-7th refinement — BUILT, MEASURED, **REJECTED**

The §3.5 hypothesis: keep a subdominant span whose confirming cadence's dominant is a genuine **V7** of the
target (recover the −2.3pp recall). Measurement rejects it on two independent grounds:

1. **It backfires for the snapshot intent.** A **tonicized** IV carries an applied dominant seventh exactly
   like a real modulation. The spurious mozart over-commit is a **C7→F** (the dominant region carries B♭ =
   `dominantSeventhPresent=True`), and bwv806's first D span likewise. So `refine_v7` would **keep** the very
   spurious spans the guard exists to drop. On the snapshot-relevant scores the refinement is actively harmful.
2. **It is a near-no-op on the full-score frame.** `refine_v7` vs `conf` recovers only **+0.3pp recall**
   (33.0→33.3%) at −0.2pp precision — within noise.

**Production guard therefore uses no refinement** (conf-gated only). The V7 marker is retained as a diagnostic
field for this record. *(The §3.5 caveat "measure at build" was correct — and the measurement says no.)*

---

## 5. §4.3 — production byte-identity (flag-OFF) — CONFIRMED `[probe]`

- **`.ours.json` 0-diff** vs the committed baseline (`tools/corpus/{baroque,jazz,default}` @ `2245aedf82`,
  which `5fee657578` documents as byte-identical for production): regenerated into `*_b2chk` with the new
  binary, `cmp`-compared per file — **baroque 0/353, jazz 0/353, default 0/353 mismatches.**
- **BIR gate: Baroque 57 / Jazz 23 / Default 57** (`characterise_bir_false.py` on the `*_b2chk` dirs) — exactly
  the committed identity set.
- **Suites green:** `composing_tests` 545, `notation_tests` 57, `pipeline_snapshot_tests` (flag-OFF) 11; goldens
  **unchanged** (no `--update-goldens`). `localmodulationdetector_tests` + `jointkeydecision_tests` pass
  unchanged (the flag-gate keeps them unguarded).

The guard changed only the dormant/diagnostic path ⇒ production byte-identical, as the premise requires.

---

## 6. §4.2 — snapshot fix DOES NOT TRANSFER — root cause: bridge-path anchor instability `[probe]`

Flag-ON (`MUSE_JOINT_KEY_WIRING=1 pipeline_snapshot_tests`), key field vs golden, with the conf-gated guard:

| score | flag-ON key over-commit (vs golden) | cleared? |
|---|---|---|
| mozart_k279_1 | **+119 "F"** key regions (golden: C) | ❌ no |
| bach_bwv806_gigue | **+144 "D"** key regions (golden: A) | ❌ no |
| corelli_op01n08a | +42 "G" (golden: C minor) | ❌ no (dominant — out of scope) + *false-suppression* |

The conf-gated output is **byte-identical to the refine_v7 output** — the guard does not change the bridge
output at all. A temporary instrumented build (`MUSE_B2_DIAG`, since removed) shows **why**: the bridge path
analyses a **16-measure window** (`pipeline_snapshot_tests.cpp:719`, `kMaxAnalysisMeasures=16`), and the
key-agnostic cadence **anchor over that window is unstable / mis-resolved**:

- **mozart** — bridge anchor resolves to **pc 5 = F major (conf up to 1.0)**, i.e. **the subdominant itself
  becomes the apparent home**. The F spans are then tagged `agreesWithAnchor=true`, `subdominantOfAnchor=false`,
  so the guard **correctly does not fire** — there is no "subdominant-of-anchor" to suppress when the anchor
  *is* F. The over-commit survives. (Full-score anchor is C 0.679, where the guard *does* suppress F — §3.)
- **bwv806** — bridge anchor is **unstable across windows** (A pc9 / D pc2 / E pc4, all at high conf). The
  guard *does* `SUPPRESS` D-spans in windows where the anchor is A, but D keys remain from the windows where
  the anchor is D itself. Net: not cleared.
- **corelli** — in some windows the bridge anchor mis-resolves to **Gm (pc7)**, and the guard then
  **false-suppresses the true C-minor home** as "subdominant of Gm" (`tonic=0 minor=1 subdom=1 → SUPPRESSED`).
  This is the guard being *misled by* a wrong anchor — an active harm, not just a no-op.

**Conclusion:** the guard is **downstream of the anchor**; it can neither fix a mis-resolved anchor (mozart) nor
avoid being misled by one (corelli). The dossier's 2/3 prediction was measured against the stable **full-score**
anchor; the **windowed bridge anchor differs**, so the prediction does not transfer. The snapshot regressions
are fundamentally an **anchor-resolution** problem in the windowed path, not a subdominant-over-commit relative
to a correct anchor.

---

## 7. Stop-condition trace (instruction §6) + disposition

| condition | fired? | note |
|---|---|---|
| Non-dormant production caller of `detectLocalModulations` | **No** | premise holds (§1) |
| Production not byte-identical flag-OFF | **No** | 0-diff / BIR 57·23·57 / suites green (§5) |
| **Measured prediction didn't transfer** | **YES — for §4.2** | snapshot fix 0/3, not 2/3 (§6 above). The §4.1 +4pp DID transfer (rel = +4.0pp). |
| Built a dominant guard / flipped wiring ON / scoped by repertoire | **No** | subdominant-only; wiring stays dormant |
| Edit outside `localmodulationdetector.*` + `tools/` | **No** | only those + the temp diagnostic (added, then removed) |

**Disposition (for user / Cowork ratification) — HELD, no commit:**
1. The guard is **byte-identical in production**, **precision-positive on the full-score frame** (+1.8pp
   conf-gated / +4.0pp relationship-only), and **dormant**. It is not harmful to ship dormant.
2. It does **NOT** meet its primary stated goal (clear the snapshot regressions), and it **can false-suppress**
   the true home when the bridge anchor mis-resolves (corelli). So the global flip-ON stays gated — now blocked
   not only by corelli's dominant case but by **bridge-path anchor instability**, which is the real, upstream
   problem.
3. The §3.5 dominant-7th refinement is **rejected** (backfires + literal formula null).
4. **Recommended next step is upstream of this guard: stabilise the bridge/windowed cadence anchor** (the
   16-measure window mis-resolves the global tonic). Until then the subdominant guard cannot deliver the
   snapshot fix, and a flip would risk the corelli false-suppression. Hold the guard dormant (or defer it)
   pending that — **the flip decision remains gated.**

Whether to keep the (byte-identical, dormant) source change or revert it is the user's call — measurement is
**not clean** (the snapshot prediction did not transfer), so per the instruction's "commit only on a clean
measurement" rule, **no commit**.

---

## 8. Files + reproduction

Changed (working tree, HELD):
- `src/composing/analysis/section/localmodulationdetector.h` — 3 diagnostic fields on `LocalKeySpan`.
- `src/composing/analysis/section/localmodulationdetector.cpp` — `jointKeyWiringEnabled()` fwd-decl, conf-floor
  constant, dominant-region mask lookup, V7/flat-7 markers, the flag-gated conf-only guard.
- `tools/batch_analyze.cpp` — `--dump-modulation` enrichment (`anchorConfidence` + 3 span fields).
- `tools/cc_b2_subdominant_guard_measure.py` — read-only per-variant precision/recall measurement.

Scratch corpora (gitignored): `tools/corpus/default_mod_b2` (measurement surface), `tools/corpus/*_b2chk`
(byte-identity check). The temporary `MUSE_B2_DIAG` instrumentation used to diagnose §6 was removed; the final
binary is clean.

Reproduce:
```
# full-score precision (§3):
python tools/run_bach_preset.py --preset Default --output-dir tools/corpus/default_mod_b2 --dump-modulation
python tools/cc_b2_subdominant_guard_measure.py tools/corpus/default_mod_b2 --floor 0.5
# byte-identity (§5):
python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus/baroque_b2chk   # + Jazz, Default
python tools/characterise_bir_false.py --corpus-dir tools/corpus/baroque_b2chk             # 57 / 23 / 57
# snapshot non-transfer (§6):
MUSE_JOINT_KEY_WIRING=1 ./ninja_build_rel/pipeline_snapshot_tests.exe   # all differ vs golden; key-axis: F/D/Gm remain
```

*Drafted by CC, 2026-06-16, base `5fee657578`. HELD: source changed in working tree, no commit. Cowork verifies
at source; user ratifies.*

**Addendum 2026-06-18 (S3-primitive refactor `8bc1441076`):** B2 was preserved (stash → refactor → re-apply)
across the shared pc/collection primitive extraction. Its three `localmodulationdetector.cpp` helper calls
`lmdPcMod12(...)` were re-pointed to the now-shared `normalizePc(...)` (proven identical). Guard logic
unchanged; `.h` + `batch_analyze.cpp` diffs unchanged. B2 remains uncommitted, dormant (flag-OFF), and
byte-identical to production (Baroque `.ours.json` 0-diff re-confirmed with B2 in the tree). Note: the held B2
set is **three** files — `localmodulationdetector.cpp`, `.h`, **and** `tools/batch_analyze.cpp` (the
`--dump-modulation` diagnostic).
