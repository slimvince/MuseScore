# CC Instruction — Engage arc #4: the INFORMATION-LOSS audit (read-only catalogue)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** The no-information-loss principle (#12) made **proactive** instead
> of accidental. The Gate A case proved this class of defect is real, lurks, and lands on exactly the surface
> Layer 5 will consume — we found it only incidentally. This dispatch **systematically catalogues** suspected
> information-loss sites.
>
> **READ-ONLY. No `src/` change, no corpus write, no build, no fixes.** Each fix is a *separate, ratified*
> event (the Gate A pattern). This is investigation + architectural review — moratorium-clear (not
> inference-fixing). The deliverable is a **grounded, classified, prioritized catalogue**, not repairs.
>
> **★ THE CENTRAL CLASSIFICATION (the user's binding rule — get this right):** not-yet-consumed information is
> **NOT automatically a defect.** Classify every candidate site on this axis:
> - **OK — PRESERVED, awaiting a future/dormant consumer.** The information is intact and carried; it simply
>   is not consumed *yet* because its consumer is not built yet (e.g. Layer 5 is dormant). This is correct
>   forward-provisioning — **record it as OK, not a defect** (it tells us the substrate is ready for engage).
> - **DEFECT — LOST.** The information is destroyed / overwritten / collapsed / dropped so that **no** consumer
>   — present OR the architecture-intended future one — can recover it. The Gate A case is this: the distinct
>   alternative is overwritten by a near-duplicate, so even the future Layer 5 selector is deprived.
> - **DEFECT — SHOULD-ALREADY-BE-CONSUMED.** The information is (or could be) preserved, but a consumer that
>   **already exists and should be using it now** does not receive it (a routing/wiring gap — "not consumed
>   downstream but it already SHOULD have been").
> - **UNCLEAR — consumer-status ambiguous** → do NOT guess. Record as unclear (is the consumer future-intended
>   or should-already?) for user adjudication. (#1 — no assumptions.)
>
> **Grounding rule (binding, #1):** every catalogued site is grounded at the code (the symbol/line + the
> mechanism), and its consumer(s) identified at the code/contract. No assumption-based entries.
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools.
>
> **Current state:** HEAD = the Gate A build commit (or `b0acb5c436` if the build has not yet landed —
> confirm), fork-only, ahead 0. Both stops green.

---

## Task 0 — state check
HEAD/branch/ahead; both stops green (read-only, so untouched). Report.

## Task 1 — sweep the load-bearing surfaces (scope — specific, not general, #2)
Statically audit the surfaces that feed Layer 5 and downstream, where lost information degrades the analysis
(the research grounding `cowork_functional_analysis_research_grounding.md` names the load-bearing signals —
bass, spelling, distinct alternatives, preserved uncertainty). Cover:
- **The carried readings / `alternatives[]`** — the carry surface Layer 5 selects among (the Gate A class).
- **Confidence / uncertainty values** — anywhere a distribution / soft score / margin is collapsed to a hard
  decision or a point estimate (the confidence-contract surface).
- **The key and chord candidate sets** — dropped/merged candidates, and the key-then-chord truncation the
  owed joint step is meant to fix.
- **Pitch spelling** — flattening spelled pitches to bare pitch classes where spelling was load-bearing
  (the research flags spelling as predictive of correct root — a #4-relevant loss).
- **The diagnostic / dump surface** — computed-then-not-surfaced signals.

## Task 2 — hunt the loss PATTERNS (the taxonomy)
For each surface, look for these forms (the user's a–d plus the extensions), and classify each hit on the
central axis above:
- **(a) overwrite/replace** a distinct value with a duplicate or weaker one (Gate A / FM2).
- **(b) compute-then-drop** — a discovered signal not carried to a consumer that needs it.
- **(c) partial-truth** — collapse a set to one element; keep the winner but discard the alternatives; report
  only some of the available detail.
- **(d) lossy dedup/merge** — merging that collapses genuinely distinct entries (inversion / spelling).
- **(e) ordering/ranking loss** — flattening or reordering a list whose order encoded preference/confidence.
- **(f) silent truncation/cap** — a cap / threshold / bar that drops candidates without recording they
  existed.
- **(g) uncertainty collapse** — reducing a distribution / soft posterior to a hard point estimate.
- **(h) spelling flattening** — spelled pitch → pitch class where spelling mattered.
- **(i) overwrite-on-recompute** — a later pass overwriting a richer earlier result with a poorer one
  (staleness / legacy class).
- **(+) any further form** the code reveals — record it as a new taxonomy entry (the user expects there are
  more than we listed).

## Task 3 — the catalogue (the deliverable)
`cowork_information_loss_audit.md` — one row per catalogued site:
- **location** (file:line + symbol) · **surface** · **taxonomy form (a–i/+)** · **what information** ·
  **intended consumer(s)** (present / future-per-contract / none) · **classification** (OK-provisioned /
  DEFECT-lost / DEFECT-should-already / UNCLEAR) · **severity** (deprives an architecture-intended consumer =
  high; cosmetic / nothing-ever-consumes = low) · **grounded evidence** (the code mechanism).
Then a **prioritized fix-queue** of the DEFECT rows (each a future separate ratified event, Gate-A-style),
and a short list of the OK-provisioned rows (so we know what substrate is already engage-ready) and the
UNCLEAR rows (for user adjudication). Cross-reference the research grounding where a loss touches a
known-load-bearing signal (spelling / uncertainty / bass / distinct alternatives → #4-relevant, flag high).

## Task 4 — report + fold + push
1. **Report** `cc_engage_information_loss_audit_report.md` (force-add): method, surfaces swept, counts by
   classification, the top DEFECT findings, all SHAs.
2. **Sandwich (trivial — read-only):** no `src/` change; both stops untouched; suites unchanged (no build).
3. **Fold** (`docs(cowork):`): the catalogue + report · `STATUS.md` · `COWORK_HANDOFF.md` ·
   `cowork_stage5_fitter_design.md` (engage-arc observation) · this instruction (force-add).
4. **Push fork-only** (`git push origin master`) — the `cfc7eb5e39` upstream HARD STOP.

## STOP conditions
- Any `src/` change, corpus write, build, or fix (read-only catalogue only — fixes are later ratified events).
- Any catalogue entry not grounded at the code, or any consumer-status **assumed** rather than verified — mark
  UNCLEAR instead of guessing (#1).
- Classifying PRESERVED-awaiting-future-consumer as a defect (it is OK), or classifying a genuine LOSS /
  should-already gap as OK — the central axis must be applied faithfully.
- Any push/PR/merge toward `upstream`/`musescore/MuseScore` (the `cfc7eb5e39` distribution HARD STOP).

## Acceptance
The load-bearing surfaces swept for the a–i(+) loss forms ✓ · every hit grounded at code and classified on the
central axis (OK-provisioned / DEFECT-lost / DEFECT-should-already / UNCLEAR), no assumed consumer-status ✓ ·
the catalogue + a prioritized DEFECT fix-queue + the OK-provisioned and UNCLEAR lists, research
cross-references on #4-relevant losses ✓ · report + fold with SHAs ✓ · no src/corpus/build/fix; both stops
green; pushed fork-only ✓.

*Cowork, 2026-07-06. Engage arc #4 — the no-information-loss principle made systematic. Read-only; every fix
is its own ratified event. On CC's report: Cowork verifies the catalogue at objects → brings you the DEFECT
fix-queue and the UNCLEAR rows to adjudicate.*
