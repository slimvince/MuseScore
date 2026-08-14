# The July screen — the out-of-period specification-bearing flagged hunks, read one at a time

> **GENERATED FILE — do not hand-edit.** Written by `tools/audit/gen_july_screen.py`; re-derive with `--check`. Every verdict below is AUTHORED and every count is DERIVED. The screen edits no document it reads.

## ★ THE FALSIFICATION RULE FIRES — the period question is RE-OPENED FOR THE USER

**1 of 68 screened hunks classify POSITIVELY-CODE-INFLUENCED.** The ruled falsification rule is: *"if any shows a code-influenced correction, the period question RE-OPENS"* — and the re-opening is the user's act on this report, not this screen's.

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
| POSITIVELY-CODE-INFLUENCED | 1 |
| RATIFIED-ACT-EDIT | 40 |
| RESTRUCTURING-SHAPED | 12 |
| UNDETERMINED | 15 |

**The classes, and the order they are applied in** (the order is declared because it decides cases, and the first class is applied FIRST so that a ratified act cannot launder a correction made under it):

- **POSITIVELY-CODE-INFLUENCED** — The change WITHDRAWS, NARROWS, QUALIFIES or REPLACES something the documentation already stated, and the source of the replacement is a fact read in implementation code THIS COMMIT DID NOT WRITE; or the change's own account states that a documentation statement was corrected against the implementation. APPLIED FIRST, so a ratified act cannot launder a correction made under it.
- **RATIFIED-ACT-EDIT** — The change writes, re-stamps or records what a NAMED user act ruled, ratified or directed — including the same-commit documentation half of a ratified change to the code. The act AND where its ratification is recorded are both cited, or the class is not admitted (assumption A3).
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

- **Limb 1 — the large majority classify RATIFIED-ACT-EDIT or RESTRUCTURING-SHAPED:** 52 of 68 (0.7647). The prediction says *large majority* and fixes no threshold, so the share is published and the reading is left to the reader rather than computed against a number nobody registered.
- **Limb 2 — ZERO classify POSITIVELY-CODE-INFLUENCED:** predicted 0, derived 1 — **REFUTED**. "one hunk whose change, or whose commit's own account, states or shows correction against the implementation" — which is the condition this screen applies as its first class.

Nothing in the verdicts was adjusted to make a limb hold. A prediction is graded and never used as an input (#17b).

## Assumption A2 — the retrieval, checked per hunk rather than asserted

Every hunk's text was retrieved from the git object by explicit hash — `git show <commit> --no-color -U0 -- <path>` — and its recorded header looked for among the headers that came back. Performed on every run, not asserted.

- Hunks that did not resolve: **0**.
- Hunks whose retrieved line counts disagree with the population's own record: **0**.

## Every hunk, with its verdict and its ground

### 2026-07-11 · `CLAUDE.md` @ `-44 +44,3` · 6b4ca1752b

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): #17(c) control-flow-first RATIFIED + the siloed-facts audit (spelling was not alone) + register section I (OI-72..OI-80)
- **Ground.** The hunk rewrites principle #17(c) to put the control-flow question first, and the added text carries its own attribution — "control flow — ratified sharpening 2026-07-10, the EG-2 desk-sim lesson". The commit's account opens "User ratified the #17(c) sharpening". No fact about the implementation appears in the change or in the account.
- **The act:** the #17(c) control-flow-first sharpening of the Premise Gate
- **Where its ratification is recorded:** the added text itself; the commit's own account; and CLAUDE.md's #17 provenance paragraph at HEAD, which records #17–19 as ratified by the user on 2026-07-10
- *Retrieve:* `git show 6b4ca1752b6f857027da1b9ddff4ea9fd3081814 --no-color -U0 -- CLAUDE.md`

### 2026-07-11 · `CLAUDE.md` @ `-63,0 +64,6` · 2454658f07

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
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

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): L1/L2 certification withheld on partial blinding - OI-89 + DT-20 + the blind re-run instruction; CLAUDE.md conventions: no self-invented labels; the self-check after every coding exercise
- **Ground.** The hunk adds two conventions, each carrying its own attribution — "(User-directed, repeatedly; recorded 2026-07-11.)" and "(user-directed, 2026-07-11)". Neither mentions the implementation.
- **The act:** the no-self-invented-labels convention and the standing self-check after every coding exercise
- **Where its ratification is recorded:** the added text itself, and both rules at CLAUDE.md at HEAD
- *Retrieve:* `git show 239408faadf40e2d46c428397522ca3d688dbe5d --no-color -U0 -- CLAUDE.md`

### 2026-07-12 · `CLAUDE.md` @ `-177,11 +177,18` · d9b52ba969

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-142/OI-143 key-grading re-baseline — corpus-transposition correction + dual home/local key columns (user-ratified 2026-07-12)
- **Ground.** Gate block (A) is re-stamped with the values the OI-142/OI-143 re-baseline measured. The commit's subject carries "(user-ratified 2026-07-12)" and the added text repeats it. The superseded column is preserved in place with its snapshot directory named (#12). What the re-baseline changed is the GRADING — the transposition offsets applied to the ground truth and the key column split in two — not a statement about what the implementation does.
- **The act:** the OI-142/OI-143 key-grading re-baseline
- **Where its ratification is recorded:** the commit subject and the added text; the same re-baseline is recorded in gate block (A)'s superseded-column lineage at CLAUDE.md at HEAD
- *Retrieve:* `git show d9b52ba9696ae51f1504c902c04825c538313754 --no-color -U0 -- CLAUDE.md`

### 2026-07-12 · `CLAUDE.md` @ `-213,4 +220,12` · d9b52ba969

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-142/OI-143 key-grading re-baseline — corpus-transposition correction + dual home/local key columns (user-ratified 2026-07-12)
- **Ground.** Gate block (A) is re-stamped with the values the OI-142/OI-143 re-baseline measured. The commit's subject carries "(user-ratified 2026-07-12)" and the added text repeats it. The superseded column is preserved in place with its snapshot directory named (#12). What the re-baseline changed is the GRADING — the transposition offsets applied to the ground truth and the key column split in two — not a statement about what the implementation does.
- **The act:** the OI-142/OI-143 key-grading re-baseline
- **Where its ratification is recorded:** the commit subject and the added text; the same re-baseline is recorded in gate block (A)'s superseded-column lineage at CLAUDE.md at HEAD
- *Retrieve:* `git show d9b52ba9696ae51f1504c902c04825c538313754 --no-color -U0 -- CLAUDE.md`

### 2026-07-12 · `CLAUDE.md` @ `-68,0 +69,9` · fe985ab047

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): preserve the concurrent live edits — publish-evidence-broadly rule + the evidence inventory + OI-146
- **Ground.** The hunk adds the amendment whose own opening is "*Amendment (user, 2026-07-12, at the evidence-inventory discussion):*" and which quotes the user's rationale. The commit's account names it "the user's 2026-07-12 amendment to the fact-publication corollary".
- **The act:** the user's amendment for EVIDENCE-class facts (publish broadly without a named consumer)
- **Where its ratification is recorded:** the added text itself, and the same amendment at CLAUDE.md at HEAD
- *Retrieve:* `git show fe985ab04757dc9eb214ed12664001fa5156238e --no-color -U0 -- CLAUDE.md`

### 2026-07-13 · `CLAUDE.md` @ `-194 +194` · 800f1a12bf

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-132 — the parent-collection mode grading, consolidated into the ONE key reduction (re-baseline, user-ratified 2026-07-13)
- **Ground.** The key columns of gate block (A) are re-stamped at the OI-132 mode-grading consolidation. The commit's account carries both dates in terms — "Ruling: the user, 2026-07-12 … Ratified: the user, 2026-07-13" — and the added text repeats "user-ratified 2026-07-13". The superseded columns are preserved with their snapshot directory named (#12). The consolidation changed how an emitted mode is GRADED, not what the implementation does.
- **The act:** the OI-132 parent-collection mode-grading consolidation
- **Where its ratification is recorded:** the commit's own account; and the same convention at CLAUDE.md at HEAD, among the four grading conventions the robust unit is measured under
- *Retrieve:* `git show 800f1a12bf136ebc80b84d05427570a9be0a7a5b --no-color -U0 -- CLAUDE.md`

### 2026-07-13 · `CLAUDE.md` @ `-196,8 +196,22` · 800f1a12bf

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(tools): OI-132 — the parent-collection mode grading, consolidated into the ONE key reduction (re-baseline, user-ratified 2026-07-13)
- **Ground.** The key columns of gate block (A) are re-stamped at the OI-132 mode-grading consolidation. The commit's account carries both dates in terms — "Ruling: the user, 2026-07-12 … Ratified: the user, 2026-07-13" — and the added text repeats "user-ratified 2026-07-13". The superseded columns are preserved with their snapshot directory named (#12). The consolidation changed how an emitted mode is GRADED, not what the implementation does.
- **The act:** the OI-132 parent-collection mode-grading consolidation
- **Where its ratification is recorded:** the commit's own account; and the same convention at CLAUDE.md at HEAD, among the four grading conventions the robust unit is measured under
- *Retrieve:* `git show 800f1a12bf136ebc80b84d05427570a9be0a7a5b --no-color -U0 -- CLAUDE.md`

### 2026-07-13 · `CLAUDE.md` @ `-230,7 +244,12` · 800f1a12bf

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
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
- **Note.** Ruling 4 of the eighteenth stop is what keeps this in view: an addition can make a correct specification wrong without removing a word. Whether a specification that states what the code does — even while calling it a defect — pre-empts the comparison a later audit would have made is not establishable from the text, which is why the verdict is NOT CLEARED rather than either clear class.
- *Retrieve:* `git show 153d45e78c5162c17844c7a488f9e9901b524141 --no-color -U0 -- docs/scoring_model.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-556 +579` · 153d45e78c

- **Verdict:** POSITIVELY-CODE-INFLUENCED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** feat(composing): OI-168 — default-OFF key-collection probe + the signature-mask A/B variant (measurement build)
- **Ground.** A STANDING table entry is REPLACED. It read "Awarded when root is a scale member of the current key."; it now reads that the bonus is awarded on membership in the current key's collection, names the code-level predicate the term shares with its sibling, and carries "including its OI-168 defect on `Altered` / `AlteredDomBB7`". The source of the replacement is a reading of implementation code THIS COMMIT DID NOT WRITE — the commit's own account states the doc-sync "documents the shared predicate and the defect", and states that the predicate's committed branch is the same test as before. That is a standing documentation statement altered against the implementation, which is this class.
- **Note.** THE COUNTER-CONSIDERATION, recorded because the user's act rests on this hunk: the replacement does not ERASE the discrepancy — it names the defect, points at the §4 block that measures it, and the same commit builds a default-OFF measurement of it. The substance of the first clause may also be unchanged, since "scale member of the current key" and "member of the current key's collection" are arguably the same claim in different words. What fires the class is the test as the dispatch states it — the change, and its commit's own account, show a documentation statement altered against the implementation — not a judgment that evidence was destroyed here.
- *Retrieve:* `git show 153d45e78c5162c17844c7a488f9e9901b524141 --no-color -U0 -- docs/scoring_model.md`

### 2026-07-14 · `CLAUDE.md` @ `-186 +186` · 10235d5547

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified)", and the added text carries "dispatch user-ratified 2026-07-13". The superseded reference is preserved with its snapshot directory named (#12).
- **The act:** the OI-168 signature-mask correctness fix and its re-baseline
- **Where its ratification is recorded:** the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose OI-168 re-baseline block records the same ratification
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `CLAUDE.md` @ `-190,8 +190,32` · 10235d5547

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified)", and the added text carries "dispatch user-ratified 2026-07-13". The superseded reference is preserved with its snapshot directory named (#12).
- **The act:** the OI-168 signature-mask correctness fix and its re-baseline
- **Where its ratification is recorded:** the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose OI-168 re-baseline block records the same ratification
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `CLAUDE.md` @ `-244 +268,4` · 10235d5547

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** Gate block (A) is re-stamped at the OI-168 signature-mask fix. The commit's account opens "The inference-affecting half of the OI-168 dispatch (cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified)", and the added text carries "dispatch user-ratified 2026-07-13". The superseded reference is preserved with its snapshot directory named (#12).
- **The act:** the OI-168 signature-mask correctness fix and its re-baseline
- **Where its ratification is recorded:** the commit's own account; and gate block (A) at CLAUDE.md at HEAD, whose OI-168 re-baseline block records the same ratification
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- CLAUDE.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-263,22 +263,34` · 10235d5547

- **Verdict:** RATIFIED-ACT-EDIT · shape `same-commit-code-documentation`
- **Commit subject:** feat(composing): OI-168 FIX — the two key-consuming scoring terms take the key SIGNATURE's collection, not the tonic (correctness re-baseline, user-ratified)
- **Ground.** The §4 block and the table entry are rewritten to describe the behaviour THIS COMMIT INTRODUCES — the two terms now test the key signature's own collection — and the form they replaced is kept beside them as "the defect it replaced". The commit's account names the act and its ratification, and names the standing rule that requires the documentation to move in the same commit. Documentation and implementation moved together under one ratified act, so no standing statement was aligned to unchanged behaviour.
- **The act:** the OI-168 signature-mask correctness fix
- **Where its ratification is recorded:** the commit's own account ("cc_instruction_oi168_fix.md, Cowork 2026-07-13, user-ratified"); and gate block (A) at CLAUDE.md at HEAD
- *Retrieve:* `git show 10235d5547865c899fb088423fcf3a151fa9520e --no-color -U0 -- docs/scoring_model.md`

### 2026-07-14 · `docs/scoring_model.md` @ `-579 +591` · 10235d5547

- **Verdict:** RATIFIED-ACT-EDIT · shape `same-commit-code-documentation`
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

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs: ratify principles #20-#24 + joint-estimator plan amendments (OI-176...OI-181), user-ratified 2026-07-18
- **Ground.** The governing-decision banner is added, its own first words "★★ GOVERNING DECISION (user-ratified 2026-07-17): the key/mode/chord estimator is JOINT". The commit's account lists it among the 2026-07-17 joint-architecture decision documents.
- **The act:** the joint key/mode/chord estimator as the target architecture
- **Where its ratification is recorded:** the added banner itself, which is still at the top of ARCHITECTURE.md at HEAD
- *Retrieve:* `git show 06d4318bd1f322d055d04622681587c44a01bffb --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-18 · `CLAUDE.md` @ `-56,0 +57,27` · 06d4318bd1

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs: ratify principles #20-#24 + joint-estimator plan amendments (OI-176...OI-181), user-ratified 2026-07-18
- **Ground.** Principles #20–#24 and the constrained-optimum ledger corollary are added. The commit's account names them "(user-ratified 2026-07-18)".
- **The act:** principles #20–#24 and the constrained-optimum ledger corollary
- **Where its ratification is recorded:** CLAUDE.md's #17–#24 provenance paragraph, which records the 2026-07-18 ratification at the joint-estimator plan review and stands at HEAD
- *Retrieve:* `git show 06d4318bd1f322d055d04622681587c44a01bffb --no-color -U0 -- CLAUDE.md`

### 2026-07-18 · `CLAUDE.md` @ `-82 +109,4` · 06d4318bd1

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
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
- **Ground.** A new document indexing the locally held copies and what each settled in the theory grounding, plus the note that the binaries live only in a private repository. Its subject is the literature and file handling; no fact from the implementation is its source.
- *Retrieve:* `git show 4f2c5ddfdb0ecd2e4363982b0dc722dd9e7e52e0 --no-color -U0 -- docs/research_papers/README.md`

### 2026-07-25 · `ARCHITECTURE.md` @ `-768 +768` · 1e35415ee0

- **Verdict:** UNDETERMINED · shape `same-commit-code-documentation`
- **Commit subject:** composing: joint estimator Task B — the L1 fact-surface additive extension (notatedNotes)
- **Ground.** The standing note-model row is extended to describe the additive `notatedNotes()` surface this commit itself adds. The commit's account names the act — "ARCHITECTURE.md L1 note-model row synced (#10 / OI-146)". A sanction is named (OI-180) but no user act and no place of ratification is citable from the change or its account, so the RATIFIED-ACT class is not admitted (assumption A3). Nothing standing is withdrawn. NOT CLEARED.
- *Retrieve:* `git show 1e35415ee06b77e001aeea3b947369a2016573b3 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-10,0 +11,25` · 205dd0843a

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** The as-built banner for the adoption is added, its own first words "★★ AS-BUILT (the OI-178 adoption, user-ratified 2026-07-26, option 1 — STAGED SCOPE)". The commit's subject and account carry the same.
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added banner; and gate block (A) at CLAUDE.md at HEAD, which records the adoption as user-ratified 2026-07-26 with its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `CLAUDE.md` @ `-219 +219,3` · 205dd0843a

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence statement, the staged-scope declaration, and the superseded columns preserved with their snapshot named (#12). The commit subject and the added text both carry "user-ratified 2026-07-26, option 1".
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified baselines still record this adoption and its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-228,7 +230,28` · 205dd0843a

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence statement, the staged-scope declaration, and the superseded columns preserved with their snapshot named (#12). The commit subject and the added text both carry "user-ratified 2026-07-26, option 1".
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified baselines still record this adoption and its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-300,8 +323,13` · 205dd0843a

- **Verdict:** RATIFIED-ACT-EDIT · shape `measured-value-re-stamp`
- **Commit subject:** composing: joint estimator — THE OI-178 ADOPTION (batch/corpus surface; staged scope, user-ratified option 1)
- **Ground.** Gate block (A) is re-baselined at the adoption: the new columns, the preset-independence statement, the staged-scope declaration, and the superseded columns preserved with their snapshot named (#12). The commit subject and the added text both carry "user-ratified 2026-07-26, option 1".
- **The act:** the OI-178 joint-estimator adoption on the batch/corpus surface (staged scope)
- **Where its ratification is recorded:** the added text; and gate block (A) at CLAUDE.md at HEAD, whose ratified baselines still record this adoption and its measurement provenance
- *Retrieve:* `git show 205dd0843aff3e41e3da3ff7e8e6e4147b320d74 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-105,0 +106,14` · 00c0df81c5

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** ratification record: notation-layer adoption increment decision surface + the decision-neutrality principles corollary (user, 2026-07-26); rows OI-193/OI-194
- **Ground.** The decision-neutrality corollary is added, its own opening "(corollary to #4/#6/#19; user-ratified 2026-07-26)". The commit's subject is a ratification record.
- **The act:** the decision-neutrality corollary
- **Where its ratification is recorded:** the added text, and the same corollary at CLAUDE.md at HEAD, whose provenance names the notation-layer adoption increment's decision surface
- *Retrieve:* `git show 00c0df81c5682fbda0515a81cea0c3c541e8ee23 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `CLAUDE.md` @ `-112 +126,3` · 00c0df81c5

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** ratification record: notation-layer adoption increment decision surface + the decision-neutrality principles corollary (user, 2026-07-26); rows OI-193/OI-194
- **Ground.** The provenance paragraph is extended to record the corollary's ratification and where its analysis lives. It is the citation half of the same act.
- **The act:** the decision-neutrality corollary
- **Where its ratification is recorded:** the extended provenance paragraph itself, at CLAUDE.md at HEAD
- *Retrieve:* `git show 00c0df81c5682fbda0515a81cea0c3c541e8ee23 --no-color -U0 -- CLAUDE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-18,3 +18,14` · 83fbb9e661

- **Verdict:** RATIFIED-ACT-EDIT · shape `same-commit-code-documentation`
- **Commit subject:** composing: joint estimator — Decision D1 EXECUTED (fitted tables + selected weight vector embedded as provenance-stamped generated source)
- **Ground.** The as-built banner is amended to record the embedded table/weight delivery THIS COMMIT introduces, and the changed sentences describe the new delivery rather than the old one. The commit's subject is "Decision D1 EXECUTED" and its account cites "ratified Decision D1, cowork_notation_adoption_increment.md §5".
- **The act:** ratified Decision D1 — the fitted tables and the selected weight vector embedded as provenance-stamped generated source
- **Where its ratification is recorded:** `cowork_notation_adoption_increment.md` §5, the decision surface CLAUDE.md's decision-neutrality corollary records as user-ratified 2026-07-26
- *Retrieve:* `git show 83fbb9e66156d2c0fc4ad6b2f98cad4ed46e4146 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-26 · `ARCHITECTURE.md` @ `-24 +35,2` · 83fbb9e661

- **Verdict:** RATIFIED-ACT-EDIT · shape `same-commit-code-documentation`
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
- **Ground.** An as-built block is added for the notation record §3.1–§3.6 delivered across this commit and its predecessors, with its establishment. The commit's account names a ratified decision (C1) for ONE part of what the block describes — the modal reading — and no user act for the rest, so the RATIFIED-ACT class is not admitted for the hunk as a whole (assumption A3). NOT CLEARED.
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

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** register split: OPEN_ITEMS.md -> lean index + open_items/ per-item detail files (user-ratified option 1, 2026-07-26; byte-reconciled, status authoritative in the index)
- **Ground.** The open-items register section is rewritten for the index-plus-detail split, and the changed text carries "split into index + detail files, user-ratified 2026-07-26" and "user-ratified option 1". The commit subject carries the same. The rules (a)–(e) are re-worded for the split; no fact from the implementation is the source.
- **The act:** the open-items register's split into a lean index plus one detail file per item
- **Where its ratification is recorded:** the changed text itself, and the same section at CLAUDE.md at HEAD
- *Retrieve:* `git show 1e32b5e92e2594d3a8d1752fcea051dab16f60a7 --no-color -U0 -- CLAUDE.md`

### 2026-07-27 · `CLAUDE.md` @ `-135,6 +135,12` · 1e32b5e92e

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** register split: OPEN_ITEMS.md -> lean index + open_items/ per-item detail files (user-ratified option 1, 2026-07-26; byte-reconciled, status authoritative in the index)
- **Ground.** The open-items register section is rewritten for the index-plus-detail split, and the changed text carries "split into index + detail files, user-ratified 2026-07-26" and "user-ratified option 1". The commit subject carries the same. The rules (a)–(e) are re-worded for the split; no fact from the implementation is the source.
- **The act:** the open-items register's split into a lean index plus one detail file per item
- **Where its ratification is recorded:** the changed text itself, and the same section at CLAUDE.md at HEAD
- *Retrieve:* `git show 1e32b5e92e2594d3a8d1752fcea051dab16f60a7 --no-color -U0 -- CLAUDE.md`

### 2026-07-27 · `CLAUDE.md` @ `-142,2 +148,3` · 1e32b5e92e

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
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
- **Ground.** Part of the P7 consolidation: the consolidated section header replaces the first per-unit heading, and the framing text restates the dual-arm posture the five blocks already carried. The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-121,2 +130,3` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** Part of the P7 consolidation: a consumer sentence is re-pointed from a later dispatch to the subsections below it. The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-130,3 +140,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** Part of the P7 consolidation: a per-unit heading becomes numbered subsection (2). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-152,2 +161,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** Part of the P7 consolidation: a per-unit heading becomes numbered subsection (3). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-177,2 +186,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** Part of the P7 consolidation: a per-unit heading becomes numbered subsection (4). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-199,4 +208` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** Part of the P7 consolidation: a forward-looking sentence about what remains before the switch is trimmed to one line, its substance carried into the new subsection (6). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-204,2 +210,2` · 4967d6b724

- **Verdict:** RESTRUCTURING-SHAPED · shape `document-relocation-or-re-heading`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** Part of the P7 consolidation: a per-unit heading becomes numbered subsection (5). The commit's account states the act and its own no-loss claim — "the five accumulated per-unit record-path blocks consolidated into ONE coherent as-built section (nothing historical removed)". No fact newly read in the implementation is the source of the change.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-223,0 +230,13` · 4967d6b724

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** notation seams-2 P7: partition close-out — completeness verified, docs consolidated (pre-switch state)
- **Ground.** A new subsection (6) is added stating the dual path's current state — the flag OFF everywhere, the partition closed out and completeness-verified, the three suites green — and what the switch would do. The state it reports is read off a verification of the code performed in the same commit. Nothing standing is withdrawn. NOT CLEARED.
- *Retrieve:* `git show 4967d6b724ba8bcb7dd0cbdfbc0ab4898bb66a17 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-100,8 +100,9` · 2a81af273e

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** THE NOTATION SWITCH: the record path is the production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens refreshed against the P6-classified record output; staged scope CLOSED
- **Ground.** The dormant-posture text is replaced by the switched posture: the record path is the production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. The commit's subject carries "(user-ratified 2026-07-27)" and every changed passage repeats it. The replaced statements were made false by the ratified act itself, not by a reading of the code.
- **The act:** THE NOTATION SWITCH — the record path made the production in-app notation analysis
- **Where its ratification is recorded:** the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED SCOPE block records the switch as user-ratified 2026-07-27
- *Retrieve:* `git show 2a81af273ee9b9339736f6e03b0fc96b55bc5005 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `ARCHITECTURE.md` @ `-231,12 +232,18` · 2a81af273e

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** THE NOTATION SWITCH: the record path is the production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens refreshed against the P6-classified record output; staged scope CLOSED
- **Ground.** The dormant-posture text is replaced by the switched posture: the record path is the production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. The commit's subject carries "(user-ratified 2026-07-27)" and every changed passage repeats it. The replaced statements were made false by the ratified act itself, not by a reading of the code.
- **The act:** THE NOTATION SWITCH — the record path made the production in-app notation analysis
- **Where its ratification is recorded:** the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED SCOPE block records the switch as user-ratified 2026-07-27
- *Retrieve:* `git show 2a81af273ee9b9339736f6e03b0fc96b55bc5005 --no-color -U0 -- ARCHITECTURE.md`

### 2026-07-27 · `CLAUDE.md` @ `-269,4 +269,16` · 2a81af273e

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** THE NOTATION SWITCH: the record path is the production notation analysis (user-ratified 2026-07-27) — flag default ON; goldens refreshed against the P6-classified record output; staged scope CLOSED
- **Ground.** The dormant-posture text is replaced by the switched posture: the record path is the production notation analysis, the legacy path compiled and dormant, the staged scope CLOSED. The commit's subject carries "(user-ratified 2026-07-27)" and every changed passage repeats it. The replaced statements were made false by the ratified act itself, not by a reading of the code.
- **The act:** THE NOTATION SWITCH — the record path made the production in-app notation analysis
- **Where its ratification is recorded:** the changed text; and gate block (A) at CLAUDE.md at HEAD, whose STAGED SCOPE block records the switch as user-ratified 2026-07-27
- *Retrieve:* `git show 2a81af273ee9b9339736f6e03b0fc96b55bc5005 --no-color -U0 -- CLAUDE.md`

### 2026-07-28 · `docs/score_inventory.md` @ `-234 +234,18` · 5135764ed7

- **Verdict:** UNDETERMINED · shape `describes-pre-existing-implementation-behaviour`
- **Commit subject:** OI-206 analysis-cost Task 6: dated notes + doc sync (READ-ONLY)
- **Ground.** A subfolder of large scores is added to the inventory with measured counts, the licence read from each file's own metadata, and a closing note that the joint decoder returns an EMPTY analysis on 13 of the 23. That last clause is a measured fact about the implementation's behaviour. Nothing standing is withdrawn and no user act is cited. NOT CLEARED.
- *Retrieve:* `git show 5135764ed7f8d7b992ed5f1c3b4c2fecab7f5d35 --no-color -U0 -- docs/score_inventory.md`

### 2026-07-28 · `CLAUDE.md` @ `-720,0 +721,19` · 8c8e57eab9

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cc): decision harvest — register rows + OI-207/208 notes (Task 0)
- **Ground.** The never-work-from-memory convention is added, its own opening "(user-directed, 2026-07-28; binds Cowork and CC equally)". Its founding instance names a specification and the position it states; the rule itself is the user's.
- **The act:** the never-work-from-memory convention
- **Where its ratification is recorded:** the added text, and the same convention at CLAUDE.md at HEAD
- *Retrieve:* `git show 8c8e57eab9c031bb126f2521f378382e8fead1e6 --no-color -U0 -- CLAUDE.md`

### 2026-07-28 · `CLAUDE.md` @ `-724,0 +744,51` · 8c8e57eab9

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cc): decision harvest — register rows + OI-207/208 notes (Task 0)
- **Ground.** The writing-standards pointer and the music-theory reserved-word convention with its disambiguation rule are added, each carrying "(user-directed, 2026-07-28)" or an earlier dated user attribution. No fact from the implementation is the source.
- **The act:** the writing-standards pointer and the music-theory reserved-word / disambiguation convention
- **Where its ratification is recorded:** the added text, and both conventions at CLAUDE.md at HEAD
- *Retrieve:* `git show 8c8e57eab9c031bb126f2521f378382e8fead1e6 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `CLAUDE.md` @ `-795,0 +796,14` · 80ad92f9d3

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cc): decisions register — Task 1 corrections (provenance re-aims, anchors, rewordings, derivation flags, STATUS order)
- **Ground.** The every-design-decision-carries-its-defense convention is added, its own opening "(user-directed, 2026-08-01, at the decisions-register ratification review)". The commit's account records it as a riding Cowork edit of that date.
- **The act:** the convention that every design decision carries its defense at its home
- **Where its ratification is recorded:** the added text, and the same convention at CLAUDE.md at HEAD
- *Retrieve:* `git show 80ad92f9d3dae1d0d51a696e402734215529ac24 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `ARCHITECTURE.md` @ `-721,0 +722,12` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** A scoping annotation is added, its own opening "★ Scoping annotation (user ruling, 2026-08-02, at the OI-234 decision-conflict adjudication — reading 3)". It scopes a standing finding to what it tested and states what it does not bear on; the ground given is the adjudication, not a reading of the code.
- **The act:** the OI-234 decision-conflict adjudication, reading 3
- **Where its ratification is recorded:** the added annotation itself, at ARCHITECTURE.md at HEAD
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-01 · `ARCHITECTURE.md` @ `-956,0 +969,27` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The MuseScore-Dependency Rule is added, its own heading carrying "(user-ratified 2026-08-02, at the OI-241 adjudication)", and its closing paragraph states the derivation from the already-ratified scoped forms.
- **The act:** the MuseScore-Dependency Rule
- **Where its ratification is recorded:** the added section heading itself, at ARCHITECTURE.md at HEAD
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- ARCHITECTURE.md`

### 2026-08-01 · `CLAUDE.md` @ `-151,0 +152,15` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The change adds the decisions-register section with its rules (a)–(e). The section's own heading carries "(shape user-ratified 2026-07-28; content + living surface 2026-08-02)", and the commit's account records the register's 228 entries as user-ratified and the living surface as landing in this commit.
- **The act:** the decisions register ratified and made the living surface (its session-start read)
- **Where its ratification is recorded:** the section heading itself at CLAUDE.md at HEAD, and the ratification recorded in the register INDEX's preamble
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `CLAUDE.md` @ `-189 +204` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The change adds the session-start read count, two files becoming three. The section's own heading carries "(shape user-ratified 2026-07-28; content + living surface 2026-08-02)", and the commit's account records the register's 228 entries as user-ratified and the living surface as landing in this commit.
- **The act:** the decisions register ratified and made the living surface (its session-start read)
- **Where its ratification is recorded:** the section heading itself at CLAUDE.md at HEAD, and the ratification recorded in the register INDEX's preamble
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- CLAUDE.md`

### 2026-08-01 · `CLAUDE.md` @ `-192,0 +208,2` · a3f0a7f0e7

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`
- **Commit subject:** docs(cowork): the decisions register RATIFIED and made the LIVING SURFACE; OI-234/OI-241 ruled; the four-perspective review pass rowed (OI-243..OI-257)
- **Ground.** The change adds the decisions-register INDEX added to the session-start reads. The section's own heading carries "(shape user-ratified 2026-07-28; content + living surface 2026-08-02)", and the commit's account records the register's 228 entries as user-ratified and the living surface as landing in this commit.
- **The act:** the decisions register ratified and made the living surface (its session-start read)
- **Where its ratification is recorded:** the section heading itself at CLAUDE.md at HEAD, and the ratification recorded in the register INDEX's preamble
- *Retrieve:* `git show a3f0a7f0e7ee70d4f9b534b08278d5370a928ab4 --no-color -U0 -- CLAUDE.md`

### 2026-08-02 · `CLAUDE.md` @ `-826,0 +827,19` · b006dc15b5

- **Verdict:** RATIFIED-ACT-EDIT · shape `governing-decision-record`  ·  *added by the ruled cut*
- **Commit subject:** docs(cowork): the three-phase sequencing rule ratified (D-231): specification completion, then issue-exhaustion, then ONE fix plan - no fix design before
- **Ground.** The three-phase sequencing rule is added, its own opening "(user-directed, 2026-08-02; sharpens #8 …)". This is the boundary commit itself — the act the ruled period opens exclusive at — and the hunk that writes the instruction whose truth half the eighteenth stop's diagnosis names.
- **The act:** D-231, the three-phase sequencing rule (specification completion, issue-exhaustion, one fix plan)
- **Where its ratification is recorded:** the added text, and the same rule at CLAUDE.md Conventions at HEAD
- *Retrieve:* `git show b006dc15b5f696f2fc86ad72b97fae58d2119cd7 --no-color -U0 -- CLAUDE.md`

## What this screen does not do

No screened document is edited. Nothing is restored, reverted, reconciled or corrected. No open-items row is marked, flipped or discarded; no register entry is written. No fix, design or measurement of the analysis is authorized or performed. The period question is not re-opened here — the report says what would re-open it, and the act is the user's.

## The inherited establishment caveat (#19)

#19, INHERITED AND NOT DISCHARGED HERE. Every count below is a re-derivation over the two candidate artifacts, and the generator that produced those artifacts (`tools/audit/gen_doc_change_candidates.py`) has itself never been positively established — it was written in one batch, and its own artifact marks assumption A3 UNESTABLISHED for every generator family. What THIS tool establishes is that the split follows from those artifacts and reconciles with the totals they publish of themselves. It establishes nothing about whether the enumeration underneath them is complete or correct, and a reader may not take a clean re-derivation here as evidence that it is. What would settle the inherited half is an establishment pass over that generator — an act named here and not started.
