# Code to Save Lives
# https://open.kattis.com/problems/codetosavelives
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
t = int(input())

for _ in range(t):
    a = ''.join(input().split())
    b = ''.join(input().split())
    
    res = int(a) + int(b)
    
    print(*str(res))