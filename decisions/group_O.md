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

**Why.** Stated constraint, ARCHITECTURE.md:4675-4676 and :4781-4782: a fixed-pitch instrument cannot adjust, so it is the natural reference - and its presence resets accumulated drift at every chord it plays.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4688`

**Provenance.** ARCHITECTURE.md:4669-4689 (§11.2). No date or ratifier stated.

### D-145 — One preference chooses the tuning system, and no tuning code hardcodes one

> All tuning code paths read the preference at call time via `preferredTuningSystem()`
> (defined in `notationtuningbridge.cpp`), which resolves the key through
> `TuningRegistry::byKey()` with a `JustIntonation` fallback if the key is unset or
> unknown.  No tuning code hardcodes a specific system.

**In plain words.** Which tuning system is in force is a single user setting, read afresh each time any tuning happens. No part of the tuning code has a system built into it.

**Why.** Stated constraint, ARCHITECTURE.md:4691-4699 - #6, one path per concern: the same preference governs per-note tuning, chord-staff population and region tuning, so the three cannot silently disagree about what tuning the user asked for.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4704`

**Provenance.** ARCHITECTURE.md:4691-4707 (§11.2a). No date or ratifier stated.

### D-146 — A tie chain is one indivisible tuning event, and its tuning comes from one authority note

> **Tied notes:** A non-partial tie chain explicitly carries a compositional instruction of
> continuity. For region tuning, the entire non-partial tie chain is treated as one tuning
> event. The chain must not be split. Its tuning is set from a single authority note and
> protected thereafter; later harmonic regions tune around that established pitch.

**In plain words.** Notes joined by ties are one sustained sound, so they are tuned once and never split apart. The tuning is worked out from a single note in the chain - the one carrying a tuning anchor if there is one, otherwise the first - and applied unchanged to the whole chain.

**Why.** Stated constraint, ARCHITECTURE.md:4950-4951 and :4923-4924: a tie is a compositional instruction of continuity, so splitting it would contradict what the composer wrote; a user who wants the sustained sound retuned as the harmony moves writes a slur instead.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4950`

**Provenance.** ARCHITECTURE.md:4950-4963 (§11.3c), with the region-tuning consequence at :5726-5729 (§11.6). No date or ratifier stated.

### D-147 — A slur, not a tie, joins the halves of a split note

> A **slur** (not a tie) connects the two halves.  This is a deliberate choice:
> MuseScore's playback engine treats tied notes as one continuous sound with a single
> tuning value, so a tie would silently discard note_B's tuning.  A slur produces two
> independent playback events with legato articulation, allowing each half to carry
> its own tuning offset.

**In plain words.** When a sustained note must be retuned partway through, it is cut in two and the halves are joined with a slur rather than a tie.

**Why.** Stated constraint, ARCHITECTURE.md:5390-5393: MuseScore's playback treats tied notes as one continuous sound with a single tuning value, so a tie would silently discard the second half's tuning; a slur produces two independent playback events, each able to carry its own offset.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5389`

**Provenance.** ARCHITECTURE.md:5382-5393 (§11.4). No date or ratifier stated.

### D-148 — The split is visible in the score; the invisible alternative is deferred

> The split is **visible** — the score shows two shorter notes connected by a slur.
> This is the simplest correct approach and is fully undoable via MuseScore's standard
> undo system.

**In plain words.** The reader sees two shorter notes joined by a slur where a note was retuned. The alternative - keeping the written note and hiding a silent playing copy - was designed and set aside.

**Why.** Stated constraint, ARCHITECTURE.md:5396-5397: the visible split is the simplest correct approach and is fully undoable through MuseScore's own undo. The excluded alternative's recorded blocker (:5360-5363) is that it needs a visual indicator for tuning-applied notes before it is practical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5395`

**Provenance.** ARCHITECTURE.md:5395-5402 (§11.4), with the deferred alternative recorded at `backlog_invisible_split.md`. No date or ratifier stated.

### D-149 — Only visible, sounding notes enter the pitch-class collection

> Chord analysis filters notes with `visible = true` and `play = true`, excluding
> both silent notes and any future invisible tuning artifacts from the pitch-class
> collection.

**In plain words.** Notes marked invisible, and notes that do not play, take no part in identifying the chord - which also keeps any hidden note created by the tuning machinery out of the analysis.

**Why.** Stated constraint, ARCHITECTURE.md:5420-5421: the filter excludes both silent notes and any future invisible tuning artifact, so tuning a passage cannot change what the analysis of that passage sees.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5419`

**Provenance.** ARCHITECTURE.md:5417-5421 (§11.4). No date or ratifier stated. The joint estimator's own eligibility flags are the Layer-1 fact surface (D-039/D-045).

### D-150 — The chord staff is the output, never an input to the analysis that fills it

> The target staff is excluded from the analysis input — it is the output, not a
> source.  This prevents feedback loops when re-running the analysis.

**In plain words.** When the harmonic reduction is written onto a staff, that staff's own contents are kept out of the analysis that produced them.

**Why.** Stated constraint, ARCHITECTURE.md:5477: it prevents a feedback loop when the analysis is re-run over music that already carries its own reduction. The joint estimator's record path realizes the same rule at its own input surface - D-013, open_items/OI-204.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5476`

**Provenance.** ARCHITECTURE.md:5467-5477 (§11.5). No date or ratifier stated.

### D-151 — Populating the chord staff overwrites whatever is in the selected range

> **Any existing content in the selected region is overwritten.**  Re-analysis after
> score edits simply selects the same range and runs again.  If the user wants to
> preserve a previous analysis, they can undo or copy it elsewhere first.

**In plain words.** Running the reduction again over the same passage replaces what is there. Keeping an earlier analysis is the user's job - undo it, or copy it somewhere else first.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5479`

**Provenance.** ARCHITECTURE.md:5479-5481 (§11.5). No date or ratifier stated.

### D-152 — Roman numerals and Nashville numbers are never shown together on one staff

> **Chord function notation** attached below the treble staff — either
> `HarmonyType::ROMAN` (Roman numerals) or `HarmonyType::NASHVILLE` (Nashville
> numbers), selected by the "Chord function notation" preference (None / Roman
> numerals / Nashville numbers).  Roman and Nashville are mutually exclusive on
> the staff because they encode identical information; displaying both would be
> redundant and legibility-destroying.

**In plain words.** The chord staff shows one or the other beneath the music, chosen by preference, never both.

**Why.** Stated constraint, ARCHITECTURE.md:5544-5546: the two notations encode identical information, so showing both would be redundant and would destroy legibility.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5541`

**Provenance.** ARCHITECTURE.md:5541-5546 (§11.5); the same choice on the analysis side is D-086. No date or ratifier stated.

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

**Why.** Stated constraint, ARCHITECTURE.md:5733-5739: the interactive output is meant to be publication-ready and indistinguishable from hand-entered symbols, while the red is a filter criterion that lets the automated review separate our inferred annotations from whatever the score already contained.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5732`

**Provenance.** ARCHITECTURE.md:5730-5739 (§11.5). No date or ratifier stated.

