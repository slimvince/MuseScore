# CC INSTRUCTION — L1/L2 Certification Audit, PASS 1 (blind enumerative) — EG-7 / OI-84

> **Issued by Cowork, 2026-07-10 (session 36).** The first layer audit of the EG-7
> dependency-ordered certification plan. **Governing docs, READ FIRST, in order:**
> `CLAUDE.md` (principles #1–#19 + the fact-publication corollary + the open-items register
> rules), `OPEN_ITEMS.md` (session-start read, mandatory), `cowork_audit_protocol.md`
> (P1–P8 — this instruction executes P1–P4 of PASS 1), `cowork_l1_l5_premise_debt_audit.md`
> (context), `BUILD_AND_TEST.md`, `STATUS.md`. **Fork-only; NEVER push `upstream`
> (`cfc7eb5e39` HARD STOP). Bash: append `; echo "exit:$?"`; redirect large output to files.**
>
> **⚠ BLINDING (protocol P8): do NOT read `DEFECT_TYPES.md`, `cowork_siloed_facts_audit.md`,
> or `cowork_adjudication_dossier.md` until your Pass-1 artifact is FROZEN** (written,
> hashed, committed). Pass 1 must enumerate without the known-problem catalog anchoring it.
> You must DECLARE in the report, on your honor as a process step, at which point you first
> opened those files. This instruction deliberately names NO suspects for L1/L2.
>
> **Scope declaration:** READ-ONLY fact-finding (explorational — surprises are findings, not
> STOPs, except in your own tooling). **NO fixes of any kind (#8): a discovered violation —
> even an obvious bug — becomes a register row, NEVER a patch.** No production behavior
> change; no constant tuned; no golden refresh; `tools/robust_stop/` and `tools/corpus/`
> untouched. **This is PASS 1 of 2 — certification is NOT granted here.** Pass 2 (the
> signature sweep + the P5/P6 sampling) is a separate instruction to a fresh session.

## Task 0 — Preconditions

1. `git log --oneline -1` must show HEAD at or after `52cc701a6d`. Working tree dirty beyond
   your own work → STOP and report (known carry: the foreign
   `cowork_joint_key_chord_design.md` banner edit, OI-51 — leave untouched).
2. Read `OPEN_ITEMS.md` in full. Read `cowork_audit_protocol.md` in full.

## Task 1 — The machine-generated inventory (protocol P1; #17(f) applied to scope)

Write `tools/audit/gen_inventory.py` (a new, committed instrument) that mechanically produces,
for the ENTIRE `src/composing/` tree — no hand-chosen file list:

1. **File table:** every file, tagged by you afterward as `L1`, `L2`, `L3+` (out of this
   audit's scope — deferred to its own layer audit), or `RETIRES` (per the roadmap retirement
   map R1–R9), each tag WITH a one-line reason. A file with no tag is an error — the script
   must fail if any file lacks a disposition. The L1/L2 definition comes from
   `ARCHITECTURE.md` + the roadmap layer definitions (read them; do not guess): L1 = the fact
   layer (raw-score interpretation: note model, eligibility, metric weights, spelling view,
   engraving bridge readers), L2 = segmentation (change-point slicing and any other
   segmenter). Where a file mixes layers, tag it with BOTH and note the split.
2. **For every `L1`/`L2`-tagged file:** the complete row lists — (a) functions/methods;
   (b) numeric literals (excluding trivial 0/1 loop indices — the exclusion rule must be IN
   the script, not applied by eye); (c) struct/class fields on any type visible outside the
   file; (d) branches (`if`/`switch` arms) in non-trivial functions; (e) cross-layer calls
   (any call into another layer's headers).
3. **Stamp** `tools/audit/l1l2/manifest.json`: HEAD commit, script commit, corpus hash
   `c50002fee1`, row counts per table. Artifacts as CSV/JSON under `tools/audit/l1l2/`.

Commit the script + artifacts as one `feat(tools):` (revertible, #14). The inventory is the
audit's domain: **Pass 1 is complete only when EVERY row has a disposition.**

## Task 2 — Pass-1 dispositions (protocol P2 + P3)

For every inventory row, record a verdict from the CLOSED set — "no issue" is a recorded
claim with a stated reason, never a blank:

- **Causal premises** (any code whose correctness rests on a claim about music, scores, or
  our own system): FACT (citation) / THEORY (citation) / **ASSUMPTION** (flag → register row).
- **Derived facts** (anything computed that a consumer could want): PUBLISHED / SILOED /
  TRAPPED / DUPLICATED — apply the ratified fact-publication corollary: a fact consumed by no
  one is *declared dormancy* (future consumer named) or *waste* (flag it).
- **Numeric literals/constants:** ESTABLISHED (fit/derivation provenance) / UNFIT (hand-set)
  / DEAD (no effect) — and whether it appears in `tools/param_manifest.json` (EG-5 feeds on
  the gaps you find).
- **Code:** RETIRES (R1–R9, with the #12 interpretation-check note: what embedded
  interpretation must be consciously kept/rejected at deletion) / SURVIVES.
- Per row, the SAME four questions (P2): what does it assume? what does it publish? who
  consumes it? what happens at its edges (empty input, ties, tuplets, grace notes, pickup,
  overlapping voices, zero-length)?

**P3 — the negative-space direction, mandatory:** from the L1/L2 CONTRACTS (what
`ARCHITECTURE.md`/the roadmap say these layers deliver to the layers above), enumerate every
expected output/behavior and locate it in the code — or flag the absence. Absences are
findings of the same rank as positives.

## Task 3 — Behavioral characterization (protocol P4)

For every L1/L2 mechanism/branch in the inventory, measure its FIRE RATE on the pinned corpus
(`c50002fee1`, Baroque preset unless a mechanism is preset-gated). Route: least-invasive
first — (a) many L1/L2 behaviors are countable from existing dumps or by a standalone script
replaying scores through the public API; (b) where only instrumentation can count, a minimal
default-OFF counter flag is permitted as a separate revertible `feat` (production
byte-identity re-proven: standard corpus regen 0-diff + both suites green, NO golden
refresh); (c) where even that is disproportionate, the row is marked **"fire-rate NOT
measured"** with the reason — flagged, never silently skipped. Report per row: fire count,
population, and whether the rate matches the mechanism's documented intent (a mechanism that
never fires, always fires, or wildly misses its intended population is a finding — DT-open,
see Task 4).

## Task 4 — Freeze, then promote (protocol P8 step 1→2 boundary)

1. **FREEZE Pass 1:** write the full disposition artifact
   (`tools/audit/l1l2/pass1_dispositions.{csv,json}`) + the report draft; commit; record the
   commit hash in the report. THIS is the blinding boundary.
2. Only now read `DEFECT_TYPES.md`. Any NEW problem TYPE your pass-1 findings imply (a
   pattern, not an instance) is PROMOTED: a new DT row in `DEFECT_TYPES.md`, same commit as
   the report (the same-commit rule). Do NOT run the pass-2 signature sweep — that is the
   next instruction, for a fresh session.

## Task 5 — Report + fold

`cc_l1l2_audit_pass1_report.md`: the inventory sizes + manifest; the disposition summary
(counts per verdict class); EVERY flagged row (ASSUMPTION / SILOED / TRAPPED / DUPLICATED /
UNFIT-not-in-manifest / never-fires / contract-absence) with file:line and one plain-language
sentence each — write for a reader who does not know the code; the blinding declaration; the
fire-rate table; the RETIRES list with its #12 interpretation-check notes. **Register
discipline: every discovered issue gets an `OPEN_ITEMS.md` row (next free OI-number) in the
SAME commit as the report; new types get DT rows.** Update `STATUS.md` (prepend to the
Last-updated block) and the `cowork_handoff.md` entry block per convention. Commits: the
Task-1 `feat(tools)` (+ optional Task-3 counter `feat`), then one `docs(cc):` fold. Fork-only
push or leave unpushed; `upstream` untouched.

## Standing constraints (mandatory)

- NO fixes, no matter how obvious (#8) — rows, not patches. If you believe something is a
  live correctness bug, say so IN THE ROW, loudly, and move on.
- Both suites green after any `feat`; byte-identity proven for any instrumentation.
- Never guess a file's layer or a constant's provenance — verify at objects (#15) or mark
  UNKNOWN with what would settle it.
- Wall-clock/timing fields excluded from any byte-identity comparison (the EG-2 precedent).
- Any surprise in your own tooling (script bugs, inventory gaps) is a STOP (#13) — fix the
  instrument, restamp, rerun; never hand-edit an artifact (#17(f)).
