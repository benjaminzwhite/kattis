# I Can Guess the Data Structure!
# https://open.kattis.com/problems/guessthedatastructure
# TAGS: data structure
# CP4: 2.3a, Priority Queue
# NOTES:
"""
- used try/except for input handling as unknown number of testcases (was early solve on Kattis OJ, getting used to I/O)

- the core logic is to use an boolean array of length 3, RES, which stores whether q, stk, h are consistent with the given inputs respectively
"""
from collections import deque
from heapq import heappush, heappop

while True:
    try:
        n = int(input())
        q, stk, h = deque([]), [], []
        RES = [True, True, True] # RES stores whether q, stk, h are consistent with the given inputs respectively
        flg = True # flg is for if we break early due to impossible operation on the datastructures
        to_process = []
        
        for _ in range(n):
            op, x = map(int, input().split())
            to_process.append((op, x))

        for tpl in to_process:
            op, x = tpl
            
            if op == 1:
                q.append(x)
                stk.append(x)
                heappush(h, -x) # MAX HEAP IS ASKED FOR, NOT MIN HEAP
            elif op == 2:
                if not stk:
                    # all 3 DS have same len so check they have elements by refering to the stack W.L.O.G.
                    print("impossible")
                    flg = False
                    break
                    
                qx = q.popleft()
                sx = stk.pop()
                hx = abs(heappop(h)) # NB TAKE abs SINCE HEAPPUSHED NEGATIVE x DUE TO PYTHON MAX HEAP
                
                for i, x_ in enumerate([qx, sx, hx]):
                    RES[i] = RES[i] & (x == x_) # if the observed x is == to qx, sx, hx respectively, then we AND true & true -> true. However if observed x != x_, then the corresponding data structure is NOT consistent so we AND true & false -> false, which will stay false forever now on

        if flg: # flg is False if we encountered an impossible operation already
            if sum(RES) == 0:
                print("impossible")
            elif sum(RES) > 1:
                print("not sure")
            else:
                if RES[0]:
                    print("queue")
                elif RES[1]:
                    print("stack")
                else:
                    print("priority queue")

    except EOFError:
        break