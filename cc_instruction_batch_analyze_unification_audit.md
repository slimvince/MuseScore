# CC Instruction — `batch_analyze` test-path unification audit (step 2, read-only)

> **Why.** Step 2 / ledger item F17. The corpus **two-tier BIR gate** — the safety net for ALL the behaviour-changing
> L1–L4 finishing work — runs through `batch_analyze`. We must confirm `batch_analyze`'s **corpus-characterisation path
> IS the production analysis path**, not a duplicate/parallel analyzer. If it has its own analysis logic, the gate is
> **testing a different path than ships** (an invalid gate) **and** violates "one path per concern" (full unification).
> **READ-ONLY — code audit, findings only.** (This needs no running tool, so the Qt/`platforms` blocker is irrelevant
> here.) *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §0 — Preamble: protect the uncommitted Cowork docs (sweep)
Commit, **local-only**, the new/modified Cowork docs — `cowork_l1l4_completion_ledger.md` (new, incl. the firewall) and
any other modified `cowork_*`/`COWORK_*`: `docs(cowork): L1-L4 completion ledger + inference firewall`. Confirm `git
show --stat <sha>` lists only docs; report the sha. *(The other parallel CC task — the L1–L3 delta-check — is read-only
and does NOT commit, so there is no git contention.)*

## §1 — Trace the corpus-characterisation path
When `batch_analyze` produces the **`.ours.json`** (the output that feeds the BIR characterisation /
`characterise_bir_false.py`) for a score, **what analysis does it call?** Trace the call chain in
`tools/batch_analyze.cpp` for the corpus/default mode (no diagnostic flag). Does it call the **production entry** — the
same `region/regionanalyzer.cpp` (`analyzeRegions`) + `section/sectionanalyzer` path the **notation product** uses — or
its **own** orchestration / a parallel analyzer? Quote the entry call(s).

## §2 — Separate production-path from diagnostic-only (don't conflate)
The diagnostic flags are **known, accepted** diagnostic-only duplicates and are **NOT** the concern: `--decode-chords`
(`ChordSliceDecoder`), `--dump-tonicization` (`tonicizationlabeler`), `--diagnose-measures` (`diagnoseChord`),
`--dump-key-candidates`, etc. **The audit is ONLY about the main corpus `.ours.json` / BIR-root path.** Confirm which
entry that path uses, and that it does **not** quietly route through a diagnostic analyzer.

## §3 — Unification verdict
- **Reuse (gate valid):** the corpus path calls the production analysis entry → the BIR gate tests the **shipped** path,
  and there is no duplicate analyzer. Confirm + cite.
- **Duplicate (gate risk + unification violation):** the corpus path has its **own** analysis logic that diverges from
  production → flag **exactly what is duplicated**, where it diverges, and the consequence (the gate validates a path
  that isn't what ships). 
- Note any **partial** case (e.g. shares the analyzer but applies different presets/options than the live product) —
  that also weakens the gate's representativeness; report it.

## §4 — Does the corpus output represent the shipped result?
Briefly: for a given score, would `batch_analyze`'s corpus key/chord output equal what the **notation product**
(`addHarmonicAnnotationsToSelection` / the live bridge) produces via the same path? (The gate's validity rests on this.)
Report any known divergence (preset defaults, section vs region granularity, etc.).

## §5 — Deliver
Write `cc_batch_analyze_unification_report.md` (gitignored): the §1 corpus-path call chain, the §2 production-vs-diagnostic
separation, the §3 **unification verdict** (reuse / duplicate / partial), and the §4 shipped-result representativeness.
**No edits beyond the §0 doc commit.** Report the §0 sha.

## §6 — Stops
- Any source edit, or any non-doc commit → STOP (read-only audit).
- A push targets `upstream` → STOP.
