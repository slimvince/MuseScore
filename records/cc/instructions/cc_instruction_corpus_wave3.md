# CC INSTRUCTION — Corpus Wave 3: full-needs acquisition + inventory (user-disposed scope, 2026-07-04)

**Status: ACTIVE DISPATCH (the only open instruction). Tools/registry/census work only — NOTHING under
`src/`, no code changes anywhere (not even `tools/*.py`), nothing touches inference, the frozen gate corpus
stays byte-untouched. This wave is clone + hash-pin + inventory + bookkeeping, exactly the Wave-2 shape,
scaled up.**

**Why this scope (user directive, verbatim intent):** best precise inference, no information loss, use ALL
available data and scores for statistics/proof, no surprises during iterations, fact- and theory-based
development. Concretely: acquire every ground-truth bed the FULL-NEEDS AUDIT found useful, inventory what we
already hold but never walked, and record everything against the full needs-vector — but change no code and
run no analysis in this wave.

## Mandatory reads BEFORE any work

1. `CLAUDE.md` — bash rules (`; echo "exit:$?"`, no large output), the gate = the 53/24/53 **case-identity
   sets**. You should not need a build.
2. `STATUS.md` header + session 22k (the audit + rulings this wave executes) + `BUILD_AND_TEST.md`.
3. `docs/score_inventory.md` + `tools/REPRODUCIBILITY.md` + `cc_corpus_wave1_report.md` +
   `cc_corpus_wave2_report.md` — the established clone/hash-pin mechanism + registry-v2 conventions.
4. `cowork_score_census.md` §3 (inclusion criteria), §4 (overlap/dedupe-by-work rule), §5 (tiers),
   **§8c (the needs-vector N1–N20 — freshly updated; every row you add is scored against ALL of it)**.
5. `cowork_census_full_needs_audit.md` — the audit whose disposition this wave executes (§2 has the per-row
   scoring; §5 the ranking; §6 the disposed surface).

## Standing rules that bind every task below

- **Intake rule (census §8c):** every acquired/inventoried item gets a **needs-coverage note scored against
  the FULL vector N1–N20** in its registry entry — never single-purpose-tagged; every GT LAYER of a
  container is inventoried, not just the layer that motivated the find.
- **License:** record the actual license class per source; NC/unclear → hash-pin-only, gitignored, never
  committed (the established mechanism). A license that forbids even local mirroring → skip + record.
- **Verify paper claims at the cloned data** (Wave-2 pattern): report match or mismatch, never silently
  accept.
- **Dedupe by work, not container** (census §4): the new jazz/pop sets overlap ChoCo heavily (CoCoPops
  absorbs Billboard/RS200; EWLD ⊃ OpenEWLD; the Jazz Corpus is itself a ChoCo partition) — record the
  overlaps explicitly in the registry notes.
- **Held-out discipline:** every new bed enters held-out; nothing is ever tuned against it.
- **Per-source failure is a report line, not a wave failure:** if one source is unavailable/moved/gated,
  record precisely what happened and what access would require, and continue with the rest. STOP only on
  the global STOP conditions at the end.

## Task 1 — jazz/pop analysis GT (needs N3, N12)

1. **CoCoPops** (`github.com/Computational-Cognitive-Musicology-Lab/CoCoPops`): clone + pin. Verify: ~414
   transcriptions, Humdrum `**harm` RN + `**kern` melody, fully symbolic. The top N3 acquisition.
2. **OpenEWLD** (`github.com/00sapo/OpenEWLD`): clone + pin (~502 PD MusicXML lead sheets — the committable
   subset; still hash-pin like everything else). **EWLD** (Zenodo 1476555, ~5,000): pin if mechanically
   feasible (research-only license → hash-pin-only); otherwise record the access path.
3. **HookTheory / HLSD full set:** the registry already pins a sample (`wayne391/lead-sheet-dataset`) and
   notes the full set "pending HF m-a-p/HookTheory access". Attempt the full research release; if gated,
   record exactly what access requires and keep the sample entry as-is.
4. **Jazz Corpus (Granroth-Wilding & Steedman, 76 pieces, harmonic-FUNCTION analyses):** we already hold it
   as a ChoCo partition — inventory that slice from the pinned ChoCo clone (count, GT layers); attempt the
   native source; record either way. Rare jazz *function* GT — score it against N3 in the registry.
5. **Weimar Jazz Database native** (`jazzomat.hfm-weimar.de`, SQLite): NOT a git repo — apply the
   pinnable-source rule (download + hash-pin the exact artifact with recorded URL/version; if no stable
   artifact exists, record options and move on). Its native phrase + form layers (beyond the ChoCo chord
   slice) are the point: score against N3, N4, N16.

## Task 2 — cadence / dual-annotator / form beds (needs N2, N4, N5, N16, N18)

1. **Sears Haydn quartet cadences** (Zenodo, Sears et al. 2018): locate the actual deposit; clone/pin.
   Verify: ~270 cadence tokens / 50 expositions, TWO annotators, plus key/modulation/**pivot** annotations.
   Score against N2 + N4 + N5.
2. **algomus Mozart string quartets** (sonata-form + cadences, ~32 mvts / 2,000+ labels): locate the repo
   from `algomus.fr/data` (the Wave-2 texture bed came from the same org's GitLab). Score against N4 +
   **N16 (this is the ratified best form/section-GT candidate)**.
3. **algomus Bach fugues** (WTC-I 24 + Shostakovich 12; subjects, countersubjects, cadences, pedals):
   locate + clone/pin. Score against N4 + **N18 (fugue/imitation GT — adopted 2026-07-04)** + N20 (its
   pedal labels).

## Task 3 — figured bass (need N10)

1. **BCFB — Bach Chorales Figured Bass** (ISMIR 2020; 139 chorales, MusicXML/kern/MEI): locate the repo,
   clone + pin. This is the gate repertoire's own composer-stated harmony evidence — verify the 139 count
   and the encodings at the data.
2. **DCMLab/figured-bass** (`github.com/DCMLab/figured-bass`, census §7 residual): clone + pin + WALK it —
   report what it actually contains (the census never inspected it), then promote its census row §7→§1
   with the findings.
3. Registry note only (no code): the DLC harmonies TSVs carry a `figbass` column on every held corpus
   (audit-verified) — record it in the two repos' needs-coverage notes as the third N10 source; the parser
   exposure is a SEPARATE queued increment, not this wave.

## Task 4 — trees / reduction / streams (needs N11, N9)

1. **Kirlin Schenker41** (ISMIR 2014, 41 excerpts, machine-readable Schenkerian MOP reductions): locate
   (paper artifact/author page), pin per the pinnable-source rule. The common-practice counterpart to the
   JHT trees — score against N11.
2. **GTTM database** (Hamanaka, gttm.jp; 300 melodies with grouping/metrical/time-span trees): likely not
   git — pinnable-source rule; if no stable artifact, record options and move on. Score against N6 + N4 +
   N11(melodic).
3. **protovoice-annotations** (`github.com/DCMLab/protovoice-annotations`): clone + pin + **INSPECT and
   report contents precisely** — piece count, annotation format, what a proto-voice derivation contains,
   score alignment. This inspection GATES the Cowork-side N9 (stream GT) search: the report's verdict is
   "usable as stream/voice-separation GT: yes/no/partially, because X". Do not build anything against it.

## Task 5 — When-in-Rome interior inventory (needs N2, N5 — exposure, NO new clone)

Against the ALREADY-PINNED WiR clone (registry `when_in_rome`, pinned commit in the registry):
- Verify presence + per-slice piece counts for: **TAVERN** (incl. the dual `analysis.txt`/`analysis_B.txt`
  file pairs — count them), **KMT**, **BPS-FH**, **HaydnSun op.20**, the WTC-I preludes, the OpenScore
  Lieder RN subset.
- Record each as a registry sub-entry or per-slice needs-coverage note (smallest additive schema change if
  needed, Wave-2 precedent), scored against the vector (TAVERN → N1+N2+N4; KMT → N5; BPS-FH → N1+N4; …).
- Count the Tymoczko-vs-DCML dual-annotation overlap (works with BOTH a Tymoczko and a DCML analysis, by
  the census §4 (composer, work, movement) key) — the N2 pre-coverage number the audit could not compute.
- **Read-only:** no reorganization, no parsing changes, no re-pinning.

## Task 6 — plain-score stress material (Tier S; no GT)

1. **OpenScore Lieder** (`github.com/OpenScore/Lieder`, CC0) + **OpenScore StringQuartets**: clone + pin.
   Verify the v3 1,300+ / 100+ counts at the data.
2. **ASAP** (`github.com/fosfrancesco/asap-dataset`): clone + pin (222 MusicXML romantic piano scores; the
   performance MIDIs ride along but are not our material — say so in the note).
3. **craigsapp closure (enumeration only, CLONE NOTHING):** fetch the `humdrum-tools/humdrum-data`
   manifest, record the complete repo list in the census (closing the census's named mechanical partial).
   Acquisition of individual kern sets is NOT this wave.

## Task 7 — census + registry bookkeeping

- Registry: one v2 entry per acquired/inventoried item, with tier / license / alignment / split=held-out /
  pinned commit + the **full-vector needs-coverage note** (the intake rule). Deterministic regeneration via
  the established generator; smallest additive schema change if a field is missing, documented.
- Census `cowork_score_census.md`: BCFB row added; `figured-bass` promoted §7→§1 with the walk's findings;
  a one-line note at the §1b JHT row that its `syntax-tree` GT layer is registry-recorded (N11); each new
  row marked "entered at Wave 3, provenance this report". Registry `_notes` note 27: append the clarifying
  clause that the TSV `form` column is DCML chord-morphology, NOT form/section GT (audit-verified).
- Do not otherwise rewrite the census.

## Task 8 — the idiom re-discovery trigger check (check, NOT run)

The trigger fires on a material change to the discovery-input corpora. This wave adds substantial NEW
chord-symbol mass (CoCoPops, OpenEWLD/EWLD, HookTheory if obtained) — **expected: FIRED.** State the answer
explicitly with reasoning per corpus (which discovery view each new corpus enters, if any). If fired:
**RECORD ONLY** — the re-discovery run is its own protocol and its own future dispatch; do not run any part
of it inside this wave.

## Acceptance (ALL required)

1. Every Task 1–6 source either cloned+pinned+inventoried+claim-verified OR precisely recorded as
   unavailable/gated with what access requires. No silent omissions.
2. Registry + census updated per Task 7; regeneration deterministic; every entry carries the full-vector
   needs-coverage note.
3. **No-contamination proof:** nothing under `src/`, no code changes anywhere; the frozen gate corpus
   byte-untouched; end-of-run gate reproduction **53/24/53 case-identity sets, set-diff empty both
   directions, all three presets**.
4. Held-out discipline stated per entry.
5. **Reuse-vs-new + what retires** (expected: reuses the clone/pin/registry machinery verbatim; new = the
   entries + any minimal additive schema field; retires nothing).
6. Report `cc_corpus_wave3_report.md` (force-added per the `/cc_*.md` convention): per-source results, the
   Task-4.3 protovoice verdict, the Task-5 WiR inventory incl. the dual-annotation overlap count, the
   Task-8 trigger answer, **commit SHAs mandatory** (self-SHA circularity handled per the 22j/D-L3a
   precedent: the report commit cites the prior commits' SHAs).
7. **The `docs(cowork):` fold rider — exactly this list, surfacing (not including) anything else dirty:**
   `STATUS.md` (the 22k entry), `cowork_handoff.md` (header), `cowork_score_census.md` (the §8c
   vector/state updates), `cowork_census_full_needs_audit.md` (new), plus force-added instruction records
   `cc_instruction_dl3a_closeout.md` and `cc_instruction_corpus_wave3.md`.
8. Commits local/unpushed, **fork-only** (never `upstream`). Suggested split: clones+pins (possibly several
   by task group) / registry+census / the fold / the report.

## STOP conditions (global — per-source failures are report lines, not STOPs)

Anything would touch `src/` or change any code; the frozen gate corpus would change; the gate sandwich
fails; a license situation is genuinely ambiguous about even LOCAL mirroring (surface, don't guess); the
Task-8 check would require running any discovery/analysis to answer; the registry regeneration stops being
deterministic.
