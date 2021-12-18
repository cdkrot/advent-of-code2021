#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys


def incrLeft(obj, val):
    if type(obj) == int:
        return obj + val
    (L, R) = obj

    return (incrLeft(L, val), R)


def incrRight(obj, val):
    if type(obj) == int:
        return obj + val
    (L, R) = obj

    return (L, incrRight(R, val))


def explode(obj, depth):
    if type(obj) == int:
        return (obj, 0, 0, False)
    else:
        L, R = obj

        if depth >= 5 and type(L) == int and type(R) == int:
            return (0, L, R, True)
        
        (Lprime, ex1, ex2, flg) = explode(L, depth + 1)

        if ex2 != 0:
            R = incrLeft(R, ex2)
            ex2 = 0

        if flg:
            return ((Lprime, R), ex1, ex2, flg)

        # ex1 == 0 and ex2 == 0
        (Rprime, ex3, ex4, flg) = explode(R, depth + 1)
        if ex3 != 0:
            Lprime = incrRight(Lprime, ex3)
            ex3 = 0

        return ((Lprime, Rprime), ex3, ex4, flg)


def split(obj):
    if type(obj) == int:
        if obj >= 10:
            return ((obj // 2, (obj + 1) // 2), True)
        return (obj, False)
    else:
        (L, R) = obj
        
        (Lprime, flg) = split(L)
        if flg:
            return ((Lprime, R), flg)

        (Rprime, flg) = split(R)
        return ((Lprime, Rprime), flg)


def magnitude(obj):
    if type(obj) == int:
        return obj
    else:
        (L, R) = obj
        return 3 * magnitude(L) + 2 * magnitude(R)


def reduce_number(inp):
    while True:
        (inpprime, _, _, flg) = explode(inp, 1)

        if flg:
            inp = inpprime
            continue

        (inpprime, flg) = split(inp)
        if flg:
            inp = inpprime
        else:
            break
    return inp


numbers = [eval(line.strip()) for line in sys.stdin]
ANS = -1
for num1 in numbers:
    for num2 in numbers:
        if num1 != num2:
            ANS = max(ANS, magnitude(reduce_number((num1, num2))))
print(ANS)
