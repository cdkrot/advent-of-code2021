#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

field = [[ch for ch in s.strip()] for s in sys.stdin]

steps = 0
while True:
    steps += 1
    last_move = (-1, -1)

    for line in field:
        print(''.join(line))
    print('')
    
    for i in range(len(field)):
        wasBusy = (field[i][0] != '.')

        for j in range(len(field[i])):
            if field[i][j] != '>' or last_move == (i, j - 1):
                continue
                
            if j == len(field[i]) - 1:
                if not wasBusy:
                    field[i][0] = field[i][j]
                    field[i][j] = '.'
                    last_move = (i, j)
            else:
                if field[i][j + 1] == '.':
                    field[i][j + 1] = field[i][j]
                    field[i][j] = '.'
                    last_move = (i, j)

    for j in range(len(field[0])):
        wasBusy = (field[0][j] != '.')

        for i in range(len(field)):
            if field[i][j] != 'v' or last_move == (i - 1, j):
                continue
                
            if i == len(field) - 1:
                if not wasBusy:
                    field[0][j] = field[i][j]
                    field[i][j] = '.'
                    last_move = (i, j)
            else:
                if field[i + 1][j] == '.':
                    field[i + 1][j] = field[i][j]
                    field[i][j] = '.'
                    last_move = (i, j)

    if last_move == (-1, -1):
        break

print(steps)
