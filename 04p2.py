#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

seq = list(map(int, input().split(',')))
where = {seq[i] : i for i in range(len(seq))}

boards = []

while True:
    try:
        input()
    except:
        break

    brd = []
    for i in range(5):
        brd.append(list(map(int, input().split())))
    boards.append(brd)

def call_moment(board):
    board_trans = [[where.get(key, int(1e9)) for key in row] for row in board]
    board_trans_t = [[board_trans[j][i] for j in range(5)] for i in range(5)]

    res = int(1e9)
    for i in range(5):
        res = min(res, max(board_trans[i]))
        res = min(res, max(board_trans_t[i]))

    return res
    
best_i = 0
for (i, board) in enumerate(boards):
    if call_moment(boards[best_i]) < call_moment(board):
        best_i = i

board = boards[best_i]
moment = call_moment(board)

board_trans = [[where.get(key, int(1e9)) for key in row] for row in board]

total = 0
for i in range(5):
    for j in range(5):
        if board_trans[i][j] > moment:
            total += board[i][j]
print(total * seq[moment])
