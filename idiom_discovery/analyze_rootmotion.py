import os, sys, random, collections
import numpy as np
sys.path.insert(0, '/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI, adjusted_mutual_info_score as AMI

C = "/sessions/nice-busy-fermat/mnt/MS/corpora"
random.seed(0)
classical = []
specs = [C+"/expl/dcml_scarlatti", C+"/expl/dcml_mozart", C+"/expl/dcml_beethoven"]
rom = C+"/expl/dcml_romantic"
specs += [os.path.join(rom, s) for s in os.listdir(rom) if os.path.isdir(os.path.join(rom, s, "harmonies"))]
for d in specs:
    ps = load_dcml_repo(d, source="dcml", composer=os.path.basename(d))
    for p in ps: p.meta["tradition"] = "classical"
    classical += ps
jazz = load_jht(C+"/expl/jazz_harmony_treebank/treebank.json")
pop = load_mcgill(C+"/ship/McGill-Billboard")
samp = lambda l, n: random.sample(l, n) if len(l) > n else l
pieces = samp(classical, 380) + samp(jazz, 380) + samp(pop, 380)
random.shuffle(pieces)
trad = np.array([p.meta.get("tradition", "") for p in pieces])

def root_seq(p):
    out = []
    for c in p.chords:
        if c.root_fifths is None: continue
        if not out or out[-1] != c.root_fifths: out.append(c.root_fifths)
    return out
docs_q = [p.transition_tokens() for p in pieces]                                  # WITH quality
docs_r = [["%d>%d" % (s[i], s[i+1]) for i in range(len(s)-1)] for s in (root_seq(p) for p in pieces)]  # root-motion ONLY

def run(docs, label, k=6, ntop=12):
    vec = CountVectorizer(analyzer=lambda d: d, min_df=5, max_df=0.9)
    X = vec.fit_transform(docs)
    lda = LatentDirichletAllocation(n_components=ntop, random_state=0, max_iter=25, learning_method="batch")
    dt = lda.fit_transform(X)
    lab = KMeans(k, random_state=0, n_init=10).fit_predict(dt)
    print("[%-10s] matrix %s  clusters<->tradition  ARI=%.3f  AMI=%.3f" % (label, X.shape, ARI(trad, lab), AMI(trad, lab)))
    return X, vec, lab

print("=== A) transition tokens WITH chord quality (baseline) ===")
Xq, vecq, labq = run(docs_q, "quality")
print("=== B) ROOT-MOTION ONLY (chord quality stripped) ===")
Xr, vecr, labr = run(docs_r, "rootmotion")

feat = vecq.get_feature_names_out()
def topcluster(c, n=12):
    incl = np.asarray(Xq[labq == c].mean(axis=0)).ravel()
    return [feat[i] for i in np.argsort(incl)[::-1][:n]]
print("\n=== cross-cutting clusters in the quality run (top share < 70%) ===")
for c in sorted(set(labq)):
    tr = collections.Counter(trad[labq == c]); tot = sum(tr.values())
    if tr.most_common(1)[0][1] / tot < 0.70:
        print("  c%d  %s" % (c, "  ".join("%s:%.0f%%" % (k, 100*v/tot) for k, v in tr.most_common())))
        print("     idioms:", " ".join(topcluster(c, 12)))
