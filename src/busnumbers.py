# Bus Numbers
# https://open.kattis.com/problems/busnumbers
# TAGS: array
# CP4: 2.3c, DAT, Others
# NOTES:
N = int(input())

xs = sorted(map(int, input().split())) + [-1] # dummy to ensure we process last element (since -1 will never continue a contig sequence of x,x+1,x+2...)

prev = xs[0]
cnt = 1
res = []

for i, x in enumerate(xs[1:], 1): # NB the indexing in enumerate since we have already initialized with prev = xs[0] and 0th element in xs treated
    if x == prev + 1:
        cnt += 1
    else:
        if cnt > 2:
            res.append(f"{prev - cnt + 1}-{prev}")
        else:
            res.extend(str(x) for x in xs[i - cnt:i])
        cnt = 1
    prev = x

print(' '.join(res))