# Binary Choosing
# https://open.kattis.com/problems/binarychoosing
# TAGS: mathematics, probability, binary
# CP4: 0, Not In List Yet
# NOTES:
"""
The (num_coins > 0) at the final res part is because, for input c=1 i.e. 1 person, the formula ceil(log2(c)) gives that 
you will flip 0  coins. If you calculate the expectation with my approach, it will give expectation 0.5.

I noticed this while trying the values of c in the test range (10**9 worked fine, so I tried lowest given c==1 value and tried to
reason to myself whether 1 person does or does not flip a coin O_o ? I guess it makes sense that answer is no, so 0 coin flips)

Also, see comments in code below for why we iterate over the binary representation of c-1 rather than c.
"""
from math import log2, ceil

c = int(input())

num_coins = ceil(log2(c)) # CARE! tried to be clever using len of bin(c) but doesn't work; have to do exactly as formula asks in text

expected_coin_flips = num_coins * c / 2 ** num_coins

b = bin(c - 1)[2:]
# condition on all possible locations of the first 1 that is > 0 in the binary representation of c-1
# (since this is the "end round early signal")
# if it occurs at pos x, i.e. on the x'th coin flip then it will:
# - occur will probability 1/2**pos
# - contribute therefore an additional expectation of pos * prob = pos / 2**pos
# CARE! you do this on the string for c-1, not c, since the VALIDS are 0,1,2,...c-1 but NOT c ITSELF.
for pos, d in enumerate(b, 1):
    if d == '0':
        expected_coin_flips += pos / 2 ** pos

expected_num_rounds = 2 ** num_coins / c 

res = (num_coins > 0) * expected_coin_flips * expected_num_rounds

print(res)