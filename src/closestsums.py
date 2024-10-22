# Closest Sums
# https://open.kattis.com/problems/closestsums
# TAGS: array, sliding window
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
I had some problems with the input format so coded each condition separately to debug, when in the end it was
just about taking the multiline inputs correctly O_o

Use l,r sliding indices to find a two-sum that is closest to target
-> need to take care to avoid "infinte loops": I create a seen set() because it avoids cycling if e.g. 2 values are 
   either side of target: e.g. [1,10,100] and target is 50 -> will oscillate between (0,2) and (0,1) infinitely

ALSO YOU CAN'T USE THE SAME ELEMENT TWICE, hence lots of l != r conditions; I think some are not necessary but I have them leftover from debugging
"""
case_number = 0

while True:
    try:
        n = int(input())
        case_number += 1
        print(f"Case {case_number}:")
        xs = []
        for _ in range(n):
            xs.append(int(input()))
        xs = sorted(xs)
        
        m = int(input())
        for _ in range(m):
            query = int(input())
            l, r = 0, len(xs) - 1
            res = float('inf')
            seen = set()
            
            while l < r and (l, r) not in seen:
                seen.add((l, r))
                guess = xs[l] + xs[r]
                if l != r and abs(query - guess) < abs(query - res):
                    res = guess
                
                if l != r and guess == query: # we can't improve result since we have exact match so break early
                    break
                elif guess > query:
                    r -= 1
                elif guess < query:
                    l += 1
            print(f"Closest sum to {query} is {res}.")
    
    except EOFError: # input format workaround O_o
        break