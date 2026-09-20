# Stage 3 Decoder Design — Drafting Report

*CC, 2026-06-12 (session 6). Base commit `3aa9db7676`. Deliverable: the design doc
`docs/decoder_design.md` (DRAFT, uncommitted pending ratification — roadmap rule 4) and
this report. No production code, no tests, no behavior change.*

---

## §1 — Probes run and what they settled

All probes were throwaway (uncommitted), run to ANSWER a design question rather than to
change anything. Four `batch_analyze.exe` runs (Git Bash launch per
`feedback_batch_analyze_windows`), `--preset Default` to reflect the live configuration.

| # | Probe | Result | What it settled |
|---|---|---|---|
| P1 | `batch_analyze K279-1.mscx --preset Default --dump-regions batch` | **84 batch regions**, avg 3.36 results/region, max 4 | The lattice **node count** for the largest perf-corpus score (Mozart, 100 measures). Settles the §2 memory-envelope claim concretely instead of by guess. |
| P2 | same, `--section-level` | **141 section regions** | The *user-visible* (P3/analyzeSection) node count — the granularity the decode-once cache actually serves. |
| P3 | `chorale_001 … --dump-regions batch` (+ section) | **40 batch / 43 section regions**, avg 3.27, max 4 | Small-score envelope bound. |
| P4 | (from the result fields) results-per-region distribution | beam-1 emits ≤ 4 candidates/region (top-3 + diff-root append) | Confirms the §2 "beam-1 candidate set" claim against live output, not just code reading. |

**Memory envelope settled (§2):** beam-1 is kilobytes; a full-snapshot-per-node wider
beam on Mozart is ≈ 2.4 MB worst case, a top-K=8 beam-in ≈ 72 KB. Memory is a
non-constraint at any beam width these scores reach; **time** (Pass-0 to produce the
snapshots) is the only real resource, which §8 addresses.

Everything else in the design is grounded in code/docs read in full (the proto-decoder
`harmonicfunctionlayer.{h,cpp}`, scoring_model §3/§4/§6/§8/§11, the Stage-1 reports, the
roadmap, the architecture review, the perf baseline, the path-divergence decisions) — no
further probe was needed, and none was run that would constitute production prototyping.

---

## §2 — The design doc's section map + the three most load-bearing claims

**Section map** (`docs/decoder_design.md`):

1. Scope — chord path over existing segmentation; joint seg+label / key / functional out,
   stated as interfaces.
2. Lattice shape — nodes = regions, candidates = `ScoringSnapshot.cells`, edges =
   transitions; beam-in control; probed memory envelope.
3. Emission/transition factorization — full term-by-term table; the four AWKWARD terms.
4. Beam-1 byte-identity argument + the FP/tie tripwires + the 5-point verification plan.
5. Path state vs `advanceTemporalContext`; Step-1/2 fields' fate; sub-region handling.
6. Oracle temporal-signal migration (3.3) + the mandatory Gate R `basisDep≤0` redesign.
7. Gate-retirement plan (per gate; 1a-F2/F5, 1b-F4 obligations named).
8. Decode-once, query-many — P3 perf fix; bounded re-decode window; closes D-P4/D-BRIDGE.
9. Quality levels ↔ beam width; the level-0 budget stated as two separate claims.
10. Config-agnosticism — prefs in, no preset logic; Default = eval column.
11. Acceptance-case roster — classified honestly with evidence; expected-movement table.
12. Migration sequencing → roadmap rows; risks; flag vs in-place; rollback.
13. Open Questions (Q1–Q7) — duplicated inline in §3 below.

**The three most load-bearing claims and their evidence:**

1. **Beam-1 reproduces the current pipeline byte-identically because the current
   pipeline IS beam-1 with backward edges against the committed predecessor and forward
   signals against a cold lookahead.** Evidence: `harmonicfunctionlayer.cpp:264–435` (the
   per-bass score expression and cross-bass argmax), `advanceTemporalContext`
   (chordanalyzer.h:819+) committing the gate-corrected identity, and `inferNextRootPc`/
   `backfillNextRootPc` precomputing `nextRootPc` independently (the cold lookahead). The
   decoder is a re-expression of this loop, so the winner and alternatives at every node
   are unchanged — *provided* the FP arithmetic order is preserved (scoring_model §3 "no
   epsilon"; the Δ=+7b 0.02 and bwv320 1.92-vs-1.90 near-ties are the tripwires).

2. **`rcb` is a destination-conditioned edge weight `0.40 × cf × af`, not a constant**,
   and the forward signals read a cold lookahead, not the decoded successor. Evidence:
   `harmonicfunctionlayer.cpp:311` (`newBasisIndep = cell.basisIndep + rcb` then `×
   complexityFactor × augFactor`) and lines 316–322 (w_seq/w_dim read `ctx.nextRootPc`,
   which is set externally). This is the single most important structural fact: a decoder
   that models rcb as a flat additive edge, or that promotes forward signals to decoded
   edges at beam 1, will **not** be byte-identical. It also dictates that the Δ=+7a fix
   (forward revision) only becomes available at wider beams (§11).

3. **Gate R's `basisDep ≤ 0` proxy must be redesigned in the same change as the
   inversion-bonus migration (3.3), to read the sounding third directly from the
   snapshot.** Evidence: the explicit cross-layer-dependency comment at
   `harmonicfunctionlayer.cpp:300–307` + chordanalyzer.h:329 debt + scoring_model §4
   "Why the `basisDep ≤ 0` condition." `sameRootInversionBonus` (the sounding-third
   signal) lives in `basisDep`; migrating it out silently breaks Gate R unless the
   condition is rewritten to test `pcWeight[third] > threshold` directly. Splitting the
   two across commits opens a silent-regression window.

---

## §3 — Open-Questions list (what gets decided at ratification)

Reproduced from `decoder_design.md` §13. Each has a CC recommendation; the decision is
Cowork/user's.

- **Q1 — Decode-once cache scope and ownership.** Whole-score decode cached once, or
  ±window per query? Where does the cache live (bridge vs a new per-score cache)?
  *Rec: whole-score decode, cached in the bridge, bounded-window invalidation.*
- **Q2 — Forward signals at Level 1.** Promote w_seq/w_dim/w_stepOut/lookahead to true
  decoded-successor edges (behavior change, likely needed for Δ=+7a), or keep the cold
  lookahead and widen only the backward search? *Rec: promote at Level 1.*
- **Q3 — Gate-mutates-context ordering.** Retire/fold gates into emission before widening
  the beam past them, or allow wider-beam edges on pre-gate identities with a documented
  re-decide? *Rec: retire-first; sequence 3.4 to lead 3.2 for identity-mutating gates.*
- **Q4 — 1b-F4 half-migrated live/captured reads (H/I/K/L).** Reproduce exactly during
  migration, or fix as a conscious re-decide while retiring? *Rec: reproduce at beam-1,
  fix-as-retire in 3.4.*
- **Q5 — Output interface to Stage 4/6.** Emit committed identity only, or the full ranked
  path + alternatives + margins? *Rec: emit the path (evidence forwarding); committed =
  `path.front()`.*
- **Q6 — Beam-in width at Level 1+.** Top-K cells per region — what K? *Rec: K = 8, tune
  at Stage 5.*
- **Q7 — P3 perf fix in 3.1 or a separate track?** *Rec: design cache-ready in 3.1, land
  caching as 3.1b after the byte-identity gate passes, so correctness and caching risks are
  verified independently.*

---

## §4 — Unknowns / caveats

- **No stop-condition was hit.** No mandatory-read contradicts the part-1 mapping in a
  way that breaks the factorization; no design choice requires weakening a Stage-1/2 pin or
  gate; no scope creep into key-path/functional-layer design beyond interface statements.
  The part-1 mapping table held against the code in every row.
- **bwv320 dual classification (§11).** bwv320 appears both as a Δ=+7b case (Gate-R-fixed,
  pinned) and as C2 (accepted residual, m27 G/E). I classified them as two distinct things
  with the caveat stated, rather than claim the decoder fixes "bwv320" wholesale — the
  Gate-R-fixed instance is a must-not-break, the C2 residual is a wider-beam target. If
  Cowork knows these are the *same* tick, the C2 row should be reconciled at ratification.
- **completeTriadInversionBonus is region-local, not temporal** (§3/§6). The roadmap 3.3
  phrase "resolutionBonus + 4 inversion bonuses" bundles it with the transitions; the
  design pulls it out as an emission term because its trigger ("3 tones present in a 3-PC
  texture") has no temporal dependency. If Cowork intends it to migrate too, that is a
  divergence to resolve — but migrating a region-local term to a transition edge would be
  an error, so I flagged it explicitly rather than follow the phrasing.
- **Region counts are `--preset Default` at one commit** (`3aa9db7676`); they are
  illustrative envelope anchors, not gate numbers. The memory conclusion (non-constraint)
  is robust to the exact counts.
- **The decode-once invalidation horizon (§8)** is designed as bounded (±edge-horizon),
  not proven incrementally correct — that proof belongs to the 3.1b implementation, not
  this design.
- **P4 empty-window fallback rate** is 0/2231 on the perf corpus but not provably 0 in
  general (perf doc caveat); the D-P4 closure assumes P4 reads the decoded path when it
  does fire, which is the contract, independent of the rate.

---

*Design doc stays uncommitted until the ratification addendum (roadmap rule 4). This
report is the input to that ratification.*
