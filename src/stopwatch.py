# Stopwatch
# https://open.kattis.com/problems/stopwatch
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
N = int(input())

if N % 2:
    print("still running")
    
else:
    prev, res = 0, 0
    while N:
        curr = int(input())
        if N % 2 == 1:
            res += curr - prev
        prev = curr
        N -= 1
    print(res)