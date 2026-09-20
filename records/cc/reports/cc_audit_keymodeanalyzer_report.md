# CC primary audit — `keymodeanalyzer.cpp` (LAYER AUDIT #4, READ-ONLY) — closes the KEY AXIS

> Phase-1 per-layer isolation audit (`docs/layer_audit_plan.md` §3). **CC = primary auditor (empirical).**
> North star: BEST = CORRECT vs the DCML oracle, not a proxy gate. **No production/inference/behavior
> change** — findings only. Cowork's note (`cowork_audit_keymodeanalyzer.md`) + the map's K2 reconcile.
>
> **Measurement is FRESH and authoritative.** ⚠ Cowork already corrected one mechanism claim at source
> this session (the disambiguation is NOT wholesale inert — clauses 3/4 resolve the one-incomplete-triad
> sub-case); this dossier **confirms that correction AND sizes it**, and corrects a stale stat in Cowork's
> own note (#1 below).

---

## §0 — Empirical method (reproducible)

- **Object:** `src/composing/analysis/key/keymodeanalyzer.cpp` (832 lines) — `analyzeKeyMode` + the six score
  terms + `applyPairwiseDisambiguation` + `tonalCenterScore` family selection. The TU is **unmodified at
  HEAD**; this session's working-tree edits (`localmodulationdetector.cpp`, `batch_analyze.cpp`) do not touch
  it nor the standard `.ours.json` `key` field — **verified**: a fresh `bwv10.7` Baroque regen reproduces the
  corpus `key` fields exactly.
- **Instruments:**
  1. `tools/cc_kma_relpair_probe.py` (committed locally this session) — aligns every region to DCML via the
     *same* committed machinery (`compare_analyses` / `dcml_parser` / `compare_rn`, verbatim) and measures the
     relative-pair error, the pcMask-replay structural floor, and the 21-mode mis-win.
  2. Fresh **mode-absent** corpora (`--ignore-declared-mode`) regenerated this session at HEAD
     (`tools/corpus/{baroque,default,jazz}_kma_abs`, 353/353, manifest-stamped) — isolates the declared-mode
     crutch. (The pre-existing `_4bi` corpora were **stale** — 45/54 regions differ on `bwv10.7` — so they were
     NOT used; that staleness is itself harmless to production, which is byte-identical.)
- **The pcMask replay** reconstructs `applyPairwiseDisambiguation`'s decision inputs from the region
  `pitchClassSet` (a 12-bit mask): for the DCML-local signature's relative pair — relative-**major** tonic
  `Tmaj` (Ionian) and relative-**minor** tonic `Tmin = Tmaj+9` (Aeolian) — whether each member's **tonic** and
  **complete triad** (tonic + 3rd + 5th) are present. This mirrors `scoreTriadEvidence`'s `weight>0.1` test
  (a pc in the mask sounded ⇒ weight>0) at region granularity, stated as a proxy. It models the **canonical
  relative pair**, which is the top-2 the disambiguation actually compares in the common case (see §2.2).
- **No production output moved.** Mode-absent regen is the read-only `--ignore-declared-mode` diagnostic.

---

## §1 — Responsibility (the contract)

**`analyzeKeyMode(pitches, keySignatureFifths, prefs, declaredMode, dumpOut) → KeyModeAnalysisResult[]`** —
per-region **key-mode scoring**. Enumerate **252 candidates** (12 tonics × 21 active modes); score each =
`scaleScore + triadScore + keySignatureScore + characteristicPitch + trueLeadingTone + modePrior`, minus the
`−declaredModePenalty` (1.0) for modes outside the declared class (4b-i); apply `applyPairwiseDisambiguation`
to the **top-2 same-signature modes by raw score**; select via the focused `tonalCenterScore` family
comparison (with a raw-score guard against modal-tie overrides); rank top-3; emit sigmoid confidence from the
top-1/top-2 gap. **One responsibility (key-mode scoring) with many evidence sub-terms — not a conflation.**
CONFIRMED, matching Cowork.

---

## §2 — Correctness vs DCML (MEASURED, all 3 presets)

### 2.1 — The RELATIVE-PAIR error (K2) — the central limit, quantified

Among regions whose DCML local key is tonal and our pick shares its signature (the relative-pair decision):

| preset | prod (declared hint) mode-correct | **note-only** (mode-absent) | declared-hint crutch |
|---|---|---|---|
| Baroque | 78.5% (err 21.5%, 1515) | **68.0%** (err 32.0%, 2162) | rescues net +647 |
| Default | 78.5% (err 21.5%, 1504) | **68.1%** (err 31.9%, 2151) | rescues net +647 |
| Jazz | 79.6% (err 20.4%, 937) | **68.2%** (err 31.8%, 1277) | rescues net +340 |

**The note-only relative-pair error is ~32% on every preset** — the scorer, on local notes alone, picks the
wrong relative ~1-in-3 times. The declared-mode hint recovers ~10 pp (to ~21%). **K2 is real and dominant**,
confirming Cowork #1.

**Reconciling the `[prov ~1383]` flip figure** (regions that flip without the declared crutch): I measure
**2467 / 2381 / 1081** relative-pair regions *change* pick prod↔note-only (Baroque/Default/Jazz), of which
the declared hint **rescues 1631 / 1583 / 793** (correct→wrong when removed) but also **hurts 753 / 750 /
268** (wrong→correct when removed — the hint is not free). The `[prov] ~1383` is the same phenomenon at the
**old (pre-2026-06-13) parser**; my corrected-parser figure for the declared-rescued count is **1631
(Baroque)**. **I confirm the direction and order of magnitude; I update the point estimate to 1631 / 2467-changed.**

### 2.2 — ★ The disambiguation-scope correction (Cowork CORRECTED at source) — CONFIRMED **and SIZED**

Source (`keymodeanalyzer.cpp:455-487`) confirms the corrected reading: `applyPairwiseDisambiguation` is **NOT**
wholesale inert on tonic-present-both. Its clauses:
- **cl. 1/2** (463-470): one side complete-triad+tonic, the other **no tonic** → boost/penalty.
- **cl. 3/4** (476-481): **both tonics present, exactly one complete triad** → boost the complete side (the
  Em/G opening). **This is the case Cowork's note (line 18) wrongly called inert.**
- **cl. 5/6** (482-487): one tonic present, other absent → small tonic bonus.

It is provably inert **only** on **both-tonic-present AND both-complete-triad** (no clause's guard holds).
**How big is each band?** (pcMask replay on the relative pair, prod corpus):

| band | Baroque | Default | Jazz | disambiguation status |
|---|---|---|---|---|
| **BOTH_COMPLETE** (genuine floor) | **4.2%** (424) | **4.3%** (433) | **3.0%** (297) | provably INERT — notes can't separate |
| ONE_COMPLETE (cl. 3/4 fire) | 16.3% (1654) | 16.4% (1659) | 16.3% (1591) | **decidable** — 72.7/72.7/73.4% point to DCML |
| TONIC_ASYM (cl. 1/2/5/6 fire) | 36.5% | 36.4% | 37.3% | decidable by tonic asymmetry |
| NEITHER (no complete relative triad) | 43.0% | 42.9% | 43.4% | weak local evidence |

**Finding — the genuinely-unresolvable-from-notes relative-pair floor is SMALL (~3-4%).** Cowork's correction
is confirmed and sized: the disambiguation **is** active on the 16% ONE_COMPLETE band and points the right way
~73% of the time. **The reframe that matters:** the 21-32% relative-pair *error* is NOT mostly the
both-complete-triad tie (4%); it is dominated by **TONIC_ASYM (~37%) + NEITHER (~43%)** regions — where the
local region simply **does not contain a decisive relative triad at all** (sparse / non-tonic-chord regions).
There the per-region note evidence is thin and the scorer leans the wrong way; the correct reading must come
from **cross-region context (cadence / global / declared)**, not the local notes. So **K2 is a "most regions
lack decisive local evidence" floor, not a "both triads tied" floor** — which is *exactly* why the joint
layer's SOFT broad-evidence integration (K3, measured the lever in audit #3) is the resolution, and why K2 is
**not reweightable within this layer**.

### 2.3 — 21-mode mis-win — measured NEGLIGIBLE

Among tonal DCML-local regions, our pick is a genuine **church/exotic** mode (Dorian/Phrygian/Lydian/
Mixolydian/Locrian/altered) only **0.1% / 0.1% / 0.4%** (14 / 13 / 21 regions). The suffix breakdown shows
**no** Dorian/Phrygian/Lydian/Mixolydian/Locrian wins at all — the only non-major/minor picks are harmonic
minor (`har`) and melodic minor (`mel`), which are **minor-class** (mode-class-correct for a minor key, not
mis-wins). **`modePrior` + same-signature-family selection contain the 21-mode richness effectively** — the
risk Cowork flagged (#2) is real in principle but **does not materialize** (~0.1%). Downgrade from "real risk"
to "contained; negligible in practice."

### 2.4 — `scoreKeySignatureProximity` partial-sig mis-anchor (the Dorian wall) — CONFIRMED structural

Source (411-420): the term penalizes candidates by circle-of-fifths distance from the **notated** signature.
On partial/modal signatures whose true key's signature ≠ notated (Dorian etc.), it **anchors to the wrong
signature** and penalizes the correct key. This is the same population the joint audit (#3) measured: **~17% of
key-stable regions / exactly 56 stems** where notated home fifths ≠ DCML global fifths (and the standing
memory `project_key_detection_baroque_partial_signature`). **Confirmed; not separately re-measured** (identical
population). Structural, foundational — production is itself locked to the notated signature.

---

## §3 — Completeness gaps

- **[completeness · key-axis] Cannot complete the relative decision from local notes.** §2.1/§2.2: ~32% note-
  only error, with the decisive evidence absent locally in ~80% of relative-pair regions (TONIC_ASYM+NEITHER).
  Needs external cadential/global evidence — confirmed.
- **[completeness · key-axis] Disambiguation scope is top-2 only** (601-621): only the two highest raw-scoring
  same-signature modes are compared. In the common case those are the relative major (Ionian) + relative minor
  (Aeolian) — so the canonical relative pair *is* compared — but a region where a third same-signature mode
  out-scores one relative could leave the true relative un-disambiguated. Low-incidence (church modes ~never
  win, §2.3), but a structural scope limit, not a bug.
- **[completeness · key-axis] Per-region scoring over a lookahead window** → window-local coupling (Cowork #5);
  modulation handled per-region but window-coupled. Confirmed by inspection; not separately measured here.

---

## §4 — Gaps → obligations (tagged)

1. **[correctness · key-axis · fix: behavior-changing → deferred] K2 is the note-evidence floor; NOT
   reweightable here.** Note-only relative-pair error ~32%; the decisive local evidence is absent in ~80% of
   relative-pair regions. No reweighting of `scaleScore`/`triadScore`/`trueLeadingTone`/disambiguation can
   manufacture evidence the region doesn't contain. **Resolution is the joint layer's SOFT integration of
   cadence + global evidence (K3, audit #3's measured lever) + upstream cadence precision (K1).** This is the
   convergence the four key-axis audits independently re-derive.
2. **[correctness · partial-sig · fix: structural → deferred] `scoreKeySignatureProximity` Dorian wall.**
   Anchors to the notated signature; mis-anchors the ~17%/56-stem partial/modal-signature population (shared
   with #3's home-pin). Structural; needs a signature-agnostic or graded-prior treatment (a later Stage-4 step).
3. **[correctness · key-axis · fix: structural — possibly now] Disambiguation top-2 scope.** Document/verify
   the rare case where a third same-signature mode displaces a relative from the top-2 (low incidence). No
   behavior change implied; a completeness note.
4. **[no-op] 21-mode mis-win is contained (~0.1%).** No obligation — `modePrior` + family selection suffice;
   recorded so a future reopen does not "fix" a non-problem.

---

## §5 — Reconciliation summary (vs `cowork_audit_keymodeanalyzer.md` + the map's K2)

| Cowork / `[prov]` claim | My fresh measurement | Verdict |
|---|---|---|
| Relative-pair = dominant key-S2 class; note-only frequently wrong | note-only err ~32% all presets; declared hint −10pp | **CONFIRM** |
| `[prov] ~1383 floor regions flip without declared crutch` | 2467 change; 1631 declared-rescued (Baroque, corrected parser) | **CONFIRM direction; update estimate to 1631 / 2467-changed** |
| Disambiguation **inert on the tonic-present-both floor** (note line 18) | inert ONLY on both-complete-triad (**4.2%**); cl. 3/4 actively resolve the 16.3% one-incomplete band, 73% correctly | **Cowork's source-correction CONFIRMED + SIZED; note line 18 is STALE — corrected here** |
| 21-mode richness a "real risk" (#2) | genuine church/exotic mis-win **~0.1%**; no Dorian/Mix/etc. wins | **CONFIRM mechanism; downgrade to negligible-in-practice** |
| `scoreKeySignatureProximity` mis-anchors partial-sig (#3) | same 17%/56-stem population as audit #3's home-pin | **CONFIRM** |
| Each key-axis layer insufficient alone → joint combination is the obligation | K2 floor is "no decisive local evidence" (≥80% of relpair errors), not a reweightable tie | **AGREE — strengthened** |

**Net:** I confirm Cowork's audit. **Two corrections, both at the mechanism's *size*:** (a) the genuinely-
unresolvable relative-pair floor is **small (~4%)** — most relative-pair error is *missing local evidence*,
not a *symmetric tie* (this sharpens K2 and is the strongest single result); (b) the 21-mode risk is real in
principle but **negligible in practice (~0.1%)**. The disambiguation is **not** wholesale inert (Cowork's own
source-correction), and Cowork's note line 18 ("clauses fire only when the relative's tonic is ABSENT") is the
stale claim, corrected here. **K2 closes the key axis: the note scorer cannot complete the relative decision,
and the deficit is structural (missing local evidence), resolvable only by the joint SOFT integration (K3) +
upstream cadence precision (K1) — not by reweighting this layer.**

Read-only; no production/inference/behavior change. Probe + fresh mode-absent corpora are diagnostics. Cowork
verifies methodology + reconciles; user ratifies.
