# Envious Exponents
# https://open.kattis.com/problems/enviousexponents
# TAGS: binary, nice
# CP4: 8.7k, Three++ Components, E
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/enviousexponents.md
"""
n, k = map(int, input().split())

n += 1

while (DIY_n_bit_count := bin(n).count('1')) != k:
    if DIY_n_bit_count > k:
        val_of_rightmost_set_bit = (n & ~(n - 1))
        n += val_of_rightmost_set_bit
    else:
        n = (n | (n + 1))

print(n)