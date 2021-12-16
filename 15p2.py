#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys, heapq

field_ = [[int(x) for x in line.strip()] for line in sys.stdin]
field = []

def shift(row):
    return [(1 if x == 9 else x + 1) for x in row]

for t in range(5):
    for row in field_:
        for _ in range(t):
            row = shift(row)
        newrow = row
        
        for _ in range(4):
            row = shift(row)
            newrow += row

        field.append(newrow)

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

heap = [(0, 0, 0)]

while heap:
    (val, besti, bestj) = heapq.heappop(heap)
    if dist[besti][bestj] != val:
        continue
    
    used[besti][bestj] = 1
    
    for (x, y) in adj(besti, bestj):
        if dist[x][y] > dist[besti][bestj] + field[x][y]:
            dist[x][y] = dist[besti][bestj] + field[x][y]
            heapq.heappush(heap, (dist[x][y], x, y))

print(dist[-1][-1])
