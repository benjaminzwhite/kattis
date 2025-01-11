# Sums
# https://open.kattis.com/problems/consecutivesums
# TAGS: mathematics, number theory, nice
# CP4: 5.3h, Working with PFs
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/consecutivesums.md
"""
T = int(input())

for _ in range(T):
    N = int(input())
    # N  =  a + (a+1) + (a+2) + (a+3) + ... + (a+b-1) = b * (a + (a+b-1)) // 2  = b * (2*a + b - 1)//2
    # so we try to look for:
    # 2*N = b * Q where Q = (2*a + b - 1)
    flg = True
    b = 2 # problem statement says need at least b=2 terms for expression to be valid (otherwise solution is trivial N = N, 1 term)
    while b * b <= 2 * N:
        if (2 * N) % b == 0:
            Q = (2 * N) // b
            # we have found b candidate - need to check the parity matching conditions (SEE NOTES ABOVE)
            if (Q % 2 == 1 and b % 2 == 0) or (Q % 2 == 0 and b % 2 == 1):
                a = (Q + 1 - b) // 2 # given the Q value above, solve for a to find the initial term of the arithmetic progression
                print(N, "=", ' + '.join(map(str, range(a, a + b)))) # print up to a+b-1 INCLUSIVE, so range up to a+b EXCLUSIVE
                flg = False
                break
        b += 1

    if flg:
        print("IMPOSSIBLE") # this should only print IMPOSSIBLE if N is a power of 2: {1,2,4,8,....}