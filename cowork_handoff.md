# Cowork Session Handoff — MuseScore Studio Harmonic Analysis

---
## ★★★★★ COWORK SESSION CLOSE 2026-07-19 — THE DESIGN PASS IS DONE: THEORY GROUNDED, FIVE DECISIONS + THE FACTORIZATION SPECIFICATION USER-RATIFIED. THE CURRENT ENTRY POINT.

**You (the next session) start clueless — this block is the entire handover.** Read, in order:
(1) `CLAUDE.md` in full (the principles are now **#1–#24** plus the constrained-optimum ledger
corollary — #20–#24 user-ratified 2026-07-18); (2) `OPEN_ITEMS.md` (current through OI-183);
(3) this block; (4) **`cowork_joint_estimator_factorization.md` — THE RATIFIED STRUCTURE** (the
variables, the ten-factor score form, the premise ledger P1–P8, the decode plan, the desk-simulation
forms and case list); (5) `cowork_joint_estimator_architecture.md` §5a (the five ratified design
decisions, each with its excluded-alternatives record); (6) `cowork_term_theory_grounding.md` (the
per-factor derived forms with fetched primary sources, the ground-truth-ceiling findings, the fitting
evidence).

**★ THE HEADLINE.** The term-level theory-grounding audit is COMPLETE in both halves (the 95-term code
inventory, commit `abca1ff2c3`; the theory derivation from five deep-research passes with primary
sources fetched), the research library is filed (`docs/research_papers/` — README index +
BIBLIOGRAPHY register; every binary lives in git ONLY in the private repo `slimvince/research-papers`;
the public fork is `.gitignore`-guarded; NOTHING is redistributed), and — the substance — **five
design decisions and the factorization specification were user-ratified 2026-07-19**: (1) mode axis
{major, minor}, modal color in the emission, the un-rounded modal reading PUBLISHED for the
presentation layer; (2) staged fitting — generative tables from counts, frozen, + convex
conditional-likelihood fit of the few combination weights, the identity-weight generative baseline as
a MANDATORY ablation; (3) the chord state is SCALE-DEGREE-VALUED (Roman numeral relative to tonic and
mode; the chord symbol a derived published fact; applied-degree classes for tonicization); (4)
non-chord tones live INSIDE the emission with chord-independent melodic/metric covariates — no
cleaning stage; ornament labels derived post-decode and published; (5) the signature/declared-mode
prior is a weak FITTED soft prior with NO conditional gate — its influence self-confines to ambiguous
passages by the probability calculus; the signature-influence rate is measured by ablation and
published at every fit; the declared-mode wall is retired.

**★ THE DESK SIMULATION IS RUN AND USER-RATIFIED (2026-07-19, this session's second act —
`cowork_factorization_desk_simulation.md`).** All ten §6 traces on paper, every corpus fact verified at
a committed source (incl. the OI-142 +2 offset on bwv145.5). Nine of ten pass as specified — including
C1 `bwv145.5@12960` right WITHOUT the OI-168 special form, and C4 `bwv110.7@2880` flipping to the GT
key by the designed mechanisms. The tenth (C3 `bwv10.7@36000`) surfaced the one surprise (#13, the
stage working): the score form's FACTOR GRANULARITY was under-specified (per-segment factors reward
merging — semi-Markov length bias) — **amended with ratification** (factorization doc §2: bass per
event, missing-tone penalty per event of length). **Also settled with ratification: the
signature/declared-mode prior is INITIAL-STATE-ONLY**, re-anchored at a notated signature change
(factorization doc §3.10). OI-181 ✅; new rows OI-184 (WiR anacrusis alignment — establish before fit
counts), OI-185 (bwv352 b4 bass check); the §4.3 sensitive-cell record feeds OI-177.

**★ THE PRE-FIT GATES ARE DRAFTED AND USER-RATIFIED (2026-07-19, this session's third act —
`cowork_prefit_gates.md`):** the OI-176 (5-fold CV grouped by analysis file, committed assignment,
train-fold-only fitting, CV headline + bootstrap CI), OI-177 (count-inventory artifact, cell threshold
20, params ≤ tokens/10, ≤ 12 weights, §4.3 sensitive-cell records), OI-178 (the adoption-event
variant, written before any diff: MAP commit / no abstention, asymmetric #17b prediction, per-preset
class-(b) net decrease with every added run explained, O-12, one revertible adoption commit), and
OI-180 (A isolated on the L1/L1.5 fact surface behind a default-OFF driver, byte-identical production,
full-surface side-by-side grading, six-item post-adoption retirement map incl. the deferred Gates A–L
dissolution, reverse map, DT-13 visibility guard) protocols. All four rows read "protocol ratified —
pending execution".

**★ THE IMMEDIATE NEXT ACTION — the funnel's probe/build arc may open under the OI-180 sanction.**
Dispatches are written just-in-time (the standing rule); the first concrete steps in order: (1) the
OI-176 fold-assignment artifact + the OI-177 count-inventory instrument (both read-only, CC
dispatches); (2) OI-184's anacrusis-alignment establishment (gates the boundary/metric-table counts);
(3) then table fitting under the ratified protocols. **The dual-path status line (the OI-180 DT-13
guard) starts appearing here from the build dispatch on.**

**★ STATE / PENDING.** Five commits ran, were verified at the objects, and are pushed to origin:
`910a998e9b` (design pass), `31b3dba6ca` (desk sim), `61a8ed750f` (pre-fit gates), `bd84d796b6`
(OI-176 fold assignment: 326 stems / 324 groups / 5 folds, duration spread 1.11 %), `dcd1b64349`
(OI-177 count inventory: 18,418 labels / 16,372 pairs / 1,720 key changes; §4.3 sensitive cells
counted — three sit below the ratified threshold 20, as the desk sim anticipated). **NEW ROW OI-186**
(CC-found: `compare_rn.extract_quality` coarse on WiR `/o` and figured-bass slashes — binds the
fit-event normalization; a separate read-only check owed on whether rn_agree grading is affected) —
the row is on disk, rides the next commit. **The ACTIVE dispatch is `cc_instruction_wir_alignment_probe.md`** — the OI-184 establishment probe
(read-only, measure-only; its commit also carries the on-disk OI-186 row and this state line). After
its report is verified: the fit-event dispatch under the ratified OI-176/OI-177 protocols (its
normalization design must respect OI-186(a)). OI-179 (the ground-truth ceiling): the literature half is ANSWERED — no
published inter-annotator agreement figure exists for classical symbolic Roman-numeral analysis
anywhere in the field, so the 87-stem BCMH measurement would be novel; BCMH is inspected at the files
(independent origin, single reading, NO annotator record anywhere; the 2023 JEP:HPP Method section
adds corpus statistics but no annotators; the sole remaining route is asking the PeARL lab); the
measurement instrument is NOT built — read-only, buildable whenever the user wants it. OI-181 is
discharged by the factorization doc's §6. OI-182/OI-183 (bridge constants; scoring-model doc symbol
gaps) are open, low, untouched.

**★ METHOD REMINDERS.** Verify every CC claim at the objects (CC hallucinates; this arc's practice
held). The user runs Cowork under "do not bash for reading local files" — host Read/Grep/Glob for
repo text; sandbox bash only for PDFs/computation/file management. No self-invented labels or
abbreviations. Every behavior change is user-ratified (#14). The presentation-layer conditions
attached to decisions (1) and (4) — the published un-rounded modal reading and the published ornament
labels — are PART of the ratified record; do not let them drop out of the build.

*(The superseded 2026-07-17 session-close block was moved verbatim to `cowork_handoff_archive.md` by
the 2026-07-19 design-pass commit `910a998e9b`.)*

---

## ⛔ STANDING RULE: THE FULL DECISION SURFACE BEFORE ANY CHOICE QUESTION (user mandate 2026-07-05)

**Never present the user with options before the ENTIRE situation has been explained in a message the
user has actually seen.** Mechanism note (the failure that made the rule): Cowork prose written between
tool calls is summarized, not shown verbatim — so an explanation "just before" a question widget may
never reach the user, and the question arrives blind. The rules:
1. The decision surface (what is being decided, the background, each option's meaning, risks both ways,
   the recommendation and why) is delivered as user-visible text FIRST — via the verbatim message
   channel or as the turn's final response.
2. For consequential decisions (ratifications, adoptions, retirements, checkpoint rulings), the choice
   question goes in a SEPARATE, LATER turn — the user reads first, then is asked.
3. A decision answered blind is voidable: re-present the surface and re-confirm.
(First application: the 2026-07-05 verdict-14 + 2.2c ratifications were re-presented and re-confirmed
after this rule was made.)

---

## ⛔ STANDING RULE: INSTRUCTIONS ARE WRITTEN JUST-IN-TIME — ONE DISPATCHED AT A TIME (user mandate 2026-07-02)

**Do NOT write CC instructions ahead of need.** Pre-written instructions go stale (their premises change under
them), risk being skipped, and risk out-of-order execution. The rules:
1. **At most ONE instruction is dispatched/being-executed at a time** (single CC, single worktree unless the user
   explicitly sets up a second).
2. **The NEXT instruction is written only when its predecessor's report is ratified** and it is actually the next
   dispatch — never speculatively.
3. **The dispatch QUEUE is a plan, not files:** upcoming work is recorded as plan lines (roadmap / STATUS "next"),
   not as pre-written instruction files.
4. **Any instruction file that exists but is not the active dispatch carries a `⏸ PARKED` banner** and MUST be
   revalidated by Cowork against the then-current STATUS/HEAD immediately before dispatch, receiving a dated
   DISPATCH note. CC must not execute a parked instruction without that note.
5. **NO MID-FLIGHT STEERING (user, 2026-07-05): a running CC is never interrupted or relayed to** —
   interruptions have several times proven disastrous. Every instruction must therefore be
   SELF-SUFFICIENT: all foreseeable forks carried as in-instruction STOP/branch rules; anything not
   covered waits for the report and is ruled at verification. The only mid-run channel is the one CC
   itself opens (its own STOP question), answered when CC asks.
   *(As of 2026-07-04: NO parked instruction files — the formerly-parked gap-analysis and Wave-1 instructions
   both executed and were ratified (sessions 21e/21i/21f). Active: `cc_instruction_c1_reliability_instrumentation.md`
   — see the START HERE header.)*

---

## STANDING RULE FOR COWORK (read every session)

**Cowork writes instruction files. CC executes them. Never the other way around.**

- When the user says "go", "do E2b", "execute", or similar: the response is
  "The instruction is ready at `cc_instruction_X.md` — give it to CC."
- Cowork MAY: read source files **via the file tools (Read / Grep / Glob) — NOT bash** (see the NEVER-BASH
  standing rule below), write `.md` instruction files, update `cowork_handoff.md` / `STATUS.md` summaries after CC reports.
- Cowork MUST NOT: spawn agents that run build commands or modify `src/` files;
  use Edit/Write tools on anything under `src/`; use bash redirects on source files.
- Violating this rule has broken the codebase twice (E1, E2b). Do not do it again.

---

## ⛔ STANDING RULE: COWORK MUST NOT HALLUCINATE OR ASSUME — VERIFY AT SOURCE (user mandate 2026-06-21)

**The same rule Cowork imposes on CC applies to Cowork itself.** Verified facts only.

- **Never assert a fact, number, file path, line, key/tonic, or claim from memory or plausibility.** If it is
  not verified this session at the committed object (`git show <hash>:path`) or a fresh read, it is NOT a fact —
  say "I need to verify" and verify, or label it explicitly as unverified.
- **Numbers and identifiers re-state, they don't persist.** Re-confirm baselines, hashes, tiers, corpus
  identities each time; do not carry a remembered figure forward (the `kma_abs`/`Gmin` slip — Cowork wrote
  "stable Gmin" for bwv40.8 from the screenshot label without verifying; the real key was F minor; CC caught it).
- **When instructing CC, only put facts Cowork has verified into the instruction** — an unverified detail in an
  instruction can trigger a false stop or mislead. Mark anything provisional as `[prov]`.
- **Distinguish "CC measured it" from "Cowork verified it."** Relay CC's measurements as CC's; verify the
  load-bearing ones at source before building on them. Flag what could not be verified (e.g. shell congested).
- This mirrors CLAUDE.md's "never hallucinate or guess, verified facts only — better ask first if unsure."

---

## ⛔ STANDING RULE: NEVER BASH FOR LOCAL FILES — FILE TOOLS ONLY (user mandate 2026-06-26)

**The Cowork shell (`bash`) reads the working tree through a virtiofs+FUSE mount that can serve a STALE cached copy.**
Verified 2026-06-26: `bash`/`wc` showed `note_model.h` truncated to 158 lines (a June-21 snapshot, 8445 bytes) while
the real file on disk was 235 lines (12686 bytes); the Read tool showed it correctly. This silently corrupted a
test-adequacy audit (the audit agents "found" missing tests — e.g. the L2 clip CP1–CP7 suite — that actually exist),
and triggered a false "the tree is corrupted" alarm. **The file tools (Read / Grep / Glob) read the LIVE disk via a
different path and are correct.**

- **Local file CONTENT, existence, line counts, searches → ALWAYS the file tools (Read / Grep / Glob).** NEVER `bash`
  `cat` / `wc` / `grep` / `sed` / `head` / `tail` / `git status` / `git diff` on working-tree files. *(Supersedes the
  older "read source via grep/cat/sed -n" line in the first standing rule above — that path is the stale one.)*
- **`bash` is permitted ONLY for read-only git OBJECT queries, BY EXPLICIT SHA from CC's commit report** (option B,
  user-ratified): `git show <sha>:path`, `git show --stat <sha>`, `git cat-file`, `git diff <shaA> <shaB>`. These are
  content-addressed and **self-verifying** — a stale/unsynced object errors loudly (`bad object`), never returns
  silently-wrong content.
- **NEVER trust `git rev-parse HEAD` / `git status` / `git log`(branch tip) for "what is current"** — those read
  mutable refs/index that can be stale. Take the SHA from CC's report, read by that SHA, corroborate with a fresh
  file-tool read.
- A `bad object` / missing-object error = a **staleness signal → surface it, do not guess.** Mount refresh is
  host-side only (CC `touch`es the file on Windows, or restart the session).
- Root cause is method, not a product bug to wait on: the bash sandbox is a Linux VM sharing the folder via
  virtiofs+FUSE; the file tools take a separate, live path.

---

## ⛔ STANDING: TWO DEFERRED STRUCTURAL REFACTORS — DO NOT FORGET (user mandate 2026-06-14)

The foundation (Stages 0–2 hygiene/tests/unification/reliable-data + the Stage-3 oneshot decoder) was
completed byte-identically BEFORE any inference improvement. **TWO structural refactors were deliberately
deferred (not skipped) and must NOT be forgotten** — the user explicitly asked that these stay tracked:

1. **Physical file-split (Stage 3.5)** — split `chordanalyzer.cpp` (~3679 lines) into files along the
   now-real layer seams + rename the iteration-vocabulary APIs (`applyIter8691Pedal` → descriptive). The
   layers are LOGICALLY clean but not PHYSICALLY split. Deferred until the layer boundaries stabilize so
   we split once. *Status: PENDING — re-evaluate when Stage-4/6 layer touches settle.*
2. **Dissolve the post-hoc gate-correction layer (Gates A–L) — Stage 5.** The gates are still
   load-bearing (3.4 found none cleanly retirable; beam-1 is numerically the old pipeline). They are
   scheduled to dissolve into fitted weights at **Stage 5 (weight fitting)**, which the roadmap places
   AFTER Stage 4 (key). *Status: PENDING Stage 5 — the gates remain a known structural debt until then.*

Neither is a prerequisite for the current Stage-4 key-inference work (key axis is separate from the
chord-axis gates; every Stage-4 step holds the gate byte-identical 53/24/53 — the ratified current gate; the older
57/23/57 was a stale presentation corrected in the 2026-06-26 doc-truth pass). But they are **owed** —
surface them at every Stage-4/5/6 planning checkpoint until done. Both are also in
`docs/implementation_roadmap.md` (3.5, Stage 5).

---

## ⛔ STANDING OBJECTIVE: FULL TEST COVERAGE — every code path regression-tested (user mandate 2026-06-21)

A near-term, owed objective: **every path/branch in the code should be exercised by a regression test.** Tracked,
not yet a standalone task. How it is discharged:
1. **Per-layer, inside the upstream-first sweep (the primary mechanism):** every rebuilt layer ships with **full
   coverage of its new paths** as part of its implementation gate — not just the correctness cases (e.g. layer-1
   T1–T8) but every branch of the new code. Don't ship a layer with uncovered paths. This accretes coverage
   layer-by-layer as we rebuild, avoiding a giant retroactive effort.
2. **Regression safety net during transition:** the snapshot tests + the per-event oracle-root metric + the
   existing unit suites are the net that catches unintended changes while a layer is being replaced. Do NOT
   exhaustively cover code that is about to be deleted/replaced — cover the *stable* code and each *new* layer.
3. **A coverage MEASUREMENT pass (the concrete near-term step):** instrument line/branch coverage on
   `composing_tests` + `notation_tests`, baseline where we are, and rank the untested paths — so we know the gaps
   rather than guessing. Prioritise stable code + each rebuilt layer; deprioritise soon-to-be-replaced code.

Surface this at each layer's sign-off and at sweep checkpoints until full coverage is reached.

---

## ⛔ STANDING RULE: ALL DOCUMENTATION ALWAYS IN SYNC — treat doc drift like a failing test (user mandate 2026-06-21)

**Documentation is a first-class artifact, kept in lockstep with the code — exactly like regression tests and
code comments.** No ratified change is "done" until *every* affected doc reflects the new reality, in the same
increment. Doc drift is a defect, not a backlog item.

Scope of "documentation" (all of it):
- **Canonical tracked docs (CC's domain, committed WITH the code):** `ARCHITECTURE.md`, `docs/implementation_roadmap.md`
  (the single stage tracker), `docs/layer_architecture_audit.md`, `docs/scoring_model.md` (already sync-mandated
  by CLAUDE.md — this rule generalizes that discipline to *all* docs), and any other `docs/*.md` the change touches.
- **Code comments / remarks:** stale header/inline comments are doc drift too (e.g. the verified-wrong
  `regiontoneprimitives` "4 quarter notes" header — actually `Fraction(4,1)` = 4 whole notes).
- **Cowork design docs (Cowork's domain):** the `cowork_*` layer-design + target-architecture docs must be moved
  to an **as-built** status once a layer lands (the signed design becomes the as-built record, not a stale target).

**Per-layer step (added to the sweep discipline):** after a layer is ratified — *before moving to the next layer* —
sync ALL affected documentation: the canonical tracked docs (CC, committed alongside), the code comments, and the
Cowork design docs (to as-built). This is the architecture analog of the `scoring_model.md` sync rule and rides in
the same checkpoint as the coverage gate. A layer is not closed until it is correct, covered, **and documented**.

**Caught 2026-06-21:** layer 1 (note model, `e30bb45a4f`) shipped with **zero** canonical-doc updates — verified:
0 mentions of the note model across the entire `docs/` tree or `ARCHITECTURE.md`, which still describe the old
segment-first pipeline. This rule exists so that gap is closed now and never recurs.

---

## ⛔ STANDING RULE: TOTAL UNIFICATION — every build increment reports reuse-vs-new + what retires (user mandate 2026-06-22)

The project objective is **one path per concern — no permanent duplicate/redundant implementations.** A *temporary*
coexistence during a transition (a new isolated module running beside the old path until it is wired in) is fine; a
*permanent* second path for the same job is not.

**Every CC implementation/build instruction Cowork writes MUST require, and every CC build report MUST contain:**
1. **Reuse-vs-new** — exactly which existing code the increment reuses, and which pieces are newly written (and why
   a new piece was needed rather than reusing/extending an existing one).
2. **What retires** — which existing path this work makes redundant, and when it is removed (now, or named as the
   retirement step — e.g. "the old resolver retires at the wiring increment"). Nothing is left as a permanent
   duplicate by silence.
3. **Shared primitives, not bespoke copies** — a capability several layers need (a pitch-context builder, a
   best-sequence/Viterbi routine, a key-distance helper) is built once and reused, not re-implemented per layer.

**Cowork verifies this at source** on every increment (does the new code duplicate an existing path? is the
retirement real or deferred-forever?). A permanent duplicate path is a defect, like doc drift or a coverage gap.

---

## ⛔ STANDING RULE: KNOWLEDGE-BASED CODING ONLY — no assumption-based production code; exploratory measurement is the path (user mandate 2026-06-23)

**Production code is written only on MEASURED knowledge, never on an assumption or an untested attribution.** When the
evidence a build decision needs is not in hand, the mandatory move is **exploratory** — a read-only diagnostic /
measurement that *earns* the knowledge — BEFORE any production logic is written on the belief. Building production code
on "we think X will work / we think the residual is Y" and hoping is forbidden; gathering the cheap evidence that turns
the belief into a fact is required. **Exploratory / diagnostic code is explicitly encouraged** (decode-only flags,
graded measurements, decompositions) — it is how the knowledge is obtained, and it is read-only / production-byte-identical.

This is the build-time companion to "verify at source" and "investigate by default": those govern *claims*; this governs
*code*. A measurement that **disproves** an assumption is a success, not wasted work — it stops a wrong build (e.g. the
fair-key test that showed wiring the key would NOT close the L4 chord-root gap, *before* any C/wiring spend). Every
layer increment is therefore **measure → decide → build**, the measurement gating the build, never the reverse.

---

## ⛔ STANDING RULE: INVESTIGATE BY DEFAULT — NEVER ASK "investigate vs proceed" (user mandate 2026-06-14)

**Whenever a step could be investigated/measured BEFORE committing, ALWAYS investigate first — and do NOT
present it to the user as a choice.** The user's standing answer to "investigate or go in some direction"
is *always investigate*, so asking wastes a turn. This is the never-guess principle's logical end: gather
the cheap evidence before any commitment, by default. When Cowork hits such a fork, it writes the
investigation/measurement instruction directly (read-only / byte-identical where possible).

**What Cowork MAY still bring to the user (the only legitimate questions):** (1) ratification of a
*measured* result (accept/proceed once the evidence is in — the user's deliberate-behavior-change call);
(2) a pure VALUE / PRIORITY / RISK-APPETITE / PRODUCT-PHILOSOPHY call that **no investigation can settle
AND that has no investigate option**. Never a "should we investigate first?" question — the answer is yes.

---

## ⛔ STANDING RULE: PREDICATES MUST BE QUALIFIED IN SPECS (user mandate 2026-06-24)

**When writing or reviewing any spec, every predicate/pointer word names its argument.** Many words are *two-place*
("uncertain" → about *what*; "defers" → *what* to *where*; "fits" → by *what measure*; "close"/"enough"/"in view" → by
*what test*; "prevailing"/"plausible"/"spurious" → by *what rule*) and are easy to write with the second place left
implied — which is exactly where specs hide holes. The mechanical check: force each such word to be followed by the
thing it points at; if that forces a phrase the prose does not supply, the predicate is **unqualified** — fix it.
Deferring a *numeric value* to tuning is allowed; leaving the *argument or its decision structure* unnamed is not. Home
of the rule: `cowork_design_doc_template.md` (writing standard). Method + worked examples: `cowork_spec_language_sweep.md`,
`cowork_layer3_spec_language_sweep.md`.

---

## ★ STANDING METHOD: LAYER-BY-LAYER AUDIT ONCE PIECES ARE IN PLACE (user, 2026-06-14)

**The architectural payoff and the back-half verification model:** *as soon as every piece of the puzzle
is in its CORRECT layer, we go layer by layer and ask whether that layer is correct AND complete —
focusing on each layer's single responsibility and ignoring the other layers.* This is only possible
because the layering work (Stages 0–3) made the seams real (oracle = vertical, competition/function
layer, post-scoring gates, key resolution, section/KeyArea, functional labeling). It is the goal the
whole refactor served, and it directly motivates finishing the TWO deferred refactors above (a layer
can't be cleanly audited while it's physically tangled in `chordanalyzer.cpp` or while its responsibility
is smeared across a post-hoc gate layer). **Method, when invoked:** pick a layer, state its single
responsibility, audit correctness + completeness against THAT responsibility only (its inputs assumed
correct, its consumers ignored), pin gaps as that layer's obligations. Apply per layer as the back half
(Stages 4–6) lands each piece in place.

**★ SHARPENED (user, 2026-06-15):** this comprehensive per-layer audit ("does this layer serve its purpose
**fully, correctly, comprehensively**?") is the back-half **ACCEPTANCE** review and is **GATED on the
layers actually existing as single-responsibility units** — i.e. it waits until the TWO deferred refactors
(chordanalyzer.cpp file-split + gate-layer A–L dissolution) have made the seams physical. Auditing now would
be auditing a moving, tangled target (e.g. chord analysis is still entangled with a stateful temporal
context, as the J-key-iii re-emission bug showed — `analyzeChord` is not yet a pure function of its layer's
inputs). **Distinct from the ongoing per-change BUILD-TIME verification** (every CC report verified at
source + measure-first checkpoints), which CONTINUES the whole way and is what catches regressions during
construction (it caught the re-emission artifact before commit). Acceptance audit = deferred to clean
layers; build-time verification = always on. They are complementary, not redundant. **Build-time
verification lesson folded in (2026-06-15):** when a change adds a NEW consumer of an existing data
structure, assert **same-input → same-output** as an explicit invariant (the missing mirror of the
J-key-iii §5 key invariant — a chord-axis "key-unchanged region ⇒ byte-identical chord" check would have
caught the re-emission bug one checkpoint earlier).

---

## What this project is

MuseScore Studio. The active development area is `src/composing/`, which implements
harmonic analysis (chord detection, inversion scoring, key inference). The main file
is `src/composing/analysis/chord/chordanalyzer.cpp`. The bridge between the composing
module and the notation layer is `src/notation/internal/notationharmonicrhythmbridge.cpp`.

Mandatory reads at the start of every session:
- `C:\s\MS\STATUS.md` (header only, first ~10 lines) — current baselines and HEAD commit
- `C:\s\MS\build_and_test.md` — all build/test/tool commands

**When CC returns a report**, always do this before evaluating it:
1. Re-read the instruction file that CC was given (listed in "Next CC task" in Current state below)
2. Then read CC's report

CC's report references task numbers, design decisions, and deviations that only make sense against the original instruction. Evaluating the report without re-reading the instruction means accepting CC's framing uncritically — which is exactly the failure mode we guard against.

**THE WORKING METHOD (canonized 2026-06-12, user mandate — these principles produced
Stages 0–3.1b without a single unplanned regression; they are not optional):**

A. **Pin before you change.** No layer/gate/method is built upon until its current
   behavior is pinned (tests) and its instruments verified (metrics, corpora, source
   identity). Instruments first, measurements second, changes third.
B. **Byte-identity bridges for every restructure.** A refactor earns zero improvements;
   its gate is 0-diff across corpora (all relevant configs), snapshots, and suites,
   with FP near-tie canaries unmodified. Golden refreshes as a reflex are FORBIDDEN —
   a diff is a stop, not a chore.
C. **Behavior changes are deliberate, measured, ratified.** Never shipped as a side
   effect (the 3.1b lesson). The answer-delta is measured BEFORE the commit is
   proposed; ratification decides on data.
D. **Never guess — investigate or state the unknown** ([probe]/[code] tags, explicit
   Unknowns sections). Binds CC and Cowork equally. Read the call site, not just the
   qualifier (the completeTriad lesson).
E. **Stop conditions are designed in advance and honored.** The system's best moments
   were stops (snapshots 0/11; DCML-worse; tracked-junk deviation). A tripped stop is
   the process succeeding.
F. **Falsified decisions get re-decided, and their evidence gets committed** (Q1 →
   `p3_granularity_ab_3_1b.md`; the cap archaeology; the M3 reconstruction). Dead ends
   are documented so they are never re-walked.
G. **One change-class per commit, explicit staging, every commit independently
   verified** (`git show --stat` + host-side reads against the claims).
H. **Errors are owned by name** — Cowork's included (the snapshot-harness premise, the
   whole-score prior, the relay gaps). Ownership is what keeps the ledger honest.

**STANDING RULE — CC trust model (made permanent 2026-06-10, user mandate):**
1. **Never fully trust CC.** CC can hallucinate, guess, and present guesses as findings.
   Every consequential CC claim gets independent verification before acceptance:
   commit contents via `git show --stat`, code claims via host-side Read/Grep of the
   actual source, numeric claims against recorded baselines. Track record this session:
   CC has been right where verifiable most of the time, but produced at least one
   guessed mechanism stated as fact ("parallel batch path resolves ties
   nondeterministically" — wrong, batch_analyze has no threading) and one
   imprecise-memory claim (junk files "M/regenerated" — that one was Cowork's own
   stale-sandbox error; verification cuts both ways).
2. **CC does not hold the bigger picture — Cowork does.** CC optimizes the task in
   front of it. Cross-cutting consequences (gate semantics, baseline integrity, layer
   architecture, re-baseline bundling, what a finding means for Stages 2–6) are
   Cowork's to evaluate. When CC proposes a disposition for a finding ("log it for
   later", "not a blocker"), treat that as input, not a decision.
3. Both rules also bind Cowork's instructions to CC: the never-guess /
   investigate-or-state-unknown rule (introduced Stage 1d) is standing for ALL future
   instructions, not per-instruction boilerplate.
4. **All Cowork adjustments/approval-conditions go in INSTRUCTION FILES, never only in
   chat replies.** Chat-relayed adjustments were lost twice (2026-06-10: the H2
   extension + 326-fact rider after the hygiene pass; the chordanalyzer.h:62 comment +
   diagnose context banner after 2.3). Instruction files have a 100% delivery record.
   "Approved with additions" means: write the additions as an addendum instruction
   file, then approve.
   **"HELD" is now unambiguous (2 slips: 3.3, metric-L0L1): "held for Cowork" =
   `git add` is OK, `git commit` is NOT, until a ratification/approval file says so.
   A pre-authorized ship that may commit-on-green-proof will say exactly that.**
5. **Cowork reads every CC report IN FULL before ratifying or approving its commits.**
   Verification-against-primary-sources does not substitute for the report's Findings/
   Unknowns/caveat sections — CC under-weights its own findings in chat summaries
   (precedent: the 326/353 fact, the preset headline), and an unread caveat went
   unanswered at the Stage-3 design ratification (the bwv320 dual-classification
   question, caught only in the 2026-06-12 retrospective sweep). Chat summaries are
   navigation aids, not the artifact.

---

## Two worktrees

- `C:\s\MS` — **master** branch (main working tree — use this for all development)
- `C:\s\MS-llm-triage` — `llm-triage` branch (separate worktree, only for LLM triage work)

All active development is on **master**. Always confirm which worktree CC is in before giving it instructions.

---

## Standing rule — CC instruction preamble (MANDATORY, every single CC session)

CC starts with ZERO context every time. Every instruction to CC must open with:

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
> `C:\s\MS\build_and_test.md`
>
> **If this session touches scoring logic in `chordanalyzer.cpp`** (templates, bonuses,
> guards, gates, score matrices): also read `C:\s\MS\docs\scoring_model.md` before
> making any changes. The doc explains why each term exists and what invariants must
> not be broken. Any commit that changes scoring logic must also update that doc.
>
> **Current state:** Branch `master`, HEAD `f9ba22157d`, working tree clean.
> BIR baselines (lenient-OR): Baroque BIR=true=25, BIR=false=16; Jazz BIR=true=36,
> BIR=false=10. Hard stops: Baroque BIR=false ≤ 25, Jazz BIR=false ≤ 13.
> Tests: 407/407 composing, **52/52 notation (fully green)**, pipeline_snapshot
> 11/11 (1 skipped, no goldens touched).
> Mismatch report: Jazz 130 items; see chord_mismatch_report.txt.
> Roman numeral baseline (HEAD `f3e0f5f72c`, 9 non-Bach corpora, 61,233 regions):
> rn_agree=27.6% (16,905/61,233); corrected classifier: key_disagree=15.4%,
> quality_disagree=6.3%. Root_agree=49.3% parity check. Hard stop: rn_agree
> must not drop below 27.6%.
>
> **Unification is complete.** Both parameter divergences are resolved: D1
> (`excludeLookAheadOnDenseStart`) is intentionally divergent and load-bearing (batch
> `true`, bridge `false`); D2 (`pass1MinDistinctPcsForCandidate`) is unified at `1` on
> both paths (`4d881e7418`). STEP 1 (`3d80d0a91d`): the dim7 characteristic bonus now
> requires the complete diminished triad, and Gate J treats a complete root-position
> diminished triad over a sounding dominant root as an inverted V7 — Jazz BIR=true
> 56→33 (−23), Baroque BIR=false 25→23 (−2).
>
> Hard stops always: Baroque BIR=false > 25, Jazz BIR=false > 13, any test
> regression beyond the 2 known Corelli notation failures.

This preamble goes before EVERY task description, no exceptions.

---

## Standing rule — Investigation-first before implementation (MANDATORY for Cowork)

**Before writing any CC implementation instruction that touches existing scoring
mechanics**, either:

1. Read the relevant source code here in Cowork first (use the Read tool on
   `chordanalyzer.cpp` at the specific section), **or**
2. Write a pure read-and-report instruction first — CC reads and reports, no code
   changes — then write the implementation instruction based on that report.

"Touching existing mechanics" means: adding a template near an existing one,
modifying a bonus/gate/guard, changing a threshold, or anything where an existing
scoring term might interact with the proposed change.

**Why:** B2 took 4 attempts and B3 was reverted because implementation instructions
were written based on incomplete understanding of existing code. The `dim7CharacteristicBonus`
rotation-selection role was only discovered mid-task. An investigation pass first
would have caught this before a single line was written.

**The C1 investigation instruction is the correct model.** Pure read-and-report,
no edits, produces a design proposal. Only after the report comes back does the
implementation instruction get written — based on actual findings, not assumptions.

---

## Standing rule — Visual inspection before debugging (MANDATORY for BIR=false cases)

Before investing CC debugging effort on any BIR=false case, **look at the score with
our annotations first.** A single image reveals whether the error is isolated or
systemic; this determines whether a targeted fix is worthwhile or whether the case
should be accepted as a Phase E residual.

**How:** Ask the user for an annotated score image, or use
`tools/inject_dcml_rn.py` to overlay DCML Roman numerals alongside ours, then open
the resulting file in MuseScore. Even our annotations alone (without DCML ground truth)
expose systemic patterns (rootContinuityBonus over-stickiness, inversion mis-labeling,
Roman numeral errors) that the BIR metric cannot see.

**Decision rule based on the image:**
- **One wrong region, rest of score looks correct** → targeted fix is likely worth it.
  Proceed to CC debugging.
- **Multiple wrong regions sharing a mechanism (e.g. tonic stickiness throughout a phrase,
  or consistent inversion errors)** → systemic; check whether it's a known dead end
  (Iter 98 / Phase E). If yes, accept as residual. If not, characterise the scope before
  committing to a fix.
- **Widespread unrelated errors** → complex residual; accept, move on.

**Introduced 2026-06-04** after bwv14.5 image review showed rootContinuityBonus
stickiness in opening measures + an unrelated m5 post-scoring promotion + Roman numeral
labeling errors — three distinct issues in one score. Score image identified all three
faster than three rounds of CC programmatic debugging.

---

## Windows Snap fix — do not revert

File: `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`
Function: `calculateWindowSize()`

Two lines that set `ptMinTrackSize` equal to the full monitor work area were removed.
This prevented Windows Snap from working on maximised MuseScore windows.
`ptMaxSize` and `ptMaxPosition` are kept. `ptMinTrackSize` is intentionally left unset.

The fix is committed as a local-only branch in the muse submodule (`fix/windows-snap-ptmintracksize`
at `b9604805a`). The parent repo's master correctly pins the submodule pointer to this commit.
**Do not restore the `ptMinTrackSize` lines. Do not push the muse submodule to upstream.**

This is documented in `C:\s\MS\CLAUDE.md` which CC reads every session.

---

## Known CC/VS Code integration issues

**Stale `git index.lock`** — When CC loses contact with a running git process (a known
VS Code integration bug), `.git/index.lock` is left behind (0 bytes). Symptom: git
commands fail with "Unable to lock the index". Fix: verify no git process is running
(`tasklist | grep git`), then delete `.git/index.lock`. Safe to delete if file is
0 bytes and no git process is running.

**Silent disconnect — three distinct triggers (diagnosed 2026-05-14 from VS Code logs)**

VS Code sets the CC session to `idle` (handing control back to user) in these situations,
while the CC process keeps running invisibly. Dangerous to submit new tasks without waiting.

**Trigger 1 — Non-zero exit code:**
A bash command returns non-zero (failing tests, grep with no matches, etc.). The extension
sees this as an error and marks the session idle. CC keeps running.
Fix: append `; echo "exit:$?"` to every command that may return non-zero. The echo always
returns 0, so the extension sees a clean result.
- BAD:  `./pipeline_snapshot_tests.exe --gtest_filter='*name*'`
- GOOD: `./pipeline_snapshot_tests.exe --gtest_filter='*name*'; echo "exit:$?"`
- BAD:  `grep -n "pattern" file.cpp`
- GOOD: `grep -n "pattern" file.cpp; echo "exit:$?"`

**Trigger 2 — stream_idle_partial (long bash output):**
When a bash command produces large output and CC takes >~15 seconds to process the result,
the API stream goes idle between chunks. The extension logs `[WARN] [Stall] stream_idle_partial`
and marks the session idle. CC is still running and will eventually complete.
Fix: break long commands into smaller steps that produce incremental output. Pipe through
`head -N` to limit output size. Write large results to a file and read separately rather
than capturing in one bash call.
- BAD:  `batch_analyze <score> --dump-regions notation`  (may produce thousands of lines)
- GOOD: `batch_analyze <score> --dump-regions notation > /tmp/out.json; echo "exit:$?"`
         then `head -50 /tmp/out.json`

**Trigger 3 — stream_idle_partial (API latency, bytesTotal=0):**
When the Anthropic API takes >15 seconds to send the first token of a response (server load,
network hiccup), the extension logs `stream_idle_partial lastChunkAgeMs=15xxx bytesTotal=0`.
This can silently drop the panel even though CC recovers and keeps running. No reliable
prevention — it's server-side latency. If the panel goes silent mid-task without any bash
errors, this is likely the cause. Check the VS Code output log before resubmitting.

Build commands (setup_and_build.bat) are launched via PowerShell Start-Process which
isolates the exit code — less affected by trigger 1.

---

## .vscode/settings.json — muse submodule noise

VS Code detects `muse/.git` (submodule gitdir pointer) and prompts to open it as a
separate repository. Two settings suppress this in `C:\s\MS\.vscode\settings.json`:
- `"git.detectSubmodules": false` — stops VS Code treating submodules as separate SCM providers
- `"git.ignoredRepositories": ["C:\\s\\MS\\muse"]` — belt-and-suspenders ignore by path

If CC hasn't applied these yet, ask it to edit `.vscode\settings.json` accordingly,
then Ctrl+Shift+P → "Reload Window".

---

## Build commands (quick reference)

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Tests (run from ninja_build_rel/)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe

# Corpus quality check
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Mismatch report location
src/composing/tests/chord_mismatch_report.txt
```

---

## Standing practices — build and corpus hygiene

Two silent failure modes that produce plausible-looking but wrong results:

**Stale build** — if the working tree has uncommitted changes and the binary
hasn't been rebuilt, corpus analysis runs against the old logic. BIR numbers
will look identical to the last clean run but the characterization is wrong.
**Always rebuild before any corpus run when the working tree has been modified**,
or when there is any doubt about whether the binary matches the source.

**Stale corpus output** — `analyze_inversion_errors.py` reads whatever JSON
files are already in `tools/corpus/`. If `run_bach_preset.py` was not run
first (or was run against a different binary), the analysis silently reads
old results. **Always run `run_bach_preset.py` immediately before
`analyze_inversion_errors.py`** — never rely on corpus JSON files left over
from a prior session or a prior build.

Canonical corpus analysis sequence (never skip steps):
```
# 1. Rebuild first if working tree has changes
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# 2. Regenerate corpus (Baroque)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus

# 3. Analyse (reads the freshly written JSONs)
cd C:\s\MS && python tools/analyze_inversion_errors.py

# Repeat steps 2–3 for Jazz if needed (reuses same output-dir)
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## Key files

| File | Purpose |
|------|---------|
| `src/composing/analysis/chord/chordanalyzer.cpp` | Main analyzer — all scoring logic |
| `src/composing/analysis/region/regionanalyzer.cpp` | Canonical region orchestrator — Pass 1/2/2b, absorb, backfill, restamp |
| `src/notation/internal/notationharmonicrhythmbridge.cpp` | Bridge — thin wrapper over `regionanalyzer` |
| `docs/llm_integration.md` | LLM / Claude Composer full design document |
| `docs/quality_observations_iter76.md` | R1–R5 recurring themes for Iter 79+ |
| `docs/score_inventory.md` | Score paths for all test/corpus files |
| `STATUS.md` | Current baselines and HEAD — read every session |
| `build_and_test.md` | All build/test/tool commands |
| `CLAUDE.md` | Standing rules for CC — read every session |
| `tools/analyze_inversion_errors.py` | BIR corpus check |
| `muse/framework/extensions/api/extapi.h` | Current extension API surface (v2) |
| `muse/framework/extensions/internal/extensionsconfiguration.cpp` | Path resolution for extensions/plugins |
