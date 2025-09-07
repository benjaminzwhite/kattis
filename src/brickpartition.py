# Bricks
# https://open.kattis.com/problems/brickpartition
# TAGS: greedy
# CP4: 0, Not In List Yet
# NOTES:
"""
This exercise has unclear wording and input format IMO, I think that's a partial reason why the difficulty rating is so high:

- **You must use all of the input letters** AFAICT
- The stuff about contiguous/nonempty/partition is so unclear about this. The BLOCKS must be mutually contiguous, not just the letters
within them (many different interpretations).

So reformulating exercise:

"You are given a string of B's and W's. You can freely place |'s in the string so long as all substrings in the resulting
arrangement all share the same, common, ratio of W:B. What is largest number of blocks you can form?"

The answer then is obvious:

Since you MUST ALWAYS USE ALL INPUT LETTERS, the "local" W:B ratio in each substring MUST BE THE SAME AS THE "TOTAL/global" W:B ratio over the entire string.

So express the **TOTAL** W:B ratio in lowest terms, then just greedy through the alternating ...W,B,W,B... counts:
as soon as you can "break off" a prefix which has the right W:B ratio -> do so, and continue (with the "head" color now adjusted
downwards by the amount used in the prefix, if there is some leftover)

e.g. **TOTAL** W:B ratio found to be 3:1. Then now go back to start of string:

WWW, BBBBB, W...
<---->
When you process B=5, you notice that B=1 would produce W=3,B=1; so continue with B=5-1 = 4 and continue on with this value:
WWW, B|BBBB, W....
<DONE> <---remaining--->

etc.

---

Implementation note

However you need to be careful with the implementation of this solution! In my code below, I left in comments my first implementation
that has a missing logic, and will get WA on some testcases (see the commented line with e.g. #acc_w += cnt).

I came up with testcases like this one:

6 B
6 W
7 B
8 W
5 B
7 W

My first submission code produced answer 2 on this testcase - specifically it updates +1 INCORRECTLY at the "5 B" step, since it:
[total W = 21 total B = 18, so GCD-> W=7 B=6]
has acc_b = 6+7+5 = 18 at this point
has acc_w = 6+8 = 14 at this point, 
and judges that therefore you can divided the 14 w evenly by 7 => q=2, and finds that there are indeed 2*6 = at least 12 B
in the preceding segments.

HOWEVER THIS IS WHERE THE SOLUTION IS INCORRECT AS NOTE THAT THE 12 B DO *NOT* OCCUR IN SUCH A WAY THAT YOU CAN FORM 
THE HYPOTHETICAL 14w12b BLOCK: 6B 6W 7B 8W would require that you skip 1st B or a B in the middle
while 6W 7B 8W 5B would require you to skip the entire first 6 B block.

-> So my first quick solution had bad logic: I assumed it was enough to simply rely on lookbehind cnt exact division properties.

-> How to fix this? it's basically a physical view/continuity argument that unlocks the correct solution:
You need to ensure that the "GOOD" interval, if it occurs, OCCURS SPECIFICALLY WITH THE ADDITION OF "this" NEW SEGMENT OF W/B elements.

To do this, you say "if it was NOT possible to form a balanced W:B ratio BEFORE adding current chars, but IS POSSIBLE AFTER adding current
chars, THEN SOMEWHERE IN THE MIDDLE THERE MUST HAVE BEEN THE EXACT W:B ratio required AND THIS OCCURED AT THE EARLIEST IN THE *CURRENT* NEWLY
ADDED block of chars"

-> In other words you need "ratio before adding curr W/B" to **undershoot** and ratio after adding curr W/B to **overshoot** (or vice versa)

---

Input format

Input format is annoying: multiple testcases, then instead of giving you the W and B count ahead of each testcase, you have to 
work through the inputs once to get this data (I spent a while thinking if you can do it without a first pass through but I don't see how?)

And even more annoying - you have the possibility of multiple lines being THE SAME COLOR CONSECUTIVELY like W 3, W 9, W 1, B 4

So you can't e.g. assume White is always in "i=even index" or whatever. I don't see what this adds to the exercise?

It would be so much simpler to say "all sequences start with White blocks" and give each sequence as 13 4 10 23 1 1 219 whatever.
"""
from math import gcd

T = int(input())
for _ in range(T):
    n = int(input())

    cnt_w = 0
    cnt_b = 0

    xs = []
    for _ in range(n):
        cnt, color = input().split()
        cnt = int(cnt)
        if color == "W":
            cnt_w += cnt
        else:
            cnt_b += cnt
        xs.append((cnt, color))

    # handle/avoid zero division errors when there are no W's or no B's
    if cnt_w == 0:
        print(cnt_b)
        continue
    if cnt_b == 0:
        print(cnt_w)
        continue

    g = gcd(cnt_w, cnt_b)

    #print(cnt_w, cnt_b)
    cnt_w //= g
    cnt_b //= g
    #print(cnt_w, cnt_b)

    res = 0
    acc_w = 0
    acc_b = 0
    for cnt, color in xs:
        if color == 'W':
        	# VVVVVVVVVVV See notes: my first approach has logic error, explained in notes
            #acc_w += cnt
            # You need to first check that the previous possible choice was "BAD"
            # and THEN you add the curr cnt, to see if you can overshoot back into "GOOD" territory
            q, r = divmod(acc_b, cnt_b)
            # check acc_b/acc_w > cnt_b/cnt_w BEFORE adding curr cnt to acc_w, so that there is the possiblity of
            # acc_b/(acc_w + cnt) to be <= cnt_b/cnt_w
            
            # Implementation best practice - avoid floats by checking: acc_b*cnt_w > cnt_b*acc_w
            if r == 0 and q > 0 and (acc_b * cnt_w > cnt_b * acc_w) and (acc_b * cnt_w <= cnt_b * (acc_w + cnt)):
                #print("updated at ",cnt,color, " q r cnt_w acc_w",q,r,cnt_w,acc_w)
                acc_b = 0
                acc_w -= q * cnt_w # will add += cnt later, outside of the if statement
                res += 1
            acc_w += cnt # NOW add it
        else:
        	# VVVVVVVVVVV See notes: my first approach has logic error, explained in notes
            #acc_b += cnt
            q, r = divmod(acc_w, cnt_w)
            if r == 0 and q > 0 and (acc_w * cnt_b > cnt_w * acc_b) and (acc_w * cnt_b <= cnt_w * (acc_b + cnt)):
                acc_w = 0
                acc_b -= q * cnt_b
                res += 1
            acc_b += cnt

    print(res)