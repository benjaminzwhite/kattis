# Candy Division
# https://open.kattis.com/problems/candydivision
# TAGS: mathematics
# CP4: 2.3g, Balanced BST (set)
# NOTES:
n = int(input())

fwd, back = [], []

for d in range(1, int(n ** 0.5) + 1):
    if n % d == 0:
        fwd.append(d - 1)
        back.append(n // d - 1)

# avoid double printing d and n//d if n is a perfect square e.g. otherwise for n=25 will get [1, 5] and [25,5] as the forward and backward lists (well, [0,4] [24,4] since you put d-1 rather than d)
if (fwd[-1] + 1) ** 2 == n:
    fwd.pop()

print(*fwd, *back[::-1])