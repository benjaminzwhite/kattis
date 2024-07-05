# Ones
# https://open.kattis.com/problems/ones
# TAGS: mathematics, number theory, brute force
# CP4: 5.3i, Modular Arithmetic
# NOTES:
"""
Can just brute force it "intelligently" O_o
(i.e. need to take sequence % n in the while loop otherwise numbers grow too big and TLE)
"""
import sys

for line in sys.stdin:
    sequence = 1 # 1,11,111,....
    cnt = 1
    n = int(line)
    while sequence % n != 0:
        cnt += 1
        sequence = (10 * sequence + 1) % n
    print(cnt)