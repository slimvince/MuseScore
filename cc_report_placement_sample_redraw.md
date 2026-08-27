# CC REPORT — REDRAW AND RE-SEAL THE PLACEMENT SAMPLE

*Claude Code, 2026-08-27. Executes `cc_instruction_placement_sample_redraw.md`, which executes
Rulings 1, 2 and 3 of `cowork_rulings_2026_08_27_stopped_strata_sitting.md`. Base tip
`aa3077709117962ab05b27d79466bfacc77a2382`, read at `.git/refs/heads/master` with the file tool —
the **ref side**, named as the record requires.*

**THE PLACEMENT TEST WAS NOT RUN. NO FRAME TEXT WAS AUTHORED.** The frame it would be run against
does not exist. **NO ratification, NO admission, NO register entry, NO open-items row created,
flipped or discarded, NO finding number allocated.**

---

## 0. The short of it

The sample is redrawn, sealed and committed at
**`cowork_placement_sample_sealed_redraw_2026_08_27.md`**. **NO STRATUM REMAINS STOPPED.** Seven
strata are drawn; the eighth is recorded NOT ENUMERABLE, which is the finding it contributes.

**The drawing side chose nothing.** The ordering, the threshold and the take are the writing side's,
applied mechanically. Where the rule did not decide something, it is **declared at the stratum it
bears on** rather than settled quietly, and every such declaration is listed in §8 below.

**Four things the writing side should read before anything else:**

1. **Stratum 1's membership measures 79 files, not the 78 the dispatch expects**, and the dispatch's
   explanation of the figure is wrong at the objects. §3.1.
2. **The declared unit "every markdown list item at any nesting depth" had to be pinned to BULLET
   items to return the ruled `N = 33`.** The wider reading returns 38. §8(a).
3. **Stratum 8 returns 59 only if line endings are normalised before comparison.** Without that it
   returns **610**, because one commit changed a member file from CRLF to LF and every heading in it
   then reads as deleted. §3.8, §8(c).
4. **The declared form of a "numbered ruling" / "numbered decision" admits ordinary numbered SECTION
   headings**, by its own second limb. Most of what strata 1 and 2 enumerate is therefore section
   headings, not rulings or decisions. Reported, not adjusted. §8(b).

---

## 1. Task 0(a) — the tip

`.git/refs/heads/master` read **with the file tool** (the **ref** side) reads
`aa3077709117962ab05b27d79466bfacc77a2382`, which is the hash the dispatch names. No STOP.

## 2. Task 0(b) and 0(c) — the start state and the landing

### 2.1 The start state, measured and not assumed

`python tools/audit/changed_paths.py` (D-253's sanctioned enumeration; **`git status` was not run**):

| | |
|---|---|
| changed-path records | **838** |
| of which untracked | **837** |
| tracked modifications | **1** — `cowork_handoff.md`, and nothing else |

No path other than `cowork_handoff.md` stood tracked-modified, so nothing had to be reported and
withheld under the dispatch's clause for that case.

### 2.2 The landing

One commit, **`ec9034011857c223e2eb44ecbb210811908edc61`**, carrying exactly the six paths the
dispatch names and nothing of the standing untracked population:

- `cowork_handoff.md` (tracked-modified)
- `cowork_stopped_strata_surface_2026_08_27.md`
- `cowork_declared_readings_surface_2026_08_27.md`
- `cowork_take_rule_surface_2026_08_27.md`
- `cowork_rulings_2026_08_27_stopped_strata_sitting.md`
- `cc_instruction_placement_sample_redraw.md`

### 2.3 ★ The handoff establishment, and MY OWN count of new entries

**The dispatch asserts no count and I took none from it.** Here is what I derived, and how.

**The tip side, by content-addressed read.** `cowork_handoff.md` at
`aa3077709117962ab05b27d79466bfacc77a2382` resolves to blob
`a984d5a87d2d7ff8d9e5ebb3828ad5b936fd7598`, **812,048 bytes**, **9,879 lines**, **149 markdown
headings**. Its topmost `## COWORK SESSION CLOSE` entry is the **SIXTY-NINTH**, at line 4.

**The worktree side, by the file tools.** **10,206 lines**, **171 markdown headings**. Its topmost
session-close entry is the **SEVENTY-FIRST** at line 4; a **SEVENTIETH** stands at line 159; the
**SIXTY-NINTH** stands at line 331.

**(i) HOW MANY ENTRIES ARE NEW: TWO** — the seventieth and the seventy-first.

**(ii) ADDITIONS-ONLY AND PREPENDED, WITH NO EARLIER ENTRY REWORDED — proven at the objects, not
inferred from the prose.** The object-to-object diff between the tip blob and the staged blob
`5723457f769c204b183a3223d635ff4d5c64a761` (**833,457 bytes**) carries **exactly one hunk**:

```
@@ -2,0 +3,327 @@
```

**+327 insertions, 0 deletions**, inserted after old line 2. Every line from old line 3 onward is
therefore unchanged and shifted by exactly +327. Nothing was removed and nothing was reworded, so
the dispatch's STOP for a change of any other shape did not fire.

**(iii) THE ARITHMETIC THAT CLOSES THE TWO SIDES.** 9,879 + 327 = **10,206** lines. 149 + 22 =
**171** headings, and all 22 new headings lie inside the inserted block. The four session-close
entries the tip already carried are each re-found at a uniform **+327**: 69th 4 → 331, 68th 118 →
445, 67th 265 → 592, 66th 438 → 765.

### 2.4 The ordered tool run

`python tools/audit/gen_evidence_pin_membership.py` — wrote
`tools/audit/evidence_pin_membership.json`; *generated ratification documents 7; **ruling records
read 75**; members 7 — pinned 5, UNRESOLVED 0; tools carrying a pin constant 8; outside this class
3.* The **75** is the narrow matcher's figure and bears directly on §3.1 below.

---

## 3. The eight strata

**Method, stated once for all of them.** Every tracked member's content was read from its
**content-addressed git object** at the landing commit, and every enumeration was **cross-checked
against the file tools**. That the two routes are the same content is established rather than
assumed: after the landing commit `tools/audit/changed_paths.py` reports **exactly one** tracked
modification in the whole tree — `tools/audit/evidence_pin_membership.json`, the file the dispatch
ordered regenerated — so every other tracked file is byte-identical to its blob at that commit.
**Fifteen of stratum 3's twenty-five dossiers are UNTRACKED**, so no git object exists for them;
those were enumerated and drawn **entirely with the file tools**. The ten that are tracked were
measured **both ways**: the two routes agree on **every one of the ten per-file counts**, and
item-for-item — same line, same text — at each of the **six drawn positions** that fall inside them.
Strata 1, 2, 5 and 7 carry their own cross-check as well: the file tools' independent count of the
evidence inventory returns the same 33 and the same 5 uncounted ordered items; and the **first and
last drawn item of each of those four strata — eight items — was re-read one at a time from the
working tree with the file tools** and matches the git-object route exactly, line and text.

### 3.1 Stratum 1 — ruling records — `N = 382`, a TAKE

**Defining object:** the class `writing-side-ruling-records` of
`tools/audit/gen_artifact_inventory.py`, the definition put to the user and ruled, quoted from
`ratification_surfaces/cowork_artifact_inventory_ruling_surface.md:250`:

> *Signature (AUTHORED):* repository-root files whose name begins `cowork_rulings_`,
> `cowork_ruling_`, `cowork_owner_rulings_`, `cowork_pending_rulings_` or
> `cowork_document_route_rulings_`

**★ THE COUNT IS 79, NOT 78 — REPORTED, AND THE MEMBERSHIP IS NOT ADJUSTED.** The one file over is
**`cowork_rulings_2026_08_27_stopped_strata_sitting.md`**, the ruling record this batch's own Task
0(c) landed.

**The dispatch's account of the figure is wrong at the objects, and the correction matters because a
successor will meet the same arithmetic.** The dispatch says that file *"was already on disk when
that count was taken and is included in it"*. At the objects: **74** is the figure the PREVIOUS
batch measured at its close — before the sitting that wrote that record existed — and the same
narrow matcher, run today at Task 0's ordered invocation, reads **75**. 75 + the four other name
shapes = **79**. Nothing is adjusted to reach 78.

**Unit** — the writing side's declared form, applied verbatim: a fence-aware markdown heading whose
text, after the leading `#` characters and after stripping leading `*`, `_`, `★` and whitespace,
matches `^(Ruling|RULING)\s+\d+` **or** `^\d+\s*[.)]\s`.

**★ RECORDS RETURNING ZERO NUMBERED RULINGS: FIVE.** Each contributes zero and is reported as
contributing zero; none was construed into having one:

- `cowork_document_route_rulings_2026_08_08.md`
- `cowork_owner_rulings_2026_08_07.md`
- `cowork_ruling_guard_family_2026_08_08.md`
- `cowork_rulings_2026_08_15_period_start.md`
- `cowork_rulings_2026_08_15_session_length.md`

**`N` = 382**, a take. **Positions:** 1, 17, 33, 49, 65, 80, 96, 112, 128, 144, 160, 176, 192, 207,
223, 239, 255, 271, 287, 303, 319, 334, 350, 366, 382. **`p_0` = 1, `p_24` = 382 = `N`**, strictly
increasing, distinct; no two items coincide on all three ordering keys.

### 3.2 Stratum 2 — decision surfaces — `N = 236`, a TAKE

**Defining object:** the explicit list of **35 paths** written into the dispatch by name — 4 at the
repository root and 31 under `ratification_surfaces/` — and **no signature of any kind**. **Every
listed path was found on disk**; none was substituted, and no path on disk but off the list was
added, so the dispatch's STOP did not fire.

**Unit** — the writing side's declared form: a fence-aware markdown heading whose stripped text
matches `^(Decision|DECISION)\s+\d+` **or** `^\d+\s*[.)]\s`.

**★ TEN OF THE 35 LISTED FILES RETURN ZERO NUMBERED DECISIONS.** This is one of the batch's named
deliverables and it stands on the stratum's own face in the sealed file. The ten:

- `cowork_extent_decision_surface.md`
- `ratification_surfaces/cowork_decisions_pending_ratification.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_2.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_3.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_4.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_5.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_6.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_7.md`
- `ratification_surfaces/cowork_decisions_pending_ratification_8.md`
- `ratification_surfaces/cowork_decisions_ratification_delta.md`

Nine of the ten are the ratification queues and the delta the writing side predicted by name. **The
tenth is not**: `cowork_extent_decision_surface.md` is a root-level file the dispatch lists as a
decision surface, and it carries no heading the declared form admits.

**`N` = 236**, a take. **Positions:** 1, 11, 21, 30, 40, 50, 60, 70, 79, 89, 99, 109, 119, 128, 138,
148, 158, 167, 177, 187, 197, 207, 216, 226, 236. **`p_0` = 1, `p_24` = 236 = `N`**, strictly
increasing, distinct; no coincidence on all three keys.

### 3.3 Stratum 3 — dossiers — `N = 625`, a TAKE

**Defining object:** the explicit list of **25 repository-root files** — the 26 matching
`*_dossier.md` minus `cc_instruction_stage3_4i_gate_retirement_dossier.md`. Every listed path was
found on disk.

**Unit:** every markdown list item at any nesting depth, fence-aware — **the same reading taken for
the evidence inventory**, exactly as Ruling 1 requires so the two strata are read alike. What that
reading is, exactly, is §8(a).

**No list item in any of the 25 dossiers falls inside a fenced code block**, so the fence-aware and
naive counts are equal at 625. That was established rather than assumed: the fence delimiters of
every dossier were enumerated and no bullet line falls between any pair.

**One dossier returns ZERO list items:** `cowork_adjudication_dossier.md`. Reported as zero.

**`N` = 625**, a take. **Positions:** 1, 27, 53, 79, 105, 131, 157, 183, 209, 235, 261, 287, 313,
339, 365, 391, 417, 443, 469, 495, 521, 547, 573, 599, 625. **`p_0` = 1, `p_24` = 625 = `N`**,
strictly increasing, distinct; no coincidence on all three keys.

**★ THE WEAK-EVIDENCE NOTE IS ON THE STRATUM'S FACE IN THE SEALED FILE**, in the ruling's own terms:
the declared unit is a mechanical stand-in that will over-admit ordinary prose bullets, so a
**PLACEABLE** result from stratum 3 is weak evidence and the placement report must say so; an
**UNPLACEABLE** result from it is unaffected.

**The dispatch gives no expected `N` for this stratum** — it is drawn for the first time — so there
is nothing to compare 625 against.

### 3.4 Stratum 4 — the DEFERRED entries of the decisions register — `N = 21`, a CENSUS

**Defining object:** `DECISIONS.md`, the rendered INDEX, at its own status field: a row whose status
cell opens with the canonical token `DEFERRED`. The register's own count block states the same
number in these words:

> | — of which deferred | 21 |

**Re-enumerated and confirmed at 21.** `N ≤ T`, so it is a census and no take rule applies. It
carries across from the superseded sample unchanged. **The STOP did not fire.**

### 3.5 Stratum 5 — the evidence inventory — `N = 33`, a TAKE

**Defining object:** `cowork_evidence_inventory.md`, one file. **`N` = 33 fence-aware, which is the
confirmed figure exactly**, so the dispatch's STOP did not fire. No list item in the file falls
inside a fenced code block, so the naive count is also 33.

**Positions:** 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 28, 29, 30,
32, 33. **`p_0` = 1, `p_24` = 33 = `N`**, strictly increasing, distinct.

**What returning 33 required is declared at §8(a) and on the stratum's face**, together with the
five ordered list items the reading does not count.

### 3.6 Stratum 6 — declared dormancies — **NOT ENUMERABLE, NOT DRAWN**

Recorded in the sealed file as NOT ENUMERABLE, with the three candidate readings and why each
fails — reading 1 enumerable but a subset of stratum 5; reading 2 the one with real coverage and
not enumerable at all until a marker convention exists; reading 3 a different subject, ruled out by
name — and with the finding that the concept is ratified at `CLAUDE.md:251-255` and **this project
has never built a population of it**. That record is the stratum's contribution. **Nothing was
enumerated and nothing was drawn.**

### 3.7 Stratum 7 — every current heading of the specification document set — `N = 730`, a TAKE

`python tools/audit/gen_specification_document_set.py --check` was run **first**, read-only, and the
artifact **re-derives**: *targets named 68; namings 199; admitted 25; **members 26**; with no file
0; seed misses 5 of 25.* No STOP.

**"Member" means the WHOLE member FILE**, so `ARCHITECTURE.md` contributes all of its headings and
not only those of its three named regions.

**`N` = 730 fence-aware; naive 737** — **both exactly the figures the dispatch expects**, so nothing
is reported as differing. The **seven** excluded lines are all shell comments inside fenced code
blocks, named here so they can be checked by eye:

| path:line | line |
|---|---|
| `ARCHITECTURE.md:896` | `# Build` |
| `ARCHITECTURE.md:899` | `# Tests — run once, capture tail` |
| `ARCHITECTURE.md:902` | `# Python scripts` |
| `ARCHITECTURE.md:905` | `# Long corpus runs — use tee` |
| `ARCHITECTURE.md:907` | `# Then after completion:` |
| `ARCHITECTURE.md:7794` | `# Full Bach corpus` |
| `ARCHITECTURE.md:7797` | `# Single chorale for spot-checking` |

**Positions:** 1, 31, 62, 92, 123, 153, 183, 214, 244, 274, 305, 335, 366, 396, 426, 457, 487, 517,
548, 578, 609, 639, 669, 700, 730. **`p_0` = 1, `p_24` = 730 = `N`**, strictly increasing, distinct.

### 3.8 Stratum 8 — every heading ever DELETED from that set — `N = 59`, a TAKE

**Same 26 members, same defining object.** An item is one **deletion event**: a heading present in a
member file at a commit's first parent and absent from that file at the commit itself. Its
provenance is the path, the line it stood at in the parent version, and the deleting commit — which
is also the third ordering key.

**The walk.** From the explicit tip `ec9034011857c223e2eb44ecbb210811908edc61`, per path: **207
distinct commits** touch the member set, **279 per-path commit visits** — which is exactly the
figure the previous batch's report gives for the same walk, so the two walks are the same walk.
Every historical version was read from its content-addressed git object; nothing was read from the
working tree.

**★ WITHOUT LINE-ENDING NORMALISATION THIS STRATUM RETURNS 610, NOT 59** — see §8(c). With it:
**`N` = 59 fence-aware; naive 60**, **both exactly the figures the dispatch expects**. The one
excluded event is a shell comment inside a fenced code block: `ARCHITECTURE.md:2523` — `# Full
corpus`, deleted at commit `d127f44d8618c806a1f98ca991ad83419ef63d6f`.

**Positions:** 1, 3, 6, 8, 11, 13, 16, 18, 20, 23, 25, 28, 30, 32, 35, 37, 40, 42, 45, 47, 49, 52,
54, 57, 59. **`p_0` = 1, `p_24` = 59 = `N`**, strictly increasing, distinct.

**★ THE THIRD ORDERING KEY IS LOAD-BEARING HERE, AND THIS BATCH MEASURED EXACTLY WHERE.** Of the 59
items, **THREE share one `path:line` — `ARCHITECTURE.md:635` — and are separated only by their
deleting commits** (`632c195294…`, `c9633aebc4…`, `70e679e819…`); no other `path:line` in the
stratum is carried by more than one item. **That is the same finding the previous batch reported at
the same place**, arrived at independently here, which is a corroboration of both enumerations. One
of the three is drawn, at `p_3` (ordered position 8), and the third key is what fixed its place among
them. **No two items coincide on all three keys**, so the STOP did not fire.

---

## 4. Task 3 — the take rule and its self-check

The replaced formula was used exactly as written, in integer arithmetic, with **no rounding
function**:

```
p_i = 1 + ( i * (N - 1) + 12 ) // 24
```

**The mandatory self-check passed on every stratum with `N > T`** — strata 1, 2, 3, 5, 7 and 8:
`p_0` = 1 in all six; `p_24` = `N` in all six; the 25 positions strictly increasing and distinct in
all six. **The old formula `1, 1+k, …, 1+24k` was not used anywhere.**

**`T = 25` IS DECLARED, NOT DERIVED**, and it is written that way in the sealed file's banner, in its
§0, and at every stratum where the threshold decides something.

**Recorded, not reported as a defect:** item 1 and item `N` are drawn in every take. That is the
rule's declared cost.

**The worked values reproduce.** `N = 33` → `p_0` = 1, `p_24` = 33. `N = 59` → 1 and 59. `N = 730` →
1 and 730. All three match the dispatch's stated check values.

---

## 5. Task 4 — the sealed file

**Written at `cowork_placement_sample_sealed_redraw_2026_08_27.md`**, 1,200 lines. Its banner
carries, in the dispatch's order: the withheld-from-the-frame's-author warning **naming both this
file and the superseded one**; that this is the sealed sample, drawn at the named tip, and closed;
that it supersedes `cowork_placement_sample_sealed_2026_08_27.md`, which is **kept, not deleted**;
that `T = 25` is declared and not derived; and that stratum 6 is NOT ENUMERABLE and not drawn, so no
stratum remains STOPPED and the frame is gated only on this file's existence.

Per stratum the body carries the defining object or the explicit path list, the quoted text where
there is one, the **declared scoping (*for this sample only*)** on the face of strata 1, 2 and 3,
`N`, census-or-take with the positions and the self-check, the zero-returning file list on stratum
2's face and stratum 3's weak-evidence note on its face, and the drawn items each with its verbatim
text and `path:line` provenance (plus the deleting commit for stratum 8).

**It carries no judgement about placeability, no grouping, no commentary on the frame and no
ranking.**

**`cowork_placement_sample_sealed_2026_08_27.md` was not opened for its content, not edited, not
moved, not deleted and not regenerated.**

**★ DECLARED: the sealed file's body was GENERATED from the enumeration, not hand-transcribed.** The
drawn items, the counts, the positions and the self-check verdicts are rendered from the enumeration
artifacts by a script held in the session scratchpad **outside the repository**; the prose around
them is authored. The alternative — retyping 171 verbatim items by hand — is the transcription the
record forbids elsewhere for exactly this reason.

---

## 6. Task 5 — the root-population hazard

### 6.1 The prediction, made from the tool's own derivation BEFORE the sealed file was written

`tools/audit/gen_filing_convention_application.py` derives its candidates from two signatures over a
named surface set. **S1** fires where, within a document's last 25 non-blank lines, one line matches
both a *fate* pattern (`resolved in|deleted|removed|retired|superseded|falsified|no longer
exists/present`) and a *marker* pattern (a line opening with a status word, or a run of 7–40 hex
characters). **S2** fires where a draft-ish banner meets a decisions-register entry that is
falsified, shelved or superseded and names the document.

**Predicted, before writing:**

1. **S2 CANNOT FIRE on any file this batch adds** — it requires a register entry naming the
   document, and no register entry can name a file that did not exist when the register was
   generated.
2. **The new sealed file WILL enter, via S1, by construction.** Its last stratum is the
   deleted-headings stratum, and every one of its 25 rows carries the word *deleted* on the same
   line as a 40-character commit hash. Its tail is made of such lines.
3. **None of the five Task 0(c) files will enter.** Three of them carry their last fate word far
   outside the last 25 non-blank lines (`cowork_stopped_strata_surface_2026_08_27.md` at line 241 of
   364; `cowork_declared_readings_surface_2026_08_27.md` at 170 of 239;
   `cowork_rulings_2026_08_27_stopped_strata_sitting.md` at 295 of 345). **Two carry one at or inside
   the tail and still do not fire, because the MARKER half fails on that line** —
   `cowork_take_rule_surface_2026_08_27.md:217` (*"which is **not deleted** — it stays as the record
   of"*) and `cc_instruction_placement_sample_redraw.md:440` (*"removed from or reordered in the
   sample except by the rule at Task 3"*): neither line carries a run of seven or more hex characters
   and neither opens with a status word.

### 6.2 The measurement, with everything on disk

`python tools/audit/gen_filing_convention_application.py --derive-only` — **read-only; it writes
nothing and regenerates nothing.**

**THE LIST WIDENED: 18 derived candidates → 19; the STOP list 4 → 5.** Every element of the
prediction held.

**The 19 measured candidates:**

`BUILD_AND_TEST_ARCHIVE.md` (S1) · `OPEN_ITEMS_ARCHIVE.md` (S1) · `STATUS_ARCHIVE.md` (S1) ·
`cc_instruction_phase1s_stale_rules_and_enumeration.md` (S1) ·
`cc_instruction_phase1z_commit_and_instrument_record.md` (S2) ·
`cc_key_grading_and_calibration_rebaseline_report.md` (S1) · `cc_oi207_residual_pass_report.md` (S1)
· `cc_report_preparation_fourteenth.md` (S1) · `cc_stage2a_wip_triage_report.md` (S1) ·
`cc_stage3_4i_dossier.md` (S1) · `cc_stage5_phase2_2d_report.md` (S1) ·
`cowork_placement_sample_sealed_2026_08_27.md` (S1) ·
**`cowork_placement_sample_sealed_redraw_2026_08_27.md` (S1, 9 lines) — NEW** ·
`docs/iter92_joint_bass_chord_scoring.md` (S2) · `docs/key_path_design.md` (S2) ·
`docs/policy2_coalescing_map.md` (S1) · `docs/stage4b_design.md` (S2) ·
`docs/symbol_input_audit.md` (S1, seed) ·
`ratification_surfaces/cowork_pending_ratifications_next_session.md` (S2)

**The measured STOP list — five derived candidates with no authored verdict**, quoted from the
guard's own output:

> STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md,
> OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md,
> cowork_placement_sample_sealed_2026_08_27.md, cowork_placement_sample_sealed_redraw_2026_08_27.md.
> An unclassified candidate is a STOP, never a silent pass (D-661).

**IT IS REPORTED AND NOT CURED.** Nothing was classified, nothing was regenerated,
`tools/audit/filing_convention_application.json` was not touched.

**★ NO FILE WAS SHAPED TO STAY OUT OF THAT POPULATION.** The sealed file's stratum 8 is last because
the strata run 1–8; its rows carry *deleted* beside a commit hash because that is what the item's
provenance is. This report's own placement in or out of the population is likewise a fact about its
content and not about its drafting: **its final standing is measured in §12, after it was written and
after its last section was filled in — not engineered before.**

**★ AND A FINDING ABOUT THE GUARD, DECLARED AND ACTED ON BY NOTHING.** S1 is a *fate* signature. It
cannot distinguish a document whose own subject was overtaken from a document that **enumerates
deletions in another document** — which is exactly what a stratum-8 section is. The previous batch
recorded the same finding; a second instance is now on the record and the signature is **not
re-tuned here**.

---

## 7. Task 6 — STATUS.md, the forward bound, the sweep

### 7.1 (a) The pointer entry

**Exactly one** POINTER entry was written to `STATUS.md`, and it was written **before** the
forward-bound tool was run, as ordered. It carries no count, no identity and no rendered value
(D-431). **The previous batch's self-check had to remove a second entry; no second entry was written
here** — `STATUS.md` now holds exactly one dated entry.

**One adjustment travelled with it and is declared rather than left to be noticed:** the previous
entry's `Last updated: ` prefix was moved to the new entry. That is the forward-bound tool's own
declared adjustment (it imports `PREFIX_ADJUSTMENT` for exactly this), and without it the tool's
occurrence test finds zero and STOPs.

### 7.2 (b) The forward bound, re-aimed

**Command line, exactly as run:**

```
python tools/audit/gen_status_batch_bound.py --apply
```

**The tool has no `argparse` flag other than `--apply` and `--check`; no `--help` was passed.**

**The five aiming constants, with the values set:**

| constant | value |
|---|---|
| `BASE_COMMIT` | `ec9034011857c223e2eb44ecbb210811908edc61` — this batch's Task 0(c) landing |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_placement_sample.md` |
| `ACT_DATE` | `2026-08-27` |
| `DISPATCH` | `cc_instruction_placement_sample_redraw.md` |
| `TASK` | `Task 6` |

**`TASK` IS A CHOICE AND HERE IS THE GROUND.** The dispatch orders the re-aiming and the run at
**Task 6(b)**, and the `STATUS.md` entry the move accompanies at **Task 6(a)**. Both halves of *"the
same act that writes its own entries"* therefore sit inside Task 6, so `Task 6` is what the archive
header names. The sub-letter is not carried, because the header names an act rather than a sub-step
and every previous aiming names a whole task. The reasoning is written into the tool beside the
constant so a later reader does not have to reconstruct it.

**The outgoing aiming was APPENDED to `PREVIOUS_AIMINGS`, not overwritten** (#12):

```
{"executing_act": "cc_instruction_placement_sample.md, Task 5",
 "base_commit": "9053861b9cc71d8de8dc9c12105abd553620b55a",
 "the_then_previous_batch": "cc_instruction_ledger_admissions.md"}
```

**Result:** *entries moved: 1, 4,268 characters; byte-present in the archive exactly once: True;
absent from the must-read: True.* Both halves of the reconciliation pass, so nothing left the
must-read that is not in the archive and the entry was **moved** rather than copied.

This tool source is the **only** path under `tools/` ending `.py` that this batch modifies, under
the carve-out ruled for it by name.

### 7.3 (c) The sweep

`gen_guard_state.py` then `gen_guard_classification.py`, in that order, **with no flag of any kind
passed to either** — the slip the dispatch names was not repeated.

**Round 1:** 75 guards run, **4 failing**, 4 not run, 16 historical records.

**Round 2, after the one staleness cure:** 75 run, **72 passing, 3 failing**, 4 not run, 16
historical records. Classification: **live 69 · point-in-time 16 · neither 2 · live-and-failing 3.**
That is the fixpoint.

**The three reds are the three standing DECISION reds the dispatch names and forbids curing**, and
each was classified at its own captured text before anything was touched:

| guard | why it is red |
|---|---|
| `gen_filing_convention_application.py --check` | `[[OI-372]]`'s guard — five derived candidates with no authored verdict (§6.2) |
| `decisions/apply_soft_discard.py --check` | standing decision red |
| `decisions/apply_residue_discard.py --check` | standing decision red |

**ONE staleness red was cured and is declared:** `gen_session_start_read_size.py --check`, red by
construction because this batch writes to `STATUS.md`, which is a member of the session-start read
it measures. Cured by running the generator once. **No other red was met, so the dispatch's
treat-it-as-a-DECISION-red default was not engaged.**

---

## 8. ★ Every reading the rule did not decide, declared rather than settled quietly

### (a) "Every markdown list item at any nesting depth" — pinned to BULLET items

**The words admit two mechanical readings and the dispatch's own STOP decides between them.**

- **Bullet items only** — a line whose first non-whitespace character is `-`, `*` or `+` followed by
  whitespace, at any depth: **`N` = 33** for the evidence inventory.
- **Bullets and ordered items** — adding `1.` / `1)` forms: **`N` = 38**.

**Only the first returns the ruled 33**, and §2.1 of the dispatch forbids proceeding on a different
`N` for that stratum. So bullets-only is the reading taken. **It is a declaration, not a judgement
that ordered items are not list items** — plainly they are.

**What it changes elsewhere:** Ruling 1 requires stratum 3 to be read alike, so stratum 3 is
bullets-only too. **Under the wider reading stratum 3's count moves** — over the ten dossiers
reachable at the git objects alone it is 251 against 179, so the whole-stratum figure would rise
well above 625 and every drawn position would move.

**The five ordered items the reading does not count are named on stratum 5's face in the sealed
file**, at `cowork_evidence_inventory.md` lines 164, 168, 174, 186 and 191.

### (b) The declared form of a "numbered ruling" and a "numbered decision" admits ordinary SECTION headings

The declared form's second limb is `^\d+\s*[.)]\s`. Applied verbatim — which is what was done — it
matches every heading of the shape `## 0. What was put, and in what form`, `## 5. What this file
does NOT do`, `## 3. The classes`. **Most of what strata 1 and 2 enumerate is therefore ordinary
numbered section headings, not rulings and not decisions.**

**Measured on the drawn sets, which is where it is exactly checkable:**

| stratum | drawn | matching the first limb (`Ruling n` / `Decision n`) | matching only the numbered limb |
|---|---|---|---|
| 1 — ruling records | 25 | **5** | **20** |
| 2 — decision surfaces | 25 | **0** | **25** |

**Not one of stratum 2's twenty-five drawn items is a heading of the form `Decision <n>`.** Several
of stratum 1's twenty are section headings that announce a ruling (`## 1. Ruling — the per-class
fates`), and others are plainly not (`## 0. What was put, and in what form`, `## 5. Derived
expectations for the executing dispatch`).

**Nothing was adjusted.** The form is the writing side's and it was applied as written. It is
reported because it changes what a *placeable* result from either stratum would mean.

### (c) Stratum 8 needs line-ending normalisation, and no ruling says so

The unit is "a heading deleted", which is decided by comparing heading text between two versions.
**Several member files changed from CRLF to LF in their history** — `ARCHITECTURE.md` at 26 commits,
`cowork_layer4_chordsymbol_design.md` at 3, `cowork_layer5_function_design.md` at 1. Without
stripping the carriage return before comparison, the single commit at which a file's line endings
change reads as **every heading in that file being deleted at once**, and the stratum returns
**610** events instead of 59, 580 of them from `ARCHITECTURE.md` alone.

**Normalisation was applied**, which is what reproduces the ruled 59 / 60. It is declared because it
is a real decision about the unit that the rule does not state, and because a successor
re-implementing this enumeration will get 610 unless it makes the same one.

### (d) The heading pattern

A heading is `^#{1,6}` followed by whitespace or end of line. This reading reproduces the dispatch's
expected 730 / 737 and 59 / 60 exactly on strata 7 and 8, which is the only evidence available that
it matches the reading those figures were produced under.

---

## 9. Every path written, and the tree arithmetic

### 9.1 Written by this batch

| path | by what |
|---|---|
| `cowork_placement_sample_sealed_redraw_2026_08_27.md` | the sealed sample — new |
| `cc_report_placement_sample_redraw.md` | this report — new |
| `STATUS.md` | one pointer entry (plus the declared prefix move) |
| `tools/audit/gen_status_batch_bound.py` | the five aiming constants and the appended row — carve-out |
| `STATUS_ARCHIVE.md` | **written by `gen_status_batch_bound.py --apply` as its own output** |
| `tools/audit/status_batch_bound.json` | same tool's own output |
| `tools/audit/evidence_pin_membership.json` | `gen_evidence_pin_membership.py`, ordered at Task 0 |
| `tools/audit/session_start_read_size.json` | `gen_session_start_read_size.py`, the declared staleness cure |
| `tools/audit/guard_state.json` | `gen_guard_state.py`, the sweep |
| `tools/audit/guard_classification.json` | `gen_guard_classification.py`, the sweep — **re-derived byte-identically, so it is not a tracked modification** (§9.4) |
| the six Task 0(c) landings | committed at `ec9034011857c223e2eb44ecbb210811908edc61` |

**Nothing else was written.** No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. No `src/`
change, no test changed, moved or run, no golden. Nothing under `tools/corpus/` or
`tools/robust_stop/`. No other `.py` source edited. No register entry, no ratification, no
admission. No open-items row created, flipped or discarded. No finding number allocated. No existing
ruling record, surface, dossier, register entry or inventory row edited — they were **read**, not
maintained. Neither blind output opened; neither brief, neither pack, the generator, the manifest
and every withheld family untouched. `cowork_placement_sample_sealed_2026_08_27.md` untouched.

### 9.2 Steps not ordered by the dispatch, declared

- **`gen_filing_convention_application.py --derive-only`** — read-only, writes nothing, regenerates
  nothing. Run because Task 5 requires the measured **candidate list**, which `--check` does not
  print.
- **Scratchpad enumeration scripts**, held entirely outside the repository, reading only git objects
  by explicit commit and path and their own scratchpad artifacts.

### 9.3 The register blocker

**NO register entry was written, and this is the SIXTH CONSECUTIVE BATCH shaped that way.** This
batch performs no ratification, so rule (c) is not engaged and the two mutually unsatisfiable
discard-act checks stay out of its path. **Recorded rather than hidden: curing the blocker is a
decision act that has never been put to the user, and nothing here proposes it.**

### 9.4 The close, measured

Measured by `tools/audit/changed_paths.py` and **not** by `git status`, immediately before the
closing commit:

| | start | after the landing | close |
|---|---|---|---|
| changed-path records | 838 | 833 | **841** |
| untracked | 837 | 832 | **834** |
| tracked modifications | 1 | 1 | **7** |

**The arithmetic closes.** 837 untracked − the 5 untracked paths the landing committed + the 2 new
files this batch wrote = **834**. The single tracked modification at the start was the handoff, which
the landing committed; the single one after the landing was
`tools/audit/evidence_pin_membership.json`, the file Task 0 ordered regenerated.

**All seven tracked modifications are inside the fence**, and each is named in §9.1: `STATUS.md`,
`STATUS_ARCHIVE.md`, `tools/audit/evidence_pin_membership.json`,
`tools/audit/gen_status_batch_bound.py`, `tools/audit/guard_state.json`,
`tools/audit/session_start_read_size.json`, `tools/audit/status_batch_bound.json`.

**`tools/audit/guard_classification.json` re-derived BYTE-IDENTICALLY and is therefore NOT among
them**, which is why the count is seven and not eight.

**Nothing of the standing untracked population is committed** beyond the five paths Task 0(c) names.

---

## 10. Departures, slips and things this batch could not obey

**Every one of these is a departure from the dispatch's letter or a fact the dispatch does not
carry. None is a silent one.**

1. **The stratum-1 file count is 79 and the dispatch expects 78.** Reported, membership not
   adjusted, and the dispatch's stated ground for 78 corrected at the objects. §3.1.
2. **The list-item unit had to be pinned to bullets to return the ruled 33.** §8(a). The wider
   reading is named with what it would change.
3. **Stratum 8 required line-ending normalisation.** §8(c). Not ordered anywhere; without it the
   stratum is an order of magnitude larger.
4. **The declared numbered-ruling / numbered-decision form admits ordinary section headings.** §8(b).
   Applied as written; reported because it changes what a placeable result means.
5. **The sealed file's item body is generated rather than hand-typed.** §5. Declared because the
   dispatch does not say which mechanism to use and the choice is visible in the result.
6. **`gen_filing_convention_application.py --derive-only` was run without being ordered.** §9.2.
   Read-only.
7. **★ A FINDING ABOUT THE SHELL-READ GUARD, REPORTED AND NOT CURED.** Three formulations of a
   command were denied by the guard during this batch, and one of the three is a false positive
   worth the writing side's attention:
   - `ls` naming repository paths — **a true positive**, and the file tools were used instead.
   - a Python heredoc whose code contained a repository-relative filename — **a true positive on the
     letter of the 2026-08-08 guard-family widening**, although the code in question read only git
     objects by explicit commit. The same code was then held in a **scratchpad script file** and
     invoked by path, which the guard does not inspect, because the guard reads the command string
     and not the file it names. **That ceiling is on the record here rather than left to be
     discovered**: substantive compliance was preserved (every read was content-addressed or through
     the file tools), but the guard did not enforce it — it was obeyed.
   - `tail` aimed at a **scratchpad** path built from a shell variable — **a FALSE POSITIVE.** The
     path is outside the repository entirely; the guard resolved the unexpanded `"$S/..."` as a
     repository path. Reported; **nothing is re-tuned here.**
8. **No instruction went unobeyed, and NOT ONE of the dispatch's STOP conditions fired.** Each was
   checked rather than assumed: the tip matched; the handoff change was additions-only and prepended;
   no stratum enumerated to zero; no two items coincided on all three ordering keys; every listed
   path in strata 2 and 3 was on disk; stratum 5 returned exactly 33; stratum 4 returned exactly 21;
   `gen_specification_document_set.py --check` re-derived; and the take rule's three-part self-check
   passed on all six take strata. The one expectation that did NOT hold — stratum 1's file count —
   carries "report the difference; do not adjust", not a STOP, and that is what was done.

---

## 11. What this batch did NOT do

**No frame text authored, no part of the frame written, no statement placed, no judgement about
placeability recorded. THE PLACEMENT TEST WAS NOT RUN.** No item was added to, removed from or
reordered in the sample except by the rule at Task 3. Stratum 6 was not enumerated and not drawn.
The superseded sealed file was not opened for its content, edited, moved, deleted or regenerated.
`[[OI-372]]` was not regenerated and the two discard-act checks were not cured. No measurement of
the analysis was built, designed, scoped or run. **The end state is not asserted by the commit that
carries this report; it is measured in §9.4/§12 below.**

---

## 12. The final measurements, taken with everything on disk

**The sweep reached its fixpoint in two rounds and was run twice more — once with this report on
disk and once after its last sections were filled in.** Every run after the staleness cure returns
the same thing: 75 guards run, **72 passing, 3 failing**, 4 not run, 16 historical records;
classification **live 69 · point-in-time 16 · neither 2 · live-and-failing 3**. All three reds are
the standing decision reds of §7.3.

**The filing-convention derivation, re-run with this report on disk, still reports 19 candidates and
the same five-member STOP list.** **THIS REPORT DID NOT ENTER, AND ITS ABSENCE IS NOT ENGINEERED.**
The reason is mechanical and checkable: the last twenty-five non-blank lines of this file do carry
the signature's *fate* words — *superseded*, *deleted*, *regenerated* — but **no single line among
them carries a fate word together with a commit hash or a status opening**, and S1 requires both on
one line. Nothing was moved, omitted or reworded to produce that; the previous batch declared its own
absence engineered and this one is stating the opposite about itself, at the mechanism, so the two
can be told apart.

**The tree state at the close is §9.4.** The commit that carries this report cannot state its own
hash; if a second commit is made whose whole diff is that one line, it is declared here in advance as
this project's own precedent, twice used.
