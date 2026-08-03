# Decisions group T — Standing process rules and local patches

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-196 — The self-check: re-read the diff against the principles before reporting

> After EVERY coding exercise — code, scripts, instruments, and document edits alike —
> and BEFORE reporting the work done: take a step back, re-read the actual diff of every
> touched file, and check it against the guiding principles, the conventions, the gate and
> threshold policies in this file, and the known problem types in `DEFECT_TYPES.md`. Any
> violation found is surfaced immediately (its own `OPEN_ITEMS.md` row if it cannot be
> corrected on the spot within the session's authorized scope), never silently shipped.
> The check is of the work actually on disk, not of the intention — read the diff, not the
> memory of writing it. This applies to CC sessions and Cowork sessions alike.

**In plain words.** After every piece of work and before reporting it, the actual difference on disk in every touched file is re-read and checked against the principles, the conventions, the gate policies and the known defect types. Anything found is surfaced at once, never quietly shipped.

**Why.** Stated constraint, CLAUDE.md:886-887: the check is of the work actually on disk, not of the intention - read the difference, not the memory of writing it. Which is the same reasoning as the never-work-from-memory rule, applied to one's own output.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:1165`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:878-887, user-directed 2026-07-11. Binds Claude Code and Cowork sessions alike.

### D-197 — The distribution constraint - the import-fix patch is fork-local and never goes upstream

> **★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the
> MuseScore community.** This patch (`cfc7eb5e39`) is fine to have in the **central repo = the user's
> fork** (`origin` = `slimvince/MuseScore`) and may be pushed there, but it must **NEVER** be pushed or
> merged to `upstream` (`musescore/MuseScore`) or otherwise contributed to the MuseScore community.
> `upstream` push is disabled in this repo; keep it so. Any future push/PR/merge that would carry
> `cfc7eb5e39` (or its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed.
> (The #9444 reference above is the upstream *bug report*; it does NOT authorize contributing THIS patch.)

**In plain words.** The MusicXML mode-import fix may live in the user's own fork of MuseScore and be pushed there. It must never be pushed, merged or otherwise contributed to the MuseScore project. Any action that would carry it toward the upstream repository stops work and is reported.

**Why.** Stated constraint, CLAUDE.md:753: the upstream issue number cited beside the patch is the upstream BUG REPORT, and referencing it does not authorize contributing this patch. Upstream pushing is disabled in the repository and is to be kept so (:683-684).

**Status.** LIVE · decided 2026-06-15 · ratified by user

**Home.** `CLAUDE.md:867`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:737-753, user-directed 2026-06-15. ★ READ WITH the general contribution intent at ARCHITECTURE.md:380-382 - two recorded positions, a general intent to contribute and a named one-patch exception; the record does not state how the general intent applies to the rest of the tree.

### D-198 — The Windows snap fix in the muse submodule is intentional and must not be reverted

> **File:** `muse/framework/ui/internal/platform/windows/winwindowscontroller.cpp`  
> **Function:** `calculateWindowSize()`
>
> Two lines were removed that set `ptMinTrackSize` equal to the full monitor work
> area inside the `WM_GETMINMAXINFO` handler. This told Windows the minimum
> allowed window size was the entire screen, which prevented Windows Snap from
> resizing a maximised MuseScore window into a chosen snap zone (the window
> stayed full-screen and lost its title-bar controls).
>
> The fix: `ptMaxSize` and `ptMaxPosition` are kept (they correctly constrain the
> maximised position); `ptMinTrackSize` is intentionally left unset.
>
> Upstream issue: musescore/MuseScore#25823 (related cousins: #21344, #16794).  
> Introduced by upstream commit `4ad218709` (5 Aug 2025).  
> **Do not restore the `ptMinTrackSize` lines.**

**In plain words.** Two lines were removed from MuseScore's Windows window-sizing code that told Windows the smallest allowed window was the whole screen. With them in place, a maximised MuseScore window could not be snapped into a screen zone - it stayed full-screen and lost its title-bar controls. The removal is deliberate and stays.

**Why.** Stated constraint, CLAUDE.md:683-709: the removed lines set the minimum window size to the full monitor work area, which is what blocked snapping; the maximised-position constraints are correct and are kept. Upstream issue musescore/MuseScore#25823, introduced by upstream commit 4ad218709 (:643-644).

**Status.** LIVE · decided 2026-05-14 · ratified by user

**Home.** `CLAUDE.md:819`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:678-713, applied 2026-05-14. Unrelated to the composing module; recorded so a dependency update does not silently overwrite it.

### D-199 — The MusicXML declared-mode import fix is intentional and must not be reverted

> The dedup guarded the `KeySig` creation on **fifths only**:
> `if (oldkey != key.key() || key.custom() || key.isAtonal())`. At score start the
> prevailing key defaults to `{C, KeyMode::UNKNOWN}` (`KeyList::key()` →
> `setConcertKey(Key::C)`), so a **0-fifths** key signature carrying an explicit
> `<mode>` (e.g. `<fifths>0</fifths><mode>minor</mode>`) matched the prevailing fifths,
> the whole `KeySig` was dropped, and the declared `<mode>` went with it →
> `KeyMode::UNKNOWN` downstream. Export *does* write `<mode>`
> (`exportmusicxml.cpp:2473`), so this broke export/import round-trip of `<mode>` and,
> in our pipeline, dropped the declared-mode anchor on ~79 zero-signature Bach stems
> (`cc_key_emission_headroom_dossier.md` — `declaredModeOrdinal=-1`). The maintainers'
> own `// TODO only if different custom key ?` flags the dedup as known-incomplete.
>
> The fix: fetch the prevailing `KeySigEvent` (not just the `Key` fifths) and add an
> `oldKeySig.mode() != key.mode()` term to the guard, so a mode-bearing key at matching
> fifths is retained. A key matching the prevailing one in **both** fifths and mode (and
> not custom/atonal) still produces **no** `KeySig`, so plain mode-less C-major scores are
> unaffected. Verified isolated to empty-signature scores (exactly 79 zero-sig `.ours.json`
> changed, 0 non-empty-signature stems); BIR gate byte-identical on all three presets
> (Baroque 57 / Jazz 23 / Default 57); key-inference S2 −378 (Default). Round-trip of
> `bwv254` (0-fifths `<mode>minor</mode>`) now preserves `<mode>`.

**In plain words.** MuseScore's importer dropped a key signature that matched the prevailing one in number of sharps or flats even when it declared a different mode - so a piece written with no sharps or flats but marked minor lost that marking on import. The fix compares the mode as well as the accidental count, so a mode-bearing key signature survives.

**Why.** Measurement, CLAUDE.md:736-739: the change is verified isolated to empty-signature scores - exactly 79 zero-signature analyses changed and no non-empty-signature piece moved - the regression gate is byte-identical on all three presets, and the round-trip of a zero-signature minor piece now preserves its mode. The underlying defect is upstream-unchanged code whose own comment flags the check as known-incomplete (CLAUDE.md:729-730, :673-674).

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Home.** `CLAUDE.md:840`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:715-745, applied 2026-06-14, commit cfc7eb5e39. ★ Carries the distribution constraint above: fork-local only, never upstream.

### D-208 — A withheld finding never enters a mandatory session-start read

> **A WITHHELD FINDING NEVER ENTERS A MANDATORY SESSION-START READ (user-ratified 2026-07-28).**
> When a pass is run blind — a finding deliberately kept from the auditor so that whether they
> rediscover it measures the audit's power — that finding must not appear in any document the

**In plain words.** When a review is run blind - deliberately keeping a finding from the reader so that whether they rediscover it measures the review's power - that finding must not appear in any document the reader is required to open at the start. The status file carries a pointer; the content lives in a separate artifact opened only afterwards.

**Why.** Measurement, OPEN_ITEMS.md:170: the rule was written because the blinding was defeated at the source - the mandatory status-file read carried the full text of all three sealed findings, and the dispatch delivered them inline as well. The consequence recorded there: the reconciliation could no longer claim knowledge-free discovery, only that the artifacts point at each mechanism on their merits.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `cowork_audit_protocol.md:56-58`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:170 (OI-222) with open_items/OI-222.md, and restated in a session handoff block. Homed under P5 of the audit protocol, which is the blinding rule it sharpens. Generalizes the earlier OI-89 instance of the same shape

### D-209 — Code that is about to be deleted gets no audit - only the no-information-loss check at deletion

> Applied BEFORE P1's enumeration. The module is partitioned against the retirement map: **code that
> retires gets no audit at all** — the only thing owed to it is the #12 no-information-loss check at
> the moment of deletion (does anything it knew go unrecorded?). The surviving stack is then audited

**In plain words.** Before auditing the system exhaustively, the code is split into what survives and what is scheduled for removal. What is scheduled for removal is not audited at all. The only thing owed to it is a check, at the moment it is deleted, that nothing it knew is lost.

**Why.** Stated constraint, OPEN_ITEMS.md:60: the alternative form - audit whatever you happen to touch - was rejected by the user as risky, because touching one per cent would audit one per cent while new work built on the unaudited rest, which is itself a violation of the no-unverified-premises principle across the whole architecture. ★ The rule's own boundary is recorded too: at cowork_handoff.md:368-369 the user ruled it does NOT shield the joint module, which is production on both surfaces and is not retiring.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `cowork_audit_protocol.md:103-105`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at open_items/OI-84.md:7 (OI-84), corrected 2026-07-10 at the user's challenge, on a row whose own status is COMPLETE. Homed as P9 of the audit protocol, with the 2026-07-28 boundary ruling (it does not shield the joint estimator module) stated beside it. The plan it belongs to is complete: every surviving layer certified on two passes each

### D-231 — Issue-exhaustion and specification completion before any fix design - the three-phase sequencing rule

> **ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN (user-directed,
> 2026-08-02; sharpens #8, which forbade inference-problem coding before layer completion — this
> forbids fix DESIGN before knowledge completion).**

**In plain words.** Before any fix is even designed: first the specifications are made complete (every decision written into its owning specification, so conformance is measured against the specifications, with the decisions register kept only as the status ledger) and true (false statements corrected); then issue-finding is exhausted with each search's miss rate measured; then one prioritized plan covers every found issue - and only after that plan does design work begin.

**Why.** The user's principles #3/#5/#13 generalized from one defect family to the whole system (gather facts before building; a surprise means the fact basis was incomplete), plus the recorded fact that the product is unshipped, so carrying known defects while knowledge completes costs no user anything (CLAUDE.md, the Conventions entry of 2026-08-02, which states the three phases in full).

**Status.** LIVE · decided 2026-08-02 · ratified by user

**Home.** `CLAUDE.md`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-02 (the audits-before-design discussion; all three phases adopted as presented). Registered in the recording commit per D-230.

### D-249 — The whole decision surface is delivered as user-visible text before any choice question

> - **THE WHOLE DECISION SURFACE IS DELIVERED AS USER-VISIBLE TEXT BEFORE ANY CHOICE QUESTION (user
>   mandate 2026-07-05; homed here 2026-08-02 from `cowork_handoff.md`, `OPEN_ITEMS.md` OI-266).**
>   Never present the user with options before the entire situation has been explained in a message the
>   user has actually seen. The decision surface — what is being decided, the background, what each
>   option means, the risks both ways, and the recommendation with its reason — is delivered as
>   user-visible text FIRST, via the verbatim message channel or as the turn's final response. For a
>   **consequential** decision (a ratification, an adoption, a retirement, a checkpoint ruling) the
>   choice question goes in a SEPARATE, LATER turn: the user reads first, then is asked. **A decision
>   answered blind is voidable** — re-present the surface and re-confirm. *Why:* the mechanism is
>   stated with the rule — prose written between tool calls is summarized rather than shown verbatim,
>   so an explanation placed "just before" a question widget may never reach the user and the question
>   arrives blind. Its first application is on the record: the 2026-07-05 verdict-14 and 2.2c
>   ratifications were re-presented and re-confirmed.

**In plain words.** Before the user is asked to choose, the situation is explained in a message the user has actually read: what is being decided, the background, what each option means, the risks both ways, and the recommendation. For a consequential call the question comes in a later turn. A decision answered blind can be voided and re-asked.

**Why.** The mechanism is stated with the rule: prose written between tool calls is summarized rather than shown verbatim, so an explanation placed just before a question widget can never reach the user and the question arrives blind (cowork_handoff.md:1590-1592). Its first application is recorded: the 2026-07-05 verdict-14 and 2.2c ratifications were re-presented and re-confirmed.

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `CLAUDE.md:1120-1132`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1589-1598, under the standing-rule heading 'FULL DECISION SURFACE BEFORE ANY CHOICE QUESTION' at cowork_handoff.md:1587 ('user mandate 2026-07-05'), with the instituting record at STATUS_ARCHIVE.md:202 - a session handoff block, which is a place for tracking a handover and not a home for a standing rule. Homed in the CLAUDE.md Conventions section, where this project's standing session-method rules live. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-250 — Dispatches are written only when they are next; a parked instruction is revalidated first

> **Do not write instructions ahead of need.** At most **one** instruction is dispatched or being
> executed at a time. The next instruction is written only once its predecessor's report is ratified
> and it is actually the next dispatch — never speculatively. Upcoming work is recorded as **plan
> lines** (the roadmap, the `STATUS.md` "next" entry), not as pre-written instruction files. Any
> instruction file that exists but is not the active dispatch carries a **`⏸ PARKED` banner** and must
> be revalidated against the then-current `STATUS.md` and HEAD immediately before dispatch, receiving
> a dated dispatch note; an executing session must not run a parked instruction without that note.
> *Why:* the three failure modes are stated with the rule — a pre-written instruction goes stale as
> its premises change under it, risks being skipped, and risks out-of-order execution.

**In plain words.** One instruction is dispatched at a time, and the next is written only once its predecessor's report is ratified. Upcoming work lives as plan lines, not as pre-written instruction files. An instruction file that is not the active one carries a parked banner and must be revalidated against the current state before it is dispatched.

**Why.** The reasons are stated with the rule: pre-written instructions go stale as their premises change under them, risk being skipped, and risk out-of-order execution (cowork_handoff.md:1606-1607).

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_audit_protocol.md:166-174`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1606-1616, stated as standing rules under the handoff's standing-rules block - a session handoff block. Homed in the new dispatch-protocol section of the audit protocol. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-251 — A running dispatch is never interrupted or steered mid-flight; every instruction is self-sufficient

> **No mid-flight steering (user, 2026-07-05):** a running session is never interrupted or relayed to.
> Every instruction must therefore be **self-sufficient** — every foreseeable fork is carried inside
> it as a stop or branch rule, and anything not covered waits for the report and is ruled at
> verification. The only mid-run channel is the one the executing session itself opens, its own STOP
> question, answered when it asks. *Why:* the evidence is stated with the rule — interruptions have
> several times proven disastrous.

**In plain words.** Once a working session is executing an instruction, nothing is relayed into it. Every foreseeable fork is written into the instruction as a stop or branch rule; anything not covered waits for the report. The only mid-run channel is a question the session itself raises.

**Why.** The evidence is stated with the rule: interruptions have several times proven disastrous (cowork_handoff.md:1618).

**Status.** LIVE · decided 2026-07-05 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_audit_protocol.md:178-183`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1617-1621 ('NO MID-FLIGHT STEERING (user, 2026-07-05)') - a session handoff block. Homed in the new dispatch-protocol section of the audit protocol. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-252 — One side writes the instruction files and the other executes them, never the reverse

> **Cowork writes instruction files. CC executes them. Never the other way around.** When the user
> says "go", "execute", or names an increment, the response is that the instruction is ready at its
> `cc_instruction_*.md` path and should be given to the executing session. The planning side **may**
> read source files via the file tools, write `.md` instruction files, and update `cowork_handoff.md`
> and `STATUS.md` after a report lands. It **must not** edit anything under `src/`, run builds, or
> spawn agents that run build commands or modify `src/`. *Why:* violating this rule has broken the
> codebase twice, at the E1 and E2b increments — the evidence is stated with the rule itself.

**In plain words.** The planning side writes instruction files and may read sources and update the summary documents; it does not edit anything under src/, run builds, or spawn agents that do. The executing side runs the instruction.

**Why.** The evidence is stated with the rule: violating it has broken the codebase twice, at the E1 and E2b increments (cowork_handoff.md:1638).

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_audit_protocol.md:156-162`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1630-1638, under 'STANDING RULE FOR COWORK (read every session)' at cowork_handoff.md:1628 - a session handoff block. Homed in the new dispatch-protocol section of the audit protocol, beside P5's withheld-finding rule and P8's pass ordering, which are already rules about how a dispatch is written and sequenced; that section's lead-in states that these three rules govern every dispatch and not only the audits above it. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-253 — Working-tree files are read with the file tools; bash is limited to git object queries by explicit hash

> - **WORKING-TREE FILES ARE READ WITH THE FILE TOOLS; SHELL ACCESS IS LIMITED TO GIT OBJECT QUERIES BY
>   EXPLICIT HASH (user mandate 2026-06-21; homed here 2026-08-02 from `cowork_handoff.md`,
>   `OPEN_ITEMS.md` OI-266).** Local file content, existence, line counts and searches always go
>   through the file tools (Read / Grep / Glob), never through shell text utilities — no `cat`, `wc`,
>   `grep`, `sed`, `head`, `tail`, `git status` or `git diff` on working-tree files. Shell access is
>   permitted **only** for read-only git OBJECT queries named by an explicit commit hash taken from a
>   session's own commit report (`git show <sha>:path`, `git show --stat <sha>`, `git cat-file`,
>   `git diff <shaA> <shaB>`). A branch tip or index read — `git rev-parse HEAD`, `git status`,
>   `git log` — is never trusted for what is current. A `bad object` or missing-object error is a
>   **staleness signal: surface it, never guess around it.** *Why:* measured failure — a stale mount
>   made the shell path return wrong content and raise a false corruption alarm while the file tools
>   read the live disk correctly; the git-object exception survives because content-addressed reads are
>   self-verifying, erroring loudly rather than returning silently-wrong content. **Scope, as the
>   record states it:** this is a standing rule for the PLANNING side — it is stated under the heading
>   "COWORK MUST NOT HALLUCINATE OR ASSUME — VERIFY AT SOURCE", and the role-separation rule beside it
>   spells out the same restriction as one of the things "Cowork MAY" do. It is homed here because
>   `CLAUDE.md` is where this project's shared standing rules live, not because its scope widens: the
>   build, test and measurement commands `BUILD_AND_TEST.md` and the sections above mandate are
>   unaffected, and nothing in the record extends the file-tools restriction to them.

**In plain words.** File content, existence, line counts and searches are read through the file tools, never through shell text utilities on the working tree. Shell access is allowed only for read-only git object queries named by an explicit commit hash, which are content-addressed and fail loudly when stale. A branch tip or index read is never trusted for what is current.

**Why.** The failure that produced it is stated in the record: a stale mount made the shell path return wrong content and triggered a false corruption alarm, while the file tools read the live disk correctly (cowork_handoff.md:1665-1667). The git-object exception is justified by self-verification: a stale object errors rather than returning silently-wrong content.

**Status.** LIVE · decided 2026-06-21 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `CLAUDE.md:1134-1152`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1669-1680, under the standing-rule heading 'COWORK MUST NOT HALLUCINATE OR ASSUME - VERIFY AT SOURCE (user mandate 2026-06-21)' at cowork_handoff.md:1642 - a session handoff block. Homed in the CLAUDE.md Conventions section. Its scope is taken FROM THE RECORD, not decided here: that heading and D-252's own text ('Cowork MAY: read source files via the file tools - NOT bash') both state it as a planning-side rule, so the homed entry says so and says the mandated build, test and measurement commands are unaffected. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-254 — Investigate by default; never ask the user whether to investigate or proceed

> - **INVESTIGATE BY DEFAULT; NEVER ASK THE USER WHETHER TO INVESTIGATE OR PROCEED (user mandate
>   2026-06-14; homed here 2026-08-02 from `cowork_handoff.md`, `OPEN_ITEMS.md` OI-266).** Wherever a
>   step could be investigated or measured BEFORE it is committed to, it is measured first — and that
>   is not put to the user as a choice. When such a fork is reached, the read-only investigation or
>   measurement is written and run directly, byte-identical where possible. *Why:* the user's standing
>   answer to "investigate, or go in some direction" is always *investigate*, so asking spends a turn
>   to learn nothing; this is the never-guess rule's logical end — gather the cheap evidence before any
>   commitment — and it operationalizes principle #5 (investigate when facts may be scarce).

**In plain words.** Wherever a step could be measured before it is committed to, it is measured first, and that is not put to the user as a choice. When the planning side reaches such a fork it writes the read-only investigation instruction directly.

**Why.** The reason is stated with the rule: the user's standing answer to that question is always to investigate, so asking wastes a turn; it is the never-guess principle's logical end (cowork_handoff.md:1793-1795). Register entry D-169 records the principle (#5) this operationalizes.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `CLAUDE.md:1154-1161`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1792-1796, under the standing-rule heading 'INVESTIGATE BY DEFAULT - NEVER ASK investigate vs proceed (user mandate 2026-06-14)' at cowork_handoff.md:1790 - a session handoff block. Homed in the CLAUDE.md Conventions section, beside principle #5, which it operationalizes. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

### D-258 — A prune and tidy pass runs before any publish of the fork, and nothing on its list is acted on before it

> **Standing deferral (user, 2026-06-22):** "back up now, tidy up files we don't want to publish later." This is the
> running list of prune/tidy decisions to make **before any publish** of the fork (`origin = slimvince/MuseScore`).
> Nothing here is to be acted on now — it is the to-do for the prune pass. Keep appending as items arise.

**In plain words.** Files that should not be published are listed as they are found and dealt with in one pass before the fork is published; the list is appended to as items arise, and nothing on it is acted on in the meantime.

**Why.** The reason is stated with the deferral: backing the work up to the fork now is worth more than keeping the fork publishable at every moment, so the publishability question is batched into one pass rather than paid per commit. Related: register entry D-197, the distribution constraint.

**Status.** DEFERRED · decided 2026-06-22 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prune_pass_checklist.md:3-5`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** cowork_prune_pass_checklist.md:3 records it as a standing deferral in the user's own words ('back up now, tidy up files we don't want to publish later'), with the date and ratifier stated. Status is DEFERRED because the record says the pass has not run (:5 - 'Nothing here is to be acted on now - it is the to-do for the prune pass'). Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-259 — Every upstream contribution is checked against the distribution constraint before it is posted

> ## 6. Standing guard (not a prune item — a permanent rule)
> - **Any** upstream GitHub comment / PR / contribution must be checked against the CLAUDE.md distribution constraint
>   **before** posting. A draft carrying a fork-local-constrained patch (`cfc7eb5e39`, #9444) is a **HARD STOP** — never
>   post. Non-constrained reports (e.g. #24673) are the user's normal call.

**In plain words.** Any comment, pull request or contribution aimed at the upstream MuseScore project is checked against the distribution constraint first. A draft carrying the fork-local import-fix patch is a hard stop and is never posted; a contribution carrying none of it is an ordinary decision for the user.

**Why.** The instance that produced it is recorded in the same file (cowork_prune_pass_checklist.md:7-18): a draft comment for the upstream issue was written carrying the constrained patch's content, before the constraint existed, and survives in the fork's history. The rule generalizes the one-patch prohibition into a pre-post check on every upstream contribution.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_prune_pass_checklist.md:43-46`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** cowork_prune_pass_checklist.md:43 states it as 'a permanent rule' explicitly distinguished from the prune items around it; no date or ratifier is stated at this home. It operationalizes register entry D-197, the ratified distribution constraint, by naming the check that has to happen and when. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-279 — The Stage-3 entry gate - seven conditions before any engagement wiring reaches production

> **★ STAGE-3 ENTRY GATE (ratified 2026-07-10 with #17–#19; evidence `cowork_l1_l5_premise_debt_audit.md`).**
> Before any E4/L5 engagement wiring can reach production:
> - **(EG-1) Tier-1 defusal is a PREREQUISITE, not an inventory item:** the resolver selection re-ordering
>   (arc #9 — the as-built `resolveAbstained` still selects progression-first at confidence 1.0, the channel

**In plain words.** Before the rebuilt path's wiring can reach production, seven conditions hold: the two measured-harmful mechanisms are defused or provably bypassed; the go/no-go measurement runs under the full Premise Gate with its measurement tool established first; the pedal reader waits on its underpowered premise being settled; the confidence-commensurability premise owes a ledger and a desk simulation before any threshold is fitted; the fit surface is completed; the Jazz preset's validation status is declared honestly; and no step opens until every layer it depends on has passed its audit.

**Why.** Each condition names the measurement or the absence that produced it (cowork_engage_arc_plan.md:66-92): the override measured at minus 756, the missing establishment record for the decode chain, the pedal premise at agreement 0.20 to 0.50 on two to five cases, and the failed calibration that stands as the warning against assuming a fit will repair an incoherent quantity. It is principle #18 at architecture scale - new construction may not carry load on unaudited foundations.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_engage_arc_plan.md:69-72`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“The stages”** — `## The stages (in principle order)` (heading at line 19). A delegation at CLAUDE.md:134 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** cowork_engage_arc_plan.md:64 states the gate as 'ratified 2026-07-10 with #17-#19', with its evidence document cited; the conditions at :64-92 and the amendment note at :128-130. The last condition is registered separately as D-209, the retiring-code audit rule, at its cowork_audit_protocol.md home. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-298 — The layer-by-layer audit - each layer is audited once its pieces are in place

> ## P10 — Verification is organised BY LAYER: a layer is audited once its pieces are in place (user-recorded standing method, 2026-06-14)
>
> Auditing is not something done to each change in isolation. When a layer's pieces are built, that layer is

**In plain words.** Verification is organised by layer: when a layer's pieces are built, that layer is audited as a whole before the work moves on, rather than checking each change in isolation.

**Why.** A user-recorded standing method, adopted as the verification model for the second half of the programme. It is the method the later per-layer certification plan realised.

**Status.** LIVE · decided 2026-06-14 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_audit_protocol.md:117-119`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 option-C block) as a new standing method, pointing at the handoff's standing block and the roadmap. Realised as the dependency-ordered per-layer certification plan (`OPEN_ITEMS.md` OI-84, complete 2026-07-12) and as the audit protocol's pass ordering. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]] — process rules go to `CLAUDE.md` or the audit protocol): written as P10 of `cowork_audit_protocol.md`, beside P8 and P9, which are the method this rule says WHEN to apply. Former home preserved (#12): `cowork_handoff_archive.md:3771`, the 2026-06-14 option-C block.

### D-314 — A correction rule kept for structural reasons must keep producing evidence that it still fires

> **O-10 (lesson from the user's methodology challenge, 2026-07-05): RETAINED structural rules carry
> ongoing LIVENESS evidence.**

**In plain words.** When a rule is kept because it encodes something structural rather than because a fitted number could replace it, its firing counts are re-measured at every adoption event. A kept rule that has quietly stopped firing then shows up at the next checkpoint instead of being discovered much later.

**Why.** The failure it answers is on the record: two rules' founding cases were silently absorbed upstream, leaving the rules dead and undetected for weeks, because nothing measured rule liveness (`cowork_stage5_fitter_design.md:1471-1478`).

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_stage5_fitter_design.md:1482`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§15 Open items & ratification asks”** — `## §15 Open items & ratification asks` (heading at line 908). A delegation at ARCHITECTURE.md:292 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

**Provenance.** Recorded in `cowork_stage5_fitter_design.md` (SIGNED, user, 2026-07-04) at open item O-10, and tracked as a standing obligation at [[OI-36]] — which is an open-items row, not a home. Found by the phase-1f final-partition wave, 2026-08-02, reading `cowork_stage5_fitter_design.md` in full (SIGNED, user, 2026-07-04). NOT RATIFIED — entered with the record's own status and put to the user in the phase-1f ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1f queue).

### D-316 — The chord-symbol parser sussus fix is a recorded local patch with an UPSTREAMABLE distribution disposition

> **★ DISTRIBUTION DISPOSITION (user-ratified 2026-08-02): UPSTREAMABLE** — a general parser
> defect fix with no fork-specific content; contributing it to `musescore/MuseScore` is permitted
> and consistent with the §1.2 contribution intent (contrast the MusicXML mode-import patch above,
> which stays fork-local).

**In plain words.** The one-line fix to MuseScore’s chord-symbol parser (the removal of a redundant assignment that caused the "sussus" double rendering, applied 2026-04-15) is now a recorded, protected local patch, and its distribution ruling is: it MAY be contributed upstream - unlike the MusicXML mode-import patch, which must never be.

**Why.** The MuseScore-dependency rule (D-229, ARCHITECTURE.md §3.3): every edit to MuseScore’s own code is recorded in the local-patches section with a per-instance distribution disposition ratified by the user. Found unrecorded by the phase-1f enumeration (OI-273 - the third such edit, the first two already recorded); disposition upstreamable because the fix is a general parser defect with no fork-specific content (the commit message and diff at b1ba7464 are the evidence).

**Status.** LIVE · decided 2026-08-02 · ratified by user

**Home.** `CLAUDE.md`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-02 (OI-273 option (i)); the CLAUDE.md local-patches subsection added in the same commit (the register’s same-commit rule).

### D-415 — An item on the roadmap may be marked done only with the evidence its own verify column names

> **Standing rule for this roadmap:** an item may only be marked done with the evidence listed
> in its "verify" column. Stages are sequential; items within a stage can run in any order
> unless noted.

**In plain words.** A planned item counts as finished only when the specific evidence written beside it has actually been produced — not when someone judges it done. Stages run in order; items inside one stage may run in any order unless the item says otherwise.

**Why.** The reason is the roadmap's own ordering principle, stated three lines above at `:6-8`: no surprises — verify and pin each layer, gate and method before building on it, so every stage has an explicit verification gate that must pass before the next stage starts. The evidence column is what makes that gate checkable rather than asserted.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:10`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/implementation_roadmap.md`:10-12, stated as "Standing rule for this roadmap". The document is dated 2026-06-10 at `:3`; no date or ratifier is stated for the rule itself. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-417 — The engage criteria — six gates that must all hold, a staged plan, and the user ratification event

> **★★ ENGAGE CRITERIA + RETIREMENT MAP (RATIFIED user 2026-07-02; FOLDED here from `cowork_engage_criteria.md`
> 2026-07-02 — that file is now a tombstone; this roadmap is the single home).** Replaces "engage deferred
> indefinitely" with "deferred until these CRITERIA (date open)"; E3 is its own user-ratification event.
> - **Gates (all must hold):** **G1** spine complete: L4+L5 dormant-validated (✅) + **L6 built dormant** + the A-1
>   contract as-built deltas closed (D-L3a remains). **G2** (measured by the E0 instrument): zero new class-(b) on the
>   case-identity gate; class-(a) per the two-tier policy; **RN vs DCML ≥ legacy on the granularity-robust unit**, all
>   presets; correct-abstention scored separately from wrong commits. **G3** perf: p95 ≤ legacy×1.10 (✅ measured
>   ~3.7× faster). **G4** coverage sealed + snapshot-strategy declared in advance. **G5** docs synced same increment.
>   **G6** user ratifies E3.

**In plain words.** Putting the rebuilt analysis layers into production is no longer "postponed indefinitely" but "postponed until six named conditions all hold": the layer stack complete and validated while dormant; no new meaningful chord-root errors and Roman numerals at least as good as the old path on the measurement unit that does not move with how finely the music is cut; speed within a tenth of the old path; test coverage sealed with the snapshot strategy declared beforehand; documentation updated in the same step; and the user ratifying the switch. Turning it on by default is its own user decision, not a step inside an engineering plan.

**Why.** The reason is the roadmap's founding ordering principle — no surprises: each stage carries an explicit verification gate that must pass before the next starts (`:6-8`), and a production switch is the largest such step. Two of the six gates cite measurements rather than judgment (the class-(b) and two-tier policy under register entries D-115/D-191, and a measured speed comparison recorded as ~3.7x faster), and the sixth reserves the switch itself to the user, which is guiding principle #14 applied to the biggest behavior change the programme had.

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:164`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/implementation_roadmap.md`:122-137, recorded as RATIFIED by the user 2026-07-02 and folded here from `cowork_engage_criteria.md`, which the same passage declares a tombstone — "this roadmap is the single home", an explicit home declaration. ★ AN OBSERVATION, NOT A STATUS CHANGE: the production switch that actually happened took a different route — the joint estimator was adopted on the batch surface 2026-07-26 (D-005) and on the notation surface 2026-07-27 (D-010), by the OI-178/notation-switch arc, not by this document's E1-E5 staging, and the criteria's G1 names a dormant L6 that was never built. The record contains no ruling that supersedes these criteria, so the entry carries the record's own status (LIVE) and the observation is recorded rather than resolved; it is rowed as `OPEN_ITEMS.md` OI-284. Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.) ★ SCOPED by the user, 2026-08-03 (the OI-284 question, ruled option (iii) — a narrower SUBJECT, a different subject): these criteria govern engaging the DORMANT L4/L5 SPINE, not the joint estimator's adoption. They STAY LIVE and are NOT retired; what was ruled is what they are about. The production switch that happened put a different architecture into production through its own ratified decision surface — the OI-178 batch adoption 2026-07-26 (D-005) and the notation switch 2026-07-27 (D-010) — so the criteria never applied to it; and what they do gate is moot, because the dormant spine they gate is what D-418's retirement map deletes. G1's 'L6 built dormant' requirement therefore needs no satisfying. ★ THE RULING IS A RECONSTRUCTION OF SCOPE AND IS LABELLED AS ONE: the record states the narrowing nowhere — the criteria as written do not say which architecture they govern — so the scope was ruled by the user rather than read out of a text that does not contain it. Recorded at the home (`docs/implementation_roadmap.md`, the annotation beneath the engage block) and at `OPEN_ITEMS.md` OI-284.

### D-418 — The retirement map — nothing retires by silence; ten named retirements, each with its trigger and its order

> - **Retirement map (nothing retires by silence):** R1 legacy chord competition + Gates A–L (E4, or Stage 5 if
>   first — the OWED refactor #2); R2 legacy circular cadence detector (needs the two notation-bridge call-site
>   migrations first — gap-analysis Rider 4); R3 `cadencekeyanchor` kept-as-diagnostic through E4, retire post-E5
>   review; R4 dual tpc reader → the shared spelling view (rides R1); R5 `resolveKeyAndModeRanked`+`collectPitchContext`
>   shrink (P4-redecode; seed S2 at E4; grading baseline may persist as diagnostic); R6 segment-first spine (E4);
>   R7 `harmonicfunctionlayer` rename (rides R1); R8 legacy confidence sentinels (rides R1/R5); R9 `chordanalyzer.cpp`
>   file-split (OWED refactor #1) AFTER E4 removals — split once; R10 batch-region gate superseded by the robust unit
>   as primary (with G2/Stage 5), case-identity + two-tier policy carry over.

**In plain words.** Every piece of the old analysis path that is to be removed is named in advance, with what must happen first and where in the order it sits — ten of them, from the old chord competition and its correction rules through to splitting the large source file last, once, after the deletions. Nothing is retired by simply ceasing to mention it.

**Why.** The principle is stated in the heading itself — nothing retires by silence — and it is guiding principle #12 applied to code: a component that disappears without a recorded decision takes the reason it existed with it. The ordering constraints each carry their own stated cause: two call sites must migrate before the old cadence detector goes; the file split is last so it happens once (register entry D-311); the old batch measurement gate is superseded rather than deleted, its case-identity and two-tier policy carried over (D-115, D-191).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Entry ratified.** 2026-08-03 · by user

**Home.** `docs/implementation_roadmap.md:180`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/implementation_roadmap.md`:138-145, part of the same block the record marks RATIFIED by the user 2026-07-02. It is live and load-bearing now: `CLAUDE.md`'s gate block (A) states that the dormant legacy notation path awaits deletion "at the OI-180 retirement map, now fully live", and `OPEN_ITEMS.md` OI-180 tracks it. R10 is already discharged — the batch gate was superseded by the robust unit at R10-b, 2026-07-06 (D-115). Found by the phase-1k continuation wave, 2026-08-03, reading `docs/implementation_roadmap.md` IN FULL (the OI-207 reading list's next document, 18 clusters). The document's own banner records it as the SINGLE TRACKER ensuring every review conclusion is addressed (`:4-8`); it carries none of the four declared status banners (register entry D-256), so it is not a contract home. NOT RATIFIED — entered with the record's own status and put to the user in the phase-1k ratification queue. ★ RATIFIED (user, 2026-08-03, the phase-1l queue — ratified AS DRAFTED, with the status exactly as the record states it; the ratification is of each RULE itself, and it supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping.)

### D-431 — A figure enters a dispatch or a report by citation to a generated artifact, never by transcription — and so does a premise

> A quantity may not be copied into a dispatch or into a session
> report as a literal value. It is named as **an artifact and a field** — *`tools/audit/decisions/
> phase1m_measurements.json` → `task6_reading_yield.owed_a_full_read`* — and the reader takes the value
> from the artifact. The same holds for a **premise**: a claim of fact about the code, the corpus or
> the record is cited to the primary source it can be checked at, never carried across from a surface
> that merely repeats it.

**In plain words.** A number is never written into a working instruction or a session report as a literal; the instruction names the generated file and the field it lives in, and the reader looks it up. A claim of fact is treated the same way: it is cited to the place it can be checked, not to a document that merely repeats it. Both the side that writes the instructions and the side that writes the reports are bound.

**Why.** Measured over the three waves that ran under the dispatch protocol before the ruling: five instances, each a value or a premise taken from a secondary surface rather than a primary one, and each caught by a dispatch's own ordered check rather than by the writer's reading — a dispatch premise refuted at the commit (`OPEN_ITEMS.md` OI-286), a dispatch premise refuted at the control flow (OI-288), a coverage count that rode forward unchecked for three waves (OI-207, the 2026-08-03 note §0), three rank correlations reported with no generator behind them, and a total transcribed from an artifact that then moved inside the same wave. All five are enumerated with their citations at the rule's home.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `cowork_audit_protocol.md:187`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the fifth ruling set of that date), homed at phase 1n in `cowork_audit_protocol.md`'s dispatch-protocol section beside **D-250**, **D-251** and **D-252**, which is the established home for rules about how a dispatch is written. It is `CLAUDE.md` principle **#17(f)** — no hand-transcribed measurement numbers — applied where it was being ignored: #17(f) was written for DOCUMENTS and was honored there, and dispatches and session reports were treated as outside it on the unstated ground that they are working correspondence rather than record. They are not: a dispatch's premise becomes the next session's starting assumption and a report's figure becomes the next report's baseline. **The register-side instance of the same shape is `OPEN_ITEMS.md` OI-283** — a hand-typed coverage claim inside a generated file — whose remedy is now one instance of this general rule rather than a one-off; that row carries a dated note saying so and does NOT close, its own remedy still being owed. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1n ratification queue.

### D-434 — The writing side runs the standing self-check before a dispatch is released, and records its output

> **before a dispatch or a decision surface is released, the writing side
> runs the standing self-check over it and RECORDS the output.**

**In plain words.** The standing self-check — re-read what is actually on disk and check it against the principles, the conventions and the known defect types before reporting — applies to the side that WRITES the working instructions, not only to the side that executes them. It runs before the instruction is handed over, and its output is written down.

**Why.** Measured on this protocol's own output: eight instances in which a dispatch or a report carried a wrong premise or an underived figure that the standing self-check would have caught, each cited at the rule's home to the row or artifact that records it, and every one of them found by the EXECUTING side running the check the writing side had not. `CLAUDE.md`'s self-check already binds both sides in its own words (*"code, scripts, instruments, and document edits alike"*); what was missing was a statement of it where the rules about writing a dispatch live, and a mechanism that makes its absence visible.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `cowork_audit_protocol.md:241`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the seventh ruling set of that date, W5), homed at phase 1p in `cowork_audit_protocol.md`'s dispatch-protocol section beside **D-431**, which is the established home for rules about how a dispatch is written (D-250, D-251, D-252 also live there). **The rule carries its own mechanism**, so that it is more than a habit: every dispatch and every session report carries a SELF-CHECK SECTION answering a named five-item checklist — the guiding principles, the conventions, the figures-and-premises rule (D-431), the file-tools rule, and uncertainty on any comparison (#24) — and the section's ABSENCE is a failure `tools/audit/process_check.py` reports. The check's own detection power against the eight instances is measured rather than claimed, at `tools/audit/process_check_establishment.json`. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1p ratification queue.

### D-436 — A mechanism is judged on three measured conditions — automatic, detection rate, false-positive rate — and a failing one is REPORTED, not automatically removed

> **Ruled by the user, 2026-08-03; AMENDED by the user the same day (the eleventh ruling set).** A
> mechanism built to enforce one of these rules is judged on three conditions: **it runs
> automatically with no human step, it has a measured detection rate against known instances of the
> failure it is for, and it has a measured false-positive rate at or near zero on legitimate work.**
> All three are measurable and none is judged. **A mechanism that fails any of them is REPORTED —
> with the condition it fails, the measurement that shows it, and the reason that condition exists.
> It is NOT removed automatically: keeping it or removing it is the user's ruling.** The reasons the
> conditions exist are unchanged, and they are what the report must carry: one needing a human step
> is a reminder, one with no measured detection rate is unestablished (#19), and **one that fires on
> legitimate work gets switched off, which is worse than having none.**

**In plain words.** Whether a check or guard built to enforce a process rule is trustworthy is measured on three things: it runs by itself with no human step; it has been measured against known instances of the failure it exists for, and found them; and it has been measured against legitimate work, and hardly ever fires on it. A mechanism that fails one of these is reported — with the condition it failed and why that condition exists — and whether it is kept or removed is the user's call, not the measuring session's. Whether it lets some written rule be deleted is not part of the test.

**Why.** Two rulings on the same day, and the second amends the first. **The test both replace** was a structural proxy standing in for a behavioral quantity, unvalidated — the substitution principle #17(d) forbids. What is at stake is whether the running burden or the failure rate falls, and prose retirement measures neither. The instance that exposed it is on the record: both mechanisms built under the withdrawn test were reported as retiring no prose (`OPEN_ITEMS.md` OI-292, and `tools/audit/claude_md_rule_triage.json` → `what_was_executed`), while each removes a failure mode — so the proxy graded them failures for a reason unrelated to what they do. **The amendment's own defense** is that the first form made failure self-executing ("is not kept"), which puts a removal decision inside a measurement; measuring is the session's act and deciding what a failing measurement means is the user's. It weakens nothing — a mechanism failing the detection-rate condition is still unestablished under #19 and still may not be put under load — and it stops a failing mechanism disappearing without a ruling, which would destroy the measurement's own evidence (#12).

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `cowork_audit_protocol.md:274`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the eighth ruling set of that date, X3), homed at phase 1q in `cowork_audit_protocol.md`'s dispatch-protocol section beside **D-431** and **D-434**, which is the established home for rules about how a dispatch is written and checked. **It WITHDRAWS a test the planning side had stated and this project had been working under** — *a mechanism must retire the prose it replaces, or it is apparatus growth* — and the withdrawal is recorded with its reason rather than left as a silent change of standard. The two mechanisms built under the withdrawn test are KEPT under this one, and their establishment artifacts carry their measured rates: `tools/audit/process_check_establishment.json` and `tools/audit/shell_read_guard_establishment.json`. The guard's third condition holds only while it is ARMED, which is the user's act on the user's machine; until then it is recorded as an expected-failing check rather than as coverage (`OPEN_ITEMS.md` OI-292). **★ AMENDED by the user 2026-08-03 (the eleventh ruling set, AA5) and re-taken at phase 1u: the criterion INFORMS; removal or retention is the user's ruling.** The three conditions and their stated reasons are unchanged — including the false-positive reason, *one that fires on legitimate work gets switched off, which is worse than having none*, which is why that condition exists and which survives the amendment intact. What changed is who decides the consequence. **The FORMER VERBATIM is preserved here (#12), being the text the entry carried before the amendment:** "**Ruled by the user, 2026-08-03.** A mechanism built to enforce one of these rules is kept when **it runs automatically with no human step, it has a measured detection rate against known instances of the failure it is for, and it has a measured false-positive rate at or near zero on legitimate work.** All three are measurable and none is judged. A mechanism that fails any of them is not kept: one needing a human step is a reminder, one with no measured detection rate is unestablished (#19), and one that fires on legitimate work gets switched off, which is worse than having none." **The amendment's first application is on the record in the same wave:** the shell-read guard has two shapes its established corpora do not cover — a common existence-listing command and a path outside the repository — and under the amended rule they are REPORTED and rowed for the false-deny establishment run rather than either added to the denied set unestablished or the guard treated as failing and dropped (`OPEN_ITEMS.md` OI-292, OI-300). NOT RATIFIED as an ENTRY — it goes to the user in the phase-1q ratification queue, with the amendment above added at phase 1u.

### D-437 — Phase 3 waits on the phase-2 items that could find another member of the family being designed for, not on all of phase 2

> **★ QUALIFICATION — PHASE 3 WAITS ON THE PHASE-2 ITEMS THAT COULD FIND ANOTHER MEMBER OF THE
>   FAMILY BEING DESIGNED FOR, NOT ON ALL OF PHASE 2 (user-ruled 2026-08-03).**

**In plain words.** A family design waits only on those phase-2 searches whose search space could contain a fact about the thing that family is about — for the struck-versus-sounding family, about what the decoder or the emission reads or about how candidates are admitted. Where an item's scope does not settle the question it still gates. Narrowing the gate does not open it: no fix, design or inference change is authorized, and the partition is recorded as a falsifiable prediction whose refutation by a non-gating item is a #13 STOP.

**Why.** D-231's phase gate was ratified so that a defect family is KNOWN before it is designed for — the standing one-fix-per-family rule of 2026-07-28 is what it protects. An item that cannot touch what the model reads or how candidates are admitted cannot change what the family is, so making the design wait on it buys no protection and spends time the fix plan is owed. The error in the other direction is bounded by the stated default: an item whose scope does not settle the question gates.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:1037-1055`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03, transmitted in the phase-1o dispatch cc_instruction_phase1o_gate_partition_and_probe_rerun.md §2.1; applied and homed at CLAUDE.md's D-231 entry in the recording commit per D-230. The partition itself is generated at tools/audit/phase3_gate_partition.json. **★ THE PER-ITEM VERDICTS WERE ACCEPTED BY THE USER 2026-08-03 (the eleventh ruling set, AA1) — accepted AS GENERATED, with the accounting of what the ruling's measured effect actually was recorded beside them.** That accounting is a block of the artifact, `what_the_partition_measured`, and no figure of it is restated here (#17f, D-431); its structural counts read fields rather than prose, and the one judgment a text test could not make honestly is carried as quoted sentences for the reader instead of as a number. **In plain words: most items GATE, several of them because their search space has ALREADY produced a member of the family rather than on the doubt default, and the narrowing bites in exactly one place** — the family design need not wait for phase 2's bounded trust statement to be WRITTEN, only for the gating searches to have RUN. **★ THE PLANNING PREDICTION THAT RECOMMENDED THIS RULING IS REFUTED AND IS RECORDED AS SUCH** (#17b applied to a planning claim): Cowork's decision surface said the option *"removes the largest share of the blocking for the smallest loss of rigor"*, and the second half holds while the first does not. **The RULING stands** — it was ruled by the user on its own terms and is not disturbed by its advocate's forecast being wrong; what the record must not do is let a later session inherit the expectation instead of the result. Full statement at the artifact's `what_the_partition_measured.the_refuted_planning_prediction`. **A second premise of the same wave was checked at the document and came back different too**: the claim about which of the four channels the phase-2 clause omits actually matter is not what the inventory supports, and the inventory's own statement that history mining is "run to completion" is not true at HEAD — both at `assumption_A1_of_the_phase1u_dispatch`. No verdict moved on either finding.

### D-438 — Open-items register rows whose subject is this project's own tracking and documentation apparatus gate nothing — but an establishment obligation always gates

> **★ QUALIFICATION OF RULE (b) — THE APPARATUS ROWS ARE DECLARED NON-GATING (user-ruled
> 2026-08-03).**

**In plain words.** An open row of the open-items register whose subject is this project's own tracking or documentation apparatus stays open and stays owed but blocks no stage; it is worked in leftover capacity. The test is whether the row's subject bears on the analysis, its inputs, or an instrument a measurement depends on — if yes it gates — and inside the documentation rows the line is what is owed: a pointer, anchor, label, banner, filing decision or section boundary is apparatus, while correcting a statement about the analysis or completing a specification gates. A row that is not apparatus, or whose subject its own text does not settle, gates. An establishment obligation (#19) always gates, whatever its subject.

**Why.** The open-items register is this project's own record-keeping, and a rule that lets its housekeeping block the work it exists to track inverts what it was created for; the cost of the error in the other direction is bounded by the stated default (anything not settled gates). The establishment exemption is not discretionary because backgrounding an establishment obligation is how it never happens, and #19 exists precisely because a thing merely unfalsified is not established.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:160-181`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03, transmitted in the phase-1o dispatch cc_instruction_phase1o_gate_partition_and_probe_rerun.md §3; applied and homed at CLAUDE.md's open-items register section, qualifying rule (b), in the recording commit per D-230. The derived set is generated at tools/audit/nongating_apparatus_rows.json.

### D-439 — The perspective inventory's §4 is the one home for the enumerated discovery channels, and CLAUDE.md's phase-2 clause points at it instead of listing its own subjects

> **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03;
>   D-439).**

**In plain words.** Section 4 of cowork_oi200_perspective_inventory.md is the ratified one home for the discovery channels that CLAUDE.md's phase-2 clause relies on; the clause now points at that section and lists no subjects of its own (#6). Ratified together with the scope ruling written into that section — which of the four channels the clause never named it reaches: channel 9 (history mining) is IN, being a distinct search the clause names nowhere; channels 4 and 8 are ALREADY REACHED, channel 4 because its own text makes it an obligation carried by the other probes rather than a search of its own and channel 8 because its own text makes it the audit passes and blind second pass the clause names immediately beforehand; channel 10 is NOT a discovery channel on its own account, its catalog-feeding role noted rather than dropped. The ratification does NOT adopt the inventory's §6 program in whole or in part, does NOT pull OI-200 forward, leaves that document's own §9 request open and untaken, authorizes no probe, fix, design or inference change, and does not complete phase 1.

**Why.** A binding user-directed rule was leaning on an unratified Cowork draft: D-231's phase-2 clause named *"the enumerated discovery channels"* and the only place in the record where those channels are enumerated is a document whose own banner read DRAFT and whose §9 recorded its one requested decision untaken. The ratification closes that, and pointing the clause at the ratified section instead of restating six subjects removes the second, shorter enumeration (#6) — which was also an under-naming, since the clause's six subjects are six of ten channels. The scope ruling was folded in rather than deferred because the four unnamed channels are exactly what a pointer makes ambiguous, and each verdict rests on the channel's own text rather than on a judgment made at the ruling.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:1059-1071`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03 (the twelfth ruling set: option C with option B's correction folded in), transmitted in the phase-1v dispatch cc_instruction_phase1v_channel_ratification.md §1 and §4; the reading surface the ruling was taken from is ratification_surfaces/cowork_perspective_inventory_ratification.md §5. Applied and homed at CLAUDE.md's phase-2 clause and its note, in the recording commit per D-230; the enumeration and the scope ruling themselves live at cowork_oi200_perspective_inventory.md §4, which that clause now delegates to by name. **★ THE CHANNEL-9 CORRECTION WAS MADE FIRST, DELIBERATELY.** The inventory's channel 9 said of history mining *"none new — the adjudication is this channel run to completion"*; that was untrue of both faces of the OI-207 adjudication at HEAD — its residual second pass ran on 2026-08-02, the unresolved cluster residual is live at tools/audit/decisions/disposition_manifest.json → disposition_counts.unresolved, and the owed full document reads are tracked on the OPEN_ITEMS.md OI-207 row. Both were established at those objects before this entry was written. Ruling the channel's scope while its own text said the work was finished would have ratified a contradiction, which is why the user's ruling folds the correction into the ratifying act rather than following it. The former wording is preserved verbatim at the inventory's own dated correction note (#12), as is the former CLAUDE.md note that recorded the gap while it stood. **★ WHAT IT DOES NOT DECIDE, stated because a later reader would otherwise assume more:** the §6 program is NOT adopted in whole or in part; OI-200 is not pulled forward and the inventory's §9 request — adopt, amend or reject that program — stays open and untaken; no probe, fix, design or inference change is authorized; and phase 1 is not complete. **★ WHAT IT RETIRES:** the stated workaround tools/audit/phase3_gate_partition.json carried about its structural source being an unratified draft — preserved verbatim in that artifact's `the_channel_enumeration_source.status_of_this_source.what_this_retires` and NOT deleted (#12). **No verdict of that partition moves**, and none was re-stated on the new authority: the verdicts were recorded as a prediction before the classified items ran, which is what makes them falsifiable. One consequence is reported rather than silently corrected — the partition's per-item `kind` field labels channel 10 a discovery channel, which this ruling supersedes; the field is left standing and the supersession is recorded beside it at that artifact's `the_channel_enumeration_source.the_scope_ruling`, because a registered prediction is not re-touched after the fact.

