# Monopoly
# https://open.kattis.com/problems/monopol
# TAGS: mathematics, probability
# CP4: 5.5a, Probability, Easier
# NOTES:
N = int(input())
targets = map(int, input().split())

sums = [1, 2, 3, 4, 5]
sums = [0, 0] + sums + [6] + sums[::-1]

res = sum(sums[t] for t in targets) / 36

print(res)