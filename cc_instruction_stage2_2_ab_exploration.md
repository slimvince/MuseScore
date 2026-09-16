# CC Instruction: Stage 2.2 (part i) — Batch-parity A/B exploration + re-baseline dossier

## Context

Roadmap **2.2** is the first *deliberate behavior change* of the plan: batch must measure
the user-facing pipeline (section-level), and the parked metric decisions land in ONE
re-baseline event. Because of that, 2.2 ships in two instructions:

- **THIS RUN (2.2-i): exploration + A/B characterization + decision dossier. NO commits
  of behavior changes.** You will implement working-tree prototypes to run the A/B, but
  nothing is committed this run. Every decision the re-baseline needs gets DATA here.
- 2.2-ii (next): Cowork/user pick the package from your dossier; you ship it.

Standing rules (handoff): never guess — investigate or state the unknown; exploration
is explicitly encouraged; CC proposes, Cowork decides.

Mandatory reads: STATUS.md header, roadmap 2.2/2.2a rows, `cc_stage1d_report.md`
(F-1/F-2/F-3), `cc_stage2_1_report.md` (Option D seam, dead shims),
`sectionanalyzer.h` (the API batch will call), `tools/batch_analyze.cpp` (the caller
you'll extend).

**Authorized working-tree changes (uncommitted prototypes):** `tools/batch_analyze.cpp`
(+ its CMake if needed), `tools/*.py`, scratch scripts under `/tmp` or `tools/` (clearly
named, listed in the report). NO changes under `src/` (the Option-D seam should make the
batch call possible without touching composing — if it does NOT, that is a finding to
report, not a thing to fix this run).

---

## Task 1 — Trace the "24" (F-3, small)

Establish what actually produced the BIR=true=24 figure (and 35 for Jazz): grep tools/
+ cc_*/docs history for the producing code path; run the candidate script(s) against the
new per-preset dirs to reproduce 24/35 (or report exactly what they produce instead and
why). Outcome: a one-paragraph provenance statement with [probe] evidence, so STATUS's
"24/13 / 35/7" lines can finally cite their sources precisely.

## Task 2 — Prototype: batch section-level pass (flag, uncommitted)

1. Survey `analyzeSection`'s signature/inputs (post-Option-D) and determine the mapping
   from batch's existing flow (Score + `analyzeRegions` output) to the section call.
   Document what analyzeSection ADDS/CHANGES vs raw regions: which of
   stabilization / sparse-quality refinement / cadence markers / pivot labels / key
   areas can alter the fields that reach `.ours.json` (root, quality, bass, ticks,
   keys) vs which are purely additive annotations.
2. Add `--section-level` to `batch_analyze` (default OFF this run): same `.ours.json`
   schema, fields populated from the post-section regions. Additive annotation types
   (cadences etc.) are NOT emitted this run (schema change is its own decision —
   note it for the dossier).
3. Confirm batch still links/builds cleanly with the call (composing is already
   linked); zero changes when the flag is off (spot-check: one score, flag off, diff
   vs HEAD output → must be byte-identical).

## Task 3 — The A/B (the heart of this run)

For BOTH presets, regenerate side-by-side corpora with the prototype:
`tools/corpus/{baroque,jazz}` (flag off — should equal current baselines; verify) and
`tools/corpus_ab/{baroque,jazz}_section` (flag on). Then:

1. **Counts + identity sets**: BIR=false old vs new per preset (characterise with
   `--corpus-dir`). Also BIR=true per Task 1's producer if available.
2. **Per-case delta table**: every score whose BIR classification changed (either
   direction), with root-pc old/new, what section-level mechanism caused it
   (stabilization? sparse refinement?) — traced, not guessed (re-run the single score
   with targeted dump/debug if needed).
3. **DCML spot-verification**: for EVERY case that newly becomes BIR=false and a
   sample (≥10) of cases that improve, check the DCML ground truth and judge
   right/wrong/ambiguous. The dossier must let us answer: is the section-level
   pipeline *better*, or just *different*?
4. **rn_agree side**: run `compare_rn` Bach-corpus (or the cheapest available aligned
   set) old vs new, current metric definitions — bucket deltas.
5. Region-count / duration sanity: total regions, mean duration old vs new (gross
   distortions would show here first).

## Task 4 — Metric-fix impact sizing (F-1 / F-2, uncommitted prototypes)

1. F-1 (letter-`o` diminished): patch `extract_quality` in the working tree; rerun
   compare_rn on the SAME corpus (old binary outputs) → bucket deltas attributable to
   the metric fix alone. Count corpus occurrences of `o`-diminished tokens on each side.
2. F-2: count Ger65/N6/It6 occurrences in the DCML side; show what each currently
   parses to; propose per-token treatment (fix It6 misparse? leave Ger/N as
   unparseable-fallback?) with the counts to justify.
3. Revert the prototypes after measuring (working tree of tools/*.py back to HEAD —
   the A/B artifacts and numbers go in the report; `git diff` must be clean for
   committed files at the end of the run except the batch prototype, which you keep
   for 2.2-ii and list explicitly).

## Task 5 — Small riders to PROPOSE (not implement): `analyze_inversion_errors.py`
`--corpus-dir`-ification scope; dead weight/pitch-context shim removal (list exact
symbols + proof of no callers); whether cadence/pivot annotations should enter the
`.ours.json` schema now or later.

## Deliverable — `cc_stage2_2_ab_dossier.md`

§1 F-3 provenance. §2 section-level mapping + what can change identities. §3 the A/B:
counts, identity sets, per-case delta table with mechanisms, DCML verdicts, rn deltas,
sanity stats. §4 metric-fix impacts with counts. §5 rider proposals. §6 **the decision
menu**: for each candidate component of the re-baseline package (section-level default,
F-1 fix, F-2 treatment, riders) — recommendation + evidence pointer + what the new
baseline numbers/identity sets would be under each combination you measured (at minimum:
all-on, and section-level-only). §7 unknowns/limits, honestly.

NO commits this run. End state: working tree = HEAD + the batch prototype (listed) +
the dossier + A/B corpus dirs (gitignored). Everything else reverted.

Stop conditions: the Option-D seam doesn't suffice for the batch call (src change
needed); the A/B shows gross distortion (region counts off by >2× class); a flag-off
output differs from HEAD on any score (prototype contamination — must be byte-identical);
anything where proceeding would mean guessing.
