# CC Instruction: E3 Architecture Investigation (read-only)

## Pre-reading (mandatory)

Read `C:\s\MS\STATUS.md` (header only) and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `a693b6ba82`. No code changes in this instruction.

---

## Background

The E3 roadmap entry (written during E2c, before the E2d redesign) says:

> "Gate J (vii°→V7 completion), Gates A–D (Minor-add6 ↔ HalfDim7 enharmonic),
> `dim7CharacteristicBonus` rotation selection — functional-reasoning rules that do
> not belong in the scorer. Move them here [to the function layer] after E2 is stable."

Since then:
- The scoring oracle / competition pipeline segregation (E2d) fundamentally changed
  the architecture. `applyHarmonicFunction` is now the sole competition pipeline.
- `applyPostScoringGates` already exists as a separate free function called AFTER
  `applyHarmonicFunction` at every production call site — the gates are already
  outside `analyzeChord`.
- The gate alphabet has grown to A–L with sub-gates (G-E, G-B/C/D, H-B/C/D).

Before writing any E3 implementation instruction, we need an independent assessment
of what E3 should actually mean given the current architecture.

**This is read-only. No code changes. No commits.**

---

## Files to read

1. `src/composing/analysis/function/harmonicfunctionlayer.h` — full
   (`HarmonicFunctionContext`, `ScoringSnapshot`, `applyHarmonicFunction` signature,
   constants)

2. `src/composing/analysis/chord/chordanalyzer.h` — `ChordTemporalContext` struct
   (all fields) and `PostScoringGateContext` struct.

3. `src/composing/analysis/chord/chordanalyzer.cpp`:
   - `applyPostScoringGates` — full function (approximately lines 1885–2458)
   - The `dim7CharacteristicBonus` call site in `analyzeChord`'s per-cell scoring loop
     (search `basisIndepMatrix` to find the line; read ~10 lines around it)
   - The `applyIter8691Pedal` function — just the signature and first 20 lines

4. `src/composing/analysis/region/regionanalyzer.cpp` — one complete production call
   site (Pass 1). Trace the full chain from `analyzeChord` through
   `applyIter8691Pedal` through `applyPostScoringGates`. Note what context/prefs are
   passed to each.

5. `C:\s\MS\docs\scoring_model.md` §4 (scoring pipeline) and §11 (E2d architecture).

---

## Questions

---

### Q1 — Full gate inventory in `applyPostScoringGates`

For every distinct gate or correction block in `applyPostScoringGates`, list:

| Gate | One-line description | Reads from `context`? (yes/no) | Specific `context` fields used |
|------|---------------------|-------------------------------|-------------------------------|
| Main bias-correction | … | … | … |
| Gate A fast-path (enharmonicFlip) | … | … | … |
| Gate B | … | … | … |
| … | … | … | … |

Mark each as **structural** (uses no `context` fields, or guards on `context != nullptr`
before using them) or **temporal** (requires `context != nullptr` to be useful).

---

### Q2 — `HarmonicFunctionContext` gap analysis

`HarmonicFunctionContext` currently has: `keyFifths`, `keyMode`, `previousRootPc`,
`nextRootPc`, `previousBassPc`, `nextBassPc`.

If ALL temporal gates from Q1 were moved into `applyHarmonicFunction`, what additional
fields would `HarmonicFunctionContext` need? List each:
- Field name and type (matching the existing `ChordTemporalContext` field)
- Which gate(s) use it
- Where it is currently populated (bridge? regionanalyzer?)

---

### Q3 — `dim7CharacteristicBonus` placement assessment

Find the `dim7CharacteristicBonus` call in `analyzeChord`.

Answer:
1. Is it inside the per-cell scoring loop (basisIndep computation per root × template)?
2. Does it use any progression context (`previousRootPc`, `nextRootPc`, bass motion,
   `recentRootPcs`)? Be specific.
3. The E3 roadmap says "move it to the function layer." Given its actual location
   and inputs, is this correct? Would moving it change any scores?

---

### Q4 — Architectural assessment

Answer these questions from first principles, based on what you read:

**Q4a.** `applyPostScoringGates` lives in `chordanalyzer.cpp`. Is this the right file?
Arguments for keeping it there vs. moving it to `harmonicfunctionlayer.cpp`:
- It uses `RawCandidate` (defined where?), `buildChordResult` (defined where?),
  `PostScoringGateContext` (defined where?) — are these types accessible from
  `harmonicfunctionlayer.cpp`, or would moving the function require promoting them?

**Q4b.** Is there a meaningful architectural distinction between:
- The competition signals (rcb, wSeq, wDim, step bonuses) in `applyHarmonicFunction`
- The temporal gates (B, C, D, G-B, G-C, G-D, H-B/C/D) in `applyPostScoringGates`

Both use prev/next context to select a winner. If they are architecturally the same
kind of thing, should they be in the same function? If they are different, explain the
distinction.

**Q4c.** Is there any scenario where the temporal post-scoring gates produce incorrect
results because they run AFTER `applyIter8691Pedal`? Or could running them before
the pedal pass (i.e. moving them into `applyHarmonicFunction`) change any output?

---

### Q5 — Concrete scope recommendation

Given your answers to Q1–Q4, propose a specific scope for E3. Choose one of:

**Option A — File relocation only**: Move `applyPostScoringGates` (unchanged) from
`chordanalyzer.cpp` to `harmonicfunctionlayer.cpp`. No behaviour change, just
architectural tidying. Assess feasibility: does it require promoting any types?

**Option B — Merge temporal gates into `applyHarmonicFunction`**: Move the temporal
gates (B, C, D, G-B, G-C, G-D, H-B/C/D) into the competition pipeline and extend
`HarmonicFunctionContext` with the needed fields. Structural gates stay in
`applyPostScoringGates`. Assess: would this change any results? Is byte-identical
possible?

**Option C — Something else entirely**: If neither A nor B is right, describe what is.

For whichever option you recommend, estimate:
- Number of files changed
- Whether all tests remain byte-identical
- Any risks or open questions

---

### Q6 — Anything that looks wrong

While reading `applyPostScoringGates`, flag anything that looks incorrect, fragile,
or inconsistent — regardless of whether it's in E3 scope.

---

## Output

Write findings to `C:\s\MS\cc_e3_investigation_report.md`.

Structure:
```
# E3 Architecture Investigation

## Q1 — Gate inventory
(table + structural/temporal classification)

## Q2 — HarmonicFunctionContext gap analysis
…

## Q3 — dim7CharacteristicBonus assessment
…

## Q4 — Architectural assessment
### Q4a — File placement
### Q4b — Signal vs gate distinction
### Q4c — Ordering with applyIter8691Pedal

## Q5 — Scope recommendation
…

## Q6 — Anomalies / concerns
…

## Summary
3–5 sentences: honest bottom line.
```

No code changes. No commits.
