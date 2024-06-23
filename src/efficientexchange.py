# Efficient Exchange
# https://open.kattis.com/problems/efficientexchange
# TAGS: greedy, mathematics, logic, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice exercise.

Basically you are trying to "set all digits to 0", if you think about it, by either "removing" or "adding" coins.

For digits < 5 you always want to set locally to 0 by removing d coins e.g. 324 involves -4, -2, -3 of each 1,10,100 unit

For digits > 5 you want to "set THIS digit to 0" by increasing to *10* which has the added effect of carrying and extra 1 onto next unit

This creates the edge case for d=5, whether you set to '0' or '10' since both involve changing 5 coins ("minus 5" or "plus 5")
i.e. do you CARRY or NOT CARRY the 1 in this specific case ?

This is determined by whether the "next" digit itself is >= 5 or not. WHY? because if next digit is itself >= 5 then carrying makes sense
as it will REDUCE the number of coins needed for the next unit (e.g. if next digit is 6, then on its own res will be += (10 - 6) since 6 >=5,
however if you can carry +1 to 6 to make 7 you REDUCE res += (10 - 7) i.e. you use FEWER COINS IN TOTAL)

You can use e.g. the testcase 12345678987654321, to see this behavior - you will get answer 43 instead of 42 until you account for this.

---

Implementation notes:

Work from least significant to most significant digit.
I implement DIY "pairwise" compare "small" and "big" digits using zip trick as usual 

CARE! WITH THIS IMPLEMENTATION NEED TO PAD WITH 2 EXTRA 0's SINCE
a) need to handle last TRUE digit, and 
b) need to handle case where LAST TRUE DIGIT CARRIES
(this was failing me during debugging on testcase 83 since e.g. if only pad to [3,8,0] instead of [3,8,0,0]
then last pair will be 8,0 and WILL NOT GET THE +=1 due to carry of the 8 since the optimum move is 8 -> 10)
"""
s = input()

it = list(map(int, s))[::-1] + [0, 0] # work from lsd to msd, dummy 0 0 at end to handle zip/pairwise SEE IMPLEMENTATION NOTES ABOVE

res = 0

carry = False 
for small, big in zip(it, it[1:]):
    curr = small + carry # int + bool Python type magic O_o
    if curr > 5:
        # always carry 1
        carry = True
        res += 10 - curr
    else:
        # maybe carry 1, if it leads to reduction of total number of coins due to NEXT COIN (here called 'big' coin) becoming 6 or more (since this leads to e.g. 10-6 instead of 10-5 etc)
        carry = (curr == 5 and big >= 5)
        res += curr

print(res)