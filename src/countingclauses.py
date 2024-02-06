# Counting Clauses
# https://open.kattis.com/problems/countingclauses
# TAGS: basic
# CP4: 8.6c, NP-hard/C, special, E
# NOTES:
"""
Kind of a troll question/reading comprehension:
Just need to count if there are >= 8 clauses or not
"""
clauses, n = map(int, input().split())

# don't need this, just in case there is end of file/exit program bugs or something O_o
for _ in range(clauses):
	input()

if clauses >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")