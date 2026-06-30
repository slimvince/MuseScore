import numpy as np, collections
from scipy import sparse
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI
X=sparse.load_npz("/tmp/X2.npz"); trad=np.load("/tmp/trad2.npy",allow_pickle=True)
sub=np.load("/tmp/sub2.npy",allow_pickle=True); feat=np.load("/tmp/feat2.npy",allow_pickle=True)
Xd=np.asarray(X.todense()); overall=Xd.mean(axis=0)+1e-9
dt=LatentDirichletAllocation(12,random_state=0,max_iter=25,learning_method="batch").fit_transform(X)
for K in [5,6]:
    lab=KMeans(K,random_state=0,n_init=10).fit_predict(dt)
    print("\n################ K=%d  (clusters<->tradition ARI=%.3f) ################"%(K,ARI(trad,lab)))
    for c in sorted(set(lab)):
        m=lab==c; n=int(m.sum()); tr=collections.Counter(trad[m])
        mk="  ".join("%s:%.0f%%"%(k,100*v/n) for k,v in tr.most_common())
        incl=Xd[m].mean(axis=0); lift=incl/overall
        cand=[i for i in range(len(feat)) if incl[i]>=0.30]; cand.sort(key=lambda i:-lift[i])
        dist=" ".join("%s"%feat[i] for i in cand[:7])
        print(" c%d n=%d [%s]\n    idioms: %s"%(c,n,mk,dist))
    # where do bach and folk land?
    for s in ["bach","folk"]:
        d=collections.Counter(lab[sub==s]); tot=sum(d.values())
        print("  %s lands in: %s"%(s,"  ".join("c%d:%.0f%%"%(c,100*v/tot) for c,v in d.most_common())))
