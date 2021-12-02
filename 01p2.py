#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

seq = [int(line) for line in sys.stdin]

sums = [x + y + z for (x,y,z) in zip(seq, seq[1:], seq[2:])]

total_increases = 0
for (old, new) in zip(sums, sums[1:]):
    if old < new:
        total_increases += 1

print(total_increases)
