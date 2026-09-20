# CC Corpus-Hygiene Report — remove stray non-chorale `corelli.xml` from the chorale gate

> **Filename note:** the instruction asked for `cc_corpus_hygiene_report.md`, but that name was **already
> taken** by a substantive, unrelated prior report (the 2026-06-11 corpus audit C1–C4, base `9e52147b04`).
> I did **not** overwrite it; this report uses the distinct name `cc_corpus_hygiene_report_corelli.md`
> (also gitignored via `/cc_*.md`). Note: that prior report independently corroborates the central finding
> here — *"of 353 stems, 326 resolve to a When-in-Rome `analysis.txt`, 27 uncovered."*

**Date:** 2026-06-30  
**Branch:** master  
**Repo HEAD:** `c932e867bb` (unchanged — no commit made; see §4)  
**Scope:** corpus data only — no `src/` / `tools/` code touched, no threshold/inference change.  
**Result headline:** removal is **gate-neutral** — Baroque 53 / Jazz 24 / Default 53 **unchanged**, all
case-identity sets byte-identical, the 352 `bwv*` `.ours.json` byte-identical pre/post. corelli was an
**unregistered, gitignored, gate-non-contributing** orphan (no WiR/DCML coverage).

---

## §1 — Investigation findings (read-only, performed before any change)

### Is `corelli.xml` in `tools/corpus/` and in the gate glob?
**Yes.** Single file `tools/corpus/corelli.xml` (97,097 bytes, dated Apr 21), a **non-chorale Corelli
trio-sonata movement** (its `.ours.json` carries `"source": "corelli.xml"`; the repo's separate
`corelli_trio_sonatas` DCML corpus lives under `tools/dcml/corelli/MS3/op01n08*.mscx`).

The gate glob is `run_bach_preset.py`'s `corpus_dir.glob("*.xml")` over flat `tools/corpus/`. Pre-removal that
glob yielded **353 `.xml` = 352 `bwv*` chorales + 1 `corelli.xml`**. So "353" was **inclusive** of corelli —
corelli was the **353rd** member (352 chorales + corelli), **not** a 354th file. `run_bach_preset.py` derives
`expected_count` from the live glob (`expected_count=total`, line ~489), so removal cleanly drops it to 352.

### Is it scored?
**Scored by `batch_analyze`, but NOT by the gate.**
- It had a matched music21 GT (`corelli.music21.json`) and a produced `corelli.ours.json` in **every**
  per-preset dir, and was a member of each `corpus_manifest.json` (`expected_count: 353`, status `OK`).
- **But it has NO WiR/DCML coverage.** `characterise_bir_false.py` only admits a case that
  `dcml.find_wir_file()` resolves (line ~146). Pre-removal the tool reported
  **"Processed 353 scores (326 with WiR coverage)"** — corelli was one of the **27** non-WiR scores, so it
  **structurally cannot** produce a BIR=false case. Post-removal: **"352 scores (326 with WiR coverage)"** —
  the WiR count **held at 326**, confirming corelli was never among the gate's scored set.

### Is it registered?
**No** (in tracked files). `git ls-files tools/corpus` = **0** — all of `/tools/corpus/` is gitignored
(`.gitignore:26`). The `corelli` hits in `tools/corpus_registry.json` and `docs/score_inventory.md` all refer
to the **separate `corelli_trio_sonatas` DCML corpus** (`corelli/MS3/op01n08*.mscx`, `tools/reports/corelli_*`
ours_dirs) — **none** reference the stray flat `tools/corpus/corelli.xml`. The only place it was "registered"
was the **gitignored** per-preset `corpus_manifest.json` (a generated artifact).

### Predicted gate effect — confirmed before changing anything
**Byte-identical.** Pre-removal measurement of the existing (git `4f63d2ab40`) dirs reproduced CLAUDE.md
exactly: Baroque **53**, Jazz **24**, Default **53**; every documented `stem@tick` identity verified
element-by-element; **corelli appeared in 0 BIR=false lines** on all three presets. → corelli is genuinely
**not** contributing a BIR identity. Per §1's branch this is **safe to clean** (no Cowork ruling required;
not a gate change).

---

## §2 — Cleanup performed (corpus data only)

Removed (all gitignored / untracked — no `git diff`):
- Flat source: `tools/corpus/corelli.xml`, `tools/corpus/corelli.music21.json`
- Active gate dirs: `corelli.music21.json` + `corelli.ours.json` from each of
  `tools/corpus/{baroque,jazz,default}/`

Then regenerated all three active presets with `run_bach_preset.py` (per CLAUDE.md), which clean-slated and
re-stamped each manifest at **352/352 complete**:

| preset | expected | ours | complete | corelli in manifest | git_hash |
|---|---|---|---|---|---|
| baroque | 352 | 352 | true | false | `c932e867bb` |
| jazz | 352 | 352 | true | false | `c932e867bb` |
| default | 352 | 352 | true | false | `c932e867bb` |

Flat `tools/corpus/*.xml` is now **352 (all `bwv*`)**; no `corelli*` remains in the flat dir or the three
active gate dirs. **No `src/` / `tools/` code touched. No registry/inventory edit** — the tracked registries
reference only the separate `corelli_trio_sonatas` corpus, which is correct and was left intact.

---

## §3 — Re-confirmed + attributed baseline

**Attribution: removal byte-identical — corelli was a gate-non-contributing (no-WiR), unregistered orphan;
sets unchanged 53 / 24 / 53.**

Two independent proofs the only change is corelli's removal:
1. **bwv output byte-identity.** The 352 `bwv*` `.ours.json` sha256 fingerprints are **identical** pre vs post
   in all three presets. (The corpus had been generated at ancestor `4f63d2ab40`; HEAD is `c932e867bb`, the
   intervening commits being "dormant, byte-identical" L5 work. The HEAD rebuild reproduced every bwv output
   exactly, **empirically ruling out** any binary-drift confound and confirming the dormant L5 work is inert
   for batch output.)
2. **Identity-set stability.** `characterise_bir_false.py` post-removal, diff-clean vs the pre-removal sets:

- **Baroque = 53** (UNCHANGED):
  `bwv10.7@36000 bwv14.5@8160 bwv144.6@15360 bwv144.6@16320 bwv151.5@13440 bwv153.1@18240 bwv16.6@16800
  bwv169.7@24960 bwv17.7@46080 bwv174.5@6240 bwv20.11@13440 bwv244.32@5760 bwv244.46@960 bwv245.15@13920
  bwv245.17@4800 bwv245.3@12480 bwv245.37@13920 bwv245.40@51360 bwv258@10560 bwv261@33840 bwv269@20640
  bwv272@4320 bwv272@4800 bwv272@8160 bwv282@9120 bwv289@20160 bwv289@21600 bwv300@13440 bwv309@8640
  bwv320@31680 bwv334@5280 bwv334@6720 bwv342@25440 bwv352@1440 bwv358@6000 bwv364@2880 bwv392@14400
  bwv40.3@2400 bwv402@22080 bwv416@10080 bwv421@2880 bwv422@23040 bwv423@28320 bwv429@24240 bwv432@5520
  bwv45.7@20160 bwv48.3@2880 bwv57.8@15360 bwv60.5@30960 bwv64.8@5280 bwv77.6@22080 bwv94.8@24960
  bwv96.6@13440`
- **Jazz = 24** (UNCHANGED):
  `bwv144.6@15360 bwv144.6@16320 bwv245.15@13920 bwv245.17@4800 bwv245.37@13920 bwv245.40@51360 bwv272@4320
  bwv272@8160 bwv280@17280 bwv282@9120 bwv291@17760 bwv301@1440 bwv313@14880 bwv334@5280 bwv342@25440
  bwv392@14400 bwv422@23040 bwv429@24240 bwv432@5520 bwv45.7@20160 bwv48.3@2880 bwv64.8@5280 bwv74.8@13440
  bwv74.8@13920`
- **Default = 53** (= Baroque-53 with `{bwv352@1440, bwv60.5@30960}` → `{bwv227.7@18000, bwv387@10560}`, as
  documented in CLAUDE.md):
  `bwv10.7@36000 bwv14.5@8160 bwv144.6@15360 bwv144.6@16320 bwv151.5@13440 bwv153.1@18240 bwv16.6@16800
  bwv169.7@24960 bwv17.7@46080 bwv174.5@6240 bwv20.11@13440 bwv227.7@18000 bwv244.32@5760 bwv244.46@960
  bwv245.15@13920 bwv245.17@4800 bwv245.3@12480 bwv245.37@13920 bwv245.40@51360 bwv258@10560 bwv261@33840
  bwv269@20640 bwv272@4320 bwv272@4800 bwv272@8160 bwv282@9120 bwv289@20160 bwv289@21600 bwv300@13440
  bwv309@8640 bwv320@31680 bwv334@5280 bwv334@6720 bwv342@25440 bwv358@6000 bwv364@2880 bwv387@10560
  bwv392@14400 bwv40.3@2400 bwv402@22080 bwv416@10080 bwv421@2880 bwv422@23040 bwv423@28320 bwv429@24240
  bwv432@5520 bwv45.7@20160 bwv48.3@2880 bwv57.8@15360 bwv64.8@5280 bwv77.6@22080 bwv94.8@24960 bwv96.6@13440`

**The case-identity set is the gate, and it is unchanged on all three presets.**

---

## Declarations (no action taken — for L6 / Cowork)

1. **`bwv112.5` fermata edge.** `bwv112.5` is present in the now-352 corpus. Per the instruction it is the one
   chorale of the set **without a fermata** — a 1-stem edge for the fermata-phrase oracle. **Declared, not
   acted on** (whether/how to handle it is an L6-design decision, not a hygiene fix).

2. **44 historical/experiment corpus dirs still hold `corelli.*.json`.** Frozen, gitignored snapshots from
   past stages (`baroque_4bi`, `default_jki`, `jazz_l5m`, …) still contain `corelli.music21.json` +
   `corelli.ours.json` and stale 353-count manifests. These are **not the gate** (the 3 active gate dirs are
   clean) and were **left untouched** (minimum-surprise; rewriting historical snapshots has no gate benefit).
   They can be swept in a separate cleanup if desired — flagging, not acting.

3. **No tracked git diff exists for this change** (§4).

---

## §4 status — commit

**No commit made.** The hygiene change lives entirely in gitignored/untracked space (`/tools/corpus/` is
ignored by `.gitignore:26`) and corelli was unregistered in any tracked file, so the removal touches **zero**
tracked files — there is nothing to `git add`. I deliberately did **not**:
- make an empty/`--allow-empty` marker commit,
- `git add -f` the gitignored corpus (beginning to track the corpus is a policy decision that is Cowork's, not
  a hygiene step),
- touch the unrelated pre-existing working-tree changes (`cowork_layer5_function_design.md`,
  `cowork_layer6_*.md`, `scratch_artifacts/`).

This report is itself gitignored. **Recommendation:** no commit is needed for a gitignored-only change; if a
tracked provenance marker is wanted, that is a Cowork call. **Did not push. `upstream` untouched.**

## §5 — Stops honored
No `src/`/`tools/` code change, no threshold/inference change, no push, `upstream` untouched. §1 confirmed
corelli is gate-non-contributing (removal does not move a BIR identity), so no Cowork ruling was required to
clean.
