# Golomb Rulers
# https://open.kattis.com/problems/golombrulers
# TAGS: array, brute force
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
import sys

for line in sys.stdin:
    xs = list(map(int, line.split()))
    seen = set()
    l = len(xs)
    M = max(xs)
    flg = True

    for i in range(l):
        for j in range(i + 1, l):
            curr = abs(xs[i] - xs[j])
            if curr in seen:
                if flg:
                    print("not a ruler")
                flg = False
                break
            else:
                seen.add(curr)

    if flg:
        if len(seen) == M:
            print("perfect")
        else:
            print("missing", ' '.join(str(x) for x in range(1, M + 1) if x not in seen))