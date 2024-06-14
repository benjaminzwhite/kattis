# Expeditious Cubing
# https://open.kattis.com/problems/expeditiouscubing
# TAGS: brute force
# CP4: 0, Not In List Yet
# NOTES:
"""
There are more efficient ways rather than resorting xs + [n] up to
2000 times, but this brute force approach passes OK in Python
"""
xs = map(float, input().split())
target = float(input())

xs = [round(x * 100) for x in xs]
target = round(target * 100)

xs = sorted(xs)

if sum(xs[1:]) <= 3 * target:
    print("infinite")
elif sum(xs[:3]) > 3 * target:
    print("impossible")
else:
    for n in range(2000, 0, -1):
        if sum(sorted(xs + [n])[1:4]) <= 3 * target:
            print(f"{n / 100:.2f}")
            break