# CC — Layer 3 key/mode: CAUSAL DECOMPOSITION of the carried-but-not-picked errors

**Date:** 2026-06-22 (session 9h follow-up — the error-decomposition increment)
**Status:** HELD / gitignored (`cc_*.md`), local-only — stays unpushed.
**Scope:** measurement only. NO production change, NOTHING wired, NO decoder tuning.
Reuses the committed decoder (`c453315faa`). The only code changes are (1) ONE additive,
diagnostic-only JSON field (`keyEmission`, the chosen candidate's per-slice emission —
§0 below) on the `--decode-keymode` path, which returns before `analyzeScore`, and (2) the
`--decompose` mode added to `tools/cc_layer3_keymode_baseline.py`. Production analysis output
is byte-identical (composing **596** / notation **57** / pipeline-snapshots **11** pass + 1
intentionally-skipped report generator, no golden refresh; `batch_analyze.cpp` is not linked
into the test suites; `.ours.json` uses the non-decode path).

This increment **measures**: it partitions the decoder's carried error mass by *cause*, which
assigns future work to layers. It **amends nothing** — no decoder setting (`topK` / window /
costs / `uncertainThreshold` / `maxAlternatives`) was read for tuning or changed.

---

## §0 — The one additive field, and why it was required

The Q1 branch compares, at each carried-error slice, the **per-slice emission** of the *picked*
(winner) candidate vs the *correct* (GT) candidate. Verified in source
(`keymodesequence.cpp:99,313,349`): `KeyModeAnalysisResult.score` IS the per-slice local-fit
emission (`emissions[t][stateIndex]`), **not** a sequence total — so each carried alternative's
serialized `confidence` (= `alt.score`) gives `emission[correct]` directly. **But** the winner's
emission was *not* serialized: the region's `keyConfidence` is the **sequence margin**
(`alpha+beta`, `keymodesequence.cpp:335`), and the chosen state is excluded from the
`alternatives` list (`:324`). So `emission[picked]` was genuinely absent from the JSON.

Per the §0 rule, exactly ONE additive diagnostic field was added —
`keyEmission` = `sk.chosen.score` — same byte-identical pattern as the `alternatives`
serialization (diagnostic path returns before `analyzeScore`). No other field was added; the
`alternatives` already carry their emissions.

---

## §1 — Inputs / method (one grading path)

Held-out **TEST** split (`md5(stem)%100 < 20`, out-of-sample), per preset, on **all scorable
misses** (decoder ≠ WiR local key). Reuses the Increment-B / characterization grading path
verbatim — `our_key_tonic_fixed`, `C._dcml_key_tonic`, `cmp.align_dcml_regions`, `split_of`,
`_pcs_in_window`, `_is_relative_pair` — extended, not forked. The carried-rate this mode
reports (**Baroque 77.1 % / Jazz 71.9 %**) reproduces the characterization's alternative-recall
exactly (anchor that the path is the same one).

The decision tree (CC instruction §1), applied per carried miss:

- **Q1** `emission[correct]` vs `emission[picked]` (per-slice local-fit, NOT the margin):
  `correct > picked` → **TRANSITION** (emission was locally right; the sequence/change-cost
  overrode it) → Q2; `correct ≤ picked` → **EMISSION** (the emission itself preferred wrong) → Q3.
- **Q2** (TRANSITION): contiguous beat-persistence of the GT-correct local key around the slice.
  `≥ cutoff` → **B** (L3 cost-recoverable, over-smoothed real modulation); `< cutoff` → **C**
  (L5 — brief tonicization the cost arguably should suppress; GT-as-key is a function call).
- **Q3** (EMISSION): does the pc distinguishing `correct` from `picked` appear in the emission
  window (corpus xml, ±4 beats)? **present** (weight ≥ cutoff) → **A** (L3 emission-reweighting);
  **absent** → relative-pair → **C**; symmetric sonority **at the slice** → **D**
  (chord/spelling); else → **F** (cause-indeterminate-from-notes / modal rotation — an honest
  §7 "needs chord/function evidence" residual, not fabricated).
- **Not-carried** (true key never in the emitted alternatives) → coverage pile **E**, sub-split
  by whether `loc` appears *anywhere* in the piece's decode (E-pruning: a viable state locally
  outranked → L3 pruning) or never (E-emission: the emission never surfaces it → structural limit).

The distinguishing pc is computed as a **pitch-class collection difference** (parent-Ionian
collection of `correct` minus that of `picked`), so a relative pair / modal rotation correctly
yields an *empty* diatonic distinguisher (note-undecidable) and falls back to the chromatic
raised leading-tone (relative) or to F (rotation). Symmetry (dim7/aug/whole-tone) is detected on
the **slice** pcs only — a ±window accumulates enough pcs to make a dim7 subset appear by chance
(this correction collapsed a spurious window-based D pile of 112→4 Baroque / 47→1 Jazz).

---

## §2 — The partition (the deliverable), central cutoffs (Q2 ≥ 4 beats, Q3 weight > 0)

### Baroque — 2444 scorable misses (carried 1884 / 77.1 %; not-carried 560 / 22.9 %)
Q1 branch of carried: TRANSITION 204 · EMISSION 1680.

| pile | count | % of miss | meaning |
|------|------:|----------:|---------|
| **A** L3 emission-recoverable      | 1332 | 54.5 % | Q3 distinguishing pc present, underweighted |
| **B** L3 cost-recoverable          |  184 |  7.5 % | Q2 sustained over-smoothed modulation |
| **C** L5 cadence-required          |  202 |  8.3 % | Q2 brief tonicization ∪ Q3 absent relative-pair |
| **D** L5 chord/spelling-required   |    4 |  0.2 % | Q3 absent ∧ symmetric dim7/aug at slice |
| **F** L5 cause-indeterminate       |  162 |  6.6 % | Q3 absent, non-relative, non-symmetric / rotation |
| **E-pruning** coverage → L3        |  361 | 14.8 % | not-carried; loc IS a piece state (locally outranked) |
| **E-emission** coverage → limit    |  199 |  8.1 % | not-carried; loc never named for the piece |

### Jazz — 2657 scorable misses (carried 1911 / 71.9 %; not-carried 746 / 28.1 %)
Q1 branch of carried: TRANSITION 286 · EMISSION 1625.

| pile | count | % of miss | meaning |
|------|------:|----------:|---------|
| **A** L3 emission-recoverable      |  902 | 33.9 % | |
| **B** L3 cost-recoverable          |  251 |  9.4 % | |
| **C** L5 cadence-required          |  184 |  6.9 % | |
| **D** L5 chord/spelling-required   |    1 |  0.0 % | |
| **F** L5 cause-indeterminate       |  573 | 21.6 % | (Jazz modal rotations dominate — `AMixolyd`→`Dmaj` etc.) |
| **E-pruning** coverage → L3        |  520 | 19.6 % | |
| **E-emission** coverage → limit    |  226 |  8.5 % | |

### ★ The reconciliation that corrects the headline (the central result)

Pile **A** as graded (54.5 % / 33.9 %) is an **upper bound**, not the real L3 headroom. A binary
"distinguishing-pc present" test **cannot** tell a *key tone the emission underweighted* (true L3)
from an *applied / chromatic accidental in a brief tonicization* (L5) — and the spot-check
confirms this is not hypothetical. Cross-tabbing the L3 piles by the §1b stable-vs-modulation
(tonicization) axis:

| | A∩stable | A∩modulation | B∩stable | B∩modulation |
|---|---:|---:|---:|---:|
| Baroque | 242 | **1090** | 39 | 145 |
| Jazz    | 121 | **781**  | 75 | 176 |

**~82 % of pile A (Baroque) / ~87 % (Jazz) sits in modulation regions** — exactly the §1b
tonicization-boundary mass that needs function evidence. Only the **stable** subset is
unambiguously emission-reweighting headroom:

- **CLEAN L3 (A∩stable + B∩stable): Baroque 281 = 11.5 % of miss; Jazz 196 = 7.4 % of miss.**

This now agrees with the characterization §2 ("genuinely-wrong-resolvable ~7.4 % Baroque /
~4.6 % Jazz") instead of contradicting it: the inflated A pile was the §1b tonicization mass
re-entering through the present-pc test. **The real L3-recoverable headroom is ~7–12 % of misses,
not ~40–60 %.**

---

## §3 — Rigor: threshold sensitivity + manual spot-check

### Threshold sensitivity (per CC §3)

**Q2 sustained/brief cutoff → B (L3) vs C (L5) split of the TRANSITION mass:**

| cutoff | Baroque B / C-from-trans | Jazz B / C-from-trans |
|---|---|---|
| ≥ 2 beats | 202 / 2  | 282 / 4   |
| ≥ 4 beats | 184 / 20 | 251 / 35  |
| ≥ 8 beats | **83 / 121** | **148 / 138** |

The B/C boundary is **cutoff-sensitive**: at ≥ 8 beats (2 measures) roughly half of the TRANSITION
mass reclassifies from "sustained modulation" (L3) to "brief tonicization" (L5). So a material
fraction of TRANSITION cases live in the 1–2-measure band that is *itself* genuinely ambiguous
between an extended tonicization and a short modulation — a function-level call. The B pile is
robust only at the short (≤ 4-beat) cutoff; its upper reach is L5-contested.

**Q3 present-weight cutoff → A (L3) vs absent (L5) split of the EMISSION mass:**

| cutoff | Baroque A / absent | Jazz A / absent |
|---|---|---|
| > 0.0 qL | 1332 / 348 | 902 / 723 |
| > 0.5 qL | 1331 / 349 | 901 / 724 |
| > 1.0 qL | 1194 / 486 | 799 / 826 |

A is **robust** to the presence cutoff between 0 and 0.5 qL (it barely moves) and drops only ~10 %
at > 1.0 qL — i.e. where a distinguishing pc is present it is usually *strongly* present
(> 0.5 qL, a held tone, not a passing brush). **The distinguishing evidence really is in the
window; the uncertainty is purely interpretive** (key tone vs applied tone), which is precisely
why the stable/modulation reconciliation — not the weight cutoff — is what bounds real A.

### Manual spot-check (independently verified against the raw score, not the harness's own pc dump)

- **A · bwv11.6 m2 (`Dmaj`→`Amaj`, mod, dpc=G♯, w≈1.5):** the score's m2 pcs = {C♯,D,E,F♯,G♯,A,B}
  = *exactly* A-major content; G♯ (A's raised 7th) is held. The harness "present" is correct — yet
  GT marks the region a modulation, and full A-major content that GT reads as a tonicization of the
  dominant **cannot be told from a real key change by the notes alone.** This is the §3-anticipated
  finding: *on the modulation subset the A/C boundary is inherently L5* — which is exactly why the
  reconciliation excludes A∩modulation from clean L3. **Attribution sound; boundary correctly flagged
  as L5.**
- **D · bwv277 m5 (`Amin`→`Dmin`, stab, dpc=B♭, w=0, sym=dim7):** score m5 pcs = {C,D,E,F,G♯,A,B♮} —
  contains B♮, *not* B♭, so the D-minor distinguisher B♭ is genuinely absent (w=0), and G♯–B–D–F is a
  full diminished-7th at the slice. Notes cannot choose A-minor vs D-minor here; it needs chord
  identity / spelling. **Attribution sound (clean L5-chord case).**
- **B · bwv11.6 m10 (`Gmaj`→`Emin`, persist=16 b, corr 29.6 > pick 27.3):** the emission already
  preferred the relative minor and it persists 16 beats; only the relative-pair change cost (2.0) kept
  G major. Genuinely cost-recoverable — and note this *refines* §1b, which lumped all relative pairs as
  "note-undecidable": here the emission *did* decide, so it is L3, not L5.
- **F · bwv11.6 m4 Jazz (`AMixolyd`→`Dmaj`, kind=rotation, dpc=∅):** our reading is A-Mixolydian =
  the D-major collection; same collection, different chosen tonal center. No diatonic distinguisher
  exists — note-undecidable which center is tonic; needs function/cadence. **Correctly L5 (the Jazz
  rotation mass).**

**Spot-check agreement: 4/4 attributions confirmed against the score.** The one place the automated
classifier *cannot* settle A-vs-C without chord/function evidence (the A∩modulation tonicizations) is
reported as a finding, not papered over — which is the boundary the reconciliation cross-tab quantifies.

---

## §4 — What it implies (plain-language read)

**L3 sweep scope is small and mostly *selection*, not coverage.** The genuinely L3-recoverable
mass is **~7–12 % of misses** (CLEAN L3 = A∩stable + B∩stable: Baroque 281 / 11.5 %, Jazz 196 /
7.4 %) — emission-reweighting on stable regions where a *strongly-present* distinguishing pc was
out-scored, plus short sustained modulations the relative-pair / change cost over-smoothed. That is
the realistic ceiling for the later, separately-ratified sweep (a carried-alternative re-rank
and/or a gentle relative-pair-cost / emission-weight tune). It is **far below** the bare A-pile
54.5 % / 33.9 % headline, which is inflated by tonicization accidentals.

**The bulk of the residual is L5, dominated by the tonicization boundary.** Adding A∩modulation +
B∩modulation + C + D + F, the function-dependent mass is the majority of misses in both presets.
The **L5 spec** the downstream layer must supply is therefore: (i) **tonicization-vs-modulation
arbitration** (the largest single need — the A∩modulation + B∩modulation + Q2-brief mass; needs
cadence/function to decide whether a sounded secondary-dominant accidental opens a key area or just
tonicizes); (ii) **relative-pair / collection-rotation tonal-center selection** (C relative-pairs +
F rotations; needs a cadence/function cue to pick tonic among same-collection candidates — heavy in
Jazz); (iii) a small **chord-identity / spelling** need for symmetric sonorities (D — only ~0–0.2 %,
genuinely tiny in this corpus).

**Coverage (E) is real but mostly a pruning/output effect, not an emission wall.** Of the
not-carried misses, the larger share (E-pruning: 14.8 % Baroque / 19.6 % Jazz) names `loc` *somewhere*
in the piece's decode — it is a viable state outranked locally / dropped from this slice's emitted
top-alternatives, i.e. recoverable by a wider per-slice alternative output or top-K (an L3 pruning
lever). Only **E-emission (8.1 % / 8.5 %)** is a genuine emission/structural limit where the decoder
never surfaces the true key for the piece at all.
*Caveat:* the E sub-split is a proxy — the decode JSON carries only the emitted alternatives
(`maxAlternatives = 4`) + winner, not the full per-slice 252-candidate emission, so "pruning vs
emission" is measured at piece granularity (does `loc` appear anywhere) rather than by `loc`'s exact
per-slice emission rank. A precise pruning-vs-emission split would need the full emission dump
(a larger diagnostic than the §0 single field authorizes — surfaced, not built).

**Bottom line for "which layer":** the later L3 work should target the **~7–12 % clean set** (chiefly
a carried-alternative re-rank — the correct key is carried on 77 % / 72 % of misses) and optionally a
modest alternatives-output widening for the E-pruning share; it should **not** chase the A-pile
headline, most of which is the tonicization problem that belongs to L5. The L5 spec is dominated by
tonicization-vs-modulation arbitration and same-collection tonal-center selection, with only a
negligible symmetric-sonority chord-identity tail in this corpus.

---

## §5 — Deliverables / files
- **Committed (this increment):**
  - `tools/batch_analyze.cpp` — one additive `keyEmission` field on the `--decode-keymode` region
    JSON (diagnostic-only; §0).
  - `tools/cc_layer3_keymode_baseline.py` — `--decompose` mode (the Q1/Q2/Q3 tree, the A/B/C/D/F + E
    partition, the stable/modulation reconciliation, the §3 sensitivity + spot-check), reusing the
    Increment-B grading path.
- **Local/gitignored (not pushed):** this report; `tools/corpus_decode/` (regenerated with
  `keyEmission`); `/tmp/decomp.json` machine dump.

## §6 — Gate / constraint compliance
- Read-only; nothing wired; production analysis byte-identical (composing 596 / notation 57 /
  snapshots 11 + 1 skipped, no golden refresh; decode path returns before `analyzeScore`).
- No decoder setting changed or read for tuning (`topK` / window / costs / `uncertainThreshold` /
  `maxAlternatives` untouched).
- One grading path (extended `cc_layer3_keymode_baseline.py`; carried-rate reproduces the
  characterization's alternative-recall exactly).
- Symmetric-sonority / chord-identity need surfaced as a (small) L5 pile rather than fabricated; the
  E pruning-vs-emission split's granularity limit is stated, not hidden.
- `upstream` never targeted; push is `origin`-only.
