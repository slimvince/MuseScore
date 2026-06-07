# Iter 97 — Categorization of the 26 Baroque BIR=false Cases

Read-only data report. No source changes were made. Generated against
HEAD `7060f2c5db` (Iter 96 baseline, uncommitted v3 working-tree changes
not active in the build used to regenerate the corpus). The corpus
under `tools/corpus/` was regenerated with the Baroque preset and the
26 BIR=false cases were extracted via
`tools/dump_birfalse_cases.py`. Per-case raw fields are preserved at
[tools/iter97_birfalse_cases_data.txt](../tools/iter97_birfalse_cases_data.txt);
the extraction script at
[tools/iter97_categorize_birfalse.py](../tools/iter97_categorize_birfalse.py).

Format notation: `pc` is pitch-class number (0=C…11=B). "WiR" = When in
Rome / DCML ground truth. "M21" = music21 third opinion. All 26 cases
satisfy `music21_dcml_agree` (WiR and music21 agree the root is wrong).

---

## Headline counts

| Bucket | Count | Share |
|---|---:|---:|
| **δ-candidate** (minor, ≤3 PCs, diatonic quality prior could fix) | **0** | 0 % |
| **ε-candidate** (major-key root-sharing rotation, full I/IV present) | **5** | 19 % |
| **segmentation** (region boundary wrong, scoring is secondary) | **4** | 15 % |
| **diffuse / other** | **17** | 65 % |
| **Total** | **26** | 100 % |

The δ premise (a diatonic quality prior on sparse minor regions) does
not actually intersect any of the 26 cases — the minor-mode 3-PC
errors all share a different, structurally distinct pattern (Pattern
B below) that no quality prior can address.

---

## ε bucket — major-key root-sharing rotation (5)

In every ε case the analyzer's wrong root is a member of the correct
triad (or vice-versa), both candidates are diatonic in the region's
key, and the correct triad has all 3 of its chord tones present in
the region. These are the cleanest targetable cluster — the same
shape that `w_seq` (Iter 95) and `w_dim` (Iter 96) already address
when the rotation produces descending-fifth root motion or a
leading-tone resolution; the unaddressed residue is the *non-cadential*
upper-third rotation.

| # | Score | tick | Key | Tones | Our (root,q) | GT (root,q) | Rotation shape |
|---|---|---:|---|---|---|---|---|
| 8 | bwv25.6  | 20640 | Cmaj  | {C,E,G,Bb}   | E°    | C maj  | I7 vs iii° (rootless V7-of-IV) |
| 10| bwv269   | 20640 | Gmaj  | {C,D,F#,A}   | D maj | F#°    | V vs vii° (rootless V7) |
| 20| bwv426   | 960   | Cmaj  | {C,E,F,G,A}  | Am    | F maj  | IV vs vi (third-related) |
| 25| bwv65.2  | 11040 | Cmaj  | {C,D,F#,A}   | A°    | D maj  | V vs vii° (rootless V7) |
| 26| bwv74.8  | 13440 | Cmaj  | {C,D,E,G}    | Em    | C maj  | I vs iii (classic) |

Sub-shape breakdown:

- **V↔vii° rotation, 2 cases** (#10, #25). Both produce the same
  ambiguity: D7 ↔ F#° in G major / V7 ↔ vii° in C major. The "missing
  fifth in the bass" reading vs the "rootless V7 from F#" reading
  share 3/3 chord tones. `w_seq` does not fire because the next region
  is V→I (D→G; D→C) which already promotes the dominant when context
  is available — but here the choice is *between* two readings *of the
  same dominant moment*, not between a dominant and its successor.
- **I/IV vs iii/vi rotation, 3 cases** (#8, #20, #26). The closer to
  literal I↔iii — all three involve a 4-tone region whose pc-set
  fully covers the I (or IV) triad plus one neighbour tone that the
  upper-third candidate uses as a fourth chord tone (Bb-as-b7 on C7,
  A-as-6th on F, D-as-9th on C).

**Suggested targeted fix shape** (one-liner, conjectural): a
major-key tiebreaker that prefers the lower-third candidate when both
the lower-third (I or IV) and the upper-third (iii or vi) are
*complete triads in the region's pc-set*; or symmetrically, a small
penalty on iii°/vii° readings when the corresponding V7 root is
present at chord-tone weight ≥ threshold. Cluster is mechanically
tight enough (5 of 26, all in major-key, all with both candidates
fully present) to justify a dedicated `w_lower_third` / `w_v7_present`
bonus on the Iter 92 joint-scoring path.

---

## segmentation bucket — boundary problems (4)

The region the analyzer produces does not align with what either WiR
or music21 calls a chord. In all four, distinctPcs is dense (4–5) or
includes pcs that don't form any single triad — strong evidence the
region spans more than one underlying chord event.

| # | Score | tick | Key | Tones | n | Our chord | GT |
|---|---|---:|---|---|---:|---|---|
| 2 | bwv14.5   | 8160  | Gmin  | {C,D,E,Bb}        | 4 | Gm/Bb (root absent!) | Bb maj |
| 5 | bwv245.17 | 4800  | Amin  | {C,D,F,A,B}       | 5 | F maj | D (Unknown qual) |
| 11| bwv301    | 960   | Dmin  | {C,D,G#,A,B}      | 5 | G/A (root absent!) | Bm |
| 19| bwv422    | 23040 | Cmaj  | {D,G,A}           | 3 | A7sus/D | G (Unknown qual) |

#2 and #11 are particularly striking — the analyzer's chosen root is
not even present in the region. That's a downstream symptom of the
region spanning a chord transition where the bass moves first.

No targeted scoring fix can reach these cases; they need a
segmentation-side change (finer boundaries at the bass-motion ticks).

---

## diffuse / other bucket (17)

This is the largest bucket. It splits cleanly into four sub-patterns
that share no single structural shape — hence "diffuse." Each
sub-pattern is too small (or too misdiagnosable) to justify a
dedicated scoring change on its own.

### Sub-pattern B — WiR labels a diminished chord whose root is absent from tones (5 cases)

The analyzer's reading IS internally consistent with the region's pc
set; the WiR ground truth labels the harmonic *function* rather than
the sounding chord. All five regions have a clean i/i6 minor reading
of {root, b3, 5}; WiR labels them as the diatonic vii° of the local
key (whose root is not played).

| # | Score | tick | Key | Tones | Our | GT (root not in tones) |
|---|---|---:|---|---|---|---|
| 1 | bwv114.7 | 6000  | Gmin | {D,F,G,Bb}  | Gm7   | A° (no A) |
| 9 | bwv258   | 6000  | Bmin | {D,F#,B}    | Bm    | C#° (no C#) |
| 12| bwv309   | 2160  | Dmin | {D,G,Bb}    | Gm    | A° (no A) |
| 15| bwv354   | 20880 | Fmin | {C#,F,Bb}   | Bbm   | C° (no C, Eb, or Gb) |
| 23| bwv48.7  | 18480 | Gmin | {D,G,Bb}    | Gm/D  | A° (no A) |

These are unreachable by any analyzer change short of one that
hallucinates roots that aren't sounding. They are best treated as a
known WiR/sounding-chord disagreement and excluded from BIR-targeting.

### Sub-pattern C — analyzer chose a rootless winner; correct triad fully present (4 cases)

These should in principle already be blocked by the Iter 78 Fix C /
Iter 82 absent-root guards. The fact that 4 cases slip through is
worth investigating — but the cluster is small.

| # | Score | tick | Key | Tones | Our (root absent) | GT (fully present) |
|---|---|---:|---|---|---|---|
| 4 | bwv174.5 | 6240  | Dmaj | {F#,G#,B}      | E/G# (no E)         | G#m (G#,B / no D#) |
| 18| bwv40.8  | 30720 | Cmin | {C#,Eb,F,Ab}   | Bbm/Db (no Bb)      | Db maj (Db,F,Ab) ✓ |
| 22| bwv45.7  | 20160 | Emaj | {C#,E,Bb}      | F#7/E (no F#)       | Bb° (Bb,Db,E≡Fb) ✓ |
| 24| bwv60.5  | 1920  | Amaj | {C,Eb,F#,Ab}   | F#°7/C (no A nat)   | Ab maj (Ab,C,Eb) ✓ |

Pattern C is the closest structural sibling of ε but the rotation is
not consistent (E vs G#m, Bbm vs Db, F#7 vs Bb°, F#° vs Ab). The
underlying gap is "root-present guard is not firing where it should"
— a precondition audit on Gate E/I/Iter 78 Fix C, not a new bonus.

### Sub-pattern D — synthesized region scored at 0.10 with negative margin (2 cases)

Both cases show the same anomalous signature: `score=0.10`,
`margin=-2.39` (the winner scored *less* than its own runner-up),
and the alternatives list includes the correct `Am7b5/C` reading at
a high score (~2.70). This looks like a bug in the head-gap region
synthesis (Iter 73 Fix B) or in the post-scoring tiebreak — the
"winner" emitted to `regions[]` does not match the highest-scoring
alternative.

| # | Score | tick | Key | Tones | Our | Best alt |
|---|---|---:|---|---|---|---|
| 13| bwv309 | 8160  | Dmin | {C,Eb,F#,G,A} | Gbm7b5/C (s=0.10, m=-2.39) | Am7b5/C (s=2.70) |
| 16| bwv356 | 25920 | Gmin | {C,Eb,G,A}    | Gbm7b5/C (s=0.10, m=-2.39) | Am7b5/C (s=2.70) |

In both, the ground-truth A° is fully present (C, Eb, A) and ranks as
a *higher-scoring alternative*. A direct fix would simply pick the
top-scoring alt when the winner's margin is negative. Mechanically
trivial; pre-condition is verifying this is a genuine bug and not a
deliberately-inverted score convention. **This is the single most
promising 2-case fix** in the entire BIR=false set — it would yield
−2 with essentially no risk.

### Sub-pattern A — WiR labels "Unknown" quality (3 cases here, see also #19 above in segmentation)

WiR considers these passing / non-chord moments. Cases #3, #7, #14
(plus #5, #19 already accounted for above).

| # | Score | tick | Key | Tones | Our | GT |
|---|---|---:|---|---|---|---|
| 3 | bwv17.7  | 46080 | Amaj  | {C#,Eb,A}    | A/Eb     | Eb (Unknown qual) |
| 7 | bwv245.40| 51360 | Ebmaj | {Eb,F,Bb}    | F7sus/Bb | Eb (Unknown qual) |
| 14| bwv354   | 14400 | Fmin  | {C,Eb,F#,Ab} | Ab7/Gb   | Db (Unknown qual) |

Same story as Pattern B: the WiR ground truth is labeling a
harmonic *function* (the resolution target) rather than the sounding
upper structure. No scoring change reaches these.

### Other isolated cases (3)

- **#6 bwv245.28** Amaj, tones {E,G#,B} = exact E major triad,
  analyzer picked B/G# (rootless B with G# bass). Sub-pattern C
  variant (rootless winner) but the rotation isn't iii/vi or V/vii°.
- **#17 bwv381** Emin, tones {D,E,F#,G,B} = full Em + full G, analyzer
  picked G6/F# over Em. This is the *minor-key analog* of ε (i↔III).
  Could plausibly be folded into a generalized "prefer lower-third
  when both fully present" rule, raising the ε family from 5 to 6.
- **#21 bwv432** Gmaj, tones {C,Eb,E,A} — contains both E and Eb,
  doesn't fit any single triad cleanly. Edge case.

---

## Cross-cutting observations

1. **There is no δ cluster in this corpus.** Every minor-mode
   ≤3-PC region in the BIR=false set is *already* read as a valid
   minor triad by the analyzer; the disagreement comes from WiR
   labeling the harmonic function (typically vii° of the next
   chord) with a root that isn't sounding. A diatonic quality prior
   on sparse minor regions has nowhere to land here.

2. **ε is the only multi-case scoring-reachable cluster (5).** Of the
   26 cases, exactly 5 are major-key root-sharing rotations where the
   correct triad has all 3 chord tones present and the analyzer chose
   the upper third. Two further variants (#6 rootless-B, #17
   minor-mode i↔III) sit adjacent to this cluster and could fall to
   the same fix if it's generalized to "prefer the candidate whose
   root is present with full triad coverage over a candidate sharing
   one or two of those tones."

3. **Sub-pattern D (2 cases) is a likely bug, not a scoring weakness.**
   `score=0.10` with `margin=-2.39` is mechanically wrong — the emitted
   winner is *lower* than its own alternative. Both cases would resolve
   to the correct A° reading already present in the alternatives list.
   Worth a 5-minute look at the synthesis / tiebreak path.

4. **8 of 26 cases (Sub-patterns A + B, 3+5) are WiR-vs-sounding-chord
   disagreements** that the analyzer cannot fix by changing scoring,
   because the WiR ground-truth root is not in the sounding pc-set.
   These represent a structural ceiling: BIR=false cannot go below
   ~18 (26 − 8) by analyzer changes alone.

5. **The remaining 4 segmentation cases would require finer
   boundaries** at bass-motion ticks (#2, #5, #11) or at sus/passing
   resolutions (#19). Not a scoring problem.

---

## Recommended sequencing (if a further iteration is undertaken)

1. **First:** investigate Sub-pattern D (cases #13, #16). If it's a
   genuine bug in synthesized-region emission, the fix is mechanical
   and yields −2 with no risk to other cases.
2. **Second:** generalized lower-third tiebreaker for ε (5 cases,
   possibly 6–7 with #6 and #17 picked up). The cluster is tight and
   structurally consistent; risk is moderate (could perturb Jazz where
   iii readings are often desired) and would need the Baroque/Jazz
   gate audit per CLAUDE.md.
3. **Third:** root-present guard audit (Sub-pattern C, 4 cases). Why
   aren't existing Iter 78/82 guards firing? Cluster is small but
   the existing guard is supposed to catch exactly this shape.
4. **Defer / accept:** Sub-patterns A + B (8 cases) and the
   segmentation bucket (4 cases). Total 12 cases that the current
   architecture cannot reach with scoring changes.

If only one of the above is taken, **Sub-pattern D is the highest
EV** — −2 BIR=false for what is likely a one-line bugfix.
