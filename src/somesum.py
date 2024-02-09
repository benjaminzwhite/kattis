# Some Sum
# https://open.kattis.com/problems/somesum
# TAGS: mathematics, number theory, basic, proof
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
You can brute force with the small input size, but here is an analytical solution:

Any block of 4 consecutive integers contains 2 evens and 2 odds, so the sum must be EVEN.
Any block of 2 consecutive integers contains 1 even and 1 odd, so the sum must be ODD.

A block of 1 or 3 consecutive integers may contains either more evens or more odds
depending on the first number in the sequence:
e.g. 3,4,5 has two odds, vs 4,5,6 which has two evens.

So in general: 

If N can be split into blocks of size 4 then sum must be EVEN.
(e.g. N=8 will always look like: 6,7,8,9|10,11,12,13 which is 2 blocks of size 4, each of which sums to an even number, so sum is EVEN also).

If N can be split into blocks of size 4, with exactly 1 block of size 2 leftover, then sum must be ODD.
(e.g. N=10 will always look like: 6,7,8,9|10,11,12,13|14,15 and sum is odd because first 2 blocks sum to even, but last remaining block 14+15 will be odd)

Finally, anything else could be either EVEN or ODD.
"""
N = int(input())

if N % 4 == 0:
    print("Even")
elif N % 4 == 2:
    print("Odd")
else:
    print("Either")