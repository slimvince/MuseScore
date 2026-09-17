# CC Instruction: Stage 3 design — the decoder design document (design-only, ratification-gated)

## Context

Stage 2 is closed. This instruction produces the **Stage 3 design document**
(`docs/decoder_design.md`) — no production code, no tests, no behavior change. The
document is ratification-gated: drafted, reviewed by Cowork/user, then committed.
Throwaway probes to ANSWER design questions are allowed (uncommitted, listed in the
report); production prototyping is not — that starts at 3.1 after ratification.

Mandatory reads (in this order): `docs/implementation_roadmap.md` Stage 3 rows
(3.1–3.5 incl. the 3.1 decode-once note and 3.4 obligations);
`cowork_target_architecture_review.md` (the part-1 mapping table is the design's
skeleton); `docs/redesign_plan.md` "Architecture review addendum"; `docs/scoring_model.md`
(§3 formula, §4 terms, §6 gates, §8 constraints); `harmonicfunctionlayer.{h,cpp}`
(the competition pipeline IS the proto-decoder); `docs/perf_p3_baseline.md`;
ARCHITECTURE.md "Path divergence decisions (Stage 2.4)" (D-P4/D-BRIDGE revisit
triggers); the Stage-1 findings lists (1a F2/F5; 1b F1–F8; 1c G1–G5).

Standing rules (trust model 1–4): never guess — where the design depends on an
unverified property of the current code, probe it; where a question is genuinely
open, put it in the §Open-Questions section for Cowork/user decision rather than
deciding silently.

## The document must cover (section per item)

1. **Scope statement.** Stage 3 decodes the CHORD path over the EXISTING segmentation
   (greedy regions stay as-is; joint segmentation+labeling is explicitly out of Stage 3
   scope — note it as the natural extension, cf. the segmental-CRF literature). Key
   path (Stage 4) and functional layer (Stage 6) are out of scope; the design states
   its interfaces to them.
2. **Lattice shape.** Nodes, edges, what a path is; where candidates come from (the
   oracle's `ScoringSnapshot` cells / `results[]`); candidate-set size control (the
   current top-3 + threshold vs a wider per-region beam-in); memory envelope estimate
   for Mozart-scale scores (use the 2.5 region counts).
3. **Emission/transition factorization — term by term.** A table mapping EVERY §3/§4
   term to its decoder home: emissions (basisIndep, basisDep, complexity/aug factors,
   wComplete), transitions (rcb + Gate R's structural condition, wSeq, wDim,
   stepIn/Out), and the AWKWARD ones that don't factor pairwise — name each and design
   its treatment explicitly: the wDim post-bonus quality guard (global, not pairwise),
   the Pass-B m7-budget guard (within-bass-group competitor scan), the score threshold
   /result cap, Iter 86/91/pedal, gates A–L (post-decode re-rank initially, retired
   per the 3.4 obligations), `maxTotalInversionContextBonus` (inert — note disposition).
   Where a term resists clean factorization, the design says what beam-1 does with it
   (byte-identity constrains the answer) and what wider beams do.
4. **Beam-1 byte-identity argument.** Why beam-1 + the stated factorization reproduces
   the current greedy pipeline exactly (the current pipeline = beam-1 with transitions
   evaluated against the committed predecessor). Identify every place the equivalence
   could break (FP evaluation order! — the §3 tie policy and the near-tie canary test
   are the tripwires) and the verification plan: 0/353 corpus A/B on Baroque + Jazz +
   Default, snapshots, all suites, BIR identity sets.
5. **Path state vs `advanceTemporalContext`.** What replaces the temporal-context
   commit chain; how `ChordTemporalContext` fields map to path state; the Step-1/2
   confidence fields' fate; sub-region (Pass 2/2b) handling under the decoder.
6. **Oracle temporal-signal migration (roadmap 3.3).** The five oracle-side signals
   (resolutionBonus + 4 inversion bonuses) → transition terms; the **Gate R
   `basisDep ≤ 0` coupling** must be redesigned in the same step (documented
   cross-layer dependency) — state the replacement condition.
7. **Gate-retirement plan (roadmap 3.4/3.4b).** Per gate: decoder-subsumed /
   stays-as-re-rank / retired-dead (B/C/D). The Stage-1 pinned tests as per-gate proof
   obligations — name which tests gate each retirement, incl. 1a F2 (first-wins tie
   scan) and F5 (threshold-gated diff-root append), and the 1b mixed live/captured
   reads (F4) the decoder must consciously re-decide.
8. **Decode-once, query-many (P3/P4/bridge).** Per-score lattice cache; what
   invalidates it (edit granularity — design a bounded re-decode window, don't promise
   full incrementality); P3 becomes a lookup (target: orders below the 33–215 ms
   medians); P4 and the bridge consume decoded path state (CLOSES the D-P4/D-BRIDGE
   revisit triggers — say so explicitly); what happens before the cache is warm.
9. **Quality levels ↔ beam width** (ARCHITECTURE §2.14): level 0 = beam 1 (budget:
   p95 ≤ 2.5-baseline ×1.10 — but state the decode-once expectation separately),
   level 1 = small beam, level 2 = exact/wide; where the knob lives.
10. **Config-agnosticism.** The decoder takes `ChordAnalyzerPreferences` like the
    current pipeline; no preset logic inside; the V4 Default config is the
    user-relevant evaluation column (gates stay Baroque/Jazz per CLAUDE.md policy).
11. **Acceptance-case roster — classified honestly by what unlocks each.** For every
    case: what Stage 3 alone should fix (Δ=+7a bwv102.7/bwv261 — inter-region
    revision; C2 bwv320-class rcb ties), what Stage 3 must NOT break (the Δ=+7b trio,
    Gate-R-fixed, pinned), and what needs Stage 4/6 (A2 dominant-in-minor = key/cadence;
    B1 mMaj7 = cadence confirmation; C1 schumann = absorption/segmentation-coupled;
    bwv187.7 = mode-prior/key-sensitive — classify with evidence, don't promise).
    Expected-movement table for the gates + the user-default column.
12. **Migration sequencing + risks.** Map design sections → roadmap rows 3.1–3.5;
    the riskiest assumptions; what gets built behind a flag vs replaces in place;
    rollback story per step.
13. **§Open Questions for Cowork/user** — anything above where you see a genuine
    fork; recommendations welcome, decisions are ours.

## Report — `cc_stage3_design_report.md`

§1 any probes run + what they settled; §2 the design doc's section map + the three
most load-bearing claims with their evidence; §3 the Open-Questions list duplicated
inline (this is what gets decided at ratification); §4 unknowns. The design doc
itself stays uncommitted until the ratification addendum arrives (rule 4).

Stop conditions: a mandatory-read contradicts the part-1 mapping in a way that breaks
the factorization (report before designing around it); any design choice that would
require weakening a Stage-1/2 pin or gate; scope creep into key-path/functional-layer
design beyond interface statements.
