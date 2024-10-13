# Grandpa Bernie
# https://open.kattis.com/problems/grandpabernie
# TAGS: dict
# CP4: 2.3e, Hash Table (map), E
# NOTES:
"""
0 based indexing but 1-based queries
e.g. asks for 1st trip but this will be 0th index in the sorted list of years he visited that country
"""
from collections import defaultdict

d = defaultdict(list)

n = int(input())

for _ in range(n):
    country, year = input().split()
    year = int(year)
    d[country].append(year)
    
for k, v in d.items():
    d[k] = sorted(v) # CARE! SORT THE YEARS SINCE THEY ARE NOT SORTED IN THE INPUT
    
q = int(input())

for _ in range(q):
    country, trip = input().split()
    i = int(trip) - 1 # 0 based indexing
    print(d[country][i])