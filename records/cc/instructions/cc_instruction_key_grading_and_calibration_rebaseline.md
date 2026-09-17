# CC INSTRUCTION — The combined re-baseline event: the parent-collection mode grading + the calibration-map refit — OI-132 / OI-144 / OI-145 wave 1

> **Issued by Cowork, 2026-07-13.** The user ruled (register row OI-132): the
> dominant-family exotic modes reduce to major/minor by the PARENT-COLLECTION rule,
> uniformly, all five modes. And the user's readiness directive requires the four
> committed calibration maps — fit on the pre-correction ground truth — refit on the
> corrected substrate (row OI-144). Both corrections move recorded figures, so they
> execute HERE as one ritual event: one outgoing snapshot, sequential implementation
> with clean attribution, one ratification pause with everything side by side, then
> two separately-revertible landing commits. This closes the last figure-moving
> remainder of wave 1 except the harness group.
>
> **The two corrections, plainly:**
> - **A — the mode-grading consolidation.** One shared reduction in the ONE
>   ground-truth/our-key parsing substrate: the five dominant-family modes (Phrygian
>   dominant, altered, Lydian dominant, Lydian augmented, Mixolydian flat-six) reduce
>   to the MINOR (or parent-appropriate) key of their PARENT collection — Phrygian
>   dominant on C-sharp grades as F-sharp minor. The second parser path folds into
>   the shared one (the wave-1 deferred half of OI-132); the name-parse failure on
>   the flat-sign modes dies with it. Expected motion, written from the probe:
>   key-agreement +0.13 to +0.49 points per column per preset; the ROOT columns and
>   the charged/floor root sets UNCHANGED (the probe proved the root axis untouched);
>   the oracle-root key-tier shuffle of a few records as measured in the wave-1
>   comparison. Any motion OUTSIDE the five-mode regions is a stop-and-explain.
> - **B — the calibration-map refit.** Re-run the calibration fit on the corrected
>   substrate (the transposition offsets now applied); all four maps are expected to
>   move. The maps are consumed at analysis time, so this is a PRODUCTION-BEHAVIOR
>   change: after the refit, a full scratch corpus regeneration is compared against
>   the committed corpus — any changed `.ours.json` is part of the adoption, must be
>   enumerated, must pass the hard stop (the meaningful root-error mass
>   non-increasing, the run-diff explained), and both test suites must be green.
>   Written expectation: the production drift is small (confidence values shift;
>   winners move only where a confidence crosses a gate threshold); if the drift is
>   LARGE (more than a handful of regions), stop and report before the pause —
>   that would be a discovery about how load-bearing the stale fit was.
>
> **Read first:** `OPEN_ITEMS.md` (OI-132 — the ruling; OI-144; OI-145),
> `cc_mode_grading_adjudication_probe_report.md` (the measured expectations),
> `cc_measurement_chain_hardening_report.md` (the wave-1 state + the deferred
> parser-fold facts), `CLAUDE.md` (the gate blocks to be re-stamped),
> `tools/REPRODUCIBILITY.md`, `BUILD_AND_TEST.md`.
>
> **REMINDERS:** the ritual is the law — snapshot FIRST, every moved figure explained
> and attributed, the user ratifies BEFORE the reference lands (#14/#16); no `src/`
> change anywhere in this event; no constant tuned beyond what the refit itself IS;
> no golden refresh unless the production drift makes one owed and the user ratifies
> it explicitly; no self-invented labels; the self-check over every diff; shell and
> git rules as standing (own files by name; the known carry unstaged; `cc_*.md`
> force-added in the fold); push to `origin` only, never `upstream` — the standing
> hard stop, `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting edits** (the user's three decisions recorded 2026-07-13:
   human-as-ground-truth + the judge-as-guidance at the corpus event, the repertoire
   breadth and its open when-question, the intonation hold with its
   future-consumer rationale; plus the evidence inventory's declared-consumer
   section):
   ```
   git add OPEN_ITEMS.md
   git add cowork_evidence_inventory.md
   git add -f cc_instruction_key_grading_and_calibration_rebaseline.md
   git commit -m "docs(cowork): OI-56 human-as-ground-truth + judge-as-guidance (closed into OI-38) + OI-62 intonation held as declared future consumer + the combined re-baseline instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor c1bc9bb513 HEAD; echo "exit:$?"` — the second must
   print `exit:0`.

## Task 1 — Snapshot the outgoing reference (O-12, before anything changes)

The current `tools/robust_stop/` reference, the committed calibration maps, and the
current ratified figures — snapshotted under the established dated-snapshot pattern,
committed as its own commit BEFORE any implementation.

## Task 2 — Correction A: the mode-grading consolidation, implemented and measured

Implement the parent-collection reduction ONCE in the shared substrate; fold the
second parser path onto it; delete the divergent copy. Then measure: the full a8 run
+ diff against the snapshot. Verify and record: the run-diff confined to regions
carrying the five mode labels; root columns and root-fail sets byte-identical; the
key columns moved within the probe's written window; establishment — with the
five-mode regions excluded, everything byte-identical. The suites and the
establishment battery green.

## Task 3 — Correction B: the calibration refit, implemented and measured

Re-run the calibration fit on the corrected substrate to scratch; diff the four maps
against the committed ones (enumerate what moved and by how much); install to
scratch-config and run the FULL scratch corpus regeneration against the committed
corpus. Enumerate every changed `.ours.json`; run the hard stop on the candidate;
run both suites. Record per-region attribution of any production change (which
confidence crossed which threshold). If drift exceeds a handful of regions per
preset: STOP and report before the pause.

## Task 4 — PAUSE: the user ratifies the combined result

Present (with full context in the question itself): the old and proposed-new figures
for every column and preset, attributed per correction (A's key-column moves; B's
map deltas and any production regions); the run-diff shapes; the hard-stop verdict;
the suites' state. DO NOT land the reference, the maps, the fixture baselines, or
the `CLAUDE.md` gate text before the user approves. If the user declines or
redirects, stop and report.

## Task 5 — On ratification: land, fold, push

1. TWO separately-revertible landing commits: (A) the grading consolidation +
   re-baselined reference + manifest re-stamp + the `CLAUDE.md` key-column figures +
   the fixture baseline update; (B) the refit maps + any production-side artifacts
   their adoption requires (+ the golden refresh ONLY if ratified). Each commit
   message carries the ratification date and the report reference.
2. The `docs(cc):` fold: `cc_key_grading_and_calibration_rebaseline_report.md` (the
   snapshot hash; both corrections' diffs explained; the ratification record; every
   expectation met/failed; anything surprising as its own register row). Register:
   close OI-132 and OI-144 with the landing hashes; update OI-145 (wave-1 remainder
   = the harness group only). `STATUS.md` (prepend) + the `cowork_handoff.md` entry
   block. Plain language everywhere.
3. The self-check over every diff. **Push — user-authorized 2026-07-13:** all local
   commits to `origin` only, after `git remote -v` confirms `upstream` push is still
   disabled; anything toward `upstream` is the standing hard stop. Confirm in the
   report: the pushed hash, `upstream` untouched.
