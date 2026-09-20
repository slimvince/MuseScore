# The `cowork_handoff.md` prepend — report (CC, 2026-09-01)

> **STATUS: CLOSED ON THE RULED STOP FORM.** Executes
> `cc_instruction_handoff_prepend_2026_09_01.md` whole.
>
> **Outcome:** one commit exists, `4c9b7af5066fdf51e4b726f6fdc151b7e4153b0c`, carrying exactly
> the four paths §3 authorises and nothing else. `cowork_handoff.md` now runs 88, 87, 86, 85, 84,
> 83, 82, 81, 80 and downward. **No entry's content was changed by this batch** — every one of the
> seven spans now inside the file was located by searching for its own source file's bytes and its
> `sha256` shown equal to that file's, the file grew by exactly the seven files' combined size with
> no join byte added or removed, and every pre-existing byte is proven present, in order and
> unsplit, against the original blob fetched from git by explicit hash. Nothing was pushed,
> amended, squashed, rebased or tagged.
>
> **No STOP of §6 fired.** One thing §6 classes as *reported rather than resolved* was met — the
> standing shell-read guard refusing a command — and is reported at §6.
>
> **★ ONE FINDING IS SURFACED, NOT REPAIRED.** The join rule the dispatch mandates preserves each
> entry file's bytes exactly, and six of the seven entry files end with a single newline rather
> than a blank line. So **six of the twenty-four entry boundaries in the resulting file carry no
> blank line before their `---` separator**, where all seventeen pre-existing boundaries do.
> Repairing it would mean adding bytes no source file holds, which §2 forbids in terms. Measured at
> every boundary, not sampled: §5.

---

## 0. Boot — what was read, and one difference between the dispatch and `CLAUDE.md`

Performed before any other act. A single-file opening instruction is not an exemption (ratified
2026-08-29, P-1), so the ordinary session-start read ran in full first.

- `CLAUDE.md` — whole.
- `DECISIONS.md` — whole (the INDEX preamble, the *How to read an entry* block, the status-words
  and terms tables, the counted-content and scope blocks, groups A…U, and the provenance block).
- `STATUS.md` — whole.
- The derived gating answer — `tools/audit/nongating_apparatus_rows.json`, read at the artifact
  (`★_the_live_gating_answer`, its establishment block, its ruled default, and `gating_ids`).
  **This batch opens no stage**, so no gating identity is consumed by any act below.
- `CLAUDE.md`'s commit rules and the dispatch protocol's — the latter read whole, from the heading
  *The dispatch protocol these audits are commissioned and run under* to the end of the file,
  every standing clause and the four ratified 2026-08-29 clauses included.
- `cowork_handoff_entry_eighty_eight.md` — whole.
- `cc_instruction_handoff_prepend_2026_09_01.md` — whole.

**The other six entry files were NOT read for their content**, as §0 directs. Their bytes were read
by machine and written; nothing in this batch depends on what they say.

### The one difference between this dispatch and `CLAUDE.md`, reported under §0.3

**`BUILD_AND_TEST.md`: the dispatch declares its condition MET; checked at `CLAUDE.md`'s own
wording, it is NOT.** `CLAUDE.md` makes that file mandatory for *"a session that builds, tests, or
runs a measurement tool **whose command lives there**"*. This batch builds nothing and tests
nothing. It ran three scripts written for it, which live in this session's scratchpad outside the
repository, and one repository tool, `tools/audit/changed_paths.py` — and `BUILD_AND_TEST.md` was
searched at the file for that tool and for every other command this batch ran: **no occurrence**
(Grep over `BUILD_AND_TEST.md` for `changed_paths`, `hash-object`, `prepend` — zero matches). The
condition is therefore unmet by the governing wording.

**I read `BUILD_AND_TEST.md` whole regardless**, because the dispatch ordered it and reading costs
nothing. §0.3 says where the two differ, `CLAUDE.md` wins and the difference is reported: it is
reported here, and the difference changed no act of this batch.

---

## 1. Task 0 and Task 1 — the pins, and the pre-state

### 1.1 The pins, and the declared departure

**The declared-departure route applies and is declared** (the standing clause ratified 2026-08-29,
P-2). The user's opening line named only the dispatch file, so the dispatch was read from the
working tree before it was pinned; the pin was then taken at Task 0 and **the blob is proven
unmoved before staging** at §1.4.

Fifteen files pinned with `git hash-object -w` — the dispatch, every file §0 names, `cowork_handoff.md`,
and each of the seven entry files. **All fifteen exist**; none was missing under the spelling §1
names.

| File | Blob at Task 0 |
|---|---|
| `cc_instruction_handoff_prepend_2026_09_01.md` | `9a2610b87576f24d1332277da4376840a25d690b` |
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` |
| `DECISIONS.md` | `238cff78e61d4ff4cd8e5a41dc17f6fab4ab7d59` |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` |
| `cowork_audit_protocol.md` | `052e8e5fb9ef335b469443ddeca65b372ed5254d` |
| `tools/audit/nongating_apparatus_rows.json` | `a2ca9f64783d45a50bd3fb299d46afe46b9fe678` |
| `cowork_handoff.md` | `4f7056c362990cfffa5bb03038f1fce1edcfe968` |
| `cowork_handoff_entry_eighty_two.md` | `343d303d2428dd0a0e412e1eb8a42d26ae68a6fb` |
| `cowork_handoff_entry_eighty_three.md` | `b4a2c892dd60194981c5bad42010211c7264edbc` |
| `cowork_handoff_entry_eighty_four.md` | `5fdf7ecab61cfc51fe6c999754f0aabfa18a5962` |
| `cowork_handoff_entry_eighty_five.md` | `94d356c5cec545b17c5649192d75dd112a29ddb2` |
| `cowork_handoff_entry_eighty_six.md` | `32b479fc5c8d9b0318165aba0c8faef8fb7e8c51` |
| `cowork_handoff_entry_eighty_seven.md` | `f89105ef65df14d07f35f13d8b71f854b3581877` |
| `cowork_handoff_entry_eighty_eight.md` | `ce544685c8f72bfc2306407aab821184c5b85907` |

**No read disagreed with its pin.** The strongest evidence is not a re-hash of my own reading but
an independent one: for the five of these files that are tracked and unmodified, git's own tree at
`98f53aaa723b143dc557ea7785b9d39d112cd114` carries **exactly the blob each pin names** (§1.3). What
I read and what git holds are the same bytes, established at the object rather than asserted.

### 1.2 `cowork_handoff.md`'s entry order before the act

Read at the file with Grep over `^## COWORK SESSION CLOSE \([A-Z-]+ ENTRY`. **Seventeen headings,
top to bottom:**

| Line | Ordinal | | Line | Ordinal |
|---:|---|---|---:|---|
| 4 | EIGHTY-FIRST | | 2223 | SEVENTY-FIRST |
| 216 | EIGHTIETH | | 2378 | SEVENTIETH |
| 834 | SEVENTY-NINTH | | 2550 | SIXTY-NINTH |
| 1031 | SEVENTY-EIGHTH | | 2664 | SIXTY-EIGHTH |
| 1195 | SEVENTY-SEVENTH | | 2811 | SIXTY-SEVENTH |
| 1343 | SEVENTY-SIXTH | | 2984 | SIXTY-SIXTH |
| 1556 | SEVENTY-FIFTH | | 3283 | SIXTY-FIFTH |
| 1715 | SEVENTY-FOURTH | | | |
| 1864 | SEVENTY-THIRD | | | |
| 2050 | SEVENTY-SECOND | | | |

**The top was the EIGHTY-FIRST**, confirming the dispatch's premise at the file rather than
inheriting it. **None of EIGHTY-SECOND … EIGHTY-EIGHTH appeared anywhere in the file** — not as a
heading and not in any other position: a case-insensitive Grep for
`EIGHTY-(SECOND|THIRD|FOURTH|FIFTH|SIXTH|SEVENTH|EIGHTH)` over the whole file returned **zero
matches**. No entry was already present, so §6's first STOP did not fire.

### 1.3 The seven entry files — existence, size, and tracked state

All seven exist at the repository root under the spelling §1 names. Sizes are `git cat-file -s`
by explicit hash — a content-addressed, self-verifying query — and were independently reproduced
byte-for-byte by the read-only inspection script
(scratchpad `inspect_entries.py`), which opened each file in binary and measured it on disk. **The
two routes agree on every one of the eight files**, which also establishes that no line-ending
conversion sits between the working tree and the object store here: every file is LF-only, CR count
zero.

| Entry file | Bytes | Tracked at HEAD? | Blob at HEAD |
|---|---:|---|---|
| `cowork_handoff_entry_eighty_two.md` | 6,558 | **TRACKED**, unmodified | `343d303d…` = its pin |
| `cowork_handoff_entry_eighty_three.md` | 11,850 | **TRACKED**, unmodified | `b4a2c892…` = its pin |
| `cowork_handoff_entry_eighty_four.md` | 45,351 | **TRACKED**, unmodified | `5fdf7eca…` = its pin |
| `cowork_handoff_entry_eighty_five.md` | 19,411 | **TRACKED**, unmodified | `94d356c5…` = its pin |
| `cowork_handoff_entry_eighty_six.md` | 13,666 | **UNTRACKED** | — |
| `cowork_handoff_entry_eighty_seven.md` | 13,635 | **UNTRACKED** | — |
| `cowork_handoff_entry_eighty_eight.md` | 17,122 | **UNTRACKED** | — |
| *(seven combined)* | **127,593** | | |
| `cowork_handoff.md` | 993,890 | **TRACKED**, unmodified | `4f7056c3…` = its pin |

**That four of the seven turn out to be already tracked is one of the things §6 classes as
reported rather than resolved**, and it is reported here. It changes what §3 authorises: those four
are not in the commit.

**The tracked/untracked verdict was reached by two independent routes that agree.** The sanctioned
substitute `tools/audit/changed_paths.py` reported the three untracked entry files as `??` records
and said nothing about the other four; and `git ls-tree` at the explicit commit hash
`98f53aaa723b143dc557ea7785b9d39d112cd114` returned the four and not the three. **The second route
was run because the first alone could not settle it**: that tool's own documented coverage limit is
that a path git ignores is invisible to it, so silence about a path is not by itself evidence that
the path is tracked. `ls-tree` at an explicit hash answers positively, and both routes give the
same partition.

### 1.4 The tracked-modification shape before the act

`tools/audit/changed_paths.py` over the working tree: **850 changed-path records, of which exactly
one is a tracked modification** — `cowork_rulings_2026_08_31_decision_surface_sitting.md`. This is
exactly the one path §7 says to expect. Every other record is an untracked path.

**The standing shell-read guard did not have to refuse `git status --porcelain` here, because it
was never attempted**: the substitute the guard itself names was used directly. Six batches have
now met that refusal; this one did not reach for the refused command. (A different refusal *was*
met, at §6.)

---

## 2. Task 2 — the prepend, and the join rule in one sentence

**THE JOIN RULE: pure byte concatenation — the seven entry files' bytes placed end to end with
nothing inserted between them, nothing stripped and nothing normalised, the whole block inserted at
byte offset 65 of `cowork_handoff.md`, which is immediately after its title line and the blank line
under it and immediately before the `---` line that opens the eighty-first entry.**

That rule needs no adjustment because two facts were measured before it was chosen rather than
assumed: **every entry file already opens with its own `---\n` separator line**, and **every entry
file already ends with a newline**. So concatenating them verbatim puts a `---` immediately before
every `## COWORK SESSION CLOSE (` heading — which is where this file's existing separators already
fall — and the file grows by exactly the sum of the seven sizes, with no join byte at all.

**Nothing was retyped.** The prepend was performed by `prepend_entries.py` (scratchpad), which
opens each entry file in binary, reads its bytes, and writes them. No content passed through tool
output, through this session's prose, or through any transformation. The script refuses to write
unless every one of these holds, and all of them held:

- `cowork_handoff.md`'s `sha256` and size equal the pre-state established at Task 1;
- the eighty-first heading occurs exactly once;
- the four bytes before it are its own `---\n` line;
- the bytes before the insertion point are exactly the title line and the blank line;
- none of the seven ordinals already appears in the file;
- every entry file opens with `---\n` and ends with a newline;
- the concatenation preserves length, the head is unmoved, and the pre-existing content below the
  insertion point is byte-identical.

The insertion is at byte 65; the seven spans then occupy 65…127,658. **The entry files themselves
were neither deleted, moved nor edited** — proven at §4.4, not asserted.

---

## 3. Task 3 — the commit

**One commit: `4c9b7af5066fdf51e4b726f6fdc151b7e4153b0c`**, on `master`. Not pushed, not amended,
not squashed, not rebased, not tagged.

**Its full path list, taken from git** (`tools/audit/changed_paths.py --commit <hash>`):

```
M	cowork_handoff.md
A	cowork_handoff_entry_eighty_eight.md
A	cowork_handoff_entry_eighty_seven.md
A	cowork_handoff_entry_eighty_six.md
4 changed path record(s) [commit]
```

**Exactly the four §3 authorises, and no fifth.** `cowork_handoff.md` plus the three entry files
Task 1 found untracked. **Entries eighty-two through eighty-five are tracked and unmodified, so
they are not in the commit** — reported here as §3 requires. The staged set was checked against
this list *before* committing (`--staged` reported the same four), so the authorisation was
verified in advance rather than only after the fact.

Nothing else reached it: not this report, not the dispatch, not
`cowork_rulings_2026_08_31_decision_surface_sitting.md`, not the three files §7 says are owed to
the next landing, and nothing under `tools/audit/derivation_exemplars/`.

**The two trailers were written exactly as §3 gives them**, and are present at the end of the
message:

```
Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01B5AoBhq79pQk4FaSV9oMsN
```

**`CLAUDE.md` forbids neither trailer**, so neither was omitted. Its commit rules are *commit only
when explicitly asked* (this dispatch asks) and principle #14's one revertible, provenance-stamped
commit (this is one, and it is revertible); it mandates no message form beyond that, so §3's block
stands unaltered. **Two differences in the trailer's wording are reported and not resolved:** the
repository's older form of the first trailer carries a parenthetical this string does not, exactly
as §3 records; and this session's own harness default carries that same parenthetical. §3 says to
use the block as given and that the difference is the user's to standardise, so it was used as
given. The message carries no value of this project's own measurement (#17f, **D-431**).

---

## 4. Task 4 — the proofs. Content first, then order.

All of §4 was re-derived **from disk after the write** by `verify_prepend.py` (scratchpad), which
trusts nothing the writing script produced: it re-reads the result, re-reads each entry file, and
**locates each span by searching the result for that entry file's own bytes**. A span found that
way is a span that was not retyped or normalised — that is the whole force of the check.

### 4.1 Each entry's bytes survived — seven of seven

For each entry the source file's `sha256` and the `sha256` of the corresponding span now inside
`cowork_handoff.md` are **equal**, and the entry's byte string occurs in the file **exactly once**.

| Entry | Span in the file | `sha256` — source **and** span (identical) |
|---|---|---|
| eighty-eighth | 65…17,187 | `4fe3638aa7d161f75c86db0382dc978f8b4deb5b490622cf8732f3581892ae38` |
| eighty-seventh | 17,187…30,822 | `1af7aa763d0178b7af09c96e02b5cd6d759c016ebc58dbf8038331008b498848` |
| eighty-sixth | 30,822…44,488 | `c350740b2a325e6befac1c58741a0e20c4df83be90ab357f13f8b585a23ce74b` |
| eighty-fifth | 44,488…63,899 | `65153ed0b9106e723420c0d81a63ce8ab0149c7dc24a55e6e5478f181a0c618a` |
| eighty-fourth | 63,899…109,250 | `84ff19954d51202768c9279dbb3aec5c22b756cf998739ad3a6f3e3458ef8178` |
| eighty-third | 109,250…121,100 | `e6992a74355cc7d902dbc1a8d8f7bd02d784cd12673180f8a860dd8528312cd7` |
| eighty-second | 121,100…127,658 | `82f73b97beec926b8b922e49d99d02811c2dbd823bf4972beeb25dbf054d4d7e` |

**Not one differing pair.** §6's third STOP did not fire.

### 4.2 The size arithmetic closes exactly

The *before* size is not taken from my own earlier reading: the verifier fetches the original blob
`4f7056c362990cfffa5bb03038f1fce1edcfe968` from git and measures it.

```
original cowork_handoff.md (git blob 4f7056c36299)      993,890
seven entry files combined                              127,593
expected after = 993,890 + 127,593                    1,121,483
actual after                                          1,121,483
```

**Equal.** The join rule §2 reports adds and removes nothing, so no allowance is claimed and none
is needed. The committed blob is `0be97f028972c0f4cae3e55b5307aaea3b032f47`, and `git cat-file -s`
on it returns **1,121,483** — so the size that was verified on disk is the size that landed, and
no conversion sits in between.

### 4.3 The pre-existing content is present unchanged — §7's insertion-only requirement

Three checks, all against the original blob fetched by explicit hash:

- the head above the insertion point is byte-identical to the original's first 65 bytes;
- **everything below the insertion point is byte-identical to the original from offset 65 onward**;
- removing the inserted block from the result reconstructs the original **exactly** — that is, the
  original file's bytes are all still present, in order, and unsplit.

Nothing already in that file was changed, reordered or removed.

### 4.4 The entry files themselves are untouched

Every one of the seven was re-hashed with `git hash-object` after the act and is **byte-identical
to its Task 0 pin** (§1.1). So were all seven other pinned files, including the dispatch —
which discharges the declared-departure route's *prove the blob unmoved before staging*. The entry
files stay at the root exactly as they stood; whether they are later retired is not this batch's.

### 4.5 The heading order, and no duplicate ordinal

**24 headings, top to bottom:** EIGHTY-EIGHTH, EIGHTY-SEVENTH, EIGHTY-SIXTH, EIGHTY-FIFTH,
EIGHTY-FOURTH, EIGHTY-THIRD, EIGHTY-SECOND, EIGHTY-FIRST, EIGHTIETH, SEVENTY-NINTH, SEVENTY-EIGHTH,
SEVENTY-SEVENTH, SEVENTY-SIXTH, SEVENTY-FIFTH, SEVENTY-FOURTH, SEVENTY-THIRD, SEVENTY-SECOND,
SEVENTY-FIRST, SEVENTIETH, SIXTY-NINTH, SIXTY-EIGHTH, SIXTY-SEVENTH, SIXTY-SIXTH, SIXTY-FIFTH.

It runs **88, 87, 86, 85, 84, 83, 82, 81, 80** and downward, as §2 requires. **Every ordinal appears
exactly once** — 24 distinct of 24 — so §6's fourth STOP did not fire. Seventeen headings before,
seven added, 24 after; the count closes.

---

## 5. ★ THE ONE FINDING — six entry boundaries lost their blank line, and it is not repaired

**What it is.** In `cowork_handoff.md` as it stood, every `---` separator line was preceded by a
blank line. **Six of the twenty-four boundaries in the resulting file are not.** Measured at every
boundary by `check_boundaries.py` (scratchpad) — not sampled, and not carried from memory of a
check:

| Boundary (the `---` before…) | Blank line before it? |
|---|---|
| EIGHTY-EIGHTH (line 3) | **YES** — the host file's own blank line under its title |
| EIGHTY-SEVENTH (236), EIGHTY-SIXTH (418), EIGHTY-FIFTH (593), EIGHTY-FOURTH (852), EIGHTY-THIRD (1403), EIGHTY-SECOND (1556) | **NO** — six seams internal to the inserted block |
| EIGHTY-FIRST (1640) | **YES** — the eighty-second entry's own bytes end with a blank line |
| the seventeen pre-existing boundaries, EIGHTIETH (1852) through SIXTY-FIFTH (4919) | **YES**, all seventeen |

**The cause, established at the bytes.** Six of the seven entry files end with a single newline;
only `cowork_handoff_entry_eighty_two.md` ends with a blank line. The join rule preserves each
file's bytes exactly, so those six files' endings become those six seams.

**Why it is not repaired.** Repairing it means inserting six bytes that no source file holds. §2
says in terms that nothing is *reformatted*, that each file's bytes are *preserved exactly as they
are*, and that a trailing newline is neither stripped nor added. Adding them would also break the
exact size equality §4.2 rests on. §6 does not list this as a STOP. So it is surfaced for the
user's ruling and left as it stands — six single-byte insertions would close it whenever he wants
it closed.

**What I can and cannot say about the consequence.** The structural fact is measured: at six
boundaries a `---` line directly follows a non-blank line. Whether a given renderer then treats
that `---` as a horizontal rule or as a setext heading underline for the line above it — the latter
would make the preceding line an H2 and remove the separator — **I did not measure**, and I do not
assert it. It is a real question about how the handover document reads, and it is the reason this
is surfaced rather than left in a table.

**No open-items row was created for it**, because §7 forbids this batch from creating, flipping or
discarding one. Under **D-641** an apparatus finding is rowed and left; that row, if the user judges
one owed, is not this batch's to write.

---

## 6. STOPs — none of §6's fired; one thing reported rather than resolved

**No STOP fired.** Taking §6's list in order: no ordinal was already present (§1.2); no entry file
was missing under the spelling §1 names (§1.3); no span digest differed from its source file's
(§4.1); no heading ordinal appears twice (§4.5); no path in the commit is unauthorised (§3); no
read disagreed with its pin (§1.1, §4.4); and no act outside §7 was taken (§7).

**Reported rather than resolved, as §6 directs:**

1. **The standing shell-read guard refused a command.** The first attempt to read the derived
   gating answer was a `python -c` naming `tools/audit/nongating_apparatus_rows.json`, and the guard
   denied it, citing `CLAUDE.md` Conventions, **D-253**, and the guard-family ruling of 2026-08-08.
   The refusal was correct and the file tools were used instead (Grep for the field, then Read at
   the artifact). No working-tree content was read through a shell anywhere in this batch. The
   three scripts this batch ran are the method §2 orders in terms — *write a script that reads each
   entry file's bytes and writes them* — which is the one route that does not retype a governing
   file's content out of tool output; they live in this session's scratchpad, outside the
   repository, so the repository footprint stays exactly what §7 declares.
2. **Four of the seven entry files turned out to be already tracked** (§1.3), which §6 names
   explicitly. They are excluded from the commit and reported.
3. **`CLAUDE.md` forbids neither trailer**, so §6's third *reported rather than resolved* case did
   not arise; the trailer-wording differences are reported at §3 instead.

---

## 7. The footprint — stated as the list of this batch's own ordered acts

**Edited: `cowork_handoff.md`, and only by insertion** — proven at §4.3 by reconstructing the
original from the result. **Created: one commit (`4c9b7af506`) and this report.**

`tools/audit/changed_paths.py` over the working tree, before and after, is what establishes that no
other path moved:

- **before the act:** 850 records — 1 tracked modification
  (`cowork_rulings_2026_08_31_decision_surface_sitting.md`) and 849 untracked;
- **after the commit:** 847 records — the same 1 tracked modification and 846 untracked.

**The arithmetic closes with nothing unexplained:** 849 − 846 = 3, exactly the three entry files
that stopped being untracked by being committed. **No new untracked path was created in the
repository by any act of this batch**, and `cowork_handoff.md` returned to clean. This report,
written after that enumeration, is the one further untracked path §7 authorises.

**The tracked-modification assumption held exactly.** §7 expects one inherited tracked modification
and expects `cowork_handoff.md` to become a second the moment §2 runs. Measured mid-flight, that is
precisely what was there — those two and no other — so nothing was carried to the user before
committing.

**Not touched:** the seven entry files' own content (§4.4); `.gitattributes` and no ignore rule —
that question is still owed to the user; `tools/audit/derivation_exemplars/` — still deliberately
untracked, still not committed; no musical source anywhere; no registry, manifest or pin;
`tools/snapshot_sources_manifest.json` and the eleven snapshot sources; no governing document other
than the handover file this batch is for; `STATUS.md` read and unedited.

**Not done at all:** no build, no test, no golden, no measurement of the analysis; nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; no boot pack rendered and no frozen pack
opened; **no open-items row created, flipped or discarded**; **no decisions-register entry and no
`D-NNN` allocated**; the workbook not opened; nothing staged from the musical corpora; no brief
written or amended; no session booted; nothing pushed.

**The three things the landing batches were forbidden to repair in passing stay unrepaired:** the
manifest's `rendered_from` line for pack member (7); the inherited bare uses of *bar* and
*register*, which belong to **OI-229**; and the `.gitattributes` question.

**The three files owed to the next landing were not committed**, as §7 requires:
`cc_instruction_sitting_landing_second_2026_09_01.md`, its report, and the ruling record.

---

## 8. The standing self-check, run before this report was written

Of the work actually on disk, read at the diff and at the objects — not of the intention.

1. **Guiding principles.** **#12** — nothing removed; every pre-existing byte proven present, in
   order and unsplit (§4.3), and the seven entry files preserved whole. **#14** — one revertible,
   provenance-stamped commit. **#15** — verified at the objects on the full output surface: content,
   size, footprint, order, the commit's own path list, and every landed blob re-established at the
   commit object; nothing rests on an assertion. **#19** — the checks are positive rather than
   merely-unfalsified: each span is *located* by its source bytes, the *before* state is fetched
   content-addressed from git, and the tracked/untracked partition is settled by two independent
   routes because the first alone could not settle it. **#6** — the seven entry files now stand
   beside a file that contains their content. That duplication is the dispatch's explicit choice
   (§2's *the entry files themselves are not deleted, moved or edited*), and their retirement is
   reserved to the user; it is reported, not resolved. **#13** — the one thing that surprised me
   (six seams losing their blank line) is surfaced at §5 before anything was built around it.
2. **Conventions.** American English. No self-invented label, abbreviation or numbering scheme; the
   ordinals, the entry names and the clause names are the record's own. Music-theory words: this
   report uses none of the reserved words in a non-musical sense — where the excluding sense of
   *bar* was wanted the word *forbid* is used, *measurement tool* and *script* stand for the
   non-musical sense of *instrument*, *value* for *figure*, *remainder* for *rest*, and *read in
   binary* replaces the operating-mode sense of *mode*. Bare *register* appears only in *the
   open-items register* and *the decisions register*, both in full.
3. **The figures-and-premises rule (D-431, and the character-figure clause).** Every value here
   names the tool that produced it: `git cat-file -s` and `git ls-tree` at explicit hashes,
   `git hash-object`, `tools/audit/changed_paths.py`, and the three scratchpad scripts
   `inspect_entries.py`, `prepend_entries.py`, `verify_prepend.py` and `check_boundaries.py`. **The
   digests and the arithmetic are stated in this report because §4 orders them stated** — *show them
   equal*, *state the arithmetic* — and each is re-derivable by anyone at a named git object, which
   is what the rule protects. No value is carried from a secondary surface; every premise about the
   file's prior state was checked at the file or at the object rather than inherited from the
   dispatch, including the dispatch's own premise that the topmost entry was the eighty-first.
4. **The file-tools rule (D-253).** All working-tree content was read with Read and Grep. The shell
   was used only for: git object queries by explicit hash (`cat-file`, `ls-tree`, `hash-object`);
   the sanctioned substitute `tools/audit/changed_paths.py`; `git add` and `git commit`, which Task
   3 orders; and the four scripts, which are §2's own mandated method. One guard refusal was met and
   obeyed (§6).
5. **Uncertainty on any comparison (#24).** No comparison between two measured quantities is
   asserted. Every claim here is an exact byte equality or an exact count, which carries no sampling
   uncertainty. The one thing I could not measure — how a renderer treats the six seams — is stated
   as unmeasured at §5 rather than asserted.

**One correction of record, so it is not mistaken for a proof.** The first inspection script printed
a boolean `ends with \n` that read `False` for all eight files. That boolean was wrong: an escaping
mistake made it test for a literal backslash-and-n. The trailing-byte facts this batch relies on
come from the same run's byte dumps of each file's last twelve bytes, which show the newline
directly, and from `prepend_entries.py`'s own guard, which refuses to write unless every entry file
ends with a newline and which did not fire. Nothing rested on the wrong boolean.

---

## 9. Done, on the ruled stop form

**What was done.** The pre-state was established at the file, not inherited: `cowork_handoff.md`'s
topmost entry was the eighty-first and none of the seven ordinals was anywhere in it. Fifteen files
were pinned and all seven entry files found present. The seven entries were prepended in the order
§2 gives, by a script that read their bytes and wrote them, under a join rule of pure concatenation
that adds and removes nothing. All seven span digests equal their source files'; the size arithmetic
closes exactly; every pre-existing byte is proven present, in order and unsplit; the heading order
runs 88 through 65 with no ordinal twice; and one commit,
`4c9b7af5066fdf51e4b726f6fdc151b7e4153b0c`, carries exactly the four authorised paths.

**What was not done.** Nothing was pushed. No entry file was deleted, moved or edited. The four
already-tracked entry files were not committed. The six boundaries that lost their blank line were
not repaired, and no open-items row was created for them. The `.gitattributes` question, the
manifest's `rendered_from` line for pack member (7), and OI-229's inherited bare uses stay
untouched. The three files owed to the next landing were not committed.

**The remainder is untouched rather than partly worked.** This batch's ordered acts are complete;
nothing is half-edited, half-staged or half-written. The working tree carries the one tracked
modification it carried before this batch began, and one new untracked path — this report.
