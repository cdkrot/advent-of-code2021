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
was_extra = False

def go(v):
    global cnt_paths, was_extra
    undo_extra = False

    if v == 'end':
        cnt_paths += 1
        return
    
    if v in cur:
        if v != 'start' and not was_extra:
            was_extra = True
            undo_extra = True
        else:
            return

    if ord('a') <= ord(v[0]) <= ord('z'):
        cur.add(v)
        
    for u in gr[v]:
        go(u)

    if undo_extra:
        was_extra = False
    elif v in cur:
        cur.remove(v)
        

go('start')
print(cnt_paths)

