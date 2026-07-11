#!/usr/bin/env python3
# Aggregate --decode-chords per-stem JSON into decoder-mechanism fire counts.
import json, sys
from pathlib import Path
from collections import Counter

D = Path(sys.argv[1])
files = sorted(D.glob("*.decode.json"))
stems = len(files)
tot=named=uncertain=abstain=empty=0
alt_ge1=alt_atcap=alt_zero=0
nct_fired=ct_fired=0
sentinel=0
qual=Counter()
altcount=Counter()
noteCountAbstain=Counter()
for f in files:
    j=json.loads(f.read_text(encoding='utf-8'))
    for r in j.get("regions",[]):
        tot+=1
        hc=r["hasChord"]
        if hc: named+=1
        else:
            abstain+=1
            noteCountAbstain[r.get("noteCount",-1)]+=1
        if r["uncertain"]: uncertain+=1
        if r.get("noteCount",0)==0: empty+=1
        alts=r.get("alternatives",[])
        altcount[len(alts)]+=1
        if len(alts)>=1: alt_ge1+=1
        if len(alts)==0: alt_zero+=1
        if len(alts)>=6: alt_atcap+=1
        nc=r.get("noteClassifications",{})
        if nc.get("nonChordTones"): nct_fired+=1
        if nc.get("chordTones"): ct_fired+=1
        # confidence sentinel (no different competitor) => confidence ~1000
        if r.get("confidence",0)>=999.0: sentinel+=1
        if hc: qual[r.get("quality","?")]+=1
print(f"stems={stems}  totalSlices={tot}")
print(f"named(hasChord=Commit+Inherit) = {named} ({100*named/tot:.1f}%)")
print(f"abstain(!hasChord)             = {abstain} ({100*abstain/tot:.1f}%)")
print(f"uncertain flag set             = {uncertain} ({100*uncertain/tot:.1f}%)")
print(f"empty slice (noteCount==0)     = {empty}")
print(f"no-competitor sentinel (conf>=999) = {sentinel} ({100*sentinel/tot:.1f}%)")
print(f"slices carrying >=1 alternative= {alt_ge1} ({100*alt_ge1/tot:.1f}%)")
print(f"slices with 0 alternatives     = {alt_zero} ({100*alt_zero/tot:.1f}%)")
print(f"slices at topK cap (>=6 alts)  = {alt_atcap} ({100*alt_atcap/tot:.1f}%)")
print(f"membership NCT non-empty       = {nct_fired} ({100*nct_fired/tot:.1f}%)")
print(f"membership CT non-empty        = {ct_fired} ({100*ct_fired/tot:.1f}%)")
print("alt-count histogram:", dict(sorted(altcount.items())))
print("chosen-quality (named slices):", dict(qual.most_common()))
aug=qual.get("Augmented",0); dim=qual.get("Diminished",0)
print(f"spelling-pin population (chosen Aug or Dim) = {aug+dim} (Aug={aug} Dim={dim})")
print("abstain noteCount histogram:", dict(sorted(noteCountAbstain.items())))
