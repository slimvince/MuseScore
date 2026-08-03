# Design-Document Standard Template (the structure every layer/component design doc follows)

> **Standing convention (user, 2026-06-22):** every architecture/design document in this project follows the
> section structure below — a synthesis of **arc42** (the 12-section architecture template) and **IEEE 1016**
> (Software Design Descriptions) + the viewpoints idea of **ISO/IEC/IEEE 42010**. Two arc42 sections —
> **Deployment view** and **Human-interface design** — are **N/A** for our backend analysis modules (no separate
> hardware/runtime deployment; no UI); each doc states that omission once rather than padding.
>
> Sources: arc42.org/overview · IEEE 1016 (standards.ieee.org/ieee/1016) · ISO/IEC/IEEE 42010.

## Writing standard — predicates must be qualified (user, 2026-06-24)
Every predicate or pointer word names its argument. Many words are *two-place*: they point at something but are easy
to write with only one place filled — "uncertain" means uncertain *about what*; "defers" means defers *what* to
*where*; "fits" means fits *by what measure*; "close" / "enough" / "in view" mean *by what test*; "prevailing" /
"plausible" / "spurious" mean *by what rule*. A spec must write the second place, not leave it implied. The mechanical
check: read each such word and force it to be followed by the thing it points at; if that forces a phrase the prose
does not actually supply, the predicate is **unqualified** and there is a hole there. Deferring a *numeric value* to
tuning is allowed; leaving the *argument, or the decision structure it stands for,* unnamed is not. (Method and worked
examples: `cowork_spec_language_sweep.md`, `cowork_layer3_spec_language_sweep.md`.)

## Writing standard — defined terms, plain vocabulary, no shorthand (user, 2026-07-02)
A specification is read by someone who knows music theory and does NOT know this project's private vocabulary.
Anything that can be misunderstood WILL be. Four rules, sharpened on the progression-recognition v2→v4 rewrites:
1. **A §0 TERMS table** (the L6 §0 discipline): every term the document uses is either **standard music theory used
   in its standard sense**, **defined in §0**, or **cited in §0 to the document that defines it** — and nothing is
   used before its row. A named example (a "Prinner") is a term: define it or cite its catalog entry.
2. **No invented synonyms for things that have names.** "Chord progressions including chord substitutions", never
   "multi-chord functional knowledge"; "harmonic sequence", never "transposing schema chain". Project-coined terms
   are allowed only where no standard term exists, and they live in §0 with their definition.
3. **No shorthand or insider compression:** "iff" → "if and only if"; a jargon handle for a mechanism ("the carried
   readings", "the bar") appears only after §0 states what it is and where it is defined — and prefer restating the
   mechanism's full rule at first use over pointing at it.
4. **Audit inherited prose as hard as new prose.** A QA pass binds the whole document regardless of which revision
   wrote each sentence; the QA record states it was run on the full current text.
5. **Multiple-meaning words: one sense per document, declared (user, 2026-07-02).** A word with more than one
   plausible reading ("key" = tonality vs important; "sequence" = the harmonic device vs an ordered series; "bar" =
   threshold vs measure; "measure" = bar vs metric) is used in exactly ONE sense throughout the document, and that
   sense gets a §0/glossary row. Where the excluded sense would be needed, a different word is used. (The catch that
   made the rule: a §-heading "…as key evidence" — meaning evidence of the key — read as "crucial evidence".)

## The sections (in order)
1. **Introduction & purpose** — what this component is, *why* it exists (the problem it solves), scope (in/out),
   and **status** (design / signed / as-built + commits).
2. **Constraints** — what the design must honor: architectural invariants (frozen upstream layers, dependency
   order, lossless/annotate-don't-transform), product constraints (any score / any size / any style, incremental
   re-analysis), and project conventions.
3. **Context & scope (external view)** — the module boundary: **imports/dependencies** (what it consumes),
   **exports/public API** (types + functions), and **consumers** (who uses it and for what). What it explicitly
   does NOT depend on.
4. **Solution strategy** — the fundamental approach and *why this shape* (the key idea, in plain terms, before the
   mechanics).
5. **Building-block view (static / internal structure)** — the internal decomposition: the parts, how they fit,
   how they implement the external promise.
6. **Runtime view (scenarios)** — behavior over time in concrete scenarios (the main flow + the important edge /
   interaction cases).
7. **Data design** — the key data structures/types: their shape, meaning, ownership, lifetime.
8. **Crosscutting concepts** — recurring concerns: error/edge handling, performance, determinism, the standing
   principles the component embodies.
9. **Architecture decisions** — each significant decision with its **alternatives** and **rationale** (why this,
   not that). The audit trail.
10. **Quality & testing** — the quality goals (correctness, performance, …) and **how it is tested** (unit /
    property / fixture / corpus / coverage / safety gates).
11. **Risks & technical debt** — known limitations, deferred work, open tunables, and the gated/future steps.
12. **Glossary** — every domain + technical term defined once (key/mode, slice, emission, Viterbi, directional, …).
13. **Background** — what this layer replaces, and corrections on record (history kept out of §1–§12; *not* needed
    to understand the layer).
14. **Related work & external sources** — what we **borrowed / built on**, what we **considered and discarded or
    deferred**, and the **corpora/datasets** used — each with the reason. The project's aim is to be the **best
    inferrer it can be**, so we survey the field and adopt the best ideas (and say plainly which we rejected and
    why). List concrete citations (paper/algorithm/dataset) so a reader knows the lineage.

*(N/A for our modules: arc42 §7 Deployment view; §"Human-interface design" — backend analysis modules, no
deployment topology or UI. Stated once per doc.)*

## Status-banner convention
Each doc opens with a one-line status: **DRAFT for sign-off** / **SIGNED (date)** / **AS-BUILT (date + commits)** /
**SUPERSEDED (→ pointer)**. The all-documentation-in-sync standing rule applies: when the code or a decision
changes, the doc moves with it.

## Implementation & test references (a *locator*, which stays — distinct from code-in-prose, which does not)
A spec carries a **locator**: which files hold the implementation and which hold the tests, so a reader can go
straight from the architecture to the code and to the tests that protect it. The locator **stays** (user, 2026-06-24).
What is *not* allowed is code **mechanics** doing explanatory work in the prose — function/type/variable names used to
*explain the algorithm*, code formulas, or commit hashes woven into the reasoning. The line: the algorithm is
described in plain architect/music-theory language; the *pointer to where it lives* is a short, clearly-marked
reference, not prose.
- **Implementation locator** — the headers and `.cpp` files — in Section 3 (Context & scope), as a labelled pointer.
- **Test locator** — the unit-test file(s) and any corpus/property validation tool — in Section 10 (Quality &
  testing).
(Deferred for layers not yet built; added when they are. A layer mid-rebuild names its current location, marked as
such. User mandate 2026-06-22, refined 2026-06-24.)

**The locator's FORM: cite by function or by section anchor, never by a raw line number** (ruled 2026-07-02;
homed here 2026-08-02 from `STATUS_ARCHIVE.md`, `OPEN_ITEMS.md` OI-272 — this is the writing standards' one
home, and the locator rule above stated no constraint on the locator's shape). A specification points at
`ParsedChord::parse()` or at `§4.3 The bridge inventory`, not at `chordlist.cpp:993`. *Why:* measured — the
gap analysis of 2026-07-02 found stale line-number citations across the layer specifications, because a line
number rots the moment anything above it changes, and the rule was made a policy at the same ruling that
repaired them. Ratified by Cowork, not by the user. The rule governs the *locator*; quoting a specific line
in a finding or a register entry, where the anchor is checked mechanically, is a different act and is
unaffected.
