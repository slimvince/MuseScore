# CC primary audit — `jointkeydecision.cpp` (LAYER AUDIT #3, READ-ONLY)

> Phase-1 per-layer isolation audit (`docs/layer_audit_plan.md` §3). **CC = primary auditor
> (empirical).** North star: BEST = CORRECT vs the DCML oracle, not a proxy gate. The audited
> producer is the **committed J-key-i strong-signature-backbone** (dormant commit `5fee657578`,
> flag OFF). **No production/inference/behavior change** — findings only.
>
> **Measurement is FRESH and authoritative.** Cowork's figures (`cowork_audit_jointkeydecision.md`)
> were `[prov]`; this dossier states which I confirm vs correct. **Headline: every `[prov]` number
> reproduces — two essentially to the decimal, one with a sign-flipped near-zero.**

---

## §0 — Empirical method (reproducible)

- **Object audited:** the source on disk — `jointkeydecision.{h,cpp}` is **unmodified** (committed at
  `5fee657578`). `localmodulationdetector.cpp` (which `decideJointKey` calls via
  `detectLocalModulations`) and `tools/batch_analyze.cpp` carry working-tree edits (the B2
  subdominant-guard diagnostic). **Verified inert on the audited path:** the B2 guard's `guardSuppresses`
  is `jointKeyWiringEnabled() && …`; the `--dump-joint-key` diagnostic does **not** set the wiring flag,
  so `detectLocalModulations` returns the full unguarded span set — byte-identical to the committed
  baseline. **Confirmed empirically:** a fresh `--dump-joint-key` of `bwv10.7` (Baroque) produced a
  `jointKey` block **byte-identical** (sorted-JSON compare) to the existing `tools/corpus/baroque_jki_re`
  dump (2026-06-15). The `_jki_re` corpora therefore validly measure the current committed strong-backbone
  producer.
- **Instruments (committed, unchanged):** `tools/cc_j_key_i_measure.py` over the three per-preset
  joint-key corpora `tools/corpus/{baroque,default,jazz}_jki_re` (353 stems each, 326 DCML-aligned). It
  aligns every region to DCML via the *same* committed machinery the residual probe uses
  (`compare_analyses` / `dcml_parser` / `compare_rn`, verbatim). Plus two supplementary tallies I ran
  inline (jointChanged footprint; per-stem home-fifths violation). **No production output moved.**

---

## §1 — Responsibility (the contract)

**`decideJointKey(regions, keySignatureFifths, weights) → JointKeyResult`** — the **constrained-joint KEY
decision** (dormant): per analysis region, decide `(tonic, mode)` by combining **soft, key-agnostic
evidence** over a **global key-path Viterbi** on a pruned lattice, with an optional **scoped chord×key
joint** on the coupled core. It emits *both* a config-A (soft-only) and config-B (soft+joint) decision per
region for attribution.

**This is the SYNTHESIS layer — CONFIRMED, with one precision.** It consumes the *evidence* produced by the
other key-axis layers: the cadence anchor + modulation spans (`cadencekeyanchor` / `localmodulationdetector`,
via `detectLocalModulations`), the `analyzeKeyMode` local candidates (`keymodeanalyzer` / `keyresolver`,
as a soft prior), the chord alternatives (`chordanalyzer`), plus bass and the declared-mode notation fact.
**Precision:** it does **not** consume the resolver's *resolved key* — that is carried only as `prodTonicPc`
(echoed comparison reference, never read; the documented no-circularity property, header §⛔). So it
synthesizes the upstream **evidence** layers, not the resolver's *output*.

**Single-responsibility?** The decision itself is cohesive. Two notes for phase 2 (not obligations here):
(a) the TU also **owns the production-wiring flag** (`setJointKeyWiringEnabled` / `jointKeyWiringEnabled`) —
a thin toggle, but it is the seam J-key-iii flips; (b) the working-tree B2 guard in
`localmodulationdetector.cpp` keys its suppression off **this** layer's `jointKeyWiringEnabled()` (a back-
reference from the modulation layer into the joint layer's flag) — a cross-layer coupling to flag for phase 2.

---

## §2 — Correctness / decision quality vs DCML (MEASURED)

All three configs scored against the DCML oracle (correct = matches DCML local key, or global when local
unknown; S1 = matches global but local differs; S2 = genuine error). Key-accuracy = correct / (correct+S1+S2).

| preset | config | scored | correct | S1 | S2 | key-acc |
|---|---|---|---|---|---|---|
| Baroque | prod | 10119 | 5566 | 3035 | 1518 | 55.0% |
| Baroque | soft | 10119 | 5920 | 2777 | 1422 | **58.5%** |
| Baroque | joint | 10119 | 5906 | 2772 | 1441 | 58.4% |
| Default | prod | 10109 | 5556 | 3021 | 1532 | 55.0% |
| Default | soft | 10109 | 5940 | 2777 | 1392 | **58.8%** |
| Default | joint | 10109 | 5936 | 2775 | 1398 | 58.7% |
| Jazz | prod | 9788 | 4544 | 2104 | 3140 | 46.4% |
| Jazz | soft | 9788 | 5742 | 2612 | 1434 | **58.7%** |
| Jazz | joint | 9788 | 5736 | 2612 | 1440 | 58.6% |

### 2.1 — The SOFT re-rank WIN — **CONFIRMED to the decimal**

| | Δ key-acc soft−prod | Δ S2 soft−prod | `[prov]` | verdict |
|---|---|---|---|---|
| Default | **+3.80 pp** | **−140** | +3.80 / −140 | ✅ exact |
| Baroque | **+3.50 pp** | **−96** | +3.50 / −96 | ✅ exact |
| Jazz | **+12.24 pp** | **−1706** | +12.24 / −1706 | ✅ exact |

**[the WIN — correct, key-axis].** Integrating note + cadence + modulation + bass + declared-hint + a global
Viterbi path beats production on every preset. The Jazz lift is enormous (+12.24 pp, S2 −1706) because the
shipped Jazz resolver is far off the oracle and the broad soft evidence is style-robust. This is the layer's
load-bearing positive result.

### 2.2 — ★ The scoped JOINT is INERT — **CONFIRMED and STRENGTHENED**

| joint − soft | measured | `[prov]` | verdict |
|---|---|---|---|
| Default | **−0.04 pp** | +0.04 | ✅ magnitude exact; **sign corrected** (+0.04 → −0.04) |
| Baroque | **−0.14 pp** | −0.14 | ✅ exact |
| Jazz | **−0.06 pp** | −0.06 | ✅ exact |

The scoped chord×key coupling moves the key decision by **≈0 pp** — and in fact **net slightly NEGATIVE** on
every preset (joint S2 *worse* than soft by +19 / +6 / +6). **Strengthening evidence I add:** the joint
decision differs from soft in only **0.23% / 0.29% / 0.16%** of regions — **26 / 33 / 17 regions across the
entire 353-score corpus** — and those few moves do not net-help. So the joint search is not merely inert; on
this corpus it is a **tiny net drag**.

**Conclusion — the META-PRINCIPLE is confirmed:** the win is the **SOFT broad-evidence integration**, NOT the
joint search. Precision on the key axis lives in **evidence breadth + calibration**, not in a chord×key
lattice search. The single most decision-relevant number for the eventual fix — *is the constrained-joint
combination the key-axis lever?* — answers **no; the soft evidence integration is.**

**The one [prov] correction** (Default joint−soft +0.04 → −0.04) does not change the conclusion: it moves the
increment from "marginally positive" to "marginally negative," i.e. *more* firmly inert. (The flip is a few
regions out of 10k; well within run-to-run framing.)

### 2.3 — Non-chorale / inherited-cadence regression (qualitative — CONFIRMED in aggregate)

The soft win is a **net**: per-case adjudication (joint≠production, §4.4 of the instrument) shows it is not
free — Baroque 739 wins vs 399 losses, Default 768/388, Jazz 2079/887. The **losses** are the cadence-anchor
inheritance Cowork flagged (I→IV/I→V over-detection → over-commit to subdominant/dominant on non-chorale; the
J-key-iii snapshot regressions). Net positive, but the loss column is the upstream-cadence-precision debt
surfacing here — **not separately fixable in this layer** (its inputs are the noise). This is the upstream
obligation, terminating here.

---

## §3 — Hard-constraint safety + completeness (MEASURED)

### 3.1 — The home-fifths HARD pin unsafe rate — **CONFIRMED at BOTH grains**

| | region rate | per-stem | `[prov]` |
|---|---|---|---|
| Baroque | 17.0% (1034/6073) | **56** / 325 | ~17% / 56 stems |
| Default | 17.0% (1032/6073) | **56** / 325 | — |
| Jazz | 17.2% (1012/5873) | **56** / 325 | — |

At DCML key-**stable** regions, the notated home-signature fifths ≠ the DCML global fifths **17%** of the
time. The `[prov]` "17% / 56 stems" conflated two grains; I confirm **both**: the **region** rate is ~17%,
and exactly **56 distinct stems** carry ≥1 such region (identical 56 across all three presets — it is a
property of the signature↔DCML relationship, preset-invariant). These are partial/modal (e.g. Dorian)
signatures whose fifths cannot represent the DCML key — **structurally excluded** by the hard home-pair
prune, the documented/ratified ceiling that **matches production** (production is itself locked to the
notated signature; header §6a/§7). The single hard constraint on the key axis is **17%-unsafe**, and the
J-key-ii soft-demotion that relaxed it was measured **not separably safe** (it shrank the soft win).

### 3.2 — The candidate "pinned-chord ⊆ key collection" hard constraint — UNSAFE, correctly left SOFT

At chord-pinned regions, the pinned chord has a note **outside** the DCML local collection **14.0% / 14.0% /
13.9%** of the time (953/6822, 949/6801, 950/6843). A hard "prune any key the pinned chord isn't diatonic to"
would therefore **discard the correct key 14% of the time** (secondary dominants, applied chords, chromatic
passing). **CONFIRMS** the design decision to leave this evidence SOFT (`couplingScore`, header step 4; §3/§7
demotion). It is correct that this is not a veto.

### 3.3 — Completeness gaps (vs the case space)

- **[completeness · key-axis] Home-pair lattice excludes non-signature keys.** The lattice is `{home major,
  home minor} ∪ committed modulation-span states` — never all 24. The 17%/56-stem partial-signature ceiling
  (§3.1) is the direct consequence; measured not separably recoverable.
- **[completeness · key-axis] Modulation de-masking floor.** Among DCML modulation regions (local≠global),
  correct *local-key* placement: prod 9.8/10.2/17.2% → **soft 17.2/16.9/18.8%** → joint ~same. Soft roughly
  **doubles** Baroque/Default modulation recovery, but the absolute floor is still **~17–19%** — the layer
  inherits the cadence/modulation imprecision (K1) and cannot place most modulations. Large completeness gap,
  upstream-rooted.
- **[completeness · key-axis] Relative-pair (mode) recovery.** Among same-signature regions, mode-correct:
  prod 78.6/78.2/80.2% → **soft 81.9/81.7/81.5%**. Soft buys +1–3 pp of relative-major/minor disambiguation
  (the global/cadential evidence overcoming the scorer's relative-pair limit K2), but a **~18% mode-error
  floor** persists. The K2 limit is **partly** overcome by the soft combination — the load it must carry —
  not eliminated.
- **[completeness · scope] Coupled-core size — DESIGN-CLAIM DISCREPANCY.** The design/`[prov]` claims the
  coupled core (chord-ambiguous AND key-ambiguous) is **~13.5%**; I measure **23.8% / 23.7% / 21.1%** — the
  instrument's coupled scope is **~1.6–1.8× the documented figure**. Worth reconciling (the design's 13.5%
  may have used a tighter coupling definition than `coupledV` here: `!chordPinned && keyAmbiguous` with a
  ±1-region span dilation). **It does not change the verdict** — even on a coupled core ~1.7× larger than
  designed, the joint search still moves only 0.2% of regions and nets negative (§2.2). If anything it
  *strengthens* the inertness finding.

---

## §4 — Gaps → obligations (tagged)

1. **[correctness · key-axis · fix: behavior-changing → deferred]** **The joint SEARCH is the wrong lever;
   invest in soft evidence quality + calibration.** Joint−soft ≈ 0 (net slightly negative; 0.2% of regions).
   The eventual fix should not pursue the chord×key lattice/search — it should improve the **soft emission
   evidence** (cadence precision, modulation recall, calibrated weights). *Highest-value obligation: it
   redirects the whole inference reopen.*
2. **[correctness · key-axis · fix: UPSTREAM, behavior-changing → deferred]** **The cadence-anchor I→IV/I→V
   over-detection** is inherited as the soft win's loss column (§2.3) and as the modulation de-masking floor
   (§3.3). Fix in `cadencekeyanchor` / `localmodulationdetector` (K1), not here. This is the convergence:
   upstream cadence precision is the root.
3. **[correctness · key-axis · fix: structural-OR-calibration → deferred]** **The home-fifths hard pin is
   17%-unsafe (56 stems).** A confident-contradiction signal (a cadence-vote-for-home, currently unbuilt) or
   a learned/calibrated emission could recover partial-signature keys, but the blunt soft-demotion was
   measured to shrink the win. Needs calibration, not relaxation.
4. **[completeness · key-axis · fix: behavior-changing → deferred]** **Modulation placement floor ~17–19%**
   and **mode-recovery floor ~18%.** Both are upstream-input-bounded (K1 cadence/modulation; K2 relative-
   pair). The soft combination is the partial remedy; the residual is the honest floor until the inputs
   improve.
5. **[scope · fix: documentation/structural — possibly now]** **Coupled-core scope ~21–24% vs documented
   ~13.5%.** Reconcile the `coupledV` definition against `docs/scoped_joint_design.md`'s 13.5% claim — a
   measurement/definition drift to resolve (no behavior change; the joint is inert regardless).
6. **[architecture · phase-2 note]** The B2 subdominant-guard (working tree, `localmodulationdetector.cpp`)
   keys suppression off **this** layer's `jointKeyWiringEnabled()` — a modulation-layer→joint-layer flag
   back-reference. Flag for the phase-2 composition review (seam direction).

---

## §5 — Reconciliation summary (vs `cowork_audit_jointkeydecision.md`)

| Cowork `[prov]` claim | My fresh measurement | Verdict |
|---|---|---|
| Soft win +3.80/+3.50/+12.24 pp; S2 −140/−96/−1706 | identical to the decimal | **CONFIRM (exact)** |
| Joint INERT +0.04/−0.14/−0.06 pp | −0.04/−0.14/−0.06; net slightly negative; moves 0.2% of regions | **CONFIRM** (Default sign corrected +0.04→−0.04; conclusion strengthened) |
| Home-fifths pin wrong ~17% / 56 stems | 17.0/17.0/17.2% regions; **56** stems exactly | **CONFIRM (both grains)** |
| Candidate chord⊆key constraint unsafe → left soft | 14.0/14.0/13.9% would-prune-correct | **CONFIRM** |
| Non-chorale regression (inherited cadence noise) | loss column 399/388/887 in the net soft win | **CONFIRM** |
| This is the convergence layer; the three obligations terminate here | obligations 1–4 all upstream/calibration-rooted, surfacing here | **AGREE** |

**Net:** I confirm Cowork's audit in full. The **one correction** is cosmetic (Default joint−soft sign flip,
near-zero) and *reinforces* the central finding. **Single most decision-relevant result:** the constrained-
joint *combination* is the key-axis lever **only via its SOFT evidence integration** (+3.5–12.2 pp); the
joint *search* is inert (≈0, net-negative, 0.2% footprint). Precision lives in evidence breadth +
calibration, not search.

Read-only; no production/inference/behavior change. Cowork verifies methodology at the committed object +
reconciles; user ratifies.
