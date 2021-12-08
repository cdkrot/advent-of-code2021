#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

def intersect(a, b):
    s = set(a).intersection(b)
    return ''.join(sorted(s))

def is_subset(a, b):
    return intersect(a, b) == a

def find(pred, s):
    for x in s:
        if pred(x):
            return x
    raise ValueError()

total = 0
for line in sys.stdin:
    left, right = line.split('|')

    toks = list(map(lambda tok: ''.join(sorted(tok)), left.split()))
    right = list(map(lambda tok: ''.join(sorted(tok)), right.split()))

    dct = {}
    
    dct[1] = find(lambda x: len(x) == 2, toks)
    dct[4] = find(lambda x: len(x) == 4, toks)
    dct[7] = find(lambda x: len(x) == 3, toks)
    dct[8] = find(lambda x: len(x) == 7, toks)

    dct[6] = find(lambda x: len(x) == 6 and len(intersect(dct[1], x)) == 1, toks)
    dct[9] = find(lambda x: len(x) == 6 and is_subset(dct[4], x), toks)
    dct[0] = find(lambda x: len(x) == 6 and x != dct[6] and x != dct[9], toks)

    dct[3] = find(lambda x: len(x) == 5 and is_subset(dct[7], x), toks)
    dct[5] = find(lambda x: len(x) == 5 and is_subset(x, dct[6]), toks)
    dct[2] = find(lambda x: len(x) == 5 and x != dct[3] and x != dct[5], toks)

    revdct = {value : key for (key, value) in dct.items()}
    
    decoded = ''.join(str(revdct[tok]) for tok in right)
    print(decoded)
    total += int(decoded)
print("Total: ", total)
