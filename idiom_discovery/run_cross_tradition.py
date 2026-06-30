"""The first CROSS-TRADITION discovery run: classical (DCML) + jazz (JHT) + pop (McGill).
THE test: do the emergent clusters track TRADITION (genre), or something else (mode, color)?
Sources balanced by subsampling so no tradition dominates the LDA (spec §5)."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from extract import build_corpus
from discover import fit_lda, summarise

C = "/sessions/nice-busy-fermat/mnt/MS/corpora"
N_PER = 380          # balance: cap each tradition
random.seed(0)

# --- classical (DCML: scarlatti+mozart+beethoven+romantics) ---
classical = []
specs = [f"{C}/expl/dcml_scarlatti", f"{C}/expl/dcml_mozart", f"{C}/expl/dcml_beethoven"]
rom = f"{C}/expl/dcml_romantic"
specs += [os.path.join(rom, s) for s in os.listdir(rom)
          if os.path.isdir(os.path.join(rom, s, "harmonies"))]
for d in specs:
    ps = load_dcml_repo(d, source="dcml_" + os.path.basename(d), composer=os.path.basename(d))
    for p in ps:
        p.meta["tradition"] = "classical"
    classical += ps

jazz = load_jht(f"{C}/expl/jazz_harmony_treebank/treebank.json", source="jht")
pop = load_mcgill(f"{C}/ship/McGill-Billboard", source="mcgill")


def sample(lst, n):
    return random.sample(lst, n) if len(lst) > n else lst


pieces = sample(classical, N_PER) + sample(jazz, N_PER) + sample(pop, N_PER)
random.shuffle(pieces)
print(f"classical {len(classical)} jazz {len(jazz)} pop {len(pop)}  ->  using {len(pieces)} balanced")

X, vocab, meta = build_corpus(pieces, view="transition", min_df=5, max_df=0.9)
print(f"piece × transition-token matrix: {X.shape}  (vocab {len(vocab)})")
lda, dt = fit_lda(X, n_topics=12, seed=0)
labels = summarise(lda, dt, vocab, meta, n_clusters=6, seed=0)

import collections, numpy as np
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
trad = np.array([p.meta.get("tradition", "") for p in pieces])   # from pieces (sync-proof)
print("\n=== TRADITION (genre) leakage — the headline test ===")
print(f"  clusters <-> tradition   ARI={adjusted_rand_score(trad, labels):+.3f}  AMI={adjusted_mutual_info_score(trad, labels):+.3f}")
print("\n=== cluster x tradition makeup ===")
for c in sorted(set(labels)):
    tr = collections.Counter(trad[labels == c])
    tot = sum(tr.values())
    comp = "  ".join(f"{k}:{v/tot:.0%}" for k, v in tr.most_common())
    print(f"  cluster {c} (n={tot:3d}): {comp}")
