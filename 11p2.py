#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [[int(x) for x in line.strip()] for line in sys.stdin]

N = len(field)
M = len(field[0])

def is_inside(x, y):
    return 0 <= x < N and 0 <= y < M

def adj(i, j):
    for dx in [-1, 0, +1]:
        for dy in [-1, 0, +1]:
            if is_inside(i+dx, j+dy) and (dx, dy) != (0, 0):
                yield (i+dx, j+dy)

step = 0
while True:
    step += 1
    
    for i in range(N):
        for j in range(M):
            field[i][j] += 1

    visited = set()

    def visit(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))
        
        for (x, y) in adj(i, j):
            field[x][y] += 1
            if field[x][y] >= 10:
                visit(x, y)
    
    for i in range(N):
        for j in range(M):
            if field[i][j] >= 10:
                visit(i, j)

    for (i, j) in visited:
        field[i][j] = 0
                
    if len(visited) == N * M:
        print(step)
        break
