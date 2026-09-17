# CC Instruction: re-run the EXPANDED idiom discovery (wobbly-6th + idiom-#5 re-check)

## Why
`idiom_discovery/run_discovery.py` now includes the newly-added sources — ChoCo **weimar** (modal/bebop) + **jaah**
+ **jazz-corpus** + **wikifonia** (5k leadsheets), **Impro-Visor** (modal jazz), and **Chordonomicon** (chromatic
pop) — wired in alongside everything from the previous run. Re-running it tests two open questions: whether the
*wobbly 6th* idiom firms up, and whether idiom *#5* stays unified or fragments.

Read-only analysis; writes only the report; do **not** touch `src/`, the build, or the MuseScore tree; nothing to commit.

## Run (same as before — no new dependencies; pandas/music21/sklearn already installed)
```
cd C:\s\MS
python idiom_discovery\run_discovery.py
```
~10–15 min (the extra sources + the chordify of Bach / `.xml` / curated). It writes
`idiom_discovery\discovery_report.md`.

## Report back — paste `discovery_report.md`, and specifically confirm:
1. **Cap-robustness** — does `clusters<->tradition ARI` stay in its band and do the idioms recur across caps
   400 / 700 / 1200?
2. **★ The wobbly 6th** — with the added modal jazz (weimar + Impro-Visor), does a **stable sixth idiom**
   (modal / static-7th) now appear at *every* cap, or does it still wobble in and out?
3. **★ Idiom #5 (cross-cutting chromatic/modal)** — with Chordonomicon + the modal jazz, does it stay **one**
   idiom or **split** into sub-idioms (e.g. chromatic-jazz vs impressionist-modal vs blues)?
4. **Curated probe** — where do steely_dan / piazzolla / hiromi land now?
5. **Load check** — flag any source that produced **0 pieces** (a path/format error), especially the new ones:
   `improvisor`, `chordonomicon`, `weimar`, `jaah`, `jazz-corpus`, `wikifonia` (the per-source `+name … N` lines
   in the run log show each source's count).

## Notes
- `improvisor` and `chordonomicon` use **estimated keys** (most-common root) — expect them to be a bit noisier; both
  are **exploration-only** (license), so this is for deciding the idioms, not shipped weights.
- If the run errors on a missing module, confirm `idiom_discovery/parsers/` has `improvisor.py` and `chordonomicon.py`
  (Cowork added them).
