# Is It Even?
# https://open.kattis.com/problems/isiteven
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
"""
If you want product of all x_i's to be divisible by 2**K then check for each individual x_i the max k such that x_i % 2**k == 0

Sum these individual values of k -> this gives you the divisibility of x1*x2*x3... by the big 2**K
"""
N, K = map(int, input().split())

curr_seen_k = 0 # <-- by the end we want this to be >= K so that product of all x_i's is divisible by 2**K

for _ in range(N):
    x = int(input())
    while x % 2 == 0:
        x //= 2
        curr_seen_k += 1

# can print(bool(curr_seen_k >= K)), just left like this for clarity what the output format is O_o
if curr_seen_k >= K:
    print(1)
else:
    print(0)