# CC dispatch — land the writing-side records, then the ARTIFACT INVENTORY: every file classified, a role and a mining verdict proposed per class

> **Status: ACTIVE DISPATCH, written 2026-08-15 (Cowork), at a verified STOP** — the period-checks
> batch completed, its three commits verified at the objects by the writing side (P1 checked cell
> by cell at the artifact; the fired hunk retrieved byte-identically at the git object), and its
> FULL close in `cowork_away_returns.md` read end to end. Nothing is running.
>
> **★ THE DIRECTIONS THIS DISPATCH APPLIES, QUOTED (D-643).** From
> `cowork_rulings_2026_08_15_method_directions.md` §2.10: *"THE ARTIFACT INVENTORY COMES FIRST —
> BEFORE THE PHASES ARE DRAFTED... A DERIVED walk of the tree (never hand-listed), every file
> classified by mechanical signature into classes with an unclassified STOP; per class: role per
> phase, mining verdict (including antipattern mining), retirement-candidate flag. Retirement
> destroys nothing (#12)... Verdicts are PROPOSED by the tool's surface and RULED by the user."*
> And §2.11's handover clause: *"Handover-safety is required at the latest by the next handover."*
> The eighteenth stop's §3 still binds: *"No repair is authorized."*
>
> **Read IN FULL, and read FIRST:** `cowork_rulings_2026_08_15_method_directions.md`;
> `cowork_rulings_2026_08_15_period_start.md`; `cowork_rulings_2026_08_13_eighteenth_stop.md`;
> the fifteenth entry block of `cowork_handoff.md`.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_artifact_inventory.md`. Acts dated from
> the clock; no positional count anywhere; rulings cited by number or by their record's file name.
>
> **★ All standing rules as adopted.** D-253 in every dialect — working-tree reads through the
> file tools; git object queries by explicit hash. NO TRANSCRIBED VALUES (D-431). Hold-don't-guess.
> **NO `src/` EDIT — no ruling permitting a named act is granted by this dispatch, and none is
> implied.** No golden, no test changed, no corpus of scores, nothing under `tools/corpus/` or
> `tools/robust_stop/`, no measurement of the analysis, no design, **no file moved, renamed,
> retired or deleted** — the inventory PROPOSES, the user RULES. D-231 and #8 stand. Commit and
> push per task boundary; `origin` only.

## 0a. THE PREDICTIONS, REGISTERED BEFORE ANYTHING RUNS (#17b)

**P1 — coverage.** Moderate confidence: an authored signature table of well under forty classes
covers every tracked file at HEAD, with the upstream MuseScore code, the build system and the
third-party libraries each ONE class with one verdict, so the fork's size costs nothing. **What
would refute it:** a final run whose unclassified bucket is non-empty — which is a STOP, not a
remainder.

**P2 — the mixed classes.** Moderate confidence: per-item descent (beyond class-level verdicts)
is needed only inside `docs/`, `tools/`, and the repository-root prose surfaces, where
specifications, reports, plans and generated artifacts interleave. **What would refute it:** a
class elsewhere whose members need opposite verdicts.

## 0b. THE PREMISE LEDGER (#17a)

**FACT:** the tracked tree at HEAD is enumerable from git objects; the writing-side records named
in Task 0 exist on disk untracked (CC's own §2.4 of the period-checks close). **ASSUMPTION —
each checked before the act resting on it; a refutation is a STOP.**

- **A1.** Path-and-signature classification is sufficient; no file content beyond banners and
  extensions is needed to class a file. *Check: the tool's unclassified bucket is EMPTY at the
  committed run, or the run is a STOP; no class is assigned by judgment of a file's substance.*
- **A2.** The population is the TRACKED tree at HEAD. Untracked files are NOT classified — they
  are listed whole in a separate appendix of the artifact (paths only), because an untracked file
  is either scratch or an un-landed record, and both are for the user to see, not for a tool to
  grade. *Check: the appendix is present even when empty.*
- **A3.** A PROPOSED verdict (role, mining, retirement flag) is an AUTHORED judgment and is
  marked as such, separately from every DERIVED count. *Check: the artifact separates
  `what_is_DERIVED` from `what_is_AUTHORED`, the shape `period_stratum_split.json` already uses.*

## 0c. THE TASKS, IN ORDER

**Task 0 — land the writing-side records (the handover-safety half).** Commit, in ONE commit,
exactly these files and nothing else: `cowork_rulings_2026_08_13_eighteenth_stop.md`,
`cowork_rulings_2026_08_15_period_start.md`, `cowork_rulings_2026_08_15_session_length.md`,
`cowork_rulings_2026_08_15_method_directions.md`,
`ratification_surfaces/cowork_restructuring_period_start_decision_surface.md`,
`cc_instruction_period_checks.md`, `cc_instruction_artifact_inventory.md` (this file), and the
modified `cowork_handoff.md` (the fifteenth entry block). These are the writing side's records;
this dispatch NAMES the act, which is what the period-checks close said such a commit needs.
Push. If any named file is absent or any UNNAMED file would be swept into the commit, STOP.

**Task 1 — the inventory tool (A1, A2).** Write `tools/audit/gen_artifact_inventory.py`, writing
`tools/audit/artifact_inventory.json`. It enumerates the tracked tree at HEAD from git objects,
classifies every file by an authored signature table (path pattern, extension, banner), and
publishes: the class list with each class's signature, count, total bytes, and example paths;
per-file class assignments for the prose and tools classes (the classes the ruling surface
descends into); the EMPTY-or-STOP unclassified bucket; and the untracked appendix (paths only).
`--check` re-derives from git objects and exits non-zero on drift. The artifact separates
DERIVED from AUTHORED and states the #19 caveat of its own signature table (authored, checked
only by the STOP). Grade P1. Commit and push.

**Task 2 — the ruling surface (A3).** Write
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md` — generated from the
artifact, one section per class: what it is; establishment status where the record already
states one; **PROPOSED role** (clean-room admissible / airlock input / mining witness / audit
material / regression pin / operational apparatus); **PROPOSED mining verdict** (mine directly /
mine via the airlock — including for ANTIPATTERNS / not worth mining, each with a reason);
**retirement-candidate flag** with grounds, and the reminder on its face that retirement is
archive-with-record, nothing destroyed (#12). Descend to per-item proposals ONLY where a class
is mixed (P2 names the expected three areas); bulk rules carry their counts. Every proposal is
marked AUTHORED and awaits the user's ruling; classes the writing side already flagged as open
rulings — the catalogs, goldens and `tools/robust_stop/` reference; the measurement layer's own
specifications — are presented as QUESTIONS, not proposals. Commit and push.

**Task 3 — the close.** One `STATUS.md` pointer entry per task, nothing else in that file.
Append the close to `cowork_away_returns.md`. Register the new tool in the guard set in the same
act that creates it (the period-checks precedent, so [[OI-373]]'s condition is not reproduced).
Report at the objects, with commit hashes.

## 0d. WHAT IS DELIBERATELY NOT DONE

**No file is moved, renamed, retired, archived or deleted** — every retirement is a PROPOSAL on
the ruling surface. **No repair**; the eighteenth stop's §3 stands whole. **No mining is
performed** — the register filter, the rulings sort and the findings ledger are LATER acts that
consume the ruled inventory. **No phase is defined and no spec is derived.** No open-items row
is marked, flipped or discarded; no decisions-register entry is written; [[OI-179]] stays OPEN
and GATES. The re-opened period question is untouched — it is the user's ruling, listed in
`cowork_rulings_2026_08_15_method_directions.md` §3.

## 0e. STOP RULES

Halt with a STOP in `cowork_away_returns.md` if: the unclassified bucket is non-empty at the
committed run; classifying any file would require judging its substance rather than its
signature (A1 refuted — name the file and the missing signature); Task 0 would sweep in an
unnamed file or a named one is missing; the tool's `--check` cannot reproduce its own output; or
a guard goes red for a cause that is neither this dispatch's own edits nor already recorded —
the three standing reds ([[OI-372]], [[OI-373]], and the unrowed guard-classification stall of
2026-08-13) are recorded and are not that.

---

*Provenance: Cowork, 2026-08-15. Executes §2.10 and §2.11 of
`cowork_rulings_2026_08_15_method_directions.md`. Form taken from
`cc_instruction_period_checks.md` and `cc_instruction_scoring_model_pass.md`, both read in full.
Self-check run before release (D-434).*
