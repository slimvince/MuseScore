import os, sys, random
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
sys.path.insert(0, '/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from parsers.choco import load_choco_harte, load_choco_m21
from parsers.bach_chordify import load_bach
C="/sessions/nice-busy-fermat/mnt/MS/corpora"; P=C+"/ship/choco/partitions"
T="/sessions/nice-busy-fermat/mnt/MS/tools"
random.seed(0)
classical=[]
specs=[C+"/expl/dcml_scarlatti",C+"/expl/dcml_mozart",C+"/expl/dcml_beethoven",T+"/dcml/corelli"]
rom=C+"/expl/dcml_romantic"
specs+=[os.path.join(rom,s) for s in os.listdir(rom) if os.path.isdir(os.path.join(rom,s,"harmonies"))]
for d in specs:
    ps=load_dcml_repo(d,source="dcml",composer=os.path.basename(d))
    for p in ps: p.meta["tradition"]="classical"; p.meta["sub"]="dcml"
    classical+=ps
bach=load_bach(limit=40)
for p in bach: p.meta["sub"]="bach"
classical+=bach
jazz=load_jht(C+"/expl/jazz_harmony_treebank/treebank.json")+load_choco_harte(P+"/real-book","real-book","jazz",limit=500)
for p in jazz: p.meta["sub"]="jazz"
pop=load_mcgill(C+"/ship/McGill-Billboard")+load_choco_harte(P+"/isophonics","isophonics","pop")
for p in pop: p.meta["sub"]="pop"
folk=load_choco_m21(P+"/nottingham","nottingham","folk",limit=500)
for p in folk: p.meta["sub"]="folk"
samp=lambda l,n: random.sample(l,n) if len(l)>n else l
N=400
pieces=samp(classical,N)+samp(jazz,N)+samp(pop,N)+samp(folk,N)
random.shuffle(pieces)
print("pools: cl",len(classical),"(bach",len(bach),") jz",len(jazz),"pop",len(pop),"folk",len(folk),"-> using",len(pieces))
trad=np.array([p.meta.get("tradition","") for p in pieces])
sub=np.array([p.meta.get("sub","") for p in pieces])
docs=[p.transition_tokens() for p in pieces]
vq=CountVectorizer(analyzer=lambda d:d,min_df=5,max_df=0.9); Xq=vq.fit_transform(docs)
sparse.save_npz("/tmp/X2.npz",Xq); np.save("/tmp/trad2.npy",trad); np.save("/tmp/sub2.npy",sub); np.save("/tmp/feat2.npy",vq.get_feature_names_out())
print("saved X2",Xq.shape)
