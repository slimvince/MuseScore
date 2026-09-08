# The Cowork memory file's outgoing content, preserved at an object (2026-09-07)

> **What this is.** On 2026-09-07 the user asked that his Claude Cowork memory be tidied, observing
> that it overlapped this repository's governing documents and was out of date. His scope ruling the
> same day, verbatim: *"I can accept that working with our extension of Musescore Studio can only be
> done while sitting at my computer."* That settled the one open question — a session with no access
> to `C:\s\MS` does not need project content — so the memory file `/areas/musescore-arranger.md` was
> cut back to pointers.
>
> **Why this file exists.** #12. The cut removed lines whose recoverability from this repository was
> NOT checked line by line, so they are preserved here verbatim rather than asserted to be safe
> elsewhere. **This file is a preservation record, not a governing surface.** Nothing in it binds
> anything, and three of its lines are recorded false at the head of this file.
>
> **The memory store is OUTSIDE this repository.** It is a small per-user store that follows the user
> across Claude surfaces. It is not a tracking surface of this project and no rule of this project
> governs it.

## The three lines established FALSE before the cut, each at an object

1. *"Identified a MuseScore core bug in `chordlist.cpp:993` (sussus double-fire) that should be
   reported upstream"* — **false at HEAD.** `CLAUDE.md`'s local-patches section records that fix as
   MADE and live in the fork, with a user-ratified UPSTREAMABLE distribution disposition
   (register entries **D-315**, **D-316**).
2. *"Vincent boots each Cowork session on this project with 'mount C:\s\MS and read
   cowork_handoff.md'"* — **superseded twice**: by the single-named-entry-file pattern, and again on
   2026-09-07 by the ruled six-span membership. The same memory file separately carried the
   2026-08-28 pattern, so it contradicted itself in place.
3. The transcribed accuracy figures — *"Corpus scores at session end: Corelli 70.9%, Bach chorales
   75.2%, Beethoven 65.2%"* and *"corpus 64.6% weighted DCML"* — carried **no date and no source**
   and are not the ratified baselines, which live in `CLAUDE.md`'s gate-policy block. A transcribed
   figure is the shape **D-431** forbids, and these sat in a store a session may read before it reads
   `STATUS.md`.

## The outgoing content, verbatim as it stood before the cut

```
- [stated] Harmonic analysis and arranging assistance module being built into MuseScore Studio's C++ core, intended as an official GPL v3 contribution
- [stated] Built on Windows with MSVC 2022; Claude Code is the implementation assistant, Claude.ai chat for planning

Recent work (Sessions 25-27+):
- [stated] Implemented look-ahead note exclusion from chord inference (commit `3f186d38ea`), resolving a key misidentification case
- [stated] Jazz-path retirement eliminated chord symbol reads from the analysis pipeline (commit `02e3733afb`)
- [stated] Deduplication campaign brought notation tests to 57/57
- [stated] Built an llm-triage system: multi-tier harmonic analysis pipeline with OpenAI, Claude, and Gemini tiers
- [stated] Confirmed MuseScore 4.6.5 headless plugin execution is non-functional on Windows (`-p` flag removed, `-j` job file silently ignores plugin key); drafted a C++ reimplementation (`batch_analyze_plugin_impl.cpp`)
- [stated] Corpus scores at session end: Corelli 70.9%, Bach chorales 75.2%, Beethoven 65.2%

Architecture & decisions (Phases 1-4, Sessions ~1-24):
- [stated] Completed Phases 1-4: selection-range annotation wired to Tools menu, inferrer stabilization (corpus 64.6% weighted DCML), submission branch `submission-phase1` created, GPL headers/doxygen/translations/CMake cleaned
- [stated] Submission scope is analysis engine + annotation interface only (implode and tuning removed)
- [stated] All annotation paths use identical analysis via `prepareUserFacingHarmonicRegions`
- [stated] Over-segmentation is preferred over under-segmentation
- [stated] Rules established: shell discipline (no background build jobs), characterization testing for integration tests, `chords_std.xml` is authoritative (`chords.xml` deprecated/buggy), commit before session end
- [stated] Identified a MuseScore core bug in `chordlist.cpp:993` (sussus double-fire) that should be reported upstream
- [stated] GPT-4.1 was tried and found unreliable; CC remains preferred

Related notation task:
- [stated] Fitted Spanish tango lyrics from Eladia Blazquez's "Para llevarme a algun pais" (Piazzolla's "Invierno Porteno") onto a melody excerpt via a Python script using direct MusicXML string manipulation (preferred over music21 round-tripping to preserve articulations); handled synaloepha, melismas, and rhythm changes

Cowork session protocol (2026-08):
- [stated] Vincent boots each Cowork session on this project with "mount C:\s\MS and read cowork_handoff.md" - the handoff's TOP entry block is the authoritative boot; older blocks are superseded as entry points but remain binding where they say so
- [stated] Roles: CC (Claude Code) executes dispatches; the Cowork session is the writing side - it verifies every CC report at the git objects by explicit hash before trusting it, reads CC's FULL close in cowork_away_returns.md (never a summary) and proves the reading by quotation; shell use on the repository is for git object queries only, file reads via file tools (their D-253 rule)
- [stated] Decision surfaces: full visible prose with alternatives, costs named to principles, and a recommendation; no option widgets; self-contained - re-explain every identifier from scratch, never assume he remembers class numbers, open-item numbers or section marks
- [stated] Repository at `C:\s\MS`; GitHub at `https://github.com/slimvince/MuseScore`
- [stated] Sessions 25-27 fixed Sus4 penalty, root-only gap carry, declared-mode override, Pass 2b iterative splitting, D#->Eb normalization, and REST inference; look-ahead note exclusion threshold is 3+ sounding pitch classes -> exclude look-ahead, sparse texture -> include for disambiguation
- [stated] All Session 26 fixes were cherry-picked to `submission-phase1`
- [stated] llm-triage pipeline tiers: Tier 1 batch_analyze, Tiers 2-4 OpenAI/Claude/Gemini, Tier 5 planned C++ reimplementation
- [stated] Rationale for over-segmentation: users can delete unwanted symbols but cannot recover missing ones
- [stated] Standing cadence (2026-08-21): one Cowork session per dispatch cycle - (a) consider what CC just reported, (b) write the next CC dispatch (every dispatch runs in a new CC session), (c) update everything needed for a handover while CC works, (d) CC finishes while Vincent and a fresh Cowork session go back to (a); a short Cowork session is the cadence working, not a defect
- [stated] 2026-08-22 direction: the governing files (CLAUDE.md, DECISIONS.md, cowork_handoff.md etc.) are to be pruned further and split into satellite files read only when needed - satellites by reason (historical archeology, gritty details, the "why" separated from the "what/how") and task-specific CLAUDE.md satellites by session kind (thinking, exploring, instructing, writing, coding); observed that pruning so far has not shrunk a session's boot context in practice and that the language may be too verbose
- [stated] 2026-08-22 standing conditions on the specification reconstruction: before any specification is "done", all existing knowledge must be scoured for good and bad things so no previously thought-of good idea is lost; before the audit of specifications against code, the specifications must be as correct and complete as possible; blind spots (no empirical findings ledger) are acceptable for the pilot only; the blind deriving session is a fresh Cowork session (ruled B)
- [stated] 2026-08-26: role boundary, corrected explicitly - the Cowork writing side does NOT hand a dispatch to CC. It writes the dispatch to disk in the repo; Vincent is the one who opens it with Claude Code. Do not offer to "hand it to CC" or to start it.
- [stated] 2026-08-26: treat Claude Code's reports as possibly hallucinated or assuming things, and remember CC has no grasp of the greater context - read every CC report in FULL (never a summary) and verify its claims at the objects. Also: no bash/shell for reading local repository files; use the file tools.
- [stated] 2026-08-27: he is assembling, with another LLM elsewhere, a comprehensive list of public research, algorithms and software on the subject, to be used at the stage where the specifications are bettered against it
- [stated] 2026-08-28: that external research list was DELIVERED - `C:\s\MS\external resarch summary\external research.xlsx` (folder name carries his spelling as-is), a 21-sheet workbook built with another LLM; ruled ours to git-handle and record; its ruled use is the framework ratification sitting (SS1.4's hold)
- [stated] 2026-08-27: the specifications are NEVER barred from ideas originating in code - quite the opposite. The plan's "NOT ALLOWED" clauses are PHASE-SCOPED, not standing bars: no implementation-derived material as design input during the FRAMEWORK phase; no specification amended to match the implementation during the AUDIT (that clause names one defect, the false-clean result). His sequence: v1 of specs (blind, to the best of our capabilities) -> audit -> amend specs with good things found in code -> fix code. Once v1 is sealed, all good ideas are evaluated on merit regardless of source
- [stated] 2026-08-27: reaching v1 of the specs is the goal - he is NOT advocating coding as soon as possible; the meta-level work is what has prevented reaching v1
- [stated] 2026-08-28 standing bar, binding Cowork and CC equally: "we are not to simply act on latest impulse - always have the progress of plan in focus" - before acting, state where the plan stands and what the act does for it
- [stated] 2026-08-28 boot pattern: session opened with one named handoff entry file (e.g. cowork_handoff_entry_eighty.md) plus the ordinary session-start read (CLAUDE.md, DECISIONS.md, STATUS.md, the derived gating answer); skipping the ordinary read when given a single named file is recorded in the handoff as an error cause
- [stated] 2026-08-29 ratification sitting (four rulings, record `cowork_rulings_2026_08_29_ratification_sitting.md`): SS9.0 had been ruled 2026-08-28 (a unit is a DECISION the analysis makes about the music); D2 ruled - a deciding layer owns the ANSWER to its question (split form; fact layers unchanged); the framework decomposition is RATIFIED (external list dispositioned, no falsifier; D3 segmentation-rivals and D5 merge-equal-retired released and ruled); the DP-D rival admitted as detail-phase input only; the mode question routed (L2 detail spec / measurement design / style system). The SS3.9 retrospective was then written and RATIFIED the same day (Ruling 5; six proposals P-1..P-6 to move to their homes by later executing acts) - the framework phase is CLOSED; the ruled rename of the framework document rides the closing dispatch (target name his one word); the detail-specification phase is next; placement test retained as post-ratification check with its shell-condition and worth questions still open
- [stated] 2026-08-30: the phase-close batch (second writing) ran clean and was verified - FRAMEWORK.md renamed/stamped and pushed, sitting record + disposition surface + retrospective landed, six proposals homed, entry eighty-one prepended; end state 8 failing = 3 known + 5 stop-reported ordered-edit reds. User-owed from it: a second signature-table change (FRAMEWORK.md currently classed as a stray working file), the retirement-caller-check KeyError mechanism question, the D-196 line-drift repair (reaim_home_anchors.py needs an order), enrolling the four new protocol clauses in the marker population, and opening the detail-specification phase (his sitting); the fifty-ninth session closed on `cowork_handoff_entry_eighty_two.md` (untracked, at the repo root) - the next session's boot authority; nothing in flight
- [stated] 2026-08-30 (sixtieth session): ruled "Agree with A" - the detail-specification phase is OPENED on SS3.4's ruled terms; sitting record `cowork_rulings_2026_08_30_detail_phase_opening_sitting.md` at the repo root (untracked, lands at a later dispatch's Task 0)
- [stated] 2026-08-30 Ruling 2 ("that is the reasonable scope. If necessary we should let a fresh LLM session do it"): a primary-source reading pass is the phase's FIRST act, before any derivation - unread populations whole, full-read upgrades follow candidacy not novelty, load-bearing framework figures verified at primaries, coupling facts extracted, findings per design point and per interface (chains), plus a whole-architecture coherence review at set ratification; commission written to `cowork_reading_pass_commission_2026_08_30.md`; the first-deriving-subject decision deferred until the findings surface is ruled
- [stated] 2026-08-31 Ruling 3 ("do the narrower and mostly forward looking things. Also, we need (CC?) to git commit at a proper point in time"): after the other cowork line finished the reading pass across several sessions, no general QA re-run ordered; instead the at-the-object re-reads of the six relayed central rows and the never-exercised candidacy-upgrade derivation, commissioned at `cowork_reading_pass_remedial_commission_2026_08_31.md`; and the landing dispatch `cc_instruction_reading_pass_landing_2026_08_31.md` (two ruled FRAMEWORK.md corrections, track the untracked population, prepend four staged handoff entries). Session closed on `cowork_handoff_entry_eighty_five.md`
- [stated] 2026-08-31 Ruling 4 ("ok, A"): the landing batch's first writing stopped at Task 0 (a ninth guard red, cause established: `gen_evidence_pin_membership.py` scans the live repo root and is not epoch-pinned, so untracked ruling records make it stale) and wrote nothing; ruled not news. Also established: the ratified handoff-splice construction does not exist as a committed tool, so the prepend is dropped and the four staged entries land as files. Fetched-content records tracked, the one paper PDF excluded with the ignore rule extended to reach subfolders. Second writing: `cc_instruction_reading_pass_landing_second_2026_08_31.md`
- [stated] 2026-08-30 principles he stated: "We should act knowledge-based" - held-but-unread research breaks #1; and the architecture is evaluated as a WHOLE against the ultimate objective, never as pieces - coupled algorithm choices mean a locally worse choice can enable a better chain
- [stated] 2026-08-30: context compaction mid-session loses knowledge - "this is one thing we must try to avoid". Constant working practice: minimize exposure to LLM context limits (short sessions per the cadence, everything on disk, wind down at a natural boundary before context runs out rather than being compacted mid-task)
- [stated] 2026-09-07: the mandatory session-start read is itself the context problem - asked what can be done to CLAUDE.md, DECISIONS.md and STATUS.md to lessen the tokens needed to understand what is in them; ordered them read with the file tools, not bash, because of staleness risk, and barred any file writing in that session
```

## What replaced it

Seven pointer lines: what the module is and its GPL v3 intent; the repository path and the GitHub
location; a standing rule that the file carries pointers only and must never become a second copy of
the record; where the record is, naming the four governing documents and what each holds; that the
boot authority is whichever handoff entry the user names, with an instruction NOT to record a boot
pattern there because the one kept there went stale twice; the role boundary; and a pointer to the
2026-08-22 satellites direction naming where in this repository it lives.

Two further memory acts the same day: `/profile.md` had one stale line corrected (Claude Code
implements, a Cowork session is the writing and planning side); and one working preference was moved
rather than dropped into `/topics/music.md` — that for fitting lyrics to a melody the user prefers
direct MusicXML manipulation over round-tripping through music21, because the round trip loses
articulations. `/preferences.md` was left untouched.

*Provenance: Cowork, 2026-09-07, the sitting recorded at
`cowork_handoff_entry_one_hundred_and_forty_seven.md`. The outgoing text above is reproduced from the
memory file as read at the start of that sitting, before any write. Non-ASCII characters in the
original (curly quotes, section marks, en dashes, Greek deltas) are transliterated here; no line is
otherwise altered, and nothing is added.*
