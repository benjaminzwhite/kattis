# Mirror Strings
# https://open.kattis.com/problems/mirrorstrings
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
The combinatorics is easy enough: for either of the symbol families, {H I O X l}, {x o}, choose the first m//2 symbols freely then
choose the mirror half in exactly 1 way.

Also note, have to handle odd even m slightly carefully: for odd m, the first (m-1)//2 chars chosen freely and paired with their mirror
but the middle one doesn't have to be paired - it can also be chosen in 5 (resp. 2) ways, depending on which family we are looking at.

The result for a given m is the sum of these 2 family of strings.

However, brute force approach will TLE so need to do a bit of geometric series as well: 

---

Below is the brute force "count them all" approach.
!!! The max range is 10**6 so this will TLE on the big cases; so see the geometric series approach in 2nd section after.

BIGMOD = 10**9 + 7

def cnt(m):
    if m%2 == 0:
        return pow(5,m//2,BIGMOD) + pow(2,m//2,BIGMOD)
    else:
        return 5*pow(5,m//2,BIGMOD) + 2*pow(2,m//2,BIGMOD)

res = 0
L,R = 2, 1000000

for m in range(L,R+1):
    res += cnt(m)

print(res % BIGMOD) # checked L,R = 2, 1000000 - gives 664868576 correct answer but 5.1 secs

---

Faster solution:
-> thinking about the sum of the geometric series of 2**k and 5**k:
Suppose sum all lengths m from 1 to R = 9:
 
   m = |     1         2        3        4          5       6         7         8        9       
m even |            5**2//2            5**4//2            5**6//2            5**8//2            
m odd  | 5*5**1//2          5*5**3//2           5*5**5//2          5*5**7//2          5*5**9//2

sum of first row is 5**1 + 5**2 ... 5**4 i.e. sum i=1 to i= (R)//2 of 5**i
sum of second row is 5**1 + 5**2 ... 5**5 i.e. sum i=1 to i = (R+1)//2 of 5**i

so contribution from both is (5**1 - 5**n+1) // (1 - 5) where n is respectively (R)//2 and (R+1)//2

N1, N2 = (R)//2, (R+1)//2
res_from_5 = (5**(N1+1) - 5) // 4 + (5**(N2+1) - 5) // 4 
res_from_2 = (2**(N1+1) - 2) + (2**(N2+1) - 2)        <--- same argument as ^^ just with 2 instead of 5 for the other family of symbols
res = res_from_5 + res_from_2
print(res % BIGMOD)

Note that this is assuming range from L=1 to R inclusive; if you have e.g. L = 472 then you need to REMOVE sum up to R' = 472-1 = 471 etc.
"""
def get_cnt_to_right_range(R):
    N1, N2 = R // 2, (R + 1) // 2

    res_from_5 = (5**(N1 + 1) - 5) // 4 + (5**(N2 + 1) - 5) // 4 
    res_from_2 = (2**(N1 + 1) - 2) + (2**(N2 + 1) - 2)

    return res_from_5 + res_from_2

BIGMOD = 10**9 + 7

L, R = map(int, input().split())

res = get_cnt_to_right_range(R) - get_cnt_to_right_range(L - 1) # NB L-1 so that we end up with L->R INCLUSIVE as our remaining result

print(res % BIGMOD)