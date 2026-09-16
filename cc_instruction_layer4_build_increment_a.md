# CC Instruction — ARCHITECTURAL LAYER 4 build, Increment A: per-slice chord path + grading harness (isolated, byte-identical)

> Layer 4 is **signed** (`cowork_layer4_chordsymbol_design.md`) and the pre-build audit is done and verified
> (`cc_layer4_audit_dossier.md`). Build the **first increment** the way L3 was built: a new per-slice chord module
> that runs **isolated** (under a read-only diagnostic, NOT wired into the live per-region path), graded against the
> held-out chord ground truth, with **production byte-identical**. The genuinely-new parts (the membership decision,
> the spelling-pin, the new chord types) come in **later increments** — this increment stands up the per-slice path
> and the grading so those land on a measured baseline.
>
> **★ No-assume:** anything not confirmable at source → STOP/surface. Terminology is plain in the spec; use the actual
> code symbols (`snapshotOut`, `weightedPcView`, …) for source references.

## §1 — The module (this increment)
New module `src/composing/analysis/chord/chordslicedecoder.{h,cpp}` (name to taste; sits beside `chordanalyzer`).
For each Layer-2 slice (`changePointSlices(noteModel)`):
- Build the slice's note window through the **indexed** builder `weightedPcView` over the slice span (and its
  immediate neighbours) — **never** a region aggregate or a DOM walk (audit §5; the per-slice perf floor).
- Run the **existing scorer** (`analyzeChord`) over that window and **surface the complete candidate list** via the
  `snapshotOut` parameter (the `ScoringSnapshot.cells` — every (bass × root × type) with its fit score), exactly as
  the L3 decoder surfaced the 252-candidate key dump. Rank, keep the top-K (∪ the prevailing chord), the L3 pattern.
- Produce a per-slice result carrier with the **spec §7 fields**: chosen chord (root + quality + **bass/inversion**),
  ranked alternatives, `confidence` (margin to the best *different* chord), `uncertain` (low margin). Membership sets
  are **stubbed empty this increment** (filled in Increment B).

**This increment does NOT yet:** decide per-note chord-tone-vs-NCT membership; pin the symmetric (dim7/aug) root from
spelling; add the diminished-seventh / minor-major chord **types**; or read extensions from membership. It is the
per-slice scorer + the complete candidate list + the result carrier + grading — so Increment B's membership lever
lands on a measured baseline.

## §2 — Grading harness (read-only diagnostic + the metrics)
- A `batch_analyze --decode-chords` flag (default OFF, mirrors `--decode-keymode`): per score, build the note model,
  slice, run the per-slice chord decoder, emit its per-slice chord (root + quality + inversion + confidence +
  uncertain). **Returns before `analyzeScore`** ⇒ production untouched.
- Grade the decoder's per-slice chord vs the **held-out** chord ground truth, per preset, **reusing** the existing
  chord-root tooling (`oracle_root_metric.py` / `characterise_bir_false.py` — one grading path, extended not forked).
- **Stand up the new membership metric *now*, even though membership is empty this increment:** build the harness that
  extracts the human-analysis **chord-tones per event** and will score per-note chord-tone-vs-NCT **precision/recall**
  (spec §10). This increment reports it as the trivial baseline (no NCTs called yet); Increment B fills it. Building
  the metric here means the lever is measured the moment it exists.

## §3 — Gate (this increment: isolated, byte-identical)
- **Production byte-identical:** the per-slice decoder runs only under `--decode-chords`; the live per-region
  `analyzeChord` path (`regionanalyzer.cpp:763`) is untouched. `composing`/`notation`/snapshot tests unchanged; BIR
  identity sets unchanged. If any production metric moves → STOP (it got wired in by accident).
- **Behavioural unit tests** for the per-slice path: a clean triad slice → that chord; the complete candidate list is
  surfaced and ranked; `redecodeRange`-style determinism (same input → same output); the carrier fields populate.
- **Directional baseline (the learning, not a pass/fail bar):** report the per-slice decoder's held-out chord-root
  vs the per-region baseline, per preset. Expect it to be **rough on embellishment-heavy slices** (no membership yet
  → passing tones over-read) — that gap *is* the Increment-B membership headroom; report it, don't tune it away.

## §4a — Unification (no permanent duplicate paths)
- **One tone-window builder.** The audit found two window families (`regiontonecollector` chord-side vs
  `regiontoneprimitives` key-side) + a legacy DOM-walk `collectPitchContext`. This increment reuses the **indexed**
  `weightedPcView`/`pitchContextOverSpan`; do **not** add a third window builder.
- **Reuse the scorer, don't fork it.** The candidate list comes from the existing `analyzeChord` + `snapshotOut` — no
  second chord scorer.
- **Report the ledger:** what is reused (the scorer, the cube via `snapshotOut`, the indexed window, the L2 slicer,
  the chord-root metric), what is newly written (the per-slice module, the result carrier, the `--decode-chords`
  diagnostic + the membership-metric harness), and what is **slated to retire at wiring** (the per-region chord path).
  End with: *"No NEW parallel path or logic duplication was introduced."*

## §5 — Effort-retrofit hygiene
The window size/extent, the top-K kept, and the uncertain threshold are **settings on a preferences struct**, not
hardcoded constants — seeded with sensible defaults, swept later.

## §6 — Deliver + the increment plan
Commit **locally (unpushed)**: the module + its tests + the `--decode-chords` diagnostic + the grading/membership-metric
harness. Leave held WIP unstaged; `cc_*` report gitignored. Write `cc_layer4_build_a_report.md`: the per-slice path as
built, the byte-identity confirmation, the §4a ledger, and the directional baseline (per-slice vs per-region, per
preset, with the expected embellishment gap).
**The increments after this** (for context, not this increment): **B** — the per-note neighbour-aware **membership**
decision + the **two-pass** resolution + the **adaptive lazy-extend window** (the lever; graded by the membership
metric + chord-root). **C** — the **spelling-pin** for the symmetric (dim7/aug) root replacing the key-driven
`dim7CharacteristicBonus`, the new **types** (diminished-seventh; re-test minor-major), and **extensions read from
membership** (retiring the post-hoc flags). **Then** the wiring increment (re-point `regionanalyzer.cpp:763`
per-slice; strip the L5 leftovers — `ChordFunction` on the result, the progression bonuses; gate on BIR + snapshots).

## §7 — Stop conditions
- The decoder gets wired into the live analysis path, or any production output moves → STOP (this increment is isolated).
- The per-slice window goes through a region aggregate or a DOM walk instead of the indexed `weightedPcView` → STOP.
- You start building the membership decision / spelling-pin / new types → STOP (those are Increments B/C).
- A second chord scorer or a third window builder appears → STOP (unification).
