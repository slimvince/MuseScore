# CC instruction — E0: the dormant FULL-SPINE pre-engage measurement (harness build + measure, byte-identical)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Also read for this task: `cowork_engage_criteria.md` (§2 G2, §3 E0 — the ratified spec this instruction executes),
> `cowork_confidence_contract.md` (§3/§4 — quote confidences in its terms), `cowork_layer5_function_design.md` §5.5/§7/§8,
> `cowork_layer4_chordsymbol_design.md` §7, and your own `cc_phase5c_stepM_report.md` method (this is Step M's
> successor on the OTHER substrate).
>
> **Dispatch state: READY — intended AFTER the gap-analysis (`cc_instruction_gap_analysis_spec_vs_impl.md`) report is
> ratified** (the gap tables may surface carry-contract gaps this harness would otherwise trip over blindly). The user
> may deliberately parallelize; if so, treat any carry-contract surprise as a STOP, not a workaround.
>
> **Current state:** branch `master`; HEAD has local unpushed commits (quote your `git rev-parse HEAD` in the report).
> Gate baseline: BIR case-identity **53/24/53** (CLAUDE.md sets). Suites: composing 974 / notation 53 (4 skipped) /
> pipeline_snapshot 11/11. **This run: ONE dormant diagnostic harness build (commit allowed, local unpushed, after the
> byte-identity proof) + a READ-ONLY measurement. No production movement, no engage, no tuning, no golden refresh.**
>
> **Bash rules (mandatory):** append `; echo "exit:$?"` to every command; redirect large output to files and `head`
> them. Build via PowerShell `Start-Process`.

## 0. Purpose — what E0 is and is not

E0 measures the **complete dormant chain end-to-end** — L1 note model → L2 `changePointSlices` → L3 decoded keys →
**L4 `ChordSliceDecoder`** → **L5 function units** — against BOTH frozen references: the legacy spine's output and
the DCML/WiR ground truth. Step M graded L5 over the **legacy region substrate**; the L4-decoder substrate is
unmeasured, and the questions that live only there are E0's deliverables (§4). **E0 is a measurement, not a
gate-pass attempt** (engage-criteria §3): wins are banked E2 evidence; every regression class is *named*, not fixed.
No constant may be adjusted in response to a number seen in this run.

## 1. Task A — the chaining harness (the only build)

A new **default-OFF** `batch_analyze` flag (suggested `--dump-fullspine`; your naming call, declare it) that, per
score: builds the L1 note model; runs L2 slicing; takes the **live** L3 decode (the production key path — reuse, do
not re-instantiate a second decoder); runs the **dormant L4 decoder** (`ChordSliceDecoder::decode`) over the slices;
feeds the resulting `SliceChord` stream — including the carried `alternatives`/`SliceConfidence`/`OpenQuestionLabel`
— into the **dormant L5 units** (Step-1..6: progression, base RN, cadence, resolver **with the §5.5 case-4 override
live on this substrate**, tonicization-vs-modulation + recompute, relational labels, output assembly); and writes a
JSON side file per stem: per slice {L4 decision (Commit/Inherit/Abstain), chosen identity, alternatives+confidence,
open question} + {L5 RN, role, open mark, confidence components}, per region {local key, cadence markers}, plus
wall-time. **Reuse over re-implementation everywhere** (the Step-M harness + `cc_stepM_l5_measure.py` are the
models; grading through `compare_rn`/`dcml_parser`/`compare_analyses` — no new comparator). Report reuse-vs-new and
what (if anything) this makes redundant, per the unification rule.

**Byte-identity gate for the harness commit:** flag default OFF; grep-proof no production reach of the new code;
suites green (composing/notation/snapshots — no golden refresh); corpus regen with flag off → `characterise_bir_false`
**53/24/53 exact identity sets** + clean `git status tools/corpus/`. Then ONE commit (`feat(tools): E0 full-spine
measurement harness …`), local, **unpushed**.

## 2. Task B — the measurement (read-only; all three presets; per stem and aggregated)

On the full 353-stem corpus, flag ON (side files only), grade the chain per **`cowork_engage_criteria.md` §3 E0**,
each measure reported vs BOTH references and on the **granularity-robust unit** (`compare_rn --granularity-robust`)
as the primary view (batch-region view as secondary):

1. **Chord root + RN accuracy** — dormant chain vs legacy vs DCML (WiR-Bach 326 denominator explicit).
2. **Key accuracy** — S1/S2 split (`--key-breakdown`) + the de-masking view (`--partial-key-breakdown`).
3. **Modulation** — track-rate + precision vs DCML modulations (the 4d-i method).
4. **Abstention** — rate; **correct-abstention** (open mark where DCML/ambiguity genuinely warrants it) scored
   SEPARATELY from wrong commits; abstention density distribution per stem (the review's F-13 display question needs
   this number).
5. **The two-tier case deltas** — signed class-(b)/class-(a) **identity sets** (stem@tick), not integers, for every
   root the chain moves vs legacy; class-(b) verified per case.
6. **★ The Phase-5b override-duty question (the headline):** of the recorded **86 class-(b) decoder cases (61 Commit /
   25 Inherit)** — how many does the §5.5 case-4 override (+ cascade through Inherit-borrows-corrected-commit)
   correct? Report the residual identity set and whether the evidence says the override must extend to
   confidently-decided = {Commit, Inherit} (the L5 §5.5 Step-M question, now answerable).
7. **Over-trigger families** — the `V/iv`-class (tonic-rooted applied) and the common-tone-`o7` class sizes on THIS
   substrate (Step-M saw 62/29/56 on legacy; D2 says the family is broader — enumerate by target degree).
8. **Wall-time** — per-stem decode time median/p95 vs the legacy path on the same machine (the G3 envelope input).
9. **Confidence readout (contract D-INV corroboration):** the distribution (min/median/max) of each boundary
   confidence actually emitted (L4 composite, L5 combined pre/post any squash) — quoted in the contract's §3 terms.

## 3. Deliverable

`cc_e0_fullspine_report.md` (gitignored, HELD for Cowork): §1 harness (reuse-vs-new, byte-identity proof); §2 the
measurement tables (per preset × per measure, robust-unit primary); §3 the override-duty answer with identity sets;
§4 regression classes NAMED (each: class, size, exemplar stem@tick, which §5.3–§5.5 inference item owns it); §5
better/worse verdict per respect (the engage-criteria G2 pre-read — explicitly NOT a pass/fail claim); §6 Unknowns.
End with the report's line count.

## 4. Stop conditions

- The L5 units require an input the L4-decoder substrate does not carry (a carry-contract gap) → **STOP, report the
  exact missing field** — do not synthesize or default it.
- Any byte-identity proof fails (suites, goldens, corpus sets, `git status`) → STOP.
- Any number tempts a constant change → out of scope, record it in §4 of the report instead.
- Corpus regen not 353/353 or manifest invalid → STOP (standard).

**On your report: Cowork re-reads this instruction, then the report in full, verifies the harness commit via
committed objects and the headline numbers against the dump files, before any E0 conclusion is ratified.**
