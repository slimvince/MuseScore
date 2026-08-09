# The eleven uncovered legacy-marked entries — reachability and transfer verdicts, for the user's review

> **STATUS: AWAITING THE USER. THESE VERDICTS CLEAR NO GUARD**, and nothing here changes a mark, a
> status, a home or a register entry. Written 2026-08-09 (CC,
> `cc_instruction_return_continuation_3.md` Task 1) on the user's **Ruling 18 of 2026-08-09**
> (`cowork_rulings_2026_08_09_third_stop.md`): a session performs the owed establishment for every
> legacy-marked entry the verification's verdict table does not cover, **by the phase-1w pass's two
> axes and no invented method** (#6, #16), and the verdicts are **delivered as a ratification-surface
> reading file for the user's review**.
>
> **★ WHY THE GUARD IS STILL RED, DELIBERATELY.** [[OI-354]]'s objection was not that the work is
> hard — it was that verdicts authored to clear a guard are the weakest establishment there is.
> Ruling 18 answers it structurally rather than waiving it: **nothing self-ratifies (#14)**, these
> verdicts are not written into the tool, the standing failure of
> `gen_phase1w_legacy_verification.py --check` is **carried**, and it clears only when the reviewed
> set is applied — in a commit that cites the user's ruling on the registration queue. **A verdict
> the user disagrees with costs one line here**, because nothing has been written that would have to
> be unwritten.
>
> **[[OI-289]]'s VERIFIED status is not withdrawn and is not in question.** It is true of the
> population it covered. What this file covers is the entries marked *since*.

---

## 1. The population, derived

**Eleven entries, derived at task start from the tool's own output** and not carried from any prose
(the dispatch's assumption A2). The tool derives the marked set from `backbone_decisions.json` —
every decision whose `legacy_subject` field is truthy — compares it against its own authored verdict
table, and names what it holds no verdict for:

**D-536, D-537, D-538, D-564, D-568, D-571, D-572, D-575, D-579, D-580, D-583.**

**Checked rather than assumed:** the committed verification artifact
`tools/audit/decisions/phase1w_legacy_verification.json` mentions none of them. No count from any
artifact is restated here (**D-431**).

## 2. The method — the phase-1w pass's own, read before the first verdict

The dispatch's assumption **A1 is DISCHARGED**: the method is stated in the pass's own record, in
full, and is reusable as stated. Nothing was invented and nothing was substituted; where a case
needed a judgment the pass had already faced, the pass's own precedent for that case is named at the
entry.

**Half A — reachability.** *"Is the entry's subject reachable on EITHER production surface at HEAD?
Because the notation arm turns on a runtime flag whose default is true rather than on compilation, a
bare 'dormant' is not an answer: each verdict names WHICH SENSE it means."* The five senses are the
pass's: **production**, **false-negative-path**, **flag-default-only**, **none**, **undetermined**.
Every verdict cites **evidence anchors** — file, line and quote, which the tool locates on each run,
so the evidence cannot go stale silently.

**Half B — transfer.** *"Does any ruling carry the decision's PRINCIPLE across to the live design?
A mark correct about the subject can still be wrong about the effect."* Values:
**ruling-transferred**, **live-prohibition-in-spec**, **carried-elsewhere**, **assigns-live-work**,
**explicitly-not-transferred**, **none-found**, **undetermined**.

**The search, and the two bounds the pass states on it — carried here unchanged, because they bound
what a `none-found` verdict is worth.** Every occurrence of each entry's identifier was collected
across `.md` / `.cpp` / `.h` / `.py` / `.txt`, register-internal data files excluded, and the hits
outside the register's own mechanics were read. **(i) It finds a transfer only where the
transferring ruling NAMES THE ENTRY** — a ruling that carries a principle without citing the
decision is invisible to it. **(ii) No marked identifier is cited anywhere under `src/`**, so no
verdict rests on a code comment. For these eleven, every hit outside the register's own mechanics
was a homing act, a ratification list or a filing classification — **with one exception, which is
the only live-specification citation in the set and is recorded at D-572.**

## 3. The verdicts

| # | Subject, in one line | Reachability | Anchors | Transfer | Ground |
|---|---|---|---|---|---|
| **D-536** | The bass and the chord chosen TOGETHER as one (bass, root, template) triple | **false-negative-path** | `NOTE_SEAM_LEGACY`, `BATCH_LEGACY_DEFAULT`, `TESTS_CHORD` | **carried-elsewhere** | The legacy chord scorer, reached by plain `batch_analyze` and the composing test suite and sitting below the record return on the note seam. Transfer is the record's own statement, in this entry's home text AND its provenance: the principle it embodies — *deciding coupled quantities together rather than committing one early* — is **the same one D-001 carries for the live design** (*"Key, mode and chord are inferred by ONE joint decode"*). The MECHANISM is legacy; the doctrine is live and named |
| **D-537** | The completeness bonus fires only for a root-position reading — the guard against demoting genuine slash chords | **false-negative-path** | `NOTE_SEAM_LEGACY`, `BATCH_LEGACY_DEFAULT`, `TESTS_CHORD` | **carried-elsewhere** | Same arm as D-536. The home text states the kinship in its own words: it is *"an early instance of the standing rule that a correction is given a **structural entry condition** rather than a widened threshold (`CLAUDE.md`, the gate and preset policy)"* — which is live and binds now. **Stated precisely so it is not over-credited:** what is carried is the general rule, not this guard; the guard itself is legacy code |
| **D-538** | A multi-signal change lands one signal at a time, the corpus re-run after each, any rise a hard stop | **none** | *(none — see the ground)* | **carried-elsewhere** | **Reach `none` on the pass's own D-302 precedent** (*"a closure of a line of work, not a mechanism; nothing implements it"*): the subject is a LANDING PROCEDURE for one past change, so there is no code at HEAD to reach at any setting, and **no code anchor can bear on it** — which is why the anchor list is empty rather than padded with an anchor that would not be evidence for the verdict. Transfer is the clearest in the set and is already RULED: the user ruled this entry's content superseded by **D-177** (#14, one revertible provenance-stamped commit per behaviour change) and **D-115** (gate block (A)'s measured non-increase), both homed in `CLAUDE.md`, with the obligation moved to them under D-642 |
| **D-564** | Correction of record: the 'function-only' share of the legacy residual was overstated — over-grab corrupts the BASS | **false-negative-path** | `BATCH_LEGACY_DEFAULT`, `TESTS_CHORD` | **none-found** | **Reach follows the pass's D-284 and D-243 precedent** — a FINDING about the legacy surface takes the reachability of the surface it is about, not of the prose that records it. Transfer: the citation scan finds only homing and triage hits; no ruling carries it. **ONE OBSERVATION, recorded rather than promoted to a verdict:** its home is `CLAUDE.md` gate block (D), and the caveat it corrects is stated there as applying *equally to the robust unit* — the live measurement. So a reader of the live block meets the corrected apportionment. That is the entry's home being live, **not a ruling carrying its principle**, and under bound (i) it is not a transfer |
| **D-568** | The two-track remedy: chord axis by hand-built rules, key axis by evidence quality and calibration — neither by a wider search | **false-negative-path** | `L3_SPEC_DORMANT`, `BATCH_LEGACY_DEFAULT`, `TESTS_CHORD`, `TESTS_KEY` | **assigns-live-work** | The two-axis pipeline it was derived on is reachable only off the default paths. **The transfer half is `assigns-live-work` on the value's own definition** — *the decision's OWN text assigns work, ownership or a property to the live design, not a later ruling* — and the record says so twice: the home text calls it *"the work-programme statement it is, not a description of what runs"*, and its key-axis half assigns the residual to *"the joint combination's SOFT integration"*, which is the live estimator. Its home is the arc plan's Stage-5 paragraph, the precision work it governs |
| **D-571** | The declared-mode influence becomes a small additive hint, and SMALLNESS IS THE GATE | **false-negative-path** | `L3_SPEC_DORMANT`, `BATCH_LEGACY_DEFAULT`, `TESTS_KEY` | **carried-elsewhere** | A scoring term of the legacy key emission. **The transfer is unusually exact and the record names it:** this entry's provenance states that the joint estimator takes the signature and declared mode as *"a weak fitted soft prior with no conditional gate anywhere"* (**D-528**) and conditions the initial key state only (**D-450**) — and *no conditional gate anywhere* is this decision's own *no separate confidence test is added*, on the live arm |
| **D-572** | The hard post-hoc declared-mode promotion REMOVED OUTRIGHT rather than kept in a gated form | **none** | **`SPEC_DONOTRETRY_DECLARED_MODE`** *(NEW — see §4)* | **live-prohibition-in-spec** | Reach `none`: the promotion was removed, so nothing at HEAD implements the subject. **This is the one entry of the eleven cited in a LIVE specification section**, and the citation is a standing do-not-retry: `ARCHITECTURE.md` carries *"Tried and closed on the declared mode's weight … do not retry; the register carries it with its evidence: D-572"*. The subject stays legacy; the prohibition binds now. *(**D-528**'s own title additionally records that the hard declared-mode wall is **formally retired** on the live arm — noted, but the do-not-retry line is the more specific and is what the verdict rests on)* |
| **D-575** | The Baroque partial-signature convention handled by DETECTING it and reinterpreting the signature one step | **false-negative-path** | `L3_SPEC_DORMANT`, `BATCH_LEGACY_DEFAULT`, `TESTS_KEY` | **none-found** | The correction is applied inside the legacy resolver, which the production arm does not run. **Deliberately NOT `explicitly-not-transferred`, and the distinction matters:** that value requires a ruling stating the decision does not bear on the live design, and what the record actually says is that the question is **unsettled** — the home text's own words are *"Whether the joint estimator handles the convention AT ALL is NOT settled by this entry and is not asserted here."* Unsettled is not the same as not-transferred, so the weaker verdict is the honest one. **★ This entry is why §5 exists** |
| **D-579** | The anchor obligation: compute the chord ONCE against its region's FINAL notes, with tonality an explicit input | **none** | `BATCH_JOINT`, `RECORD_SECTION` | **carried-elsewhere** | **Reach `none` on the pass's own D-215 precedent** — the obligation was never executed on the path it was written for, so nothing at HEAD implements the subject. Its two anchors are the production-path anchors, and they are the evidence for the transfer as much as for the reach: the record states the obligation *"was met by replacement rather than by repair"* — the live arm is one joint decode over key, mode, chord and segmentation together (**D-001**), which is the ordering this step asked for, reached by a different route |
| **D-580** | Two of the twelve post-scoring gates are purely-local and MUST survive the dissolution; the other ten dissolve | **false-negative-path** | `FM2_FLIP`, `BATCH_LEGACY_DEFAULT`, `TESTS_CHORD` | **undetermined** | The gates are legacy code at HEAD, and the entry's own home text says the surviving rule name for one of the two is **FM2** — which is the anchor. **The transfer half is UNDETERMINED on the pass's own D-325 precedent, and this is the sharpest of the eleven.** The rule this constrains — dissolving the post-hoc correction layer into the competition — is **D-429**, whose principle a user ruling DID carry to the live design. Whether the carve-out rides across with it, or was scoped to the legacy dissolution that never ran, is **a ruling and not a session's call**. Recorded as open rather than resolved either way |
| **D-583** | A known deferred loss is KEPT only while it stays characterized EXACTLY, and re-adjudicated when its form changes | **false-negative-path** | `JKEY_WIRING_FLAG`, `JKEY_NO_REEMIT`, `BATCH_LEGACY_DEFAULT` | **none-found** | The characterized loss sits on the legacy region path behind a SECOND default-OFF flag — the same anchors the pass gives D-278, the shelved step this defers to. **One thing the record states and the verdict does not credit:** its provenance says *"the CONDITION it states is general"*, while the behaviour it characterizes is legacy. Under bound (i) a general condition no ruling carries is `none-found` — but a reader should not take the condition itself for legacy-scoped, and that is said here rather than folded into a verdict |

## 4. The one new anchor this set needs

Ten of the eleven verdicts rest on anchors the pass already declares and already locates. **One new
anchor is required**, for D-572's do-not-retry citation:

| Key | File | Line | Quote | What it says |
|---|---|---|---|---|
| `SPEC_DONOTRETRY_DECLARED_MODE` | `ARCHITECTURE.md` | 4198 | `Tried and closed on the declared mode's weight` | The same construction as the pass's three existing do-not-retry anchors, on the declared-mode weight — a LIVE specification line naming D-572 with its evidence. It is a fourth instance of a construction the pass already anchors on the chord layer, the key layer and the search |

**Located, not transcribed:** the quote was read at that line of `ARCHITECTURE.md`. It is written
here as a proposal; **it is not added to the tool by this file.**

## 5. ★ ONE FINDING BEARING ON THE ANALYSIS CAME OUT OF HALF B, AND IT IS SURFACED RATHER THAN LEFT IN A CELL

**D-575's transfer verdict is `none-found`, and the reason it is `none-found` is a live open
question about the arm that ships.** The Baroque partial-signature convention — scores notated with
one accidental fewer than the modern convention, so the sounding key sits one step to the sharp
side — was detected and corrected **inside the legacy key resolver**. The production arm does not
run that resolver.

**What is established, each at the object:** the detection-and-reinterpretation machinery is in the
legacy key path and nowhere else; the joint module carries no construct of that name (its only
matches on the search terms are a phrase-split remark and a partial-record remark, both read and
neither related); and D-575's own home text states the question is **not settled and not asserted**.

**What is NOT claimed, and the distinction is the whole point.** Absence of the machinery is not
absence of the handling: the live arm reads the signature and declared mode as a **weak fitted soft
prior** (**D-528**) rather than as a hard constraint, so a key one step to the sharp side is
reachable there without an explicit correction. **Whether it in fact reads these scores correctly is
unestablished — in both directions.**

**And one thing substantially reduces the alarm, stated so the finding is not read as larger than it
is:** the production arm's key agreement on exactly this repertoire **is measured and published** in
gate block (A). So this is not an unmeasured failure hiding behind a green gate — any effect is
already inside a published figure. What is missing is whether a known, named, corpus-wide notation
convention is handled at all on the arm that ships, which bears on how that figure should be read.

**Rowed at [[OI-357]] in the same commit (rule (c)), and surfaced at `cowork_away_returns.md` §2.8.**
Nothing is proposed for it beyond the row: no fix, no design, no inference change (D-231, #8).

## 6. What this file does NOT do

- **It writes no verdict into `gen_phase1w_legacy_verification.py`** and clears no guard. The
  standing failure is carried.
- **It changes no LEGACY mark.** The marking convention (`CLAUDE.md` decisions-register rule (f)) is
  not in question, and none of the eleven is asserted mis-marked.
- **It reopens no phase-1w verdict** and does not touch [[OI-289]]'s status.
- **It moves no status, no home and no register entry**, and assigns no identifier.
- It touches no `src/`, no golden, no corpus of scores and nothing in `tools/robust_stop/`.

**Phase 1's completion statement is not written, not drafted and not partially written here.**

*Provenance: the user's Ruling 18 of 2026-08-09 (`cowork_rulings_2026_08_09_third_stop.md`),
recorded at [[OI-354]]. The method is `tools/audit/decisions/gen_phase1w_legacy_verification.py`'s
own `THE_TEST` block, read in full before the first verdict was written (the dispatch's assumption
A1, discharged). The population is that tool's own output at task start (A2). Every entry's record
was read at its rendered register entry — verbatim, plain restatement, status, home and provenance —
and every successor named in a transfer verdict was confirmed to exist at its own heading. No
defense, reason or citation here is reconstructed from memory.*
