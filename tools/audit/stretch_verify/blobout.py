"""Write a loose git blob's content (its SHA-1 recomputed first) to a file.

Usage: python3 -I blobout.py <objects_dir> <blob_hash> <out_file>
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import load
od, h, out = sys.argv[1:4]
t, b = load(od, h); assert t == 'blob %d' % len(b), t
open(out, 'wb').write(b); print('wrote', h, len(b), 'bytes to', out)
