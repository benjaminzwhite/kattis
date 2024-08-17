# Beat The Spread!
# https://open.kattis.com/problems/beatspread
# TAGS: basic
# CP4: 1.6f, Real Life, Medium
# NOTES:
n = int(input())

for _ in range(n):
    s, d = map(int, input().split())
    a = (s + d) / 2
    b = s - a
    if (a < 0) or (b < 0) or (int(a) != a) or (int(b) != b):
        print("impossible")
    else:
        print(f"{int(a)} {int(b)}")