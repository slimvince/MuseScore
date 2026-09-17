# CC Instruction: commit the idiom-discovery session (pipeline + docs), fork-only

## Pre-reading
Read `C:\s\MS\CLAUDE.md`. This is a **docs + research-tooling** commit — **no `src/`, no build, no tests, no corpus
measurement**. The discovery pipeline is a standalone research tool under `idiom_discovery/`; it does not touch the
composing module.

## Step 0 — reconcile (HARD STOP if a source/build file is dirty)
```
git status -s; echo "exit:$?"
```
Expected untracked/modified set is **docs + the `idiom_discovery/` pipeline + this session's `cc_instruction_*.md`**.
**STOP and report** if `git status` shows any change under `src/`, `muse/`, `tools/` `.cpp`/`.h`/`_tests.*`, or any
build artifact — this session changed none of those. `corpora/` must **not** appear (it's locally git-ignored via
`.git/info/exclude`); if it does, stop.

Expected members (reconcile against `git status` — report any mismatch, don't silently add/omit):
- **`idiom_discovery/`** — the pipeline: `model.py`, `parsers/` (dcml, jht, mcgill, choco, bach_chordify, improvisor,
  chordonomicon, voiceleading), `extract.py`, `discover.py`, `run_discovery.py`, `build_full.py`, plus the
  exploratory scratch scripts and `discovery_report.md` (the generated run report — fine to keep as a record).
- **Docs (new/modified):** `cowork_idiom_discovery_design.md`, `cowork_idiom_discovery_findings.md`,
  `cowork_style_taxonomy_proposal.md`, `cowork_idiom_entry_mapping.md`, `cowork_upstream_merge_risk.md`, and the
  modified `cowork_style_clustering_plan.md`.
- **CC instructions (this session):** `cc_instruction_{vocabulary_build, corpus_clone, run_discovery,
  rerun_discovery, convert_curated_scores, fetch_more_scores, commit_idiom_work}.md` (+ any other `cc_instruction_*`
  created this session).

## Step 1 — STATUS entry
Prepend a new top entry to `STATUS.md` (the living doc), demoting the current top to "Previous:". Suggested text
(adjust to house style; fill the commit hash after committing):

> *Last updated: 2026-06-30 (session 19 — **HARMONIC IDIOM DISCOVERY (Cowork research track) — empirical
> cross-tradition study COMPLETE: 5 ratified harmonic idioms + voice-leading confirmed as a 2nd, orthogonal axis;
> docs + standalone `idiom_discovery/` pipeline; NO src/build/test change**) — A research-track session: a from-scratch
> unsupervised discovery of harmonic structure across ~9,400 lead-sheet+score pieces (DCML, JHT, ChoCo's 18 sources
> incl. weimar/jaah/jazz-corpus/wikifonia, McGill, Nottingham, iRealPro, Impro-Visor, Chordonomicon, music21 Bach
> chordify, the curated Steely Dan/Piazzolla/Hiromi). **Result (cap-robust, ARI≈0.16 — genre is a weak organizer):
> FIVE structural progression idioms** — Diatonic-functional, Chromatic-functional, Seventh-functional, Triadic-modal,
> Chromatic-coloristic — **+ mode & chromaticism cross-axes**; the harmonically dense genre-defying corpora all
> converge on the cross-cutting Chromatic-coloristic idiom; Baroque/galant/Classical share ONE idiom (era ≠ axis); the
> candidate 6th (modal/static jazz) is not separable at K=6. **Voice-leading pilot: a confirmed 2nd orthogonal axis**
> (chorale-vs-piano ARI 0.68; chorales separate by part-writing, not chords). Ratified the idiom names + the
> idioms-as-tags / presets-as-idiom-weightings model (`cowork_style_taxonomy_proposal.md`,
> `cowork_idiom_entry_mapping.md`). **Next (separate steps):** the StyleTag swap in `harmonicvocabulary` (per the
> entry-mapping), the fuller voice-leading-idiom discovery, and instrumentation as a context prior. **Commit:** the
> `idiom_discovery/` pipeline + the docs (this commit), fork-only.*

## Step 2 — one commit, push fork-only
```
git add idiom_discovery/ cowork_idiom_discovery_design.md cowork_idiom_discovery_findings.md \
        cowork_style_taxonomy_proposal.md cowork_idiom_entry_mapping.md cowork_upstream_merge_risk.md \
        cowork_style_clustering_plan.md STATUS.md cc_instruction_*.md
#  (reconcile the exact list against `git status` first)
git commit -m "research(idiom-discovery): cross-tradition harmonic idiom study — 5 idioms + voice-leading axis; pipeline + docs"; echo "exit:$?"
git push origin HEAD; echo "exit:$?"
```

**★ FORK-ONLY HARD STOP:** push to `origin` (`slimvince/MuseScore`) only — **never** `upstream`
(`musescore/MuseScore`). If a push would target `upstream`, or `origin` resolves to `musescore/MuseScore`, STOP.

## After
`git log --oneline -3` — report the hash + that the push reached `origin` only. Do not run a build or tests
(nothing compiled changed).
