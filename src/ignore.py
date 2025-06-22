# Ignore the Garbage
# https://open.kattis.com/problems/ignore
# TAGS: mathematics
# CP4: 5.2d, Base Number Variants
# NOTES:
"""
NOTES: right-way up, the numbers are generated in order 
                    1
                    2
                    3
                    4
                    5
                    6
                    ... etc.

If you filter out the ones which contain digits that are not flippable: 3,4,7
you are therefore looking at (rightside up) numbers which use the digits 0,1,2,5,6,8,9 in "normal order"
i.e. this subset of numbers will be generated as 1,2,5,6,8,9,10,11,12,15... where I've deleted the BADS with digits 3,4,7.

What the UPSIDEDOWN person will see therefore is: these "NUMBERS" in this order, but upside down.

Below, I'm doing a walkthrough without simplification to keep a record of the reasoning.
"""
import sys

LOOKUP = [0, 1, 2, 5, 6, 8, 9]

for l in sys.stdin:
    n = int(l)

    # generate the n'th *RIGHTSIDE UP* number that only uses the digits: 0,1,2,5,6,8,9
    tmp = []
    while n:
        n, r = divmod(n, 7) # <- 7 is the len(0,1,2,5,6,8,9)
        tmp.append(LOOKUP[r])

    # CARE! we appended to tmp "backwards" from LSD to MSD, relative to what the value actually is, so RIGHTSIDE UP IS tmp[::-1]
    rightside_up = tmp[::-1]

    # now turn this upside down -> this is what the person sees, in order:
    # to turn upside down, you:
    # a) read rightside_up from right to left AND
    # b) convert each digit to its upsidedown paired value e.g. 0->0, 1->1, 2->2, 5->5, 6->9, 8->8, 9->6
    res = []
    PAIRS = {0: 0, 1: 1, 2: 2, 5: 5, 6: 9, 8: 8, 9: 6}
    for d in rightside_up[::-1]:
        res.append(PAIRS[d])

    print(''.join(map(str, res)))