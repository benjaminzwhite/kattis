# Election
# https://open.kattis.com/problems/election2
# TAGS: dict
# CP4: 2.3e, Hash Table (map), E
# NOTES:
n = int(input())

candidates = {}

# update: don't know why I didn't do for _ in range(n) O_o
while n:
    n -= 1
    name = input()
    party = input()
    candidates[name] = party

cnt = {c:0 for c in candidates.keys()}

m = int(input())

for _ in range(m):
    x = input()
    if x in candidates:
        cnt[x] += 1

max_votes = max(v for v in cnt.values())

winners = [c for c in candidates if cnt[c] == max_votes]
if len(winners) == 1:
    print(candidates[winners[0]])
else:
    print("tie")