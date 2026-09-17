# CC instruction — OI-199 joint module: complete the CONTRACT-DIRECTION check and the BEHAVIOURAL characterization to the L4 standard, on BOTH corpora (READ-ONLY; dispositions are NOT redone)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and the detail files this
> dispatch serves: **OI-215** (the empty-decode cliff — this dispatch's subject is whether it is
> ALONE), **OI-199** (the review), **OI-110** (the ratified counter disposition: default-OFF,
> byte-identity proven, REVERTED at the end, hash recorded), **OI-209** (the large-score
> requirement), **OI-222** (the blinding failure — its structural remedy is now in force, see
> below), **OI-216…OI-223** (your own pass-1 rows). Also the METHOD precedent you are completing
> against: `cc_l4_audit_pass1_decoder_report.md` and its artifacts
> `tools/audit/l4/pass1_dispositions_decoder.csv`, `pass1_decoder_behavior.txt`,
> `pass1_oracle_firecount.json`.
>
> **What this is, and what it is NOT.** Your pass-1 dispositions are **NOT being redone**. Cowork
> verified them against the certified precedent and was wrong to fault them: the L4 decoder pass
> the user certified carries nine distinct (kind, verdict, reason) combinations over 311 rows —
> all 127 of its branches on one verdict — against your ten over 1,069. Generated dispositions
> with hand-curated exception sets ARE the ratified method, and Cowork's proposed
> "verdict-entropy guard" is **withdrawn**, having been calibrated against nothing. Your
> inventory, partition proposal, feasibility stop, field curation and rows all stand.
>
> **Two arms genuinely under-delivered against the L4 standard, and this dispatch completes
> them:**
> - **P4, the behavioural characterization.** At L4 it ran real routes over the corpus — 29,080
>   slices, commit 34.4 % / inherit 3.0 % / abstain 62.6 %, plus per-site fire counts from the
>   OI-110 instrument. Yours was a passing test suite plus a fire structure read off the code.
> - **P3's second side.** It reported one code-with-no-expectation finding (stale dormancy
>   headers). Cowork searched the ratified `cowork_joint_estimator_factorization.md` for the
>   decoder's candidate-admission rule — the root-present prune, the member-overlap prune, the
>   non-chord-tone budget — and **found no description of candidate admission anywhere in it**.
>   If that holds, the rule that empties the analysis on 13 of 23 large scores entered production
>   with no ratified basis, and P3's second side should have said so.
>
> **The question this dispatch exists to answer: IS OI-215 ALONE?** One admission-rule failure was
> found by accident, on one texture, by a measurement that was not looking for it. #3 says a
> surprise means the fact basis was incomplete; designing a fix around a single instance without
> knowing whether it has siblings is what that principle forbids. **No fix may be designed until
> the family is enumerated** — that is the whole purpose here.
>
> **Current state:** branch `master`; expected HEAD `b14a523112` — verify; mismatch = STOP.
> Riding Cowork edits: `cowork_handoff.md` and `STATUS.md` ride your first commit. This dispatch
> file stays untracked.
>
> **Hard stops:** origin only; **no fix, no design, no behaviour change, no constant tuned** —
> you are characterizing, not amending; no golden, `tools/corpus/` or `tools/robust_stop/`
> movement; the dispositions CSV/JSON are **annotated, never rewritten** (#10/#12). A surprise is
> a STOP (#13). VS Code bash rules on every command.
>
> **★ THE OI-222 REMEDY IS NOW IN FORCE (standing).** Findings that must not steer a later blind
> pass never go into a mandatory session-start read: `STATUS.md` carries a POINTER, the content
> lives in a post-freeze artifact. This dispatch is not blind — the joint module's findings are
> permanently in the register and blindness there is unrecoverable — but the rule binds from now
> on, and the instruments partition depends on it.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28, at the user's ruling (amended alternative 2).

**Touchable set:** `src/composing/analysis/joint/` **only** for the default-OFF fire-count
instrument under the OI-110 disposition (reverted at close, hash recorded); the test dirs
(drivers); `tools/audit/oi199/` (annotations and new artifacts); the register INDEX and detail
files; `STATUS.md`; the riding Cowork files.

---

## Task 0 — predictions, and the rows this dispatch owes

**Register your prediction bands in the artifact BEFORE the measuring run (#17b).** Your pass-1
report declared that you registered none last time and that Cowork's interpretation error was
exactly what that guard catches. State, with bands: how many admission-rule-class failures you
expect to find beyond OI-215 (zero, one, several), which branches you expect to be dead on the
fit corpus, and which you expect to be dead on the large-score set. **No prediction, no run.**

Rows (rule (c), index + detail, in the commit that records the discovery):

1. **P4 under-delivered against the L4 standard** at pass 1 — no corpus route, no fire counts —
   and it is the arm that would have exposed the member-overlap prune's rejection behaviour.
   Record it as a method finding on OI-199, with this dispatch as the remedy.
2. **A correction of record on Cowork's account** — the claim that the pass-1 dispositions were
   "generated, not made" and therefore void was **wrong**, measured against the certified L4
   precedent (nine combinations over 311 rows versus your ten over 1,069). The verdict-entropy
   guard is withdrawn. Recorded so no future reader treats the committed dispositions as
   discredited.

## Task 1 — P4 to the L4 standard, on BOTH corpora

Per-branch and per-filter fire counts for the joint decoder, under the **OI-110 disposition**:
default-OFF, zero work and zero behaviour change when off, byte-identity proven with it off, and
**REVERTED in its own commit at the end** with the hash recorded for a one-cherry-pick re-add.

**Run it over two populations, and report them separately:**

- **(A) the fit corpus** — the covered chorales, the population every prior characterization used.
- **(B) the committed large-score set** — `"tools/extra scores/large/"`, all 23. **This is the
  point of the task.** It is the first time this module's branch behaviour will be characterized
  on the repertoire the large-score requirement names, and the thirteen scores that decode to
  nothing are the cheapest and most informative cases, because admission rejects before the
  costly dynamic program runs.

Report, per population and per score:

1. **Candidate admission** — invocations of the candidate enumeration, candidates offered, and
   **rejections split by filter**: root-present, member-overlap, non-chord-tone budget. Plus the
   distribution of distinct onset pitch classes per examined window, since that is the quantity
   the member-overlap rule actually tests.
2. **Coverage failure** — events with no admissible covering segment, and whether the dynamic
   program reached the final boundary.
3. **The decode's own route rates** — commit / inherit / abstain or their equivalents on this
   decoder, the L4 pattern.
4. **Dead branches** — every branch that fires zero times, per population. **A branch dead on
   (A) but live on (B), or vice versa, is a headline finding**: it means the fit corpus never
   exercised it, which is the structural shape of OI-215 and the thing we are hunting.

**Then answer the question plainly: is OI-215 alone?** Enumerate every admission-rule-class or
coverage-class failure the counts reveal, with its mechanism and its measured extent. If there
are none beyond OI-215, say so — that is a valid and useful answer, and it releases the fix
design.

## Task 2 — P3's second side, done properly

Two-sided, as the pattern requires, but the side that under-delivered is the second:

**Every element of the joint module's decode that is not accounted for by a ratified
expectation.** Work from the ratified documents — `cowork_joint_estimator_factorization.md` (the
structure, the ten-factor score form, the premise ledger P1–P8, the §5 decode plan),
`cowork_prefit_gates.md`, `cowork_notation_output_contract.md`, `ARCHITECTURE.md` — and locate
each mechanism the code implements. Report, with file:line, every mechanism that has **no**
stated basis in any of them.

**Candidate admission is the specific case to settle, not to assume.** The root-present prune,
the member-overlap prune (`present < min(2, |members|)`), and the non-chord-tone budget
(`max(1, j - i)`) exist in both the C++ decoder and the pinned Python reference, where they carry
only inline comments. Cowork found no description of candidate admission in the ratified
factorization. **Search exhaustively and report the finding either way** — a located basis
closes the question; an absent one means a production inference rule was never a premise, which
is OI-207's subject matter and bears directly on the OI-215 fix design.

Note also, for the record and without acting on it: the admission filters test **onset** pitch
classes, while the segment's **sounding** pitch classes are computed on the adjacent line
(`piece.overlap_pcs(i, j)` in the reference; the C++ equivalent). Confirm or refute that at the
code.

## Task 3 — annotate the frozen dispositions

Add the two evidence columns the L4 rows carried and yours do not — the fire route linking each
row to Task 1's characterization, and the parameter-manifest registration status — as an
**annotation artifact beside** `pass1_dispositions_joint.csv`, not by rewriting it. The frozen
rows are the record of what pass 1 verdicted (#12); the annotation is what pass 2's second reader
will need in order to sample against evidence rather than against a bare verdict.

## Task 4 — revert, notes, close

Revert the counters in their own final commit; prove `src/` byte-identical to `b14a523112`;
both suites and the pipeline snapshots green; record the reverted hash in the row. Dated notes on
OI-215 (the family answer) and OI-199; `STATUS.md` entry **carrying a pointer, not the findings'
content** (the OI-222 remedy). Commits per change-class. Push origin.

## Report

Hashes per commit including the revert. Your registered predictions and the measured outcome
against each band. The Task-1 fire-count tables for populations (A) and (B), the filter-split
rejection counts, the onset-diversity distribution, the dead-branch sets per population and their
difference, and **the plain answer on whether OI-215 is alone**, with every sibling enumerated
and its extent measured. The Task-2 list of mechanisms with no ratified basis, candidate
admission settled either way, and the onset-versus-sounding confirmation. The Task-3 annotation
artifact. The byte-identity proof for the revert. Anomalies each diagnosed — a surprise is a STOP.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

**After this dispatch:** Cowork drafts the OI-215 decision surface under the Premise Gate — one
design at the correct layer covering the whole family this dispatch enumerates, never a patch per
symptom (#6/#7) — for the user's ratification. Then the instruments partition, sealed and blind
under the OI-222 remedy (#19: every figure steering this arc came from instruments nobody has
reviewed). Pass 2, the analysis-extent decision, and the record-seams partition all wait behind
those.
