#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys
from collections import defaultdict

freq = defaultdict(int)
length = None

for line in sys.stdin:
    length = len(line.strip())
    for (i, c) in enumerate(line.strip()):
        freq[(i, c)] += 1

s     = ''.join(('1' if freq[(i, '1')] > freq[(i, '0')] else '0') for i in range(length))
s_inv = ''.join(('0' if freq[(i, '1')] > freq[(i, '0')] else '1') for i in range(length))

print(int(s, base=2) * int(s_inv, base=2))
