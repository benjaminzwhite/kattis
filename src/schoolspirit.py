# School Spirit
# https://open.kattis.com/problems/schoolspirit
# TAGS: array
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
n = int(input())

xs = [int(input()) for _ in range(n)]

def get_score(xs):
    res = 0.2 * sum(x * (0.8)**i for i, x in enumerate(xs))
    return res

before = get_score(xs)
removeds = 0
for i in range(n):
    removeds += get_score(xs[:i] + xs[i+1:])

print(before)
print(removeds / n)