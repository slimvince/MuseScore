# CC report — Engage arc #3: Gate A promotion unification (design & scoping, read-only)

**Dispatch:** `cc_instruction_engage_gateA_unification_design.md` (Cowork, 2026-07-06). The engage arc's
order-of-operations first step (restructuring design before Layer 5 engagement). **Read-only DESIGN + SCOPING —
no `src/` change, no corpus write, no build, no push of a behavior change.** The unification itself is a
*separate* user-ratified build event; this pass produces its ratification surface.

**Deliverable:** `cowork_gateA_unification_design.md` (Tasks 1–4) + this report.

---

## What landed

| Task | outcome |
|---|---|
| 0 — state | HEAD `71c0be114a`, `master`, ahead 0; batch 52/24/52 set-diff empty; robust identity-PASS; corpus `c50002fee1`. |
| 1 — duplication at source | Characterized: **one** real builder `buildChordResult` + **three** thin `buildResult` wrapper lambdas (two byte-identical); **two** promotion idioms (swap-existing vs append-built); mechanical cause of divergence grounded at code + at the 2.2c object verification. |
| 2 — blast radius (FULL surface) | Re-measured read-only at HEAD: **36 Baroque** scores, **0 winner-diffs / 352** (winner-inert on the full set), alternatives-only; **enumerated by name**; carry-delta **content** characterized; snapshot reach = none. |
| 3 — unified design | One `promoteToWinner` primitive (present-first dedup guard) + one collapsed builder wrapper; correct carry = **C_HEAD**, grounded at the O1b carry contract (not assumed); Gate A becomes full-surface-inert and removable; Layer 4, in-layer. |
| 4 — build-event plan | Touches + full-surface verification (expected byte-identical ×3) + the 36-score ratification surface + reuse/retire line. |

---

## Grounding sources (read, not summarized from memory)

- **O-11** — the GateA byte-identity ruling: `cowork_stage5_fitter_design.md:990-999` (winner-inert /
  alternatives-active on 36 Baroque; `std::swap` vs `push_back(buildResult)`; retires when the promotion
  machinery unifies; evidence-method lesson = full surface).
- **O1b carry contract** — `cowork_stage5_fitter_design.md:991-992` (L5 selects among carried readings; E-14
  user-visible) — grounds the correct-carry choice.
- **Measurement of record** — `cc_stage5_phase2_2c_report.md` (RETIRE-5 → byte-identity STOP; 36 diffs;
  0 winners; GateA-alone; `bwv17.7` object mechanism; un-retire → RETIRE-4; FM2 RETAIN-as-structural).
- **Code at HEAD:**
  - Builder function: `chordanalyzer.h:590`, `chordanalyzer.cpp:911`; delegation `chordanalyzer.cpp:1579`.
  - Wrapper lambdas: `postscoringgates.cpp:65`, `chordpostpasses.cpp:129`, `harmonicfunctionlayer.cpp:516`.
  - Gate A swap: `postscoringgates.cpp:214-219`. FM2 append: `postscoringgates.cpp:223-235`.
    Gate E: `255-266`. Gate G-E swap/raw-pull/phantom-pop: `366-373` / `346-356` / `388-392`. Gate G-D: `381-387`.
  - Iter 91 append: `chordpostpasses.cpp:191-199`. Build loop / inversion append: `harmonicfunctionlayer.cpp:520-548`.
  - `RawCandidate` "promote a cell not in top-N" doc: `chordanalyzer.h:312-315`. Enum: `paramoverride.h:74-75`.
  - Call-site pair (`applyIter8691Pedal`+`applyPostScoringGates`): `regiontoneprimitives.cpp:511/516`,
    `harmonicsegmenter.cpp` (×6), `regionanalyzer.cpp:980/1207/1404`, `sectionanalyzer.cpp:427/432`,
    `chorddiagnose.cpp:172/176`.

---

## The blast-radius measurement (Task 2 — read-only, in-scope)

Read-only decode with the **HEAD binary** (no rebuild), `--param-override "disable_rule GateA"` (≡ deletion),
Baroque preset, into a **scratch** dir (frozen `tools/corpus/` untouched); diffed against frozen
`tools/corpus/baroque` (C_HEAD). Enumerator: scratch `enum_gateA_delta.py`.

- **36 / 352** whole-file byte-diffs; **0 / 352** winner-diffs → alternatives-only, winner-inert on the FULL
  surface. Matches the 2.2c recorded count exactly, now enumerated:
  `bwv126.6, bwv139.6, bwv145.5, bwv17.7, bwv177.5, bwv178.7, bwv244.40, bwv245.22, bwv245.40, bwv248.5,
  bwv296, bwv297, bwv300, bwv301, bwv310, bwv319, bwv323, bwv325, bwv346, bwv355, bwv356, bwv365, bwv379,
  bwv383, bwv389, bwv390, bwv398, bwv40.6, bwv40.8, bwv405, bwv424, bwv437, bwv60.5, bwv64.4, bwv78.7, bwv85.6`.
- **Carry-delta content (uniform):** the Minor7-slash winner's **enharmonic Major-add6 partner** is retained
  as an alternative under Gate A (Idiom A / reuse), but under FM2 (Idiom B / append) the last alternative slot
  is overwritten by a **freshly-built near-duplicate of the winner** — a §12 information-loss form (the distinct
  partner reading is lost). E.g. `bwv17.7@19680`: `[A6,A6,A6]` → `[A6,A6,F#m7/A]`.
- **Snapshot reach = none:** the 11 snapshot-corpus stems do not intersect the 36 `bwv###` scores.

**Correct carry = C_HEAD** (retain the distinct partner), grounded at the O1b contract — not chosen because
Gate A is at HEAD. The same anti-pollution principle already exists in-code (the Gate G-E phantom-pop,
`postscoringgates.cpp:388-392`).

---

## The design in one line

One `promoteToWinner` primitive with a **present-first dedup guard** (swap if the reading is already carried,
build-and-append only if genuinely absent) + one collapsed builder wrapper ⟹ Gate A and FM2 become the two
internal branches of one promotion ⟹ the separate `GateA` rule is redundant and removes **byte-identically**
(winner AND carry), because the guarded primitive reproduces Gate A's swap on the 36 and FM2's append on the
absent cases. All Layer 4, in-layer.

---

## Sandwich (trivial — read-only)

No `src/` change ⟹ byte-identical to HEAD by construction: batch stop 52/24/52 untouched, robust sandwich
untouched, suites unchanged (no build). The frozen gate corpus (`c50002fee1`) was **read** for the diff base
and **not written**; the `disable_rule GateA` decode wrote only to session scratch.

---

## Deviations / flags

- **Doc-staleness (reported, not fixed — read-only):** `chordpostpasses.cpp:128` says the wrapper "mirrors the
  buildResult lambda in applyPostScoringGates / analyzeChord" — `analyzeChord` holds no such lambda (it
  delegates to `fn::applyHarmonicFunction`). The third real wrapper is in `applyHarmonicFunction`. The build
  event should correct the comment when it collapses the wrappers.
- **Read-only decode justified in-scope:** the 36-score enumeration was not fully recorded (2.2c recorded the
  count + the `bwv17.7` example only); per the dispatch's Task-2 escape hatch ("otherwise a read-only
  comparison"), the HEAD-binary `disable_rule` decode produced it — decode-only, no `src`/corpus/build, scratch
  output.

---

## SHAs

One `docs(cowork):` fold commit lands this report + `cowork_gateA_unification_design.md` + the STATUS
(session 26) / COWORK_HANDOFF (header) / fitter-O-19 / instruction (force-add) fold — the only commit, no
`src`/corpus/build. Its final SHA is reported to Cowork in the dispatch response (the self-SHA cannot be
embedded in the commit it names — the 22g/22k precedent). Pushed fork-only (`git push origin master`;
`cfc7eb5e39` upstream HARD STOP honored).
