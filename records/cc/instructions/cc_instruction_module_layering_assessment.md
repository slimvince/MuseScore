# CC Instruction — Module layering assessment: READ-ONLY survey

> **Refactor #1 done** (`chordanalyzer.cpp` byte-identical split, committed `41f7c65f63`, Cowork-verified).
> Before deciding the next split(s) or starting the layer audit, **investigate** whether the OTHER major
> composing modules conflate responsibilities the way `chordanalyzer.cpp` did — i.e. which need a similar
> byte-identical layer-split, and which are already single-responsibility (audit-ready). **Read-only. No code
> change.** This sizes the remaining structural refactoring and the audit-readiness, per "investigate first."

---

## §1 — Scope

Read-only survey of `src/composing/analysis/` — at minimum: `key/keyresolver.cpp`, `key/keymodeanalyzer.cpp`,
`section/sectionanalyzer.cpp`, `region/regionanalyzer.cpp`, `function/harmonicfunctionlayer.cpp`,
`section/jointkeydecision.cpp`, `section/localmodulationdetector.cpp`, `section/cadencekeyanchor.cpp`,
`function/tonicizationlabeler.cpp` (+ any other TU > ~400 lines). **No edits, no build** (source reading;
cite `file:line`). HEAD unchanged (`41f7c65f63`).

## §2 — The assessment tasks

1. **Inventory.** For each significant TU: line count + the distinct responsibilities it holds (the way the
   `chordanalyzer.cpp` map enumerated oracle / gates / formatter / voicing / diagnose).
2. **Classify each:** **SINGLE-RESPONSIBILITY** (one clean job → no split needed, audit-ready) vs
   **CONFLATED** (multiple responsibilities in one TU, like `chordanalyzer.cpp` was → candidate for a split).
   For each CONFLATED one, list the responsibilities + the rough seams (call-site boundaries, like the
   chord map) — enough to judge splittability, not a full split plan.
3. **The joint-decision 2-pass bolt-on (specifically).** `applyJointKeyWiring` (in `regionanalyzer.cpp`) +
   `decideJointKey` (`jointkeydecision.cpp`): is the wiring cleanly layered, or a bolt-on whose
   responsibility is smeared into `analyzeRegions`? Flag it — and note whether restructuring it would be
   **byte-identical** (pure structure) or **behavior-touching** (then it is NOT a pure refactor; defer).
4. **Byte-identity feasibility per candidate.** For each proposed split, state whether it is achievable as
   **pure movement** (byte-identical, like #1) or whether the responsibilities are **logically entangled**
   such that separating them would change behavior (→ flag as a behavior-change refactor, deferred under the
   no-inference-change rule — NOT a pure split).
5. **Prioritize.** Order the pure-byte-identical split candidates worst-tangle-first; list the
   already-clean (audit-ready) TUs separately.

## §3 — Output: the layering assessment (dossier, no code)

Write `cc_module_layering_assessment_dossier.md` (gitignored, HELD): the per-module inventory + classification
(clean vs conflated), the prioritized **pure-byte-identical split list** (each with its seams + feasibility),
the separately-listed **behavior-entangled** candidates (deferred), and the **audit-readiness verdict** —
which layers are already separable-and-auditable now, and which splits should precede a meaningful
layer-by-layer audit. Frame it as the spec for the next refactor decision (more splits, in priority order,
vs begin the audit). **Recommend nothing built — surface the measured map for a Cowork/user direction call.**

## §4 — Stop conditions
- Any code change in this step (read-only) → STOP.
- A "split" that would require a logic change to separate the responsibilities → classify it as
  **behavior-entangled** (deferred), do NOT plan it as a pure split.
- Uncertain about a TU's responsibilities or a seam → read the source, cite `file:line`, surface — never
  guess whether something is conflated.
