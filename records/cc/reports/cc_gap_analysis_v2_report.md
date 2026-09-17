# CC gap-analysis report v2 — spec-completeness vs the §2.15 contracts + doc inventory

> **Run type:** READ-ONLY audit. No production edit, no golden refresh, no corpus regen, no commit. Only file written = this report.
> **Instruction:** the V2 re-dispatch (2026-07-02, "this time properly") of `cc_instruction_gap_analysis_spec_vs_impl.md`.
> **HEAD:** `246e4542e87e08072700ab158fe60c38008c7649` (branch `master`, local/unpushed). This is **2 commits ahead of
> the v1 report's HEAD** `5f7cb7376e`; both intervening commits (`2e378c6ec7` registry v2, `246e4542e8` DLC baseline
> driver) touch **`tools/` only** — ✔CC `git diff --name-only 5f7cb7376e 246e4542e8 | grep -v ^tools/` is EMPTY. Zero
> spec/source change since v1.
> **Baseline (existing binaries, this run):** composing **998/998 PASSED** (2 disabled); notation **53/53 PASSED**
> (57 total, 4 skipped); pipeline_snapshot **11/11 PASSED** (1 skipped). All green — identical to v1. ✔CC
> **Gate:** BIR case-identity Baroque 53 / Jazz 24 / Default 53 (unchanged; not re-measured — nothing changed).
>
> **What v2 adds over v1.** v1 audited code↔spec **faithfulness** (is each spec rule implemented?). It had two blind
> spots the user named: (a) a spec that itself *under-specifies* an architecture obligation scored N/A, so
> completeness holes hid; (b) scope was the 7 layer specs — the cross-layer `cowork_bounded_context_design.md` went
> unaudited. **v2 = two NEW dimensions in full + deltas to v1.** §A = spec↔**contract** completeness (7 §2.15
> contracts × 8 layer specs, gaps qualified) + the bounded_context §10 propagation verified at spec AND code. §B =
> the full doc inventory + reference-integrity + kill/merge list. §C = deltas to v1's tables. §D = Unknowns.
> **v1's §1 faithfulness tables, §2 riders, §3 confidence inventory carry forward VERBATIM** (nothing changed) — this
> report does NOT re-derive them; read v1 for them.
>
> **Method.** Each layer spec walked §-by-§ for completeness against the 7 contracts by a dedicated read-only auditor;
> every cell carries a §-cite + short quote. Load-bearing contrasts re-verified by CC at source (marked ✔CC). Bounded
> context §10 verified at BOTH spec and code with file:line. The 7 contracts are quoted verbatim from ARCHITECTURE.md
> §2.15 (lines 496–564).

---

## §A. The completeness matrix (7 §2.15 contracts × 8 layer specs)

**The seven contracts.** C1 **finest-grain** (atomic unit = constant-sonority slice; coarser things are derived
views). C2 **style-only-in-calibration** (fact layers carry no style; style only as priors/weights in judgment
layers, never structure). C3 **forward-override + confidence contract** (confident inference overturnable by a
localized forward recompute; boundary confidences [0,1], class-declared M/P, compared only in declared frames). C4
**span typology** ("region" unqualified banned; every layer names its span). C5 **verifiability** (prefer
GT-verifiable; unverifiable theory gets an alternative-confidence path + "empirically-unvalidated" mark). C6
**bounded context** (selection-based; append-only extension request from L1 with stop condition + hard bound;
whole-score = degenerate). C7 **single-responsibility/minimality + maximal info** (one evidence×question, states
non-ownership, defers as ranked alternatives + uncertain mark, uses all lossless L1 info).

Verdict legend: **STATED** = obligation stated with WHEN/HOW (rule/owner/trigger). **STATED‑∅** = stated *as an
absence* (e.g. "carries no style", "publishes no confidence") — a legitimate obligation, not a gap. **PARTIAL** =
concept present but a required qualifier missing. **GAP** = COMPLETENESS-GAP (bare deferral / concept present but no
trigger/owner). **ABSENT** = not addressed at all.

| Spec | C1 finest-grain | C2 style-calib | C3 conf/override | C4 span-typology | C5 verifiability | C6 bounded-ctx | C7 single-resp |
|---|---|---|---|---|---|---|---|
| **L1** note_model | STATED | STATED‑∅ | STATED‑∅ | **PARTIAL** | PARTIAL | STATED | STATED |
| **L1.5** phrase_boundary | STATED | STATED‑∅ | **PARTIAL** | **PARTIAL** | STATED | **ABSENT** | STATED |
| **L2** slicing | STATED | STATED‑∅ | STATED‑∅ | **PARTIAL** | STATED | STATED | STATED |
| **L3** keymode | STATED | STATED | STATED* | **PARTIAL** | STATED | STATED | STATED |
| **L4** chordsymbol | STATED | STATED | STATED* | **PARTIAL** | STATED | STATED (code UNCODED) | STATED |
| **L5** function | STATED | STATED | STATED | **STATED** | STATED | STATED (code UNCODED) | STATED |
| **L6** grouping | STATED | **PARTIAL** | STATED | **STATED** | STATED | STATED | STATED |
| **Vocab** dictionary | STATED | STATED | STATED‑∅ | **PARTIAL** | STATED | STATED‑∅ | STATED |

`*` = STATED in body but the confidence-contract **boundary squash to [0,1]** is delegated to
`cowork_confidence_contract.md`, not stated as an in-body rule (L3 publishes a raw "sequence margin"; L4 a composite)
— see gap A-3.

### The qualified completeness gaps (the non-STATED cells, ranked)

**A-1 — C4 span-typology vocabulary gap (the dominant cluster; 6 of 8 specs).** L1, L1.5, L2, L3, L4, and Vocab each
name the span they operate on/emit **in local terms** but never adopt the §2.15 typology vocabulary for it: L2/L1
say "slice"/"span of time" but never equate it to the typology's **harmonic region**; **L3 never coins "key-span"**
for its emitted span (✔CC — `grep key-span cowork_layer3_keymode_design.md` = 0 hits); **L4 never labels its emitted
span "harmonic region"** (✔CC — only appears in a disclaimer about L6's punctuation-span); Vocab defines its own
local "span" (a run of committed chords) unlinked to the family. **The two NEWEST specs, L5 (§5.0) and L6 (§0), DO
adopt it in full** — L5 §5.0 names key-span / decision-context span / punctuation-span and explicitly disambiguates
the banned bare "region" (✔CC — `cowork_layer5_function_design.md:162-181,654-656`); L6 §0 renames phrase→
punctuation-span. **Root cause:** the span-rename + typology hardened 2026-07-01/02; L1–L4/L1.5 were signed
2026-06-22..26 and predate it. **Verdict: CODE-RIGHT/SPEC-STALE** — a spec-vocabulary alignment pass on the six
older specs; concept is present everywhere, only the coined term lags. Low-moderate severity (navigation/consumer-
naming, not behavior).

**A-2 — C6 bounded-context ABSENT at L1.5 (genuine hole).** The L1.5 phrase-boundary spec **never mentions**
bounded context, extension, selection-edge, score-boundary recognition, or the degenerate case — it does not cite
`cowork_bounded_context_design.md` at all (✔CC — its only "extend" hits are "extend the primitive to any
instrumentation" and "all-voice-rest span cannot be extended", `cowork_phrase_boundary_design.md:43,119,216,283`,
none bounded-context). It consumes L1/L2 outputs, so its likely obligation is "inherits the loaded span, requests no
own extension" — but the spec must **say so**. **Verdict: SPEC-RIGHT/CODE-GAP (spec-side)** — add a one-line
bounded-context stanza to L1.5. Moderate severity. (This is a true COMPLETENESS-GAP of the class v1 excluded.)

**A-3 — C3 confidence-contract in-body under-specification (L1.5, L3, L4).** L1.5 publishes a graded [0,1] boundary
strength (§4.1 max-normalisation) but never **class-declares** it per the confidence contract (margin M vs
calibrated-probability P) nor states its participation/non-participation in override frames → PARTIAL. L3 and L4
declare their confidence and its consumption in override frames, but the **U2 boundary squash to [0,1]** the
confidence contract requires is **delegated to the contract doc**, not stated as an in-body rule — L3's body
publishes a raw unbounded "sequence margin" (§5.4). **Verdict: CODE-RIGHT/SPEC-STALE** — one cross-reference +
class-declaration line per spec; ties directly to confidence-contract **D-L3a** (already tracked) and **D-INV**.
Low-moderate severity.

**A-4 — C2 at L6 PARTIAL; C5 at L1 PARTIAL; C1 at L4/L4 span-name (minor).** L6 never positively states "no style in
structure" — it relies on being a pure assembly layer; only the §7 firewall (alignment window / codetta margin /
key-area combiner as precision-phase constants) engages C2 obliquely. L1 never states it emits **no theory** (so the
C5 alternative-confidence-path/unvalidated-mark obligation is defensibly N/A but left to the reader). Both
near-N/A, low severity — note, do not action before engage.

### Bounded-context §10 propagation — verified at BOTH spec AND code (the crown finding)

`cowork_bounded_context_design.md` §10 claims the contract was propagated "done with this design" into each layer
spec. Verified per layer:

| Layer | Spec-propagated? | Coded? | Verdict |
|---|---|---|---|
| **L1** | YES — note_model §3 "build over a selection, then extend on request; append-only; clamp… report it" | **CODED (interim)** — `note_model.h:194` `extend(Direction,int)`, `:184` `build(sc,start,end)` selection overload; interim whole-score rebuild `.cpp:123-125` (§8-conceded) | fully-done (spec+code), interim impl |
| **L2** | YES — slicing §8 "re-slice… the newly loaded region; context slices… not part of the output" | **CODED** — `slicer.h:55-64` bounded-context clip; `slicer.cpp:63-91` clip-to-loaded-span, `:413` re-slice-on-extend; tests CP1–CP7 incl. `CP7_ReSliceEquivalence` | fully-done |
| **L3** | YES — keymode §2 "This reach-back **is an extension request**… stop… hard bound" | **CODED, gated OFF** — reach-back loop `regionanalyzer.cpp:631-693`; flag `regionanalyzer.h` `enabled=false`; calls `extend(Earlier,…)` `:675` | fully-done as capability; default-OFF ⇒ production byte-identical |
| **L4** | YES — chordsymbol §2 "request an extension… or… proceeds with the truncated window" | **UNCODED** — `chordslicedecoder.cpp:197-200` silently clamps `lo/hi` to `[0,n-1]`; no L1 request; no TODO | **spec-done / code-UNCODED** (= v1 gap #5; bounded_context §5 self-concedes; §11 acceptance item) |
| **L5** | YES — function §5.0 decision-context extent PINNED (i cadence-anchored / ii punctuation boundary / iii K-slice/B-beat bound), superseding §15-3 | **UNCODED** — no extension-request code beyond L3's reach-back; the extent is a spec-level identification only | **spec-done / code-UNCODED** (bounded_context §11 lists "L5's pinned extent + discovery rule" as still-to-code) |
| **L6** | YES — grouping §5.1 amendment: `clipped-by-selection-edge` provenance + `extension-cue` tag; L6 surfaces, orchestrator acts | **dormant by design** — `:176,:343` "dormant + byte-identical until engagement" | dormant-by-design, not a gap |

**Reading:** §10's "done with this design" is **accurate as *spec* propagation for all six**, but §11's own
acceptance list is only partly met **in code**: L1/L2/L3 coded (L3 gated OFF for byte-identity), **L4 + L5 UNCODED**,
L6 dormant. The two UNCODED request paths are exactly why bounded_context is the stated **hard gate before L6**. This
is the same object as v1's ranked gap #5, now generalized: **it is two gaps (L4 *and* L5), of one class.** Highest
engage-relevance of anything in §A. Not a spec completeness gap (the specs are complete); a **build-completeness**
gap.

### Body-vs-as-built self-disclosures surfaced (not completeness gaps; §D-relevant)

- **L3 §15:** body C7 presents note-evidence ownership as complete, but §15 concedes the layer is **spelling-blind
  (pitch-class only)** and the notated-tpc (maximal-info) obligation is unbuilt and **reassigned to Layer 5**. The
  spec discloses this rather than hiding it, but body and as-built diverge on "uses *all* lossless L1 info."
- **L5 §15-3:** the §5.4 region-key-alternatives carry it selects among shipped as a deliberate **"byte-identical v1
  placeholder"** (`cowork_layer5_function_design.md:749-753`, "Do not carry the v1 placeholder past this step"); the
  §5.4 body presents the recompute's selection menu as if fully specified. Self-disclosed as-built tension.

---

## §B. Doc inventory + reference-integrity + kill/merge list

**Scope enumerated in full:** 72 `cowork_*.md` (repo root) + 48 `docs/*.md` (top-level) + 4 control docs
(ARCHITECTURE/STATUS/CLAUDE/BUILD_AND_TEST) = **124 in-scope docs**. Build-tree/`_deps`/`old_docs`/`apidocs`
markdown excluded. Classified from status banners; fold candidates confirmed by deeper reads. (Full 124-row table in
the auditor record; the material findings are below.)

**Class distribution.** Canonical/authoritative: ARCHITECTURE, STATUS, CLAUDE, BUILD_AND_TEST, the 6 signed layer
specs (L1 note_model, L2 slicing, L3 keymode, L4 chordsymbol, L5 function, L6 grouping) + L1.5 phrase_boundary,
`docs/implementation_roadmap.md` (the single stage tracker + engage-criteria home), `docs/scoring_model.md`,
`docs/score_inventory.md`, `cowork_score_census.md`, `cowork_design_doc_template.md`. **Satellite-contracts (the
§2.15 anchors):** `cowork_bounded_context_design.md` (the ONE cross-layer extension spec), `cowork_confidence_
contract.md` (the ONE §2.15 confidence satellite), `cowork_progression_schema_dictionary.md` (the Vocabulary
component). Remainder: ~40 design-records + ~45 reports/dossiers + 2 tombstones + 2 superseded drafts.

### §B2. Reference-integrity findings

**Stale inbound pointers to the two killed tombstones — 3 found (v1-auditor found 2; CC found a 3rd in code):**

| Site (file:line) | Points to | Should re-point to | ✔? |
|---|---|---|---|
| `cowork_layer6_grouping_design.md:5` (live status banner, the L6 build-gate condition) | `cowork_temporal_extension_contract.md` (KILLED) | `cowork_bounded_context_design.md` (§11 acceptance list) | ✔CC (`sed -n 5p`) |
| `cowork_confidence_contract.md:60` (§3 legacy-path row, "Retires at engage") | `cowork_engage_criteria.md` (KILLED) | `docs/implementation_roadmap.md` (ENGAGE CRITERIA block) | ✔CC (`sed -n 60p`) |
| **`tools/cc_e0_fullspine_measure.py:7`** (docstring: "per cowork_engage_criteria.md §3") | `cowork_engage_criteria.md` (KILLED) | `docs/implementation_roadmap.md` (E0 stage / retirement map) | ✔CC — **correction to the auditor**, which reported the code sweep "clean" |

All other tombstone references are **correct fold-provenance** (`docs/implementation_roadmap.md:105,110,145,151`
"KILLED into it" / "FOLDED here from") or **narrative log** (`STATUS.md:6,8,20`) — no action. **No dangling markdown
paths** found (spot-checked the most-referenced targets — all exist). **Renamed-concept straggler:** the
"phrase"→"punctuation-span" (2026-07-01) span rename is complete in L6 + ARCHITECTURE §2.15 + L5 §5.0; the retained
boundary-sense "phrase" usages (the L1.5 primitive keeps its name) are deliberate (L6 §15-7 maps them 1:1) — **not**
a defect. (The §A A-1 finding is the *typology-adoption* half of this same rename lagging in the six older specs.)

### §B3. Ranked kill/merge candidate list

| # | File | Disposition | Rationale |
|---|---|---|---|
| 1 | `cowork_temporal_extension_contract.md` | tombstone — delete next docs commit | ☠ KILLED stub; content merged into bounded_context + L5 §5.0; kept only so stale refs fail loudly |
| 2 | `cowork_engage_criteria.md` | tombstone — delete next docs commit | ☠ KILLED stub; folded into `docs/implementation_roadmap.md` |
| 3 | `cowork_layer3_analysis_design.md` | kill/archive | ⛔ SUPERSEDED 2026-06-21 "do not use"; fat-L3 model decomposed into separate L3–L6 specs (✔CC banner) |
| 4 | `cowork_layer3_keymode_incrementC_design.md` | kill/archive | ⛔ SUPERSEDED 2026-06-22, "folded into `cowork_layer3_keymode_design.md`" (✔CC banner) |
| 5 | `cowork_github_9444_comment_draft.md` | kill | Already flagged DELETE in `cowork_prune_pass_checklist.md`; SUPERSEDED—DO-NOT-POST; **distribution-constraint-sensitive** (embeds `cfc7eb5e39`) |
| 6–7 | `cowork_score_census_gt_draft.md`, `cowork_score_census_plain_draft.md` | merge → `cowork_score_census.md` | The GT + plain appendix halves of the delivered census v1 |
| 8 | `cowork_layer3_keymode_impl_design.md` | merge-candidate → L3 spec (low urgency) | Build-sequencing companion; delivery-sequencing ≠ standalone architecture |
| 9 | `cowork_target_architecture.md` | keep-but-demoted (watch) | Already ★ demoted 2026-06-29 to a rationale ref under ARCHITECTURE.md; fold candidate at a future tidy pass |
| 10 | the `cowork_audit_*` set (~15) + `cowork_audit_remaining_layers.md` | retire as a batch post-reconcile | Phase-1 per-layer second-opinion dossiers whose obligations fold into `cowork_audit_obligation_map.md`; closed by `cowork_l1l4_completion_ledger.md` (SIGN-OFF CLEAN) — historical, retire at the prune pass, not individually now |

**Anti-sprawl anchors to NOT mis-merge** (keep): the 3 satellite-contracts above, the 6 signed layer specs + L1.5,
the 4 control docs, `docs/implementation_roadmap.md`, `docs/scoring_model.md`, `docs/score_inventory.md`.

**Two doc-rider fixes worth doing (NOT done — read-only):** re-point the 3 stale pointers in §B2 (the L6 banner, the
confidence-contract §3 row, and `tools/cc_e0_fullspine_measure.py:7`).

---

## §C. Deltas to the v1 tables

**Global delta since v1's HEAD (`5f7cb7376e` → `246e4542e8`): NONE to any v1 gap-table row.** ✔CC the only two
intervening commits touch `tools/` exclusively (`2e378c6ec7` score-census registry v2; `246e4542e8` DLC baseline
driver `run_dlc_baseline.py`) — no `src/`, no spec, no test change. Therefore **v1's §1 per-layer faithfulness
tables (~132 FAITHFUL / 19 DEVIATION / 14 MISSING / 3 EXTRA), §2 seven riders, and §3 confidence inventory hold
verbatim.** Suites + gate identical to v1.

**The v2 dimensions are ADDITIVE, not corrective.** §A audits spec↔**contract** completeness — a dimension v1
structurally excluded (it scored under-specification as N/A). No v1 row reverses. The intersections:

1. **v1 ranked gap #5 (L4 "request extension" missing) → generalized in §A** to the C6 spec-done/code-UNCODED
   *class*, now covering **L4 *and* L5** (v1 named only L4; the L5 pinned-extent path is the same uncoded class,
   confirmed at code this run). This is the single most engage-relevant carry.
2. **L5 §5.0 pin + L6 2026-07-02 amendments** — already reflected in v1's L5/L6 tables; §A confirms they make **L5
   and L6 the only two fully contract-complete specs** (all 7 contracts STATED, incl. C4 typology + C6 pinned
   in-spec). The six older specs are the C4/C6/C3 completeness laggards (§A A-1/A-2/A-3).
3. **Refinement to v1's Vocabulary F-6/A-6 "two-stores" row.** v1 framed the pairwise licensed root motions as
   "delegated to `functionprogression`". The Vocab completeness read finds §5.1 states the dictionary **HOLDS** them
   ("the descending fifth… third… ascending second") rather than delegating — so the open question is **potential
   duplication** (held here AND in functionprogression?), not delegation. Minor sharpening of the v1 UNDECIDABLE.
4. **v1 §4 stale-line-number gap (#9)** is unchanged and now has a documentation companion: §A A-1 (the six specs'
   C4 typology-term lag) is the *vocabulary* sibling of the same "older-spec doc-refresh pass owed" theme.

No new highest-severity finding this run: no back-edge (v1 Rider 1 holds — no spec/source change), no new undeclared
carry-gap (v1 Rider 7 holds). The two UNCODED request paths (A/§10) are declared build-gate items, not defects while
dormant.

---

## §D. Unknowns (stated as such — never guessed)

- **A-1 disposition (C4 typology-vocabulary lag on the six older specs).** Whether this is an *accepted* known-
  lagging vocabulary pass (the specs predate the 2026-07-01 rename; L5/L6 adopted it, the rest did not yet) or is
  **owed before engage** needs a Cowork/user ruling. It is tracked *nowhere* as a pending item that I found — that
  absence is itself the question. UNDECIDABLE.
- **A-2 (L1.5 C6 ABSENT).** Whether L1.5 is *legitimately exempt* from bounded context (a derived-view primitive
  that inherits the loaded span and requests no extension) or genuinely owes an extension behavior. Either way the
  spec should state its stance; which stance is canonical is a ruling.
- **The L4 + L5 UNCODED request paths (§A/§10).** Confirmed uncoded at source this run; whether they are built as
  part of the bounded_context §11 acceptance work *before* or *concurrent with* L6 is a sequencing decision on the
  roadmap, not something the audit can settle.
- **L3 §15 spelling-blind vs C7 maximal-info, and L5 §15-3 v1-placeholder carry** — both are spec-self-disclosed
  as-built tensions; whether the reassignment (L3 tpc → L5) and the placeholder retirement are still open or already
  closed elsewhere was not independently settled here.
- **Score-census appendix fold (§B3 #6–7)** and the `cowork_audit_*` batch retirement (#10) are housekeeping
  dispositions requiring a human call at the next docs commit, not audit conclusions.
- **Completeness of the 124-doc enumeration** — the inventory is the auditor's full sweep of `cowork_*.md` +
  `docs/*.md` + the 4 control docs; a doc outside those globs (e.g. a root research `.md` like
  `contrapunctus_findings.md`, referenced but out of the stated scope) is acknowledged as a valid target, not
  re-enumerated.

---

*End of report. Load-bearing v2 claims independently re-verified at source by CC (✔CC): span-typology adoption
contrast (L5 §5.0 names key-span/decision-context/punctuation-span & bans "region"; L3/L4 coin neither — greps);
L1.5 has no bounded-context language (grep); bounded_context §10 L4/L5 UNCODED (`chordslicedecoder.cpp:197-200`
silent clamp; no L5 extension code) + L1/L2/L3 coded with L3 gated OFF (`regionanalyzer.h enabled=false`); three
stale tombstone pointers incl. the code one `tools/cc_e0_fullspine_measure.py:7` (correction to the auditor's
"clean" claim); two superseded L3 banners; no spec/source change since v1 HEAD (`git diff`); suites green
998/53/11. No file modified except this report; no commit.*

LINE COUNT: this file is 247 lines.
