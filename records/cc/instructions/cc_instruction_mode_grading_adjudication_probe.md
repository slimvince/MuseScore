# CC INSTRUCTION — The mode-grading adjudication probe (read-only) — OI-132 / OI-145 wave 1

> **Issued by Cowork, 2026-07-12.** The wave-1 hardening surfaced a genuine
> music-theory disagreement between two graded tools: they reduce our analyzer's
> dominant-family exotic modes (Phrygian dominant, the altered scale, Lydian dominant
> — the modes whose tonic triad quality and parent collection point in different
> directions) to major-or-minor DIFFERENTLY for key-agreement grading. Consolidating
> to one shared rule (the OI-132 fix) moves a graded figure whichever rule wins, so
> the USER rules on the rule — and this probe produces the evidence that ruling needs.
> READ-ONLY: both candidate rules are computed side by side in the probe only; the
> graded pipeline is not touched; the consolidation + ritual re-baseline happen at the
> subsequent combined event (together with the OI-144 calibration-map refit), after
> the user's ruling.
>
> **The two candidate rules, plainly:**
> - **Tonic-triad quality:** a key is named by its tonic chord — Phrygian dominant's
>   tonic triad is major, so a span our engine labels Phrygian dominant grades as
>   MAJOR (of the same tonic).
> - **Parent collection:** Phrygian dominant is the fifth mode of harmonic minor, so
>   the span grades as MINOR (of the collection's tonic — a different tonic).
> The right rule is the one that matches what the DCML annotators actually wrote for
> such spans — measured, not argued from the armchair.
>
> **Cowork's written expectations (#17, recorded before you look; answer each
> met/failed):** (1) the disagreeing population is SMALL — under 1 % of graded
> duration on Baroque/Default, possibly more on Jazz; (2) for Phrygian-dominant
> spans, the PARENT-COLLECTION rule matches the annotators' practice on 60 % or more
> of desk-checked cases (such spans in chorales are usually dominant-heavy passages
> the annotator keeps in the minor key), while for altered/Lydian-dominant spans the
> evidence may lean the other way; (3) the two rules' whole-corpus key-agreement
> difference is under 0.5 percentage points per column per preset. Weakly held —
> that is why we measure.
>
> **Read first:** `OPEN_ITEMS.md` (OI-132 carries the discovery; OI-145 the gate),
> `CLAUDE.md`, `cc_measurement_chain_hardening_report.md` (the discovery's record),
> `tools/REPRODUCIBILITY.md`, `BUILD_AND_TEST.md`. Open-book; surprises are findings
> except in your own tooling.
>
> **REMINDERS:** READ-ONLY — no graded-pipeline change, no constant tuned, no golden
> refresh; `tools/robust_stop/` and `tools/corpus/` written by NOTHING (scratch
> only); findings become register rows, never patches; verify at the code and data,
> never at assertion; no self-invented labels or jargon; the self-check over every
> diff; shell rules (`; echo "exit:$?"`, redirect large output); git rules (stage
> only your own files by name; never `git add -A`; `git status` after every commit;
> the known carry `cowork_joint_key_chord_design.md` stays unstaged; `cc_*.md`
> gitignored — force-add this instruction in the fold); push to `origin` only,
> never `upstream` — the standing hard stop, `git remote -v` first.

## Task 0 — Preconditions

1. `git rev-parse HEAD; echo "exit:$?"` and
   `git merge-base --is-ancestor 26f53b5ba2 HEAD; echo "exit:$?"` — the second must
   print `exit:0`. The working tree should hold only the known carry + untracked
   scratch; anything else, stop and report.

## Task 1 — Enumerate the disagreeing population, mechanically

A committed probe script (read-only over the committed corpus + ground truth through
the one corrected substrate): for every graded region on all three presets, compute
the major/minor reduction of OUR emitted key/mode under BOTH candidate rules; a
region enters the disagreeing population iff the two rules yield different graded
outcomes (different mode, or different tonic, or different agreement verdict against
either ground-truth column). Report: the population's size (regions and duration,
absolute and as a share of graded duration, per preset), its composition by our
emitted mode label, and the stems it concentrates in.

## Task 2 — Grade both rules corpus-wide

Both key-agreement columns (home and local), all three presets, under rule A and
rule B — eight figures per preset, with the deltas. Establishment: with the
disagreeing population EXCLUDED, both rules must reproduce the committed columns
exactly (the rules differ only where they differ — prove it). Coverage reported
beside every figure per the abstention convention.

## Task 3 — Desk-check the cases against the annotators

From the disagreeing population, select 6–10 regions covering the mode labels and
presets involved (include every Phrygian-dominant case if there are few). For each,
at the score and the ground-truth annotation text: what did the annotator actually
write for this span (the local key line, the chords)? Which rule's reduction matches
that practice? One plain-language paragraph per case, citing the stem, the ticks,
our emitted mode, both reductions, and the annotator's text. Tally the verdicts per
mode label.

## Task 4 — Report, register, push

1. `cc_mode_grading_adjudication_probe_report.md`: the population; the eight-figure
   table with deltas; the establishment proof; the desk-check cases with the tally;
   the three expectations answered met/failed; a closing statement of which rule the
   evidence supports, per mode label if they split — measurement, not a decision;
   the ruling is the user's. Machine-readable results beside it under
   `tools/reports/`.
2. Register discipline: update OI-132 with the probe's outcome (ruling pending with
   the user); any new discovery gets its own row in the same commit. Update
   `STATUS.md` (prepend) and the entry block of `cowork_handoff.md`. Plain language
   everywhere.
3. Commits: one `feat(tools):` for the probe script + artifacts; one `docs(cc):`
   fold (force-add this instruction). Run the self-check over every diff.
   **Push — user-authorized 2026-07-12:** all local commits to `origin` only, after
   `git remote -v` confirms `upstream` push is still disabled; anything that would
   touch `upstream` is the standing hard stop. Confirm in the report: the pushed
   hash, `upstream` untouched.
