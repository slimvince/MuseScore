"""Git blob identity of files as they are, with size, line-feed count and carriage-return flag.

Usage: python3 -I blobhash.py <file> [<file> ...]
"""
import sys, hashlib
for p in sys.argv[1:]:
    d = open(p, 'rb').read()
    print(hashlib.sha1(b'blob %d\0' % len(d) + d).hexdigest(), len(d), d.count(b'\n'),
          'CR' if b'\r' in d else 'noCR', p)
