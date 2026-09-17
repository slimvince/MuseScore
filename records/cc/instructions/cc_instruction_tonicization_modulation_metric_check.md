# CC Instruction: metric check — does `compare_rn` over-penalize the tonicization↔modulation equivalence?

## Authorization + framing

6-tonic-i found a raw 78% false-label rate against DCML, of which **91.8% is the tonicization-vs-modulation
notation boundary** (409/427: our tonicization target degree == DCML's local tonic — same harmonic event,
two notations). Before committing to BUILDING the tonicization-vs-modulation discriminator, the user wants
this **quantified**: how much of that gap is a **metric artifact** (the metric penalizing a defensible
equivalent notation) versus a **real output-quality problem** (cases where DCML's modulation is genuinely
correct and our tonicization notation is wrong). That ratio decides whether — and how much — the
discriminator is worth building.

**READ-ONLY metric-design investigation.** No production change, no metric change, no commit. Reuse
`compare_rn` + the 6-tonic-i diagnostic + the committed cadence instrument as analysis inputs. Tag every
claim `[probe]`/`[code]`/`[oracle]`. Deliverable: `cc_tonicization_modulation_metric_dossier.md`.

## The crux to resolve

For each of the ~409 "we say tonicization `V/d`, DCML says modulation to local key d" cases, is our
notation a **defensible equivalent** (a brief tonicization — either notation valid) or is DCML's modulation
the **correct** analysis (an *established* local key we are mis-notating as a passing tonicization)? The
split is the answer:
- **brief / either-valid** ⇒ **metric artifact**: the metric over-penalizes; crediting the equivalence
  recovers it WITHOUT the discriminator.
- **sustained / modulation-correct** ⇒ **real output gap**: our output genuinely should say "modulation",
  and the discriminator is warranted for exactly those.

## Tasks

1. **How `compare_rn` scores these now [code][probe].** Read `compare_rn`/`classify_pair` at source: when
   our RN is `V/d` (home key) and DCML's is `V` or `I` in local key d at the same tick, what does the
   comparator return — miss / partial / credit? Does it normalize across the reference-key difference at
   all? Quantify the score impact of the 409 cases on the headline number.

2. **Characterize the 409 by local-key establishment [probe][oracle].** For a representative sample (and
   aggregate where feasible), classify each as **brief tonicization** vs **established modulation** using
   objective signals: the DCML local-key SPAN DURATION (how long DCML stays in d), whether DCML places a
   CADENCE confirming d (use the committed cadence instrument + DCML's own cadence annotations if present),
   and the number of chords in the local key. Report the split: what fraction are brief (our notation
   defensible) vs sustained (DCML's modulation correct, our `V/d`-everywhere is wrong).

3. **Size the two buckets [probe].** (a) **Metric-artifact** fraction = brief/either-valid → recoverable by
   crediting the equivalence in the metric (no discriminator). (b) **Real-output-gap** fraction =
   sustained/modulation-correct → the discriminator's actual value. Combine with the already-measured 6.4%
   genuine plain-diatonic FP + the inversion recall gap to give the corrected picture of where the S1
   headroom really is.

4. **The crediting rule, if warranted [code/probe].** If a large metric-artifact bucket exists, sketch
   what a fair `compare_rn` crediting rule would be (e.g. `V/d` in home key ≡ `V` in local-key-d when the
   targets match) — DESIGN ONLY, do not change the comparator this run. Note any false-equivalence risk
   (cases where crediting would wrongly mask a real error).

## Deliverable — `cc_tonicization_modulation_metric_dossier.md`
The comparator's current behavior on these cases; the brief-vs-sustained split (the headline); the
metric-artifact vs real-output-gap sizing; the corrected S1 headroom; and a **recommendation**:
- mostly metric artifact ⇒ the discriminator buys little — credit the equivalence (a metric refinement) +
  wire the sound predicate; OR
- substantial real-output gap ⇒ the discriminator is warranted, sized to that bucket.
Every number `[probe]`, every root `[oracle]`. READ-ONLY — no commit, no production/metric change.

## Stop conditions
- Drifting into BUILDING the discriminator or CHANGING `compare_rn` — this run only quantifies and
  recommends; both are separate ratified steps.
- The brief-vs-sustained classification needing a signal that doesn't exist in-zone (DCML spans + cadence
  instrument + region durations should suffice) — if a needed signal is genuinely absent, report it as a
  finding rather than guess the split.
