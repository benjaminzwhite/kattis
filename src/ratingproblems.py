# Rating Problems
# https://open.kattis.com/problems/ratingproblems
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
n, k = map(int, input().split())

S = 0
for _ in range(k):
    S += int(input())

print((S - 3 * (n - k)) / n, (S + 3 * (n - k)) / n )