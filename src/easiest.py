# The Easiest Problem Is This One
# https://open.kattis.com/problems/easiest
# TAGS: brute force
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Reading comprehension:

CARE! p > 10, not >= 10

It's asking for next p > 10 such that sum_digits(N*p) == N
"""
while True:
    N = input()
    if N == '0':
        break
    
    target = sum(int(d) for d in N)
    N = int(N)
    p = 11 # p > 10 O_o
    while True:
        if sum(int(d) for d in str(N * p)) == target:
            print(p)
            break
        p += 1