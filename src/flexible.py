# Flexible Spaces
# https://open.kattis.com/problems/flexible
# TAGS: basic, brute force
# CP4: 3.2g, Try All Answers
# NOTES:
W, P = map(int, input().split())

ls = map(int, input().split())

ls = [0] + list(ls) + [W]

res = set()

for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        res.add(ls[j] - ls[i])

print(*sorted(res))