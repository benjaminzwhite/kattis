# Left and Right
# https://open.kattis.com/problems/leftandright
# TAGS: logic, nice
# CP4: 9.cons, Construction
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/leftandright.md
"""
n = int(input())
s = input()
s += 'R' # IMPLEMENTATION: dummy R will trigger the last ("real") range processing, then stop.

res = []
smallest_avail, curr_descent_size = 1, 0
for c in s:
    if c == 'L':
        curr_descent_size += 1
    else:
        tmp = list(range(smallest_avail + curr_descent_size, smallest_avail - 1, -1)) # CARE! note range is REVERSED: i.e. want [4,3,2] not [2,3,4]
        res.extend(tmp) 
        smallest_avail += curr_descent_size + 1
        curr_descent_size = 0

for x in res:
    print(x)