# CC Instruction: Commit Stage 2.1, then investigate the floating Jazz BIR count

## Part 1 — Commits (approved)

Both Stage-2.1 commits are approved as proposed in `cc_stage2_1_report.md`:
- **Commit A** (rider: chordanalyzer.h doc-comment) — commit first, separately.
- **Commit B** (the Phase 4c move, Option D) — the zero-snapshot-diff result is the
  decisive gate; the Jazz observation below is not attributable to the move (sources
  semantically identical for the batch path) and does not block it.
Explicit staging per your file map; never `muse`; report both hashes.

## Part 2 — Investigation: the Jazz BIR count floats (7–9). Find the REAL mechanism.

**Why this is urgent (bigger picture):** every hard-stop gate since Iter 97 says
"Jazz BIR=false ≤ 7". If the metric is actually a band, the gate semantics are broken —
a regression could hide inside the noise, and a "7" pass may have been luck. This must
be characterized BEFORE Stage 2.2's re-baseline (which will set NEW numbers — they must
be set on a deterministic metric or explicitly as a distribution).

**Correction to your stated mechanism (this is why we investigate rather than log):**
`batch_analyze.cpp` contains no threading (verified by grep: no std::thread/async/omp).
The parallelism is PROCESS-level in `run_bach_preset.py` — independent workers over
independent chorales. That cannot make one score's tie resolution nondeterministic.
"Parallel batch path resolves ties nondeterministically" was a guess — the never-guess
rule applies. Two real candidate mechanisms, both cheaply testable:

- **M1 — C++ nondeterminism within a single batch_analyze process.** Same input, same
  binary, different output across runs ⇒ ASLR-dependent behavior: iteration over
  pointer-keyed containers (`std::map<Element*>`, `unordered_*` with pointer hash),
  or uninitialized reads. At a margin=0.000 exact tie, candidate order from such a
  container decides the winner. Plausible: engraving traversal code uses pointer-keyed
  maps in places.
- **M2 — Python-side nondeterminism in the metric scripts.** Per-process salted string
  hashing (`PYTHONHASHSEED` random) changes set/dict iteration order; if alignment or
  classification ever iterates a set to break an equal-overlap tie, the COUNT floats
  while the JSONs are identical. (The Stage-1d determinism test ran same-process —
  it cannot catch cross-process hash salting.)

### Protocol (run in order; stop when the mechanism is proven)

1. **Isolate the layer.** With the corpus ALREADY regenerated once for Jazz
   (`tools/corpus` in Jazz state):
   ```
   cd C:\s\MS && for i in 1 2 3 4 5; do python tools/characterise_bir_false.py 2>&1 | tail -2; done; echo "exit:$?"
   ```
   Same corpus dir, five runs. If the count varies → **M2 proven** (script-side); go to
   step 4. If stable → C++ side; continue.
2. **Single-score determinism (M1).** Pick one of the flipping cases (identify which
   scores flip by diffing the BIR case lists between a "8" run and a "9" run — capture
   the per-case output, not just the total). Run `batch_analyze.exe` on that ONE score
   5× to fresh output files; `diff`/hash the JSONs:
   ```
   cd C:\s\MS && for i in 1 2 3 4 5; do ninja_build_rel/batch_analyze.exe <score> --preset Jazz <args per build_and_test.md> > /tmp/nd_$i.json 2>/dev/null; done; md5sum /tmp/nd_*.json; echo "exit:$?"
   ```
   (Adapt the exact CLI from build_and_test.md — do not guess flags.) Differing hashes
   → **M1 proven**; identical → the nondeterminism enters between single-score runs and
   the full regen (driver-level: worker assignment, file collisions — investigate
   run_bach_preset.py's aggregation next).
3. **If M1: localize.** Diff two differing JSONs to find WHICH chord flips; then read
   the code path that produced that field, hunting pointer-keyed iteration or
   uninitialized state. Do not fix yet — localize and report. (A fix changes behavior
   ⇒ Stage 2.2 re-baseline territory.)
4. **If M2: localize.** Rerun step 1 with `PYTHONHASHSEED=0` fixed: if the count
   stabilizes, hash salting is confirmed; find the set/dict iteration that breaks
   alignment ties (likely in `align_regions`/`_best_dcml_match_by_overlap` candidate
   ordering or a dict over case keys). Again: localize, don't fix.
5. **Characterize the band regardless of mechanism:** 10 measurements (regen → measure,
   or measure-only if M2) → report the distribution (e.g. {7: n, 8: m, 9: k}) and the
   IDENTITY of every case that flips (score + tick + the tied candidates + margins).
   Also run Baroque 3×: is 13 genuinely stable or just less tie-prone?
6. **History check (cheap form only):** were the historical "7"s ever multi-sampled?
   Search the cc_* reports/STATUS for evidence of repeated same-session Jazz runs. Do
   NOT rebuild old commits.

### Deliverable — `cc_jazz_nondeterminism_report.md`

Mechanism (M1/M2/other, with the proving observation), flipping-case identities, band
distribution, Baroque stability, the localized code site(s), and a recommended fix
DESIGN (deterministic tie-break or hash-seed pinning) for the Stage 2.2 decision — no
fix implemented. Interim gate guidance: propose how "Jazz ≤ 7" should read until fixed
(e.g., gate on case identities + Baroque + snapshots instead of the raw Jazz count).

Tag every claim [probe]/[code]. Stop conditions: the mechanism is neither M1 nor M2 and
the next hypothesis would be a guess; or the flipping cases implicate Baroque too
(gate integrity emergency — report immediately).
