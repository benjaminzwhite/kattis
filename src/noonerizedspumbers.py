# Noonerized Spumbers
# https://open.kattis.com/problems/noonerizedspumbers
# TAGS: brute force
# CP4: 8.7h, Mathematics+Other
# NOTES:
"""
Code not very DRY because I was unclear what is and isn't allowed and got a few WA:

It says proper prefixes i.e cant have empty or full a, b, res being used but this doesnt seem to be implemented?
Also says "mathemtically correct" strings but I got errors when not handling leading 0 in resulting string
-> SYNTAX ERROR try/except is for cases where string leads with 0.
"""
a, op, b, _, res = input().split()

def solve():
    # 3 cases:
    for ia in range(len(a)):
        for ib in range(len(b)):
            # res unchanged:
            try:
                if eval(b[:ib]+a[ia:]+op+a[:ia]+b[ib:]) == int(res):
                    return f"{b[:ib]+a[ia:]} {op} {a[:ia]+b[ib:]} = {res}"
            except SyntaxError:
                continue

    for ia in range(len(a)):
        for ires in range(len(res)):
            # b unchanged
            try:
                if eval(res[:ires]+a[ia:]+op+b) == int(a[:ia]+res[ires:]):
                    return f"{res[:ires]+a[ia:]} {op} {b} = {a[:ia]+res[ires:]}"
            except SyntaxError:
                continue

    for ib in range(len(b)):
        for ires in range(len(res)):
            # a unchanged:
            try:
                if eval(a+op+res[:ires]+b[ib:]) == int(b[:ib]+res[ires:]):
                    return f"{a} {op} {res[:ires]+b[ib:]} = {b[:ib]+res[ires:]}"
            except SyntaxError:
                continue

print(solve())