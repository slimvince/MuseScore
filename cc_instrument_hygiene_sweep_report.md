# The measurement-instrument hygiene sweep — OI-145 wave-1 close

**Session:** CC, 2026-07-13. **Dispatch:** `cc_instruction_instrument_hygiene_sweep.md` (Cowork, at the
user's direction). **Type:** hygiene / dedup / establishment on the `tools/` measurement instruments.
**No `src/composing` or `src/notation` file was touched. No re-baseline. No graded figure moved.**

---

## 1. The headline

**Every governing metric is byte-identical, before and after.** The establishment battery
(`tools/audit/hardening_battery.py`) reproduces exactly, run before the first edit and after the last:

| gate | before | after |
|---|---|---|
| `register` | 157 row IDs, no collision | 159 row IDs, no collision (two new discoveries) |
| `a8_diff` | `+0 / -0` all three presets, class-(b) Δ+0, coverage OK | **identical** |
| `calib` | 4/4 maps sha256-identical | **identical** |
| `validate` | 3/3 corpus manifests OK | **identical** |
| Python suites | green | green (119 → **127** tests; 8 added, 0 removed) |

Root 66.04 / 64.98 / 65.93, RN 46.33 / 44.10 / 46.23, key-home 71.42 / 67.83 / 70.65, key-local
65.99 / 62.98 / 65.71 — all unmoved. **No re-baseline, no snapshot owed.**

**Three findings are declared, none of which this sweep was authorized to fix.** Two are new register
rows (OI-158, OI-159); one is the narrowed remainder of OI-125. They are in §5.

---

## 2. Per-row disposition

| row | disposition |
|---|---|
| **OI-157** — the third mode-classification copy | ✅ **CLOSED.** Table deleted; the probe grades through the ONE shared reduction. Self-check **0 mismatches / 6409 / 6311 / 6413 regions**. |
| **OI-151** — the adjudication probe's destructive default | ✅ **CLOSED.** `--out` defaults to scratch; verified a default run leaves the committed evidence untouched. |
| **OI-132(b)** — the two cross-language value copies | ✅ **CLOSED** (and with it OI-132 entirely). Both copies mechanically pinned by a producer-parsing test. |
| **OI-127(a)/(b)/(e)** | ✅ **CLOSED**, each proven byte-identical by measurement *before* the edit. (c)/(d) remain. |
| **OI-125** — the comparator tolerances | 🔶 **2 of 3 ESTABLISHED as derived.** Narrowed to the extrapolation constant — see §5.3. |
| **OI-133(c)** — the 13 "grading tolerances" | 🔶 **Split three ways.** Most are not tolerances at all; two are genuinely load-bearing and left **owed**; one is dead code (→ OI-158). |
| **OI-158** *(new)* | ★ **DISCOVERY** — the music21 corroborator's local-key path has never run. |
| **OI-159** *(new)* | ★ **DISCOVERY** — the OI-142 correction silently staled the committed OI-43 probe evidence. |

Out of scope and untouched, as directed: OI-131, OI-152, OI-156, the OI-34 corpus line-ending amendment.

---

## 3. What was folded (Tier 1)

### OI-157 — the third mode copy, folded into the ONE reduction

`measure_joint_probe._MAJOR_MODE_IDX` classified a carried key from its `KeySigMode` **enum index**.
The dispatch suggested reading the region's key string instead — but that is not sufficient: **the
carried alternatives carry no key string**, only `(tonicPc, KeySigMode int)`. An integer therefore has
to be resolved to a mode *name* before it can be graded at all.

So the integer is resolved to the **producer's own emitted suffix**, the key string the producer itself
would print is composed from it, and *that* is graded by `crn._our_key_ident`. The suffix comes from
**`tools/producer_key_modes.py` (new)** — the ONE reader of the producer's `KeySigMode` vocabulary,
which parses `keyModeSuffix()`, the `KeySigMode` declaration order, and `keyModeIsMajor()`. The two
copies of those parsers that `test_metric_primitives_l0l1.py` held are folded onto it (#6).

The stale table and the shared reduction disagree on **11 of the 21 producer modes** — the five exotics
whose tonic *moves* under the OI-132 parent-collection ruling (an index→bool table cannot express a
tonic move at all), and six whose accidental/digit suffix the shared reduction abstains on (OI-152):

| | old table (tonic C) | shared reduction (tonic C) |
|---|---|---|
| `PhrygDom` | C minor | **F minor** (parent collection) |
| `Lyd♭7` / `Mix♭6` / `Lyd+` / `alt` | C major / C major / C major / C minor | **G / F / A / C♯ minor** |
| `Dor♭2`, `Loc#2`, `Loc#6`, `Ion+`, `Dor#4`, `Lyd#2` | a confident major/minor | **abstain** (OI-152 regex) |

**Establishment (full corpus, all three presets):** the probe's own faithfulness self-check — renamed
`key_ident_selfcheck`, because the old name described a table that no longer exists — reports **0
mismatches on 6409 / 6311 / 6413 committed regions**. The identity composed from `(tonicPc, mode int)`
equals the identity of the key string `batch_analyze` actually emitted, on every region.

The consumer `classify_key_disagreement.py` imports `_key_ident`, so it is fixed by the same fold.

**Inherited, and recorded (not a defect of the fold):** the probe now abstains on the six
accidental/digit-suffix modes, because the ONE reduction does. When OI-152 fixes that regex, the probe
is fixed with it — which is the point of having one path.

### OI-151 — and the same defect at a second instrument

`mode_grading_adjudication_probe.py` defaulted `--out` to `tools/reports/mode_grading_adjudication_probe.json`,
which is **committed evidence the user's OI-132 ruling rests on**. Now defaults to scratch. Verified:
a bare default run prints `ESTABLISHMENT PASS`, writes to scratch, and leaves `git status
tools/reports/` clean.

**The sweep found the same defect at a second instrument:** `measure_joint_probe.py` defaulted to
`tools/reports/joint_probe_measure.json` — also committed. Also fixed (in the OI-157 commit).

### OI-132(b) — the value copies, now red-on-drift

Neither copy can be single-sourced from Python, so both are **mechanically pinned** instead —
`tools/tests/test_cross_language_constants.py` parses the producing C++ declaration and asserts the
Python copy equals it:

- `analyze_inversion_errors.INVERSION_SUSPICION_MARGIN` (0.70) ↔ the `inversionSuspicionMargin` default
  in `analysistypes.h`. (Hoisted from inside `main()` to module scope so the guard can see it — same
  value, same single use.)
- `music21_batch.TICKS_PER_QUARTER` (480) ↔ `Constants::DIVISION` in `src/engraving/types/constants.h`.

### OI-127 — two false-agreement edges, measured before being closed

Both were **measured byte-identical before the edit**, not asserted:

- **(b) the `-1` root sentinel.** `_load_region` defaults a missing root to `-1`, not to the `None` the
  OI-52 abstain convention is written in — so two rootless regions compared *equal* and scored a chord
  **agreement**. That is a false agreement that *flatters* the metric. Measured over 33,296 aligned
  pairs (352 stems × 3 presets — the same denominator `roots_agree` cites): an unresolved root occurs
  on **neither side, 0 times**. `_roots_match` now refuses it structurally rather than relying on it
  never happening (#19).
- **(a) `_QUALITY_NORMALISE` completeness.** Established by measuring *both* producers' vocabularies:
  ours emits exactly the 8 strings `qualityToString()` can return (all mapped); music21 emits 5, of
  which `Unknown` (5,856 regions) is the no-quality marker. A pin test now parses `qualityToString()`
  so a new `ChordQuality` cannot land and pass through unnormalised; and two `Unknown`s no longer
  score as a quality match (two abstains are not an agreement).
- **(e) the `gen_inventory` false positive — closed at the class.** The hand-listed `_PY_STDLIB_MODS`
  mis-resolved every stdlib module it forgot (`import platform` → a nonexistent `tools/platform.py`,
  tagged an instrument dependency). The stdlib set is now asked of the interpreter
  (`sys.stdlib_module_names`), and an edge is only claimed when the resolved file **actually exists**.
  Verified by regenerating the L5 inventory to scratch: the phantom row is gone and **no legitimate
  edge is dropped**. The committed audit CSVs are frozen pass-1 evidence and were **not** regenerated.

---

## 4. Tolerance establishment (Tier 2)

**Established as *derived*** — these are not fitted numbers, they are the definitions of the words they
implement, and no other value is coherent:

- **`ALIGN_OVERLAP_FRACTION` = 0.5.** Two spans name the same harmonic event iff one of them spends the
  **majority** of its life inside the other; 0.5 is the majority boundary — the only value for which
  "majority" means majority. Two properties fall out, and both are wanted: when our region is covered by
  exactly two ground-truth regions the ≥0.5-of-ours leg **always** succeeds by pigeonhole (two parts of
  a whole cannot both be under half), so the pair never silently drops; and the OR (either duration, not
  both) is what keeps a segmentation **over-grab** aligned and therefore *graded as an error* — requiring
  both halves would let over-grabbed regions vanish from the denominator, i.e. flatter the score.
- **`ALIGN_BEAT_DISTANCE_TOL` = 0.5.** Half the spacing of a 1.0-beat grid — the nearest-neighbour
  (Voronoi) radius. The unique tolerance for which every on-grid beat matches its *nearest* beat and
  nothing else: larger admits a non-nearest beat, smaller leaves a dead band.

**Established as *not tolerances at all*** — the audit's classification was too broad. The ±0.26 beat
window, the `noteCount>=3` grouping and the margin cut-points in `analyze_inversion_errors` are
**histogram bucket edges and report labels in a printed diagnostic**. They classify nothing; no figure
is graded through them; they owe no derivation.

**Left owed, with the concrete experiment named** — `calibration_fit`'s two genuinely load-bearing
gates. Rather than justify them after the fact, they are now named constants carrying an explicit
`[hand-set; NOT established]` note and the experiment each would take:

| constant | what it decides | the experiment that would establish it |
|---|---|---|
| min-cell 50 / 20 | whether a calibration row is fitted **at all** | sweep the counts; the floor is where the fitted curve stops moving under resampling |
| `NEAR_LOGISTIC_TOL` 0.05 | whether a row ships a **Platt** curve or an **isotonic** one | show held-out ECE is insensitive to the tie-break across the band where the two curves agree |

Neither is a desk exercise, so neither was forced (#19: an instrument constant is trusted only once
*positively* established, never because it has not misbehaved).

---

## 5. The three findings

### 5.1 ★ OI-158 — the music21 corroborator's local-key path has never run

Establishing the OI-133(c) "FloatingKey ±4 tolerance" showed **it is not a tolerance.** It is
unreachable configuration on an object that is never constructed:

`music21_batch` calls `m21_floatingKey.FloatingKey()`, but `music21.analysis.floatingKey` **exports no
such name** (v9.9.1 — the class is `KeyAnalyzer`). The constructor raises `AttributeError`, a bare
`except Exception` swallows it, `fk_analyzer` stays `None`, and `local_key` silently falls back to the
**global** key for every region — which then feeds `romanNumeral` and the emitted `key` field.

**Proven at the artifact, not inferred: all 28,914 regions of the committed Baroque corroborator have
`key == keyGlobal`**, on every stem. The intended local sliding window has never once run, and the
`.music21.json` Roman numerals were computed against the global key throughout.

This is a Class-B (#19) instrument-establishment failure — the instrument does not do what it says —
plus a silent-degradation defect (a bare `except` masking an API mismatch) and a doc-sync break (the
docstring advertised a `keyLocal` field that is never written; corrected).

**No governing figure is affected.** The ratified robust unit is DCML-only and never reads music21; the
BIR gate reads music21's *root and quality*, not its key or RN. The blast radius is the
`full_agree` / `chord_agree_rn_differs` / `chord_agree_key_differs` sub-split in
`compare_analyses.classify`.

**NOT FIXED — deliberately.** Constructing `KeyAnalyzer` would give the corroborator genuinely local
keys and RNs, changing the committed `.music21.json`: a ground-truth-corroborator re-baseline under the
user's ratification, not a hygiene edit. **The user rules** — activate it (regen ×3 presets, O-12
snapshot, explained diff on the sub-split), or declare the global-key reading intended and delete the
dead block. The current state — a dead path the docs describe as live — should not stand either way.

### 5.2 ★ OI-159 — the OI-142 correction silently staled the committed OI-43 probe evidence

`tools/reports/mode_key_chord_probe.json` is stamped `git 243cfd2165`, which **pre-dates** the OI-142
transposition correction to `dcml_parser.load_wir_regions`. Nothing re-ran the probe, and the OI-142 row
enumerated the graded surfaces it re-based but not this read-only consumer.

The probe's figures moved for two independent reasons, so I **attributed them** by re-running the
*pre-fold* code at HEAD (isolating OI-142) as well as the folded code:

| preset | quantity | committed | HEAD, pre-fold | HEAD, folded | Δ from **OI-142** | Δ from **OI-157** |
|---|---|---|---|---|---|---|
| Baroque | key-disagree regions | 1982 | 1786 | 1775 | **−196** | −11 |
| Jazz | key-disagree regions | 2143 | 1956 | 1936 | **−187** | −20 |
| Default | key-disagree regions | 2019 | 1828 | 1820 | **−191** | −8 |
| Baroque | menu-containment | 1322 | 1346 | 1342 | **+24** | −4 |
| Jazz | menu-containment | 1320 | 1339 | 1329 | **+19** | −10 |
| Default | menu-containment | 1295 | 1320 | 1320 | **+25** | +0 |
| all three | **chord-flip-under-GT** | 7 / 8 / 6 | 7 / 8 / 6 | **7 / 8 / 6** | **+0** | **+0** |

The bulk is OI-142; the fold is a small remainder confined to the exotic/abstain modes, exactly as
designed.

**The OI-43/OI-44 conclusion is unchanged under the corrected instrument — measured, not assumed.**
`chord-flip-under-GT` (the number the shelve ruling turns on) is **byte-identical**: the coupling is
still inert. Menu-containment rises from 62–67 % to 68.7–75.6 % — still below the 80 % bar the
prediction set, so P3 is still **not met**. The shelve ruling stands; only the recorded *figures* are
stale, and the "menu-widening signal" is weaker than recorded.

The committed evidence was **not** overwritten — that is precisely the OI-151 discipline.

### 5.3 OI-125 narrowed — a load-bearing 4/4 assumption that happens to be right

`EXTRAPOLATION_BEATS_PER_MEASURE = 4` is **not** derivable, and the branch is **not** inert. Measured
over the committed corpus, it **fires 162 times across 15 stems** — overwhelmingly the pickup measure,
which DCML numbers 0 while our regions start at 1.

On **every one of those 15 stems, the measure length derived from the piece's own anchors is exactly
4.0 beats**, so the constant is correct wherever it currently fires: no committed figure rests on luck.
But it hard-codes 4/4 and is simply *wrong* for any other meter (a 3/4 pickup at beat 3 is placed a full
beat early), and the corpus that would break it is one we plan to add (OI-38/OI-39).

**The fix already sits three lines above the use:** the *interpolation* branch derives
`tick_per_measure` from the anchors instead of assuming it, and the same estimator serves extrapolation.
That change is **byte-identical on today's corpus** (measured: derived == 4.0 on every firing stem) —
but it edits the shared tick resolver `_dcml_tick_for`, which the a8 path also uses, so it is left to be
**ratified** rather than slipped into a hygiene sweep. OI-125 stays open on exactly that.

---

## 6. Premise Gate — predictions vs outcomes (#17b)

| prediction (written before measuring) | outcome |
|---|---|
| Battery byte-identical; the probes feed nothing graded | ✅ **MET** — a8_diff +0/−0 ×3, calib 4/4, validate 3/3, identical before/after |
| The folded probe's self-check reports **0 mismatches**, all presets | ✅ **MET exactly** — 0/6409, 0/6311, 0/6413 |
| A default adjudication-probe run leaves the committed evidence untouched | ✅ **MET** — `ESTABLISHMENT PASS`, scratch output, clean `git status` |
| The pin test and the OI-127 folds are byte-identical by construction | ✅ **MET** — and the OI-127 folds were *measured* (0 of 33,296 pairs affected) rather than assumed |
| Tolerance establishment is byte-identical unless it surfaces a wrong value → STOP | ⚠️ **Surfaced a dead one.** No value was wrong; one "tolerance" turned out to be unreachable code (OI-158). Not fixed — surfaced, per protocol. |

Nothing landed off-prediction. No graded figure moved anywhere in the sweep.

---

## 7. Where this leaves OI-145 wave 1

Wave 1 (the measurement chain) is **closed** apart from three explicitly-owed items, none of which
blocks: the two `calibration_fit` gates (OI-133(c)), the extrapolation derivation (OI-125), and the two
new discoveries (OI-158, OI-159) — all with concrete gates recorded.

**The next move is wave 2** — the `src/` substrate hygiene (OI-86, OI-13, OI-87, the file-table
reasons) toward lifting the key-layer readiness gate.

**Two items need the user's ruling before they can move:** OI-158 (activate `KeyAnalyzer` and re-baseline
the corroborator, or delete the dead block) and OI-125's extrapolation derivation (byte-identical, but it
edits a shared graded resolver).
