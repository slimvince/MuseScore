# CC INSTRUCTION — The backlog triage pass (read-only + register verdicts) — the register's weakest tier

> **Issued by Cowork, 2026-07-12.** The user asked whether anything in the register
> lacks a concrete resolution path. The honest answer was: about a dozen rows — the
> pre-register backlog inherited from before the register existed, whose recorded plan
> is only "triage: verify this is still real, then assign or supersede" — plus a few
> deliberate long-horizon holds. This session IS that triage: every such row gets a
> checked verdict, so afterward the register contains no row whose plan is merely a
> promise to make a plan.
>
> **The verdict set (closed, per row):**
> - **SUPERSEDED** — the item's substance was resolved or replaced by later work; close
>   the row with provenance naming what superseded it.
> - **STILL REAL — ASSIGNED** — verified current at the code/tests/scores; the row is
>   adopted out of the backlog into the proper register section with a named owner,
>   stage, and gate.
> - **STILL REAL — USER DECISION** — current, but what to do about it is genuinely the
>   user's call; state the decision needed and the options, plainly.
> - **CLOSED AS DECIDED** — for rows whose own text says "decide and close either way":
>   decide, justify in one paragraph, close.
> No row may keep the verdict "triage later." That is the tier being eliminated.
>
> **Verification means CHECKING, not remembering:** a claimed regression is re-run (a
> build + the relevant suite/scores is authorized — read-only in substance: no source
> change, no golden refresh, no constant); a claimed missing feature is grepped for at
> the current code; a claimed stale reference is resolved. Where a check would cost a
> disproportionate build/run, say so and mark the row's verdict as conditioned on that
> stated check — but prefer checking; the session exists to convert memory into fact.
>
> **Read first:** `OPEN_ITEMS.md` in full (the triage targets are the section of
> submission-era backlog rows and any other row whose status contains "triage" or
> "verify still-current"; the long-horizon holds get a lighter treatment — see Task 2),
> `CLAUDE.md`, `STATUS.md`, `BUILD_AND_TEST.md`. Open-book; surprises are findings.
>
> **REMINDERS:** no fixes — verdicts and register moves only (guiding principle 8; a
> trivial fix temptation is still a row, not a patch); verify at the code and data,
> never at assertion (principles 15 and 19); no self-invented labels or jargon; the
> self-check over every diff; shell rules (`; echo "exit:$?"`, redirect large output);
> git rules (stage only your own files by name; never `git add -A`; `git status` after
> every commit; the known carry `cowork_joint_key_chord_design.md` stays unstaged;
> `cc_*.md` gitignored — force-add this instruction in the fold); push to `origin`
> only, never `upstream` — the standing hard stop, `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting edits** (the user's parent-collection ruling recorded at
   its row, the wave-1 remainder status, the state-space direction and the
   phrase-facts enrichment in the design opening, and the rests-as-phrase-ends
   enrichment in the evidence inventory):
   ```
   git add OPEN_ITEMS.md
   git add cowork_key_layer_design_opening.md
   git add cowork_evidence_inventory.md
   git add -f cc_instruction_backlog_triage.md
   git commit -m "docs(cowork): parent-collection RULED (OI-132) + the Baroque state-space direction (design decision 6, research-enriched) + rests-as-phrase-ends (evidence inventory) + the backlog-triage instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and confirm ancestry against the newest hash
   in `STATUS.md`.

## Task 1 — The triage proper

For EVERY row whose status contains "triage", "verify still-current", or an
undecided "decide and close either way": run the check its claim requires, and issue
one verdict from the closed set, with the evidence cited (file and line, test
output, score behavior — whatever the claim is about). Expect roughly: the old
tonicization-classifier row against the certified dormant function machinery (a
likely supersession candidate — verify, don't assume); the ninth-detection and
known-gaps items against the current oracle/formatter behavior; the old notation
regressions and deferred tests re-run at head; the "blocking trio" re-checked at the
current bridges; the documented-but-unimplemented tuning notes against the current
scoring model; the corpus-QA row against the manifest discipline that now exists;
the designed-but-unbuilt review script against what the audit instruments now
provide; the dangling-file reference resolved (recreate or re-point is itself a
verdict); and the trivial helper row decided and closed either way.

## Task 2 — The long-horizon holds, lighter touch

For each deliberately-held long-horizon row: one sentence each — is the hold still
the right disposition, and is its trigger/owner still accurate? Do not expand scope;
the verdict "hold confirmed" is legitimate for these. Anything whose trigger has
quietly already fired gets promoted to STILL REAL — ASSIGNED.

## Task 3 — Report, register, push

1. `cc_backlog_triage_report.md`: the verdict table (row / claim / check performed /
   evidence / verdict); every USER-DECISION item with its options stated plainly for
   a reader who does not know the code; anything new discovered during checking gets
   its own row (same-commit rule).
2. Register discipline: every verdict lands as its row's status flip in the SAME
   commit as the report — SUPERSEDED rows closed with provenance, ASSIGNED rows moved
   into their proper section with owner/stage/gate, USER-DECISION rows marked as
   awaiting the user with the question stated. Update `STATUS.md` (prepend) and the
   entry block of `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-0 register commit; one `docs(cc):` fold (this instruction
   force-added). Run the self-check over every diff. **Push — user-authorized
   2026-07-12:** all local commits to `origin` only, after `git remote -v` confirms
   `upstream` push is still disabled; anything that would touch `upstream` is the
   standing hard stop. Confirm in the report: the pushed hash, `upstream` untouched.
