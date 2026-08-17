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

**Home.** `CLAUDE.md:1796`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1367`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1319`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1340`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:715-745, applied 2026-06-14, commit cfc7eb5e39. ★ Carries the distribution constraint above: fork-local only, never upstream.

### D-208 — A withheld finding never enters a mandatory session-start read

> **A WITHHELD FINDING NEVER ENTERS A MANDATORY SESSION-START READ (user-ratified 2026-07-28).**
> When a pass is run blind — a finding deliberately kept from the auditor so that whether they
> rediscover it measures the audit's power — that finding must not appear in any document the

**In plain words.** When a review is run blind - deliberately keeping a finding from the reader so that whether they rediscover it measures the review's power - that finding must not appear in any document the reader is required to open at the start. The status file carries a pointer; the content lives in a separate artifact opened only afterwards.

**Why.** Measurement, OPEN_ITEMS.md:170: the rule was written because the blinding was defeated at the source - the mandatory status-file read carried the full text of all three sealed findings, and the dispatch delivered them inline as well. The consequence recorded there: the reconciliation could no longer claim knowledge-free discovery, only that the artifacts point at each mechanism on their merits.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `cowork_audit_protocol.md:93-95`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1 specification-completion pass): formerly recorded only at OPEN_ITEMS.md:170 (OI-222) with open_items/OI-222.md, and restated in a session handoff block. Homed under P5 of the audit protocol, which is the blinding rule it sharpens. Generalizes the earlier OI-89 instance of the same shape

### D-209 — Code that is about to be deleted gets no audit - only the no-information-loss check at deletion

> Applied BEFORE P1's enumeration. The module is partitioned against the retirement map: **code that
> retires gets no audit at all** — the only thing owed to it is the #12 no-information-loss check at
> the moment of deletion (does anything it knew go unrecorded?). The surviving stack is then audited

**In plain words.** Before auditing the system exhaustively, the code is split into what survives and what is scheduled for removal. What is scheduled for removal is not audited at all. The only thing owed to it is a check, at the moment it is deleted, that nothing it knew is lost.

**Why.** Stated constraint, OPEN_ITEMS.md:60: the alternative form - audit whatever you happen to touch - was rejected by the user as risky, because touching one per cent would audit one per cent while new work built on the unaudited rest, which is itself a violation of the no-unverified-premises principle across the whole architecture. ★ The rule's own boundary is recorded too: at cowork_handoff.md:368-369 the user ruled it does NOT shield the joint module, which is production on both surfaces and is not retiring.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `cowork_audit_protocol.md:140-142`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1728-1740`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:203-211`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1606-1616, stated as standing rules under the handoff's standing-rules block - a session handoff block. Homed in the new dispatch-protocol section of the audit protocol. ★ RATIFIED (user, 2026-08-02, the residual-pass queue). ★ THE DECIDING ACT KEPT ON THE RECOVERY PASS'S ORIGINAL EVIDENCE (user's ruling of 2026-08-17, cowork_rulings_2026_08_17_residue_sitting.md §4 (Ruling 4)): the tested document-ratification shape is not present for this entry, so the recovery pass's evidence stands exactly as it stood. A passage at `open_items/OI-266.md` line 15, carrying a user-act marker and matching the entry's own identity, reads — "| entry | the rule | ratifier and date in the record | |---|---|---| | D-249 | The whole decision surface is delivered as user-visible text before any choice question | user mandate 2026-07-05 | | D-250 | Dispatches are written only when they are next; a parked instruction is revalidated first | not stated | | D-251 | A running dispatch is never interrupted or steered mid-flight | user, 2026-07-05 | | D-252 | One side writes the instruction files and the other executes them, never the reverse | not stated | | D-253 | Working-tree files are read with the file tools; shell access is limited to git object queries by explicit hash | user mandate 2026-06-21 | | D-254 | Investigate by default; never ask the user whether to investigate or proceed | user mandate 2026-06-14 |" The act is quoted from `tools/audit/deciding_act_recovery.json`; no other field of this entry is touched.

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

**Home.** `cowork_audit_protocol.md:215-220`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:193-199`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Re-homed 2026-08-02 (the phase-1d enumeration wave; OPEN_ITEMS OI-266 closes on this move): formerly recorded only at cowork_handoff.md:1630-1638, under 'STANDING RULE FOR COWORK (read every session)' at cowork_handoff.md:1628 - a session handoff block. Homed in the new dispatch-protocol section of the audit protocol, beside P5's withheld-finding rule and P8's pass ordering, which are already rules about how a dispatch is written and sequenced; that section's lead-in states that these three rules govern every dispatch and not only the audits above it. ★ RATIFIED (user, 2026-08-02, the residual-pass queue). ★ THE DECIDING ACT KEPT ON THE RECOVERY PASS'S ORIGINAL EVIDENCE (user's ruling of 2026-08-17, cowork_rulings_2026_08_17_residue_sitting.md §4 (Ruling 4)): the tested document-ratification shape is not present for this entry, so the recovery pass's evidence stands exactly as it stood. A passage at `open_items/OI-266.md` line 15, carrying a user-act marker and matching the entry's own identity, reads — "| entry | the rule | ratifier and date in the record | |---|---|---| | D-249 | The whole decision surface is delivered as user-visible text before any choice question | user mandate 2026-07-05 | | D-250 | Dispatches are written only when they are next; a parked instruction is revalidated first | not stated | | D-251 | A running dispatch is never interrupted or steered mid-flight | user, 2026-07-05 | | D-252 | One side writes the instruction files and the other executes them, never the reverse | not stated | | D-253 | Working-tree files are read with the file tools; shell access is limited to git object queries by explicit hash | user mandate 2026-06-21 | | D-254 | Investigate by default; never ask the user whether to investigate or proceed | user mandate 2026-06-14 |" The act is quoted from `tools/audit/deciding_act_recovery.json`; no other field of this entry is touched.

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

**Home.** `CLAUDE.md:1742-1760`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `CLAUDE.md:1785-1792`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home section.** **“The stages”** — `## The stages (in principle order)` (heading at line 19). A delegation at CLAUDE.md:294 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** cowork_engage_arc_plan.md:64 states the gate as 'ratified 2026-07-10 with #17-#19', with its evidence document cited; the conditions at :64-92 and the amendment note at :128-130. The last condition is registered separately as D-209, the retiring-code audit rule, at its cowork_audit_protocol.md home. Found by the phase-1d enumeration wave, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1d queue).

### D-298 — The layer-by-layer audit - each layer is audited once its pieces are in place

> ## P10 — Verification is organised BY LAYER: a layer is audited once its pieces are in place (user-recorded standing method, 2026-06-14)
>
> Auditing is not something done to each change in isolation. When a layer's pieces are built, that layer is

**In plain words.** Verification is organised by layer: when a layer's pieces are built, that layer is audited as a whole before the work moves on, rather than checking each change in isolation.

**Why.** A user-recorded standing method, adopted as the verification model for the second half of the programme. It is the method the later per-layer certification plan realised.

**Status.** LIVE · decided 2026-06-14 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_audit_protocol.md:154-156`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** Recorded in `cowork_handoff_archive.md` (the 2026-06-14 option-C block) as a new standing method, pointing at the handoff's standing block and the roadmap. Realised as the dependency-ordered per-layer certification plan (`OPEN_ITEMS.md` OI-84, complete 2026-07-12) and as the audit protocol's pass ordering. Found by the phase-1e second-partition archive read, 2026-08-02. ★ RATIFIED (user, 2026-08-02, the phase-1e archive queue). ★ HOMED 2026-08-02 (CC, phase 1j, executing the user's per-kind ruling on [[OI-272]] — process rules go to `CLAUDE.md` or the audit protocol): written as P10 of `cowork_audit_protocol.md`, beside P8 and P9, which are the method this rule says WHEN to apply. Former home preserved (#12): `cowork_handoff_archive.md:3771`, the 2026-06-14 option-C block.

### D-314 — A correction rule kept for structural reasons must keep producing evidence that it still fires

> **O-10 (lesson from the user's methodology challenge, 2026-07-05): RETAINED structural rules carry
> ongoing LIVENESS evidence.**

**In plain words.** When a rule is kept because it encodes something structural rather than because a fitted number could replace it, its firing counts are re-measured at every adoption event. A kept rule that has quietly stopped firing then shows up at the next checkpoint instead of being discovered much later.

**Why.** The failure it answers is on the record: two rules' founding cases were silently absorbed upstream, leaving the rules dead and undetected for weeks, because nothing measured rule liveness (`cowork_stage5_fitter_design.md:1471-1478`).

**Status.** LIVE · decided 2026-07-05 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_stage5_fitter_design.md:1493`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **“§15 Open items & ratification asks”** — `## §15 Open items & ratification asks` (heading at line 919). A delegation at ARCHITECTURE.md:301 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**.

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

**Home.** `cowork_audit_protocol.md:224`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the fifth ruling set of that date), homed at phase 1n in `cowork_audit_protocol.md`'s dispatch-protocol section beside **D-250**, **D-251** and **D-252**, which is the established home for rules about how a dispatch is written. It is `CLAUDE.md` principle **#17(f)** — no hand-transcribed measurement numbers — applied where it was being ignored: #17(f) was written for DOCUMENTS and was honored there, and dispatches and session reports were treated as outside it on the unstated ground that they are working correspondence rather than record. They are not: a dispatch's premise becomes the next session's starting assumption and a report's figure becomes the next report's baseline. **The register-side instance of the same shape is `OPEN_ITEMS.md` OI-283** — a hand-typed coverage claim inside a generated file — whose remedy is now one instance of this general rule rather than a one-off; that row carries a dated note saying so and does NOT close, its own remedy still being owed. NOT RATIFIED as an ENTRY — it goes to the user in the phase-1n ratification queue.

### D-434 — The writing side runs the standing self-check before a dispatch is released, and records its output

> **before a dispatch or a decision surface is released, the writing side
> runs the standing self-check over it and RECORDS the output.**

**In plain words.** The standing self-check — re-read what is actually on disk and check it against the principles, the conventions and the known defect types before reporting — applies to the side that WRITES the working instructions, not only to the side that executes them. It runs before the instruction is handed over, and its output is written down.

**Why.** Measured on this protocol's own output: eight instances in which a dispatch or a report carried a wrong premise or an underived figure that the standing self-check would have caught, each cited at the rule's home to the row or artifact that records it, and every one of them found by the EXECUTING side running the check the writing side had not. `CLAUDE.md`'s self-check already binds both sides in its own words (*"code, scripts, instruments, and document edits alike"*); what was missing was a statement of it where the rules about writing a dispatch live, and a mechanism that makes its absence visible.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `cowork_audit_protocol.md:331`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:364`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-03 (the eighth ruling set of that date, X3), homed at phase 1q in `cowork_audit_protocol.md`'s dispatch-protocol section beside **D-431** and **D-434**, which is the established home for rules about how a dispatch is written and checked. **It WITHDRAWS a test the planning side had stated and this project had been working under** — *a mechanism must retire the prose it replaces, or it is apparatus growth* — and the withdrawal is recorded with its reason rather than left as a silent change of standard. The two mechanisms built under the withdrawn test are KEPT under this one, and their establishment artifacts carry their measured rates: `tools/audit/process_check_establishment.json` and `tools/audit/shell_read_guard_establishment.json`. The guard's third condition holds only while it is ARMED, which is the user's act on the user's machine; until then it is recorded as an expected-failing check rather than as coverage (`OPEN_ITEMS.md` OI-292). **★ AMENDED by the user 2026-08-03 (the eleventh ruling set, AA5) and re-taken at phase 1u: the criterion INFORMS; removal or retention is the user's ruling.** The three conditions and their stated reasons are unchanged — including the false-positive reason, *one that fires on legitimate work gets switched off, which is worse than having none*, which is why that condition exists and which survives the amendment intact. What changed is who decides the consequence. **The FORMER VERBATIM is preserved here (#12), being the text the entry carried before the amendment:** "**Ruled by the user, 2026-08-03.** A mechanism built to enforce one of these rules is kept when **it runs automatically with no human step, it has a measured detection rate against known instances of the failure it is for, and it has a measured false-positive rate at or near zero on legitimate work.** All three are measurable and none is judged. A mechanism that fails any of them is not kept: one needing a human step is a reminder, one with no measured detection rate is unestablished (#19), and one that fires on legitimate work gets switched off, which is worse than having none." **The amendment's first application is on the record in the same wave:** the shell-read guard has two shapes its established corpora do not cover — a common existence-listing command and a path outside the repository — and under the amended rule they are REPORTED and rowed for the false-deny establishment run rather than either added to the denied set unestablished or the guard treated as failing and dropped (`OPEN_ITEMS.md` OI-292, OI-300). NOT RATIFIED as an ENTRY — it goes to the user in the phase-1q ratification queue, with the amendment above added at phase 1u.

### D-437 — Phase 3 waits on the phase-2 items that could find another member of the family being designed for, not on all of phase 2

> **★ QUALIFICATION — PHASE 3 WAITS ON THE PHASE-2 ITEMS THAT COULD FIND ANOTHER MEMBER OF THE
>   FAMILY BEING DESIGNED FOR, NOT ON ALL OF PHASE 2 (user-ruled 2026-08-03).**

**In plain words.** A family design waits only on those phase-2 searches whose search space could contain a fact about the thing that family is about — for the struck-versus-sounding family, about what the decoder or the emission reads or about how candidates are admitted. Where an item's scope does not settle the question it still gates. Narrowing the gate does not open it: no fix, design or inference change is authorized, and the partition is recorded as a falsifiable prediction whose refutation by a non-gating item is a #13 STOP.

**Why.** D-231's phase gate was ratified so that a defect family is KNOWN before it is designed for — the standing one-fix-per-family rule of 2026-07-28 is what it protects. An item that cannot touch what the model reads or how candidates are admitted cannot change what the family is, so making the design wait on it buys no protection and spends time the fix plan is owed. The error in the other direction is bounded by the stated default: an item whose scope does not settle the question gates.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:1645-1663`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03, transmitted in the phase-1o dispatch cc_instruction_phase1o_gate_partition_and_probe_rerun.md §2.1; applied and homed at CLAUDE.md's D-231 entry in the recording commit per D-230. The partition itself is generated at tools/audit/phase3_gate_partition.json. **★ THE PER-ITEM VERDICTS WERE ACCEPTED BY THE USER 2026-08-03 (the eleventh ruling set, AA1) — accepted AS GENERATED, with the accounting of what the ruling's measured effect actually was recorded beside them.** That accounting is a block of the artifact, `what_the_partition_measured`, and no figure of it is restated here (#17f, D-431); its structural counts read fields rather than prose, and the one judgment a text test could not make honestly is carried as quoted sentences for the reader instead of as a number. **In plain words: most items GATE, several of them because their search space has ALREADY produced a member of the family rather than on the doubt default, and the narrowing bites in exactly one place** — the family design need not wait for phase 2's bounded trust statement to be WRITTEN, only for the gating searches to have RUN. **★ THE PLANNING PREDICTION THAT RECOMMENDED THIS RULING IS REFUTED AND IS RECORDED AS SUCH** (#17b applied to a planning claim): Cowork's decision surface said the option *"removes the largest share of the blocking for the smallest loss of rigor"*, and the second half holds while the first does not. **The RULING stands** — it was ruled by the user on its own terms and is not disturbed by its advocate's forecast being wrong; what the record must not do is let a later session inherit the expectation instead of the result. Full statement at the artifact's `what_the_partition_measured.the_refuted_planning_prediction`. **A second premise of the same wave was checked at the document and came back different too**: the claim about which of the four channels the phase-2 clause omits actually matter is not what the inventory supports, and the inventory's own statement that history mining is "run to completion" is not true at HEAD — both at `assumption_A1_of_the_phase1u_dispatch`. No verdict moved on either finding.

### D-438 — Open-items register rows whose subject is this project's own tracking and documentation apparatus gate nothing — but an establishment obligation always gates

> **★ QUALIFICATION OF RULE (b) — THE APPARATUS ROWS ARE DECLARED NON-GATING (user-ruled
> 2026-08-03).**

**In plain words.** An open row of the open-items register whose subject is this project's own tracking or documentation apparatus stays open and stays owed but blocks no stage; it is worked in leftover capacity. The test is whether the row's subject bears on the analysis, its inputs, or an instrument a measurement depends on — if yes it gates — and inside the documentation rows the line is what is owed: a pointer, anchor, label, banner, filing decision or section boundary is apparatus, while correcting a statement about the analysis or completing a specification gates. A row that is not apparatus, or whose subject its own text does not settle, gates. An establishment obligation (#19) always gates, whatever its subject.

**Why.** The open-items register is this project's own record-keeping, and a rule that lets its housekeeping block the work it exists to track inverts what it was created for; the cost of the error in the other direction is bounded by the stated default (anything not settled gates). The establishment exemption is not discretionary because backgrounding an establishment obligation is how it never happens, and #19 exists precisely because a thing merely unfalsified is not established.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:331-352`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03, transmitted in the phase-1o dispatch cc_instruction_phase1o_gate_partition_and_probe_rerun.md §3; applied and homed at CLAUDE.md's open-items register section, qualifying rule (b), in the recording commit per D-230. The derived set is generated at tools/audit/nongating_apparatus_rows.json.

### D-439 — The perspective inventory's §4 is the one home for the enumerated discovery channels, and CLAUDE.md's phase-2 clause points at it instead of listing its own subjects

> **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03;
>   D-439).**

**In plain words.** Section 4 of cowork_oi200_perspective_inventory.md is the ratified one home for the discovery channels that CLAUDE.md's phase-2 clause relies on; the clause now points at that section and lists no subjects of its own (#6). Ratified together with the scope ruling written into that section — which of the four channels the clause never named it reaches: channel 9 (history mining) is IN, being a distinct search the clause names nowhere; channels 4 and 8 are ALREADY REACHED, channel 4 because its own text makes it an obligation carried by the other probes rather than a search of its own and channel 8 because its own text makes it the audit passes and blind second pass the clause names immediately beforehand; channel 10 is NOT a discovery channel on its own account, its catalog-feeding role noted rather than dropped. The ratification does NOT adopt the inventory's §6 program in whole or in part, does NOT pull OI-200 forward, leaves that document's own §9 request open and untaken, authorizes no probe, fix, design or inference change, and does not complete phase 1.

**Why.** A binding user-directed rule was leaning on an unratified Cowork draft: D-231's phase-2 clause named *"the enumerated discovery channels"* and the only place in the record where those channels are enumerated is a document whose own banner read DRAFT and whose §9 recorded its one requested decision untaken. The ratification closes that, and pointing the clause at the ratified section instead of restating six subjects removes the second, shorter enumeration (#6) — which was also an under-naming, since the clause's six subjects are six of ten channels. The scope ruling was folded in rather than deferred because the four unnamed channels are exactly what a pointer makes ambiguous, and each verdict rests on the channel's own text rather than on a judgment made at the ruling.

**Status.** LIVE · decided 2026-08-03 · ratified by user

**Home.** `CLAUDE.md:1667-1679`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling 2026-08-03 (the twelfth ruling set: option C with option B's correction folded in), transmitted in the phase-1v dispatch cc_instruction_phase1v_channel_ratification.md §1 and §4; the reading surface the ruling was taken from is ratification_surfaces/cowork_perspective_inventory_ratification.md §5. Applied and homed at CLAUDE.md's phase-2 clause and its note, in the recording commit per D-230; the enumeration and the scope ruling themselves live at cowork_oi200_perspective_inventory.md §4, which that clause now delegates to by name. **★ THE CHANNEL-9 CORRECTION WAS MADE FIRST, DELIBERATELY.** The inventory's channel 9 said of history mining *"none new — the adjudication is this channel run to completion"*; that was untrue of both faces of the OI-207 adjudication at HEAD — its residual second pass ran on 2026-08-02, the unresolved cluster residual is live at tools/audit/decisions/disposition_manifest.json → disposition_counts.unresolved, and the owed full document reads are tracked on the OPEN_ITEMS.md OI-207 row. Both were established at those objects before this entry was written. Ruling the channel's scope while its own text said the work was finished would have ratified a contradiction, which is why the user's ruling folds the correction into the ratifying act rather than following it. The former wording is preserved verbatim at the inventory's own dated correction note (#12), as is the former CLAUDE.md note that recorded the gap while it stood. **★ WHAT IT DOES NOT DECIDE, stated because a later reader would otherwise assume more:** the §6 program is NOT adopted in whole or in part; OI-200 is not pulled forward and the inventory's §9 request — adopt, amend or reject that program — stays open and untaken; no probe, fix, design or inference change is authorized; and phase 1 is not complete. **★ WHAT IT RETIRES:** the stated workaround tools/audit/phase3_gate_partition.json carried about its structural source being an unratified draft — preserved verbatim in that artifact's `the_channel_enumeration_source.status_of_this_source.what_this_retires` and NOT deleted (#12). **No verdict of that partition moves**, and none was re-stated on the new authority: the verdicts were recorded as a prediction before the classified items ran, which is what makes them falsifiable. One consequence is reported rather than silently corrected — the partition's per-item `kind` field labels channel 10 a discovery channel, which this ruling supersedes; the field is left standing and the supersession is recorded beside it at that artifact's `the_channel_enumeration_source.the_scope_ruling`, because a registered prediction is not re-touched after the fact.

### D-473 — A theory-grounding pass labels every load-bearing claim FACT / THEORY / CONJECTURE, cross-checks its central sources independently, and carries no equation out of a text it could not fetch

> *Theory-grounding corollary to #1/#2 (2026-07-19; the record states no ratifier):* where published
> research is used to justify a design, **every load-bearing claim is labeled FACT** (stated or
> measured in a paper actually fetched and read), **THEORY** (established published theory), or

**In plain words.** When published research is used to justify a design, each claim is marked as either measured in a paper that was actually read, established theory, or a guess. The main papers are read by more than one pass and the readings compared. If a paper could not be obtained, nothing is copied from it — the gap is stated instead.

**Why.** Stated with the method and derivable from #1: a citation to a paper nobody read is not a fact basis, and an equation reconstructed from a snippet is an assumption wearing a citation. The document applies the rule to itself — its own source register carries a 'still unfetched/unverified (no equation carried)' list.

**Status.** LIVE · decided 2026-07-19 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:268-270`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** The stated method of the term-level theory-grounding audit, in a document whose banner records it as written at the user's direction. Entered by the phase-1 reads WAVE 2 (dispatch `cc_instruction_reads_2.md`) from the full read of the document. ★ RATIFIED (user, 2026-08-04, the READ WAVE 3 ratification queue — the thirty-three READ WAVE 2 entries D-469…D-501 ratified AS DRAFTED, each keeping the status the record states, several of which are 'not stated', and left that way. What the ratification of an ENTRY settles is that the register records the decision correctly; it is not a judgment that the decision is good and it is not a conformance finding. It supplies no date and no ratifier the original record never had, so every 'not stated' fact above stands unchanged (#12). Home and provenance remain bookkeeping. Dispatch cc_instruction_reads_3.md §1.2.) It sharpens principle #17(a) rather than restating it: #17(a) requires the FACT / THEORY / ASSUMPTION labels, and the unfetched-source rule and the independent cross-extraction are this document's additions. ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` the corollary block that follows the guiding principles, as the theory-grounding corollary to #1/#2, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_term_theory_grounding.md:6-11`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `project-convention` entry (the register's own home rule): section "# Term-level theory grounding — the derivation half of the theory-grounding audit", label "the opening block (above the first section heading)", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "`tools/term_inventory/term_inventory.csv` (95 terms, 80 live). **Method:** five parallel deep-research\npasses with primary-source fetch (2026-07-19); every load-bearing claim labeled **FACT** (stated/measured\nin a fetched paper), **THEORY** (established published theory), or **CONJECTURE**, per #1. Verification:\nthe central sources (Raphael-Stoddard, Ni et al., Temperley, Masada & Bunescu) were extracted\nindependently by 2–3 agents each and cross-checked for agreement; unfetchable sources are flagged and no\nequation is carried from an unfetched text. **Nothing here decides anything** — the keep/fix/drop rows are". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

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

**Home.** `cowork_audit_protocol.md:57-64`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:76-83`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:106-114`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:126-136`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `docs/stage4b_design.md:217-218`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4b_design.md`, the Stage-4b design implementing the user's ratified Stage-4 redirect; the staged approach was chosen by the user 2026-06-14. Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY key path** (`keymodeanalyzer` / `keyresolver`), which the joint estimator replaced on both surfaces. Recorded as the document's §7 stop conditions. Unlike D-571 and D-572 this clause is a MEASUREMENT rule, not a scoring term, so it is not legacy-scoped: it binds any future ablation that removes a support to size its contribution.

### D-574 — The pass-bar for a measured change is set AFTER the baseline measurement, so the threshold is data-grounded rather than guessed

> | 6 — mode-absent pass-bar | **Set after 4b-i's floor measurement** (data-grounded). Dossier's ≥70% of the +378 is the starting reference; **user ratifies the number** once the floor is known. |

**In plain words.** How much of a drop would be acceptable is not decided in advance. The measurement runs first, the size of the effect becomes known, and only then is the bar the work must clear set — by the user.

**Why.** Stated with the disposition and defended by what it avoids: a threshold chosen before the effect is known is a guess that the work will then be tuned against. The document names the earlier proposal's number as a starting reference rather than a bar, and reserves the decision to the user.

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/stage4b_design.md:167`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4b_design.md`, the Stage-4b design implementing the user's ratified Stage-4 redirect; the staged approach was chosen by the user 2026-06-14. Read in full by READ WAVE 4, 2026-08-04. **Its subject is the LEGACY key path** (`keymodeanalyzer` / `keyresolver`), which the joint estimator replaced on both surfaces. Recorded as disposition OQ6 of the document's open-question table, and confirmed in its §6 ratification asks. Like **D-573** this is a measurement rule rather than a scoring term and is not legacy-scoped. It stands beside the standing requirement that a fit declares its held-out data and capacity budget BEFORE fitting (#20) — that rule fixes what is declared early, this one fixes what may not be.

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

> - **A layer's measurement is judged on COVERAGE-MATCHED ACCURACY and CORRECT ABSTENTION, never on raw
>   coverage** (2026-06-26; the record states no ratifier). Two things are reported together: how
>   accurate the layer is over the cases it answered, and whether the cases it declined were ones it

**In plain words.** When a stage of the analysis is measured, two things are reported together: how accurate it is over the cases it actually answered, and whether the cases it declined were ones it should have declined. How MANY cases it answered is not the measurement — declining a case that genuinely cannot be decided at that stage is a correct answer, not a gap.

**Why.** Recorded as the lesson of the preceding layer's build, where the decoder was measured materially better than the legacy path WHERE IT COMMITS and about eighty-five per cent of its abstention was established as genuinely function-dependent — a figure that raw coverage would have read as failure. It is also the reason the granularity-robust stop is abstain-aware (**D-212**): an agreement percentage that ignores abstention is reducible by declining more often.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:938-940`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_phase5c_l5_build_plan.md`, the Layer-5 build plan, DRAFT 2026-06-26. Read in full by READ WAVE 5, 2026-08-04. Recorded in the plan's build-discipline block. Its companion in the same block — build the mechanisms right at their defaults and stop, do not chase accuracy — is the proportionality rule **D-480** already carries for the phrase-boundary primitive, stated here for the function layer and not re-entered (#6). The record states no ratifier for the gate criterion. ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` gate block (A), as the second of the three further measurement conventions homed beside the four grading conventions, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_phase5c_l5_build_plan.md:27-29`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `process` entry (the register's own home rule): section "## The build discipline (every step)", label "“The build discipline”", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **The gate criterion (the L4 lesson).** Judge each measurement by **coverage-matched accuracy + correct\n  abstention**, never raw coverage — abstaining correctly on a genuinely function-undecidable slice is a *right*\n  outcome.". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

### D-603 — While the pipeline is being rebuilt, a behaviour-changing increment is graded DIRECTIONALLY and not against a fixed bar — meaningful comparison happens only against the fully reconstructed pipeline

> - **While the pipeline is being rebuilt, a behaviour-changing increment is graded DIRECTIONALLY and
>   not against a fixed bar** (user, 2026-06-22). Both the baseline numbers AND the metric definitions
>   move as the layers around an increment are reconstructed, so a rebuild step is judged on whether it

**In plain words.** While the stages below and above are still being rebuilt, both the numbers and the way they are measured will keep moving. So a rebuild step is judged by whether it moved the specific defects it was meant to move in the right direction, not by whether it beat a number recorded earlier. The comparison that means something is against the finished pipeline.

**Why.** The reason is stated with the decision: the baseline figures AND the metric definitions themselves will move as the rest of the pipeline is reconstructed, so a fixed bar set now would be a bar against a measurement that no longer exists when it is tested. It is the same reasoning `CLAUDE.md` #16 and #24 apply to instrument and sampling error, applied to a measurement whose definition is still in motion.

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:947-949`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `cowork_layer3_keymode_impl_design.md`, the Layer-3 key/mode implementation design. Read in full by READ WAVE 5, 2026-08-04. Marked *user, 2026-06-22* at the head of the design's metric section. Read alongside **D-574** — the pass-bar for a measured change is set AFTER the baseline is measured — which governs how a bar is set once one is set at all; this governs whether a fixed bar is admissible during a rebuild. ★ HOMED 2026-08-07 (CC, the licensed homing wave, executing the user's ruling R2 of 2026-08-07, dispatch `cc_instruction_licensed_homing_and_oi344.md` §0a — the LICENSING class of finish-line item 1's re-home set, homed under the edit-surface licence the user ruled on the same date). Written into `CLAUDE.md` gate block (A), as the third of the three further measurement conventions homed beside the four grading conventions, in that section's own voice and with its defense. The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. FORMER HOME, PRESERVED (#12): `cowork_layer3_keymode_impl_design.md:83-86`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — it is removed because the home-class criteria do not reach a `process` entry (the register's own home rule): section "## §4 — Metric / gates (Increment C — the behavior-changing one)", label "“§4”", verdict EXCLUDE, decided by "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade"; former_class gap, class_before_phase1q gap, class_before_phase1r gap. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**★ METRICS ARE PROVISIONAL — grade DIRECTIONALLY, not against a fixed bar (user, 2026-06-22).** The Increment-B\nbaseline numbers (held-out Baroque 87.3% / Jazz 61.5%) **and the metric definitions** WILL move as the rest of the\npipeline (L4–L6) is reconstructed/refactored. **Meaningful comparison happens only against the fully reconstructed\npipeline**, not increment-by-increment.". Provenance is recorded in this field and NOT in the specification text, on the ruling's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson). What the specification text carries is the rule, its date and its ratifier where the record states one, and its defense.

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

**Home.** `cowork_audit_protocol.md:292-323`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:616-663`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:714-747`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:749-772`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Home.** `cowork_audit_protocol.md:774-801`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-04, transmitted in the dispatch `cc_instruction_guard_fix_and_item1d.md` §0a as R2, which states in the same act that it is precedent and names the precedent's location. Homed in `cowork_audit_protocol.md`'s dispatch-protocol section beside D-431, D-434, D-436, D-640, D-641, D-642 and D-643; `nonspec_kind` is `process` because its subject is what the record's own completion criterion obliges for one shape of entry, not the system. RECORDED against criterion C1 itself at `tools/audit/phase1_completion_inventory.json` → `the_requirement.criteria` → C1, beside D-642's block, where the PRECEDENT is located by anchor in `ARCHITECTURE.md` and quoted in full on every run rather than paraphrased (D-643). Cross-ref D-642 (the ruling whose open shape this closes), D-058 (the precedent's own entry), D-231 (the clause both bound), `OPEN_ITEMS.md` OI-315 (the row the precedent was performed under).

### D-645 — A homing dispatch may edit docs/scoring_model.md, CLAUDE.md and BUILD_AND_TEST.md, and the license is scoped to homing acts alone

> ### A homing dispatch may edit three further files, and the license is scoped to homing acts alone
>
> **Ruled by the user, 2026-08-07** (dispatch `cc_instruction_five_rulings.md`, §0a R1). **The edit
> surface a HOMING dispatch may touch is widened to `docs/scoring_model.md`, `CLAUDE.md` and
> `BUILD_AND_TEST.md`, SCOPED TO HOMING ACTS ONLY** — writing a register entry's decision into its
> owning specification, in that section's own voice, with its defense, and with the entry's former
> home, its former class and its former verbatim preserved (#12). **The license does not extend to any
> other edit of those three files.**
>
> **What the license is a license FOR.** Criterion C1 — D-231's phase-1 obligation that every recorded
> decision is written into its owning specification — names an owning specification per entry, and for
> part of finish-line item 1 that specification is a section of one of these three files. Until this
> ruling a session could identify the owed act and not perform it, because the file lay outside the
> standing authorization, which names `src/composing/`, `notationaccessibility.cpp` and
> `ARCHITECTURE.md` and no other document. The widening removes that obstruction and removes nothing
> else: a homing act writes a decision the register already holds into the section that owns its
> subject, and every other edit of these files remains outside what a dispatch may take.
>
> **The context the ruling was taken on, and the half it deliberately does not reach.** The blocker for
> item 1's re-home class is partitioned at `tools/audit/decisions/item1_rehome_blocker.json`, derived
> per entry from each row's own recorded reason. **Edit-surface licensing is the MINORITY** of that
> class; the majority record an owner the record itself calls not determinate, and a widening moves
> none of them. **That half is untouched by this ruling and returns to the user per entry.** No
> population, identifier or count is restated here (**D-431**) — the artifact carries them.
>
> **What it does not authorize.** No fix to the analysis, no design, no inference change, no
> re-classification of any entry's home class, and no edit of these three files for any purpose other
> than a homing act. **The dispatch that records the license performs no homing under it**: the ruling
> and its first exercise are deliberately separate acts, so that what the license permits is on the
> record before anything is written under it.

**In plain words.** A dispatch whose job is to write a recorded decision into the specification that owns it may now edit three documents it previously could not — the scoring model, the standing-instructions file and the build-and-test guide. The permission covers that one kind of act and nothing else: the decision is written in the receiving section's own voice with the reason it was made, and the register keeps the entry's former home, class and wording. Any other edit of those three files is still outside what a dispatch may do, and the dispatch that recorded the permission deliberately used none of it.

**Why.** Criterion C1 names an owning specification per entry, and for part of finish-line item 1 that specification is a section of one of these three files — so the owed act could be identified and not performed, the standing autonomous-operation authorization naming only `src/composing/`, `notationaccessibility.cpp` and `ARCHITECTURE.md`. The ruling was taken on the measured blocker partition at `tools/audit/decisions/item1_rehome_blocker.json`, which is derived per entry from each row's own recorded reason and shows edit-surface licensing to be the MINORITY of the open re-home class; the majority record an owner the record itself calls not determinate, which a widening does not move and which returns to the user per entry. No count is carried here (D-431).

**Status.** LIVE · decided 2026-08-07 · ratified by user

**Home.** `cowork_audit_protocol.md:935-964`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-07, transmitted in the dispatch `cc_instruction_five_rulings.md` §0a as R1 and taken on Cowork's decision surface of the same day, after the surface with its alternatives was delivered as user-visible text. Homed in `cowork_audit_protocol.md`'s dispatch-protocol section beside D-431, D-434, D-436, D-640, D-641, D-642, D-643 and D-644; `nonspec_kind` is `process` because its subject is what a dispatch may edit, not the system. The dispatch that recorded it performed NO homing under it, by its own Task 1.3. Cross-ref D-231 (the phase-1 clause criterion C1 states), D-642 (which entries C1 reaches), `OPEN_ITEMS.md` OI-342 (the row whose owner column the blocker partition was cut against), `tools/audit/decisions/item1_rehome_blocker.json` (the partition the ruling was taken on).

### D-646 — A generated record that must outlive its own writer is frozen at an established snapshot, and the freeze is enforced by a hash STOP

> ### A generated record that must outlive its own writer is FROZEN at an established snapshot, and the freeze is a hash STOP
>
> **Ruled by the user, 2026-08-08** (`cowork_rulings_2026_08_08_pre_away.md`, Ruling 1). **Where a
> generated artifact RECORDS WHAT A PASS FOUND and the tool that writes it must go on running, the
> artifact is declared HISTORICAL and frozen at an ESTABLISHED SNAPSHOT; the writer then runs at HEAD;
> and the freeze is enforced by a STOP on the snapshot's own bytes.** The writing tool carries one
> frozen CLASS EPOCH per completed pass on the same construction, so no value an earlier pass recorded
> is overwritten by a later one (#12).

**In plain words.** Some generated files are not a view of the tree as it is now — they are the record of what one pass found. When the tool that writes such a file has to keep running, the file is declared historical and frozen at a snapshot whose bytes are hashed, the tool goes on running against the current tree, and any attempt to regenerate over the frozen record stops the run instead of quietly succeeding.

**Why.** Measured at the failure of the alternative. The remedy previously in use was to HOLD the writing tool for as long as the record had to survive; that hold stopped a live derivation for a month, and it did not even work — the held run was performed by more than one later wave and the record survived only because a snapshot had been taken (the divergence is recorded at `tools/audit/decisions/phase1q_record_divergence.json`, from git objects by explicit hash; no value is carried here, D-431). The ruling's own wording is that the hazard is discharged by freezing rather than by holding the writer forever — the epoch treatment a tool already applied to its own fields, applied one level up to the artifact. The hash STOP is what makes it a mechanism rather than a promise (#19).

**Status.** LIVE · decided 2026-08-08 · ratified by user

**Home.** `cowork_audit_protocol.md:590-597`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-08, Ruling 1 of `cowork_rulings_2026_08_08_pre_away.md` ("All three ratified"), applied 2026-08-08 by `cc_instruction_away_execution.md` Task 0. CLASSIFIED as a DECISION the register carries — rather than an exercise of one it already holds — by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), on the classification queue `ratification_surfaces/cowork_ruling_registration_queue_2026_08_09.md` entry A, whose ground is that the ruling states a REUSABLE METHOD a future wave meeting the same hazard needs and that nothing in the register carried it. Homed by that same ruling in `cowork_audit_protocol.md`'s dispatch-protocol block, in that block's own voice, per rule (e) and the D-645 homing pattern; `nonspec_kind` is `process` because its subject is how the record's own generated artifacts are kept, not the system. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT: what the user ruled is the classification and the home, and this text was written afterwards, so nothing here is self-ratifying (#14). The applying tool states the whole arrangement in its own docstring (`tools/audit/decisions/gen_home_classification.py`), which this entry points at rather than copying (#6). Cross-ref D-436 (the mechanism-change reservation the freeze was licensed under), D-648 (the maintenance-versus-mechanism line), `OPEN_ITEMS.md` OI-301 (the hazard class), OI-305 and OI-319 (the rows the hold was carried on).

### D-647 — The shell-read guard denies on indeterminate as standing policy, and the ceiling it cannot see is published in the measured rate

> ### When a shell-read policy cannot decide, it DENIES — and the ceiling it cannot see is published in the measured rate
>
> **Ruled by the user, 2026-08-08** (`cowork_ruling_guard_family_2026_08_08.md`, clauses 4 and 2).
> Two standing statements about the guard that enforces the working-tree-read rule, both of which
> bind beyond the act that introduced them.
>
> **DENY ON INDETERMINATE, adopted as standing policy.** Where the guard cannot decide whether a
> command reads working-tree content — the ruling's own case is a shell variable it has not
> expanded — it DENIES. *Why, in the ruling's own asymmetry:* **a false deny costs a retry through
> the file tools; a false admit costs an unverified read through the very mount whose measured
> stale-content failure created the working-tree-read rule.** The two errors are not the same size,
> so the policy is a consequence of that difference rather than a preference between them.

**In plain words.** Where the guard that stops working-tree files being read through a shell cannot tell whether a command reads one, it refuses. And where it decides by policy rather than by understanding the language — interpreter code — the shapes it cannot see are written into the corpus its rates are measured on, so the published refusal rate says what it does not cover instead of being silent about it.

**Why.** The asymmetry is stated in the ruling itself and is measured rather than assumed: a false deny costs a retry through the file tools, while a false admit costs an unverified read through the very mount whose measured stale-content failure created D-253 in the first place. The ceiling half rests on #17(d) and #19 together — a guard that cannot parse interpreter code and behaves as though it could is an unvalidated structural proxy standing in for a behavioral quantity, and a rate measured over a corpus that excludes the shape it cannot see bounds less than it appears to. Both halves are established over the extended corpus at `tools/audit/shell_read_guard_establishment.json`; no rate is carried here (D-431).

**Status.** LIVE · decided 2026-08-08 · ratified by user

**Home.** `cowork_audit_protocol.md:505-516`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-08, `cowork_ruling_guard_family_2026_08_08.md` clauses 4 (deny-on-indeterminate adopted as standing policy) and 2 (interpreter code decided by policy, with the computed-path residual carried into the corpus so the published rate reports the ceiling); applied 2026-08-08 by `cc_instruction_away_execution.md` Task 1, corpus first. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry D, on the ground that these two clauses bind beyond the act while the ruling's other three clauses are the mechanism change itself and its ordering, the ordering being attributed by the ruling to the earlier OI-343 and OI-345 rulings. Homed by that same ruling in `cowork_audit_protocol.md`'s dispatch-protocol block beside the three measured conditions a mechanism is judged on, because the ceiling half is a #19 statement about a published rate. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-253 (the rule the guard enforces), D-436 (the mechanism-change reservation), `OPEN_ITEMS.md` OI-300, OI-348, OI-351 (the family), OI-355 (the deny-side shape the corpus does not yet contain).

### D-648 — Moving an authored judgment whole into a retired block is authored-input MAINTENANCE, not a mechanism change

> ### Moving an authored judgment WHOLE into a retired block is MAINTENANCE, not a mechanism change
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_return.md`, Ruling 4(b)). A generated
> pass whose inputs are partly AUTHORED — a per-document judgment, a per-entry verdict, a per-row
> classification — STOPS when one of those inputs names something the tree no longer has. **Moving
> that judgment WHOLE into the pass's own retired block, with the reason it retired and with nothing
> deleted (#12), is AUTHORED-INPUT MAINTENANCE, and a session performs it. It is not a mechanism
> change**, so the reservation stated immediately above — that a mechanism's fate is decided by the
> user — is not engaged by it.

**In plain words.** Several generated passes take some hand-written judgments as input, and stop when one of those judgments names something the repository no longer has. Moving that judgment, unchanged and with its reason, into the pass's own retired list is ordinary upkeep that a session may do. Re-deciding it, deleting it, or writing a new judgment for something the pass never covered is a change to the mechanism, and that stays the user's.

**Why.** It draws the line that says when the mechanism-change reservation (D-436) is engaged, and it is recorded because the two acts look identical at the diff: without the line a session either returns to the user on every stale authored input or edits mechanisms under the cover of upkeep. Evidenced by recurrence rather than by argument — the same shape arose repeatedly across three consecutive batches, each time as a pass REFUSING TO RUN rather than as a defect a reader noticed, which is those passes' own STOPs working. The protection in the other direction (resurrecting a retired judgment unread also stops the pass) is what keeps retirement from becoming a quiet way of dropping an input (#12).

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:533-541`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 4(b) of `cowork_rulings_2026_08_09_return.md` ("agree with recommendations"), whose own words are that the act is the same authored-input maintenance performed under the tools' own STOPs and "not a mechanism change under D-436"; applied 2026-08-09 by `cc_instruction_return_continuation.md` Task 0. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry 4b, on the ground that it legitimises a CLASS and has since decided several acts across three batches; Ruling 4(a), the pointer re-aim, is classified an exercise and is not carried here. Homed by that same ruling in `cowork_audit_protocol.md` against the mechanism-change reservation it bounds. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-436 (the reservation), D-646 (the epoch treatment, whose own retirement discipline is the same shape one construct out).

### D-649 — Where the implementation contradicts the decision being homed, the decision is written in as what it is with the contradiction stated beside it and no verdict taken

> ### Where the implementation CONTRADICTS the decision being homed, the shelving is written in AS a shelving, the contradiction stated beside it, and the questions POINTED at their rows
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_return.md`, Ruling 5). Same family as
> the two rules above: a FORM for writing a decision into a specification when the plain form would
> state something false. **Where the record says a later build specified the opposite of the decision
> being homed, the decision is written into its owning section AS WHAT IT IS — a shelving as a
> shelving, a deferral as a deferral — the later build's contradiction is stated BESIDE it in a marked
> block, and the two questions that would need a judgment (does the implementation conform, and what
> should the rule now be) are POINTED at the rows that own them. NO VERDICT IS TAKEN either way.**

**In plain words.** Sometimes a decision has to be written into the specification that owns it while the code does the opposite. The form for that case is: record the decision as the kind of thing it is, state the contradiction next to it in a marked block, and point the two questions that would need judgment — does the code conform, and what should the rule now be — at the tracking rows that own them, deciding neither.

**Why.** Without the form such a decision cannot be homed at all: writing it plainly states a rule the code does not follow, omitting it leaves the decision homeless and criterion C1 with no closing act, and deciding which of the two is right is a judgment about the analysis that a filing act may not take. The form lets the record become complete without becoming untrue, which is exactly the split D-231's phase 1 draws between making the specifications complete and true and fixing what they then expose. It carries a pre-act check with it — the receiving section must STATE RULES rather than record findings, the register's own kind test, read before any home text is written.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:803-811`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 5 of `cowork_rulings_2026_08_09_return.md`, which names the pattern in terms ("D-286 is homed by the D-472 PATTERN") and attaches the STATES-RULES pre-act check as its own condition; applied 2026-08-09 by `cc_instruction_return_continuation.md` Task 2, where the check ran first and passed. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry 5, on the PATTERN only — the homing of the entry that occasioned it is an exercise. Homed by that same ruling in `cowork_audit_protocol.md` beside D-644, the other form for writing a decision into a specification when the plain form would state something false. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-231 (the phase-1 clause it serves), D-644 (the removal form), D-650 (the comparison condition and its remedy, the third of the family), D-286 and D-472 (the two entries homed under it).

### D-650 — Two same-dated texts are compared verbatim before either is retired into the other, and where they bind different acts they are homed side by side

> ### Two same-dated texts are compared VERBATIM before either is retired into the other; where they bind different acts they are homed SIDE BY SIDE
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_return.md`, Ruling 7, and
> `cowork_rulings_2026_08_09_second_stop.md`, Ruling 11 — one method, recorded as one rule because the
> test and the remedy are useless apart). Same family as the form above.
>
> **THE CONDITION.** Before a recorded decision is treated as ONE DECISION RECORDED TWICE and retired
> into a text that appears to duplicate it, **the two texts are compared VERBATIM, at their sources,
> and any BINDING difference is a STOP back to the user.** Sharing a date, an argument, a source and a
> vocabulary is not the test; what the two texts FORBID is.

**In plain words.** Before one recorded rule is folded into another that looks like a duplicate of it, the two texts are read side by side at their sources and compared word for word; if they forbid different acts, the folding stops and goes back to the user. Where that happens, the two are written into the same section beside each other, each pointing at the other, with the narrower prohibition kept in the words it was recorded in — never merged into one wider sentence.

**Why.** Applied at the case that produced it, the comparison stopped a collapse that would have lost the more specific and more easily violated of two prohibitions: a session could have obeyed the surviving text in full while breaching the one about to be retired into it. The remedy rests on #6 read correctly — #6 forbids two homes for ONE rule, and two texts that bind different acts are demonstrably two rules, so it does not demand the merge — while the merge itself would edit an already-ruled text (#14) and risks paraphrasing away the narrower prohibition (#12). The condition and the remedy are recorded as one rule because each is useless without the other: the test alone leaves a session with a STOP and no form to write the answer in.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:825-834`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** TWO user rulings of 2026-08-09, recorded as ONE entry on the user's instruction: Ruling 7 of `cowork_rulings_2026_08_09_return.md` supplies the verbatim-comparison condition, and Ruling 11 of `cowork_rulings_2026_08_09_second_stop.md` supplies the side-by-side remedy the condition leaves open. The condition FIRED when applied (`cc_instruction_return_continuation.md` Task 2, reported at `cowork_away_returns.md` §1.6) and the remedy was applied at the next stop (`cc_instruction_return_continuation_2.md` Task 0). CLASSIFIED as ONE DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entries 7 and 11 taken together, on the ground that splitting them across two entries would put the test in one place and what to do about it in another. Homed by that same ruling in `cowork_audit_protocol.md` beside D-649 and D-644. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-291 (the entry whose measurement half the condition fired on) and D-656 (the half homed side by side under the remedy), D-649 and D-644 (the same family).

### D-653 — A correction reconciling a specification to the arm that ships must carry the behavioural non-equivalence visibly, as unmeasured

> ### A correction that reconciles a specification to the arm that SHIPS carries the behavioural non-equivalence visibly, as unmeasured
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_second_stop.md`, Ruling 15). The
> doc-sync case of the same family. **Where a specification names one implementation as a rule's
> precondition and the arm that ships meets that precondition by a DIFFERENT design, the correction
> states the requirement rather than the implementation, names the design on each arm — and MUST CARRY
> THE RECORDED BEHAVIOURAL DIFFERENCE BETWEEN THE TWO ARMS VISIBLY, stated as UNMEASURED (#24). It may
> not word the difference away as equivalence, and it may not claim either arm's output is the better
> one.**

**In plain words.** When a specification says a rule depends on some earlier step, and the version of the program that actually ships meets that dependency by a different design, the fix is to state what the rule requires and name the design on each side. The correction must also say, visibly, that the two designs do not behave identically and that the difference has not been measured — it may not tidy the difference away into a sentence that reads as though the two were the same.

**Why.** An arm-reconciling correction invites exactly one failure: it reads as the two being the same, and a real, unmeasured behavioural difference disappears into a tidy sentence. That loses information the record held (#12) and asserts an equivalence nobody measured (#24), on the surface a later design will treat as the compliance reference. The instance that produced the ruling had that shape precisely — two mechanisms meet one requirement, one erasing a condition unconditionally and the other only making it expensive, with no comparison of the two outputs taken.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:917-925`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 15 of `cowork_rulings_2026_08_09_second_stop.md`, which puts the non-equivalence requirement in capitals as a condition on the licensed correction; applied 2026-08-09 by `cc_instruction_return_continuation_2.md` Task 0 at the `ARCHITECTURE.md` Layer-6 section. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry 15, NARROWLY — on the non-equivalence requirement only; the wording correction itself is phase-1 true-half work and an exercise. Homed by that same ruling in `cowork_audit_protocol.md` beside D-649 and D-650, the doc-sync case of the same family; the queue's stated alternative home was `CLAUDE.md`'s phase-1 clause and was not taken. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-472 (the entry whose wording the ruling corrected), D-649 and D-650 (the same family), `OPEN_ITEMS.md` OI-349 (the probe that established the by-other-means finding).

### D-654 — Where a licence's letter leaves a known falsity standing in the file it licensed, the session corrects it and REPORTS the widening in the same act

> ### Where a licence's letter leaves a known falsity standing in the file it licensed, the session CORRECTS it and REPORTS the widening in the same act
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_third_stop.md`, Ruling 17). The
> subsection above states the SCOPE of a licence. This states the one case that scope does not cover.
> **Where performing a one-edit licence to the letter would leave, in the very file being corrected, a
> second instance of the same falsity made false by the same act, the session CORRECTS THAT INSTANCE
> TOO AND REPORTS THE WIDENING IN THE SAME ACT — naming what it did, why the licence's heading-level
> subject covers it, and what the one edit would be if the narrower scope was meant.**

**In plain words.** A one-edit licence sometimes turns out to leave a second copy of the same false statement standing in the file it was granted for. The session fixes that too, and says so in the same act — what it did, why the licence's own heading covers it, and which single edit would undo it if the narrower reading was meant. A widening that is reported can be reviewed; a silent one cannot, and would not have been accepted. The default for every future licence is unchanged: read it narrowly.

**Why.** Its ground is stated with the ruling: leaving the second instance would ship a statement false at HEAD, in the very file being edited because its account of itself was false, which the doc-sync half of phase 1 does not admit. The half that keeps it from becoming a precedent is equally part of the rule — the one-edit licensing discipline's narrow-letter default is unchanged, so this is not permission to read a licence past its letter but a statement of what a session OWES when the letter leaves a known falsity in place. The excluded alternative is recorded with the ruling: reverting the second correction, which would knowingly re-insert a false statement in order to make a process point.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:966-973`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 17 of `cowork_rulings_2026_08_09_third_stop.md`, which accepts a past widening on a stated ground and says in terms that the report is part of what is ratified and that a silent widening would not have been accepted; recorded at its subject by `cc_instruction_return_continuation_3.md` Task 0 with nothing re-edited. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry 17, NARROWLY — on the reported-widening clause only; the acceptance of the one past act is an exercise. Homed by that same ruling in `cowork_audit_protocol.md` beside D-645, the subsection that states the scope of a licence, because this is the one case that subsection does not cover. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-645 (the licence scope), D-231 (the phase-1 true half the correction serves), D-644 (the shape the licensed replacement text was written in).

### D-655 — A session may author an owed establishment; its verdicts clear no guard until the reviewed set is applied

> ### A session may AUTHOR an establishment; its verdicts clear no guard until the reviewed set is applied
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_third_stop.md`, Ruling 18). The block
> immediately above says WHEN an establishment obligation starts gating. This says how it STOPS.
> **A session is licensed to perform an owed establishment and to author its verdicts — by the
> originating pass's own method and by no invented one (#6, #16) — and those verdicts CLEAR NO GUARD
> when they are written.** They are delivered as a ratification-surface reading file; the standing
> check goes on failing, deliberately, across the authoring session; and it clears only when the
> REVIEWED set is applied, in a commit that cites the user's ruling on it. **Authoring and clearing
> are two acts by two parties, and a session performs only the first.**

**In plain words.** A session may do an owed establishment and write down its verdicts, using the method of the pass that first performed one and not a method of its own. Those verdicts clear no check when they are written: they go to the user as a reading file, the check stays red across that session on purpose, and it clears only when the reviewed set is applied in a commit citing the user's ruling on it.

**Why.** It answers, structurally rather than by exhortation, the objection the occasioning row raised — that verdicts written in order to clear a guard are the weakest establishment there is, being the session's own unreviewed judgment discharging the session's own obligation, which is what #14 and #19 exist against. The remedy is that nothing self-ratifies because at the moment of writing there is nothing the verdicts could ratify; and it costs the user nothing to disagree, since a rejected verdict is one line in a reading file rather than an edit that has to be unwritten.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:690-699`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 18 of `cowork_rulings_2026_08_09_third_stop.md`, recorded on `OPEN_ITEMS.md` OI-354's row by `cc_instruction_return_continuation_3.md` Task 0 and EXECUTED at that dispatch's Task 1, with the guard deliberately left failing. CLASSIFIED as a DECISION by the user's Ruling 20 of 2026-08-09 (`cowork_rulings_2026_08_09_fourth_stop.md`), queue entry 18, NARROWLY — on the authoring-does-not-clear separation only; the licence itself and the by-that-method-and-no-invented-one half are exercises of #6 and #16. The queue flagged it as reasonably downgradable and the user ruled it KEPT, on the same ground as entry 12. Homed by that same ruling in `cowork_audit_protocol.md` beside the always-gates clause, which says when such an obligation starts gating where this says how it stops. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-438 (the gating declaration whose exception clause it completes), D-652 (the other clause governing when a register-clearing act may be performed), `OPEN_ITEMS.md` OI-289 and OI-354 (the verification and the population that grew).

### D-657 — A mechanism change is decided over its whole population both ways before it is applied, and only the members the defect's own shape names may move

> ### A mechanism change is decided over its WHOLE population BOTH WAYS before it is applied, and only the members the defect's own shape names may move
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fourth_stop.md`, Ruling 25). The two
> rules above bound the mechanism question from either side — how a mechanism is JUDGED once it
> exists, and when the mechanism-change reservation is ENGAGED at all. This states what a mechanism
> CHANGE owes BEFORE it is applied.
>
> **THE CONDITION.** Every member of the population is decided under **BOTH** rules — the one live at
> HEAD and the proposed one — before and after. **Only the members the defect's own shape names may
> move. ANY OTHER MOVEMENT IS A STOP back to the user**, and the change is not applied.

**In plain words.** Before a proposed change to one of the record's own mechanisms is applied, every member of the population that mechanism reads is decided twice — once under the rule running now and once under the proposed rule — and the two answers are compared per member. Only the members the defect's own description names are allowed to move. Anything else moving stops the change and returns it to the user.

**Why.** It binds because it has already killed a ruled remedy: applied at the case that produced it, the both-ways table established that the proposed correction fixed one member of its population and broke two, where a forward-only application would have reported the fix alone. The construction is part of the rule for the same reason — a table that implements both rules itself can SHOW a movement, while a diff of outputs can only assert that something changed. Nothing in the register carried the test: D-436 judges a mechanism by three measured rates once it exists, which is a different question, and D-648 draws the maintenance-versus-mechanism line without saying what a mechanism change owes before it is applied.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:557-566`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 25 of `cowork_rulings_2026_08_09_fourth_stop.md`, whose correction was then REFUTED by this very condition and never applied — the condition is what survives, and it is the whole of what is registered here. CLASSIFIED as a DECISION, narrowly, by the user's Ruling 36 of 2026-08-09 (`cowork_rulings_2026_08_09_sixth_stop.md`), on the classification queue `ratification_surfaces/cowork_ruling_registration_queue_2026_08_09.md` §7 entry 25; the queue flagged it as reasonably downgradable — the ruling calls it 'the A5 pattern', naming a dispatch assumption — and the user ruled it KEPT as a decision on the standing cheap-insurance ground. Homed by that same ruling in `cowork_audit_protocol.md`'s dispatch-protocol block beside D-436 and D-648, in that block's own voice, per rule (e) and the D-645 homing pattern. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT: what the user ruled is the classification and the home, and this text was written afterwards (#14). The two applications and their findings are at `cowork_away_returns.md` §1.10 and the fifth continuation's Task 1 log, and no value is carried here (D-431). Cross-ref D-436 (the three measured conditions, whose own text carries the ground that a mechanism firing on legitimate work is worse than none), D-648 (the maintenance-versus-mechanism line), `OPEN_ITEMS.md` OI-356, OI-361, OI-362 (the family the condition was applied over).

### D-658 — Where the record does not settle the question, the surface that returns it to the user gathers facts and makes no recommendation

> ### Where the record does not settle the question, the surface that returns it to the user gathers FACTS and makes NO recommendation
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fourth_stop.md`, Ruling 27), on the
> user's own instruction, quoted in the ruling verbatim: *"follow the rule: fact based decisions or
> exploration to gather facts are allowed, not decided on unsure/fabulated/misremembered facts."* The
> third member of the family above, and the case those two do not cover: not *the plain form would
> state something false*, but *the record does not answer the question at all*.
>
> **THE FORM.** Where a question the session cannot settle has to go back to the user, the surface it
> goes back on carries: **every claim CITED AT ITS SOURCE and read in place; the records concerned
> READ WHOLE; anything the record does not settle marked UNSETTLED rather than filled — and NO
> RECOMMENDATION AT ALL.**

**In plain words.** When a question has to go back to the user because the record does not answer it, the surface it goes back on cites every claim at the place it can be checked, reads the records concerned whole, marks anything the record does not settle as unsettled instead of filling it in, and offers no recommendation of any kind.

**Why.** The no-recommendation clause is the load-bearing one and the one a session will be tempted to break: a fact-gathering pass that ends in a recommendation has decided the question it was sent to inform, so the user then rules on the session's reading rather than on the facts — which is exactly what the user's quoted instruction exists against. Marking an item unsettled is likewise an answer rather than a shortfall, since filling it from the most plausible reading is the invention D-112 forbids. Evidenced at the case that produced it: gathering the facts LOCATED a conflict between two records that nobody had put side by side, wrote both readings onto the surface, and chose neither — a pass permitted to recommend would have chosen one, and the conflict would have been settled by a session's reading of intent.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:891-902`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 27 of `cowork_rulings_2026_08_09_fourth_stop.md`, which quotes the user's instruction verbatim and takes no verdict on the cell it was asked about; the surface it ordered was delivered at `ratification_surfaces/cowork_d580_transfer_fact_gathering_2026_08_09.md` and the user then ruled the cell on facts (Ruling 34). CLASSIFIED as a DECISION, narrowly — on the fact-gathering-surface FORM only, the refusal to decide one cell being an exercise — by the user's Ruling 36 of 2026-08-09 (`cowork_rulings_2026_08_09_sixth_stop.md`), queue §7 entry 27; the queue flagged it as reasonably downgradable, on the reading that the no-recommendation clause is already implied by #5 and D-112, and the user ruled it KEPT. Homed by that same ruling in `cowork_audit_protocol.md` beside D-649 and D-650, the third member of that family. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-112 (never work from memory), D-649 and D-650 and D-653 (the same family of forms), D-580 (the cell the form was built for), `OPEN_ITEMS.md` OI-365 (the residual the ruling declined to decide).

### D-661 — Complete means complete relative to a named derivation, whose measured miss rate against the record is part of its name

> ### "Complete" means complete relative to a NAMED DERIVATION, whose measured miss rate against the record is part of its name
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fifth_stop.md`, Ruling 31; restated as
> the standing statement by Ruling 37 of `cowork_rulings_2026_08_09_sixth_stop.md` when the derivation
> it licensed came back negative). It belongs beside the three measured conditions above because it is
> the same rule one level out: those say what a MECHANISM is worth unmeasured, and this says what a
> COMPLETENESS CLAIM is worth unmeasured.
>
> **A hand-made inventory's completeness is not known, and it becomes checkable BY DERIVATION.** The
> candidate population is DERIVED from named surfaces; the existing hand-made list is demoted to
> **SEED VERDICTS** rather than standing as the population; every derived candidate carries an
> AUTHORED verdict; **an unclassified candidate is a STOP**; and the derivation is RE-DERIVED as the
> tree grows. *Complete* thereafter means complete **relative to that named derivation** and to
> nothing wider.

**In plain words.** A hand-made list cannot be known to be complete just because nobody has found a gap in it. It becomes checkable by deriving the candidate population from named surfaces, treating the hand-made list as seed verdicts rather than as the population, requiring an authored verdict for every derived candidate, stopping while any candidate is unclassified, and re-deriving as the tree grows. Complete then means complete relative to that named derivation, and the derivation's measured miss rate against the seed is published as part of what it is called.

**Why.** It is #19 applied to a completeness claim: an inventory trusted because nobody has found a gap in it is exactly the thing merely unfalsified, and the register stated the test nowhere else. The miss-rate half has its own measured ground — the derivation licensed under this rule missed seed words the record already held, and one seed word was missed by both readings of the musical surface, so the record is not a subset of the derivation either; a derivation that misses a known positive cannot be trusted to have found the unknown ones. That is also why the population stays advisory rather than being narrowed until the misses disappear, which would be fitting the signal to the cases that motivated it (DT-2).

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:403-416`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 31 of `cowork_rulings_2026_08_09_fifth_stop.md`, executed by `cc_instruction_return_continuation_5.md` Task 2; its outcome was then ruled by the user's Ruling 37 of `cowork_rulings_2026_08_09_sixth_stop.md`, which records the completeness question as ANSWERED rather than closed and makes this the standing statement of what complete means here. CLASSIFIED as a DECISION, narrowly — on the derived-population answer to the completeness question only, the scanner licence itself being an exercise — by the user's Ruling 36 of 2026-08-09, queue §7 entry 31; the queue flagged it as reasonably downgradable, on the reading that the derived-population-with-authored-verdicts-and-a-STOP shape is already the practice of three existing tools, and the user ruled it KEPT. Homed by that same ruling in `cowork_audit_protocol.md` beside D-436. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Every measured value lives in `tools/audit/reserved_word_scanner.json` and none is carried here (D-431). Cross-ref D-436 (the three measured conditions, whose third is the separation a derived population must show before it may guard), D-660 (the cleanup this inventory feeds), `OPEN_ITEMS.md` OI-229 (the tracking row).

### D-663 — A direction with its artifact named is not a transcribed value

> ### A DIRECTION with its artifact named is not a transcribed value
>
> **Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fifth_stop.md`, Ruling 35(c)). A
> reading of the rule immediately above, recorded against it so that a session meeting the
> prohibition meets the clause that says what it still permits. **A DIRECTION — *fewer than half*,
> *the large majority*, *markedly better* — stated with the generated artifact CITED BESIDE IT is not
> a transcribed value, and is what the rule above asks for.**

**In plain words.** Saying which way a result went — fewer than half, the large majority, markedly better — with the generated artifact named beside it is not a transcribed value and is allowed. It does not permit restating the value itself, in digits or in words, and it does not relax the rule that an asserted difference between two measured quantities carries its uncertainty.

**Why.** The prohibition it reads exists so that a quantity cannot enter prose and then go stale while the artifact moves; a direction with its artifact named leaves the value in the artifact and still tells a reader what was found. Without the clause the safe reading of the prohibition is that any characterization of a result is forbidden, which would make findings unreportable — and sessions had repeatedly had to guess at where the line falls, which is the recurrence that made it worth ruling.

**Status.** LIVE · decided 2026-08-09 · ratified by user

**Home.** `cowork_audit_protocol.md:272-278`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-09, Ruling 35(c) of `cowork_rulings_2026_08_09_fifth_stop.md`, taken over the qualitative characterizations in `OPEN_ITEMS.md` OI-363's row, which are ruled ACCEPTABLE and were not re-edited; recorded on that row by `cc_instruction_return_continuation_5.md` Task 0. CLASSIFIED as a DECISION, narrowly — on that clause only — by the user's Ruling 36 of 2026-08-09 (`cowork_rulings_2026_08_09_sixth_stop.md`), queue §7 entry 35c, on the ground that it is a reading of D-431 the register does not carry. Homed by that same ruling in `cowork_audit_protocol.md` beside D-431 itself. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14). Cross-ref D-431 (the prohibition it reads), D-187 (principle #24, the uncertainty requirement it does not relax), `OPEN_ITEMS.md` OI-363 (the row the ruling was taken over).

### D-668 — A homing act tests a section in a FIXED ORDER — pointer move first, kind half before any write — and a findings-recording owner means HELD, never written by stretch

> ### A homing act tests a section in a FIXED ORDER — pointer move first, kind half before any write — and a findings-recording owner means HELD, never written by stretch
>
> **Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_tenth_stop.md`, Ruling 49, taking the
> upgrade reading of Ruling 40 of `cowork_rulings_2026_08_09_eighth_stop.md`). Same family as the two
> forms above, and the one they leave out: those say HOW to write a decision into a section that will
> not take the plain form, and this says **in what order a homing act tests a section at all, and what
> happens when the test fails.**

**In plain words.** A homing act tests the owning section in one fixed order. First it tries the cheapest act: if that section already states the rule, the entry's pointer moves there and no text is written. Only if it does not does the act write the rule in, and only where the section states rules at all. Where the owning section records findings instead, the entry is HELD with its row named, because adding a rule-stating block to a findings table is a document-structure act reserved to the user. The kind judgment is made per section and before any writing, and an entry fitting none of the three steps stops the act rather than being decided.

**Why.** Each step exists against a different failure, which is why the order binds rather than describing good practice: step 1 first, because a write that was not needed is a second statement of a homed rule (#6) and a session starting at step 2 makes one; the kind half before the write, because a section judged afterwards is judged by a reader who has already written into it; and step 3 rather than a widened step 2, because the temptation at a findings table is exactly to argue it into a rule-stating section, which turns a mechanical test into a matter of taste. The procedure earned the upgrade by measurement rather than by argument: applied over one document's whole set, step 1 closed NOTHING with two near-misses recorded as checked-and-declined, and step 3 fired for four entries that were not one shape — and the user's own rulings on all four confirmed the STOP rather than relaxing it, three needing no home at all and the fourth closing by a write only because the user MADE the general rule a session may not compose.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_audit_protocol.md:850-856`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 49 of `cowork_rulings_2026_08_11_tenth_stop.md`, which TAKES the upgrade reading the registration queue's §11.1 offered for Ruling 40 of `cowork_rulings_2026_08_09_eighth_stop.md` — its ground being that the order and the STOP bind every homing act, that they have fired correctly twice, and that their only carrier was a generator's own text no future act elsewhere would find, which makes registering them the insurance logic rather than an exception to it. Applied by `cc_instruction_return_continuation_10.md` Task 1. Homed by that same ruling in `cowork_audit_protocol.md`'s homing-under-difficulty family, beside D-653 (the shelving form) and D-657's neighbour D-649/D-650 line — the sections that say HOW to write a decision a section will not take plainly, where this says in what ORDER a section is tested at all. THE KIND HALF WAS JUDGED BEFORE THE WRITE: the dispatch-protocol block states in its own opening that what follows are rules governing every dispatch, and every existing subsection states one with its ruling and its defense. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification and the home, and the entry text was written afterwards. The licence half of Ruling 40, scoped to nine named entries, is EXERCISED and expired and is deliberately not carried here; what is registered is the order, the kind-half timing and the STOP. Cross-ref D-653 (the shelving form), D-655 (the authoring-does-not-clear separation), D-664 (rule (l), the ROUTE this procedure executes), D-666 and D-667 (the two cases the procedure's step-3 holds produced), D-430 (the section-level home unit whose kind half this fixes the timing of).

### D-669 — A maintenance act establishes the cause BEFORE it touches the mechanism — and a cause that resists establishment is a STOP, with no fix taken on a named-but-unasserted candidate

> ### A maintenance act ESTABLISHES THE CAUSE before it touches the mechanism — and a cause that resists establishment is a STOP, with no fix taken on a named-but-unasserted candidate
>
> **Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_eleventh_stop.md`, Ruling 52, taking
> Ruling 50 of `cowork_rulings_2026_08_11_tenth_stop.md`). The two sections above say what a MECHANISM
> is worth unmeasured and what a COMPLETENESS CLAIM is worth unmeasured. This says what an ACT owes
> before it changes a mechanism at all, and it is sited here so that a reader meeting the fix order in
> the guard-family rules below meets the diagnosis order first.

**In plain words.** Before a maintenance act changes a failing mechanism, it must establish at the objects WHY the mechanism is failing. The fix comes only after that, in whatever order that mechanism's own family discipline sets. If the cause cannot be established, the act stops and goes back to the user, and no fix is taken on a candidate cause the record merely names — not even a candidate that later turns out to be right.

**Why.** The STOP is stated rather than left to #19 because a named-but-unasserted candidate LOOKS like a diagnosis: a row that names a plausible cause and honestly declines to assert it reads, one wave later, as though the cause were known, so a fix gets taken on it and the symptom disappearing is read as confirmation — the merely-unfalsified trust #19 refuses, arriving by the one route that looks like diligence. The register already carries the FIX half's order for this family (corpus rows first, both rates re-measured on the same extended corpus, the revert condition governing) at D-436 and the guard-family entries, and none of them says the cause must be established first or what happens when it cannot be. The act that produced the ruling also supplies the evidence: the diagnosis was taken with NO change to the tool — the module loaded twice from its own file by an ordinary import from outside the repository, once under each spelling of the drive letter in that path, each load applying the same equality test the mechanism applies to its own artifact — while the row's own closing clause had declined that diagnosis on the ground that it would change the tool. A tool can be diagnosed without being edited, so declining a diagnosis on that ground is a conclusion that deserves checking.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_audit_protocol.md:472-478`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 52 of `cowork_rulings_2026_08_11_eleventh_stop.md`, which ratifies the registration queue's §13 with BOTH proposed decisions KEPT and takes Ruling 50 of `cowork_rulings_2026_08_11_tenth_stop.md` as a register entry at the home §13.3 proposes. Applied by `cc_instruction_return_continuation_11.md` Task 0. The ruling's recorded ground for keeping it a decision: a named-but-unasserted candidate looks like a diagnosis, and nothing in the register stated the act-level order or its STOP. THE KIND HALF WAS JUDGED BEFORE THE WRITE: the dispatch-protocol block states in its own opening that what follows are rules governing every dispatch, and every existing subsection states one with its ruling and its defense. SITING: immediately after the two conditions-family sections (D-436's three measured conditions and D-661's completeness rule) and immediately before the guard-family sections whose FIX order it precedes, which is what the proposed home's own words ask for — a reader meeting the fix order meets the diagnosis order in the same place. It was NOT inserted between D-436's and D-661's sections, because D-661's own text claims adjacency to D-436 and an insertion there would have weakened a standing statement to gain nothing. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification and the home, and the entry text was written afterwards. The queue offered a downgrade reading in one line (read the order as #19 applied to one act) and the user KEPT the decision. Cross-ref D-436 (the three measured conditions this precedes), D-661 (completeness by named derivation), D-670 (the sibling ruled in the same act, the other half of how an act is SEQUENCED), D-648 (authored-input maintenance versus a mechanism change), D-655 (the authoring-does-not-clear separation).

### D-670 — A task that cannot be stopped partway is dispatched FIRST with nothing large in front of it, and the ordering is ruled rather than preferred

> ### A task that CANNOT BE STOPPED PARTWAY is dispatched FIRST, with nothing large in front of it — and the ordering is RULED, never left to a preference
>
> **Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_eleventh_stop.md`, Ruling 52, taking
> Ruling 51 of `cowork_rulings_2026_08_11_tenth_stop.md`). Every other rule in this block says what a
> dispatch may contain or how an act inside one is performed. This says in what ORDER the tasks of a
> dispatch are placed, and it exists because two rules the project already runs on collide and nothing
> said which wins.

**In plain words.** Some tasks have to be finished whole or not published at all, because publishing a portion of a derived population reads as covering the class. Others — per-entry passes — can stop at any member boundary, since each finished member stands on its own. The second kind will always soak up whatever capacity is left, so the first kind is placed first in a dispatch, with nothing large before it, and that placement is written down as a ruling rather than left as the dispatch-writer's preference.

**Why.** A preference does not survive one more capacity squeeze, which is why the placement is ruled. The structural point is that such a task is small in COUNT and large in READING, so every honest estimate of it looks cheap while every attempt at it loses to work that can stop at a boundary — and each individual refusal is CORRECT on its own terms, which is what makes the pattern invisible from inside any one dispatch. It is measured rather than argued: one such task was declined by seven consecutive dispatches, every refusal right for the same reason each time, and dispatched first under this rule it closed WHOLE in one act and turned up a finding nobody was looking for while deriving its own population — the ordering being the whole difference, with nothing about the task changed.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_audit_protocol.md:988-994`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 52 of `cowork_rulings_2026_08_11_eleventh_stop.md`, which ratifies the registration queue's §13 with BOTH proposed decisions KEPT and takes Ruling 51 of `cowork_rulings_2026_08_11_tenth_stop.md` as a register entry at the home §13.3 proposes. Applied by `cc_instruction_return_continuation_11.md` Task 0. The ruling's recorded ground for keeping it a decision: the unstoppable-task class recurs with every whole-population derivation, and a rule arbitrating between two recorded rules belongs in the register rather than in dispatch prose, its collision measured at seven consecutive correct refusals. THE KIND HALF WAS JUDGED BEFORE THE WRITE: the dispatch-protocol block states in its own opening that what follows are rules governing every dispatch. SITING, RECORDED RATHER THAN SMOOTHED OVER: the proposed home named this block *beside the two rules it arbitrates between*, and those two — the no-silent-cap rule and the partial-stop allowance — are subsections of NO governing surface, living only in dispatch prose and session records, which is itself one reason nothing ever stated what happens when they meet. The entry is sited in the block the ruling names, at its end, with the two rules stated in the terms this rule needs them in; homing them is a separate act nobody has ruled and it is not taken here. It was not placed among the block's original three rules, because the block's own preamble counts them. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification and the home, and the entry text was written afterwards. The queue offered a downgrade reading in one line (read it as one dispatch's sequencing decision, already discharged) and the user KEPT the decision. ★ THE SITING NOTE'S CLOSING CLAUSE IS OVERTAKEN 2026-08-11: the user's Ruling 55 of `cowork_rulings_2026_08_11_twelfth_stop.md` ruled that separate act, and both arbitrated rules are now homed immediately below this entry's own section as D-671 and D-672. The former wording stands in place at the home (#12) with a dated correction beside it; nothing in this entry's rule moves. Cross-ref D-669 (the sibling ruled in the same act, the other half of how an act is SEQUENCED), D-671 and D-672 (the two rules this one arbitrates between, homed one stop later), D-250 (dispatches are written only when they are next), D-251 (a running dispatch is never interrupted or steered mid-flight), D-436 (the measured-conditions rule whose derivations are the unstoppable class).

### D-671 — A derivation, a measurement or a sizing over a derived population is published WHOLE or not at all, and a subset only under a scope that NAMES its members

> ### A derivation, a measurement or a sizing over a derived population is published WHOLE or not at all — and a subset is published only under a scope that NAMES its members
>
> **Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_twelfth_stop.md`, Ruling 55), which
> homes a rule this project had been running on since the fourth return continuation without any
> governing surface stating it. The rule above arbitrates between this rule and the one below; until
> this act neither of the two was written anywhere a session would find them.

**In plain words.** If a task's deliverable is one derivation, one measurement or one sizing over a population that is derived rather than chosen, it covers all of that population or it is not begun. Where a subset has to be published anyway, the surface carrying it names its members one by one, so nobody can read it as the whole.

**Why.** A derivation covering some of its population READS as covering the class, and the failure is silent by construction: the surface looks complete, every value in it is correct, and nothing in it says what was left out — so a reader is not under-informed but wrongly informed, with no way to notice. That is why *opened and left part-done* is worse than *not opened*, which reverses the ordinary presumption about partial progress. The second half exists so the rule does not throw away findings: a subset whose members are NAMED cannot be mistaken for the whole, which removes the silent half of the failure and keeps the finding — the shape both published subsets on the record actually used. Measured rather than argued: one derivation was declined by seven consecutive dispatches, each refusal citing this rule and each correct on its own terms, and the cost of those refusals is what the ordering rule D-670 exists to pay rather than an argument against this one.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_audit_protocol.md:1033-1038`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 55 of `cowork_rulings_2026_08_11_twelfth_stop.md`, which homes the no-silent-cap rule and the partial-stop allowance in the audit protocol's dispatch-protocol block beside D-670, in that block's own voice, each with the defense the record holds. Applied by `cc_instruction_return_continuation_12.md` Task 1. THE REGISTER MECHANICS ARE THE RULING'S OWN: it directs that where either rule already carries an entry that entry's home moves, and where it does not the entry is CREATED. Checked at the register data before the write — NEITHER rule carried an entry — so this is a creation, landing in the commit that records the ratification (rule (c)). THE KIND HALF WAS JUDGED BEFORE THE WRITE: the dispatch-protocol block states in its own opening that what follows are rules governing every dispatch, and every existing subsection states one with its ruling and its defense. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the homing and its site, and the entry text was written afterwards; Ruling 55's own classification joins the registration queue's seventh extension for the user's next ratification. Cross-ref D-670 (the ordering rule that arbitrates between this rule and D-672, and whose siting note recorded that these two had no governing surface), D-672 (the other half of the arbitration), D-436 (the measured-conditions rule whose derivations are this rule's principal subject), D-661 (completeness relative to a NAMED derivation, which is what makes a whole-population claim checkable at all).

### D-672 — A per-entry pass may be stopped at any member boundary, and the stop is RECORDED — what was done, what was not, and that the remainder is untouched

> ### A PER-ENTRY PASS may be stopped at any member boundary, and the stop is RECORDED — what was done, what was not, and that the remainder is untouched rather than partly worked
>
> **Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_twelfth_stop.md`, Ruling 55), the
> second of the two rules the ordering rule above arbitrates between, and homed in the same act for the
> same reason: it governed every batch of this arc from dispatch prose alone.

**In plain words.** A task that works through members one at a time — entries, rows, sites — may stop at any member boundary, on capacity or because a later task binds harder, and that is a result rather than a failure. When it happens the record says which members were completed, that the remainder was left untouched rather than partly worked, and that nothing is left half-edited.

**Why.** The allowance is safe here and nowhere else because each completed member is WHOLE IN ITSELF: a homed entry, a corrected row, a re-aimed anchor is not made wrong by the next one never happening, so a stopped pass publishes nothing that reads as more than it is — exactly the property a derivation over a population does not have, which is why these are two rules and not one. The recording clause is the load-bearing half: an unrecorded stop turns a per-entry pass into the thing D-671 forbids, since a reader meets a list of completed members and cannot tell a finished pass from an interrupted one. It is also why the continuing session DERIVES the remainder fresh rather than carrying the stopping session's account of it.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_audit_protocol.md:1069-1073`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 55 of `cowork_rulings_2026_08_11_twelfth_stop.md`, the second of the two homings that ruling orders. Applied by `cc_instruction_return_continuation_12.md` Task 1. Checked at the register data before the write — this rule carried NO entry — so this is a creation under the ruling's own register mechanics, landing in the commit that records the ratification (rule (c)). THE KIND HALF WAS JUDGED BEFORE THE WRITE, at the same block and by the same reading as D-671. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the homing and its site, and the entry text was written afterwards. WHAT THE HOME TEXT DELIBERATELY DOES NOT CARRY: no count of the stops this arc has taken and no identity of any batch that took one — those are records of acts and live in the batch logs that made them (D-431); the section states the rule and names the shape only. Cross-ref D-670 (the ordering rule that arbitrates between D-671 and this one), D-671 (the rule this one is the exception to, and the reason the exception is safe), D-250 (dispatches are written only when they are next), D-251 (a running dispatch is never interrupted or steered mid-flight).

### D-673 — An enumerating pattern whose reach is unmeasured may STATE its bound on its own artifact, and the test is whether an analysis decision consumes it

> ### An ENUMERATING PATTERN whose reach has never been measured may STATE its bound on its own artifact instead of owing a detection measurement — and the test is whether an ANALYSIS DECISION consumes it
>
> **Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 60, taking
> the proposed decision of Ruling 59 of `cowork_rulings_2026_08_11_thirteenth_stop.md`). It belongs
> beside the two sections above for the reason the second gives for its own siting: those say what a
> MECHANISM is worth unmeasured and what a COMPLETENESS CLAIM is worth unmeasured, and this says which
> of the two an ENUMERATING PATTERN is — a search expression run over text to locate every instance of
> a class.
>
> **THE RULE.** Where such a pattern's reach against the text it scans has never been measured, the
> limit may be **STATED ON THE PATTERN'S OWN ARTIFACT** — marked advisory, with its empty verdict
> recorded as bounding nothing — **instead of a detection measurement being owed**. **THE TEST FOR
> WHICH IT IS: does an ANALYSIS DECISION CONSUME the enumeration?** Where one does, the measurement is
> owed exactly as the three conditions above require and the bound is no substitute for it. Where none
> does, the bound is the whole of what is owed.

**In plain words.** A search expression used to find every instance of a class can be trusted only as far as its reach against the text it scans has been measured. Where that reach has never been measured, the limit may simply be written on the pattern's own artifact — marked advisory, with an empty run recorded as evidence of nothing — instead of a detection measurement being owed. Which of the two applies is decided by one question: does an analysis decision consume the enumeration? If one does, the measurement is owed and the stated bound is no substitute. The test is applied per enumeration and is never inherited from a similar-looking pattern.

**Why.** As the record stood without it, D-436's detection-rate condition and D-661's completeness rule together left every unmeasured enumerating pattern owing a measurement, with no route by which any of them could ever be written off — so the register carried the obligation and never its limit, and an obligation that cannot end is one that never closes. The clause concentrates establishment effort where #19 buys something: on the measurement chain that feeds inference. It is safe because a stated bound claims nothing about coverage — it records that the misses are unknown, so an empty run may not be cited as evidence — and what it removes is the standing debt rather than the ignorance. The instance it was ruled at is a comment sweep that reported its class empty at HEAD while an instance of the class stood in a file the correcting act had touched: nothing in the analysis consumes a comment sweep, so the bound was stated and the measurement declined. The excluded alternative is the reading the record already carried — owing the measurement — which had produced no measurement in any wave that met the pattern.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `cowork_audit_protocol.md:434-448`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 60 of `cowork_rulings_2026_08_11_fourteenth_stop.md`, which RATIFIES the proposed decision the ruling-registration queue's §19 put forward for the second half of Ruling 59 (`cowork_rulings_2026_08_11_thirteenth_stop.md`) and KEEPS it as a DECISION, the offered downgrade reading declined. Applied by `cc_instruction_return_continuation_14.md` Task 0. Checked at the register data before the write — the rule carried NO entry — so this is a creation landing in the commit that records the ratification (rule (c)). THE KIND HALF WAS JUDGED BEFORE THE WRITE: the receiving block of `cowork_audit_protocol.md` states rules with their ruling and their defense in every existing subsection, and the two sections this one sits beside are the homes of D-436 and D-661. ★ THE HOME IS DERIVED RATHER THAN PROPOSED, AND THAT DEPARTURE IS REPORTED: the queue's §19 carries no proposed-home subsection although its own §1 rule requires one for every ruling proposed as a DECISION, so the site was taken from the record instead — both entries this clause qualifies, D-436 and D-661, are homed in this block, and that block's own text states the one-level-out siting logic it is placed under. Recorded at `cowork_away_returns.md` §1.18 so the departure is reviewable rather than silent. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the classification, and the entry text was written afterwards. Cross-ref D-436 (the three measured conditions, whose detection-rate condition this bounds), D-661 (completeness relative to a NAMED derivation, the other half of the debt this closes), `OPEN_ITEMS.md` OI-368 (the row whose second half this ruling closed without the measurement being taken), OI-367 (the sibling pattern this ruling explicitly does NOT reach — the test is applied per enumeration).

### D-675 — Phase 1 completes when the INFERENCE-BEARING obligations are discharged — the finish line is cut by D-438's test, the apparatus residue does not gate the completion, and the cut carries a falsification test

> **★ WHEN PHASE 1 IS COMPLETE — THE FINISH LINE IS CUT BY D-438'S TEST, AND THE APPARATUS RESIDUE
> DOES NOT GATE THE COMPLETION (user-ruled 2026-08-11; the ruling record is
> `cowork_rulings_2026_08_11_fifteenth_stop.md`, Ruling 65).**

**In plain words.** Phase 1's own clause says what phase 1 requires, but not which of those requirements its completion waits on — and the derived finish line waited on all of them. From now on each item of that finish line is sorted by the same test that decides whether an open row makes a stage wait: does its subject bear on the analysis, on the analysis's inputs, or on a measurement tool something depends on? Phase 1 completes when the items that pass that test are discharged; the residue about the project's own paperwork does not hold it up. An obligation to establish that something works still gates whatever its subject. The sorting is computed and regenerated rather than decided by hand, the state before the sorting is kept beside the state after it, and the sorting halts if it ever files as paperwork something the record elsewhere says bears on the analysis.

**Why.** Stated with the ruling, in the user's own recorded ground: the documentation work was genuinely valuable and its marginal value has fallen — the struck-versus-sounding family, the unspecified candidate-admission rule, the layer wrongly assumed tonic-independent, and the finding that a key-layer design sitting's decisions had no object on the shipping arm were all found by reading specification against code or by probes, while most of the rulings the registration queue's §21 carried have record-keeping about record-keeping as their subject — the ruling record's own wording, and no count is restated here (D-431). D-641's own recorded ground says the same thing from the other side: the apparatus is now large enough to generate its own defect stream indefinitely, and treating each defect as owed is what produced the backlog `OPEN_ITEMS.md` OI-337 records. The mechanical point is that this applies to the FINISH LINE the non-gating declaration D-438 already carries — the one surface the record had never applied it to: D-438 governs what a STAGE waits on, D-639 says in terms that what PHASE 1 OWES is a different test with a different subject, and the finish line's items therefore carried their gate separately, with one item explicitly the class whose place had not been decided. The falsification test is what keeps the declaration distinguishable from wishful filing, and the derived-not-hand-classified clause is D-436's own reservation with OI-336 as the recorded lesson of hand-adding a gate verdict.

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `CLAUDE.md:1606-1633`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 65 of `cowork_rulings_2026_08_11_fifteenth_stop.md`. Applied by `cc_instruction_apply_the_bearing_cut.md` Task 1. Checked at the register data before the write — NO entry stated this rule, which is the dispatch's assumption A2 discharged rather than assumed: the nearest neighbours are D-231 (the three phases), D-438 (an apparatus row gates nothing but stays owed), D-639 (how far the doc-sync half reaches) and D-641 (a FINDING's disposition), and none of them says when phase 1 completes. So this is a creation landing in the commit that records the ruling (rule (c)), and the ruling record itself says no exercise reading was available for it. ★ THE HOME WAS DERIVED AND VERIFIED, NOT ASSUMED, and the comparison is recorded because the dispatch named two candidates and required a STOP if they were equally supported. The dispatch-protocol block of `cowork_audit_protocol.md` was the other candidate and is NOT equally supported: that block declares its own scope in its own words — the rules there govern every DISPATCH, and the document is their home because it is where the project's dispatch-construction rules already live — and this rule governs neither how a dispatch is written nor how an act inside one is performed. It states when a PHASE completes, which is D-231's own subject, and D-231's clause is in `CLAUDE.md`. The closest precedent points the same way: D-639, the immediately preceding ruling about how far a phase-1 HALF reaches, is homed at this very clause; the counter-precedents D-642 and D-644 are homed in the protocol block because they govern how a DERIVATION over the register reads criterion C1, which is a different subject. THE HOMING PROCEDURE (D-668) WAS RUN IN ITS FIXED ORDER: step 1 was tried FIRST and DECLINED — the phase-1 clause states the three phases and their strict order and says nothing about which requirements the completion waits on, so no pointer move was available and a write was needed; step 2 then applied, the section STATING RULES rather than recording findings, judged before the write. The edit surface is licensed: the 2026-08-07 ruling widens a HOMING dispatch's surface to `CLAUDE.md` scoped to homing acts alone, and this is one. THE GROUPING is presentational and is recorded rather than left silent: group T (standing process rules) beside D-231, D-436, D-438 and D-641, the alternative being group S beside D-639, which shares the home but not the subject. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the rule, and the entry text was written afterwards. Cross-ref D-231 (the phase whose completion this decides), D-438 (the declaration whose test this applies to the finish line), D-639 (the neighbouring rule at the same home, which still decides what the doc-sync half REACHES), D-676 (the sibling ruled in the same act — what an apparatus row is then OWED), D-436 (a gating verdict comes from a cut and is never hand-added), D-641 (the same test applied to a FINDING rather than to the finish line), `OPEN_ITEMS.md` OI-336 (the recorded lesson of a hand-added gate verdict).

### D-676 — An apparatus row STAYS OPEN, STOPS GATING and STOPS BEING OWED — with a per-row lapse record naming the derivation that graded it, and no row lapses without one

> **★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE RECORD (user-ruled
> 2026-08-11; the ruling record is `cowork_rulings_2026_08_11_fifteenth_stop.md`, Ruling 66).**

**In plain words.** An open row of the open-items register whose subject is this project's own tracking or documentation apparatus stays open, blocks no stage, and is no longer work anybody owes — it stops drawing leftover capacity. Its status cell does not move, because a lapse is not a resolution. Each lapse is written down on the row itself, naming the derivation that graded it, so a later reader can see why the row stopped being owed and can re-open it by challenging that derivation rather than by rediscovering the issue; a row with no named grading does not lapse. An obligation to establish that something works is untouched and never lapses.

**Why.** Stated with the ruling. D-438 had already removed the blocking, so the reading that keeps the row owed and merely unblocked was declined as changing almost nothing — and *stays owed, worked in leftover capacity* is precisely the mechanism D-641's own recorded ground names as the cause of the backlog it describes (`OPEN_ITEMS.md` OI-337; no figure is restated here, D-431). Resolving the rows outright was argued as not a live option and was not taken, on four grounds: the register's rule (d) flips a row with provenance and there is none because nothing was done; #19 forbids converting *merely unfalsified* into *established*; #10 forbids the record stating something false about itself; and three separate derivations read the INDEX's status token, so a false resolution propagates mechanically. The costs are recorded as accepted rather than discharged: a residual #19 exposure mitigated only as well as the cut encodes the carve-out, a motion against #5 since this decides to stop investigating a population, and practical irreversibility, which the per-row lapse record is what softens. The token question the surface named as this reading's price was ESTABLISHED rather than assumed and turned out not to be a cost: rule (f) carries a row's open-or-resolved bit and nothing else — its vocabulary maps every canonical opening to exactly those two values, and the one index parser publishes exactly that one state field — so a lapsed row is still OPEN and *owed* is a derived field of the same cut that already derives gating, while a new token would put one state in two places (#6).

**Status.** LIVE · decided 2026-08-11 · ratified by user

**Home.** `CLAUDE.md:355-385`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-11, Ruling 66 of `cowork_rulings_2026_08_11_fifteenth_stop.md`, the second of the two rulings that record records. Applied by `cc_instruction_apply_the_bearing_cut.md` Task 1. Checked at the register data before the write — NO entry stated this rule, the dispatch's assumption A2 discharged at the objects: D-438 says an apparatus row gates nothing AND stays owed, which is the clause this supersedes; D-641 governs a FINDING at the moment of discovery and states in its own text that it ADDS to D-438 rather than amending it, and the ruling record says in terms that D-641 is not retired and continues to govern findings made while an item is worked. So this is a creation landing in the commit that records the ruling (rule (c)). ★ THE HOME WAS DERIVED AND VERIFIED, NOT ASSUMED, and the comparison is recorded because the dispatch named two candidates and required a STOP if they were equally supported. It is not a close call: this rule REPLACES two of the three clauses of a sentence that lives in `CLAUDE.md`'s open-items register section — *it stays open, it stays owed, and it is worked in leftover capacity* — so writing it anywhere else would leave that sentence stating something false (#10) and would put one concern in two places (#6). The dispatch-protocol block of `cowork_audit_protocol.md` was the other candidate and is not supported at all here: its own opening declares that the rules it holds govern every DISPATCH, and this governs what a REGISTER ROW is owed. THE FORMER WORDING IS PRESERVED IN PLACE (#12) rather than deleted — the superseded clause stands in the declaration above and this block names it and dates it. THE HOMING PROCEDURE (D-668) WAS RUN IN ITS FIXED ORDER: step 1 was tried FIRST and DECLINED, because the owning section states the OPPOSITE of the rule and a pointer move would have pointed at a contradiction; step 2 then applied, the section STATING RULES — it carries the register's lettered rules (a)–(f) — judged before the write. The edit surface is licensed by the 2026-08-07 ruling that widens a HOMING dispatch's surface to `CLAUDE.md` scoped to homing acts alone. THE GROUPING is group T beside D-438, whose declaration this amends. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the rule, and the entry text was written afterwards. Cross-ref D-438 (the declaration this amends, at the same home), D-675 (the sibling ruled in the same act — when phase 1 completes), D-641 (the neighbouring rule for a FINDING rather than for a standing row, untouched), D-662 (the canonical status token, which this deliberately does not extend), D-436 (the mechanism rule a change to the cut answers to), `OPEN_ITEMS.md` OI-337 (the six-wave backlog the ruling's ground names).

### D-677 — A DISCARD verdict on an already-rowed item is an INPUT to the derivation that decides gating, never an edit to a gating verdict — the row stays open, draws no capacity, and a record lacking finding, date or reason does not reach the cut

> **★ AND WHAT A DISCARD VERDICT DOES TO A ROW ALREADY ON THE BOOKS — IT IS AN INPUT TO THE
> DERIVATION THAT DECIDES GATING, NEVER AN EDIT TO A GATING VERDICT (user-ruled 2026-08-13; the
> ruling record is `cowork_rulings_2026_08_13_seventeenth_stop.md`, Ruling 69).**

**In plain words.** The worth test decides which findings are worth fixing, but the ruling that created it deliberately left open what happens to rows already on the books. This settles it: where an open row carries a DISCARD verdict, that verdict is fed to the computation that decides whether the row makes a stage wait — it is never used to edit a gating verdict by hand. The gate stays computed; what changes is what the computation reads. The row itself stays open and stops drawing capacity. Because a discard verdict is written by a person rather than computed, it only moves the gate when it carries the three things the worth test already demands of every discard: what was found, when, and why it was discarded; a record missing any of the three does not reach the computation at all. It is ruled for the whole class, not for the one row that raised it.

**Why.** Stated with the ruling, and forced by the first case of the shape: a row that was open, GATED and carried a discard verdict blocked phase 1 while the test said the work should never be done, so as it stood the row could never close. The route was chosen over a hand-made correction because D-436 reserves to the user the question of what a derived cut carries, and a hand-REMOVED gate is the same act as a hand-ADDED one, which the record forbids — the recorded lesson being `OPEN_ITEMS.md` OI-336. Three alternatives were declined with their principled costs: leaving the discard record standing beside the gate, declined on #10 because the record would then state two incompatible things about one row and on #4 because the row becomes a permanent block; withdrawing the discard and working the row, declined on #4 as capacity spent on free-text reason strings in an audit artifact and because it would empty the worth test of force on its second application; and ruling that the worth test reaches new findings only, declined as the first option restated as policy, since the gating population could then shrink only by being worked while containing rows nobody thinks worth working. Two costs are recorded as ACCEPTED rather than discharged: it extends the retroactivity disclaimer D-174's own ruling carries, which was written to prevent exactly a sweep; and it makes the gating population sensitive to an authored verdict, which the guard bounds but does not remove.

**Status.** LIVE · decided 2026-08-13 · ratified by user

**Home.** `CLAUDE.md:415-463`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** User ruling of 2026-08-13, Ruling 69 of `cowork_rulings_2026_08_13_seventeenth_stop.md`, taken on a surface carrying four mutually exclusive options with their principled costs and objective ratings. Applied by `cc_instruction_ruling69_discard_input.md` Task 1. Checked at the register data before the write — NO entry stated this rule: D-174 states the worth test and its consequence for a FINDING (no row, no gate, no capacity) and says in terms that what the test does to rows already on the books is a separate act; D-676 says an apparatus row stays open, stops gating and stops being owed, on a criterion that is not the worth test; D-436 forbids hand-adding a gating verdict but does not say what a discard does to one. So this is a creation landing in the commit that records the ruling (rule (c)). ★ THE HOME WAS DERIVED AND VERIFIED, NOT ASSUMED, and the comparison is recorded because the dispatch required a STOP if two candidates were equally supported. THE OPEN-ITEMS REGISTER SECTION OF `CLAUDE.md` IS THE HOME, and it is not a close call. The rule's subject is what a REGISTER ROW's gate is derived from: it is stated in the shape the lapse rule immediately above it uses, it turns the same three clauses of the non-gating declaration (stays open / stops gating / stops being owed), and both of those live in that section — so writing it elsewhere would put one concern in two places (#6). THE TWO OTHER CANDIDATES ARE NAMED AND NEITHER IS EQUALLY SUPPORTED. Principle #10 — D-174's home, where the worth test itself lives — is the nearer of the two and is still not it: #10 decides which FINDINGS are worth fixing and its own sentence already carries the consequence (no row, no gate, no capacity), while this rule decides how that consequence REACHES a row through a derivation over the register, which is the register section's subject and not the principle's; the ruling's own text says it is the separate act #10's ruling deferred, and a deferred act homed inside the clause that deferred it would read as though nothing had been deferred. The dispatch-protocol block of `cowork_audit_protocol.md` is not supported at all: its own opening declares that the rules it holds govern every DISPATCH, and this governs neither how a dispatch is written nor how an act inside one is performed. THE DELEGATION RULES (g)–(k) DO NOT ADMIT OR EXCLUDE THIS ENTRY, and that is stated rather than left silent: they decide which documents and sections are CONTRACT HOMES, and this entry's class is `process`, which criterion C1 declares correctly homed and not outstanding — the same class and the same home as D-675 and D-676, ruled two batches earlier. THE EDIT SURFACE IS LICENSED by the 2026-08-07 ruling that widens a HOMING dispatch's surface to `CLAUDE.md` scoped to homing acts alone, and this is one. THE GROUPING is group T (standing process rules) beside D-438, D-675 and D-676 — the declaration and the two rulings whose machinery this joins; the alternative was group S beside D-174, which shares the worth test but not the subject. THE ENTRY ITSELF CARRIES NO SEPARATE RATIFICATION EVENT (#14) — the user ruled the rule, and the entry text was written afterwards. ★ THE MECHANISM THE RULING NAMES IS BUILT IN THE NEXT COMMIT OF THE SAME BATCH (Task 2), which is where the derivation begins consuming discard verdicts; at THIS commit the rule is written and entered and nothing is consumed yet, and that is stated so a reader does not take the entry for the mechanism. Cross-ref D-174 (the worth test, whose deferred act this is), D-676 (the lapse rule whose shape it takes, at the same home), D-438 (the non-gating declaration whose three clauses it turns), D-675 (the bearing cut this input feeds), D-436 (a gating verdict comes from a cut and is never hand-added), D-431 (no derived identity or count is restated at the home), `OPEN_ITEMS.md` OI-336 (the recorded lesson of a hand-added gate verdict).

