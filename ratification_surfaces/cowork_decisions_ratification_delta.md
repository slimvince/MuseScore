# The ratification delta — what changed in DECISIONS.md since the version the user reviewed

> **GENERATED REVIEW AID (Cowork, 2026-08-02).** The tables below are extracted mechanically from
> `tools/audit/decisions/backbone_decisions.json` (the register's source of record), never
> retyped. Purpose: `DECISIONS.md` (228 entries) no longer renders comfortably; the user reviewed
> and commented on the 115-entry version, whose review corrections are already applied. This file
> shows ONLY what has changed since that reviewed version, so ratification can proceed without
> re-reading the whole register. Drill into any entry by its D-number in `DECISIONS.md`.

## Part A — changes to the 115 entries you already reviewed

1. **A "Why." line was added to every entry** (your rationale directive, 2026-08-01): 183 of the
   full 228 populated from the record with citations; 45 honestly say "derivation not recorded."
   Nothing was invented after the fact.
2. **Your review corrections are in:** D-033, D-050 and D-100 plain restatements reworded exactly
   as discussed (ownership-not-evidence-restriction; the slicer-not-the-analysis; the
   EVIDENCE-class publication amendment included); **D-103 is now SUPERSEDED BY D-207** (the
   voice-independent pedal-point class you remembered — now its own entry); D-004's segment-cap
   value, D-015's boundary convention and D-059's window are flagged "derivation not recorded."
3. **17 of 53 provenance cross-references were re-aimed** (they pointed at the wrong open-item
   rows — the numbers had been guessed before the rows were numbered). A guard now verifies every
   reference resolves, so the class cannot recur.
4. **The home-warning marker was split into four honest categories:** documentation gap (8) /
   recorded only on a tracking surface (12) / project-wide convention correctly homed in
   CLAUDE.md (31) / process decision correctly homed (16). Previously one warning covered all four.
5. **No verbatim quote changed anywhere** — the quote-at-home check passes 228/228.


## Part B — the 113 NEW entries, by group (title + the plain-language restatement from DECISIONS.md)

Each entry below shows its title and its "In plain words" restatement exactly as DECISIONS.md
carries them; the verbatim quote, Why, and provenance are in DECISIONS.md under the same
D-number. Status and home in parentheses; "derivation not recorded" marks a Why the record
does not supply.


### C. Cross-cutting analysis contracts (4 new entries)

**D-191 — The two-tier regression class policy - functional regression stops, rotation churn is tracked.** A newly wrong reading is one of two kinds. If the chord's root is decidable from the notes at all - any ordinary triad or seventh chord - and the analysis now gets the root or the key wrong, that is a functional regression and it is an absolute bar: never one more of them, on any style preset. The other kind is a sonority whose root the notes genuinely cannot decide - a symmetric diminished seventh, an augmented chord, a chord that shares all its notes with another - where no reading is more correct than another by pitch alone. Those are counted and watched, not barred. *(LIVE 2026-06-22; CLAUDE.md)*

**D-210 — An exotic mode is graded against its parent collection's minor key, not its own tonic triad.** When the analysis emits one of the five dominant-family exotic modes, grading reduces it to the MINOR key of the collection it belongs to - an emitted C-sharp Phrygian dominant is graded as F-sharp minor, the key it is the dominant of - rather than to the key its own tonic triad would name. *(LIVE 2026-07-13; OPEN_ITEMS.md)*

**D-211 — Key agreement is reported against both the global home key and the local key.** There are two defensible questions about a key reading - does it match the key the piece is in, and does it match the key this passage is in - and the record carries both numbers everywhere the key column appears, rather than choosing one. *(LIVE 2026-07-12; OPEN_ITEMS.md)*

**D-212 — The regression stop is abstain-aware: an abstention counts as disagreement on root.** If the analysis declines to name a chord root, that counts as getting it wrong, so declining more often can never look like improving. On the key axis the declined cells are excluded from the percentage instead, and a rise in declining trips a flag in the comparison tool. *(LIVE 2026-07-12; OPEN_ITEMS.md)*


### G. Layer 4 - chord identity (1 new entries)

**D-207 — The pedal-point class is defined voice-independently, superseding the bass-only fact.** A pedal point is a note held - or struck again and again - while the harmony changes around it, in ANY voice, not only the bass. It is labelled by where it sits: in the bass, inside the texture, or above it. This replaces the older fact, which could only see a pedal in the lowest voice. *(DEFERRED 2026-07-26; open_items/OI-194.md)*


### I. Module boundaries and code structure (2 new entries)

**D-227 — Read how MuseScore already does it, and never invent parallel infrastructure.** Before touching anything MuseScore already provides - panels, walking the score, playback, settings, translation - the existing MuseScore code for it is read and followed. A second, parallel mechanism of our own is never created. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-228 — The bridge pattern - engraving types enter and leave at named free functions in the notation namespace.** The only code that may take MuseScore's own score objects and turn them into analysis results is a plain function living on the notation side, declared in a bridge header and defined in the matching bridge source file. Whoever calls it includes the bridge header, not the analysis headers, for the call itself. *(LIVE; ARCHITECTURE.md)*


### K. Documentation governance (5 new entries)

**D-127 — An architectural decision that changes is documented in the same commit.** When a design decision changes, the change to this document goes in the same commit as the change to the code. *(LIVE; ARCHITECTURE.md)*

**D-192 — A scoring change and its documentation land in the same commit.** Any commit that adds or changes a template, bonus, guard, gate or other scoring term in the chord analyzer must carry the matching update to the scoring-model document. They may never drift apart. *(LIVE; CLAUDE.md)*

**D-193 — The writing standards live in one place, and predicates must be qualified.** Anything written as a specification, a design, a decision surface, or for the user follows two standards. Every word that relates two things must name the second one - the check is to force the word to be followed by the thing it points at, and a phrase the prose cannot supply is a hole in the thinking. And terms are defined before use, in plain vocabulary, with no invented synonyms and no insider shorthand. *(LIVE 2026-07-02; CLAUDE.md)*

**D-194 — No self-invented labels, abbreviations, numbering schemes or jargon.** A thing is called by the name it already has in the repository. If it has none, it is described in plain words rather than given a coined label - in documents, rows of the open-items register, commit messages and conversation alike. *(LIVE 2026-07-11; CLAUDE.md; derivation not recorded)*

**D-195 — Every design decision carries its defense at its home.** Wherever a design decision is written down - the owning layer's specification first - the record says WHY: the published research or algorithm it adopts, the measurement that decided it, or the constraint that forced it. Every design decision must be defendable and its defense written where the decision lives. Where the record has none, the decisions register says 'derivation not recorded' rather than supplying one afterwards. *(LIVE 2026-08-01; CLAUDE.md)*


### L. Licensing, contribution, and coding standards (11 new entries)

**D-116 — The system is a module inside MuseScore Studio, not a plugin.** The harmonic analysis is built into MuseScore Studio's own program code as a new component of it, not added on afterwards as a plugin. It uses MuseScore's own score model, engraving, playback and interface directly. *(LIVE; ARCHITECTURE.md)*

**D-117 — The long-term intent is an official contribution to MuseScore Studio.** The aim is for this work eventually to become part of MuseScore Studio proper, so it is written to MuseScore's own coding, licensing and contribution rules from the start. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-118 — GPL v3, and every external library must be GPL v3 compatible.** All the code is released under the GPL v3 licence, the same licence MuseScore Studio uses, and no outside library may be used unless its licence is compatible with that. *(LIVE; ARCHITECTURE.md)*

**D-119 — The MuseScore contributor licence agreement is signed before any pull request.** Before any of this work is offered back to MuseScore as a pull request, the contributor agreement with MuseScore must be signed. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-120 — MuseScore's coding style is followed, with clang-format run before every commit.** The code looks like MuseScore's own code: the formatter configuration in the repository is run before every commit, names follow MuseScore's conventions, every file carries the GPL v3 header, and includes are ordered MuseScore's way. *(LIVE; ARCHITECTURE.md)*

**D-121 — Where MuseScore's documentation practice is minimal, the higher standard applies.** Following MuseScore's conventions does not mean copying how little it documents. Where MuseScore documents sparsely, this project documents properly instead. *(LIVE; ARCHITECTURE.md)*

**D-122 — Every public class and method is documented in musical terms.** A public class must say which musical idea it implements, what music it takes in, what it produces, and what it deliberately does not handle. A public method must say the same about the musical operation it performs, in musical terms rather than programming terms. *(LIVE; ARCHITECTURE.md)*

**D-123 — Every non-obvious scoring weight or threshold explains its musical reasoning.** A number in the scoring code that is not self-evident must be accompanied by the musical reason it has the value it has. *(LIVE; ARCHITECTURE.md)*

**D-124 — The analyzer code must be readable by a musician.** Every weight, threshold and rule of thumb in the chord and key analyzers carries its musical reason, to the standard that a musician with ordinary theoretical training can read the code and see why each choice was made. *(LIVE; ARCHITECTURE.md)*

**D-125 — Every test documents the musical situation, the expected result, and what a failure means.** A test says which musical situation it exercises, what the right answer is and why it is musically right, and what it would mean about the system if the test failed. *(LIVE; ARCHITECTURE.md)*

**D-126 — One coherent piece of functionality per pull request.** Each contribution offered back to MuseScore does one thing. *(LIVE; ARCHITECTURE.md)*


### M. The style system and the knowledge base (6 new entries)

**D-128 — Styles are defined entirely in data; adding one never requires code changes.** A musical style is a data file. The program code implements the mechanisms - voice leading, chord generation, voicing - and the style file supplies the numbers that make one style behave differently from another. Adding a style is never a code change. *(LIVE; ARCHITECTURE.md)*

**D-129 — Style conflicts resolve by a declared priority - explicit overrides always win.** When a style assembles itself from several inherited sources, the order of precedence is fixed: system defaults are weakest, inherited sources come next in the order they are declared with later ones winning, and anything the style file states explicitly wins outright. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-130 — The style loader never names a style in code.** The loader reads whatever style files it finds in the styles directory. No style's name appears anywhere in the program code. *(LIVE; ARCHITECTURE.md)*

**D-131 — One shared style taxonomy, not two parallel vocabularies.** The list of style families the presets choose from is the SAME list the harmonic vocabulary tags its entries with - one hierarchy, not two that can drift apart. A style earns a place on it only if its functional harmony is genuinely distinct, which is why free jazz and atonal music are not on it. *(LIVE; ARCHITECTURE.md)*

**D-132 — The style taxonomy is a theory-based first version; grounding it empirically is committed work.** The style families and their weights are currently drawn from music theory, not from data. Deriving both from corpora instead is recorded as work that will be done, not as an option. *(DEFERRED; ARCHITECTURE.md)*

**D-133 — The harmonic vocabulary is a queried reference component, not a layer of the analysis.** The catalogue of progressions and substitutions is something the analysis stages ask questions of, not a stage they pass through. Its entries say where the theory comes from; whether that theory holds up against real music is the caller's question, not the catalogue's. *(LIVE; ARCHITECTURE.md)*


### N. Generation, constraints, visualization, and the LLM integration (10 new entries)

**D-134 — A voicing type is never requested directly; the style selects it.** A caller asking for a voicing says which style it wants, never which voicing technique. The style decides whether the answer is a drop-2, a shell, a chorale spacing or something else, and in what proportion. *(LIVE; ARCHITECTURE.md)*

**D-135 — A fixed element is a hard constraint the optimizer may never modify.** Anything the user has pinned - a note, a voice, a chord, a passage - anchors the search for good voice leading. The optimizer works around it and never changes it. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-136 — The inference demo view is a developer tool and is not shipped.** The step-by-step view of the analysis making its decisions exists so a developer can watch and judge it by eye and ear. It is not part of what a user gets. *(DEFERRED; ARCHITECTURE.md)*

**D-137 — The harmony maps are our own visual design, and are chosen partly to avoid intellectual-property claims.** The planned map of harmonic function draws on published chord-scale theory but is laid out our own way, not copied from the commercial product that inspired it. *(DEFERRED; ARCHITECTURE.md)*

**D-138 — Chord preview uses MuseScore's note-input pathway, not the playback pipeline.** Clicking a chord on a harmony map plays it through the same quick path MuseScore uses when you hear a note as you enter it, not through full score playback. *(DEFERRED; ARCHITECTURE.md)*

**D-139 — The language model holds no object references - every tool call carries its own musical address.** When a language model asks the program to do something, it names the place in the music each time. It never holds a handle to an object in the score. *(DEFERRED; ARCHITECTURE.md)*

**D-140 — The language model is a search agent and is never given the whole score.** Rather than being handed the entire score, the language model is given tools to find what it needs and fetches it piece by piece - the way a person reads a large document by searching it. *(DEFERRED; ARCHITECTURE.md)*

**D-141 — The language model sees what the user set, not what the engraving engine derived.** The model is shown the composer's own choices - pitches, dynamics, articulation, colour, lyrics, visibility - and not the results of laying the music out, such as positions, beam geometry or stem lengths. *(DEFERRED; ARCHITECTURE.md)*

**D-142 — The composing module is the language model's context provider; the model never re-derives harmony.** Every stretch of music sent to a language model arrives with our harmonic analysis already attached - chord symbols, Roman numerals, key, harmonic rhythm. The model reads that; it does not work the harmony out from the notes itself. *(DEFERRED; ARCHITECTURE.md)*

**D-143 — The language-model bridge is built as a module but confined to the core access layer, so it can become a plugin.** It is written inside the program for speed of development, but restricted to the same narrow interface a plugin would have, so that moving it out to a plugin later is straightforward. *(DEFERRED; ARCHITECTURE.md)*


### O. Intonation (10 new entries)

**D-144 — Percussion is excluded from analysis and tuning; fixed-pitch instruments are the tuning anchor.** Unpitched percussion takes no part in working out the harmony and receives no tuning adjustment. Where a piano or organ is playing, the other instruments tune to it. *(LIVE; ARCHITECTURE.md)*

**D-145 — One preference chooses the tuning system, and no tuning code hardcodes one.** Which tuning system is in force is a single user setting, read afresh each time any tuning happens. No part of the tuning code has a system built into it. *(LIVE; ARCHITECTURE.md)*

**D-146 — A tie chain is one indivisible tuning event, and its tuning comes from one authority note.** Notes joined by ties are one sustained sound, so they are tuned once and never split apart. The tuning is worked out from a single note in the chain - the one carrying a tuning anchor if there is one, otherwise the first - and applied unchanged to the whole chain. *(LIVE; ARCHITECTURE.md)*

**D-147 — A slur, not a tie, joins the halves of a split note.** When a sustained note must be retuned partway through, it is cut in two and the halves are joined with a slur rather than a tie. *(LIVE; ARCHITECTURE.md)*

**D-148 — The split is visible in the score; the invisible alternative is deferred.** The reader sees two shorter notes joined by a slur where a note was retuned. The alternative - keeping the written note and hiding a silent playing copy - was designed and set aside. *(LIVE; ARCHITECTURE.md)*

**D-149 — Only visible, sounding notes enter the pitch-class collection.** Notes marked invisible, and notes that do not play, take no part in identifying the chord - which also keeps any hidden note created by the tuning machinery out of the analysis. *(LIVE; ARCHITECTURE.md)*

**D-150 — The chord staff is the output, never an input to the analysis that fills it.** When the harmonic reduction is written onto a staff, that staff's own contents are kept out of the analysis that produced them. *(LIVE; ARCHITECTURE.md)*

**D-151 — Populating the chord staff overwrites whatever is in the selected range.** Running the reduction again over the same passage replaces what is there. Keeping an earlier analysis is the user's job - undo it, or copy it somewhere else first. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-152 — Roman numerals and Nashville numbers are never shown together on one staff.** The chord staff shows one or the other beneath the music, chosen by preference, never both. *(LIVE; ARCHITECTURE.md)*

**D-153 — Interactive annotations are written in the score's normal colour; the batch pipeline writes red.** When a person runs the annotation, what it writes looks like anything else they typed. When the headless batch tool runs it, everything it writes is red. *(LIVE; ARCHITECTURE.md)*


### P. The user interface, persistence, and machine-learning readiness (8 new entries)

**D-154 — New panels use MuseScore's own panel and interface infrastructure.** Any new panel is built with the same window-docking and interface technology MuseScore already uses, after reading how MuseScore's existing panels are built. No parallel machinery is created. *(DEFERRED; ARCHITECTURE.md)*

**D-155 — Every user-visible string goes through MuseScore's localization, in English and Swedish.** Text a user can read is translatable through MuseScore's own translation system, and every new string is supplied in English and Swedish. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-156 — Accessibility follows MuseScore's existing patterns.** Keyboard navigation, focus handling and screen-reader support are done the way MuseScore already does them. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-157 — The harmonic-display preference exists for clarity, not for cost.** The setting that hides the harmonic information from the status bar is there because some users find it distracting, not because the analysis is expensive. Switching it off does not skip the analysis. *(LIVE; ARCHITECTURE.md)*

**D-158 — Our data lives in separate files inside the score archive; the score file is never touched.** Constraints, branches, cached analysis and preferences travel with the score as extra files inside its archive, beside the standard MuseScore score file, which our code never modifies. *(DEFERRED; ARCHITECTURE.md)*

**D-159 — Every custom file carries a format version, and the score file is never rewritten by our persistence.** Each of our own files records which version of its format it is, so older files can be migrated when the format changes; the standard MuseScore score file inside the archive is never rewritten by us. *(DEFERRED; ARCHITECTURE.md; derivation not recorded)*

**D-160 — Arranger interactions are logged from the start, with consent, as future training data.** Every suggestion a user accepts, changes or rejects is recorded - with their consent - as a labelled example for future machine learning. *(DEFERRED; ARCHITECTURE.md)*

**D-161 — Chord symbols already in a score are a second analyst's opinion, not ground truth.** When the automated review meets a score that already carries chord symbols, it treats them as another analyst's reading. Disagreements are discussed, not scored as our errors. *(DEFERRED; ARCHITECTURE.md)*


### Q. Scope and the development toolchain (3 new entries)

**D-162 — The development tools are not part of the shipping product.** The batch analysis tool, the comparison scripts and the remaining measurement tools are built only in development builds and never ship to a user. *(LIVE; ARCHITECTURE.md; derivation not recorded)*

**D-163 — The batch tool deliberately skips post-load layout.** The headless analysis tool never lays the music out on the page, because it only ever reads the logical structure. *(LIVE; ARCHITECTURE.md)*

**D-164 — What is out of scope, and what degrades gracefully at the boundary.** Live performance, film and game synchronization, audio transcription, spatial music and extended techniques as a primary language are not attempted. Non-Western traditions and post-tonal music are not attempted either, but the system is required to fail gracefully where it meets them rather than producing confident nonsense. *(LIVE; ARCHITECTURE.md; derivation not recorded)*


### S. The guiding principles (33 new entries)

**D-165 — #1 - build only on established fact and theory.** Nothing is built on a hunch. Every method comes from published research, a public algorithm, or public software. Investigating to find out what the facts are is a separate, permitted activity. *(LIVE; CLAUDE.md; derivation not recorded)*

**D-166 — #2 - target the specific open question, not the general topic.** Research effort goes to the exact question in front of us, not to the surrounding subject generally or to something already handled. *(LIVE; CLAUDE.md)*

**D-167 — #3 - an unexpected finding is a failure to diagnose, not a curiosity.** Being surprised means the facts and theory we built on were incomplete. Surprise is treated as a defect in our own understanding, not as an interesting result. *(LIVE; CLAUDE.md)*

**D-168 — #4 - the long-term goal is maximum-precision inference.** The objective the whole project is measured against is getting the analysis as accurate as it can be made. *(LIVE; CLAUDE.md; derivation not recorded)*

**D-169 — #5 - when facts may be scarce, investigate.** If it is unclear whether we know enough about something, the answer is to go and find out, not to proceed on what we have. *(LIVE; CLAUDE.md)*

**D-170 — #6 - total unification: one path per concern.** There is exactly one implementation of any given concern. No duplicated code, no second place the same question is answered. *(LIVE; CLAUDE.md)*

**D-171 — #7 - a layer is enhanced only with what belongs to it.** A stage of the analysis gets only the methods that are properly its own. If the right method does not belong there, the layers are redesigned rather than the method smuggled across. *(LIVE; CLAUDE.md)*

**D-172 — #8 - no inference-problem-driven coding until every method sits in its correct layer.** Work is not steered by whichever analysis error is currently visible. Until the structure is built out, a fix is made at the stage that owns it, at the time that stage is being built. *(LIVE; CLAUDE.md; derivation not recorded)*

**D-173 — #9 - measure only on corpora known to be non-stale and accurate.** A measurement is only run against music whose annotations are current and correct. *(LIVE; CLAUDE.md)*

**D-174 — #10 - documentation always in sync with code.** The documents describing the system never lag behind the system. *(LIVE; CLAUDE.md)*

**D-175 — #11 - regression tests in sync with code, and run between iterations.** The tests that guard against going backwards are kept current with the code, and they are run between each step of work rather than at the end. *(LIVE; CLAUDE.md; derivation not recorded)*

**D-176 — #13 - surface a surprise as a stop before building around it.** When something unexpected turns up, work halts and it is reported. It is never quietly worked around. *(LIVE 2026-07-06; CLAUDE.md)*

**D-177 — #14 - every behavior change is one user-ratified, revertible, provenance-stamped commit.** Anything that changes what the system does is ratified by the user first, lands as a single commit that can be undone whole, and carries the record of where it came from. *(LIVE 2026-07-06; CLAUDE.md; derivation not recorded)*

**D-178 — #15 - verify at the objects on the full output surface, never at an assertion.** A result is confirmed by looking at the actual data it produced, across everything it produced - the chosen reading and the alternatives carried beside it - not by a test that asserts what was expected. *(LIVE 2026-07-06; CLAUDE.md)*

**D-179 — #16 - every measurement is stamped to its corpus and its tooling, and the outgoing reference is snapshotted.** A measurement records which music it was run on and which version of the measuring code produced it, and the previous reference numbers are saved before new ones replace them. *(LIVE 2026-07-06; CLAUDE.md)*

**D-180 — #17 - the Premise Gate.** Before anything that affects the analysis is built or even probed: every load-bearing causal claim is written down and labelled as an established fact, a published theory, or an assumption; every assumption gets a written numerical prediction BEFORE anything is measured; the mechanism is traced by hand through three to five real failing cases, asking first whether it fires at all and only then what it changes; any stand-in quantity must itself be justified; any claim that one thing cannot affect another must name how it could; and no number enters a document by being typed in by hand. *(LIVE 2026-07-10; CLAUDE.md)*

**D-181 — #18 - an unverified causal premise is forbidden (Class A).** No design may rest on a claim about how our own system or data behaves when that claim could be checked and has not been. *(LIVE 2026-07-10; CLAUDE.md)*

**D-182 — #19 - an unestablished measurement tool is forbidden (Class B).** A measuring script, a corpus, a gate or a recorded figure is trusted only once it has been positively shown to be right - checked against an independent oracle, with a derivation of what its unit actually measures, and a reproduce-check. Never merely because nothing has contradicted it. *(LIVE 2026-07-10; CLAUDE.md)*

**D-183 — #20 - fit and evaluation are separated.** No number is graded on the same music that helped choose it. Before any fitting, the held-back music and the budget of how many free values may be fitted are declared; the headline figure is always the one measured on the held-back music. *(LIVE 2026-07-18; CLAUDE.md)*

**D-184 — #21 - ground truth is a measurement tool too, and its accuracy is measured.** How right the reference annotations are is itself something to be measured - how far annotators agree with each other, axis by axis - not assumed. Every precision target and every claim that a remaining error is irreducible is read against that measured ceiling. *(LIVE 2026-07-18; CLAUDE.md)*

**D-185 — #22 - every hard gate declares in advance how it handles the largest change it will meet.** A rule that decides whether a change may ship must say, before the fact, what it does when the change is far bigger than the incremental ones it was written for. It must never be rewritten while such a change is sitting in front of it. *(LIVE 2026-07-18; CLAUDE.md)*

**D-186 — #23 - an end-state principle needs a lawful transition.** When a planned piece of work must temporarily break a principle that describes the finished state - such as building a second analysis path beside the first - the breach is declared, bounded, and approved in advance together with the plan for removing it. *(LIVE 2026-07-18; CLAUDE.md)*

**D-187 — #24 - every reported figure carries its uncertainty.** How much a measured number could move by chance, given how much music it was measured on, is quantified and reported with it. A difference inside that range is not a finding and no decision may rest on one. *(LIVE 2026-07-18; CLAUDE.md)*

**D-188 — The constrained-optimum ledger corollary.** When a design is chosen because it complies with the method rather than because it measured best, the record must name what the best-performing alternative actually was and why it is ruled out. *(LIVE 2026-07-18; CLAUDE.md)*

**D-189 — The scope of surprise, and the three-stage funnel.** Being surprised is allowed - expected, even - in exploratory work whose whole purpose is to remove ignorance. It is not allowed while building the analysis itself: there a surprise stops the work and shows the Premise Gate was not satisfied. The order of work is: trace it by hand for hours, then probe it read-only for a session, then build it. *(LIVE 2026-07-10; CLAUDE.md)*

**D-190 — The decision-neutrality corollary - what exists carries no weight in choosing a design.** A design is chosen on the principles and the goal of the best possible analysis, and on nothing else. What it would cost to make existing code obsolete is a secondary consideration that can only break a tie between designs already equal; how many places downstream would have to change counts for nothing; and a change in what the user sees counts for nothing either - though every such change still needs ratifying and verifying exactly as before. The best design is chosen first, and what exists then either serves it or is retired. *(LIVE 2026-07-26; CLAUDE.md)*

**D-200 — Make it work first; compromise on performance only if performance proves a problem.** Getting the analysis right comes first. Speed is traded against it only once slowness has actually turned out to be a problem. That does not make speed unimportant - it puts it second: anything that makes the same computation faster is free on every principle and is done first, and the settings that buy speed by giving up precision are the last resort, not the first. *(LIVE 2026-07-28; cowork_handoff.md)*

**D-201 — Very large scores must be handled, and are expected to be more common than our corpora.** A Wagner act or a symphony must work. The user expects such scores to be a more common use than the chorales the system was fitted on. This is a standing requirement every later design is judged against, not a defect report. *(LIVE 2026-07-28; OPEN_ITEMS.md)*

**D-202 — The effort control is one setting with several dials, and it must bound the time taken.** How hard the analysis works is a single setting the user turns, not several. Behind it sit several dials, and among the things it must be able to bound is how long the analysis takes. It is too early to build: which pieces of the analysis have to be switchable is not yet known. *(DEFERRED 2026-07-28; OPEN_ITEMS.md)*

**D-203 — Candidate admission is completion, not refinement - so #8 permits fixing it now.** The rule that decides which chords the decoder will even consider is not a refinement of something already built - it is a piece that was never finished. So the principle that forbids chasing visible analysis errors before the structure is complete does not block fixing it. *(LIVE 2026-07-28; cowork_handoff.md)*

**D-204 — One fix is designed once over the whole enumerated family, never per symptom.** When several observed faults turn out to share a cause, the remedy is designed once for all of them together. Fixing whichever one is currently visible, on its own, is the error the one-path-per-concern and layer principles exist to prevent. *(LIVE 2026-07-28; cowork_handoff.md)*

**D-205 — A human acts as ground truth where no formal ground truth exists.** For music nobody has published an analysis of, the reference answer is a person's judgment. They may reach it however they like, including by letting an automated judge point them at the passages most likely to be wrong. That judge is guidance for the human, never a grader and never a number we report. *(LIVE 2026-07-13; open_items/OI-56.md)*

**D-206 — Intonation is held as a future feature, and is a declared future consumer of the analysis.** The six unbuilt pieces of the tuning design stay on the books as a deliberate long-horizon hold, revisited at a natural pause in the analysis work. The reason the hold is strategic rather than neglect: tuning will read the analysis - knowing the mode, the chord, its function and the progression is what lets a just-intonation decision be made, particularly the decision about staying in tune over time versus letting the pitch drift. *(DEFERRED 2026-07-13; open_items/OI-62.md)*


### T. Standing process rules and local patches (6 new entries)

**D-196 — The self-check: re-read the diff against the principles before reporting.** After every piece of work and before reporting it, the actual difference on disk in every touched file is re-read and checked against the principles, the conventions, the gate policies and the known defect types. Anything found is surfaced at once, never quietly shipped. *(LIVE 2026-07-11; CLAUDE.md)*

**D-197 — The distribution constraint - the import-fix patch is fork-local and never goes upstream.** The MusicXML mode-import fix may live in the user's own fork of MuseScore and be pushed there. It must never be pushed, merged or otherwise contributed to the MuseScore project. Any action that would carry it toward the upstream repository stops work and is reported. *(LIVE 2026-06-15; CLAUDE.md)*

**D-198 — The Windows snap fix in the muse submodule is intentional and must not be reverted.** Two lines were removed from MuseScore's Windows window-sizing code that told Windows the smallest allowed window was the whole screen. With them in place, a maximised MuseScore window could not be snapped into a screen zone - it stayed full-screen and lost its title-bar controls. The removal is deliberate and stays. *(LIVE 2026-05-14; CLAUDE.md)*

**D-199 — The MusicXML declared-mode import fix is intentional and must not be reverted.** MuseScore's importer dropped a key signature that matched the prevailing one in number of sharps or flats even when it declared a different mode - so a piece written with no sharps or flats but marked minor lost that marking on import. The fix compares the mode as well as the accidental count, so a mode-bearing key signature survives. *(LIVE 2026-06-14; CLAUDE.md)*

**D-208 — A withheld finding never enters a mandatory session-start read.** When a review is run blind - deliberately keeping a finding from the reader so that whether they rediscover it measures the review's power - that finding must not appear in any document the reader is required to open at the start. The status file carries a pointer; the content lives in a separate artifact opened only afterwards. *(LIVE 2026-07-28; OPEN_ITEMS.md)*

**D-209 — Code that is about to be deleted gets no audit - only the no-information-loss check at deletion.** Before auditing the system exhaustively, the code is split into what survives and what is scheduled for removal. What is scheduled for removal is not audited at all. The only thing owed to it is a check, at the moment it is deleted, that nothing it knew is lost. *(LIVE 2026-07-10; open_items/OI-84.md)*


### U. The standing decision-bearing surfaces (14 new entries)

**D-213 — The defect-type catalog is the living list of every problem type, and it is added to at discovery.** Every kind of problem ever found in this project has an entry saying what it is, the case that first showed it, and how to detect it - mechanically wherever possible. A newly discovered kind of problem gets its entry in the same commit that records the discovery. Entries are never deleted: a kind of problem that a structural change has made impossible is marked as such, with the mechanism that kills it. *(LIVE 2026-07-10; DEFECT_TYPES.md)*

**D-214 — The dim7 characteristic bonus is the rotation selector and may not simply be removed.** The bonus that makes a diminished-seventh chord prefer one rotation over another is what selects the rotation. Removing it without putting an equivalent mechanism in its place breaks the choice. *(LIVE; docs/scoring_model.md)*

**D-215 — Gating the root-continuity bonus on a sparse predecessor is a dead end.** Making the bonus that rewards keeping the same root depend on how much evidence the previous chord had was tried in two forms and abandoned. *(LIVE; docs/scoring_model.md)*

**D-216 — The stepwise-bass bonus's four gates are each load-bearing.** The bonus for a bass moving by step is switched off in four situations, and each of the four is there because it prevented a specific regression that was actually observed. *(LIVE; docs/scoring_model.md)*

**D-217 — The segmentation phase must suppress every context-dependent bonus.** While the analysis is still deciding where one chord ends and the next begins, none of the bonuses that look at neighbouring chords may score anything. Adding a new context bonus without that gate will make the segmentation worse. *(LIVE; docs/scoring_model.md)*

**D-218 — Template array sizes derive from one constant, so the compiler enforces them.** Every array whose length must equal the number of chord templates takes that length from a single named constant. Adding a template means changing the constant and adding the template in the same edit. *(LIVE; docs/scoring_model.md)*

**D-219 — Gates B, C and D were unreachable and were removed; no temporal condition may be added to the enharmonic flip.** Three post-scoring gates turned out to be unreachable, because the conditions of the gate before them were a strict subset of theirs, and they were deleted. The constraint that follows: nothing that depends on time or on neighbouring chords may be added to the major-with-added-sixth against minor flip, because the safety net those gates provided is gone. *(LIVE; docs/scoring_model.md)*

**D-220 — The augmented-seventh guard requires both the major third and the augmented fifth.** The guard fires only when both intervals are present, not when either one is. Requiring only the third was tried and reverted. *(LIVE; docs/scoring_model.md)*

**D-221 — A sparse upper-register lowest note does not earn inversion bonuses.** A low note that is thin and high in the texture is not treated as a structural bass, so the bonuses that reward a recognisable inversion do not fire for it. *(LIVE; docs/scoring_model.md)*

**D-222 — If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used.** The bonus that favours diminished readings can, in the course of comparing bass notes, end up electing a winner that is not diminished at all. When that happens the analysis falls back to the answer it had before the bonus was applied. *(LIVE; docs/scoring_model.md; derivation not recorded)*

**D-223 — A gate that judges the pre-correction winner reads a snapshot, not the live result.** Where a gate has to compare against whatever the analysis thought before a correction was applied, it reads a copy taken beforehand rather than the current top result, which the correction may already have changed. *(LIVE; docs/scoring_model.md)*

**D-224 — Joint bass-and-chord scoring requires accumulated regional evidence.** The scoring that considers the bass note and the chord together only switches on when the notes came from accumulating a whole stretch of music. The single-moment paths - the status bar, a unit test - use the simpler single-bass scoring. *(LIVE; docs/scoring_model.md; derivation not recorded)*

**D-225 — A corpus is regenerated before its baseline figures are updated.** The measurement scripts read files produced by an earlier run. Updating a recorded baseline without regenerating those files first produces a number that silently describes an older state of the system. *(LIVE; BUILD_AND_TEST.md)*

**D-226 — The music21 export is version-pinned; regenerating it is a deliberate re-baseline.** The committed corpus files and the paired corroborating analyses were produced by one specific version of music21, recorded inside the files themselves. Regenerating them with a different version is not a refresh - it moves the denominators every agreement figure is measured against, and is treated like updating a golden reference. *(LIVE; tools/REPRODUCIBILITY.md)*


## Part C — the render-size problem, and the fix to ratify with the register

`DECISIONS.md` at 228 full entries has outgrown comfortable rendering — the same failure mode
that split the open-items register (user-ratified 2026-07-26, index + detail files). The same
cure applies and is already within the ratified shape's bound ("the index stays lean...
per-decision detail files where warranted", OI-208): regenerate the register as a LEAN INDEX
(one table row per decision: ID, title, status, home) plus per-group detail files carrying the
verbatim quotes, plain restatements and Why lines. A generator change only - the data file is
untouched, every guard still runs. Say yes and it is one regeneration.
