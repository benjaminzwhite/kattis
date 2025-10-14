# Bannorð
# https://open.kattis.com/problems/bannord
# TAGS: basic, string
# CP4: 1.5d, Input Parsing (Iter)
# NOTES:
bads = set(input())

s = input()

res = []
for word in s.split():
    if any(c in bads for c in word):
        res.append(len(word) * '*')
    else:
        res.append(word)

print(' '.join(res))