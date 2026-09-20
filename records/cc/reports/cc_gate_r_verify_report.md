# Gate R — Final Verification Report

**Date:** 2026-06-09
**Verifier:** Claude Code (Gate R commit gate — independent re-measurement)
**Method:** Two clean builds compared. PRE = baseline (`git checkout` of
`harmonicfunctionlayer.cpp` at HEAD, no Gate R). POST = Gate R (restored from the
uncommitted working-tree edit). For each build the full 353-score corpus was
regenerated for **both** presets and `tools/dump_bir_cases.py` enumerated every
three-way-genuine BIR error; the two case lists were `comm`-diffed. The PRE→POST
difference is therefore attributable **solely** to the Gate R source change (the only
file that differed between the two builds).

---

## 0. Headline

- **Part A arithmetic closes exactly.** Both presets: BIR=false −3 (the three Δ=+7b
  targets), BIR=true −1 (bwv349). **Zero** cases appeared post-Gate-R; **zero** cases
  moved BIR=true → BIR=false. No regression.
- **Part B:** of the 6 drifted snapshots, only **two** have a real user-facing output
  change — both **DCML-verified improvements**: `bach_chorale_003` (Asus4 → D/F#) and
  `bach_bwv806_prelude` (F#m/B → E/G#). The other four (incl. `bach_chorale_137`) are
  **alternatives-list-only** changes with **unchanged winners → Neutral**.
- All gates clear: pipeline snapshots 11/11, composing 407/407, notation PASS.

---

## 1. bwv349 — before/after chord identity + DCML expectation (Part A item 1)

**Region:** bwv349 m13, beat 1, tick **17280**. Note content = pitch classes {0,5,9}
= **C, F, A** (an F-major triad), bass = A (pc 9).

| | rootPc | quality | bassPc | bassIsRoot | symbol | DCML root |
|---|---|---|---|---|---|---|
| **Before (baseline)** | 9 (A) | Minor | 9 (A) | **true** | `Am` (root pos.) | 5 (F) |
| **After (Gate R)** | 5 (F) | Major | 9 (A) | false | `F/A` (I6 in F) | 5 (F) |

- **DCML expects root 5 (F).** The baseline read `Am` (root A = bass) — a BIR=**true**
  error (bass is the root, but the root is wrong). The notes C-F-A are a complete
  F-major triad; the A-minor reading needed E (absent) and treated F as foreign.
- **After Gate R the root is F (matches DCML), bass A = the 3rd → first inversion
  `F/A`, RN I6 in F major.** Correct. The case leaves the BIR error enumeration
  entirely (it is neither BIR=true nor BIR=false post-Gate-R).
- **Mechanism (confirmed against the POST corpus):** at m13 the predecessor region is
  `C major` (root C, tick 16320). With predecessor root = C, **no** root-continuity
  bonus is awarded to either the A-rooted or F-rooted candidate at m13, so F major
  wins cleanly on its complete-triad vertical fit (C-F-A). In the baseline the
  A-rooted reading was carried by root-continuity that Gate R removes upstream; the
  net effect at m13 is the correct `F/A`. This is the **same Gate R family** as the
  three targets (a root-continuity-propped reading displaced by a better-fitting
  complete triad).

---

## 2. Full BIR case diff + arithmetic closure proof (Part A item 2)

Counts (independently re-measured, both presets):

| Preset | metric | PRE (baseline) | POST (Gate R) | Δ |
|---|---|---|---|---|
| Baroque | BIR=false | 16 | 13 | **−3** |
| Baroque | BIR=true  | 25 | 24 | **−1** |
| Jazz    | BIR=false | 10 | 7  | **−3** |
| Jazz    | BIR=true  | 36 | 35 | **−1** |

**Cases that CHANGED STATUS (identical set for BOTH presets):**

```
Moved BIR=false → (removed, fixed):
  bwv245.28  m3  tick4320   our=B/G#(root11)  dcmlRoot=4   [Δ=+7b target]
  bwv296     m12 tick23040  our=D/B (root2)   dcmlRoot=7   [Δ=+7b target]
  bwv320     m27 tick37440  our=G/E (root7)   dcmlRoot=0   [Δ=+7b target]

Moved BIR=true → (removed, fixed):
  bwv349     m13 tick17280  our=Am (root9)    dcmlRoot=5   [bonus fix → F/A]

Moved BIR=true  → BIR=false :  NONE
Moved BIR=false → BIR=true  :  NONE
New cases appearing post-Gate-R (either bucket):  NONE
```

**Arithmetic closure.** The report's "Fixed 4" lumps two different buckets:
- 3 of the 4 fixes (bwv245.28, bwv296, bwv320) were **BIR=false** errors → BIR=false
  16→13 (−3).
- 1 of the 4 fixes (bwv349) was a **BIR=true** error → BIR=true 25→24 (−1).

So `−3` (not `−4`) for BIR=false is correct: only three of the four fixed cases were
ever in the BIR=false bucket. Both BIR=true and BIR=false are **error** counts;
reducing either is an improvement. The instruction's worry ("if bwv349 was a fix
BIR=true should go up") rested on reading BIR=true as a "good" bucket — it is not; it
is the count of root-position (bass-is-root) errors, and fixing one lowers it.

**Regression check (Part A item 3).** bwv349 m13/tick17280 was the **only** bwv349
case in either PRE list (BIR=true). Post-Gate-R it is **absent from both** the
BIR=true and BIR=false lists — it did **not** move to BIR=false; it became correct
(root now = DCML root 5/F). It is the **same** region the report calls "fixed," not a
different one. **No bwv349 region moved BIR=true → BIR=false. No regression.**

Evidence files: `/c/tmp/{pre,post}_{baroque,jazz}.txt` (sorted case enumerations),
diffed with `comm`.

---

## 3. bach_chorale_003 — verdict: **IMPROVEMENT** (Part B)

**Source:** `tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx`
**DCML (When-in-Rome 003, BWV 153.1, analyst A. Jones / proof. Tymoczko–Robb).**

**Tick mapping** (1-quarter pickup ⇒ m1 b1 = tick 480): tick **7680 = m4 beat 4**.
WIR 003 m4: `i6/4 b2 V b3 i :|| b4 G: V6`. So m4 b4 = **`G: V6`** = V of G, first
inversion = **D major, bass F# = `D/F#`**. (Cross-checks: tick 6240 = m4 b1 "i6/4"
key A ✓; tick 7200 = m4 b3 "i" = Am key A ✓.)

**The change.** First snapshot divergence is in the **implode (P1)** region array:

| path | golden (baseline) | POST (Gate R) |
|---|---|---|
| implode P1 (root/quality) | **`Asus4`** (root A, sus4) | **`D major`** (root D) |
| annotation P2 (`text`) | `D/F#` / `IV6` (UNCHANGED) | `D/F#` |
| tickRegional P3 (winner) | `D major` (root D, UNCHANGED) | `D major` |

In the **baseline golden the P2 and P3 paths already read D major (`D/F#`)**; only the
P1 implode path read `Asus4`. Gate R brings P1 into agreement with P2/P3.

**Why D is correct and Asus4 is wrong.** Region notes = D-F#-A (a D-major triad, bass
F#). `Asus4` = A-D-E: it needs E (**absent**) and excludes F# (**present**). The
baseline `Asus4` was root-continuity propped (previousRootPc = 9 = A, the Am at tick
7200) with bass F# (interval 9, M6 — foreign to every A-template); Gate R strips that
rcb and the complete D-major triad wins. **POST `D/F#` = DCML `G: V6`. Moves toward
DCML and unifies all three paths → Improvement.**

---

## 4. bach_chorale_137 — verdict: **NEUTRAL** (Part B)

**Source:** `tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx`
**DCML:** When-in-Rome **134** (D minor, 1 flat — matches the score's key signature
`-1`; the other "Weltgebäude" setting, WIR 087, is G minor / 2 flats and does not
match).

**The change (full structural diff).** A single region at tick **21120** (key D),
**alternatives-list only**:

| | alternatives |
|---|---|
| baseline | [F maj 2.488, **C maj 1.975**, F maj 1.787] |
| POST | [F maj 2.488, **F maj 2.488**, A min 1.75] |

**The region winner is `F major` in BOTH baseline and POST — unchanged** (the
`root`/`quality` winner fields are identical; no `text`/`harmonyText` changed). The
demoted candidate is a **C-major alternative inflated by root-continuity**
(previousRootPc = 0 = C) whose bass is foreign to C-major — exactly Gate R's target.
Removing it does not change the user-facing chord.

**No output change → Neutral** (the internal alternatives reorder is consistent with
Gate R's intent).

---

## 5. The other four drifted snapshots (completeness)

Direct structural diffs (baseline golden vs POST) classify all six:

| Snapshot | Change | Winner changed? | Verdict |
|---|---|---|---|
| bach_chorale_003 | implode `Asus4`→`D/F#` | **yes** | **Improvement** (DCML `G:V6`) |
| bach_bwv806_prelude | `F#m/B`→`E/G#` (V6) + bridge split @23280 | **yes** | **Improvement** (DCML `I6` of localkey E) |
| bach_chorale_137 | alternatives only | no | Neutral |
| bach_bwv806_gigue | alternatives only (runner-up D maj→C♯ min) | no | Neutral |
| mozart_k279_1 | alternatives only (spurious `G/E` alt dropped) | no | Neutral |
| chopin_bi105_op30_2 | alternatives only (B-min/B-dim tie reorder) | **no** | Neutral |

Two notes correcting the implementation report's §8:
- **chopin_bi105_op30_2 is NOT a winner change.** The region winner is `B minor` in
  both baseline and POST; only the (tied 2.165) alternatives reordered. The report's
  "winner B min→B dim" is inaccurate. → Neutral, not a winner change.
- **bach_bwv806_prelude IS DCML-verified.** DCML harmonies TSV
  (`bach_en_fr_suites/.../BWV806_01_Prelude.harmonies.tsv`, 12/8, global key A) at
  **mn9 onset 1/8 (qb 48.5 = tick 23280)** is labelled **`I6` in local key E (= V of
  A)** = **E major, first inversion, bass G# = `E/G#`**. POST reads exactly `E/G#` /
  `V6`; baseline read `F#m/B`. The bridge-path segmentation split at tick 23280
  matches DCML's harmonic rhythm (DCML: I at qb 48 → I6 at qb 48.5). → Improvement.

So **only two snapshots change user-facing output; both are DCML-confirmed
improvements.** The remaining four are alternatives-only with unchanged winners.

---

## 6. Test suites (final Gate R binary)

- pipeline_snapshot_tests: **11/11 PASS** after `--update-goldens` (6 goldens
  refreshed: chorale_003, chorale_137, bwv806_prelude, bwv806_gigue, mozart_k279_1,
  chopin_bi105_op30_2).
- composing_tests: **407/407 PASS**.
- notation_tests: **52/52 PASS**.

---

## 7. Commit hashes

- Gate R + scoring_model.md + 6 refreshed goldens (8 files): **`638ced1c12`**
- STATUS.md: **`0b51395527`**

Both on `master`. **Not pushed.**

---

## 8. Verdict

Part A arithmetic closes with **zero regressions** in either preset (independently
re-measured by full baseline diff). Part B: both real output changes are
DCML-verified improvements; the rest are output-neutral. **Cleared to commit.**
