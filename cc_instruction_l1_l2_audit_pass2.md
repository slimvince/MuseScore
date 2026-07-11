# CC INSTRUCTION — L1/L2 Certification Audit, second pass — EG-7 / OI-84

> **Issued by Cowork, 2026-07-11.** This is the second and final pass of the audit of
> layers 1 and 2. Certification of these layers is decided here, following the audit
> protocol in `cowork_audit_protocol.md`. This instruction carries out three parts of that
> protocol: the independent second reading (protocol step P5), the measured error rate
> (protocol step P6), and the sweep with the catalog of known problem types (protocol step
> P8, second run).
>
> **Read first, in this order:** `CLAUDE.md` (the guiding principles and the conventions —
> note the convention added 2026-07-11: no self-invented labels, abbreviations, numbering
> schemes, or jargon; use existing repository names or plain words),
> `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `STATUS.md`.
>
> **Push rules:** the only allowed remote is `origin`, the user's fork
> (`slimvince/MuseScore`). Never push to `upstream` (`musescore/MuseScore`) — that is the
> standing hard stop recorded in `CLAUDE.md` around commit `cfc7eb5e39`.
>
> **Shell rules (from `CLAUDE.md`):** append `; echo "exit:$?"` to any command that may
> return non-zero; redirect large output to a file and read the file.
>
> **What you may not read yet:** to keep your independent second reading honest, you must
> form your own judgments before seeing what the first pass concluded. Therefore do NOT
> open any of the following until Task 1 is finished and committed:
> `cc_l1l2_audit_pass1_report.md`, `tools/audit/l1l2/pass1_dispositions.csv`,
> `tools/audit/l1l2/pass1_dispositions.json`, `cowork_siloed_facts_audit.md`,
> `cowork_adjudication_dossier.md` — and also `OPEN_ITEMS.md`, because it now contains
> rows summarizing the first pass's findings. Deferring `OPEN_ITEMS.md` deviates from the
> standing rule that it is read at session start; the deviation is deliberate, limited to
> Task 1, and declared here so the user sees it. In your report, state at which point you
> first opened each of these files.
>
> **What this session is and is not:** read-only fact-finding. You change no production
> behavior, tune no constant, refresh no test golden, and leave `tools/robust_stop/` and
> `tools/corpus/` untouched. If you find a problem — even an obvious bug — you record it
> as a row in `OPEN_ITEMS.md` and describe it plainly; you do not fix it. Fixing waits
> until all refactoring, architectural design, and algorithmic completion are done
> (guiding principle 8), and any eventual fix belongs to the layer that owns the concern
> (guiding principle 7). Unexpected findings in the audited code are findings to record,
> not reasons to stop; an unexpected failure in your own tooling is a stop — fix the tool,
> re-stamp, re-run, and never hand-edit a generated artifact.

## Task 0 — Preconditions

1. `git log --oneline -1` must show a commit at or after `68f0b2c59b` (the first pass's
   documentation commit).
2. The working tree may contain the user's or Cowork's uncommitted edits. Known at time of
   writing: an edit to `cowork_joint_key_chord_design.md` (register row OI-51) and possibly
   an edit to `CLAUDE.md`. Leave all of these untouched. When you commit, stage only your
   own files, named one by one; never use `git add -A` or `git add .`. After any commit
   made through low-level git commands, run `git status` and confirm the files on disk
   match the new commit — the first pass hit an incident (register row OI-85, catalog row
   DT-18) where committed content and the files on disk disagreed.
3. Do not read `OPEN_ITEMS.md` yet, as explained above.

## Task 1 — The independent second reading (protocol step P5)

You are a second reader working without knowledge of the first pass's verdicts. Your job
is to find what the first pass got wrong or missed. You succeed by finding disagreements,
not by confirming.

1. Read only the first pass's row inventory under `tools/audit/l1l2/` (the tables listing
   every function, numeric literal, externally visible field, branch, and cross-layer call,
   plus `manifest.json`). Do not read the verdict files named above.
2. Write a small script (for example `tools/audit/gen_pass2_sample.py` — commit it; no
   hand-picked rows) that draws a random sample of at least 100 rows from that inventory,
   using a fixed random seed recorded in the output. The sample must be spread across the
   five row kinds in proportion to their counts, and every file the first pass classified
   as belonging to layer 1 or layer 2 must be represented. Base the spread only on the
   inventory's own structure, never on anything the first pass concluded.
3. Judge every sampled row yourself, from scratch, using the fixed verdict vocabulary in
   `cowork_audit_protocol.md` (step P2) and its four standing questions: what does this
   row assume, what does it publish, who consumes it, and what happens at its edge cases.
   Verify claims by looking at the actual code and data, not by trusting comments or
   documentation. Work through the rows in the random order the script produced.
4. Write your verdicts to `tools/audit/l1l2/pass2_blind_sample.csv` and `.json`, and
   commit the script and the results as one commit with a `feat(tools):` message. Record
   that commit's hash in your report. From this point the reading-restriction above is
   lifted.

## Task 2 — Compare the two readings

1. Now read, in this order: `OPEN_ITEMS.md` in full (the deferred mandatory read),
   `DEFECT_TYPES.md`, `cc_l1l2_audit_pass1_report.md`, and the first pass's verdict files.
2. Compare your verdicts with the first pass's on the same rows. Treat every disagreement
   as a stop-and-diagnose case: work out which step of the protocol allowed the first pass
   to miss or misjudge the row (incomplete inventory? ambiguous verdict vocabulary? the
   contract-side check skipped? a misread behavior measurement?), and classify each
   disagreement as a substantive miss, a difference in wording, or a genuine judgment tie.
   Record the diagnosis for each one, and report the overall disagreement rate.

## Task 3 — Sweep the whole layer with the catalog of known problem types

Apply every entry of `DEFECT_TYPES.md` — all nineteen, including the two added after the
first pass — across the ENTIRE inventory of layers 1 and 2. All rows, not a sample. This
is the main instance-finding work of this pass.

1. For catalog entries whose detection rule is mechanical, write one committed script (for
   example `tools/audit/gen_signature_sweep.py`) that runs every such rule and writes a
   hit table per catalog entry under `tools/audit/l1l2/`. The script must fail loudly if
   any mechanical rule could not be run, rather than skipping it silently.
2. For catalog entries that require human reading, go through the inventory row by row and
   record, per entry: how many rows were checked and every hit.
3. For every hit, record the file and line, one plain-language sentence a reader who does
   not know the code can understand, and whether it is already covered by an existing
   `OPEN_ITEMS.md` row (name the row) or is new.
4. If the sweep reveals a NEW KIND of problem — a pattern, not just another instance — add
   it to `DEFECT_TYPES.md` in the same commit as your report, following the standing rule
   that every newly discovered problem type gets its catalog entry in the commit that
   records its discovery.

## Task 4 — Measure the audit's own error rate (protocol step P6)

1. Draw a second random sample: 40 rows from the full inventory, uniformly random, with a
   different fixed seed, also recorded. (The user may direct a larger number; 40 is
   Cowork's proposal.)
2. For each of the 40, verify the first pass's verdict thoroughly at the actual code and
   data — read the code, its callers, and whatever else settles the question.
3. The fraction of these 40 where the first pass was wrong is the audit's measured error
   rate. Report it as a number and list the failing rows. Every wrong verdict gets the
   same stop-and-diagnose treatment as in Task 2. If a wrong verdict implies a whole class
   of rows was judged wrongly, say so plainly — that class must be re-examined; it must
   not be averaged away.
4. State a certification proposal: propose certifying layers 1 and 2 only if both passes
   are complete, the error rate is measured, and every disagreement is diagnosed;
   otherwise propose withholding certification and name concretely what remains. You only
   PROPOSE. Cowork verifies your report against the code, and the user decides. In the
   report and in any register row, write the status as "proposed, awaiting the user's
   decision" — do not mark the audit plan (register row OI-84) or the entry-gate condition
   (EG-7) as satisfied yourself.

## Task 5 — Report, documentation, push

1. Write `cc_l1l2_audit_pass2_report.md` containing: how both samples were drawn and their
   seeds; when each withheld file was first opened; the comparison table from Task 2 with
   a diagnosis per disagreement; the per-catalog-entry sweep results from Task 3; the
   error rate from Task 4 with its failing rows; and the certification proposal with
   exactly what it rests on.
2. Every newly discovered issue gets its own `OPEN_ITEMS.md` row (next free number) in the
   same commit as the report. Issues the first pass already registered are referenced by
   their existing row, not duplicated. Update `STATUS.md` (prepend to the most-recent
   block) and the entry block of `cowork_handoff.md` as usual. Write everything in plain
   language; coin no new terms or abbreviations.
3. Commits: the Task-1 commit described above; if the Task-3 sweep script warrants its own
   commit, a second `feat(tools):`; then one documentation commit with a `docs(cc):`
   message for the report and the updated shared documents. Each commit revertible on its
   own; stage only your own files.
4. **Push — authorized by the user 2026-07-11:** after the documentation commit, push all
   local commits — including the first pass's two commits `68e71665ce` and `68f0b2c59b` —
   to `origin` only. Before pushing, run `git remote -v` and confirm the `upstream` remote
   still cannot be pushed to. If anything about the push would send content toward
   `upstream`, stop and report instead — that is the standing hard stop. Confirm in the
   report: the hash pushed to `origin`, and that `upstream` was untouched.

## Standing constraints

- No fixes of any kind, however obvious. A live bug is described loudly in its register
  row and left alone.
- If you believe an instrument would require touching production code to do its job, stop
  and report instead of building it.
- Never guess a file's layer, a constant's origin, or who consumes a value — verify at the
  code and data, or record UNKNOWN together with what would settle it.
- Exclude wall-clock and timing fields from any byte-for-byte comparison.
- You may not grant certification; you propose it (Task 4, point 4).
