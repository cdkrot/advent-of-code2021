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

pairs = defaultdict(int)
for (let, let2) in zip(polymer, polymer[1:]):
    pairs[(let, let2)] += 1

for t in range(40):
    newpairs = defaultdict(int)

    for (pair, quant) in pairs.items():
        let, let2 = pair

        let1 = rules[let + let2]
        
        newpairs[(let, let1)] += quant
        newpairs[(let1, let2)] += quant
    
    pairs = newpairs

freq = defaultdict(int)
for pair, quant in pairs.items():
    let, let2 = pair
    
    freq[let] += quant
    freq[let2] += quant

freq[polymer[0]] += 1
freq[polymer[-1]] += 1

print((max(freq.values()) - min(freq.values())) // 2)
