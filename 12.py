#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys, collections

gr = collections.defaultdict(list)

for line in sys.stdin:
    s, t = line.strip().split('-')
    gr[s].append(t)
    gr[t].append(s)

cnt_paths = 0
cur = set()

def go(v):
    global cnt_paths
    if v in cur:
        return

    if v == 'end':
        cnt_paths += 1
        return

    if ord('a') <= ord(v[0]) <= ord('z'):
        cur.add(v)
        
    for u in gr[v]:
        go(u)
    
    if v in cur:
        cur.remove(v)

go('start')
print(cnt_paths)

