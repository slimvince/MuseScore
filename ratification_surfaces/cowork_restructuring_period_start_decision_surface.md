# Decision surface — where the restructuring period OPENS, ruled as a commit

> **STATUS: COWORK DECISION SURFACE, not ratified, deciding nothing itself.** Written 2026-08-15
> (Cowork) at the user's request, after the user accepted that the candidate enumeration stands.
> The question it prepares is one of the acts the eighteenth stop leaves to the user: naming the
> start of the restructuring period. Rulings cited are from
> `cowork_rulings_2026_08_13_eighteenth_stop.md`. Presentation follows the standing form: every
> alternative with pros and cons naming principles, rated against the ultimate objective.

## 1. What is being decided, and in what form

**The decision: the commit at which the restructuring period OPENS, exclusive** — everything
after that commit is inside the period; the commit itself and everything before it is outside.

**Why a commit and not a date or a time of day.** Three grounds. *(i)* The record carries a
measured date discrepancy: the thirteenth handoff block records rulings dated 2026-08-11 while
the clock read 2026-08-13, with the instruction to establish dates at the git author dates before
citing them. A ruling by date inherits that hazard; a ruling by commit does not. *(ii)* A date
boundary needs a timezone convention (commits in this repository are stamped +02:00); a commit
needs none. *(iii)* A commit hash is content-addressed and self-verifying — D-253's own ground
for admitting git object queries by explicit hash — and it is the form the candidate artifact
already encodes (`range.start_commit_EXCLUSIVE`).

**What the period governs, read from the rulings:** Ruling 10's pre-pollution baseline (the tree
at the opening commit is the baseline the reconciliation compares against); Ruling 13's marking
of open-items rows affected by pollution; Ruling 12's sizing and sequencing. **What it does NOT
govern:** the published enumeration, which keeps its S1 floor whatever is ruled — narrowing is a
filter over strata, nothing is re-derived (the artifact states this of itself).

## 2. The established facts and the declared assumptions (the premise ledger, Cowork's own)

- **F1 (FACT, read at the git objects this session, by explicit hash):**
  `9306dc5072` 2026-07-11 01:23 — the open-items register created (S1).
  `51d4f6dcf3` 2026-07-18 19:56 — the STATUS/handoff doc split (S2).
  `1e32b5e92e` 2026-07-27 12:44 — the open-items index split (S3).
  `b006dc15b5` 2026-08-02 00:00:30 — D-231 ratified (S4).
  Then, inside S4 the same night: `200a4e1087` 00:55:16 (LF-normalization chore),
  `f833a2d2a9` 00:55:52 (phase 1 Task 1 — the homing acts, 20 decisions written into their owning
  specifications), `ab336f43b5` 00:56:29 (phase 1 Task 2 — *"the truth-sync (every named false
  specification statement corrected at HEAD)"*), which is `f833a2d2a9`'s direct child.
- **F2 (FACT, read at the candidate artifact):** 435 commits, 22,198 flagged hunks; the
  specification-bearing slice is 314 (governing 239 + specification-or-docs 75); the digit-run
  shape is 62.24 % of the candidate list.
- **A1 (ASSUMPTION, derived but not by a checked tool):** the per-stratum split of the flagged
  set — specification-bearing flags S1: 22, S2: 17, S3: 28, S4: 247; source-comment flags
  S1+S2+S3: 234, S4: 19; flagged totals 705 / 378 / 1,279 / 19,836. Derived 2026-08-15 by an
  ad-hoc script over staged snapshots of the artifact and its hunk file (a declared departure of
  the same shape CC's candidate-pass close declares). **The check it owes:** re-derivation by a
  checked tool before any act rests on the split.
- **A2 (ASSUMPTION, not established):** the pre-S4 flags are dominated by the documentation
  edits of ratified, measured July work (the mode-grading consolidation 07-13, the
  signature-mask fix 07-14, the joint-estimator adoption 07-26, the notation switch 07-27) and
  not by code-influenced correction of specifications. Inferred from dates; no pre-S4 hunk was
  read individually. **The check it owes:** the July screen — read the pre-S4
  specification-bearing flagged hunks (67 under A1) one by one.
- **A3 (carried caveat, not Cowork's):** the measurement tool that produced every count above
  was written in one batch and has never been established (#19). Every number inherits it.

## 3. The alternatives

### Alternative A — open exclusive at `9306dc5072` (2026-07-11): the earliest named restructuring act

**Pro (#12, no information loss; the pass's own asymmetry):** under-inclusion is the
catastrophic direction — a destroyed discrepancy is a lost audit signal, and erring early makes
missing one impossible within the named bounds. No act of the restructuring shape named anywhere
in the record escapes. **Pro (cost of adoption zero):** it is the published population's own
floor; nothing is re-derived.
**Con (#4, capacity — the arc's measured scarcest resource):** it marks three weeks dominated by
ratified, evidenced work for re-evaluation under Ruling 13. **Con (record quality):** a row
marked polluted with no nameable polluting instruction is the weak shape the lapse rule already
guards against — a mark with no named grading. **Con (signal dilution):** the reconciliation
reads more differences that turn out benign, at the sites least likely to hold evidence.
**Rating against the ultimate objective:** safe but expensive — it buys insurance against a
mechanism nobody has named operating before 2026-08-02.

### Alternative B — open exclusive at `b006dc15b5` (2026-08-02 00:00): D-231's ratification

The first three in-period commits are the LF chore, the homing acts, and the truth-sync.
**Pro (the diagnosis's own ground):** the eighteenth stop blames one instruction — D-231's truth
half. It did not exist before this commit, and its first exercise (`ab336f43b5`) landed 56
minutes after it. The period then has a nameable cause, so every Ruling 13 mark carries its
mechanism — the strong record shape. **Pro (#4):** capacity concentrates where the
specification-bearing changes are (247 of 314 under A1). **Pro (precision):** the baseline is
exact — the tree at `b006dc15b5`.
**Con (#12/#19, the catastrophic direction):** if any code-influenced specification correction
happened between 07-11 and 08-02 outside ratified acts, it falls outside the period and its
destroyed signal is lost silently — and Ruling 5 says influence is invisible in the text, which
cuts against any cleanliness argument made from the text alone. **Mitigation, not a discharge:**
the enumeration keeps the July flags regardless, and the July screen (A2's check) bounds the
risk cheaply (#5).
**Rating:** best alignment with the diagnosis, provided its under-inclusion risk is checked
rather than assumed.

### Alternative C — open exclusive at `1e32b5e92e` (2026-07-27): the index split, covering the harvest era

**Pro:** covers the decisions-register construction (harvest 2026-07-28 onward), whose origin
Ruling 8 names — production code comments were a harvest source, so observation-of-code content
exists in the register by construction. **Con (the decisive one):** Ruling 8's remedy is the
register FILTER, whose test — can a deciding act be named — does not read the period at all; C
buys coverage the filter already provides. **Con:** outside the register the S3 stratum's
specification-bearing flags are few (28 under A1), and the line has no named mechanism of its
own — it inherits A's weakness at smaller size. **Rating:** dominated — choose A's insurance or
B's mechanism; C is a partial payment for either.

### Alternative D — open exclusive at `f833a2d2a9`, truth-sync onward only: DECLINED, stated so it is not re-raised

The homing acts are restructuring — growth, which Rulings 2 and 4 class as content change — and
Ruling 5's influence test cannot separate a homing rewrite from a truth-sync rewrite after the
fact. A period that excludes the homing commit written 37 seconds before the truth-sync would
rest on the commit message's own division of one night's work.

## 4. The recommendation

**Alternative B — the period opens exclusive at `b006dc15b5` — with two checks attached before
Ruling 13's marking runs:** (1) A1's split re-derived by a checked tool; (2) the July screen —
the pre-S4 specification-bearing flagged hunks read individually, **with the falsification rule
stated now: if any shows a code-influenced correction, the period question RE-OPENS.** That
keeps the asymmetry honest — B's under-inclusion risk is checked for the price of reading a few
dozen hunks, not accepted on assumption.

## 5. What this ruling would NOT decide

No repair is authorized — the reconciliation still waits on the phase re-ruling and the pilot.
No row is marked — Ruling 13's marking is a separate act that reads the ruled period. The
enumeration is not re-run. D-231's rephrasing, the new phases, the pilot's file, the register
filter and the `src/` comment marking all remain owed exactly as the eighteenth stop leaves them.

*Provenance: Cowork, 2026-08-15. F1 read at git objects by explicit hash; F2 read at
`tools/audit/doc_change_candidates.json`; A1/A2 declared above with their checks; A3 carried
from the fourteenth handoff block.*
