#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [[int(x) for x in line.strip()] for line in sys.stdin]

N = len(field)
M = len(field[0])

def is_inside(x, y):
    return 0 <= x < N and 0 <= y < M

def adj(i, j):
    for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if is_inside(x, y):
            yield (x, y)

dist = [[int(1e9) for i in range(M)] for _ in range(N)]
used = [[False for i in range(M)] for _ in range(N)]
dist[0][0] = 0

while True:
    best = None

    for i in range(N):
        for j in range(M):
            if not used[i][j] and (not best or dist[i][j] < dist[best[0]][best[1]]):
                best = (i, j)

    if not best:
        break
    used[best[0]][best[1]] = 1
    
    for (x, y) in adj(best[0], best[1]):
        if dist[x][y] > dist[best[0]][best[1]] + field[x][y]:
            dist[x][y] = dist[best[0]][best[1]] + field[x][y]

print(dist[-1][-1])
