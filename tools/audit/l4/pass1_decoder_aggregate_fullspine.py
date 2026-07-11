#!/usr/bin/env python3
# Aggregate --dump-fullspine per-stem JSON for the L4 decoder decision/open-question fire counts.
# (Route caveat: fullspine scores under the LIVE home key from L3, not the notated signature.)
import json, glob, sys
from collections import Counter

D = sys.argv[1]
fs = sorted(glob.glob(D + "/*.fs.json"))
dec = Counter(); oq = Counter(); amb = Counter()
tot = 0
comp_lt = 0  # composite < 0.5
extk = extu = altk = altu = 0
for f in fs:
    j = json.loads(open(f, encoding='utf-8').read())
    for r in j.get("regions", []):
        tot += 1
        dec[r.get("l4Decision", "?")] += 1
        oq[r.get("openQuestion", "?")] += 1
        amb[r.get("ambiguityKind", "?")] += 1
        if r.get("l4Composite", 1.0) < 0.5:
            comp_lt += 1
        if r.get("l4ChosenExtKnown"):
            extk += 1
        else:
            extu += 1
print(f"stems={len(fs)}  totalRegions={tot}")
print("l4Decision:", {k: (v, f'{100*v/tot:.1f}%') for k, v in dec.most_common()})
print("openQuestion:", {k: (v, f'{100*v/tot:.1f}%') for k, v in oq.most_common()})
print("ambiguityKind:", {k: (v, f'{100*v/tot:.1f}%') for k, v in amb.most_common()})
print(f"l4Composite < 0.5: {comp_lt} ({100*comp_lt/tot:.1f}%)")
print(f"chosen ext known/unknown (per region): known={extk} unknown={extu}")
