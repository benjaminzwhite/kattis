# Bus Numbers
# https://open.kattis.com/problems/busnumbers2
# TAGS: mathematics, number theory, brute force
# CP4: 8.7c, Fast DS+Other, Easier
# NOTES:
N_MAX = 400_001
PRECOMPUTE = [0] * N_MAX

# N_MAX**(1/3) = 73.6
# Also, take inner loop from i + 1 which ensures that j > i so we DON'T double count
# e.g. don't double count: 5**3 + 2**3 and 2**3 + 5**3 as distinct ways
for i in range(1, 74):
    for j in range(i + 1, 74):
        tmp = i**3 + j**3
        if tmp < N_MAX:
            PRECOMPUTE[tmp] +=1

m = int(input())

res = next((i for i in range(m, -1, -1) if PRECOMPUTE[i] >= 2), "none")

print(res)