# Gene Block
# https://open.kattis.com/problems/geneblock
# TAGS: logic
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
There are many ways to solve this. For example:

- check the pattern of removing 7 from all numbers ending in 1,2,3....
- you find the cycle of length up to 10 for numbers ending in 0

You obtain e.g.

       last_digit_of_number = 7 4 1 8 5 2 9 6 3 0
hm_7s_to_remove_to_end_in_7 = 0 1 2 3 4 5 6 7 8 9
                                    ^
                                    |
                                    |
i.e. If the last digit of your number is ___8, then you need to remove 3x 7 to get a number ending in 7.

CARE! With this approach, you need to check an additional condition:
- check that you have "enough" 7's to remove from the given input 

e.g. 32 -> ends in 2, so need to remove 5x 7s.
Final res is the total number of blocks, so involves the 1 "big" leftover block ending with 7
So: res = 1 + 5 = 6, so need at least 6 blocks, but since 6*7 > 32, you can't do this even if all the blocks are of minimal size (7).

By contrast, say input was 100032, then you'd remove 5x 7s to get 100032 - 5*7 = 99997, which is the 6th block ending with 7, so this works.
"""
for _ in range(int(input())):
    x = input()

    indexes = "7418529630"

    d = indexes.find(x[-1])
    res = 1 + d

    if int(x) >= res * 7:
        print(res)
    else:
        print(-1)