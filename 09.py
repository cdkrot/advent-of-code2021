#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [line.strip() for line in sys.stdin]

N = len(field)
M = len(field[0])

total = 0
for i in range(N):
    for j in range(M):
        is_localmin = True
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < N and 0 <= y < M and field[i][j] >= field[x][y]:
                is_localmin = False

        if is_localmin:
            total += int(field[i][j]) + 1
print(total)
