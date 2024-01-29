# Grading
# https://open.kattis.com/problems/grading
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
a, b, c, d, e = map(int, input().split())

n = int(input())

if n >= a:
    print('A')
elif n >= b:
    print('B')
elif n >= c:
    print('C')
elif n >= d:
    print('D')
elif n >= e:
    print('E')
else:
    print('F')