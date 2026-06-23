# Design-Document Standard Template (the structure every layer/component design doc follows)

> **Standing convention (user, 2026-06-22):** every architecture/design document in this project follows the
> section structure below — a synthesis of **arc42** (the 12-section architecture template) and **IEEE 1016**
> (Software Design Descriptions) + the viewpoints idea of **ISO/IEC/IEEE 42010**. Two arc42 sections —
> **Deployment view** and **Human-interface design** — are **N/A** for our backend analysis modules (no separate
> hardware/runtime deployment; no UI); each doc states that omission once rather than padding.
>
> Sources: arc42.org/overview · IEEE 1016 (standards.ieee.org/ieee/1016) · ISO/IEC/IEEE 42010.

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

## Implementation & test references (once the source code is stable)
Once a layer's source code has stabilized, the doc names both:
- its **implementation files (headers and `.cpp`)** — in Section 3 (Context & scope), and
- its **regression tests** (the unit-test file(s) and any corpus/property validation tool) — in Section 10
  (Quality & testing),
so a reader can go straight from the architecture to the code *and* to the tests that protect it. (Deferred for
layers not yet built; added when they are. User mandate 2026-06-22.)
