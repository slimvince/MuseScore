# Why does our key/mode inference not work? — the diagnosis (OI-141)

> **Status: READ-ONLY DIAGNOSIS (CC, 2026-07-12).** Executes
> `cc_instruction_key_mode_inference_diagnosis.md` against the Premise-Gate opening
> `cowork_key_mode_inference_diagnosis.md`. No `src/` change, no constant tuned, no golden
> refresh; `tools/robust_stop/` and `tools/corpus/` written to by nothing. Explorational,
> open-book: surprises here are findings (#3 scope rule), not stops — and there are several.
> The diagnostic MEASURES; the what-next decision is the user's (#8/#14).
>
> **Provenance / reproducibility (#16).** Corpus `c50002fee1` (pinned, 352 XMLs; 326/352
> WiR-covered per preset). HEAD `a5fb0065d3` (the Task-0 register commit). Reconciliation
> reference: `tools/a8_rebaseline_measure.py` on the frozen corpus (reproduces the ratified
> key column 68.13/64.43/67.50 exactly). Classifier: `tools/classify_key_disagreement.py`
> (this session, `feat(tools)`) — one loading substrate, reuses
> `compare_analyses`/`compare_rn`/`dcml_parser`/`run_bach_preset`/`measure_joint_probe`; the
> C++ probe instrument (`689840d2ef`) is **unchanged** (no dump field added — the zero-C++
> route). Machine-readable artifact: `tools/reports/key_mode_inference_diagnosis.json`.
> Both regression stops untouched (no production analysis moved).

---

## §0 — Headline (what the numbers say)

The ratified key metric grades **our per-region key against the DCML GLOBAL key**
(`a8_rebaseline_measure.py`, union-of-boundaries cells, duration-weighted). The failing
mass to explain is the ~32/36/32 % that disagrees. Classified read-only against the DCML
ground truth, that failing mass is **not mostly key-inference failure**:

1. **~½ of the failing mass is not a genuine inference error at all.**
   - **The tonicization/modulation label-gap dominates: 43.1 / 37.82 / 42.12 %** of failing
     duration (Baroque/Jazz/Default). Here **our region key equals the DCML LOCAL key** and
     differs only from the global — we correctly follow a real modulation, penalized solely
     because the metric grades against the global key. This is the largest single class on
     every preset. **The opening document predicted 15–30 % and predicted relative-key
     confusion (35–50 %) to be the largest — both PREDICTIONS FAILED.**
   - **Corpus transposition mismatch: 12 pieces = 12.36 / 11.08 / 12.13 %** of failing
     duration. These scores are **transposed relative to their When-in-Rome reference
     edition** (a constant whole-piece root offset) — our reading follows the notated
     signature, the reference is in another key. They are **100 % key- AND root-disagree by
     construction**, NOT inference error (§5). Removing them, key-agreement rises to
     **70.92 / 67.08 / 70.27 %** (from 68.13 / 64.43 / 67.50).

2. **Of the GENUINE local-key errors, the dominant type is being in the WRONG KEY AREA — not
   relative/parallel sibling confusion.** By our key's relationship to the in-effect (local)
   key, the failing mass splits: **dominant/subdominant-of-local 21.0 / 27.68 / 20.38 %**
   (reading V or IV as the tonic), **distant 17.8 / 21.3 / 18.1 %** (of which about half is
   the transposition contamination — clean-corpus distant is ~9.7 %), **relative 16.2 / 11.2
   / 16.4 %**, **parallel 1.6 / 1.7 / 1.8 %**. Wrong-key-area (fifth-off + distant) exceeds
   relative/parallel on every preset. This points at **anchoring, beam width, and
   hysteresis** (OI-94 un-re-anchored notated key change, OI-91 unfit priors, OI-97
   hysteresis margin), not primarily at relative-sibling disambiguation.

3. **The leading-tone (chord-hints) thesis, tested directly: the leading tone is present in
   ~57 % of relative-confusion duration (local anchoring), below the predicted ≥ 60 %.**
   Global-anchored it is only ~32 %. So decisive within-region evidence exists for a **slim
   majority** of relative-confusion cases — but (a) it is not the ≥ 60 % "silver bullet" the
   prediction expected, and (b) relative confusion is only ~11–16 % of the failing mass, so
   fixing it cannot move the headline much. **PREDICTION FAILED (both anchorings).**

4. **The true GLOBAL key is present-but-outranked in ~77 % of failing duration** (predicted
   55–70 % — **FAILED, above range**); absent in ~22 %. But "carried-but-outranked" is
   inflated by the label-gap (we outrank the global key with the *correct* local key), so it
   is not cleanly a ranking-failure signal.

**Plain answer to "why does key/mode inference not work":** on this corpus and metric, most
of the reported failure is **either the global-vs-local grading choice penalizing correct
modulation-following (~40 %), or a corpus transposition artifact (~12 %)** — together about
half. The genuine remaining inference errors are dominated by **wrong-key-area drift (a fifth
off, or distant)**, with relative/parallel sibling confusion a smaller share. The user's
functional-evidence thesis (leading tone) addresses the relative subset, where the evidence
is present only ~57 % of the time. *These are measurements; the what-next call is the user's.*

---

## §1 — Desk simulation (Task 1): five absent-key cases, hand-traced

Five regions where the ground-truth GLOBAL key is ABSENT from the carried
`keyAlternatives` menu, from five scores, hand-traced at the score signature, the WiR
annotation, our `.ours.json` keys, and the `--dump-joint-probe` carried menu. The question
per case: is the absence a **beam-width**, **hysteresis**, **late-anchor**, or
**segmentation** fact? The traces surfaced a **fifth mechanism the four-way question did not
list — corpus transposition** — and confirmed segmentation is not among them.

| # | region | our key | DCML global | mechanism (traced) |
|---|---|---|---|---|
| 1 | `bwv115.6@0` (5 measures) | G major | Eb major | **transposition** — score notated 1 sharp (G); every chord root is a constant +4 from WiR; our reading is correct *for our score*, the WiR edition is in Eb. The true key is "absent" because our score is genuinely in another key. |
| 2 | `bwv267@480` (~11.5 measures) | G major | Ab major | **transposition** — notated 1 sharp; constant −1 (=+11) root offset on 35/37 chords. |
| 3 | `bwv226.2@36960` (m21–25) | Bb major | G major | **beam-width / neighborhood drift** — after a-minor/e-minor excursions the analyzer settled onto the flat side; the 5–6-candidate menu carries Bb/Eb/F/g-min/c-min but **never G major** (it does carry g *minor*). The true key scored too low to be in the beam. |
| 4 | `bwv369@10080` (m6–8) | G major | e minor (local D) | **relative-major over-pull + hysteresis** — DCML local key is D here; we read D at m5 then flip to G (the relative major of the global e minor / subdominant of D) and stay. The global key is carried at the run edges but drops off the beam mid-run. |
| 5 | `bwv121.6@25920` (m14–16) | b minor | e minor (local b) | **label-gap, not an error** — our key equals the DCML LOCAL key (b minor); the global e minor is "absent" because we are legitimately in the local key. The absence is expected, not a failure. |

**Reading the desk sim.** Among absent-GT-key cases, the mechanisms are a MIX: transposition
(a corpus fact, cases 1–2), beam-width/hysteresis drift into a wrong neighborhood (cases
3–4), and correct local-following whose global key is trivially absent (case 5). **No traced
case was a segmentation fact** — consistent with the diagnosis running on the
segmentation-invariant union-of-boundaries unit (§2). These traces anchor the classifier's
cause definitions and its transposition detector below.

---

## §2 — The classifier: established before believed (Task 2)

**Unit and denominator.** Exactly the a8 unit: the union-of-boundaries cell grid, our region
key vs the DCML **global** key, duration-weighted. The failing mass = cells where our key ≠
global key at pitch-class identity (a8 `disagree`) plus cells whose key is unparseable (a8
`keyfail`). Runs are maximal touching failing cells of constant (our key, global key, local
key).

**Mechanical cause rules (stated, per the closed list).** Let K = our key, G = global, L =
DCML local key, each a `(tonic_pc, is_major)` via the ratified `_our_key_tonic` /
`_dcml_key_tonic` parsers. `collection(K)` = the relative-major tonic (major C and minor A
both → 0). Precedence, first match wins:

1. **enharmonic** — K = G at pitch class but spelled differently. **Impossible at this unit**
   (a8 compares pitch-class identity, so a pure respelling grades as *agree*); reported as a
   structural 0. Verified: 0 on every preset.
2. **tonicization/modulation** — K = L and L ≠ G (we match the in-effect local key; the
   disagreement is only against global-key grading — "would-agree-against-local"). Anchor-free.
3. **relative-key** — collection(K) = collection(ref), K ≠ ref (relative maj/min).
4. **parallel-mode** — tonic(K) = tonic(ref), mode differs.
5. **segmentation-edge** — run shorter than one measure (per-piece median inter-measure tick
   gap) AND both temporal neighbors key-agree AND a DCML local-key change lies within ± one
   measure (a real GT boundary placed at a different tick — WHERE not WHETHER).
6. **wrong-neighborhood** — ref absent from the carried menu AND ref not a collection-sibling
   of any carried key (the true key area was never offered).
7. else **UNCLASSIFIED** — counted, never forced; characterized by K's relationship to L.

Two anchorings of the reference `ref` are computed: **global-anchored** (ref = G, the
opening document's literal classes) and **local-anchored** (ref = L, the in-effect key — what
"true key" means musically and what our analyzer tracks). The local-anchored view is the
primary explanatory one; both reconcile.

**Establishment (#19), before any share was read.** The classifier's per-verdict scored
duration reconciles **EXACTLY** with a8 on all three presets (`class==fail` global=True,
local=True; agree/disagree/keyfail/scored all equal):

| preset | my disagree | a8 disagree | my keyfail | a8 keyfail | key-agree vs global | probe-join |
|---|---|---|---|---|---|---|
| Baroque | 2 635 920 | 2 635 920 | 7 680 | 7 680 | 68.1251 % | 10255/10255 (100 %) |
| Jazz | 2 938 320 | 2 938 320 | 10 800 | 10 800 | 64.4321 % | 9919/9919 (100 %) |
| Default | 2 662 560 | 2 662 560 | 33 120 | 33 120 | 67.4972 % | 10247/10247 (100 %) |

The carried menu comes from `--dump-joint-probe`, joined to the frozen regions by start tick:
the frozen `.ours.json` region stream matches the fresh probe stream **byte-for-byte** on
(startTick, endTick, key) for **100 %** of regions, so the menu-dependent flags
(carried/outranked, wrong-neighborhood) are exact. The standard `.ours.json` carries only a
single `keyModeRunnerUp`, not the menu, which is why the probe is run. Coverage: 326/352
scores per preset (26 lack WiR), reported beside every figure (OI-33).

---

## §3 — The predictions answered (Task 3)

Duration-weighted shares of failing mass, per preset (Baroque / Jazz / Default). Cause shares
are the **local-anchored** table (the primary explanatory view); the global-anchored table is
in the artifact and differs only marginally (relative and wrong-neighborhood shift ≤ 1.5 pp).

| prediction (opening doc) | measured (B / J / D) | verdict |
|---|---|---|
| **relative-key 35–50 %, the LARGEST class** | **16.2 / 11.2 / 16.4 %** — not largest | **FAILED** |
| **tonicization/modulation 15–30 %** | **43.1 / 37.8 / 42.1 %** — the largest | **FAILED (above)** |
| **parallel-mode 5–15 %** | **1.6 / 1.7 / 1.8 %** | **FAILED (below)** |
| **wrong-neighborhood 10–25 %** | **10.3 / 10.7 / 10.8 %** | **MET** |
| **segmentation-edge 5–15 %** | **0.22 / 0.28 / 0.19 %** | **FAILED (below)** — expected: the unit is segmentation-invariant by construction, so boundary artifacts are negligible |
| **enharmonic < 5 %** | **0 %** (structural) | **MET** |
| **present-but-outranked 55–70 %** | **77.8 / 76.9 / 77.2 %** carried | **FAILED (above)** |
| **leading-tone ≥ 60 %** | **32.0 / 32.7 / 33.6 %** (global-anchored); **56.7 / 53.7 / 58.6 %** (local-anchored) | **FAILED (both)** — a slim majority under local anchoring, not the ≥ 60 % expected |

**The dominant cause is the tonicization/modulation label-gap** (our key = the DCML local
key; disagree only vs the global grading). It is not an inference failure; it is the
global-key metric penalizing correct modulation-following. Six of eight predictions FAILED —
per #17/#3 the opening document's grounded estimates were built on an incomplete picture of
where the failure lives (a diagnosis-worthy outcome, not a defect in the predictions, which
were written to be checked).

**The genuine-error decomposition (our key vs the in-effect local key):**

| relationship to LOCAL key | Baroque | Jazz | Default | meaning |
|---|---|---|---|---|
| equal (label-gap) | 43.1 % | 37.8 % | 42.1 % | correct local-following, not an error |
| dominant/subdominant | 21.0 % | 27.7 % | 20.4 % | read V or IV as the tonic (a fifth off) |
| distant | 17.8 % | 21.3 % | 18.1 % | >a fifth away, not a sibling (~half is transposition, §5) |
| relative | 16.2 % | 11.2 % | 16.4 % | relative-key confusion |
| parallel | 1.6 % | 1.7 % | 1.8 % | parallel-mode confusion |

Excluding the transposed pieces (§5), the clean-corpus Baroque split is: equal 49.0 %,
dominant/subdominant 21.6 %, relative 18.3 %, distant 9.7 %, parallel 1.1 %. **Wrong-key-area
(dominant/subdominant + distant) is the largest genuine-error class on every preset**, ahead
of relative confusion.

---

## §4 — The leading-tone (chord-hints) thesis, answered

The user's thesis (OI-141): key/mode inference may need chord-derived FUNCTIONAL evidence
(cadences, leading-tone accidentals, progressions), since chord ROOTS alone cannot split
relative keys (the OI-43 probe measured that inert). The cheapest specific test — is the
minor key's raised seventh present in the region's sounding pitch classes for relative-key
runs whose true key is the minor sibling — gives:

- **local-anchored (true key = in-effect key): 56.7 / 53.7 / 58.6 %** present.
- **global-anchored (true key = piece global): 32.0 / 32.7 / 33.6 %** present.

So within-region leading-tone evidence exists in a **slim majority (~57 %) of relative-key
confusion duration** and our emission scoring is not using it there — supporting the thesis
for that subset. But it is **below the ≥ 60 % the prediction expected**, so the leading tone
alone is not decisive; and relative confusion is only ~11–16 % of the failing mass, so this
lever cannot move the headline much. The larger genuine-error class — dominant/subdominant
confusion — is plausibly addressable by the *broader* functional channel (recognizing a
cadential dominant as V-of-something rather than a new tonic), which this test does not
measure and which the certified-dormant Layer-5 cadence machinery already points at. *This is
measurement; the research-target selection is the user's.*

---

## §5 — Surprise: corpus transposition mismatch (a #9/#19 finding, new register row OI-142)

**12 of 326 WiR-covered pieces are transposed relative to their When-in-Rome reference
edition.** The signature is definitive: a **constant whole-piece root offset** (our chord
root minus the DCML root, mod 12) covering 81–100 % of aligned chords — the same piece,
shifted. Confirmed independently by the notated key signature, which matches OUR reading (the
transposed key), not DCML's, on the cases checked (e.g. bwv115.6 notated 1 sharp = G, DCML
Eb, offset +4). Our reading is correct *for our score*; the reference edition is in another
key. Each such piece is **100 % key-disagree AND 100 % root-disagree** (`fail_dur == scored`
for all 12) — pure corpus/ground-truth misalignment, not inference error.

The 12 (Baroque, offset from the WiR global key): `bwv126.6` (+2), `bwv267` (+11), `bwv180.7`
(+2), `bwv30.6` (+2), `bwv184.5` (+7), `bwv145.5` (+2), `bwv39.7` (+3), `bwv177.5` (+3),
`bwv244.62` (+10), `bwv73.5` (+3), `bwv148.6` (+1), `bwv115.6` (+4). They are **12.36 / 11.08
/ 12.13 %** of the failing mass. **Removing them raises key-agreement to 70.92 / 67.08 / 70.27
%** (from 68.13 / 64.43 / 67.50). Because they are also 100 % ROOT-disagree, they equally
contaminate the **root-agreement column (the hard regression stop, 63.36/62.37/63.25 %)** and
the class-(b) root-fail mass — a cross-cutting concern for the whole measurement substrate,
not only the key axis. Detection is a stated, reproducible mechanical rule
(`classify_key_disagreement._piece_transposition`, modal nonzero offset ≥ 70 % coverage);
the primary tables still INCLUDE these pieces (to reconcile with the a8 column, which also
includes them), with a clean-corpus companion view that excludes them. **Recorded as OI-142;
the disposition — re-transpose our editions to the WiR reference, exclude these pieces from
the graded set, or accept the caveat — is the user's.**

---

## §6 — Deviations, surprises, tooling

**Deviation from the opening document's cause list (surfaced, not hidden — #13).** The
opening document's six global-anchored classes leave a large UNCLASSIFIED remainder (28.3 /
37.9 / 27.5 % local-anchored) because the biggest genuine phenomena — dominant/subdominant
and distant confusion relative to the LOCAL key — are not named classes. I did **not**
force-fit them; UNCLASSIFIED is counted and characterized by the local relationship (§3
table). I added the local-anchored view and the transposition detector as read-only
refinements; both are established (exact reconciliation; the transposition rule is a stated
mechanical test cross-checked against the notated signature).

**Surprises (#3), all fact-grounded, none a build-time Premise-Gate failure (this is an
explorational run):**
- the label-gap dominates (metric grades vs global, our analyzer tracks local) — consistent
  with the CLAUDE.md cross-layer caveat, now quantified;
- wrong-key-area beats relative confusion among genuine errors;
- segmentation ≈ 0 (the robust unit is segmentation-invariant by design — the unit does its
  job);
- the leading tone is present in only ~57 % of relative cases, not the assumed silver bullet;
- corpus transposition (OI-142) — the largest single "surprise," a corpus-integrity fact the
  predictions did not anticipate.

**Tooling fixes made during the session (declared).** (1) A minor-key fifths cross-check table
I used for a *supplementary* transposition confirmation had two wrong entries; the primary
transposition evidence is the constant root offset (independent of that table), which stands —
the two cases it flagged (bwv145.5, bwv177.5) are confirmed transposed by the offset (95 %,
81 % coverage). No result depends on the buggy table. (2) The clean-corpus failing-mass
denominator initially excluded keyfail runs; corrected so shares sum and clean key-agreement
is exact. Both fixed before the reported run.

---

## §7 — Boundary honored + both stops untouched + self-check

- **Read-only w.r.t. production.** No `src/` change, no constant tuned, no golden refresh. The
  C++ probe instrument (`689840d2ef`) is unchanged (zero-C++ route). Only new code:
  `tools/classify_key_disagreement.py` (a sibling that reuses the one loading substrate — #6)
  + the artifact `tools/reports/key_mode_inference_diagnosis.json`. `tools/robust_stop/` and
  `tools/corpus/` written to by nothing.
- **Both regression stops green by construction** — no production analysis output moved (the
  classifier reads the frozen corpus and a read-only probe that returns before `writeJson`).
  Corpus frozen `c50002fee1`.
- **Establishment first (#19):** exact reconciliation to the ratified key column on all three
  presets; 100 % probe-stream join; enum-table faithfulness inherited from
  `measure_joint_probe._key_ident` (0 mismatch, re-used unchanged).
- **Self-check (mandated re-read of the diff):** ✅ classifier reuses the substrate, no second
  parser, no duplicated metric (grid + key_verdict recomputed via the same `crn` functions and
  proven equal to a8 by reconciliation). ✅ figures enter via the generated artifact + a8
  summary — no hand-transcribed measurement numbers (the §1 desk-sim table is hand-traced
  control flow, roots cross-checked at the dump). ✅ coverage (326/352) reported beside every
  figure (OI-33). ✅ no self-invented labels — cause classes use the opening document's names;
  the relationship descriptors (dominant/subdominant, distant, relative, parallel, equal) are
  plain words. ✅ every prediction answered met/failed with the number. ✅ every surprise and
  tooling fix declared. ✅ new discovery OI-142 gets its register row in the same commit.

*CC, 2026-07-12. The diagnosis, read-only, reconciled to the ratified column: about half the
reported key "failure" is the global-vs-local grading choice plus a corpus transposition
artifact; the genuine remainder is dominated by wrong-key-area drift, with relative confusion
(where the leading tone helps only ~57 % of the time) a smaller share. Measurement handed up;
the what-next is the user's (#8/#14). Fork-only; `upstream` untouched.*
