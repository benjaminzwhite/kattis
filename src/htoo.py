# H to O
# https://open.kattis.com/problems/htoo
# TAGS: interpreter, logic, improve
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
TODO: IMPROVE: DIY parser maybe can do with regex

Basically the logic after is easy; check which atom is the "rate limiting one" for the wanted molecule compared to how many you have etc
"""
from collections import defaultdict

have, amount = input().split()
amount = int(amount)
want = input()

def parser(s):
    d = defaultdict(int)
    i = 0
    while i < len(s):
        n = '0'
        atom = s[i]
        while i + 1 < len(s) and s[i + 1].isdigit():
            i += 1
            n += s[i] 
        if int(n) == 0:
            d[atom] += 1
        else:
            d[atom] += int(n)
        i += 1
    return d

d_have = parser(have)
d_want = parser(want)

res = float('inf')
for want_atom, want_qty in d_want.items():
    if want_atom not in d_have:
        res = 0
        break
    else:
        res = min(res, (d_have[want_atom] * amount) // want_qty)

print(res)