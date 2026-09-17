# CC Instruction — part 3: is the carried "uncertain" residual resolved by FUNCTION or by a note-separable cue? (read-only; gates O1)

> **Context.** Open item O1 (`cowork_uncertain_resolver_investigation.md`): is the step that resolves a slice marked
> "uncertain" **Architectural Layer 5 (function) itself**, or a **distinct gated step** ahead of it? The provisional
> verdict (design + literature) is **Layer 5 — no new box**: the residual is function-circular, so resolving it is
> part of assigning function. This measurement tests that verdict empirically, and is the *only* thing that could
> overturn it. **It is read-only / decode-only: no production change, no wiring, no new layer.** The verdict input
> is the FUNCTIONAL-vs-SEPARABLE split of the true residual.
>
> **The decisive question, operationalized:** for each carried-ambiguity case, is the ground-truth-correct reading
> predicted by a **single-slice note cue** the note-layers already own (spelling, bass, metric weight, local stepwise
> resolution) — **SEPARABLE** — or is it predicted by **none** of those, so that only the surrounding functional
> progression can pick it — **FUNCTIONAL**? A class that is reliably FUNCTIONAL belongs in Layer 5 (no new box); a
> class reliably SEPARABLE would justify a distinct step (or a fix back in Layer 4).

## §0 — Ground rule: the GT is the function oracle; do NOT use our cadence detector
Our cadence detector was verified **unusable** earlier. Do **not** build the FUNCTIONAL test on it. Use the
**human Roman-numeral ground truth** (When-in-Rome / DCML, via the existing music21 `RomanNumeral` oracle and
`compare_rn`) as the source of both the correct reading and the surrounding functional context. One grading path —
reuse the existing GT/grader, do not stand up a new one.

## §1 — Assemble the TRUE residual case set (both presets, held-out)
The residual is what reaches the resolver — i.e. the carried-ambiguity slices **that Layer 4 does not already settle
from notes + spelling**. Build it, do not assume it:
1. Start from the known ambiguity classes already characterized: relative-major/minor and tonicization-vs-modulation
   (the key-side, from the L3 residual characterization), and the share-tone chord pairs (`V6`↔`vii°`, `iii`↔`I6`)
   plus the **unspelled** dim7/aug rotation (the chord-side, from the BIR=false / `characterise_bir_false` sets).
2. **Exclude** the cases Layer 4 resolves without function: where the **notated spelling alone** pins the
   root/quality (the spelled dim7 majority), or where the slice has **sufficient notes** to fix the chord outright.
   Those never become "uncertain," so they are not residual. Report how many are excluded here and why.
3. The remainder is the **true residual**. Report its size per class, per preset.

## §2 — The separability test (per residual case)
For each true-residual case, with the GT-correct reading known, compute whether any **single-slice note cue** predicts
that reading on its own:
- **(a) spelling** — does the notated tonal-pitch-class spelling pick the GT reading? (Should be ~empty here, already
  excluded in §1.2 — a non-empty count is a finding: those are L4's job, not the resolver's.)
- **(b) bass / inversion** — does the bass note alone pick the GT reading?
- **(c) metric weight** — does metric position alone (the strong-beat reading) pick it?
- **(d) local stepwise resolution** — does the ambiguous note's step-resolution **within the window** pick it,
  *without* needing the chord it resolves to be functionally named (i.e. computable from notes + window alone)?

Classify each case:
- **SEPARABLE** — at least one of (a)–(d) predicts the GT reading. Record **which** cue.
- **FUNCTIONAL** — none of (a)–(d) predicts it; the GT reading is distinguishable from its alternative only by the
  **surrounding progression** (the chord before and/or after, read functionally). Operationally: FUNCTIONAL = not
  note-cue-predictable by (a)–(d).

Determinism: the test is a fixed computation over the GT + the note-layer cues; no tuning, no threshold sweep.

## §3 — Reuse existing measurements; do not redo them
Several sub-parts are already measured — **reference, do not repeat**:
- the **joint key+chord** investigation (whether joint search helps beyond feed-forward — found inert);
- the **modulation scoping** (stay-home vs modulate diagnosis);
- **`compare_rn` crediting `V/d`↔local-`V`** (the tonicization/applied-chord credit).
Cite their results where they already bear on a class (e.g. the key-side tonicization-vs-modulation behaviour), and
only newly compute the §2 FUNCTIONAL-vs-SEPARABLE split.

## §4 — The verdict (the input to O1)
State plainly, **per class, per preset**: the true-residual size and the FUNCTIONAL vs SEPARABLE share (with the cue
breakdown for the SEPARABLE ones).
- **If the residual is essentially all FUNCTIONAL** (no class reliably resolved by a single-slice note cue) →
  **confirms O1's verdict**: the resolver is Architectural Layer 5; no distinct box; the specs collapse the three
  names to "Layer 5."
- **If a class is reliably SEPARABLE by a named note cue** → **surface it**: that class, its cue, and its share define
  either a fix that belongs **back in Layer 4** (if the cue is one L4 already owns and simply under-uses) or a
  **distinct gated step** (if the cue is a genuinely new `(evidence × question)`). Name which, with the evidence — do
  not assert a box.
- **If (a) is non-empty** (spelling predicts cases still in the residual) → those are Layer-4 leakage, not resolver
  work; report separately.

## §5 — Constraints
- **Read-only / decode-only.** No production change, no wiring, no new layer or step is built — this measures whether
  one is *needed*. The decode/measurement tooling may stay **local (uncommitted, gitignored)**, like the fair-key/tpc
  measurements.
- **GT is the function oracle** (§0); our cadence detector is not used.
- **One grading path** (reuse music21 GT + `compare_rn` + the existing characterization tools).
- `upstream` untouched; any push is `origin` only and is not required for this read-only measurement.

## §6 — Deliverable
`cc_uncertain_resolver_measurement_report.md` (held/gitignored): the §1 true-residual sizes (and the §1.2 exclusions),
the §2 FUNCTIONAL-vs-SEPARABLE split per class per preset with the SEPARABLE cue breakdown, the §3 references to the
reused measurements, and the §4 verdict — confirming Layer 5, or naming the separable class + cue that would justify a
distinct step.

## §7 — Stop conditions
- Any production output moves, or a real new layer/step gets built → STOP (this measures necessity, read-only).
- The FUNCTIONAL test starts depending on our cadence detector → STOP (use the GT oracle).
- A second grading path appears → STOP (one path).
- A push would target `upstream` → STOP.
