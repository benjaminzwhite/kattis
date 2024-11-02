# Islands in the Data Stream
# https://open.kattis.com/problems/islands
# TAGS: brute force, improve
# CP4: 3.2g, Try All Answers
# NOTES:
"""
TODO: IMPROVE: I just brute force O(n**2) over the inputs (can't think of a linear solution atm)

I used variable name "left and right BOOKENDS" to emphasize that we are placing these indices "OUTSIDE" of the range/island under consideration

e.g.          1 8 9 7 8 9 9 9 2
left_bookend__^               ^____ right_bookend

In the above example, the left and right are currently positioned so that they define a "island candidate" [8,9,7,8,9,9,9]
For each such island candidate, we += cnt if it is valid I.E. if ALL ITS ELEMENTS ARE > left AND right bookend values
"""
P = int(input())

for _ in range(P):
    k, *xs = map(int, input().split())
    xs = list(xs) # not needed actually
    cnt = 0
    for left_bookend in range(12):
        for right_bookend in range(left_bookend + 2, 12): # +2 relative to left_bookend since this ensure that Island Candidates have length AT LEAST 1
            if xs[left_bookend] < min(xs[left_bookend + 1:right_bookend]) > xs[right_bookend]:
                cnt += 1
    print(k, cnt)