# Electrical Outlets
# https://open.kattis.com/problems/electricaloutlets
# TAGS: logic
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
All strips, except the "last one" (W.L.O.G), have effectively -1 available outlet since
there will be some other strip that needs to plug into it.

So, for each strip, the contribution is: size_of_strip - 1
except for the last one which is size_of_strip

So total is - for k strips:

sum( (size_1 -1 ) + (size_2-1) + (size_3 - 1) + ... (size_k-1 - 1) + (size_k -1 + 1) )

where the last/k_th strip has -1 + 1 shown for clarity.

So the answer is just, after rearranging, the sum of all strip sizes, plus k times -1, plus +1.
"""
N = int(input())

for _ in range(N):
    k, *xs = map(int, input().split())
    print(sum(xs) - k + 1)