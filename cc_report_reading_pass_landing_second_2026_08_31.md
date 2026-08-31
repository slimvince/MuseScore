# CC report — the reading-pass landing (SECOND writing): Rulings 2 and 3 executed, the pass's evidence base in git

> **Dispatch:** `cc_instruction_reading_pass_landing_second_2026_08_31.md`, pinned before it was read
> at blob `a06bfc2a392267428f0b1182d67035b2ff0b14cc`; every later read taken from that object.
>
> **The first writing** (`cc_instruction_reading_pass_landing_2026_08_31.md`) stopped at Task 0 and
> wrote nothing. It and its stop report are landed by this batch as record and were never run.

## Outcome

**Tasks 0 through 5 performed. No STOP.** The two ruled `FRAMEWORK.md` corrections are executed and
proven additions-plus-preserved-former-wording at the objects; the reading pass's whole evidence base
is tracked; the research-paper subfolder is split by kind with the ignore rule widened and verified
both ways; the evidence-pin membership artifact is regenerated and its prediction held exactly.

**Four declared departures are in §7. Nothing was absorbed silently.**

---

## 1. Task 0 — pinned first, then established

| what | value |
|---|---|
| this dispatch, pinned before reading | `a06bfc2a392267428f0b1182d67035b2ff0b14cc` |
| `master` | `b8e738448ea061a2212d82de454e46a55ecf6f8f` |
| `origin/master` | `b8e738448ea061a2212d82de454e46a55ecf6f8f` |

**Identical — no STOP on step 1.** Established again at the object rather than carried from the first
writing, as the dispatch requires.

**The guard set** — `python tools/audit/gen_guard_state.py --check`, the full set, run **before the
first act**; the runner exited 1 on drift against a committed artifact that records eight:

**75 run, 9 failing, 4 not run, 16 historical records. Exactly the declared nine, and no tenth.** The
three long-known (`gen_filing_convention_application.py`, `decisions/apply_soft_discard.py`,
`decisions/apply_residue_discard.py`); the five stop-reported ordered-edit reds
(`gen_artifact_inventory_surface.py`, `gen_test_construction_evidence.py`,
`gen_retirement_caller_check.py`, `gen_derivation_boot_pack.py`,
`decisions/gen_cluster_dispositions.py --verify`); and the ninth,
`gen_evidence_pin_membership.py --check`. **None was repaired.**

**The tree enumeration** (`python tools/audit/changed_paths.py`; a raw `git status` was denied by the
shell-read guard and the denial was obeyed, not routed around — **D-253**):

| | |
|---|---|
| records | **852** |
| tracked modifications | **0** |
| untracked | **852** |

The single difference from the first writing's 851 is this dispatch's own file.

**Pins re-verified before use rather than carried** — the ruling record, both decision surfaces, the
V4 STOP memo and the first writing all hash to the values the first writing pinned, and
`FRAMEWORK.md` in the working tree was byte-identical to its blob at HEAD, so Task 1's difference is
measured against an unmoved base.

---

## 2. Task 1 — the two ruled corrections to `FRAMEWORK.md`

Content taken from `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3a and §3b **at the
object**, and from the surfaces each ruling names — not from the dispatch's paraphrase.

| what | blob |
|---|---|
| `FRAMEWORK.md` before | `41ab164f4eaf6240fafc45b982d1c4b6ae67f77a` |
| `FRAMEWORK.md` after | `0b4a96dbc1ab8f94af3611010233c952d9b54e72` |
| blob-to-blob `--numstat` | **54 insertions, 5 deletions** |

### 2.1 The additions-only proof, and what the five deletion lines are

The dispatch permits a deletion line **only** where a ruling's preservation form requires the old
text to move rather than vanish, and then requires the moved text shown intact at its new place.
**Both conditions are met, and every deleted word is accounted for:**

- **Ruling 2 — two deleted lines.** One carried the clause that was wrong; it is shown **intact** in
  the preservation block as *"harmonic change was counted at 71.5% of tactus beats against 2.4% of
  the lowest metrical level"*. The remainder of those two lines — the six-point ablation half — is
  **not** preserved in a block because it did not move: it survives in the corrected sentence itself,
  word for word, re-wrapped only.
- **Ruling 3 — three deleted lines.** The opening of the first (`containing a different number of
  chords. *Ground:* the ground truth's own form; and `) survives **verbatim in place** at the head of
  the new text. The rest — the whole of ground 2 — is shown **intact** in that clause's preservation
  block, **with its own `**above**` emphasis markers**, and the block says so.

**No other line of `FRAMEWORK.md` changed.** The two hunks are at §5 (L1's charter) and §9 (the
design points) and nowhere else.

### 2.2 What each correction says

**Ruling 2 (V4), Option A.** The clause now reads the primary's own three-level gradient — 71.5% of
the strongest-level beats, 22.3% of tactus beats, 2.4% of the level below, cited to Temperley 2009,
Table 1, Kostka–Payne corpus. The preservation block names the ruling, the STOP memo
(`reading_pass/stop_v4_divergence_2026_08_30.md`) and the decision surface, states why the clause was
false at its primary, and records that the design point is untouched and its ground sharpened.

**Option B is declined and its content is NOT in the charter.** The block records the decline and
points at where the further finding lives; **it does not restate the finding**, which is what the
ruling forbids.

**Ruling 3 (DP-K's second ground), Option B.** Ground 2 is narrowed to what its primary supports —
one study of popular-music audio, its evaluated systems about ten percent above the
annotator-pairwise agreement that same study measured — with the second study recorded beside it and
**no contradiction asserted between them**. The two on-domain findings are added as further grounds,
**each carrying the read grade it was obtained at**: the dual-key-reading principle at *DECLARED
PARTIAL, chapter level* (Feisthauer 2021, the Lille thesis), and the divergence between annotation
traditions at *RELAYED* (Nápoles López, Feisthauer, Levé & Fujinaga 2020). **DP-K is not reopened and
its first ground is untouched**, and the block says so.

### 2.3 ★ THE THIRD INSTANCE — REPORTED AS A NEW USER ITEM, NOT TOUCHED

The misstated metric-strength figure appears at **three** places in `FRAMEWORK.md`. Ruling 2 reaches
one.

| where | what it is | disposition |
|---|---|---|
| §5, L1, *"Why metric strength earns its place"* | the ruled clause | **corrected** |
| **§14.1, *"What this framework builds on"*** | a source-family summary line — *"and for the finding that automatic systems now score above human-human agreement"* sits in the same list, and the metrical-constraint bullet immediately above it | **★ NEW USER ITEM — not edited** |
| Appendix B, S5 | inside the first-stage draft, preserved *"whole and unedited"* | **correctly untouched by construction** |

**The §14.1 instance is put to the user as a new item.** It is a live governing line, not a preserved
draft, and neither ruling reaches it; the bounds forbid editing it. **The same question arises for
DP-K**: its ground-2 wording also appears at §14.1 and twice in Appendix B, and only the §9 instance
was ruled. *This report takes no view on whether the §14.1 lines should be corrected — that is a
ruling, and it is not this session's.*

---

## 3. Task 2 — the untracked population, classified in full

**Every one of the 852 untracked records is classified below.** The classification was completed
before anything was added.

| class | what | records | disposition |
|---|---|---|---|
| **(i)** | `reading_pass/` — population, additions, continuation, the V4 STOP memo, 20 extracts, 8 second-pass extracts, 8 cross-checks | 40 files | **TRACKED** |
| **(i)** | `ratification_surfaces/` — the five decision surfaces of 2026-08-31 | 5 | **TRACKED** |
| **(i)** | the findings surface, both commissions, both ruling records | 5 | **TRACKED** |
| **(i)** | both writings of this dispatch, and the first writing's stop report | 3 | **TRACKED** |
| **(ii)** | the four staged handoff entries, **as files** | 4 | **TRACKED, not prepended, not deleted** |
| **(iii)** | `docs/research_papers/reading_pass_2026_08/` — the markdown content records | 17 | **TRACKED** |
| **(iii)** | `docs/research_papers/reading_pass_2026_08/` — the paper binary | 1 | **NOT tracked; now ignored** |
| **(iv)** | **outside the dispatch's three classes** — see below | 777 | **untouched** |

**Staged total: 81 records — 74 additions and 7 modifications, with no `.pdf` among them**, measured
with `changed_paths.py --staged` rather than asserted.

### 3.1 ★ CLASS (iv) — DECLARED, BECAUSE THE DISPATCH'S THREE CLASSES DO NOT REACH IT

The dispatch says *"classify every untracked path"* and gives three classes. **777 untracked records
fall outside all three** and are left exactly as found: the long-standing `cc_*.md` reports and
dispatches at the repository root, the whole of `scratch_artifacts/`, and the two PDFs under
`external resarch summary/` — a folder this batch is barred from opening, renaming or moving. **None
of them is a product of the reading pass.** They are declared here rather than silently omitted from
a classification the dispatch asked to be complete.

### 3.2 The redistribution convention, established at the objects

| question | answer | how established |
|---|---|---|
| are the library PDFs tracked at HEAD? | **no** — the only tracked entries under `docs/research_papers/` are `BIBLIOGRAPHY.md` and `README.md`; **zero** `.pdf` | `git ls-tree -r b8e738448e… docs/research_papers/` |
| by what mechanism are they kept out? | a **`.gitignore` entry**, under the comment naming the private repository as their git home, *"never this public fork"* | `git check-ignore -v` on library PDFs |
| did it reach the new subfolder? | **no** — a single `*` does not cross `/` | `git check-ignore -v` returned no match for anything in the subfolder |

### 3.3 The `.gitignore` amendment — the only one made, verified BOTH ways

`docs/research_papers/*.pdf` → `docs/research_papers/**/*.pdf`, the existing comment kept and a
dated note added saying what was widened and why. `**/` matches zero or more directories, so the
library's own top level is covered exactly as before. **No other rule was added or changed.**

| direction | result |
|---|---|
| **must be ignored** — two library PDFs and the subfolder's Saarland PDF | all three matched, by the amended rule |
| **must NOT be ignored** — all 17 subfolder records, all of `reading_pass/`, the five surfaces, the root records, the four handoff entries, `FRAMEWORK.md`, `.gitignore` | **no match for any** |

**Nothing the batch means to track became ignored**, and no `.pdf` reached the index.

### 3.4 ★ THE KIND CHECK ON THE FIFTEEN UNREAD RECORDS (#19)

The writing side read two of the seventeen. **All seventeen were measured mechanically, from their
git objects**, never from the working tree.

**The measure, stated so the verdict is checkable rather than asserted.** For each record: total
characters; the share of characters lying inside a quotation span (a run between paired straight or
curly double quotes, on one line); and the longest single such span. **A record whose bulk is our own
prose with short attributed quotations has a low quoted share and no long span; a substantial
reproduction shows the opposite on at least one.**

| | measured across all seventeen |
|---|---|
| length | 1,771 – 8,864 characters |
| quoted share | **1.3% – 8.1%** |
| longest single quotation | **140 characters**, across all seventeen |
| carrying a retrieval / read-grade header in their first 20 lines | **17 of 17** |

**So no record is less than 91.9% our own prose, and no quotation anywhere runs past 140 characters.
None is substantially a reproduction; no STOP.**

**The measure's own weakness, stated with it:** a reproduction pasted *without* quote marks would
score zero on both counts, so the numbers alone cannot settle it. **The unquoted bulk was therefore
also sampled by eye** — the longest record and the highest-quoted-share record read whole or at
length, both plainly our own compressed summary prose under a retrieval header, plus the one the
first writing had already read whole. *This is a sample, and it is reported as one.*

### 3.5 The artifact-inventory check after the additions — reported, not repaired

Run after the additions. **Its result is in §6 with the end-state guard run**, unrepaired, and the
signature table was not touched.

---

## 4. Task 3 — the evidence-pin membership artifact, regenerated

| what | blob |
|---|---|
| before | `fd5c2e980779df4f7ad7ef7c5406bcc46cf278e6` |
| after | `fb3a00be268401e5386954cc3c410c9c827539df` |
| blob-to-blob `--numstat` | 3 insertions, 1 deletion |

**The prediction P-3 was recorded before the act and held exactly.** The whole difference is:

- `"ruling_records_read"` 83 → 85;
- exactly two ruling records appear — `cowork_rulings_2026_08_30_detail_phase_opening_sitting.md`
  and `cowork_rulings_2026_08_31_decision_surface_sitting.md`.

**Nothing else moved: no member added or removed, no member's pin state changed, no other field.**
The tool did not halt. This is a regeneration of a generated surface whose own source population
changed — not a repair, and not a hand edit.

---

## 5. Task 5's other half — `STATUS.md` and its forward bound

The `STATUS.md` entry is a **POINTER** per the OI-222 convention: no count, no identity and no
rendered value is restated in it (**D-431**).

**The forward bound was maintained** by `tools/audit/gen_status_batch_bound.py --apply`, re-aimed to
this batch. Its `--check` re-derives: **4 entries moved, byte-present in the archive exactly once,
absent from the must-read** — both directions proven, not asserted.

**Its STOP fired once, correctly, and was obeyed rather than worked around.** The first apply halted
with *"the entry at base line 8 occurs 0 time(s) in the live STATUS.md"*. The cause was read at the
tool's own source: the outgoing newest entry must lose the `Last updated: ` prefix as the incoming
one takes it — the ONE declared textual adjustment the mechanism carries. That adjustment was made
and the apply then succeeded. **No entry was retyped at any point.**

---

## 6. The end state — the guard set re-run

*Completed in the follow-up commit; see §7 departure 4.*

---

## 7. Declared departures — four

1. **The first writing's stop report did not exist and was authored by this session.** Task 2(i)
   names it as a thing to track. It did not exist, because the first writing stopped at Task 0 and
   wrote nothing — which was that writing behaving correctly. It is written now as
   `cc_report_reading_pass_landing_2026_08_31.md`, **carrying a banner that says when it was written
   and by whom**, so it is not mistaken for a contemporaneous record. Its content is what that run
   measured and delivered.

2. **A tool source WAS edited — the forward bound's per-batch re-aiming — and it is not a breach.**
   The standing bounds forbid editing any tool source. Task 5 orders the forward bound maintained,
   and that tool cannot be aimed at a new batch except by editing four authored constants and
   appending a row to its list of previous aimings. **The user has already ruled this exact conflict:
   Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md` names the re-aiming a
   *"named carve-out from the no-tool-source-edit bar in this and future dispatches"*, taken
   precisely so the conflict could not recur.** Two authored comments beside those constants were
   corrected in the same act because the re-aiming made them state something false about this batch
   (#10). **No mechanism changed.**

3. **Class (iv) — 777 untracked records outside the dispatch's three classes**, declared at §3.1 and
   left untouched.

4. **The report's end-state section is completed in a follow-up commit.** The dispatch orders one
   commit. The end-state guard run and the commit identities cannot exist until the commit does, so
   the SHA table and §6 are completed in a small second commit that touches this report only — the
   construction the phase-close batch used for the same reason.

---

## 8. What this batch did NOT do

No `src/` change. **No test changed, moved or run.** No golden refreshed, no build, **no measurement
of the analysis**, nothing under `tools/corpus/` or `tools/robust_stop/`. No specification derived or
amended and no design taken. **No open-items row created, flipped or discarded; no decisions-register
entry written and no `D-NNN` allocated** — the rule-(c) suspension stands. **No guard failure
repaired.** `FRAMEWORK.md` edited at the two ruled clauses and nowhere else. **`cowork_handoff.md`
untouched; no entry prepended, spliced or deleted.** The reading pass's own record files landed
exactly as they stand. The workbook was not opened in any portion and no folder was renamed.

## 9. The standing self-check

1. **#12.** Both `FRAMEWORK.md` corrections preserve their former wording at the site, and one
   preserved quotation was corrected mid-batch to restore its own emphasis markers — the
   silently-improved-quotation defect this same ruling sitting names at its Ruling 4.
2. **#17f / D-431.** The `STATUS.md` entry restates no count, identity or rendered value. Every
   figure in this report is a measurement this batch took, cited to the object it was taken at.
3. **#19.** The kind check is a measurement with a stated measure and a stated weakness, not a
   sample presented as a population claim.
4. **D-253.** Working-tree content was read with the file tools. Shell use was git object queries by
   explicit hash, the sanctioned `tools/audit/` scripts, and the ordered writes. **The shell-read
   guard denied two commands and neither was routed around** — a raw `git status`, and one `git
   diff` whose arguments were shell variables the guard could not resolve; the second was re-run
   with literal hashes.
5. **#24.** Every comparison here is a byte-exact object-to-object measurement or an exact count. No
   difference between two estimated quantities is asserted, so no uncertainty interval is owed.

---

*Provenance: written by the CC session that ran this dispatch, 2026-08-31. Dispatch pinned at
`a06bfc2a392267428f0b1182d67035b2ff0b14cc`; every ruling and surface read at its own object.*
