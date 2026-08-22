# Rulings — the boot-list sitting for derivation sessions, 2026-08-22

> **STATUS: RULING RECORD.** Cowork, 2026-08-22 (the forty-second Cowork session). An interim carrier
> under the standing clause that a sitting record is written in the turn its ruling is given and
> lands in git at the next dispatch's Task 0.
>
> **Taken at branch tip `40fb613060`** (parent `d276e8afb2`; `refs/heads/master` and
> `refs/remotes/origin/master` both at the tip), read by this session with `git show -s` and
> `git for-each-ref` at the explicit hash on the user's machine at boot. The object ruled on is
> `cowork_curated_boot_list_draft_2026_08_19.md` (tracked at the tip; 11,298 bytes at staging),
> read whole through the file tools from a bridge-staged snapshot. No document ruled here is
> generated.

---

## 0. What was put, and in what form

One decision, put self-contained as the turn's final response with no question in it — the
referents re-explained from scratch, the draft's content, three facts that arose after the draft
was written (one of them a contradiction measured at git objects), four alternatives each rated
towards the ultimate objective and towards the guiding principles, and this session's
recommendation. The choice question was put in the following turn. The user ruled with the
alternative's letter.

The surface was put first in an ORDER this session stated and the user directed by the ultimate
objective ("take them in the order that best meets the ultimate objective of best possible
inference"): the boot-list ruling first, because the pilot may not open without it and a session
may not rule it; the per-entry pass continued on the coding side in parallel under Ruling 1 of the
dispatch-order sitting, which needs no new ruling; the pilot's opening second; the routing of the
four quarantined findings and the two unrowed dispositions third; the pruning-and-satellites
surface last.

## 1. Ruling 1 — the curated boot list for derivation sessions is the 2026-08-19 draft's six members and eight exclusions, RATIFIED with three amendments forced by the 2026-08-21 rulings (Alternative A; the user's word: "A")

**The question ruled.** The curated boot list — the implementation-free read list an
implementation-blind session boots from, ruled on 2026-08-17 (§4 of the session-start-read
sitting) to be "DRAFTED and RULED before any derivation session boots from it" — was drafted on
2026-08-19 and ruled on 2026-08-21 for the two plan evaluations only. Its ruling for derivation
sessions was the pilot's one stated hard prerequisite and was still owed (plan §6.1; Ruling 1 of
`cowork_rulings_2026_08_22_dispatch_order_sitting.md`).

**Ruled.** The draft's six members — (1) the phase definitions surface
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3 whole; (2) `CLAUDE.md` at
two spans named by heading anchor, the guiding principles through the delegation pointer and the
conventions through the self-check; (3) `cowork_design_doc_template.md` whole; (4) the
dispatch-protocol section of `cowork_audit_protocol.md`; (5) the `DESIGN-INTENT` class of
`tools/audit/rulings_sort_classification.json`; (6) `DEFECT_TYPES.md` — and its eight exclusions
(the rest of `CLAUDE.md`; `DECISIONS.md` and its group files; `STATUS.md`; `ARCHITECTURE.md`;
`docs/scoring_model.md`; the open-items register and the derived gating answer; the handoff,
dispatches and coding-side reports; `BUILD_AND_TEST.md`) are the STANDING boot list for derivation
sessions, with these three amendments:

**(a1) A per-session WITHHELD LIST, generated, never hand-cut.** A dispatch for a session that runs
the held-out test (Ruling 4 of 2026-08-21) names the withheld register identities as an AUTHORED
INPUT carrying finding, date and reason — the same shape as an authored exclusion (D-677; the
`STATUS.md` exclusion of `gen_specification_document_set.py`). A generator cuts member (5) to the
`DESIGN-INTENT` class LESS those identities, derives and adds every entry of the class that quotes
or cross-references the withheld oracle's home lines, STOPs on a named identity that is not in the
class, and publishes the cut artifact; the session boots from that artifact and never from the
whole sort. For the ruled oracle of the held-out test the first withheld identity is **D-057**
("the priority of evidence — actual sounding notes are the strongest evidence"). The ten-factor
model `cowork_joint_estimator_factorization.md` is recorded as ORACLE material for the pilot
(Ruling 4's second arm), not a boot member; Ruling 2's admission of it is to the FRAMEWORK phase's
source list and reaches no pilot session.

**(a2) The ledger hole is carried exactly as Ruling 8 of 2026-08-21 declares it** — the pilot opens
without the empirical findings ledger, the admission test applied by hand, each admitted fact
recorded in the ledger's entry shape, the hole declared in the session's source declaration. The
draft's §4 choice is taken by that ruling and is not re-opened here.

**(a3) `DEFECT_TYPES.md` is admitted at its TYPE and DEFINITION columns only**; its founding-instance
and signature columns are excluded, on the Cowork evaluator's finding of 2026-08-21 (plan §5) that
they are implementation descriptions. *Taken in the split form the recommendation named. The
surface offered the whole-file-with-declaration form as the other reading of (a3); the user's
word was the alternative's letter, and this record takes the recommended form — if the user
intended the whole-file form, one word corrects it here.*

**The fact that forced (a1), measured at git objects by explicit hash.** Ruling 4 names as the
held-out test's oracle "the evidence-ranking ruling of 2026-08-11 (`ARCHITECTURE.md:394-402`)".
At `git show 40fb613060:ARCHITECTURE.md` those lines state the four-rank ordering and say in terms
that "the legacy statement of the same ranking is §5.2's priority-of-evidence table (register entry
D-057)". At `git show 40fb613060:tools/audit/rulings_sort_classification.json` the entry `D-057`
carries `proposed_class: DESIGN-INTENT`, decided by `home_is_layer_spec: true`. So a held-out
session booting from member (5) as drafted would read the oracle it must be blind to, and the test
that positively establishes the method (#19) would be void. The draft is not in error on its own
terms — it predates the held-out test — and is amended, not rewritten (#12).

**The alternatives declined.** B — ratify as drafted and withhold by instruction in the dispatch:
declined because a session told not to read one entry of a file it reads cannot prove it did not;
independence asserted, not measured (#19). C — re-draft whole before ruling: declined on cost; its
content is A's. D — defer and let the pilot dispatch declare a one-off list: declined as
contradicting the ruled definition and as a session ruling the prerequisite by itself, the ground
of yesterday's Ruling 1.

**What this ruling does NOT do.** It opens no session and writes no dispatch. No finding number is
allocated; the series stands at F88. No open-items row is created, flipped or discarded;
[[OI-179]] stays OPEN and GATES. No register entry is written or moved; D-057 is unchanged. The
ordinary session-start read is untouched (Ruling 4 of 2026-08-17 in terms). The membership stays
AUTHORED, as the draft's own §6 states, and is not claimed complete. The generator of (a1) is
dispatched with the pilot's opening, not before, and is the one mechanism this ruling adds —
stated so guardrail 3 is not breached silently. The pilot's opening is the NEXT surface owed.

---

*Provenance: Cowork, 2026-08-22, the forty-second session, at tip `40fb613060`. Every governing
document read from a bridge-staged snapshot with the file tools; the object reads named above were
taken with `git show <hash>:path` on the user's machine; the declared tells of this session are
recorded in the forty-second handover block. The user's word: "A".*
