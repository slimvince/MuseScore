"""Line counts and diff sizes for the reading file.

Usage: python3 -I counts.py <reading_file> [--base <file>] [--task2 <file>] [<record_name> ...]
Counts matching lines for the six standard openings, 'as proposed', and each record name given;
with --base / --task2, prints added and deleted line counts against that file, counted from the
system `diff` program's output (lines starting '>' and '<').
"""
import sys, re, subprocess
args = sys.argv[1:]; f = args.pop(0); others = {}
while args and args[0].startswith('--'):
    k = args.pop(0); others[k] = args.pop(0)
lines = open(f, encoding='utf-8').read().split('\n')
pats = [r'\*RULED DISPOSITION \(', r'\*RULED PLACEMENT \(', r'\*RECORDED DISPOSITION \(', r'\*LEAVES L3 \(',
        r'\*Row 7\.67 is not transferred', r'\*NOT QUARANTINED \(', r'as proposed'] + [re.escape(a) for a in args]
for p in pats:
    print(p, sum(1 for l in lines if re.search(p, l)))
for k, g in others.items():
    r = subprocess.run(['diff', g, f], capture_output=True, text=True, encoding='utf-8')
    assert r.returncode in (0, 1), r.stderr
    out = r.stdout.split('\n')
    print(k, 'added', sum(1 for l in out if l.startswith('>')), 'deleted', sum(1 for l in out if l.startswith('<')))
