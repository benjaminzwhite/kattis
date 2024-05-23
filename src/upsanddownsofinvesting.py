# The Ups and Downs of Investing
# https://open.kattis.com/problems/upsanddownsofinvesting
# TAGS: array, logic
# CP4: 2.2b, 1D Array, Harder
# NOTES:
"""
NOTES: reading comprehension - very weird input format, you have to take MULTILINE inputs, and keep checking whether
you have reached the required number, s, of elements. Even more confusing because there are no example testcases that
illustrate this.

Important comment compared to other similar exercises:
here it explicity says that no 2 consecutive numbers are the same, so no PLATEAU handling needed e.g. 1,2,3,3,3,2,1
---

TODO: IMPROVE: there are some similar exercises to this, my solutions are always linear but I wonder
if can improve the implementation/clarity.

https://open.kattis.com/problems/highesthill
https://open.kattis.com/problems/inverteddeck
"""
s, n, m = map(int, input().split())

xs = []
while len(xs) != s:
    tmp = list(map(int, input().split()))
    xs.extend(tmp)

climbing, falling = False, False

climb_len, fall_len = 0,0 

peaks, valleys = 0, 0

# no 2 consec are the same so no plateaus
for left, right in zip(xs, xs[1:]):
    if right > left:
        if climbing:
            climb_len += 1
        else:
            # have we just seen at least n-1 consec rises followed by n-1 consec falls
            if climb_len >= n - 1 and fall_len >= n - 1:
                peaks += 1
            # reset climb_len to 0, then add 1 since we just climbed
            climb_len = 1
            climbing = True
            falling = False
    else:
        if falling:
            fall_len += 1
        else:
            if fall_len >= m - 1 and climb_len >= m - 1:
                valleys += 1
            fall_len = 1
            falling = True
            climbing = False

# can't think of clever way to append something to xs to trigger end of array processing
# so need final check: we may have 1 more peak or valley left unhandled
if climb_len >= n - 1 and fall_len >= n - 1 and falling:
    peaks += 1
if climb_len >= m - 1 and fall_len >= m - 1 and climbing:
    valleys += 1

print(peaks, valleys)