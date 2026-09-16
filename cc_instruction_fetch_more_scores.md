# CC Instruction: fetch two public score sources (for re-checking idiom #5 + the wobbly 6th)

## Why
The idiom-discovery study wants more **chromatic pop** (to stress idiom #5) and more **modal jazz** (to test whether
the "wobbly 6th" jazz split is real). Two public datasets target these. **Read-only download + verify**; do not
modify `src/`, the build, or the MuseScore tree; nothing to commit.

Put both under `C:\s\MS\corpora\expl\` (already locally git-ignored). License + format must be verified before we use
them for anything shipped (per the plan §5).

## 1. Chordonomicon (chromatic pop / idiom #5) — HuggingFace, public, ~264 MB
679,807 songs as **chord progressions** with **genre / sub-genre / release-date** + structure. Public (no token).
```
pip install -U "huggingface_hub[cli]"
cd C:\s\MS\corpora\expl
huggingface-cli download ailsntua/Chordonomicon --repo-type dataset --local-dir chordonomicon
```
Source: `https://huggingface.co/datasets/ailsntua/Chordonomicon` (repo: `github.com/spyroskantarelis/chordonomicon`).

**★ Verify and report (this decides whether we can use it):**
- the **license** (HF dataset card);
- the **on-disk format** (CSV/parquet?) and the **column names** — paste the header + one row;
- **★ does it carry a KEY / tonic per song?** (we key-normalize by tonic — if there's no key column, flag it; we'd
  have to estimate key from the chords, which adds noise). Also note the **chord notation** (Harte? plain letters?).

## 2. Impro-Visor "Imaginary Book" leadsheets (modal jazz / the wobbly 6th) — ~2,600 leadsheets
Jazz leadsheets incl. **modal jazz**, in Impro-Visor's `.ls` text format (each has a key).
```
cd C:\s\MS\corpora\expl
mkdir improvisor
#  download TheImaginaryBookandOtherLeadsheets.zip from the OSDN/SourceForge mirror:
#  https://osdn.net/projects/sfnet_impro-visor/downloads/TheImaginaryBookandOtherLeadsheets.zip/
#  (or via the SourceForge project: sourceforge.net/projects/impro-visor/ )
#  extract the .ls files into improvisor/
```
**Verify and report:**
- the **license** (Impro-Visor is open-source — confirm GPL/other and whether the *leadsheet content* is separately
  licensed);
- count of `.ls` files extracted, and **paste the first ~25 lines of one `.ls`** so Cowork can write the `.ls` parser
  (it's a textual leadsheet notation with key + chord symbols).

## After
Report both: counts, formats, license, and (for Chordonomicon) whether a key column exists. Cowork then writes the two
parsers (`chordonomicon` CSV, Impro-Visor `.ls`) and folds them into `run_discovery.py`. Nothing committed; `src/`,
build, MuseScore tree untouched.
