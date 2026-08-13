# Key-as-a-Path — Stage 4 Design (key HMM + KeyArea spans)

> **DRAFT — UNCOMMITTED. Design only; no production code, no behavior change.**
> Base commit `f8c6b3932a` ([probe] `git rev-parse --short HEAD`). Ratification-gated:
> this document is **HELD** (`git add` permitted, `git commit` NOT) until a ratification
> addendum lands.
>
> Every existence claim is tagged **[code]** (read the source) or **[probe]** (ran a script
> and read output). The §3 derivation — *does the path actually fix S2?* — is the
> load-bearing part and is grounded in real per-region margins, not asserted.
>
> *Mandatory inputs read: `cowork_target_architecture_review.md` rec.2; `cc_precision_headroom_dossier.md`
> §1.5/§2; `docs/precision_metric_design.md` §3.1/§3.2 (L1 rung); `ARCHITECTURE.md` §4.2/§5.2;
> `src/composing/analysis/key/keyresolver.{h,cpp}`, `keymodeanalyzer.{h,cpp}`;
> `src/composing/analysis/region/regionanalyzer.cpp` (the per-region call site);
> `src/composing/tests/regionanalysis_tests.cpp` (Stage-1c key pins); `docs/redesign_plan.md`
> Step-3 (shelved) + the arch addendum.*

---

## §0 — TL;DR

| | Statement | Basis |
|---|---|---|
| **Target** | S2 = key_disagree∧(our key ≠ DCML global) = **1032 regions, 10.2%** of the Bach gate set; relative-major/minor + partial-signature dominated. | [probe] reproduced exactly |
| **Mechanism** | Key as an **HMM path**: states = (tonic×mode); emissions = the EXISTING `analyzeKeyMode` per-window scores; transitions = circle-of-fifths modulation penalty; **Viterbi** over windows → a key PATH, replacing per-window argmax + `promoteWinnerInPlace` hysteresis. | rec.2; [code] |
| **§3 finding (reshapes the value)** | The path fixes only the **~10%** of S2 that is a *local flip in a mostly-correct stem* (margins ≈0.05–0.20, correct key is the runner-up). The other **~90%** is a *consistently-wrong emission* (153 regions, 14.8%, in stems whose key NEVER changes; correct key often not even rank-2; margins 2.0–3.3). For that bulk a modulation penalty is **neutral-to-harmful** (it entrenches the wrong key). | [probe] `s2_derive.py` |
| **Conclusion** | Stage 4 is **necessary but not sufficient** for S2. Its real, defensible deliverables are (a) the flip + hysteresis-trap fix (~10–15%), (b) **superseding the `promoteWinnerInPlace` confidence wart** with a principled global decode, (c) the **KeyArea spans** Stage 6 needs (independent of whether S2 shrinks). The remaining ~85% of S2 needs an **emission** fix (partial-signature extension / key-profile), which Stage 4 must bundle to claim S2. | §3 |
| **Reuse** | `analyzeKeyMode` (the 252-candidate scorer) = emission, REUSED. `resolveKeyAndModeRanked`'s per-region hysteresis + `promoteWinnerInPlace` = REPLACED by the decode. Partial-signature correction = KEPT (folds into emission input). **The piece-start shortcut is not in this list — it no longer exists; see the correction block below.** | [code] |
| **Caveat (not a falsification)** | The resolver currently surfaces only the **top-3** candidates with post-family-selection scores, not the raw 252. The HMM emission needs the **top-N (or full 252) raw scores** exposed — a small refactor of `analyzeKeyMode`'s output, not a rebuild. | [code] |

> **★ CORRECTED 2026-08-13 — THE PIECE-START SHORTCUT DOES NOT EXIST AT HEAD, AND FOUR STATEMENTS IN
> THIS DOCUMENT RESTED ON IT (`OPEN_ITEMS.md` OI-315).** §1's item 2 already recorded the removal.
> The **Reuse** row above, §2.1's *Initial state* bullet, §5's reuse-map row and §9.1's step 2 still
> described the shortcut as live code — the correcting sentence sitting sections away from the four
> statements it refutes. All four are corrected in place, each with **its former wording preserved
> beside it (#12)**; nothing else in this document is touched, and no design decision is taken here.
>
> **The filing branch, and why the body is corrected rather than bannered.** The filing convention
> (`cowork_design_doc_template.md`, the user's Ruling 62 of
> `cowork_rulings_2026_08_11_fourteenth_stop.md`) has two branches by kind, and the derived
> enumeration that convention ordered records this document's verdict as **BRANCH TWO — a live
> governing surface, so the body is corrected** (`tools/audit/filing_convention_application.json`,
> the row for this file). Contrast `docs/stage4b_design.md`, the design that LANDED, whose verdict in
> the same enumeration is **branch one** and whose body is therefore untouched behind a historical
> banner.
>
> **Established at the code, this session, reading the whole enclosing function rather than a matching
> line.** `keyresolver::resolveKeyAndModeRanked` carries no piece-start branch: its only early return
> is the insufficient-pitch-classes fallback, gated on the window's distinct-pitch-class count and on
> nothing about the tick, and the function's own comment dates the removal to Stage 4b-i and names the
> re-targeted pins. The bridge entry point `resolveKeyAndMode`
> (`notationcomposingbridgehelpers.cpp`) loads analyzer preferences and delegates to that function
> with no branch of its own. The removal is likewise recorded in `ARCHITECTURE.md` §5.2 and in the
> re-targeted pins `PieceStartOpening_NoteBased_DeclaredMinor` / `_DeclaredMajor`.

---

## §1 — Scope: what S2 is, what Stage 4 fixes, enables, and must not regress

**S2, measured.** On `tools/corpus/default` (the live out-of-box config), 326 WiR-covered Bach
chorales, 10 108 matched regions, batch granularity [probe, reproduces dossier §1.2/§1.5 exactly]:

- `key_disagree` total = 2 823 (27.9%): root_pc✓, coarse-quality✓, **degree differs**.
- Of those, **S1 = 1 791 (17.7%)**: our key = DCML *global* but ≠ DCML *local* → DCML tonicized
  and we stayed in the global key. **Not a key-detection error** — a missing tonicization *label*.
  Stage 6's, not Stage 4's.
- **S2 = 1 032 (10.2%)**: our key ≠ DCML *global* → genuine key/mode error. **This is Stage 4's target.**

**What S2 is made of** [probe `s2_derive.py tools/corpus/default`]:
- **49.3% (509)** — our key is the *relative major/minor* of the DCML global (a↔C, d↔F, e↔G…).
- **50.7%** — *not* relative: fifth/dominant confusion (bwv343: g read as **D** minor), modal slips
  (Lydian/Mixolydian-♭6 readings), and the Baroque **partial-signature** pattern [doc].
- **48.4% (499)** — the DCML global key is present as **our region runner-up** (reachable in a 2-wide
  lattice); the complementary **51.6%** is not (the correct key is not even rank-2).

**What Stage 4 FIXES:** the *local-flip* and *hysteresis-trap* sub-classes of S2 (§3) — roughly 10–15%
of S2 — plus it removes the `promoteWinnerInPlace` hysteresis brittleness corpus-wide.

**What Stage 4 ENABLES but does not itself fix:** **S1 (17.7%)**, the single largest slice. S1 is
unlockable only by a tonicization labeler (Stage 6.1) consuming **KeyArea spans** (§4). Stage 4
*produces* the spans; Stage 6 *consumes* them. Stage 4 alone moves zero S1.

**What Stage 4 MUST NOT regress:**
1. The `81978321e3` **partial-signature correction** (Corelli C-minor-under-2-flats → −3, and its
   negative counter-case G-minor-under-2-flats *not* corrected). Pinned by
   `regionanalysis_tests.cpp::PartialSignature_CMinorUnderTwoFlats_Corrected` /
   `_GMinorUnderTwoFlats_NotCorrected` [code]. The correction must remain an **emission-input**
   adjustment, untouched by the decode.
2. The **piece-start shortcut** — **REMOVED in Stage 4b-i** (2026-06-14): the declared-mode anchor no
   longer short-circuits the opening; the normal note-based lookahead runs from piece start. The pins
   were re-targeted to the new behavior (`PieceStartOpening_NoteBased_DeclaredMinor/Major`). The
   **insufficient-data fallback** (pinned `InsufficientPitchClasses_FallbackConfidenceZero`) is
   unchanged [code]. The HMM's initial-state prior is now whatever the note-based opening produces (no
   declared start-anchor to reproduce); empty-emission handling is still the fallback. Also removed in
   4b-i: the hard "strong declared-mode prior" promotion in `resolveKeyAndModeRanked` (the note-based
   hysteresis `promoteWinnerInPlace` stays). Declared mode now enters only as a small 1.0 hint inside
   `analyzeKeyMode`. See `stage4b_design.md` §2.7 / `cc_stage4b_i_report.md`.
3. The **Baroque BIR identity set** and **pipeline snapshots** — because the per-region key feeds
   chord emission (§9), a key change is *also* a chord-axis change.

---

## §2 — Key as a path — the HMM, concretely

### 2.1 The state space, emission, transition

- **States** at window `t`: `(tonicPc, mode)` candidates. The full space is 12×21 = 252 (the existing
  scorer's space, ARCHITECTURE §4.2 [code]). In practice the decode runs over the **top-N emissions
  per window** (N a config, default ≈ 5–8) plus the *incumbent* (so staying is always an option even
  if the incumbent fell out of the current window's top-N).
- **Emissions** `e_t(s)` = the EXISTING `analyzeKeyMode` raw `score` for candidate `s` at window `t`
  [code `keymodeanalyzer.cpp:564` — `eval.score` = scaleScore + triadScore + keySigScore + charScore +
  ltScore + priorScore, with the post-hoc pairwise disambiguation and the declared-mode penalty already
  folded in]. **No new scorer.** This is rec.2's "reuse your existing window scores."
- **Transitions** `τ(s_{t-1} → s_t)` = `0` for staying in the same key; a **modulation penalty**
  `−λ · cofDistance(s_{t-1}, s_t)` for a key change, where `cofDistance` is the circle-of-fifths
  distance between the two key signatures, with **relative / parallel / closely-related cheaper than
  distant**. Structure (not numbers):

  | transition | cost | rationale |
  |---|---|---|
  | same (tonic,mode) | `0` | no modulation |
  | relative major↔minor (same key sig) | `λ_rel` (small) | shared diatonic pool, common |
  | parallel major↔minor / mode change, same tonic | `λ_par` | common in Baroque |
  | ±1 fifth (closely related) | `λ_near` | adjacent key |
  | distant | `λ_far · steps` | rare |

  The current resolver already *encodes this ordering crudely* as two hysteresis margins
  (`relativeKeyHysteresisMargin` for same-key-sig switches, `hysteresisMargin` otherwise [code
  `keyresolver.cpp:312`]) — the HMM generalizes the two-bucket margin to a proper distance-graded edge.

- **Decode**: Viterbi over the window sequence maximizing `Σ_t e_t(s_t) + Σ_t τ(s_{t-1}→s_t)`. The
  argmax over the whole path replaces the greedy `.front()` + `promoteWinnerInPlace` of today.
- **Initial state**: **there is no declared start-anchor to reproduce.** The piece-start shortcut this
  bullet was written against was removed in Stage 4b-i (2026-06-14; §1 item 2, which states the
  consequence in the same words), so the start prior is whatever the note-based opening's own emission
  produces at the first window, and a degenerate opening is covered by the insufficient-data fallback
  rather than by a declared seed. *(**★ CORRECTED 2026-08-13** — see the correction block under §0.
  **THE FORMER WORDING, PRESERVED (#12):** "the **piece-start shortcut** becomes the HMM's start prior
  — when no pitch evidence exists (tick < 16 beats, declared mode present), seed `s_0` = declared key
  at a prior weight = `relativeKeyHysteresisMargin` (the exact value the shortcut uses today as
  `decl.score` [code `keyresolver.cpp:272`]), so the decode reproduces the pin by construction.")*

### 2.2 The observation unit (window)

The decode runs over the **same windows the resolver runs over today**: one observation per
*analysis tick* the pipeline already resolves a key at — i.e. per Pass-1 boundary region
[code `regionanalyzer.cpp:418`, the per-region `resolveKeyAndModeRanked` call]. Each window's
emission is `analyzeKeyMode` over the existing 16-beat-lookback + dynamic-lookahead context
[code `keyresolver.cpp:251–298`]. **Stage 4 does not change segmentation or the window content** — it
changes only how the per-window scores are *combined across windows* (argmax+hysteresis → Viterbi).
This keeps Stage 4 orthogonal to joint segmentation (deferred past Stage 5 [doc]).

### 2.3 Why the 252→top-N emission is sound

`analyzeKeyMode` returns only the top-3 today [code `keymodeanalyzer.cpp:697–724`], chosen via a
key-signature-family selection that can place a lower-raw-score candidate first (the `bestByCenter`
vs `bestByRaw` logic [code:633–663]). For the HMM the emission must be the **raw `eval.score`** of each
candidate (not the family-selected ordering), so the path — not a per-window selector — picks the
winner. **Build item:** expose the top-N raw `(tonic,mode,score)` from `analyzeKeyMode` (it already
computes all 252 in `evaluations[]` [code:544]; the change is to emit more of them, not to recompute).
The family-selection logic (`bestByCenter`/tonal-center override) is *subsumed* by the decode and is a
**removal candidate** (§5), not a thing to thread through.

### 2.4 Weights are Stage-5-fitted, not hand-tuned

`λ_rel, λ_par, λ_near, λ_far` and the emission/transition scale ratio are **transition-model weights**.
This design fixes their **structure** (the table in §2.1) and **defers the numbers to Stage 5**, whose
objective is the granularity-robust, DCML-only metric [doc, precision_metric_design §3.3]. Hand-setting
them here would repeat the calibration trap the arch review flagged (§2.4 of that review). For the
ratification A/B (§7) a single provisional `λ` per bucket may be used to *demonstrate direction*, but it
is explicitly a placeholder, not a calibrated value.

---

## §3 — Does the path beat per-window argmax on S2? — derived from real margins

> This is the load-bearing section. The instruction's hypothesis: *"a per-window scorer flips a↔C at
> local evidence; a path with a modulation penalty resists the flip."* I probed the actual S2 cases.
> **The hypothesis holds for ~10% of S2 and FAILS for the rest** — exactly the kind of reshaping the
> beam-widening derivation produced for Δ=+7a. Probe: `/c/tmp/s2_derive.py` (read-only, reuses
> `compare_rn`/`compare_analyses`/`dcml_parser` verbatim; estimates per-window margins by inverting the
> committed confidence sigmoid, with the hysteresis caveat below).

### 3.1 The three sub-mechanisms (per-region traces)

**Class A — spurious relative flip (path FIXES).** `bwv16.6` (DCML global = a minor throughout):
our key trace is `Amin Amin Amin | Cmaj …×19… Cmaj | Amin Amin Amin` — a long flip to the relative
**major** in the middle while DCML stays in *a*. The runner-up is `Amin` on **every** flipped region,
and the winner-over-runner-up margin (sigmoid-inverted `keyConfidence`) is **0.01–0.20** [probe]:

```
  #  tick  our_key  dcml_loc dcml_glob  bucket        gap~  runnerUp  S2
  3  1440  Cmaj     a        a          root_err      0.01  Amin
  4  1920  Cmaj     G        a          key_disagree  0.08  Amin      S2
  5  2400  Cmaj     G        a          key_disagree  0.20  Amin      S2
 ...  (Cmaj holds for ~18 regions, gap~ 0.01–0.20, runner-up Amin throughout)
 24 17760  Amin     a        a          exact         0.50  Amin
```
A circle-of-fifths transition penalty of even `λ_rel ≈ 0.3` exceeds the 0.01–0.20 emission gap, so the
decode **stays in a minor** and the flip vanishes. `bwv420` is the same shape (correct `Aharm` for 17
regions, then a thin-margin flip to `Cmaj`, runner-up `Amin`, gap~ 0.01–0.12 on most flipped regions).
**For Class A the hypothesis is confirmed with real margins.**

**Class B — consistent relative error (path does NOT fix).** `bwv244.54` (DCML global = **F major**):
our key is `Dmin` for **all 29 regions** (`distinct our-keys across stem: ['Dmin']`). Dmin is the
relative minor of F. There is **no flip to resist** — we never leave Dmin. Worse [probe]:

```
  #  tick  our_key  dcml_glob  gap~  runnerUp   S2
  1   960  Dmin     F          3.35  Dharm      S2
  5  3360  Dmin     F          2.49  GDor       S2
 ... (Dmin wins by 2.0–3.3 over the runner-up; runner-up is Dharm/GDor — NEVER Fmaj)
```
Two independent reasons the path can't help: (1) the correct key **F major is never even rank-2** — it
is not in the candidate set the decode chooses among; (2) the emission margin favoring the wrong Dmin is
**2.0–3.3**, an order of magnitude larger than any plausible `λ`. **A modulation penalty makes this
worse**, not better: it adds cost to *ever leaving* the (wrong) established Dmin, entrenching the error.

**Class C — hysteresis-trapped late switch (path FIXES, via a different mechanism).** `bwv343`
(DCML global = g minor; this is a *non-relative* error — we read g as **D** minor, the dominant): our
key is `Dmin` for 25 regions then finally `GDor/Gmel`. The runner-up is `GDor` (correct tonic!)
throughout. Early on Dmin genuinely outscores GDor (gap~ 2.3–2.5 — a Class-B consistent error). But
**late**, the sigmoid-inverted gap goes **negative** (−0.7 to −1.0) [probe] — meaning GDor's raw
window score now *exceeds* Dmin's, yet the greedy resolver **keeps Dmin** because the cross-window
hysteresis test (`front.score < prev.score + margin` [code `keyresolver.cpp:315`]) holds it. A global
decode is **not** trapped this way — it would switch to GDor where GDor genuinely wins. **But the early
Class-B half of bwv343 the path still can't fix.** (Note: this exposes a real flaw in the *current*
hysteresis — it compares the current window's winner score to the *previous window's* winner score, two
incommensurable quantities from different-content windows. The HMM transition penalty is applied to
**same-window** emission differences inside the decode, which is the principled replacement.)

### 3.2 Corpus-wide quantification (the headline) [probe]

For each of the 1 032 S2 regions, classify by *robust* signals only (no margin dependence): is it a
**local deviation in a mostly-correct stem** (we get the DCML global right on ≥50% of the stem's
regions) or part of a **mostly-wrong stem** (<50%)?

```
S2 mechanism split (stem-correct-fraction × relative-pair):
  deviation     rel    :   77  (7.5%)
  deviation     nonrel :   29  (2.8%)
  mostly-wrong  rel    :  432  (41.9%)
  mostly-wrong  nonrel :  494  (47.9%)
  --> path-fixable (deviation in a mostly-right stem):   106  (10.3%)
  --> NOT path-fixable by transitions alone (mostly-wrong): 926  (89.7%)
  ... AND 153 (14.8%) are in stems whose key NEVER CHANGES (single distinct key) — a pure
      emission error with no transition at all for a penalty to act on.
```

**The derivation's verdict:** the modulation penalty's whole power is *stickiness* — it makes the path
resist changing key. Stickiness helps **only** when the path is mostly right and occasionally flips
wrong (Class A, **10.3%**). When the emission is *consistently* wrong (Class B, the bulk), stickiness is
neutral at best and **counterproductive** (it entrenches the wrong key and resists the rare correct
window). Class C (hysteresis traps) is a real, separate win but is a *correctness-of-mechanism* fix
(replacing a broken cross-window threshold), not a *coverage* fix — it is not separately sized but is
bounded by the late-switch tails visible in traces like bwv343.

### 3.3 What this means for Stage 4 (honest)

Stage 4-as-a-path, **alone**, addresses ≈10–15% of S2 (Class A + the Class C tails) — roughly **1.0–1.5%
of all matched regions**, not the headline 10.2%. To claim the full S2 slice, Stage 4 must **also**
move the emission for the consistent-error bulk:

- **Partial-signature extension** — the 81978321e3 mechanism already fixes the *minor-under-Dorian-sig /
  major-under-Mixolydian-sig* class [code]. Several Class-B stems (the d↔F, g-read-as-d cases) are
  one-accidental-short Baroque notations the current detector does not catch (it only flips ±1 toward
  the declared accidental and requires a pervasiveness+dominance ratio). Broadening the *detector*
  (not the threshold) is an emission fix that lives naturally in Stage 4.
- **Key-profile / emission reweight** — the relative-major-vs-minor decision is the
  `applyPairwiseDisambiguation` + `tonalCenterScore` machinery [code]; its constants are
  hand-set [code, all `[empirical]`]. These are Stage-5 fit targets, but the *structure* (which
  evidence distinguishes a from C) is an emission concern, not a transition one.

So the design's recommended framing: **Stage 4 = the key HMM path (Class A/C fix + KeyArea + hysteresis
supersession) bundled with the emission-side partial-signature/profile work for Class B.** The path is
the scaffold; it is not, by itself, the S2 fix the headline implies. This is reported as the §3 finding
(per the stop condition), and it is the same shape as the beam-widening result: *search/path cannot
move an error the emission consistently prefers.*

---

## §4 — KeyArea spans — the first-class output Stage 6 consumes

### 4.1 The structure

```cpp
struct KeyArea {
    int       startTick;
    int       endTick;          // half-open [start, end)
    int       tonicPc;          // 0..11
    KeySigMode mode;
    int       keySignatureFifths;
    double    confidence;       // path-marginal, NOT the broken normalizedConfidence (§5)
};
```

A `KeyArea` is a **maximal run of windows the decode assigned the same `(tonicPc, mode)`**. The decode
produces a key per window; coalescing equal-key adjacent windows yields the span list. This is what
`unified_analysis_pipeline.md` wanted and is the natural output of the decode (rec.2: "KeyArea spans
fall out of the decode"), *not* a post-grouping over greedy per-window labels (which would inherit the
hysteresis brittleness).

`confidence` is the **path marginal** (the decode's own measure: e.g. the score gap between the best
path and the best path forced through a different key over the span), explicitly **replacing** the
sigmoid `normalizedConfidence` the Step-3 investigation found unreliable [doc; code: the wart is pinned
by `PromoteWinnerInPlace_HysteresisDoesNotRecomputeConfidence`].

### 4.2 The tonicization-vs-modulation boundary (interface stub for Stage 6)

This is where Stage 4.2 meets Stage 6 (metric contract §3.1, the "tonicization vs modulation" row [doc]).
The KeyArea path gives Stage 6 the *global/established* key over a span. A region **inside** a KeyArea
that locally tonicizes a secondary is distinguished from a genuine local-key modulation as follows
(stub — the labeler is Stage 6, not Stage 4):

- **Modulation** = the **KeyArea boundary itself** — the decode committed a new key span. Within the new
  span, a `V` is a local-key `V`.
- **Tonicization** = a chord *inside* a KeyArea pointing at a non-tonic degree (a secondary dominant /
  applied chord) **without** the decode opening a new KeyArea. Stage 6 reads: "this region is inside
  KeyArea(g minor); its sonority is a D-major triad → `V/V`, not a modulation to D."

The **contract** Stage 4 must satisfy for this to work: KeyArea boundaries must be **conservative** —
the decode should open a new span only for a *sustained* key change (which the modulation penalty `λ`
controls: higher `λ` = fewer, longer KeyAreas = more in-key tonicizations for Stage 6 to label; lower
`λ` = the path tracks every local tonic and Stage 6 has nothing to do). **This couples `λ` to Stage 6's
job** and is the strongest reason Stage 4 and the Stage-6 contract should **co-ratify** (§10, OQ-1).
The metric rung for it is **L2** (S1 migrating `key_disagree → exact/partial` as Stage 6 emits `V/x`)
[doc, precision_metric_design §3.2].

---

## §5 — Relationship to the existing key machinery (reuse map)

| Component [code] | Role under Stage 4 | Disposition |
|---|---|---|
| `KeyModeAnalyzer::analyzeKeyMode` (252-candidate scorer, 6 helper terms) | **Emission model** `e_t(s)` | **REUSE.** Expose top-N raw `eval.score` instead of only top-3 family-selected (§2.3). |
| `resolveKeyAndModeRanked` — per-region orchestration | The decode replaces its *combination* logic; its evidence-gathering (window build, lookahead loop) is reused | **REFACTOR.** Becomes the per-window emission provider; the decode is layered over the window sequence. |
| `partialSignatureCorrection` (81978321e3) | Emission-input adjustment to `keyFifths` | **KEEP, untouched.** Folds into each window's emission exactly as today. |
| Piece-start shortcut (declared mode, tick<16beats) — **REMOVED FROM THE CODE in Stage 4b-i, 2026-06-14 (§1 item 2)** | — (there is no such component to give a role) | **NOTHING TO REUSE.** The start prior is the note-based opening's own emission; a degenerate opening is the fallback row below. *(★ Corrected 2026-08-13 — see the block under §0. **THE FORMER WORDING, PRESERVED (#12):** role "HMM **initial-state prior** (seed `s_0`)", disposition "**REUSE as start prior** (reproduces the pin).")* |
| Insufficient-data fallback (`<3` distinct PCs) | Empty/degenerate emission → carry incumbent or notated key | **REUSE** (reproduces the pin). |
| Per-region **hysteresis** (`relativeKeyHysteresisMargin`/`hysteresisMargin`, cross-window score threshold) | The principled, distance-graded **transition penalty** | **REPLACED.** The decode *is* the hysteresis, done right (same-window emission diffs, not cross-window absolute scores — §3.1 Class C). |
| `promoteWinnerInPlace` (re-rank without recomputing confidence — the Stage-1c wart) | — | **REMOVED.** The decode is the principled re-ranking; confidence becomes the path marginal (§4.1). |
| `analyzeKeyMode`'s `bestByCenter`/`tonalCenterScore` family-selection [code:615–663] | A per-window winner selector | **REMOVED (subsumed).** The path selects the winner; the tonal-center disambiguation is replaced by the decode + (Stage-5) emission reweight. |
| `normalizedConfidence` sigmoid | — | **REPLACED** by the path marginal. The Step-3 finding (0.025–1.00 for one correctly-keyed piece [doc]) does **not** affect the HMM: the decode uses the **raw `eval.score`**, never the sigmoid confidence. |

**No falsification on read.** The reuse split holds: `analyzeKeyMode` is a clean emission model and the
resolver's per-window argmax + hysteresis is exactly the part a decode replaces. The one refinement is
the top-N-vs-top-3 emission exposure (§2.3) — a small, additive change, not a rebuild.

---

## §6 — Reconciliation with the shelved Step-3 "key-as-distribution"

`redesign_plan.md` Step-3 shelved key-as-distribution (2026-06-08) because [doc]:
1. its motivating case (Corelli "G minor instead of C minor") was already fixed by the partial-signature
   correction `81978321e3`; and
2. "no live case showed the correct key at rank 1/2" — there was no measured target.

**Both reasons are now resolved, and the prior shelving evidence does not block the HMM:**

- **There is now a measured target.** The headroom dossier provides **1 032 live S2 cases** [probe].
  Step-3 was shelved for lack of a target; that gap is closed. Stage 4 is *not* "distribution for its
  own sake" — it is an HMM motivated by 1 032 measured errors, **measurable on the L1 rung** the moment
  it ships (`--key-breakdown` S2 shrink, [doc]).
- **The "rank 1/2" objection is partially confirmed and partially answered by §3.** Step-3 said the
  correct key didn't appear at rank 1/2. §3 shows that for **51.6%** of S2 the correct key is indeed
  **not even rank-2** — confirming Step-3's worry for the Class-B bulk. This is precisely why §3
  concludes the path alone is insufficient and bundles the emission fix. For the **48.4%** where the
  correct key *is* rank-2, the path can reach it — but (Class A vs B) only the *flip* subset benefits.
- **The `normalizedConfidence` unreliability that sank the Step-2 "scale-by-confidence" idea does NOT
  affect the HMM.** That idea multiplied a bonus by the sigmoid confidence [doc]; the HMM never touches
  the sigmoid — it decodes over raw `eval.score`. The wart is *removed*, not depended upon (§5).

So Stage 4 is no longer premature: it has a measured target, a measurable gate, and it sidesteps the
exact mechanism (sigmoid confidence) that made Step-2/Step-3 fragile.

---

## §7 — Measurement plan (on the L1 rung)

All measurement is **DCML-only** on the **granularity-robust unit** [doc, precision_metric_design §2/§3.3;
both shipped at `f8c6b3932a` as `--granularity-robust`]. Success = **S2 (`key_disagree, ≠global`)
shrinking** on `--key-breakdown` [doc, L1 rung], with:

1. **No S1 regression** — Stage 4 must not push `=global≠local` regions into `≠global` (it must not
   start mis-detecting the global key in order to "explain" a tonicization). `--key-breakdown` reports
   both halves; the S1 half must hold.
2. **No `81978321e3` regression** — the Corelli C-minor case and the partial-signature pins (§1) stay
   green.
3. **Both surfaces** — the Bach gate (`--wir-bach`, 326/353) **and** the non-Bach cross-corpus
   (key error ~2× harder — dossier §1.4 root_err 50.7% vs 26.8%). Report per-corpus; never a single
   blended number that hides which corpus moved [doc, §3.3 coverage honesty].

**Expected-direction table** (per the §3 classes; signs, not magnitudes — magnitudes are Stage-5):

| Case class | metric | expected | confidence |
|---|---|---|---|
| Class A — relative flip in mostly-right stem (≈10% of S2) | S2 ↓ | **improves** | HIGH (margins ≤ λ, §3.1) |
| Class C — hysteresis-trapped late switch | S2 ↓ | **improves** | MED (mechanism-sound; size unbounded) |
| Class B — consistent relative error (≈80–85%) | S2 | **≈flat** (path alone); **worsens** if `λ` too high | HIGH (correct key not reachable, §3.1) |
| Partial-signature Class-B subset (with the §3.3 emission extension) | S2 ↓ | **improves** | MED (needs the detector-broadening, A/B'd separately) |
| Chord axis (BIR, snapshots) | identity sets | **must hold or move DCML-correctly** | gate (§9) |

**The chord-axis side effect is measured too** (§9): every Stage-4 key change is re-scored on Baroque
BIR + pipeline snapshots; any movement must be DCML-adjudicated, exactly as a 3.2-class behavior change.

---

## §8 — Single path / config / cost

**One key path, all consumers.** Per the Stage-2 "one pipeline, one truth" principle, the decode must
serve **every** key consumer through a single code path:
- **batch** (`batch_analyze`, the BIR/rn metric surface) — `regionanalyzer.cpp` per-region loop;
- **the bridge / P3** (`notationcomposingbridgehelpers.cpp` also calls `resolveKeyAndModeRanked` [code]);
- **chord emission** — the decoded per-window key feeds `analyzeChord(tones, localKeyFifths,
  localKeyMode, …)` [code `regionanalyzer.cpp:453`] and freezes into `snapshot.keyTonicPc/scale →
  cell.basisIndep` [doc, redesign Step-3 finding]. No second/parallel key logic (the D-PASS0 lesson:
  divergent paths are a measurement blind spot).

**Config-agnostic.** `λ` and the emission top-N are `KeyModeAnalyzerPreferences` fields (prefs in),
like every other weight. Default config is `--preset Default` (the live product); the Baroque-tuned
chord gate thresholds are untouched (Stage 4 touches key, not the gate constants).

**Decode-once cache (3.1b interaction).** The chord path already memoizes the per-window section build
inside the expanding-window P3 algorithm [doc, Stage 3.1b]. The key decode is a **separate, cheaper**
pass (252 candidates × windows, one Viterbi) and should share the same decode-once-query-many lifecycle:
decode the key path once per analysis span, cache it, and let P3/P4/bridge read it. The key decode does
**not** depend on the chord decode (key feeds chord, not vice versa, in the current factorization), so
it runs **first** in the per-span order.

**Per-window cost.** Emission is already paid today (`analyzeKeyMode` runs per region). The added cost
is the Viterbi: O(windows × N² ) with N = top-N states (≈5–8) — negligible vs the Pass-0 chord cost
(≈99% of query time [doc, Stage 2.5]). No perf gate risk.

---

## §9 — Migration sequencing, risks, rollback

### 9.1 Sub-steps (each independently gated)

1. **4.0 — expose top-N raw emissions** from `analyzeKeyMode` (additive; byte-identical: nothing
   consumes them yet). Gate: 0/353 × 3 configs, snapshots 11/11.
2. **4.1 — key decode behind a flag** (`decodeKeyPath`, default OFF = today's per-region argmax+hysteresis,
   byte-identical). Implement Viterbi over the window sequence; reproduce the **note-based-opening**
   (`PieceStartOpening_NoteBased_DeclaredMinor` / `_DeclaredMajor`) / insufficient-data /
   partial-signature pins under flag-OFF. Gate: flag-OFF byte-identical. *(**★ CORRECTED 2026-08-13**
   — see the correction block under §0. **THE FORMER WORDING, PRESERVED (#12):** "reproduce the
   piece-start / insufficient-data / partial-signature pins under flag-OFF". The pins were re-targeted
   to the note-based opening when the shortcut was removed, so the former wording named a pin that no
   longer exists.)*
3. **4.1-measure — flip the flag in a corpus A/B**, measure S2 on `--key-breakdown` (Class A/C expected
   ↓; Class B flat). **Decision point:** ratify the `λ` direction; this is the second intentional
   behavior change (the first since the decoder went byte-identical), gated like 3.2 — measured,
   DCML-adjudicated, ratified, **with the chord-axis side effects measured** (BIR + snapshots; a key
   change re-scores chords). 
4. **4.2 — emit KeyArea spans** from the decode (coalesce equal-key windows; path-marginal confidence).
   Plumb to batch JSON + bridge. Gate: spans match the decoded per-window keys by construction.
5. **4.3 — partial-signature detector broadening** (the §3.3 Class-B emission fix), A/B'd **separately**
   from the path so the two effects are not conflated. Baroque + Jazz corpus gate per CLAUDE.md.
6. **4.x cleanup — remove** `promoteWinnerInPlace`, the `bestByCenter` family-selector, and
   `normalizedConfidence` (replaced by the path marginal), once 4.1 is the default. Re-pin the Stage-1c
   key tests to the decode (the wart pin becomes a "decode does not exhibit the wart" pin).

### 9.2 Risks

- **Riskiest assumption — the §3 derivation.** It says the path fixes only ~10% of S2 and the bulk
  needs emission work. If the provisional `λ` A/B (step 3) shows S2 *worsening* on Class B (the
  stickiness-entrenchment hazard), that **confirms** §3 and routes the bulk to 4.3/Stage-5 emission —
  it does not invalidate the path (KeyArea + Class A/C still stand). If, conversely, S2 improves more
  than §3 predicts, re-examine the `is_relative`/stem-fraction proxy (it is a *robust-signal* proxy,
  not a per-case causal read — §3.2 caveat).
- **`λ` too high → over-smoothing.** A high modulation penalty entrenches wrong keys (Class B) AND
  swallows genuine modulations (Class C false-negatives), and over-merges KeyAreas so Stage 6 sees
  spurious in-key tonicizations. `λ` is the central Stage-5 fit; the L1 + L2 gates bound it from both
  sides (S2 down, S1 not up).
- **Chord-axis ripple.** A key change flips diatonic-sensitive chord terms (`basisIndep`), so Baroque
  BIR and snapshots can move. This is *expected* and *gated* (step 3): movements must be DCML-correct.
  This is where the project's byte-identity era ends — Stage 4 is the second sanctioned behavior change.

### 9.3 Rollback

Flag-gated (`decodeKeyPath` default OFF) through 4.1; a single flag flip reverts to the pinned
argmax+hysteresis path. KeyArea emission (4.2) and the partial-signature broadening (4.3) are
independently revertible. No step removes the old path until 4.x, after the new default is ratified.

---

## §10 — Open questions for Cowork/user (genuine forks — not guessed)

- **OQ-1 — co-ratification with the Stage-6 contract.** `λ` controls KeyArea granularity, which *is*
  Stage 6's tonicization-vs-modulation boundary (§4.2). Should Stage 4's `λ` structure and the Stage-6
  label contract (precision_metric_design §3.1) be **ratified together**? *Recommendation: yes* — they
  are one decision surface (a key span boundary and a tonicization label are the same event seen twice).
- **OQ-2 — Class B routing (the §3 finding's fork).** Given the path fixes only ~10% of S2, do we:
  (a) ship Stage 4 as path-only (Class A/C + KeyArea + hysteresis fix) and route Class B entirely to
  Stage 5 emission fitting; or (b) **bundle** the partial-signature/key-profile emission work (4.3) into
  Stage 4 so it can claim a larger S2 slice? *Recommendation: (b) for partial-signature (it is a
  detector, not a fitted weight, and it is Baroque-structural), (a) for the relative-major/minor profile
  (that is genuinely a Stage-5 fit).*
- **OQ-3 — KeyArea confidence definition.** Path marginal via (i) best-path-minus-best-alternative-key-
  path over the span, or (ii) forward-backward posterior over the span? (i) is cheaper and decode-native;
  (ii) is the textbook marginal but needs a full FB pass. *Recommendation: (i)* unless Stage 6 needs a
  calibrated probability.
- **OQ-4 — emission top-N.** Decode over top-3 (today's surface, cheapest), top-8, or full 252? §3 shows
  51.6% of S2 has the correct key outside rank-2, so top-3 structurally caps the reachable S2. *But*
  widening N only helps Class A (Class B's correct key being rank-5 doesn't help if the path is sticky).
  *Recommendation: top-8 as a balance; full-252 only if a measured case needs it (mirrors the beam-revisit
  trigger discipline).*

---

*Drafted by CC, 2026-06-13, base `f8c6b3932a`. Read-only: the only repo write is this draft (HELD,
uncommitted). Probe `/c/tmp/s2_derive.py` (throwaway) reuses the committed metric machinery verbatim;
no production code changed. Awaiting ratification.*
