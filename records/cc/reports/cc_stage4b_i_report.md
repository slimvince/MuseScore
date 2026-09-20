# CC Report — Stage 4b-i: demote the declared-mode wall + measure the honest floor

**Date:** 2026-06-14 · **Status:** HELD (`git add` done, **NO commit**) · **Build:** clean, all suites green.
Implements ratified `docs/stage4b_design.md` §2 (4b-i) per instruction
`cc_instruction_stage4b_i_demote_wall.md`. Every number tagged `[probe]` (measured),
`[code]` (read at source), `[oracle]` (DCML/music21 RomanNumeral checked).

This is the project's **2nd intentional behavior change**. Byte-identity ends on the key AND chord
axes for affected scores — measured and adjudicated below, **not shipped**.

---

## 1. The four demotions (verified call sites)

All edits are inside `src/composing/` (autonomous zone) + `tools/`. **No `src/notation`/`src/engraving`
PRODUCTION file was edited.** The two `src/notation/tests/` edits are test/golden re-pins (§5), the
sanctioned ratified-change path — not production.

| # | Mechanism | Site `[code]` | Change |
|---|---|---|---|
| 1 | −7 penalty → small hint | `keymodeanalyzer.cpp:571-577` (apply); `keymodeanalyzer.h:319` (default); `:454` (bounds) | default `7.0 → 1.0`; bounds lower `3.0 → 0.0`; application point & logic unchanged; doc-comment rewritten ("tiebreaker, not a wall"). Field NOT renamed (kept `declaredModePenalty`; rename was optional). |
| 2 | hard post-hoc promotion → REMOVED | `keyresolver.cpp:344-367` | whole "Strong declared-mode prior" block deleted. |
| 3 | piece-start anchor → note-based opening | `keyresolver.cpp:274-287` | declared short-circuit removed; normal lookahead runs from piece start. |
| 4 | partial-sig correction | `keyresolver.cpp:248` | **UNCHANGED** (declared-gated, intentionally crutch-dependent for 4b-i). |
| 5 | mode-absent toggle | `keymodeanalyzer.h` (`ignoreDeclaredMode` field); `keyresolver.cpp` (clear after derivation); `tools/batch_analyze.cpp` (`--ignore-declared-mode`); `tools/run_bach_preset.py` (passthrough) | forces `declaredMode = std::nullopt`. Default OFF = no-op. |

**Hysteresis confirmation `[code]`:** the note-based hysteresis `promoteWinnerInPlace` block at
`keyresolver.cpp:320-342` (guarded `prevResult != nullptr`, `prevResult`-mode) was **NOT touched** —
only the declared-mode promotion at :344-367 was removed. Verified at source before deleting.

**Piece-start graceful-`nullptr` check `[code]`:** with the anchor gone, piece start (`prevResult ==
nullptr`, `tick < lookbackDuration`) falls through to the dynamic-lookahead loop; `windowStart` clamps
to `Fraction(0,1)` (`:264-266`); the hysteresis block is skipped (`prevResult != nullptr` guard); the
insufficient-PCs fallback (`:314-318`) still covers a degenerate `<3`-PC opening. **No degenerate
piece-start case observed** in any of the 6 corpus runs (no crash, no empty result).

**Flag-off byte-identity `[code]`:** the toggle is a single guarded statement
(`if (prefs.ignoreDeclaredMode) declaredMode = std::nullopt;`) that is unreachable when the flag is
false — so flag-off output is identical to not having the line, **by construction**. Empirically the
mode-present (flag-off) corpora differ from 4a only via demotions §1–3 (the gate is byte-identical
mode-present, §4), never via the toggle. A standalone empirical 0/353×3 of the *toggle-only* commit
would need a toggle-only build (proposed in the commit split, §8).

**Bounds gotcha handled `[code]`:** `keymodeanalyzer.h:454` was `{3.0, 15.0, true}`; lowered to
`{0.0, 15.0, true}` so 1.0 (and 0.0/full-drop) is expressible. No other clamp on the field (grepped).

---

## 2. Key axis — S2 mode-present AND mode-absent (DCML L1 `--key-breakdown`) `[probe]` `[oracle roots]`

Metric: `compare_rn.py --wir-bach <dir> --key-breakdown` (the `a96f179f40` instrument; 326-chorale
WiR-Bach gate set). S2 = `≠global` (genuine key error, lower = better). 4a baseline = the existing
`tools/corpus/{preset}` (post-import-fix, mode-present, with-wall state).

| Preset | 4a (wall 7.0) | 4b-i present (hint 1.0) | Δ present | 4b-i mode-absent (FLOOR) | Δ absent |
|---|---|---|---|---|---|
| **Default** | 685 | **687** | **+2** | **2070** | **+1385** |
| **Baroque** | 683 | **683** | **0** | **2099** | **+1416** |
| Jazz* | 1937 | 2002 | +65 | 2959 | +1022 |

*Jazz key S2 is **unreliable**: 39–46% of our key labels fail to parse (Jazz emits non-standard modal
labels the metric can't map), inflating S2 by ~1800. Treat Baroque/Default as the load-bearing key
numbers. S1 (Default): 4a 2127 → present 2093 → **absent 1205** (−922).

### Headline findings

**(a) Demoting the 7.0 wall to a 1.0 hint is nearly free mode-present.** Default S2 +2, Baroque 0. A
1.0 hint reproduces the wall's aggregate effect because both decide the same thing — relative-pair
near-ties — toward the declared mode; the wall's extra magnitude (7.0) was non-load-bearing for
aggregate accuracy. This is the shippable mode-present behavior.

**(b) The mode-absent floor collapses ~3×** (Default 687→2070, Baroque 683→2099). With **no** declared
mode, note-based inference alone cannot disambiguate relative major/minor (shared diatonic pool), so
~1383 near-tie regions flip to the wrong relative. **The declared mode is a near-total relative-pair
tiebreaker crutch.** This is the central 4b-i measurement and is a **finding, not a failure** (per
instruction §stop-conditions): it quantifies exactly how much of 4a's win is note-recoverable today
(little, without strengthening) and sizes the 4b-ii target.

**(c) The 242 S2→S1 gains do NOT hold mode-absent.** 4a moved 242 region-cases S2→S1 (global key became
correct). Mode-absent S1 drops 2127→1205 (−922) while S2 rises +1385 → the global-key correctness for
those cases is crutch-dependent; note-based inference alone does not keep them globally correct.

---

## 3. The 7 over-lock stems — recovery by condition `[probe]` `[oracle DCML key]`

Detected global key (`detectedKey`), Default preset. DCML key from the 4a report table.

| stem | DCML | notated | 4a | 4b-i present | 4b-i absent | recovery |
|---|---|---|---|---|---|---|
| bwv64.2 | G major | A min | Amin | Amin | Amin | **none** — note inference reads A minor in all conditions |
| bwv365 | a minor | C maj | Cmaj | Cmaj | **Amin ✓** | recovers **mode-absent only** |
| bwv33.6 | a minor | C maj | Cmaj | Cmaj | **Amin ✓** | recovers **mode-absent only** |
| bwv83.5 | d minor | d min | Amin | Amin | Amin | **none** — note inference reads A minor |
| bwv276 | d minor | C maj | Cmaj | FLyd | **DDor** | tonic D recovered mode-absent (Dorian flavor) |
| bwv371 | G major | maj | Cmaj | **GMixolyd** | **GMixolyd** | tonic **G** recovered both (Mixolydian flavor) |
| bwv437 | d minor | min | Amin | **Dmel** | **Dmel** | tonic **D** recovered both (melodic-minor flavor) |

Reading:
- The **relative-pair over-locks** (bwv365, bwv33.6 — declared major over a-minor-DCML) are fixed by
  removing the declared bias, **but only mode-absent**: the 1.0 hint still over-locks them mode-present
  (consistent with §2 — a 1.0 hint is decisive for relative near-ties, helpful when notation=DCML,
  harmful for these notation≠DCML stems).
- bwv371/bwv437/bwv276 recover the correct **tonic** (wrong church-mode flavor — a 4b-ii / Stage-5
  mode-flavor question, not a wrong-key question).
- **bwv64.2 (the stress case) and bwv83.5 do NOT recover any condition.** The note evidence itself reads
  A minor; the over-lock here is not a wall artifact removable by demotion — it needs stronger
  note-based discriminators (4b-ii) or is genuine notation-vs-analyst ambiguity.

---

## 4. Chord axis — BIR gate, both conditions, all three presets `[probe]` `[oracle]`

`characterise_bir_false.py` on each regenerated corpus; identity sets diffed vs the committed 4a
57/23/57.

| Preset | 4a | 4b-i present | 4b-i mode-absent |
|---|---|---|---|
| Baroque | 57 | **57 — byte-identical (0 moved)** | 57 (SWAP: −bwv60.5@30960, +bwv40.8@30720) |
| Jazz | 23 | **23 — byte-identical (0 moved)** | 23 — byte-identical |
| Default | 57 | **57 — byte-identical (0 moved)** | **58** (+bwv40.8@30720) |

**Mode-present: ZERO gate movement on all three presets.** The ratification hard-stop (un-adjudicated
BIR=false increase) **does not fire** in the shippable condition.

**Mode-absent (floor only — not a shippable config) — every moved case DCML-adjudicated:**
- **+bwv40.8@30720** (default + baroque): our reading `Bbm/Db`, **kConf 0.04**, DCML root +9 away
  (whole-tone trichord — an inherently ambiguous sonority whose root the key context must
  disambiguate). **Correct mode-present** (NOT in the mode-present set). → a chord-root error *caused by
  the collapsed mode-absent key*, fully attributable to the deliberate no-crutch condition; not a
  shippable regression. `[oracle]` DCML root Db, ours Bb.
- **−bwv60.5@30960** (baroque): dropped out of the BIR=false set mode-absent (its key context also
  shifted under the floor). Net Baroque stays 57 (swap).

**Verdict:** no un-adjudicated BIR=false increase. The only increase (Default mode-absent +1) is a
DCML-adjudicated artifact of the measurement floor and is correct mode-present. Ratification gate
satisfied.

---

## 5. Snapshots + test re-pins (DCML-adjudicated) `[oracle]`

**Snapshot goldens refreshed (2 of 11), both DCML-verified-correct:**
1. **corelli_op01n08a** — `key G / RN "iv"` → **`key C / RN "i"`** (chord text "Cm" unchanged). DCML
   `op01n08a.harmonies.tsv`: `globalkey=c`, opening `chord=i` `[oracle]`. The removed piece-start anchor
   had been returning the declared key at the **uncorrected −2 signature = G minor** (op01n08a does not
   trigger partial-sig — Ab not pervasive, unlike op01n08d); note-based inference now correctly finds
   C minor i. **Improvement** — validates the whole 4b thesis on a real score.
2. **chopin_bi105_op30_2** — keyArea **confidence only** 0.975 → 0.393 (keyFifths 2, mode "min"
   unchanged = B minor). Honest note-based confidence (no longer inflated by the removed
   promotion/anchor); key identity DCML-neutral. Safe.

After `--update-goldens`, snapshots re-run **11/11 pass**; exactly those 2 `.json` changed.

**Test re-pins (deliberate, listed per instruction §6):**
- `regionanalysis_tests.cpp`: `PieceStartShortcut_DeclaredMinor/Major` → renamed
  `PieceStartOpening_NoteBased_DeclaredMinor/Major`, re-pinned to the note-based path (size 3, C
  minor/C major still at rank 0; dropped the anchor-specific confidence==0.5 / score==margin
  assertions). `PartialSignature_GMinorUnderTwoFlats_NotCorrected` re-pinned: −2 / tonic-G **minor**
  preserved (the guard), winner flavor now `HarmonicMinor` (was Aeolian under the removed wall).
  `PartialSignature_CMinorUnderTwoFlats_Corrected` passes unchanged (comment de-staled).
- `notationimplode_tests.cpp::CorelliOp01n08dOpeningNoteContextMatchesPopulateInCMinor`: the
  `keyConfidence >= 0.5` floor (the removed anchor's hardcoded 0.5) re-pinned to `(0.0, 0.5)` —
  honest note-based 0.2248; chord/key identity (Cm / i) unchanged and DCML-correct. **This is a
  notation *test* re-pin, not a production edit.**

---

## 6. Suites `[probe]`

- composing **505/505** (renamed 2 keyresolver tests, net count unchanged)
- notation **57/57** (after the confidence re-pin)
- pipeline snapshots **11/11** (2 goldens refreshed)
- Build clean (only pre-existing C4100 unreferenced-parameter warnings).

---

## 7. What the floor implies for 4b-ii (first-pass read)

The floor↔ceiling gap (~1383 Default regions) is **almost entirely relative-pair disambiguation** —
note-based inference cannot currently separate relative major/minor without the declared tiebreaker.
4b-ii should strengthen the terms that actually separate relatives, in priority order suggested by the
data:
1. **Tonic-triad / tonic salience** (`tonicWeight` 1.60, `completeTriadBonus` 2.50,
   `missingTonicPenalty` −2.50) and **`applyPairwiseDisambiguation`** (4.50/1.50/1.00) — the direct
   relative-pair discriminators. bwv365/bwv33.6 (recover only when the declared bias is removed) are
   the canonical targets: the correct relative IS note-distinguishable, the bias just overrode it.
2. **True leading tone** (`trueLeadingToneBoost` 1.20) — separates harmonic-minor i from its relative;
   relevant to the bwv371/bwv437/bwv276 tonic-correct/flavor-wrong cases.
3. **Cadence→key wiring** (OQ4, deferred) only if 1–2 leave a residual.
The hard cases (bwv64.2, bwv83.5) where note inference reads a *different* key than DCML are NOT
relative-pair ties — they need either a stronger global tonic model or are genuine ambiguity; flag for
Stage-5/6, do not chase in 4b-ii.

---

## 8. Commit decision (for later — DO NOT commit yet)

HELD. Proposed split:
- **Commit A (infra, byte-identical by construction):** the `--ignore-declared-mode` toggle —
  `keymodeanalyzer.h` field, `keyresolver.cpp` clear, `tools/batch_analyze.cpp` flag + help,
  `tools/run_bach_preset.py` passthrough. Flag-off is inert; a toggle-only build would show 0/353×3.
- **Commit B (the behavior change):** the §1–3 demotions + the test re-pins + the 2 snapshot goldens +
  the doc sync. This is the ratifiable 2nd-behavior-change commit; mode-present gate byte-identical,
  the 2 snapshots DCML-verified.

**Change-set (git-added, HELD):** `src/composing/analysis/key/{keymodeanalyzer.cpp,keymodeanalyzer.h,
keyresolver.cpp,keyresolver.h}`, `src/composing/tests/regionanalysis_tests.cpp`,
`src/notation/tests/notationimplode_tests.cpp`,
`src/notation/tests/pipeline_snapshot_tests/snapshots/{chopin_bi105_op30_2,corelli_op01n08a}.json`,
`tools/batch_analyze.cpp`, `tools/run_bach_preset.py`, `docs/{stage4b_design,back_half_design,
key_path_design}.md`, `cc_stage4b_i_report.md`.

**Doc-sync note:** `docs/scoring_model.md` is the **Chord Analyzer** scoring model (chordanalyzer.cpp
templates/gates/bonuses); `declaredModePenalty` is a **KeyModeAnalyzer** term and is not documented
there (the doc has no key/mode section). Sync was therefore directed to the key-path docs
(`stage4b_design.md` §2.7, `back_half_design.md` §4, `key_path_design.md`) + the in-code comments. The
scoring_model.md §2 template-count invariant is unaffected (no template change).

**Not in the change-set (pre-existing, left untouched):** `docs/decoder_design.md`,
`docs/implementation_roadmap.md`, `STATUS.md`, `COWORK_HANDOFF.md` carried uncommitted edits from a
prior session (metric re-baseline content); not mine, deliberately excluded from `git add`.

**Transient measurement artifacts (gitignored, not committed):** `tools/corpus/{baroque,jazz,default}
_4bi[_abs]/` (the 6 regenerated corpora).

---

## 9. Stop conditions — none triggered
- No `src/notation`/`src/engraving` PRODUCTION edit needed (test/golden re-pins only).
- Correct `promoteWinnerInPlace` block deleted (declared promotion :344-367; note-based hysteresis
  :320-342 preserved — verified at source).
- No un-adjudicated BIR=false increase (mode-present 0 movement; mode-absent +1 adjudicated as a
  floor-condition key-collapse artifact, correct mode-present).
- No degenerate piece-start case after removing the anchor.
- The mode-absent floor collapsing far below the mode-present win is reported plainly as the **finding**
  it is (§2b) — it shapes 4b-ii, it is not a failure.
