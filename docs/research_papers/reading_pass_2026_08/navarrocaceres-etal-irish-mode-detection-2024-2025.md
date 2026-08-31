# FETCHED CONTENT RECORD — the Irish-traditional mode-detection pair (population row 9): Navarro-Cáceres, Carvalho, Bernardes, Jiménez-Bravo & Navarro-Cáceres 2024 (MCM, LNCS 14639, 412–420) and Navarro-Cáceres, Jiménez-Bravo & Navarro-Cáceres 2025 (Applied Sciences 15(6):3162)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass. The surface's row names ("four-
> mode symbolic detection on Irish traditional music at roughly 80% reported accuracy…",
> R110–R111) resolve to TWO papers by one group: **(a)** "Exploring Mode Identification in Irish
> Folk Music with Unsupervised Machine Learning and Template-Based Techniques" (MCM 2024) — the
> "~80% average accuracy" primary, **ABSTRACT-READ ONLY: its full text is paywalled at Springer
> and no open copy was found; nothing beyond the abstract is carried**; and **(b)** "Evaluating
> Preprocessing Techniques for Unsupervised Mode Detection in Irish Traditional Music" (Applied
> Sciences 2025, open access) — read whole via one prompted extraction call (`mdpi.com/2076-3417/15/6/3162`).
> The standing environment bound of `reading_pass/additions.md` applies.

## (a) MCM 2024 — abstract facts only

"Extensive computational research has been dedicated to detecting keys and modes in tonal
Western music within the major and minor modes. Little research has been dedicated to other
modes and musical expressions, such as folk or non-Western music. This paper tackles this
limitation by comparing traditional template-based with unsupervised machine-learning methods
for diatonic mode detection within folk music." Reported: "an average accuracy of about 80%"
across Ionian, Dorian, Mixolydian, Aeolian. **Full method, corpus and per-mode numbers NOT
carried — full text not held.**

## (b) Applied Sciences 2025 — read whole

Input: ABC notation, The Session corpus as curated by Sturm et al. — 23,636 Irish folk tunes,
ALL TRANSPOSED TO TONIC C (the tonic is GIVEN; only the mode is inferred). Mode distribution:
Ionian 15,861 (67.1%), Dorian 2,971 (12.6%), Mixolydian 1,620 (6.9%), Aeolian 3,184 (13.5%);
labels from the dataset's metadata.

Method: preprocessing comparison — simple / duration-and-beat-weighted / binary pitch-class
profiles, optionally UMAP or LLE reduction, against three learned audio-embedding spaces
(JukeMIR 4800-d, Mule 1728-d, MERT 1024-d) — across K-means, agglomerative clustering, DBSCAN,
mean shift, self-organizing maps; SMOTE class balancing.

Results: best = BINARY pitch-class profile with agglomerative clustering (NMI 0.5976, ARI
0.5756; K-means 0.5807/0.5626); purity above 60% on all modes for the two centroid methods;
the learned embeddings collapse most tunes into one cluster and underperform throughout;
density methods unreliable.

Mode-vs-key position, quoted: "A mode does not necessarily imply tonal harmony or a functional
chord system. Instead, it primarily governs melodic characteristics, defining which notes are
used and how they interact, without requiring harmonic resolution." Folk melodies "lack strong
harmonic direction and may drift between tonal centers or avoid traditional cadences." Prior
work scarcity, quoted: "Within the domain of music computing, there has been little research on
mode detection. Most existing approaches focus on identifying the major and minor modes";
Dorian/Phrygian/Lydian/Mixolydian/Locrian "remain under-researched and need deeper
investigation."

Limits (as stated): Western diatonic scope; embedding failure; parameter-sensitive clusterers.
