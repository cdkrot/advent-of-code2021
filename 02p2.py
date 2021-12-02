#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

depth = 0
horizontal = 0
aim = 0

for line in sys.stdin:
    direction, l = line.split()
    l = int(l)
    
    if direction == 'forward':
        horizontal += l
        depth += l * aim
    elif direction == 'up':
        aim -= l
    else:
        aim += l
print(depth, horizontal)
