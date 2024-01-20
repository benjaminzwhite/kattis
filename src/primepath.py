# Prime Path
# https://open.kattis.com/problems/primepath
# TAGS: mathematics, bfs
# CP4: 8.7g, Graph+Other
# NOTES:
"""
Nice exercise.

The logic below is: 
- Precompute all 4 digit primes
- Then do BFS from start to end prime (use strings to be able to modify and work easily with a seen set())
- For each BFS step, pop current n then try all "adjacent" 4 digit primes (you have 4 possible digit locations and 10 possible digit values)
- For these 40 candidates, lookup which ones are indeed primes, then append those to the end of BFS dequeue.
"""
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

FOUR_DIGIT_PRIMES = {str(x) for x in range(1_000, 10_000) if is_prime(x)}

from collections import deque

def bfs_primes(n, target):
    q = deque([(n, 0)]) # tuple is curr_n, curr_cost
    seen = set()

    while q:
        curr_n, curr_cost = q.popleft()
        if curr_n == target:
            print(curr_cost)
            break
        if curr_n in seen:
            continue

        seen.add(curr_n)
        for i in range(4):
            for d in '0123456789':
                if (next_n := curr_n[:i] + d + curr_n[i + 1:]) in FOUR_DIGIT_PRIMES and next_n not in seen:
                    q.append((next_n, curr_cost + 1))


T = int(input())

for _ in range(T):
    n, target = input().split()
    bfs_primes(n, target)