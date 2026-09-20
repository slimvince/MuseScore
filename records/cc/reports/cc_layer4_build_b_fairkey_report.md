# CC — Layer 4 / Increment B — fresh build+test + the FAIR-KEY re-measurement

**Status:** READ-ONLY / decode-only. Two checks on the current tree (HEAD `5f6b9828a5`, Increment B), per the CC
instruction: (§1) re-confirm B's gate with **freshly re-run** numbers; (§2) the **fair-key re-measurement** — feed the
chord decoder the **real Layer-3 per-slice key** in place of the single notated signature, to test whether the −15.4
chord-root residual is the **key handicap** (the build-B report's attribution) or a real per-slice limitation. Nothing
wired; production byte-identical; no new commit (the diagnostic is held local/uncommitted). `upstream` untouched.

**Verdict up front (§3):** **STOP and surface.** Feeding the real L3 per-slice key recovers **+0.04 pts (Baroque) /
−0.01 pts (Jazz)** of the ~15.4-pt gap — it **barely moves from 58.4**. Per the instruction's §3, this is the
"attribution is wrong" branch: **the single-notated-key handicap is NOT the explanation for the residual.** The residual
is a real per-slice limitation (the symmetric/relative root confusions + per-slice vs per-region granularity), i.e.
Increment-C territory — but the build-B report's claim that "much of the residual closes with the real key (a wiring
concern)" is **refuted**. Decision on whether C proceeds is for Cowork + the user; the evidence is below.

---

## §1 — Fresh build+test (current tree, HEAD `5f6b9828a5`)

Built the current tree (`setup_and_build.bat`; `ninja: no work to do` — the committed HEAD + held WIP were already
built) and re-ran all three suites **freshly** (not relayed):

| suite | result | notes |
|---|---|---|
| `composing_tests` | **617/617 PASS** | (1 disabled) — matches the build-B gate |
| `pipeline_snapshot_tests` | **11/11 PASS, NO golden refresh** | byte-identity proof — production output did not move |
| `notation_tests` | **52/57** | the **same 5** held-WIP failures, **no new failure** |

The 5 notation failures are byte-for-byte the build-B set, all driven by the **held, uncommitted key-decoder WIP** in the
working tree (NOT Layer 4):
`Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian`,
`Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord`,
`Notation_ImplodeTests.PopulateChordTrackEmitsCadenceMarkersOnCorelli`,
`NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral`,
`NotationInteractionHarmonyPinning.BehaviorSnapshot_Nashville`.
**§6 STOP not triggered** (no new notation failure; no production output moved). After adding the §2 diagnostic and
rebuilding, `pipeline_snapshot_tests` was re-run = **11/11 still** (the composing lib recompiled; production byte-identical).

## §2 — The fair-key re-measurement

### What was built (decode-only; production byte-identical)
A new read-only diagnostic flag **`--decode-chords-l3key`** (implies `--decode-chords`; mirrors `--decode-keymode`). On
this path the chord decode, per slice, is scored under the **Layer-3 sequence decoder's per-slice key/mode**
(`keymodeseq::KeyModeSequenceDecoder::decode` — the SAME per-slice key the wired decoder would produce, over the SAME
slices/model), in place of the single notated signature. This simulates exactly what the wiring increment's key
feed-forward delivers.

Mechanically: `ChordSliceDecoder::decode` gained a **per-slice-key overload** taking a `std::vector<{fifths, mode}>`
(one entry per slice). The key enters **only** candidate generation (`analyzeChord`'s diatonic prior) — slicing and
windowing are untouched — so a **constant** per-slice key reproduces the scalar single-key `decode()`
**byte-for-byte** (verified below). The L3 feed runs only under the diagnostic, which **returns before `analyzeScore`**;
`grep` confirms `ChordSliceDecoder` is referenced only by its own `.h/.cpp`, the tests, and `batch_analyze.cpp` — never
by the production region/section analyzers. **One grading path** (`cc_layer4_chord_baseline.py`, unchanged).

**Byte-identity check:** a *fresh* single-notated-key run on the new binary
(`tools/corpus_decode_chord_b`) reproduces the build-B report to the digit — Baroque dur-wt **58.387%**, Jazz
**58.337%**, membership NCT-recall **34.5%** / CT-precision **82.9%** — confirming the overload did not perturb the
single-key path.

### The result (held-out TEST split, dur-weighted chord-root, both presets)

| chord-root, dur-weighted (TEST) | Baroque | Jazz |
|---|---|---|
| per-region **baseline** (`.ours.json`) | **73.84%** | **73.67%** |
| B — **single notated key** (current) | 58.39% | 58.34% |
| **B — real L3 per-slice key** (this test) | **58.43%** | **58.33%** |
| Δ (L3-key − single-key) | **+0.04 pts** | **−0.01 pts** |
| Δ to per-region baseline | **−15.41** | **−15.34** |

Region-count match: single-key 3425/6240 → L3-key 3426/6240 (Baroque, **+1 region**); 3420/6240 → 3420/6240 (Jazz,
**0**). Membership metrics unchanged (NCT recall 34.5%, CT precision 82.9/82.8%). The top root misses are **unchanged**
and remain the symmetric/relative-fifth confusions: `2→9 (D→A), 9→4, 9→2, 7→2, 5→2, 11→2`.

### Breakdown — how much of the −15.4 closes, and why it doesn't

**It does not close: +0.04 pts of ~15.45 (Baroque), −0.01 (Jazz) ≈ 0% of the gap.**

This is **not** because the L3 key equals the notated key. The L3 per-slice key **genuinely differs** from the notated
signature on a large fraction of slices (dur-weighted, TEST):

| L3 key vs notated | Baroque | Jazz |
|---|---|---|
| slices where L3 key ≠ notated | **34.0%** | **43.9%** |

Of the Baroque differing slices (all splits): ~4774 carry a **different key signature** (a genuinely different diatonic
PC set), ~2802 are **same-signature** relative/modal respellings (relative major↔minor: same 7 PCs), and ~2589 are
harmonic-minor / modal labels (`Gharm`, `Aharm`, `DDor`, `GMixolyd`…). So even when the chord scorer is handed a
**substantively different — and, per L3's own held-out grading, more locally-accurate — key prior on a third to nearly
half of slices, the chord-root match is flat.**

The mechanism: in the chord competition the key/mode is a **weak diatonic tiebreaker** (it tips genuinely-close readings
toward the key's scale). The dominant residual error modes are **not** decided by that tiebreaker:
- the top misses are **symmetric / relative-fifth root confusions** (`D↔A`, `dim7` rotations, relative major/minor) —
  the **Increment-C spelling-pin** target; the key prior cannot pick the spelling-correct rotation among same-PC
  candidates;
- a relative major↔minor key change keeps the **same diatonic PC set**, so the diatonic-membership bonus is identical →
  no root change (a large share of the 34/44% differences are of this kind);
- the rest is the **per-slice vs per-region granularity** difference, already largely addressed by the membership lever
  (the +12.6 in build-B) and not a key concern.

## §3 — Verdict (the decision input for Increment C)

Per the instruction's §3 decision rule:

> *"If B-with-L3-key barely moves from 58.4: the key handicap is NOT the explanation → the attribution is wrong → STOP
> and surface for investigation before any C / wiring spend."*

**This is the branch we are in. STOP and surface.**

What the evidence establishes:
1. **The build-B report's residual attribution is partly WRONG.** The claim that the −15.4 is *dominated by* the
   single-notated-key prior (a wiring concern) is **refuted**: the real per-slice L3 key — different on 34–44% of slices
   — recovers ≈0 pts. **Wiring the L3 key into the chord layer will not, by itself, improve chord-root.**
2. **The surviving explanation is the OTHER source the build-B report named (b): the symmetric / relative-root
   confusions** — now shown to carry essentially the **whole** residual, not a part of it. That is precisely the
   Increment-C spelling-pin's target. So C's *motivation* is strengthened, even as the "wiring recovers much of it"
   premise is removed.
3. **Open question for Cowork + user before C/wiring spend:** the residual is a genuine per-slice limitation split
   between (i) spelling/relative-root (C's spelling-pin) and (ii) per-slice-vs-per-region granularity. The fair-key test
   cannot separate those two; a clean next read-only step would quantify how much of the −15.4 is granularity (per-slice
   over-segmentation scored against per-region GT) vs spelling, to size what C's spelling-pin can actually reach before
   committing to it.

I am **not** proceeding to Increment C or to wiring. Cowork + the user decide, with this evidence.

## §4 — Constraints honored
- **Read-only / decode-only.** Production byte-identical: `pipeline_snapshot_tests` 11/11 with no golden refresh both
  before and after the diagnostic was added; `ChordSliceDecoder` is grep-confirmed decode-only (no production caller);
  the L3-key feed runs only under `--decode-chords-l3key`, which returns before `analyzeScore`. **One grading path.**
- **No wiring.** The live per-region `analyzeChord` seam is untouched.
- The fair-key diagnostic stays **local (uncommitted)**, like the tpc measurement; held WIP stays unstaged; this report
  is gitignored (`/cc_*.md`). `upstream` untouched.

## §5 — Files (held / uncommitted; decode-only)
- `src/composing/analysis/chord/chordslicedecoder.{h,cpp}` — additive **per-slice-key `decode` overload** (constant
  vector ⇒ byte-identical to the scalar path; `decodeWindowed` refactored to look up the key per slice).
- `tools/batch_analyze.cpp` — the `--decode-chords-l3key` flag + the L3 per-slice key feed in the `--decode-chords`
  block (runs the L3 decoder over the same slices/model, builds the per-slice key vector, calls the overload; emits
  `l3KeyFeed` / `l3KeyedSlices` + per-region key). Help updated.
- Decode output (gitignored): `tools/corpus_decode_chord_b/` (fresh single-key re-confirm),
  `tools/corpus_decode_chord_l3key/` (the fair-key run), both presets, 353/353 each.
- Grader `tools/cc_layer4_chord_baseline.py` — **unchanged** (one grading path).
