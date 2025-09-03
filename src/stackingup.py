# Stacking Up
# https://open.kattis.com/problems/stackingup
# TAGS: array, logic, interpreter, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/stackingup.md
"""
n = int(input())

xs = list(map(int, input().split()))

ops = []
acc_plus_ops = 0 # how many times have we needed to perform + operation prior to this current x value
for x in xs[::-1]:
    x_ = x + acc_plus_ops
    curr_ops = []
    
    # do the "binary log/matrix power" type decomposition of x_:
    while x_ != 1:
        if x_ % 2 == 1:
            curr_ops.append("1+")
            acc_plus_ops += 1
            x_ -= 1
        else:
            curr_ops.append("d+")
            acc_plus_ops += 1
            x_ //= 2
    
    # now x_ == 1: so "end" the process with the '1'
    # (since we are working backwards this INITIALIZES the st process)
    curr_ops.append('1')
    
    ops.append(curr_ops[::-1]) # CARE! Remember to reverse the curr_ops!

# remember to REVERSE THE ORDER in which you produce the string, since we produced the tokens right to left
#             -----------------------VVVVVV--------------------
res = ''.join(''.join(x) for x in ops[::-1])

print(res)