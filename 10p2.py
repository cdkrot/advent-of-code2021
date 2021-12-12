#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

penalty = {'(': 1, '[': 2, '{': 3, '<': 4}

types = {'(': +1,
         '[': +2,
         '{': +3,
         '<': +4,
         ')': -1,
         ']': -2,
         '}': -3,
         '>': -4}

penalties = []
for line in sys.stdin:
    line = line.strip()

    st = []
    failed = False
    for ch in line:
        if types[ch] > 0:
            st.append(ch)
        elif len(st) == 0 or types[st[-1]] + types[ch] != 0:
            failed = True
            break
        else:
            st.pop()

    if not failed:
        score = 0
        for tok in reversed(st):
            score = 5 * score + penalty[tok]
        penalties.append(score)

penalties.sort()
print(penalties)
print(len(penalties))
print(penalties[len(penalties) // 2])
        
