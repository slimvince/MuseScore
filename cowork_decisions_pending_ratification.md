# The 113 decisions pending ratification — complete entries — ★ RATIFIED BY THE USER 2026-08-02

> **GENERATED REVIEW AID (Cowork, 2026-08-02; regenerate with the one-off in the session record).**
> Exactly the entries added by the completion pass (D-116 and above), rendered CHARACTER-IDENTICAL
> to the register's group files by the register generator's own entry renderer — verbatim quote,
> plain restatement, Why, status, home, provenance. The how-to-read guide and the terms table are
> in `DECISIONS.md`. The 115 entries you already reviewed are NOT here; their post-review changes
> are summarized in `cowork_decisions_ratification_delta.md` Part A.


## Group L — Licensing, contribution, and coding standards

### D-116 — The system is a module inside MuseScore Studio, not a plugin

> This system is implemented as a new module (`composing`) within MuseScore Studio's
> existing C++ codebase. It is not a plugin. It integrates directly with MuseScore's
> score model, rendering pipeline, playback engine, and UI infrastructure.

**In plain words.** The harmonic analysis is built into MuseScore Studio's own program code as a new component of it, not added on afterwards as a plugin. It uses MuseScore's own score model, engraving, playback and interface directly.

**Why.** Stated constraint, ARCHITECTURE.md:370-374: the analysis library itself has NO engraving dependency and is pure music theory; the bridge layer is what touches the engraving model. Being a module rather than a plugin is what lets that bridge exist at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:324`

**Provenance.** ARCHITECTURE.md:322-326 (§1.2). No date or ratifier stated.

### D-117 — The long-term intent is an official contribution to MuseScore Studio

> The long-term intent is for this to become an official contribution to MuseScore Studio.
> All code follows MuseScore's coding standards, licensing requirements, and contribution
> guidelines.

**In plain words.** The aim is for this work eventually to become part of MuseScore Studio proper, so it is written to MuseScore's own coding, licensing and contribution rules from the start.

**Why.** Derivation not recorded for the intent itself. What the record does state is the consequence it carries (ARCHITECTURE.md:329-330): following MuseScore's standards from the start is what keeps the contribution possible.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:328`

**Provenance.** ARCHITECTURE.md:328-330 (§1.2); restated at ARCHITECTURE.md:6415-6417 (the composing module is 'intended as a future contribution'). ★ READ WITH the CLAUDE.md DISTRIBUTION CONSTRAINT (D-197): the MusicXML declared-mode import patch cfc7eb5e39 is FORK-LOCAL ONLY and must NEVER reach musescore/MuseScore. Two recorded positions - a general intent and a one-patch exception - and the record does not state how the general intent applies to the rest of the tree.

### D-118 — GPL v3, and every external library must be GPL v3 compatible

> All code is licensed under **GPL v3** — consistent with MuseScore Studio's open source
> license. All external libraries used must be GPL v3 compatible.

**In plain words.** All the code is released under the GPL v3 licence, the same licence MuseScore Studio uses, and no outside library may be used unless its licence is compatible with that.

**Why.** Stated constraint, ARCHITECTURE.md:334-335: consistency with MuseScore Studio's own open source licence. A GPL-incompatible library would make the code undistributable with MuseScore.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:334`

**Provenance.** ARCHITECTURE.md:332-335 (§1.3). No date or ratifier stated. The per-file consequence is ARCHITECTURE.md:6248 - a GPL v3 header on every file.

### D-119 — The MuseScore contributor licence agreement is signed before any pull request

> The Contributor License Agreement (CLA) with MuseScore must be signed before any
> pull requests are submitted.

**In plain words.** Before any of this work is offered back to MuseScore as a pull request, the contributor agreement with MuseScore must be signed.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:337`

**Provenance.** ARCHITECTURE.md:337-338 (§1.3), restated at ARCHITECTURE.md:6344-6346 (§18.3). No date or ratifier stated.

### D-120 — MuseScore's coding style is followed, with clang-format run before every commit

> Follow MuseScore's existing coding style throughout:
> - Formatting defined in `.clang-format` — run clang-format before every commit
> - Naming conventions — consistent with existing MuseScore code
> - File headers — GPL v3 license header on every file (see existing files for template)
> - Include ordering — follow MuseScore's convention

**In plain words.** The code looks like MuseScore's own code: the formatter configuration in the repository is run before every commit, names follow MuseScore's conventions, every file carries the GPL v3 header, and includes are ordered MuseScore's way.

**Why.** Stated constraint, ARCHITECTURE.md:467-471 (§2.8): read how MuseScore already does a thing and follow the same pattern rather than inventing parallel infrastructure - the same reason that governs panels, score traversal, playback, settings and localization.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6245`

**Provenance.** ARCHITECTURE.md:6243-6249 (§17.1). No date or ratifier stated.

### D-121 — Where MuseScore's documentation practice is minimal, the higher standard applies

> Where MuseScore's documentation practice is minimal, use good practice instead.

**In plain words.** Following MuseScore's conventions does not mean copying how little it documents. Where MuseScore documents sparsely, this project documents properly instead.

**Why.** Stated constraint, ARCHITECTURE.md:6303-6306 (§17.3): the analyzers are the most complex components in the codebase, and a musician with reasonable theoretical knowledge must be able to read them and understand why each decision was made.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6251`

**Provenance.** ARCHITECTURE.md:6243-6251 (§17.1). No date or ratifier stated.

### D-122 — Every public class and method is documented in musical terms

> Every public class must have a documentation comment explaining:
> - What musical concept it implements
> - What it receives as input (in musical terms)
> - What it produces as output (in musical terms)
> - What it does not handle (important for setting expectations)

**In plain words.** A public class must say which musical idea it implements, what music it takes in, what it produces, and what it deliberately does not handle. A public method must say the same about the musical operation it performs, in musical terms rather than programming terms.

**Why.** Stated constraint, ARCHITECTURE.md:452-456 (§2.6) with :6322-6323: the documentation is written so a person with reasonable musical knowledge and basic programming familiarity can read it, including MuseScore contributors with no familiarity with this codebase at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6255`

**Provenance.** ARCHITECTURE.md:6253-6265 (§17.2). No date or ratifier stated.

### D-123 — Every non-obvious scoring weight or threshold explains its musical reasoning

> Every non-obvious scoring weight or threshold must explain its musical reasoning.

**In plain words.** A number in the scoring code that is not self-evident must be accompanied by the musical reason it has the value it has.

**Why.** Stated constraint, ARCHITECTURE.md:6303-6306 (§17.3): the analyzers are the most complex components, and their weights and thresholds are where the musical judgment actually lives - an undocumented one is unreadable and unarguable.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6267`

**Provenance.** ARCHITECTURE.md:6267 (§17.2). No date or ratifier stated. ★ This is the rule the 2026-08-01 CLAUDE.md Conventions entry generalizes from scoring values to design decisions as a class (D-195) - and the rule this register's rationale field serves.

### D-124 — The analyzer code must be readable by a musician

> Every scoring weight, threshold, and heuristic must be documented with its musical
> rationale. A musician with reasonable theoretical knowledge must be able to read the
> analyzer code and understand why each decision was made.

**In plain words.** Every weight, threshold and rule of thumb in the chord and key analyzers carries its musical reason, to the standard that a musician with ordinary theoretical training can read the code and see why each choice was made.

**Why.** Stated constraint, ARCHITECTURE.md:6303: these are the most complex components in the codebase, so they are where readability is worth the most.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6304`

**Provenance.** ARCHITECTURE.md:6301-6313 (§17.3), which gives a worked example from existing code (the circle-of-fifths interval deltas). No date or ratifier stated.

### D-125 — Every test documents the musical situation, the expected result, and what a failure means

> Every test must document:
> - What musical situation is being tested
> - What the expected result is and why it is musically correct
> - What a failure would indicate about the system's behavior

**In plain words.** A test says which musical situation it exercises, what the right answer is and why it is musically right, and what it would mean about the system if the test failed.

**Why.** Stated constraint, ARCHITECTURE.md:6322-6323: the tests must be readable by MuseScore contributors with no deep familiarity with this codebase.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6317`

**Provenance.** ARCHITECTURE.md:6315-6323 (§17.4). No date or ratifier stated.

### D-126 — One coherent piece of functionality per pull request

> Each pull request should implement one coherent piece of functionality. Large
> pull requests are hard to review. The phased plan in Section 15 defines natural
> PR boundaries.

**In plain words.** Each contribution offered back to MuseScore does one thing.

**Why.** Stated constraint, ARCHITECTURE.md:6338-6340: large pull requests are hard to review, and the phased plan defines where the natural boundaries fall.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6338`

**Provenance.** ARCHITECTURE.md:6336-6340 (§18.2). No date or ratifier stated.


## Group K — Documentation governance

### D-127 — An architectural decision that changes is documented in the same commit

> When an architectural decision changes — update this document in the same commit.
> Stale documentation is worse than no documentation because it actively misleads.
> Claude Code should update relevant sections of this document as its last act when
> a session changes an architectural decision.

**In plain words.** When a design decision changes, the change to this document goes in the same commit as the change to the code.

**Why.** Stated constraint, ARCHITECTURE.md:6351: stale documentation is worse than no documentation, because it actively misleads.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6350`

**Provenance.** ARCHITECTURE.md:6348-6353 (§18.4); the standing principle is CLAUDE.md #10 (D-174). No date or ratifier stated.


## Group M — The style system and the knowledge base

### D-128 — Styles are defined entirely in data; adding one never requires code changes

> Musical styles are defined entirely in JSON files. The C++ code implements mechanisms —
> voice leading optimization, chord generation, voicing rules — while JSON files define
> parameters. Adding a new style never requires C++ changes.

**In plain words.** A musical style is a data file. The program code implements the mechanisms - voice leading, chord generation, voicing - and the style file supplies the numbers that make one style behave differently from another. Adding a style is never a code change.

**Why.** Stated constraint, ARCHITECTURE.md:388-390 (§2.1) with the worked wrong/correct pair at :392-402: behaviour that branched on a style's identity would make every new or renamed style a code change.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:3986`

**Provenance.** ARCHITECTURE.md:3984-3988 (§6.1); the principle it realizes is D-070 (§2.1). No date or ratifier stated.

### D-129 — Style conflicts resolve by a declared priority - explicit overrides always win

> **Conflict resolution priority:**
> 1. System defaults — lowest priority
> 2. Mixin sources — in declared order, later overrides earlier
> 3. Explicit `overrides` in the style file — highest priority, always wins

**In plain words.** When a style assembles itself from several inherited sources, the order of precedence is fixed: system defaults are weakest, inherited sources come next in the order they are declared with later ones winning, and anything the style file states explicitly wins outright.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4030`

**Provenance.** ARCHITECTURE.md:4030-4033 (§6.2). No date or ratifier stated.

### D-130 — The style loader never names a style in code

> The style loader scans the styles directory recursively and loads all valid JSON files.
> It never references specific style IDs in code — it simply loads whatever it finds.

**In plain words.** The loader reads whatever style files it finds in the styles directory. No style's name appears anywhere in the program code.

**Why.** Stated constraint, ARCHITECTURE.md:435-438 (§2.4): no comparison against a style name anywhere in the codebase - style-specific behaviour flows entirely through parameters.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4066`

**Provenance.** ARCHITECTURE.md:4064-4067 (§6.4); the principle it realizes is D-070 (§2.1/§2.4). No date or ratifier stated.

### D-131 — One shared style taxonomy, not two parallel vocabularies

> The style vocabulary the presets select on is **one shared, hierarchical taxonomy** (common-practice / jazz / vernacular
> families — Baroque, Classical/galant, Romantic; trad, swing/songbook, bebop, hard-bop, cool, modal; blues, ragtime,
> gospel-soul, rock, pop, folk, barbershop) — the **same** set the Harmonic Vocabulary (§7) tags its entries with, not two
> parallel vocabularies. Inclusion rule: a style is listed iff it has a **distinct functional-harmonic vocabulary** (free
> jazz / atonal excluded).

**In plain words.** The list of style families the presets choose from is the SAME list the harmonic vocabulary tags its entries with - one hierarchy, not two that can drift apart. A style earns a place on it only if its functional harmony is genuinely distinct, which is why free jazz and atonal music are not on it.

**Why.** Stated constraint, ARCHITECTURE.md:4114-4116 - #6, one path per concern, applied to a vocabulary: two parallel taxonomies of the same thing would diverge, and the inclusion rule (a distinct functional-harmonic vocabulary) is what keeps the list from growing by analogy.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4112`

**Provenance.** ARCHITECTURE.md:4110-4120 (§6.7); full proposal `cowork_progression_schema_dictionary.md` §6/§12 and `cowork_style_clustering_plan.md`. No date or ratifier stated.

### D-132 — The style taxonomy is a theory-based first version; grounding it empirically is committed work

> It is a **theory-based v1**; **empirically grounding** it — deriving the clusters *and* the
> per-style weights by clustering corpora — is committed future work (`cowork_style_clustering_plan.md`)

**In plain words.** The style families and their weights are currently drawn from music theory, not from data. Deriving both from corpora instead is recorded as work that will be done, not as an option.

**Why.** Stated constraint, ARCHITECTURE.md:4117-4119: the clusters and their feature distributions are one data-derived object, and it is reachable for jazz and pop from lead-sheet corpora even where note-level ground truth is scarce - which is what makes the grounding committable rather than aspirational.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4116`

**Provenance.** ARCHITECTURE.md:4110-4120 (§6.7). No date or ratifier stated.

### D-133 — The harmonic vocabulary is a queried reference component, not a layer of the analysis

> It is reference knowledge **queried** by the layers and by
> future tools, **not a pipeline layer**. Entries carry **provenance** (established theory), not a ground-truth-validation
> status — validation is the *consumer's* concern (verifiability contract, §2.15).

**In plain words.** The catalogue of progressions and substitutions is something the analysis stages ask questions of, not a stage they pass through. Its entries say where the theory comes from; whether that theory holds up against real music is the caller's question, not the catalogue's.

**Why.** Stated constraint, ARCHITECTURE.md:4138 - the verifiability contract (D-029): reference knowledge grounded in established theory may be carried without corpus validation, provided the consumer that puts it under load is the one that must validate it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4136`

**Provenance.** ARCHITECTURE.md:4129-4143 (§7); own specification `cowork_progression_schema_dictionary.md`. No date or ratifier stated.


## Group N — Generation, constraints, visualization, and the LLM integration

### D-134 — A voicing type is never requested directly; the style selects it

>     // Style determines which voicing types are used and in what proportion.
>     // Never call with a specific voicing type directly — encode that in the style.

**In plain words.** A caller asking for a voicing says which style it wants, never which voicing technique. The style decides whether the answer is a drop-2, a shell, a chorale spacing or something else, and in what proportion.

**Why.** Stated constraint, ARCHITECTURE.md:4234-4237: keeping the interface voicing-type agnostic is what lets a new voicing type be added as a generator implementation plus a style parameter, without the interface changing.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4242`

**Provenance.** ARCHITECTURE.md:4229-4251 (§8.2); the principle it realizes is D-070 (§2.1). No date or ratifier stated.

### D-135 — A fixed element is a hard constraint the optimizer may never modify

> Fixed elements are hard constraints in the voice leading optimizer — they anchor
> the dynamic programming search. The optimizer guarantees never modifying them.

**In plain words.** Anything the user has pinned - a note, a voice, a chord, a passage - anchors the search for good voice leading. The optimizer works around it and never changes it.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4411`

**Provenance.** ARCHITECTURE.md:4373-4412 (§9.1-§9.2). No date or ratifier stated.

### D-136 — The inference demo view is a developer tool and is not shipped

> A step-through visualization of the inference pipeline, for use by developers
> during quality assurance and algorithmic development. Not shipped to end users.

**In plain words.** The step-by-step view of the analysis making its decisions exists so a developer can watch and judge it by eye and ear. It is not part of what a user gets.

**Why.** Stated constraint, ARCHITECTURE.md:4430-4432: it exists to make musical correctness checkable by eye and ear rather than only through the automated agreement numbers.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4426`

**Provenance.** ARCHITECTURE.md:4424-4514 (§10.0), whose own status line reads 'Not yet started'. No date or ratifier stated.

### D-137 — The harmony maps are our own visual design, and are chosen partly to avoid intellectual-property claims

> MTH Pro-style map based on Berklee chord-scale theory (Nettles, Levine). Positions
> chords by functional region (tonic, subdominant, dominant) and shows available
> tensions. Our own visual design — not a reproduction of MTH Pro's specific layout.

**In plain words.** The planned map of harmonic function draws on published chord-scale theory but is laid out our own way, not copied from the commercial product that inspired it.

**Why.** Stated constraint, ARCHITECTURE.md:4559 and :4573: the circle of fifths and the Tonnetz were chosen partly because they carry no intellectual-property claim - the Tonnetz being a nineteenth-century mathematical structure - and the same reasoning is what forces an original layout for the functional map.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4577`

**Provenance.** ARCHITECTURE.md:4556-4579 (§10.2-§10.4), all three marked planned. No date or ratifier stated.

### D-138 — Chord preview uses MuseScore's note-input pathway, not the playback pipeline

> **Implementation note:** Use MuseScore's note-input preview pathway (same as hearing
> a note when clicking in input mode) — not the full score playback pipeline. The
> full pipeline has too much latency for interactive map exploration. Inference runs
> on a background thread via `QtConcurrent` to keep the UI responsive.

**In plain words.** Clicking a chord on a harmony map plays it through the same quick path MuseScore uses when you hear a note as you enter it, not through full score playback.

**Why.** Stated constraint, ARCHITECTURE.md:4609-4611: the full playback pipeline has too much delay for interactive exploration, and the inference runs on a background thread so the interface stays responsive.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4608`

**Provenance.** ARCHITECTURE.md:4581-4611 (§10.5), a planned component. No date or ratifier stated.

### D-139 — The language model holds no object references - every tool call carries its own musical address

> **Stateless tool-call model.** The LLM does not hold object references. Each
> tool call carries its own musical address. No proxy objects, no EID handles,
> no lifecycle management. This is the right model for LLM interaction and the
> simpler one to implement.

**In plain words.** When a language model asks the program to do something, it names the place in the music each time. It never holds a handle to an object in the score.

**Why.** Stated constraint, ARCHITECTURE.md:6383-6384: no proxy objects, no element handles and no lifecycle management - recorded as both the right model for this kind of interaction and the simpler one to implement.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6381`

**Provenance.** ARCHITECTURE.md:6374-6384 (§19.2), a planned module; full design `docs/llm_integration.md`. No date or ratifier stated.

### D-140 — The language model is a search agent and is never given the whole score

> **LLM as search agent.** The LLM is never given a full score dump. It has
> search tools (`find_notes`, `get_part`, `get_measure`, `search_harmony`) and
> fetches what it needs iteratively — exactly as Claude Code uses Grep and Read
> in a large codebase. Serialization quality is the critical foundation: clean,
> hierarchical, beat-aligned, free of layout noise.

**In plain words.** Rather than being handed the entire score, the language model is given tools to find what it needs and fetches it piece by piece - the way a person reads a large document by searching it.

**Why.** Stated constraint, ARCHITECTURE.md:6389-6390: because the model reads what it fetches, the quality of that serialization - clean, hierarchical, beat-aligned, free of layout noise - is the critical foundation.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6386`

**Provenance.** ARCHITECTURE.md:6374-6390 (§19.2), a planned module. No date or ratifier stated.

### D-141 — The language model sees what the user set, not what the engraving engine derived

> **Intentional vs. computed.** The LLM sees everything the user deliberately
> set (pitch, dynamics, articulation, note color, lyrics formatting, visibility).
> It does not see what the engraving engine derived (positions, beam geometry,
> stem lengths, `LayoutData`). The `Pid` property system is the practical
> boundary.

**In plain words.** The model is shown the composer's own choices - pitches, dynamics, articulation, colour, lyrics, visibility - and not the results of laying the music out, such as positions, beam geometry or stem lengths.

**Why.** Stated constraint, ARCHITECTURE.md:6396: MuseScore's own property system is the practical boundary between the two, so the split is enforceable rather than judged case by case.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6392`

**Provenance.** ARCHITECTURE.md:6374-6396 (§19.2), a planned module. No date or ratifier stated.

### D-142 — The composing module is the language model's context provider; the model never re-derives harmony

> The composing module (`src/composing/`) is the LLM's context provider. Its
> harmonic analysis output (chord symbols, Roman numerals, key inference,
> harmonic rhythm) is included in every score section sent to the LLM. The LLM
> does not re-derive harmony from raw pitch data — it receives pre-digested
> musical context.

**In plain words.** Every stretch of music sent to a language model arrives with our harmonic analysis already attached - chord symbols, Roman numerals, key, harmonic rhythm. The model reads that; it does not work the harmony out from the notes itself.

**Why.** Stated constraint, ARCHITECTURE.md:6411-6413: the same analysis also drives the validation step that checks voice leading and harmonic consistency before a generated change reaches the score, so one analysis serves both directions.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6405`

**Provenance.** ARCHITECTURE.md:6403-6417 (§19.3), a planned module. No date or ratifier stated.

### D-143 — The language-model bridge is built as a module but confined to the core access layer, so it can become a plugin

> **Build strategy:** Implement the LLM bridge as a native module initially for
> speed, but strictly constrained to the Core Access Layer only (never bypassing
> it to the DOM). When the plugin API matures, migration to a plugin is then
> straightforward. See `docs/llm_integration.md §11` for the full argument.

**In plain words.** It is written inside the program for speed of development, but restricted to the same narrow interface a plugin would have, so that moving it out to a plugin later is straightforward.

**Why.** Stated constraint, ARCHITECTURE.md:6419-6424: with a properly designed plugin interface the bridge does not need to live in the core at all - it becomes optional, independently updatable, provider-agnostic and open to community alternatives - so the constraint is what keeps that end state reachable.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6426`

**Provenance.** ARCHITECTURE.md:6419-6429 (§19.4), a planned module; full argument `docs/llm_integration.md` §11. No date or ratifier stated.


## Group O — Intonation

### D-144 — Percussion is excluded from analysis and tuning; fixed-pitch instruments are the tuning anchor

> Percussion instruments are excluded from both harmonic analysis and intonation.
> Fixed-pitch instruments (piano) serve as intonation anchors when present.

**In plain words.** Unpitched percussion takes no part in working out the harmony and receives no tuning adjustment. Where a piano or organ is playing, the other instruments tune to it.

**Why.** Stated constraint, ARCHITECTURE.md:4636-4637 and :4781-4782: a fixed-pitch instrument cannot adjust, so it is the natural reference - and its presence resets accumulated drift at every chord it plays.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4649`

**Provenance.** ARCHITECTURE.md:4630-4650 (§11.2). No date or ratifier stated.

### D-145 — One preference chooses the tuning system, and no tuning code hardcodes one

> All tuning code paths read the preference at call time via `preferredTuningSystem()`
> (defined in `notationtuningbridge.cpp`), which resolves the key through
> `TuningRegistry::byKey()` with a `JustIntonation` fallback if the key is unset or
> unknown.  No tuning code hardcodes a specific system.

**In plain words.** Which tuning system is in force is a single user setting, read afresh each time any tuning happens. No part of the tuning code has a system built into it.

**Why.** Stated constraint, ARCHITECTURE.md:4652-4660 - #6, one path per concern: the same preference governs per-note tuning, chord-staff population and region tuning, so the three cannot silently disagree about what tuning the user asked for.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4665`

**Provenance.** ARCHITECTURE.md:4652-4668 (§11.2a). No date or ratifier stated.

### D-146 — A tie chain is one indivisible tuning event, and its tuning comes from one authority note

> **Tied notes:** A non-partial tie chain explicitly carries a compositional instruction of
> continuity. For region tuning, the entire non-partial tie chain is treated as one tuning
> event. The chain must not be split. Its tuning is set from a single authority note and
> protected thereafter; later harmonic regions tune around that established pitch.

**In plain words.** Notes joined by ties are one sustained sound, so they are tuned once and never split apart. The tuning is worked out from a single note in the chain - the one carrying a tuning anchor if there is one, otherwise the first - and applied unchanged to the whole chain.

**Why.** Stated constraint, ARCHITECTURE.md:4911-4912 and :4923-4924: a tie is a compositional instruction of continuity, so splitting it would contradict what the composer wrote; a user who wants the sustained sound retuned as the harmony moves writes a slur instead.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:4911`

**Provenance.** ARCHITECTURE.md:4911-4924 (§11.3c), with the region-tuning consequence at :5726-5729 (§11.6). No date or ratifier stated.

### D-147 — A slur, not a tie, joins the halves of a split note

> A **slur** (not a tie) connects the two halves.  This is a deliberate choice:
> MuseScore's playback engine treats tied notes as one continuous sound with a single
> tuning value, so a tie would silently discard note_B's tuning.  A slur produces two
> independent playback events with legato articulation, allowing each half to carry
> its own tuning offset.

**In plain words.** When a sustained note must be retuned partway through, it is cut in two and the halves are joined with a slur rather than a tie.

**Why.** Stated constraint, ARCHITECTURE.md:5351-5354: MuseScore's playback treats tied notes as one continuous sound with a single tuning value, so a tie would silently discard the second half's tuning; a slur produces two independent playback events, each able to carry its own offset.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5350`

**Provenance.** ARCHITECTURE.md:5343-5354 (§11.4). No date or ratifier stated.

### D-148 — The split is visible in the score; the invisible alternative is deferred

> The split is **visible** — the score shows two shorter notes connected by a slur.
> This is the simplest correct approach and is fully undoable via MuseScore's standard
> undo system.

**In plain words.** The reader sees two shorter notes joined by a slur where a note was retuned. The alternative - keeping the written note and hiding a silent playing copy - was designed and set aside.

**Why.** Stated constraint, ARCHITECTURE.md:5357-5358: the visible split is the simplest correct approach and is fully undoable through MuseScore's own undo. The excluded alternative's recorded blocker (:5360-5363) is that it needs a visual indicator for tuning-applied notes before it is practical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5356`

**Provenance.** ARCHITECTURE.md:5356-5363 (§11.4), with the deferred alternative recorded at `backlog_invisible_split.md`. No date or ratifier stated.

### D-149 — Only visible, sounding notes enter the pitch-class collection

> Chord analysis filters notes with `visible = true` and `play = true`, excluding
> both silent notes and any future invisible tuning artifacts from the pitch-class
> collection.

**In plain words.** Notes marked invisible, and notes that do not play, take no part in identifying the chord - which also keeps any hidden note created by the tuning machinery out of the analysis.

**Why.** Stated constraint, ARCHITECTURE.md:5381-5382: the filter excludes both silent notes and any future invisible tuning artifact, so tuning a passage cannot change what the analysis of that passage sees.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5380`

**Provenance.** ARCHITECTURE.md:5378-5382 (§11.4). No date or ratifier stated. The joint estimator's own eligibility flags are the Layer-1 fact surface (D-039/D-045).

### D-150 — The chord staff is the output, never an input to the analysis that fills it

> The target staff is excluded from the analysis input — it is the output, not a
> source.  This prevents feedback loops when re-running the analysis.

**In plain words.** When the harmonic reduction is written onto a staff, that staff's own contents are kept out of the analysis that produced them.

**Why.** Stated constraint, ARCHITECTURE.md:5438: it prevents a feedback loop when the analysis is re-run over music that already carries its own reduction. The joint estimator's record path realizes the same rule at its own input surface - D-013, open_items/OI-204.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5437`

**Provenance.** ARCHITECTURE.md:5428-5438 (§11.5). No date or ratifier stated.

### D-151 — Populating the chord staff overwrites whatever is in the selected range

> **Any existing content in the selected region is overwritten.**  Re-analysis after
> score edits simply selects the same range and runs again.  If the user wants to
> preserve a previous analysis, they can undo or copy it elsewhere first.

**In plain words.** Running the reduction again over the same passage replaces what is there. Keeping an earlier analysis is the user's job - undo it, or copy it somewhere else first.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5440`

**Provenance.** ARCHITECTURE.md:5440-5442 (§11.5). No date or ratifier stated.

### D-152 — Roman numerals and Nashville numbers are never shown together on one staff

> **Chord function notation** attached below the treble staff — either
> `HarmonyType::ROMAN` (Roman numerals) or `HarmonyType::NASHVILLE` (Nashville
> numbers), selected by the "Chord function notation" preference (None / Roman
> numerals / Nashville numbers).  Roman and Nashville are mutually exclusive on
> the staff because they encode identical information; displaying both would be
> redundant and legibility-destroying.

**In plain words.** The chord staff shows one or the other beneath the music, chosen by preference, never both.

**Why.** Stated constraint, ARCHITECTURE.md:5505-5507: the two notations encode identical information, so showing both would be redundant and would destroy legibility.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5502`

**Provenance.** ARCHITECTURE.md:5502-5507 (§11.5); the same choice on the analysis side is D-086. No date or ratifier stated.

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

**Why.** Stated constraint, ARCHITECTURE.md:5694-5700: the interactive output is meant to be publication-ready and indistinguishable from hand-entered symbols, while the red is a filter criterion that lets the automated review separate our inferred annotations from whatever the score already contained.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5693`

**Provenance.** ARCHITECTURE.md:5691-5700 (§11.5). No date or ratifier stated.


## Group P — The user interface, persistence, and machine-learning readiness

### D-154 — New panels use MuseScore's own panel and interface infrastructure

> New panels follow MuseScore's existing panel architecture — KDDockWidgets for
> panel management, QML for UI components. Do not create parallel infrastructure.
> Read how existing MuseScore panels are implemented before creating new ones.

**In plain words.** Any new panel is built with the same window-docking and interface technology MuseScore already uses, after reading how MuseScore's existing panels are built. No parallel machinery is created.

**Why.** Stated constraint, ARCHITECTURE.md:467-471 (§2.8): read how MuseScore already does it and follow the same pattern - the same rule that governs score traversal, playback, settings and localization.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5811`

**Provenance.** ARCHITECTURE.md:5809-5813 (§12.1); the panels themselves are planned (§12.2-§12.5). No date or ratifier stated.

### D-155 — Every user-visible string goes through MuseScore's localization, in English and Swedish

> All user-visible strings use MuseScore's existing Qt localization infrastructure
> (`.ts` files, Qt Linguist). English and Swedish translations provided for all new strings.

**In plain words.** Text a user can read is translatable through MuseScore's own translation system, and every new string is supplied in English and Swedish.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5815`

**Provenance.** ARCHITECTURE.md:5815-5816 (§12.1); listed in the Core scope at ARCHITECTURE.md:6211-6212. No date or ratifier stated.

### D-156 — Accessibility follows MuseScore's existing patterns

> Accessibility follows MuseScore's existing Qt accessibility patterns — focus
> management, keyboard navigation, screen reader hooks.

**In plain words.** Keyboard navigation, focus handling and screen-reader support are done the way MuseScore already does them.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5818`

**Provenance.** ARCHITECTURE.md:5818-5819 (§12.1); listed in the Core scope at ARCHITECTURE.md:6212. No date or ratifier stated.

### D-157 — The harmonic-display preference exists for clarity, not for cost

> A user preference controls whether harmonic analysis is shown in the status bar. This
> preference exists for UI clarity — some users find the chord and key information
> distracting, particularly when doing work unrelated to harmony. It is not a performance
> control: analysis cost is negligible (well under 1ms) and suppressing the display does
> not require skipping the analysis.

**In plain words.** The setting that hides the harmonic information from the status bar is there because some users find it distracting, not because the analysis is expensive. Switching it off does not skip the analysis.

**Why.** Measurement named in the record, ARCHITECTURE.md:5825-5827: the analysis cost at this seam is 'well under 1ms'. ★ That number is the LEGACY bounded-window path's; open_items/OI-203 and OI-206 record the record arm running a whole-score decode per selection, measured in seconds on large scores - so the reason this preference is not a performance control no longer holds as stated.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5823`

**Provenance.** ARCHITECTURE.md:5821-5831 (§12.1a). No date or ratifier stated.

### D-158 — Our data lives in separate files inside the score archive; the score file is never touched

> MuseScore's MSCZ format is a ZIP archive. Our metadata lives as additional files
> within the archive alongside `score.mscx`:

**In plain words.** Constraints, branches, cached analysis and preferences travel with the score as extra files inside its archive, beside the standard MuseScore score file, which our code never modifies.

**Why.** Stated trade-off, ARCHITECTURE.md:5901-5905: the score stays a valid standard MuseScore file with zero interference in MuseScore's own reading and writing, and our data travels with it. The accepted cost is stated too - exporting to MusicXML, PDF or MIDI loses it, which is acceptable because the workflow is MuseScore-native.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5889`

**Provenance.** ARCHITECTURE.md:5887-5905 (§13.1), a planned component. No date or ratifier stated.

### D-159 — Every custom file carries a format version, and the score file is never rewritten by our persistence

> All our custom files include a format version field. When the format changes,
> migration code handles existing files. The score.mscx is never modified by our
> persistence layer.

**In plain words.** Each of our own files records which version of its format it is, so older files can be migrated when the format changes; the standard MuseScore score file inside the archive is never rewritten by us.

**Why.** derivation not recorded.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5909`

**Provenance.** ARCHITECTURE.md:5907-5911 (§13.2), a planned component. No date or ratifier stated.

### D-160 — Arranger interactions are logged from the start, with consent, as future training data

> The system logs arranger interactions from the start — with user consent — as
> future ML training data. Every suggestion accepted, modified, or rejected is a
> labeled training example specific to vocal jazz arranging, filling the corpus gap
> identified in the design phase.

**In plain words.** Every suggestion a user accepts, changes or rejects is recorded - with their consent - as a labelled example for future machine learning.

**Why.** Stated constraint, ARCHITECTURE.md:5954-5955: the recording exists to fill the corpus gap identified in the design phase, there being no existing labelled corpus of vocal jazz arranging decisions.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5952`

**Provenance.** ARCHITECTURE.md:5950-5967 (§14.2), a planned component. No date or ratifier stated.

### D-161 — Chord symbols already in a score are a second analyst's opinion, not ground truth

> Mode 2 — Pre-existing symbols present: treated as a second analyst's opinion,
> not ground truth. Judge comments on agreements and disagreements without
> scoring disagreements as errors. Framing: "two analysts may reach different
> but equally valid conclusions."

**In plain words.** When the automated review meets a score that already carries chord symbols, it treats them as another analyst's reading. Disagreements are discussed, not scored as our errors.

**Why.** Stated constraint, ARCHITECTURE.md:5986-5987, in the record's own words: two analysts may reach different but equally valid conclusions. Errors are scored only in Mode 3, against a known ground-truth corpus (:5989-5990) - the same distinction the project's standing rule draws between corroboration and ground truth.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:5984`

**Provenance.** ARCHITECTURE.md:5969-5994 (§14, the automated annotation review), marked planned. No date or ratifier stated.


## Group Q — Scope and the development toolchain

### D-162 — The development tools are not part of the shipping product

> The following tools live in `tools/` and are **not part of the shipping product**.
> They are compiled/run only in development builds (`MUE_BUILD_ENGRAVING_DEVTOOLS=ON`).

**In plain words.** The batch analysis tool, the comparison scripts and the remaining measurement tools are built only in development builds and never ship to a user.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6032`

**Provenance.** ARCHITECTURE.md:6030-6033 (§15). No date or ratifier stated.

### D-163 — The batch tool deliberately skips post-load layout

> and `iex_musicxml` — no notation module required. Because the tool only consumes
> logical score structure, it deliberately skips forced post-load layout; this avoids
> legacy native MSCX cache-overflow crashes (for example Mozart `K533-3`) without
> changing the emitted harmonic-analysis JSON.

**In plain words.** The headless analysis tool never lays the music out on the page, because it only ever reads the logical structure.

**Why.** Stated constraint, ARCHITECTURE.md:6042-6044: skipping the layout avoids a legacy cache overflow crash on some scores (Mozart K533-3 is named) without changing the harmonic-analysis output at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6041`

**Provenance.** ARCHITECTURE.md:6035-6044 (§15). No date or ratifier stated.

### D-164 — What is out of scope, and what degrades gracefully at the boundary

> Live and real-time operation, film synchronization, adaptive game music, non-Western
> traditions (graceful degradation at boundary), post-tonal and serial music (graceful
> degradation at boundary), audio transcription from recording, spatial music, extended
> techniques as primary language.

**In plain words.** Live performance, film and game synchronization, audio transcription, spatial music and extended techniques as a primary language are not attempted. Non-Western traditions and post-tonal music are not attempted either, but the system is required to fail gracefully where it meets them rather than producing confident nonsense.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:6234`

**Provenance.** ARCHITECTURE.md:6199-6237 (§16), which sorts the whole feature set into Core / Important / Prepared / Out of scope. No date or ratifier stated.


## Group S — The guiding principles

### D-165 — #1 - build only on established fact and theory

> 1. **Fact- and theory-based coding only.** Build only on established fact and theory —
>    published research, public algorithms, public software. Fact-finding (investigative)
>    coding is allowed.

**In plain words.** Nothing is built on a hunch. Every method comes from published research, a public algorithm, or public software. Investigating to find out what the facts are is a separate, permitted activity.

**Why.** Derivation not recorded as a separate defense - this is the founding premise the other principles are stated against. Its operational consequence is recorded: #3 makes an unexpected finding a failure of this principle rather than a curiosity (CLAUDE.md:14-16).

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:9`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:9-11, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-166 — #2 - target the specific open question, not the general topic

> 2. **Specific research over general.** Most research so far has been general or on
>    already-handled topics; target the specific open question.

**In plain words.** Research effort goes to the exact question in front of us, not to the surrounding subject generally or to something already handled.

**Why.** Stated constraint, CLAUDE.md:12-13: most research done so far has been general or on already-handled topics - the observation that motivates the rule.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:12`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:12-13, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-167 — #3 - an unexpected finding is a failure to diagnose, not a curiosity

> 3. **An unexpected finding means we have failed #1** (and possibly #2, #4, #6). Surprise
>    signals that the fact/theory basis was incomplete — treat it as a failure to diagnose,
>    not a curiosity.

**In plain words.** Being surprised means the facts and theory we built on were incomplete. Surprise is treated as a defect in our own understanding, not as an interesting result.

**Why.** Stated constraint, CLAUDE.md:14-15: surprise signals that the fact and theory basis was incomplete, which is a failure of #1. Its operational form is #13 - surface it as a stop before building around it.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:14`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:14-16, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-168 — #4 - the long-term goal is maximum-precision inference

> 4. **Long-term goal: maximum-precision inference.**

**In plain words.** The objective the whole project is measured against is getting the analysis as accurate as it can be made.

**Why.** Derivation not recorded - this is the stated objective, not a decision derived from something else. It is what the decision-neutrality corollary (CLAUDE.md:106-118) means by 'the ultimate objective'.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:17`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:17, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-169 — #5 - when facts may be scarce, investigate

> 5. **Investigate when facts may be scarce.** If we are unsure whether facts are scarce,
>    gather more facts.

**In plain words.** If it is unclear whether we know enough about something, the answer is to go and find out, not to proceed on what we have.

**Why.** Stated constraint, CLAUDE.md:85-89 (the scope-of-surprise rule): explorational runs whose purpose is to eliminate ignorance are exactly where surprises are permitted - so fact-finding is the cheap stage that keeps surprises out of the expensive one.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:18`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:18-19, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-170 — #6 - total unification: one path per concern

> 6. **Total unification — no duplication of any code.** One path per concern.

**In plain words.** There is exactly one implementation of any given concern. No duplicated code, no second place the same question is answered.

**Why.** Measurement named elsewhere in the record: `cowork_siloed_facts_audit.md` found 17 instances of facts being re-derived rather than read (CLAUDE.md:94-95), and open_items/OI-173 records four inequivalent definitions of one predicate as the cost of a second path. The end-state reading is fixed by #23 and by the decision-neutrality corollary (CLAUDE.md:116-118): #6 is a structural end-state principle, not a preservation claim for whatever exists now.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:20`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:20, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-171 — #7 - a layer is enhanced only with what belongs to it

> 7. **Adhere to layers.** Enhance a layer only with algorithms/methods that belong to it,
>    nothing else. Worst case, this forces a layer redesign rather than a cross-layer patch.

**In plain words.** A stage of the analysis gets only the methods that are properly its own. If the right method does not belong there, the layers are redesigned rather than the method smuggled across.

**Why.** Stated constraint, CLAUDE.md:22: the worst case is a layer redesign, which is explicitly preferred to a cross-layer patch.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:21`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:21-22, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-172 — #8 - no inference-problem-driven coding until every method sits in its correct layer

> 8. **No inference-problem-driven coding until all methods and algorithms are implemented
>    in their correct layer.**

**In plain words.** Work is not steered by whichever analysis error is currently visible. Until the structure is built out, a fix is made at the stage that owns it, at the time that stage is being built.

**Why.** Derivation not recorded as a separate defense. The related recorded position is that a fix at its #8-correct stage is 'never a knob-turn' - the phrase carried on the open-item rows that defer a fix for this reason (for example open_items/OI-192, OI-216, OI-217).

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:23`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:23-24, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-173 — #9 - measure only on corpora known to be non-stale and accurate

> 9. **Test and measure only on corpora known to be non-stale and accurate.**

**In plain words.** A measurement is only run against music whose annotations are current and correct.

**Why.** Sharpened by #21 (CLAUDE.md:61-65): the accuracy of ground truth is itself a measured quantity rather than an assumed one, so 'accurate' means measured per-axis annotator agreement, not an assumption.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:25`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:25, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-174 — #10 - documentation always in sync with code

> 10. **Documentation always in sync with code.**

**In plain words.** The documents describing the system never lag behind the system.

**Why.** Stated constraint, ARCHITECTURE.md:6351: stale documentation is worse than no documentation because it actively misleads. The same-commit rule that operationalizes it is at ARCHITECTURE.md:6350-6353.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:26`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:26, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-175 — #11 - regression tests in sync with code, and run between iterations

> 11. **Regression test cases always in sync with code; regression-test between iterations.**

**In plain words.** The tests that guard against going backwards are kept current with the code, and they are run between each step of work rather than at the end.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratified by user

**Home.** `CLAUDE.md:27`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:27, the user's standing list. CLAUDE.md:120-132 records the provenance of the whole list: principles 1-11 are the user's standing list; #12-#16 were ratified by the user 2026-07-06; #17-#19 and the surprise-scope rule 2026-07-10; #20-#24 and the constrained-optimum ledger corollary 2026-07-18 at the joint-estimator plan review.

### D-176 — #13 - surface a surprise as a stop before building around it

> 13. **Surface a surprise as a STOP before building around it** (the operational form of #3).

**In plain words.** When something unexpected turns up, work halts and it is reported. It is never quietly worked around.

**Why.** Stated constraint, CLAUDE.md:31: this is the operational form of #3 - if surprise means the fact basis was incomplete, then building on top of the surprise builds on the same incomplete basis.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:31`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:31; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-177 — #14 - every behavior change is one user-ratified, revertible, provenance-stamped commit

> 14. **Every behavior change is user-ratified as one revertible, provenance-stamped commit.**

**In plain words.** Anything that changes what the system does is ratified by the user first, lands as a single commit that can be undone whole, and carries the record of where it came from.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:32`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:32; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-178 — #15 - verify at the objects on the full output surface, never at an assertion

> 15. **Verify at objects/data on the full output surface, never at assertion** (winner *and*
>     carry, not the winner alone).

**In plain words.** A result is confirmed by looking at the actual data it produced, across everything it produced - the chosen reading and the alternatives carried beside it - not by a test that asserts what was expected.

**Why.** Stated constraint, CLAUDE.md:33-34: checking the winner alone would miss a change in the carried alternatives, which are part of the published surface (#12).

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:33`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:33-34; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-179 — #16 - every measurement is stamped to its corpus and its tooling, and the outgoing reference is snapshotted

> 16. **Reproducibility.** Every measurement is stamped to corpus-hash + instrument-commit;
>     snapshot the outgoing reference before any re-baseline.

**In plain words.** A measurement records which music it was run on and which version of the measuring code produced it, and the previous reference numbers are saved before new ones replace them.

**Why.** Stated constraint, CLAUDE.md:75-78 (#24): reproducibility bounds the error the measuring tools introduce, as the companion of the sampling error #24 bounds - so a number without both is not interpretable.

**Status.** LIVE · decided 2026-07-06 · ratified by user

**Home.** `CLAUDE.md:35`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:35-36; ratified by the user 2026-07-06 (CLAUDE.md:120-122).

### D-180 — #17 - the Premise Gate

> 17. **The Premise Gate.** Before any inference-affecting design is built or probed:
>     (a) a **premise ledger** — every load-bearing causal claim explicitly labeled **FACT**
>     (citation to code/measurement), **THEORY** (citation to published research answering the
>     *specific* question, #2), or **ASSUMPTION**; (b) a **written quantitative prediction per
>     assumption** (fire-rate, magnitude, direction, population) recorded *before* measuring —
>     no prediction, no build; (c) a **desk simulation** — trace the mechanism by hand through
>     the intended architecture on 3–5 real corpus cases drawn from the known failing sets,
>     answering FIRST "does the mechanism FIRE on this case?" (control flow — ratified sharpening
>     2026-07-10, the EG-2 desk-sim lesson), THEN "which term moves, by how much?" (arithmetic);
>     (d) every **proxy→target
>     link is itself a ledger premise** (a structural proxy never stands in for a behavioral
>     quantity unvalidated); (e) every **insulation claim** ("X cannot affect Y") must enumerate
>     the false-negative path explicitly; (f) **no hand-transcribed measurement numbers** —
>     figures enter docs only via generated artifacts (the `manifest.json` pattern).

**In plain words.** Before anything that affects the analysis is built or even probed: every load-bearing causal claim is written down and labelled as an established fact, a published theory, or an assumption; every assumption gets a written numerical prediction BEFORE anything is measured; the mechanism is traced by hand through three to five real failing cases, asking first whether it fires at all and only then what it changes; any stand-in quantity must itself be justified; any claim that one thing cannot affect another must name how it could; and no number enters a document by being typed in by hand.

**Why.** Measurement, CLAUDE.md:44-45: part (c)'s fire-first ordering is a ratified sharpening from a specific failure - the desk simulation that traced arithmetic through a mechanism which, on the real case, never fired. Part (f)'s reason is recorded across the decisions register as the generated-artifact pattern: a hand-transcribed figure cannot be re-derived, and the harvest's own counts drifted one regeneration stale exactly that way.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:37`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:37-50; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-181 — #18 - an unverified causal premise is forbidden (Class A)

> 18. **Unverified causal premises are FORBIDDEN (Class A).** No design may carry load on a
>     causal claim about our own system or data that is checkable but unchecked.

**In plain words.** No design may rest on a claim about how our own system or data behaves when that claim could be checked and has not been.

**Why.** Stated constraint, CLAUDE.md:51-52: the prohibition is specifically about claims that are CHECKABLE - the cost of checking is what makes leaving them unchecked indefensible.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:51`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:51-52; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-182 — #19 - an unestablished measurement tool is forbidden (Class B)

> 19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
>     recorded figure is trusted only after being *positively established* (oracle cross-check,
>     derivation of what the measurement unit actually measures, reproduce-check) — never
>     because it is merely unfalsified.

**In plain words.** A measuring script, a corpus, a gate or a recorded figure is trusted only once it has been positively shown to be right - checked against an independent oracle, with a derivation of what its unit actually measures, and a reproduce-check. Never merely because nothing has contradicted it.

**Why.** Stated constraint, CLAUDE.md:55-56: 'never because it is merely unfalsified' - absence of contradiction is not evidence, so establishment has to be a positive act.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:53`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:53-56; ratified by the user 2026-07-10, analysis in `cowork_premise_gate_reflection.md` (CLAUDE.md:122-125).

### D-183 — #20 - fit and evaluation are separated

> 20. **Fit/evaluation separation.** No value is graded on data that helped fit it. Every fit
>     event declares its held-out data (split or k-fold) and its capacity budget (parameter
>     count, regularization, justified against corpus size) BEFORE fitting; the headline claim
>     is the held-out figure. A fitted-and-self-measured number is not established (#19).

**In plain words.** No number is graded on the same music that helped choose it. Before any fitting, the held-back music and the budget of how many free values may be fitted are declared; the headline figure is always the one measured on the held-back music.

**Why.** Stated constraint, CLAUDE.md:60: a value fitted and then measured on its own fitting data is not established at all (#19) - the figure describes the fitting, not the system.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:57`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:57-60; ratified by the user 2026-07-18 at the joint-estimator plan review, analysis `cowork_joint_estimator_architecture.md` §6/§7 (CLAUDE.md:125-129). The ratified protocols are open_items/OI-176 and OI-177.

### D-184 — #21 - ground truth is a measurement tool too, and its accuracy is measured

> 21. **Ground truth is an instrument too.** The accuracy of ground truth is itself a measured
>     quantity — per-axis annotator agreement, not an assumed binary (sharpens #9's "accurate").
>     Every precision target and every "irreducible residual" verdict is interpreted against
>     that measured ceiling; without it, structural error and annotator disagreement are
>     indistinguishable in the residual.

**In plain words.** How right the reference annotations are is itself something to be measured - how far annotators agree with each other, axis by axis - not assumed. Every precision target and every claim that a remaining error is irreducible is read against that measured ceiling.

**Why.** Stated constraint, CLAUDE.md:63-65: without the measured ceiling, our own structural error and disagreement between annotators are indistinguishable in what is left over - so an 'irreducible residual' verdict cannot be made at all.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:61`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:61-65; ratified by the user 2026-07-18 (CLAUDE.md:125-129). Sharpens #9.

### D-185 — #22 - every hard gate declares in advance how it handles the largest change it will meet

> 22. **Every hard gate carries a pre-declared protocol for the largest change it will face.**
>     A gate written only for incremental change must not be amended under the pressure of a
>     live diff — the exceptional-event variant (e.g. architecture-scale adoption: aggregate
>     criterion + explained diff + snapshot + ratification) is written and ratified before such
>     a change is on the table.

**In plain words.** A rule that decides whether a change may ship must say, before the fact, what it does when the change is far bigger than the incremental ones it was written for. It must never be rewritten while such a change is sitting in front of it.

**Why.** Stated constraint, CLAUDE.md:67-68: a gate amended under the pressure of a live difference is no longer a gate. The exceptional-event variant this required was written and ratified as open_items/OI-178 before the joint estimator's first decode was measured against the stop.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:66`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:66-70; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-186 — #23 - an end-state principle needs a lawful transition

> 23. **End-state principles need lawful transitions.** When a planned change must temporarily
>     violate an end-state principle (e.g. #6, one path per concern, during a parallel build),
>     the violation is declared, bounded, and pre-ratified with a retirement map — migration is
>     a first-class state, never an undeclared exception.

**In plain words.** When a planned piece of work must temporarily break a principle that describes the finished state - such as building a second analysis path beside the first - the breach is declared, bounded, and approved in advance together with the plan for removing it.

**Why.** Stated constraint, CLAUDE.md:73-74: migration is a first-class state, never an undeclared exception - the alternative being a temporary duplicate that nobody is obliged to remove. The instance is open_items/OI-180, the sanctioned dual path.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:71`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:71-74; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-187 — #24 - every reported figure carries its uncertainty

> 24. **Every reported figure carries its uncertainty.** Sampling noise on the measurement
>     corpus is quantified; a difference within the uncertainty is not a finding, and no
>     decision rests on one. (The companion of #16: reproducibility bounds instrument error,
>     this bounds sampling error.)

**In plain words.** How much a measured number could move by chance, given how much music it was measured on, is quantified and reported with it. A difference inside that range is not a finding and no decision may rest on one.

**Why.** Stated constraint, CLAUDE.md:77-78: this is the companion of #16 - reproducibility bounds the error the measuring tools introduce, and this bounds the error the sample introduces.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:75`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:75-78; ratified by the user 2026-07-18 (CLAUDE.md:125-129).

### D-188 — The constrained-optimum ledger corollary

> *Ledger corollary to #17 (ratified with #20–#24):* when a decision selects a **constrained
> optimum** (a design chosen for methodology-compliance rather than raw measured performance),
> the ledger records what the unconstrained best known alternative is and why it is excluded —
> so a future reader can re-test whether the constraint still binds.

**In plain words.** When a design is chosen because it complies with the method rather than because it measured best, the record must name what the best-performing alternative actually was and why it is ruled out.

**Why.** Stated constraint, CLAUDE.md:82-83: so that a future reader can re-test whether the constraint still binds - without the excluded alternative on record, a constraint that has since been lifted is invisible.

**Status.** LIVE · decided 2026-07-18 · ratified by user

**Home.** `CLAUDE.md:80`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:80-83; ratified with #20-#24 by the user 2026-07-18 (CLAUDE.md:125-129).

### D-189 — The scope of surprise, and the three-stage funnel

> *Scope of surprise (ratified with #17–19):* surprises are **allowed in explorational runs**
> whose purpose is to eliminate ignorance (#5 fact-finding); they are **NOT allowed when building
> actual inference code** — there, a surprise is a STOP (#13) and evidence the Premise Gate was
> not satisfied. The stage funnel: **desk-simulate (hours) → read-only probe (a session) → build
> (an arc)** — each stage kills bad premises before the next pays for them.

**In plain words.** Being surprised is allowed - expected, even - in exploratory work whose whole purpose is to remove ignorance. It is not allowed while building the analysis itself: there a surprise stops the work and shows the Premise Gate was not satisfied. The order of work is: trace it by hand for hours, then probe it read-only for a session, then build it.

**Why.** Stated constraint, CLAUDE.md:89: each stage kills bad premises before the next one pays for them - the funnel is ordered by what a wrong premise costs at that stage.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `CLAUDE.md:85`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:85-89; ratified with #17-#19 by the user 2026-07-10 (CLAUDE.md:122-125).

### D-190 — The decision-neutrality corollary - what exists carries no weight in choosing a design

> *Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified
> 2026-07-26):* Designs are chosen from the principles and the ultimate objective — enabling the
> best possible inference — alone. In that choice: **(a)** the value of reusing existing code, and
> the cost of making existing code obsolete, are SECONDARY — they may break ties between designs
> equal under the principles and the objective, and reuse counts only as carried-forward
> establishment (#19), never as sunk cost or saved effort; **(b)** downstream implementation
> impact — whether and how many consumers must change — carries NO weight; **(c)**
> end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling),
> while every behavior change remains ratification-gated (#14) and verification-gated (#15/#19)
> exactly as before. The best-possible-inference design is chosen first; what exists then either
> serves it or retires. (This does not weaken #6 — one path per concern is an END-STATE structural
> principle, not a preservation claim for the existing path; nor #19 — establishment must still
> exist before trust.)

**In plain words.** A design is chosen on the principles and the goal of the best possible analysis, and on nothing else. What it would cost to make existing code obsolete is a secondary consideration that can only break a tie between designs already equal; how many places downstream would have to change counts for nothing; and a change in what the user sees counts for nothing either - though every such change still needs ratifying and verifying exactly as before. The best design is chosen first, and what exists then either serves it or is retired.

**Why.** Stated constraint, CLAUDE.md:110-111 and :116-118: reusing existing code counts only as establishment already carried forward (#19), never as effort saved or cost sunk; and the corollary is explicitly said not to weaken #6 - one path per concern is an end-state structural principle, not a claim that the existing path is the one to preserve.

**Status.** LIVE · decided 2026-07-26 · ratified by user

**Home.** `CLAUDE.md:106`  — a project-wide convention with no owning layer; this is its correct home.

**Provenance.** CLAUDE.md:106-118; user-ratified 2026-07-26 at the notation-layer adoption increment's decision surface, analysis `cowork_notation_adoption_increment.md` §2 (CLAUDE.md:129-131).


## Group C — Cross-cutting analysis contracts

### D-191 — The two-tier regression class policy - functional regression stops, rotation churn is tracked

> **Two-tier refinement (user-ratified 2026-06-22) — class-(b) functional regression vs class-(a)
> symmetric-rotation churn.** A *new* BIR=false case is one of two classes:
> - **Class (b) — functional/key regression: UNCHANGED HARD STOP.** A new BIR=false case at a sonority
>   whose root is *pitch-class-decidable* (any non-symmetric chord — triads, dominant sevenths, etc.)
>   where the analysis now gets the root or key wrong. **Zero** new class-(b) cases on any preset, ever.
>   This is the gate's real intent and does not move.

**In plain words.** A newly wrong reading is one of two kinds. If the chord's root is decidable from the notes at all - any ordinary triad or seventh chord - and the analysis now gets the root or the key wrong, that is a functional regression and it is an absolute bar: never one more of them, on any style preset. The other kind is a sonority whose root the notes genuinely cannot decide - a symmetric diminished seventh, an augmented chord, a chord that shares all its notes with another - where no reading is more correct than another by pitch alone. Those are counted and watched, not barred.

**Why.** Stated constraint, CLAUDE.md:409-414: the pitch-class analyzer is spelling-blind and cannot pick the spelling-correct rotation of a symmetric chord, so counting a rotation flip as a regression would be counting a coin-flip. Measurement bounding the split: on the robust unit the decidable-root class is about 96.5 % of root-fail time (CLAUDE.md:379-382), so the hard stop governs almost all of it. Founding evidence, verified at the score against music21 ground truth: bwv272@4320, bwv289@20160, bwv291@17760, bwv387@10560 (CLAUDE.md:428-431).

**Status.** LIVE · decided 2026-06-22 · ratified by user

**Home.** `CLAUDE.md:403`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:394-437, block (B), carried over unchanged to the robust unit at R10-b. Full provenance `cowork_gate_policy_amendment.md`. The four guardrails that make the tracked class conditional - verified at the score per case, default to the barred class on any doubt, the barred class non-increasing, case identities recorded - are at CLAUDE.md:415-424.


## Group K — Documentation governance

### D-192 — A scoring change and its documentation land in the same commit

> **Sync rule — mandatory:** Any commit that adds or modifies a template, bonus,
> guard, gate, or other scoring term in `chordanalyzer.cpp` **must** include a
> corresponding update to `docs/scoring_model.md` in the same commit. The two
> must never drift apart. Specifically:
>
> - Adding a template: update the Templates section (§2), increment the template
>   count in the array-size comment, add the guard description if applicable
> - Adding or changing a bonus/gate: update the relevant §4 or §6 entry
> - Adding a new constraint or dead end: add it to §8

**In plain words.** Any commit that adds or changes a template, bonus, guard, gate or other scoring term in the chord analyzer must carry the matching update to the scoring-model document. They may never drift apart.

**Why.** Stated constraint, CLAUDE.md:576-581: violating the scoring model's invariants without reading it first has caused several failed attempts, named in the record - the leading-tone ambiguity attempt, four attempts at one bonus, and a rotation-selector bypass. The staleness check is mechanical: the template count in the document must equal the array size in the code (CLAUDE.md:593-596).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `CLAUDE.md:583`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:572-611. The document itself is `docs/scoring_model.md`.

### D-193 — The writing standards live in one place, and predicates must be qualified

> - **THE WRITING STANDARDS LIVE IN `cowork_design_doc_template.md` — read it before writing any
>   specification, design document, decision surface, or anything presented to the user.** Two
>   standards: **predicates must be qualified** (user, 2026-06-24 — every two-place word names its
>   argument; the mechanical check is to force the word to be followed by the thing it points at,
>   and a phrase the prose cannot supply is a hole), and **defined terms, plain vocabulary, no
>   shorthand** (user, 2026-07-02 — a terms table with nothing used before its row; no invented
>   synonyms; no insider compression, a jargon handle only after its rule has been stated; inherited
>   prose audited as hard as new). That file also carries the fourteen-section document structure,
>   the status-banner convention, and the implementation/test locator rule. It is the ONE home for
>   writing standards; the entry below sharpens its rule 5 and does not replace it (#6).

**In plain words.** Anything written as a specification, a design, a decision surface, or for the user follows two standards. Every word that relates two things must name the second one - the check is to force the word to be followed by the thing it points at, and a phrase the prose cannot supply is a hole in the thinking. And terms are defined before use, in plain vocabulary, with no invented synonyms and no insider shorthand.

**Why.** Stated constraint, CLAUDE.md:750-751: inherited prose is audited as hard as new prose, so the standard is about the document a reader meets rather than about who wrote which sentence. The one-home rule is #6 applied to the standards themselves (CLAUDE.md:752-753).

**Status.** LIVE · decided 2026-07-02 · ratified by user

**Home.** `CLAUDE.md:744`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:744-753; predicate qualification user-directed 2026-06-24, defined terms user-directed 2026-07-02. The ONE home is `cowork_design_doc_template.md`, which also carries the fourteen-section document structure, the status-banner convention and the implementation/test locator rule. Conformance of the existing tree is open at OPEN_ITEMS OI-230.

### D-194 — No self-invented labels, abbreviations, numbering schemes or jargon

> - **No self-invented labels, abbreviations, numbering schemes, or jargon** — in documents,
>   register rows, commit messages, and conversation alike. Use the name a thing already has
>   in the repository; if it has none, describe it in plain words. (User-directed, repeatedly;
>   recorded 2026-07-11.)

**In plain words.** A thing is called by the name it already has in the repository. If it has none, it is described in plain words rather than given a coined label - in documents, rows of the open-items register, commit messages and conversation alike.

**Why.** derivation not recorded.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:740`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:740-743, user-directed repeatedly and recorded 2026-07-11.

### D-195 — Every design decision carries its defense at its home

> - **EVERY DESIGN DECISION CARRIES ITS DEFENSE AT ITS HOME (user-directed, 2026-08-01, at the
>   decisions-register ratification review).** Wherever a design decision is recorded — the owning
>   layer's specification in `ARCHITECTURE.md` first — the record states WHY the decision was made:
>   the published research or algorithm adopted (#1/#2), the measurement that decided it, or the
>   constraint that forced it. Every design decision must be defendable, and its defense documented
>   where the decision lives. This generalizes `ARCHITECTURE.md` §17.2 (every non-obvious scoring
>   weight or threshold must explain its musical reasoning) from scoring values to design decisions
>   as a class. The decisions register (`DECISIONS.md`) points at the defense; where a decision's
>   derivation is not in the record, the register says **"derivation not recorded"** — the gap is
>   stated, never filled in retroactively from memory (a defense written after the fact without a
>   source is invention, and the never-work-from-memory rule forbids it). Founding instances of the
>   gap: the decode segment cap's value (4), the legacy 16-beats-back/8-forward window, the
>   boundary-tick-belongs-to-the-segment-it-starts convention — each recorded with no derivation.

**In plain words.** Wherever a design decision is written down - the owning layer's specification first - the record says WHY: the published research or algorithm it adopts, the measurement that decided it, or the constraint that forced it. Every design decision must be defendable and its defense written where the decision lives. Where the record has none, the decisions register says 'derivation not recorded' rather than supplying one afterwards.

**Why.** Stated constraint, CLAUDE.md:801-802: this generalizes ARCHITECTURE.md §17.2 - every non-obvious scoring weight or threshold must explain its musical reasoning - from scoring values to design decisions as a class. The reason the gap is stated rather than filled: a defense written after the fact without a source is invention, which the never-work-from-memory rule forbids (CLAUDE.md:805-806).

**Status.** LIVE · decided 2026-08-01 · ratified by user

**Home.** `CLAUDE.md:796`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:796-808, user-directed 2026-08-01 at the decisions-register ratification review. The register's rationale field is what serves it; the founding instances the entry names are D-004's segment-cap value, D-059's window and D-015's boundary-tick convention.


## Group T — Standing process rules and local patches

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

**Why.** Stated constraint, CLAUDE.md:818-819: the check is of the work actually on disk, not of the intention - read the difference, not the memory of writing it. Which is the same reasoning as the never-work-from-memory rule, applied to one's own output.

**Status.** LIVE · decided 2026-07-11 · ratified by user

**Home.** `CLAUDE.md:812`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:810-819, user-directed 2026-07-11. Binds Claude Code and Cowork sessions alike.

### D-197 — The distribution constraint - the import-fix patch is fork-local and never goes upstream

> **★ DISTRIBUTION CONSTRAINT (user, 2026-06-15): FORK-LOCAL ONLY — NEVER merge upstream / to the
> MuseScore community.** This patch (`cfc7eb5e39`) is fine to have in the **central repo = the user's
> fork** (`origin` = `slimvince/MuseScore`) and may be pushed there, but it must **NEVER** be pushed or
> merged to `upstream` (`musescore/MuseScore`) or otherwise contributed to the MuseScore community.
> `upstream` push is disabled in this repo; keep it so. Any future push/PR/merge that would carry
> `cfc7eb5e39` (or its content) toward `musescore/MuseScore` is a HARD STOP — surface, do not proceed.
> (The #9444 reference above is the upstream *bug report*; it does NOT authorize contributing THIS patch.)

**In plain words.** The MusicXML mode-import fix may live in the user's own fork of MuseScore and be pushed there. It must never be pushed, merged or otherwise contributed to the MuseScore project. Any action that would carry it toward the upstream repository stops work and is reported.

**Why.** Stated constraint, CLAUDE.md:685: the upstream issue number cited beside the patch is the upstream BUG REPORT, and referencing it does not authorize contributing this patch. Upstream pushing is disabled in the repository and is to be kept so (:683-684).

**Status.** LIVE · decided 2026-06-15 · ratified by user

**Home.** `CLAUDE.md:679`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:679-685, user-directed 2026-06-15. ★ READ WITH the general contribution intent at ARCHITECTURE.md:328-330 - two recorded positions, a general intent to contribute and a named one-patch exception; the record does not state how the general intent applies to the rest of the tree.

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

**Why.** Stated constraint, CLAUDE.md:634-641: the removed lines set the minimum window size to the full monitor work area, which is what blocked snapping; the maximised-position constraints are correct and are kept. Upstream issue musescore/MuseScore#25823, introduced by upstream commit 4ad218709 (:643-644).

**Status.** LIVE · decided 2026-05-14 · ratified by user

**Home.** `CLAUDE.md:631`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:629-645, applied 2026-05-14. Unrelated to the composing module; recorded so a dependency update does not silently overwrite it.

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

**Why.** Measurement, CLAUDE.md:668-671: the change is verified isolated to empty-signature scores - exactly 79 zero-signature analyses changed and no non-empty-signature piece moved - the regression gate is byte-identical on all three presets, and the round-trip of a zero-signature minor piece now preserves its mode. The underlying defect is upstream-unchanged code whose own comment flags the check as known-incomplete (CLAUDE.md:661-662, :673-674).

**Status.** LIVE · decided 2026-06-14 · ratified by user

**Home.** `CLAUDE.md:652`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** CLAUDE.md:647-677, applied 2026-06-14, commit cfc7eb5e39. ★ Carries the distribution constraint above: fork-local only, never upstream.


## Group S — The guiding principles

### D-200 — Make it work first; compromise on performance only if performance proves a problem

> The user's actual rule: **make it work first (best inference), compromise on performance only if
> performance proves to be a problem.** That does not demote runtime speed; it sequences it — and
> it means work that makes the same computation faster costs nothing on any principle axis and must
> be exhausted BEFORE anything that trades precision for speed. The effort dial and the extent
> question are **last resorts, not first ones**.

**In plain words.** Getting the analysis right comes first. Speed is traded against it only once slowness has actually turned out to be a problem. That does not make speed unimportant - it puts it second: anything that makes the same computation faster is free on every principle and is done first, and the settings that buy speed by giving up precision are the last resort, not the first.

**Why.** Stated constraint, cowork_handoff.md:361-364: work that makes the same computation faster costs nothing on any principle axis, so it must be exhausted BEFORE anything that trades precision for speed - which is what sequences the effort dial and the analysis-extent question last rather than demoting them.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `cowork_handoff.md:360`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:358-364, the user's rulings at the analysis-cost session, 2026-07-28; recorded again as a standing rule at cowork_handoff.md:227-228. It corrects a Cowork misreading of 'implementation efficiency is not very relevant', which meant BUILD effort, not runtime.

### D-201 — Very large scores must be handled, and are expected to be more common than our corpora

> User-directed 2026-07-28, in the user's words: very large scores MUST be handled and are expected to be a MORE COMMON use case than our corpora. A STANDING DESIGN REQUIREMENT (not a defect) — every subsequent inference/notation design is judged against it.

**In plain words.** A Wagner act or a symphony must work. The user expects such scores to be a more common use than the chorales the system was fitted on. This is a standing requirement every later design is judged against, not a defect report.

**Why.** Stated constraint, OPEN_ITEMS.md:157: the requirement is recorded together with the collision it creates - the joint estimator's ratified tractability envelope is chorale size (60-150 events), and the fitted corpus is 326 Bach chorales by one composer.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `OPEN_ITEMS.md:157`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:157 (OI-209) with open_items/OI-209.md. Consumed by the analysis-extent question (OI-210), the corpus onboarding (OI-38), and the architecture step-back (OI-200). The measured collision is OI-215/OI-227 - the decode returns nothing on 13 of 23 committed large scores.

### D-202 — The effort control is one setting with several dials, and it must bound the time taken

> The effort control is ONE setting with several dials that must bound TEMPORALLY too; too early to implement until we know factually which parts must be switchable — which this dispatch's measurement establishes.

**In plain words.** How hard the analysis works is a single setting the user turns, not several. Behind it sit several dials, and among the things it must be able to bound is how long the analysis takes. It is too early to build: which pieces of the analysis have to be switchable is not yet known.

**Why.** Stated constraint, OPEN_ITEMS.md:157: it is too early to implement until we know FACTUALLY which pieces must be switchable - which is a measurement, and the measurement is what the analysis-cost dispatch was for. The user's recorded prediction beside it: 'always read the entire score will VERY likely not survive (maybe only under some effort setting = EXTREME)'.

**Status.** DEFERRED · decided 2026-07-28 · ratified by user

**Home.** `OPEN_ITEMS.md:157`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:157 (OI-209). The two standing design rules the effort dial must satisfy are older and are in the architecture document (D-035, ARCHITECTURE.md:739-741): every cost-driving choice is a setting, and every optional expensive refinement is cleanly separable.

### D-203 — Candidate admission is completion, not refinement - so #8 permits fixing it now

> **The fix is DEFERRED BY
> DESIGN** until the whole family is known — the user ruled candidate admission is COMPLETION (not
> refinement, so #8 permits it)

**In plain words.** The rule that decides which chords the decoder will even consider is not a refinement of something already built - it is a piece that was never finished. So the principle that forbids chasing visible analysis errors before the structure is complete does not block fixing it.

**Why.** Stated constraint, cowork_handoff.md:31-32: the design happens ONCE over the whole family, never per symptom (#6/#7) - which is why the fix is deferred until the family is enumerated even though #8 permits it. The measured family: OI-215 (the sparse member-overlap gate), OI-227 (the dense fit gate), OI-226 (admission has no ratified basis), OI-228 (the emission reads struck rather than sounding notes).

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `cowork_handoff.md:29`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:26-32, the user's ruling recorded at the OI-199 pass-2 session. Cross-read with STATUS.md's earlier note that the classification 'is the user's to settle' - this row records that it was settled.

### D-204 — One fix is designed once over the whole enumerated family, never per symptom

> but the design happens ONCE over the family, never per symptom
> (#6/#7).

**In plain words.** When several observed faults turn out to share a cause, the remedy is designed once for all of them together. Fixing whichever one is currently visible, on its own, is the error the one-path-per-concern and layer principles exist to prevent.

**Why.** Stated constraint, cowork_handoff.md:28-29 and #3: the fix is deferred BY DESIGN until the whole family is known, because designing over part of a family is the patch-per-symptom error. The instance that produced the rule: the empty-decode cliff turned out to have a sibling at the opposite end of the density spectrum (OI-227) and an emission-side twin (OI-228), neither visible from the first symptom.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `cowork_handoff.md:31`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** cowork_handoff.md:28-32, recorded at the OI-199 pass-2 session, 2026-07-28.

### D-205 — A human acts as ground truth where no formal ground truth exists

> a HUMAN acts as ground truth where no formal ground truth exists** — the human decides by any method they choose, INCLUDING using the triage judge as guidance. So the judge lands eventually as a guidance instrument for the human-as-ground-truth workflow (never a grader, never a graded number); the branch is preserved until then.

**In plain words.** For music nobody has published an analysis of, the reference answer is a person's judgment. They may reach it however they like, including by letting an automated judge point them at the passages most likely to be wrong. That judge is guidance for the human, never a grader and never a number we report.

**Why.** Stated constraint, open_items/OI-56.md:7: a language-model judge is not ground truth (#9, and the standing rule that music21 corroborates but does not adjudicate), so it could never grade us - at most it can triage, by pointing a human at the scores most likely wrong.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `open_items/OI-56.md:7`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-56.md:7, decided by the user 2026-07-13. The when-question is tied to the corpus-onboarding event (OI-38) and the timing is itself open.

### D-206 — Intonation is held as a future feature, and is a declared future consumer of the analysis

> KEEP HELD — intonation IS a future feature** (the six §11.3 items + the tie limitation stay as a deliberate long-horizon hold, revisited at a natural pause in the analysis work). **AND the user stated the dependency that makes the hold strategic, recorded here and in the evidence inventory: the intonation feature will CONSUME the analysis facts** — knowing mode/chord/chord-function/progression enables just-intonation tuning decisions, especially in the TIME dimension (stay in tune over time vs allow drift) — i.e., intonation is a declared FUTURE CONSUMER of the published analysis surfaces, a concrete instance of the publish-evidence-broadly rationale.

**In plain words.** The six unbuilt pieces of the tuning design stay on the books as a deliberate long-horizon hold, revisited at a natural pause in the analysis work. The reason the hold is strategic rather than neglect: tuning will read the analysis - knowing the mode, the chord, its function and the progression is what lets a just-intonation decision be made, particularly the decision about staying in tune over time versus letting the pitch drift.

**Why.** Stated constraint, open_items/OI-62.md:7: intonation is a named future CONSUMER of the published analysis surfaces - a concrete instance of the rule that evidence is published broadly so a future design can recognize facts it would never have thought to ask for (D-100's 2026-07-12 amendment).

**Status.** DEFERRED · decided 2026-07-13 · ratified by user

**Home.** `open_items/OI-62.md:7`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-62.md:7, decided by the user 2026-07-13. The six unbuilt items are specified at ARCHITECTURE.md §11.3a-g and confirmed absent from the code in the row.


## Group G — Layer 4 — chord identity

### D-207 — The pedal-point class is defined voice-independently, superseding the bass-only fact

> the ornament vocabulary includes the PEDAL-POINT class defined VOICE-INDEPENDENTLY — a tone sustained (or continuously restruck) against changing harmony in ANY voice, sub-labeled by position (bass / internal / inverted) — superseding the legacy BASS-ONLY `isPedalPoint`/`pedalBassPc` fact

**In plain words.** A pedal point is a note held - or struck again and again - while the harmony changes around it, in ANY voice, not only the bass. It is labelled by where it sits: in the bass, inside the texture, or above it. This replaces the older fact, which could only see a pedal in the lowest voice.

**Why.** Stated constraint, open_items/OI-194.md:7: the legacy fact was produced by an unestablished post-pass and retires with the legacy path; the voice-independent class comes from the emission's own non-chord-tone categories, which do not privilege the bass. Two unresolved audit rows are recorded as dispositioned by this ruling.

**Status.** DEFERRED · decided 2026-07-26 · ratified by user

**Home.** `open_items/OI-194.md:7`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-194.md:7, sharpened at the P1 pedal-point ruling, user-ratified 2026-07-26 at the consumption-audit verification (`cowork_notation_adoption_increment.md` §7 + §10). DEFERRED: it lands with the ornament-label publication, its own increment after the notation switch; until then the record arm leaves the pedal fields empty (D-021) and the 'X ped.' annotation is a declared gap.


## Group T — Standing process rules and local patches

### D-208 — A withheld finding never enters a mandatory session-start read

> Remedy (OI-89 generalized): cross-check every required read + the dispatch body against every withholding requirement; keep §S in a separate post-freeze artifact; do not headline the withheld findings in a mandatory blind-pass read.

**In plain words.** When a review is run blind - deliberately keeping a finding from the reader so that whether they rediscover it measures the review's power - that finding must not appear in any document the reader is required to open at the start. The status file carries a pointer; the content lives in a separate artifact opened only afterwards.

**Why.** Measurement, OPEN_ITEMS.md:170: the rule was written because the blinding was defeated at the source - the mandatory status-file read carried the full text of all three sealed findings, and the dispatch delivered them inline as well. The consequence recorded there: the reconciliation could no longer claim knowledge-free discovery, only that the artifacts point at each mechanism on their merits.

**Status.** LIVE · decided 2026-07-28 · ratified by user

**Home.** `OPEN_ITEMS.md:170`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:170 (OI-222) with open_items/OI-222.md; restated as a standing rule at cowork_handoff.md:230. Generalizes the earlier OI-89 instance of the same shape.

### D-209 — Code that is about to be deleted gets no audit - only the no-information-loss check at deletion

> (a) PARTITION the module by the retirement map R1–R9 — code that RETIRES at E4 gets NO audit, only the #12 interpretation-check at deletion (A1 verdict)

**In plain words.** Before auditing the system exhaustively, the code is split into what survives and what is scheduled for removal. What is scheduled for removal is not audited at all. The only thing owed to it is a check, at the moment it is deleted, that nothing it knew is lost.

**Why.** Stated constraint, OPEN_ITEMS.md:60: the alternative form - audit whatever you happen to touch - was rejected by the user as risky, because touching one per cent would audit one per cent while new work built on the unaudited rest, which is itself a violation of the no-unverified-premises principle across the whole architecture. ★ The rule's own boundary is recorded too: at cowork_handoff.md:368-369 the user ruled it does NOT shield the joint module, which is production on both surfaces and is not retiring.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `open_items/OI-84.md:7`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** open_items/OI-84.md:7 (OI-84), corrected 2026-07-10 at the user's challenge. The plan it belongs to is complete: every surviving layer certified on two passes each.


## Group C — Cross-cutting analysis contracts

### D-210 — An exotic mode is graded against its parent collection's minor key, not its own tonic triad

> the parent-collection reduction ruled by the user + landed (800f1a12bf), key columns moved as predicted, root byte-identical; the two value-copies mechanically pinned

**In plain words.** When the analysis emits one of the five dominant-family exotic modes, grading reduces it to the MINOR key of the collection it belongs to - an emitted C-sharp Phrygian dominant is graded as F-sharp minor, the key it is the dominant of - rather than to the key its own tonic triad would name.

**Why.** Measurement, CLAUDE.md:342-347: on the affected duration the parent-collection reading agrees with the published annotators on 67 % of the local key column, and the tonic-triad reading on 0 %. The consolidation moved only the key columns - root, Roman numeral, every root-failing run set and the hard-stop duration were byte-identical, run-difference +0/-0 on all presets.

**Status.** LIVE · decided 2026-07-13 · ratified by user

**Home.** `OPEN_ITEMS.md:225`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:225 (OI-132), ruled by the user 2026-07-13 and landed at 800f1a12bf. The adjudication probe is `cc_mode_grading_adjudication_probe_report.md`; the re-baseline record is `cc_key_grading_and_calibration_rebaseline_report.md`. It is implemented in ONE shared reduction, `compare_rn._our_key_tonic`, onto which the second key parser was folded (#6).

### D-211 — Key agreement is reported against both the global home key and the local key

> Grade the key-agreement column against BOTH the DCML global (home) and local key, both carried everywhere the key column appears. | measurement | ✅ RESOLVED 2026-07-12 (adoption d9b52ba969) — the dual column landed; local < home (the analyzer tracks the tonal home more faithfully); both views kept

**In plain words.** There are two defensible questions about a key reading - does it match the key the piece is in, and does it match the key this passage is in - and the record carries both numbers everywhere the key column appears, rather than choosing one.

**Why.** Measurement, OPEN_ITEMS.md:253: the local figure is lower than the home figure, which is itself the finding - the analyzer tracks the tonal home more faithfully than it tracks momentary tonicizations - so keeping only one column would have hidden a real property of the system.

**Status.** LIVE · decided 2026-07-12 · ratified by user

**Home.** `OPEN_ITEMS.md:256`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:256 (OI-143), adopted at d9b52ba969. The current values are in the CLAUDE.md gate block (A): key-agree against the home key 56.14 %, against the local key 78.42 %.

### D-212 — The regression stop is abstain-aware: an abstention counts as disagreement on root

> convention written + mechanically enforced (root counts an abstain as disagreement; key-agree excludes abstained cells; robust_stop_diff flags an abstain rise

**In plain words.** If the analysis declines to name a chord root, that counts as getting it wrong, so declining more often can never look like improving. On the key axis the declined cells are excluded from the percentage instead, and a rise in declining trips a flag in the comparison tool.

**Why.** Stated constraint, OPEN_ITEMS.md:200: the metric is abstention-reducible - without the convention, a change that made the system decline more would raise the agreement figure without analysing anything better - and the convention was owed before any abstaining path could be gated on the stop at all.

**Status.** LIVE · decided 2026-07-12 · ratified by user

**Home.** `OPEN_ITEMS.md:203`  ⚠ **recorded only on a tracking surface** — an open-item row or a session handoff block, neither of which is a home for a standing decision; see `OPEN_ITEMS.md`.

**Provenance.** OPEN_ITEMS.md:203 (OI-33), resolved 2026-07-12 in the key-layer readiness wave 1. Its current reading on the production arm is D-114 - the decoder commits its best path, so the abstain counter reads zero.


## Group U — The standing decision-bearing surfaces

### D-213 — The defect-type catalog is the living list of every problem type, and it is added to at discovery

> **Created 2026-07-10 (session 36), user-directed.** The second half of the audit protocol
> (`cowork_audit_protocol.md` P7/P8): every problem TYPE ever discovered in this project, each
> with its detection signature — mechanical where possible. **Standing rule (mirrors the
> OPEN_ITEMS rule): every newly discovered problem TYPE gets a catalog entry in the same
> commit that records its discovery.** Types are never removed; a type made impossible by a
> structural fix is marked NEUTRALIZED with the mechanism that kills it (the kTemplateCount
> precedent). IDs are stable.

**In plain words.** Every kind of problem ever found in this project has an entry saying what it is, the case that first showed it, and how to detect it - mechanically wherever possible. A newly discovered kind of problem gets its entry in the same commit that records the discovery. Entries are never deleted: a kind of problem that a structural change has made impossible is marked as such, with the mechanism that kills it.

**Why.** Stated constraint, DEFECT_TYPES.md:8-9: keeping a neutralized type on the list, with the mechanism that killed it, is what stops the same defect being reintroduced by a later change that removes the mechanism. The named precedent is the template-count constant, which closed a silent buffer overrun by making the compiler enforce the sizes.

**Status.** LIVE · decided 2026-07-10 · ratified by user

**Home.** `DEFECT_TYPES.md:3`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** DEFECT_TYPES.md:3-9, user-directed 2026-07-10. It is the second half of the audit protocol; the standing rule mirrors the open-items register's rule (c). The catalog is one of the four surfaces the self-check reads (D-196).

### D-214 — The dim7 characteristic bonus is the rotation selector and may not simply be removed

> - **`dim7CharacteristicBonus` is the dim7 rotation selector.** Do not
>   suppress without replacing the non-diatonic-♭♭7 mechanism (B3 lesson).

**In plain words.** The bonus that makes a diminished-seventh chord prefer one rotation over another is what selects the rotation. Removing it without putting an equivalent mechanism in its place breaks the choice.

**Why.** Measurement named in the record: the B3 lesson - an attempt that suppressed it and had no replacement for the non-diatonic double-flat-seventh mechanism.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:912`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-215 — Gating the root-continuity bonus on a sparse predecessor is a dead end

> - **`rootContinuityBonus` sparse-predecessor gate is a dead end** (Iter 98).
>   Both density-based and inversion-aware variants tried; both regress
>   mozart_k280-1 IV→V65 Alberti bass.

**In plain words.** Making the bonus that rewards keeping the same root depend on how much evidence the previous chord had was tried in two forms and abandoned.

**Why.** Measurement named in the record: both the density-based and the inversion-aware variants regress the same passage - a Mozart sonata movement's Alberti-bass progression from the subdominant to the dominant in first inversion.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:915`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-216 — The stepwise-bass bonus's four gates are each load-bearing

> - **`w_stepIn`/`w_stepOut` has four gates, each load-bearing** — the
>   `ScoringPhase::Final` call-site gate, root-position guard,
>   first-inversion-m7-family surgical guard, power-quality exclusion. Each prevents
>   a specific documented regression.

**In plain words.** The bonus for a bass moving by step is switched off in four situations, and each of the four is there because it prevented a specific regression that was actually observed.

**Why.** Measurement named in the record: each gate prevents a specific documented regression.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:919`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-217 — The segmentation phase must suppress every context-dependent bonus

>   seq, and dim bonuses plus Gate R are all skipped in the Segmentation phase (gated at
>   the `applyHarmonicFunction` call site, not inside the now-stateless bonus functions).
>   Adding a new context bonus without gating it on `applyProgressionSignals` /
>   `ScoringPhase::Final` will cause segmentation regressions.
>
> - **Template arrays update atomically under `analysis::kTemplateCount`.** All

**In plain words.** While the analysis is still deciding where one chord ends and the next begins, none of the bonuses that look at neighbouring chords may score anything. Adding a new context bonus without that gate will make the segmentation worse.

**Why.** Stated constraint: where a boundary falls decides which notes each candidate sees, and chord identity is itself a signal for where boundaries belong (ARCHITECTURE.md:641-644), so a context bonus scoring the exploratory passes lets the answer choose its own input. Its specification home is D-062.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:925`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-218 — Template array sizes derive from one constant, so the compiler enforces them

>   constant since `a236a0ff21`, so the compiler enforces sizes. Adding a template =
>   bump the constant + add the template/mask entries in the same edit (§9 step 5).
>   The historical silent stack-buffer overrun from a missed matrix size is closed.
>   (Stage 2.3 removed the `kDiagTemplates` mirror — one fewer site to keep in sync.)
>
> - **Gate A subsumed Gates B/C/D — now removed (Stage 3.4b, historical); Gate A itself
>   unified into `promoteToWinner`/FM2 (2026-07-06, §6a).** Gate A's entry conditions were a

**In plain words.** Every array whose length must equal the number of chord templates takes that length from a single named constant. Adding a template means changing the constant and adding the template in the same edit.

**Why.** Measurement named in the record: the historical failure was a silent stack buffer overrun from a missed matrix resize, caught during an attempted template addition; deriving the extents from the constant closes it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:932`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-219 — Gates B, C and D were unreachable and were removed; no temporal condition may be added to the enharmonic flip

>   removed in the Stage-3 per-gate retirement audit (roadmap 3.4b) as a byte-identical change
>   (0/353 × 3 configs, snapshots zero-diff). Gate A's swap later became the present branch of
>   the unified `promoteToWinner()` primitive under the FM2 rule (byte-identical, full surface).
>   Constraint going forward: do not add temporal conditions to the enharmonic flip — there is
>   no longer a B/C/D safety net; any forward/window/consecutive-stepwise variant of the
>   Major-add6 ↔ Minor flip must be reintroduced explicitly and tested.
>
> - **B2 aug7 guard requires BOTH M3 and aug5** (`||` not `&&`). M3-only was
>   tried and reverted (Schumann D-major, Corelli G-major snapshot flips).
>
> - **Gate thresholds are Baroque-calibrated.** Do not widen Baroque-tuned
>   thresholds to accommodate Jazz or other styles (see CLAUDE.md "Gate
>   threshold and preset policy"). Use a tighter structural guard or a
>   preset-specific override instead.

**In plain words.** Three post-scoring gates turned out to be unreachable, because the conditions of the gate before them were a strict subset of theirs, and they were deleted. The constraint that follows: nothing that depends on time or on neighbouring chords may be added to the major-with-added-sixth against minor flip, because the safety net those gates provided is gone.

**Why.** Measurement named in the record: the removal was proven byte-identical - 0 differences across 353 pieces in three configurations, with the snapshot tests showing no difference either.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:940`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-220 — The augmented-seventh guard requires both the major third and the augmented fifth

> - **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register
>   "bass" notes do not get inversion bonuses (Corelli op01n08d m2 b3).

**In plain words.** The guard fires only when both intervals are present, not when either one is. Requiring only the third was tried and reverted.

**Why.** Measurement named in the record: the either-one form flipped snapshots on a Schumann piece in D major and a Corelli piece in G major.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:955`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-221 — A sparse upper-register lowest note does not earn inversion bonuses

>   live `results[0]` reference (Sub-9a lesson).

**In plain words.** A low note that is thin and high in the texture is not treated as a structural bass, so the bonuses that reward a recognisable inversion do not fire for it.

**Why.** Measurement named in the record: a Corelli trio-sonata movement, measure 2 beat 3.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:964`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-222 — If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used

>   fires only when at least one tone has `onsetAtRegionStart == true` or
>   `distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).
>   Single-tick / status-bar / unit-test paths use the legacy single-bass path.

**In plain words.** The bonus that favours diminished readings can, in the course of comparing bass notes, end up electing a winner that is not diminished at all. When that happens the analysis falls back to the answer it had before the bonus was applied.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:967`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-223 — A gate that judges the pre-correction winner reads a snapshot, not the live result

> ---
>
> ## 9. How to add a new template safely (checklist)

**In plain words.** Where a gate has to compare against whatever the analysis thought before a correction was applied, it reads a copy taken beforehand rather than the current top result, which the correction may already have changed.

**Why.** Measurement named in the record: the lesson came from a specific numbered attempt in which the live reference had already moved.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:971`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-224 — Joint bass-and-chord scoring requires accumulated regional evidence

> Derived from the B1, B2, and B3 lessons.
>
> 1. **Read the existing template nearest to yours.** Understand its intervals,
>    TPC deltas, and which existing terms / guards apply to it.

**In plain words.** The scoring that considers the bass note and the chord together only switches on when the notes came from accumulating a whole stretch of music. The single-moment paths - the status bar, a unit test - use the simpler single-bass scoring.

**Why.** derivation not recorded.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `docs/scoring_model.md:975`

**Provenance.** docs/scoring_model.md:907-979 (§8, known constraints and dead ends), whose own opening states that these are load-bearing design decisions future changes must respect. No date or ratifier stated per entry.

### D-225 — A corpus is regenerated before its baseline figures are updated

> **IMPORTANT — corpus JSONs must be regenerated before updating baselines.**
> `analyze_inversion_errors.py` reads existing `.ours.json` files and will silently
> report stale numbers if those files are not current. Whenever you update the BIR
> baselines here, you must first regenerate the corpus (as above), then run the script
> against the per-preset dir and record the new figures.

**In plain words.** The measurement scripts read files produced by an earlier run. Updating a recorded baseline without regenerating those files first produces a number that silently describes an older state of the system.

**Why.** Stated constraint, BUILD_AND_TEST.md:286-287: the script reads existing analysis files and will silently report stale numbers if they are not current - silently being the operative word, since nothing about the output reveals it.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `BUILD_AND_TEST.md:285`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** BUILD_AND_TEST.md:285-289. The mechanical enforcement is the per-preset corpus manifest: the regeneration script exits nonzero on an incomplete corpus and the measurement refuses a directory whose manifest is missing or whose fingerprints do not match (CLAUDE.md:465-476).

### D-226 — The music21 export is version-pinned; regenerating it is a deliberate re-baseline

> **music21 version pin (audit C2):** the committed `tools/corpus/*.xml` were
>   exported by **music21 v.9.9.1** (recorded in each file's
>   `<software>music21 v.9.9.1</software>` / `<encoding-date>2026-04-05</encoding-date>`
>   tag), and the paired `*.music21.json` ground truth is from the same generator.
>   Regenerating with a different music21 is a **deliberate re-baseline** of the
>   BIR denominators, not a refresh. `run_bach_preset.py` now copies the
>   detected music21 version into each `corpus_manifest.json` (`music21_version`,
>   informational — not validated).

**In plain words.** The committed corpus files and the paired corroborating analyses were produced by one specific version of music21, recorded inside the files themselves. Regenerating them with a different version is not a refresh - it moves the denominators every agreement figure is measured against, and is treated like updating a golden reference.

**Why.** Stated constraint, tools/REPRODUCIBILITY.md:148-152: the committed corroborating analyses are canonical as committed, and regenerating them with ANY version shifts the denominators - so the event is coordinated rather than allowed to happen incidentally. This is the reproducibility principle (#16) applied to a third-party tool.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `tools/REPRODUCIBILITY.md:139`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** tools/REPRODUCIBILITY.md:139-155, recorded as audit finding C2. The pinned version is 9.9.1, enforced in `tools/music21_batch.py` (MUSIC21_PIN), which refuses to regenerate on a mismatch unless explicitly overridden. Note the asymmetry the record itself states: the version copied into each corpus manifest is informational and is NOT validated.


## Group I — Module boundaries and code structure

### D-227 — Read how MuseScore already does it, and never invent parallel infrastructure

> Before implementing anything that touches MuseScore's existing infrastructure —
> UI panels, score traversal, playback, settings, localization — read how MuseScore
> already does it and follow the same pattern. Do not invent parallel infrastructure.

**In plain words.** Before touching anything MuseScore already provides - panels, walking the score, playback, settings, translation - the existing MuseScore code for it is read and followed. A second, parallel mechanism of our own is never created.

**Why.** Derivation not recorded as a separate defense. Its consequences are recorded across the document and are what the rule buys: the panel infrastructure (§12.1), the localization path (§12.1), the accessibility patterns (§12.1), the coding style (§17.1), and the preview pathway (§10.5) all resolve by this rule rather than by separate argument.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:469`

**Provenance.** ARCHITECTURE.md:467-471 (§2.8). No date or ratifier stated. This is the GENERAL form of the relationship to existing MuseScore code; the two scoped forms are D-072 (the analysis library depends on no engraving type) and D-073 (shared logic has one implementation). What none of the three states is which MuseScore interfaces our bridge code may call - see OPEN_ITEMS OI-241.

### D-228 — The bridge pattern - engraving types enter and leave at named free functions in the notation namespace

> - Takes engraving types as input (Note*, Score*, Fraction, …)
> - Produces composing-domain results (ChordAnalysisResult, HarmonicRegion, …)
> - Lives in `mu::notation` namespace
> - Is declared in a `notation/internal/notation*bridge.h` header
> - Is defined in the corresponding `notation/internal/notation*bridge.cpp`
>
> **Callers** of bridge functions include only the notation-side bridge header, not composing headers, for the function itself. They may still include composing headers for the composing types in the function signature.

**In plain words.** The only code that may take MuseScore's own score objects and turn them into analysis results is a plain function living on the notation side, declared in a bridge header and defined in the matching bridge source file. Whoever calls it includes the bridge header, not the analysis headers, for the call itself.

**Why.** Stated constraint, ARCHITECTURE.md:958-962: the analysis library is pure music theory and can be unit-tested in complete isolation - no score, no staves, no interface - which is what makes its test suite fast and reliable. If analysis headers imported engraving types the tests would have to link the whole engraving library, and more fundamentally the music theory would carry knowledge of one particular score format, a coupling that makes the algorithms harder to reuse or replace.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:966`

**Provenance.** ARCHITECTURE.md:964-975 (§3.3, the bridge pattern), with the enforcement statement at :955 (D-072) - any code that would invert the dependency order must be moved to the bridge layer. The bridge file inventory at :977-985 is the as-built list. No date or ratifier stated.

