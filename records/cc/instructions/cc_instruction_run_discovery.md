# CC Instruction: run the full balanced idiom-discovery (with cap-robustness) on this machine

## Why here
The full run is **chordify-bound (~10 min)** and exceeds Cowork's sandbox 45 s/call cap, so it runs on your machine
(more compute, no cap — the §11.3 plan). It is **read-only analysis** that writes one report file; it does **not**
touch `src/`, the build, or the MuseScore tree, and commits nothing.

## What it does
`idiom_discovery/run_discovery.py` (path-portable — all paths derived from its own location) builds the **full
balanced corpus** (every chord-symbol source + note-level Bach/`.xml` chordify; ChoCo `ireal-pro` raw excluded; each
source capped), runs the discovery, sweeps **three per-source caps (400 / 700 / 1200)** as the **cap-robustness
check**, and projects the **curated Steely Dan / Piazzolla / Hiromi** scores into the idiom space. Output:
`idiom_discovery/discovery_report.md`.

## Step 0 — Python env
Use a Python (the repo `.venv`, or a fresh one) with these installed:
```
pip install music21 scikit-learn scipy numpy pandas
```
(music21 ships its bundled corpus — needed for the Bach chorales.)

## Step 1 — run it
```
cd C:\s\MS
python idiom_discovery\run_discovery.py
```
Expect ~10 minutes (chordify of Bach + the `.xml` jazz + the 49 curated `.mxl` is the cost). It prints progress per
cap and writes `idiom_discovery\discovery_report.md` at the end.

## Step 2 — report back
Paste the contents of `idiom_discovery\discovery_report.md` (it's short). The things to confirm:
- the **cap-robustness sweep**: are the ~6 idioms and the `clusters<->tradition ARI` **stable across the three caps**
  (400 / 700 / 1200)? (If yes, the idiom set isn't an artifact of the balancing knob.)
- the **curated probe**: where do steely_dan / piazzolla / hiromi land (expected: the cross-cutting chromatic/modal
  idioms, not the clean ones).
- flag any source that **failed to load** (a path/format error) or any of the 5 force-converted curated scores that
  produced odd output.

## Notes
- `corpora/` is locally git-ignored; `discovery_report.md` is the only file written (under `idiom_discovery/`,
  currently untracked — no commit needed, just paste it back).
- Don't touch `src/`, the build, or the MuseScore tree; nothing to commit or push.
