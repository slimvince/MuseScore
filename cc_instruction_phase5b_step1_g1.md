# CC Instruction — Phase 5b Step 1: build G1 — commit / inherit / abstain + sufficiency gate (the lever)

> **Why.** Per the grounded `cowork_phase5b_l4_build_plan.md` (Steps 1..n), Step 0 (`9ef7ff312a`) measured the new
> per-slice path **−15 vs legacy**, and **all of it is the unbuilt G1 mechanism** — `chordslicedecoder` always commits
> the top candidate (only a margin `uncertain` flag at `:298/:319`; no abstain, no inherit, no ≥3-chord-tone
> sufficiency gate). Build G1 per the spec (`cowork_layer4_chordsymbol_design.md`). **This is algorithmic completion of
> the L4 layer per its spec — build-it-right, NOT inference-tuning** (the firewall is about tuning accuracy on hard
> cases; this builds a *designed, missing* mechanism). The decoder is **production-dead**, so this is **byte-identical
> on production** (corpus 53/24/53 + suites + snapshots unchanged); only its diagnostic output changes — which we then
> **re-measure**. *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read the spec's G1 (commit / inherit / abstain + sufficiency) against the as-built `chordslicedecoder` and confirm the
build maps cleanly. Report, then build only if clean:
- **The sufficiency-gate's chord-tone source:** the ≥3-chord-tone gate must count the **candidate template's own chord
  tones present in the slice** (root/3rd/5th/7th structural presence) — **independent of the NCT membership** (that's
  G2, still flat/wrong). Confirm the decoder exposes (or can compute) the candidate's template-tone presence count
  without depending on the G2 membership rule. *(If sufficiency unavoidably needs the correct membership first → STOP
  and report: the G1-before-G2 order would need amending.)*
- **Inherit source:** what "prevailing chord" is carried (the previous committed slice's result) — confirm it's
  available in the decode loop.
- **Abstain representation:** how a no-commit/abstain slice is represented in the result (a no-chord / open marker),
  distinct from today's margin `uncertain` flag.

## §2 — BUILD G1 (in `chordslicedecoder`, dormant — production-dead)
Per the spec: for each slice, after ranking candidates —
- **Sufficiency gate:** commit a chord only if the top candidate has **≥3 of its template chord tones present** in the
  slice (the phantom-root guard). 
- **Inherit:** if no candidate is sufficient but the slice is a thin/transitional continuation, **inherit the prevailing
  committed chord** (carry it forward) rather than naming a phantom.
- **Abstain:** if neither commit nor inherit applies (genuinely no scorable/ sufficient chord), **abstain** — emit the
  spec's no-chord/open marker (not a forced top candidate).
- Keep the **one `analyzeChord` cube** (no second scorer); this is decision logic on the existing candidate ranking.

## §3 — RE-MEASURE (the assess-for-amendment checkpoint)
Re-run the diagnostic new-vs-legacy comparison (Step-0 method, Baroque + Default): the new per-slice chord-root accuracy
**before → after G1**, and the phantom-root / thin-slice rates before→after. **Report the delta.**

## §4 — Gate
- **Production byte-identical:** corpus **53/24/53**, `composing_tests`, `notation_tests`, `pipeline_snapshot_tests`
  **unchanged** (decoder is production-dead). **Any production movement → STOP** (the decoder leaked onto the live path).
- **New unit tests** for sufficiency / inherit / abstain (oracle-asserted: a thin slice → inherit; a phantom-root
  candidate <3 tones → abstain/no-commit; a clear triad → commit).
- Build green.

## §5 — ASSESS (does the sequence hold?)
- **Expected:** G1 closes **most** of the −15 (the phantom-root + thin-slice rates drop sharply). If it does → the
  grounded order holds; proceed to Step 2 (membership).
- **If G1 does NOT close most of the deficit** (the residual stays large, or a different failure mode dominates) →
  **STOP and report**: the sequence (or the spec's G1 rule, or — worst case — the layer decomposition) needs amendment.
  Do **not** push on to Step 2 on a failed assessment.

## §6 — Deliver
Commit **locally (unpushed)**: the G1 logic + its unit tests (decoder + tests only — no production wiring). Write
`cc_phase5b_step1_report.md` (gitignored): the §1 confirm, the §2 build, the §3 **re-measured delta** (chord-root +
phantom/thin rates before→after), the §5 assessment (sequence holds / needs amendment), and the commit sha — so Cowork
verifies by sha that only `chordslicedecoder.*` + tests changed, production byte-identical.

## §7 — Stops
- Sufficiency needs the G2 membership first → STOP (re-order question).
- Any production movement (corpus/suites/snapshots) → STOP (decoder leaked live).
- G1 doesn't close most of the −15 → STOP, report (amend the sequence/spec).
- A push targets `upstream` → STOP.
