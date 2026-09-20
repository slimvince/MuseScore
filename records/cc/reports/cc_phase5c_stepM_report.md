# CC Report — Phase 5c Step M: the read-only L5 (FUNCTION) measure + the engage GO/NO-GO

**Scope.** A MEASUREMENT, not an engage. The dormant Layer-5 (FUNCTION) build (Steps 0–6 +
the A-D2 follow-up) is byte-identical by construction; Step M answers: **if we engaged L5,
what would change against the DCML ground truth, per case, signed — and does it pass the
two-tier BIR gate?** No production movement, no tuning, no inference fix, no legacy-path
retirement, no engage. Spec: `cowork_layer5_function_design.md` (SIGNED) §5.6/§7; gate
policy: `CLAUDE.md` two-tier BIR. **You (CC) measure and recommend; Cowork verifies and the
user ratifies the engage.**

**Headline.** **GO** on the two-tier gate: **zero new class-(b)** and **zero new class-(a)**
on all three presets (the L5 relational layer is ADDITIVE — it never moves a committed root
pc), the BIR root gate stays byte-identical **53 / 24 / 53** (same case identities), and the
RN accuracy vs DCML **improves** **+2.48 / +1.91 / +2.32 pts** (Baroque / Jazz / Default).
Two quality caveats declared to Cowork (neither trips the gate): a `V/iv`-on-tonic applied
**over-trigger** (12 / 6 / 13 cases) and the **tonicization-vs-modulation** residual the
§5.4 modulation recompute (not on this substrate) targets.

---

## §0 — Preamble (sweep + STATUS)
Working tree was clean at session open (no unstaged Cowork docs pending — the §5.6 amendment
rode with `9bd60a063b`; `scratch_artifacts/` is gitignored scratch). STATUS.md session-15
opening entry committed: **`449f19fbd5`** (`docs(status): open Phase-5c Step M …`).

---

## §1 — INVESTIGATE-confirm (read-only) — NO STOP

**(a) A diagnostic path CAN invoke the dormant L5 over a score and dump its would-be labels,
with NO production consumer.** Confirmed by source:
- `assembleFunctionOutput` / `classifyRelationalLabel` / `functionrelationallabel` /
  `functionoutput` have **zero** `src/` consumers outside their own module + unit tests
  (grep), and **zero** `tools/` consumers before this step — fully dormant.
- `tools/batch_analyze.cpp` already carries the **exact default-OFF diagnostic-flag
  precedent** (`--section-level`, `--dump-tonicization`, `--dump-cadence-anchor`,
  `--dump-modulation`): a flag that *appends* a read-only key to the regions JSON, default
  OFF ⇒ byte-identical, never wired into the production notation pipeline. batch_analyze is a
  `tools/` measurement binary, **not** the production notation path — so adding a dormant-L5
  dump flag is measurement, not engage. **No production wiring is required → NO STOP.**

**(b) Substrate decision (declared build-decision).** The dormant L5 units are
producer-agnostic / hand-injectable; to run them over a score the harness must feed them a
committed-chord + key stream. Two substrates exist:
- the **L4-decoder** substrate (`--decode-chords` `SliceChord`) — carries the per-slice
  carried-reading contract the resolver/override needs, BUT runs on a single score-level key
  (no per-region L3 key, no phrase boundaries) and is a **separate** engage (Phase-5b, already
  measured); driving the full spine there would conflate the L5 delta with the
  decoder-vs-legacy (L4) delta;
- the **legacy region** substrate (`AnalyzedRegion`) — the **SAME** chord + key source as the
  53/24/53 BIR gate baseline (`r.chord.identity` + `r.key` + `r.tones` (tpc) + `r.pcMask` =
  exactly `classifyRelationalLabel`/`assembleFunctionOutput`'s inputs).

**Chosen: the legacy region substrate** — it isolates the L5-attributable delta on the exact
substrate the production gate is measured on, and is proportionate (`classifyRelationalLabel`
is one call per region; `assembleFunctionOutput` is pure assembly). **What this substrate does
NOT exercise** (declared, not a defect): the §5.5 resolver/fine-grain **override** and the
§5.4 **modulation recompute** consume the L4-decoder carried contract / the local-modulation
substrate, which the legacy region path does not carry — so on this substrate L5 is the
**relational-label + cadence/key annotation** layer, which is **ADDITIVE over L4 (§7) and
root-preserving** (the override is the ONLY L5 root-mover, and it is inert here). This makes
the class-(b) gate measurable by construction and keeps the harness diagnostic-only.

**(c) Reuse map (confirmed, no re-implementation):**
| need | reused tool | entry |
|---|---|---|
| RN equivalence / credit vs DCML | `compare_rn.py` | `classify_pair`, `score_regions` (categories exact/partial/key_disagree/quality_disagree/root_err) |
| oracle-correct GT roots/RNs | `dcml_parser.py` | `find_wir_file`, `parse_rntxt_file` (When-in-Rome Bach) → `DcmlRegion.root_pc`/`chord_symbol` |
| region↔GT alignment | `compare_analyses.py` | `load_analysis`, `align_dcml_regions` (50% time-overlap) |
| two-tier BIR gate | `characterise_bir_false.py` | `validate_corpus_dir` + `run` (`--corpus-dir`) |
| per-preset regen | `run_bach_preset.py` | `--preset … --output-dir …` (353 scores, manifest-stamped); `--dump-l5` pass-through added |

The would-be L5 RN is fed through `compare_rn` exactly as the production RN is: it is the same
`Region.roman_numeral` field (the L5 stream is the same regions with `roman_numeral` replaced
by `classifyRelationalLabel.label`, via `dataclasses.replace`).

---

## §2 — The measurement harness (diagnostic-only, default OFF, NO production consumer)

**`batch_analyze --dump-l5`** (new, default OFF), mirroring `--dump-tonicization`:
- New `writeL5Json(regions, globalKey, out)` reads the analyzed `regions` and, per region,
  builds the `RelationalLabelInput` from `r.chord.identity` + `r.key` + the next committed
  root + `r.tones` tpcs + `r.pcMask`, runs **`classifyRelationalLabel`** (Step 5), assembles a
  `FunctionUnitAssembly`, and calls **`assembleFunctionOutput`** (Step 6, §7) over the score's
  units — dumping per unit: the would-be L5 RN (`romanNumeral`, carried verbatim by the §7
  assembly), the relational `role`, the `openMark`, the echoed committed `rootPitchClass`, the
  **unguarded inline `formatRomanNumeral` baseline** (`inlineRomanNumeral`, the §5.6
  applied-divergence comparator), and `nextRootPc`. Appended as a top-level `"l5"` array.
- Threaded as `dumpL5` (declaration / arg-parse `--dump-l5` / both `writeJson` call sites /
  help text); `run_bach_preset.py` gains a `--dump-l5` pass-through.
- The dormant L5 **never** feeds any production output; L5 is additive (the committed root is
  echoed unchanged). Files: `tools/batch_analyze.cpp`, `tools/run_bach_preset.py`.

**Build-gate (this build itself):**
- composing **972 PASSED**, notation **53 PASSED** (4 skipped baseline), pipeline_snapshot
  **11/11 — NO golden refresh** (independently proves P1–P4 byte-identity; the test binaries
  were not even rebuilt — only `tools/batch_analyze.cpp` changed).
- **Corpus 53 / 24 / 53 unchanged — case-identity SETS IDENTICAL** to the canonical dirs on
  all three presets (`characterise_bir_false.py` on `--dump-l5` regen vs canonical; diff of
  the `stem@tick` BIR=false sets is empty on Baroque/Jazz/Default).
- **`regions[]` deep-equal across all 353 stems** between the canonical and the `--dump-l5`
  dir (the canonical has no `l5` key, the dump dir has it) — the flag is **purely additive**;
  the default-OFF path is byte-identical on production. **No production movement.**

---

## §3 — The would-be-engage delta vs DCML (all three presets, per case, signed, two-tier)

Measured by `tools/cc_stepM_l5_measure.py` over the `--dump-l5` regen (326/353 stems carry a
When-in-Rome annotation; 27 have none and are never scored against human GT).

| metric | **Baroque** | **Jazz** | **Default** |
|---|---|---|---|
| matched GT regions | 10119 | 9780 | 10113 |
| rn_agree LEGACY (production RN) | 53.9% (5452) | 52.2% (5109) | 53.8% (5437) |
| rn_agree **L5** (would-be RN) | **56.4%** (5703) | **54.2%** (5296) | **56.1%** (5672) |
| **would-be-engage rn_agree Δ** | **+2.48 pts (+251)** | **+1.91 pts (+187)** | **+2.32 pts (+235)** |
| exact (legacy → L5) | 4132 → 4133 (+1) | 3873 → 3880 (+7) | 4127 → 4125 (−2) |
| root_agree (legacy / L5) | 76.7% / 76.7% (**+0**) | 77.0% / 77.0% (**+0**) | 76.6% / 76.6% (**+0**) |
| L5 changed the RN string at | 536 units | 490 units | 518 units |
|  — improves | 311 | 267 | 298 |
|  — regresses | 62 | 79 | 63 |
|  — neutral | 163 | 144 | 157 |

**★ The two-tier classification (the GO criterion).** L5 on this substrate is ADDITIVE — the
committed root pc is **never moved** (verified per case): **root pc MOVED by L5 = 0** and
**NEW root_err (legacy ok → L5 root_err) = 0** on **all three presets**. Therefore:
- **class-(b) signed delta = 0** (no pitch-class-decidable root read wrong by L5) — **GO
  criterion met.**
- **class-(a) signed delta = 0** (L5 touches no symmetric-rotation root either).
- The entire L5 delta is **RN-string (label) change, root-orthogonal** — it can only move a
  unit between exact/partial/key_disagree/quality_disagree, never into root_err. This is
  class-(b)-neutral **by construction** and is confirmed empirically per case.

**Relational-role census (per unit).** Baroque None 9234 / **AppliedSecondary 702** /
**ModalMixture 312** / Neapolitan 9 / AugmentedSixth 2; Jazz 9059 / 611 / 239 / 9 / 1;
Default 9227 / 696 / 320 / 7 / 2.

**Improvement structure (dominant — 311/267/298).** Almost entirely **AppliedSecondary**
(287/246/286): L5 emits a secondary-dominant / applied label DCML agrees with where the
production region RN had the wrong degree, e.g. (Baroque) `IV(key_disagree) → V/VII(partial)
[DCML V]`, `II6(key_disagree) → V/V(partial) [DCML V6/V]`, `I6 → V/iv(partial) [DCML V6/iv]`,
`III(key_disagree) → V/vi(partial) [DCML V]`; plus a few mixture/spelling fixes
(`biø65 → viiø65 [DCML viio6]`).

**Regression structure (62/79/63) — TWO classes, both root-unchanged (class-(b)-neutral):**

1. **Tonicization-vs-modulation artifact** (role None: **47 / 72 / 48**). L5's §5.6 foreign-tone
   guard correctly refuses to call a **fully-diatonic** chord "applied" → emits the diatonic
   numeral (e.g. `VII65`, `iiø65`), but **DCML modulated** and writes the same root as a
   dominant in the new key (e.g. `V6/5`, `viio6`). The legacy `V7/III` only scored "partial"
   by coincidence (same root, both "V"); L5's theory-correct diatonic numeral scores
   quality_disagree against DCML's modulated reading. **These are KEY-LEVEL disagreements, not
   chord errors** (root identical) — the **§5.4 modulation recompute** is exactly what would
   re-read these in the new key; it is not on this (legacy) substrate, so they surface as
   RN-string regressions here. Example (g-minor, B♭=III tonicized): `bwv10.7@4320`
   `legacy=V7/III → L5=VII65, DCML=V6/5` — F-rooted F-major-7 is fully diatonic to g minor, so
   the guard is right that it is *not* an applied chord; DCML reads the passage as a modulation
   to B♭ and writes V6/5.

2. **Applied OVER-TRIGGER** (role AppliedSecondary: **12 / 6 / 13**, ALL `legacy=I → L5=V/iv`,
   `DCML=I`). A **plain diatonic tonic** before a `iv` chord is mislabeled `V/iv`. Cause: the
   reused dormant `tonicizationlabeler` (called first inside `emitAppliedLabel`) fires
   `isApplied` on the `I→iv` root motion and `emitAppliedLabel` returns **before** the §5.6
   foreign-tone guard runs (the guard would reject it — `I` is fully diatonic). **This is a
   genuine L5 label over-trigger** — declared to Cowork below (§8). Root unchanged
   (class-(b)-neutral). Case identities (Baroque): `bwv26.6@11040, bwv265@7200, bwv279@3360,
   bwv301@3840, bwv323@17280, bwv345@11040, bwv358@19200, bwv40.8@25920, bwv403@8640,
   bwv412@22560, bwv425@30240, bwv87.7@19200`.

---

## §4 — The deferred items, AS MEASUREMENTS (read-only; nothing changed)

**(1) The two applied-label divergences (`V7/III` on diatonic `bVII7→III`; `viio/III` on
diatonic `ii°→III`) — does DCML side with the §5.6 GUARD (reject → diatonic) or the legacy
INLINE path (emit applied)?** Measured as the cases where the unguarded inline emits an applied
label but the §5.6 guard rejects it (→ L5 diatonic):

| preset | divergence cases | **DCML sides with the GUARD** (diatonic) | DCML sides with INLINE (applied) |
|---|---|---|---|
| Baroque | 78 | **72 (92%)** | 6 |
| Jazz | 114 | **103 (90%)** | 11 |
| Default | 82 | **76 (93%)** | 6 |

**The §5.6 foreign-tone guard is the DCML-correct call in ~90–93%.** DCML reads these
fully-diatonic chords diatonically (`viio6`, `V`, `I6`, `V7`, the plain `VII`), agreeing with
the guard's rejection — the legacy unguarded inline path's `V7/III` / `viiø7/III` over-emission
is wrong there. The 6/11/6 residual where the inline path was right are genuine tonicizations
DCML *did* apply (e.g. `bwv16.6@960` DCML `viio6/III`; jazz `bwv148.6@17760` DCML `V6/5/V`) —
these are the same tonicization-vs-modulation continuum, recoverable by function/cadence
context (the §5.4/§5.5 layers, not this substrate). **Engage-time verdict: keep the §5.6
guard** (it is the DCML-aligned call); the small inline-right residual is a precision-phase
refinement, not a guard reversal.

**(2) The Inherit class-(b) override coverage (61 Commit / 25 Inherit, the §5.5/§10 duty).**
This is a **DECODER-substrate (L4)** measurement, not a legacy-substrate one. Provenance:
`cc_phase5b_stepM_measure_report.md` §1 measured **86 projected class-(b) cases (61 Commit /
25 Inherit)** as the **L4-decoder's own transient commits** — "engaging L4-alone is **−5.9 vs
legacy with 86 class-(b) regressions**"; L5's fine-grain override is the mechanism that
**fixes** them. On the **legacy region substrate** (this Step-M measurement, = the current
production gate) there are **no L4 abstains / carried alternatives**, so the resolver/override
is **inert** and contributes **zero** class-(b) (confirmed: §3 root-moved = 0). **Therefore the
Inherit-vs-Commit override-extension question is a DECODER-engage (Phase-5b) measurement, not an
L5-relational-engage gate** — it must be re-measured on the decoder substrate when L4 engages
(if a residual Inherit class-(b) remains after the Commit-override + cascade, broaden the
override to {Commit, Inherit}; the design note already provides for this). Not gating the L5
relational layer.

**(3) The `kEstablishmentMinChords` modulation floor (= 5).** Measured over the corpus via the
existing `--dump-modulation` substrate (`tools/corpus/default_mod`, 353 scores): **867 committed
local-key spans**, of which **429 are non-home modulation candidates** (all cadence-confirmed
by construction), in **273/353 scores**. **247 spans sit exactly at the floor**
(`establishmentChords == 5`; **151 of them non-home** — the marginal admits a floor of 6 would
drop). The establishment-length histogram declines from the floor (5:247, 6:171, 7:107, 8:89,
…). **Reach is substantial** — the §5.3 hysteresis decides which of the 429 candidates become
modulations, and those modulations are exactly what would re-read the **47/72/48 None-role
regressions** (§3) toward DCML. **The Step-4 build's open Step-M check** ("does the floor ever
*reject* a real short modulation the hysteresis would have admitted?") needs a **floor-sweep**
(re-dump at floor 4/3 and diff the new spans against DCML local-key changes) — not done here
(it is a deeper investigation, and the floor is a *candidate pre-filter* the §5.3 hysteresis
sits above); recorded as a residual for Phase B. The committed-floor reach itself is the
quantification above.

**(4a) Pinned region-reduction content (§15-3 pin, Step 4).** The pinned region-level
key-alternatives reduction has **no production consumer** (read only by the lock-in test +
`inheritRegionKeyContext`'s plumbing copy; the joint re-key is gated OFF). **Measured
production effect: zero** — byte-identical (Step-4 report; re-confirmed this step by the
`regions[]` deep-equal across 353 stems, §2). Nothing to reconcile at this substrate.

**(4b) Minor-key mixture scope.** `tryModalMixture` fires the **chromatic-root** mixture in all
keys (bVI, bIII, bVII…) but the **quality-altering** mixture only in Ionian keys (the
documented scope — iv-in-major). Measured: ModalMixture role fires **312 / 239 / 320** units;
Neapolitan **9 / 9 / 7**; AugmentedSixth **2 / 1 / 2**. The minor-key quality-mixture cases are
carried as role None with the **formatter's correct numeral** (the LABEL string is always
right; only the *role tag* is conservative), so the scope limit does **not** affect the RN-vs-
DCML measurement (it is a role-annotation completeness item, not an RN error). Recorded; no RN
impact.

---

## §5 — GO / NO-GO

| | **Baroque** | **Jazz** | **Default** | criterion |
|---|---|---|---|---|
| **class-(b) signed Δ** | **0** | **0** | **0** | ≤ 0, non-increasing → **PASS** |
| **class-(a) signed Δ** | **0** | **0** | **0** | small wobble → **PASS** |
| net BIR case-identity changes | none (53) | none (24) | none (53) | sets identical → **PASS** |
| RN-agree vs DCML | +2.48 pts | +1.91 pts | +2.32 pts | net improvement |
| applied-divergence verdict | guard 72 / inline 6 | guard 103 / inline 11 | guard 76 / inline 6 | DCML backs the §5.6 GUARD ~92% |
| declared label caveat | V/iv over-trigger ×12 | ×6 | ×13 | class-(b)-neutral; pre-engage fix |

**RECOMMENDATION: GO** for engaging the L5 **relational-label + annotation** layer on the
current (legacy region) production substrate. It **passes the two-tier gate** — **zero new
class-(b)** and **zero new class-(a)** on every preset (additive, root-preserving), the BIR
root gate stays byte-identical 53/24/53 (identical case identities), and RN accuracy vs DCML
**improves** on every preset; the §5.6 applied guard is the DCML-aligned call in ~92%.

**Conditioned on Cowork's call on two declared items (neither trips the gate):**
1. **The `V/iv`-on-tonic over-trigger (12/6/13)** — a real RN-label regression from the reused
   `tonicizationlabeler` firing before the §5.6 foreign-tone guard. A clean pre-engage label
   fix (route the labeler's output through the same foreign-tone guard, or move the guard
   ahead of the labeler call) would remove it. It is an **inference/labeler fix → out of Step
   M's scope** (declared, not done).
2. **The tonicization-vs-modulation residual (47/72/48 None-role regressions)** is the §5.4
   **modulation recompute**'s job; engaging the relational layer **without** the modulation
   layer leaves these as root-neutral RN-string regressions. The full L5 spine (modulation
   layer) is on a different substrate (the decoder / per-region recompute) and is the natural
   companion engage.

**Scope note for Cowork (you hold the engage plan, I don't).** This GO is for **L5-relational-
on-the-production-substrate**. If "engage L5" means **stacking L5 on the L4 decoder** (the full
new spine), then the **86 decoder class-(b) cases (61/25)** from Phase-5b are in play and must
be gated on the **decoder** substrate (the override's effectiveness there) — that is a Phase-5b
/ decoder-engage measurement, **out of this Step-M-as-measured scope**, surfaced here so the
two readings are not conflated.

---

## §6 — Constants
**No tuning, none.** Step M measured the dormant build at its default constants. One constant
flagged for **Phase B** (recorded, NOT changed): the `tonicizationlabeler`'s applied trigger
lacks the §5.6 foreign-tone guard for the `I→iv` case (the over-trigger, §3/§5/§8). No
threshold, weight, or gate was altered.

---

## §7 — Deliverables + shas
- **`449f19fbd5`** — `docs(status): open Phase-5c Step M …` (the §0 STATUS opening entry).
- **Harness commit (this delivery)** — `tools/batch_analyze.cpp` (`--dump-l5` +
  `writeL5Json`), `tools/run_bach_preset.py` (`--dump-l5` pass-through), and the measurement
  harness `tools/cc_stepM_l5_measure.py` (force-added; `tools/cc_*` is gitignored, but
  load-bearing cc_ harnesses are tracked by precedent — `cc_layer3_*`). **No production
  movement.** Sha recorded in STATUS at delivery.
- This report `cc_phase5c_stepM_report.md` (gitignored).
- Measurement evidence (gitignored scratch): `scratch_artifacts/stepM_l5_measure.txt` (the
  full per-case dump), `scratch_artifacts/char_*_l5m.txt` (the 53/24/53 gate + identity diff),
  `scratch_artifacts/sm_*.txt` (the suites).

**Verification handles for Cowork.** The harness is diagnostic-only (production byte-identical:
suites green, snapshot 11/11 no-refresh, `regions[]` deep-equal across 353 stems, BIR identity
sets identical). The measurement is against **DCML** (When-in-Rome via `dcml_parser` +
`compare_rn`), not self-graded. The two-tier classification is **per-case verified** (root-pc
moved = 0; new root_err = 0; the over-trigger and modulation-artifact classes enumerated with
case identities). The GO/NO-GO follows the gate (class-(b) ≤ 0).

---

## §8 — Declared findings / non-actions (for Cowork; nothing changed in production)
1. **L5 applied OVER-TRIGGER `V/iv` on a diatonic tonic (12/6/13 cases).** Root cause: the
   reused `tonicizationlabeler` (inside `emitAppliedLabel`) fires `isApplied` on the `I→iv`
   root motion and returns before the §5.6 foreign-tone guard; the guard would reject it (`I`
   is fully diatonic). An **inference/labeler fix**, not Step M's job — **DECLARED, not fixed.**
2. **Tonicization-vs-modulation residual (47/72/48).** The §5.6 guard is theory-correct (a
   diatonic chord is not applied) but DCML resolves the same passages as **modulations**; the
   **§5.4 modulation recompute** (not on this substrate) is the recovery path. Not a chord
   error (root identical). Declared as the natural companion to a relational-only engage.
3. **The class-(b) override duty (86 = 61 Commit / 25 Inherit) is a DECODER-substrate (Phase-5b)
   concern**, inert on the legacy substrate; the Inherit-extension question must be re-measured
   when L4 engages. Declared so the L5-relational GO is not read as clearing the decoder gate.
4. **STOPS honored:** no production movement, no threshold tuning, no inference fix, no legacy-
   path retirement, no engage switch (that is Phase 5d, after Cowork verifies + the user
   ratifies). `upstream` untouched.
