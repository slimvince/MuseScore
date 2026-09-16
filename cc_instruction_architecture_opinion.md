# CC Instruction: Architectural Second Opinion — Layer Structure and Deferred Commitment

## Pre-reading (mandatory every session)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, and `C:\s\MS\docs\scoring_model.md` before starting.

**This is a read-and-reason pass. No code changes. No commits.**

---

## The question

The current pipeline commits to a winner at the template-scoring layer, using only
local PC evidence, and then applies functional context as a correction in layers above
it. The hypothesis under evaluation is:

> Commitment to a chord identity should be deferred until after functional context
> is applied. Template scoring should produce a scored distribution over possible
> identities; the functional layer should resolve that distribution using harmonic
> context (predecessor confidence, progression signals, key stability). Most of the
> current dead ends are symptoms of committing too early.

You have seen every failure mode in this codebase firsthand. This instruction asks
you to evaluate the hypothesis by reasoning from those specific failures — not from
architectural theory.

---

## Part 1 — Failure case analysis

For each failure case below, answer: **would deferred commitment dissolve this
failure, move it, or leave it unchanged?** Be specific about the mechanism.

A failure "dissolves" if the functional layer, seeing a distribution rather than a
committed winner, would have enough information to select the correct identity.
A failure "moves" if the problem shifts to a different layer but doesn't go away.
A failure "remains" if the failure is not about commitment timing at all.

### Case A — Iter 98: rootContinuityBonus mis-fires (5 Baroque residuals)
Mechanism: a sparse/uncertain predecessor region commits to rootPc=X; the next
region's rootContinuityBonus rewards staying on X (+0.40), tipping a wrong winner.
Attempts to gate the bonus at consumption time (distinctPcs proxy) failed because
the proxy couldn't separate wrong sparse predecessors from correct Alberti-bass
predecessors.

If the predecessor region instead produced a distribution (winner score, margin,
root pcWeight, distinctPcs all preserved), rootContinuityBonus could scale by
predecessor confidence rather than applying flat +0.40. Would this dissolve the
Iter 98 dead end, or is the failure deeper than confidence scaling?

### Case B — bwv301: G-absent winner from template scoring
Mechanism: G major template fires because G's 3rd (B) and 5th (D) are present in
the sub-segment, even though G's root pcWeight = 0.0. The DCML-correct B-rooted
reading loses because Bm7 is missing its 5th (F#). Commitment happens inside
`applyHarmonicFunction` before any functional context is applied.

If commitment were deferred, what functional signal would select B over G?
The predecessor context, the key, the bass register — which of these carries
the disambiguating information, and is it currently available at the functional layer?

### Case C — B1 (MinorMajor7 template): leading-tone ambiguity
Mechanism: {0,3,7,11} matches both genuine i(maj7) and {tonic+leading-tone-of-V}
in Baroque minor-key contexts. The template fires on local PC evidence alone and
cannot distinguish the two without knowing whether the leading tone is resolving.
Deferred to Phase E.

With deferred commitment, the functional layer would see both i(maj7) and the
{tonic+leading-tone-of-V} reading in the distribution. What functional signal
resolves the ambiguity? Is that signal currently in `HarmonicFunctionContext`,
or would it need new infrastructure?

### Case D — B3 (dim7CharacteristicBonus): rotation-selector role
Mechanism: the dim7 bonus is not just a scoring weight — it is a rotation-selection
mechanism for enharmonic dim7 ambiguity. It uses a non-diatonic ♭♭7 check to
asymmetrically reward the correct enharmonic rotation. Without it, all four rotations
of a dim7 score identically. This means commitment to a dim7 rotation happens inside
the scoring layer itself, not just at winner-selection.

Is this a case where deferred commitment doesn't help — because the rotation
ambiguity is intrinsic to the chord type and requires the same non-diatonic check
regardless of when commitment happens? Or is there a functional signal (key, voice
leading, resolution target) that would resolve dim7 rotation better than the
current non-diatonic check?

### Case E — The deduction-block guard (5 snapshot regressions)
Mechanism: the absent-root guard placed in the inversion-deduction block
(chordanalyzer.cpp L2839–2880) caused 5 snapshot regressions because that block
deliberately promotes weak-root first-inversion alternatives — the guard fired
on legitimate cases. The guard at the `applyHarmonicFunction` winner-selection
point avoids this.

Does this failure case tell us anything about layer structure — specifically,
whether the inversion-deduction block is doing work that belongs at a different
layer? Or is it correctly placed and the guard was simply the wrong tool for it?

---

## Part 2 — Implementation constraint audit

Read the following sections of code and identify the load-bearing assumptions
about early commitment:

### 2a — applyIter8691Pedal

```
grep -n "applyIter8691Pedal\|Iter.*86\|Iter.*91\|pedal" \
  C:\s\MS\src\composing\analysis\region\regionanalyzer.cpp | head -30; echo "exit:$?"
```

Where does this pass run relative to winner commitment? Does it read or mutate
results[]? If results[] is not yet committed when this runs, what breaks?

### 2b — Gate cascade dependency on results[0]

```
grep -n "results\[0\]\|winner\b" \
  C:\s\MS\src\composing\analysis\chord\chordanalyzer.cpp | head -40; echo "exit:$?"
```

How many gates in `applyPostScoringGates` reference `results[0]` directly or via
the `winner` capture? If results[] contained a distribution rather than a committed
winner at results[0], which gates would break and which would be unaffected?

### 2c — ScoringSnapshot as distribution representation

Read `harmonicfunctionlayer.h` — specifically the `ScoringSnapshot` and `ScoringCell`
structs. Does `ScoringSnapshot` already represent a scored distribution over all
(bass, root, template) cells? Could it serve as the "pre-commitment distribution"
that a deferred-commitment architecture would pass to the functional layer, or does
it lack something essential?

### 2d — previousRootPc propagation

```
grep -n "previousRootPc\|nextRootPc\|advanceTemporal\|HarmonicFunctionContext" \
  C:\s\MS\src\composing\analysis\region\regionanalyzer.cpp | head -30; echo "exit:$?"
```

At what point in regionanalyzer is `previousRootPc` set? Is it set from the
committed winner, or from some pre-commitment state? If commitment were deferred,
when would `previousRootPc` be available to the next region's context?

---

## Part 3 — Your independent assessment

Having reasoned through the failure cases and the implementation constraints, answer:

**Q1 — Which failure modes are genuinely about commitment timing?**
Separate the cases where deferred commitment would make a real difference from
the cases where the failure is about something else (missing voice-leading model,
segmentation, insufficient template coverage, etc.).

**Q2 — Is ScoringSnapshot already the right foundation?**
`ScoringSnapshot` captures all (bass, root, template) cells with their scores.
Is this already a "distribution before commitment" that the functional layer could
use directly — with commitment deferred to after functional signals are applied?
Or is the current `applyHarmonicFunction` already doing this, and the problem is
only in what gets passed to the NEXT region?

**Q3 — What is the minimum change that moves commitment to the right place?**
Not "what is the full redesign" — but what is the smallest structural change that
would defer commitment past functional context for the cases where it matters?
Candidates: (a) enrich `HarmonicFunctionContext` with predecessor scoring metadata
and scale rootContinuityBonus by confidence; (b) something larger.

**Q4 — What failure mode have you seen that we have NOT discussed, that you think
is the most important structural mismatch between the current architecture and the
inference problem?**
This is your opportunity to surface something from your operational experience that
hasn't come up in the high-level analysis. Be specific — name the score, the
mechanism, and why you think it points to a structural issue rather than a
parameter-tuning issue.

---

## Output

Write findings to `C:\s\MS\cc_architecture_opinion.md`.

Keep the response tight. For each failure case in Part 1: two to four sentences,
not a paragraph. For Part 3: answer each question directly, then stop.

The most valuable thing you can contribute is a specific, falsifiable claim about
which failure modes would dissolve and which would not — not a general endorsement
or critique of the architecture.

**No code changes. No commits.**
