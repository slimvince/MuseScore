# OI-178 adoption measurement — the adoption record (measurement only; no adoption act)

**CC, 2026-07-26.** Dispatch `cc_instruction_adoption_measurement.md` (Cowork 2026-07-20, at the user's
**★R = A1** ruling). This executes the OI-178 robust-stop architecture-adoption protocol's **measurement
phase**: A decodes the full covered corpus **from its own fact adapter (the production path)**, is graded
on the robust unit against the committed `tools/robust_stop/` reference per preset, and every PASS
condition (as amended ★R=A1) is evaluated. **No adoption act, no re-baseline, no golden refresh, no
production wiring** — this produces the record for the user's ratification.

Every figure below is read from the generated dossier (#17f): `tools/joint_estimator/adoption_record.json`
(+ `adoption_record_summary.txt`, the readable summary) and `adoption_setdiff.json` (the complete
set-diff). Nothing is hand-computed.

---

## 0. Method and the firewall (grep-proven)

- **Decode = the production path.** A's Pieces are built from the C++ fact adapter's own extraction
  (`adapter_facts.json`, the `composing/analysis/joint/jointfactadapter` dump), decoded by the pinned
  `probe_decoder.decode_piece` at the **direct-metric SELECTED all-326 weight vector** (`random07`,
  R_train 0.477130 — the exact vector `decode_parity_ref.selected_weights` carries), the ratified **§5
  tie-break** (inside the decoder), seg_cap 4, leftover 2a, `table_set="all"`.
- **Grading = the retained chain, reused verbatim.** `probe_run.decode_to_regions` →
  `probe_run.grade_regions` → `a8_rebaseline_measure.build_piece_grid` vs `dcml_parser.load_wir_regions`.
  The per-preset run enumeration + class-(a)/(b) split + set-diff is the pinned **a8 + robust_stop_diff
  R10 sandwich**, run over A's decode rendered as a candidate corpus (the ratified pattern). Pooled
  columns + piece-bootstrap = `fit_run`; modulation = `search_run`.
- **The firewall.** The only decoder input is the frozen selected weight vector; nothing here fits,
  tunes, or feeds a value back. The instruments are import-only; no `src/`, no build, no golden, no
  `tools/robust_stop/` re-baseline, no `tools/corpus/` mutation.

## 1. Establishment (#19) — both checks PASS

- **The Python-from-adapter decode reproduces the C++ production decode EXACTLY.** Cross-language decoder
  parity is 326/326 on identical input (Task A); the adapter Piece is that identical input. The
  observable: the divergent-vs-note-events-oracle stem set is **byte-identical to `joint_endtoend_parity`'s
  C++-from-adapter set** — the same ten pieces `{bwv113.8, bwv261, bwv274, bwv276, bwv284, bwv380,
  bwv383, bwv384, bwv4.8, bwv48.3}` (the OI-184 reader-skew class, option-1 accepted). So this
  measurement IS the production path's output.
- **The current-system per-piece grading reproduces the committed manifest ROOT column exactly**
  (baroque 66.04 vs 66.0406, jazz 64.98 vs 64.983, default 65.93 vs 65.9307) — the paired-CI baseline
  arm is established.
- a8's self-validation (`build_piece_grid` variant-(b) buckets == `grid_score_regions` byte-for-byte)
  passed on every covered piece at generation.

## 2. ★ THE PASS-CONDITION TABLE (OI-178 as amended ★R=A1) — ALL PASS

| condition | verdict | detail |
|---|---|---|
| **(i) key-LOCAL exceeds baseline beyond CI, every preset** | **PASS** | A−current +12.37 [+10.57,+14.19] B / +15.37 [+13.55,+17.21] J / +12.63 [+10.82,+14.41] D — every interval excludes 0 |
| **(i) root non-degrading** | **PASS** | A−current +11.0 / +12.1 / +11.1 (improves) |
| **(i) RN non-degrading** | **PASS** | A−current +17.8 / +20.0 / +17.9 (improves) |
| **(i-b) modulation-rate band [3.96, 6.60]** | **PASS** | A 6.07 changes/piece (GT measured 5.28) — inside the band |
| **(ii) class-(b) duration NET DECREASE, every preset** | **PASS** | −33.0% B / −34.7% J / −33.1% D; `robust_stop_diff` OVERALL PASS (rc 0) |
| **(iii) class-(a) tracked** | **PASS** | −13440 / −30720 / −18480 ticks (all decrease; no INVESTIGATE) |
| **(—) key-abstain reads zero (A commits MAP)** | **PASS** | b_key_fail 0 on every preset (OI-33 flag zero, as required) |
| **(iv) user ratification** | **PENDING** | this record is the input to that ruling — no adoption act here |

**The columns** (A from the adapter, all-326 selected, vs the committed current-system baselines B/J/D):

| axis | A (all-326) | current B / J / D |
|---|---|---|
| key-LOCAL | **78.42** | 65.99 / 62.98 / 65.71 |
| key-HOME | 56.14 | 71.42 / 67.83 / 70.65 |
| root | **77.03** | 66.04 / 64.98 / 65.93 |
| RN | **64.12** | 46.33 / 44.10 / 46.23 |

## 3. Prediction-versus-measured (Cowork's #17b bands, recorded before measuring)

| axis | predicted | measured (B / J / D) | verdict |
|---|---|---|---|
| class-(b) duration | NET DECREASE 10–30% | −33.0% / −34.7% / −33.1% | decrease **exceeds** the band (favorable) |
| key-local delta | +8 … +13 | +12.4 / +15.4 / +12.6 | held (jazz +15.4 slightly **above**, favorable) |
| key-home delta | −12 … −18 | −15.3 / −11.7 / −14.5 | held (jazz −11.7 slightly less negative, favorable) |
| RN delta | +12 … +16 | +17.8 / +20.0 / +17.9 | **exceeds** the band (favorable) |
| root delta | large (carried as known) | +11.0 / +12.1 / +11.1 | as expected |
| modulation | within the ★R band | 6.07 in [3.96, 6.60] | held |

**Every band deviation is in the FAVORABLE direction** — A performed at or slightly above prediction on
each axis. Flagged per the discipline (a band deviation is reported prominently); none is a regression or
an inverted mechanism (contrast OI-187). The large root/RN improvement was pre-declared as known
(the architecture's asymmetric expectation, reviewed at the probe stage).

## 4. ★R — the key-HOME decomposition against the GT self-agreement ceiling

- **Ceiling = 59.27 %** — the fraction of A's graded duration where the ground truth's own LOCAL key
  equals its HOME (global) key. This is the maximum key-HOME agreement a **perfect local-following
  decoder** can reach; the complement, 40.73 %, is duration where the music has modulated away from home.
- **A's key-home = 56.14 %**, just below the 59.27 % ceiling — A is a good-but-imperfect local follower.
- **The current system's key-home (71.42 / 67.83 / 70.65) sits 12–15 points ABOVE the ceiling.** A
  system scoring above the local-follower ceiling on the home column is achieving it by **under-following
  modulation** — staying in the home key where the music has left it. The gap is far beyond any grid
  effect. This is exactly the ★R=A1 argument the amended condition rests on: the home column rewards the
  very defect A exists to fix, so it is TRACKED (with this decomposition) rather than a PASS axis, and the
  never-modulate failure it would have guarded is guarded directly by the modulation-rate band (i-b),
  where A (6.07) sits closest to the GT (5.28) of any arm.

## 5. The run-level set-diff and the added-class-(b) diagnosis

As predicted, the set-diff is **LARGE in both directions** — A re-segments wholesale, so run identities
(keyed by start tick + roots) move en masse; the aggregate criterion (net class-(b) duration decrease) is
the ratified hard stop for exactly this event. Per preset (baroque shown; jazz/default within a few runs):

- runs: reference 6506 → candidate **4547**  (**+3688 / −5647**)
- added class-(b) 3474 (dur 1 442 040); **removed class-(b) dur 2 319 520**; class-(b) net **−896 720
  ticks (−33.0 %)**.
- **A grades slightly MORE duration than the reference** (scored 8 300 640 vs 8 293 680), so the net
  decrease is genuine better inference, not a coverage artifact (`robust_stop_diff` also independently
  confirms WiR coverage 326 = 326, no shrink).

**Every added class-(b) run is classified by its mechanical signature** (root-interval class × A-local-key-
correct? × churn-vs-genuine-new) in `adoption_setdiff.json`'s `diagnosis_buckets`; **none is
undiagnosable.** The subset that warrants scrutiny — **GENUINE-NEW** class-(b) runs, where the current
system was root-correct and A is wrong — is enumerated individually:

- **1474 genuine-new class-(b) runs, dur 671 880 ticks** (baroque; ~8 % of the current system's class-(b)
  failure duration). The other ~770k ticks of added class-(b) are **churn** — both systems fail, only the
  boundary moved.
- **Diagnosis:** 70 % (1033) are root errors with the LOCAL KEY CORRECT; the dominant interval is a
  **FIFTH (506) + its inverse the fourth (176) = 46 %** — the classic functional substitution (A reads
  the dominant/subdominant root where the ground truth reads the tonic, or vice versa), the signature of
  the chord-transition/bass factor. Relative/third confusions (major-sixth 165, minor-third 129) and the
  key-wrong subset (441, 30 %) account for the rest. The largest are all "fifth, key-right"
  (`bwv123.6@31680` 11→6, `bwv382@5760` 9→4, `bwv375@6000` 2→9).

**This is a FINDING, surfaced not built around (declared to Cowork).** A's improvement is a strongly
favorable NET trade — it removes ~2.32M ticks of class-(b) root error and introduces ~0.67M ticks of new
error, net −33 %. The genuine-new subset is dominated by fifth-apart functional root substitutions with
the key correct — an inference-behavior observation about the chord-transition/bass factor, a natural
candidate for the OI-180 retirement-map's fitted-transition refinement. It is not a STOP: the aggregate
hard stop passes strongly, every added run is diagnosed, and no run is inexplicable.

## 6. Timing (the tractability record) and provenance

- **Decode: mean 3.285 s / max 18.021 s / total 1071 s** for 326 pieces (Python, production scale;
  the C++ production decoder ran the same at mean 4.59 s, `joint_decode_parity.json`).
- Instrument `020baca347`; corpus `e3d17c325d`; O-12 snapshot at
  `tools/robust_stop/snapshot_2026-07-26_pre_oi178_adoption/` (byte-identical copy of the outgoing
  reference; **no re-baseline occurred**).

## 7. What the adoption commit WOULD contain (for the user's ruling; NOT executed here)

- The wiring point: A becomes the inference-layer key/mode/chord estimator; the analysis is
  **preset-independent at the inference layer** (the ratified mode decision) — presets stay presentation
  concerns.
- The re-baselined `tools/robust_stop/` reference (a8 re-run over A's decode; the set-diff explained and
  ratified; the manifest re-stamped via `robust_stop_restamp.py`; the O-12 snapshot already taken).
- The OI-180 retirement map's first steps (each its own later verified increment).
- One revertible, provenance-stamped commit; suites + pipeline snapshots refreshed only if adoption
  changes committed output.

## 8. Verdict

**Every OI-178 PASS condition (as amended ★R=A1) holds**, with the establishment proven, the key-home
decomposition explaining the tracked column against its ceiling, the modulation rate closest to the
ground truth of any arm, and the class-(b) hard stop passing by −33 % on every preset. The one substantive
finding — the genuine-new fifth-substitution subset — is fully diagnosed and surfaced as the honest cost
side of a strongly favorable trade. **The funnel returns for the user's adoption ruling; nothing is
adopted in this dispatch.**
