# CC REPORT — OI-199 comprehensive review, PASS 1 (blind enumerative) — the inventory, the partition, and the joint module's deep dispositions

> **Session 2026-07-28.** Executes `cc_instruction_oi199_pass1.md` (the user-directed comprehensive
> review of everything the L1–L5 certifications predate: the joint module, the record path and seams,
> the codegen machinery, the new instruments). Protocol: `cowork_audit_protocol.md` P1–P4, blind
> (P8 first run), reusing the L3/L4/L5 vocabulary unchanged. **Read-only fact-finding — no `src/`
> change, no constant tuned, no golden refreshed; `tools/robust_stop/` and `tools/corpus/` untouched;
> no behavior change.** Certification is NOT granted by this pass.
>
> **★ OUTCOME: the Task-1 FEASIBILITY STOP fired** (expected). The four-area inventory is complete and
> frozen at **6,375 deep rows across 67 files**; area (a) the joint module (**1,069 rows**) is
> fully dispositioned this session (first claim); the other three areas are partitioned into the
> sequential sessions proposed in §2.
>
> **★ AND A PROCESS STOP THAT MUST BE STATED FIRST: the blinding of this pass was DEFEATED at the
> source, before any auditing began (§0).** Two independent leaks — the mandatory `STATUS.md`
> session-start read AND the dispatch's own inline §S — both carry the full text of the three sealed
> findings. This is the **DT-20** self-defeating-instruction pattern (OI-89's founding shape), and it
> materially limits what the Task-4 reconciliation can claim. It is surfaced here, not worked around.

## 0. Blinding log — and the disclosure that the blinding FAILED (protocol P8; DT-20)

The pass is *designed* as blind: `OPEN_ITEMS.md`, `open_items/OI-*.md`, and the dispatch's §S are
withheld until after the Task-3 freeze, so that pass 1's discovery of the sealed findings — or its
failure to discover them — is evidence about the audit method's power.

**I did not open any withheld FILE early.** `OPEN_ITEMS.md`, the `open_items/OI-*.md` detail files,
and the `tools/audit/**` dispositions/blind/sweep/errorrate artifacts were not opened during Tasks
0–3. The freeze commit is the boundary.

**But the blinding was compromised before Task 1 by two leaks I could not avoid, both DT-20:**

1. **`STATUS.md` (a MANDATORY session-start read) carries the full S1/S2/S3 text.** The dispatch
   itself instructs "Read `CLAUDE.md`, `STATUS.md` and `BUILD_AND_TEST.md` as usual." The current
   top entry of `STATUS.md` (2026-07-28, LATEST) states **OI-215 verbatim** ("the joint decoder
   returns an EMPTY analysis … `candidateStates` … skips any class where `present < min(2,|members|)`
   … one uncoverable event empties `V[N]` → `complete=false`" — this **is** S1, with the exact
   `jointdecoder.cpp` line cites), **the C++-slower-than-Python anomaly** ("the C++ decoder appears
   SLOWER than the pure-Python reference … `std::string` state in the innermost dynamic-programming
   loops" — this **is** S2), and **`buildAdapterFacts` near-quadratic** ("`events^1.80`" — this **is**
   S3). So the required read leaked all three sealed findings. This is the exact **DT-20 founding
   instance** (OI-89: "a required session-start read that leaks exactly what a blinding requirement
   withholds").
2. **The dispatch delivered §S inline.** The dispatch file `cc_instruction_oi199_pass1.md` contains
   §S (S1–S5) in full at its foot, and it was delivered to me in full. I did not "open" a separate
   sealed file — the sealed content was in front of me from the first turn.

**Consequence for the reconciliation (Task 4).** I cannot honestly claim to have found S1/S2/S3
*independently of prior knowledge* — I had that knowledge from the required reads before Task 1.
What I CAN report, and do report in Task 4, is the **mechanical/structural** question that is
knowledge-independent: **do the audit's generated artifacts and a rigorous code-reading of the
dispositioned rows point at each sealed finding's mechanism on their own merits?** That question is
answerable from the artifacts (the fire-structure of `candidateStates` + the `V[N]`-empty branch, the
`std::string`-keyed DP state in the disposition CSV, the nested-scan structure of `buildAdapterFacts`)
regardless of what I knew. I answer it honestly, and I flag the limit.

**Safe reads used this pass (Tasks 0–3):** `CLAUDE.md`, `STATUS.md`, `BUILD_AND_TEST.md`,
`DEFECT_TYPES.md`, `ARCHITECTURE.md`, the prior audit reports named in the dispatch
(`cc_l3_audit_pass1_report.md`, `cc_l4_audit_pass1_report.md`, `cc_l4_audit_pass1_decoder_report.md`,
`cc_l5_audit_pass1_report.md`), the source under `src/composing/analysis/joint/` +
`src/composing/composingconfiguration.cpp` + the notation record-path files, and the `tools/audit/`
inventory tables (not the dispositions/sweep findings). No `cc_*_report.md` beyond the four named,
no `cowork_*` doc, and no `OPEN_ITEMS`/`open_items/` file was opened before the freeze.

## 1. Task 1 — the machine inventory across the four areas (protocol P1)

Extended the ONE inventory instrument `tools/audit/gen_inventory.py` with `--layer oi199` (one path
per concern, #6 — no second tool). The extension adds: a base `src/composing/analysis/joint/` tag so
totality holds; an `oi199` refinement over `src/composing` (JOINT / CODEGEN / RECORD-SEAM tags + the
generated-data and drift-guard file-level tags + the joint tests); two additional scope roots (the
curated `src/notation/internal` record-arm files + every tracked `.py` under `tools/joint_estimator`
and `tools/notation_seams`); and it routes the Python instruments through the existing `ast`
extractor. Artifacts under `tools/audit/oi199/`, manifest-stamped HEAD `5135764ed7`, corpus
`c50002fee1`.

**The instrument change is PROVEN inert for the prior layers.** Regenerating `l1l2/l3/l4/l5` with my
edited tool reproduces, byte-for-byte, the output of a minimal tool = HEAD's tool + ONLY the joint
base rule (deep-CSVs AND file_tables identical, all four layers). So every `oi199` addition is
layer-gated; the only prior-layer effect is the joint base rule adding the 22 joint file-table rows.
*(The deep CSVs differ from the COMMITTED prior-layer artifacts — but that is pure source drift: HEAD
`5135764ed7` is far past the frozen inventory commits `7123c7cb55`/`9e294f398d`/`7f57aad4b5`/
`940632ecd1`, e.g. `note_model.{cpp,h}` gained 126 lines since the l1l2 freeze. The extraction ENGINE
functions — `blank_code`/`extract_functions`/`extract_python`/… — were not touched. The prior-layer
committed inventories are commit-stale, an OI-95-class housekeeping note one level up — recorded, not
fixed here.)*

### Inventory totals by area (deep rows)

| area | tag(s) | files | fn | lit | br | fld | dcl | x | io | **deep rows** |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **(a) joint module** | `JOINT` | 20 | 143 | 338 | 367 | 109 | 64 | 48 | 0 | **1,069** |
| **(b) record path/seams** | `RECORD-SEAM` | 12 | 86 | 93 | 472 | 10 | 17 | 140 | 0 | **818** |
| **(c) codegen machinery** | `CODEGEN` | 2 | 8 | 14 | 14 | 5 | 2 | 0 | 8 | **≈51** |
| **(d) new instruments** | `INSTRUMENT-JOINT` + `INSTRUMENT-SEAMS` | 33 | 538 | 1,543 | 2,028 | 54 | 0 | 32 | 284 | **≈4,479** |
| | | **67** | | | | | | | | **6,375** |

*(c) = the accessor `jointembeddedartifacts.h` (7 rows) + the source generator `gen_embedded_tables.py`
(~44 rows). **File-level, NOT deep** (per the dispatch): `jointembeddedartifacts.cpp` = a GENERATED
DATA population (180 KB of verbatim-embedded JSON bytes on a few long lines), established by its drift
guard (byte-equality vs the committed artifacts, LF-normalized, OI-195), not by row disposition;
`joint_embedded_tests.cpp` = the drift guard (`CODEGEN-GUARD`); the 10 joint tests = `JOINT-TEST`
(P4 characterization inputs).*

### (b) The legacy-arm tagging rule and the excluded count

The dispatch requires tagging every area-(b) row **record-arm / legacy-arm / shared** and excluding
legacy-only rows. **Doing that per row is DEEP work, not a mechanical inventory pass** — it needs
reading each `useJointNotationRecord` branch span. So this Task-1 inventory reports the **file rows
(818)** and the **record-arm ENTRY sites** mechanically, and hands the per-row arm split to area (b)'s
own deep pass. Mechanically identifiable record-arm entry: `useJointNotationRecord`/
`produceNotationRecord`/`analyzeSectionFromRecord` appears **12× in `notationcomposingbridge.cpp`, 9×
in `notationimplodebridge.cpp`, 6× in `notationtuningbridge.cpp`** — the record-arm branch heads.
`sectionrecordadapter.{h,cpp}` (474 rows) is **entirely record-arm** (it exists only for the record
path). The three big bridges (`notationcomposingbridge` 1522 lines, `notationimplodebridge` 1446,
`notationtuningbridge` 1302) are **majority legacy-arm / shared**: only the record-arm branches behind
the flag are in the OI-199 scope. **Estimated in-scope record-arm subset of area (b): the ~474
sectionrecordadapter rows + roughly 100–200 record-arm branch rows across the three bridges** — a
small fraction of the 818 file rows. The precise arm classification, and any site where the arms
CANNOT be separated mechanically (a #6 entanglement finding), is the area-(b) deep pass's Task 2.

## 2. Task 1 — the feasibility stop and the proposed partition

**The stop fired.** 6,375 deep rows across 67 files is 2–3× the largest single rigorous-disposition
session on record (L4 stopped at 2,121; L5 froze at 3,372). No silent sampling; the complete inventory
is frozen (`tools/audit/oi199/`). Only area (a) is dispositioned this session.

**Proposed partition** (honoring the two ratified ordering rules: the **joint module holds first
claim**; the **instruments are the SECOND partition**, Cowork's amendment — every figure steering this
arc came from them, #19):

| # | partition | files | rows | notes |
|---|---|--:|--:|---|
| **1** | **(a) the joint module** | 20 | **1,069** | **DONE THIS SESSION** (§3–§5). The production inference module on both surfaces. |
| **2** | **(d) the new instruments** | 33 | **≈4,479** | The figures steering this whole arc (#19). Large — needs a **2–3-way sub-split**: `tools/joint_estimator/*.py` (26 files, ≈4,061 rows — the fitting/parity/probe/search chain) is itself ≥2 sessions; `tools/notation_seams/*.py` (7 files, ≈420 rows) folds into one. Establishment form (#19): what each instrument measures, what oracle validates it, what is stamped, what breaks silently. Fold **(c) codegen** (≈51 rows) in here — the source generator physically lives among these instruments. |
| **3** | **(b) the record path/seams** | 12 | 818 file / ~600 in-scope | The record-arm subset only (the arm split is this partition's Task 2). One session; the work is the arm classification + the inference↔presentation boundary re-verification. |

Area (c) codegen (~51 deep rows + the generated-data population + the drift guard) is too small for its
own partition; fold it into partition 2. The partition JSON is `tools/audit/oi199/manifest.json` +
`file_table.csv`.

## 3. Task 2 — the joint module dispositions (protocol P2)

Every one of the **1,069 JOINT rows** carries a closed-set verdict in
`tools/audit/oi199/pass1_dispositions_joint.{csv,json}` (reproducible via
`tools/audit/oi199/gen_joint_dispositions.py`), applying the **same vocabulary** the L3/L4/L5 passes
used (SURVIVES / NO-ISSUE / ESTABLISHED / UNFIT / PUBLISHED / FORWARD-OK / BACK-EDGE-NOTE). "No issue"
is a recorded claim with a stated reason. I read the full inference core at the code
(`jointdecoder`, `jointfactadapter`, `jointadapter`, `jointprimitives`, `jointnotationrecord`,
`jointnotationproducer`, `labelclass`, `jointtables`, `jointweights`, `jointrender`) and verified the
load-bearing rows by hand.

| Row kind | Verdict tally |
|---|---|
| function (143) | SURVIVES 143 |
| decl (64) | SURVIVES 64 |
| branch (367) | NO-ISSUE 367 |
| literal (338) | ESTABLISHED 336 · **UNFIT 2** |
| field (109) | PUBLISHED 64 · SURVIVES 45 |
| crosslayer (48) | FORWARD-OK 47 · **BACK-EDGE-NOTE 1** |

**Reading of the tally.**
- **Functions / branches / decls — all SURVIVES / NO-ISSUE.** The joint module is production-surviving
  on both surfaces (the notation record path since THE SWITCH; the batch decode surface since OI-178);
  no function retires, no dead branch. The batch-only loaders (`loadPiecesFromNoteEvents`,
  `FittedAdapter::load`/`JointTables::load` from the filesystem) also SURVIVE (the batch/parity
  inference surface).
- **Literals — 336 ESTABLISHED, only 2 UNFIT.** This is the notable positive finding of the module:
  **the joint module's source is constant-CLEAN.** Its fitted parameters (the 13-weight vector, all
  table probabilities) are **externalized to the generated embedded artifacts**, so almost every
  source literal is a structural/theory constant (pc cardinality 12, the major/minor scale tables, the
  quality templates, the line-of-fifths maps, the tertian interval spellings) or a byte-established
  `probe_decoder`-parity reference value (the `safeLog`/emission floors `1e-6`/`1e-9`/`0.02`/`0.01`/
  `1/24`, verified bit-identical by the parity tests + the Neumaier-compensated `neumaierSum`
  reproducibility coupling). The only 2 UNFIT literals are the ratified-but-hand-chosen **decode
  hyperparameters**: `kKeyPruneTopK = 6` (`jointdecoder.cpp:39`) and `seg_cap = 4`
  (`jointnotationproducer.cpp:57`) — sweepable choices, committed under §5. (Contrast L3, which had
  ~60 UNFIT in-source emission constants.)
- **Fields — 64 PUBLISHED, 45 SURVIVES; the fact-publication check.** The module's OUTPUT surface is
  the §3 notation record (`NotationRecord`/`RecordSegment`/`RecordProvenance`/`EventBassFact`/`Modal*`/
  `SegmentSlice`) + the decode/producer outputs (`DecodeResult`/`SegmentSummary`/`NotationRecordResult`/
  `NoteView`). **Publication verified at consumers** (grep, outside `joint/`): `diatonicToKey` (12),
  `chordSymbol` (10), `romanNumeral` (6), `.slices`/posterior (2), `.provenance` (1),
  `bassPerEvent`/`rootSpellingLof` (read by `sectionrecordadapter`) — all PUBLISHED + consumed. **Two
  published families have NO current external consumer** — flagged as PUBLISHED-unconsumed (declared
  dormancy, named future consumer = the presentation layer): the **§3.4 modal reading**
  (`ModalKeyRun`/`ModalDegree`/`ModalInflection`, 10 fields — 0 consumers) and the **§3.2
  `augSixthSubType`** (1 field — 0 consumers; relates to the aug-sixth display-completeness work). The
  internal state fields (`Piece`/`NoteRec`/`ChordInfo`/`Framework`/`JointTables`/`WeightVector`/
  `m_apportionCache`/…) are SURVIVES. **No genuine silo, no trapped/overwritten fact was found.**
- **Cross-layer — 47 FORWARD-OK, 1 BACK-EDGE-NOTE.** The module reaches forward only: L1
  `note_model.h` (the sanctioned single fact source, OI-180), the engraving score model
  (`engraving/dom/*` — a fact adapter reading the structural score), and the muse framework
  (`serialization/json.h`, `types/bytearray.h`). **One back-edge:** `jointprimitives.cpp` →
  `chord/analysisutils.h` for `normalizePc` — the sanctioned dependency-free pitch leaf, the exact
  OI-93/OI-86 shape (a layering smell, not a heavy coupling; the header documents it and the
  inference↔presentation boundary guard exempts it).

## 4. Task 2 — contract-direction check (protocol P3)

From `ARCHITECTURE.md` (the ★★ joint-estimator governing decision + the AS-BUILT record-path section,
lines 3–250) and `cowork_notation_output_contract.md` §3 as cited there, the joint module must:
extract L1 facts + structural facts → decode the event lattice with the exact block-factorized
semi-Markov Viterbi (seg_cap 4, top-K key prune) → assemble the §3 notation record (committed facts +
derived facts + posterior slice + modal reading) → publish it as the ONE output surface, with a hard
inference↔presentation boundary. Each expectation located in the code:

| Contract expectation | Located in code | Status |
|---|---|---|
| L1-only fact extraction (no raw-DOM walk) | `buildAdapterFacts` reads `NoteModel::notatedNotes()` + `engraving/dom` structural facts only | ✅ present (OI-180) |
| input-scoping via `excludeStaves` (OI-204) | `buildAdapterFacts(score, stem, excludeStaves)` skips excluded-staff notes at the fact layer | ✅ present (empty default = byte-identical) |
| exact block-factorized semi-Markov Viterbi | `decodePiece` — the DP over `V[0..N]`, per-boundary states, §5 total-order tie-break | ✅ present, `probe_decoder`-parity |
| seg_cap 4, top-K key prune (K=6) | `seg_cap` arg = 4 (`jointnotationproducer.cpp:57`); `kKeyPruneTopK = 6` (`jointdecoder.cpp:39`) | ✅ present (the 2 UNFIT hyperparameters) |
| candidate content gates (root-present / member-overlap / fit) | `candidateStates` (`jointdecoder.cpp:438/444-445/448`) | ✅ present — **behavioral note in §5** |
| §5 total-order tie-break (fewer segments; earliest ticks; class order) | `sigLess`/`prefixSig`/`fullSig`/`better`/`betterPrefix` | ✅ present, no epsilon |
| the 13 factors (emission/spelling/bass/absent/boundary/entry/keyTrans/chordTrans/prior + 4 cadence) | `FittedAdapter::*Logp` + the Katz below-threshold apportionment (§5 option 2a) | ✅ present |
| reproducibility coupling (Neumaier-compensated sum == CPython `sum()`) | `neumaierSum` (`jointprimitives.h:66`), used at `weightedContent`/`cadenceAt`/`distSum` | ✅ present, documented, parity-verified |
| §3.1 piece block + provenance from the D1 embedded constants | `assembleNotationRecord` §3.1 + `RecordProvenance` from `embedded::*` | ✅ present (discharges the constants' dormancy) |
| §3.2 committed + derived facts (spellings/members/diatonicToKey/bass roles/augSixth subtype) | `assembleNotationRecord` §3.2, `recordDiatonicToKey`, `recordAugSixthSubType`, `jointprimitives::rootSpellingLof`/`factorSpellingLof` | ✅ present (structural read, OI-173 lesson) |
| §3.3 posterior slice attached, not recomputed | `computePosteriorSlice` → `rec.slices` | ✅ present |
| §3.4 un-rounded modal reading | `computeModalReading` → `rec.modalReading` | ✅ present — **but unconsumed (§3 finding)** |
| §3.5 ornament fields RESERVED-absent; §3.6 excluded fields absent | no field declared | ✅ correct-by-absence |
| whole-score decode ONCE, deterministic, NO caching; unambiguous failure never partial (#13) | `produceNotationRecord` (both overloads); `ok=false`/empty on adapter failure | ✅ present |
| render primitives single-sourced (§5.6 formatter continuity, #6) | `jointrender` (`jointChordSymbol`/`jointRenderRn`/`jointOursQuality`), reused by the record | ✅ present |
| inference↔presentation boundary: the joint module includes NO legacy presentation formatter | crosslayer scan: `joint/` includes NO `chordsymbolformatter`/`chordanalyzer.h` (only the exempt `analysisutils.h` pc leaf) | ✅ present (the boundary holds from the joint side; the guard test is area (b)) |

**Two-sided result (the finding is any expectation with no code, or any code with no expectation):**
- **Expectation with no code:** none found — every §3 contract item is realized.
- **Code with no expectation / a stale contract statement:** **the module's own headers uniformly
  assert DORMANCY that the code has outgrown.** `jointdecoder.h:43`, `labelclass.h:39`, `jointadapter.h:41`,
  `jointtables.h:44-45`, `jointweights.h`, and `jointnotationrecord.h:48-50` all say "DORMANT (no
  production consumer)" / "Nothing in src/ reads it yet" / "the weights are applied … in a later commit
  / this increment is dormant." **These are stale post-switch.** The flag default is `Val(true)`
  (`composingconfiguration.cpp:178`, correctly commented), and the three notation bridges call
  `produceNotationRecord` behind it — so the module IS the production notation analysis. A #10 doc-sync
  finding (see §6).

## 5. Task 2 — behavioral characterization (protocol P4)

**Route A — the test suite.** `composing_tests` joint suites: **78/78 pass** across 17 suites
(`JointAdapterTest`, `JointDecoderTests`, `JointEmbeddedDriftGuard`/`Load`/`Provenance`,
`JointModalTests`, `JointPrimitivesTests`, `JointProducerTests`, `JointRecordTests`, `JointSliceTests`,
`JointSpellingTests`, `JointLabelClassTests`, `JointWeightsTests`, `JointTablesLoadTest`/`Tests`,
`JointKeyDecision`, + the two boundary-guard tests + `NoCoupledCoreSoftEqualsJoint`). The module's
mechanisms are covered including the drift guard, the parity spot-checks, the null-score failure path,
the span-view/note-view boundary rules, and the empty-input case (`JointKeyDecision.EmptyInput`).

**Route B — fire structure of the decode (characterized from the code; no counter built).** Following
the L4-decoder precedent (which characterized fire rates from existing diagnostics without new
instrumentation), and to keep this pass read-only and cheap, I did NOT add a fire-count counter; the
load-bearing branches are characterized structurally from the code (a per-branch fire-count counter
under the OI-110 discipline is the area-(a) deep pass's completion, route named). The three
mechanisms that carry the module's behavior:

1. **The candidate content gate (`candidateStates`, `jointdecoder.cpp:427-454`).** Three gates
   compose per candidate `(key, class)` over a window `[i, j)`: **(1) ROOT-PRESENT** (`:438` — the
   class root pc must be in the window's onset-pc union), **(2) MEMBER-OVERLAP** (`:444-445` —
   `popcount(mem & onsetPcs) ≥ min(2, |mem|)`; every vocabulary class has ≥2 members, so this demands
   ≥2 distinct member pcs among the onsets), **(3) FIT** (`:448`). **Structural consequence, derivable
   from the code:** a window whose onset-pc union has **fewer than 2 distinct pcs** admits NOTHING —
   gate (2) rejects every class. In the DP, a boundary with no candidate on any admissible window gets
   no state; if some event's every `≤ segCap` window is that sparse, `V[N]` stays empty and the decode
   returns `complete=false`, **0 segments** (`:838-841` — a branch the authors explicitly coded, i.e.
   anticipated). On the dense 4-voice chorale corpus this NEVER fires empty (route A + the parity
   corpus all complete); the empty branch's real population is **sparse/sustained/unison texture**,
   which the chorale corpus does not exercise. (This is the S1 mechanism — see the §7 reconciliation.)
2. **The DP inner-loop state is `std::string`-keyed throughout.** The semi-Markov DP
   (`jointdecoder.cpp:732-836`) builds a `std::string` per candidate per window per boundary:
   `stateEnc(tonic,major,ckey)` (`:820`), the `content()` cache key
   `to_string(i)+","+to_string(j)+","+stateEnc(...)` (`:659`), the `candidates()` cache key (`:651`),
   `keyEnc` (`:793`), and `StateEntry::backEnc` — all keyed into `unordered_map<std::string, …>`
   (`bh.idx`, `contentCache`, `candCache`, `kchg`, `perClass`, `summ`). This is heap-allocating string
   construction + hashing in the hottest loop — the dominant per-candidate cost shape. (This is the S2
   mechanism — a cost-structural observation, blind from the disposition of these rows; the *direction*
   of the C++-vs-Python comparison is a timing claim I did not measure.)
3. **`buildAdapterFacts` re-scans all notes per boundary.** The event-lattice construction
   (`jointfactadapter.cpp:465-491`) nests `for (const NoteRec& n : notes)` (`:471`, the `anySounding`
   scan) inside `for (bi …)` over the boundary list (`:466`) → **O(events × notes)**; and `melodic`
   (`:279`) scans the whole part-note list twice per call and is called per note (`:439-442`) →
   **O(notes × part_notes)**. Both are repeated full scans that a sweep-line / interval index would
   make linear — the near-quadratic event scaling. (This is the S3 mechanism — a DT-6-adjacent
   repeated-derivation / efficiency shape, blind from the disposition of the fact-build loop.)

**Read:** the joint module is a clean, well-tested, `probe_decoder`-parity port whose inference is
correct and whose output surface carries the contract facts. Its behavioral risks are **not
correctness of the decode arithmetic** but **(i)** an all-or-nothing empty-result on out-of-envelope
(sparse) texture and **(ii)** a cost structure (string-keyed DP + quadratic fact-build) that the
chorale-fit envelope never stressed. All three are surfaceable from the code/artifacts; the register
rows for them are written at Task 4 (§7).

## 6. FINDINGS (blind pass) — recorded for the register (written at Task 4)

Most-load-bearing first. Nothing is fixed this session (principle 8); each is a register row in the
Task-4 unblind commit. Per the guiding-principle 8 constraint (no inference-problem-driven coding) and
the auditor-not-amender rule, these are **declared to Cowork**, not acted on.

- **F-OI199-1 (medium, #10 doc-sync / DT-12) — the joint module's headers uniformly claim DORMANCY the
  code has outgrown.** Six+ headers (`jointdecoder.h:43`, `labelclass.h:39`, `jointadapter.h:41`,
  `jointtables.h:44`, `jointweights.h`, `jointnotationrecord.h:48-50`) say "DORMANT — no production
  consumer" while the module is the production notation analysis (flag default `Val(true)`; the three
  bridges call `produceNotationRecord`). Documentation not in sync with code (§10). *(Also present in
  area (b): the record-arm branch-site comments say "default OFF" — that is the record-seam pass's
  finding.)*
- **F-OI199-2 (low-medium, fact-publication corollary / DT-5) — two published record facts have no
  consumer.** The §3.4 modal reading (`modalReading`, 10 fields) and the §3.2 `augSixthSubType` are on
  the published surface but consumed by nobody outside `joint/` (grep-verified). Declared dormancy
  (named future consumer = the presentation layer, per the contract), so not waste — but flagged so a
  reader does not mistake them for live signals, and so their future consumer is tracked.
- **F-OI199-3 (behavioral, for Cowork — an inference concern, DECLARED not acted) — the content gate
  empties the whole analysis on sparse texture.** `candidateStates`' `≥2-member` gate + the `V[N]`-empty
  branch return an empty `complete=false` analysis when a segment's admissible windows all carry <2
  distinct onset pcs. Structural; the chorale corpus never exercises it. **This is an inference-behavior
  matter (all-or-nothing, no partial result — itself a #12 information-loss shape), declared to Cowork
  per the standing "no inference-problem-driven coding; declare to Cowork" rule.**
- **F-OI199-4 (cost-structural, for Cowork) — the DP is `std::string`-keyed in its hot loop** and
  **`buildAdapterFacts` is near-quadratic** (nested per-boundary note scans + per-note part scans).
  Both are performance shapes, not correctness defects; declared, not acted.
- **F-OI199-5 (process, DT-20 — the most important process finding) — this pass's blinding was
  DEFEATED at the source.** Both the mandatory `STATUS.md` read and the dispatch's inline §S carried the
  full S1/S2/S3 text before Task 1. The exact OI-89 shape. The remedy is the OI-89 remedy, generalized:
  a blind dispatch must cross-check every required read (and its own body) against every withholding
  requirement — `STATUS.md`'s rolling headline and the dispatch's own §S both violated it here.
- **F-OI199-6 (housekeeping, DT-12/OI-95) — the prior-layer inventory artifacts are commit-stale.**
  The committed `tools/audit/{l1l2,l3,l4,l5}/` deep CSVs predate the joint arc; regenerating at HEAD
  differs by source drift (proven not to be a tooling change). An OI-95-class note, one level up.
- **F-OI199-7 (positive finding, recorded) — the joint module source is constant-clean.** 336/338
  literals ESTABLISHED, only 2 UNFIT (decode hyperparameters); the fitted values are externalized to
  the generated artifacts. A structural strength worth recording (it means the source carries almost no
  un-established tunable, unlike the L3/L4 scorers).

## 7. Task 4 — unblind, the register, and the reconciliation (written after the freeze `0ea3d31204`)

**Withheld files first opened AFTER the freeze commit `0ea3d31204`, in order:** `OPEN_ITEMS.md`, the
`open_items/OI-*.md` detail files (OI-215, OI-199), §S as an object of analysis. The freeze is the
provenance boundary; the §0–§6 content above was fixed before it. *(The unavoidable exception — the
whole point of OI-222 — is that S1/S2/S3 were already in my context from the mandatory `STATUS.md` read
and the dispatch's inline §S, before Task 1.)*

### 7.1 Register rows written (rule (c): index row + detail file in this commit)

| OI | what | class |
|---|---|---|
| **OI-215** (existing) | S1 — the empty analysis on sparse texture. Read, not re-rowed; a pass-1 confirmation note appended. | STOP (#13) |
| **OI-216** (new) | S2 — the C++ decode is `std::string`-keyed in the DP hot loop; appears slower than Python. | cost |
| **OI-217** (new) | S3 — `buildAdapterFacts` is near-quadratic (repeated note scans). | cost |
| **OI-218** (new) | S4 — incremental patching is UNMEASURED, not refuted (record). | correction of record |
| **OI-219** (new) | S5 — the #17(b) prediction bands were not pre-registered (record). | process |
| **OI-220** (new) | F-OI199-1 — the joint headers assert stale dormancy (#10). | doc-sync |
| **OI-221** (new) | F-OI199-2 — two published record facts unconsumed (declared dormancy). | fact-publication |
| **OI-222** (new) | F-OI199-5 — the blinding was defeated at the source (DT-20). | process |
| **OI-223** (new) | F-OI199-6 — the prior-layer inventories are commit-stale (OI-95 class). | housekeeping |

F-OI199-7 (the constant-clean positive finding) is recorded in the OI-199 detail file, not rowed (a
strength, not an issue). F-OI199-3/4 map to OI-215/216/217. The OI-199 index row + detail carry the
pass-1 delivery; certification remains WITHHELD.

### 7.2 THE RECONCILIATION — and why it cannot be the clean measurement the sealing intended

**★ The sealing was defeated before Task 1 (OI-222 / DT-20).** The three sealed findings were in my
context from two mandatory sources — `STATUS.md`'s current top entry (a required read) states S1 with
its exact line cites, S2 with the `std::string`-state hypothesis, and S3 with `events^1.80`; and the
dispatch delivered §S inline. **So I cannot honestly report "found it blind."** I report instead the
knowledge-independent question the artifacts *can* answer: **does a rigorous disposition + the P4
structural characterization point at each finding's mechanism on its own merits, regardless of what I
knew?** That is a real, useful measurement of the audit *method*'s reach — it just is not the
blind-recall measurement the sealing wanted (which pass 2, a fresh session, must supply). I do not
rationalize this; the leak is a finding about the method's delivery (OI-222), exactly the cheap lesson
the sealing exists to produce.

**The three-line verdict table** (verdict = does the method's ARTIFACT/disposition surface the
mechanism on its merits; every line carries the blindness caveat):

| finding | verdict | basis, and the honest limit |
|---|---|---|
| **S1** (content gate empties the analysis) | **ARTIFACT-SURFACED (structurally) — NOT blind** | The P4 characterization (§5.1) surfaces the `candidateStates` ≥2-member gate AND the explicitly-coded `V[N]`-empty branch (`:838-841`), and states the empty branch's population is sparse texture the chorale corpus does not exercise. **But:** a pure fire-rate ON THE PINNED (chorale) CORPUS would show the empty branch at **0%** and MISS the real-world failure entirely — surfacing S1 needs the *structural* read of `candidateStates` + the coded empty branch, not the corpus counters. And the pass was not blind (OI-222). So: the method's *structural* arm reaches S1; its *corpus-fire-rate* arm alone would miss it; blind recall is unproven here. |
| **S2** (string-keyed DP; C++ slower) | **ARTIFACT-SURFACED (the cost cause) — NOT blind; direction unmeasured** | The disposition of the DP rows + §5.2 flag the `std::string`-keyed hot loop (stateEnc/keyEnc/to_string keys, `unordered_map<string>`) as the dominant per-candidate cost shape (→ OI-216) — a code-reading observation independent of timing. **But:** the *direction* of the comparison (C++ slower than Python) is Cowork's timing measurement; I did not re-measure it. And not blind (OI-222). |
| **S3** (`buildAdapterFacts` super-linear) | **ARTIFACT-SURFACED (the scan cause) — NOT blind; exponent unmeasured** | §5.3 + the disposition of the fact-build flag the O(events·notes) event-lattice scan + the O(part²) `melodic` scan (→ OI-217) — a code-reading observation. **But:** the *exponent* (1.80) is Cowork's fit; I did not measure the scaling. And not blind (OI-222). |

**What this tells the user about the remaining OI-199 partitions.** The mechanical audit method's
*structural* arm (a rigorous per-row disposition + a code-read P4) demonstrably reaches all three
sealed mechanisms — that is genuine evidence the deep passes are worth their cost. The method's
*corpus-fire-rate* arm, run only on the fit corpus, would have MISSED the most important one (S1) —
a concrete lesson: the deep passes must characterize behavior on **out-of-envelope inputs**, not only
the pinned corpus, or they will rubber-stamp exactly the robustness cliffs that matter. And the whole
"is the method blind" question is unanswered by this pass and must be re-measured by a genuinely blind
pass 2 (fresh session, seeded error rate) with the OI-222 remedy applied — do not headline the withheld
findings in a mandatory read; keep §S in a separate post-freeze artifact.

### 7.3 Certification status

**WITHHELD.** Pass 1 (blind enumerative) found **no correctness defect** in the joint module — a clean,
well-tested, `probe_decoder`-parity port whose output surface carries the §3 contract facts and whose
layering is forward-only bar one sanctioned pc-leaf back-edge; its risks are the cost/robustness
shapes (OI-215/216/217, all declared to Cowork, none fixed) and the doc-sync/publication hygiene
(OI-220/221). But certification needs BOTH passes plus the P6 error rate: pass 2 (a genuinely blind
second reading in a fresh session, a seeded error rate at full vocabulary, the whole-scope DT-signature
sweep) AND the partition-2/3 deep passes are owed, and this pass's blinding was compromised (OI-222).
Certification is not self-granted; it returns to the user on the measured record after pass 2.

## 8. Self-check (CLAUDE.md, run over the actual diff before reporting done)

Re-read every touched file's diff against the guiding principles / conventions / gate policy /
DEFECT_TYPES:
- **#8 / auditor-not-amender:** no inference code, no fix — read-only; every discovered issue is a
  register row, not a patch. The only code change is the `gen_inventory.py` tooling extension +
  read-only disposition scripts. ✓
- **#6 (one path):** the SAME `gen_inventory.py` extended (`--layer oi199`), no parallel tool; proven
  inert for L1/L2/L3/L4/L5 (byte-identical vs a minimal joint-rule-only tool). ✓
- **#15/#19 (verify at objects; establish):** every population tag and every load-bearing row verified
  at the code + call sites (the dormancy contradiction, the publication grep, the crosslayer scan, the
  content-gate/empty-branch, the DP string state, the fact-build scans); no inherited tag trusted. ✓
- **#16 (reproducibility):** artifacts manifest-stamped (HEAD `5135764ed7`, corpus `c50002fee1`, script
  blob sha); dispositions reproducible via `gen_joint_dispositions.py`. ✓
- **Conventions (no self-invented labels):** verdicts are the L3/L4/L5 set verbatim
  (SURVIVES/NO-ISSUE/ESTABLISHED/UNFIT/PUBLISHED/FORWARD-OK/BACK-EDGE-NOTE); tags follow the existing
  `L4-SCORER`/`L5-DORMANT`/`INSTRUMENT-*` pattern (JOINT/CODEGEN/RECORD-SEAM/INSTRUMENT-JOINT/
  INSTRUMENT-SEAMS); finding IDs follow the `F-L5-N` style. Reasons cite real repository names. ✓
- **Scope:** no `src/` change, no constant tuned, no golden/`tools/corpus/`/`tools/robust_stop/`
  movement, no behavior change. No counter was built (P4 via existing tests + structural read), so no
  build/revert cycle and no byte-identity question arises; the compiled suites are unaffected (baseline
  joint tests 78/78 confirmed at HEAD). ✓
- **Git/shell rules:** `; echo "exit:$?"` on fallible commands; large output redirected; files staged
  by name; the riding Cowork STATUS/handoff edits preserved; `cc_*.md` force-added; `origin` only. ✓
- **A surprise is a STOP (#13):** the two STOP-class items — S1/OI-215 (already a rowed STOP) and the
  DT-20 blinding failure (OI-222) — are surfaced, not built around; nothing was worked around. ✓
