#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

lst = list(map(int, input().split(',')))

lst.sort()

position = lst[len(lst) // 2]
cost = sum(abs(position - crab) for crab in lst)
print(cost)
