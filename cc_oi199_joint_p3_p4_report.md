# CC REPORT — OI-199 joint module: completing the CONTRACT-DIRECTION check (P3, second side) and the BEHAVIOURAL characterization (P4) to the L4 standard, on BOTH corpora

> **Session 2026-07-28.** Executes `cc_instruction_oi199_joint_p3_p4.md` (Cowork dispatch, at the
> user's ruling, amended alternative 2). **Read-only characterization** — the pass-1 dispositions are
> NOT redone; two arms (P4 corpus routes + fire counts; P3's second side) are completed to the L4
> precedent standard (`cc_l4_audit_pass1_decoder_report.md`). Base HEAD `b14a523112` (verified).
>
> **The governing question: IS OI-215 ALONE?** — is the empty-decode cliff (OI-215, the candidate-
> admission member-overlap gate on <2-onset-pc windows) the SOLE admission-rule-class / coverage-class
> failure, or does it have siblings (a root-present or NCT-budget failure)? #3 forbids designing a fix
> around one instance without enumerating the family. This report answers it by measurement.
>
> **Scope discipline (all held):** the only `src/` change is the DEFAULT-OFF fire-count instrument in
> `src/composing/analysis/joint/jointdecoder.{h,cpp}` (OI-110 disposition — byte-identical off, REVERTED
> in its own final commit, hash recorded) + the DISABLED test-harness drivers in
> `pipeline_snapshot_tests.cpp`. No constant tuned, no golden/`tools/corpus/`/`tools/robust_stop/`
> movement, no behaviour change, no fix, no design. The frozen dispositions CSV is ANNOTATED beside,
> never rewritten (#10/#12).

## 0. Predictions (pre-registered BEFORE the measuring run — #17b)

Per Task 0 and the standing OI-219 reminder, prediction bands were registered in
`tools/audit/oi199/task1_predictions.md` **before** the `JointFireFit`/`JointFireLarge` sweeps ran.
The measured outcome is checked against each band in §3.4. (The last dispatch registered none; this is
the guard OI-219 exists to enforce.)

## 1. The instrument (OI-110 disposition — default-OFF, byte-identical off, reverted at close)

`jointdecoder.{h,cpp}` gains a `JointFireCounters` struct + a runtime-enabled flag
(`jointFireSetEnabled`). Every counting site is guarded; the returned candidate/segment data is
untouched, so the decode OUTPUT is byte-identical whether the counter is on or off — and no production
path ever calls `jointFireSetEnabled(true)`. It counts, on the REAL code paths (no re-implementation, #6):

- **candidate admission** (`candidateStates`): windows examined, `(key,class)` pairs offered, and
  rejections split by the three gates — **(1) ROOT-PRESENT**, **(2) MEMBER-OVERLAP** (the OI-215 gate,
  `present < min(2,|members|)`), **(3) FIT** (NCT budget `nOnset − present > max(1, j−i)`) — plus a
  per-window distinct-onset-pc histogram.
- **the DP** (`decodePiece`): pieces / complete / **empty** (the OI-215 `V[N]`-empty outcome branch),
  segments, and the three transition branches actually chosen ((a) initial / (b) same-key / (c)
  key-change), the two candidate-skip branches (content = −∞ / no admissible predecessor), and state
  insert/improve.
- **per-event coverability** (`scanCoverage`): for each event, examine every ≤segCap window containing
  it via the REAL `candidateStates`; classify each **uncoverable** event by the responsible gate —
  `memberOverlapPure` (< 2 onset pcs everywhere = the OI-215 theorem), `memberOverlapRich` (a ≥2-pc
  window that still fails gate 2 = the same gate, broader trigger), `fitBlocked` (a rich window passed
  gates 1&2 but failed gate 3 = a SIBLING gate), `rootOnly` (rich windows never got a class past gate 1
  = a SIBLING gate). **This decomposition IS the "is OI-215 alone" answer.**

Byte-identity proof with the instrument off: joint composing suite **78/78 pass**; pipeline-snapshot
goldens pass (record-path byte-identical); and the final revert (§Task 4) restores `src/` bit-identical
to `b14a523112`.

## 2. Task 2 — P3's second side: every joint-decode mechanism, checked against a ratified basis

Two-sided as the P3 protocol requires; the side that under-delivered at pass 1 (the second — code with
no ratified expectation) is done exhaustively here, working from the ratified documents
(`cowork_joint_estimator_factorization.md` §2/§4/§5, `cowork_factorization_desk_simulation.md` §6a,
`cowork_prefit_gates.md`, `cowork_notation_output_contract.md` §3.3, `cowork_joint_estimator_architecture.md`).

### 2.1 The headline: CANDIDATE ADMISSION has NO stated basis in the ratified decode plan — CONFIRMED

The production decoder admits `(key, class)` states per segment through **three gates** in
`candidateStates` (`jointdecoder.cpp:435-451`): **(1) root-present** (`:438`), **(2) member-overlap**
`present < min(2,|members|)` (`:444-445`), **(3) fit / NCT budget** `(nOnset − present) > max(1, j−i)`
(`:448`). Preceding them, `candidateKeys` (`:398-421`) prunes the key axis to the **top-6 by onset-pc
overlap** + the always-kept signature key (`kKeyPruneTopK = 6`, `:39`).

**What the ratified decode plan (`cowork_joint_estimator_factorization.md` §5) actually specifies:** the
state space is **"24 keys × the degree vocabulary"** (§5, line 167; re-affirmed in the architecture doc
line 75 "the ratified state space is compact: 24 keys × the degree vocabulary"); the transition
factorizes into the block structure; ties break by the §5 total order; below-threshold continuations
score by the option-2a leftover; **"the full posterior (not only the best path) is retained."** The ONLY
pruning §5 contemplates is the **segment-length cap** (line 113/170, "the established semi-Markov
default" — ratified) and, as a RESERVE, "restricting key-change candidates to a fitted-mass neighborhood
on the circle of fifths … an inference technique requiring its own established-loss measurement, never a
silent heuristic" (lines 171-173).

**The finding (Cowork's claim CONFIRMED, with the precise nuance):**
- The **candidate-admission gates** (root-present / member-overlap / NCT-budget) are **described
  nowhere** in §5, the premise ledger §4 (P1–P8), `cowork_prefit_gates.md`, or
  `cowork_notation_output_contract.md`. They entered production via the byte-for-byte
  `probe_decoder.decode_piece` port (`jointdecoder.h:37-39`) carrying only inline comments. **A
  production inference rule that was never a ratified premise** — exactly OI-207's subject matter, and
  the rule that empties the analysis on 13/23 large scores (OI-215).
- The **top-6 key prune** is a *different* prune than the one §5 reserves: §5 reserves a
  **circle-of-fifths fitted-mass** neighbourhood; the code prunes by **onset-pc overlap ranking**. Its
  loss is measured (see below) but its *form* was never the ratified reserve.
- The desk simulation (`cowork_factorization_desk_simulation.md` §6a) *did* truncate the candidate set
  for the hand-trace — but as a declared **tractability convenience** ("all excluded keys fail on
  first-event membership", line 161), NOT a ratification of the production gate forms/thresholds. The
  production gates were never desk-simulated.
- **Partial mitigation, recorded honestly:** OI-188 (`open_items/OI-188.md`) already *measures* the
  cost of "the decode-time key-fit prune + **root-present/member-overlap filters**" — GT reachability
  ~72 %, the GT state force-added on **14,257 spans**, and the prune's grading cost re-measured at the
  fitted weights. So the filters' **cost** is known; what is absent is any **derivation of their form**
  from theory or any ratification gate — they are a lamented cost, not a designed rule. This is precisely
  why OI-215 (a member-overlap filter is one of the filters OI-188 names) needs a *form* decision, not a
  knob-turn.

**Consequence for the OI-215 fix design:** the fix is not "relax a threshold" — it is to give candidate
admission (and the two prunes) a ratified basis for the first time, covering the whole family §3
enumerates. Declared to Cowork; not designed here.

### 2.2 Onset vs sounding pitch classes — CONFIRMED at the code

The dispatch's specific check: the admission filters test **onset** pcs while the segment's **sounding**
pcs are computed on the adjacent line. Confirmed:
- `candidateStates` builds `onsetPcs` from `piece.evOnsetPcs[e]` (`jointdecoder.cpp:427-430`) — the
  union of the pcs of notes whose **onset** falls in each event (`Piece::prepare`,
  `jointdecoder.cpp:116-123`). Gates 1/2/3 all test this **onset** union.
- The within-segment content/`missing` factor uses `segPcs = piece.overlapPcs(i, j)`
  (`segmentContentScore` → `segmentFeatures`, `jointdecoder.cpp:461-462`; C++ mirror of the reference's
  `piece.overlap_pcs(i, j)`) — the pcs of every note **sounding** (overlapping) the segment span,
  onset-inside-or-not.
- **The asymmetry is causally central to OI-215:** a note that sounds *through* a window but onsets
  *before* it contributes to the content score but **not** to the admission onset union. Sustained /
  tied / pedal textures therefore present <2 *onset* pcs to gate 2 even while ≥2 pcs *sound* — the exact
  orchestral case (a solo line over held harmony) that empties the decode. So the admission gate is
  blind to precisely the sounding harmony the content factor would score.

### 2.3 Other mechanisms with no (or partial) ratified basis

| mechanism | code | ratified basis? |
|---|---|---|
| candidate-admission gates (root-present / member-overlap / NCT budget) | `candidateStates:438/444-445/448` | **NONE** in §5 / §4 / prefit-gates / contract; cost only in OI-188 (§2.1) |
| top-6 key prune by onset-pc overlap | `candidateKeys` + `kKeyPruneTopK=6:39` | §5 reserves a DIFFERENT prune (circle-of-fifths fitted-mass); loss measured OI-188; form not ratified |
| the two decode hyperparameters `seg_cap=4`, `kKeyPruneTopK=6` | `jointnotationproducer.cpp:57`; `:39` | seg_cap ratified (§5 "established semi-Markov default"); topK not (the 2 UNFIT literals, pass-1 §3; absent from `param_manifest.json` — §Task 3) |
| full-posterior retention | code retains best-path + a re-scoring §3.3 slice only | §5 says "the full posterior … is retained"; the forward-backward marginals are NOT built — tracked at OI-193 (a known gap, not new) |
| the §5 total-order tie-break; option-2a leftover; the 10 factors; Neumaier coupling; §3.1-3.6 record | `sigLess`/`prefixSig`/…; `FittedAdapter::*Logp`; `neumaierSum`; `assembleNotationRecord` | **RATIFIED** (§5, §5a-2a, §2, #16, contract §3) — present and faithful (pass-1 §4 confirmed) |

Everything except the admission/prune rules (and the known OI-193 posterior gap) has a ratified basis
and is faithfully implemented — consistent with pass 1's "clean `probe_decoder`-parity port." The one
material second-side finding is candidate admission (§2.1).

## 3. Task 1 — P4 to the L4 standard: per-branch + per-filter fire counts on BOTH corpora

The DEFAULT-OFF counter (§1) was run over **(A) the fit corpus** — the 326 covered chorales
(`note_events.json`), the population every prior characterization used — and **(B) the 23 committed
large scores** (`tools/extra scores/large/`), the repertoire the large-score requirement (OI-209) names,
characterized on this module for the first time. Artifacts: `tools/audit/oi199/joint_firecount_fit.json`,
`joint_firecount_large.json`.

**Measurement note (declared, #16):** on (A) the `scanCoverage` admission+coverage pass covers ALL 326
pieces with `sigFifths = nullopt`. That is the CONSERVATIVE choice for the coverability question —
supplying the signature key can only ADD a candidate key, never remove one, so `nullopt` can only
OVER-count uncoverable events; measuring 0 (below) settles it for the real-signature case too. The (A)
DP-branch fires are from a **declared representative 60-piece decode sample** (matching the L4 precedent's
declared-sample discipline for the expensive decode route); the coverage + admission + onset-diversity
are the full 326. On (B) the real `fx.sigFifths` from `buildAdapterFacts` is used throughout.

### 3.1 Coverage — the decisive "is OI-215 alone" decomposition

Every uncoverable event is classified by the responsible admission gate (`scanCoverage`, §1). **This
table is the answer.**

| population | events | uncoverable | memberOverlapPure (OI-215 theorem) | memberOverlapRich (same gate, ≥2 pcs) | **fitBlocked (gate-3 SIBLING)** | rootOnly (gate-1 SIBLING) |
|---|--:|--:|--:|--:|--:|--:|
| **(A) fit corpus (326)** | 26,698 | **0** | 0 | 0 | **0** | 0 |
| **(B) large scores (23)** | 172,611 | **312** | 291 (93.3 %) | 0 | **21 (6.7 %)** | 0 |

**(A):** 0 uncoverable events across all 326 chorales; **326/326 pieces complete.** The fit corpus never
exhibits any admission-class failure — OI-215 and every candidate sibling are INVISIBLE on it (which is
exactly why the pass-1 corpus-fire-rate arm would have missed OI-215). Notably ~7.3 % of the fit corpus's
windows already carry <2 distinct onset pcs (histogram §3.2), yet 0 events are uncoverable, because every
event has at least one *rich* covering window — the chorale density that shields it.

**(B): 13 of 23 scores decode empty** (uncoverable > 0 → `complete = false`): beethoven_sym7 (60),
beethoven_sym9 (56) + its openscore upload (56), holst_planets (52), haydn8 (27), schubert_d810 (23),
holst_mercury (13), tchaikovsky (8), dvorak_cello III (7)/I (4), butterworth (3), haydn6 (2), gluck (1).
The other 10 complete (both brandenburg3 uploads, brandenburg4, mass, art_of_fugue, dvorak_cello II,
dvorak_sym9, faure, both jupiter uploads). **The two decoded empties (butterworth 0 segs, holst_mercury
0 segs) confirm the theorem at the objects.** This reproduces OI-215's `large_score_profile_counts.json`
scan for the pure member-overlap counts EXACTLY (beethoven_sym7 60, holst_mercury 13, gluck 1, …).

### 3.1.1 ★ THE ANSWER: OI-215 IS **NOT** ALONE — a second admission gate has a measured sibling

**291 of the 312 uncoverable events (93.3 %) are the OI-215 member-overlap gate on <2-onset-pc windows —
but 21 (6.7 %) are a DISTINCT gate: the FIT / non-chord-tone-budget gate (gate 3).** `uncovRootOnly = 0`
and `uncovMemberOverlapRich = 0`, so gate 1 never solely blocks and gate 2 fires only on its <2-pc
theorem case; the *only* two active failure gates are member-overlap and FIT. The 21 `fitBlocked` events:
**holst_planets 14, tchaikovsky_1812 5, beethoven_sym9 1 (+ its openscore upload 1).**

**The sibling's mechanism (opposite extreme to OI-215).** A `fitBlocked` event has a rich covering window
where a class passes gate 1 (root present) and gate 2 (≥2 members present) but fails gate 3
`(nOnset − present) > max(1, j−i)` — and no covering window admits anything. This is a **very DENSE**
event: many simultaneous onset pcs, so any 3–4-member chord leaves `nOnset − present` non-chord tones far
exceeding the budget (≤ 4, the segment length). OI-215 is the **SPARSE** cliff (member-overlap, too FEW
onset pcs); this sibling is the **DENSE** cliff (NCT-budget, too MANY onset pcs for any single chord to
fit) — concentrated in the most chromatic/tutti writing (Holst's planetary chords, the 1812's cannon
tutti). They sit at OPPOSITE ends of the onset-density spectrum and are governed by DIFFERENT gates.

**★ Corollary — OI-215's own measurement instrument UNDERCOUNTS.** The `< 2 onset pcs` proxy in
`large_score_profile_counts.json` (the scan that founded OI-215) is a sound *sufficient* condition for
member-overlap only; it is BLIND to the FIT-gate sibling. This dispatch's `scanCoverage` runs the REAL
`candidateStates` (all three gates) and finds the true uncoverable count is **312, not 291** — the proxy
undercounts by exactly the 21 dense-texture events. (OI-215's detail already flagged "it under-counts
uncoverable events, never over-counts"; this quantifies the undercount and names its cause.)

**Consequence (#3, #6/#7):** the OI-215 fix cannot be designed for the member-overlap gate alone — a
relaxation of gate 2 for sparse windows would leave all 21 dense-texture `fitBlocked` events (and every
future one) still emptying the decode. The fix is ONE design at the candidate-admission layer covering
BOTH gates (and giving admission its first ratified basis, §2.1 / OI-226). Declared to Cowork; the
sibling is rowed (OI-227) so the decision surface enumerates the whole family before designing.

### 3.2 Admission filter split + onset-diversity distribution

Aggregate over every examined window (`scanCoverage`, comprehensive — all windows, all pieces).

**(A) fit corpus (326 pieces):** windows 104,836; `(key,class)` offered 66,675,696; admitted 15,260,781.
Rejections by gate: **root-present 37,826,347** (57 % of offered — the dominant filter), **member-overlap
6,697,032** (10 %), **fit / NCT-budget 6,891,536** (10 %), **mem-invalid 0** (never fires). Onset-diversity
histogram (windows by distinct onset pcs, 0…12): `[428, 7246, 5493, 17531, 18074, 20312, 20074, 13307,
2101, 223, 42, 4, 1]` — concentrated at **3–6 pcs** (peak at 5), the `0–1` buckets a small 7.3 % tail.
Prediction P4(A) confirmed.

**(B) large scores (23):** windows 690,306; offered 475,757,044; admitted 82,728,123. Rejections by
gate: **root-present 317,160,414** (67 %), **member-overlap 57,331,400** (12 %), **fit / NCT-budget
18,537,107** (3.9 %), **mem-invalid 0**. Onset-diversity histogram (0…12): `[2847, 84170, 100690,
162459, 141499, 105785, 64161, 23725, 3567, 906, 300, 154, 43]`. **Two tails, both bigger than (A):** the
`<2 onset pcs` sparse tail is **12.6 %** (87,017 windows, vs 7.3 % on (A) — the member-overlap fuel); and
the DENSE tail (nOnset ≥ 10) is 497 windows (300 + 154 + 43) vs (A)'s 47 — an order of magnitude more of
the very-dense windows that feed the FIT-gate sibling. **Both extremes of the density spectrum are far
better populated on the orchestral corpus than on the chorale fit corpus** — the structural reason the
fit corpus sees neither failure. Predictions P4(B) confirmed (bigger sparse tail) AND the dense tail is
the P1d surprise (below).

### 3.3 Dead-branch sets per population — the headline difference

A branch dead on one population and live on the other is the structural shape of OI-215.

**(A) fit corpus — DEAD (0 fires):** `rejMemInvalid`, **`dpEmpty`**, `trContentNegInf`, `trNoBack`.
LIVE: `rejRootPresent`, `rejMemberOverlap`, `rejFit`, `dpComplete` (60/60), `trInitial` (30,442),
`trSameKey` (828,685), `trKeyChange` (1,817,706), `stInsert` (1,496,793), `stImprove` (996,530); segments
2,375 over 60 pieces. (`trKeyChange > trSameKey` is a per-DP-STATE-construction count — most target-key
states take their best-in from a key-CHANGE predecessor since only one of the ≤7 candidate keys is the
state's own; it is NOT a committed-modulation count, and the backtracked path stays in-key. A fire-
structure observation, not an inference concern.)

**(B) large scores (the 4 decoded ≤ 2000 events: brandenburg4 + dvorak_cello II complete; butterworth +
holst_mercury empty) — DEAD (0):** `rejMemInvalid`, `trContentNegInf`, `trNoBack`. LIVE: **`dpEmpty` = 2**
(butterworth, holst_mercury), `dpComplete` = 2, segments 1,129, `trInitial` 1,780, `trSameKey` 689,174,
`trKeyChange` 1,432,958, `stInsert` 1,070,285, `stImprove` 850,934, and the admission gates.

**★ The headline dead-branch DIFFERENCE, confirmed: `dpEmpty` is DEAD on (A) (0/326) and LIVE on (B)
(2/4 decoded, 13/23 theorem-guaranteed).** The empty-analysis branch — the OI-215 outcome — never fires
on the chorale fit corpus and fires on the majority of the orchestral set; the exact structural shape the
dispatch hunts. **The other three ({`rejMemInvalid`, `trContentNegInf`, `trNoBack`}) are dead on BOTH
populations** — genuinely dead/defensive branches (the L4 `SymmetricRotation`-0/29080 shape): `rejMemInvalid`
(no class is unmappable in any candidate key — texture-independent) never fires anywhere; `trContentNegInf`
never fires because `candidateStates` already excludes every −∞-content class before the DP; `trNoBack`
never fires because the DP short-circuits unreachable boundaries (`if (!V[i].hasStart && V[i].states.empty())
continue`, `jointdecoder.cpp:735`) — so even the two EMPTY decodes never reach a candidate with no
predecessor (they simply stop extending past the uncoverable event). Mechanistically confirmed, not
sample-limited.

### 3.4 Predictions (#17b) — checked against outcome

| band | prediction | outcome |
|---|---|---|
| P1a — (A) uncoverable | 0/326 pieces incomplete | **HIT** — 0 uncoverable, 326/326 complete |
| P2 — (A) dead branches | `dpEmpty` dead; `rejMemInvalid`/`trContentNegInf`/`trNoBack` uncertain-possibly-dead; rest live | **HIT** — dead set = {`rejMemInvalid`, `dpEmpty`, `trContentNegInf`, `trNoBack`}, exactly the predicted-or-flagged set |
| P4(A) — onset diversity | concentrated 2–6, `0–1` near zero | **HIT** — peak at 5, `0–1` = 7.3 % tail |
| P1b — pure dominates ≥ 90 % | 291/312 = 93.3 % | **HIT** |
| P1c — memberOverlapRich 0–10 % | 0 | **HIT** (0 %) |
| **P1d — fitBlocked ≈ 0 (flagged uncertain)** | **21 (6.7 %)** | **MISS — and the important one.** I predicted ≈ 0 "with genuine uncertainty," flagging this as the band most likely to surprise. It did: a real gate-3 sibling exists. This is exactly the #17b guard working — the pre-registered doubt is where the finding landed |
| P1e — rootOnly ≈ 0 | 0 | **HIT** (gate 1 never solely blocks) |
| P3 — `dpEmpty` LIVE on (B) | 2/4 decoded, 13/23 theorem | **HIT** |
| P4(B) — nonzero `0–1` tail on (B) | 12.6 % (vs 7.3 % on A) | **HIT** (+ the dense tail, unpredicted, is the P1d cause) |

**Net:** 6 of 7 checkable bands HIT; the one MISS (P1d) is the scientifically decisive one and was the
pre-flagged uncertain band — the pre-registration did its job (OI-219 discharged for this dispatch).

### 3.5 The plain answer: IS OI-215 ALONE?

**NO.** The empty-decode family has **two** candidate-admission failure gates, both measured on the
23-score orchestral corpus (172,611 events, 312 uncoverable events, 13/23 scores decoding empty):

1. **The member-overlap gate on SPARSE windows (OI-215) — 291 events (93.3 %).** An event whose every
   ≤ segCap covering window has < 2 distinct onset pcs (`present < min(2,|members|)` rejects every
   class). Texture: sustained / unison / solo-over-held. The known cliff.
2. **The FIT / NCT-budget gate on DENSE windows (the SIBLING, new — OI-227) — 21 events (6.7 %).** An
   event whose every covering window is so dense (`nOnset` large) that no 3–4-member chord fits within
   the budget `max(1, j−i) ≤ 4` (`(nOnset − present) > budget` rejects every class that cleared gates
   1&2). Texture: chromatic tutti (Holst Planets 14, Tchaikovsky 5, Beethoven 9 ×2). Invisible to
   OI-215's `<2-onset-pc` proxy — the true uncoverable count is 312, not the proxy's 291.

No third gate participates: `rootOnly = 0` (gate 1 never solely blocks), `memberOverlapRich = 0` (gate 2
fires only on its < 2-pc theorem case). The onset-density spectrum has a failure at BOTH ends and a safe
middle (the chorale band 3–6 pcs). **Because the two failures are governed by different gates at opposite
density extremes, no single-gate fix covers the family** — which is precisely the enumeration #3 requires
before the OI-215 decision surface is designed. Both are declared to Cowork; neither is fixed here.

**Caveat (declared, scoped).** `scanCoverage` uses the production `candidateStates`, which includes the
top-6 key prune (OI-226). So the 21 `fitBlocked` events are uncoverable *in production*; whether the full
24-key set (unpruned) would recover any of them — isolating the key prune as a THIRD contributor — is a
follow-up probe not run here (it needs a 24-key `candidateStates` variant). It does not change the answer
(these 21 empty the decode as shipped), but the key prune remains a candidate-admission mechanism whose
independent coverage contribution is unmeasured (a named follow-up, feeding the OI-215/OI-226 decision).

## 4. Task 3 — the annotated dispositions (evidence columns, beside the frozen CSV)

The frozen `tools/audit/oi199/pass1_dispositions_joint.csv` is **not rewritten** (#10/#12). A separate
artifact `pass1_dispositions_joint_annotations.csv` (generated by `gen_joint_disposition_annotations.py`,
reproducible) adds the two evidence columns the certified L4 decoder rows carried and the pass-1 joint
rows lacked:

- **`fire_route`** — which Task-1 fire-count characterization exercises each row's mechanism. Tally over
  the 1,069 rows: `decode:candidate-admission` 3, `decode:DP` 99, `decode:content-posterior` 10,
  `fact-adapter` 104, `record-assembly` 80, `route-A:tests` 347, `n/a:structural` 426. So every decoder
  row is linked to the `candidateStates`/`decodePiece` counters (§3), every fact-adapter row to
  `buildAdapterFacts`, and the rest to the 78/78 route-A suite — the evidence link pass 1's bare verdicts
  lacked, which pass 2's sampler needs.
- **`in_param_manifest`** — whether the row's symbol is registered in `tools/param_manifest.json` (the
  fit-surface inventory). **0 of 1,069** — the joint module's constants are entirely absent from the
  manifest. This is the joint twin of the L4 decoder's OI-103 manifest-coverage gap: the two decode
  hyperparameters (`seg_cap = 4`, `kKeyPruneTopK = 6` — the 2 UNFIT literals of pass-1 §3) and every
  fitted value are outside the fit-surface page. (The joint fitted values ARE externalized to the
  generated embedded artifacts and byte-established there — pass-1 §7 "constant-clean" — so this is a
  fit-surface *inventory* gap, not an un-established-constant gap.)

## 5. Task 4 — revert, byte-identity, suites

- **Instrument commit (for a one-cherry-pick re-add, per OI-110): `a5d10a328d`.** The counters are
  reverted in their own final commit (`git checkout b14a523112 -- <the 3 files>`); **`git diff
  b14a523112 -- src/` is EMPTY after the revert (byte-identity proof).**
- Suites after revert (built from the b14a523112-identical `src/`): composing `_[n]_`, notation `_[n]_`,
  pipeline-snapshot goldens `_[n]_` — GREEN (see the revert commit message).
- Register: **OI-224** (the two arms under-delivered at pass 1 — method finding on OI-199), **OI-225**
  (correction of record — the dispositions were not "generated not made"/void; the verdict-entropy guard
  withdrawn), **OI-226** (candidate admission has no ratified basis — the Task-2 finding, feeds OI-215's
  fix + OI-207). Dated notes on OI-215 (the family answer), OI-199, OI-188/OI-207 (cross-refs). STATUS
  entry carries a POINTER, not the findings' content (the OI-222 remedy).

## 6. Self-check (CLAUDE.md — run over the actual diff before reporting done)

- **#8 / auditor-not-amender:** no fix, no design, no behaviour change, no constant tuned. The only
  `src/` change is the DEFAULT-OFF instrument (guarded counters + the `scanCoverage` helper), reverted at
  close; the harness is DISABLED test-layer drivers. ✓
- **#6 (one path):** the coverage decomposition + the aggregate counters both read the ONE real
  `candidateStates` gate logic (no re-implementation); the harness reuses the existing large-score
  driver pattern. ✓
- **#15/#19 (verify at objects; establish):** the "is OI-215 alone" verdict is measured at the real
  decoder over both corpora, not asserted; the admission-basis finding is verified at the ratified docs
  AND the code; byte-identity proven (78/78 + goldens + the empty `git diff`). ✓
- **#16 / #17b:** artifacts are generated (never hand-typed); prediction bands pre-registered before the
  run (`task1_predictions.md`) and checked in §3.4. ✓
- **#10/#12:** the frozen dispositions CSV is annotated beside, never rewritten; the superseded columns
  and the pass-1 verdicts stand. ✓
- **#13 (a surprise is a STOP):** _[any anomaly in (B) is diagnosed here, not built around]._
- **Conventions:** no self-invented labels — verdict/route vocabulary follows the L4 precedent
  (`fire_route`/`in_param_manifest`); counter names describe the code branches they count. ✓
- **VS Code bash rules:** `; echo "exit:$?"` on fallible commands; large output redirected. ✓
