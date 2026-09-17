# CC dispatch — the PowerShell corpus and guard widening, OI-342's close, the commit and the push

> **Status: ACTIVE DISPATCH, written 2026-08-08 (Cowork).** Read IN FULL — and read
> **`cowork_rulings_oi345_oi342_2026_08_07.md` IN FULL FIRST**: it is the ratified ruling record
> for Tasks 1 and 2 and is not restated here (#6).
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_guard_dialect_close_and_push.md`.
>
> **★ THE FREEZE IS NOT RELAXED except by ruling R1** (the guard widening, licensed by the user
> under D-436, corpus first). Everything else found is rowed and left, except a finding whose
> subject bears on the analysis, its inputs, or a measurement tool a measurement depends on —
> SURFACED, not acted on (D-641). An establishment obligation (#19) always gates and is always
> surfaced.
>
> **★ NO FIGURES (D-431) AND NO STATE NOT READ (#17a).** No `src/` change, no goldens, no
> corpus, no `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to
> inference, no design. Phase 1 under D-231. **Never bash to read working-tree files (D-253) —
> in EITHER dialect; the guard's blindness this dispatch fixes was never a licence.**
>
> **★ D-472 is NOT worked here** — it is held in item 1 and its ruling is with the user.
>
> **★ Item 2 of the finish line is not started. Phase 1's completion statement is not written,
> drafted, or partially written.**

## 0a. THE RULING LEDGER

- **R1 — OI-345 fixed, corpus first** — the ruling as `cowork_rulings_oi345_oi342_2026_08_07.md`
  records it, read whole. The order is OI-343's, adopted by the ruling: corpus extended with the
  PowerShell family and its aliases BEFORE any rate is republished; then the utility set
  widened; both rates published against the extended corpus; the revert condition — a material
  rise in false denials — governs.
- **R2 — OI-342 closes** — as the same record states it: the INDEX row flips with this ruling as
  provenance; the detail file gains the dated resolution note.
- **R3 — COMMIT AND PUSH, ruled by the user 2026-08-08** ("It is also time to instruct cc to
  git-push", following the standing commit authorization of this arc). At close: ONE
  provenance-stamped commit of the accumulated uncommitted waves (five_rulings,
  licensed_homing, three_owner_rulings, owner_rulings_homing, this wave, and the Cowork ruling
  records), guards re-run at the committed tree, then **`git push origin master`**.
  **★ THE HARD STOP, RESTATED VERBATIM FROM `CLAUDE.md`:** push to `origin` =
  `slimvince/MuseScore` (the user's fork) ONLY. **NEVER push or merge to `upstream`
  (`musescore/MuseScore`) or otherwise contribute toward the MuseScore community** — upstream
  push is disabled in this repo; keep it so; any push/PR/merge that would carry `cfc7eb5e39` (or
  its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed. If
  `bd3a608fecf8` was already pushed on the user's earlier instruction, this push is incremental;
  if not, it carries both commits. Either is correct.

**None of R1–R3 authorizes a fix to the analysis, a design, or an inference change.**

## 0b. THE PREMISE LEDGER (#17a)

**FACT — established by Cowork this session:**

- **F1.** OI-345's measured finding, at its row: the four PowerShell utilities admitted at
  `decide()` where `cat` is denied; the corpus containing no member of the family; the rates
  re-deriving while blind.
- **F2.** The ruling record for R1 and R2: `cowork_rulings_oi345_oi342_2026_08_07.md`.
- **F3.** The prior commit of this arc, made by Cowork on the user's instruction:
  `bd3a608fecf82c446f959432b13e0a5944093cd2` on `refs/heads/master`, parent `4a9c0d4827…` —
  recorded in `STATUS.md`'s five_rulings-wave entry.

**ASSUMPTION — each checked BEFORE the act it licenses, with a STOP if refuted:**

- **A1.** That the PowerShell family's members and aliases can be enumerated from PowerShell's
  own alias table rather than authored ad hoc (`Get-Alias` ships the mapping; `gc`, `type`,
  `sls`, `gci`, `ls`, `dir`, `cat` among them). → enumerate first, record the source of the
  list in the corpus artifact; a hand-authored list with no source is the "vocabulary assembled
  until the answer comes out right" failure and is not acceptable.
- **A2.** That the widening leaves the POSIX side's measured behaviour untouched — same
  verdicts on every pre-existing corpus row. → both rates published on the extended corpus;
  any POSIX-side verdict change is a STOP.
- **A3.** That the working tree at commit time contains only the enumerated waves' work. →
  stage from the union of the waves' recorded enumerations (`changed_paths_five_rulings.json`,
  `changed_paths_licensed_homing.json`, `changed_paths_three_owner_rulings.json`,
  `changed_paths_owner_rulings_homing.json`, this wave's own, and the Cowork ruling-record
  files), verify with `tools/audit/changed_paths.py --staged`, and STOP on any path outside
  that union rather than sweeping it in. The `scratch_artifacts/` rule from the `bd3a608`
  commit stands: only `robust_stop_cells_dumps/` inside it is tracked; the rest stays
  untracked.

## 1. Task 1 — R1: the corpus, then the guard

**1.1** Discharge A1; extend the establishment corpus with the family — sanctioned forms (the
same commands aimed outside the tree, and at git objects by hash) and forbidden forms (aimed at
repository paths) both. **1.2** Re-run `--establish --check` at the UNWIDENED guard and record
that the new rows are misclassified — the blindness measured, which is what the old rates could
not show. **1.3** Widen the utility set. **1.4** Publish both rates against the extended
corpus; discharge A2; the revert condition governs. **1.5** Flip OI-345's INDEX row with
provenance; dated note records that the previous rates were blind to the dialect, not wrong
(#12, the OI-343 wording).

## 2. Task 2 — R2: OI-342 closes

Flip the INDEX row with R2 as provenance; dated resolution note on the detail file.

## 3. Task 3 — Close, commit, push

**3.1** Regenerate what this wave's edits make stale; re-aim any drifted anchors per citation;
guards at the tree — **fix nothing beyond Task 1**. **3.2** Record the worktree enumeration to a
named artifact; run `tools/audit/process_check.py` over this dispatch. **3.3** `STATUS.md` gains
one POINTER entry — written BEFORE the commit so the commit carries it. **3.4** Discharge A3;
ONE commit, provenance-stamped, its message naming the waves it carries; guards re-run at the
committed tree. **3.5** `git push origin master` under R3's hard stop. **3.6** Report the
commit hash and the push result verbatim.

## 4. Accepted outcomes

**A1 finding the alias route insufficient (an alias set that differs by PowerShell version) is
reported with the version pinned, not papered over.** **A2 tripping is a revert-and-report.**
**A3 finding an unenumerated path is a STOP with the path named — never a silent sweep-in.**
**The push failing on credentials or a diverged remote is REPORTED VERBATIM and not worked
around — no force push, no rebase, no pull-merge without the user.**

## 5. Self-check (D-434) — run by Cowork before release

- **Ruling ledger:** R1 and R2 point at the ruling record read whole; R3 quotes the
  distribution hard stop rather than summarizing it.
- **#17(a):** three facts; three assumptions with ordered checks and STOPs.
- **Principles:** #19 at the corpus-first order; #6 at the one-remedy-per-defect-class reuse;
  #12 at the not-wrong-but-blind wording and the preserved former rates; #16 at guards re-run
  at the committed tree; D-431 — the one hash cited is provenance, not a measured figure;
  D-436 at the licensed mechanism change.
- **Scope:** no D-472 work; no upstream remote touched; push exactly one remote, one branch.
