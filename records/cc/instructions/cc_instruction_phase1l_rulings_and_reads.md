# CC dispatch — phase 1l: apply the 2026-08-03 second ruling set, then continue the full reads

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date.** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1l_rulings_and_reads.md` — in every
> commit message. The phase-1k commits (`7454abe5db`, `16f1f1775e`) cited a dispatch filename that
> does not exist anywhere in the tree; Task 2 repairs that, and the same mistake must not be made
> twice. Copy the name, do not retype it from memory.

## 0. Standing constraints that govern every task below

These are the user's, restated because a dispatch that omits them invites the failure:

1. **Every amendment lands in the PROPER LAYER** (#7). A rule about the estimator goes in the
   estimator's specification; a rule about a document's status goes in that document. Never a
   cross-layer patch.
2. **NO inference-problem fixing.** D-231's three phases govern: this is phase 1. No fix, no
   design, no behavior change, no `src/` edit, no golden refresh, no `tools/corpus/` or
   `tools/robust_stop/` movement.
3. **Never use the shell to read working-tree files.** Content, existence, line counts and searches
   go through the file tools. Shell access is for read-only git object queries by explicit commit
   hash, and for running the guard and generator scripts this dispatch names.
4. **Never work from memory.** Every claim written into a specification or an entry cites its
   primary source file:line, re-read in this session.
5. **A surprise is a STOP** (#13). If a check contradicts what this dispatch assumes, report and
   halt that task — do not build around it.
6. **Bare words carry the musical meaning.** Bash: append `; echo "exit:$?"`; never let one call
   produce large output.

## 1. The rulings this dispatch applies (user, 2026-08-03, second set)

Presented as user-visible prose and read before the ruling was given (D-249 satisfied). Six
rulings. **Two of them are CONDITIONAL and are NOT applied in this dispatch — they are measured
here and applied later.** Do not collapse that distinction.

| # | Subject | Ruling | Applied here? |
|---|---|---|---|
| S1 | D-416, the two owed structural refactors | **Superseded-with-transfer** (option C) | Yes — **after** the Task 3 code check |
| S2 | D-415…D-423 | **Ratified as drafted** (option A) | Yes |
| S3 | OI-281 + the Cowork-ratification sibling | **The delegation-specificity criterion** (option iii), ruled once over both | **NO — measure only** |
| S4 | OI-284, the engage criteria | **Scoped narrower — different subject** (option iii); D-417 stays LIVE-but-scoped | Yes |
| S5 | OI-285, the uncommitted ratification surfaces | **Commit them** (option a) + a directory convention | Yes, **in place** — see §6 |
| S6 | The register's status-line convention | **A distinct "entry ratified" field** (option C) | Yes |

## 2. Task 1 — Repair the phase-1k provenance mis-citation

Both phase-1k commit messages cite `cc_instruction_phase1k_apply_rulings.md`. That file does not
exist on disk and is not in the tree at any commit. The dispatch actually executed is
`cc_instruction_phase1k_ratification_application_and_reads.md`, present on disk and (until Task 5)
untracked.

Commit messages are immutable, so the repair is a **dated correction note** where a reader will
meet it: append it to `open_items/OI-285.md` (the row that already owns the uncommitted-surface
problem), naming both SHAs, the cited name, the true name, and the fact that the executed content
matches the true file. Do **not** rewrite history.

## 3. Task 2 — D-416: check the code FIRST, then write the ruling (S1)

**This task has a mandatory order. The check precedes the ruling. If the check's result does not
match what §3.1 expects, STOP and report — the ruling was given on a stated premise and a
different premise voids it.**

### 3.1 The check

Establish, at the code and the record, **what remains owed of D-416 half (1)** — "the physical
split of `chordanalyzer.cpp` along the layer seams + iteration-API renames".

Known at dispatch time, verified by Cowork: `src/composing/analysis/chord/` contains
`postscoringgates.cpp`, `chordpostpasses.cpp`, `chordsymbolformatter.cpp`, `chorddiagnose.cpp` and
`chordvoicing.cpp` as separate translation units beside `chordanalyzer.cpp`; `docs/scoring_model.md:15-26`
describes this as "refactor #1 (byte-identical layer split)", pure code movement.

Answer, each with its citation: **(a)** is the physical split delivered, partly delivered, or not —
and is "refactor #1" the same act as **D-311**'s R9 split or a different one? **(b)** are the
iteration-API renames done, and if not, what is still named in iteration-era terms? **(c)** does
anything in half (1) have a subject OUTSIDE the dormant legacy path — i.e. is any of it owed
against code that is not scheduled for deletion at the retirement map (**D-418**)?

Question (c) decides the ruling's shape. If any of half (1) touches live code, say so plainly —
that is a STOP condition, because the ruling assumes both halves' subjects are legacy.

### 3.2 The ruling, written only if §3.1 confirms the premise

Record **D-416 as SUPERSEDED-WITH-TRANSFER**, per half, using the transfer marker variant (the one
phase 1i added because the fixed LEGACY wording's "no effect on the live solution" is false where a
principle carried across):

- **Half (1)** — superseded by the retirement map (**D-418**): the subject is deleted rather than
  refactored. Name what §3.1 found still outstanding, so the disposition retires a known quantity.
- **Half (2)** — superseded by **the joint estimator's standing rule (a)** (`ARCHITECTURE.md:264-269`,
  user-ratified 2026-07-17): factor forms from theory, values fit once, never tuned per case. The
  objective — no post-hoc correction layer — is met by construction on the production surface.

**The transfer half.** The PRINCIPLE binds the phase-3 family design: **corrections belong in
fitted factor values, never in a post-hoc correction layer laid over the decode.**

Where it goes, and where it must NOT go: rule (a) already states this in the estimator's
specification, so **do NOT add a seventh standing rule** — that would be a second copy of one
concern (#6). Instead: **(i)** D-416's register entry carries the transfer annotation naming rule
(a) as its live successor; **(ii)** a one-line pointer is added beside rule (a) recording that
D-416's mandate transferred into it and binds the family design; **(iii)** the family rows
(**OI-215, OI-226, OI-227, OI-228, OI-243, OI-244, OI-246, OI-277**) each gain a cross-reference to
D-416 as a phase-3 design constraint — the discoverability remedy is the pointer from where a
reader works, never more copies (the OI-272 ruling).

**The surfacing duty survives.** D-416's "surface at every planning checkpoint" stays in force
until the retirement actually happens; the disposition removes it as a phase-3 blocker, not as a
standing reminder. Say so in the entry.

## 4. Task 3 — Ratify D-415…D-423 (S2)

Nine entries, ratified as drafted, statuses exactly as the record states them (D-422 DEFERRED;
D-423 LIVE ⚠LEGACY; the rest LIVE). D-416 is in this batch **and** is the subject of Task 2 — it is
ratified as a correct record of the mandate, and separately dispositioned. Those are two acts, not
one; do not let either absorb the other.

Ratification is recorded per the S6 convention (Task 6), not in the Status line.

## 5. Task 4 — OI-284: the scoping ruling (S4)

Record the user's ruling: **the engage criteria (D-417) governed engaging the L4/L5 dormant spine,
not the joint estimator's adoption.** The switch that happened took a different architecture through
its own ratified decision surface (the OI-178 batch adoption 2026-07-26, **D-005**; the notation
switch 2026-07-27, **D-010**), so the criteria never applied to it, and what they do gate is moot
because that spine is what **D-418** deletes. Gate G1's "L6 built dormant" requirement therefore
needs no satisfying.

- **D-417 stays LIVE**, scoped — not retired. Its entry carries the scoping ruling with its
  reasoning and the note that this is a **reconstruction of scope, labelled as one**: the record
  does not state the narrowing, and the ruling says so rather than implying the record does.
- `docs/implementation_roadmap.md` gains the OI-232/OI-265-shaped **scoping sentence** on all three
  statements OI-284 names — the current-state table (`:42-52`, `:39-40`), the engage block
  (`:122-137`), and the batch case-identity gate (`:12-18`, superseded in whole at R10-b by the
  robust unit, **D-115**, `CLAUDE.md` block (C) historical only).
- The row flips with provenance; the detail file gains a dated note and never a status.

## 6. Task 5 — OI-285: commit the ratification surfaces (S5), with one refinement

**The refinement, and its reason — read before executing.** The ruling was "commit them, and give
the class a directory". Moving the files would break the paths nine committed register entries
already cite as their ratification provenance, and re-aiming ratified provenance is a larger act
than a filing decision. So:

- **Commit all seven IN PLACE, at their current paths, unchanged**
  (`cowork_decisions_pending_ratification_2.md` … `_8.md`). Their content is the text the user read;
  it is not edited, reformatted or re-bannered.
- **Also commit `cc_instruction_phase1k_ratification_application_and_reads.md`** — the eighth
  instance, the one OI-285's enumeration missed, and the file both phase-1k commits cite as their
  authority. Add it to the row.
- **The directory convention is ROWED, not executed** — a new open item: the ratification surfaces
  and the dispatches want a home, and the move is its own act because it re-aims cited paths.
  Record that the move must re-aim every citation per citation from the `--verify` drift report,
  never by an assumed path rewrite.
- OI-285's row flips to resolved **for the commit half only**, with the directory half carried on
  the new row. Do not flip it whole.

## 7. Task 6 — The register's "entry ratified" field (S6)

Add a field distinct from the decision's own date and ratifier, so the status surface shows an
entry's ratification without falsifying the original event's facts.

- Schema: extend `tools/audit/decisions/backbone_decisions.json`'s entry shape with an
  entry-ratification field (date + ratifier). Plain naming, no invented label.
- Generator: `gen_decisions_register.py` renders it on the full entry **and** surfaces it on the
  INDEX, so a session reading only the mandatory INDEX can see it. The Status line keeps the
  original decision's facts unchanged — "date not stated" / "ratifier not stated" stay exactly as
  they are (#12).
- Backfill from provenance, **mechanically and only where the provenance states it**: the thirty-odd
  entries carrying a ★ RATIFIED note. Do not infer a ratification that the provenance does not
  state; report any entry whose provenance is ambiguous rather than guessing.
- The backbone JSON round-trips byte-identical at `json.dumps(indent=2, ensure_ascii=False)`, no
  trailing newline.

## 8. Task 7 — OI-281: MEASURE the delegation-specificity criterion (S3) — do NOT apply it

The user ruled the criterion; the user did **not** authorize re-classifying against it before the
cost is known. **This task produces a measurement and a report. It changes no entry's home class.**

The criterion as ruled: *a document is a contract home when a user-ratified surface delegates to it
BY NAME, FOR A STATED CONCERN, and the document is stable enough to be cited.* The banner's
self-description is not the test; the delegation's specificity is. Rule (g)'s guard is intact —
an assistant's stamp confers nothing, because the delegation does the conferring and only the user
writes a delegation into `ARCHITECTURE.md`.

Measure and report, with no changes written:

1. Applied to the ~112 entries phase 1i classified under the old test: **how many move, in which
   direction, and which ones?** List them.
2. Do the two precedents the criterion was built to explain come out right —
   `cowork_layer5_engagement_design.md` **admitted** (three by-name delegations in a user-ratified
   arc plan) and `cowork_structural_integrity_audit.md` **excluded**? If either comes out the other
   way, the criterion does not do what it was ruled to do: **STOP and report that**, it is a #13
   surprise.
3. The two sibling populations: `cowork_progression_schema_dictionary.md` (9 entries,
   D-406…D-414) and the Cowork-ratification set (21 — `docs/decoder_design.md` 4,
   `cowork_score_census.md` 17). Do they answer **consistently** under one criterion? That
   consistency was the reason for ruling them together.
4. Any entry where the criterion is genuinely ambiguous — report it as ambiguous. A criterion that
   needs judgment on many entries has not solved the problem it was ruled to solve, and that is a
   finding, not a failure.

## 9. Task 8 — Continue the full reads (OI-207)

63 documents owed of 143 (39 read, 41 on the user's accepted exclusion list). Read IN FULL, in the
OI-207 artifact's order — the three at 17 unresolved clusters next.

Per document: enter every decision-bearing statement with **the record's own status only**;
inference of a status is forbidden and "not stated" is expected. Row any OI-232/OI-274/OI-276/OI-279
class finding (a document stating as current something false at HEAD). Update the OI-207 note with
the new read count and the remaining list. **Do not revise the remaining-session estimate downward
without a measured basis.**

## 10. Task 9 — Guards, notes, close

```
cd C:\s\MS && python tools/audit/decisions/gen_decisions_register.py --check > /tmp/reg_1l.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/ver_1l.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/open_items_split_check.py > /tmp/split_1l.txt 2>&1; echo "exit:$?"
```

Read each output file separately; all three must pass at the committed tree. Anchor drift from the
Task 5 roadmap edits and any `ARCHITECTURE.md` pointer is **re-aimed per citation from the drift
report's own line numbers** — never by an assumed uniform shift.

`STATUS.md` gains one POINTER entry (the OI-222 remedy). Commits by git plumbing
(`write-tree`/`commit-tree`/`update-ref`); every guard run explicitly at the committed tree because
plumbing bypasses hooks. Report the SHAs.

**Still owed and NOT in this dispatch, so a later session does not think they were done:** OI-280
(the "D5" label collision), OI-282 (`cowork_style_clustering_plan.md` still calls the clusters half
future work), OI-283 (the register's hand-typed coverage line count, #17f), OI-274's body-tense
half.

## 11. Accepted outcomes

Tasks 1–7 and 9 are bounded and expected complete. **Task 8 may stop short** — report the count
measured, do not compress the earlier tasks to make room. **Task 7 producing a STOP is a success,
not a failure:** it exists to find out whether the ruled criterion holds before thirty entries move
on it.
