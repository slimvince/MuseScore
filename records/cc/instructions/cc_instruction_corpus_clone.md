# CC Instruction: clone the GitHub corpora for the idiom-discovery study

## Context

A read-only data-gathering chore for the harmonic-idiom-discovery work (`cowork_idiom_discovery_design.md`,
`cowork_style_clustering_plan.md` §4). Clone the public dataset repos into `C:\s\MS\corpora\`, **kept out of the
MuseScore repo's git tracking**. This touches **no** `src/`, no build, no tests — it only populates a data folder.

The licensing split matters (plan §5): **ship/** = permissive enough to feed shipped weights; **expl/** = non-commercial
/ restricted → exploration / cluster-deciding only. Keep them in separate subfolders so the distinction is structural.

---

## Step 0 — folder + local gitignore (do NOT pollute the MuseScore repo)

`C:\s\MS\` is the MuseScore fork's working tree. Cloning datasets inside it would nest git repos and flood
`git status`. Prevent that **without** modifying any tracked file:

```
mkdir -p C:\s\MS\corpora\ship C:\s\MS\corpora\expl
# local-only ignore (NOT the tracked .gitignore — no commit, no repo change):
printf '\n/corpora/\n' >> C:\s\MS\.git\info\exclude
```

Confirm `git -C C:\s\MS status` does **not** show `corpora/` after cloning. If it does, stop and report.

---

## Step 1 — clone the [ship] (permissive) repos → `corpora\ship\`

```
cd C:\s\MS\corpora\ship
git clone https://github.com/smashub/choco                 choco              # ChoCo aggregator (mostly CC-BY); large
git clone https://github.com/jukedeck/nottingham-dataset   nottingham         # folk, ABC melody+chords
git clone https://github.com/DCMLab/lda_tpcs               lda_tpcs           # Moss method reference (MIT) — not a corpus
```

## Step 2 — clone the [expl] (non-commercial / restricted) repos → `corpora\expl\`

```
cd C:\s\MS\corpora\expl
git clone https://github.com/DCMLab/JazzHarmonyTreebank    jazz_harmony_treebank   # jazz (treebank.json)
git clone https://github.com/DCMLab/mozart_piano_sonatas   dcml_mozart             # classical + RN GT
git clone https://github.com/DCMLab/ABC                    dcml_beethoven          # Annotated Beethoven Corpus
git clone https://github.com/DCMLab/romantic_piano_corpus  dcml_romantic
git clone https://github.com/DCMLab/scarlatti_sonatas      dcml_scarlatti
git clone https://github.com/wayne391/lead-sheet-dataset   hooktheory_hlsd         # pop/rock, melody+chord+key+function
git clone https://github.com/music-x-lab/POP909-Dataset    pop909                  # pop, MIDI + chord .txt
```

---

## Step 3 — git-LFS check

Some DCML / ChoCo repos may store scores (`.mscx`/`.mscz`) or JAMS via **git-LFS**. After cloning, in each repo
that looks LFS-backed (tiny files that are pointer stubs), run:

```
git lfs install ; git lfs pull
```

Install `git-lfs` first if absent. Flag any repo where this was needed.

---

## Step 4 — report

For each repo: clone success/fail, the on-disk size (`du -sh`), and the top-level file types (so we know whether the
harmony is chord-symbols, TSV, MIDI, or scores). Specifically flag:
- any repo that **404s** (a name may have changed — report it, don't guess a replacement);
- any that needed **LFS**;
- `corpora/` correctly **absent from `git status`** in the MuseScore repo.

**Do not** add any of these as git submodules, do not commit them, do not touch `src/` or the MuseScore tree, do not
push anything.

---

## NOT in this task (non-GitHub — the user will fetch these)

- **McGill Billboard** (CC0, pop, → `corpora\ship\`): direct download from
  `https://ddmal.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/`.
- **iRealPro corpus** (broader jazz, [expl], → `corpora\expl\`): Zenodo `https://zenodo.org/record/3546040`.

---

## Follow-up (2026-06-30) — fetch the FULL Hooktheory HLSD (the clone is only a sample)

**★ UPDATED — the Google Drive route is DEAD.** CC verified (2026-06-30): the README's 4.9 GB Drive id
`13iB5Brk1hypKsw9TSf8_d4Ka3xU0XmFZ` is a hard 404 (privatized); every research mirror points back to it; the 2018
crawler is dead (Hooktheory is now a gated SPA). **Do not retry the Drive link.**

**Live route — HuggingFace `m-a-p/HookTheory` (CC-BY-NC-4.0, gated → needs the user's HF token after approval):**
the symbolic harmony is just `Hooktheory.json.gz` (~20 MB) + `Hooktheory_Raw.json.gz` (~96 MB) + the Key/Structure
`.jsonl` splits (the 112 GB is audio — skip). When access is granted:
```
pip install -U "huggingface_hub[cli]"
export HF_TOKEN=<the user's token>
cd C:\s\MS\corpora\expl
huggingface-cli download m-a-p/HookTheory Hooktheory.json.gz Hooktheory_Raw.json.gz \
    --repo-type dataset --local-dir hooktheory_hf
```
Keep under `expl/` (CC-BY-NC). Report the section count (target ~18,843) and the JSON schema. Layout is m-a-p
keyed-JSON (Cowork parses it directly). Provenance saved to memory `project_hlsd_full_pending_hf`.

## Note — the `corpora\expl\` DCML clones are redundant with `tools\dcml\`

`tools\dcml\` already holds the DCML RN corpora (bach_chorales, corelli, cpe_bach_keyboard, when_in_rome, mozart, ABC,
chopin, grieg, schumann, dvorak, tchaikovsky — see `docs/score_inventory.md`). The `corpora\expl\dcml_{mozart,
beethoven,romantic}` clones **duplicate** it; only `dcml_scarlatti` is genuinely new. Harmless — no action required —
but the pipeline will read classical from `tools\dcml\` (richer); the redundant clones may be deleted to save space.

