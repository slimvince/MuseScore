# The staggered-entries exemplar — decoded, whole-staff-checked, named and provenanced (dispatch, 2026-09-01)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side, executing **Ruling 19 (§3w)** of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md` — the staggered-entries slot is filled by
> container decode, with two conditions that are part of the ruling and a declared fallback.
> **The user opens it with the CC run of his choice.**
>
> **★ THE WRITING SIDE'S RESTRAINT.** From hand-over, the writing side does not touch this file or any
> file named in §0's read-first block while the batch runs.
>
> **★ WHAT THIS BATCH IS, IN ONE SENTENCE.** It extracts one `.mscx` from one `.mscz`, subjects it to the
> whole-staff check Ruling 19's **condition (i)** makes part of the ruling, and — only if that check
> passes — writes it into the repository under a declared name with a provenance note, which is
> **condition (ii)**.
>
> **★ AND WHAT IT IS NOT. IT STAGES NOTHING.** Ruling 19 states in terms that *the decode is a dispatch
> and the staging is a later act*. **No brief is written, no boot pack is rendered and no session is
> booted.** Writing a file into the tree is not staging it in front of a deriving session.
>
> **★ TWO CHOICES IN THIS DISPATCH ARE THIS SIDE'S AND ARE DECLARED, NOT HIDDEN.** The **destination
> directory** and the **file name** are not in Ruling 19; the ruling requires only *"a name that does"*
> name the music. Both are this side's, both are stated at §4, and **both are the user's to overturn at
> no cost** — nothing downstream has been built on either.

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1).

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
   gating answer.
2. `BUILD_AND_TEST.md` — **conditionally mandatory, condition NOT met** (no build, no test, no project
   tool, no measurement of the analysis).
3. `docs/score_inventory.md` — **whole.** Hard rules **2** and **3** bind this batch by name.
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` **§3o (Ruling 15), §3u, §3v and §3w (Ruling
   19)** — **whole.** §3w is the authority; §3u and §3v are the check questions it applies.
5. `cc_mscz_container_establishment_report.md` — **whole.** Its claims are **RELAYED**; §1 orders the
   load-bearing ones re-established at the objects.
6. This document, whole.

The bash rules of `CLAUDE.md`'s VS Code section bind every command (#6). **Hard rule 3: the path
`"tools/extra scores"` CONTAINS A SPACE and is quoted in every command.**

## 1. Task 0 and Task 1 — pin, then establish the start state BEFORE anything rests on it

**Pin** this file and every file §0 names with `git hash-object -w`; later reads from `git cat-file blob`.
A read disagreeing with its pin is a **STOP**.

**Establish and report, BEFORE any assertion rests on it:**

- **The source archive is the object the previous batch measured.** `"tools/extra scores/large/bach-
  brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"` must be **75,260 bytes** with
  **`sha256 56e2241707caea88e24ec9ab9ae0e5ff9f26dffabfd7638badda8df6acf89cfb`**. **A mismatch is a
  STOP** — the file moved since it was established and nothing below is about the same object.
- **The tracked-modification shape** (§7). *If `git status --porcelain` is refused by the standing
  shell-read guard, use the substitute the guard names and say so — the previous batch met exactly this
  and reported it.*
- **The destination directory does not already exist**, and **no file already stands at the destination
  path of §4.** If either exists, **STOP and report** rather than overwriting.
- **★ THE LINE-ENDING HAZARD, ESTABLISHED AT `.gitattributes` BEFORE ANY FILE IS WRITTEN.** That file
  carries `*  text=auto` and, in its own comment, *"(.mscx is uncompressed XML and is left under
  text=auto by design — only the committed .mscz set needs this.)"* **So a committed `.mscx` IS subject
  to line-ending normalisation — the OI-195 / OI-34 class the same file names.** Confirm that wording at
  the object and report it. **This batch does NOT edit `.gitattributes`**; §4 handles the consequence by
  measuring it, and §5 leaves the question owed.

## 2. Task 2 — extract, and re-establish the plainness and provenance counts

**Extract to a scratch directory OUTSIDE the repository working tree** — the OS temp directory, exactly
as the previous batch did. **Report the absolute scratch path.**

**Re-establish at the extracted file, not at the previous report (#15).** The previous batch reports the
values in the right-hand column; **confirm each, and report any divergence rather than resolving it**:

| Fact | Previously reported |
|---|---|
| the single `.mscx` member's name | `temp_10111.mscx` |
| its uncompressed byte length, and that extraction equals it | 1,701,770 |
| its `sha256` | `a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80` |
| `<Harmony>` / `<FiguredBass>` / `<StaffText>` | **0 / 0 / 0** |
| part-list and body `<Staff id="N">` sections | 9 and 9 |
| `<museScore version>` / `<programVersion>` | `3.01` / `3.0.0` |

**The `programVersion` line is §3v's third check question — *whose file is it?* — and it is the reason
this file is a candidate at all:** `3.0.0` is two major versions before the `5.0.0` this repository
builds (`version.cmake`), **so it cannot be this build's output.** Confirm it at the file.

## 3. Task 3 — CONDITION (i): the whole-staff check, which is part of the ruling

**The previous batch tested the first 24 chords only and correctly reported *matches over the tested
window*, never *duplicate*. Ruling 19 makes the wider check part of itself.**

**For EVERY body staff, emit the ordered sequence of `<pitch>` values over the WHOLE staff** — every
`<Chord>` in document order, every `<pitch>` child in file order — and compare **all 36 pairs**.

**Report, for each of the three pairs the window flagged — `1↔4` (Violino principale / Violino 1),
`2↔3` (the two recorders), `7↔9` (Violoncello / Continuo):**

- the total chord count and total pitch count of each staff;
- **whether the two sequences are identical over the whole staff**;
- if not, **the index of the FIRST divergence and the two values there**, and the **proportion of
  positions that agree**;
- and the same one-line verdict for any **other** pair that turns out to match over the whole staff.

**★ THE RULED CONSEQUENCE, AND THE BATCH DOES NOT CHOOSE IT.**

- **If any pair is identical over the WHOLE staff, the file is in Corelli's class. STOP. Write no file
  into the repository, report the result, and close.** Ruling 19's fallback then fires — *the slot goes
  to `tools/dcml/frescobaldi_fiori_musicali/MS3/12.15_Recercar_dopo_il_Credo.mscx` with `<Harmony>`
  barred by element name* — **but that is a LATER act and is NOT this batch's**. Do not stage, copy or
  touch the Frescobaldi file.
- **If every pair diverges, condition (i) is met** and Task 4 runs.

**★ WRITTEN PREDICTION, MADE BEFORE THE ACT (#17b). A falsified prediction is RECORDED as falsified and
not repaired.** **This side predicts all three pairs DIVERGE**, on the reading that they are
concerto-grosso doublings — a principale doubled by the ripieno first violin, two recorders in unison at
the opening, and a continuo doubling the cello — which separate as the movement proceeds. **The reading
is this side's and is not evidence; the sequences are.** *The ABC file's staves 1 and 2 were in unison
for fourteen chords and separated at the fifteenth, which is why a window was never enough.*

## 4. Task 4 — CONDITION (ii): the licence check, the write, and the provenance note

**(a) THE LICENCE IS CHECKED AT THE FILE BEFORE ANYTHING ENTERS THE REPOSITORY.**
`tools/extra_scores_registry.json` records `"license": "CC0"` and
`"license_metaTag_raw": "OpenScore (CC0)"` for this path, and `docs/score_inventory.md` states the
licence was read **from each file's own copyright metaTag only**. **Read that metaTag in the extracted
`.mscx` and quote it.** **If it does not say CC0 — or is empty — STOP and write nothing**: the reason
this file may be copied in-tree at all is its licence, where `docs/score_inventory.md` records that the
DCML clones' licences make an in-tree copy GPL-incompatible.

**(b) THE DESTINATION AND THE NAME — THIS SIDE'S CHOICES, DECLARED.**

```
tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md
```

**The directory** sits beside `tools/audit/derivation_boot_pack/`, the existing home of derivation
material, and is created by this batch. **The name** follows the `bach_en_fr_suites` convention
(`BWV806_10_Gigue.mscx`). **`temp_10111.mscx` names nothing about the music, which is why Ruling 19
requires a name at all.** Both choices are the user's to overturn.

**(c) THE WRITE, AND THE MEASUREMENT THAT KEEPS ITS CLAIM HONEST.** Copy the extracted file to that path
**byte-for-byte** — no re-encoding, no re-formatting, no line-ending conversion. **Then `sha256` the file
as it now stands on disk.**

- **If the on-disk `sha256` differs from the extracted one, that is a STOP** — something normalised the
  file on the way in, and the provenance note must not claim what is not true.
- **Report both digests either way.** And **report, without acting on it, that `.gitattributes` leaves
  `.mscx` under `text=auto`, so a later checkout on a CRLF platform may alter this file's line endings.**
  **Do not edit `.gitattributes` and do not add an ignore rule** — §5 leaves that owed.

**(d) THE PROVENANCE NOTE**, at the `.provenance.md` path above, carrying **only established facts**:

1. the source archive's path, byte size and `sha256`;
2. the member name inside it (`temp_10111.mscx`) and its recorded uncompressed length;
3. that the file arrived by **container extraction** and **no byte was altered**, with the proof stated
   as what it is — **extracted length equals the archive's recorded length, and the member's stored
   CRC-32 verifies** — and the on-disk `sha256` beside the extracted one;
4. the declared `<museScore version>` and `<programVersion>`, and the plain statement that `3.0.0`
   **predates this repository's `5.0.0` and so is not this build's output**;
5. the licence metaTag, quoted;
6. the three annotation counts (`<Harmony>`, `<FiguredBass>`, `<StaffText>`), all 0;
7. **condition (i)'s result in full** — every pair's verdict, with the first-divergence index for the
   three flagged pairs;
8. that the naming and the directory are **the Cowork writing side's choices under Ruling 19 condition
   (ii)**, and the `.gitattributes` line-ending caveat;
9. the authority: **Ruling 19 (§3w)** of `cowork_rulings_2026_08_31_decision_surface_sitting.md`.

**No figure of this project's own measurement appears in it (#17f, D-431).**

## 5. Done

Done when: the source archive matched its pin; the plainness and provenance facts were re-established
and any divergence reported; **condition (i) ran over whole staves and its verdict is reported pair by
pair**; and either the STOP fired and nothing was written, or the licence was quoted, the file was
written byte-identical to the extraction and proven so, and the provenance note carries all nine items.
**Every STOP met is written up. Then close on the ruled stop form.**

**Left OWED and not acted on, stated so it is not mistaken for done:** whether `.gitattributes` should
gain a rule keeping committed `.mscx` exemplars byte-stable. **That is the user's.**

**The standing self-check runs before the report is written** — the actual diff on disk of every touched
file, against the principles, the conventions and `DEFECT_TYPES.md`.

## 6. STOPs

The source archive's size or `sha256` not matching §1; the destination directory or either destination
file already existing; the licence metaTag not saying CC0, or empty; **any staff pair identical over the
whole staff**; the on-disk `sha256` differing from the extracted `sha256`; extraction writing anywhere
under the repository working tree; a read disagreeing with its pin; any act outside §7.

**Not a STOP, and reported rather than resolved:** any divergence from the previous report's figures; the
prediction of §3 falsified; the shell-read guard refusing a command.

## 7. The footprint

**Created:** `tools/audit/derivation_exemplars/l0-l1/` and the two files §4(b) names, **and this batch's
report — and nothing else.** **Edited: NOTHING.** **`.gitattributes` is NOT edited.** No `.gitignore` rule
is added. No score anywhere is edited, renamed, moved, converted or re-saved — **the source `.mscz` is
read only.** No registry, manifest or pin is touched; **`tools/snapshot_sources_manifest.json` and the
eleven snapshot sources are untouched (Hard rule 2)**; `tools/extra_scores_registry.json` is **READ
only** and gains no row. No tool source is edited.

**Not done at all:** no build, no test, no golden, no measurement of the analysis, nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and neither frozen pack
opened**; **no governing document amended** — including `docs/score_inventory.md`, which this batch reads
and does not touch; **no open-items row created, flipped or discarded**; **no decisions-register entry and
no `D-NNN`** — that register cannot accept one and `cowork_register_rule_c_suspension_2026_08_28.md` is
the route; the workbook not opened; **NO SCORE STAGED**; **the Frescobaldi fallback file not touched**; no
brief written; no session booted.

**The tracked-modification assumption, as a SHAPE with a STOP and with the known exceptions named.** This
batch expects untracked Cowork material, **and expects these tracked-and-modified files:
`FRAMEWORK.md`, `cowork_rulings_2026_08_31_decision_surface_sitting.md`,
`tools/audit/derivation_boot_pack.json` and `tools/audit/gen_derivation_boot_pack.py`** — the same four
the previous batch established, the sitting record having since gained §3w and §3x. **None is a STOP. Any
OTHER tracked modification this batch did not make IS a STOP.**

---

*Provenance: written by the Cowork writing side, 2026-09-01, executing Ruling 19 (§3w) of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`. **The facts this dispatch asserts were read at
their objects by this side with file tools**: the `.gitattributes` `text=auto` rule and its `.mscx`
comment; `version.cmake`'s `MUSE_APP_VERSION` 5.0.0; the registry's licence and measured row for the
source archive; Hard rules 2 and 3 at `docs/score_inventory.md`. **The archive's own figures — the member
name, the digests, the staff and annotation counts — are RELAYED from
`cc_mscz_container_establishment_report.md` and §1 and §2 order every one re-established at the object,
because a relayed figure is not this batch's.** No shell command was run on the repository by the writing
side. No figure of this project's own measurement is restated (#17f, D-431).*
