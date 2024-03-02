# Trip Odometer
# https://open.kattis.com/problems/tripodometer
# TAGS: dict
# CP4: 2.3d, Hash Table (set)
# NOTES:
N = input()
xs = list(map(int, input().split()))

S = sum(xs)

tmp = []
for x in xs:
    tmp.append(S - x)

res = set(tmp)

print(len(res))
print(*sorted(res))