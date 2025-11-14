# Manhattan Mornings
# https://open.kattis.com/problems/manhattanmornings
# TAGS: longest increasing subsequence
# CP4: 3.5c, LIS
# NOTES:
"""
It's a longest increasing subsequence application.

CARE! start is not always "below and left" of end point.
This doesn't really add anything, but it just forces you to e.g. reverse x and/or y so transform into
"standard configuration" where your Manhattan paths have increasing x and increasing y coordinates:
You can do this by flipping x axis if start_x > end_x and same same for y.

Note also that there are some particular requirements that mean your implementation has to handle
tiebreakers (so use bisect_right etc.) - I left comments below.
"""
N = int(input())

start_x, start_y, end_x, end_y = map(int, input().split())

# See notes above: the inputs don't always have start pos "below left" from end pos O_o
# so we "transform axes" a bit to align with a standard configuration
rev_x, rev_y = False, False

if start_x > end_x:
    rev_x = True
    start_x = -start_x
    end_x = -end_x
if start_y > end_y:
    rev_y = True
    start_y = -start_y
    end_y = -end_y

xs = []
for _ in range(N):
    x, y = map(int, input().split())
    if rev_x:
        x = -x
    if rev_y:
        y = -y
    if (start_x <= x <= end_x) and (start_y <= y <= end_y):
        xs.append((x, y))

# sort on ascending x, then will do LIS on the resulting y coordinates
ys = sorted(xs, key=lambda x: (x[0], x[1]))

# actual LIS code
# CARE! bisect_right not bisect_left since it is allowed to extend "LIS" with EQUAL elements e.g. 1,1,3,3,3,7,8 valid
from bisect import bisect_right

last_val_of_LIS_of_len = [float('inf')] * N

# CARE! I had this as default max_len = 1
# but in this exercise ALL POINTS CAN LIE OUTSIDE "PATH"/start-to-end boundary SO IN PRINCIPLE MAX_LIS_LENGTH = 0
max_LIS_len = 0
for (_, y) in ys:
    insert_pos = bisect_right(last_val_of_LIS_of_len, y)
    last_val_of_LIS_of_len[insert_pos] = y
    if insert_pos + 1 > max_LIS_len:
        max_LIS_len = insert_pos + 1

print(max_LIS_len)