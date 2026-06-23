# Layer 3 — KEY/MODE — IMPLEMENTATION DESIGN (for user sign-off → CC instructions)

> The L3 key/mode design is **signed** and **audited** (`cowork_layer3_keymode_design.md`,
> `cc_layer3_keymode_audit_dossier.md`). This doc sequences the **build** into increments and pins the
> implementation decisions, so each increment becomes a focused CC instruction. **L3 changes analysis behavior** —
> validated by the direct key/mode-vs-ground-truth metric (held-out) + the oracle KEY tier + dual-preset BIR, not
> byte-identity.
>
> **Vocabulary:** key/mode (`C-major`, `F-mixolydian`); chord symbol (`Bm7`); function (`V/V`). L3 = **key/mode
> only**, from **pitch-class content + tonic emphasis** (the cadence-free `KeyModeAnalyzer`); modulation/passing
> keys from the **path's transition penalty**; NO cadence/function (gated Stage 5).

## §0 — Build sequence (three increments, upstream-first within L3)
1. **Increment A — the L1 query indexing fix (BYTE-IDENTICAL prerequisite).** `NoteModel::overlapping`/`onsetIn`
   are O(N) per call → O(N²) over slices (audit, `note_model.cpp:141-176`). The per-slice path calls them per slice,
   so this is fatal at full-act scale (R1). Fix the query to indexed; **output identical** (a pure perf fix). Done
   first because it unblocks everything and carries **zero behavior change** (a clean, low-risk start).
2. **Increment B — the held-out ground-truth harness (READ-ONLY diagnostic).** The direct key/mode-vs-RN metric
   with a **held-out split**, the unambiguous/ambiguous classification, per preset. Built BEFORE the rebuild so the
   rebuild is graded against the §6 done-criterion. Production byte-identical (diagnostic only).
3. **Increment C — the key-path decoder (the behavior-changing rebuild).** Replace the per-region key argmax with a
   per-slice **key/mode path** (emission = `KeyModeAnalyzer`, transition = key-distance + self-transition penalty),
   wired into the live pipeline. This is the layer's substance; it moves the metric.

Each increment: its own CC instruction, its own gate, committed + verified + ratified before the next.

## §1 — Increment A: L1 query indexing (byte-identical)
**Problem:** `overlapping(t0,t1)` / `onsetIn(t0,t1)` scan `m_notes` from the head (bounded only at the top by the
first onset ≥ t1) → O(N) per call. **Fix:** index the onset-sorted `m_notes` so a query is O(log N + result):
- `onsetIn(t0,t1)` is trivial — binary-search the onset-sorted vector for `[t0, t1)` (both bounds).
- `overlapping(t0,t1)` is the harder one (a note with `onset < t0` can still overlap if `release > t0`). Options
  (pick in the impl, confirm at source): **(a)** an auxiliary **max-release interval index** (e.g. an interval
  tree, or the onset-sorted array augmented with a running `maxReleaseUpTo` + a release-sorted secondary index);
  **(b)** a **segment/bucket index** over ticks. Lean: the augmented onset-sorted structure (built once in
  `NoteModel::build`, O(N log N)), giving O(log N + result) queries.
- **It is an L1 amendment in the proper layer** (the query *implementation*), but **byte-identical**: L1's output
  contract is unchanged; only the query is faster.
**Gate:** the indexed query returns **identical results** to the linear scan on every `nm_*`/`slicer` fixture AND on
the full corpus (a property test: indexed == linear for random ranges on all 353 stems); both suites + snapshots +
BIR/oracle **byte-identical**; a performance check (per-query and per-stem time) showing O(N²) → ~O(N log N).

## §2 — Increment B: the held-out ground-truth harness (read-only)
Build the **direct key/mode-accuracy** measurement (design §6), as a read-only diagnostic (production byte-identical):
- **Extract ground-truth key/mode per location** from the RN corpora — DCML `localkey`/`globalkey` and/or music21
  `RomanNumeral.key`. Reuse `compare_rn`/`dcml_parser` (audit: confirm they surface the local key/mode; resolve the
  global+local into an absolute key/mode per tick).
- **Unambiguous vs ambiguous split:** unambiguous = the sources **concur** (the DCML ∧ music21 policy-A analogue);
  ambiguous = differ. Report the corpus split (sizes the bar).
- **Held-out split:** a fixed train/test partition (out-of-sample; the Contrapunctus discipline). Tune on train,
  report on test. (Address the audit's "no held-out split yet".)
- **The metric:** per slice/event, per preset — full (tonic+mode) match on unambiguous; on ambiguous, "ground truth
  among L3's ranked alternatives OR L3 flagged ∧ annotators disagreed." Report against the **done-criterion** (§6).
- **Fix the audit caveats:** enumerate and repair the Jazz 39% key-parse-fail before trusting Jazz numbers; replace
  the single-source unambiguous proxy with the true two-source concurrence where the data allows.
**Gate:** read-only (production byte-identical); reproduces the audit baseline (~85.5%/91.5% unambiguous) as a
sanity check, now on the held-out split + with Jazz parse fixed; documents the split + the metric precisely.

## §3 — Increment C: the key-path decoder (the rebuild)
**Emission (reuse).** Per slice, `KeyModeAnalyzer::analyzeKeyMode` over a **window** = the slice + its look-around
(§0.2 R3 context), → a score per (tonic × mode) candidate (the cadence-free 252-candidate scorer, kept). Prune to
**top-K** per slice for tractability (beam).
**State + transition (new).** States = key/mode candidates. Transition cost = **key-distance** (circle-of-fifths /
relative-pair aware) + a **self-transition bonus** (stay in the current key) — the principled replacement for the
hand-tuned hysteresis; it is what makes modulation cost evidence and **passing keys not switch unless sustained**.
**Decoder (new, dedicated).** A **Viterbi/beam over the slice sequence** — `ChordPathDecoder` is chord-specific and
NOT reusable (audit), so a **dedicated key-path decoder**. Linear in slices ⇒ R1/R2-compatible. Lean: beam (bounded
state) for incrementality.
**Output (the §1 contract).** Per slice: the chosen key/mode + **ranked alternatives + confidence** + a **flagged
residual** marker (relative/modulation) — so L4 reads a confident prior and the gated Stage-5 step resolves the rest.
Confidence from the path (margin between the best and runner-up paths), not just the per-slice sigmoid.
**Context extension (R3).** The look-around window per slice; the **lazy backward extension** until the key area
stabilizes (the §0.2 demand→supply protocol). Pin the cap + stop criterion here.
**Passing keys / modulation.** Fall out of emission + self-transition penalty; optional **multi-timescale
(keyscape) persistence** check as a refinement (a key that survives only at a fine window is passing). No cadence.
**Wiring.** Replace the per-region `resolveKeyAndModeRanked` argmax (regionanalyzer) with the per-slice path. This
**changes output** (not byte-identical). Keep the path **revisable** so the gated Stage-5 joint feedback can later
refine the residual.
**Gate:** the §4 metric set; snapshot goldens refresh **only after verified-correct**; full branch coverage; the
direct ground-truth metric (Increment B) used **directionally** (rotation/relative-pair defects should drop —
provisional, not a fixed bar, §4); dual-preset BIR no-regression hard stop.

## §4 — Metric / gates (Increment C — the behavior-changing one)
> **★ METRICS ARE PROVISIONAL — grade DIRECTIONALLY, not against a fixed bar (user, 2026-06-22).** The Increment-B
> baseline numbers (held-out Baroque 87.3% / Jazz 61.5%) **and the metric definitions** WILL move as the rest of the
> pipeline (L4–L6) is reconstructed/refactored. **Meaningful comparison happens only against the fully reconstructed
> pipeline**, not increment-by-increment. So Increment C is graded **directionally**: did it reduce the genuine
> **rotation/relative-pair defects** (wrong tonic on unambiguous, stable, major/minor cases) without regressing the
> safety net? It is **NOT** gated on "beat 87.3%/61.5%." Crucially, **distinguish a rotation DEFECT from a
> modal-GT LIMITATION**: ~69% of Jazz "misses" are perfect-fifth displacements where our reading is a *defensible
> modal* one (e.g. `G-mixolydian`) the major/minor ground truth cannot represent — those are NOT defects to optimize
> away (the done-criterion's "defensible-or-flagged on ambiguous", + the major/minor-GT scope caveat). Do not chase
> the major/minor GT on modal readings.
- **Directional primary: the held-out direct metric (Increment B)** as a *signal* — rotation/relative-pair defects
  on unambiguous major/minor cases should **drop**; report the move, not a pass/fail vs a fixed bar.
- **Safety net — Oracle-root KEY tier** (the indirect proxy), both presets; **BIR-false increase in either preset =
  hard stop**.
- Snapshot goldens refreshed only after the change is verified correct; both suites pass; full branch coverage of
  the new decoder; expect + explain the L1 +3/+1/+1 re-tune.

## §5 — Open implementation questions (resolve in the per-increment audits/instructions)
- **State pruning:** top-K per slice — what K keeps the relative-pair + modulation candidates alive without blowing
  up the beam?
- **Transition cost shape:** circle-of-fifths distance vs a learned/tuned matrix; the self-transition magnitude
  (the Stage-5-fit analogue of today's `relativeKeyHysteresisMargin`).
- **Window for the emission:** fixed look-around vs the lazy R3 extension feeding the emission window directly.
- **Confidence definition:** per-slice sigmoid vs path-margin vs both → the flagged-residual threshold.
- **Incremental (R2):** design the decoder interface so a dirty span + margin can be re-decoded without a full pass
  (even if the full editor-incremental wiring is a later step).

## §6 — Sign-off + CC instruction plan
- [ ] **Sequence (§0):** Increment A (indexing, byte-identical) → B (ground-truth harness, read-only) → C (key-path
      decoder, behavior-changing). Approved / amended: ____________________
- [ ] **A (§1):** the byte-identical indexing fix + identical-results gate.
- [ ] **B (§2):** the held-out direct metric + the split + the Jazz parse fix.
- [ ] **C (§3):** emission = `KeyModeAnalyzer`; dedicated key-path decoder; self-transition transition; the output
      contract; wired in; validated by the §4 metric set, not byte-identity.
- [ ] Then: a CC instruction per increment (A, then B, then C), each committed + verified + ratified before the next.

*Cadences/function are NOT in L3 (gated Stage 5). L1/L2 frozen (A is a byte-identical L1 perf fix); L4–L6 downstream.*
