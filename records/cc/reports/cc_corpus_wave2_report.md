# CC Corpus Wave 2 — the axis-2 annotation beds

> **Executes the user-ratified core scope of the "Corpus Wave 2" dispatch (2026-07-03):** onboard the three
> annotation/validation beds the targeted §6b sweep verified, serving the just-built axis 2 (voice leading) —
> VL-C validation, VL-E footing, VL-F footing — plus census/registry bookkeeping and the standing re-discovery
> trigger check. **HEAD at run: `4c6952de18`.** This wave changed **no `src/`** and **no gate corpus**; the gate
> reproduces byte-for-byte (§6). Tools/registry/census only, exactly as scoped. **Out of scope (Wave 3):** Tier J
> and the Tier G/S remainder.

---

## 0. Headline

- **Three beds cloned + hash-pinned under a new gitignored `corpora/annot/` subtree** (kept deliberately separate
  from the idiom-discovery inputs in `corpora/ship|expl/`). All three are **research-tier, hash-pin-only, held-out**
  (never tuned against) — label layers over scores, not analysis/gate corpora.
- **Every paper-claim verified at the cloned data.** Two matched exactly (texture 1,164 labels; schema
  structure 10 types / 20 subtypes / 54 movements); **one benign mismatch reported, not silently accepted** —
  the schema dataset has **273** true instances at the pin vs the 2020 paper's **244** (a living repo grown since
  publication; structure otherwise matches — §1).
- **Registry v2 gains a minimal additive `annotation_beds` section** (3 entries, `kind="annotation-bed"`); the 40
  DLC + 16 other_sources rows are byte-identical. **Census §1** marks the DCMLab-org schema bed + the Essen folk
  bed and adds an enumerated **algomus/Dezrann** row (moved up from §7 residual risk).
- **Re-discovery trigger: NOT fired** — confirmed by inventory, not merely asserted (§5).
- **No-contamination proof holds:** nothing under `src/`; the frozen gate corpus is byte-untouched; the gate
  reproduces **53 / 24 / 53**, case-identity set-diff **empty both directions**, all three presets (§6).

Pinned commits (source of truth = `tools/score_census_registry.json → annotation_beds[].pinned_commit`,
read live from the clones):

| bed | repo | pin | axis-2 role |
|---|---|---|---|
| schema_annotation_data | `github.com/DCMLab/schema_annotation_data` | `76f810a1a5522fc599f389ffae0c6a0c5cf94b5c` | VL-F footing |
| symbolic-texture-dataset | `gitlab.com/algomus.fr/symbolic-texture-dataset` | `3dce4ab8cff8c50d540783ec435480551a1d71c6` | VL-C validation |
| essen-folksong-collection | `github.com/ccarh/essen-folksong-collection` | `2d0ca75e87dc7a725556c8090e3681c1fa3a0452` | VL-E footing |

---

## 1. Task 1 — the schema-annotation bed (VL-F footing)

**Source:** `github.com/DCMLab/schema_annotation_data` (Finkensiep, Déguernel, Neuwirth & Rohrmeier, ISMIR 2020),
pinned `76f810a1a5522fc599f389ffae0c6a0c5cf94b5c` (branch `master` HEAD at clone).

**Paper-claim verification (measured at the pin, `scratchpad/count_schema.py`):**

| claim (§6b / paper) | measured at pin | verdict |
|---|---|---|
| 18 Mozart sonatas / **54 movements** | 54 (`mscore`/`musicxml`/`notelist` = 54 each) | ✅ match |
| **10 schema types / 20 subtypes** | 10 base types with ≥1 instance / **20 non-empty subtype dirs** | ✅ match (25 dirs total; `folia`,`grandcad` + several fenaroli variants empty at pin) |
| Do-Re-Mi 5 | doremi 5 | ✅ match |
| Prinner 32 | prinner **33** | ⚠ +1 |
| Fonte 49 (+2 +8 variants) | fonte.2 **51**, .flipped 2, .majmaj 8 (base 61) | ⚠ +2 on .2 |
| Quiescenza 46 (+6) | quiescenza.2 **47**, .diatonic 6 (base 53) | ⚠ +1 on .2 |
| **244 total true instances** | **273** | ⚠ +29 |

**Mismatch reported (not a STOP):** the total is **273 vs 244** (and small per-type upward drifts). This is a
**living-repo growth past the 2020 paper snapshot**, not a contradiction of the §6b record: the corpus (Mozart
sonatas we already hold), the 10-type / 20-subtype *structure*, and the 54-movement span all confirm §6b exactly;
only the instance *counts* grew (chiefly `fenaroli.2.flipped` = 49). The repo's own `doc/Internal.md` states no
authoritative total (no "244"/"273" in any text file), consistent with a curated, still-growing dataset. Per the
dispatch ("report any mismatch, do not silently accept") this is **reported**; the STOP condition ("content
contradicts the §6b record") is **not** met — a +29 superset with intact type structure is corroboration-with-drift,
not a wrong corpus. The pinned commit makes 273 reproducible.

**License:** **no LICENSE file anywhere in the repo** → `license_class = unclear` (DCMLab org states CC BY-NC-SA
[reported]). Hash-pin-only regardless (the established C1 mechanism; the clone is gitignored, never redistributed).

**Alignment note (document only — built nothing):** annotations are nested note-ID lists (e.g.
`[["note455","note469"],…]`) keyed to **repo-local note IDs** (`noteN`) that the repo's own tooling
(`tools/add_ids.py`) assigns to the repo's own `musicxml/*.xml`, generated from its own `mscore/*.mscx` sources;
`notelist/*.json` is the concordance (pitch `p` + onset/offset) resolving each ID (verified: `note455`/`note511`
resolve into `K279-1`'s 4090-entry notelist). The scores are the **same 18 Mozart sonatas / 54 movements** as DCML
`mozart_piano_sonatas` (identical `K279-1 … K576-3` filenames), but a **distinct, self-contained encoding** with a
repo-local ID scheme independent of the DCML MS3 `.mscx` + `harmonies` TSVs. To use with our DCML clones one would
either (a) consume the repo's bundled scores directly (recommended — it ships scores + notelists + annotations, no
external dependency) or (b) re-derive note IDs on the DCML `.mscx` via an equivalent id-assignment pipeline and
match by onset+pitch. Whether the bundled MuseScore edition is byte-identical to the DCML edition is **not
established** and not required — the bundle is self-contained.

---

## 2. Task 2 — the per-bar texture-annotation bed (VL-C validation + spec §15-1 reference)

**Source located from `algomus.fr/code`:** the annotation repo is `gitlab.com/algomus.fr/symbolic-texture-dataset`
(Couturier, Bigo & Levé, ISMIR 2022, **v1.1**, DOI 10.5281/zenodo.7316712), pinned
`3dce4ab8cff8c50d540783ec435480551a1d71c6` (branch `main`).

**Paper-claim verification (measured at the pin):**

| claim (§6b / paper) | measured at pin | verdict |
|---|---|---|
| **9 movements** (K.279/K.280/K.283, all 3 mvts each) | K279-1/2/3, K280-1/2/3, K283-1/2/3 in `dataset/{txt,tsv,dez}/` | ✅ match |
| **1,164 bar-level labels** | **1,164** TSV data rows (= unique measure numbers; one row per bar) | ✅ exact |
| 1,357 configurations | consistent (extra configs come from the `,` sequential-separation flag within a bar) | ✅ consistent |
| syntax: M/H/S functions, density, diversity, h/p/o elements | `dataset/tsv/README.md` columns: `M`/`H`/`S` functions + `h`/`p`/`o` motion elements (+ `h+`,`p+`,`s`,`t`,`b`,`r`,`_`,`,`); label string encodes density/diversity | ✅ match |
| 62 bar-level texture descriptors | README §"Discover the descriptors": 62, in `descriptors/descriptors.py` (`generatedescriptors.py`) | ✅ match |

**Target-score identity confirmed:** the TSV `mn` column is defined verbatim from the **DCML Annotated Mozart
Sonatas (Hentschel et al. 2021)** measure-numbering convention (cited in `dataset/tsv/README.md`), and the README
instructs cloning `github.com/DCMLab/mozart_piano_sonatas` as the score input for descriptor generation. Annotations
are therefore keyed by **(K-identifier, bar `mn`)** and **align directly to the DCML `mozart_piano_sonatas` we
already hold** (`tools/dcml/mozart_piano_sonatas`, also `corpora/expl/dcml_mozart`) — no re-encoding needed for the
labels. **Caveat (documented):** the paper extracted its *descriptors* against the **v1.0** release of DCML mozart;
our pin (`5337257…`) may differ from that tag — this affects descriptor *recomputation* only, not the measure-keyed
annotation labels.

**Descriptor-code repo:** **bundled in the dataset repo** (`descriptors/`, `descriptors.py`,
`generatedescriptors.py`) — the dispatch's condition "if it is a separate small repo" is **not met**, so no separate
clone was made. The related repos `gitlab.com/algomus.fr/texture` (2021), `.../comparing-texture` (2023 follow-up),
and `gitlab.com/pythouille/smc22-symbolic-texture-piano` (SMC 2022 syntax) are **recorded as tooling-reference, not
cloned** (not our tooling).

**License:** explicit dual license — **GPLv3 (code) + ODbL-1.0 (data)** (`LICENSE` = GPLv3; README badges + Zenodo
record state ODbL for the data). The most permissive of the three beds; still **hash-pin-only** here (consistent
mechanism, under gitignored `corpora/annot/`).

---

## 3. Task 3 — the Essen phrase-boundary bed (VL-E footing)

**Source chosen (documented):** `github.com/ccarh/essen-folksong-collection` — CCARH's Humdrum **kern edition
(assembled by Helmut Schaffrath; kern version prepared by David Huron), pinned
`2d0ca75e87dc7a725556c8090e3681c1fa3a0452` (branch `main`). **Choice rationale:** a Git repo cloneable + hash-pinnable
like the others (the dispatch's preferred form), from CCARH — the collection's official distributor — avoiding
loose-file vendoring of the EsAC distributions. No STOP: a pinnable source exists.

**Inventory (measured at the pin):**

| item | measured |
|---|---|
| total `.krn` files | **8,473** (all regions) |
| europa subset | **6,213** (≈ the literature ≈6,236 European figure; small edition variance) |
| other regions | asia 2,246 (largely Chinese), america 13, africa 1 |
| phrase-mark encoding | Humdrum kern phrase tokens **`{`** (open) / **`}`** (close), attached inline to notes |
| phrase coverage | **100%** of europa files carry `{`; **36,094** phrase-open tokens (europa) |
| texture | single-spine `**kern` (1 kern spine, 0 `**harm` spines) — monophonic |

**Coverage caveat (recorded verbatim per the dispatch):** *monophonic folk melodies — a single-line vocal bed for
the per-voice phrase task, not usable for motion profiles (no voice pairs) nor for the harmonic idiom pipeline (no
chord symbols).* Verified: the kern files are single-spine monophonic melodies with no chord symbols.

**License:** **CCARH MuseData license** (`license.txt`) — restrictive **non-commercial**: "does not authorize the use
of the enclosed MuseData files in the production of derivative editions intended for commercial distribution, nor for
public performance … nor for sound recording." Recorded `license_class = CCARH-MuseData-NC`. **Not a STOP:** the
license grants a nonexclusive *use* license; a local, gitignored, never-redistributed research clone (hash-pin-only)
is within it. Flagged prominently so it is never committed in-tree or redistributed.

---

## 4. Task 4 — census + registry bookkeeping

**Registry (`tools/score_census_registry.json`, generated by `tools/build_score_census_registry.py`):** added a new
**`annotation_beds`** array (3 entries) — the **smallest additive schema change**: a new top-level section parallel
to `distant_listening_corpus` / `other_sources`, so the existing **40 DLC + 16 other_sources rows are byte-identical**
(the JSON diff is only the `_notes` enum line + the appended section). Each bed carries the registry-v2 base fields
plus four bed-specific ones — **`kind="annotation-bed"`**, `axis2_role`, `target_corpus`, `label_count` — and
`tier=C`, `split=held-out`, `distribution=hash-pin-only`, verified `label_count`, and a per-bed `license_class`
(`unclear` / `ODbL-1.0 (data) + GPLv3 (code)` / `CCARH-MuseData-NC`). `gt_type` carries the bed-native layer
(`schema` / `texture` / `phrase`); the `_notes` enum documentation was extended accordingly. **Regeneration is
deterministic** (`build_score_census_registry.py` → `DLC=40 other=16 beds=3 total=59`; two consecutive runs
byte-identical; shas read live from the clones so the file never drifts from disk).

**Census (`cowork_score_census.md` §1):** surgical additions only (no rewrite) —
(a) the **DCMLab-org** row now names `schema_annotation_data` and carries a `[Wave-2 ONBOARDED … annotation bed]`
marker; (b) the **folk-containers** row (which already named Essen) carries a Wave-2 Essen-bed marker; (c) a **new
enumerated `algomus / Dezrann` row** was added and the §7 residual-risk mention updated to note it is now enumerated
(with `symbolic-texture-dataset` onboarded at Wave 2). Each new marker cites this report as provenance.

**Provenance surface** (all committed; the clones themselves are gitignored/hash-pin-only): pins live in the
committed registry (`provenance_url` + `pinned_commit`) and in a new `corpora/annot/` section of
`tools/REPRODUCIBILITY.md` (clone + checkout commands); `docs/score_inventory.md` gains a `corpora/annot/`
subsection distinguishing these beds from the idiom-discovery inputs.

---

## 5. Task 5 — the idiom re-discovery trigger check (checked, not run)

**Trigger: NOT fired.** The trigger fires on a *material change to the discovery-input corpora*
(`corpora/ship|expl/` + `idiom_discovery/`). Confirmed by inventory, not assertion:

- **Tasks 1–2 add labels over scores already in the discovery corpus.** Both the schema and texture beds annotate
  the **Mozart piano sonatas**, which are already a discovery input (`corpora/expl/dcml_mozart` is present; also
  `tools/dcml/mozart_piano_sonatas`). No new scores enter the discovery input; label layers are orthogonal to the
  feature streams the discovery consumes (chord symbols / note streams). The scores themselves were not modified.
- **Task 3 adds material outside both discovery views.** Essen is monophonic `**kern` with **no chord symbols**
  (→ no harmonic view) and **no voice pairs** (→ no voice-pair motion view), so it cannot be a discovery input.
- **All three clones went into a new, separate `corpora/annot/` subtree;** `corpora/ship|expl/` and
  `idiom_discovery/` are byte-untouched.

The expectation is therefore **confirmed, not contradicted** — no STOP, and the re-discovery run (its own protocol
and dispatch) is not triggered.

---

## 6. Acceptance — no-contamination proof + discipline

**No `src/`, gate corpus byte-untouched.** `git status` shows only the five files this wave authored
(`cowork_score_census.md`, `docs/score_inventory.md`, `tools/REPRODUCIBILITY.md`,
`tools/build_score_census_registry.py`, `tools/score_census_registry.json`) plus the (pre-existing, untouched)
`STATUS.md` / `COWORK_HANDOFF.md` edits which were **excluded** from every commit. No path under `src/` changed; no
path under `tools/corpus/` changed. All bed clones are gitignored (`git check-ignore` confirms all three;
`git status --porcelain corpora/annot` empty).

**Gate reproduction (`characterise_bir_false.py --corpus-dir tools/corpus/{baroque,jazz,default}`, each "Processed
352 scores (326 with WiR coverage)"):**

| preset | count | case-identity set-diff vs CLAUDE.md |
|---|---|---|
| Baroque | **53** | EMPTY both directions ✅ |
| Jazz | **24** | EMPTY both directions ✅ |
| Default | **53** | EMPTY both directions ✅ |

Set-diff computed by parsing each run's "Full BIR=false enumeration (all N cases)" block into `stem@tick`
identities and diffing against the authoritative CLAUDE.md sets (`scratchpad/gate_setdiff.py`): **`missing` and
`extra` both empty for all three presets**. The gate is byte-untouched.

**Held-out discipline:** all three beds are `split=held-out` validation material; nothing here creates or touches
any held-out *designation change* and nothing is tuned against — they are validation beds by construction.

**Reuse-vs-new + what retires.**
- **Reused verbatim:** the clone + `git checkout <pin>` mechanism; the gitignored-tree hash-pin-only convention
  (`.git/info/exclude → /corpora/`); the deterministic registry generator + registry-v2 schema; the census §1
  container-enumeration form; `characterise_bir_false.py` as the gate-reproduction oracle.
- **New (minimal):** the `corpora/annot/` subtree (under the already-excluded `/corpora/`); the registry
  `annotation_beds` section + `kind`/`axis2_role`/`target_corpus`/`label_count` fields + `annotation_bed_rows()` in
  the generator; three census markers + one enumerated algomus/Dezrann row; a `corpora/annot/` section in
  REPRODUCIBILITY.md + score_inventory.md.
- **Retires:** nothing.

---

## 7. STOP conditions — none tripped

Checked each: source availability (all three cloned cleanly); content vs §6b (schema total drift is a benign
superset with intact structure — **reported**, not a contradiction; §1); license forbidding hash-pin mirroring
(none — CCARH/DCML/ODbL all permit a local gitignored research clone); alignment documentability (schema =
self-contained repo-local IDs; texture = (K-id, `mn`) to DCML mozart; both precisely documented); the Task-5
expectation (confirmed, not contradicted); `src/` or gate-corpus touch (none). No condition met.

---

## 8. Commits (local, unpushed, fork-only)

Per the dispatch's suggested split. `git add` used explicit paths only — the pre-existing `STATUS.md` /
`COWORK_HANDOFF.md` edits were never staged.

| # | scope | SHA | files |
|---|---|---|---|
| 1 | clones + pins provenance | `36391978a0` | `tools/REPRODUCIBILITY.md`, `docs/score_inventory.md` |
| 2 | registry + census | `ad04f3f7c8` | `tools/build_score_census_registry.py`, `tools/score_census_registry.json`, `cowork_score_census.md` |
| 3 | this report | (recorded on commit; force-added per the `/cc_*.md` gitignore convention) | `cc_corpus_wave2_report.md` |

Nothing pushed; `upstream` push remains disabled; fork (`origin = slimvince/MuseScore`) only.
