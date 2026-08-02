# The OI-207 residual second pass — report

> **Status:** DELIVERED 2026-08-02. Read-only on the system: no `src/` change, no golden /
> `tools/corpus/` / `tools/robust_stop/` movement, no behavior change, no fix, no design, no
> `ARCHITECTURE.md` edit. **Nothing here is ratified by this pass** — the 23 new register entries
> carry the status the record gives them and go to the user in §5.
>
> Dispatch: `cc_instruction_oi207_residual_pass.md` (Cowork, 2026-08-02) — phase 1c of the
> three-phase rule (`CLAUDE.md` Conventions, register entry D-231).
>
> **Commits:** `8f0c181a3c` (the bulk rules) → `249fc81b6c` (the register entries + the field-shape
> guard) → this one (the rows, the notes, the partition artifact, `STATUS.md`).
>
> **Every figure in this report is read from a generated artifact** —
> `tools/audit/decisions/disposition_manifest.json` and `DECISIONS.md`, both regenerated at this
> commit. None is hand-transcribed (#17f).

---

## 1. What the pass faced

The residual is the clusters the first adjudication could not classify mechanically — bulk rule
**BR-8**, "none of the above applies". The dispatch's figure was **5,204**, and that figure was
already right: the phase-1 specification-completion pass had regenerated the disposition layer at
the ratified 231-entry backbone, which moved it from the register's published 6,374 (see the
[[OI-207]] note of 2026-08-02, first entry). This pass starts at 5,204 and works against the
completed specifications and the 231-entry register.

## 2. The disposition table over 14,460 clusters

Every cluster carries exactly one disposition; the coverage guarantee is re-proved at this commit
(`gen_cluster_dispositions.py --check`: 14,460/14,460 clusters, 15,224/15,224 occurrences, OVERALL
PASS).

| bulk rule | the class | clusters |
|---|---|---|
| BR-1 | the clustering layer's labelled boilerplate bucket, confirmed | 74 |
| BR-2 | every occurrence is a section heading | 1,099 |
| BR-3 | matches a backbone decision whose home IS a layer specification | **5,511** |
| BR-4 | matches backbone decisions, all recorded outside a layer specification | 551 |
| BR-5 | dispatch scaffolding (a read-only banner, a push or build instruction) | 169 |
| BR-6 | a session report or dispatch that is measurement or delivery narrative | 1,593 |
| BR-7 | a table row admitted by the harvest's broad signature tier only | 299 |
| **BR-9** | **a list lead-in — ends in a colon, no sentence before it** | **157** |
| **BR-10** | **a row or section header of the open-items register** | **29** |
| **BR-11** | **a `cc_instruction_*` dispatch statement carrying no ruling word** | **886** |
| **BR-12** | **a `cc_*` session-report statement carrying no ruling word** | **993** |
| **BR-13** | **a `src/**/tests/**` comment carrying no ruling word** | **164** |
| BR-8 | residual — unresolved | **2,935** |

By disposition: **restates 5,511 · not-a-decision 5,389 · boilerplate 74 · no-spec-home 551 ·
unresolved 2,935.**

### 2.1 The five new rules, and the guardrail that bounds them

Each rule is stated in `disposition_manifest.json` so it can be disputed a class at a time, and each
runs **after** BR-3/BR-4, so a cluster that names a backbone decision is never swept by one.

- **BR-9 — a list lead-in.** With markdown stripped the text ends in a colon and contains no
  sentence-ending period before it: it introduces a list whose items are separate harvested units.
  Like a heading (BR-2) it names a subject and states nothing.
- **BR-10 — a row or section header of the open-items register.** That register records issues,
  their status and their provenance; the ratified ruling 1 on `open_items/OI-208.md` puts decisions
  in the decisions register and non-conformance here.
- **BR-11 / BR-12 — a dispatch or a session report.** The ratified decisions-register rules make a
  dispatch or report a **citer** of decisions (rule (b)) and land a new ratification in the register
  in the commit that records it (rule (c)). Neither is a home of record. BR-12 is BR-6 widened from
  its narrative-pattern test to the whole report class.
- **BR-13 — a test-file comment.** It states what the test pins; the decision it pins is stated in
  the specification, which is where BR-3 finds it.

**The guardrail.** BR-11, BR-12 and BR-13 apply only to a unit carrying **none** of an explicit
ruling vocabulary, listed in the manifest: *ratified · ratification · shelved · falsified · dead end
· do not re-attempt/retry/pursue/add/use/revert/remove · DECIDED · DECISION · the rule is · must not
· forbidden · never add/use/read/be/do/widen/assume · user-ruled/directed/ratified/decision/mandate ·
rejected · withdrawn · overturned · superseded by · retired · deferred to/until/indefinitely ·
standing rule · policy · convention.* A unit using any of those is **not swept** — it stays in BR-8
for a reader, and 610 dispatch/report clusters plus 76 test-comment clusters did exactly that.

Three further limits, all deliberate:

1. **The two archives are swept by nothing.** No bulk rule touches `STATUS_ARCHIVE.md` or
   `cowork_handoff_archive.md`. This row exists because a shelving-with-evidence hid in one of them;
   a class sweep over the archives is the failure mode itself.
2. **No bulk rule touches production code comments.** The 44-line Stage-3.1b block in
   `notationcomposingbridge.cpp` is the standing proof that decisions live in code.
3. **A mixed-source cluster is never swept.** Each rule requires *every* occurrence of the cluster
   to sit inside its class.

## 3. The NEW decisions — 23, register 231 → 254

Every verbatim quote is **extracted from its home by line range, never retyped** (#19). Status, date
and ratifier come from the record only; where the record does not say, the entry carries the
register's "not stated". **None is ratified by this pass.**

### 3.1 Seventeen already homed in the owning specification (D-232…D-248)

Their home is `ARCHITECTURE.md`, so they raise no documentation gap. They cluster where the earlier
passes' patterns did not reach:

- **§4.1d, monophonic and arpeggiated inference — a specification section that carried NO register
  entry at all.** Five decisions: the two-pitch-class rule (D-238), bounded expansion (D-239),
  tunable parameters rather than prose-only rules (D-240), the deferred grouping problem (D-241),
  and the no-direct-comparison rule between the vertical and monophonic engines (D-242).
- **§2.12 process rules:** the section numbers are authoritative (D-232), the synchronous
  one-run-one-result discipline (D-233), and Rule 16 — a chord symbol string must be valid under
  `chords_std.xml` (D-234).
- **§4.1f:** per-symbol trust rather than a per-score toggle (D-236) and the untrusted-symbol
  exclusion (D-237).
- **§10/§11 intonation:** the anchor-note rules (D-247), fixed-pitch instruments (D-246), automatic
  melody detection (D-245), the interval-family choice (D-244).
- **§4.2:** the tonal-centre raw-score guard (D-235). **§5.7a:** the planning band and its excluded
  corpora (D-243). **§5.10:** the deferred tonicization labels (D-248).

### 3.2 Six recorded only on a tracking surface (D-249…D-254) — rowed [[OI-266]]

The working-protocol standing rules of `cowork_handoff.md`, entered `home_is_layer_spec: false`,
`nonspec_kind: "unhomed"` per [[OI-240]]'s own ruling that a handoff block tracks work and is not a
home. **This moves the register's tracking-surface-only count 0 → 6** — the phase-1 homing pass
drove it to zero over the 231 entries it knew about, not over the repository.

## 4. The remaining 2,935 — measured, and why it is a population, not a failure

`disposition_manifest.json` now carries `unresolved_partition_by_surface`, computed by the same tool
that assigns the dispositions (#17f), each cluster counted exactly once:

| surface | clusters |
|---|---|
| `cowork_*` design documents | 870 |
| `docs/` design documents | 407 |
| `cc_*` session reports (ruling-word-carrying) | 316 |
| `tools/` script comments | 296 |
| `cc_instruction_*` dispatches (ruling-word-carrying) | 294 |
| `src` production code comments | 277 |
| the two archives | 256 |
| `src` test comments (ruling-word-carrying) | 76 |
| `ARCHITECTURE.md` | 55 |
| the open-items register | 35 |
| the session handoff | 30 |
| `CLAUDE.md` | 12 |
| mixed sources | 9 |
| `DEFECT_TYPES.md` | 2 |
| **total** | **2,935** |

**The diagnosis.** The register's 254 entries are homed almost entirely in `ARCHITECTURE.md` (166)
and `CLAUDE.md` (46), with 11 in `docs/scoring_model.md` and a handful elsewhere. The three largest
surviving blocks — `cowork_*` design documents, `docs/` design documents, the two archives, 1,533
clusters together — have **never been enumerated for the backbone**. The 2026-08-01 completion pass
read `ARCHITECTURE.md` and `CLAUDE.md` in full and followed the rulings that live on the tracking
surfaces; it stopped there, and said so. So these are not hard cases this pass failed on: they are
an unread population, and a bulk rule over them is precisely the blind sweep §2.1's guardrail
forbids.

**What each block would take.** `cowork_*` + `docs/` (1,277) are the design documents, read one
document at a time against the register — the highest expected yield of genuine unregistered
decisions, and the natural input to the next homing wave. The archives (256) must be read, never
swept. The three code-comment blocks (649) are where the Stage-3.1b precedent says decisions also
live. The 686 ruling-word-carrying dispatch, report and test clusters are the exemption set the
sweeps refused to take, so each needs a reader.

## 5. ★ RATIFICATION QUEUE — the user's

Twenty-three entries, each with the status the record gives it. Full text: `DECISIONS.md` and the
group files. Verbatim quotes are in the register; the one-line summaries below are the plain
restatements.

| entry | decision (plain) | proposed status | proposed home |
|---|---|---|---|
| D-232 | Section numbers identify a coding/process rule; a "Rule N" label is only a local name | live · date not stated · ratifier not stated | `ARCHITECTURE.md:601-603` — already the owning specification |
| D-233 | Build and test commands run synchronously in the foreground; one run, one result | live · not stated | `ARCHITECTURE.md:623-625` |
| D-234 | Everything the formatter emits must parse under `chords_std.xml`; `chords.xml` is not relied on | live · not stated | `ARCHITECTURE.md:664-670` |
| D-235 | Tonal-centre disambiguation may settle a close same-signature tie but not overturn a clearly stronger raw winner | live · not stated | `ARCHITECTURE.md:2403-2407` |
| D-236 | Chord-symbol trust is per symbol; a per-score toggle is rejected | deferred · not stated | `ARCHITECTURE.md:2598-2600` |
| D-237 | Only a symbol marked trusted becomes analyzer input; an untrusted one is never read | deferred · not stated | `ARCHITECTURE.md:2609-2613` |
| D-238 | Two pitch classes may nominate a chord but not finalize one; one pitch class may not | deferred · not stated | `ARCHITECTURE.md:2754-2758` |
| D-239 | Chord identity stays local; expansion is by one neighbouring region and is bounded | deferred · not stated | `ARCHITECTURE.md:2763-2770` |
| D-240 | The monophonic smoothing terms are tunable parameters, not prose-only rules | deferred · not stated | `ARCHITECTURE.md:2780-2781` |
| D-241 | The monophonic local-grouping problem is deferred to Phase 2 | deferred · not stated | `ARCHITECTURE.md:2810-2811` |
| D-242 | Vertical and monophonic raw scores are never compared directly | deferred · not stated | `ARCHITECTURE.md:2838-2840` |
| D-243 | The 65-75 % planning band, and the thin-texture corpora excluded from it | **superseded in fact** · not stated | `ARCHITECTURE.md:3556-3564` |
| D-244 | The interval-family choice for an ambiguous sonority is deferred; fixed tables are used | deferred · not stated | `ARCHITECTURE.md:5069-5078` |
| D-245 | Voice role comes from staff position or explicit assignment; melody detection is deferred | deferred · not stated | `ARCHITECTURE.md:5192-5194` |
| D-246 | Fixed-pitch instruments are deferred and will never receive tuning offsets | deferred · not stated | `ARCHITECTURE.md:5293-5295` |
| D-247 | An anchor note stays at 12-TET, is never split, and is excluded from drift and centering | live · not stated | `ARCHITECTURE.md:5311-5323` |
| D-248 | Tonicization labels are not implemented and are deferred | deferred · not stated | `ARCHITECTURE.md:6001-6003` |
| D-249 | The whole decision surface is delivered as user-visible text before any choice question | live · 2026-07-05 · user | `cowork_handoff.md:1589-1598` — **no specification home** ([[OI-266]]) |
| D-250 | Dispatches are written only when next; a parked instruction is revalidated first | live · not stated | `cowork_handoff.md:1606-1616` — **no specification home** |
| D-251 | A running dispatch is never interrupted or steered mid-flight | live · 2026-07-05 · user | `cowork_handoff.md:1617-1621` — **no specification home** |
| D-252 | One side writes the instruction files and the other executes them, never the reverse | live · not stated | `cowork_handoff.md:1630-1638` — **no specification home** |
| D-253 | Working-tree files are read with the file tools; shell access is git-object queries by hash | live · 2026-06-21 · user | `cowork_handoff.md:1669-1680` — **no specification home** |
| D-254 | Investigate by default; never ask the user whether to investigate or proceed | live · 2026-06-14 · user | `cowork_handoff.md:1792-1796` — **no specification home** |

**Two judgments in this queue are the user's, not mechanical.**

1. **D-243's status.** The record states the band (`ARCHITECTURE.md:3556-3564`) tied to one
   comparison methodology. The governing measurement surface is now the robust unit ratified at
   R10-b, reported per preset on a different unit. **No ruling names the band as replaced**, so it
   is entered `superseded-in-fact` — never inferred into `superseded-by`. If a ruling does exist and
   this pass did not find it, the entry should be corrected.
2. **The classification of D-249…D-254.** They are entered "recorded only on a tracking surface".
   The register also has a category for a **decision about the process, correctly homed** (26
   entries) — but every one of those lives in `CLAUDE.md`. Whether a handover document counts as a
   home for a working-protocol rule is a ruling, and [[OI-266]] states it rather than settling it.
   `CLAUDE.md` already names "the ⛔ TOTAL UNIFICATION rule (`cowork_handoff.md`)" among its
   companion standing rules elsewhere, which cuts the other way.

## 6. Findings rowed

- **[[OI-265]] — the Layer-4 as-built body still says production chord analysis runs the legacy
  path.** `ARCHITECTURE.md:1336-1337` is false at HEAD on both surfaces. The phase-1 truth-sync's
  Layer-4 correction (`:1325-1332`) addresses only the "engages with L5" clause; the **Layer-3**
  correction of the same commit carries the sentence that makes its body safe to read — "*it is no
  longer a description of what runs*" (`:1268-1269`) — and the Layer-4 one does not. A ninth
  statement of the [[OI-232]] class, in a block that pass corrected but did not finish. One sentence
  at the next `ARCHITECTURE.md` touch.
- **[[OI-266]] — the six handoff standing rules have no specification home.** [[OI-240]]'s sibling;
  §3.2 above.

## 7. Guard results, at this commit

| guard | result |
|---|---|
| `gen_cluster_dispositions.py --verify` | 254 decisions · **254/254** verbatim quotes found at their cited home · **249/249** line anchors correct (5 cited to a file with no line number, by design) · cross-references **ALL** resolving · field shapes clean |
| `gen_cluster_dispositions.py --check` | clusters in 14,460 · dispositioned 14,460 · **OVERALL PASS** |
| `gen_decisions_register.py --check` | the register matches its data across all **21** files |
| `tools/open_items_split_check.py` | index 266 · detail 266 · all 200 original items byte-verbatim · **OVERALL PASS** |

## 8. Anomalies, each diagnosed

1. **The register could carry a silently-empty field.** This pass's own first write of the 17
   `ARCHITECTURE.md` entries used `ratified_by: []` where the register's convention is
   `["not stated"]`. The renderer printed "**ratified by** " with nothing after it and every guard
   passed. Found by the standing self-check reading the diff, not by a guard. *Diagnosis:*
   `gen_decisions_register.py` branches on the exact list `["not stated"]` and falls through to the
   name-joining branch for anything else, including empty. *Remedy, shipped in `249fc81b6c`:*
   `--verify` now rejects an empty `ratified_by` or `date`, so the class cannot recur. The 17
   entries were corrected before the register was regenerated.
2. **The residual partition first summed to 2,944 against an unresolved total of 2,935.** *Diagnosis:*
   the first implementation counted a cluster once per surface its occurrences touch, so the nine
   mixed-source clusters were counted twice. *Remedy:* each cluster is now counted exactly once,
   with a `mixed sources` bucket; the partition sums to the total by construction.
3. **`ARCHITECTURE.md` line numbers in the harvest are stale.** The harvest ran at the pre-phase-1
   tree; every residual unit's cited line has since moved. *Diagnosis:* expected, not a defect — the
   harvest is a frozen artifact. *Handling:* every `ARCHITECTURE.md` residual unit was re-located at
   HEAD by normalized text search before any judgment was made about it, and all 82 were found; the
   17 new entries cite HEAD lines and `--verify` proves each starts where it is cited.
4. **The dispatch's 5,204 needed no correction.** It matched `disposition_manifest.json` at HEAD
   exactly. Recorded because the dispatch flagged the figure as a correction of the register's
   published 6,374 and asked that every count read 5,204.

## 9. What this pass did not do

It did not read the 2,935 remaining clusters, and does not claim to have. It did not ratify
anything. It did not edit a specification, propose a fix, or design one — phase 3 is not open. The
honest state of this row's last scope: **worked and measured, not finished**, with the remainder
partitioned so the next pass starts from a named population rather than a number.
