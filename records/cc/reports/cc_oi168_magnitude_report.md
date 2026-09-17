# OI-168 — the δ tonic-dependence magnitude: measurement report

**Session:** CC, 2026-07-14. **Dispatch:** `cc_instruction_oi168_magnitude.md` (Cowork, 2026-07-13).
**Type:** MEASUREMENT build — default-OFF instrumentation + a default-OFF signature-mask A/B variant.
**No fix is promoted to default.** The production path is unchanged and regenerates the corpus byte-identically.

---

## 1. What is being measured, and why

OI-168 establishes at the code that `analyzeChord`'s two key-consuming scoring terms —
`dim7CharacteristicBonus` (`chordanalyzer.cpp:574-578`) and `diatonicRootContribution` (`:901-905`) — test
membership in the set

    S = { (keyTonicPc + scale[i]) mod 12 },  keyTonicPc = ionianTonicPcFromFifths(fifths) + keyModeTonicOffset(M),
                                             scale      = the intervals of DIATONIC_PARENT_INDEX[M]

which equals the key signature's own diatonic collection **iff δ = keyModeTonicOffset(M) −
keyModeTonicOffset(parent(M)) = 0**. δ = 0 for 19 of the 21 modes; δ = +1 for `Altered` and `AlteredDomBB7`,
whose S is the signature's collection **transposed up a semitone** (2 of 7 pitch classes shared).

The break is confirmed. **The magnitude is not:** whether the corrupted membership ever actually flips a
*committed* chord decides the fix's path — byte-identical structural hardening (0 flips) versus a
correctness re-baseline (>0 flips). This report measures that number.

---

## 2. Premise Gate — predictions, recorded BEFORE measuring (#17b)

*(Written and committed to this file before the instrumented binary existed. A gap between prediction and
finding is diagnostic (#3), not a curiosity.)*

### Task A — the `sparsechordrefinement` Aeolian lone-tonic/dominant guard (`sparsechordrefinement.cpp:154-159`)

| quantity | prediction | confidence | basis |
|---|---|---|---|
| guard **fires** (Baroque / Jazz / Default) | **0 / 0 / 0** | HIGH | Desk-sim: a fire leaves `quality = Unknown`, and no later pass re-qualifies an `Unknown` region (`applyTonicPriorToSparseChord` only touches Power/Sus2/Sus4). A fire would therefore surface as an `Unknown`-quality, one-pitch-class region in `.ours.json`; the OI-167 pass found none on any preset. |
| guard **shape matched** (uniquePcs == 1 AND degree ∈ {0,4} AND the degree's diatonic triad is Minor — evaluated under **any** mode, not just Aeolian) | **0**, or a very small number | MEDIUM | If the shape ever matched, Aeolian (common in the Bach chorales) would coincide often enough to produce fires. Fires = 0 therefore predicts the shape itself never matches. Which sub-condition kills it is not predicted. |
| function **entries** (`refineSparseChordQualityFromKeyContext` reached with `quality == Unknown`) | non-zero, order 10²–10³ per preset | LOW | Four call sites; no other basis. |

### Task B — the `Altered` / `AlteredDomBB7` population

| quantity | prediction | confidence | basis |
|---|---|---|---|
| region-commit `analyzeChord` calls with `keyMode == Altered` (Baroque / Jazz / Default) | **0 / 24 / 0** | HIGH — *confirmation, not a blind guess* | Read off the committed corpus output surface: the region `key` string carries `keyModeSuffix`, and exactly 24 Jazz regions end in `alt` (`keymode_branch_tests.cpp:153`). Declared as a confirmation because the number is already known from the surface; the counter tests whether the surface and the scorer agree. |
| region-commit calls with `keyMode == AlteredDomBB7` | **0 / 0 / 0** | HIGH | No region key string ends in `altDom` (`keymode_branch_tests.cpp:161`) on any preset. |
| **decoder-window** `analyzeChord` calls (`ChordSliceDecoder` → `candidatesForWindow`), any mode | **0 / 0 / 0** in a default corpus regen | MEDIUM | The decoder is reached only from `--decode-chords`, `--dump-fullspine` and `--dump-joint-probe`; the default `.ours.json` route runs the region analyzer. batch_analyze's own comment calls the decoder "dormant" (`batch_analyze.cpp:3121`). If this prediction holds, OI-168's phrase "the ENGAGED decoder" needs correcting: the defect is live **through the region path**, and the decoder inherits it when engaged. |
| total `analyzeChord` calls with `keyMode == Altered` (Jazz) | **40–48** (> 24) | MEDIUM | `inferNextRootPc` re-enters `analyzeChord` on the *next* region's tones under the *current* region's local key, so each Altered region with a following region and a bass adds one extra call. |

### Task C — the committed-chord flip count (the crux)

| quantity | prediction | confidence | basis |
|---|---|---|---|
| **any** flip at all | **YES — flips > 0** | MEDIUM-HIGH | Desk-sim, `bwv353@7680` (`key = F#alt`): signature fifths = −1 ⇒ the true collection is F major {0,2,4,5,7,9,10}; the code's S is the F♯-major collection {1,3,5,6,8,10,11}. The committed root is **D (pc 2)** — a member of the true collection, **not** of S. So `diatonicRootContribution` today **withholds** its +0.30 from the correct root and grants it to a semitone-transposed set of rivals. With ~12 roots re-scored by ±0.30 in each of 24 regions, some winners must move. |
| flips on Jazz, within the 24 Altered regions | **6–14** (point estimate **9**) | LOW on the exact number | `diatonicRootBonus = 0.30` (`analysistypes.h:210`, no preset override) against unknown per-cell margins; `chordScoreMargin` in the corpus is 0.000 on 22 of the 24 regions, so it is not a usable predictor and no tighter estimate is honest. |
| flips on Jazz **outside** the 24 Altered regions | **exactly 0** | HIGH — structural | For all 19 δ = 0 modes the two membership sets are provably the same set, so the variant's predicate is identical there. Any flip outside the Altered regions would REFUTE the derivation and is a STOP. |
| flips on Baroque and Default | **exactly 0 / 0** | HIGH — structural | Neither preset emits an `Altered` or `AlteredDomBB7` region key (Task B); every mode they do emit has δ = 0. |
| direction of the flips | the variant's reading should be the musically-defensible one more often than not | MEDIUM | The variant scores against the collection the signature actually declares. |

**The load-bearing structural prediction** is the third and fourth rows: *the total flip count equals the
flip count inside the Altered regions, and is 0 everywhere else.* That, not the exact Jazz number, is what
the derivation in OI-168 stakes.

---

## 3. The instrumentation (default-OFF), and the proof that it is inert

`src/composing/analysis/chord/keycollectionprobe.{h,cpp}` — one counter block, two environment
switches, both read once at static init and both unset in production:

| switch | effect |
|---|---|
| `MU_KEY_COLLECTION_PROBE` | the counters count; `batch_analyze` writes `<output>.ours.json.probe.json` beside each score |
| `MU_KEY_COLLECTION_SIGMASK_VARIANT` | the A/B: the two key-consuming terms test `pcInMask(diatonicMaskFromFifths(keySignatureFifths), pc)` instead of the mode-transposed set |

Both switches are **value-less flags**, so a corpus arm is the ordinary `tools/run_bach_preset.py`
with the flag exported — no separate driver and no Windows-path rewriting (the mangling problem the
OI-110 instrument had to work around). The counters are plain integers that no scoring path reads;
the variant flag is `false` unless set.

The two membership loops are unified into one predicate, `pcInKeyCollection`
(`chordanalyzer.cpp`), which carries the A/B. Its committed branch is the same test the two loops
ran before, so the production path is unchanged. The reporting instrument is
`tools/cc_oi168_probe_report.py` (`byteid` / `counters` / `flips`).

**Inertness, proven by regeneration** (each arm = 352 scores × 3 presets, compared per-file by sha256
against the committed `tools/corpus/<preset>`):

| arm | Baroque | Jazz | Default |
|---|---|---|---|
| pre-change binary (HEAD) — *establishes that the committed corpus is at-HEAD-reproducible* | 352/352 identical | 352/352 | 352/352 |
| instrumented binary, **both flags unset** (the required OFF-path proof) | **352/352 identical** | **352/352** | **352/352** |
| instrumented binary, **counters ON**, variant off | **352/352 identical** | **352/352** | **352/352** |

`composing_tests` 1103/1103, `notation_tests` 53/53, `pipeline_snapshot_tests` 11/11 — all green,
**no golden refreshed**, `tools/robust_stop` and `tools/corpus` untouched (every arm wrote to a
scratch directory).

*(Side establishment, worth recording: the committed `tools/corpus` reproduces byte-identically at
HEAD on all three presets, so it is a sound reference despite the manifest being stamped to the
older corpus commit `c50002fee1`.)*

---

## 4. Task A — the Aeolian guard: measured DEAD, and deader than inferred

Counters over 352 scores × 3 presets:

| counter | Baroque | Jazz | Default |
|---|---|---|---|
| `refineSparseChordQualityFromKeyContext` reached with an `Unknown`-quality chord | **0** | **0** | **0** |
| the guard's shape preconditions held (one distinct pitch class, tonic-or-dominant degree, minor diatonic triad — under **any** mode) | **0** | **0** | **0** |
| **the Aeolian guard fired** | **0** | **0** | **0** |

**Prediction met, and the mechanism is further upstream than predicted.** CC's OI-167 inference
(zero fires, argued from the absence of an `Unknown`-quality lone-pitch-class region on the output
surface) is confirmed at a real counter. But the guard is not merely unreached — **the whole
function body is unreached**: across all four call sites and 1,056 score analyses, `analyzeChord`
never once hands the region path an `Unknown`-quality chord, so the early return
(`quality != Unknown`) takes every call. The tonic-dependence of the guard is therefore
**unexercised on this corpus**, not merely un-fired.

**Consequence for OI-167:** its site (b) — "if that guard survives the engagement, L4 is NOT
tonic-independent" — is answered on the measurement side. The guard cannot currently change any
committed chord. Whether it should nonetheless be retired is still OI-102's `sparsechordrefinement`
disposition question; this measurement is evidence FOR retirement (a dead body carrying a
tonic dependence), not a substitute for the decision.

---

## 5. Task B — the population: the surface UNDERCOUNTS the scorer's exposure ~2×

| counter (whole corpus, per preset) | Baroque | Jazz | Default |
|---|---|---|---|
| `analyzeChord` entries, all callers | 122,047 | 121,435 | 122,043 |
| … under `keyMode == Altered` | **0** | **97** | **0** |
| … under `keyMode == AlteredDomBB7` | **0** | **0** | **0** |
| the **committing** region call (`regionanalyzer.cpp`) | 27,073 | 27,073 | 27,073 |
| … under `Altered` | **0** | **49** | **0** |
| … under `AlteredDomBB7` | **0** | **0** | **0** |
| `ChordSliceDecoder` slice-window entries | **0** | **0** | **0** |
| membership verdicts where the signature collection **disagrees** with the mode-transposed set — `diatonicRootContribution` | **0** | **15,563** | **0** |
| the same, `dim7CharacteristicBonus` | **0** | **6** | **0** |

Three findings, two of which correct the register:

**(1) `AlteredDomBB7` is 0-firing** — confirmed at the counter, on all three presets. **`Altered` is
Jazz-only** — confirmed. Baroque and Default never enter the scorer under a δ ≠ 0 mode, and their
`…MembershipDiffers` counters are exactly 0, which is the δ = 0 derivation verified at runtime rather
than on paper.

**(2) The committing call fires 49 times under `Altered`, but only 24 Altered regions survive to the
`.ours.json` surface** (10 scores enter the scorer under `Altered`; only 9 keep an Altered region —
`bwv335` enters 3 times and keeps none). The region analyzer scores each region more than once
(the attempt/pass structure), so **the output surface undercounts the corrupted scorer's exposure by
about a factor of two.** OI-168's "24 Jazz regions" is right about the *surface*; the *scorer* runs
corrupted 49 times. This does not change the conclusion, but it means a future estimate of this kind
must not be read off the surface.

**(3) `decoderWindowCalls == 0` — the `ChordSliceDecoder` is NOT on the production path.** OI-168's
headline says the break is "*INSIDE the ENGAGED decoder*" and that "the ENGAGED `ChordSliceDecoder`
calls the same `analyzeChord`". Measured: in a default `batch_analyze` corpus regeneration the
decoder is entered **zero** times — it is reached only from `--decode-chords`, `--dump-fullspine`
and `--dump-joint-probe`, and `batch_analyze.cpp:3121` calls it "the dormant per-slice decoder".
**The correction:** the defect is live **today, through the REGION path** (`regionanalyzer.cpp`'s
committing `analyzeChord` call), and the decoder — which calls the same scorer — will **inherit** it
when it is engaged. The substance of OI-168 is unchanged and if anything stronger (the corrupted
term reaches the committed output *now*, not only after the engagement); only the word "engaged"
needs replacing.

---

## 6. Task C — the A/B: ONE committed chord flips, and it flips to the RIGHT answer

### 6.1 The flip count

| | Baroque | Jazz | Default |
|---|---|---|---|
| `.ours.json` files changed by the variant | **0 / 352** | **9 / 352** | **0 / 352** |
| regions under an Altered-family local key | 0 | 24 | 0 |
| **committed-chord flips inside those regions** | **0** | **1** | **0** |
| **committed-chord flips anywhere else** | **0** | **0** | **0** |
| regions whose score moved but whose committed chord did not | 0 | 22 | 0 |
| regions absorbed by the flip's downstream re-segmentation | 0 | 1 | 0 |

**The structural prediction held exactly.** Baroque and Default are **byte-identical** under the
variant — all 352 files, both presets. On Jazz, every changed byte lies inside the 24 Altered
regions. Nothing outside the δ ≠ 0 population moved, on any preset. The OI-168 derivation is
confirmed at the objects, not merely on paper.

**The magnitude prediction was wrong by ~9×** (predicted 6–14 flips, point estimate 9; actual **1**).
The diagnosis is visible in the score-only rows: in 22 of the 24 regions the corrupted membership was
**withholding** the +0.30 diatonic-root bonus from a root that was *already winning* — so the
corrected form raises the winner's score (typically by exactly +0.30, less where the complexity
factor scales it) and **reinforces the same winner**. The defect corrupts the *score* on every one of
these regions; it changes the *decision* on one. It is, in the dispatch's terms, mostly latent — but
not entirely.

### 6.2 The one flip, verified at the score

**`bwv145.5` @12960 (m10 b1), local key `D#alt`** — sounding notes, read off the region's own tones
with their notated spelling (`tpc` 23 / 20 / 19 on the line of fifths):

    D♯3 (tpc 23, the bass) · F♯3 (tpc 20) · B4 (tpc 19)   →   a B-major triad in first inversion

| | committed chord | root | score |
|---|---|---|---|
| current code | `Ebm` (roman `i`) | pc 3 | 1.830 |
| variant (the corrected collection) | `B/Eb` (roman `bVI6`) | **pc 11** | 1.900 |

The current reading is not merely a different rotation — **it is a chord the notes do not contain.**
E♭ minor is {E♭, G♭, B♭}; the sounding set is {D♯, F♯, B}. The B is not a chord tone of the committed
`Ebm` at all. The scorer picked E♭ as the root because, under `D#alt`, its corrupted collection S is
the **D♯-major** collection (which contains E♭/D♯ and excludes B), while the key signature's actual
collection is **D major** (which contains B and excludes D♯). The +0.30 diatonic-root bonus was
handed to the wrong root by exactly the semitone transposition OI-168 derives.

**Both oracles agree with the variant, not with the committed output:**

- **music21** (corroboration): tick 12960 → `rootPitchClass: 11, Major triad`; tick 13440 →
  `rootPitchClass: 11, dominant seventh`.
- **DCML / When-in-Rome** (the authoritative ground truth): the robust-stop enumeration lists
  `bwv145.5@12960  our_root=3 -> dcml_root=11  dur=480  cls=b` — i.e. this region is **today a
  class-(b) root failure**, and the variant's root (11) is the ground-truth root.

The flip also merges the following region: `@13440` (`B7/Eb`, a B dominant seventh over the same
bass) is absorbed into the corrected `@12960` B reading, giving one B chord over 12960–13920. That
is the same-root run-coalescing behaving correctly once the root is right — and music21 reads both
halves as root 11 too.

### 6.3 The governing metric moves the right way

Run read-only into a scratch out-dir (`tools/robust_stop` untouched):

```
python tools/a8_rebaseline_measure.py --out-dir <scratch> --corpus-root <variant corpus>
python tools/robust_stop_diff.py --candidate <scratch>
```

| preset | root-failing runs (ref → cand) | class-(b) root-disagree duration | class-(a) | key-agree |
|---|---|---|---|---|
| Baroque | 6506 → 6506 (+0 / −0) | 2,714,000 → 2,714,000 (**+0**) | +0 | unchanged |
| **Jazz** | 6689 → **6688** (+0 / **−1**) | 2,784,160 → 2,783,680 (**−480**) | +0 | unchanged |
| Default | 6522 → 6522 (+0 / −0) | 2,718,080 → 2,718,080 (**+0**) | +0 | unchanged |

`OVERALL: PASS`. The run-level set-diff is **removal-only** and consists of exactly one run — the
case above. Zero additions on any preset; class-(a) unmoved; the key columns unmoved (the key layer
is upstream of this term and the variant does not touch it).

---

## 7. Predicted vs. actual

| prediction | actual | verdict |
|---|---|---|
| Aeolian guard fires 0/0/0 | 0/0/0 | **met** — and the whole function body is unreached, a stronger result than the inference claimed |
| guard shape-match ≈ 0 | 0 | met |
| `refineSparse…` entries: order 10²–10³ | **0** | **missed** — no `Unknown`-quality chord ever arrives; the function is dead on this corpus |
| region-commit `Altered`: 0 / 24 / 0 | 0 / **49** / 0 | **missed on Jazz** — the surface undercounts the scorer's exposure ~2× (multiple scoring attempts per region) |
| `AlteredDomBB7`: 0/0/0 | 0/0/0 | met |
| decoder-window calls: 0/0/0 | 0/0/0 | met — and it corrects OI-168's "engaged decoder" framing |
| **flips outside the Altered regions: exactly 0; Baroque/Default: exactly 0** | **0 / 0 / 0** (both presets byte-identical) | **met — the load-bearing structural claim** |
| flips inside the Altered regions (Jazz): 6–14, estimate 9 | **1** | **missed, ~9× over** — the corruption mostly withheld a bonus from an already-winning root, so it moved scores without moving decisions |
| the flip's reading should be the musically-correct one | it is — DCML root 11, music21 root 11, notated spelling D♯–F♯–B | met |

The one prediction that mattered for the derivation (the structural one) held exactly. The one that
was wrong was the magnitude — and being wrong high is the useful direction: the defect is real,
reaches the committed output, and costs exactly one ground-truth root error today.

---

## 8. Fix-path recommendation

**The flip count is > 0 ⇒ the fix is a correctness re-baseline, not byte-identical hardening.** But it
is the smallest, most favorable re-baseline this repository has seen:

- **Baroque and Default: byte-identical.** No golden, no corpus, no metric moves. Proven, not argued.
- **Jazz: 9 files change; 1 committed chord flips; the flip removes a class-(b) root failure**
  (−480 ticks, removal-only run-diff, zero additions). The hard stop (class-(b) duration
  non-increase, all presets) **PASSES** with room to spare, and the change is a strict improvement
  against the authoritative ground truth.
- The corrected terms take **no tonic at all** (`pcInMask(diatonicMaskFromFifths(fifths), pc)`), so
  the collection/tonic property becomes **structural** — it cannot silently lapse again when a new
  mode is added, which is precisely how it lapsed.

**Recommended next step (a separate, user-ratified commit — NOT done here):** promote the
signature-mask form to the default by deleting the `pcInKeyCollection` committed branch, and
re-baseline `tools/robust_stop/` with the O-12 outgoing snapshot, the run-level set-diff explained
(it is one run — the case in §6.2), and the class-(b) non-increase proven per preset (measured
above). The Jazz `.ours.json` change list is the 9 stems: `bwv135.6`, `bwv145.5`, `bwv187.7`,
`bwv245.37`, `bwv314`, `bwv353`, `bwv404`, `bwv60.5`, `bwv64.8`.

**No pipeline-snapshot golden is affected** — verified on two independent grounds: the snapshot suite
runs the **default** configuration (its only preset mention is a prose comment), and Default is
byte-identical under the variant on all 352 scores; and separately, none of its 12 stems
(`bach_bwv806_prelude/gigue`, `bach_chorale_001/003/137`, `chopin_bi105_op30_1/2`, `corelli_op01n08a`,
`mozart_k279_1`, `mozart_k280_1`, `schumann_kinderszenen_n01`, `C`) is among the 9 that change.

**What this does NOT resolve.** The local key `D#alt` that the region was scored under is itself the
key layer's output, and whether an Altered mode is a defensible local key for a Bach chorale is a
key-layer question this measurement does not touch. The fix makes the chord layer read the *signature's*
collection correctly whatever mode the key layer emits; it does not make the emitted mode right.

---

## 9. Incidental finding — declared, not fixed

**`structuralPenalties` silently ignores its `extThreshold` parameter** (`chordanalyzer.cpp`). Every
caller passes `prefs.extensionThreshold` and the function never reads it — its four penalty branches
use `kSus4StructuralFourthThreshold` and two hardcoded `0.05` literals instead. Pre-existing at HEAD
(confirmed by reading `git show HEAD:…`); it surfaced only as a `C4100 unreferenced formal parameter`
warning when this session's edit forced the translation unit to recompile. A preset knob that appears
wired to a term but does not reach it is a live trap for anyone tuning it. Registered as its own
`OPEN_ITEMS.md` row; **not fixed here** (inference-affecting, and outside this dispatch's scope).

---

## 10. Provenance and reproduce

**Every figure in this report is cited from the generated artifact
`cc_oi168_magnitude_measurements.txt`** (#17f — no hand-transcribed measurement numbers): the raw
stdout of all three byte-identity arms, the counters, the flip diff, and the `robust_stop_diff.py`
verdict, produced by `tools/cc_oi168_probe_report.py` + `tools/a8_rebaseline_measure.py` +
`tools/robust_stop_diff.py`. Corpus reference: `tools/corpus/{baroque,jazz,default}`, verified
at-HEAD-reproducible in arm 1 of that artifact.

```
# arm: counters on, production terms unchanged  (byte-identical to the committed corpus)
MU_KEY_COLLECTION_PROBE=1 python tools/run_bach_preset.py --preset Jazz --output-dir <dir>

# arm: the A/B variant
MU_KEY_COLLECTION_PROBE=1 MU_KEY_COLLECTION_SIGMASK_VARIANT=1 \
    python tools/run_bach_preset.py --preset Jazz --output-dir <dir>

python tools/cc_oi168_probe_report.py byteid   <dir> tools/corpus/jazz
python tools/cc_oi168_probe_report.py counters <dir>
python tools/cc_oi168_probe_report.py flips    tools/corpus/jazz <variant dir>
```

