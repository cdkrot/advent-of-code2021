#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys, itertools

target_x1, target_x2, target_y1, target_y2 = map(int, input().split())

def hit(X, Y):
    posx, posy = 0,0
    bestY = posy
    
    while True:
        bestY = max(bestY, posy)
        
        if target_x2 < posx or posy < target_y1:
            return -1
        if target_x1 <= posx <= target_x2 and target_y1 <= posy <= target_y2:
            return bestY
        
        posx += X
        posy += Y
        
        if X:
            X -= 1
        Y -= 1

best = -1
cnt = 0
for X, Y in itertools.product(range(1, 1000), range(-1000, 1000)):
    t = hit(X, Y)
    best = max(best, t)

    if t != -1:
        cnt += 1
        
print(best, cnt)
