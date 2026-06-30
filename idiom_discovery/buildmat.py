import os, sys, random, collections
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
sys.path.insert(0, '/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from parsers.choco import load_choco_harte
C = "/sessions/nice-busy-fermat/mnt/MS/corpora"
P = C + "/ship/choco/partitions"
random.seed(0)
# classical: DCML + Corelli (Baroque)
classical = []
specs = [C+"/expl/dcml_scarlatti", C+"/expl/dcml_mozart", C+"/expl/dcml_beethoven", C+"/tools/dcml/corelli"]
rom = C+"/expl/dcml_romantic"
specs += [os.path.join(rom,s) for s in os.listdir(rom) if os.path.isdir(os.path.join(rom,s,"harmonies"))]
for d in specs:
    if not os.path.isdir(os.path.join(d,"harmonies")): 
        # corelli lives under tools/dcml (path uses MS, not corpora) — fix:
        d2 = d.replace(C+"/tools","/sessions/nice-busy-fermat/mnt/MS/tools")
        d = d2 if os.path.isdir(os.path.join(d2,"harmonies")) else d
    ps = load_dcml_repo(d, source="dcml", composer=os.path.basename(d))
    for p in ps: p.meta["tradition"]="classical"
    classical += ps
jazz = load_jht(C+"/expl/jazz_harmony_treebank/treebank.json") + load_choco_harte(P+"/real-book","real-book","jazz",limit=900)
pop  = load_mcgill(C+"/ship/McGill-Billboard") + load_choco_harte(P+"/isophonics","isophonics","pop")
samp = lambda l,n: random.sample(l,n) if len(l)>n else l
N=500
pieces = samp(classical,N)+samp(jazz,N)+samp(pop,N)
random.shuffle(pieces)
print("pools: classical",len(classical),"jazz",len(jazz),"pop",len(pop),"-> using",len(pieces))
trad = np.array([p.meta.get("tradition","") for p in pieces])
docs_q=[p.transition_tokens() for p in pieces]
def rseq(p):
    o=[]
    for c in p.chords:
        if c.root_fifths is not None and (not o or o[-1]!=c.root_fifths): o.append(c.root_fifths)
    return o
docs_r=[["%d>%d"%(s[i],s[i+1]) for i in range(len(s)-1)] for s in (rseq(p) for p in pieces)]
vq=CountVectorizer(analyzer=lambda d:d,min_df=5,max_df=0.9); Xq=vq.fit_transform(docs_q)
vr=CountVectorizer(analyzer=lambda d:d,min_df=5,max_df=0.9); Xr=vr.fit_transform(docs_r)
sparse.save_npz("/tmp/Xq.npz",Xq); sparse.save_npz("/tmp/Xr.npz",Xr)
np.save("/tmp/trad.npy",trad); np.save("/tmp/featq.npy",vq.get_feature_names_out())
print("saved Xq",Xq.shape,"Xr",Xr.shape)
