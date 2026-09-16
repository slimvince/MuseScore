# CC instruction — the BOUNDED-CONTEXT/EXTENSION BUILD (L1–L5, the L6 gate) + the consolidated docs commit

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Also, mandatory: **`cowork_bounded_context_design.md` (SIGNED 2026-07-02) in FULL** — §3 contract, §4 protocol,
> §5 per-layer roles (incl. the merged L4 sharpening + L5 pinned extent), §8 risks, **§11 acceptance = this build's
> definition of done**; `cc_gap_analysis_v2_report.md` §A/§10 table (the spec-done/code-UNCODED evidence).
>
> **Dispatch state: ACTIVE (2026-07-02, on the signed design + the v2 report).** This is the HARD GATE before L6.
> Commits: one change-class each, local, unpushed, fork-only. **No θ, no constant tuning, no inference fixing.**
> Bash rules as always; cite by function/§ anchor.
>
> **Cowork rulings this instruction executes (v2 §D):** A-2 closed (L1.5 exempt-but-stated — stanza added by
> Cowork); L4+L5 request paths built NOW (before L6, per the user's gate); the L5 §15-3 placeholder concern is
> CLOSED (the Step-4 pin + lock-in test — v1 table row; the "do not carry past this step" text is the satisfied
> historical mandate); A-1 typology-vocabulary pass is COWORK-owned (not yours); census appendices are KEPT (no
> merge).

## Task 0 — the consolidated docs commit (docs-only; two commits)

**0a (docs):** commit the accumulated Cowork working-tree docs batch as ONE fork-only docs commit (the session-21
series: review + contracts + census & its two appendices + layer-spec amendments incl. L5 §5.0 pin, L6 sign-off +
banner fix, L1.5 bounded-context stanza + `score_inventory.md` with BOTH pending sections + roadmap/handoff/STATUS).
In the same commit, **DELETE**: the two ☠ tombstones (`cowork_temporal_extension_contract.md`,
`cowork_engage_criteria.md`), the two ⛔-superseded L3 drafts (`cowork_layer3_analysis_design.md`,
`cowork_layer3_keymode_incrementC_design.md`), and `cowork_github_9444_comment_draft.md` (sensitive — v2 §B3 #5;
if untracked, plain-delete). Confirm no other inbound references break (v2 §B2 says the three found are fixed —
two by Cowork already).
**0b (tools):** fix the stale docstring `tools/cc_e0_fullspine_measure.py` ("per cowork_engage_criteria.md §3" →
the roadmap's ENGAGE CRITERIA block / E0 stage). Tiny separate commit.

## Task 1 — L1 seam (commit; mostly test)

Assert **extend-equivalence at L1** (design §4/§8): after any `extend`, the model ≡ a fresh `build` over the enlarged
span (the interim whole-score rebuild makes this cheap to prove; the test is what outlives the interim). Idempotent
re-request test (already-loaded span = no-op).

## Task 2 — L3 reach-back: capability verified, activation MEASURED + HELD (commits: tests; then a held A/B)

The loop exists gated-OFF. (a) Extend `reachback_tests` to assert **equivalence** (reach-back result ≡ fresh decode
over the union span), the hard-bound termination, and the score-boundary truncate path. (b) **Flag-ON A/B,
read-only:** on a set of RANGE queries (the live product analyzes time ranges — P3-style selections over the
snapshot-source scores), measure flag-ON vs flag-OFF output deltas + wall-time. **Do NOT default-ON** — activation
changes live range-query behavior and is its own ratification (report the A/B; Cowork/user decide). Whole-score
paths must be provably untouched either way (I2).

## Task 3 — the L4 starved-window request path (commit; the v1-gap-#5 build)

Per design §5 (sharpened): at a selection edge, when the truncation is **decision-relevant** (the decision under the
truncated window is not already a full-margin `Commit`), the decoder runs the requester loop — `extend` (increment =
its natural unit, slices→ticks) → re-slice → re-decode the affected range → re-check — bounded by the stop condition,
the hard bound, and the score boundary (score-boundary ⇒ proceed truncated, no request). **Denial/truncation
provenance:** the slice result gains `clippedBySelectionEdge` (+ `cueDenied` where a request was refused) — design
§3 item 10. Dormant substrate ⇒ byte-identical on production by construction (grep-proof). Tests: must-fire
(figure straddling the edge, decision-relevant), must-not-fire (full-margin Commit at the edge; score boundary),
equivalence (post-extension ≡ fresh run over the final span), provenance on denial.

## Task 4 — the L5 pinned-extent discovery + request (commit)

Per design §5 / L5 §5.0 (pinned): a §5.5/§5.2/§5.3 decision whose decision-context span is cut by the selection edge
before any of (i) cadence-anchored function / (ii) punctuation boundary / (iii) the K-slice/B-beat bound holds →
the requester loop, forward. Extension re-runs obey the **§8 one-pass closure** (may finalize an open decision;
never re-opens a closed one — write the test that proves it). Denial → honest open mark + item-10 provenance.
Dormant ⇒ byte-identical. Tests: must-fire (cadence just beyond the edge), must-not-fire (span ended by (i)/(ii)/(iii)),
equivalence, no-reopen, provenance.

## Task 5 — system tests + the §11 gate proof (commit: tests)

**Step-size independence** (one big extend ≡ several small, same final span — design §8); **determinism** (same
score+selection+settings ⇒ same requests/results); **no-oscillation/termination**; and the standing proof:
**I2 whole-score inertness** — with selection = score, zero requests fire anywhere (assert it), suites green
(composing/notation/snapshots, NO golden refresh), corpus regen **53/24/53 exact identity sets**, `git status
tools/corpus` clean.

## Deliverable

`cc_extension_build_report.md` (HELD, line count at end): §0 docs commit summary; §1–§5 per task — reuse-vs-new,
commit hash, tests added, the L3 A/B numbers (HELD for ratification); §6 the §11 acceptance checklist, item by item,
each PASS/OPEN; §7 Unknowns. **On your report: Cowork re-reads this instruction, reads the report in full, verifies
every commit at committed objects and the §11 checklist before ratifying — L6 un-parks only on that ratification
(+ the user's L3-activation decision, which is separate).**

## Stop conditions

Any production-reachable behavior change outside Task-2's HELD A/B → STOP. Any I2 violation (a request firing on
whole-score) → STOP. Equivalence test failing → STOP (the invariant is the design; do not weaken the test). The L4/L5
request needing anything not obtainable through L1 `extend` + forward re-run → STOP + name it. No θ anywhere.
