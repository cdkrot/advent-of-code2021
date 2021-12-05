#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [[0 for i in range(1000)] for j in range(1000)]

for line in sys.stdin:
    A, B, C = line.split()
    x1, y1 = map(int, A.split(','))
    x2, y2 = map(int, C.split(','))

    if x1 == x2 or y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            for y in range(min(y1,y2), max(y1,y2)+1):
                field[x][y] += 1

cnt = 0
for row in field:
    for elem in row:
        if elem >= 2:
            cnt += 1
print(cnt)
print([row[:10] for row in field[:10]])
