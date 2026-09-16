# CC Instruction: cadence-instrument precision investigation — can it be fixed key-agnostically, and does it unblock 4d?

## Authorization + framing

4d-i proved the local-modulation detector's logic is sound (recall 9.7%→33.4%) but its **precision is
capped by the cadence instrument** — ~70% of the modulation false-positives are upstream cadence noise:
**43.3% dominant/subdominant** (the cadence detector reads I→IV / V→I-of-X tonicizations as cadences =
the deferred "#4 guard") + **27.5% relative-pair** (the cadence anchor picks the wrong relative
major/minor — right only 72.4%). The cadence instrument is the **shared bottleneck** (it feeds modulation
detection, tonicization-vs-modulation labeling, AND the relative-pair floor), so its precision is the
highest-leverage work.

**This run INVESTIGATES — read-only, no build, no commit.** Before building any cadence-precision fix,
DERIVE whether a **key-agnostic** discriminator can separate these false cadences from true ones, the
**achievable precision ceiling**, and — the real test — **how much it would lift the 4d-i modulation
precision**. A negative result (precision not fixable key-agnostically) is a valid, valuable finding.
Reuse the committed cadence diagnostic + the 4d-i modulation diagnostic + the existing measurement scripts.
Tag every claim `[probe]`/`[code]`/`[oracle]`.

## The two false-cadence classes — derive a key-agnostic discriminator for each

1. **Dominant/subdominant tonicization misreads (43.3% — the primary lever).** The detector's
   descending-fifth test (`root_b ≡ root_a − 7`) fires on I→IV (e.g. C→F) and other within-key
   dominant-relations, and the leading-tone test passes because the relevant tone is **diatonic**
   (E is F's LT but is in C major). **Candidate discriminator: require the cadence's leading tone to be
   CHROMATIC vs the notated signature** (an accidental — the same signature-relative test 4c-iii already
   computes for salience, here as a per-cadence GATE) — a real secondary-dominant/modulation cadence to a
   non-home degree carries a chromatic LT; a within-key I→IV / V→vi does not. **Derive its coverage AND
   its asymmetry honestly:** dominant-direction modulations (to V) DO carry a chromatic LT (good); but
   **subdominant-direction modulations (to IV) carry NO chromatic signal** — they are genuinely
   indistinguishable from I→IV by this test. Quantify: of the dom/subdom FPs, how many a chromatic-LT gate
   removes, how many true subdominant cadences it would wrongly drop (recall cost), and what residual it
   leaves. Note other key-agnostic signals if the chromatic test under-covers (bass leap, metric position).

2. **Relative-pair anchor errors (27.5% — the recurring hard problem).** The cadence anchor mis-picks the
   relative major/minor of the resolution (right only 72.4%) — the same relative-pair decision that
   defeated 4b-ii reweighting. Characterize these: is there a key-agnostic signal that fixes the anchor's
   relative pick (e.g. the resolution chord's own quality major-vs-minor, the raised-LT presence), or is it
   the same structural relative-pair ceiling? Be honest if it's the latter.

## Measure — the achievable ceiling + the DOWNSTREAM unblock [probe][oracle]

1. **Cadence precision lift:** applying the derived discriminator(s), what is the cadence instrument's
   precision before→after, and the recall cost? (Reuse the 4c diagnostic.)
2. **★ The real test — modulation-precision lift:** re-run the 4d-i modulation measurement with the cadence
   FPs filtered by the proposed discriminator (simulate the improved cadence input). Does the modulation
   detector's precision (47%) rise toward a **wireable** level, and at what recall? This is what decides
   whether the cadence-precision work actually unblocks 4d-ii.
3. **Ceiling honesty:** state the realistic combined precision ceiling and the irreducible residual (the
   subdominant-direction modulations + the relative-pair structural floor) that a key-agnostic cadence fix
   CANNOT reach — that residual is the next-layer / learned-model evidence.

## Deliverable — `cc_cadence_precision_investigation_dossier.md`
Per-class FP characterization; the derived key-agnostic discriminator(s) + honest coverage/asymmetry; the
cadence-precision lift; the **simulated downstream modulation-precision lift** (the unblock test); the
irreducible residual. **Recommendation:** clear achievable lift that unblocks 4d-ii ⇒ build the
discriminator (measure-first, separate instruction); precision ceiling too low ⇒ report it as the finding
(the key-agnostic cadence approach is precision-limited → the residual needs a different layer / richer
model). READ-ONLY — no build, no commit, no production/metric change.

## Stop conditions
- Drifting into BUILDING the discriminator (this run derives + simulates only).
- The discriminator needing the resolved key (it must be key-agnostic — notated signature + pitch content
  + cadence structure only).
- The simulated modulation-precision lift being marginal — report honestly; do NOT recommend a build that
  won't reach a wireable precision (the 4d-ii precision-lean still governs).
