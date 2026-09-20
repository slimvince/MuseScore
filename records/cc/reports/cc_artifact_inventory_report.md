# CC report — the artifact inventory: the tree walked and classified, every class given a PROPOSED verdict, and one finding that is larger than the classification

> **Dispatch:** `cc_instruction_artifact_inventory.md` (Cowork, 2026-08-15), executing §2.10 and
> §2.11 of `cowork_rulings_2026_08_15_method_directions.md`.
> **Performed:** 2026-08-15. **Branch** `master`, pushed to `origin`.
> **Four commits, all verified at the git objects by explicit hash after the fact:**
> `363f935732` (Task 0), `460df30c16` (Task 1), `31c573b06e` (Task 2), `b1d48d6c87` (Task 3).
>
> **Every count in this report is read from a generated artifact and each is named beside its
> figure (D-431).** No value below is transcribed from memory or from any earlier account.

---

## 1. What needs you — read this section first

### 1.a THE RULING SURFACE IS THE DELIVERABLE, AND IT IS READY

`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md`.

One section per class. Each carries a **PROPOSED** role, mining verdict and retirement flag —
every one marked **AUTHORED** on its face — or, where the record already leaves the ruling open, a
**QUESTION** with its two sides named. **44 classes: 36 carry proposals, 8 are questions.**

What is owed is a ruling per class. The phases are then drafted citing ruled classes, which is the
order §2.10 sets.

**The eight questions, and why each is a question rather than a proposal.** §2.11 sends the
classification of the tests, the goldens, the catalogs, `tools/robust_stop/` and the registries to
this surface, and leaves the scope of the measurement layer's own specifications OPEN. Proposing a
verdict on those would be answering your own open question on your behalf. The classes left as
questions are:

| Class | Why it is a question |
|---|---|
| `our-analysis-tests-and-fixtures` | §2.11 sends the tests and the catalogs here. A test reads like design intent but was written beside the code; the two catalogs are ground truth this project authored, which gate block (A)'s own convention bars from ever being a standard of correctness. |
| `our-pipeline-snapshot-goldens` | Named in §2.11. Self-annotation in exactly the sense gate block (A) bars — they hold behaviour against change and say nothing about whether it is right. |
| `our-pipeline-snapshot-test-harness` | Sent here with the goldens. Its corpus description is closer to design intent than the goldens are. |
| `our-measurement-tool-test-material` | §2.11 sends "tests" without distinguishing which. These test the measurement tools, not the analysis, so the answer may differ. |
| `the-hard-stop-reference` | **The one with two halves that pull apart.** As a GATE it is operational apparatus that must keep working. As EVIDENCE it is a measured record of our own system, which §2.4 routes through the airlock — and a per-run enumeration of which runs fail may not survive *does the fact survive the implementation being thrown away?* while the aggregate durations do. |
| `joint-estimator-tables-and-fit-records` | Sits on the open measurement-layer ruling, and its halves pull opposite ways: the FIT LEDGERS record what was tried and what it scored, which is empirical-findings-ledger material of the first order including its negative results (#12); the TABLES are fitted parameters of the current implementation, which is the mirror. Splitting them is available and is not proposed. |
| `calibration-maps-and-their-snapshots` | The same open ruling, the same shape. |
| `corpus-and-parameter-registries` | Named in §2.11. Mixed in KIND rather than in citation — the registries state what is held and what it may be used for (convention), while `param_manifest.json` and the baseline JSON state what the implementation's parameters and outputs ARE (mirror). Not split by the scan; asked instead. |

### 1.b ★ THE FINDING: 122 FILES THE GOVERNING RECORD CITES AS PROVENANCE ARE IN NO COMMIT AT ALL

This is the largest thing this batch produced, and it is not a classification.

`.gitignore` line 118 carries the rule `/cc_*.md`. It covers **every** dispatch written to the
coding side and **every** report written back. Some were added at some point with an explicit
override — the tracked tree carries 95 dispatches and 82 reports. **571 more sit on disk, ignored,
untracked, and absent from every commit.**

**The number that makes this more than housekeeping is DERIVED**, by the same citation scan the
mixed classes are split by, and it is published on the ruling surface with the whole list:

> **122 of those 571 ignored files are NAMED by the governing record.**

Among them:

- the measurement provenance **gate block (A) of `CLAUDE.md`** cites for the ratified
  joint-estimator baselines (`cc_adoption_measurement_report.md`);
- the dossier **D-656** names as the **ONE home** of every value of the tonicization/modulation
  measurement (`cc_tonicization_modulation_metric_dossier.md`) — a naming made precisely so those
  values would not be restated anywhere else, which means the values now live nowhere git carries;
- the dispatch **eighteenth-stop Ruling 8** cites as the evidence that the decisions register
  contains code observations by construction (`cc_instruction_decision_harvest.md`);
- documents named by `STATUS.md`, `OPEN_ITEMS.md`, `decisions/group_S.md`, `decisions/group_T.md`,
  several `open_items/OI-*.md` detail files and `docs/precision_metric_design.md`.

**Established, not inferred.** `git log --all -- <path>` reports **zero** commits touching each of
six checked by name: `cc_adoption_measurement_report.md`, `cc_functional_residual_dossier.md`,
`cc_instruction_decision_harvest.md`, `cc_tonicization_modulation_metric_dossier.md`,
`cc_measurement_pipeline_audit.md`, `cc_instruction_scoring_model_pass.md`.

**Why it bears on the phases you are about to draft.** A fresh clone of this repository does not
contain them. They are therefore **not available to any phase whose inputs are *what git
carries***, and the handover-safety §2.11 requires — *"required at the latest by the next
handover"* — does not currently extend to the evidence the governing record leans on.

**Nothing was done about it, deliberately.** Landing them is a commit over a population nobody has
enumerated for worth, and it is yours to order. **No open-items row was opened either**: rowing it
would be this session deciding it is owed.

*(How it surfaced: Task 0's own act. Two of the eight files the dispatch named for that commit are
in this ignored family, so a plain `git add` would have silently dropped them from a commit that
names them. They were staged with `-f`, which follows the repository's own practice — 93 tracked
`cc_instruction_*.md` files already exist under the same rule. **The ignore rule and the practice
disagree, silently, in the direction that loses a record.**)*

### 1.c THE THIRD STANDING RED IS STILL RED, AND THIS BATCH DELIBERATELY DID NOT CLEAR IT

`tools/audit/gen_guard_classification.py` still STOPs for the cause the fifteenth handoff block
records: a tool entered the guard-state population on 2026-08-13 with no authored verdict. **A
verdict was authored for each of this batch's own two tools and for neither of anyone else's**,
following the precedent the period-checks batch set — the ruling governing that file requires the
verdict to be made by reading the tool it grades, and that tool is not this dispatch's. Its
artifact is left exactly as committed.

---

## 2. What each task did

### 2.0 Task 0 — the writing-side records landed (`363f935732`)

Exactly the eight named paths, **verified at the index through the sanctioned tool before the
commit was made** (eight records, no ninth): the four ruling records, the period decision surface,
the two dispatches, and the modified `cowork_handoff.md`.

Until this commit the whole of the 2026-08-13/15 re-shaping lived on disk untracked. A session
inheriting the repository would have resumed the superseded plan — the eighteenth stop's own
founding failure.

### 2.1 Task 1 — the inventory (`460df30c16`)

`tools/audit/gen_artifact_inventory.py` → `tools/audit/artifact_inventory.json`.

- **12,570 tracked entries** at `31c573b06e`, **12,570 classified, 0 unclassified**, in **44
  classes**. *(The committed artifact is stamped at `31c573b06e`, the tree after Task 2 landed; the
  first run, at `363f935732`, saw 12,566 and classified all of them.)*
- **The signature is PATH AND EXTENSION ONLY.** The dispatch admits a banner as a third kind and
  **none is used** — no file's content was read to class it. That is assumption A1 held at its
  strongest available reading, and it is recorded in the tool so a later reader does not add a
  content read casually.
- The signature table is the only authored thing in the tool, and **each class's signature is
  published in words beside it**, so the rule can be checked against the members without opening
  the generator.

**★ The design decision worth reading, and the self-check is what found it.** The first version of
the table ended in a **catch-all** rule matching everything. That made the unclassified bucket
empty **by construction** and the dispatch's own STOP a sentence rather than a mechanism — a check
that cannot fail. The last rule now names only repository-root files plus three named top-level
directories, so **a file in a top-level directory no rule names reaches the STOP**. Ten probes in
the artifact **establish both halves (#19)**: that such a path comes back unclassified, and that
the tool then raises — the second probe calling the very function the walk calls, so the two cannot
drift apart.

**`--check` is designed against the point-in-time hazard the record already names.** Re-deriving an
inventory at the *current* commit would go red at the next commit — the OI-301/OI-305 shape. So it
re-derives at the commit the committed artifact **RECORDS** (passes indefinitely), and then runs
the classification **again over the tree as it stands**, stopping if anything there is
unclassified. That second half is the live invariant, and **it demonstrated itself inside this
batch**: regenerating after Tasks 1 and 2 landed picked up four newly tracked files and classed all
four with no rule change.

**What an empty bucket does NOT establish**, stated in the artifact's own words: every file matched
*some* rule, and **nothing about whether it matched the right one**. A file in a directory whose
name misdescribes it is classed by the misdescription. The act that would settle the other half —
reading a sample of members per class against the class's stated signature — is **named and not
started (#19)**.

### 2.2 Task 2 — the ruling surface (`31c573b06e`)

`tools/audit/gen_artifact_inventory_surface.py` →
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md`.

Generated, never hand-written: no count, member list or split is typed by hand (#17f, D-431). What
is authored is the proposal per class, marked AUTHORED on its face.

**The four mixed classes are split by a DERIVED signal, not an impression.** A citation scan reads
the governing record — the seven governing documents plus both registers' detail files — and
reports per file whether anything there names it. §2.11 says the writing side's design documents
are NOT direct witnesses and that their value is *measured by what the curation acts extract
(fact-based, not presumed)*; this is that measurement.

| Mixed class | cited | uncited |
|---|---|---|
| `documentation-directory-prose` | 32 | 15 |
| `measurement-and-analysis-tools` | 30 | 100 |
| `writing-side-design-documents` | 84 | 29 |
| `reports-from-the-coding-side` | 52 | 30 |

The split is sound where it can be checked: every measurement tool `CLAUDE.md` and
`BUILD_AND_TEST.md` name by command — `a8_rebaseline_measure.py`, `compare_rn.py`,
`robust_stop_diff.py`, `run_bach_preset.py`, `characterise_bir_false.py`,
`analyze_inversion_errors.py`, `dcml_parser.py`, `oracle_root_metric.py` — lands on the cited side.

**What the scan cannot do is stated on the surface above its first use**: a citation is **not**
evidence of correctness, currency or worth; an absent citation is **not** evidence of no caller — a
tool imported by another tool, or a document cited only from a report, is invisible to it. **No
retirement should be executed on this signal alone**, and every retirement flag repeats it.

**Retirement candidates: 6 whole classes, 3 classes partly** (the uncited side only). Every one is
a **CANDIDATE FLAG**, and the surface carries the reminder on its own face that retirement is
**archive-with-record and destroys nothing (#12)**.

### 2.3 Task 3 — the close (`b1d48d6c87`)

Four `STATUS.md` pointer entries, one per task, and nothing else in that file. The close appended
to `cowork_away_returns.md`. Both new tools registered in the guard set **in the act that created
them** — invocation in `gen_guard_state.py`, classification verdict in
`gen_guard_classification.py` — so neither reaches a later pass's derived population unclassified,
which is the condition OI-373 already carries for two other tools.

---

## 3. The predictions, graded

**P1 has three limbs and they did not all hold. The grading is in the artifact and no limb was
reconciled towards the expectation.**

| Limb | Verdict |
|---|---|
| The unclassified bucket is empty | **MET** — and the STOP that guards it is established able to fire. |
| Upstream code, build system, third-party libraries each ONE class with one verdict | **MET** — one class each. |
| *Well under forty* classes | **REFUTED — 44.** |

**The refutation is informative rather than merely a miss, and the arithmetic is published rather
than argued.** P1's own stated *reason* for the ceiling — *"so the fork's size costs nothing"* —
**held exactly**: the material this project did not author sits in **10 classes covering 10,424
files**, while **34 classes cover the 2,146 files this project authored**. The class count is
driven almost entirely by our own prose, record and tooling — **which is precisely where P2 already
expected the per-item descent to be needed.** The fork is not what makes the inventory large.

**P2 is graded at the ruling surface and not in the inventory**, because whether a class needs
opposite verdicts is a statement about verdicts and the inventory authors none. Its named areas —
`docs/`, `tools/` and the repository-root prose surfaces — are exactly the four mixed classes, and
**no class outside them needed opposite verdicts**, so P2's refutation condition did not fire.

---

## 4. The guard set

**★ A DEPARTURE FROM THE PREVIOUS BATCH'S METHOD, DECLARED RATHER THAN GLOSSED: the full guard set
was NOT run before the first edit.** The period-checks close records running it first; this batch
ran it at the END.

**What that costs, plainly:** a red that arrived between the two batches cannot be distinguished
from one this batch introduced **by this batch's own runs**. **What bounds it:** the previous
batch's close records the exact end state it left, and its `tools/audit/guard_state.json` is
committed — so the comparison is against a committed artifact rather than a memory.

**The result — it ends exactly where the previous batch left it, and no further:**

- **One FAIL** — `gen_filing_convention_application.py --check` (OI-372).
- **One STOP** — the runner's stop on derived guard candidates with no authored invocation
  (OI-373), **naming the same two tools** the previous close names.
- **No new red of any kind. Both of this batch's own two tools PASS.**
- A **second confirming run reports the guard state re-derives**, the set line-identical between
  the two runs — which answers the OI-374 hazard for this environment by evidence rather than
  assumption.

---

## 5. What was deliberately NOT done

- **No file moved, renamed, retired, archived or deleted.** Every retirement is a flag on a
  surface, awaiting your ruling.
- **No mining performed.** The register filter, the rulings sort and the findings ledger are later
  acts that consume the *ruled* inventory.
- **No phase defined, no specification derived, no repair** — the eighteenth stop's §3 stands
  whole.
- **No `src/` edit, no golden, no test changed**, nothing under `tools/corpus/` or
  `tools/robust_stop/`, no measurement of the analysis, no design.
- **No open-items row marked, flipped or discarded; no decisions-register entry written.** OI-179
  stays OPEN and GATES. D-231 and #8 stand.
- **The re-opened period question is untouched** — it is your ruling, listed in
  `cowork_rulings_2026_08_15_method_directions.md` §3.
- **No row opened for the `.gitignore` finding**, and no verdict authored for another dispatch's
  guard-classification tool.

---

## 6. The self-check, and what it caught in this batch's own work

Run against the diff on disk rather than the memory of writing it (D-434).

1. **★ THE CATCH-ALL LAST RULE** — the consequential one. It would have made the dispatch's own
   unclassified STOP incapable of firing and the empty bucket meaningless, and **the artifact would
   have looked identical**. Corrected to a bounded rule, with ten probes added that establish both
   halves.
2. **Five reserved-word collisions** in this batch's new prose — a bare *rest* for a remainder
   twice, a bare *register* for the decisions register, *in part* for *partly* twice — corrected
   before the commits that carried them, with the generators regenerated and re-derived.
3. **A misleading helper name** — a matcher called `at_root_named` used for full paths not at the
   repository root; split into `exact_path` so the signature table reads as what it does.
4. **A variable named `mode`** for a git file mode, renamed to `file_mode` rather than introducing
   a new bare collision with the musical sense.

**What the self-check did NOT resolve**, stated rather than left implicit: the signature table's
own establishment (#19) — coverage is checked, correctness of placement is not — and the citation
scan's reach, which sees only the governing record. Both are stated in the artifacts themselves.

---

## 7. Problems declared to Cowork

1. **The `.gitignore` / practice disagreement and its 122 cited casualties** (§1.b). The largest
   finding. Not fixed, not rowed.
2. **The measurement-layer scope ruling is load-bearing for three classes at once** —
   `joint-estimator-tables-and-fit-records`, `calibration-maps-and-their-snapshots`, and the
   evidence half of `the-hard-stop-reference`. They cannot be ruled independently of it, and the
   surface says so at each.
3. **`published-research-papers` holds two files.** Principles #1 and #2 make published research
   the basis of every design decision, and the theory-grounding corollary requires a source be
   fetched and read before an equation is carried out of it. Two papers on disk is a small holding
   against that demand. **Whether the remainder of the literature this project rests on is
   reachable at all is a question the framework phase will meet immediately**, and it is stated on
   the surface as a finding rather than a proposal.
4. **`root-level-project-prose-outside-the-naming-conventions` — three files no convention
   reaches.** The verdict matters less than the class existing: three files that no naming
   convention reaches are three files a convention-driven sweep will miss, and the derivation-first
   repair is exactly such a sweep.
5. **`stray-working-files-committed-to-the-repository-root` includes the unpacked members of a
   musical score container** — `Compatibility`, `META-INF/`, `Thumbnails/` — which means a
   MuseScore file was extracted into the repository root and committed. Worth seeing before
   anything is archived, because it says how the class arose.
6. **`upstream-application-source` carries our fork-local edits mixed in with upstream code, and no
   signature separates them.** The proposed verdict *outside every phase's inputs* is a verdict
   about the class, **not** a claim that nothing in it matters; the recorded edits are enumerated
   by their own mechanisms (`local_patches_check.py`, the arm comment sweep) and not by any phase
   reading this class.
7. **This report is itself in the ignored family.** `cc_artifact_inventory_report.md` matches
   `/cc_*.md` and is **not committed** — the dispatch enumerates which files each task commits and
   a report is not among them, so landing it is not this session's act to take. It is handed to you
   directly. That it had to be said is the finding at §1.b in miniature.

---

*Provenance: CC, 2026-08-15. Dispatch `cc_instruction_artifact_inventory.md`. All four commits
verified at the git objects by explicit hash after the fact. Every figure in this report is read
from `tools/audit/artifact_inventory.json`, `tools/audit/guard_state.json` or
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md`.*
