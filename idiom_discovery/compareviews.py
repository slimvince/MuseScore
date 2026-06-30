import numpy as np, collections
from scipy import sparse
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI
X2=sparse.load_npz("/tmp/X2.npz"); Xp=np.load("/tmp/Xp.npy")
trad=np.load("/tmp/trad2.npy",allow_pickle=True)
K=6
# progression view (transition tokens -> LDA -> KMeans)
dt=LatentDirichletAllocation(12,random_state=0,max_iter=25,learning_method="batch").fit_transform(X2)
labp=KMeans(K,random_state=0,n_init=10).fit_predict(dt)
# vocabulary view (Moss-style tonal profile -> KMeans)
labv=KMeans(K,random_state=0,n_init=10).fit_predict(Xp)
print("progression-view  clusters<->tradition  ARI=%.3f"%ARI(trad,labp))
print("vocabulary-view   clusters<->tradition  ARI=%.3f"%ARI(trad,labv))
print("AGREEMENT  progression<->vocabulary      ARI=%.3f"%ARI(labp,labv))
print("\n=== vocabulary-view clusters (tradition makeup + tonal-profile peak fifths) ===")
for c in sorted(set(labv)):
    m=labv==c; n=int(m.sum()); tr=collections.Counter(trad[m])
    mk="  ".join("%s:%.0f%%"%(k,100*v/n) for k,v in tr.most_common())
    prof=Xp[m].mean(axis=0)
    peaks=sorted(range(25),key=lambda i:-prof[i])[:7]
    peakf=sorted(p-12 for p in peaks)  # fifths positions (0=tonic,+1=dom,-1=subdom)
    print(" v%d n=%d [%s]  profile mass at fifths %s"%(c,n,mk,peakf))
