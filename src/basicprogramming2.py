# Basic Programming 2
# https://open.kattis.com/problems/basicprogramming2
# TAGS: array, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
"""
t == 1 condition is that x+y = 7777 for 2 values x,y in the input array AND that x != y
But since 7777 is odd, it is impossible that x = y so no need to check anyway
Don't know if this is an intended "gotcha" or oversight O_o

Also the input N is max: 200_000
So you can't do naive 2-sum search over range i (0,N) and range j (i+1, N) in O(N**2) -> need to do O(N) 2-sum approach
"""
from collections import Counter

N, t = map(int, input().split())

xs = list(map(int, input().split()))

if t == 1:
    needed = set()
    flg = True
    for x in xs:
        if x in needed:
            print("Yes")
            flg = False
            break
        else:
            needed.add(7777 - x)
    if flg:
        print("No")
        
elif t == 2:
    print("Unique" if len(xs) == len(set(xs)) else "Contains duplicate") # N = 200_000, didnt need to optimize (ie iterating and stopping early if see a duplicate) it passed using set() approach

elif t == 3:
    c = Counter(xs)
    print(next((k for k, v in c.items() if v > (N / 2)), -1)) # implementation improve : should compare 2 * v > N for numerical stability
    
elif t == 4:
    xss = sorted(xs)
    l = len(xss)
    if l % 2 == 1:
        print(xss[(l - 1) // 2])
    else:
        print(xss[(l // 2) - 1], xss[l // 2])

elif t == 5:
    xss = sorted(xs)
    res = (x for x in xss if 100 <= x <= 999)
    print(' '.join(map(str, res)))