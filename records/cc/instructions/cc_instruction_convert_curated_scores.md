# CC Instruction: convert the curated .mscz scores to .mxl (for the idiom-discovery probe)

## Why
The harmonic-idiom-discovery pipeline (Cowork) runs on music21, which **cannot read `.mscz`** (MuseScore native).
The curated scores under `tools/extra scores/` — Steely Dan, Piazzolla, Hiromi — are the most interesting "hard
case" probes for the idiom set, but they're all `.mscz`. Convert them to **`.mxl`** (compressed MusicXML, which
music21 reads) so Cowork can chordify them.

This is a **read-only conversion** — do not modify the originals. Note the source path **contains a space**:
`"tools/extra scores"` — quote it everywhere.

## Task
Use the MuseScore CLI (the built `mscore`/`MuseScore4`, or an installed MuseScore 4) to convert each `.mscz` to
`.mxl`, into a folder Cowork can read. Keep the three sets separate.

```bash
# adjust the mscore path to your build / install
MSCORE="MuseScore4"     # or e.g.  C:\s\MS\ninja_build_rel\mscore.exe  (whatever your build produces)

mkdir -p C:\s\MS\corpora\expl\curated_mxl\steely_dan \
         C:\s\MS\corpora\expl\curated_mxl\piazzolla \
         C:\s\MS\corpora\expl\curated_mxl\hiromi

# MuseScore batch conversion: one .mscz -> one .mxl
for set_src in "Steely dan:steely_dan" "piazzolla:piazzolla" "hiromi:hiromi"; do
  src="${set_src%%:*}"; dst="${set_src##*:}"
  for f in "C:\s\MS\tools\extra scores\\$src\"*.mscz; do
    base=$(basename "$f" .mscz)
    "$MSCORE" -o "C:\s\MS\corpora\expl\curated_mxl\\$dst\\$base.mxl" "$f"
  done
done
```

(If MuseScore's batch `-o` job mode is easier — a JSON job file mapping each `.mscz` to its `.mxl` — that's fine too;
the only requirement is one `.mxl` per input under `corpora\expl\curated_mxl\<set>\`.)

## Report
- the count of `.mxl` produced per set (expect Steely Dan 23, Piazzolla 6, Hiromi 20), and any that failed to convert.
- `corpora/` is already locally git-ignored (`.git/info/exclude`), so these should not show in `git status` — confirm.

Do not touch the originals, `src/`, or the MuseScore tree; nothing to commit or push.
