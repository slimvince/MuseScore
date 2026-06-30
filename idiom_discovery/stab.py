import numpy as np, itertools, collections
from scipy import sparse
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI
trad=np.load("/tmp/trad.npy",allow_pickle=True)
for name,fn in [("quality (with chord quality)","/tmp/Xq.npz"),("root-motion only","/tmp/Xr.npz")]:
    X=sparse.load_npz(fn)
    lda=LatentDirichletAllocation(n_components=12,random_state=0,max_iter=25,learning_method="batch")
    dt=lda.fit_transform(X)
    print("\n=== %s  (X=%s) ===" % (name, X.shape))
    print("  K   trad-ARI mean±sd     self-stability")
    for K in [3,4,5,6,8]:
        labs=[KMeans(K,random_state=s,n_init=10).fit_predict(dt) for s in range(5)]
        t=[ARI(trad,l) for l in labs]
        slf=[ARI(a,b) for a,b in itertools.combinations(labs,2)]
        print("  %d   %.3f ± %.3f        %.3f" % (K, np.mean(t), np.std(t), np.mean(slf)))
# makeup at K=6 on the quality view (does cross-cutting persist at scale?)
X=sparse.load_npz("/tmp/Xq.npz")
dt=LatentDirichletAllocation(n_components=12,random_state=0,max_iter=25,learning_method="batch").fit_transform(X)
lab=KMeans(6,random_state=0,n_init=10).fit_predict(dt)
print("\n=== K=6 cluster x tradition makeup (quality view, expanded corpus) ===")
for c in sorted(set(lab)):
    tr=collections.Counter(trad[lab==c]); tot=sum(tr.values())
    print("  c%d n=%4d: %s" % (c,tot,"  ".join("%s:%.0f%%"%(k,100*v/tot) for k,v in tr.most_common())))
