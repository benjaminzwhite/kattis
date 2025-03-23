# Semi-prime H-numbers
# https://open.kattis.com/problems/hnumbers
# TAGS: mathematics, number theory, brute force, improve
# CP4: 8.7j, Other+DP 1D RSQ/RMQ
# NOTES:
"""
TODO: IMPROVE: I solved this just via "brute force" basically. 

Not sure if there is a better way, using the 4n+1 decomposition for ex.

---

Multiply all numbers of the form 4n+1 by those of the form 4m+1; let p be the result of this multiplication

Then set WAYS[p] = 1 the first time this product is reached.

If p can be reached a second time, then p is NOT A SEMIPRIME, so assign dummy value like 999 or whatever.

Finally, "accumulate" (ACC below) the entire WAYS[] list, with the following rule:
anytime you see a WAYS == 1 value, then the corresponding i is a semiprime, so += 1 the ACC and continue etc.
"""
import sys

N_MAX = 10**6 + 123 # 123 is sentinel value

# count all ways that i can be written as numbers of the form 4n+1 * 4m+1
# if WAYS == 0 it is a prime, if WAYS == it is a semiprime, anything more than 1 -> not a semiprime
WAYS = [0] * N_MAX
for fst in range(5, N_MAX, 4):
    for snd in range(fst, N_MAX, 4):
        p = fst * snd
        if p > N_MAX:
            break
        elif WAYS[fst] > 0 or WAYS[snd] > 0:
            WAYS[p] = 999 # dummy value
        else:
            WAYS[p] = 1

ACC = [0] * N_MAX
for i, x in enumerate(WAYS[1:], 1):
    ACC[i] = ACC[i - 1] + int(x == 1)
    
for line in sys.stdin:
    n = int(line)
    if n != 0:
        print(n, ACC[n])