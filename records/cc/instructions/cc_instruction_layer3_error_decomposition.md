# CC Instruction — Layer 3 key/mode: CAUSAL DECOMPOSITION of the carried-but-not-picked errors (read-only)

> The characterization (`cc_layer3_characterization_report.md`) found the dominant error mode is **selection,
> not coverage**: on ~72–77 % of wrong slices the true key/mode is *carried in the alternatives* but not picked.
> We do NOT know yet *why* it isn't picked — and the "why" is exactly what assigns each error to a layer. This
> increment computes that decomposition. It is **measurement only**: NO fix, NO decoder tuning, NOTHING wired,
> NO production change. Its *output* (a partition of the errors by cause) is what later tells us which layer to
> amend — but this increment amends nothing.
>
> **★ No-assume / no-context guard:** you have no view of the larger architecture. Do not "fix" anything you find.
> Do not change any decoder setting (`topK` / window / costs / `uncertainThreshold`). If a measurement needs
> chord/function evidence to compute, STOP and surface it (that is the signal it belongs to a later layer).

## §0 — Confirm the inputs exist before adding anything
The decomposition needs, per carried-but-not-picked error slice: the **emission score** of the *picked* (chosen)
candidate AND of the *correct* (GT) candidate. The decode JSON already carries each candidate's emission as
`KeyModeAnalysisResult.score` (the chosen and each alternative). **Verify this is the per-candidate emission, not a
sequence total.** Only if Q1 (below) genuinely cannot be computed from the existing JSON may you add ONE additive,
diagnostic-only field (e.g. the per-candidate total) — same byte-identical pattern as the `alternatives`
serialization (the `--decode-keymode` path returns before `analyzeScore`). Prefer NOT adding if not needed.

## §1 — The decomposition (held-out TEST split, per preset, on the carried error set)
For every scorable miss where the true key/mode IS in the carried `alternatives` (the ~72–77 %), classify by this
tree. Reuse the Increment-B grading path (`our_key_tonic_fixed`, `align_dcml_regions`, `_dcml_key_tonic`,
`md5(stem)%100<20`) — one grading path, extended not forked.

**Q1 — did the LOCAL emission already rank the correct candidate above the picked one?**
Compare `emission[correct]` vs `emission[picked]` at that slice (the per-candidate emission, NOT the sequence total).
- `emission[correct] > emission[picked]` → the emission was locally right; the **sequence/transition overrode it**.
  → branch **TRANSITION** (Q2).
- `emission[correct] ≤ emission[picked]` → the **emission itself preferred wrong**. → branch **EMISSION** (Q3).

**Q2 (TRANSITION) — was the suppressed switch a real key change or a brief tonicization?**
Measure how long the GT-correct local key persists contiguously around the slice (in the GT, in beats/measures or
contiguous slices).
- **Sustained** (persists ≥ threshold) → the change cost over-smoothed a genuine modulation → **L3, cost-recoverable
  (notes-only)**.
- **Brief / embedded** (< threshold, sitting inside a longer different key) → it is a tonicization the cost arguably
  *should* suppress, and GT labeling it a key change is a function-level call → **L5-required (cadence/function)**.

**Q3 (EMISSION) — is the distinguishing pitch evidence present in the window or absent?**
Identify the pitch class(es) that distinguish `correct` from `picked` (the third for maj/min; the raised leading
tone for a relative-minor reading; the characteristic degree for a church mode — e.g. ♮6 Dorian, ♭7 Mixolydian),
and check the emission window's pitch content (from the corpus `*.xml`, as §1c did):
- **Present** (the distinguishing pc appears with non-trivial weight) → the emission *underweighted* it →
  **L3, emission-reweighting recoverable (notes-only)**.
- **Absent** (the window genuinely lacks the distinguishing pc) → notes alone cannot decide → **L5-required**,
  sub-typed by the signal it needs: relative-pair → cadence; symmetric sonority (dim7/whole-tone/aug) →
  chord-identity / spelling.

**Also partition the NOT-carried errors** (the ~23–28 % where the true key never made the top-K∪incumbent union) as a
separate **coverage** pile: is the true key absent because top-K pruned it (its emission rank was just outside K) or
because the emission scored it near-bottom (genuine local failure / undecidable)? This tells us whether coverage is a
pruning setting (L3) or an emission/structural limit.

## §2 — Output: the partition (the deliverable)
Per preset, the carried error mass split into four piles + the coverage pile, with **counts and % of scorable**:
- **A — L3 emission-recoverable** (Q3 present-but-underweighted)
- **B — L3 cost-recoverable** (Q2 sustained over-smoothed modulation)
- **C — L5 cadence-required** (Q2 brief tonicization ∪ Q3 relative-pair, distinguisher absent)
- **D — L5 chord/spelling-required** (Q3 symmetric / whole-tone / augmented)
- **E — coverage** (not-carried; sub-split pruning-vs-emission)
Piles A+B size the **real L3 headroom** (what the later sweep / re-rank may move); C+D are the **L5 spec** (what
downstream evidence L5 must supply); E flags any pruning gain. This partition is the answer to "which layer."

## §3 — Rigor (so the partition isn't an artifact)
- **Threshold sensitivity:** report the partition under 2–3 choices of the Q2 sustained/brief cutoff and the Q3
  "present" weight cutoff, so a pile's size is shown to be robust, not an artifact of one cutoff.
- **Manual spot-check:** hand-verify a small sample from each pile against the score (as §1c did), to confirm the
  automated cause-attribution is sound. Report the agreement. If the classifier cannot tell A from C on a sample
  without chord/function evidence, say so — that itself is a finding (the boundary may be inherently L5).

## §4 — Constraints
- Read-only. No production change; nothing wired; `composing` / `notation` / snapshot tests and `.ours.json`
  byte-identical. No decoder setting changed. One grading path (extend `cc_layer3_keymode_baseline.py`).
- Amend NO layer. This increment only *measures*; the output assigns future work to layers, it does not do it.

## §5 — Deliverable
- Committed: the harness extension (the decomposition mode) + any single additive diagnostic field from §0 if it
  was genuinely required.
- Local/gitignored (`cc_*`, unpushed): `cc_layer3_error_decomposition_report.md` — the §2 partition per preset, the
  §3 sensitivity + spot-check, and a one-paragraph plain-language read of what it implies for the L3 sweep scope
  and the L5 spec.

## §6 — Commit + push
- Commit locally as its own increment; leave held WIP (B2 trio, `STATUS.md`, WIP docs) unstaged; `cc_*` report
  gitignored/local. **Push `origin` only. NEVER `upstream`** (disabled; hard stop if a push would target it).
  Report the new `origin/master` SHA and the committed file list.

## §7 — Stop conditions
- Any production output moves, or the decoder lands on a live path → STOP (measurement-only).
- You are tempted to change a decoder setting to shrink a pile → STOP (that is the later, separately-ratified sweep).
- A pile cannot be computed without chord/function evidence → STOP and record it as a C/D (L5) finding rather than
  fabricating a cause.
- A push would target `upstream` → STOP (fork-only).
