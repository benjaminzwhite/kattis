# Alchemy 101
# https://open.kattis.com/problems/alchemy101
# TAGS: binary, brute force, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE:

Solved experimentally, not sure I understand the period 4 behavior yet (corresponds to last 2 digits being 00,01,10,11)

Experimental investigation below

---

Code used:

from functools import reduce

for n in range(25+1):
    print("{0:>3} {1:>3} {2:>3}".format(n, r:=reduce(lambda acc,x: acc^x, range(1, n+1), 0), n - r))

---

Observe a repeating pattern of period 4: e.g from 0 -> 15:

  A: n itself
      B: reduce XOR on 1->n inclusive
          C: A - B
  A   B   C
 -----------
  0   0   0
  1   1   0 # !!!!!!!!!! UPDATE !!!!!!!!!! case n==1 breaks the pattern you don't "skip n-1" as you would for all other n%4==1 cases
  2   3  -1
  3   0   3
  4   4   0 <--- period 4
  5   1   4   *|***
  6   7  -1    |  *  
  7   0   7    |  *  period 4
  8   8   0 <--   *
  9   1   8   *****  
 10  11  -1
 11   0  11
 12  12   0
 13   1  12
 14  15  -1
 15   0  15

So cases:
- n%4 == 0: B is already == n so can reduce entire range 1->n
- n%4 == 1: C is n-1 so need to XOR again with n-1 (which is equivalent to XOR'ing twice with n-1, i.e. XOR'ing 0 times) -> range 1->n but SKIP n-1
- n%4 == 2: C is -1 so need to XOR again with 1 (which is equivalent to XOR'ing twice with 1, i.e. XOR'ing 0 times) -> range 1->n but SKIP 1
- n%4 == 3: C is 0 so need to XOR again with n (which is equivalent to XOR'ing twice with n, i.e. XOR'ing 0 times) -> range 1->n but SKIP n
"""
def range_with_skip(n):
    if n % 4 == 0:
        print(n) # dont skip any value in the range 1->n
        skip_val = None
    elif n % 4 == 1:
        print(n-1)
        skip_val = n - 1
    elif n % 4 == 2:
        print(n - 1)
        skip_val = 1
    else:
        print(n - 1)
        skip_val = n
    print(*filter(lambda x: x != skip_val, range(1, n + 1)))

T = int(input())

for _ in range(T):
    m = int(input())
    if m == 1:
        print(1) # update - m==1 is an exceptional case where you don't skip m-1 even though m%4==1 (noticed this with sample testcase)
        print(1)
    else:
        range_with_skip(m)