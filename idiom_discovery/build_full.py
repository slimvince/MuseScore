"""Full-coverage corpus builder for idiom discovery.  Every source, per-source CAPPED
(balance + bound time), ChoCo `ireal-pro` raw EXCLUDED (dup of JHT/iRb).  Auto-includes
the curated .mxl once converted.  FAST=1 skips the slow chordify sources (symbolic only).
Run on the user's machine for the full thing (no 45s cap); chordify is the cost driver."""
import os, sys, random, time
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
sys.path.insert(0,'/sessions/nice-busy-fermat/mnt/MS/idiom_discovery')
from parsers.dcml import load_dcml_repo
from parsers.jht import load_jht
from parsers.mcgill import load_mcgill
from parsers.choco import load_choco_harte, load_choco_m21
from parsers.bach_chordify import load_bach, load_xml_scores
C="/sessions/nice-busy-fermat/mnt/MS/corpora"; P=C+"/ship/choco/partitions"; T="/sessions/nice-busy-fermat/mnt/MS/tools"
FAST=os.environ.get("FAST")=="1"
random.seed(0); t0=time.time(); pieces=[]
def add(ps, trad, sub):
    for p in ps: p.meta["tradition"]=trad; p.meta["sub"]=sub
    pieces.extend(ps); print("  +%-22s %-9s %4d  (%.0fs)"%(sub,trad,len(ps),time.time()-t0))

# --- classical: DCML harmonies (fast) ---
dcml=[(C+"/expl/dcml_scarlatti","scarlatti"),(C+"/expl/dcml_mozart","mozart"),
      (C+"/expl/dcml_beethoven","beethoven"),(T+"/dcml/corelli","corelli"),
      (T+"/dcml/cpe_bach_keyboard","cpe_galant"),(T+"/dcml/bach_en_fr_suites","bach_suites")]
rom=C+"/expl/dcml_romantic"
dcml+=[(os.path.join(rom,s),s) for s in (os.listdir(rom) if os.path.isdir(rom) else []) if os.path.isdir(os.path.join(rom,s,"harmonies"))]
for d,name in dcml:
    add(load_dcml_repo(d,source=name,composer=name),"classical",name)
# --- jazz / pop / folk: symbolic ---
add(load_jht(C+"/expl/jazz_harmony_treebank/treebank.json"),"jazz","jht")
add(load_choco_harte(P+"/real-book","real-book","jazz",limit=1000),"jazz","real-book")
add(load_mcgill(C+"/ship/McGill-Billboard"),"pop","mcgill")
add(load_choco_harte(P+"/isophonics","isophonics","pop"),"pop","isophonics")
add(load_choco_m21(P+"/nottingham","nottingham","folk",limit=1000),"folk","nottingham")
# --- chordify sources (slow) ---
if not FAST:
    add(load_bach(limit=200),"classical","bach_chorale")
    for fld,sub in [(T+"/corpus_rampageswing_full","rampageswing"),(T+"/corpus_effendi_src","effendi")]:
        add(load_xml_scores(fld,sub,"jazz"),"jazz",sub)
    cur=C+"/expl/curated_mxl"
    for sub,trad in [("steely_dan","pop"),("piazzolla","classical"),("hiromi","jazz")]:
        d=os.path.join(cur,sub)
        if os.path.isdir(d): add(load_xml_scores(d,sub,trad),trad,sub)
        else: print("  (curated %s not converted yet — skipped)"%sub)

trad=np.array([p.meta["tradition"] for p in pieces]); sub=np.array([p.meta["sub"] for p in pieces])
docs=[p.transition_tokens() for p in pieces]
vq=CountVectorizer(analyzer=lambda d:d,min_df=5,max_df=0.9); Xq=vq.fit_transform(docs)
tag="fast" if FAST else "full"
sparse.save_npz("/tmp/Xf_%s.npz"%tag,Xq); np.save("/tmp/tradf_%s.npy"%tag,trad)
np.save("/tmp/subf_%s.npy"%tag,sub); np.save("/tmp/featf_%s.npy"%tag,vq.get_feature_names_out())
import collections
print("TOTAL %d pieces in %.0fs  matrix %s"%(len(pieces),time.time()-t0,Xq.shape))
print("by tradition:",dict(collections.Counter(trad)))
