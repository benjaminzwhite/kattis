# Grid Magic
# https://open.kattis.com/problems/gridmagic
# TAGS: mathematics, brute force, precompute
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
Since n, m are <= 8 you can precompute all n*m possible answers.

I left an (unoptimised) precomputation code below, you can adjust the n, m values
manually to fill out the 2d RES[][] array locally.

---

Precomputation notes:

For larger values of n,m > 4ish you get very slow computation for the itertools product, so don't know if there is a smart on-the-fly computation
BUT you notice as you fill in the RES grid that e.g. n,m=1,6 leads to RES = 0, SO YOU CAN CONCLUDE THAT n,m=1,7 and 8 also have = 0
(because if you can't satisfy the property for 6 primes you can't satisfty for 7 or 8 either)
So basically you fill in the RES grid until you reach a 0 value, then all others in that row are 0 also
NOTE ALSO that RES[n][m] == RES[m][n] so can avoid recomputing a few values

A few more observations:
-> 1 digit_primes are 2,3,5,7
-> then only need to append characters from 1,3,5,7,9 since appending even number will never lead to a 2,3,4..digit prime 
(since will end in even number at some point)

---

Precomputation code:

# Do these calculations for n,m in range(1,8+1)
# Note that as mentioned above once you get RES=0 you don't need to test higher value of m in that row/col etc.
n, m = 2, 2 # <-- adjust when running locally

from itertools import product

def is_prime(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return n > 1

digit_primes = {d:set() for d in range(1, 8 + 1)}
digit_primes[1] = set({'2','3','5','7'})

for d in range(2, 8 + 1):
    for prefix in digit_primes[d - 1]:
        for next_digit in '13579':
            p = int(prefix + next_digit)
            if is_prime(p):
                digit_primes[d].add(str(p))

p = product(digit_primes[n], repeat=m)
cnt = 0
for it in p:
    if all(''.join(col) in digit_primes[m] for col in zip(*it)):
        cnt += 1

print(cnt)
"""

# Obtained RES[][] array from running the above precomputation steps
RES = [[0,0,0,0,0,0,0,0,0],
[0,4,4,3,3,2,0,0,0],
[0,4,9,5,0,0,0,0,0],
[0,3,5,16,0,0,0,0,0],
[0,3,0,0,0,0,0,0,0],
[0,2,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

n, m = map(int, input().split())

print(RES[n][m])