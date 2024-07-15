# Moscow Dream
# https://open.kattis.com/problems/moscowdream
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
a, b, c, n = map(int, input().split())

print("YES" if n >= 3 and all(x > 0 for x in {a, b, c}) and a + b + c >= n else "NO")