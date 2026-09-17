# CC instruction — the decision harvest: extract every decision-bearing statement in the repository into ONE candidate list (MECHANICAL, READ-ONLY; no adjudication)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and the detail files this
> dispatch serves: **OI-207** (the decision-conformance audit this prepares the input for) and
> **OI-208** (the decisions register the output will populate).
>
> **What this is, and what it is emphatically NOT.** OI-207 asks whether anything is implemented
> in direct opposition to a recorded decision. Answering that has two halves: **find the
> decisions**, then **check the implementation against each**. The second half needs judgment and
> is scheduled separately. **This dispatch does ONLY the first half, and it does it
> mechanically.** You are building a bounded candidate list so the adjudication pass spends its
> capacity on judging rather than on searching roughly a megabyte of prose.
>
> **Do NOT adjudicate. Do NOT check any decision against the code. Do NOT judge whether a
> candidate is really a decision.** Over-capture is free — the adjudication pass discards.
> Under-capture is the only real failure mode, and Task 3 measures it.
>
> **Current state:** branch `master`; expected HEAD `383429961f` — verify; mismatch = STOP.
> Riding Cowork edits: `cowork_handoff.md` and `STATUS.md` ride your first commit. This dispatch
> file stays untracked.
>
> **Hard stops:** origin only; **no `src/` change of any kind**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; no behaviour change; no fix; no adjudication. A surprise is a
> STOP (#13). VS Code bash rules on every command.
>
> **★ STANDING RULE, NEWLY DIRECTED (user, 2026-07-28) AND BINDING ON THIS DISPATCH: NEVER WORK
> FROM MEMORY INSTEAD OF DOCUMENTED FACTS.** It rides your Task-0 commit as a `CLAUDE.md`
> Conventions entry (a riding Cowork edit, already on disk). No claim in your report may rest on
> recalled or inferred content where a documented source exists — open the source and cite it
> file:line. Being right from memory does not satisfy it: correct recall is indistinguishable from
> incorrect recall without the check, and the check is what surfaces what the memory did not
> contain. For this dispatch specifically it has teeth: **do not decide from memory what a
> document "says about" a topic — harvest the text verbatim and let the adjudication pass read
> it.**
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28, at the user's direction.

---

## ★★ GOVERNING REQUIREMENT — THE USER WILL READ THIS OUTPUT HIMSELF

Normally your reports are read by Cowork and translated. **Not this one.** The user has stated he
will read the inventory directly, and that most CC output is unreadable to him. This is a
deliverable requirement, not a style preference, and it is graded.

**Who the reader is.** Deep knowledge of **music theory**. Deep knowledge of **software
architecture and design**. A working software developer — **but not a C++ programmer**, and **not
a statistician**. He knows this project's *musical* and *architectural* intent completely; he does
not know its internal vocabulary, and should not have to.

**Therefore, beside the machine artifacts, produce `tools/audit/decisions/decision_inventory.md`
— a document written to be READ.** The JSON and CSV stay exactly as specified, verbatim and
complete, for the adjudication pass. The Markdown document is the same content made legible.

**Rules for it, each testable:**

1. **Group by SUBJECT, not by source file.** A reader wants the decisions about one thing
   together. Suggested groups — adjust if the material argues otherwise, and say why: *which
   notes we look at and when*; *how the music is cut into stretches for analysis*; *how a key is
   decided*; *what may count as a chord, and how one is chosen*; *how non-chord tones are
   treated*; *what the analysis publishes and who may read it*; *how the result is displayed*;
   *how we measure ourselves and what counts as a regression*; *how work is sequenced and
   ratified*. File and line stay on every entry, but they are provenance, not organisation.
2. **Two forms per entry, never one.** (a) the statement **verbatim**, unaltered — the
   adjudication depends on it; (b) beneath it, **one or two sentences of plain restatement**: what
   this actually decided, in ordinary words. The restatement never replaces the verbatim.
3. **Define every project-internal term at first use, in the document itself.** If a restatement
   cannot be written without a term like *slice*, *segment*, *emission*, *class*, *factor*,
   *gate*, *record*, *seam*, *arm* — define it in one clause the first time it appears.
4. **No statistics vocabulary without plain explanation.** Where a decision is genuinely
   statistical, say what it means for the music or for the program's behaviour. Never leave
   *marginal*, *posterior*, *prior*, *likelihood*, *held-out*, *capacity*, *convex* standing
   unexplained. If a decision cannot be explained without its mathematics, say so plainly and give
   the consequence.
5. **No C++.** Describe behaviour, not syntax. The reader does not read templates, and should not
   need to in order to know what was decided.
6. **MUSIC-THEORY WORDS ARE RESERVED FOR THEIR MUSICAL MEANING, AND THE BARE WORD IS ALWAYS THE
   MUSICAL ONE** (the standing convention as directed 2026-07-28 — now in `CLAUDE.md`, a riding
   edit; read it there, it is the authority). **One rule: the bare word carries the musical
   meaning; every non-musical use is explicitly qualified.** Bare *score* is the music — write
   *candidate score* or *content score* when you mean a number. Bare *key* is tonality — write
   *map key* or *cache key*. Bare *measure* is the bar — write *measurement* for the gauging
   sense. Bare *note* is a pitch event — write *remark* or *entry*. Applied to the rest: **score**
   (say *numerical score* or *candidate score* when you do not mean the music), **key** (say *map
   key*, *cache key*, *lookup key* when you do not mean tonality), **measure** (say *to gauge*,
   *measurement run*, or reserve *measure* for the bar — and say which you mean, every time),
   **stem** (say *file name* or *piece identifier*, never the filename stem), **note** (say
   *annotation*, *remark*, *entry* when you do not mean a pitch event), **mode** (say *operating
   mode* explicitly, or reserve the word), **tie** (say *tie-break* in full, never bare *tie*),
   **dynamic programming** (spell it in full, never bare *dynamic*), **register** (say *issue
   register* or *the open-items register* in full), **beat** (never as a verb for "outperformed"),
   **scale** (say *grows with* rather than *scales*), **figure** (say *number* or *value*),
   **interval** (say *uncertainty range*), **resolution** (say *level of detail*), **sharpen**
   (say *refine*), **flat** (say *featureless* or *uniform*), **root** (say *underlying cause*),
   **rest** (say *remainder*). Where the existing repository text you are quoting uses a collided
   word, the verbatim quote stands unaltered — but your restatement beneath it must not.
7. **No abbreviation or label you invented.** Use the name a thing already has, or describe it in
   plain words — the standing convention, applied here with teeth.
8. **The self-test before you ship it.** For each entry ask: *would a reader who knows music
   theory and software architecture, but nothing about this repository, understand what was
   decided and why it matters?* If not, rewrite the restatement. Report how many entries you
   rewrote on that test — that number is evidence the test was actually applied.

**Length discipline:** this is for reading. Keep restatements to one or two sentences. If a group
grows past what can be read in a sitting, split it and say so; do not compress by deleting.

**Touchable set:** a NEW instrument and its artifacts under `tools/audit/decisions/`; the
register INDEX and detail files; `STATUS.md`; the riding Cowork files.

---

## Task 0 — the row this dispatch owes, and one Cowork finding to record

**Row it (rule (c), index + detail):** **the pitch and spelling emission is restricted to STRUCK
tones.** The ratified `cowork_joint_estimator_factorization.md` specifies the pitch emission as
`P_emit(tone | k, c; covariates)` — **per tone** — and its 2026-07-19 granularity amendment
evaluates the pitch and spelling emissions *per tone* while specifying the bass factor as "each
event's **sounding** bass against the segment's chord"; the emission's covariate set includes
**tied-over preparation**, which presupposes that tones arriving by tie are emitted at all. The
implementation walks `piece.notes_by_event[e]` for the events inside the segment — i.e. only
tones whose **onset** falls in the segment — so a note that is already sounding contributes
nothing to the pitch evidence for the stretch it sounds through. The one place the sounding set
is consulted is the missing-template-tone penalty: a held note can spare a chord a penalty but
can never support it. **★ AND THE LAYER ARCHITECTURE DECIDED THIS EXPLICITLY — twice — so this is a departure from a
stated decision, not a narrowing of an ambiguous one** (found 2026-07-28 when the user asked
whether the primary source had been read; it had not): **`ARCHITECTURE.md:1045-1053`** — the
Layer-2 slicer's boundaries are "the sorted-unique union of every **onset AND every release** of
the eligible notes", a slice is "constant **tonal** sonority", "**Slice identity is the eligible
sounding-NOTE set**", and notes that open no boundary "still ride along in each slice's
`overlapping()` set (passed through, not dropped)"; and **`ARCHITECTURE.md:3134-3141`** — the
priority-of-evidence table ranks "**Actual sounding notes** — what is literally happening now" as
the **STRONGEST** evidence, above temporal context, the notated signature and the mode tag.

**The mechanism connecting the two layers, and it is the sharpest statement of the defect:** the
slicer creates a boundary at every **release**, by design, because a note ending changes the
sonority — and those are exactly the moments at which nothing is struck (the fire-count histogram
records 428 windows with zero distinct onset pitch classes). So the architecture, working
correctly, manufactures the moments at which the emission concludes there is no pitch evidence.
One layer publishes the sounding set on every slice; the consumer does not read it.

Record it as a conformance gap, **priority**, feeding OI-207 — with the two open caveats carried
honestly: (a) the note tables were FITTED by counting tones in some particular way, so if they
were counted by onset, correcting the decode without refitting would leave the model reading one
thing through numbers calibrated to another — a real constraint on any fix; (b) the extent of the
consequence is unmeasured — the admission gates fail loudly and were therefore found, but the
emission miscounts silently, so wherever admission happens to succeed on a sustained texture the
reading may still be skewed, which is an accuracy question everywhere rather than a coverage
question in one place.

*(The user's position, recorded: a note that is already sounding is part of the sonority, and
whether it belongs to the chord is what the emission's chord-member / non-chord-tone categories
are for. The "held notes are weaker evidence" argument does not survive: the fit corpus is voices
and organ — sustaining throughout — so the decay reading never applied even where the model was
fitted.)*

**Also row (rule (c), index + detail): the music-theory terminology collision.** User-directed
2026-07-28, generalizing the "instrument" case: any term coinciding even slightly with music
theory is reserved for its musical meaning, because an ambiguous domain vocabulary in a
music-analysis system makes every document harder to read and every specification easier to
misapply. The rule is now in `CLAUDE.md` Conventions (a riding edit) and **binds new writing
immediately**; the existing tree is **NOT renamed unilaterally** — that pass is its own scoped,
ratified work item, because some names carry correspondence to the published research the design
is grounded in (#1/#2), which makes it a decision surface rather than a sweep. Record the starting
inventory of known collisions from the `CLAUDE.md` entry, and note the two that are structural
rather than careless: **score** (a candidate's numerical score versus the music) and **measure**
(to gauge versus the bar) — both pervasive, both used in this project in *both* senses already,
and both with a real cost to renaming.

**Also row (rule (c), index + detail): the writing-standards conformance question — DEFERRED BY
THE USER to the Friday discussion, recorded so it does not live only in conversation (rule (e)).**
`cowork_design_doc_template.md` is the ratified home of this project's writing standards: the
**predicate-qualification** standard (user, 2026-06-24 — every two-place word names its argument,
with the stated mechanical check), the **defined-terms / plain-vocabulary / no-shorthand**
standard (user, 2026-07-02, whose rule 5 on multiple-meaning words already used *key*, *bar* and
*measure* as its examples), the **fourteen-section document structure** (arc42 + IEEE 1016), the
**status-banner** convention, and the **implementation/test locator** rule. It names two worked
examples not yet read by the current sessions (`cowork_spec_language_sweep.md`,
`cowork_layer3_spec_language_sweep.md`). **The open questions, for Friday, not for this dispatch:**
(a) does the current documentation tree conform to these standards — several decision-surface
documents plainly do not follow the fourteen-section structure, and whether that is a gap or a
deliberate exemption is unjudged; (b) are DOCUMENTS inside or outside the scope of the conformance
enumeration, or is only the analysis in scope; (c) the tree-wide music-terminology cleanup implied
by the 2026-07-28 sharpening is unratified and unscoped. **Do not act on any of these here.**

## Task 1 — the harvest

Build `tools/audit/decisions/gen_decision_harvest.py`. Deterministic, re-runnable, artifact-
producing (#17f). It scans the decision-bearing corpus and emits every candidate statement with
enough context to be adjudicated later **without reopening the source**.

**Scope — the corpus to scan (extend if you find another decision-bearing surface; report it):**

- `cowork_handoff.md` and `cowork_handoff_archive.md`
- `STATUS.md` and `STATUS_ARCHIVE.md`
- every `cowork_*.md` design and decision document at the repository root
- **`ARCHITECTURE.md` — and specifically its PER-LAYER SPECIFICATIONS, which are the PRIMARY
  place decisions about how a layer should work are recorded** (user-directed 2026-07-28). Do not
  treat this file as background: harvest its layer specs, its contract tables, its priority-of-
  evidence statements and its per-layer invariants as first-class decision statements. Two
  worked examples of what is being missed if this is skimmed — `:1045-1053` (the Layer-2 slicer:
  boundaries are the union of every **onset AND every release**; "Slice identity is the eligible
  **sounding-NOTE set**"; non-boundary-opening notes "ride along in each slice's `overlapping()`
  set, passed through, not dropped") and `:3134-3141` (the priority-of-evidence table ranking
  "**Actual sounding notes** — what is literally happening now" as the STRONGEST evidence, above
  temporal context, the notated signature and the mode tag)
- `CLAUDE.md` (the guiding principles and their provenance trail)
- `docs/` — in particular `scoring_model.md` (§8 constraints and dead ends),
  `p3_granularity_ab_3_1b.md`, `score_inventory.md`, and the other committed evidence documents
- `DEFECT_TYPES.md`
- `OPEN_ITEMS.md` and `open_items/`
- the `cc_*_report.md` reports at the root (they carry rulings recorded nowhere else)
- **production code comments** — decisions are recorded in code too (the 44-line Stage-3.1b block
  in `notationcomposingbridge.cpp` is the proof); scan `src/composing/` and `src/notation/` and
  `tools/*.py` comment text only, never code semantics

**Signatures — cast the net WIDE.** At minimum: ratified, ratification, user-ratified, decided,
decision, ruled, ruling, adjudicated, shelved, falsified, refuted, excluded, rejected, dead end,
superseded, retired, deferred, held, parked, "do not", "never", "must not", "no longer",
"replaced by", "in favour of", "chosen", "we will", "the rule is", constrained optimum, premise,
"not to be", "forbidden". Add any further signature you find productive and **report the final
list**.

**Per candidate, emit:** a stable identifier; source file; line; the matched signature; the
statement text; enough surrounding context to stand alone (a few lines either side, or the
enclosing bullet/paragraph — declare your rule); the date if one is discoverable nearby; who
ratified it if stated; and any nearby pointer to evidence (a document name, a commit hash, an
artifact path). **Do not summarize or paraphrase the statement — carry it verbatim.**

**Deduplicate conservatively:** the same statement quoted in several places is normal and its
repetitions are evidence of standing, so record them as linked occurrences rather than dropping
them. Never drop an occurrence merely because a similar one exists.

Emit `tools/audit/decisions/decision_candidates.json` (full) plus a CSV for reading, and a short
`manifest.json` stamped with the corpus git hash and the instrument commit (#16).

## Task 2 — the shape, for the register that will consume this

Emit the candidates in the field shape a decisions index would need, so the later pass populates
a register rather than writing prose: identifier; the decision in the author's own words; date;
who ratified; **status left EMPTY for the adjudication pass** (live / superseded-by / shelved-
with-evidence / falsified / unknown); the evidence pointer; the source occurrences; and an empty
conformance field. **Do not fill status or conformance. That is the next pass's work and filling
it here would defeat the purpose.**

## Task 3 — recall, measured (the establishment, #19)

A harvest is an instrument and is trusted only if positively established. **Seed it with
decisions we already know exist and measure whether it caught them.** At minimum:

1. the Stage-3.1b shelving of whole-score interactive analysis (`docs/p3_granularity_ab_3_1b.md`
   and the code comment block in `notationcomposingbridge.cpp`);
2. the joint-native record ruling (decision A2);
3. the two-mode key ruling with the published un-rounded modal reading (decision C1);
4. the embedded-tables ruling (decision D1);
5. the pedal-point ruling, with its voice-independence sharpening;
6. the decision-neutrality corollary in `CLAUDE.md`;
7. the full-candidate-list amendment to the output contract;
8. the "never merge this patch upstream" distribution constraint in `CLAUDE.md`;
9. the ratified robust-unit regression stop;
10. the ordering rule that the retirement map precedes the reviews.

Report caught / missed per seed, **with the missed ones diagnosed** — a miss means the signature
list is wrong and it is far cheaper to learn it now. Iterate the signatures until recall on the
seed set is complete, and report both the before and after.

Also report the harvest's raw size: candidates per source file, and the total. If the total is
so large as to be unusable, say so and propose a tightening — but **do not tighten unilaterally**;
an over-large list is a better failure than a lossy one.

## Task 4 — notes and close

Dated notes on OI-207 (its input now exists) and OI-208 (the candidate shape). `STATUS.md` entry
— a POINTER, not content (the OI-222 remedy is standing). Commits per change-class. Push origin.

**No adjudication anywhere in this dispatch.**

## Report

Hashes. The final signature list. Candidate counts per source and in total. The Task-3 seed
recall table, before and after iteration, with every miss diagnosed. Any decision-bearing surface
you found that this dispatch's scope did not name. The artifact paths. **And the readability
report on `decision_inventory.md`: the subject groups you used and why, the count of entries you
rewrote at the self-test, and any entry you could NOT restate in plain words — that last one is a
finding, because a decision nobody can restate plainly is a decision nobody can check.** Anomalies each diagnosed —
a surprise is a STOP.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

**After this dispatch:** the OI-207 adjudication pass — a higher-capacity session that takes this
candidate list and checks each entry against the current implementation, populating the decisions
register (OI-208) whose shape the user ratifies separately. The OI-215 / OI-226 / OI-227 fix
surface waits for it, because today's emission finding suggests admission and emission may share
one defect — the model reading struck notes where the design says sounding — and a fix designed
over part of a family is the patch-per-symptom error (#6/#7).
