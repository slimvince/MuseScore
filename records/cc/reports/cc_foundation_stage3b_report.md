# CC — Foundation Stage 3b: notation-failure disposition (TEST-ONLY)

**Scope honored: test-only.** No scorer / production / inference code changed. No golden
refreshed. Stash `bc4fa79c4a` untouched. `origin` held, `upstream` never (no push of any kind).
Base HEAD `1fb168f56e` → commit A `f755b18315` (tests) → commit B `92e92e105b` (Cowork docs).

---

## §0 — Outcome at a glance

The 5 baseline notation failures are disposed. **One deviation from the written §3 plan, ratified
by Cowork:** the #3 cadence test's new marker proved **spurious** (does not land on a DCML
cadence), so per the §3/§6 STOP-and-surface branch it was surfaced and — on Cowork's decision —
**xfail'd as the same L3 key-emission regression** rather than refreshed. Net: **4 xfail + 1
behavior-neutral correction** (the plan anticipated 3 xfail + 2 corrections).

Final suite state (all green):
- **composing_tests: 624 passed**
- **pipeline_snapshot_tests: 11/11 passed** (the 1 skipped `PipelineDivergenceCObservation.GenerateReport`
  is the pre-existing env-gated diagnostic, `PIPELINE_OBSERVE_DIVERGENCE_C=1`; not a regression)
- **notation_tests: 53 passed / 4 skipped / 0 failed**

All five failures trace to `a6b08af3fe` (*Layer 3 — wire key/mode decoder to replace the per-region
resolver, Step 1*). The fix for the underlying key-emission regression is scheduled at **L1/L3
stabilization plan Phase 4c** (de-brittle the char/lt presence-gate). Nothing here patches it.

---

## §1 — #1 / #4 / #5: xfail the diagnosed C→F key regression (no fix, no golden refresh)

Marked **expected-fail** with `GTEST_SKIP()` at the top of each; assertions and goldens left
exactly as-is (the F reading is flagged-not-blessed). Each skip message keeps the cause visible and
points at the diagnosis + the scheduled fix.

| # | Test | File | Observed failure (HEAD binary) |
|---|---|---|---|
| 1 | `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian` | `notationimplode_tests.cpp` | `keySignatureFifths` = **-1** (F), expected 0 (C) — line 744 |
| 4 | `NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral` | `notationinteraction_harmony_pinning_tests.cpp` | `rows[0].roman` = **"V"**, expected "I" — line 240 |
| 5 | `NotationInteractionHarmonyPinning.BehaviorSnapshot_Nashville` | `notationinteraction_harmony_pinning_tests.cpp` | `rows[0].nashville` = **"5"**, expected "1" — line 286 |

Cause (verified against `cc_keyregression_diagnosis_report.md`): the `characteristicPitch` /
`trueLeadingTone` scorer terms are hard-gated on a `>0.1` window weight. C major's leading tone
B♮ carries weight **0.093** in the 4-beat decoder window at the K279 opening (and is wholly absent
in the bare-C-triad harmony-pin fixture, diagnosis §4), so C is denied both anchors and the opening
flips to **F major**. #4/#5 use `harmony_pinning_i_iv_v_i.mscx` (C-major triad), which the diagnosis
§4 shows reproduces the identical fault — so the F key makes m1's I read as V (RN) / 5 (Nashville).

- No assertion expected-values changed; `mozart_k279_1.json` **not** refreshed; scorer untouched.

## §2 — #2 Corelli `…DoNotSmearPreviousChord`: behavior-neutral correction (now PASSES)

Two fixes, test file only. Verified green in both build cycles.

1. **Stale assertion.** m1 b3 expectation **"Gm" → "G"**. The analyzer at HEAD reads m1 b3 as `G`
   (failure showed `actualSymbol "G"` / annotation `"Chord: G / V (2.17)"`). This is DCML-correct:
   `op01n08d.harmonies.tsv` row `mn=1 mn_onset=1/2` is **V** (= G major) in local key i. The old "Gm"
   was the pre-L3 sparse-chord natural-Aeolian-v reading and is now stale. Comment updated to match.
2. **Matching bug — substring false positive at m10.** The smear check did
   `annotation.find(unexpectedSymbol)` over the whole annotation string. At m10 the annotation is
   `"Chord: Gm / i (2.17) (in area: G PhrygDom)"`; `find("D")` returned **38**, matching the "D"
   inside the key-area label **"PhrygDom"**, not the m10 chord (correctly "Gm"). Fixed by extracting
   the **leading chord-symbol token** (`chordSymbolToken` lambda — text after `"Chord: "` up to the
   `" / "` roman separator or the `" ("` score, preserving slash-chord internal "/") and comparing it
   **exactly**: `EXPECT_EQ(chordToken, expected)` / `EXPECT_NE(chordToken, unexpected)`. The
   anti-smear property the test guards is preserved (m10 still must not carry the m10-b1 "D"; m1 b3
   still must not smear the b1 tonic "Cm"). All 5 beats pass the exact token match.

## §3 — #3 `…EmitsCadenceMarkersOnCorelli`: SPURIOUS marker → STOP-and-surface → xfail (Cowork-ratified)

**The new marker does NOT land on a DCML cadence — it is spurious.** Per §3/§6 this is a STOP
condition; surfaced to Cowork, who chose to **xfail it as the same L3 key-emission regression**
(rather than refresh the count or treat it as a separate bug). The assertion is left at **0** (the
correct C-minor count) — deliberately **not** refreshed to 1 (which would bless the spurious marker).

Evidence (read-only; temporary probe added to the test, captured, then fully reverted — the test is
byte-identical to HEAD apart from the added `GTEST_SKIP`):

- **Probe:** exactly one marker — `tick=53280` (measure 38 beat 1), label **PC** (plagal).
- **Analyzer regions** (`batch_analyze --dump-regions notation --section-level`): the entire ending
  (m36.67–m39) is mis-keyed as **"GPhrygDom"** (G Phrygian-dominant), under which:

  | tick | measure·beat | chord | analyzer RN (GPhrygDom) | DCML (C minor) | keyConf |
  |---|---|---|---|---|---|
  | 52800 | m37 b3 | Cm | **iv** (deg 3) | **i** | 0.991 |
  | 53280 | m38 b1 | G  | **I** (deg 0)  | **V** | 0.990 |

  The pair (Cm/iv → G/I) satisfies `detectCadences`' PC condition (`a.degree==3 && b.degree==0`)
  with assertive confidence on both, same key, different roots → a **PC** marker on the G at m38 b1.
- **DCML reality** (`op01n08d.harmonies.tsv`, cadence rows): cadences are **m8 HC / m13 PAC /
  m21 PAC / m30 PAC / m39 PAC**. The marker sits on a non-cadential **V** (m38 b1), labels the
  *inverse* function (plagal iv→I vs the real i→V), one measure before the genuine **m39 b3 PAC**
  (authentic V→i, tick 55680). It matches **none** of the DCML cadences.
- **Same regression family:** the "G PhrygDom" mislabeling is the *dominant-as-tonic* sibling of the
  K279 *subdominant-as-tonic* (C→F) error; both are key-emission faults introduced by `a6b08af3fe`.
  (It is also the same "G PhrygDom" area label already visible in the m10 annotation in §2.)

`GTEST_SKIP` message records the spurious-marker mechanism, the no-DCML-cadence finding, and "do not
refresh to 1". Fix scheduled Phase 4c (restoring the correct C-minor key returns the count to 0).

---

## §4 — Verification

| Suite | Result | Notes |
|---|---|---|
| `notation_tests` | **53 pass / 4 skipped / 0 failed** (exit 0) | skipped = K279, RomanNumeral, Nashville, EmitsCadenceMarkers |
| `composing_tests` | **624 pass** (exit 0) | unchanged |
| `pipeline_snapshot_tests` | **11 pass** (exit 0) | +1 pre-existing env-gated skip (DivergenceCObservation) |

- Production output unchanged — `git diff` for commit A touches only the two notation **test** files;
  no scorer, no golden, no `.json`/snapshot. (Probe build mid-stage confirmed §1+§2 independently:
  53 pass / 3 skip / only #3 failing, before #3 was xfail'd.)
- Deviation from §7's predicted "N pass / 3 skipped": **4 skipped**, because #3 was xfail'd (Cowork
  decision) instead of refreshed.

## §5 — Commits (local only; origin held; upstream never)

- **Commit A — `f755b18315`** `test(notation): dispose the 5 baseline notation failures — xfail 4
  L3 key-emission regressions, correct the Corelli anti-smear test`
  - `src/notation/tests/notationimplode_tests.cpp` (73 ±)
  - `src/notation/tests/notationinteraction_harmony_pinning_tests.cpp` (15 +)
- **Commit B — `92e92e105b`** `docs(cowork): record the leading-tone presence-gate key regression
  (L3 §11) + schedule the de-brittling fix (plan Phase 4c)`
  - `cowork_l1l3_stabilization_plan.md` (Phase 4c added, prior 4c→4d)
  - `cowork_layer3_keymode_design.md` (§11 leading-tone-gate weakness bullet)

`git show --stat` for each lists only those files. Working tree clean. No push performed.

## §6 — Stop conditions honored

- No scorer / production code changed (the key-regression fix is Phase 4c, not patched here).
- No golden refreshed; no expectation moved to the F reading; the #3 count stays at 0 (spurious
  marker not blessed).
- The #3 marker did not land on a real cadence → **STOPped and surfaced**; xfail applied only after
  Cowork ratified it.
- Stash `bc4fa79c4a` untouched; no push to `upstream` (or anywhere).

After this, the foundation is clean (0 failed) and work resumes at stabilization-plan **Phase 2**.
The four xfails are the standing reminder that Phase 4c (de-brittle the char/lt presence-gate) is the
gating fix; they flip back to green when it lands.
