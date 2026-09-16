# CC Instruction — Phase 5b Step 3: G6 — confidence model + open-question label (the L4→L5 abstain contract)

> **Why.** Step 3 of the grounded `cowork_phase5b_l4_build_plan.md`. Step 2-final accepted (`d52cfd0847` +
> `4aa88452cd`): the two-reading inherit is the best variant; abstain is higher *by design* (transition slices → L5).
> Step 3 builds **G6** — the spec's confidence model beyond margin-only, and the **open-question label**: when the
> decoder **abstains**, it must **name the open question** (the competing readings) and **carry them forward** so
> Architectural Layer 5 can resolve them. This is the **L4→L5 abstain contract** — the forward interface. **Build the
> *representation/model* per the spec — build-it-right. The *threshold calibration* (how confident is confident enough)
> is Phase B — do NOT tune it here (the firewall).** Decoder production-dead → **byte-identical on production.**
> *(Reminder: the never-bash rule is Cowork's.)*

## §1 — INVESTIGATE-confirm BEFORE building (the incremental check)
Read the spec's G6 (confidence + open-question / "name the open question", and the L4→L5 carry) against the as-built
`chordslicedecoder`. Confirm and report:
- **The confidence model** the spec specifies beyond the current margin-only `uncertain` flag — and whether it **changes
  the commit/abstain *decision*** (accuracy-affecting) or is a **richer confidence *value*** carried alongside the same
  decision (representational). State which.
- **The open-question representation:** on an abstain, what does the spec say L4 carries to L5 — the **competing
  readings** (the top candidates that tied/were close), the kind of ambiguity (share-tone / relative-pair /
  transition-vs-continuation), and any provisional context. Confirm the decoder already has these (the ranked
  candidates / margins) to populate it.
- **The L4→L5 contract shape:** confirm this is a forward, additive interface (L4 *declares* uncertainty + names the
  question; L5 *resolves* with function/progression) — it must **not** itself try to resolve the open question (that's
  L5). If building it needs L5 or a structural change beyond the decoder → **STOP and report.**

## §2 — BUILD G6 (in `chordslicedecoder`, dormant)
- **Confidence model** per the spec (beyond margin-only). If it is purely a richer value (no decision change), build it
  as such; if the spec's model changes the commit/abstain boundary, build the **model** but keep its parameters at the
  spec's described defaults — **no threshold tuning for accuracy** (Phase B).
- **Open-question label:** on abstain, populate a structured marker — the **competing readings** + the ambiguity kind —
  and carry it on the slice result for L5. Distinct from a bare `uncertain` flag.
- Keep the **one `analyzeChord` cube**; this is representation/decision wiring, not a new scorer.

## §3 — RE-MEASURE (the assess checkpoint — per the CORRECTED gate)
New-vs-legacy, Baroque + Default. Judge by **coverage-matched accuracy + correct abstention**, NOT raw coverage. Expect
G6 to be **accuracy-neutral-or-better** (the open-question label is representational; the confidence model should not
regress committed accuracy). Report coverage-matched accuracy + abstain before(Step-2-final)→after(G6), and **confirm
the open-question label is populated on abstained slices** (a spot-check: a share-tone abstain names both readings).

## §4 — Gate
- **Production byte-identical:** corpus 53/24/53, both suites, snapshots unchanged (decoder dead). **Movement → STOP.**
- **New unit tests** (oracle-asserted): a share-tone abstain (e.g. Am6↔F♯ø7) carries **both** competing readings + the
  ambiguity kind; the confidence model returns the spec's value on a clear vs an ambiguous slice. Build green.

## §5 — ASSESS
- **Expected:** the confidence/open-question representation is built, coverage-matched accuracy holds-or-improves, the
  L4→L5 contract is populated on abstains → proceed to **Step 4 (spelling-pin, G4)**.
- **If committed accuracy regresses, or the open-question contract needs L5 to populate, or it needs threshold tuning to
  not regress → STOP and report** (don't tune — firewall; re-assess).

## §6 — Deliver
Commit **locally (unpushed)**: G6 + unit tests (decoder + tests only). Write `cc_phase5b_step3_report.md` (gitignored):
the §1 confirm, the §2 build, the §3 re-measure + the open-question spot-check, the §5 assessment, and the commit sha —
so Cowork verifies by sha that only `chordslicedecoder.*` + tests changed, production byte-identical.

## §7 — Stops
- The confidence/open-question needs L5 to populate, or a structural change beyond the decoder, or threshold-tuning to
  avoid a regression → STOP, report.
- Any production movement → STOP. `upstream` → STOP.
