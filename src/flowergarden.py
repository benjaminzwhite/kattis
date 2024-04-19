# Flower Garden
# https://open.kattis.com/problems/flowergarden
# TAGS: geometry
# CP4: 5.3b, (Prob) Prime Testing
# NOTES:
"""
Implementation note after re-reading:

Adding 0 to PRIMES to handle the case where res < 2 in the next(...) call is bad practice, should
just use next((...), 0) which handles the case where next() results in StopIteration 
"""
PRIMES = [0] # add 0 to list so handle the edge case where res < 2
for n in range(2, 20_000 + 1):
    if all(n % d != 0 for d in range(2, int(n**0.5) + 1)):
        PRIMES.append(n)

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())

    locs = [(0, 0)]
    for _ in range(N):
        x, y = map(int, input().split())
        locs.append((x, y))

    total_dist = 0
    flowers = 0
    for (x, y), (x_, y_) in zip(locs, locs[1:]):
        total_dist += ((x - x_)**2 + (y - y_)**2)**0.5
        if total_dist > D:
            break
        flowers += 1

    res = next(p for p in PRIMES[::-1] if p <= flowers) # 2263 primes <= 20_000, so ok to search T=10 times 2263 linearly O_o
    
    print(res)