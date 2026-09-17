# CC Instruction — Phase 5b Step M (part 1): the engage measurement — read-only

> **Why.** All L4 build increments are complete (G1, G2/G3, two-reading inherit, G6, spelling-pin). Before the engage
> GO/NO-GO we need the real numbers: how the **full-capability new path** compares to legacy, and — the strategic
> question — **how much of the ~58% abstention is *recoverable* by the deferred refinements** (§15-O2 inherit, C2 new
> four-note types, dim7-commit spelling-pin) **vs genuinely function-dependent → L5.** That decides
> **refine-then-engage** vs **engage-with-L5**. **READ-ONLY: measurement + analysis, no production edits** (it RUNS the
> diagnostic decode; production is untouched). *(Reminder: the never-bash rule is Cowork's.)*

## §0 — Preamble (sweep)
If any `cowork_*`/`COWORK_*` docs are unstaged (the Phase-5b plan edits, the ledger), commit them local-only
(`docs(cowork): Phase-5b plan/ledger updates`); report the sha. Otherwise note none.

## §1 — Full coverage-matched comparison (the GO/NO-GO baseline)
Run the full-capability new path (`--decode-chords`, all increments on) vs **legacy** over the corpus, **Baroque +
Default**. Report, per preset:
- **where the new path commits, its chord-root accuracy vs legacy's accuracy on the *same* slices** (the honest
  "is it better where it answers" number);
- **coverage-matched accuracy**, raw committed accuracy, and **abstain %**;
- **class-(b) check:** any pitch-class-decidable root the new path commits *wrong* where legacy is right (the hard-stop
  class — count + identities).

## §2 — Abstain breakdown by RECOVERABILITY (the strategic data — use the G6 labels)
Of the abstained duration, bucket each abstain by the **G6 open-question `ambiguity` label** (ShareTone / RelativePair /
SymmetricRotation / Transition / Insufficient / Close), then map each to **what would recover it**:
- **O2-recoverable** — `Insufficient`/`Transition` abstains on **consecutive thin slices where pass-1's neighbour is
  itself a phantom** (the two-reading abstained on a bad neighbour; an O2 joint window would resolve). Estimate the share.
- **C2-recoverable** — `SymmetricRotation`/`Insufficient` that would **commit if the new four-note dim7/mMaj7 types
  existed** (catalogue gap).
- **dim7-commit-recoverable** — `SymmetricRotation` dim7 where the **spelling-pin could deterministically commit the
  root** (currently abstained by the phantom-root guard / low margin).
- **genuinely function-dependent → L5** — `Transition`/`ShareTone`/`RelativePair`/`Close` that need the progression /
  function (irreducible at L4; correctly → L5).
Report the **% of abstention in each bucket** (both presets).

## §3 — Engage-viability projection
From §2: **if O2 + C2 + dim7-commit were pulled in, what is the PROJECTED abstain rate** (the genuinely-function
residual) and the projected coverage-matched accuracy? State whether the full-capability new path would be
**(a) better-than-legacy where committed AND (b) with an acceptable residual abstain → L5** — i.e. whether
**refine-then-engage** looks viable, or the residual is large enough that **engage-with-L5** is the honest call.

## §4 — Deliver
Write `cc_phase5b_stepM_measure_report.md` (gitignored): the §1 comparison (incl. the class-(b) check), the §2
recoverability breakdown (with the bucket %s and the identities of a few examples per bucket), and the §3 engage-
viability projection. **No production edits, no decoder change.** This is the data for the refine-then-engage vs
engage-with-L5 decision (Cowork + user).

## §5 — Stops
- Any production `src/composing/` edit, or a decoder change → STOP (read-only measurement).
- A class-(b) regression appears in §1 → flag it prominently (it's the hard-stop class for engagement) but continue the
  measurement (it's data, not a build STOP).
- A push targets `upstream` → STOP.
