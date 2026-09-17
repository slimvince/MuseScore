# CC INSTRUCTION — The key/mode inference diagnosis (read-only) — OI-141

> **Issued by Cowork, 2026-07-12.** The user directed: understand WHY our key/mode
> inference does not work. This session executes the diagnosis whose Premise-Gate
> opening — the cause classes and the written predictions — is
> `cowork_key_mode_inference_diagnosis.md`. READ IT FIRST; it is the contract this
> session reports against. This is an explorational, open-book, READ-ONLY session
> (surprises are findings, not stops — except in your own tooling: stop, fix,
> restamp, rerun). No blinding.
>
> **Read in this order:** `cowork_key_mode_inference_diagnosis.md`, `OPEN_ITEMS.md`
> (session-start rule — the relevant rows are OI-141, OI-75/OI-81, OI-94, OI-78,
> OI-91, OI-97, OI-33), `CLAUDE.md` in full, `cc_mode_key_chord_probe_report.md` +
> `tools/reports/mode_key_chord_probe.json` (the instrument and numbers this
> extends), `BUILD_AND_TEST.md`. The layer-3 audit report
> (`cc_l3_audit_pass1_report.md`) is useful context for the key layer's mechanics.
>
> **Scope declaration:** READ-ONLY with respect to production: no `src/` behavior
> change, no constant tuned, no golden refresh; `tools/robust_stop/` and
> `tools/corpus/` written to by NOTHING (all outputs to scratch +
> `tools/reports/`). Instrument work in Python under `tools/`, extending the
> existing probe harness — one harness, no fork. If a needed fact is not in the
> existing dumps, prefer computing it from the score files or the ground truth
> directly in Python; a C++ dump extension is a LAST resort (default-OFF, own
> revertible `feat(tools):` commit, production byte-identity re-proven to scratch,
> both suites green).
>
> **REMINDERS:** you decide nothing the user owns — the diagnostic measures, the
> user decides; findings become register rows, never patches (guiding principle 8);
> any eventual fix belongs to the key layer at its proper stage (principle 7); no
> self-invented labels, abbreviations, numbering schemes, or jargon — the cause
> classes carry the exact plain names the opening document gives them; verify at
> the code and data, never at assertion (principles 15 and 19); run the self-check
> over every diff before reporting done; never stop a long-running process without
> asking — no subset substitutes for a full-corpus run; shell rules
> (`; echo "exit:$?"`, redirect large output); git rules (stage only your own files
> by name; never `git add -A`; `git status` after every commit; the known carry
> `cowork_joint_key_chord_design.md` stays unstaged); push to `origin` (the user's
> fork) ONLY, never `upstream` — the standing hard stop, `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting edits** (the OI-44 closure, the OI-43 settlement, the
   OI-141 reframing, and the diagnosis opening document):
   ```
   git add OPEN_ITEMS.md
   git add cowork_key_mode_inference_diagnosis.md
   git add -f cc_instruction_key_mode_inference_diagnosis.md
   git commit -m "docs(cowork): OI-44 declared SHELVED both axes + OI-43 settled + OI-141 reframed by the user (why does key/mode inference not work) + the diagnosis opening (cause classes + written predictions) + the diagnostic instruction"
   ```
   (Force-add the opening document too if a gitignore rule catches it.)
   Then `git status --short; echo "exit:$?"` — remaining: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 0fed3e8729 HEAD; echo "exit:$?"` — the second must
   print `exit:0`.

## Task 1 — Desk simulation first: the absent-key cases

Select 3–5 real regions where the ground-truth key is ABSENT from the carried
candidate-key list (the probe artifact identifies the population; pick cases from
different scores and, if possible, different apparent shapes). Hand-trace each at
the score and the dumps: is the absence a beam-width fact (the true key scored but
fell off the carried list), a hysteresis fact (the analyzer stayed in the previous
key past a real change), a late-anchor fact (the change is caught but late — check
against the un-re-anchored notated-key-change row OI-94), or a segmentation fact
(the region spans a boundary the ground truth places elsewhere)? Write the trace
per case, plainly. There is no hard gate here — the diagnosis proceeds regardless —
but these traces are the sanity anchor for the classifier's cause definitions.

## Task 2 — The classifier, established before it is believed

1. Extend the probe harness (`tools/measure_joint_probe.py` or a sibling script
   under `tools/` that reuses its loading substrate — ONE loading path, no second
   parser) to label EVERY key-disagreeing run of duration with exactly ONE primary
   cause from the opening document's closed list: relative-key confusion /
   tonicization-versus-modulation boundary / parallel-mode confusion / wrong
   neighborhood / segmentation-edge artifact / enharmonic-spelling. Precise,
   mechanical definitions for each, stated in the report (for example:
   relative-key confusion = the committed key and the ground-truth key share a
   pitch collection and differ in tonic; segmentation-edge artifact = the run is
   shorter than one measure and adjacent to a boundary where both sides otherwise
   agree; state and justify every such rule). Plus, per run: the true key
   carried/absent flag, the outranked flag where carried, and the leading-tone
   presence test (for relative-key runs whose true key is the minor sibling: is
   that key's raised seventh present among the region's sounding pitch classes?).
2. **Establishment (#19), before any result is read:** the classifier's totals
   must reconcile EXACTLY with the established key-agreement column per preset —
   the classified failing duration equals the reference failing duration
   (68.13/64.43/67.50 agreeing) — and every figure is reported beside its grading
   coverage (row OI-33). A run that fits no class is UNCLASSIFIED and counted,
   never silently dropped or forced into a class. If reconciliation fails, stop
   and fix the instrument, not the numbers.

## Task 3 — Run, and answer the predictions

Full corpus (`c50002fee1`), all three presets. The report answers EVERY prediction
of the opening document explicitly — met or failed, with the measured number
beside the predicted range: the six cause-class shares, the present-but-outranked
share, and the leading-tone unused-evidence test. Machine-readable results to
`tools/reports/key_mode_inference_diagnosis.json` (stamped: HEAD, corpus hash,
coverage). Long runs: let them finish.

## Task 4 — Report, register, push

1. `cc_key_mode_inference_diagnosis_report.md`: the desk traces; the classifier's
   rule definitions; the establishment/reconciliation run; the per-preset cause
   table against the predictions; the unclassified remainder; every surprise and
   tooling fix declared. State plainly which cause DOMINATES and what the
   leading-tone test says about the user's chord-hints thesis — measurement, not
   recommendation; the what-next decision is the user's.
2. Register discipline: update OI-141 with the measured breakdown (the decision on
   what to pursue stays the user's); any new discovery gets its own row in the
   SAME commit. Update `STATUS.md` (prepend) and the entry block of
   `cowork_handoff.md`. Plain language everywhere.
3. Commits: the Task-0 register commit; one `feat(tools):` for the classifier +
   artifacts (plus the separate byte-identity-proven `feat` ONLY if a C++ dump
   field was unavoidable); one `docs(cc):` fold (this instruction force-added).
   Run the self-check over every diff.
4. **Push — authorized by the user, 2026-07-12:** all local commits to `origin`
   only, after `git remote -v` confirms `upstream` push is still disabled;
   anything that would send content toward `upstream` is the standing hard stop.
   Confirm in the report: the pushed hash, `upstream` untouched.
