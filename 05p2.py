#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [[0 for i in range(1000)] for j in range(1000)]

for line in sys.stdin:
    A, B, C = line.split()
    x1, y1 = map(int, A.split(','))
    x2, y2 = map(int, C.split(','))

    dx = 0
    dy = 0

    if x1 < x2:
        dx = +1
    elif x1 > x2:
        dx = -1
        
    if y1 < y2:
        dy = +1
    elif y1 > y2:
        dy = -1

    px = x1
    py = y1
    while (px, py) != (x2, y2):
        field[px][py] += 1
        px += dx
        py += dy

    field[x2][y2] += 1                

cnt = 0
for row in field:
    for elem in row:
        if elem >= 2:
            cnt += 1
print(cnt)
