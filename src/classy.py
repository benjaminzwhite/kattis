# A Classy Problem
# https://open.kattis.com/problems/classy
# TAGS: sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
"""
Hard to understand/reading comprehension problem mainly.

AFAICT this part:

"When comparing classes, once you have reached the lowest level of detail, you should assume
that all further classes are the same as the middle level of the previous level of detail. 
So upper class and middle-upper class are equivalent, as are middle-middle-lower-middle and lower-middle."

means that [since there are at most 10 subclasses in inputs] the "default" is mid-mid-mid-mid-mid-mid-mid-mid-mid-mid
in the absence of any subdivision info, so you just "ZFILL" with "mid" all the sort keys up to length 10

---

CARE! ALSO, NOT VERY CLEAR, BUT THIS STUFF IS ACTUALLY BEING "READ" RIGHT TO LEFT
-> so lower-upper class means MAIN: upper, SUBDIVISION_1: lower NOT VICE VERSA

THIS IS REALLY ANNOYING BECAUSE THE TESTCASE WORKS WITH *BOTH* INTERPRETATIONS (really bad testcase design)

---

Implementation note:

instead of FILL with "mid" -> I encode UPPER/MID/LOWER as 3,2,1 (arbitrary) and FILL WITH 2 (corresponding to mid above)
"""
d = {"upper": '3', "middle": '2', "lower": '1'}

T = int(input())
for _ in range(T):
    res = []

    n = int(input())
    for _ in range(n):
        who, vals, _ = input().split()
        sortkey = ''.join(d[v] for v in vals.split('-')[::-1]).ljust(10, '2')
        res.append((who[:-1], int(sortkey))) # [:-1] because there is a : at end of string of each name

    res = sorted(res, key=lambda x: (-x[1], x[0])) # highest sortkey, tiebreak on alphabetical

    for who, _ in res:
        print(who)

    print('=' * 30)