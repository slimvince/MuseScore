# The L2-S48 family — L2's publication covers exactly the working span — ratification surface, 2026-10-09

> **STATUS: RATIFICATION SURFACE (a reading for the user; nothing in it is ruled until the record says so).**
> Cowork, 2026-10-09 (Stockholm), the sitting that booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_twenty_eight.md`. Written under the L2 route
> ruling of 2026-10-04 (Alternative A: disposition rulings by family, one surface per turn). **Tags:**
> *checked* = read at the object by this sitting; *relayed* = taken from a record and not opened here;
> *my reading* = this side's inference. Nothing here is applied: the reading file's rows are re-marked, and amended
> texts written, by the application dispatch the route ruling names as its step 2. No decisions-register identity
> is allocated. **This is the last family in statement-number order** (entry 328 §3).

---

## §A.1 What this family is

**The derived statement**, quoted whole from `cowork_blind_derivation_l2_2026_09_27.md` (repository root, lines
1163–1173, *checked*):

> **L2-S48. L2's publication covers exactly the working span. The result after any sequence of enlargements equals a
> single fresh run over the final loaded span.**
> - *Defense.* "The analysis output covers exactly the selection" [RULED — D-260]. "The result after any sequence of
>   extensions must equal a single fresh run over the final loaded span" [RULED — D-264]. The input contract gives L1's
>   half of the same invariant [RULED — IC beside S-53, Ruling 46 (ii)].
> - *Source class.* Given — design intent.
> - *Status.* Settled.
> - *Premise.* L2's search is deterministic. L2-S43's tie rule makes it so.
> - *Falsifier.* CODE. **Observable:** the publication after enlargements against a fresh run. **Decision rule:**
>   falsified if they differ in any published field. **Not falsified by:** differences in internal caches.

The derivation's terms table defines the **working span** as "The stretch of music the caller asks the analysis to
read. Output covers exactly this span, and music loaded beyond it is evidence only (D-260, pack member 05)" (line 28,
*checked*). The working-order record of 2026-10-05 states: "**The working span:** given in the record's own positions
(Ruling 46 clause (i), ruled 2026-09-02)", and adds that reading this as "notated positions" "is the surface's reading
… put to the user with the surface and not separately ruled" (its §1, *checked*). *(Corrected at the check. Former
wording, preserved (#12): "Since the working-order ruling of 2026-10-05, the working span is given in the record's own
notated positions" — "notated" is that surface's reading, not the ruling.)*

**In plain words.** The user selects some bars. L2 publishes its reading — tonality, chord boundaries, chords, which
notes are chord tones — for those bars and for nothing else. To read the edges of the selection well it may ask for
more music before and after (L2-S22); that music is evidence and is never itself labelled. And the way L2 gets to its
final amount of music must not matter: if it reached bars 16–44 in three steps, the result is exactly what one fresh
reading of bars 16–44 would give.

**The rows.** The comparison's §7 lists, at lines 71285–71288 of `ratification_surfaces/cowork_comparison_l2_reading.md`
(*checked*): **29 AGREES** (Rows 6.14(ii), 6.61(i), 7.34, 7.54(i), 17.34(ii), 21.59(i), 21.61, 22.83(i), 22.84(ii),
30.75(ii), 43.74, 43.77(i), 43.79, 45.1, 45.9(i), 45.13(ii), 45.35, 45.38(i), 45.43, 45.52(iii), 45.64(i), 45.66(i),
45.71, 45.76(i), 45.81, 45.88, 45.89, 49.1(i), 51.60(i)) and **1 DIFFERS** (Row 45.60(ii), proposed UNPLACED).

**Taken in on subject (entry 322 §2: the route cuts ADOPTED — proposed rows by subject):** five ADOPTED — proposed
rows — three whose own current-text axis names L2-S48 as not covering them (Rows 45.5, 45.24, 45.74), and Row 21.60(ii),
whose axis names no statement but whose proposal is the same edit rule as Row 45.74's ("its result equal to a fresh
run"), with Row 45.44(i) travelling with it *(corrected at the check; former wording, preserved (#12): "five ADOPTED —
proposed rows whose own current-text axis names L2-S48 as the nearest statement that does not cover them, or which
travel with such a row" — Row 21.60(ii)'s axis reads only "THE DERIVATION IS SILENT")* — **Row 45.5** (L2 reads nothing outside the music loaded for it), **Row 45.24** (the publication does not
depend on the step size), **Row 45.74** (enlargement and an edit compose), **Row 21.60(ii)** and **Row 45.44(i)**
travelling with it (an edited stretch re-read, the result equal to a fresh run). **35 row-parts.**

## §A.2 The research, searched before writing (entry 319 §2)

- **The derivation's defense of L2-S48 cites rulings only** (D-260, D-264, the input contract's Ruling 46) and no paper
  (*checked*, lines 1165–1167).
- `docs/research_papers/BIBLIOGRAPHY.md` (*checked*): searched for *incremental*, *online*, *streaming*,
  *determinis*, *reproducib*, *selection*, *context*, *window*, *real-time*, *fixed-lag*, *smoothing*, *forgetting*.
  Three hits, each read at its line, none on the subject: a publisher's URL (line 20), Mauch & Dixon's title
  "Simultaneous Estimation of Chords and Musical Context from Audio" (line 58; an audio paper whose "musical context",
  on *my reading* of the title alone — the paper was not opened — is not the stretch of music a caller selects), and a
  "published online" date (line 100). *(Corrected at the check. Former wording, preserved (#12): "\"context\" there is
  the tonality and bass around a chord, not the stretch of music read" — a gloss of a paper not opened, stated as fact.)*
- **The charter says outright that no research source states this requirement.** `FRAMEWORK.md`'s reconciliation table,
  item 13: "Cost scales with the working span; re-analysis is incremental; the working span is extensible —
  **CARRIED FORWARD at stage two.** … it is a product requirement about very large scores and about editing, and **no
  published research source states it.**" (line 1195, *checked*).
- **The one research document on the neighbouring subject** is `ratification_surfaces/cowork_l2_context_convergence_research_2026_10_07.md`
  (L2-S22's stopping rule). Read at its §4.1 to §6 (lines 200–259, *checked*). It bears on Row 45.24 only: its §4.3 says
  "The step-size independence test already owed (D-264; Rows 45.24, 45.72) stays the test", and its §4.1 that a
  "coalescence" check (all surviving readings at the far edge agree on the in-span reading) is what would make the
  principal reading independent of the step, its two-sided form "not derived here".

**So:** L2-S48 is a rule about what L2 publishes and how its result may be computed, not a claim about music; the
searches above found no source on it (*my reading*). Item 13 covers the neighbouring product requirement — cost, the
incremental re-analysis after an edit, the extensible span — and so bears directly on Question 3's subject; it does not
itself name "output covers exactly the selection" or the fresh-run equality. *(Corrected at the check. Former wording,
preserved (#12): "the record holds no source on it and the charter says none exists (*my reading*, resting on item
13)" — wider than item 13's subject and than the searches run. The bullet heading above, "The charter says outright that
no research source states this requirement", is read with the same narrowing: "this requirement" is item 13's.)*

## §A.3 What the record has already settled

**The two ruled decisions L2-S48 restates** (each *checked* at `decisions/group_C.md`, LIVE, ratified by the user
2026-08-02):
- **D-260** (home `cowork_bounded_context_design.md:43-44`): "The analysis output covers **exactly the selection**;
  everything outside it is evidence, never a result."
- **D-264** (home `cowork_bounded_context_design.md:142-147`), verbatim whole: "**Equivalence invariant (the
  correctness guard).** The result after **any** sequence of extensions must equal a **single fresh run over the final
  loaded span** — extension is an optimisation of *"load more, then run from scratch,"* never a different computation.
  In practice the forward cascade is **bounded**: the new context changes inference only where it actually reaches (a
  carried-in key affects the leading-edge slices and decays inward), so only the affected slices re-infer — the same
  locality that makes the stop condition terminate, and which composes with the existing *"re-analyse a sub-range"*
  capability." Its recorded *Why*: "without it, incremental extension could silently produce an answer no single run
  would produce, and the result would depend on the extension granularity rather than on the music."

**Two neighbouring ruled decisions that speak to the step size** (*checked*, same file):
- **D-261**, item 6: convergence "is what keeps the result independent of the extension step size (the equivalence
  invariant, §4)."
- **D-262**: the increment "is an **efficiency knob only**: a larger increment means fewer round-trips (and perhaps a
  slightly larger final loaded span), never a different answer, because convergence (item 6) fixes the result."

**L1's half — Ruling 46 of `records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`** (read at
§3ba, lines 3720–3818; user's words "Agree on recommendation"). Its Position one, quoted: "the contract stated at L1 as
a consequence of purity, L0 gaining no operation." *(Quoted apart, D-643 —)* its "What was decided": "(i) the working
span is given in the record's own positions …; (ii) L1 computed over a larger span is exactly what a fresh computation
over that span yields, so the result never depends on how many steps reached the span or in what order; … (v) the
decision to enlarge, the increment and the stop test belong to the requester, never to L0 or L1 …; (vi) a span edge
that coincides with the record's own start or end is published as such". It adds: "none of D-260 to D-266 is
contradicted in substance, D-264 being clause (ii)."

**Edits, on the L0/L1 side — Ruling 43** (same record, §3ax, lines 3571–3615, read; user's word "Agree"). Its Position
one, quoted: L0 "is built from the record on request and fixed until rebuilt; it observes no editor and detects no
edit; deciding the record has changed and requesting the rebuild, with the changed span R2 needs, belongs to the caller
that owns the record." *(Quoted apart, D-643 —)* its "What was decided": "At the ratification act L0 gains the clause
above, beside S-3 to S-7 as part of the input contract, with a pointer to the bounded-context design for the dirty span
and nothing of that design restated (#6)." Its position three, silence, was "excluded, item 13's *carried forward*
being an obligation to state and not a licence to omit, and a silent product requirement being discovered at the audit
or by a user".

**The charter** (`FRAMEWORK.md`, *checked*): **C-8** — "Cost scales with the working span, not with the whole score.
The analysis runs on the user's selection; a layer needing more music requests an append-only extension of the loaded
music. Whole-score analysis is the degenerate case. Re-analysis after an edit is incremental over the changed stretch
plus a bounded margin." (lines 176–179). **§6.7** — "An edit to the score. Only the changed stretch plus a bounded
margin is re-decided (C-8). The margin exists because the tonality at the edge of a stretch is not fixed by one
settled indication — a tonality established over a stretch of earlier music is what fixes it." (lines 533–535).

**The L2 rulings of this month that bear on it** (each *checked*):
- **Tractability Ruling 1 (ii)** (2026-10-05): "'The end' is the end of the music loaded for the selection — the
  working span with its context (L2-S43), the context extended by convergence (D-261) under the safety cap (D-624) and
  C-8's scaling — not the end of the whole score, unless the whole score is the selection or convergence does not
  settle before the cap."
- **Context-at-the-edge Ruling 2** (2026-10-07, user's word "2"): L2-S22's last sentence becomes "At the top effort
  setting it stops when its in-span publication — the readings, the span-rivals and their masses — is the same after
  an enlargement as before it. …" The same record's Ruling 1 recorded, as the surface's reading, that the risk of a
  convergence test stopping too early "is guarded by the step-size independence test already owed (D-264; Rows 45.24,
  45.71, 45.72)". Its surface §A.9 carried Row 45.24 on, not decided, and Row 45.60(ii) as "not this family's".
- **Weight-meaning Ruling 3** (2026-10-05, user's word "confirmed"), the ruling quoted whole: "The forward override of
  D-339 ('A confident earlier inference can be overturned by decisive later evidence, via one general
  confidence-weighted forward-recompute mechanism') has no site in L2: inside L2 key, boundaries, notes' roles and chord
  are one decision scored over the whole loaded music; at L2's boundary the contract table reads 'L3 → L2:
  **Nothing.**' The framework's general admission of the act (§8.4, Δ8) is untouched." It placed 29 rules of that
  mechanism HISTORICAL, among them Row 5.224 — the old function design's §8: the overturned decision "is **closed for
  that pass**: it is **marked final for the remainder of this analysis pass** (a one-pass closure flag on the
  decision)" (Row 5.224's text read at the comparison, line 7256).
- **Working-order ruling** (2026-10-05, user's word "one"): one reading per notated position; the working span in the
  record's own positions.

**None of the 35 row-parts is placed by an earlier record** (searched: all 39 ruling records of 2026-10 for each row
identity; the hits were other halves — Row 45.13(i) and Row 30.75(i) by context-at-the-edge Ruling 1, Row 45.52(i) by
the no-early-discarding record, Row 45.60(i) by the nothing-from-L3 record — and different rows sharing a prefix, read
at their lines). *(Corrected at the check: the first writing's search left out "30.75"; it was run at the check, one
hit, claim (i). The nothing-from-L3 hit is from the check's search for "45.60". Former wording, preserved (#12): "the
hits were other halves — Row 45.13(i) by context-at-the-edge Ruling 1, Row 45.52(i) by the no-early-discarding record —
and different rows sharing a prefix".)*

## §A.4 The rows (*checked*, each read at its row in the comparison)

### §A.4.1 The 29 that agree

**27 proposed ADOPTED — carried (L2-S48)**, in three groups by what they say:

| What they say | Rows (member) |
|---|---|
| **Output for the selection only; the rest is evidence.** E.g. Row 45.9(i): "A layer **outputs analysis only for the selection**"; Row 43.77(i): "Output covers only the selection"; Row 45.64(i): "Output covers **only 20–40**". | 6.14(ii), 6.61(i) (chord-layer design); 7.34, 7.54(i) (key-layer design); 21.59(i) (`ARCHITECTURE.md` §2.15); 22.84(ii) (`ARCHITECTURE.md` Layer 2: selection membership "derived by the consumer"); 43.74, 43.77(i) (target architecture); 45.1, 45.9(i), 45.52(iii), 45.64(i), 45.81 (bounded-context design); 49.1(i) (output contract: "the data the joint module publishes per analyzed score span") |
| **The whole piece is the case where the selection is the piece.** E.g. Row 21.61: "Whole-score analysis is the degenerate case (selection = score)." | 21.61; 43.79; 45.66(i), 45.76(i), 45.89; 51.60(i) (note-model design) |
| **A re-run is a fresh run; any sequence of extensions equals one fresh run.** E.g. Row 45.43: "The result after **any** sequence of extensions must equal a **single fresh run over the final loaded span**"; Row 45.71: "extending in one big step or several small ones to the same span must give the same result." | 22.83(i); 45.13(ii), 45.35, 45.38(i), 45.43, 45.71, 45.88 |

Readings recorded, none moving a placement (*my reading*):
- **Rows 6.61(i) and 7.54(i)** say "at any size" as well as "the user's selected music". L2-S48 carries the selection
  half; whether L2 can afford any size is OQ-L2-8 (tractability), still open, and D-201's. The comparison's AGREES
  rests on the selection half.
- **Row 45.38(i)** (the requester re-infers with the new music in view) is carried; its other half, the cascade of
  tonality then chord, is HISTORICAL by the comparison (travelling with Row 18.2(i)), not taken in.
- **Row 49.1(i)** is the old output contract's definition of the record; it agrees on "per analyzed span". Its
  other half (the notation path reads it) is RELOCATED to L3 and not taken in.

**2 proposed QUARANTINED, though they agree** (entry 314 §2: follow the proposal):
- **Row 17.34(ii)** — "WHOLE-score decode ONCE; deterministic; NO caching" (`ARCHITECTURE.md`, the record-path
  paragraph), claim (ii) "the decode is deterministic", AGREES with L2-S48's premise. *Audit question, as the
  comparison writes it:* "do two runs of the producer over the same score give byte-identical records?"
- **Row 30.75(ii)** — "no annotations written outside the selection boundary" (`ARCHITECTURE.md`, member 30's passages,
  *Annotate path annotation layers (Roman numeral mode)*), travelling with Row 22.107. *Audit question at Row 22.107:* "on which arm do the section analyzer's
  stabilization, cadence and pivot detection run at the current commit?" Claim (i) of the same row was placed
  QUARANTINED, travelling with Row 22.107, by context-at-the-edge Ruling 1 — the same treatment.

### §A.4.2 The one that differs — Row 45.60(ii)

**The row** (`cowork_bounded_context_design.md` §5, Architectural Layer 5, lines 181–183): "Extension re-runs flow
forward under the §8 one-pass closure (an extension may finalize an open decision, never re-open a closed one — data
supply, not a back-edge)." Claim (i), re-runs flow forward, is placed ADOPTED — carried (L2-S49) — one of the 160
AGREES parts the nothing-from-L3 record (2026-10-07, user's word "confirmed") placed as proposed — not this family's.
*(Corrected at the check. Former wording, preserved (#12): "is ADOPTED — carried (L2-S49), not this family's" — stated
the proposal without the ruling that placed it.)* Claim
(ii): "an extension may settle a decision still open and never reopens one already closed" — **DIFFERS** from L2-S48,
proposed **UNPLACED**: "a disposition would choose between them."

**What the difference is, in musical terms.** Under the old rule, once the old function layer had *closed* a decision
— say it had fixed a chord's function at bar 21 — music loaded later could no longer change it, even if that music
showed the reading was wrong. Under L2-S48, after more music is loaded the publication is whatever one fresh reading of
all the loaded music gives, so a reading at bar 21 can change.

**Why the record already decides it** (*my reading*, from the objects quoted in §A.3):
- The "§8 one-pass closure" the row names is the old function layer's mechanism (Row 5.224: the overturned decision
  "marked final for the remainder of this analysis pass"). **Weight-meaning Ruling 3** found that this mechanism has no
  site in L2 — L2 decides key, boundaries, chord-tone roles and chord as one decision scored over the whole loaded
  music — and placed its rules, Row 5.224 among them, HISTORICAL. Row 45.60(ii) is that mechanism's rule applied to an
  extension.
- **D-264** (ratified) says the result after any sequence of extensions equals a single fresh run — "never a different
  computation". A closed decision that an extension may not reopen would make the result depend on the order in which
  music arrived, which is what D-264 exists to forbid.
- **Context-at-the-edge Ruling 2** has L2 keep asking for music until its whole in-span publication stops changing —
  which presupposes that more music may change what was published.
- **Tractability Ruling 1** and L2-S43: no reading is dropped before the whole loaded music is scored. A "closed"
  decision would keep its rivals from being weighed again against the newly loaded music. *(Corrected at the check.
  Former wording, preserved (#12): "would drop every rival of it" — an absolute about an old mechanism whose rival
  handling was not read.)*

So the choice the comparison left open is already made, the other way: the row is a rule of a superseded design —
**HISTORICAL**, the treatment Ruling 3 gave the 29 rules of the same mechanism.

### §A.4.3 The five taken in on subject

**Row 45.5** (bounded-context design §3 item 1, line 53): "A layer **never reads notes or slices outside the loaded
span.**" — THE DERIVATION IS SILENT: "L2-S48 fixes what L2 publishes over and L2-S22 when L2 asks for more music;
neither states that L2 reads nothing beyond what has been loaded." Proposed **ADOPTED — proposed**: "that L2 read no
event and no slice outside the music loaded for it."

**Row 45.24** (§3 item 8, lines 97–99): "It is an **efficiency knob only**: a larger increment means fewer round-trips
(and perhaps a slightly larger final loaded span), never a different answer, because convergence (item 6) fixes the
result." — SILENT: "L2-S48 equates enlargements that reach the same final span; it says nothing of increments that
reach different ones." Proposed **ADOPTED — proposed**: "that L2's publication not depend on the size of the step by
which it enlarges the music it reads." *(The sentence is part of D-262's ratified verbatim.)*

**Row 45.74** (§8, lines 231–232): "Extension (grow the loaded span) and re-analysis (re-run part of it) must compose
cleanly — an edit *inside* the selection and an extension *outside* it are different operations on the same model." —
SILENT: "L2-S48 speaks to enlargements and not to an edit." Proposed **ADOPTED — proposed**: "that L2's enlargement and
its re-reading of an edited stretch compose, each giving the result of a fresh run over the music it ends with."

**Row 21.60(ii)** (`ARCHITECTURE.md` §2.15, lines 1173–1175): "(R2) re-analysis is incremental over the dirty span plus
a bounded margin" — SILENT. Proposed **ADOPTED — proposed**: "that L2 re-read an edited stretch plus a bounded margin,
its result equal to a fresh run." **Row 45.44(i)** (§4, lines 144–147: "the new context changes inference only where
it actually reaches … so only the affected slices re-infer") — SILENT, proposed **ADOPTED — proposed, travelling with
Row 21.60(ii)**. *(Row 45.44(i)'s sentence is part of D-264's ratified verbatim; it came to the L2 file also through
the L0/L1 side, as Row 62.43 → L0/L1 Row 18.27, checked at line 70817.)*

**Two notes on wording, so the questions below quote the proposals honestly** (*my reading*):
- Row 45.5's "loaded" predates Ruling 39 (L0 holds the whole record; the working span restricts what L1 publishes, never
  what L0 supplies). In the derived layers, the music "loaded for" L2 is the working span plus the context L2 has asked
  L1 for; L1 tiles exactly that (Ruling 40; B8). L2 still reads L0 directly for facts L1 does not define, such as the key
  signature (L2-S47's "Not falsified by"); the proposal speaks of *events and slices*, which are L1's.
- Row 21.60(ii)'s source says "incremental over the dirty span plus a bounded margin" and nothing about equality; the
  words "its result equal to a fresh run" are the comparison's proposal, taken from Row 45.74 and D-264.

## §A.5 What the record does not settle, and what follows without a question

**A. The step-size property is not guaranteed by L2's stopping rule as now ruled.** Context-at-the-edge Ruling 2 stops
L2, at the top effort setting, when the publication is the same after one enlargement (below the top, within a
tolerance). *(Corrected at the check: the setting was not stated.)* A step that adds music changing nothing, while the music that
would change the reading lies one step further, would stop L2 early; a larger step would have reached it, and the two
publications would differ. The research document's §4.1 names a check that rules this out for the principal reading
(its two-sided form "not derived here"); Row 45.72 ("A required test", proposed RELOCATED to the measurement of the
analysis, placed by no record found) is the test. *(Corrected at the check: "RELOCATED" was written without
"proposed".)* So adopting Row 45.24 states a property that a measurement can falsify; if it is falsified, L2-S22's stopping
rule needs strengthening — a later algorithm question, not this one (*my reading*). **Carried, UNSETTLED.**

**B. How large the margin round an edit is.** C-8 and §6.7 say "a bounded margin" and give its reason (the tonality at
a stretch's edge is fixed by music further away). If the result after an edit must equal a fresh run (Question 3), the
margin cannot be a fixed width chosen in advance; it is whatever makes the result equal — the same discovery as at the
edge of the working span (D-261), under the same safety cap (D-624) (*my reading*). That is a consequence of the
equality, not a further choice, and how it is computed is the build's (D-200: a speed-up that leaves the result
unchanged). **Recorded, not put.**

**C. Searched and not taken in** (*checked* at their rows unless stated):
- **The enlargement step, the maximum distance, the oscillation guard and truncation provenance** — Rows 45.22(ii),
  45.23(ii), 45.29(ii), 45.30(i); 2.14(ii), 45.21(i), 45.70, 45.86; 45.21(iv); 45.26(ii), 45.61(ii). All ADOPTED —
  proposed, all about *how L2 asks for more music*, which is L2-S22's subject; the context-at-the-edge surface (§A.9)
  carried them, not decided. Not L2-S48's question. **With this the last family in statement-number order (entry 328
  §3), no family now planned reaches them, so under the route ruling they stay proposals** ("Rows no family reaches stay proposals", route record §2, *checked*) unless the
  user wants them put.
- **Row 21.60(i)** — "that L2's cost grow with the working span and not with the whole piece" (ADOPTED — proposed). The
  cost side: C-8 states it; Ruling 39: "The D-030 reconciliation is not settled here and remains the measurement
  side's"; and OQ-L2-8 (tractability) carries L2's cost. *(Corrected at the check. Former wording, preserved (#12):
  "Ruling 39 reserved \"the D-030 cost reconciliation … to the measurement side\"" — those words are Ruling 46's
  summary of Ruling 39, quoted as Ruling 39's.)* Not this family's. Stays a proposal.
- **Rows 6.61(ii), 7.54(ii)** and their travellers 21.44, 48.46(i) — "that L2's structure … assume no style". Other
  halves of this family's rows; their filing does not depend on this family's question. Stay proposals (no record
  placing them was found: searched the 2026-10 records for "6.61", "7.54", and at the check for "21.44", "48.46" — no
  hit). *(Corrected at the check: the travellers had not been searched.)*
- **Row 9.115(i)** — "that L2's fit be deterministic" (ADOPTED — proposed). Its axis names L2-S43 and L2-S48 only to say
  they make the search, not the fit, deterministic. The fit's subject, not this family's. Stays a proposal.
- **The other halves of this family's rows** — 6.14(i), 17.34(i), 17.34(iii), 22.83(ii)–(iii), 22.84(i), 30.75(i),
  43.77(ii), 45.9(ii), 45.13(i), 45.38(ii), 45.52(i)–(ii), 45.60(i), 45.64(ii), 45.66(ii), 45.76(ii), 49.1(ii),
  51.60(ii): each names another statement or carries its own proposal; none depends on this family's question. Not
  taken in.

## §A.6 What stands, and what the questions would decide

**The method that stands** (the derived statements and the rulings, unchanged by any question below):
- **L2-S48** — L2's publication covers exactly the working span; the result after any sequence of enlargements equals a
  single fresh run over the final loaded span; L2's search is deterministic (L2-S43's tie rule).
- **L2-S22, as context-at-the-edge Ruling 2 amends it** — L2 asks for more music at the edges and, at the top effort
  setting, stops when its whole in-span publication is the same after an enlargement as before it; the safety cap ends a
  loop that does not settle, the publication then marked truncated.
- **L2-S43 with tractability Ruling 1** — no reading is dropped before the whole loaded music is scored.
- **The charter and L2-S47** — L2 consumes "everything L0 and L1 publish. Nothing else." (`FRAMEWORK.md`, L2), and
  never re-derives an L1 fact (L2-S47). *(Corrected at the check. Former wording, preserved (#12): "**L2-S47** — L2
  reads everything L0 and L1 publish and nothing else, and never re-derives an L1 fact" — the first half is the
  charter's, not L2-S47's.)*
- **The L0/L1 side** — L1 over a larger span equals a fresh computation over it (Ruling 46 (ii)); L0 is fixed until
  rebuilt, and the caller that owns the record asks for the rebuild after an edit (Ruling 43).
- **On edits, L2's own specification says nothing today** (the derivation searched at the check for "edit": no hit).
  The charter's C-8 and §6.7 govern: the changed stretch plus a bounded margin is re-decided. *(Corrected at the
  check: the search behind the negative had not been run.)*

### Recorded as this side's derivation, not put — 29 row-parts (the comparison's proposals unchanged)

**27 ADOPTED — carried (L2-S48)** (§A.4.1's table) and **2 QUARANTINED** with their audit questions (Rows 17.34(ii),
30.75(ii)). No live alternative: each agreeing row restates L2-S48, which restates two ruled decisions (D-260, D-264);
the two quarantined rows describe code, which the vocabulary sends to the audit (§5 of the comparison; entry 314 §2).
Under `CLAUDE.md` Conventions, *HOW A DECISION SURFACE IS WRITTEN*, step 2, these are recorded as the tractability
record's §1c and the never-re-derives record's §1 recorded theirs, and not put. **The user may still have them put.**
**Documentation:** labels on rows. **Algorithm:** unchanged.

### Question 1 — a confirmation, the alternatives having collapsed (documentation only)

**Whether Row 45.60(ii) is placed HISTORICAL, from UNPLACED** — the old rule that an extension may settle an open
decision but never reopen a closed one, a rule of the one-pass closure that weight-meaning Ruling 3 found has no site in
L2.
- **Documentation:** one row's label. **Algorithm:** unchanged — L2-S48 already says the result after any sequence of
  enlargements equals a fresh run, so a reading may change when music is added.
- **Recommendation: confirm.** Towards the objective (#4): a reading that later music shows to be wrong is not frozen;
  the result depends on the music, not on the order it was loaded in. Towards the principles: D-264 as ratified; #12
  (no rival dropped by a closure — L2-S43, tractability Ruling 1); #16 (reproducible); consistency with weight-meaning
  Ruling 3, which placed the same mechanism's rules HISTORICAL; D-599 (the record decides). Meta level: a label on one
  row of the analysis's specification file.
- **The alternatives, and why they fall:** QUARANTINED — possible only if the row described code; it states a design
  rule. ADOPTED — proposed (write "an enlargement never reopens a decision" into L2) — against D-264, against Ruling 2's
  stopping rule, and against Ruling 3. So the choice collapses to HISTORICAL. It is put, not recorded as derivation,
  because the comparison left the row for the user to place (its vocabulary: UNPLACED "is a row the user places"),
  as the context-at-the-edge record put Rows 5.73, 45.58, 45.59(ii).

### Question 2 — a confirmation, the alternatives having collapsed (adds two sentences to L2's specification; the reading L2 computes is unchanged)

**Whether Rows 45.5 and 45.24 are placed ADOPTED — proposed, as proposed**, the proposals written beside L2-S48 at the
application act. *This side's wording, for the application act (not ruled by the question):* "L2 reads no event and no
slice outside the music L1 publishes for it — the working span and the context L2 has asked for." And: "The publication
does not depend on the size of the steps by which L2 enlarged the music it reads (D-261 item 6, D-262)", the falsifier
gaining: "falsified if two runs over the same selection with different enlargement steps publish differently, neither
stopped by the safety cap."
- **Documentation:** two sentences and one falsifier clause beside L2-S48.
- **Algorithm:** what L2 computes does not change. The second sentence states a property the current stopping rule does
  not guarantee by construction (§A.5 A); it makes the owed step-size test a falsifier of L2's own text, so that if the
  test fails, the stopping rule is revisited. That revisiting would be a later algorithm question.
- **Recommendation: confirm.** Towards the objective (#4): the result depends on the music and not on how L2 happened
  to step through it; a too-early stop becomes something L2's own specification can be caught on. Towards the
  principles: D-261 and D-262 (ratified; "never a different answer"); #19 (a property relied on is stated so it can be
  tested); Ruling 39's precedent on the L0/L1 side, where the user chose to write a rule explicitly rather than leave it
  holding by implication ("a rule holding only by implication is what the built system had when the cap crept in");
  the context-at-the-edge record, which carries, as its surface's reading recorded with Ruling 1, Row 45.24 among the
  guards against an early stop. Meta level: the analysis's own specification. *(Corrected at the check. Former
  wording, preserved (#12): "context-at-the-edge Ruling 1, which leaned on Row 45.24 as the guard for its stopping
  rule" — the record says the reading was not ruled separately.)*
- **The alternative weighed and set aside: leave both as proposals.** For it: Row 45.5 follows already, on *my
  reading*, from L2-S47, the charter's "Consumes … Nothing else" and L1 tiling exactly the working span (#6 — no second
  statement) *(corrected at the check: "my reading" was not marked)*; the step-size
  test is owed at the measurement side anyway (Row 45.72). Against it: with no family after this one, both rows would
  never reach L2's specification, so the property the ruled stopping rule relies on would be stated nowhere in L2's
  text, and the explicit-rule precedent of Ruling 39 points the other way.

### Question 3 — a confirmation, the alternatives having collapsed (adds one rule on edits to L2's specification; the reading L2 computes for any score is unchanged)

**Whether Rows 21.60(ii), 45.44(i) and 45.74 are placed ADOPTED — proposed, as proposed**, written beside L2-S48 at the
application act. *This side's wording, for the application act (not ruled by the question):* "After an edit, L2
re-decides the changed stretch with a margin around it (C-8; `FRAMEWORK.md` §6.7), and its publication equals a single
fresh run over the edited record for the same working span. Enlargements and edits compose: after any sequence of
both, the result equals one fresh run over the music L2 ends with." The falsifier gaining: "falsified if the
publication after an edit differs from a fresh run over the edited record in any published field."
- **Musical example.** In a 100-bar selection the user changes one note in bar 30, turning a chord into one that
  belongs to a new tonality. Re-reading only bars 28–33 might keep the old tonality from bar 20, while a fresh reading
  of the edited score moves the change of tonality back to bar 24. The rule says the second answer is the one L2
  publishes; re-reading less is allowed only when it gives the same answer.
- **Documentation:** one rule and one falsifier clause beside L2-S48.
- **Algorithm:** L2's reading of a given score does not change — it is defined as the fresh run. What is added is a
  constraint on how an edit may be handled: no quicker path may publish a different answer. The size of the margin
  follows from the equality (§A.5 B) and is the build's to compute.
- **Recommendation: confirm.** Towards the objective (#4): after an edit the user sees what the music now says, not
  what was left over from before. Towards the principles: D-264's own reason ("could silently produce an answer no single
  run would produce"), applied to edits; C-8 and §6.7 (the charter already requires the incremental re-decision; this
  says what it must equal); Ruling 43's ground (silence on a carried-forward product requirement "discovered at the audit
  or by a user"); #16. Meta level: the analysis's own specification.
- **The alternative weighed and set aside: leave the three as proposals**, the charter's C-8 alone governing edits. For
  it: the charter already states the edit rule and D-092 says a cross-cutting contract is stated once. Against it: the
  charter states the cost (re-decide a stretch plus a margin), not the result's equality; L2's specification would be
  silent on what an edited score's reading must be, and with no later family the rows would never reach it.

## §A.7 Searches made so the questions do not repeat an earlier ruling, or miss a row

- All 39 ruling records of 2026-10 (staged) for every row identity of this family but "30.75" (searched at the check),
  "45.60", "5.218", "5.224",
  "5.225", "one-pass", "D-339", "D-260", "D-264", "45.24", "45.74", "21.60", "45.44", "45.5", "6.61", "7.54", "9.115",
  "OQ-L2-16", "L2-S46". Hits read at their lines: weight-meaning (whole), context-at-the-edge (whole), tractability
  (whole), working-order (lines 28–52), no-early-discarding (line 52), and prefix matches in other records (other rows).
- All 39 `cowork_l2_*` files in `ratification_surfaces` (staged) for "45.5", "45.24", "45.74", "21.60", "45.44",
  "6.61", "7.54", "9.115", "45.60", "17.34", "30.75", "22.84", "D-264": hits in the context-at-the-edge surface (lines
  255–440 read), the convergence research document (lines 200–259 read), the pivot-chord and nothing-from-L3
  surfaces (other halves of Row 30.75 and 45.60, read at the hit lines), and a prefix match in the
  tonality-and-progression-terms surface (Row 39.115, another row). *(The last added at the check.)* **At the check:**
  the 2026-10 records for "30.75", "45.60", "21.44", "48.46", "45.72" (hits: context-at-the-edge lines 29 and 43);
  the nothing-from-L3 record searched for its rulings and words (lines seen in the search results only, among them
  lines 183–207 on the 160 AGREES parts); the derivation for "edit" (no hit).
- The comparison: §7 at lines 71270–71293; every row of the family read whole at its row; member 45 read whole as
  tabulated to Row 45.90 (lines 59129–60289; Rows 45.91 to 45.94 and the member's arithmetic not read) *(corrected at
  the check; former wording, preserved (#12): "member 45 read whole as tabulated (lines 59129–60290)" — the member runs
  past line 60290)*; Row 2.10 at its tail and Rows 2.11–2.17, 5.224–5.225, 9.115, 17.34, 21.59–21.61, 22.83–22.84, 22.107, 30.75,
  43.74–43.79, 49.1, 51.60; member 62's Rows 62.41–62.46 (lines 70790–70853); the list of ADOPTED — proposed rows at
  lines 73640–73684; a pattern search for ADOPTED — proposed proposals naming "fresh", "working span", "selection",
  "enlarg", "loaded" or "edited stretch" (ten lines, covering Rows 21.60, 45.5, 45.21, 45.22, 45.23, 45.24, 45.26,
  45.29 and 45.74, all named above). The vocabulary §5 (lines 295–350).
- The L0/L1 side: the 2026-08-31 record at Rulings 39, 40 (to line 3430), 43 and 46.
- `FRAMEWORK.md` for "working span", "fresh run", "selection", "C-8": lines 174–181, 494–555, 596–607, 1195 read.
- `decisions/group_C.md` at D-260 to D-265 (lines 336–460).

## §A.8 What was not read

The input contract itself (S-32, S-53 and Rulings 40/46's clauses are quoted from the 2026-08-31 record); the brief;
`cowork_bounded_context_design.md` itself (every passage quoted is the comparison's row or D-260 to D-264's verbatim);
the derivation outside lines 1–60, 572–601, 1058–1087, 1140–1199, 1195–1273 and 1515–1544; the convergence research
document outside lines 200–259; the context-at-the-edge surface outside lines 255–440; Ruling 40 beyond line 3430;
`FRAMEWORK.md` beyond the lines named in §A.7; D-092 at its group file (cited from `DECISIONS.md`'s index line only);
*(added at the check)* member 45's Rows 45.91 to 45.94; the nothing-from-L3 record beyond its search-result lines; the
Mauch & Dixon paper.

## §B The check, at the sources (2026-10-09, on the user's "continue")

Run over the whole surface for coherence, completeness, correctness and overstatement, each claim taken back to the
object it rests on. **Confirmed at the objects:** L2-S48's text and line numbers; the terms-table line; §7's lists and
counts (29 + 1); every row quotation and proposal in §A.4 against its row; D-260, D-261 item 6, D-262 and D-264 against
`decisions/group_C.md`; Ruling 46's Position one and "What was decided"; the tractability, context-at-the-edge and
weight-meaning quotations; C-8 and §6.7; the arithmetic (27 + 2 = 29 derivation; 1 + 2 + 3 = 6 put; 29 + 6 = 35; §7's
30 + 5 taken in = 35). **Corrections, each at its site with the former wording kept (#12):**

1. **§A.1, "notated positions"** — the working-order record rules "the record's own positions"; "notated" is its
   surface's reading, not ruled. Reworded with the record quoted.
2. **§A.1, the taken-in rows** — Row 21.60(ii)'s axis names no statement; it was described as naming L2-S48.
3. **§A.2, Mauch & Dixon** — a gloss of a paper not opened, stated as fact. Marked a reading from the title.
4. **§A.2, item 13** — "the charter says none exists" was wider than item 13's subject (cost, edits, extensibility).
   Narrowed.
5. **§A.3, the search for earlier placements** — "30.75" had not been searched; run at the check (one hit, claim (i),
   already named in §A.4.1). Row 45.60(i)'s placement by the nothing-from-L3 record added.
6. **§A.4.2, claim (i) of Row 45.60** — stated as a proposal; it is placed (nothing-from-L3 record, "confirmed").
7. **§A.4.2, "would drop every rival"** — an absolute about an old mechanism not read. Narrowed.
8. **§A.5 A** — the top effort setting not named; Row 45.72 called RELOCATED without "proposed".
9. **§A.5 C, Ruling 39** — a sentence of Ruling 46 quoted as Ruling 39's. Ruling 39's own words now quoted.
10. **§A.5 C, Rows 21.44, 48.46(i)** — called unplaced without a search; searched at the check, no hit.
11. **§A.6, L2-S47** — the charter's "Nothing else" attributed to L2-S47. Attribution split.
12. **§A.6, "says nothing today" on edits** — a negative written before its search; the derivation searched at the check
    for "edit", no hit.
13. **Question 2, "leaned on Row 45.24"** — the context-at-the-edge record carries that as its surface's reading, not
    ruled separately. Reworded.
14. **Question 2, Row 45.5 "follows already"** — this side's reading, unmarked. Marked.
15. **§A.7, reads** — member 45 was described as read whole; Rows 45.91 to 45.94 were not. The search over the records
    was described as covering "every row identity"; "30.75" was missing. Both corrected; the check's own searches listed.

**No correction moves a placement, a count, a question or a recommendation.** Corrections 2 and 4 bear on Question 3's
grounds and leave them standing: Row 21.60(ii) is taken in for its proposal's subject, and item 13 names edits
directly.

**Degradation, reported (the user's standing rule of 2026-08-15):** corrections 5, 12 and 15 are searches described as
wider than they ran or negatives written before the search; correction 9 is a quotation attributed to the wrong ruling.
That is two tells and more. This side recommends putting the three questions, one per turn, recording each, and
handing over at the placed family with entry 329.

**Departures.** No shell command was run, in the container or on the device. No memory tool, git, widget, task list,
subagent or web access. The repository root was not listed. The surface's first landing came through one edit behind
(the bridge fault, stale shape); it was proved at phrases from the last edits and re-committed guarded by the staged
modification time, no `force`.
