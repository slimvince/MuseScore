# CC — OI-160: the joint-probe evidence collapsed to ONE artifact; both rulings re-confirmed

**Session:** 2026-07-13 (CC), on Cowork's dispatch `cc_instruction_oi160_and_push.md` and the user's
**option-A ruling**. **Type:** evidence-record hygiene on `tools/reports/` + the wave-1 fork push.
**NOT `src/` work, NOT a governing re-baseline.**

> **Provenance / reproducibility (#16).** Corpus `c50002fee1` (pinned, 352 XMLs, 326/352 WiR-covered
> per preset — unchanged). Instrument `tools/measure_joint_probe.py`, measurement code **unchanged**
> by this session (verified: `git diff --stat 6725329381..HEAD` touches no `src/`, no
> `measure_joint_probe.py`, no `compare_rn` / `compare_analyses` / `dcml_parser`). Starting HEAD
> `edd4d3e4cf`. **No `src/composing` or `src/notation` file is touched. No gate, threshold, fit, or
> baseline reads this artifact.** Establishment battery byte-identical across the whole session.

---

## 1. The headline

**Every prediction held; both rulings stand; nothing governing moved.**

The two committed artifacts of the one instrument `measure_joint_probe.py` are **collapsed into one**,
refreshed under the OI-142-corrected ground truth. The **arc-12 chord-axis no-go** and the
**OI-43/OI-44 shelve** are both **re-confirmed with corrected numbers — neither is reopened.**

| gate | before the first edit | after the last |
|---|---|---|
| `register` | 160 row IDs, no collision | **identical** |
| `a8_diff` | `+0 / −0` all three presets, class-(b) Δ +0, coverage OK | **identical** |
| `calib` | 4/4 maps sha256-identical | **identical** |
| `validate` | 3/3 corpus manifests OK | **identical** |
| Python suites | 134 + regression suite, green | **134 + regression suite, green** |

All four battery gates compared field-by-field before vs after: **0 differ.**

---

## 2. The collapse premise — PROVEN at the files, not assumed (#18)

The dispatch's ruling rests on a causal claim — *the arc-12 artifact is a strict subset of the OI-43
run* — and the dispatch itself said: **if that does not hold at the files, STOP.** It was therefore
checked before anything was written, by walking both JSON trees:

| check | result |
|---|---|
| Fields in `joint_probe_measure.json` (arc-12, `fa0a881aa4`) **absent** from `mode_key_chord_probe.json` (OI-43, `6725329381`) | **0** |
| Fields the newer adds | **93**, and **every one** under `key_axis_desksim` |
| Fields the newer adds **outside** `key_axis_desksim` | **0** |
| Corpus / instrument / score count | identical (`c50002fee1`, 352 scores, 3 presets) |

**The subset relation holds exactly.** The newer run is the older run plus the key-axis block and
nothing else. There was never a second *concern* — only a second *file*. The collapse premise is
sound, and #6 (one path per concern) was being violated, not served, by keeping two.

---

## 3. What is canonical, and why that was a fact rather than a choice

The dispatch said: write the full run to **"the instrument's natural committed target."** That target
is recorded in the instrument's own code, so no invention was needed —
`tools/measure_joint_probe.py:470-477` names exactly **one** committed path in its `--out` help:

> *"that file is COMMITTED evidence (the arc-#12 / OI-43 go/no-go the shelve ruling rests on) …
> pass `tools/reports/joint_probe_measure.json` explicitly to re-baseline the committed evidence"*

It is also the name derived from the instrument's own (`measure_joint_probe.py` →
`joint_probe_measure.json`), and the instrument's comment **already named both rulings** as resting on
it — the code anticipated the collapse the file layout had drifted away from.

- ✅ **Canonical: `tools/reports/joint_probe_measure.json`** — one file, **both axes**.
- 🗑️ **Retired: `tools/reports/mode_key_chord_probe.json`** (the dispatch's "separately-named" file).
- 📸 **O-12 snapshot FIRST:** both outgoing files preserved verbatim at
  `tools/reports/snapshot_2026-07-13_pre_oi160/`, with a `SNAPSHOT_NOTE.md` recording what each was
  and why it was superseded. (The prior OI-159 snapshot is kept beside it, untouched.)

To stop a future session re-creating the duplicate, the instrument's `--out` comment now states that
this is **the one committed artifact, both axes**, and that a new question belongs in a new **block**
of the report, not a new file.

---

## 4. Re-confirmation 1 — the arc-12 chord-axis NO-GO STANDS

`cc_engage_stage3_joint_measure_report.md` §2.1, refreshed (superseded figures kept beside, #12):

| preset | top-alt flip corr / harm → **net** | as % of the ~6,200 scored regions |
|---|---|---|
| Baroque | 37/28 → **38/29** | net **+9** = **+0.14 pp** |
| Jazz | 36/33 → **39/33** | net **+3 → +6** = **+0.10 pp** |
| Default | 35/25 → **36/26** | net **+10** = **+0.16 pp** |

**Net (corr−harm) `+9 / +3 / +10` → `+9 / +6 / +10`.** The written shelve floor is **+0.3 pp**; the
corrected figures are **+0.10 to +0.16 pp** — a third to a half of the floor. Baroque and Default did
not move at all; Jazz moved by three regions. **The no-go is not close to being threatened.**

**★ And the evidence it actually rests on never moved at all.** The report's §2.2 — the **coupled
minority**, the *only* population the joint step is theory-scoped to (key-uncertain regions, sequence
margin < 1.0) — is **byte-identical** under the corrected ground truth:

| preset | coupled flipped regions | corr / harm / neutral | net |
|---|---|---|---|
| Baroque | 16 | 4 / 4 / 8 | **0** *(unmoved)* |
| Jazz | 15 | 8 / 3 / 4 | **+5** *(unmoved)* |
| Default | 11 | 2 / 4 / 5 | **−2** *(unmoved)* |

None of the three re-sorted flips fell in the coupled minority. So the sharpest form of the go/no-go —
*"on the population the joint step is scoped to, the net is zero-to-noise and the sign is not even
stable across presets"* — is **untouched by the correction, not merely unthreatened by it.**

---

## 5. Re-confirmation 2 — the OI-43/OI-44 SHELVE STANDS

Re-confirmed at OI-159 and reproduced here to the digit from the canonical artifact:

| prediction | bar | measured | verdict |
|---|---|---|---|
| **P3** menu-containment (GT key in the carried menu) | ≥ 80 % | **75.6 / 68.7 / 72.5 %** | **NOT MET** — still under the bar |
| **P1** chord-flip-under-GT (the coupling mechanism) | — | **7 / 8 / 6** regions (0.33–0.41 %) | **inert**, as ruled |
| key-ident self-check | 0 mismatch | **0 / 6409, 0 / 6311, 0 / 6413** | clean |

The coupling the joint-step question turned on still does not fire; the menu still misses the true key
often enough to matter (but in **~¼** of key-disagree regions, not ~⅓ — the menu-widening signal is
**weaker** than originally recorded). **The shelve stands.**

---

## 6. The causal claim held exactly — our analyzer never moved

This is the check worth keeping. Of the **109 fields** the retired arc-12 subset shares with the
refreshed run, **the only ones that moved are ground-truth-graded** (`benefit_top_alt_flip`,
`benefit_per_flip_pairs`, `benefit_any_alt_bound` — corr / harm / neutral / net):

- **Not one** `fire_rate` field moved (99 / 95 / 89 flip regions, byte-identical).
- **Not one** `beam_width_carried_keys`, `pedal_owed_p1`, `n_regions`, `n_committed`, or
  `n_scored_regions` field moved.

Which chords flip is a property of **our analyzer**; whether a flip *corrects or harms* is graded
against the **ground truth**. OI-142 corrected the ground truth. Exactly the fields that depend on the
ground truth moved, and exactly the fields that depend on our analyzer did not. **The mechanism is
confirmed at the field level, not inferred.**

Stronger still — the refreshed artifact vs the OI-159 run: **181 leaf fields compared, exactly ONE
differs: `git_hash`.** Nothing in the measurement path changed between the two runs, and the
measurement proves it.

---

## 7. Citations re-pointed — and the ones deliberately left alone

**Re-pointed (live evidence pointers — a reader following these must land on the canonical artifact):**

- `cc_engage_stage3_joint_measure_report.md` — the **arc-12 no-go record**: §2.1 figures corrected in
  place (superseded kept beside, #12), §2.2 marked byte-identical, provenance block re-pointed.
- `cc_mode_key_chord_probe_report.md` — the **OI-43/OI-44 shelve record**: artifact path re-pointed
  (3 sites), and its own OI-160 forward-reference closed.
- `OPEN_ITEMS.md` — OI-160 flipped to resolved with provenance; OI-43 and OI-141 evidence pointers
  re-pointed; OI-159 given a forward pointer so its historical paths do not strand a reader.
- `cowork_key_mode_inference_diagnosis.md`, `cowork_handoff.md` — re-pointed.
- `tools/measure_joint_probe.py` — the `--out` comment now names the single canonical artifact
  (doc-comment only; **no measurement code touched**).

**Deliberately NOT rewritten — declared, not skipped:** past **instruction files** and **historical
session reports** (`cc_instrument_hygiene_sweep_report.md`, `cc_wave1_finalize_report.md`, the
`cc_instruction_*.md` dispatches, the dated session-log blockquotes in `cowork_handoff.md` / `STATUS.md`)
still name `mode_key_chord_probe.json`. Those record **what was true when they were written** —
rewriting them would falsify provenance and destroy information (#12), which is a worse fault than a
stale path in a dated log. The register row and the snapshot note tell any reader who follows one of
those paths exactly where the file went.

**A doc-sync tail, fixed in passing:** OI-159 refreshed the artifact and its own report, but two *other*
live consumers still carried its **superseded** menu-containment (66.7 / 61.6 / 64.1 %) — the **OI-141
register row** and `cowork_key_mode_inference_diagnosis.md`. Both now carry **75.6 / 68.7 / 72.5 %**
with the superseded figure beside it. Not a new defect class — the last tail of the same OI-142 drift.

---

## 8. Premise Gate — predictions vs outcomes (#17b)

Written to `predictions.md` **before** any measurement was run.

| prediction (written before measuring) | outcome |
|---|---|
| **P-0** The arc-12 artifact is a strict subset; the newer adds only `key_axis_desksim` | ✅ **MET exactly** — 0 fields missing; all 93 added fields under `key_axis_desksim`, 0 elsewhere |
| **P-1** Fire-rate byte-identical at 99 / 95 / 89 (our analyzer's property) | ✅ **MET** — byte-identical |
| **P-2** corr/harm re-sorts to 38/29, 39/33, 36/26 ⇒ net **+9 / +6 / +10** | ✅ **MET to the digit** |
| **P-3** The refresh reproduces the OI-159 run in **every** measurement field; only `git_hash` differs | ✅ **MET** — 181 leaves, **exactly 1 differs: `git_hash`** |
| **P-4** Both rulings stand (no preset above the +0.3 pp floor; menu 75.6/68.7/72.5 %; flip 7/8/6) | ✅ **MET** — max +0.16 pp; both reproduced exactly |
| **P-5** Establishment battery byte-identical (no governing surface touched) | ✅ **MET** — all 4 gates identical, 0 fields differ |
| **P-6** The push reaches `origin` only; `upstream` untouched and still push-disabled | ✅ **MET** — see §9 |

**Nothing landed off-prediction. No surprise, therefore no STOP (#3/#13).** One thing was *found*
rather than predicted — the OI-141 / diagnosis-doc stale-figure tail (§7) — and it is a doc-sync
correction inside the dispatch's own "re-point every citation" scope, not a new finding.

---

## 9. The push (Task 2)

`git remote -v` verified **before** pushing: `upstream` (`musescore/MuseScore`) push is **`disabled`**
and was left so. Pushed to **`origin` only** (`slimvince/MuseScore`), branch `master`. The fork-local
MusicXML declared-mode patch `cfc7eb5e39` travels to `origin` only; an `upstream` push/PR would be a
**HARD STOP** and none was attempted.

---

## 10. Self-check against the standing instructions (#10, CLAUDE.md)

Diff of every touched file re-read on disk before reporting.

- ✅ **#1 fact/theory only** — the collapse premise was *proven at the files* before acting, and the
  dispatch's own STOP condition was honored as a real branch, not a formality.
- ✅ **#6 total unification** — the whole point: one instrument, one artifact. The duplicate is gone
  and the instrument now says so, so it cannot silently come back.
- ✅ **#12 no information loss** — the retired file is snapshotted verbatim (O-12); every superseded
  figure is kept beside its correction rather than overwritten; historical records are not rewritten.
- ✅ **#15 verify at objects on the full output surface** — verified at 181 leaf fields, not at the
  headline: the winner *and* the carry.
- ✅ **#16 reproducibility** — every figure enters via the generated artifact; **no hand-transcribed
  numbers** (#17f). The one derived quantity in prose (pp of scored regions) is arithmetic on two
  artifact fields — **and the self-check caught me getting it wrong.** The §4 table (computed from the
  artifact) read Baroque `9 / 6249 = +0.14 pp` correctly, but the one-line *summary triple* I then
  hand-wrote into `STATUS.md`, `OPEN_ITEMS.md` and `cowork_handoff.md` said **+0.10** / +0.10 / +0.16.
  Recomputed from the artifact and corrected to **+0.14 / +0.10 / +0.16 pp** in all three before
  committing. Nothing downstream depended on it (the shelve floor is +0.3 pp either way), but it is
  precisely the failure mode #17f exists to prevent: **the number was right where it was generated and
  wrong where it was retyped.** Recorded, not quietly fixed.
- ✅ **#19 no unestablished instrument** — the instrument is unchanged and its self-check reports
  **0 mismatches** on 6409 / 6311 / 6413 regions.
- ✅ **No self-invented labels** — "menu-containment", "chord-flip-under-GT", "coupled minority",
  "fire-rate" are the names already in the code and the records.
- ✅ **No `src/` change, no build, no golden refresh, no re-baseline, no fit, no constant tuned.**
- ✅ **No inference-problem-driven coding** — no inference behavior was designed or changed; this is
  evidence hygiene. Nothing was built around a surprise.

---

## 11. Where this leaves the gate

**OI-145 wave 1 — the measurement chain — is CLOSED and PUSHED.** Every item it surfaced is
dispositioned; no wave-1 item is left open; every graded surface is established and byte-identical
across every commit of the wave.

**Next: wave 2 — the `src/` substrate** (OI-86, OI-13, OI-87, the file-table reasons), toward lifting
the key-layer readiness gate.
