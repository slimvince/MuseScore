# CC report — the pilot prepared: the boot-pack generator of boot-list amendment (a1), and the withheld family for the harmony-boundary subject

> **Dispatch:** `cc_instruction_pilot_preparation_withheld_family.md` (Cowork, 2026-08-22), **as
> amended in place by that dispatch's own governing top block** after a previous Claude Code session
> started it and crashed before its Task 0 commit. Under Ruling 1 of
> `cowork_rulings_2026_08_22_pilot_order_sitting.md`, amendment (a1) of Ruling 1 of
> `cowork_rulings_2026_08_22_boot_list_sitting.md`, and Ruling 1 of
> `cowork_rulings_2026_08_22_member_two_leak_sitting.md`.
>
> **Commits, resolved at the objects by explicit hash:**
> Task 0 `c42f8141f46bf966e746358957b949e77c92db6c` (parent `dcbfa5fe329d4e096bbcc145465af708c62e9071`);
> Task 1 `a12cc0350322dd286708dcbf19d95548b01f7d55` (parent `c42f8141f4…`).
> Task 2's commit and the end-state commit are named in the close.
>
> **★ NO SESSION WAS BOOTED FROM THE PACK. NOTHING WAS DERIVED. NO ORACLE WAS OPENED.** Rendering
> the pack is not opening it, and this batch performed only the preparation the ruling names.
>
> **★ THE WITHHELD FAMILY IS AUTHORED AND CLEARS NOTHING** (D-655). Its verdicts are delivered as
> `ratification_surfaces/cowork_withheld_family_harmony_boundary_reading.md` and take effect only
> when the user rules them.

---

## 0. Words used in this report, explained at first use

- **The pilot** — the phase that proves the derivation method before the method is trusted.
- **An implementation-blind deriving session** — one that writes what the analysis *should* do for
  one unit without reading what the code or the specifications say it *does*.
- **The curated boot list** — the implementation-free read list such a session opens at boot; its
  membership was ruled 2026-08-22 (six members, eight exclusions, three amendments).
- **The boot pack** — the rendered, self-contained directory generated from that list, which a
  deriving session opens and outside which it opens nothing.
- **The held-out test** — one decision derived blind with the user's own ratified ruling on it
  withheld; that withheld ruling is the *oracle*.
- **The withheld family** — the recorded decisions, documents and passages cut out of the pack for
  one subject.
- **The index** — git's staging area; a *staged* path is one `git add` has recorded for a commit
  that has not yet been made.
- **A leak** — here, a rendered entry whose own text points into material the pack excludes.

## 1. The declared start state — MATCHED exactly

The dispatch declared two failing checks at the tree this batch would meet, each with its cause, and
said a third failing verdict or a membership difference beyond the one addition would be a
STOP-and-report.

Measured before the first edit, by running the whole guard set in check mode: **exactly two failing
checks**, and they are the two declared — [[OI-372]]'s tool, the one standing red; and the
evidence-pin membership check reporting its artifact STALE, caused by this dispatch's own untracked
ruling records. **`gen_guard_state.py --check` opened "STALE vs the run" for the same cause**, which
the dispatch declares is not a third failing check. **Zero STOP verdicts.** The guard classification
re-derived and passed.

## 2. Task 0 — the amended landing, and the tree that was actually met

**A1's check was taken FIRST and entirely at content-addressed objects**, because the bare
working-tree forms are denied by the armed guard and are measured to time out on this mount.

Every item of the dispatch's governing amendment held, and each was checked rather than assumed:

1. **The index was populated** with exactly the four original Task 0 paths and nothing else.
2. **The membership artifact was modified against the tip by exactly the crashed session's own
   regeneration** — the predicted route, the predicted amount, the predicted single name, and that
   record's appearance under the un-generated-document listing. Nothing else.
3. **The six other tracked paths the dispatch touches were unmodified against the tip.**
4. **The five untracked inputs were present and absent from the tip**, each checked at the object.
5. **`cowork_handoff.md` carried two inserted blocks** above the committed content, the earlier two
   headings marked superseded.

**And the population was enumerated rather than sampled.** A1 makes a modification at any other
tracked path a STOP, so the whole tracked-modification set was enumerated with the sanctioned
enumeration tool: it holds exactly the four paths above and no other. The check could not have been
satisfied by looking only where the dispatch pointed.

**★ ONE THING THE DISPATCH DID NOT DESCRIBE, AND WHAT WAS DONE ABOUT IT.** The crashed session also
left a **zero-length `index.lock`** in the git directory, which refused every staging operation. Its
cause was ESTABLISHED before the mechanism was touched, in three independent ways: no git process
was running; the lock was zero bytes, so nothing had been written into it; and the live index was
intact and consistent, having just been read successfully against the tip. Git's own error message
prescribes removing it by hand in exactly this state. It was removed, and nothing was lost — a
zero-length lock holds no content, and the index is a separate file. **Recorded here as an act this
report performed and the dispatch did not name.**

**The membership artifact was then REGENERATED over the tree as it now stands and its difference
MEASURED against the committed blob before it was accepted, from every route.** Route A moved by
exactly the predicted amount with exactly the predicted three names. Route B added nothing: none of
the three landed ruling records carries the word that route matches on — checked at the records
themselves. The blind session's brief did **not** enter, being no ruling record. Nothing else moved:
no member, no route, no document, no pin constant, no state and no count. The one further difference
is an **additive derived cross-reference** caused by the very act the dispatch orders, which the
standing clause on a derived artifact's difference admits and which is reported rather than absorbed.

**Seven paths were committed and no other**, each re-staged by explicit path — the crashed session's
staging was not trusted — and the staged set was enumerated before the commit rather than assumed.
Pushed; `origin/master` verified at the object to name the Task 0 commit. The membership check then
**PASSES** at the resulting tree, so the guard set stands at one failing check from Task 0 onward.

**Registered expectation E0 — MET in every particular**, at the amended figures.

## 3. Task 1 — the generator, the candidates, the authored family, the rendered pack

One commit, as the dispatch requires: a tree with the generator and no artifact, or an artifact and
no guard registration, was never committed.

### 3.1 What the generator is, and what in it is authored rather than derived

`tools/audit/gen_derivation_boot_pack.py` renders the ruled boot list into
`tools/audit/derivation_boot_pack/<subject>/` and publishes what it did at
`tools/audit/derivation_boot_pack.json`.

**AUTHORED:** the six ruled members and the spans that make them up, **each by anchor text and never
by line number**, imported from the ruled draft rather than re-decided; the withheld table per
subject — identities, documents and passages, each with its finding, its date and its reason, in the
shape the specification-document-set tool already uses for an authored exclusion; and one verdict per
derived candidate.

**DERIVED:** the candidate list with its matching criterion per candidate; the two `ARCHITECTURE.md`
oracle spans, located by their own text on every run; the cross-reference additions; the cut of the
design-intent class; the leak check; every rendered file byte for byte; and every count.

**Its STOPs are what make it a derivation rather than a rendering.** An anchor that does not match
exactly one line halts it — so no span is ever cut from a coordinate that has drifted, which is the
whole reason the boot list was ruled by anchor. A candidate with no authored verdict halts it, and a
verdict for an entry the derivation no longer returns halts it too: the two directions together, so
a candidate cannot be graded by silence and a verdict cannot outlive its subject. A withheld identity
outside the design-intent class, one nobody derived as a candidate, a withholding record missing its
finding, date or reason, a verdict outside the closed three-value vocabulary, a distribution that does
not account for the population, a member's source file the tree does not carry, and a withheld
passage whose anchors do not resolve exactly once inside their ruled scope each halt it as well.

### 3.2 The candidate derivation, and the bound stated on it

The criterion is the dispatch's own, applied over the design-intent class: group E; the two named
home documents; a home inside either oracle span, each located by its own text; a case-insensitive
match of eighteen fixed words over four fields; and the identity the ruling names.

**Its reach is a plain substring match and is DECLARED UNMEASURED on the artifact**, under the
standing clause for an enumerating pattern, whose test is met: no analysis decision consumes the
enumeration — the user does. Every figure is at
`tools/audit/derivation_boot_pack.json` → `subjects.harmony-boundary.counted` and none is restated
here (**D-431**).

**★ A FINDING ABOUT THE CRITERION, SURFACED RATHER THAN ABSORBED, AND WHAT WAS DONE.** Two candidates
reported a keyword match this report could not see in their own text. Rather than accept the tool's
word or explain it away, the entry was read at the register's data file through the file tools — and
the match is real: **`slice` occurs inside `isLicensedProgression`**. The pattern fires inside longer
words, which is a property of the substring match the dispatch fixes and not a defect in it. **The
tool was changed to publish, for every keyword match, the matched text IN ITS OWN CONTEXT**, so a
match a reader cannot see can no longer stand unchallenged. Three candidates reach the list only that
way — two through `release` inside *released* — and each says so in its own verdict and in the
reading file.

### 3.3 The authored family — IN, OUT, UNPLACED

Every candidate carries exactly one verdict with its finding, its date and its reason. The test was
applied concretely: **IN** where the entry discloses either where a boundary falls or which evidence
outranks which in deciding one; **OUT** where it discloses neither, with what it bears on instead
stated; **UNPLACED** where the entry's own text does not settle it. **Default nothing** was honoured:
three entries could not be defended either way in one sentence at their own verbatim and were left
UNPLACED with exactly what was read, rather than guessed into a class. Each of the three names a
boundary-adjacent phrase inside an entry whose subject is plainly another unit; none is recommended
in either direction, because where the record does not settle a question the surface that returns it
gathers facts and makes none.

The identity amendment (a1) names is graded IN, and the generator STOPs if it were not. The withheld
document is the one the ruling records as oracle material. The **derived cross-reference additions**
are published whole, with the field and identity that matched, and with their bound stated: one pass,
from the authored identities only, **not transitive**. Several of them are entries graded OUT — an
entry can be irrelevant on its own subject and still be a route to a withheld one, and both facts are
kept (#12).

### 3.4 The pack as rendered, and the two withholdings that cut into it

Seven files: a read-me and the six ruled members, rendered in order. The read-me carries the
session-boot guard the dispatch specifies — this directory replaces the ordinary session-start read;
nothing outside it is opened; no branch rule is taken; and if the session nonetheless meets a
statement about how this project's analysis currently works it stops reading that file and records
where it was and how much it had seen.

**The leak check is scoped to the two members the tool GENERATES**, and the scope is stated on the
artifact, in the tool's docstring and in the reading file, because a scope that is not stated reads as
total. Three entries were listed rather than rendered, each for a path into the implementation's own
documents or code. **A leak in the four members quoted whole is deliberately not checked**: those
members are ruled whole, and member (2) names `ARCHITECTURE.md` in the never-work-from-memory rule by
design — a string check over them would strike the rule that tells a deriving session where a primary
source lives.

**The withheld passage ruled the same day is applied.** It is located by its own text — never by line
number — inside the bullet the ruling scopes it to, with the anchors required to resolve exactly once
and the closing required to follow the opening. It is cut from the rendered member and marked in place
with one line saying a passage is withheld for this subject, carrying no content and no reason.
**`CLAUDE.md` itself is untouched.**

**Verified after rendering, at the pack itself:** none of the oracle's own phrases occurs anywhere in
the directory, and the design-intent member carries no withheld identity, no withheld document name,
no `ARCHITECTURE.md` and no `docs/` or `src/` path.

### 3.5 The registration, and A4 graded route by route

The tool was registered in **both** guard registries in the same commit that adds it, **by pure
insertion — no line of either registry was removed or changed**, verified at the diff.

- **`guard_state.json`** — the population rises by exactly one; the addition is the new generator's
  check, PASSING; the failing set is unchanged at [[OI-372]]'s tool; zero STOPs. **As predicted.**
- **`guard_classification.json`** — one added member with its authored verdict and its evidence
  citation, read in this session at the tool it names. **As predicted.**
- **`epoch_write_path.json`** — the tools walked rises by one; **members UNCHANGED**; the new tool
  appears only in the non-member listing. **As predicted.**
- **`recognizer_establishment_sort.json`** — it gains exactly the records its derivation writes for
  one new tool; **no existing member's classification moves**; every change is additive. **As
  predicted.**
- **A3 route C** — the new tool did **not** enter the evidence-pin membership artifact, and the
  membership check still passes. **As predicted.**

Each was measured against the committed blob before it was accepted, not after.

*Recorded because it is a fact about the new tool and not a defect to chase: the recognizer sort
places it on the **no independently-known population** side, because its candidate collection is not
assigned to a key of its own artifact in the shape that sort's recognizer looks for. Its candidate
list IS published whole, as the verdict rows. Reshaping the tool to satisfy a recognizer would be
fitting to the detector, which the defect catalog names, so it was not done — the classification is
reported instead.*

**Registered expectation E1 — MET.** The generator registered in both registries with its check
passing; the six members rendered by anchor; the leak check run on the two generated members with
every leak listed rather than rendered; the candidate list published whole with its criterion per
candidate and its bound stated; every candidate carrying exactly one verdict with finding, date and
reason; the derived additions published with their cause; the manifest and every pack file re-derived
byte-identically by the check; and **`ARCHITECTURE.md`, `DEFECT_TYPES.md`, `CLAUDE.md`,
`cowork_design_doc_template.md`, `cowork_audit_protocol.md`, the phase-definition surface,
`DECISIONS.md`, the register's data file and the sort artifact all byte-unchanged**, each verified
individually. No session booted.

## 4. Task 2 — the reading file, the pointers, the close

The reading file `ratification_surfaces/cowork_withheld_family_harmony_boundary_reading.md` is
written in the standing ratification-surface shape: the subject re-explained from scratch, the oracle
as Ruling 4 states it (quoted, with the oracle's own content deliberately not restated), the candidate
criterion with its bound, and then **five lists** — IN, OUT, UNPLACED, LEAKS, and the withheld
passage — each candidate with its identity, its title and its one-sentence reason, each UNPLACED with
what was read, and each leak with the field and string that matched. It states what the user is asked
to rule and what the ruling does not do. **No recommendation is made on any UNPLACED candidate.**

One `STATUS.md` pointer entry per task that did work; the previous batch's entries moved verbatim to
`STATUS_ARCHIVE.md` through the forward-bound tool at its three declared authored inputs — **authored
input maintenance, licensed in terms by this dispatch, so it is not a departure** — with the
reconciliation proved in both directions by that tool's own check. The session-start read measurement
was regenerated, which is the red the dispatch predicted at the close and the act that clears it.

## 5. Assumptions and expectations, graded

| | Verdict |
|---|---|
| **A1** — the working tree, stated by content | **HELD**, item by item, at the objects, with the whole tracked population enumerated. One state the dispatch did not describe — the stale index lock — is reported in §2. |
| **A2** — one red remains, zero STOPs | **HELD.** The reds this batch caused were exactly the ones declared, each cleared in the act that caused it. |
| **A3** — the membership regeneration from every route | **HELD** on all three routes, measured before acceptance. |
| **A4** — the guard registry from every route | **HELD** on all four artifacts; every movement additive and inside the prediction. |
| **E0** | **MET** (§2). |
| **E1** | **MET** (§3.5). |
| **E2** | Graded in the close, at the tree that carries it, and **not asserted here** — the end-state run is a later commit than this report. |

## 6. Declared departures, and acts this dispatch did not name

1. **The stale `index.lock` was removed** (§2). Cause established at three independent facts before
   the mechanism was touched; git's own message prescribes the act; nothing was lost.
2. **The generator gained a field the dispatch did not ask for** — the matched text in its own
   context, per keyword match (§3.2). It was added because a match a reader cannot see is a match
   nobody can challenge, and it is what turned an apparent tool defect into an established property
   of the pattern.
3. **The manifest carries each candidate's own verbatim and plain restatement** beside its verdict,
   so every verdict is checkable at the text it was made from. This is the manifest and not the pack:
   the pack directory is what a deriving session opens, and its read-me forbids opening anything
   outside it.
4. **`gen_status_batch_bound.py`'s three authored inputs were re-aimed and the previous aiming
   appended rather than overwritten** — authored-input maintenance, licensed in terms by this
   dispatch.
5. **One accidental empty interpreter invocation** occurred while composing a shell command; it
   opened an interactive interpreter that errored out immediately and wrote nothing. Recorded because
   an unrecorded stray act is worse than a recorded one.
6. **Reads not performed:** no boot-list member was read beyond the spans the generator renders and
   the anchors it locates; `cowork_blind_session_brief_harmony_boundary.md` was read at its status
   banner only, as the dispatch directs; the two evaluation reports, the sizing surfaces and the
   corpus artifacts were not opened.

## 7. The standing self-check over this batch's own diff

1. **Principles.** **#19** — the family is authored and clears nothing until ruled; the criterion's
   reach is declared unmeasured on its own artifact; the new tool's guard verdict states what it does
   NOT assert. **#6** — the withheld family has one home, the generator's authored table, and the
   pack is derived from it rather than a second copy kept by hand. **#12** — OUT and UNPLACED verdicts
   are kept beside IN, the leaks are listed rather than dropped, the previous forward-bound aiming is
   appended rather than replaced, and the withheld passage is cut from the pack and not from its home.
   **#17(f)/D-431** — no count is transcribed anywhere in this report, the reading file, the commit
   messages or the `STATUS.md` entries; every figure is named to an artifact and a field. **#13** —
   the one surprise (a match the text did not appear to contain) was surfaced and established at the
   objects before anything was built around it. **#24** — no comparison between measured quantities
   is asserted. **Conforms.**
2. **Conventions.** American English. No self-invented label: `WITHHELD`, `derived_because` and the
   read-me's name follow the tools' own authored/derived shapes and are explained at first use.
   Music-theory words in their musical sense — the new prose was swept for the reserved set and three
   bare non-musical uses were corrected before the commit (*scale* as magnitude, and two numerical
   uses of *score*), *measurement tool* is used and never the reserved word, *the decisions register*
   is written in full.
3. **Figures and premises.** Every quantity is at its artifact; every ruling is quoted at its record;
   every premise the dispatch carried was re-derived rather than accepted, and the two facts about
   the register's own text were read at the register's data file rather than at a surface repeating
   it.
4. **The file-tools rule.** Working-tree content was read with the file tools throughout. Shell use
   was limited to read-only git object queries by explicit hash, the sanctioned enumeration tool, and
   running the project's own scripts. The armed guard denied four attempts during this batch — a
   working-tree `git diff` without a hash, a `wc` over repository paths, a `grep` over a repository
   path, and two interpreter invocations carrying a literal repository path — and each was replaced
   with the file-tools or explicit-hash route rather than worked around.
5. **Uncertainty.** No difference between two measured quantities is asserted anywhere in this batch.

## 8. Quarantined audit questions

**None new.** This batch derived nothing about the analysis and measured nothing about it. The five
already surfaced stand exactly as they were, unacted on, and are not restated here.

## 9. What this batch did NOT do

No session booted from the pack; no derivation; no comparison; no oracle opened; no pilot act beyond
the preparation the ruling names. No boot-list member edited at its home. No register entry, sort
artifact or register data file touched. No open-items row created, flipped or discarded — [[OI-179]]
stays OPEN and GATES, [[OI-372]] and [[OI-374]] stand as found. No finding number allocated. No
`src/` change, no golden, no test changed, moved or run, nothing under `tools/corpus/` or
`tools/robust_stop/`. No document archived, moved or deleted as a file — the `STATUS.md` entries the
forward bound moved are the one licensed exception and are proved present in the archive and absent
from the must-read.

---

*Provenance: Claude Code, 2026-08-22, executing `cc_instruction_pilot_preparation_withheld_family.md`
as amended. Every commit hash above was resolved at the object before it was written. TOWARDS the
ultimate objective and TOWARDS the guiding principles.*
