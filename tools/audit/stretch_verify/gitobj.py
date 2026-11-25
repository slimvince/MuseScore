"""Read loose git objects from a STAGED copy of .git/objects, recomputing each SHA-1.

Usage: python3 -I gitobj.py <objects_dir> <hash> [<hash> ...]
Prints each object's type and, for a commit, its text; for a tree, its entries.
Stops with an AssertionError if an object's recomputed SHA-1 differs from its name.
Packed objects are not read; a missing loose object raises FileNotFoundError.
"""
import sys, os, zlib, hashlib

def load(objects_dir, h):
    p = os.path.join(objects_dir, h[:2], h[2:])          # folder = first 2 chars, file = other 38
    raw = zlib.decompress(open(p, 'rb').read())
    assert hashlib.sha1(raw).hexdigest() == h, ('HASH MISMATCH', h)
    hdr, body = raw.split(b'\0', 1)
    return hdr.decode(), body

def tree_entries(body):
    out = []; i = 0
    while i < len(body):
        sp = body.index(b' ', i); nul = body.index(b'\0', sp)
        out.append((body[i:sp].decode(), body[sp+1:nul].decode(), body[nul+1:nul+21].hex()))
        i = nul + 21
    return out

if __name__ == '__main__':
    od = sys.argv[1]
    for h in sys.argv[2:]:
        t, b = load(od, h)
        print('==', h, t, 'hash ok')
        if t.startswith('tree'):
            for e in tree_entries(b): print('  ', *e)
        elif t.startswith('commit'):
            print(b.decode())
