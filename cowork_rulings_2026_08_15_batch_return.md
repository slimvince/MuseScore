# User rulings — 2026-08-15 (the batch return): the class-1 follow-up, the [[OI-373]] clearing act, the second ignore rule removed, and the guard-staleness fix

> **STATUS: RULING RECORD, an interim carrier (D-230).** Taken by the user in conversation on
> 2026-08-15, at the return of the batch `cc_instruction_ruled_inventory_landing.md`, whose report
> and full close were read whole and verified at the objects by explicit hash before any decision
> was put. Each decision was presented as a self-contained visible surface — restated from scratch
> on the user's correction that identifiers must never be assumed remembered — with alternatives,
> costs, and a recommendation. **The user's ruling, verbatim: "I agree on all recommendations."**
> Each section below states the recommendation adopted whole; the operationalizations are the
> writing side's, accepted in sequence. **The classification of each ruling — decision or
> exercise — is OWED and not made here**, and no decisions-register entry is written (the
> eighteenth stop's filtering ruling stands).
>
> The executing dispatch for the acts ordered below is `cc_instruction_batch_return_rulings.md`.
> §1 orders no act of the coding side; it is record only.

## 1. Ruling — the class-1 follow-up: the twenty specification-derived tests (Alternative B)

The condition the user attached to class 1 (`our-analysis-tests-and-fixtures`) at the inventory
sitting — *"IFF the regression test were constructed based solely on code and not at all on
specs"* — was checked by the returned batch and does not hold for 20 of the 123 members (the
artifact is `tools/audit/test_construction_evidence.json`; the finding is
`cc_report_ruled_inventory_landing.md` §1; per D-431 no count is restated beyond what this
section reports about). **RULED:**

- **All 123 members remain EXCLUDED from the implementation-blind redesign** — the wall of the
  class-1 Alternative A verdict, unchanged. The design intent the 20 carry is not lost by the
  exclusion: what they derive from is specification text the redesign already meets as an
  untrusted witness; a test adds no independent design source.
- **The 20 SPEC-DERIVED-EVIDENCE members are RECORDED as audit material of a sharper kind:**
  each names the specification section its expectations came from, so each is a ready-made
  three-way comparison point — specification versus test versus code — for the audit phase.
- **The two members whose evidence sits only in a commit subject keep the weaker-evidence
  marking exactly as the artifact records it.** A commit subject describes the commit, not one
  file inside it; the two cases stay distinguishable without re-derivation.
- **With this follow-up, class 1's conditional verdict CARRIES LOAD** — the condition of the
  inventory-sitting record §3.1 is discharged. The catalogs returned CODE-BUILT on both sides of
  their split and stay where the class-1 verdict put them.
- No file is edited, moved or run under this ruling. The write-back of ruled verdicts onto the
  generated surface remains the later act it already was.

## 2. Ruling — the [[OI-373]] clearing act is permitted (the coherent one-act version)

The returned batch discharged the substance of open-items row [[OI-373]] (the two run-instructions
authored, the runner's STOP cleared) and correctly STOPPED on the ordered row flip:
`tools/audit/gen_discard_records.py` carries an authored discard pointer for that row and refuses
on any entered row resolved at the INDEX, so the flip alone would have left two standing reds
against the inventory sitting's own stated outcome. **RULED — a ruling permitting a named act,
under D-436, for this act alone:**

- **In ONE act:** the authored discard pointer for [[OI-373]] is RETIRED from the tool's
  authored table WHOLE — moved into a retired block (added if the mechanism does not yet carry
  one), with the reason it leaves, the date, and the retiring dispatch's name; **nothing is
  destroyed (#12)** — AND [[OI-373]]'s INDEX row is flipped RESOLVED with provenance, its detail
  file gaining the dated remark and never a status.
- The refusal logic that caught the incoherence is not otherwise changed.
- **After the act the standing reds are ONE — [[OI-372]]** — the outcome the inventory sitting's
  §5 stated.

## 3. Ruling — the second ignore rule is removed

The ruled removal of `.gitignore`'s `/cc_*.md` line was performed exactly, but the NARROWER rule
`/cc_instruction_*.md` two lines above survives, so every dispatch written from now on would stay
silently outside version control — the rule-versus-practice disagreement the inventory sitting's
§1 set out to end, surviving in smaller form (the finding is
`cc_report_ruled_inventory_landing.md` §3). **RULED:**

- **The line `/cc_instruction_*.md` is REMOVED from `.gitignore`**, on §1's own ground: ending
  the disagreement in the direction that keeps records. **No other line moves** — `/cc_e2d_*.md`
  and `ai-assistant/CC_INSTRUCTION_*.md` are NOT ruled on.
- **Declared consequence, accepted:** previously ignored instruction files on disk become
  visible as untracked. **Landing them is NOT ruled** — they ride their classes' verdicts and
  the caller-check sequence, exactly as the remaining ignored files do.

## 4. Ruling — the guard-staleness fix, at the printing side

The returned batch diagnosed at the code why the committed `guard_state.json` reads stale at
every tree except the one it was generated at: `tools/audit/gen_artifact_inventory.py`'s live
half prints the current commit's short hash in a line the runner's normalization pattern does
not reach, so committing anything makes the artifact stale by construction — a check red
everywhere teaches a reader to ignore it (the diagnosis is `cc_report_ruled_inventory_landing.md`
§4.a). **RULED — a ruling permitting a named act, under D-436, for this act alone:**

- **`gen_artifact_inventory.py`'s live half changes WHAT IT PRINTS** so its commit-hash line
  carries the exact shape the runner's EXISTING normalization reaches — the pattern read at
  `gen_guard_state.py` before the edit, never assumed.
- **The runner's normalization is NOT widened.** The fix is the smaller edit, on the printing
  side only.

## 5. Recorded note — decision surfaces re-explain their subjects (user-directed, this exchange; not a ruling on any act)

The user, verbatim: *"Do you still believe I remember what class-1 was or what OI-373 is, or
§4.a is? Rewrite decision as decided."* Standing form from this date: **every decision surface is
self-contained** — each identifier's referent re-explained from scratch in plain terms before its
question is put. This joins the presentation rules already in force (full visible prose,
alternatives with costs named to principles, no option widgets) and the session-length record's
tells.

## 6. What is NOT ruled or done, and must not be assumed

- **No phase definition, no repair, no specification derived** — the eighteenth stop's §3 stands
  whole. The phase-definition surface is the next writing-side act AFTER the executing dispatch
  returns and is verified.
- **The remaining previously-ignored files are NOT landed.** The caller-check at the objects is
  NOT started. **The ruled verdicts are NOT yet written back onto the generated surface** — the
  ruling records remain the carrier.
- The register filter has not run. The findings ledger does not exist. The curated boot list for
  redesign sessions is not ruled.
- **[[OI-372]] is untouched.** [[OI-179]] stays OPEN and GATES. D-231 and #8 stand. **No
  decisions-register entry is written** (the filtering ruling stands).

*Provenance: Cowork, 2026-08-15, recorded in the turns the rulings were given. The user's
verbatim words are marked as such throughout; everything else is the writing side's
operationalization, accepted in sequence. The returned batch's five commits were verified at the
objects by explicit hash before the decisions were put (path counts, the `.gitignore` diff, the
committed artifacts' own counted fields, the push state at `origin/master`); the full close was
read whole and the reading proved by quotation (eighteenth-stop Ruling 15).*
