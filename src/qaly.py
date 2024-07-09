# Quality-Adjusted Life-Year
# https://open.kattis.com/problems/qaly
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
N = int(input())

res = 0

for _ in range(N):
    x, y = map(float, input().split())
    res += x * y
    
print(res)