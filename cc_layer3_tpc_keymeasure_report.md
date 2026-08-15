# Layer 3 — does a TPC-aware (spelling) key emission beat the pitch-class baseline?

**READ-ONLY / DECODE-ONLY measurement.** Per the CC instruction
"MEASURE whether a tpc-aware (spelling) key emission improves key accuracy."
No production change; no decoder/scorer default changed; one grading path; nothing
wired; `upstream` untouched. Held / gitignored (`cc_*.md`, `tools/corpus_*/`).

HEAD `0147fba317` (the committed Layer-3 wiring increment, Step 1 `a6b08af3fe`, is in
the tree — the decoder is now the live key path). The committed decoder emission is
**pitch-class** (spelling-blind); this measures whether adding the notated **tpc**
spelling helps the held-out key metric, to set the build-order decision **L3-tpc
retrofit before L4** vs **L4-first**.

---

## §0 TL;DR / verdict

There **is** a genuine spelling signal, and it sits **exactly where theory predicts**
(modulation regions), and it **beats a switch-rate control** — but as a standalone
per-slice emission reweight its net effect on held-out **overall** key accuracy is
**MARGINAL** (best **+0.5 pts** Baroque / **+0.6 pts** Jazz), because the modulation
gain is bought back by a near-equal stable-region loss. By the instruction's magnitude
criterion this reads **marginal → L4-first is the disciplined order; the tpc retrofit
is later polish** — with the refinement that the tpc term's weakness is precisely the
missing **tonicization-vs-modulation discriminator that L4 (cadence/function) supplies**,
so the retrofit should be done *jointly with / after L4*, not as a blocking
upstream-first step. Number is the **upper bound** (engraved corpus, reliable spelling).

---

## §1 The tpc term (the variant)

The committed per-slice emission scores 252 `(tonic × mode)` candidates from MIDI pitch
only (`KeyModeAnalyzer::PitchContext` carried `pitch`, not the spelling). The note model
(`NoteEvent`) already carries the notated **tpc** (line-of-fifths spelling); it was being
discarded at the bridge.

**The variant = the committed emission + one tpc term** (so the delta isolates tpc):

- Thread tpc note→emission: add `int tpc` to `PitchContext`; populate it in
  `engravingbridge::pitchContextOverSpan` from `NoteEvent.tpc`. (`pitchContextOverSpan`
  is consumed **only** by the L3 decoder; the live per-region resolver uses
  `collectPitchContext`, untouched.)
- The term (`keymodesequence.cpp::tpcKeyFitForSignature`): TPC is a direct
  line-of-fifths index (`Tpc::TPC_C`=14; each +1 tpc = +1 fifth), so a key whose
  signature is `sf` (Ionian-convention fifths) has its 7 diatonic notes on the
  contiguous line-of-fifths window **[sf−1, sf+5]**. Each note spelled outside that
  window is penalized by its line-of-fifths distance from the nearest edge, weighted by
  the **same note weight the emission uses** (`min(dur·beat, cap)·(bass?mult:1)`), so the
  term is on the emission's scale. Candidate score becomes
  `emission + tpcKeyFitWeight × (−Σ w·lofDistanceOutsideWindow)`; top-K is re-ranked on
  the adjusted score. This is the standard spelling-aware key signal (Temperley "notes
  close on the line of fifths" / Chew Spiral-Array centre), as a first reasonable variant.
- `tpcKeyFitWeight` is a **swept SETTING** on `KeyModeSequencePreferences` (effort
  hygiene), default **0.0**. At 0 the term is skipped and the path is the committed
  pitch-class emission **byte-for-byte**.

**Property the term has by construction (important, see §4):** the window depends only
on the candidate's **signature**, so candidates that share a signature (relative
major/minor; the modes of one key) get the **identical** penalty → the tpc term **cannot
change a same-signature decision**. It re-weights only **cross-signature** (sharp/flat-
side, modulation) choices. The enharmonic distinction it *can* make (F♯ vs G♭ windows
differ) is not gradable here — the WiR ground truth is pitch-class major/minor.

**Production byte-identity (verified):** composing **596/596**; pipeline snapshots
**11/11, NO golden refresh** (production analysis output unmoved). notation **52/57** —
the 5 failures are the *exact* documented "expected production moves" of the already-
committed wiring increment (`cc_layer3_wiring_report.md` §244; MozartK279 opening,
Corelli sparse-beat, Corelli cadence markers, RN + Nashville behaviour snapshots), with
test expectations not yet updated — **pre-existing, independent of this change**. And the
freshly-regenerated weight-0 `base` corpus reproduces the prior committed
`tools/corpus_decode` **exactly** (Δ +0.0 on every axis, both presets) — confirming the
weight-0 path is byte-identical even when regenerated after the edits.

---

## §2 Method (grading)

Held-out **TEST** split (`md5(stem)%100<20`, the harness's existing deterministic
split), per preset (Baroque, Jazz), one grading path — the same direct
**full (tonic+mode) == WiR-local** metric the rest of `cc_layer3_keymode_baseline.py`
uses (`our_key_tonic_fixed` / `C._dcml_key_tonic` / `cmp.align_dcml_regions`), reused
not forked (`--tpc-measure` mode). Region-type breakdown: **STABLE** (WiR local==global)
vs **MODULATION** (local≠global, matched-local). Decode-only throughout: each variant
is a full decode of the 353-stem corpus via
`batch_analyze --decode-keymode --seq-tpc-weight W` (returns before `analyzeScore`).
Sweep = tpc weight {0.25, 0.5, 1, 2, 4}; **controls** = change-cost lowering
(`--seq-change-base` 1.5 / 1.0, no tpc) to test whether any modulation gain is just a
generic "switch more" effect rather than spelling.

---

## §3 Results

Held-out TEST split. `Δ` is variant − baseline in percentage points; region counts in
parentheses are out of stable 3595 / modulation 2645 / scorable 6240 (Baroque ≈ Jazz —
same stems/alignment).

### BAROQUE — baseline (pc, w=0): overall 60.8% (3796/6240) · stable 83.9% (3015) · modul 29.5% (781)

| variant | overall | Δ overall | Δ stable | Δ modul |
|---|---|---|---|---|
| **tpc 0.25** | **61.3%** | **+0.5** [dur +0.3] | −0.4 | **+1.7** |
| tpc 0.5  | 61.0% | +0.2 [dur −0.0] | −1.5 | +2.5 |
| tpc 1.0  | 60.5% | −0.4 | −2.9 | +3.1 |
| tpc 2.0  | 60.6% | −0.2 | −5.1 | +6.4 |
| tpc 4.0  | 59.1% | −1.7 | −8.9 | +8.1 |
| change-base 1.5 (no tpc) | 60.7% | −0.1 | −0.7 | +0.7 |
| change-base 1.0 (no tpc) | 60.6% | −0.3 | −1.1 | +0.8 |

### JAZZ — baseline (pc, w=0): overall 57.4% (3583/6240) · stable 77.6% (2790) · modul 30.0% (793)

| variant | overall | Δ overall | Δ stable | Δ modul |
|---|---|---|---|---|
| tpc 0.25 | 57.5% | +0.1 | −0.4 | +0.7 |
| **tpc 0.5**  | **58.0%** | **+0.6** [dur +0.9] | −0.3 | **+1.8** |
| tpc 1.0  | 57.4% | −0.0 | −1.5 | +1.9 |
| tpc 2.0  | 56.9% | −0.6 | −2.9 | +2.6 |
| tpc 4.0  | 56.2% | −1.2 | −5.7 | +4.8 |
| change-base 1.5 (no tpc) | 57.6% | +0.2 | −0.3 | +0.9 |
| change-base 1.0 (no tpc) | 57.6% | +0.2 | −0.2 | +0.8 |

**Two clean, monotone facts (both presets):** the tpc term **monotonically improves
modulation** matching (Baroque modul +1.7→+8.1; Jazz +0.7→+4.8 as weight rises) and
**monotonically hurts stable** regions (Baroque −0.4→−8.9; Jazz −0.4→−5.7). Overall =
stable + modul exactly (they partition the scorable set), so the net is positive only
at the **low-weight sweet spot** (Baroque ≈0.25, Jazz ≈0.5) and turns negative as the
stable cost overtakes.

### The frontier — tpc vs the switch-rate control (modulation gained per stable lost)

The decisive comparison: does lowering the *transition cost* (catch more modulations,
no spelling) reproduce the tpc frontier? **No** — tpc's modulation-gain/stable-loss
ratio strictly dominates on both presets.

| BAROQUE | Δstable | Δmodul | net | mod-gained / stable-lost |
|---|---|---|---|---|
| **tpc 0.25** | −16 | +46 | **+30** | **2.88** |
| tpc 0.5 | −55 | +67 | +12 | 1.22 |
| change-base 1.5 | −25 | +18 | −7 | 0.72 |
| change-base 1.0 | −38 | +22 | −16 | 0.58 |

| JAZZ | Δstable | Δmodul | net | mod-gained / stable-lost |
|---|---|---|---|---|
| **tpc 0.5** | −10 | +48 | **+38** | **4.80** |
| tpc 0.25 | −15 | +19 | +4 | 1.27 |
| change-base 1.0 | −7 | +20 | +13 | 2.86 |
| change-base 1.5 | −11 | +23 | +12 | 2.09 |

Lowering the change cost is **net-negative** on Baroque (the committed change-base 2.0 is
about right for Baroque stability) and only modestly net-positive on Jazz; in every case
the **best tpc frontier point beats the best switch-rate frontier point** (Baroque 2.88
vs 0.72; Jazz 4.80 vs 2.86). The modulation help is therefore genuine **spelling**
information — accidentals carry key evidence a generic switch-propensity knob cannot.

---

## §4 What the tpc term cannot reach (the residual ceiling)

By construction (§1) the tpc term is **blind to same-signature ambiguity**: it gives the
identical penalty to relative major/minor and to the modes of one key, so it **cannot
move** a relative-pair or modal-rotation decision. The baseline's top misses are
dominated by exactly these same-signature confusions —
`A min→C maj` (157 Baroque / 151 Jazz), `D min→F maj`, `A min→D min`, and the
dominant/relative fifth-rotations — a large share of which tpc leaves untouched. So tpc
addresses **only the cross-signature error class** (modulation, sharp/flat-side). The
same-signature residual needs chord-root / cadence / function evidence (L4/L5), not
spelling.

This is also *why* the stable-region losses appear: a stable region decorated with an
applied-chord's accidental (a tonicization, not a key change) gets pulled toward the
neighbouring signature by the tpc term — a spurious switch that only a
**tonicization-vs-modulation discriminator (L4 cadence/function)** can veto. The tpc
modulation-sensitivity and the stable over-switching are two faces of the *same* missing
L4 signal.

---

## §5 Reliability caveat (stated, not hidden)

The Bach/Jazz corpus is **engraved**, so its spelling is trustworthy and this is the
**upper bound** of the tpc benefit — "tpc benefit *where spelling is reliable*." A MIDI
import carries arbitrary enharmonics (pitch2tpc defaults), so the line-of-fifths window
fit would be noisier and the benefit smaller or absent. Any deployment must treat the
tpc term as conditional on spelling provenance (engraved/MusicXML-with-accidentals →
trust; raw MIDI → discount or disable).

---

## §6 Verdict (the build-order input)

**Does the tpc-aware emission beat the pitch-class baseline on held-out key, and by how
much, where?**

- **Where:** at **modulations**, cleanly and monotonically (up to +8.1 pts Baroque /
  +4.8 Jazz on the modulation slice), and with a modulation-gain/stable-loss frontier
  that **beats a switch-rate control** — i.e. real spelling signal, exactly where theory
  predicts. It is **blind** to the large same-signature (relative-pair / modal-rotation)
  residual.
- **By how much (overall):** **marginal** — best held-out overall full-match **+0.5 pts**
  (Baroque, tpc 0.25) / **+0.6 pts** (Jazz, tpc 0.5), dur-weighted +0.3 / +0.9; net-
  negative beyond the low-weight sweet spot, because the modulation gain is offset by an
  almost-equal stable-region loss.

**Recommendation → L4-first.** On the instruction's magnitude criterion the held-out
*overall* gain is marginal, so building Layer 4 on the current pitch-class key is fine; a
tpc retrofit is **not** a blocking upstream-first step. The crucial refinement: the tpc
term's weakness is **not** that the signal is absent — it is that, applied at the emission
layer alone, it lacks the tonicization-vs-modulation gate. That gate is **L4's job**.
The disciplined order is therefore: **build L4 first, then retrofit tpc jointly with
L4's modulation/cadence decision** (where its clean +2–8 pt modulation sensitivity can be
admitted without the stable-region cost), rather than locking the stable/modulation
trade-off into the L3 emission before L4 exists. Doing the retrofit pre-L4 would commit
to a wash; doing it with L4 converts it to a gain. **Cowork + user make the order call;
evidence above.**

---

## §7 Reproduction + local (uncommitted) change inventory

**Local edits (decode-only / measurement; all uncommitted, held):**
- `src/composing/analysis/key/keymodeanalyzer.h` — add `int tpc=-1` to `PitchContext`
  (production scorer ignores it).
- `src/composing/analysis/engravingbridge/regiontoneprimitives.cpp` —
  `pitchContextOverSpan` sets `p.tpc = ne->tpc` (L3-decoder-only consumer).
- `src/composing/analysis/key/keymodesequence.{h,cpp}` — `tpcKeyFitWeight` setting
  (default 0.0) + `tpcKeyFitForSignature` + the gated buildLattice branch (weight 0 =
  committed path byte-for-byte).
- `tools/batch_analyze.cpp` — decode-only `--seq-tpc-weight N` (sets `seqPrefs`,
  `--decode-keymode` path only) + help text.
- `tools/cc_layer3_keymode_baseline.py` — additive `--tpc-measure` + `--variant-dir`
  (reuses the existing extractors/aligner/split; one grading path).
- `tools/cc_gen_tpc_corpora.sh` — corpus generation driver (held scratch).

**Reproduce:**
```
# build (byte-identical at the production default; weight-0 == committed decoder)
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# generate base (w=0) + tpc sweep + change-cost controls (≈ 6.5 min/config-pair)
bash tools/cc_gen_tpc_corpora.sh            # base, w0p5, w1, w2, w4
python tools/decode_keymode_corpus.py --preset Baroque --out tools/corpus_tpc/w0p25 --extra-args "--seq-tpc-weight 0.25"
#   (… Jazz; and cb1p5/cb1p0 via --extra-args "--seq-change-base 1.5|1.0")

# grade (held-out TEST split, both presets, stable/modul breakdown)
python tools/cc_layer3_keymode_baseline.py --tpc-measure \
   --decode-dir tools/corpus_tpc/base \
   --variant-dir tools/corpus_tpc/w0p25 tools/corpus_tpc/w0p5 tools/corpus_tpc/w1 \
                 tools/corpus_tpc/w2 tools/corpus_tpc/w4 \
                 tools/corpus_tpc/cb1p5 tools/corpus_tpc/cb1p0 \
   --presets baroque jazz
```
Corpora under `tools/corpus_tpc/` (gitignored). No commit (speculative measurement, per
instruction §5/§6); pursue-tpc decision is the user/Cowork's, jointly with L4.
