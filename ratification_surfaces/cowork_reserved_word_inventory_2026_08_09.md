# The reserved-word inventory — what the DERIVATION says about the twenty, and what the user is being asked to rule in batches

> **★ STATUS: AWAITING THE USER — an ADVISORY reading surface. NOTHING IS RENAMED, nothing is
> proposed for renaming, and no check is adopted.** Written 2026-08-09 (CC,
> `cc_instruction_return_continuation_5.md` Task 2) on the user's **Ruling 31** of
> `cowork_rulings_2026_08_09_fifth_stop.md`, which licensed the scanner, and **Ruling 30**, which
> fixes what happens with its output: **no tree-wide rename** — the inventory first, then the user
> rules per-word batches, governing surfaces first.
>
> **Every value in this file lives in `tools/audit/reserved_word_scanner.json` and none is
> transcribed here (D-431).** What is written here is the SHAPE of the result and the decision it
> puts to the user.
>
> **Nothing here authorizes a fix to the analysis, a design, or an inference change.**

---

## 1. The question this answers, in the user's own terms

The user asked **how the twenty-word collision inventory's completeness is known.** Ruling 31's
answer: *it is not, and it becomes checkable by derivation.* This file reports what the derivation
found.

**The derivation, in one sentence.** A candidate is a word that is both **(a)** in the project's own
musical vocabulary — extracted from its own domain surfaces — and **(b)** used by the project's
governance surfaces, whose subject is not music. The twenty words are the **seed verdicts**, not the
population.

---

## 2. What was measured, and both derivations are reported because neither is sufficient alone

Two readings of *(a)* were computed, and the comparison is the finding rather than a detail.

- **The SHARP surface** — every `enum` in the analysis code, its name and its enumerators, crossed
  with the two music-theory documents. An enumeration is where a program writes down the categories
  its domain actually has, so for this module those are the chord qualities, the modes, the degrees,
  the cadence kinds and the interval classes.
- **The BROAD surface** — every word inside any identifier in the analysis code, crossed with the
  same documents.

**★ THE RESULT IS THAT NEITHER IS BOTH SOUND AND BOUNDED, AND THAT IS REPORTED RATHER THAN TUNED.**

- **The SHARP derivation is not SOUND: it misses seed words the user's own inventory names**, and
  one of them is a collision this project's standing self-check has actually caught in its own prose
  more than once. A derivation that misses a known positive cannot be trusted to have found the
  unknown ones.
- **The BROAD derivation is not BOUNDED**: it proposes a population an order of magnitude larger,
  dominated by ordinary English that happens to appear on both surfaces. It reaches all but one of
  the seed words and buys that with a population no session can rule on.

**Both lists — reached, missed by the sharp one, missed by both — are enumerated in the artifact.**
The one word missed by BOTH is the sharpest single result in the file: it is a collision the user
recorded which **no** in-repo derivation proposes, so the record is not a subset of the derivation
either.

---

## 3. What that means for the completeness question — stated plainly

1. **The inventory of twenty is NOT complete** relative to either derivation. Both propose many
   words it does not carry.
2. **The derivation is NOT complete either**, relative to the record. It misses words the user
   listed.
3. So the honest statement is the one Ruling 31 already makes: *"complete" means complete relative
   to a NAMED derivation, re-derived as the tree grows* — and **this derivation's name now includes
   its measured miss rate against the seed**, which is what makes the claim checkable instead of
   asserted.

**★ AND THE EXTERNAL LEG IS ABSENT, WHICH IS SAID RATHER THAN WORKED AROUND.** Ruling 31 admits an
external music glossary as an optional second source. None is used: this repository vendors no
music-theory glossary, and importing one would put an unestablished list under load (#19). **The
consequence:** a musical word this project never writes in its own code or specifications is outside
the derived population. That is the most likely cause of the seed words the derivation misses, and
it is a hypothesis rather than a finding — it is not asserted here.

---

## 4. Why NO check is adopted, and why that is the result rather than a shortfall

Ruling 31 permits adoption as a diff-time check on new text **ONLY on measured clean separation**.

**There is no separation to measure at the level a check would fire.** The population says which
WORDS deserve a ruling; it does not say which USE of a word is the non-musical sense — and that is
the semantic judgment **Ruling 32** closed the neighbouring limb over. A diff-time check built on
this population would fire on every legitimate musical use of every word in it, which is exactly the
mis-firing **D-473** refuses and **D-436**'s third condition measures.

**Nothing was tuned to make the measurement look better.** Narrowing the population until it stopped
firing would be fitting the signal to the cases that motivated it, which is the defect the catalog
names DT-2 — the same trap the previous continuation's consistency check reported rather than
adjusted.

---

## 5. What the user is being asked

**Nothing is urgent and nothing is blocked.** The convention is already LIVE for new writing, and
the standing self-check keeps catching collisions in each wave's own prose — four consecutive waves
have now done so, which is evidence the rule works and that the collisions arrive by matching the
surrounding prose's idiom.

**The decision this file puts, in Ruling 30's own order:**

1. **Is the derivation worth authoring verdicts over at all**, given that it is neither sound nor
   bounded? Authoring a verdict per candidate — collision, non-collision-with-reason, or structural
   case — is **a named act of its own** over a population the artifact counts, and it is not a step
   inside another task. It is not started here.
2. **If yes, which batch first?** Ruling 30 fixes the order — governing surfaces first
   (`CLAUDE.md`, `ARCHITECTURE.md`, the signed specifications), with code identifiers and
   research-tied names each a named later decision.
3. **A third reading is available and is stated because it may be the cheapest right answer:**
   leave the inventory as the user's twenty, keep the convention live for new writing, and let the
   per-wave self-check go on catching collisions — recording that the completeness question has been
   ANSWERED (it is not complete, and here is by how much) rather than closed. The scanner then
   stands as the evidence for that answer and is run again when the tree has grown.

**Ruling 30's two-tier test for research-tied names is recorded in the artifact and is NOT applied
here.** Deciding which candidates are research-tied, and which site is a term's introduction site, is
authorship of the same kind as the per-candidate verdicts.

---

## 6. What this file and its tool do NOT do

They rename nothing and propose no rename. They adopt no guard. They move no status, home nothing and
authorize nothing. They touch no `src/`, no golden, no corpus of scores and nothing in
`tools/robust_stop/`. The scanner is registered in the guard population as **NOT RUN**, with the
reason stated there: its STOP is its headline rather than a failure, and a guard set carrying a
member that fails by design teaches a reader to ignore the set.

**Phase 1's completion statement is not written, not drafted and not partially written here.**

---

*Provenance: the user's Rulings 30 and 31 of 2026-08-09
(`cowork_rulings_2026_08_09_fifth_stop.md`), applied at
`cc_instruction_return_continuation_5.md` Task 2. The tracking row is `OPEN_ITEMS.md` OI-229, which
carries the rulings' disposition and stays OPEN. The tool and every value are at
`tools/audit/gen_reserved_word_scanner.py` and `tools/audit/reserved_word_scanner.json`.*
