# CC Instruction — Phase 5 refactor (1 of 2): derive `kMasks` from one canonical interval source (byte-identical)

> **Why.** Audit Q1.3: `kMasks` (`function/harmonicfunctionlayer.cpp:191-209` — 17 hand-typed `uint16_t` bitmasks) is a
> **hand-maintained duplicate** of the template intervals in `chord/chordanalyzer.cpp`'s `templates[]`
> (`:1198-1216`). The headers themselves warn the two "MUST stay in sync"; the compiler enforces only the *count*, not
> the *contents*, so a wrong/zero mask **silently disables Gate R** for that template. Fix: define the intervals **once**
> and **derive** `kMasks`, closing the hazard. **Build-it-right refactor, byte-identical — NO scoring/template/gate
> logic change.** The 17 mask *values* must be unchanged.
>
> **Grounded (verified at source by Cowork, file tools):** `kMasks` = `static constexpr std::array<uint16_t,
> kTemplateCount>` at `harmonicfunctionlayer.cpp:191`, bit *i* set ⇔ interval *i* is a template tone, `static_assert
> size==kTemplateCount` at `:210`. `templates` = `static const std::array<TemplateDef, kTemplateCount>` at
> `chordanalyzer.cpp:1198`, each `{ ChordQuality, intervals{…}, weights{…} }`; the **intervals** column is exactly what
> `kMasks` encodes (Cowork confirmed all 17 match).

## §0 — Preamble: protect the uncommitted Cowork docs (sweep-protection)
Commit, **local-only**, the accumulated Cowork doc edits in the tree — `cowork_phase5_branch_backfill_spec.md` (new),
`cowork_l1l3_stabilization_plan.md` (the Phase-5b/6 re-sequence), `cowork_l1l4_architecture_audit.md` (corrections),
`cowork_tpc_capability_design.md`, and any other modified `cowork_*`/`COWORK_*` docs:
`docs(cowork): Phase-5 branch-backfill spec + plan re-sequence (L1-L4 seal) + audit/handoff corrections`. Confirm
`git show --stat <sha>` lists only doc files (no source). Report the sha.

## §1 — Read-only confirm BEFORE changing (this is the safety gate)
- Confirm the `TemplateDef.intervals` representation (type, fixed vs variable length).
- **Compute** each template's mask from its intervals and **compare to the 17 current hand-typed `kMasks` values.**
  They MUST be **exactly equal**. **If ANY differ → STOP and report** — a mismatch is a *latent live bug* (a mask that
  silently mis-gates), a surfaced defect to escalate, NOT something to "correct" inside this refactor.

## §2 — The refactor: one canonical interval source → derive `kMasks`
- Define the template intervals **once** in a place both `chordanalyzer.cpp` (its `templates`) and
  `harmonicfunctionlayer.cpp` (`kMasks`) can see — e.g. a `constexpr` interval table near `kTemplateCount` in
  `chordanalyzer.h`. Pick the **minimal** form.
- **Derive `kMasks`** from that source with a `constexpr` function (mask bit *i* = OR over the template's intervals);
  **delete the hand-typed `kMasks` literal array.**
- **Single-source the templates too IF it's clean:** if `templates[]` can take its intervals from the canonical table
  without disturbing the `weights`/score-matrices, do so (true one-source). **If that is invasive/risky, it is
  acceptable for this step** to instead keep `templates[]`'s interval literals but add
  `static_assert(maskFromIntervals(templates[i].intervals) == kMasks[i])` for all *i* — compiler-enforced single-truth
  without restructuring the scoring array. **Report which path you took** and why.

## §3 — Gate (byte-identical is the hard gate)
- The 17 derived `kMasks` values **exactly equal** the current hand-typed values (the §1 equality / a `static_assert`
  against a frozen snapshot proves it at compile time).
- **Corpus BIR 53/24/53, both suites, snapshots — UNCHANGED** (Gate R behaviour is identical). **Any movement → STOP**
  (the derivation altered a mask — a bug, not a refresh).
- **No scoring/template/gate/weight/matrix logic changed** — only the interval data is single-sourced.

## §4 — Scope & stops
- A computed mask ≠ the current hand-typed one → **STOP**, report (latent live bug; do not silently change behaviour).
- You change any score weight, matrix, template membership, or gate → STOP (out of scope — interval single-sourcing +
  `kMasks` derivation ONLY).
- **Doc sync:** `docs/scoring_model.md` §3/§9 describe the kMasks↔templates hand-sync rule — update them to the
  now-**derived** (no hand-sync) state in the same commit (the §-sync rule).
- `upstream` never; local commit only.

## §5 — Deliver
Commit **locally (unpushed)**: the refactor + the `scoring_model.md` update (the §0 docs committed separately first).
Write `cc_kmasks_derive_report.md` (gitignored): the §1 equality proof (all 17 match), the §2 path taken (full
single-source vs compiler-checked), the byte-identity proof (corpus/suites/snapshots unchanged), the doc update, and
the commit sha (so Cowork verifies by sha that only `harmonicfunctionlayer.*` / `chordanalyzer.h` / `scoring_model.md`
changed — no scoring logic).
