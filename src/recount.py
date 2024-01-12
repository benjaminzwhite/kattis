# Recount
# https://open.kattis.com/problems/recount
# TAGS: counter
# CP4: 2.3e, Hash Table (map), E
# NOTES:
from collections import Counter

c = Counter()

while True:
    s = input()
    if s == "***":
        break
    c.update( {s} ) # CARE! Python syntax: update with {s} since want the string, s, itself in the set (not its letters)
    
res = []
max_v = 0
for k,v in c.items():
    if v > max_v:
        max_v = v
        res = [k]
    elif v == max_v:
        res.append(k)
        
if len(res) == 1:
    print(res[0])
else:
    print("Runoff!")