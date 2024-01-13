# GCVWR
# https://open.kattis.com/problems/gcvwr
# TAGS: basic
# CP4: 1.4a, I/O + Sequences Only
# NOTES:
G, T, N = map(int, input().split())

xs = map(int, input().split())

print(9 * ((G - T) // 10) - sum(xs))