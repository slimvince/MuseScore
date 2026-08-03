# CC dispatch — phase 1k: apply the 2026-08-03 rulings, then continue the full reads

> **Status: ACTIVE DISPATCH, written 2026-08-03 (Cowork), carrying the user's rulings of the same
> date.** It applies rulings already made; it does not ask for new ones. Read it IN FULL before
> touching anything it owns. The governing sequencing rule is D-231 (three phases): this is phase
> 1 work — specifications made complete and true — and **NO FIX DESIGN is licensed here**.

## 0. Terms (read first — nothing below uses a term before its row)

| Term | Meaning (or citation) |
|---|---|
| **The register** | `DECISIONS.md` (the INDEX) + `decisions/group_<X>.md` (full entries). A GENERATED surface: change `tools/audit/decisions/backbone_decisions.json` and regenerate; never hand-edit a rendered file (`CLAUDE.md`, decisions-register rule (d)). |
| **Contract home** | The fifth home case (user-ratified 2026-08-02, OI-268): a ratified contract document the owning `ARCHITECTURE.md` section points to is a proper home. Criteria: ratified or signed + a status banner + the delegation pointer. |
| **The dictionary** | `cowork_progression_schema_dictionary.md` — the Harmonic Vocabulary component specification. |
| **The five idioms** | Diatonic-functional · Chromatic-functional · Seventh-functional · Triadic-modal · Chromatic-coloristic, with *mode* and *chromaticism* as orthogonal cross-attributes. Ratified by the user 2026-06-30 (`cowork_style_taxonomy_proposal.md`) and encoded. |
| **The genre taxonomy** | The superseded hand-made list (Baroque, Classical/galant, Romantic; trad, swing/songbook, bebop, hard-bop, cool, modal; blues, ragtime, gospel-soul, rock, pop, folk, barbershop). |
| **Anchor drift** | The line-number shift an insertion causes in files the register cites. Remapped PER CITATION from the `--verify` drift report's own line numbers, NEVER by an assumed uniform shift. |

## 1. The rulings this dispatch applies (user, 2026-08-03)

The decision surface was delivered as user-visible prose and read before the ruling was given
(D-249 satisfied). The user's words: *"I agree w your recommendations."* The recommendations, as
presented, resolve to the five rulings below. **If any task cannot be executed exactly as written,
STOP and report — do not substitute judgment.**

- **R1 — The four status banners are RATIFIED as drafted** (option A). The 14 register entries
  homed in those documents become **contract-home**. `OPEN_ITEMS.md` OI-274 does **NOT** close:
  the `docs/scoring_model.md` body tense and the three smaller instances it records stay open for
  the truth-sync clause.
- **R2 — D-406…D-414 are RATIFIED as drafted**, statuses exactly as the record states them
  (option A). The home-class question for the dictionary is **NOT** decided here; it becomes its
  own row (R5b).
- **R3 — The `ARCHITECTURE.md` §6.7 doc-sync correction is ORDERED** (option (a)): §6.7 restated
  over the five idioms, the genre taxonomy retained as **marked historical context** (#12), and
  the "theory-based v1" characterization corrected — the five idioms are empirically discovered.
  D-131's verbatim is re-taken from the corrected text.
- **R4 — D-132 is NARROWED** (option (i)): DEFERRED over the **per-preset weights alone**; the
  clusters half marked **superseded-by** the 2026-06-30 five-idiom ratification.
- **R5 — Two items are rowed, not resolved:** (a) the dictionary's internal **"D5" label
  collision**; (b) the **draft-home question** — whether an `ARCHITECTURE.md` delegation pointer
  confers contract-home status on a document that self-declares "v1 draft".

## 2. Hard stops (violating any of these is a STOP-and-report, not a judgment call)

1. **No `src/` change. No golden refresh. No `tools/corpus/` or `tools/robust_stop/` movement.
   No behavior change, no inference change, no fix, no design.** This dispatch is documentation
   and register work only.
2. **No new ratification.** Anything discovered that would need one enters with the record's own
   status and goes to the user in the report's RATIFICATION QUEUE.
3. **No decision's SUBJECT is rewritten beyond R3/R4.** D-131 keeps its title and its meaning —
   one shared taxonomy, not two parallel vocabularies; only its verbatim and the list it names
   change. D-132 keeps its subject; only its scope and status change.
4. **The genre taxonomy text is not deleted** — it is retained, marked historical (#12).
5. **The register is regenerated, never hand-edited** (rule (d)). The backbone JSON round-trips
   byte-identical at `json.dumps(indent=2, ensure_ascii=False)`, no trailing newline.
6. **Never work from memory.** Every claim written into a specification or a register entry cites
   its primary source file:line, re-read in this session.
7. **Bare words carry the musical meaning** (`CLAUDE.md`, the disambiguation convention).
8. **Bash rules:** append `; echo "exit:$?"` to every command; never let one call produce large
   output — redirect to a file and read it separately.

## 3. Task 1 — Apply the four status banners (R1)

Write each banner verbatim as drafted below, at the head of its document, beneath the title and
before any other content. Do **not** paraphrase; these texts were ratified as written.

1. **`docs/scoring_model.md`** — *"LIVE MANDATORY REFERENCE — the scoring pipeline's one
   specification (CLAUDE.md makes it a required read for any session touching scoring logic). Its
   mechanism content describes the LEGACY vertical scorer, which is dormant on both production
   surfaces since 2026-07-26/27; its §8 constraints and dead ends remain in force and must not be
   retried."*
2. **`docs/redesign_plan.md`** — *"SUPERSEDED AS A PLAN — RETAINED AS THE RECORD OF WHAT WAS TRIED
   AND CLOSED. Its four dead ends (D-317…D-320) are LIVE prohibitions about the legacy chord path;
   nothing else here is a current plan."*
3. **`docs/iteration_path1_summary.md`** — *"ITERATION-ERA RECORD (path 1). Two of its rules are
   standing and registered — gates read structured fields only (D-280) and the batch measurement
   tool must emit the structured fields on every alternative (D-281); its commit-timing lesson is
   reconciled by the dated annotation at :112-130. Not a current plan."*
4. **`cowork_architecture_reassessment.md`** — *"PLANNING RE-ASSESSMENT — ITS FOUR META-FINDINGS
   WERE RULED SUPERSEDED (user, 2026-08-02, OI-270): D-282→D-115/D-191, D-283→D-001/D-096,
   D-284→D-036 with D-001/D-010, D-285→the ratified factorization emission design. Retained for
   the derivations; none of it is a live prohibition."*

Then, in the backbone JSON, **re-classify the 14 affected entries to contract-home**: D-321,
D-322, D-323, D-324 (`docs/scoring_model.md`); D-317, D-318, D-319, D-320
(`docs/redesign_plan.md`); D-280, D-281 (`docs/iteration_path1_summary.md`); D-282, D-283, D-284,
D-285 (`cowork_architecture_reassessment.md`). Verify the count is exactly 14 and that no entry
outside this set changes class. **Existing LEGACY marks are preserved** — D-317…D-320, D-321,
D-322, D-324 and D-284 carry them at HEAD and a home re-classification does not touch them.

**Report:** the 14 entries listed by identifier with their before/after home class, plus the
count check.

## 4. Task 2 — Ratify D-406…D-414 (R2)

In the backbone JSON, set each of the nine to **user-ratified 2026-08-03**, preserving each
entry's recorded status exactly: D-406 LIVE, D-407 LIVE, D-408 LIVE, D-409 LIVE, **D-410
DEFERRED**, **D-411 DEFERRED**, D-412 LIVE, D-413 LIVE, D-414 LIVE.

Preserve every entry's existing "date not stated" / "ratifier not stated" fact **in the
provenance** (#12) — the ratification is dated today; it does not retroactively supply a date the
record never had. D-406 already reads "ratified by user" for the 2026-07-02 D5 owner ruling;
record today's act without overwriting that.

**The nine keep their `⚠gap` home flag.** The dictionary's banner still reads "component spec, v1
draft (2026-06-29)" (`cowork_progression_schema_dictionary.md:3`), so it fails the contract-home
banner criterion. This is deliberate and is the subject of the R5b row — **do not resolve it by
editing the dictionary's banner.**

**Report:** the nine with before/after ratification state, and confirmation the gap flags stand.

## 5. Task 3 — The §6.7 correction, D-131 and D-132 (R3, R4)

### 5.1 Rewrite `ARCHITECTURE.md` §6.7

Sources to re-read before writing, and to cite in the new text:

- `cowork_progression_schema_dictionary.md:317-330` (§12.1 — the supersession record: the five
  idioms, the two cross-attributes, ratified 2026-06-30, encoded);
- `cowork_progression_schema_dictionary.md:239` (the `{Baroque, Jazz, Default}` StyleTag retired);
- `cowork_style_taxonomy_proposal.md` (the ratified proposal);
- `cowork_style_clustering_plan.md` (the per-preset weights, still future work).

The corrected §6.7 must state, in the section's own voice and with its defense (`CLAUDE.md`,
every design decision carries its defense at its home):

1. the shared style vocabulary **is the five idioms**, with *mode* and *chromaticism* as
   orthogonal cross-attributes, ratified 2026-06-30 and encoded;
2. that it is the **same** set the Harmonic Vocabulary (§7) tags entries with — the one-shared-
   taxonomy property D-131 records, which survives the change unaltered;
3. that the five idioms are **empirically discovered**, correcting "theory-based v1", which was
   false in the direction of understating what is established;
4. that the `{Baroque, Jazz, Default}` StyleTag is **retired**;
5. that the remaining committed future work is **the per-preset weights** by clustering, **not
   the clusters** — the clusters half is delivered;
6. the genre taxonomy retained beneath, explicitly marked **historical context, superseded
   2026-06-30** (#12), with the note that it is the list this section previously presented as
   current;
7. the pointer to the dictionary §6/§12 and `cowork_style_clustering_plan.md`, kept.

**Do not** invent an inclusion rule for the five idioms. §6.7's existing inclusion rule ("a style
is listed iff it has a distinct functional-harmonic vocabulary; free jazz / atonal excluded")
belongs to the genre taxonomy. If the dictionary or the proposal states the five-idiom set's own
admission basis, quote it; **if neither does, say "not stated in the record" and row it** — do not
carry the old rule across by analogy.

### 5.2 D-131 and D-132 in the backbone JSON

- **D-131** — verbatim re-taken from the corrected §6.7 text; title and meaning unchanged; home
  anchor re-aimed; the former verbatim preserved in provenance (#12).
- **D-132** — status **DEFERRED, narrowed to the per-preset weights alone**; the clusters half
  recorded as **superseded by the 2026-06-30 five-idiom ratification**; verbatim re-taken;
  defense stated (the clustering plan holds the weights; the clusters are delivered and encoded);
  the former verbatim and the former undifferentiated scope preserved in provenance.

### 5.3 Anchor drift — the part that has bitten twice

Rewriting §6.7 shifts every register anchor below `ARCHITECTURE.md:4536`. After the edit:

```
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/verify_1k.txt 2>&1; echo "exit:$?"
```

then read `/tmp/verify_1k.txt` and **re-aim each drifted citation individually from the drift
report's own line numbers**. An assumed uniform shift is forbidden — phases 1i and 1j re-aimed 159
and 182 anchors one by one for this reason. Re-run until clean.

### 5.4 Flip OI-279

`OPEN_ITEMS.md`'s OI-279 row flips to RESOLVED with provenance naming the user's 2026-08-03
ruling, the two options as presented, and which was taken. Append a dated resolution note to
`open_items/OI-279.md` — **the detail file never carries a status of record**.

## 6. Task 4 — Two new rows (R5)

Each gets an INDEX row in `OPEN_ITEMS.md` **and** its detail file `open_items/OI-<n>.md`, in the
same commit that records the discovery (`CLAUDE.md`, register rule (c)).

**(a) The "D5" label collision.** `cowork_progression_schema_dictionary.md` uses the label "D5"
for two different decisions — the dependency-map ownership ruling at §1 (`:41`, entered as D-406)
and the harmonic-scope component decision at §7 (`:261-263`, entered as D-408). Recorded already
in D-406's provenance but with no row of its own. Class: documentation gap; it offends
`CLAUDE.md`'s no-self-invented-numbering convention. Not in doubt: both decisions' content.

**(b) The draft-home question.** Does an explicit `ARCHITECTURE.md` delegation pointer (§7 →
the dictionary, `:4545-4547`) confer contract-home status on a document that self-declares "v1
draft" (`:3`)? The delegation half of the OI-268 criterion is satisfied; the banner half is not.
State both readings without choosing: (i) transitive authority reaches it, since the delegating
surface is user-ratified — which would close nine gap flags at their cause (#6); (ii) it does not,
because rule (g)'s transitive clause was ratified with the guard that an assistant's stamp alone
never confers contract-home status, and a self-declared draft names no ratifier. Record the scope
honestly: **the answer applies to every draft `ARCHITECTURE.md` points at, not to this one
document** — which is why it is a user ruling and not a homing act. Cross-reference OI-268 and
its still-open sibling question (whether a Cowork ratification counts — 21 entries).

## 7. Task 5 — Continue the full reads (OI-207)

64 documents remain of 143; 38 are read, 41 covered by the user's accepted exclusion list. Read
IN FULL, in this order, as far as capacity allows:

1. `docs/implementation_roadmap.md` (18)
2. then the three at 17, in the order the OI-207 artifact lists them.

Per document: enter every decision-bearing statement as a register entry **with the record's own
status only** — inference of a status is forbidden, "not stated" is a permitted and expected
value. Row any finding of the OI-232/OI-274/OI-276 class (a document stating as current something
false at HEAD). Update the OI-207 note with the new read count and the remaining list.

## 8. Task 6 — Guards, notes, close

Run every guard **explicitly at the committed tree** — a commit made by plumbing bypasses hooks:

```
cd C:\s\MS && python tools/audit/decisions/gen_decisions_register.py --check > /tmp/reg_check_1k.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/audit/decisions/gen_cluster_dispositions.py --verify > /tmp/verify_1k_final.txt 2>&1; echo "exit:$?"
cd C:\s\MS && python tools/open_items_split_check.py > /tmp/split_1k.txt 2>&1; echo "exit:$?"
```

Read each output file separately. **All three must pass before the close.** Report the counts:
quotes, anchors, references, files, clusters, occurrences, and the open-items living check.

`STATUS.md` gains one entry, written as a **POINTER** per the OI-222 remedy — the content lives in
the specifications, the register and the dated notes, not in STATUS. It must name: the rulings
applied, the register count before → after, the 14 contract-home re-classifications, the nine
ratifications, the §6.7 correction, D-131/D-132, the two new rows, the read count, and the guard
results.

`cowork_pending_ratifications_next_session.md` is **superseded by this dispatch's execution**: flip
its status block to RULED, pointing at the commit and at this file. Do not delete it (#12).

**Commits:** the same-commit rule (D-230) governs — each ruling lands in the commit that records
it. From the sandbox use git plumbing (`write-tree` / `commit-tree` / `update-ref`); `git commit`
times out on index refresh. Push if credentials permit; report the SHAs either way.

## 9. What Cowork will verify at the objects when the report arrives

Stated here so the report is written to be checkable: the SHAs by `git show`; fresh file-tool
reads of every edited document; the 14-entry count re-derived independently from the register; the
nine entries' statuses compared against the dictionary's own text; the corrected §6.7 read against
`cowork_progression_schema_dictionary.md:317-330` line by line; the guards re-run live; and the
two new rows opened from the INDEX.

## 10. Accepted outcomes

A **feasibility stop with a measured partition proposal is an accepted outcome** for Task 5 only.
Tasks 1–4 and 6 are bounded and are expected complete. If Task 5 cannot start, say so and close —
do not compress Tasks 1–4 to make room for it.
