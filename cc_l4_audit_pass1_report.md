# L4 (chord) Certification Audit — PASS 1 (blind enumerative) — Task-1 + FEASIBILITY STOP

> **CC, 2026-07-11.** Executes `cc_instruction_l4_audit_pass1.md` (EG-7 / OI-84), the next
> layer in dependency order after the user-granted L3 certification. Pass 1 of 2, blind
> enumerative (protocol P1–P4). **Read-only fact-finding — no `src/` change, no constant
> tuned, no golden refresh; `tools/robust_stop/` and `tools/corpus/` untouched.**
>
> **★ OUTCOME: the Task-1.4 FEASIBILITY STOP fired.** Task 1 (the machine inventory) is
> complete and frozen; the deep-row count (2,121 rows, ~1,880 genuinely in scope) makes an
> every-row disposition + contract-direction check + fire-rate characterization **infeasible
> to complete rigorously in one session.** Per the instruction ("do NOT silently sample or
> skip; the protocol's totality is the point"), Tasks 2–3 are **NOT attempted this session**;
> this report delivers the inventory, the three-population partition with counts, the Task-1
> findings, and a **proposed partition of the deep audit into sequential sessions** for Cowork
> to draft.

---

## 1. What was done, and the commits

| Task | Done | Commit |
|---|---|---|
| Task 0 — preconditions: commit Cowork's waiting register edit (L3-cert grant) + the instruction file; verify git state | ✅ | `7f57aad4b5` `docs(cowork):` |
| Task 1 — extend `gen_inventory.py` with `--layer l4`; generate `tools/audit/l4/`; manifest; **this is the freeze / blinding boundary** | ✅ | `88befa3055` `feat(tools):` |
| Task 2 — dispositions + contract-direction check | ⛔ **DEFERRED** (feasibility stop) | — |
| Task 3 — fire-rate characterization | ⛔ **DEFERRED** (feasibility stop) | — |
| Task 5 — this report + register + STATUS/handoff | ✅ | this `docs(cc):` fold |

The Task-1 commit `88befa3055` is the **blinding boundary**: every withheld file
(`OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `STATUS.md`, `cowork_handoff.md`) was opened **only after**
it existed. The three-population tagging and every finding below were formed blind (from the
code, the safe reference docs, and one read-only call-site–tracing sub-agent), before any
withheld file was read.

## 2. The machine inventory (protocol P1)

Instrument: `tools/audit/gen_inventory.py`, extended with `--layer l4` (one path per concern,
#6 — the SAME enumeration/extraction that served L1/L2 and L3; `--layer` picks the deep-tag set,
the out-dir, and the L4 tag refinement). Artifacts under `tools/audit/l4/`, manifest-stamped
HEAD `7f57aad4b5…` / corpus `c50002fee1`.

- **216 tracked files**, all tagged (P1 totality — the script exits nonzero on any untagged file).
- **10 deep-audited files** → **2,121 inventory rows**: 136 functions, 1,067 numeric literals,
  612 branches, 262 fields, 22 decls, 22 cross-layer includes.

Per-file extraction (establish-the-instrument cross-check, `--self-check`):

| File | population | fn | lit | br | fld | dcl | x | rows |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| chord/chordanalyzer.cpp | scorer (c) | 39 | 345 | 157 | 0 | 0 | 4 | **545** |
| chord/chordsymbolformatter.cpp | scorer (c) | 17 | 221 | 265 | 0 | 0 | 2 | **505** |
| types/analysistypes.h | mixed | 2 | 251 | 0 | 115 | 0 | 0 | **368** (≈130 L4) |
| chord/chordanalyzer.h | scorer (c) | 15 | 103 | 22 | 82 | 16 | 3 | **241** |
| chord/chordslicedecoder.cpp | decoder (b) | 41 | 51 | 127 | 0 | 0 | 5 | **224** |
| chord/chordslicedecoder.h | decoder (b) | 2 | 21 | 0 | 61 | 0 | 3 | **87** |
| chord/analysisutils.h | scorer (c) | 6 | 41 | 18 | 0 | 4 | 0 | **69** |
| region/sparsechordrefinement.cpp | scorer (c) | 7 | 31 | 23 | 0 | 0 | 2 | **63** |
| decode/chordpathdecoder.h | scorer (c) | 7 | 3 | 0 | 4 | 1 | 1 | **16** |
| region/sparsechordrefinement.h | scorer (c) | 0 | 0 | 0 | 0 | 1 | 2 | **3** |

**Instrument regression (self-check):** the L4 edit is provably inert for the other layers —
regenerating L3 gives **byte-identical** CSVs, and regenerating L1/L2 differs **only in
`note_model.h` line numbers** (the (file,name) sets are identical), i.e. pre-existing source
drift already recorded at **OI-95(b)**, not a tooling change. The extraction engine
(`blank_code`/`extract_functions`/…) was not touched; only the l4 tag table + layer plumbing
were added.

## 3. The three-population partition (the layer-4 wrinkle)

Every tag was **re-verified at the code with call sites traced** (a mis-tag is a finding, not
inherited — the instruction's warning about the inherited file-table). Tag counts: `L4-SCORER`
7, `L4-DECODER` 2, `L4-MIXED` 1, `L4-RETIRES` 2, `DEFERRED` 11 (+ 178 `L3+` / 11 `L1` / 2 `L2` /
2 `RETIRES` non-chord files out of scope).

**(c) LIVE surviving scorer core — `L4-SCORER` (7 files, deep):** the vertical scoring oracle the
dormant decoder REUSES, plus its live in-scope satellites.
- `chord/chordanalyzer.cpp` — `analyzeChord` (the oracle) + templates/score matrices +
  `buildChordResult`/`detectExtensions` + the factory. **Live** (`regionanalyzer.cpp:987`) and
  **reused by the decoder** (`chordslicedecoder.cpp:453`).
- `chord/chordanalyzer.h` — the stable contract surface (`kTemplateCount`, `ChordIdentity`/
  `ChordAnalysisResult`/`RawCandidate`, `IChordAnalyzer`/factory; also declares
  `PostScoringGateContext`/`PromotionTarget` for the retiring gates).
- `chord/chordsymbolformatter.cpp` — the live shared chord-symbol formatter.
- `chord/analysisutils.h` — live cross-cutting pc/key helper header.
- `decode/chordpathdecoder.h` — the live beam-1 commit-chain re-expression (Stage 3.1).
- `region/sparsechordrefinement.{h,cpp}` — the live diatonic chord-quality refinement.

**(b) DORMANT-but-surviving decoder — `L4-DECODER` (2 files, deep):** `chord/chordslicedecoder.{h,cpp}`
— `ChordSliceDecoder`, the engagement's clean target. Not wired; runs only under `batch_analyze
--decode-chords`. It runs `analyzeChord` over each Layer-2 slice and reads the candidate cube
("reuse the one scorer and its cube; do NOT fork a second scorer").

**mixed — `L4-MIXED` (1 file, deep, L4 portion only):** `types/analysistypes.h` — the L4 chord
types (`ChordAnalyzerPreferences`, `ChordAnalysisTone`, `ChordTemporalContext`,
`DecodeQualityLevel`, `ChordQuality`) beside the L3/L5 types already covered by the L3 audit.

**(a) RETIRES at engagement — `L4-RETIRES` (2 files, file-level note only, NO deep rows):**
- `chord/postscoringgates.cpp` — Gates A–L (`applyPostScoringGates`); **literally roadmap R1**.
- `chord/chordpostpasses.cpp` — the legacy late-promotion tail (`applyIter8691Pedal`: Iter-86
  bass-♭7 + Iter-91 bass-as-root + two-pass pedal-point).

**verified NOT Layer 4 — `DEFERRED` (11 files, out of L4 scope):**
- `chord/chordvoicing.cpp` — a chord-tone/voicing utility serving notation Implode + display
  stabilization (arrangement concern), **not** chord decoding.
- `chord/chorddiagnose.cpp` — a diagnostic satellite (`diagnoseChord` replays the pipeline),
  reached only via `--diagnose-measures`; coupled to R1's gates.
- `vocabulary/harmonicvocabulary.{h,cpp}` — the ARCHITECTURE §7 Harmonic Vocabulary, a queried
  reference catalog consumed by the L5 progression/function machinery; DORMANT.
- `voiceleading/*` (7 files) — the voice-leading **axis 2** (VL-A/VL-B/VL-C), orthogonal to the
  harmonic spine; DORMANT.

## 4. Task-1 findings (all map to existing types / rows — no new defect type this session)

Pass-1 **dispositions** (where new defect types normally emerge) are deferred; the findings below
are the **tagging-and-scope** findings that Task 1 itself produces. Each maps to an existing
`DEFECT_TYPES.md` type and, where applicable, an existing register row.

**F-1 — file-table mis-tags (DT-21), sibling of OI-90.** The inherited L1/L2→L3 file-table tags,
re-verified at the code:
- `chord/chordanalyzer.cpp` was tagged **whole-file `RETIRES`**. It is the **surviving vertical
  scoring oracle** the dormant decoder reuses; only the *competition* (`function/`, out of L4
  scope) + Gates A–L retire (R1), and R9 **file-splits** this file — it is not deleted.
  Inheriting `RETIRES` would have given it a file-level note only and **missed deep-auditing the
  surviving scorer core** — exactly the DT-21 "miss a file" failure. **Corrected to `L4-SCORER`.**
- `chord/chordvoicing.cpp` was deferred-to-L4; it is a notation voicing/arrangement helper —
  **not L4.** Corrected to `DEFERRED`.
- `vocabulary/*` carried "(L4)" and `voiceleading/*` carried "(L4/L5)"; both are **not L4** (an
  L5-consumer catalog, and axis 2). Corrected to `DEFERRED`.
- (Confirmed correct: `decode/chordpathdecoder.h` and `region/sparsechordrefinement.*` — the two
  mis-tags OI-90 already fixed at the L3 audit — are indeed L4.)

**F-2 — two live in-scope files with an OPEN population/boundary question (flag, not decided):**
- `region/sparsechordrefinement.{h,cpp}` sits on the **L4/L5 boundary**: it overwrites
  `identity.quality` (an L4 field) from the resolved key (an L5-flavored concern) *post-commit*
  on the region path (`regionanalyzer.cpp:1003/1005`). This is the **DT-4** silent-overwrite
  shape and the **OI-10** quality-from-key-single-owner / **OI-29** §6-block-dissolution
  substance. Whether it is audited under L4 or L5 is a scoping question to settle when its
  session opens; classified `L4-SCORER` (live, in scope) for now with the flag recorded.
- `decode/chordpathdecoder.h` is the live beam-1 commit-chain re-expression; whether it
  **retires** with the legacy path or **survives** as Stage-3.2 wider-beam scaffolding is OPEN.
  Classified `L4-SCORER` (live; default-to-surviving until proven retiring) with the flag.

**F-3 — the retiring-code interpretation-check notes (#12), captured in the file table now:**
- `postscoringgates.cpp` (Gates A–L): Gate J (vii°→V7), Gate L (Major-over-augmented), Gate I
  (first-inversion-Major-over-Minor), the enharmonic Maj-add6↔m7 flip (FM2), and the bias
  correction are the **only site** of several key-function chord reselections — L5 must
  consciously re-home or reject **each** before deletion.
- `chordpostpasses.cpp`: the pedal-point detection + the Iter-86/91 bass-root late promotions are
  legacy-winner corrections the dormant decoder does **not** reuse — confirm the decoder/L5 covers
  or rejects each before deletion.

## 5. Contract-direction (protocol P3) — one spot-check now, the rest deferred

The full spec→code enumeration (from `docs/scoring_model.md`, `ARCHITECTURE.md` §4/§7, the
decoder design) is part of Task 2 and is **deferred**. One cheap invariant was checked now — the
scoring document's own staleness check (§2 "the template count must match the declared
constant"): `chordanalyzer.h` `kTemplateCount = 17`, `scoring_model.md` §2 "currently 17", and
`kTemplateIntervals` has **17** interval rows — **the invariant holds.**

## 6. Fire rates (protocol P4) — deferred, with the route named

Not measured this session. The route per population, for the partitioned sessions:
- **(b) decoder:** zero on the production path by construction (`--decode-chords` returns before
  `analyzeScore`); characterize via `decode_chord_tests.cpp` and the `--decode-chords` diagnostic.
  (The L3 pass-1 already measured the region decoder at 352/352 on `c50002fee1`.)
- **(c) scorer core:** existing diagnostic dumps first (`diagnoseChord`, `batch_analyze
  --dump-regions`); a minimal default-OFF counter only where instrumentation is the only route,
  as its own revertible `feat(tools):` commit with production byte-identity re-proven.

## 7. ★ The feasibility stop and the proposed partition

**Why stop:** ~1,880 in-scope deep rows (excluding the ~240 non-L4 type rows in `analysistypes.h`
and the two file-level retiring files), dominated by dense scoring/formatting logic
(`chordanalyzer.cpp` 545 + `chordsymbolformatter.cpp` 505 + `chordanalyzer.h` 241 = ~1,291
scorer-core rows; decoder 311). Each row needs a verdict + the four standing questions + at-code
verification; on top sit the contract-direction enumeration and the fire-rate instrumentation
(a default-OFF counter + a full-corpus regen for the live scorer). Completing all of that
rigorously in one session is not realistic; attempting it risks either rubber-stamping (forbidden)
or an un-frozen partial pass (worse than a clean partition).

**Proposed partition** (Cowork to draft the per-session instructions; counts are the guide):

| # | session | files | rows | notes |
|---|---|---|---|---|
| **L4-2a** | the DORMANT decoder (b) | `chordslicedecoder.{h,cpp}` | ~311 | the engagement's clean target, "audited as surviving code in full"; contract vs `cowork_layer4_chordsymbol_design.md` + `docs/decoder_design.md`; touches OI-16 / OI-18 / OI-28 / OI-72 / OI-73 / OI-9 |
| **L4-2b** | the surviving scorer-core oracle (c) | `chordanalyzer.cpp` + `chordanalyzer.h` + `analysisutils.h` | ~855 | contract vs `docs/scoring_model.md` (§2/§4/§11 + the template-count sync); the §4 scorer constants → `param_manifest.json` check (OI-87-class); touches OI-17 / OI-23 / OI-30. Fold the two `L4-RETIRES` file-level #12 interpretation-checks here |
| **L4-2c** | live satellites (c) + L4 types | `chordsymbolformatter.cpp` + `chordpathdecoder.h` + `sparsechordrefinement.{h,cpp}` + the L4 rows of `analysistypes.h` | ~717 | resolve F-2 (the sparsechordrefinement L4/L5 boundary — with OI-10/OI-29 — and the chordpathdecoder retire question); the `ChordSliceDecoderPreferences`/`ChordAnalyzerPreferences` constants → manifest (OI-91-class) |

Each is a blind pass-1 disposition session freezing its own dispositions; the **layer's pass-2
signature sweep** (protocol P8, the DT catalog over the whole layer) follows as a separate session,
as it did for L3. The split points and session count are a **proposal** — Cowork owns the
instruction boundaries.

## 8. Register and cross-references (this commit)

- **OI-84** (the master audit plan) — L4 line updated: pass-1 **Task 1 done + feasibility stop**;
  the deep audit partitioned (see OI-102). Certification NOT proposed — the deep work is owed.
- **OI-101 (new)** — the L4 pass-1 file-table mis-tags (F-1 above; DT-21), sibling of OI-90.
- **OI-102 (new)** — the L4 pass-1 **feasibility stop + the proposed partition** (Tasks 2–3 for
  the whole layer owed across ~3 sequential sessions + the pass-2 sweep); carries the F-2
  population/boundary open questions (references OI-10/OI-29).
- References, not duplicated: `note_model.h` line-drift = **OI-95(b)**; the `sparsechordrefinement`
  quality-overwrite substance = **OI-10 / OI-29 / DT-4**; the working-tree concurrent-edit pattern
  = **OI-85 / DT-18** (see §10).
- **DEFECT_TYPES.md — no new type** this session (F-1 = DT-21, F-2 = DT-4). New types emerge from
  dispositions, which are deferred.

## 9. Withheld-file open log (the DT-20 discipline)

All opened **only after** the Task-1 freeze commit `88befa3055`:
`OPEN_ITEMS.md`, `DEFECT_TYPES.md`, `STATUS.md`, `cowork_handoff.md`. During Task 1 the safe
reads were: `CLAUDE.md`, `cowork_audit_protocol.md`, `BUILD_AND_TEST.md`, `ARCHITECTURE.md`,
`docs/implementation_roadmap.md`, `docs/scoring_model.md`, the source code, and the raw
`tools/audit/` inventory tables + `gen_inventory.py`. (No `cc_*_report.md` / `cowork_*.md`
analysis doc was read at any point except the safe references named here.)

## 10. Working-tree disclosures

- **`OPEN_ITEMS.md` carries a pre-existing external edit to rows OI-43/OI-44** (a Cowork/user
  register refinement — sharpening the joint (key,chord) hold to lift "when the FULL
  dependency-ordered audit certification (OI-84, all layers) is complete"). It appeared in the
  working tree during this session, not authored by CC. This is the **known OI-85 / DT-18
  concurrent-edit pattern** (the working tree is live-edited by Cowork; CC stages only its own
  files and appends, never rewrites, shared docs). It is **preserved** (not reverted) and rides
  this `docs(cc)` commit alongside CC's own register rows — disclosed here and in the commit
  message.
- **The committed `tools/audit/l1l2/{l1l2_functions.csv,l1l2_decls.csv,inventory.json}` are
  line-stale** vs current `note_model.h` (substance byte-identical). Already **OI-95(b)**; not
  touched here (re-baselining another audit's frozen reference is out of scope).
- **`cowork_joint_key_chord_design.md`** — the known carry, **OI-51**; left untouched.

## 11. Self-check (against the diff on disk)

- **Principle 8 / 7:** nothing fixed — read-only; every discovered issue is a register row, not a
  patch. **Principle 15 / 19:** every population tag verified at the code + call sites, not at the
  inherited tag; the mis-tags are the proof the re-verification was real.
- **Conventions (no self-invented jargon):** the tag tokens echo the instruction's own population
  names and the existing `L3-MIXED` style; reasons use repository names (`analyzeChord`, Gate
  J/L/I, FM2, `regionanalyzer.cpp:987`, …).
- **#6 (one path):** the L4 inventory is the SAME `gen_inventory.py`, `--layer`-selected — no
  parallel script; proven inert for L1/L2 and L3.
- **#16 (reproducibility):** artifacts manifest-stamped HEAD + corpus + script blob sha.
- **Scope:** no `src/` change, no constant tuned, no golden refresh, both regression references
  untouched. Git: staged only CC's own files, named one by one; `upstream` push confirmed
  disabled.
- **Catalog part of the self-check (post-freeze):** the findings were checked against
  `DEFECT_TYPES.md` after unblinding — F-1→DT-21, F-2→DT-4; no untyped finding.
