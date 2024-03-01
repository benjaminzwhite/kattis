# Early Winter
# https://open.kattis.com/problems/earlywinter
# TAGS: basic, array
# CP4: 1.4e, Control Flow
# NOTES:
"""
It wants next index for which x <= dm (dm is the input target value).

Can use next() instead of the Flag below.
"""
_, dm = map(int, input().split())

xs = map(int, input().split())

F = 0
for i, x in enumerate(xs):
    if x <= dm:
        res = i
        F = 1
        break

if F == 0:
    print("It had never snowed this early!")
else:
    print(f"It hadn't snowed this early in {res} years!")