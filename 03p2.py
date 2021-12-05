#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin]

output = []

for rev in [False, True]:
    cur = list(lines)

    for bit in range(len(lines[0])):
        if len(set(cur)) == 1:
            break
        
        cnt = [0,0]

        for L in cur:
            cnt[ord(L[bit]) - ord('0')] += 1

        select = int(rev ^ (0 if cnt[1] < cnt[0] else 1))
        cur = [line for line in cur if ord(line[bit]) - ord('0') == select]

    output.append(cur[0])

print(output)

print(int(output[0], base=2) * int(output[1], base=2))
