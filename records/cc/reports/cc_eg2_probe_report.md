# cc_eg2_probe_report.md — EG-2: the E0 instrument established, then the rebuilt-vs-legacy probe

> **HELD for Cowork** (gitignored). Executes `cc_instruction_eg2_establish_and_probe.md` (Cowork,
> session 36) under the Premise Gate (CLAUDE.md #17–#19) and the pre-registered ledger
> `cowork_eg2_scoping.md` (§5 predictions RECORDED before this probe existed; the verdict is read
> AGAINST them, never adjusted to them). **Findings only — NO recommendation to build; the go/no-go
> decision is handed UP (#8).** Tasks 1–2 are instrument establishment (surprise ⇒ STOP #13); Task 3
> is read-only explorational (surprises are findings). No production behavior change: no constant
> tuned, no golden refreshed, `tools/robust_stop/` untouched, no adoption. HEAD `33c390bbc7`, corpus
> `c50002fee1`.

---

## 0. Precondition note (Task 0)

HEAD is `33c390bbc7` (after the desk-sim commit `3d8cf74e52`, ✓). The working tree carried, at
session start, one **foreign** uncommitted item — `cowork_joint_key_chord_design.md` (an 11-line
arc-#12 SHELVED banner, documentation-only, unrelated to EG-2) — plus the staged deletion of the
gitignored instruction file (the intended EG-2 handoff, Task 4 re-adds it) and untracked scratch.
None touch code, corpus, the E0 harness, or the robust-stop reference, so none can perturb the
instrument or the measurement. I left the foreign doc edit **untouched** and did not stage/commit it.
Recorded here rather than treated as a hard STOP because it is inert to every Task-1/3 object.

---

## 1. ESTABLISHMENT RECORD (Task 1 — the #19 instrument, established)

### 1.1 Exact invocation (Task 1.1) + the override-OFF variant (Task 1.2, gap G3)

The E0 chain is `batch_analyze --dump-fullspine` (return-early diagnostic; production never reached).
The probe arm additionally needs the §5.5 case-4 fine-grain override DISABLED (G3 — the Tier-1 T1-2
armed trap, measured net-harmful −756; `functionresolver.cpp:529-531`, unconditional). **The disable
uses the EXISTING dormant θ, not a new mechanism:** `attemptFineGrainOverride` fires ONLY through
`OnePassClosure::tryOverride` → `overrides(c, S) = S > baseBar + confidenceScale·c`
(`forwardoverride.h:80-100`, `functionresolver.cpp:468`). Raising `FunctionResolverParams.override.
baseBar` impassably high (1.0e9) makes `overrides()` always false, so the override returns at
`functionresolver.cpp:469` **before any mutation / forwardRecompute** — Phase-1 abstain resolution
(`resolveAbstained`) untouched.

Because the driver called the resolver with default params, one **minimal default-OFF flag**
`--fullspine-no-override` was added to the diagnostic driver only (`tools/batch_analyze.cpp`
`runFullSpine` + dispatch + `tools/run_bach_preset.py` pass-through). **A second additive field —
`pitchClassSet` — was added to the fullspine `regions[]` emit** (= `ctx[i].pcMask`, the slice's
sounding pcs, the same semantic as the standard path's `pitchClassSet` = `r.pcMask`): the a8 robust
grader's `cell_class()` reads it to run the symmetric-sonority test (dim7/aug/whole-tone/share-tone →
class-(a)); **without it every root-fail would misclassify as class-(b), biasing against rebuilt.**
Both changes are driver-only, additive, and confined to the (default-OFF) fullspine path.

Effect verified at objects on `bwv10.7` (Default): override ON fires 3 overrides (e.g. `@5760` root
0→3, over-turning the L4 commit); override OFF → 0 overrides, roots revert to the L4 argmax. So the
probe arm measures **decoder carry + argmax + the as-built L5 abstain-resolution/cadence/modulation
arms, MINUS the override** — the G3-declared lower bound on the intended selection.

### 1.2 Production byte-identity re-proven (Task 1.2)

- **Suites:** composing **1101/1101** (2 disabled), notation **53** (3 skipped), pipeline_snapshot
  **11/11 — NO golden refresh**.
- **Standard corpus regen (flag OFF, Baroque) → diff vs committed `tools/corpus/baroque`: 0 diffs /
  352 files.** The two additive changes live only in the fullspine path; the production `writeJson`
  path is byte-identical by construction and by measurement.

### 1.3 Fresh stamped dumps + reproduce-check (Task 1.3/1.4)

Dumped Baroque + Default (Jazz consistency-only) with `--dump-fullspine --fullspine-no-override` to
fresh scratch (`C:/tmp/eg2/fs{1,2}/<preset>`, NOT the validated `tools/corpus/<preset>`). Each dir
carries a `run_bach_preset.py`-stamped `corpus_manifest.json`: **git_hash `33c390bbc7`, complete,
352/352**, corpus inputs unchanged since `c50002fee1` (`git status tools/corpus/*.xml,*.music21.json`
clean; the legacy `tools/corpus/baroque` manifest is git_hash `c50002fee1`).

**Reproduce-check (each dump run TWICE, diff run1 vs run2):** **0 content-diffs / 352 files** for
BOTH Baroque and Default, excluding the two `wallTimeLegacyMs`/`wallTimeDecodeMs` lines (wall-clock
timing — definitionally non-reproducible, and never read by the a8 grader). The analysis content is
fully deterministic (the R10-b identity lesson honored, with the timing exclusion declared).

*(One transient artifact: on the first Default run, `bwv272`'s post-run `compare_files` returned a
non-zero subprocess exit (empty stderr — the known Qt/offscreen parallel-subprocess flake), marking
that run's manifest incomplete. The `.ours.json` WAS written and 3 standalone re-runs produce
byte-identical output (120327 bytes); the second Default run is complete and validated. Not analysis
non-determinism — the content is deterministic. The canonical Default arm is the complete run `fs2`.)*

### 1.4 Coverage-equality — the P4(c) insulation check (Task 1.5) — DIAGNOSED and RESOLVED

**The a8 unit anchors the DCML (When-in-Rome rntxt, no `abs_tick`) ground truth to ticks by
reconstructing measure anchors FROM the arm's own regions (`compare_analyses._dcml_time_spans` →
`_build_measure_anchors`/`_dcml_tick_for`).** This reconstruction is granularity-sensitive:
`_dcml_tick_for` **interpolates** the tick for any measure with no region-anchor. The coarse legacy
arm (~27 regions/piece) leaves some measures un-anchored → interpolated (approximate) DCML positions;
the fine per-slice rebuilt arm (~86 regions/piece) anchors nearly every measure → exact positions. So
graded each-arm-own-anchor, **128/326 pieces show DCML span-boundary shifts (~one beat) and 160 total
mismatches**; scored duration differs 8349600 (rebuilt) vs 8293680 (legacy) = **+0.67 %**. This is
exactly the scoping-doc P4(c) hole: the unit is segmentation-invariant WITHIN an arm, not ACROSS arms
with different anchor inference.

**Resolution — a common anchoring + an intersection restriction (added to the read-only probe, not to
the pinned a8 instrument):**
- Grading both arms against a **common DCML anchoring** (the rebuilt/fine positions, the most
  accurate) removes the boundary shifts (128 → 0); a residual 48 pieces still differ in scored_dur,
  all because the per-slice rebuilt arm COVERS MORE ticks (pickup/trailing) than the coarse legacy
  regions — a superset that **handicaps** rebuilt (more spans to err on).
- The **intersection mode** grades both arms on EXACTLY the `ours ∩ ours ∩ DCML` cell set →
  **scored coverage byte-exactly equal (8296320 = 8296320, n_mismatch = 0** on all three presets).

**Grader faithfulness proven at objects:** the probe grader is abstain-aware (see §2), but on the
all-committed LEGACY arm in own-anchor mode it reduces EXACTLY to the pinned a8 instrument —
`b_cls_b_dur` = **2932400 (Baroque) / 2936000 (Default)**, byte-identical to the committed
`tools/robust_stop/` reference; `b_cls_a_dur`, `b_cls_b_cells`, `root_agree_pct` (63.3581 %) all
reproduce. The per-piece variant-b bucket decomposition self-validates against
`grid_score_regions()`.

### 1.5 GATE (Task 2): the instrument is ESTABLISHED

Every Task-1 item is green: invocation derived at source; override-OFF via the dormant θ, verified;
production byte-identical (0/352 + suites); reproduce-check byte-identical (0/352 excl. timing);
coverage-equality diagnosed (the P4(c) measure-anchor confound) and RESOLVED to exact equality
(intersection mode); grader reproduces the committed reference exactly. **The probe number below is
produced by an established instrument (#19).**

---

## 2. THE PROBE (Task 3, read-only) — class-(b) root-disagree DURATION, abstain-aware

**The metric (the robust-stop hard-stop quantity):** class-(b) (pitch-class-decidable-root)
root-disagree DURATION, variant-b, root axis, same `cell_class()` machinery as the robust stop. **One
required adaptation (declared):** the rebuilt per-slice arm ABSTAINS (`rootPitchClass = -1`) on ~18 %
of scored duration; `classify_pair` scores an abstain as `root_err`, but the two-tier policy + E0
report §4-C define class-(b) as a wrong COMMIT — an abstain is coverage-loss, NOT class-(b) (otherwise
a decrease could never be predicted, as §5 does). So a root-failing cell is bucketed: committed &
wrong → `cell_class` (a/b); abstain → coverage-loss. On the all-committed legacy arm this is identical
to a8 (proven, §1.4).

### 2.1 The number (Task 3.1) — coverage-equal intersection mode (the airtight column)

| Preset | rebuilt class-(b) dur | legacy class-(b) dur | Δ dur | **Δ %** | own-anchor Δ % (confounded) |
|---|---|---|---|---|---|
| Baroque | 2 535 200 | 3 017 720 | −482 520 | **−15.99 %** | −13.32 % |
| Default | 2 529 800 | 3 021 320 | −491 520 | **−16.27 %** | −13.62 % |
| Jazz *(consistency-only, EG-6 — no correctness claim)* | 2 525 840 | 3 083 600 | −557 760 | −18.09 % | — |

The raw class-(b) DURATION **decreases** on both correctness presets by ~16 %, robust across all
anchorings (own −13 %, legacy-anchor −16.1 %, rebuilt-anchor −15.8 %, intersection −16.0 %). **On the
literal robust-stop criterion this lands in the §5 aggregate prediction band (−15…40 %).**

*(Note: the legacy class-(b) in intersection mode (3 017 720) differs from the self-anchored committed
reference (2 932 400) ONLY because both arms are graded against the common rebuilt anchoring; the Δ is
computed within one consistent anchoring, which is what makes it valid.)*

### 2.2 ★ The decomposition that changes the reading — the decrease is an ABSTENTION ARTIFACT

The duration decrease is **not** a per-commit accuracy gain. Decomposed on the coverage-equal
intersected cells:

| | Baroque | Default |
|---|---|---|
| rebuilt committed fraction of scored dur | 82.4 % | 82.3 % |
| **rebuilt class-(b) rate on COMMITTED cells** | **37.11 %** | **37.06 %** |
| **legacy class-(b) rate on committed cells** | 36.37 % | 36.42 % |
| per-committed delta | **+0.73 pp (WORSE)** | **+0.64 pp (WORSE)** |

**Per committed cell, the rebuilt arm is marginally WORSE than legacy.** The entire −16 % duration
reduction is bought by committing on 18 % fewer ticks. And the abstention is **not** precision-selective —
decomposed against legacy on the same cells (Baroque, 1 464 060 abstain-ticks):

- **47 %** land where **legacy was RIGHT** → a coverage REGRESSION (rebuilt dropped a gettable root);
- **51 %** land where legacy was WRONG class-(b) → a GOOD abstain (avoided a wrong commit);
- 2 % class-(a).

Default is identical (47 % / 51 %). The abstention is a near coin-flip, not a "hard-cases-only"
filter. **So the robust-stop metric — designed for a commit-everywhere path — is moved the predicted
direction by abstention, a lever §5 did not anticipate, while the underlying root accuracy is
flat-to-slightly-worse.**

### 2.3 The explained set-diff (Task 3.2) — class-(b) runs, Baroque intersection

3 369 class-(b) runs **fixed** by rebuilt (legacy-broken, rebuilt-not); 4 130 **newly broken** by
rebuilt (rebuilt-broken, legacy-not). Full enumerations in `C:/tmp/eg2/probe_isect/baroque_{fixed_by,
new_broken_by}_rebuilt.txt`. All are cls=b by construction.

**New-broken interval census (our_root − dcml_root, mod 12):** the dominant new-error class is
**fifth-relation mis-rooting** — P4 (root = 4th of DCML) **1059 runs / 337 620 dur**, P5 (root = 5th)
**706 runs / 262 980 dur** — together **43 %** of new errors. By label: major/other 1815, minor 1563,
**sus 605**, halfdim 132, dim 15.

**20 largest new-broken (dur):** dominated by `Xsus` on the dominant — `bwv87.7@9600 Asus(9)→dcml D`,
`bwv227.1@9600 Bsus(11)→dcml E`, `bwv410@24960 Dsus(2)→dcml G`, `bwv301@7680 Asus`, `bwv64.8@9600
Bsus`, `bwv323@7680 Esus`, … **20 largest fixed (dur):** legacy over-grab/slash misreads rebuilt
gets right-or-abstains — `bwv282@7680 Eaddb9/G#→D`, `bwv48.3@16800 Ebmadd9→Bb`, `bwv112.5@20640
E7/G#→G`, `bwv226.2@11520 F/G→D`, …

### 2.4 New-error mechanism census (Task 3.5) — a DIFFERENT dominant mechanism (first-order finding)

§5 predicted the new-error mechanism would be "a short passing tone completing a stronger template"
(the bwv416-slice-2 type). **That is NOT the dominant mechanism.** The dominant new-error class is
**suspension / fifth mis-rooting**: the per-slice decoder commits an `Xsus` chord rooted on the 5th of
the true chord (X = dominant of the DCML root), reading the true triad's root as a suspended 4th over
its own 5th. Three score-verified examples (rebuilt sounding pcs vs the true triad):

- `bwv87.7@9600` slice pcs **{D,F,A} = D minor** → committed **Asus** (root A = 5th of D). DCML root D.
- `bwv227.1@9600` slice pcs **{E,G,B} = E minor** → committed **Bsus** (root B = 5th of E). DCML root E.
- `bwv410@24960` slice pcs **{D,G,B} = G major** → committed **Dsus** (root D = 5th of G). DCML root G.

In each, the very next short slice commits the TRUE root correctly (`Dm`/`Em`/`D`), so this is a
long-slice suspension-template mis-rooting, not a passing tone. sus = 15 % of new-broken runs (17 % of
new-broken dur); the P4/P5 fifth-relation family is 43 %.

### 2.5 The five §5 cases (Task 3.3) — prediction vs measured at the rebuilt arm

| case | class | §5 prediction | rebuilt actual root | verdict |
|---|---|---|---|---|
| `bwv10.7@36000` | **b** | WIN root G (7) | **C (0)** — L4 Abstain, `resolveAbstained` picked Cm from carry `[0:Min, 7:Maj…]` (G was carried, not selected) | **MISS** |
| `bwv352@1440` | **a** | WIN root F♯ (6) | E (4) — L4 Abstain; top alt was `6:HalfDim` but E selected | **MISS (but class-(a)** — ø7/m6 share-tone {C,E,F♯,A}, doesn't touch the class-(b) verdict) |
| `bwv272@4320` | **a** | WIN root G♯ (8) via spelling-pin | G (7) — L4 Abstain; carry `[7:Maj,4:Maj,2:Hd,2:Maj]` has NO G♯ reading | **MISS (but class-(a)** — symmetric dim7 {D,F,A♭,B}; the spelling-pin did NOT fire) |
| `bwv174.5@6240` | **b** | NO CHANGE (stay wrong E/G♯, root 4) | **ABSTAIN (−1)** — coverage-loss, no class-(b) error | **PARTIAL** — better than predicted: avoids the wrong commit by abstaining, not by a correct commit |
| `bwv416@10080` (slice 1) | **a** | HALF-WIN G♯ (8) via pin | **ABSTAIN (−1)** — dim7 {D,F,A♭,B}, pin did NOT fire | **MISS** (abstains, not G♯) |
| `bwv416@10320` (slice 2) | **b** | uncertain (maybe E7) | A (9) — L4 Abstain, committed A; DCML G♯ (8) | **MISS** (commits A, wrong) |

**Four of five per-case WIN/HALF-WIN predictions MISS.** Two of the misses are class-(a) (the rotation
is a coin-flip; irrelevant to the class-(b) verdict); the class-(b) cases (`bwv10.7`, `bwv416`-slice-2)
stay wrong. Critically, the predicted DECODER mechanisms (spelling-pin → G♯; `bassNoteRootBonus` →
F♯) did **not** fire — those slices were **L4 Abstains** whose final root was chosen by
`resolveAbstained` (progression-first, confidence 1.0 — the un-disabled Tier-1 T1-1 arm), which
selected a wrong carried alternative (`bwv10.7`: Cm over the carried G).

### 2.6 G4 confirm (Task 3.4) — dim7 rotation distribution on the rebuilt arm

Rebuilt Baroque carries **324** dim7 (T3-invariant, 4-note) sonorities. **L4 abstains on 278 (86 %)**;
of the 214 that end committed (incl. resolver-resolved), only **4** carry a Diminished-quality (pinned
dim7) reading — **210 are Major/Minor triad rotations** of the dim7 subset (Major 121, Minor 49,
HalfDim 29, Sus 10, Aug 1). **The "spelling-pin selects the correct dim7 root" mechanism the desk sim
relied on does NOT fire.** BUT because every dim7 is class-(a) by construction, this rotation churn
never enters the class-(b) count — so the §5 **disposition** ("the extensions gap has no class-(b)
root path; no pre-probe carry-fix needed for ROOT") **HOLDS**, though via a different route
(abstain/rotate, not the pin). Corollary: rebuilt's class-(a) duration RISES (Baroque 152 880 vs
legacy 106 560, **+46 320**, above the advisory `CLASS_A_INVESTIGATE_TICKS = 9600` flag) — the dim7
rotation churn, advisory only, not a stop.

### 2.7 RN + key tracked beside (Task 3.6, SECONDARY — G4 makes rebuilt RN LOW by declaration)

Duration-weighted over COMMITTED cells (the E0 §2.1 convention), coverage-equal intersection:

| Preset | rebuilt root / RN / key | legacy root / RN / key |
|---|---|---|
| Baroque | 60.7 % / 37.9 % / 80.3 % | 62.3 % / 43.9 % / 68.1 % |
| Default | 60.7 % / 37.9 % / 81.0 % | 62.2 % / 43.7 % / 67.5 % |
| Jazz *(consistency)* | 60.6 % / 37.5 % / 79.6 % | 61.3 % / 41.8 % / 64.4 % |

- **root (committed):** rebuilt ~1.6 pp LOWER than legacy — consistent with §2.2 (rebuilt is
  marginally worse per committed cell).
- **RN:** rebuilt ~6 pp LOWER — the declared L4→L5 seventh/extension carry drop (triad-level base RN;
  E0 §4-A), expected and LOW by declaration (not a surprise).
- **key:** rebuilt HIGHER (committed-only, using the per-slice local-key field). **Flagged secondary
  and NOT a correctness claim:** it is measured over committed cells only and on a different key
  substrate than the E0 all-slice `key_disagree` finding (which found chain key WORSE); the two are
  not comparable. Reported as-measured, not interpreted.

---

## 3. §5 PREDICTION vs MEASURED — the verdict line per prediction (Task 4)

The G1 asymmetry is applied as declared: a rebuilt win under the single-home-key handicap is
decision-grade; a loss/dissolution is diagnosed, not concluded.

| §5 prediction | measured | verdict |
|---|---|---|
| **Aggregate: class-(b) dur decreases 15–40 % on Baroque/Default** | −15.99 % / −16.27 % (coverage-equal) | **DIRECTION HIT, MECHANISM MISS** — the duration lands in-band, but the decomposition shows it is an ABSTENTION artifact (per-committed rate +0.7 pp WORSE; commit-frac 82 %; abstention 47 % regression / 51 % good), NOT the predicted accuracy mechanisms (over-grab / spelling / bass-corrected share-tone). |
| Wins concentrate in over-grab, symmetric-spelling (dim7), bass-corrected share-tone | dim7 spelling-pin does NOT fire (G4); the dominant NEW-error class is fifth/sus mis-rooting | **MISS** — predicted win-mechanisms not observed; a new dominant loss-mechanism instead. |
| `bwv10.7@36000` WIN G | Cm (resolveAbstained picked wrong carried alt) | **MISS** |
| `bwv352@1440` WIN F♯ | E; case is class-(a) | **MISS** (class-(a), verdict-irrelevant) |
| `bwv272@4320` WIN G♯ | G; case is class-(a); pin did not fire | **MISS** (class-(a), verdict-irrelevant) |
| `bwv174.5@6240` NO CHANGE (stay wrong) | ABSTAIN (avoids the wrong commit) | **PARTIAL** (better than predicted, via abstention) |
| `bwv416@10080` HALF-WIN ≥240/480 via pin | slice-1 ABSTAIN, slice-2 commits A (wrong) | **MISS** |
| New errors: "short passing tone completes a stronger template" | fifth/sus mis-rooting (P4 1059 / P5 706 / sus 605) — a DIFFERENT dominant mechanism | **MISS** (first-order finding, §2.4) |
| G4: NO pre-probe carry-fix needed for ROOT (extensions gap has no class-(b) root path) | HOLDS (dim7 are class-(a); abstain/rotate) — but the underlying reason (spelling-pin) is REFUTED | **HIT (disposition) / mechanism refuted** |

---

## 4. What is handed up (#8) — findings only, NO build recommendation

1. **The instrument is established** (#19): override-OFF via the dormant θ, production byte-identical,
   reproduce-check byte-identical (excl. timing), coverage made byte-exactly equal (the P4(c)
   measure-anchor confound diagnosed and controlled by the intersection mode), grader reproduces the
   committed robust-stop reference exactly.

2. **On the literal robust-stop metric, the rebuilt arm (E0 chain, override-OFF) "wins": class-(b)
   root-disagree DURATION −16 % on both correctness presets, in the §5 band.**

3. **But the win does not survive decomposition (#15, verify at objects):** it is entirely an
   ABSTENTION artifact. Per committed cell the rebuilt arm is marginally WORSE (+0.7 pp class-(b)
   rate); it commits on only 82 % of duration; and its abstention is a near coin-flip (47 % drops
   roots legacy got right, 51 % avoids legacy's wrong commits) — not a precision-selective filter. So
   the **P1 assumption ("the rebuilt path is more root-correct than the legacy path") is NOT supported
   by this probe** — the metric moves for a reason §5 did not anticipate, and the predicted per-case
   and per-mechanism wins mostly MISS.

4. **Two first-order mechanism findings (explorational scope):** (a) the dominant NEW class-(b) error
   is **fifth/suspension mis-rooting** (`Xsus` on the dominant of the true root), not the predicted
   passing-tone type; (b) the decoder's dim7 **spelling-pin does not fire** (86 % abstain, the rest
   rotate to Major/Minor) — the §5 root disposition still HOLDS only because dim7 are class-(a).

5. **Interpretation caveat (unchanged from CLAUDE.md block D):** the robust-stop class-(b) duration
   metric was defined for a commit-everywhere path; on an abstaining path it is reducible by
   abstention alone. Any go/no-go read of the −16 % must be paired with the per-committed rate + the
   abstention decomposition above. **The decision is Cowork's / the user's.**

---

## 5. Artifacts

- Instrument feat (driver-only, revertible): `--fullspine-no-override` + `pitchClassSet` emit in
  `tools/batch_analyze.cpp` `runFullSpine`; `tools/run_bach_preset.py` pass-through.
- Probe measurement tool (read-only, reuses the pinned a8/compare_rn/compare_analyses primitives;
  abstain-aware; own/legacy/rebuilt/intersect anchoring; self-validates against the committed
  reference): `tools/cc_eg2_probe.py`.
- Scratch (not committed): dumps `C:/tmp/eg2/fs{1,2}/<preset>/` (manifest-stamped), probe outputs
  `C:/tmp/eg2/probe_*/` (per-preset summary JSON + fixed/new-broken/classb run enumerations +
  coverage-mismatch lists).
- Committed `tools/robust_stop/` and `tools/corpus/` UNTOUCHED (verified); no golden refresh; no
  constant tuned; no adoption.

*Report line count target met; measurements reproducible from the artifacts + corpus `c50002fee1`.*
