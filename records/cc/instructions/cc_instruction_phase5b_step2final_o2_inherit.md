# CC Instruction — Phase 5b Step 2-final: correct (keep G2/G3, revert over-inherit) + build the §4 two-reading both-sides inherit

> **Why.** Step 2 (`1b7fee1cd5`) built the G2/G3 membership ladder + plausibility fix (**correct, accuracy-neutral —
> keep**) **plus** a **one-sided, note-only inherit** (it carries the prevailing/left chord when a thin slice's extra
> notes are stepwise NCTs of it). That **over-inherits** (measured −4.3% among-committed; thin-slice misses 45→300),
> because it **cannot see the next chord** — it can't tell a *continuation* of the prevailing chord from a *transition*
> to the next.
>
> **Crucially, the spec already specifies the fix — and it is NOT the deferred O2 joint window.** §4 (lines ~183–191)
> says the inherit/abstain test "need the neighbouring chords … the **second reading** re-decides each slice using the
> provisional neighbours **on both sides**"; the inherit fallback "acts **only on the second reading**." CC built a
> *one-sided* inherit — **less than the spec's two-reading baseline.** **The fix is to build the §4 two-reading
> BOTH-SIDES inherit correctly.** §15-O2 (a bounded-window *joint* resolution) stays **deferred** (only if the
> two-reading still falls short — §15-O2 line 501–502). This keeps the call in **Layer 4** (next *chord*, a Layer-4
> result — not Layer-5 function); the genuinely **function-dependent residual abstains → L5**. **Algorithmic completion
> per the spec — build-it-right, NOT inference-tuning.** Decoder production-dead → **byte-identical on production.**
> *(Reminder: the never-bash rule is Cowork's.)*

## §A — Correct Step 2 (commit A): keep G2/G3, revert the one-sided over-inherit
Revert the one-sided note-only inherit relaxation to G1's conservative template-only inherit; **KEEP the G2/G3
three-tier ladder + plausibility fix** (accuracy-neutral, correct). Re-confirm the baseline (among-committed ~77%,
abstain ~53% = G1 + G2/G3). **Commit A** (decoder + tests). Verify production byte-identical.

## §B — INVESTIGATE-confirm the §4 two-reading both-sides inherit BEFORE building
Read §4 (the two-reading scheme) + §5-step-4 against the as-built decode. Confirm and report:
- Does the decoder's **two-pass** (Increment-B) already produce **provisional neighbours on BOTH sides** (a first
  provisional reading available to a second reading)? Is the gap simply that the inherit decision uses only the
  **prevailing/left** neighbour, not the **next/right** provisional chord?
- The §4 inherit rule with both-side neighbours: inherit the prevailing chord through a thin slice **iff both-side
  provisional neighbours are the prevailing chord (a CONTINUATION)**; if the **next provisional chord differs
  (a TRANSITION)**, do NOT inherit (commit/abstain per the slice's own evidence).
- The **function-dependent residual** (passing-vs-cadential 6/4 etc. — undecidable from chord neighbours) → **ABSTAIN
  (→ L5)**, never forced.
- **Stay note + membership + provisional-neighbour-CHORD only — never progression grammar** (the spec's §15-O2 guard:
  too much and it becomes the Layer-5 progression decode). If the both-sides inherit needs a structural change beyond
  the decoder, or genuinely needs L5 *function* for the BULK → **STOP and report** (re-decide; the inherit may be L5).

## §C — BUILD the §4 two-reading both-sides inherit (commit B)
Make the second-reading inherit decision use the **next provisional chord** (both-side neighbours), per §4 — not just
the prevailing. Keep the **one `analyzeChord` cube**; this is the second-reading decision wiring, not a new scorer, and
**not** the deferred O2 joint window (leave O2 deferred; flag if the two-reading falls short).

## §D — RE-MEASURE (the assess checkpoint)
New-vs-legacy, Baroque + Default, reporting the two-reading inherit **vs the two known failure modes** {G1-conservative
(under-inherits, 53% abstain); the one-sided note-only (over-inherits, regresses)}: among-committed accuracy,
abstain/coverage, coverage-matched. **The two-reading should land between them** — coverage **higher** than
G1-conservative, accuracy **NOT regressed** like the one-sided. Report the table.

## §E — Gate
- **Production byte-identical:** corpus 53/24/53, both suites, snapshots unchanged (decoder dead). **Movement → STOP.**
- **New unit tests** (oracle-asserted): a continuation thin slice (next == prev) → inherit; a transition thin slice
  (next differs) → don't-inherit; a function-dependent residual → abstain. Build green.

## §F — ASSESS
- **Expected:** the two-reading raises coverage vs G1 **without** the one-sided regression → sequence holds; proceed to
  Step 3 (confidence/open-question, G6).
- **If it regresses, fails to raise coverage, or the bulk genuinely needs L5-function → STOP and report** — re-decide
  (the inherit may be an L5 responsibility, or O2 is genuinely needed). Do not push to Step 3 on a failed assessment.

## §G — Deliver
Commit **A** (corrected G2/G3) then **B** (two-reading inherit), local/unpushed, decoder + tests only. Write
`cc_phase5b_step2final_report.md` (gitignored): §A baseline, §B confirm (does the two-pass give both neighbours?), §C
build, §D re-measure table (two-reading vs G1-conservative vs one-sided), §F assessment, **both commit shas** — so
Cowork verifies by sha that only `chordslicedecoder.*` + tests changed, production byte-identical.

## §H — Stops
- The both-sides inherit needs beyond-decoder structure, or L5-function for the bulk → STOP, report.
- Any production movement → STOP. It regresses / no coverage gain → STOP. `upstream` → STOP.
