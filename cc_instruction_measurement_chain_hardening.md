# CC INSTRUCTION — Measurement-chain hardening, wave 1 of the key-layer readiness gate — OI-145

> **Issued by Cowork, 2026-07-12.** The user directed (register row OI-145): every open
> issue that directly or indirectly impacts the key layer is FIXED before the key layer
> is built. This session is WAVE 1: the measurement chain — every future key-work probe
> and fit is graded through these instruments, so they come first. This is a FIXING
> session (the first in the arc): the fixes are integrity and hygiene work on the
> measurement instruments under `tools/` — NOT inference coding (the moratorium is not
> touched; no `src/composing` analysis behavior changes; the one C++ file in scope is
> the harness `tools/batch_analyze.cpp`).
>
> **The governing expectation, stated up front: NO GRADING DIGIT MOVES.** Every fix
> here is to failure paths, validation, duplication, and documentation. After each fix
> the establishment battery (below) must reproduce the committed results byte-for-byte.
> If a fix DOES move a grading — or exposes a poisoned artifact, a wrong figure, or any
> new issue — that is a DISCOVERY, exactly what the user said fixing might buy:
> STOP work on that item, record it as its own register row, report it prominently,
> and await the user's decision. Never silently absorb a moved digit.
>
> **Read first:** `OPEN_ITEMS.md` (rows OI-145 — the gate this executes — and every row
> listed below), `CLAUDE.md` in full (gate blocks = the contracts being hardened),
> `tools/REPRODUCIBILITY.md`, `BUILD_AND_TEST.md`, the instrument audit reports
> (`cc_l5_audit_pass1_instruments_report.md`, `cc_l5_audit_pass1_grading_fitting_report.md`,
> `cc_l5_audit_pass1_harness_report.md`, `cc_l5_audit_pass2_report.md`). Open-book.
>
> **REMINDERS:** each row's fix is ONE revertible commit (guiding principle 14) —
> tightly-coupled rows may share a commit only when they change the same mechanism
> (say so in the message); register flips ride the SAME commit as their fix; no
> self-invented labels or jargon; the self-check over every diff before reporting
> done; never stop a long-running process; shell rules (`; echo "exit:$?"`, redirect
> large output); git rules (stage only your own files by name, never `git add -A`,
> `git status` after every commit; the known carry `cowork_joint_key_chord_design.md`
> stays unstaged; `cc_*.md` gitignored — force-add this instruction in the fold); push
> to `origin` only, never `upstream` — the standing hard stop, `git remote -v` first.

## Task 0 — Preconditions and the register commit

0. **Commit Cowork's waiting edits** (the OI-145 gate row + the OI-141 design-opening
   update + the design opening document):
   ```
   git add OPEN_ITEMS.md
   git add cowork_key_layer_design_opening.md
   git add -f cc_instruction_measurement_chain_hardening.md
   git commit -m "docs(cowork): OI-145 the key-layer readiness gate (user directive: fix everything the key layer depends on first) + the key-layer design opening (read with caveat) + the wave-1 hardening instruction"
   ```
   Then `git status --short; echo "exit:$?"` — remaining: the known carry plus
   untracked scratch only; anything else, stop and report.
1. `git rev-parse HEAD; echo "exit:$?"` and the ancestor check against the current
   head recorded in `STATUS.md`'s newest entry; no `git log` restriction this session
   (open-book).

## Task 1 — The establishment battery (run BEFORE any fix, then after EVERY fix)

Define once, script it, commit it as the session's instrument
(`tools/audit/hardening_battery.py` or the simplest equivalent): the a8 regression-stop
run + diff vs the committed reference (must PASS, +0/−0, coverage unchanged), the
fitting fixture reproduce (must MATCH the ratified figures), the calibration maps
byte-identity, `validate_corpus_dir` on all three presets, and — whenever
`tools/batch_analyze.cpp` was touched — a full scratch corpus regeneration compared
per-score sha256 against the committed corpus (must be identical, as the harness audit
proved at head). Run it FIRST to record the clean starting state. Any post-fix battery
deviation = the discovery protocol above.

## Task 2 — The five blocking rows, in this order

1. **OI-140 — the governing stop's silent ground-truth swallow.** In the a8
   instrument, a WiR parse failure currently becomes an empty region list and a
   silent exclusion. Fix: parse failures are counted and NAMED in the summary
   (per-stem), and `robust_stop_diff` reconciles WiR coverage against the committed
   reference — a coverage shrink FAILS the diff loudly. The committed reference
   manifest gains the coverage figures (a metadata re-stamp, gradings untouched —
   explain the manifest diff in the report).
2. **OI-124 — the unfingerprinted ground truth.** Extend the corpus validation so the
   `.music21.json` ground-truth files (and the WiR source files' identity, via the
   offsets-file pattern already established) are fingerprinted like the `.ours.json`
   files: manifests regenerated with the added fingerprints (metadata-only — prove
   the gradings byte-identical), `validate_corpus_dir` checks them,
   `robust_stop_diff` cross-checks the baseline it reads against the manifest it
   claims. If any EXISTING committed ground-truth file turns out poisoned (for
   example a 0-region `.music21.json` from a historical chordify failure — the
   OI-123/OI-128 failure shape), that is a DISCOVERY: stop, row, report.
3. **OI-129 — the grading chain skips validation.** `calibration_fit` and
   `c1_reliability` (and any graded consumer found in the same state) route through
   `validate_corpus_dir` before reading a corpus directory.
4. **OI-132 — two key-parser paths in the grading tools.** Single-source the key
   parsing into the one shared substrate (the `dcml_parser` route every graded
   consumer now uses); delete the dead duplicate and the dead `lt_2` helper; the
   battery proves the consolidation changed no output.
5. **OI-33 — the abstain-aware grading convention.** Write the convention down where
   the instruments' contract lives (the coverage figure reported beside every graded
   figure, so opting out can never flatter a result), and implement the coverage
   column in the graded outputs that lack it. Convention text + mechanical
   enforcement, both.

## Task 3 — The remaining wave-1 rows

In severity order, same discipline (one row, one commit, battery after each):

- **OI-123 / OI-128 — silent exception swallows** in the regression-stop core and the
  grading/fitting instruments: narrow every broad catch to the specific expected
  condition, log what is skipped WITH the stem, and make the wrong-bucket folds
  (`no_wir` mis-classification; the chordify-failure 0-region GT write) impossible —
  a failed GT production writes a failure record, never a fake GT file.
- **OI-130 — destructive default output paths + the unenforced pin:** no instrument
  defaults its output into `tools/corpus/`, the committed calibration maps, or the
  registries — explicit output arguments required (the DT-24 family closed at the
  producing side); the music21 version pin is checked at run start where GT is
  produced.
- **OI-135 — the harness's hand-copied constants:** single-source the "Default"
  preset's 21 mode priors from their owning source and the hard-coded
  `onsetBoundaryThreshold` from its preference; the corpus-regeneration battery
  proves byte-identity (the values are copies TODAY — single-sourcing must change
  nothing).
- **OI-126 — dead + duplicated instrument code:** delete `parse_dcml_file` /
  `find_dcml_file` if truly dead (verify at callers fresh), single-source the
  note→pitch-class map (three copies).
- **OI-125 — hand-set grading tolerances:** centralize into one named, commented
  constants block per instrument with provenance notes (documentation + single home;
  re-derivation is later work, flagged per constant).
- **OI-35 — the stale-manifest process gap:** the validate-or-re-manifest rule the
  row records, implemented at the read sites that today trust stale manifests.
- **OI-136 / OI-137 / OI-138 / OI-139 — harness + doc precision:** the six parsed
  flags documented in the help text; the CRLF/LF and exit-path asymmetry either
  fixed (if provably inert via the battery) or documented as intentional with the
  flush guarantee stated; the stale docstring figures, dangling anchors, and
  manifest site-lines corrected to current fact.
- **OI-144 — the ~50 secondary scripts on the raw parse:** scoped per the row — any
  script found to feed a GRADED surface routes through `load_wir_regions` (the
  offsets-corrected substrate); purely exploratory scripts get a one-line header
  warning that their view is uncorrected. No mass rewrite.

## Task 4 — Report, register, push

1. `cc_measurement_chain_hardening_report.md`: per row — what changed, the commit,
   the battery result after it; the full discovery list (found issues, new rows,
   anything that moved — expected: nothing); the before/after establishment battery
   records; the state of OI-145 wave 1 (which rows closed, which remain and why).
2. Register discipline: every fixed row FLIPPED in the same commit as its fix; every
   discovery gets its row; OI-145 updated with wave-1 completion state. Update
   `STATUS.md` (prepend) and the entry block of `cowork_handoff.md`. Plain language
   everywhere.
3. Run the self-check over every diff before reporting done. **Push —
   user-authorized 2026-07-12:** all local commits to `origin` only, after
   `git remote -v` confirms `upstream` push is still disabled; anything that would
   touch `upstream` is the standing hard stop. Confirm in the report: the pushed
   hash, `upstream` untouched.
4. If the session cannot honestly complete all of Task 3 at full rigor, STOP at a
   row boundary with the battery green, report what is done and what remains —
   never thin the verification to fit.
