#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

ans = 0
for line in sys.stdin:
    _, right = line.split('|')

    for tok in right.split():
        if len(tok) in [2,4,3,7]:
            ans += 1

print(ans)
