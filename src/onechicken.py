# One Chicken Per Person!
# https://open.kattis.com/problems/onechicken
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
"""
Reading comprehension/spelling:

print "pieces" vs "piece" when result == 1 (didn't notice this in testcases)
"""
N, M = map(int, input().split())

if N < M:
    print(f"Dr. Chaz will have {M - N} piece{'' if M == N + 1 else 's'} of chicken left over!")
else:
    print(f"Dr. Chaz needs {N - M} more piece{'' if N == M + 1 else 's'} of chicken!")