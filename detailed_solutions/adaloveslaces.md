# Detailed solution for Kattis - Ada Loveslaces

[Problem statement on Kattis](https://open.kattis.com/problems/adaloveslaces)

This is a really interesting recursive/combinatorial generation problem. I ended up solving it in 2 different ways - the first approach is recursive, the second is combinatorial (I've included both solutions consecutively on this page).

---

**IMPORTANT: I noticed after writing my solution notes that I label the eyelets from `1 -> N` on BOTH sides of the shoe, while the problem author uses `0,2,4...` and `1,3,5,...` for the left and right side for a total of `2 * N` positions. Hopefully this does not cause too much confusion (I think mine is much clearer - you can think of my labelling of positions as e.g. `1 right`, `6 left` etc.)**

---

Note (see code where this comment will become clearer):

While solving I noticed that it also - in Python at least - requires a performant solution as the input sizes have up to 100 `L` queries, and `N` can be up to `9`. I found that for the `N = 9` case there are `64069` possible length values, which would mean possibly up to `100 * 64069` queries. So you can't just naively re-compute every query one by one, instead I do the following precomputation:

1. precompute once **all** valid `exact_lengths` that can be obtained for the given `N`
2. sort this list, call it `PRECOMPUTE`
3. now for the queries, each with a different query on `l` i.e. how many lengths can fit given the 'tolerances' `fmin` and `fmax`, you can go through `PRECOMPUTE`: from smallest to largest `exact_length`, each `exact_length` determines a range given by: `exact_length + 2*fmin <= l_query_value <= exact_length + 2*fmax`, and you can further therefore optimize this step by breaking early once the `exact_lengths` are too big for the lower bound to hold. You could also binary search twice (the upper and lower range values) for further performance optimization if there were more tests with `N` very large also.

## Tags

recursion, combinatorics

## Solution - first approach, recursive

Note that the problem is using 1-based indexing (first eyelet is `1`, and last is `N`).

For solving, it's easier to focus on a single "half" of the lacing pattern and we will multiply this by 2 to account for the "other side" once we reach a valid pattern. We also ignore the distance `s` between the eyelets at position 1, and the the thickness of these 2 eyelets at position 1. So later, we will need to add a total length of `s + 2*t` in our code, corresponding to the length of the initial configuration.

The recursive logic is as follows: Starting at position `1`, we can either go to any available eyelet on the "opposite" side of where we are, or we can go to an available eyelet at position +1 or -1 on the "same" side as where we are.

When we move to the opposite side, we add a total length given by the hypothenuse distance `d * abs(other_pos - position))**2 + s**2)**0.5` plus another `t` due to adding a new eyelet.

When we move to a position +1 or -1 on the same side, we add a total length given simply by `d` plus another `t` due to adding a new eyelet.

The base case for the recursive function is when we reach position `N`. At this point (see comment above) we need to remember to multiply whatever the `current_length` of laces is by `2` (since we have been focusing on only one "half" of the lacing pattern) and also then add a total length of `s + 2*t` (this is due to my implentation of not initializing the length to `s + 2*t` corresponding to the laces being initially horizontally threaded across eyelets at position `1`.

The recursive call needs to track which positions are usable - I call this array `can_use` in code below; note that due to 1-based indexing I create a dummy 0th entry in the array for convenience.

Once you recursively generate all possible patterns and their `exact_lengths`, for a given query you then just count how many patterns have an `exact_length` that satisfies the inequality.


## AC code - first approach, recursive

```python
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
```

## Solution - second approach, combinatorial

You can also generate all the possible lacing patterns combinatorially. In what follows, everything else is as before as in the previous section; I'll focus on the combinatorial logic.

The idea is to try all possible patterns of the form `1 | any permutation of any subset of the numbers {2,3,...,N-1} | N`.

**Note: it is important to note that a single pattern, such as `1 | 6 3 4 | 7` may have MULTIPLE "interpretations" when viewed as a lacing pattern.** For example in the above, you can only move from position `4 -> 7` by going "across" since the distance `7 - 4 == +3` is not equal to `+/- 1`. However, the move from position `3 -> 4` could be **either** an "across" move, **or a "same-side" +1 move.** The walkthrough below should make these 2 cases clearer.

If say `N = 9`, then a lace pattern is combinatorially obtained as follows:

- You must have start with `1` and end with `N=9` in the pattern.
- You can have *any number* of additional terms i.e. these are the "intermediate positions" between `1` and `9` that are used.
- For each choice of additional terms e.g. `1| {2,4,5} | 9` you can **permute the middle part** in all possible ways.

For each such final sequence obtained, **you may be able to interpret the pattern in more than one way:**

E.g. for a final sequence `1 | 2 5 4 | 9` then picturing the lace being threaded pairwise from `1 -> 2` then `2 -> 5` then `5 -> 4` then `4 -> 9`:

1. you can **always** interpret any pair as doing an "across move". This corresponds to the left/right positions in the pair being on opposite sides of the shoe. For example, `2 -> 5 : across` means going from position `2` on one side of shoe to position `5` on the other side. 
2. you can **sometimes** interpret a pair as doing a "same-side move". This corresponds to the left/right positions in the pair being on **the same side** of the shoe. **You can only interpret a pair this way if the values are within +/-1 of each other** so for our current example, only the pairs `1 -> 2` and `5 -> 4` could be interpreted in the 2 possible ways.

Finally, for all possible patterns and all possible interpretations of each pattern, you can compute the lengths that it produces and add these to your `PRECOMPUTE` list as we did previously for the recursive approach.

---

As a full worked example, with `N=3` there are only two possible combinatorial patterns (draw them to be 100% clear):

The pattern `1 | | 3` with no intermediate positions. This has only 1 valid interpreation:
- 1 cross to 3

The other pattern `1 | 2 | 3` which uses `2` as an intermediate position. This has 4 interpretations:
- 1 same-side to 2, then 2 same-side to 3
- 1 same-side to 2, then 2 cross to 3
- 1 cross to 2, then 2 same-side to 3
- 1 cross to 2, then 2 cross to 3



## AC code - second approach, combinatorial

```python
from itertools import combinations, permutations

N, d, s, t, fmin, fmax = map(int, input().split())

# -- PRECOMPUTE --

COMB_PRECOMPUTE = []

# starting at position 1 and ending at N:
# can choose to visit from 0 up to N-2 of the possible intermediate positions in between these 2 positions
for intermediate_positions in range(0, N-2 + 1):
	# select the subset of intermediate_positions that will be used in the current batch of patterns
	for comb in combinations(range(2, N), intermediate_positions):
		# permute the intermediate positions between 1 and N in all possible ways -> this corresponds to generating
		# all possible valid paths through the current list of positions
		# CARE! at this point we are generating the patterns of numbers, we are NOT "interpreting" them yet.
		# so for example pattern 1 | 2 5 4 | 9 will appear but this will corresponds to several actual lacing patterns ...
		for p in permutations(comb):
			pattern = [1] + list(p) + [N] # this is now something like:  1 | 2 5 4 | 9
			res = [0] # res will contain all the partial lengths
			# ... work out all "interpretations" of the pairs in this pattern e.g. 1 | 2 5 4 | 9 see in the NOTES how this should be parsed
			for fst, snd in zip(pattern, pattern[1:]):
				tmp = []
				# 1) you can **always** interpret any pair as doing an "across move"
				tmp.extend((((d * abs(fst - snd))**2 + s**2)**0.5 + t + x) for x in res ) # x in res are all the partial lengths, up to this position 

				# 2) you can **sometimes** interpret a pair as doing a "same-side move", ONLY if the 2 positions are ADJACENT
				if abs(fst - snd) == 1:
					tmp.extend((x + d + t) for x in res) # x in res are all the partial lengths, up to this position

				res = tmp # update res - now is the lengths of all partial lengths up until this position with this latest position (i.e. snd) included
			COMB_PRECOMPUTE.extend(res)

PRECOMPUTE = sorted(2*x + s + 2*t for x in COMB_PRECOMPUTE) # add the ---- length, s, and the 2*t eyelets at position 1
# -- END PRECOMPUTE --


# -- QUERIES --
while True:
    try:
        q = int(input())
        cnt = 0
        # PRECOMPUTE is sorted so can continue/break early for invalid ranges
        for exact_length in PRECOMPUTE:
            if q > (exact_length + 2*fmax):
                continue
            elif q < (exact_length + 2*fmin):
                break
            else:
                cnt += 1
        print(cnt)
    except:
        break
```