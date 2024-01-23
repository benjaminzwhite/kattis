# Triple Texting
# https://open.kattis.com/problems/tripletexting
# TAGS: array
# CP4: 1.6m, Input Parsing (Iter)
# NOTES:
s = input()

L = len(s) // 3

res = ''.join(sorted(triple)[1] for triple in zip(s[:L], s[L:2*L], s[2*L:]))

print(res)