# Keywords
# https://open.kattis.com/problems/keywords
# TAGS: basic, string
# CP4: 2.3d, Hash Table (set)
# NOTES:
n = int(input())

S = set()

for _ in range(n):
    x = input()
    y = x.replace('-', ' ').lower()
    S.add(y)

print(len(S))