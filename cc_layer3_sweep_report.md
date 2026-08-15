# CC — Layer 3 key/mode: the BOUNDED L3 SWEEP

**Date:** 2026-06-22 (session 9h follow-up — the bounded-sweep increment)
**Status:** HELD / gitignored (`cc_*.md`), local-only — stays unpushed (the report).
**Scope:** decoder-private tuning only. The decoder stays ISOLATED/unwired; production analysis
output byte-identical. Acts on the **clean L3 set (A∩stable + B∩stable)** only; no L5 work.
Reuses the committed decoder (`c453315faa`) + the decomposition harness (`1538193d4d`).

Baseline (HEAD `1538193d4d`): decode corpus `tools/corpus_decode/{baroque,jazz}` (353/353 each,
with `keyEmission`). The `--decompose` mode reproduces `cc_layer3_error_decomposition_report.md`
exactly: **CLEAN L3 = A∩stable + B∩stable = Baroque 281 (11.5% of miss) / Jazz 196 (7.4%)**.

### BOTTOM LINE
1. **A∩stable is genuine** (§1): sustained home-key regions read as a fifth-relative, distinguishing
   pc strongly present (85%/86%), 10/10 score-verified — not tonicization-contaminated. Target stands.
2. **No decoder-private knob recovers the clean set net-positive** (§2): windowBeats recovers A∩stable
   but kills modulation tracking (net −143…−403); change-cost is net-negative for Baroque (Jazz-only
   gain); topK is saturated at 8; maxAlternatives is output-only. → **all defaults left at baseline.**
3. **The clean-set fix is a SHARED-scorer emission reweight, now MEASURED** (§3-SPEC): sharpen the
   scale-membership out-of-candidate-scale penalty (NOT the leading-tone weight, which crashes). Tested
   decode-only, it lifts **both** stable and modulation accuracy (NET +57…+73 Baroque / +38…+68 Jazz)
   with **no tradeoff** — handed to the wiring increment, BIR-gated.
4. **Production byte-identical** (§4): suites 596/57/11 (no golden refresh); default decode 0/353 diff.
   Decoder unwired, no default changed.

---

## §1 — Step 1 (read-only): A∩stable CONFIRMED genuine (not tonicization-contaminated)

The clean-L3 claim rests on A∩stable, which was absent from the 4 decomposition spot-checks. I
extracted the full A∩stable pile and hand-verified a sample (≥5 per preset) against the **raw
score** via an INDEPENDENT music21 parse (`C:\tmp\verify_astable.py`) — not the harness's own
`_pc_weights_in_window` dump — plus the WiR ground-truth annotation for the home-key check.

**Pile shape (central cutoffs Q2≥4, Q3>0):**

| preset | A∩stable slices | fifth-related (our↔loc 5/7 st) | dpc strongly present (w≥1.0) | kind |
|---|---:|---:|---:|---|
| Baroque | 242 | 206 (85%) | 209 (86%) | diatonic-diff 213 · relative-lt 28 · parallel-3rd 1 |
| Jazz    | 121 | 103 (85%) |  104 (86%) | diatonic-diff 103 · relative-lt 17 · parallel-3rd 1 |

**The dominant pattern is FIFTH-DISPLACEMENT (~85% both presets):** the decoder reads the
**dominant or subdominant** (occasionally the parallel) as the tonic across a **sustained home-key
region** (GT local == global, persist 12–61 beats). This is the *opposite* of a brief tonicization
— it is a sustained home key mis-read as a fifth-relative, exactly the "strongly-present
distinguishing pc out-scored" failure §1 describes.

**Independent score spot-check — 10/10 attributions confirmed** (decoder pick = a 5th from GT home;
distinguishing pc independently present in the score at the dpc-bearing slice):

| stem | m | decoder→GT | relation | dpc | indep. score check |
|---|---|---|---|---|---|
| bwv190.7 | 22 | Gmaj→Dmaj | IV→I | C♯ | C♯ present ql=1 (m22); home D-maj persists 61b |
| bwv277   | 3  | Amin→Dmin | v→i  | B♭ | B♭ present ql=1; WiR cadences resolve to D minor |
| bwv372   | 5–6| Dmin→Gmin | v→i  | E♭ | E♭ present ql=1.5/1.0 both measures |
| bwv40.3  | 9–10| Dmin→Gmin| v→i  | E♭ | E♭ present ql=1.5/1.0; WiR `g:` home |
| bwv304   | 12–13| Gmaj→Dmaj| IV→I| C♯ | C♯ present ql=0.5/1.0 |
| bwv56.5  | 4  | Gmaj→Gmin | parallel | E♭ | **E♭ ql=3** (very strong); G major read despite ♭3 |
| bwv227.11| 12 | Amin→Emin | iv→i | F♯ | **F♯ ql=2.5** (strong); E-min home |
| bwv346   | 7  | Fmaj→Cmaj | IV→I | B♮ | B♮ present (weak ql=0.5); boundary-adjacent |
| bwv418   | 14 | Emin→Amin | v→i  | F♮ | F♮ ql=0.5 **and** F♯ ql=1.5 — GT key-boundary mid-measure (`a:` at b4); alignment-granularity case |
| bwv9.7   | 9  | Amaj→Emaj | IV→I | D♯ | D♯ ql=1.5, D♮ absent — clean |

**Verdict — Step 1 PASSES.** A∩stable is NOT contaminated by tonicizations: the cases are
*sustained* home-key regions read as a fifth-relative (85%), with the home-key distinguishing
degree *strongly present* (86% at w≥1.0). The single boundary case found (bwv418 m14, a GT
local-key change mid-region) is an alignment-granularity artifact, not tonicization contamination,
and is a small minority. The clean-L3 target (281 / 196) stands; no revision needed.

**Diagnostic seed for §3:** the consistent fifth-displacement + relative-lt signature points the
root cause at the **emission scorer underweighting the leading-tone / characteristic raised degree**
relative to raw pitch-class coverage — the dominant/subdominant shares most of the tonic's pcs, so
without sufficient weight on the one discriminating degree (LT for major-IV/I and minor-v/i; raised
LT for relative pairs; ♭3 for parallel) the fifth-relative out-scores the true tonic. Quantified in §3.

---

## §3 — A∩stable root-cause diagnosis (the pivotal finding)

I dumped the SHARED scorer's per-term breakdown (`--dump-key-candidates`, the same `analyzeKeyMode`
+ `KeyModeAnalyzerPreferences` the decoder's emission uses) for 25 representative A∩stable cases per
preset, comparing the decoder's *picked* (fifth-relative) candidate vs the *correct* (GT) candidate.
Per-term Δ = (correct − picked); positive favors correct.

**Finding 1 — A∩stable is largely a decoder emission-CONTEXT effect, NOT a shared-weight deficiency.**
The *same shared scorer*, evaluated at the wider **production region context**, picks the CORRECT key
on **17/25 Baroque** A∩stable cases (winner == correct). The decoder misses them only because its
**per-slice emission** (slice ± `windowBeats`=4.0) fragments the region: individual slices that lack
the sparse distinguishing pc locally favor the fifth-relative, and the change-cost smoothing then
keeps the wrong incumbent across the region. The weights are mostly adequate — the *context* is too
narrow. (Jazz production picks correct on only 7/25, because the Jazz winners are mostly **modal
rotations** of the correct collection — `EDor`/`AMixolyd`/`GLyd`/`DDor` — i.e. the §1b same-collection
center/mode-selection problem, which is L5, not a clean weight fix. See Finding 4.)

**Finding 2 — the discriminating evidence flows through `scaleMembership`, not the dedicated
leading-tone term.** Summed Δ over the 25 cases:

| term | Baroque ΣΔ | Jazz ΣΔ | reading |
|---|---:|---:|---|
| scaleMembership | **+36.98** | **+29.59** | the distinguishing pc (in-correct-scale, out-of-picked) — the real lever |
| keySignatureProximity | +13.20 | +9.60 | notated-signature proximity, consistently favors correct (+0.60) |
| trueLeadingTone (`lt`) | +1.20 | +1.20 | **≈ 0 per case** — both keys share the candidate-LT, so it does NOT discriminate |
| characteristicPitch | 0.00 | +4.80 | only fires for modal (Jazz Dorian/Mixolyd) discrimination |
| triadEvidence | −8.11 | −7.86 | consistently favors the *picked* fifth-relative (~−0.7/case) |
| modePrior | −0.20 | 0.00 | negligible |

The decisive (largest-favoring) term is `scaleMembership` in 20/25 (Baroque) and 17/25 (Jazz). The
dedicated `leadingToneWeight`(0.40)/`trueLeadingTone` term is **inert** for these cases (the fifth-
relative shares the candidate's own leading tone), so simply raising `leadingToneWeight` would NOT
help — the distinguishing degree (D's C♯ etc.) is scored as an in-scale tone, via `scaleMembership`.

**Finding 3 — the decoder-private `windowBeats` is therefore the primary, legitimate A∩stable lever.**
Because the miss is a per-slice context-narrowness effect (same weights win at wider context), widening
the emission window should let each slice accumulate more of the region's distinguishing-pc mass and
recover A∩stable WITHOUT touching the shared scorer. §2 authorizes `windowBeats` exactly when grading
shows a window effect on A∩stable — Finding 1 establishes that. The windowBeats sweep (§2 below) tests
the magnitude.

**Finding 4 — Jazz A∩stable carries an irreducible modal-selection residual.** Where Baroque misses
are tonic displacement (Gmaj↔Dmaj, scoreable by scale coverage), many Jazz A∩stable winners are
**same-collection modal rotations** (E-Dorian / A-Mixolydian for a D-major region; D-Dorian for D-minor).
These are note-undecidable center/mode picks (the §1b rotation/parallel problem) and belong to L5
(cadence/function), not a window or weight change. Quantified in the sweep below.

## §2 — The sweep (decoder-private knobs)

All knobs swept by regenerating the decode corpus (353 stems × 2 presets per point, decode-only
`--seq-*` overrides; production untouched) and grading at REGION granularity on the held-out TEST
split, split by GT stable (loc==global) vs modulation (loc!=global). Baseline (windowBeats=4,
changeBaseCost=2.0, relativePairExtraCost=2.0, topK=8, maxAlternatives=4): **Baroque acc 60.83%
(stable 83.87% / mod 29.53%) · Jazz 57.42% (stable 77.61% / mod 29.98%)**.

### §2a — windowBeats (the A∩stable lever) — REJECTED: net-negative

Widening the emission window recovers A∩stable/B∩stable (stable accuracy rises) but **destroys the
decoder's modulation tracking** (the window bleeds across modulation boundaries) — the inverse trade,
net-negative, monotone-worsening:

| windowBeats | Baroque stable acc | Baroque mod acc | Baroque NET vs base | Jazz NET |
|---:|---:|---:|---:|---:|
| 4 (base) | 83.87% | 29.53% | — | — |
| 6 | 87.2% | 19.58% | **−143** (stable rec +181 / mod dam −276) | −78 |
| 8 | 88.96% | 14.1% | **−225** (stable rec +246 / mod dam −420) | −206 |
| 12 | _(monotone worse)_ | | | |
| 16 | _(monotone worse)_ | | | |

**Verdict:** the A∩stable recovery a wide window buys (≈ +180–250 stable regions) is *more than
cancelled* by the modulation-tracking it sacrifices (≈ −276–443 mod regions). The decoder's narrow
4-beat window is deliberately calibrated for the design's core thesis (track local modulations
~2-3× better than the per-region resolver). **windowBeats is left at 4.0.** A∩stable cannot be
recovered by the window without sacrificing the very capability the decoder exists to provide — so
A∩stable's true fix is the emission reweight (§3 spec, deferred to wiring), which strengthens the
distinguishing degree per-slice WITHOUT widening the window.

### §2b — change-cost (the B-recovery lever) — tradeoff curve, defensible point = BASELINE

Lowering `changeBaseCost` makes switching easier → recovers B (modulation regions) but damages C
(stable regions that spuriously switch = tonicization errors). The tradeoff curve (held-out TEST,
region granularity; B = GT-modulation wrong→correct, C = GT-stable correct→wrong):

| knob value | Baroque B-rec / C-dam → NET | Baroque modAcc Δ | Jazz B-rec / C-dam → NET | Jazz modAcc Δ |
|---|---|---:|---|---:|
| changeBaseCost 2.0 (base) | — | — | — | — |
| changeBaseCost 1.5 | 21 / 29 → **−7** | +0.68 | 30 / 11 → **+12** | +0.87 |
| changeBaseCost 1.0 | 40 / 44 → **−16** | +0.83 | 39 / 29 → **+13** | +0.76 |
| changeBaseCost 0.5 | 55 / 68 → **−27** | +1.21 | 71 / 57 → **+11** | +1.48 |
| relativePairExtraCost 2.0 (base) | — | — | — | — |
| relativePairExtraCost 1.0 | 6 / 22 → **−21** | −0.38 | 23 / 18 → **+5** | +0.04 |
| relativePairExtraCost 0.0 | 9 / 28 → **−20** | −0.27 | 58 / 70 → **−12** | +0.80 |

**Reading:** lowering the change cost is a real B-vs-C tradeoff, and it is **net-negative for Baroque
at every swept value** (C-damage always ≥ B-recovery — e.g. cb0.5 recovers 55 modulation regions but
damages 68 stable). It is net-positive for **Jazz only** (cb1.0/1.5 ≈ +12). Per the threshold policy
(never regress the Baroque-tuned setting to cover a non-Baroque case; do not trade C for B
net-negative), the defensible point for both knobs is the **BASELINE** (changeBaseCost 2.0,
relativePairExtraCost 2.0). A Jazz-only change would require preset-conditioning the decoder-private
prefs — that is new wiring/architecture, out of scope for this isolated sweep (noted for wiring).
`changePerFifthStep` was not swept independently: the curve above shows the change-cost family is
already net-negative on Baroque, and `changePerFifthStep` only scales the same (cof-distance) cost
term — it cannot turn a net-negative family net-positive without the same Baroque C-damage.

### §2c — topK / maxAlternatives (the E-pruning lever) — no recovery (coverage-only)

| value | Baroque acc / carried-rate | Jazz acc / carried-rate | NET |
|---|---|---|---:|
| topK 8, maxAlts 4 (base) | 60.83% / 77.1% | 57.42% / 71.9% | — |
| topK 16, maxAlts 8 | 60.83% / 87.2% | 57.42% / (≈+10pp) | **0** |
| maxAlts 8 (topK 8) | 60.83% / 87.2% | 57.42% / (≈+10pp) | **0** |

**Reading:** topK=16 leaves the decode **byte-for-byte identical** to topK=8 (NET 0, every region
unchanged) — the per-slice top-K state union is already **saturated at 8** (the states ranked 9–16
never win at any slice, so they never enter the Viterbi lattice in a way that changes a pick).
`maxAlternatives` 4→8 raises the **carried-rate** (77.1%→87.2% Baroque, the E-pruning coverage share
the decomposition flagged) but changes **no pick** — it only controls how many ranked alternatives are
*serialized*, not the decode. So the E-pruning lever is **necessary-but-not-sufficient exactly as §2
anticipated**: it surfaces more carried true-keys in the output, but a carried state still has to *win
selection* to recover a miss, and none do here. It buys zero accuracy in the isolated decoder. (It
becomes useful only at WIRING, if a downstream gated re-rank consumes the richer alternative list —
recommendation below.)

### §2 SUMMARY — the chosen defaults = the committed BASELINE (no decoder-private change is defensible)

| knob | swept range | best clean-set effect | collateral | chosen default |
|---|---|---|---|---|
| `windowBeats` | 4 → 6, 8, 12, 16 | A∩stable ↓ (stable acc +5pp) | **modulation acc −15pp; NET −143…−403** | **4.0** (unchanged) |
| `changeBaseCost` | 2.0 → 1.5, 1.0, 0.5 | B(mod) recovered | **Baroque NET −7…−27** (C-damage > B-rec); Jazz-only +12 | **2.0** (unchanged) |
| `relativePairExtraCost` | 2.0 → 1.0, 0.0 | tiny B | Baroque NET −20…−21 | **2.0** (unchanged) |
| `changePerFifthStep` | (not swept — same net-neg family) | — | — | **0.60** (unchanged) |
| `topK` | 8 → 16 | none (lattice saturated) | none | **8** (unchanged) |
| `maxAlternatives` | 4 → 8 | carried-rate +10pp (output-only) | none, but no recovery | **4** (unchanged; raise at wiring) |

**The decoder-private knobs cannot move the clean L3 set net-positive.** Every lever that touches the
clean set (windowBeats for A∩stable, change-cost for B) is **net-negative on Baroque** because the
note-only decoder faces a genuine tension: the *same* context width / switch-readiness that fixes a
stable-region misread also degrades the modulation tracking that is the decoder's reason to exist.
This is the §4 PLATEAU: further knob tuning yields negative returns on the clean set → **STOP.** The
identifiable clean-L3 headroom (A∩stable + B∩stable, Baroque 281 / Jazz 196) is **real but not
unlockable by decoder-private tuning** — it requires the shared **emission reweight** (A∩stable, §3
spec) and a **preset-conditioned change-cost** (B / Jazz), both of which belong to the WIRING
increment where the scorer is tuned once for both paths with no byte-identity conflict.

## §3-SPEC — the A∩stable emission-reweighting spec for the WIRING increment (MEASURED, not predicted)

§3 forbids applying an emission-weight change in this isolated increment (it would move production), so
the proposed reweight was **measured decode-only** (a local `decodeKeyPrefs` copy passed to the
emission; the production `keyPrefs` and `analyzeScore` are untouched → production byte-identical,
confirmed in §4). This turns the spec from predicted into measured evidence. (This is NOT a decoder-side
re-rank/scorer-duplicate — it is the *same* shared scorer evaluated with a different weight value,
measured; the actual change is handed to wiring, where it is applied **once** to the shared
`KeyModeAnalyzerPreferences` for both paths.)

**The lever — sharpen the scale-membership out-of-candidate-scale penalty** (NOT raise the dedicated
leading-tone weight). The distinguishing degree (D's C♯ vs G; D-minor's B♭ vs A-minor; etc.) is scored
by the decoder's emission as an ordinary *scale-membership* tone — present-in-correct-scale,
absent-from-picked-scale — while the dedicated `trueLeadingTone`/`leadingToneWeight` term is **inert**
(both candidate keys credit their own leading tone). So the fix is to make a present distinguishing pc
*penalize the keys that do not contain it* more strongly:

| field | current default | proposed (conservative → strong) |
|---|---:|---|
| `scaleScoreInKeySigOnly` (in notated-sig scale but NOT candidate) | −0.20 | **−0.60 → −0.90** |
| `scaleScoreInNeither` (outside both scales) | −0.05 | **−0.30 → −0.50** |
| `leadingToneWeight` | 0.40 | **leave unchanged** (raising it CRASHES — see control) |

**Measured effect (held-out TEST, region granularity, decode-only override; vs the committed
decoder):**

| reweight | Baroque acc / stable / mod | Baroque NET | Jazz acc / stable / mod | Jazz NET |
|---|---|---:|---|---:|
| baseline | 60.83 / 83.87 / 29.53 | — | 57.42 / 77.61 / 29.98 | — |
| **sharp1** (−0.6 / −0.3) | 61.75 / **84.53** / **30.78** | **+57** | 58.03 / 78.19 / 30.62 | **+38** |
| **sharp2** (−0.9 / −0.5) | 62.00 / **84.45** / **31.49** | **+73** | 58.51 / 78.50 / 31.34 | **+68** |
| LT control (leadingToneWeight 0.4→1.2) | 53.09 / 75.13 / 23.14 | **−483** | 47.79 / 67.76 / 20.64 | **−601** |

**The decisive result:** the scale-contrast reweight raises **BOTH stable AND modulation accuracy
simultaneously** (sharp2: Baroque stable +0.58, mod +1.96) — there is **no stable-vs-modulation
tradeoff**, unlike windowBeats. This is exactly why the reweight is the correct A∩stable lever and the
window is not: sharpening the *per-slice emission discrimination* helps every slice decide its key
better, whereas widening the *temporal window* bleeds context across modulation seams. The
leading-tone-weight control crashes (−483/−601), empirically confirming Finding 2 — the LT term is the
wrong knob (it rewards every key whose LT sounds, including the wrong ones → mass over-switching).

**Spec for wiring:**
1. Apply the scale-contrast sharpen (start at sharp1 = `scaleScoreInKeySigOnly` −0.60, `scaleScoreInNeither`
   −0.30; sharp2 if BIR permits) to the **shared** `KeyModeAnalyzerPreferences` — once, for both the
   decoder and (until retired) the per-region resolver.
2. **GATE (mandatory, measured at wiring where production moves):** dual-preset BIR case-identity
   (Baroque 57 / Jazz 23 / Default 57) byte-or-better + the oracle KEY tier + both snapshot suites.
   These weights are Baroque-calibrated; the magnitude must be BIR-tuned (sharp1 is the conservative
   entry; back off if BIR regresses). The DIRECTION (sharpen out-of-scale contrast) is validated here;
   the magnitude is a wiring-time calibration.
3. **Re-validate** with this exact harness (`--decompose` clean-L3 piles + the region tradeoff grader)
   after the wiring reweight — the instrumentation is committed and reusable.
4. **Residual NOT addressed by this reweight (stays L5):** the Jazz A∩stable modal-rotation tail
   (Finding 4 — `EDor`/`AMixolyd`/`DDor` same-collection center/mode picks) needs cadence/function, not
   a scale weight; and A∩modulation (the bulk of pile A) is the tonicization-arbitration problem.

**B / Jazz change-cost (secondary spec):** lowering `changeBaseCost` to ~1.0–1.5 is net-positive for
**Jazz only** (+12/+13) and net-negative for Baroque (−16/−7). If wiring wants it, it must be
**preset-conditioned** (thread the style preset into `KeyModeSequencePreferences`) — new architecture,
deferred. Do NOT lower it globally (regresses Baroque).

**maxAlternatives (E-pruning carried substrate):** raising `maxAlternatives` 4→8 lifts carried-rate
77→87% with zero decode change — recommended at wiring **if** a downstream gated re-rank consumes the
richer alternative list. No benefit (and so not set) in this isolated increment.

## §4 — Grading / close the loop

**Chosen decoder-private defaults = the committed BASELINE (no change).** Because no default moved, the
decoder output is **byte-identical to the committed decoder** and the directional move vs the pre-sweep
decoder is **zero by construction**. Re-running `--decompose` / `--characterize` on the (unchanged)
decoder reproduces the baseline exactly (CLEAN L3 Baroque 281 / Jazz 196; calibration: uncertainty
recall 14.4% Baroque / 18.3% Jazz, alternative-recall 77.1% / 71.9%). The clean-L3 piles did **not**
shrink via decoder-private tuning — confirming the §2 plateau and that the recoverable headroom is
deferred to the wiring emission reweight (§3-SPEC, where it is measured to recover the set).

**Production byte-identical (verified, not asserted):**
- Test suites on the rebuilt tree: **composing 596/596 ✓, notation 57/57 ✓, pipeline-snapshots 11/11 ✓**
  (12th = the intentionally-skipped report generator) — NO golden refresh. `batch_analyze.cpp` is not
  linked into the suites; the production analysis path was not edited.
- **Default decode byte-identical:** the full Baroque decode corpus regenerated with the rebuilt binary
  (no override flags) is **0/353 files different** vs the committed `tools/corpus_decode/baroque`. The
  new `--seq-*` / `--key-*` flags default to no-op (seqPrefs = `kDefaultKeyModeSequencePreferences`;
  override optionals = nullopt ⇒ `decodeKeyPrefs == keyPrefs`).
- All behavior-changing measurements (§2 sweep, §3 reweight) ran via the decode-only `--seq-*`/`--key-*`
  overrides, which return before `analyzeScore` ⇒ cannot move production.

**Calibration:** unchanged (decoder unchanged). Uncertainty recall is low (14.4% / 18.3%) — a later
`uncertainThreshold` question, noted, not addressed here.

**STOPPING RULE met (§4):** every decoder-private knob yields diminishing/negative returns on the clean
set → STOP. The residual is the attributed L5 mass + the §3-SPEC emission reweight (measured, deferred
to wiring).

## §5 — Deliverables / files
- **Committed (this increment — the sweep INSTRUMENTATION; no decoder default changed):**
  - `tools/batch_analyze.cpp` — decode-only `--seq-*` (KeyModeSequencePreferences) overrides + the §3
    decode-only `--key-*` emission-weight measurement overrides (both read only on `--decode-keymode`,
    which returns before `analyzeScore`; default no-op ⇒ byte-identical). B2 hunks left UNSTAGED.
  - `tools/decode_keymode_corpus.py` — `--extra-args` pass-through for the decode-only sweep flags.
  - `tools/cc_layer3_sweep_grade.py` — the region-level stable/modulation tradeoff grader (B-recovered
    vs C-damaged) reusing the harness internals.
- **Local / gitignored (not pushed):** this report; `tools/corpus_decode_sweep/` (per-point regens);
  `C:\tmp\*` machine dumps + helper scripts.
- **Held / UNSTAGED:** the B2 trio (`section/localmodulationdetector.{cpp,h}` + the `batch_analyze.cpp`
  B2 hunks), `STATUS.md`, the WIP docs, the pre-existing `tools/compare_rn.py` M.

## §6 — Gate / constraint compliance
- Decoder stays isolated/unwired; production **byte-identical** (suites 596/57/11 no golden refresh;
  default decode 0/353 diff). The shared `KeyModeAnalyzer(Preferences)` default is **untouched** (the §3
  reweight was measured via a decode-only copy, never committed as a default).
- Only `KeyModeSequencePreferences` was *swept* (decoder-private); **no default changed** — the
  defensible point is the baseline (every knob net-negative/zero on the clean set).
- One grading path (extended `cc_layer3_keymode_baseline.py` + the region grader reusing its internals).
- A∩stable confirmed (§1) not tonicization-contaminated; the B/C change-cost tradeoff curve reported
  and the net-negative-for-Baroque point honored (not B-maximized); E-pruning reported as
  necessary-but-not-sufficient.
- No decoder-side re-rank built; the emission reweight is specified (and measured) for wiring, not
  applied. No L5 work. `upstream` never targeted; push is `origin`-only.

## §4 — Grading / close the loop

_(in progress)_
