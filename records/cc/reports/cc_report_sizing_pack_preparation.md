# CC report — the SIZING PACK: the `scoring-model` subject rendered with an EMPTY withheld family, and the leak list delivered

> **Dispatch:** `cc_instruction_sizing_pack_preparation.md`, performed 2026-08-24, executing Ruling 1
> and §4(1) of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`, and landing
> `cowork_rulings_2026_08_24_method_ruling_sitting.md` — landed, not acted on.
>
> **NO SESSION WAS BOOTED, nothing was derived, nothing compared, no oracle opened, and
> `docs/scoring_model.md` was NOT opened.** The deliverable is
> `ratification_surfaces/cowork_sizing_pack_leak_list_reading.md`; the full close is the
> **THE PILOT CLOSED ESTABLISHED AND THE SIZING PACK RENDERED** section of `cowork_away_returns.md`.
> Where this report would name hashes it cannot contain, it points at the git log — no backfill
> commit was written.

---

## 1. What was done, in one paragraph

Task 0 landed two sitting records, the modified handoff and the dispatch, and regenerated the
evidence-pin membership after measuring its difference against the committed blob from every route.
Task 1 authored a second subject, `scoring-model`, into the boot-pack generator's AUTHORED tables
with an EMPTY withheld family, took one of the two licensed rendering accommodations, rendered the
pack for both subjects, and wrote the leak list as a reading file in LIST FOUR's shape. Task 2 is the
close. The harmony-boundary subject — its pack, its family, its reading file and its manifest block —
is byte-unchanged, proven at the objects rather than asserted.

## 2. Task 0 — the landing, the membership, the push

**A1's check was taken as the first act after the ordered session-start read, entirely at
content-addressed objects,** because the bare working-tree forms are denied by the armed guard and
time out on this mount.

1. **Exactly ONE tracked modification, and it is the one A1 names.** The population was ENUMERATED
   with the sanctioned enumeration tool rather than sampled: `cowork_handoff.md`, and no other
   tracked path anywhere in the tree.
2. **The three named untracked paths are present and all three are absent from the tip**, each
   checked at the object.
3. **A1's CONTENT description was measured INCOMPLETE, and the difference is reported rather than
   absorbed — see §6.1. A1's declared STOP did not fire and the ordered act is unchanged.**
4. **The premise ledger re-checked at the objects:** the tip and both refs, with the stated parent
   and subject; the guard summary at its own artifact; the committed membership artifact's
   ruling-record count; and the harmony-boundary subject's whole `counted` block, all matching the
   ledger.

**The membership was regenerated and measured against the committed blob BEFORE it was accepted, from
every route.** Route A moved by exactly the predicted amount with exactly the two predicted names;
route B added nothing, neither landed record carrying on any line the word that route matches on;
route C is unmoved, this batch adding no measurement tool. **The measured difference is three hunks:
the count, the two added names, and ONE additive derived cross-reference** — the method-ruling
record's leading blockquote names a ratification surface no tool writes, so that document's list of
namings gains the record. **That is the addition A3's own text anticipates and orders reported.** No
existing value moved anywhere.

The five ordered paths were staged, enumerated as staged, committed under the exact ordered subject,
pushed, and verified at the object; the enumeration was re-taken at the commit.
**`gen_evidence_pin_membership.py --check` passes at the resulting tree.**

## 3. Task 1 — the subject authored, the pack rendered, the leak list delivered

### (a) The authored `scoring-model` entry

Three authored tables gained one entry each: the `WITHHELD` table (a plain-words subject line naming
`docs/scoring_model.md` as the unit whose specification a later blind session derives; an oracle field
stating in terms that there is none and citing the ruling that empties the family; an empty document
map and an empty passage list; and NO `the_identity_the_ruling_names`, the ruling naming none); the
`CRITERION` table (every term empty); and the `VERDICTS` table (empty, authored explicitly so the
emptiness is visible where a reader looks for a subject's verdicts).

### (b) The two licensed accommodations — ONE was needed, and it is quoted whole

**(i) was NOT needed.** The tool's authored shape expresses an empty withheld family and an empty
candidate criterion with **no code change at all**: the optional keys are read through `.get`, an
empty criterion returns no candidate, an empty verdict table grades none, and the distribution
accounts for the population exactly. **No change was made under licence (i).**

**(ii) WAS needed and was taken.** Before it, the read-me's what-was-cut section was hardcoded: a
`Two kinds:` lead-in, an entries bullet, and a passages line that renders `* 0 passages inside …` at
zero — so a subject withholding nothing would have told its session that material had been withheld
from it. The section is now DERIVED from the counts. **The whole diff, three hunks:**

```diff
@@ -1125,18 +1170,68 @@ def render_defect_types(rows: list[list[str]], header: list[str]) -> str:
     return "\n".join(out) + "\n"


-def render_read_me(subject: str, subject_words: str, passages: list[dict]) -> str:
+def render_what_was_cut(withheld_entries: int, passages: list[dict]) -> str:
+    """The read-me's what-was-cut section, DERIVED from what was actually withheld.
+
+    LICENSED ACCOMMODATION (ii) of §4(1) of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`,
+    quoted verbatim: *"the read-me's what-was-cut section renders truthfully for a subject with no
+    withheld entries and no withheld passages"*.  Before it, the two-kinds lead-in and the
+    entries bullet were HARDCODED, so a subject withholding nothing would have told its session
+    that material had been withheld from it and that there were `0 passages` — the zero-passage
+    bound the record declared twice.
+
+    IT IS DERIVED FROM THE COUNTS AND NOT SWITCHED ON A SUBJECT NAME, so it is true at any future
+    subject; and the two-kinds state re-renders BYTE-IDENTICALLY, which is what shows the
+    rendering derived rather than duplicated (#6).
+    """
+    member_two = MEMBERS[1]["filename"]
+    kinds: list[str] = []
+    if withheld_entries:
+        kinds.append("entries of the design-intent file that were not rendered — you will see "
+                     "identifier gaps, and\n  those gaps are **not** evidence of anything")
+    n = len(passages)
+    if n == 1:
+        kinds.append(f"one passage inside `{member_two}`, marked in place where it was removed")
+    elif n > 1:
+        kinds.append(f"{n} passages inside `{member_two}`, each marked in place where it was "
+                     f"removed")
+
+    head = "## What has been cut out of this pack, and why you are told"
+    tail = ("**Do not try to reconstruct any of it, and do not treat a gap as a hint.** Derive the "
+            "unit from the\ndomain and from what this pack does carry.")
+
+    if not kinds:
+        return f"""{head}
+
+**Nothing has been withheld from this pack for this subject.** No register entry and no passage
+was held back: this unit is not held out against a ruled answer you have not read.
+
+What the design-intent file does not carry is the entries a standing check removed for a
+different reason — an entry whose own rendered words name a path into this project's own
+implementation documents. You will see identifier gaps where that happened, and those gaps are
+**not** evidence of anything.
+
+{tail}"""
+
+    lead = "One kind:" if len(kinds) == 1 else "Two kinds:"
+    bullets = "\n".join("* " + k + (";" if i < len(kinds) - 1 else ".")
+                        for i, k in enumerate(kinds))
+    return f"""{head}
+
+Material has been withheld from this pack **for this subject**, so that what you derive can be
+compared against a ruled answer you have not read. {lead}
+
+{bullets}
+
+{tail}"""
+
+
+def render_read_me(subject: str, subject_words: str, passages: list[dict],
+                   withheld_entries: int) -> str:
     names = [READ_ME] + [m["filename"] for m in MEMBERS]
     listing = "\n".join(
         [f"{i + 1}. `{m['filename']}` — {m['title']}" for i, m in enumerate(MEMBERS)])
-    # DERIVED from the passages actually applied for this subject, so the sentence stays true at
-    # whatever count a subject's authored table carries: singular wording at one, plural at more.
-    n = len(passages)
-    passages_line = (
-        f"* one passage inside `{MEMBERS[1]['filename']}`, marked in place where it was removed."
-        if n == 1 else
-        f"* {n} passages inside `{MEMBERS[1]['filename']}`, each marked in place where it was "
-        f"removed.")
+    what_was_cut = render_what_was_cut(withheld_entries, passages)
     return f"""# READ THIS FIRST — the whole of what this session opens
```

```diff
@@ -1166,17 +1261,7 @@ file, including one of these six — STOP READING THAT FILE AT THAT POINT and re
 and HOW MUCH you had seen.** That record is part of your output. It is not a failure; an unrecorded
 one is.

-## What has been cut out of this pack, and why you are told
-
-Material has been withheld from this pack **for this subject**, so that what you derive can be
-compared against a ruled answer you have not read. Two kinds:
-
-* entries of the design-intent file that were not rendered — you will see identifier gaps, and
-  those gaps are **not** evidence of anything;
-{passages_line}
-
-**Do not try to reconstruct any of it, and do not treat a gap as a hint.** Derive the unit from the
-domain and from what this pack does carry.
+{what_was_cut}

 ## What your output is
```

```diff
@@ -1349,7 +1434,7 @@ def build_subject(subject: str, sort_entries: list[dict], backbone: dict) -> tup
         raise Stop(f"{want_passages} withheld passage(s) authored, {len(passages_applied)} applied")

     files[READ_ME] = render_read_me(subject, authored["the_subject_in_plain_words"],
-                                    passages_applied)
+                                    passages_applied, len(withheld_ids))
```

**★ THE CHECK THAT (ii) IS DERIVED AND NOT HARDCODED WAS TAKEN BEFORE ANY FILE WAS WRITTEN.** With
the authored tables and the new rendering in place and nothing yet rendered, the pack's own `--check`
was run. It reported drift at exactly two things — the manifest, which must gain a subject block, and
the missing `scoring-model` directory — **and at NO file of the harmony-boundary pack.** Since
`check_all` re-renders every file of every subject in memory and compares it to disk both ways, that
is the proof: the harmony-boundary read-me re-renders byte-identically under the changed code.

### (c) The render and the checks

The generator was run bare, so both subjects were written. `--check` over both subjects is **GREEN**.
`gen_guard_classification.py --check` re-derives.

### (d) A5, measured at the manifest and at both pack directories

Every item held. The values are at `tools/audit/derivation_boot_pack.json` →
`subjects.scoring-model.counted` and none is restated here (**D-431**). What was measured rather than
predicted, and its answer:

- **The leak count.** The check ran over the whole design-intent class. **The three harmony-boundary
  leaks recur and there is no further member** — none of the entries formerly withheld for the other
  subject carries a leak string of its own. The identities and their exact matched strings are in the
  reading file.
- **Member byte-identity across the two subjects.** Taken at the **content-addressed blob identifiers
  of the staged files**, not by sampling: members (1), (3), (4) and (6) are BYTE-IDENTICAL across
  subjects; members (2) and (5) and the read-me differ, each by exactly the construction that must
  differ.
- **Member (2) carries ZERO withheld markers**, measured by searching the rendered file for the
  marker string; the harmony-boundary copy carries its two.
- **The harmony-boundary manifest block is BYTE-UNCHANGED.** The manifest's whole difference against
  the Task 0 commit is ONE purely additive hunk, with no removed content line anywhere in the diff.
- **The harmony-boundary pack DIRECTORY is byte-unchanged, every file** — proven by enumerating the
  tracked-modification population after the render: only the manifest and the generator appear.

### (e) The reading file

`ratification_surfaces/cowork_sizing_pack_leak_list_reading.md`, in LIST FOUR's shape: what the leak
check is and what it is for; its scope, stated because a scope that is not stated reads as total; the
full list with each entry's identifier, title, rendered field and exact matched string; the statement
that **this file withholds nothing** — the family is empty by ruling — and that the one question
asked is whether the check goes on excluding these entries for this subject; and a *what this file
does not do* section.

### (f) The guard run and the commit

The FULL set was run again as a check: one failing, [[OI-372]]'s tool alone, zero STOPs, the
population unmoved. The ten paths were staged, enumerated as staged, committed under the exact ordered
subject, pushed, and verified at the object.

## 4. Task 2 — the close

Two `STATUS.md` pointer entries, one per task that did work. The forward bound was applied through
`gen_status_batch_bound.py --apply` after its three authored inputs were re-aimed and the outgoing
aiming appended to the kept list (**D-648**, licensed in terms); it moved the previous batch's two
entries and its reconciliation holds in both directions. `gen_session_start_read_size.py` was
regenerated and its `--check` passes. The full close is the **THE PILOT CLOSED ESTABLISHED AND THE
SIZING PACK RENDERED** section of `cowork_away_returns.md`.

## 5. What this batch did NOT do

No session booted. No derivation, no comparison, no oracle. `docs/scoring_model.md` not opened.
Nothing of the harmony-boundary subject touched. No `src/` change, no golden, no test changed, moved
or run, nothing under `tools/corpus/` or `tools/robust_stop/`. No measurement of the analysis built,
designed, scoped or run. No edit to the generator beyond the authored entry and the one accommodation
taken. No edit to any governing document, any register entry or any register source. **No finding
number — the series stands at F88** — and no open-items row created, flipped or discarded.
[[OI-179]] stays OPEN and GATES; [[OI-372]] and [[OI-374]] stand as found.

## 6. Surfaced for the writing side

1. **THE DISPATCH'S ASSUMPTION A1 UNDERSTATES THE WORKING TREE BY ONE HANDOVER ENTRY.** A1 states
   ONE entry (the fifty-second) inserted above the committed content with the fifty-first heading
   marked superseded-as-entry-point. Measured at the objects, **the committed handoff's newest entry
   is the FIFTIETH**: the tree carried BOTH the fifty-first and the fifty-second entries uncommitted,
   and the ONE replaced line is the FIFTIETH heading, which gains its own superseded-as-entry-point
   clause. The arithmetic closes exactly — the two inserted blocks plus one replaced line account for
   the whole measured difference. **The cause is on the record:** the fifty-first entry was written at
   the method-ruling sitting, which produced no dispatch to land it. **A1's declared STOP did not
   fire**, the untracked landing set is exactly the three named, and the ordered act is unchanged.
2. **THE MANIFEST'S OWN PROSE ABOUT THE CANDIDATE CRITERION IS WRITTEN FOR A NON-EMPTY CRITERION AND
   WAS NOT CORRECTED.** For the new subject the block's five conditional bullets and the
   `★_the_bound_on_the_candidate_criterion` paragraph describe a pattern match over the register's
   text, while this subject's criterion is empty **by ruling** rather than by a search that returned
   nothing. The parameter lists rendered directly beneath the bullets are all published empty, and the
   bound paragraph's own words say an empty match is evidence of nothing — so a careful reader is not
   misled — but the prose reads as though a search had been run. **No license reaches it**: it is
   neither the authored subject entry nor either accommodation, and the narrow-letter default governs.
   Reported for the writing side to rule.
3. **THE GENERATOR'S TOP-LEVEL `the_rulings_it_executes` LIST DOES NOT NAME THE SIZING-PILOT RULING**,
   for the same reason. The ruling IS cited inside the authored subject entry, which is licensed, so
   the manifest carries the citation at the subject it governs; the top-level list is now incomplete
   rather than false.
4. **LICENSED ACCOMMODATION (i) WAS NOT NEEDED**, and that is a measured fact about the tool worth
   carrying: the authored shape already expresses an empty family and an empty criterion.

## ★ THE STANDING SELF-CHECK (D-434) OVER THIS BATCH'S OWN WORK

1. *Principles touched.* **#19** — nothing is withheld without a ruled reason, and the reading file
   states what its check does NOT cover. **#6** — one generator, one authored home, and the (ii)
   proof is the harmony-boundary read-me re-rendering byte-identically, taken before any file was
   written. **#12** — the harmony-boundary subject byte-unchanged everywhere; the leak list delivered
   rather than absorbed. **#17(f)/D-431** — the leak count measured at the artifact and restated in no
   prose anywhere. **#13** — the A1 understatement surfaced with its arithmetic rather than worked
   around. **#10** — the two places where the generated manifest's prose is written for the other
   subject are reported rather than corrected past the licence's letter. Conforms.
2. *Conventions.* American English; no self-invented labels; music-theory words in their musical
   sense, every non-musical use qualified — the self-check over the delivered reading file replaced
   bare *figure* in its numeric sense and kept bare *score* out of it entirely.
3. *Figures and premises.* The tip, the guard summary, the membership count and the harmony-boundary
   `counted` block were re-read at the objects; the leak identities were read from the artifact the
   render itself wrote; the member comparison was read from the staged blob identifiers.
4. *File-tools rule.* Declared at §5.1 of the close, including one `python -c` naming a repository
   path that the armed guard DENIED at the session's start, after which the read was retaken with the
   file tools.
5. *Uncertainty.* No difference between measured quantities is asserted in this batch.
6. *Re-read from disk before release.* The generator's whole diff was re-read from the git objects
   after the edits and before the commit; the rendered read-me and the delivered reading file were
   re-read whole from disk.

## 7. THE CORRECTION — a FIFTH commit, added after the end state

**The standing self-check over this batch's own diff, run after the end-state commit, found ONE
convention slip, and a fifth commit corrects it.** The full record is the **★ THE CORRECTION** block
at the end of the close section of `cowork_away_returns.md`; what follows is the same act stated
here, because the previous batch's precedent is that an extra commit is declared in BOTH surfaces.

- **What it was.** The newer of this batch's two `STATUS.md` pointer entries closed with *"no count,
  no leak identity and no rendered figure is restated here"*. **Bare *figure* is reserved for
  figuration**; the numeric sense is written *number* or *value*. The reserved-word inventory names
  this exact collision and the standing bar is that no NEW instance of a known collision is
  introduced. Corrected to *value*.
- **Where it was not.** The close section and this report carried no bare numeric use of the word —
  their only appearances are metalinguistic mentions of the word itself — so nothing else moved.
- **What the fifth commit carries, and nothing else:** the one corrected word in `STATUS.md`; the
  session-start read-size artifact regenerated, so that correcting a must-read leaves no red; this
  section; and the close's own declaration block.
- **What it does not disturb.** The end state is a property of the tree the close commit LEFT, which
  is fixed and historical; this commit cannot change what that run measured. The one standing red is
  unmoved, no STOP is created, and the guard population is untouched.
- **A second, smaller item, DECLARED rather than corrected.** The end-state commit's subject reads
  *OI-372s tool* where it means *OI-372's tool*: a POSIX single-quoted commit subject cannot carry an
  apostrophe, and the dispatch fixes plain single-quoted subjects. **A commit subject is immutable
  without a rewrite of history, which is not an act this batch may take**, so it is declared and left.
  The subject's meaning is unaffected.
- **The commit count.** The ordered structure yields FOUR; the correction made FIVE.

## 8. THE CORRECTION'S OWN CLAIM, MEASURED — a SIXTH commit

**§7's correction block asserted that the one standing red is unmoved, that no STOP is created and
that the guard population is untouched. Those three were written BEFORE they were taken** — a claim
resting on an assertion rather than on an object (**#15**). A sixth commit records the measurement,
rather than editing the claim silently, so the text stands as it was written (**#12**).

**Measured at the tree the correction commit left**, with the FULL guard set run in check mode —
which writes nothing, so the tree carried **zero tracked modifications** before and after the run,
enumerated with the sanctioned enumeration tool both times: **75 guards run**, 4 not run, 16
historical, the population UNMOVED; **ONE failing check**, [[OI-372]]'s tool, the standing red;
**ZERO STOP verdicts**; `gen_guard_classification.py --check` re-derives.

**The three claims hold, and the correction commit created no red.** It is recorded because a claim
that turns out to be right was still unmeasured when it was written, and *it happened to be right* is
not the establishment this record accepts. The full block is at the end of the close section of
`cowork_away_returns.md`.

**THE COMMIT COUNT, RE-TAKEN: this batch carries SIX.** Both surfaces declare it.

---

*Provenance: CC, 2026-08-24, under `cc_instruction_sizing_pack_preparation.md`, executing Ruling 1
and §4(1) of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`. Every value above was read at a
content-addressed git object or at the artifact the run itself wrote; none was carried forward from
an earlier run or inferred from a summary. TOWARDS the ultimate objective and TOWARDS the guiding
principles.*
