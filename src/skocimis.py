# Skocimis
# https://open.kattis.com/problems/skocimis
# TAGS: logic
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
Nice little puzzle; optimal move is to leave as many spaces available for next turn, by jumping directly adjacent
to one of the other 2 kangaroos every turn.

e.g. with testcase 3 5 9

There are 5-3 - 1 = 1 spaces between 3 and 5
There are 9-5 - 1 = 3 spaces between 5 and 9

If 3 jumps to 7, he leaves only 1 space (either 6 or 8) for subsequent plays

However if 3 jumps to 6 or 8 (i.e. adjacent to 5 or 9), he leaves 2 spaces for subsequent plays, and then we
recursively solve from this new game configuration (i.e. 5 6 9 or 5 8 9) having added +1 to total number of moves.
"""
A, B, C = map(int, input().split())

res = max(C-B, B-A) - 1

print(res)