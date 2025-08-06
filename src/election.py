# Election
# https://open.kattis.com/problems/election
# TAGS: mathematics, combinatorics, probability
# CP4: 5.4b, Binomial Coefficients
# NOTES:
"""
The probability/combinatorics is easy enough, just got WA a few times due to reading comprehension and ceil/+1 stuff:

you should print "RECOUNT!" if "your candidate has no chance of *WINNING*"

-> to win, your candidate needs STRICTLY > N/2 votes

So, if V2 has e.g. 5 out of 10 votes, even if you reached V1=5 votes YOU CANNOT *WIN* but only draw so the check is V2 >= ceil(N/2)
"""
from math import comb,ceil

T = int(input())
for _ in range(T):
    N, V1, V2, W = map(int, input().split())
    # V1 > N/2 rewrite to avoid floats:
    if 2 * V1 > N:
        # V1 > N/2 means already have won, 2nd option is winning with prob > W see later
        print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
    elif V2 >= ceil(N / 2): # CARE! it says if "your candidate has no chance of *WINNING*" so i believe this is correct interpretation: if V2 is already == N/2, then V1 cannot *WIN*,but can only draw
        print("RECOUNT!")
    else:
        remaining = N - V1 - V2
        needed = ceil((N + 1) / 2) - V1
        goods = sum(comb(remaining, k) for k in range(needed, remaining + 1))
        ALL = 2 ** remaining
        # goods/ALL must be strictly > W/100 to be champagne
        # -> rewrite 100*goods > W * ALL
        if 100 * goods > W * ALL:
            print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
        else:
            print("PATIENCE, EVERYONE!")