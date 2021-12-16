#!/usr/bin/python3
# Dmitry [cdkrot.me] Sayutin (2021)

import sys
from collections import defaultdict

polymer = input().strip()
input()

rules = dict()
for line in sys.stdin:
    st, arrow, to = line.strip().split()

    rules[st] = to

for t in range(10):
    letters = [polymer[0]]
    for i in range(1, len(polymer)):
        letters.append(rules[polymer[i - 1] + polymer[i]])
        letters.append(polymer[i])
    
    polymer = ''.join(letters)

freq = defaultdict(int)
for let in polymer:
    freq[let] += 1

print(max(freq.values()) - min(freq.values()))
