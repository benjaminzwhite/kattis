# Happy Happy Prime Prime
# https://open.kattis.com/problems/happyprime
# TAGS: brute force, mathematics
# CP4: 5.6a, Cycle Finding
# NOTES:
def is_prime(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return n > 1

def is_happy(n):
    seen = set()
    while (n not in seen) and (n != 1):
        seen.add(n)
        n = int(sum((d * d) for d in map(int, str(n))))
    return n == 1

P = int(input())

for _ in range(P):
    K, m = map(int, input().split())
    if is_prime(m) and is_happy(m):
        res = "YES"
    else:
        res = "NO"
    print(K, m, res)