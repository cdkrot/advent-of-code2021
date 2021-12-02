#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

increases = 0
last = int(1e9)
for line in sys.stdin:
    n = int(line)

    if n > last:
        increases += 1

    last = n

print(increases)
