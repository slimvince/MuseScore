# Decisions group O — Intonation

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-144 — Percussion is excluded from analysis and tuning; fixed-pitch instruments are the tuning anchor

> Percussion instruments are excluded from both harmonic analysis and intonation.
> Fixed-pitch instruments (piano) serve as intonation anchors when present.

**In plain words.** Unpitched percussion takes no part in working out the harmony and receives no tuning adjustment. Where a piano or organ is playing, the other instruments tune to it.

**Why.** Stated constraint, ARCHITECTURE.md:4976-4977 and :4781-4782: a fixed-pitch instrument cannot adjust, so it is the natural reference - and its presence resets accumulated drift at every chord it plays.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6101`

**Provenance.** ARCHITECTURE.md:4970-4990 (§11.2). No date or ratifier stated.

### D-145 — One preference chooses the tuning system, and no tuning code hardcodes one

> All tuning code paths read the preference at call time via `preferredTuningSystem()`
> (defined in `notationtuningbridge.cpp`), which resolves the key through
> `TuningRegistry::byKey()` with a `JustIntonation` fallback if the key is unset or
> unknown.  No tuning code hardcodes a specific system.

**In plain words.** Which tuning system is in force is a single user setting, read afresh each time any tuning happens. No part of the tuning code has a system built into it.

**Why.** Stated constraint, ARCHITECTURE.md:4992-5000 - #6, one path per concern: the same preference governs per-note tuning, chord-staff population and region tuning, so the three cannot silently disagree about what tuning the user asked for.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6117`

**Provenance.** ARCHITECTURE.md:4992-5008 (§11.2a). No date or ratifier stated.

### D-146 — A tie chain is one indivisible tuning event, and its tuning comes from one authority note

> **Tied notes:** A non-partial tie chain explicitly carries a compositional instruction of
> continuity. For region tuning, the entire non-partial tie chain is treated as one tuning
> event. The chain must not be split. Its tuning is set from a single authority note and
> protected thereafter; later harmonic regions tune around that established pitch.

**In plain words.** Notes joined by ties are one sustained sound, so they are tuned once and never split apart. The tuning is worked out from a single note in the chain - the one carrying a tuning anchor if there is one, otherwise the first - and applied unchanged to the whole chain.

**Why.** Stated constraint, ARCHITECTURE.md:5251-5252 and :4923-4924: a tie is a compositional instruction of continuity, so splitting it would contradict what the composer wrote; a user who wants the sustained sound retuned as the harmony moves writes a slur instead.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6363`

**Provenance.** ARCHITECTURE.md:5251-5264 (§11.3c), with the region-tuning consequence at :5726-5729 (§11.6). No date or ratifier stated.

### D-147 — A slur, not a tie, joins the halves of a split note

> A **slur** (not a tie) connects the two halves.  This is a deliberate choice:
> MuseScore's playback engine treats tied notes as one continuous sound with a single
> tuning value, so a tie would silently discard note_B's tuning.  A slur produces two
> independent playback events with legato articulation, allowing each half to carry
> its own tuning offset.

**In plain words.** When a sustained note must be retuned partway through, it is cut in two and the halves are joined with a slur rather than a tie.

**Why.** Stated constraint, ARCHITECTURE.md:5691-5694: MuseScore's playback treats tied notes as one continuous sound with a single tuning value, so a tie would silently discard the second half's tuning; a slur produces two independent playback events, each able to carry its own offset.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6802`

**Provenance.** ARCHITECTURE.md:5683-5694 (§11.4). No date or ratifier stated.

### D-148 — The split is visible in the score; the invisible alternative is deferred

> The split is **visible** — the score shows two shorter notes connected by a slur.
> This is the simplest correct approach and is fully undoable via MuseScore's standard
> undo system.

**In plain words.** The reader sees two shorter notes joined by a slur where a note was retuned. The alternative - keeping the written note and hiding a silent playing copy - was designed and set aside.

**Why.** Stated constraint, ARCHITECTURE.md:5697-5698: the visible split is the simplest correct approach and is fully undoable through MuseScore's own undo. The excluded alternative's recorded blocker (:5360-5363) is that it needs a visual indicator for tuning-applied notes before it is practical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6808`

**Provenance.** ARCHITECTURE.md:5696-5703 (§11.4), with the deferred alternative recorded at `backlog_invisible_split.md`. No date or ratifier stated.

### D-149 — Only visible, sounding notes enter the pitch-class collection

> Chord analysis filters notes with `visible = true` and `play = true`, excluding
> both silent notes and any future invisible tuning artifacts from the pitch-class
> collection.

**In plain words.** Notes marked invisible, and notes that do not play, take no part in identifying the chord - which also keeps any hidden note created by the tuning machinery out of the analysis.

**Why.** Stated constraint, ARCHITECTURE.md:5721-5722: the filter excludes both silent notes and any future invisible tuning artifact, so tuning a passage cannot change what the analysis of that passage sees.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6832`

**Provenance.** ARCHITECTURE.md:5718-5722 (§11.4). No date or ratifier stated. The joint estimator's own eligibility flags are the Layer-1 fact surface (D-039/D-045).

### D-150 — The chord staff is the output, never an input to the analysis that fills it

> The target staff is excluded from the analysis input — it is the output, not a
> source.  This prevents feedback loops when re-running the analysis.

**In plain words.** When the harmonic reduction is written onto a staff, that staff's own contents are kept out of the analysis that produced them.

**Why.** Stated constraint, ARCHITECTURE.md:5787: it prevents a feedback loop when the analysis is re-run over music that already carries its own reduction. The joint estimator's record path realizes the same rule at its own input surface - D-013, open_items/OI-204.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6906`

**Provenance.** ARCHITECTURE.md:5777-5787 (§11.5). No date or ratifier stated.

### D-151 — Populating the chord staff overwrites whatever is in the selected range

> **Any existing content in the selected region is overwritten.**  Re-analysis after
> score edits simply selects the same range and runs again.  If the user wants to
> preserve a previous analysis, they can undo or copy it elsewhere first.

**In plain words.** Running the reduction again over the same passage replaces what is there. Keeping an earlier analysis is the user's job - undo it, or copy it somewhere else first.

**Why.** SEARCHED 2026-08-09 (CC, `cc_instruction_return_continuation_3.md` Task 2). The home states a RECOURSE and a WORKFLOW rather than a derivation, and both are in the decision's own words: re-analysis after score edits "simply selects the same range and runs again", and a user who wants to keep an earlier analysis "can undo or copy it elsewhere first". So what defends the overwrite is that it costs the user nothing they cannot recover, and that it keeps re-running trivial — a ground, but not a comparison against any alternative (merging, appending, or refusing to overwrite are not weighed). NOTHING IS BORROWED FROM THE SENTENCE IMMEDIATELY ABOVE, which is a reason for a DIFFERENT rule — the target staff is excluded from the analysis input because that "prevents feedback loops when re-running the analysis".

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6909`

**Provenance.** ARCHITECTURE.md:5789-5791 (§11.5). No date or ratifier stated.

### D-152 — Roman numerals and Nashville numbers are never shown together on one staff

> **Chord function notation** attached below the treble staff — either
> `HarmonyType::ROMAN` (Roman numerals) or `HarmonyType::NASHVILLE` (Nashville
> numbers), selected by the "Chord function notation" preference (None / Roman
> numerals / Nashville numbers).  Roman and Nashville are mutually exclusive on
> the staff because they encode identical information; displaying both would be
> redundant and legibility-destroying.

**In plain words.** The chord staff shows one or the other beneath the music, chosen by preference, never both.

**Why.** Stated constraint, ARCHITECTURE.md:5854-5856: the two notations encode identical information, so showing both would be redundant and would destroy legibility.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6971`

**Provenance.** ARCHITECTURE.md:5851-5856 (§11.5); the same choice on the analysis side is D-086. No date or ratifier stated.

### D-153 — Interactive annotations are written in the score's normal colour; the batch pipeline writes red

> Interactive annotate path (human use): annotations written in score default
> color (black). Publication-ready, indistinguishable from manually entered
> symbols. No user preference exposed.
>
> Automated pipeline (`batch_analyze` headless): annotations written in red,
> hardcoded in `tools/batch_analyze.cpp`. Never exposed to human user. Used by
> `auto_review.py` to filter our inferred annotations from pre-existing score
> content by color comparison.

**In plain words.** When a person runs the annotation, what it writes looks like anything else they typed. When the headless batch tool runs it, everything it writes is red.

**Why.** Stated constraint, ARCHITECTURE.md:6043-6049: the interactive output is meant to be publication-ready and indistinguishable from hand-entered symbols, while the red is a filter criterion that lets the automated review separate our inferred annotations from whatever the score already contained.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:7162`

**Provenance.** ARCHITECTURE.md:6040-6049 (§11.5). No date or ratifier stated.

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6192-6201`

**Provenance.** ARCHITECTURE.md:5088-5089 states it is not a current implementation target; the same deferral is recorded in the retired-session record at STATUS_ARCHIVE.md:2335 ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

### D-245 — Voice role comes from staff position or explicit assignment; automatic melody detection is deferred

> Automatic melody detection is deferred. For now, voice role is determined by staff position
> or explicit user assignment — not automatic detection. Per-staff override of voice role is
> a future extension.

**In plain words.** Which voice counts as the melody is taken from where it sits in the score or from what the user says. Working it out automatically is left for later, as is a per-staff override.

**Why.** Derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6315-6317`

**Provenance.** ARCHITECTURE.md:5203-5205 states the deferral ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

### D-246 — Fixed-pitch instruments are deferred, and will never receive tuning offsets

> Fixed-pitch instruments (piano, organ, fretted guitar) are deferred — their handling is not
> yet implemented. When implemented, they will serve as absolute anchors that other
> instruments tune to, and will never receive tuning offsets themselves.

**In plain words.** Piano, organ and fretted guitar are not handled yet. When they are, they will be the fixed reference other instruments tune to, and will not be retuned themselves.

**Why.** The constraint is the instruments themselves: their pitch is fixed by construction, so a tuning offset cannot be applied to them (ARCHITECTURE.md:5304-5306).

**Status.** DEFERRED · date not stated · ratifier not stated

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6416-6418`

**Provenance.** ARCHITECTURE.md:5304-5306 states both the deferral and the eventual behaviour ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

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

**Entry ratified.** 2026-08-02 · by user

**Home.** `ARCHITECTURE.md:6434-6446`

**Provenance.** ARCHITECTURE.md:5322-5334; the FreeDrift behaviour is restated at :5448-5453 ★ RATIFIED-FOR-NOW (user, 2026-08-02): to be REVIEWED when the intonation feature's implementation is revisited (the OI-62 held feature).

### D-366 — Recorded-performance intonation material is OUT of corpus scope — the intonation features are validated by theory and by listening

> | N15 | performed-intonation reference material | T-21/T-24 | **★ SCOPE RULING RATIFIED (user, 2026-07-04):** audio-domain, out of corpus scope; T-21/T-24 validate by theory/listening |

**In plain words.** Reference material for how performers actually tune is audio, not notation, and is ruled outside what the corpus collection covers. The two intonation features that would have consumed it are validated instead against tuning theory and by ear.

**Why.** derivation not recorded — the record states the ruling and its consequence but gives no reason beyond the material being audio-domain.

**Status.** LIVE · decided 2026-07-04 · ratified by the user

**Entry ratified.** 2026-08-02 · by user

**Home.** `cowork_score_census.md:221`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8c** — `## 8c. The FULL-NEEDS AUDIT — the union-of-needs mechanism (user question, 2026-07-03)` (heading at line 187). A delegation at ARCHITECTURE.md:349 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Its class before the phase-1n staged application was `gap`.

**Provenance.** Found by the phase-1h continuation wave, 2026-08-02, reading `cowork_score_census.md` IN FULL. The cell records `★ SCOPE RULING RATIFIED (user, 2026-07-04)`. NOT RATIFIED as a register entry — entered with the record's own status and put to the user in the phase-1h ratification queue. ★ RATIFIED (user, 2026-08-02, the phase-1h queue).

