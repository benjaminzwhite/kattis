# Snakes and Masters
# https://open.kattis.com/problems/snakesandmasters
# TAGS: mathematics, recurrence
# CP4: 5.4a, Fibonacci Numbers
# NOTES:
N = int(input())

a, b = 1, 1

for _ in range(N - 1):
    a, b = b, (a + b) % 10**6

print(b)