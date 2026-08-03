# The 23 decisions pending ratification (D-232…D-254) — complete entries

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** Found by the OI-207 residual second pass over the
> 5,204 unresolved clusters; entered into the register with status taken from the record only —
> RATIFICATION IS YOURS. Rendered character-identical to the register by its own entry renderer.
> The two judgments CC flagged as yours, not mechanical: D-243's superseded-in-fact status, and
> whether a handover document counts as a home for a working-protocol rule (the six handoff-homed
> entries — OI-266).


## Group K — Documentation governance

### D-232 — The section numbers are authoritative; the "Rule N" labels are a legacy flat numbering

> *The "Rule N" labels in §2.11–§2.12 are a legacy flat numbering of the coding/process rules and do not align with the
> §-numbers (and appear out of order); the **§-numbers are authoritative**. Read each "Rule N" as a local name for the
> rule stated beside it, not a cross-reference to a numbered list.*

**In plain words.** Where a coding or process rule in sections 2.11-2.12 carries a "Rule N" label, that label is only a local name for the rule beside it. The section number is what identifies the rule.

**Why.** The constraint that forced it, stated in the quote: the flat numbering does not align with the section numbers and appears out of order, so reading a "Rule N" label as a cross-reference sends the reader to the wrong rule.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:601-603`

**Provenance.** ARCHITECTURE.md:601-603 (stated as a standing reading instruction in the document itself)


## Group I — Module boundaries and code structure

### D-233 — Build and test commands run synchronously; one run, one result

> **Rule 14 — Shell discipline for long-running commands**
>
> All build and test commands must run synchronously (foreground). Never use background jobs or split output.

**In plain words.** Every build and test command is run in the foreground and its output is read whole. A command is never backgrounded, never killed and re-run differently, and never silently re-run: unexpected output is reported and instructions asked for.

**Why.** Derivation not recorded. The record states the rule and its correct/incorrect patterns (ARCHITECTURE.md:627-649) but not the incident or measurement that produced it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:623-625`

**Provenance.** ARCHITECTURE.md:623-625 (Rule 14) and :649 (the one-run-one-result statement)


## Group J — Presentation and output conventions

### D-234 — A chord symbol string must be valid under chords_std.xml; chords.xml is not relied on

> **Rule 16 — Do not rely on chords.xml**
>
> MuseScore has two chord description files:
> - `share/chords/chords_std.xml` — the active standard chord list used by default in all scores
> - `share/chords/chords.xml` — legacy file, likely deprecated, contains known bugs and inconsistencies with the parser
>
> When our formatter produces a chord symbol string, it must be valid according to `chords_std.xml` only. Do not add chord symbol strings that exist only in `chords.xml` — they will fail to parse correctly under the Standard chord style and may produce corrupted output.

**In plain words.** MuseScore ships two chord description files. Everything our formatter emits must parse under the active one, chords_std.xml. A string that exists only in the legacy chords.xml is not used.

**Why.** The measurement that decided it is cited in the record: `9sus` exists in chords.xml (id=134) and not in chords_std.xml, and under the Standard chord style it triggers `generateDescription()`, producing the corrupted `Fsussus9` render (ARCHITECTURE.md:672). The remedy named there is `sus(add9)`.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:664-670`

**Provenance.** ARCHITECTURE.md:664-674 (Rule 16), restated in the retired-session record at STATUS_ARCHIVE.md:2247


## Group F — Layer 3 — key and mode

### D-235 — Tonal-centre disambiguation may break a close tie but may not overturn a stronger raw winner

> The key-signature path uses a separate focussed `tonalCenterScore` formula for the
> final same-key-signature family decision, independent of the main scoring weights so
> both can be tuned without cross-interference. For diatonic family decisions, tonal-
> centre disambiguation is now guarded by the raw candidate score: it may break close
> same-key-signature ties, but it must not overturn a materially stronger raw winner.

**In plain words.** The same-key-signature family decision is scored by its own formula, separate from the main key weights. On diatonic families that separate decision is allowed to settle a near-tie, but a candidate that already wins the raw scoring by a clear margin stands.

**Why.** The constraint stated in the record: the two formulas are kept independent so both can be tuned without cross-interference; the raw-score guard bounds what the secondary formula may do. The measurement that set the guard's bar is not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2403-2407`

**Provenance.** ARCHITECTURE.md:2403-2407; the same guard is listed among the key-path scoring terms at :2480-2482


## Group G — Layer 4 — chord identity

### D-236 — Chord-symbol trust is per symbol, not a per-score preference

> **Per-symbol trust, not per-score preference.** A per-score toggle is explicitly
> rejected — too coarse-grained, since a single score may contain both trusted
> lead-sheet-style annotations and untrusted draft symbols.

**In plain words.** If written chord symbols are ever treated as authoritative input, the authority is carried by each symbol. A single switch for a whole score is rejected.

**Why.** The reason is stated with the decision: one score may carry both trusted lead-sheet annotations and untrusted draft symbols, so a per-score toggle is too coarse-grained (ARCHITECTURE.md:2598-2600).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2598-2600`

**Provenance.** ARCHITECTURE.md:2576 heads the section "Future: Authoritative Chord Symbol Mode"; the current rule is that written symbols are never analyzer input (register entry D-066)

### D-237 — Only a symbol marked trusted becomes analyzer input; an untrusted symbol is never read

> **Analyzer semantics:** Only when a `Harmony` element has `trusted = true` does it
> become boundary AND identity input for the harmonic region it opens. The analyzed
> root and quality are taken from the written symbol, not from note-based inference.
> Untrusted symbols remain comparison metadata only and are never read by the analysis
> pipeline.

**In plain words.** Under the planned authoritative-symbol mode, a written chord symbol opens a region and names its chord only when it is marked trusted. An untrusted symbol stays comparison metadata and the analysis never reads it.

**Why.** Derivation not recorded. The record states the semantics but not the evidence or constraint that fixed them.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2609-2613`

**Provenance.** ARCHITECTURE.md:2576 (the section is headed Future); register entry D-066 records the rule in force today

### D-238 — Two pitch classes may nominate a chord but may not finalize one; one pitch class may not

> Initial rule:
> - 2 distinct pitch classes may nominate a candidate set
> - 2-PC evidence alone must not finalize a chord without contextual support
> - 1-PC evidence is insufficient for independent chord resolution and may only
>   participate in continuity-preserving abstention logic

**In plain words.** In the monophonic fallback, a slice with only two distinct pitch classes can propose candidates but cannot settle the chord without context; a single pitch class cannot settle one at all and may only keep an existing reading alive.

**Why.** The reason is stated beside the rule: it avoids over-interpretation of isolated tones (ARCHITECTURE.md:2760-2761).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2754-2758`

**Provenance.** ARCHITECTURE.md:2724 heads the section "Phase 1b - Minimal Monophonic Fallback Without Chord Symbols"; ARCHITECTURE.md:3496-3503 records monophonic input as planned

### D-239 — Chord identity stays local; expansion is by one neighbouring region and is bounded

> **Bounded expansion in Phase 1b:**
> Chord identity should remain local. When a local group is too weak to resolve,
> the analyzer may expand by one neighboring region and re-score. Expansion is
> bounded and should stop when:
> - confidence crosses threshold
> - top-vs-second margin crosses threshold
> - the same winner survives repeated expansion
> - the hard expansion cap is reached

**In plain words.** When a group of notes is too weak to resolve on its own, the analyzer may take in one neighbouring region and score again. It stops as soon as confidence or the margin crosses its threshold, the winner repeats, or the expansion cap is reached.

**Why.** Derivation not recorded. The stop conditions are stated; the thresholds and the cap are left to be calibrated (see register entry D-240).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2763-2770`

**Provenance.** ARCHITECTURE.md:2724 (the Phase 1b section heading); the stop conditions are stated with the rule

### D-240 — The monophonic smoothing terms are tunable parameters, not prose-only rules

> These terms must be implemented as tunable parameters rather than prose-only
> rules.

**In plain words.** The margins and thresholds that govern the monophonic fallback's smoothing are implemented as named settings, so they can be changed and measured rather than being buried in prose.

**Why.** Derivation not recorded. The record states the requirement and names the parameters it produces, but not the incident or principle that forced it.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2780-2781`

**Provenance.** ARCHITECTURE.md:2724 (the Phase 1b section heading); the named parameters are listed at :2783-2790

### D-241 — The monophonic local-grouping problem is deferred to Phase 2

> The local grouping problem is intentionally deferred to Phase 2 because it is
> the hardest part of monophonic inference.

**In plain words.** Deciding how to group a single melodic line into harmonic units is left to the later, full monophonic engine rather than attempted in the minimal fallback.

**Why.** The reason is stated with the deferral: local grouping is the hardest part of monophonic inference (ARCHITECTURE.md:2810-2811).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2810-2811`

**Provenance.** ARCHITECTURE.md:2796 heads "Phase 2 - Full Monophonic Engine"

### D-242 — Vertical and monophonic raw scores are never compared directly

> The unified layer must not compare vertical and monophonic raw scores directly.
> The two engines use different evidence models and therefore require explicit
> confidence calibration.

**In plain words.** The layer that combines the two chord engines may not put their raw numbers side by side. The two engines weigh different evidence, so their confidences must be calibrated onto a common footing first.

**Why.** The reason is stated with the rule: the two engines use different evidence models (ARCHITECTURE.md:2839-2840). It is the same commensurability constraint the cross-layer confidence contract states generally (register entry D-032).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:2838-2840`

**Provenance.** ARCHITECTURE.md:2813 heads "Unified Orchestration Layer", part of the provisional phased plan recorded at :3498-3503


## Group C — Cross-cutting analysis contracts

### D-243 — The planning band for the vertical engine, and the corpora excluded from it

> For planning purposes, the current vertical tertian engine plus targeted texture
> fixes should be expected to plateau around 65–75% exact external root+quality
> agreement on **full-texture tonal corpora** (SATB choral, chamber, full piano
> accompaniment). This band applies specifically to region-centric DCML comparison
> methodology. Thin-texture corpora (Mozart piano sonatas, C.P.E. Bach keyboard,
> solo melody) are excluded from this target — they require a separate inference
> strategy and should not be compared against the same band. The When in Rome and
> music21-surface comparisons use different methodologies and are not directly
> comparable to this figure.

**In plain words.** For planning, the vertical engine plus texture fixes is expected to settle around 65-75 % exact root-and-quality agreement on full-texture tonal music, measured region-centrically against DCML annotations. Thin-texture corpora are outside that target and are not judged against it, and figures from other comparison methods are not comparable to it.

**Why.** The constraint stated in the record: the band is tied to one comparison methodology (region-centric DCML), and mixing methodologies is what makes a figure incomparable (ARCHITECTURE.md:3559-3564).

**Status.** SUPERSEDED IN FACT · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3556-3564`

**Provenance.** The band is stated at ARCHITECTURE.md:3556-3564. The governing measurement surface is now the robust unit ratified at R10-b (CLAUDE.md gate block (A)), whose figures are reported per preset on a different unit; no ruling names this band as replaced.


## Group O — Intonation

### D-244 — Choosing an interval family for an ambiguous sonority is deferred; fixed tables are used

> Another deferred design question is **which interval family to prefer for
> ambiguous sonorities**.  The current shipped tuning systems use fixed lookup
> tables (for example, 5-limit just intonation uses 9/5 for a minor seventh and
> 15/8 for a major seventh) rather than a style-aware policy that can choose
> between alternatives such as 5-limit dominant sevenths versus septimal
> "harmonic sevenths" (7/4), or other competing targets for altered/extended
> sonorities.  This is not specific to seventh chords — similar ambiguity also
> appears in tritones, minor sonorities, diminished/augmented chords, and larger
> extensions.  This choice architecture should be explored later, but it is not a
> current implementation target.

**In plain words.** When more than one pure interval could be targeted - a 5-limit minor seventh against a septimal one, and the same choice for tritones, minor and altered sonorities - the tuning systems keep their fixed lookup tables. A style-aware choice is left for later.

**Why.** Derivation not recorded. The record states the design space and that it is deferred, but not the measurement or constraint behind the deferral.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5069-5078`

**Provenance.** ARCHITECTURE.md:5077-5078 states it is not a current implementation target; the same deferral is recorded in the retired-session record at STATUS_ARCHIVE.md:2335

### D-245 — Voice role comes from staff position or explicit assignment; automatic melody detection is deferred

> Automatic melody detection is deferred. For now, voice role is determined by staff position
> or explicit user assignment — not automatic detection. Per-staff override of voice role is
> a future extension.

**In plain words.** Which voice counts as the melody is taken from where it sits in the score or from what the user says. Working it out automatically is left for later, as is a per-staff override.

**Why.** Derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5192-5194`

**Provenance.** ARCHITECTURE.md:5192-5194 states the deferral

### D-246 — Fixed-pitch instruments are deferred, and will never receive tuning offsets

> Fixed-pitch instruments (piano, organ, fretted guitar) are deferred — their handling is not
> yet implemented. When implemented, they will serve as absolute anchors that other
> instruments tune to, and will never receive tuning offsets themselves.

**In plain words.** Piano, organ and fretted guitar are not handled yet. When they are, they will be the fixed reference other instruments tune to, and will not be retuned themselves.

**Why.** The constraint is the instruments themselves: their pitch is fixed by construction, so a tuning offset cannot be applied to them (ARCHITECTURE.md:5293-5295).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5293-5295`

**Provenance.** ARCHITECTURE.md:5293-5295 states both the deferral and the eventual behaviour

### D-247 — An anchor note stays at 12-TET, is never split, and is excluded from drift and centering

> **Rules for anchor notes:**
> - **Zero tuning offset** — the note is left exactly at 12-TET.
> - **Never split** — anchor notes are not divided at harmonic boundaries.
> - **Not a FreeDrift reference** — in FreeDrift mode the anchor note is
>   excluded from the drift reference hierarchy (P1/P2/P3); it sits at 0 ¢
>   and other notes accumulate drift around it.
> - **Excluded from zero-sum centering** — other voices in the harmonic region
>   absorb the full centering correction; the anchor contributes zero.
> - Applies to the specific note carrying the Expression only — subsequent notes
>   on the same staff are not automatically anchored.
>
> **Priority:** Highest. Overrides all duration-based, context-based, and
> FreeDrift reference hierarchy rules.

**In plain words.** A note carrying the anchor expression is left exactly at equal temperament. It is not divided at a harmonic boundary, it is not used as the drift reference in FreeDrift, and it takes no share of the zero-sum centering correction. Only that one note is anchored, and the rule outranks every duration-, context- and drift-based rule.

**Why.** Derivation not recorded. The record states the rules and their priority but not the musical reasoning or measurement behind the priority.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5311-5323`

**Provenance.** ARCHITECTURE.md:5311-5323; the FreeDrift behaviour is restated at :5448-5453


## Group H — Layer 5 and Layer 6 — function, cadence, grouping

### D-248 — Tonicization labels are not implemented and are deferred

> - Tonicization labels (V/V, V/ii, V/IV etc.) — **NOT YET IMPLEMENTED**
>   (deferred; no `relativeRoot`/secondary-dominant field in
>   `ChordFunction`; requires standalone implementation first)

**In plain words.** Applied-chord labels such as V/V are not produced. The data structure has no field for the relative root, and the feature waits on a standalone implementation.

**Why.** The constraint is stated in the record: `ChordFunction` carries no `relativeRoot` or secondary-dominant field, so the label has nowhere to live (ARCHITECTURE.md:6002-6003).

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6001-6003`

**Provenance.** ARCHITECTURE.md:6001-6003. Section 5.10 (ARCHITECTURE.md:3849) is the tonicization section; the memory-held backlog item is recorded in the same terms.


## Group T — Standing process rules and local patches

### D-249 — The whole decision surface is delivered as user-visible text before any choice question

> **Never present the user with options before the ENTIRE situation has been explained in a message the
> user has actually seen.** Mechanism note (the failure that made the rule): Cowork prose written between
> tool calls is summarized, not shown verbatim — so an explanation "just before" a question widget may
> never reach the user, and the question arrives blind. The rules:
> 1. The decision surface (what is being decided, the background, each option's meaning, risks both ways,
>    the recommendation and why) is delivered as user-visible text FIRST — via the verbatim message
>    channel or as the turn's final response.
> 2. For consequential decisions (ratifications, adoptions, retirements, checkpoint rulings), the choice
>    question goes in a SEPARATE, LATER turn — the user reads first, then is asked.
> 3. A decision answered blind is voidable: re-present the surface and re-confirm.

**In plain words.** Before the user is asked to choose, the situation is explained in a message the user has actually read: what is being decided, the background, what each option means, the risks both ways, and the recommendation. For a consequential call the question comes in a later turn. A decision answered blind can be voided and re-asked.

**Why.** The mechanism is stated with the rule: prose written between tool calls is summarized rather than shown verbatim, so an explanation placed just before a question widget can never reach the user and the question arrives blind (cowork_handoff.md:1590-1592). Its first application is recorded: the 2026-07-05 verdict-14 and 2.2c ratifications were re-presented and re-confirmed.

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Home.** `cowork_handoff.md:1589-1598`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:1587 (the standing-rule heading, "user mandate 2026-07-05"); the instituting record is at STATUS_ARCHIVE.md:202

### D-250 — Dispatches are written only when they are next; a parked instruction is revalidated first

> **Do NOT write CC instructions ahead of need.** Pre-written instructions go stale (their premises change under
> them), risk being skipped, and risk out-of-order execution. The rules:
> 1. **At most ONE instruction is dispatched/being-executed at a time** (single CC, single worktree unless the user
>    explicitly sets up a second).
> 2. **The NEXT instruction is written only when its predecessor's report is ratified** and it is actually the next
>    dispatch — never speculatively.
> 3. **The dispatch QUEUE is a plan, not files:** upcoming work is recorded as plan lines (roadmap / STATUS "next"),
>    not as pre-written instruction files.
> 4. **Any instruction file that exists but is not the active dispatch carries a `⏸ PARKED` banner** and MUST be
>    revalidated by Cowork against the then-current STATUS/HEAD immediately before dispatch, receiving a dated
>    DISPATCH note. CC must not execute a parked instruction without that note.

**In plain words.** One instruction is dispatched at a time, and the next is written only once its predecessor's report is ratified. Upcoming work lives as plan lines, not as pre-written instruction files. An instruction file that is not the active one carries a parked banner and must be revalidated against the current state before it is dispatched.

**Why.** The reasons are stated with the rule: pre-written instructions go stale as their premises change under them, risk being skipped, and risk out-of-order execution (cowork_handoff.md:1606-1607).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_handoff.md:1606-1616`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:1606-1616 (stated as standing rules under the handoff's standing-rules block)

### D-251 — A running dispatch is never interrupted or steered mid-flight; every instruction is self-sufficient

> 5. **NO MID-FLIGHT STEERING (user, 2026-07-05): a running CC is never interrupted or relayed to** —
>    interruptions have several times proven disastrous. Every instruction must therefore be
>    SELF-SUFFICIENT: all foreseeable forks carried as in-instruction STOP/branch rules; anything not
>    covered waits for the report and is ruled at verification. The only mid-run channel is the one CC
>    itself opens (its own STOP question), answered when CC asks.

**In plain words.** Once a working session is executing an instruction, nothing is relayed into it. Every foreseeable fork is written into the instruction as a stop or branch rule; anything not covered waits for the report. The only mid-run channel is a question the session itself raises.

**Why.** The evidence is stated with the rule: interruptions have several times proven disastrous (cowork_handoff.md:1618).

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Home.** `cowork_handoff.md:1617-1621`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:1617 ("NO MID-FLIGHT STEERING (user, 2026-07-05)")

### D-252 — One side writes the instruction files and the other executes them, never the reverse

> **Cowork writes instruction files. CC executes them. Never the other way around.**
>
> - When the user says "go", "do E2b", "execute", or similar: the response is
>   "The instruction is ready at `cc_instruction_X.md` — give it to CC."
> - Cowork MAY: read source files **via the file tools (Read / Grep / Glob) — NOT bash** (see the NEVER-BASH
>   standing rule below), write `.md` instruction files, update `cowork_handoff.md` / `STATUS.md` summaries after CC reports.
> - Cowork MUST NOT: spawn agents that run build commands or modify `src/` files;
>   use Edit/Write tools on anything under `src/`; use bash redirects on source files.
> - Violating this rule has broken the codebase twice (E1, E2b). Do not do it again.

**In plain words.** The planning side writes instruction files and may read sources and update the summary documents; it does not edit anything under src/, run builds, or spawn agents that do. The executing side runs the instruction.

**Why.** The evidence is stated with the rule: violating it has broken the codebase twice, at the E1 and E2b increments (cowork_handoff.md:1638).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_handoff.md:1630-1638`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:1628 ("STANDING RULE FOR COWORK (read every session)")

### D-253 — Working-tree files are read with the file tools; bash is limited to git object queries by explicit hash

> - **Local file CONTENT, existence, line counts, searches → ALWAYS the file tools (Read / Grep / Glob).** NEVER `bash`
>   `cat` / `wc` / `grep` / `sed` / `head` / `tail` / `git status` / `git diff` on working-tree files. *(Supersedes the
>   older "read source via grep/cat/sed -n" line in the first standing rule above — that path is the stale one.)*
> - **`bash` is permitted ONLY for read-only git OBJECT queries, BY EXPLICIT SHA from CC's commit report** (option B,
>   user-ratified): `git show <sha>:path`, `git show --stat <sha>`, `git cat-file`, `git diff <shaA> <shaB>`. These are
>   content-addressed and **self-verifying** — a stale/unsynced object errors loudly (`bad object`), never returns
>   silently-wrong content.
> - **NEVER trust `git rev-parse HEAD` / `git status` / `git log`(branch tip) for "what is current"** — those read
>   mutable refs/index that can be stale. Take the SHA from CC's report, read by that SHA, corroborate with a fresh
>   file-tool read.
> - A `bad object` / missing-object error = a **staleness signal → surface it, do not guess.** Mount refresh is
>   host-side only (CC `touch`es the file on Windows, or restart the session).

**In plain words.** File content, existence, line counts and searches are read through the file tools, never through shell text utilities on the working tree. Shell access is allowed only for read-only git object queries named by an explicit commit hash, which are content-addressed and fail loudly when stale. A branch tip or index read is never trusted for what is current.

**Why.** The failure that produced it is stated in the record: a stale mount made the shell path return wrong content and triggered a false corruption alarm, while the file tools read the live disk correctly (cowork_handoff.md:1665-1667). The git-object exception is justified by self-verification: a stale object errors rather than returning silently-wrong content.

**Status.** LIVE · decided 2026-06-21 · ratified by user

**Home.** `cowork_handoff.md:1669-1680`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:1642 ("COWORK MUST NOT HALLUCINATE OR ASSUME — VERIFY AT SOURCE (user mandate 2026-06-21)"), under which this rule is stated

### D-254 — Investigate by default; never ask the user whether to investigate or proceed

> **Whenever a step could be investigated/measured BEFORE committing, ALWAYS investigate first — and do NOT
> present it to the user as a choice.** The user's standing answer to "investigate or go in some direction"
> is *always investigate*, so asking wastes a turn. This is the never-guess principle's logical end: gather
> the cheap evidence before any commitment, by default. When Cowork hits such a fork, it writes the
> investigation/measurement instruction directly (read-only / byte-identical where possible).

**In plain words.** Wherever a step could be measured before it is committed to, it is measured first, and that is not put to the user as a choice. When the planning side reaches such a fork it writes the read-only investigation instruction directly.

**Why.** The reason is stated with the rule: the user's standing answer to that question is always to investigate, so asking wastes a turn; it is the never-guess principle's logical end (cowork_handoff.md:1793-1795). Register entry D-169 records the principle (#5) this operationalizes.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Home.** `cowork_handoff.md:1792-1796`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:1790 ("INVESTIGATE BY DEFAULT — NEVER ASK 'investigate vs proceed' (user mandate 2026-06-14)")

