# CC Report — Stage 4b-ii: strengthen note-based relative-pair inference (structural-sufficiency test)

**Date:** 2026-06-14 · **Status:** HELD — **NO commit, NO production weight change proposed** (the
finding is that none is shippable) · **Base:** committed 4b-i (`6e3351e695`) · **Build:** clean, all
suites green. Implements `docs/stage4b_design.md` §5 (4b-ii) per the 4b-ii CC instruction.
Every number tagged `[probe]` (measured), `[code]` (read at source), `[oracle]` (DCML/music21 checked).

This run answers the **load-bearing question**, not "make the number better": **can the existing
note-based structure, with better weights, carry the relative-major/minor decision — or is a new
mechanism needed?** The answer, measured below across all three instruction-named levers, is: **the
existing structure cannot.** Every lever either does nothing to the floor or buys floor only by
regressing the shippable mode-present condition. That is the structural-sufficiency verdict (§5), and it
is the input to the OQ6 mode-absent pass-bar the user sets.

---

## 1. Method + baseline reproduction `[probe]`

Base binary = committed 4b-i, rebuilt clean. **4b-i floor reproduced exactly** before any change
(`compare_rn.py --wir-bach <dir> --key-breakdown`, the `a96f179f40` L1 instrument; S2 = ≠global genuine
key error, lower = better; `characterise_bir_false.py` for the BIR gate):

| | Default | Baroque | Jazz* |
|---|---|---|---|
| mode-present S2 | **687** | **683** | 2002 |
| mode-absent S2 (FLOOR) | **2070** | **2099** | 2959 |
| BIR gate (present) | **57** | **57** | **23** |

*Jazz key S2 is unreliable (39–46% label-parse failures, as in 4b-i) — Baroque/Default are
load-bearing. Floor↔ceiling gap to close: **Default +1383, Baroque +1416**.

Each candidate weight set was applied in `keymodeanalyzer.h`, built, and measured **mode-present AND
mode-absent on all three presets** (6 corpora/config) + the BIR gate on the three present corpora,
diffed against the captured baseline identity sets. Measurement harness: `tools/b2_measure.sh`
(in-zone tool, written this run). Probes were chosen to be **principled and provisional**, NOT
fit to the 326-chorale gate (overfitting guard).

---

## 2. The four principled probes — floor movement + mode-present non-regression `[probe]`

All values `[empirical — Stage-5 fits]`. Δ vs the 4b-i floor (present 687/683, absent 2070/2099). Gate
held **57/57/23 in mode-present on every probe** (no BIR=false identity moved on any preset — the
ratification hard-stop never fired; details §4).

| Probe | Change (term, baseline→probe) | Def present | Def absent | Bar present | Bar absent |
|---|---|---|---|---|---|
| **baseline** | — | 687 | 2070 | 683 | 2099 |
| **B1** | `tonalCenterLeadingTone` 0.50→**1.20** | 772 (**+85**) | 2311 (**+241**) | 750 (+67) | 2305 (+206) |
| **A1** | `tonalCenterTonicWeight` 2.20→**3.50** | 685 (−2) | 2066 (−4) | 683 (0) | 2094 (−5) |
| **A3** | `noteWeightCap` 3.0→**4.5** | 920 (**+233**) | 1933 (**−137**) | 800 (+117) | 1843 (−256) |
| **A2** | `noteWeightCap` 3.0→**6.0** + `tonalCenterTonicWeight`→3.50 | 1122 (**+435**) | 1566 (**−504**) | 1020 (+337) | 1574 (−525) |
| **P1** | `disambiguation` Triad/Cost/Tonic 4.5/1.5/1.0→**6.0/2.5/3.0** | 687 (**0**) | 2070 (**0**) | 683 (0) | 2099 (0) |

Each probe maps to one of the three relative-pair discriminators the instruction named (dossier §2):

### 2.1 — Pairwise disambiguation (P1) — instruction's **#1** lever — **STRUCTURALLY INERT** `[probe]` `[code]`
A *large* bump (triad-bonus +33%, tonic-bonus **tripled**, cost +67%) produces **exactly zero floor
movement** (Default 2070→2070, Baroque 2099→2099) and zero present movement. Root cause, verified at
source (`keymodeanalyzer.cpp:455-488`) and in the `--dump-key-candidates` trace: every clause of
`applyPairwiseDisambiguation` fires **only when one relative LACKS its tonic** (`!bHasTonic`) or lacks a
complete triad. But the floor's relative-pair near-ties have **both** relatives' tonics **and** complete
triads present (e.g. bwv365 opening: both Cmaj and Amin show `completeTriad:true`, `disambig:0`). So the
mechanism the instruction called "the strongest existing relative-pair discriminator" is a **no-op on
exactly the population that constitutes the floor.** It discriminates *augmented-vs-suspended-tonic*
cases, not *both-diatonic-present* relative pairs. This is the single most important structural finding
of the run.

### 2.2 — Tonic salience (A1 / A3 / A2) — bites only when **uncapped**, and uncapping is a strict trade-off `[probe]`
- **A1** (raise `tonalCenterTonicWeight` 2.20→3.50, +59%, within the cap): floor moves **−4 / −5**
  (~0.3% of the gap). Negligible, because `noteWeightCap = 3.0` flattens the tonic term — when both
  relatives' tonic weights exceed 3.0 (the common case; e.g. bwv33.6 both ≈4.1–4.4), they contribute
  **identically** and the weight is inert. Gate-safe, present-safe, but does essentially nothing.
- **A3 / A2** (relax the cap to 4.5 / 6.0 so salience can express): the floor **does** close
  (A3 −137/−256, A2 **−504/−525** ≈ 36% of the gap) — but **mode-present regresses in lockstep**
  (A3 **+233/+117**, A2 **+435/+337**). The frontier (baseline→A1→A3→A2) is **smooth and monotone**:
  every region of floor recovery is paid for by a comparable-or-larger mode-present loss. **No point on
  it gives floor improvement at acceptable mode-present cost.** Per instruction §stop-conditions this is
  the **trade-off finding** ("the structure can't separate relatives without collateral damage =
  insufficient") — reported, not pushed through.

### 2.3 — True leading tone (B1) — **wrong corpus-level direction** `[probe]`
Raising `tonalCenterLeadingTone` 0.50→1.20 is **net-negative in BOTH conditions** (present +85/+67,
absent +241/+206). The chromatic leading tone *does* discriminate a genuine minor piece (in bwv33.6 the
entire 0.96 tonalCenter margin for A-minor comes from G♯ weight 3.0 vs B weight 1.08 — `[code]` dump),
but applied uniformly it **drifts the major-dominant corpus toward the relative minor**: the minor
relative's leading tone (G♯ for a-minor) appears at every V–i cadence *and* at every vi-tonicization
inside a major piece, so weighting it over-fires toward minor. The directional lever the instruction
hoped would separate harmonic-minor relatives is, in aggregate, a relative-minor bias.

---

## 3. Per-case adjudication `[probe]` `[oracle DCML]`

Mode-absent resolved key at piece start, baseline (matches 4b-i §3 exactly) and under the trade-off
lever A2 (the only lever that moves anything):

| stem | DCML | baseline absent | under A2 (uncap) | reading |
|---|---|---|---|---|
| bwv365 | a minor | **Amin ✓** | **Cmaj ✗** | A2 **regresses** it — uncap picks the locally-heavier C tonic (Cmaj tonicW 6.85 vs A 2.71) |
| bwv33.6 | a minor | **Amin ✓** | Amin ✓ | held (A genuinely the heavier tonic here) |
| bwv64.2 | G major | Amin ✗ | **GMixolyd** (tonic G ✓) | A2 **helps** the hard case find G — but Mixolydian flavor, and not shippable |
| bwv83.5 | d minor | Amin ✗ | Amin ✗ | no lever recovers it (note inference reads A-minor in all conditions) |
| bwv371 | G major | GMixolyd (tonic G ✓) | — | tonic correct, church-mode flavor (4b-i state, unchanged) |
| bwv437 | d minor | Dmel (tonic D ✓) | — | tonic correct, melodic flavor (unchanged) |
| bwv276 | d minor | DDor (tonic D ✓) | — | tonic correct, Dorian flavor (unchanged) |

**Reading:** the targets the instruction flagged as "should recover — the relative IS
note-distinguishable" (**bwv365, bwv33.6**) are *already* recovered mode-absent in 4b-i; no
strengthening was needed for them. The one lever that moves the corpus (A2) **regresses bwv365** (loses
it to C) while **helping bwv64.2** — i.e. it doesn't cleanly target the right population; it reshuffles.
**bwv64.2 / bwv83.5** (the hard class) confirm the instruction's prediction: note inference reads a
*different* key than DCML, not a relative-pair tie. bwv64.2 needs the global key G established over the
whole piece (only the uncap, reaching across the window, finds it — at an unacceptable present cost);
bwv83.5 stays A-minor under every lever. **Both are Stage-5/6 / richer-emission cases, not 4b-ii
reweighting cases** — confirmed, not chased.

---

## 4. Mode-present non-regression + BIR gate `[probe]` `[oracle]`

- **BIR gate (chord axis), mode-present, all three presets: 57 / 57 / 23 — byte-identical on EVERY
  probe.** No BIR=false identity moved (diffed against the captured baseline sets). The CLAUDE.md
  ratification hard-stop (un-adjudicated BIR=false increase) **never fired**. The key changes the
  cap-relaxation probes induce did not reach the gate cases' chord roots.
- **Mode-present key S2** is the disqualifier instead: A3 (+233/+117) and A2 (+435/+337) regress the
  *shippable* condition badly. Per the instruction ("Mode-present must NOT regress … it should stay ≈
  the 4b-i +2/0, not worsen"), A2/A3 fail. Only A1/P1 keep mode-present ≈baseline — and those are the
  probes that do nothing to the floor.
- **The coupling is structural, not incidental.** The floor regions are, *by construction*, the regions
  where the note-evidence relative-pair gap is **< the 1.0 declared hint** (else the hint would not have
  been the deciding factor mode-present in 4b-i). To win those regions mode-**absent**, note-inference
  must swing them by more than their current wrong-margin; but a note term strong enough to do that also
  **overrides the (correct) 1.0 hint mode-present** in exactly the same regions — regressing the 4b-i
  mode-present wins. The hint and the note-strengthening compete for one population. This is why every
  floor gain (§2.2) comes paired with a mode-present loss, and it is **independent of which note term is
  strengthened.**

---

## 5. Structural-sufficiency verdict (the point of the run)

**The existing note-based structure is INSUFFICIENT to carry the relative-major/minor decision by
reweighting.** Across all three instruction-named discriminators:

1. **Pairwise disambiguation** is *structurally inert* on the floor population (its clauses require a
   tonic-absent relative; the floor is tonic-present-both). No weight closes a gap a no-op can't touch.
2. **Tonic salience** is *blunted by the cap* (negligible within it) and, when *uncapped* to bite,
   produces a *strict monotone trade-off* — every floor region recovered costs a comparable-or-larger
   mode-present region. The present↔absent coupling (§4) is structural: both conditions decide the same
   sub-1.0 near-ties.
3. **True leading tone** is the *wrong aggregate direction* (relative-minor drift), net-negative in both
   conditions.

So the floor↔ceiling gap is **not a weighting problem**; it is a **missing-signal problem.** The
relative-pair near-ties (~1383 Default) are regions where the *local windowed* note terms are genuinely
balanced; the declared mode was a proxy for a signal those terms do not encode — the **global/cadential
identity of the key** (which relative the piece *resolves to*, established over the whole piece, not the
lookahead window). No reweighting of local, per-region salience can synthesize that signal.

**Residual genuinely unreachable by these terms (→ Stage-5/6 / the A-vs-B question):**
- The ~1383-region relative-pair floor that needs **global/cadential context** (OQ4 cadence→key wiring,
  deferred) or a **learned key-emission model** that integrates over the piece, not the window.
- The hard class (**bwv64.2, bwv83.5**) where local note inference reads a *different* key than DCML.
- The church-mode **flavor** residual (bwv371/437/276: tonic correct, mode flavor wrong) — a separate
  Stage-5 question, not a relative-pair tie.

**Provisional weight set for 4b-ii: baseline (UNCHANGED).** No principled bump improves the mode-absent
floor without regressing the shippable mode-present condition, so there is nothing to ship and nothing
for Stage 5 to "fit" within this structure. Proposing a non-regressing-but-negligible bump (A1) would be
going through the motions — the honest 4b-ii deliverable is the insufficiency verdict, not a no-op
weight. The source tree is therefore left at committed 4b-i (verified `git diff` empty on
`keymodeanalyzer.{h,cpp}` / `keyresolver.cpp`); suites green (composing **505** / notation **57** /
snapshots **11**); **no snapshot/golden refresh needed** (no winner moved).

---

## 6. First-pass read: can Stage 5 take it further? — **structural ceiling, not a fitting gap**

A weight-fitter (Stage 5) operating on **these terms** would land on the §2.2 trade-off frontier: it
could pick a point with a slightly better floor at a slightly worse present, but it cannot escape the
present↔absent coupling, because the coupling is a property of the *structure* (local salience deciding
sub-1.0 near-ties), not of the *weights*. **Stage 5 fitting alone will not close this gap.** What is
needed is one of:

- **A decoupled relative-pair signal** — the precise structural lever the data points to is a
  **tonalCenter-only tonic cap** (let salience express in the family-selection relative decision *only*,
  keeping `noteWeightCap = 3.0` for the global score so non-relative decisions are unperturbed). This
  removes the *non-relative collateral* of A2/A3 — but the §4 coupling argument predicts it will **still**
  regress mode-present on the relative axis itself (it cannot win the sub-1.0 near-ties mode-absent
  without overriding the correct hint mode-present). It is worth a single Stage-5 confirmation as the
  cleanest isolation, but it is **not expected to be the fix.** (I did not build it here: it is a new
  parameter beyond "bump an existing weight," and the run's stop-condition is to report such a lever as a
  finding, not build it.)
- **Global/cadential context (OQ4, deferred):** a cadence→key term feeding `analyzeKeyMode`, so the
  relative decision is anchored by *where the phrase resolves*, not just window salience. This is the
  signal the declared mode was proxying. **This is the recommended next structural step** — it adds the
  missing modality rather than reweighting the present one.
- **Learned key emission (Stage 6 / the A-vs-B question):** if even cadence wiring leaves a residual,
  the relative-pair decision is evidence that the key axis needs a richer/learned emission model — the
  A-vs-B "is the hand-built scorer enough" question resolves toward **B (richer model needed)** for the
  relative axis specifically.

**Bottom line for OQ6:** the mode-absent pass-bar should be set knowing that **the 4b-ii structure
recovers ~0 of the +1383 floor without regressing mode-present.** The honest recoverable-by-reweighting
fraction is **near zero**; meaningful floor recovery requires the deferred cadence→key work, not weight
tuning. The dossier's starting reference (≥70% of the +378 surviving mode-absent) is **not reachable by
4b-ii reweighting** and should be re-scoped onto the cadence/Stage-6 step.

---

## 7. Commit shape (HELD — DO NOT commit)

- **No production change to commit.** The four probes were applied, measured, and **reverted**; the
  source tree is at committed 4b-i (`git diff` empty on the key-analyzer files).
- **Working-tree artifacts (this run):** `cc_stage4b_ii_report.md` (this file) and
  `tools/b2_measure.sh` (the in-zone measurement harness — keep or drop at Cowork's discretion; it
  documents the dual-condition probe protocol). No snapshot golden, no test re-pin, no `docs/` sync
  (no scoring term changed).
- **Transient (gitignored, not committed):** `tools/corpus/b2*_*/` (the 30 regenerated probe corpora).

## 8. Stop conditions — disposition
- ✅ **Trade-off that wrecks mode-present (A2/A3):** reported as the §2.2/§5 finding; **not pushed
  through** — no trade-off point proposed for ship.
- ✅ **Un-adjudicated BIR=false increase:** none — gate byte-identical 57/57/23 mode-present on every
  probe.
- ✅ **`src/notation`/`src/engraving` production edit:** none required (none made; no golden refresh
  needed since no winner moved).
- ✅ **Overfitting guard:** caught and honored — no weight is fit to the gate; the deliverable is the
  sufficiency verdict + the baseline (unchanged) provisional, exactly as the stop-condition directs.
- ✅ **Hard-class cases needing a new mechanism (bwv64.2/bwv83.5):** reported as Stage-5/6 / A-vs-B
  findings (§3, §6); **no new term built.**
