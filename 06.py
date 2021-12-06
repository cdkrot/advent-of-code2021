#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

init = list(map(int, input().split(',')))

state = [init.count(x) for x in range(9)]

for i in range(int(input())):
    newstate = [0 for _ in range(9)]

    for i in range(1, 9):
        newstate[i - 1] += state[i]
    newstate[6] += state[0]
    newstate[8] += state[0]
    state = newstate

print(sum(state))
