# Cowork handoff entry 220 — 2026-09-20

**The current entry point.** Entry 219 is superseded as entry point and stands otherwise. Grades as in
entries 210 and 219: **[checked]** = opened or measured at the file by this sitting; **[relayed]** = not.

## 0. State at close

- **Nothing is running. No dispatch is out. Nothing awaits the user.** Two rulings were taken this
  sitting and both are recorded at §3; neither has been executed.
- **Both ref files read `d42fa5604538ece1abadcada6437415e67a81dbd` [checked]** — `.git/refs/heads/master`
  at modification time 1789922733029, `.git/refs/remotes/origin/master` at 1789922879696. Both values
  and both times are what entry 219 §0 records, so nothing has been committed to either ref since that
  entry closed. **No commit to git by this side.**
- **Uncommitted on the user's disk**, as entry 219 §0 records and this sitting did not change: the third
  close's report (26,585 bytes **[checked]**), entry 219 (18,120 **[checked]**), and
  `tools/audit/claude_md_finer_archive.json`, whose modification's cause is still established by nobody
  this side has read. This entry joins them.

## 1. What this sitting did

1. **Boot**, per entry 219 §5, in its order. **The device-info call WAS made first, before the
   folder-access request**, which is what that section puts at its head. `C:\s` was listed names-only to
   confirm `MS` before the request; **no repository root was listed**. Entry 219 was **18,120 bytes at
   the listing of `records/cowork/handoff/`** — the size the opening instruction gave, **read at the
   listing rather than taken** — and was read whole, §6 included. The close dispatch read **28,997 bytes
   at modification time 1789921234545**, unchanged from what entry 219 §2 measured after CC's run, and
   the close's report **26,585 bytes**. All **[checked]**.
2. **§7 item 1 — the failing boot-pack check — its cause is ESTABLISHED** (§2). No repair was taken and
   nothing about the tool, the manifest or any pack was touched.
3. **The user ruled twice on what follows from it** (§3), and the design those rulings settle is at §4.

## 2. The cause of the failing check, established at the objects

**What the check is.** `tools/audit/gen_derivation_boot_pack.py --check` has two limbs **[checked at
`check_all` and `verify_frozen`]** *(★ CORRECTED AT THE CHECK, §9. FORMER: "at `check_all`,
`verify_frozen` and `write_all`" — `write_all` carries nothing about `--check`.)*. It rebuilds the manifest —
`tools/audit/derivation_boot_pack.json`, the record file that describes the three boot-pack directories
and is part of none of them — and compares it byte for byte with the manifest on disk; a difference is a
drift line and exit 1. And for each frozen subject it verifies that the pack directory holds exactly the
recorded files and that each hashes to its recorded blob; a mismatch there raises a `STOP:` line instead
of joining the drift list.

**All three subjects are frozen** — `harmony-boundary` and `scoring-model` on 2026-08-31, `l0-l1` on
2026-09-04 **[checked at the `FROZEN` table]**. So the per-subject re-rendering comparison ranges over
nothing, no pack file is compared as text, and **the only drift line that can fire is the manifest's**.

**Why the manifest drifts.** The tool builds every subject in full on every run, frozen or not, and only
afterwards skips the frozen directories **[checked at `build_subject`, `check_all` and `write_all`, and
at the recorded PASS output in `guard_state.json`, which names all three subjects as frozen and
verified — `build()` itself was NOT read]**. So the manifest's
records for a frozen subject are built from the sources as they stand today; the tool says so in its own
words at `frozen_block`, adding that where a member's sources have grown those records describe what
WOULD be rendered and not what the directory holds, the digests being the authority on that.

**The three sources that moved.** Member (8) of the `l0-l1` pack is rendered from five reading-pass
extracts. Against the manifest's recorded `lines_rendered` for each, the files as they now stand
**[checked, line counts taken over the staged copies]**:

| extract | the manifest records | on disk now | modification time |
|---|---|---|---|
| pardo-birmingham 2002 | 415 | 415 | 1789869879031 |
| temperley-sleator 1999 | 261 | **309** | 1789893141045 |
| bigo-feisthauer et al. 2018 | 192 | **225** | 1789894269069 |
| karystinaios-widmer 2022 | 200 | **280** | 1789897690140 |
| sears et al. 2018 | 238 | 238 | 1788188373332 |

The manifest was last written at **1789890832910**. The three that differ were edited after it; the two
that match were not — pardo-birmingham was edited earlier the same day and sears not since 2026-09-04.
**The two exact matches are the evidence that the counting used here agrees with the generator's own ON
THESE FILES** *(★ CORRECTED AT THE CHECK, §9. FORMER: "are also what establishes that the counting used
here agrees with the generator's own" — two agreements are evidence, not establishment.)* Four of the five carry
text dated 2026-09-20 **[checked by search]**; **which sitting made each edit is NOT established here** —
entries 211 to 216 were not read.

**The failure is a RECURRENCE and was established once already today.** The second framework DP-C
correction batch met the same red at its own start, traced it to one reading-pass extract edited earlier
that day, regenerated the manifest as a commit of its own — `f1119a772e63e0144dd06b26739007ee3bb8454f` —
and recorded `--check` printing green twice afterwards **[relayed, at that batch's report §2, §3(d) and
§3(c)]**. **It went red again about 38 minutes after that regeneration**, at the first of the three
further extract corrections; the second came about 57 minutes after it and the third about an hour and
fifty-four minutes after it, each figure the difference of the modification times above **[checked]**.
*(★ CORRECTED AT THE CHECK, §9. FORMER: "It went red again within the hour as three more extracts were
corrected" — true of the first correction only.)* **So what entry 219 §7 item 1 carries as a cause
nobody established — itself carried from entry 218 §3 item 2 [relayed, entry 218 not read] — is the
recurrence, not a new defect.**

**The freeze is not implicated by anything read.** The three directories hold exactly the file names the
freeze records, and **every file in them carries a modification time PREDATING its subject's freeze
date** — the two 2026-08-31 subjects at 1787909395781–788 and `l0-l1` at 1788246453080–084, none of
them touched since **[checked at a recursive listing]**. A frozen mismatch prints `STOP:` rather than a drift line
**[checked at the code]**, and the captured output of the failure was the single manifest drift line
**[relayed]**. **That all twenty-four pack files re-hash to their pins is [relayed]** — a blob hash
cannot be computed without a shell.

## 3. The two rulings taken this sitting

**RULING 1 followed the decision-surface form:** the whole self-contained surface in a turn of its own,
the choice question in a separate later turn. **RULING 2 DID NOT, and the departure is declared here:**
its question stood at the foot of the message that carried the design, not in a turn of its own.
*(★ ADDED AT THE CHECK, §9. The former sentence — "The alternatives were delivered as a self-contained
surface in a turn of its own, the choice question in a later turn, one decision at a time" — was true of
Ruling 1 and untrue of Ruling 2.)* The user's words, verbatim: **"C it is then."** and **"I'll go with
your recommendation"**.

**RULING 1 — option C: for a frozen subject the manifest describes the directory, not a re-render.** The
ground the user was given: with every subject spent, the only thing this check can report is a staleness
that says nothing about any pack, and a guard whose red is routine cannot carry the one signal that
reaches the objective — that a frozen pack, the record of what a completed derivation was given, has been
altered. The alternatives put beside it were leaving the arrangement as it is, adding a
regenerate-the-manifest step to every batch that edits a source, and standing the guard down; the last
was stated to carry the freeze's own hash check down with it.

**RULING 2 — the drift stays, printed and uncompared.** The records built from today's sources are kept,
computed exactly as they are computed now, printed as an ordinary line of the check's output, and
excluded from what the check compares, so they never set the exit code.

**★ THIS SIDE GAVE RECOMMENDATIONS, AND THAT IS A DEPARTURE FROM D-658**, which says a surface returning
an unsettled question to the user gathers facts and makes no recommendation. Both surfaces were first
delivered without one; the user then asked for a recommendation on each. The same shape entry 186 head
(3) records for 2026-09-16.

**Neither ruling is in the decisions register.** Rule (c) wants a register entry in the commit that
records a ruling; the route where that register cannot take one is
`cowork_register_rule_c_suspension_2026_08_28.md` **[relayed, from the 2026-08-31 rulings record's
Ruling 17 note, read this sitting]**. Not taken here.

## 4. The design as settled — what the dispatch must execute

1. **For a subject in `FROZEN` the manifest carries**: the authored structure unchanged (which source
   each file came from, which spans and anchors, what was cut and why — all constants of the tool); the
   freeze block with its digests; and measured fields taken from the frozen files on disk rather than
   from the re-render. A frozen subject's entry would then depend on the tool's own constants and on the
   pack files alone. **That it re-derives stably is the design's INTENT and is proved by the dispatch
   that builds it, not here** *(★ CORRECTED AT THE CHECK, §9. FORMER: "and re-derives stably" — stated
   of a thing not yet built.)*.
2. **Frozen subjects go on being BUILT.** The tool's own STOPs — an anchor no longer found exactly once,
   a withheld passage that no longer matches, a verdict left unpaired — run because every subject is
   built, and stopping that would leave the tool checking almost nothing while all three subjects are
   spent. This is why Ruling 2's form costs nearly nothing: nothing is removed from the build path.
3. **The drift is printed at `--check` and excluded from the comparison.**
4. **Any batch condition over this guard is written on the VERDICT and never on the output text.** The
   printed drift line moves whenever a source moves, so an equality condition over output would stop a
   batch for a green guard. **The near case is the third backup's first close, whose guard step required
   every guard's RESULT to equal the opening capture's and stopped when two flipped FAIL to PASS
   [checked at `STATUS.md`]** — an equality condition of the same family, over verdicts rather than over
   output text *(★ CORRECTED AT THE CHECK, §9. FORMER: "the shape the third backup's first close already
   stopped on" — that close's condition was over verdicts, and the sentence read as though it were the
   same condition.)*.
5. **NOT decided here, and the dispatch's own design**: the exact field names, and whether the per-span
   measured fields are omitted for a frozen subject or measured from the rendered file. Neither is
   settled by anything read.

## 5. Boot order for the next session

1. **THE DEVICE-INFO CALL FIRST**, before any folder-access request. File tools only; no shell in the
   container or on the device; **list no repository root.**
2. The ordinary session-start read (entry 186's Boot block: `CLAUDE.md` at its six spans, the membership
   read at that file's own "Build and test commands" block; `DECISIONS.md` whole; `STATUS.md`; the gating
   answer's identity list), entry 118's bridge-fault section, entry 152's (v)–(x), entry 169 whole.
   **Then this entry whole.** Read entry 219 at its §2, §4 and §7, and entry 218 only where entry 219
   points into it.
3. **Read both ref files. They should BOTH read `d42fa5604538ece1abadcada6437415e67a81dbd`.** If either
   has moved, find out what ran before anything else. An unmoved ref establishes that nothing has been
   committed to that ref, and nothing more.
4. Verify at listings: this entry (the size in the opening instruction) at `records/cowork/handoff/`; the
   close dispatch (28,997 bytes) at `records/cc/instructions/`; the close's report (26,585 bytes) at
   `records/cc/reports/`. **`records/cc/instructions/`'s listing exceeds the tool's inline limit** — the
   tool saves it to a file and it is searched with `Grep`, not read whole.
5. Then §6 in order.

## 6. What comes next, in this order

1. **Write the dispatch that executes §4. It is the next act, and it is the head of this list.** It
   changes one file, `tools/audit/gen_derivation_boot_pack.py`, and regenerates the manifest once. **It
   writes into no pack directory, and cannot**: write mode skips every subject in `FROZEN` before it
   creates a directory or writes a file, and all three are frozen **[checked at `write_all`]**. The
   dispatch is source-checked at the objects before the user runs it.
2. **The close's report, entry 219 and this entry are uncommitted.** The next batch that closes commits
   them.
3. Carried from entry 219 §7 item 3, unchanged: the one-word *figure* → *value* fix in `FRAMEWORK.md`;
   §14.1's uncorrected restatement; the unknown cause of `tools/audit/claude_md_finer_archive.json`'s
   modification; then steps 3 and 4 of the plan in entry 169 §2.
4. Open, not decided: whether row 8's second extract is renamed (entry 215 §3 item 3).

## 7. Declared departures, and this side's own state

- **NO SHELL COMMAND WAS RUN**, in the container or on the device. **No repository path was read or
  written through a shell on either machine.** No WebSearch, WebFetch, subagent, popup or task list.
  **No commit to git by this side.**
- **Directories listed:** `C:\s` (a names-only skeleton, to confirm `MS` before the access request);
  `records/cowork/handoff/`; `records/cc/reports/`; `records/cc/instructions/` (the result exceeded the
  tool's inline limit, was saved to a file by the tool and was searched with `Grep`, not read whole —
  the same departure entries 218 and 219 declare for that directory); `tools/audit/`;
  `tools/audit/derivation_boot_pack/` (recursively). **No repository-root listing.**
- **The user's Cowork memory store was NOT read and NOT written to** by any memory tool call.
- **Read whole:** entries 219, 186, 169; `DECISIONS.md` (862 lines, **three calls** — *★ CORRECTED AT
  THE CHECK, §9. FORMER: "two calls".*); `STATUS.md`.
- **Read at sections:** `CLAUDE.md` at its six ruled spans, located by a heading search; the gating
  answer at its counts fields (222 gating, 25 non-gating, 247 open) and through its identity list, which
  holds 222 entries; entry 118 at its bridge-fault section; entry 152 at (v)–(x);
  `tools/audit/gen_derivation_boot_pack.py` at its header STOP list, `MEMBERS`, the `FROZEN` table,
  member (8)'s extras, `build_subject`'s render loop, `read_text`, `check_all`, `verify_frozen`,
  `frozen_block`, `write_all` and `main`; `tools/audit/derivation_boot_pack.json` at its head and at
  member (8)'s five part records; `tools/audit/guard_state.json` at this tool's own entry, which records
  it **PASSING**, in an artifact whose own modification time is 1788906367566 — the date is that
  artifact's, not a field of the entry, which was not read *(★ NARROWED AT THE CHECK, §9. FORMER:
  "which records it PASSING on 2026-09-08".)*; `records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`
  at Ruling 17 whole; the third close's report and the second DP-C correction report by search.
- **Measured rather than read:** the five reading-pass extracts, by line count and by a search for
  today's date; their contents were not read.
- **Staged but NOT opened:** `FRAMEWORK.md`, `DEFECT_TYPES.md`, `EMPIRICAL_FINDINGS_LEDGER.md`,
  `cowork_audit_protocol.md`, `cowork_design_doc_template.md`, the phase-definition surface — staged to
  establish that each member source is where the tool names it and to read its modification time.
- **NOT read at all:** `OPEN_ITEMS.md`; `ARCHITECTURE.md`; entries 211 to 218; every paper; every other
  extract; every rulings record but the one named.
- **Landed:** this entry, by container path through the bridge.
- **Degradation, as the standing rule asks. One shape of this side's is named rather than counted:** the
  drift sub-question was put to the user as a binary — keep it behind a new mode, or drop it — and
  reading the build path afterwards showed a third form that costs less than either. That is a bar
  written by this side and answered by the objects, which the user's ruling of 2026-08-28 names. It was
  corrected before the choice was taken, in the turn that recommended. Otherwise this sitting's claims
  rest on objects it opened, and no second tell was found. **The judgment: close here.** The dispatch at
  §6 item 1 is precise writing with its own start-state conditions and wants a session that has not
  spent its capacity on a boot and an establishment.

## 8. Landing

Written in the container's outputs folder and committed to
`C:\s\MS\records\cowork\handoff\cowork_handoff_entry_two_hundred_and_twenty.md`. Its closing size is in
the closing report and in the phrase for the next session's opening instruction. **It is uncommitted to
git, as §6 item 2 records.**

**Whether it came in under entry 219's 18,120 bytes, against cadence 12, is stated in that closing
report from the measured size and is not predicted here** — entry 219 §10 records a first writing that
predicted it and was made false by its own landing.

**★ MEASURED, AND IT DID NOT.** At the staging call taken before this paragraph was added the entry
stood at **20,366 bytes, against entry 219's 18,120 — over by 2,246.** Its first landing, before the
check at §9, was **15,479**, so **the whole of the overshoot is the check apparatus and the corrections
it ordered**, not new work. **This is the THIRD consecutive entry to come in above the one before it**,
entry 219 §10 having recorded the second and said that two in a row is the point at which the trend is
worth saying out loud rather than noting per entry. **A next side should read it as the trend and not as
this entry's own defect**, and the final figure is in the closing report, this paragraph having moved it
again.

## 9. ★ The user-ordered fact- and source-check, written in the act that ran it

**This entry was re-read WHOLE as first landed — 15,479 bytes at the staging call — at the device's own
copy staged back**, and each claim was checked against the object it rests on, on the four axes of the
user's rule of 2026-09-12: completeness, coherence, correctness, and misuse of absolutes. **It did not
come back empty.** Every correction is at its site with the former wording preserved (#12). Named rather
than counted:

- **A false statement about this side's own conduct**, and the one that matters most: §3 said both
  rulings were taken with the choice question in a turn of its own. **That is true of Ruling 1 and
  untrue of Ruling 2**, whose question stood at the foot of the design message. Declared at §3.
- **A time claim true of one case and written over three:** *"within the hour"* at §2, now three
  measured figures.
- **Two citations naming objects that do not carry the claim:** `write_all` for what `--check` does, and
  `build()` named as read when it was not — the build-every-subject claim now cites what was actually
  opened.
- **An establishment claim where the evidence is two cases:** the line-count agreement at §2.
- **A property asserted of a design not yet built:** *"re-derives stably"* at §4 item 1.
- **A near case written as the same case:** the third backup's first close at §4 item 4 stopped on an
  equality over VERDICTS, not over output text.
- **A count of this side's own calls, wrong:** `DECISIONS.md` was read in three calls, not two.
- **A date attributed to a record that does not carry it:** the boot-pack guard's PASS in
  `guard_state.json`, now cited to that artifact's modification time.

**What the check CONFIRMED at its objects and did not strike:** both ref values and both modification
times against entry 219 §0; the three boot sizes; the five extracts' recorded and current line counts
and their modification times; the manifest's own last write time; the pack directories' file names and
modification times; the `FROZEN` table's three subjects and their freeze dates; and the quoted verbatim
words of both rulings against this conversation.

**What it did NOT do.** It opened no object this sitting had not already opened, read no entry between
211 and 218, computed no blob hash, and re-read neither CC report whole. **Nothing here says a further
pass would come back empty.**
