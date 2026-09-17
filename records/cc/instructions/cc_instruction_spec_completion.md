# CC instruction — Phase 1 of the three-phase rule: make the specifications COMPLETE (the homing acts) and TRUE (the truth-sync)

> **Read first (every session):** `C:\s\MS\CLAUDE.md` IN FULL — note especially the THREE newest
> Conventions entries (every design decision carries its defense at its home, 2026-08-01; the
> decisions-register section — `DECISIONS.md` is now a MANDATORY session-start read and a new
> ruling lands in the register in its recording commit; **the three-phase sequencing rule,
> 2026-08-02, D-231 — THIS DISPATCH IS ITS PHASE 1**). Also `C:\s\MS\DECISIONS.md` (the INDEX;
> full entries under `decisions/group_*.md`), `C:\s\MS\STATUS.md`, `C:\s\MS\BUILD_AND_TEST.md`,
> `C:\s\MS\OPEN_ITEMS.md` (INDEX) with detail files **OI-237, OI-240** (the homing lists) and
> **OI-232, OI-233, OI-236, OI-238, OI-242, OI-257, OI-107, OI-112** (the truth-sync lists), and
> `C:\s\MS\cowork_design_doc_template.md` (the writing standards BIND every specification
> sentence you write: predicates qualified; defined terms, plain vocabulary; the bare word always
> carries the musical meaning).
>
> **Current state:** branch `master`; expected HEAD `b006dc15b5` — verify; mismatch = STOP.
> **NOTE: the local branch is AHEAD of origin** (pushes from the authoring environment fail on
> credentials); your FIRST act after verifying HEAD is `git push origin master` to land the
> pending commits, and your last act is pushing your own.
>
> **Hard stops:** origin only; **no `src/` change of any kind**; no golden, `tools/corpus/` or
> `tools/robust_stop/` movement; **no fix, no design, no inference change — `ARCHITECTURE.md`
> text edits ARE this dispatch's work, and they RECORD decisions already ratified; they never
> make new ones.** Where writing a specification entry would force you to RESOLVE something the
> record leaves open (a tension, a missing value, an unstated rule), you STOP on that entry,
> record it as a remainder, and move on — resolving is phase-3 work. A surprise is a STOP (#13).
> VS Code bash rules on every command. A feasibility stop with a measured partition is an
> accepted outcome.

**Dispatch author:** Cowork, 2026-08-02.

## Why this dispatch exists

The user ruled (D-231): conformance will be measured against the SPECIFICATIONS, not against the
decisions register — so the specifications must first be made complete (every decision written
into its owning specification) and true (no statement that misdescribes HEAD). The register
remains the status ledger and index. Phase 2 (the exhaustive audits) runs against the
specifications this dispatch completes.

## Task 1 — the homing acts (specifications made COMPLETE)

**Select mechanically, never by hand-list:** every register entry in
`tools/audit/decisions/backbone_decisions.json` whose `nonspec_kind` is `"gap"` (8 expected) or
`"unhomed"` (12 expected). For each:

1. Write the decision into its OWNING specification — the layer's section of `ARCHITECTURE.md`
   for layer-governing decisions; for the `unhomed` class, `open_items/OI-240.md` names candidate
   homes per kind — follow them, and justify any deviation in the report. The entry states the
   RULE in the specification's own voice (not a quotation of the register) AND its defense (the
   research, measurement, or constraint — the 2026-08-01 rationale rule; §17.2's model), citing
   the ratifying event by date.
2. **Do not resolve open tensions by drafting.** Known live case: D-114 (no key abstention) sits
   in tension with D-090 (calibrated abstention, already in a layer specification) — the D-114
   entry states the decided rule AND names the tension with a pointer; it does not settle it.
3. Update the register entry: `home` moves to the new `file:line`; the former home goes into
   `status_source` (provenance is never discarded, #12); `home_is_layer_spec`/`nonspec_kind`
   updated. The verbatim quote must be re-taken from the NEW home (the guard checks it there).

## Task 2 — the truth-sync (specifications made TRUE)

Correct every specification statement the named rows establish as false at HEAD — text-only,
each correction citing its row: the eight stale which-code-is-running statements (OI-232, list
in its detail file), OI-233, OI-236, the §5.13 table (OI-238 — including the caller column: the
implode bridge contains no call to `analyzeHarmonicContextAtTick`; the tuning bridge calls
different functions; and the record-arm reality, flag default ON), the false "well under 1 ms"
§12.1a reason (OI-242 — state the measured truth: a whole-score decode per single-note selection
on the record arm, the status bar the sole per-selection payer; do NOT prescribe the fix), the
§12.1b two-of-nine actions table + the undocumented chord-anchor choice (OI-257), and the older
§4/§5 drifts (OI-107, OI-112). Each corrected statement must describe HEAD exactly; where the
correct statement depends on an unresolved question, say "open — see OI-nnn" rather than
guessing.

## Task 3 — regeneration, guards, and the anchor discipline

Your `ARCHITECTURE.md` insertions SHIFT LINE ANCHORS for everything below them. After each
editing wave: regenerate the register (`gen_decisions_register.py`), run
`gen_cluster_dispositions.py --verify`, and remap every drifted citation in the backbone (the
JSON round-trips byte-identical at `json.dumps(indent=2, ensure_ascii=False)` with no trailing
newline — parse, remap `ARCHITECTURE.md:<n>` references by the insertion deltas, re-serialize;
the drift report gives authoritative new start lines). All three guards must PASS at the final
tree: `gen_decisions_register.py --check` (all 21 files), `--verify` (quotes, anchors,
references), `python tools/open_items_split_check.py`.

## Task 4 — rows, notes, close

Flip OI-237 and OI-240 (resolved — homes written) and each truth-sync row you fully discharge
(OI-242, OI-257, and OI-232/233/236/238/107/112 as applicable — partial discharge = dated note,
not a flip). Dated notes on every flipped or noted row. `STATUS.md` entry — a POINTER at the TOP
of the file. Commits per change-class. **Push origin** (first act AND last act — see above).

## Report

Hashes (including confirmation the pre-existing local commits were pushed). Task 1: the 20
entries, each with old home → new home, and any deviation from OI-240's candidate homes.
Task 2: each corrected statement, before/after, with its row. Task 3: guard results + the anchor
remap counts. Task 4: rows flipped vs noted. Every entry you could NOT home or correct without
resolving something open — listed as remainders with the reason (these are phase-3 inputs, and
an honest remainder list is a successful outcome). Standing self-check before reporting.
