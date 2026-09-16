# CC Instruction — L6 oracle check: does our ground truth carry phrase + cadence annotations? (read-only)

> **One read-only question, no code/build/commit/production movement.** L6 (grouping) produces **flat phrases + key-areas
> + cadence-to-phrase alignment**. Its validatability depends on **what our ground truth actually annotates.** Determine,
> from the GT files we validate against, whether they carry **(a) phrase boundaries (`{ }`, or the legacy `\\`)**,
> **(b) cadence labels (`|PAC`/`|HC`/…)**, and **(c) local-key / key-area spans** — and at what coverage across the 353
> stems. This decides L6's oracle; it changes nothing. **Declare findings; do not infer or build.** *(The never-bash rule
> is Cowork's — you read corpus files and may run read-only corpus tooling.)*

## §1 — Identify the ground-truth source + format (read-only)
- From `tools/dcml_parser.py`, `tools/compare_rn`, `docs/score_inventory.md`, and the registries
  (`tools/corpus_registry.json`, `tools/extra_scores_registry.json`), report **exactly which files** are the GT we score
  against (DCML `.tsv`/`.mscx`? When-in-Rome RomanText `.rntxt`? music21? a derived `.music21.json`?) and **where they
  live**. Name the format and a representative path.

## §2 — Phrase annotations
- Inspect the GT files: are **phrase boundaries** present — the DCML curly brackets `{` / `}` (or the legacy `\\`
  phrase-end marker)? Report the **marker form**, an example line, and **coverage** (how many of the 353 stems carry any
  phrase annotation). If the parser strips them, check the **raw** GT, not just the parsed `.json`.

## §3 — Cadence labels
- Are **cadence labels** present — the DCML `|PAC` / `|IAC` / `|HC` / `|DC` / `|EC` / `|PC` on the ultima? Report which
  types appear, an example, and **coverage** across the 353 stems.

## §4 — Local key / key-area
- Confirm **local-key** annotations are present (we expect yes — the RN GT carries `localkey`) and report their form
  (RomanText `Key:` lines / DCML `localkey` column / the modulation dot `.` notation) and coverage. This is the
  key-area oracle.

## §5 — Fermatas in the scores (the phrase-primitive input + fallback oracle)
- In the **score files** the analyzer reads (the `.musicxml`/`.mscx` corpus, not the GT analyses), confirm **fermatas**
  are present at phrase ends (the chorale phrase marker our phrase-boundary primitive consumes). Report coverage. This is
  the **fallback phrase oracle** if §2 finds no `{ }` annotations.

## §6 — Deliver (report only)
Write `cc_L6_corpus_oracle_report.md` (gitignored): a small table — for **phrases, cadences, local-key, fermatas** —
{present? · marker form · example · coverage/353}, the GT source+format from §1, and a one-line verdict:
- **If phrases + cadences are present in the GT** → L6 phrase/cadence output is **directly validatable** against ground
  truth.
- **If only RN + local-key** → key-areas are validatable against the GT; **phrases validate against the score fermatas**
  (§5) instead, and **cadences would have no direct GT oracle** (flag this — it bears on whether L6's cadence-alignment
  output is gradeable, and feeds the verifiability-contract decision for that part).
**No code, no build, no commit, no production movement.** `upstream` → STOP. Declare everything; this is a measurement of
what the oracle contains, not a change.
