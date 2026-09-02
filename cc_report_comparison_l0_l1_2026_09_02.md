# CC report — the L0/L1 comparison batch: the derivation landed, the outgoing population derived, and the comparison NOT opened

> **STATUS: SESSION REPORT. It decides nothing, establishes nothing, and recommends nothing.**
> Prepared by Claude Code, 2026-09-02, under `cc_instruction_comparison_l0_l1_2026_09_02.md`,
> executing Ruling 32 (§3am of `cowork_rulings_2026_08_31_decision_surface_sitting.md`) and, through
> it, Rulings 1–4 and §5 of `cowork_rulings_2026_08_24_comparison_design_sitting.md` and the
> disposition discipline of `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`
> §0 and §3.4.
>
> **What the user is asked to rule here: ONE thing** — whether the term list is narrowed or the
> comparison is split across dispatches. That question is the dispatch's own, handed back by its own
> ruled size stop. **Nothing else in this report asks for a ruling and nothing in it recommends
> anything.**
>
> **Where this report would name hashes it cannot contain — the close commit and the end-state
> commit — it points at the git log**, as the dispatch directs.

---

## 1. The headline

**Task 0 and Task 1 ran and are complete. Task 2 did not open. Task 3 closed the batch.**

The dispatch ruled, in advance and in its own words, that if the number of term-search hit files
outside the named members exceeds forty, the batch **stops after committing the population artifact**
and reports the count and the distribution by term, the user ruling whether the term list narrows or
the comparison splits across dispatches. **That threshold is exceeded.** So:

- **no statement of any outgoing text received a disposition**;
- **no derived statement was graded on the current-text axis**;
- **no difference was stated, no proposal written, no transfer list and no audit question produced**;
- **`ratification_surfaces/cowork_comparison_l0_l1_reading.md` was not created and does not exist.**

**No document was partly worked.** The remainder is untouched rather than half-done, which is the
state the stop exists to produce and the boundary the next dispatch resumes from.

## 2. What was landed, and the proof the derivation is untouched

Task 0 committed **six paths and no others** — the blind derivation, the twice-amended brief, the
sitting record carrying Rulings 26–32, the running order, the eighty-ninth handoff entry, and this
batch's own dispatch — and pushed, **carrying with it the three commits that had been sitting
unpushed**. `origin/master` was then verified equal to the new tip by reading
`.git/refs/remotes/origin/master` at the file rather than by trusting the push's output, and the same
verification was repeated after Task 1's push.

**The derivation landed untouched, and that is proven rather than asserted.** Its committed blob is
`9b102c575643d672e4747b4cfc23e377cd344c27` at **112,954 bytes** — the byte count the dispatch's own
FACT declared. The blob was extracted from the object by explicit hash to a scratch path outside the
repository and compared byte-for-byte with the file on disk using `cmp`, which returned equal.

**The dispatch was pinned** to blob `5b0db6f73bd16ba200f662ec5dcdda2e11da1328` at Task 0 under
standing clause P-2 and re-hashed immediately before staging, returning the same identifier. The
working-tree-first read is declared as that clause's own fallback route, the user's opening line
having named the dispatch file alone.

**The membership artifact was measured before it was accepted.** `evidence_pin_membership.json` was
snapshotted, regenerated and diffed against the snapshot: **byte-identical, zero lines of
difference**, and `ruling_records_read` unmoved against the committed blob at the tip. All three of
assumption A3's declared routes hold by that identity. **It therefore did not move and was not
committed** — the ordered path list says *only if it moved* — which is why the commit carries six
paths and not seven.

## 3. The outgoing population, and what its artifact does and does not claim

`tools/audit/gen_l0_l1_outgoing_population.py` writes
`tools/audit/l0_l1_outgoing_population.json`. It does four things and nothing else.

**It lists the eleven members Ruling 32 names**, each **proven present at its path** — a missing one
is a STOP the tool raises, and it did not arise. The three `ARCHITECTURE.md` sections are **located
by heading text and never by line number** (**D-307**): each record carries the heading it opened at,
the opening heading exactly as found in the file, the pattern that closes it, and the closing heading
as found, so a heading moving under the tool cannot leave a stale coordinate behind.

**It runs the term search** over every file of the three inventory classes the ruling names, reading
class membership from `tools/audit/artifact_inventory.json` → each class's `every_member` and **never
from a directory listing**, so the searched population is the ruled one rather than whatever the file
system happens to hold. Two tiers: **admitting** terms, one hit of which admits a file, and
**recorded** terms — single words too common to admit a file on their own — counted per hit so that
the effect of the other rule is readable rather than argued.

**The two tiers and the rule between them are AUTHORED, and the artifact says so on its own face.**
Ruling 32 names the charter's vocabulary; it does not partition that vocabulary into a tier that
admits and a tier that does not. The dispatch fixes the partition, and the artifact records that this
is an authored choice rather than a derived one.

**It states its reach (D-673), and the statement is the honest one.** The term list is authored, so a
passage about L0's or L1's subject that uses none of these words is not found. **Nothing other than
this search enumerates "passages of the current text about L0's or L1's subject"**, so there is no
independently-known population to reconcile against, no seed set can establish it, and the artifact
therefore publishes its output as a **LOWER BOUND with its reach declared UNMEASURED, never as a
census** — the recognizer clause of the dispatch protocol, applied because its own test returns *no*.
What bounds the exposure is stated with it: the eleven named members are in the population by name
regardless of the search, and they are the territory the ruling identified by reading rather than by
pattern. **The search widens that territory; it does not define it.**

**It counts, at the artifact and nowhere else** — files searched per class, files with hits, hits per
file, hits per term — and **no figure of it is restated in this report** (#17f, **D-431**). The whole
ordered population is written to `the_population_in_comparison_order`: the eleven named members
first, in the ruling's order, then the hit files by descending admitting-hit count with ties broken by
path so the order is deterministic. **That order is the batch order the next dispatch resumes on.**

**The size stop is recorded on the artifact as what it is:** a threshold for *this batch*, ruled in
its dispatch so the decision is not the executing session's, and **not a figure about the corpus**. It
states nothing about how large the outgoing text is.

## 4. What was refuted, and each cause established rather than guessed

Three of the dispatch's own premises did not survive measurement. **All three are reported and graded
rather than absorbed**, under standing clause P-3, and none was worked around.

**(a) The declared start state.** The dispatch's FACT reads the guard summary at
`4c9b7af5…:tools/audit/guard_state.json` and names eight failing tools. The CHECK-mode run before this
batch's first edit returned **eleven**. The cause is established at the objects: **that artifact was
last written at commit `21e78f575a`, three commits before the tip this batch met**, so the declared
state was read from an object predating the reading-pass landing, this sitting's products and the
handoff prepend. Seven of the eight named reds were present; **`gen_derivation_boot_pack.py --check`
was not — it passes.** The four outside the declared set were each re-run individually and their
messages read: one is the artifact-inventory STOP the previous batch already reported and was ordered
to leave unrepaired, whose signature table's amendment is reserved to the user; the other three are
STALE derivations whose populations moved under those same three commits. **One of them,
`gen_session_start_read_size.py`, is cleared by this batch's own ordered regeneration; the other two
were not this batch's subject and were not touched.**

**(b) Assumption A1.** Its two named tracked modifications are confirmed at the diff — the brief's
four deleted passages were read at a scratch copy and are exactly the allow-list and stop-on-meeting
rewordings and the delivery-route change; the sitting record is additions only. But **the tree carries
a third tracked modification A1 does not name**: `cowork_handoff.md`, amended by the writing side with
the *SUPERSEDED IN PART* block and the §3ag-to-§3aj correction. A1 makes any other tracked
modification a STOP-and-report. **It was reported and graded rather than auto-stopped**, because A1 is
written as a blanket over the pre-existing tree rather than as the list of this batch's own ordered
acts, which is precisely what P-3 forbids — and because **the modification is the very amended text
the dispatch ordered this session to read as the topmost handoff entry**, so stopping on it would have
stopped on the dispatch's own input. The file is on no commit list of this batch and was not touched.

**(c) Assumption A4 — and this one is a live halt, not a bookkeeping difference.** A4 predicts the new
script unenrolled with *population unchanged at run 75; failing set unchanged*. Measured after Task 1,
`gen_guard_state.py --check` returns
`STOP: derived candidate(s) with no authored invocation: ['tools/audit/gen_l0_l1_outgoing_population.py']`.
The runner derives its candidate population from every `tools/audit/*.py` carrying a `--check`,
`--verify` or `--establish` mode, and an unclassified candidate is a STOP **by construction** — the
runner's own authored comments call enrolling a new tool in the dispatch that creates it *the standing
new-tool rule*, and name two other tools already carrying that condition. **So an unenrolled tool with
a `--check` mode does not leave the guard population unmoved; it halts the runner.** The dispatch
forbids enrolment twice — in A4 and again under *What this batch does NOT do*, where enrolment is
named a separate ruled act on the user-owed list. **It was therefore not enrolled, the halt stands,
and it is attributed here to this batch's own ordered act.**

**The consequence for E3, stated plainly:** its acceptance limb demands a failing set of exactly eight
at a tree that carried eleven before the first edit, and a population at run 75 that its own A4 makes
unreachable. **E3 cannot be met.** This is the founding shape P-3 names — an acceptance criterion
written independently of the declared start state and the footprint rather than derived from them —
and it is reported, not engineered around.

## 5. E0–E3 and A1–A5, graded

**Graded in full in the close**, appended to `cowork_away_returns.md` as the section *THE L0/L1
COMPARISON TABULATED, NOTHING DECIDED*. In summary: **E0 MET; E1 MET; E2 NOT REACHED** (its every limb
is conditioned on documents being tabulated, and none was — no document was partly worked); **E3
CANNOT BE MET**, for the reason in §4(c). **A2 held on its own prediction** (the membership check
passed) and **A3 held on all three routes, measured**; **A1 and A4 are refuted** as above; **A5 holds
at the objects for every member** — the derivation, the brief, the pack artifact, `ARCHITECTURE.md`,
`CLAUDE.md` and the sampled outgoing texts all verified SAME between the Task-0 commit and the close —
**while its blanket over *every governing document* collides with Task 3's own ordered `STATUS.md`
entries and forward-bound move.** That collision is reported rather than resolved by a session.

## 6. Declared departures

1. **The dispatch was read from the working tree before it was pinned** — P-2's fallback route, the
   user's opening line having named only the dispatch file. Pinned at Task 0; blob proven unmoved
   before staging.
2. **The ordered first read preceded the session-start read** — the derivation's §5, then §6, then
   §7, then the whole file, before `CLAUDE.md`. Ordered by Ruling 2 of the comparison-design sitting
   as Ruling 32 applies it. **The read SET is unchanged; only its ORDER.**
3. **`tools/audit/gen_status_batch_bound.py` was edited** — its three aiming inputs and its act date,
   the per-batch re-aiming its own carve-out provides for and the dispatch licenses in terms. **The
   previous aiming is recorded in the file beside the new one rather than overwritten** (#12), and the
   tool's own already-in-the-archive STOP is what established that the previous move had run.
4. **A scratch directory outside the repository** carried every diff, every extracted object and every
   captured tool output, each read back with the file tools.

## 7. What this batch did NOT do

**No decision on any disposition, any difference, the derivation, the method or the L0/L1 split. No
verdict on the deriving session's independence — its record was not relayed at all, that being a Task
2 deliverable. No session booted. No measurement of the analysis built, designed, scoped or run. No
specification statement derived.** No edit to the derivation, the brief, the pack, its generator, its
artifact, any outgoing text, any register source, or any governing document other than `STATUS.md`
under Task 3's own order. **No `src/` change, no golden, no test changed, moved or run, no build,
nothing under `tools/corpus/` or `tools/robust_stop/`. No open-items row created, flipped or
discarded. No decisions-register entry and no `D-NNN` allocated** — that register cannot accept one,
and `cowork_register_rule_c_suspension_2026_08_28.md` is the route. **No finding number allocated.**
**No guard enrolment of the new script.** No recommendation anywhere.

## 8. The self-check over this batch's own diff, as the standing rule requires

Read at the diff actually on disk, not at the intention.

1. **Principles.** **#19** — the population artifact establishes nothing and says so; its reach is
   declared UNMEASURED and its output published as a lower bound, never a census. **#12** — the
   previous aiming of the re-aimed tool is preserved beside the new one; the recorded search tier is
   counted rather than discarded; nothing found was dropped. **#13** — three refuted premises are
   surfaced as findings of this report rather than built around. **#17(f) / D-431** — no count of the
   population artifact appears in this report, in the close, or in either `STATUS.md` entry. **#6** —
   the five dispositions are not restated here, having one home; the population has one artifact.
   **#24** — no comparison of two measured quantities is asserted. Conforms.
2. **Conventions.** American English. No self-invented label: the disposition words are the phase
   definition's and were not used, no disposition having been taken. Music-theory words in their
   musical sense — *score* is the music, *key* is tonality, *bar* is the metric unit, *release* is a
   note's ending, *slice* is the stretch between change points; the prohibiting sense is written
   *exclude*, and *measurement tool* or *script* is used where the collided word would be wrong. No
   numeric grade anywhere.
3. **Figures and premises.** Every figure in this report is either a commit or blob identifier read at
   the object by explicit hash, a byte count proven by `cmp` against the object, or a guard tally from
   this batch's own two runs. **The population's counts are cited to the artifact and its field, never
   transcribed.** Every premise the dispatch supplied was re-checked at its own source before use, and
   the three that failed are in §4.
4. **The file-tools rule.** Working-tree content was read with Read, Grep and Glob throughout; the
   shell was used for git object queries by explicit hash, for the sanctioned enumeration and
   generator scripts, and for writes into scratch outside the repository. The guard refused two
   commands aimed at repository paths during this batch and both were re-taken through the file tools;
   **the refusals are recorded here rather than passed over.**
5. **Uncertainty.** The one uncertainty that matters is stated where it lives: the term search's reach
   is **UNMEASURED**, and the artifact says so rather than implying coverage it cannot claim.

## 9. Where the hashes this report cannot contain are found

The close commit and the end-state commit cannot name themselves. **Both are in the git log**, and the
close's own table names every commit that precedes them by explicit hash. **The end state is not
asserted in the close**; the one further commit carries it, per the dispatch's item 3.

---

*Provenance: CC, 2026-09-02, executing `cc_instruction_comparison_l0_l1_2026_09_02.md` at local tip
`4c9b7af5066fdf51e4b726f6fdc151b7e4153b0c` with `origin/master` three commits behind at
`f54995c092585f508c4ce572a6a4f553c033da3c`. Every commit and blob identifier was read at the object;
`origin/master` was read at its ref file after each push; the guard verdicts are this batch's own
runs. TOWARDS the ultimate objective and TOWARDS the guiding principles.*
