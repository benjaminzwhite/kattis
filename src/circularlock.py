# Circular Lock
# https://open.kattis.com/problems/circularlock
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
"""
Not really sure what to think about this, basically after all the reading it tells you the equivalent requirement:
that you can deactivate if you can deactivate a "equivalent lock" with
single P = gcd(p11, p12, p21, p22) and modified s' = s % P for all 4 values of s

---

So I just thought about how you can deactivate such a lock:

First thought was that you need both vals in row1 and row2 to be == or same for col e.g.

P = 100 (whatever) and e.g. 
          26 26   <--- press this row 74 times to reach 100
          91 91   <--- press this row  9 times to reach 100

Then I realised you actually need that the difference between the values should be the same %P (slight generalisation of above thought process)

e.g. you can have something like

P = 15 (whatever):
          2  7 <--- press this row 8 times, so that it becomes 10 15, then can press first column 5 times so that you get 15,15,15,15 res
         10 15

---

Implementation notes:

gcd on multiple integers doesn't work in Kattis Python 3.8 environment, only on
two integers gcd(a,b), so need to manually implement it with reduce
"""
from math import gcd
from functools import reduce

T = int(input())

for _ in range(T):
    s11, s12, p11, p12 = map(int, input().split())
    s21, s22, p21, p22 = map(int, input().split())

    P = reduce(gcd, [p11, p12, p21, p22])
    if ((s12 - s11) % P == (s22 - s21) % P) or ((s21 - s11) % P == (s22 - s12) % P):
        print("Yes")
    else:
        print("No")