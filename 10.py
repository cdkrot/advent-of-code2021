#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys

penalty = {')': 3, ']': 57, '}': 1197, '>': 25137}

types = {'(': +1,
         '[': +2,
         '{': +3,
         '<': +4,
         ')': -1,
         ']': -2,
         '}': -3,
         '>': -4}

total = 0
for line in sys.stdin:
    line = line.strip()

    st = []
    
    for ch in line:
        if types[ch] > 0:
            st.append(ch)
        elif len(st) == 0 or types[st[-1]] + types[ch] != 0:
            total += penalty[ch]
            break
        else:
            st.pop()
print(total)
        
