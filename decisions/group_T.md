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

**Home.** `CLAUDE.md:910`  — a decision about how the work is done, not about the system; this is its correct home.

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

**Provenance.** CLAUDE.md:728-734, user-directed 2026-06-15. ★ READ WITH the general contribution intent at ARCHITECTURE.md:373-375 - two recorded positions, a general intent to contribute and a named one-patch exception; the record does not state how the general intent applies to the rest of the tree.

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

