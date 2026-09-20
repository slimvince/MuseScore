# CC Stage 3a — Triage of the 5 committed `notation_tests` failures (READ-ONLY)

**Date:** 2026-06-25 · **HEAD:** `1fb168f56e` · **Build:** green (composing + notation built this session).
**Mode:** READ-ONLY — no golden refresh, no `--update-goldens`, no code fix, no commit. Working tree
verified clean before and after; stash `bc4fa79c4a…` untouched; `upstream` not touched.

---

## §0 — Decisive provenance (applies to all 5)

All 5 failures were **caused by one ratified commit**, and that commit *says so in its own message*:

> `a6b08af3fe` — *feat(composing): Layer 3 — wire key/mode decoder to replace the per-region resolver (Step 1)*
> > "Suites: composing 596/596; **notation 52/57 (5 expected production moves)**; pipeline_snapshot 11/11
> > after the ratified P1/P2/P3 golden refresh (P4 untouched)."
> > "the **Step-2 scaleMembership reweight is NOT applied** (shared scorer at baseline −0.20/−0.05)."

So the L3 key/mode **decoder** replaced the per-region key resolver on the production region path
(`regionanalyzer.cpp @633 seam`) and on the shared resolver entry points. The commit author **knew**
exactly 5 notation tests moved, refreshed the **P1/P2/P3 pipeline-snapshot goldens** (incl. `mozart_k279_1.json`,
311 lines), but **left these 5 `notation_tests` assertions unchanged**, labelling them "expected production moves."
3a is the at-the-score check the commit deferred.

Git-blame confirms every failing assertion **predates** `a6b08af3fe`:
- `notationimplode_tests.cpp:744` (Mozart fifths==0) — `2e152d50e7`, 2026-04-12.
- `notationimplode_tests.cpp:1160` ("Gm"), `:1702` (cadence 0) — `81978321e3`, 2026-06-03 (the Baroque
  partial-signature C-minor fix; **deliberately** pinned "Gm" as an interim wrong value pending a deferred fix).
- `notationinteraction_harmony_pinning_tests.cpp:240/286` (Roman "I" / Nashville "1") — `f22d71da3d`, 2026-04-23.

**The hypothesis in the instruction (ratified key change → stale goldens) is therefore CONFIRMED as the *cause*.
But "expected production move" ≠ "musically correct."** The BIR gate that ratified `a6b08af3fe` is measured only
on the **Bach chorale corpus** — it does **not** include Mozart K279 or the synthetic harmony-pinning fixture, so
the key behaviour on those scores was **never gate-checked**. 3a finds that 3 of the 5 moves are genuine key
**regressions** invisible to that gate, and 2 are real **improvements**.

---

## §1 — Per-failure triage

### Failure #1 — `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian`
- **Asserts** (`notationimplode_tests.cpp:729`, assert at **:744–745**): for the first region of K279-1 m1,
  `keySignatureFifths == 0` and `mode == Ionian` (C major). This is a **musical-property assertion** (the test
  name is literally "prefers C major"), not a free snapshot — per §3 of the instruction, a property that now
  fails is a *lost property = regression*.
- **Actual at HEAD:** `keySignatureFifths == -1` (fifths assertion fails first; the run did not reach the mode line).
  −1 fifths = **F major / one flat (B♭)**.
- **Correct answer, at the score:** **C major (0 fifths, Ionian).**
  - Score notes, K279-1 m1 (`tools/dcml/mozart_piano_sonatas/MS3/K279-1.mscx`): pitch/tpc =
    E·G·C·C·**B♮(71/tpc19)**·D·C·E·D·**F♮(77/tpc13)**·E·G·F — a C-major scalar line. The measure contains **B♮**,
    which is **foreign to F major** (F major needs B♭). A −1 (B♭) key signature directly **contradicts the notes**.
  - DCML GT (`…/harmonies/K279-1.harmonies.tsv` row 2): `globalkey=C`, `localkey=I`, `globalkey_is_minor=0`,
    m1 label `C.I{` (tonic, chord_tones C-E-G, duration 4.0). Unambiguous C major I.
- **Classification: FIX (regression) — L3 key.** The decoder reads the C-major opening as **F major** (a
  systematic subdominant/flat-side shift). Confirmed at the production level by the refreshed snapshot golden
  `…/snapshots/mozart_k279_1.json`: tick 0 `key:"F"`, chord `"C"` → `"V"`; m2 (tick 1920) `"Dm/F"` → `"vi6"` —
  i.e. the *whole* opening reframed a fifth down (C→F). **Cause:** the newly-wired L3 decoder (`a6b08af3fe`,
  "Step 1") with the **Step-2 scaleMembership reweight explicitly deferred** — without scale-membership
  penalisation, the decoder does not penalise F major for the foreign B♮, so the subdominant reading wins.
- **Disposition note for 3b:** this is a **path we keep** (the L3 decoder *is* the target key path), but it is
  **mid-rebuild**. The proper fix is the deferred L3 **Step-2 reweight**, not a hand-patch — so the practical
  disposition overlaps **DEFER-TO-REBUILD**. Do **NOT** refresh the assertion to −1/F: that would enshrine a
  key the notes contradict (and the K279 snapshot golden already carries the same error — refreshing the
  assertion would *compound* it, not fix it). The honest green-keeping move is a **tracked skip / xfail**
  referencing L3 Step-2. (Refresh-to-current vs skip is Cowork's + the user's call.)

### Failures #4 & #5 — `NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral` / `…_Nashville`
**These two are ONE root cause** (the instruction's prediction is confirmed): the *same* chord rendered two ways.
- **Asserts:** for the fixture `harmony_pinning_i_iv_v_i.mscx` (single-note path `analyzeNoteHarmonicContext`),
  `rows[0]` = measure 1's C-E-G triad should format as **Roman "I"** (`…pinning_tests.cpp:240`) and **Nashville
  "1"** (`:286`). The file header calls these "behavior snapshots," **but the failing value is a musical fact**
  (m1 of an I-IV-V-I phrase is the tonic, not the dominant), so it functions as a property here.
- **Actual at HEAD:** `rows[0].roman == "V"` (`:240`) and `rows[0].nashville == "5"` (`:286`).
- **Correct answer, at the score:** **I / 1** (C major tonic).
  - Fixture (`src/notation/tests/notationtuning_data/harmony_pinning_i_iv_v_i.mscx`): **no `<KeySig>`** (defaults
    to 0 fifths); staff-0 notes are I(C-E-G) | IV(F-A-C) | V(**G-B♮-D**) | I(C-E-G). Total pitch content =
    C·D·E·F·G·A·B — **all naturals = the C-major collection**. F major would need B♭ (B♮ present in m3); G major
    would need F♯ (F♮ present in m2) — **C major is the only key that fits all seven naturals**. m1 = I.
- **Why "V"/"5":** for a C-major triad to be the 5th degree, the key must be **F major (−1)** — exactly the same
  subdominant shift as #1. Roman "V" (uppercase/major) ⇒ F **major**, not D minor (C in D-minor would render ♭VII).
- **Classification: FIX (regression) — L3 key. Same root cause as #1** (decoder flat-side/subdominant shift
  C→F; reached here via the single-note resolver path that `a6b08af3fe` also refactored — these are 2 of the
  "5 expected production moves"). #4 ≡ #5. **Same disposition note as #1** (do not refresh to "V"/"5"; fix is L3
  Step-2; interim skip/xfail is the honest hold).

### Failure #2 — `Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord`
**A property assertion ("do not smear the previous chord") plus pinned interim values — and the property still HOLDS.**
The test has two independent sub-failures; **neither is a chord regression**:

- **Sub-failure (a) — m1 b3, `:1185/:1190/:1205`.** Asserts the thin C-minor V beat (lone G, no third) reads
  **"Gm"** (`expectedBeat` at **:1160**). Actual = **"G"** (annotation `"Chord: G / V (2.17)"`).
  - **Correct answer, at the score:** **"G" (G major = V).** DCML GT (`…/corelli/harmonies/op01n08d.harmonies.tsv`
    row 3: mc 1, onset 1/2, label **`V`**, root/bass = G, chord_type M) ⇒ G major. The test's *own comment*
    (`:1151–1159`) says: *"DCML's V (= G major) is the convention-correct reading … When that fix lands, revert
    m1 b3 to 'G'."* The "Gm" was a **deliberately-pinned interim wrong value**; the corrected-key decoder now
    produces the **DCML-correct "G"**. → **improvement.**
  - **Classification: ACCEPTED-UPDATE.** Update the m1 b3 expectation `"Gm"`→`"G"` (and drop/adjust the
    `unexpectedSymbol "Cm"`). Justification: matches DCML V; the deferred dominant-quality concern is resolved by
    the L3 decoder. Layer: L3 key/L4 chord — **correct now.**
- **Sub-failure (b) — m10 b3, `:1208`.** Asserts the m10 b1 V/v chord ("D") is **not smeared** into m10 b3:
  `EXPECT_EQ(annotation.find("D"), npos)`. Actual: `find("D") == 38`, i.e. matched.
  - **Root cause is a NEW key-area annotation, not a smear.** Annotation = `"Chord: Gm / i (2.17) (in area:
    **G PhrygDom**)"`. The chord reading is **"Gm / i"** — **DCML-correct** (op01n08d row 19: mc 10 onset 1/2 =
    `i/v` = G minor, the tonic of the tonicised dominant). The anti-smear property **HOLDS** (no D chord). The
    failure is purely that the naive substring `find("D")` matches the capital **D** inside **"Phryg·D·om"**
    (Phrygian Dominant), the new L3 key-**area** label (char index 38, verified). This is **test fragility**
    exposed by a new feature, not a chord error.
  - **Classification: ACCEPTED-UPDATE + a required test-robustness fix.** 3b should make the anti-smear check
    token/word-aware (or assert on the chord-symbol field rather than the free-text annotation that now carries
    key-area text). No analysis change is warranted.
- **Net #2:** the analysis is **correct/improved** at every beat checked; both failures are stale-expectation /
  test-construction issues from ratified L3 changes. **No regression.**

### Failure #3 — `Notation_ImplodeTests.PopulateChordTrackEmitsCadenceMarkersOnCorelli`
- **Asserts** (`:1673`, assert at **:1702**): `countCadenceMarkersOnTrack(...) == 0` on op01n08d (C-minor sonata).
  This is a **post-fix behavior pin** — the comment (`:1678–1690`) says the cadence moments exist musically but
  the 0.8 dual-confidence floor wasn't simultaneously met by both halves of any V→i pair under the corrected key.
- **Actual at HEAD:** **1** cadence marker.
- **Detector behaviour** (`sectioncadencedetection.cpp:55–135`, threshold `kAnnotateKeyConfidenceThreshold = 0.8`,
  confirmed `sectionanalyzer.h:86`): a marker is emitted **only** on a textbook pattern — PAC (V→i, V non-minor,
  or viio→i), PC (IV→i), DC (V→vi), or HC (final dominant arrival) — **gated on ≥0.8 key confidence on *both*
  chords and same key/mode**. It cannot fire on a non-cadential transition.
- **Correct answer, at the score:** op01n08d is **wall-to-wall V→i in C minor** and DCML marks several cadences:
  HC at m8 (`V|HC`), PAC at m13 b3 (`i/v|PAC`), PAC at m21 (`I/III|PAC`), PAC at m30 b3 (`i|PAC`), plus the closing
  i. So **a cadence marker is musically warranted**; emitting **1** is strictly **more** correct than the pinned
  **0** (which the test comment itself concedes was a degenerate artifact, not a musical truth). The L3 decoder
  raised regional key-confidence on op01n08d (the piece stays correctly in C minor — see #2: G=V, "G PhrygDom"
  local area), so one V→i pair now clears the 0.8 floor.
- **Classification: ACCEPTED-UPDATE** (assertion "0" is stale; 1 marker on a cadence-rich C-minor sonata is an
  improvement, driven by the ratified L3 key-confidence change). **Layer:** cadence detector (unchanged) reacting
  to higher L3 key confidence.
- **Caveat / 3b action:** I could not extract the marker's exact tick read-only (it's a StaffText written during
  populate; no read-only dump exposes it without instrumentation, which 3a forbids). The classification rests on
  the detector being **structurally incapable** of firing off-cadence + the DCML cadence list. **3b should confirm
  the single marker lands on one of the DCML cadences (m8 HC / m13 / m21 / m30 PAC) before refreshing the count
  to 1.** If, contrary to expectation, it sits at a non-cadence, re-class to FIX.

---

## §2 — Summary

| # | Test | Symptom (actual → expected) | Score-verified correct | Class | Root cause / layer |
|---|------|------------------------------|------------------------|-------|--------------------|
| 1 | `…MozartK279OpeningPrefersCMajorOverFLydian` | fifths **−1 → 0** | **C major** (B♮ rules out F; DCML I) | **FIX** (defer→L3 Step-2) | L3 key decoder: subdominant shift C→F |
| 4 | `…HarmonyPinning.BehaviorSnapshot_RomanNumeral` | **"V" → "I"** | **I** (C-major collection) | **FIX** (defer→L3 Step-2) | same as #1 (key=F) |
| 5 | `…HarmonyPinning.BehaviorSnapshot_Nashville` | **"5" → "1"** | **1** (C-major collection) | **FIX** (defer→L3 Step-2) | same as #1/#4 (key=F) |
| 2 | `…CorelliOp01n08d…DoNotSmearPreviousChord` | "G"→"Gm" (m1); "D" matched (m10) | **"G"** (DCML V) / **"Gm"** (DCML i/v) | **ACCEPTED-UPDATE** (+test-fix) | ratified L3 improvement + new key-area label substring trap |
| 3 | `…PopulateChordTrackEmitsCadenceMarkersOnCorelli` | count **1 → 0** | ≥1 cadence (DCML PAC/HC) | **ACCEPTED-UPDATE** | higher L3 key-confidence → real V→i now qualifies |

**Tally:** FIX = 3 (but **one** key root cause: the L3 decoder C→F subdominant shift; #4 ≡ #5 literally the same
chord, and #1 is the same family on a different score/path). ACCEPTED-UPDATE = 2. REFRESH = 0. Pure
DEFER-TO-REBUILD = 0 (but #1/#4/#5's fix lives in the ongoing L3 Step-2 work, so their *green-keeping* disposition
is defer-style — skip/xfail, **not** refresh).

**Are #4 and #5 one root cause?** **Yes** — confirmed: both are measure 1's C-E-G triad rendered (Roman vs
Nashville) as the 5th degree because the key resolved to F major. **And #1 is the same underlying regression**
(C-major opening keyed as F major) on a different score and entry point.

## §3 — Headline finding for Cowork

The L3 key-decoder wiring (`a6b08af3fe`, ratified on the **Bach-chorale** BIR gate) introduced a **subdominant /
flat-side key shift (C major → F major)** that the gate **cannot see** (Mozart and the synthetic fixture aren't in
the chorale corpus). It is **already baked into a refreshed snapshot golden** (`mozart_k279_1.json` reads the whole
opening in F). The most probable mechanism is the **explicitly-deferred Step-2 `scaleMembership` reweight** —
without it the decoder fails to penalise F major for the foreign B♮. **3 of the "5 expected production moves"
(#1, #4, #5) are genuine key regressions, not acceptable drift; the other 2 (#2, #3) are real improvements whose
test assertions are merely stale.** Recommend 3b: (a) for #2/#3, refresh the assertions (and harden #2's anti-smear
substring check; confirm #3's marker tick at the score); (b) for #1/#4/#5, do **not** refresh to the F-major
reading — track them against L3 Step-2 (skip/xfail interim), and **re-audit the refreshed `mozart_k279_1.json`
golden**, which carries the same C→F error.

## §4 — Constraints honoured
READ-ONLY: no golden refresh / `--update-goldens` / code edit / commit. Working tree clean (verified). Stash
`bc4fa79c4a…` intact. `upstream` untouched; `origin` not pushed. Every "correct answer" is cited to the score
(notes/tpc) and/or DCML GT, not to the test's own expectation.
