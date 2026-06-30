import os, sys, random, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from extract import build_corpus
from discover import fit_lda, summarise
from sklearn.metrics import adjusted_rand_score as ARI, adjusted_mutual_info_score as AMI

C = "/sessions/nice-busy-fermat/mnt/MS/corpora"
N_PER = 380
random.seed(0)
classical = []
specs = [C+"/expl/dcml_scarlatti", C+"/expl/dcml_mozart", C+"/expl/dcml_beethoven"]
rom = C+"/expl/dcml_romantic"
for s in os.listdir(rom):
    if os.path.isdir(os.path.join(rom, s, "harmonies")):
        specs.append(os.path.join(rom, s))
for d in specs:
    ps = load_dcml_repo(d, source="dcml_"+os.path.basename(d), composer=os.path.basename(d))
    for p in ps:
        p.meta["tradition"] = "classical"
    classical += ps
jazz = load_jht(C+"/expl/jazz_harmony_treebank/treebank.json", source="jht")
pop = load_mcgill(C+"/ship/McGill-Billboard", source="mcgill")
def samp(lst, n):
    return random.sample(lst, n) if len(lst) > n else lst
pieces = samp(classical, N_PER) + samp(jazz, N_PER) + samp(pop, N_PER)
random.shuffle(pieces)
print("classical", len(classical), "jazz", len(jazz), "pop", len(pop), "-> using", len(pieces))
X, vocab, meta = build_corpus(pieces, view="transition", min_df=5, max_df=0.9)
print("matrix", X.shape, "vocab", len(vocab))
lda, dt = fit_lda(X, n_topics=12, seed=0)
labels = summarise(lda, dt, vocab, meta, n_clusters=6, seed=0)
trad = np.array([p.meta.get("tradition", "") for p in pieces])
print()
print("=== TRADITION (genre) leakage — headline ===")
print("  clusters<->tradition  ARI=%.3f  AMI=%.3f" % (ARI(trad, labels), AMI(trad, labels)))
print("=== cluster x tradition makeup ===")
for c in sorted(set(labels)):
    tr = collections.Counter(trad[labels == c]); tot = sum(tr.values())
    comp = "  ".join("%s:%.0f%%" % (k, 100*v/tot) for k, v in tr.most_common())
    print("  cluster %d (n=%3d): %s" % (c, tot, comp))
