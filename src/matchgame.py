# Match Game
# https://open.kattis.com/problems/matchgame
# TAGS: logic, precompute
# CP4: 1.6d, Game (Others), Harder
# NOTES:
"""
Nice little exercise, should be self explanatory code below - only 2 possible real cases:

Either there is 1 digit that is not equal between start and end, or there are 2 digits that are not equal.

- if only 1 digit is !=, then check the start and end digit is obtainable by moving one match "internally" i.e. 2 -> 3 ok
- if 2 digits, check that: the 2 start digits turn into corresponding "digit with 1 match removed" and "digit with 1 match added"
"""
s, e = input().split()

MOVE_ONE = {'0':'69','2':'3','3':'25','5':'3','6':'09','9':'60'}
REMOVE_ONE = {'6':'5','7':'1','8':'069','9':'35'}
ADD_ONE = {'0':'8','1':'7','3':'9','5':'69','6':'8','9':'8'}

mismatches = []
for c1, c2 in zip(s, e):
    if c1 != c2:
        mismatches.append((c1, c2))

L = len(mismatches)
if L == 0 or L > 2:
    print("no")
else:
    if L == 1:
        c1, c2 = mismatches[0]
        if c2 in MOVE_ONE.get(c1, '') or c1 in MOVE_ONE.get(c2, ''):
            print("yes")
        else:
            print("no")
    else:
        c1, c2 = mismatches[0]
        c3, c4 = mismatches[1]
        if c2 in REMOVE_ONE.get(c1, '') and c4 in ADD_ONE.get(c3, ''):
            print("yes")
        elif c4 in REMOVE_ONE.get(c3, '') and c2 in ADD_ONE.get(c1, ''):
            print("yes")
        else:
            print("no")