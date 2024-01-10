# Running Race
# https://open.kattis.com/problems/kaploeb
# TAGS: sorting
# CP4: 2.3f, Hash Table (map), H
# NOTES:
"""
Sorting criteria are:

- only the runners who complete all K laps are considered for the results
  hence the condition in res -> if len(v) == K

- also, the sort key is by total time, lowest to highest
  -> sum(d[x]) the values of their K laps
  
- however, tie breaker is lowest number/runner id, hence the 2-ple key:
  -> "key = lambda x: (sum(d[x]), int(x))"
"""
from collections import defaultdict

L,K,S = map(int, input().split())

d = defaultdict(list)

for _ in range(L):
    runner, time = input().split()
    mins, secs = map(int, time.split('.'))
    d[runner].append(60*mins + secs)

res = sorted((k for k, v in d.items() if len(v) == K), key = lambda x: (sum(d[x]), int(x)))

for x in res:
    print(x)