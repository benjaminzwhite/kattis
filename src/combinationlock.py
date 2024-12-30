# Combination Lock
# https://open.kattis.com/problems/combinationlock
# TAGS: logic
# CP4: 1.4i, Function
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/combinationlock.md
"""
while True:
    s, a, b, c = map(int, input().split())
    if s == a == b == c == 0:
        break

    # Step 1 means going from start, s, to a, and we are turning CLOCKWISE, SO SUBTRACT a FROM s
    # So e.g. if s=5 and a=35 we will click through 4,3,2,1,0,39,38,37,36,35//
    step1 = (s - a)
    if step1 < 0:
        step1 += 40 #e.g. if s=5 and a=35, step1 is 5-35 = -30, which corresponds to fact we turned 10 degrees

    # Step 2 means going from a to b, and we are turning CCW so we TAKE NEGATIVE of (a - b)
    step2 = - (a - b) # i.e. b-a
    if step2 < 0:
        step2 += 40

    # Step 3 is same as Step 1, go from b to c CLOCKWISE so subtract c from b
    step3 = (b - c)
    if step3 < 0:
        step3 += 40

    # In the steps above we are incremementing by 1/40th of 360 degrees i.e. 9 degrees
    # REMEMBER in all cases you will do 2*360 + 1*360 = 1080 due to 2 full turns clockwise and 1 full turn CCW
    res = 1080 + 9 * (step1 + step2 + step3)

    print(res)