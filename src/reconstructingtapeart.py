# Reconstructing Tape Art
# https://open.kattis.com/problems/reconstructingtapeart
# TAGS: array, stack, improve
# CP4: 9.cons, Construction
# NOTES:
"""
TODO: IMPROVE: is there a way to do it in a single pass ? I don't see how atm.

---

Here what we do is: first pass, get the leftmost and rightmost occurence of every color in the xs list

Then 2nd pass, basically do a stack-based {} [] () open close brackets type problem:

-> append the FIRST occurence representative of every color
-> dont need to append e.g. 3,3,3,3,3 just 3 which tracks that current left group is color 3
-> then, if you encounter an index which is known to be the RIGHTMOST occurence of a particular color,
   then the top of the stack MUST CONTAIN THAT SAME COLOR ALSO - if they match, then can pop the stk and have processed that color successfully
=> however if the stk top mismatches when you encounter the rightmost occurence of a color, then condition is impossible:
   e.g. with 1,2,1,2 this is what happens when you encouter the rightmost 1 color, the 2 on the stk has NOT been popped yet
"""
n = int(input())
xs = list(map(int, input().split()))

d = {}
for i, x in enumerate(xs, 1):
    if x not in d:
        d[x] = [i, i] # leftmost occurence stored in [0],  rightmost occurence stored in [1]
    else:
        d[x][1] = i # update rightmost occurence

stk = []
flg = True
for i, x in enumerate(xs, 1):
    if i == d[x][0]:
        stk.append(x)
    if i == d[x][1]:
        if stk[-1] == x:
            stk.pop()
        else:
            flg = False
            break

if flg:
    print(len(d))
    for k, v in d.items():
        print(*v, k)
else:
    print("IMPOSSIBLE")