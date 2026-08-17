# BUILD_AND_TEST.md — ARCHIVE (historical, reference-only)

> **The archive companion of `BUILD_AND_TEST.md`.** Created 2026-08-17 by `cc_instruction_preparation_sixth.md` Task 1, executing Rulings 1, 2 and 3 of `cowork_rulings_2026_08_17_governing_surface_split.md` over the ratification surface `ratification_surfaces/cowork_governing_surface_split_2026_08_16.md`. It receives spans moved VERBATIM out of `BUILD_AND_TEST.md`, in the order they left it, each under a provenance line naming its position in the parent's pre-act blob. **NOT part of the session-start read** — read `BUILD_AND_TEST.md` for what governs.
>
> **Nothing was edited in transit.** The reconciliation is re-derived by `tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md` and proves both directions: every archived span is byte-present here and absent from the parent, and moved + kept accounts for the parent's pre-act committed blob to the character (#12, preservation elsewhere-with-record on the register-split precedent).

> **From `BUILD_AND_TEST.md` lines 136–138 at `1f84f5d621` (measured at `c4f15a7b32`), class `preserved-former-wording`, 289 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

*Former wording, preserved in place (#12): "**Current baseline: 974/974** passing, 2 disabled (verify
with CC — count changes as tests are added)." The 974 value was measured on 2026-07-13 and was stale
at HEAD; its "verify with CC" caveat went unexercised from then until this re-stamp.*

> **From `BUILD_AND_TEST.md` lines 173–177 at `1f84f5d621` (measured at `c4f15a7b32`), class `preserved-former-wording`, 478 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

*Former wording, preserved in place (#12): "**Current baseline: 53/53** passing (verify with CC —
count changes as tests are added)." It reported a clean suite: the count was stale at HEAD **and** it
named none of the four xfails, so a reader checking whether the tests pass was told yes and never
learned that four DCML-checked cases were failing by design. That concealment, not the stale count,
is the harm `OPEN_ITEMS.md` OI-150 rowed as the harmful one of its two halves.*

> **From `BUILD_AND_TEST.md` lines 323–326 at `1f84f5d621` (measured at `c4f15a7b32`), class `self-declared-historical-or-superseded`, 188 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

Previous baseline (Iteration 54, corpus regeneration 2026-05-11):
- 3-way genuine BIR=true: 14
- 3-way genuine BIR=false: 132
- Commit: f92a4f1a3b (greedy-expand segmentation, batch path)

> **From `BUILD_AND_TEST.md` lines 333–335 at `1f84f5d621` (measured at `c4f15a7b32`), class `self-declared-historical-or-superseded`, 126 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

Previous baseline (Iteration 46, corpus regeneration 2026-05-09):
- 3-way genuine BIR=true: 21
- 3-way genuine BIR=false: 128

> **From `BUILD_AND_TEST.md` lines 344–346 at `1f84f5d621` (measured at `c4f15a7b32`), class `self-declared-historical-or-superseded`, 153 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

Previous baseline (Iteration 36, corpus regeneration 2026-05-08 with new alternatives JSON):
- 3-way genuine BIR=true: 32
- 3-way genuine BIR=false: 177

> **From `BUILD_AND_TEST.md` lines 394–397 at `1f84f5d621` (measured at `c4f15a7b32`), class `self-declared-historical-or-superseded`, 261 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

Previous Jazz baseline (Iteration 46 binary, validated 2026-05-09):
- 3-way genuine BIR=true: 106  (Jazz harmony is outside Baroque gate scope — not a target)
- 3-way genuine BIR=false: 20
- Total regions: 9389 across 353 scores; chord identity agreement 80.3%

> **From `BUILD_AND_TEST.md` lines 402–405 at `1f84f5d621` (measured at `c4f15a7b32`), class `self-declared-historical-or-superseded`, 208 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

Previous figures for reference (Iteration 32, Baroque):**
- 3-way genuine BIR=true: 48
- 3-way genuine BIR=false: 787
(With _matches_alternative disabled these are still recoverable from the Iter 36 corpus.)

> **From `BUILD_AND_TEST.md` lines 416–423 at `1f84f5d621` (measured at `c4f15a7b32`), class `self-declared-historical-or-superseded`, 540 characters.** Moved 2026-08-17; authored per span, read in the file itself (A4).

Previous baselines for reference:
Iteration 30 (2026-05-08): BIR=true=52, BIR=false=787.
Gate K — prefer first-inversion augmented over root-position augmented. When the
winner is Augmented bassIsRoot=true and a runner-up has the same bass note at interval+4
from its own root (I4 = major-third inversion), the runner-up quality is Augmented or
Major+SharpFifth, the runner-up's root is diatonic to the key, and the score margin
is ≤ 0.20, swap to the first-inversion reading.
1 BIR=true fix (bwv40.6 m=6: A+ → F#5/A); BIR=false unchanged.

