# Cowork independent audit — sectioncadencedetection (to reconcile with CC)

> Second-opinion pass from the committed-object source (HEAD). Correctness judged vs the TRUE analysis
> (what an analyst would label), not the gate. Reconcile with `cc_audit_sectioncadencedetection_report.md`.

## Responsibility
`detectCadences` (PAC/PC/DC/HC markers) + `detectPivotChords` (pivot labels) + `hasAssertiveKeyConfidence`
(a ≥0.8 confidence gate). This is the **key-DEPENDENT cadence/pivot annotation for DISPLAY** — it reads
`function.degree` + `keyModeResult` (the *resolved* key). **Distinct responsibility from `cadencekeyanchor`**
(key-AGNOSTIC, for key INFERENCE): different input (resolved key vs key-agnostic), output (display markers vs
anchor), and position (downstream vs upstream). **So the "two cadence detectors" is NOT redundancy** — they
serve different layers. (Phase-2 note: the V→I *detection logic* is nonetheless duplicated in concept; a
shared cadence primitive with key-agnostic vs key-dependent wrappers is a possible decomposition.)

## Correctness gaps (vs the true label)
1. **[correctness · display] PAC conflates PAC with IAC.** It labels *any* V→I (`b.deg==0` & `a.deg==4`
   non-minor, or viio→I) as **"PAC"** with **no inversion / soprano check** — but a Perfect Authentic Cadence
   requires root-position V & I and tonic in the soprano. Inverted or non-tonic-soprano authentic cadences
   (IACs) are mislabeled "PAC." There is no IAC label at all → every authentic cadence is reported as PAC.
2. **[correctness · display] HC ignores phrase boundary.** It labels the **last in-selection region** "HC" if
   it is degree 4 — a half cadence is specifically a *phrase* ending on V. A non-phrase-final dominant at the
   selection edge is mislabeled HC; HCs not at the selection end are missed. (Contrast: `cadencekeyanchor`
   *does* carry an `endsPhrase` phrase-boundary signal — available but unused here.)
3. **[correctness · display] DC is major-key only.** Deceptive requires `b.quality==Minor` (V→vi) → it misses
   the **minor-key deceptive V→VI** (a major submediant). 

## Completeness gaps (vs the cadence-type space)
4. **[completeness · display] Incomplete vocabulary:** no IAC, no Phrygian half (iv6→V), no minor-key
   deceptive, no evaded cadence. Covers only PAC(+IAC-as-PAC) / PC / DC(major) / HC.
5. **[completeness · display] The ≥0.8 confidence gate silences uncertain regions.** Both detectors require
   `hasAssertiveKeyConfidence` on every region → **NO cadence/pivot is emitted on low-confidence (floor /
   near-tie) regions.** Exactly the blind spot the `cadencekeyanchor` header calls out for the OLD detector —
   it persists here. A genuine cadence in an uncertain passage is invisible.

## Phase-2 carry-forward
- **Two cadence detectors** (inference / display) = distinct responsibilities, but shared detection concept →
  possible common primitive (decomposition).
- **The ≥0.8 confidence-gate blind spot is CROSS-CUTTING** (here + the old detector + KeyArea grouping) — an
  architecture-level pattern: confidence-gating systematically silences the uncertain cases, which are the
  ones that most need analysis. Worth a phase-2 finding.
- **Correctness is upstream-bounded:** this layer consumes the resolved key/degree, so its display correctness
  inherits every key-inference error — a dependency note (its obligations are downstream of the key axis).

## Reconciliation targets (for CC's empirical audit)
- Quantify PAC-mislabel rate (authentic cadences that are actually IAC) + HC false/missed vs phrase boundaries.
- Measure how many true cadences fall in <0.8-confidence regions (the gate blind spot).
- Confirm the two-detector responsibilities are genuinely distinct (agree/disagree on the decomposition note).
