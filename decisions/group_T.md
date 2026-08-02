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

**Why.** Stated constraint, CLAUDE.md:867-868: the check is of the work actually on disk, not of the intention - read the difference, not the memory of writing it. Which is the same reasoning as the never-work-from-memory rule, applied to one's own output.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:953`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:859-868, user-directed 2026-07-11. Binds Claude Code and Cowork sessions alike.

### D-197 — The distribution constraint - the import-fix patch is fork-local and never goes upstream

> **★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the
> MuseScore community.** This patch (`cfc7eb5e39`) is fine to have in the **central repo = the user's
> fork** (`origin` = `slimvince/MuseScore`) and may be pushed there, but it must **NEVER** be pushed or
> merged to `upstream` (`musescore/MuseScore`) or otherwise contributed to the MuseScore community.
> `upstream` push is disabled in this repo; keep it so. Any future push/PR/merge that would carry
> `cfc7eb5e39` (or its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed.
> (The #9444 reference above is the upstream *bug report*; it does NOT authorize contributing THIS patch.)

**In plain words.** The MusicXML mode-import fix may live in the user's own fork of MuseScore and be pushed there. It must never be pushed, merged or otherwise contributed to the MuseScore project. Any action that would carry it toward the upstream repository stops work and is reported.

**Why.** Stated constraint, CLAUDE.md:734: the upstream issue number cited beside the patch is the upstream BUG REPORT, and referencing it does not authorize contributing this patch. Upstream pushing is disabled in the repository and is to be kept so (:683-684).

**Status.** LIVE · decided 2026-06-15 · ratified by user

**Home.** `CLAUDE.md:728`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:728-734, user-directed 2026-06-15. ★ READ WITH the general contribution intent at ARCHITECTURE.md:380-382 - two recorded positions, a general intent to contribute and a named one-patch exception; the record does not state how the general intent applies to the rest of the tree.

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

**Why.** Stated constraint, CLAUDE.md:683-690: the removed lines set the minimum window size to the full monitor work area, which is what blocked snapping; the maximised-position constraints are correct and are kept. Upstream issue musescore/MuseScore#25823, introduced by upstream commit 4ad218709 (:643-644).

**Status.** LIVE · decided 2026-05-14 · ratified by user

**Home.** `CLAUDE.md:680`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:678-694, applied 2026-05-14. Unrelated to the composing module; recorded so a dependency update does not silently overwrite it.

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

**Why.** Measurement, CLAUDE.md:717-720: the change is verified isolated to empty-signature scores - exactly 79 zero-signature analyses changed and no non-empty-signature piece moved - the regression gate is byte-identical on all three presets, and the round-trip of a zero-signature minor piece now preserves its mode. The underlying defect is upstream-unchanged code whose own comment flags the check as known-incomplete (CLAUDE.md:710-711, :673-674).

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Home.** `CLAUDE.md:701`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:696-726, applied 2026-06-14, commit cfc7eb5e39. ★ Carries the distribution constraint above: fork-local only, never upstream.

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

**Home.** `CLAUDE.md:908-920`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:154-162`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:166-171`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:144-150`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:922-940`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:942-949`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1792-1796, under the standing-rule heading 'INVESTIGATE BY DEFAULT - NEVER ASK investigate vs proceed (user mandate 2026-06-14)' at cowork_handoff.md:1790 - a session handoff block. Homed in the CLAUDE.md Conventions section, beside principle #5, which it operationalizes. ★ RATIFIED (user, 2026-08-02, the residual-pass queue).

