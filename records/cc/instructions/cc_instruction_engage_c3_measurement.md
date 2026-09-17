# CC Instruction — Engage arc #2: MEASURE the C3 genuinely-coupled key↔chord population (investigation, read-only-first)

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** The specific, scarce-fact investigation the F-B design pass
> (engage arc #1) called for. Principle-driven and principle-cited throughout — the newly-ratified
> `## Guiding principles` block in `CLAUDE.md` (1–16) is the guide.
>
> **Why this, and why now — from the principles:** the F-B pass hit a genuine surprise (the progression
> contradiction is *uncorrelated with root-correctness*; the theory-first repair is net-negative). Per **#3**
> a surprise means our fact/theory basis is incomplete; per **#5 + #2** the response is *specific research
> where facts are scarce*, not construction. The one unmeasured, scarce fact is the **C3 population** (split
> UNKNOWN, flagged in the F-B design doc §2.5). F-B is **dormant** — nothing is actively harmed or lost
> today — so **#3/#5 govern: close the surprise before any build.** The eventual frame is already fixed by
> **#12 (no information loss) + #6 (total unification) + #7 (layers): annotate via the EXISTING open-mark
> carry, never disable.** This dispatch does **not** build that redesign — **it measures.**
>
> **The C3 trigger (contract §6-C3, verbatim):** a slice where **(a) the L3 key confidence is below its bar
> AND (b) the L4 decision is sensitive to the carried KEY alternatives — a different carried key flips the
> chord reading.** Note (b) is about carried **key** alternatives, NOT F-B's chord-alternative pool
> (`s.alternatives`) — do not conflate them.
>
> **Scope / hard limits:** measurement + investigation only. **No behavior change** (annotate/disable is a
> LATER, separately-ratified build event). The ONLY `src/` change permitted is **additive, default-off,
> byte-identity-proven telemetry** that *surfaces an already-computed signal* (the `bothLicensed` /
> `phraseNumVoices` precedent) — and only if the read-only path (Task 1) proves insufficient. **No new C3
> detector** (that would violate **#6** and pre-build the mechanism, **#8**). No corpus write, no θ retune,
> no push toward `upstream`/`musescore/MuseScore` (the `cfc7eb5e39` distribution HARD STOP).
>
> **Read first (build on knowledge, not assumptions — #1, and the binding grounding rule):**
> `cowork_confidence_contract.md` §6-C3 + §7 D-FS · `cowork_fb_redesign_design.md` §2 / §3.D-2 / §4 · the
> L3 key-confidence source (`HarmonicRegion.keyConfidence`, the D-L3a boundary confidence) + its "bar"
> (the 0.8 annotate gate input, per D-L3a — verify at source, do not assume the value) · the carried
> **key** alternative source in the decode/region path · the existing `C:/tmp/c1/fs_*` E0 dump schema + the
> §2 taxonomy scripts (`fb_taxonomy.py`, `fb_vertical.py`, `theta_fit.collect_fb_fires`).
>
> **Current state:** HEAD `712830210a`, branch `master`, fork-only, **ahead 0** (backlog pushed).
> **Uncommitted Cowork edit in the tree:** the `## Guiding principles` section at the top of `CLAUDE.md`
> (ratified 2026-07-06) — **fold it into this dispatch's docs commit.** Both stops green (batch 52/24/52;
> robust sandwich identity-PASS). Corpus `c50002fee1` (#9 — the pinned, non-stale corpus; measure on it).
>
> **VS Code bash rules:** append `; echo "exit:$?"`; large output → file + `head`. **Do NOT bash to read
> files** — use the file tools.

---

## Task 0 — state + fold the pending principles edit
Confirm HEAD/branch/ahead-0; batch 52/24/52 set-diff empty; corpus fingerprint `c50002fee1`. Confirm the
uncommitted `CLAUDE.md` `## Guiding principles` block is present in the tree (Cowork-applied) and will ride
this dispatch's docs commit.

## Task 1 — feasibility: can C3 be measured READ-ONLY? (#5 cheapest-first, #6 reuse)
Determine, at the source and the existing `fs_*` dump schema, whether **both** C3 trigger components are
derivable **without any `src/` change**:
- **(a) L3 key confidence below its bar** — is `HarmonicRegion.keyConfidence` (and its bar) present in the
  E0 dump for each F-B fire's slice? Derive/verify the bar value at source; if a single bar is not
  well-defined, plan to report across the plausible range (do not assume — the binding rule).
- **(b) chord flips under a carried KEY alternative** — does the E0 dump carry the **carried key alternative
  set** AND a **per-key chord reading** (so "a different carried key flips the chord" is decidable from
  dumped fields)? This is the crux — F-B's dumped `alternatives[]` are *chord* alternatives; (b) needs
  *key* alternatives.

Three possible verdicts, report which:
1. **Read-only measurable** (both derivable from existing dumps) → measure in Task 2 with **no `src/`
   change** (the ideal — #6).
2. **Minimal additive telemetry needed** → identify the smallest default-off field(s) that **surface the
   already-computed** key-alternative-sensitivity signal (byte-identity 0/352 ×3 + a pinned test; the
   `bothLicensed` precedent). Surface an existing quantity — do **not** compute a new one.
3. **The trigger is NOT computed anywhere** (e.g. per-key chord re-decode is not done on this path) →
   **STOP-and-report** (do not build it). This is itself a load-bearing finding: C3-restrict (§3.D-2) would
   require the owed joint-step machinery, so it cannot be scoped as a near-term F-B home — report it and
   proceed to the Task-3 verdict on that basis.

## Task 2 — measure the C3 population within the 1043 F-B fires (#9 pinned corpus, #16 stamped)
On the pinned corpus `c50002fee1`, joined exactly as the §2 taxonomy (reproduce 1043 = 53 + 809 + 181 first):
- **How many of the 1043 fires are C3-qualifying** (both (a) and (b) hold)? Report the count and % of fires.
- **Within C3-qualifying fires: the corr / harm / neutral split.** Is C3 the region where the override is
  net-positive (corr ≥ harm), or is it net-negative like every §2.3 stratum?
- **Complement — within NON-C3 fires:** the corr/harm/neutral split (expected: the fourth/fifth
  "progression-tidying" harm majority per §2.2 — confirm or refute).
- If the bar is range-dependent, report the split across the plausible bar range (sensitivity), not one
  assumed point.
- Stamp the measurement to corpus-hash + instrument-commit (#16); scripts are read-only scratch orchestration
  over dumped fields (the sanctioned "no pinned tool modified" path).

## Task 3 — verdict + the decision surface (does C3 close the surprise? — #3)
- **If C3 isolates a net-positive correction subpopulation:** §3.D-2 (C3-restrict) is a viable correction
  home — it recovers some of the 53 corrections without importing the harms. The principled endgame becomes
  **annotate-via-open-mark everywhere (no loss, #12) + C3-restrict where the override is measured-corrective**
  — state it as the build-event surface.
- **If C3 is also net-negative / too small / un-computable (Task-1 verdict 3):** C3 is not the home; the
  frame stands at **annotate-via-open-mark (honest carry, no correction, no loss)**, and recovering the 53
  becomes an open inference-quality question — **declared, blocked by #8**, not built.
- **#3 discharge:** does the C3 result *explain* the uncorrelated-contradiction surprise (e.g. "the override
  is only theory-justified on C3, and C3 is a Y% minority — the rest was always mis-scoped"), or does a
  residual surprise remain that needs further investigation? State it.
- Name what the eventual build event would touch (`functionresolver.cpp` annotate action reusing the
  existing open-mark carry; contract §4 F-B re-declared as an annotation channel; L5 §5.5/§10/§15-2 spec;
  `docs/scoring_model.md` sync — #10) and the acceptance gate (robust-unit stop; dormant ⟹ identity today,
  must move favorably at engage). **No build here.**

## Task 4 — sandwich + doc + fold + push
1. **If read-only (Task-1 verdict 1):** no `src/` change ⟹ no build; both stops untouched (batch 52/24/52;
   robust sandwich identity-PASS); suites unchanged.
   **If additive telemetry (verdict 2):** build; prove **byte-identity 0/352 ×3** (production `.ours.json`
   unchanged); pinned additive-field test; suites 1101/53+4skip/11 green; **snapshot goldens NOT refreshed**
   (byte-identical — the `bothLicensed` pattern). If any golden would move, STOP (the field is not inert).
2. **Design doc** `cowork_fb_redesign_design.md` §3.D-2 updated with the measured C3 split (or the
   un-computable finding); **report** `cc_engage_c3_measurement_report.md` (force-add) with all SHAs.
3. **Fold** (`docs(cowork):`): the pending **`CLAUDE.md` `## Guiding principles`** edit · `STATUS.md` ·
   `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md` (O-18) · this instruction (force-add).
4. **Push fork-only** (`git push origin master`) — the `cfc7eb5e39` upstream HARD STOP applies.

## STOP conditions
- Any behavior change (annotate/disable is a later event); any golden refresh; any additive field not
  byte-identity-proven 0/352 ×3.
- Building a new C3 detector instead of surfacing an already-computed signal (#6; #8) — Task-1 verdict 3 is
  a report, not a build.
- Any `src/` change beyond additive default-off telemetry; any corpus write; any θ retune.
- Any push/PR/merge toward `upstream`/`musescore/MuseScore` (the `cfc7eb5e39` distribution HARD STOP).
- Any step resting on an unverified assumption (the key-confidence bar value; the dump-schema contents) —
  verify at source or report across the range; do not assume (the binding rule, #1).
- `characterise` ≠ 52/24/52 or the robust sandwich not identity-PASS at close.

## Acceptance
C3 feasibility verdict stated (read-only / minimal-additive-telemetry / un-computable-finding) ✓ · the
C3-qualifying count + its corr/harm/neutral split within the 1043 fires measured (or the un-computable
finding reported), complement measured, bar-sensitivity handled without assumption ✓ · verdict on whether
C3 is a net-positive correction home + the annotate(±C3) decision surface + the #3 surprise-closure
assessment ✓ · if telemetry added: byte-identity 0/352 ×3 + pinned test + stops green + no golden refresh ✓ ·
design doc + report + fold (incl. the Cowork `CLAUDE.md` principles edit) with SHAs ✓ · pushed fork-only,
upstream untouched ✓.

*Cowork, 2026-07-06. Engage arc #2. Investigation (measurement-first), principle-driven (#3/#5/#2 open it;
#12/#6/#7 fix the eventual frame; #8 bounds it). On CC's report: Cowork verifies at objects → presents the
annotate(±C3) build-event decision surface to the user.*
