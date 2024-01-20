# Stacking Cups
# https://open.kattis.com/problems/cups
# TAGS: basic, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
N = int(input())
ts = []

for _ in range(N):
    a, b = input().split()
    if a.isdigit():
        ts.append((b, int(a) // 2))
    else:
        ts.append((a, int(b)))

for t in sorted(ts, key=lambda x:x[1]):
    print(t[0])