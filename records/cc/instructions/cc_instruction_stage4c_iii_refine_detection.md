# CC Instruction: Stage 4c-iii — refine cadence detection (structural/raised-LT/Picardy) + re-measure (no wiring)

## Authorization + framing

The 4c-i §8 "far below ceiling" stop fired (realized detection **55.7%**, clean-stem contradiction **34%** —
too low to wire). `cc_stage4c_i_report.md` diagnosed the cause precisely: the naive count/finality vote
**reproduces the relative-major error** — abundant diatonic V→III tonicizations (G→C in A-minor) outvote
the rarer true V→i. This run **improves detection discrimination, then RE-MEASURES realized detection —
still NO wiring** (production untouched → byte-identical, same as 4c-i). Wiring is 4c-ii, gated on this number.

**Architecture clarification (corrects a 4c-i over-statement):** *reading/calling* the engraving Score is
allowed from any code we may edit. The cadence diagnostic runs in `tools/batch_analyze` (writable), which
already loads the Score — so **fermata/phrase-boundary info is read there directly and passed into the
composing detector via a new IN-ZONE field on `CadenceRegionInput`. NO `src/notation`/`src/engraving` code
edit is needed for 4c-iii.** (The notation-bridge change to feed fermatas to the *live* resolver is the
later 4c-ii wiring step, separately authorized — not this run.)

Zone: `src/composing/` (the detector + its input struct) + `tools/` (read fermatas, build inputs, measure).
HELD — no commit. Key-agnosticism is still mandatory (see below). Tag every claim `[probe]`/`[code]`/`[oracle]`.

## The three refinements (each targets a diagnosed 4c-i failure mode)

1. **Structural-vs-interior discrimination — fermata-gated (targets the 308 V→III tonicizations).**
   Read fermatas/phrase boundaries from the Score in `batch_analyze`; add a `bool endsPhrase` (or a
   phrase-boundary tick set) to `CadenceRegionInput`. Weight cadences whose **resolution coincides with a
   phrase boundary** (a structural cadence) far above interior cadences. A diatonic V→III tonicization in
   the middle of a phrase should carry little/no vote; the phrase-final and piece-final cadences should
   dominate. (This is the primary fix — the relative-major tonicizations are overwhelmingly *interior*.)
2. **Raised-leading-tone salience — KEY-AGNOSTIC via the signature (targets the relative-major masquerade).**
   The discriminator between a true minor V→i and a diatonic V→III is the **chromatic** leading tone: in a
   0-sharp signature, E→Am needs G♯ (an accidental, OUTSIDE the diatonic collection) while G→C uses B (in
   the collection). Weight cadences whose dominant's leading tone is **chromatic relative to the key
   SIGNATURE fifths** (reliable per the Stage-4 premise) above purely-diatonic ones. **CRITICAL: use the
   signature fifths + pitch content ONLY — NEVER the resolved key/mode** (that is the circularity the whole
   approach exists to avoid). Pass the signature fifths into the detector as a parameter (key-agnostic-safe).
3. **Picardy handling (targets the 91 parallel-major misreads).** A minor piece often ends on a MAJOR
   tonic triad (Picardy third); the detector currently reads that major resolution as major mode. A
   Picardy-major *final* cadence must not flip the piece to major — detect the pattern (major tonic
   resolution that is the final cadence and/or contradicts the body's minor cadences) and resolve toward
   minor, or down-weight a lone major final against minor interior cadences.

Weights are provisional `[empirical — Stage-5 fits]` — explore principled values; do NOT corpus-fit to the
326-chorale gate (the overfitting guard from 4b-ii still stands).

## Re-measure (the deliverable — identical protocol to 4c-i)

Read-only diagnostic; production scoring untouched. Reuse `tools/cc_floor_classify.py` + the 4c-i harness.
Report, vs the 4c-i baseline (55.7% / 34%):
1. **Realized fraction `[probe][oracle]`:** correct-anchor % on the relative-pair floor (precision/recall),
   and the per-refinement contribution (which of the three moves the number, by how much).
2. **Clean-stem contradiction rate `[probe]`:** the % of already-correct mode-present stems the anchor now
   contradicts — this must drop **well below the 34%** that blocked wiring (it is the mode-present-regression
   proxy; it is the binding constraint for 4c-ii, more than the raw accuracy).
3. **Per-target `[oracle]`:** bwv365, bwv33.6, bwv64.2 (all relative-major misses in 4c-i — do the
   refinements recover them?); bwv83.5 (must stay correct Dmin, not spuriously claimed).
4. **Residual `[probe]`:** what still misses, and whether it's interior-cadence noise (more discrimination)
   vs genuinely cadence-less / different-key (→ Stage 6 / B).

## Byte-identity gate (unchanged from 4c-i)
Detector still diagnostic-only; the resolver/winner never calls it. **BIR 57/23/57, snapshots 11/11
zero-diff, suites green.** Any movement = the detector leaked into scoring = STOP.

## Held / report — `cc_stage4c_iii_report.md`
The three refinements at source (key-agnostic inputs re-confirmed: signature-fifths + fermata + pitch
content, NO resolved mode), the re-measured realized fraction + clean-stem contradiction vs 4c-i, per-target,
residual, byte-identity proof. **Branch recommendation:** contradiction low + accuracy worthwhile ⇒ proceed
to 4c-ii wiring (the bar is primarily the contradiction rate); still short ⇒ report what's left (further
refinement vs the key-axis A-vs-B / Stage-6 reassessment). Every number `[probe]`, every root `[oracle]`.
HELD — no commit.

## Stop conditions
- Any `src/notation`/`src/engraving` **code edit** appearing necessary (reading the Score in `batch_analyze`
  is NOT an edit; but if a bridge/engraving *code change* seems required even for the measurement, STOP and
  surface it — it shouldn't be).
- Key-agnosticism broken — the raised-LT/structural logic using the resolved key/mode instead of signature
  fifths + pitch content + fermata. That reintroduces the circularity; STOP.
- Production behavior change (gate/snapshot/suite movement) — the detector leaked into scoring; STOP.
- Realized fraction / contradiction still failing the bar after all three refinements — report as the
  detection-reliability finding (further work vs key-axis A-vs-B / Stage-6); do NOT wire a sub-bar detector.
