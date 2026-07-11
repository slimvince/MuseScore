# CC — Layer-3 (key/mode) audit PASS-2: fine-label re-derivation from the FROZEN blind prose — EG-7 / OI-84 / OI-100

> **Read-only measurement.** No `src/` read for labeling, no production change, no constant tuned, no
> golden refreshed; `tools/robust_stop/` and `tools/corpus/` untouched. This session answers ONE
> checkable-but-unchecked claim the L3 pass-2 second reading made in its own defense: that its
> deliberately-coarse four-label vocabulary (ESTABLISHED / SURVIVES / PUBLISHED / DEAD) lost nothing
> because "the per-row prose carries the finer distinctions" (`cc_l3_audit_pass2_report.md` §1–§2). The
> user directed that claim be CHECKED before the L3 certification is decided (OI-100). Method: re-derive
> the protocol-P2 fine verdict for every frozen blind row from the ROW IDENTITY + COARSE LABEL + PROSE
> ALONE — blind to pass 1 until frozen — then crosstab against pass 1 and measure how far the prose
> carries. Instruction: `cc_instruction_l3_audit_pass2_relabel.md`.

## 0. Blinding log — when each withheld file was first opened

The instruction WITHHELD every pass-1 artifact + every conclusion-bearing doc until the Task-2 freeze
existed, so the re-derivation could not be anchored by pass 1's labels or the pass-2 crosstab. The
freeze held.

**Freeze commit (the boundary): `30194061d1`.** Every withheld file below was first opened AFTER it, in
Task 3.

| Withheld file | First opened |
|---|---|
| `OPEN_ITEMS.md` (the deferred mandatory session-start read) | Task 3 (after the `30194061d1` freeze) |
| `cc_l3_audit_pass2_report.md` | Task 3 |
| `tools/audit/l3/pass1_dispositions.json` | Task 3 |
| `tools/audit/l3/pass2_compare_reading.csv` / `pass2_compare_errorrate.csv` (carry pass-1 verdicts) | Task 3 |
| `STATUS.md` (head, for the Task-4 prepend) | Task 3 |
| `cowork_handoff.md` (entry block, to append) | Task 3 |
| `DEFECT_TYPES.md` | **not opened** — no new problem type is introduced by the re-derivation (every finding maps to an existing DT), so it was not needed |
| `tools/audit/l3/pass1_dispositions.csv`, `sweep_results.json/.txt`, `firerate.json`, every other `cc_*_report.md` | **not opened** — not needed for the crosstab |

**Safe reads used BEFORE the freeze (Task 0/1):** `CLAUDE.md`, `cowork_audit_protocol.md` (its step P2
defines the fine vocabulary emitted here), the instruction, and the two frozen artifacts
`tools/audit/l3/pass2_blind_reading.{csv,json}` + `pass2_blind_errorrate.{csv,json}`. The frozen
artifacts' `context` field (the captured code line) was used only in Task 3 for diagnosis, never in
Task-1 labeling — the labels are derived from the prose, not from a re-reading of the code the reader
captured.

## 1. Method (Task 1) — what "re-derive from the prose alone" meant

For every one of the 156 frozen blind rows (116-row reading + 40-row error sample) the protocol-P2 fine
verdict was derived from the row's kind/file/line/identifier + its coarse label + its prose reasoning,
and NOTHING else. Axis is mechanical from the row kind: `branch`/`function`/`crosslayer` → the **code**
axis (SURVIVES/RETIRES); `literal` → the **constants** axis (ESTABLISHED/UNFIT/DEAD); `field` →
**constants** when the coarse label is ESTABLISHED/DEAD (the field holds a numeric parameter),
**derived-facts** when it is PUBLISHED (PUBLISHED/SILOED/TRAPPED/DUPLICATED). A row whose prose does not
decide its fine label is **UNRESOLVABLE-FROM-PROSE** with one sentence why — that outcome IS the
measurement, not a failure.

**No premise rows.** The P2 premise axis (FACT/THEORY/ASSUMPTION) is not exercised: the machine
inventory enumerates functions, literals, fields, cross-layer calls, and branches — none is a
causal-premise ledger row — so 0 of 156 rows land on that axis. (Theory-bearing literals such as scale
intervals are classified as constants, ESTABLISHED, per the rubric.)

**The one deliberate judgment on the constants axis** — structural vs fitted:
- **Structural constants** (scale-interval/pc-arithmetic tables, mod-12 normalization, array sizes,
  capacity hints, zero-inits, div-guards, the sigmoid math constant, and the fitter-range/slider **range
  bounds** whose prose confirms the default lies inside) → **ESTABLISHED**: theory/mechanics/well-formedness
  IS the establishment criterion; there is no fit to have provenance.
- **Fitted magnitudes** (mode priors, weights, penalties, costs, multipliers, empirical scale-scores)
  whose prose argues only "empirical / in-bounds / theory-grounded ORDERING / live / documented" →
  **UNRESOLVABLE-FROM-PROSE**: "empirical" says the value is fitted, not that its fit is positively
  established (#19); ESTABLISHED-vs-UNFIT turns on fit provenance the prose does not engage.
- Fitted magnitudes whose prose explicitly flags the fit as **"provisional"** → **UNFIT** (live, not
  positively established — the only bucket left in {ESTABLISHED,UNFIT,DEAD} once provisional is stated).

The mapping of each row to a reason code IS the recorded judgment
(`tools/audit/l3/pass2_fine_relabel_judgments.json`); the reason code deterministically fixes the fine
verdict + a `prose_decided` flag + the axis. The generator `tools/audit/l3/relabel_fine.py` does only
parse / join / totality-check (every frozen row judged, no extras) / axis-consistency-check / count /
render — the generated CSV/JSON is never hand-edited (#17(f)).

## 2. Per-row artifact locations

| Artifact | What |
|---|---|
| `tools/audit/l3/pass2_fine_relabel_judgments.json` | the hand-authored per-row recorded judgment (reason codes + notes) |
| `tools/audit/l3/relabel_fine.py` | the generator (parse/join/count/render only) |
| `tools/audit/l3/pass2_fine_relabel_reading.{csv,json}` | 116 rows: fine verdict, prose_decided, justification, note, coarse reasoning |
| `tools/audit/l3/pass2_fine_relabel_errorrate.{csv,json}` | 40 rows, same columns |
| `tools/audit/l3/crosstab_fine_vs_pass1.py` | the Task-3 crosstab (three buckets), run after unblind |
| `tools/audit/l3/pass2_fine_relabel_crosstab_{reading,errorrate}.{csv,json}` | per-row bucket + manifest-coverage flag + counts |

## 3. The re-derivation result (fine verdict counts)

| Sample | SURVIVES | ESTABLISHED | PUBLISHED | UNFIT | DEAD | UNRESOLVABLE-FROM-PROSE |
|---|---|---|---|---|---|---|
| reading (116) | 40 | 45 | 14 | 2 | 1 | 14 |
| error (40) | 16 | 14 | 2 | 0 | 0 | 8 |

`prose_decided = yes` on 134/156, `no` (= UNRESOLVABLE) on 22/156. Every UNRESOLVABLE row is a fitted
constant on the constants axis; there is no UNRESOLVABLE on the code or derived-facts axis.

## 4. The crosstab against pass 1 (Task 3)

Joined by the seed-fixed `process_order` carried in the pass-2 comparison CSVs (the authoritative join
the pass-2 report used). Every row lands in exactly one bucket. Pass 1 used a SUPERSET vocabulary
(NO-ISSUE / FORWARD-OK / MIXED-DEFERRED / BACK-EDGE(-NOTE) / DEFERRED beyond the P2 set); on each P2
axis those collapse to one P2 verdict (code: all = live/SURVIVES; derived: NO-ISSUE = a fine consumed
field = PUBLISHED; constants: matched exactly).

| Sample | CONCORDANT | GENUINE-DISAGREEMENT | UNRESOLVABLE-FROM-PROSE |
|---|---|---|---|
| reading (116) | 86 | 16 | 14 |
| error (40) | 27 | 5 | 8 |
| **both (156)** | **113** | **21** | **22** |

**Per fine axis (both samples):**

| Axis | rows | CONCORDANT | GENUINE-DISAGREEMENT | UNRESOLVABLE |
|---|---|---|---|---|
| code (SURVIVES/RETIRES) | 56 | 56 | 0 | 0 |
| derived-facts (PUBLISHED/…) | 16 | 16 | 0 | 0 |
| constants (ESTABLISHED/UNFIT/DEAD) | 84 | 41 | 21 | 22 |

**The prose carries the fine label completely on the code and derived-facts axes** (56/56 and 16/16):
every branch/function/include the prose called live maps to a pass-1 live verdict (no RETIRES row was in
either sample); every field the prose called PUBLISHED names a consumer and pass 1 agrees
(PUBLISHED or NO-ISSUE). **All divergence is on the constants axis** — the axis the coarse vocabulary
most plausibly collapsed.

## 5. Every genuine disagreement, diagnosed

The 21 genuine disagreements are ONE real (already-tracked) defect + 20 constants-classification
differences. None is a new correctness defect.

**(1) `DEAD` (me) × `ESTABLISHED` (pass 1) — 1 row, reading po16 `extraToneScore`.** The `= 0.0` at
`keymodeanalyzer.cpp:588` writes a local field read nowhere. My re-derivation independently reaches
**DEAD** from the frozen prose ("read NOWHERE, grep-confirmed … vestigial/dead"); pass 1 templated the
literal ESTABLISHED without a consumer-check. This reproduces the ONE substantive miss the pass-2
second reading caught — already registered **OI-96 (DT-5)**. *Diagnosis:* pass 1's mechanical
constant-classifier assigned a structural reason to a dead-field write; the fine re-derivation confirms
OI-96 from an independent path and strengthens it. Pass 1 was the pass in error; no new row.

**(2) `ESTABLISHED` (me) × `UNFIT`/`DEFERRED` (pass 1) — 20 rows.** Examined at the frozen `context`:
**18 are `ParameterBoundsMap` range-endpoint literals** (e.g. `{ "extraScaleFactor", { 0.0, 0.5 } }`,
`{ "modePriorMixolydian", { -5.0, 5.0, true } }`), **1 is an inline `×0.5` half-boost factor**
(`characteristicPitchBoost * 0.5`, po69), **1 is an inert else-branch `0.0`** (`c.endsPhrase ?
kWeightStructural : 0.0`, po111). My prose-reading identified the literal precisely (a bound / an inert
zero → structural → ESTABLISHED); pass 1's mechanical classifier assigned each numeric literal in the
bounds-map / preferences region the DISPOSITION OF THE PARAMETER it relates to — **UNFIT** for an L3
emission param, **DEFERRED** for an L4 param on the shared leaf — without distinguishing a range
endpoint or an inert else-value from a fitted default (its per-row reason string literally calls the
bound `5.0` an "emission default"). *Diagnosis:* a rubric-application difference on structural literals,
**not a correctness defect in either pass**. Pass 1's coarser treatment is the more CONSERVATIVE one
(the whole `ParameterBoundsMap` is part of the un-manifest L3/L4 parameter surface, OI-91), and it
already covers these; my prose-derived ESTABLISHED is the LESS conservative reading — the prose's
"default in range, consistent" checks well-formedness, not manifest-tracking or fit, so it over-states
establishment for the range bounds (and for the inline `×0.5`, an OI-25-class inline hand-set factor).
Where the two readings differ, pass 1's UNFIT/DEFERRED is the one to rely on; it is already tracked
(OI-91 / L4 audit). No new row; no code defect.

Direction check: there is **no row where pass 1 decided a fine label my re-derivation contradicts in a
way that reveals an untracked L3 code defect.** The one place pass 1 was wrong (the dead field) my
re-derivation catches; everywhere else pass 1 is either concordant or more conservative.

## 6. The constants axis — ESTABLISHED-versus-UNFIT, and manifest-sweep coverage

This is the axis the coarse vocabulary collapsed, and the finding is precise:

- **The prose recovers UNFIT for only 2 of the ~24 fitted L3 magnitudes** — exactly the two whose prose
  says "provisional" (`declaredModePenalty`, `JointKeyWeights::modulation`); both are **CONCORDANT** with
  pass 1's UNFIT. For the other **22 fitted magnitudes the prose stays UNRESOLVABLE**: it says
  "empirical / in-bounds / theory-grounded ordering / live", which distinguishes fitted from structural
  but does NOT reach the "not-positively-established / UNFIT" verdict — that verdict comes from the
  manifest cross-check, not the prose.
- **So the pass-2 report's claim "the per-row prose carries the finer distinctions" is TRUE on the code
  and derived-facts axes and OVERSTATED on the constants axis.** The prose carries the coarse
  structural-vs-empirical split (it says "empirical"); it does NOT carry the P2 ESTABLISHED-vs-UNFIT
  verdict the coarse vocabulary dropped — that is precisely the distinction that was collapsed, and the
  prose does not restore it.

**Is every unresolvable constant row covered by the mechanical manifest sweep? — Almost:
21 of 22 (`tools/audit/l3/pass2_fine_relabel_crosstab_*.json → unresolvable_constants`).**
- 17 (pass-1 UNFIT) + 2 (pass-1 DEFERRED, L4 params) are directly flagged not-in-manifest by the DT-2
  sweep / the L4 deferral (OI-91).
- 2 mode-prior `ModePriorPreset::` struct fields that pass 1 filed NO-ISSUE (plumbing) are still swept by
  DT-2 (`*Preferences`/`*Preset`/`*Weights` members are all flagged — the pass-2 report's DT-2 122 count
  includes them), so they are covered.
- **The ONE exception: `ReachBackOptions::maxReachSteps = 8`** — a bound on the default-OFF reach-back
  feature. The DT-2 struct-name patterns (`*Preferences`/`*Preset`/`*Weights`/`k*`) do not match
  `ReachBackOptions`, and pass 1 filed it NO-ISSUE (plumbing). It is therefore NOT mechanically covered —
  but reach-back is dormant on production (fire-rate 0 by construction, pass-1 §P4), so the value is
  inert and carries no inference load. It is within OI-91's spirit (the whole L3 emission/config surface
  un-manifest) but outside its enumerated list and the sweep's patterns; the EG-5/OI-91 manifest
  extension should pick up dormant-config bounds like it.

## 7. Updated certification statement (proposed, awaiting the user's decision)

Taking pass 1, the pass-2 sweep, the blind reading, and this re-derivation together: **the L3 (key/mode)
spine certification proposal (`cc_l3_audit_pass2_report.md` §6) still stands, weakened only by named,
bounded, covered gaps** —

1. The pass-2 second reading's coarse constants vocabulary does not itself carry the P2
   ESTABLISHED-vs-UNFIT verdict for the L3 fitted-parameter surface (22 rows UNRESOLVABLE-from-prose),
   and it over-establishes ~20 structural range-bound/inline literals that pass 1 flags more
   conservatively. **This is a property of the audit's vocabulary, not of the L3 code** — and it is fully
   backstopped by the independent DT-2 mechanical manifest sweep (OI-91), which flags the entire L3
   emission + bounds + config parameter surface as not-in-manifest. The single row the sweep's patterns
   miss (`maxReachSteps`) is dormant/inert.
2. The one correctness-relevant finding on the constants axis — the dead `extraToneScore` field — is
   **independently reproduced** by this re-derivation and is already registered (OI-96, a hygiene item,
   no runtime effect).
3. The code and derived-facts axes are carried by the prose without loss (56/56, 16/16), so the
   vocabulary deviation cost nothing there.

Net: the deviation lost fine information the coarse reading's prose alone cannot recover on the
constants axis, but the loss is named, bounded, and covered by the mechanical sweep — it does **not**
introduce or hide any untracked correctness defect. The certification decision remains the user's.
**Status: proposed, awaiting the user's decision.** This report does **not** mark OI-84 or the EG-7 entry
gate satisfied — those are the user's; OI-84 and OI-100 are left OPEN.

## 8. Self-check (the CLAUDE.md rule)

Read the diff of every touched file against the guiding principles, conventions, and gate policies:
- **#8 (no inference-problem-driven coding):** none — read-only measurement; no `src/`, no constant, no
  golden, no reference artifact touched.
- **#12 (no information loss):** the UNRESOLVABLE bucket is carried explicitly rather than forcing a
  label — the exclusion IS the measurement.
- **#15/#19 (verify at objects; establish instruments):** the crosstab is joined at the frozen artifacts;
  `relabel_fine.py` self-checks totality + axis-consistency and fails loud; `crosstab_fine_vs_pass1.py`
  prints every bucket. The 20 bounds disagreements were verified at the frozen `context`, not asserted.
- **#17(f) (no hand-transcribed numbers):** every figure in §3–§6 is emitted by a generator
  (`relabel_fine.py`, `crosstab_fine_vs_pass1.py`); none is hand-typed from memory.
- **Conventions (no self-invented labels):** the emitted vocabulary is the protocol's
  (ESTABLISHED/UNFIT/DEAD · SURVIVES/RETIRES · PUBLISHED/SILOED/TRAPPED/DUPLICATED) plus the instruction's
  plain phrase "unresolvable from prose"; the reason codes are internal generator keys (each expanded to
  a plain-language justification in the output), never surfaced as jargon in this prose. American English;
  British spellings appear only inside quoted frozen `coarse_reasoning`.
- **git:** only my own files staged by name; the known carry `cowork_joint_key_chord_design.md` untouched;
  `upstream` push disabled (verified); fork-only.
