# Zipf's Law
# https://open.kattis.com/problems/zipfslaw
# TAGS: sorting, dict
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
It's trivial just tedious parsing input - all the annoying stuff, like: unknown number of lines, testcases,
you have to print weird strings, have to ignore case in the input etc.

The "algorithm" is literally just a Counter.

NOTE: I used groupby isalpha() since it says "word is anything separated by nonletters" so I presume there is some
testcase where the inputs are like jahfh$afaf*afhf and you can't just split on spaces etc.
"""
from itertools import groupby
from collections import defaultdict

is_first_case = True
while True:
    try:
        n = int(input())

        if not is_first_case:
            print()
        is_first_case = False

        d = defaultdict(int)
        curr_case = True
        while curr_case:
            for k, v in groupby(map(str.lower, input()), key=str.isalpha):
                if k:
                    s = tuple(v)
                    if s == ('e', 'n', 'd', 'o', 'f', 't', 'e', 'x', 't'):
                        res = sorted(w for w, cnt in d.items() if cnt == n)
                        if not res:
                            print("There is no such word.")
                        else:
                            for w in res:
                                print(''.join(w))
                        curr_case = False
                        break
                    else:
                        d[s] += 1
    except:
        break