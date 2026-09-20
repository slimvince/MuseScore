# Step-Back Assessment + Investigations

*CC session 2026-06-08. Start HEAD `a693b6ba82`. Pessimistic-by-design assessment.*

---

## Part 0 — E3 cleanup

**Git state at start:**
- `M src/composing/analysis/chord/chordanalyzer.cpp` — working diff contained **only**
  Task 2 (`halfDimPulledFromRaw` + `results.pop_back()`) and Task 3 (three
  `kGate*Margin` constants + their three uses replacing `0.45f`/`0.20f`/`0.35f`).
  **No Task 1 content was present** — no winner-capture movement, no gate relocation
  outside the outer `inversionSuspicionMargin … && distinctPcs >= 3` guard. Task 1 had
  already been discarded (or never applied) in this working tree, so there was nothing
  to `git checkout --`.
- `M COWORK_HANDOFF.md` — a Cowork-owned doc update (records "E3 investigation complete").
  Left untouched per the standing rule that Cowork owns the handoff doc.
- 15 untracked files (ai-assistant/* = separate project; tools/*.txt = generated dumps).

**Actions taken:**
1. Rebuild (`setup_and_build.bat`) → `ninja: no work to do` — the binary already
   reflected exactly Tasks 2+3 (the prior session had rebuilt after removing Task 1).
2. Verified: `composing_tests` **407/407**; `pipeline_snapshot_tests` **11/11** (1
   intentional skip, no goldens refreshed).
3. `git add src/composing/analysis/chord/chordanalyzer.cpp` only; committed.

**New HEAD: `f9ba22157d`** — *"fix: remove G-E phantom HalfDim when no sub-gate fires;
float literals to named constants (E3 Tasks 2+3)"* (1 file, +16 −3).

**Working-tree state after Part 0:** `chordanalyzer.cpp` clean (committed). The only
remaining *tracked* modification is `COWORK_HANDOFF.md` (Cowork's doc, intentionally
left for Cowork to finalize). Untracked files are pre-existing non-code artifacts.

| Acceptance check | Result |
|---|---|
| composing_tests | ✅ 407/407 |
| pipeline_snapshot_tests | ✅ 11/11 (no goldens updated) |
| G-E phantom fix committed | ✅ |
| Named constants committed | ✅ |
| Gate decoupling (Task 1) | ✅ not committed / not present |
| Working tree after Part 0 | ✅ clean apart from the Cowork-owned `COWORK_HANDOFF.md` |

---

## Part 1 — Architecture assessment

### Q1 — Baroque BIR=false=16: is the wall real?

Baseline re-confirmed this session after a fresh Baroque corpus regen:
**BIR=true=25, BIR=false=16**. Full enumeration with ticks captured.

The headline finding: **the "evidence-absent (5)" bucket is mislabelled and is not one
mechanism — it is at least three, and two of the five are actually the same
absent-OUR-root family as the "actionable" Sub-9b case.** I dumped the actual Baroque
regions (pcWeights, bass, neighbours) for all five:

| Case | tick | our read | pcWeights (region) | DCML root present? | True mechanism |
|---|---|---|---|---|---|
| bwv245.17 | 4800 | F/D | {A:1.8,C:.4,F:.4,B:.2,**D:.2**} | D at threshold; D7's 3rd **F# absent** | **(a) genuine** — F natural sounds, A dominates → F major is acoustically right; DCML labels implied dom7. Same as Maj→Dom7 family. |
| bwv17.7 | 46080 | A/Eb | {A:.6,Db:.2,**Eb:.2**} | Eb at threshold; half-dim's Gb **absent** | **(a) sparse dim/half-dim rotation** — tritone (Δ=+6) enharmonic ambiguity on a 3-PC slice. wDim can't fire (needs ≥4 PCs). |
| bwv174.5 | 6240 | E/G# | {B:.6,Gb:.2,**Ab:.2**} — **E (our root) absent!** | DCML root G#=Ab **present** (it's the bass) | **absent-OUR-root** — we invent an E that is not sounding; DCML's G#m7 root is present. Same family as Sub-9b. |
| bwv301 | 960 | G/A | {B:1.25,D:1.25,A:1.05,C:.25,Ab:.2} — **G (our root) absent!** | DCML root B **strongly present (1.25)** | **absent-OUR-root + mild over-merge** — we invent G; B is the strongest tone. dur=2 beats with foreign C/Ab minority tones → a (b)-segmentation flavour on top. |
| bwv381 | 4800 | G6/F# | {D:.5,E:.5,B:.5,G:.25,Gb:.25} | E present (0.5); G also present | **6th-vs-m7 template tie** (the B4 item) — {E,G,B,D} = Em7 = G6; DCML picks Em7, we pick G6. |

**Direct answers:**

- **Does any of the 5 look like (b) segmentation rather than (a) non-harmonic bass?**
  Only **bwv301** has a segmentation flavour — a 2-beat region carrying foreign minority
  tones (C, Ab) that dilute a strongly-present B. But its *primary* defect is
  absent-root promotion, not pure over-merge, so it is not a clean (b). None of the
  five is a clean "short adjacent event absorbed" case in the way bwv269/bwv432 (the
  declared segmentation pair) are.

- **The genuinely useful re-classification:** the "evidence-absent" label "DCML root not
  in pcs" is **inaccurate for bwv174.5 and bwv301** — in both, the DCML root *is*
  present (strongly so for bwv301) and it is **our** root that is absent from the
  sounding tones. These two are the **same absent-root-winner mechanism as the Sub-9b
  bwv14.5 case** that the handoff already flagged as "Actionable — absent-root guard."

**Re-openable with current tooling (no Phase D/E):**
- **Highest value — absent-root winner guard.** It would target **3 cases** (bwv14.5 +
  bwv174.5 + bwv301), not the 1 the handoff implies, because the bucket conflates two
  mechanisms. All three share a clean signature: winner `pcWeight[rootPc] ≈ 0` while a
  present-root alternative sits within a small margin. The prior attempt (inversion-
  deduction-block guard, L2839–2880) regressed 5 snapshots because it was scoped to the
  wrong block; a guard scoped to the **final winner-selection** in `applyHarmonicFunction`
  (reject a winner whose root PC weight ≤ extensionThreshold when a within-margin
  present-root alternative exists) is worth a fresh, narrowly-scoped attempt. This is the
  single best re-openable item in the Baroque set.
- **Marginal — bwv381 (B4 6th-vs-m7 tie).** Re-openable as an Em7-vs-G6 root preference,
  but B4 is correctly flagged "needs analysis first" (adding {0,4,7,9}/{0,3,7,9} templates
  creates new ambiguities); not low-risk.
- **Not re-openable without Phase D/E:** bwv245.17 and the F#-absent half of bwv17.7
  (genuine DCML-implied-function — the defining third is absent); the 5 Δ=+7
  rootContinuity cases (Iter 98 dead end — sparse-suppression regresses Alberti-bass);
  the sus/quartal/whole-tone placeholders (no template); bwv269/bwv432 segmentation.

**Verdict:** the wall is *mostly* real, but it is ~2–3 cases softer than the handoff
implies. The "evidence-absent 5" is not 5 dead cases — it is 1 genuine implied-function
case (bwv245.17), 1 sparse-rotation case (bwv17.7), 2 absent-root cases that belong with
the actionable Sub-9b guard (bwv174.5, bwv301), and 1 template-tie (bwv381).

### Q2 — Jazz BIR=false=10: prior expectations (stated before Part 2)

The Jazz preset differs from Baroque only in scoring weights (same pitches), the load-
bearing ones being `extensionThreshold=0.12` (vs 0.20) and
`maxTotalInversionContextBonus=0.6` (vs 2.5).

- **Lower `maxTotalInversionContextBonus` (0.6) → fewer inversion/slash promotions.**
  Prediction: Jazz should make **fewer absent-root / spurious-inversion errors** than
  Baroque, because the very bonus that drives "promote a rootless first-inversion read"
  is throttled. I expect the Baroque absent-root cases (bwv14.5, bwv174.5, bwv301) to
  largely *disappear* under Jazz.
- **Lower `extensionThreshold` (0.12) → more tones count as "present" → richer chords.**
  Prediction: Jazz should produce **more extended-chord readings** (7ths/6ths/9ths), so
  I expect *new* Jazz-specific errors of the "added-tone tetrachord read as a 7th
  inversion" type that Baroque's stricter threshold suppresses.
- **Net:** I expect Jazz BIR=false to be a near-subset of Baroque's (the shared Δ=+7,
  sus/quartal, and dim→dom cases survive both because they are weight-independent) plus
  a small number of Jazz-only extension-driven cases. I expect the Δ=+7 cluster to
  reappear unchanged (it is a temporal-context bonus, not a threshold effect).

### Q3 — Minimum viable Phase E

The function-layer shell exists and is wired in: `applyHarmonicFunction` owns winner
selection and already consumes `HarmonicFunctionContext` (keyFifths, keyMode,
previousRootPc, nextRootPc, previousBassPc/nextBassPc) via `rootContinuityBonus`,
`wSeqBonus`, `wDimBonus`, `stepBonus`. What's missing is **functional state about the
neighbours** — their *quality* and *confidence*, and a persisted cadence flag.

**Would a simple "did the previous chord resolve stepwise to this root?" signal suffice?**
- For **A2 (dominant quality in minor)** and **B1 (mMaj7)**: *partially yes* — both turn
  on the same question, "is there a V→i (down-a-P4) cadential resolution adjacent to this
  region?" The root-motion half of that signal **already exists** (`wSeqBonus` keys on
  `nextRootPc` a P4 below). What's missing is wiring it to **gate quality** (promote a
  thirdless degree-5 to major V when the next root is a P4 below; block mMaj7 when the
  current root's "leading tone" is in a resolving-dominant context). A stepwise/root-
  motion cadence tag is enough to *unblock* these two; it will not make them *robust*
  (distinguishing a true jazz i(maj7) from a Baroque V-with-suspension needs the next
  chord's function, i.e. E4-grade cadence detection).
- For the **Δ=+7 rootContinuity cluster (5 cases)**: *no.* Iter 98 proved that suppressing
  rootContinuity on sparse/stepwise predecessors regresses Alberti-bass textures, which
  *genuinely* need that continuity. Separating bwv320 from Mozart K280 needs
  **tonic-prolongation reasoning** (is the continued root the local tonic being
  prolonged, or a passing artifact?), which is strictly harder than a stepwise signal.

**First concrete structure that must exist:**
1. Extend `HarmonicFunctionContext` with **previous/next region quality and a
   confidence/distinctPcs field** (today it carries only neighbour root/bass PCs).
2. A new **post-function "cadence-evidence" pass** that walks the region sequence and
   tags each region T/PD/D from root motion + scale degree (a V→I down-a-P4 with
   dominant-flavoured quality → tag "cadential dominant"). This is the cadence-evidence
   accumulator the question asks about — a single forward pass, not a per-cell bonus.
3. Two conditional quality gates in `applyHarmonicFunction` keyed on that tag (A2 promote;
   B1 block).

**Estimate (honest):**
- Minimum viable that unblocks **A2 + B1 (2 of 3)** via a *root-motion-only* cadence tag:
  **~1–2 weeks** of CC work. Risk: the tag will misfire on deceptive cadences and
  non-cadential P4 motion, so expect a calibration loop against both BIR presets.
- A version robust enough to also touch the **Δ=+7 cluster**: that needs E4-grade cadence
  detection (metric position, suspension resolution, PAC vs HC) plus tonic-prolongation
  tracking — **1 month or longer**, and it is the E4 roadmap item the architecture note
  already sequences before E5.

So: the minimum addition unblocks A2 and B1 in ~1–2 weeks; the Δ=+7 cluster (the largest
single Baroque category) stays blocked behind real E4 work.

---

## Part 2 — Jazz BIR=false=10 characterisation

Regenerated Jazz corpus (353/353); `characterise_bir_false.py` reports **10 genuine
BIR=false cases — matches the baseline.** Jazz BIR=true=36 also confirmed.

| # | Score | Region | Analyzer | DCML | Δ | Mechanism | Actionable now? |
|---|---|---|---|---|---|---|---|
| 1 | bwv244.15 | m6 b1 t10080 | Bm/D | G major (IV6/4) | +4 | **Root mis-selection** — {D,G,B}=G major 2nd inv read as Bm/D; key conf 0.00, G not even in alts | No (key-driven) |
| 2 | bwv245.17 | m3 b2 t4800 | F/D | incomplete D7 | +3 | **Evidence-absent** — F# absent, A dominant; F major acoustically right | No (Phase D/E) |
| 3 | bwv245.28 | m3 b2 t4320 | B6/G# | E major (V6) | +7 | **rootContinuity Δ=+7** | No (Iter 98 dead end) |
| 4 | bwv245.40 | m27 b3 t51360 | F7sus/Bb | quartal trichord | +2 | **Sus/quartal placeholder** | No (no template) |
| 5 | bwv296 | m12 b4 t23040 | D6/B | G major (I6) | +7 | **rootContinuity Δ=+7** ({D,G,B}=G major) | No (Iter 98 dead end) |
| 6 | bwv320 | m27 b1 t37440 | G6/E | C major (V6) | +7 | **rootContinuity Δ=+7** (the canonical Iter-98 case) | No (Iter 98 dead end) |
| 7 | bwv422 | m14 b1 t23040 | A7sus/D | quartal trichord | +2 | **Sus/quartal placeholder** | No (no template) |
| 8 | bwv432 | m3 b3.5 t5520 | Am/E | minor triad (vi) | +5 | **Segmentation** — viio7→i→V2 over-merge | Maybe (risky) |
| 9 | bwv45.7 | m11 b2 t20160 | F#7/E | diminished triad | +8 | **dim→dom absent-root** — {A#,C#,E}=A#° read as rootless F#7 (V42); F# absent | Partial (absent-root guard) |
| 10 | bwv74.8 | m7 b4 t13440 | Em7/D | maj-2nd major tetrachord (I) | +4 | **Added-tone tetrachord** — {C,D,E,G}=Cadd9 read as Em7/D; the B4 6th/add ambiguity | No (B4 needs analysis) |

**Jazz vs Baroque BIR=false set:**
- Shared (8): bwv245.17, bwv245.28, bwv245.40, bwv296, bwv320, bwv422, bwv432, bwv45.7
- Jazz-only (2): **bwv244.15, bwv74.8**
- Baroque-only (8, Jazz gets right): bwv102.7, bwv261 (Δ=+7), bwv17.7, bwv174.5, bwv301,
  bwv381 (evidence-absent / absent-root / template), bwv269 (segmentation), bwv14.5 (Sub-9b)

**Mechanism distribution (Jazz):** Δ=+7 rootContinuity ×3 · sus/quartal ×2 · evidence-
absent ×1 · segmentation ×1 · dim→dom absent-root ×1 · Jazz-specific root/template ×2.

**Comparison to Q2 priors — confirmed, no surprises:**
- *Lower `maxTotalInversionContextBonus` → fewer inversion/absent-root errors:* **confirmed.**
  Jazz drops exactly the Baroque absent-root inversion cases (bwv14.5, bwv174.5, bwv301)
  and the bwv381 6th-inversion tie — the throttled inversion bonus no longer promotes the
  rootless first-inversion readings. Jazz's 10 < Baroque's 16 is driven by this.
- *Lower `extensionThreshold` → new extension-driven errors:* **confirmed.** The single
  clearest Jazz-only case, **bwv74.8**, is exactly this: the 0.12 threshold admits the D
  as a 7th, so {C,D,E,G} (a Cadd9/I) reads as Em7/D instead of C — Baroque's 0.20
  threshold leaves it correct. bwv244.15 is the other Jazz-only case (a key-confidence-0
  root mis-selection, not weight-driven).
- *Δ=+7 reappears unchanged:* **confirmed** — all three Δ=+7 cases (bwv245.28, bwv296,
  bwv320) are weight-independent temporal-context mis-fires, identical to Baroque.

**Actionable now without Phase D/E:** essentially none cleanly. The only partial lever is
the **absent-root guard** (bwv45.7's rootless-F#7 promotion, plus the Baroque trio it
would address) — the same item surfaced in Q1.

---

## Part 3 — Min→Maj / Maj→Min quality confusion

Extracted every Min→Maj and Maj→Min `quality_disagree` case from the `f3e0f5f72c`
cross-corpus snapshot (`live_20260603`, Standard preset, 9 non-Bach corpora), with tone
evidence (m3/M3 pcWeight, bass, noteCount). Counts match the baseline exactly:
**Min→Maj 714, Maj→Min 467.**

**Structural fact (categorical, from the classifier):** every `quality_disagree` case has
**root_pc agreeing** by construction. So in **all 1,181 cases the analyzer's root equals
DCML's root** — these are quality calls on the *same root*, never root-confusion that
slipped the root filter. (Answers Step 3b/3c point 5 definitively: not a slash/root-
assignment problem.)

### Third-presence distribution (threshold 0.20)

| | both thirds | only m3 | only M3 | **neither** | bass==root |
|---|---|---|---|---|---|
| **Min→Maj (714)** | 4 | 187 | **1** | **522 (73%)** | 568 (80%) |
| **Maj→Min (467)** | 3 | **5** | 100 | **359 (77%)** | 367 (79%) |

Two facts jump out:

1. **~75% of both directions are thirdless** (neither third present above threshold) —
   single notes or root+fifth dyads (many noteCount=1). With no third sounding, the
   analyzer assigns a quality from key/degree context and lands on the opposite colour
   from DCML's functional label. The disagreement RN pairs are overwhelmingly degree
   disagreements: `v→V`, `ii→V`, `iii→V`, `viio→V` (Min→Maj) and `bV→viio`, `bVII→ii`,
   `I→i` (Maj→Min). **This is the same wall as the deferred A2 (dominant-quality-in-minor)
   and key_disagree (15.4%) — a key/functional-context problem, not a scorer-picks-the-
   wrong-third bug.**

2. **When a third IS present, the analyzer matches it.** Min→Maj has only **1** case where
   the M3 sounds while we say minor; Maj→Min has only **5** where the m3 sounds while we
   say major. So the scorer is *not* mis-ranking a present third. The "one-third-present"
   minorities (187 / 100) are cases where the sounding third **agrees with our reading**
   and DCML **overrides by function**:
   - *Min→Maj, m3 sounding (187):* DCML labels are `III`/`I`/`V` — same-degree case flips
     (`iii→III`, `i→I`, `v→V`) where DCML reads the chord as major despite a sounding
     minor third (modal mixture, enharmonic/secondary-dominant spelling, or the m3 being
     a non-harmonic tone in DCML's functional parse).
   - *Maj→Min, M3 sounding (100):* DCML labels are dominated by `i` (27), `ii6`, `iv6`,
     `v` — a sounding **major** third on a scale degree DCML calls **minor** (raised
     third / picardy / applied-dominant inflection, e.g. Corelli op01n02a m2 G# sounds,
     we say I6, DCML says i). DCML labels the scale degree by function; the major third
     is a chromatic alteration in its grammar.

### Mechanism summary

- **Dominant mechanism, both directions (~75%): thirdless quality-guessing entangled with
  key/degree detection.** Not "third-presence" in the scorer sense — there is no third to
  score. This is the A2 / key_disagree family.
- **Minority (~25%): DCML function-over-sonority convention.** The sounding third agrees
  with our reading; DCML overrides via modal mixture, raised/lowered thirds, secondary
  dominants, picardy, or enharmonic spelling. In these the analyzer is acoustically
  reasonable and DCML is labelling function — analogous to the Maj→Dom7 finding (DCML
  labels implied function). A sliver could be Phase D (the present third is a genuine
  passing/appoggiatura tone).
- **Ruled out:** *bass-root bias* (bass==root in ~80% — these are root-position, not
  slash-inversion artifacts); *third-presence scorer bug* (the scorer matches a present
  third); *root-confusion* (root agrees by construction).

**Same mechanism for both directions?** **Yes — they are mirror images of one mechanism**
(thirdless quality-guess + key/degree disagreement, ~75%; symmetric function-override
convention, ~25%), not two distinct phenomena.

**Fixable with a targeted scoring/gate change?** **No.** The thirdless majority has no
evidence for a gate to act on and is entangled with key detection (the A2 / keyConfidence
dead end — no bimodal gap). The convention minority needs functional reasoning (Phase E).
A non-trivial fraction of these "errors" are DCML convention rather than analyzer defects,
so the *true actionable defect rate* inside `quality_disagree` is well below the headline
6.3%.

---

## Summary

The project is in a genuinely good but plateaued state: Part 0 banked two clean E3
fixes (HEAD `f9ba22157d`, 407/407 · 11/11), and the BIR baselines hold (Baroque 25/16,
Jazz 36/10, both re-confirmed against fresh corpora this session). The two largest open
investigations both resolve to the **same conclusion**: the dominant residual mechanisms
are functional/key-context problems, not scoring bugs. Part 3 is the sharpest result —
~75% of the 1,181 Min↔Maj quality disagreements are *thirdless* sonorities where the
analyzer guesses quality from key context and lands opposite DCML's functional label
(the A2 / key_disagree wall), while the remaining ~25% are DCML labelling function over a
sounding third the analyzer correctly heard; **none is a scoring/gate target, and a real
fraction are DCML convention rather than defects.** Part 2 confirmed the Jazz preset's
priors exactly: throttled inversion bonus removes Baroque's absent-root errors, while the
lower extension threshold adds extension-driven ones (bwv74.8), and the Δ=+7 cluster
reappears unchanged. The one genuinely actionable thread that surfaced *independently in
all three parts* is the **absent-root winner guard**: Q1 re-classification shows it would
address 3 Baroque cases (bwv14.5 + bwv174.5 + bwv301, not the 1 the handoff implies,
because the "evidence-absent" bucket conflates DCML-root-absent with our-root-absent),
and Part 2 shows the same mechanism in Jazz bwv45.7 — a guard scoped to the final
winner-selection in `applyHarmonicFunction` (reject a winner whose root PC weight ≤
extensionThreshold when a within-margin present-root alternative exists) is the highest-
leverage next step that needs **no Phase D/E**, provided it is scoped narrowly enough to
avoid the 5-snapshot regression the earlier deduction-block attempt hit. Beyond that, the
honest picture is that the high-value items (A2, B1, the Δ=+7 cluster, and the bulk of
the cross-corpus quality/key disagreements) are all blocked on the **same Phase E
cadence-evidence work** — a ~1–2-week root-motion cadence tag unblocks A2 and B1, but the
Δ=+7 cluster and robust functional labelling need genuine E4 cadence detection (1 month+).
