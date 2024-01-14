# Number Fun
# https://open.kattis.com/problems/numberfun
# TAGS: basic
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
"""
Basic optimisation/good practice:
can avoid using division by rearranging to multiplication
e.g. instead of checking a/b==c, check a==b*c etc
"""
N = int(input())

for _ in range(N):
    a, b, c = map(int, input().split())
    
    if a + b == c or abs(a - b) == c or a * b == c or b * c == a or a * c == b:
        print("Possible")
    else:
        print("Impossible")