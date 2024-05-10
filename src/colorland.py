# Colorland
# https://open.kattis.com/problems/colorland
# TAGS: array, greedy
# CP4: 4.4b, SSSP, BFS, Harder
# NOTES:
"""
It's always optimal to go as far as possible i.e. to the color which is furthest away 
i.e. to the color whose NEXT APPEARANCE is as far away (that is the rule, you can only go to next appearance of any of the colors)
Why? because there is a never a situation where an extra intermediate move allows you to make a better move later on:
e.g. imagine blue ..... blue ..... red yellow .... red  where here these are first appearances of the colors
if you go from ^ to  this ^ blue instead of going to yellow directly (which is the furthest "next appearance" of any of the colors)
then for this +1 move cost you HAVE NOT GOT ANY MOVES THAT YOU COULD NOT MAKE FROM YELLOW DIRECTLY (since if you can get to a cell from 
the 2nd blue location you can also get to it from the yellow location also).

---

Implementation notes:

I realised after submitting that AFAICT you don't need minheaps or anything, can just do with lists since the indexes are ALREADY IN ASCENDING ORDER.
I was overcomplicating: you just need for each color a list of its indexes [1,221,4414] etc. and then at each step of the
loop check the head of all the color lists, find the max of the heads, then delete from each color list until the
heads are all >= this curr value, then repeat until reach goal

Also, CARE! how you handle/interpret testcases with single entry
e.g. "Red" -> my original solution would return 0 but it seems that the correct/expected answer is 1, since you
are supposed to MOVE to Red (there is a "start cell" that you are on)
"""
from heapq import heappush, heappop

B, O, P, G, R, Y = [], [], [], [], [], []

# elif monstrosity not very DRY but it works O_o
N = int(input())
for i in range(N):
    x = input()
    if x == "Blue":
        heappush(B, i)
    elif x == "Orange":
        heappush(O, i)
    elif x == "Pink":
        heappush(P, i)
    elif x == "Green":
        heappush(G, i)
    elif x == "Red":
        heappush(R, i)
    elif x == "Yellow":
        heappush(Y, i)

cnt = 0
curr = 0
while curr < N - 1:
    for minheap in B, O, P, G, R, Y:
        if minheap:
            curr = max(curr, minheap[0])
    for minheap in B, O, P, G, R, Y:
        while minheap and minheap[0] <= curr:
            heappop(minheap)
    cnt += 1

if cnt == 0: # workaround for when input is just 1 cell, e.g. "Red", see Implementation Notes
    cnt += 1

print(cnt)