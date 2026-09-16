# CC Instruction — corpus hygiene: remove the stray non-chorale `corelli.xml` from the chorale gate (careful, attributed)

> **A deliberate, attributed corpus cleanup — INVESTIGATE first, then clean, then re-confirm the baseline.** The L6
> oracle check found a stray non-chorale `corelli.xml` inside the 353-stem `tools/corpus/*.xml` glob. The chorale gate
> must be **chorales only** before the non-chorale DCML-TSV validation corpora are brought in (clean separation). This is
> **data hygiene, not inference-fixing** (firewall-clean), but it touches the corpus, so **any 53/24/53 movement must be
> understood and attributed, never silent** (minimum-surprise). *(The never-bash rule is Cowork's — you run the corpus
> tooling.)*

## §1 — INVESTIGATE first (read-only; report BEFORE changing anything)
Answer precisely:
- **Is `corelli.xml` actually in `tools/corpus/` and in the gate glob?** Confirm the path(s). How many `.xml` files does
  the glob yield — is the "353" inclusive of `corelli` (i.e. 352 chorales + corelli) or is corelli a 354th file?
- **Is it scored?** Does `corelli.xml` have a matched ground truth (`*.music21.json` / a WiR `analysis.txt` / a `.ours.json`)?
  Does `characterise_bir_false.py` / `run_bach_preset.py` actually include it in the 53/24/53 measurement, or is it an
  **unscored orphan** the GT-match step skips?
- **Is it registered?** Check `tools/corpus_registry.json` / `tools/extra_scores_registry.json` / `docs/score_inventory.md`
  — is corelli a registered member, or an orphan file?
- **Predicted gate effect:** the 53/24/53 identity sets are all `bwv*` (no `corelli@…`), which suggests corelli is **not**
  contributing a BIR case. Confirm whether removal is therefore **byte-identical on the gate** or actually moves a count.
**Report these findings. If removal would move a BIR case-identity (corelli is genuinely scored) → say so and STOP for a
Cowork ruling before cleaning** (that would be a real gate change, not pure hygiene).

## §2 — CLEAN (only after §1 confirms it is safe / an orphan)
- Remove `corelli.xml` from the chorale corpus location, plus any **derived artifacts** for it (`corelli.music21.json`,
  `corelli.ours.json`, manifest entries) so the chorale corpus is purely `bwv*` chorales.
- If it was registered, update the registry/manifest accordingly.
- Do **not** touch any `src/`/`tools/` analysis code — this is corpus data only.

## §3 — RE-CONFIRM + ATTRIBUTE the baseline
- Re-run the gate on all three presets (`run_bach_preset.py` + `characterise_bir_false.py`, per `CLAUDE.md`) and report
  the **53/24/53 case-identity sets**.
- **Attribute the result explicitly:** either "removal byte-identical — corelli was an unscored orphan; sets unchanged
  53/24/53" **or** the exact delta if anything moved (which case, why). The case-identity set is the gate — state it.
- **`bwv112.5` note:** it lacks a fermata (the one chorale of 353 without one) — a 1-stem edge for the fermata phrase
  oracle. **Declare it; do not act** — whether/how to handle it is an L6-design decision, not a hygiene fix.

## §4 — Deliver
Commit **locally (unpushed)** the corpus-hygiene change (corpus data + registry only): message e.g.
`chore(corpus): remove stray non-chorale corelli.xml from the chorale gate; gate 53/24/53 unchanged` (adjust if the gate
moved). Write `cc_corpus_hygiene_report.md` (gitignored): the §1 findings, the §2 removal (files/entries removed), the §3
re-confirmed/attributed 53/24/53, the `bwv112.5` note, and the sha. **Push is a separate Cowork-issued step — do not push.**

## §5 — Stops
- §1 shows corelli is genuinely scored and removal would move a BIR identity → STOP, report, await Cowork ruling. Any
  `src/`/`tools/` **code** change, any threshold/inference change, any push → STOP. `upstream` → STOP.
