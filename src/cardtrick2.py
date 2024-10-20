# Card Trick
# https://open.kattis.com/problems/cardtrick2
# TAGS: brute force
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
NOTES: just do the actual shuffles algorithmically - i.e. perform 1, then 2 then 3... swaps
each time appending head to tail of current list.
Once number of swaps is done, head element corresponds to res[head-1] = swaps

MUCH EASIER TO VISUALIZE IF YOU USE e.g. "ABCDE" on a piece of paper:

               A B C D E
                 B C D E A     after num_swaps = 1, head is now B so ace must FIRST (ie 1) APPEAR IN POSITION = POSITION B in ORIGINAL ABCDE LINE UP i.e position "B" "2" or "index 1" (2 -1 = 1 due to 0 based indexing)
                 ^____________ now remove B
                   C D E A
    do 2 swaps:      D E A C
              :        E A C D after num_swaps = 2, head is now E so ace must SECOND (ie 2) APPEAR IN POSITION "E" -> i.e. position 5/ index 4
 
etc. etc.
"""
T = int(input())

for _ in range(T):
    n = int(input())
    
    res = [None] * n
    xs = list(range(1, n + 1))
    
    for swaps in range(1, n + 1):
        for _ in range(swaps):
            xs = xs[1:] + [xs[0]]
        res[xs[0] - 1] = swaps # -1 because of 1-based counting
        xs = xs[1:]
    
    print(*res)