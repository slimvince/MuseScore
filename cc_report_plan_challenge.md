# CC report — the CHALLENGE to the specification-reconstruction plan v4

> **Dispatch:** `cc_instruction_plan_challenge.md` (Cowork, 2026-08-19, written at branch tip
> `891bacc5d2`). **Subject:** `cowork_specification_reconstruction_plan_v4_2026_08_19.md`, on disk and
> untracked, **NOT RATIFIED** and treated here as authority for nothing.
>
> **This report reviews. It executes nothing the plan describes.** No specification text was written,
> no frame built, no derivation run, no `src/` edit, no golden, no test changed, moved or run, nothing
> under `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis built, designed, scoped
> or run, no design, no repair, no mining, no document archived, moved or deleted as a file, **no
> open-items row created, flipped or discarded**, and **no specification text edited**. [[OI-372]] and
> [[OI-374]] stand as found; [[OI-179]] stands OPEN and GATES. No finding number is allocated.
>
> **Ten verdicts, one per assumption, from the closed set of three.** Where an assumption survives,
> what was checked that could have refuted it is stated. **Nothing in this report concludes that the
> plan looks sound.**

---

## 0. The reads, and the A1 check taken first

**A1 — HELD on its tracked half, checked as the first act, entirely at content-addressed objects.**
`tools/audit/changed_paths.py` (the D-253-sanctioned enumeration, which reports paths and status codes
and cannot return file content) reports **837 records, of which ZERO are tracked modifications** — every
record is `??`. There is therefore no tracked path to compare blob against blob, and the F57 caveat does
not arise for any file, because no file is claimed unmodified against a committed blob.

**A1's untracked half is reported as the tree carries it, not as A1 words it.** A1 names "the four
untracked plan and boot-list files this sitting wrote". The tree carries **five**:
`cowork_specification_reconstruction_plan_2026_08_19.md`, `…_v2_…`, `…_v3_…`, `…_v4_…` and
`cowork_curated_boot_list_draft_2026_08_19.md`, plus this dispatch. The plan's own provenance line — "the
subject plan and its three withdrawn predecessors" — accounts for four plan files, so "four" appears to
count the plan versions and to have absorbed the boot list into the same phrase. **Not a STOP:** A1's
STOP condition is scoped to tracked paths and the tracked half held exactly.

**The mandated reads were performed by this session, not by delegation.** `CLAUDE.md` (the harness
injects the file's contents in full), `STATUS.md`, `DECISIONS.md` (859 lines, read whole in three
passes), the derived gating answer narrowed to its identity list
(`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`),
`cowork_handoff.md`'s THIRTY-THIRD block, and `cowork_audit_protocol.md`'s dispatch-protocol section
whole (lines 180–1524, every section carrying the `★ STANDING CLAUSE` membership marker).
`BUILD_AND_TEST.md` was **NOT** read: this batch runs no build, no test and no measurement tool whose
command lives there, so the condition is not met. The plan v4 was read in full.

---

## 1. THE LARGEST RETURN, STATED BEFORE THE TEN — the plan is not situated against the RULED phase structure

This is not one of the ten and it changes how several of them read, so it is stated first.

**`CLAUDE.md`'s Conventions section states that the three-phase structure is SUPERSEDED and that "the
ruled definitions' ONE home is `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3
— a pointer, never a copy, #6".** That section defines **six phases: preparation → the pilot → the
framework → the detail specifications → measurement design → the audit.** Read at that text, the plan
proposes work belonging to phases 2–4 and **omits, contradicts or re-decides five things the user has
already ruled**:

| what the ruled structure holds | where | what the plan does |
|---|---|---|
| **The FRAMEWORK phase** — "decide the all-encompassing analysis architecture: the layer decomposition, each layer's **charter** … and the **boundary contracts** between layers — so detail specifications are derived INSIDE ruled charters and are born one-home-per-concern" | surface §3.3 | **No framework phase.** Phase A derives a frame from the current documents' own headings instead. This is exactly the substitution L1 and L3 rest on. |
| **The implementation-blind rule.** §3.2's pilot constraints: "**NOT ALLOWED: reading implementation-derived material inside the deriving session**"; §3.4's the same for the detail-specification phase; §3.8: "**The implementation-blind rule binds every deriving session**" | surface §3.2, §3.4, §3.8 — all inside §3, which `CLAUDE.md` names as the ruled definitions' ONE home | Plan §2 lists deriving blind as **AUTHORED and challengeable**, and §15 offers it for refutation as **L7**. It is neither authored nor the plan's to give up. |
| **The DETAIL-SPECIFICATION phase's five disposition classes** (adopted / relocated / quarantined / discarded / historical), "a **proposal per difference**, never a silent rewrite", and the **cross-layer transfer list** for content found in the wrong layer | surface §3.4, §0 | Plan §5's own statement form and B3's four outcomes (confirms / contradicts / adds / dead end). Different vocabulary, no transfer list, no quarantine. |
| **The PILOT's inputs name the preserved pre-restructuring version `b006dc15b5` and the examination set** (the fired changed passage and the fifteen not-cleared changed passages of the July screen), carried BY NAME | surface §3.2 | Named nowhere in v4. |
| **The curated boot list is preparation output (d), "DRAFTED here and RULED by the user before any derivation session boots from it"**, and is the pilot's stated hard prerequisite | surface §3.1, §3.2 | Plan open question 4 asks "**Is the curated boot list still needed?**" — proposing to reconsider a ruled output. |
| **"[[OI-179]] gates as an establishment obligation until discharged"** is a standing constraint over **every** phase; its ceiling measurement maps to the **measurement-design stage** | surface §3.8, §3.5 | Plan §7 heads it "What runs BESIDE this plan and is **not gated by it**" and calls it "independent of this plan". |

**The plan's §14 open question 3 does ask "Does this replace the ruled PILOT phase, or execute it?"** — so
the author knows a collision exists. But that question names **one** of the six phases, while the plan's
Phase B is plainly the detail-specification phase and its Phase A is plainly a substitute for the
framework phase. **The collision is under-declared by a factor of three.**

**A consequence for this review's own brief.** §15 invites refutation of L7, which is a ruled standing
constraint. A reviewing side asked to refute a user ruling either attacks the ruling or reports that it
cannot. This report does the second, and answers L7 on the two grounds that remain open (§2, L7).

---

## 2. Task 1 — the ten assumptions

### L1 — "Section structure is less polluted than sentences." → **REFUTED**

**Both routes the plan itself names fire, and a third that neither names is worse than either.**

**(a) Sections that exist because a code module exists.** §3 *Directory Structure* is the plan's own
named candidate and it holds: §3.1 opens "The new code lives in `src/composing/`…" and is a fenced
listing of the source tree; §3.2 is a namespace→directory table; §3.3 opens "Read this section before
touching any code that crosses the composing ↔ notation boundary". §4 *Existing Components* is
one-subsection-per-class — every §4.1–§4.6 heading is a class, file or interface name, each opening with
a `**File:**` line (`ARCHITECTURE.md:2488, :3251, :3806, :3921, :3947, :4028, :4047, :4108`), and the
majority of its `####` children are declaration dumps (`Input — ChordAnalysisTone`, `Output —
ChordAnalysisResult`, `Chord Quality Enum`, `Public Interface`, `Factory — ChordAnalyzerFactory`).
Further code-driven sections outside §3/§4: §10.0 *Inference Demo Mode (Developer Tool)*, §11.5, §12,
§15's *Development Tools*.

**The structurally decisive one: the ENTIRE Layer 1–6 analysis specification — the document's principal
body of musical knowledge — is filed as `####` children of §3.3**, beginning immediately after the
`#### Bridge File Inventory` table of `.h`/`.cpp` filenames (`ARCHITECTURE.md:1537` → `:1560` Layer 1 …
`:2192` Layer 6). The music sits subordinate to a section about where files live. **A frame taken from
the headings inherits that subordination**, and A2 is declared "Mechanical", so nothing in Phase A would
notice.

**(b) The structure was edited under the doc-sync programme.** Four headings declare their own
creation-by-homing in their first body line (`:503`, `:5621`, `:7351`, `:385`). The unnumbered top-level
section at `:265` states its six rules "were until 2026-08-02 recorded only on tracking surfaces or in
`CLAUDE.md`, which is why they are stated here". Twenty-four "re-homed into this specification/section"
inserts dated 2026-08-04/07/08 cluster in §3.3's layer subsections and in §6/§7/§11; at least nine dated
"Delegation pointer (the fifth home case…)" blocks were written into pre-existing sections. §2.15
(`:1100-1110`) records that the ratified family rename reached the Cowork documents but **not** this one,
names four of its own headings as still carrying the banned word (§3.3, §4.1, §11.5, §11.6 — all four
still present verbatim), and defers the fix.

**(c) The route neither refutation names, and it is the sharpest.** `ARCHITECTURE.md` carries 26 `##`
headings. **The production inference layer's own specification sits ABOVE the Table of Contents and is
absent from it**: the ToC at `:582-603` enumerates items 1..19 and nothing else, while `## The joint
estimator — the standing rules of the production inference layer` (`:265`), `## Document governance and
the standing architecture notes` (`:551`) and both appendices are unlisted. **A2 therefore returns
different frames depending on whether it reads headings or the ToC, and the difference falls exactly on
the live production layer.**

**And A2 is not "Mechanical" as declared.** Lines `:896`, `:899`, `:902`, `:905`, `:907` match `^# ` and
are shell comments inside a fenced code block in §2.12. A heading enumerator that does not track fences
admits *Build*, *Tests — run once, capture tail* and *Python scripts* as top-level sections of the
specification. §4's numbering is separately broken: §4.1f sits at `###` level **between** §4.2 and §4.3,
a second §4.1d appears at `:3522` against the first at `:2873`, and seven `###` "Phase" headings hang at
section level with no number at all.

*What was checked that could have supported L1 and did not:* whether the code-shaped sections are a
minority (they are not — §3 and §4 span `:1333`–`:4262` and §3.3 holds the layer specification); and
whether the heading text is clean of the programme's footprint (four headings state their own homing
origin, and §2.15 names four of its own headings as non-conformant).

---

### L2 — "A specification statement can carry a code-falsifiable condition." → **REFUTED**

Task 2 supplied the material and Task 2 answers it in detail (§3 below). The verdict, stated here:
**of the five probes, exactly ONE — S3 — could be returned from field five alone without
interpretation, and the property that made it work is that its statement is about the EXISTENCE OF A
NAMED FIELD rather than about behaviour.** For all four behavioural statements the falsification clause
was insufficient, and in three of the four the opposite verdict was available to a reviewer reading the
same clause differently.

Three structural causes, each measured rather than argued:

1. **A behaviour is distributed across sites the clause cannot name in advance.** S1's clause names "the
   boundary-proposal site". On the live arm there are two sites with opposite answers: boundary
   PROPOSAL is exhaustive enumeration over `i ∈ [j−4, j)` and tests nothing at all
   (`jointdecoder.cpp:734`), while boundary SCORING is a fitted `beat_class → P(boundary)` table
   (`jointdecoder.cpp:331-333` → `jointadapter.cpp:484-500` → `jointtables.h:111`). The clause says
   "proposed or scored" and the two give different answers.
2. **The verdict often turns on code the clause cannot see.** S5's clause is "there is no abstention
   path on the root axis at all". `rootPc` is `std::optional` on both the decode and the record surface
   (`jointdecoder.h:114`, `jointnotationrecord.h:87`), so the type alone reads as an abstention path.
   The NOT-IMPLEMENTED verdict comes from admission filter (1) at `jointdecoder.cpp:438` making the
   empty case unreachable — two files away, and invisible from the clause.
3. **The statement must name the ARM, and the §5 form has no arm field.** Three of the five probes have
   different answers on the live joint arm and the legacy arm. Worse, **three source files in the live
   chain still declare themselves DORMANT** — `jointdecoder.h:43` "DORMANT (no production consumer)",
   `jointtables.h:44-45` "This module is DORMANT — no production path reads it",
   `jointnotationproducer.cpp:40` "this increment is dormant" — while
   `composingconfiguration.cpp:178` defaults `USE_JOINT_NOTATION_RECORD` to `Val(true)`. **A delta run
   that trusted the code's own self-declaration would answer against the wrong arm.**

L2 is stated unqualified — that *a* specification statement *can* carry a code-falsifiable condition.
The measured answer is that it can for existence statements and cannot, as the form stands, for
behavioural ones; and the plan's own §5 makes field five mandatory on **every** statement. **As stated,
REFUTED.** §3 gives the replacement form, from the delta side.

---

### L3 — "The problem is separable per section at all." → **REFUTED**

Answered at the text of the joint estimator's standing rules (`ARCHITECTURE.md:265-549`), as ordered.

**Can those rules be stated as independent per-section statements without loss? NO.** Five distinct
losses, each at the text:

**(i) The chord axis's value space is indexed by the key state.** The joint state's chord axis is
scale-degree-valued — a Roman numeral relative to the state's own tonic and mode, with the chord symbol
a derived fact (register entry **D-526**). A chord-section statement therefore cannot be written
independently of the key section without changing what a chord *is*. B2 derives each unit blind, with
the other units closed; a blind chord section would produce statements about absolute roots, which is
the wrong representation.

**(ii) Rule (b)'s capacity budget is one budget over the union of all sections.** "free parameters stay
at or below one tenth of the token count, and the weight vector holds at most 12 weights"
(`:293-296`). Guardrail 9 — "A ratified unit is closed" — means a later section's derivation can
consume the budget invisibly to every earlier, closed section. There is no object in the plan that
holds a constraint whose argument is the whole set.

**(iii) The record already carries a MEASURED case of one section's decision deciding another
section's answer.** The counted-quantities block's defense (`:438-445`): "under per-segment bookkeeping
a longer segment pays the bass and missing-tone terms once where a split pays them twice, so merging
harvests a discount unrelated to the music, which is the classic semi-Markov length bias. **On the case
that exposed it the bookkeeping alone decided merge against split, against the ground truth.**" A
bookkeeping decision belonging to the emission/bass section decided the **segmentation** outcome. That
is L3's feared failure mode, on the record, with a case behind it.

**(iv) The record already carries a LIVE, DECLARED, UNSETTLED contradiction between two sections, and
the plan has no step that could find it.** Rule (d) (`:331-338`): "On the key axis the decoder commits
its maximum-a-posteriori path; it never abstains … **This sits in tension with the abstention rule at
§5.7a** … The two statements are both in force in the record … **Which governs is not settled here.**"
The plan derives each unit blind (B2), reads it adversarially per unit (B5), ratifies it per unit (B6)
and **closes** it (guardrail 9). **There is no cross-unit consistency step anywhere in the plan.** Two
individually defensible, jointly incoherent statements would pass straight through — the exact words
L3 uses of itself.

**(v) Four of the six rules, and one whole subsection, are cross-cutting by their own declaration.**
(a), (b), (e) and (f) bind every factor; and the evidential-priority subsection says so in terms
(`:396-398`): "It is a **CROSS-CUTTING EVIDENTIAL RULE** about what the analysis may treat as evidence
and in what order, not a property of either implementation." The §5 statement form is atomic — one rule
per statement, five fields, **no scope field and no cross-reference field** — so a cross-cutting rule is
either restated in each section it binds (which #6 forbids) or unreachable from them.

**And the ruled structure already answers L3, which is why assuming it is the error.** The FRAMEWORK
phase exists to "decide the layer decomposition, each layer's charter … and the boundary contracts
between layers — **so detail specifications are derived INSIDE ruled charters and are born
one-home-per-concern**" (phase-definition surface §3.3). Separability is not a property to be assumed
from the existing documents' headings; it is a thing a ruled phase constructs. **The plan takes for
granted the output of a phase it omits.**

*What was checked that could have supported L3 and did not:* whether the document's own section
structure already isolates the joint concerns — it does the opposite. It allocates **one section per
legacy class** (§4.1 ChordAnalyzer, §4.2 KeyModeAnalyzer, both of the dormant arm) and **one section to
the entire joint production estimator**. The section structure partitions the dormant code more finely
than the live code.

---

### L4 — "Failing runs can be attributed to a section at all." → **REFUTED**

**What a failing run carries.** The committed diff base
(`tools/robust_stop/{preset}_variant_b_root_fail_runs.txt`, 4547 runs per preset) records **exactly
eight fields**, written at `a8_rebaseline_measure.py:569-576`: `stem`, `runStartTick`, the half-open
span, duration, our chord symbol, our root pitch class, the DCML root pitch class, and a one-letter
class (a)/(b). `summary.json` and `manifest.json` add nothing per run. `robust_stop_diff.py:51-53,
73-75` reads five of the eight.

**Attribution from those fields alone: NO.** The only cause-bearing field is the class letter, and it is
computed from **our** pitch-class set alone — it says the root is undecidable by symmetry, not which
decision failed. **94.3 % of failing cells are class (b)**, which carries no signal. Nine richer
per-cell fields built one function earlier (`:209-223`) — our quality, the DCML chord symbol, the
Roman-numeral verdict, the key verdict against the home key **and** against the local key, the music21
class, bass-is-root — are all **dropped at the run merge** (`:485-487`).

**What attribution would require, and its cost.** The key verdict; our bass against the inversion digits
parsed out of the ground-truth numeral; our region boundaries against the ground-truth spans for
over-grab; the neighbouring regions for voice-leading and cadence — all recomputable from `.ours.json`
plus the *When in Rome* annotations but **not** from the committed artifact — **plus the musical score
itself** for spelling, because the corpus JSON carries pitch classes only and no letter names. The
corpus is gitignored, so any such pass begins with a full regeneration (≈1071 s decode for 326 pieces).
**The plan's own §13 forbids building a measurement tool, so A4 as written is either not answerable
from the artifact or not permitted.**

**And the precedent shows the shape of the failure.** `adoption_measure_b.py:103-160` reloaded every
analysis region and the ground truth to recover **one** extra bit — whether our local key is correct —
and still emits a forced two-way `factor_hint` (`:149-150`) that **structurally cannot express a
multi-cause run**.

**The record refutes per-layer attribution on its own case.** `CLAUDE.md`'s cross-layer-budget caveat
partitions the failing set across Layers 1–5; its own 2026-07-10 correction states that **over-grabbed
segmentation corrupts the BASS** — the very cue the partition uses to book a case as bass/inversion or
as function-only — "so some of what this caveat books as reaching Architectural Layer 5 is resolvable at
the segmentation layer" (register entry **D-564**). **The classes are not mutually exclusive and the
record says so.** Add **D-576**: root and bass are largely key-independent, so a root-governed run list
systematically under-represents key-caused failure, and any clustering over it under-weights the key
decision.

**Expected multi-causal share (Task 3.3's number): HIGH.** On the one population where per-case cues
were counted, Baroque shows 24 cue hits over 16 separable cases → **≥ 50 % fire two or more cues**;
Jazz 11 over 8 → ≥ 37.5 %. Those are floors, not estimates, since a hit can only land on a separable
case. **CANNOT ESTABLISH the actual fraction over the 4547 runs** — no per-run cause labelling exists
in the repository, and computing one is outside this batch's bars.

**And on a joint estimator the question is not well-posed.** The decode chooses key, mode, chord and
segmentation together, so a failing run is a wrong **path**, not a wrong decision. "Which decision it
turns on" is a counterfactual — re-decode with one factor forced and see whether the run flips — and
that is a measurement of the analysis.

---

### L5 — "The annotation schema is a valid enumeration of what the analysis must decide." → **REFUTED**

**The schema is a LABEL schema, not a DECISION schema.** Both formats record the outcome — a chord label
placed at an onset — and record essentially none of the decisions that produce it. **The gate runs on
the rntxt path** (`a8_rebaseline_measure.py:383-409`), the narrower of the two: no figured-bass column,
no pedal, no cadence, no phrase end, no duration.

Decisions the analysis must make that **no** annotation field reflects:

| decision | annotation field |
|---|---|
| **Where a harmony boundary falls** | **NONE.** Only an onset is recorded; span ends are reconstructed by our own comparator as the next onset (`compare_analyses.py:625-631`), and the gate metric is deliberately built to be invariant to the boundary decision (`compare_rn.py:687-695`). Two annotators of chorale 001 disagree on the row set at bars 3 and 8 — the decision showing up as data rather than as a field. |
| **Which sounding tone is a non-chord tone, and of which ornament class** | **NONE.** No per-note annotation anywhere. The bracket syntax `[add4][no3]` occurs **zero** times in the whole Bach-chorale gate corpus. |
| **Whether to abstain** | **NONE.** `.` / `~` / `@none` are silence markers. Annotator uncertainty exists only as prose `Note:` lines — 1448 of them across 370 chorale files — all discarded. |
| **Confidence** | **NONE**, against `keyConfidence`, `chordScore` and `chordScoreMargin` on our side. |
| **Which alternatives are carried** | At most **one, unranked**: `alt_label` (populated, never read), 286 rntxt `var` lines (explicitly discarded), and a whole parallel `analysis_BCMH.txt` reading per chorale (never opened, `dcml_parser.py:620`) — against a ranked candidate list on our side. |
| **How much context to load; the effort setting** | **NONE, and none possible.** |
| **Candidate admission** | **NONE.** Only the chosen label is recorded. |
| **Tonicization versus modulation** | Outcome recorded, decision not: no scope, no confirmation, no hesitation — distinguished by a mechanical persistence rule. |
| **Enharmonic spelling of the root** | Determinate in the TSV as line-of-fifths integers, but the parser reduces to pitch class mod 12 and the governing root axis is spelling-blind by construction. |

The corpus's own documentation states its analyses are "a reductive act that includes a good degree of
subjective reading … not in any sense 'definitive'" (`when_in_rome/README.md:309-311`), so the gap is a
property of the ground-truth measurement tool and not of these particular files — which is principle #21
arriving at exactly the place A4 proposes to lean on.

---

### L6 — "The delegation-bar home population is the right document set." → **REFUTED**

Both routes fire, at the generated artifact (`tools/audit/decisions/home_classification.json`: 146
entries over 34 documents, 127 contract-home / 19 gap; 23 documents hold at least one admitted section,
11 admit nothing).

**Documents that specify the analysis and are NOT in it.** **`ARCHITECTURE.md` itself is excluded by
construction** — 161 live entries are classed `home_is_layer_spec` and are not in the home population at
all — as is the layer-specification half of `docs/scoring_model.md`. **This alone is decisive**: a
document set assembled to reconstruct the specification cannot exclude the canonical specification.
Beyond it: `cowork_layer1_note_model_design.md` and `cowork_layer2_slicing_design.md` — both as-built
layer contracts **explicitly delegated at `ARCHITECTURE.md:1569` and `:1695`** — dropped out of the
population when their entries retired; and a set of built-but-undelegated analysis designs
(layer1_extend, layer3_reachback, layer2_reslice, types_header, layer3_keymode_impl) is reached only by
a glob pattern, which `CLAUDE.md` rule (k) says confers nothing.

**Documents in it that specify nothing about the analysis.** `cowork_engage_arc_plan.md` (3 entries),
`cowork_score_census.md` (11), `cowork_structural_integrity_audit.md` (1),
`cowork_notation_adoption_increment.md` (3), `docs/llm_integration.md` (7) — **25 entries**, or 33
counting `cowork_prefit_gates.md` and `cowork_stage5_fitter_design.md`.

**The plan's own words are what make this bite.** A1 says "Read that derivation rather than listing
documents by hand." The derivation answers *where is a recorded decision homed*, which is a different
question from *which documents specify the analysis*. **And the sibling artifact
`tools/audit/decisions/outstanding_delegations.json` is STALE** — 190 entries, pre-dating the 2026-08-16
soft discard — so an A1 that reads the delegation artifacts without knowing which is live imports a
superseded population.

---

### L7 — "Deriving blind before reading beats the reverse." → **REFUTED**

**First, it is mis-classified.** `CLAUDE.md` names
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` **§3** as the ruled phase
definitions' ONE home. Inside §3, the implementation-blind rule appears three times: as the pilot's
"**NOT ALLOWED: reading implementation-derived material inside the deriving session**" (§3.2), as the
same constraint on the detail-specification phase (§3.4), and as a standing constraint over every phase
— "**The implementation-blind rule binds every deriving session**" (§3.8, whose own heading marks it
AUTHORED-restating-ruled-ground). Plan §2 lists it as authored and §15 offers it for refutation. It is
not the plan's to assume or to concede. *Stated at the width the record uses:* the surface's §6 also
proposes a formal supersession of eighteenth-stop Ruling 10 by derivation-first, **but §6 is outside §3
and this session did not open the ruling record to establish whether that decision was taken** — so no
weight is placed on it here.

**Second, on the merits, for the load-bearing sections.** The plan's own §1 fact table is largely a list
of measured **dead ends**: a wider search cannot reach the arpeggio root failure because the wrong
reading is the global optimum; the third-above ambiguity is non-local and two discriminators were built
and both regressed; **the progression contradiction does not predict which root is correct** (D-490,
FALSIFIED). Blind derivation from music theory produces the *opposite* of the third — a progression
grammar that predicts roots is what theory suggests and what measurement refuted. The same holds for the
counted-quantities block: nothing in music theory settles that the bass factor is evaluated per event
rather than per segment; its whole defense is a measured semi-Markov length bias. **For those sections
the blind pass produces statements B3 must withdraw and the content arrives by salvage — the check
dominating, which is L7's own stated refutation condition.**

**Third, and this is the ground that reaches furthest: blindness is UNVERIFIABLE.** Guardrail 4 requires
sources declared before reading and never extended mid-pass. **Reading leaves no trace.** No party —
including the session itself in hindsight — can detect a breach, and the plan builds no mechanism that
could, because guardrail 11 makes proposing one "itself the tell firing". B3 is declared "the
measurement of whether the derivation method can be trusted at all", and **it measures nothing unless
blindness is established.** Under #19 a thing merely unfalsified is not established.

*The honest qualification:* ground (b) does not reach theory-settled sections. But the plan's own §0
already assigns those the **Shallow** tier, so the blind-first ordering buys least exactly where it might
hold.

---

### L8 — "Phase A terminates." → **REFUTED, measured**

Measured over 13 specification documents by read-only git history query — the one cheap measurement the
dispatch authorises at Task 3.5.

- **229 unique commits** touch the 13 documents; **150 delete at least one line**; **15,483 lines
  deleted** across **844 contiguous deletion sites**; **38,252 diff lines** in total.
- To enumerate every section ever deleted, **150 commit-diffs must be read**. That is an exact floor —
  the 79 zero-deletion commits provably removed nothing.
- **The cost driver is classification, not reading.** Deletions here are frequently **relocations**:
  `CLAUDE.md` carries explicit "ARCHIVED → `CLAUDE_ARCHIVE.md`, N line(s)" markers, and five append-only
  archive documents (24 commits, 6,104 added lines) are the standing destination. **Each of the 780
  non-rewrite sites needs a destination cross-check before it can be called deleted rather than moved.**
- `ARCHITECTURE.md` carries 13,725 of the deleted lines, **90.3 % of them inside two whole-file
  rewrites** — one line-ending normalization (semantically null) and one 2026-06-21 as-built sync
  (del 5828 / add 5865) **in which any dropped section is invisible without a section-by-section
  before/after comparison**.
- **Verdict: 12–24 hours, i.e. 2–4 sessions minimum, for 13 of 25+ candidate documents**, against a
  declared budget of **one** session for A1–A3.
- A triaged variant — deletion sites of 15+ lines only, 23 of them outside the rewrites — fits ~1.5–2 h,
  **but the 15-line threshold is the measurer's own cut and is directly counter-evidenced by 4- and
  5-line blocks the record itself names as archived sections** (`CLAUDE.md:60`, `:467`). Under #19 it
  would need establishing before it could be used.

**And the budget was declared against a population that does not exist yet:** which documents are in the
A1 set is A1's own output, so the sizing could not have been taken before the plan was written and was
not.

---

### L9 — "Depth can be decided BEFORE reading." → **REFUTED**

**Its stated basis is circular.** Prior-attempt density is derived from "the size of the declared source
list at B1, **which exists before any reading**" (§0). But B1's source list is "the passages of every A1
document covering the section" — and establishing *which passages of every A1 document cover a section*
requires reading those documents. At best a heading-level match exists before reading, and L1 has just
shown what the headings are.

**A second derived axis fails independently.** Error mass comes from A4, and L4 refutes A4's attribution.
Two of the four derived axes are therefore unavailable or unsound.

**The measured counterexample.** The contestedness of the joint-estimator section is invisible from
headings, from blast radius, from error mass and from source-list size, and visible only on opening it:
rule (d)'s declared unsettled tension with §5.7a (`:335-338`), and rule (c)'s "**has no specified form
anywhere in this architecture and no recorded basis**" (`:309-313`). **A section whose defect is a HOLE
has no advance signature at all** — nothing in a heading, a dependency order or a source count announces
that the record is silent where a specification is owed.

**And the plan concedes the point without measuring it.** §10's tier branch exists precisely because a
section may open and prove to need a deeper tier. With no measurement of how often that fires, the plan
cannot distinguish a tier system from a delay — which is L9's own stated refutation condition, and the
plan supplies no evidence against it.

---

### L10 — "Three tiers are enough, and the five axes are the right axes." → **REFUTED**

**Axes that change the answer and are on neither list:**

1. **Whether the section's subject is LIVE or DORMANT.** `docs/scoring_model.md`'s ratified banner:
   "Its mechanism content describes the LEGACY vertical scorer, which is **dormant on both production
   surfaces** since 2026-07-26/27; its §8 constraints and dead ends remain in force". `ARCHITECTURE.md`
   §4.1 and §4.2 specify legacy classes. Whether a section describes the shipped arm changes the depth
   owed enormously, and it is not an axis — **the plan's open question 5 asks it as a question about one
   document instead.**
2. **Establishment status.** §8 declares every hand-set scoring magnitude **UNFALSIFIED, NOT
   ESTABLISHED**. A section whose content is unestablished needs different treatment from one whose
   content is measured, and #19 is what makes the difference binding.
3. **Contestedness / openness** — rule (d)'s declared tension and rule (c)'s hole, above.

**Sections that fit no tier:**

- **A pointer section.** At least nine dated "Delegation pointer (the fifth home case…)" blocks exist.
  Shallow reads "current text and register entries" and returns a pointer; the content lives in another
  document. The tier ladder runs on **history depth**, and this section's depth question is **delegation
  depth**, which no tier expresses.
- **Sections that are not about the analysis at all** — §3.1, §3.2, §13 File Persistence, §17 Coding
  Standards, §18 Contributing, §10.0 Inference Demo Mode. Blast radius on the analysis is zero, error
  mass is zero, theory-settlement is not applicable. **No axis assigns them a tier**, and A2's mechanical
  enumeration puts every one of them in the frame.
- **`docs/scoring_model.md` §8** (327 content lines, 34 enumerable items), which binds a **future
  rebuild by prohibition** while asserting nothing about the live arm. Its depth question is neither
  history nor code sites; it is "what may a later design not attempt".

---

## 3. Task 2 — field five judged from the DELTA side

**Registered expectation E2.** Per-statement verdict on whether **conforms / diverges / not implemented
/ present in code but in no statement** is returnable **from field five alone, without interpretation**;
and, where not, what field five would have to carry instead.

| | field five sufficient? | what actually happened |
|---|---|---|
| **S1** boundary rule | **NO** | Two failures at once. The clause names "the boundary-proposal site", and the live arm has **two** sites with opposite answers — proposal is exhaustive enumeration up to a segment cap of 4 and tests nothing (`jointdecoder.cpp:734`); scoring is a fitted `beat_class → P(boundary)` table (`jointdecoder.cpp:331-333` → `jointadapter.cpp:484-500` → `jointtables.h:111`), whose four ordinal classes are `downbeat / mid_strong / other_tactus / sub_tactus` (`jointdecoder.cpp:44`). Deciding that those classes "test metric weight" is an interpretation: **the code names no quantity called weight or strength.** And the stepwise clause has a near-miss two files away — a step/leap covariate exists (`jointfactadapter.cpp:275-319`) and is combined with metric class in one back-off key (`jointprimitives.cpp:487`) — but it is part-scoped, magnitude-only (≤2 semitones), and feeds the **emission** factor (`jointdecoder.cpp:301`), never the boundary factor. A reviewer reading the clause loosely returns *conforms*; the *diverges* verdict rests on the words "within the same beat" and "resolution". |
| **S2** knowledge item | **NO** | "DATA rather than code" versus "literals in source" is **not exhaustive, and the live store is both** — a generated table whose JSON bytes are embedded verbatim in a generated source file (`jointembeddedartifacts.cpp:23`, `:50`) and parsed at load. Consulted at analysis time via `chordTransLogp` (`jointadapter.cpp:353-392`, called at `jointdecoder.cpp:799`). A reviewer applying "literals compiled into source" literally returns the opposite verdict. A second near-miss: a hand-written progression catalogue **does** exist (`harmonicvocabulary.cpp:208-259`) and is declared DORMANT with no production consumer. |
| **S3** enablement constraint | **YES — the only one** | Fully mechanical. `RecordSegment` and `NotationRecord` (`jointnotationrecord.h:79-154`) carry **no** status field, and a case-insensitive search for `unvalidated\|establishmentStatus\|EvidenceStatus` across `src/` returns **zero hits**. Verdict **NOT IMPLEMENTED**, measured against `ARCHITECTURE.md:1254-1258`. The only interpretation needed was declining two near-misses — `RecordProvenance` (`:59-64`, a different quantity: which fitted artifacts produced the analysis) and the internal `BoundaryCell::reliable` flag (`jointtables.h:71`), which is never published. **The property that made it work: the statement is about the existence of a named field, not about behaviour.** |
| **S4** numeric threshold | **NO** | The clause presumes a count; **the code's threshold is not a constant** but `std::min(2, popcount(*info.mem))` (`jointdecoder.cpp:445`), so "at least three" is falsified while "N = 2" holds only for classes with two or more member pitch classes. A second unforced reading: filter (1) at `:438` is itself a 1-of-1 test on the root specifically, so "N" is arguably *two including a named tone*. The evidence read is **onset** pitch classes, not sustained ones. And `ARCHITECTURE.md:309-313` records this very rule as having **no specified form anywhere in this architecture and no recorded basis** — so the delta's other direction (*present in code but in no statement*) is already the record's own verdict. |
| **S5** abstention rule | **NO** | `rootPc` is `std::optional` on both the decode and the record surface (`jointdecoder.h:114`, `jointnotationrecord.h:87`), so **the type alone reads as an abstention path**. The NOT-IMPLEMENTED verdict comes from admission filter (1) (`:438`) making the empty case unreachable — code the clause cannot see. The only decline is whole-decode failure (`:838-842`), which is all-or-nothing. The near-miss is on the other arm: the dormant slice decoder carries a full trichotomy `SliceDecision::{Commit, Inherit, Abstain}` (`chordslicedecoder.h:363-367`). |

### The replacement form, proposed by the party that would run the delta

Field five as specified is one sentence of prose. **It needs four sub-fields, and one more that the five
probes make unavoidable:**

- **ARM** — `joint` / `legacy-live` / `legacy-dormant`. Three of the five probes have different answers
  per arm, and **three live source files still declare themselves DORMANT** against a live default of
  `true` (`composingconfiguration.cpp:178`), so the arm cannot be recovered from the code's own text.
- **SITE** — a **named symbol** (function, struct field, table), never a description. "The
  boundary-proposal site" resolved to two sites with opposite answers.
- **OBSERVABLE** — what the check actually reads. For S1: *does any argument of the boundary factor
  derive from pitch?* That is answerable without deciding what "metric weight" means.
- **DECISION RULE** — the predicate over the observable, stated so that the verdict is a computation.
  For S4: *"FALSIFIED IF the admission predicate at `candidateStates` is not exactly (root sounds) ∧
  (|members ∩ onsets| ≥ min(3, |members|))"* — a predicate, not a number.
- **NOT-FALSIFIED-BY** — the named near-miss the clause must not be satisfied by. **Every one of the
  five probes had such a near-miss, and in three of five it lived in a different file from the true
  site**: the step covariate for S1, the dormant progression catalogue for S2, `RecordProvenance` and
  `BoundaryCell::reliable` for S3, the dormant `SliceDecision::Abstain` for S5. Without this line the
  delta's most likely error is not a wrong verdict but a **right verdict against the wrong object**.

**One consequence for the plan's own sequencing.** A6 proposes to prove the format on five statements
Cowork writes. Three of the five interpretations above could only be resolved by reading code — which is
the delta, not the format test. **A format test run by the side that will not run the delta cannot
establish that field five is checkable**, and this dispatch is the evidence: the insufficiency was found
by tracing the code, not by reading the clauses.

---

## 4. Task 3 — feasibility of A4, A5 and the budget

### 3.1 Can the decisions the implementation makes be enumerated as a reconcilable population?

**On the code side, YES — and most of it is already paid.** Two generated enumerations already run in
opposite directions and have **never been joined**: `tools/audit/gen_inventory.py` (functions, numeric
literals, struct fields, branches, cross-layer calls — 14,283 rows over five runs, 6,178 dispositioned
for `src/composing`), and `tools/audit/decisions/gen_decision_harvest.py` (15,224 decision claims from
prose and code comments, clustered to 14,460). `tools/param_manifest.json` is the proof of concept: 78
rows, each with name, `file:line` site, family, value at source, consuming path and fit/frozen status —
and the Layer-4 audit **already ran the both-ways reconciliation against it**, finding three constants
registered in code and absent from the manifest. For one decision class, on three files.

**Cost to finish the code side.** 42 of 129 non-test source files (9,821 lines, 26 %) have never been
deep-audited, and they are the worst ones to be missing: `postscoringgates.cpp`,
`harmonicfunctionlayer`, `harmonicsegmenter`, `harmonicvocabulary`, all of `voiceleading/`,
`paramoverride`, all of `intonation/`, the top-level configuration. At the measured 0.22 rows/line that
is ≈2,170 further rows, ≈3 sessions at the recorded disposition rate of 700–900 rows/session.

**What would make it infeasible is the JOIN, not the population.** A code row's identity is
(file, line, kind, name); a claim's identity is a Markdown block, and **98.7 % of the 14,460 claim
clusters are singletons. There is no key.** The one artifact that has a join key — the parameter
manifest's `file:line` site — drifted and had to be re-cited symbol-led (OI-138), which is the whole
problem in miniature.

**And for the live arm the question is largely misdirected.** The joint estimator is a closed 22-file,
4,917-line subtree with **13 named weights and roughly 6 authored constants**, because its behaviour
lives in 154 KB of embedded fitted table data, not in code. So "the decisions the implementation makes"
is, on the arm that ships, mostly a question about **table values**, which no code enumeration reaches.

**One discrepancy to resolve before any such enumeration is trusted:** the Layer-4 manifest inventories
2,121 rows over its 10 deep files while the three Layer-4 disposition files sum to 1,865 — a **256-row
gap** whose cause is stated nowhere.

### 3.2 Can the ground-truth annotation schema's fields be enumerated from the corpus data?

**YES, cheaply — it was done in this dispatch** (§2, L5): a 12-field parsed record over a ~30-column TSV
schema and a narrower rntxt schema, with the gate running on the narrower one. **But it does not answer
what A4 wants it for.** Enumerating the fields establishes what the annotators *recorded*; A4 uses it as
"a population a frame can be reconciled against", and L5 shows the population is of conclusions, not of
decisions. **Feasible and nearly free; sound only as a check on the label vocabulary, not as an
enumeration of what the analysis must decide.**

### 3.3 Can the failing runs be clustered by which decision they turn on?

**NO from the committed artifact** (§2, L4): eight fields, one of them cause-bearing, and that one
computed from our own pitch-class set. **Attribution requires a full corpus regeneration** (the corpus is
gitignored; ≈1071 s decode for 326 pieces) **plus re-derivation of the key, bass and boundary verdicts,
plus the musical score itself for spelling** — and the plan's §13 forbids building a measurement tool.

**Expected multi-causal share: HIGH — floor ≥ 50 % on the one population where per-case cues were
counted** (Baroque 24 hits over 16 separable cases; Jazz 11 over 8 → ≥ 37.5 %), with the record's own
2026-07-10 correction (D-564) establishing that the classes are not mutually exclusive and D-576
establishing that the root-governed list under-represents key-caused failure. **CANNOT ESTABLISH the
actual fraction over the 4547 runs.** Since error mass per section feeds **both** the ordering and the
depth tier, this is not a marginal input — it is the load under two of the plan's four derived axes.

### 3.4 Is A5's sample of 60 the right size, and is the STOP threshold of more than ten defensible?

**The size and the threshold do not fit each other, and the threshold contradicts the plan's own text.**

- **Power.** With n = 60 and a STOP at more than ten unplaceable (> 16.7 %), a missing axis covering
  **10 %** of out-of-frame statements gives an expected 6 unplaceable, and the probability of reaching 11
  is about **3 %** — the test essentially never fires. It acquires usable power only at a true
  unplaceable rate of roughly **20–25 %**. **A5 detects only a very large missing axis.**
- **The internal contradiction.** A5 states "**An unplaceable statement is a finding about the FRAME**" —
  one is a finding. §10 states that fewer than eleven unplaceable means the frame is not the wrong frame
  — ten are not a finding. **The same plan says both.**
- **The plan's own founding instance refutes the threshold.** §3 records that "the gap that produced v2
  was found by placing **one real example** — a chord-progression library — and watching it not fit."
  Under this threshold that discovery would have been declared not a finding.
- **#24.** A count of 10 versus 11 out of 60 differs by roughly a third of one standard deviation. A
  bright line inside sampling noise is a difference that is not a finding, which principle #24 forbids
  resting a decision on. The plan reports no uncertainty range on the sample.

**Verdict as asked: the threshold is arbitrary as stated** — not merely unmotivated, but inconsistent
with two other sentences of the same plan. **No replacement number is proposed here** (D-658: where the
record does not settle a question, the surface returning it gathers facts and makes no recommendation).

### 3.5 Is the Phase-A budget of three working sessions realistic?

**NO**, on measurement, not on impression.

- **A3 alone is 2–4 sessions** for 13 of 25+ candidate documents (§2, L8: 150 commit-diffs, 38,252 diff
  lines, 780 sites needing a move-versus-delete cross-check), against a declared budget of **one**
  session for A1–A3 together.
- **A4 is not deliverable at all as written** (§4.3): its third limb needs a corpus regeneration and new
  derivation, and its second limb answers a question L5 shows is the wrong question.
- **A6 is the cheapest limb and is substantially discharged by this dispatch**, at the cost of one
  session's reading — which is itself the finding that A6 cannot be run by the side that authored the
  statements.
- **And the budget was set against an unknown population:** which documents are in the A1 set is A1's
  own output. **Guardrail 5 requires every phase to carry a declared budget; §11 declares no Phase-B
  number at all**, so the guardrail is unmet by the plan itself on the larger of its two phases.

### 3.6 Are the eleven guardrails checkable from the executing side?

| # | checkable? | note |
|---|---|---|
| 1 | **YES**, at the diff | statements + open questions + findings note, nothing else |
| 2 | **YES**, but **cannot comply as written** | see below |
| 3 | **YES**, at the diff | no new tool file, no edit under `tools/` |
| 4 | **NO — and it is the load-bearing one** | see below |
| 5 | **YES**, and **already unmet** | §11 fixes no Phase-B number |
| 6 | **YES** | a done condition either exists in the unit file or does not |
| 7 | **YES** | a ruling either appears in the record or does not |
| 8 | **YES**, at the diff | one path per unit |
| 9 | **YES**, and it is what makes L3's coupling unrecoverable | a closed unit cannot absorb a later-found cross-section constraint |
| 10 | **YES** | frame additions are visible |
| 11 | **YES**, but **self-sealing** | see below |

**Guardrail 4 is undetectable.** "Sources and tier declared before reading; never extended mid-pass."
**Reading leaves no trace.** No party — the executing session included, in hindsight — can establish
that a pass read only what it declared. B2's entire method rests on it, and B3 is declared "the
measurement of whether the derivation method can be trusted at all", so **the plan's central
measurement is downstream of an unestablishable premise** (#19).

**Guardrail 11 protects that hole.** "A proposal to build something that checks these guardrails is
itself the tell firing." So the one guardrail that cannot be verified is guarded by a clause forbidding
the act that would verify it. Against D-436 — a mechanism is judged on three **measured** conditions —
and against #19, the project's standing position is that a rule enforced only by exhortation is not
established. **This is the guardrail I would be unable to comply with in the sense that matters: I could
obey it perfectly and no one, including me, could ever know.**

**Guardrail 2 collides with two standing rules.** "Findings attach to their section; **no numbers, no
rows**." The open-items register's rule (c) requires every newly discovered issue to get an index row
**and** its detail file in the commit that records the discovery, and **D-641** requires a finding
bearing on the analysis to be **SURFACED whatever its size**, and an apparatus finding to be **ROWED AND
LEFT** unless the worth test discards it. A finding made during a pass that bears on the analysis cannot
be left attached to a section. **As written, guardrail 2 instructs a breach of the register's rule (c).**

---

## 5. Findings from this review — reported, not rowed and not numbered

Per the dispatch: no finding number is allocated and no open-items row is created. The first two bear on
the analysis or on an instrument a measurement depends on (D-438's test) and are therefore **surfaced**;
the remainder are apparatus and are recorded here only.

**(1) SURFACED — three live source files declare themselves DORMANT.** `jointdecoder.h:43` "DORMANT (no
production consumer)", `jointtables.h:44-45` "This module is DORMANT — no production path reads it",
`jointnotationproducer.cpp:40` "this increment is dormant" — while `composingconfiguration.cpp:178`
defaults `USE_JOINT_NOTATION_RECORD` to `Val(true)` and `jointnotationrecord.h:47-49` asserts LIVE. A
specification/code comparison that trusts a file's own self-declaration answers against the wrong arm.
This is precisely the comparability principle #10 exists to protect.

**(2) SURFACED — `CLAUDE.md` principle #21's commissioning clause still names a superseded phase
numbering.** #21 says the ceiling measurement "**OPENS WITH PHASE 2**, desk simulation first". Under the
six-phase structure ruled 2026-08-15, phase 2 is **the pilot on `docs/scoring_model.md`**. The correct
remapping exists — the phase-definition surface §3.5 states that the commissioning "D-231 attached to
'phase 2' maps HERE", the measurement-design stage — **but `CLAUDE.md` is the mandatory session-start
read and the ratification surface is not**, and #21 carries no pointer to the remapping. A session
reading #21 at HEAD lands on a superseded numbering for a #19 obligation that gates every phase.

**(3) The plan's §1 fact "Decisions register: 677 entries" is not true of the register a session
reads.** `DECISIONS.md` publishes "**474 decisions**" and carries exactly **474** rows. 677 is the entry
count of the **data file**, which the retired-entries block's own field
`the_population_before_this_retirement` records as the **pre-retirement** population; 203 entries were
soft-discarded on the user's ruling of 2026-08-16 and are not rendered. The plan then divides 677 into
411 / 182 / 84 and reasons about "the decisions register" from those values — and the artifact it cites
names itself "**THE DECISIONS-REGISTER FILTER, PROPOSED AND NOT EXECUTED**", which the 2026-08-16
retirement subsequently overtook. D-431's citation rule was met; the **label on the row** is what is
wrong, and it overstates the register by about 43 %.

**(4) `decisions/group_P.md` is an orphan, and the retired-entries block states something false about
itself.** That block states: "**Nothing in this block is rendered into the register's INDEX or its group
files.**" `decisions/group_P.md` renders five retired entries — D-154, D-158 and three more, both
verified present in the retired block — in the **live-entry form**, under a banner claiming it is "Part
of the decisions register". The renderer skips a group with no live members (`gen_decisions_register.py`
`if not members: continue`) but does not delete the stale group file, so the INDEX has no `## P.` section
while the detail directory still carries one. Detail entries total 479 against the INDEX's 474.

**(5) A2's "mechanical" heading enumeration is unsafe, and the ToC omits the production layer.** Five
`^# `-matching lines at `ARCHITECTURE.md:896-907` are shell comments inside a fenced code block; the ToC
(`:582-603`) lists items 1..19 and omits the joint-estimator section, the document-governance section and
both appendices.

**(6) `tools/audit/decisions/outstanding_delegations.json` is stale** — 190 entries, pre-dating the
2026-08-16 soft discard — while A1 is instructed to read the delegation derivation rather than list
documents by hand.

**(7) A 256-row gap in the Layer-4 audit** — the manifest inventories 2,121 rows over its 10 deep files
while the three disposition files sum to 1,865; the cause is stated nowhere.

**(8) `ARCHITECTURE.md` §4's numbering is internally broken** — §4.1f at `###` level between §4.2 and
§4.3, a duplicate §4.1d at `:3522` against `:2873`, and seven un-numbered `###` "Phase" headings at
section level.

**(9) `docs/scoring_model.md:87` claims each §8 constraint "carries its own ⚠ LEGACY-subject mark"**; the
twelve original bullets at `:1134-1191` carry none.

**(10) The plan lineage shows load-bearing clauses disappearing with no version recording the loss.**
v1's ten `*Stops:*` clauses — and v1's own statement that the failure is named "**so the guardrail cannot
be softened into general advice**" — vanish at v2 unrecorded. v2's self-declared governing correction,
"`ARCHITECTURE.md` is one of several polluted documents, not *the* polluted document", survives in
neither v3 nor v4. Guardrails 7, 9 and 10 each lose their operative second clause between v3 and v4.
**And v4 carries one flat contradiction:** v1, v2 and v3 all make "every deletion ever made from those
passages" an **unconditional** member of every source list, on the stated ground that "only removals are
invisible … by construction"; v4's **Shallow** tier says "**No history walk**" without answering that
ground, while v4's own B1 source paragraph still enumerates the deletions the Shallow tier forbids
reading.

**(11) A material conflict under the plan's open question 4, recorded in neither document.** The curated
boot list draft excludes, **as implementation-derived**, `CLAUDE.md`'s gate block and
`docs/scoring_model.md` — and those are exactly the two sources v4 §8 records as **already read and
standing for the whole programme**, with measured values from both carried into v4 §1 (the production
baselines; three §8 dead ends including D-490). **A v4 B2 session therefore cannot be a
boot-list-conformant implementation-blind session as v4 is written.**

---

## 6. Declared departures

1. **The A1 check and the L8 measurement used the shell.** The dispatch says "Running anything is not
   [permitted]" while ordering the A1 check "at content-addressed objects" as the first act and
   authorising "one cheap measurement" of the deletion history at Task 3.5. Both were performed
   read-only: `tools/audit/changed_paths.py` (the D-253-sanctioned enumeration, which by construction
   cannot return file content) and git history queries. **Nothing was written, staged or regenerated.**
   The repository's own shell-read guard fired once, correctly, on an attempt to inspect a JSON artifact
   through `python -c` with a literal repository path; the read was redone with the file tools.
2. **Evidence gathering was delegated to nine read-only subagents; the mandated reads were not.** The
   thirty-third handover block records that reading `CLAUDE.md` and `DECISIONS.md` by delegation is a
   **DEPARTURE and not a discharge**, so this session performed every mandated read itself. The
   delegation covered evidence sweeps only, under an explicit bar on edits, builds, tests and
   measurement tools. **Verdicts resting on a sweep's citations that this session did not personally
   re-open:** the failing-run field list and the multi-causal cue tallies (L4); the annotation field list
   (L5); the home-population counts (L6); every value in the deletion-history measurement (L8); the code
   inventory values (Task 3.1); the S1–S5 code sites (L2, Task 2); and the arm-identification citations behind
   finding (1). **Verdicts this session
   established at the primary source itself:** the joint estimator's standing rules and the Table of
   Contents (`ARCHITECTURE.md:265-605`), the ruled six-phase structure
   (`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §§0, 3.1–3.5, 3.8),
   `DECISIONS.md`'s row count, the backbone data file's population and retired-entries block,
   `decisions/group_P.md`, and the fenced-code heading hazard.
3. **`CLAUDE.md` was read from the copy the harness injects as the file's contents**, rather than by a
   separate Read call.
4. **A1's untracked count was reported as the tree carries it** (five files, not four) rather than as A1
   words it — F82 applied rather than repeated. Not a STOP.
5. **Two premise corrections are reported, not corrected.** `ARCHITECTURE.md` is **8,267 lines**, not the
   ~6,500 the dispatch and register prose state (established at the file-tool read terminus, `:8265-8267`
   being the final content, after the repository guard refused a shell line count). And the plan's §1
   "Decisions register: 677 entries" is finding (3) above. Nothing was edited.
6. **No recommendation is made on A5's threshold**, per D-658 — the internal contradiction is reported as
   a fact and the replacement value is left to the user.

---

## 7. The standing self-check, over this session's own reading

**Principles.** **#1/#2** — every verdict is grounded in a primary source read this session or a
citation to a named file and line; no verdict rests on a general argument alone. **#5** — where a
question could be settled by reading rather than by reasoning, it was read (the joint estimator's rules,
the phase-definition surface, the code sites). **#6** — nothing here is a second home for anything: the
ruled phase definitions, the standing clauses and the register's rules are **pointed at**, never
restated. **#12** — no finding is discarded; the ones that could not be established are stated as
CANNOT ESTABLISH (the actual multi-causal fraction; the origin of §4's numbering anomalies; whether the
13 measured documents are the A1 set). **#13** — the two surprises this review met are surfaced as
findings (1) and (2) rather than built around. **#17(f) / D-431** — every value is cited to the artifact
or file it was read from; the deletion-history and inventory values are the sweeps', named with their
sources, and no value was carried from memory. **#19** — the establishment status of every borrowed
value is declared in §6.2; the ones taken from sweeps are marked as such rather than presented as this
session's own. **#24** — the one statistical claim (A5's power) is stated as an approximate probability
with its assumption named, and the report asserts no difference between two measured quantities.

**Conventions.** American English. No self-invented label, abbreviation or numbering scheme — the
identifiers used (L1–L10, S1–S5, A1–A6, B1–B7) are the dispatch's and the plan's own. Music-theory words
are reserved: *score* is the music (the numerical sense appears only as `chordScore`, quoted as a code
identifier); *key* is tonality; *measurement* is used for the gauging sense and *bar* for the metric
unit; *mode* is the musical mode; *register* appears only as *the open-items register* / *the decisions
register*, in full; *root* is the chord root and *underlying cause* is used for the other sense;
*instrument* is not used for a measurement tool; *note* is a pitch event and *entry* / *annotation* is
used for the other; `stem` appears only as a quoted field name of a generated artifact.

**The figures-and-premises rule.** No quantity was transcribed from a secondary surface. The one place a
value is restated rather than pointed at — the deletion-history measurement in L8 — is this dispatch's
own ordered measurement, taken for this report and existing nowhere else, and it is reported with its
method and its stated floor.

**The file-tools rule.** Working-tree content was read with Read, Grep and Glob throughout. Shell use was
confined to the sanctioned enumeration tool and to read-only git history queries, both declared in §6.1.
The guard's one refusal is recorded there rather than worked around.

**Did this batch produce anything other than this report?** **No.** One file,
`cc_report_plan_challenge.md`; one commit; no `STATUS.md` entry, no close in `cowork_away_returns.md`,
no handover block, no chain table, no register row, no artifact regenerated, and the guard set unmoved
because nothing this batch did touches it.

---

*Provenance: CC, 2026-08-20, at branch tip `891bacc5d2`. Dispatch `cc_instruction_plan_challenge.md`.
Subject `cowork_specification_reconstruction_plan_v4_2026_08_19.md`, unratified. The plan is not treated
as authority for anything, and nothing it describes was executed.*
