# The Engage-Arc Path Forward — ratified, principle-grounded

> **RATIFIED by the user, 2026-07-07.** The standing reference for the order of work from here to the
> precision phase. It does not re-derive the fix details — those live in `cowork_structural_integrity_audit.md`
> (§3 fix-queue, §4 sequencing) and the roadmap (E4/R9, the §6-block dissolution). This document fixes the
> **order and the principle behind each step**, so the plan is checkable against the principles, not memory.

## The governing rule and the two placement rules

- **#8 sets the macro-shape:** no inference-problem-driven coding until ALL refactoring, architectural design,
  and algorithmic completion are done. Architecture first; precision last.
- **#6 (one path per concern, no duplicated effort) places the legacy tangles:** do not refactor code that is
  about to be retired and already has a clean replacement. The `results` cap→workaround tangle is legacy
  Layer-4 code whose clean-target is **already built in the dormant decoder** — so it is retired by the
  decoder engagement (E4), never a standalone throwaway refactor.
- **#7 (each concern owned by its proper layer) places the owner-decisions:** a fix whose correct owner is a
  layer still being designed waits for that design (e.g. quality-from-key's owner is a Layer-5 decision).

## The stages (in principle order)

**Stage 1 — PRE-Layer-5 refactoring. ★ DELIVERED 2026-07-07 (arc #7).** The portable unification wins that
stand alone (#8-first; restores #6/#7). **Landed byte-identical:** the fact-layer duplication cleanups (FQ-5:
beat-weight, emission-sigmoid, node-builder; S7 partial), the serialization/display cap-views (FQ-6,
byte-identical structural only — the cap-#2 value lift stays deferred to Stage 3), the key-decoder constant
sourcing (FQ-7/S8; S9 verified load-bearing and KEPT). **Reassigned to Stage 3 (E4) after code inspection:**
FQ-1 (the four "best different-root" scans are NOT one decision — legacy compares root-only, the decoder
root+quality; the legacy scans retire with the decoder, not a false pre-L5 unification) and FQ-3
(`findTemporalContext` is relocatable but E4-supersedes it — throwaway pre-L5, #6). Minor open: S7 full
single-sourcing (a dependency-profile call). **Execution discipline:** each is one revertible,
provenance-stamped
commit (#14), verified on the full output surface — winner AND alternatives (#15) — on the frozen corpus
(#9), docs + regression tests in step (#10/#11); byte-identical is the expectation, any output move gets the
explained re-baseline (#16), never a silent edit.

**Stage 2 — the Layer-5 engagement DESIGN (#8's architectural-design phase; read-only).** Built on
established fact — the decoder's already-clean carry is the factual basis (#1) — carrying the full graded
distribution incl. ruled-out readings (#12, finding-by-exclusion). Decides the owners the audit surfaced:
quality-from-key (FQ-2), pedal detection's home, the confidence-scale fix (F-1/S19). Grounded also by
`cowork_functional_analysis_research_grounding.md`.

**Stage 3 — algorithmic completion: E4 (decoder engages) + the §6-block dissolution (OWED #2).** The
`results` tangle dies by construction as the decoder's governed carry replaces the substrate (FQ-4); the owed
migrations land (two-segmenters retirement, two-pitch-context collapse, tpc-reader fold, `function/` rename);
quality-from-key gets its one owner (FQ-2); the divergent legacy different-root scans retire (FQ-1, the
decoder's root+quality version is the clean one); `findTemporalContext` ownership moves here (FQ-3). Each a ratified behavior change (#14) proven on the full surface
(#15) under the robust-unit regression stop (#11), with the re-baseline discipline (#16).

**Stage 4 — R9: the `chordanalyzer.cpp` file split (OWED #1), LAST.** "Split once," after the E4 removals.

**Stage 5 — the moratorium lifts (#8): the PRECISION work (#4).** Recover the corrections the fine-grain
override gave up (bass/spelling/joint-consistency, per the research), wire the calibration maps + θ, the
remaining calibration items (L1.5 texture, cadence). Everything deliberately gated behind finishing the
architecture.

## Standing habits (throughout)
Surface a surprise as a STOP before building around it (#13); investigate rather than assume when facts are
thin (#5); test/measure only on non-stale corpora (#9); verify at objects on the full surface (#15).

*Cowork, ratified 2026-07-07. Cross-refs: `cowork_structural_integrity_audit.md` §3/§4;
`cowork_stage5_fitter_design.md` (O-22, the owed refactors); the roadmap ENGAGE block (E0–E5) + R9.*
