"""Compare pairs of git tree objects (one level each) from a staged .git/objects.

Usage: python3 -I treediff.py <objects_dir> <treeA>:<treeB> [<treeA>:<treeB> ...]
Prints every entry name whose mode or object differs (None = absent on that side).
Walk a changed path by staging the next level's two trees and running again.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import load, tree_entries

def entries(od, h):
    t, b = load(od, h); assert t.startswith('tree'), (h, t)
    return {n: (m, s) for m, n, s in tree_entries(b)}

if __name__ == '__main__':
    od = sys.argv[1]
    for pair in sys.argv[2:]:
        a, b = pair.split(':'); A, B = entries(od, a), entries(od, b)
        print('==', a[:8], '->', b[:8])
        for n in sorted(set(A) | set(B)):
            if A.get(n) != B.get(n): print('  ', n, A.get(n), '->', B.get(n))
