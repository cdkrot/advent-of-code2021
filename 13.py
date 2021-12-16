#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

pts = set()
for line in sys.stdin:
    line = line.strip()
    if line == '':
        break

    x, y = map(int, line.split(','))
    pts.add((x, y))

for line in sys.stdin:
    toks = line.strip().split()
    assert toks[0] == 'fold'

    tp, coord = toks[2].split('=')
    coord = int(coord)
    
    newpts = set()
    for (x, y) in pts:
        if tp == 'x' and x > coord:
            x = (2 * coord) - x
        if tp == 'y' and y > coord:
            y = (2 * coord) - y
        newpts.add((x, y))
    
    pts = newpts

print(len(pts))
for row in range(30):
    print(''.join('*' if (col, row) in pts else ' ' for col in range(50)))
