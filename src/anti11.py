# Ocean's Anti-11
# https://open.kattis.com/problems/anti11
# TAGS: mathematics, combinatorics, recurrence, proof
# CP4: 5.4a, Fibonacci Numbers
# NOTES:
"""
While generating the GOODS list for N_MAX = 100 I noticed the Fibonacci pattern.
Kept logic below for reference.

Count bads by conditioning on the location of the first 11 in the string:
 
g g g 0 1 1 _ _ _ _ _ 
        ^
        |_____i=4 in this example is index of first 11

Any bad string with first bad index i is made up of:
- A good string of len i-1 (not i, because THERE MUST BE A 0 BEFORE THE GIVEN 11, otherwise it would not be the first 11 in the string)
- A 0 (because THERE MUST BE A 0 BEFORE THE GIVEN 11) ^^^ see above
- A 11
- A remaining binary string which can be anything, of len n-i-2 -> there are 2**(n-i-2) of them

N_MAX = 100
GOODS = [1, 2] # there are 1 GOOD strings of len 0 and 2 GOOD strings of len 1

for n in range(2, N_MAX+1):
    bads = 0
    
    # handle case i=0 separately since avoids GOODS[i-1] failure
    # i.e. for i=0 we start with 11_____ : so there are n-2 remaining symbols which can be anything thus 2**(n-2) bad strings of this form
    bads += 2**(n - 2)
    
    for i in range(1, (n - 2) + 1): # loop to i_max = n-2 INCLUSIVE (corresponds to first occurence of 11 in the bad string being at the end ____11)
        bads += GOODS[i - 1] * (2**(n - 2 - i))
    
    goods = 2**n - bads
    
    GOODS.append(goods)
"""
N_MAX = 10_000
BIGMOD = 10**9 + 7

# -- Precompute Fibonacci numbers --
res = [1]
a, b = 1, 2 # CARE! watch out for +/-1 index errors and start of sequence convention
for _ in range(N_MAX + 1):
    a, b = b, a + b
    res.append(a % BIGMOD)

# -- Queries --
T = int(input())

for _ in range(T):
    n = int(input())
    print(res[n])