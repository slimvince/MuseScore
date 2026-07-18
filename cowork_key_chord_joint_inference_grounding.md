# Research grounding — is key/mode inference separable from chord inference, or must it be joint?

**Purpose.** Ground the architecture question raised by the OI-165/OI-166/OI-170/OI-175 findings — the
committed chord depends on the (provisionally) inferred key/mode; segmentation depends on a provisional key;
mode (relative major/minor) is disambiguated by the very cadences/chords it governs — against the published
literature. Method: five parallel literature searches with primary-source fetch (deep-research harness,
2026-07-14); every load-bearing claim labeled **FACT** (stated/measured in-paper), **THEORY** (established
published theory), or **CONJECTURE** (author speculation or our inference), per principle #1. Citations are
to fetched primary texts unless noted.

---

## 0. The one-line answer

**The mutual dependence of key, mode, and chord is the ESTABLISHED, consensus structure of tonal analysis —
not a defect in our system (#3 resolved: the finding is expected, we had simply not grounded it). The
best-established methods infer the coupled quantities JOINTLY (one probabilistic model decoded in a single
pass, or one shared representation), NOT as a clean feed-forward pipeline.** The measured benefit of
jointness is **asymmetric — it lands mostly on KEY/MODE, barely on the chord** — which both explains our
architecture and points at the minimal coupling we actually need.

---

## 1. The consensus that the problem is joint (THEORY, broadly stated)

- Micchi, Gotham & Giraud, *Not All Roads Lead to Rome*, **TISMIR 3(1):42–54, 2020**: automatic functional
  analysis "require[s] the **simultaneous assessment of keys and chords**"; the sub-problems are "**deeply
  related but in complex ways**," resting on "**mutually informative decisions**" over where chords change
  and where keys change. **THEORY/consensus.** (https://transactions.ismir.net/articles/10.5334/tismir.45)
- Wu, Nakamura & Yoshii, APSIPA ASC 2020: "**Given the mutual dependency between keys and chords**… we
  propose a unified deep classification model," grounding it in Krumhansl (1990) and key-dependent HMMs.
  **THEORY.**
- Nápoles López, Gotham & Fujinaga (AugmentedNet, ISMIR 2021): functional harmony "requires other adjacent
  tasks to be solved **simultaneously**, notably including the detection and identification of key changes."
  **FACT-of-framing.**
- Lineage cited as the consensus base: Lee & Slaney (key-dependent chord HMMs, 2007/2008), Mauch & Dixon
  (2010), Papadopoulos & Peeters (joint chords+downbeats, 2011), Pauwels & Peeters (joint keys+chords+
  boundaries, 2013).

*No paper in the surveyed set reports a SURPRISE that joint modeling helped — it is treated as a
well-diagnosed fact, exactly the fact-basis #1 asks for.*

## 2. The established JOINT architectures, most-principled first

**(a) A single composite hidden state `(tonic, mode, chord)`, decoded in one pass — the cleanest structure.**
Raphael & Stoddard, *Functional Harmonic Analysis Using Probabilistic Models*, **Computer Music Journal
28(3):45–52, 2004** (free companion: *Harmonic Analysis with Probabilistic Graphical Models*, ISMIR 2003).
**FACT:** each metric period carries one hidden triple `(tonic∈12, mode∈{maj,min}, chord∈{I…VII})` =
12×2×7 = **168 states**; a first-order Markov chain over that *joint* state with a factored transition
(key-change transposition-invariant; chord transitions key-independent while the key holds); inference is a
**single Viterbi/DP decode** `argmax_L P(L|X)` — "capable of finding the globally optimal harmonic
labeling," no beam needed; parameters trained unsupervised by Baum-Welch/EM on generic MIDI. Secondary
dominants are modeled as momentary modulation, not a separate chord class. **This is the reference structure
for "infer key + mode + chord simultaneously."** Caveat (**FACT**): the paper offers *no* error-rate
evaluation — the disambiguation benefit is argued, not measured (**CONJECTURE-grade there**).

**(b) Coupled chains with a key-conditioned chord transition — the same idea, factored.**
Ni, McVicar, Santos-Rodríguez & De Bie, *An End-to-End Machine Learning System for Harmonic Analysis*,
**IEEE TASLP 20(6):1771–1783, 2012** (arXiv:1107.4969). **FACT:** separate key/chord/bass chains; the
coupling is the **key-conditioned chord transition `p(cₜ | cₜ₋₁, kₜ)`**; a **single joint Viterbi** over
`(key,chord,bass)` (with pruning heuristics for tractability, still one joint decode). **The empirical
payoff (their ablation ladder, MIREX-2010, 217 songs) is the cleanest evidence in this literature:**
chord-only → key-conditioned → fully joint raises chord-overlap only ~77.8→78.2→78.8 % (≈1 pp) but raises
**key accuracy ~76.9 → 83.8 %** — *joint helps KEY, not chord.* Caveat (**FACT**): the ladder also changes
the chromagram and the training regime, so it is not a clean isolate-the-coupling ablation.

**(c) Shared-representation multi-task neural nets — the modern SOTA mechanism.**
Chen & Su (ISMIR 2018, BPS-FH) → Micchi et al. (TISMIR 2020) → **AugmentedNet** (ISMIR 2021) → **ChordGNN**
(ISMIR 2023) → **RNBERT** (ISMIR 2024) → **AnalysisGNN** (arXiv 2509.06654, 2025). **FACT:** all share one
encoder and predict key, degree(s), quality, inversion, root (AugmentedNet: **11 tasks**; AnalysisGNN:
**~20**, incl. cadence/phrase/pedal) through **parallel task heads** — a shared *representation*, but the
heads decode *independently*. Coupling is implicit (shared features) except in two lines that add explicit
coherence: the **Harmony Transformer** (Chen & Su 2019/2021) couples segmentation→recognition in an
encoder–decoder, and **RNBERT** (Sailor 2024) adds optional **key-conditioned** RN decoding. **Evidence
joint > separate (FACT):** Chen & Su 2018 (MTL beats single-task on all five functions); Wu et al. 2020
(clean same-architecture ablation: key +3.5 pp, up to +10 pp with a VAE regularizer; **chord ≈ flat**);
AugmentedNet 6→11 tasks (key 82.7→83.7, RN 43.3→45.0).

**Contested (FACT):** explicit joint *decoding* mechanisms are NOT a free win — RNBERT found NADE-style
sub-task chaining (after Micchi et al. 2021) and learned loss-weighting each gave "a small
degradation"; key-conditioning mainly buys *coherence* (avoids "I64 in the wrong key") rather than accuracy
once *predicted* (not oracle) keys are used. **Joint representation-sharing is the robust, uncontested win;
joint decoding is mixed.**

## 3. Segmentation is part of the joint problem too (FACT)

The purpose-built joint-segmentation lineage is **semi-Markov / segmental**: Masada & Bunescu, *A Segmental
CRF Model*, **TISMIR 2019** (semi-CRF jointly choosing chord spans + labels by DP over segmentations, "**joint
segmentation and labeling**," reported "substantially better" than Melisma and HMM baselines — **confounded**
by richer features, they note); the neural semi-CRF **Harana** (Yang, Cwitkowitz & Duan, ISMIR 2023, "**lack
of boundary modeling… could lead to segmentation errors**"); the **Harmony Transformer** (segmentation
informs recognition). By contrast the mainstream neural RN systems (Micchi, AugmentedNet) are **frame-wise on
a fixed 32nd-note grid** and recover segments by post-hoc merging — segmentation is *not* a joint hidden
variable there. **So the strongest theory says segmentation, chord, and key are one joint estimation;
the popular neural systems approximate it with a fixed grid.**

## 4. The counter-example that matters for us — Temperley is feed-forward, and it shows the seam

David Temperley's systems (the drift-grounding already cites him) are the clearest **feed-forward** design,
and they reveal exactly where the seam is. **FACT:** in *The Cognition of Basic Musical Structures* (2001)
the order is pitch-spelling → **harmony → key** (harmony feeds key; key does **not** feed the harmony
decision; Roman numerals are computed *after* key from the fixed chords — Dannenberg review, *Music
Perception* 20(3), 2003; Melisma docs). His key-finder is a **Krumhansl-Schmuckler descendant scored on the
pitch-class distribution — chord-INDEPENDENT** ("What's Key for Key?", *Music Perception* 17(1), 1999;
*Music and Probability*, 2007). His one genuinely *joint* model (JNMR 38(1):3–18, 2009) unifies
**meter+harmony+stream and drops key entirely.** Dannenberg names the reason the 2001 model pipelines rather
than joins: the DP framework "**cannot handle rule systems where interactions are not additive.**"

**The lesson (THEORY + our synthesis):** *key can be substantially inferred from the pitch-class
distribution alone, independently of the committed chords* (Krumhansl/Temperley) — which is why a feed-forward
key stage is viable at all. What genuinely needs the coupling is (i) **mode** — relative major vs minor of a
signature, which the pitch-class profile disambiguates poorly and cadences/chords disambiguate well; (ii)
**chord FUNCTION** (key-relative by definition); (iii) **local key / modulation**. The coupling is real but
*narrow*, and it is strongest exactly on the mode/key axis, matching §2's asymmetry.

---

## 5. Architectural implication for our from-scratch analyzer

1. **A pure feed-forward pipeline is not the established best design, but it is not worthless either.** Key
   *can* be bootstrapped chord-independently from the pitch-class distribution (Temperley) — which is what
   our `resolveKeyAndModeRanked` initial pass already is. The published SOTA nonetheless models key and chord
   **jointly**; feed-forward is the weaker approximation, and its known failure point is **mode / relative-key
   / function** — precisely our OI-174 (spurious `Altered`), OI-147 (exotic mode on plain material), and the
   relative-major/minor errors in the key diagnosis.

2. **Our current architecture is already an ITERATIVE approximation of the joint model** (initial
   pitch-class key → segmentation → sequence decode → chord using the key). That is a legitimate,
   published family (provisional-then-refine / EM-style bootstrap). The OI-175 "back-edge" is not a bug to
   eliminate at all costs — it is the coupling the problem demands, appearing as iteration. The design choice
   is whether to keep it *implicit and ad-hoc* or make it *principled*.

3. **The minimal principled joint structure, per the best-established methods, is the Raphael-Stoddard
   composite state `(tonic, mode, chord)` decoded in one Viterbi/DP pass** (§2a) — or, factored, a
   key-conditioned chord transition in one joint decode (§2b, Ni et al., whose ablation shows the payoff is
   on key). For a symbolic analyzer aiming at maximum precision (#4, which sanctions the complexity), this is
   the fact-based target: **one decode over the coupled state, not two layers pretending to be independent.**

4. **The coupling we most need is narrow and we already have the channel for it.** The asymmetry (joint helps
   key/mode, barely chord) plus Temperley's chord-independent key-finding means the highest-value coupling is
   *chord/cadence evidence → mode & local-key*, not *full chord identity ↔ key*. That is exactly the
   **key-agnostic cadence pre-scan** we specified at OI-166: it is the established mechanism (cadence/chord
   evidence disambiguating mode) delivered as a forward-consumable vote, i.e. the joint coupling in a
   tractable form. **THEORY/our synthesis** — consistent with Ni et al.'s key-conditioning and the
   multi-task consensus, but the specific "pre-scan vote" packaging is our design, not a cited result.

5. **Segmentation belongs inside the joint estimate** (§3, semi-CRF lineage). If we formalize a joint key/mode/
   chord decode, harmonic-rhythm/segmentation should be a modeled variable in it (semi-Markov segment
   durations), not a fixed pre-pass a provisional key silently shaped — which is the honest resolution of
   OI-175.

**Open design fork this grounds (for the design pass, the user's call):**
(A) **Formalize a joint `(tonic, mode, chord)` decode** (Raphael-Stoddard/Ni et al. structure, optionally
semi-Markov for segmentation) — the most principled, highest-complexity, most fact-aligned option; or
(B) **Keep an explicit provisional-then-refine iteration** but make its coupling principled and its
convergence stated; or (C) a **shared-representation** coupling. The literature's robust win is joint
*representation/decode* (A/C) over independent layers; its one caution is that heavy explicit joint-decoding
machinery buys coherence more than accuracy, so the coupling should be **minimal** — which argues for the
narrow cadence/mode channel of (4) rather than a full chord↔key feedback loop.

---

## Sources (primary, fetched 2026-07-14)

Raphael & Stoddard, CMJ 28(3):45–52, 2004 (https://direct.mit.edu/comj/article-abstract/28/3/45/93927) +
ISMIR 2003 (https://ismir2003.ismir.net/papers/Raphael.pdf) · Ni et al., IEEE TASLP 20(6), 2012
(https://arxiv.org/abs/1107.4969) · Temperley: *Cognition* 2001, "What's Key for Key?" MP 17(1) 1999,
*Music and Probability* 2007, JNMR 38(1) 2009 (https://davidtemperley.com/wp-content/uploads/2015/11/temperley-jnmr09.pdf),
Dannenberg review (https://www.cs.cmu.edu/~rbd/papers/temperley-online.pdf) · Chen & Su, ISMIR 2018
(http://ismir2018.ircam.fr/doc/pdfs/178_Paper.pdf) · Micchi et al., TISMIR 2020
(https://transactions.ismir.net/articles/10.5334/tismir.45) · Chen & Su Harmony Transformer, ISMIR 2019
(https://zenodo.org/records/3527794) + "Attend to Chords" TISMIR 2021
(https://transactions.ismir.net/articles/10.5334/tismir.65) · AugmentedNet, ISMIR 2021
(https://archives.ismir.net/ismir2021/paper/000050.pdf) · ChordGNN, ISMIR 2023
(https://arxiv.org/abs/2307.03544) · RNBERT, ISMIR 2024
(https://malcolmsailor.com/assets/RNBERT_ISMIR_Camera_Ready.pdf) · Wu, Nakamura & Yoshii, APSIPA 2020
(https://www.apsipa.org/proceedings/2020/pdfs/0000500.pdf) · Masada & Bunescu, TISMIR 2019
(https://arxiv.org/abs/1810.10002) · Yang, Cwitkowitz & Duan (Harana), ISMIR 2023
(https://archives.ismir.net/ismir2023/paper/000080.pdf) · AnalysisGNN, 2025 (https://arxiv.org/abs/2509.06654).

*Verification caveats carried from the search pass: the Ni et al. per-cell ablation decimals were partly
OCR-scrambled (the trend and the ~77→84 key jump are reliable; exact decimals need the typeset table); no
paper offers a clean three-way key→chord vs chord→key vs joint benchmark on symbolic RN (the "joint wins"
case rests on MTL-vs-single-task and key-conditioning ablations plus the one clean audio VAE ablation); the
semi-CRF segmentation gain is confounded with richer features; a verbatim bidirectional key↔harmony sentence
in Temperley's print chapters was not accessible to confirm.*
