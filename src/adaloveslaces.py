# Ada Loveslaces
# https://open.kattis.com/problems/adaloveslaces
# TAGS: recursion, combinatorics, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/adaloveslaces.md
"""
N, d, s, t, fmin, fmax = map(int, input().split())

# -- PRECOMPUTE --

PRECOMPUTE = []

# NOTE: the recursive calculations are based on "one half" of the pattern.
# I will 2x this length and also add the initial --- horizontal part
# as part of the base case when I reach the final position, N.

def precompute(N, d, s, t):
    
    can_use = [False] + [True] * N # 1 based indexing so 0 is just a dummy position for ease of indexing

    def go(position=1, curr_len=0): # default position 1 and curr_len = 0 to start the go() call
        if position == N:
            # base case: we have reached a valid lacing pattern that ends at position N
            # ==> Store the exact length to lace this unique pattern 
            # i.e. the entire length, up to position N.
            # We need to add (s + 2*t) which is due to the length ----- across the top, and the eyelets at position 1
            # Also multiply curr_len twice (by mirror symmetry) since so far we are accounting for one side of the pattern
            exact_length = 2 * curr_len + (s + 2 * t)
            
            PRECOMPUTE.append(exact_length)

        # Recursive case: we select this position, so it cannot be used anymore
        can_use[position] = False
        
        # Recursive case: 1) try all valid crossing side X patterns:
        for other_pos in range(1, N + 1):
            if can_use[other_pos]:
                go(other_pos, curr_len + ((d * abs(other_pos - position))**2 + s**2)**0.5 + t) # CARE!! the hypothenuse is determined by d*delta_position
        
        # Recursive case: 2) ALSO: try all valid adjacents on same side - can only move to position +/- 1 on same side:
        if position + 1 <= N and can_use[position + 1]:
            go(position + 1, curr_len + d + t)
        if position - 1 >= 1 and can_use[position - 1]:
            go(position - 1, curr_len + d + t)

        # Recursive case: relax use of this position
        can_use[position] = True

    go()

precompute(N, d, s, t)

PRECOMPUTE.sort()
# -- END PRECOMPUTE --


# -- QUERIES --

while True:
    try:
        q = int(input())
        cnt = 0
        # PRECOMPUTE is sorted so can continue/break early for invalid ranges
        for exact_length in PRECOMPUTE:
            if q > (exact_length + 2 * fmax):
                continue
            elif q < (exact_length + 2 * fmin):
                break
            else:
                cnt += 1
        print(cnt)
    except:
        break