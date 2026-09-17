# CC instruction ADDENDUM — grammar-completion ripple: the Cowork ruling (2026-07-03)

> **DISPATCH note (Cowork, 2026-07-03): ACTIVE — the ruling on your STOP (`cc_grammar_completion_report.md`).
> Executes together with the base instruction; the base instruction's Task 1/Task 2 work stands as built.**
> Cowork verified at source before ruling: the two uniqueness branches and the fall-through order
> (`functionresolver.cpp`, the TransitionVsContinuation / ShareTone cases → prevailing-match arm → §5.7
> `tieBreakOrOpen`), the licensing deltas of the cited fixtures (Am6→G = Δ10; C→G = Δ7 — both now licensed), and the
> production-dormancy include chain claim. Your class-(a)/(b) split and your STOP were both correct. The dispatch's
> coupling-map omission was a **Cowork instruction defect** (the D5 map governs the catalog↔grammar coupling only;
> in-layer consumers of the grammar are ordinary same-layer callers my instruction failed to enumerate) — owned,
> recorded in STATUS.

## The ruling (grounded in the signed spec, not fiat)

**No resolver/sibling-module production code changes. The new both-licensed outcomes are the spec's own
firewall-era behaviour, not a regression to bless:** L5 §5.0 states *"the numeric preference among licensed readings
is a precision-phase weight; the licensing itself is the rule here."* The §5.5 rules select by the progression test
**only where it separates**; where the completed grammar licenses both readings, the case falls to the structural
tie-breaks and the honest open mark. The pre-amendment resolutions rested on motions being *absent from an
incomplete grammar* — artifacts, not evidence. The preference-order-among-licensed-motions remedy you flagged is
exactly §5.0's named precision-phase lever: it is **deferred to Stage-5 weight fitting**, now recorded as **L5 §15
item 13** (the spec also gained a §5.5 "both-licensed case" note — both already written by Cowork, in your docs-rider
batch). Do not implement any preference order in this increment.

## Task A — class (a): the 2 FunctionOutput fit tests (mechanical re-point)

Re-point each fixture's "unlicensed example" at a motion that is **still unlicensed under the completed grammar**
(e.g. an ascending third, Δ3/Δ4, or Δ6 into a non-diminished arrival — your choice; state the chosen motion and its
delta in the test comment, with a one-line note that the fixture was re-pointed at the §15-12 completion because the
old example, the ascending fifth, is now licensed). The tests' subjects (fit = 0 for unlicensed motion; the boundary
squash's pinned monotonicity sweep) are preserved unchanged.

## Task B — class (b): the 4 FunctionResolver tests (subject-preserving re-pick + new both-licensed pins)

No production code edits. Two sub-cases by test subject:

1. **The two disambiguation-subject tests** (`ShareTone_ResolvedByLicensedProgressionIntoNext`,
   `Transition_ResolvedAsArrivingFunction`): **re-pick the fixtures** so exactly ONE competing reading forms a
   licensed motion into the next function under the completed grammar (state both deltas in the comment) — the
   unique-licensing arm they demonstrate still exists and stays covered. **Additionally add two NEW tests** pinning
   the both-licensed arm explicitly (use the old fixtures, which are now both-licensed by construction):
   - ShareTone, both licensed, no bass-prior split → **open mark** (resolved=false, openMark=true, basis None);
   - Transition, both licensed, one reading matching the prevailing harmony → **that reading via NeighbourHarmony**
     (the passing-within-prevailing arm), confidence 0.5 as coded.
   Comment each with the citation: L5 §5.5 "both-licensed case" note + §15-13 (the deferred preference lever) — these
   pins are the firewall-era semantics and are expected to be **deliberately revisited** when Stage-5 fits the
   preference weight.
2. **The two extension tests** (`L5EXT2_CutAbstain_RequestFiresAndResolves`,
   `L5EXT5_ForwardExtension_DoesNotReopenClosedDecision`): their subject is the **extension mechanics**, not the
   disambiguation — the share-tone fixture was only the vehicle. Re-pick the vehicle to a still-uniquely-licensed
   pair so the capability each demonstrates (the cut-abstain request fires AND resolves; a closed decision is not
   reopened by a forward extension) is preserved as a *resolving* case. State old→new fixture in the report.

## Task C — one clarifying comment line (the coupling-map correction, at the owner)

In the `functionprogression.h` dependency-map block, add one line: the D5 map's "only coupling" statement governs
the **catalog↔grammar** relationship; the in-layer consumers (`functionresolver`, `functionoutput`,
`functioncadence`) are ordinary same-layer callers of the grammar, expected to move with it. Mirror nothing into
`harmonicvocabulary.h` (its side of the map is unchanged).

## Acceptance (supersedes the base instruction's item 3)

1. Full `composing_tests` green (no skips, no vestigial fixtures) + `notation_tests` green; **no snapshot refresh**.
2. The 3-preset gate regen run and proven **53/24/53 byte-identical (exact sets)** — the architectural dormancy
   argument is accepted but the measurement is still required.
3. Dormancy re-proven (no new production call site).
4. Commit: the code commit (grammar + tests + the Task-C comment), then the `docs(cowork):` commit per the base
   instruction's rider — which now also carries the L5 §5.5 both-licensed note, L5 §15-13, the STATUS session-22b
   entry, and this addendum + your report.
5. Report update (`cc_grammar_completion_report.md` §5 or an appendix): fixtures old→new with deltas, the two new
   both-licensed pins, reuse-vs-new unchanged, what retires unchanged (nothing beyond the knownGaps list).
