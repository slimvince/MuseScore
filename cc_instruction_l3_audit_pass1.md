# CC INSTRUCTION — Layer-3 (key/mode) Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Issued by Cowork, 2026-07-11.** Layers 1 and 2 were certified by the user today; the
> audit plan's dependency order names layer 3 — the key/mode inference layer — as the next
> layer to audit. This is the FIRST of two passes; certification is NOT granted here. The
> audit protocol is `cowork_audit_protocol.md`; this instruction carries out its
> enumerate-then-classify inventory, closed-verdict dispositions, contract-direction check,
> and behavioral characterization (steps P1–P4), blind (step P8, first run).
>
> **REMINDERS — the standing rules you work under (read `CLAUDE.md` in full; these are
> pointers, not replacements):**
> - Guiding principle 8: no inference-problem fixing until ALL refactoring, architectural
>   design, and algorithmic completion are done. You fix NOTHING in this session. A
>   discovered violation — even an obvious bug — becomes a register row, never a patch.
> - Guiding principle 7: any amendment belongs to the layer that owns the concern; you are
>   an auditor here, not an amender.
> - Guiding principles 15 and 19: verify at the actual code and data, never at assertion —
>   including assertions in comments, docs, and earlier sessions' reports.
> - The conventions: no self-invented labels, abbreviations, numbering schemes, or jargon —
>   in your report, register rows, commit messages, everywhere. Use existing repository
>   names or plain words.
> - The self-check rule (`CLAUDE.md`, 2026-07-11): after every coding exercise — scripts
>   and document edits included — and before reporting done, re-read the actual diff of
>   every touched file and check it against the principles, the conventions, and the gate
>   policies. The check against `DEFECT_TYPES.md` happens only after your Task-4 freeze,
>   since that file is withheld until then.
> - Shell rules: append `; echo "exit:$?"` to any command that may return non-zero;
>   redirect large output to a file and read the file.
> - Git rules: stage only your own files, named one by one; never `git add -A`. After any
>   commit, confirm with `git status` that disk matches the commit (the register row OI-85
>   convention). The working tree may carry the user's or Cowork's uncommitted edits —
>   leave them untouched. Note: `cc_*.md` files are gitignored; tracked ones follow the
>   established force-add (`git add -f`) convention.
> - Push rules: `origin` (the user's fork, `slimvince/MuseScore`) only. NEVER `upstream`
>   (`musescore/MuseScore`) — the standing hard stop. Verify with `git remote -v` first.
>
> **⚠ WITHHELD READS (blinding, protocol P8 first run, strengthened per catalog row DT-20).**
> Pass 1 must enumerate without the known-problem catalog or prior findings anchoring it.
> Do NOT open any of the following until your Task-4 freeze commit exists:
> `DEFECT_TYPES.md`, `OPEN_ITEMS.md`, `STATUS.md`, `cowork_handoff.md`,
> `cowork_siloed_facts_audit.md`, `cowork_adjudication_dossier.md`, and every
> `cc_*_report.md`. The mandatory session-start read of `OPEN_ITEMS.md` is deferred to
> Task 5 — deliberately, declared here so the user sees it: the register now carries rows
> naming layer-3 suspects, and Cowork performed the session-start register check for this
> dispatch instead (no open register row gates the layer-3 audit). Declare in your report
> when each withheld file was first opened. Safe reads from the start: `CLAUDE.md`,
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`, the roadmap (needed
> for the layer definitions and the retirement map; it names planned retirements — that is
> scope information you need, accepted and declared), the pass-1 inventory instruments and
> tables under `tools/audit/` (scope, not verdicts — do NOT open the `*dispositions*`,
> `*blind*`, `*errorrate*`, `*compare*`, or `sweep_results*` files there), and the source
> code itself.
>
> **Scope declaration:** READ-ONLY fact-finding. No production behavior change; no
> constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/` reference
> artifacts untouched. Surprises in the audited code are findings to record; a surprise in
> your own tooling is a stop — fix the tool, restamp, rerun, never hand-edit a generated
> artifact.

## Task 0 — Preconditions

0. **First action — commit Cowork's waiting register edits** (their content is Cowork's,
   user-ratified today, summarized in this preamble: the two register rows recording the
   user's L1/L2 certification, plus this instruction file). Stage WITHOUT opening the
   register (staging needs no reading):
   ```
   git add OPEN_ITEMS.md
   git add -f cc_instruction_l3_audit_pass1.md
   git commit -m "docs(cowork): L1/L2 certification GRANTED by the user (OI-84/OI-89 updated) + the layer-3 audit pass-1 instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining entries should be only the known
   OI-51 carry (`cowork_joint_key_chord_design.md`) and untracked scratch; anything else,
   stop and report. If a file has nothing to stage, say so and continue.
1. Check the git state WITHOUT displaying commit messages (recent messages summarize
   audit findings): `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 6e62d7f9e4 HEAD; echo "exit:$?"` — the second must print
   `exit:0`.
2. Do not read the withheld files.

## Task 1 — The machine-generated inventory (protocol P1)

1. **Extend `tools/audit/gen_inventory.py` — do not write a second inventory instrument**
   (one path per concern). It already tags every file in `src/composing/`; add the deep
   row extraction for the files tagged as layer 3. The layer-3 definition comes from
   `ARCHITECTURE.md` and the roadmap's layer definitions (read them; do not guess); the
   existing file table's tags are your starting point, but re-verify the layer-3/mixed
   tags at the code — a mis-tagged file is a finding of pass 1, not something to inherit
   silently. Where a file mixes layers, its layer-3 parts are in scope and the split is
   recorded.
2. For every layer-3 file: the complete row lists, same shape as before — functions and
   methods; numeric literals (the trivial-0/1 exclusion rule stays IN the script);
   fields visible outside the file; branches in non-trivial functions; cross-layer calls
   in BOTH directions (what layer 3 reads from below, what it publishes upward, and any
   upward include out of layer 3 into layer 4 or 5).
3. Artifacts under `tools/audit/l3/` as CSV/JSON; stamp `tools/audit/l3/manifest.json`
   with HEAD commit, script state, corpus hash `c50002fee1`, and row counts. The script
   fails if any file lacks a disposition tag. Commit script + artifacts as one
   `feat(tools):` commit.

## Task 2 — Dispositions (protocol P2 + P3)

For EVERY inventory row, a verdict from the closed set — "no issue" is a recorded claim
with a stated reason, never a blank:

- Causal premises (code whose correctness rests on a claim about music, scores, or our
  own system): FACT (citation) / THEORY (citation to published research answering the
  specific question) / ASSUMPTION (flag — future register row).
- Derived facts (anything computed that a consumer could want — pay attention to key
  alternatives, margins, runner-up information, and per-region key metadata): PUBLISHED /
  SILOED / TRAPPED / DUPLICATED, under the fact-publication corollary in `CLAUDE.md`
  (published once on the producing layer's surface; a fact consumed by no one is declared
  dormancy with its future consumer named, or waste).
- Numeric literals and constants: ESTABLISHED (fit or derivation provenance) / UNFIT
  (hand-set) / DEAD (no effect) — and whether each appears in `tools/param_manifest.json`.
- Code: RETIRES (per the roadmap retirement map, with the note on what embedded
  interpretation must be consciously kept or rejected at deletion) / SURVIVES.
- Per row, the same four questions: what does it assume? what does it publish? who
  consumes it? what happens at its edge cases (empty input, single-slice regions, ties,
  key changes at region boundaries, pickup measures, enharmonic keys, modal ambiguity)?

**The contract direction is mandatory (protocol P3):** from what `ARCHITECTURE.md` and the
roadmap say layer 3 must deliver to the layers above, enumerate every expected output and
behavior and locate each in the code — or flag the absence. Absences are findings of the
same rank as positives.

## Task 3 — Behavioral characterization (protocol P4)

For every layer-3 mechanism and branch: measure its fire rate on the pinned corpus
(`c50002fee1`; Baroque preset unless preset-gated). Least-invasive route first: existing
diagnostic dumps and standalone scripts over the public interfaces; where only
instrumentation can count, a minimal default-OFF counter as its own revertible
`feat(tools):` commit with production byte-identity re-proven (standard corpus
regeneration, zero diff, both test suites green, NO golden refresh); where even that is
disproportionate, the row says "fire rate not measured" with the reason — flagged, never
silently skipped. Report per row: fire count, population, and whether the rate matches
the mechanism's documented intent — a mechanism that never fires, always fires, or
wildly misses its documented population is a finding.

## Task 4 — Freeze (the blinding boundary)

Write the full disposition artifact (`tools/audit/l3/pass1_dispositions.csv` and `.json`)
plus the report draft; commit; record the hash in the report. THIS commit lifts the
withheld-reads list.

## Task 5 — Unblind, promote, report, fold, push

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read),
   `DEFECT_TYPES.md`, `STATUS.md`. Where a pass-1 finding coincides with an existing
   register row, say so and reference the row instead of duplicating it.
2. Any NEW problem TYPE your findings imply (a pattern, not an instance) is promoted into
   `DEFECT_TYPES.md` in the same commit as the report. Do NOT run the second-pass
   signature sweep — that is the next instruction, for a fresh session.
3. `cc_l3_audit_pass1_report.md`: inventory sizes and manifest; disposition summary
   (counts per verdict class); EVERY flagged row with file and line and one
   plain-language sentence for a reader who does not know the code; the fire-rate table;
   the RETIRES list with its interpretation-check notes; when each withheld file was
   first opened. Every discovered issue gets an `OPEN_ITEMS.md` row (next free number) in
   the SAME commit as the report; new types get their catalog rows. Update `STATUS.md`
   (prepend) and the entry block of `cowork_handoff.md` as usual. Plain language
   everywhere.
4. Run the self-check over every diff before reporting done.
5. **Commit and PUSH (user-authorized 2026-07-11):** commits are the Task-0 commit, the
   Task-1 `feat(tools):`, any Task-3 counter `feat(tools):`, and one `docs(cc):` fold —
   each revertible, own files only. Then push all local commits to `origin` only, after
   `git remote -v` confirms `upstream` push is still disabled. Anything that would send
   content toward `upstream` is the standing hard stop — stop and report instead.
   Confirm in the report: the pushed hash, `upstream` untouched.
