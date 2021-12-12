#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [line.strip() for line in sys.stdin]

N = len(field)
M = len(field[0])

def is_inside(x, y):
    return 0 <= x < N and 0 <= y < M

def adj(i, j):
    for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if is_inside(x, y):
            yield (x, y)

def cnt_smaller_neigh(i, j):
    return len(list(filter(lambda p: field[i][j] >= field[p[0]][p[1]], adj(i, j))))

components = []
for i in range(N):
    for j in range(M):
        if not cnt_smaller_neigh(i, j):
            visited = set()
            que = []

            def consider(x, y):
                if (x, y) in visited or field[x][y] == '9':
                    return
                
                visited.add((x, y))
                que.append((x, y))

            consider(i, j)
                
            while que:
                (x, y) = que.pop()

                for (a, b) in adj(x, y):
                    if field[a][b] >= field[x][y]:
                        consider(a, b)

            components.append(len(visited))

print(components)
components.sort()
print(components[-1] * components[-2] * components[-3])
