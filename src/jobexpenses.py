# Job Expenses
# https://open.kattis.com/problems/jobexpenses
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
N = int(input())

res = -sum(x for x in map(int, input().split()) if x < 0)

print(res)