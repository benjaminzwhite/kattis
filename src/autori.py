# Autori
# https://open.kattis.com/problems/autori
# TAGS: basic
# CP4: 1.6m, Input Parsing (Iter)
# NOTES:
s = input()

res = ''.join(w[0] for w in s.split('-'))

print(res)