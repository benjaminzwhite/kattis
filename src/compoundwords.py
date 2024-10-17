# Compound Words
# https://open.kattis.com/problems/compoundwords
# TAGS: set
# CP4: 2.3g, Balanced BST (set)
# NOTES:
import sys

seen = set()
words = []

for l in sys.stdin:
    words.extend(l.split())
    
for w1 in words:
    for w2 in words:
        if w1 != w2:
            seen.add(w1 + w2)
            
for word in sorted(seen):
    print(word)