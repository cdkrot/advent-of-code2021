#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

lst = list(map(int, input().split(',')))
s = sum(lst)

mincost = int(1e100)

for position in range(0, 1500):
    deltas = (abs(position - crab) for crab in lst)
    cost = sum(delta * (delta + 1) // 2 for delta in deltas)
    mincost = min(mincost, cost)
print(mincost)
