# CC dispatch — phase 1m: the D-416 dispositions, the marker correction, and two measurements

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date (fourth set).** Read IN FULL before touching anything it owns.
>
> **★ CITE THIS FILE BY ITS EXACT NAME** — `cc_instruction_phase1m_dispositions_and_measurements.md`
> — in every commit message. The phase-1k commits cited a filename that exists nowhere in the tree.
> Copy the name; do not retype it from memory.
>
> **★ THIS IS A RULING-APPLICATION WAVE. IT READS NO DOCUMENTS FOR OI-207 — BY DESIGN.** The user
> ruled (D2) that reads become their own dedicated waves and rulings are batched between them. The
> read count stays at 40 of 143 this wave. That is intentional; do not treat it as a shortfall and
> do not open a document to "make progress".

## 0. Standing constraints

1. **Every amendment lands in the PROPER LAYER** (#7). A rule about the estimator goes in the
   estimator's specification; a rule about a document's status goes in that document.
2. **NO inference-problem fixing.** Phase 1 under D-231. No fix, no design, no behavior change, no
   `src/` edit, no golden refresh, no `tools/corpus/` or `tools/robust_stop/` movement.
   **Renaming a symbol is a `src/` change and is NOT licensed here** — Task 1 disposes of the
   rename obligation on paper only.
3. **Never use the shell to read working-tree files.** File tools for content, existence, counts and
   searches. Shell only for read-only git object queries by explicit hash, and for the guard and
   generator scripts named below.
4. **Never work from memory.** Every written claim cites its primary source file:line, re-read this
   session.
5. **A surprise is a STOP** (#13).
6. Bare words carry the musical meaning. Bash: append `; echo "exit:$?"`; no large single outputs.

## 1. The rulings this dispatch carries

| # | Subject | Ruling | Applied here? |
|---|---|---|---|
| T1 | D-416 / OI-286 | **Split into its three real components**, each disposed on its own evidence (option A2) | Yes |
| T2 | The five stale "parked" statements | **Correct now**, including the three in user-ratified surfaces | Yes |
| T3 | Live-reachability of the legacy scorer | **Phase-2 row, not a blocker** (option A4's measurement, deferred) | Row only |
| T4 | The LEGACY marker's wording | **Weaken to what is established** (option C3); full re-verification is a phase-2 row (C2) | Yes + row |
| T5 | The contract-home criterion | **The KIND test replaces "stable enough to be cited"** (option B2) | **NO — measure only** |
| T6 | The remaining reads | **Partition by measured yield, residual bounded and stated** (option D3) | **NO — measure only** |

**T5 and T6 are measurements. They change no entry's home class and reorder no reading list.** Do
not collapse that distinction; the user ruled the criterion and the method, not their application
before the cost is known.

## 2. Task 1 — D-416: three components, three dispositions

**Label this as what it is.** D-416 records one 2026-06-14 user mandate. Splitting it into three is
**Cowork's reading of that mandate, user-ratified 2026-08-03** — it is a reconstruction, and the
register must say so rather than implying the record always held three items.

Create the components as register entries, each carrying D-416 as its parent and each with its own
status and defense. D-416 itself **remains ratified as a correct record of the mandate** and is not
retired; it gains a disposition note pointing at the three.

**(1a) The physical file split — DELIVERED.** Commit `41f7c65f63` (2026-06-17), 2,178 lines moved
out of `chordanalyzer.cpp` into five sibling translation units, touching nothing else but
`CMakeLists.txt` and `docs/scoring_model.md`. Evidence and the five stale counter-statements are
enumerated at `open_items/OI-286.md`; cite it, do not re-derive it. **This component is closed.**

**(1b) The iteration-API renames — OWED, subject PARTLY LIVE.** `applyIter8691Pedal` is still the
declared name (`chordanalyzer.h:729`, defined `chordpostpasses.cpp:119`), with call sites including
`sectionanalyzer.cpp:450`, `regionanalyzer.cpp:1011`, `harmonicsegmenter.cpp` (six sites),
`notationcomposingbridge.cpp:663` and `regiontoneprimitives.cpp:511`/`:569`. The last of these is
the live Layer-1.5→Layer-4 fact cycle `OPEN_ITEMS.md` OI-165 records as *"not currently scheduled
to die"*. **Therefore this is ordinary technical debt on partly-live code, NOT legacy work**, and it
must not carry the LEGACY marker. Record it OWED with its subject stated. Enumerate the full call
site list in the entry's provenance so a later session does not re-discover it.

**(2) The gate dissolution — OWED, subject NOT wholly dormant.** The dissolution of the post-hoc
gate-correction layer (Gates A–L) into fitted weights is undone. Its subject is dormant on the main
production path — the joint estimator's standing rule (a), `ARCHITECTURE.md:264-269`, has no
post-hoc correction layer by construction — **but it is reachable on the live notation arm**:
`notationcomposingbridge.cpp:750-753` marks `analyzeHarmonicContextLocallyAtTick` as the *"P4
fallback… Fires 0/2231 on the perf corpus"*, and that function runs `findTemporalContext` (`:651`),
`analyzeChord` (`:656`) and `applyIter8691Pedal` (`:663`).

**Write the qualification explicitly:** a zero fire count on one corpus is not an establishment
(#19), and OI-215's finding is that a branch measured dead on the fit population can be live on the
repertoire the requirement names. So component (2) is **OWED with its subject's liveness UNRESOLVED**
— not superseded, not discharged by rule (a). Record that Cowork's earlier reading (that rule (a)
discharges it) was **withdrawn on this evidence**; the withdrawal belongs in the record (#12).

**The transfer half still stands and still needs its home.** The principle — *corrections belong in
fitted factor values, never in a post-hoc correction layer laid over the decode* — binds the phase-3
family design. Per §7 and the OI-272 ruling: **do NOT add a seventh standing rule**, since rule (a)
already states it and a second copy is a #6 violation. Instead: a one-line pointer beside rule (a)
recording that D-416's mandate transferred into it; and a cross-reference on the family rows
(**OI-215, OI-226, OI-227, OI-228, OI-243, OI-244, OI-246, OI-277**) naming component (2) as a
phase-3 design constraint.

**The surfacing duty survives** for (1b) and (2) until they are done. Say so.

## 3. Task 2 — Correct the five stale "parked" statements

`open_items/OI-286.md:35-41` enumerates them. Correct each in place, with a dated note naming the
user's 2026-08-03 ruling and commit `41f7c65f63` as the delivery:

1. `docs/implementation_roadmap.md` — the R9 line (the retirement map, **user-ratified 2026-07-02,
   D-418**);
2. `STATUS_ARCHIVE.md:166`;
3. `cowork_stage5_fitter_design.md:103`;
4. `cowork_structural_integrity_audit.md:313-314`;
5. register entry **D-311** — status DEFERRED is stale for the split half; restate it over what
   remains (the renames), preserving the former verbatim and the former status in provenance (#12).

**Three of these sit in user-ratified surfaces** (the retirement map, D-311, and the arc plan's
scope-out). The user ruled the correction; cite the ruling in each note so a reader sees the
authority. **Do not delete any original wording** — annotate.

## 4. Task 3 — The live-reachability row (phase 2)

Open one row: **how live are the P4 fallback and the OI-165 Layer-1.5 primitive on real
repertoire?** It is a fire-rate question of the kind OI-199's P4 arm exists to answer, it bears on
D-416 component (2)'s disposition, and the family design needs it regardless. State: the only figure
we have is 0/2231 on the perf corpus; OI-215's lesson is that the fit population hides what the
requirement's repertoire shows; and the 23 committed large scores are the population that would
answer it. **Not scheduled here** — it enters phase 2's program.

## 5. Task 4 — Weaken the LEGACY marker, and row the re-verification

**The change.** The marker's fixed wording asserts the decision *"has no effect on the live
solution."* That clause has now failed twice — D-329 (phase 1i, which produced the transfer variant)
and D-311 (this wave, whose subject produced `chordsymbolformatter.cpp`, run by the record arm at
`notationimplodebridge.cpp:1170`). **Remove the clause.** The marker states that the subject is the
legacy pipeline awaiting deletion at the retirement map, and stops there.

Do it in the **generator** (`gen_decisions_register.py`), not by editing rendered files — the marker
is generated text, so one change covers all 75 and cannot drift (#17f). The transfer variant keeps
its transfer language; only the unsupported clause goes.

**The row.** Open a phase-2 row for the full re-verification: all **75** LEGACY-marked entries
checked against a live-reachability test, on the ground that a swept population with two
demonstrated errors is not established (#19). Note that the P4-fallback finding (Task 3) may bear on
a whole class of them, not just on D-311.

## 6. Task 5 — MEASURE the KIND test (do not apply it)

**The criterion as ruled.** A document may be a contract home when a user-ratified surface delegates
to it **by name, for a stated concern**, and the document is of a **kind that states rules**
— specification, contract, design, component spec, binding plan — rather than a kind that **records
findings** — audit, report, census, inventory, measurement artifact, probe or dossier of findings.
The operative question is the document's **purpose**: does it state what shall be, or record what was
found? The banner's self-description is not the test. Rule (g)'s guard is intact: an assistant's
stamp confers nothing, because the delegation confers, and only the user writes a delegation into
`ARCHITECTURE.md`.

Measure and report, **writing no home-class change**:

1. Classify every candidate document by kind. **Report any document whose kind is genuinely
   ambiguous rather than forcing a binary** — a roadmap or a plan may state what shall be and also
   track state, and that population is a finding.
2. Re-run the 131-entry population from phase 1l's Task 7 under the kind test. **How many move, in
   which direction, which ones?**
3. Check the two precedents: `cowork_layer5_engagement_design.md` (a design) must come out
   **admitted**, `cowork_structural_integrity_audit.md` (an audit) **excluded**. If either comes out
   otherwise, **STOP and report** — the test was ruled precisely because it explains both.
4. **The expected consequence, stated in advance so it is not read as a failure:** `cowork_score_census.md`
   is a census — a findings kind — so its **17 entries should move OUT**, against phase 1l's
   measurement which moved them in. Cowork predicts this before the run (#17b). If they do not move
   out, the kind classification disagrees with Cowork's reading of what that document is, and that
   is the finding.
5. Does the ambiguous population **shrink** relative to phase 1l's 33? The criterion was ruled to
   make the test mechanical; if ambiguity does not fall materially, say so plainly — that is the
   honest verdict on a criterion Cowork proposed, and it must not be softened.
6. Does the test still make OI-268's Cowork-ratification question moot? It should: kind and
   delegation are both independent of who ratified the document.

## 7. Task 6 — MEASURE the reading yield and propose the partition (do not act on it)

**Report a proposal, reorder nothing.**

1. Over the **40 documents already read**, measure decision yield: entries produced per document,
   with its distribution and tail, and the same for rows opened.
2. Rank the remaining **62** by a proxy for expected yield, using observable features only (kind,
   length, age, whether the document is a LIVE-SPEC surface or an archive, whether
   `ARCHITECTURE.md` points at it, and any other feature the measured 40 supports).
3. **State the proxy→target link as a premise, not a fact** (#17d): a structural proxy does not
   stand in for a behavioral quantity unvalidated. Say how the ranking would be **validated** —
   for example by reading a random sample from the predicted-low band and comparing actual yield
   against the prediction — and register the predicted band **before** any such check.
4. Propose the partition: which documents are read in full, which are carried, and **what bound is
   claimed over the carried tail** — with the bound's own basis stated. A bound that rests only on
   the unvalidated proxy is not a bound; say so if that is where it lands.
5. Report the implied wave count for the read-in-full set under the dedicated-wave regime.

## 8. Task 7 — Guards, notes, close

```
cd C:\s\MS && python tools/audit/decisions/gen_decisions_register.py --check > /tmp/reg_1m.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/ver_1m.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/open_items_split_check.py > /tmp/split_1m.txt 2>&1; echo "exit:$?"
```

Read each output separately; all three pass at the committed tree. Anchor drift from the Task 2
edits and the Task 1 pointer is **re-aimed per citation from the drift report's own line numbers** —
never by an assumed uniform shift.

`STATUS.md` gains one POINTER entry (the OI-222 remedy), stating explicitly that **this wave read no
OI-207 documents by design** and that reads resume as dedicated waves.

Commits by git plumbing; guards run explicitly at the committed tree because plumbing bypasses
hooks. Report the SHAs.

**Still owed and NOT in this dispatch:** OI-280, OI-282, OI-283, OI-274's body-tense half, OI-287
(the ratification-surface directory), and the 62 remaining reads.

## 9. Accepted outcomes

Tasks 1–4 and 7 are bounded and expected complete. **Tasks 5 and 6 producing an unwelcome answer is
a success** — both exist to test a criterion and a method Cowork proposed, before either is applied
to a population. A report that says "the kind test does not reduce ambiguity" or "the yield proxy
does not support a bound" is the outcome those tasks were written to be able to produce.
