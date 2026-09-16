# CC instruction — CORPUS WAVE 1: complete the DCML/DLC container + registry v2 + the free cadence win

> **✅ DISPATCHED (Cowork revalidation note, 2026-07-02, post-gap-analysis, user "go").** Revalidated against the
> session-21e state. Binding deltas for this run:
> - **Current state supersedes the stanza below:** HEAD carries the E0-arc commits (tip `5f7cb7376e`, local,
>   unpushed); suites composing **998** / notation 53 (4 skipped) / snapshots 11/11; gate **53/24/53** unchanged.
>   Quote your own `git rev-parse HEAD`. Queue position confirmed: this is the ONLY active instruction.
> - **The dev/held-out designation (Task A `split` field), per the engage-criteria E2 discipline:**
>   the 11 already-in-use corpora = `dev` (they are development material by history). For the NEWLY onboarded
>   sub-corpora: **`dev` = {beethoven_piano_sonatas, wagner_overtures, liszt_pelerinage, rachmaninoff_piano,
>   schulhoff_suite_dansante_en_jazz, monteverdi_madrigals}** (the named capability/idiom measurement beds);
>   **every other newly onboarded sub-corpus = `held-out` by default.** Held-out material is never tuned against;
>   a held-out→dev demotion happens only by explicit recorded Cowork/user decision (never silently).
> - Baseline measurements (Task B step 4) run on dev AND held-out alike (measurement ≠ tuning; the held-out
>   restriction binds fixes/calibration, not descriptive baselines).
> - Reminder from the gap-analysis ruling #9 (applies to anything you write): cite code by function/§ anchor, not
>   raw line number.

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\BUILD_AND_TEST.md`.
> Also read for this task: `cowork_score_census.md` (§3 criteria, §4 dedup rule, §5 tiers, §6 riders — the ratified
> census this instruction executes), `cowork_score_census_gt_draft.md` (the DLC table — your shopping list),
> `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md`, `tools/corpus_registry.json` + `tools/extra_scores_registry.json`.
>
> **Dispatch state: queued AFTER the E0 report** (same worktree, single CC — do not interleave with E0 work).
>
> **Current state:** gate baseline BIR **53/24/53** — **this instruction MUST NOT change it: no `src/` edit, no
> gate-corpus touch, the frozen Bach gate corpus (`tools/corpus/`, `tools/dcml/bach_chorales` etc.) stays
> byte-untouched.** All new material is **research-tier**. Clones land under the established gitignored locations;
> committed artifacts are only: registry files, validation scripts, REPRODUCIBILITY/score_inventory updates, and your
> report pointer. Commits local, unpushed, fork-only.
>
> **Bash rules (mandatory):** `; echo "exit:$?"` on every command; big output → file + `head`. Clones may be large —
> batch them and report per batch.

## 0. Purpose

Execute census §5 Tier G's first wave + §6 riders 1–2: **complete the Distant Listening Corpus container** (we use
11 of its 41 sub-corpora; onboard the rest), extend the registry to the census schema, and bank the zero-acquisition
cadence win (the cadence labels already inside our cloned DCML Mozart TSVs). Everything research-tier; the census's
"?" cells get closed with real counts; every [reported] census row you touch gets verified at source.

## 1. Task A — registry v2 (the schema change, one commit)

Extend `tools/corpus_registry.json` / `extra_scores_registry.json` (or introduce `tools/score_census_registry.json`
if cleaner — your call, declare it) to carry per source: `name, container, content, pieces (count), gt_type
(rn|chords|key|cadence|phrase|none), annotation_standard, score_format, alignment (score-aligned|chords-only|none),
license_class (PD|CC0|CC-BY|CC-BY-NC|unclear), distribution (committable|hash-pin-only), tier (G|J|C|S|X),
status (onboarded|pinned|recorded|rejected), provenance_url, pinned_commit, split (dev|held-out)`. The `split`
field implements the engage-criteria E2 held-out discipline (user, 2026-07-02): Cowork designates the dev/held-out
assignment per sub-corpus at revalidation-before-dispatch; held-out material is never tuned against and demotes to
dev only by explicit recorded decision. Populate v1 rows from the census
appendices for everything the project ALREADY uses + everything this instruction onboards. Census appendix tables are
the source of truth; where a row is [reported], verify at onboarding and correct.

## 2. Task B — onboard the missing DLC sub-corpora (the container completed)

From `cowork_score_census_gt_draft.md`'s verified 41-submodule list, onboard **every sub-corpus not already present**
(the present 11 are listed in `docs/score_inventory.md`). Per sub-corpus:
1. Clone under the established gitignored external-clone location; **hash-pin** (commit sha) in REPRODUCIBILITY.md +
   the registry (the C1-audit mechanism — license class recorded; NC/unclear = pin-only, never committed in-tree).
2. Record: piece/movement count (closing the census "?"), annotation-standard version (DCML harmony 2.x — note the
   exact version; version DRIFT between sub-corpora is a finding, not something to silently normalize), score format.
3. **Parse smoke-test:** run `dcml_parser` over its annotation TSVs; a sub-corpus that fails to parse is
   **QUARANTINED + reported** (format/version drift) — do NOT patch the parser this run.
4. **Baseline measurement (research-tier):** for parseable sub-corpora, run the export→`batch_analyze`→`compare_rn`
   chain (the `run_<corpus>_validation.py` pattern; add a script per sub-corpus or a generic driver — prefer ONE
   generic driver + a config table over 30 copied scripts, per the unification rule; declare your choice) and report
   per-corpus: root_agree / rn_agree (granularity-robust mode where runnable) as the FIRST per-style baselines.
   These numbers are descriptive — no target, no tuning, no gate.
5. **`wagner_overtures` specifically:** confirm whether the Tristan Prelude is included — report yes/no + the piece
   list (the review's stress-scenario want).

Batch order (report after each batch): (1) chromatic/romantic — beethoven_piano_sonatas, wagner_overtures,
liszt_pelerinage, rachmaninoff_piano, plus the other late-romantic sets; (2) pre-Baroque/Baroque-adjacent —
monteverdi, sweelinck, peri, frescobaldi, scarlatti_sonatas, couperin; (3) the remainder incl. bartok_bagatelles and
schulhoff_suite_dansante_en_jazz; (4) anything left. Disk/time overrun → stop at a batch boundary and report.

## 3. Task C — the free cadence win (read-only inventory, no metric wiring)

The DCML Mozart-sonatas TSVs we already have cloned carry **cadence labels**. Inventory them: which files/columns,
the label vocabulary (PAC/IAC/HC/DC/EC/PC per the DCML standard), the count per movement, and whether our
`dcml_parser` currently reads or drops them [code]. Deliver the inventory + a one-page proposal sketch (NOT an
implementation) for how they would ground an L5 §5.2 validation measure. Check the other already-cloned DCML
sub-corpora for the same columns while you are at it.

## 4. Deliverable + commits

`cc_corpus_wave1_report.md` (gitignored, HELD): §1 registry v2 (schema + row count); §2 per-batch onboarding table
(sub-corpus, pinned sha, pieces, standard version, parse OK/quarantined, baseline numbers); §3 Tristan answer; §4
cadence-label inventory; §5 census corrections (every [reported] row you verified/corrected); §6 quarantines +
Unknowns. End with the line count. **Commits (local, unpushed, fork-only):** Task A (registry v2 + docs) as one
commit; validation driver/scripts as one; REPRODUCIBILITY/score_inventory updates may ride either. Nothing under
`src/`; the Bach gate corpus untouched (verify with `git status` + `characterise_bir_false` reproducing 53/24/53
once at the end as the no-contamination proof).

## 5. Stop conditions

- Anything would touch the frozen gate corpus dirs or `src/` → STOP.
- `dcml_parser` fails on a sub-corpus → quarantine + report (no parser patching this run).
- License unclear → pin-only + flag; never commit content in-tree on a guess.
- Disk/time budget exceeded → finish the current batch, report, await next dispatch.

**On your report: Cowork re-reads this instruction, reads the report in full, verifies the pinned shas + registry
commit via committed objects, and spot-checks the baseline numbers before the census rows are marked onboarded.**
