# Floor Plan
# https://open.kattis.com/problems/floorplan
# TAGS: mathematics, number theory
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
If n = m**2 - k**2 then write n = (m+k)(m-k) = m**2 - k**2
-> So look for factorization of n into 2 factors c,d such that c+d = m+k + m-k = 2*m
-> Then divide by 2 to get a possible value of m, then remove m from c=m+k to get k
-> Check that m**2 - k**2 == original n and we are done

---

You can simplify the above reasoning to get a short formula (rewrite n = (m-k)*(m+k) as -> n = (f)*(f+2k) and do a parity analysis on this)
"""
n = int(input())

flg = False
for d in range(1, int(n**0.5) + 1):
    if n % d == 0:
        c = n // d
        mm = c + d
        m = mm // 2
        k = c - m
        if n == m**2 - k**2:
            print(m, k)
            flg = True
            break

if not flg:
    print("impossible")