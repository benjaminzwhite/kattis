# Election Paradox
# https://open.kattis.com/problems/electionparadox
# TAGS: sorting
# CP4: 1.4e, Control Flow
# NOTES:
"""
See logic in code below.

CARE! With N // 2 + 1 with the indexing inclusive/exclusive.
"""
N = int(input())

votes = sorted(map(int, input().split()))

res = 0

# take the N // 2 largest regions and win them all with ALL VOTES
res += sum(votes[N // 2 + 1:])

# take the N // 2 + 1 smallest regions and lose each one with v // 2
res += sum(v // 2 for v in votes[:N // 2 + 1])

print(res)