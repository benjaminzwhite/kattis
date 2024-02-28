# Meow Factor
# https://open.kattis.com/problems/meowfactor
# TAGS: mathematics, number theory
# CP4: 5.3k, Divisibility Test
# NOTES:
"""
Just iterate downwards from max possible value of a, so that as soon as you find a
value that satisfies n % a**9 == 0 you know it's the max value.
"""
n = int(input())

upper_range = int(n ** (1 / 9) + 1)

for a in range(upper_range, 0, -1):
    if n % a**9 == 0:
        print(a)
        break