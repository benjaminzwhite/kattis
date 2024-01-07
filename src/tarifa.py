# Tarifa
# https://open.kattis.com/problems/tarifa
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
X = int(input())
N = int(input())

res = X

for _ in range(N):
    res += (X - int(input()))

print(res)