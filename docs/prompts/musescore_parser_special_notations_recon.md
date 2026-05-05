# Recon — MuseScore Parser Acceptance for Special-Notation Catalog Entries

**Scope:** Read-only investigation. No source edits, no build, no
tests. Determine whether MuseScore's chord-symbol parser
(`HarmonyType::STANDARD` path in `src/engraving/dom/harmony.cpp`)
accepts each of the 5 RealDiff catalog entries that current
classification put in "special notations" or "structural mismatches"
buckets. The answer determines whether these entries are
**vocabulary mismatches** (catalog uses labels MuseScore can't
parse, so analyzer can never emit them) or **genuine
disagreements** the analyzer could potentially resolve.

Vincent already verified one case: m285's catalog expected is
`C Tristan`, which MuseScore's parser does not accept. The recon
extends this verification across all 5 entries.

**Reference docs (read first):**
- `docs/phase5_recon.md` Q1 — engraving capability for chord
  symbol vs. Roman numeral parsing. Notes that `HarmonyType::ROMAN`
  parsing is a no-op (accepts any string), but `HarmonyType::STANDARD`
  has real parsing with equals-sign stripping at lines 226-228.
- `src/composing/tests/chord_mismatch_report.txt` — current
  mismatch report; has the catalog's expected text for each
  RealDiff entry
- `src/engraving/dom/harmony.cpp` — chord symbol parser (the file
  Phase 5 recon already characterized for ROMAN parsing; this
  recon focuses on STANDARD parsing)

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer outputs
  parseable maximal output; bounded by parser vocabulary
- `project_chord_symbol_ban` — analyzer doesn't read user
  chord-symbol input; this recon is about analyzer-emit
  vocabulary, not analyzer-input

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).

---

## Investigation

This is a read-only recon. Do not modify any source file. Do not
run the build or tests. The only file written this session is the
recon report itself.

### Q1 — Identify the 5 RealDiff catalog expected labels

Read `src/composing/tests/chord_mismatch_report.txt` and identify
the catalog's expected chord-symbol text for each of the 5
RealDiff entries. The entries should include:

- m285 (catalog expected per Vincent: `C Tristan`)
- m340 (sus4/triad ambiguity per CC's earlier classification)
- Three more entries with catalog labels matching `C7alt`,
  `CPhryg`, `Cm9b5` (or similar names — verify exact text from
  the report)

For each entry, capture:
- Measure number
- Catalog's expected chord-symbol text (verbatim — copy-paste from
  the report, don't paraphrase)
- Analyzer's actual output (also verbatim)

Surface as a table. If any entry's expected text differs from the
"special notation" pattern (e.g., it's actually a parseable
chord-symbol with some other reason for being a RealDiff),
categorize separately.

### Q2 — Locate MuseScore's `HarmonyType::STANDARD` parser

Find the parsing code path for STANDARD chord symbols in
`src/engraving/dom/harmony.cpp`. Phase 5 recon noted the file
has equals-sign stripping at lines 226-228; the actual parser
entry point is somewhere else in the same file (or a sibling).

Identify:
- The parser entry function name and location (file:line)
- What "successfully parsed" means in MuseScore terms — does the
  parser produce a valid root+quality+extensions structure? Or
  is "parsed" looser (any string accepted but flagged
  TPC_INVALID, like the ROMAN path)?
- Where in the parser unrecognized chord types fall through to
  failure (or to a textual-only mode)

### Q3 — Categorize each catalog label's parser acceptance

For each of the 5 catalog labels from Q1, reason from the parser
code (Q2) about what MuseScore does:

- **Recognized** — parser produces a valid root + quality +
  extensions. The chord symbol is a first-class chord MuseScore
  understands.
- **Accepted-as-text** — parser accepts the string but produces
  `TPC_INVALID` or equivalent unparseable marker. The text
  displays but isn't recognized as a chord with structure.
- **Rejected** — parser fails or errors on the string.

For uncertain cases (where reasoning from code alone doesn't
clearly resolve to one of these three), flag as **uncertain —
empirical verification needed** rather than guessing.

The known case (Vincent's verification): `C Tristan` is
**rejected** or **accepted-as-text** (depending on how MuseScore
handles it; per Vincent: "Musescore cannot parse" — likely the
unparseable-text outcome, but worth confirming the parser's
specific behavior).

### Q4 — Implication per entry

For each entry's verdict from Q3:

- **Recognized:** the analyzer should be ABLE to emit this label.
  The fact that it doesn't is a real analyzer gap (missing chord
  type recognition or formatting). Belongs in actionable RealDiff
  bucket.
- **Accepted-as-text or Rejected:** the catalog's label is
  outside the analyzer's emit vocabulary by construction. No
  analyzer change can produce a match without breaking parser
  rendering. Belongs in a new category (vocabulary mismatch).

If all 5 entries categorize as "vocabulary mismatch," the actionable
RealDiff baseline drops to 0 once the new category is recognized.
If any are "Recognized," that's a real analyzer gap to address
separately.

### Q5 — Resolution recommendation

Based on Q1-Q4, recommend a path forward. Three options Vincent
already framed:

- **(A) Accept and re-categorize.** Extend `classifyComparison`
  with a `VocabularyMismatch` classification (alongside `DirectMatch`,
  `ConventionDiff`, `RealDiff`). Entries where the catalog's
  expected text isn't parser-recognized go in this new bucket.
  No catalog edits.
- **(B) Update the catalog** to use parser-recognized labels for
  these entries. Requires explicit approval per the
  do-not-touch rule.
- **(C) Allow multiple acceptable expected labels per catalog
  entry.** Catalog format extension; comparison protocol checks
  against any of multiple acceptable strings.

Recommend one based on Q3-Q4 findings. State the trade-off briefly
(no catalog edits vs. cleaner test signal vs. format flexibility).

---

## Deliverable

Write a single report file at
`docs/musescore_parser_special_notations_recon.md` with sections
matching Q1-Q5. Concise and citation-heavy — every parser-behavior
claim backed by file:line. Total length: probably 2-3 pages of
markdown.

Suggested skeleton:

```markdown
# MuseScore Parser Acceptance for Special-Notation Catalog Entries

Date: 2026-04-26
Scope: read-only, no source edits.

## Verdict

[Per-entry parseability table; recommended resolution path with
brief rationale]

## Q1 — Catalog expected labels

[Verbatim table from chord_mismatch_report.txt for the 5 entries]

## Q2 — STANDARD parser location and behavior

[Parser entry, success/failure semantics, citations]

## Q3 — Per-entry parseability

[Per-entry verdict: Recognized / Accepted-as-text / Rejected /
Uncertain, with parser-code reasoning per entry]

## Q4 — Implication per entry

[Whether each is actionable RealDiff or vocabulary mismatch]

## Q5 — Resolution recommendation

[Recommend (A) / (B) / (C) with rationale]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Recon: MuseScore parser acceptance for special-notation catalog entries

Investigates whether the 5 RealDiff catalog entries (m285's
"C Tristan" plus four others) are real analyzer disagreements or
vocabulary mismatches between catalog labels and MuseScore's
HarmonyType::STANDARD parser.

Findings: [N of 5] entries are parser-rejected (vocabulary
mismatch), [M] are parser-recognized (real analyzer gap), [K]
uncertain.

Recommends [A/B/C] for resolution. [Brief rationale.]
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Verdict table: per-entry parseability summary
- Recommended resolution path (A/B/C) with one-sentence rationale
- The single most surprising finding (e.g., one of the entries is
  actually parser-recognized and represents a real analyzer gap;
  or all 5 are unparseable; etc.)
- Any uncertain cases flagged as needing empirical verification
- Any deviations from this prompt and why

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/musescore_parser_special_notations_recon.md`.
- **Do not** run the build or tests. Pure code-and-report-reading
  recon. Empirical verification (creating Harmony elements,
  checking parser behavior at runtime) is out of scope; flag
  uncertain cases instead of running code to resolve them.
- **Do not** propose code changes in the report — fix prompts
  come after, informed by the verdict.
- **Do not** speculate beyond what the parser code shows. "I
  can't determine this from code reading alone" is a valid
  finding; confidently-wrong guesses are worse than honest
  uncertainty.
- **Do not** modify the catalog (`chordanalyzer_catalog.musicxml`)
  in this session. Catalog edits are a separate session pending
  Vincent's approval.
- **Do not** confuse `HarmonyType::ROMAN` parsing (no-op, accepts
  any string) with `HarmonyType::STANDARD` parsing (real chord-symbol
  parsing). The recon targets STANDARD specifically; ROMAN is
  not relevant here since the catalog's chord-symbol expected
  texts are STANDARD-typed.
