# CC Instruction — Phase 5c Step 2 amendment RESOLUTION: commit the relaxation; the limit is by-design

> **Your §5 STOP finding is correct and important — and it does NOT block.** A key-agnostic event-pair test cannot
> separate a plain V→I from a plain I→IV (exact transpositions); the leading-tone-resolution event is not a key-agnostic
> discriminator. **My spec premise was wrong and is now corrected** (`cowork_layer5_function_design.md` §5.2 — "the
> key-agnostic limit"). But the *relaxation you applied is right* — a plain V→I **is** an authentic cadence (the chorale
> phrase-end), and re-adding the seventh gate would lose it. The disambiguation is **not the key-agnostic detector's job**
> — it is **resolved downstream**: the seventh (position-independent signature), the **phrase gate** (rejects the common
> mid-phrase I→IV), and the **key-layer aggregation** of the soft tonic-vote against the home-signature pull (absorbs the
> rare at-boundary I→IV). The cadence detector casts **soft evidence**; it is not a key-aware classifier. *(Reminder: the
> never-bash rule is Cowork's.)*

## §1 — Commit the relaxation (it is correct)
- **Keep the relaxation** (genuine-dominant dropped as a family gate; the seventh/tritone is the `+wSeventh` vote
  strengthener; perfect/imperfect by bass-five-to-one unchanged). **Commit it.**
- The two positive tests stay green: `PlainTriadVToIIsPerfectAuthentic` and `SeventhStrengthensTheVoteOverAPlainTriadV`.

## §2 — Reframe the "STOP" test as a documented limit (not a blocker)
- Rename `PlainAuthenticAndItsTranspositionAreIndistinguishable_STOP` → a **documented-limit** test (e.g.
  `..._KeyAgnosticLimit_ResolvedDownstream`). It correctly asserts that the **event-pair test alone** returns the same
  verdict for a genuine V→I and its +5 transposition — that is **by design** (the detector is key-agnostic and casts a
  soft vote). Add a code comment + the test docstring pointing to §5.2 "the key-agnostic limit": disambiguation is the
  phrase gate + the key-layer aggregation, not this unit.

## §3 — Confirm (and test) the downstream noise-reduction that DOES hold here
- **The phrase gate:** confirm at source that cadence candidates are admitted **only at a phrase boundary** (the
  `phraseBoundaryTicks` gate), so a **mid-phrase** plain I→IV is **not** admitted as a candidate in the real pipeline.
  Add a test: a plain I→IV **not** at a phrase boundary yields **no cadence**; the same pair **at** a phrase boundary is
  admitted (and casts the soft vote that the key layer will weigh). If the phrase gate is not applied at candidate
  admission, report it — that is the place the common-case discrimination must live.
- Leave the **rare at-boundary I→IV** as the documented soft-evidence residual (the key layer absorbs it). **Do not** add
  a key-aware test inside this key-agnostic unit (that would re-introduce the circularity).

## §4 — Gate
- **Dormant + byte-identical:** corpus **53/24/53** unchanged, `composing_tests` / `notation_tests` /
  `pipeline_snapshot_tests` green, no golden refresh. Movement → STOP.

## §5 — Deliver
Commit **locally (unpushed)**: the relaxation + the reframed/added tests. Append to `cc_phase5c_step2_amendment.md` the
resolution (relaxation committed; the limit documented; the phrase-gate confirmation) + the commit sha. Then **Step 2 is
complete** — proceed to await the Step-3 (resolver) instruction.

## §6 — Stops
- The **phrase gate is not applied at candidate admission** (so even the common mid-phrase I→IV is admitted) → STOP and
  report — the common-case discrimination would be missing and we must place it before proceeding.
- Any production movement, any threshold **tuning**, or re-adding the seventh **gate** → STOP. `upstream` → STOP.
