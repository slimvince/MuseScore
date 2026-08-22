# The July screen — the out-of-period specification-bearing flagged hunks, read one at a time

> **GENERATED FILE — do not hand-edit.** Written by `tools/audit/gen_july_screen.py`; re-derive with `--check`. Every verdict below is AUTHORED and every count is DERIVED. The screen edits no document it reads.

## ★ THE FALSIFICATION RULE FIRES — the period question is RE-OPENED FOR THE USER

**1 of 68 screened hunks classify POSITIVELY CODE-INFLUENCED.** The ruled falsification rule is: *"if any shows a code-influenced correction, the period question RE-OPENS"* — and the re-opening is the user's act on this report, not this screen's.

**What that does and does not mean.** It means the screen found positive evidence of the shape the rule names, and that the period question is now the user's to re-open or to leave settled. It does NOT mean the period ruling is wrong, and this tool takes no view on that. Nothing is repaired, reverted or restored by this finding.

## What the screen cannot settle, stated before the result

Ruling 5 of the eighteenth stop states that influence is INVISIBLE IN THE TEXT — a narrowed rule reads exactly like a rule that was always narrow. So this screen finds POSITIVE evidence of influence and nothing else, and a clear verdict here is bounded by that. A clean class is not a certificate that the change was uninfluenced; the not-cleared class exists for exactly this reason and is published whole.

## The population

- **68 hunks**, across **32 commits** and **6 documents**.
- By stratum: S1-open-items-register 22, S2-status-handoff-doc-split 17, S3-open-items-register-split 28, S4-D231-phase-1 1.
- By document: `ARCHITECTURE.md` 27, `CLAUDE.md` 33, `docs/research_papers/BIBLIOGRAPHY.md` 1, `docs/research_papers/README.md` 1, `docs/score_inventory.md` 1, `docs/scoring_model.md` 5.
- The population is imported whole from `tools/audit/period_stratum_split.json` and never re-listed here (#6); a member entering or leaving it halts the generator rather than being graded silently or quietly dropped.

## The verdicts

| class | hunks |
|---|---|
| POSITIVELY CODE-INFLUENCED | 1 |
| RATIFIED-ACT EDIT | 40 |
| RESTRUCTURING-SHAPED | 12 |
| UNDETERMINED | 15 |

**The classes, and the order they are applied in** (the order is declared because it decides cases, and the first class is applied FIRST so that a ratified act cannot launder a correction made under it):

- **POSITIVELY CODE-INFLUENCED** — The change WITHDRAWS, NARROWS, QUALIFIES or REPLACES something the documentation already stated, and the source of the replacement is a fact read in implementation code THIS COMMIT DID NOT WRITE; or the change's own account states that a documentation statement was corrected against the implementation. APPLIED FIRST, so a ratified act cannot launder a correction made under it.
- **RATIFIED-ACT EDIT** — The change writes, re-stamps or records what a NAMED user act ruled, ratified or directed — including the same-commit documentation half of a ratified change to the code. The act AND where its ratification is recorded are both cited, or the class is not admitted (assumption A3).
- **RESTRUCTURING-SHAPED** — Relocation, split, re-heading or growth whose source is not a fact read in implementation code the commit did not write.
- **UNDETERMINED** — NOT CLEARED — the dispatch's own gloss. A fact in the implementation is the source but the change adds material rather than replacing a standing statement, or no ground supports any class above. Reported whole, never argued down.

## The reported shapes — what kind of change sits behind each verdict

A shape is never a verdict. It is what lets a reader see the KIND of change without the class name standing in for it.

| shape | hunks | what it is |
|---|---|---|
| `describes-pre-existing-implementation-behaviour` | 6 | The change ADDS a description of how the implementation already behaves, read at the code or measured on it. Nothing standing is withdrawn — in the instances here the behaviour is named as a DEFECT — but the source is the implementation, so the hunk is not cleared. |
| `document-relocation-or-re-heading` | 10 | The change moves, splits, re-heads or re-points documentation; no fact from the implementation is its source. |
| `governing-decision-record` | 25 | The change records a user ruling, ratification or direction in the governing document. |
| `measured-value-re-stamp` | 11 | The change re-stamps measured values into gate block (A) at a ratified re-baseline. The values describe what a measurement of the system produced; they are not a statement of design intent, and every superseded column is preserved in place (#12). |
| `new-document-content` | 2 | The change creates a document or a section of one, with no fact from the implementation as its source. |
| `same-commit-code-documentation` | 14 | The change documents code the SAME commit introduces, under the standing same-commit sync rules. Influenced by facts in the code by construction; destroys no discrepancy, because documentation and implementation moved together in one act. |

## The hunks that fire the rule, quoted whole

### `docs/scoring_model.md` @ `-556 +579` — 153d45e78c, 2026-07-14

*Commit subject:* feat(composing): OI-168 — default-OFF key-collection probe + the signature-mask A/B variant (measurement build)

**Ground.** A STANDING table entry is REPLACED. It read "Awarded when root is a scale member of the current key."; it now reads that the bonus is awarded on membership in the current key's collection, names the code-level predicate the term shares with its sibling, and carries "including its OI-168 defect on `Altered` / `AlteredDomBB7`". The source of the replacement is a reading of implementation code THIS COMMIT DID NOT WRITE — the commit's own account states the doc-sync "documents the shared predicate and the defect", and states that the predicate's committed branch is the same test as before. That is a standing documentation statement altered against the implementation, which is this class.

**THE COUNTER-CONSIDERATION, recorded because the user's act rests on this hunk: the replacement does not ERASE the discrepancy — it names the defect, points at the §4 block that measures it, and the same commit builds a default-OFF measurement of it. The substance of the first clause may also be unchanged, since "scale member of the current key" and "member of the current key's collection" are arguably the same claim in different words. What fires the class is the test as the dispatch states it — the change, and its commit's own account, show a documentation statement altered against the implementation — not a judgment that evidence was destroyed here.**

**Removed:**

```
| `diatonicRootBonus`                  | 0.30          | Awarded when root is a scale member of the current key. |
```

**Added:**

```
| `diatonicRootBonus`                  | 0.30          | Awarded when the root is a member of the current key's collection (`diatonicRootContribution`). Shares the `pcInKeyCollection()` membership predicate with `dim7CharacteristicBonus` — including its OI-168 defect on `Altered` / `AlteredDomBB7`; see §4. |
```

*Retrieve it yourself:* `git show 153d45e78c5162c17844c7a488f9e9901b524141 --no-color -U0 -- docs/scoring_model.md`

## The registered prediction P2, graded

- **Limb 1 — the large majority classify RATIFIED-ACT EDIT or RESTRUCTURING-SHAPED:** 52 of 68 (0.7647). The prediction says *large majority* and fixes no threshold, so the share is published and the reading is left to the reader rather than computed against a number nobody registered.
- **Limb 2 — ZERO classify POSITIVELY CODE-INFLUENCED:** predicted 0, derived 1 — **REFUTED**. "one hunk whose change, or whose commit's own account, states or shows correction against the implementation" — which is the condition this screen applies as its first class.

Nothing in the verdicts was adjusted to make a limb hold. A prediction is graded and never used as an input (#17b).

## Assumption A2 — the retrieval, checked per hunk rather than asserted

Every hunk's text was retrieved from the git object by explicit hash — `git show <commit> --no-color -U0 -- <path>` — and its recorded header looked for among the headers that came back. Performed on every run, not asserted.

- Hunks that did not resolve: **0**.
- Hunks whose retrieved line counts disagree with the population's own record: **0**.

## Every hunk, with its verdict and its ground

### 2026-07-11 · `CLAUDE.md` @ `-44 +44,3` · 6b4ca1752b

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): #17(c) control-flow-first RATIFIED + the siloed-facts audit (spelling was not alone) + register section I (OI-72..OI-80)
- **Ground.** The hunk rewrites principle #17(c) to put the control-flow question first, and the added text carries its own attribution — "control flow — ratified sharpening 2026-07-10, the EG-2 desk-sim lesson". The commit's account opens "User ratified the #17(c) sharpening". No fact about the implementation appears in the change or in the account.
- **The act:** the #17(c) control-flow-first sharpening of the Premise Gate
- **Where its ratification is recorded:** the added text itself; the commit's own account; and CLAUDE.md's #17 provenance paragraph at HEAD, which records #17–19 as ratified by the user on 2026-07-10
- *Retrieve:* `git show 6b4ca1752b6f857027da1b9ddff4ea9fd3081814 --no-color -U0 -- CLAUDE.md`

### 2026-07-11 · `CLAUDE.md` @ `-63,0 +64,6` · 2454658f07

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): RATIFIED - the fact-publication corollary (into CLAUDE.md) + the seven Part-A verdicts (A3 acceptance explicit); OI-84 added - exhaustive audit OWED
- **Ground.** The hunk adds the fact-publication corollary, whose own first line reads "(ratified by the user, 2026-07-10)". The commit's account opens "User ratified: (1) the fact-publication corollary". Its evidence citations are to two Cowork documents, not to the code.
- **The act:** the fact-publication corollary to #6/#7/#12
- **Where its ratification is recorded:** the added text itself, and the same corollary at CLAUDE.md at HEAD
- *Retrieve:* `git show 2454658f077a2ba5efd43600b409b309ebfdd486 --no-color -U0 -- CLAUDE.md`

### 2026-07-11 · `CLAUDE.md` @ `-74 +74` · 7123c7cb55

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cowork): cowork_handoff.md is THE single entry document - tracked name lowercased (was COWORK_HANDOFF.md), entry block reframed, live references fixed
- **Ground.** One pointer, `COWORK_HANDOFF.md` → `cowork_handoff.md`, following the tracked rename of that documentation file in the SAME commit. The source is a documentation file's own name; nothing about the implementation appears in the change or in the account.
- *Retrieve:* `git show 7123c7cb5512b011811edb4b4c87bb1d8c94e877 --no-color -U0 -- CLAUDE.md`

### 2026-07-11 · `CLAUDE.md` @ `-554,0 +555,15` · 239408faad

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): L1/L2 certification withheld on partial blinding - OI-89 + DT-20 + the blind re-run instruction; CLAUDE.md conventions: no self-invented labels; the self-check after every coding exercise
- **Ground.** The hunk adds two conventions, each carrying its own attribution — "(User-directed, repeatedly; recorded 2026-07-11.)" and "(user-directed, 2026-07-11)". Neither mentions the implementation.
- **The act:** the no-self-invented-labels convention and the standing self-check after every coding exercise
- **Where its ratification is recorded:** the added text itself, and both rules at CLAUDE.md at HEAD
- *Retrieve:* `git show 239408faadf40e2d46c428397522ca3d688dbe5d --no-color -U0 -- CLAUDE.md`

### 2026-07-12 · `CLAUDE.md` @ `-177,11 +177,18` · d9b52ba969

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-142/OI-143 key-grading re-baseline — corpus-transposition correction + dual home/local key columns (user-ratified 2026-07-12)
- **Ground.** Gate block (A) is re-stamped with the values the OI-142/OI-143 re-baseline measured. The commit's subject carries "(user-ratified 2026-07-12)" and the added text repeats it. The superseded column is preserved in place with its snapshot directory named (#12). What the re-baseline changed is the GRADING — the transposition offsets applied to the ground truth and the key column split in two — not a statement about what the implementation does.
- **The act:** the OI-142/OI-143 key-grading re-baseline
- **Where its ratification is recorded:** the commit subject and the added text; the same re-baseline is recorded in gate block (A)'s superseded-column lineage at CLAUDE.md at HEAD
- *Retrieve:* `git show d9b52ba9696ae51f1504c902c04825c538313754 --no-color -U0 -- CLAUDE.md`

### 2026-07-12 · `CLAUDE.md` @ `-213,4 +220,12` · d9b52ba969

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-142/OI-143 key-grading re-baseline — corpus-transposition correction + dual home/local key columns (user-ratified 2026-07-12)
- **Ground.** Gate block (A) is re-stamped with the values the OI-142/OI-143 re-baseline measured. The commit's subject carries "(user-ratified 2026-07-12)" and the added text repeats it. The superseded column is preserved in place with its snapshot directory named (#12). What the re-baseline changed is the GRADING — the transposition offsets applied to the ground truth and the key column split in two — not a statement about what the implementation does.
- **The act:** the OI-142/OI-143 key-grading re-baseline
- **Where its ratification is recorded:** the commit subject and the added text; the same re-baseline is recorded in gate block (A)'s superseded-column lineage at CLAUDE.md at HEAD
- *Retrieve:* `git show d9b52ba9696ae51f1504c902c04825c538313754 --no-color -U0 -- CLAUDE.md`

### 2026-07-12 · `CLAUDE.md` @ `-68,0 +69,9` · fe985ab047

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): preserve the concurrent live edits — publish-evidence-broadly rule + the evidence inventory + OI-146
- **Ground.** The hunk adds the amendment whose own opening is "*Amendment (user, 2026-07-12, at the evidence-inventory discussion):*" and which quotes the user's rationale. The commit's account names it "the user's 2026-07-12 amendment to the fact-publication corollary".
- **The act:** the user's amendment for EVIDENCE-class facts (publish broadly without a named consumer)
- **Where its ratification is recorded:** the added text itself, and the same amendment at CLAUDE.md at HEAD
- *Retrieve:* `git show fe985ab04757dc9eb214ed12664001fa5156238e --no-color -U0 -- CLAUDE.md`

### 2026-07-13 · `CLAUDE.md` @ `-194 +194` · 800f1a12bf

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-132 — the parent-collection mode grading, consolidated into the ONE key reduction (re-baseline, user-ratified 2026-07-13)
- **Ground.** The key columns of gate block (A) are re-stamped at the OI-132 mode-grading consolidation. The commit's account carries both dates in terms — "Ruling: the user, 2026-07-12 … Ratified: the user, 2026-07-13" — and the added text repeats "user-ratified 2026-07-13". The superseded columns are preserved with their snapshot directory named (#12). The consolidation changed how an emitted mode is GRADED, not what the implementation does.
- **The act:** the OI-132 parent-collection mode-grading consolidation
- **Where its ratification is recorded:** the commit's own account; and the same convention at CLAUDE.md at HEAD, among the four grading conventions the robust unit is measured under
- *Retrieve:* `git show 800f1a12bf136ebc80b84d05427570a9be0a7a5b --no-color -U0 -- CLAUDE.md`

### 2026-07-13 · `CLAUDE.md` @ `-196,8 +196,22` · 800f1a12bf

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-132 — the parent-collection mode grading, consolidated into the ONE key reduction (re-baseline, user-ratified 2026-07-13)
- **Ground.** The key columns of gate block (A) are re-stamped at the OI-132 mode-grading consolidation. The commit's account carries both dates in terms — "Ruling: the user, 2026-07-12 … Ratified: the user, 2026-07-13" — and the added text repeats "user-ratified 2026-07-13". The superseded columns are preserved with their snapshot directory named (#12). The consolidation changed how an emitted mode is GRADED, not what the implementation does.
- **The act:** the OI-132 parent-collection mode-grading consolidation
- **Where its ratification is recorded:** the commit's own account; and the same convention at CLAUDE.md at HEAD, among the four grading conventions the robust unit is measured under
- *Retrieve:* `git show 800f1a12bf136ebc80b84d05427570a9be0a7a5b --no-color -U0 -- CLAUDE.md`

### 2026-07-13 · `CLAUDE.md` @ `-230,7 +244,12` · 800f1a12bf

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-132 — the parent-collection mode grading, consolidated into the ONE key reduction (re-baseline, user-ratified 2026-07-13)
- **Ground.** The key columns of gate block (A) are re-stamped at the OI-132 mode-grading consolidation. The commit's account carries both dates in terms — "Ruling: the user, 2026-07-12 … Ratified: the user, 2026-07-13" — and the added text repeats "user-ratified 2026-07-13". The superseded columns are preserved with their snapshot directory named (#12). The consolidation changed how an emitted mode is GRADED, not what the implementation does.
- **The act:** the OI-132 parent-collection mode-grading consolidation
- **Where its ratification is recorded:** the commit's own account; and the same convention at CLAUDE.md at HEAD, among the four grading conventions the robust unit is measured under
- *Retrieve:* `git show 800f1a12bf136ebc80b84d05427570a9be0a7a5b --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `ARCHITECTURE.md` @ `-609,0 +610,4` · 153d45e78c

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** feat(composing): OI-168 — default-OFF key-collection probe + the signature-mask A/B variant (measurement build)
- **Ground.** Four lines are added to the source-tree listing for `keycollectionprobe.h/.cpp`, files this commit itself creates. The commit's account names the act — "Doc-sync in the same commit (#10) … ARCHITECTURE.md lists the new TU". So a fact in the code is the source, and the code is this commit's own; nothing standing is withdrawn and no user act is cited. NOT CLEARED.
- *Retrieve:* `git show 153d45e78c5162c17844c7a488f9e9901b524141 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-262,0 +263,23` · 153d45e78c

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** feat(composing): OI-168 — default-OFF key-collection probe + the signature-mask A/B variant (measurement build)
- **Ground.** A new §4 block is added describing the membership predicate's COMMITTED FORM — the mode-transposed set, the 19-of-21 equality, the two modes it is wrong for — and stating in terms that "both terms score against the wrong collection". The behaviour described is pre-existing: the commit's own account says the unified predicate's "committed branch is the same test as before". So the source is a reading of implementation code this commit did not write. It is an ADDITION — nothing standing is withdrawn, and the discrepancy is NAMED as a defect rather than removed — so it is not a correction; it is also not cleared. This is the largest instance of the shape in the whole screened population and it is reported as one.
- **Remark.** Ruling 4 of the eighteenth stop is what keeps this in view: an addition can make a correct specification wrong without removing a word. Whether a specification that states what the code does — even while calling it a defect — pre-empts the comparison a later audit would have made is not establishable from the text, which is why the verdict is NOT CLEARED rather than either clear class.
- *Retrieve:* `git show 153d45e78c5162c17844c7a488f9e9901b524141 --no-color -U0 -- docs/scoring_model.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-556 +579` · 153d45e78c

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** feat(composing): OI-168 — default-OFF key-collection probe + the signature-mask A/B variant (measurement build)
- **Ground.** A STANDING table entry is REPLACED. It read "Awarded when root is a scale member of the current key."; it now reads that the bonus is awarded on membership in the current key's collection, names the code-level predicate the term shares with its sibling, and carries "including its OI-168 defect on `Altered` / `AlteredDomBB7`". The source of the replacement is a reading of implementation code THIS COMMIT DID NOT WRITE — the commit's own account states the doc-sync "documents the shared predicate and the defect", and states that the predicate's committed branch is the same test as before. That is a standing documentation statement altered against the implementation, which is this class.
- **Remark.** THE COUNTER-CONSIDERATION, recorded because the user's act rests on this hunk: the replacement does not ERASE the discrepancy — it names the defect, points at the §4 block that measures it, and the same commit builds a default-OFF measurement of it. The substance of the first clause may also be unchanged, since "scale member of the current key" and "member of the current key's collection" are arguably the same claim in different words. What fires the class is the test as the dispatch states it — the change, and its commit's own account, show a documentation statement altered against the implementation — not a judgment that evidence was destroyed here.
- *Retrieve:* `git show 153d45e78c5162c17844c7a488f9e9901b524141 --no-color -U0 -- docs/scoring_model.md`

### 2026-07-14 · `CLAUDE.md` @ `-186 +186` · 10235d5547

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified)", and the added text carries "dispatch user-ratified 2026-07-13". The superseded reference is preserved with its snapshot directory named (#12).
- **The act:** the OI-168 signature-mask correctness fix and its re-baseline
- **Where its ratification is recorded:** the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose OI-168 re-baseline block records the same ratification
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `CLAUDE.md` @ `-190,8 +190,32` · 10235d5547

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified)", and the added text carries "dispatch user-ratified 2026-07-13". The superseded reference is preserved with its snapshot directory named (#12).
- **The act:** the OI-168 signature-mask correctness fix and its re-baseline
- **Where its ratification is recorded:** the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose OI-168 re-baseline block records the same ratification
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `CLAUDE.md` @ `-244 +268,4` · 10235d5547

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified)", and the added text carries "dispatch user-ratified 2026-07-13". The superseded reference is preserved with its snapshot directory named (#12).
- **The act:** the OI-168 signature-mask correctness fix and its re-baseline
- **Where its ratification is recorded:** the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose OI-168 re-baseline block records the same ratification
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-263,22 +263,34` · 10235d5547

- **Verdict:** RATIFIED-ACT EDIT · shape `same-commit-code-documentation`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** The §4 block and the table entry are rewritten to describe the behaviour THIS COMMIT INTRODUCES — the two terms now test the key signature's own collection — and the form they replaced is kept beside them as "the defect it replaced". The commit's account names the act and its ratification, and names the standing rule that requires the documentation to move in the same commit. Documentation and implementation moved together under one ratified act, so no standing statement was aligned to unchanged behaviour.
- **The act:** the OI-168 signature-mask correctness fix
- **Where its ratification is recorded:** the commit's own account ("cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified"); and gate block (A) at CLAUDE.md at HEAD
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- docs/scoring_model.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-579 +591` · 10235d5547

- **Verdict:** RATIFIED-ACT EDIT · shape `same-commit-code-documentation`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** The §4 block and the table entry are rewritten to describe the behaviour THIS COMMIT INTRODUCES — the two terms now test the key signature's own collection — and the form they replaced is kept beside them as "the defect it replaced". The commit's account names the act and its ratification, and names the standing rule that requires the documentation to move in the same commit. Documentation and implementation moved together under one ratified act, so no standing statement was aligned to unchanged behaviour.
- **The act:** the OI-168 signature-mask correctness fix
- **Where its ratification is recorded:** the commit's own account ("cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified"); and gate block (A) at CLAUDE.md at HEAD
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- docs/scoring_model.md`

### 2026-07-16 · `docs/scoring_model.md` @ `-297,0 +298,25` · b3d6c0f03a

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** feat(composing): OI-170 — default-OFF instrumentation + signature-mask A/B for the THREE remaining collection-membership sites (measurement build; NO fix promoted)
- **Ground.** A block is added recording what a default-OFF A/B measured at three PRE-EXISTING sites — that zero committed chords move, that one published flag moves on nine files, and what a future fix may and may not do. The source is a measurement of implementation code this commit did not write. Nothing standing is withdrawn and no user act is cited. NOT CLEARED.
- *Retrieve:* `git show b3d6c0f03a18a72d87341ad89220a81e090039ba --no-color -U0 -- docs/scoring_model.md`

### 2026-07-18 · `ARCHITECTURE.md` @ `-2,0 +3,8` · 06d4318bd1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: ratify principles #20-#24 + joint-estimator plan amendments (OI-176...OI-181), user-ratified 2026-07-18
- **Ground.** The governing-decision banner is added, its own first words "★★ GOVERNING DECISION (user-ratified 2026-07-17): the key/mode/chord estimator is JOINT". The commit's account lists it among the 2026-07-17 joint-architecture decision documents.
- **The act:** the joint key/mode/chord estimator as the target architecture
- **Where its ratification is recorded:** the added banner itself, which is still at the top of ARCHITECTURE.md at HEAD
- *Retrieve:* `git show 06d4318bd1f322d055d04622681587c44a01bffb --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-18 · `CLAUDE.md` @ `-56,0 +57,27` · 06d4318bd1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: ratify principles #20-#24 + joint-estimator plan amendments (OI-176...OI-181), user-ratified 2026-07-18
- **Ground.** Principles #20–#24 and the constrained-optimum ledger corollary are added. The commit's account names them "(user-ratified 2026-07-18)".
- **The act:** principles #20–#24 and the constrained-optimum ledger corollary
- **Where its ratification is recorded:** CLAUDE.md's #17–#24 provenance paragraph, which records the 2026-07-18 ratification at the joint-estimator plan review and stands at HEAD
- *Retrieve:* `git show 06d4318bd1f322d055d04622681587c44a01bffb --no-color -U0 -- CLAUDE.md`

### 2026-07-18 · `CLAUDE.md` @ `-82 +109,4` · 06d4318bd1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: ratify principles #20-#24 + joint-estimator plan amendments (OI-176...OI-181), user-ratified 2026-07-18
- **Ground.** The provenance paragraph is extended to record who ratified #20–#24 and when. It is the citation half of the same act.
- **The act:** principles #20–#24 and the constrained-optimum ledger corollary
- **Where its ratification is recorded:** the extended provenance paragraph itself, at CLAUDE.md at HEAD
- *Retrieve:* `git show 06d4318bd1f322d055d04622681587c44a01bffb --no-color -U0 -- CLAUDE.md`

### 2026-07-18 · `CLAUDE.md` @ `-168 +168,2` · 51d4f6dcf3

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cc): split STATUS.md + cowork_handoff.md into lean active must-reads + verbatim archives (cc_instruction_doc_split.md)
- **Ground.** The doc-split commit updates the session-start read's description of the now-lean STATUS.md. Its account is "Pure documentation hygiene per the dispatch … the history moves verbatim to reference-only archives. No code, no build, no golden, no corpus, no register change", and it reports a byte-level reconciliation of the partition. No fact from the implementation is its source.
- *Retrieve:* `git show 51d4f6dcf34121a2598750c41b808c2f895ae674 --no-color -U0 -- CLAUDE.md`

### 2026-07-18 · `CLAUDE.md` @ `-170 +171,3` · 51d4f6dcf3

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cc): split STATUS.md + cowork_handoff.md into lean active must-reads + verbatim archives (cc_instruction_doc_split.md)
- **Ground.** The doc-split commit updates the pointer to the two reference-only archives. Its account is "Pure documentation hygiene per the dispatch … the history moves verbatim to reference-only archives. No code, no build, no golden, no corpus, no register change", and it reports a byte-level reconciliation of the partition. No fact from the implementation is its source.
- *Retrieve:* `git show 51d4f6dcf34121a2598750c41b808c2f895ae674 --no-color -U0 -- CLAUDE.md`

### 2026-07-19 · `docs/research_papers/BIBLIOGRAPHY.md` @ `-0,0 +1,99` · 4f2c5ddfdb

- **Verdict:** RESTRUCTURING-SHAPED · shape `new-document-content`
- **Commit subject:** docs(cc): research-paper library link-rot mitigation — private repo, nothing redistributed
- **Ground.** A new document: one row per published source, with its link, whether a local copy exists and its redistribution tier. Its subject is the published literature and this fork's handling of it; no fact from the implementation is its source.
- *Retrieve:* `git show 4f2c5ddfdb0ecd2e4363982b0dc722dd9e7e52e0 --no-color -U0 -- docs/research_papers/BIBLIOGRAPHY.md`

### 2026-07-19 · `docs/research_papers/README.md` @ `-0,0 +1,27` · 4f2c5ddfdb

- **Verdict:** RESTRUCTURING-SHAPED · shape `new-document-content`
- **Commit subject:** docs(cc): research-paper library link-rot mitigation — private repo, nothing redistributed
- **Ground.** A new document indexing the locally held copies and what each settled in the theory grounding, plus the statement that the binaries live only in a private repository. Its subject is the literature and file handling; no fact from the implementation is its source.
- *Retrieve:* `git show 4f2c5ddfdb0ecd2e4363982b0dc722dd9e7e52e0 --no-color -U0 -- docs/research_papers/README.md`

### 2026-07-25 · `ARCHITECTURE.md` @ `-768 +768` · 1e35415ee0

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** composing: joint estimator Task B — the L1 fact-surface additive extension (notatedNotes)
- **Ground.** The standing note-model row is extended to describe the additive `notatedNotes()` surface this commit itself adds. The commit's account names the act — "ARCHITECTURE.md L1 note-model row synced (#10 / OI-146)". A sanction is named (OI-180) but no user act and no place of ratification is citable from the change or its account, so the RATIFIED-ACT class is not admitted (assumption A3). Nothing standing is withdrawn. NOT CLEARED.
- *Retrieve:* `git show 1e35415ee06b77e001aeea3b947369a2016573b3 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-10,0 +11,25` · 205dd0843a

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** The as-built banner for the adoption is added, its own first words "★★ AS-BUILT (the OI-178 adoption, user-ratified 2026-07-26, option 1 — STAGED SCOPE)". The commit's subject and account carry the same.
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added banner; and gate block (A) at CLAUDE.md at HEAD, which records the adoption as user-ratified 2026-07-26 with its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `CLAUDE.md` @ `-219 +219,3` · 205dd0843a

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence statement, the staged-scope declaration, and the superseded columns preserved with their snapshot named (#12). The commit subject and the added text both carry "user-ratified 2026-07-26, option 1".
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified baselines still record this adoption and its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-228,7 +230,28` · 205dd0843a

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence statement, the staged-scope declaration, and the superseded columns preserved with their snapshot named (#12). The commit subject and the added text both carry "user-ratified 2026-07-26, option 1".
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified baselines still record this adoption and its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-300,8 +323,13` · 205dd0843a

- **Verdict:** RATIFIED-ACT EDIT · shape `measured-value-re-stamp`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence statement, the staged-scope declaration, and the superseded columns preserved with their snapshot named (#12). The commit subject and the added text both carry "user-ratified 2026-07-26, option 1".
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified baselines still record this adoption and its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-105,0 +106,14` · 00c0df81c5

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** ratification record: notation-layer adoption increment decision surface + the decision-neutrality principles corollary (user, 2026-07-26); rows OI-193/OI-194
- **Ground.** The decision-neutrality corollary is added, its own opening "(corollary to #4/#6/#19; user-ratified 2026-07-26)". The commit's subject is a ratification record.
- **The act:** the decision-neutrality corollary
- **Where its ratification is recorded:** the added text, and the same corollary at CLAUDE.md at HEAD, whose provenance names the notation-layer adoption increment's decision surface
- *Retrieve:* `git show 00c0df81c5682fbda0515a81cea0c3c541e8ee23 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-112 +126,3` · 00c0df81c5

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** ratification record: notation-layer adoption increment decision surface + the decision-neutrality principles corollary (user, 2026-07-26); rows OI-193/OI-194
- **Ground.** The provenance paragraph is extended to record the corollary's ratification and where its analysis lives. It is the citation half of the same act.
- **The act:** the decision-neutrality corollary
- **Where its ratification is recorded:** the extended provenance paragraph itself, at CLAUDE.md at HEAD
- *Retrieve:* `git show 00c0df81c5682fbda0515a81cea0c3c541e8ee23 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-18,3 +18,14` · 83fbb9e661

- **Verdict:** RATIFIED-ACT EDIT · shape `same-commit-code-documentation`
- **Commit subject:** composing: joint estimator — Decision D1 EXECUTED (fitted tables + selected weight vector embedded as provenance-stamped generated source)
- **Ground.** The as-built banner is amended to record the embedded table/weight delivery THIS COMMIT introduces, and the changed sentences describe the new delivery rather than the old one. The commit's subject is "Decision D1 EXECUTED" and its account cites "ratified Decision D1, cowork_notation_adoption_increment.md §5".
- **The act:** ratified Decision D1 — the fitted tables and the selected weight vector embedded as provenance-stamped generated source
- **Where its ratification is recorded:** `cowork_notation_adoption_increment.md` §5, the decision surface CLAUDE.md's decision-neutrality corollary records as user-ratified 2026-07-26
- *Retrieve:* `git show 83fbb9e66156d2c0fc4ad6b2f98cad4ed46e4146 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-24 +35,2` · 83fbb9e661

- **Verdict:** RATIFIED-ACT EDIT · shape `same-commit-code-documentation`
- **Commit subject:** composing: joint estimator — Decision D1 EXECUTED (fitted tables + selected weight vector embedded as provenance-stamped generated source)
- **Ground.** The as-built banner is amended to record the embedded table/weight delivery THIS COMMIT introduces, and the changed sentences describe the new delivery rather than the old one. The commit's subject is "Decision D1 EXECUTED" and its account cites "ratified Decision D1, cowork_notation_adoption_increment.md §5".
- **The act:** ratified Decision D1 — the fitted tables and the selected weight vector embedded as provenance-stamped generated source
- **Where its ratification is recorded:** `cowork_notation_adoption_increment.md` §5, the decision surface CLAUDE.md's decision-neutrality corollary records as user-ratified 2026-07-26
- *Retrieve:* `git show 83fbb9e66156d2c0fc4ad6b2f98cad4ed46e4146 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-44,0 +45,22` · 56439ebad7

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** joint: posterior slice on the C++ module surface + bit-identical parity driver (contract §3.3 group (i))
- **Ground.** An as-built block is added for the posterior slice this commit itself implements, with its establishment and its parity result. The commit's account names the act — "Doc sync (#10): ARCHITECTURE.md joint-estimator as-built". A contract section and a dispatch are cited; no user act is, so the RATIFIED-ACT class is not admitted (assumption A3). NOT CLEARED.
- *Retrieve:* `git show 56439ebad7f5010013cec41eab834d39189f52f6 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-66,0 +67,27` · e336bd0348

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** joint: the §3.4 un-rounded modal reading + establishment + doc sync (contract §3.4; dormant)
- **Ground.** An as-built block is added for the notation record §3.1–§3.6 delivered across this commit and its predecessors, with its establishment. The commit's account names a ratified decision (C1) for ONE PORTION of what the block describes — the modal reading — and no user act for the remainder, so the RATIFIED-ACT class is not admitted for the hunk as a whole (assumption A3). NOT CLEARED.
- *Retrieve:* `git show e336bd034837cfc4e81cf1c5bb4b00d611c283b4 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-90,3 +90,8` · 6e71b3ceff

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** joint: seams part 1 — the record-producing entry + the two §1 seam views (dormant; contract §1; dispatch cc_instruction_notation_seams_1.md Task 2)
- **Ground.** A standing establishment sentence is extended with the C++/Python spelling parity this commit's own Task 1 established on 13,063 committed segments, and the consumer clause is re-pointed at the producer this commit adds. Nothing standing is withdrawn — a measured establishment is inserted — but the source is a measurement of the implementation. NOT CLEARED.
- *Retrieve:* `git show 6e71b3ceff61dcdf9c79cfb722111fa95e79e0c8 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-93,0 +99,22` · 6e71b3ceff

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** joint: seams part 1 — the record-producing entry + the two §1 seam views (dormant; contract §1; dispatch cc_instruction_notation_seams_1.md Task 2)
- **Ground.** An as-built block is added for the record producer and the two seam views this commit implements. The commit's account names the act — "Doc sync (#10)". No user act is cited. NOT CLEARED.
- *Retrieve:* `git show 6e71b3ceff61dcdf9c79cfb722111fa95e79e0c8 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `CLAUDE.md` @ `-133 +133` · 1e32b5e92e

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** register split: OPEN_ITEMS.md -> lean index + open_items/ per-item detail files (user-ratified option 1, 2026-07-26; byte-reconciled, status authoritative in the index)
- **Ground.** The open-items register section is rewritten for the index-plus-detail split, and the changed text carries "split into index + detail files, user-ratified 2026-07-26" and "user-ratified option 1". The commit subject carries the same. The rules (a)–(e) are re-worded for the split; no fact from the implementation is the source.
- **The act:** the open-items register's split into a lean index plus one detail file per item
- **Where its ratification is recorded:** the changed text itself, and the same section at CLAUDE.md at HEAD
- *Retrieve:* `git show 1e32b5e92e2594d3a8d1752fcea051dab16f60a7 --no-color -U0 -- CLAUDE.md`

### 2026-07-27 · `CLAUDE.md` @ `-135,6 +135,12` · 1e32b5e92e

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** register split: OPEN_ITEMS.md -> lean index + open_items/ per-item detail files (user-ratified option 1, 2026-07-26; byte-reconciled, status authoritative in the index)
- **Ground.** The open-items register section is rewritten for the index-plus-detail split, and the changed text carries "split into index + detail files, user-ratified 2026-07-26" and "user-ratified option 1". The commit subject carries the same. The rules (a)–(e) are re-worded for the split; no fact from the implementation is the source.
- **The act:** the open-items register's split into a lean index plus one detail file per item
- **Where its ratification is recorded:** the changed text itself, and the same section at CLAUDE.md at HEAD
- *Retrieve:* `git show 1e32b5e92e2594d3a8d1752fcea051dab16f60a7 --no-color -U0 -- CLAUDE.md`

### 2026-07-27 · `CLAUDE.md` @ `-142,2 +148,3` · 1e32b5e92e

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** register split: OPEN_ITEMS.md -> lean index + open_items/ per-item detail files (user-ratified option 1, 2026-07-26; byte-reconciled, status authoritative in the index)
- **Ground.** The open-items register section is rewritten for the index-plus-detail split, and the changed text carries "split into index + detail files, user-ratified 2026-07-26" and "user-ratified option 1". The commit subject carries the same. The rules (a)–(e) are re-worded for the split; no fact from the implementation is the source.
- **The act:** the open-items register's split into a lean index plus one detail file per item
- **Where its ratification is recorded:** the changed text itself, and the same section at CLAUDE.md at HEAD
- *Retrieve:* `git show 1e32b5e92e2594d3a8d1752fcea051dab16f60a7 --no-color -U0 -- CLAUDE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-123,0 +124,22` · b2c71fb6e3

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** notation seams-2 P-strings Task 3+4: the permanent inference↔presentation boundary guard + doc sync (dispatch cc_instruction_notation_pstrings.md)
- **Ground.** An as-built block is added for the notation consumer re-plumb and the permanently guarded inference/presentation boundary this commit implements. Ratified rules are cited inside it (Decision D2, the contract amendment) but no user act is named for this change, so the RATIFIED-ACT class is not admitted (assumption A3). NOT CLEARED.
- *Retrieve:* `git show b2c71fb6e3b29d1ae1b7595a6875199389604b75 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-145,0 +146,25` · 599eebd45e

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** notation seams-2 P4 Task 3+4: the tuning region record path + OI-182 EXECUTED + doc sync
- **Ground.** An as-built block is added for the implode and tuning span-seam consumers and the exposure-bucket unification this commit implements, including the two constants' declared sites. The commit's account names the act — "ARCHITECTURE.md gains the implode/tuning record-path + exposure-bucket as-built block". No user act is cited. NOT CLEARED.
- *Retrieve:* `git show 599eebd45eb5a050e1901ef9111a7b5890716817 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-170,0 +171,27` · 903125a5dc

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** notation seams-2 note-seam Task 3+4: the three consumers on the carriage + structural pins + doc sync
- **Ground.** An as-built block is added for the note-seam re-plumb this commit implements, down to which fields the record-arm builder fills and which it leaves at defaults. The commit's account names the act — "Doc sync (#10)". No user act is cited. NOT CLEARED.
- *Retrieve:* `git show 903125a5dc79b9ac80865f82b79fa15cd604bdc5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-107 +107,7` · 89412b48b2

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** notation seams-2 P6 Task 3+4: the classified diff + doc sync (the switch evidence)
- **Ground.** A standing sentence about the producer is extended with the OI-204 input-scoping parameter and what it does at the fact adapter. Nothing standing is withdrawn; the source is the implementation. The commit's account names the act — "Doc sync: ARCHITECTURE.md (the OI-204 input-scoping parameter + the dual-arm instrument as-built)". NOT CLEARED.
- *Retrieve:* `git show 89412b48b27e2cfe70254e5a2199d6c3c681958c --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-197,0 +204,21` · 89412b48b2

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** notation seams-2 P6 Task 3+4: the classified diff + doc sync (the switch evidence)
- **Ground.** An as-built block is added for the dual-arm classified-comparison tool this commit delivers, with the classes it assigns and what it measured. No user act is cited. NOT CLEARED.
- *Retrieve:* `git show 89412b48b27e2cfe70254e5a2199d6c3c681958c --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-100,2 +100,11` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: the consolidated section header replaces the first per-unit heading, and the framing text restates the dual-arm posture the five blocks already carried. The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-121,2 +130,3` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: a consumer sentence is re-pointed from a later dispatch to the subsections below it. The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-130,3 +140,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: a per-unit heading becomes numbered subsection (2). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-152,2 +161,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: a per-unit heading becomes numbered subsection (3). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-177,2 +186,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: a per-unit heading becomes numbered subsection (4). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-199,4 +208` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: a forward-looking sentence about what remains before the switch is trimmed to one line, its substance carried into the new subsection (6). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-204,2 +210,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** One step of the P7 consolidation: a per-unit heading becomes numbered subsection (5). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-223,0 +230,13` · 4967d6b724

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** A new subsection (6) is added stating the dual path's current state — the flag OFF everywhere, the partition closed out and completeness-verified, the three suites green — and what the switch would do. The state it reports is read off a verification of the code performed in the same commit. Nothing standing is withdrawn. NOT CLEARED.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-100,8 +100,9` · 2a81af273e

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** THE NOTATION SWITCH: the record path is the production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens refreshed against the P6-classified record output; staged scope CLOSED
- **Ground.** The dormant-posture text is replaced by the switched posture: the record path is the production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. The commit's subject carries "(user-ratified 2026-07-27)" and every changed passage repeats it. The replaced statements were made false by the ratified act itself, not by a reading of the code.
- **The act:** THE NOTATION SWITCH — the record path made the production in-app notation analysis
- **Where its ratification is recorded:** the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED SCOPE block records the switch as user-ratified 2026-07-27
- *Retrieve:* `git show 2a81af273ee9b9339736f6e03b0fc96b55bc5005 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-231,12 +232,18` · 2a81af273e

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** THE NOTATION SWITCH: the record path is the production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens refreshed against the P6-classified record output; staged scope CLOSED
- **Ground.** The dormant-posture text is replaced by the switched posture: the record path is the production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. The commit's subject carries "(user-ratified 2026-07-27)" and every changed passage repeats it. The replaced statements were made false by the ratified act itself, not by a reading of the code.
- **The act:** THE NOTATION SWITCH — the record path made the production in-app notation analysis
- **Where its ratification is recorded:** the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED SCOPE block records the switch as user-ratified 2026-07-27
- *Retrieve:* `git show 2a81af273ee9b9339736f6e03b0fc96b55bc5005 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `CLAUDE.md` @ `-269,4 +269,16` · 2a81af273e

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** THE NOTATION SWITCH: the record path is the production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens refreshed against the P6-classified record output; staged scope CLOSED
- **Ground.** The dormant-posture text is replaced by the switched posture: the record path is the production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. The commit's subject carries "(user-ratified 2026-07-27)" and every changed passage repeats it. The replaced statements were made false by the ratified act itself, not by a reading of the code.
- **The act:** THE NOTATION SWITCH — the record path made the production in-app notation analysis
- **Where its ratification is recorded:** the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED SCOPE block records the switch as user-ratified 2026-07-27
- *Retrieve:* `git show 2a81af273ee9b9339736f6e03b0fc96b55bc5005 --no-color -U0 -- CLAUDE.md`

### 2026-07-28 · `docs/score_inventory.md` @ `-234 +234,18` · 5135764ed7

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** OI-206 analysis-cost Task 6: dated notes + doc sync (READ-ONLY)
- **Ground.** A subfolder of large scores is added to the inventory with measured counts, the licence read from each file's own metadata, and a closing statement that the joint decoder returns an EMPTY analysis on 13 of the 23. That last clause is a measured fact about the implementation's behaviour. Nothing standing is withdrawn and no user act is cited. NOT CLEARED.
- *Retrieve:* `git show 5135764ed7f8d7b992ed5f1c3b4c2fecab7f5d35 --no-color -U0 -- docs/score_inventory.md`

### 2026-07-28 · `CLAUDE.md` @ `-720,0 +721,19` · 8c8e57eab9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cc): decision harvest — register rows + OI-207/208 notes (Task 0)
- **Ground.** The never-work-from-memory convention is added, its own opening "(user-directed, 2026-07-28; binds Cowork and CC equally)". Its founding instance names a specification and the position it states; the rule itself is the user's.
- **The act:** the never-work-from-memory convention
- **Where its ratification is recorded:** the added text, and the same convention at CLAUDE.md at HEAD
- *Retrieve:* `git show 8c8e57eab9c031bb126f2521f378382e8fead1e6 --no-color -U0 -- CLAUDE.md`

### 2026-07-28 · `CLAUDE.md` @ `-724,0 +744,51` · 8c8e57eab9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cc): decision harvest — register rows + OI-207/208 notes (Task 0)
- **Ground.** The writing-standards pointer and the music-theory reserved-word convention with its disambiguation rule are added, each carrying "(user-directed, 2026-07-28)" or an earlier dated user attribution. No fact from the implementation is the source.
- **The act:** the writing-standards pointer and the music-theory reserved-word / disambiguation convention
- **Where its ratification is recorded:** the added text, and both conventions at CLAUDE.md at HEAD
- *Retrieve:* `git show 8c8e57eab9c031bb126f2521f378382e8fead1e6 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `CLAUDE.md` @ `-795,0 +796,14` · 80ad92f9d3

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cc): decisions register — Task 1 corrections (provenance re-aims, anchors, rewordings, derivation flags, STATUS order)
- **Ground.** The every-design-decision-carries-its-defense convention is added, its own opening "(user-directed, 2026-08-01, at the decisions-register ratification review)". The commit's account records it as a riding Cowork edit of that date.
- **The act:** the convention that every design decision carries its defense at its home
- **Where its ratification is recorded:** the added text, and the same convention at CLAUDE.md at HEAD
- *Retrieve:* `git show 80ad92f9d3dae1d0d51a696e402734215529ac24 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `ARCHITECTURE.md` @ `-721,0 +722,12` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** A scoping annotation is added, its own opening "★ Scoping annotation (user ruling, 2026-08-02, at the OI-234 decision-conflict adjudication — reading 3)". It scopes a standing finding to what it tested and states what it does not bear on; the ground given is the adjudication, not a reading of the code.
- **The act:** the OI-234 decision-conflict adjudication, reading 3
- **Where its ratification is recorded:** the added annotation itself, at ARCHITECTURE.md at HEAD
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-01 · `ARCHITECTURE.md` @ `-956,0 +969,27` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The MuseScore-Dependency Rule is added, its own heading carrying "(user-ratified 2026-08-02, at the OI-241 adjudication)", and its closing paragraph states the derivation from the already-ratified scoped forms.
- **The act:** the MuseScore-Dependency Rule
- **Where its ratification is recorded:** the added section heading itself, at ARCHITECTURE.md at HEAD
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-01 · `CLAUDE.md` @ `-151,0 +152,15` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The change adds the decisions-register section with its rules (a)–(e). The section's own heading carries "(shape user-ratified 2026-07-28; content + living surface 2026-08-02)", and the commit's account records the decisions register's 228 entries as user-ratified and the living surface as landing in this commit.
- **The act:** the decisions register ratified and made the living surface (its session-start read)
- **Where its ratification is recorded:** the section heading itself at CLAUDE.md at HEAD, and the ratification recorded in the decisions register's INDEX preamble
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `CLAUDE.md` @ `-189 +204` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The change adds the session-start read count, two files becoming three. The section's own heading carries "(shape user-ratified 2026-07-28; content + living surface 2026-08-02)", and the commit's account records the decisions register's 228 entries as user-ratified and the living surface as landing in this commit.
- **The act:** the decisions register ratified and made the living surface (its session-start read)
- **Where its ratification is recorded:** the section heading itself at CLAUDE.md at HEAD, and the ratification recorded in the decisions register's INDEX preamble
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `CLAUDE.md` @ `-192,0 +208,2` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The change adds the decisions-register INDEX added to the session-start reads. The section's own heading carries "(shape user-ratified 2026-07-28; content + living surface 2026-08-02)", and the commit's account records the decisions register's 228 entries as user-ratified and the living surface as landing in this commit.
- **The act:** the decisions register ratified and made the living surface (its session-start read)
- **Where its ratification is recorded:** the section heading itself at CLAUDE.md at HEAD, and the ratification recorded in the decisions register's INDEX preamble
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- CLAUDE.md`

### 2026-08-02 · `CLAUDE.md` @ `-826,0 +827,19` · b006dc15b5

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`  ·  *added by the ruled cut*
- **Commit subject:** docs(cowork): the three-phase sequencing rule ratified (D-231): specification completion, then issue-exhaustion, then ONE fix plan - no fix design before
- **Ground.** The three-phase sequencing rule is added, its own opening "(user-directed, 2026-08-02; sharpens #8 …)". This is the boundary commit itself — the act the ruled period opens exclusive at — and the hunk that writes the instruction whose truth half the eighteenth stop's diagnosis names.
- **The act:** D-231, the three-phase sequencing rule (specification completion, issue-exhaustion, one fix plan)
- **Where its ratification is recorded:** the added text, and the same rule at CLAUDE.md Conventions at HEAD
- *Retrieve:* `git show b006dc15b5f696f2fc86ad72b97fae58d2119cd7 --no-color -U0 -- CLAUDE.md`

---

# The WIDENED screen — the same method, over the ruled specification document set

> **The population is widened by MEMBERSHIP, not by role.** Its enumeration lives at `tools/audit/period_stratum_split.json` → `★_the_widened_screen_population` and is imported whole here, never re-listed (#6).

**What this is, honestly.** An AUTHORED VERDICT PER HUNK over a DERIVED population — the FLAG hunks of the candidate enumeration whose file is a member of the ruled specification document set. It finds POSITIVE EVIDENCE OF INFLUENCE ONLY, and it is bounded by the invisibility the original screen declares of itself: influence is invisible in the text, because a narrowed rule reads exactly like a rule that was always narrow. SO A CLEAN CLASS IS NOT A CERTIFICATE that a change was uninfluenced. That text is INHERITED from the screen this widens and is not re-argued here.

**The method is inherited whole.** The four classes, the ORDER they are applied in, the six reported shapes and the five STOPs are the existing screen's and are unchanged — "its method untouched" is Ruling 7's own clause. What is added is a SECOND POPULATION, a SECOND AUTHORED BLOCK for it, and two declared values: NOT YET READ, the one declared exception to the no-verdict STOP, and OUTSIDE NAMED SECTIONS, for a hunk of a section-scoped member falling outside the sections its delegation names.

**A code-influenced hunk HERE is not the period question's falsification.** The falsification rule at the head of this artifact belongs to the ORIGINAL screen and to its population, which is OUT-OF-PERIOD by construction: a code-influenced correction found THERE would mean the ruled period start is in the wrong place, and it re-opens that question. THIS population is deliberately wider — every stratum, in-period and out-of-period alike — because Ruling 7 asks it to MEASURE the pollution rather than to test the period. So an IN-PERIOD positively-code-influenced hunk here is the measurement's own subject and is EXPECTED: the period is defined as the programme under which the truth-sync happened. It is not a falsification of anything, and it must not be read as one. Each hunk records whether it is in period, so the two readings never have to be guessed apart.

**The existing sixty-eight are not re-read or re-graded.** A widened hunk that is ALREADY in the existing screen population inherits that hunk's existing verdict verbatim; no verdict of the original sixty-eight is re-authored, and the `verdicts` array above is byte-unchanged by this widening. Digest of the existing authored block: `32366793f298ff1c1d17422b61aed4660b0fdefe7aa201bc677ead0e0435320c`. Compare it across the runs of this batch. An identical value is a measurement that the existing authored block did not move; a different one means a verdict of the original sixty-eight changed, which the widening may not do.

## ★ The ruled failure signal — INCONCLUSIVE-AT-THIS-COVERAGE

*The rule as ruled.* Ruling 7, with the plan's §4: "if most passages land UNDETERMINED the premise is not measurable, and that is a STOP to the user, not a licence to proceed." It is not a licence to argue the class down either.

The widened population is not yet read whole, so a majority over the read members cannot be reported as the ruled signal firing. The read share is published beside the majority, and the ruling's own words are that a majority reached only because few members were read is reported this way rather than as the signal firing.

- Read members: **157** of **237** (read share 0.6624).
- UNDETERMINED among the read: **15** (share of the read 0.0955).

## The widened population

- **237 hunks** across **64 commits** and **17 documents** — **32** already screened and inherited, **205** new.
- By verdict: NOT YET READ 80, POSITIVELY CODE-INFLUENCED 42, RATIFIED-ACT EDIT 84, RESTRUCTURING-SHAPED 16, UNDETERMINED 15.

## The per-document pollution distribution

| member | hunks | read | POSITIVELY CODE-INFLUENCED | RATIFIED-ACT EDIT | RESTRUCTURING-SHAPED | UNDETERMINED | NOT YET READ | OUTSIDE NAMED SECTIONS | coverage gap | pollution input |
|---|---|---|---|---|---|---|---|---|---|---|
| `ARCHITECTURE.md` | 152 | 152 | 41 | 82 | 16 | 13 | 0 | 0 | — | MEASURED |
| `cowork_bounded_context_design.md` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | — | MEASURED |
| `cowork_confidence_contract.md` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — | MEASURED |
| `cowork_evidence_inventory.md` | 6 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | — | MEASURED |
| `cowork_idiom_entry_mapping.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at d9b2020623, 2026-06-30 |
| `cowork_joint_estimator_architecture.md` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | — | MEASURED |
| `cowork_joint_estimator_factorization.md` | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | — | MEASURED |
| `cowork_layer1_note_model_design.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at ce509b0961, 2026-07-03 |
| `cowork_layer2_slicing_design.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at ce509b0961, 2026-07-03 |
| `cowork_layer3_keymode_design.md` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — | MEASURED |
| `cowork_layer4_chordsymbol_design.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at a31b56639d, 2026-07-05 |
| `cowork_layer5_engagement_design.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at 416b7d6215, 2026-07-10 |
| `cowork_layer5_function_design.md` | 5 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | — | MEASURED |
| `cowork_layer6_grouping_design.md` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | — | MEASURED |
| `cowork_notation_adoption_increment.md` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | — | MEASURED |
| `cowork_notation_output_contract.md` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | — | MEASURED |
| `cowork_phrase_boundary_design.md` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | — | MEASURED |
| `cowork_prefit_gates.md` | 5 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | — | MEASURED |
| `cowork_progression_schema_design.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at ce509b0961, 2026-07-03 |
| `cowork_progression_schema_dictionary.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at ce509b0961, 2026-07-03 |
| `cowork_score_census.md` | 6 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | — | MEASURED |
| `cowork_stage5_fitter_design.md` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | — | MEASURED |
| `cowork_target_architecture.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at ce509b0961, 2026-07-03 |
| `cowork_voiceleading_axis_design.md` | 5 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | — | MEASURED |
| `docs/llm_integration.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **yes** | NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at 5b08465924, 2026-06-07 |
| `docs/scoring_model.md` | 31 | 5 | 1 | 2 | 0 | 2 | 26 | 0 | — | MEASURED |

## The coverage gap — the members the screen cannot see at all

Every document-set member with NO FLAG hunk in the candidate enumeration, with the reason the enumeration gives for ITSELF rather than a reason invented here. This is the plan's own finding about the premise's measurability: a member with no flagged hunk contributes nothing to the pollution distribution, and the distribution must be read knowing which members are silent and why.

**The declared third value of the pollution input, as ruled.** Ruling 2(b) of `cowork_rulings_2026_08_22_step_zero_return_sitting.md`: "ONLY the pollution input of Ruling 12 is affected. For each of the nine, the July screen's per-document value is recorded as a DECLARED THIRD VALUE — 'NOT EDITED IN THE RESTRUCTURING PERIOD; last authored before it, at <commit, date>' — derived by the generator from the candidate enumeration and from git, never hand-typed (#17f, D-431). It is distinct from a measured distribution and from 'clean': the screen measures corrections made toward the code DURING the period and has never measured authoring-time influence for any member; the fact-gate tests that, per statement, for every source."

**9 of 26 members carry no flagged hunk in the candidate enumeration.**

- `cowork_idiom_entry_mapping.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_layer1_note_model_design.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_layer2_slicing_design.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_layer4_chordsymbol_design.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_layer5_engagement_design.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_progression_schema_design.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_progression_schema_dictionary.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `cowork_target_architecture.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.
- `docs/llm_integration.md` — NO hunk of this file is in the candidate enumeration. The enumeration's own commit population is the restructuring period — opening EXCLUSIVE at 9306dc5072153dec647b227725f626f8741f8c1b, ending at f2da61f8cd142a5bd6c2bb3ee2a6539d1f5dca37, 435 commits — so a file no commit of that population touched has nothing to enumerate. The file does not appear in the enumeration's `files` table at all.

## What remains UNREAD, per document

Recorded so that a continuing session derives the remainder fresh rather than carrying it from this session's account of it. The order below is the artifact's own — by document, then by commit, then by hunk.

- `cowork_bounded_context_design.md` — **4** unread
- `cowork_confidence_contract.md` — **1** unread
- `cowork_evidence_inventory.md` — **6** unread
- `cowork_joint_estimator_architecture.md` — **2** unread
- `cowork_joint_estimator_factorization.md` — **9** unread
- `cowork_layer3_keymode_design.md` — **1** unread
- `cowork_layer5_function_design.md` — **5** unread
- `cowork_layer6_grouping_design.md` — **1** unread
- `cowork_notation_adoption_increment.md` — **2** unread
- `cowork_notation_output_contract.md` — **3** unread
- `cowork_phrase_boundary_design.md` — **2** unread
- `cowork_prefit_gates.md` — **5** unread
- `cowork_score_census.md` — **6** unread
- `cowork_stage5_fitter_design.md` — **2** unread
- `cowork_voiceleading_axis_design.md` — **5** unread
- `docs/scoring_model.md` — **26** unread

## Every NEW hunk read so far, with its verdict and its ground

### 2026-08-02 · `ARCHITECTURE.md` @ `-250,0 +251,45` · f833a2d2a9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)
- **Ground.** The commit's own account is "phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)", and it states what it is: every register entry whose home was a documentation gap or a tracking surface is written into the specification that owns it, "in that specification's own voice, with its defense and its ratifying date". The hunk adds text that carries its own ratification date. No fact about the implementation is the source of the addition, and nothing the documentation already stated is withdrawn or narrowed by it. Here the added block is the joint estimator's standing rules, and each rule carries its own ratifying date inside the added text — "Ratified by the user 2026-07-17", "Protocols ratified 2026-07-19", the OI-178 adoption "user-ratified 2026-07-26". The block also NAMES an unresolved tension (the key axis against §5.7a) and leaves it unsettled, which is a homing act recording a decision rather than taking one.
- **The act:** the D-231 phase-1 homing of the joint estimator's four standing rules into their owning specification
- **Where its ratification is recorded:** each rule's own ratifying date inside the added text; and D-231 itself at `CLAUDE.md` Conventions at HEAD
- *Retrieve:* `git show f833a2d2a9f4fd389da913fb17b9ff3b558012ec --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-843,0 +889,60` · f833a2d2a9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)
- **Ground.** The commit's own account is "phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)", and it states what it is: every register entry whose home was a documentation gap or a tracking surface is written into the specification that owns it, "in that specification's own voice, with its defense and its ratifying date". The hunk adds text that carries its own ratification date. No fact about the implementation is the source of the addition, and nothing the documentation already stated is withdrawn or narrowed by it. Here the added text is §2.15's three cross-cutting contracts and the new §2.16, and every one carries its own attribution — "Ratified by the user 2026-07-02", "ratified by the user 2026-07-06", "Ratified by the user 2026-07-10 and amended 2026-07-12", and "Two requirements the user stated on 2026-07-28".
- **The act:** the D-231 phase-1 homing of the cross-layer confidence contract, the negative-evidence rule, the fact-publication corollary and the two standing design requirements
- **Where its ratification is recorded:** each contract's own attribution inside the added text; and the same rules at `CLAUDE.md` at HEAD
- *Retrieve:* `git show f833a2d2a9f4fd389da913fb17b9ff3b558012ec --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3654 +3759,6` · f833a2d2a9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)
- **Ground.** The commit's own account is "phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)", and it states what it is: every register entry whose home was a documentation gap or a tracking surface is written into the specification that owns it, "in that specification's own voice, with its defense and its ratifying date". The hunk adds text that carries its own ratification date. No fact about the implementation is the source of the addition, and nothing the documentation already stated is withdrawn or narrowed by it. Here the hunk QUALIFIES §5.12's Status line by recording that the two-pass pedal detector is superseded as a DESIGN by the voice-independent class, "user-ratified 2026-07-26". ★ The first class was tested and does not fire: the qualification's ground — that the two-pass detector can only see the lowest voice — is stated by §5.12's own text, which specifies the detector on the lowest-pitched tone, so it is available from the documentation and is not a fact read in implementation code this commit did not write.
- **The act:** the voice-independent pedal-point ruling of the notation-adoption increment
- **Where its ratification is recorded:** the added text's own "user-ratified 2026-07-26"; and §7.4 at HEAD, which states the ratifying surface as `cowork_notation_adoption_increment.md` §7 + §10
- *Retrieve:* `git show f833a2d2a9f4fd389da913fb17b9ff3b558012ec --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-4230,0 +4341,13` · f833a2d2a9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)
- **Ground.** The commit's own account is "phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)", and it states what it is: every register entry whose home was a documentation gap or a tracking surface is written into the specification that owns it, "in that specification's own voice, with its defense and its ratifying date". The hunk adds text that carries its own ratification date. No fact about the implementation is the source of the addition, and nothing the documentation already stated is withdrawn or narrowed by it. Here the added block is §7.4's voice-independent pedal-point class (D-207), "user-ratified 2026-07-26". ★ The first class was tested and does not fire, and the call is recorded because it is close: the added text DOES cite implementation code this commit did not write (`chordpostpasses.cpp:275`) and DOES supersede a standing pair of published facts. What decides it is that the code citation is offered as the DESIGN reason the legacy mechanism is inadequate, not as a fact against which a documentation statement was found false — the supersession's source is the user's ratification, which the text names.
- **The act:** the voice-independent pedal-point class of the ornament vocabulary (D-207)
- **Where its ratification is recorded:** the added text's own "user-ratified 2026-07-26" and its naming of the ratifying surface `cowork_notation_adoption_increment.md` §7 + §10
- *Retrieve:* `git show f833a2d2a9f4fd389da913fb17b9ff3b558012ec --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-4655,0 +4779,11` · f833a2d2a9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)
- **Ground.** The commit's own account is "phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)", and it states what it is: every register entry whose home was a documentation gap or a tracking surface is written into the specification that owns it, "in that specification's own voice, with its defense and its ratifying date". The hunk adds text that carries its own ratification date. No fact about the implementation is the source of the addition, and nothing the documentation already stated is withdrawn or narrowed by it. Here the added block is §11's HELD status and the declaration that intonation is a named future CONSUMER of the analysis, "user-decided 2026-07-13", quoting the user's own stated dependency.
- **The act:** the user's decision of 2026-07-13 that intonation is held and is a declared future consumer of the analysis (D-206)
- **Where its ratification is recorded:** the added text's own "user-decided 2026-07-13"; the row it names, `OPEN_ITEMS.md` OI-62
- *Retrieve:* `git show f833a2d2a9f4fd389da913fb17b9ff3b558012ec --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-6239,0 +6374,11` · f833a2d2a9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)
- **Ground.** The commit's own account is "phase 1 Task 1 — the homing acts (20 decisions written into their owning specifications)", and it states what it is: every register entry whose home was a documentation gap or a tracking surface is written into the specification that owns it, "in that specification's own voice, with its defense and its ratifying date". The hunk adds text that carries its own ratification date. No fact about the implementation is the source of the addition, and nothing the documentation already stated is withdrawn or narrowed by it. Here the added block is §16's rule that a HUMAN acts as ground truth where none is published, "user-decided 2026-07-13", with the language-model judge admitted as triage and explicitly never as a grader.
- **The act:** the user's decision of 2026-07-13 that a human is ground truth where none is published (D-205)
- **Where its ratification is recorded:** the added text's own "user-decided 2026-07-13"; the rows it names, `OPEN_ITEMS.md` OI-38 and OI-56
- *Retrieve:* `git show f833a2d2a9f4fd389da913fb17b9ff3b558012ec --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-39,4 +39,9` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the STAGED-SCOPE clause, which said the in-app notation layer stays on the legacy pipeline, with the statement that the switch closed the migration on both surfaces; its own parenthesis says the replaced sentence "the switch made false". The correction's own text cites the flag default at `composingconfiguration.cpp:178`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-138,2 +143,4` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the layer-sections scope note, which had the two surfaces the wrong way round; its own parenthesis says the replaced sentence said "the legacy pipeline was still live on the notation path". The correction's own text cites the notation switch and the resulting dormant-compiled state of both surfaces, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-819 +826,4` · ab336f43b5

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. ★ BUT THIS HUNK IS NOT A CORRECTION AGAINST THE IMPLEMENTATION. It replaces the parenthetical "ratification-gated" with "RATIFIED by the user 2026-07-02" — a statement about a RULING, corrected against the ruling record, with no fact from the code in its source. The first class was applied first and does not fire; the second does, and the hunk records what a named user act ratified.
- **The act:** the user's ratification of review amendment A-1, the cross-layer confidence and calibration contract, on 2026-07-02
- **Where its ratification is recorded:** `cowork_confidence_contract.md`'s own banner, "Status: RATIFIED (user, 2026-07-02)"; and the corrected parenthesis itself at `ARCHITECTURE.md` at HEAD
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-821 +831,2` · ab336f43b5

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. ★ BUT THIS HUNK CARRIES NONE OF THAT. It appends one sentence re-pointing the reader to where the contract's own rule and defense are stated, in the list below. No standing statement is withdrawn, no code fact is its source, and no user act is recorded — it is a pointer added inside the document.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-823,2 +834,12` · ab336f43b5

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. ★ BUT THIS HUNK CORRECTS THE DOCUMENT'S ACCOUNT OF ITSELF, NOT OF THE CODE. It withdraws the claim that the span-typology rename was "propagated through every layer spec" and states what it actually covered — established by reading THIS document, which still uses the banned bare word in four headings the correction names. Its source is the document's own text; nothing from the implementation appears in it. The shape is reported as a re-heading because the subject of both the original claim and the correction is a renaming programme; it is the nearest of the six inherited shapes and no seventh is invented.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1236 +1257,13` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES Layer 3's build-state tag `Built+Live` with `Built+Dormant` and adds the verification; its own heading is "Build-state correction" and it says the tag "the two adoptions made false". The correction's own text cites all four production call sites — `notationcomposingbridge.cpp:324-328` and `:1509-1513`, `notationimplodebridge.cpp:1434-1441`, `notationtuningbridge.cpp:794` — and the flag default at `composingconfiguration.cpp:178`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1290 +1323,10` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES Layer 4's heading clause "engages with L5", which "no longer describes anything scheduled", and records that the plan was overtaken without any ruling naming it. The correction's own text cites the state of the production inference layer on both surfaces since the two adoptions, which this commit did not write. The source is what the implementation became, established at the adoptions rather than at a ruling — the hunk's own words are "a supersession in fact, not by decision".
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1362,4 +1404,8` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the voice-leading layer's description "not built"; its own parenthesis says the entry "said 'not built', contradicting §2.15 in the same document". The correction's own text cites the built-and-dormant state of the axis-2 foundation (VL-A/VL-B/VL-C), which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1622,0 +1669,3` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the note recording that the documented bit order was wrong, correcting the listing against the header it claims to reproduce. The correction's own text cites `chordanalyzer.h:213-230`, which this commit did not write. The added note states the consequence itself: "a reader deriving a mask from this listing would be wrong".
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1628,2 +1677,2` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk SWAPS the documented bits 4 and 5 of the Extension mask, correcting the listing against the header it claims to reproduce. The correction's own text cites `chordanalyzer.h:213-230`, which this commit did not write. The added note states the consequence itself: "a reader deriving a mask from this listing would be wrong".
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1633,2 +1682,2` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk SWAPS the documented bits 9 and 10 of the Extension mask, correcting the listing against the header it claims to reproduce. The correction's own text cites `chordanalyzer.h:213-230`, which this commit did not write. The added note states the consequence itself: "a reader deriving a mask from this listing would be wrong".
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1638,2 +1687,2` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk SWAPS the documented bits 14 and 15 of the Extension mask, correcting the listing against the header it claims to reproduce. The correction's own text cites `chordanalyzer.h:213-230`, which this commit did not write. The added note states the consequence itself: "a reader deriving a mask from this listing would be wrong".
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1641,0 +1691,2` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the note recording that four fields were missing from the documented field list. The correction's own text cites the `ChordIdentity` definition the listing claims to reproduce, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1643 +1694` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the documented meaning of `score` — "Raw confidence. Higher is better. Not normalized." becomes "Raw template-match score. Higher is better. Ranking only." The correction's own text cites what the field actually is in the scorer, which this commit did not write. A documented statement about what a published value MEANS, corrected against the code that produces it.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1647,0 +1699` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS `naturalFifthPresent` to the documented field list, re-syncing it with the struct. The correction's own text cites the `ChordIdentity` definition in the code, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1648,0 +1701` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS `tiePriority` to the documented field list, re-syncing it with the struct. The correction's own text cites the `ChordIdentity` definition in the code, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1649,0 +1703,3` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS `isPedalPoint` and `pedalBassPc` to the documented field list, re-syncing it with the struct. The correction's own text cites the `ChordIdentity` definition in the code, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1685 +1741,4` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the documented default of `bassNoteRootBonus`, 0.65 with 0.70. The correction's own text cites the code default at `analysis/types/analysistypes.h:196`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1718 +1777` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the gates' documented home and drops Gate K from the list of live calibrated thresholds. The correction's own text cites `postscoringgates.cpp`, where the two surviving margin constants are declared, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1726,0 +1786,9` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the two corrections in full — the gates' home, and Gate K's retirement, which made listing it "as a live calibrated threshold false". The correction's own text cites `postscoringgates.cpp:46`, `:47`, `:49` and `:523`, which this commit did not write. It also records that the same retired threshold is still listed in `CLAUDE.md` and that correcting a governing document was outside the pass's scope — an owed correction named rather than taken.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1769 +1837,2` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §4.1b's restatement of the same constant, 0.65 with 0.70. The correction's own text cites the same code default, cited as OI-107(a), which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1787,4 +1856,20` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk MARKS §4.1b's safety constraint superseded and states the constraint that actually survives, "read off the code", noting that it differs between the two predicates. The correction's own text cites `chordanalyzer.cpp:855-870` and `:829-853`, which this commit did not write. Its closing sentence states the direction of the correction exactly: "No code change is owed — the code is the later behaviour and is correct; what was owed was saying so here."
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-2239 +2324,7` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the backlog item's status with PARTLY DONE and states which half was done. The correction's own text cites `analysis/chord/chordsymbolformatter.cpp` and the absence of a `chordsymbolformatter.h`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-2818 +2909,6` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §4.3's single "File:" line, which "predated refactor-1". The correction's own text cites the split between the declaring header and the implementing translation unit, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-2867,3 +2963,6` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the Roman-numeral scope paragraph, which said extensions beyond the 7th are "not yet emitted". The correction's own text cites `chordsymbolformatter.cpp:590-616`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3032 +3131,3` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES AnalysisUtils' documented path, which omitted the `chord/` component. The correction's own text cites the header as it stands at `analysis/chord/analysisutils.h`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3034 +3135,2` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the one-line description of what the leaf is. The correction's own text cites the header as it stands at `analysis/chord/analysisutils.h`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3039,0 +3142,5` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the three functions the listing was missing. The correction's own text cites the header as it stands at `analysis/chord/analysisutils.h`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3753,3 +3860,10` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §5.11's assertion that the augmented-sixth labels are "Gated to Standard and Baroque presets only", which "the code defers exactly". The correction's own text cites `chordsymbolformatter.cpp:882-883`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3838,2 +3952,13` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §5.13's claim that there is "no path-selection flag", which was "false at HEAD". The correction's own text cites `notationcomposingbridge.cpp:728-738`, `:703`, `:621`, `:1385`, `notationimplodebridge.cpp:1409-1431`, `notationtuningbridge.cpp:794` and the flag default at `composingconfiguration.cpp:178`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3842,0 +3968,3` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the sentence declaring what each row of the rebuilt table means at HEAD. The correction's own text cites `notationcomposingbridge.cpp:728-738`, `:703`, `:621`, `:1385`, `notationimplodebridge.cpp:1409-1431`, `notationtuningbridge.cpp:794` and the flag default at `composingconfiguration.cpp:178`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-3845,7 +3973,27` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES the whole entry-point table, every row rebuilt against what runs. The correction's own text cites `notationcomposingbridge.cpp:728-738`, `:703`, `:621`, `:1385`, `notationimplodebridge.cpp:1409-1431`, `notationtuningbridge.cpp:794` and the flag default at `composingconfiguration.cpp:178`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-4677,0 +4826,8` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the premise correction to §10.0, recording that its prerequisite and "the whole premise above are false at HEAD". The correction's own text cites the production annotation path, which "never calls `greedyExpandSegmentation()`", which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-5591,4 +5747,13` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §11.5's status and its account of what the implode action runs. The correction's own text cites `notationimplodebridge.cpp:1409-1431` and `:1434-1441`, and the declared-versus-defined split at `notationcomposingbridge.h:161` / `notationharmonicrhythmbridge.cpp:69`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-5998,3 +6163,22` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §12.1a's two clauses — "analysis cost is negligible (well under 1ms)" and "suppressing the display does not require skipping the analysis" — both of which the correction states are "false on the production path". The correction's own text cites the note-seam funnel's whole-score decode and the measurement at `tools/joint_estimator/noteseam_latency.json`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-6008,2 +6192,4` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk REPLACES §12.1b's claim that two actions are registered. The correction's own text cites `notationuiactions.cpp:1402`–`:1432`, `notationcontextmenumodel.cpp:174` and `:210-214`, and `notationactioncontroller.cpp:387`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-6016,3 +6202,22` · ab336f43b5

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. This hunk ADDS the seven further actions, each with its registration site, and records the right-click chord anchor with "derivation not recorded". The correction's own text cites `notationuiactions.cpp:1402`–`:1432`, `notationcontextmenumodel.cpp:174` and `:210-214`, and `notationactioncontroller.cpp:387`, which this commit did not write.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-6307 +6512` · ab336f43b5

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. ★ BUT THIS HUNK IS A HEADING RE-MARK whose source is the project's own work history, not the code: `*(next)*` becomes `*(not started; NOT the next thing)*`. No fact read in implementation code is its source.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-6313,0 +6519,6` · ab336f43b5

- **Verdict:** RESTRUCTURING-SHAPED · shape `new-document-content`
- **Commit subject:** docs: phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)
- **Ground.** The commit's own account is "phase 1 Task 2 — the truth-sync (every named false specification statement corrected at HEAD)", and it states the correction's direction in terms: "a specification cannot be the compliance standard while it misdescribes the code, so every statement the named open-items rows establish as false at HEAD is corrected". That is the first class's second limb, word for word. ★ BUT THIS HUNK'S SOURCE IS THE PROJECT'S OWN WORK HISTORY, not the code: it adds the correction paragraph for the heading above, whose ground is that "no session since 2026-04 has treated [Phase 3] as the next thing". It leaves when the phase becomes next OPEN and settles nothing.
- *Retrieve:* `git show ab336f43b5e5610077488117a8a3a1ea32cec440 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1333,0 +1334,11` · 19fbe9e271

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs: phase 1d Task 0 — the two riding acts (OI-265 truth-sync, OI-266's six rules homed)
- **Ground.** The commit's own account is "phase 1d Task 0 — the two riding acts (OI-265 truth-sync, OI-266's six rules homed)", and this hunk is the truth-sync half. It adds a scope note to Layer 4 which states in terms that the section "carries one sentence about what runs — that production chord analysis still runs the legacy `analyzeChord` + post-scoring gates (§4.1) — which was true when written and is **false at HEAD**". That is a documentation statement found false against the implementation, and the correction cites the flag default at `composingconfiguration.cpp:178`, which this commit did not write.
- *Retrieve:* `git show 19fbe9e2714f3f5d65db753e4d999e57e7f15649 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-281,0 +282,2` · ebda0889f2

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1i task 3 — the pointer pass (6 lines, pointer class only), 25 more entries contract-homed, 159 anchors re-aimed
- **Ground.** The commit's own account is "phase 1i task 3 — the pointer pass (6 lines, pointer class only)", and it states its own bound: "Every ARCHITECTURE.md insertion is the ratified POINTER class — a one-line delegation pointer or a one-line tried-and-closed pointer. No content was copied and no ruling was made; the whole diff is 12 added lines and nothing else." The first class was applied first and does not fire: nothing standing is withdrawn and no fact from the implementation is the source. What the hunk records is the fifth home case, which the added line itself dates. Here the added line is the delegation pointer to the fitting event's own design contract.
- **The act:** the fifth home case — a ratified contract document the owning `ARCHITECTURE.md` section points at is a proper home — and the pointer pass performed under it
- **Where its ratification is recorded:** the added line's own "(the fifth home case, user-ratified 2026-08-02)"; and the same rule at `CLAUDE.md`'s decisions-register section, rule (g), at HEAD
- *Retrieve:* `git show ebda0889f2f6c6076df4a0041008733b8d2296d8 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-293,0 +296,2` · ebda0889f2

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1i task 3 — the pointer pass (6 lines, pointer class only), 25 more entries contract-homed, 159 anchors re-aimed
- **Ground.** The commit's own account is "phase 1i task 3 — the pointer pass (6 lines, pointer class only)", and it states its own bound: "Every ARCHITECTURE.md insertion is the ratified POINTER class — a one-line delegation pointer or a one-line tried-and-closed pointer. No content was copied and no ruling was made; the whole diff is 12 added lines and nothing else." The first class was applied first and does not fire: nothing standing is withdrawn and no fact from the implementation is the source. What the hunk records is the fifth home case, which the added line itself dates. Here the added line is the tried-and-closed pointer on the search.
- **The act:** the fifth home case — a ratified contract document the owning `ARCHITECTURE.md` section points at is a proper home — and the pointer pass performed under it
- **Where its ratification is recorded:** the added line's own "(the fifth home case, user-ratified 2026-08-02)"; and the same rule at `CLAUDE.md`'s decisions-register section, rule (g), at HEAD
- *Retrieve:* `git show ebda0889f2f6c6076df4a0041008733b8d2296d8 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1270,0 +1275,4` · ebda0889f2

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1i task 3 — the pointer pass (6 lines, pointer class only), 25 more entries contract-homed, 159 anchors re-aimed
- **Ground.** The commit's own account is "phase 1i task 3 — the pointer pass (6 lines, pointer class only)", and it states its own bound: "Every ARCHITECTURE.md insertion is the ratified POINTER class — a one-line delegation pointer or a one-line tried-and-closed pointer. No content was copied and no ruling was made; the whole diff is 12 added lines and nothing else." The first class was applied first and does not fire: nothing standing is withdrawn and no fact from the implementation is the source. What the hunk records is the fifth home case, which the added line itself dates. Here the added line is Layer 3's delegation pointer and its tried-and-closed line.
- **The act:** the fifth home case — a ratified contract document the owning `ARCHITECTURE.md` section points at is a proper home — and the pointer pass performed under it
- **Where its ratification is recorded:** the added line's own "(the fifth home case, user-ratified 2026-08-02)"; and the same rule at `CLAUDE.md`'s decisions-register section, rule (g), at HEAD
- *Retrieve:* `git show ebda0889f2f6c6076df4a0041008733b8d2296d8 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-02 · `ARCHITECTURE.md` @ `-1333,0 +1342,4` · ebda0889f2

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1i task 3 — the pointer pass (6 lines, pointer class only), 25 more entries contract-homed, 159 anchors re-aimed
- **Ground.** The commit's own account is "phase 1i task 3 — the pointer pass (6 lines, pointer class only)", and it states its own bound: "Every ARCHITECTURE.md insertion is the ratified POINTER class — a one-line delegation pointer or a one-line tried-and-closed pointer. No content was copied and no ruling was made; the whole diff is 12 added lines and nothing else." The first class was applied first and does not fire: nothing standing is withdrawn and no fact from the implementation is the source. What the hunk records is the fifth home case, which the added line itself dates. Here the added line is Layer 4's delegation pointer and its tried-and-closed line.
- **The act:** the fifth home case — a ratified contract document the owning `ARCHITECTURE.md` section points at is a proper home — and the pointer pass performed under it
- **Where its ratification is recorded:** the added line's own "(the fifth home case, user-ratified 2026-08-02)"; and the same rule at `CLAUDE.md`'s decisions-register section, rule (g), at HEAD
- *Retrieve:* `git show ebda0889f2f6c6076df4a0041008733b8d2296d8 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-258,2 +258,3` · 88fd87e9d1

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit is the phase-1j homing half, and this hunk is its heading half: the standing-rules heading is re-worded from "Four rules" to "Six rules" and its subject list extended, to keep the heading in step with the two rules the SAME commit adds below. Nothing outside the document is its source — not a fact read in implementation code, and not a ruling; the source is the commit's own addition. It is a re-heading.
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-305,0 +307,24` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is rules (e) and (f) of the joint estimator's standing rules — the shipped-value licence pool and the per-idiom fit. The added text carries its own dates: "Ratified by the user 2026-07-04 … reaffirmed as written by the user 2026-08-02", and for (f) "Ratified by the user; the record does not date the mandate" — the gap stated rather than filled.
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-937,0 +963,9` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is the boundary of the no-information-loss rule — never COMPUTING a possibility is not loss, only DISCARDING a computed one is. The added text records its own provenance honestly: "Decided 2026-07-07; the record does not name the ratifier."
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-948,0 +983,10` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is the rule that the analysis always emits its fullest reading and that simplifying is a comparison-side act only. The added text states "the record states neither a date nor a ratifier for the rule itself", so the homing records a gap rather than inventing an attribution.
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-1117,0 +1162,10` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is clause 4 of the MuseScore-dependency rule — reading and calling MuseScore's engraving code is allowed; only editing it is off limits. The added text names the act: "a user correction, 2026-06-14, of an over-statement that had conflated the two".
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-1278,0 +1333,9` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is the rule that Layer 3's backward re-reading facility stays switched off in the shipped configuration. The added text names the act and its date: "Decided by the user 2026-07-02."
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-1345,0 +1409,8` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is the deferral of non-chord-tone detection, with the shape it is constrained to in advance. The added text states "**derivation not recorded**" and "The record states neither a date nor a ratifier" — the gap written down rather than filled.
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-1411,0 +1483,2` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is Layer 5's delegation pointer to the engagement contract, with its TRANSITIVE authority stated. The added line carries "(the fifth home case, user-ratified 2026-08-02)" and names the user-ratified surface the authority passes through.
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-2561,0 +2635,10` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is the rule that the annotation ban is decided by WHAT AN ANNOTATION SAYS rather than by how the score stores it. The added text states "**derivation not recorded**" and that the record names neither a date nor a ratifier.
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-2565,0 +2649,13` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is the standing consequence that jazz accuracy is not measurable on the corpora held, and that no jazz-specific scoring work is planned on them. The added text names the measurement it rests on — the bass-injection experiment — and records "Decided 2026-04-08; the record does not name the ratifier."
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-6169,0 +6266,8` · 88fd87e9d1

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)
- **Ground.** The commit's own account is "phase 1j task 1 — the OI-272 HOMING half (16 rules written into their owning specifications)". The hunk writes a rule the decisions register already held into the specification that owns it, in that specification's own voice and with its defense. The first class was applied first and does not fire: nothing the documentation already stated is withdrawn or narrowed, and no fact read in implementation code this commit did not write is the source of the addition. Here the rule written in is §12's governing requirement of zero information loss to the end user. The added text records "Ratified by the user; the record does not date it."
- **The act:** the D-231 phase-1 homing act of 2026-08-02, writing a recorded decision into its owning specification
- **Where its ratification is recorded:** D-231 itself at `CLAUDE.md` Conventions at HEAD, which directs the homing; and, where the homed rule's own ratification is recorded, the date the added text carries
- *Retrieve:* `git show 88fd87e9d16e2eacca38c9dd8ea4c1e4a43d7b27 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-970 +970` · 3fbece9c1a

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): phase 1j self-check correction — D-297's homed text said 'slices' where the record says cases
- **Ground.** The hunk REPLACES one word of a standing statement in §2.15 — the shelved joint step's measured fire rate, stated as a percentage "of slices", becomes a percentage "of cases". ★ The first class was applied first and does NOT fire: the commit's own account names the source, and it is the record rather than the code — "the shelved joint step's measured fire-rate is stated over regions, and the homed §2.15 text called the same quantity a percentage of slices. Corrected to 'cases', which is what the source claim supports without asserting a unit." No fact read in implementation code is its source, and the account does not say the statement was corrected against the implementation. ★ Nor does the second class fire — no user act is named, the correction being the standing self-check's own product — and the third does not, because the hunk replaces a standing statement rather than relocating, splitting, re-heading or growing text. NOT CLEARED: the statement it corrects is about MEASURED behaviour of the system, and the screen cannot clear a correction of such a statement as restructuring.
- *Retrieve:* `git show 3fbece9c1a6570df394839f4b87e9094e44eeb94 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-4505,2 +4505,4` · 7454abe5db

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1k tasks 1-4 — the five 2026-08-03 rulings APPLIED (banners, nine ratifications, the §6.7 taxonomy correction, D-131/D-132)
- **Ground.** The commit's own account is "phase 1k tasks 1-4 — the five 2026-08-03 rulings APPLIED", and it states its own scope: "Documentation and register work only: no src/ change, no golden refresh, no tools/corpus/ or tools/robust_stop/ movement, no behavior change, no fix, no design." The ruling this hunk carries is R3, which the account states as "ARCHITECTURE.md §6.7 restated over the five idioms". Here the hunk REPLACES §6.5's terminology note, whose examples named the retired genre families, with the five idioms — and the replacement carries its own dated attribution inside the added text: "(Corrected 2026-08-03 with the §6.7 restatement — this note previously gave the retired genre families 'Baroque, swing, bebop' as its examples.)" ★ The first class was applied first and does not fire: a standing statement IS replaced, but its source is the §6.7 restatement the same ruling orders, and no fact read in implementation code is cited anywhere in the added text.
- **The act:** the user's ruling R3 of 2026-08-03 — the §6.7 taxonomy restatement over the five idioms — carried into §6.5 in the same act so the restatement does not leave the terminology note contradicting the section it cites
- **Where its ratification is recorded:** the added text's own "(Corrected 2026-08-03 with the §6.7 restatement …)"; the commit's own account naming the surface the rulings were taken at, `cowork_pending_ratifications_next_session.md`, and the dispatch that applied them, `cc_instruction_phase1k_apply_rulings.md`
- *Retrieve:* `git show 7454abe5db4e169fcbdc43440c018b1add4db31b --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-4528,9 +4530,51` · 7454abe5db

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1k tasks 1-4 — the five 2026-08-03 rulings APPLIED (banners, nine ratifications, the §6.7 taxonomy correction, D-131/D-132)
- **Ground.** The commit's own account is "phase 1k tasks 1-4 — the five 2026-08-03 rulings APPLIED", and it states its own scope: "Documentation and register work only: no src/ change, no golden refresh, no tools/corpus/ or tools/robust_stop/ movement, no behavior change, no fix, no design." The ruling this hunk carries is R3, which the account states as "ARCHITECTURE.md §6.7 restated over the five idioms". Here the hunk REPLACES §6.7's genre taxonomy with the five idioms and their two orthogonal cross-attributes, and every load-bearing clause carries its own attribution inside the added text — "Ratified by the user 2026-06-30 and ENCODED" — with the discovery study's own figures as the defense and the superseded genre list preserved beneath it as historical context (#12). ★ The first class was applied first and does not fire, and the call is recorded because it is close: the added text DOES state something about the code — that the placeholder `{Baroque, Jazz, Default}` StyleTag is retired and replaced in the dormant `harmonicvocabulary` component by `enum class Idiom` + `IdiomSet`. What decides it is that every citation offered for that statement is a record document (`cowork_style_taxonomy_proposal.md`, `cowork_progression_schema_dictionary.md`) and none is implementation code; the encoding is recorded as part of what the 2026-06-30 ratification settled, not as a fact against which a documentation statement was found false.
- **The act:** the user's ratification of the five-idiom taxonomy on 2026-06-30, applied to `ARCHITECTURE.md` §6.7 by the user's ruling R3 of 2026-08-03
- **Where its ratification is recorded:** the added text's own "Ratified by the user 2026-06-30 and ENCODED"; and the commit's own account of R3, taken at `cowork_pending_ratifications_next_session.md`
- *Retrieve:* `git show 7454abe5db4e169fcbdc43440c018b1add4db31b --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-270,0 +271,2` · 1b8ecaf685

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1m — the D-416 disposition (one mandate, three components), five stale "parked" statements corrected, the LEGACY marker weakened, and two measurements run without being applied
- **Ground.** The hunk ADDS one paragraph beside the joint estimator's standing rule (a), and the added text declares what it is in its own opening words: "Pointer, not a seventh rule (added 2026-08-03 on the user's D-416 ruling; register entry D-429)". It records that the 2026-06-14 mandate to dissolve the legacy post-hoc gate-correction layer carries a principle binding on this estimator, and states in terms that the mandate is NOT treated as discharged. ★ The first class was applied first and does not fire: nothing standing is withdrawn, and no fact read in implementation code appears in the added text. The commit's account DOES report a dispatch premise refuted at the code — that the gate layer is unreachable on the live notation arm — but that refutation is recorded in the register entry and in the row it names, not in this hunk.
- **The act:** the user's D-416 ruling of 2026-08-03 (the fourth ruling set of that date), which split the two-deferred-refactors mandate into its three components and transferred component (2)'s principle to the phase-3 family design
- **Where its ratification is recorded:** the added text's own "added 2026-08-03 on the user's D-416 ruling"; the dispatch the commit names, `cc_instruction_phase1m_dispositions_and_measurements.md`; and register entry D-429
- *Retrieve:* `git show 1b8ecaf685295024cdeafee067332ca38b26be04 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-50,0 +51,6` · 1642c48e7f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1r — the write list committed, D-430's verbatim re-taken over the granularity clause, 215 anchors re-aimed, and the re-classification re-run against the user's six delegations
- **Ground.** The commit's own account opens "The user wrote all six delegations the phase-1q write list asked for (OI-293). This commit records them and re-runs every downstream act against them." Each of this commit's `ARCHITECTURE.md` hunks carries that attribution inside its own added text. ★ The first class was applied first and does not fire on any of them: no fact read in implementation code is cited in any added passage, and where a standing statement IS replaced the source is the user's own direction. Here the hunk ADDS the delegation pointer for the pre-fit protocols, naming `cowork_prefit_gates.md` (USER-RATIFIED 2026-07-19) and D-270…D-274, with its own parenthesis recording why the weaker naming above it does not delegate under rule (i).
- **The act:** the six delegations the user wrote into `ARCHITECTURE.md` on 2026-08-03 — the OI-293 write list, which the phase-1q classification pass asked for and only the user may write (decisions-register rule (g))
- **Where its ratification is recorded:** each hunk's own "written 2026-08-03 on the user's direction, the OI-293 write list" / "widened 2026-08-03 on the user's direction (the OI-293 write list)"; `OPEN_ITEMS.md` OI-293; and the commit's own account, which lists the seven write-list edits as verified present and unaltered
- *Retrieve:* `git show 1642c48e7f8c41f02a9ed14129ab2b9c6291b814 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-74 +80,2` · 1642c48e7f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1r — the write list committed, D-430's verbatim re-taken over the granularity clause, 215 anchors re-aimed, and the re-classification re-run against the user's six delegations
- **Ground.** The commit's own account opens "The user wrote all six delegations the phase-1q write list asked for (OI-293). This commit records them and re-runs every downstream act against them." Each of this commit's `ARCHITECTURE.md` hunks carries that attribution inside its own added text. ★ The first class was applied first and does not fire on any of them: no fact read in implementation code is cited in any added passage, and where a standing statement IS replaced the source is the user's own direction. Here the hunk REPLACES the notation-record contract's section list, §3.1–§3.4 becoming §2–§3.4, with the user's direction and the reason inside the added text: "the provenance rule that §3.1's own text depends on is in §2".
- **The act:** the six delegations the user wrote into `ARCHITECTURE.md` on 2026-08-03 — the OI-293 write list, which the phase-1q classification pass asked for and only the user may write (decisions-register rule (g))
- **Where its ratification is recorded:** each hunk's own "written 2026-08-03 on the user's direction, the OI-293 write list" / "widened 2026-08-03 on the user's direction (the OI-293 write list)"; `OPEN_ITEMS.md` OI-293; and the commit's own account, which lists the seven write-list edits as verified present and unaltered
- *Retrieve:* `git show 1642c48e7f8c41f02a9ed14129ab2b9c6291b814 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-902 +909,5` · 1642c48e7f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1r — the write list committed, D-430's verbatim re-taken over the granularity clause, 215 anchors re-aimed, and the re-classification re-run against the user's six delegations
- **Ground.** The commit's own account opens "The user wrote all six delegations the phase-1q write list asked for (OI-293). This commit records them and re-runs every downstream act against them." Each of this commit's `ARCHITECTURE.md` hunks carries that attribution inside its own added text. ★ The first class was applied first and does not fire on any of them: no fact read in implementation code is cited in any added passage, and where a standing statement IS replaced the source is the user's own direction. Here the hunk REPLACES the voice-leading contract's section list, §0/§5.3 becoming §0/§5.1/§5.3/§8/§9, and states which sections are deliberately NOT named and why — "they are ratification asks, not rule-stating sections", which is the register's own kind half.
- **The act:** the six delegations the user wrote into `ARCHITECTURE.md` on 2026-08-03 — the OI-293 write list, which the phase-1q classification pass asked for and only the user may write (decisions-register rule (g))
- **Where its ratification is recorded:** each hunk's own "written 2026-08-03 on the user's direction, the OI-293 write list" / "widened 2026-08-03 on the user's direction (the OI-293 write list)"; `OPEN_ITEMS.md` OI-293; and the commit's own account, which lists the seven write-list edits as verified present and unaltered
- *Retrieve:* `git show 1642c48e7f8c41f02a9ed14129ab2b9c6291b814 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-03 · `ARCHITECTURE.md` @ `-1484,0 +1496,2` · 1642c48e7f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): phase 1r — the write list committed, D-430's verbatim re-taken over the granularity clause, 215 anchors re-aimed, and the re-classification re-run against the user's six delegations
- **Ground.** The commit's own account opens "The user wrote all six delegations the phase-1q write list asked for (OI-293). This commit records them and re-runs every downstream act against them." Each of this commit's `ARCHITECTURE.md` hunks carries that attribution inside its own added text. ★ The first class was applied first and does not fire on any of them: no fact read in implementation code is cited in any added passage, and where a standing statement IS replaced the source is the user's own direction. Here the hunk ADDS the delegation pointer for the function layer, naming `cowork_layer5_function_design.md` (SIGNED, user, 2026-06-26) and D-335…D-342, with its own parenthesis recording that the "Full spec:" line above is a citation and not a delegation — "this paragraph is the delegation the record relied on and never had".
- **The act:** the six delegations the user wrote into `ARCHITECTURE.md` on 2026-08-03 — the OI-293 write list, which the phase-1q classification pass asked for and only the user may write (decisions-register rule (g))
- **Where its ratification is recorded:** each hunk's own "written 2026-08-03 on the user's direction, the OI-293 write list" / "widened 2026-08-03 on the user's direction (the OI-293 write list)"; `OPEN_ITEMS.md` OI-293; and the commit's own account, which lists the seven write-list edits as verified present and unaltered
- *Retrieve:* `git show 1642c48e7f8c41f02a9ed14129ab2b9c6291b814 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-3510,8 +3510,34` · c7d44b010e

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): phase 1y, read wave 1 and phase 1z committed together — the specification stops asserting a mechanism the code removed, and the pinned instrument's change is recorded where the block that pins it lives
- **Ground.** The commit's own subject states the direction of the correction in terms: "the specification stops asserting a mechanism the code removed". Its Task 3 account says §5.2 "now states what the key opening actually does at HEAD (note-based, each clause read at the code, pins named), with the removal recorded as a tried-and-closed line", and the added text says it again: "The paragraph this replaces specified a piece-start shortcut in the present tense. The code removed that short-circuit in Stage 4b-i on 2026-06-14 and this document went on asserting it." That is the first class's second limb, word for word, and the class is applied FIRST. This hunk REPLACES the piece-start-shortcut paragraph outright — the exception is gone and the opening is stated as note-based — and adds the scoping sentence saying which path §5.2 describes at all. The correction's own text cites `notationcomposingbridgehelpers.cpp:140`, `keyresolver.cpp:255`, `:286-289`, `:303-326`, `:340` and `:358-367`, the flag default at `composingconfiguration.cpp:178`, and the two regression pins at `regionanalysis_tests.cpp:122` and `:144`, which this commit did not write.
- *Retrieve:* `git show c7d44b010e630c4a28bbb5d9faf8420aa39c7fc1 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-3536,4 +3562,4` · c7d44b010e

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): phase 1y, read wave 1 and phase 1z committed together — the specification stops asserting a mechanism the code removed, and the pinned instrument's change is recorded where the block that pins it lives
- **Ground.** The commit's own subject states the direction of the correction in terms: "the specification stops asserting a mechanism the code removed". Its Task 3 account says §5.2 "now states what the key opening actually does at HEAD (note-based, each clause read at the code, pins named), with the removal recorded as a tried-and-closed line", and the added text says it again: "The paragraph this replaces specified a piece-start shortcut in the present tense. The code removed that short-circuit in Stage 4b-i on 2026-06-14 and this document went on asserting it." That is the first class's second limb, word for word, and the class is applied FIRST. This hunk REPLACES the fallback list's count and drops the removed shortcut from it — "the list read 'two' and named the removed piece-start shortcut as the first of them". The correction's own text cites the surviving fallback's own guard, `results.empty() || distinctPitchClasses(ctx) < 3`, which this commit did not write.
- *Retrieve:* `git show c7d44b010e630c4a28bbb5d9faf8420aa39c7fc1 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-3541 +3567,4` · c7d44b010e

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): phase 1y, read wave 1 and phase 1z committed together — the specification stops asserting a mechanism the code removed, and the pinned instrument's change is recorded where the block that pins it lives
- **Ground.** The commit's own subject states the direction of the correction in terms: "the specification stops asserting a mechanism the code removed". Its Task 3 account says §5.2 "now states what the key opening actually does at HEAD (note-based, each clause read at the code, pins named), with the removal recorded as a tried-and-closed line", and the added text says it again: "The paragraph this replaces specified a piece-start shortcut in the present tense. The code removed that short-circuit in Stage 4b-i on 2026-06-14 and this document went on asserting it." That is the first class's second limb, word for word, and the class is applied FIRST. This hunk REPLACES the surviving fallback's description, adding the confidence it actually returns, the code coordinate and the pin, and the statement that it fires at any tick and is not a piece-start rule. The correction's own text cites `keyresolver.cpp:328-332` and the pin at `regionanalysis_tests.cpp:164`, which this commit did not write.
- *Retrieve:* `git show c7d44b010e630c4a28bbb5d9faf8420aa39c7fc1 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-3544 +3573` · c7d44b010e

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): phase 1y, read wave 1 and phase 1z committed together — the specification stops asserting a mechanism the code removed, and the pinned instrument's change is recorded where the block that pins it lives
- **Ground.** The commit's own subject states the direction of the correction in terms: "the specification stops asserting a mechanism the code removed". Its Task 3 account says §5.2 "now states what the key opening actually does at HEAD (note-based, each clause read at the code, pins named), with the removal recorded as a tried-and-closed line", and the added text says it again: "The paragraph this replaces specified a piece-start shortcut in the present tense. The code removed that short-circuit in Stage 4b-i on 2026-06-14 and this document went on asserting it." That is the first class's second limb, word for word, and the class is applied FIRST. This hunk REPLACES the closing back-reference, "these two fallback paths" becoming "that one fallback path". The correction's own text cites the same single surviving fallback, which this commit did not write.
- *Retrieve:* `git show c7d44b010e630c4a28bbb5d9faf8420aa39c7fc1 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-331,0 +332,15` · e10479a09f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the six-wave backlog committed as one act — read waves 4, 5 and 6, the completion inventory, the delegations-and-corrections wave, and the census delegation
- **Ground.** The commit's own account states what it is and what it is not: "Committed on the user's ruling R1 of 2026-08-04 … This commit adds nothing to any of the six waves and changes nothing in them. It is the authorization each of them was owed and none of them received." Every `ARCHITECTURE.md` hunk of it carries its own attribution to a user act inside the added text. ★ The first class was applied first and does not fire on any of them: each ADDS a delegation pointer, none withdraws a standing statement, and no fact read in implementation code is cited in any added passage. Here the hunk WIDENS the census pointer to the sections holding that document's own standing rules, and states what the widening settles and what it does not — the delegation half alone, with the kind half left to be judged per section at the classification pass.
- **The act:** the user's census-delegation ruling of 2026-08-04, written under the fifth home case (decisions-register rule (g), user-ratified 2026-08-02)
- **Where its ratification is recorded:** the added text's own "written 2026-08-04 on the user's ruling; the fifth home case, rule (g), user-ratified 2026-08-02"; and the commit's own account of the census-delegation wave, `cc_instruction_census_delegation_and_commit.md`
- *Retrieve:* `git show e10479a09f39c46419a62ada58e584a826f275ca --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-1241,0 +1257,4` · e10479a09f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the six-wave backlog committed as one act — read waves 4, 5 and 6, the completion inventory, the delegations-and-corrections wave, and the census delegation
- **Ground.** The commit's own account states what it is and what it is not: "Committed on the user's ruling R1 of 2026-08-04 … This commit adds nothing to any of the six waves and changes nothing in them. It is the authorization each of them was owed and none of them received." Every `ARCHITECTURE.md` hunk of it carries its own attribution to a user act inside the added text. ★ The first class was applied first and does not fire on any of them: each ADDS a delegation pointer, none withdraws a standing statement, and no fact read in implementation code is cited in any added passage. Here the hunk ADDS two delegation pointers — the Layer-1 note model's contract and the Layer-1.5 phrase-boundary primitive's — the second with its siting reasoned in its own parenthesis, including why it is not sited at the consuming Layer-6 section.
- **The act:** the OI-327 write list — the delegations the user wrote into `ARCHITECTURE.md` on 2026-08-04
- **Where its ratification is recorded:** each pointer's own "written 2026-08-04 on the user's direction, the OI-327 write list"; `OPEN_ITEMS.md` OI-327; and the commit's own account of read wave 5, which records three delegations written and two withheld
- *Retrieve:* `git show e10479a09f39c46419a62ada58e584a826f275ca --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-1327,0 +1347,2` · e10479a09f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the six-wave backlog committed as one act — read waves 4, 5 and 6, the completion inventory, the delegations-and-corrections wave, and the census delegation
- **Ground.** The commit's own account states what it is and what it is not: "Committed on the user's ruling R1 of 2026-08-04 … This commit adds nothing to any of the six waves and changes nothing in them. It is the authorization each of them was owed and none of them received." Every `ARCHITECTURE.md` hunk of it carries its own attribution to a user act inside the added text. ★ The first class was applied first and does not fire on any of them: each ADDS a delegation pointer, none withdraws a standing statement, and no fact read in implementation code is cited in any added passage. Here the hunk ADDS the Layer-2 slicer's delegation pointer, with its own parenthesis recording that the "See …" line above is a citation of three documents and not a delegation under rule (i).
- **The act:** the OI-327 write list — the delegations the user wrote into `ARCHITECTURE.md` on 2026-08-04
- **Where its ratification is recorded:** the pointer's own "written 2026-08-04 on the user's direction, the OI-327 write list"; `OPEN_ITEMS.md` OI-327
- *Retrieve:* `git show e10479a09f39c46419a62ada58e584a826f275ca --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-04 · `ARCHITECTURE.md` @ `-1508,0 +1530,2` · e10479a09f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the six-wave backlog committed as one act — read waves 4, 5 and 6, the completion inventory, the delegations-and-corrections wave, and the census delegation
- **Ground.** The commit's own account states what it is and what it is not: "Committed on the user's ruling R1 of 2026-08-04 … This commit adds nothing to any of the six waves and changes nothing in them. It is the authorization each of them was owed and none of them received." Every `ARCHITECTURE.md` hunk of it carries its own attribution to a user act inside the added text. ★ The first class was applied first and does not fire on any of them: each ADDS a delegation pointer, none withdraws a standing statement, and no fact read in implementation code is cited in any added passage. Here the hunk ADDS the Layer-6 delegation pointer together with the user's answer to the question it had been withheld over — why a contract home is coherent for a layer that may not be built — and states in terms that D-266 is untouched and that the pointer authorizes no build, no wiring and no change to what the analysis computes.
- **The act:** the OI-327 write list, together with the user's 2026-08-04 answer on the withheld Layer-6 clause
- **Where its ratification is recorded:** the pointer's own "written 2026-08-04 on the user's direction, the OI-327 write list" and its own "the question this clause was withheld over on 2026-08-04 and which the user has now answered"; `OPEN_ITEMS.md` OI-327
- *Retrieve:* `git show e10479a09f39c46419a62ada58e584a826f275ca --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-07 · `ARCHITECTURE.md` @ `-1289,0 +1290,24` · bd3a608fec

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): commit three phase-1 waves on the user's instruction
- **Ground.** The commit's own subject is "commit three phase-1 waves on the user's instruction", and its body names the three dispatches and their rulings. Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1 — a register decision written into the specification that owns it — and each added block names the register entry it carries and says it was "re-homed into this specification 2026-08-04". Here the added blocks carry D-628, the change-point as the finest meaningful extension step, and D-607, the absence of any validated deterministic rule set for polyphonic phrase-boundary detection. ★ The first class was applied first and does not fire: both ADD material and withdraw nothing, and neither ground is a fact read in implementation code — D-628's is what a Layer-2 slice IS as this same document specifies it, and D-607's is a stated fact of absence established by a literature survey.
- **The act:** the D-231 phase-1 re-homing of two register decisions into the specification that owns them, performed under the user's instruction of 2026-08-04 and criterion C1 as re-issued that day
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-04"; the commit's own "on the user's instruction"; D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02); and the C1 ruling the commit names, `cc_instruction_c1_ruling_and_item1c.md` (register entry D-642)
- *Retrieve:* `git show bd3a608fecf82c446f959432b13e0a5944093cd2 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-07 · `ARCHITECTURE.md` @ `-1375,0 +1400,30` · bd3a608fec

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): commit three phase-1 waves on the user's instruction
- **Ground.** The commit's own subject is "commit three phase-1 waves on the user's instruction", and its body names the three dispatches and their rulings. Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1 — a register decision written into the specification that owns it — and each added block names the register entry it carries and says it was "re-homed into this specification 2026-08-04". Here the added blocks carry D-624, D-635 and D-623. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: two of the three rest on what the implementation currently does — D-635's claim that the requirement is MASKED rests on "the note model still loads the whole score anyway", and D-623's on the capability having been built as an option on the existing driver and being off by default. What decides it is the distinction the inherited method already draws at a homing act: all three ADD material and none withdraws a standing documentation statement, and each implementation fact is stated as the DECISION'S OWN CONTENT — what the design chose and what state it left — not as a fact against which a documentation statement was found false.
- **The act:** the D-231 phase-1 re-homing of three bounded-context and orchestration decisions into the specification that owns them, performed under the user's instruction of 2026-08-04
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-04"; the commit's own "on the user's instruction"; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show bd3a608fecf82c446f959432b13e0a5944093cd2 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-07 · `ARCHITECTURE.md` @ `-1505,0 +1560,22` · bd3a608fec

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): commit three phase-1 waves on the user's instruction
- **Ground.** The commit's own subject is "commit three phase-1 waves on the user's instruction", and its body names the three dispatches and their rulings. Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1 — a register decision written into the specification that owns it — and each added block names the register entry it carries and says it was "re-homed into this specification 2026-08-04". ★ BUT THE FIRST CLASS FIRES HERE, and it is applied first exactly so that a ratified act cannot launder a correction made under it. The added block's own heading is "Two premises this decoder carries were MEASURED, and both came back against it", and it QUALIFIES what this section specifies: the symmetric-root spelling pin's entry premise is stated FALSE and the mechanism effectively unreachable (D-608), and the abstention rate is stated to ride on a never-fitted seed constant (D-609). The source is named in the added text itself — "measured at the probe and traced at the code" for the first, "established at the code — the constant is a seed in the decoder's own header, and the control flow was traced" for the second — and this commit wrote none of that code.
- *Retrieve:* `git show bd3a608fecf82c446f959432b13e0a5944093cd2 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-07 · `ARCHITECTURE.md` @ `-1520,0 +1597,31` · bd3a608fec

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): commit three phase-1 waves on the user's instruction
- **Ground.** The commit's own subject is "commit three phase-1 waves on the user's instruction", and its body names the three dispatches and their rulings. Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1 — a register decision written into the specification that owns it — and each added block names the register entry it carries and says it was "re-homed into this specification 2026-08-04". Here the added block carries D-584, D-585 and D-586, three standing constraints on this layer's methods. ★ The first class was applied first and does not fire, and the call is recorded because it is close: D-586's text DOES name our own legacy component — "the legacy component carrying the name compares candidate chords instead". What decides it is that the constraint's stated ground is a literature survey ("established by survey — every published autonomous Roman-numeral system the catalog names …"), the naming of our own component being an explanatory corollary rather than the source; and that nothing standing in the documentation is withdrawn — the closing sentence EXPLAINS why the layer's output is already specified as the Roman numeral rather than replacing that specification.
- **The act:** the D-231 phase-1 re-homing of three method constraints into the specification that owns them, performed under the user's instruction of 2026-08-04; the three decisions are recorded as user-ratified on that date
- **Where its ratification is recorded:** the added block's own "re-homed into this specification 2026-08-04"; the commit's own "on the user's instruction"; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show bd3a608fecf82c446f959432b13e0a5944093cd2 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-07 · `ARCHITECTURE.md` @ `-3565,0 +3673,11` · bd3a608fec

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): commit three phase-1 waves on the user's instruction
- **Ground.** The commit's own subject is "commit three phase-1 waves on the user's instruction", and its body names the three dispatches and their rulings. Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1 — a register decision written into the specification that owns it — and each added block names the register entry it carries and says it was "re-homed into this specification 2026-08-04". Here the added block records D-572 — the hard post-hoc declared-mode promotion — as a tried-and-closed line beside the §5.2 correction the preceding commit made, which is the form the commit's own body names: "ruling R2 recorded (D-644) and applied to D-572 at ARCHITECTURE.md §5.2". ★ The first class was applied first and does NOT fire: the hunk ADDS the closed line and withdraws nothing — the standing statement it belongs to had already been replaced by the preceding commit, which is graded on its own hunks above — and it cites no code coordinate. ★ ONE THING THE SCREEN CANNOT ESTABLISH IS RECORDED RATHER THAN RESOLVED: the added text attributes the removal's defense to "the defense recorded with the change" without naming WHERE that record is, so whether the wording came from the code beside the removal or from the change's own written record is not decidable at this hunk's text. It does not move the verdict, because the ACT this hunk performs is the ruled one and is named.
- **The act:** ruling R2 of 2026-08-04 — where a superseded decision's content is a REMOVAL, the specification states the current behaviour and records the removal as a tried-and-closed line — applied here to D-572
- **Where its ratification is recorded:** the dispatch the commit's own body names, `cc_instruction_guard_fix_and_item1d.md` ("ruling R2 recorded (D-644) and applied to D-572 at ARCHITECTURE.md §5.2"); and the rule's home at `cowork_audit_protocol.md`, register entry D-644
- *Retrieve:* `git show bd3a608fecf82c446f959432b13e0a5944093cd2 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-264,0 +265,2` · d1891db158

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds a HEADING and nothing else — "## The joint estimator — the standing rules of the production inference layer" — which is the commit's own "the joint estimator gains a section a decision can be sited inside". ★ The first class was applied first and does not fire: no statement of any kind is made, so nothing can be withdrawn and no source is cited. The second does not fire either — a heading records no ruling's content — and the third does, this being a re-heading whose source is not a fact read in implementation code.
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-355,0 +358,76` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the decode's five counted quantities — factor granularity, the key-signature and declared-mode prior's scope, the secondary-dominant pooling level, the leftover back-off and the per-factor missing-tone penalty — and the document-governance heading beneath them. ★ The first class was applied first and does not fire: every block ADDS and withdraws nothing, and each ground named in the added text is a desk simulation, a count over the ground-truth corpus or the published back-off construction — not a fact read in implementation code. The counting is over the annotated corpus, which is ground truth and not our own output.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-533,0 +612,17` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the standing verdict that the hand-built analysis is CONFIRMED and the learned replacement NOT triggered, retained as an explicit fallback with a concrete trigger. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the verdict's whole ground is a MEASUREMENT of what this implementation produces — "the error mass decomposes into causes reachable within it", "the corrected metric showed the residual had been inflated by already-correct artifacts and by mis-attributed cases". What decides it is that the block ADDS and withdraws nothing, and that the measurement is the DECISION'S OWN SUBJECT — the choice between a hand-built and a learned scorer was sized by measuring, which is the decision — not a fact against which a documentation statement was found false.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1207,0 +1303,28` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the two boundary invariants that keep the rendered form from crossing back into the analysis — structured fields only, and a written chord symbol readable only as a comparison or ground-truth label — and states in its own text why they are sited at the boundary's own section rather than copied (#6). ★ The first class was applied first and does not fire: both invariants ADD, both defenses are stated as the rules' own reasoning, and neither cites a fact read in implementation code.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1481,0 +1605,55` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds four standing rules of the key/mode layer — what a local-key hypothesis may read, at what scope a global tonic anchor enters, the refuted reach-back proxy, and the owed enharmonic-identity rule for key spans. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the second rule's ⚠ LEGACY mark is justified by a REACHABILITY CHECK AT THE CODE this commit did not write — "the window scorer this rule excludes (`KeyModeAnalyzer::analyzeKeyMode`) is reached only through the legacy resolver and this layer's dormant sequence decoder, and the resolver is retired from the production region path" — and the added text says in terms that the mark "follows a check at the code, not the decision's age". What decides it is that all four ADD and none withdraws a standing documentation statement: the code check SCOPES a rule arriving here for the first time, rather than refuting a statement this document already carried.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1581,0 +1760,27` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the chord search's output-surface contract and the shared spelling primitive's presence test. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the presence-test rule's own defense is "established at the source rather than asserted" — the source being the shared line-of-fifths primitive, whose sign convention and whose `tpcIsValid()` predicate this commit did not write — and it carries an honest bound read at the same place, that the predicate cannot tell a real flattest spelling from a default-initialised field. What decides it is that both rules ADD and neither withdraws a standing documentation statement: the primitive's sign convention is cited as the REASON FOR THE RULE, not as a fact that found an existing statement false.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1627,0 +1833,25` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the two ratified obligations the function layer owes — a stated fallback for a featureless phrase-boundary profile, and key-confirmation channels that do not require a cadence — and marks both DESIGN-ONLY in its own words, "work this layer is required to specify, not mechanisms it has". ★ The first class was applied first and does not fire: both ADD, both grounds are the architecture review's own stress simulation on resolution-denying music, and no fact read in implementation code is cited.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-3787,0 +4018,25` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds two standing rules on the temporal-context structure — what may enter it, and that its extension fields are recorded by the producing pass and never rebuilt by a consumer. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the first rule's finding is stated about the CODE and not about the record — "Four fields describing the previous winner's competition outcome were added to it that belong to the planned progression-level structure instead", the finding being that "one had been growing into the other with no migration plan written down". What decides it is that both rules ADD and neither withdraws a standing documentation statement, and that the code fact is what the rule is ABOUT — a prohibition on adding more of the same — rather than a fact that found an existing statement false.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-4304,0 +4560,7` · d1891db158

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds a POINTER and nothing else — that why the tick-local path is a separate module at all is decided at §11.5 and stated once there (#6). ★ The first class was applied first and does not fire: no statement about the system is made or withdrawn here, the paragraph only re-points the reader. The second does not fire — a pointer records no ruling's content — and the third does.
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-4330,0 +4593,7` · d1891db158

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds a POINTER — that how a spelling's presence is tested belongs to the Layer-4 section that specifies the shared primitive, and is stated once there (#6). ★ The first class was applied first and does not fire, and the call is recorded because the pointer repeats the rule's one-clause reason ("the flat side of the line of fifths is negative"). What decides it is that the paragraph withdraws nothing and states no fact of its own: it re-points, which is the third class exactly. The rule it points at is graded at its own hunk above.
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-4712,0 +4982,18` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the rule that every uncalibrated style constant and idiom carries the empirically-unvalidated mark with its validation path named beside it, and closes by stating in terms what it does NOT claim — that the mark is applied at HEAD; it is not, and applying it is owed work tracked in the open-items register. ★ The first class was applied first and does not fire: the block ADDS, and its ground is the architecture review's own finding about where the mark is ABSENT FROM THE SPECIFICATION, which is a fact about the record and not one read in implementation code.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-4766,0 +5054,68` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the five rules of the method that produces and re-produces the idiom taxonomy — discover-then-name, the key-normalised tonal-pitch-class encoding, confound control as a validity gate, the external mechanical extractor, and re-discovery riding every corpus wave. ★ The first class was applied first and does not fire: the block ADDS, and every ground is methodological or prior art. Where our own tooling is named — the slicer not used for extraction, the analyzer deliberately kept out of it — it is named as the study's own DESIGN CHOICE and its stated reason, not as a fact against which a documentation statement was found false.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-4789,0 +5145,25` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds the harmonic vocabulary's declared dormancy — the function layer does not touch it until the recognition consumer is built, and the connection is absent rather than partial — and states the one open structural question with the trigger that decides it. ★ The first class was applied first and does not fire: the block ADDS, and both grounds are the ratified build order and the component's own contract, with no fact read in implementation code cited.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-6405,0 +6786,35` · d1891db158

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): five waves committed as one — and the shell-read guard, blind to the dialect it was armed on, fixed corpus-first
- **Ground.** The commit carries five waves and names each with the dispatch that ran it; the wave whose acts these hunks are is `cc_instruction_owner_rulings_homing.md` — "the forty-eight owner rulings homed; the joint estimator gains a section a decision can be sited inside". Every `ARCHITECTURE.md` hunk of it is a RE-HOMING act under D-231's criterion C1, and the added blocks say so in their own words — "re-homed into this specification 2026-08-07 on the user's ruling". The commit's own scope line is "No src/ change, no goldens, no tools/corpus/ or tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds this pipeline's own scope statement — the point-in-time path left outside it by design — and the pre-declared keep-or-drop rule for the sub-beat annotation duration gate, with both branches fixed in advance and the gate recorded undischarged at HEAD. ★ The first class was applied first and does not fire: the block ADDS and withdraws nothing, its scope half restates a decision's own stated reason (point-in-time semantics differ too much to force one interface), and its gate half is a protocol written BEFORE the measurement it governs — the pre-declared-protocol discipline, which is the opposite of a correction made against a result.
- **The act:** the user's owner rulings of 2026-08-07, homed into the specifications that own them under D-231's phase-1 criterion C1
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-07 on the user's ruling"; the ruling record the commit lands beside them, `cowork_owner_rulings_2026_08_07.md`; the dispatch `cc_instruction_owner_rulings_homing.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show d1891db1588d73fbf41789c9139006d269a1c766 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-272,0 +273,7` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the delegation pointer for the estimator's factor structure, naming `cowork_joint_estimator_factorization.md` and saying what the six rules beneath it govern by contrast. ★ The first class was applied first and does not fire: the pointer ADDS, withdraws nothing, and cites no fact read in implementation code.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-431,0 +439,50` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the hard/soft line the evidence classification rests on, and where the hand-built-versus-learned choice lives — four statements carried forward out of a superseded architecture proposal, with the added text stating in terms that nothing of the superseded proposal's SHAPE is carried. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: three of the four rest on MEASUREMENTS — the notated signature measured to pin the wrong home key, and three reading-shaped producers each measured to pin wrong. What decides it is that the block ADDS and withdraws nothing, that the signature finding's own scope clause says it is "a property of the written music and its human analyses, not of any one of our pipelines", and that the producers' measurements are carried with an explicit ⚠ LEGACY SCOPE saying they are of those producers and not claims about the estimator this section specifies.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1436,0 +1494,12` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the rule that voice slots and stem direction are structural notational metadata and may therefore be read by this layer. ★ The first class was applied first and does not fire: the block ADDS, and its whole defense is the line the chord-symbol prohibition already draws — what the score IS versus what a user has CLAIMED about it — applied to a new pair of fields, with no fact read in implementation code cited.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1495,0 +1565,31` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds what may be asserted across an extension and what a slice carries — the loaded-edge boundary being artificial so that the edge slice GROWS, with an old-slices-stay-byte-identical assertion recorded FALSE and prohibited as a test, and the slice kept minimal. ★ The first class was applied first and does not fire: the block ADDS, and the false assertion it prohibits is corrected against a COUNTEREXAMPLE THE DESIGN STATES IN FULL — a single eligible note spanning the loaded start — not against a fact read in implementation code. Its one implementation statement, that the minimal form was taken at the build, records the decision's outcome rather than sourcing it.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1659,0 +1760,18` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the Baroque partial-signature handling — detect the convention and reinterpret the signature one step, never widen the candidate family for every score. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the block carries a ⚠ LEGACY / SUPERSEDED IN FACT qualification whose ground is an ARM CHECK AT THE CODE — "the correction is applied inside the legacy resolver, which the production arm no longer runs; no ruling superseded it, a later build replaced what it governs". What decides it is that the rule and its qualification arrive TOGETHER in one addition: no standing statement of this document is withdrawn, and the block explicitly declines to assert anything about the arm that runs — "Whether the joint estimator handles the convention AT ALL is NOT settled by this entry and is not asserted here."
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1674,0 +1793,13` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the constraint that a rebuilt or re-tuned chord scoring must not lean on the held-note repetition bonus the faithful note model removed. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the constraint's ground is a MEASUREMENT taken when the removal surfaced — "removing the inflation moved a small number of cases the wrong way while the key axis stayed flat". What decides it is that the block ADDS and withdraws nothing, and that the added text refuses the very assertion a correction would make: "Whether those cases have since recovered is NOT stated here and was not checked — the constraint binds regardless."
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1799,0 +1931,18` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds that the resolver of carried uncertain readings is this layer itself and that there is no distinct gated box between the note layers and it. ★ The first class was applied first and does not fire: the block ADDS, and its defense is "derived from the layer-identity test and then confirmed by measurement" — a derivation from the layer contract with a corpus measurement as corroboration, and the three admission tests for a new component applied to it. No standing documentation statement is withdrawn; the added text reads the 'gated step' language elsewhere as describing this layer's own gated entry.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1868,0 +2018,26` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the key-area grouping rule — a smoothing pass over stabilized regions, with a disagreeing region keeping its own key while being grouped — together with a marked block that splits the decision across the two arms. ★ The first class was applied first and does NOT fire, and this is the closest call in the commit: the marked block IS an arm check at the code, citing `sectionrecordadapter.cpp:360` and `sectionanalyzer.cpp:750`, and it reports that the rule is live on the record arm while the stabilization pass it names as a PRECONDITION has its only call site inside the legacy arm. What decides it is that the rule and the split arrive together in one addition, so nothing this document already stated is withdrawn — and that the block takes NO verdict: it states the question as OPEN, says in terms that it bears on the analysis, and points it at the open-items register. ★ Recorded so a reader meets it: this is a code-read fact reaching a specification, and it is cleared here only because it withdraws nothing and adjudicates nothing.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-5121,0 +5297,100` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds what the taxonomy and its weights are as an object, three findings about the second axis the discovery study found, and the whole of §6.8 — the user-facing preset layer's naming, coverage tiers, mixture contract and licence split, marked RECORDED and DEFERRED product work. ★ The first class was applied first and does not fire: the block ADDS, and its grounds are the discovery study's own measurements over external corpora and the standing principles, none of them a fact read in implementation code. Its one implementation remark — that custom properties survive the native format while the MusicXML round-trip is only partial — is recorded as an open check the feature must make, not as a source.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-6493,0 +6769,8` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the delegation pointer for the notation-surface adoption increment, with its own sentence separating what stays in that contract from what this section states. ★ The first class was applied first and does not fire: the pointer ADDS, withdraws nothing and cites no fact read in implementation code.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-7527,0 +7811,6` · 82ebfd68d9

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the hold is over — the phase-1q record frozen at its snapshot, the applying run run, and the six blocked generators freed
- **Ground.** The commit's own account is "Task 0 of the away batch (`cc_instruction_away_execution.md`), applying the user's Ruling 1 of 2026-08-08 (`cowork_rulings_2026_08_08_pre_away.md`)", and it states its own scope: "No `src/` change, no golden, no `tools/corpus/` or `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Every `ARCHITECTURE.md` hunk of it says in its own added text either "re-homed into this specification 2026-08-08 on the user's ruling" or "this delegation written 2026-08-08 on the user's ruling". Here the hunk adds the delegation pointer for the language-model integration's detailed design. ★ The first class was applied first and does not fire, on the same ground as the pointer above: it ADDS, withdraws nothing and cites no fact read in implementation code.
- **The act:** the user's rulings of 2026-08-08, under which the owed decisions were homed into the specifications that own them and four delegations were written, D-231's phase-1 criterion C1 being the standing obligation they discharge
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08 on the user's ruling" / "this delegation written 2026-08-08 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show 82ebfd68d9f7760396aab2b792ea3a1dce02a9e5 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-316,0 +317,14` · dfbf3ab824

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): nine archive-only decisions moved into the specifications that own them, D-601's hold ended, and three held because the act they need is a ruling
- **Ground.** The commit's own account is "Task 2 of the away batch (`cc_instruction_away_execution.md`). D-601's homing is the one edit Ruling 2 of `cowork_rulings_2026_08_08_pre_away.md` authorizes", and it states what the act was FOR: entries that "lived ONLY in a session-handoff archive" or were "already NAMED in an `ARCHITECTURE.md` 'Tried and closed' line without the section saying what they were, so a reader met an identifier and could not learn the rule". Both `ARCHITECTURE.md` hunks say so in their own added text: "re-homed into this specification 2026-08-08". The commit's scope line is "No `src/` change, no golden, no corpus of scores, no `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds what D-288 IS — do not retry widening the search to consider more candidate readings in parallel — behind a naming the section already carried. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the rule's ground is a MEASUREMENT of this system's own behaviour, "the wrong reading is the highest-scoring one", cross-checked against independent earlier measurements. What decides it is that the block ADDS the content behind an existing identifier and withdraws nothing, and that the measurement is the SHELVING'S OWN SUBJECT rather than a fact against which a documentation statement was found false.
- **The act:** the away batch's Task 2 under the user's rulings of 2026-08-08, re-homing archive-only decisions into the specifications that own them — D-231's phase-1 criterion C1 being the standing obligation discharged
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08"; the ruling record the batch applies, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show dfbf3ab824f0717d83cf3cce8e332c69f1074328 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-08 · `ARCHITECTURE.md` @ `-1613,0 +1628,25` · dfbf3ab824

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): nine archive-only decisions moved into the specifications that own them, D-601's hold ended, and three held because the act they need is a ruling
- **Ground.** The commit's own account is "Task 2 of the away batch (`cc_instruction_away_execution.md`). D-601's homing is the one edit Ruling 2 of `cowork_rulings_2026_08_08_pre_away.md` authorizes", and it states what the act was FOR: entries that "lived ONLY in a session-handoff archive" or were "already NAMED in an `ARCHITECTURE.md` 'Tried and closed' line without the section saying what they were, so a reader met an identifier and could not learn the rule". Both `ARCHITECTURE.md` hunks say so in their own added text: "re-homed into this specification 2026-08-08". The commit's scope line is "No `src/` change, no golden, no corpus of scores, no `tools/robust_stop/` movement, no behaviour change to the analysis, no fix to inference, no design." Here the hunk adds what the key layer's two named dead ends ARE — the ranked key-candidate carry, and deciding the key from key-agnostic cadences one at a time — each with its stated re-open condition or its stated scope. ★ The first class was applied first and does NOT fire, on the same ground as the hunk above: both rules ADD content behind namings the section already carried, both grounds are measurements of legacy mechanisms that are the shelvings' own subjects, and one of them is explicitly re-read for the joint estimator — "that design carries a full posterior by construction, so the concern this shelving withdrew is met by a different design rather than by reviving this one".
- **The act:** the away batch's Task 2 under the user's rulings of 2026-08-08, re-homing archive-only decisions into the specifications that own them — D-231's phase-1 criterion C1 being the standing obligation discharged
- **Where its ratification is recorded:** each added block's own "re-homed into this specification 2026-08-08"; the ruling record the batch applies, `cowork_rulings_2026_08_08_pre_away.md`; and D-231's phase-1 clause at `CLAUDE.md` Conventions (user-directed 2026-08-02)
- *Retrieve:* `git show dfbf3ab824f0717d83cf3cce8e332c69f1074328 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-09 · `ARCHITECTURE.md` @ `-1212,0 +1213,30` · 935efcf993

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the ten rulings of 2026-08-09 applied through Task 3 — and one ruling's own condition is not met, so half of it stops
- **Ground.** The commit's own account is "the ten rulings of 2026-08-09 applied through Task 3", applying `cowork_rulings_2026_08_09_return.md` read whole, and it states its scope: "No src/ change, no golden, no corpus of scores, no tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Both `ARCHITECTURE.md` hunks carry their own attribution — "written into this section 2026-08-09 on the user's ruling". Here the hunk homes D-286 — whole-score interactive analysis SHELVED WITH EVIDENCE against a bounded window — into §2.16, with a marked block stating that the implementation at HEAD contradicts the shelving. ★ The first class was applied first and does NOT fire, and this is a close call recorded in full: the marked block IS a statement read at the implementation — "The record producer takes no tick range: every record-arm seam analyzes the whole score and narrows to the requested span afterward" — and it is offered against the very decision being homed. What decides it is that the shelving and the contradiction arrive TOGETHER in one addition, so nothing this document already stated is withdrawn, and that the block takes NO verdict — it says in terms "This section does not decide which of the two is right" and points the conformance question at its own rows. That is the ruled form for homing a decision the implementation contradicts, applied rather than improvised.
- **The act:** the user's Ruling 5 of 2026-08-09 — where the implementation contradicts the decision being homed, the shelving is written in AS a shelving, the contradiction stated beside it and the questions pointed at their rows, with no verdict taken
- **Where its ratification is recorded:** the added block's own "written into this section 2026-08-09 on the user's ruling"; the ruling record the commit names, `cowork_rulings_2026_08_09_return.md`; and the rule's home at `cowork_audit_protocol.md`, register entry D-649
- *Retrieve:* `git show 935efcf99349bf414196e81613f07b9cfae99f43 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-09 · `ARCHITECTURE.md` @ `-2045,0 +2076,28` · 935efcf993

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the ten rulings of 2026-08-09 applied through Task 3 — and one ruling's own condition is not met, so half of it stops
- **Ground.** The commit's own account is "the ten rulings of 2026-08-09 applied through Task 3", applying `cowork_rulings_2026_08_09_return.md` read whole, and it states its scope: "No src/ change, no golden, no corpus of scores, no tools/robust_stop/ movement, no behaviour change to the analysis, no fix to inference, no design." Both `ARCHITECTURE.md` hunks carry their own attribution — "written into this section 2026-08-09 on the user's ruling". Here the hunk homes the BUILD half of D-291 — the tonicization labeller is deliberately left unwired and the real lever is a local-modulation detector at the key layer — with its measurement half explicitly left where it belongs (#6). ★ The first class was applied first and does NOT fire: the block ADDS and withdraws nothing, and its ground is a measurement of the GRADING COMPARISON against the human annotations — that the comparison scores by root and quality and therefore MASKS the key error — which is a fact about the measurement apparatus and the ground truth, not a fact read in implementation code that found a documentation statement false.
- **The act:** the user's Ruling 11 of 2026-08-09, splitting D-291 and homing its build half at the Layer-5 function section with its defense
- **Where its ratification is recorded:** the added block's own "written into this section 2026-08-09 on the user's ruling"; `cowork_rulings_2026_08_09_return.md`; and the measurement half's own home in `CLAUDE.md` gate block (A), which the block points at rather than restating
- *Retrieve:* `git show 935efcf99349bf414196e81613f07b9cfae99f43 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-09 · `ARCHITECTURE.md` @ `-2115,25 +2115,48` · 4aab2ec297

- **Verdict:** POSITIVELY CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** docs(cowork): the specification now describes the arm that ships — and a ruling's own prediction is refuted, uncovering a verification that had stopped covering its population
- **Ground.** The commit's own subject states the direction of the change in terms: "the specification now describes the arm that ships". ★ THE FIRST CLASS FIRES, on both of its limbs. The hunk REPLACES a standing statement of this document — the heading's "OVER STABILIZED REGIONS" and the whole OPEN QUESTION block beneath it, both of which this same population carries as an earlier hunk — with a corrected account of what supplies the smoothed key sequence on each arm. And the correction's source is named as a read at the code: "after the read-only probe the open-items register had reserved to the user established the answer at the code". Its own why-clause is the first class's second limb word for word — "the former text named the legacy step as THE precondition, so it described an arm that does not ship; the record arm meets the requirement by other means, and a specification that says otherwise cannot be the compliance standard (#10)". The corrected text carries the behavioural non-equivalence between the two arms visibly and calls it UNMEASURED, and the former wording stands preserved in place (#12).
- *Retrieve:* `git show 4aab2ec297444a4a85d7b0197cf07e66fe9d5354 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-10 · `ARCHITECTURE.md` @ `-1094,0 +1095,14` · 9fe7f4561f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): the homing default is executed for three entries — the span typology gains the per-voice kind it was told to carry, the axis's unowned objects get their owner, and a motion-type reading stops being "owed at build"
- **Ground.** The commit's own account is "Dispatch `cc_instruction_return_continuation_6.md` Task 1, on the user's Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`: re-homing into the owning layer's specification is the DEFAULT closing route for the finish line's homing items", and both `ARCHITECTURE.md` hunks carry their own attribution — "user-ratified 2026-07-03; written here 2026-08-09". Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk adds the per-voice span kind to the span typology, with what the record deliberately does NOT assert stated beside it — that consecutive phrases within one voice tile that voice exactly. ★ The first class was applied first and does not fire: the block ADDS a member to the typology, withdraws nothing, and its ground is contrapuntal writing itself — phrases running concurrently and out of step across voices — with no fact read in implementation code cited.
- **The act:** the user's Ruling 38 of 2026-08-09, making re-homing into the owning layer's specification the default closing route, executed here for two entries the user ratified on 2026-07-03
- **Where its ratification is recorded:** each added block's own "user-ratified 2026-07-03; written here 2026-08-09"; the ruling record the commit names, `cowork_rulings_2026_08_09_sixth_stop.md`; and the rule's home at `CLAUDE.md`, decisions-register rule (l)
- *Retrieve:* `git show 9fe7f4561f750de4403b9bf9cfe812e474a1a5b3 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-10 · `ARCHITECTURE.md` @ `-1124 +1138,17` · 9fe7f4561f

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): the homing default is executed for three entries — the span typology gains the per-voice kind it was told to carry, the axis's unowned objects get their owner, and a motion-type reading stops being "owed at build"
- **Ground.** The commit's own account is "Dispatch `cc_instruction_return_continuation_6.md` Task 1, on the user's Ruling 38 of `cowork_rulings_2026_08_09_sixth_stop.md`: re-homing into the owning layer's specification is the DEFAULT closing route for the finish line's homing items", and both `ARCHITECTURE.md` hunks carry their own attribution — "user-ratified 2026-07-03; written here 2026-08-09". Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk assigns four ownerless analysis objects to the voice-leading axis, each written in AS A CLAIM discharged only at that component's own ratified design. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: one ground is a check at our own built catalogue — "the built chord catalogue already records exactly that with a voice-leading-defined flag on the entries concerned, checked at the catalogue rather than assumed". What decides it is that the hunk's one replaced line is a SPLIT made to insert the block, not a withdrawal, and that the catalogue check is offered as the REASON an object belongs to the axis rather than as a fact that found a documentation statement false.
- **The act:** the user's Ruling 38 of 2026-08-09, making re-homing into the owning layer's specification the default closing route, executed here for two entries the user ratified on 2026-07-03
- **Where its ratification is recorded:** each added block's own "user-ratified 2026-07-03; written here 2026-08-09"; the ruling record the commit names, `cowork_rulings_2026_08_09_sixth_stop.md`; and the rule's home at `CLAUDE.md`, decisions-register rule (l)
- *Retrieve:* `git show 9fe7f4561f750de4403b9bf9cfe812e474a1a5b3 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-10 · `ARCHITECTURE.md` @ `-369,0 +370,6` · 2fae57d212

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): Ruling 39's delegation is written verbatim — and its predicted outcome is refuted by measurement, because a delegation to the census cannot reach an entry that does not sit in the census
- **Ground.** The commit's own account is "Ruling 39's delegation is written verbatim", performed on the user's Ruling 39 of `cowork_rulings_2026_08_09_seventh_stop.md`, and it records that the wording is "the user's own, approved verbatim" and that the clause "and nothing else" was written. ★ The first class was applied first and does not fire: the hunk ADDS a delegation clause beside an existing naming, withdraws nothing, and cites no fact read in implementation code. ★ The commit's own body reports that the ruling's PREDICTED OUTCOME was refuted by measurement; that refutation is about which register entries the delegation reaches and is recorded on the rows, not in this hunk's text.
- **The act:** the user's Ruling 39 of 2026-08-09 — the exception to the Ruling 38 re-homing default, naming `cowork_score_census.md` as a document-level delegation whose reach is judged per section
- **Where its ratification is recorded:** the added text's own "user-ratified 2026-08-09; the Ruling 39 exception to the Ruling 38 re-homing default"; and the ruling record the commit names, `cowork_rulings_2026_08_09_seventh_stop.md`
- *Retrieve:* `git show 2fae57d21219e834a24a2e8cf391ae47cf66f63d --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-384,0 +385,42` · a74c821f89

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the first commissioning sitting's five rulings applied in one commit — and the one closing act needed the same rule applied twice along a chain the register itself names
- **Ground.** The commit's own account is "Rulings 60–64 of `cowork_rulings_2026_08_11_fourteenth_stop.md`, read whole (D-643), applied under `cc_instruction_return_continuation_14.md` Task 0", and all three `ARCHITECTURE.md` hunks are Ruling 63's — the priority-of-evidence rule homed for the production arm, the phase-1z scoping note annotated rather than re-worded, and one unqualified predicate corrected. Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk adds the evidential priority the emission is scored under, ruled ARM-INDEPENDENT, and states why: a premise a live open item puts under load had been stated only inside a section whose own scoping sentence disclaims describing the shipped analysis. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the block NAMES a conformance gap in the implementation — "the pitch and bass emissions reading the STRUCK set where the design says sounding". What decides it is that the block ADDS a rule and withdraws nothing, that its two grounds are the user's own recorded position of 2026-07-28 and the Layer-2 slice-identity specification, and that the gap is named in the WHAT-THIS-DOES-NOT-DO clause as DECLARED AND NOT FIXED, with the remedy left to the one design over the whole family at its #8-correct stage.
- **The act:** the user's Ruling 63 of 2026-08-11 — the priority-of-evidence rule homed for the production arm under D-668, the scoping note annotated rather than re-worded (#12), and the unqualified "no exception" corrected to "no PIECE-START exception"
- **Where its ratification is recorded:** each added block's own citation of the ruling — "Ruled by the user, 2026-08-11 (`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 63, closing `OPEN_ITEMS.md` OI-324)" — and that ruling record itself
- *Retrieve:* `git show a74c821f891415f42d5aa4f864901ae100c72697 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-4210,0 +4253,18` · a74c821f89

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the first commissioning sitting's five rulings applied in one commit — and the one closing act needed the same rule applied twice along a chain the register itself names
- **Ground.** The commit's own account is "Rulings 60–64 of `cowork_rulings_2026_08_11_fourteenth_stop.md`, read whole (D-643), applied under `cc_instruction_return_continuation_14.md` Task 0", and all three `ARCHITECTURE.md` hunks are Ruling 63's — the priority-of-evidence rule homed for the production arm, the phase-1z scoping note annotated rather than re-worded, and one unqualified predicate corrected. Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk adds an ANNOTATION beside the phase-1z scoping note saying what that note does and does not scope — the MECHANISM, not the evidential ranking — with the note itself preserved exactly as written (#12) and the excluded reading recorded. ★ The first class was applied first and does not fire: nothing is withdrawn, the annotation is explicitly chosen OVER a re-wording, and no fact read in implementation code is its source.
- **The act:** the user's Ruling 63 of 2026-08-11 — the priority-of-evidence rule homed for the production arm under D-668, the scoping note annotated rather than re-worded (#12), and the unqualified "no exception" corrected to "no PIECE-START exception"
- **Where its ratification is recorded:** each added block's own citation of the ruling — "Ruled by the user, 2026-08-11 (`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 63, closing `OPEN_ITEMS.md` OI-324)" — and that ruling record itself
- *Retrieve:* `git show a74c821f891415f42d5aa4f864901ae100c72697 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-4245 +4305,6` · a74c821f89

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the first commissioning sitting's five rulings applied in one commit — and the one closing act needed the same rule applied twice along a chain the register itself names
- **Ground.** The commit's own account is "Rulings 60–64 of `cowork_rulings_2026_08_11_fourteenth_stop.md`, read whole (D-643), applied under `cc_instruction_return_continuation_14.md` Task 0", and all three `ARCHITECTURE.md` hunks are Ruling 63's — the priority-of-evidence rule homed for the production arm, the phase-1z scoping note annotated rather than re-worded, and one unqualified predicate corrected. Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk REPLACES one sentence — "the priority of evidence, which now has no exception" becomes "which now has no PIECE-START exception" — with the correction's reason in its own parenthesis. ★ The first class was applied first and does NOT fire, although a standing statement IS replaced: the correction's source is stated in the added text and it is the DOCUMENT'S OWN INCONSISTENCY — a predicate that "named no argument — no exception TO WHAT — and which read plainly as contradicting the 'all but one narrow fallback case' sentence below it". No fact read in implementation code is cited, and the added text says which neighbouring sentence establishes the intended reading.
- **The act:** the user's Ruling 63 of 2026-08-11 — the priority-of-evidence rule homed for the production arm under D-668, the scoping note annotated rather than re-worded (#12), and the unqualified "no exception" corrected to "no PIECE-START exception"
- **Where its ratification is recorded:** each added block's own citation of the ruling — "Ruled by the user, 2026-08-11 (`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 63, closing `OPEN_ITEMS.md` OI-324)" — and that ruling record itself
- *Retrieve:* `git show a74c821f891415f42d5aa4f864901ae100c72697 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-2619,0 +2620,15` · 11af13a572

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction
- **Ground.** The commit's own account is "OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction", executing `cc_instruction_return_continuation_14.md` Task 1. It is the APPLICATION half of D-497, RATIFIED AMENDMENT A-7, and its scope line names no `src/` change, no golden, no corpus of scores, no constant moved and no behaviour change to the analysis. Here the hunk adds the mark on the Jazz chord-scoring constants, with the validation path named and the one thing a reader could mistake for validation named too — the Jazz regression check runs the Jazz preset over the Bach chorale corpus, which is not jazz ground truth. ★ The first class was applied first and does NOT fire, and the call is recorded because it is close: the block cites the implementation to say WHICH values are marked — the extension threshold against the default "the header declares", and the reduced inversion bonuses "set in `tools/batch_analyze.cpp`" — code this commit did not write. What decides it is that the block ADDS a mark and withdraws no statement: the citations IDENTIFY the constants the ratified rule reaches, and the establishment offered is the record's own (§4.1c and the corpus census), not a fact found in the code.
- **The act:** the application of D-497 — RATIFIED AMENDMENT A-7, user-ratified 2026-08-04, that every uncalibrated style constant carries the empirically-unvalidated mark with its validation path named — tracked at `OPEN_ITEMS.md` OI-346
- **Where its ratification is recorded:** each added block's own "the §6.6 rule applied, 2026-08-11 (`OPEN_ITEMS.md` OI-346, the application half of D-497)"; §6.6 itself, which states the rule and its maintenance; and D-497's own ratification at the 2026-07 architecture review
- *Retrieve:* `git show 11af13a5729a3b06cb49c3dbfdc76f3509a7ba58 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-4172 +4187` · 11af13a572

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction
- **Ground.** The commit's own account is "OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction", executing `cc_instruction_return_continuation_14.md` Task 1. It is the APPLICATION half of D-497, RATIFIED AMENDMENT A-7, and its scope line names no `src/` change, no golden, no corpus of scores, no constant moved and no behaviour change to the analysis. Here the hunk REPLACES the Jazz row of the preset table to carry the empirically-unvalidated mark and its validation path. ★ The first class was applied first and does NOT fire although a standing row IS replaced: the six values themselves are unchanged, what is added is the mark the ratified rule requires, and the source of the change is that rule rather than a fact read in implementation code.
- **The act:** the application of D-497 — RATIFIED AMENDMENT A-7, user-ratified 2026-08-04, that every uncalibrated style constant carries the empirically-unvalidated mark with its validation path named — tracked at `OPEN_ITEMS.md` OI-346
- **Where its ratification is recorded:** each added block's own "the §6.6 rule applied, 2026-08-11 (`OPEN_ITEMS.md` OI-346, the application half of D-497)"; §6.6 itself, which states the rule and its maintenance; and D-497's own ratification at the 2026-07 architecture review
- *Retrieve:* `git show 11af13a5729a3b06cb49c3dbfdc76f3509a7ba58 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-4176,0 +4192,15` · 11af13a572

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction
- **Ground.** The commit's own account is "OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction", executing `cc_instruction_return_continuation_14.md` Task 1. It is the APPLICATION half of D-497, RATIFIED AMENDMENT A-7, and its scope line names no `src/` change, no golden, no corpus of scores, no constant moved and no behaviour change to the analysis. Here the hunk adds what the mark on that row means and what it does NOT say — not that the six values are wrong, and not that anything about the analysis moves. ★ The first class was applied first and does NOT fire, and the call is recorded because the establishment offered is a MEASUREMENT — §4.1c's recorded consequence that jazz accuracy is not measurable on the corpora held, measured by the bass-injection experiment. What decides it is that the measurement is about the CORPORA HELD rather than about our code, that the block ADDS and withdraws nothing, and that it is offered as the ratified rule's own establishment requirement.
- **The act:** the application of D-497 — RATIFIED AMENDMENT A-7, user-ratified 2026-08-04, that every uncalibrated style constant carries the empirically-unvalidated mark with its validation path named — tracked at `OPEN_ITEMS.md` OI-346
- **Where its ratification is recorded:** each added block's own "the §6.6 rule applied, 2026-08-11 (`OPEN_ITEMS.md` OI-346, the application half of D-497)"; §6.6 itself, which states the rule and its maintenance; and D-497's own ratification at the 2026-07 architecture review
- *Retrieve:* `git show 11af13a5729a3b06cb49c3dbfdc76f3509a7ba58 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-5391,4 +5421,20` · 11af13a572

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs(architecture): OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction
- **Ground.** The commit's own account is "OI-346's marks reached at last as a dedicated task — the Jazz half applied with its establishment, the idiom half HELD because #19 forbids a verdict in either direction", executing `cc_instruction_return_continuation_14.md` Task 1. It is the APPLICATION half of D-497, RATIFIED AMENDMENT A-7, and its scope line names no `src/` change, no golden, no corpus of scores, no constant moved and no behaviour change to the analysis. Here the hunk REPLACES §6.6's closing clause — which said the mark was not applied at HEAD — with how far the application has got, and records the idiom half as HELD rather than guessed, because #19 forbids a verdict in either direction where no surface maps the five idiom names onto a per-idiom ground-truth verdict. The former wording stands preserved (#12). ★ The first class was applied first and does NOT fire although a standing statement IS replaced: what made it false is THIS COMMIT'S OWN documentation act, not a fact read in implementation code.
- **The act:** the application of D-497 — RATIFIED AMENDMENT A-7, user-ratified 2026-08-04, that every uncalibrated style constant carries the empirically-unvalidated mark with its validation path named — tracked at `OPEN_ITEMS.md` OI-346
- **Where its ratification is recorded:** each added block's own "the §6.6 rule applied, 2026-08-11 (`OPEN_ITEMS.md` OI-346, the application half of D-497)"; §6.6 itself, which states the rule and its maintenance; and D-497's own ratification at the 2026-07 architecture review
- *Retrieve:* `git show 11af13a5729a3b06cb49c3dbfdc76f3509a7ba58 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-1111 +1111,11` · bf48b1f834

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: the session-small drain — four gating rows closed, and one act came out different from its sizing because the drift sat inside a correction
- **Ground.** The commit's own account is "the session-small drain — four gating rows closed", executing `cc_instruction_return_continuation_14.md` Task 3, and the three `ARCHITECTURE.md` hunks are OI-318's two label defects. Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk records that the document's own account of how far the rename reached was ONE INSTANCE SHORT, and states what that shows about the enumeration — it was built by looking for one banned word, so a second banned word was outside what it could find, and its count is not a bound on how many exist. ★ The first class was applied first and does not fire: the correction's source is a READ OF THIS DOCUMENT — a second reserved word standing in its own Layer-6 paragraph — and no fact read in implementation code is cited.
- **The act:** the ratified terminology rename of 2026-07-01, which reserves the bare word for the accepted melodic phrase alone, applied here to the two places this document breached it — tracked at `OPEN_ITEMS.md` OI-318 item (1)
- **Where its ratification is recorded:** each added block's own naming of "the ratified 2026-07-01 rename" and of the delegated design's terminology section, which the correction cites as the thing the breach contradicted
- *Retrieve:* `git show bf48b1f834afe7b0b71da7473b373e37549e99ea --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-2184,3 +2194,8` · bf48b1f834

- **Verdict:** RATIFIED-ACT EDIT · shape `governing-decision-record`
- **Commit subject:** docs: the session-small drain — four gating rows closed, and one act came out different from its sizing because the drift sat inside a correction
- **Ground.** The commit's own account is "the session-small drain — four gating rows closed", executing `cc_instruction_return_continuation_14.md` Task 3, and the three `ARCHITECTURE.md` hunks are OI-318's two label defects. Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk REPLACES the Layer-6 paragraph's three uses of the reserved word with the punctuation-span, with the former wording preserved in place (#12) and the reason stated — the paragraph told a reader that the grouping layer segments melodic phrases, "the one thing the delegated design's terminology section exists to deny". ★ The first class was applied first and does NOT fire although a standing statement IS replaced: the source is the ratified rename and the delegated design's own terminology section, not a fact read in implementation code.
- **The act:** the ratified terminology rename of 2026-07-01, which reserves the bare word for the accepted melodic phrase alone, applied here to the two places this document breached it — tracked at `OPEN_ITEMS.md` OI-318 item (1)
- **Where its ratification is recorded:** each added block's own naming of "the ratified 2026-07-01 rename" and of the delegated design's terminology section, which the correction cites as the thing the breach contradicted
- *Retrieve:* `git show bf48b1f834afe7b0b71da7473b373e37549e99ea --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-11 · `ARCHITECTURE.md` @ `-8153 +8168,7` · bf48b1f834

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** docs: the session-small drain — four gating rows closed, and one act came out different from its sizing because the drift sat inside a correction
- **Ground.** The commit's own account is "the session-small drain — four gating rows closed", executing `cc_instruction_return_continuation_14.md` Task 3, and the three `ARCHITECTURE.md` hunks are OI-318's two label defects. Its scope line names no `src/` change, no golden, no corpus of scores and no behaviour change to the analysis. Here the hunk RENUMBERS a section heading: two sections carried the same number, and neighbouring text cites into that run by number, so a citation did not resolve. ★ The first class was applied first and does not fire — no statement about the system is made or withdrawn, and the added parenthesis says in terms that the change "changes no content and leaves nothing below it renumbered". The second does not fire either: the act cites a standing documentation rule about this document's section numbers rather than recording what any user act ruled. The third does, this being a re-heading exactly.
- *Retrieve:* `git show bf48b1f834afe7b0b71da7473b373e37549e99ea --no-color -U0 -- ARCHITECTURE.md`

## What this screen does not do

No screened document is edited. Nothing is restored, reverted, reconciled or corrected. No open-items row is marked, flipped or discarded; no decisions-register entry is written. No fix, design or measurement of the analysis is authorized or performed. The period question is not re-opened here — the report says what would re-open it, and the act is the user's.

## The inherited establishment caveat (#19)

#19, INHERITED AND NOT DISCHARGED HERE. Every count below is a re-derivation over the two candidate artifacts, and the generator that produced those artifacts (`tools/audit/gen_doc_change_candidates.py`) has itself never been positively established — it was written in one batch, and its own artifact marks assumption A3 UNESTABLISHED for every generator family. What THIS tool establishes is that the split follows from those artifacts and reconciles with the totals they publish of themselves. It establishes nothing about whether the enumeration underneath them is complete or correct, and a reader may not take a clean re-derivation here as evidence that it is. What would settle the inherited half is an establishment pass over that generator — an act named here and not started.
