# Final Exam
# https://open.kattis.com/problems/finalexam2
# TAGS: basic, array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
n = int(input())

prev = input()

res = 0

for _ in range(n - 1):
    curr = input()
    if curr == prev:
        res += 1
    prev = curr

print(res)