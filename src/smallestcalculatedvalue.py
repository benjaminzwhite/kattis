# Smallest Calculated Value
# https://open.kattis.com/problems/smallestcalculatedvalue
# TAGS: interpreter, mathematics
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
It's not 100% clear from description but I think that you aren't allowed to do:
7 3 3 -> 7/3*3 = 7
since the intermediate step 7/3 is noninteger (no such example shown, but I get WA if I don't implement this requirement)

---

In the last if statement of code below:

You don't need the tmp2 % 1 == 0 check anymore it is a leftover from when I was doing / during the a,b,c operations
and checking at the end - but that fails on a test case like 7 3 3 since intermediate value of 7/3 was formed
even though you end up with an integer
"""
from itertools import product
from operator import add, sub, truediv, mul

OPS = [add, sub, truediv, mul]

a, b, c = map(int, input().split())

best = float('inf')
for op1, op2 in product(OPS, repeat=2):
    if op1 == truediv and a % b != 0:
        continue
    tmp1 = op1(a, b)
    if op2 == truediv and tmp1 % c != 0:
        continue
    tmp2 = op2(tmp1, c)
    if tmp2 % 1 == 0 and tmp2 >= 0:
        best = min(best, tmp2)

print(int(best))