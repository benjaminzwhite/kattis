# Silver Star Stands Alone
# https://open.kattis.com/problems/silverstarstandsalone
# TAGS: mathematics, number theory, dynamic programming
# CP4: 0, Not In List Yet
# NOTES:
"""
Build the dp array incrementally:
- there is 1 path that ends at prime=2 intially (which is at index 0 in the PRIMES list and will therefore give dp[0] = 1)
- then for all subsequent primes, add up how many paths end at all previous primes, subject to the condition that the previous prime is within distance 14
  (the 14 is because that's the exercise requirement O_o) 
"""
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]

dp = [0] * len(PRIMES)
dp[0] = 1

for j in range(1, len(PRIMES)):
    for i in range(j):
        if PRIMES[j] - PRIMES[i] <= 14:
            dp[j] += dp[i]

n = int(input())

res = dp[PRIMES.index(n)]

print(res)