# CC instruction — the notation consumption-surface audit (READ-ONLY) + Task 0: the ratification commit

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + newest
> entries), `C:\s\MS\BUILD_AND_TEST.md`, and **the ratified decision surface this dispatch
> executes: `C:\s\MS\cowork_notation_adoption_increment.md`** (user-ratified 2026-07-26 — the
> §1 verified state, the six rulings, the §8 verification plan). Also `OPEN_ITEMS.md` (session-
> start rule; note the NEW rows OI-193/OI-194 already on disk, riding your Task-0 commit).
>
> **Current state:** branch `master`; expected HEAD `205dd0843a` (the OI-178 adoption commit,
> pushed to origin) — verify by `git show --stat 205dd0843a` and that HEAD matches it; if HEAD
> differs, STOP and report. Working tree carries FIVE Cowork-authored uncommitted edits that
> ride Task 0: `cowork_notation_adoption_increment.md` (new file, the ratified decision surface),
> `OPEN_ITEMS.md` (rows OI-193/OI-194), `cowork_handoff.md` (the ratification addendum), plus the
> two files YOU edit in Task 0 (`CLAUDE.md`, `STATUS.md`). Verify these are the only non-yours
> diffs; anything else unexpected is a STOP. This dispatch file itself stays untracked
> (`/cc_*.md` ignore policy).
>
> **Hard stops, always:** any push toward `upstream` (`musescore/MuseScore`) — origin only;
> any file modification outside the Task-0 list and the Task-5 artifact locations; any
> `src/` edit whatsoever (this audit is READ-ONLY on the code); a surprise is a STOP (#13),
> not a workaround. The VS Code bash rules (CLAUDE.md) apply to every command: append
> `; echo "exit:$?"`, never large output un-redirected.
>
> **No mid-flight steering:** this instruction is self-sufficient; anything it does not cover
> waits for the report and is ruled at verification.

**Dispatch author:** Cowork, 2026-07-26, at the user's ratification of
`cowork_notation_adoption_increment.md` (all six rulings granted). This is the §8.1 step of the
ratified verification plan: the read-only audit that makes the Decision-A2 #12 check exhaustive
before any contract text or build dispatch is written.

---

## Task 0 — the ratification commit (ONE commit, before anything else)

The 2026-07-26 ratifications become a committed record (the 2026-07-18 principles-ratification
pattern, commit `06d4318bd1`).

**0.1 — CLAUDE.md: insert the ratified decision-neutrality corollary.** In the "Guiding
principles" section, AFTER the fact-publication corollary paragraph (the one ending "…kept in
sync as facts are adopted (OI-146).") and BEFORE the "*Provenance: principles 1–11…*" paragraph,
insert exactly:

```
*Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified
2026-07-26):* Designs are chosen from the principles and the ultimate objective — enabling the
best possible inference — alone. In that choice: **(a)** the value of reusing existing code, and
the cost of making existing code obsolete, are SECONDARY — they may break ties between designs
equal under the principles and the objective, and reuse counts only as carried-forward
establishment (#19), never as sunk cost or saved effort; **(b)** downstream implementation
impact — whether and how many consumers must change — carries NO weight; **(c)**
end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling),
while every behavior change remains ratification-gated (#14) and verification-gated (#15/#19)
exactly as before. The best-possible-inference design is chosen first; what exists then either
serves it or retires. (This does not weaken #6 — one path per concern is an END-STATE structural
principle, not a preservation claim for the existing path; nor #19 — establishment must still
exist before trust.)
```

Then, in the provenance paragraph, extend the ratification-history sentence — the one ending
"…operational rows OI-176…OI-181." — by inserting, before its final period: "; the
decision-neutrality corollary was ratified by the user on 2026-07-26 at the notation-layer
adoption increment's decision surface — analysis in `cowork_notation_adoption_increment.md` §2".
(Do not touch the paragraph's final "Companion standing rules elsewhere…" sentence.)

**0.2 — STATUS.md: add a new dated entry at the top** (above the current newest), exactly:

```
*Last updated: 2026-07-26, third entry (Cowork — **★ THE NOTATION-LAYER ADOPTION INCREMENT'S DECISION SURFACE IS USER-RATIFIED (`cowork_notation_adoption_increment.md`)** — the principles gain the decision-neutrality corollary (reuse/obsolescence secondary, counting only as carried-forward establishment #19; consumer-change impact and end-user behavior-change impact carry no weight; #14/#15/#19 gates unchanged — CLAUDE.md updated this commit), and the five design rulings: (A2) the joint-native record IS the notation surface, no compatibility view, `HarmonicRegion` retires with the legacy path; (B-full) the uncertainty contract is the FULL posterior (forward-backward marginals, status-marked model probabilities), delivered established-slice-first, completion rowed OI-193; (C1) two-mode key + the published un-rounded modal reading, no 21-value mode inferred again; (D1) fitted tables embedded as provenance-stamped generated source; (E) modal reading inside the increment, ornament labels their own increment, rowed OI-194. NEXT: the read-only notation consumption-surface audit (`cc_instruction_notation_consumption_audit.md`), then the contract drafting, then the build dispatches under the OI-180 sanction pattern.)*
```

**0.3 — commit** all six files (`CLAUDE.md`, `STATUS.md`, `OPEN_ITEMS.md`, `cowork_handoff.md`,
`cowork_notation_adoption_increment.md` — verify no other file is staged) as ONE commit,
message: `ratification record: notation-layer adoption increment decision surface + the
decision-neutrality principles corollary (user, 2026-07-26); rows OI-193/OI-194`. Push origin
only. Report the hash.

## Tasks 1–4 — the read-only audit (no code changes anywhere)

**The question the audit answers:** for every fact the live notation path consumes from the
legacy analysis surface, EITHER a declared source on A's surface (the `DecodeResult` fields +
the ratified planned publications: the full posterior OI-193, the un-rounded modal reading, the
ornament labels OI-194, the derived chord facts) EXISTS, OR the fact needs a declared
retirement-with-rationale — so that the Decision-A2 switch drops nothing silently (#12). Your
dispositions are PROPOSALS (input to Cowork/user rulings), not decisions.

**Task 1 — the consumer/field enumeration (the core).**
- **Scope check FIRST (the OI-175 lesson — a scoped sweep proves the scope, not the question):**
  enumerate tree-wide (all of `src/`, excluding pure test files, which are listed separately)
  every reader of the notation analysis output surface: consumers of
  `analyzeHarmonicRhythm(...)`'s returned stream, of `HarmonicRegion` and its nested records
  (`ChordAnalysisResult`/`ChordIdentity`/`ChordFunction`, `KeyModeAnalysisResult`,
  `ChordAnalysisTone`, `ChordTemporalExtensions`), and of the section/function-labeling records
  derived from them on the notation path (the `sectionanalyzer` output and its readers,
  the Roman-numeral/relational-label emitters, the accessibility surface, the implode and
  tuning bridges). The expected members (from the decision doc §1): `notationcomposingbridge`,
  `notationimplodebridge`, `notationtuningbridge`, `sectionanalyzer` + downstream function
  labeling, accessibility — but the tree-wide sweep decides the roster, not this list; report
  any member beyond it.
- Per consumed FIELD: file:line of the read; the fact it carries; its role
  (decision-bearing / presentation / diagnostic-only); and the disposition PROPOSAL —
  `A-SOURCED` (name the A-surface source: which `DecodeResult`/posterior/publication field),
  `DERIVABLE` (recomputable from A-published facts — name the derivation), or
  `RETIRE-CANDIDATE` (name what information would be lost and why that is acceptable or not).
  A field you cannot disposition is reported as `UNRESOLVED`, never guessed (#18/never-guess).
- Tests that pin the surface (`pipeline_snapshot_tests`, `notationimplode_tests`, others found)
  are enumerated in their own table (they follow the ratified switch; they do not decide the
  contract).

**Task 2 — the exotic-mode consumer list (Decision C1's disposition input).** Every site on the
notation path whose behavior branches on `KeySigMode` values beyond Ionian/Aeolian (switch/if on
mode, mode-name formatting, the 21 mode-prior plumbing from
`IComposingAnalysisConfiguration` through `notationharmonicrhythmbridge.cpp:92–113` including
any settings/UI surface feeding those preferences). Per site: file:line, what it does with the
exotic value, disposition proposal against the C1 rule (two-mode + published modal reading).

**Task 3 — the OI-182 constants' fate.** `notationimplodebridge.cpp:79–96`
(`kTentativeKeyExposureThreshold`, `kAssertiveKeyExposureThreshold`, `keyExposureBucket`) and
`kSameChordReannotationGap` (`:661`): enumerate what feeds them today (WHICH confidence value)
and what consumes their output, so the contract's confidence-mapping ruling (the B-full
posterior gap/mass replacing legacy confidences) can disposition them. Proposal only.

**Task 4 — the in-memory-only fields.** Confirm at the code (not from the decision doc) that
`keyAlternatives` and `fanout` still have no production consumer, and report any change.

## Task 5 — the generated artifact + the report

- **Artifact (#17f):** `tools/audit/notation_surface/` — a small read-only generator script (the
  `tools/audit` precedent) emitting `consumption_fields.csv` (Task 1, one row per consumed
  field) and `summary.json` (roster, counts per disposition class, the Task 2–4 lists), every
  figure in the report drawn from it, nothing hand-typed.
- **Report:** `cc_notation_consumption_audit_report.md` (untracked, per policy): method, the
  scope-check result, the tables, findings, UNRESOLVED items, unknowns/caveats. Include the
  standing **reuse-vs-new / what-retires** section (for this audit: the generator reuses the
  existing audit-tooling pattern; nothing retires — say so explicitly).
- **Commit (second, last act):** the `tools/audit/notation_surface/` artifacts only, message
  `notation consumption-surface audit artifacts (read-only; dispatch
  cc_instruction_notation_consumption_audit.md)`. Push origin only. The report stays untracked.

## STOP conditions (beyond the standing ones)

- HEAD mismatch or unexpected working-tree diffs at Task 0.
- A consumed, decision-bearing fact that is provably NOT derivable from A's surface plus the
  ratified planned publications is a **FINDING, not a stop** — report it `UNRESOLVED` with the
  evidence; it returns to the user as its own decision (the decision doc §3 anticipates this).
- A live production consumer of the analysis surface that your tree-wide sweep finds OUTSIDE
  the expected roster: include it in scope and flag it prominently (that is the sweep working).
- Any contradiction between what the code shows and a ratified ruling's premise: STOP, report,
  do not reinterpret.
- Any temptation to edit `src/` (even a comment): STOP — this dispatch is read-only on code.

## Report checklist

Task-0 commit hash + files; the audit's roster (expected vs found); per-task tables (from the
artifact); disposition-class counts; every UNRESOLVED item; the Task-4 confirmation; the
second commit hash; anomalies. The standing self-check (CLAUDE.md) applies: re-read your actual
diffs (the two commits) against the principles and DEFECT_TYPES.md before reporting.
