# CC Instruction — Phase 5 refactor (2 of 2): types-only header — READ-ONLY INVESTIGATION

> **Why.** The last Phase-5 structural refactor (audit Q2): extract the shared **value types** that cross layer
> boundaries into a leaf `analysis/types/` header, killing the header **back-edges** (L1.5/L3 currently `#include`
> `chord/`+`key/` headers *only* for value types). The crux: `KeyModeAnalyzer::PitchContext` is **nested**, so the
> extraction needs un-nesting + a full reference-graph chase — which is why this is an **investigation FIRST**, before
> any design or build. **READ-ONLY — no source edits, findings only.** Cowork designs the extraction from your report;
> CC then builds it.
>
> **Note (clarifying a misread):** the "never bash for reading files" rule is **Cowork's** discipline (the Linux mount
> serves stale file content), and does **NOT** constrain your normal build/test/tool execution. Run whatever you need.
> (The `batch_analyze` Qt `platforms/`-plugin issue is a separate tracked blocker, not relevant to this read-only task.)

## §1 — Inventory the cross-layer value types
For each shared type that creates a back-edge — the audit named **`ChordAnalysisTone`**, **`ChordTemporalContext`**,
**`ChordAnalyzerPreferences`** (+ `kDefaultChordAnalyzerPreferences`), **`KeyModeAnalyzer::PitchContext`** — report:
- **where defined** (file:line) and **whether nested** in a class/struct;
- **its own dependencies** — does the type's definition reference *other* layer types, engraving types, or only
  primitives/STL? (this determines whether it can live in a dependency-free leaf header);
- **every reference site** across `src/composing/` (and `tools/` + tests) — a count + the files, so the extraction's
  blast radius is known.
Also **find any OTHER types** that cross the boundary that the audit did not name (sweep the actual `#include`s — §2).

## §2 — Map the exact header back-edges to kill
Confirm, at source, each earlier-layer header that `#include`s a later-layer header **only for types**:
- `engravingbridge/regiontonecollector.h` → which `chord/`+`key/` headers, and **which types** each pull is for.
- `key/keymodeanalyzer.h` → `chord/analysisutils.h` (or others) — which types.
- Any others found in §1.
For each back-edge, list the **exact set of types** it needs — that set is what the leaf header must carry.

## §3 — The un-nesting question (the crux — be precise)
`KeyModeAnalyzer::PitchContext` is nested. To live in a leaf header it must be **un-nested** (a standalone
`PitchContext`, e.g. in a `types` namespace) with every `KeyModeAnalyzer::PitchContext` reference updated. Report:
- **how many** `KeyModeAnalyzer::PitchContext` reference sites exist (and where);
- whether `PitchContext`'s definition **depends on `KeyModeAnalyzer` internals** (nested enums/constants/typedefs) — if
  it does, un-nesting is harder; quote what it touches;
- whether the un-nest can be **byte-identical** — a pure type relocation + (optionally) a `using KeyModeAnalyzer::PitchContext = types::PitchContext;`
  alias to keep call sites compiling — with **no behaviour change**. Flag anything that isn't a pure relocation.

## §4 — Feasibility verdict + proposed leaf-header shape
- Can a leaf `analysis/types/<name>.h` (depending on **nothing** from `chord/`/`key/`) carry these types, with
  `chordanalyzer.h` / `keymodeanalyzer.h` then **`#include`-ing it** (so existing includers + tests keep compiling
  transitively, via the alias where needed), and the L1.5/L3 headers including **only** the leaf header (back-edge
  gone)? 
- Propose the **leaf header's contents** (which types move) and which headers change their includes.
- **Flag any type whose extraction is NOT byte-identical** or needs a behaviour touch → that's a STOP-class item for
  the design (we'd scope it out, not force it).

## §5 — Deliver
Write `cc_types_header_investigation_report.md` (gitignored): the §1 type inventory (def site, nested?, deps,
reference-site count+files), the §2 back-edge map (header → exact type set), the §3 `PitchContext` un-nesting
assessment, and the §4 feasibility verdict + proposed leaf-header contents. **No code changes** — this grounds the
design.

## §6 — Stops
- Any source edit (this is read-only) → STOP.
- A push targets `upstream` → STOP.
