# Odd Man Out
# https://open.kattis.com/problems/oddmanout
# TAGS: basic, array
# CP4: 2.3d, Hash Table (set)
# NOTES:
"""
An approach that avoids maintaining Counter:
- each time you see an item for the 1st time, add it to seen
- each time you see an item for a 2nd time, remove it from seen
- at the end, the only item in seen is the one that has been seen only once
"""
N = int(input())

for case_num in range(1, N+1):
    G = int(input())
    
    seen = set()
    for x in input().split():
        if x in seen:
            seen.discard(x)
        else:
            seen.add(x)
    
    res = seen.pop()
    
    print(f"Case #{case_num}: {res}")