# Detailed Differences
# https://open.kattis.com/problems/detaileddifferences
# TAGS: basic
# CP4: 6.2e, String Comparison
# NOTES:
N = int(input())

for _ in range(N):
    s1 = input()
    s2 = input()
    print(s1)
    print(s2)
    print(''.join('*' if c1 != c2 else '.' for c1, c2 in zip(s1, s2)))
    print()