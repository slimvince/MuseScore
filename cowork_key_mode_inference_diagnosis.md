# Why does our key/mode inference not work? — the diagnosis opening

> **Cowork, 2026-07-12.** The Premise-Gate opening for the register row OI-141, as
> reframed by the user: *"We should understand why our key/mode inference does not
> work."* This document records the candidate causes and a written quantitative
> prediction for each BEFORE the diagnostic measures anything (CLAUDE.md #17). The
> diagnostic itself is read-only; any fix follows later, in the key layer, at its
> proper stage. Predictions are Cowork's grounded estimates, written to be checked,
> not to be right.

## 1. What is already fact

- The isolated key/mode check exists and is established: key agreement against the
  DCML ground truth is **68.13 / 64.43 / 67.50 %** of graded duration
  (Baroque/Jazz/Default — the ratified baselines). The failing mass to explain is
  the remaining **~32 / 36 / 32 %**.
- In the failing regions, the ground-truth key is PRESENT in the carried
  candidate-key list (`keyAlternatives`) for **66.7 / 61.6 / 64.1 %** of regions and
  ABSENT for the rest (`tools/reports/mode_key_chord_probe.json`). The list carries
  no usable per-candidate confidence (populated on 2 of 25,864), and the runner-up
  closeness is computed then discarded (rows OI-75/OI-81).
- Chord ROOTS cannot separate relative keys — measured inert (the OI-43 probe):
  same pitch collection, same roots. FUNCTIONAL evidence can: a V–i cadence in the
  relative minor contains the leading tone (a note outside the relative major's
  set); phrase-final dominants and cadence placement are the published
  discriminators. The built-but-gated chord→key coupling term (`decideJointKey`)
  and the certified dormant layer-5 cadence/modulation machinery already point at
  this channel.
- Known key-layer facts from the certified audits that are candidate contributors:
  a mid-piece NOTATED key-signature change is not re-anchored (row OI-94); the
  declared mode is siloed to the key path (row OI-78); the mode priors and
  emission weights are hand-set, unfit (row OI-91); the relative-key hysteresis
  margin is a soft value-copy (row OI-97).

## 2. The candidate causes, each with its written prediction

Every key-disagreeing run of duration gets exactly one primary cause label. The
predictions are duration-weighted shares OF THE FAILING MASS, per preset; ranges are
deliberately wide — the point is falsifiability, not precision. If the measured
share falls outside its range, that prediction FAILED and says so in the report.

- **Relative-key confusion** — right pitch collection, wrong tonic/mode among the
  collection siblings (C major chosen where A minor is true, or the reverse).
  PREDICTION: the largest single class, **35–50 %** of failing duration.
- **Tonicization-versus-modulation boundary** — we commit a local key change where
  the ground truth stays home (or the reverse); the note-identical judgment-call
  class the cross-layer caveat names. PREDICTION: **15–30 %**.
- **Parallel-mode confusion** — same tonic, wrong mode (C major versus C minor).
  PREDICTION: **5–15 %**.
- **Wrong neighborhood** — the true key absent from the candidate list AND not a
  collection sibling of anything carried: late anchoring after a real modulation,
  the un-re-anchored notated key change (row OI-94), over-wide segmentation.
  PREDICTION: **10–25 %**.
- **Segmentation-edge artifacts** — short wrong-key runs at region boundaries where
  our segmentation and the ground truth's disagree about WHERE the key changes,
  not WHETHER. PREDICTION: **5–15 %**.
- **Enharmonic/spelling** — the same sounding key spelled differently.
  PREDICTION: under **5 %**.

Two cross-cutting predictions:

- **The present-but-outranked share:** of the failing duration, the true key is
  carried in the candidate list but outranked in **55–70 %** (the region-wise
  two-thirds, expected to hold duration-wise).
- **The unused-evidence test (the cheapest test of the user's chord-hints
  thesis):** among relative-key-confusion regions where the true key is the MINOR
  sibling, the leading tone of that minor key (its raised seventh — a note outside
  the shared collection) is actually PRESENT in the region's notes in **at least
  60 %** of the failing duration. If this holds, decisive note-level evidence
  exists inside the regions and our emission scoring is not using it — the
  strongest possible case that better evidence use (not more candidates) fixes the
  dominant class. If it fails, within-region evidence is genuinely insufficient
  and the remedy must be contextual (cadences, phrase structure, progressions).

## 3. The method (read-only, the dispatch executes it)

1. Desk simulation first: 3–5 real cases where the true key is absent from the
   candidate list, hand-traced at the score — is the absence a beam-width fact, a
   hysteresis fact, a late anchor, or a segmentation fact?
2. A classifier over the existing dumps and the ground truth: every
   key-disagreeing run labeled with exactly one primary cause from the closed list
   above, plus the carried/absent and outranked flags and the leading-tone
   presence test. No new production output surface — read what is already dumped.
3. Establishment before reading results: the classifier's totals must reconcile
   exactly with the established key-agreement column (classified failing duration
   equals the reference failing duration, per preset), and grading coverage is
   reported beside every figure (the abstention caveat, row OI-33).
4. The report answers every prediction above: met, failed, with the numbers.

## 4. What follows (not now)

The dominant measured cause selects the targeted research question (#2 — specific
over general): if relative-key confusion dominates and the leading-tone test holds,
the research target is leading-tone- and cadence-aware key scoring; if the
tonicization boundary dominates, the target is the ground truth's own convention
and our local-modulation gating; if wrong-neighborhood dominates, the target is
anchoring and beam width. Any build lands in the key layer at its proper stage,
under the certified-layer discipline and the entry-gate ordering.

*Cross-references: OI-141 (the question, user-framed), OI-75/OI-81 (discarded
ranking facts), OI-94/OI-78/OI-91/OI-97 (key-layer audit facts), OI-33 (abstention
caveat), `tools/reports/mode_key_chord_probe.json` (containment),
`cc_mode_key_chord_probe_report.md` (the probe this follows).*
