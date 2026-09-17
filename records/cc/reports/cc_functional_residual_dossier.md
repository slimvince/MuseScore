# Functional-Root Residual — the OQ-1 (A-vs-B) decomposition, RE-DERIVED on the corrected metric

*CC, 2026-06-14. **REPLACES the 2026-06-13 version, which was computed on the BUGGY parser
and is superseded in full.** Base = HEAD `bcd4319aa7` + the three STAGED/HELD corrected-parser
tool files (`tools/dcml_parser.py` blob `2db84ba9…`, `tools/compare_analyses.py` blob
`c27c7ddb…`, `tools/rerun_dcml_comparison.py`) — uncommitted, per the user's "report only"
decision (`cc_metric_rebaseline_report.md`). READ-ONLY measurement + classification: no build,
no commit, no behavior change. Corpus = `tools/corpus/default` (manifest git `bcd4319aa7`,
353/353), decomposed over its **326 WiR-rntxt-covered Bach stems** (10,108 three-way-scored
regions, 140 `no_dcml`). All drivers are throwaway `C:\tmp\*.py` reusing the committed metric
machinery verbatim (`compare_analyses`, `compare_rn`, `dcml_parser`) + music21 9.9.1
`roman.RomanNumeral`/`romanNumeralFromChord` as a read-only oracle. This file is the only repo
write.*

Evidence tags: **[probe]** ran a script, read output · **[oracle]** music21 9.9.1 ·
classifications are **sampled** (read N cases, hand-classified by a stated criterion) or
**inferred** (deduced from aggregate structure). Gates the OQ-1 ratification (`back_half_design`
§3: A = improve the hand-built emission + build a functional layer; B = learned model).

---

## §0 — Task 0: the headroom decomposition, re-derived on the CORRECTED metric

**Method validated by exact OLD-reproduction.** I built one driver (`task0_decomp.py`) and ran
it twice: with the staged corrected parser (= NEW), and with `tools/dcml_parser.py` +
`tools/compare_analyses.py` reverted to their HEAD blobs (= OLD, the gate-rebaseline-verify A/B
method — worktree reverted via `git restore --source=HEAD`, measured, restored; staged blobs
verified byte-identical `2db84ba9…`/`c27c7ddb…` before and after, unstaged diff empty) [probe].
**The OLD run reproduces the prior (stale) dossier EXACTLY** — root_err 2706, all_differ 2576,
m21-fixable 130, functional 95.2 %, S1 1791 — so the driver is the same instrument and the NEW
vs OLD deltas below are apples-to-apples.

### §0.1 — The three headline counts (NEW vs OLD)

| figure | OLD (buggy parser) | NEW (corrected) | Δ |
|---|---:|---:|---:|
| **root_err** (ours root ≠ DCML root, per-ours) | **2706** | **2365** | **−341 (−12.6 %)** |
| **all_differ** ("neither" — we≠DCML ∧ m21≠DCML) | **2576** | **2153** | **−423 (−16.4 %)** |
| **music21_dcml_agree** (m21-fixable; m21=DCML, we≠) | **130** | **212** | **+82 (+63 %)** |
| per-ours root_err rate (/10108 scored) | 26.8 % | 23.4 % | −3.4 pp |
| root_agree (all_agree + dcml_ours_agree) | 7402 | 7743 | +341 |

The `root_err = all_differ + music21_dcml_agree` identity holds both sides (2706 = 2576+130;
2365 = 2153+212) [probe]. A large share of the old "vertical" root error was a parser/alignment
artifact, exactly as the metric report's directional read predicted.

### §0.2 — The corrected functional-vs-vertical split (and how inflated the old 95.2 % was)

Operational definition (the headroom dossier's headline, = the "music21 gate sees X %" of
`back_half_design` §1): **functional = all_differ / root_err** (neither vertical analyzer reaches
DCML's root → DCML reads a functional root the sonority doesn't show); **vertical =
music21_dcml_agree / root_err** (a second *independent* vertical analyzer reaches DCML's root, so
a better vertical scorer would too).

| | OLD | NEW |
|---|---:|---:|
| functional % (all_differ/root_err) | **95.2 %** | **91.0 %** |
| vertical % (m21_dcml/root_err) | **4.8 %** | **9.0 %** |

**The old 95.2 % functional was inflated by ≈4.2 pp absolute; the vertical share nearly DOUBLED
(4.8 → 9.0 %)** [probe]. The de-inflation is mechanically explained in §0.3: the buggy parser
buried 365 already-correct cases + 75 genuinely-vertical-fixable cases inside `all_differ`,
mis-counting them as "functional residual."

### §0.3 — What the parser fix REMOVED vs what SURVIVES (the artifact split, set-diffed)

Set-diff of the `all_differ` identity sets (`stem@tick`) OLD vs NEW [probe]:

| | count |
|---|---:|
| OLD all_differ | 2576 |
| **dissolved by the fix (OLD-only)** | **440** |
| persisted (genuine functional residual, in both) | **2136** |
| newly added (NEW-only) | 17 |
| **NEW all_differ** | **2153** (= 2136 + 17) |

**Where the 440 dissolved cases went under the corrected parser** (`t0c_removed.py`, NEW
three-way category of each) [probe]:

| NEW category of the dissolved case | count | meaning |
|---|---:|---|
| `all_agree` + `dcml_ours_agree` (→ root-agree) | **365** | **pure ARTIFACT — we were already correct**; the WiR-rntxt parser had mis-rooted the GT (applied / minor-LT) |
| `music21_dcml_agree` | **75** | **revealed VERTICAL-fixable** — m21 was already right, the bug had hidden it in all_differ |

**This confirms the prior (buggy-parser) dossier's two predicted numbers to the case: it
estimated "366 artifact (ours already correct)" and "75 VERT_FIXABLE the parser artifact had
hidden" — the corrected parser dissolves 365 to agreement and surfaces exactly 75 as vertical**
[probe]. So ≈17.1 % of the OLD 2576-region "functional residual" was bogus (365 artifact + 75
mis-attributed), and the genuine functional residual is the **2136 survivors (+ 17 new) = 2153**.

### §0.4 — Within the corrected residual, the two vertical analyzers still agree (94.1 %)

Inside NEW all_differ (2153), **m21 == ours in 2025/2153 = 94.1 %** (OLD 92.1 %) [probe]. In 94 %
of the corrected residual the two *independent* vertical analyzers produce the **same** root and
DCML differs — the signature of a non-vertical (functional) DCML reading **or** a defensible
ambiguity, not a vertical-scoring bug (those are the now-separated 212).

### §0.5 — S1 tonicization recount (NEW vs OLD)

`kd_eq_global` (key_disagree where our tonic+mode == DCML *global*, ≠ local): **1791 → 1885
(+94)** [probe]. It grew because the corrected WiR roots produce more root-agreements, shifting
some former root_err cases into root-correct/key-disagree, of which the eq_global (tonicization)
subset absorbed +94.

### §0.6 — Rider: `analyze_inversion_errors.py` re-measured under the corrected parser

The OLD `bassIsRoot` three-way `music21_dcml_agree` genuine split (24/13 Baroque · 35/7 Jazz) was
stale/pending. Corrected [probe]:

| preset | OLD (true / false) | NEW (true / false) | total |
|---|---|---|---:|
| Baroque | 24 / 13 | **47 / 57** | 37 → 104 |
| Jazz | 35 / 7 | **81 / 23** | 42 → 104 |

The BIR=**false** halves (57, 23) match the re-baselined gate exactly (CLAUDE.md/STATUS.md:
Baroque 57 / Jazz 23). The loose end is closed: the secondary `bassIsRoot` metric moved as a
strict superset, same correction as the gate.

---

## §1 — Task 1: S1 tonicization is rule-reachable (confirmed on the corrected metric)

S1 = 1885 (§0.5). **Sampled 10/10 are mechanical tonicizations** [probe, criterion: our root ==
WiR root ∧ our key == WiR global ∧ the chord is exactly the tonic/dominant of the WiR *local*
area, which is a diatonic tonicization target of the global key]; root-pc match within all of S1
is **1885/1885 = 100 %** (by construction — key_disagree requires root agreement):

| case | ours | WiR (local→global) | mechanism |
|---|---|---|---|
| bwv10.7@960 | VII6, root F, Gmin | V6/III, root F, g | our root **is** the V-of-III, only the label differs |
| bwv155.5@1920 | v, root C, Fmaj | ii, local Bb, g.F | C = tonicized ii (Bb area), root+global correct |
| bwv244.3@14880 | VI, root G, Bmin | IV, local D | G = IV-of-D tonicized |
| bwv302@17760 | VI, root B, Dmaj | V, local e | B = V-of-e tonicized |
| bwv391@1920 | IV, root C, Gmaj | I, local C | C tonicized |
| bwv44.7@12000 | vi, root G, Bbmaj | i, local g | g tonicized |

**Verdict: S1 reachable by emission + KeyArea (Stage 4) + a mechanical secondary-labeler (Stage
6) — HIGH confidence.** The comparator already credits the `V/x` label once emitted. It is the
single largest reachable functional slice and is *root-and-global-key-already-correct* (a
pure-add label).

---

## §2 — Task 2: the corrected "neither" residual (all_differ = 2153), three-way decomposed

### §2.1 — Mechanical proxy sizing (priority partition, hard counts) [probe]

`task2_size.py` over the 2153 NEW all_differ records (each carries our reading, m21 root, WiR
root+label+local/global key, our pcs, WiR-root-in-pcs, and our prev/next-region roots):

| proxy bucket | criterion | count | % |
|---|---|---:|---:|
| **NHT_HELD** | WiR root == our prev- or next-region root (we over-segment a held harmony) | 906 | 42.1 % |
| **CAD64** | WiR root == our bass ≠ our root (I64-over-^5 → V shape) | 69 | 3.2 % |
| **DROOT_PRESENT** | WiR root IS a tone in our sonority (we picked another root) | 345 | 16.0 % |
| **DROOT_ABSENT** | WiR root NOT in our sonority, not held | 833 | 38.7 % |

Cross-cuts: applied (`wir_label` has `/`) = 264; WiR-root-present total = 790. Δ=(our−WiR)
distribution is **classic-functional**: +7 (V-for-I) dominates at 508, then +5 (321), +2 (318),
+3 (270), +10 (217) [probe].

### §2.2 — Hand-classification into the three OQ-1 buckets (sample n=44, 38 stems)

Stratified sample (NHT_HELD 14, DROOT_ABSENT 14, DROOT_PRESENT 10, CAD64 6), each read with our
reading + DCML chord+local/global key + our pcs + flanking-region roots [probe]. Buckets &
criteria:

1. **RULE-REACHABLE** — DCML's root is derivable by a hand-built functional/key/segmentation rule
   (cadential-6-4: I64-over-^5→V; suspension/NHT/passing where the held root is read correctly in
   a neighbor; applied/secondary = the V/LT of the next root; key/relative = same RN *degree*,
   root differs only by the key).
2. **NEEDS-RICHER-MODEL** (the B-trigger) — correct root needs sequence/phrase context **no clean
   rule captures** AND it is not merely ambiguous/noise. *State why a rule can't reach it.*
3. **GENUINE-AMBIGUITY / CONVENTION / NOISE** — DCML's reading is one of several defensible
   (criterion: would a 2nd competent annotator plausibly write our reading, or is the disagreement
   alignment/granularity noise?) → ceiling for **everyone, including B**.

**Result of the 44-case read:**

| bucket | strict count | criterion that placed it |
|---|---:|---|
| **B2 — needs-richer-model** | **0 / 44** | *no* case was simultaneously (a) un-reachable by a key/NHT/cad/applied/segmentation rule, (b) not a metric artifact, (c) not genuinely ambiguous/alignment-noise |
| B1 — rule-reachable (strict) | 11 / 44 (25 %) | cad64 (bwv121.6), suspension-over-V/iv with root present (bwv10.7, bwv340, bwv315), NHT/passing in a held harmony (bwv304, bwv437), key/relative same-degree (bwv245.40 V=V, bwv126.6 V6=V6, bwv180.7 I=I), known Stage-target (bwv261 Δ=+7a) |
| B3 — ambiguity / convention / noise | 33 / 44 (75 %) | inversion/added-6th (D6≡Bm7 bwv190.7), dim7/7th-rotation (bwv278 C#ø7≡Em7), share-tone viio↔V7 (bwv190.7), aug6 representational gap (bwv351 It6), sparse 1–2-note (bwv392 {C}, bwv267 {D,F#}), and **"ours reads the actual notes, DCML root absent"** alignment/defensible cases (bwv101.7, bwv296, bwv366, bwv436 …) |

**The B1/B3 boundary is soft and dominated by how NHT_HELD over-segmentation is dispositioned**
(segmentation-rule-reachable vs annotation-granularity-ceiling) — exactly the axis the prior
dossier and `cc_gate_rebaseline_verify_report` §2.3 flagged as unsplit. **Both dispositions route
away from B2**, so the OQ-1 verdict is insensitive to it. Generous accounting (count NHT_HELD +
CAD64 over-segmentation as segmentation-reachable, plus the key/applied/suspension subset of the
present/absent strata) lifts B1 toward ~55 % — matching the prior dossier's 50.7 % reachable.

### §2.3 — Extrapolated three-way split (population-weighted, sampled · MED confidence)

Per-stratum B1 rates from the sample (NHT 4/14, CAD64 1/6, PRESENT 3/10, ABSENT 3/14) weighted by
the §2.1 population sizes:

| bucket | strict est. | generous est. (over-seg = rule) |
|---|---:|---:|
| **B1 rule-reachable** | ≈ 550 (**26 %**) | ≈ 1180–1270 (**~55–59 %**) |
| **B3 ambiguity / convention / noise** | ≈ 1600 (**74 %**) | ≈ 880–970 (**~41–45 %**) |
| **B2 needs-richer-model** | **≈ 0** (0/44 sampled; rule-of-three corpus upper bound **~6.8 %**) | same |

The decisive figure is **B2 ≈ 0**. The two estimates of the B1/B3 line bracket the soft
over-segmentation disposition; in **both**, the residual is rule-reachable + ambiguity/noise, with
**no populated needs-a-learned-model bucket**.

---

## §3 — Task 3: literature calibration + the music21-RN probe

**music21's *vertical* RN analyzer fails the functional roots exactly as we do** — direct,
read-only evidence that bucket 1 is a functional-*layer* problem, not a vertical-scorer problem.
`roman.romanNumeralFromChord(chord, key)` on four bucket-1 sonorities [oracle]:

| case | pcs / key | music21 vertical RN | DCML functional root | reached? |
|---|---|---|---|---|
| cad64 bwv121.6 | {D,F#,B} / b | `i6` (root B) | V (F#) | **no** |
| susp bwv340 | {C,D,F,G} / C | `ii542` (root D) | V6/5 (G) | **no** |
| susp bwv10.7 | {C,F,Bb} / Bb | `i74` (root Bb) | V (F) | **no** |
| NHT-held bwv304 | {D,F#,G,B} / D | `IV43` (root G) | I (D) | **no** |

0/4 reached — music21 returns the literal sonority root, like us. Meanwhile `roman.RomanNumeral`
(the notation→root direction) gets every DCML figure right (it is the §0 oracle, 99.97 %
corpus-wide) — so the DCML labels are well-formed functional analyses, and the residual is
unreachable by *any* vertical scorer (the corpus-scale version is the §0.4 m21==ours 94.1 %).

**Published-system calibration** (`cowork_target_architecture_review.md` §2.2–2.3, §5 [doc]):
- **Rule-based functional analyzers — Temperley/Melisma (Viterbi DP + ornamental-dissonance/NHT
  preference rules), Pardo & Birmingham HarmAn (template scoring + global segmentation)** — target
  precisely bucket 1: cadential context, applied dominants, suspensions/NHT, and segmentation.
  Bucket 1 (CAD64 + NHT_HELD + applied/secondary + key) is the classic rule-based-functional
  domain → a **hand-built** Stage-6 functional layer reaches the reachable part = **A**.
- **Neural systems — AugmentedNet/ChordGNN/RNBert (~45–50 % full-RN vs our ~27 % rn_agree)
  [doc].** Their advantage is *full-RN* joint label optimization on harder repertoire — they push
  into **bucket 3** (defensible-label disambiguation) and the harder non-Bach corpora, not into a
  root-axis mass a rule provably cannot reach. RNBert's *decoder* is the CRF/lattice already built;
  the *gain* is the learned emission, which matters only if a measured ceiling appears — and on
  this axis it has not.

---

## §4 — Task 4: the OQ-1 verdict input

**Recommendation: ratify A (hand-built emission + functional layer); B is NOT triggered — and the
corrected metric STRENGTHENS A vs the buggy one.** The bug had inflated the apparent "functional"
mass with 365 already-correct artifacts + 75 mis-attributed vertical cases; removing them leaves a
cleaner 2153-region residual that decomposes into rule-reachable + ambiguity/noise with an
**empty** needs-richer-model bucket (0/44 sampled). The loud stop-condition ("bucket 2 dominating →
flip OQ-1 to B") **did not fire.**

| slice | size (corrected) | A reaches? | B beats A here? |
|---|---:|---|---|
| metric artifact (we were already correct) | 365 (dissolved) | **already done** | no — nothing to beat |
| vertical-fixable (m21 right, we wrong) | 212 (130 + 75 revealed) | yes (Stage 5 emission) | no advantage shown |
| **S1 tonicization** (root+global correct, label-gap) | **1885** | **yes** (Stage 4 KeyArea + Stage 6 labeler) | no — pure-add label |
| rule-reachable functional residual (bucket 1) | ≈ 550–1180 | yes (Stage 4/5/6) | no advantage shown |
| ambiguity / convention / alignment-noise (bucket 3) | ≈ 970–1600 | partially (ties) | **no — ceiling for B too** |
| needs-richer-model (bucket 2, the B-trigger) | **≈ 0** (<~7 % bound) | maybe not | maybe — but empty |

**The three sizes the instruction asks for:**
- **Total hand-built-reachable functional headroom = S1 (1885) + bucket 1 (≈550–1180) + the
  already-reached artifact correction (365).** The dominant, addressable mass; the biggest single
  piece (S1) is a pure-add label on already-correct readings.
- **Everyone-ceiling (bucket 3) ≈ 970–1600** — defensible inversion/rotation/added-tone +
  aug6 convention + sparse + **alignment noise**. A perfect model (incl. B) cannot uniquely match
  DCML here. A lenient-alignment audit would *shrink* this (the noise share is not a real ceiling),
  which only **strengthens** A.
- **B-differentiated mass (bucket 2) ≈ 0** (sampled 0/44, corpus upper bound ~7 %) — too small to
  justify B's cost (explainability loss + DCML training dependency).

**Confidence.** The §0 partition (root_err / all_differ / m21-fixable / artifact-365 / vertical-75
/ S1-1885) is corpus-wide, mechanical, oracle-cross-checked, and reproduces the OLD numbers
exactly → **HIGH**. The bucket-2-is-empty conclusion (the OQ-1 hinge) is **sampled (44 cases),
MED-HIGH**: robust because B2 would have to hide inside the uncertain residual, and *every*
sampled hard case resolved to a hand-built rule, a defensible ambiguity, or alignment noise —
never to "a learned model uniquely gets this and a rule can't." The B1-vs-B3 magnitude is the
softest number (MED) but **both readings route away from B**, so the verdict is insensitive to it.

**Consequences for the back half** (reinforce the ratified order, `back_half_design` §4):
1. **Stage 4 (key) first** is even better-justified: S1 (1885) + the key/relative slice of bucket
   1 are the two largest reachable masses and both are KeyArea-gated.
2. **The metric fix is now a prerequisite, not optional, before Stage-5 fitting** — fitting against
   the *old* gate would have optimized against 365 phantom errors and 75 mis-labeled vertical
   errors. The corrected parser (this base) closes that; it must be committed before fitting.

---

## §5 — Unknowns / what couldn't be cheaply pinned

1. **The B1↔B3 boundary inside NHT_HELD (906) / the over-segmentation slice** is the softest split
   — segmentation-rule-reachable vs annotation-granularity-ceiling. Not auto-tallied (no
   functional ground-truth oracle to mechanize "the right segmentation"). Both dispositions are
   non-B; the *magnitude* of B1 (26 % vs ~55 %) turns on it, not the verdict.
2. **Alignment-noise vs genuine-disagreement inside DROOT_ABSENT (833)** is not separated. Many
   sampled DROOT_ABSENT cases are "ours reads the actual notes, DCML root not even in the sonority"
   — a mix of real defensible disagreement and time-overlap alignment artifacts. This **inflates
   B3** with non-musical noise; a lenient-alignment audit would shrink the everyone-ceiling and
   strengthen A. Unmeasured here.
3. **Bach WiR-rntxt only.** The decomposition is the `tools/corpus/default` Bach gate corpus. The
   non-Bach TSV corpora (corelli/mozart/chopin/…) use the corrected applied-root path but the
   minor-LT artifact's recurrence there and their functional-vs-ambiguity split are unmeasured (no
   `.music21.json` for ABC/Beethoven — headroom dossier §4.3).
4. **Sample is n=44, stratified-not-proportional.** Population-weighting was applied for §2.3 but
   the per-stratum B1 rate rests on 6–14 cases each (MED). A larger labeled read would tighten the
   B1/B3 magnitude (not the B2≈0 verdict).
5. **The music21-RN probe is 4 cases** — illustrative of the vertical→functional gap, not a
   corpus-scale measurement (the corpus-scale version is the §0.4 m21==ours 94.1 %).
6. **Pedal points** are not separately detected (a subset of DROOT_ABSENT where a sustained bass ≠
   the harmony); none were obvious in the sample. Sizing needs a pedal detector (Stage 6 scope).

---

*Drivers (throwaway, untracked, `C:\tmp\`): `task0_decomp.py` (NEW/OLD three-way + S1 recount),
`task0b_dump.py` (per-case all_differ records + identity sets), `task2_size.py` (proxy sizing +
stratified sample), `t0c_removed.py` (NEW category of the dissolved 440), `t1_s1_new.py` (S1
sample). OLD numbers obtained by the gate-rebaseline-verify A/B revert (HEAD blobs → measure →
restore staged, byte-identity verified). music21 9.9.1 used read-only as a root oracle. This
dossier is the only repo write.*
