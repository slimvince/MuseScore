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

**Home.** `CLAUDE.md:1288`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:963`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:915`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:936`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1243-1255`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1257-1275`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1277-1284`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home section.** **“The stages”** — `## The stages (in principle order)` (heading at line 19). A delegation at CLAUDE.md:177 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

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

**Home.** `cowork_audit_protocol.md:274`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:307`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the eighth ruling set of that date, X3), homed at phase 1q in `cowork_audit_protocol.md`'s dispatch-protocol section beside **D-431** and **D-434**, which is the established home for rules about how a dispatch is written and checked. **It WITHDRAWS a test the planning side had stated and this project had been working under** — *a mechanism must retire the prose it replaces, or it is apparatus growth* — and the withdrawal is recorded with its reason rather than left as a silent change of standard. The two mechanisms built under the withdrawn test are KEPT under this one, and their establishment artifacts carry their measured rates: `tools/audit/process_check_establishment.json` and `tools/audit/shell_read_guard_establishment.json`. The guard's third condition holds only while it is ARMED, which is the user's act on the user's machine; until then it is recorded as an expected-failing check rather than as coverage (`OPEN_ITEMS.md` OI-292). **★ AMENDED by the user 2026-08-03 (the eleventh ruling set, AA5) and re-taken at phase 1u: the criterion INFORMS; removal or retention is the user's ruling.** The three conditions and their stated reasons are unchanged — including the false-positive reason, *one that fires on legitimate work gets switched off, which is worse than having none*, which is why that condition exists and which survives the amendment intact. What changed is who decides the consequence. **The FORMER VERBATIM is preserved here (#12), being the text the entry carried before the amendment:** "**Ruled by the user, 2026-08-03.** A mechanism built to enforce one of these rules is kept when **it runs automatically with no human step, it has a measured detection rate against known instances of the failure it is for, and it has a measured false-positive rate at or near zero on legitimate work.** All three are measurable and none is judged. A mechanism that fails any of them is not kept: one needing a human step is a reminder, one with no measured detection rate is unestablished (#19), and one that fires on legitimate work gets switched off, which is worse than having none." **The amendment's first application is on the record in the same wave:** the shell-read guard has two shapes its established corpora do not cover — a common existence-listing command and a path outside the repository — and under the amended rule they are REPORTED and rowed for the false-deny establishment run rather than either added to the denied set unestablished or the guard treated as failing and dropped (`OPEN_ITEMS.md` OI-292, OI-300). NOT RATIFIED as an ENTRY — it goes to the user in the phase-1q ratification queue, with the amendment above added at phase 1u.

### D-437 — Phase 3 waits on the phase-2 items that could find another member of the family being designed for, not on all of phase 2

> **★ QUALIFICATION — PHASE 3 WAITS ON THE PHASE-2 ITEMS THAT COULD FIND ANOTHER MEMBER OF THE
>   FAMILY BEING DESIGNED FOR, NOT ON ALL OF PHASE 2 (user-ruled 2026-08-03).**

**In plain words.** A family design waits only on those phase-2 searches whose search space could contain a fact about the thing that family is about — for the struck-versus-sounding family, about what the decoder or the emission reads or about how candidates are admitted. Where an item's scope does not settle the question it still gates. Narrowing the gate does not open it: no fix, design or inference change is authorized, and the partition is recorded as a falsifiable prediction whose refutation by a non-gating item is a #13 STOP.

**Why.** D-231's phase gate was ratified so that a defect family is KNOWN before it is designed for — the standing one-fix-per-family rule of 2026-07-28 is what it protects. An item that cannot touch what the model reads or how candidates are admitted cannot change what the family is, so making the design wait on it buys no protection and spends time the fix plan is owed. The error in the other direction is bounded by the stated default: an item whose scope does not settle the question gates.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:1160-1178`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03, transmitted in the phase-1o dispatch cc_instruction_phase1o_gate_partition_and_probe_rerun.md §2.1; applied and homed at CLAUDE.md's D-231 entry in the recording commit per D-230. The partition itself is generated at tools/audit/phase3_gate_partition.json. **★ THE PER-ITEM VERDICTS WERE ACCEPTED BY THE USER 2026-08-03 (the eleventh ruling set, AA1) — accepted AS GENERATED, with the accounting of what the ruling's measured effect actually was recorded beside them.** That accounting is a block of the artifact, `what_the_partition_measured`, and no figure of it is restated here (#17f, D-431); its structural counts read fields rather than prose, and the one judgment a text test could not make honestly is carried as quoted sentences for the reader instead of as a number. **In plain words: most items GATE, several of them because their search space has ALREADY produced a member of the family rather than on the doubt default, and the narrowing bites in exactly one place** — the family design need not wait for phase 2's bounded trust statement to be WRITTEN, only for the gating searches to have RUN. **★ THE PLANNING PREDICTION THAT RECOMMENDED THIS RULING IS REFUTED AND IS RECORDED AS SUCH** (#17b applied to a planning claim): Cowork's decision surface said the option *"removes the largest share of the blocking for the smallest loss of rigor"*, and the second half holds while the first does not. **The RULING stands** — it was ruled by the user on its own terms and is not disturbed by its advocate's forecast being wrong; what the record must not do is let a later session inherit the expectation instead of the result. Full statement at the artifact's `what_the_partition_measured.the_refuted_planning_prediction`. **A second premise of the same wave was checked at the document and came back different too**: the claim about which of the four channels the phase-2 clause omits actually matter is not what the inventory supports, and the inventory's own statement that history mining is "run to completion" is not true at HEAD — both at `assumption_A1_of_the_phase1u_dispatch`. No verdict moved on either finding.

### D-438 — Open-items register rows whose subject is this project's own tracking and documentation apparatus gate nothing — but an establishment obligation always gates

> **★ QUALIFICATION OF RULE (b) — THE APPARATUS ROWS ARE DECLARED NON-GATING (user-ruled
> 2026-08-03).**

**In plain words.** An open row of the open-items register whose subject is this project's own tracking or documentation apparatus stays open and stays owed but blocks no stage; it is worked in leftover capacity. The test is whether the row's subject bears on the analysis, its inputs, or an instrument a measurement depends on — if yes it gates — and inside the documentation rows the line is what is owed: a pointer, anchor, label, banner, filing decision or section boundary is apparatus, while correcting a statement about the analysis or completing a specification gates. A row that is not apparatus, or whose subject its own text does not settle, gates. An establishment obligation (#19) always gates, whatever its subject.

**Why.** The open-items register is this project's own record-keeping, and a rule that lets its housekeeping block the work it exists to track inverts what it was created for; the cost of the error in the other direction is bounded by the stated default (anything not settled gates). The establishment exemption is not discretionary because backgrounding an establishment obligation is how it never happens, and #19 exists precisely because a thing merely unfalsified is not established.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:203-224`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03, transmitted in the phase-1o dispatch cc_instruction_phase1o_gate_partition_and_probe_rerun.md §3; applied and homed at CLAUDE.md's open-items register section, qualifying rule (b), in the recording commit per D-230. The derived set is generated at tools/audit/nongating_apparatus_rows.json.

### D-439 — The perspective inventory's §4 is the one home for the enumerated discovery channels, and CLAUDE.md's phase-2 clause points at it instead of listing its own subjects

> **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03;
>   D-439).**

**In plain words.** Section 4 of cowork_oi200_perspective_inventory.md is the ratified one home for the discovery channels that CLAUDE.md's phase-2 clause relies on; the clause now points at that section and lists no subjects of its own (#6). Ratified together with the scope ruling written into that section — which of the four channels the clause never named it reaches: channel 9 (history mining) is IN, being a distinct search the clause names nowhere; channels 4 and 8 are ALREADY REACHED, channel 4 because its own text makes it an obligation carried by the other probes rather than a search of its own and channel 8 because its own text makes it the audit passes and blind second pass the clause names immediately beforehand; channel 10 is NOT a discovery channel on its own account, its catalog-feeding role noted rather than dropped. The ratification does NOT adopt the inventory's §6 program in whole or in part, does NOT pull OI-200 forward, leaves that document's own §9 request open and untaken, authorizes no probe, fix, design or inference change, and does not complete phase 1.

**Why.** A binding user-directed rule was leaning on an unratified Cowork draft: D-231's phase-2 clause named *"the enumerated discovery channels"* and the only place in the record where those channels are enumerated is a document whose own banner read DRAFT and whose §9 recorded its one requested decision untaken. The ratification closes that, and pointing the clause at the ratified section instead of restating six subjects removes the second, shorter enumeration (#6) — which was also an under-naming, since the clause's six subjects are six of ten channels. The scope ruling was folded in rather than deferred because the four unnamed channels are exactly what a pointer makes ambiguous, and each verdict rests on the channel's own text rather than on a judgment made at the ruling.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:1182-1194`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03 (the twelfth ruling set: option C with option B's correction folded in), transmitted in the phase-1v dispatch cc_instruction_phase1v_channel_ratification.md §1 and §4; the reading surface the ruling was taken from is ratification_surfaces/cowork_perspective_inventory_ratification.md §5. Applied and homed at CLAUDE.md's phase-2 clause and its note, in the recording commit per D-230; the enumeration and the scope ruling themselves live at cowork_oi200_perspective_inventory.md §4, which that clause now delegates to by name. **★ THE CHANNEL-9 CORRECTION WAS MADE FIRST, DELIBERATELY.** The inventory's channel 9 said of history mining *"none new — the adjudication is this channel run to completion"*; that was untrue of both faces of the OI-207 adjudication at HEAD — its residual second pass ran on 2026-08-02, the unresolved cluster residual is live at tools/audit/decisions/disposition_manifest.json → disposition_counts.unresolved, and the owed full document reads are tracked on the OPEN_ITEMS.md OI-207 row. Both were established at those objects before this entry was written. Ruling the channel's scope while its own text said the work was finished would have ratified a contradiction, which is why the user's ruling folds the correction into the ratifying act rather than following it. The former wording is preserved verbatim at the inventory's own dated correction note (#12), as is the former CLAUDE.md note that recorded the gap while it stood. **★ WHAT IT DOES NOT DECIDE, stated because a later reader would otherwise assume more:** the §6 program is NOT adopted in whole or in part; OI-200 is not pulled forward and the inventory's §9 request — adopt, amend or reject that program — stays open and untaken; no probe, fix, design or inference change is authorized; and phase 1 is not complete. **★ WHAT IT RETIRES:** the stated workaround tools/audit/phase3_gate_partition.json carried about its structural source being an unratified draft — preserved verbatim in that artifact's `the_channel_enumeration_source.status_of_this_source.what_this_retires` and NOT deleted (#12). **No verdict of that partition moves**, and none was re-stated on the new authority: the verdicts were recorded as a prediction before the classified items ran, which is what makes them falsifiable. One consequence is reported rather than silently corrected — the partition's per-item `kind` field labels channel 10 a discovery channel, which this ruling supersedes; the field is left standing and the supersession is recorded beside it at that artifact's `the_channel_enumeration_source.the_scope_ruling`, because a registered prediction is not re-touched after the fact.

### D-473 — A theory-grounding pass labels every load-bearing claim FACT / THEORY / CONJECTURE, cross-checks its central sources independently, and carries no equation out of a text it could not fetch

> `tools/term_inventory/term_inventory.csv` (95 terms, 80 live). **Method:** five parallel deep-research
> passes with primary-source fetch (2026-07-19); every load-bearing claim labeled **FACT** (stated/measured
> in a fetched paper), **THEORY** (established published theory), or **CONJECTURE**, per #1. Verification:
> the central sources (Raphael-Stoddard, Ni et al., Temperley, Masada & Bunescu) were extracted
> independently by 2–3 agents each and cross-checked for agreement; unfetchable sources are flagged and no
> equation is carried from an unfetched text. **Nothing here decides anything** — the keep/fix/drop rows are

**In plain words.** When published research is used to justify a design, each claim is marked as either measured in a paper that was actually read, established theory, or a guess. The main papers are read by more than one pass and the readings compared. If a paper could not be obtained, nothing is copied from it — the gap is stated instead.

**Why.** Stated with the method and derivable from #1: a citation to a paper nobody read is not a fact basis, and an equation reconstructed from a snippet is an assumption wearing a citation. The document applies the rule to itself — its own source register carries a 'still unfetched/unverified (no equation carried)' list.

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_term_theory_grounding.md:6-11`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# Term-level theory grounding — the derivation half of the theory-grounding audit` (heading at line 1). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** The stated method of the term-level theory-grounding audit, in a document whose banner records it as written at the user's direction. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) It sharpens principle #17(a) rather than restating it: #17(a) requires the FACT / THEORY / ASSUMPTION labels, and the unfetched-source rule and the independent cross-extraction are this document's additions.

### D-547 — An audit's scope is generated mechanically from the code and every row gets a disposition — the auditor never chooses what to look at

> ## P1 — Enumerate-then-classify; never search
>
> The audit scope is generated MECHANICALLY from the code, not chosen by anyone: the complete
> list of (a) functions, (b) numeric literals, (c) struct fields on cross-layer surfaces,
> (d) cross-layer calls, (e) branches, for the layer under audit — produced by script (the
> #17(f) generated-artifact rule applied to audit SCOPE: no hand-chosen inventory). The
> auditor's output is a **disposition for EVERY row** — findings are not "reported", rows are
> exhausted. An item cannot be silently skipped because every item demands a verdict.

**In plain words.** What an audit covers is produced by a script from the code itself — every function, every number written into the code, every field on a shared surface, every call between layers, every branch — and the auditor must record a verdict for each one. Nothing can be passed over, because each item demands an answer.

**Why.** Stated with the rule and measured on the sweeps that preceded it: those were driven by SEARCH, so the auditor's expectations chose the queries and therefore chose the coverage. The cited proof is that one unadmitted premise was invisible to every sweep and surfaced only when a measurement contradicted it. Bias is not removed by effort; it is removed by making the audit a total function over a machine-generated domain.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_protocol.md:11-18`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The certification-audit protocol, `cowork_audit_protocol.md`, user-directed 2026-07-10 (session 36) as the protocol every per-layer certification audit must follow. Read in full by READ WAVE 4, 2026-08-04. The record states the protocol as user-directed; this step is its P1.

### D-548 — The audit's verdict set is closed with no silent escape, and 'no issue' is itself a recorded claim with a stated reason

> ## P2 — A closed verdict set with no silent escape
>
> Every row gets a verdict from a fixed rubric — premises: FACT / THEORY / ASSUMPTION;
> derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED; code: RETIRES(R1–R9) / SURVIVES;
> constants: ESTABLISHED / UNFIT / DEAD — and **"no issue" is itself a recorded claim with a
> stated reason**, auditable later. The rubric's questions are the same for every row (what
> does it assume? what does it publish? who consumes it? what happens at its edge cases?), so
> the auditor does not get to choose the questions per item — choosing questions is where
> priors leak in.

**In plain words.** Every item in an audit is answered from a fixed list of possible verdicts, and the questions asked of each item are the same. Finding nothing wrong is not silence — it is a recorded claim, with its reason, that someone can check later.

**Why.** Stated with the rule: choosing the questions per item is where the auditor's expectations leak back in, which is the same failure the mechanical scope (D-547) removes on the population side.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_protocol.md:20-28`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The certification-audit protocol, `cowork_audit_protocol.md`, user-directed 2026-07-10 (session 36) as the protocol every per-layer certification audit must follow. Read in full by READ WAVE 4, 2026-08-04. This step is its P2.

### D-549 — An audit runs in BOTH directions — from the contract to the code as well as from the code to the reader's judgment — because an absence is findable only from the contract side

> ## P3 — Audit the negative space (spec→code, not only code→intuition)
>
> Reading code and asking "does this look fine?" finds only what priors recognize. The second
> direction is mandatory: from the layer's CONTRACT (architecture docs, the layer's declared
> outputs), enumerate what the layer SHOULD handle and publish, then check each expectation
> against the code. Absences (an unpublished fact, an unhandled case, a consumer that should
> exist and doesn't) are findable only in this direction — the siloed-facts class was exactly
> this.

**In plain words.** Reading code and asking whether it looks right finds only the problems the reader already knows to look for. So an audit also starts from what the layer is supposed to do and publish, and checks each expectation against the code. Missing things — a fact never published, a case never handled, a consumer that ought to exist and does not — can be found no other way.

**Why.** Stated with the rule and grounded in a measured instance: the siloed-facts class of findings was exactly this shape, and was reachable only from the contract direction.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_protocol.md:30-37`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The certification-audit protocol, `cowork_audit_protocol.md`, user-directed 2026-07-10 (session 36) as the protocol every per-layer certification audit must follow. Read in full by READ WAVE 4, 2026-08-04. This step is its P3.

### D-550 — Every mechanism in the audit inventory carries a MEASURED fire rate beside what it claims — reading answers what it claims, counting answers what it does

> ## P4 — Behavioral characterization, not just reading (the PC-1 lesson)
>
> For every mechanism/branch in the inventory: measure its FIRE RATE on the pinned corpus with
> a cheap read-only counter (the O-10 liveness idea generalized to every branch of the audited
> layer). A mechanism that never fires, always fires, or fires wildly off its designed
> population is surfaced MECHANICALLY, no suspicion required — this is the only method in the
> set that would have caught PC-1 before EG-2 did. Reading answers "what does it claim?";
> counting answers "what does it do?"; the audit requires both columns per row.

**In plain words.** For each mechanism and each branch in the audited layer, a cheap read-only counter measures how often it actually fires on the pinned corpus. One that never fires, always fires, or fires on quite a different population than it was designed for is then surfaced by the measurement rather than by somebody's suspicion. Both columns are required per row.

**Why.** Stated with the rule: it is the only method in the set that would have caught the founding case before a later gate did, and it needs no suspicion to work.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_protocol.md:39-46`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The certification-audit protocol, `cowork_audit_protocol.md`, user-directed 2026-07-10 (session 36) as the protocol every per-layer certification audit must follow. Read in full by READ WAVE 4, 2026-08-04. This step is its P4, the lesson the record names after that founding case.

### D-551 — The audit is itself established with a MEASURED residual-error rate; an audit whose error rate is unknown certifies nothing

> ## P6 — Establish the audit itself (#19): a measured residual-error rate
>
> Randomly sample N rows (random, not "interesting" — neutral processing order throughout, so
> attention fatigue lands on random rows rather than systematically on the unglamorous tail);
> deep-verify their dispositions at objects (#15). The disagreement rate is the audit's
> measured error estimate — **the audit's completeness is then a NUMBER, not a claim.** An
> audit with an unmeasured error rate is an unestablished instrument and does not certify a
> layer (EG-7 gate not satisfied). Disagreements found in P5/P6 are #13 STOPs for the audit:
> diagnosed (which protocol step let the miss through?) before certification.

**In plain words.** A random sample of the audited rows is deep-verified against the objects themselves, and the rate at which the verification disagrees with the audit is the audit's own measured error. Completeness is then a number rather than a claim. An audit without that number is an unestablished measuring tool and does not certify a layer.

**Why.** Guiding principle #19 applied to the audit itself: a thing is trusted after being positively established, never because it is merely unfalsified. The rule also fixes the sampling as RANDOM rather than interesting, with a neutral processing order, so that attention fatigue lands on random rows instead of systematically on the unglamorous tail.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_protocol.md:69-77`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The certification-audit protocol, `cowork_audit_protocol.md`, user-directed 2026-07-10 (session 36) as the protocol every per-layer certification audit must follow. Read in full by READ WAVE 4, 2026-08-04. This step is its P6, and it is the step that makes an audit an established instrument rather than a report.

### D-552 — An audit is TWO runs in a fixed order — blind enumeration first, then the known-problem signature sweep — and certification requires both

> ## P8 — TWO RUNS, in this order (user-directed, 2026-07-10)
>
> 1. **Pass 1 — BLIND enumerative** (P1–P4, no suspects named, catalog withheld): finds new
>    types without anchoring. Types discovered here are PROMOTED into the catalog immediately.
> 2. **Pass 2 — SIGNATURE sweep** with the FULL catalog (known types + pass-1 promotions):
>    every catalog row applied across the whole layer — mechanical signatures as scripts over
>    all rows, review signatures row-by-row against the P1 inventory.
> The order matters: blind-first prevents the catalog from anchoring enumeration (which would
> re-import the bias P1 removed); signatures suffer no anchoring, so they run second at full
> strength. Pass-1-vs-pass-2 disagreements feed the P6 error estimate. Certification requires
> BOTH passes complete.

**In plain words.** The first pass is run without being told what anyone suspects, so it can find problem types nobody had named; anything it finds is added to the catalog immediately. The second pass then applies the whole catalog of known problem types across the layer. The order matters: showing the catalog first would anchor the enumeration and re-import the very bias the mechanical scope removes, while signatures cannot be anchored and so lose nothing by running second. Where the two passes disagree, the disagreement feeds the audit's measured error rate.

**Why.** Stated with the rule: blind-first prevents the catalog from anchoring enumeration, and signatures suffer no anchoring, so they run second at full strength.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_protocol.md:89-99`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** The certification-audit protocol, `cowork_audit_protocol.md`, user-directed 2026-07-10 (session 36) as the protocol every per-layer certification audit must follow. Read in full by READ WAVE 4, 2026-08-04. This step is its P8.

### D-557 — Build-it-right comes BEFORE tune-precision, strictly — no inference-problem fixing anywhere until the refactoring, the architectural design and the algorithmic completion are done

> 8. **No inference-problem-driven coding until the refactoring, the architectural design and the
>    algorithmic completion are done.** Build-it-right comes BEFORE tune-precision, strictly. All
>    three must be finished, not the last alone: every method and algorithm implemented in its
>    correct layer, the architecture designed, and the refactoring carried out.

**In plain words.** Two phases in a fixed order. First, build the system properly — carry out the refactoring, design the architecture, and finish the algorithms in their correct layers. Only afterwards comes the reactive work of asking why the analysis is not as good as hoped. All three of the first phase's parts must be finished, not the last one alone.

**Why.** The reason is given in the plan this rule was homed in until 2026-08-04: every lower-layer change ripples upward, so tuning a layer that is about to change underneath means paying for the validation twice — which is why that plan also names which of its phases may not move a corpus number at all. The widening's own defense is stated at the principle: the governing document carried a narrower width than the one being applied in practice, so a session reading only `CLAUDE.md` would have concluded that refactoring and architectural design were not among the things that must finish first.

**Status.** SUPERSEDED BY D-172 · decided 2026-06-25 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:23-26`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** ★ SUPERSEDED INTO **D-172** ON 2026-08-04, on the user's ruling R3 (READ WAVE 6, dispatch `cc_instruction_reads_6.md` Task 3; `OPEN_ITEMS.md` OI-329). The 2026-08-04 re-homing below put this rule at `CLAUDE.md` principle #8, where **D-172** already stood as that principle's entry — so two live entries recorded ONE rule at ONE home, the duplication #6 forbids. The user ruled that **D-172 survives** and this entry is recorded superseded into it, with its former home and its former text preserved here (#12). **NOTHING ABOUT THE DECISION IS WITHDRAWN OR WEAKENED:** the rule is in force at D-172, at the full three-clause width, and this entry's 2026-06-25 user-ratification of that width is carried into D-172's own provenance so the record does not read as if the widened rule were decided on 2026-08-04. This supersession is a FILING act between two entries of the same rule, not a supersession of the rule by a later ruling. ★ RE-HOMED AND WIDENED 2026-08-04 on the user's ruling (READ WAVE 5, dispatch `cc_instruction_reads_5.md` §0a ruling R2): the rule is now `CLAUDE.md` principle #8 — the ONE home (#6) — and `cowork_l1l3_stabilization_plan.md` points at it and does not restate it. The verbatim and the home above are re-taken at the new home. **THE FORMER VERBATIM, PRESERVED (#12)** — quoted from `cowork_l1l3_stabilization_plan.md:14-22` as it stood until this date: "## Ordering principle — build-it-right BEFORE tune-precision (user-ratified 2026-06-25) Two phases, strictly in order: - **Build-it-right** — refactoring + architectural design + algorithmic completion, building each layer to use **all   available evidence** (the **maximal-information** principle — *including the notated spelling / tpc capability*). This   plan's Phases 1–4, then the L4/L5/L6 algorithmic builds. **No reactive precision-chasing here.** - **Tune-precision (Phase B — LAST, after the whole L1–L6 stack is built)** — the reactive *"actively understand why   inference isn't as good as we hoped"* work: the measured key-quality levers (scale-membership), the leading-tone   de-brittling, the L3 tpc-weight calibration. **No inference-problem-fixing happens until all refactoring,   architectural design, and algorithmic completion is done.**" **THE FORMER HOME, PRESERVED:** cowork_l1l3_stabilization_plan.md:14-22. **THE FORMER PROVENANCE SENTENCE, PRESERVED:** `cowork_l1l3_stabilization_plan.md`, the ordering plan for bringing Layers 1–3 to production shape before Layer 4 is built. Read in full by READ WAVE 4, 2026-08-04. The record marks the ordering principle *user-ratified 2026-06-25*. It is the layer-stack instance of `CLAUDE.md` principle #8 and of the standing issue-exhaustion-before-fix-design rule (**D-231**), stated for this plan a month before that rule was generalized. *(Nothing about the DECISION changed: it was user-ratified 2026-06-25 in the fuller three-clause form, and the 2026-08-04 act moved that form into the governing document and widened the narrower statement standing there. The date and ratifier fields are unmoved, because a re-homing supplies neither.)*

### D-558 — An unhit branch is routed one of three ways, and defensive can't-happen code is ANNOTATED, never deleted — removing safety code to lift a coverage number is forbidden

> - **Resolve the staged scaffolding + dead branches (audit Q5 + the branch-coverage triage):** `chordslicedecoder`,
>   `redecodeRange`, `tonicizationlabeler`, and the inert `DecodeQualityLevel::Normal/Deep` each reach a **wired-or-removed**
>   verdict (decided by the Phase-5b build). The branch-coverage map's unhit directions are routed **three ways**: *add a
>   test* → fold back to the coverage backfill; *wire-or-remove* → here; *exclude as intentional-unreachable* → defensive
>   "can't-happen" code is **annotated, never deleted** (removing safety code to lift a coverage number is forbidden).

**In plain words.** Where a branch of the code is never exercised by the tests, there are exactly three lawful answers: write a test for it; decide the code should be wired up or removed; or mark it as deliberately unreachable safety code and exclude it from the count. Deleting a guard against a case that cannot happen, in order to make the coverage figure look better, is not one of them.

**Why.** Stated with the rule as a prohibition rather than a preference. The coverage figure is a measurement of the tests, so improving it by removing code measures nothing and costs the guard.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l3_stabilization_plan.md:158-162`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l3_stabilization_plan.md`, the ordering plan for bringing Layers 1–3 to production shape before Layer 4 is built. Read in full by READ WAVE 4, 2026-08-04. Stated in the plan's Phase-6 seal, where the branch-coverage triage is routed. The record states no date and no ratifier for this clause.

### D-559 — Movement in the corpus numbers is classified BY PHASE: in the foundation phases any movement at all is a bug and a STOP, in the build phases it is gated, and only the last phase tunes

> - **Three movement classes, by phase:** **Phases 1–4 do not move the numbers** (1–3 byte-identical; 4 BIR-flat, term
>   defaulted) — any movement there is a bug, STOP. **Phases 5b–8 are behaviour-changing build-it-right** (engagement,
>   legacy retirement, the L4/L5/L6 builds): they run under the **two-tier BIR gate** — **zero** class-(b)
>   (pitch-class-decidable) regressions ever; only small, every-case-verified class-(a) symmetric churn is tolerated.
>   This is *correctness/architecture* movement, **not** precision-chasing. **Phase B is the only precision-tuning** — the
>   reactive "better the inference" work, last, over the whole sealed stack.

**In plain words.** Which phase a change belongs to decides what a change in the measured numbers means. The foundation phases are supposed to leave the output identical, so any movement there is a defect to investigate rather than a result to accept. The building phases do change behaviour and run under the regression gate. Only the final phase is allowed to be about improving the numbers.

**Why.** It makes the same measurement mean different things at different times deliberately, so that a byte-identity guard cannot be quietly reinterpreted as an acceptable small regression. The plan states the consequence in terms: if the foundation phases move a number, do not refresh the pinned outputs to make it agree.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l3_stabilization_plan.md:218-223`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l3_stabilization_plan.md`, the ordering plan for bringing Layers 1–3 to production shape before Layer 4 is built. Read in full by READ WAVE 4, 2026-08-04. Stated in the plan's own Notes. The record states no date and no ratifier for this clause; the ordering it rests on is **D-557**.

### D-561 — A probe arm may not carry a component already measured net-harmful — it runs with that component disabled, and the verdict declares what it therefore does not exercise

> | G3 | **Selection:** the E0 chain runs the AS-BUILT resolver — progression-first + `attemptFineGrainOverride` UNCONDITIONAL (the Tier-1 traps, `functionresolver.cpp:221-246/529-531`) — NOT the intended selection (arc #9) | the override is measured net-harmful (−756): running it in the probe poisons the rebuilt arm with a known-bad component | **the probe arm must run with the override DISABLED** (the Phase-3 finding: "best measurable θ disables it") and must declare that the channel re-ordering is NOT exercised — the probe measures *decoder carry + argmax (+key/cadence arms as-built minus override)*, a LOWER BOUND on the intended selection |

**In plain words.** When a measurement compares a rebuilt path against the existing one, the rebuilt side is not run with a part that has already been measured to make things worse. That part is switched off for the measurement, and the report says plainly which behaviour was consequently never tested — so the result is read as a lower bound on the intended design rather than as a measurement of it.

**Why.** Stated with the gap it addresses: running the known-bad component would poison the arm under test, so a loss could not be attributed. The declaration half is what stops the lower bound being read as the thing itself.

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_eg2_scoping.md:47`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_eg2_scoping.md`, the first work item opened under the Premise Gate (Cowork, 2026-07-10, session 36). Read in full by READ WAVE 4, 2026-08-04. Recorded as gap G3 of the document's proxy-to-target ledger, which #17(d) requires each such gap to be. The record states no ratifier.

### D-562 — Where a measurement carries a declared handicap, the verdict is read ASYMMETRICALLY and the asymmetry is declared before the measurement runs

> | G1 | **Key feed:** E0 gives the decoder ONE home key (`inferLocalKey[0]`, `cc_e0_fullspine_report.md:51`); E4 feeds per-slice L3 keys | **Handicaps the rebuilt path on modulating pieces** — a rebuilt WIN under G1 is strong evidence; a LOSS is ambiguous (could be the handicap) | asymmetric read of the verdict, declared up front |

**In plain words.** If the arm under test is deliberately given less than it will eventually have, then a win is strong evidence and a loss proves little, because the loss might be the handicap. Which way the result may be read is written down before the measurement, not decided once the number is in.

**Why.** The declaration's timing is what makes it a rule rather than an excuse: an asymmetry argued after an unwelcome result is indistinguishable from special pleading, and the Premise Gate (#17b) requires the prediction to be recorded before measuring.

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_eg2_scoping.md:45`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_eg2_scoping.md`, the first work item opened under the Premise Gate (Cowork, 2026-07-10, session 36). Read in full by READ WAVE 4, 2026-08-04. Recorded as gap G1 of the proxy-to-target ledger, whose own column reads *asymmetric read of the verdict, declared up front*. The record states no ratifier.

### D-563 — The funnel's stages run strictly cheapest-first, and the plan is committed with its prediction section EMPTY before any measurement exists

> **Strictly sequential, per the #17 funnel: (1) commit this doc with §5 EMPTY (pre-registration —
> the plan is provenance-stamped before any measurement, #16/#17(b)); (2) desk sim (§4) — the
> cheapest stage runs first and may kill or reshape the probe before the establishment re-dumps
> are paid for; (3) instrument establishment (§3) only if the desk sim's filled predictions
> warrant a probe; (4) probe spec, then run.** The probe itself is read-only (explorational

**In plain words.** The order is fixed: first commit the plan itself, with the predictions deliberately blank, so that the plan is time-stamped before anything is measured; then run the paper simulation, which is the cheapest stage and may kill or reshape the measurement before the expensive preparation is paid for; then establish the measuring tool, but only if the simulation's filled-in predictions still warrant it; then specify and run the measurement.

**Why.** Two principles combined and stated as one order: reproducibility (#16) requires the plan to be stamped before any measurement, and the Premise Gate's funnel (#17) requires each stage to kill bad premises before the next one pays for them. The record calls the order a correction made at pre-registration.

**Status.** LIVE · decided 2026-07-10 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_eg2_scoping.md:147-151`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_eg2_scoping.md`, the first work item opened under the Premise Gate (Cowork, 2026-07-10, session 36). Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's §6, headed *Sequencing (corrected at pre-registration)*. The record states no ratifier.

### D-566 — STRUCTURAL fixes come before correctness fixes: never tune an inference decision while a responsibility is still in the wrong place

> **★ SEQUENCING GATE (user, 2026-06-17): STRUCTURAL fixes BEFORE inference.** This audit is QA on the
> layers + the overall architecture. Its findings are two kinds, fixed in STRICT ORDER:
> **(1) STRUCTURAL — "wrong place / missing place"** (a responsibility smeared/duplicated, a layer to split or
> merge, a missing proper layer something is compensating for) = **the C-obligations (S1–S3) + the
> decomposition flags + X2/X3.** These are fixed FIRST — they ARE "getting the architecture right," the
> precondition. **(2) CORRECTNESS — "right place, wrong output"** = the **A/B obligations (K*, C1–C4)** —
> deferred to AFTER the structure is correct. **Never tune a K1/C1 correctness fix while a responsibility is
> still misplaced** (it would tune inference on a structure about to change). So: finish the audit → phase-2
> architecture review → **fix the structural obligations (architecture phase)** → THEN inference correctness
> (on the corrected architecture).

**In plain words.** An audit's findings divide in two. Some say a job is being done in the wrong place, or is smeared across places, or has no place at all — those are fixed first, because they are what getting the architecture right means. The rest say the right component gave the wrong answer, and those wait: correcting an answer on a structure that is about to change means tuning against something that will not survive.

**Why.** Stated with the rule by the user who directed it, and it is the same reason the build-it-right ordering gives (**D-557**): work that will be invalidated by a pending structural change is paid for twice.

**Status.** LIVE · decided 2026-06-17 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_obligation_map.md:35-44`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_audit_obligation_map.md`, the phase-1 synthesis of the per-layer audits. Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's own *SEQUENCING GATE (user, 2026-06-17)*. It is an antecedent of the later, wider rule that issue-finding is exhausted before any fix design (**D-231**), stated here for the audit's own findings.

### D-567 — An audit document labels each claim TRUTH or PROVISIONAL — a claim read from the source this session stands; any quantity carried from memory of an earlier investigation does not

> **★ PROVENANCE (user, 2026-06-17 — "redo wherever you audited memory and not truth"):** This map separates
> two kinds of claim. **TRUTH = committed-object source reads done THIS session** (the mechanisms, structure,
> code logic, decomposition seams) — these stand. **PROVISIONAL = any NUMBER or any "measured (B/B2/4b/4c/4d/
> functional-residual/J-key-*)" finding carried from MEMORY of prior investigations** — these are NOT verified,
> are error-prone, and must be re-measured by CC's fresh per-layer empirical audit before they are trusted.
> Memory already produced THREE errors, all corrected by fresh source reads: **(1)** anchor "~44% pin-wrong" →
> CC's measured **27.6%** (I'd mis-cited a hard-constraint-on-contested-cases metric as piece accuracy);
> **(2)** detector fires on "I→V" → actually **V/V→V** (I→V is an ascending fifth, excluded — verified
> `cadencekeyanchor.cpp:95`); **(3)** disambiguation "inert on tonic-present-both" → only on the
> **both-complete-triad** sub-floor (verified `keymodeanalyzer.cpp:455-487`). **Treat every `[prov]`-tagged
> number below as pending CC measurement.** The map's STRUCTURE (mechanisms + the two-track verdict) is
> source-grounded and held by CC's reconciliation so far; the QUANTITIES are not.

**In plain words.** Inside an audit's own text, two kinds of statement are marked apart. What was read from the code or the record during the work stands as it is written. Any number recalled from earlier work is marked provisional and must be measured again before anything rests on it.

**Why.** Measured on the document's own output, which is why the labelling exists rather than a resolution to be careful: three claims taken from memory were each wrong and each was corrected by a fresh read of the source — a figure that turned out to be a different statistic entirely, a detector's firing condition, and the scope of a disambiguation step. The document's own summary of the pattern is that its structures and verdicts held while its quantities and attributions did not.

**Status.** LIVE · decided 2026-06-17 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_audit_obligation_map.md:22-33`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_audit_obligation_map.md`, the phase-1 synthesis of the per-layer audits. Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's own PROVENANCE block, on the user's direction of 2026-06-17 (*redo wherever you audited memory and not truth*). It is the earliest recorded instance of what became the standing prohibition on working from memory (**D-112**, user-directed 2026-07-28); this one is narrower — a labelling rule inside an audit — and carries the measured evidence that rule cites in general terms.

### D-573 — A floor measurement that collapses is a FINDING, not a failure — it is reported, not papered over

> - The mode-absent floor collapsing far below the mode-present win **is a finding, not a failure** — it
>   quantifies crutch-dependence and shapes 4b-ii; report it, do not paper over it.

**In plain words.** When a support is deliberately removed to find out how much the analysis was leaning on it, a large drop is the answer to the question, not a regression. It is reported as measured and used to aim the next step.

**Why.** Stated as a stop condition of the implementation, which is what makes it binding rather than encouraging: it sits in the list of things that must halt the work, next to the two conditions that genuinely do halt it, and says explicitly that this one does not.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/stage4b_design.md:196-197`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4b_design.md`, the Stage-4b design implementing the user's ratified Stage-4 redirect; the staged approach was chosen by the user 2026-06-14. Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY key path** (`keymodeanalyzer` / `keyresolver`), which the joint estimator replaced on both surfaces. Recorded as the document's §7 stop conditions. Unlike D-571 and D-572 this clause is a MEASUREMENT rule, not a scoring term, so it is not legacy-scoped: it binds any future ablation that removes a support to size its contribution.

### D-574 — The pass-bar for a measured change is set AFTER the baseline measurement, so the threshold is data-grounded rather than guessed

> | 6 — mode-absent pass-bar | **Set after 4b-i's floor measurement** (data-grounded). Dossier's ≥70% of the +378 is the starting reference; **user ratifies the number** once the floor is known. |

**In plain words.** How much of a drop would be acceptable is not decided in advance. The measurement runs first, the size of the effect becomes known, and only then is the bar the work must clear set — by the user.

**Why.** Stated with the disposition and defended by what it avoids: a threshold chosen before the effect is known is a guess that the work will then be tuned against. The document names the earlier proposal's number as a starting reference rather than a bar, and reserves the decision to the user.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/stage4b_design.md:146`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4b_design.md`, the Stage-4b design implementing the user's ratified Stage-4 redirect; the staged approach was chosen by the user 2026-06-14. Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY key path** (`keymodeanalyzer` / `keyresolver`), which the joint estimator replaced on both surfaces. Recorded as disposition OQ6 of the document's open-question table, and confirmed in its §6 ratification asks. Like **D-573** this is a measurement rule rather than a scoring term and is not legacy-scoped. It stands beside the standing requirement that a fit declares its held-out data and capacity budget BEFORE fitting (#20) — that rule fixes what is declared early, this one fixes what may not be.

### D-577 — An audit verdict distinguishes DESIGN debt from MIGRATION debt — the wrong cut, versus the right cut whose legacy is not yet retired

> dirs) and `src/composing/tests/`. Built from three parallel source audits, with every load-bearing claim re-verified
> by Cowork at the file. Each finding is cited; verdicts distinguish **design debt** (wrong cut) from **migration debt**
> (right cut, legacy not yet retired) — almost everything here is the latter.

**In plain words.** When an audit finds the code departing from the intended architecture, it says which of two things it found: that the division of responsibilities is itself wrong, or that the division is right and the old implementation simply has not been removed yet. The two need entirely different work and must not be reported as one kind of finding.

**Why.** The distinction earns its place in the audit's own result: almost every deviation it found was the second kind, so a report without the distinction would have read as an indictment of the architecture when the architecture was sound and the schedule was the issue. The audit states that conclusion as its through-line.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l4_architecture_audit.md:13-15`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l4_architecture_audit.md`, the read-only L1–L4 audit of 2026-06-26. Read in full by READ WAVE 4, 2026-08-04. Recorded in the document's own status banner as the vocabulary its verdicts use. The record states no ratifier.

### D-578 — An orphan claim requires a WHOLE-REPOSITORY search; a per-directory one produces false orphans

> - **Orphaned test fixtures — CORRECTED 2026-06-26 (the original list was partly wrong; CC re-verified whole-repo).**
>   Confirmed orphan, zero references: **only** `chord_analysis_test.{musicxml,_expected.json,py}` (literal "content
>   moved" stubs). **NOT orphans:** `mono_smoke_test.musicxml` is loaded and asserted by
>   `tools/test_batch_analyze_regressions.py:117,137` *(Cowork-verified)* — the original audit used a negative-grep
>   scoped to `src/composing/tests/` and missed the `tools/` caller; `data/solid theory.musicxml` is provenance-
>   referenced in `note_model_tests.cpp` comments (not a clean orphan). Lesson: orphan claims need a **whole-repo** grep,
>   not a per-dir one.

**In plain words.** Saying that a test fixture or a file is unused is a claim about the entire repository, so it has to be checked against the entire repository. Checking only the directory the file lives in reports files as unused when the thing using them lives somewhere else.

**Why.** Measured on this audit's own error: a search scoped to one test directory reported a fixture as an orphan when a script in the tools directory loads and asserts it, and a second file was called an orphan while being referenced from a test's comments. The audit records the correction and states the lesson in its own words.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l4_architecture_audit.md:110-116`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l4_architecture_audit.md`, the read-only L1–L4 audit of 2026-06-26. Read in full by READ WAVE 4, 2026-08-04. Recorded as the correction to the audit's own orphaned-fixture finding, with the two false orphans named. The record states no ratifier. It is the search-scope instance of the general defect the catalog carries as scope-assumed enumeration (`DEFECT_TYPES.md` DT-26).

### D-592 — What FINISHED means for a layer, as the user's standing bar: restructured, built, dead code resolved, legacy retired, regression- and reachable-branch-tested, specs synced — nothing left

> **Purpose.** Enumerate **everything** still outstanding on L1–L4 so "finished" is well-defined and nothing falls
> through — the precondition for the **L1–L4 COMPLETE (nothing-left)** gate before L5. "Finished" (the user's standing
> bar) = each layer **restructured + built + dead-code resolved + legacy retired + regression/reachable-branch tested**,
> specs synced to as-built, **nothing left**.

**In plain words.** A stage of the analysis counts as finished only when all of six things are true: it has been restructured into its proper shape, built, its unused code resolved one way or the other, the old code it replaces retired, its behaviour pinned by tests including the branches that can actually run, and its written specification brought into line with what was built. Anything outstanding means it is not finished.

**Why.** The reason is the ledger's own purpose: 'finished' had to be well-defined before it could be a gate, and an undefined bar lets a layer be declared complete while residue remains. The bar is recorded as the user's standing one rather than derived here.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l4_completion_ledger.md:48-51`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l4_completion_ledger.md`, the no-residue completion map for Layers 1-4 (2026-06-26). Read in full by READ WAVE 5, 2026-08-04. The ledger states the bar as *the user's standing bar*. It is what **D-557** / `CLAUDE.md` principle #8 means by the algorithmic completion being DONE, and no other home states the six conditions.

### D-593 — The line inside the build-it-right firewall: plain correctness bugs are allowed now, accuracy on hard cases is not — and a KNOWN WRONG ANSWER on the key axis is on the forbidden side

> The line, because it WILL blur during the finish:
> - **Build-it-right (allowed now / during the L4 build):** architecture, each layer's algorithmic completion per its
>   spec, and plain **correctness** bugs — crashes, contract violations, rendering errors (e.g. **C7 German-bass slash**).
> - **Tune-precision / inference improvement (Phase B — LAST):** making the analysis *more accurate on hard/ambiguous
>   cases* — the scale lever, leading-tone de-brittling, tpc-weight calibration, ambiguous-case accuracy.
> - **The trap, live in this ledger:** the **leading-tone presence-gate / Mozart C→F key regression is INFERENCE-QUALITY
>   → Phase B → DO NOT TOUCH during the finish**, even though it is a known wrong answer. It is pinned only as a labelled
>   regression-guard. Fixing the *key misread* is precisely the inference work the firewall defers.

**In plain words.** The rule that no accuracy work happens until the system is built right needs a line, because the two sides look alike while finishing. A crash, a broken contract or a rendering error is a plain bug and may be fixed now. Making the analysis get a hard case right is not, and the test case is named: a piece whose key the program reads wrong stays wrong, pinned by a labelled guard, because fixing it is exactly the deferred work.

**Why.** The reason for drawing the line at all is stated with it — it WILL blur during the finish, so the boundary is written down before the pressure arrives, which is the same discipline `CLAUDE.md` #22 states for gates. The worked case is what makes it operational: a known wrong answer is the hardest thing to leave alone, so the record names one and forbids touching it.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l4_completion_ledger.md:61-68`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l4_completion_ledger.md`, the no-residue completion map for Layers 1-4 (2026-06-26). Read in full by READ WAVE 5, 2026-08-04. Recorded under the ledger's own STANDING FIREWALL heading, marked *user mandate, reaffirmed 2026-06-26*. It is the operational boundary of **D-557** / `CLAUDE.md` principle #8, which states the rule but not where the line falls. The Mozart key regression it names is the subject of the session-memory entry `project_k279_key_regression_diagnosis.md`; whether the joint estimator that now runs reproduces it is NOT stated here and is not asserted.

### D-596 — The north star: BEST means CORRECT — every obligation is judged against the ground-truth oracle and never against whether it passes a proxy gate

> **★ NORTH STAR (user, 2026-06-17): the goal is the BEST possible inference, where BEST = CORRECT.** Every
> per-layer obligation is judged against the **true analysis** — the DCML / music21 ground-truth oracle where
> the layer's output is checkable — NOT against whether it passes a proxy gate (BIR / rn_agree). A layer can
> pass the gate and still be WRONG on cases the gate never sees; those are precisely the obligations we want.
> Keep the established metric discipline: the oracle is the correctness standard (never game a proxy), and
> **separate genuine incorrectness from convention-boundary ambiguity** (cases where analysts themselves
> disagree = the honest floor, not a fixable error).

**In plain words.** A stage of the analysis is judged by whether its answer is right, measured against the published human analyses — not by whether it passes the regression check. A stage can pass the check and still be wrong everywhere the check does not look, and those cases are exactly what an audit is for. Cases where the human analysts disagree with each other are a floor, not a fault to be fixed.

**Why.** The reason is stated in the decision: a gate is a proxy with a limited reach, so passing it is compatible with being wrong on everything outside it. The second half is the same distinction `CLAUDE.md` #21 later generalises — without separating annotator disagreement from structural error, the residual cannot be interpreted.

**Status.** LIVE · decided 2026-06-17 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/layer_audit_plan.md:11-17`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/layer_audit_plan.md`, the combined layer-audit plan. Read in full by READ WAVE 5, 2026-08-04. Marked *user, 2026-06-17* in the plan's own header block. It states for the AUDIT what the grading conventions in `CLAUDE.md` gate block (A) state for the measurement — the human annotation is the only ground truth — and it is the standard the obligations this plan produced were written against. The algorithmic second opinion it names beside the human annotation is a noise filter under that convention, not a standard of correctness.

### D-597 — The layer audit runs in two phases in a fixed order — every layer audited ALONE first, the architecture reviewed second on the accumulated findings

> - **Phase 1 — per-layer isolation audits.** Each layer audited alone: state its single responsibility, audit
>   correctness + completeness against THAT responsibility only (inputs assumed correct, consumers ignored),
>   pin gaps as that layer's obligations. Order within phase 1 is pure prioritization (each audit is
>   independent) — sequenced by value below, but any order is valid.
> - **Phase 2 — architecture review.** AFTER phase 1, using its accumulated findings: are these the *right*
>   layers, is any responsibility split / duplicated / misplaced across layers, and do the layers depend +
>   compose correctly (feed-forward vs circular, the seams, the bolt-ons). Phase 1's depth feeds phase 2.

**In plain words.** Each stage of the analysis is examined on its own first: what is it responsible for, does it do that correctly, does it cover every case its responsibility implies — with its inputs taken as given and its consumers ignored. Only afterwards is the question asked whether these are the right stages at all and whether they fit together. The order matters between the two; inside the first it does not.

**Why.** Stated with the decision: phase 1's depth is what phase 2 reasons from — whether a responsibility is split or misplaced is only visible once each layer's own responsibility has been stated and tested. Interaction gaps are explicitly excluded from phase 1 for the same reason.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/layer_audit_plan.md:23-29`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/layer_audit_plan.md`, the combined layer-audit plan. Read in full by READ WAVE 5, 2026-08-04. Recorded in the plan's §1. Distinct from **D-552**, which fixes the order of the TWO RUNS of a single audit (blind enumeration first, then the contract-driven pass); this fixes the order of the two PHASES of the layer-audit programme. The record states neither a date nor a ratifier for this item.

### D-599 — Adjudication method: apply the standing principles FIRST, and only where they do not decide is there a genuine user choice — what remains for the user is ratifying the derivation, not picking an option

> **Method: apply the standing principles first; only where they do NOT
> decide is there a genuine user choice.** Result: the principles decide essentially
> everything; what remains for the user is ratifying the derivations (#14), not choosing among
> arbitrary options.

**In plain words.** When a list of open questions is put to the user, each one is first run against the project's standing principles. Most are settled by them, and what the user is then asked to do is confirm the reasoning rather than choose between alternatives. Only a question the principles genuinely leave open is presented as a choice.

**Why.** Measured on the population it was applied to: of the seven audit rows, six were pure rule applications and exactly one was a genuine acceptance the principles did not settle. The dossier's own result is the defense of its method.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_adjudication_dossier.md:6-9`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_adjudication_dossier.md`, the 2026-07-10 user-directed adjudication of the structural audit's open rows and the siloed-fact findings. Read in full by READ WAVE 5, 2026-08-04. The dossier records the method as user-directed and its result as RATIFIED by the user 2026-07-10. It is the working form of `CLAUDE.md`'s decision-surface rule (the whole situation is explained before any choice question) — that rule governs HOW a decision is put; this governs WHICH questions are decisions at all.

### D-602 — A layer's measurement is judged on coverage-matched accuracy AND correct abstention, never on raw coverage — abstaining on a genuinely undecidable case is a RIGHT outcome

> - **The gate criterion (the L4 lesson).** Judge each measurement by **coverage-matched accuracy + correct
>   abstention**, never raw coverage — abstaining correctly on a genuinely function-undecidable slice is a *right*
>   outcome.

**In plain words.** When a stage of the analysis is measured, two things are reported together: how accurate it is over the cases it actually answered, and whether the cases it declined were ones it should have declined. How MANY cases it answered is not the measurement — declining a case that genuinely cannot be decided at that stage is a correct answer, not a gap.

**Why.** Recorded as the lesson of the preceding layer's build, where the decoder was measured materially better than the legacy path WHERE IT COMMITS and about eighty-five per cent of its abstention was established as genuinely function-dependent — a figure that raw coverage would have read as failure. It is also the reason the granularity-robust stop is abstain-aware (**D-212**): an agreement percentage that ignores abstention is reducible by declining more often.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_phase5c_l5_build_plan.md:27-29`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“The build discipline”** — `## The build discipline (every step)` (heading at line 16). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_phase5c_l5_build_plan.md`, the Layer-5 build plan, DRAFT 2026-06-26. Read in full by READ WAVE 5, 2026-08-04. Recorded in the plan's build-discipline block. Its companion in the same block — build the mechanisms right at their defaults and stop, do not chase accuracy — is the proportionality rule **D-480** already carries for the phrase-boundary primitive, stated here for the function layer and not re-entered (#6). The record states no ratifier for the gate criterion.

### D-603 — While the pipeline is being rebuilt, a behaviour-changing increment is graded DIRECTIONALLY and not against a fixed bar — meaningful comparison happens only against the fully reconstructed pipeline

> **★ METRICS ARE PROVISIONAL — grade DIRECTIONALLY, not against a fixed bar (user, 2026-06-22).** The Increment-B
> baseline numbers (held-out Baroque 87.3% / Jazz 61.5%) **and the metric definitions** WILL move as the rest of the
> pipeline (L4–L6) is reconstructed/refactored. **Meaningful comparison happens only against the fully reconstructed
> pipeline**, not increment-by-increment.

**In plain words.** While the stages below and above are still being rebuilt, both the numbers and the way they are measured will keep moving. So a rebuild step is judged by whether it moved the specific defects it was meant to move in the right direction, not by whether it beat a number recorded earlier. The comparison that means something is against the finished pipeline.

**Why.** The reason is stated with the decision: the baseline figures AND the metric definitions themselves will move as the rest of the pipeline is reconstructed, so a fixed bar set now would be a bar against a measurement that no longer exists when it is tested. It is the same reasoning `CLAUDE.md` #16 and #24 apply to instrument and sampling error, applied to a measurement whose definition is still in motion.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer3_keymode_impl_design.md:83-86`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“§4”** — `## §4 — Metric / gates (Increment C — the behavior-changing one)` (heading at line 82). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_layer3_keymode_impl_design.md`, the Layer-3 key/mode implementation design. Read in full by READ WAVE 5, 2026-08-04. Marked *user, 2026-06-22* at the head of the design's metric section. Read alongside **D-574** — the pass-bar for a measured change is set AFTER the baseline is measured — which governs how a bar is set once one is set at all; this governs whether a fixed bar is admissible during a rebuild.

### D-611 — The tidy guardrails, in three tiers — and the dormant path and its staged scaffolding are DEFERRED-ENGAGEMENT, not dead code: removing them is a STOP

> - **MUST NOT touch:** inference accuracy (the leading-tone C→F gate, scoring tuning — firewall, Phase B); the
>   **dormant new-L4 path and the staged scaffolding** (`chordslicedecoder`, `redecodeRange`, `tonicizationlabeler`,
>   `DecodeQualityLevel`) — they are *deferred-engagement*, NOT dead-code-to-delete (their wire-or-remove verdict is the
>   joint L4+L5 engagement). Removing them is a STOP.

**In plain words.** During a tidying pass, documentation, orphaned test data, stale tests and stale comments may be cleaned up freely; anything that changes behaviour goes through the regression gate. Two things are off limits entirely: making the analysis more accurate, and deleting the built-but-inactive components. Those components look like unused code and are not — the decision about whether to wire or remove them belongs to a later step, so removing them stops the work.

**Why.** The reason is named in the decision: the wire-or-remove verdict for the staged components belongs to a specific later step, so a tidying pass deleting them would take that decision by default at the wrong stage. It is the tidying-pass form of the same rule **D-558** states for an unhit branch — defensive can't-happen code is annotated, never deleted — and of the retirement map's principle that nothing retires by silence (**D-418**).

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_l1l4_review_charter.md:22-25`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_l1l4_review_charter.md`, the step-3 QA charter, context ratified 2026-06-26. Read in full by READ WAVE 5, 2026-08-04. Recorded in the charter's Standards block, which states the three tiers together: freely tidy, tidy only byte-identical or gated, and must not touch. ⚠ The components it names are on the LEGACY/dormant side; their retirement is the OI-180 map's business and this entry does not schedule it.

### D-617 — A perfect-detection CEILING is never banked — the realized fraction is measured before the mechanism is wired into production scoring

> **The risk.** The investigation's "≈91% / ~1259 regions addressable" is a **perfect-detection CEILING**
> (hint-parity). A real note-derived cadence detector is imperfect; the **realized** fraction is bounded by
> detection reliability, which is **unmeasured**. So this design's first obligation is to **measure realized
> detection BEFORE wiring it into production scoring** — never bank the 91%.

**In plain words.** A figure saying how much of a problem a mechanism could address if it worked perfectly is not a figure for how much it will address. The share it actually reaches depends on how reliably it fires, and that is a separate measurement, taken before the mechanism is connected to anything that decides an answer.

**Why.** The reason is stated with the rule: the addressable figure was computed at hint-parity — as if detection were perfect — while real detection reliability was unmeasured, so the two quantities differ by exactly the unmeasured term. The design also names what a shortfall MEANS rather than treating it as failure: a realized fraction far below the ceiling is itself the finding, and the answer is richer detection or an escalation of the architecture question, never wiring a weak detector through.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Home.** `docs/stage4c_cadence_key_design.md:26-31`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4c_cadence_key_design.md` §1, DRAFT and ratification-gated, 2026-06-14. Read in full by READ WAVE 6, 2026-08-04. Recorded as the design's own first obligation and repeated in its §8 stop conditions. It is the measure-before-build gate (**D-279**) stated for a specific quantity, and it is the discipline the case that follows vindicated: the local key-agnostic cadence approach was later measured at its precision ceiling and falsified (**D-290**) rather than shipped on the ceiling figure. The record states no ratifier.

### D-626 — A scoring term lands together with its tuning — a dormant weight-zero term is code with no effect and no test that exercises its effect

> **Phase 4 builds the shared primitive only; it does NOT touch the Architectural Layer 3 key emission.** The ratified
> scope keeps the L3 spelling *term* together with its *tuning*: the line-of-fifths / modulation-direction term in the
> `keymodeanalyzer` scorer, **and** the weight that realises it, both land in **Phase B**, where the precision work
> lives. Reason: a dormant weight-0 L3 term would be code with no effect and no test that exercises its effect; landing
> the term *with* its calibration (where the stable-region cost is measured and Layer-5 function can gate the
> tonicization-vs-modulation call) is cleaner under "build-it-right **then** tune-precision."

**In plain words.** A new term in a scoring formula is not added ahead of the number that gives it force. Added early with a weight of zero it changes nothing, so no test can show it works, and it sits in the code as something nobody has exercised. It is written when the step that fits its weight arrives.

**Why.** Stated with the decision, and it is the one place the build-it-right-before-tune-precision ordering could be misread as forbidding the pairing: a term whose weight is zero is not a built mechanism but an unexercised one, so building it early buys no capability and costs a test surface that cannot exist. The exception it does not disturb is stated in the same document — a primitive with a real consumer is not premature.

**Status.** LIVE · decided 2026-06-26 · ratified by user

**Home.** `cowork_tpc_capability_design.md:53-58`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_tpc_capability_design.md` §2, marked *scope ratified (option B, 2026-06-26)* in the document's own status block. Read in full by READ WAVE 6, 2026-08-04. It qualifies **D-172** / `CLAUDE.md` #8 at the seam where the two phases meet: the ordering defers tuning, and this says a term whose only content is its tuning defers with it rather than landing inert ahead of it. Distinct from **D-558**, which forbids DELETING an unexercised branch; this governs whether one is created.

### D-627 — The CONTRACT ships first behind a correct byte-identical interim; the efficiency is a separate deferred step that never blocks the layers above it

> - **1a — the contract, with an interim that is correct and byte-identical.** `build(selection)` and `extend` present
>   the full bounded-context API, but **internally may still walk the whole score and retain the notes overlapping the
>   loaded span**, and **rebuild the static index** over the loaded set on build and on each extend. This is trivially
>   correct (the whole-score walk already captures every note, including sustained-in ones — Section 4 is free), it is
>   **byte-identical to today on the degenerate case** (selection = score → retain everything → identical), and it gives
>   the layers above the real API to build against. Performance is *not* improved yet — that is the point: ship the
>   contract, not the optimisation.
> - **1b — the efficiency, byte-identical, DEFERRED (can land after L4).** Replace the interim with (i) a walk scoped to
>   the loaded span plus a leading-edge "sounding-at-`loadedStart`" lookup (Section 4), and (ii) an **extensible index**
>   (Section 5). **Gate:** byte-identical to 1a, and `index ≡ linear scan` over extended spans. Because 1b changes no
>   behaviour, it is purely a performance step and never blocks the layers above.

**In plain words.** The interface a stage promises is delivered first, with an implementation behind it that is obviously correct and produces exactly today's answers even though it does no less work than before. The faster implementation is a separate step, judged only on producing the same bytes, and because it changes nothing it can be done at any time without holding up the stages built on top.

**Why.** The reason is stated with the split and it is a risk argument: the genuinely hard parts — capturing a note that sounds across the edge of the loaded span without walking the whole score, and an index that accepts insertions — are isolated from the contract, so the foundational correction lands immediately while the tricky code waits behind a byte-identity gate. It is the same sequencing the make-it-work-first rule states generally: work that only makes the same computation faster is exhausted last, and never before the contract it serves exists.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_layer1_extend_design.md:50-60`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_layer1_extend_design.md` §3, the Layer-1 build-over-a-selection and extend detail design, DRAFT for sign-off. Read in full by READ WAVE 6, 2026-08-04. The record shows the split was carried out — the register already carries the as-built note that the span-scoped walk is what remains — and the same two-level shape is used one layer up for the incremental re-slice. The record states neither a date nor a ratifier for this item.

### D-633 — A cause-classifier is established BEFORE its results are read — its totals must reconcile exactly with the established agreement column, and every failing run gets exactly one cause from a closed list

> 2. A classifier over the existing dumps and the ground truth: every
>    key-disagreeing run labeled with exactly one primary cause from the closed list
>    above, plus the carried/absent and outranked flags and the leading-tone
>    presence test. No new production output surface — read what is already dumped.
> 3. Establishment before reading results: the classifier's totals must reconcile
>    exactly with the established key-agreement column (classified failing duration
>    equals the reference failing duration, per preset), and grading coverage is
>    reported beside every figure (the abstention caveat, row OI-33).

**In plain words.** Before any conclusion is drawn from a tool that sorts failures into causes, the tool has to account for exactly the amount of failure the established measurement reports — no more and no less. Each failing stretch gets one cause and only one, chosen from a list fixed in advance, and how much of the material could be graded at all is reported next to every figure.

**Why.** It is the establishment principle applied to a diagnostic rather than to an inference: a classifier whose totals do not reconcile with the measurement it decomposes is unfalsified rather than established, and its shares would be shares of an unknown denominator. The single-cause rule and the closed list are what make the shares add up at all; the coverage report is the abstention convention, without which a share can be moved by declining to grade.

**Status.** LIVE · decided 2026-07-12 · ratifier not stated

**Home.** `cowork_key_mode_inference_diagnosis.md:87-94`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_key_mode_inference_diagnosis.md` §3, the Premise-Gate opening for the key/mode diagnosis, written 2026-07-12 with its predictions registered before any measurement (#17b). Read in full by READ WAVE 6, 2026-08-04. The document is otherwise a registered PREDICTION rather than a decision surface — its candidate causes carry written quantitative ranges precisely so they can fail — and this is the one clause in it that binds any future diagnostic of the same shape. The record states no ratifier.

### D-634 — Where the specification and the code diverge on a music-theoretic question, THE SPECIFICATION IS THE CORRECT REFERENCE and the code goes on the build backlog

> - **D1 — membership cue-combination.** The **spec is the correct reference**, not the code. Music-theoretically the
>   code's `weak OR stepwise → NCT` is wrong in two quadrants: it marks a *weak leap* (an arpeggiated extension) a
>   non-chord tone, and it marks *every* strong-stepwise note a non-chord tone rather than only the accented passing
>   tone over a clear prevailing chord. The spec's `weak AND stepwise` rule plus its two hard cases is the right
>   behaviour. → **L4 code backlog; no spec change.**

**In plain words.** When the written design and the built code disagree about a question of music theory, the design is treated as right and the code as owing a fix — not the other way round. The disagreement is written down as work, and the design is left alone.

**Why.** Decided at the music rather than by precedence, which is what makes it a disposition rather than a preference: the code's rule was traced through the cases it decides and found wrong in two of the four, marking an arpeggiated leap a decoration and marking every accented step one regardless of the harmony under it. The design's rule handles both. The second finding disposed the same way is sharper still — the built penalty charges the opposite of what the design specifies, so it cannot make the discrimination the design exists for.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_delta_check_dispositions.md:21-25`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_delta_check_dispositions.md`, the Cowork verification and per-layer disposition of the Layer-1-to-Layer-4 specification-versus-implementation delta check. Read in full by READ WAVE 6, 2026-08-04. Both dispositions were verified at the source by Cowork directly rather than taken from the report they respond to. ⚠ The code they dispose is the DORMANT Layer-4 decoder, which the document states affects no shipped output. The record states neither a date nor a ratifier. It is the resolution rule the doc-sync principle #10 leaves open: sync says the two must agree, this says which one moves.

### D-636 — The per-step build method: INVESTIGATE, BUILD, VERIFY, ASSESS-FOR-AMENDMENT — no step starts before the prior step's assessment, and a surprise pauses the sequence

> **Method per step (non-negotiable):** **INVESTIGATE (CC, read-only) → BUILD → VERIFY (Cowork, by-sha + source) →
> ASSESS-FOR-AMENDMENT.** No step starts before the prior step's assessment is in. A surprising finding pauses the
> sequence and re-plans — that is the point of going incremental.

**In plain words.** Each step of a staged build runs in the same four parts: find out what is actually there, build, check the result at the committed code rather than at a report, and then ask whether what was learnt changes the steps still to come. The next step waits for that last part, and anything surprising stops the sequence rather than being worked around.

**Why.** The reason is stated with the method: going incrementally buys nothing unless each step's findings can amend the steps after it, so the assessment is what the increments are for. Its worth is on the record in the same plan — the grounding step measured the new path fifteen points behind the old and located the whole gap in one unbuilt mechanism, which re-ordered the remaining steps to attack that mechanism first.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_phase5b_l4_build_plan.md:8-10`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_phase5b_l4_build_plan.md`, the Phase-5b incremental Layer-4 build plan. Read in full by READ WAVE 6, 2026-08-04. Marked *non-negotiable* in the plan's own header block. It is the staged-build instance of the surprise-is-a-STOP rule (#13) and of the funnel #17 states — desk-simulate, probe, build — with the addition that names it: the assessment step, which is what lets a finding amend the plan rather than only the code. The record states neither a date nor a ratifier.

### D-637 — Engaging a different DECOMPOSITION will move the corpus output — that movement is the gated behaviour change, not a byte-identity violation

> The legacy path is **per-region** (`greedyExpandSegmentation` + `analyzeChord` + `ChordPathDecoder`). The new path is
> **per-slice** (`changePointSlices` + `chordslicedecoder`). They are *different decompositions*, so engaging the new path
> **will move the corpus output** — that movement is the behaviour change we gate, not a byte-identity violation. We build
> and prove the new path **before** any switch.

**In plain words.** The old and new ways of analysing chords divide the music up differently, so switching to the new one is bound to change the answers. That change is the thing the regression gate exists to judge; it is not a sign that something went wrong with a change meant to produce identical output. Until the switch, the new path is built beside the old and produces nothing.

**Why.** It follows from what the two paths ARE, and the plan states it so the gate is not misread: one groups the music into regions and the other into change-point slices, so identical output would be a coincidence rather than a target. Naming the distinction in advance is what keeps a byte-identity gate meaningful for the increments that precede the switch — each of those really is byte-identical, because the new path is dormant.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_phase5b_l4_build_plan.md:18-21`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_phase5b_l4_build_plan.md`, the incremental shape section. Read in full by READ WAVE 6, 2026-08-04. It is the distinction the migration-state principle #23 needs to be operable — a declared parallel build produces two paths, and the switch between them is a ratified behaviour change rather than a broken invariant. The same shape governed the notation switch, whose diffs were reconciled against classified evidence rather than expected to vanish. The record states neither a date nor a ratifier.

### D-640 — A count of outstanding work is derived from state at HEAD, never taken from the membership of a list of asks or from an authored disposition beside a row

> ### A count of OUTSTANDING work is DERIVED from state, never taken from the membership of a list of asks
>
> **Ruled by the user, 2026-08-04** (dispatch `cc_instruction_phase1_delegations_and_corrections.md`,
> R4). A figure reporting how much of something is still owed is computed from the CURRENT STATE of
> each candidate, at HEAD. It is **never** taken from the length of a list that records what was asked
> for, and never from an authored disposition field written beside the row when the ask was made.
> **A list of asks carries no state**, and #12 keeps a satisfied ask in it rather than deleting it — so
> its membership counts asks EVER MADE, which is a different quantity and is always the larger one.
>
> *Why:* measured at the instance that produced the ruling. The OI-293 / OI-327 **write list** — the
> homes the record means to keep, each awaiting a delegation only the user may write — was read two
> ways at once, and both were wrong in the same direction:
>
> 1. **The count was the list's length.** `tools/audit/gen_phase1_completion_inventory.py` reported
>    `documents_awaiting_a_delegation_only_the_user_may_write` as `len(write_list)`, inside the artifact
>    a phase-1 completion statement would rest on. Derived at HEAD from the delegation grades and the
>    home data, the figure is a small fraction of it — and the derivation additionally names a document
>    the write list never carried, so the list was wrong in both directions at once about WHICH
>    documents are outstanding.
> 2. **The per-row state was an authored field, and a second one was appended beside it.** Each row
>    carries a `disposition_2026_08_04`; read wave 6 then answered two of those rows in a NEW field,
>    `disposition_2026_08_04_wave6`. The reader read only the first and published *"NOT WRITTEN —
>    WITHHELD"* for a document the user had since delegated to, and for one the user had ruled is not a
>    delegation target at all.
>
> **The remedy is not a status field on the list** — that is the same authored-field hazard a third
> time. The list keeps its role as the record of what was asked for, with each draft wording and each
> reason (#12), and **states in its own data that its membership is not a count of outstanding work**;
> the STATE is derived, at `tools/audit/decisions/outstanding_delegations.json`. This is the general
> form of the same shape `OPEN_ITEMS.md` **OI-283** and the figures rule above already carry: a
> recorded finding that is never marked discharged becomes a count of work that is no longer owed.
> Tracked at `OPEN_ITEMS.md` **OI-335**.

**In plain words.** When a report says how much of something is still owed, that number is computed from what is true now about each candidate. It is never the length of the list that records what was asked for, and never read off a status sentence someone wrote beside a row when the ask was made. A list of asks has no status of its own, and the project's no-information-loss rule keeps a satisfied ask in it rather than deleting it, so its length counts asks ever made rather than asks outstanding — always the larger number.

**Why.** Measured at the instance that produced the ruling, and stated with it: the OI-293 / OI-327 write list was read both ways at once, and both readings overstated the work. The completion inventory reported the count as the list's length; and each row's state was an authored field to which read wave 6 appended a SECOND field, so a reader taking the first published 'NOT WRITTEN — WITHHELD' for a document the user had delegated to and for one the user had ruled is not a delegation target. The remedy deliberately is NOT a status field on the list — that is the same authored-field hazard a third time — but a derived view, `tools/audit/decisions/outstanding_delegations.json`, with the list keeping its role as the record of what was asked for (#12). It is the general form of OI-283's shape and of the figures rule D-431 states one section above it.

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `cowork_audit_protocol.md:235-266`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_phase1_delegations_and_corrections.md` §0a as R4 — 'the outstanding delegation population is DERIVED at HEAD from the delegation grades and the home data — never taken from the write list, which carries no state and therefore cannot distinguish written from unwritten'. Homed in `cowork_audit_protocol.md` beside D-431, the figures rule whose shape it generalizes; `nonspec_kind` is `process` because its subject is how the work is measured and reported, not the system. Tracked at `OPEN_ITEMS.md` OI-335.

### D-641 — A finding that bears on the analysis is surfaced to the user whatever its size; a finding about this project's own apparatus is rowed and left, and gets no wave

> ### A finding that bears on the analysis is SURFACED whatever its size; an apparatus finding is ROWED AND LEFT
>
> **Ruled by the user, 2026-08-04** (dispatch `cc_instruction_commit_and_finish_line.md`, R3). Every
> finding a session makes is sorted by **D-438's own test**, and by nothing else: *does the finding's
> subject bear on the analysis, on the analysis's inputs, or on an instrument a measurement depends
> on?*
>
> - **If YES — it is SURFACED to the user for decision, WHATEVER ITS SIZE.** Not held for a later
>   wave, not absorbed into the middle of a report, and never left as a row on the ground that it
>   looked small. Size is not one of the test's terms.
> - **If NO — it is ROWED AND LEFT: no wave, no dispatch, no surface.** The row is written, and the
>   row is the whole of what is owed.
>
> **★ THE EXCEPTION, STATED PLAINLY: AN ESTABLISHMENT OBLIGATION (#19) ALWAYS GATES, AND IS THEREFORE
> ALWAYS SURFACED, WHATEVER ITS SUBJECT** — including one whose subject is this project's own
> apparatus. R3 does not weaken that clause and does not touch it. The reason is the one
> `CLAUDE.md`'s non-gating declaration already gives in the same words: backgrounding an
> establishment obligation is how it never happens, and #19 exists because a thing merely unfalsified
> is not established.
>
> **What this ADDS to D-438, which it does not amend.** D-438 declares that a row whose subject is
> this project's own tracking and documentation apparatus **gates nothing**. What D-438 does not say
> is what such a row is then OWED. R3 answers on both sides — the duty to surface on the one, and,
> the operative half, **the prohibition on spending a wave on the other.** Without it, "gates
> nothing" had come to mean "still gets a wave, just not a blocking one", which is the same work at a
> lower priority rather than less work.
>
> *Why, in the user's own ground for the ruling:* **the apparatus is now large enough to generate its
> own defect stream indefinitely, and treating each defect as owed is what produced a six-wave
> backlog** — the state `OPEN_ITEMS.md` **OI-337** records — **while the findings that bear on the
> objective came from reads and probes, not from apparatus repair.** That ground is the user's and is
> recorded as the user's; this section derives no measurement of its own for it, and a later session
> must not cite it as one. What it does have beside it is the record each wave left: the read waves'
> yields are in their own artifacts (`tools/audit/decisions/reads<n>_yield.json`), and no value from
> any of them is restated here (**D-431**).
>
> **How it composes with the finish line.** R2 of the same ruling makes the derived finish line the
> SCOPE — `tools/audit/phase1_finish_line.json`, regenerated by
> `tools/audit/gen_phase1_finish_line.py`. R3 governs what happens to a finding made while an item on
> that list is worked: it decides whether the finding is surfaced or rowed, and it never adds the
> finding to the list. **Adding an item to the finish line is a user ruling**, which is what keeps a
> scope from growing by the same mechanism this rule exists to stop.
>
> **What it is NOT.** It is not permission to leave an apparatus defect undocumented — the row is
> mandatory, and the open-items register's rule (c) still requires the row and its detail file in the
> commit that records the discovery. It is not a claim that apparatus defects are harmless. And it
> does not decide what PHASE 1 OWES: D-231's clause and D-639 decide that, and D-639 says in terms
> that what a stage waits on and what phase 1 owes are different tests with different subjects.

**In plain words.** Every finding a session makes is sorted by one test, the same one that decides whether an open row makes a stage wait: does its subject bear on the analysis, on the analysis's inputs, or on a measurement tool something depends on? If it does, the finding goes to the user for a decision no matter how small it is. If it does not, a row is written and that is the end of it — no wave of work is spent on it, no dispatch is written for it, and it is not put in front of the user. The one thing this never applies to is an obligation to establish that something works: that always makes a stage wait and always goes to the user, whatever its subject.

**Why.** The ground is the user's and is recorded as the user's rather than derived here: the apparatus is now large enough to generate its own defect stream indefinitely, and treating each defect as owed is what produced a six-wave backlog — the state OPEN_ITEMS.md OI-337 records — while the findings that bear on the objective came from reads and probes, not from apparatus repair. The rule ADDS to D-438 rather than amending it: D-438 says an apparatus row gates nothing but does not say what such a row is then owed, so 'gates nothing' had come to mean 'still gets a wave, just not a blocking one'. The operative half is therefore the prohibition on spending a wave, not the duty to surface. The #19 exception is stated in the ruling and is untouched, for the reason CLAUDE.md's non-gating declaration already gives: backgrounding an establishment obligation is how it never happens.

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `cowork_audit_protocol.md:346-393`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_commit_and_finish_line.md` §0a as R3 — 'A finding whose subject bears on the analysis, its inputs, or an instrument a measurement depends on — D-438's own test — is SURFACED to the user for decision, whatever its size. A finding that does not is rowed and left: no wave, no dispatch, no surface.' Homed in `cowork_audit_protocol.md`'s dispatch-protocol section beside D-431, D-434, D-436 and D-640, as the dispatch's Task 3 directs; `nonspec_kind` is `process` because its subject is how the work is sorted and reported, not the system. It composes with ruling R2 of the same act, the derived finish line at `tools/audit/phase1_finish_line.json`, which R3 never adds to.

### D-642 — Criterion C1 reaches every decision whose content is LIVE — a superseded entry's obligation moves to its successor, and is discharged only where that successor is homed

> ### Criterion C1 reaches every decision whose content is LIVE — a superseded entry's obligation moves to its successor
>
> **Ruled by the user, 2026-08-04** (dispatch `cc_instruction_c1_ruling_and_item1c.md`, §0a R1).
> **Criterion C1 — D-231's phase-1 obligation that every recorded decision is written into its owning
> specification — reaches every decision whose content is LIVE.** A superseded decision's live content
> lives in its **successor**; C1 is satisfied for that content **when the successor is homed**, and the
> superseded entry itself is recorded in the register, which D-231 makes the status ledger for
> supersession. **Where the successor is NOT homed, C1 is defeated and the owed act is homing the
> SUCCESSOR — not the superseded entry.**
>
> **The basis, at D-231's own clause.** The clause assigns two things to two places in one sentence:
> *"the decisions register remains the status ledger (supersession, shelving, the same-commit rule),
> never the conformance reference"*. Supersession and shelving are named there as two distinct things
> the register is the ledger OF, and conformance is assigned to the specifications — so a superseded
> decision is not something conformance is measured against. The clause is quoted **entire**, derived
> at HEAD, at `tools/audit/phase1_completion_inventory.json` → `the_requirement.phase_1_verbatim`,
> which is what the rule immediately below requires of a citation like this one.
>
> **★ THE BASIS PREVIOUSLY CLAIMED IS WITHDRAWN, AND THE WITHDRAWAL IS PART OF THE RULING.** The
> preceding dispatch (`cc_instruction_finish_line_item1b.md`) presented this ruling as an APPLICATION
> of `OPEN_ITEMS.md` OI-272's per-kind home scheme to the superseded kind, and declared that reading as
> an assumption with an instruction to STOP rather than stretch the scheme. The check came back
> negative and **the reading is withdrawn**: the scheme partitions by what a decision IS rather than by
> what its STATUS is, and applied at its own text it routes the affected entries the OPPOSITE way. The
> four grounds that refuted it live at `open_items/OI-340.md` and are not restated here (#6) — a wrong
> basis retracted is evidence (#12), and the row that produced the refutation is where that evidence
> belongs.
>
> **Where it is applied, and what it does not authorize.** The ruling is recorded against criterion C1
> itself — `tools/audit/phase1_completion_inventory.json` → `the_requirement.criteria` → C1 — and
> applied per entry over finish-line item 1's no-home class at
> `tools/audit/decisions/r1_superseded_reach.json`; no verdict or count is restated here (**D-431**).
> It authorizes no fix to the analysis, no design, no inference change, and no re-classification of any
> entry's home class. It decides which entries criterion C1 reaches, and nothing else.

**In plain words.** Phase 1's requirement that every recorded decision be written into the specification that owns it applies to decisions whose content is still in force. Where a decision has been superseded, the thing still in force is its successor, so the requirement is met once that successor is written into its own specification; the superseded entry stays in the register, which is what D-231 makes the register for. If the successor has NOT been written in, the requirement is not met — and what is owed is writing in the successor, not the superseded entry.

**Why.** D-231's phase-1 clause assigns two things to two places in one sentence: 'the decisions register remains the status ledger (supersession, shelving, the same-commit rule), never the conformance reference'. Supersession and shelving are named there as two distinct things the register is the ledger OF, and conformance is assigned to the specifications — so a superseded decision is not something conformance is measured against. The basis previously claimed for the same ruling, that it applied OI-272's per-kind home scheme to the superseded kind, is WITHDRAWN in the ruling that replaces it: the scheme partitions by what a decision IS rather than by its STATUS, and at its own text routes the affected entries the opposite way. The four grounds are preserved at `open_items/OI-340.md` (#12) and are not restated at the home (#6).

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `cowork_audit_protocol.md:395-428`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_c1_ruling_and_item1c.md` §0a as R1, which carries its own withdrawal of the basis previously claimed for it. Homed in `cowork_audit_protocol.md`'s dispatch-protocol section beside D-431, D-434, D-436, D-640 and D-641; `nonspec_kind` is `process` because its subject is how the record's own completion criterion is applied, not the system. It is RECORDED against criterion C1 itself, at `tools/audit/phase1_completion_inventory.json` → `the_requirement.criteria` → C1, where the ruling is quoted in full from this home rather than restated (#6), and APPLIED per entry at `tools/audit/decisions/r1_superseded_reach.json`. The application's own assumption check came back REFUTED IN PART and the artifact records what it found; no verdict or count is carried here (D-431). Cross-ref D-231 (the clause), D-639 (the sibling ruling bounding the same clause's other half), `OPEN_ITEMS.md` OI-340 (the row that refuted the withdrawn basis).

### D-643 — A claim that invokes a ruling as an application of it quotes that ruling in full, never the branch of it that supports the claim

> ### A claim that invokes a ruling AS AN APPLICATION quotes that ruling in full, not the branch that supports the claim
>
> **Ruled by the user, 2026-08-04** (dispatch `cc_instruction_c1_ruling_and_item1c.md`, §0a R2). **A
> claim that invokes a ruling as an application of it must QUOTE THAT RULING IN FULL, not the branch of
> it that supports the claim.**
>
> *Why, at the instance that produced the ruling:* the withdrawn reading above cited OI-272's class
> about shelvings, falsifications and dead ends — and **never put class 1 on the page.** Class 1 is the
> branch that decided the case the other way: the entries at issue are, by kind, standing constraints,
> so class 1 claims them, and class 1 prescribes homing them into the owning specification — the very
> act the invoking ruling exists to forbid. Quoting the helpful branch is not a weaker citation of a
> ruling; it is a citation of a different ruling, and the reader cannot see that it is one. *(The
> scheme itself is quoted in full — all four of its classes — at `open_items/OI-340.md`, so this
> paragraph's account of it is checkable at a primary source rather than taken from here, which is what
> the rule it states would require of it.)*
>
> **How it composes with D-431, which it does not amend.** D-431 requires a premise to be cited to the
> primary source it can be checked at. This rule governs what the citation must then CARRY: the whole
> of the ruling, including the parts that cut against the claim being made. **A citation that is
> correctly sourced and selectively quoted satisfies D-431 and fails this one** — which is why it needs
> stating separately rather than being read into D-431.
>
> **Both sides are bound**, the writing side's dispatches and the executing side's reports alike, on
> the same ground D-431 gives: a dispatch's premise becomes the next session's starting assumption.

**In plain words.** When a dispatch or a report says that some rule follows from an existing ruling, it must quote the whole of that ruling — including the parts that argue against the point being made — and not only the part that helps. Quoting the helpful part is not a shorter citation of the ruling; it is a citation of a different ruling, and a reader cannot tell that it is one.

**Why.** Measured at the instance that produced it: a dispatch invoked OI-272's per-kind home scheme as the basis for the ruling recorded at D-642, quoted the class about shelvings, falsifications and dead ends, and never put class 1 on the page — and class 1 is the branch that decided the case the other way, claiming the entries at issue as standing constraints and prescribing the very act the invoking ruling exists to forbid. It ADDS to D-431 rather than amending it: D-431 governs where a premise is cited FROM, this governs what the citation must then carry, so a citation that is correctly sourced and selectively quoted satisfies D-431 and fails this rule.

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `cowork_audit_protocol.md:430-453`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_c1_ruling_and_item1c.md` §0a as R2 — 'A claim that invokes a ruling as an application must quote that ruling in full, not the branch that supports the claim' — with its measured instance stated in the same act. Homed in `cowork_audit_protocol.md`'s dispatch-protocol section as the dispatch's Task 1.3 directs, beside D-431, D-434, D-436, D-640 and D-641; `nonspec_kind` is `process` because its subject is how a dispatch and a report cite, not the system. Binds both sides, on D-431's own ground. Cross-ref D-431 (the figures-and-premises rule it composes with), D-642 (the ruling whose withdrawn basis is its measured instance).

### D-644 — Where a superseded decision's content is a REMOVAL, the owning specification states the current behaviour and records the removal as a tried-and-closed line

> ### Where a superseded decision's content is a REMOVAL, the specification states the current behaviour and records the removal as a tried-and-closed line
>
> **Ruled by the user, 2026-08-04** (dispatch `cc_instruction_guard_fix_and_item1d.md`, §0a R2).
> **Where a superseded decision's content is a REMOVAL, the owning specification STATES THE CURRENT
> BEHAVIOUR and RECORDS THE REMOVAL AS A TRIED-AND-CLOSED LINE; the register holds the status.**
>
> **This is PRECEDENT, not a new rule.** It is what was already done at `ARCHITECTURE.md` §5.2 for the
> declared-mode piece-start shortcut (`OPEN_ITEMS.md` OI-315, register entry **D-058**), and the ruling
> names that act as its own source. The precedent is quoted **in full**, located by its own anchors and
> re-read from `ARCHITECTURE.md` on every run, at `tools/audit/phase1_completion_inventory.json` →
> `the_requirement.criteria` → C1 → the removal block; it is deliberately not restated here (#6), and a
> rewording of it STOPS the derivation rather than leaving a stale account of it standing.
>
> **What the precedent shows, and why it answers a question D-642 leaves open.** D-642 moves a
> superseded entry's obligation to its **successor**. A removal has no successor: nothing later states
> the rule, because the rule is that the mechanism is gone. Read without this ruling, such an entry
> falls through — the register records it superseded, no specification carries it, and criterion C1 has
> no closing act to name. The precedent supplies one, and it is two acts rather than one: the
> specification is made TRUE about HEAD (there the specification had gone on asserting the removed
> mechanism in the present tense, which is exactly D-231's doc-sync half), and the removal is recorded
> where a later reader will meet it before retrying it. **Neither half alone is sufficient** — stating
> the current behaviour without the tried-and-closed line loses the information that the alternative
> was tried (#12), and recording the closed line without correcting the text leaves the specification
> misdescribing the code.
>
> **What it does not authorize.** No fix to the analysis, no design, no inference change, and no
> re-classification of any entry's home class. It says what the owning specification owes for one shape
> of entry, and nothing else.

**In plain words.** Some superseded decisions were not replaced by a later decision — what happened is that a mechanism was taken out. For those, the specification that owns the subject says what the code does now, and adds a short line recording that the removed mechanism was tried and closed so nobody retries it. The register goes on holding the status. Both halves are required: the current-behaviour statement alone would lose the fact that the alternative was tried, and the tried-and-closed line alone would leave the specification describing code that no longer exists.

**Why.** It is precedent rather than a new rule: the act it prescribes was already performed at `ARCHITECTURE.md` §5.2 for the declared-mode piece-start shortcut (D-058, `OPEN_ITEMS.md` OI-315), where the specification had gone on asserting the removed short-circuit in the present tense and was corrected to state the note-based opening, with a tried-and-closed pointer beside it. It answers a shape D-642 leaves open: D-642 moves a superseded entry's obligation to its successor, and a removal has no successor, so without this the entry has no closing act criterion C1 could name. The precedent is quoted in full from `ARCHITECTURE.md` by anchor, on every run, at `tools/audit/phase1_completion_inventory.json` (D-643, #17f).

**Status.** LIVE · decided 2026-08-04 · ratified by user

**Home.** `cowork_audit_protocol.md:455-482`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_guard_fix_and_item1d.md` §0a as R2, which states in the same act that it is precedent and names the precedent's location. Homed in `cowork_audit_protocol.md`'s dispatch-protocol section beside D-431, D-434, D-436, D-640, D-641, D-642 and D-643; `nonspec_kind` is `process` because its subject is what the record's own completion criterion obliges for one shape of entry, not the system. RECORDED against criterion C1 itself at `tools/audit/phase1_completion_inventory.json` → `the_requirement.criteria` → C1, beside D-642's block, where the PRECEDENT is located by anchor in `ARCHITECTURE.md` and quoted in full on every run rather than paraphrased (D-643). Cross-ref D-642 (the ruling whose open shape this closes), D-058 (the precedent's own entry), D-231 (the clause both bound), `OPEN_ITEMS.md` OI-315 (the row the precedent was performed under).

