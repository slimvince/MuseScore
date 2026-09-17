# CC instruction — implementation ↔ spec GAP ANALYSIS (read-only) + the five review riders

> **✅ RE-DISPATCHED AS V2 (Cowork, 2026-07-02, post-consolidation — user: "this time properly").** The v1 run
> (`cc_gap_analysis_report.md`) was ratified but its FRAME had two blind spots the user called out: (a) it audited
> code↔spec faithfulness only — a spec that *itself* under-specifies an architecture obligation scored N/A
> ("deferred-by-design"), which is exactly how the temporal-extension holes hid; (b) its scope was the 7 listed layer
> specs — the cross-layer `cowork_bounded_context_design.md` (DRAFT, unsigned, already carrying the extension
> protocol) was not on the list and went unaudited. V2 adds two dimensions and widens scope. **Baseline supersedes
> the v1 stanza:** HEAD = your `git rev-parse HEAD` (post-E0-arc); reuse the v1 report — do NOT re-derive its
> still-valid rows; v2 DELTAS only, plus the new dimensions in full.
>
> **V2 Dimension A — spec-completeness vs the architecture contracts.** For EACH §2.15 contract (finest-grain;
> style-only-in-calibration; forward-override + the confidence contract; span typology; verifiability; **bounded
> context/extension**; single-responsibility/minimality) × EACH layer spec (L1, L1.5, L2, L3, L4, L5, L6,
> Vocabulary): does the spec state the layer's obligation under that contract — with the WHEN/HOW qualified (a rule,
> an owner, a trigger), not a bare deferral? A bare deferral (no trigger/owner) = a **COMPLETENESS-GAP** row (the
> class v1 structurally excluded). Verify `cowork_bounded_context_design.md` §10's "propagation done" claims per
> layer at BOTH spec and code.
>
> **V2 Dimension B — the doc inventory + reference-integrity audit (the anti-sprawl sweep).** Enumerate EVERY
> `cowork_*.md` + `docs/*.md` (+ ARCHITECTURE/STATUS/CLAUDE/BUILD_AND_TEST): classify each {canonical / satellite-
> contract / design-record / report / TOMBSTONE / **DUPLICATE-or-FOLD-CANDIDATE**}; verify every cross-reference
> resolves (tombstones: `cowork_temporal_extension_contract.md`, `cowork_engage_criteria.md` — flag any inbound
> reference that should be re-pointed, incl. in code comments); deliver a ranked kill/merge candidate list with a
> one-line rationale each. The 2026-07-02 consolidation rulings to honor: extension spec home =
> `cowork_bounded_context_design.md`; engage criteria home = the roadmap; confidence contract = KEPT as the one
> §2.15-satellite (report inbound references, do not propose its fold unless you find real duplication).
>
> **V2 report:** `cc_gap_analysis_v2_report.md` (HELD, line count at end): §A the completeness matrix (contracts ×
> layers, gaps qualified), §B the inventory + kill/merge list + broken references, §C deltas to the v1 tables (rows
> that changed since — the carry-fixes, the L5 §5.0 pin, the L6 amendments), §D Unknowns. Read-only, no commit, no
> file modified but the report. All v1 stop conditions apply.

> **✅ DISPATCHED (Cowork revalidation note, 2026-07-02, post-E0″).** Revalidated against the session-21d state.
> The E0-arc updates that bind this run:
> - **Current state supersedes the stanza below:** HEAD carries the E0-arc commits (`f8768e6b41`, `60392a7df8`,
>   `4b3d054d89`, `0a88747e7f`, `3aaa2cbd63`, `5f7cb7376e` — all local, unpushed); suites composing **998** /
>   notation 53 (4 skipped) / snapshots 11/11; gate 53/24/53 unchanged. Quote your own `git rev-parse HEAD`.
> - **Known findings — do NOT re-discover as new; mark as CLOSED/KNOWN rows in the gap tables:** the L4→L5
>   projection drop (FIXED `4b3d054d89`); the resolver bare-reconstruction (FIXED `3aaa2cbd63` — `candidateFromProg`
>   retired); D-L5a (CLOSED `0a88747e7f`); the E0″ EXACT-cap decomposition (L4 NCT over-emission ~45% +
>   bass/inversion ~42% — known inference residuals, not new gaps).
> - **Rider 3 is PARTIALLY answered** (your own Task-2 STOP analysis verified the two §8 sites: F-B =
>   `s.confidence.composite` vs plausibility-diff; F-A = `homeKeyConfidence` vs `cadentialWeight`). The remaining
>   Rider-3 work: find any OTHER `forwardoverride`/`tryOverride` consumers, and complete the Rider-6 inventory
>   (now including `combinedBoundary`).
> - **NEW Rider 7 — the SYSTEMATIC PROJECTION SWEEP (the E0-arc lesson: two carry gaps of one class found by
>   accident in two days).** Enumerate EVERY projection/marshalling site in the rebuilt spine — inter-layer (L1→L2
>   eligibility read, L2→L3 slice feed, L3→L4 key feed, L4→L5 carry, L5→L6 `FunctionLayerOutput`) AND intra-layer
>   (the resolver substrates, the cadence event views, the modulation detector inputs, the output assembly). For
>   each: one table row — source struct's fields vs projected fields; every DROPPED field; whether ANY spec §-rule
>   consumes or could consume a dropped field (the carry-gap class); verdict (harmless-drop / known-fixed /
>   CANDIDATE-GAP). This is the systematic closure of the class; file:line per row.

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
>
> **Dispatch state: READY — dispatch after the user ratifies `cowork_confidence_contract.md` (A-1) and
> `cowork_engage_criteria.md` (A-2)**, because Rider 3/6 verify against the A-1 contract's tables.
>
> **Current state:** branch `master`; HEAD carries local unpushed commits (take the exact SHA from your own
> `git rev-parse HEAD` and quote it in the report). Gate baseline: BIR case-identity **Baroque 53 / Jazz 24 /
> Default 53** (CLAUDE.md sets). Suites at last session: composing 974, notation 53 (4 skipped), pipeline_snapshot
> 11/11. **This run is READ-ONLY: no production edit, no golden refresh, no corpus regen, NO COMMIT** (exception §6).
>
> **Bash rules (mandatory, every command):** append `; echo "exit:$?"`; never let one call produce large output —
> redirect to a file and `head` it. Build via PowerShell `Start-Process` only if a build is genuinely needed (it
> should NOT be — this is a source + test audit; the suites may be run from the existing binaries).

## 0. Purpose

The external architecture review (`cowork_architecture_review_2026_07.md`, amendments ratified 2026-07-02) cleared
the architecture at the spec level. This run establishes the **implementation ↔ spec gap table**: for every rule in
the signed layer specs, where it is implemented, whether it deviates, and whether it is tested — plus five targeted
source-verification riders the review flagged. **Classify; do not fix.** Every gap gets one of three verdicts:
`SPEC-RIGHT/CODE-GAP` (code must change, later), `CODE-RIGHT/SPEC-STALE` (doc must change, later), or `UNDECIDABLE`
(needs a Cowork/user ruling — state the question precisely).

## 1. Scope — the specs to audit (each §-by-§ against source)

| Layer | Spec | Primary as-built modules (verify, don't assume) |
|---|---|---|
| L1 | `cowork_layer1_note_model_design.md` | `analysis/notemodel/note_model.{h,cpp}`, `engravingbridge` views |
| L1.5 | `cowork_phrase_boundary_design.md` (+ spelling view per L4 §G4/C1) | `engravingbridge/phraseboundaryview.{h,cpp}`, `engravingbridge` spelling/`lineOfFifths` |
| L2 | `cowork_layer2_slicing_design.md` | `analysis/slicing/slicer.{h,cpp}` |
| L3 | `cowork_layer3_keymode_design.md` | `analysis/key/keymodesequence.{h,cpp}` + the `regionanalyzer.cpp` wiring seam |
| L4 | `cowork_layer4_chordsymbol_design.md` | `analysis/chord/chordslicedecoder.{h,cpp}` |
| L5 | `cowork_layer5_function_design.md` | `analysis/function/*` (progression, RN, cadence, resolver, forwardoverride, modulation, relational label, output) + reused `tonicizationlabeler`, `localmodulationdetector` |
| Vocabulary | `cowork_progression_schema_dictionary.md` | `analysis/vocabulary/harmonicvocabulary.{h,cpp}` |

For each spec: walk §4/§5 (solution strategy + building-block rules) rule by rule; also check §7 (data design) field
by field and §15/§9 decisions that claim "as-built". Produce one gap-table row per rule: *(spec §, rule, code site
[file:line], status: FAITHFUL / DEVIATION / MISSING / EXTRA-BEHAVIOR-NOT-IN-SPEC, tested? [test name or NONE],
verdict, note)*. "EXTRA" rows matter: behavior the code has that no spec licenses is drift too.

## 2. The five review riders (verify at source, report with file:line evidence)

1. **No production back-edge anywhere in the rebuilt spine.** For L2→L3→L4→L5(→L6 n/a): verify no module calls back
   into an earlier layer's *decision* function (data-supply calls down to L1 are legal; the §8 forward recompute must
   be forward + re-entrancy-guarded). Evidence: include graph + call sites of `forwardRecompute`/`OnePassClosure`.
2. **The L4→L5 carried-readings contract.** Verify at source: `alternatives` + `confidenceModel` populated on EVERY
   decision (Commit/Inherit/Abstain), all six `AmbiguityKind` values reachable via `nameOpenQuestion`, the topK cap
   and spelling-pinned-sibling exclusion as documented (L4 §15-O1b), and the lock-in test that pins the carry.
3. **The §8 override sites' actual confidence scales (A-1 evidence).** For each site that compares a contradiction
   strength against an earlier confidence (the §5.4 modulation recompute; the §5.5 case-4 fine-grain override; any
   other caller of the `forwardoverride` mechanism): report the EXACT quantities compared (variable, formula, range)
   and whether a squash to [0,1] happens at the boundary. This confirms or corrects `cowork_confidence_contract.md`
   §3/§4/§7 (deltas D-L5a, D-L3a).
4. **The three cadence implementations' call graphs.** `sectioncadencedetection::detectCadences`/`detectPivotChords`
   (legacy), `cadencekeyanchor` (instrument), `function/functioncadence` (L5): who calls each (production / tools /
   tests), with file:line. This grounds the retirement map rows R2/R3 (`cowork_engage_criteria.md` §4).
5. **B-swap readiness (producer-agnostic seams).** Verify the claims: the L4 decoder's `decideSlice` is
   scorer-independent; the L5 units are producer-agnostic / hand-injectable (report §7 claims); the Vocabulary's
   consumers query it without back-references. Name any seam where a hand-built scorer is structurally entangled
   (i.e. a learned emission could NOT drop in without restructuring).

## 3. Rider 6 — the confidence inventory (feeds the A-1 contract's D-INV close-out)

For every boundary confidence in `cowork_confidence_contract.md` §3: the exact as-built formula, its range on real
inputs, where it is squashed (or not), and every consumer that reads it. Include: L3 sequence margin + the C1
emission `normalizedConfidence` (BOTH — the D-L3a two-numbers question), L4 `SliceConfidence.composite` and its three
components, L5 `FunctionConfidence.combined` and its components, the cadence vote weight, the phrase-boundary
strength normalization, and the legacy `normalizedConfidence` sentinels. Table form, file:line per row.

## 4. Method + suites

- Source reads via your normal tools; quote file:line for every claim (never from memory — CLAUDE.md rule).
- Run the three suites from existing binaries to pin the green baseline for the report (composing, notation,
  pipeline_snapshot; output redirected per the bash rules). **No corpus regen** (not needed; nothing changes).
- Where a spec rule is only exercised via a dormant/diagnostic path, say so — dormancy is a property, not a gap.

## 5. Deliverable

`cc_gap_analysis_report.md` with: §1 per-layer gap tables; §2 the five riders (evidence-first); §3 the confidence
inventory; §4 a ranked summary — the top-10 gaps by severity with your suggested verdict each; §5 Unknowns (anything
you could not verify, stated as such — never guessed). End the report with its line count as an end-marker.

## 6. Stop conditions / boundaries

- **Any production back-edge found (Rider 1) = finding of the highest severity** — report precisely, do NOT fix.
- Any suite not green at baseline = STOP, report before proceeding.
- **No file may be modified.** Exception: if the report itself reveals nothing else, the single permitted write is
  the report file. NO commit of any kind this run.
- If a spec and its own §13/§15 as-built notes contradict each other, that is an `UNDECIDABLE` row — surface it.

**On your report: Cowork will re-read this instruction first, then the report in full, and verify the load-bearing
claims against committed objects before any verdict is ratified.**
