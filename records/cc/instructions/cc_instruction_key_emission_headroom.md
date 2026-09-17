# CC Instruction: Key-emission headroom investigation — scope the Stage-4 emission fix

## Context

The Stage-4 design finding (verified): the key PATH fixes ~10% of S2; ~85% is Class B —
the EMISSION consistently prefers the wrong key (correct key not even rank-2 in 51.6% of
S2). The HMM path is deferred (META-PRINCIPLE: precision is emission, not search — roadmap).
What Stage 4 must actually deliver is **KeyArea spans + a key-emission fix**. This
investigation scopes that emission fix: **how much of the ~85% Class-B is recoverable, by
which mechanism (structural partial-signature/profile fix vs Stage-5 fitting vs genuine
ceiling)?** That answer shapes Stage 4.

Base `f8c6b3932a`. Method A–H. **HELD = `git add` ok, commit NOT, until an approval file
says so** — EXCEPT the one diagnostic instrument in Task 2, which has its own explicit
proof-gate-and-commit authorization below. Read-only otherwise.

Mandatory reads: `cc_stage4_design_report.md` §1 (the Class A/B/C split, the 509 relative
/ 153 single-key / 499 runner-up-reachable structural numbers); `docs/key_detection_baroque_partial_signature.md`
(the `81978321e3` fix — what it does and its scope); `keymodeanalyzer.{h,cpp}` (the six
scoring helpers: `scoreScaleMembership`, `scoreTriadEvidence`, `scoreCharacteristicPitch`,
`scoreTrueLeadingTone`, `scoreKeySignatureProximity`, `scoreModePrior`,
`applyRelativePairDisambiguation` — ARCHITECTURE §4.2); `keyresolver.cpp`
(`partialSignatureCorrection`, `promoteWinnerInPlace`).

## Task 1 — Tier-1 structural decomposition (cheap, serialized fields, no build)

Refine the Class-B bulk (926 regions) from the committed `.ours.json` + DCML, **no
emission internals needed**:
1. Decompose Class-B by cause: relative major/minor (the 509-ish), fifth-related, modal,
   other; × single-key-stem vs modulating-stem. Per-class counts.
2. Of the relative-pair Class-B: how many SHARE a key signature with the correct key
   (the partial-signature target) vs differ by signature? (Relative pairs share a
   signature by definition — confirm, and check whether `81978321e3`'s correction
   *could* reach them mid-piece or only at piece-start, from the fix's logic.)
3. The 153 single-key stems: are they uniformly relative-locks, or mixed? These are the
   purest emission-error floor.

## Task 2 — The diagnostic instrument (AUTHORIZED build, byte-identity-gated)

The causal question — WHICH of the six scoring terms makes the wrong key win — cannot be
read from serialized winners. Build a **read-only key-candidate dump** (e.g.
`batch_analyze --dump-key-candidates TICK[,TICK]` or a per-region mode), exposing
`keymodeanalyzer`'s already-computed per-candidate `eval.score` AND its six component
sub-scores for the top-N candidates at a window. This is diagnostic-only, the
diagnose-chord precedent: **production analysis must be byte-identical** (the dump only
serializes scores already computed; the selected winner is unchanged).

Proof gate (this instrument MAY commit on green, like the 3.4 pre-authorized ships):
build + composing/notation suites + snapshots 11/11 zero-diff + a Baroque corpus spot
sha256 (0/353 — the dump doesn't touch the winner). Commit:
`feat: read-only key-candidate diagnostic dump (Stage-4 emission instrument)`.
If byte-identity does NOT hold (the dump perturbs the winner), STOP — that's a finding.

## Task 3 — Tier-2 causal analysis (using the instrument)

On a deliberate sample of Class-B cases (bwv244.54 D-min-for-F-maj, the bwv343 early
half, + relative-pair and single-key representatives — ≥12 windows): read the
component-score breakdown for the wrong winner vs the correct key. **Which term(s)
account for the 2.0–3.3 gap?** Hypotheses to test, not assume:
- `scoreModePrior` (Aeolian/minor prior vs Ionian/major — does the minor prior over-favor
  the relative minor?);
- `scoreTriadEvidence` (does the relative-minor tonic triad get more support because its
  pitches are more present?);
- `scoreCharacteristicPitch` / `scoreTrueLeadingTone` (leading-tone evidence for the
  wrong key);
- `applyRelativePairDisambiguation` (the existing tie-breaker — is it firing wrong, or
  not firing?).
Report the term-level attribution with the actual numbers per sampled case.

## Task 4 — Scope the fix + recommend Stage 4's shape

From the causal attribution, classify the Class-B recoverable headroom:
- **Structural fix** (a partial-signature/disambiguation rule change — Baroque-structural,
  not a fitted weight): how much of Class-B, and what's the rule? (e.g. broaden
  `applyRelativePairDisambiguation` / `partialSignatureCorrection` to fire mid-piece on
  the triad-evidence pattern the sample reveals.)
- **Stage-5 fitted** (the six terms' weights are mis-balanced — a fitting problem): how
  much, and which weights.
- **Genuine ceiling** (tonally ambiguous even with perfect emission — the chorale really
  is a/C ambiguous): how much.
Then recommend Stage 4's final shape: emission fix (structural part now / fitted part to
Stage 5) + KeyArea spans, HMM path deferred — or, if the data surprises, otherwise.
**Do not implement the emission fix** — this run scopes it; the fix itself is the ratified
Stage-4 build.

## Deliverable — `cc_key_emission_headroom_dossier.md`

§1 Tier-1 decomposition (counts); §2 the instrument (+ commit hash, byte-identity proof);
§3 the term-level causal attribution (real numbers per sampled case); §4 the fix scoping
(structural/fitted/ceiling split with sizes) + the Stage-4-shape recommendation; §5
unknowns. Every number [probe]; every causal call sampled-or-flagged.

Stop conditions: the dump perturbing the winner (byte-identity fail — stop); a causal
attribution that would be a guess (mark "needs more windows," don't assign); discovering
the Class-B bulk is mostly genuine ceiling (report — it caps Stage 4's key-axis value and
routes the residual to "accepted ambiguity," reshaping again); scope creep into
implementing the fix (this run scopes only).
