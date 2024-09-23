# Snapper Chain (Hard)
# https://open.kattis.com/problems/snapperhard
# TAGS: binary
# CP4: 2.2h, Bit Manipulation
# NOTES:
"""
Submitted the "fast" solution (i.e. without explicitly updating the states via transition diagram) to the one with small values of n
since didn't realise you were supposed to do an actual simulation for the easy case (it's ranked as higher 2.7 difficulty than hard at 2.4 lol)

---

Compute the binary expansion of k e.g. k = 7 -> 111
for the on/off of the snappers. If the first n are all 1 then power can flow to device attached to n
CARE! need to zfill with 0's for cases where n > num of binary digits in k e.g. n=100 k = 3. 
e.g. in binary k=3 -> 11 but there are only n' = 2 units here, the 100-98 others are 0 so power does NOT reach n=100 location
"""
T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    b = bin(k)[2:].zfill(n)[-n:]
    if all(d == '1' for d in b):
        print(f"Case #{test_case}: ON")
    else:
        print(f"Case #{test_case}: OFF")