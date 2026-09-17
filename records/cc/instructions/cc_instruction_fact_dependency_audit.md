# CC instruction — whole-graph fact-dependency audit (READ-ONLY; establish acyclicity before the key-layer build)

**Dispatch author:** Cowork, 2026-07-13, at the user's direction. **Type:** a READ-ONLY analysis — the
first stage of the #17 funnel. **No build, no `src/` edit, no golden refresh, no register/design re-scope,
no corpus/report write beyond the audit report.** This is not coding. The single deliverable is a
code-grounded fact-dependency graph + proposed layer placements, for a later design pass and the user's
ratification.

**Why this exists (the premise under test).** Before the key layer is built, the user wants to be convinced
that our producer→consumer fact graph is **acyclic and correctly layer-assigned** — that the feed-forward
through layers actually holds for every fact the key layer will consume. The evidence inventory
(`cowork_evidence_inventory.md` §8) argues all alleged circles break ("one side is fixed input, or a
key-agnostic form of the detector exists"). That argument is sound as **THEORY but is not established
against the realized code**: the clearest case — the cadence→key channel — has its detector physically in
L5 (`functioncadence.cpp`, consumed today only by L6 `groupinglayer`), so a key layer consuming it
as-placed would be a real upward L3←L5 edge, closing the L3→L5→L3 loop. Under #18 (no design carries load on
an unverified causal claim about our own system), #19 (a premise is trusted only after positive
establishment), and #13 (surface a surprise as a STOP before building around it), the §8 map must be turned
from prose into an established, code-cited graph before any key-layer build opens.

**Scope: the WHOLE graph** — every layer, every produced/consumed fact, not just the key layer's set (the
user's explicit choice: re-establish the full §8 map).

Read first: `CLAUDE.md`, `OPEN_ITEMS.md`, then the grounding set — `ARCHITECTURE.md` (the layer specs +
order), `cowork_evidence_inventory.md` (§8 map + the per-layer produced/consumed lists),
`cowork_key_layer_design_opening.md` (what the key layer intends to consume),
`docs/implementation_roadmap.md` (layers/retirements), and the code.

---

## 1. Governing constraints

Read-only throughout. Apply the Premise Gate (#17): write the §7 predictions BEFORE deriving the graph;
verify every producer/consumer edge **at the code** (the actual reads/writes), never from the design prose
or the register summary or memory; label every edge and every "break" claim **FACT** (code citation),
**THEORY** (design/roadmap citation), or **ASSUMPTION**. No self-invented labels — use the layer names,
fact names, OI-N, retirement names, and principle numbers already in the repository; where a fact has no
name, describe it plainly.

**Be adversarial — try to BREAK acyclicity, do not rubber-stamp §8.** The value of this pass is only real if
it would actually find a true cycle. For each alleged break, attempt to falsify it at the code (#15 —
verify at the objects on the full surface; #19 — established, not merely unfalsified). A break you cannot
confirm realizable is a STOP, not an assumption.

---

## 2. Task 1 — the canonical layer order

From `ARCHITECTURE.md` and the roadmap, state the total layer order used to define "upward" (input/DOM →
L1 index/primitives → L1.5/L2 engraving-bridge/segmentation/metric-weights → L3 key/mode → L4 chord decoder
→ L5 function → L6 grouping — confirm this at the specs, correct it if wrong). Note explicitly whether the
architecture intends a strictly forward feed, and where (if anywhere) a deliberate re-request/bounded-context
loop is specified — that is a designed control-flow loop, distinct from a fact-dependency cycle, and must
not be conflated with one.

## 3. Task 2 — per-layer produced/consumed facts, FROM THE CODE

For each layer, enumerate the facts it PRODUCES (writes to its output surface) and CONSUMES (reads from a
lower layer), derived from the actual code (what each module reads and emits), and cross-checked against the
§8 per-layer lists. Record every discrepancy between the code and the evidence inventory as a proposed
correction (the inventory may be stale or aspirational). Cover the full set the inventory names — cadence
votes + leading-tone events, notated spelling/signatures/accidentals, harmonic rhythm + boundary strength,
NCT-cleaned tone collections, progression grammaticality, the collection/tonic split, beat strength,
fermatas/phrase facts, bass-motion skeletons — plus anything the code produces that the inventory omits.

## 4. Task 3 — build the directed fact graph; flag every upward edge

Build the graph: each fact is an edge from its producer layer to each consumer layer. Mark every edge's
direction against the Task-1 order. Flag as a candidate cycle every **upward edge** (a consumer in a lower
layer than the producer). Include BOTH:
- **current** upward edges in the code (e.g. does anything already reach up?), and
- **planned** upward edges — every fact `cowork_key_layer_design_opening.md` intends the key layer to
  consume that is produced above it (the cadence vote is the known one; find the rest — progression
  grammaticality, leading-tone events, harmonic rhythm, boundary strength, etc.).

## 5. Task 4 — for each upward edge, test the break AND propose the owning layer

For every upward/cyclic edge, apply the §8 break test AT THE CODE and record the result:
- **Is one side a fixed input?** (spelling, signatures, fermatas, annotations enter once, not inferred.)
- **Is a key-agnostic (or lower-layer-agnostic) FORM of the detector realizable?** For the cadence vote:
  confirm at `functioncadence.cpp` whether the detection actually needs key/mode, or only chord
  roots/qualities/voice-leading/metric position (the "key-agnostic tonic-voting machinery" the inventory
  claims). Distinguish **detection** (the cadential motion / leading-tone resolution / bass arrival —
  key-agnostic) from **interpretation** (this arrival is the home tonic vs a tonicization vs a modulation —
  key-dependent).
- **PROPOSE the owning layer** (the user's explicit request): for each relocatable detector — cadence
  especially, and progression-grammar, leading-tone, and any other upward-edge producer — name the layer at
  or below its consumer where the key-agnostic form should live so the consumption is strictly forward, with
  the reasoning. Present this as ONE candidate for the later design pass, not a decision — flag the
  trade-offs (e.g. does relocating cadence detection to a low layer duplicate any chord-layer work; does the
  key-agnostic vote lose any precision the key-dependent form had).

## 6. Task 5 — reconcile the §8 map; STOP on any true cycle

Walk the five §8 circles (key↔spelling, key↔cadence, key↔chord/provisional-refine, key↔NCT,
key↔progression-grammar) and, for each, state whether it is still broken **given the realized code** and by
which mechanism, with citations — upgrading each from THEORY to FACT where the code bears it out, or
flagging where it does not. Then, adversarially, look for any upward edge the §8 map did NOT enumerate (a
sixth circle). **STOP-and-report** any fact whose break is not realizable — a place the feed-forward
genuinely does not hold — with the evidence; that is a real architectural finding, exactly what this pass
exists to surface, not something to assume away.

---

## 7. Premise Gate — predictions to write BEFORE deriving the graph (#17b)

Record first: how many upward edges you expect to find (current vs planned); which §8 circles you expect to
confirm broken vs find shaky at the code; whether you expect any sixth, un-enumerated cycle; and your prior
on the cadence detector's proper layer. A large gap between prediction and finding is itself diagnostic
(#3). No prediction, no derivation.

## 8. Deliverable — a proposal, not a decision

- **A report `cc_fact_dependency_audit_report.md`**: the Task-1 layer order; the Task-2 per-layer
  produced/consumed tables (code-cited, discrepancies vs §8 noted); the Task-3 directed graph with every
  upward edge flagged (current + planned); the Task-4 per-edge break test + **proposed owning layers** (with
  trade-offs); the Task-5 reconciled §8 map (each circle FACT/THEORY, with the mechanism) and any STOP.
- **Everything is a PROPOSAL.** Do not edit `ARCHITECTURE.md`, the evidence inventory, the design opening, or
  any register row's scope; do not open any build. Where the code contradicts the evidence inventory or a
  layer spec, record a **proposed correction with evidence** — the user and the design pass ratify.
- **Commit:** the report as a `docs(cc)` fold + a `STATUS.md`/`cowork_handoff.md` note that the fact graph is
  under establishment and the key-layer funnel does not open until it is ratified. Force-add this
  instruction file. Nothing else is written.

**On completion:** we have a code-established, acyclic (or honestly-not-acyclic) fact-dependency graph and a
candidate layer placement for the cadence detector and any other relocatable producer — the thing the user
wants to be convinced of before building. The next step is a design pass (with CC's proposed placements as
one input among several) that ratifies the layer assignment; only then does the key-layer funnel open.
