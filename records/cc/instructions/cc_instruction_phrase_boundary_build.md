# CC Instruction — build the phrase-boundary primitive (Architectural Layer 1.5)

> **Authoritative spec: `cowork_phrase_boundary_design.md` (SIGNED).** That document is the contract — implement its
> mechanism exactly; this instruction is the **build sequencing, gates, and discipline**, not a re-spec. Read the design
> first. Companion research/proportionality: `cowork_phrase_boundary_methods.md`, `contrapunctus_findings.md` addendum.
> **★ Proportionality (user-ratified):** the SOTA reference (Contrapunctus) does no phrase/cadence detection and is still
> competitive — so this primitive is load-bearing for *our* cadence mechanism, **not** an accuracy requirement. Build the
> graded model **right, at its default constants, and stop** — do **not** chase segmentation accuracy. *(Reminder: the
> never-bash rule is Cowork's; it does not constrain your build/test runs.)*

## §0 — Preamble (sweep)
Commit local-only any unstaged Cowork docs (the phrase-boundary design + methods, the L5 amendments, the Contrapunctus
addendum): `docs(cowork): phrase-boundary design + proportionality`. Report the sha.

## §1 — INVESTIGATE (read-only) — STOP & report before the output-moving build
Establish the facts that decide byte-identity and placement; **do not build yet**:
1. **Enumerate every live consumer of the per-region "ends a phrase" flag** (and the two duplicated fermata scans —
   `regionanalyzer.cpp` `jkdPhraseBoundaryTicks` and `batch_analyze.cpp` `collectPhraseBoundaryTicks`). For each consumer,
   state whether it is **live in production** or **dormant/gated-off** (e.g. the key-agnostic cadence anchor; the
   default-off J-key-iii pass). **This settles the central question:** are the new boundary sources **byte-identical on
   production today** (all consumers dormant/gated) or **output-moving** (a live consumer)?
2. Confirm the **owning layer** (Layer-1.5 engraving-bridge / notation-derived views, beside the bass and spelling views)
   and that **all the design's notation inputs are reachable** from the engraved score: per-note voice/pitch/onset/
   duration (L1), eligible voices, fermatas, **breath marks / caesuras**, **double/final/repeat barlines**, **mid-score
   key-signature changes** (the engraved signature event, NOT an inferred key), **subito tempo changes / written
   ritardandos**, and the **L2 empty slices**. Flag any input not reachable from the notation view → STOP.
3. **STOP and report** the consumer enumeration + the byte-identity verdict + any unreachable input, before §3. (§2 is
   byte-identical and may proceed; §3 waits on this verdict.)

## §2 — BUILD Step A — the owned primitive + byte-identical de-duplication
- Create the **one owned Layer-1.5 phrase-boundary primitive** and move the existing **fermata-only** scan into it;
  **repoint every consumer** (the enumerated `ends-a-phrase` sites) at it. At this step the *definition is unchanged*
  (fermata-only) — this is pure de-duplication.
- **Gate (byte-identical):** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh. Movement → STOP (the de-dup changed behaviour).
- Commit locally. This is the safe foundation; it can land regardless of the §3 verdict.

## §3 — BUILD Step B — the graded model (per the design §4) — at default constants only
Implement the design's graded model on the owned primitive — **exactly per `cowork_phrase_boundary_design.md` §4**:
- **§4.2 deterministic marker spikes:** fermata, breath/caesura, double/final/repeat barline, **mid-score key-signature
  change** (engraved event, not inferred key), subito tempo change / written ritardando, all-voice-rest onset — each a
  fixed additive spike **after** the surface core is normalised, magnitude ≥ max surface strength.
- **§4.1 + §4.3 per-voice surface-cue core:** per eligible voice, the **gap / inter-onset / pitch-interval** profiles via
  the **local-change rule** (`x · (left + right change-ratios)`), **max-normalised** per profile; the gap-dominant
  **weighted sum**; **aggregated to the texture** by summing per-voice strengths over **τ-merged onsets**. Expose **both**
  the per-voice profiles and the texture profile.
- **§4.4 peak-picking:** local maximum on the texture profile **and** above the **Simple-Picker** threshold (whole-profile
  mean + k·SD); emit the picked boundary ticks + the per-region "ends a phrase" flag.
- **★ Constants stay at the design's stated DEFAULTS (§11-1): the gap-dominant weights, k, τ, the minimum-silence
  duration, the spike magnitude, and any optional coincidence weight. DO NOT tune them for accuracy — that is the
  precision phase (the firewall) and is explicitly out of scope here.** Build the mechanism; leave the numbers.

## §4 — Tests (per the design §7)
- **Oracle tests:** a rest yields a high-strength texture peak; a long note among short ones yields an inter-onset peak; a
  fermata / double-barline / key-sig change / subito tempo change yields a marker spike; a single mid-phrase leap does
  **not** clear the threshold alone; a region containing a picked boundary reports "ends a phrase"; a one-voice phrase end
  scores a per-voice boundary but a low texture strength.
- **Chorale-corpus validation:** check the picked texture boundaries against the corpus's known phrase structure (the
  per-voice aggregation is engineering on top of monophonic-validated cues — validate, don't assume).

## §5 — Gate
- **If §1 found all `ends-a-phrase` consumers dormant/gated → the graded model is byte-identical on PRODUCTION today:**
  corpus **53/24/53** unchanged, suites + snapshots green, no golden refresh. (The new strength becomes load-bearing only
  when the function layer engages.) Movement → STOP.
- **If §1 found a LIVE consumer → the output moves:** measure against the **corpus two-tier BIR gate on BOTH presets** —
  **zero** new class-(b) (pitch-class-decidable) cases, the **case-identity set** the gate (per CLAUDE.md), and report the
  before/after sets. Any class-(b) increase → STOP. Suites + snapshots green (refresh goldens only if the change is
  verified-correct, with the before/after diff in the report).

## §6 — Deliver
Commit **locally (unpushed)** per step (Step A; Step B + tests). Write `cc_phrase_boundary_build_report.md` (gitignored):
the §1 consumer enumeration + byte-identity verdict, the Step-A de-dup (sha, byte-identical proof), the Step-B build (sha)
+ the §4 tests + chorale validation, and the §5 gate result. So Cowork verifies by sha that the de-dup is byte-identical
and the graded model honours the gate + the default-constant / proportionality discipline.

## §7 — Stops
- §1 finds an unreachable notation input, or the byte-identity verdict is unclear → STOP, report (don't guess).
- Any byte-identity break at Step A, or a class-(b) increase at Step B → STOP.
- Tempted to **tune** the weights / threshold for accuracy, or to add cues beyond the design's set → STOP (firewall +
  proportionality; the design's marker list is extensible later, not now).
- `upstream` push → STOP.
