# The L0+L1 boot pack — the generator extended, the render STOPPED (report, 2026-08-31)

> **STATUS: CLOSED ON THE RULED STOP FORM.** Written by the CC run of
> `cc_instruction_l0l1_boot_pack_2026_08_31.md`, executing Rulings 11, 12, 15 and 16 of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md`.
>
> **★ THE HEADLINE, BECAUSE IT DECIDES HOW THE REST IS READ.** The generator IS extended and the
> extension IS proven additive — every file of both existing packs renders identically under the
> pre-batch and the post-batch generator at the same sources, and the manifest differs only by the
> added subject. **THE PACK WAS NOT RENDERED TO DISK.** A STOP the dispatch itself names fired
> before the write: **both existing packs were ALREADY STALE at the commit this batch started
> from**, so Task 6's `--check`-green and byte-identical conditions cannot both hold, and §4's
> *"a difference anywhere in either existing pack is a STOP, not a thing to explain afterwards"*
> settles which way that falls. **Nothing was written to either existing pack, to the new pack
> directory, or to the manifest**, proven by re-hash.
>
> Per the OI-222 pointer convention this report POINTS at its artifact,
> `tools/audit/l0l1_boot_pack_extension.json`; no count and no hash is restated here (**D-431**).

## Task 2 — THE PREDICTION, WRITTEN BEFORE TASK 3 WAS BEGUN

**#17(b): the prediction is recorded before the measurement, not after.** It was written to the
artifact and to this report before the first character of the generator was edited, and the
pre-batch state of every file it names was pinned to a git blob in the same act.

> **The extension is additive and per-subject. The ruled six members stay in every pack, unchanged
> and in their ruled order. For the two existing subjects the extras list is EMPTY, so
> `tools/audit/derivation_boot_pack/harmony-boundary/`, `…/scoring-model/` and
> `tools/audit/derivation_boot_pack.json` MUST re-render BYTE-IDENTICAL.**

## Task 1 — the generator, established at the file and not taken from the dispatch on trust

Everything below was read at `tools/audit/gen_derivation_boot_pack.py`, and each is named by its
own symbol.

- **`MEMBERS`** — a list of six member records in order: (1) `01_the_phase_definitions.md` from
  `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`, one heading-to-heading
  span; (2) `02_the_guiding_principles_and_the_conventions.md` from `CLAUDE.md`, two spans, a
  heading-to-paragraph and a heading-to-eof; (3) `03_the_writing_standards.md` from
  `cowork_design_doc_template.md`, whole; (4) `04_the_dispatch_protocol.md` from
  `cowork_audit_protocol.md`, heading-to-eof; (5) `05_the_ratified_design_intent.md`, GENERATED;
  (6) `06_the_defect_type_catalog.md`, GENERATED. Beside it **`READ_ME`** names
  `00_READ_THIS_FIRST.md`, which is not a member and is not in the read-me's own listing.
- **The three authored subject tables** are **`WITHHELD`**, **`CRITERION`** and **`VERDICTS`**.
  **`build_subject` STOPs on absence from `WITHHELD` and on absence from `CRITERION`, and NOT on
  absence from `VERDICTS`** — that one is read through `VERDICTS.get(subject, {})`, so a missing
  entry becomes an empty grading, which then STOPs only if the derivation returned a candidate.
  **`build` enumerates subjects from `sorted(WITHHELD)`**, so `WITHHELD` is what makes a subject
  exist at all.
- **`write_all`** writes the manifest to `tools/audit/derivation_boot_pack.json` **for every
  subject on any invocation**, and then, per subject, creates
  `tools/audit/derivation_boot_pack/<subject>/` and writes each rendered file. **`--subject`
  filters only the directory writing, never the manifest** — which is why no partial render was
  available to this batch.
- **`check_all`** compares three things: the manifest on disk against the re-derived JSON text;
  the sorted **directory listing** of each pack against the sorted set of generated file names;
  and each file's content against its re-rendered text.
- **`render_read_me`** stated *"## The six files of this pack, in order"* with the count
  **hard-coded**, built its listing from the global `MEMBERS`, and carried a dead local naming the
  pack's files as read-me-plus-`MEMBERS`.

**The `scoring-model` precedent, established specifically because Ruling 16 rests on it and this
side had it only as a relayed claim: IT EXISTS AS DESCRIBED.** At the generator,
`WITHHELD["scoring-model"]` carries `withheld_documents: {}`, `withheld_passages: []` and no
`the_identity_the_ruling_names`; `CRITERION["scoring-model"]` has every term empty; and
`VERDICTS["scoring-model"]` is `{}`. At the rendered manifest the same subject shows an empty
identities list, an empty documents object, an empty passages list, zero candidates and the
empty-criterion branch's own *"NO CANDIDATE SEARCH WAS RUN FOR THIS SUBJECT"* text. **No STOP; the
subject tables for `l0-l1` were therefore filled by this batch as Task 4 orders.**

## Task 3 and Task 4 — what the extension is

`EXTRAS` is a fourth authored per-subject table, carrying an entry for **every** subject — an
empty list is authored, never left absent, and a subject missing from it STOPs the tool. Its
entries render **after** the ruled six. An extra is quoted from named **parts**, each naming one
source, the spans taken from it by the same four span kinds the ruled members use, and two
authored filters: **`removals`** (a passage by anchor text, deleted from the opening of the
delimiter pair it sits inside to that pair's close) and **`cuts`** (a section by what its heading
contains, deleted to the next heading at the same level).

**Both filters are verified in BOTH directions on every render, and either failing is a STOP:**
what was removed is absent from the rendered text, **and** re-inserting exactly what was removed
at the offsets it came from reproduces the source byte for byte — which is what proves nothing
else was taken out. **Neither marks its omission in place**, because the ruling's own verification
is that the rendered member equals its source with exactly the named spans deleted, and a mark is
an addition; what was cut is disclosed to the session in the read-me instead.

Three further STOPs were added: a subject with no `EXTRAS` entry; an anchor not matching exactly
once, a cut heading not matching exactly once or not terminated, or two filters overlapping; and
**the ruled six not standing intact, in their ruled order, at the head of a subject's rendered
members** — which makes Ruling 16's central protection mechanical rather than a promise.

`l0-l1` was added to all four tables with an **empty withheld family**, an **empty criterion** and
an **empty verdict table**. **One thing is recorded in the table itself rather than smoothed
over:** for `scoring-model` a ruling states in its own words that the unit is not held out and has
no oracle; **no ruling of 2026-08-31 says that of `l0-l1`.** What the record carries is Task 4's
order and the precedent it rests on, and that is exactly what the authored entry says — the ground
is DECLARED, not established (#24). Inventing a ruling to fill it would be the
defence-written-afterwards the never-work-from-memory rule forbids.

**`check_all` needed no edit, and that is a finding rather than an omission.** It ranges over the
rendered file map, which is the single place the extras are added to, so it covers them exactly as
it covers the six: the directory-listing comparison and the per-file byte comparison both see
them. Adding a second path would have put one concern in two places (#6).

## Task 5 — the three extras, and what was verified

**(a) The charter member.** `FRAMEWORK.md` §5 whole and §9 whole and nothing else, taken by
heading anchors. **Both ruled anchors matched EXACTLY ONCE** in the member's own source text —
each spans a line break in the file, so the match is whitespace-normalised, which is the
generator's own convention for a passage anchor. Each parenthetical was removed from its `*(` to
its `)*` inclusive, verified both ways. **Appendix A never enters, and no other section does.**

**(b) The five extracts.** They are the five the reading-progress table of
`reading_pass/candidacy_upgrades.md` names as the L1 slice, checked there at the file. **The cut
heading was found exactly once in each, and terminated at a `## ` heading in each** — two of the
five word it *"L1 or L2"* rather than *"L1"*, which is why the containment test is the right one.
Each cut verified both ways.

**(c) The ledger.** `EMPIRICAL_FINDINGS_LEDGER.md`, whole and unfiltered.

### ★ THE SWEEP — REPORTED, AND EVERY CANDIDATE LEFT IN PLACE

The dispatch orders a sweep of the member's source for any FURTHER passage describing what this
project currently has, and orders that a candidate not on the ruled list is a **STOP** and is
**not removed**. **Candidates were found. None was removed. The filter was not widened.**

**Genuine candidates, by the sweep's own stated test — a statement about this project's own
specifications, its record, its documents or its code:**

1. **§5, the second-axis parenthetical** — *"(This is adopted from this project's material; the
   first-stage draft had no second axis and placed phrase structure on the spine…)"*. Its second
   half is drafting history and out of scope; its **first half is not** — it tells the reader that
   this project's own material holds this decision, which is the same shape as the two ruled
   anchors and is why it is listed first.
2. **§9, DP-N's evidence sentence** — *"Our own two independent analyses of the same bar disagree
   — one writes `i6/4` and the other `Cad64`"*. It describes what this project's held annotation
   material contains. **Borderline against the stated test**, which names specifications, record,
   documents and code and not corpus material — and it is load-bearing EVIDENCE for the design
   point rather than provenance, so removing it would take a ground with it.
3. **§5 and §9, the two references to *the ledger*** — *"the ledger records what a grid does"* and
   *"the ledger's admitted facts are overwhelmingly…"*. Candidates by the letter of the test, since
   the ledger is this project's own record; **empty in substance**, because extra (c) puts that
   ledger in the pack whole, so nothing is disclosed that the pack does not carry.
4. **§9, DP-Q's *"the three exemplar analyses contain neither"*** — a statement about the
   ground-truth exemplars this project holds. Same class as 2.

**Examined and NOT candidates, because the dispatch excludes the framework's own drafting
history:** §5's 2026-08-31 correction block and §9's ground-2 narrowing block (both record how
this document was amended, naming the ruling and reading-pass records as the provenance of that
amendment); §5's onset/release correction note; §9's DP-M narrowing note; and §9's *"on this
project's own repertoire"*, which names the domain rather than the record.

**One further observation, not a filter candidate:** §5 and §9 as rendered carry cross-references
to §4.2, §7, §8.4, §11, R-1, the C-numbered ledger findings and Appendix A — none of which is in
the member. A deriving session will meet pointers it cannot follow. That is a consequence of the
ruled span choice, not of the filter.

### ★ WHAT THE FINDINGS SECTIONS CARRY — REPORTED AND NOT CUT

Ruling 11 Decision 2 cuts ONE named section; this batch did not widen it. Each of the five
extracts also carries a **★ Findings, routed and not applied** section, and the deriving session
will inherit all five. What they contain, so the user can see it before the pack is opened:

- **Verification verdicts against the charter's own sentences.** Three of the charter's `[FACT]`
  claims are checked at their primaries and confirmed — the cadence-cue paragraph in three
  separate places, the half-cadence F-measure pair, and L0's meter circularity — each stating *no
  correction is owed*. A session reading these learns that the charter it is deriving under has
  been verified at the object, which is a statement about this project's own record.
- **Addition candidates routed to the charter and not applied**, including a boundaries-given-
  versus-boundaries-found result on symbolic classical music offered as a stronger form of a
  chosen design point's ground, and a third independent statement on the half cadence.
- **Explicit register identities and apparatus names** — two `D-` identities, the framework's own
  risk items, the commission the extracts were written under, and the candidacy rows by number.
  These are the plainest disclosures of this project's own record in the five files.
- **Precisions a derivation should carry**, chiefly that the charter's *"two independent studies"*
  are independent in method and not in data, and that a bass-only cue can carry the wrong sign.
- **A ceiling caution repeated by four of the five**, that the annotation and not only the method
  bounds the measured figure.

**Also inherited, and worth seeing:** each extract's own header names the paper's PDF under
`docs/research_papers/` and cites its candidacy row — a `docs/` path of exactly the kind the
standing leak check strikes out of the generated members. The leak check is ruled over members (5)
and (6) only, so it does not reach an extra.

## Task 6 — ★ THE STOP, AND WHY NOTHING WAS WRITTEN

**The prediction HELD, and it was tested properly rather than at the disk.** A disk comparison
could not have answered it, because the packs on disk were already stale; a difference there would
have confounded source drift with the effect of the extension. So the **pre-batch generator and
the post-batch generator were both run over the same sources, in memory, writing nothing**, and
what each would render was compared. Every file of both existing packs is identical between them,
`MEMBERS` is unchanged, the ruled six stand at the head of every subject in their ruled order, and
the post manifest with the new subject removed is byte-identical to the pre manifest. All of it is
at the artifact.

**THE START-STATE STOP.** `--check` was **already red before this batch touched anything**. Four
files do not re-render — members (2) and (4) of BOTH existing packs — because `CLAUDE.md` and
`cowork_audit_protocol.md` have grown since those packs were last rendered. **This was established
without the generator in the argument at all:** at commit `f54995c092` both the sources and the
pack files are tracked and were unmodified in the working tree, so both are at that commit; their
content was taken with `git show`, the ruled spans re-cut by the same rule the tool applies, and
compared with the pack file at the same commit. They differ, and the drift is **addition-only** in
both.

**The consequence, and it is not a matter of judgment.** Task 6's three conditions cannot all hold
from this start state: `--check` GREEN requires the two existing packs to be re-rendered from the
grown sources, and *byte-identical to their pre-batch state* forbids exactly that. **§4 settles
it** — *a difference anywhere in either existing pack is a STOP, not a thing to explain
afterwards* — so the STOP fires BEFORE the write, which is why the pre-batch state was pinned
first. And no partial route existed: `write_all` writes the manifest for every subject on any
invocation, so even `--subject l0-l1` would have moved the two existing subjects' manifest
entries, which the same task forbids in terms.

**Beyond the dispatch's own bar, the act was the user's in any case.** Refreshing those two packs
changes what a future blind deriving session reads — a behaviour change on a ratified surface,
ratification-gated under #14 — and this batch repairs nothing it finds.

**Proven by re-hash after every act of this batch: every one of the fifteen pack and manifest
files still carries its pre-batch blob.** Nothing was written to either existing pack, to
`tools/audit/derivation_boot_pack/l0-l1/`, or to `tools/audit/derivation_boot_pack.json`.

**What the extended tool WOULD render, measured in memory and reported so the user can rule on it
with the facts in hand:** the `l0-l1` pack comes to ten files — the read-me, the ruled six, and
the three extras at 7, 8 and 9. Its read-me renders *"The nine files of this pack, in order"*,
lists all nine, and its what-was-cut section states truthfully that two passages were taken out of
the charter member and five whole sections out of the extracts member, deleted with no mark. Both
anchors and all five cut headings resolved uniquely, and every filter passed its both-ways
verification.

### Four residuals the extension causes and this batch did NOT repair

1. **`the_pack_files_in_order`** in the manifest names the ruled six and the read-me and does not
   name any subject's extras. **This is Ruling 16's own finding (2)**, and repairing it is
   forbidden by Task 6's requirement that the manifest change only by the added subject — every
   such field is global. A subject's actual file list is at its own `the_members_as_rendered`.
2. **`the_rulings_it_executes`**, **`the_STOPS`** and **`what_is_AUTHORED`** in the manifest
   likewise still describe the pre-extension tool, for the same reason and with the same bar.
3. **The read-me's stop-and-record clause still reads *"including one of these six"***. The
   dispatch orders that clause untouched **in terms**. It is not false — the rule it states binds
   *"in any file"*, and the phrase is an inclusive example — but it names six of nine.
4. **All four are recorded inside the generator's own module docstring**, so a reader of the tool
   meets them where the tool is, and none of them can be mistaken for completeness.

The module docstring WAS updated to describe the extras dimension and its STOPs; a docstring is
not rendered into any artifact, so it moves nothing.

### One thing changed beyond the letter of §5's named defect, declared rather than slipped in

§5 names one prose defect the extension must fix, the read-me's hard-coded count. The extension
causes a **second** one in the same file: `render_what_was_cut` derives its text from the withheld
family alone, so a subject with an empty family but a filtered extra would have told its session
*"Nothing has been withheld from this pack for this subject"* while three of its nine members had
material deleted out of them **silently**. That is the exact falsity the licensed accommodation
already recorded in that function was written to remove, in the same section, and it would land in
the FIRST thing a blind deriving session reads. **The extras' filtering is therefore derived into
that section from the counts, exactly as the other two kinds are, and not switched on a subject
name; a subject whose extras are empty renders byte-identically to before.** The opening sentence
is derived too, because *"so that what you derive can be compared against a ruled answer you have
not read"* is false where nothing is held out. **The alternative — leave it and STOP-report the
falsity — was available and is recorded here so the user can take it instead.** The boundary
clause and the stop-and-record clause are untouched, as ordered.

## Task 7 — the Corelli claim, checked at the file

**`tools/dcml/corelli/MS3/op01n08a.mscx` DOES exhibit staggered entries.** Sixteen bars, 4/4, two
flats, four staves. **Nothing was staged.**

**What was read.** In **bar 1** the first staff enters on beat 1 with C5 held two beats; the second
staff **rests a quarter** and enters on beat 2 with the **same pitch**, C5, also held two beats,
releasing on beat 4 — an imitative entry at the unison displaced by one quarter. The two parts'
onsets (beats 1 and 3 against beats 2 and 4) and releases (beats 3 and 5 against 4 and 5) do not
coincide anywhere in the bar. **Bar 5, after the mid-piece fermata, repeats the shape exactly**:
first staff G5 across beats 1–2, second staff a quarter rest then G5 across beats 2–3, then F♯5 on
beat 4.

**Releases falling away from onsets, at three densities.** In **bar 4** all four staves sound a
half note under a fermata and then a **half rest** — every part releases at beat 3 and nothing
begins: a change point produced by releases alone, and real silence. In **bar 8** the second staff
and the third release at beat 3 into half rests while the first staff takes a new onset there and
the fourth sounds a new half note — three different treatments of one instant. In **bar 9** the
third staff opens with a half rest under sounding upper parts.

**Two facts a stager needs, found in the same reading.**

- **The two bass-clef staves are not a duplicate pair, and they diverge.** Staff 3 carries the
  DCML Roman-numeral annotations, staff 4 the original figured bass, and they double each other
  until **bar 8, where staff 3 rests through the second half while staff 4 sounds F♯3** — which is
  consistent with Corelli's own scoring of this set for two violins, violone, and organ bass, two
  bass parts that mostly double and occasionally do not. So the file's four staves are four real
  parts, not three parts and an annotation carrier.
- **The instrument labels are mismatched to the staff contents.** Part 1 owns staff 1 and is named
  *organ*; part 2 owns staff 2 and is named *cello*; parts 3 and 4 own the two staves that carry
  `<defaultClef>F</defaultClef>` and are both named *violn*. The pitch content says the opposite —
  staves 1 and 2 are the upper parts, staves 3 and 4 the bass. **A session told that voice
  membership is given would meet a file whose part NAMES are wrong**, which bears directly on L0's
  contract and on the phenomenon Ruling 15 names for the keyboard-or-orchestral slot.

**The qualification, stated because the claim it supports is a spanning claim.** This piece
delivers *staggered entries* plainly and twice. It delivers *the release case at real density*
**weakly**: the entries are offset by a quarter, so most releases still land on some other part's
onset, and the release-only change points here are the general rest at bar 4 and the one-part
rests at bars 8 and 9. If the staged set is meant to exercise release-driven change points at
density, this piece is not by itself that exemplar.

## The footprint, as it actually stands

**Created:** `tools/audit/l0l1_boot_pack_extension.json` — this batch's artifact — and this
report. **The artifact's name is NOT in §11's Created list**, which names only the pack directory
and the report; it is created under Task 2's own order to state the prediction *"in the artifact
and in the report"*, §11's heading being that the footprint is enumerated from this batch's own
orders. The divergence is reported here and on the artifact's own face rather than absorbed.

**Edited:** `tools/audit/gen_derivation_boot_pack.py` only.

**NOT created:** `tools/audit/derivation_boot_pack/l0-l1/` and its files — the STOP above.
**NOT edited:** `tools/audit/derivation_boot_pack.json`, and no other tool source; the forward
bound's own per-batch re-aiming was not needed and was not run.

**Read and never written:** `FRAMEWORK.md`, the five extracts, `EMPIRICAL_FINDINGS_LEDGER.md`,
`reading_pass/candidacy_upgrades.md`, `tools/dcml/corelli/MS3/op01n08a.mscx`. **`FRAMEWORK.md` is
not amended.**

**Not done at all:** no build, no test, no golden, no measurement of the analysis, nothing under
`tools/corpus/` or `tools/robust_stop/`, nothing under `src/` or `docs/`; no governing document
amended; **no open-items row created, flipped or discarded**; no decisions-register entry and no
`D-NNN`; the workbook not opened; no score staged; no brief written; no session booted.

**The pins.** This file and every file §0 names were pinned to git blobs before any other act and
**re-hashed at the close: all seven reproduce exactly.** No read disagreed with its pin.

**The tracked-modification assumption.** The session-start snapshot the harness supplied showed
exactly one tracked modification — `cowork_rulings_2026_08_31_decision_surface_sitting.md`, the
named known exception — and no other. **That bound is DECLARED from that snapshot, not established
by a shell `git status`, which the standing rule forbids** (#24: where a condition cannot be
established at an inspectable object the session may reach, it is declared and the result stands
with the bound attached).

## The self-check

The diff of the one edited file was read blob-to-blob by explicit hash, not from memory of writing
it. It is **471 insertions and 11 deletions**, and every one of the eleven deletions is accounted
for: the docstring's STOP-8 terminal punctuation; the two changed function signatures and the two
changed call sites; the hard-coded `lead`; the two hard-coded opening lines of the what-was-cut
section; the read-me's hard-coded heading; the listing built from the global `MEMBERS`; and **one
dead local** in `render_read_me` that named the pack's file list as read-me-plus-`MEMBERS` — dead
before this batch, and false for a subject with extras had it been left. **No ruled member, no
`MEMBERS` entry, no existing subject's authored table, no STOP, no leak-check line, and nothing in
`write_all` or `check_all` was removed or altered.**

Checked against the principles: **#6** — `check_all` gained no second path, the extras being
covered by the one file map it already ranges over, and the read-me's derived count replaced a
literal rather than adding a second statement of it. **#12** — the filters delete and never
rewrite, and what each removed is carried on the manifest record beside it. **#17(b)** — the
prediction preceded the act. **#17(f)/D-431** — no figure is transcribed into this report; each is
at the artifact. **#19** — the both-ways verification is a mechanism whose output is inspectable,
not a session's assurance. **#13** — the start-state staleness was surfaced as a STOP before
anything was built around it. **DEFECT_TYPES.md** — the scope of the sweep, of the leak check and
of the extras' verification is stated on each rather than left to read as total (DT-26).

## Done, on the ruled stop form

**DONE.** The §0 read and the pins. The generator established at the file, including the
`scoring-model` precedent Ruling 16 rests on. The prediction, written first. The generator
extended additively and per-subject, with the ruled six protected by a mechanical STOP, the
read-me's count derived, and `l0-l1` added to all four authored tables. The three extras defined
and their filters verified in both directions. The sweep run and every candidate reported. The
prediction proven, pre-generator against post-generator at the same sources. Task 7's Corelli
finding established at the file.

**NOT DONE.** The render. `--check` is not green and cannot be from this start state. The pack
directory `tools/audit/derivation_boot_pack/l0-l1/` does not exist, and `derivation_boot_pack.json`
does not carry the new subject. **`--check` now reports one more line than it did before this batch
— the missing `l0-l1` directory — and the five pre-existing lines are unchanged: the manifest, and
members (2) and (4) of both existing packs.**

**THE REMAINDER IS UNTOUCHED.** Both existing packs and the manifest stand at their pre-batch
blobs, proven by re-hash. `FRAMEWORK.md`, the extracts, the ledger and the Corelli score were read
and not written. Nothing was staged, no brief was written, and no session was booted.

**What the user is owed a ruling on, in the order it blocks work:** whether the two existing packs
may be re-rendered from the grown `CLAUDE.md` and `cowork_audit_protocol.md` — which unblocks the
render and is a behaviour change on a ratified surface; whether the sweep's candidates widen
Ruling 11's filter; and whether the four manifest and read-me residuals are repaired, which
requires relaxing the manifest's byte-comparison bar.

---

*Provenance: CC, 2026-08-31, under `cc_instruction_l0l1_boot_pack_2026_08_31.md`. Every working-tree
read through the file tools; shell used only for git object queries by explicit hash, for
`git hash-object`, and for running the generator and the two scratchpad drivers. The artifact is
`tools/audit/l0l1_boot_pack_extension.json`; no figure of it is restated here (#17f, D-431).*
