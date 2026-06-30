import numpy as np, collections, pickle
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
X=sparse.load_npz("/tmp/Xf_fast.npz"); trad=np.load("/tmp/tradf_fast.npy",allow_pickle=True)
feat=list(np.load("/tmp/featf_fast.npy",allow_pickle=True))
cur=pickle.load(open("/tmp/curated.pkl","rb"))
cur=[c for c in cur if len(c[3])>=5]   # drop empty/failed
cdocs=[c[3] for c in cur]; csets=np.array([c[1] for c in cur])
vec=CountVectorizer(analyzer=lambda d:d, vocabulary=feat); Xc=vec.transform(cdocs)
lda=LatentDirichletAllocation(12,random_state=0,max_iter=25,learning_method="batch").fit(X)
dts=lda.transform(X); dtc=lda.transform(Xc)
km=KMeans(6,random_state=0,n_init=10).fit(dts); ls=km.labels_; lc=km.predict(dtc)
Xd=np.asarray(X.todense()); overall=Xd.mean(axis=0)+1e-9
print("=== the 6 idiom clusters (tradition makeup + signature) ===")
for c in sorted(set(ls)):
    m=ls==c; tr=collections.Counter(trad[m]); n=int(m.sum())
    mk="  ".join("%s:%.0f%%"%(k,100*v/n) for k,v in tr.most_common(3))
    incl=Xd[m].mean(axis=0); lift=incl/overall
    cand=[i for i in range(len(feat)) if incl[i]>=0.30]; cand.sort(key=lambda i:-lift[i])
    print(" c%d [%s]  %s"%(c,mk," ".join(feat[i] for i in cand[:5])))
print("\n=== WHERE THE CURATED SCORES LAND ===")
for s in ["steely_dan","piazzolla","hiromi"]:
    d=collections.Counter(lc[csets==s]); tot=sum(d.values())
    print("  %-11s (n=%2d): %s"%(s,tot,"  ".join("c%d:%.0f%%"%(c,100*v/tot) for c,v in d.most_common())))
