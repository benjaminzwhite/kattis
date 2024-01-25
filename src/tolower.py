# ToLower
# https://open.kattis.com/problems/tolower
# TAGS: string
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
Bit of reading comprehension:
Basically, for each group of T words, "Are all of their [1:] letters in lowercase (i.e. ignore first letter) ?"
"""
P, T = map(int, input().split())

res = 0
for _ in range(P):
    ok = True
    for _ in range(T):
        s = input()
        if not all(x.islower() for x in s[1:]):
            ok = Falses
    if ok:
        res += 1

print(res)