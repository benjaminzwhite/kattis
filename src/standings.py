# Biased Standings
# https://open.kattis.com/problems/standings
# TAGS: sorting, greedy
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
Old exercise so a bit overranked - just greedy sorting
"""
T = int(input())

for _ in range(T):
    input()
    N = int(input())
    
    xs = []
    for _ in range(N):
        _, x = input().split()
        xs.append(int(x))
    
    res = sum(abs(a - b) for a, b in zip(sorted(xs), range(1, N + 1)))
    
    print(res)