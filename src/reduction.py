# Work Reduction
# https://open.kattis.com/problems/reduction
# TAGS: sorting
# CP4: 3.2b, Iterative (Two Loops), E
# NOTES:
T = int(input())
for testcase in range(1, T + 1):
    print("Case", testcase)
    N, M, L = map(int, input().split())
    xs = []
    for _ in range(L):
        name, x = input().split(':')
        minus_one, half = map(int, x.split(','))
        cost = 0
        n = N
        while n >= 2 * M and half < (n - n // 2) * minus_one:
            n //= 2
            cost += half

        cost += (n - M) * minus_one
        xs.append((name, cost))
    xs = sorted(xs, key=lambda x: (x[1], x[0])) # decreasing value, tiebreak on alphabetical
    for x in xs:
        print(*x)