# CC dispatch — the L3 application, SESSION 8 of several: the full check of Task 1 (Task 1 (e) and E1) over the whole successor, and nothing else

> **STATUS: RELEASED 2026-11-22** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety.md`, under Ruling 1 of
> `records/cowork/rulings/cowork_rulings_2026_11_22_l3_application_split_into_sessions_sitting.md` (the user's word "C":
> the big dispatch is executed by several new Claude Code sessions in turn). Executed by Claude Code when the user hands
> it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that step
> and report it. Do not continue to the next one.**

## 0. What this file is

The L3 application dispatch, `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` (called **the big
dispatch** below; 941,330 bytes, 7,157 lines, git blob `b5274c2c7b82c171e1b44c1ed79635a34877b142`), is executed by
several Claude Code sessions in turn. Session 1 executed its Task 0. Sessions 2 to 7 applied Task 1, the successor file
`cowork_derived_specification_l3_2026_11_08.md`, in six stretches covering §L.1 to §L.55, each stretch committed,
pushed and checked against the stretch before it. Session 7's commits are `c011244275e9df9916b90241fc277816da501a22`,
`0241e328f773cafe7ebfeb83b634f26838a8c268` (the successor, blob `b4397e720b52f0f8afb23dbc47e675303cdc212d`) and
`ae8fa501c2d4517f6930ad406030f2119b5f161c` (its report), all verified at the objects by the Cowork sitting that wrote
entry 1190.

**This is session 8. It runs the check of the big dispatch's Task 1 (e) and E1 over the WHOLE successor: the diff of
the successor against the derivation object, with every changed passage attributed in a table. It writes that table
and the check's other results into a report, commits and pushes the report, and STOPS.** It edits no file other than
writing its report. In particular it does not edit the successor, whatever the check finds.

**How the attribution is done, and why.** Every one of sessions 2 to 7 already attributed every changed passage of its
own stretch, in a table in its report, against the successor version before it. The full diff is the sum of those six
steps. So this session does not re-derive any attribution from the ruling ledger (§L, about 5,500 lines of the big dispatch, which do
not fit beside this check). Instead a read-only script (§3, given whole) follows every line of the successor back through
the six versions to the session that wrote it, and lists, for every changed passage of the full diff, the session and
the changed passage of that session's own diff it came from. You then read each attribution off that session's report
table. The script also runs the counting checks of Task 1 (e). The writing side ran the script over the same git objects
on 2026-11-22 and its expected results are given in §3.

**The big dispatch stays the authority for every order it gives.** This file replaces only the orders listed in §4,
and only for this session. Where this file and the big dispatch seem to differ on anything §4 does not list, STOP and
report; do not choose.

**Documentation only. No algorithm change is decided by this session.** It checks a file already written and decides
nothing about the specification.

## 1. First checks — before any other act

Every shell command carries `; echo "exit:$?"` (`CLAUDE.md`, the bash-rules section).

1. **The tip.** Read with the Read tool: `.git/HEAD` must read `ref: refs/heads/master`; `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master` must both read `ae8fa501c2d4517f6930ad406030f2119b5f161c`. Anything else: STOP and
   report what you found. Do not try to find out what moved it.
2. **The big dispatch is unchanged.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_2026_11_08.md; echo "exit:$?"` must print
   `b5274c2c7b82c171e1b44c1ed79635a34877b142`. Anything else: STOP and report.
3. **This instruction's own identity, for the report.**
   `git hash-object records/cc/instructions/cc_instruction_l3_application_session_8_task_1_check_2026_11_22.md; echo "exit:$?"`.
   Record the hash. There is no expected value.
4. **The successor stands as session 7 committed it.**
   `git hash-object cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"` must print
   `b4397e720b52f0f8afb23dbc47e675303cdc212d`, and
   `git ls-tree ae8fa501c2d4517f6930ad406030f2119b5f161c -- cowork_derived_specification_l3_2026_11_08.md; echo "exit:$?"`
   must show the same blob. Anything else: STOP and report.
5. **The seven versions the check reads exist as git objects.** For each of the seven blobs in the script's `CHAIN`
   list (§3), `git cat-file -t <blob>; echo "exit:$?"` must print `blob`. And the derivation at the declared start tip
   is the first of them:
   `git ls-tree e855ff2a38883bc453b3f1c83cb20b9fd89cda05 -- cowork_blind_derivation_l3_2026_10_17.md; echo "exit:$?"`
   must show blob `c01793f98c51e0267fb0dc7487613ac477cc1fbb`. Anything else: STOP and report.
6. **The working tree.** Enumerate it with `tools/audit/changed_paths.py` (the sanctioned tool; the guard refuses
   `git status`). Write its output to your session scratchpad and read it there with the file tools; do not pipe it to
   another command.
   - **Tracked modifications expected: exactly one,** `tools/audit/claude_md_finer_archive.json`, which differs from the
     tip only in line endings. Prove it: `git hash-object tools/audit/claude_md_finer_archive.json; echo "exit:$?"` must
     print `1df4f20771b6782cbb965c293db4d445bc7ec892`, and `git ls-tree ae8fa501c2d4517f6930ad406030f2119b5f161c -- tools/audit/claude_md_finer_archive.json; echo "exit:$?"`
     must show the same blob. If both hold, it is not a modification and is not landed. Any other tracked modification,
     or either hash differing: STOP and report.
   - **Untracked paths expected:** the two files §5 act 1 lands (this instruction and handoff entry 1190), plus the 393
     untracked paths sessions 2 to 7 reported and did not land (387 under `scratch_artifacts/`; `Claude outputs/`;
     `Codex research inventory/`; `docs/research_papers/polyph9-release/`; the two PDFs under
     `external resarch summary/`; `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). `.claude/` and
     `tools/extra scores/.mscbackup/` exist but are git-ignored, so the tool does not list them; that is expected and
     not a STOP. List in the report every untracked path the tool reports outside those. A further untracked
     `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` is the writing side's, is not landed and is not a STOP (the
     big dispatch's A1, unchanged).

## 2. What you read, in this order (replaces the big dispatch's line 98 for this session)

1. **This file** — your first tool call, alone (the opening line the user gives you says so).
2. **The six session reports, each WHOLE**, in this order:
   - `records/cc/reports/cc_report_l3_application_session_2_task_1_stretch_1_2026_11_22.md` (23,097 bytes)
   - `records/cc/reports/cc_report_l3_application_session_3_task_1_stretch_2_2026_11_22.md` (18,829 bytes)
   - `records/cc/reports/cc_report_l3_application_session_4_task_1_stretch_3_2026_11_22.md` (15,627 bytes)
   - `records/cc/reports/cc_report_l3_application_session_5_task_1_stretch_4_2026_11_22.md` (15,814 bytes)
   - `records/cc/reports/cc_report_l3_application_session_6_task_1_stretch_5_2026_11_22.md` (14,070 bytes)
   - `records/cc/reports/cc_report_l3_application_session_7_task_1_stretch_6_2026_11_22.md` (15,015 bytes)

   Their diff tables are the source of every attribution you write. Note the STOP-and-report items each one lists (for
   example session 2's §L.15 amendment 4) for §6 item 6.
3. **Session 3's instruction at lines 161–168 only:**
   `records/cc/instructions/cc_instruction_l3_application_session_3_task_1_stretch_2_2026_11_22.md`. These lines are
   the staleness fix that instruction added at the end of the successor's §4; §4 item 3 below explains why you read
   them.
4. **`CLAUDE.md`** is loaded whole into your context at session start as a project memory file. Do not read it again.
   If your context does NOT show `C:\s\MS\CLAUDE.md` as a loaded memory file, STOP and report.
5. **The ordinary session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in ranges of about 150 lines; and the
   gating answer — **only the list** `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
   `gating_ids`, as `CLAUDE.md`'s open-items register section, rule (a), names it. Do not read the rest of that section
   or the open-items index. **`BUILD_AND_TEST.md` is not read**: this session builds nothing, runs no test and no guard.
6. **`records/cowork/handoff/cowork_handoff.md` at its topmost block** (lines 1 to 255; the dispatch-protocol clause on
   the read-first block), and **two handoff entries, whole**:
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety.md` (the current entry point,
   written by the sitting before the one that wrote this file; untracked, §5 act 1 lands it) and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_eighty_nine.md` (the one before it).
7. **`cowork_audit_protocol.md`'s section headed *"The dispatch protocol these audits are commissioned and run under"***
   (from its line 180 to the end): every `###` section in it that carries the standing-clause marker.
8. **`DEFECT_TYPES.md` whole** (18,368 bytes), for the self-check after the work.
9. **The big dispatch, at these lines only, with the Read tool by line range:**
   - lines 1–37;
   - lines 59–97;
   - **line 98 from the git blob**, as it is about 4,400 bytes long and the guard refuses `sed` on the working-tree file:
     `git cat-file -p b5274c2c7b82c171e1b44c1ed79635a34877b142 | sed -n '98p' | fold -s -w 1000; echo "exit:$?"`;
   - lines 99–394 (the words, the ruling ledger's opening, the forms, the premise ledger, the declared start state, the
     standing bars, the findings rule);
   - lines 395–430 (how §L is written);
   - **lines 6100–6571 (Task 1, whole; (d), (e) and E1 are at its end, lines 6543–6563)**;
   - lines 7111–7135 (*What this batch does NOT do*).

   **Do not read in this session:** lines 38–58; lines 431–5906 (the ledger entries §L.1 to §L.55, already applied and
   attributed by sessions 2 to 7); lines 5907–6099 (Task 0); lines 6572–7110 (Tasks 2 to 5); lines 7136 to the end.
   Nor the successor whole, the derivation whole, the ruling records, the reading file, `FRAMEWORK.md` or
   `records/cowork/handoff/cowork_away_returns.md`. The script reads the successor and the derivation as git objects;
   where a table row needs a successor line looked at, read that line range at the git object
   (`git show b4397e720b52f0f8afb23dbc47e675303cdc212d` written to a scratch path and read with the Read tool in that
   range only). When you search the big dispatch, search only inside the ranges above.

## 3. The check script — given whole, run once

**What it is.** A read-only Python script. It reads git objects by explicit hash only (`git cat-file -p <blob>` and
`git diff -U0 <blob> <blob>`), writes nothing but its printed output, and ends with exit 1 if any of its checks fails. It is
NOT a repository file: write it into your session scratchpad, outside the repository, with the Write tool, exactly as
below. The big dispatch's bar on writing `tools/audit/*.py` is untouched by it.

**Write it** to `<your scratchpad>/l3_session8_trace.py`, the text between the two fence lines, nothing added. Then
prove it is the tested text: `git hash-object --no-filters "<your scratchpad>/l3_session8_trace.py"; echo "exit:$?"`
must print `82800a17865009f35e5abf7c6153ce4eba1a9d85`. If it prints anything else, check whether the file carries
carriage returns (`python -I -c "import sys; print(b'\r' in open(sys.argv[1],'rb').read())" "<your scratchpad>/l3_session8_trace.py"; echo "exit:$?"`):
if it does, write it again without them and re-check; any other difference is a STOP-and-report. Do not edit the
script to make it run.

```python
# Read-only check for session 8 of the L3 application. Reads git objects by explicit hash only
# (git cat-file -p, git diff -U0 between two blobs). Writes nothing. Run from the repository root:
#   python -I <this file> > <scratch output file>
import re, subprocess, sys

CHAIN = [
    ("derivation", "c01793f98c51e0267fb0dc7487613ac477cc1fbb"),
    ("session 2", "e5c7ef48aba2f0c8f5f65c0bf100acfc949101a1"),
    ("session 3", "32cf8fdb7e942168a4ce153b3ccbcd8be081deca"),
    ("session 4", "b77ee3306957e14a1862dd98d928c1b8005b7824"),
    ("session 5", "a76ffaec74802d82d827cbffeb80930ab3d86687"),
    ("session 6", "668eacc479f4fc812f8459aa4f25726c1da2044c"),
    ("session 7", "b4397e720b52f0f8afb23dbc47e675303cdc212d"),
]
sys.stdout.reconfigure(encoding="utf-8", newline="\n")
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
failures = []

def fail(msg):
    failures.append(msg)
    print("FAIL: " + msg)

def lines_of(h):
    data = subprocess.run(["git", "cat-file", "-p", h], capture_output=True, check=True).stdout
    if b"\r" in data:
        fail("carriage return in blob " + h)
    text = data.decode("utf-8")
    out = text.split("\n")
    if out and out[-1] == "":
        out.pop()
    return out

def hunks_of(a, b):
    out = subprocess.run(["git", "diff", "-U0", "--no-color", "--no-ext-diff", a, b],
                         capture_output=True, check=True).stdout.decode("utf-8")
    res = []
    for ln in out.split("\n"):
        m = HUNK.match(ln)
        if m:
            os_, oc, ns, nc = m.groups()
            res.append((int(os_), 1 if oc is None else int(oc), int(ns), 1 if nc is None else int(nc),
                        ln.split(" @@")[0] + " @@"))
    return res

def walk(old_n, new_n, hunks):
    """Yield ('keep', old, new) / ('del', old, hunk_index) / ('add', new, hunk_index), 1-based."""
    oi, ni = 1, 1
    for k, (os_, oc, ns, nc, _hdr) in enumerate(hunks, 1):
        keep_to = os_ if oc == 0 else os_ - 1
        while oi <= keep_to:
            yield ("keep", oi, ni); oi += 1; ni += 1
        if nc and ni != ns:
            fail("line alignment at hunk %d: new %d, expected %d" % (k, ni, ns))
        for _ in range(oc):
            yield ("del", oi, k); oi += 1
        for _ in range(nc):
            yield ("add", ni, k); ni += 1
    while oi <= old_n:
        yield ("keep", oi, ni); oi += 1; ni += 1
    if ni - 1 != new_n:
        fail("line count after walk: %d, blob has %d" % (ni - 1, new_n))

texts = [lines_of(h) for _, h in CHAIN]

# --- 1. the chain: each session's hunks, and each line's session of origin ---
origin = [("derivation", i, None) for i in range(1, len(texts[0]) + 1)]
removed_by = {}          # derivation line -> (session, hunk index, header)
step_hunks = {}
print("== 1. THE CHAIN, each step diffed against the one before (git diff -U0) ==")
for s in range(1, len(CHAIN)):
    label = CHAIN[s][0]
    hs = hunks_of(CHAIN[s - 1][1], CHAIN[s][1])
    step_hunks[label] = hs
    print("%s: %s -> %s, %d hunks" % (label, CHAIN[s - 1][1][:8], CHAIN[s][1][:8], len(hs)))
    for k, h in enumerate(hs, 1):
        print("   %s hunk %d: %s" % (label, k, h[4]))
    new = []
    for kind, a, b in walk(len(texts[s - 1]), len(texts[s]), hs):
        if kind == "keep":
            if texts[s - 1][a - 1] != texts[s][b - 1]:
                fail("%s: kept line differs, old %d new %d" % (label, a, b))
            new.append(origin[a - 1])
        elif kind == "del":
            o = origin[a - 1]
            if o[0] == "derivation":
                removed_by[o[1]] = (label, b, hs[b - 1][4])
        else:
            new.append((label, b, a))   # (session, its hunk index, line number in its own blob)
    origin = new

final = texts[-1]
counts = {}
for o in origin:
    counts[o[0]] = counts.get(o[0], 0) + 1
print("\nSuccessor lines by session of origin: " + ", ".join("%s %d" % kv for kv in counts.items()))
print("Derivation lines removed, by session: " + ", ".join(
    "%s %d" % (lab, sum(1 for v in removed_by.values() if v[0] == lab)) for lab, _ in CHAIN[1:]))

# --- 2. the full diff, derivation -> successor, each passage traced through the chain ---
full = hunks_of(CHAIN[0][1], CHAIN[-1][1])
print("\n== 2. THE FULL DIFF, %s -> %s: %d hunks ==" % (CHAIN[0][1][:8], CHAIN[-1][1][:8], len(full)))
pairing = []
in_full_add = set()
in_full_del = set()
for kind, a, b in walk(len(texts[0]), len(final), full):
    if kind == "add":
        in_full_add.add(a)
    elif kind == "del":
        in_full_del.add(a)
for n in range(1, len(final) + 1):
    o = origin[n - 1]
    if n in in_full_add and o[0] == "derivation":
        pairing.append(("full diff marks added, chain says derivation line %d" % o[1], n, final[n - 1]))
    if n not in in_full_add and o[0] != "derivation":
        pairing.append(("full diff marks unchanged, chain says %s hunk %d" % (o[0], o[1]), n, final[n - 1]))
surviving = {o[1] for o in origin if o[0] == "derivation"}
for d in sorted(in_full_del):
    if d in surviving:
        pairing.append(("full diff marks derivation line %d removed, chain keeps it" % d, None, texts[0][d - 1]))
for d in sorted(set(removed_by) - in_full_del):
    pairing.append(("chain removes derivation line %d, full diff keeps it" % d, None, texts[0][d - 1]))

for k, (os_, oc, ns, nc, hdr) in enumerate(full, 1):
    print("\nFULL HUNK %d  %s" % (k, hdr))
    if nc:
        groups = []
        for n in range(ns, ns + nc):
            o = origin[n - 1]
            key = (o[0], o[1]) if o[0] != "derivation" else ("derivation", None)
            if groups and groups[-1][0] == key:
                groups[-1][2] = n
            else:
                groups.append([key, n, n])
        for (lab, hk), lo, hi in groups:
            if lab == "derivation":
                print("   successor lines %d-%d: carried from the derivation (a pairing difference)" % (lo, hi))
            else:
                print("   successor lines %d-%d: %s hunk %d %s" % (lo, hi, lab, hk, step_hunks[lab][hk - 1][4]))
    if oc:
        groups = []
        for d in range(os_, os_ + oc):
            key = removed_by.get(d, ("kept by the chain", 0, ""))
            if groups and groups[-1][0] == key:
                groups[-1][2] = d
            else:
                groups.append([key, d, d])
        for (lab, hk, hh), lo, hi in groups:
            if hk == 0:
                print("   derivation lines %d-%d removed: kept by the chain (a pairing difference)" % (lo, hi))
            else:
                print("   derivation lines %d-%d removed: %s hunk %d %s" % (lo, hi, lab, hk, hh))

print("\n== 3. PAIRING DIFFERENCES between the full diff and the chain: %d ==" % len(pairing))
worded = 0
for why, n, t in pairing:
    flag = "" if t.strip() in ("", "---") else "   <-- HAS WORDS"
    if flag:
        worded += 1
    print("   %s; successor line %s: %r%s" % (why, n, t[:80], flag))
if worded:
    fail("%d pairing differences carry words" % worded)

# --- 4. checks over the successor against the derivation ---
print("\n== 4. CHECKS OVER THE SUCCESSOR ==")
def stmt_heads(t):
    return [i for i, l in enumerate(t) if re.match(r"^\*\*L3-S\d+\. ", l)]
def num(l):
    return int(re.match(r"^\*\*L3-S(\d+)\. ", l).group(1))
for name, t in (("derivation", texts[0]), ("successor", final)):
    ns_ = sorted(num(t[i]) for i in stmt_heads(t))
    oq = sorted(int(m.group(1)) for l in t for m in [re.match(r"^- \*\*OQ-L3-(\d+)\b", l)] if m)
    print("%s: statements %d, L3-S1..42 once each: %s; open questions %d, OQ-L3-1..14 once each: %s"
          % (name, len(ns_), ns_ == list(range(1, 43)), len(oq), oq == list(range(1, 15))))
    if ns_ != list(range(1, 43)) or oq != list(range(1, 15)):
        fail(name + ": statement or open-question numbering")

def blocks(t):
    heads = stmt_heads(t)
    res = {}
    for i in heads:
        j = i + 1
        while j < len(t) and not re.match(r"^\*\*L3-S\d+\. ", t[j]) and not t[j].startswith("#"):
            j += 1
        head_end = i
        while head_end + 1 < j and not t[head_end + 1].startswith("- "):
            head_end += 1
        para = " ".join(t[i:head_end + 1])
        res[num(t[i])] = (t[i:j], " | ".join(re.findall(r"\*\*(.+?)\*\*", para)))
    return res
bd, bs = blocks(texts[0]), blocks(final)
changed = [n for n in range(1, 43) if bd[n][0] != bs[n][0]]
bold = [n for n in range(1, 43) if bd[n][1] != bs[n][1]]
print("statements whose block differs from the derivation's (%d): %s" % (len(changed), ", ".join("L3-S%d" % n for n in changed)))
print("statements byte-identical to the derivation's (%d): %s" % (42 - len(changed), ", ".join("L3-S%d" % n for n in range(1, 43) if n not in changed)))
print("statements whose bold text differs (%d): %s" % (len(bold), ", ".join("L3-S%d" % n for n in bold)))

sec4 = next(i for i, l in enumerate(final) if l.startswith("## 4."))
sec4_end = next(i for i in range(sec4 + 1, len(final)) if final[i].startswith("## "))
answered, cur = [], None
for l in final[sec4:sec4_end]:
    m = re.match(r"^- \*\*OQ-L3-(\d+)\b", l)
    if m:
        cur = int(m.group(1))
    if "**ANSWERED (" in l and cur is not None and cur not in answered:
        answered.append(cur)
print("ANSWERED marks in section 4 under: " + ", ".join("OQ-L3-%d" % n for n in answered))
banner = [l for l in final[:20] if "stand with their ANSWERED marks where a ruling answered them (" in l]
print("banner lines carrying the ANSWERED parenthesis: %d" % len(banner))
for l in banner:
    m = re.search(r"answered them \(([^)]*)\)", l)
    print("   banner parenthesis: " + (m.group(1) if m else "NOT FOUND"))
heads_ = [l for l in final if l.startswith("#")]
print("successor: %d lines, longest %d characters, %d heading lines" % (len(final), max(len(l) for l in final), len(heads_)))

print("\nRESULT: " + ("TRACE OK" if not failures else "STOP, %d failures" % len(failures)))
sys.exit(1 if failures else 0)
```

**Run it** from the repository root, its output redirected to the scratchpad (`CLAUDE.md`'s bash rule 2):
`python -I "<your scratchpad>/l3_session8_trace.py" > "<your scratchpad>/l3_session8_trace_out.txt"; echo "exit:$?"`.
Then `git hash-object --no-filters "<your scratchpad>/l3_session8_trace_out.txt"; echo "exit:$?"`, and read the output
with the Read tool (about 16 KB, 352 lines).

**Expected results** (the writing side's run on 2026-11-22, git 2.43.0, over the same seven blobs). The output's blob
was `f3854866ec1e434028bd805d9ca8d7235fcb28a8`; if yours is the same, every line below holds and you need not compare
them one by one. If it differs, compare the lines below and report each difference; a difference is a STOP only where
this list says so.
- Exit code 0 and the last line `RESULT: TRACE OK`. **Exit 1 or any line beginning `FAIL:` is a STOP-and-report.**
- Section 1, the changed passages of each session's own diff: **session 2: 41; session 3: 28; session 4: 2; session 5:
  2; session 6: 4; session 7: 2.** Sessions 2, 3 and 7 state their count in their reports (41 git hunks; 28; two);
  sessions 4, 5 and 6 list their hunks in their tables. **A session whose count here differs from its report's is a
  STOP-and-report.**
- Successor lines by session of origin: session 2: 222; session 3: 253; session 4: 355; session 5: 40; session 6: 61;
  session 7: 6; carried from the derivation: 1,193 (2,130 in all). Derivation lines removed: session 2: 287; session 3:
  20; session 7: 1; the others 0.
- Section 2: **the full diff has 63 changed passages** (`FULL HUNK 1` to `FULL HUNK 63`). (Entry 1190 counted 92 with
  a different diff method, Python's `difflib`; git groups the same changes into fewer passages. 63 is the figure for
  this check.)
- Section 3: **12 pairing differences, every one a blank line or `---`, none marked `HAS WORDS`.** These are places
  where the full diff and the chain of six diffs pair an identical blank line or `---` differently; no text differs.
  They are expected. One marked `HAS WORDS` makes the script fail (above).
- Section 4: L3-S1 to L3-S42 and OQ-L3-1 to OQ-L3-14 each present once, in the derivation and in the successor; 36
  statements whose block differs from the derivation's and 6 byte-identical (**L3-S1, L3-S3, L3-S4, L3-S18, L3-S21,
  L3-S29**); **5 statements whose bold text differs: L3-S7, L3-S16, L3-S17, L3-S24, L3-S28**; ANSWERED marks under
  OQ-L3-2, 3, 4, 5, 6, 7, 8 and 10, and one banner line whose parenthesis names the same eight; the successor 2,130
  lines, longest 1,205 characters, 42 heading lines.

## 4. The orders of the big dispatch this session replaces — the complete list

Nothing outside this list is replaced. Every replaced order keeps its text in the big dispatch, which is not edited.

1. **The reading order (line 98)** → §2 above, for this session.
2. **Task 1 (e)'s method.** *"Diff the successor against the derivation object: `git diff --no-index <scratch copy of
   the object> cowork_derived_specification_l3_2026_11_08.md`"* → `git diff -U0` between the two blobs
   `c01793f98c51e0267fb0dc7487613ac477cc1fbb` and `b4397e720b52f0f8afb23dbc47e675303cdc212d`, run inside the script,
   which compares the same two contents (sessions 2 to 7 declared the same change of method). The full diff's
   changed passages are the script's `FULL HUNK` entries.
3. **Task 1 (e)'s list of attributions gains one entry, and two lines of the sessions' tables are read under (b).**
   - **Added:** *"session 3's instruction, §3 item 6 (a staleness fix shown, added by that file)"*. Session 3's
     instruction added one correction of its own, under the user's rule of 2026-09-22, that no §L entry orders: in the
     successor's §4 closing sentence (*"Questions for the user, counted from the ★ marks: 5 of 14"*), it added that all
     five are now ANSWERED, with its `(was: …)` mark. Task 1 (e)'s list, written before the work was split into
     sessions, has no entry for it; without this entry it would be an unattributed passage. *Authored by the writing
     side; overrulable by the user.*
   - **Read under (b):** where a session's table attributes the banner's ANSWERED set to *"session N's instruction,
     §3 item 4"*, attribute it to **(b)**, whose banner writes *"the set the file carries"*.
   - **No longer present:** the in-progress line beneath the banner, written by session 2 and changed by sessions 3 to 6,
     was removed by session 7. If the script shows any successor line traced to it, STOP and report.
4. **Task 1 (d), one commit for the whole of Task 1** → **no commit of the successor in this session.** The successor
   was committed stretch by stretch by sessions 2 to 7, each under its own instruction's §3 item 5. This session commits
   only its report (§5 act 3).
5. **Task 1 (e)'s *"A changed passage none of those accounts for is a STOP-and-report and the file is not committed
   until it is removed"*** → the file is already committed, so: **do not edit the successor.** Mark such a passage
   **UNATTRIBUTED** in the table, with its lines and the session the script traces it to, finish the table, write and
   commit the report, and name every UNATTRIBUTED passage in your closing message. Removing it is a later act of the
   writing side's with the user. *Authored by the writing side; overrulable by the user.*
6. **The report Task 1 (e) and E1 name** (*"a table in the report"*; *"the diff table in the report"*), which is the
   batch's report of Task 5, `records/cc/reports/cc_report_l3_application_2026_11_08.md` → **this session's own report,
   `records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md`**, as sessions 2 to 7 each wrote
   theirs. Task 5's report, when its session writes it, points at this one. *Authored by the writing side, on the shape
   the six session reports set; overrulable by the user.*
7. **Where the batch ends for this session.** After §5's acts, this session STOPS. It does not begin Task 2 or any later
   Task.

## 5. The acts, in order

1. **Land the writing side's two files first, in a commit of their own.** Exactly two paths, both expected UNTRACKED:
   this file, `records/cc/instructions/cc_instruction_l3_application_session_8_task_1_check_2026_11_22.md`, and
   `records/cowork/handoff/cowork_handoff_entry_one_thousand_one_hundred_and_ninety.md`. Run §1 check 2 again
   immediately before staging. Subject exactly:
   `record: handoff entry 1190 and the session 8 instruction of the L3 application landed; the full Task 1 check follows`
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip.
2. **The check.** Write, prove and run the script (§3). Then build the diff table, one row per `FULL HUNK`, in the
   script's order:
   - **Columns:** the full hunk's number and git header; the derivation lines and successor lines it covers; the site
     (statement and field, open question, section, or banner), in the words the session table uses; the attribution;
     and the session or sessions and their own hunk numbers the script names.
   - **The attribution** is the one the named session's table gives for the named hunk of that session's own diff,
     written in Task 1 (e)'s terms: a §L entry and its amendment number (or its *Successor* part, where the session's
     table names it so); (a)'s replacement of §5 to §7 by the heading and paragraph; (a)'s two added sections (the
     section of added statements and the *Notes* section); (b)'s title and banner (with §4 item 3's reading); (c) item
     1's change, by statement and field, for L3-S25, L3-S16, L3-S9 and L3-S42; or §4 item 3's added entry. Where a full
     hunk draws on several sessions' hunks, give each, in the order of the successor's lines. Where a session table
     splits one of its hunks into several sites, use the site the full hunk's lines fall in; read the successor at the
     git object in that line range if the table does not settle it.
   - **Lines the script marks as a pairing difference** (`carried from the derivation`, or `kept by the chain`) are
     written *"pairing difference: blank line (or `---`), no text"* and need no attribution.
   - **To match a session's hunk to its table row:** each table gives its hunks by line numbers (session 2 by
     derivation lines; the others by lines of their own new version or by git header). The script prints every
     session hunk's git header in its section 1, so match by those numbers. **A session hunk that matches no row of its
     session's table is a STOP-and-report.**
   - **The other results of Task 1 (e) and E1,** from the script's section 4 and the six reports: every statement and
     open question present once; the 6 byte-identical statements, and confirmation that none of them is the site of
     any row of the six diff tables (a table row whose site is one of them is a STOP-and-report; a mention outside the
     tables, such as a report's list of statements left untouched, is not); the 5 statements whose bold text differs, set against Task 1 (e)'s
     allowed list (L3-S7, L3-S24 and L3-S28 whole; L3-S17's second sentence; L3-S16's feature (6) closing clause), and
     for each the session row that changed it; the ANSWERED set against the banner; §0 to §4 carried whole except where
     the table attributes a change; §5 to §7 replaced (the full hunk at the end of the file, against session 2's rows).
3. **The report.** Write `records/cc/reports/cc_report_l3_application_session_8_task_1_check_2026_11_22.md` with the
   items of §6. Commit that ONE path alone, subject exactly:
   `report: session 8 of the L3 application, the full Task 1 check (Task 1 (e) and E1) written; Task 2 follows in a new session`.
   PUSH; verify at `.git/refs/remotes/origin/master` that it equals the new tip. Write no `STATUS.md` entry; that
   belongs to Task 5.

## 6. What the report states, and the same in your closing message to the user

1. §1's six results, the blobs, and the repeat of check 2 before staging.
2. The two commits by their full hashes, each verified at the object (`git show --stat <hash>; echo "exit:$?"`), and
   `origin/master` at the last.
3. The script: its hash check (§3), its exit code, its output's blob, and each of §3's expected results held or
   differing (with the difference).
4. **The diff table** of §5 act 2, every one of the 63 full hunks attributed, or marked UNATTRIBUTED under §4 item 5.
5. The other results of Task 1 (e) and E1, as §5 act 2's last bullet lists them, each held or not.
6. **E1, graded item by item:** the successor at the root; §0 to §4 carried whole and §5 to §7 replaced by the heading
   and paragraph; every amendment applied in its form, citing its record and ruling, **or listed as STOP-and-report —
   list here every STOP-and-report the six session reports give, with the session and its reason**; the ANSWERED set in
   the banner; the banner as (b); the diff table with every changed passage attributed; no recommendation anywhere.
7. Every departure from this file or the big dispatch, declared, including any order of reads you could not follow.
8. The last sentence, exactly: *"Session 8 of the L3 application ends here. Task 2 is not begun. Nothing else was done."*

## 7. What the earlier sessions established, for the record (relayed here; verified by the Cowork sittings at the objects)

Session 1 committed Task 0 as `cbde76fd78a244540df64895191a511df186cc29` and stopped at Task 0's guard-set check: two
tools failing beyond the thirteen of the declared start state, item 2 (`gen_evidence_pin_membership.py`, which counts
the ruling records on disk, and `gen_per_session_reading.py`, which finds handoff entries through git). Session 2 applied
§L.1 to §L.15 and held one amendment as STOP-and-report, §L.15 amendment 4, as that entry's own settled note orders.
Sessions 3 to 7 applied §L.16 to §L.55 with no STOP. The successor versions they committed, which the script reads, are
in its `CHAIN` list. **This session runs no guard**, so neither red bears on its acts; both are declared here so that no
later reader takes them for this session's doing.

## 8. Stop conditions, gathered in one place

STOP and report at once, and do nothing further, when:
- any check in §1 fails;
- `CLAUDE.md` is not in your context as a memory file (§2 item 4);
- the script's hash cannot be made to match (§3), or the script exits 1 or prints a `FAIL:` line;
- a session's hunk count from the script differs from its report's, or a session hunk matches no row of its table;
- a successor line traces to the in-progress line (§4 item 3), or a byte-identical statement is named as a site in a
  session table (§5 act 2);
- a push cannot be verified at `.git/refs/remotes/origin/master`;
- this file and the big dispatch seem to differ on something §4 does not list.

An UNATTRIBUTED passage is NOT a stop of the session: §4 item 5 says what to do. After a STOP, report what you did and
what you did not do. Do not try to repair anything.

*Provenance: Cowork, 2026-11-22 (Stockholm), the sitting booted on entry 1190. Read at the objects for this file: the
three git reference files; the big dispatch (blob computed from the staged bytes) at lines 6100–6571 and 7021–7135,
and the byte sizes of the ranges §2 item 9 names; the successor and the derivation (blobs computed from the staged
bytes, `b4397e72…` and `c01793f9…`) and their headings; the five intermediate successor blobs, from the staged loose
objects, each hashing to itself; session 7's instruction and report whole; the diff tables of sessions 2 and 3, and the
attribution column of all six reports; session 3's instruction at lines 140–179; entry 1190 (blob computed,
`a804d4cf…`). The script was run by the writing side, with the user's leave ("A"), in a throwaway git repository in its
own container holding exactly the seven blobs, with the results §3 gives. Not re-measured here, relayed from entry 1190
[checked there]: the commits of the successor chain and session 7's three commits at their trees. The user's words: the
opening instruction; "shortened"; "A" (the test of the script).*
