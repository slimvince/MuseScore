"""Rebuild the L3 reading file from a committed base blob and an instruction's own text.

Usage: python3 -I rebuild.py <objects_dir> <base_blob> <instruction.md> <out_file> [<compare_file>]

What it applies, taken from the instruction's text only:
  - every code block introduced by a line '*Row <n>.<m> — <k> line(s)...' : its k lines go to
    that row, each followed by one blank line, inserted after the blank line that ends the
    row's '*PROPOSED DISPOSITION.*' paragraph, in the block's order;
  - the one line of the instruction that, stripped, starts with '`*Application in progress'
    replaces the reading file's line 54.
It STOPS (AssertionError) when: a row heading '^**Row <n>.<m> —' is not found exactly once;
a row has not exactly one '*PROPOSED DISPOSITION.*' line before its '---'; a row already
carries a '*RULED' or '*RECORDED' line; a code block's line count differs from its heading;
line 54 is not an in-progress line; or there is not exactly one in-progress line.
It does NOT apply: lines placed elsewhere than after the proposed paragraph, rows with earlier
ruled or recorded lines, transfer-list (§10) entries, audit-question (§11) lines, or any other
kind of change. An instruction that orders one of those needs this script extended first,
and the extension established again (README).
Prints each row's placement, then the rebuilt file's blob, size and line count; with
<compare_file>, prints IDENTICAL or DIFFERS.
"""
import sys, os, re, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import load

od, base_h, instr, out = sys.argv[1:5]
cmpf = sys.argv[5] if len(sys.argv) > 5 else None
t, base = load(od, base_h); assert t == 'blob %d' % len(base), t
ins = open(instr, encoding='utf-8').read().split('\n')

rows = []; i = 0
while i < len(ins):
    m = re.match(r'^\*Row (\d+\.\d+) — (\d+) lines?', ins[i])
    if m:
        assert ins[i+1] == '```', ('no code block after', ins[i])
        j = i + 2; L = []
        while ins[j] != '```': L.append(ins[j]); j += 1
        assert len(L) == int(m.group(2)), ('line count', m.group(1), len(L))
        rows.append((m.group(1), L)); i = j
    i += 1
prog = [l.strip() for l in ins if l.strip().startswith('`*Application in progress')]
assert len(prog) == 1, ('in-progress lines found', len(prog))
prog = prog[0][1:-1]

lines = base.decode('utf-8').split('\n')
assert lines[53].startswith('*Application in progress'), 'line 54 is not the in-progress line'
lines[53] = prog
inserts = []
for r, L in rows:
    hits = [k for k, l in enumerate(lines) if re.match(r'^\*\*Row ' + re.escape(r) + ' —', l)]
    assert len(hits) == 1, ('row heading matches', r, hits)
    h = hits[0]
    end = next(k for k in range(h + 1, len(lines)) if lines[k] == '---')
    pd = [k for k in range(h, end) if lines[k].startswith('*PROPOSED DISPOSITION.*')]
    assert len(pd) == 1, ('proposed paragraphs', r, pd)
    assert not any(lines[x].startswith(('*RULED', '*RECORDED')) for x in range(h, end)), ('earlier line at', r)
    k = pd[0]
    while lines[k] != '': k += 1
    inserts.append((k + 1, L, r, lines[k + 1][:40]))
for pos, L, r, nxt in sorted(inserts, reverse=True):
    new = []
    for l in L: new += [l, '']
    lines[pos:pos] = new
for pos, L, r, nxt in sorted(inserts):
    print('Row', r, len(L), 'line(s) inserted before:', repr(nxt))
data = '\n'.join(lines).encode('utf-8')
open(out, 'wb').write(data)
print('rows', len(rows), 'lines', sum(len(L) for _, L in rows))
print('blob', hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest(), len(data), data.count(b'\n'))
if cmpf:
    print('compare:', 'IDENTICAL' if open(cmpf, 'rb').read() == data else 'DIFFERS')
