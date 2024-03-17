# Guess the Number
# https://open.kattis.com/problems/guess
# TAGS: binary search
# CP4: 9.inte, Interactive Problem
# NOTES:
"""
First interactive exercise on Kattis: you respond to the result from each input() call
"""
lo, hi = 1, 1000

while True:
    mid = (lo + hi) // 2
    print(mid)
    response = input()
    if response == "lower":
        hi = mid
    elif response == "higher":
        lo = mid + 1
    elif response == "correct":
        break