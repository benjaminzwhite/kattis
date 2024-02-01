# Hay Points
# https://open.kattis.com/problems/haypoints
# TAGS: basic
# CP4: 2.3e, Hash Table (map), E
# NOTES:
m, n = map(int, input().split())
d = {}

for _ in range(m):
    w, amount = input().split()
    d[w] = int(amount)

for _ in range(n):
    total = 0
    while (sentence := input()) != '.':
        for word in sentence.split():
            total += d.get(word, 0)
    print(total)