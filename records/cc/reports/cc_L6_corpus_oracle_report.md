# CC — L6 Oracle Check: does our ground truth carry phrase + cadence annotations?

**Read-only measurement. No code, no build, no commit, no production movement.** This
reports *what the oracle contains*, so Cowork can decide L6 (grouping: flat phrases +
key-areas + cadence-to-phrase alignment) verifiability. Findings are declared, not inferred.

Date: 2026-06-30. Scope: the **353-stem Bach-chorale gate** (`tools/corpus/`), plus the
DCML TSV corpora for completeness (the format that *does* carry the markers Cowork referenced).

---

## §1 — Ground-truth source + format

The 353 stems are the **music21 Bach-chorale corpus** (`tools/corpus/*.xml`, 353; the
analyzer's input), scored against **two** ground truths — and a **third** GT path exists for
the *other* (non-chorale) corpora:

| GT | Format | Path (representative) | Covers 353? | Coverage |
|---|---|---|---|---|
| **music21 (machine)** | derived JSON, per-region | `tools/corpus/<preset>/bwv269.music21.json` | yes | **353/353** |
| **When-in-Rome (human)** | **RomanText `.txt` (rntxt)** | `tools/dcml/when_in_rome/Corpus/Early_Choral/Bach,_Johann_Sebastian/Chorales/001/analysis.txt` (folder `001` → `bwv269.mxl` via `remote.json`) | yes, partial | **326/353** ¹ |
| DCML TSV (human) | tab-separated `.harmonies.tsv` | `tools/dcml/corelli/harmonies/op01n01a.harmonies.tsv` | **NO** — corelli/mozart/chopin/ABC/grieg/schumann/dvorak/tchaikovsky/cpe_bach/bach_en_fr_suites only | n/a to 353 |

- The WiR rntxt is the **human** chorale oracle, resolved per stem by
  `dcml_parser.find_wir_file` (reads each folder's `remote.json` → music21 stem → `analysis.txt`).
  Parsed by `parse_rntxt_file`.
- **DCML `bach_chorales/` has NO `harmonies/` dir** (only `measures/`, `notes/`, `MS3/`,
  `metadata.tsv`, `reviewed/`) → there are **no DCML-format RN/phrase/cadence annotations for Bach
  chorales at all**. That is *why* the chorale oracle is WiR rntxt, not DCML TSV.
- The DCML TSV path (`parse_abc_harmonies_file`) serves the classical/Baroque corpora — **different
  repertoire**, not the 353. (And the 353 ↔ DCML-bach mapping is **not recoverable in-repo**:
  music21 BWV ids vs DCML Riemenschneider numbers, no concordance — per `docs/score_inventory.md`.)

¹ `326/353` is the documented WiR-resolution denominator (`score_inventory.md`, Stage 2.3 Rider 2;
324 distinct analysis files). The remaining 27 stems have no human Roman-numeral annotation.

---

## §2–§5 — Marker inventory

### Table A — the 353-stem Bach-chorale oracle (WiR rntxt + score)

| Annotation | Present in GT? | Marker form | Example | Coverage / 353 |
|---|---|---|---|---|
| **Phrase boundaries** | **NO** | RomanText has no `{ }` / `\\` syntax. `\|\|` exists but the spec defines it as a **pivot-chord** marker, not a phrase end | `m4 V \|\| b3 I` (bwv269) — pivot, not phrase | **0/353** (0/371 analysis.txt carry `{`) |
| **Cadence labels** | **NO** | RomanText has no `\|PAC`/`\|HC`/… syntax; only `Cad64`/`Ca64` (a cadential-6/4 *chord*, not a cadence *type*) — and even that is absent here | none present | **0/353** (0/371 carry `Cad` or `\|PAC\|HC\|IAC\|DC\|EC\|PC`) |
| **Local key / key-area** | **YES** | `Key:` colon token; `\|\|` introduces a pivot to a new key | `m0 b3 G: I` (bwv269); spec ex. `m2 I \|\| f: III` | **326/353** human ² |
| **Fermatas (score, §5)** | **YES** (in the `.xml` the analyzer reads, not the GT) | `<fermata …>` in MusicXML | `bwv269.xml` carries `<fermata` | **351/353** ³ |

² All **371/371** WiR analysis.txt carry ≥1 `Key:` token; **367/371 modulate** (≥2 distinct
keys) → the key-area oracle has rich *interior* structure, not just a global key. The 353-coverage
number is the WiR-resolution rate (326).
Additionally, **music21.json carries a per-region `key` + `keyGlobal` field at 353/353** — a
*machine* key-area oracle. Caveat: in the sampled chorale every region's `key` == `keyGlobal`
(no local-key segmentation surfaced), so music21's key-area granularity looks **coarser** than the
human WiR annotation; treat music21 as a backstop, WiR as the finer key-area truth.

³ `351/353` `.xml` carry `<fermata`. The 2 without: `bwv112.5`, and a **stray non-chorale
`corelli.xml`** that is sitting in the 353-glob (data-hygiene note — not a chorale; genuine chorale
fermata coverage ≈ 351/352). Fermatas land at chorale phrase ends → this is the **fallback phrase
oracle** for §2.

### Table B — the DCML TSV corpora (corelli/mozart/chopin/ABC/grieg/… — NOT the 353)

This is where the `{ }` phrase markers and `|PAC` cadence labels Cowork referenced actually live —
but on **non-chorale repertoire**.

| Annotation | Present? | Marker form | Example (corelli `op01n01a`) | Note |
|---|---|---|---|---|
| **Phrase boundaries** | **YES** | `phraseend` column: `{` open, `}` close, `}{` adjacent | row 1 `phraseend = {`; 5×`{`/5×`}` in op01n01a | populated across the corpus |
| **Cadence labels** | **YES** | `cadence` column | `PAC` (×209 corelli-wide), `HC` ×65, `IAC` ×36, `EC` ×6, `DC` ×1 | DCML standard PAC/IAC/HC/DC/EC |
| **Local key** | **YES** | `localkey` column (absolute or RN-relative) | `I`, `V`, … resolved vs `globalkey` | as parsed today |

**Important for any reuse:** `dcml_parser.parse_abc_harmonies_file` currently reads **only**
`numeral`/`localkey`/keys/ticks — it does **not** extract the `cadence` or `phraseend` columns.
The data is on disk; the parser does not surface it. (Declared, not a recommendation to change.)

---

## §6 — Verdict

The 353-stem Bach-chorale gate is the **"only RN + local-key"** case from the instruction:

- **Key-areas → directly validatable against GT.** Human WiR `Key:` spans (326/353, 367/371
  modulating) are the fine oracle; music21 `key`/`keyGlobal` (353/353) is a coarser machine backstop.
- **Phrases → no `{ }` / `\\` GT for the chorales.** Validate L6's flat-phrase output against
  **score fermatas (351/353)** — the fallback phrase oracle (§5), not a Roman-numeral annotation.
- **Cadences → NO direct GT oracle for the chorales.** ⚠ **Flag for the verifiability contract:**
  L6's cadence-to-phrase **alignment output is not gradeable against ground truth on the 353-stem
  gate.** The WiR rntxt carries no cadence-type labels, and DCML-bach carries no harmonies at all.
  Cadence-type GT (PAC/HC/IAC/DC/EC) *does* exist — but only in the **DCML TSV** corpora
  (corelli/mozart/chopin/ABC/grieg/…, Table B), which are different repertoire, reached by a
  different parse path, and whose `cadence`/`phraseend` columns the parser does not currently read.
  Mapping those onto the 353 chorales is blocked (no BWV↔Riemenschneider concordance; no DCML-bach
  harmonies).

**One line:** *Key-areas validate against the GT; phrases validate against score fermatas; cadences
have no direct GT oracle on the 353-stem chorale gate (real cadence labels exist only in the
non-chorale DCML TSV corpora).*

*(No code, no build, no commit. `upstream` untouched. This is a measurement of oracle contents.)*
