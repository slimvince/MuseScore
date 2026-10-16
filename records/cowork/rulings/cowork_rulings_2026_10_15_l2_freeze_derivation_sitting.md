# Derivation — the L2 freeze question, 2026-10-15

> **STATUS: RECORD OF A DERIVATION. NO RULING WAS TAKEN.** Cowork, 2026-10-15 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ten.md`. Entry 410 §3 item 1 orders this side to check
> first whether the record settles the question, and to record it as a derivation if it does. An interim carrier under
> the standing clause that a sitting record lands in git at the next dispatch's Task 0. **No act of this sitting is a
> commit to git.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read
> `a01e9402fbaf034fe0d357214b67c06a8294309c`, read as files with the file tools over staged copies. **The user may
> overrule this derivation; if he does, the question goes to him on a surface.**

## 0. The question

L2's deriving session has run, so its boot pack is spent and must be frozen before L3's pack is built (Ruling 1 of
`cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, its *"Noted, not ruled"* paragraph: *"L2's pack must be frozen
before L3's is built. Housekeeping under the user's rule of 2026-09-22; not a question for the user."*). The first-half
batch stopped at its Task 1 (`records/cc/reports/cc_report_l3_pack_build_first_half_2026_10_15.md` §5): in
`tools/audit/gen_derivation_boot_pack.py`, `build_subject` uses *"is in `FROZEN`"* to decide two other things as well —
which fields the cross-reference rule searches (`XREF_FIELDS_FROZEN`, five fields, against `XREF_FIELDS`, three), and
whether the extras' leak check (limb B) runs (`extras_leaks` is `None` for a frozen subject) — and the wording of the
additions block's `★_what_these_are` follows the same test. All three were written for the three packs frozen so far,
which were rendered before the rulings that introduced the three-field search (2026-09-27) and limb B (2026-09-21).
L2's pack was rendered under both. So adding `l2` to `FROZEN` as the generator stands would re-derive L2's withheld set
under the five-field search and drop its extras leak list, and the manifest's record of what L2's session was given
would state a withheld set and a leak list its pack never carried. **The question: is the repair the user's to decide,
or does the record settle it?**

**Checked at the code by this sitting:** the comment block and the two field tuples (the lines beginning
`# ── the fields the cross-reference rule searches`), the call `cross_reference_additions(…, XREF_FIELDS_FROZEN if
subject in FROZEN else XREF_FIELDS)`, the limb-B comment and the line `extras_leaks: list[dict] | None = None if subject
in FROZEN else []`, the `★_what_these_are` switch, the `FROZEN` table (three subjects), `build()`, `frozen_block`,
`frozen_from_disk` and `write_all`. **Relayed, not checked:** that the committed manifest's `l2` additions equal the
three-field derivation exactly, and the in-memory simulation's result — both from the report §5.

## 1. What the record says

1. **The ruling the scoping executes, quoted whole at its scope (D-643)** — Ruling 1 of
   `cowork_rulings_2026_09_27_l2_leak_list_sitting.md`: the rule searches `title`, `verbatim` and `plain` only *"for
   every subject that is not FROZEN."* Its own scope note, added at the source-check of the execution: *"The tool
   builds every subject in full, frozen or not, and keeps each frozen subject's manifest record as the record of what
   its session was given; … An unscoped change would rewrite that record. The tool's own limb-B check is already
   scoped to subjects not FROZEN, on D-657, and this takes the same shape; the frozen subjects keep the five-field
   search, prose included."* **The stated purpose of the scope is that no spent subject's record is rewritten.** When
   it was written, "not FROZEN" and "built under this rule" named the same subjects.
2. **The generator's own grounds for the two branches.** For the fields: *"A FROZEN subject keeps the five-field
   search its pack was built under, so that its manifest record — the record of what its session was given — does not
   move."* For limb B: *"a frozen subject's record describes a directory rendered before this check existed
   (D-657)."* Both are false of `l2`.
3. **D-646** (`cowork_audit_protocol.md`): a generated record that must outlive its writer is frozen so that it does
   not move. Freezing `l2` as the generator stands would move it.
4. **D-669**: the cause is established at the objects before the mechanism is touched. Done — at the code by the
   first-half batch and again by this sitting (§0).
5. **D-657**: a mechanism change is decided over its whole population both ways, and only the members the defect's own
   shape names may move; any other movement is a STOP back to the user. This sets what the repair's evidence must look
   like. It does not by itself make the repair a question.
6. **The user's rule of 2026-09-22** **[relayed — from his saved working preferences; no repository object carrying
   it was located this sitting]**: *"Staleness and other apparent 'errors' should be fixed, no need to ask for
   permission in those cases"* — not extending to a verdict, a measured value or a finding. The repair moves none of
   those; its purpose is to stop one moving.
7. **The condition the user attached to Ruling 1 of 2026-09-27**: *"B under the condition we are NOT spending time on
   apparatus that has NO bearing on ultimate objective"*.

## 2. The derivation

**The record settles it.** The ruled rule is that every spent subject keeps the record of what its session was given,
and that a subject is searched and leak-checked under the shape its pack was built under. The generator implements
"built before the 2026-09-21 and 2026-09-27 rulings" by "is in `FROZEN`", which was exact for three subjects and is
wrong for the fourth. Repairing the test so that it names what it was written to name applies Ruling 1 of 2026-09-27
as ruled, to a subject its proxy no longer describes. It changes no rule by which a withheld set is derived, no verdict,
no measured value and no finding: read at the code, the three subjects already frozen and every live subject keep
the field set and limb-B behaviour they have today, and the one subject whose behaviour changes is `l2`, whose record
then does not move (to be proved by the evidence below, not assumed). Under point 6 it is fixed
without asking, and under point 7 it should not grow into a surface.

**The repair, as the second-half dispatch must carry it.** The three tests on `subject in FROZEN` named in §0 — the
field choice, limb B, and the `★_what_these_are` wording — are keyed instead on an authored statement of which
subjects' packs were rendered before those rulings: `harmony-boundary`, `scoring-model` and `l0-l1`, each with its
finding, date and reason. `l2` then freezes with the three-field search and limb B, as it was built. The hash STOP, the
`frozen_from_disk` re-pointing and `write_all`'s refusal to write a frozen directory are untouched.

**The evidence it owes (D-657), and the STOP.** Before and after the change, every subject's manifest record is
compared, the before half read from the committed manifest at an explicit hash. **The three subjects already frozen
must not move at all. `l2` may move only by gaining its `★_FROZEN` block and the re-pointing `frozen_from_disk`
performs.** Any other movement is a STOP back to the user, with nothing committed.

**A risk named in advance, so it is not a surprise (#13).** A frozen subject is still built from today's sources, and
`frozen_from_disk` re-points member sizes at the directory but not the extras' leak list. L2's extras include the
charter member, whose source (`FRAMEWORK.md` §5) has changed since L2's pack was rendered (Ruling 1 of the L3 boot-list
record). If today's re-render of an extra carries a different leak hit from the one the user ruled on, L2's
`LEAKS_IN_THE_EXTRAS` moves, and the STOP above fires. Whether it does is unmeasured; the dispatch measures it.

**Bound, stated so the derivation is not read as wider than it is.** This side reads the repair as keeping a ruled
scope true, not as a new mechanism. If the user reads it as a mechanism change under the reservation D-436 and D-657
keep for him, it is his, and he says so.

## 3. Documentation or algorithm

This concerns what the record of a spent session's reading says. **It amends no specification and changes no
algorithm of the analysis.** The currently decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I (*"split —
cues at L1, type at L3"*), as the boot-list record states it (not re-read at `FRAMEWORK.md` by this sitting).

## What this record does NOT do

It edits no tool, renders no pack, writes no dispatch, takes no ruling and allocates **no decisions-register identity**
— the register cannot accept one while `cowork_register_rule_c_suspension_2026_08_28.md` is the route.

*Provenance: Cowork, 2026-10-15 (Stockholm), the sitting booted on entry 410. The user's words: the opening
instruction.*
