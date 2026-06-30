# Idiom discovery — full balanced run + cap-robustness sweep (2026-06-30)

## cap=400  (4320 pieces, 32s)  by-tradition={'jazz': 1742, 'pop': 1417, 'classical': 761, 'folk': 400}
  clusters<->tradition ARI = 0.166
   c0 [jazz:93%  pop:7%]  5:dom7>4:min7 5:halfdim7>4:dom7 1:dom7>0:maj7 4:halfdim7>3:dom7 0:maj7>3:min7 4:dom7>3:min7
   c1 [pop:76%  folk:10%  classical:8%]  0:maj>-2:maj 2:min>-2:maj -2:maj>-1:maj 1:min>0:maj -2:maj>0:maj 1:maj>-1:maj
   c2 [jazz:34%  pop:33%  classical:31%]  -6:dom7>-7:maj -2:maj>0:min 0:min>-2:maj -3:maj>0:min 0:min>-3:maj -4:maj>-3:maj
   c3 [jazz:83%  pop:17%  folk:1%]  -1:dom7>0:dom7 0:other>-2:other 0:dom7>1:dom7 0:dom7>4:min7 -2:other>0:other 0:dom7>2:min7
   c4 [classical:43%  folk:35%  pop:13%]  3:min>1:dom7 0:maj>5:dim 0:maj>1:dom7 5:dim>0:maj 2:min>1:dom7 1:maj>2:dom7
   c5 [jazz:68%  pop:28%  classical:2%]  -1:dom7>0:maj 0:maj>-1:dom7 0:maj>3:dom7 0:maj>4:dom7 0:maj>0:maj7 1:dom7>2:min7

## cap=700  (6882 pieces, 216s)  by-tradition={'jazz': 2806, 'classical': 1061, 'pop': 2315, 'folk': 700}
  clusters<->tradition ARI = 0.184
   c0 [jazz:92%  pop:8%]  -1:dom7>0:dom7 0:dom7>1:dom7 0:dom7>3:dom7 1:dom7>0:maj7 4:dom7>3:min7 4:min7>3:dom7
   c1 [classical:68%  pop:16%  jazz:12%]  2:dim>0:min -1:min>2:dim 0:min>-5:maj -2:maj>-2:dom7 0:min>-1:min 2:dim>1:maj
   c2 [folk:53%  pop:24%  jazz:20%]  3:min>1:dom7 2:min>1:dom7 -1:maj>1:dom7 0:maj>1:dom7 1:dom7>0:maj 0:maj>2:dom7
   c3 [pop:75%  folk:13%  classical:7%]  2:maj>4:min 2:maj>0:maj 4:min>2:maj 0:maj>2:maj 1:maj>2:maj 4:min>0:maj
   c4 [pop:86%  folk:10%  jazz:5%]  -2:maj>0:min -4:maj>-2:maj 0:min>-2:maj 2:min>-2:maj -2:maj>0:maj 1:min>0:maj
   c5 [jazz:52%  pop:28%  classical:18%]  -6:dom7>-7:maj 1:dom7>0:min7 0:min7>-1:dom7 5:dim>0:maj 0:maj>5:dim 3:dom7>2:min

## cap=1200  (9427 pieces, 270s)  by-tradition={'jazz': 4163, 'pop': 3501, 'classical': 761, 'folk': 1002}
  clusters<->tradition ARI = 0.163
   c0 [jazz:67%  pop:30%  folk:2%]  0:maj>-1:dom7 0:maj>4:dom7 0:maj>3:dom7 -1:dom7>0:maj -1:maj>-1:min 1:dom7>2:min7
   c1 [jazz:92%  pop:8%]  0:dom7>-1:maj7 5:halfdim7>4:dom7 1:dom7>0:maj7 5:dom7>4:min7 4:dom7>3:min7 0:maj7>2:min7
   c2 [jazz:79%  pop:21%]  -1:dom7>0:min7 -1:dom7>-2:min7 -1:min7>0:min7 1:min7>0:min7 0:min7>-1:min7 0:min7>-1:dom7
   c3 [folk:53%  pop:30%  jazz:12%]  3:min>1:dom7 -1:maj>1:dom7 2:min>1:dom7 0:maj>1:dom7 1:dom7>0:maj 0:maj>-1:maj
   c4 [pop:79%  folk:11%  jazz:6%]  2:maj>4:min 4:min>2:maj 2:maj>0:maj 0:maj>2:maj 4:min>0:maj 1:maj>2:maj
   c5 [pop:49%  classical:28%  jazz:17%]  0:min>5:dim 0:min>-3:maj -2:maj>0:min 5:dim>0:min 0:min>-2:maj 0:min>1:min

## curated probe (where Steely Dan / Piazzolla / Hiromi land)
   steely_dan  (n=22) -> c5:100%
   piazzolla   (n=6) -> c5:83%  c1:17%
   hiromi      (n=19) -> c5:100%

# done in 490s
