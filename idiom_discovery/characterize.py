import numpy as np, collections
from scipy import sparse
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
X=sparse.load_npz("/tmp/Xq.npz"); trad=np.load("/tmp/trad.npy",allow_pickle=True)
feat=np.load("/tmp/featq.npy",allow_pickle=True)
Xd=np.asarray(X.todense()); overall=Xd.mean(axis=0)+1e-9
dt=LatentDirichletAllocation(12,random_state=0,max_iter=25,learning_method="batch").fit_transform(X)
for K in [4,5]:
    lab=KMeans(K,random_state=0,n_init=10).fit_predict(dt)
    print("\n################ K=%d ################"%K)
    for c in sorted(set(lab)):
        m=lab==c; n=int(m.sum()); tr=collections.Counter(trad[m])
        makeup="  ".join("%s:%.0f%%"%(k,100*v/n) for k,v in tr.most_common())
        incl=Xd[m].mean(axis=0); lift=incl/overall
        cand=[i for i in range(len(feat)) if incl[i]>=0.30]
        cand.sort(key=lambda i:-lift[i])
        distinct=["%s(x%.1f)"%(feat[i],lift[i]) for i in cand[:8]]
        freq=[feat[i] for i in np.argsort(incl)[::-1][:8]]
        print("\n c%d  n=%d  [%s]"%(c,n,makeup))
        print("   frequent:   ", " ".join(freq))
        print("   distinctive:", " ".join(distinct))
