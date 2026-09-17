# The wave-1 finalizers — OI-158, OI-125, OI-159 (and one new discovery, OI-160)

**Session:** CC, 2026-07-13. **Dispatch:** `cc_instruction_oi158_oi125_oi159.md` (Cowork, on the
user's rulings of the instrument-hygiene sweep's three findings). **Type:** a measurement-instrument
fix pass on `tools/`. **No `src/composing` or `src/notation` file was touched. No re-baseline. No
graded figure moved anywhere.**

---

## 1. The headline

**All three predictions held, and every governing surface is byte-identical.** The establishment
battery (`tools/audit/hardening_battery.py`) passes identically before the first edit and after the
last:

| gate | before | after |
|---|---|---|
| `register` | 159 row IDs, no collision | **160** row IDs, no collision (the new OI-160) |
| `a8_diff` | `+0 / −0` all three presets, class-(b) Δ+0, coverage OK | **identical** |
| `calib` | 4/4 maps sha256-identical | **identical** |
| `validate` | 3/3 corpus manifests OK | **identical** |
| Python suites | 127 + 4, green | **134** + 4, green (7 added for OI-125, 0 removed) |

Beyond the gate's own checks, **all 159 leaf fields of the a8 summary were diffed against the
committed reference and none moved** — root 66.04 / 64.98 / 65.93, RN 46.33 / 44.10 / 46.23,
key-home 71.42 / 67.83 / 70.65, key-local 65.99 / 62.98 / 65.71, the class-(a)/(b) durations, and
coverage 326/326/326. **No re-baseline, no snapshot of the robust-stop reference owed.**

**With this, OI-145 wave 1 (the measurement chain) is closed.** One new discovery is declared, not
absorbed: **OI-160** (§5).

---

## 2. Per-row disposition

| row | disposition |
|---|---|
| **OI-158** — the corroborator's dead local-key path | 🔶 **DEAD-CODE HALF CLOSED** (the user's ruling: delete, do not activate `KeyAnalyzer`, do not foreclose). **Evidence half OPEN**, filed in the inventory. |
| **OI-125** — the 4/4 extrapolation assumption | 🔶 **EXTRAPOLATION HALF CLOSED** — the resolver derives each stem's measure length. Open only on the named `calibration_fit` remainder it shares with OI-133(c). |
| **OI-159** — the stale OI-43 probe evidence | ✅ **CLOSED.** Refreshed from a HEAD run; the shelve ruling **re-confirmed**, not reopened. |
| **OI-160** *(new)* | ★ **DISCOVERY** — the same staleness in the sibling arc-12 artifact. Filed, not fixed. |

Commits, one per row, each carrying its own register flip:
`e02bbebf88` (OI-158) → `6725329381` (OI-125) → `126918aaba` (OI-159 + the OI-160 row) → this
`docs(cc)` fold.

**Task 0 was a no-op, verified:** `git status --porcelain` showed no waiting Cowork register or
handoff edit — the register was already current at `e610cafa0a`. `cowork_joint_key_chord_design.md`
was left unstaged, as directed.

---

## 3. OI-158 — the dead FloatingKey block is gone, and the question it raises is not

**The fire-check first (control flow before arithmetic, #17c).** In the installed music21 **9.9.1**,
`music21.analysis.floatingKey` imports fine but exports **no name `FloatingKey`** — the class is
`KeyAnalyzer`. So the import guard set `_HAS_FLOATING_KEY = True`, the constructor raised
`AttributeError` on every single run, a bare `except` swallowed it, and `local_key` fell back to the
global key for every region ever produced. The `numFlats`/`numSharps` ±4 that the L5 audit
catalogued as a hand-set *tolerance* were unreachable configuration on an object that is never
constructed.

**What was removed:** the `_HAS_FLOATING_KEY` import/flag, the `fk_analyzer` construction block, and
the `local_key` branch. The corroborator now reads plainly at the global key and the docstring says
so, instead of advertising a `keyLocal` field that was never written.

**★ The proof, at the artifact, not by assertion.** The corroborator was regenerated in full — 352
chorales — into a scratch dir and sha256-compared against every committed copy:

| committed set | files | sha256-identical | differ | missing |
|---|---|---|---|---|
| `tools/corpus/` (flat) | 352 | **352** | 0 | 0 |
| `tools/corpus/baroque/` | 352 | **352** | 0 | 0 |
| `tools/corpus/jazz/` | 352 | **352** | 0 | 0 |
| `tools/corpus/default/` | 352 | **352** | 0 | 0 |

**1408 of 1408 byte-identical.** That is the proof the removed code never once affected output — the
analog of the harness `.ours.json` regen proof, and the condition the dispatch set for the removal.

**What was NOT done, deliberately.** `KeyAnalyzer` was **not** activated. Doing so would give the
corroborator genuinely local keys and Roman numerals, changing every committed `.music21.json` — a
ground-truth-corroborator **re-baseline** under the user's ratification (#16), and it would put an
unvalidated heuristic under load (#19). Neither is a hygiene edit.

**The evidence question is filed, not decided** (#12 — a possible evidence source is not discarded
by deleting dead code). `cowork_evidence_inventory.md` **§8c** now carries it: *should the key layer
consume a music21 `KeyAnalyzer` **local** key as an unvalidated, non-ground-truth second opinion?*
Gate: the key-layer design conversation. If ever adopted it enters as an explicitly-unvalidated
field and stays out from under load until positively established (#19); music21 is **not** ground
truth (DCML/When-in-Rome is — it only corroborates).

**One thing left deliberately verbatim.** The two frozen L5 disposition rows for the ±4
(`tools/audit/l5/gen_grading_fitting_dispositions.py`) are **stamped audit evidence** whose
artifacts must keep reproducing, so their note strings are unchanged — but they now carry a comment
recording that OI-158 **refuted** the causal claim in that note ("shapes keyLocal, which feeds
`oracle_root_metric`'s KEY tiers" — it shaped nothing). The live record is the register row, not the
frozen table.

---

## 4. OI-125 — the ground-truth tick resolver stops assuming 4/4

`compare_analyses._dcml_tick_for` resolves a DCML `(measure, beat)` onset to a tick. When the onset
lies **beyond the outermost measure our regions anchor** — overwhelmingly the pickup measure, which
DCML numbers 0 while our regions start at 1 — it extrapolated with a hard-coded 4 beats per measure.
That is simply wrong for any other meter (a 3/4 pickup at beat 3 lands a full beat early), and this
is a **shared** resolver: the a8 governing path reads it.

**It now uses the measure length derived from each stem's own anchors** — the new
`_derive_ticks_per_measure`: the median tick distance per measure across consecutive anchored
measures, which is robust to the two anchors that are legitimately short (a pickup, and a final
measure our segmentation truncates). This is the same quantity the *interpolation* branch three
lines above already derives from the two anchors it sits between; extrapolation now uses it too.

**★ The prediction, written before the measurement (#17b), and what was measured.** A read-only
probe instrumented the resolver over all three presets **before the edit**:

| quantity | predicted | measured |
|---|---|---|
| extrapolation firings | 162 | **162** |
| distinct stems that fire | 15 | **15** |
| derived measure length on firing stems | 4.0 beats everywhere | **4.0 beats, every firing** |
| resolved ticks that change | 0 | **0 of 162** |
| stems too thinly anchored to derive (< 2 anchors) | — | **0 of 352, every preset** |

So the fix is **byte-identical by construction on today's corpus**, and the battery confirmed it
afterwards (a8_diff +0/−0, class-(b) Δ+0, calib 4/4, validate 3/3, all 159 a8 summary leaves
unmoved). It was confirmed a **second, independent way**: the OI-159 joint probe — which grades
through this same resolver — was run before and after the change, and the two runs are identical in
all **177** measurement fields (only `git_hash` differs).

**`EXTRAPOLATION_BEATS_PER_MEASURE` survives, but only as a last resort** for a stem too thinly
anchored to derive any measure length (fewer than two anchored measures — i.e. every analyzer region
of the piece inside a single measure). Measured: **0 of 352 stems on any preset**, so it never fires
today. It is kept rather than returning "unresolvable", so such a stem would still resolve its onset
instead of silently dropping the ground-truth row from the denominator (#12 — the silent-shrink
shape OI-123/OI-128 fought).

**The measurement is reproducible, not hand-transcribed (#17f, #16).** The probe is committed as
`tools/cc_oi125_extrapolation_probe.py` (read-only; it writes nothing) and reprints the table above
on demand:

```
python tools/cc_oi125_extrapolation_probe.py
```

**And the behavior is pinned by tests (#11).** Seven cases were added to
`tools/tests/test_metric_primitives_l0l1.py` (`TestDcmlTickExtrapolation`): the derivation itself;
its robustness to a short pickup and a truncated final measure; the `None` it returns when fewer
than two measures are anchored; **a 3/4 stem's pickup, which the superseded constant placed a full
beat early and the derived rule places correctly** (this is the meter-correctness claim, tested —
not merely asserted); the 4/4 agreement with the old constant (the corpus byte-identity, in unit
form); and that the interpolation branch is untouched.

**What stays open on OI-125:** exactly the remainder the hygiene sweep named, shared with
OI-133(c) — `calibration_fit`'s two genuinely load-bearing gates, still hand-set and **not**
established (#19): the **min-cell 50/20** fit-at-all floor, and the **`NEAR_LOGISTIC_TOL` 0.05**
Platt-vs-isotonic tie-break. Each carries the concrete experiment that would establish it; neither
is a desk exercise, and both belong to the calibration / Stage-5 work, not here.

---

## 5. OI-159 — the OI-43 evidence refreshed, the ruling re-confirmed, and a sibling found stale

**O-12 first.** The outgoing artifact was snapshotted **before** the refreshing run was written:
`tools/reports/snapshot_2026-07-13_pre_oi159/` (the artifact + a `SNAPSHOT_NOTE.md` recording what
it preserves and why it was superseded). `tools/reports/mode_key_chord_probe.json` then took a run at
HEAD (stamped `6725329381`; corpus `c50002fee1`, unchanged).

**The refresh, measured** (Baroque / Jazz / Default):

| figure | committed (`243cfd2165`) | refreshed (HEAD) | reading |
|---|---|---|---|
| key-disagree regions | 1982 / 2143 / 2019 | **1775 / 1936 / 1820** | **−207 / −207 / −199** |
| menu-containment (P3) | 66.7 / 61.6 / 64.1 % | **75.6 / 68.7 / 72.5 %** | **still under the 80 % bar → P3 STILL NOT MET** |
| chord-flip-under-GT (P1's mechanism) | 7 / 8 / 6 | **7 / 8 / 6** | **BYTE-IDENTICAL** (coupled 3/4/2; durations 9600/11760/8160 unchanged) |

**Attribution of the drift** (from the hygiene sweep's A/B, reproduced by this run's totals): the
**OI-142 ground-truth correction** accounts for **−196 / −187 / −191** key-disagree regions and the
**OI-157 mode-grading fold** for **−11 / −20 / −8** — summing to the −207 / −207 / −199 measured
here.

**★ The ruling is re-confirmed, not reopened.** The OI-43/OI-44 shelve rests on the coupling being
inert (chord-flip-under-GT) and on menu-containment failing its 80 % bar. The first is
**byte-identical**; the second is **higher but still short of the bar**. Only the recorded figures
were stale — and the "menu-widening signal" the re-scope option (OI-44) names is **weaker** than
recorded: the menu misses the ground-truth key in ~¼ of key-disagree regions, not ~⅓.
`cc_mode_key_chord_probe_report.md` now carries the refreshed figures with the superseded ones kept
beside them (#12) and the drift attributed.

### ★ OI-160 — the discovery, declared not absorbed

The refresh run surfaced that **the same OI-142 cause also staled the SIBLING artifact**,
`tools/reports/joint_probe_measure.json` — the **arc-12 chord-axis go/no-go**, stamped
`fa0a881aa4`, backing a *different* ruling (`cc_engage_stage3_joint_measure_report.md`). OI-159
named only the key-axis evidence; nothing named this one.

Measured at HEAD: the **fire-rate is byte-identical** (99 / 95 / 89 flip regions — *which* chords
flip is a property of our analyzer, not of the ground truth), but **whether a flip corrects or harms
is graded against the ground truth**, so the split re-sorts:

| preset | corr / harm — committed | corr / harm — HEAD | net (corr − harm) |
|---|---|---|---|
| Baroque | 37 / 28 | **38 / 29** | +9 → **+9** |
| Jazz | 36 / 33 | **39 / 33** | +3 → **+6** |
| Default | 35 / 25 | **36 / 26** | +10 → **+10** |

**Not fixed here, on purpose.** The arc-12 conclusion is not visibly threatened — a net of +6 to +10
regions out of ~6200 scored per preset is still the "nearly a coin-flip, ~+0.1 pp" reading the no-go
rests on — but that is a **ruling**, and this dispatch was not authorized to rewrite a ratified
decision record. Filed as **OI-160**, together with the **#6 duplication** behind it: *two* committed
artifacts are produced by *one* instrument (`measure_joint_probe.py`), the older a strict subset of
the newer's blocks — so `joint_probe_measure.json` may simply be **superseded** rather than
refreshed. Both halves belong to whoever next touches the arc-12 record.

---

## 6. Premise Gate — predictions vs outcomes (#17b)

Predictions were written to `predictions.md` before any measurement was run.

| prediction (written before measuring) | outcome |
|---|---|
| Every governing surface byte-identical (a8_diff +0/−0, calib 4/4, validate 3/3, key columns unmoved) | ✅ **MET** — and verified at all 159 a8 summary leaves, not just the gate's own checks |
| **Fire-check:** `floatingKey` imports, `FloatingKey` raises `AttributeError` on music21 9.9.1 | ✅ **MET exactly** — the module exports `KeyAnalyzer`, not `FloatingKey` |
| The `.music21.json` regen is sha256-identical to the committed set | ✅ **MET** — 1408 / 1408 files, 0 differ |
| OI-125: 162 firings on 15 stems; derived == 4 × tpb on all; battery byte-identical | ✅ **MET to the digit** — 162 / 15 / 4.0 / 0 tick changes |
| OI-159: evidence-only, battery byte-identical; chord-flip-under-GT 7/8/6; menu 68.7–75.6 % | ✅ **MET exactly** — all three reproduced |

**Nothing landed off-prediction. No graded figure moved anywhere.** The one thing the session
surfaced that no prediction covered is OI-160 — declared, not absorbed (§5).

---

## 7. Where this leaves OI-145

**Wave 1 — the measurement chain — is CLOSED.** Every graded surface is established and
byte-identical; the key columns are intact; the register carries no open wave-1 row except the two
named `calibration_fit` tolerance establishments (OI-125 / OI-133(c)), which are scheduled at the
calibration / Stage-5 work and gate nothing here.

**Next: wave 2 — the `src/` substrate** (OI-86, OI-13, OI-87, the file-table reasons), toward
lifting the key-layer readiness gate.

*CC, 2026-07-13. `tools/`-only. No `src/` file touched, no constant tuned, no gate threshold moved,
no golden refreshed, no corpus regenerated into the committed tree. Fork-only; nothing pushed.*
