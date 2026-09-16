# CC Instruction — Foundation Stage 2a: understand & classify the preserved WIP, hunk-by-hunk (READ-ONLY)

> **Context.** The ~1700-line WIP preserved in stash `bc4fa79c4a…` + the per-file patches `foundation_wip/` must be
> triaged **hunk-by-hunk** before the foundation is clean — user requirement: **each hunk must be understood**, even
> the ones we discard. This stage is **read-only classification only** — understand and recommend, **dispose nothing**.
> The actual keep/discard disposition is a separate, gated **Stage 2b** after Cowork + user review this report. The
> stash stays intact throughout.

## §0 — Two small protected steps first (the held-over items)
1. **Commit Cowork's CLAUDE.md gate-table correction** (currently uncommitted in the tree — Stage 1): the BIR tables
   were corrected `57/23/57 → 53/24/53` (the ratified post-L3-wiring state). Commit **local-only**:
   `docs: correct BIR gate tables to the ratified 53/24/53 (post-L3-wiring delta; the 57/23/57 tables were stale)`.
   Confirm `git show --stat` lists **only `CLAUDE.md`**.
2. **Re-emit the exact Default-53 BIR case set** (read-only): the Stage-0 report's one-line Default-delta *prose* was
   internally inconsistent. Re-read `tools/corpus/default`'s `characterise_bir_false.py` output (or re-run it) and
   paste the **exact 53-case stem@tick list**, so Cowork can finalize the CLAUDE.md Default identities. (No code change.)

## §1 — Scope and method
**Scope** — the Stage-0 §2 "leave-in-stash" set (everything *except* Cowork's already-recovered docs):
- **Code:** `src/composing/analysis/chord/chordslicedecoder.{cpp,h}`,
  `src/composing/analysis/key/keymodesequence.{cpp,h}`, `src/composing/analysis/key/keymodeanalyzer.h`,
  `src/composing/analysis/section/localmodulationdetector.{cpp,h}`,
  `src/composing/analysis/engravingbridge/regiontoneprimitives.cpp`.
- **Tooling:** `tools/batch_analyze.cpp`, `tools/cc_layer3_keymode_baseline.py`, `tools/compare_rn.py`.
- **Pre-existing non-Cowork doc WIP:** `STATUS.md`, `BUILD_AND_TEST.md`, `cowork_github_9444_comment_draft.md`,
  `docs/back_half_design.md`, `docs/decoder_design.md`.

**Method** — work from the per-file patches `foundation_wip/<file>.patch` (and the stash for context). Go
**file-by-file, hunk-by-hunk**. For **each hunk**, record:
- **(a) what it changes** — one concise line;
- **(b) layer** — which architectural layer it belongs to (L1/L2/L3/L4/tooling/doc);
- **(c) intent** — its evident purpose (what was it trying to do?);
- **(d) superseded?** — is it already on committed HEAD, or superseded by the new layered specs / the phase plan
  (e.g. tpc → Phase 4b built fresh; an L4 decoder change → the rewritten L4 spec's build backlog)?
- **(e) classification + one-line rationale** — **KEEP / DISCARD / INVESTIGATE** (rubric below).

## §2 — Classification rubric (the discipline)
- **KEEP** — ratified or clearly valuable, belongs in its proper layer essentially as-is, **not** superseded by
  committed HEAD or the layered rebuild. (Expect this to be **rare** — most of this WIP is exploratory.)
- **DISCARD** — exploratory / superseded by the layered rebuild or already-landed work, or the **tpc half-feature**
  (pre-decided discard: the consumer was already backed out at `b57dbfa7a8`; tpc is rebuilt properly in **Phase 4b**).
  Still **describe and understand** it before recommending discard — that is the user's explicit requirement.
- **INVESTIGATE** — intent or value genuinely unclear; flag for deeper review or a measurement before deciding.

Anchor every call against three references: **committed HEAD** (already landed?), the **layered specs**
(`cowork_layer*_design.md` — is the *proper* version of this idea specified there, to be built fresh?), and the
**stabilization plan** (`cowork_l1l3_stabilization_plan.md` — is this Phase-4a scale-membership-lever or Phase-4b tpc
work, hence the WIP version superseded by a fresh, gated build?).

**Pre-decided (still describe):** the tpc hunks — the `tpcKeyFitWeight` member in `keymodesequence.*`, the tpc reads
in `regiontoneprimitives.cpp`, and any tpc/`--seq-tpc-weight` remnant in `batch_analyze.cpp` — are **DISCARD** (Choice
1; Phase-4b rebuild). Note them, don't re-land them.

## §3 — Watch for a hidden load-bearing hunk
The build break was a committed consumer depending on an uncommitted member. **If any WIP hunk turns out to be
depended on by committed HEAD** (i.e. discarding it would break the build or a test), **flag it prominently** — it is
another half-committed dependency we must resolve deliberately, not a free discard.

## §4 — Deliverable
`cc_stage2a_wip_triage_report.md` (gitignored):
- the §0 results (the CLAUDE.md commit hash + `--stat`; the exact Default-53 list);
- a **per-file → per-hunk table**: `hunk (patch:lines) | what | layer | intent | superseded? | KEEP/DISCARD/INVESTIGATE | rationale`;
- a **summary**: counts per classification, and a short list of every **KEEP** and **INVESTIGATE** hunk (these are
  the only ones needing a Cowork + user decision before Stage 2b);
- any **load-bearing** hunk flagged per §3.

## §5 — Constraints & stop conditions
- **READ-ONLY classification.** Beyond the §0 CLAUDE.md commit and the read-only Default re-emit, **apply / revert /
  commit / drop NOTHING.** The stash `bc4fa79c4a…` stays intact.
- **No disposition** — do not commit a KEEP or revert a DISCARD; that is Stage 2b, gated, after review.
- Every classification **cites `foundation_wip/<file>.patch` line ranges** so Cowork can verify the call at source.
- `upstream` never; `origin` held; local commit only for §0.
- A hunk is found load-bearing for committed HEAD → flag (don't act). You begin disposing hunks → STOP (that's 2b).
