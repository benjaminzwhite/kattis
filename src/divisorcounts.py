# Divisor Counts
# https://open.kattis.com/problems/divisorcounts
# TAGS: mathematics, number theory, brute force
# CP4: 0, Not In List Yet
# NOTES:
N = int(input())

N_MAX = N + 5 # sentinel

res = [1] * N_MAX

for n in range(2, N_MAX):
    for i in range(n, N_MAX, n):
        res[i] += 1

for i in range(1, N + 1):
    print(res[i])