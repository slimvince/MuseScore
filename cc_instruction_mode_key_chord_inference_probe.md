# CC INSTRUCTION — Mode/key + chord inference: the desk simulation and the key-axis probe — OI-43 / OI-44

> **Issued by Cowork, 2026-07-12.** The OI-84 certification plan is complete and the
> user opened the held OI-43 discussion. This session executes the first two stages of
> the Premise-Gate funnel for it: the DESK SIMULATION, then — only if the mechanism
> fires — the READ-ONLY key-axis probe. The build decision is not made here; the
> numbers go back to the user against predictions that were written before you
> started.
>
> **This is NOT an audit session, and it is NOT blind.** It is an explorational
> fact-finding run under the surprise-scope rule (CLAUDE.md): surprises here are
> findings to record, not stops — except in your own tooling, where a surprise still
> means stop, fix, restamp, rerun. READ FIRST, in this order:
> `cowork_mode_key_chord_inference_discussion.md` (the opening document — its three
> written predictions are the contract this session reports against),
> `cowork_joint_key_chord_design.md` (the bounded pair-beam architecture),
> `cc_engage_stage3_joint_measure_report.md` (the chord-axis measurement being
> reopened, and its instrument), `cowork_functional_analysis_research_grounding.md`
> §3, `OPEN_ITEMS.md` (session-start rule, normal here), `CLAUDE.md` in full, and
> `BUILD_AND_TEST.md`.
>
> **Scope declaration:** READ-ONLY with respect to production: no `src/` behavior
> change, no constant tuned, no golden refresh; `tools/robust_stop/` and
> `tools/corpus/` written to by NOTHING. Instrument work happens in Python under
> `tools/` (extending the existing probe harness). If — and only if — the existing
> `--dump-joint-probe` output lacks a field the key-axis grading needs, a minimal
> extension of that already-default-OFF dump is permitted as its own revertible
> `feat(tools):` commit with production byte-identity re-proven (standard corpus
> regeneration to scratch, zero diff vs committed, both suites green, no golden
> refresh). Prefer the zero-C++ route: compute from the existing dump plus the
> established grading substrate wherever possible.
>
> **REMINDERS:** you decide nothing the user owns — the probe measures, the user
> decides (guiding principles 8 and 14); no self-invented labels, abbreviations,
> numbering schemes, or jargon — use the names things already have; run the self-check
> over every diff before reporting done; never stop a long-running process without
> asking — no subset substitutes for a full-corpus run; shell rules
> (`; echo "exit:$?"`, redirect large output); git rules (stage only your own files by
> name; never `git add -A`; `git status` after every commit; the known carry
> `cowork_joint_key_chord_design.md` MAY have working-tree edits — leave it unstaged);
> push to `origin` (the user's fork) ONLY, never `upstream` — the standing hard stop,
> `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting edits** (the certification-grant and plan-completion
   updates to the register, and the discussion opening document):
   ```
   git add OPEN_ITEMS.md
   git add cowork_mode_key_chord_inference_discussion.md
   git add -f cc_instruction_mode_key_chord_inference_probe.md
   git commit -m "docs(cowork): L5 + instruments CERTIFIED; the OI-84 certification plan COMPLETE; the OI-43 discussion opens - the mode/key + chord inference discussion basis (premise ledger + written predictions) + the probe instruction"
   ```
   (If the discussion document is caught by a gitignore rule, force-add it too.)
   Then `git status --short; echo "exit:$?"` — remaining entries: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor a402ba94f0 HEAD; echo "exit:$?"` — the second must
   print `exit:0`.

## Task 1 — The desk simulation (#17(c)) — the cheap stage that can kill the premise

Select 3–5 REAL key-disagree cases from the known failing material: the
note-identical relative-key class the cross-layer caveat names (the `bwv352` family
is the documented seed; take the others from the robust-stop reference's key-disagree
runs, choosing cases where the committed key disagrees with the DCML ground truth and
the sonorities are key-ambiguous). For EVERY case, by hand, at the score and the
committed dumps — in this order:

1. **Does the mechanism FIRE here?** Is the ground-truth key present in the carried
   `keyAlternatives` menu for the region? Does re-decoding the chord under that
   carried key produce a different chord than under the argmax key? (Control flow
   before arithmetic — the ratified sharpening.)
2. **Which term moves, and by how much?** If it fires: trace what a pair ranking
   would see — the key sequence margin between argmax and the alternative, the
   decoder's margin under each key — and state whether the true pair could plausibly
   win, and on which evidence.
3. Write the trace per case, plainly.

**HARD GATE:** if the mechanism fires on NONE of the cases — the true key absent from
every menu, or the chord never differing — STOP after Task 1, commit the desk-sim
record, report, and push. The premise dies at the cheap stage, exactly as the funnel
intends; do not build the probe extension around a mechanism the failing cases say
cannot fire.

## Task 2 — Establish the key-axis grader (#19) before reading any number

Extend `tools/measure_joint_probe.py` (the ONE existing probe harness — extend, do
not fork) to grade the KEY axis on the same established substrate the ratified
baselines use (the robust-unit grading: duration-weighted key agreement against the
DCML ground truth).

**Establishment, before any probe number is read:** with the ranking disabled (every
region keeping its production argmax key), the extended grader must reproduce the
ratified key-agreement column — 68.13 / 64.43 / 67.50 (Baroque/Jazz/Default) — from
the committed corpus, to the precision the substrate provides. Record this
establishment run in the report. Honor the abstain-aware caveat (register row OI-33):
report grading coverage alongside every figure, so coverage movement cannot flatter a
result. If establishment fails, stop and report — do not proceed to Task 3 on an
unestablished grader.

## Task 3 — The probe (read-only, full corpus, all three presets)

Run over the pinned corpus (`c50002fee1`), all three presets. Two measurement forms,
both honest about what they bound — do NOT invent a fitted pair-score (the
key-score/chord-score scales are not established commensurable; that is a known open
item, and fitting is Stage-5 work):

1. **The ceiling (no ranking rule needed):** per region, does ANY carried (key,
   chord) pair — the chord re-decoded under each carried key — match the ground truth
   better than the committed pair, on the key axis and on both axes jointly? This
   bounds from above what any ranking could recover from the carried menu.
2. **The declared floor:** ONE simple, declared, unfitted composition (state it
   exactly in the report — for example: prefer a pair whose re-decoded chord is
   key-stable AND whose key sequence margin deficit is below the smallest carried
   margin gap; whatever is chosen, it is a probe-only rule, labeled as such) — to
   bound from below what a naive ranking already achieves. Its purpose is honesty
   about the gap between ceiling and floor, not design.

Report, per preset, against the three written predictions of the discussion
document, each answered explicitly (met / not met / bracketed between floor and
ceiling, with the numbers):

- the key-flip population size and its net key-agreement effect (ceiling and floor);
- the concentration of correct flips across the carried key-confidence quartiles;
- the menu-containment rate: in what fraction of key-disagree regions the
  ground-truth key is present in the carried alternatives.

Also report the root-axis effect of the same flips (the arc-12 chord-axis numbers
should be reproduced or explained), so both axes sit in one table.

## Task 4 — Report, register, push

1. `cc_mode_key_chord_probe_report.md`: the desk-sim traces (or the hard-gate stop);
   the grader establishment run; the probe results against each written prediction;
   every deviation, surprise, and tooling fix declared. Machine-readable results
   under `tools/reports/` (a JSON beside the report, the existing pattern).
2. Register discipline: update OI-43 (probe delivered, numbers in) and OI-44 (status
   still the user's decision — state what the numbers support); any new discovery
   gets its own row in the SAME commit. Update `STATUS.md` (prepend) and the entry
   block of `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-0 register commit; the Task-2/3 `feat(tools):` (probe extension +
   artifacts; plus the separate byte-identity-proven `feat` ONLY if a C++ dump field
   was unavoidable); one `docs(cc):` fold. Run the self-check over every diff.
4. **Push — authorized by the user, 2026-07-12:** all local commits to `origin` only,
   after `git remote -v` confirms `upstream` push is still disabled; anything that
   would send content toward `upstream` is the standing hard stop. Confirm in the
   report: the pushed hash, `upstream` untouched.
