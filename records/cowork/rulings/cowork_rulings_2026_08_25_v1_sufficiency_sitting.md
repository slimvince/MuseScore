# Ruling record — 2026-08-25, the v1-sufficiency sitting

Written in the turn its rulings were given (standing clause). Untracked at the repository root;
lands at the next dispatch's Task 0. The tip was unmoved throughout: `0f18b358bc6a8da5ec6064760d675129e64d8f3b`.
Nothing was committed, regenerated, swept or rowed by this sitting.

This record is deliberately short. The user flagged, for the second sitting running, that the work
is borderline too meta; a long record about a ruling that reduces the apparatus would contradict
its own content.

---

## Ruling 1 — the derivation method is ruled USABLE for v1, on the user's ground, not on the held-out test

**The user's words: "yes".**

The ground is his, put in his own framing across the sitting: a first version of a specification
cannot be the ultimate one, because the sources are not exhausted until the audit against the code
has run. What v1 can be is the best derivable from everything already held except the code, plus
added research. Deriving it that way is therefore good enough by construction — and it improves on
the current text on provenance alone, since the current text is partly code-derived and that is the
defect the phases exist to repair.

This discharges the pilot's postcondition at §3.2 of the phase-definition surface — *"the method is
ruled usable, amended, or refuted by the user on evidence"* — by the first of its three limbs.

**What it replaces.** The method's VOIDED status — untested, neither established nor refuted — is
superseded. The verdict now rests on a different ground from the one the held-out test was built to
supply, so the contamination that voided the earlier verdict does not reach it.

## Ruling 2 — independence is evidenced by the ten DIFFERS rows

The held-out test was a proxy for a narrower worry than "will v1 be good": whether a deriving session
is genuinely independent of the code, or quietly re-imports its assumptions the way the previous
generation of specifications did.

Ten of the blind output's twenty-six statements differ from the shipped code
(`ratification_surfaces/cowork_comparison_harmony_boundary_reading.md` §6, current-text axis: 15
AGREES / 10 DIFFERS / 1 SILENT). A session covertly reading the implementation does not produce ten
disagreements with it. That evidence needs no oracle, is inspectable at the file, and is untouched by
the contamination.

**Not claimed:** that the ten are substantive. Whether they are real discrepancies worth having is
open and was offered as a first pass this sitting; it was not taken up.

## Ruling 3 — the framework and detail-specification phases are no longer HELD, and E and C are not the next act

Both phases were held on the pilot's method verdict. Ruling 1 supplies it, so the hold lapses.

**What it replaces.** Ruling 3 of `cowork_rulings_2026_08_25_regress_termination_sitting.md` — *E
first, then C with B running alongside* — is superseded as the ordering. E (the user's judgement of
the existing derivation against the oracle) and C (the re-run of the held-out test) are not the next
act and are not owed. **B is untouched:** the empirical findings ledger remains owed before the
framework phase, exactly as it stood.

The user's ground for setting E and C aside, recorded because it is the load-bearing part: the
held-out test's pass condition — reproduces the ruled intent, or a defended alternative the user
would rank beside it — tests whether the output lands near a judgement he already made. It does not
test design quality, and a method could pass it while producing poor engineering.

---

## Recorded beside the rulings, ordering nothing

**Salvage share.** Nineteen of the twenty-six statements lean at least partly on design-intent
entries the user had already ruled; seven stand free of them (same file, §6, the salvage line — each
row names its own identifiers). This bears on what the method costs at full width, not on whether it
is usable. It is a count read off that file, not a re-derivation.

**The pilot's remaining open half is sizing** — time per statement, differences per document, share
needing a user ruling (§3.2 outputs). It needs neither E nor C. It is the pilot's only unfinished
business.

**Coverage bound, restated.** The oracle reached eight of twenty-six rows. That thinness was among
the grounds for not spending further on E.

---

## Declared by the writing side

**Reads taken.** `ARCHITECTURE.md` at lines 378–409 only — the evidence-ranking ruling — read in
order to explain it to the user at his request. **This makes this side oracle-aware for the
harmony-boundary unit.** Neither blind output was opened at any point, and this side neither judged
nor compared either. Also read: this repository's handoff at its sixty-fifth and sixty-fourth entries
whole and the sixty-third at its opening; the comparison reading at §1, §2.1–2.2, Rows 11, 12, 16, 17,
18 and §6; the phase-definition surface at §0 (referents), §2, §3.2–3.4; the 2026-08-21 successor-plan
record at Ruling 4.

**Not read.** The session-start read was not taken. `CLAUDE.md`, `STATUS.md`, `DECISIONS.md`,
`BUILD_AND_TEST.md` not opened. `decisions/group_S.md` not opened.

**Memory filesystem.** Not read before the rulings were given. `/preferences.md` was read after them
and one line appended — the user's standing "too meta" bar. No repository content was written to it.

**Method of measurement.** The tip and `origin/master` read from `.git/HEAD`,
`.git/refs/heads/master` and `.git/refs/remotes/origin/master` with the file tools on the user's
machine; no shell command was run on the repository and `git status` was never at risk. On-disk sizes
of the eleven files the sixty-fifth entry names taken by staging each path — a narrower route than the
root listing that defeated the previous two sittings, which still exceeds the bridge tool's output cap.
**No hashes and no carriage-return counts were taken**; that part of the ordered start-state
measurement still stands undone.

**Relayed, not re-measured.** Every figure quoted from the comparison reading is read off that file
and not verified at the blind output, which this side may not open. The four tracked modifications are
taken as the sixty-fifth entry states them.

**Errors this sitting — three, all caught by the user.** (1) The two positions at Row 18 were put on
mismatched axes — "content" set against an evidence ranking without saying that content *is* the
ranking's top class — so they could not be read side by side; he caught it by asking what "content"
was. (2) "We are not trying to find the best inference method" was confirmed to him when the ultimate
objective is *maximum-precision harmonic inference* and every proposal is rated towards it; corrected
in the next turn. (3) He was pointed at the raw derivation and the raw ruling for three turns without
being told that the row-by-row comparison already existed and was committed. A fourth, his, not mine
to count: he believed this side had read the blind output; it had not, and said so.
